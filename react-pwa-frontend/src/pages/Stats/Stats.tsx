import Grid from "@mui/material/Grid";
import Box from "@mui/material/Grid";
import Paper from "@mui/material/Paper";
import { FullSizeCenteredFlexBox } from "@/components/styled";

const Stats = () => {
  return (
    <>
      <Grid container spacing={2} columns={16}>
        <Grid item xs={8}>
          <h1>1</h1>
        </Grid>
        <Grid item xs={8}>
          <h1>2</h1>
        </Grid>
      </Grid>
      <Grid container spacing={2} columns={16}>
        <Grid item xs={8}>
          <h1>1</h1>
        </Grid>
        <Grid item xs={8}>
          <h1>2</h1>
        </Grid>
      </Grid>
      <Grid container spacing={2} columns={16}>
        <Grid item xs={8}>
          <h1>1</h1>
        </Grid>
        <Grid item xs={8}>
          <h1>2</h1>
        </Grid>
      </Grid>
    </>
  );
};

export default Stats;
