import Chip from "@mui/material/Chip";
import Container from "@mui/material/Container";
import Grid from "@mui/material/Grid";
import Paper from "@mui/material/Paper";
import Stack from "@mui/material/Stack";

import Meta from "@/components/Meta";

function TechSkills() {
  return (
    <>
      <Meta title="Tech Stack" />
      <Container disableGutters={true}>
        <h1>Tech Stack</h1>
        <h4>Languages</h4>
        <Stack direction="row" spacing={1}>
          <Chip label="Python" />
          <Chip label="JavaScript" />
          <Chip label="TypeScript" />
          <Chip label="SQL" />
          <Chip label="Bash" />
        </Stack>
        <h4>Frameworks</h4>
        <Stack direction="row" spacing={1}>
          <Chip label="FastAPI" />
          <Chip label="Django" />
          <Chip label="Flask" />
          <Chip label="Express" />
          <Chip label="React" />
          <Chip label="Vue" />
        </Stack>
        <h4>Containerization Technologies</h4>
        <Stack direction="row" spacing={1}>
          <Chip label="Docker" />
        </Stack>
        <h4>Versioning Systems</h4>
        <Stack direction="row" spacing={1}>
          <Chip label="Git" />
          <Chip label="GitHub" />
          <Chip label="GitLab" />
        </Stack>
        <h4>Cloud Providers</h4>
        <Stack direction="row" spacing={1}>
          <Chip label="Azure" />
          <Chip label="AWS" />
          <Chip label="DigitalOcean" />
        </Stack>
      </Container>
    </>
  );
}

export default TechSkills;
