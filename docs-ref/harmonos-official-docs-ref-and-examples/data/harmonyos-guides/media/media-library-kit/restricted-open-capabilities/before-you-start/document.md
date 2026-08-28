# Before You Start

An application needs to obtain a PhotoAccessHelper instance before accessing or modifying the media data in an album. User personal data is involved in the PhotoAccessHelper module. Therefore, the application must also apply for the read and write permissions from the user. Unless otherwise specified, the APIs of the PhotoAccessHelper module are used in **pages/index.ets** of the project or other customized .ets files.

#### Obtaining a PhotoAccessHelper Instance

The application needs to call [getPhotoAccessHelper](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-photoaccesshelper-f#photoaccesshelpergetphotoaccesshelper) to obtain a PhotoAccessHelper instance based on the application context. Then, the application can use the instance obtained to access or modify the media data (such as images and videos) in an album.

**How to Develop**

1.  Import the photoAccessHelper module.
2.  Call **getUIContext().getHostContext()** to obtain the application context.
3.  Obtain a PhotoAccessHelper instance.

import { photoAccessHelper } from '@kit.MediaLibraryKit';
import { common } from '@kit.AbilityKit';

// The photoAccessHelper instance obtained here is a global object. Unless otherwise specified, the object obtained here is used in subsequent operations in this document. If an undefined error is reported, add the code snippet here.
// Obtain the context from the component and ensure that the return value of this.getUiContext().getHostContext() is UIAbilityContext.
@Entry
@Component
struct Index {
  @State outputText: string = 'Supported formats:\\n';

  build() {
    Row() {
      Button("example").onClick(async () => {
        let context: Context = this.getUIContext().getHostContext() as common.UIAbilityContext;
        let phAccessHelper = photoAccessHelper.getPhotoAccessHelper(context);
      }).width('100%')
    }
    .height('90%')
  }
}

#### Requesting Permissions

Before requesting the permissions for the PhotoAccessHelper module, ensure that the [basic principles for using permissions](../../../../system/security/application-access-control/application-permission-management/application-permission-management-overview/document.md#basic-principles-for-using-permissions) are met. The following permissions are required.

| Permission | Description | Authorization Mode |
| :-- | :-- | :-- |
| ohos.permission.READ\_IMAGEVIDEO | Allows an application to read images and videos in the media library. | user\_grant |
| ohos.permission.WRITE\_IMAGEVIDEO | Allows an application to read and write images and videos in the media library. | user\_grant |
| ohos.permission.MEDIA\_LOCATION | Allows an application to access geographical locations in the user's media file. | user\_grant |

The required permissions must be authorized by the user. After adding the permissions in the **module.json5** file, use [abilityAccessCtrl.requestPermissionsFromUser](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-abilityaccessctrl#requestpermissionsfromuser9) to check whether the required permissions are granted by the user. If yes, the application can access and manipulate the data. Otherwise, display a dialog box to request user authorization.

**How to Develop**

1.  The permissions mentioned earlier are restricted permissions, typically not granted to third-party applications. However, if you require these permissions in specific scenarios, submit relevant application materials and apply for permission certificates through AppGallery Connect (AGC). Before the application, refer to the [Restricted Development Permissions](../../../../system/security/application-access-control/application-permission-management/application-permissions/restricted-permissions/document.md) to confirm the appropriate permission scenarios. Then, follow the steps outlined in [Requesting Restricted Permissions](../../../../system/security/application-access-control/application-permission-management/requesting-application-permissions/requesting-restricted-permissions/document.md) to apply for the permissions.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d1/v3/4fOuVtqBTj-HbetrAJIBaw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062044Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=F0CA28C7FB9899757DAD50CCC246674EA9F4AFC4FF4EA440F8B705BCCE05A4C6)

Even if the user has granted the permission, the permission will still be checked before an API protected by the permission is called. The permission granted status should not be persisted, because the user can revoke the permission through the system application **Settings**.
