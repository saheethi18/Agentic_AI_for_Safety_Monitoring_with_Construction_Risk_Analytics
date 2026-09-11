import { Router } from "express";
import { detect } from "../controllers/detectionController.js";
const router = Router();
router.post("/", detect);
export default router;
