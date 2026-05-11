import { useState } from 'react'
import { useAuth } from '@/context/auth.jsx'
import back_service from '@/api/main';
import { LoadingAnimation } from '@/components/utils/loading_animation.jsx';


export const UserPage = () => {
    const [loading, set_loading] = useState(false)
    const { user, logout } = useAuth()
    const [data, set_data] = useState({ nick: user?.nick ?? '' })

    const handle_change = (e) => set_data({ nick: e.target.value })

    const form_submit = async () => {
        set_loading(true)
        await back_service.users.set_nick(data.nick)
        set_loading(false)
        window.location.href = '/'
    }

    if (loading) return <LoadingAnimation />

    return <div className='base_flex_column no_wrap' style={{width: '100%', maxWidth: '300px'}}>
        <div className='base_flex_row' style={{width: '100%'}}>
            <span className='no_select'>Имя: </span>
            <span>{user?.name}</span>
        </div>
        <form className='base_flex_row no_wrap' onSubmit={(e) => { e.preventDefault(); form_submit() }} style={{
            width: '100%'
        }}>
            <input
                type='text'
                name='Ник'
                style={{padding: 5, width: '100%'}}
                className='rounded_border'
                placeholder='ник'
                value={data.nick}
                onChange={handle_change}
                required
            />
            <input type='submit' style={{padding: 5}} className='rounded_border' value='Подтвердить'/>
        </form>
        <button onClick={logout}>Выйти</button>
    </div>
};
