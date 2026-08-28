# open\_file\_boost.h

#### Overview

Declares the set of APIs for enabling file open boost.

**Library**: libopen\_file\_boost.so

**System capability**: SystemCapability.PCService.OpenFileBoost

**Start version**: 5.0.3(15)

**Related module**: [Preview](../../../modules/preview/document.md)

#### Summary

#### \[h2\]Macro Definition

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

[MAX\_BUFFER\_LENGTH](../../../modules/preview/document.md#gaa8a8ed5c9e057542ff818fde39a94f07) 1024

 | 

Maximum length of the sandbox path.

 |

#### \[h2\]Types

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

typedef [OpenFileBoost\_AppState](../../../modules/preview/document.md#gafae4452b9e410d76236258ec57e0af62)(\*[HMS\_OpenFileBoost\_QueryAppState](../../../modules/preview/document.md#ga8de1d5d3db37e7701a91f24a56dee641)) (void)

 | 

Called when the system queries the app status. This function calls back the app before calling the [HMS\_OpenFileBoost\_OnFilePreload](../../../modules/preview/document.md#ga7cb236400dadbd94b0586c7f234ad23b) recommendation file. This function is used to query whether the app is suitable for file recommendation. For example, if the app is in the foreground focus or in certain special states and is not suitable for preloading files, the app returns a specific enumerated value to reject preloading.

 |
| 

typedef [OpenFileBoost\_CbErrCode](../../../modules/preview/document.md#ga773c6beb8645cfe54e1ce7eab67b8161)(\*[HMS\_OpenFileBoost\_OnFilePreload](../../../modules/preview/document.md#ga7cb236400dadbd94b0586c7f234ad23b)) (void\* fileInfo)

 | 

Called when the system recommends or cancels the recommendation of a preloaded file to an app. The system predicts the files that may be opened by the user and notifies the app through the callback function. In some scenarios, for example, the available memory of the system is insufficient or other files are more likely to be opened by the user, the system instructs the app to cancel the preloading of some files.

 |

#### \[h2\]Enumerations

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

[OpenFileBoost\_ErrCode](../../../modules/preview/document.md#ga5716dcdf88f1609b3466aadc675a0efc) {

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

[OpenFileBoost\_CbErrCode](../../../modules/preview/document.md#ga773c6beb8645cfe54e1ce7eab67b8161) {

OPEN\_FILE\_BOOST\_CALLBACK\_SUCCESS = 0,

OPEN\_FILE\_BOOST\_CALLBACK\_FAILURE = 1017210000

}

 | 

Enumerates the error code for the callback function [HMS\_OpenFileBoost\_OnFilePreload](../../../modules/preview/document.md#ga7cb236400dadbd94b0586c7f234ad23b). It is used by the app to return the callback function execution result to the system.

 |
| 

[OpenFileBoost\_AppState](../../../modules/preview/document.md#gafae4452b9e410d76236258ec57e0af62) {

OPEN\_FILE\_BOOST\_APP\_STATE\_ALLOW\_PRELOAD = 0,

OPEN\_FILE\_BOOST\_APP\_STATE\_REJECT\_PRELOAD = 1,

OPEN\_FILE\_BOOST\_APP\_STATE\_FOREVER\_REJECT\_PRELOAD = 2

}

 | 

Enumerates the app status, indicating whether the app allows the system to recommend preloaded files.

 |

#### \[h2\]Functions

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

[OpenFileBoost\_ErrCode](../../../modules/preview/document.md#ga5716dcdf88f1609b3466aadc675a0efc) [HMS\_OpenFileBoost\_GetFdFromPreloadFileInfo](../../../modules/preview/document.md#ga13429f2e33ddd0805274b46223a3f5b3) (void\* fileInfo, int32\_t\* fd)

 | 

Obtains the file descriptor information.

 |
| 

[OpenFileBoost\_ErrCode](../../../modules/preview/document.md#ga5716dcdf88f1609b3466aadc675a0efc) [HMS\_OpenFileBoost\_GetSandboxPathFromPreloadFileInfo](../../../modules/preview/document.md#ga16b482acdc9b56ebd8d01efed6875e95) (void\* fileInfo, char\* sandboxPath, int32\_t pathLen)

 | 

Obtains the sandbox path information.

 |
| 

[OpenFileBoost\_ErrCode](../../../modules/preview/document.md#ga5716dcdf88f1609b3466aadc675a0efc) [HMS\_OpenFileBoost\_RegisterFilePreload](../../../modules/preview/document.md#ga0ff9ab52e40e265bc90a9cca779d0fd1) ([HMS\_OpenFileBoost\_QueryAppState](../../../modules/preview/document.md#ga8de1d5d3db37e7701a91f24a56dee641) queryAppState, [HMS\_OpenFileBoost\_OnFilePreload](../../../modules/preview/document.md#ga7cb236400dadbd94b0586c7f234ad23b) filePreload, [HMS\_OpenFileBoost\_OnFilePreload](../../../modules/preview/document.md#ga7cb236400dadbd94b0586c7f234ad23b) cancelFilePreload)

 | 

Registers the preloading callback.

 |
| 

[OpenFileBoost\_ErrCode](../../../modules/preview/document.md#ga5716dcdf88f1609b3466aadc675a0efc) [HMS\_OpenFileBoost\_UnregisterFilePreload](../../../modules/preview/document.md#gafdef9962cc4c394dad2103bd8c773e90) (void)

 | 

Unregisters the preloading callback.

 |
| 

[OpenFileBoost\_ErrCode](../../../modules/preview/document.md#ga5716dcdf88f1609b3466aadc675a0efc) [HMS\_OpenFileBoost\_NotifyPreloadHit](../../../modules/preview/document.md#ga613e9855b8e471157a522ba19bac4d5e) (int32\_t fd, char\* sandboxPath, int32\_t pathLen)

 | 

Called to notify the system of the preloading hit when a user opens a preloaded file. This helps improve the prediction accuracy of file preloading.

 |
