import GitHubCalendar from "react-github-calendar";

import Meta from "@/components/Meta";

import gitHubUsername from "./meta";

function GithubActivityBar() {
  console.log("Github Activity Bar.");
  return (
    <>
      <Meta title="Github Activity Bar" />
      <GitHubCalendar username={gitHubUsername} />
    </>
  );
}

export default GithubActivityBar;
