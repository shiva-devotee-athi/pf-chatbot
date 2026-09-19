import fs from "node:fs";
import path from "node:path";

// const knowledgeDirectory = path.join(process.cwd(), "src", "knowledge");
// const knowledgeDirectory = path.join(__dirname, "src", "knowledge");
const knowledgeDirectory = path.join(__dirname, "..", "knowledge");

const readDocument = (filename: string): string => {
  const filePath = path.join(knowledgeDirectory, filename);

  return fs.readFileSync(filePath, "utf-8");
};

export const getKnowledge = (): string => {
  return `
================ EXPERIENCE ================

${readDocument("experience.md")}

================ PROJECTS ================

${readDocument("projects.md")}

================ SKILLS ================

${readDocument("skills.md")}
`;
};
