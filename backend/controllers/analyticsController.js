import { getAnalytics } from "../services/analyticsService.js";
export function analytics(_request, response) { response.json(getAnalytics()); }
