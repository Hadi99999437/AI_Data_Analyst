"use client";

import Link from "next/link";

export default function Sidebar() {

    return (

        <aside className="w-64 bg-slate-900 text-white h-screen p-6">

            <h1 className="text-2xl font-bold mb-10">
                AI Analyst
            </h1>

            <nav className="space-y-4">

                <Link href="/dashboard" className="block">
                    Dashboard
                </Link>

                <Link href="/datasets" className="block">
                    Datasets
                </Link>

                <Link href="/analysis" className="block">
                    Analysis
                </Link>

                <Link href="/reports" className="block">
                    Reports
                </Link>

                <Link href="/chat" className="block">
                    AI Chat
                </Link>

            </nav>

        </aside>

    );

}