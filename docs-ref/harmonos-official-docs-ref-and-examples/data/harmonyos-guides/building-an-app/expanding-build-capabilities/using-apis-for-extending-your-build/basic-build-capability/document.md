# Basic Build Capability

#### hvigor Object

**hvigor** is a predefined object used to indicate an instance of the hvigor build engine being executed. You can use this object to obtain build information and perform related operations.

## Modules to Import

import { hvigor } from '@ohos/hvigor';

## getRootNode

getRootNode(): HvigorNode

Obtains the node object of the root project. This API must be used in the [nodesInitialized and later phases](../../../overview/build-system-lifecycle/document.md#section746253616316). Otherwise, an error is reported.

**Since**: Hvigor 4.3.0

**Return value**

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

[HvigorNode](#section14832104719474)

 | 

Root **HvigorNode** object.

 |

**Example**: Obtaining the root node object

import { hvigor } from '@ohos/hvigor';
const rootNode = hvigor.getRootNode();

## getAllNodes

getAllNodes(): HvigorNode\[\]

Obtains an array of all nodes. Make sure the node is initialized before calling this API. Attempting to call it before initialization will result in an error.

**Since**: Hvigor 4.3.0

**Return value**

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

[HvigorNode](#section14832104719474)\[\]

 | 

Array of all **HvigorNode** objects.

 |

**Example**: Obtaining an array of all node objects

import { hvigor } from '@ohos/hvigor';
const allNodes = hvigor.getAllNodes();

## getNodeByName

getNodeByName(nodeName: string): HvigorNode | undefined

Obtains a node object based on the node name. Make sure the node is initialized before calling this API. Attempting to call it before initialization will result in an error.

**Since**: Hvigor 4.3.0

**Parameters**

| 
Name

 | 

Type

 | 

Mandatory

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

nodeName

 | 

string

 | 

Yes

 | 

Node name.

 |

**Return value**

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

[HvigorNode](#section14832104719474) | undefined

 | 

Node object found based on the name. If the node object does not exist, **undefined** is returned.

 |

**Example**: Obtaining a node object by node name

import { hvigor } from '@ohos/hvigor';
const entryNode = hvigor.getNodeByName('entry');

## getHvigorConfig

getHvigorConfig(): HvigorConfig

Obtains this **HvigorConfig** object.

**Since**: Hvigor 4.3.0

**Return value**

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

[HvigorConfig](#section7253174081515)

 | 

**HvigorConfig** object.

 |

**Example**: Obtaining the current **HvigorConfig** object

import { hvigor } from '@ohos/hvigor';
const hvigorConfig = hvigor.getHvigorConfig();

## getParameter

getParameter(): Parameter

Obtains this **Parameter** object.

**Since**: Hvigor 4.3.0

**Return value**

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

[Parameter](#section18886457152915)

 | 

**Parameter** object.

 |

**Example**: Obtaining the current **Parameter** object

import { hvigor } from '@ohos/hvigor';
const parameter = hvigor.getParameter();

## getHvigorVersion

getHvigorVersion(): string

Obtains the Hvigor version number.

**Since**: Hvigor 6.22.3

**Return value**

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

string

 | 

Hvigor version.

 |

**Example**

import { hvigor } from '@ohos/hvigor';
const hvigorVersion = hvigor.getHvigorVersion();

## configEvaluated

configEvaluated(fn: (HvigorConfig) => {}): void

Adds a callback function after the config file is evaluated.

**Since**: Hvigor 4.3.0

**Parameters**

| 
Name

 | 

Type

 | 

Mandatory

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

fn

 | 

([HvigorConfig](#section7253174081515)) => {}

 | 

Yes

 | 

A method whose input parameter is empty or **hvigorConfig**.

 |

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/25/v3/CZpcKxrTQ6mSyFUNBhrw7g/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062156Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=18826CBA6D8C398F051FF45F13483D003224D891DB88F84FB96A5D699DA77750)

This API is effective only when included in the [hvigorconfig.ts](../../../overview/build-system-lifecycle/document.md#section810245135914) file and is executed in the initialization phase of the build lifecycle.

**Example**: Registering the **configEvaluated** hook

// hvigorconfig.ts file
import { hvigor } from '@ohos/hvigor'
hvigor.configEvaluated(hvigorConfig => {
    console.log('configEvaluated');
})

## beforeNodeEvaluate

beforeNodeEvaluate(fn: (HvigorNode) => {}): void

Adds a callback function before node evaluation for all nodes.

**Since**: Hvigor 4.3.0

**Parameters**

| 
Name

 | 

Type

 | 

Mandatory

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

fn

 | 

([HvigorNode](#section14832104719474)) => {}

 | 

Yes

 | 

A method whose input parameter is empty or an **HvigorNode** object.

 |

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/56/v3/HJkIv_OATiaeoTFX0SgHjQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062156Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=0795B402CD8D9B1D761A2A118680350C19207D0A5C2D4898FED923E1B44141C9)

This API is effective only when included in the [hvigorconfig.ts](../../../overview/build-system-lifecycle/document.md#section810245135914) file and is executed in the initialization phase of the build lifecycle.

**Example**: Registering the **beforeNodeEvaluate** hook

// hvigorconfig.ts file
import { hvigor } from '@ohos/hvigor';
hvigor.beforeNodeEvaluate(hvigorNode => {
    console.log('beforeNodeEvaluate');
})

## afterNodeEvaluate

afterNodeEvaluate(fn: (HvigorNode) => {}): void

Adds a callback function after node evaluation for all nodes.

**Since**: Hvigor 4.3.0

**Parameters**

| 
Name

 | 

Type

 | 

Mandatory

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

fn

 | 

([HvigorNode](#section14832104719474)) => {}

 | 

Yes

 | 

A method whose input parameter is empty or an **HvigorNode** object.

 |

**Example**: Registering the **afterNodeEvaluate** hook

import { hvigor } from '@ohos/hvigor';
hvigor.afterNodeEvaluate(hvigorNode => {
    console.log('afterNodeEvaluate');
})

## nodesInitialized

nodesInitialized(fn: (Hvigor) => {}): void

Adds a callback function for completing node initialization.

**Since**: Hvigor 4.3.0

**Parameters**

| 
Name

 | 

Type

 | 

Mandatory

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

fn

 | 

([Hvigor](#section64891890155)) => {}

 | 

Yes

 | 

A method whose input parameter is empty or an **Hvigor** object.

 |

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d9/v3/adOVyBOKQjy35OoIvzRyog/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062156Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=BB72083198E5E9B917FE4B0A2F9C7F3B0D0FC485874C803FDE92FEA64EA23277)

This API is effective only when included in the [hvigorconfig.ts](../../../overview/build-system-lifecycle/document.md#section810245135914) file and is executed in the initialization phase of the build lifecycle.

**Example**: Registering the **nodesInitialized** hook

// hvigorconfig.ts file
import { hvigor } from '@ohos/hvigor';
hvigor.nodesInitialized(() => {
    console.log('nodesInitialized');
})

## nodesEvaluated

nodesEvaluated(fn: (Hvigor) => {}): void

Called when the hvigor configuration is complete. This callback should be used before the hvigor configuration is complete. You can add this callback in the configuration phase to perform deferred tasks, such as obtaining node plug-in context or registering a task. The added callbacks are stored in a queue and follow the first in first out (FIFO) approach, which allows the first callback added to be invoked first.

**Since**: Hvigor 4.0.2

**Parameters**

| 
Name

 | 

Type

 | 

Mandatory

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

fn

 | 

([Hvigor](#section64891890155)) => {}

 | 

Yes

 | 

A method whose input parameter is empty or an **Hvigor** object.

 |

**Example**: Obtaining the plugin context of a subnode

In Hvigor, the project node plug-ins are loaded prior to the module node plug-ins. You can use this API to obtain the context of the task registered by a subnode. The callback added will be invoked after all nodes are loaded.

import { hvigor } from '@ohos/hvigor';
import { OhosHapContext, OhosPluginId } from "@ohos/hvigor-ohos-plugin";
hvigor.nodesEvaluated(() => {
   // Obtain subnode information after all nodes are loaded.
  hvigor.getRootNode().subNodes(subNode => {
    const hapContext = subNode.getContext(OhosPluginId.OHOS\_HAP\_PLUGIN) as OhosHapContext;
  });
});

## taskGraphResolved

taskGraphResolved(fn: (Hvigor) => {}): void

Adds a callback function for completing graph parsing.

**Since**: Hvigor 4.3.0

**Parameters**

| 
Name

 | 

Type

 | 

Mandatory

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

fn

 | 

([Hvigor](#section64891890155)) => {}

 | 

Yes

 | 

A method whose input parameter is empty or an **Hvigor** object.

 |

**Example**: Adding a callback function for graph parsing completion

import { hvigor } from '@ohos/hvigor';
hvigor.taskGraphResolved(() => {
    console.log('taskGraphResolved');
});

## buildFinished

buildFinished(fn: (BuildResult) => {}): void

Adds a callback function for finishing the build.

**Since**: Hvigor 4.3.0

**Parameters**

| 
Name

 | 

Type

 | 

Mandatory

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

fn

 | 

([BuildResult](#section1476618469121)) => {}

 | 

Yes

 | 

A method whose input parameter is empty or a **BuildResult** object.

 |

**Example**: Obtaining the build completion information and, if the build fails, printing out the information

import { hvigor } from '@ohos/hvigor';
hvigor.buildFinished(buildResult => {
  if (buildResult.getError()) {
    console.log(buildResult.getError().stack);
  }
})

## getCommandEntryTask

getCommandEntryTask(): string\[\] | undefined

Obtains the array of names of the entry tasks for the build.

**Since**: Hvigor 4.3.0

**Return value**

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

string\[\] | undefined

 | 

Array of names of the entry tasks for the build. If the entry tasks do not exist, **undefined** is returned.

 |

**Example**: Obtaining the entry task and printing it out

import { hvigor } from '@ohos/hvigor';
console.log(hvigor.getCommandEntryTask());

## isCommandEntryTask

isCommandEntryTask(taskName: string): boolean

Checks whether this task is an entry task for the command.

**Since**: Hvigor 4.3.0

**Parameters**

| 
Name

 | 

Type

 | 

Mandatory

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

taskName

 | 

string

 | 

Yes

 | 

Task name

 |

**Return value**

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

boolean

 | 

Whether the task is an entry task.

 |

**Example**: Checking whether the task is an **assembleHap** task and printing it out

import { hvigor } from '@ohos/hvigor';
console.log(hvigor.isCommandEntryTask('assembleHap'));

#### getNode

getNode(scriptPath: string): HvigorNode | undefined

Obtains the current node object by passing the **hvigorfile.ts** script file path. If the input parameter **scriptPath** does not point to the **hvigorfile.ts** file in the project, **undefined** is returned.

**Since**: Hvigor 4.0.2

**Parameters**

| 
Name

 | 

Type

 | 

Mandatory

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

scriptPath

 | 

string

 | 

Yes

 | 

Full path of the **hvigorfile.ts** file.

 |

**Return value**

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

[HvigorNode](#section14832104719474) | undefined

 | 

hvigor node object. If the input parameter **scriptPath** does not point to the **hvigorfile.ts** file in the project, **undefined** is returned.

 |

**Example**: Obtaining the current node object

import { getNode } from "@ohos/hvigor";
const node = getNode(\_\_filename);

#### BuildResult

Represents an object that encapsulates the build result; if the build ends exceptionally, it will contain information about the exception.

## getError

getError(): Error | null

Obtains the error information. If no error occurs, **null** is returned.

**Since**: Hvigor 4.3.0

**Return value**

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

Error | null

 | 

Error information. If no error occurs, **null** is returned.

 |

**Example**: Obtaining the build completion information and, if the build fails, printing out the information

import { hvigor } from '@ohos/hvigor';
hvigor.buildFinished(buildResult => {
  if (buildResult.getError()) {
    console.log(buildResult.getError().stack);
  }
})

## getReportJson

getReportJson(): any

Obtains the visualization record **report.json** for this build.

**Since**: Hvigor 5.0.10

**Return value**

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

any

 | 

Visualization record **report.json** for the current build.

 |

different types of build events have different structures; the following is a typical structure example:

// report.json
{
  "version": "2.0", // Fixed field
  "ppid": 524, // process.ppid
  "events": \[ // Build event
    ...
    {
      "head": {
        "id": "61068546-11d9-49d0-baa7-733e167af7d6", // Event ID
        "name": "Finished :entry:default@PreBuild", // Event name
        "description": "Pre-build in the stage model.",// Description
        "type": "log" // Type
      },
      "body": {
        "pid": 3960, // process.pid
        "tid": "Main Thread", // thread id
        "startTime": 1280741873226000, // Start time
        "endTime": 1280741896325200, // End time
        "totalTime": 22868300 // Total time
      },
      "additional": {
        "logType": "info", // Log type
        "children": \[\], // Child event ID list
      }
    }
  \],
  "workLog": \[\]
}

**Example**

// Project-level hvigorfile.ts file
import { appTasks } from '@ohos/hvigor-ohos-plugin';
import { hvigor, FileUtil } from '@ohos/hvigor';

hvigor.buildFinished(buildResult => {
  // Write data to the file in the specified path.
  const json5FilePath = FileUtil.pathResolve('D:\\\\', 'testJson.json5');
  FileUtil.ensureFileSync(json5FilePath);
  FileUtil.writeFileSync(json5FilePath, JSON.stringify(buildResult.getReportJson(), null, 2));
})

export default {
    system: appTasks,  /\* Built-in plugin of Hvigor. It cannot be modified. \*/
    plugins:\[\]         /\* Custom plugin to extend the functionality of Hvigor. \*/
}

#### HvigorConfig

Represents an object used to save the description of each node before the node object is created.

## getRootNodeDescriptor

getRootNodeDescriptor(): HvigorNodeDescriptor

Obtains the descriptor object of the root node.

**Since**: Hvigor 4.3.0

**Return value**

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

[HvigorNodeDescriptor](#section1914012226435)

 | 

Descriptor object of the root node.

 |

**Example**: Obtaining an array of all node descriptor objects

import { hvigor } from '@ohos/hvigor';
const rootNodeDescriptor = hvigor.getHvigorConfig().getRootNodeDescriptor();

## getAllNodeDescriptor

getAllNodeDescriptor(): HvigorNodeDescriptor\[\]

Obtains an array of all node descriptor objects.

**Since**: Hvigor 4.3.0

**Return value**

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

[HvigorNodeDescriptor](#section1914012226435)\[\]

 | 

Array of all node descriptor objects.

 |

**Example**

import { hvigor } from '@ohos/hvigor';
const allNodeDescriptors = hvigor.getHvigorConfig().getAllNodeDescriptor();

## getNodeDescriptorByName

getNodeDescriptorByName(name: string): HvigorNodeDescriptor

Obtains a node descriptor object by node name.

**Since**: Hvigor 4.3.0

**Parameters**

| 
Name

 | 

Type

 | 

Mandatory

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

name

 | 

string

 | 

Yes

 | 

Node name.

 |

**Return value**

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

[HvigorNodeDescriptor](#section1914012226435)

 | 

Node descriptor object obtained by node name.

 |

**Example**

import { hvigor } from '@ohos/hvigor';
const entryNodeDescriptors = hvigor.getHvigorConfig().getNodeDescriptorByName('entry');

## includeNode

includeNode(name: string, srcPath: string, extraOptions?: Record<string, any>): void

Includes a node.

**Since**: Hvigor 5.4.0

**Parameters**

| 
Name

 | 

Type

 | 

Mandatory

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

name

 | 

string

 | 

Yes

 | 

Node name.

 |
| 

srcPath

 | 

string

 | 

Yes

 | 

Source path of the node.

 |
| 

extraOptions

 | 

Record<string, any>

 | 

No

 | 

Extra configuration, which will be parsed as the targets of the node.

 |

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/64/v3/f7TjkYY1SM2DDzCp3dwdwA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062156Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=E7C30BD60B26E50EDCD18321E66E7831E461E79DB69CE88CC718CD060F60B05E)

This API is effective only when included in the [hvigorconfig.ts](../../../overview/build-system-lifecycle/document.md#section810245135914) file and is executed in the initialization phase of the build lifecycle.

**Example 1**: Adding a node named **exampleNodeName** without extra configuration information

// hvigorconfig.ts file
import { hvigor } from '@ohos/hvigor';

const hvigorConfig = hvigor.getHvigorConfig();
hvigorConfig.includeNode('exampleNodeName', './exampleNodeName');

**Example 2**: Adding a node named **exampleNodeName** with **targets** information

// hvigorconfig.ts file
import { hvigor } from '@ohos/hvigor';

const hvigorConfig = hvigor.getHvigorConfig();
hvigorConfig.includeNode('exampleNodeName', './exampleNodeName', {
  "targets": \[
    {
      "name": "default",
      "applyToProducts": \[
        "default"
      \]
    },
    {
      "name": "targetTest1",
      "applyToProducts": \[
        "default"
      \]
    }
  \]
});

## excludeNodeByName

excludeNodeByName(name: string): void

Excludes a node by name.

DevEco Studio 6.0.0 Beta3 and later versions allow you to exclude missing modules from the project. For details, see [Executing ohpm install Using Hvigor](../../../improving-build-efficiency/enabling-performance-optimization-experimental-features/document.md#section11663628141317).

**Since**: Hvigor 5.4.0

**Parameters**

| 
Name

 | 

Type

 | 

Mandatory

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

name

 | 

string

 | 

Yes

 | 

Node name.

 |

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/35/v3/Dl_vt-ZsSPe3l1nXyiHn3g/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062156Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=F9E6C7E87B2C72C4229E9615D90E0F88343B065075A72333CDD83B4D8EBF27C0)

This API is effective only when included in the [hvigorconfig.ts](../../../overview/build-system-lifecycle/document.md#section810245135914) file and is executed in the initialization phase of the build lifecycle.

**Example**: Excluding the node named **exampleNodeName**

// hvigorconfig.ts file
import { hvigor } from '@ohos/hvigor';

const hvigorConfig = hvigor.getHvigorConfig();
hvigorConfig.excludeNodeByName('exampleNodeName');

#### HvigorNodeDescriptor

Represents a node descriptor object of hvigor. hvigor uses this object to construct the **hvigorNode** object during the build process.

## Properties

| 
Member

 | 

Type

 | 

Read-Only

 | 

Description

 | 

Available Since

 |
| :-- | :-- | :-- | :-- | :-- |
| 

name

 | 

string

 | 

No

 | 

Node name.

 | 

Hvigor 4.3.0

 |
| 

srcPath

 | 

string

 | 

No

 | 

Source path of the node.

 | 

Hvigor 4.3.0

 |
| 

extraOptions

 | 

Map<string, any>

 | 

No

 | 

Custom properties to save passed data.

 | 

Hvigor 4.3.0

 |

## getChildNode

getChildNode(): HvigorNodeDescriptor\[\] | undefined

Obtains all child node descriptors; returns **undefined** if no child nodes exist.

**Since**: Hvigor 4.3.0

**Return value**

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

[HvigorNodeDescriptor](#section1914012226435)\[\] | undefined

 | 

All child node descriptor objects. **undefined** is returned if no child nodes exist.

 |

**Example**

// [hvigorconfig.ts](../../../overview/build-system-lifecycle/document.md#li194356217319)
import { hvigorConfig } from '@ohos/hvigor';
const rootNodeDescriptors = hvigorConfig.getRootNodeDescriptor();
rootNodeDescriptors.getChildNode()?.forEach(child => {
  console.log(\`child: ${child.name}\`);
});

## getRootNode

getRootNode(): HvigorNodeDescriptor

Obtains the descriptor object of the root node.

**Since**: Hvigor 4.3.0

**Return value**

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

[HvigorNodeDescriptor](#section1914012226435)

 | 

Descriptor object of the root node.

 |

**Example**

// [hvigorconfig.ts](../../../overview/build-system-lifecycle/document.md#li194356217319)
import { hvigorConfig } from '@ohos/hvigor';
const entryNodeDescriptor = hvigorConfig.getNodeDescriptorByName('entry');
console.log(\`rootNode name: ${entryNodeDescriptor.getRootNode().name}\`);

#### Product

Provides product information APIs in the project-level configuration for HarmonyOS app building. Before calling this API, you can use the [getCurrentProduct](../plug-in-context/document.md#section962214395515) method of **OhosAppContext** to obtain the object.

## Importing Modules

import { Product } from '@ohos/hvigor-ohos-plugin';

## getProductName

getProductName: () => string

Obtains the product name.

**Return value**

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

string

 | 

Product name.

 |

Sample code for the project-level **hvigorfile.ts** file:

import { hvigor, HvigorNode, HvigorPlugin } from '@ohos/hvigor';
import { appTasks, OhosAppContext, OhosPluginId, Product } from '@ohos/hvigor-ohos-plugin';

// Implement a custom plugin.
export function customPlugin(): HvigorPlugin {
    return {
        pluginId: 'customPlugin',
        async apply(currentNode: HvigorNode): Promise<void> {
            hvigor.nodesEvaluated(async () => {
                const context: OhosAppContext = currentNode.getContext(OhosPluginId.OHOS\_APP\_PLUGIN) as OhosAppContext;
                const currentProduct: Product = context.getCurrentProduct();
                console.log(currentProduct.getProductName());
            });
        }
    };
}
export default {
    system: appTasks,  /\* Built-in plugin of Hvigor. It cannot be modified. \*/
    plugins:\[customPlugin()\]         /\* Custom plugin to extend the functionality of Hvigor. \*/
}

## getBundleType

getBundleType: () => string

Obtains the value of **bundleType** used by the product.

**Return value**

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

string

 | 

Value of **bundleType**.

 |

Sample code for the project-level **hvigorfile.ts** file:

import { hvigor, HvigorNode, HvigorPlugin } from '@ohos/hvigor';
import { appTasks, OhosAppContext, OhosPluginId, Product } from '@ohos/hvigor-ohos-plugin';

// Implement a custom plugin.
export function customPlugin(): HvigorPlugin {
    return {
        pluginId: 'customPlugin',
        async apply(currentNode: HvigorNode): Promise<void> {
            hvigor.nodesEvaluated(async () => {
                const context: OhosAppContext = currentNode.getContext(OhosPluginId.OHOS\_APP\_PLUGIN) as OhosAppContext;
                const currentProduct: Product = context.getCurrentProduct();
                console.log(currentProduct.getBundleType());
            });
        }
    };
}
export default {
    system: appTasks,  /\* Built-in plugin of Hvigor. It cannot be modified. \*/
    plugins:\[customPlugin()\]         /\* Custom plugin to extend the functionality of Hvigor. \*/
}

## getBundleName

getBundleName: () => string

Obtains the value of **bundleName** used by the product.

**Return value**

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

string

 | 

Value of **bundleName**.

 |

Sample code for the project-level **hvigorfile.ts** file:

import { hvigor, HvigorNode, HvigorPlugin } from '@ohos/hvigor';
import { appTasks, OhosAppContext, OhosPluginId, Product } from '@ohos/hvigor-ohos-plugin';

// Implement a custom plugin.
export function customPlugin(): HvigorPlugin {
    return {
        pluginId: 'customPlugin',
        async apply(currentNode: HvigorNode): Promise<void> {
            hvigor.nodesEvaluated(async () => {
                const context: OhosAppContext = currentNode.getContext(OhosPluginId.OHOS\_APP\_PLUGIN) as OhosAppContext;
                const currentProduct: Product = context.getCurrentProduct();
                console.log(currentProduct.getBundleName());
            });
        }
    };
}
export default {
    system: appTasks,  /\* Built-in plugin of Hvigor. It cannot be modified. \*/
    plugins:\[customPlugin()\]         /\* Custom plugin to extend the functionality of Hvigor. \*/
}

#### Target

Provides target information APIs in the module-level configuration for HarmonyOS app building.

## Importing Modules

import { Target } from '@ohos/hvigor-ohos-plugin';

## getCurrentProduct

getCurrentProduct: () => Product

Obtains the product configured for the current target.

**Return value**

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

[Product](#section1553414254713)

 | 

**Product** object for the target build.

 |

**Example**

// Project-level hvigorfile.ts file
import { appTasks, OhosHapContext, OhosPluginId, Target } from '@ohos/hvigor-ohos-plugin';
import { hvigor, HvigorNode } from '@ohos/hvigor';

hvigor.nodesEvaluated(() => {
    const rootNode = hvigor.getRootNode();
    rootNode.subNodes((node: HvigorNode) => {
        const hapContext = node.getContext(OhosPluginId.OHOS\_HAP\_PLUGIN) as OhosHapContext;
        if (!hapContext) {
            return
        }
        hapContext.targets((target: Target) => {
            // Processing logic for each target
            const currentProduct = target.getCurrentProduct();
            console.log(\`Product Name: ${currentProduct.getProductName()}\`);
        });
    });
})
export default {
    system: appTasks,  /\* Built-in plugin of Hvigor. It cannot be modified. \*/
    plugins:\[\]         /\* Custom plugin to extend the functionality of Hvigor. \*/
}

## getBuildTargetOutputPath

getBuildTargetOutputPath: () => string

Obtains the output path of the current target build.

**Return value**

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

string

 | 

Output path of the current target build.

 |

**Example**

// Project-level hvigorfile.ts file
import { appTasks, OhosHapContext, OhosPluginId, Target } from '@ohos/hvigor-ohos-plugin';
import { hvigor, HvigorNode } from '@ohos/hvigor';

hvigor.nodesEvaluated(() => {
    const rootNode = hvigor.getRootNode();
    rootNode.subNodes((node: HvigorNode) => {
        const hapContext = node.getContext(OhosPluginId.OHOS\_HAP\_PLUGIN) as OhosHapContext;
        if (!hapContext) {
            return
        }
        hapContext.targets((target: Target) => {
            // Processing logic for each target
            const buildTargetOutputPath = target.getBuildTargetOutputPath();
            console.log(\`Build Target Output Path: ${buildTargetOutputPath}\`);
        });
    });
})
export default {
    system: appTasks,  /\* Built-in plugin of Hvigor. It cannot be modified. \*/
    plugins:\[\]         /\* Custom plugin to extend the functionality of Hvigor. \*/
}

## getTargetName

getTargetName: () => string

Obtains the target name.

**Return value**

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

string

 | 

Target name.

 |

**Example**

// Project-level hvigorfile.ts file
import { appTasks, OhosHapContext, OhosPluginId, Target } from '@ohos/hvigor-ohos-plugin';
import { hvigor, HvigorNode } from '@ohos/hvigor';

hvigor.nodesEvaluated(() => {
    const rootNode = hvigor.getRootNode();
    rootNode.subNodes((node: HvigorNode) => {
        const hapContext = node.getContext(OhosPluginId.OHOS\_HAP\_PLUGIN) as OhosHapContext;
        if (!hapContext) {
            return
        }
        hapContext.targets((target: Target) => {
            // Processing logic for each target
            const targetName = target.getTargetName();
            console.log(\`Target Name: ${targetName}\`);
        });
    });
})

export default {
    system: appTasks,  /\* Built-in plugin of Hvigor. It cannot be modified. \*/
    plugins:\[\]         /\* Custom plugin to extend the functionality of Hvigor. \*/
}

#### Parameter

Represents the command configuration parameter object in hvigor, which can be obtained through [hvigor.getParameter()](#section1349018305379).

## getProperty

getProperty(key: string): any | undefined

Obtains a property value. If the value does not exist, **undefined** is returned.

**Since**: Hvigor 4.1.2

You can run the following command to configure **properties** in key-value pairs or configure it in the **hvigor-config.json5** file. If different values are configured for the same key, the value configured by the command takes precedence over the value configured in the configuration file.

-   Command: **\--config properties.{key}={value}** or **\-c properties.{key}={value}** (Command-line arguments always take precedence over configuration file properties for the same key.)
-   **hvigor-config.json5** file:
    
    "properties": {
      "key": "value"
    }
    

**Parameters**

| 
Name

 | 

Type

 | 

Mandatory

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

key

 | 

string

 | 

Yes

 | 

Key of the property to obtain.

 |

**Return value**

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

any | undefined

 | 

Value (a string, number, or boolean) obtained. If no value is specified, **undefined** is returned.

 |

**Example**

Add code to **hvigorfile.ts**.

import { hvigor } from '@ohos/hvigor';
const key = hvigor.getParameter().getProperty('key');
console.log(key);

Run the **hvigorw --sync -c properties.key=hello** command. The following information is displayed on the console:

hello

## getProperties

getProperties(): Properties

Obtains all properties.

**Since**: Hvigor 4.1.2

**Return value**

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

Properties

 | 

All properties obtained.

 |

**Example**

Add code to **hvigorfile.ts**.

import { hvigor } from '@ohos/hvigor';
const properties = hvigor.getParameter().getProperties();
console.log(properties\['key'\]);

Run the **hvigorw --sync -c properties.key=hello** command. The following information is displayed on the console:

hello

## setProperty

setProperty(key: string, value: any): void

Sets a property.

**Since**: Hvigor 5.10.3

**Parameters**

| 
Name

 | 

Type

 | 

Mandatory

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

key

 | 

string

 | 

Yes

 | 

Key of the **properties** field in the **hvigor-config.json5** file.

 |
| 

value

 | 

any

 | 

Yes

 | 

Value corresponding to the key of the **properties** field in the **hvigor-config.json5** file

 |

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cd/v3/cQe2bKAwSQy1yszekeNYNA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062156Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=240D552B5BE118D6EEF998FAF725FF6BA0B94123C90C9B5FC069C640CCA2F89F)

Call this API in the project-level **hvigorfile.ts** file. Calling it in the module-level **hvigorfile.ts** file does not take effect.

**Example**

Add code to the project-level **hvigorfile.ts** file.

import {hvigor, HvigorPlugin} from '@ohos/hvigor';
import {appTasks} from '@ohos/hvigor-ohos-plugin';
export function plugin(): HvigorPlugin{
    console.log('before: ', hvigor.getParameter().getProperty('hvigor.analyzeHtml')); // undefined
    hvigor.getParameter().setProperty('hvigor.analyzeHtml', true);
    return {
        pluginId:'example',
        apply: (node) => {
            console.log('after: ', hvigor.getParameter().getProperty('hvigor.analyzeHtml')); // true
        }
    };
}
export default {
    system: appTasks,  /\* Built-in plugin of Hvigor. It cannot be modified. \*/
    plugins: \[plugin()\]         /\* Custom plugin to extend the functionality of Hvigor. \*/
};

## getExtParam

getExtParam(key: string): string | undefined

Obtains the value of a parameter that is configured by **\-p** in the command. If the value does not exist, **undefined** is returned.

**Since**: Hvigor 4.1.2

**Parameters**

| 
Name

 | 

Type

 | 

Mandatory

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

key

 | 

string

 | 

Yes

 | 

Key of the parameter configured by **\-p** in the command.

 |

**Return value**

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

string | undefined

 | 

Value obtained. If the value does not exist, **undefined** is returned.

 |

**Example**

import { hvigor } from '@ohos/hvigor';
const extParam = hvigor.getParameter().getExtParam('key');
console.log(extParam);

Run the **hvigorw --sync -p key=hello** command. The following information is displayed on the console:

hello

## getExtParams

getExtParams(): Record<string, string>

Obtains all parameters that are configured by **\-p** in the command.

**Since**: Hvigor 4.1.2

**Return value**

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

Record<string, string>

 | 

All parameters obtained.

 |

**Example**

import { hvigor } from '@ohos/hvigor';
const extParams = hvigor.getParameter().getExtParams();
console.log(extParams\['key'\]);

Run the **hvigorw --sync -p key=hello** command. The following information is displayed on the console:

hello

## getStartParams

getStartParams(): StartParam

Obtains hvigor startup parameters, such as the settings of the daemon process, parallel build, and incremental build, and the log level.

**Since**: Hvigor 4.1.2

**Return value**

| 
Type

 | 

Property

 | 

Description

 |
| :-- | :-- | :-- |
| 

StartParams

 | 

daemon: boolean

 | 

Whether the daemon process is enabled. The value **true** (default) means the daemon process is enabled; the value **false** means the opposite.

 |
| 

StartParams

 | 

parallel: boolean

 | 

Whether parallel build is enabled. The value **true** (default) means parallel build is enabled; the value **false** means the opposite.

 |
| 

StartParams

 | 

incremental: boolean

 | 

Whether incremental build is enabled. The value **true** (default) means incremental build is enabled; the value **false** means the opposite.

 |
| 

StartParams

 | 

logLevel: string

 | 

Log level, which can be **info**, **debug**, **warn**, or **error**.

 |
| 

StartParams

 | 

typeCheck: boolean

 | 

Whether the **hvigorfile.ts** type check is enabled. The value **true** means the type check is enabled; the value **false** (default) means the opposite.

 |

**Example**

import { hvigor } from '@ohos/hvigor';
const startParams = hvigor.getParameter().getStartParams();
console.log(startParams\['daemon'\]);
console.log(startParams\['logLevel'\]);

## getWorkspaceDir

getWorkspaceDir(): string

Obtains the Hvigor workspace directory. The workspace refers to the location where the Hvigor plug-in of the current project is installed.

**Since**: Hvigor 4.1.2

**Return value**

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

string

 | 

Hvigor workspace directory.

 |

**Example**

import { hvigor } from '@ohos/hvigor';
const workspaceDir = hvigor.getParameter().getWorkspaceDir();
console.log(workspaceDir);

#### HvigorNode

Provides APIs for managing nodes in a Hvigor project. Each Hvigor project has a node object corresponding to the root module and a node object corresponding to each submodule. A node object contains the configuration, attributes, and tasks of a module.

## Modules to Import

import { HvigorNode } from '@ohos/hvigor';

## Obtaining an Instance

You can obtain an **hvigorNode** instance using the following methods: [getRootNode](#section10705432367) and [getAllNodes](#section16393827185) on a hvigor object, [getNode](#section208181154171019), and the [apply](#section2027815313120) method in HvigorPlugin.

The following uses the **apply** method of HvigorPlugin as an example:

import { HvigorNode, HvigorPlugin } from '@ohos/hvigor';

// Implement a custom plugin.
export function customPlugin(): HvigorPlugin {
    return {
        pluginId: 'customPlugin',
        async apply(currentNode: HvigorNode): Promise<void> {
            // You can use the methods of hvigorNode through currentNode.
        }
    };
}

## registerTask

registerTask: (task: HvigorTask) => void

Registers a task for this node. This API is called during the configuration phase of the Hvigor lifecycle. The **HvigorTask** object must be implemented and used as the input parameter.

**Since**: Hvigor 4.0.2

**Parameters**

| 
Name

 | 

Type

 | 

Mandatory

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

task

 | 

[HvigorTask](#section2386634104512)

 | 

Yes

 | 

Task to register.

 |

**Example**: Registering a custom task

// For details about how to obtain the node, see [Obtaining an Instance](#section17571175618316).
node.registerTask({
    name: 'customTask',
    run() {
        console.log('this is Task');
    }
});

## getTaskByName

getTaskByName: (taskName: string) => Task | undefined

Obtains a registered task of this node.

**Since**: Hvigor 4.0.2

**Parameters**

| 
Name

 | 

Type

 | 

Mandatory

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

taskName

 | 

string

 | 

Yes

 | 

Name of the task to obtain.

 |

**Return value**

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

[Task](#section2055582515349) | undefined

 | 

Task object obtained. If the task does not exist, **undefined** is returned.

 |

**Example**

// For details about how to obtain the node, see [Obtaining an Instance](#section17571175618316).
node.getTaskByName('assembleApp')

## getNodeName

getNodeName: () => string

Obtains the name of this node.

**Since**: Hvigor 4.0.2

**Return value**

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

string

 | 

Node name obtained.

 |

**Example**

// For details about how to obtain the node, see [Obtaining an Instance](#section17571175618316).
const nodeName = node.getNodeName();

## getNodePath

getNodePath: () => string

Obtains the path of this node.

**Since**: Hvigor 4.0.2

**Return value**

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

string

 | 

Node path obtained.

 |

**Example**

// For details about how to obtain the node, see [Obtaining an Instance](#section17571175618316).
const nodePath = node.getNodePath();

## getParentNode

getParentNode: () => HvigorNode | undefined

Obtains the parent node of this node.

**Since**: Hvigor 4.0.2

**Return value**

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

[HvigorNode](#section14832104719474) | undefined

 | 

Parent node obtained, or **undefined** if the node does not have a parent node.

 |

**Example**

// For details about how to obtain the node, see [Obtaining an Instance](#section17571175618316).
const parentNode = node.getParentNode();

## subNodes

subNodes: (callbackfn: (node: HvigorNode) => void) => void

Called after all the subnodes of this node are traversed. You can use this API to operate subnodes of this node.

Project nodes are loaded prior to module nodes. Before operating a subnode, call **hvigor.nodesEvaluated** and wait until all nodes are loaded.

**Since**: Hvigor 4.0.2

**Parameters**

| 
Name

 | 

Type

 | 

Mandatory

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

callbackfn

 | 

(node: [HvigorNode](#section14832104719474)) => void

 | 

Yes

 | 

Callback with a parameter of the HvigorNode type. A void function is returned.

 |

**Example**

// Project-level hvigorfile.ts
import { HvigorNode, HvigorPlugin } from '@ohos/hvigor'
import { appTasks } from '@ohos/hvigor-ohos-plugin';

export function customPlugin(): HvigorPlugin {
    return {
        pluginId: 'customPlugin',      
        async apply(currentNode: HvigorNode): Promise<void> {
            currentNode.subNodes((node: HvigorNode) => {
              // Perform operations related to the subnode here.
              // For example, obtain the name of the subnode.
              const subNodeName = node.getNodeName();
            })
        }
    };
}

export default {
    system: appTasks,  /\* Built-in plugin of Hvigor. It cannot be modified. \*/
    plugins:\[customPlugin()\]         /\* Custom plugin to extend the functionality of Hvigor. \*/
}

## getSubNodeByName

getSubNodeByName: (nodeName: string) => HvigorNode | undefined

Obtains a node object based on the node name.

**Since**: Hvigor 4.0.2

**Parameters**

| 
Name

 | 

Type

 | 

Mandatory

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

nodeName

 | 

string

 | 

Yes

 | 

Name of the subnode to obtain.

 |

**Return value**

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

[HvigorNode](#section14832104719474) | undefined

 | 

Subnode object obtained, or **undefined** if the subnode does not exist.

 |

**Example**

// Project-level hvigorfile.ts
import { appTasks } from '@ohos/hvigor-ohos-plugin';
import { HvigorNode, HvigorPlugin } from '@ohos/hvigor';
// In the hvigorfile.ts file in the root directory of the project, currentNode indicates the app, and its subnode includes entry.
// You can obtain the entry object using getSubNodeByName.
export function customPlugin(): HvigorPlugin {
    return {
        pluginId: 'customPlugin',
        async apply(currentNode: HvigorNode): Promise<void> {
            const subNode = currentNode.getSubNodeByName('entry');
        }
    };
}
export default {
    system: appTasks,  /\* Built-in plugin of Hvigor. It cannot be modified. \*/
    plugins: \[customPlugin()\]         /\* Custom plugin to extend the functionality of Hvigor. \*/
}

## getContext

getContext: (pluginId: string) => any

Obtains the context of a plug-in of this node.

**Since**: Hvigor 4.0.2

**Parameters**

| 
Name

 | 

Type

 | 

Mandatory

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

pluginId

 | 

string

 | 

Yes

 | 

ID of the plug-in to obtain.

 |

**Return value**

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

any

 | 

Context obtained, whose type can be customized.

 |

**Example**

// Project-level hvigorfile.ts
import { appTasks, OhosAppContext, OhosPluginId } from '@ohos/hvigor-ohos-plugin';
import { hvigor, getNode, HvigorNode, HvigorPlugin } from '@ohos/hvigor';
// Import OhosPluginId and OhosAppContext to obtain context information.
// Obtain it in the lifecycle hook.
hvigor.nodesEvaluated(() => {
    const node: HvigorNode = getNode(\_\_filename);
    const appContext = node.getContext(OhosPluginId.OHOS\_APP\_PLUGIN) as OhosAppContext;
    // Here you can use appContext to obtain context information, such as the project name.
    console.log('projectName:', appContext.getProjectName());
});
// Alternatively, you can obtain it directly using apply.
export function customPlugin(): HvigorPlugin {
    return {
        pluginId: 'customPlugin',
        async apply(currentNode: HvigorNode): Promise<void> {
            const appContext = currentNode.getContext(OhosPluginId.OHOS\_APP\_PLUGIN) as OhosAppContext;
            console.log('projectName:', appContext.getProjectName());
        }
    };
}
export default {
    system: appTasks,  /\* Built-in plugin of Hvigor. It cannot be modified. \*/
    plugins: \[customPlugin()\]         /\* Custom plugin to extend the functionality of Hvigor. \*/
}

## getAllPluginIds

getAllPluginIds: () => string\[\]

Obtains all plug-ins loaded by this node.

**Since**: Hvigor 4.0.2

**Return value**

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

string\[\]

 | 

IDs of the loaded plug-ins.

 |

**Example**

// Project-level hvigorfile.ts
import { HvigorNode, HvigorPlugin } from '@ohos/hvigor'
import { appTasks } from '@ohos/hvigor-ohos-plugin';
export function customPlugin(): HvigorPlugin {
    return {
        pluginId: 'customPlugin',
        async apply(currentNode: HvigorNode): Promise<void> {
            const allPluginIds = currentNode.getAllPluginIds();
            allPluginIds.forEach((id) => {
                console.log(id);
            })
        }
    };
}
export default {
    system: appTasks,  /\* Built-in plugin of Hvigor. It cannot be modified. \*/
    plugins: \[customPlugin()\]         /\* Custom plugin to extend the functionality of Hvigor. \*/
}

## nodeDir

nodeDir: NormalizedFile

**NormalizedFile** object of the current node's root directory.

**Since**: Hvigor 4.3.0

## getNodeDir

getNodeDir: () => NormalizedFile

Obtains the **NormalizedFile** object of this node's root directory.

**Since**: Hvigor 4.3.0

**Return value**

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

[NormalizedFile](#section281448112713)

 | 

**NormalizedFile** object of the current node's root directory.

 |

**Example**

// Project-level hvigorfile.ts
import { HvigorNode, HvigorPlugin } from '@ohos/hvigor';
import { appTasks } from '@ohos/hvigor-ohos-plugin'
export function customPlugin(): HvigorPlugin {
    return {
        pluginId: 'customPlugin',
        async apply(currentNode: HvigorNode): Promise<void> {
           const dir = currentNode.getNodeDir();
        }
    };
}
export default {
    system: appTasks,  /\* Built-in plugin of Hvigor. It cannot be modified. \*/
    plugins: \[customPlugin()\]         /\* Custom plugin to extend the functionality of Hvigor. \*/
}

## addExtraOption

addExtraOption: (key: string, value: any) => void

Adds a custom property to the current node.

**Since**: Hvigor 4.3.0

**Parameters**

| 
Name

 | 

Type

 | 

Mandatory

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

key

 | 

string

 | 

Yes

 | 

Key of the custom property to add.

 |
| 

value

 | 

any

 | 

Yes

 | 

Value of the custom property to add.

 |

**Example**

// Project-level hvigorfile.ts
import { HvigorNode, HvigorPlugin } from '@ohos/hvigor';
import { appTasks } from '@ohos/hvigor-ohos-plugin'
export function customPlugin(): HvigorPlugin {
    return {
        pluginId: 'customPlugin',
        async apply(currentNode: HvigorNode): Promise<void> {
           currentNode.addExtraOption('key', 'value');
        }
    };
}
export default {
    system: appTasks,  /\* Built-in plugin of Hvigor. It cannot be modified. \*/
    plugins: \[customPlugin()\]         /\* Custom plugin to extend the functionality of Hvigor. \*/
}

## getExtraOption

getExtraOption: (key: string) => any

Obtains the custom property set on the current node using the **addExtraOption()** function.

**Since**: Hvigor 4.3.0

**Parameters**

| 
Name

 | 

Type

 | 

Mandatory

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

key

 | 

string

 | 

Yes

 | 

Key of the custom property.

 |

**Return value**

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

any

 | 

Value of the custom property.

 |

**Example**

// Project-level hvigorfile.ts
import { HvigorNode, HvigorPlugin } from '@ohos/hvigor';
import { appTasks } from '@ohos/hvigor-ohos-plugin'
export function customPlugin(): HvigorPlugin {
    return {
        pluginId: 'customPlugin',
        async apply(currentNode: HvigorNode): Promise<void> {
           currentNode.addExtraOption('key', 'value');
           currentNode.getExtraOption('key');
        }
    };
}
export default {
    system: appTasks,  /\* Built-in plugin of Hvigor. It cannot be modified. \*/
    plugins: \[customPlugin()\]         /\* Custom plugin to extend the functionality of Hvigor. \*/
}

## beforeNodeEvaluate

beforeNodeEvaluate(fn: (HvigorNode) => {}): void

Adds a callback function before node evaluation for this node.

**Since**: Hvigor 4.3.0

**Parameters**

| 
Name

 | 

Type

 | 

Mandatory

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

fn

 | 

([HvigorNode](#section14832104719474)) => {}

 | 

Yes

 | 

A method whose input parameter is empty or an **HvigorNode** object.

 |

**Example**: Registering a **beforeNodeEvaluate** hook for a node named **entry** and printing out the node's information

import { hvigor } from '@ohos/hvigor';
hvigor.nodesInitialized(() => {
  hvigor.getRootNode().subNodes(node => {
    if (node.getNodeName() === 'entry') {
      node.beforeNodeEvaluate(hvigorNode => {
        console.log(hvigorNode.getNodeName());
      })
    }
  })
});

## afterNodeEvaluate

afterNodeEvaluate(fn: (HvigorNode) => {}): void

Adds a callback function after node evaluation for this node.

**Since**: Hvigor 4.3.0

**Parameters**

| 
Name

 | 

Type

 | 

Mandatory

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

fn

 | 

([HvigorNode](#section14832104719474)) => {}

 | 

Yes

 | 

A method whose input parameter is empty or an **HvigorNode** object.

 |

**Example**: Registering an **afterNodeEvaluate** hook for a node named **entry** and printing out the node's information

import { hvigor } from '@ohos/hvigor';
hvigor.nodesInitialized(() => {
  hvigor.getRootNode().subNodes(node => {
    if (node.getNodeName() === 'entry') {
      node.afterNodeEvaluate(hvigorNode => {
        console.log(hvigorNode.getNodeName());
      })
    }
  })
});

#### HvigorPlugin

Defines a Hvigor plugin instance. You can use it to develop a Hvigor plugin.

## Modules to Import

import { HvigorPlugin } from '@ohos/hvigor';

## pluginId

pluginId: string

Represents the unique ID of the plug-in.

**Example**

// Project-level hvigorfile.ts file
import { HvigorNode, HvigorPlugin } from '@ohos/hvigor';
import { appTasks } from '@ohos/hvigor-ohos-plugin';

// Implement a custom plugin.
export function customPlugin(): HvigorPlugin {
    return {
        pluginId: 'customPlugin',
        context() {
            return {
                data: 'customPlugin xxx'
            };
        },
        async apply(currentNode: HvigorNode): Promise<void> {
        }
    };
}

export default {
    system: appTasks,  /\* Built-in plugin of Hvigor. It cannot be modified. \*/
    plugins: \[customPlugin()\]         /\* Custom plugin to extend the functionality of Hvigor. \*/
}

## context

context?: (() => any) | any

Represents the context of the plugin, which is optional. You can use **node.getContext('_plugin ID_')** to obtain the context of a plugin.

**Return value**

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

(() => any) | any

 | 

A value of any type or a function that returns a value of any type.

 |

**Example**

// Project-level hvigorfile.ts file
import { HvigorNode, HvigorPlugin } from '@ohos/hvigor';
import { appTasks } from '@ohos/hvigor-ohos-plugin';

// Implement a custom plugin.
export function customPlugin(): HvigorPlugin {
    return {
        pluginId: 'customPlugin',
        context() {
            return {
                data: 'customPlugin xxx'
            };
        },
        async apply(currentNode: HvigorNode): Promise<void> {
        }
    };
}

export default {
    system: appTasks,  /\* Built-in plugin of Hvigor. It cannot be modified. \*/
    plugins:\[customPlugin()\]         /\* Custom plugin to extend the functionality of Hvigor. \*/
}

## apply

apply: (node: HvigorNode) => void | Promise<void>

Represents the function that defines the plugin implementation logic (for example, task registration). This function is called in the configuration phase of the Hvigor lifecycle.

**Parameters**

| 
Name

 | 

Type

 | 

Mandatory

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

node

 | 

[HvigorNode](#section14832104719474)

 | 

Yes

 | 

hvigor node object.

 |

**Return value**

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

void | Promise<void>

 | 

No return value, or the return value is of the Promise<void> type.

 |

**Example**

// Project-level hvigorfile.ts file
import { hvigor, HvigorNode, HvigorPlugin } from '@ohos/hvigor';
import { appTasks } from '@ohos/hvigor-ohos-plugin';

// Implement a custom plugin.
export function customPlugin(): HvigorPlugin {
    return {
        pluginId: 'customPlugin',
        context() {
            return {
                data: 'customPlugin xxx'
            };
        },
        async apply(currentNode: HvigorNode): Promise<void> {
            hvigor.nodesEvaluated(async () => {
                // Register a module-level task.
            });
        }
    };
}

export default {
    system: appTasks,  /\* Built-in plugin of Hvigor. It cannot be modified. \*/
    plugins:\[customPlugin()\]         /\* Custom plugin to extend the functionality of Hvigor. \*/
};

#### HvigorTask

Defines a Hvigor task instance, which is required when a task is created.

## Modules to Import

import { HvigorTask } from '@ohos/hvigor';

## name

name: string

Defines the task name.

**Example**

// Project-level hvigorfile.ts file
import { appTasks } from '@ohos/hvigor-ohos-plugin';
import { getNode, HvigorNode, HvigorTask } from '@ohos/hvigor';

// Obtain the current hvigorNode object.
const node: HvigorNode = getNode(\_\_filename);

// Register the task.
node.registerTask({
    name: 'customTask',
    run() {
        console.log('this is Task');
    }
});

export default {
    system: appTasks,  /\* Built-in plugin of Hvigor. It cannot be modified. \*/
    plugins:\[\]         /\* Custom plugin to extend the functionality of Hvigor. \*/
}

## context

context?: (() => any) | any

Represents the data object that is partially shared in a task. This object is injected to the **this.context** attribute when the task is registered. In the **input()**, **output()**, and **run()** functions, **this.context** can directly invoke the object and attributes defined in **context**.

**Return value**

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

(() => any) | any

 | 

A value of any type or a function that returns a value of any type.

 |

**Example**

// Project-level hvigorfile.ts file
import { appTasks } from '@ohos/hvigor-ohos-plugin';
import { getNode, HvigorNode, HvigorTask } from '@ohos/hvigor';

// Obtain the current hvigorNode object.
const node: HvigorNode = getNode(\_\_filename);

// Register the task.
node.registerTask({
    name: 'customTask',
    context() {
        return {
            data: 'customRegisterTask xxx'
        };
    },
    run() {
        console.log(this.context);
    }
});

export default {
    system: appTasks,  /\* Built-in plugin of Hvigor. It cannot be modified. \*/
    plugins:\[\]         /\* Custom plugin to extend the functionality of Hvigor. \*/
}

## input

input?: (input: TaskInput) => void

Defines the input condition for the incremental build task.

**Parameters**

| 
Name

 | 

Type

 | 

Mandatory

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

input

 | 

[TaskInput](#section425723621113)

 | 

Yes

 | 

Input condition.

 |

**Example**

// Project-level hvigorfile.ts file
import { appTasks, OhosAppContext, OhosPluginId } from '@ohos/hvigor-ohos-plugin';
import { getNode, hvigor, HvigorTaskContext, TaskInput, TaskOutput } from "@ohos/hvigor";
import fse from "fs-extra";
import path from "path";

const currentNode = getNode(\_\_filename);

hvigor.nodesEvaluated(() => {
    const context = currentNode.getContext(OhosPluginId.OHOS\_APP\_PLUGIN) as OhosAppContext;
    const outputFilePath = path.resolve(context.getBuildRootPath(), 'test.txt');
    // Register a file generation task and enable incremental processing for this task.
    currentNode.registerTask({
        name: "testTask",
        run(taskContext: HvigorTaskContext): void | Promise<void> {
            fse.writeFileSync(outputFilePath, context.getProjectName());
            return undefined;
        },
        input(input: TaskInput): void {
            input.property('projectName', context.getProjectName());
        },
        async output(output: TaskOutput): Promise<void> {
            try {
                const parentDir = path.dirname(outputFilePath);
                await fse.ensureDir(parentDir); // Ensure that the parent directory exists.
                await fse.ensureFile(outputFilePath);
                output.file(outputFilePath);
            } catch (error) {
                console.error('File creation failed:', error);
                throw error;
            }
        },
        postDependencies: \['assembleApp'\]
    })
})

export default {
    system: appTasks,  /\* Built-in plugin of Hvigor. It cannot be modified. \*/
    plugins:\[\]         /\* Custom plugin to extend the functionality of Hvigor. \*/
}

Add **dependencies** to **hvigor-config.json5** as follows:

// hvigor-config.json5
"dependencies": {
    "fs-extra": "11.2.0",
    "@types/fs-extra": "9.0.13"
},

## output

output?: (output: TaskOutput) => void

Defines the output condition for the incremental build task.

**Parameters**

| 
Name

 | 

Type

 | 

Mandatory

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

output

 | 

[TaskOutput](#section135442202125)

 | 

Yes

 | 

Output condition.

 |

**Example**

// Project-level hvigorfile.ts file
import { appTasks, OhosAppContext, OhosPluginId } from '@ohos/hvigor-ohos-plugin';
import { getNode, hvigor, HvigorTaskContext, TaskInput, TaskOutput } from "@ohos/hvigor";
import fse from "fs-extra";
import path from "path";

const currentNode = getNode(\_\_filename);

hvigor.nodesEvaluated(() => {
    const context = currentNode.getContext(OhosPluginId.OHOS\_APP\_PLUGIN) as OhosAppContext;
    const outputFilePath = path.resolve(context.getBuildRootPath(), 'test.txt');
    // Register a file generation task and enable incremental processing for this task.
    currentNode.registerTask({
        name: "testTask",
        run(taskContext: HvigorTaskContext): void | Promise<void> {
            fse.writeFileSync(outputFilePath, context.getProjectName());
            return undefined;
        },
        input(input: TaskInput): void {
            input.property('projectName', context.getProjectName());
        },
        async output(output: TaskOutput): Promise<void> {
            try {
                const parentDir = path.dirname(outputFilePath);
                await fse.ensureDir(parentDir); // Ensure that the parent directory exists.
                await fse.ensureFile(outputFilePath);
                output.file(outputFilePath);
            } catch (error) {
                console.error('File creation failed:', error);
                throw error;
            }
        },
        postDependencies: \['assembleApp'\]
    })
})

export default {
    system: appTasks,  /\* Built-in plugin of Hvigor. It cannot be modified. \*/
    plugins:\[\]         /\* Custom plugin to extend the functionality of Hvigor. \*/
}

Add **dependencies** to **hvigor-config.json5** as follows:

// hvigor-config.json
"dependencies": {
    "fs-extra": "11.2.0",
    "@types/fs-extra": "9.0.13"    
},

## run

run: (taskContext: HvigorTaskContext) => void | Promise<void>

Represents the function that defines the task logic. You can define the task processing logic in this function.

**Parameters**

| 
Name

 | 

Type

 | 

Mandatory

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

taskContext

 | 

HvigorTaskContext

 | 

No

 | 

Default common information type injected.

 |

**Return value**

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

void | Promise<void>

 | 

No return value, or the return value is of the Promise<void> type.

 |

**Example**

// Project-level hvigorfile.ts file
import { appTasks } from '@ohos/hvigor-ohos-plugin';
import { getNode, HvigorNode, HvigorTask } from '@ohos/hvigor';

// Obtain the current hvigorNode object.
const node: HvigorNode = getNode(\_\_filename);

// Register the task.
node.registerTask({
    name: 'customTask',
    run() {
        console.log('this is Task');
    }
});

export default {
    system: appTasks,  /\* Built-in plugin of Hvigor. It cannot be modified. \*/
    plugins:\[\]         /\* Custom plugin to extend the functionality of Hvigor. \*/
}

## beforeRun

beforeRun?: (taskContext: HvigorTaskContext) => void | Promise<void>

Represents the function to call before **run()**. When the task is executed, this function is called before **run()**.

**Parameters**

| 
Name

 | 

Type

 | 

Mandatory

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

taskContext

 | 

HvigorTaskContext

 | 

No

 | 

Default common information type injected.

 |

**Return value**

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

void | Promise<void>

 | 

No return value, or the return value is of the Promise<void> type.

 |

**Example**

// Project-level hvigorfile.ts file
import { appTasks } from '@ohos/hvigor-ohos-plugin';
import { getNode, HvigorNode, HvigorTask } from '@ohos/hvigor';

// Obtain the current hvigorNode object.
const node: HvigorNode = getNode(\_\_filename);

// Register the task.
node.registerTask({
    name: 'customTask',
    run() {
        console.log('customTask');
    },
    beforeRun() {
        console.log('beforeRun');
    }
});

export default {
    system: appTasks,  /\* Built-in plugin of Hvigor. It cannot be modified. \*/
    plugins:\[\]         /\* Custom plugin to extend the functionality of Hvigor. \*/
}

## afterRun

afterRun?: (taskContext: HvigorTaskContext) => void | Promise<void>

Represents the function to call after **run()**. When the task is executed, this function is called after **run()**.

**Parameters**

| 
Name

 | 

Type

 | 

Mandatory

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

taskContext

 | 

HvigorTaskContext

 | 

No

 | 

Default common information type injected.

 |

**Return value**

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

void | Promise<void>

 | 

No return value, or the return value is of the Promise<void> type.

 |

**Example**

// Project-level hvigorfile.ts file
import { appTasks } from '@ohos/hvigor-ohos-plugin';
import { getNode, HvigorNode, HvigorTask } from '@ohos/hvigor';

// Obtain the current hvigorNode object.
const node: HvigorNode = getNode(\_\_filename);

// Register the task.
node.registerTask({
    name: 'customTask',
    run() {
        console.log('customTask');
    },
    afterRun() {
        console.log('afterRun');
    }
});

export default {
    system: appTasks,  /\* Built-in plugin of Hvigor. It cannot be modified. \*/
    plugins:\[\]         /\* Custom plugin to extend the functionality of Hvigor. \*/
}

## dependencies

dependencies?: (() => string\[\]) | string\[\]

Represents the dependencies for this task. This API configures the previous task on which this task depends. The task execution sequence is: previous task -> this task -> next task.

Since DevEco Studio 6.0.0 Beta2, tasks that depend on other modules are supported. Add **_Module name_:** before such tasks, for example, **har:assembleHar**.

**Return value**

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

(() => string\[\]) | string\[\]

 | 

An array of string or a function that returns an array of strings.

 |

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/dd/v3/xDBX09wPQKOBNtCk9ZWJgQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062156Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=D733A89A18D850F7A58E6FCD803F84F725B968173DC748BDD2A1891FE651F3DE)

For tasks depending on other modules, register them in [hook-nodesEvaluated](../../../overview/build-system-lifecycle/document.md#section746253616316). Otherwise, tasks of other modules may not be initialized during registration, and the current task cannot be registered.

**Example 1**: Tasks that depend on the current module

// Project-level hvigorfile.ts file
import { appTasks } from '@ohos/hvigor-ohos-plugin';
import { getNode, HvigorNode, HvigorTask } from '@ohos/hvigor';

// Obtain the current hvigorNode object.
const node: HvigorNode = getNode(\_\_filename);

// Register the task.
node.registerTask({
    name: 'customTask',
    run() {
        console.log('customTask');
    },
    dependencies: \['customTask1'\],
});

// Register the task.
node.registerTask({
    name: 'customTask1',
    run() {
        console.log('customTask1');
    },
});

export default {
    system: appTasks,  /\* Built-in plugin of Hvigor. It cannot be modified. \*/
    plugins:\[\]         /\* Custom plugin to extend the functionality of Hvigor. \*/
}

**Example 2**: Tasks that depend on other modules

// Project-level hvigorfile.ts file
import { appTasks } from '@ohos/hvigor-ohos-plugin';
import { hvigor, HvigorNode, HvigorPlugin } from '@ohos/hvigor';

// Obtain the current entry node object.
const entryNode = hvigor.getNodeByName('entry');

// Place the logic in hook-nodesEvaluated.
hvigor.nodesEvaluated(async () => {
  // Registers the task.
  entryNode.registerTask({
    // Configure the task name.
    name: \`default@CustomTask\`,
    run() {
      console.log('customTask1')
    },
    // Configure the dependencies for this task.
    dependencies: \['har:assembleHar'\], // Cross-module dependency on the assembleHar task of the HAR module. Ensure that the HAR module exists.
    // Configure the dependencies for the next task.
    postDependencies: \['entry:default@PreBuild'\]  // Two formats are supported: entry:default@PreBuild and default@PreBuild.
  });
});

export default {
  system: appTasks, /\* Built-in plugin of Hvigor. It cannot be modified. \*/
  plugins: \[\]       /\* Custom plugin to extend the functionality of Hvigor. \*/
}

## postDependencies

postDependencies?: (() => string\[\]) | string\[\]

Represents the dependencies for the next task. This API configures the task that depends on this task. The task execution sequence is: previous task -> this task -> next task.

Since DevEco Studio 6.0.0 Beta2, tasks that depend on other modules are supported. Add **_Module name_:** before such tasks, for example, **har:default@PreBuild**.

**Return value**

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

(() => string\[\]) | string\[\]

 | 

An array of string or a function that returns an array of strings.

 |

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e6/v3/RpJhyxB8QCebcvL-E8UJ7A/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062156Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=6F9EED6750F675EEF6D7A2620F4A8397250C3265D04328754D8EBFA7ECC1D0D7)

For tasks depending on other modules, register them in [hook-nodesEvaluated](../../../overview/build-system-lifecycle/document.md#section746253616316). Otherwise, tasks of other modules may not be initialized during registration, and the current task cannot be registered.

**Example 1**: Tasks that depend on the current module

// Project-level hvigorfile.ts file
import { appTasks } from '@ohos/hvigor-ohos-plugin';
import { getNode, HvigorNode, HvigorTask } from '@ohos/hvigor';

// Obtain the current hvigorNode object.
const node: HvigorNode = getNode(\_\_filename);

// Register the task.
node.registerTask({
    name: 'customTask1',
    run() {
        console.log('customTask1');
    },
});

// Register the task.
node.registerTask({
    name: 'customTask',
    run() {
        console.log('customTask');
    },
    postDependencies: \['customTask1'\],
});

export default {
    system: appTasks,  /\* Built-in plugin of Hvigor. It cannot be modified. \*/
    plugins:\[\]         /\* Custom plugin to extend the functionality of Hvigor. \*/
}

**Example 2**: Tasks that depend on other modules

// Project-level hvigorfile.ts file
import { appTasks } from '@ohos/hvigor-ohos-plugin';
import { hvigor, HvigorNode, HvigorPlugin } from '@ohos/hvigor';

// Obtain the current entry node object.
const entryNode = hvigor.getNodeByName('entry');

// Place the logic in hook-nodesEvaluated.
hvigor.nodesEvaluated(async () => {
  // Registers the task.
  entryNode.registerTask({
    // Configure the task name.
    name: \`default@CustomTask\`,
    run() {
      console.log('customTask1')
    },
    // Configure the dependencies for this task.
    dependencies: \['entry:default@PreBuild'\], // Two formats are supported: entry:default@PreBuild and default@PreBuild.
    // Configure the dependencies for the next task.
    postDependencies: \['har:default@PreBuild'\]  // Cross-module dependency on the PreBuild task of the HAR module. Ensure that the HAR module exists.
  });
});

export default {
  system: appTasks, /\* Built-in plugin of Hvigor. It cannot be modified. \*/
  plugins: \[\]       /\* Custom plugin to extend the functionality of Hvigor. \*/
}

#### TaskInput

Provides basic functions for adding input conditions for an incremental build task.

## Modules to Import

import { TaskInput } from '@ohos/hvigor';

## property

property(key: string, value: TaskInputValue): TaskInput

Adds a property in the form of a key-value pair as the input condition for an incremental build task.

**Parameters**

| 
Name

 | 

Type

 | 

Mandatory

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

key

 | 

string

 | 

Yes

 | 

Key of the property to add.

 |
| 

value

 | 

TaskInputValue

 | 

Yes

 | 

Value of the property to add. The value can be a number, string, boolean, or an array of them.

 |

**Return value**

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

[TaskInput](#section425723621113)

 | 

Task input condition used for method chaining.

 |

**Example**

// Project-level hvigorfile.ts file
import { appTasks, OhosAppContext, OhosPluginId } from '@ohos/hvigor-ohos-plugin';
import { getNode, hvigor, HvigorTask, HvigorTaskContext, TaskInput, TaskOutput } from "@ohos/hvigor";
import fse from "fs-extra";
import path from "path";

const currentNode = getNode(\_\_filename);

hvigor.nodesEvaluated(() => {
    const context = currentNode.getContext(OhosPluginId.OHOS\_APP\_PLUGIN) as OhosAppContext;
    const outputFilePath = path.resolve(context.getBuildRootPath(), 'test.txt');
    // Register a file generation task and enable incremental processing for this task.
    currentNode.registerTask({
        name: "testTask",
        run(taskContext: HvigorTaskContext): void | Promise<void> {
            fse.writeFileSync(outputFilePath, context.getProjectName());
            return undefined;
        },
        input(input: TaskInput): void {
            input.property('projectName', context.getProjectName());
        },
        async output(output: TaskOutput): Promise<void> {
            try {
                const parentDir = path.dirname(outputFilePath);
                await fse.ensureDir(parentDir); // Ensure that the parent directory exists.
                await fse.ensureFile(outputFilePath);
                output.file(outputFilePath);
            } catch (error) {
                console.error('File creation failed:', error);
                throw error;
            }
        },
        postDependencies: \['assembleApp'\]
    })
})

export default {
    system: appTasks,  /\* Built-in plugin of Hvigor. It cannot be modified. \*/
    plugins:\[\]         /\* Custom plugin to extend the functionality of Hvigor. \*/
}

Add **dependencies** to **hvigor-config.json5** as follows:

// hvigor-config.json5
"dependencies": {
    "fs-extra": "11.2.0",
    "@types/fs-extra": "9.0.13"
},

## file

file(path: string): TaskInput

Adds the path of a file or folder as the input condition for an incremental build task.

**Parameters**

| 
Name

 | 

Type

 | 

Mandatory

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

path

 | 

string

 | 

Yes

 | 

Path to add.

 |

**Return value**

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

[TaskInput](#section425723621113)

 | 

Task input condition used for method chaining.

 |

**Example**

// Project-level hvigorfile.ts file
import { appTasks, OhosAppContext, OhosPluginId } from '@ohos/hvigor-ohos-plugin';
import { getNode, hvigor, HvigorTask, HvigorTaskContext, TaskInput, TaskOutput } from "@ohos/hvigor";
import fse from "fs-extra";
import path from "path";
const currentNode = getNode(\_\_filename);
hvigor.nodesEvaluated(() => {
    const context = currentNode.getContext(OhosPluginId.OHOS\_APP\_PLUGIN) as OhosAppContext;
    const outputFilePath = path.resolve(context.getBuildRootPath(), 'testOutput.txt');
    // Add the path of a file as the input condition for an incremental build task.
    const inputFilePath = path.resolve(context.getProjectPath(), 'testInput.txt'); 
    // Register a file generation task and enable incremental processing for this task.
    currentNode.registerTask({
        name: "testTask",
        run(taskContext: HvigorTaskContext): void | Promise<void> {
            const parentDir = path.dirname(outputFilePath);
            fse.ensureDirSync(parentDir); // Ensure that the parent directory exists.
            fse.ensureFileSync(outputFilePath);
            fse.writeFileSync(outputFilePath, context.getProjectName());
            return undefined;
        },
        input(input: TaskInput): void {
            input.property('projectName', context.getProjectName());
            if (fse.existsSync(inputFilePath)) {
                input.file(inputFilePath);
            }
        },
        async output(output: TaskOutput): Promise<void> {
            output.file(outputFilePath);
        },
        postDependencies: \['assembleApp'\]
    })
})
export default {
    system: appTasks,  /\* Built-in plugin of Hvigor. It cannot be modified. \*/
    plugins:\[\]         /\* Custom plugin to extend the functionality of Hvigor. \*/
}

Add **dependencies** to **hvigor-config.json5** as follows:

// hvigor-config.json5
"dependencies": {
    "fs-extra": "11.2.0",
    "@types/fs-extra": "9.0.13"
},

## files

files(paths: string\[\]): TaskInput

Adds the paths of multiple files or folders as the input condition for an incremental build task running.

**Parameters**

| 
Name

 | 

Type

 | 

Mandatory

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

paths

 | 

string

 | 

Yes

 | 

Paths to add.

 |

**Return value**

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

[TaskInput](#section425723621113)

 | 

Task input condition used for method chaining.

 |

**Example**

// Project-level hvigorfile.ts file
import { appTasks, OhosAppContext, OhosPluginId } from '@ohos/hvigor-ohos-plugin';
import { getNode, hvigor, HvigorTask, HvigorTaskContext, TaskInput, TaskOutput } from "@ohos/hvigor";
import fse from "fs-extra";
import path from "path";
const currentNode = getNode(\_\_filename);
hvigor.nodesEvaluated(() => {
    const context = currentNode.getContext(OhosPluginId.OHOS\_APP\_PLUGIN) as OhosAppContext;
    const outputFilePath = path.resolve(context.getBuildRootPath(), 'test.txt');
    // Add the path of a file as the input condition for an incremental build task.
    const inputFilePath = path.resolve(context.getProjectPath(), 'test.txt'); 
    // Register a file generation task and enable incremental processing for this task.
    currentNode.registerTask({
        name: "testTask",
        run(taskContext: HvigorTaskContext): void | Promise<void> {
            const parentDir = path.dirname(outputFilePath);
            fse.ensureDirSync(parentDir); // Ensure that the parent directory exists.
            fse.ensureFileSync(outputFilePath);
            fse.writeFileSync(outputFilePath, context.getProjectName());
            return undefined;
        },
        input(input: TaskInput): void {
            input.property('projectName', context.getProjectName());
            if (fse.existsSync(inputFilePath)) {
                input.files(\[inputFilePath, \]);
            }
        },
        async output(output: TaskOutput): Promise<void> {
            output.files(\[outputFilePath,\]);
        },
        postDependencies: \['assembleApp'\]
    })
})
export default {
    system: appTasks,  /\* Built-in plugin of Hvigor. It cannot be modified. \*/
    plugins:\[\]         /\* Custom plugin to extend the functionality of Hvigor. \*/
}

Add **dependencies** to **hvigor-config.json5** as follows:

// hvigor-config.json5
"dependencies": {
    "fs-extra": "11.2.0",
    "@types/fs-extra": "9.0.13"
},

#### TaskOutput

Provides basic functions for adding output conditions for an incremental build task.

## Modules to Import

import { TaskOutput } from '@ohos/hvigor';

## file

file(path: string): TaskOutput

Adds the path of a file or folder as the output condition for an incremental build task.

**Parameters**

| 
Name

 | 

Type

 | 

Mandatory

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

path

 | 

string

 | 

Yes

 | 

Path to add.

 |

**Return value**

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

[TaskOutput](#section135442202125)

 | 

Task output condition used for method chaining.

 |

**Example**

// Project-level hvigorfile.ts file
import { appTasks, OhosAppContext, OhosPluginId } from '@ohos/hvigor-ohos-plugin';
import { getNode, hvigor, HvigorTaskContext, TaskInput, TaskOutput } from "@ohos/hvigor";
import fse from "fs-extra";
import path from "path";
const currentNode = getNode(\_\_filename);
hvigor.nodesEvaluated(() => {
    const context = currentNode.getContext(OhosPluginId.OHOS\_APP\_PLUGIN) as OhosAppContext;
    const outputFilePath = path.resolve(context.getBuildRootPath(), 'testOutput.txt');
    // Add the path of a file as the input condition for an incremental build task.
    const inputFilePath = path.resolve(context.getProjectPath(), 'testInput.txt'); 
    // Register a file generation task and enable incremental processing for this task.
    currentNode.registerTask({
        name: "testTask",
        run(taskContext: HvigorTaskContext): void | Promise<void> {
            const parentDir = path.dirname(outputFilePath);
            fse.ensureDirSync(parentDir); // Ensure that the parent directory exists.
            fse.ensureFileSync(outputFilePath);
            fse.writeFileSync(outputFilePath, context.getProjectName());
            return undefined;
        },
        input(input: TaskInput): void {
            input.property('projectName', context.getProjectName());
            if (fse.existsSync(inputFilePath)) {
                input.file(inputFilePath);
            }
        },
        async output(output: TaskOutput): Promise<void> {
            output.file(outputFilePath);
        },
        postDependencies: \['assembleApp'\]
    })
})
export default {
    system: appTasks,  /\* Built-in plugin of Hvigor. It cannot be modified. \*/
    plugins:\[\]         /\* Custom plugin to extend the functionality of Hvigor. \*/
}

Add **dependencies** to **hvigor-config.json5** as follows:

// hvigor-config.json5
"dependencies": {
    "fs-extra": "11.2.0",
    "@types/fs-extra": "9.0.13"
},

## files

files(paths: string\[\]): TaskOutput

Adds the paths of multiple files or folders as the output condition for an incremental build task.

**Parameters**

| 
Name

 | 

Type

 | 

Mandatory

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

paths

 | 

string\[\]

 | 

Yes

 | 

Paths to add.

 |

**Return value**

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

[TaskOutput](#section135442202125)

 | 

Task output condition used for method chaining.

 |

**Example**

// Project-level hvigorfile.ts file
import { appTasks, OhosAppContext, OhosPluginId } from '@ohos/hvigor-ohos-plugin';
import { getNode, hvigor, HvigorTaskContext, TaskInput, TaskOutput } from "@ohos/hvigor";
import fse from "fs-extra";
import path from "path";
const currentNode = getNode(\_\_filename);
hvigor.nodesEvaluated(() => {
    const context = currentNode.getContext(OhosPluginId.OHOS\_APP\_PLUGIN) as OhosAppContext;
    const outputFilePath = path.resolve(context.getBuildRootPath(), 'testOutput.txt');
    // Add the path of a file as the input condition for an incremental build task.
    const inputFilePath = path.resolve(context.getProjectPath(), 'testInput.txt'); 
    // Register a file generation task and enable incremental processing for this task.
    currentNode.registerTask({
        name: "testTask",
        run(taskContext: HvigorTaskContext): void | Promise<void> {
            const parentDir = path.dirname(outputFilePath);
            fse.ensureDirSync(parentDir); // Ensure that the parent directory exists.
            fse.ensureFileSync(outputFilePath);
            fse.writeFileSync(outputFilePath, context.getProjectName());
            return undefined;
        },
        input(input: TaskInput): void {
            input.property('projectName', context.getProjectName());
            if (fse.existsSync(inputFilePath)) {
                input.files(\[inputFilePath, \]);
            }
        },
        async output(output: TaskOutput): Promise<void> {
            output.files(\[outputFilePath,\]);
        },
        postDependencies: \['assembleApp'\]
    })
})
export default {
    system: appTasks,  /\* Built-in plugin of Hvigor. It cannot be modified. \*/
    plugins:\[\]         /\* Custom plugin to extend the functionality of Hvigor. \*/
}

Add **dependencies** to **hvigor-config.json5** as follows:

// hvigor-config.json5
"dependencies": {
    "fs-extra": "11.2.0",
    "@types/fs-extra": "9.0.13"
},

#### Task

**Task** is an external object of **HvigorTask**. You can use this object to access properties of a task and manage tasks.

## Modules to Import

import { Task } from '@ohos/hvigor';

## getName

getName: () => string

Obtains the task name.

**Return value**

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

string

 | 

Task name obtained.

 |

**Example**

// Project-level hvigorfile.ts file
import { appTasks } from '@ohos/hvigor-ohos-plugin';
import { hvigor, Task } from '@ohos/hvigor';

hvigor.nodesEvaluated(() => {
    const rootNode = hvigor.getRootNode();
    const assembleAppTask: Task | undefined = rootNode.getTaskByName('assembleApp');
    if (assembleAppTask) {
        const taskName = assembleAppTask.getName();
        console.log(\`taskName: ${taskName}\`);
    }
});

export default {
    system: appTasks,  /\* Built-in plugin of Hvigor. It cannot be modified. \*/
    plugins:\[\]         /\* Custom plugin to extend the functionality of Hvigor. \*/
}

## getDependencies

getDependencies: () => string\[\]

Obtains the dependencies, on which this task depends.

**Return value**

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

string\[\]

 | 

Dependencies to obtain.

 |

**Example**

// Project-level hvigorfile.ts file
import { appTasks } from '@ohos/hvigor-ohos-plugin';
import { hvigor, Task } from '@ohos/hvigor';

hvigor.nodesEvaluated(() => {
    const rootNode = hvigor.getRootNode();
    const assembleAppTask: Task | undefined = rootNode.getTaskByName('assembleApp');
    if (assembleAppTask) {
        const taskDependencies = assembleAppTask.getDependencies();
        console.log(\`Task Dependencies: ${taskDependencies}\`);
    }
});

export default {
    system: appTasks,  /\* Built-in plugin of Hvigor. It cannot be modified. \*/
    plugins:\[\]         /\* Custom plugin to extend the functionality of Hvigor. \*/
}

## setEnable

setEnable: (enable: boolean) => void

Sets task status. Disabling a task skips the execution of the task without affecting the task dependency relationships. When a task is registered, it is enabled by default.

**Parameters**

| 
Name

 | 

Type

 | 

Mandatory

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

enable

 | 

boolean

 | 

Yes

 | 

Whether to enable the task. The value **true** means to enable the task, and the value **false** means the opposite.

 |

**Example**

// Project-level hvigorfile.ts file
import { appTasks, OhosHapContext, OhosPluginId, Target } from '@ohos/hvigor-ohos-plugin';
import { hvigor, HvigorNode } from '@ohos/hvigor';

hvigor.nodesEvaluated(() => {
    const rootNode = hvigor.getRootNode();
    rootNode.subNodes((node: HvigorNode) => {
        // Obtain the context information of the HAP module.
        const hapContext = node.getContext(OhosPluginId.OHOS\_HAP\_PLUGIN) as OhosHapContext;
        const moduleName = hapContext?.getModuleName();
        hapContext?.targets((target: Target) => {
            // Disable the task.
            node.getTaskByName(\`${target.getTargetName()}@SignHap\`)?.setEnable(false);
        });
    });
});

export default {
    system: appTasks,  /\* Built-in plugin of Hvigor. It cannot be modified. \*/
    plugins:\[\]         /\* Custom plugin to extend the functionality of Hvigor. \*/
}

## beforeRun

beforeRun: (fn: Function) => void

Adds a hook function to run before this task. Hook functions are stored in a stack struct and follow the first in last out (FILO) approach, which allows the last function added to be processed first.

**Parameters**

| 
Name

 | 

Type

 | 

Mandatory

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

fn

 | 

Function

 | 

Yes

 | 

Hook function to add.

 |

**Example**

// Project-level hvigorfile.ts file
import { appTasks } from '@ohos/hvigor-ohos-plugin';
import { hvigor, Task } from '@ohos/hvigor';

hvigor.nodesEvaluated(() => {
    const rootNode = hvigor.getRootNode();
    const assembleAppTask: Task | undefined = rootNode.getTaskByName('assembleApp');
    if (assembleAppTask) {
        // Hook function to run before this task
        assembleAppTask.beforeRun(() => {
            console.log('Before Task: assembleApp');
        });
    }
});

export default {
    system: appTasks,  /\* Built-in plugin of Hvigor. It cannot be modified. \*/
    plugins:\[\]         /\* Custom plugin to extend the functionality of Hvigor. \*/
}

## afterRun

afterRun: (fn: Function) => void

Adds a hook function to run after this task. Hook functions are stored in a stack struct and follow the FIFO approach, which allows the first function added to be processed first.

**Parameters**

| 
Name

 | 

Type

 | 

Mandatory

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

fn

 | 

Function

 | 

Yes

 | 

Hook function to add.

 |

**Example**

// Project-level hvigorfile.ts file
import { appTasks } from '@ohos/hvigor-ohos-plugin';
import { hvigor, Task } from '@ohos/hvigor';

hvigor.nodesEvaluated(() => {
    const rootNode = hvigor.getRootNode();
    const assembleAppTask: Task | undefined = rootNode.getTaskByName('assembleApp');
    if (assembleAppTask) {
        // Hook function to run after this task
        assembleAppTask.afterRun(() => {
            console.log('After Task: assembleApp');
        });
    }
});

export default {
    system: appTasks,  /\* Built-in plugin of Hvigor. It cannot be modified. \*/
    plugins:\[\]         /\* Custom plugin to extend the functionality of Hvigor. \*/
}

#### SdkDetails

Represents the information of the SDK used by the app project. Before calling this API, you can use the [getSdkDetails](../plug-in-context/document.md#section085712212299) method of **OhosAppContext** to obtain the object.

## Importing Modules

import { SdkDetails } from '@ohos/hvigor-ohos-plugin';

## getSdkDir

getSdkDir: () => string

Obtains the SDK directory.

**Since**: Hvigor 6.0.4

**Return value**

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

string

 | 

SDK directory to obtain.

 |

Sample code for the project-level **hvigorfile.ts** file:

// Project-level hvigorfile.ts file
import { appTasks, OhosAppContext, OhosPluginId, SdkDetails } from '@ohos/hvigor-ohos-plugin';
import { hvigor, HvigorNode, HvigorPlugin } from '@ohos/hvigor';

export function customPlugin(): HvigorPlugin {
  return {
    pluginId: 'customPlugin',
    context() {
      return {
        data: 'customPlugin xxx'
      };
    },
    async apply(currentNode: HvigorNode): Promise<void> {
      hvigor.afterNodeEvaluate(node => {
        const appContext = node.getContext(OhosPluginId.OHOS\_APP\_PLUGIN) as OhosAppContext;
        if (appContext) {
          let sdk:SdkDetails = appContext.getSdkDetails();
          console.log(sdk?.getSdkDir())
        }
      });
    }
  };
}

export default {
  system: appTasks,  /\* Built-in plugin of Hvigor. It cannot be modified. \*/
  plugins:\[customPlugin()\]         /\* Custom plugin to extend the functionality of Hvigor. \*/
}

## isOhos

isOhos: () => boolean

Determines whether the OpenHarmony SDK is in use.

**Since**: Hvigor 6.0.4

**Return value**

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

boolean

 | 

Whether the OpenHarmony SDK is in use.

 |

Sample code for the project-level **hvigorfile.ts** file:

// Project-level hvigorfile.ts file
import { appTasks } from '@ohos/hvigor-ohos-plugin';
import { OhosAppContext, OhosPluginId, SdkDetails } from '@ohos/hvigor-ohos-plugin';
import { hvigor, HvigorNode, HvigorPlugin } from '@ohos/hvigor';

export function customPlugin(): HvigorPlugin {
  return {
    pluginId: 'customPlugin',
    context() {
      return {
        data: 'customPlugin xxx'
      };
    },
    async apply(currentNode: HvigorNode): Promise<void> {
      hvigor.afterNodeEvaluate(node => {
        const appContext = node.getContext(OhosPluginId.OHOS\_APP\_PLUGIN) as OhosAppContext;
        if (appContext) {
          let sdk:SdkDetails = appContext.getSdkDetails();
          console.log(sdk?.isOhos())
        }
      });
    }
  };
}

export default {
  system: appTasks,  /\* Built-in plugin of Hvigor. It cannot be modified. \*/
  plugins:\[customPlugin()\]         /\* Custom plugin to extend the functionality of Hvigor. \*/
}

## getSdkVersion

getSdkVersion: () => number

Obtains the SDK version number.

**Since**: Hvigor 6.0.4

**Return value**

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

number

 | 

SDK version.

 |

Sample code for the project-level **hvigorfile.ts** file:

// Project-level hvigorfile.ts file
import { appTasks } from '@ohos/hvigor-ohos-plugin';
import { OhosAppContext, OhosHapContext, OhosPluginId, SdkDetails } from '@ohos/hvigor-ohos-plugin';
import { hvigor, HvigorNode, HvigorPlugin } from '@ohos/hvigor';

export function customPlugin(): HvigorPlugin {
  return {
    pluginId: 'customPlugin',
    context() {
      return {
        data: 'customPlugin xxx'
      };
    },
    async apply(currentNode: HvigorNode): Promise<void> {
      hvigor.afterNodeEvaluate(node => {
        const appContext = node.getContext(OhosPluginId.OHOS\_APP\_PLUGIN) as OhosAppContext;
        if (appContext) {
          let sdk:SdkDetails = appContext.getSdkDetails();
          console.log(sdk?.getSdkVersion())
        }
      });
    }
  };
}

export default {
  system: appTasks,  /\* Built-in plugin of Hvigor. It cannot be modified. \*/
  plugins:\[customPlugin()\]         /\* Custom plugin to extend the functionality of Hvigor. \*/
}

## getEtsComponentVersion

getEtsComponentVersion: () => string

Obtains the version number of the ETS components in the SDK (components located in the **_DevEco Studio installation directory_/sdk/default/openharmony/ets** directory).

**Since**: Hvigor 6.0.4

**Return value**

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

string

 | 

Version number to obtain.

 |

Sample code for the project-level **hvigorfile.ts** file:

// Project-level hvigorfile.ts file
import { appTasks } from '@ohos/hvigor-ohos-plugin';
import { OhosAppContext, OhosPluginId, SdkDetails } from '@ohos/hvigor-ohos-plugin';
import { hvigor, HvigorNode, HvigorPlugin } from '@ohos/hvigor';

export function customPlugin(): HvigorPlugin {
  return {
    pluginId: 'customPlugin',
    context() {
      return {
        data: 'customPlugin xxx'
      };
    },
    async apply(currentNode: HvigorNode): Promise<void> {
      hvigor.afterNodeEvaluate(node => {
        const appContext = node.getContext(OhosPluginId.OHOS\_APP\_PLUGIN) as OhosAppContext;
        if (appContext) {
          let sdk:SdkDetails = appContext.getSdkDetails();
          console.log(sdk?.getEtsComponentVersion())
        }
      });
    }
  };
}

export default {
  system: appTasks,  /\* Built-in plugin of Hvigor. It cannot be modified. \*/
  plugins:\[customPlugin()\]         /\* Custom plugin to extend the functionality of Hvigor. \*/
}

## getEtsComponentReleaseType

getEtsComponentReleaseType: () => string

Obtains the release type of the ETS components in the SDK (components located in the **_DevEco Studio installation directory_/sdk/default/openharmony/ets** directory).

**Since**: Hvigor 6.0.4

**Return value**

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

string

 | 

Release type to obtain.

 |

Sample code for the project-level **hvigorfile.ts** file:

// Project-level hvigorfile.ts file
import { appTasks } from '@ohos/hvigor-ohos-plugin';
import { OhosAppContext, OhosPluginId, SdkDetails } from '@ohos/hvigor-ohos-plugin';
import { hvigor, HvigorNode, HvigorPlugin } from '@ohos/hvigor';

export function customPlugin(): HvigorPlugin {
  return {
    pluginId: 'customPlugin',
    context() {
      return {
        data: 'customPlugin xxx'
      };
    },
    async apply(currentNode: HvigorNode): Promise<void> {
      hvigor.afterNodeEvaluate(node => {
        const appContext = node.getContext(OhosPluginId.OHOS\_APP\_PLUGIN) as OhosAppContext;
        if (appContext) {
          let sdk:SdkDetails = appContext.getSdkDetails();
          console.log(sdk?.getEtsComponentReleaseType())
        }
      });
    }
  };
}

export default {
  system: appTasks,  /\* Built-in plugin of Hvigor. It cannot be modified. \*/
  plugins:\[customPlugin()\]         /\* Custom plugin to extend the functionality of Hvigor. \*/
}

#### NormalizedFile

Implements the file class in the hvigor API. You can perform some basic file operations through the class object.

## filePath

filePath: string

Path information of this object.

**Since**: Hvigor 4.3.0

**Example**

// Project-level hvigorfile.ts file
import { appTasks } from '@ohos/hvigor-ohos-plugin';
import { hvigor } from '@ohos/hvigor';

hvigor.nodesEvaluated(() => {
    const rootNode = hvigor.getRootNode();
    const moduleNormalizedFile = rootNode.nodeDir;
    console.log(\`Module Normalized File Path: ${moduleNormalizedFile.filePath}\`);

})

export default {
    system: appTasks,  /\* Built-in plugin of Hvigor. It cannot be modified. \*/
    plugins:\[\]         /\* Custom plugin to extend the functionality of Hvigor. \*/
}

## getPath

getPath: () => string

Obtains the path information of this object.

**Since**: Hvigor 4.3.0

**Return value**

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

string

 | 

Path information of the current object.

 |

**Example**

// Project-level hvigorfile.ts file
import { appTasks } from '@ohos/hvigor-ohos-plugin';
import { hvigor } from '@ohos/hvigor';

hvigor.nodesEvaluated(() => {
    const rootNode = hvigor.getRootNode();
    const moduleNormalizedFile = rootNode.nodeDir;
    console.log(\`Module Normalized File Path: ${moduleNormalizedFile.getPath()}\`);
})

export default {
    system: appTasks,  /\* Built-in plugin of Hvigor. It cannot be modified. \*/
    plugins:\[\]         /\* Custom plugin to extend the functionality of Hvigor. \*/
}

## file

file: (\_path: string) => NormalizedFile

Concatenates the path to the existing directory path in a chain, and obtains its **NormalizedFile** object.

**Since**: Hvigor 4.3.0

**Parameters**

| 
Name

 | 

Type

 | 

Mandatory

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

\_path

 | 

string

 | 

Yes

 | 

Path to be concatenated.

 |

**Return value**

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

[NormalizedFile](#section281448112713)

 | 

**NormalizedFile** object obtained through chaining of paths to the existing **NormalizedFile** object.

 |

**Example**

// Project-level hvigorfile.ts file
import { appTasks } from '@ohos/hvigor-ohos-plugin';
import { hvigor } from '@ohos/hvigor';

hvigor.nodesEvaluated(() => {
    const rootNode = hvigor.getRootNode();
    const moduleNormalizedFile = rootNode.nodeDir;
    const buildProfileNormalizedFile = moduleNormalizedFile.file('build-profile.json5');
    console.log(\`buildProfile File Path: ${buildProfileNormalizedFile.getPath()}\`);
})

export default {
    system: appTasks,  /\* Built-in plugin of Hvigor. It cannot be modified. \*/
    plugins:\[\]         /\* Custom plugin to extend the functionality of Hvigor. \*/
}

## asFileList

asFileList: () => NormalizedFile\[\]

Obtains all the files and directories recursively contained within the **NormalizedFile** object, including the object itself.

**Since**: Hvigor 4.3.0

**Return value**

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

[NormalizedFile](#section281448112713)\[\]

 | 

Files and directories recursively contained within the **NormalizedFile** object, including the object itself.

 |

Currently, you can only obtain the **NormalizedFile** object of the root path of a node using the **node.nodeDir** or **node.node.getNodeDir()** API. Then, by using the **NormalizedFile.file(\_path: string)** API to concatenate subsequent paths, you can obtain a new **NormalizedFile** object. The following is an example of the project-level **hvigorfile.ts** file:

import { appTasks } from '@ohos/hvigor-ohos-plugin';
// Import dependencies.
import { HvigorPlugin, HvigorNode} from '@ohos/hvigor';
// Implement a custom plugin.
function customPlugin(): HvigorPlugin {
    return {
        pluginId: 'customPlugin',
        apply(node: HvigorNode) {
            appTask(node);
        }
    }
}
function appTask(currentNode: HvigorNode) {
    // Project-level node
    currentNode.subNodes((node: HvigorNode) => {
        // Module-level node
        // Obtain the NormalizedFile object in the root path of the node through node.nodeDir or node.node.getNodeDir().
        const moduleNormalizedFile = node.nodeDir;
        // Use NormalizedFile.file () to concatenate subsequent paths and generate a new NormalizedFile object.
        // Generate the NormalizedFile object of the build-Profile.json5 file for the module.
        const buildProfileNormalizedFile = moduleNormalizedFile.file('build-profile.json5');
    })
}
export default {
    system: appTasks,  /\* Built-in plugin of Hvigor. It cannot be modified. \*/
    plugins:\[
        customPlugin()  // Custom plug-in.
    \]         /\* Custom plugin to extend the functionality of Hvigor. \*/
}

#### FileUtil

Represents the file utility class, which supports some basic file operations.

## Modules to Import

import { FileUtil } from '@ohos/hvigor';

## exist

exist: (filePath: string) => boolean

Checks whether a file path exists.

**Since**: Hvigor 4.3.0

**Parameters**

| 
Name

 | 

Type

 | 

Mandatory

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

filePath

 | 

string

 | 

Yes

 | 

File path.

 |

**Return value**

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

boolean

 | 

**true**: The file path exists. **false**: The file path does not exist.

 |

**Example**

// Project-level hvigorfile.ts file
import { appTasks, OhosPluginId, OhosAppContext } from '@ohos/hvigor-ohos-plugin';
import { hvigor, FileUtil, getNode } from '@ohos/hvigor';
import path from "path";
const currentNode = getNode(\_\_filename);
hvigor.nodesEvaluated(() => {
    const context = currentNode.getContext(OhosPluginId.OHOS\_APP\_PLUGIN) as OhosAppContext;
    const testFilePath = path.resolve(context.getProjectPath(), 'test.txt');
    if (FileUtil.exist(testFilePath)) {
        console.log(\`File exists: ${testFilePath}\`);
    } else {
        console.log(\`File doesn't exist: ${testFilePath}\`);
    }
})
export default {
    system: appTasks,  /\* Built-in plugin of Hvigor. It cannot be modified. \*/
    plugins:\[\]         /\* Custom plugin to extend the functionality of Hvigor. \*/
}

## isDictionary

isDictionary: (file: string | NormalizedFile) => boolean

Checks whether a file path or **NormalizedFile** object is a directory.

**Since**: Hvigor 4.3.0

**Parameters**

| 
Name

 | 

Type

 | 

Mandatory

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

file

 | 

string | [NormalizedFile](#section281448112713)

 | 

Yes

 | 

File path or **NormalizedFile** object.

 |

**Return value**

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

boolean

 | 

**true**: The target is a directory. **false**: The target is not a directory.

 |

**Example**

// Project-level hvigorfile.ts file
import { appTasks, OhosPluginId, OhosAppContext } from '@ohos/hvigor-ohos-plugin';
import { hvigor, FileUtil, getNode } from '@ohos/hvigor';
import path from "path";

const currentNode = getNode(\_\_filename);

hvigor.nodesEvaluated(() => {
    const context = currentNode.getContext(OhosPluginId.OHOS\_APP\_PLUGIN) as OhosAppContext;
    const testFilePath = path.resolve(context.getProjectPath(), 'test.txt');
    FileUtil.ensureFileSync(testFilePath);
    if (FileUtil.isDictionary(testFilePath)) {
        console.log(\`It is a directory: ${testFilePath}\`);
    } else {
        console.log(\`It is not a directory: ${testFilePath}\`);
    }
})

export default {
    system: appTasks,  /\* Built-in plugin of Hvigor. It cannot be modified. \*/
    plugins:\[\]         /\* Custom plugin to extend the functionality of Hvigor. \*/
}

## isFile

isFile: (file: string | NormalizedFile) => boolean

Checks whether a file path or **NormalizedFile** object is a file.

**Since**: Hvigor 4.3.0

**Parameters**

| 
Name

 | 

Type

 | 

Mandatory

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

file

 | 

string | [NormalizedFile](#section281448112713)

 | 

Yes

 | 

File path or **NormalizedFile** object.

 |

**Return value**

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

boolean

 | 

**true**: The target is a file. **false**: The target is not a file.

 |

**Example**

// Project-level hvigorfile.ts file
import { appTasks, OhosPluginId, OhosAppContext } from '@ohos/hvigor-ohos-plugin';
import { hvigor, FileUtil, getNode } from '@ohos/hvigor';
import path from "path";

const currentNode = getNode(\_\_filename);

hvigor.nodesEvaluated(() => {
    const context = currentNode.getContext(OhosPluginId.OHOS\_APP\_PLUGIN) as OhosAppContext;
    const testFilePath = path.resolve(context.getProjectPath(), 'test.txt');
    FileUtil.ensureFileSync(testFilePath);
    if (FileUtil.isFile(testFilePath)) {
        console.log(\`It is a file: ${testFilePath}\`);
    } else {
        console.log(\`It is not a file: ${testFilePath}\`);
    }
})

export default {
    system: appTasks,  /\* Built-in plugin of Hvigor. It cannot be modified. \*/
    plugins:\[\]         /\* Custom plugin to extend the functionality of Hvigor. \*/
}

## ensureDirSync

ensureDirSync: (dirPath: string) => void

Ensures that the directory exists; creates it if does not exist.

**Since**: Hvigor 4.3.0

**Parameters**

| 
Name

 | 

Type

 | 

Mandatory

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

dirPath

 | 

string

 | 

Yes

 | 

Destination directory address.

 |

**Example**

// Project-level hvigorfile.ts file
import { appTasks, OhosPluginId, OhosAppContext } from '@ohos/hvigor-ohos-plugin';
import { hvigor, FileUtil, getNode } from '@ohos/hvigor';
import path from "path";
const currentNode = getNode(\_\_filename);
hvigor.nodesEvaluated(() => {
    const context = currentNode.getContext(OhosPluginId.OHOS\_APP\_PLUGIN) as OhosAppContext;   
    FileUtil.ensureDirSync(path.dirname(context.getBuildRootPath()));
})
export default {
    system: appTasks,  /\* Built-in plugin of Hvigor. It cannot be modified. \*/
    plugins:\[\]         /\* Custom plugin to extend the functionality of Hvigor. \*/
}

## ensureFileSync

ensureFileSync: (filePath: string) => void

Ensures that the file exists; creates it if does not exist.

**Since**: Hvigor 4.3.0

**Parameters**

| 
Name

 | 

Type

 | 

Mandatory

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

filePath

 | 

string

 | 

Yes

 | 

Destination file address.

 |

**Example**

// Project-level hvigorfile.ts file
import { appTasks, OhosPluginId, OhosAppContext } from '@ohos/hvigor-ohos-plugin';
import { hvigor, FileUtil, getNode } from '@ohos/hvigor';
import path from "path";

const currentNode = getNode(\_\_filename);

hvigor.nodesEvaluated(() => {
    const context = currentNode.getContext(OhosPluginId.OHOS\_APP\_PLUGIN) as OhosAppContext;
    const testFilePath = path.resolve(context.getProjectPath(), 'test.txt');
    FileUtil.ensureFileSync(testFilePath);
})

export default {
    system: appTasks,  /\* Built-in plugin of Hvigor. It cannot be modified. \*/
    plugins:\[\]         /\* Custom plugin to extend the functionality of Hvigor. \*/
}

## readJson5

readJson5: (file: string | NormalizedFile) => JSON

Reads a JSON5 file synchronously.

**Since**: Hvigor 4.3.0

**Parameters**

| 
Name

 | 

Type

 | 

Mandatory

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

file

 | 

string | [NormalizedFile](#section281448112713)

 | 

Yes

 | 

JSON5 file path or **NormalizedFile** object.

 |

**Return value**

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

JSON

 | 

Read JSON data.

 |

**Example**

// Project-level hvigorfile.ts file
import { appTasks, OhosPluginId, OhosAppContext } from '@ohos/hvigor-ohos-plugin';
import { hvigor, FileUtil, getNode } from '@ohos/hvigor';
import path from "path";

const currentNode = getNode(\_\_filename);

hvigor.nodesEvaluated(() => {
    const context = currentNode.getContext(OhosPluginId.OHOS\_APP\_PLUGIN) as OhosAppContext;
    const json5FilePath = path.resolve(context.getProjectPath(), 'testJson.json5');
    FileUtil.ensureFileSync(json5FilePath);
    FileUtil.writeFileSync(json5FilePath, JSON.stringify(context.getAppJsonOpt()));
    const jsonContent = FileUtil.readJson5(json5FilePath);
    console.log(\`Read JSON5 content: ${JSON.stringify(jsonContent, null, 2)}\`);
})

export default {
    system: appTasks,  /\* Built-in plugin of Hvigor. It cannot be modified. \*/
    plugins:\[\]         /\* Custom plugin to extend the functionality of Hvigor. \*/
}

## readFileSync

readFileSync: (file: string | NormalizedFile) => Buffer

Reads a file synchronously.

**Since**: Hvigor 4.3.0

**Parameters**

| 
Name

 | 

Type

 | 

Mandatory

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

file

 | 

string | [NormalizedFile](#section281448112713)

 | 

Yes

 | 

File path or **NormalizedFile** object.

 |

**Return value**

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

Buffer

 | 

Read buffer data.

 |

**Example**

// Project-level hvigorfile.ts file
import { appTasks, OhosPluginId, OhosAppContext } from '@ohos/hvigor-ohos-plugin';
import { hvigor, FileUtil, getNode } from '@ohos/hvigor';
import path from "path";

const currentNode = getNode(\_\_filename);

hvigor.nodesEvaluated(() => {
    const context = currentNode.getContext(OhosPluginId.OHOS\_APP\_PLUGIN) as OhosAppContext;
    const json5FilePath = path.resolve(context.getProjectPath(), 'testJson.json5');
    FileUtil.ensureFileSync(json5FilePath);
    FileUtil.writeFileSync(json5FilePath, JSON.stringify(context.getAppJsonOpt()));
    const content = FileUtil.readFileSync(json5FilePath);
    console.log(\`Content of ${json5FilePath}: ${content}\`);
})

export default {
    system: appTasks,  /\* Built-in plugin of Hvigor. It cannot be modified. \*/
    plugins:\[\]         /\* Custom plugin to extend the functionality of Hvigor. \*/
}

## readFile

readFile: (file: string | NormalizedFile) => Promise<Buffer>

Reads a file asynchronously.

**Since**: Hvigor 4.3.0

**Parameters**

| 
Name

 | 

Type

 | 

Mandatory

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

file

 | 

string | [NormalizedFile](#section281448112713)

 | 

Yes

 | 

File path or **NormalizedFile** object.

 |

**Return value**

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

Promise

 | 

Promise<Buffer>

 |

**Example**

// Project-level hvigorfile.ts file
import { appTasks, OhosPluginId, OhosAppContext } from '@ohos/hvigor-ohos-plugin';
import { hvigor, FileUtil, getNode } from '@ohos/hvigor';
import path from "path";

const currentNode = getNode(\_\_filename);

hvigor.nodesEvaluated(async () => {
    const context = currentNode.getContext(OhosPluginId.OHOS\_APP\_PLUGIN) as OhosAppContext;
    const json5FilePath = path.resolve(context.getProjectPath(), 'testJson.json5');
    FileUtil.ensureFileSync(json5FilePath);
    FileUtil.writeFileSync(json5FilePath, JSON.stringify(context.getAppJsonOpt()));
    const content = await FileUtil.readFile(json5FilePath);
    console.log(content.toString());
})

export default {
    system: appTasks,  /\* Built-in plugin of Hvigor. It cannot be modified. \*/
    plugins:\[\]         /\* Custom plugin to extend the functionality of Hvigor. \*/
}

## writeFileSync

writeFileSync: (file: string | NormalizedFile, content: any) => void

Write data to a file synchronously.

**Since**: Hvigor 4.3.0

**Parameters**

| 
Name

 | 

Type

 | 

Mandatory

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

file

 | 

string | [NormalizedFile](#section281448112713)

 | 

Yes

 | 

File path or **NormalizedFile** object.

 |
| 

content

 | 

any

 | 

Yes

 | 

Data to be written to the file.

 |

**Example**

// Project-level hvigorfile.ts file
import { appTasks, OhosPluginId, OhosAppContext } from '@ohos/hvigor-ohos-plugin';
import { hvigor, FileUtil, getNode } from '@ohos/hvigor';
import path from "path";

const currentNode = getNode(\_\_filename);

hvigor.nodesEvaluated(() => {
    const context = currentNode.getContext(OhosPluginId.OHOS\_APP\_PLUGIN) as OhosAppContext;
    const json5FilePath = path.resolve(context.getProjectPath(), 'testJson.json5');
    FileUtil.ensureFileSync(json5FilePath);
    FileUtil.writeFileSync(json5FilePath, JSON.stringify(context.getAppJsonOpt()));
    const jsonContent = FileUtil.readJson5(json5FilePath);
    console.log(\`Read JSON5 content: ${JSON.stringify(jsonContent, null, 2)}\`);
})

export default {
    system: appTasks,  /\* Built-in plugin of Hvigor. It cannot be modified. \*/
    plugins:\[\]         /\* Custom plugin to extend the functionality of Hvigor. \*/
}

## writeFile

writeFile: (file: string | NormalizedFile, content: any) => Promise<void>

Write data to a file asynchronously.

**Since**: Hvigor 4.3.0

**Parameters**

| 
Name

 | 

Type

 | 

Mandatory

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

file

 | 

string | [NormalizedFile](#section281448112713)

 | 

Yes

 | 

File path or **NormalizedFile** object.

 |
| 

content

 | 

any

 | 

Yes

 | 

Data to be written to the file.

 |

**Return value**

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

Promise

 | 

Promise<void>

 |

**Example**

// Project-level hvigorfile.ts file
import { appTasks, OhosPluginId, OhosAppContext } from '@ohos/hvigor-ohos-plugin';
import { hvigor, FileUtil, getNode } from '@ohos/hvigor';
import path from "path";

const currentNode = getNode(\_\_filename);

hvigor.nodesEvaluated(() => {
    const context = currentNode.getContext(OhosPluginId.OHOS\_APP\_PLUGIN) as OhosAppContext;
    const json5FilePath = path.resolve(context.getProjectPath(), 'testJson.json5');
    FileUtil.ensureFileSync(json5FilePath);
    FileUtil.writeFile(json5FilePath, JSON.stringify(context.getAppJsonOpt()));
})

export default {
    system: appTasks,  /\* Built-in plugin of Hvigor. It cannot be modified. \*/
    plugins:\[\]         /\* Custom plugin to extend the functionality of Hvigor. \*/
}

## copyFileSync

copyFileSync: (file: string | NormalizedFile, dest: string) => void

Copies a file synchronously.

**Since**: Hvigor 4.3.0

**Parameters**

| 
Name

 | 

Type

 | 

Mandatory

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

file

 | 

string | [NormalizedFile](#section281448112713)

 | 

Yes

 | 

File path or **NormalizedFile** object.

 |
| 

dest

 | 

string

 | 

Yes

 | 

Target file path.

 |

**Example**

// Project-level hvigorfile.ts file
import { appTasks, OhosPluginId, OhosAppContext } from '@ohos/hvigor-ohos-plugin';
import { hvigor, FileUtil, getNode } from '@ohos/hvigor';

const currentNode = getNode(\_\_filename);

hvigor.nodesEvaluated(() => {
    const context = currentNode.getContext(OhosPluginId.OHOS\_APP\_PLUGIN) as OhosAppContext;
    const json5FilePath = FileUtil.pathResolve(context.getProjectPath(), 'testJson.json5');
    FileUtil.ensureFileSync(json5FilePath);
    FileUtil.writeFileSync(json5FilePath, JSON.stringify(context.getAppJsonOpt()));
    const copyFilePath = FileUtil.pathResolve(context.getProjectPath(), 'testJson\_copy.json5');
    FileUtil.copyFileSync(json5FilePath, copyFilePath);
})

export default {
    system: appTasks,  /\* Built-in plugin of Hvigor. It cannot be modified. \*/
    plugins:\[\]         /\* Custom plugin to extend the functionality of Hvigor. \*/
}

## copyFile

copyFile: (file: string | NormalizedFile, dest: string) => Promise<void>

Copies a file asynchronously.

**Since**: Hvigor 4.3.0

**Parameters**

| 
Name

 | 

Type

 | 

Mandatory

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

file

 | 

string | [NormalizedFile](#section281448112713)

 | 

Yes

 | 

File path or **NormalizedFile** object.

 |
| 

dest

 | 

string

 | 

Yes

 | 

Target file path.

 |

**Return value**

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

Promise

 | 

Promise<void>

 |

**Example**

// Project-level hvigorfile.ts file
import { appTasks, OhosPluginId, OhosAppContext } from '@ohos/hvigor-ohos-plugin';
import { hvigor, FileUtil, getNode } from '@ohos/hvigor';

const currentNode = getNode(\_\_filename);

hvigor.nodesEvaluated(() => {
    const context = currentNode.getContext(OhosPluginId.OHOS\_APP\_PLUGIN) as OhosAppContext;
    const json5FilePath = FileUtil.pathResolve(context.getProjectPath(), 'testJson.json5');
    FileUtil.ensureFileSync(json5FilePath);
    FileUtil.writeFileSync(json5FilePath, JSON.stringify(context.getAppJsonOpt()));
    const copyFilePath = FileUtil.pathResolve(context.getProjectPath(), 'testJson\_copy.json5');
    FileUtil.copyFile(json5FilePath, copyFilePath);
})

export default {
    system: appTasks,  /\* Built-in plugin of Hvigor. It cannot be modified. \*/
    plugins:\[\]         /\* Custom plugin to extend the functionality of Hvigor. \*/
}

## pathResolve

pathResolve: (...paths: string\[\]) => string

Concatenates paths.

**Since**: Hvigor 4.3.0

**Parameters**

| 
Name

 | 

Type

 | 

Mandatory

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

...paths

 | 

string\[\]

 | 

Yes

 | 

Array of file paths.

 |

**Return value**

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

string

 | 

Path obtained after concatenation.

 |

**Example**

// Project-level hvigorfile.ts file
import { appTasks, OhosPluginId, OhosAppContext } from '@ohos/hvigor-ohos-plugin';
import { hvigor, FileUtil, getNode } from '@ohos/hvigor';

const currentNode = getNode(\_\_filename);

hvigor.nodesEvaluated(() => {
    const context = currentNode.getContext(OhosPluginId.OHOS\_APP\_PLUGIN) as OhosAppContext;
    const json5FilePath = FileUtil.pathResolve(context.getProjectPath(), 'testJson.json5');
    FileUtil.ensureFileSync(json5FilePath);
    FileUtil.writeFile(json5FilePath, JSON.stringify(context.getAppJsonOpt()));
})

export default {
    system: appTasks,  /\* Built-in plugin of Hvigor. It cannot be modified. \*/
    plugins:\[\]         /\* Custom plugin to extend the functionality of Hvigor. \*/
}

#### submitWorker

submitWorker(node: HvigorNode, taskName: string, workPath: string, workerOption: WorkerOption): TCB

Submits a worker to the thread pool and executes it. The worker must belong to a specific task, indicating that the task has not yet ended. However, the main thread can execute other tasks at this time, while other tasks dependent on this task will still queue and wait.

**Since**: Hvigor 6.0.4

**Parameters**

| 
Name

 | 

Type

 | 

Mandatory

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

node

 | 

[HvigorNode](#section14832104719474)

 | 

Yes

 | 

Node of the task to which the worker belongs.

 |
| 

taskName

 | 

string

 | 

Yes

 | 

Name of the task that submits the worker to the thread pool.

 |
| 

workPath

 | 

string

 | 

Yes

 | 

File path of the worker to be executed, to which the function name can be appended, for example, **D:/xx/a.js/run**, indicating the **run** method of **a.js**.

 |
| 

workerOption

 | 

[WorkerOption](#section2701859185318)

 | 

Yes

 | 

Worker configuration.

 |

**Return value**

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

[TCB](#section282818554815)

 | 

Status of the submitted worker.

 |

**Example**: Submitting a worker to the thread pool in the custom task of the HAP module

import { hapTasks } from '@ohos/hvigor-ohos-plugin';
import { HvigorNode, HvigorPlugin, submitWorker } from "@ohos/hvigor";
import path from "path";

// Implement a custom plugin.
function customPlugin(): HvigorPlugin {
  return {
    pluginId: 'customPlugin',
    apply(node: HvigorNode) {
      // Plugin code.
      node.registerTask({
        name: 'customTask',
        run() {
          submitWorker(node, this.name, path.join(\_\_dirname, 'wait-job.js', 'wait'), {callback: () => {
            console.log('submit Worker callback');
          }});
        },
        dependencies: \['default@PreBuild'\],
        postDependencies: \['assembleHap'\],
      });
    }
  }
}

export default {
  system: hapTasks /\* Built-in plugin of Hvigor. It cannot be modified. \*/,
  plugins: \[customPlugin()\] /\* Custom plugin to extend the functionality of Hvigor. \*/,  
};

Configure the following in **wait-job.js**. The file is in the same directory as **hvigorfile.ts**.

function sleep(ms) {
    return new Promise(resolve => setTimeout(resolve, ms));
}

async function wait() {
    console.log('Waiting for 10 seconds...');
    await sleep(10000);
    console.log('Finished, exiting the program');
}

exports.wait = wait;

#### WorkerOption

Sets the configuration for submitting a worker to the thread pool. For details, see [submitWorker](#section94763341419).

**Since**: Hvigor 6.0.4

| 
Member

 | 

Declaration

 | 

Description

 |
| :-- | :-- | :-- |
| 

workInput

 | 

workInput?: unknown;

 | 

Input value of the thread to be executed.

 |
| 

priority

 | 

priority?: [Priority](#section162915519616);

 | 

Priority of the thread to be executed.

 |
| 

targetWorkers

 | 

targetWorkers?: number\[\];

 | 

IDs of the threads to execute in.

 |
| 

callback

 | 

callback?: Function;

 | 

Callback function triggered after the execution is complete.

 |
| 

callbackInput

 | 

callbackInput?: unknown\[\];

 | 

Input parameters of the callback function.

 |
| 

useReturnVal

 | 

useReturnVal?: boolean;

 | 

Whether the callback function uses the value returned upon the thread execution completion as the input. The priority of this option is higher than that of **callbackInput**.

 |

#### Priority

Enumerates the priorities of thread execution.

**Since**: Hvigor 6.0.4

| 
Member

 | 

Description

 |
| :-- | :-- |
| 

FIRST

 | 

The priorities decrease from top to bottom.

 |
| 

HEAVY

 |
| 

MEDIUM

 |
| 

LIGHT

 |
| 

LAST

 |

#### TCB

Indicates the status returned after a worker is submitted to the thread pool. For details, see [submitWorker](#section94763341419).

**Since**: Hvigor 6.0.4

| 
Member

 | 

Declaration

 | 

Description

 |
| :-- | :-- | :-- |
| 

getId

 | 

getId(): string;

 | 

Obtains the TCB ID.

 |
| 

getWorkerId

 | 

getWorkerId(): number | undefined;

 | 

Obtains the worker ID.

 |
| 

getSubmitTime

 | 

getSubmitTime(): number;

 | 

Obtains the submission time.

 |
| 

getStartTime

 | 

getStartTime(): number | undefined;

 | 

Obtains the execution start time.

 |
| 

getEndTime

 | 

getEndTime(): number | undefined;

 | 

Obtains the execution end time.

 |
| 

getState

 | 

getState(): TaskState;

 | 

Obtains the worker status.

 |
| 

getPriority

 | 

getPriority(): [Priority](#section162915519616);

 | 

Obtains the execution priority.

 |
| 

getCallback

 | 

getCallback(): Function;

 | 

Obtains the callback function.

 |
| 

getCallbackInput

 | 

getCallbackInput(): unknown\[\];

 | 

Obtains the input of the callback function.

 |
| 

getTaskPath

 | 

getTaskPath(): string;

 | 

Obtains the task path.

 |
| 

getTaskName

 | 

getTaskName(): string;

 | 

Obtains the task name.

 |
| 

getTaskCompletePath

 | 

getTaskCompletePath(): string;

 | 

Obtains the full task path, including the task path and task name.

 |
| 

useReturnVal

 | 

useReturnVal(): boolean;

 | 

Specifies whether the callback function uses the value returned upon the thread execution completion as the input.

 |
