"use client";

import DashboardLayout from "@/components/layout/DashboardLayout";

export default function DashboardPage() {

    return (

        <DashboardLayout>

            <div className="space-y-8">

                <h1 className="text-4xl font-bold">
                    AI Data Analyst Dashboard
                </h1>

                <div className="grid grid-cols-4 gap-6">

                    <div className="bg-white rounded-xl shadow p-6">

                        <h2 className="text-gray-500">
                            Datasets
                        </h2>

                        <p className="text-3xl font-bold">
                            0
                        </p>

                    </div>

                    <div className="bg-white rounded-xl shadow p-6">

                        <h2 className="text-gray-500">
                            Analyses
                        </h2>

                        <p className="text-3xl font-bold">
                            0
                        </p>

                    </div>

                    <div className="bg-white rounded-xl shadow p-6">

                        <h2 className="text-gray-500">
                            Reports
                        </h2>

                        <p className="text-3xl font-bold">
                            0
                        </p>

                    </div>

                    <div className="bg-white rounded-xl shadow p-6">

                        <h2 className="text-gray-500">
                            AI Chats
                        </h2>

                        <p className="text-3xl font-bold">
                            0
                        </p>

                    </div>

                </div>

            </div>

        </DashboardLayout>

    );

}