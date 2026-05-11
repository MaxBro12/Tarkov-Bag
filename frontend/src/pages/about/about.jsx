
import {Link, useSearchParams} from "react-router-dom";


export const AboutPage = () => {
    const [params] = useSearchParams();
    const content = {
        'about': 'Это приложение для помощи тиммейтам в поисках нужных вам придметов. Укажите какие предметы вам необходимы и ваши тиммейты их увидят. Так же помогайте своим друзьям. Приложение в бета версии, как и тарков.'
    }
    const error = params.get('error') || undefined;

    if (error === 'backend_off') {
        return <div>Не удалось подключиться к серверу. Пожалуйста, попробуйте позже.</div>;
    }
    if (error === 'inner') {
        return <div>Внутренняя ошибка приложения. Обратитесь к администратору.</div>;
    }

    return <div style={{
        padding: '10px',
        gap: '10px'
    }} className='base_flex_column'>
        <span>{content?.about}</span>
        <Link to='/about/feetback' className='base_button'>Нашли ошибку или есть предложение?</Link>
    </div>
}


export default AboutPage;