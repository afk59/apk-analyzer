# App Review Service

With this service, users can leave reviews directly inside the app, without navigating to the details page on AppGallery.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/eb/v3/2L0Um7Q7RgCbUO-WiWDIFw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062059Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=96BAF87E7932759158CE40BEFEAACC912E2EA7F3E38B2E390A84822F629C2095)

From version 6.0.0(20), the app review pop-up can be displayed.

#### Use Cases

-   Launching an app review pop-up
    
    You can use this API to trigger an app review pop-up, allowing users to rate and comment on your app without navigating to the details page on AppGallery.
    

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2d/v3/MqOwLhVNQpCYVsyZ2oLAYA/en-us_image_0000002337734716.jpg?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062059Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=E23A1B092FD5F5683BA0D98781832CF15BBB82E32BE9B6AA31BB6EA554AF46F7 "Click to enlarge")

#### Service Process

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/23/v3/vsOJqdg0TvaIzf5tS3E8JQ/en-us_image_0000002337734720.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062059Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=E70E2F2363DCF6DE15A1607DE0E00C4F2C1E5B8998445EAB25D312FE482ECE5F "Click to enlarge")

1.  The user wants to leave a review within the app.
2.  The app calls **showCommentDialog** to launch an app review pop-up.
3.  AppGallery Kit returns the API call result to the app.
4.  The app displays the review pop-up to the user.

#### Restrictions

The app review service does not support the Emulator. Use a real device for debugging.

#### API Description

The app review service provides the following APIs. For details, please refer to the [API reference](https://developer.huawei.com/consumer/en/doc/harmonyos-references/appgallery-commentmanager).

| 
API

 | 

Description

 |
| :-- | :-- |
| 

[showCommentDialog](https://developer.huawei.com/consumer/en/doc/harmonyos-references/appgallery-commentmanager#section887383520415)(context: common.UIExtensionContext | common.UIAbilityContext): Promise<void>

 | 

Launches an app review pop-up for users to rate and comment on an app.

 |

#### Development Procedure

1.  Import the **commentManager** module and related common modules.
    
    import { commentManager} from '@kit.AppGalleryKit';
    import { hilog } from '@kit.PerformanceAnalysisKit';
    import { BusinessError } from '@kit.BasicServicesKit';
    import type { common } from '@kit.AbilityKit';
    
2.  Call [showCommentDialog](https://developer.huawei.com/consumer/en/doc/harmonyos-references/appgallery-commentmanager) to launch a review pop-up.
    
    try {
      const uiContext = this.getUIContext().getHostContext() as common.UIAbilityContext;
      commentManager.showCommentDialog(uiContext).then(()=>{
        hilog.info(0, 'TAG', "succeeded in showing commentDialog.");
      }).catch((error: BusinessError<Object>) => {
        hilog.error(0, 'TAG', \`showCommentDialog failed, Code: ${error.code}, message: ${error.message}\`);
      });
    } catch (error) {
      hilog.error(0, 'TAG', \`showCommentDialog failed, Code: ${error.code}, message: ${error.message}\`);
    }
