# Statically Loading Native Modules

In ECMAScript 6.0 (ES6) module design, the **import** syntax is used to load content exported by other files, as defined by the ECMAScript specification. To help you import content exported from native modules (.so), ArkTS has adapted and provides the following methods:

#### Direct Import

Export content from the **index.d.ts** file of a native module, and then import the content to the file.

## Named Import

// index.d.ts corresponding to libentry.so
export const add: (a: number, b: number) => number;

// test.ets
import { add } from 'libentry.so'
add(2, 3);

## Default Import

// index.d.ts corresponding to libentry.so
export const add: (a: number, b: number) => number;

// test.ets
import entry from 'libentry.so'
entry.add(2, 3);

## Namespace Import

// index.d.ts corresponding to libentry.so
export const add: (a: number, b: number) => number;

// test.ets
import \* as entry from 'libentry.so'
entry.add(2, 3);

#### Indirect Import

## Export as Named Variables and Import

// index.d.ts corresponding to libentry.so
export const add: (a: number, b: number) => number;

// test1.ets
// Encapsulate the API of libentry.so and export it.
import { add } from 'libentry.so';
export { add };

// test2.ets
// Import APIs from the intermediate module.
import { add } from './test1';
const result = add(2, 3);

## Export as Namespaces and Import

// index.d.ts corresponding to libentry.so
export const add: (a: number, b: number) => number;

// test1.ets
export \* from 'libentry.so'

// test2.ets
import { add } from './test1'
add(2, 3);

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c6/v3/LbdNcjYzQJ29jzqO7o_brg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061925Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=8A02258DF8D1CEFA3058CA7BF6465FBE9AE94E5407E5D21BD7BE6D35A4E669F2)

Native modules do not support both export and import using namespaces simultaneously.

**Anti-example:**

// test1.ets
export \* from 'libentry.so'

// test2.ets
import \* as add from './test1'
// The add object cannot be obtained.

#### Dynamic Import

## Direct Import

// index.d.ts corresponding to libentry.so
export const add: (a: number, b: number) => number;

// test.ets
import('libentry.so').then((entry:ESObject) => {
    entry.default.add(2, 3);
})

## Indirect Import

// test1.ets
import entry from 'libentry.so'
export { entry }

// test2.ets
import('./test1').then((ns:ESObject) => {
    ns.entry.add(2, 3);
})

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ef/v3/TciHzEpKTBSmybZ8GL-QNQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061925Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=E8021991825C315B4DDD3FCAF30A7BA0D5E4E5D5DD8D98B7D3C29B6971EFB2EB)

Dynamic imports do not support exporting files using namespace exports.

**Anti-example:**

// test1.ets
export \* from 'libentry.so'

// test2.ets
import('./test1').then((ns:ESObject) => {
    // The ns object cannot be obtained.
})
