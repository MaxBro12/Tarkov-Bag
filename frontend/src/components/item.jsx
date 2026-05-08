
export const ItemIcon = ({id, name}) => {
    return <img src={`https://assets.tarkov.dev/${id}-icon.webp`} alt={name} style={{
        height: 32,
        width: 32,
    }}/>
};


export const Item = ({ id, name }) => {
    return <div className='rounded_border base_flex_row nowrap'>
        <ItemIcon id={id} name={name} />
        <span>{name}</span>
    </div>
};
