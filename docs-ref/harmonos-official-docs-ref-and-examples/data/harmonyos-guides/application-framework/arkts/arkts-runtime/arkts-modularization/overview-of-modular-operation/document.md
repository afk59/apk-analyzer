# Overview of Modular Operation

To address challenges of large and complex application development—such as increased package size due to multiple copies of code during compilation, file dependencies, difficulties in sharing code and resources, and pollution of singletons and global variables—ArkTS supports modular compilation, packaging, and running. This approach not only streamlines the development process but also facilitates easier code writing and feature maintenance.

Modularization is the process of organizing ArkTS/TS/JS modules (where each file corresponds to a module), including so modules, and then [loading](#loading-process-of-modular-operation), parsing, combining, and executing these modules through compilation tools or runtime mechanisms.

ArkTS supports various module types, including ETS/TS/JS files, JSON files, and native modules. It adheres to both [ECMAScript module specifications](#ecmascript-module) and [CommonJS module specifications](#commonjs-module). In addition, ArkTS extends loading modes to include [dynamic import](../dynamic-import/document.md), static import, [lazy import](../lazy-import/document.md), [synchronous dynamic loading of native modules](../dynamically-loading-native-modules-in-synchronous-mode/document.md), and [loading files using Node-API](../loading-modules-using-node-api/document.md).

#### Loading Process of Modular Operation

ArkTS modular operation is implemented according to the ECMAScript module specification and executes modules using a post-order traversal method: starting from the leftmost subtree of the module graph, it executes the modules, then their peers, and finally their parents. This algorithm runs recursively until it reaches the root of the module graph.

For example, in the figure below, each parent node loads its corresponding child nodes and executes peers in the order specified by the **import** statements. The execution order for the module graph files is as follows: D->F->G->E->B->I->H->C->A.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/be/v3/PH7nA7mZRtqErhP_qei2mA/en-us_image_0000002537764388.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061925Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=3242F4E0C8BDCA3A51EB4EF60326DAEF7717F41C5C12FEC8189B1799B9FF2AB4)

Here, file A is referred to as the entry file, which is the starting point for execution. Certain built-in interfaces for loading content, such as [windowStage.loadContent](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-window-window#loadcontent9) and [Navigation](../../../../arkui/ui-development-arkts-based-declarative-development-paradigm/setting-component-navigation-and-page-routing/component-navigation-recommended/document.md), will also be executed as entry files, especially when these files are not loaded using the **import** syntax.

Starting from file A, a complete set of files will be loaded, including file A, files on which file A depends, and subsequently dependent files, until the leaf nodes of each branch is reached.

A regular module is loaded once in the same thread and multiple times in different threads, creating a new module object in each thread. If you only want to load the module once in a process, use the [shared module](../../../arkts-concurrency/inter-thread-communication/inter-thread-communication-objects/sendable-object/shared-module/document.md).

#### Modular Specifications Supported by ArkTS

## ECMAScript Module

ECMAScript modules (ES modules) are a module feature implemented in JavaScript starting from ECMAScript 6.0, standardized in the ECMAScript® 2025 Language Specification (tc39.es). The module functionality is composed of two commands: **export** and **import**.

For details about how to use **export** and **import** in ArkTS, see [ArkTS Introduction](../../../../../getting-started/learning-arkts/introduction-to-arkts/document.md#module).

## CommonJS Module

CommonJS modules were proposed as a standard by the JavaScript community in 2009 and first partially adopted and implemented in Node.js. CommonJS treats each file as a module, with the **module** variable representing the current module. **module.exports** is the variable exported by the module, and each module also has an **exports** variable (exports === module.exports).

The following table lists the module import and export syntax.

| Loading Type | Module Import | Module Export (Do Not Mix module.exports with exports) |
| :-- | :-- | :-- |
| Variable | const ohos = require('ohos') | exports.add = add or module.exports.name = name |
| Variable | const ohos = require('ohos') | module.exports = add |
| Function | 
const ohos = require('ohos')

ohos.fun();

 | exports.fun = function foo () {} or module.exports.fun = function foo () {} |

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/67/v3/Rcx87oPfTmaCqP0EbOJupQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061925Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=DC98955FA3542EA5DA90CE75566FEC4EA17A1171211B351014CAA9680079CA4E)

CommonJS modules can be used only to export third-party packages. They cannot be created or used in projects.

## Compatibility Between CommonJS and ES Modules

The following table lists the compatibility between CommonJS and ES modules, with the import and export syntax following their respective specifications.

| Inter-Module Reference | ES Module Export | CommonJS Export |
| :-- | :-- | :-- |
| ES Module Import | Supported | Supported |
| CommonJS Import | Not supported | Supported |

#### Module Types Supported by ArkTS

## ETS/TS/JS

When loading the ETS, TS, and JS modules, you need to comply with the [ECMAScript module specifications](#ecmascript-module) and [CommonJS module specifications](#commonjs-module).

## JSON File

JavaScript Object Notation (JSON) is a lightweight data interchange format that uses a text-based format independent of any programming language to store and represent data.

JSON files can only be imported using the **default** method, as shown below:

import data from './example.json'

## Native Module

The syntax specifications for importing and exporting the native module (.so) are the same as those for loading the ETS, TS, and JS files. Native modules (.so files) follow the same import/export and loading syntax as ETS/TS/JS modules. For details, see [Statically Loading Native Modules](../statically-loading-native-modules/document.md).

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b8/v3/TotF6y0wQu-UZ3lk9wNU_w/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061925Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=592722EE50E4EB1E39B931DCDDCF311DA5C32DEC622E435CA9B3BB7B208EEE6D)

Native modules cannot be imported to CommonJS modules.

Example:

// index.d.ts corresponding to libentry.so
export const add: (a: number, b: number) => number;

// test.ets
import { add } from 'libentry.so'
add(2, 3)
