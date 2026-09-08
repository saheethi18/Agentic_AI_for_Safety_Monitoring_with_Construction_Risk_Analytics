export default class Detection { constructor({ id, riskScore, hazards = [] }) { this.id = id; this.riskScore = riskScore; this.hazards = hazards; this.createdAt = new Date().toISOString(); } }
