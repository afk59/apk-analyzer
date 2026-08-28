# Conducting an Incremental Build

Incremental build is an optimization to the task execution of Hvigor. If the input and output of a task remain unchanged between two executions, Hvigor skips executing the task.

For custom Hvigor tasks to be compatible with incremental builds, you need to specify the inputs and outputs. For details, see [Introduction](#section18840102817255).

Incremental build is enabled in Hvigor by default. You can manage the settings using the following methods:

-   Using the menu bar of DevEco Studio
    -   Choose **File** > **Settings** (**DevEco Studio** > **Preferences**/**Settings** on macOS) > **Build, Execution, Deployment** > **Build Tools** > **Hvigor** and select or deselect **Re-execute the task in incremental mode**.
-   Using commands
    -   Run the following command (replace **<task>** with the actual task name):
        
        // Enable incremental build.
        hvigorw <task> --incremental
        // Disable incremental build.
        hvigorw <task> --no-incremental
        
    -   Configure **execution.incremental** in [hvigor-config.json5](../../configuration-files/hvigor-config-json5-file/document.md).

#### Introduction

An important part of any build tool is the ability to avoid re-executing work that has already been done. In the case of a project rebuild, if a previously compiled source file has not changed in a way that affects the project input and output, then that file does not need to be recompiled. The build process itself is time-consuming, so skipping unnecessary tasks can save a significant amount of time.

Hvigor naturally supports incremental builds. If a task is marked as UP-TO-DATE in the console output, it means that an incremental build is working.

During the first build in DevEco Studio, a full build is performed, and a build cache directory is created. For subsequent rebuilds:

-   If you choose **Build** > **Clean Project** and then rebuild the project, the full build is performed.
-   If you do not choose **Build** > **Clean Project**, the incremental build is performed.

## Task Input and Output

Normally, a task generates outputs based on certain inputs. As part of incremental builds, Hvigor records the inputs and outputs of any task from the previous build and compares with those of the current build. If there are no changes, Hvigor considers the task unchanged and skips its execution. A task usually has at least one input and may not have an output. Therefore, to make incremental builds work, you should define at least one output when defining a task.

To define an incremental task, you only need to tell Hvigor which task attributes are inputs and which are outputs. If a task attribute affects the output, be sure to register it as an input; otherwise, the task may be considered up-to-date when it should not be. Conversely, if a task attribute does not affect the output, do not register it as an input; otherwise, the task may be executed unnecessarily. Also, note that non-deterministic tasks should not be configured as incremental tasks because they may generate different outputs for the same inputs, causing up-to-date checks to fail.

## How Does It Work

Before the first execution of a task, Hvigor takes a snapshot of the inputs, including the file name, path, size, last modification time, and the corresponding hash. After the task is executed, Hvigor takes a snapshot of the outputs, which also includes the file name, path, size, last modification time, and the corresponding hash. Of course, Hvigor also takes a snapshot of the task itself. Hvigor retains snapshots of the inputs and outputs for the next task execution.

Before each subsequent task execution, Hvigor takes new snapshots of the inputs and outputs. If the new snapshots are the same as the previous ones, Hvigor considers the outputs up-to-date and skips executing the task. If they are different, Hvigor executes the task, and stores the new snapshots of inputs and outputs.
