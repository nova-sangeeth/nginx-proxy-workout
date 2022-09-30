import { atom } from "recoil";

const statState1 = atom<string>({
  key: "stat-item-1",
  default: "",
});

const statState2 = atom<string>({
  key: "stat-item-2",
  default: "",
});

export { statState1, statState2 };
