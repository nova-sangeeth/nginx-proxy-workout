import Typography from '@mui/material/Typography';

import Meta from '@/components/Meta';
import { FullSizeCenteredFlexBox } from '@/components/styled';

function Page3() {
  return (
    <>
      <Meta title="About Me" />
      <FullSizeCenteredFlexBox>
        <Typography variant="h3">About Me</Typography>
      </FullSizeCenteredFlexBox>
    </>
  );
}

export default Page3;
