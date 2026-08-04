"use client";

import { useState } from "react";
import { useRouter } from "next/navigation";
import { useAuth } from "@/hooks/useAuth";

export default function LoginPage() {

    const router = useRouter();

    const { login } = useAuth();

    const [email, setEmail] =
        useState("");

    const [password, setPassword] =
        useState("");

    async function handleSubmit(
        e: React.FormEvent
    ) {

        e.preventDefault();

        await login(email, password);

        router.push("/dashboard");
    }

    return (

        <div className="flex items-center justify-center h-screen">

            <form
                onSubmit={handleSubmit}
                className="space-y-4 w-96"
            >

                <h1 className="text-3xl font-bold">
                    Login
                </h1>

                <input
                    className="border p-3 w-full"
                    placeholder="Email"
                    onChange={(e) =>
                        setEmail(e.target.value)
                    }
                />

                <input
                    className="border p-3 w-full"
                    type="password"
                    placeholder="Password"
                    onChange={(e) =>
                        setPassword(e.target.value)
                    }
                />

                <button
                    className="bg-blue-600 text-white w-full p-3"
                >
                    Login
                </button>

            </form>

        </div>

    );
}