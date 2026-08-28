# FAQs About Stability

#### How do I troubleshoot the issue that an application often crashes during running

-   Question: During Node-API development, an application often crashes, and the cpp crash stack is displayed. The stack top is the system library **libark\_jsruntime.so**, and the first few frames of the crash stack contain **libace\_napi.z.so**. How do I troubleshoot this issue?

The issue occurs frequently. The crash stack varies slightly each time, but the crash stack top is **libark\_jsruntime.so** or **libace\_napi.z.so** of the system library.

-   The crash information is as follows:

Reason:Signal:SIGSEGV(SEGV\_MAPERR)@0x00000136 probably caus
Fault thread info:
Tid:15894, Name:e.myapplication
#00 pc 002b8dd4 /system/lib/platformsdk/libark\_jsruntime.so
#01 pc 0024d3e1 /system/lib/platformsdk/libark\_jsruntime.so
#02 pc 0024d0d9 /system/lib/platformsdk/libark\_jsruntime.so
#03 pc 002eac5d /system/lib/platformsdk/libark\_jsruntime.so
#04 pc 00428d0f /system/lib/platformsdk/libark\_jsruntime.so

-   Answer:

If the application frequently crashes when the Node-API is used, and the crash stack top is in the system **library libark\_jsruntime.so**, the issue may be caused by improper use of the Node-API.

-   You can refer to the following troubleshooting methods:

1.  Check whether there are multi-thread safety issues, which are likely to occur.
    
    DevEco Studio provides a switch for checking multi-thread safety issues. After the switch is enabled, recompile, package, and run the code to check whether the crash stack complies with the description in the following topic. If yes, multi-thread safety problems occur when Node-API is used.
    
    Multi Thread Check in DevEco Studio:
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/97/v3/Q9PXLtsTTEiNQ7UFDES5yg/en-us_image_0000002568765021.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062132Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=6DA9BCA526996C7863E0C0853C3484ACA410DB95BE8DD6208CAA544C02015E50)
    
2.  Check whether the input parameter of the Node-API is invalid.
    

-   In this case, the .so file appears higher on the crash stack. The .so file calls a specific Node-API, for example, **napi\_call\_function**. Then, the Node-API calls **libark\_jsruntime .so**, and the crash occurs in **libark\_jsruntime**.

The following shows an example stack structure.

#01 /system/lib/platformsdk/libark\_jsruntime.so
#02 /system/lib/platformsdk/libark\_jsruntime.so
#03 /system/lib/platformsdk/libace\_napi.z.so(napi\_set\_named\_property+170) -- Node-API .so, which displays the failed API call.
#04 /data/storage/el1/bundle/libs/arm/libentry.so -- Your .so file.

