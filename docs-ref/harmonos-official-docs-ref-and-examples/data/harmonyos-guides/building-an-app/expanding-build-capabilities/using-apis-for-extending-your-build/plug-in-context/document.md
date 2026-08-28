# Plug-in Context

#### OhosPluginId

Defines plug-in IDs for **hvigor-ohos-plugin**.

## Modules to Import

import { OhosPluginId } from '@ohos/hvigor-ohos-plugin';

| 
Constant

 | 

Type

 | 

Description

 |
| :-- | :-- | :-- |
| 

OHOS\_APP\_PLUGIN

 | 

string

 | 

AppPlugin ID.

 |
| 

OHOS\_HAP\_PLUGIN

 | 

string

 | 

HapPlugin ID.

 |
| 

OHOS\_HSP\_PLUGIN

 | 

string

 | 

HspPlugin ID.

 |
| 

OHOS\_HAR\_PLUGIN

 | 

string

 | 

HarPlugin ID.

 |

#### OhosAppContext

Context extension API provided by the **appTasks** plug-in externally, containing project information and product information.

## Modules to Import

import { OhosAppContext } from '@ohos/hvigor-ohos-plugin';

## getProjectName

getProjectName: () => string

Obtains the project name.

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

Project name.

 |

**Sample code**

// Project-level hvigorfile.ts file
import { appTasks, OhosAppContext, OhosPluginId } from '@ohos/hvigor-ohos-plugin';
import { hvigor } from '@ohos/hvigor';

