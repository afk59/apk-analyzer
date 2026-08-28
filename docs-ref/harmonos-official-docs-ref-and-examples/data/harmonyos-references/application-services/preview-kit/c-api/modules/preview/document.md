# Preview

#### Overview

Preview Kit provides a convenient file preview function for apps. Apps can use the preview APIs provided by Preview Kit to quickly display the preview page, so that users can preview various types of files.

The C APIs provide the file open boost function, which allows apps to load files in advance, shortening the file opening time and providing smooth and seamless experience for users.

For details, please refer to [File Open Boost (C/C++)](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/preview-openfileboost).

**Start version**: 5.0.3(15)

#### Summary

#### \[h2\]Files

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

[open\_file\_boost.h](../../header-files-and-structs/header-files/open-file-boost-h/document.md)

 | 

Declares the set of APIs for enabling file open boost.

 |
| 

[preview\_kit.h](../../header-files-and-structs/header-files/preview-kit-h/document.md)

 | 

Declares all header files contained in Preview Kit.

 |

#### \[h2\]Macro Definition

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

[MAX\_BUFFER\_LENGTH](#gaa8a8ed5c9e057542ff818fde39a94f07) 1024

 | 

The sandbox path can contain a maximum of 1024 characters.

 |

#### \[h2\]Types

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

typedef [OpenFileBoost\_AppState](#gafae4452b9e410d76236258ec57e0af62)(\*[HMS\_OpenFileBoost\_QueryAppState](#ga8de1d5d3db37e7701a91f24a56dee641)) (void)

 | 

Called before [HMS\_OpenFileBoost\_OnFilePreload](#ga7cb236400dadbd94b0586c7f234ad23b) is called to recommend files. This function is used to query whether the app is suitable for file recommendation. For example, if the app is in the foreground focus or in certain special states and is not suitable for preloading files, the app returns a specific enumerated value to reject preloading.

 |
| 

typedef [OpenFileBoost\_CbErrCode](#ga773c6beb8645cfe54e1ce7eab67b8161)(\*[HMS\_OpenFileBoost\_OnFilePreload](#ga7cb236400dadbd94b0586c7f234ad23b)) (void\* fileInfo)

 | 

The system predicts the files that may be opened by the user and notifies the app through the callback function. In some scenarios, for example, the available memory of the system is insufficient or other files are more likely to be opened by the user, the system instructs the app to cancel the preloading of some files.

 |

#### \[h2\]Enumerations

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

[OpenFileBoost\_ErrCode](#ga5716dcdf88f1609b3466aadc675a0efc) {

OPEN\_FILE\_BOOST\_SUCCESS = 0,

OPEN\_FILE\_BOOST\_PERMISSION\_NOT\_GRANTED = 201,

OPEN\_FILE\_BOOST\_INVALID\_PARAM = 401,

OPEN\_FILE\_BOOST\_INTERNAL\_ERROR = 1017200001,

OPEN\_FILE\_BOOST\_INSUFFICIENT\_BUFFER = 1017200002,

OPEN\_FILE\_BOOST\_SERVICE\_UNAVAILABLE = 1017200003,

OPEN\_FILE\_BOOST\_NO\_MEMORY = 1017200004

}

 | 

Enumerates the error code for file open boost.

 |
| 

[OpenFileBoost\_CbErrCode](#ga773c6beb8645cfe54e1ce7eab67b8161) {

OPEN\_FILE\_BOOST\_CALLBACK\_SUCCESS = 0,

OPEN\_FILE\_BOOST\_CALLBACK\_FAILURE = 1017210000

}

 | 

Enumerates the error code for the callback function [HMS\_OpenFileBoost\_OnFilePreload](#ga7cb236400dadbd94b0586c7f234ad23b). It is used by the app to return the callback function execution result to the system.

 |
| 

[OpenFileBoost\_AppState](#gafae4452b9e410d76236258ec57e0af62) {

OPEN\_FILE\_BOOST\_APP\_STATE\_ALLOW\_PRELOAD = 0,

OPEN\_FILE\_BOOST\_APP\_STATE\_REJECT\_PRELOAD = 1,

OPEN\_FILE\_BOOST\_APP\_STATE\_FOREVER\_REJECT\_PRELOAD = 2

}

 | 

App status, indicating that the app allows, rejects, or permanently rejects the file preloading recommended by the system.

 |

#### \[h2\]Functions

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

[OpenFileBoost\_ErrCode](#ga5716dcdf88f1609b3466aadc675a0efc) [HMS\_OpenFileBoost\_GetFdFromPreloadFileInfo](#ga13429f2e33ddd0805274b46223a3f5b3) (void\* fileInfo, int32\_t\* fd)

 | 

Obtains the file descriptor information.

 |
| 

[OpenFileBoost\_ErrCode](#ga5716dcdf88f1609b3466aadc675a0efc) [HMS\_OpenFileBoost\_GetSandboxPathFromPreloadFileInfo](#ga16b482acdc9b56ebd8d01efed6875e95) (void\* fileInfo, char\* sandboxPath, int32\_t pathLen)

 | 

Obtains the sandbox path information.

 |
| 

[OpenFileBoost\_ErrCode](#ga5716dcdf88f1609b3466aadc675a0efc) [HMS\_OpenFileBoost\_RegisterFilePreload](#ga0ff9ab52e40e265bc90a9cca779d0fd1) ([HMS\_OpenFileBoost\_QueryAppState](#ga8de1d5d3db37e7701a91f24a56dee641) queryAppState, [HMS\_OpenFileBoost\_OnFilePreload](#ga7cb236400dadbd94b0586c7f234ad23b) filePreload, [HMS\_OpenFileBoost\_OnFilePreload](#ga7cb236400dadbd94b0586c7f234ad23b) cancelFilePreload)

 | 

Registers the preloading callback.

 |
| 

[OpenFileBoost\_ErrCode](#ga5716dcdf88f1609b3466aadc675a0efc) [HMS\_OpenFileBoost\_UnregisterFilePreload](#gafdef9962cc4c394dad2103bd8c773e90) (void)

 | 

Unregisters the preloading callback.

 |
| 

[OpenFileBoost\_ErrCode](#ga5716dcdf88f1609b3466aadc675a0efc) [HMS\_OpenFileBoost\_NotifyPreloadHit](#ga613e9855b8e471157a522ba19bac4d5e) (int32\_t fd, char\* sandboxPath, int32\_t pathLen)

 | 

Called to notify the system of the preloading hit when a user opens a preloaded file. This helps improve the prediction accuracy of file preloading.

 |

#### Macro Description

#### \[h2\]MAX\_BUFFER\_LENGTH

#define MAX\_BUFFER\_LENGTH   1024

**Description**

Maximum length of the sandbox path.

**Start version**: 5.0.3(15)

#### Type Description

#### \[h2\]HMS\_OpenFileBoost\_OnFilePreload

typedef [OpenFileBoost\_CbErrCode](#ga773c6beb8645cfe54e1ce7eab67b8161)(\*HMS\_OpenFileBoost\_OnFilePreload) (void\* fileInfo)

**Description**

Called when the system recommends or cancels the recommendation of a preloaded file to an app. The system predicts the files that may be opened by the user and notifies the app through the callback function. In some scenarios, for example, the available memory of the system is insufficient or other files are more likely to be opened by the user, the system instructs the app to cancel the preloading of some files.

**Start version**: 5.0.3(15)

**Parameters**:

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

fileInfo

 | 

Preloads file information. The app can call [HMS\_OpenFileBoost\_GetFdFromPreloadFileInfo](#ga13429f2e33ddd0805274b46223a3f5b3) to obtain the corresponding file descriptor information, and then call [HMS\_OpenFileBoost\_GetSandboxPathFromPreloadFileInfo](#ga16b482acdc9b56ebd8d01efed6875e95) to obtain the corresponding sandbox path information. The app must synchronously parse the preloaded file in the current callback context so that the system can evaluate the resource consumption of the preloaded file.

 |

**Returns**:

Function execution result. Returns **OPEN\_FILE\_BOOST\_CALLBACK\_SUCCESS** if the function is executed successfully; returns **OPEN\_FILE\_BOOST\_CALLBACK\_FAILURE** if the function fails to be executed.

#### \[h2\]HMS\_OpenFileBoost\_QueryAppState

typedef [OpenFileBoost\_AppState](#gafae4452b9e410d76236258ec57e0af62)(\*HMS\_OpenFileBoost\_QueryAppState) (void)

**Description**

Called when the system queries the app status. This function calls back the app before calling the [HMS\_OpenFileBoost\_OnFilePreload](#ga7cb236400dadbd94b0586c7f234ad23b) recommendation file. This function is used to query whether the app is suitable for file recommendation. For example, if the app is in the foreground focus or in certain special states and is not suitable for preloading files, the app returns a specific enumerated value to reject preloading.

**Start version**: 5.0.3(15)

**Returns**:

Returns **OPEN\_FILE\_BOOST\_APP\_STATE\_ALLOW\_PRELOAD** if the app allows file recommendation. Then the system calls [HMS\_OpenFileBoost\_OnFilePreload](#ga7cb236400dadbd94b0586c7f234ad23b) to preload the recommendation file. Returns **OPEN\_FILE\_BOOST\_APP\_STATE\_REJECT\_PRELOAD** if the app rejects the recommendation. Returns **OPEN\_FILE\_BOOST\_APP\_STATE\_FOREVER\_REJECT\_PRELOAD** if the app does not want to receive recommendations during this registration, and [HMS\_OpenFileBoost\_UnregisterFilePreload](#gafdef9962cc4c394dad2103bd8c773e90) should be called to cancel the registration as soon as possible.

#### Enumeration Type Description

#### \[h2\]OpenFileBoost\_AppState

enum [OpenFileBoost\_AppState](#gafae4452b9e410d76236258ec57e0af62)

**Description**

Enumerates the app status, indicating whether the app allows the system to recommend preloaded files.

**Start version**: 5.0.3(15)

| 
Enumerated Value

 | 

Description

 |
| :-- | :-- |
| 

OPEN\_FILE\_BOOST\_APP\_STATE\_ALLOW\_PRELOAD

 | 

The app allows the file preloading recommended by the system.

 |
| 

OPEN\_FILE\_BOOST\_APP\_STATE\_REJECT\_PRELOAD

 | 

The app rejects the file preloading recommended by the system.

 |
| 

OPEN\_FILE\_BOOST\_APP\_STATE\_FOREVER\_REJECT\_PRELOAD

 | 

The app permanently rejects the file preloading recommended by the system during this registration.

 |

#### \[h2\]OpenFileBoost\_CbErrCode

enum [OpenFileBoost\_CbErrCode](#ga773c6beb8645cfe54e1ce7eab67b8161)

**Description**

Enumerates the error code for the callback function [HMS\_OpenFileBoost\_OnFilePreload](#ga7cb236400dadbd94b0586c7f234ad23b). It is used by the app to return the callback function execution result to the system.

**Start version**: 5.0.3(15)

| 
Enumerated Value

 | 

Description

 |
| :-- | :-- |
| 

OPEN\_FILE\_BOOST\_CALLBACK\_SUCCESS

 | 

The callback function is successfully executed.

 |
| 

OPEN\_FILE\_BOOST\_CALLBACK\_FAILURE

 | 

The callback function fails to be executed.

 |

#### \[h2\]OpenFileBoost\_ErrCode

enum [OpenFileBoost\_ErrCode](#ga5716dcdf88f1609b3466aadc675a0efc)

**Description**

Enumerates the error code for file open boost.

**Start version**: 5.0.3(15)

| 
Enumerated Value

 | 

Description

 |
| :-- | :-- |
| 

OPEN\_FILE\_BOOST\_SUCCESS

 | 

Success.

 |
| 

OPEN\_FILE\_BOOST\_PERMISSION\_NOT\_GRANTED

 | 

Permission not granted.

 |
| 

OPEN\_FILE\_BOOST\_INVALID\_PARAM

 | 

Invalid input parameter.

 |
| 

OPEN\_FILE\_BOOST\_INTERNAL\_ERROR

 | 

Internal error.

 |
| 

OPEN\_FILE\_BOOST\_INSUFFICIENT\_BUFFER

 | 

Insufficient buffer.

 |
| 

OPEN\_FILE\_BOOST\_SERVICE\_UNAVAILABLE

 | 

Service unavailable.

 |
| 

OPEN\_FILE\_BOOST\_NO\_MEMORY

 | 

Insufficient memory.

 |

#### Function Description

#### \[h2\]HMS\_OpenFileBoost\_GetFdFromPreloadFileInfo()

[OpenFileBoost\_ErrCode](#ga5716dcdf88f1609b3466aadc675a0efc) HMS\_OpenFileBoost\_GetFdFromPreloadFileInfo (void\* fileInfo, int32\_t\* fd)

**Description**

Obtains the file descriptor information.

**Start version**: 5.0.3(15)

**Parameters**:

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

fileInfo

 | 

Information about the preloaded file recommended by the system to the app.

 |
| 

fd

 | 

File descriptor information of the preloaded file.

 |

**Returns**:

Function execution result. Returns **OPEN\_FILE\_BOOST\_SUCCESS** if the function is executed successfully; returns a specific error code if the function fails to be executed. For details, see [OpenFileBoost\_ErrCode](#ga5716dcdf88f1609b3466aadc675a0efc).

#### \[h2\]HMS\_OpenFileBoost\_GetSandboxPathFromPreloadFileInfo()

[OpenFileBoost\_ErrCode](#ga5716dcdf88f1609b3466aadc675a0efc) HMS\_OpenFileBoost\_GetSandboxPathFromPreloadFileInfo (void\* fileInfo, char\* sandboxPath, int32\_t pathLen)

**Description**

Obtains the sandbox path information.

**Start version**: 5.0.3(15)

**Parameters**:

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

fileInfo

 | 

Information about the preloaded file recommended by the system to the app.

 |
| 

sandboxPath

 | 

Information about the sandbox path of the preloaded file. The app should pass a pointer to a valid memory region, into which the system fills the sandbox path information.

 |
| 

pathLen

 | 

Length of the memory area used to fill in the sandbox path.

 |

**Returns**:

Function execution result. Returns **OPEN\_FILE\_BOOST\_SUCCESS** if the function is executed successfully; returns **OPEN\_FILE\_BOOST\_INSUFFICIENT\_BUFFER** if the input memory buffer is too small. For details about other errors, see [OpenFileBoost\_ErrCode](#ga5716dcdf88f1609b3466aadc675a0efc).

#### \[h2\]HMS\_OpenFileBoost\_NotifyPreloadHit()

[OpenFileBoost\_ErrCode](#ga5716dcdf88f1609b3466aadc675a0efc) HMS\_OpenFileBoost\_NotifyPreloadHit (int32\_t fd, char\* sandboxPath, int32\_t pathLen)

**Description**

Called to notify the system of the preloading hit when a user opens a preloaded file. This helps improve the prediction accuracy of file preloading.

**Start version**: 5.0.3(15)

**Parameters**:

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

fd

 | 

File descriptor information of the hit file.

 |
| 

sandboxPath

 | 

Sandbox path of the hit file.

 |
| 

pathLen

 | 

Length of the sandbox path.

 |

**Returns**:

Function execution result. Returns **OPEN\_FILE\_BOOST\_SUCCESS** if the function is executed successfully; returns a specific error code if the function fails to be executed. For details, see [OpenFileBoost\_ErrCode](#ga5716dcdf88f1609b3466aadc675a0efc).

#### \[h2\]HMS\_OpenFileBoost\_RegisterFilePreload()

[OpenFileBoost\_ErrCode](#ga5716dcdf88f1609b3466aadc675a0efc) HMS\_OpenFileBoost\_RegisterFilePreload ([HMS\_OpenFileBoost\_QueryAppState](#ga8de1d5d3db37e7701a91f24a56dee641) queryAppState, [HMS\_OpenFileBoost\_OnFilePreload](#ga7cb236400dadbd94b0586c7f234ad23b) filePreload, [HMS\_OpenFileBoost\_OnFilePreload](#ga7cb236400dadbd94b0586c7f234ad23b) cancelFilePreload)

**Description**

Registers the preloading callback.

**Start version**: 5.0.3(15)

**Parameters**:

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

queryAppState

 | 

Callback used for querying the app status. Before the preloading notification is sent, the callback function is invoked to query whether the preloading file can be recommended.

 |
| 

filePreload

 | 

Callback used for file preloading. The system predicts the files that may be opened by users and notifies the invoker through this callback function.

 |
| 

cancelFilePreload

 | 

Callback used for canceling file preloading. For example, when the available system memory is insufficient, the system notifies the invoker of canceling file preloading.

 |

**Returns**:

Function execution result. Returns **OPEN\_FILE\_BOOST\_SUCCESS** if the function is executed successfully; returns a specific error code if the function fails to be executed. For details, see [OpenFileBoost\_ErrCode](#ga5716dcdf88f1609b3466aadc675a0efc).

#### \[h2\]HMS\_OpenFileBoost\_UnregisterFilePreload()

[OpenFileBoost\_ErrCode](#ga5716dcdf88f1609b3466aadc675a0efc) HMS\_OpenFileBoost\_UnregisterFilePreload (void)

**Description**

Unregisters the preloading callback.

**Start version**: 5.0.3(15)

**Returns**:

Function execution result. Returns **OPEN\_FILE\_BOOST\_SUCCESS** if the function is executed successfully; returns a specific error code if the function fails to be executed. For details, see [OpenFileBoost\_ErrCode](#ga5716dcdf88f1609b3466aadc675a0efc).
