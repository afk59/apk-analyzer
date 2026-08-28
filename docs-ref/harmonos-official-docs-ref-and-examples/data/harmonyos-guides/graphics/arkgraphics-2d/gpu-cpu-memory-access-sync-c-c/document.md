# GPU/CPU Memory Access Sync (C/C++)

#### Overview

NativeFence is a module that manages the sync status of **fenceFd**. You can use the APIs to set the blocking time, block **fenceFd** permanently, close **fenceFd**, and check the validity of **fenceFd**.

#### Available APIs

| Name | Description |
| :-- | :-- |
| OH\_NativeFence\_IsValid (int fenceFd) | Checks whether **fenceFd** is valid. |
| OH\_NativeFence\_Wait (int fenceFd, uint32\_t timeout) | Blocks the input **fenceFd**. The timeout parameter specifies the maximum waiting time. |
| OH\_NativeFence\_WaitForever (int fenceFd) | Permanently blocks the input **fenceFd**. |
| OH\_NativeFence\_Close (int fenceFd) | Closes **fenceFd**. |

For details about the APIs, see [NativeFence](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-nativefence).

#### How to Develop

The following describes how to use the native APIs provided by NativeFence.

**Adding Dynamic Link Libraries**

Add the following library file to the **CMakeLists.txt** file.

libnative\_fence.so

Header Files

#include <native\_fence/native\_fence.h>
#include <cstring>
#include <iostream>
#include <linux/sync\_file.h>
#include <signal.h>
#include <sys/signalfd.h>
#include <unistd.h>

1.  Call **signalfd()** to create **fenceFd**.
    
    sigset\_t mask;
    sigemptyset(&mask);
    sigaddset(&mask, SIGINT); // Monitor SIGINT signal (Ctrl C)
    sigaddset(&mask, SIGURG); // Generated when urgent data or out of band data arrives at the socket
    sigprocmask(SIG\_BLOCK, &mask, NULL);
    int sfd = signalfd(-1, &mask, 0);
    
2.  Check whether the input **fenceFd** is valid.
    
    bool isValid = OH\_NativeFence\_IsValid(INVALID\_FD);
    if (!isValid) {
        DRAWING\_LOGW("fenceFd is invalid");
    }
    
3.  Call the **OH\_NativeFence\_Wait** blocking API to wait for the fence to complete and then perform the next operation.
    
    constexpr uint32\_t TIMEOUT\_MS = 5000;
    // ···
    bool result = OH\_NativeFence\_Wait(INVALID\_FD, TIMEOUT\_MS);
    
4.  Call the **OH\_NativeFence\_WaitForever** blocking API to wait for the fence to complete and then perform the next operation.
    
    bool result2 = false;
    auto startTime = std::chrono::steady\_clock::now();
    result2 = OH\_NativeFence\_WaitForever(sfd);
    auto endTime = std::chrono::steady\_clock::now();
    auto duration = std::chrono::duration\_cast<std::chrono::milliseconds>(endTime - startTime).count();
    if (result2) {
        DRAWING\_LOGI("SyncFenceWaitForever has an event occurring result2 %{public}d, cost\_time: %{public}d",
            result2, duration);
    } else {
        DRAWING\_LOGI("SyncFenceWaitForever timeout with no event occurrence"
            "result2 %{public}d, cost\_time: %{public}d", result2, duration);
    }
    
5.  The GPU or CPU sends a sync signal to notify **fenceFd** of unblocking.
    
6.  Close **fenceFd**.
    
    OH\_NativeFence\_Close(sfd);
