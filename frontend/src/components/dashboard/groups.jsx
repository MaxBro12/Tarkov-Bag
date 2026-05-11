import {Item} from "@/components/item.jsx";

const Member = ({member}) => {
    return <div className='base_flex_column' style={{
        width:'100%',
        alignItems: 'flex-start',
        padding: '5px',
        borderRadius: '15px',
    }}>
        <span>{member.nick}</span>
        {member.items.map(item => <div key={item.id} className="base_flex_row no_wrap" style={{width:'100%', padding: '5px'}}>
            <Item id={item.id} name={item.name} />
            <span>{item.count}</span>
        </div>)}
    </div>
}


const Group = ({group}) => {
    return <div className='base_flex_column rounded_border' style={{width:'100%'}}>
        {group.members.map(member => <Member member={member} key={member.nick}/>)}
    </div>
}


export const DashboardGroups = ({groups}) => {
    return <div className='base_flex_column' style={{width:'100%', marginTop: '5px'}}>
        {groups.map(group => <Group key={group.id} group={group} />)}
    </div>
}