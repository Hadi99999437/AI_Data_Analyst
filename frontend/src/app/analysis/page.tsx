"use client";

import DashboardLayout from "@/components/layout/DashboardLayout";

export default function AnalysisPage() {
    return (
        <DashboardLayout>
            <div className="space-y-8">

                <div>
                    <h1 className="text-3xl font-bold">
                        AI Analysis
                    </h1>

                    <p className="text-gray-500 mt-2">
                        Start an analysis on one of your uploaded datasets.
                    </p>
                </div>

                <div className="border rounded-xl p-6 bg-white shadow">

                    <h2 className="text-xl font-semibold mb-4">
                        New Analysis
                    </h2>

                    <select className="border rounded-lg p-3 w-full mb-4">
                        <option>Select Dataset</option>
                    </select>

                    <select className="border rounded-lg p-3 w-full mb-6">
                        <option>Exploratory Data Analysis</option>
                        <option>Classification</option>
                        <option>Regression</option>
                        <option>Clustering</option>
                        <option>Time Series</option>
                    </select>

                    <button
                        className="bg-blue-600 hover:bg-blue-700 text-white px-6 py-3 rounded-lg"
                    >
                        Start Analysis
                    </button>

                </div>

                <div className="border rounded-xl p-6 bg-white shadow">

                    <h2 className="text-xl font-semibold mb-4">
                        Previous Analysis Jobs
                    </h2>

                    <p className="text-gray-500">
                        Your analysis history will appear here.
                    </p>

                </div>

            </div>
        </DashboardLayout>
    );
}