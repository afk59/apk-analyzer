# Examples

#### (Recommended) Using Hooks and Plug-in Context to Implement Dynamic Configuration

## Modifying build-profile.json5 Configuration for Individual hvigorNode

The following example demonstrates how to register a hook for a single node and

update the signing information in the **build-profile.json5** file in the root directory by adding the following content to the **hvigorfile.ts** file in the project root directory:

import { appTasks, OhosAppContext, OhosPluginId } from '@ohos/hvigor-ohos-plugin';
import { hvigor,getNode } from '@ohos/hvigor'

// Obtain the root node.
const rootNode = getNode(\_\_filename);
// Add an afterNodeEvaluate hook to the root node, modify the build-profile.json5 file in the root directory, and enable the hook.
rootNode.afterNodeEvaluate(node => {
    // Obtain the context object of the app plug-in.
    const appContext = node.getContext(OhosPluginId.OHOS\_APP\_PLUGIN) as OhosAppContext;
    // Obtain the obj object read from the build-profile.json5 file through the context object.
    const buildProfileOpt = appContext.getBuildProfileOpt();
    // Modify the obj object as required. In this example, signingConfigs in app is updated.
    buildProfileOpt\['app'\]\['signingConfigs'\] = \[
        {
            "name": "default",
            "type": "HarmonyOS",
            "material": {
                "certpath": "D:\\\\SigningConfig\\\\debug\_hos.cer",
                "storePassword": "\*\*\*\*\*\*",
                "keyAlias": "debugKey",
                "keyPassword": "\*\*\*\*\*\*",
                "profile": "D:\\\\SigningConfig\\\\debug\_hos.p7b",
                "signAlg": "SHA256withECDSA",
                "storeFile": "D:\\\\SigningConfig\\\\debug\_hos.p12"
            }
        }
    \];
    // Set the obj object back to the context object to apply the changes to the build process and results.
    appContext.setBuildProfileOpt(buildProfileOpt);
})
export default {
    system: appTasks,  /\* Built-in plug-in of hvigor. It cannot be modified. \*/
    plugins:\[\]         /\* Custom plug-in to extend the functionality of hvigor. \*/
}

## Modifying module.json5 Configuration

You can use the hook capability of the **hvigor** object to quickly create hooks for all nodes. The following is an example of creating a hook for a single node, **entry**, and modifying its **module.json5** configuration.

Add the following content to the **hvigorfile.ts** file of the **entry** module:

import { hapTasks, OhosHapContext, OhosPluginId } from '@ohos/hvigor-ohos-plugin';
import { getNode } from '@ohos/hvigor'

const entryNode = getNode(\_\_filename);
// Add an afterNodeEvaluate hook for the node, modify the content of module.json5 in the hook, and enable it.
entryNode.afterNodeEvaluate(node => {
    // Obtain the context object of the plug-in used by this node, which is the HAP plug-in context in this case.
    const hapContext = node.getContext(OhosPluginId.OHOS\_HAP\_PLUGIN) as OhosHapContext;
    // Obtain the obj object read from the module.json5 file through the context object.
    const moduleJsonOpt = hapContext.getModuleJsonOpt();
    // Modify the obj object as required. In this example, deviceTypes in module is updated.
    moduleJsonOpt\['module'\]\['deviceTypes'\] = \["phone", "tablet", "2in1", "car"\];
    // Set the obj object back to the context object to apply the changes to the build process and results.
    hapContext.setModuleJsonOpt(moduleJsonOpt);
})
export default {
    system: hapTasks,  /\* Built-in plugin of Hvigor. It cannot be modified. \*/
    plugins:\[\]         /\* Custom plug-in to extend the functionality of hvigor. \*/
}

## Modifying app.json5 Configuration

Add the following content to the **hvigorfile.ts** file in the project root directory:

import { appTasks, OhosAppContext, OhosPluginId } from '@ohos/hvigor-ohos-plugin';
import { hvigor } from '@ohos/hvigor'

