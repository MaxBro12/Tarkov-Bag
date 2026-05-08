import api from "@/api/base.jsx";

export const back_service = {
    items: {
        all: async ({skip = 0, limit = 10}) => {
            return (await api.get('/v1/items', {
                params: {
                    skip: skip,
                    limit: limit,
                }
            })).data.apps || []
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
    },
}

export default back_service;
