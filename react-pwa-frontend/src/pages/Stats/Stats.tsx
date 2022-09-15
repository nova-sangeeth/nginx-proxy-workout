import { useEffect, useState } from "react";

import { Card, CardContent } from "@mui/material";
import { Typography } from "@mui/material";

import { FullSizeCenteredFlexBox } from "@/components/styled";

const Stats = () => {
  const [statItem1, setStatItem1] = useState<string>("");
  const [statItem2, setStatItem2] = useState<string>("");

  const fetchStats = () => {
    const temp_values_1 = "stat  1";
    const temp_values_2 = "stat state 2";

    setStatItem1(temp_values_1);
    setStatItem2(temp_values_2);
  };

  useEffect(() => {
    fetchStats();
  }, [statItem1]);

  return (
    <>
      <FullSizeCenteredFlexBox>
        <Card sx={{ minWidth: 375 }}>
          <CardContent>
            <Typography>Stat Card 1</Typography>
            <Typography>{statItem1}</Typography>
          </CardContent>
        </Card>
        <Card sx={{ minWidth: 375, marginLeft: 3 }}>
          <CardContent>
            <Typography>Stat Card 2</Typography>
            <Typography>{statItem2}</Typography>
          </CardContent>
        </Card>
      </FullSizeCenteredFlexBox>
    </>
  );
};

export default Stats;
