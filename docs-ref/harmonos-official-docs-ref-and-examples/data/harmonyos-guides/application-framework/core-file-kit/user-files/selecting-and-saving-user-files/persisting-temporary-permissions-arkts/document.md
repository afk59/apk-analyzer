# Persisting Temporary Permissions (ArkTS)

#### When to Use

If an application accesses a file by using Picker, the permission for accessing the file will be automatically invalidated after the application exits or the device restarts. To retain the permission for accessing the file, you need to persist the temporarily granted permission.

#### Persisting a Temporary Permission Granted by Picker

You can use Picker to select a file or folder, and persist the temporary permission granted by Picker by using the API provided by [ohos.fileshare](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-fileshare).

1.  When an application needs to temporarily access data in a user directory, for example, a communication application needs to send a user file or image, it calls [select()](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-file-picker#select-3) of Picker to select the file or image to be sent. In this case, the application obtains the temporary permission for accessing the file or image. After the application or device is restarted, the application still needs to call a Picker API to access the file or image.
    
2.  Sometimes, an application needs to access a file or directory multiple times. For example, after editing a user file, a file editor application needs to select and open the file directly from the history records. In this case, you can use Picker to select the file, and use [ohos.fileshare.persistPermission](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-fileshare#filesharepersistpermission11) to persist the temporary permission granted by Picker.
    

Before persisting a temporary permission, ensure that:

The device must have the system capability SystemCapability.FileManagement.AppFileService.FolderAuthorization. You can use **canIUse()** to check whether the device has the required system capability.

if (!canIUse('SystemCapability.FileManagement.AppFileService.FolderAuthorization')) {
    console.error('this api is not supported on this device');
    return;
}

**Required Permissions**

ohos.permission.FILE\_ACCESS\_PERSIST. For details about how to request the permission, see [Workflow for Requesting Permissions](../../../../../system/security/application-access-control/application-permission-management/requesting-application-permissions/workflow-for-requesting-permissions/document.md).

**Example**

import { BusinessError } from '@kit.BasicServicesKit';
import { picker } from '@kit.CoreFileKit';
import { fileShare } from '@kit.CoreFileKit';

export async function persistPermissionExample() {
  try {
    // ···
    let documentSelectOptions = new picker.DocumentSelectOptions();
    let documentPicker = new picker.DocumentViewPicker();
    let uris = await documentPicker.select(documentSelectOptions);
    let policyInfo: fileShare.PolicyInfo = {
      uri: uris\[0\],
      operationMode: fileShare.OperationMode.READ\_MODE,
    };
    let policies: fileShare.PolicyInfo\[\] = \[policyInfo\];
    fileShare.persistPermission(policies).then(() => {
      console.info('persistPermission successfully');
    }).catch((err: BusinessError<Array<fileShare.PolicyErrorResult>>) => {
      console.error('persistPermission failed with error message: ' + err.message + ', error code: ' + err.code);
      if (err.code == 13900001 && err.data) {
        for (let i = 0; i < err.data.length; i++) {
          console.error('error code : ' + JSON.stringify(err.data\[i\].code));
          console.error('error uri : ' + JSON.stringify(err.data\[i\].uri));
          console.error('error reason : ' + JSON.stringify(err.data\[i\].message));
        }
      }
    });
  } catch (error) {
    let err: BusinessError = error as BusinessError;
    console.error(\`persistPermission failed with err, Error code: ${err.code}, message: ${err.message}\`);
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/79/v3/cZdPO1qDSaONmNl8Nffprw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061951Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=1E5E5C1B897E28C67D440300DDF6ABF4F430FBFC32C7A4817FBDB7B4DA447BA8)

-   You are advised to save the URI of the file with persistent permission for the related application locally to facilitate the subsequent activation.
-   The permission persistence data is also stored in the system database. After the application or device is restarted, the persistent permission can be used only after being activated. For details, see [Activating a Persistent Permission](#activating-a-persistent-permission-for-accessing-a-file-or-folder).
-   Before persisting permissions, use **canIUse()** to check whether the device has the required system capability and permission.
-   When an application is uninstalled, all the permission authorization data will be deleted. After the application is reinstalled, re-authorization is required.

For details about how to persist a temporary permission using C/C++ APIs, see [OH\_FileShare\_PersistPermission](../persisting-temporary-permissions-c-c/document.md).

You can use [ohos.fileshare.revokePermission](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-fileshare#filesharerevokepermission11) to revoke the persistent permission from a file, and update the data stored in the application to delete the file URI from the recently accessed data.

**Required Permissions**

ohos.permission.FILE\_ACCESS\_PERSIST. For details about how to request the permission, see [Workflow for Requesting Permissions](../../../../../system/security/application-access-control/application-permission-management/requesting-application-permissions/workflow-for-requesting-permissions/document.md).

**Example**

import { BusinessError } from '@kit.BasicServicesKit';
import { picker } from '@kit.CoreFileKit';
import { fileShare } from '@kit.CoreFileKit';

// ···
export async function revokePermissionExample() {
  try {
    let uri = 'file://docs/storage/Users/username/tmp.txt';
    let policyInfo: fileShare.PolicyInfo = {
      uri: uri,
      operationMode: fileShare.OperationMode.READ\_MODE,
    };
    let policies: fileShare.PolicyInfo\[\] = \[policyInfo\];
    fileShare.revokePermission(policies).then(() => {
      console.info('revokePermission successfully');
    }).catch((err: BusinessError<Array<fileShare.PolicyErrorResult>>) => {
      console.error('revokePermission failed with error message: ' + err.message + ', error code: ' + err.code);
      if (err.code == 13900001 && err.data) {
        for (let i = 0; i < err.data.length; i++) {
          console.error('error code : ' + JSON.stringify(err.data\[i\].code));
          console.error('error uri : ' + JSON.stringify(err.data\[i\].uri));
          console.error('error reason : ' + JSON.stringify(err.data\[i\].message));
        }
      }
    });
  } catch (error) {
    let err: BusinessError = error as BusinessError;
    console.error(\`revokePermission failed with err, Error code: ${err.code}, message: ${err.message}\`);
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9e/v3/-ho3_qeuS6y0W4qs-MhSxQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061951Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=69D34C7CFD47F0F56B83513DFFB6C232DA43A808F310E190F9144603E79A3331)

-   The URI in the example comes from the permission persistence data stored for the application.
-   You are advised to activate the persistent permissions based on service requirements. Do not activate all persistent permissions.
-   Before persisting permissions, use **canIUse()** to check whether the device has the required system capability and permission.

For details about how to revoke a persistent permission using C/C++ APIs, see [OH\_FileShare\_RevokePermission](../persisting-temporary-permissions-c-c/document.md).

#### Activating a Persistent Permission for Accessing a File or Folder

Each time an application is started, its persistent permissions have not been loaded to the memory. To make a persistent permission still valid after the application is restarted, use [ohos.fileshare.activatePermission](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-fileshare#fileshareactivatepermission11) to activate the permission.

**Required Permissions**

ohos.permission.FILE\_ACCESS\_PERSIST. For details about how to request the permission, see [Workflow for Requesting Permissions](../../../../../system/security/application-access-control/application-permission-management/requesting-application-permissions/workflow-for-requesting-permissions/document.md).

**Example**

import { BusinessError } from '@kit.BasicServicesKit';
import { picker } from '@kit.CoreFileKit';
import { fileShare } from '@kit.CoreFileKit';

// ···
export async function activatePermissionExample() {
  try {
    let uri = 'file://docs/storage/Users/username/tmp.txt';
    let policyInfo: fileShare.PolicyInfo = {
      uri: uri,
      operationMode: fileShare.OperationMode.READ\_MODE,
    };
    let policies: fileShare.PolicyInfo\[\] = \[policyInfo\];
    fileShare.activatePermission(policies).then(() => {
      console.info('activatePermission successfully');
    }).catch((err: BusinessError<Array<fileShare.PolicyErrorResult>>) => {
      console.error('activatePermission failed with error message: ' + err.message + ', error code: ' + err.code);
      if (err.code == 13900001 && err.data) {
        for (let i = 0; i < err.data.length; i++) {
          console.error('error code : ' + JSON.stringify(err.data\[i\].code));
          console.error('error uri : ' + JSON.stringify(err.data\[i\].uri));
          console.error('error reason : ' + JSON.stringify(err.data\[i\].message));
          if (err.data\[i\].code == fileShare.PolicyErrorCode.PERMISSION\_NOT\_PERSISTED) {
            // Persist the permission for a file or folder and then activate it.
          }
        }
      }
    });
  } catch (error) {
    let err: BusinessError = error as BusinessError;
    console.error(\`activatePermission failed with err, Error code: ${err.code}, message: ${err.message}\`);
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9e/v3/mX3z6r5JST-AsAV-T_RIrQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061951Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=AB74FC0D868786A4950399BE42ED807137C020D7341C646B7511ABBF3DD3E3FD)

-   The URI in the example comes from the permission persistence data stored for the application.
-   You are advised to activate the persistent permissions based on service requirements. Do not activate all persistent permissions.
-   If the activation fails because the permission has not been persisted, persist the permission first.
-   Before persisting permissions, use **canIUse()** to check whether the device has the required system capability and permission.

For details about how to activate a persistent permission using C/C++ APIs, see [OH\_FileShare\_ActivatePermission](../persisting-temporary-permissions-c-c/document.md).
