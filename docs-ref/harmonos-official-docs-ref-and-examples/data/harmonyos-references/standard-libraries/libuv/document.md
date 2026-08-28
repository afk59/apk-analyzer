# libuv

#### Introduction

[libuv](http://libuv.org/) is a cross-platform library that implements asynchronous I/O based on event loops. It applies to network programming and file system operations. It is one of the core libraries of Node.js and has been widely used by other software projects.

#### Supported Capabilities

[libuv](http://libuv.org/) implements event-driven asynchronous I/O across platforms and supports standard library interfaces.

#### Including libuv

To use libuv capabilities, include the following header file:

#include <uv.h>

Add the following dynamic link library to **CMakeLists.txt**:

libuv.so

#### Available APIs

For details, see [API documentation](http://docs.libuv.org/en/v1.x/api.html).

#### Background of Introducing libuv to HarmonyOS

HarmonyOS introduced Node-API of Node.js in its earlier versions to facilitate Node.js developers to extend their JavaScript (JS) APIs with HarmonyOS. It also introduced libuv of Node.js to implement event loops.

## Evolution Trend

To address the scheduling issues caused when the application main thread has an event loop that contains **uvloop**, we plan to normalize the event loops in the application model to allow only one task queue in the application main loop with task priorities controlled.

You are advised not to use libuv NDK on the main loop of the application obtained by calling napi\_get\_uv\_event\_loop. Otherwise, various problems may occur, and a large amount of workload will be brought to future compatibility changes.

If you want to implement interaction with the main thread cyclically, for example, insert a task, use [Node-API](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/napi-data-types-interfaces).

We will continue to provide capabilities of interacting with the main thread and extend JS APIs through Node-API in the future for a long period of time, but shield the event loops in the implementation layer. the main functional APIs of Node-API will be maintained for a long time and provide the same native behavior of Node-API, so that the developers who are familiar with the node.js extension mechanism can easily expand their code to HarmonyOS.

If you are familiar with libuv and can handle memory management and multithreading problems, you can still use libuv to develop your services on HarmonyOS. Unless otherwise required, you do not need to import the libuv library to your application project.

#### Current Problems and Solutions

According to the existing mechanism, only one event loop can exist in a thread. To ensure proper running of the main event loop of the system application, the main event loop listens for the FD events in the JS environment and executes **uv\_run** only when an FD event is reported. As a result, certain functions that depend on the **uvloop** event cannot take effect.

Common scenarios and solutions are as follows:

## Scenario 1: The JS main thread throws an asynchronous task to a worker thread for execution and executes the result returned by the JS code.

**Example (incorrect)**

Call **napi\_get\_uv\_event\_loop()** to obtain the system loop, and use libuv NDK APIs to implement related functions.

ArkTS side:

import { hilog } from '@kit.PerformanceAnalysisKit';
import testNapi from 'libentry.so'

@Entry
@Component
struct Index {
  build() {
    Row() {
      Column() {
        Button("test")
          .width('40%')
          .fontSize('14fp')
          .onClick(() => {
              testNapi.test();
        }).margin(20)
      }.width('100%')
    }.height('100%')
  }
}

Native side:

#include "napi/native\_api.h"
#include "uv.h"
#define LOG\_DOMAIN 0X0202
#define LOG\_TAG "MyTag"
#include <hilog/log.h>

static void execute(uv\_work\_t\* work)
{
    OH\_LOG\_INFO(LOG\_APP, "ohos in execute");
}

static void complete(uv\_work\_t\* work, int status)
{
    OH\_LOG\_INFO(LOG\_APP, "ohos in complete");
    delete work;
}
static napi\_value Test(napi\_env env, napi\_callback\_info info)
{
    uv\_loop\_s\* loop = nullptr;
    /\* Obtain the uv\_loop of the application JS main thread. \*/
    napi\_get\_uv\_event\_loop(env, &loop);
    uv\_work\_t\* work = new uv\_work\_t;
    int ret = uv\_queue\_work(loop, work, execute, complete);
    if (ret != 0) {
        OH\_LOG\_INFO(LOG\_APP, "delete work");
        delete work;
    }
    return 0;
}

EXTERN\_C\_START
static napi\_value Init(napi\_env env, napi\_value exports)
{
    napi\_property\_descriptor desc\[\] = {{"test", nullptr, Test, nullptr, nullptr, nullptr, napi\_default, nullptr}};
    napi\_define\_properties(env, exports, sizeof(desc) / sizeof(desc\[0\]), desc);
    return exports;
}
EXTERN\_C\_END
    
static napi\_module demoModule = {
    .nm\_version = 1,
    .nm\_flags = 0,
    .nm\_filename = nullptr,
    .nm\_register\_func = Init,
    .nm\_modname = "entry",
    .nm\_priv = ((void \*)0),
    .reserved = {0},
};

extern "C" \_\_attribute\_\_((constructor)) void RegisterEntryModule(void)
{
    napi\_module\_register(&demoModule);
}

Add the following code to the **index.d.ts** file:

export const test:() => number;

**Example (correct)**:

Use **napi\_create\_async\_work** and **napi\_queue\_async\_work** together.

ArkTS side:

import { hilog } from '@kit.PerformanceAnalysisKit';
import testNapi from 'libentry.so'

@Entry
@Component
struct Index {
  build() {
    Row() {
      Column() {
        Button("test")
          .width('40%')
          .fontSize('14fp')
          .onClick(() => {
              testNapi.test();
        }).margin(20)
      }.width('100%')
    }.height('100%')
  }
}

Native side:

#include "napi/native\_api.h"
#include "uv.h"
#define LOG\_DOMAIN 0X0202
#define LOG\_TAG "MyTag"
#include <hilog/log.h>
uv\_loop\_t\* loop = nullptr;
napi\_value jsCb;
int fd = -1;

static napi\_value Test(napi\_env env, napi\_callback\_info info)
{
    napi\_value work\_name;
    napi\_async\_work work;
    napi\_create\_string\_utf8(env, "ohos", NAPI\_AUTO\_LENGTH, &work\_name);
    /\* The fourth parameter specifies the work task of the asynchronous thread, and the fifth parameter is the callback of the main thread. \*/
    napi\_create\_async\_work(
        env, nullptr, work\_name, \[\](napi\_env env, void\* data){OH\_LOG\_INFO(LOG\_APP, "ohos in execute"); },
        \[\](napi\_env env, napi\_status status, void\* data){
            /\* The specific implementation is skipped. \*/
            OH\_LOG\_INFO(LOG\_APP, "ohos in complete");
            napi\_delete\_async\_work(env, (napi\_async\_work)data);
        },
        nullptr, &work);
    /\* Call napi\_queue\_async\_work to trigger an async task. \*/
    napi\_queue\_async\_work(env, work);
    return 0;
}

EXTERN\_C\_START
static napi\_value Init(napi\_env env, napi\_value exports)
{
    napi\_property\_descriptor desc\[\] = {{"test", nullptr, Test, nullptr, nullptr, nullptr, napi\_default, nullptr}};
    napi\_define\_properties(env, exports, sizeof(desc) / sizeof(desc\[0\]), desc);
    return exports;
}
EXTERN\_C\_END
    
static napi\_module demoModule = {
    .nm\_version = 1,
    .nm\_flags = 0,
    .nm\_filename = nullptr,
    .nm\_register\_func = Init,
    .nm\_modname = "entry",
    .nm\_priv = ((void \*)0),
    .reserved = {0},
};

extern "C" \_\_attribute\_\_((constructor)) void RegisterEntryModule(void)
{
    napi\_module\_register(&demoModule);
}

Add the following code to the **index.d.ts** file:

export const test:() => number;

## Scenario 2: The libuv API does not work when throwing an FD event to the main loop of the application from the native side.

The main loop of the application receives only FD events, and executes **uv\_run** only after **backend\_fd** in **uvloop** is triggered. That means **uv\_run** will never be executed if no FD event is triggered when libuv APIs are called in the main loop of the application. As a result, calling libuv APIs does not take effect.

**Example (incorrect)**

In the following example, calling **uv\_poll\_start** in the same way as in native libuv on HarmonyOS does not take effect.

ArkTS side:

import { hilog } from '@kit.PerformanceAnalysisKit';
import testNapi from 'libentry.so'

@Entry
@Component
struct Index {
  build() {
    Row() {
      Column() {
        Button("testClose")
          .width('40%')
          .fontSize('14fp')
          .onClick(() => {
              testNapi.testClose();
        }).margin(20)
      }.width('100%')
    }.height('100%')
  }
}

Native side:

#include "napi/native\_api.h"
#include "uv.h"
#define LOG\_DOMAIN 0X0202
#define LOG\_TAG "MyTag"
#include <hilog/log.h>
#include <thread>
#include <sys/eventfd.h>

uv\_loop\_t\* loop = nullptr;
napi\_value jsCb;
int fd = -1;

void poll\_handler(uv\_poll\_t\* handle,int status, int events)
{
    OH\_LOG\_INFO(LOG\_APP, "ohos poll print");
}

static napi\_value TestClose(napi\_env env, napi\_callback\_info info)
{
    std::thread::id this\_id = std::this\_thread::get\_id();
    OH\_LOG\_INFO(LOG\_APP, "ohos thread id : %{public}ld", this\_id);
    size\_t argc = 1;
    napi\_value workBname;
    
    napi\_create\_string\_utf8(env, "test", NAPI\_AUTO\_LENGTH, &workBname);
    
    napi\_get\_cb\_info(env, info, &argc, &jsCb, nullptr, nullptr);
    // Obtain the event loop.
    napi\_get\_uv\_event\_loop(env, &loop);
    // Create an eventfd.
    fd = eventfd(0, 0);
    OH\_LOG\_INFO(LOG\_APP, "fd is %{public}d",fd);
    uv\_poll\_t\* poll\_handle = new uv\_poll\_t;
    // Initialize a poll handle and associate it with eventfd.
    uv\_poll\_init(loop, poll\_handle, fd);
    // Start to listen for the poll event.
    uv\_poll\_start(poll\_handle, UV\_READABLE, poll\_handler);
    // Create a new thread and write data to eventfd.
    std::thread mythread(\[\](){
        for (int i = 0; i < 8; i++){
            int value = 10;
            int ret = eventfd\_write(fd, value);
            if (ret == -1){
                OH\_LOG\_INFO(LOG\_APP, "write failed!");
                continue;
            }
        }
    });
    mythread.detach();
    return 0;
}

EXTERN\_C\_START
static napi\_value Init(napi\_env env, napi\_value exports)
{
    napi\_property\_descriptor desc\[\] = {{"testClose", nullptr, TestClose, nullptr, nullptr, nullptr, napi\_default, nullptr}};
    napi\_define\_properties(env, exports, sizeof(desc) / sizeof(desc\[0\]), desc);
    return exports;
}
EXTERN\_C\_END
    
static napi\_module demoModule = {
    .nm\_version = 1,
    .nm\_flags = 0,
    .nm\_filename = nullptr,
    .nm\_register\_func = Init,
    .nm\_modname = "entry",
    .nm\_priv = ((void \*)0),
    .reserved = {0},
};

extern "C" \_\_attribute\_\_((constructor)) void RegisterEntryModule(void)
{
    napi\_module\_register(&demoModule);
}

Add the following code to **index.d.ts**:

export const testClose:() => number;

The process is as follows:

1.  Call **napi\_get\_uv\_event\_loop** to obtain **uvloop** of the application main thread.
2.  Create an eventfd instance.
3.  Initialize **uv\_poll\_t**, and start the handle for it to take effect. Invoke the **poll\_handler** callback when the eventfd instance is readable.
4.  Create a thread and write data to the eventfd instance.

After the preceding code is executed, **poll\_handler** has no output. This is because the application main thread executes **uv\_run** based on the FD rather than looping in UV\_RUN\_DEFAULT mode. Although **event\_handler** listens for **backend\_fd** in **uvloop**, the FD is not added to **backend\_fd** through **epoll\_ctl** when **uv\_poll\_start** is executed. The **epoll\_ctl** function is executed only when **uv\_\_io\_poll** in **uv\_run** is executed the next time. Therefore, if no **backend\_fd** event is triggered in the application process, the libuv APIs may not work as expected.

**Workaround**

In the current system version, do not use **napi\_get\_uv\_event\_loop** to obtain **uvloop** of the application main thread to develop service logic. If libuv must be used to implement service functions, after **uv\_xxx\_start** is called, use **uv\_async\_send** to trigger the main thread of the application to execute **uv\_run**. In this way, **uv\_xxx\_start** can be properly executed.

Modify the code as follows:

ArkTS side:

import { hilog } from '@kit.PerformanceAnalysisKit';
import testNapi from 'libentry.so'

@Entry
@Component
struct Index {
  build() {
    Row() {
      Column() {
        Button("testClose")
          .width('40%')
          .fontSize('14fp')
          .onClick(() => {
              testNapi.testClose();
        }).margin(20)
      }.width('100%')
    }.height('100%')
  }
}

Native side:

#include "napi/native\_api.h"
#include "uv.h"
#define LOG\_DOMAIN 0x0202
#define LOG\_TAG "MyTag"
#include <hilog/log.h>
#include <thread>
#include <sys/eventfd.h>

uv\_loop\_t\* loop = nullptr;
napi\_value jsCb;
int fd = -1;

void poll\_handler(uv\_poll\_t\* handle,int status, int events)
{
    OH\_LOG\_INFO(LOG\_APP, "ohos poll print");
}

static napi\_value TestClose(napi\_env env, napi\_callback\_info info)
{
    std::thread::id this\_id = std::this\_thread::get\_id();
    OH\_LOG\_INFO(LOG\_APP, "ohos thread id : %{public}ld", this\_id);
    size\_t argc = 1;
    napi\_value workBName;
    
    napi\_create\_string\_utf8(env, "test", NAPI\_AUTO\_LENGTH, &workBName);
    
    napi\_get\_cb\_info(env, info, &argc, &jsCb, nullptr, nullptr);

    napi\_get\_uv\_event\_loop(env, &loop);

    fd = eventfd(0, 0);
    OH\_LOG\_INFO(LOG\_APP, "fd is %{public}d",fd);
    uv\_poll\_t\* poll\_handle = new uv\_poll\_t;
    uv\_poll\_init(loop, poll\_handle, fd);
    uv\_poll\_start(poll\_handle, UV\_READABLE, poll\_handler);

    // Trigger an FD event to enable the main thread to execute uv\_run.
    uv\_async\_send(&loop->wq\_async);
    
    std::thread mythread(\[\](){
        for (int i = 0; i < 8; i++){
            int value = 10;
            int ret = eventfd\_write(fd, value);
            if (ret == -1){
                OH\_LOG\_INFO(LOG\_APP, "write failed!");
                continue;
            }
        }
    });
    mythread.detach();
    return 0;
}

EXTERN\_C\_START
static napi\_value Init(napi\_env env, napi\_value exports)
{
    napi\_property\_descriptor desc\[\] = {{"testClose", nullptr, TestClose, nullptr, nullptr, nullptr, napi\_default, nullptr}};
    napi\_define\_properties(env, exports, sizeof(desc) / sizeof(desc\[0\]), desc);
    return exports;
}
EXTERN\_C\_END
    
static napi\_module demoModule = {
    .nm\_version = 1,
    .nm\_flags = 0,
    .nm\_filename = nullptr,
    .nm\_register\_func = Init,
    .nm\_modname = "entry",
    .nm\_priv = ((void \*)0),
    .reserved = {0},
};

extern "C" \_\_attribute\_\_((constructor)) void RegisterEntryModule(void)
{
    napi\_module\_register(&demoModule);
}

Add the following code to **index.d.ts**:

export const testClose:() => number;

#### Using libuv

In the libuv NDK, all the APIs that depend on **uv\_run** do not work as expected in the application main loop of the current system, and may cause freezing or loss of frames. You are advised not to directly use libuv NDK APIs in the JS main thread. You can use Node-API to implement asynchronous task execution and communication with the main thread via thread-safe functions.

## Mappings Between libuv APIs and Node-APIs

Instead of using libuv APIs, you can use the equivalent Node-API provided by HarmonyOS, which includes asynchronous work APIs and thread-safe APIs.

**Asynchronous Task APIs**

libuv provides the **uv\_queue\_work** API to perform a time-consuming operation in an asynchronous thread and return the result to the main thread for processing through a callback.

You can use [napi\_async\_work](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/use-napi-asynchronous-task) APIs of Node-API to implement asynchronous operations.

The related Node-API interfaces are as follows:

/\*\*
\* @brief Creates a work object that executes logic asynchronously.
\*
\* @param env Pointer to the current execution environment.
\* @param async\_resource (Optional) Resource object used to trace asynchronous operations.
\* @param async\_resource\_name (Optional) Name of the resource object. The value is a string.
\* @param execute Callback invoked to perform an asynchronous operation in another thread.
\* @param execute Callback to be invoked when the asynchronous operation is complete.
\* @param data Pointer to the customized data to be passed to the execute() and complete() callbacks.
\* @param result Pointer to the asynchronous work object created.
\*/
napi\_status napi\_create\_async\_work(napi\_env env,
                                  napi\_value async\_resource,
                                  napi\_value async\_resource\_name,
                                  napi\_async\_execute\_callback execute,
                                  napi\_async\_complete\_callback complete,
                                  void\* data,
                                  napi\_async\_work\* result);

/\*\*
\* @brief Adds an asynchronous work object to the queue so that it can be scheduled for execution.
\*
\* @param env Pointer to the current execution environment.
\* @param work Pointer to the asynchronous work object to add.
\*/
napi\_status napi\_queue\_async\_work(napi\_env env, napi\_async\_work work);

/\*\*
\* @brief Deletes an asynchronous work object.
\*
\* @param env Pointer to the current execution environment.
\* @param work Pointer to the asynchronous work object to delete.
\*/
napi\_status napi\_delete\_async\_work(napi\_env env, napi\_async\_work work);

**Thread-safe APIs for Cross-Thread Sharing and Invocation**

When you want to pass a callback from any child thread to the application main thread for execution, you can use the libuv **uv\_async\_t** handle for inter-thread communication, and the following functions:

-   uv\_async\_init()
-   uv\_async\_send()

The equivalent Node-API interfaces are [napi\_threadsafe\_function](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/use-napi-thread-safety) APIs.

The related Node-API interfaces are as follows:

/\*\*
\* @brief Creates a thread-safe function, which can be called in multiple threads without causing data contention or other thread-safe issues.
\*
\* @param env Pointer to the Node-API environment. It is used to create and operate JS values.
\* @param func Pointer to the JavaScript function to create.
\* @param async\_resource Asynchronous resource, which is usually an object that indicates an asynchronous operation.
\* @param async\_resource\_name Pointer to the resource name, which is used for logging and debugging.
\* @param max\_queue\_size An integer specifying the maximum size of a queue. When the queue is full, new calls will be discarded.
\* @param initial\_thread\_count An unsigned integer indicating the initial number of threads when a thread-safe function is created.
\* @param thread\_finalize\_data Data to be cleared before all threads are created.
\* @param napi\_finalize Callback function thread\_finalize\_cb, which is called when all threads are complete and is used to clear resources
\* @param context Pointer to the context, which is passed to call\_js\_func().
\* @param call\_js\_cb Pointer to the callback to be invoked when the JS function is called.
\* @param result Pointer to the napi\_threadsafe\_function struct, which will be constructed as the thread-safe function created.
\*/
napi\_status napi\_create\_threadsafe\_function(napi\_env env,
                                            napi\_value func,
                                            napi\_value async\_resource,
                                            napi\_value async\_resource\_name,
                                            size\_t max\_queue\_size,
                                            size\_t initial\_thread\_count,
                                            void\* thread\_finalize\_data,
                                            napi\_finalize thread\_finalize\_cb,
                                            void\* context,
                                            napi\_threadsafe\_function\_call\_js call\_js\_cb,
                                            napi\_threadsafe\_function\* result);

/\*\*
\* @brief Acquires a thread-safe function.
\*
\* @param function Pointer to the thread-safe function to release.
\*/
napi\_status napi\_acquire\_threadsafe\_function(napi\_threadsafe\_function function);

/\*\*
\* @brief Calls a thread-safe function.
\* @param function Pointer to the thread-safe function to release.
\* @param data Pointer to the user data.
\* @param is\_blocking Enumerated value that determines whether the JavaScript function call is blocking or non-blocking.
\*/
napi\_status napi\_call\_threadsafe\_function(napi\_threadsafe\_function function,
                                          void\* data,
                                          napi\_threadsafe\_function\_call\_mode is\_blocking);
/\*\*
\* @brief Releases a thread-safe function.
\*
\* @param function Pointer to the thread-safe function to release.
\* @param is\_blocking Enumerated value that determines whether the JavaScript function call is blocking or non-blocking.
\*/
napi\_status napi\_release\_threadsafe\_function(napi\_threadsafe\_function function,
                                             napi\_threadsafe\_function\_call\_mode is\_blocking);

If you need to use other libuv APIs to implement service functions, read on to discover basic libuv concepts and common APIs to be used in HarmonyOS, which are helpful to prevent application crashes when using libuv APIs. The following also provides information about the APIs that can be used in the application main thread and those cannot.

## Available APIs

| API Type | API |
| :-- | :-- |
| [Loop](#event-loops-in-libuv) | uv\_loop\_init |
| [Loop](#event-loops-in-libuv) | uv\_loop\_close |
| [Loop](#event-loops-in-libuv) | uv\_default\_loop |
| [Loop](#event-loops-in-libuv) | uv\_run |
| [Loop](#event-loops-in-libuv) | uv\_loop\_alive |
| [Loop](#event-loops-in-libuv) | uv\_stop |
| [Handle](#handles-and-requests-in-libuv) | uv\_poll\_\* |
| [Handle](#handles-and-requests-in-libuv) | uv\_timer\_\* |
| [Handle](#handles-and-requests-in-libuv) | uv\_async\_\* |
| [Handle](#handles-and-requests-in-libuv) | uv\_signal\_\* |
| [Handle](#handles-and-requests-in-libuv) | uv\_fs\_\* |
| [Request](#handles-and-requests-in-libuv) | uv\_random |
| [Request](#handles-and-requests-in-libuv) | uv\_getaddrinfo |
| [Request](#handles-and-requests-in-libuv) | uv\_getnameinfo |
| [Request](#handles-and-requests-in-libuv) | uv\_queue\_work |
| [Inter-Thread communication](#inter-thread-communication) | uv\_async\_init |
| [Inter-Thread communication](#inter-thread-communication) | uv\_async\_send |
| [Thread pool](#thread-pool) | uv\_queue\_work |

## Constraints for libuv Single Thread

When using libuv in HarmonyOS, observe to the following: The thread for calling **uv\_run** must be the loop thread (the thread that initializes the loop using **uv\_loop\_init**), and all non-thread-safe operations of **uvloop** must be performed on the loop thread. Otherwise, the application may crash. HarmonyOS imposes stricter restrictions on the use of libuv. For non-thread-safe functions, libuv implements the multi-thread check mechanism, which generates warning logs when detecting multi-threading problems. To ensure the check accuracy and prevent incorrect use of uv interfaces, it is recommended that the same thread be used for creating an event loop and executing **uv\_run**. The constraints vary depending on the source of the loop. Specifically, you can create a loop or obtain a loop from **env**.

**Creating a Loop**

You can call **uv\_loop\_new** to create a loop or call **uv\_loop\_init** to initialize a loop. You need to manage the lifecycle of the loop. In this case, ensure that **uv\_run** is executed on the loop thread, that is, the thread where the loop is created or initialized. In addition, non-thread-safe operations, such as operations related to the timer, must be performed on the loop thread.

If tasks have to be thrown from other threads to the loop thread, use **uv\_async\_send**. Specifically, register a callback when the async handle is initialized, and implement the corresponding operation in the callback. When **uv\_async\_send** is called, execute the registered callback on the main thread.

ArkTS side:

import { hilog } from '@kit.PerformanceAnalysisKit';
import testNapi from 'libentry.so'

@Entry
@Component
struct Index {
  build() {
    Row() {
      Column() {
        Button("TestTimerAsync")
          .width('40%')
          .fontSize('14fp')
          .onClick(() => {
              testNapi.testTimerAsync();  // Initialize the async handle.
        }).margin(20)
          
          Button("TestTimerAsyncSend")
          .width('40%')
          .fontSize('14fp')
          .onClick(() => {
              testNapi.testTimerAsyncSend(); // Call uv\_async\_send from a child thread to submit the timer task.
        }).margin(20)
      }.width('100%')
    }.height('100%')
  }
}

Native side:

#include <napi/native\_api.h>
#include <uv.h>
#define LOG\_DOMAIN 0x0202
#define LOG\_TAG "MyTag"
#include "hilog/log.h"
#include <thread>

uv\_async\_t\* async = new uv\_async\_t;
bool cond1 = false;
bool cond2 = false;

// Tips: When using a loop, pay special attention to the uv\_stop function. Before calling uv\_stop,
// instruct all threads associated with the loop to close their handles. For details, see the implementation of the stop\_loop function.
int stop\_loop(uv\_loop\_t\* loop)
{
    uv\_stop(loop);
    auto const ensure\_close = \[\](uv\_handle\_t\* handle, void\*) {
        if (uv\_is\_closing(handle)) {
            return;
        } else {
            uv\_close(handle, nullptr);
        }
    };
    // Iterate through all handles. If a handle is active, call ensure\_close on it.
    uv\_walk(loop, ensure\_close, nullptr);
    // Continue to run uv\_run until there is no active handle or request in the loop.
    while(true) {
        if (uv\_run(loop, UV\_RUN\_DEFAULT) == 0) {
            break;
        }
    }

    // Check the loop status.
    if (uv\_loop\_alive(loop) != 0) {
        return -1;
    }
    return 0;
}

// Create a timer.
void async\_cb(uv\_async\_t\* handle) {
    auto loop = handle->loop;
    uv\_timer\_t\* timer = new uv\_timer\_t;
    uv\_timer\_init(loop, timer);

    // Close the async handle at appropriate time.
    if (cond2) {
        uv\_close((uv\_handle\_t\*)handle, \[\](uv\_handle\_t\* handle){
            delete (uv\_async\_t\*)handle;
        });
        return;
    }

    uv\_timer\_start(timer,
        \[\](uv\_timer\_t\* timer){
            // Do something.
            // Stop the timer at the right time.
            if (cond1) {
                uv\_timer\_stop(timer);
                uv\_close((uv\_handle\_t\*)timer, \[\](uv\_handle\_t\* handle){
                    delete(uv\_timer\_t\*)handle;
                });
            }
        },
        100, 100);
}

// Initialize the async handle and bind the corresponding callback.
static napi\_value TestTimerAsync(napi\_env env, napi\_callback\_info info) {
    std::thread t(\[\](){  // Thread A, loop thread
        uv\_loop\_t\* loop = new uv\_loop\_t;
        // Create a loop and manage the loop lifecycle.
        uv\_loop\_init(loop);
        // Initialize an async handle and register a callback.
        uv\_async\_init(loop, async, async\_cb);
        // Start the loop.
        uv\_run(loop, UV\_RUN\_DEFAULT);
        // Close all handles.
        stop\_loop(loop);
        // Release the loop.
        uv\_loop\_close(loop);
        delete loop;
    });
    t.detach();
    return 0;
}

// Call uv\_async\_send on another thread.
static napi\_value TestTimerAsyncSend(napi\_env env, napi\_callback\_info info)
{
    std::thread t1(\[\](){ // Thread B.
        uv\_async\_send (async); // Call uv\_async\_send to instruct the loop thread to call timer\_cb bound to the async handle.
        uv\_sleep(500);
        // Modify cond1 and disable the timer handle.
        cond1 = true;
    });

    std::thread t2(\[\](){ // Thread B.
        uv\_sleep(1000);
        // Modify cond2 and disable the async handle.
        cond2 = true;
        uv\_async\_send(async);
    });

    t1.detach();
    t2.detach();
    return 0;
}

EXTERN\_C\_START
static napi\_value Init(napi\_env env, napi\_value exports)
{
    napi\_property\_descriptor desc\[\] = {
        {"testTimerAsync", nullptr, TestTimerAsync, nullptr, nullptr, nullptr, napi\_default, nullptr},
        {"testTimerAsyncSend", nullptr, TestTimerAsyncSend, nullptr, nullptr, nullptr, napi\_default, nullptr},
    };
    napi\_define\_properties(env, exports, sizeof(desc) / sizeof(desc\[0\]), desc);
    return exports;
}
EXTERN\_C\_END
    
static napi\_module demoModule = {
    .nm\_version = 1,
    .nm\_flags = 0,
    .nm\_filename = nullptr,
    .nm\_register\_func = Init,
    .nm\_modname = "entry",
    .nm\_priv = ((void \*)0),
    .reserved = {0},
};

extern "C" \_\_attribute\_\_((constructor)) void RegisterEntryModule(void)
{
    napi\_module\_register(&demoModule);
}

Add the following code to **index.d.ts**:

export const testTimerAsync:() => number;
export const testTimerAsyncSend:() => number;

**Obtaining a Loop from env**

Generally, the loop obtained from **env** by using **napi\_get\_uv\_event\_loop** is an event loop of a JS main thread created by the system. Therefore, avoid calling non-thread-safe functions on its child threads.

If a non-thread-safe function has to be called on a non-loop thread due to service requirements, use the thread-safe function **uv\_async\_send** to submit the task to the loop thread. Specifically, define a handle of the **uv\_async\_t**\* type. When initializing the handle, add the non-thread-safe function that needs to be called on a child thread in async\_cb. Then, call **uv\_async\_send** in a non-loop thread, and execute **async\_cb** on the loop thread. For details, see case 2 of "Correct Example" in [Handles and Requests in libuv](#handles-and-requests-in-libuv).

## Thread-safe Functions

A large number of asynchronous works are involved in libuv. Improper use of libuv APIs may cause multithreading issues. The following lists the common thread-safe and non-thread-safe functions in libuv. If you call a non-thread-safe function in multi-thread programming, you must add a lock for the function or ensure correct code execution sequence. Otherwise, a crash issue may occur.

Thread-safe functions:

-   **uv\_async\_send()**: sends a signal to an asynchronous handle. This API can be called in any thread.
-   **uv\_thread\_create()**: creates a thread and executes the specified function. This API can be called in any thread.
-   Lock-related APIs, such as **uv\_mutex\_lock()** and **uv\_mutex\_unlock()**.

Tips: Even if the function like **uv\_xxx\_init** is implemented in a thread-safe manner, avoid calling it on multiple threads at the same time. Otherwise, resource contention may occur. The best way is to call the function in an event loop thread.

Note: After **uv\_async\_send** is called, the callback is invoked asynchronously. libuv only ensures that at least one callback is executed if **uv\_async\_send** is called multiple times. As a result, if **uv\_async\_send** is called multiple times for the same handle, the callback processing in libuv may not align with your expectations. However, the native side can ensure that the number of callback execution times matches the number of times that **napi\_call\_threadsafe\_function** is called.

Non-thread-safe functions:

-   **uv\_os\_unsetenv()**: deletes an environment variable.
-   **uv\_os\_setenv()**: sets an environment variable.
-   **uv\_os\_getenv()**: obtains an environment variable.
-   **uv\_os\_environ(**): retrieves all environment variables.
-   **uv\_os\_tmpdir()**: obtains the temporary directory.
-   **uv\_os\_homedir()**: obtains the home directory.

## Event Loops in libuv

As a core concept in libuv, an event loop manages all resources of the entire event loop and runs through the lifecycle of the entire event loop. Generally, the thread where **uv\_run** is located is the main thread of the event loop.

**Event Loop Running Modes**

**UV\_RUN\_DEFAULT**: runs the event loop until there are no active handles or requests. This is the default mode.

**UV\_RUN\_ONCE**: polls for I/O once. If there is a callback in **pending\_queue**, execute the callback and then skip **uv\_\_io\_poll**. In this mode, there is an event to occur in the loop by default.

**UV\_RUN\_NOWAIT**: polls for I/O once but do not block if there are no pending callbacks. In this mode, **uv\_\_io\_poll** is executed once and **pending\_queue** is not executed.

**Common APIs**

int uv\_loop\_init(uv\_loop\_t\* loop);

Initializes a loop.

int uv\_loop\_close(uv\_loop\_t\* loop);

Closes a loop. The operation is successful only after all handles and requests in the loop are closed. Otherwise, **UV\_EBUSY** is returned.

int uv\_loop\_delete(uv\_loop\_t\* loop);

Releases a loop. This API calls **uv\_loop\_close** to release all internal resources associated with the loop and then releases the loop. In HarmonyOS, the **assert()** function does not take effect. Therefore, the loop is released regardless of whether **uv\_loop\_close** successfully clears the loop resources. When using this API, ensure that the resources associated with the loop can be successfully released when the loop thread exits. That is, all the handles and requests associated with the loop must be closed. Otherwise, resource leaks occur. **Exercise caution when using this API. You are advised not to use this API unless necessary.**

uv\_loop\_t\* uv\_default\_loop(void);

Creates a process-level loop. In HarmonyOS, libuv loops still exist in the application main loop and other JS worker threads. You are not advised to use this API to create loops and implement service functions.

int uv\_run(uv\_loop\_t\* loop, uv\_run\_mode mode);

Runs an event loop. For details about the running mode, see "Event Loop Running Modes."

int uv\_loop\_alive(uv\_loop\_t loop);

Checks whether a loop is active.

void uv\_stop(uv\_loop\_t\* loop);

Stops an event loop. The event loop stops only in the next iteration of the loop. If this API is called before an I/O operation, **uv\_\_io\_poll** will be skipped instead of being blocked.

## Handles and Requests in libuv

A handle indicates a persistent object, which is usually mounted to the corresponding **handle\_queue** in a loop. If a handle is active, **uv\_run** will process the callback in the handle each time.

A request indicates a temporary request. A request triggers only one callback.

The commonly used handles and requests in HarmonyOS include the following:

/\* Handle types. \*/
typedef struct uv\_handle\_s uv\_handle\_t;
typedef struct uv\_timer\_s uv\_timer\_t;
typedef struct uv\_async\_s uv\_async\_t;
typedef struct uv\_signal\_s uv\_signal\_t;

/\* Request types. \*/
typedef struct uv\_req\_s uv\_req\_t;
typedef struct uv\_work\_s uv\_work\_t;
typedef struct uv\_fs\_s uv\_fs\_t;

Note: In handles, **uv\_xxx\_t** inherits from **uv\_handle\_t**. In requests, **uv\_work\_t** inherits from **uv\_req\_t**.

It is critical to understand the handles in libuv and manage its lifecycle. Observe the following when using a handle:

-   Perform the handle initialization in the event loop thread.
-   If the handle needs to be initialized in a worker thread due to service requirements, use an atomic variable to check whether the initialization is complete before the handle is used.
-   For the handle that is no longer used, call **uv\_close** to remove it from the loop.

Note that **uv\_close** is used to close a handle asynchronously. Its prototype is as follows:

void uv\_close(uv\_handle\_t\* handle, uv\_close\_cb close\_cb)

Where:

-   **handle**: pointer to the handle to close.
-   **close\_cb**: function used to process the handle. This function is used to perform operations such as memory management.

After **uv\_close** is called, the handle to be closed is added to the **closing\_handles** queue in the loop, and waits for the loop thread to run **uv\_\_run\_closing\_handles**. Finally, the **close\_cb** callback is executed in the next iteration of the loop. Therefore, operations such as memory release should be performed in **close\_cb**. Improper use of the **close** API that is executed asynchronously may cause multithreading issues. You need to ensure correct timing of **uv\_close** and ensure that all the handles are closed before **close\_cb** is executed.

Tips: The following rule of thumb in the [official libuv documentation](http://libuv.org/) needs to be observed. If a handle of type **uv\_foo\_t** has a **uv\_foo\_start()** function, then it is active from the moment that function is called. Likewise, **uv\_foo\_stop()** deactivates the handle again.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4f/v3/dqgLVyzuSTiaCuany0PKbw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062528Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=7CE5F313E2103A011B07EAF60733BCD04AFC6EFC18EF6792375ECAE3C3C3D2EC)

-   Call **uv\_close** before all handles are closed, and all memory operations must be performed in **close\_cb** of **uv\_close**.
    
-   All handle operations cannot be called on non-loop threads by obtaining the loop of other threads.
    

When asynchronous tasks are submitted, the libuv requests that are dynamically acquired must be released in the **complete()** callback executed on the loop thread. The following uses **uv\_work\_t** as an example.

uv\_work\_t\* work = new uv\_work\_t;
uv\_queue\_work(loop, work, \[\](uv\_work\_t\* req) {
    // Asynchronous operation
}, \[\](uv\_work\_t\* req, int status) {
    // Callback
    delete req;
});

## Using libuv Timers

Observe the following when using the libuv timers:

-   Do not use libuv APIs (**uv\_timer\_start**, **uv\_timer\_stop**, and **uv\_timer\_again**) in multiple threads to operate the timer heap of the same loop simultaneously. Otherwise, the application may crash. To use libuv APIs to operate timers, perform the operations on the thread associated with the current **env**'s loop.
-   To throw a timer to a thread, use **uv\_async\_send**.

**Incorrect Example**

In the following example, operations on the timer heap of the same loop are performed in multiple threads at the same time, which poses a high crash rate.

ArkTS side:

import { hilog } from '@kit.PerformanceAnalysisKit';
import testNapi from 'libentry.so'

function waitforRunner(): number {
    "use concurrent"
    hilog.info(0xff, "testTag", "executed");
    return 0;
}

@Entry
@Component
struct Index {
  build() {
    Row() {
      Column() {
        Button("TimerTest")
          .width('40%')
          .fontSize('14fp')
          .onClick(() => {
            let i: number = 20;
            while (i--) {
              setTimeout(waitforRunner, 200);
              testNapi.testTimer();
          }
        }).margin(20)
      }.width('100%')
    }.height('100%')
  }
}

Native C++:

#include <napi/native\_api.h>
#include <uv.h>
#define LOG\_DOMAIN 0x0202
#define LOG\_TAG "MyTag"
#include "hilog/log.h"
#include <thread>
#include <unistd.h>

static napi\_value TestTimer(napi\_env env, napi\_callback\_info info)
{
    uv\_loop\_t\* loop = nullptr;
    uv\_timer\_t\* timer = new uv\_timer\_t;
    
    napi\_get\_uv\_event\_loop(env, &loop);
    uv\_timer\_init(loop, timer);
    std::thread t1(\[&loop, &timer\](){
        uv\_timer\_start(timer, \[\](uv\_timer\_t\* timer){
            uv\_timer\_stop(timer);
        }, 1000, 0);
    });
    
    t1.detach();
    return 0;
}

EXTERN\_C\_START
static napi\_value Init(napi\_env env, napi\_value exports)
{
    napi\_property\_descriptor desc\[\] = {
        {"testTimer", nullptr, TestTimer, nullptr, nullptr, nullptr, napi\_default, nullptr},
    };
    napi\_define\_properties(env, exports, sizeof(desc) / sizeof(desc\[0\]), desc);
    return exports;
}
EXTERN\_C\_END
    
static napi\_module demoModule = {
    .nm\_version = 1,
    .nm\_flags = 0,
    .nm\_filename = nullptr,
    .nm\_register\_func = Init,
    .nm\_modname = "entry",
    .nm\_priv = ((void \*)0),
    .reserved = {0},
};

extern "C" \_\_attribute\_\_((constructor)) void RegisterEntryModule(void)
{
    napi\_module\_register(&demoModule);
}

Add the following code to **index.d.ts**:

export const testTimer:() => number;

**Correct Example**

**Case 1**: Ensure that timer-related operations are performed on the JS main thread. Modify the **TestTimer()** function used in the previous example as follows:

static napi\_value TestTimer(napi\_env env, napi\_callback\_info info)
{
    uv\_loop\_t\* loop = nullptr;
    uv\_timer\_t\* timer = new uv\_timer\_t;
    
    napi\_get\_uv\_event\_loop(env, &loop);
    uv\_timer\_init(loop, timer);
    uv\_timer\_start(timer, \[\](uv\_timer\_t\* timer){
        uv\_timer\_stop(timer);
    }, 1000, 0);

    return 0;
}

**Case 2**: To throw a timer to a child thread, use the thread-safe function **uv\_async\_send**.

ArkTS side:

import { hilog } from '@kit.PerformanceAnalysisKit';
import testNapi from 'libentry.so'

@Entry
@Component
struct Index {
  build() {
    Row() {
      Column() {
        Button("TestTimerAsync")
          .width('40%')
          .fontSize('14fp')
          .onClick(() => {
              testNapi.testTimerAsync();  // Initialize the async handle.
        }).margin(20)
          
          Button("TestTimerAsyncSend")
          .width('40%')
          .fontSize('14fp')
          .onClick(() => {
              testNapi.testTimerAsyncSend(); // Call uv\_async\_send from a child thread to submit the timer task.
        }).margin(20)
      }.width('100%')
    }.height('100%')
  }
}

Native side:

#include <napi/native\_api.h>
#include <uv.h>
#define LOG\_DOMAIN 0x0202
#define LOG\_TAG "MyTag"
#include "hilog/log.h"
#include <thread>
#include <unistd.h>
uv\_async\_t\* async = new uv\_async\_t;

// Create a timer.
void async\_cb(uv\_async\_t\* handle)
{
    auto loop = handle->loop;
    uv\_timer\_t\* timer = new uv\_timer\_t;
    uv\_timer\_init(loop, timer);
    
    uv\_timer\_start(timer, \[\](uv\_timer\_t\* timer){
        uv\_timer\_stop(timer);
    }, 1000, 0);
}

// Initialize the async handle and bind the corresponding callback.
static napi\_value TestTimerAsync(napi\_env env, napi\_callback\_info info)
{
    uv\_loop\_t\* loop = nullptr;
    napi\_get\_uv\_event\_loop(env, &loop);
    uv\_async\_init(loop, async, async\_cb);
    return 0;
}

static napi\_value TestTimerAsyncSend(napi\_env env, napi\_callback\_info info)
{
    std::thread t(\[\](){
        uv\_async\_send (async); // Call uv\_async\_send in a child thread to instruct the main thread to call timer\_cb associated with async.
    });
    t.detach();
    return 0;
}

EXTERN\_C\_START
static napi\_value Init(napi\_env env, napi\_value exports)
{
    napi\_property\_descriptor desc\[\] = {
        {"testTimerAsync", nullptr, TestTimerAsync, nullptr, nullptr, nullptr, napi\_default, nullptr},
        {"testTimerAsyncSend", nullptr, TestTimerAsyncSend, nullptr, nullptr, nullptr, napi\_default, nullptr},
    };
    napi\_define\_properties(env, exports, sizeof(desc) / sizeof(desc\[0\]), desc);
    return exports;
}
EXTERN\_C\_END
    
static napi\_module demoModule = {
    .nm\_version = 1,
    .nm\_flags = 0,
    .nm\_filename = nullptr,
    .nm\_register\_func = Init,
    .nm\_modname = "entry",
    .nm\_priv = ((void \*)0),
    .reserved = {0},
};

extern "C" \_\_attribute\_\_((constructor)) void RegisterEntryModule(void)
{
    napi\_module\_register(&demoModule);
}

Add the following code to **index.d.ts**:

export const testTimerAsync:() => number;
export const testTimerAsyncSend:() => number;

## Inter-Thread Communication

So far, you have acquainted yourself with the basic concepts of libuv. Now let's dive into the inter-thread communication in libuv.

The inter-thread communication of libuv is implemented based on the **uv\_async\_t** handle. The related APIs are as follows:

int uv\_async\_init(uv\_loop\_t\* loop, uv\_async\_t\* handle, uv\_async\_cb async\_cb)

Initializes a handle.

-   **loop**: pointer to the event loop.
    
-   **handle**: pointer to the handle for inter-thread communication.
    
-   **async\_cb**: callback to be invoked.
    
    This API returns **0** if the operation is successful; returns an error code if the operation fails.
    

int uv\_async\_send(uv\_async\_t\* handle)

Wakes up the event loop and calls the async handle's callback.

-   **handle**: pointer to the handle for inter-thread communication.
    
    This API returns **0** if the operation is successful; returns an error code if the operation fails.
    

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/41/v3/n56SonZVQ_e6gauPdA-bUQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062528Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=C5A9C41AF111B9B6A34DF4D7272D6AE5A906FE79A635212D2254DF0A317FE958)

-   **uv\_async\_t** remains active after **uv\_async\_init** is called till it is closed by **uv\_close**.
    
-   **uv\_async\_t** is executed in the sequence defined by **uv\_async\_init** instead of **uv\_async\_send**. Therefore, it is necessary to manage the timing according to the initialization sequence.
    

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/93/v3/ZtLArHr-SY29DugEsD-j8A/en-us_image_0000002537926386.jpg?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062528Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=6D1EBE549292BFF48C2AFC1C60A00761A881215AA44440D34DD7B9D60FA73305)

Example:

#include <iostream>
#include <thread>
#include "uv.h"

uv\_loop\_t\* loop = nullptr;
uv\_async\_t\* async = nullptr;
int g\_counter = 10;

void async\_handler(uv\_async\_t\* handle)
{
    std::cout << "ohos async print" << std::endl;
    if (--g\_counter == 0) {
        // Call uv\_close to close the async handle and release the memory in the main loop.
        uv\_close((uv\_handle\_t\*)async, \[\](uv\_handle\_t\* handle) {
            std::cout << "delete async" << std::endl;
            delete (uv\_async\_t\*)handle;
        });
    }
}

int main()
{
    loop = uv\_default\_loop();
    async = new uv\_async\_t;
    uv\_async\_init(loop, async, async\_handler);
    std::thread subThread(\[\]() {
        for (int i = 0; i < 10; i++) {
            usleep (100); // Avoid multiple calls to uv\_async\_send being executed only once.
            std::cout << i << "th: subThread triggered" << std::endl;
            uv\_async\_send(async);
        }
    });
    subThread.detach();
    return uv\_run(loop, UV\_RUN\_DEFAULT);
}

The sample code describes only a simple scenario. The procedure is as follows:

1.  Initialize the async handle in the main thread.
2.  Create a worker thread and trigger **uv\_async\_send** every 100 milliseconds. After **uv\_async\_send** is called 10 times, call **uv\_close** to close the async handle.
3.  Run the event loop on the main thread.

As indicated by the following information, each time **uv\_async\_send** is called, the main thread executes the callback.

0th:subThread triggered
ohos async print
1th:subThread triggered
ohos async print
2th:subThread triggered
ohos async print
3th:subThread triggered
ohos async print
4th:subThread triggered
ohos async print
5th:subThread triggered
ohos async print
6th:subThread triggered
ohos async print
7th:subThread triggered
ohos async print
8th:subThread triggered
ohos async print
9th:subThread triggered
ohos async print
delete async

## Thread Pool

The thread pool in libuv uses the member variable **wq\_async** in **uv\_loop\_t** to control the communication between the main thread and worker threads. The core API is as follows:

int uv\_queue\_work(uv\_loop\_t\* loop,
                  uv\_work\_t\* req,
                  uv\_work\_cb work\_cb,
                  uv\_after\_work\_cb after\_work\_cb)

Initializes a work request which will run the given **work\_cb** in a thread from the thread pool.

-   **work\_cb**: task submitted to the worker thread.
    
-   **after\_work\_cb**: callback to be executed by the loop thread.
    

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7f/v3/C8YCiO1cStCn7aI2OO9OnA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062528Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=D699B02F115F2B6F3C5D7A6BE78B85357AC11D343AA8D930834B4B84CAEB133A)

**after work\_cb** is called after **work\_cb** is complete. It is triggered by an FD event triggered by **uv\_async\_send(loop->wq\_async)** and executed in the next iteration of the loop thread. The **uv\_work\_t** lifecycle ends only when **after\_work\_cb** is executed.

**Submitting Asynchronous Tasks**

The following figure illustrates a simplified workflow of the native libuv thread pool. The default pending flag of the handle is 1. The number of worker threads is an example only.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/36/v3/OcjOX7PjSJaopn_kFZcOlA/en-us_image_0000002568686163.jpg?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062528Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=BE61FC4BA5F52D55D87D7B990F5A647BB9BAA94908F3F5F84FB8A671577E4A35)

**Precautions for Submitting Asynchronous Tasks**

In HarmonyOS, **uv\_queue\_work()** in a UI thread works as follows: Throw **work\_cb** to the thread pool of the related priority of Function Flow Runtime (FFRT) and wait for FFRT to schedule and execute the task; throw **after\_work\_cb** to the event queue of **eventhandler** with the corresponding priority, wait for **eventhandler** to schedule, and return to the loop thread for execution. Note: After **uv\_queue\_work()** is called, it does not mean any task is complete. It only means **work\_cb()** is inserted into the thread pool of the related priority of FFRT. The workflow of the taskpool and jsworker threads is the same as that of native libuv.

In special cases, for example, in memory-sensitive cases, the same request can be used repeatedly when:

-   The sequence of the same type of tasks is ensured.
    
-   The request can be successfully released when **uv\_queue\_work** is called the last time.
    

uv\_work\_t\* work = new uv\_work\_t;
uv\_queue\_work(loop, work, \[\](uv\_work\_t\* work) {
        // Do something.
    },
    \[\](uv\_work\_t\* work, int status) {
        // Do something.
        uv\_queue\_work(loop, work, \[\](...) {/\* do something\*/}, \[\](...) {
            // Do something.
            if (last\_task) {  // Release the request after the last task is executed.
                delete work;
            }
        });
    },
    )

**Constraints of Using uv\_queue\_work()**

**uv\_queue\_work()** is only used to throw asynchronous tasks. The **execute()** callback of an asynchronous task added to the thread pool will be scheduled and executed. Therefore, it does not guarantee that tasks and their callbacks submitted multiple times will be executed in the order they were submitted.

**uv\_queue\_work()** can be called only on the loop thread. This prevents multi-threading issues. Do not use **uv\_queue\_work()** as a means for inter-thread communication. Specifically, do not use **uv\_queue\_work** to throw an asynchronous task from thread A to thread B, setting **execute()** to an empty task and executing the **complete()** callback on thread B. This approach is not only inefficient but increases the difficulty in locating faults. To avoid inefficient task submission, use [napi\_threadsafe\_function](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/use-napi-thread-safety).

## Use of libuv in HarmonyOS

Currently, libuv threads are used in the main thread, JS Worker thread, TaskWorker thread in the Taskpool, and IPC thread of HarmonyOS. Except the main thread, which uses **eventhandler** as the main loop, other threads use the **UV\_RUN\_DEFAULT** mode in libuv as the event main loop of the calling thread to execute tasks. In the main thread, **eventhandler** triggers task execution by an FD event. **eventhandler** listens for **backend\_fd** in **uv\_loop**. Once an FD event is triggered in the loop, **eventhandler** calls **uv\_run** to execute tasks in libuv.

As a result, all the libuv APIs that are not triggered by an FD event in the main thread are not responded in a timely manner. The libuv APIs on the JS worker threads work as expected.

In addition, in the application main thread, all asynchronous tasks are eventually executed through libuv. However, in the current system, the libuv thread pool has been incorporated to the FFRT. Any asynchronous task thrown to the libuv thread will be scheduled by the FFRT thread. The callbacks of the application main thread are also inserted into the **eventhandler** queue by **PostTask()**. This means that after the async task in an FFRT thread is complete, the callback of the main thread is not triggered by **uv\_async\_send**. The following figure shows the process.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/de/v3/KzhBMbYmRAuh5St9jlO4qQ/en-us_image_0000002568766173.jpg?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062528Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=E1C3FEAE87169658A110D38F4A8986DD34ED3E1486BBE236EF50866CC0B1E480)

The following types of requests can be processed as expected in the application main loop:

-   uv\_random\_t
    
    Function prototype:
    
    /\*\*
    \* @brief Adds a work request to an event loop queue.
    \*
    \* @param loop Pointer to the event loop.
    \* @param req Pointer to the request.
    \* @param buf Buffer for storing the random number.
    \* @param buflen Length of the buffer.
    \* @param flags Options for generating a random number. The value is an unsigned integer.
    \* @param cb Callback used to return the random number generated.
    \*
    \* @return Returns 0 if the operation is successful; returns an error code otherwise.
    \*/
    int uv\_random(uv\_loop\_t\* loop,
                 uv\_random\_t\* req,
                 void\* buf,
                 size\_t buflen,
                 unsigned flags,
                 uv\_random\_cb cb);
    
-   uv\_work\_t
    
    Function prototype:
    
    /\*\*
    \* @brief Adds a work request to an event loop queue. \*\*work\_cb\*\* will be called by a new thread in the next iteration of the event loop. When \*\*work\_cb\*\* is complete, \*\*after\_work\_cb\*\* will be called on the event loop thread.
    \*
    \* @param loop Pointer to the event loop.
    \* @param req Pointer to the work request.
    \* @param work\_cb Callback to be executed on a new thread.
    \* @param after\_work\_cb Callback to be invoked on the event loop thread.
    \*
    \* @return Returns 0 if the operation is successful; returns -1 otherwise.
    \*/
    int uv\_queue\_work(uv\_loop\_t\* loop,
                      uv\_work\_t\* req,
                      uv\_work\_cb work\_cb,
                      uv\_after\_work\_cb after\_work\_cb);
    
-   uv\_fs\_t
    
    All asynchronous APIs provided by the file class can work as expected in the application main thread. Common APIs include the following:
    
    /\*\*
    \* @brief Reads a file asynchronously.
    \*
    \* @param loop Pointer to the event loop.
    \* @param req Pointer to the file operation request.
    \* @param file File descriptor.
    \* @param bufs An array of buffers for storing the data read.
    \* @param nbufs Number of buffers.
    \* @param off Offset in the file from which data is read.
    \* @param cb Callback to be invoked when the read operation is complete.
    \* @return Returns 0 if the operation is successful; returns -1 otherwise.
    \*/
    int uv\_fs\_read(uv\_loop\_t\* loop, uv\_fs\_t\* req,
                  uv\_file file,
                  const uv\_buf\_t bufs\[\],
                  unsigned int nbufs,
                  int64\_t off,
                  uv\_fs\_cb cb);
    
    /\*\*
    \* @brief Opens a file asynchronously.
    \*
    \* @param loop Pointer to the event loop.
    \* @param req Pointer to the file operation request.
    \* @param path Pointer to the path of the file to open.
    \* @param flags Modes for opening the file.
    \* @param mode Permission on the file.
    \* @param cb Callback to be invoked when the file is opened.
    \*
    \* @return Returns 0 if the operation is successful; returns -1 otherwise.
    \*/
    int uv\_fs\_open(uv\_loop\_t\* loop,
                   uv\_fs\_t\* req,
                   const char\* path,
                   int flags,
                   int mode,
                   uv\_fs\_cb cb);
    
    /\*\*
    \* @brief Sends data from a file to another asynchronously.
    \*
    \* @param loop Pointer to the event loop.
    \* @param req Pointer to the file operation request.
    \* @param out\_fd File descriptor of the destination file.
    \* @param in\_fd File descriptor of the source file.
    \* @param off Offset in the source file from which data is sent.
    \* @param len Length of the data to be sent.
    \* @param cb Callback to be invoked when the data is sent.
    \*
    \* @return Returns 0 if the operation is successful; returns -1 otherwise.
    \*/
    int uv\_fs\_sendfile(uv\_loop\_t\* loop,
                       uv\_fs\_t\* req,
                       uv\_file out\_fd,
                       uv\_file in\_fd,
                       int64\_t off,
                       size\_t len,
                       uv\_fs\_cb cb);
    
    /\*\*
    \* @brief Writes data to a file asynchronously.
    \*
    \* @param loop Pointer to the event loop.
    \* @param req Pointer to the file operation request.
    \* @param file File descriptor.
    \* @param bufs An array of buffers for storing the data to be written.
    \* @param nbufs Number of buffers.
    \* @param off Offset in the file from which data is written.
    \* @param cb Callback to be invoked when the read operation is complete.
    \*
    \* @return Returns 0 if the operation is successful; returns -1 otherwise.
    \*/
    int uv\_fs\_write(uv\_loop\_t\* loop,
                    uv\_fs\_t\* req,
                    uv\_file file,
                    const uv\_buf\_t bufs\[\],
                    unsigned int nbufs,
                    int64\_t off,
                    uv\_fs\_cb cb);
    
    /\*\*
    \* @brief Copies a file asynchronously.
    \*
    \* @param loop Pointer to the event loop.
    \* @param req Pointer to the file operation request.
    \* @param path Pointer to the path of the file to copy.
    \* @param new\_path Pointer to the destination path.
    \* @param flags Options for the copy operation.
    \* @param cb Callback to be invoked when the copy operation is complete.
    \*
    \* @return Returns 0 if the operation is successful; returns -1 otherwise.
    \*/
    int uv\_fs\_copyfile(uv\_loop\_t\* loop,
                       uv\_fs\_t\* req,
                       const char\* path,
                       const char\* new\_path
                       int flags,
                       uv\_fs\_cb cb);
    
-   uv\_getaddrinfo\_t
    
    Function prototype:
    
    /\*\*
    \* @brief Obtains address information asynchronously.
    \*
    \* @param loop Pointer to the event loop.
    \* @param req Pointer to the request for obtaining address information.
    \* @param cb Callback to be invoked when the address information is obtained.
    \* @param hostname Pointer to the host name to resolve.
    \* @param service Pointer to the service name.
    \* @param hints Pointer to the address information with additional address type constraints.
    \*
    \* @return Returns 0 if the operation is successful; returns -1 otherwise.
    \*/
    int uv\_getaddrinfo(uv\_loop\_t\* loop,
                       uv\_getaddrinfo\_t\* req,
                       uv\_getaddrinfo\_cb cb,
                       const char\* hostname,
                       const char\* service,
                       const struct addrinfo\* hints);
    
-   uv\_getnameinfo\_t
    
    Function prototype:
    
    /\*\*
    \* @brief Obtains name information asynchronously.
    \*
    \* @param loop Pointer to the event loop.
    \* @param req Pointer to the request.
    \* @param getnameinfo\_cb Callback to be invoked when the name information is obtained.
    \* @param addr Pointer to the address information to resolve.
    \* @param flags Flags for controlling the behavior of the lookup.
    \*
    \* @return Returns 0 if the operation is successful; returns -1 otherwise.
    \*/
    int uv\_getnameinfo(uv\_loop\_t\* loop,
                       uv\_getnameinfo\_t\* req,
                       uv\_getnameinfo\_cb getnameinfo\_cb,
                       const struct sockaddr\* addr,
                       int flags);
    

The following APIs do not work as expected in the application main thread:

-   **Idle** handle
-   **prepare** handle
-   **check** handle
-   signal-related functions
-   Functions related to TCP and UDP
