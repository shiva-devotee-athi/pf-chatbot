import { Router } from "express";

const router = Router();

router.get("/", (_req, res) => {
  res.json({
    success: true,
    status: "ok",
    service: "resume-ai-api",
  });
});

export default router;