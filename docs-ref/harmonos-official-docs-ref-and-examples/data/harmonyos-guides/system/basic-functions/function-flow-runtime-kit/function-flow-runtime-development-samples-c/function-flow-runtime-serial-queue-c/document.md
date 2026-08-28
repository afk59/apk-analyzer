# Function Flow Runtime Serial Queue (C)

#### Overview

The FFRT serial queue is implemented based on the coroutine scheduling model. It provides efficient message queue functions and supports multiple service scenarios, such as asynchronous communication, mobile data peak clipping, lock-free status and resource management, and architecture decoupling. The following functions are supported:

-   **Queue creation and destruction**: The queue name and priority can be specified during creation. Each queue is equivalent to an independent thread. Tasks in the queue are executed asynchronously compared with user threads.
-   **Task delay**: The delay can be set when a task is submitted. The unit is μs. The delayed task will be scheduled and executed after uptime (submission time + delay time).
-   **Serial scheduling**: Tasks in the same queue are sorted in ascending order of uptime and executed in serial mode. Ensure that the next task starts to be executed only after the previous task in the queue is complete.
-   **Task canceling**: You can cancel a task that is not dequeued based on the task handle. The task cannot be canceled if it has been started or completed.
-   **Task waiting**: You can wait for a task to complete based on the task handle. When a specified task is complete, all tasks whose uptime is earlier than the specified task in the queue have been executed.
-   **Task priority**: You can set the priority of a single task when submitting the task. Priorities take effect only after a task is dequeued relative to other system loads, and do not affect the serial task order in the same queue. If the task priority is not set, the priority of the queue is inherited by default.

#### Example: Asynchronous Log System

The following is an example of implementing an asynchronous log system. The main thread submits the log task to the queue, and the background thread obtains the task from the queue and writes the task to the file. It ensures the log sequence and prevents the main thread from being blocked by the file write operation.

With FFRT APIs, you only need to focus on service logic implementation and do not need to pay attention to asynchronous thread management, thread security, and scheduling efficiency.

The example simplifies the logic for handling exceptions and ensuring thread security. The code is as follows:

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include "ffrt/ffrt.h" // From the HarmonyOS third-party library "@ppd/ffrt"

typedef struct {
    FILE \*logFile;          // Pointer to a log file.
    ffrt\_queue\_t queue;     // Task queue.
} logger\_t;

// Global logger variable.
logger\_t\* g\_logger = NULL;

// Initialize the log system.
logger\_t \*logger\_create(const char \*filename)
{
    logger\_t \*logger = (logger\_t \*)malloc(sizeof(logger\_t));
    if (!logger) {
        perror("Failed to allocate memory for logger\_t");
        return NULL;
    }

    // Open the log file.
    logger->logFile = fopen(filename, "a");
    if (!logger->logFile) {
        perror("Failed to open log file");
        free(logger);
        return NULL;
    }
    printf("Log file opened: %s\\n", filename);

    // Create a task queue.
    logger->queue = ffrt\_queue\_create(ffrt\_queue\_serial, "logger\_queue\_c", NULL);
    if (!logger->queue) {
        perror("Failed to create queue");
        fclose(logger->logFile);
        free(logger);
        return NULL;
    }

    return logger;
}

// Destroy the log system.
void logger\_destroy(logger\_t \*logger)
{
    if (logger) {
        // Destroy the queue.
        if (logger->queue) {
            ffrt\_queue\_destroy(logger->queue);
        }

        // Close the log file.
        if (logger->logFile) {
            fclose(logger->logFile);
            printf("Log file closed\\n");
        }

        free(logger);
    }
}

// Log task.
void write\_task(void \*arg)
{
    char \*message = (char \*)arg;
    if (g\_logger && g\_logger->logFile) {
        fprintf(g\_logger->logFile, "%s\\n", message);
        fflush(g\_logger->logFile);
    }

    free(message);
}

// Add a log task.
void logger\_log(logger\_t \*logger, const char \*message)
{
    if (!logger || !logger->queue) {
        return;
    }

    // Copy the message string.
    char \*messageCopy = strdup(message);
    if (!messageCopy) {
        perror("Failed to allocate memory for message");
        return;
    }

    ffrt\_queue\_submit\_f(logger->queue, write\_task, messageCopy, NULL);
}

int main()
{
    // Initialize the global logger.
    g\_logger = logger\_create("log\_c.txt");
    if (!g\_logger) {
        return -1;
    }

    // Use the global logger to add a log task.
    logger\_log(g\_logger, "Log message 1");
    logger\_log(g\_logger, "Log message 2");
    logger\_log(g\_logger, "Log message 3");

    // Simulate the main thread to continue executing other tasks.
    sleep(1);

    // Destroy the global logger.
    logger\_destroy(g\_logger);
    g\_logger = NULL;
    return 0;
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2a/v3/JEjj1FLCR_SOgyT-V2ySXQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062021Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=E3D4D8D2186559D6B113F9B5E3C4BAE36F504B0EEC9138C55ABD850F02261765)

The ffrt\_queue\_submit\_h\_f API can receive a naked function pointer task as a parameter. If there are pre-processing and post-processing operations on the task, refer to the [ffrt\_alloc\_auto\_managed\_function\_storage\_base](../../function-flow-runtime-c-apis/document.md#ffrt_alloc_auto_managed_function_storage_base) function to construct the task structure.

#### Available APIs

The main FFRT APIs involved in the preceding example are as follows:

| Name | Description |
| :-- | :-- |
| [ffrt\_queue\_create](../../function-flow-runtime-c-apis/document.md#ffrt_queue_t) | Creates a queue. |
| [ffrt\_queue\_destroy](../../function-flow-runtime-c-apis/document.md#ffrt_queue_t) | Destroys a queue. |
| [ffrt\_queue\_submit\_f](../../function-flow-runtime-c-apis/document.md#ffrt_queue_t) | 
Submits a task to a queue.

**Note**: This API is supported since API version 20.

 |

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/15/v3/ZwPE9EvTR7CSq46Yc4QOBQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062021Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=C18A40C858140F04B30FC0593918F92465B608F14F2F435553C471BEC6CC04B5)

-   For details about how to use FFRT C++ APIs, see [Using FFRT C++ APIs](../../function-flow-runtime-development/document.md#using-ffrt-c-api-1).
-   When using FFRT C or C++ APIs, you can use the FFRT C++ API third-party library to simplify the header file inclusion, that is, use the #include "ffrt/ffrt.h" header file to include statements.

#### Constraints

-   **Avoid submitting ultra-long tasks.** The FFRT has a built-in process-level queue task timeout detection mechanism. When the execution time of a serial task exceeds the preset threshold (30 seconds by default), the system prints and reports exception logs and triggers the preset process timeout callback function (if configured).
-   **Use synchronization primitives correctly.** Do not use std::mutex, std::condition\_variable, or std::recursive\_mutex in the task closure submitted to FFRT. As synchronization primitives in the standard library will occupy the FFRT Worker thread for a long time, you should use the synchronization primitives provided by FFRT: ffrt::mutex, ffrt::condition\_variable, or ffrt::recursive\_mutex. The usage is the same as that of the standard library.
-   **Manage queues in global variables.** If serial queues are managed in global variables and destroyed with service processes, pay attention to lifecycle decoupling in the test program. When the test is complete, the serial queue needs to be explicitly released. Other resources can be released with global variables. The reason is that global variables are destructed after the main function ends, and the release of serial queues depends on other resources in the FFRT framework, and the resources may have been destroyed.
