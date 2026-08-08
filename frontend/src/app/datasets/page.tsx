"use client";

import { useEffect, useState } from "react";
import Link from "next/link";

import { getDatasets } from "@/services/dataset";

interface Dataset {
    id: string;
    filename?: string;
    name?: string;
    created_at?: string;
}

export default function DatasetsPage() {

    const [datasets, setDatasets] = useState<Dataset[]>([]);
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState("");

    useEffect(() => {

        async function loadDatasets() {

            try {

                const data = await getDatasets();

                setDatasets(data);

            } catch (err) {

                console.error(err);

                setError(
                    "Unable to load datasets."
                );

            } finally {

                setLoading(false);

            }
        }

        loadDatasets();

    }, []);

    if (loading) {

        return (
            <div className="p-8">
                <h1 className="text-2xl font-bold">
                    Datasets
                </h1>

                <p className="mt-4">
                    Loading datasets...
                </p>
            </div>
        );
    }

    return (

        <div className="p-8">

            <div className="flex items-center justify-between">

                <div>
                    <h1 className="text-3xl font-bold">
                        Datasets
                    </h1>

                    <p className="text-gray-500 mt-1">
                        Manage your uploaded datasets.
                    </p>
                </div>

                <Link
                    href="/datasets/upload"
                    className="rounded-lg bg-black px-5 py-3 text-white"
                >
                    Upload Dataset
                </Link>

            </div>

            {error && (
                <div className="mt-6 rounded-lg border border-red-300 bg-red-50 p-4 text-red-600">
                    {error}
                </div>
            )}

            {!error && datasets.length === 0 && (

                <div className="mt-10 rounded-xl border p-10 text-center">

                    <h2 className="text-xl font-semibold">
                        No datasets yet
                    </h2>

                    <p className="mt-2 text-gray-500">
                        Upload a CSV or dataset to start analyzing your data.
                    </p>

                    <Link
                        href="/datasets/upload"
                        className="mt-5 inline-block rounded-lg bg-black px-5 py-3 text-white"
                    >
                        Upload Dataset
                    </Link>

                </div>
            )}

            {datasets.length > 0 && (

                <div className="mt-8 grid gap-5 md:grid-cols-2 lg:grid-cols-3">

                    {datasets.map((dataset) => (

                        <div
                            key={dataset.id}
                            className="rounded-xl border bg-white p-6 shadow-sm"
                        >

                            <div className="flex items-start justify-between">

                                <div>

                                    <h2 className="font-semibold text-lg">
                                        {dataset.filename ||
                                            dataset.name ||
                                            "Unnamed Dataset"}
                                    </h2>

                                    <p className="mt-2 text-sm text-gray-500">
                                        Dataset
                                    </p>

                                </div>

                                <div className="rounded-lg bg-gray-100 px-3 py-2 text-xs">
                                    CSV
                                </div>

                            </div>

                            {dataset.created_at && (

                                <p className="mt-4 text-sm text-gray-500">
                                    Uploaded:{" "}
                                    {new Date(
                                        dataset.created_at
                                    ).toLocaleString()}
                                </p>

                            )}

                            <div className="mt-5 flex gap-3">

                                <Link
                                    href={`/datasets/${dataset.id}`}
                                    className="rounded-lg border px-4 py-2 text-sm"
                                >
                                    View
                                </Link>

                                <Link
                                    href={`/analysis?datasetId=${dataset.id}`}
                                    className="rounded-lg bg-black px-4 py-2 text-sm text-white"
                                >
                                    Analyze
                                </Link>

                            </div>

                        </div>

                    ))}

                </div>
            )}

        </div>
    );
}