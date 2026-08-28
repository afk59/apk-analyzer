# Function Flow Runtime Task Graph (C)

#### Overview

The FFRT task graph supports task dependency and data dependency. Each node in the task graph indicates a task, and each edge indicates the build dependency between tasks. Task dependency is classified into input dependency (in\_deps) and output dependency (out\_deps).

You can use either of the following ways to build a task graph:

-   Use the task dependency to build a task graph. The task handle is used to indicate a task object.
-   Use the data dependency to build a task graph. The data object is abstracted as a data signature, and each data signature uniquely indicates a data object.

## Task Dependency

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cd/v3/Ui53GAJSQpWWjix-i9i_BA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062022Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=EFC1CD5A3A671DD015D454AF6AD46DE0774E556E36D9A8446476BF78F97974DB)

When a task handle appears in in\_deps, the corresponding task is the previous task. When a task handle appears in out\_deps, the corresponding task is the subsequent task.

Task dependency applies to scenarios where tasks have specific sequence or logical process requirements. For example:

-   Tasks with sequence. For example, a data preprocessing task is executed before a model training task.
-   Logic process control. For example, in a commodity transaction process, three steps need to be performed in sequence: order placement, production, and logistics transportation.
-   Multi-level chain: For example, during video processing, you can perform tasks such as transcoding, generating thumbnails, adding watermarks, and releasing the final video.

## Data Dependency

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7c/v3/pN80croZTECxt85IJmQl7g/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062022Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=6DBA33C5589C4D98BAC50D62BB63BAB844EE97CB386E19F81F90A872100B091E)

When the signature of a data object appears in in\_deps of a task, the task is referred to as a consumer task that executes without modifying the original input data object.

When the signature of a data object appears in out\_deps of a task, the task is referred to as a producer task that updates the output data object's content to create a new version.

Data dependency applies to scenarios where tasks are triggered by data production and consumption relationships.

A data object may have multiple versions. Each version corresponds to one producer task and zero, one, or more consumer tasks. A sequence of the data object versions and the version-specific producer task and consumer tasks are defined according to the delivery sequence of the producer task and consumer tasks.

When all producer tasks and consumer tasks of the data object of all the available versions are executed, the data dependency is removed. In this case, the task enters the ready state and can be scheduled for execution.

FFRT can dynamically build producer/consumer-based data dependencies between tasks at runtime and perform scheduling based on the task data dependency status, including:

-   Producer-Consumer dependency
    
    A dependency formed between the producer task of a data object of a specific version and a consumer task of the data object of the same version. It is also referred to as a read-after-write dependency.
    
-   Consumer-Producer dependency
    
    A dependency formed between a consumer task of a data object of a specific version and the producer task of the data object of the next version. It is also referred to as a write-after-read dependency.
    
-   Producer-Producer dependency
    
    A dependency formed between the producer task of a data object of a specific version and a producer task of the data object of the next version. It is also referred to as a write-after-write dependency.
    

For example, the relationship between a group of tasks and data A is expressed as follows:

task1(OUT A);
task2(IN A);
task3(IN A);
task4(OUT A);
task5(OUT A);

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/19/v3/MmM-X5F-S02jKyazqDRONw/en-us_image_0000002537765102.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062022Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=8891470E8373878966BBB4F27B6D532BF689C8D6E1EBE969BAA65D549659EAAE)

For ease of description, circles are used to represent tasks and squares are used to represent data.

The following conclusions can be drawn:

-   task1 and task2/task3 form a producer-consumer dependency. This means that task2/task3 can read data A only after task1 writes data A.
-   task2/task3 and task4 form a consumer-producer dependency. This means that task4 can write data A only after task2/task3 reads data A.
-   task 4 and task 5 form a producer-producer dependency. This means that task 5 can write data A only after task 4 writes data A.

#### Example: Streaming Video Processing

A user uploads a video to the platform. The processing steps include: parsing, transcoding, generating a thumbnail, adding a watermark, and releasing the video. Transcoding and thumbnail generation can occur simultaneously. The following figure shows the task process.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/62/v3/cTDeJIvrRGSG-PBdOQrzZw/en-us_image_0000002537925042.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062022Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=61EF0C292B685C14025EEEBE440685A0A6CAB6FC482FE62D4335D0FE53004B4F)

