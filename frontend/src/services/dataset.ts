import api from "./api";

export const uploadDataset = async (
    file: File
) => {

    const formData = new FormData();

    formData.append("file", file);

    const response = await api.post(
        "/datasets/upload",
        formData,
        {
            headers: {
                "Content-Type": "multipart/form-data",
            },
        }
    );

    return response.data;
};

export const getDatasets = async () => {

    const response = await api.get("/datasets");

    return response.data;
};

export const deleteDataset = async (
    id: string
) => {

    await api.delete(`/datasets/${id}`);
};