# How do I set task priorities?

Set task priorities by referring to the code below.

import { taskpool } from '@kit.ArkTS';

@Concurrent
function printArgs(args: number): number {
  console.log("printArgs: " + args);
  return args;
}

let task: taskpool.Task = new taskpool.Task(printArgs, 100); // 100: test number
taskpool.execute(task, taskpool.Priority.HIGH).then((res) => {
  console.log("taskpool result is :" + res);
});

-   **HIGH**: The value is **0**, indicating that the task is of high priority.
-   **MEDIUM**: The value is **1**, indicating that the task is of medium priority.
-   **LOW**: The value is **2**, indicating that the task is of low priority.

**Reference**

[Priority](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-taskpool#priority)
