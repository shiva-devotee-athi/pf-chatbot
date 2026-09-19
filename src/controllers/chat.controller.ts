import { Request, Response } from "express";
import { z } from "zod";
import { askAI } from "../services/ai.service";

const chatSchema = z.object({
  message: z
    .string()
    .trim()
    .min(1, "Message is required")
    .max(1000, "Message is too long"),
});

export const chatController = async (
  req: Request,
  res: Response
) => {
  try {
    const result = chatSchema.safeParse(req.body);

    if (!result.success) {
      return res.status(400).json({
        success: false,
        message: result.error.issues[0]?.message,
      });
    }

    const answer = await askAI(result.data.message);

    return res.status(200).json({
      success: true,
      data: answer,
    });
  } catch (error) {
    console.error("AI Error:", error);

    return res.status(500).json({
      success: false,
      message: "Unable to process your request.",
    });
  }
};