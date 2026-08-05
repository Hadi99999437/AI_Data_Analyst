"use client";

import UploadDataset from "@/components/dataset/UploadDataset";

export default function UploadPage() {
    return (
        <div className="p-6">
            <h1 className="text-3xl font-bold mb-6">
                Upload Dataset
            </h1>

            <UploadDataset />
        </div>
    );
}