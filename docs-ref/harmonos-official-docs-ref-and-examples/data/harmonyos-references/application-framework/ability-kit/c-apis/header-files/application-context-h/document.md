# application\_context.h

#### Overview

The file declares the APIs related to the application-level context.

**File to include**: <AbilityKit/ability\_runtime/application\_context.h>

**Library**: libability\_runtime.so

**System capability**: SystemCapability.Ability.AbilityRuntime.Core

**Since**: 13

**Related module**: [AbilityRuntime](../../modules/abilityruntime/document.md)

#### Summary

#### \[h2\]Functions

| Name | Description |
| :-- | :-- |
| [AbilityRuntime\_ErrorCode OH\_AbilityRuntime\_ApplicationContextGetCacheDir(char\* buffer, int32\_t bufferSize, int32\_t\* writeLength)](#oh_abilityruntime_applicationcontextgetcachedir) | Obtains the application-level cache directory of the application. |
| [AbilityRuntime\_ErrorCode OH\_AbilityRuntime\_ApplicationContextGetAreaMode(AbilityRuntime\_AreaMode\* areaMode)](#oh_abilityruntime_applicationcontextgetareamode) | Obtains the application-level file data encryption level of the application. |
| [AbilityRuntime\_ErrorCode OH\_AbilityRuntime\_ApplicationContextGetBundleName(char\* buffer, int32\_t bufferSize, int32\_t\* writeLength)](#oh_abilityruntime_applicationcontextgetbundlename) | Obtains the bundle name of the application. |
| [AbilityRuntime\_ErrorCode OH\_AbilityRuntime\_ApplicationContextGetTempDir(char\* buffer, const int32\_t bufferSize, int32\_t\* writeLength)](#oh_abilityruntime_applicationcontextgettempdir) | Obtains the application-level temporary file directory of the application. |
| [AbilityRuntime\_ErrorCode OH\_AbilityRuntime\_ApplicationContextGetFilesDir(char\* buffer, const int32\_t bufferSize, int32\_t\* writeLength)](#oh_abilityruntime_applicationcontextgetfilesdir) | Obtains the application-level common file directory of the application. |
| [AbilityRuntime\_ErrorCode OH\_AbilityRuntime\_ApplicationContextGetDatabaseDir(char\* buffer, const int32\_t bufferSize, int32\_t\* writeLength)](#oh_abilityruntime_applicationcontextgetdatabasedir) | Obtains the application-level database file directory of the application. |
| [AbilityRuntime\_ErrorCode OH\_AbilityRuntime\_ApplicationContextGetPreferencesDir(char\* buffer, const int32\_t bufferSize, int32\_t\* writeLength)](#oh_abilityruntime_applicationcontextgetpreferencesdir) | Obtains the application-level preferences file directory of the application. |
| [AbilityRuntime\_ErrorCode OH\_AbilityRuntime\_ApplicationContextGetBundleCodeDir(char\* buffer, const int32\_t bufferSize, int32\_t\* writeLength)](#oh_abilityruntime_applicationcontextgetbundlecodedir) | Obtains the application-level installation file directory of the application. |
| [AbilityRuntime\_ErrorCode OH\_AbilityRuntime\_ApplicationContextGetDistributedFilesDir(char\* buffer, const int32\_t bufferSize, int32\_t\* writeLength)](#oh_abilityruntime_applicationcontextgetdistributedfilesdir) | Obtains the application-level distributed file directory of the application. |
| [AbilityRuntime\_ErrorCode OH\_AbilityRuntime\_ApplicationContextGetCloudFileDir(char\* buffer, const int32\_t bufferSize, int32\_t\* writeLength)](#oh_abilityruntime_applicationcontextgetcloudfiledir) | Obtains the application-level cloud file directory of the application. |
| [AbilityRuntime\_ErrorCode OH\_AbilityRuntime\_ApplicationContextGetLogFileDir(char\* buffer, const int32\_t bufferSize, int32\_t\* writeLength)](#oh_abilityruntime_applicationcontextgetlogfiledir) | Obtains the application-level log file directory of the application. |
| [AbilityRuntime\_ErrorCode OH\_AbilityRuntime\_ApplicationContextGetResourceDir(const char\* moduleName, char\* buffer, const int32\_t bufferSize, int32\_t\* writeLength)](#oh_abilityruntime_applicationcontextgetresourcedir) | Obtains the application-level resource directory of the application. |
| [AbilityRuntime\_ErrorCode OH\_AbilityRuntime\_StartSelfUIAbility(AbilityBase\_Want \*want)](#oh_abilityruntime_startselfuiability) | Starts the UIAbility of the current application. |
| [AbilityRuntime\_ErrorCode OH\_AbilityRuntime\_StartSelfUIAbilityWithStartOptions(AbilityBase\_Want \*want,AbilityRuntime\_StartOptions \*options)](#oh_abilityruntime_startselfuiabilitywithstartoptions) | Starts the UIAbility of the current application using **StartOptions**. |
| [AbilityRuntime\_ErrorCode OH\_AbilityRuntime\_ApplicationContextGetVersionCode(int64\_t\* versionCode)](#oh_abilityruntime_applicationcontextgetversioncode) | Obtains the application version code. |
| [AbilityRuntime\_ErrorCode OH\_AbilityRuntime\_StartSelfUIAbilityWithPidResult(AbilityBase\_Want \*want, AbilityRuntime\_StartOptions \*options, int32\_t \*targetPid)](#oh_abilityruntime_startselfuiabilitywithpidresult) | Starts the UIAbility of the current application using **StartOptions** and obtains the process ID of the target UIAbility. |
| [AbilityRuntime\_ErrorCode OH\_AbilityRuntime\_ApplicationContextGetLaunchParameter(char\* buffer, const int32\_t bufferSize, int32\_t\* writeLength)](#oh_abilityruntime_applicationcontextgetlaunchparameter) | Obtains **WantParams** passed for the initial launch of the UIAbility of the current application. |
| [AbilityRuntime\_ErrorCode OH\_AbilityRuntime\_ApplicationContextGetLatestParameter(char\* buffer, const int32\_t bufferSize, int32\_t\* writeLength)](#oh_abilityruntime_applicationcontextgetlatestparameter) | Obtains **WantParams** passed for the most recent launch of the UIAbility of the current application. |

#### Function Description

#### \[h2\]OH\_AbilityRuntime\_ApplicationContextGetCacheDir()

AbilityRuntime\_ErrorCode OH\_AbilityRuntime\_ApplicationContextGetCacheDir(char\* buffer, int32\_t bufferSize, int32\_t\* writeLength)

**Description**

Obtains the application-level cache directory of the application.

**Since**: 13

**Parameters**

| Name | Description |
| :-- | :-- |
| char\* buffer | Pointer to the buffer, which is used to receive the application-level cache directory of the application. |
| int32\_t bufferSize | Buffer size, in bytes. |
| int32\_t\* writeLength | Pointer to the length of the string written to the buffer (measured in bytes) when [ABILITY\_RUNTIME\_ERROR\_CODE\_NO\_ERROR](../ability-runtime-common-h/document.md#abilityruntime_errorcode) is returned. |

**Returns**

| Type | Description |
| :-- | :-- |
| [AbilityRuntime\_ErrorCode](../ability-runtime-common-h/document.md#abilityruntime_errorcode) | 
One of the following execution results:

**ABILITY\_RUNTIME\_ERROR\_CODE\_NO\_ERROR**: The operation is successful.

**ABILITY\_RUNTIME\_ERROR\_CODE\_PARAM\_INVALID**: The passed-in value of **buffer** or **writeLength** is null, or the buffer size is less than the size of the string to be written.

**ABILITY\_RUNTIME\_ERROR\_CODE\_CONTEXT\_NOT\_EXIST**: The application context does not exist. For example, the application-level context does not exist in the [child process](../../modules/childprocess/document.md) created by the application.

 |

#### \[h2\]OH\_AbilityRuntime\_ApplicationContextGetAreaMode()

AbilityRuntime\_ErrorCode OH\_AbilityRuntime\_ApplicationContextGetAreaMode(AbilityRuntime\_AreaMode\* areaMode)

**Description**

Obtains the application-level file data encryption level of the application.

**Since**: 13

**Parameters**

| Name | Description |
| :-- | :-- |
| [AbilityRuntime\_AreaMode](../context-constant-h/document.md#abilityruntime_areamode)\* areaMode | Pointer to the encryption level of the received data. |

**Returns**

| Type | Description |
| :-- | :-- |
| [AbilityRuntime\_ErrorCode](../ability-runtime-common-h/document.md#abilityruntime_errorcode) | 
One of the following execution results:

**ABILITY\_RUNTIME\_ERROR\_CODE\_NO\_ERROR**: The operation is successful.

**ABILITY\_RUNTIME\_ERROR\_CODE\_PARAM\_INVALID**: The passed-in value of **buffer** or **writeLength** is null, or the buffer size is less than the size of the string to be written.

**ABILITY\_RUNTIME\_ERROR\_CODE\_CONTEXT\_NOT\_EXIST**: The application context does not exist. For example, the application-level context does not exist in the [child process](../../modules/childprocess/document.md) created by the application.

 |

#### \[h2\]OH\_AbilityRuntime\_ApplicationContextGetBundleName()

AbilityRuntime\_ErrorCode OH\_AbilityRuntime\_ApplicationContextGetBundleName(char\* buffer, int32\_t bufferSize, int32\_t\* writeLength)

**Description**

Obtains the bundle name of the application.

**Since**: 13

**Parameters**

| Name | Description |
| :-- | :-- |
| char\* buffer | Pointer to the buffer, which is used to receive the bundle name. |
| int32\_t bufferSize | Buffer size, in bytes. |
| int32\_t\* writeLength | Pointer to the length of the string written to the buffer (measured in bytes) when [ABILITY\_RUNTIME\_ERROR\_CODE\_NO\_ERROR](../ability-runtime-common-h/document.md#abilityruntime_errorcode) is returned. |

**Returns**

| Type | Description |
| :-- | :-- |
| [AbilityRuntime\_ErrorCode](../ability-runtime-common-h/document.md#abilityruntime_errorcode) | 
One of the following execution results:

**ABILITY\_RUNTIME\_ERROR\_CODE\_NO\_ERROR**: The operation is successful.

**ABILITY\_RUNTIME\_ERROR\_CODE\_PARAM\_INVALID**: The passed-in value of **buffer** or **writeLength** is null, or the buffer size is less than the size of the string to be written.

**ABILITY\_RUNTIME\_ERROR\_CODE\_CONTEXT\_NOT\_EXIST**: The application context does not exist. For example, the application-level context does not exist in the [child process](../../modules/childprocess/document.md) created by the application.

 |

#### \[h2\]OH\_AbilityRuntime\_ApplicationContextGetTempDir()

AbilityRuntime\_ErrorCode OH\_AbilityRuntime\_ApplicationContextGetTempDir(char\* buffer, const int32\_t bufferSize, int32\_t\* writeLength)

**Description**

Obtains the application-level temporary file directory of the application.

**Since**: 16

**Parameters**

| Name | Description |
| :-- | :-- |
| char\* buffer | Pointer to the buffer, which is used to receive the temporary file directory. |
| const int32\_t bufferSize | Buffer size, in bytes. |
| int32\_t\* writeLength | Pointer to the length of the string written to the buffer (measured in bytes) when [ABILITY\_RUNTIME\_ERROR\_CODE\_NO\_ERROR](../ability-runtime-common-h/document.md#abilityruntime_errorcode) is returned. |

**Returns**

| Type | Description |
| :-- | :-- |
| [AbilityRuntime\_ErrorCode](../ability-runtime-common-h/document.md#abilityruntime_errorcode) | 
One of the following execution results:

**ABILITY\_RUNTIME\_ERROR\_CODE\_NO\_ERROR**: The operation is successful.

**ABILITY\_RUNTIME\_ERROR\_CODE\_PARAM\_INVALID**: The passed-in value of **buffer** or **writeLength** is null, or the buffer size is less than the size of the string to be written.

**ABILITY\_RUNTIME\_ERROR\_CODE\_CONTEXT\_NOT\_EXIST**: The application context does not exist. For example, the application-level context does not exist in the [child process](../../modules/childprocess/document.md) created by the application.

 |

#### \[h2\]OH\_AbilityRuntime\_ApplicationContextGetFilesDir()

AbilityRuntime\_ErrorCode OH\_AbilityRuntime\_ApplicationContextGetFilesDir(char\* buffer, const int32\_t bufferSize, int32\_t\* writeLength)

**Description**

Obtains the application-level common file directory of the application.

**Since**: 16

**Parameters**

| Name | Description |
| :-- | :-- |
| char\* buffer | Pointer to the buffer, which is used to receive the common file directory. |
| const int32\_t bufferSize | Buffer size, in bytes. |
| int32\_t\* writeLength | Pointer to the length of the string written to the buffer (measured in bytes) when [ABILITY\_RUNTIME\_ERROR\_CODE\_NO\_ERROR](../ability-runtime-common-h/document.md#abilityruntime_errorcode) is returned. |

**Returns**

| Type | Description |
| :-- | :-- |
| [AbilityRuntime\_ErrorCode](../ability-runtime-common-h/document.md#abilityruntime_errorcode) | 
One of the following execution results:

**ABILITY\_RUNTIME\_ERROR\_CODE\_NO\_ERROR**: The operation is successful.

**ABILITY\_RUNTIME\_ERROR\_CODE\_PARAM\_INVALID**: The passed-in value of **buffer** or **writeLength** is null, or the buffer size is less than the size of the string to be written.

**ABILITY\_RUNTIME\_ERROR\_CODE\_CONTEXT\_NOT\_EXIST**: The application context does not exist. For example, the application-level context does not exist in the [child process](../../modules/childprocess/document.md) created by the application.

 |

#### \[h2\]OH\_AbilityRuntime\_ApplicationContextGetDatabaseDir()

AbilityRuntime\_ErrorCode OH\_AbilityRuntime\_ApplicationContextGetDatabaseDir(char\* buffer, const int32\_t bufferSize, int32\_t\* writeLength)

**Description**

Obtains the application-level database file directory of the application.

**Since**: 16

**Parameters**

| Name | Description |
| :-- | :-- |
| char\* buffer | Pointer to the buffer, which is used to receive the database file directory. |
| const int32\_t bufferSize | Buffer size, in bytes. |
| int32\_t\* writeLength | Pointer to the length of the string written to the buffer (measured in bytes) when [ABILITY\_RUNTIME\_ERROR\_CODE\_NO\_ERROR](../ability-runtime-common-h/document.md#abilityruntime_errorcode) is returned. |

**Returns**

| Type | Description |
| :-- | :-- |
| [AbilityRuntime\_ErrorCode](../ability-runtime-common-h/document.md#abilityruntime_errorcode) | 
One of the following execution results:

**ABILITY\_RUNTIME\_ERROR\_CODE\_NO\_ERROR**: The operation is successful.

**ABILITY\_RUNTIME\_ERROR\_CODE\_PARAM\_INVALID**: The passed-in value of **buffer** or **writeLength** is null, or the buffer size is less than the size of the string to be written.

**ABILITY\_RUNTIME\_ERROR\_CODE\_CONTEXT\_NOT\_EXIST**: The application context does not exist. For example, the application-level context does not exist in the [child process](../../modules/childprocess/document.md) created by the application.

 |

#### \[h2\]OH\_AbilityRuntime\_ApplicationContextGetPreferencesDir()

AbilityRuntime\_ErrorCode OH\_AbilityRuntime\_ApplicationContextGetPreferencesDir(char\* buffer, const int32\_t bufferSize, int32\_t\* writeLength)

**Description**

Obtains the application-level preferences file directory of the application.

**Since**: 16

**Parameters**

| Name | Description |
| :-- | :-- |
| char\* buffer | Pointer to the buffer, which is used to receive the preferences file directory. |
| const int32\_t bufferSize | Buffer size, in bytes. |
| int32\_t\* writeLength | Pointer to the length of the string written to the buffer (measured in bytes) when [ABILITY\_RUNTIME\_ERROR\_CODE\_NO\_ERROR](../ability-runtime-common-h/document.md#abilityruntime_errorcode) is returned. |

**Returns**

| Type | Description |
| :-- | :-- |
| [AbilityRuntime\_ErrorCode](../ability-runtime-common-h/document.md#abilityruntime_errorcode) | 
One of the following execution results:

**ABILITY\_RUNTIME\_ERROR\_CODE\_NO\_ERROR**: The operation is successful.

**ABILITY\_RUNTIME\_ERROR\_CODE\_PARAM\_INVALID**: The passed-in value of **buffer** or **writeLength** is null, or the buffer size is less than the size of the string to be written.

**ABILITY\_RUNTIME\_ERROR\_CODE\_CONTEXT\_NOT\_EXIST**: The application context does not exist. For example, the application-level context does not exist in the [child process](../../modules/childprocess/document.md) created by the application.

 |

#### \[h2\]OH\_AbilityRuntime\_ApplicationContextGetBundleCodeDir()

AbilityRuntime\_ErrorCode OH\_AbilityRuntime\_ApplicationContextGetBundleCodeDir(char\* buffer, const int32\_t bufferSize, int32\_t\* writeLength)

**Description**

Obtains the application-level installation file directory of the application.

**Since**: 16

**Parameters**

| Name | Description |
| :-- | :-- |
| char\* buffer | Pointer to the buffer, which is used to receive the installation file directory. |
| const int32\_t bufferSize | Buffer size, in bytes. |
| int32\_t\* writeLength | Pointer to the length of the string written to the buffer (measured in bytes) when [ABILITY\_RUNTIME\_ERROR\_CODE\_NO\_ERROR](../ability-runtime-common-h/document.md#abilityruntime_errorcode) is returned. |

**Returns**

| Type | Description |
| :-- | :-- |
| [AbilityRuntime\_ErrorCode](../ability-runtime-common-h/document.md#abilityruntime_errorcode) | 
One of the following execution results:

**ABILITY\_RUNTIME\_ERROR\_CODE\_NO\_ERROR**: The operation is successful.

**ABILITY\_RUNTIME\_ERROR\_CODE\_PARAM\_INVALID**: The passed-in value of **buffer** or **writeLength** is null, or the buffer size is less than the size of the string to be written.

**ABILITY\_RUNTIME\_ERROR\_CODE\_CONTEXT\_NOT\_EXIST**: The application context does not exist. For example, the application-level context does not exist in the [child process](../../modules/childprocess/document.md) created by the application.

 |

#### \[h2\]OH\_AbilityRuntime\_ApplicationContextGetDistributedFilesDir()

AbilityRuntime\_ErrorCode OH\_AbilityRuntime\_ApplicationContextGetDistributedFilesDir(char\* buffer, const int32\_t bufferSize, int32\_t\* writeLength)

**Description**

Obtains the application-level distributed file directory of the application.

**Since**: 16

**Parameters**

| Name | Description |
| :-- | :-- |
| char\* buffer | Pointer to the buffer, which is used to receive the distributed file directory. |
| const int32\_t bufferSize | Buffer size, in bytes. |
| int32\_t\* writeLength | Pointer to the length of the string written to the buffer (measured in bytes) when [ABILITY\_RUNTIME\_ERROR\_CODE\_NO\_ERROR](../ability-runtime-common-h/document.md#abilityruntime_errorcode) is returned. |

**Returns**

| Type | Description |
| :-- | :-- |
| [AbilityRuntime\_ErrorCode](../ability-runtime-common-h/document.md#abilityruntime_errorcode) | 
One of the following execution results:

**ABILITY\_RUNTIME\_ERROR\_CODE\_NO\_ERROR**: The operation is successful.

**ABILITY\_RUNTIME\_ERROR\_CODE\_PARAM\_INVALID**: The passed-in value of **buffer** or **writeLength** is null, or the buffer size is less than the size of the string to be written.

**ABILITY\_RUNTIME\_ERROR\_CODE\_CONTEXT\_NOT\_EXIST**: The application context does not exist. For example, the application-level context does not exist in the [child process](../../modules/childprocess/document.md) created by the application.

 |

#### \[h2\]OH\_AbilityRuntime\_ApplicationContextGetCloudFileDir()

AbilityRuntime\_ErrorCode OH\_AbilityRuntime\_ApplicationContextGetCloudFileDir(char\* buffer, const int32\_t bufferSize, int32\_t\* writeLength)

**Description**

Obtains the application-level cloud file directory of the application.

**Since**: 16

**Parameters**

| Name | Description |
| :-- | :-- |
| char\* buffer | Pointer to the buffer, which is used to receive the cloud file directory. |
| const int32\_t bufferSize | Buffer size, in bytes. |
| int32\_t\* writeLength | Pointer to the length of the string written to the buffer (measured in bytes) when [ABILITY\_RUNTIME\_ERROR\_CODE\_NO\_ERROR](../ability-runtime-common-h/document.md#abilityruntime_errorcode) is returned. |

**Returns**

| Type | Description |
| :-- | :-- |
| [AbilityRuntime\_ErrorCode](../ability-runtime-common-h/document.md#abilityruntime_errorcode) | 
One of the following execution results:

**ABILITY\_RUNTIME\_ERROR\_CODE\_NO\_ERROR**: The operation is successful.

**ABILITY\_RUNTIME\_ERROR\_CODE\_PARAM\_INVALID**: The passed-in value of **buffer** or **writeLength** is null, or the buffer size is less than the size of the string to be written.

**ABILITY\_RUNTIME\_ERROR\_CODE\_CONTEXT\_NOT\_EXIST**: The application context does not exist. For example, the application-level context does not exist in the [child process](../../modules/childprocess/document.md) created by the application.

 |

#### \[h2\]OH\_AbilityRuntime\_ApplicationContextGetLogFileDir()

AbilityRuntime\_ErrorCode OH\_AbilityRuntime\_ApplicationContextGetLogFileDir(char\* buffer, const int32\_t bufferSize, int32\_t\* writeLength)

**Description**

Obtains the application-level log file directory of the application.

**Since**: 22

**Parameters**

| Name | Description |
| :-- | :-- |
| char\* buffer | Pointer to the buffer, which is used to receive the log file directory. |
| const int32\_t bufferSize | Buffer size, in bytes. |
| int32\_t\* writeLength | Pointer to the length of the string written to the buffer (measured in bytes) when [ABILITY\_RUNTIME\_ERROR\_CODE\_NO\_ERROR](../ability-runtime-common-h/document.md#abilityruntime_errorcode) is returned. |

**Returns**

| Type | Description |
| :-- | :-- |
| [AbilityRuntime\_ErrorCode](../ability-runtime-common-h/document.md#abilityruntime_errorcode) | 
One of the following execution results:

**ABILITY\_RUNTIME\_ERROR\_CODE\_NO\_ERROR**: The operation is successful.

**ABILITY\_RUNTIME\_ERROR\_CODE\_PARAM\_INVALID**: The passed-in value of **buffer** or **writeLength** is null, or the buffer size is less than the size of the string to be written.

**ABILITY\_RUNTIME\_ERROR\_CODE\_CONTEXT\_NOT\_EXIST**: The application context does not exist. For example, the application-level context does not exist in the [child process](../../modules/childprocess/document.md) created by the application.

 |

#### \[h2\]OH\_AbilityRuntime\_ApplicationContextGetResourceDir()

AbilityRuntime\_ErrorCode OH\_AbilityRuntime\_ApplicationContextGetResourceDir(const char\* moduleName, char\* buffer, const int32\_t bufferSize, int32\_t\* writeLength)

**Description**

Obtains the application-level resource directory of the application.

**Since**: 20

**Parameters**

| Name | Description |
| :-- | :-- |
| char\* moduleName | Pointer to the module name. |
| char\* buffer | Pointer to the buffer, which is used to receive the resource directory. |
| int32\_t bufferSize | Buffer size, in bytes. |
| int32\_t\* writeLength | Pointer to the length of the string written to the buffer (measured in bytes) when [ABILITY\_RUNTIME\_ERROR\_CODE\_NO\_ERROR](../ability-runtime-common-h/document.md#abilityruntime_errorcode) is returned. |

**Returns**

| Type | Description |
| :-- | :-- |
| [AbilityRuntime\_ErrorCode](../ability-runtime-common-h/document.md#abilityruntime_errorcode) | 
One of the following execution results:

**ABILITY\_RUNTIME\_ERROR\_CODE\_NO\_ERROR**: The operation is successful.

**ABILITY\_RUNTIME\_ERROR\_CODE\_PARAM\_INVALID**: The passed-in value of **buffer** or **writeLength** is null, or the buffer size is less than the size of the string to be written.

**ABILITY\_RUNTIME\_ERROR\_CODE\_CONTEXT\_NOT\_EXIST**: The application context does not exist. For example, the application-level context does not exist in the [child process](../../modules/childprocess/document.md) created by the application.

 |

#### \[h2\]OH\_AbilityRuntime\_StartSelfUIAbility()

AbilityRuntime\_ErrorCode OH\_AbilityRuntime\_StartSelfUIAbility(AbilityBase\_Want \*want)

**Description**

Starts the UIAbility of the current application.

**Required permissions**: ohos.permission.NDK\_START\_SELF\_UI\_ABILITY

**Since**: 15

**Device behavior differences**: This API can be properly called only on 2-in-1 devices and tablets. If it is called on other device types, error code **ABILITY\_RUNTIME\_ERROR\_CODE\_NOT\_SUPPORTED** is returned.

**Parameters**

| Name | Description |
| :-- | :-- |
| [AbilityBase\_Want](../../structs/abilitybase-want/document.md) \*want | Pointer to the Want information required for starting the UIAbility. |

**Returns**

| Type | Description |
| :-- | :-- |
| [AbilityRuntime\_ErrorCode](../ability-runtime-common-h/document.md#abilityruntime_errorcode) | 
**ABILITY\_RUNTIME\_ERROR\_CODE\_NO\_ERROR**: The operation is successful.

**ABILITY\_RUNTIME\_ERROR\_CODE\_PERMISSION\_DENIED**: Permission verification for the caller fails.

**ABILITY\_RUNTIME\_ERROR\_CODE\_PARAM\_INVALID**: Parameter verification for the caller fails.

**ABILITY\_RUNTIME\_ERROR\_CODE\_NOT\_SUPPORTED**: The device type is not supported.

**ABILITY\_RUNTIME\_ERROR\_CODE\_NO\_SUCH\_ABILITY**: The specified ability name does not exist.

**ABILITY\_RUNTIME\_ERROR\_CODE\_INCORRECT\_ABILITY\_TYPE**: The ability type is incorrect.

**ABILITY\_RUNTIME\_ERROR\_CODE\_CROWDTEST\_EXPIRED**: The crowdtesting application expires.

**ABILITY\_RUNTIME\_ERROR\_CODE\_WUKONG\_MODE**: The ability is started or stopped in Wukong mode.

**ABILITY\_RUNTIME\_ERROR\_CODE\_CONTROLLED**: The application is under control.

**ABILITY\_RUNTIME\_ERROR\_CODE\_EDM\_CONTROLLED**: The application is under control by EDM.

**ABILITY\_RUNTIME\_ERROR\_CODE\_CROSS\_APP**: Redirecting to third-party applications is not allowed in API versions later than 11.

**ABILITY\_RUNTIME\_ERROR\_CODE\_INTERNAL**: An internal error occurs.

**ABILITY\_RUNTIME\_ERROR\_CODE\_NOT\_TOP\_ABILITY**: The application is not a top one.

**ABILITY\_RUNTIME\_ERROR\_CODE\_UPPER\_LIMIT\_REACHED** (available since API version 17): The number of instances has reached the upper limit.

**ABILITY\_RUNTIME\_ERROR\_CODE\_APP\_INSTANCE\_KEY\_NOT\_SUPPORTED** (available since API version 17): Setting **APP\_INSTANCE\_KEY** is not supported.

For details, see **AbilityRuntime\_ErrorCode**.

 |

**Example**

#include <AbilityKit/ability\_base/want.h>
#include <AbilityKit/ability\_runtime/application\_context.h>

void startSelfUIAbilityTest()
{
    AbilityBase\_Element element;
    element.abilityName = const\_cast<char\*>("EntryAbility");
    element.bundleName = const\_cast<char\*>("com.example.myapplication");
    element.moduleName = const\_cast<char\*>("entry");
    AbilityBase\_Want\* want = OH\_AbilityBase\_CreateWant(element);

    AbilityRuntime\_ErrorCode err = OH\_AbilityRuntime\_StartSelfUIAbility(want);
    if (err != ABILITY\_RUNTIME\_ERROR\_CODE\_NO\_ERROR) {
        // Record error logs and other service processing.
        return;
    }
    // Destroy the Want to prevent memory leakage.
    OH\_AbilityBase\_DestroyWant(want);
}

#### \[h2\]OH\_AbilityRuntime\_StartSelfUIAbilityWithStartOptions()

AbilityRuntime\_ErrorCode OH\_AbilityRuntime\_StartSelfUIAbilityWithStartOptions(AbilityBase\_Want \*want,AbilityRuntime\_StartOptions \*options)

**Description**

Starts the UIAbility of the current application using **StartOptions**.

**Required permissions**: ohos.permission.NDK\_START\_SELF\_UI\_ABILITY

**Since**: 17

**Device behavior differences**: This API can be properly called only on 2-in-1 devices and tablets. If it is called on other device types, error code **ABILITY\_RUNTIME\_ERROR\_CODE\_NOT\_SUPPORTED** is returned.

**Parameters**

| Name | Description |
| :-- | :-- |
| [AbilityBase\_Want](../../structs/abilitybase-want/document.md) \*want | Pointer to the Want information required for starting the UIAbility. |
| [AbilityRuntime\_StartOptions](../../structs/abilityruntime-startoptions/document.md) \*options | Pointer to **StartOptions** required for starting the UIAbility. If the value of [startVisibility](../context-constant-h/document.md#abilityruntime_startvisibility) is not null, ensure that the current application has been added to the status bar. Otherwise, the [ABILITY\_RUNTIME\_ERROR\_VISIBILITY\_SETTING\_DISABLED](../ability-runtime-common-h/document.md#abilityruntime_errorcode) error code is returned. |

**Returns**

| Type | Description |
| :-- | :-- |
| [AbilityRuntime\_ErrorCode](../ability-runtime-common-h/document.md#abilityruntime_errorcode) | 
**ABILITY\_RUNTIME\_ERROR\_CODE\_NO\_ERROR**: The operation is successful.

**ABILITY\_RUNTIME\_ERROR\_CODE\_PERMISSION\_DENIED**: Permission verification for the caller fails.

**ABILITY\_RUNTIME\_ERROR\_CODE\_PARAM\_INVALID**: Parameter verification for the caller fails.

**ABILITY\_RUNTIME\_ERROR\_CODE\_NOT\_SUPPORTED**: The device type is not supported.

**ABILITY\_RUNTIME\_ERROR\_CODE\_NO\_SUCH\_ABILITY**: The specified ability name does not exist.

**ABILITY\_RUNTIME\_ERROR\_CODE\_INCORRECT\_ABILITY\_TYPE**: The ability type is incorrect.

**ABILITY\_RUNTIME\_ERROR\_CODE\_CROWDTEST\_EXPIRED**: The crowdtesting application expires.

**ABILITY\_RUNTIME\_ERROR\_CODE\_WUKONG\_MODE**: The ability is started or stopped in Wukong mode.

**ABILITY\_RUNTIME\_ERROR\_CODE\_CONTROLLED**: The application is under control.

**ABILITY\_RUNTIME\_ERROR\_CODE\_EDM\_CONTROLLED**: The application is under control by EDM.

**ABILITY\_RUNTIME\_ERROR\_CODE\_CROSS\_APP**: Redirecting to third-party applications is not allowed in API versions later than 11.

**ABILITY\_RUNTIME\_ERROR\_CODE\_INTERNAL**: An internal error occurs.

**ABILITY\_RUNTIME\_ERROR\_CODE\_NOT\_TOP\_ABILITY**: The application is not a top one.

**ABILITY\_RUNTIME\_ERROR\_VISIBILITY\_SETTING\_DISABLED**: Setting the window visibility during startup is not allowed.

**ABILITY\_RUNTIME\_ERROR\_CODE\_MULTI\_APP\_NOT\_SUPPORTED**: The application does not support clone or multi-instance mode.

**ABILITY\_RUNTIME\_ERROR\_CODE\_INVALID\_APP\_INSTANCE\_KEY**: The multi-instance key is invalid.

**ABILITY\_RUNTIME\_ERROR\_CODE\_UPPER\_LIMIT\_REACHED**: The number of instances has reached the upper limit.

**ABILITY\_RUNTIME\_ERROR\_MULTI\_INSTANCE\_NOT\_SUPPORTED**: The application does not support multi-instance mode.

**ABILITY\_RUNTIME\_ERROR\_CODE\_APP\_INSTANCE\_KEY\_NOT\_SUPPORTED**: Setting **APP\_INSTANCE\_KEY** is not supported.

For details, see **AbilityRuntime\_ErrorCode**.

 |

**Example**

#include <AbilityKit/ability\_base/want.h>
#include <AbilityKit/ability\_runtime/application\_context.h>

void demo()
{
    AbilityBase\_Element element;
    element.abilityName = const\_cast<char\*>("EntryAbility");
    element.bundleName = const\_cast<char\*>("com.example.myapplication");
    element.moduleName = const\_cast<char\*>("entry");
    AbilityBase\_Want\* want = OH\_AbilityBase\_CreateWant(element);
    if (want == nullptr) {
        // Record error logs and other service processing.
        return;
    }

    AbilityRuntime\_StartOptions\* options = OH\_AbilityRuntime\_CreateStartOptions();
    if (options == nullptr) {
        // Record error logs and other service processing.

        // Destroy the Want to prevent memory leakage.
        OH\_AbilityBase\_DestroyWant(want);
        return;
    }
    AbilityRuntime\_ErrorCode err = OH\_AbilityRuntime\_StartSelfUIAbilityWithStartOptions(want, options);
    if (err != ABILITY\_RUNTIME\_ERROR\_CODE\_NO\_ERROR) {
        // Record error logs and other service processing.
    }
    // Destroy the Want to prevent memory leakage.
    OH\_AbilityBase\_DestroyWant(want);

    // Destroy options to prevent memory leakage.
    OH\_AbilityRuntime\_DestroyStartOptions(&options);
}

#### \[h2\]OH\_AbilityRuntime\_ApplicationContextGetVersionCode()

AbilityRuntime\_ErrorCode OH\_AbilityRuntime\_ApplicationContextGetVersionCode(int64\_t\* versionCode)

**Description**

Obtains the application version code.

**Since**: 21

**Parameters**

| Name | Description |
| :-- | :-- |
| int64\_t\* [versionCode](../../../arkts-apis/dependent-elements-and-definitions/bundlemanager/bundleinfo/document.md#bundleinfo-1) | Pointer to the bundle's version code, which corresponds to the **versionCode** field in **bundleInfo**. |

**Returns**

| Type | Description |
| :-- | :-- |
| [AbilityRuntime\_ErrorCode](../ability-runtime-common-h/document.md#abilityruntime_errorcode) | 
One of the following execution results:

**ABILITY\_RUNTIME\_ERROR\_CODE\_NO\_ERROR**: The operation is successful.

**ABILITY\_RUNTIME\_ERROR\_CODE\_PARAM\_INVALID**: **versionCode** is null.

**ABILITY\_RUNTIME\_ERROR\_CODE\_CONTEXT\_NOT\_EXIST**: The application context does not exist. For example, the application-level context does not exist in the [child process](../../modules/childprocess/document.md) created by the application.

**ABILITY\_RUNTIME\_ERROR\_CODE\_GET\_APPLICATION\_INFO\_FAILED**: Failed to obtain the application information.

 |

#### \[h2\]OH\_AbilityRuntime\_StartSelfUIAbilityWithPidResult()

AbilityRuntime\_ErrorCode OH\_AbilityRuntime\_StartSelfUIAbilityWithPidResult(AbilityBase\_Want \*want, AbilityRuntime\_StartOptions \*options, int32\_t \*targetPid)

**Description**

Starts the UIAbility of the current application using **StartOptions** and obtains the process ID of the target UIAbility.

This function cannot be called on the main thread of an application, but can be called on the main thread of a [child process](../../modules/childprocess/document.md) created by the application.

If it is called on the main thread of the application, error code **ABILITY\_RUNTIME\_ERROR\_CODE\_MAIN\_THREAD\_NOT\_SUPPORTED** is returned.

**Required permissions**: ohos.permission.NDK\_START\_SELF\_UI\_ABILITY

**Since**: 21

**Device behavior differences**: This API can be properly called only on 2-in-1 devices and tablets. If it is called on other device types, error code **ABILITY\_RUNTIME\_ERROR\_CODE\_NOT\_SUPPORTED** is returned.

**Parameters**

| Name | Description |
| :-- | :-- |
| [AbilityBase\_Want](../../structs/abilitybase-want/document.md) \*want | Pointer to the Want information required for starting the UIAbility. |
| [AbilityRuntime\_StartOptions](../../structs/abilityruntime-startoptions/document.md) \*options | Pointer to **StartOptions** required for starting the UIAbility. If the value of [startVisibility](../context-constant-h/document.md#abilityruntime_startvisibility) is not null, ensure that the current application has been added to the status bar. Otherwise, the [ABILITY\_RUNTIME\_ERROR\_VISIBILITY\_SETTING\_DISABLED](../ability-runtime-common-h/document.md#abilityruntime_errorcode) error code is returned. |
| int32\_t \*targetPid | Pointer to the process ID of the target UIAbility. |

**Returns**

| Type | Description |
| :-- | :-- |
| [AbilityRuntime\_ErrorCode](../ability-runtime-common-h/document.md#abilityruntime_errorcode) | 
**ABILITY\_RUNTIME\_ERROR\_CODE\_NO\_ERROR**: The operation is successful.

**ABILITY\_RUNTIME\_ERROR\_CODE\_PERMISSION\_DENIED**: Permission verification for the caller fails.

**ABILITY\_RUNTIME\_ERROR\_CODE\_PARAM\_INVALID**: Parameter verification for the caller fails.

**ABILITY\_RUNTIME\_ERROR\_CODE\_NOT\_SUPPORTED**: The device type is not supported.

**ABILITY\_RUNTIME\_ERROR\_CODE\_NO\_SUCH\_ABILITY**: The specified ability name does not exist.

**ABILITY\_RUNTIME\_ERROR\_CODE\_INCORRECT\_ABILITY\_TYPE**: The ability type is incorrect.

**ABILITY\_RUNTIME\_ERROR\_CODE\_CROWDTEST\_EXPIRED**: The crowdtesting application expires.

**ABILITY\_RUNTIME\_ERROR\_CODE\_WUKONG\_MODE**: The ability is started or stopped in Wukong mode.

**ABILITY\_RUNTIME\_ERROR\_CODE\_CONTROLLED**: The application is under control.

**ABILITY\_RUNTIME\_ERROR\_CODE\_EDM\_CONTROLLED**: The application is under control by EDM.

**ABILITY\_RUNTIME\_ERROR\_CODE\_CROSS\_APP**: Redirecting to third-party applications is not allowed in API versions later than 11.

**ABILITY\_RUNTIME\_ERROR\_CODE\_INTERNAL**: An internal error occurs.

**ABILITY\_RUNTIME\_ERROR\_CODE\_NOT\_TOP\_ABILITY**: The application is not a top one.

**ABILITY\_RUNTIME\_ERROR\_VISIBILITY\_SETTING\_DISABLED**: Setting the window visibility during startup is not allowed.

**ABILITY\_RUNTIME\_ERROR\_CODE\_MULTI\_APP\_NOT\_SUPPORTED**: The application does not support clone or multi-instance mode.

**ABILITY\_RUNTIME\_ERROR\_CODE\_INVALID\_APP\_INSTANCE\_KEY**: The multi-instance key is invalid.

**ABILITY\_RUNTIME\_ERROR\_CODE\_UPPER\_LIMIT\_REACHED**: The number of instances has reached the upper limit.

**ABILITY\_RUNTIME\_ERROR\_MULTI\_INSTANCE\_NOT\_SUPPORTED**: The application does not support multi-instance mode.

**ABILITY\_RUNTIME\_ERROR\_CODE\_APP\_INSTANCE\_KEY\_NOT\_SUPPORTED**: Setting **APP\_INSTANCE\_KEY** is not supported.

**ABILITY\_RUNTIME\_ERROR\_CODE\_START\_TIMEOUT**: Starting the UIAbility times out.

**ABILITY\_RUNTIME\_ERROR\_CODE\_MAIN\_THREAD\_NOT\_SUPPORTED**: The function cannot be called on the main thread of the application.

 |

**Example**

#include <AbilityKit/ability\_base/want.h>
#include <AbilityKit/ability\_runtime/application\_context.h>

void demo()
{
    AbilityBase\_Element element;
    element.abilityName = const\_cast<char\*>("EntryAbility");
    element.bundleName = const\_cast<char\*>("com.example.myapplication");
    element.moduleName = const\_cast<char\*>("entry");
    AbilityBase\_Want\* want = OH\_AbilityBase\_CreateWant(element);
    if (want == nullptr) {
        // Record error logs and other service processing.
        return;
    }

    AbilityRuntime\_StartOptions\* options = OH\_AbilityRuntime\_CreateStartOptions();
    if (options == nullptr) {
        // Record error logs and other service processing.

        // Destroy the Want to prevent memory leakage.
        OH\_AbilityBase\_DestroyWant(want);
        return;
    }
    int32\_t pid = -1;
    AbilityRuntime\_ErrorCode err = OH\_AbilityRuntime\_StartSelfUIAbilityWithPidResult(want, options, &pid);
    if (err != ABILITY\_RUNTIME\_ERROR\_CODE\_NO\_ERROR) {
        // Record error logs and other service processing.
    }
    // Destroy the Want to prevent memory leakage.
    OH\_AbilityBase\_DestroyWant(want);

    // Destroy options to prevent memory leakage.
    OH\_AbilityRuntime\_DestroyStartOptions(&options);
}

#### \[h2\]OH\_AbilityRuntime\_ApplicationContextGetLaunchParameter

AbilityRuntime\_ErrorCode OH\_AbilityRuntime\_ApplicationContextGetLaunchParameter(
    char\* buffer, const int32\_t bufferSize, int32\_t\* writeLength)

**Description**

Obtains **WantParams** passed for the initial launch of the UIAbility of the current application. For details about **WantParams**, see [parameters in Want](../../../arkts-apis/apis-no-longer-maintained/ability/want/document.md).

**Since**: 21

**Parameters**

| Name | Description |
| :-- | :-- |
| char\* buffer | Pointer to the buffer, which is used to receive **WantParams**. |
| const int32\_t bufferSize | Buffer size, in bytes. |
| int32\_t\* writeLength | Pointer to the length of the string written to the buffer (measured in bytes) when [ABILITY\_RUNTIME\_ERROR\_CODE\_NO\_ERROR](../ability-runtime-common-h/document.md#abilityruntime_errorcode) is returned. |

**Returns**

| Type | Description |
| :-- | :-- |
| [AbilityRuntime\_ErrorCode](../ability-runtime-common-h/document.md#abilityruntime_errorcode) | 
One of the following execution results:

**ABILITY\_RUNTIME\_ERROR\_CODE\_NO\_ERROR**: The operation is successful.

**ABILITY\_RUNTIME\_ERROR\_CODE\_PARAM\_INVALID**: The passed-in value of **buffer** or **writeLength** is null, or the buffer size is less than the size of the string to be written.

**ABILITY\_RUNTIME\_ERROR\_CODE\_CONTEXT\_NOT\_EXIST**: The application context does not exist. For example, the application-level context does not exist in the [child process](../../modules/childprocess/document.md) created by the application.

 |

**Example**

#include "napi/native\_api.h"
#include "AbilityKit/ability\_runtime/application\_context.h"

static napi\_value GetLaunchParameter(napi\_env env, napi\_callback\_info info)
{
    const int32\_t bufferSize = 2048; // Adjust the buffer size as required.
    char buffer\[bufferSize\] = {0};
    int32\_t writeLength = 0;
    int32\_t ret = OH\_AbilityRuntime\_ApplicationContextGetLaunchParameter(buffer, bufferSize, &writeLength);

    if (ret != ABILITY\_RUNTIME\_ERROR\_CODE\_NO\_ERROR) {
        // Handle exceptions.
    }
    // Create a JS string and return WantParams.
    napi\_value result;
    napi\_create\_string\_utf8(env, buffer, writeLength, &result);
    return result;
}

#### \[h2\]OH\_AbilityRuntime\_ApplicationContextGetLatestParameter

AbilityRuntime\_ErrorCode OH\_AbilityRuntime\_ApplicationContextGetLatestParameter(
    char\* buffer, const int32\_t bufferSize, int32\_t\* writeLength)

**Description**

Obtains **WantParams** passed for the mose recent launch of the UIAbility of the current application. For details about **WantParams**, see [parameters in Want](../../../arkts-apis/apis-no-longer-maintained/ability/want/document.md).

**Since**: 21

**Parameters**

| Name | Description |
| :-- | :-- |
| char\* buffer | Pointer to the buffer, which is used to receive **WantParams**. |
| const int32\_t bufferSize | Buffer size, in bytes. |
| int32\_t\* writeLength | Pointer to the length of the string written to the buffer (measured in bytes) when [ABILITY\_RUNTIME\_ERROR\_CODE\_NO\_ERROR](../ability-runtime-common-h/document.md#abilityruntime_errorcode) is returned. |

**Returns**

| Type | Description |
| :-- | :-- |
| [AbilityRuntime\_ErrorCode](../ability-runtime-common-h/document.md#abilityruntime_errorcode) | 
One of the following execution results:

**ABILITY\_RUNTIME\_ERROR\_CODE\_NO\_ERROR**: The operation is successful.

**ABILITY\_RUNTIME\_ERROR\_CODE\_PARAM\_INVALID**: The passed-in value of **buffer** or **writeLength** is null, or the buffer size is less than the size of the string to be written.

**ABILITY\_RUNTIME\_ERROR\_CODE\_CONTEXT\_NOT\_EXIST**: The application context does not exist. For example, the application-level context does not exist in the [child process](../../modules/childprocess/document.md) created by the application.

 |

**Example**

#include "napi/native\_api.h"
#include "AbilityKit/ability\_runtime/application\_context.h"

static napi\_value GetLatestParameter(napi\_env env, napi\_callback\_info info)
{
    const int32\_t bufferSize = 2048; // Adjust the buffer size as required.
    char buffer\[bufferSize\] = {0};
    int32\_t writeLength = 0;
    int32\_t ret = OH\_AbilityRuntime\_ApplicationContextGetLatestParameter(buffer, bufferSize, &writeLength);

    if (ret != ABILITY\_RUNTIME\_ERROR\_CODE\_NO\_ERROR) {
        // Handle exceptions.
    }
    // Create a JS string and return WantParams.
    napi\_value result;
    napi\_create\_string\_utf8(env, buffer, writeLength, &result);
    return result;
}
