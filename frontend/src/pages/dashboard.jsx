import {useCallback, useEffect, useRef, useState} from "react";
import { back_service } from "@/api/main.jsx";
import { useAuth } from "@/context/auth.jsx";
import { useNavigate } from "react-router-dom";
import { Item } from "@/components/item.jsx";
import { Search } from "@/components/utils/search.jsx";
import {ItemUserCount} from "@/components/dashboard/item_user_count.jsx";


const DashSearchItem = ({data}) => {
    return <Item id={data.id} name={data.name} />
};


export const DashboardPage = () => {
    const navigate = useNavigate()
    const { user, check_auth } = useAuth()
    const [items, set_items] = useState([])
    const [user_items, set_user_items] = useState([])
    const [groups, set_groups] = useState([])

    const timerRef = useRef(null);

    // Если у пользователя нет никакого ника, перенаправляем на страницу авторизации
    if (user.nick === null) {
        navigate('/auth/user')
    }

    // Получаем данные о всех предметах и предметах пользователя
    useEffect(() => {
        const fetch_data = async () => {
            if (user.nick === null || user.nick === undefined) {
                await check_auth()
            }
            set_items(await back_service.items.all({skip_: 0, limit_: 10000}))
            set_user_items(await back_service.users.user_items(user.nick))
            set_groups(await back_service.groups.items(user.nick));
        }
        fetch_data()
    }, [])

    // Добавляем предмет пользователю
    const handle_user_select_item = (item) => {
        set_user_items([...user_items, {...item, count: 1}])
    }

    // Обновляем количество предмета пользователя
    const handleQuantityChange = (itemId, newQuantity) => {
        if (newQuantity > 0) {
            set_user_items(user_items.map(item =>
                item.id === itemId
                    ? { ...item, count: newQuantity }
                    : item
            ));
        }
    };

    // Удаляем предмет пользователя
    const handleRemove = (itemId) => {
        set_user_items(user_items.filter(item => item.id !== itemId));
    };

    // Храним выбранные предметы
    const userItemsRef = useRef(user_items)
    useEffect(() => {
        userItemsRef.current = user_items;
    }, [user_items]);
    const [is_sync, set_is_sync] = useState(false);

    const fetch_user_data = useCallback(async () => {
        if (is_sync) return;

        set_is_sync(true);
        try {
            if (userItemsRef.current.length !== 0) {
                const currentItems = userItemsRef.current;
                await back_service.users.sync_items({
                    user_id: user.name,
                    items: currentItems,
                });
            }
            set_groups(await back_service.groups.items(user.nick));
        } finally {
            set_is_sync(false);
        }
    }, [is_sync])

    // Запускаем таймер при монтировании компонента
    useEffect(() => {
        // Первая отправка через 2 минуты
        timerRef.current = setInterval(fetch_user_data, 2 * 60 * 1000); // 120000 мс = 2 минуты

        // Очистка таймера при размонтировании
        return () => {
            if (timerRef.current) {
                clearInterval(timerRef.current);
            }
        };
    }, [fetch_user_data]);

    return <div style={{width:'100%', maxWidth: '500px', padding: '5px'}}>
        <h1>{user.nick || 'Не авторизован'}</h1>
        <Search
            items={items}
            handle_select={handle_user_select_item}
            Line_element={DashSearchItem}
            placeholder='Название...'
        />
        <div className="base_flex_column" style={{
            alignItems: 'flex-start',
            width: '100%',
            marginTop: '5px'
        }}>
            {user_items.map((item) => <ItemUserCount
                key={item.id}
                data={item}
                onQuantityChange={handleQuantityChange}
                onRemove={handleRemove}
            />)}
        </div>
    </div>
};

export default DashboardPage;
