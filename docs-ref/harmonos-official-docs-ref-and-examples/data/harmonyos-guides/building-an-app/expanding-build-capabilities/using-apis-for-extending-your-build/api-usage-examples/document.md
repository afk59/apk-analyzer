# API Usage Examples

Register a project-level task and a module-level task in the project-level **hvigorfile.ts** file.

// Project-level hvigorfile.ts file
import { hvigor, HvigorNode, HvigorPlugin } from '@ohos/hvigor';
import { appTasks, OhosHapContext, OhosPluginId, Target } from '@ohos/hvigor-ohos-plugin';

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
      const outputPath = target.getBuildTargetOutputPath();
      // Disable the task.
      node.getTaskByName(\`${target.getTargetName()}@SignHap\`)?.setEnable(false);
      node.registerTask({
        // Task name.
        name: \`${targetName}@onlineSignHap\`,
        // Function that defines the task logic.
        run() {
          console.log('module Task');
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
