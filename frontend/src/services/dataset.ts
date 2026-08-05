import api from "./api";

export async function uploadDataset(
    file: File,
    name: string
) {
    const formData = new FormData();

    formData.append("file", file);
    formData.append("name", name);

    const response = await api.post(
        "/datasets/upload",
        formData,
        {
            headers: {
                "Content-Type":
                    "multipart/form-data",
            },
        }
    );

    return response.data;
}

export async function getDatasets() {

    const response = await api.get(
        "/datasets"
    );

    return response.data;
}

export async function deleteDataset(
    datasetId: string
) {

    await api.delete(
        `/datasets/${datasetId}`
    );
}