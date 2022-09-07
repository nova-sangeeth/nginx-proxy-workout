import { Typography } from "@mui/material";
import Grid from "@mui/material/Grid";
import Box from "@mui/material/Grid";
import Paper from "@mui/material/Paper";

import { FullSizeCenteredFlexBox } from "@/components/styled";

const Stats = () => {
  return (
    <>
      <Grid container spacing={2} columns={16}>
        <Grid item xs={8}>
          <Paper>
            <Typography>Number of Hits today</Typography>
          </Paper>
        </Grid>
        <Grid item xs={8}>
          <Paper>
            <Typography>Total Number of Hits</Typography>
          </Paper>
        </Grid>
      </Grid>
      <Grid container spacing={2} columns={16}>
        <Grid item xs={8}>
          <Paper>
            <Typography>Version number</Typography>
          </Paper>
        </Grid>
        <Grid item xs={8}>
          <Typography>2</Typography>
        </Grid>
      </Grid>
      <Grid container spacing={2} columns={16}>
        <Grid item xs={8}>
          <Typography>1</Typography>
        </Grid>
        <Grid item xs={8}>
          <Typography>2</Typography>
        </Grid>
      </Grid>
    </>
  );
};

export default Stats;
