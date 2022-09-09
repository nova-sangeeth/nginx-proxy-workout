import AddTaskIcon from "@mui/icons-material/AddTask";
import BugReportIcon from "@mui/icons-material/BugReport";
import GitHubIcon from "@mui/icons-material/GitHub";
import HomeIcon from "@mui/icons-material/Home";
import QueryStatsIcon from "@mui/icons-material/QueryStats";
import TerrainIcon from "@mui/icons-material/Terrain";

import asyncComponentLoader from "@/utils/loader";

import { Pages, Routes } from "./types";

const routes: Routes = {
  [Pages.Welcome]: {
    component: asyncComponentLoader(() => import("@/pages/Welcome")),
    path: "/",
    title: "Welcome",
    icon: HomeIcon,
  },
  [Pages.Page1]: {
    component: asyncComponentLoader(() => import("@/pages/Page1")),
    path: "/tech-stack",
    title: "Tech Stack",
    icon: GitHubIcon,
  },
  [Pages.Page2]: {
    component: asyncComponentLoader(() => import("@/pages/Page2")),
    path: "/projects",
    title: "Projects",
    icon: AddTaskIcon,
  },
  [Pages.Page3]: {
    component: asyncComponentLoader(() => import("@/pages/Page3")),
    path: "/about-me",
    title: "About Me",
    icon: TerrainIcon,
  },
  [Pages.Page4]: {
    component: asyncComponentLoader(() => import("@/pages/Page4")),
    path: "/social",
    title: "Social",
    icon: BugReportIcon,
  },
  [Pages.Stats]: {
    component: asyncComponentLoader(() => import("@/pages/Stats")),
    path: "/stats",
    title: "Stats",
    icon: QueryStatsIcon,
  },
  [Pages.NotFound]: {
    component: asyncComponentLoader(() => import("@/pages/NotFound")),
    path: "*",
  },
};

export default routes;