-   If the input parameter is incorrect, the .so file usually appears high on the crash stack (it will not be far away from the stack top, such as #10). However, you can also refer to the following troubleshooting methods.
-   Troubleshooting methods:

a. Check whether the **napi\_value** is not initialized (the value is not assigned successfully, but is passed to the API as an invalid input parameter).

b. Check whether the error-prone API can be found by referring to the following topic.

#### How to handle thread safety issues when the ArkTS method is concurrently called in the thread pool

-   In an ArkTS class method, **napi\_ref** is created. To concurrently call the ArkTS method in the C++ thread pool, I have the following questions:

1.  Can the ArkTS class method cached by **napi\_ref** be called in the thread pool created by C++?
2.  How to ensure thread safety when ArkTS is called back?

Answer to question 1:

An ArkTS task can be thrown back to the ArkTS thread only in the C++ thread. In this case, the task is not called synchronously, but is thrown.

Note that the ArkTS method can be executed only on the ArkTS thread.

Answer to question 2:

As mentioned above, C++ threads throw tasks to ArkTS threads to execute ArkTS methods. For details about thread safety, see [Thread Safety Development Using Node-API](../../typical-node-api-use-cases/thread-safety-development-using-node-api/document.md).

In addition, you can enable the Ark multi-thread check during development to intercept multi-thread security issues.

#### What should I do if the content of napi\_value changes

-   Question: When a program is initialized, **env** and a method (**napi\_value**) are saved. The method is checked when it is created. The result of **napi\_typeof** is **napi\_function**, which meets the expectation. After the program runs for a period of time, the saved **env** and method fail to be checked, and the method is not a **napi\_function**. The **env** and method are saved and used in the same main thread. How to solve this problem?
    
-   Answer:
    

1.  Check whether **napi\_value** is used out of the scope.
    
2.  You are advised to use **napi\_ref** instead of **napi\_value**.
    

#### Is there a method to obtain the latest napi\_env

-   Question: The native layer needs to call an ArkTS method at a deeper layer and cannot pass **napi\_env** layer by layer. If **napi\_env** is directly cached, the system crashes. What should I do?

#00 /system/lib/platformsdk/libark\_jsruntime.so(panda::JSValueRef::IsFunction)
#01 /system/lib/platformsdk/libace\_napi.z.so(napi\_call\_function)
#02 /data/storage/el1/bundle/libs/arm/libentry.so
...

-   Answer:

1.  To save **napi\_env**, you can only pass it by calling functions layer by layer because Node-API does not provide the capability of directly obtaining **napi\_env**. You are not advised to save **napi\_env** due to the following reasons:
    
    -   If the **napi\_env**'s exit is not perceived, the **use-after-free** issue may occur.
        
    -   **napi\_env** is strongly bound to the ArkTS thread. If **napi\_env** is used by other ArkTS threads, multi-thread safety issues may occur.
        
    
    References:
    
    [Why cannot napi\_env be cached?](https://developer.huawei.com/consumer/en/doc/harmonyos-faqs/faqs-ndk-73)
    
2.  The key to this issue is as follows:
    
    To forcibly save the **env**, you can use the callback of **napi\_add\_env\_cleanup\_hook** to check whether the **env** exits. In addition, enable **Multi Thread Check** during development to avoid multi-thread safety issues.
    
3.  The crash may occur because the input parameter **func** is invalid when **napi\_call\_function** is called. You can check whether **napi\_value** is cached. The possible cause is that **napi\_value** exceeds the **napi\_handle\_scope** after being cached.
    
    To use similar logic, use **napi\_ref** for storage can prolong the lifecycle.
    
    References:
    
    [napi\_create\_reference, napi\_delete\_reference](../../node-api-guides/performing-lifecycle-management-using-node-api/document.md)
    

#### What should I do if napi\_add\_env\_cleanup\_hook is called incorrectly

-   Question: What should I do if an error is reported when **napi\_add\_env\_cleanup\_hook** or **napi\_remove\_env\_cleanup\_hook** is called?

When an error is reported when **napi\_add\_env\_cleanup\_hook** or **napi\_remove\_env\_cleanup\_hook** is called, the possible causes and logs are as follows:

1.  The two APIs are used outside the ArkTS thread to which **env** belongs, causing multi-thread safety issues. The error log "current napi interface cannot run in multi-thread" is reported.
2.  When **napi\_add\_env\_cleanup\_hook** is called, the same **args** is repeatedly used to register different callbacks. As a result, the registration fails. The third input parameter **args** of the API is used as the **key** value of the internal **map** of the API. When the callback of the same **args** is registered repeatedly, only the first registration is successful. If the registration fails, subsequent service functionalities may be abnormal or crash. The error log "AddCleanupHook Failed" is reported.
3.  When **napi\_remove\_env\_cleanup\_hook** is called, the callback is deleted using **args** that does not exist or has been deleted. The API fails to be called, and the error message "RemoveCleanupHook Failed" is displayed.

Example:

void AddEnvCleanupHook(napi\_env env)
{
    napi\_add\_env\_cleanup\_hook(env, \[\](void\* args) -> void {
        // Callback of the cleanup function.
    }, env); // env is a common data. Even if it is not repeatedly registered here, it may be registered in advance in other places. As a result, the registration fails.
}

static napi\_value Test(napi\_env env, napi\_callback\_info info)
{
    // First registration.
    AddEnvCleanupHook(env);
    // Second registration.
    AddEnvCleanupHook(env);
    return nullptr;
}

-   Answer:

1.  To ensure multi-thread safety, ensure that the API is called by the ArkTS thread to which **env** belongs.
2.  If the registration fails, you need to specify the function to be registered and ensure that the **key** value (the third input parameter of **napi\_add\_env\_cleanup\_hook**) is unique.
3.  If the deletion fails, ensure that **args** has been registered and not deleted.

References:

[Working with Cleanup Hooks Using Node-API](../../node-api-guides/working-with-cleanup-hooks-using-node-api/document.md)

#### What are the typical error scenarios of lifecycle-related development between napi\_open\_handle\_scope and napi\_close\_handle\_scope

-   Question: What should I do if the stability is affected when I use napi\_open\_handle\_scope and napi\_close\_handle\_scope to manage ArkTS objects?

Stability problems occur when **napi\_open\_handle\_scope** and **napi\_close\_handle\_scope** are incorrectly called. The common causes are as follows:

1.  **napi\_open\_handle\_scope** and **napi\_close\_handle\_scope** are not used in pairs. A scope is opened but not closed. As a result, memory leaks occur and the program may break down.
2.  The scopes are not closed in the reverse order of opening the scope. As a result, memory corruption may occur. In the scenario where **open\_scope1**, **open\_scope2**, **close\_scope1**, and **close\_scope2** are used, the pointer is returned after **close\_scope1** is called, which may overwrite the memory in **scope2** and cause memory corruption.
3.  The scope created in the native method is not closed before the method returns. As a result, the scope pairing is disordered during function reentry, causing stability issues.

Example:

#include "napi/native\_api.h"
#include <hilog/log.h>

// 1. Global scope
static napi\_handle\_scope g\_globalScope = nullptr;

static napi\_value CallFunction(napi\_env env, napi\_callback\_info info) {
    size\_t argc = 1;
    napi\_value argv\[1\] = {nullptr};
    napi\_get\_cb\_info(env, info, &argc, argv, nullptr, nullptr);
    
    napi\_valuetype type = napi\_undefined;
    if (argv\[0\] == nullptr || napi\_typeof(env, argv\[0\], &type) != napi\_ok || type != napi\_function) {
        OH\_LOG\_INFO(LOG\_APP, "Invalid JS function parameter");
        napi\_value errRet = nullptr;
        napi\_create\_int32(env, -1, &errRet);
        return errRet;
    }

    if (!g\_globalScope) {
        OH\_LOG\_INFO(LOG\_APP, "\[Initial call\] The global scope is empty. Open the scope.");
        napi\_open\_handle\_scope(env, &g\_globalScope);
        // Initial call: Execute the JS function.
        napi\_value global = nullptr;
        napi\_get\_global(env, &global);
        napi\_value result = nullptr;
        napi\_call\_function(env, global, argv\[0\], argc, argv, &result);
        return result; // Directly return the result for the initial call, and do not execute the subsequent close logic.
    } else {
        // Reentrant call: Return the fixed value and close the scope.
        napi\_value result = nullptr;
        napi\_create\_int32(env, 10, &result);
        OH\_LOG\_INFO(LOG\_APP, "\[Reentrant call\] The global scope is not empty. Close the scope.");
        napi\_close\_handle\_scope(env, g\_globalScope);
        g\_globalScope = nullptr;
        return result;
    }
}

API declaration

// index.d.ts
export const callFunction : (func : Function) => void;

ArkTS code:

import { hilog } from '@kit.PerformanceAnalysisKit';
import testNapi from 'libentry.so';

function reenterFunc(count = 1) : void{
  hilog.info(0x0000, 'testTag', \`\[JS\] Recursion\`);
  if (count <= 0) {
    return;
  }
  testNapi.callFunction(() => reenterFunc(count - 1));
  hilog.info(0x0000, 'testTag', \`\[JS\] Reentrant call\`);
  return;
}

try {
  testNapi.callFunction(reenterFunc);
  hilog.info(0x0000, 'testTag', '\[Execution completed\]');
} catch (error) {
  hilog.error(0x0000, 'testTag', \`Call error: ${error.message}\`);
}

CMakeLists.txt

cmake\_minimum\_required(VERSION 3.5.0)
project(Test)

set(NATIVERENDER\_ROOT\_PATH ${CMAKE\_CURRENT\_SOURCE\_DIR})

if(DEFINED PACKAGE\_FIND\_FILE)
    include(${PACKAGE\_FIND\_FILE})
endif()

include\_directories(${NATIVERENDER\_ROOT\_PATH}
                    ${NATIVERENDER\_ROOT\_PATH}/include)

add\_library(entry SHARED napi\_init.cpp)
add\_definitions( "-DLOG\_DOMAIN=0xd0d0" )
add\_definitions( "-DLOG\_TAG=\\"testTag\\"" )
target\_link\_libraries(entry PUBLIC libace\_napi.z.so libhilog\_ndk.z.so)

-   Answer:

1.  **napi\_open\_handle\_scope** and **napi\_close\_handle\_scope** must be used in pairs. Check whether they are used in pairs.
2.  All scopes must be closed in the reverse order of opening.
3.  All scopes created in the native method must be closed before the method returns.

References:

[Performing Lifecycle Management Using Node-API](../../node-api-guides/performing-lifecycle-management-using-node-api/document.md#napi_open_handle_scopenapi_close_handle_scope)
