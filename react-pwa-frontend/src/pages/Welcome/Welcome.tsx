import { Typography } from "@mui/material";
import Grid from "@mui/material/Grid";

import Meta from "@/components/Meta";
import { FullSizeCenteredFlexBox } from "@/components/styled";
import useOrientation from "@/hooks/useOrientation";

import muiLogo from "./logos/mui.svg";
import pwaLogo from "./logos/pwa.svg";
import reactLogo from "./logos/react_ed.svg";
import recoilLogo from "./logos/recoil.svg";
import rrLogo from "./logos/rr.svg";
import tsLogo from "./logos/ts.svg";
import viteLogo from "./logos/vite.svg";
import { Image } from "./styled";

function Welcome() {
  const isPortrait = useOrientation();

  const width = isPortrait ? "40%" : "30%";
  const height = isPortrait ? "30%" : "40%";

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
              <h1>I'm Nova Sangeeth</h1>
            </Typography>
            <Typography>
              <h4>I am a Full Stack Developer</h4>
            </Typography>
          </Grid>
        </Grid>
      </FullSizeCenteredFlexBox>
    </>
  );
}

export default Welcome;
