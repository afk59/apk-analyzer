# Developing an Hvigor Task

#### Understanding a Task

As a basic execution unit in the Hvigor build process, a task usually contains a segment of executable code, and it can depend on multiple other tasks. During task scheduling, Hvigor parses dependencies to determine the task execution sequence.

UP-TO-DATE

This task ID indicates that the task is not actually executed. Hvigor supports the incremental task skipping mechanism. If the input and output conditions of a task do not change during secondary task execution, the task is skipped to improve the build efficiency.

Example:

\> hvigor UP-TO-DATE ::PackageApp...

Finished

This task ID indicates that the task is finished.

Example:

\> hvigor Finished ::PackageApp... after 310 ms

#### Registering a Task

A task is registered using the **HvigorNode** object.

1.  Modify the **hvigorfile.ts** file in the project.
    
    // Import the module.
    import { getNode, HvigorNode, HvigorTask } from '@ohos/hvigor';
    
2.  Build service code.
    
    // Obtain the current **hvigorNode** object.
    const node: HvigorNode = getNode(\_\_filename);
    
    // Register the task.
    node.registerTask({
      name: 'customTask',
      run() {
        console.log('this is Task');
      }
    });
    
3.  Execute the task.
    
    Execute the task on the hvigor command line tool.
    
    hvigorw customTask
    
4.  View the task execution result.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/85/v3/TuQBikinTdWrk5Q_nCaRtw/en-us_image_0000002501070050.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062156Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=4CB510D0302EFBEE88C5919511FB94F9CED77B8AA1FB2B2868C7506EF3550D34 "Click to enlarge")
