# ModuleInstall

#### Overview

This section describes the on-demand distribution capability provided by AppGallery Kit.

**Start version**: 5.0.2(14)

#### Summary

#### \[h2\]Files

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

[module\_install.h](../../header-file/module-install-h/document.md)

 | 

Declares the APIs provided by the on-demand distribution capability.

 |

#### \[h2\]Types

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

typedef struct [ModuleInstall\_InstalledModule](#osaccount_errcode) [ModuleInstall\_InstalledModule](#osaccount_errcode)

 | 

Module information.

 |
| 

typedef struct [ModuleInstall\_FetchModulesResult](#section115389533615) [ModuleInstall\_FetchModulesResult](#section115389533615)

 | 

Module installation result.

 |
| 

typedef struct [ModuleInstall\_StatusCallback](#section48269177812) [ModuleInstall\_StatusCallback](#section48269177812)

 | 

Module installation status callback.

 |
| 

typedef void (\*[ModuleInstall\_OnStatusCallback](#section9881414171010))(char \*bundleName, char \*eventInfo)

 | 

Callback listener.

 |

#### \[h2\]Enumerations

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

[ModuleInstall\_ErrCode](#osaccount_errcode-1)

 | 

Enumerates error codes.

 |
| 

[ModuleInstall\_InstallStatus](#section19925459265)

 | 

Enumerates installation statuses.

 |
| 

[ModuleInstall\_RequestCode](#section10742174163618)

 | 

Enumerates request codes.

 |
| 

[ModuleInstall\_TaskStatus](#section14463723193715)

 | 

Enumerates task statuses.

 |

#### \[h2\]Functions

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

[HMS\_ModuleInstall\_GetInstalledModule](#oh_osaccount_getname)

 | 

Queries whether a module has been installed.

 |
| 

[HMS\_ModuleInstall\_GetInstalledModuleName](#section19475184213526)

 | 

Obtains the module name.

 |
| 

[HMS\_ModuleInstall\_GetInstalledModuleType](#section39341746155513)

 | 

Obtains the module type.

 |
| 

[HMS\_ModuleInstall\_GetModuleInstallStatus](#section84699521566)

 | 

Obtains the module installation status.

 |
| 

[HMS\_ModuleInstall\_FetchModules](#section1533121613581)

 | 

Requests to download a module.

 |
| 

[HMS\_ModuleInstall\_GetFetchModulesRequestCode](#section191414113614)

 | 

Obtains the module download request code.

 |
| 

[HMS\_ModuleInstall\_GetFetchModulesTaskStatus](#section142448141910)

 | 

Obtains the module download task status.

 |
| 

[HMS\_ModuleInstall\_GetFetchModulesTaskId](#section979412409101)

 | 

Obtains the module download task ID.

 |
| 

[HMS\_ModuleInstall\_GetFetchModulesDesc](#section762681812121)

 | 

Obtains the module download description.

 |
| 

[HMS\_ModuleInstall\_GetFetchModules](#section55521545111313)

 | 

Obtains the name of the downloaded module.

 |
| 

[HMS\_ModuleInstall\_GetFetchModulesTotalSize](#section1071043411515)

 | 

Obtains the total size of the downloaded module.

 |
| 

[HMS\_ModuleInstall\_GetFetchModulesDownloadedSize](#section04641118168)

 | 

Obtains the downloaded size of the module.

 |
| 

[HMS\_ModuleInstall\_CancelTask](#section1177619221712)

 | 

Cancels a download task.

 |
| 

[HMS\_ModuleInstall\_ShowCellularDataConfirmation](#section1897653081720)

 | 

Displays a mobile data reminder pop-up.

 |
| 

[HMS\_ModuleInstall\_CreateStatusCallback](#section1710031151816)

 | 

Creates a callback for listening to the download progress.

 |
| 

[HMS\_ModuleInstall\_On](#section18492123951816)

 | 

Listens to the download progress.

 |
| 

[HMS\_ModuleInstall\_ReleaseStatusCallback](#section1541418516194)

 | 

Frees up the callback for listening to the download progress.

 |
| 

[HMS\_ModuleInstall\_Off](#section1260162551917)

 | 

Cancels the callback for listening to the download progress.

 |

#### Type Definition Description

#### \[h2\]ModuleInstall\_InstalledModule

typedef struct ModuleInstall\_InstalledModule ModuleInstall\_InstalledModule

**Description**

Module information.

**Start version**: 5.0.2(14)

#### \[h2\]ModuleInstall\_FetchModulesResult

typedef struct ModuleInstall\_FetchModulesResult ModuleInstall\_FetchModulesResult

**Description**

Module installation result.

**Start version**: 5.0.2(14)

#### \[h2\]ModuleInstall\_StatusCallback

typedef struct ModuleInstall\_StatusCallback ModuleInstall\_StatusCallback

**Description**

Module installation status callback.

**Start version**: 5.0.2(14)

#### \[h2\]ModuleInstall\_OnStatusCallback

typedef void (\*ModuleInstall\_OnStatusCallback)(char \*bundleName, char \*eventInfo)

**Description**

Callback listener.

**Start version**: 5.0.2(14)

#### Enumeration Type Description

#### \[h2\]ModuleInstall\_ErrCode

enum ModuleInstall\_ErrCode

**Description**

Enumerates error codes.

**Start version**: 5.0.2(14)

| 
Enumeration

 | 

Description

 |
| :-- | :-- |
| 

E\_NO\_ERROR = 0

 | 

Successful.

 |
| 

E\_PARAMS = 401

 | 

Invalid parameters.

 |
| 

E\_QUERY\_MODULE = 1006500001

 | 

Failed to call the API of the Bundle Manager Service (BMS).

 |
| 

E\_REPEATED\_CALL = 1006500002

 | 

The API is called repeatedly with the same input.

 |
| 

E\_CONNECT\_SA = 1006500004

 | 

Service exception.

 |
| 

E\_OFF\_WITHOUT\_ON = 1006500006

 | 

Not used together with the [HMS\_ModuleInstall\_On](#section18492123951816) API.

 |
| 

E\_CONNECT\_SERVICE\_EXTENSION = 1006500007

 | 

Failed to connect to the service.

 |
| 

E\_WRITE\_PARAM = 1006500008

 | 

Failed to write parameters.

 |
| 

E\_REQUEST\_SERVER = 1006500009

 | 

Failed to request the service.

 |
| 

E\_RESPONSE\_INVALID = 1006500010

 | 

Response parameters cannot be parsed.

 |
| 

E\_INNER\_ERROR = 1006500011

 | 

Internal error.

 |

#### \[h2\]ModuleInstall\_InstallStatus

enum ModuleInstall\_InstallStatus

**Description**

Enumerates installation statuses.

**Start version**: 5.0.2(14)

| 
Enumeration

 | 

Description

 |
| :-- | :-- |
| 

INSTALLED = 0

 | 

Installed.

 |
| 

NOT\_INSTALLED = 1

 | 

Not installed.

 |

#### \[h2\]ModuleInstall\_RequestCode

enum ModuleInstall\_RequestCode

**Description**

Enumerates on-demand module download request codes.

**Start version**: 5.0.2(14)

| 
Enumeration

 | 

Description

 |
| :-- | :-- |
| 

MODULE\_ALREADY\_EXISTS = -8

 | 

The specified module already exists.

 |
| 

MODULE\_UNAVAILABLE = -7

 | 

The module to be downloaded does not exist or does not adapt to the device.

 |
| 

INVALID\_REQUEST = -6

 | 

The request is invalid because the information contained in the request is incorrect.

 |
| 

NETWORK\_ERROR = -5

 | 

Request failed due to a network exception.

 |
| 

INVOKER\_VERIFICATION\_FAILED = -4

 | 

The caller information is abnormal.

 |
| 

FOREGROUND\_REQUIRED = -3

 | 

On-demand loading is allowed only when the app is running in the foreground.

 |
| 

ACTIVE\_SESSION\_LIMIT\_EXCEEDED = -2

 | 

The request is denied because at least one download task is in progress.

 |
| 

FAILURE = -1

 | 

Failed.

 |
| 

SUCCESS = 0

 | 

Successful.

 |
| 

DOWNLOAD\_WAIT\_WIFI = 1

 | 

Mobile data is in use.

Call the [HMS\_ModuleInstall\_ShowCellularDataConfirmation](#section1897653081720) API to confirm with the user whether to use mobile data for the download.

 |

#### \[h2\]ModuleInstall\_TaskStatus

enum ModuleInstall\_TaskStatus

**Description**

Enumerates task statuses.

**Start version**: 5.0.2(14)

| 
Enumeration

 | 

Description

 |
| :-- | :-- |
| 

CREATE\_TASK\_FAILED = -4

 | 

Failed to create a download task.

 |
| 

HIGHER\_VERSION\_INSTALLED = -3

 | 

The same or a later version already exists on the user's device.

 |
| 

TASK\_ALREADY\_EXISTS = -2

 | 

The download task already exists.

 |
| 

TASK\_UNFOUND = -1

 | 

No download task exists.

 |
| 

TASK\_CREATED = 0

 | 

A download task is created successfully.

 |
| 

DOWNLOADING = 1

 | 

Downloading.

 |
| 

DOWNLOAD\_PAUSED = 2

 | 

Paused.

 |
| 

DOWNLOAD\_WAITING = 3

 | 

Pending download.

 |
| 

DOWNLOAD\_SUCCESSFUL = 4

 | 

Download successful.

 |
| 

DOWNLOAD\_FAILED = 5

 | 

Download failed.

 |
| 

DOWNLOAD\_WAIT\_FOR\_WIFI = 6

 | 

Scheduled to download with Wi-Fi.

 |
| 

INSTALL\_WAITING = 20

 | 

Waiting to install.

 |
| 

INSTALLING = 21

 | 

Installing.

 |
| 

INSTALL\_SUCCESSFUL = 22

 | 

Installation completed.

 |
| 

INSTALL\_FAILED = 23

 | 

Installation failed.

 |

#### Function Description

#### \[h2\]HMS\_ModuleInstall\_GetInstalledModule

ModuleInstall\_ErrCode HMS\_ModuleInstall\_GetInstalledModule(const char \*moduleName, unsigned int length,
    ModuleInstall\_InstalledModule \*\*installedModule)

**Description**

Queries whether a module has been installed.

**System capability**: SystemCapability.AppGalleryService.Distribution.OnDemandInstall

**Start version**: 5.0.2(14)

**Parameters**:

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

moduleName

 | 

Module name.

 |
| 

length

 | 

Length of the module name. A module name can contain a maximum of 512 characters.

 |
| 

installedModule

 | 

Module information.

 |

**Returns**:

**E\_NO\_ERROR**: The operation is successful. **E\_PARAMS**: The input parameters are invalid. **E\_QUERY\_MODULE**: An exception occurs when an API of the BMS is called.

#### \[h2\]HMS\_ModuleInstall\_GetInstalledModuleName

char \*HMS\_ModuleInstall\_GetInstalledModuleName(const ModuleInstall\_InstalledModule \*installedModule)

**Description**

Obtains the module name.

**System capability**: SystemCapability.AppGalleryService.Distribution.OnDemandInstall

**Start version**: 5.0.2(14)

**Parameters**:

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

installedModule

 | 

Module information.

 |

**Returns**:

Module name.

#### \[h2\]HMS\_ModuleInstall\_GetInstalledModuleType

int HMS\_ModuleInstall\_GetInstalledModuleType(const ModuleInstall\_InstalledModule \*installedModule)

**Description**

Obtains the module type.

**System capability**: SystemCapability.AppGalleryService.Distribution.OnDemandInstall

**Start version**: 5.0.2(14)

**Parameters**:

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

installedModule

 | 

Module information.

 |

**Returns**:

Module type. For details, please refer to [bundleManager.ModuleType](../../../../../application-framework/ability-kit/arkts-apis/both-models-recommended/ohos-bundle-bundlemanager-bundle-management-module/document.md#moduletype). When [ModuleInstall\_InstallStatus](#section19925459265) is **1**, **0** will be returned by default.

#### \[h2\]HMS\_ModuleInstall\_GetModuleInstallStatus

ModuleInstall\_InstallStatus HMS\_ModuleInstall\_GetModuleInstallStatus(const ModuleInstall\_InstalledModule \*installedModule)

**Description**

Obtains the module installation status.

**System capability**: SystemCapability.AppGalleryService.Distribution.OnDemandInstall

**Start version**: 5.0.2(14)

**Parameters**:

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

installedModule

 | 

Module information.

 |

**Returns**:

Module installation status. For details, please refer to [ModuleInstall\_InstallStatus](#section19925459265).

#### \[h2\]HMS\_ModuleInstall\_FetchModules

ModuleInstall\_ErrCode HMS\_ModuleInstall\_FetchModules(const char \*bundleName, unsigned int length, char \*\*moduleNames, unsigned int moduleNamesLength, ModuleInstall\_FetchModulesResult \*\*fetchModulesResult)

**Description**

Requests to download a module.

**System capability**: SystemCapability.AppGalleryService.Distribution.OnDemandInstall

**Start version**: 5.0.2(14)

**Parameters**:

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

bundleName

 | 

Package name.

 |
| 

length

 | 

Length of the package name. A package name can contain a maximum of 512 characters.

 |
| 

moduleNames

 | 

Array of module names.

 |
| 

moduleNamesLength

 | 

Length of the module name array. An array can contain a maximum of 512 characters.

 |
| 

fetchModulesResult

 | 

Module installation result.

 |

**Returns**:

**E\_NO\_ERROR**: The operation is successful. **E\_PARAMS**: The input parameters are invalid. **E\_CONNECT\_SA**: A service exception occurs. **E\_CONNECT\_SERVICE\_EXTENSION**: The service connection fails. **E\_WRITE\_PARAM**: Failed to write parameters. **E\_REQUEST\_SERVER**: The service request is abnormal. **E\_RESPONSE\_INVALID**: The response parameters cannot be parsed. **E\_INNER\_ERROR**: An internal error occurs.

#### \[h2\]HMS\_ModuleInstall\_GetFetchModulesRequestCode

ModuleInstall\_RequestCode HMS\_ModuleInstall\_GetFetchModulesRequestCode(const ModuleInstall\_FetchModulesResult \*fetchModulesResult)

**Description**

Obtains the module download request code.

**System capability**: SystemCapability.AppGalleryService.Distribution.OnDemandInstall

**Start version**: 5.0.2(14)

**Parameters**:

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

fetchModulesResult

 | 

Module installation result.

 |

**Returns**:

On-demand module download request code. For details, please refer to [ModuleInstall\_RequestCode](#section10742174163618).

#### \[h2\]HMS\_ModuleInstall\_GetFetchModulesTaskStatus

ModuleInstall\_TaskStatus HMS\_ModuleInstall\_GetFetchModulesTaskStatus(const ModuleInstall\_FetchModulesResult \*fetchModulesResult)

**Description**

Obtains the module download task status.

**System capability**: SystemCapability.AppGalleryService.Distribution.OnDemandInstall

**Start version**: 5.0.2(14)

**Parameters**:

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

fetchModulesResult

 | 

Module installation result.

 |

**Returns**:

Module download task status. For details, please refer to [ModuleInstall\_TaskStatus](#section14463723193715).

#### \[h2\]HMS\_ModuleInstall\_GetFetchModulesTaskId

char \*HMS\_ModuleInstall\_GetFetchModulesTaskId(const ModuleInstall\_FetchModulesResult \*fetchModulesResult)

**Description**

Obtains the module download task ID.

**System capability**: SystemCapability.AppGalleryService.Distribution.OnDemandInstall

**Start version**: 5.0.2(14)

**Parameters**:

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

fetchModulesResult

 | 

Module installation result.

 |

**Returns**:

Task ID.

#### \[h2\]HMS\_ModuleInstall\_GetFetchModulesDesc

char \*HMS\_ModuleInstall\_GetFetchModulesDesc(const ModuleInstall\_FetchModulesResult \*fetchModulesResult)

**Description**

Obtains the module download description.

**System capability**: SystemCapability.AppGalleryService.Distribution.OnDemandInstall

**Start version**: 5.0.2(14)

**Parameters**:

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

fetchModulesResult

 | 

Module installation result.

 |

**Returns**:

Download description.

#### \[h2\]HMS\_ModuleInstall\_GetFetchModules

char\* HMS\_ModuleInstall\_GetFetchModules(const ModuleInstall\_FetchModulesResult \*fetchModulesResult)

**Description**

Obtains the name of the downloaded module.

**System capability**: SystemCapability.AppGalleryService.Distribution.OnDemandInstall

**Start version**: 5.0.2(14)

**Parameters**:

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

fetchModulesResult

 | 

Module installation result.

 |

**Returns**:

Name of the downloaded module.

#### \[h2\]HMS\_ModuleInstall\_GetFetchModulesTotalSize

int HMS\_ModuleInstall\_GetFetchModulesTotalSize(const ModuleInstall\_FetchModulesResult \*fetchModulesResult)

**Description**

Obtains the total size of the downloaded module.

**System capability**: SystemCapability.AppGalleryService.Distribution.OnDemandInstall

**Start version**: 5.0.2(14)

**Parameters**:

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

fetchModulesResult

 | 

Module installation result.

 |

**Returns**:

Total size of the downloaded module.

#### \[h2\]HMS\_ModuleInstall\_GetFetchModulesDownloadedSize

int HMS\_ModuleInstall\_GetFetchModulesDownloadedSize(const ModuleInstall\_FetchModulesResult \*fetchModulesResult)

**Description**

Obtains the downloaded size of the module.

**System capability**: SystemCapability.AppGalleryService.Distribution.OnDemandInstall

**Start version**: 5.0.2(14)

**Parameters**:

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

fetchModulesResult

 | 

Module installation result.

 |

**Returns**:

Downloaded size of the module.

#### \[h2\]HMS\_ModuleInstall\_CancelTask

ModuleInstall\_ErrCode HMS\_ModuleInstall\_CancelTask(const char \*taskId, unsigned int length, unsigned int cancelResult)

**Description**

Cancels a download task.

**System capability**: SystemCapability.AppGalleryService.Distribution.OnDemandInstall

**Start version**: 5.0.2(14)

**Parameters**:

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

taskId

 | 

Task ID.

 |
| 

length

 | 

Length of the task ID. A task ID can contain a maximum of 512 characters.

 |
| 

cancelResult

 | 

Download cancellation result.

 |

**Returns**:

**E\_NO\_ERROR**: The operation is successful. **E\_PARAMS**: The input parameters are invalid. **E\_CONNECT\_SERVICE\_EXTENSION**: Service connection failed. **E\_WRITE\_PARAM**: Failed to write parameters. **E\_REQUEST\_SERVER**: The service request is abnormal. **E\_RESPONSE\_INVALID**: The response parameters could not be parsed.

#### \[h2\]HMS\_ModuleInstall\_ShowCellularDataConfirmation

ModuleInstall\_ErrCode HMS\_ModuleInstall\_ShowCellularDataConfirmation(const char \*taskId, unsigned int length, unsigned int showResult)

**Description**

Displays a mobile data reminder pop-up.

**System capability**: SystemCapability.AppGalleryService.Distribution.OnDemandInstall

**Start version**: 5.0.2(14)

**Parameters**:

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

taskId

 | 

Task ID.

 |
| 

length

 | 

Length of the task ID. A task ID can contain a maximum of 512 characters.

 |
| 

showResult

 | 

Result of displaying the mobile data reminder pop-up.

 |

**Returns**:

**E\_NO\_ERROR**: The operation is successful. **E\_PARAMS**: The input parameters are invalid. **E\_CONNECT\_SERVICE\_EXTENSION**: Service connection failed. **E\_WRITE\_PARAM**: Failed to write parameters. **E\_REQUEST\_SERVER**: The service request is abnormal. **E\_RESPONSE\_INVALID**: The response parameters could not be parsed.

#### \[h2\]HMS\_ModuleInstall\_CreateStatusCallback

ModuleInstall\_StatusCallback \*HMS\_ModuleInstall\_CreateStatusCallback(ModuleInstall\_OnStatusCallback \*onStatusCallback)

**Description**

Creates a callback for listening to the download progress.

**System capability**: SystemCapability.AppGalleryService.Distribution.OnDemandInstall

**Start version**: 5.0.2(14)

**Parameters**:

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

onStatusCallback

 | 

Callback.

 |

**Returns**:

Callback for listening to the download progress.

#### \[h2\]HMS\_ModuleInstall\_On

ModuleInstall\_ErrCode HMS\_ModuleInstall\_On(const char \*bundleName, unsigned int length, unsigned int appIndex, unsigned int period, ModuleInstall\_StatusCallback \*\*callback)

**Description**

Listens to the download progress.

**System capability**: SystemCapability.AppGalleryService.Distribution.OnDemandInstall

**Start version**: 5.0.2(14)

**Parameters**:

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

bundleName

 | 

Package name.

 |
| 

length

 | 

Length of the package name. A package name can contain a maximum of 512 characters.

 |
| 

appIndex

 | 

Index of the app twin.

 |
| 

period

 | 

Listening period.

 |
| 

callback

 | 

Callback for listening to the download progress.

 |

**Returns**:

**E\_NO\_ERROR**: The operation is successful. **E\_PARAMS**: The input parameters are invalid. **E\_REPEATED\_CALL**: The API is called repeatedly. **E\_CONNECT\_SA**: A service exception occurred.

#### \[h2\]HMS\_ModuleInstall\_ReleaseStatusCallback

void HMS\_ModuleInstall\_ReleaseStatusCallback(ModuleInstall\_StatusCallback \*statusCallback)

**Description**

Frees up the callback for listening to the download progress.

**System capability**: SystemCapability.AppGalleryService.Distribution.OnDemandInstall

**Start version**: 5.0.2(14)

**Parameters**:

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

statusCallback

 | 

Callback for listening to the download progress.

 |

#### \[h2\]HMS\_ModuleInstall\_Off

ModuleInstall\_ErrCode HMS\_ModuleInstall\_Off(const char \*bundleName, unsigned int length, unsigned int appIndex)

**Description**

Cancels the callback for listening to the download progress.

**System capability**: SystemCapability.AppGalleryService.Distribution.OnDemandInstall

**Start version**: 5.0.2(14)

**Parameters**:

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

bundleName

 | 

Package name.

 |
| 

length

 | 

Length of the package name. A package name can contain a maximum of 512 characters.

 |
| 

appIndex

 | 

Index of the app twin.

 |

**Returns**:

**E\_NO\_ERROR**: The operation is successful. **E\_PARAMS**: The input parameters are invalid. **E\_OFF\_WITHOUT\_ON**: The API is not used with the listening API. **E\_CONNECT\_SA**: A service exception occurred.
