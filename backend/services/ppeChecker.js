export function checkPPE(observations = []) { return { compliant: observations.filter((item) => item.compliant).length, total: observations.length }; }
