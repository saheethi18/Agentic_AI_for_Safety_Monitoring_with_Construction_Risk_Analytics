export function monitorWorkers(workers = []) { return workers.map((worker) => ({ ...worker, monitored: true })); }