The FFRT provides task graph that can describe the task dependency and parallelize the preceding video processing process. The code is as follows:

#include <stdio.h>
#include "ffrt/ffrt.h" // From the HarmonyOS third-party library "@ppd/ffrt"

void func\_TaskA(void\* arg)
{
    printf("Parse\\n");
}

void func\_TaskB(void\* arg)
{
    printf("Transcode\\n");
}

void func\_TaskC(void\* arg)
{
    printf("Generate a thumbnail\\n");
}

void func\_TaskD(void\* arg)
{
    printf("Add watermark\\n");
}

void func\_TaskE(void\* arg)
{
    printf("Release\\n");
}

int main()
{
    // Submit task A.
    ffrt\_task\_handle\_t hTaskA = ffrt\_submit\_h\_f(func\_TaskA, NULL, NULL, NULL, NULL);

    // Submit tasks B and C.
    ffrt\_dependence\_t taskA\_deps\[\] = {{ffrt\_dependence\_task, hTaskA}};
    ffrt\_deps\_t dTaskA = {1, taskA\_deps};
    ffrt\_task\_handle\_t hTaskB = ffrt\_submit\_h\_f(func\_TaskB, NULL, &dTaskA, NULL, NULL);
    ffrt\_task\_handle\_t hTaskC = ffrt\_submit\_h\_f(func\_TaskC, NULL, &dTaskA, NULL, NULL);

    // Submit task D.
    ffrt\_dependence\_t taskBC\_deps\[\] = {{ffrt\_dependence\_task, hTaskB}, {ffrt\_dependence\_task, hTaskC}};
    ffrt\_deps\_t dTaskBC = {2, taskBC\_deps};
    ffrt\_task\_handle\_t hTaskD = ffrt\_submit\_h\_f(func\_TaskD, NULL, &dTaskBC, NULL, NULL);

    // Submit task E.
    ffrt\_dependence\_t taskD\_deps\[\] = {{ffrt\_dependence\_task, hTaskD}};
    ffrt\_deps\_t dTaskD = {1, taskD\_deps};
    ffrt\_submit\_f(func\_TaskE, NULL, &dTaskD, NULL, NULL);

    // Wait until all tasks are complete.
    ffrt\_wait();

    ffrt\_task\_handle\_destroy(hTaskA);
    ffrt\_task\_handle\_destroy(hTaskB);
    ffrt\_task\_handle\_destroy(hTaskC);
    ffrt\_task\_handle\_destroy(hTaskD);
    return 0;
}

The expected output may be as follows:

Video parsing
Video transcoding
Thumbnails generation
Watermark adding
Video release

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cb/v3/1Ro-6s1hQUiHZ_b9FTyYlw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062022Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=E8E91EC43643B21B03C4FCECCFB004380A772C014135A176306D150F887C71E3)

