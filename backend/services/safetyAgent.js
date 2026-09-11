export function runDetection(input = {}) { return { riskScore: 64, riskLevel: "HIGH", hazards: input.hazards || [], recommendations: ["Review PPE compliance", "Confirm equipment exclusion zones"] }; }
export function getSafetySummary() { return { workers: 185, compliantWorkers: 176, openAlerts: 3, riskScore: 64, riskLevel: "HIGH" }; }
