# What should I do if "The re-export name 'xx' need to be marked as type" is reported during compilation?

**Symptom**

After DevEco Studio is upgraded to 3.1 Beta2 Release, the warning "The re-export name 'T' need to be marked as type, please use 'export type'" is displayed during the compilation of a project using API version 9 in the stage model.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6b/v3/x3CpN5yTR_KVGAsV_Yu2rg/en-us_image_0000002229604241.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062616Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=C0B7EBEB8CB60E5919299A580C788C093BFB2D258B806FDE7559A4A5115BC96C)

**Solution**

Modular compilation is enabled by default in DevEco Studio 3.1 Beta2 Release. If the **re-export** syntax exists in the application, a warning will be triggered. The following example should be avoided:

  // index.ets
  import {test} from "./test"
  export {test}
  let b : test = {a : 'index'}

  // test.ets
  export interface test {
    a: string
  }
  let obj : test = {a : 'string'}

The type symbol declared in the .ets or .ts module will be eliminated in the compiled .js module, while the **import** statement will be retained. If an explicit **type** symbol is not added to the import statement, the corresponding type symbol cannot be found.

In this case, you can add an explicit **type** symbol to the **import** statement so that the .js module can find the type-related imports during runtime.

import type {test} from "./test"  //Here, add a type declaration
export {test}
let b : test = {a : 'index'}

// test.ets
export interface test {
  a: string
}
let obj : test = {a : 'string'}
