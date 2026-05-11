import { useState } from 'react';
import {Item} from "@/components/item.jsx";


export const ItemUserCount = ({ data, onRemove, onQuantityChange }) => {
    const [isEditing, setIsEditing] = useState(false);
    const [editValue, setEditValue] = useState(data.count);

    const handleQuantityClick = () => {
        setIsEditing(true);
        setEditValue(data.count);
    };

    const handleQuantityChange = (e) => {
        const value = e.target.value;
        // Разрешаем только цифры
        if (/^\d*$/.test(value)) {
            setEditValue(value);
        }
    };

    const handleQuantityBlur = () => {
        setIsEditing(false);
        const newQuantity = parseInt(editValue) || 0;
        if (newQuantity > 0) {
            onQuantityChange(data.id, newQuantity);
        } else {
            // Если количество 0 или меньше, можно удалить предмет или установить минимум
            if (newQuantity <= 0) {
                onRemove(data.id);
            }
        }
    };

    const handleKeyDown = (e) => {
        if (e.key === 'Enter') {
            handleQuantityBlur();
        }
    };

    return <div className='base_flex_row' style={{flexWrap: 'nowrap', width: '100%'}}>
        <Item id={data.id} name={data.name}/>
        <button
            className="no_select"
            onClick={() => onQuantityChange(data.id, data.count - 1)}
            disabled={data.count <= 1}
        >
            -
        </button>

        {isEditing ? (
            <input
                type="text"
                value={editValue}
                onChange={handleQuantityChange}
                onBlur={handleQuantityBlur}
                onKeyDown={handleKeyDown}
                autoFocus
            />
        ) : (
            <span
                onClick={handleQuantityClick}
                title="Кликните для редактирования"
            >
            {data.count}
          </span>
        )}

        <button
            onClick={() => onQuantityChange(data.id, data.count + 1)}
            className='no_select'
        >
            +
        </button>
        <button
            onClick={() => onRemove(data.id)}
            title="Удалить предмет"
            className='no_select'
        >
            ✕
        </button>
    </div>
};
