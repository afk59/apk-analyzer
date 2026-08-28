# How do I traverse JSON objects?

Refer to the code snippet below.

import { ArrayList } from '@kit.ArkTS';

interface Winner { num: number };
let tmpStr: Record<string, Winner> = JSON.parse('{ "0": {"num": 1}, "1": {"num": 2} }');
const arrayList: ArrayList<Winner> = new ArrayList();
Object.entries(tmpStr).forEach((item) => {
  const value = item\[1\];
  arrayList.add(value);
})
