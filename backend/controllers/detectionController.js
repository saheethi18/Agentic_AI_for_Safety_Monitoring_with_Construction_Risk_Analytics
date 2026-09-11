import { runDetection } from "../services/safetyAgent.js";
export function detect(request, response) { response.json(runDetection(request.body)); }