hvigor.nodesEvaluated(() => {
    const appContext = hvigor.getRootNode().getContext(OhosPluginId.OHOS\_APP\_PLUGIN) as OhosAppContext;
    const projectName = appContext.getProjectName();
    console.log(\`Project Name: ${projectName}\`);
});

export default {
    system: appTasks,  /\* Built-in plugin of Hvigor. It cannot be modified. \*/
    plugins:\[\]         /\* Custom plugin to extend the functionality of Hvigor. \*/
}

## getProjectPath

getProjectPath: () => string

Obtains the project path.

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

Project path.

 |

**Sample code**

// Project-level hvigorfile.ts file
import { appTasks, OhosAppContext, OhosPluginId } from '@ohos/hvigor-ohos-plugin';
import { hvigor } from '@ohos/hvigor';

hvigor.nodesEvaluated(() => {
    const appContext = hvigor.getRootNode().getContext(OhosPluginId.OHOS\_APP\_PLUGIN) as OhosAppContext;
    const projectPath = appContext.getProjectPath();
    console.log(\`Project Path: ${projectPath}\`);
});

export default {
    system: appTasks,  /\* Built-in plugin of Hvigor. It cannot be modified. \*/
    plugins:\[\]         /\* Custom plugin to extend the functionality of Hvigor. \*/
}

## getBuildRootPath

getBuildRootPath: () => string

Obtains the root path of the build directory.

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

Root path of the build directory.

 |

**Sample code**

// Project-level hvigorfile.ts file
import { appTasks, OhosAppContext, OhosPluginId } from '@ohos/hvigor-ohos-plugin';
import { hvigor } from '@ohos/hvigor';

hvigor.nodesEvaluated(() => {
    const appContext = hvigor.getRootNode().getContext(OhosPluginId.OHOS\_APP\_PLUGIN) as OhosAppContext;
    const buildRootPath = appContext.getBuildRootPath();
    console.log(\`Build Root Path: ${buildRootPath}\`);
});

export default {
    system: appTasks,  /\* Built-in plugin of Hvigor. It cannot be modified. \*/
    plugins:\[\]         /\* Custom plugin to extend the functionality of Hvigor. \*/
}

## getBuildProductOutputPath

getBuildProductOutputPath: () => string

Obtains the output path of the current product build package.

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

Output path of the current product build package.

 |

**Sample code**

// Project-level hvigorfile.ts file
import { appTasks, OhosAppContext, OhosPluginId } from '@ohos/hvigor-ohos-plugin';
import { hvigor } from '@ohos/hvigor';

hvigor.nodesEvaluated(() => {
    const appContext = hvigor.getRootNode().getContext(OhosPluginId.OHOS\_APP\_PLUGIN) as OhosAppContext;
    const buildProductOutputPath =  appContext.getBuildProductOutputPath();
    console.log(\`Build Product Output Path: ${buildProductOutputPath}\`);
});

export default {
    system: appTasks,  /\* Built-in plugin of Hvigor. It cannot be modified. \*/
    plugins:\[\]         /\* Custom plugin to extend the functionality of Hvigor. \*/
}

## getCurrentProduct

getCurrentProduct: () => Product

Obtains the product object specified by the current build.

**Return value**

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

[Product](../basic-build-capability/document.md#section1553414254713)

 | 

Product object specified by the current build.

 |

**Sample code**

// Project-level hvigorfile.ts file
import { appTasks, OhosAppContext, OhosPluginId } from '@ohos/hvigor-ohos-plugin';
import { hvigor } from '@ohos/hvigor';

hvigor.nodesEvaluated(() => {
    const appContext = hvigor.getRootNode().getContext(OhosPluginId.OHOS\_APP\_PLUGIN) as OhosAppContext;
    const currentProduct = appContext.getCurrentProduct();
 });

export default {
    system: appTasks,  /\* Built-in plugin of Hvigor. It cannot be modified. \*/
    plugins:\[\]         /\* Custom plugin to extend the functionality of Hvigor. \*/
}

## getBuildMode

getBuildMode: () => string

Obtains the **BuildMode** specified by the current build.

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

**BuildMode** specified by the current build.

 |

**Sample code**

// Project-level hvigorfile.ts file
import { appTasks, OhosAppContext, OhosPluginId } from '@ohos/hvigor-ohos-plugin';
import { hvigor } from '@ohos/hvigor';

hvigor.nodesEvaluated(() => {
    const appContext = hvigor.getRootNode().getContext(OhosPluginId.OHOS\_APP\_PLUGIN) as OhosAppContext;
    const buildMode = appContext.getBuildMode();
    console.log(\`Build Mode: ${buildMode}\`);
});

export default {
    system: appTasks,  /\* Built-in plugin of Hvigor. It cannot be modified. \*/
    plugins:\[\]         /\* Custom plugin to extend the functionality of Hvigor. \*/
}

## getAppJsonOpt

getAppJsonOpt: () => any

Obtains the object in the **app.json5** file in this build.

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

Object obtained from the **app.json5** file in the current build.

 |

**Sample code**

// Project-level hvigorfile.ts file
import { appTasks, OhosAppContext, OhosPluginId } from '@ohos/hvigor-ohos-plugin';
import { hvigor } from '@ohos/hvigor';

hvigor.nodesEvaluated(() => {
    const appContext = hvigor.getRootNode().getContext(OhosPluginId.OHOS\_APP\_PLUGIN) as OhosAppContext;
    const appJsonOpt =  appContext.getAppJsonOpt();
    console.log(\`bundleName: ${appJsonOpt.app.bundleName}\`);
});

export default {
    system: appTasks,  /\* Built-in plugin of Hvigor. It cannot be modified. \*/
    plugins:\[\]         /\* Custom plugin to extend the functionality of Hvigor. \*/
}

## setAppJsonOpt

setAppJsonOpt: (appJsonOpt: any) => void

Sets the object in the **app.json5** file in this build.

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

appJsonOpt

 | 

any

 | 

Yes

 | 

Object parsed from the contents of the **app.json5** file in this build.

 |

**Sample code**

// Project-level hvigorfile.ts file
import { appTasks, OhosPluginId, OhosAppContext, AppJson } from '@ohos/hvigor-ohos-plugin';
import { hvigor, getNode, HvigorNode  } from '@ohos/hvigor';

hvigor.nodesEvaluated(() => {
    const node: HvigorNode = getNode(\_\_filename);
    const appContext = node.getContext(OhosPluginId.OHOS\_APP\_PLUGIN) as OhosAppContext;
    console.log('projectName:', appContext.getProjectName());
    const appJson5: AppJson.AppOptObj = appContext.getAppJsonOpt();
    if (appContext.getBuildMode() === 'debug') {
        appJson5.app.versionName = '1.0.0-debug';
    } else {
        appJson5.app.versionName = '1.0.0-release';
    }
    appContext.setAppJsonOpt(appJson5);
});
export default {
    system: appTasks,  /\* Built-in plugin of Hvigor. It cannot be modified. \*/
    plugins:\[\]         /\* Custom plugin to extend the functionality of Hvigor. \*/
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6f/v3/rsJBwAjVTKmuQHqNcE_6mA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062156Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=096654647CEE5D3C33E2AA04564B94FF9E0E01F30590142A7C76D6176E0BC397)

The **setAppJsonOpt** API performs schema validation; if the passed object does not conform to the validation rules, it will throw an exception.

## getBuildProfileOpt

getBuildProfileOpt: () => any

Obtains the object from the **build-profile.json5** file located in the root directory of this build.

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

Object obtained from the **build-profile.json5** file located in the root directory of the current build.

 |

**Sample code**

// Project-level hvigorfile.ts file
import { appTasks, OhosAppContext, OhosPluginId } from '@ohos/hvigor-ohos-plugin';
import { hvigor } from '@ohos/hvigor';

hvigor.nodesEvaluated(() => {
    const appContext = hvigor.getRootNode().getContext(OhosPluginId.OHOS\_APP\_PLUGIN) as OhosAppContext;
    const buildProfileOpt = appContext.getBuildProfileOpt();
});

export default {
    system: appTasks,  /\* Built-in plugin of Hvigor. It cannot be modified. \*/
    plugins:\[\]         /\* Custom plugin to extend the functionality of Hvigor. \*/
}

## setBuildProfileOpt

setBuildProfileOpt: (buildProfileOpt: any) => void

Sets the object in the **build-profile.json5** file in this build.

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

buildProfileOpt

 | 

any

 | 

Yes

 | 

Object from the **build-profile.json5** file located in the root directory of the current build.

 |

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/49/v3/myIEclY_RqeURLphFt2KWA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062156Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=A1B3D60F255D659824AF4BEEC02B82045A5FE3EA021D2B7D8B1A89B288A7BEBD)

-   The **setBuildProfileOpt** API performs schema validation; if the passed object does not conform to the validation rules, it will throw an exception.
-   The **maxFlowDepth** field cannot be set using the **setBuildProfileOpt** method.

**Sample code**

// Project-level hvigorfile.ts file
import { appTasks, OhosAppContext, OhosPluginId } from '@ohos/hvigor-ohos-plugin';
import { hvigor } from '@ohos/hvigor';

hvigor.nodesEvaluated(() => {
    const appContext = hvigor.getRootNode().getContext(OhosPluginId.OHOS\_APP\_PLUGIN) as OhosAppContext;
    const buildProfileOpt = appContext.getBuildProfileOpt();
    // Add an external module.
    const newModule = {
        "name": "har",
        "srcPath": "./../MyApplication40/har",// Ensure that the source code module exists.
    }
    buildProfileOpt.modules.push(newModule);
    appContext.setBuildProfileOpt(buildProfileOpt);
    console.log(buildProfileOpt.modules.map(module => {
        return module.name;
    }));
});

export default {
    system: appTasks,  /\* Built-in plugin of Hvigor. It cannot be modified. \*/
    plugins:\[\]         /\* Custom plugin to extend the functionality of Hvigor. \*/
}

## getOhpmDependencyInfo

getOhpmDependencyInfo: () => Record<string, OhpmDependencyInfo> | object

Obtains the dependency information configured in the project-level **oh-package.json5** file.

**Since**: Hvigor 5.0.0

**Return value**

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

Record<string, OhpmDependencyInfo> | object

 | 

Dependency information configured in **oh-package.json5**.

 |

**Sample code**

// Project-level hvigorfile.ts file
import { HvigorNode, HvigorPlugin } from '@ohos/hvigor';
import { appTasks } from '@ohos/hvigor-ohos-plugin';
import { OhosPluginId } from '@ohos/hvigor-ohos-plugin';

// Custom plug-in code
export function customPlugin(): HvigorPlugin {
    return {
        pluginId: 'customPlugin',
        async apply(currentNode: HvigorNode): Promise<void> {
            const rootNodeContext = currentNode.getContext(OhosPluginId.OHOS\_APP\_PLUGIN);
            if (!rootNodeContext) {
                return;
            }
            const ohpmInfo = rootNodeContext.getOhpmDependencyInfo();
            console.log(ohpmInfo)
        }
    };
}

export default {
    system: appTasks,  /\* Built-in plugin of Hvigor. It cannot be modified. \*/
    plugins:\[customPlugin()\]         /\* Custom plugin to extend the functionality of Hvigor. \*/
}

## getOhpmRemoteHspDependencyInfo

getOhpmRemoteHspDependencyInfo: (isSigned: boolean) => Record<string, OhpmDependencyInfo> | object

Obtains the HSP dependency information configured in the project-level **oh-package.json5** file.

**Since**: Hvigor 5.6.2

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

signed

 | 

boolean

 | 

No

 | 

Whether to obtain the paths of the signed HSPs. The default value is **false**.

 |

**Return value**

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

Record<string, OhpmDependencyInfo> | object

 | 

HSP dependency information configured in the project-level **oh-package.json5** file.

 |

**Sample code**

// Project-level hvigorfile.ts file
import { hvigor, HvigorNode, HvigorPlugin } from '@ohos/hvigor';
import { appTasks, OhosHapContext, OhosAppContext, OhosPluginId, Target } from '@ohos/hvigor-ohos-plugin';
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
                hapTask(currentNode);
            });
        }
    };
}
function hapTask(currentNode: HvigorNode) {
   // Obtain subnode information after all nodes are loaded.
    currentNode.subNodes((node: HvigorNode) => {
                    // Obtain the context information of the HAP module.
        const hapContext = node.getContext(OhosPluginId.OHOS\_HAP\_PLUGIN) as OhosHapContext;
        const moduleName = hapContext?.getModuleName();
        hapContext?.targets((target: Target) => {
            const targetName = target.getTargetName();
            node.registerTask({
                // Task name.
                name: \`${targetName}@getRemoteHspInfo\`,
                // Function that defines the task logic.
                run() {
                    const rootNodeContext = currentNode.getContext(OhosPluginId.OHOS\_APP\_PLUGIN) as OhosAppContext;
                    if (!rootNodeContext) {
                        return;
                    }
                    // Obtain the information about the unsigned remote HSPs.
                    const remoteHspInfo = rootNodeContext.getOhpmRemoteHspDependencyInfo(false);
                    console.log(remoteHspInfo)
                    // Obtain the information about the signed remote HSPs.
                    const signedRemoteHspInfo = rootNodeContext.getOhpmRemoteHspDependencyInfo(true);
                    console.log(signedRemoteHspInfo)
                },
                // Configure the dependencies for this task.
                dependencies: \[\`${targetName}@PackageHap\`\],
                // Configure the dependencies for the next task.
                postDependencies: \['assembleHap'\]
            });
        });
    });
}
export default {
    system: appTasks,  /\* Built-in plugin of Hvigor. It cannot be modified. \*/
    plugins:\[customPlugin()\]         /\* Custom plugin to extend the functionality of Hvigor. \*/
};

## getDependenciesOpt

getDependenciesOpt: () => any

Obtains the dependencies configured in the project-level **oh-package.json5** file.

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

Dependencies configured in the project-level **oh-package.json5** file.

 |

**Sample code**

// Project-level hvigorfile.ts file
import { HvigorNode, HvigorPlugin } from '@ohos/hvigor';
import { appTasks } from '@ohos/hvigor-ohos-plugin';
import { OhosPluginId } from '@ohos/hvigor-ohos-plugin';

// Custom plug-in code
export function customPlugin(): HvigorPlugin {
    return {
        pluginId: 'customPlugin',
        async apply(currentNode: HvigorNode): Promise<void> {
            const rootNodeContext = currentNode.getContext(OhosPluginId.OHOS\_APP\_PLUGIN);
            if (!rootNodeContext) {
                return;
            }
            const DependenciesInfo = rootNodeContext.getDependenciesOpt();
            console.log(DependenciesInfo)
        }
    };
}

export default {
    system: appTasks,  /\* Built-in plugin of Hvigor. It cannot be modified. \*/
    plugins:\[customPlugin()\]         /\* Custom plugin to extend the functionality of Hvigor. \*/
}

## setDependenciesOpt

setDependenciesOpt: (dependencies: any) => void

Sets the dependencies in the project-level **oh-package.json5** file. Ensure that the **dependencies** field exists in the **oh-package.json5** file.

**Since**: Hvigor 5.0.10

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

dependencies

 | 

any

 | 

Yes

 | 

Dependencies in **oh-package.json5** of the current project.

 |

**Sample code**

// Project-level hvigorfile.ts file
import { HvigorNode, HvigorPlugin } from '@ohos/hvigor';
import { appTasks } from '@ohos/hvigor-ohos-plugin';
import { OhosPluginId } from '@ohos/hvigor-ohos-plugin';

// Custom plug-in code
export function customPlugin(): HvigorPlugin {
    return {
        pluginId: 'customPlugin',
        async apply(currentNode: HvigorNode): Promise<void> {
            const rootNodeContext = currentNode.getContext(OhosPluginId.OHOS\_APP\_PLUGIN);
            if (!rootNodeContext) {
                return;
            }
            const dependenciesInfo = rootNodeContext.getDependenciesOpt()
            dependenciesInfo\["har"\] = "./har";  // Ensure that the dependencies exist.
            rootNodeContext.setDependenciesOpt(dependenciesInfo);   
      }
    };
}

export default {
    system: appTasks,  /\* Built-in plugin of Hvigor. It cannot be modified. \*/
    plugins:\[customPlugin()\]         /\* Custom plugin to extend the functionality of Hvigor. \*/
}

## getDevDependenciesOpt

getDevDependenciesOpt: () => any

Obtains the development dependencies in the project-level **oh-package.json5** file.

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

Development dependency information configured in the project-level **oh-package.json5** file.

 |

**Sample code**

// Project-level hvigorfile.ts file
import { HvigorNode, HvigorPlugin } from '@ohos/hvigor';
import { appTasks } from '@ohos/hvigor-ohos-plugin';
import { OhosPluginId } from '@ohos/hvigor-ohos-plugin';

// Custom plug-in code
export function customPlugin(): HvigorPlugin {
    return {
        pluginId: 'customPlugin',
        async apply(currentNode: HvigorNode): Promise<void> {
            const rootNodeContext = currentNode.getContext(OhosPluginId.OHOS\_APP\_PLUGIN);
            if (!rootNodeContext) {
                return;
            }
            const devDependenciesInfo = rootNodeContext.getDevDependenciesOpt();
            console.log(devDependenciesInfo)
        }
    };
}

export default {
    system: appTasks,  /\* Built-in plugin of Hvigor. It cannot be modified. \*/
    plugins:\[customPlugin()\]         /\* Custom plugin to extend the functionality of Hvigor. \*/
}

## setDevDependenciesOpt

setDevDependenciesOpt: (devDependencies: any) => void

Sets the development dependencies in the project-level **oh-package.json5** file. Ensure that the **devDependencies** field exists in the **oh-package.json5** file.

**Since**: Hvigor 5.0.10

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

devDependencies

 | 

any

 | 

Yes

 | 

Development dependency information in **oh-package.json5** of the current project.

 |

**Sample code**

// Project-level hvigorfile.ts file
import { HvigorNode, HvigorPlugin } from '@ohos/hvigor';
import { appTasks } from '@ohos/hvigor-ohos-plugin';
import { OhosPluginId } from '@ohos/hvigor-ohos-plugin';

// Custom plug-in code
export function customPlugin(): HvigorPlugin {
    return {
        pluginId: 'customPlugin',
        async apply(currentNode: HvigorNode): Promise<void> {
            const rootNodeContext = currentNode.getContext(OhosPluginId.OHOS\_APP\_PLUGIN);
            if (!rootNodeContext) {
                return;
            }
            const devDependenciesInfo = rootNodeContext.getDevDependenciesOpt()
            devDependenciesInfo\["har"\] = "./har";  // Ensure that the development dependencies exist.
            rootNodeContext.setDevDependenciesOpt(devDependenciesInfo);   
      }
    };
}

export default {
    system: appTasks,  /\* Built-in plugin of Hvigor. It cannot be modified. \*/
    plugins:\[customPlugin()\]         /\* Custom plugin to extend the functionality of Hvigor. \*/
}

## getDynamicDependenciesOpt

getDynamicDependenciesOpt: () => any

Obtains the dynamic dependencies configured in the project-level **oh-package.json5** file.

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

Dynamic dependency information configured in the project-level **oh-package.json5** file.

 |

**Sample code**

// Project-level hvigorfile.ts file
import { HvigorNode, HvigorPlugin } from '@ohos/hvigor';
import { appTasks } from '@ohos/hvigor-ohos-plugin';
import { OhosPluginId } from '@ohos/hvigor-ohos-plugin';

// Custom plug-in code
export function customPlugin(): HvigorPlugin {
    return {
        pluginId: 'customPlugin',
        async apply(currentNode: HvigorNode): Promise<void> {
            const rootNodeContext = currentNode.getContext(OhosPluginId.OHOS\_APP\_PLUGIN);
            if (!rootNodeContext) {
                return;
            }
            const dynamicDependenciesInfo = rootNodeContext.getDynamicDependenciesOpt();
            console.log(dynamicDependenciesInfo)
        }
    };
}

export default {
    system: appTasks,  /\* Built-in plugin of Hvigor. It cannot be modified. \*/
    plugins:\[customPlugin()\]         /\* Custom plugin to extend the functionality of Hvigor. \*/
}

## setDynamicDependenciesOpt

setDynamicDependenciesOpt: (dynamicDependencies: any) => void

Sets the dynamic dependencies in the project-level **oh-package.json5** file. Ensure that the **dynamicDependencies** field exists in the **oh-package.json5** file.

**Since**: Hvigor 5.0.10

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

dynamicDependencies

 | 

any

 | 

Yes

 | 

Dynamic dependency information in **oh-package.json5** of the current project.

 |

**Sample code**

// Project-level hvigorfile.ts file
import { HvigorNode, HvigorPlugin } from '@ohos/hvigor';
import { appTasks } from '@ohos/hvigor-ohos-plugin';
import { OhosPluginId } from '@ohos/hvigor-ohos-plugin';

// Custom plug-in code
export function customPlugin(): HvigorPlugin {
    return {
        pluginId: 'customPlugin',
        async apply(currentNode: HvigorNode): Promise<void> {
            const rootNodeContext = currentNode.getContext(OhosPluginId.OHOS\_APP\_PLUGIN);
            if (!rootNodeContext) {
                return;
            }
            const dynamicDependenciesInfo = rootNodeContext.getDynamicDependenciesOpt()
            dynamicDependenciesInfo\["har"\] = "./har";  // Ensure that the dynamic dependencies exist.
            rootNodeContext.setDynamicDependenciesOpt(dynamicDependenciesInfo);   
      }
    };
}

export default {
    system: appTasks,  /\* Built-in plugin of Hvigor. It cannot be modified. \*/
    plugins:\[customPlugin()\]         /\* Custom plugin to extend the functionality of Hvigor. \*/
}

## getOverrides

getOverrides: () => any

Obtains the **overrides** settings configured in the project-level **oh-package.json5** file.

**Since**: Hvigor 5.10.3

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

**overrides** settings configured in the project-level **oh-package.json5** file.

 |

**Sample code**

// Project-level hvigorfile.ts file
import { appTasks } from '@ohos/hvigor-ohos-plugin';
import {OhosAppContext, OhosPluginId } from '@ohos/hvigor-ohos-plugin';
import { hvigor } from '@ohos/hvigor';
hvigor.afterNodeEvaluate(node => {
  const appContext = node.getContext(OhosPluginId.OHOS\_APP\_PLUGIN) as OhosAppContext;
  if (appContext) {
    let dependency = appContext.getOverrides() ?? {};
    console.log(dependency)
  }
});
export default {
    system: appTasks,  /\* Built-in plugin of Hvigor. It cannot be modified. \*/
    plugins:\[\]         /\* Custom plugin to extend the functionality of Hvigor. \*/
}

## setOverrides

setOverrides: (overrides: any) => void

Sets the **overrides** field in the project-level **oh-package.json5** file.

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

overrides

 | 

any

 | 

Yes

 | 

**overrides** field to set in the project-level **oh-package.json5** file.

 |

**Sample code**

// Project-level hvigorfile.ts file
import { appTasks } from '@ohos/hvigor-ohos-plugin';
import {OhosAppContext, OhosHapContext, OhosPluginId} from '@ohos/hvigor-ohos-plugin';
import { hvigor } from '@ohos/hvigor';
hvigor.afterNodeEvaluate(node => {
  const appContext = node.getContext(OhosPluginId.OHOS\_APP\_PLUGIN) as OhosAppContext;
  if (appContext) {
    let dependency = appContext.getOverrides() ?? {};
    dependency\['library'\] = 'file:./library.har'; // Dynamically add a dependency on an internal HAR within your project in the project-level oh-package.json5 file.
    appContext.setOverrides(dependency);
    return;
  }
  const hapContext = node.getContext(OhosPluginId.OHOS\_HAP\_PLUGIN) as OhosHapContext;
  if (hapContext) {
    const dependency = hapContext.getDependenciesOpt();
    dependency\['library'\] = 'file:./../library';    // Dynamically add a dependency on an internal module in the project to the entry module.
    hapContext.setDependenciesOpt(dependency);
  }
});
export default {
    system: appTasks,  /\* Built-in plugin of Hvigor. It cannot be modified. \*/
    plugins:\[\]         /\* Custom plugin to extend the functionality of Hvigor. \*/
}

## getSdkDetails

getSdkDetails: () => SdkDetails

Obtains SDK information.

**Since**: Hvigor 6.0.4

**Return value**

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

[SdkDetails](../basic-build-capability/document.md#section1463642114714)

 | 

SDK information.

 |

**Sample code**

// Project-level hvigorfile.ts file
import { appTasks } from '@ohos/hvigor-ohos-plugin';
import { OhosAppContext, OhosPluginId } from '@ohos/hvigor-ohos-plugin';
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
          let sdk = appContext.getSdkDetails();
          console.log(sdk?.getSdkDir())
          console.log(sdk?.isOhos())
          console.log(sdk?.getSdkVersion())
          console.log(sdk?.getEtsComponentVersion())
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

#### OhosHapContext

Context API provided by the HAP module plug-in. To obtain this API in the hvigor node of a HAP module, you can use the **getContext** method to pass **OhosPluginId.OHOS\_HAP\_PLUGIN\_ID**. The API mainly contains the module and target information of the HAP module.

## Modules to Import

import { OhosHapContext } from '@ohos/hvigor-ohos-plugin';

## getModuleName

getModuleName: () => string

Obtains the module name.

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

Module name.

 |

**Sample code**

// Project-level hvigorfile.ts file
import { appTasks, OhosHapContext, OhosPluginId } from '@ohos/hvigor-ohos-plugin';
import { hvigor, HvigorNode } from '@ohos/hvigor';

hvigor.nodesEvaluated(() => {
    const rootNode = hvigor.getRootNode();
    rootNode.subNodes((node: HvigorNode) => {
        // Obtain all subnodes.
        const hapContext = node.getContext(OhosPluginId.OHOS\_HAP\_PLUGIN) as OhosHapContext;
        const moduleName = hapContext?.getModuleName();
        console.log(\`Module Name: ${moduleName}\`);
    });
})

export default {
    system: appTasks,  /\* Built-in plugin of Hvigor. It cannot be modified. \*/
    plugins:\[\]         /\* Custom plugin to extend the functionality of Hvigor. \*/
}

## getModulePath

getModulePath: () => string

Obtains the module path.

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

Module path.

 |

**Sample code**

// Project-level hvigorfile.ts file
import { appTasks, OhosHapContext, OhosPluginId } from '@ohos/hvigor-ohos-plugin';
import { hvigor, HvigorNode } from '@ohos/hvigor';

hvigor.nodesEvaluated(() => {
    const rootNode = hvigor.getRootNode();
    rootNode.subNodes((node: HvigorNode) => {
        // Obtain all subnodes.
        const hapContext = node.getContext(OhosPluginId.OHOS\_HAP\_PLUGIN) as OhosHapContext;
        const modulePath = hapContext?.getModulePath();
        console.log(\`Module Path: ${modulePath}\`);
    });
})

export default {
    system: appTasks,  /\* Built-in plugin of Hvigor. It cannot be modified. \*/
    plugins:\[\]         /\* Custom plugin to extend the functionality of Hvigor. \*/
}

## getModuleType

getModuleType: () => string

Obtains the module type. The return value is obtained from the **type** field in the **module.json5** configuration file.

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

Module type.

 |

**Sample code**

// Project-level hvigorfile.ts file
import { appTasks, OhosHapContext, OhosPluginId } from '@ohos/hvigor-ohos-plugin';
import { hvigor, HvigorNode } from '@ohos/hvigor';

hvigor.nodesEvaluated(() => {
    const rootNode = hvigor.getRootNode();
    rootNode.subNodes((node: HvigorNode) => {
        // Obtain all subnodes.
        const hapContext = node.getContext(OhosPluginId.OHOS\_HAP\_PLUGIN) as OhosHapContext;
        const moduleType = hapContext?.getModuleType();
        console.log(\`Module Type: ${moduleType}\`);
    });
})

export default {
    system: appTasks,  /\* Built-in plugin of Hvigor. It cannot be modified. \*/
    plugins:\[\]         /\* Custom plugin to extend the functionality of Hvigor. \*/
}

## getBuildProductRootPath

getBuildProductRootPath: () => string

Obtains the root path of the module based on the product build.

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

Root path of the module based on the product build.

 |

**Sample code**

// Project-level hvigorfile.ts file
import { appTasks, OhosHapContext, OhosPluginId } from '@ohos/hvigor-ohos-plugin';
import { hvigor, HvigorNode } from '@ohos/hvigor';

hvigor.nodesEvaluated(() => {
    const rootNode = hvigor.getRootNode();
    rootNode.subNodes((node: HvigorNode) => {
        // Obtain all subnodes.
        const hapContext = node.getContext(OhosPluginId.OHOS\_HAP\_PLUGIN) as OhosHapContext;
        const buildProductRootPath = hapContext?.getBuildProductRootPath();
        console.log(\`Build Product Root Path: ${buildProductRootPath}\`);
    });
})

export default {
    system: appTasks,  /\* Built-in plugin of Hvigor. It cannot be modified. \*/
    plugins:\[\]         /\* Custom plugin to extend the functionality of Hvigor. \*/
}

## targets

targets: (callbackfn: (target: Target) => void) => void

Represents the callback method of the target object to be constructed.

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

callback

 | 

(target: [Target](../basic-build-capability/document.md#section12392182963714)) => void

 | 

Yes

 | 

The passed parameter is of the **Target** type, and the return value is a void function.

 |

**Sample code**

// Project-level hvigorfile.ts file
import { appTasks, OhosHapContext, OhosPluginId, Target } from '@ohos/hvigor-ohos-plugin';
import { hvigor, HvigorNode } from '@ohos/hvigor';

hvigor.nodesEvaluated(() => {
    const rootNode = hvigor.getRootNode();
    rootNode.subNodes((node: HvigorNode) => {
        // Obtain all subnodes.
        const hapContext = node.getContext(OhosPluginId.OHOS\_HAP\_PLUGIN) as OhosHapContext;
        hapContext?.targets((target: Target) => {
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

## getBuildMode

getBuildMode: () => string

Obtains the **BuildMode** specified by the current build.

**Since**: Hvigor 5.18.4

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

**BuildMode** specified by the current build.

 |

**Sample code**

// Project-level hvigorfile.ts file
import { appTasks, OhosHapContext, OhosPluginId } from '@ohos/hvigor-ohos-plugin';
import { hvigor, HvigorNode } from '@ohos/hvigor';

hvigor.nodesEvaluated(() => {
    const rootNode = hvigor.getRootNode();
    rootNode.subNodes((node: HvigorNode) => {
        // Obtain all subnodes.
        const hapContext = node.getContext(OhosPluginId.OHOS\_HAP\_PLUGIN) as OhosHapContext;
        const buildMode = hapContext?.getBuildMode();
        console.log(\`Build Mode: ${buildMode}\`);
    });
})

export default {
    system: appTasks,  /\* Built-in plugin of Hvigor. It cannot be modified. \*/
    plugins:\[\]         /\* Custom plugin to extend the functionality of Hvigor. \*/
}

## getModuleJsonOpt

getModuleJsonOpt: () => any

Obtains the object from the **module.json5** file of this module.

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

Object obtained from the **module.json5** file of the current module.

 |

**Sample code**

// Project-level hvigorfile.ts file
import { appTasks, OhosHapContext, OhosPluginId } from '@ohos/hvigor-ohos-plugin';
import { hvigor, HvigorNode } from '@ohos/hvigor';

hvigor.nodesEvaluated(() => {
    const rootNode = hvigor.getRootNode();
    rootNode.subNodes((node: HvigorNode) => {
        // Obtain all subnodes.
        const hapContext = node.getContext(OhosPluginId.OHOS\_HAP\_PLUGIN) as OhosHapContext;
        const moduleJsonOpt = hapContext?.getModuleJsonOpt();
        console.log(\`Module Json Opt: ${JSON.stringify(moduleJsonOpt)}\`);
    });
})

export default {
    system: appTasks,  /\* Built-in plugin of Hvigor. It cannot be modified. \*/
    plugins:\[\]         /\* Custom plugin to extend the functionality of Hvigor. \*/
}

## setModuleJsonOpt

setModuleJsonOpt: (moduleJsonOpt: any) => void

Sets the object in the **module.json5** file of this module.

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

moduleJsonOpt

 | 

any

 | 

Yes

 | 

Object parsed from the **module.json5** file of the current module.

 |

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c4/v3/oaw217FfSoi_zZHC25znzg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062156Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=CF59514524A1362D3F36739E80D758A61A3678C72FD2BA343D852AB63ED206D1)

The **setModuleJsonOpt** API performs schema validation; if the passed object does not conform to the validation rules, it will throw an exception.

**Sample code**

// Project-level hvigorfile.ts file
import { appTasks, OhosHapContext, OhosPluginId } from '@ohos/hvigor-ohos-plugin';
import { hvigor, HvigorNode } from '@ohos/hvigor';

hvigor.nodesEvaluated(() => {
    const rootNode = hvigor.getRootNode();
    rootNode.subNodes((node: HvigorNode) => {
        // Obtain all subnodes.
        const hapContext = node.getContext(OhosPluginId.OHOS\_HAP\_PLUGIN) as OhosHapContext;
        const moduleJsonOpt = hapContext?.getModuleJsonOpt();
        moduleJsonOpt.module.deviceTypes = \["phone", "tablet"\]; // Modify the deviceTypes field in module.json.
        hapContext?.setModuleJsonOpt(moduleJsonOpt); // Update module.json.
        console.log(\`Module Json Opt: ${JSON.stringify(moduleJsonOpt)}\`);
    });
})

export default {
    system: appTasks,  /\* Built-in plugin of Hvigor. It cannot be modified. \*/
    plugins:\[\]         /\* Custom plugin to extend the functionality of Hvigor. \*/
}

## getBuildProfileOpt

getBuildProfileOpt: () => any

Obtains the object from the **build-profile.json5** file of this module.

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

Object obtained from the **build-profile.json5** file of the current module.

 |

**Sample code**

// Project-level hvigorfile.ts file
import { appTasks, OhosHapContext, OhosPluginId } from '@ohos/hvigor-ohos-plugin';
import { hvigor, HvigorNode } from '@ohos/hvigor';

hvigor.nodesEvaluated(() => {
    const rootNode = hvigor.getRootNode();
    rootNode.subNodes((node: HvigorNode) => {
        // Obtain all subnodes.
        const hapContext = node.getContext(OhosPluginId.OHOS\_HAP\_PLUGIN) as OhosHapContext;
        const buildProfileOpt = hapContext?.getBuildProfileOpt();
        console.log(\`Build Profile Opt: ${JSON.stringify(buildProfileOpt)}\`);
    });
})

export default {
    system: appTasks,  /\* Built-in plugin of Hvigor. It cannot be modified. \*/
    plugins:\[\]         /\* Custom plugin to extend the functionality of Hvigor. \*/
}

## setBuildProfileOpt

setBuildProfileOpt: (buildProfileOpt: any) => void

Sets the object in the **build-profile.json5** file of this module.

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

buildProfileOpt

 | 

any

 | 

Yes

 | 

Object from the **build-profile.json5** file of the current module.

 |

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/54/v3/nHZJwY-WQKq6I3WeiMVqIQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062156Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=0FFA86861F362749FB509610BF04BCB7B786F94B0566B3CA231A5EC9273693A5)

The **setBuildProfileOpt** API performs schema validation; if the passed object does not conform to the validation rules, it will throw an exception.

**Sample code**

// Project-level hvigorfile.ts file
import { appTasks, OhosHapContext, OhosPluginId } from '@ohos/hvigor-ohos-plugin';
import { hvigor, HvigorNode } from '@ohos/hvigor';

hvigor.nodesEvaluated(() => {
    const rootNode = hvigor.getRootNode();
    rootNode.subNodes((node: HvigorNode) => {
        // Obtain all subnodes.
        const hapContext = node.getContext(OhosPluginId.OHOS\_HAP\_PLUGIN) as OhosHapContext;
        const buildProfileOpt = hapContext?.getBuildProfileOpt();
        // Modify buildProfileOpt.
        buildProfileOpt?.targets?.push({
            "name": "default1",
        })
        hapContext?.setBuildProfileOpt(buildProfileOpt); // Update buildProfileOpt.
        console.log(\`Build Profile Opt: ${JSON.stringify(buildProfileOpt)}\`);
    });
})

export default {
    system: appTasks,  /\* Built-in plugin of Hvigor. It cannot be modified. \*/
    plugins:\[\]         /\* Custom plugin to extend the functionality of Hvigor. \*/
}

## getVersion

getVersion: () => string

Obtains the version number configured in the **oh-package.json5** file.

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

Version number configured in the **oh-package.json5** file.

 |

**Sample code**

// Project-level hvigorfile.ts file
import { appTasks, OhosHapContext } from '@ohos/hvigor-ohos-plugin';
import { hvigor, HvigorNode, HvigorPlugin } from '@ohos/hvigor';
import { OhosPluginId } from '@ohos/hvigor-ohos-plugin';

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
                currentNode.subNodes((node: HvigorNode) => {
                    // Obtain the context information of the HAP module.
                    // For HARs or HSPs, use OHOS\_HAR\_PLUGIN/OHOS\_HSP\_PLUGIN.
                    const hapNodeContext = node.getContext(OhosPluginId.OHOS\_HAP\_PLUGIN) as OhosHapContext;
                    if (!hapNodeContext) {
                        return;
                    }
                    const moduleVersion = hapNodeContext.getVersion();
                    console.log(moduleVersion);
                });
            });
        }
    };
}
export default {
    system: appTasks,  /\* Built-in plugin of Hvigor. It cannot be modified. \*/
    plugins:\[customPlugin()\]         /\* Custom plugin to extend the functionality of Hvigor. \*/
}

## setVersion

setVersion: (version: string) => void

Sets the version number in the **oh-package.json5** file.

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

version

 | 

string

 | 

Yes

 | 

Version number in the **oh-package.json5** file.

 |

**Sample code**

// Project-level hvigorfile.ts file
import { appTasks, OhosHapContext } from '@ohos/hvigor-ohos-plugin';
import { hvigor, HvigorNode, HvigorPlugin } from '@ohos/hvigor';
import { OhosPluginId } from '@ohos/hvigor-ohos-plugin';

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
                currentNode.subNodes((node: HvigorNode) => {
                    // Obtain the context information of the HAP module.
                    // For HARs or HSPs, use OHOS\_HAR\_PLUGIN/OHOS\_HSP\_PLUGIN.
                    const hapNodeContext = node.getContext(OhosPluginId.OHOS\_HAP\_PLUGIN) as OhosHapContext;
                    if (!hapNodeContext) {
                        return;
                    }
                    hapNodeContext.setVersion('2.0.0');
                    const moduleVersion = hapNodeContext.getVersion();
                    console.log(moduleVersion);
                });
            });
        }
    };
}
export default {
    system: appTasks,  /\* Built-in plugin of Hvigor. It cannot be modified. \*/
    plugins:\[customPlugin()\]         /\* Custom plugin to extend the functionality of Hvigor. \*/
}

## getOhpmDependencyInfo

getOhpmDependencyInfo: () => Record<string, OhpmDependencyInfo> | object

Obtains the dependency information configured in the module-level **oh-package.json5** file.

**Since**: Hvigor 5.0.0

**Return value**

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

Record<string, OhpmDependencyInfo> | object

 | 

Dependency information configured in **oh-package.json5**.

 |

**Sample code**

// Project-level hvigorfile.ts file
import { appTasks, OhosHapContext } from '@ohos/hvigor-ohos-plugin';
import { hvigor, HvigorNode, HvigorPlugin } from '@ohos/hvigor';
import { OhosPluginId } from '@ohos/hvigor-ohos-plugin';

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
                currentNode.subNodes((node: HvigorNode) => {
                    // Obtain the context information of the HAP module.
                    const hapNodeContext = node.getContext(OhosPluginId.OHOS\_HAP\_PLUGIN) as OhosHapContext;
                    if (!hapNodeContext) {
                        return;
                    }
                    const ohpmInfo = hapNodeContext.getOhpmDependencyInfo();
                    console.log(ohpmInfo)

                });
            });
        }
    };
}

export default {
    system: appTasks,  /\* Built-in plugin of Hvigor. It cannot be modified. \*/
    plugins:\[customPlugin()\]         /\* Custom plugin to extend the functionality of Hvigor. \*/
}

## getOhpmRemoteHspDependencyInfo

getOhpmRemoteHspDependencyInfo: (isSigned: boolean) => Record<string, OhpmDependencyInfo> | object

Obtains the HSP dependency information configured in the module-level **oh-package.json5** file.

**Since**: Hvigor 5.6.2

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

isSigned

 | 

boolean

 | 

No

 | 

Whether to obtain the paths of the signed HSPs. The default value is **false**.

 |

**Return value**

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

Record<string, OhpmDependencyInfo> | object

 | 

HSP dependency information configured in the module-level **oh-package.json5** file.

 |

**Sample code**

// Project-level hvigorfile.ts file
import { appTasks, OhosHapContext, Target } from '@ohos/hvigor-ohos-plugin';
import { hvigor, HvigorNode, HvigorPlugin } from '@ohos/hvigor';
import { OhosPluginId } from '@ohos/hvigor-ohos-plugin';
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
                currentNode.subNodes((node: HvigorNode) => {
                    // Obtain the context information of the HAP module.
                    const hapNodeContext = node.getContext(OhosPluginId.OHOS\_HAP\_PLUGIN) as OhosHapContext;
                    hapNodeContext?.targets((target: Target) => {
                        const targetName = target.getTargetName();
                        node.registerTask({
                // Task name.
                            name: \`${targetName}@getRemoteHspInfo\`,
                // Function that defines the task logic.
                            run() {
                                // Obtain the information about the unsigned remote HSPs.
                                const remoteHspInfo = hapNodeContext.getOhpmRemoteHspDependencyInfo(false);
                                console.log(remoteHspInfo);
                                // Obtain the information about the unsigned remote HSPs.
                                const signedRemoteHspInfo = hapNodeContext.getOhpmRemoteHspDependencyInfo(true);
                                console.log(signedRemoteHspInfo);
                            },
                // Configure the dependencies for this task.
                            dependencies: \[\`${targetName}@PackageHap\`\],
                // Configure the dependencies for the next task.
                            postDependencies: \['assembleHap'\]
                        });
                    });
                });
            });
        }
    };
}
export default {
    system: appTasks,  /\* Built-in plugin of Hvigor. It cannot be modified. \*/
    plugins:\[customPlugin()\]         /\* Custom plugin to extend the functionality of Hvigor. \*/
}

## getDependenciesOpt

Works in the same way as [getDependenciesOpt](#section1085223315215) in **OhosAppContext**.

## setDependenciesOpt

Works in the same way as [setDependenciesOpt](#section18789410129) in **OhosAppContext**.

## getDevDependenciesOpt

Works in the same way as [getDevDependenciesOpt](#section192992531393) in **OhosAppContext**.

## setDevDependenciesOpt

Works in the same way as [setDevDependenciesOpt](#section8534132541914) in **OhosAppContext**.

## getDynamicDependenciesOpt

Works in the same way as [getDynamicDependenciesOpt](#section3891011201117) in **OhosAppContext**.

## setDynamicDependenciesOpt

Works in the same way as [setDynamicDependenciesOpt](#section2756613192210) in **OhosAppContext**.

#### OhosHspContext

Represents the HSP module context, which is consistent with **OhosHapContext**.

#### OhosHarContext

Represents the HAR module context, which is consistent with **OhosHapContext**.
