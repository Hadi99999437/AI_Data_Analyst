"use client";

import { useAuth } from "@/hooks/useAuth";

export default function Navbar() {

    const { user } = useAuth();

    return (

        <header className="h-16 bg-white shadow flex items-center justify-between px-8">

            <h2 className="font-semibold">

                Welcome

            </h2>

            <div>

                {user?.email}

            </div>

        </header>

    );

}