# Inheriting Media File Access Permissions After Device Upgrade

If an application, running on HarmonyOS 3.1 Release (API version 9) or earlier, has the permission to access images/videos and stores their paths or URIs within the application, it can access the images/videos in real-time when entering specific UIs.

However, after the device is upgraded to HarmonyOS 5.0.2 or later, the method for accessing media files changes. The application can no longer use the original paths or URIs to access these files. In addition, the new version does not allow applications to directly access media files by default. To regain access, the application must request the media file access permission from users. Once granted, the application can inherit the original permission.

This guide describes how to inherit the media file access permission after the upgrade.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f1/v3/-_Z1vjarSq-DjFkEDXR23w/en-us_image_0000002220860121.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062044Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=20FC900128A106CFA6081AC4D5C2175AE9E2D308ABE704A69E73EBCFDFD2F780)

Once the application is initiated or navigates to the corresponding UI, it obtains from the application data the URIs of media files that previously had permissions on HarmonyOS 3.1/4.0 and now require inherited permissions. It then calls the [convertFileUris()](https://developer.huawei.com/consumer/en/doc/harmonyos-references/scenario-fusion-fileuriresult#section1272664195920) API of Scenario Fusion Kit to obtain the URIs accessible on HarmonyOS 5.0. Following this, it calls the [requestPhotoUrisReadPermission()](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-photoaccesshelper-photoaccesshelper#requestphotourisreadpermission14) API of Media Library Kit, passing the URIs of the media files that need the inherited access permission, to launch the authorization page. On the authorization page, image/video thumbnails are displayed based on the input URIs. Users can select the desired images/videos and grant permission, thereby enabling the application to access these files.

The following figure shows the effect on the UI.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a9/v3/BkDdKDU4QvmfYm4_tSlTCg/en-us_image_0000002220785681.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062044Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=5B7BB18AE3A1B1B6A02E4B60A1C77DB120F1FB8402C0BB02A8877DAEB555F125 "Click to enlarge")

#### How to Develop

This section describes how to call the [requestPhotoUrisReadPermission()](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-photoaccesshelper-photoaccesshelper#requestphotourisreadpermission14) API of Media Library Kit. In this API, enter the URIs of the media files that need the inherited access permission and launch the authorization page.

For details about how to call the [convertFileUris()](https://developer.huawei.com/consumer/en/doc/harmonyos-references/scenario-fusion-fileuriresult#section1272664195920) API of Scenario Fusion Kit to obtain the URIs accessible on HarmonyOS 5.0, see [Public Directory File URI Inheritance](../../../application-framework/core-file-kit/application-files/application-data-backup-and-restore/guidelines-on-application-data-migration-and-adaptation-after-device-upgrade/precautions-for-code-development-during-application-upgrade/document.md#section174971342123917).

1.  Import the modules.
    
    import { photoAccessHelper } from '@kit.MediaLibraryKit';
    
2.  Initialize the input URIs.
    
    // Used for the interface class instance during initialization.
    // Obtain the context from the component and ensure that the return value of this.getUiContext().getHostContext() is UIAbilityContext.
    import { common } from '@kit.AbilityKit';
    let context: Context = this.getUIContext().getHostContext() as common.UIAbilityContext;
    let phAccessHelper: photoAccessHelper.PhotoAccessHelper = photoAccessHelper.getPhotoAccessHelper(context);
    
3.  Initialize the input URIs and assign a value.
    
    private uris: Array<string> = new Array<string>();
    // Enter the URIs to be authorized.
    this.uris = \[\];
    
4.  Open the authorization page.
    
    try {
      phAccessHelper.requestPhotoUrisReadPermission(uri).then((result: Array<string>) => {
        console.info("requestPhotoUrisReadPermission, result = " + JSON.stringify(result));
        if (result) {
          // The URIs authorized are returned.
        } else {
          // Handle authorization failures.
        }
      })
    } catch(error) {
      console.error("requestPhotoUrisReadPermission error: " + JSON.stringify(error));
    }
    

#### Sample Code

import { photoAccessHelper } from '@kit.MediaLibraryKit';
import { common } from '@kit.AbilityKit';
@Entry
@Component
struct Index{
  private uris: Array<string> = new Array<string>();

  build() {
    Row() {
      Column() {
        Button("Trigger authorization").width('100%').height('10%').margin({top: 150})
          .onClick(()=>{
            // Enter the URIs to be authorized.
            this.uris = \[\];
            let context: Context = this.getUIContext().getHostContext() as common.UIAbilityContext;
            let phAccessHelper: photoAccessHelper.PhotoAccessHelper = photoAccessHelper.getPhotoAccessHelper(context);
            try {
              phAccessHelper.requestPhotoUrisReadPermission(this.uris).then((result: Array<string>) => {
                console.info("requestPhotoUrisReadPermission, result = " + JSON.stringify(result));
                if (result) {
                  // The URIs authorized are returned.
                } else {
                  // Handle authorization failures.
                }
              })
            } catch(error) {
              console.error("requestPhotoUrisReadPermission error: " + JSON.stringify(error));
            }
          })
      }
      .width('100%')
    }
    .height('100%')
  }
}
