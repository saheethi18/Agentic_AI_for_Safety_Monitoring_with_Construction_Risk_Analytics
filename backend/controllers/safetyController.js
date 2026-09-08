import { getSafetySummary } from "../services/safetyAgent.js";
export function summary(_request, response) { response.json(getSafetySummary()); }
