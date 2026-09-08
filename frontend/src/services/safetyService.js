const API_BASE_URL = import.meta.env.VITE_API_URL || "http://localhost:8000";

export async function getSafetySummary() {
  const response = await fetch(`${API_BASE_URL}/api/safety/summary`);
  if (!response.ok) throw new Error(`Safety summary failed: ${response.status}`);
  return response.json();
}

export async function getAlerts() {
  const response = await fetch(`${API_BASE_URL}/api/alerts`);
  if (!response.ok) throw new Error(`Alerts request failed: ${response.status}`);
  return response.json();
}
