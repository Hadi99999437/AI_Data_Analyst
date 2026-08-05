"use client";

import { useState } from "react";
import { uploadDataset } from "@/services/dataset";

export default function UploadDataset() {

    const [file, setFile] =
        useState<File | null>(null);


    const [loading, setLoading] =
        useState(false);

    async function handleUpload() {

        if (!file) {
            alert("Select a CSV file");
            return;
        }

        setLoading(true);

        try {

            await uploadDataset(file);
            alert("Dataset uploaded successfully");

            setFile(null);
            

        } catch {

            alert("Upload failed");

        } finally {

            setLoading(false);

        }

    }

    return (

        <div className="max-w-xl space-y-5">

            <h1 className="text-3xl font-bold">
                Upload Dataset
            </h1>

            <input
                className="border p-3 w-full rounded"
                placeholder="Dataset Name"
                
            />

            <input
                type="file"
                accept=".csv"
                onChange={(e)=>
                    setFile(
                        e.target.files?.[0] || null
                    )
                }
            />

            <button
                onClick={handleUpload}
                disabled={loading}
                className="bg-blue-600 text-white px-5 py-3 rounded"
            >
                {
                    loading
                    ? "Uploading..."
                    : "Upload Dataset"
                }
            </button>

        </div>

    );

}