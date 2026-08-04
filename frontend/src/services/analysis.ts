import api from "./api";

export const runAnalysis = async (
    datasetId: string
) => {

    const response = await api.post(
        "/analysis",
        {
            dataset_id: datasetId,
            analysis_type: "full",
        }
    );

    return response.data;
};

export const getAnalysis = async (
    jobId: string
) => {

    const response = await api.get(
        `/analysis/${jobId}`
    );

    return response.data;
};