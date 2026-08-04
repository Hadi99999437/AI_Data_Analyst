import api from "./api";

export const askQuestion = async (
    datasetId: string,
    question: string
) => {

    const response = await api.post(
        "/chat",
        {
            dataset_id: datasetId,
            question,
        }
    );

    return response.data;
};