// Add an afterNodeEvaluate hook for the root node, modify the content of app.json5 in the hook, and enable it.
hvigor.getRootNode().afterNodeEvaluate(rootNode => {
    // Obtain the context object of the app plug-in.
    const appContext = rootNode.getContext(OhosPluginId.OHOS\_APP\_PLUGIN) as OhosAppContext;
    // Obtain the obj object read from the app.json5 file through the context object.
    const appJsonOpt = appContext.getAppJsonOpt();
    // Modify the obj object as required. In this example, versionCode in app is updated.
    appJsonOpt\['app'\]\['versionCode'\] = 1000001;
    // Set the obj object back to the context object to apply the changes to the build process and results.
    appContext.setAppJsonOpt(appJsonOpt);
})
export default {
    system: appTasks,  /\* Built-in plug-in of hvigor. It cannot be modified. \*/
    plugins:\[\]         /\* Custom plug-in to extend the functionality of hvigor. \*/
}

## Modifying Dependencies in oh-package.json5

You can edit the project-level or module-level **hvigorfile.ts** file to modify the dependencies in the project-level or module-level **oh-package.json5** file. The following is an example:

// Project-level hvigorfile.ts
import { appTasks, OhosAppContext, OhosPluginId, Target } from '@ohos/hvigor-ohos-plugin';
import { HvigorNode, HvigorPlugin, TaskInput, TaskOutput } from '@ohos/hvigor';
export function customPlugin(): HvigorPlugin {
    return {
        pluginId: 'customPlugin',
        async apply(currentNode: HvigorNode): Promise<void> {
            const appContext = currentNode.getContext(OhosPluginId.OHOS\_APP\_PLUGIN) as OhosAppContext;
            const dependency = appContext.getDependenciesOpt();  // Obtain dependencies.
            dependency\["library"\]="file:library.har"    // Ensure that the HAR package exists.
            console.log(dependency);
            appContext.setDependenciesOpt(dependency );  // Modify dependency. Ensure that the dependencies field exists in the oh-package.json5 file.
        }
    };
}
export default {
    system: appTasks,  /\* Built-in plug-in of hvigor. It cannot be modified. \*/
    plugins:\[customPlugin()\]         /\* Custom plugin to extend the functionality of Hvigor. \*/
}

// Module-level hvigorfile.ts
import {hapTasks,OhosHapContext,OhosPluginId,Target} from '@ohos/hvigor-ohos-plugin';
import { hvigor, HvigorNode, HvigorPlugin} from '@ohos/hvigor';
import \* as fs from 'fs';
export function customPlugin(): HvigorPlugin {
    return {
        pluginId: 'customPlugin',
        async apply(currentNode: HvigorNode): Promise<void> {
            const hapContext = currentNode.getContext(OhosPluginId.OHOS\_HAP\_PLUGIN) as OhosHapContext;
            const dependency = hapContext.getDependenciesOpt();    // Obtain dependencies.
            dependency\["library"\]="file:library.har"    // Ensure that the HAR package exists.
            hapContext.setDependenciesOpt(dependency);}   // Ensure that the dependencies field exists in the oh-package.json5 file.
        }
    };
export default {
    system: hapTasks,  /\* Built-in plugin of Hvigor. It cannot be modified. \*/
    plugins:\[customPlugin()\]         /\* Custom plugin to extend the functionality of Hvigor. \*/
}

#### (Not Recommended) Configuring Signing and Version Information Using overrides

Use functions in **hvigorfile.ts** to dynamically configure the signing material, version number, and version name.

// Project-level hvigorfile.ts
import { appTasks } from '@ohos/hvigor-ohos-plugin';
export default {
    system: appTasks,  /\* Built-in plug-in of hvigor. It cannot be modified. \*/
  plugins: \[\],       /\* Custom plugin to extend the functionality of Hvigor. \*/
  config: {
    ohos: {
      overrides:{
        signingConfig: getSigningConfig(), // Signing configuration object
        appOpt: {
          versionCode: getVersionCode(),
          versionName: getVersionName(),
        } // Content in app.json
      }
    }
  }
}

function getSigningConfig() {
  return {
    type: "HarmonyOS",
    material: {
      certpath: "D:\\\\SigningConfig\\\\debug\_hos.cer",
      storePassword: "\*\*\*\*\*\*",
      keyAlias: "debugKey",
      keyPassword: "\*\*\*\*\*\*",
      profile: "D:\\\\SigningConfig\\\\debug\_hos.p7b",
      signAlg: "SHA256withECDSA",
      storeFile: "D:\\\\SigningConfig\\\\debug\_hos.p12"
    }
  }
}

function getVersionCode() {
  return 100000+new Date().getFullYear();
}

function getVersionName() {
  return \`1.0.0${new Date().getTime()}\`;
}
