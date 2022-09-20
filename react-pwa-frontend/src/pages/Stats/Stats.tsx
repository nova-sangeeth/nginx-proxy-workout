import { useEffect, useState } from "react";
import { atom, useRecoilState } from "recoil";

import { Card, CardContent } from "@mui/material";
import { Typography } from "@mui/material";

import { FullSizeCenteredFlexBox } from "@/components/styled";

// create a recoil state.
const StatsState = atom<string>({
  key: "stat-item-1",
  default: "",
});

const Stats = () => {
  // const [statItem1, setStatItem1] = useState<string>("");
  // const [statItem2, setStatItem2] = useState<string>("");

  // use recoil state management.
  const [statItem1, setStatItem1] = useRecoilState(StatsState);

  const fetchStats = () => {
    const temp_values_1 = "updated state";

    setStatItem1(temp_values_1);
  };

  useEffect(() => {
    fetchStats();
  });

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
            {/* <Typography>{statItem2}</Typography> */}
          </CardContent>
        </Card>
      </FullSizeCenteredFlexBox>
    </>
  );
};

export default Stats;
