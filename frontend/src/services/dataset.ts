import api from "./api";

export const uploadDataset = async (file: File) => {

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