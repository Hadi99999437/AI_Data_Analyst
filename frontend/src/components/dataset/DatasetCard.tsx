"use client";

import { useRouter } from "next/navigation";

interface DatasetCardProps {
    dataset: {
        id: string;
        name?: string;
        file_name?: string;
        file_type?: string;
        rows?: number;
        columns?: number;
    };
}

export default function DatasetCard({ dataset }: DatasetCardProps) {
    const router = useRouter();

    const datasetName =
        dataset.name || dataset.file_name || "Unnamed Dataset";

    return (
        <div className="rounded-xl border bg-white p-6 shadow-sm">
            <div className="flex items-start justify-between">
                <div>
                    <h2 className="text-xl font-semibold">
                        {datasetName}
                    </h2>

                    <p className="mt-2 text-sm text-gray-500">
                        Dataset
                    </p>
                </div>

                <span className="rounded-lg bg-gray-100 px-3 py-2 text-sm">
                    {dataset.file_type || "CSV"}
                </span>
            </div>

            <div className="mt-6 flex gap-3">
                <button
                    onClick={() =>
                        router.push(`/datasets/${dataset.id}`)
                    }
                    className="rounded-lg border px-4 py-2 hover:bg-gray-100"
                >
                    View
                </button>

                <button
                    onClick={() =>
                        router.push(`/analysis?datasetId=${dataset.id}`)
                    }
                    className="rounded-lg bg-black px-4 py-2 text-white hover:bg-gray-800"
                >
                    Analyze
                </button>
            </div>
        </div>
    );
}