# How do I write the compilation script of the HAR file?

Write the following code in the **hvigorfile.ts** file in the **entry** directory:

import { harTasks } from '@ohos/hvigor-ohos-plugin';

function harTask(): HvigorPlugin {
    return {
        pluginId: 'harTask',
        apply(node: HvigorNode) {
            console.log('hello harTasks!');
        }
    }
}

export default {
    system: harTasks,
    plugins: \[harTask()\]
}
