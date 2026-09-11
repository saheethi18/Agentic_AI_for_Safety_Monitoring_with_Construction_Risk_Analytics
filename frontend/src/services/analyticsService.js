const API_BASE_URL = import.meta.env.VITE_API_URL || "http://localhost:8000";

export async function getAnalytics() {
  const response = await fetch(`${API_BASE_URL}/api/analytics`);
  if (!response.ok) throw new Error(`Analytics request failed: ${response.status}`);
  return response.json();
}
