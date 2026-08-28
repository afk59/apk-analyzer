# File Open Boost (C/C++)

Starting from version 5.0.3(15), the file open boost function has been added. Provides APIs for registration and unregistration, and allows apps to register a series of callback functions. The file open boost service recommends files to apps for preloading by calling the callback API.

#### API Description

For details about the APIs, please refer to the [API document of openFileBoost](https://developer.huawei.com/consumer/en/doc/harmonyos-references/openfileboost-index).

**Table 1** File preloading APIs (C API)
| 
API

 | 

Description

 |
| :-- | :-- |
| 

OpenFileBoost\_ErrCode HMS\_OpenFileBoost\_RegisterFilePreload(

HMS\_OpenFileBoost\_QueryAppState queryAppState,

HMS\_OpenFileBoost\_OnFilePreload filePreload,

HMS\_OpenFileBoost\_OnFilePreload cancelFilePreload);

 | 

Registers the file preloading callback with the system. The system predicts the files that may be opened by the user. Before notifying the preloading, the system calls **queryAppState** to query whether the preloaded files can be recommended. If the app returns a result indicating that the preloaded files can be recommended, the system calls **filePreload** to recommend a file to the app for preloading. In some scenarios, for example, the available memory of the system is insufficient or other files are more likely to be opened by the user, the system calls **cancelFilePreload** to cancel the preloading of some files.

 |
| 

typedef OpenFileBoost\_AppState (\*HMS\_OpenFileBoost\_QueryAppState)(void);

 | 

Called when the system queries the app status.

 |
| 

typedef OpenFileBoost\_CbErrCode (\*HMS\_OpenFileBoost\_OnFilePreload)(void\* fileInfo);

 | 

Called when the system recommends or cancels the recommendation of a preloaded file to an app.

 |
| 

OpenFileBoost\_ErrCode HMS\_OpenFileBoost\_GetFdFromPreloadFileInfo(

void\* fileInfo, int32\_t\* fd);

 | 

Called when the app obtains the file descriptor information in the callback context for recommending or canceling the recommendation of a preloaded file to the app.

 |
| 

OpenFileBoost\_ErrCode HMS\_OpenFileBoost\_GetSandboxPathFromPreloadFileInfo(

void\* fileInfo, char\* sandboxPath, int32\_t pathLen);

 | 

Called when the app obtains the file sandbox path information in the callback context for recommending or canceling the recommendation of a preloaded file to the app.

 |
| 

OpenFileBoost\_ErrCode HMS\_OpenFileBoost\_UnregisterFilePreload(void);

 | 

Unregisters the preloading callback.

 |
| 

OpenFileBoost\_ErrCode HMS\_OpenFileBoost\_NotifyPreloadHit(

int32\_t fd, char\* sandboxPath, int32\_t pathLen);

 | 

Called to notify the system of the preloading hit when a user opens a preloaded file. This helps improve the prediction accuracy of file preloading.

 |

#### Getting Started

Use [Syscap](< https://developer.huawei.com/consumer/en/doc/harmonyos-references/syscap#checking-whether-an-api-is-available>) to check whether the target device supports the **SystemCapability.PCService.OpenFileBoost** system capability. Currently, this capability is supported only on 2-in-1 devices.

#### Development Procedure

1.  Apply for the corresponding permission of the file open boost service and add the file preloading permission to the **module.json5** file. Note that ohos.permission.PRELOAD\_FILE is a restricted permission. For details, please refer to [Requesting Restricted Permissions](../../../system/security/application-access-control/application-permission-management/requesting-application-permissions/requesting-restricted-permissions/document.md).
    
    "requestPermissions":\[
      {
        "name": "ohos.permission.PRELOAD\_FILE"
      }
    \]
    
2.  Add the corresponding header file.
    
    #include "PreviewKit/open\_file\_boost.h"
    
3.  Compile **CMakeLists.txt** and add the dependency on the file open boost function.
    
    target\_link\_libraries(entry PUBLIC
        libopen\_file\_boost.so
    )
    
4.  Register the file preloading callback. After the registration, the system calls the callback function to recommend files to an app when conditions are met.
    
    OpenFileBoost\_ErrCode ret = HMS\_OpenFileBoost\_RegisterFilePreload(AppQueryAppStateCb,
        AppOnFilePreload, AppCancelFilePreload);
    if (ret != OPEN\_FILE\_BOOST\_SUCCESS){
        // Registration fails. You can customize error handling.
    }
    
5.  The app should synchronously parse the preloaded file in the current callback context, or wait until the parsing is complete before returning the result. In this way, the system can evaluate the resource consumption of the preloaded file.
    
    // Callback for querying the current app status. Before recommending a file to an app, the system calls the status query callback function to query whether the app is suitable for file recommendation.
    OpenFileBoost\_AppState AppQueryAppStateCb(void)
    {
        // If file preloading is allowed, **OPEN\_FILE\_BOOST\_APP\_STATE\_ALLOW\_PRELOAD** is returned. **CanPreload** is a sample code. Actual codes that determine whether to allow file preloading may vary.
        if (CanPreload()) {
            return OPEN\_FILE\_BOOST\_APP\_STATE\_ALLOW\_PRELOAD;
        } else {
            return OPEN\_FILE\_BOOST\_APP\_STATE\_REJECT\_PRELOAD;
        }
    }
    
    // File preloading callback.
    OpenFileBoost\_CbErrCode AppOnFilePreload(void\* fileInfo)
    {
        int32\_t fileDescriptor = 0;
        // The **fileInfo** pointer is valid only in the current callback context. Call **HMS\_OpenFileBoost\_GetFdFromPreloadFileInfo** in the callback to obtain the file descriptor.
        OpenFileBoost\_ErrCode ret = HMS\_OpenFileBoost\_GetFdFromPreloadFileInfo(fileInfo, &fileDescriptor);
        if (ret != OPEN\_FILE\_BOOST\_SUCCESS) {
            return OPEN\_FILE\_BOOST\_CALLBACK\_FAILURE;
        }
        char sandboxPath\[MAX\_BUFFER\_LENGTH\] = {0};
        // The **fileInfo** pointer is valid only in the current callback context. Call **HMS\_OpenFileBoost\_GetSandboxPathFromPreloadFileInfo** in the callback to obtain the file path.
        ret = HMS\_OpenFileBoost\_GetSandboxPathFromPreloadFileInfo(fileInfo, sandboxPath, MAX\_BUFFER\_LENGTH);
        if (ret != OPEN\_FILE\_BOOST\_SUCCESS) {
            return OPEN\_FILE\_BOOST\_CALLBACK\_FAILURE;
        }
        // You can save the file descriptor and file path so that the file preloading can be canceled when receiving a cancellation notification.
        // You can customize the logic for file preloading.
        return OPEN\_FILE\_BOOST\_CALLBACK\_SUCCESS;
    }
    
    // Callback for canceling preloading.
    OpenFileBoost\_CbErrCode AppCancelFilePreload(void\* fileInfo)
    {
        // Obtain the file descriptor and sandbox path in the same way.
        int32\_t fileDescriptor = 0;
        OpenFileBoost\_ErrCode ret = HMS\_OpenFileBoost\_GetFdFromPreloadFileInfo(fileInfo, &fileDescriptor);
        if (ret != OPEN\_FILE\_BOOST\_SUCCESS) {
            return OPEN\_FILE\_BOOST\_CALLBACK\_FAILURE;
        }
        char sandboxPath\[MAX\_BUFFER\_LENGTH\] = {0};
        ret = HMS\_OpenFileBoost\_GetSandboxPathFromPreloadFileInfo(fileInfo, sandboxPath, MAX\_BUFFER\_LENGTH);
        if (ret != OPEN\_FILE\_BOOST\_SUCCESS) {
            return OPEN\_FILE\_BOOST\_CALLBACK\_FAILURE;
        }
        // You can customize the logic for canceling file preloading.
        return OPEN\_FILE\_BOOST\_CALLBACK\_SUCCESS;
    }
    
6.  If you open a preloaded file, the app needs to call **HMS\_OpenFileBoost\_NotifyPreloadHit** to notify the system. This helps the system adjust the preloading status of the file.
    
    // Pass the descriptor, path, and length of the preloaded file you opened.
    OpenFileBoost\_ErrCode ret = HMS\_OpenFileBoost\_NotifyPreloadHit(fileDescriptor, sandboxPath, pathLen);
    if (ret != OPEN\_FILE\_BOOST\_SUCCESS){
        // Notification fails. You can customize error handling.
    }
    
7.  If you do not wish to receive the callback again or you are exiting the process, call the preloading cancellation API.
    
    OpenFileBoost\_ErrCode ret = HMS\_OpenFileBoost\_UnregisterFilePreload();
    if (ret != OPEN\_FILE\_BOOST\_SUCCESS){
        // Unregistration fails. You can customize error handling.
    }
