import api from "./api";

export const uploadDataset = async (file: File) => {

    const formData = new FormData();

    formData.append("file", file);

    const response = await api.post(
        "/datasets/upload",
        formData,
        {
            headers: {
                Authorization:
                    `Bearer ${localStorage.getItem("token")}`,
                "Content-Type":
                    "multipart/form-data",
            },
        }
    );

    return response.data;
};

export const getDatasets = async () => {

    const response = await api.get(
        "/datasets",
        {
            headers: {
                Authorization:
                    `Bearer ${localStorage.getItem("token")}`,
            },
        }
    );

    return response.data;
};
export const getDataset = async (id: string) => {
    const response = await api.get(`/datasets/${id}`);
    return response.data;
};