# @ohos.fileshare (File Sharing)

The **FileShare** module provides APIs for granting permissions on a user file to another application based on the file Uniform Resource Identifier (URI). Then, the authorized application can call [@ohos.file.fs](../ohos-file-fs-file-management/document.md) APIs to access the file.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7d/v3/_G9pRzQCQ_WvL5SRmBf_vw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062320Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=F055BBFC9C15AFD468C873CEAA3A8C43AA1DE80EE2AF0E13FF5908BFDABF7784)

The initial APIs of this module are supported since API version 9. Newly added APIs will be marked with a superscript to indicate their earliest API version.

#### Modules to Import

import { fileShare } from '@kit.CoreFileKit';

#### OperationMode11+

Enumerates the modes for accessing a URI.

**System capability**: SystemCapability.FileManagement.AppFileService.FolderAuthorization

| Name | Value | Description |
| :-- | :-- | :-- |
| READ\_MODE | 0b1 | Read. |
| WRITE\_MODE | 0b10 | Write. |
| CREATE\_MODE20+ | 0b100 | Permission to create a file or folder. |
| DELETE\_MODE20+ | 0b1000 | Permission to delete a file or folder. |
| RENAME\_MODE20+ | 0b10000 | Permission to rename a file or folder. |

#### PolicyErrorCode11+

Enumerates the error codes for a permission policy.

**System capability**: SystemCapability.FileManagement.AppFileService.FolderAuthorization

| Name | Value | Description |
| :-- | :-- | :-- |
| PERSISTENCE\_FORBIDDEN | 1 | The permission on the URI cannot be persisted. |
| INVALID\_MODE | 2 | Invalid mode. |
| INVALID\_PATH | 3 | Invalid path. |
| PERMISSION\_NOT\_PERSISTED12+ | 4 | The permission is not persisted. |

#### PolicyErrorResult11+

type PolicyErrorResult = { uri: string; code: PolicyErrorCode; message: string; }

Represents the detailed permission policy error result, which can be used when **persistPermission**, **revokePermission**, **activatePermission**, or **deactivatePermission** throws an error.

