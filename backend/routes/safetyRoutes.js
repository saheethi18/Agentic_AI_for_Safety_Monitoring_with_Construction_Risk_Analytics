import { Router } from "express";
import { summary } from "../controllers/safetyController.js";
const router = Router();
router.get("/summary", summary);
export default router;
