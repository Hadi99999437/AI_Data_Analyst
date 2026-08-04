"use client";

import {
    createContext,
    useEffect,
    useState,
    ReactNode,
} from "react";

import * as authService from "@/services/auth";

interface User {
    email: string;
}

interface AuthContextType {
    user: User | null;
    login: (
        email: string,
        password: string
    ) => Promise<void>;
    register: (
        name: string,
        email: string,
        password: string
    ) => Promise<void>;
    logout: () => void;
}

export const AuthContext =
    createContext<AuthContextType | null>(null);

export function AuthProvider({
    children,
}: {
    children: ReactNode;
}) {

    const [user, setUser] =
        useState<User | null>(null);

    useEffect(() => {

        const token =
            localStorage.getItem("token");

        const email =
            localStorage.getItem("email");

        if (token && email) {
            setUser({ email });
        }

    }, []);

    async function login(
        email: string,
        password: string
    ) {

        const data =
            await authService.login({
                email,
                password,
            });

        localStorage.setItem(
            "token",
            data.access_token
        );

        localStorage.setItem(
            "email",
            email
        );

        setUser({ email });
    }

    async function register(
        full_name: string,
        email: string,
        password: string
    ) {

        await authService.register({
            full_name,
            email,
            password,
        });
    }

    function logout() {

        localStorage.removeItem("token");
        localStorage.removeItem("email");

        setUser(null);
    }

    return (
        <AuthContext.Provider
            value={{
                user,
                login,
                register,
                logout,
            }}
        >
            {children}
        </AuthContext.Provider>
    );
}