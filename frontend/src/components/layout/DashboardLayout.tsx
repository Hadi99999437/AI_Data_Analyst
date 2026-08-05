"use client";

import Sidebar from "./Sidebar";
import Navbar from "./Navbar";

export default function DashboardLayout({

    children,

}: {

    children: React.ReactNode;

}) {

    return (

        <div className="flex h-screen">

            <Sidebar />

            <div className="flex-1 flex flex-col">

                <Navbar />

                <main className="flex-1 bg-slate-100 p-8 overflow-auto">

                    {children}

                </main>

            </div>

        </div>

    );

}