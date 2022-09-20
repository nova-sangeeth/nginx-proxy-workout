import { useEffect, useState } from "react";
import { atom, useRecoilState } from "recoil";

import { Card, CardContent } from "@mui/material";
import { Typography } from "@mui/material";

import { FullSizeCenteredFlexBox } from "@/components/styled";

// create a recoil state.
const statState1 = atom<string>({
  key: "stat-item-1",
  default: "",
});

const statState2 = atom<string>({
  key: "stat-item-2",
  default: ""
})
const Stats = () => {
  // const [statItem1, setStatItem1] = useState<string>("");
  // const [statItem2, setStatItem2] = useState<string>("");

  // use recoil state management.
  const [statItem1, setStatItem1] = useRecoilState(statState1);
  const [statItem2, setStatItem2] = useRecoilState(statState2);

  const fetchStats = () => {
    const temp_values_1 = "updated state";
    const temp_values_2 = "updated state data"

    setStatItem1(temp_values_1);
    setStatItem2(temp_values_2);
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
            <Typography>{statItem2}</Typography>
          </CardContent>
        </Card>
      </FullSizeCenteredFlexBox>
    </>
  );
};

export default Stats;
