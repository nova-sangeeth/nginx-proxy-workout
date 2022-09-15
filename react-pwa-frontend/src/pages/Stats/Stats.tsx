import { Card, CardActions, CardContent } from "@mui/material";
import { Typography } from "@mui/material";
import { Theme, createStyles, makeStyles } from "@mui/material";

import { FullSizeCenteredFlexBox } from "@/components/styled";

const Stats = () => {
  return (
    <>
      <FullSizeCenteredFlexBox>
        <Card sx={{ minWidth: 375 }}>
          <CardContent>
            <Typography>Stat Card 1</Typography>
            <Typography>Stat Content</Typography>
          </CardContent>
        </Card>
        <Card sx={{ minWidth: 375 }}>
          <CardContent>
            <Typography>Stat Content</Typography>
          </CardContent>
        </Card>
      </FullSizeCenteredFlexBox>
    </>
  );
};

export default Stats;
