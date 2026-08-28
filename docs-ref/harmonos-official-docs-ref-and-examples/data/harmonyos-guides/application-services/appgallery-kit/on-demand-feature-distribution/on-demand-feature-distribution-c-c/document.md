# On-Demand Feature Distribution (C/C++)

#### Use Cases

As HarmonyOS apps continue to evolve, their features are becoming increasingly diverse. 80% of users tend to use just 20% of app features, while the remaining features are tailored to specific users. To prevent first-time app downloads from taking too long and using too much users' device space, AppGallery Kit offers on-demand distribution, which allows users to dynamically download enhanced features as needed.

#### Basic Concepts

On-demand distribution: An app is packaged into multiple installation packages, which contain all app code and static resources. The app downloaded from AppGallery contains only basic features. When a user needs to use enhanced features, they can download the corresponding installation packages from the server to their devices.

#### Restrictions

-   The app must be released on AppGallery.
-   On-demand feature distribution supports phones, tablets, and PCs/2-in-1 devices. Starting from 5.1.1(19), it also supports TVs.

#### API Description

On-demand feature distribution provides the following C APIs. For details, please refer to the [API reference](https://developer.huawei.com/consumer/en/doc/harmonyos-references/store-c-moduleinstall#函数).

| 
API

 | 

**Description**

 |
| :-- | :-- |
| 

[HMS\_ModuleInstall\_GetInstalledModule](https://developer.huawei.com/consumer/en/doc/harmonyos-references/store-c-moduleinstall#oh_osaccount_getname)

 | 

Queries whether a module has been installed.

 |
| 

[HMS\_ModuleInstall\_GetInstalledModuleName](https://developer.huawei.com/consumer/en/doc/harmonyos-references/store-c-moduleinstall#section19475184213526)

 | 

Obtains the module name.

 |
| 

[HMS\_ModuleInstall\_GetInstalledModuleType](https://developer.huawei.com/consumer/en/doc/harmonyos-references/store-c-moduleinstall#section39341746155513)

 | 

Obtains the module type.

 |
| 

[HMS\_ModuleInstall\_GetModuleInstallStatus](https://developer.huawei.com/consumer/en/doc/harmonyos-references/store-c-moduleinstall#section84699521566)

 | 

Obtains the module installation status.

 |
| 

[HMS\_ModuleInstall\_FetchModules](https://developer.huawei.com/consumer/en/doc/harmonyos-references/store-c-moduleinstall#section1533121613581)

 | 

Requests to download a module.

 |
| 

[HMS\_ModuleInstall\_GetFetchModulesRequestCode](https://developer.huawei.com/consumer/en/doc/harmonyos-references/store-c-moduleinstall#section191414113614)

 | 

Obtains the module download request code.

 |
| 

[HMS\_ModuleInstall\_GetFetchModulesTaskStatus](https://developer.huawei.com/consumer/en/doc/harmonyos-references/store-c-moduleinstall#section142448141910)

 | 

Obtains the module download task status.

 |
| 

[HMS\_ModuleInstall\_GetFetchModulesTaskId](https://developer.huawei.com/consumer/en/doc/harmonyos-references/store-c-moduleinstall#section979412409101)

 | 

Obtains the module download task ID.

 |
| 

[HMS\_ModuleInstall\_GetFetchModulesDesc](https://developer.huawei.com/consumer/en/doc/harmonyos-references/store-c-moduleinstall#section762681812121)

 | 

Obtains the module download description.

 |
| 

[HMS\_ModuleInstall\_GetFetchModules](https://developer.huawei.com/consumer/en/doc/harmonyos-references/store-c-moduleinstall#section55521545111313)

 | 

Obtains the name of the downloaded module.

 |
| 

[HMS\_ModuleInstall\_GetFetchModulesTotalSize](https://developer.huawei.com/consumer/en/doc/harmonyos-references/store-c-moduleinstall#section1071043411515)

 | 

Obtains the total size of the downloaded module.

 |
| 

[HMS\_ModuleInstall\_GetFetchModulesDownloadedSize](https://developer.huawei.com/consumer/en/doc/harmonyos-references/store-c-moduleinstall#section04641118168)

 | 

Obtains the downloaded size of the module.

 |
| 

[HMS\_ModuleInstall\_CancelTask](https://developer.huawei.com/consumer/en/doc/harmonyos-references/store-c-moduleinstall#section1177619221712)

 | 

Cancels a download task.

 |
| 

[HMS\_ModuleInstall\_ShowCellularDataConfirmation](https://developer.huawei.com/consumer/en/doc/harmonyos-references/store-c-moduleinstall#section1897653081720)

 | 

Displays a mobile data reminder pop-up.

 |
| 

[HMS\_ModuleInstall\_CreateStatusCallback](https://developer.huawei.com/consumer/en/doc/harmonyos-references/store-c-moduleinstall#section1710031151816)

 | 

Creates a callback for listening to the download progress.

 |
| 

[HMS\_ModuleInstall\_On](https://developer.huawei.com/consumer/en/doc/harmonyos-references/store-c-moduleinstall#section18492123951816)

 | 

Listens to the download progress.

 |
| 

[HMS\_ModuleInstall\_ReleaseStatusCallback](https://developer.huawei.com/consumer/en/doc/harmonyos-references/store-c-moduleinstall#section1541418516194)

 | 

Frees up the callback for listening to the download progress.

 |
| 

[HMS\_ModuleInstall\_Off](https://developer.huawei.com/consumer/en/doc/harmonyos-references/store-c-moduleinstall#section1260162551917)

 | 

Cancels the callback for listening to the download progress.

 |

#### Instructions

To use the on-demand distribution capability provided by **ModuleInstall**, add the corresponding header file.

## Linking the Dynamic Library in the CMake Script

target\_link\_libraries(sample PUBLIC libhmsmoduleinstall.so)

## Adding the Header File

You can use APIs related to on-demand distribution only after importing the [module\_install.h](https://developer.huawei.com/consumer/en/doc/harmonyos-references/store-c-module_install) header file.

#include "AppGalleryKit/module\_install.h"

#### Obtaining Module Installation Information

Before using the on-demand distribution capability, call the [HMS\_ModuleInstall\_GetInstalledModule](https://developer.huawei.com/consumer/en/doc/harmonyos-references/store-c-moduleinstall#oh_osaccount_getname) API to check whether the module to be distributed on demand has been installed. Then you can obtain the module name, module type, and module installation status through the [HMS\_ModuleInstall\_GetInstalledModuleName](https://developer.huawei.com/consumer/en/doc/harmonyos-references/store-c-moduleinstall#section19475184213526), [HMS\_ModuleInstall\_GetInstalledModuleType](https://developer.huawei.com/consumer/en/doc/harmonyos-references/store-c-moduleinstall#section39341746155513), and [HMS\_ModuleInstall\_GetModuleInstallStatus](https://developer.huawei.com/consumer/en/doc/harmonyos-references/store-c-moduleinstall#section84699521566) APIs, respectively.

char \*moduleName;
ModuleInstall\_InstalledModule \*installedModule;
ModuleInstall\_ErrCode ret = HMS\_ModuleInstall\_GetInstalledModule(moduleName, strlen(moduleName), &installedModule);
if (ret == E\_NO\_ERROR) {
    char \*installedModuleName = HMS\_ModuleInstall\_GetInstalledModuleName(installedModule);
    int moduleType = HMS\_ModuleInstall\_GetInstalledModuleType(installedModule);
    int installStatus = HMS\_ModuleInstall\_GetModuleInstallStatus(installedModule);
}
if (installedModule != nullptr) {
    delete installedModule;
    installedModule = nullptr;
}

#### Loading a Module on Demand

You can load a module for your app as required through the [HMS\_ModuleInstall\_FetchModules](https://developer.huawei.com/consumer/en/doc/harmonyos-references/store-c-moduleinstall#section1533121613581) API. Then you can obtain the module download information through the [HMS\_ModuleInstall\_GetFetchModulesRequestCode](https://developer.huawei.com/consumer/en/doc/harmonyos-references/store-c-moduleinstall#section191414113614), [HMS\_ModuleInstall\_GetFetchModulesTaskStatus](https://developer.huawei.com/consumer/en/doc/harmonyos-references/store-c-moduleinstall#section142448141910), [HMS\_ModuleInstall\_GetFetchModulesTaskId](https://developer.huawei.com/consumer/en/doc/harmonyos-references/store-c-moduleinstall#section979412409101), [HMS\_ModuleInstall\_GetFetchModulesDesc](https://developer.huawei.com/consumer/en/doc/harmonyos-references/store-c-moduleinstall#section762681812121), [HMS\_ModuleInstall\_GetFetchModules](https://developer.huawei.com/consumer/en/doc/harmonyos-references/store-c-moduleinstall#section55521545111313), [HMS\_ModuleInstall\_GetFetchModulesTotalSize](https://developer.huawei.com/consumer/en/doc/harmonyos-references/store-c-moduleinstall#section1071043411515), and [HMS\_ModuleInstall\_GetFetchModulesDownloadedSize](https://developer.huawei.com/consumer/en/doc/harmonyos-references/store-c-moduleinstall#section04641118168) APIs.

char \*bundleName;
int arraySize = 1;
char\*\* moduleNames = new char\*\[arraySize\];
for (int i = 0; i < arraySize; i++) {
     moduleNames\[i\] = new char\[256\];
}
ModuleInstall\_FetchModulesResult \*fetchModulesResult;
ModuleInstall\_ErrCode ret = HMS\_ModuleInstall\_FetchModules(bundleName, strlen(bundleName), moduleNames, arraySize, &fetchModulesResult);
if (ret == E\_NO\_ERROR) {
    ModuleInstall\_RequestCode code = HMS\_ModuleInstall\_GetFetchModulesRequestCode(fetchModulesResult);
    ModuleInstall\_TaskStatus taskStatus = HMS\_ModuleInstall\_GetFetchModulesTaskStatus(fetchModulesResult);
    char \*taskId = HMS\_ModuleInstall\_GetFetchModulesTaskId(fetchModulesResult);
    char \*desc = HMS\_ModuleInstall\_GetFetchModulesDesc(fetchModulesResult);
    char \*modules = HMS\_ModuleInstall\_GetFetchModules(fetchModulesResult);
    int totalSize = HMS\_ModuleInstall\_GetFetchModulesTotalSize(fetchModulesResult);
    int downloadedSize = HMS\_ModuleInstall\_GetFetchModulesDownloadedSize(fetchModulesResult);
}
if (moduleNames != nullptr) {
    delete\[\] moduleNames;
    moduleNames = nullptr;
}
if (fetchModulesResult != nullptr) {
    delete fetchModulesResult;
    fetchModulesResult = nullptr;
}

#### Canceling a Download Task

Your app can call the [HMS\_ModuleInstall\_CancelTask](https://developer.huawei.com/consumer/en/doc/harmonyos-references/store-c-moduleinstall#section1177619221712) API to cancel a download task. The value of **taskId** is returned by the [HMS\_ModuleInstall\_GetFetchModulesTaskId](https://developer.huawei.com/consumer/en/doc/harmonyos-references/store-c-moduleinstall#section979412409101) API.

char \*taskId; // Download task ID.
int cancelResult; // Result of canceling the download task.
ModuleInstall\_ErrCode ret = HMS\_ModuleInstall\_CancelTask(taskId, strlen(taskId), cancelResult);
if (ret == E\_NO\_ERROR && cancelResult == 0) {
    // Download task canceled successfully.
}

#### Displaying a Mobile Data Reminder Pop-up

If **DOWNLOAD\_WAIT\_WIFI** is returned after the [HMS\_ModuleInstall\_GetFetchModulesRequestCode](https://developer.huawei.com/consumer/en/doc/harmonyos-references/store-c-moduleinstall#section191414113614) API is called, you need to call the [HMS\_ModuleInstall\_ShowCellularDataConfirmation](https://developer.huawei.com/consumer/en/doc/harmonyos-references/store-c-moduleinstall#section1897653081720) API to display the mobile data reminder pop-up.

char \*taskId; // Download task ID.
int showResult; // Result of displaying the mobile data reminder pop-up.
ModuleInstall\_ErrCode ret = HMS\_ModuleInstall\_ShowCellularDataConfirmation(taskId, strlen(taskId), showResult);
if (ret == E\_NO\_ERROR && showResult == 0) {
    // The mobile data reminder pop-up is successfully displayed.
}

#### Monitoring Download Tasks

## Defining a Callback Function to Monitor Download Tasks

void onEvent(char \*bundleName, char \*eventInfo) {
    // Handling in the callback.
}

## Initializing the Download Progress Callback

The app can call [HMS\_ModuleInstall\_CreateStatusCallback](https://developer.huawei.com/consumer/en/doc/harmonyos-references/store-c-moduleinstall#section1710031151816) to initialize the download progress callback.

ModuleInstall\_StatusCallback \*statusCallback;
ModuleInstall\_OnStatusCallback onStatusCallback = onEvent;
statusCallback = HMS\_ModuleInstall\_CreateStatusCallback(&onStatusCallback);

## Monitoring the Download Progress

The app can monitor the download progress through the [HMS\_ModuleInstall\_On](https://developer.huawei.com/consumer/en/doc/harmonyos-references/store-c-moduleinstall#section18492123951816) API.

char \*bundleName; // App package name.
int appIndex; // App twin index.
int period; // Monitoring period.
ModuleInstall\_ErrCode ret = HMS\_ModuleInstall\_On(bundleName, strlen(bundleName), appIndex, period, &statusCallback);

#### Canceling the Monitoring of Download Tasks

The app can cancel the download progress monitoring through the [HMS\_ModuleInstall\_Off](https://developer.huawei.com/consumer/en/doc/harmonyos-references/store-c-moduleinstall#section1260162551917) API.

char \*bundleName; // App package name.
int appIndex; // App twin index.
ModuleInstall\_ErrCode ret = HMS\_ModuleInstall\_Off(bundleName, strlen(bundleName), appIndex);
if (ret == E\_NO\_ERROR) {
    // Monitoring canceled successfully.
}

#### Complete Sample Code

Refer to the following example to complete the on-demand distribution process.

#include <cstring>
#include "AppGalleryKit/module\_install.h"

void GetInstalledModule() {
    char \*moduleName;
    ModuleInstall\_InstalledModule \*installedModule;
    ModuleInstall\_ErrCode ret = HMS\_ModuleInstall\_GetInstalledModule(moduleName, strlen(moduleName), &installedModule);
    if (ret == E\_NO\_ERROR) {
        char \*installedModuleName = HMS\_ModuleInstall\_GetInstalledModuleName(installedModule);
        int moduleType = HMS\_ModuleInstall\_GetInstalledModuleType(installedModule);
        int installStatus = HMS\_ModuleInstall\_GetModuleInstallStatus(installedModule);
    }
    if (installedModule != nullptr) {
        delete installedModule;
        installedModule = nullptr;
    }
}

void ShowCellularDataConfirmation(char \*taskId) {
    int showResult;
    ModuleInstall\_ErrCode ret = HMS\_ModuleInstall\_ShowCellularDataConfirmation(taskId, strlen(taskId), showResult);
}

void FetchModules() {
    char \*bundleName;
    int arraySize = 1;
    char \*\*moduleNames = new char \*\[arraySize\];
    for (int i = 0; i < arraySize; i++) {
        moduleNames\[i\] = new char\[256\];
    }
    ModuleInstall\_FetchModulesResult \*fetchModulesResult;
    ModuleInstall\_ErrCode ret = HMS\_ModuleInstall\_FetchModules(bundleName, strlen(bundleName), moduleNames, arraySize, &fetchModulesResult);
    if (ret == E\_NO\_ERROR) {
        ModuleInstall\_TaskStatus taskStatus = HMS\_ModuleInstall\_GetFetchModulesTaskStatus(fetchModulesResult);
        char \*taskId = HMS\_ModuleInstall\_GetFetchModulesTaskId(fetchModulesResult);
        ModuleInstall\_RequestCode code = HMS\_ModuleInstall\_GetFetchModulesRequestCode(fetchModulesResult);
        if (code == DOWNLOAD\_WAIT\_WIFI) {
            ShowCellularDataConfirmation(taskId);
        }
        char \*desc = HMS\_ModuleInstall\_GetFetchModulesDesc(fetchModulesResult);
        char \*modules = HMS\_ModuleInstall\_GetFetchModules(fetchModulesResult);
        int totalSize = HMS\_ModuleInstall\_GetFetchModulesTotalSize(fetchModulesResult);
        int downloadedSize = HMS\_ModuleInstall\_GetFetchModulesDownloadedSize(fetchModulesResult);
    }

    if (moduleNames != nullptr) {
        delete\[\] moduleNames;
        moduleNames = nullptr;
    }

    if (fetchModulesResult != nullptr) {
        delete fetchModulesResult;
        fetchModulesResult = nullptr;
    }
}

void CancelTask() {
    char \*taskId;
    int cancelResult;
    ModuleInstall\_ErrCode ret = HMS\_ModuleInstall\_CancelTask(taskId, strlen(taskId), cancelResult);
}

void onEvent(char \*bundleName, char \*eventInfo) {}

void On() {
    char \*bundleName;
    int appIndex;
    int period;
    ModuleInstall\_StatusCallback \*statusCallback;
    ModuleInstall\_OnStatusCallback onStatusCallback = onEvent;
    statusCallback = HMS\_ModuleInstall\_CreateStatusCallback(&onStatusCallback);
    ModuleInstall\_ErrCode ret = HMS\_ModuleInstall\_On(bundleName, strlen(bundleName), appIndex, period, &statusCallback);
}

void Off() {
    char \*bundleName;
    int appIndex;
    ModuleInstall\_ErrCode ret = HMS\_ModuleInstall\_Off(bundleName, strlen(bundleName), appIndex);
}
