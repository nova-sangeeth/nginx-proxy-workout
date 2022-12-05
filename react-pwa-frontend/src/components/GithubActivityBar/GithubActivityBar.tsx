import GitHubCalendar from "react-github-calendar";

import Container from "@mui/material/Container";

import Meta from "@/components/Meta";

import gitHubUsername from "./meta";

function GithubActivityBar() {
  console.log("Github Activity Bar.");
  return (
    <Container disableGutters={true}>
      <Meta title="Github Activity Bar" />
      <h1>My Coding Activity</h1>
      <GitHubCalendar username={gitHubUsername} />
    </Container>
  );
}

export default GithubActivityBar;
