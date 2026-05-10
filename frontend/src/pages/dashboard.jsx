import { useEffect, useState } from "react";
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
    const { user } = useAuth()
    const [items, set_items] = useState([])
    const [user_items, set_user_items] = useState([])

    if (user.nick === null) {
        navigate('/auth/user')
    }

    const handle_user_select_item = (item) => {
        set_user_items([...user_items, {...item, count: 1}])
    }

    const handleQuantityChange = (itemId, newQuantity) => {
        if (newQuantity > 0) {
            set_user_items(user_items.map(item =>
                item.id === itemId
                    ? { ...item, count: newQuantity }
                    : item
            ));
        }
    };

    const handleRemove = (itemId) => {
        set_user_items(user_items.filter(item => item.id !== itemId));
    };

    useEffect(() => {
        const fetch_data = async () => {
            set_items(await back_service.items.all({skip_: 0, limit_: 10000}))
            set_user_items(await back_service.users.user_items())
        }
        fetch_data()
    }, [])

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
