import { useEffect, useState } from "react";
import { back_service } from "@/api/main.jsx";
import { useAuth } from "@/context/auth.jsx";
import { useNavigate } from "react-router-dom";


export const DashboardPage = () => {
    const navigate = useNavigate()
    const { user } = useAuth()
    const [nicks, set_nicks] = useState([])

    if (user.nick === null) {
        navigate('/auth/user')
    }

    useEffect(() => {
        const fetch_nicks = async () => {
            set_nicks(await back_service.users.nicks())
        }
        fetch_nicks()
    }, [])

    return (
        <div>
            <h1>Welcome, {user.nick}</h1>
            <ul>
                {nicks.map((nick) => (
                    <li key={nick}>{nick}</li>
                ))}
            </ul>
        </div>
    );
};

export default DashboardPage;
