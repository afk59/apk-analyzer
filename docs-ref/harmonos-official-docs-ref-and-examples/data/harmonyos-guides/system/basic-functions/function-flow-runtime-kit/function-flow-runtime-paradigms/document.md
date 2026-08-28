# Function Flow Runtime Paradigms

To cope with fixed task execution sequence, flexible priority-based scheduling, and complex task dependencies in actual services, Function Flow Runtime (FFRT) supports three paradigms: serial queue, concurrent queue, and task graph.

#### Serial Queue

The serial queue is often used for:

1.  **Sequential execution**: The serial queue ensures that tasks are executed one by one in sequence, avoiding data inconsistency and errors caused by out-of-order execution.
2.  **Data security**: The serial queue prevents multiple threads from competing for shared resources concurrently, ensuring data consistency and security.
3.  **Task scheduling**: The serial queue can schedule the execution sequence of complex tasks. For example, it ensures that a task begins after the previous one completes when tasks with multiple dependencies are performed.
4.  **Simplified development**: The serial queue is more simple and clear compared with manual mutex management and synchronization. You only need to add tasks to the queue for automatic system scheduling and execution, simplifying development and debugging.
5.  **Resource management**: The serial queue can limit the number of concurrent tasks and avoid resource competition and overload, optimizing system resource usage.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ab/v3/DtWh5m1gTC-EkmItOtuNMw/en-us_image_0000002568764825.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062021Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=D6DEEB53490295444BB0D14D7F1623048A0BC726EAC75BC827928BBACC1BF4F4)

For details about the development sample, see [Serial Queue (C)](../function-flow-runtime-development-samples-c/function-flow-runtime-serial-queue-c/document.md) or [Serial Queue (C++)](../function-flow-runtime-development-samples-c--00020177/function-flow-runtime-serial-queue-c/document.md).

#### Concurrent Queue

The concurrent queue is often used for:

1.  **Concurrency improvement**: The concurrent queue allows concurrent execution of multiple tasks, fully utilizing the computing capability of the multi-core processor and significantly improving the concurrency and overall performance of the system.
2.  **Efficient resource utilization**: The concurrent queue can allocate tasks to available CPU cores to optimize resource usage and reduce task waiting time and resource competition.
3.  **Flexible task scheduling**: The concurrent queue can schedule tasks based on priorities and QoS to ensure that key tasks can be executed in a timely manner and improve the system response speed.
4.  **Resource impact prevention**: The concurrent queue can set the maximum concurrency to avoid system resource impact caused by excessive concurrent tasks, ensuring system stability and performance.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d4/v3/hWxHQAukRNWv1nqRgPtjPg/en-us_image_0000002537765100.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062021Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=9F0AE372F5F263EB984DBD5DAA3BBB42512C46ACA56BDF55053364061D9F55B3)

For details about the development sample, see [Concurrent Queue (C)](../function-flow-runtime-development-samples-c/function-flow-runtime-concurrent-queue-c/document.md) or [Concurrent Queue (C++)](../function-flow-runtime-development-samples-c--00020177/function-flow-runtime-concurrent-queue-c/document.md).

#### Task Graph

The task graph is often used for:

1.  **Complex task dependency**: In actual applications, tasks have complex dependencies among each other. The task graph represents task dependencies by using directed graphs to clearly manage and schedule tasks.
2.  **Dynamic task scheduling**: The task graph can dynamically adjust task scheduling and dependencies and execution sequence according to the running conditions.
3.  **Concurrent task execution**: The task graph allows multiple independent tasks to be executed concurrently, making full use of system computing resources and improving concurrency and execution efficiency.
4.  **Structured concurrency**: The clear task lifecycles and dependencies in the task graph ensure that the creation and completion of concurrent tasks are explicit in the code structure, reducing the complexity and errors of concurrent programming.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/59/v3/52L0YuNrRN6K9s3ivugSuA/en-us_image_0000002537925040.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062021Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=48F91D54D7AE824425BE0843AC889F852C71D061D19B1DD1B3789613532BBEE7)

For details about the development sample, see [Task Graph (C)](../function-flow-runtime-development-samples-c/function-flow-runtime-task-graph-c/document.md) or [Task Graph (C++)](../function-flow-runtime-development-samples-c--00020177/function-flow-runtime-task-graph-c/document.md).

#### Job Partner

Since API version 20, FFRT supports the Job\_Partner feature. The job partner is often used for:

1.  **Multithreaded collaboration**: In many real-world applications, some functionalities must run in a specific environment, while others can run in any environment. This is when multithreaded collaboration is needed: certain functionalities run in thread A, then switch back to thread B, and finally return to thread A.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/99/v3/84KKU7bsTr-1fB3gcW0BOA/en-us_image_0000002568684817.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062021Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=DC949DE4CE58C3C95346F79B2BEF5652446DA590B344E5CB1CEECA87A00E71D1)
    
2.  **Dynamic concurrent scheduling**: In some scenarios, the number of concurrent tasks fluctuates dynamically. By adjusting the number of workers dynamically, you can maximize performance and reduce scheduling overhead.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ee/v3/swEwlqSAQLG-QZvQ1hAo6Q/en-us_image_0000002568764827.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062021Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=C53C2188AEF62772A62186F3FD57D45E3F720F129F8103C4BF3780360AF3478F)
    
    The parameters in the figure are as follows:
    
    -   job\_num: number of submitted tasks.
    -   partner\_num: number of workers.
    -   threshold: threshold for starting the worker.
    -   ratio: ratio of the number of tasks to the number of workers.
    -   max: maximum number of workers.

For details about the development example of the collaborative concurrency paradigm, see [Job Partner (C++)](../function-flow-runtime-development-samples-c--00020177/function-flow-runtime-job-partner-c/document.md).
