"use client";

import { useParams } from "next/navigation";

export default function DatasetDetailsPage() {
    const params = useParams();

    const id = params.id as string;

    return (
        <div className="p-8">
            <h1 className="text-3xl font-bold">
                Dataset Details
            </h1>

            <p className="mt-4">
                Dataset ID: {id}
            </p>
        </div>
    );
}