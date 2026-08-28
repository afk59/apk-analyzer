# How do I add a custom task during compilation?

1.  Open the module-level **hvigorfile.ts** file.
2.  Use the **registerTask** method of **pluginContext** to register a custom task and write this task in the **run** method.
    
    import { hapTasks } from '@ohos/hvigor-ohos-plugin';
    import { getNode, HvigorNode, HvigorTask } from '@ohos/hvigor';
    
    
    const node = getNode(\_\_filename);
    node.registerTask({
        name: 'customTask',
        run() {
            console.log('this is Task');
        }});
    
3.  Enter the following code in the terminal to execute the task:
    
    ./hvigorw customTask
    

**Reference**

[Developing an Hvigor Task](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/ide-hvigor-task)
