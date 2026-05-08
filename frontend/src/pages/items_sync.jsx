import { useState } from 'react';
import { back_service } from '@/api/main.jsx';


export const ItemsSyncPage = () => {
    const [data, set_data] = useState({ code: '' });

    const handle_change = (e) => {
        set_data({
            ...data,
            [e.target.name]: e.target.value,
        });
    }

    const form_submit = async (e) => {
        e.preventDefault();
        console.log(data);
        const result = await back_service.items.sync({ code: data.code });
        console.log(result);
    };

    return <div>
        <form className='base_flex_column' onSubmit={(e) => form_submit(e)}>
            <input
                type="text"
                name='code'
                style={{padding: 5, width: '100%'}}
                className='rounded_border'
                placeholder='Код'
                value={data.code}
                onChange={handle_change}
                required
            />
            <input type='submit' style={{padding: 5}} className='rounded_border' value='Обновить'/>
        </form>
    </div>
};

export default ItemsSyncPage;
