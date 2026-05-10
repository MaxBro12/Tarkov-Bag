import {useNavigate} from "react-router-dom";


export const NavigateButton = ({inner, nav_to, adt_style}) => {
    const navigate = useNavigate();
    const style ={
        ...adt_style
    }

    const onClick = () => {
        navigate(nav_to)
    }

    return (
        <button onClick={(e) => (onClick(e))} style={style} className='base_button'>{inner}</button>
    )
}
