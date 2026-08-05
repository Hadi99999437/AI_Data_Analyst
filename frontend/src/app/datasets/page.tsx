import DashboardLayout from "@/components/layout/DashboardLayout";

export default function DatasetsPage() {
    return (
        <DashboardLayout>
            <h1 className="text-3xl font-bold mb-6">
                Datasets
            </h1>

            <a
                href="/datasets/upload"
                className="bg-blue-600 text-white px-5 py-3 rounded"
            >
                Upload Dataset
            </a>
        </DashboardLayout>
    );
}