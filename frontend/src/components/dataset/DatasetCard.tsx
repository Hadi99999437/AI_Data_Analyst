"use client";

import { useRouter } from "next/navigation";

export default function DatasetCard({ dataset }: any) {

    const router = useRouter();

    return (
        <div className="dataset-card">

            <div className="flex justify-between items-start">

                <div>
                    <h2 className="text-xl font-semibold text-white">
                        {dataset.name || dataset.file_name || "Unnamed Dataset"}
                    </h2>

                    <p className="text-gray-400 mt-1">
                        {dataset.file_type || "Dataset"}
                    </p>
                </div>

                <span className="dataset-badge">
                    {(dataset.file_type || "CSV").toUpperCase()}
                </span>

            </div>

            <div className="grid grid-cols-2 gap-3 mt-6">

                <div>
                    <p className="text-gray-500 text-sm">
                        Rows
                    </p>

                    <p className="text-white font-medium">
                        {dataset.rows ?? "—"}
                    </p>
                </div>

                <div>
                    <p className="text-gray-500 text-sm">
                        Columns
                    </p>

                    <p className="text-white font-medium">
                        {dataset.columns ?? "—"}
                    </p>
                </div>

            </div>

            <div className="flex gap-3 mt-6">

                <button
                    onClick={() =>
                        router.push(`/datasets/${dataset.id}`)
                    }
                    className="dataset-view-button"
                >
                    View
                </button>

                <button
                    onClick={() =>
                        router.push(`/analysis?datasetId=${dataset.id}`)
                    }
                    className="dataset-analyze-button"
                >
                    Analyze
                </button>

            </div>

        </div>
    );
}