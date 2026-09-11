import { getOpenAlerts } from "../services/alertGenerator.js";
export function listAlerts(_request, response) { response.json({ alerts: getOpenAlerts() }); }
