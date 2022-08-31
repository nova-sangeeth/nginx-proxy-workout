import Typography from '@mui/material/Typography';

import Meta from '@/components/Meta';
import { FullSizeCenteredFlexBox } from '@/components/styled';

function Page1() {
  return (
    <>
      <Meta title="Tech Stack" />
      <FullSizeCenteredFlexBox>
        <Typography variant="h3">Tech Stack</Typography>
      </FullSizeCenteredFlexBox>
    </>
  );
}

export default Page1;
