import { Router } from "express";
import { listWorkers } from "../controllers/workerController.js";
const router = Router();
router.get("/", listWorkers);
export default router;
