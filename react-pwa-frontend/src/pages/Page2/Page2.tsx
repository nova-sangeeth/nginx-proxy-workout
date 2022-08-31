import Typography from '@mui/material/Typography';

import Meta from '@/components/Meta';
import { FullSizeCenteredFlexBox } from '@/components/styled';

function Page2() {
  return (
    <>
      <Meta title="Projects" />
      <FullSizeCenteredFlexBox>
        <Typography variant="h3">Projects</Typography>
      </FullSizeCenteredFlexBox>
    </>
  );
}

export default Page2;
