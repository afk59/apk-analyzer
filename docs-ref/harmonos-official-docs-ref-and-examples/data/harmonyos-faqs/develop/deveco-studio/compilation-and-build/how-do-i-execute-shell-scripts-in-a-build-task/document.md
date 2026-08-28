# How do I execute shell scripts in a build task?

Write the following code in the **hvigorfile.ts** file:

import { harTasks } from '@ohos/hvigor-ohos-plugin';
import { exec } from 'node:child\_process';
import util from 'node:util';

const scriptPath = 'xxxx.bat';

export function customPluginFunction1(str?: string) {
  return {
    pluginId: 'CustomPluginID1',
    apply(pluginContext) {
      pluginContext.registerTask({
       // Write a custom task
        name: 'customTask1',
        run: (taskContext) => {
          console.log('run into: ');
          const execPromise = util.promisify(exec)
          execPromise(scriptPath).then(res => {
            console.log(res, 'res');
          }).catch(err => {
            console.log(err, 'err');
          })
        },
        // Confirm custom task insertion position
        dependencies: \['default@BuildJS'\],
        postDependencies: \['default@CompileArkTS'\]
      })
    }
  }
}

export default {
  system: harTasks, /\* Built-in plugin of Hvigor. It cannot be modified. \*/
  plugins: \[customPluginFunction1()\] /\* Custom plugin to extend the functionality of Hvigor. \*/
}
