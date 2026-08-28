# How do I pass parameters using the command lines and obtain them using the extension plugin of Hvigor during compiling?

Use the **hvigor** command:

 > hvigorw -s -p key1=value2222

To obtain the passed parameters, refer to the following sample code snippet:

// hvigorfile.ts
import { harTasks } from '@ohos/hvigor-ohos-plugin';
import { hvigor } from '@ohos/hvigor';

export default {
    system: harTasks,  /\* Built-in plugin of Hvigor. It cannot be modified. \*/
    plugins:\[\]         /\* Custom plugin to extend the functionality of Hvigor. \*/
}
console.log('value===', hvigor.getParameter().getExtParam('key1'));