The ffrt\_submit\_h\_f and ffrt\_submit\_f APIs can receive naked function pointer tasks as parameters. If there are pre-processing and post-processing operations on the task, refer to the [ffrt\_alloc\_auto\_managed\_function\_storage\_base](../../function-flow-runtime-c-apis/document.md#ffrt_alloc_auto_managed_function_storage_base) function to construct the task structure.

#### Example: Fibonacci Sequence

Each number in the Fibonacci sequence is the sum of the first two numbers. The process of calculating the Fibonacci number can well express the task dependency through the data object. The code for calculating the Fibonacci number using the FFRT framework is as follows:

#include <stdio.h>
#include "ffrt/ffrt.h" // From the HarmonyOS third-party library "@ppd/ffrt"

typedef struct {
    int x;
    int\* y;
} fib\_ffrt\_s;

void fib\_ffrt(void\* arg)
{
    fib\_ffrt\_s\* p = (fib\_ffrt\_s\*)arg;
    int x = p->x;
    int\* y = p->y;

    if (x <= 1) {
        \*y = x;
    } else {
        int y1, y2;
        fib\_ffrt\_s s1 = {x - 1, &y1};
        fib\_ffrt\_s s2 = {x - 2, &y2};

        // Build data dependencies.
        ffrt\_dependence\_t dx\_deps\[\] = {{ffrt\_dependence\_data, &x}};
        ffrt\_deps\_t dx = {1, dx\_deps};
        ffrt\_dependence\_t dy1\_deps\[\] = {{ffrt\_dependence\_data, &y1}};
        ffrt\_deps\_t dy1 = {1, dy1\_deps};
        ffrt\_dependence\_t dy2\_deps\[\] = {{ffrt\_dependence\_data, &y2}};
        ffrt\_deps\_t dy2 = {1, dy2\_deps};
        ffrt\_dependence\_t dy12\_deps\[\] = {{ffrt\_dependence\_data, &y1}, {ffrt\_dependence\_data, &y2}};
        ffrt\_deps\_t dy12 = {2, dy12\_deps};

        // Submit tasks separately.
        ffrt\_submit\_f(fib\_ffrt, &s1, &dx, &dy1, NULL);
        ffrt\_submit\_f(fib\_ffrt, &s2, &dx, &dy2, NULL);

        // Wait until the task is complete.
        ffrt\_wait\_deps(&dy12);
        \*y = y1 + y2;
    }
}

int main()
{
    int r;
    fib\_ffrt\_s s = {5, &r};
    ffrt\_dependence\_t dr\_deps\[\] = {{ffrt\_dependence\_data, &r}};
    ffrt\_deps\_t dr = {1, dr\_deps};
    ffrt\_submit\_f(fib\_ffrt, &s, NULL, &dr, NULL);

    // Wait until the task is complete.
    ffrt\_wait\_deps(&dr);
    printf("Fibonacci(5) is %d\\n", r);
    return 0;
}

Expected output:

Fibonacci(5) is 5

In the example, fibonacci(x-1) and fibonacci(x-2) are submitted to FFRT as two tasks. After the two tasks are complete, the results are accumulated. Although a single task is split into two subtasks, the subtasks can be further split. Therefore, the concurrency of the entire computational graph is very high.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c5/v3/Ptqe9SncS6WJUpE4qd1avQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062022Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=58C7770D74BC293212E94405D6216F86111C09786FED8D4450F2BC0E3D37DB56)

The ffrt\_submit\_f API can receive a naked function pointer task as a parameter. If there are pre-processing and post-processing operations on the task, refer to the [ffrt\_alloc\_auto\_managed\_function\_storage\_base](../../function-flow-runtime-c-apis/document.md#ffrt_alloc_auto_managed_function_storage_base) function to construct the task structure.

Each task forms a call tree in the FFRT.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/23/v3/VS6D0QN8RwidiBlLhvjhow/en-us_image_0000002568684819.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062022Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=A99BBA8B69DCEFA14F540AA1CDEBE58089F6C51EEF4E35E01AECB0F1D7F1F505)

#### Available APIs

The main FFRT APIs involved in the preceding example are as follows:

| Name | Description |
| :-- | :-- |
| [ffrt\_submit\_f](../../function-flow-runtime-c-apis/document.md#ffrt_submit_f) | 
Submits a task.

**Note**: This API is supported since API version 20.

 |
| [ffrt\_submit\_h\_f](../../function-flow-runtime-c-apis/document.md#ffrt_submit_h_f) | 

Submits a task, and obtains the task handle.

**Note**: This API is supported since API version 20.

 |
| [ffrt\_wait\_deps](../../function-flow-runtime-c-apis/document.md#ffrt_wait_deps) | Waits until the dependent tasks are complete. |

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/70/v3/qfl45l7wSWWImy36lDWPqw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062022Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=78436FDDE1219F50FC992D8E95AB5D2791BEA41DF6513C2DC79140640347898B)

-   For details about how to use FFRT C++ APIs, see [Using FFRT C++ APIs](../../function-flow-runtime-development/document.md#using-ffrt-c-api-1).
-   When using FFRT C or C++ APIs, you can refer to the FFRT C++ API third-party library to simplify the header file inclusion, that is, use the #include "ffrt/ffrt.h" header file to include statements.

#### Constraints

-   For ffrt\_submit\_base, the total number of input dependencies and output dependencies of each task cannot exceed 8.
-   For ffrt\_submit\_h\_base, the total number of input dependencies and output dependencies of each task cannot exceed 7.
-   When a parameter is used as both input dependency and output dependency, the number of dependencies is counted only once. For example, if the input dependency is {&x} and the output dependency is {&x}, the actual number of dependencies is 1.
