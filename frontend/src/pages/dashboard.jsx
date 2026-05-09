import { useEffect, useState } from "react";
import { back_service } from "@/api/main.jsx";
import { useAuth } from "@/context/auth.jsx";
import { useNavigate } from "react-router-dom";
import { Item } from "@/components/item.jsx";


export const DashboardPage = () => {
    const navigate = useNavigate()
    const { user } = useAuth()
    const [nicks, set_nicks] = useState([])
    const [user_items, set_user_items] = useState([])

    if (user.nick === null) {
        navigate('/auth/user')
    }

    useEffect(() => {
        const fetch_data = async () => {
            set_nicks(await back_service.users.nicks())
            set_user_items(await back_service.users.user_items())
        }
        fetch_data()
    }, [])

    return (
        <div>
            <h1>{user.nick || 'Не авторизован'}</h1>
            <div className="base_flex_column">
                {user_items.map((item) => (
                    <Item key={item.id} id={item.id} name={item.name}/>
                ))}
            </div>
        </div>
    );
};

export default DashboardPage;
