import Box from "@mui/material/Box";
import Button from "@mui/material/Button";
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
      label: "Project 1",
      description: `This is a fake description of project completed...`,
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
              <StepContent>
                {step.description}
                <Box sx={{ mb: 2 }}>
                  <Button variant="contained" sx={{ mt: 1, mr: 1 }}>
                    {index === steps.length - 1 ? "finish" : "continue"}
                  </Button>
                  <Button disabled={index === 0} sx={{ mt: 1, mr: 1 }}>
                    Back
                  </Button>
                </Box>
              </StepContent>
            </Step>
          ))}
        </Stepper>
      </FullSizeCenteredFlexBox>
    </>
  );
}

export default Page2;
