import { PrismaClient } from "@prisma/client";
import express from "express";

const app = express();
const prisma = new PrismaClient();

app.use(express.json());

app.listen(3000, () =>
  console.log("Express Server with Prisma Runs on port 3000")
);

// async function main() {
//   const newUser = await prisma.user.create({
//     data: {
//       name: "test",
//       email: "test@prisma.io",
//       posts: {
//         create: {
//           title: "Hello World",
//         },
//       },
//     },
//   });
//   console.log("Created new user: ", newUser);

//   const allUsers = await prisma.user.findMany({
//     include: { posts: true },
//   });
//   console.log("All users: ");
//   console.dir(allUsers, { depth: null });
// }

// main()
//   .catch((e) => console.error(e))
//   .finally(async () => await prisma.$disconnect());
