# Requesting Permissions to Access the Pasteboard

#### Overview

In API version 12 and later, permission control is added to the pasteboard reading API to enhance user privacy protection.

Related APIs:

| Name | Description |
| :-- | :-- |
| [getData(callback: AsyncCallback<PasteData>): void](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-pasteboard#getdata9) | Reads a **PasteData** object from the pasteboard. This API uses an asynchronous callback to return the result. |
| [getData(): Promise<PasteData>](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-pasteboard#getdata9-1) | Reads a **PasteData** object from the pasteboard. This API uses a promise to return the result. |
| [getDataSync(): PasteData](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-pasteboard#getdatasync11) | Reads data from the system pasteboard. This API returns the result synchronously. |
| [getUnifiedData(): Promise<unifiedDataChannel.UnifiedData>](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-pasteboard#getunifieddata12) | Reads the data of a unified data object from the system pasteboard. |
| [getUnifiedDataSync(): unifiedDataChannel.UnifiedData](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-pasteboard#getunifieddatasync12) | Reads the data of a unified data object from the system pasteboard. This API returns the result synchronously. |
| [OH\_UdmfData\* OH\_Pasteboard\_GetData (OH\_Pasteboard \*pasteboard, int \*status)](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-oh-pasteboard-h#oh_pasteboard_getdata) | Obtains data from the pasteboard. |
| [getDataWithProgress(params: GetDataParams): Promise<PasteData>](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-pasteboard#getdatawithprogress15) | Obtains the pasteboard data and paste progress. This API uses a promise to return the result. Folders cannot be copied. |
| [OH\_UdmfData\* OH\_Pasteboard\_GetDataWithProgress(OH\_Pasteboard\* pasteboard, Pasteboard\_GetDataParams\* params, int\* status)](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-oh-pasteboard-h#oh_pasteboard_getdatawithprogress) | Obtains the pasteboard data and paste progress. Folders cannot be copied. |

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c9/v3/Y1KOOEDHQ2mKfK8ilImTWQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062021Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=BFADB96CA0BA0B1A810EB96D9AB998D0636EBF7DAC09F40F95C02FB81E951585)

Before requesting the pasteboard permission, an application needs to check whether the pasteboard contains the required data. For example, use **hasData** to check whether there is data in the pasteboard, **hasDataType** or **getMimeTypes** to check whether required data types are contained, and **getChangeCount** to check whether the data changes. For details, see [Optimizing Pasteboard Dialog Box Adaptation](#optimizing-pasteboard-dialog-box-adaptation).

#### Accessing Pasteboard Content

Applications can access the pasteboard content in either of the following ways:

-   Using security components
    
    Applications that use [PasteButton](../../../../security/application-access-control/using-security-components/using-pastebutton/document.md) can access the pasteboard content without the need to request permissions.
    
    Applications that use the security components can access the pasteboard content without any adaptation.
    
-   Requesting the ohos.permission.READ\_PASTEBOARD permission
    
    This is a restricted user\_grant permission. After an application that uses custom components requests this permission, the application can access the pasteboard content with user authorization.
    
    How to request permissions:
    

1.  Check whether the application meets the requirements for requesting the permission according to the [READ\_PASTEBOARD](../../../../security/application-access-control/application-permission-management/application-permissions/restricted-permissions/document.md#ohospermissionread_pasteboard) description.
2.  [Request a release profile in AGC](https://developer.huawei.com/consumer/en/doc/app/agc-help-add-releaseprofile-0000001914714796), which will be used for configuring application signing information.
3.  [Declare the permission](../../../../security/application-access-control/application-permission-management/requesting-application-permissions/declaring-permissions/document.md) in the module.json5 file.
4.  [Request user authorization](../../../../security/application-access-control/application-permission-management/requesting-application-permissions/requesting-user-authorization/document.md) in a dialog box.

#### Optimizing Pasteboard Dialog Box Adaptation

Before requesting the pasteboard permission, an application needs to check whether the pasteboard contains the required data to avoid invalid dialog boxes.

-   Use [hasData](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-pasteboard#hasdata9) to check whether the pasteboard contains data. If no data is contained, the application does not access the pasteboard.
    
-   Use [hasDataType](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-pasteboard#hasdatatype11) or [getMimeTypes](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-pasteboard#getmimetypes14) to check whether the pasteboard contains the data types supported by the application. If no supported data type is contained, the application does not access the pasteboard.
    
-   Use [getChangeCount](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-pasteboard#getchangecount18) to obtain the number of pasteboard content changes and compare it with the number of changes queried when the pasteboard is read last time. If the numbers are the same, the pasteboard content does not change and the application does not access the pasteboard.
    
-   Use [detectPatterns](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-pasteboard#detectpatterns13) to detect patterns on the local pasteboard. If the application password does not match the pattern, the application does not access the pasteboard. If the application password matches the pattern, it is recommended that the application use [clearData](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-pasteboard#cleardata9) to clear the password in the pasteboard.
    

#### Sample Code

import { BusinessError, pasteboard } from '@kit.BasicServicesKit';
import { abilityAccessCtrl, common, Permissions } from '@kit.AbilityKit';
import { preferences } from '@kit.ArkData';
import { hilog } from '@kit.PerformanceAnalysisKit';

const permissions: Permissions\[\] = \['ohos.permission.READ\_PASTEBOARD'\];
const systemPasteboard: pasteboard.SystemPasteboard = pasteboard.getSystemPasteboard();
const patterns: pasteboard.Pattern\[\] = \[pasteboard.Pattern.URL, pasteboard.Pattern.EMAIL\_ADDRESS\];
let dataPreferences: preferences.Preferences | null = null;
// ...
async function isNeedGetPermissionFromUser(): Promise<boolean> {
  try {
    let hasData: boolean = await systemPasteboard.hasData();
    if (!hasData) {
      // Pasteboard does not have data. No permission is required.
      return false;
    }
    // Obtain the number of content changes in the pasteboard.
    let result: number = systemPasteboard.getChangeCount();
    hilog.info(0xFF00, '\[Sample\_pasteboard\]', 'Succeeded in getting the ChangeCount. Result: ${result}');
    // Read the value of changeCount stored last time from Preferences.
    let storedChangeCount: number = dataPreferences ? Number(dataPreferences.getSync('pasteboardChangeCount', 0)) : 0;
    if (result === storedChangeCount) {
      // The pasteboard data does not change. No permission is required.
      return false;
    }
  } catch (err) {
    hilog.error(0xFF00, '\[Sample\_pasteboard\]', 'Failed to get the ChangeCount. Cause: ${err.message}');
    return false;
  };

  // Check whether the pasteboard contains the data type required by the application.
  try {
    // (Optional) Check whether the data type required by the application exists.
    let result: boolean = systemPasteboard.hasDataType(pasteboard.MIMETYPE\_TEXT\_PLAIN);
    hilog.info(0xFF00, '\[Sample\_pasteboard\]', 'Succeeded in checking the DataType. Result: ${result}');
    if (!result) {
      // The pasteboard does not contain the data type required by the application. No permission is required.
      return false;
    }
    // (Optional) If the copied contents contain passwords or other special contents, use detectPatterns to filter out the unwanted contents.
    let data: pasteboard.Pattern\[\] = await systemPasteboard.detectPatterns(patterns);
    if (patterns.sort().join('') != data.sort().join('')) {
      hilog.info(0xFF00, '\[Sample\_pasteboard\]', 'Not all needed patterns detected, no need to get data.');
      return false;
    }
  } catch (err) {
    hilog.error(0xFF00, '\[Sample\_pasteboard\]', 'Failed to check the DataType. Cause:' + err.message);
    return false;
  };
  return true;
}

@Entry
@Component
struct Index {
  // ...

  build() {
    Row() {
      Column() {
        // ...
        Button('Paste')
          // ...
          .onClick(() => {
            const context: common.UIAbilityContext = this.getUIContext().getHostContext() as common.UIAbilityContext;
            if (!isNeedGetPermissionFromUser()) {
              hilog.info(0xFF00, '\[Sample\_pasteboard\]', 'No need to bring up the permission pop-up window');
              return;
            }
            let atManager: abilityAccessCtrl.AtManager = abilityAccessCtrl.createAtManager();
            // Determine whether to display a user authorization dialog box based on the return value of requestPermissionsFromUser.
            atManager.requestPermissionsFromUser(context, permissions).then((data) => {
              let grantStatus: number\[\] = data.authResults;
              for (const status of grantStatus) {
                if (status === 0) {
                  // Use the get operation to read the pasteboard content after user authorization.
                  // ...
                  // Determine whether the password is of the current application and use the cleardata API to clear the password in the pasteboard after obtaining the data.
                  systemPasteboard.clearData().then((data: void) => {
                    hilog.info(0xFF00, '\[Sample\_pasteboard\]', 'Succeeded in clearing the pasteboard.');
                  }).catch((err: BusinessError) => {
                    hilog.error(0xFF00, '\[Sample\_pasteboard\]', 'Failed to clear the pasteboard. Cause: ${err.message}');
                  });
                  // Obtain the value of current ChangeCount.
                  let currentChangeCount: number = systemPasteboard.getChangeCount();
                  hilog.info(0xFF00, '\[Sample\_pasteboard\]', 'Current ChangeCount: ' + currentChangeCount);
                  // Update the value of ChangeCount in Preferences.
                  if (dataPreferences) {
                    dataPreferences.putSync('pasteboardChangeCount', currentChangeCount);
                    dataPreferences.flushSync(); // Flush data to Preferences for persistent storage.
                    hilog.info(0xFF00, '\[Sample\_pasteboard\]', 'ChangeCount has been updated to: ' + currentChangeCount);
                  }
                } else {
                  // If the user denies the permission, display a message indicating that user authorization is required, and direct the user to set the permission in Settings.
                  return;
                }
              }
              // Authorization is successful.
            }).catch((err: BusinessError) => {
              hilog.error(0xFF00, '\[Sample\_pasteboard\]', 'Failed to request permissions from user. ');
            })
          })
        // ...
      }
      // ...
    }
    // ...
  }
}
