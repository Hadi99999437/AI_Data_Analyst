import api from "./api";

export const getReport = async (
    jobId: string
) => {

    const response = await api.get(
        `/report/${jobId}`
    );

    return response.data;
};