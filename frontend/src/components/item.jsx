
export const ItemIcon = ({id, name}) => {
    return <img src={`https://assets.tarkov.dev/${id}-icon.webp`} alt={name} style={{
        height: 32,
        width: 32,
        borderWidth: 0,
    }} className='rounded_border no_select'/>
};


export const Item = ({ id, name }) => {
    return <div className='rounded_border base_flex_row' style={{
        borderWidth: 0,
        flexWrap: 'nowrap',
        width: '100%',
    }}>
        <ItemIcon id={id} name={name} />
        <span>{name}</span>
    </div>
};
