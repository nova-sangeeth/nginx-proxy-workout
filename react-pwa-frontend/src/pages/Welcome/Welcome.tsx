import GitHubCalendar from "react-github-calendar";
import { Typewriter } from "react-simple-typewriter";
import { animated, useSpring } from "react-spring";

import { Typography } from "@mui/material";
import Grid from "@mui/material/Grid";

import Meta from "@/components/Meta";
import SkillStepper from "@/components/SkillStepper";
import { FullSizeCenteredFlexBox } from "@/components/styled";
import useOrientation from "@/hooks/useOrientation";

import TechSkills from "../Page1/Page1";
import { Image } from "./styled";

function Welcome() {
  const isPortrait = useOrientation();
  const content_words = ["Hello There", "I'm Nova Sangeeth", "I'm a Full Stack Developer"];

  return (
    <>
      <Meta title="Welcome" />
      <FullSizeCenteredFlexBox flexDirection={isPortrait ? "column" : "row"}>
        <h1>
          <Typewriter words={content_words} loop={false} cursor={true} cursorStyle={"_"} />
        </h1>
      </FullSizeCenteredFlexBox>
      <FullSizeCenteredFlexBox flexDirection={isPortrait ? "column" : "row"}>
        <GitHubCalendar username="nova-sangeeth" />
      </FullSizeCenteredFlexBox>
      <FullSizeCenteredFlexBox flexDirection={isPortrait ? "column" : "row"}>
        <SkillStepper />
      </FullSizeCenteredFlexBox>
      <FullSizeCenteredFlexBox>
        <TechSkills />
      </FullSizeCenteredFlexBox>
    </>
  );
}

export default Welcome;
