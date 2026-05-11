import {createContext, useState, useMemo, useEffect, useContext, useCallback} from 'react';
import auth_service from '@/api/auth.jsx';
import {LoadingAnimation} from "@/components/utils/loading_animation.jsx";


const AuthContext = createContext({});


export function AuthProvider({ children }) {
    const [user, set_user] = useState(null);
    const [loading, set_loading] = useState(true);

    const check_auth = async () => {
        try {
            set_loading(true);
            const new_user = await auth_service.user()
            set_user({
                name: new_user.name,
                nick: new_user.nick,
            })
        } catch (error) {
            if (error.status === 401) {
                set_user(null);
            }
        } finally {
            set_loading(false);
        }
    };

    useEffect(() => {
        check_auth();
    }, []);

    const login = useCallback(async (name, password) => {
        set_loading(true);
        const data = await auth_service.login(name, password);
        set_user({ name: data.name, nick: data.nick });
        set_loading(false);
    }, []);

    const logout = useCallback(async () => {
        set_loading(true);
        await auth_service.logout();
        set_user(null);
        set_loading(false);
    }, []);

    const contextValue = useMemo(() => ({
        user,
        login,
        logout,
        loading,
        check_auth
    }), [user, loading, login, logout]);

    if (loading) {
        return <LoadingAnimation />;
    }

    return <AuthContext.Provider value={contextValue}>
        {children}
    </AuthContext.Provider>
}

export const useAuth = () => {
    const context = useContext(AuthContext);
    if (!context) {
        throw new Error('useAuth must be used within AuthProvider');
    }
    return context;
};