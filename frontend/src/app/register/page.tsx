"use client";

import { useState } from "react";
import { useRouter } from "next/navigation";
import { useAuth } from "@/hooks/useAuth";

export default function RegisterPage() {

    const router = useRouter();

    const { register } = useAuth();

    const [name, setName] =
        useState("");

    const [email, setEmail] =
        useState("");

    const [password, setPassword] =
        useState("");

    async function handleSubmit(
        e: React.FormEvent
    ) {

        e.preventDefault();

        await register(
            name,
            email,
            password
        );

        router.push("/login");
    }

    return (

        <div className="flex items-center justify-center h-screen">

            <form
                onSubmit={handleSubmit}
                className="space-y-4 w-96"
            >

                <h1 className="text-3xl font-bold">
                    Register
                </h1>

                <input
                    className="border p-3 w-full"
                    placeholder="Full Name"
                    onChange={(e) =>
                        setName(e.target.value)
                    }
                />

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
                    className="bg-green-600 text-white w-full p-3"
                >
                    Register
                </button>

            </form>

        </div>

    );
}