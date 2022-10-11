import Card from "@mui/material/Card";
import CardContent from "@mui/material/CardContent";
import Typography from "@mui/material/Typography";

import Meta from "@/components/Meta";
import { FullSizeCenteredFlexBox } from "@/components/styled";

function Page3() {
  return (
    <>
      <Meta title="About Me" />
      <FullSizeCenteredFlexBox>
        <Card sx={{ minWidth: 275 }}>
          <CardContent>
            <Typography>About me Content</Typography>
            <Typography>Hello There</Typography>
            <Typography>
              I am a full Stack developer who is passionate about technology and building ideal
              appications to solve real world problems.
            </Typography>
          </CardContent>
        </Card>
      </FullSizeCenteredFlexBox>
    </>
  );
}

export default Page3;