**System capability**: SystemCapability.FileManagement.AppFileService.FolderAuthorization

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| uri | string | Yes | URI of the file, on which the permission fails to be granted or activated. |
| code | [PolicyErrorCode](#policyerrorcode11) | Yes | Error code. |
| message | string | Yes | Error message. |

#### PolicyInfo11+

Represents a permission policy, that is, a policy for granting or activating the permission on a file.

**System capability**: SystemCapability.FileManagement.AppFileService.FolderAuthorization

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| uri | string | No | No | URI of the file, on which the permission is to be granted or activated. |
| operationMode | number | No | No | URI operation mode. For details, see [OperationMode](#operationmode11). To grant multiple permissions, you can combine them, for example, use READ\_MODE | WRITE\_MODE to grant the read and write permissions. |

#### PathPolicyInfo15+

Represents the information about the file or directory to be queried.

**System capability**: SystemCapability.FileManagement.AppFileService.FolderAuthorization

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| path | string | No | No | Path to be queried. |
| operationMode | OperationMode | No | No | Operation mode of the path to be queried. For details, see [OperationMode](#operationmode11). |

#### PolicyType15+

Enumerates the authorization modes corresponding to the queried policy information.

**System capability**: SystemCapability.FileManagement.AppFileService.FolderAuthorization

| Name | Value | Description |
| :-- | :-- | :-- |
| TEMPORARY\_TYPE | 0 | Temporary permission. |
| PERSISTENT\_TYPE | 1 | Persistent permission. |

#### fileShare.persistPermission11+

persistPermission(policies: Array<PolicyInfo>): Promise<void>

Checks persistent permissions. This API uses a promise to return the result. This API is available only to the devices with the required system capability. (This API does not support persistent permissions for media URIs and remote URIs.)

**Required permissions**: ohos.permission.FILE\_ACCESS\_PERSIST

**System capability**: SystemCapability.FileManagement.AppFileService.FolderAuthorization

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| policies | Array<[PolicyInfo](#policyinfo11)\> | Yes | Array of permission policies. The maximum number of policies is 500. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Error codes**

For details about the error codes, see [File Management Error Codes](../../error-codes/file-management-error-codes/document.md) and [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

If the permission persistence of some URIs fails, error code 13900001 will be returned and the **data** field provides error information of these URIs in the Array<[PolicyErrorResult](#policyerrorresult11)\> format.

| ID | Error Message |
| :-- | :-- |
| 201 | Permission verification failed, usually the result returned by VerifyAccessToken. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 801 | Capability not supported. |
| 13900001 | Operation not permitted. |
| 13900042 | Out of memory. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';
import { picker } from '@kit.CoreFileKit';

async function persistPermissionExample() {
  try {
    let DocumentSelectOptions = new picker.DocumentSelectOptions();
    let documentPicker = new picker.DocumentViewPicker();
    let uris = await documentPicker.select(DocumentSelectOptions);
    let policyInfo: fileShare.PolicyInfo = {
      uri: uris\[0\],
      // Multiple permissions can be granted in combination. For example, the read and write permissions can be granted using fileShare.OperationMode.READ\_MODE | fileShare.OperationMode.WRITE\_MODE.
      operationMode: fileShare.OperationMode.READ\_MODE
    };
    let policies: Array<fileShare.PolicyInfo> = \[policyInfo\];
    fileShare.persistPermission(policies).then(() => {
      console.info("persistPermission successfully");
    }).catch((err: BusinessError<Array<fileShare.PolicyErrorResult>>) => {
      console.error("persistPermission failed with error message: " + err.message + ", error code: " + err.code);
      if (err.code == 13900001 && err.data) {
        for (let i = 0; i < err.data.length; i++) {
          console.error("error code : " + JSON.stringify(err.data\[i\].code));
          console.error("error uri : " + JSON.stringify(err.data\[i\].uri));
          console.error("error reason : " + JSON.stringify(err.data\[i\].message));
        }
      }
    });
  } catch (error) {
    let err: BusinessError = error as BusinessError;
    console.error('persistPermission failed with err: ' + JSON.stringify(err));
  }
}

#### fileShare.revokePermission11+

revokePermission(policies: Array<PolicyInfo>): Promise<void>

Revokes permissions from multiple files or directories. This API uses a promise to return the result. This API is available only to the devices with the required system capability. (This API does not support persistent permissions for media URIs and remote URIs.)

**Required permissions**: ohos.permission.FILE\_ACCESS\_PERSIST

**System capability**: SystemCapability.FileManagement.AppFileService.FolderAuthorization

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| policies | Array<[PolicyInfo](#policyinfo11)\> | Yes | Array of permission policies. The maximum number of policies is 500. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Error codes**

For details about the error codes, see [File Management Error Codes](../../error-codes/file-management-error-codes/document.md) and [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

If the permission revocation of some URIs fails, error code 13900001 will be returned and the **data** field provides error information of these URIs in the Array<[PolicyErrorResult](#policyerrorresult11)\> format.

| ID | Error Message |
| :-- | :-- |
| 201 | Permission verification failed, usually the result returned by VerifyAccessToken. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 801 | Capability not supported. |
| 13900001 | Operation not permitted. |
| 13900042 | Out of memory. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';
import { picker } from '@kit.CoreFileKit';

async function revokePermissionExample() {
  try {
    let DocumentSelectOptions = new picker.DocumentSelectOptions();
    let documentPicker = new picker.DocumentViewPicker();
    let uris = await documentPicker.select(DocumentSelectOptions);
    let policyInfo: fileShare.PolicyInfo = {
      uri: uris\[0\],
      // Multiple permissions can be revoked in combination. For example, the read and write permissions can be revoked using fileShare.OperationMode.READ\_MODE | fileShare.OperationMode.WRITE\_MODE.
      operationMode: fileShare.OperationMode.READ\_MODE,
    };
    let policies: Array<fileShare.PolicyInfo> = \[policyInfo\];
    fileShare.revokePermission(policies).then(() => {
      console.info("revokePermission successfully");
    }).catch((err: BusinessError<Array<fileShare.PolicyErrorResult>>) => {
      console.error("revokePermission failed with error message: " + err.message + ", error code: " + err.code);
        if (err.code == 13900001 && err.data) {
          for (let i = 0; i < err.data.length; i++) {
            console.error("error code : " + JSON.stringify(err.data\[i\].code));
            console.error("error uri : " + JSON.stringify(err.data\[i\].uri));
            console.error("error reason : " + JSON.stringify(err.data\[i\].message));
          }
        }
    });
  } catch (error) {
    let err: BusinessError = error as BusinessError;
    console.error('revokePermission failed with err: ' + JSON.stringify(err));
  }
}

#### fileShare.activatePermission11+

activatePermission(policies: Array<PolicyInfo>): Promise<void>

Activates the permissions that have been persisted on multiple files or directories. This API uses a promise to return the result. This API is available only to the devices with the required system capability. (This API does not support persistent permissions for media URIs and remote URIs.)

**Required permissions**: ohos.permission.FILE\_ACCESS\_PERSIST

**System capability**: SystemCapability.FileManagement.AppFileService.FolderAuthorization

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| policies | Array<[PolicyInfo](#policyinfo11)\> | Yes | Array of permission policies. The maximum number of policies is 500. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Error codes**

For details about the error codes, see [File Management Error Codes](../../error-codes/file-management-error-codes/document.md) and [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

If the permission activation of some URIs fails, error code 13900001 will be returned and the **data** field provides error information of these URIs in the Array<[PolicyErrorResult](#policyerrorresult11)\> format.

| ID | Error Message |
| :-- | :-- |
| 201 | Permission verification failed, usually the result returned by VerifyAccessToken. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 801 | Capability not supported. |
| 13900001 | Operation not permitted. |
| 13900042 | Out of memory. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

async function activatePermissionExample() {
  try {
    let uri = "file://docs/storage/Users/username/tmp.txt";
    let policyInfo: fileShare.PolicyInfo = {
      uri: uri,
      // Multiple permissions can be activated in combination. For example, the read and write permissions can be activated using fileShare.OperationMode.READ\_MODE | fileShare.OperationMode.WRITE\_MODE.
      operationMode: fileShare.OperationMode.READ\_MODE,
    };
    let policies: Array<fileShare.PolicyInfo> = \[policyInfo\];
    fileShare.activatePermission(policies).then(() => {
      console.info("activatePermission successfully");
    }).catch(async (err: BusinessError<Array<fileShare.PolicyErrorResult>>) => {
      console.error("activatePermission failed with error message: " + err.message + ", error code: " + err.code);
        if (err.code == 13900001 && err.data) {
          for (let i = 0; i < err.data.length; i++) {
            console.error("error code : " + JSON.stringify(err.data\[i\].code));
            console.error("error uri : " + JSON.stringify(err.data\[i\].uri));
            console.error("error reason : " + JSON.stringify(err.data\[i\].message));
            if(err.data\[i\].code == fileShare.PolicyErrorCode.PERMISSION\_NOT\_PERSISTED){
              await fileShare.persistPermission(policies);
            }
          }
        }
    });
  } catch (error) {
    let err: BusinessError = error as BusinessError;
    console.error('activatePermission failed with err: ' + JSON.stringify(err));
  }
}

#### fileShare.deactivatePermission11+

deactivatePermission(policies: Array<PolicyInfo>): Promise<void>

Deactivates the permissions on multiple files or directories. This API uses a promise to return the result. This API is available only to the devices with the required system capability. (This API does not support persistent permissions for media URIs and remote URIs.)

**Required permissions**: ohos.permission.FILE\_ACCESS\_PERSIST

**System capability**: SystemCapability.FileManagement.AppFileService.FolderAuthorization

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| policies | Array<[PolicyInfo](#policyinfo11)\> | Yes | Array of permission policies. The maximum number of policies is 500. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Error codes**

For details about the error codes, see [File Management Error Codes](../../error-codes/file-management-error-codes/document.md) and [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

If the permission deactivation of some URIs fails, error code 13900001 will be returned and the **data** field provides error information of these URIs in the Array<[PolicyErrorResult](#policyerrorresult11)\> format.

| ID | Error Message |
| :-- | :-- |
| 201 | Permission verification failed, usually the result returned by VerifyAccessToken. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 801 | Capability not supported. |
| 13900001 | Operation not permitted. |
| 13900042 | Out of memory. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

async function deactivatePermissionExample() {
  try {
    let uri = "file://docs/storage/Users/username/tmp.txt";
    let policyInfo: fileShare.PolicyInfo = {
      uri: uri,
      // Multiple permissions can be deactivated in combination. For example, the read and write permissions can be deactivated using fileShare.OperationMode.READ\_MODE | fileShare.OperationMode.WRITE\_MODE.
      operationMode: fileShare.OperationMode.READ\_MODE,
    };
    let policies: Array<fileShare.PolicyInfo> = \[policyInfo\];
    fileShare.deactivatePermission(policies).then(() => {
      console.info("deactivatePermission successfully");
    }).catch((err: BusinessError<Array<fileShare.PolicyErrorResult>>) => {
      console.error("deactivatePermission failed with error message: " + err.message + ", error code: " + err.code);
        if (err.code == 13900001 && err.data) {
          for (let i = 0; i < err.data.length; i++) {
            console.error("error code : " + JSON.stringify(err.data\[i\].code));
            console.error("error uri : " + JSON.stringify(err.data\[i\].uri));
            console.error("error reason : " + JSON.stringify(err.data\[i\].message));
          }
        }
    });
  } catch (error) {
    let err: BusinessError = error as BusinessError;
    console.error('deactivatePermission failed with err: ' + JSON.stringify(err));
  }
}

#### fileShare.checkPersistentPermission12+

checkPersistentPermission(policies: Array<PolicyInfo>): Promise<Array<boolean>>

Checks persistent permissions. This API uses a promise to return the result.

**System capability**: SystemCapability.FileManagement.AppFileService.FolderAuthorization

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| policies | Array<[PolicyInfo](#policyinfo11)\> | Yes | Array of permission policies. The maximum number of policies is 500. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<Array<boolean>> | Promise used to return the result. The value **true** means the permission is persistent; the value **false** means the opposite. |

**Error codes**

For details about the error codes, see [File Management Error Codes](../../error-codes/file-management-error-codes/document.md) and [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 801 | Capability not supported. |
| 13900042 | Out of memory. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';
import { picker } from '@kit.CoreFileKit';

async function checkPersistentPermissionExample() {
  try {
    let documentSelectOptions = new picker.DocumentSelectOptions();
    let documentPicker = new picker.DocumentViewPicker();
    let uris = await documentPicker.select(documentSelectOptions);
    let policyInfo: fileShare.PolicyInfo = {
      uri: uris\[0\],
      // Multiple permissions can be checked in combination. For example, the read and write permissions can be checked using fileShare.OperationMode.READ\_MODE | fileShare.OperationMode.WRITE\_MODE.
      operationMode: fileShare.OperationMode.READ\_MODE,
    };
    let policies: Array<fileShare.PolicyInfo> = \[policyInfo\];
    fileShare.checkPersistentPermission(policies).then(async (data) => {
      let result: Array<boolean> = data;
      for (let i = 0; i < result.length; i++) {
        console.info("checkPersistentPermission result: " + JSON.stringify(result\[i\]));
        if(!result\[i\]){
          let info: fileShare.PolicyInfo = {
            uri: policies\[i\].uri,
            operationMode: policies\[i\].operationMode,
          };
          let policy : Array<fileShare.PolicyInfo> = \[info\];
          await fileShare.persistPermission(policy);
        }
      }
    }).catch((err: BusinessError<Array<fileShare.PolicyErrorResult>>) => {
      console.error("checkPersistentPermission failed with error message: " + err.message + ", error code: " + err.code);
    });
  } catch (error) {
    let err: BusinessError = error as BusinessError;
    console.error('checkPersistentPermission failed with err: ' + JSON.stringify(err));
  }
}
