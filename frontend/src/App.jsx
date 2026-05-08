import {lazy, Suspense} from "react";
import {
    BrowserRouter,
    Routes,
    Route,
} from "react-router-dom";

import './css/style.css';
import {useTheme} from "@/context/theme.jsx"
import CustomHeader from "@/components/utils/custom_header.jsx";

import {LoginPage} from "@/pages/auth/login.jsx";
import {LogoutPage} from "@/pages/auth/logout.jsx";
import {RegisterPage} from "@/pages/auth/register.jsx";
import {AuthOutlet} from "@/pages/auth/outlet.jsx";
import { UserPage } from "@/pages/auth/user.jsx";

import { DashboardPage } from "@/pages/dashboard.jsx";

const AboutPage = lazy(() => import("@/pages/about/about.jsx"));
const ItemsSyncPage = lazy(() => import("@/pages/items_sync.jsx"));


function App() {
    const {theme} = useTheme();

    const headers = [
        {
            path: '/',
            label: 'Главная',
            no_user_show: false,
        },
        {
            path: '/party',
            label: 'Группы',
            no_user_show: false
        },
    ]

    return (
        <BrowserRouter>
            <div className='App' data-theme={theme}>
                <CustomHeader headers={headers}/>
                <Suspense>
                    <Routes>
                        <Route path="/auth" element={<AuthOutlet />}>
                            <Route path="login" element={<LoginPage />}/>
                            <Route path="logout" element={<LogoutPage />}/>
                            <Route path="register" element={<RegisterPage />}/>
                            <Route path="user" element={<UserPage />}/>
                        </Route>
                        <Route path='/about' element={<AboutPage />} />

                        <Route path="/" element={<DashboardPage />} />
                        <Route path="/items/sync" element={<ItemsSyncPage />} />
                    </Routes>
                </Suspense>
            </div>
        </BrowserRouter>
    )
}

export default App
