import { Router } from "express";
import { analytics } from "../controllers/analyticsController.js";
const router = Router();
router.get("/", analytics);
export default router;
