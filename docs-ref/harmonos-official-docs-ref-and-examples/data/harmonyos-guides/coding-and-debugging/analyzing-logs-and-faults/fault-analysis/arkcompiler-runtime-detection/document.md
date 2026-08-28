# ArkCompiler Runtime Detection

#### Multi Thread Check

In the JavaScript runtime environment, the safety of multi-threading is an important consideration. Since the JavaScript main thread is single-threaded, JS objects created in the main thread (especially DOM-related ones) can only be operated within it. Violating this rule can lead to multi-threading safety issues. Here are some detailed explanations on how to determine and handle these issues.

## Introduction

-   Single-threaded execution
    
    JavaScript is a single-threaded language, which means that it can only execute code on one thread at a time. Any JavaScript object can only be operated on the thread where it is created.
    
-   Node-API
    
    The Node-API is directly involved in the operation of JavaScript objects. The vast majority (about 95%) of Node-APIs can only be called on the JavaScript thread that created these objects.
    

-   Multi thread check mechanism
    
    The multi thread check mechanism detects whether the current thread is consistent with the JavaScript thread ID in the JavaScript virtual machine environment (**vm/env**) being used. If they are not consistent, it indicates that the virtual machine environment is being used across threads, and there is a multi-threading safety issue.
    

## Common Multi-threading Safety Issues

-   Non-JavaScript thread using Node-API
    
    A non-JavaScript thread attempting to call the Node-API may lead to undefined behavior or crashes.
    

-   Node-API using another thread's **env**:
    
    A thread attempting to use a JavaScript environment (**env**) created by another thread can also lead to multi-threading safety issues.
    

**How to determine whether a multi-threading safety issue has occurred:**

If you encounter the following fatal error message during runtime, it means a multi-threading safety issue has occurred:

Fatal: ecma\_vm cannot run in multi-thread! thread:3096 currentThread:3550

Here, **thread:3096** indicates the ID of the thread that created and owns this JavaScript environment. **currentThread:3550** indicates the ID of the thread that is trying to operate on this JavaScript environment.

The current thread number is 3550, and the JavaScript environment used is created by thread 3096. This indicates that the virtual machine environment (**vm/env**) is being used across threads, leading to a multi-threading safety issue.

## Enabling Multi Thread Check

You can enable multi thread check in either of the following ways:

-   **Method 1**
    
    Choose **Run** > **Edit Configurations** > **Diagnostics** and select **Multi Thread Check**.
    

-   **Method 2**
    
    Run the following command:
    
    aa start -a {abilityName} -b {bundleName} -R
    

## Using Multi Thread Check

1.  Run or debug the app.
2.  When a multi-threading safety issue occurs, the crash log message will be displayed. You can click the link provided in the message to navigate to the code that causes the issue. For details about how to analyze multi-threading safety issues, see [Analyzing Error Logs and Crashes Triggered by Using Node-API](../../../../ndk-development/code-development/using-node-api/typical-node-api-use-cases/analyzing-error-logs-and-crashes-triggered-by-using-node-api/document.md).
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3f/v3/M9_58vFuTwCRYzdPGbyoGg/en-us_image_0000002504092422.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062153Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=4F00A9C61B662A8C8FEAFFC753A01F4532A5DF183082545629AAEFBE8F06A973)
    

#### Enhanced Error Info

During ArkTS project development, there may be scenarios where native modules need to be loaded. To obtain more information from the error messages caused by loading native modules in ArkTS projects to facilitate your native code issue diagnosis, you can enable the Enhanced Error Info feature.

## Enabling Enhanced Error Info

To enable Enhanced Error Info, use either of the following methods:

-   Method 1
    
    Choose **Run** > **Edit Configurations** > **Diagnostics** and select **Enhanced Error Info**.
    

-   Method 2
    
    Run the following command:
    
    aa start {abilityName} {bundleName} -E
    

## Using Enhanced Error Info

1.  Run or debug the app.
2.  With Enhanced Error Info enabled, error messages due to native module loading display more detailed and accurate information.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b/v3/E-xohxvQQ3m-VQXjgCQYcQ/en-us_image_0000002501070380.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062153Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=CFDF4DAAFCD3A0AF868F296166D95B67C301FDF786F96EF847265DBC8477D8CD)
