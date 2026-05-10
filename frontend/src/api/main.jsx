import api from "@/api/base.jsx";

export const back_service = {
    items: {
        all: async ({ skip_ = 0, limit_ = 10 }) => {
            return (await api.get('/v1/items', {
                params: {
                    skip: skip_ ?? 0,
                    limit: limit_ ?? 10000,
                }
            })).data.items || []
        },
        sync: async ({code}) => {
            return (await api.post('/v1/items/sync', { code: code }))
        },
    },
    users: {
        nicks: async () => {
            return (await api.get('/v1/users/nicks')).data.nicks || []
        },
        set_nick: async (nick) => {
            return (await api.post('/v1/users/new', { nick: nick }))
        },
        user_items: async (user_id) => {
            return (await api.get(`/v1/users/${user_id}/items`)).data.items || []
        },
        sync_items: async ({user_id, items}) => {
            const new_items = items.map(({name, ...rest}) => rest);
            return (await api.post(`/v1/users/${user_id}/items/sync`, { items: new_items }))
        }
    },
    groups: {
        items: async ({user_id}) => {
            return (await api.get(`/v1/groups/${user_id}/items`)).data.items || []
        }
     },
}

export default back_service;
