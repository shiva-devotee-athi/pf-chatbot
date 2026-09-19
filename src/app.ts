import express from "express";
import cors from "cors";
import helmet from "helmet";

import chatRoutes from "./routes/chat.routes";
import healthRoutes from "./routes/health.routes";
import { rateLimit } from "./middleware/rate-limit";

const app = express();

app.use(helmet());

app.use(
  cors({
    origin: process.env.FRONTEND_URL,
  }),
);

app.use(express.json({ limit: "10kb" }));

app.get("/", (_req, res) => {
  res.json({
    service: "Resume AI API",
    status: "running",
  });
});

app.use("/api/health", healthRoutes);

app.use("/api/chat", rateLimit, chatRoutes);

export default app;
