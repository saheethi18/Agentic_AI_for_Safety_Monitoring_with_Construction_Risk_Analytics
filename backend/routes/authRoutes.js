import { Router } from "express";
import { forgotPassword, login, signup } from "../controllers/authController.js";
const router = Router();
router.post("/login", login);
router.post("/signup", signup);
router.post("/forgot-password", forgotPassword);
export default router;
