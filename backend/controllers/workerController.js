import Worker from "../models/Worker.js";
export function listWorkers(_request, response) { response.json({ workers: Worker.all() }); }
