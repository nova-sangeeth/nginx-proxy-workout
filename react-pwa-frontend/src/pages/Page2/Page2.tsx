import Step from "@mui/material/Step";
import StepContent from "@mui/material/StepContent";
import StepLabel from "@mui/material/StepLabel";
import Stepper from "@mui/material/Stepper";
import Typography from "@mui/material/Typography";

import Meta from "@/components/Meta";
import { FullSizeCenteredFlexBox } from "@/components/styled";

function Page2() {
  return (
    <>
      <Meta title="Projects" />
      <FullSizeCenteredFlexBox>
        <Typography variant="h5">Projects</Typography>

        <Stepper  orientation="vertical">
          <Step>
            <StepLabel>Step 1</StepLabel>
            <StepContent></StepContent>
          </Step>
          <Step>
            <StepLabel>Step 2</StepLabel>
            <StepContent></StepContent>
          </Step>
          <Step>
            <StepLabel>Step 3</StepLabel>
            <StepContent></StepContent>
          </Step>
          <Step>
            <StepLabel>Step 4</StepLabel>
            <StepContent></StepContent>
          </Step>
        </Stepper>
      </FullSizeCenteredFlexBox>
    </>
  );
}

export default Page2;
