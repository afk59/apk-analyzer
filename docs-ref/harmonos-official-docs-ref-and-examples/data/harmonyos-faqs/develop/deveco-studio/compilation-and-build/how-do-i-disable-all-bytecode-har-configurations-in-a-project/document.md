# How do I disable all bytecode HAR configurations in a project?

**Solution**

Solution 1: If your project contains only a few HAR modules, you can manually update the **byteCodeHar** field in each **build-profile.json5** file to **false**. For details, see [Module-level build-profile.json5 File](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/ide-hvigor-build-profile).

Solution 2: If your project contains a large number of HAR modules, manually updating each **build-profile.json5** file can be time-consuming. In this case, you can use a custom plugin to automate the process. Note that this approach takes effect at compile time, but does not change the field values in the build-profile.json5 files directly.

// Engineering-level hvigorfile.ts file
import { hvigor, HvigorNode, HvigorPlugin } from '@ohos/hvigor';
import { appTasks, OhosHarContext, OhosPluginId, Target } from '@ohos/hvigor-ohos-plugin';
// Implement custom plugins
export function customPlugin(): HvigorPlugin {
  return {
    pluginId: 'customPlugin',
    async apply(currentNode: HvigorNode): Promise<void> {
      hvigor.afterNodeEvaluate(async () => {
        // Register module-level tasks
        harTask(currentNode);
      });
    }
  };
}
function harTask(currentNode: HvigorNode) {
  currentNode.subNodes((node: HvigorNode) => {
    const context = node.getContext(OhosPluginId.OHOS\_HAR\_PLUGIN)
    context?.targets((target: Target) => {
      const targetName = target.getTargetName();
      node.registerTask({
        // Task name
        name: \`HarTask\`,
        // Main function of task execution logic
        run() {
          if (context.getBuildProfileOpt) {
            const buildProfile = context.getBuildProfileOpt();
            console.log(buildProfile)
            // Set the bytecode har config to false
            buildProfile\["buildOption"\] = { arkOptions: { byteCodeHar: false } };
            console.log(buildProfile)
            context.setBuildProfileOpt(buildProfile);
          }
        },
        // Configure the dependency of the pre-task
        dependencies: \[\`${targetName}@PackageHar\`\],
        // Post-task dependency for configuring tasks
        postDependencies: \['assembleHar'\]
      });
    });
  });
}
export default {
  system: appTasks,  /\* Built-in plugin of Hvigor. It cannot be modified. \*/
  plugins:\[customPlugin()\]  /\* Custom plugin to extend the functionality of Hvigor. \*/
}
