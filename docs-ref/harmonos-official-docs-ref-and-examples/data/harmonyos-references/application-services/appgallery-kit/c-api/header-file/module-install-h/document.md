# module\_install.h

#### Overview

Declares the APIs provided by the on-demand distribution capability.

**Library**: libhmsmoduleinstall.so

**System capability**: SystemCapability.AppGalleryService.Distribution.OnDemandInstall

**Start version**: 5.0.2(14)

**Related module**: [ModuleInstall](../../modules/moduleinstall/document.md)

#### Summary

#### \[h2\]Type

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

typedef struct [ModuleInstall\_InstalledModule](../../modules/moduleinstall/document.md#osaccount_errcode) [ModuleInstall\_InstalledModule](../../modules/moduleinstall/document.md#osaccount_errcode)

 | 

Module information.

 |
| 

typedef struct [ModuleInstall\_FetchModulesResult](../../modules/moduleinstall/document.md#section115389533615) [ModuleInstall\_FetchModulesResult](../../modules/moduleinstall/document.md#section115389533615)

 | 

Module installation result.

 |
| 

typedef struct [ModuleInstall\_StatusCallback](../../modules/moduleinstall/document.md#section48269177812) [ModuleInstall\_StatusCallback](../../modules/moduleinstall/document.md#section48269177812)

 | 

Module installation status callback.

 |
| 

[ModuleInstall\_OnStatusCallback](../../modules/moduleinstall/document.md#section9881414171010)

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

typedef enum [ModuleInstall\_ErrCode](../../modules/moduleinstall/document.md#osaccount_errcode-1) {

E\_NO\_ERROR = 0,

E\_PARAMS = 401,

E\_QUERY\_MODULE = 1006500001,

E\_REPEATED\_CALL = 1006500002,

E\_CONNECT\_SA = 1006500004,

E\_OFF\_WITHOUT\_ON = 1006500006,

E\_CONNECT\_SERVICE\_EXTENSION = 1006500007,

E\_WRITE\_PARAM = 1006500008,

E\_REQUEST\_SERVER = 1006500009,

E\_RESPONSE\_INVALID = 1006500010,

E\_INNER\_ERROR = 1006500011

}

 | 

Enumerates error codes.

 |
| 

typedef enum [ModuleInstall\_InstallStatus](../../modules/moduleinstall/document.md#section19925459265) {

INSTALLED = 0,

NOT\_INSTALLED = 1

}

 | 

Enumerates installation statuses.

 |
| 

typedef enum [ModuleInstall\_RequestCode](../../modules/moduleinstall/document.md#section10742174163618) {

MODULE\_ALREADY\_EXISTS = -8,

MODULE\_UNAVAILABLE = -7,

INVALID\_REQUEST = -6,

NETWORK\_ERROR = -5,

INVOKER\_VERIFICATION\_FAILED = -4,

FOREGROUND\_REQUIRED = -3,

ACTIVE\_SESSION\_LIMIT\_EXCEEDED = -2,

FAILURE = -1,

SUCCESS = 0,

DOWNLOAD\_WAIT\_WIFI = 1

}

 | 

Enumerates request codes.

 |
| 

typedef enum [ModuleInstall\_TaskStatus](../../modules/moduleinstall/document.md#section14463723193715) {

CREATE\_TASK\_FAILED = -4,

HIGHER\_VERSION\_INSTALLED = -3,

TASK\_ALREADY\_EXISTS = -2,

TASK\_UNFOUND = -1,

TASK\_CREATED = 0,

DOWNLOADING = 1,

DOWNLOAD\_PAUSED = 2,

DOWNLOAD\_WAITING = 3,

DOWNLOAD\_SUCCESSFUL = 4,

DOWNLOAD\_FAILED = 5,

DOWNLOAD\_WAIT\_FOR\_WIFI = 6,

INSTALL\_WAITING = 20,

INSTALLING = 21,

INSTALL\_SUCCESSFUL = 22,

INSTALL\_FAILED = 23

}

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

[HMS\_ModuleInstall\_GetInstalledModule](../../modules/moduleinstall/document.md#oh_osaccount_getname)

 | 

Queries whether a module has been installed.

 |
| 

[HMS\_ModuleInstall\_GetInstalledModuleName](../../modules/moduleinstall/document.md#section19475184213526)

 | 

Obtains the module name.

 |
| 

[HMS\_ModuleInstall\_GetInstalledModuleType](../../modules/moduleinstall/document.md#section39341746155513)

 | 

Obtains the module type.

 |
| 

[HMS\_ModuleInstall\_GetModuleInstallStatus](../../modules/moduleinstall/document.md#section84699521566)

 | 

Obtains the module installation status.

 |
| 

[HMS\_ModuleInstall\_FetchModules](../../modules/moduleinstall/document.md#section1533121613581)

 | 

Requests to download a module.

 |
| 

[HMS\_ModuleInstall\_GetFetchModulesRequestCode](../../modules/moduleinstall/document.md#section191414113614)

 | 

Obtains the module download request code.

 |
| 

[HMS\_ModuleInstall\_GetFetchModulesTaskStatus](../../modules/moduleinstall/document.md#section142448141910)

 | 

Obtains the module download task status.

 |
| 

[HMS\_ModuleInstall\_GetFetchModulesTaskId](../../modules/moduleinstall/document.md#section979412409101)

 | 

Obtains the module download task ID.

 |
| 

[HMS\_ModuleInstall\_GetFetchModulesDesc](../../modules/moduleinstall/document.md#section762681812121)

 | 

Obtains the module download description.

 |
| 

[HMS\_ModuleInstall\_GetFetchModules](../../modules/moduleinstall/document.md#section55521545111313)

 | 

Obtains the name of the downloaded module.

 |
| 

[HMS\_ModuleInstall\_GetFetchModulesTotalSize](../../modules/moduleinstall/document.md#section1071043411515)

 | 

Obtains the total size of the downloaded module.

 |
| 

[HMS\_ModuleInstall\_GetFetchModulesDownloadedSize](../../modules/moduleinstall/document.md#section04641118168)

 | 

Obtains the downloaded size of the module.

 |
| 

[HMS\_ModuleInstall\_CancelTask](../../modules/moduleinstall/document.md#section1177619221712)

 | 

Cancels a download task.

 |
| 

[HMS\_ModuleInstall\_ShowCellularDataConfirmation](../../modules/moduleinstall/document.md#section1897653081720)

 | 

Displays a mobile data reminder pop-up.

 |
| 

[HMS\_ModuleInstall\_CreateStatusCallback](../../modules/moduleinstall/document.md#section1710031151816)

 | 

Creates a callback for listening to the download progress.

 |
| 

[HMS\_ModuleInstall\_On](../../modules/moduleinstall/document.md#section18492123951816)

 | 

Listens to the download progress.

 |
| 

[HMS\_ModuleInstall\_ReleaseStatusCallback](../../modules/moduleinstall/document.md#section1541418516194)

 | 

Frees up the callback for listening to the download progress.

 |
| 

[HMS\_ModuleInstall\_Off](../../modules/moduleinstall/document.md#section1260162551917)

 | 

Cancels the callback for listening to the download progress.

 |
