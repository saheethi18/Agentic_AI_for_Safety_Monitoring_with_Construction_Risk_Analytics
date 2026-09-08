const workers = [{ id: "W-001", name: "Site crew A", zone: "North elevation", status: "Monitored" }, { id: "W-002", name: "Site crew B", zone: "Concrete deck", status: "Review needed" }];
export default class Worker { static all() { return workers; } }
