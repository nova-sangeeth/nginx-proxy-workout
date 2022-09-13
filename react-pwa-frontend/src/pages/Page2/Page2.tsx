import Step from "@mui/material/Step";
import StepContent from "@mui/material/StepContent";
import StepLabel from "@mui/material/StepLabel";
import Stepper from "@mui/material/Stepper";
import Typography from "@mui/material/Typography";

import Meta from "@/components/Meta";
import { FullSizeCenteredFlexBox } from "@/components/styled";

function Page2() {
  const steps = [
    {
      label: "Position 1",
      description: `content 1`,
    },
    {
      label: "Position 2",
      description: `content 2`,
    },
    {
      label: "Position 3",
      description: `content 3`,
    },
  ];
  return (
    <>
      <Meta title="Projects" />
      <FullSizeCenteredFlexBox>
        {/* <Typography variant="h5">Projects</Typography> */}

        <Stepper orientation="vertical">
          {steps.map((step, index) => (
            <Step key={step.label}>
              <StepLabel>{step.label}</StepLabel>
              <StepContent>{step.description}</StepContent>
            </Step>
          ))}
        </Stepper>
      </FullSizeCenteredFlexBox>
    </>
  );
}

export default Page2;
