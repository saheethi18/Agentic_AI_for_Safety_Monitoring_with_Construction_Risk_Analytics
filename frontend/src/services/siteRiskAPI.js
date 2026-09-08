const API_BASE_URL =
  "http://localhost:8000";


export const getDatasetSummary = async () => {
  const response = await fetch(
    `${API_BASE_URL}/dataset/summary`
  );

  if (!response.ok) {
    throw new Error(
      `Failed to fetch dataset summary: ${response.status}`
    );
  }

  return await response.json();
};


export const getSiteRisk = async (
  projectId = "P001"
) => {

  const response = await fetch(
    `${API_BASE_URL}/site-risk/${projectId}`
  );

  if (!response.ok) {

    throw new Error(
      `Failed to fetch site risk: ${response.status}`
    );

  }

  return await response.json();
};


export const analyzeSiteRisk = async (
  siteData
) => {

  const response = await fetch(
    `${API_BASE_URL}/site-risk/analyze`,
    {
      method: "POST",

      headers: {
        "Content-Type":
          "application/json"
      },

      body: JSON.stringify(siteData)
    }
  );


  if (!response.ok) {

    throw new Error(
      `Site risk analysis failed: ${response.status}`
    );

  }

  return await response.json();
};


export const checkBackendStatus =
  async () => {

    try {

      const response = await fetch(
        `${API_BASE_URL}/health`
      );

      return response.ok;

    } catch {

      return false;

    }

  };


const siteRiskAPI = {
  getSiteRisk,
  analyzeSiteRisk,
  checkBackendStatus,
  getDatasetSummary
};


export default siteRiskAPI;