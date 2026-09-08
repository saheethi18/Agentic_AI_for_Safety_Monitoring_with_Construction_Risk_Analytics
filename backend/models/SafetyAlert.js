export default class SafetyAlert { constructor({ id, title, severity, status = "open" }) { this.id = id; this.title = title; this.severity = severity; this.status = status; } }
