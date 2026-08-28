# How do I export native APIs from multiple xxx.d.ts files?

**Question**

The C++ library is large and a large number of APIs need to be exposed. Can I split the C++ library into multiple .d.ts files and export the APIs?

**Answer**

The **types** field in **oh-package.json5** can specify only one value. To solve the problem, you can define all the APIs in a file and then re-export them from your main file.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a7/v3/dtoeBYDlSpmtORXFSiYJQw/en-us_image_0000002194318472.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062546Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=A9CED105E11C5A06F1FFD62650CA1BF2EFEB8913A836981CF9DA11210258C454 "Click to enlarge")

Do as follows:

Declare all the native APIs in the **index1.d.ts** file, and then use the **index.d.ts** file to re-export the APIs to ArkTS.

Export APIs from the **index1.d.ts** file.

export const sub: (a: number, b: number) => number;

Re-export the APIs in the **index.d.ts** file.

export {sub} from './index1'
export const add: (a: number, b: number) => number;
