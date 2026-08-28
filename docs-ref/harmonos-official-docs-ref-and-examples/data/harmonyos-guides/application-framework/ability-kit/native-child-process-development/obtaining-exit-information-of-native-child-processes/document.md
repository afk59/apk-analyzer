# Obtaining Exit Information of Native Child Processes

#### When to Use

Starting from API version 20, parent processes can register a callback function to monitor child processes and obtain their abnormal exit information, facilitating further optimizations by the parent process. The child processes to be monitored must be created by calling [OH\_Ability\_StartNativeChildProcess](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-native-child-process-h#oh_ability_startnativechildprocess), [OH\_Ability\_StartNativeChildProcessWithConfigs](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-native-child-process-h#oh_ability_startnativechildprocesswithconfigs), or [startNativeChildProcess](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-app-ability-childprocessmanager#childprocessmanagerstartnativechildprocess13).

#### Available APIs

| Name | Description |
| :-- | :-- |
| [Ability\_NativeChildProcess\_ErrCode](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-native-child-process-h#ability_nativechildprocess_errcode) [OH\_Ability\_RegisterNativeChildProcessExitCallback](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-native-child-process-h#oh_ability_registernativechildprocessexitcallback) ([OH\_Ability\_OnNativeChildProcessExit](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-native-child-process-h#oh_ability_onnativechildprocessexit) onProcessExit) | Registers a callback function for detecting abnormal exit of a native child process. |
| [Ability\_NativeChildProcess\_ErrCode](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-native-child-process-h#ability_nativechildprocess_errcode) [OH\_Ability\_UnregisterNativeChildProcessExitCallback](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-native-child-process-h#oh_ability_unregisternativechildprocessexitcallback) ([OH\_Ability\_OnNativeChildProcessExit](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-native-child-process-h#oh_ability_onnativechildprocessexit) onProcessExit) | Unregisters the callback function used for detecting abnormal exit of a native child process. |

#### How to Develop

**Linking Dynamic Libraries**

libchild\_process.so

**Including Header Files**

#include <AbilityKit/native\_child\_process.h>

1.  (Main process) Register and unregister the callback for abnormal exit of native child processes.
    
    Call [OH\_Ability\_RegisterNativeChildProcessExitCallback](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-native-child-process-h#oh_ability_registernativechildprocessexitcallback) to register a callback for detecting child process exits. If the return value is **NCP\_NO\_ERROR**, the registration is successful.
    
    Call [OH\_Ability\_UnregisterNativeChildProcessExitCallback](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-native-child-process-h#oh_ability_unregisternativechildprocessexitcallback) to unregister the callback used for detecting child process exits. If the return value is **NCP\_NO\_ERROR**, the unregistration is successful.
    
    #include <AbilityKit/native\_child\_process.h>
    #include <hilog/log.h>
    
    // ···
    
    void OnNativeChildProcessExit(int32\_t pid, int32\_t signal)
    {
        OH\_LOG\_INFO(LOG\_APP, "pid: %{public}d, signal: %{public}d", pid, signal);
    }
    
    void RegisterNativeChildProcessExitCallback()
    {
        Ability\_NativeChildProcess\_ErrCode ret =
            OH\_Ability\_RegisterNativeChildProcessExitCallback(OnNativeChildProcessExit);
        if (ret != NCP\_NO\_ERROR) {
            OH\_LOG\_ERROR(LOG\_APP, "register failed.");
        }
        // ···
    }
    
    void UnregisterNativeChildProcessExitCallback()
    {
        Ability\_NativeChildProcess\_ErrCode ret =
            OH\_Ability\_UnregisterNativeChildProcessExitCallback(OnNativeChildProcessExit);
        if (ret != NCP\_NO\_ERROR) {
            OH\_LOG\_ERROR(LOG\_APP, "unregister failed.");
        }
        // ···
    }
    
2.  (Main process) Add build dependencies.
    
    Modify the **CMaklist.txt** file to add the dependencies. The following assumes that the main process is implemented in the library file named **libmainprocesssample.so**. (The implementation of the main process and child processes can be compiled to the same dynamic link library file.)
    
    target\_link\_libraries(mainprocesssample PUBLIC
        # Add the dependency of the dynamic link library of Ability Kit.
        libchild\_process.so
        
        # Dependencies of other dynamic link libraries
        # ...
    )
