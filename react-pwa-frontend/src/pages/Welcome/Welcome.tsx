import GitHubCalendar from "react-github-calendar";

import { Typography } from "@mui/material";
import Grid from "@mui/material/Grid";

import Meta from "@/components/Meta";
import { FullSizeCenteredFlexBox } from "@/components/styled";
import useOrientation from "@/hooks/useOrientation";

import { Image } from "./styled";

function Welcome() {
  const isPortrait = useOrientation();

  return (
    <>
      <Meta title="Welcome" />
      <FullSizeCenteredFlexBox flexDirection={isPortrait ? "column" : "row"}>
        <Grid container spacing={2}>
          <Grid item xs={8}>
            {/* <Typography><h1>Hello There</h1></Typography> */}
          </Grid>
          <Grid item xs={4}>
            <Typography>
              <h1>Hello There</h1>
            </Typography>
            <Typography>
              <h1>I am Nova Sangeeth</h1>
            </Typography>
            <Typography>
              <h4>I am a Full Stack Developer</h4>
            </Typography>
          </Grid>
        </Grid>
        <GitHubCalendar username="nova-sangeeth" />
      </FullSizeCenteredFlexBox>
    </>
  );
}

export default Welcome;
