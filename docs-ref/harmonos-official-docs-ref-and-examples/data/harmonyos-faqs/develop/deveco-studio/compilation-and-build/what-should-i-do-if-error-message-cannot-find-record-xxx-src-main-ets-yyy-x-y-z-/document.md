# What should I do if "Error message:cannot find record '&XXX/src/main/ets/YYY&x.y.z', please check the request path.'ZZZ.abc'." is reported when I deploy a package for debugging?

**Symptom**

When a package is deployed on a device for debugging with DevEco Studio, a JS crash is reported, and the FaultLog window displays the following message: "Error message:cannot find record '&XXX/src/main/ets/YYY&x.y.z', please check the request path.'ZZZ.abc'.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5e/v3/Gp9y65nKTtaZryRggJUhSA/en-us_image_0000002251128405.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062621Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=E4358105B41C59580108C1442309CDE5D0694E692DDE9EDB917A1C9A804DFC2A)

**Possible Causes**

**Scenario 1**

The dependency package XXX used by the bytecode HAR (H) is not configured in **dependencies** or **dynamicDependencies** of **oh-package.json5** of the module (incorrectly configured in the project-level **oh-package.json5**). For details, see [Constraints](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/ide-hvigor-build-har#section38518561610).

**Solution**

The bytecode HAR (H) producer needs to release a new package and add the dependency on the XXX package to **oh-package.json5** of the module.

**Scenario 2**

Different versions of the XXX package are depended on in both the project-level **oh-package.json5** and module-level **oh-package.json5**. For details, see [Constraints](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/ide-hvigor-build-har#section38518561610).

**Solution**

Solution 1: Manually modify the project-level or module-level **oh-package.json5** file to ensure that the versions of the XXX package are the same.

Solution 2: Use the **overrides** field in the project-level **oh-package.json5** file to override other versions used in the module.

**Scenario 3**

After converting an HSP into a HAR, **packageType** is not deleted. As a result, the dependency is not parsed during packaging by bytecode. For details, see [How to Convert](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/hsp-to-har#how-to-convert).

**Solution**

Delete the **"packageType": "InterfaceHar"** configuration from the **oh-package.json5** file of the module by referring to step 4 in How to Convert.

**Scenario 4**

The code is modified using incompatible third-party plugins or SDKs (such as obfuscation and hardening SDKs), causing code unidentification.

**Solution**

Contact the third-party plugin or SDK provider to solve the problem, for example, upgrade the version.

**Scenario 5**

The XXX package that the application depends on is built in the [incremental build](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/ide-hvigor-incremental-build) mode, and the **version** field in the module-level **oh-package.json5** is modified. As a result, some files in the XXX package cannot be found by using the old version.

**Solution**

Solution 1: In the project corresponding to package XXX, choose **Build** > **Clean Project**, and rebuild the project.

Solution 2: Add a plugin to the project-level **hvigorfil.ts** file.

(1) Add the **plugin.ts** file to the root directory of the project.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7f/v3/Qd8QsH4HSWilFKSLpobkDA/en-us_image_0000002215928680.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062621Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=18DEAC91CCAFF6B5E60B8F1D67FB3E89D7E6AB070C570146D1BB57EC0DBC997A)

Content of the **plugin.ts** file:

import {OhosPluginId, Target} from '@ohos/hvigor-ohos-plugin';
import {hvigor, HvigorNode, HvigorPlugin} from '@ohos/hvigor';
import path from "path";
import fs from "fs";

function getLoaderJsonPath(target: Target) {
  return path.resolve(target.getBuildTargetOutputPath(), \`../../intermediates/loader/${target.getTargetName()}/loader.json\`);
}

function getPkgContextInfoPath(target: Target) {
  return path.resolve(target.getBuildTargetOutputPath(), \`../../intermediates/loader/${target.getTargetName()}/pkgContextInfo.json\`);
}

function deleteLoaderJson(target: Target) {
  const loaderJsonPath = getLoaderJsonPath(target);
  if (fs.existsSync(loaderJsonPath)) {
    fs.rmSync(loaderJsonPath);
  }
}

function deletePkgContextInfo(target: Target) {
  const pkgContextInfoPath = getPkgContextInfoPath(target);
  if (fs.existsSync(pkgContextInfoPath)) {
    fs.rmSync(pkgContextInfoPath);
  }
}

function deleteRollupCache(target: Target, buildMode: string) {
  const arkTSCompileCachePath = path.resolve(target.getBuildTargetOutputPath(),
    \`../../cache/${target.getTargetName()}/${target.getTargetName()}@HarCompileArkTS/esmodule/${buildMode}/compiler.cache\`);
  if (fs.existsSync(arkTSCompileCachePath)) {
    fs.rmSync(arkTSCompileCachePath, { recursive: true });
  }
}

function updateHapHspAbcVersion(subNode: HvigorNode, target: Target) {
  const task = subNode.getTaskByName(\`${target.getTargetName()}@GenerateLoaderJson\`);
  if (!task) {
    console.log('GenerateLoaderJson not found.');
    return;
  }
  deleteLoaderJson(target);
  deletePkgContextInfo(target);
  task.afterRun(() => {
    const pkgContextInfoPath = getPkgContextInfoPath(target);
    if (!fs.existsSync(pkgContextInfoPath)) {
      console.log('pkgContextInfo not found.');
      return;
    }
    const pkgContextInfoObj = JSON.parse(fs.readFileSync(pkgContextInfoPath).toString());
    if (!pkgContextInfoObj) {
      console.log('pkgContextInfo parse failed.');
      return;
    }
    const loaderJsonPath = getLoaderJsonPath(target);
    if (!fs.existsSync(loaderJsonPath)) {
      console.log('loaderJson not found.');
      return;
    }
    const loaderJsonObj = JSON.parse(fs.readFileSync(loaderJsonPath).toString());
    if (!loaderJsonObj) {
      console.log('loaderJson parse failed.');
      return;
    }
    for (const \[key, value\] of Object.entries(pkgContextInfoObj)) {
      if (!value?.version) {
        continue;
      }
      if (!loaderJsonObj.updateVersionInfo\[key\]) {
        loaderJsonObj.updateVersionInfo\[key\] = {};
      }
      loaderJsonObj.updateVersionInfo\[key\]\[key\] = value.version;
    }
    fs.writeFileSync(loaderJsonPath, JSON.stringify(loaderJsonObj));
  });
}

function updateHarAbcVersion(target: Target) {
  deleteLoaderJson(target);
  deleteRollupCache(target, 'debug');
  deleteRollupCache(target, 'release');
}

// The user of bytecode har can use this plugin to correctly modify the version number of ohmurl in abc when integrating bytecode har, ensuring no crashes during runtime
export function updateAbcVersionPlugin(): HvigorPlugin {
  return {
    pluginId: 'updateAbcVersionPlugin',
    apply(node: HvigorNode) {
      hvigor.nodesEvaluated(() => {
        hvigor.getRootNode().subNodes(subNode => {
          let context = subNode.getContext(OhosPluginId.OHOS\_HAP\_PLUGIN);
          if (!context) {
            context = subNode.getContext(OhosPluginId.OHOS\_HSP\_PLUGIN);
          }
          if (!context) {
            return;
          }
          context.targets(target => {
            updateHapHspAbcVersion(subNode, target);
          });
        });
      });
    }
  };
}

// The generator of bytecode har uses this plugin to incrementally build ohmurl with the correct bytecode har after modifying the version number
export function updateHarAbcVersionPlugin(): HvigorPlugin {
  return {
    pluginId: 'updateHarAbcVersionPlugin',
    apply(node: HvigorNode) {
      hvigor.nodesEvaluated(() => {
        hvigor.getRootNode().subNodes(subNode => {
          const context = subNode.getContext(OhosPluginId.OHOS\_HAR\_PLUGIN);
          if (!context) {
            return;
          }
          context.targets(target => {
            updateHarAbcVersion(target);
          });
        });
      });
    }
  };
}

(2) Add the two plugins to the project-level **hvigorfile.ts** file and click **Sync Now**.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4e/v3/WflgrDU3QM6sphT6vA4jQQ/en-us_image_0000002216088460.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062621Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=D5C9950054637B7F5ABF8E38A0C77F54DB7295E0E9DD6B87FB17C5D7C894A952)

Content of the **hvigorfile.ts** file:

import { appTasks } from '@ohos/hvigor-ohos-plugin';
import { updateAbcVersionPlugin, updateHarAbcVersionPlugin } from './plugin.ts';

export default {
    system: appTasks,  /\* Built-in plugin of Hvigor. It cannot be modified. \*/
    plugins:\[updateAbcVersionPlugin(), updateHarAbcVersionPlugin()\]         /\* Custom plugin to extend the functionality of Hvigor. \*/
}

(3) Run the following command on the terminal:

hvigorw --stop-daemon

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bc/v3/saZuZOH1Td-v4wk2FE93ng/en-us_image_0000002251048357.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062621Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=6366A1B53D6455E96E34BAA99424BF0C726DDF34B19379E4D07B695815B89606)
