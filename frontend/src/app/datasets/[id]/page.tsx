"use client";

import { useEffect, useState } from "react";
import { useParams, useRouter } from "next/navigation";

import { getDataset } from "@/services/dataset";

export default function DatasetDetailsPage() {
    const params = useParams();
    const router = useRouter();

    const [dataset, setDataset] = useState<any>(null);
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState("");

    useEffect(() => {
        const loadDataset = async () => {
            try {
                const data = await getDataset(params.id as string);
                setDataset(data);
            } catch (err) {
                console.error(err);
                setError("Unable to load dataset.");
            } finally {
                setLoading(false);
            }
        };

        loadDataset();
    }, [params.id]);

    if (loading) {
        return (
            <div className="min-h-screen flex items-center justify-center bg-[#080b12] text-white">
                Loading dataset...
            </div>
        );
    }

    if (error) {
        return (
            <div className="min-h-screen flex items-center justify-center bg-[#080b12]">
                <div className="text-red-400">{error}</div>
            </div>
        );
    }

    if (!dataset) {
        return (
            <div className="min-h-screen flex items-center justify-center bg-[#080b12] text-white">
                Dataset not found.
            </div>
        );
    }

    return (
        <div className="min-h-screen bg-[#080b12] text-white p-8">

            <div className="max-w-6xl mx-auto">

                <button
                    onClick={() => router.push("/datasets")}
                    className="mb-6 text-gray-400 hover:text-white transition"
                >
                    ← Back to Datasets
                </button>

                <div className="mb-8">
                    <h1 className="text-4xl font-bold">
                        {dataset.name || dataset.file_name || "Dataset"}
                    </h1>

                    <p className="text-gray-400 mt-2">
                        Dataset details and metadata
                    </p>
                </div>

                <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-5">

                    <div className="dataset-detail-card">
                        <p className="dataset-detail-label">
                            File Name
                        </p>
                        <p className="dataset-detail-value">
                            {dataset.file_name || "N/A"}
                        </p>
                    </div>

                    <div className="dataset-detail-card">
                        <p className="dataset-detail-label">
                            File Type
                        </p>
                        <p className="dataset-detail-value">
                            {dataset.file_type || "N/A"}
                        </p>
                    </div>

                    <div className="dataset-detail-card">
                        <p className="dataset-detail-label">
                            Rows
                        </p>
                        <p className="dataset-detail-value">
                            {dataset.rows ?? "N/A"}
                        </p>
                    </div>

                    <div className="dataset-detail-card">
                        <p className="dataset-detail-label">
                            Columns
                        </p>
                        <p className="dataset-detail-value">
                            {dataset.columns ?? "N/A"}
                        </p>
                    </div>

                </div>

                <div className="mt-6 dataset-detail-card">

                    <h2 className="text-xl font-semibold mb-5">
                        Dataset Information
                    </h2>

                    <div className="grid grid-cols-1 md:grid-cols-2 gap-5">

                        <div>
                            <p className="dataset-detail-label">
                                Upload Status
                            </p>

                            <p className="text-green-400 mt-1">
                                {dataset.upload_status || "Unknown"}
                            </p>
                        </div>

                        <div>
                            <p className="dataset-detail-label">
                                Dataset ID
                            </p>

                            <p className="text-gray-300 mt-1 break-all">
                                {dataset.id}
                            </p>
                        </div>

                        <div>
                            <p className="dataset-detail-label">
                                File Size
                            </p>

                            <p className="text-gray-300 mt-1">
                                {dataset.file_size
                                    ? `${(
                                        dataset.file_size / 1024
                                    ).toFixed(2)} KB`
                                    : "N/A"}
                            </p>
                        </div>

                        <div>
                            <p className="dataset-detail-label">
                                Uploaded
                            </p>

                            <p className="text-gray-300 mt-1">
                                {dataset.created_at
                                    ? new Date(
                                        dataset.created_at
                                    ).toLocaleString()
                                    : "N/A"}
                            </p>
                        </div>

                    </div>

                </div>

            </div>

        </div>
    );
}