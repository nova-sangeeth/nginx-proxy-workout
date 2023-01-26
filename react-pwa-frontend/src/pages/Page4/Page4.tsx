import { Link } from "react-router-dom";

import GitHubIcon from "@mui/icons-material/GitHub";
import LinkedInIcon from "@mui/icons-material/LinkedIn";
import Button from "@mui/material/Button";
import Typography from "@mui/material/Typography";
import Container from "@mui/material/Container";
import Meta from "@/components/Meta";
import { FullSizeCenteredFlexBox } from "@/components/styled";

function Page4() {
  return (
    <>
      <Meta title="Social" />
        <Container disableGutters={true}>
        <Typography variant="h3">Social</Typography>
        </Container>
        {/* <Button
          to={`/${Math.random().toString()}`}
          component={Link}
          variant="outlined"
          sx={{ mt: 4 }}
          size="small"
          color="warning"
        >
          Whant to check 404?
        </Button> */}
        <LinkedInIcon />
        <GitHubIcon />
    </>
  );
}

export default Page4;
