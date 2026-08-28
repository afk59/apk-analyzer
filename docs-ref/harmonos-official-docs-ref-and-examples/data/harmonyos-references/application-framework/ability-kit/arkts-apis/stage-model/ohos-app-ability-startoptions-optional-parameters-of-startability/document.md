# @ohos.app.ability.StartOptions (Optional Parameters of startAbility)

StartOptions can be used as an input parameter for APIs used to start a UIAbility (for example, [startAbility()](../../dependent-elements-and-definitions/application/uiabilitycontext/document.md#startability-1)). It specifies the options for starting the target UIAbility, including but not limited to the window mode and the display where the target UIAbility is started.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/92/v3/xK99rDzEQ2CdV9-i17klgA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062206Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=757EBC0F41BAD4630AE4A4A487AE11EAA3D8F349817B099E16F92AE7145ACCC1)

-   The initial APIs of this module are supported since API version 9. Newly added APIs will be marked with a superscript to indicate their earliest API version.
    
-   The APIs of this module can be used only in the stage model.
    

#### Modules to Import

import { StartOptions } from '@kit.AbilityKit';

#### StartOptions

StartOptions is used to specify the options for starting a UIAbility.

**System capability**: SystemCapability.Ability.AbilityRuntime.Core

| Name | Type | Read-only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| windowMode12+ | number | No | Yes | Window mode for the UIAbility upon startup. For details, see [WindowMode](../ohos-app-ability-abilityconstant-ability-related-constants/document.md#windowmode12). |
| displayId | number | No | Yes | 
Display ID, which is an integer greater than or equal to -1.

\- The value **\-1** means the current screen.

\- The value **0** means the primary screen.

\- A positive integer means a specific screen with that ID.

**NOTE**

Starting from API version 14, the default value is **\-1**, indicating the current screen.

In versions earlier than API version 14, the default value is **0**, indicating the primary screen.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| withAnimation11+ | boolean | No | Yes | 

Whether animation effects are used for the UIAbility upon startup. **true** if used, **false** otherwise.

**Constraints**:

1\. This property takes effect only on 2-in-1 devices and tablets.

2\. The caller and target must be the same application.

 |
| windowLeft11+ | number | No | Yes | 

With the top-left vertex of the screen specified by displayId as the origin, this value represents the window's offset along the x-axis (in px). A positive value indicates the window is to the right of the origin, while a negative value indicates it is to the left of the origin. The value is an integer. Non-integer values will be rounded down. When the top-left vertex of the window exceeds the screen area of the specified **displayId**, the window is restricted to be visible only within the screen range of the specified **displayId**. When configuring this field, you are advised to configure **windowTop** at the same time.

**Constraints**:

This function takes effect only in the [freeform window](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/window-terminology#freeform-window) state.

 |
| windowTop11+ | number | No | Yes | 

With the top-left vertex of the screen specified by displayId as the origin, this value represents the window's offset along the y-axis (in px). A positive value indicates the window is below the origin, while a negative value indicates it is above the origin. The value is an integer. Non-integer values will be rounded down. When the top of the window exceeds the screen area of the specified **displayId**, the window is restricted to be visible only within the screen range of the specified **displayId**. When configuring this field, you are advised to also configure **windowLeft**.

**Constraints**:

This function takes effect only in the [freeform window](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/window-terminology#freeform-window) state.

 |
| windowWidth11+ | number | No | Yes | 

Window width, in px.

The value range is \[**minWindowWidth**, **maxWindowWidth**\], with the unit being vp. You can call [vp2px](../../../../arkui/arkts-api/ui/ohos-arkui-uicontext-uicontext/class-uicontext/document.md#vp2px12) to convert it to the corresponding px value.

**Constraints**:

This function takes effect only in the [freeform window](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/window-terminology#freeform-window) state.

 |
| windowHeight11+ | number | No | Yes | 

Window height, in px.

The value range is \[**minWindowHeight**, **maxWindowHeight**\], with the unit being vp. You can call [vp2px](../../../../arkui/arkts-api/ui/ohos-arkui-uicontext-uicontext/class-uicontext/document.md#vp2px12) to convert it to the corresponding px value.

**Constraints**:

This function takes effect only in the [freeform window](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/window-terminology#freeform-window) state.

 |
| processMode12+ | [contextConstant.ProcessMode](../ohos-app-ability-contextconstant-context-related-constants/document.md#processmode12) | No | Yes | 

Process mode of the UIAbility after it is started.

**Constraints**:

1\. This property takes effect only on 2-in-1 devices and tablets.

2\. This property takes effect only in [UIAbilityContext.startAbility](../../dependent-elements-and-definitions/application/uiabilitycontext/document.md#startability-1).

3\. **processMode** and **startupVisibility** must be set in pair.

 |
| startupVisibility12+ | [contextConstant.StartupVisibility](../ohos-app-ability-contextconstant-context-related-constants/document.md#startupvisibility12) | No | Yes | 

Visibility status of the UIAbility after it is started. If the target UIAbility is set to invisible, the window of the target UIAbility is not displayed in the foreground, there is no icon in the dock, and the **onForeground** lifecycle of the target UIAbility is not triggered.

**Constraints**:

1\. This property takes effect only on 2-in-1 devices and tablets.

2\. This property takes effect only in [UIAbilityContext.startAbility](../../dependent-elements-and-definitions/application/uiabilitycontext/document.md#startability-1).

3\. **processMode** and **startupVisibility** must be set in pair.

 |
| startWindowIcon14+ | [image.PixelMap](../../../../../media/image-kit/arkts-apis/ohos-multimedia-image-image-processing/interface-pixelmap/document.md) | No | Yes | 

Icon displayed on the starting window for the UIAbility of the current application upon startup. If this property is not set, the value of **startWindowIcon** in the **module.json5** file is used by default.

**Constraints**:

\- This property does not take effect for the UIAbility of another application.

\- This property takes effect only on 2-in-1 devices and tablets.

\- This property takes effect only in [UIAbilityContext.startAbility](../../dependent-elements-and-definitions/application/uiabilitycontext/document.md#startability-1).

\- The maximum size of an image used as the startup icon is 600 MB.

 |
| startWindowBackgroundColor14+ | string | No | Yes | 

Background color of the window for the UIAbility of the current application upon startup. The value is in ARGB format, for example, **#E5FFFFFF**. If this property is not set, the value of **startWindowBackground** in the **module.json5** file is used by default.

**Constraints**:

\- This property does not take effect for the UIAbility of another application.

\- This property takes effect only on 2-in-1 devices and tablets.

\- This property takes effect only in [UIAbilityContext.startAbility](../../dependent-elements-and-definitions/application/uiabilitycontext/document.md#startability-1).

 |
| supportWindowModes14+ | Array<[bundleManager.SupportWindowMode](../../both-models-recommended/ohos-bundle-bundlemanager-bundle-management-module/document.md#supportwindowmode)\> | No | Yes | 

Window mode supported by the UIAbility when it is started. The supported window mode specifies whether to display the maximize, minimize, or split-screen button. If this property is not set, the value of **supportWindowMode** configured under [abilities](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/module-configuration-file#abilities) in the [module.json5](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/module-configuration-file) file corresponding to the UIAbility is used by default.

\- **FULL\_SCREEN**: full-screen mode.

\- **FLOATING**: floating window mode.

\- **SPLIT**: split-screen mode. Generally, **FULL\_SCREEN** or **FLOATING** must be used together. You are not advised to configure only **SPLIT**. If only **SPLIT** is configured, the window on 2-in-1 devices is in floating window mode by default and can transition to the split-screen mode, and the window on tablets is in full-screen mode by default and can transition to the split-screen mode.

When **FULL\_SCREEN** and **SPLIT** are both configured for a [freeform window](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/window-terminology#freeform-window), the window will be started in floating window mode if the value of [targetAPIVersion](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/app-configuration-file#tags-in-the-configuration-file) is less than 15, and in full-screen mode if the value is greater than or equal to 15.

**Constraints**:

This property takes effect only on 2-in-1 devices and tablets.

 |
| minWindowWidth17+ | number | No | Yes | 

Minimum width of the window, in vp. You can call [getWindowLimitsVP](../../../../arkui/arkts-api/window-manager/ohos-window-window/interface-window/document.md#getwindowlimitsvp22) to obtain the size limit of the current window.

**Constraints**:

This function takes effect only in the [freeform window](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/window-terminology#freeform-window) state.

 |
| minWindowHeight17+ | number | No | Yes | 

Minimum height of the window, in vp. You can call [getWindowLimitsVP](../../../../arkui/arkts-api/window-manager/ohos-window-window/interface-window/document.md#getwindowlimitsvp22) to obtain the size limit of the current window.

**Constraints**:

This function takes effect only in the [freeform window](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/window-terminology#freeform-window) state.

 |
| maxWindowWidth17+ | number | No | Yes | 

Maximum width of the window, in vp. You can call [getWindowLimitsVP](../../../../arkui/arkts-api/window-manager/ohos-window-window/interface-window/document.md#getwindowlimitsvp22) to obtain the size limit of the current window.

**Constraints**:

This function takes effect only in the [freeform window](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/window-terminology#freeform-window) state.

 |
| maxWindowHeight17+ | number | No | Yes | 

Maximum height of the window, in vp. You can call [getWindowLimitsVP](../../../../arkui/arkts-api/window-manager/ohos-window-window/interface-window/document.md#getwindowlimitsvp22) to obtain the size limit of the current window.

**Constraints**:

This function takes effect only in the [freeform window](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/window-terminology#freeform-window) state.

 |
| completionHandler20+ | [CompletionHandler](../ohos-app-ability-completionhandler-application-launch-result-handler/document.md) | No | Yes | 

Operation class used to handle the result of an application launch request.

**Atomic service API**: This API can be used in atomic services since API version 20.

 |
| hideStartWindow20+ | boolean | No | Yes | 

Whether to hide the starting window for the UIAbility of the current application upon startup. The options include **true** (yes) and **false** (no). For details about the starting window and its specifications, see [StartWindow](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/module-configuration-file#startwindow).

**Constraints**:

1\. This property takes effect only on tablets in free windows mode and 2-in-1 devices.

2\. This property applies only for an attempt to launch the UIAbility of the current application.

 |
| windowCreateParams20+ | [window.WindowCreateParams](../../../../arkui/arkts-api/window-manager/ohos-window-window/interfaces-others/document.md#windowcreateparams20) | No | Yes | Parameters for the window for the UIAbility upon startup. |

**Example**

import { UIAbility, Want, StartOptions, bundleManager, CompletionHandler } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { image } from '@kit.ImageKit';
import { window } from '@kit.ArkUI';

export default class EntryAbility extends UIAbility {
  onForeground() {
    let want: Want = {
      deviceId: '',
      bundleName: 'com.example.myapplication',
      abilityName: 'EntryAbility'
    };

    let completionHandler: CompletionHandler = {
      onRequestSuccess: (elementName: bundleManager.ElementName, message: string): void => {
        console.info(\`${elementName.bundleName}-${elementName.moduleName}-${elementName.abilityName} start succeeded: ${message}\`);
      },
      onRequestFailure: (elementName: bundleManager.ElementName, message: string): void => {
        console.error(\`${elementName.bundleName}-${elementName.moduleName}-${elementName.abilityName} start failed: ${message}\`);
      }
    };

    let color = new ArrayBuffer(512 \* 512 \* 4); // Create an ArrayBuffer object to store image pixels. The size of the object is (height \* width \* 4) bytes.
    let imagePixelMap: image.PixelMap;
    let windowParam: window.WindowCreateParams = {};
    let bufferArr = new Uint8Array(color);
    for (let i = 0; i < bufferArr.length; i += 4) {
      bufferArr\[i\] = 255;
      bufferArr\[i+1\] = 0;
      bufferArr\[i+2\] = 122;
      bufferArr\[i+3\] = 255;
    }
    image.createPixelMap(color, {
      editable: true, pixelFormat: image.PixelMapFormat.RGBA\_8888, size: { height: 512, width: 512 }
    }).then((data) => {
      imagePixelMap = data;
      let options: StartOptions = {
        displayId: 0,
        startWindowIcon: imagePixelMap,
        startWindowBackgroundColor: '#E510FFFF',
        supportWindowModes: \[
          bundleManager.SupportWindowMode.FULL\_SCREEN,
          bundleManager.SupportWindowMode.SPLIT,
          bundleManager.SupportWindowMode.FLOATING
        \],
        minWindowWidth: 320,
        minWindowHeight: 240,
        maxWindowWidth: 2560,
        maxWindowHeight: 2560,
        completionHandler: completionHandler,
        hideStartWindow: true,
        windowCreateParams: windowParam
      };

      try {
        this.context.startAbility(want, options, (err: BusinessError) => {
          if (err.code) {
            // Process service logic errors.
            console.error(\`startAbility failed, code is ${err.code}, message is ${err.message}\`);
            return;
          }
          // Carry out normal service processing.
          console.info('startAbility succeed');
        });
      } catch (err) {
        // Process input parameter errors.
        let code = (err as BusinessError).code;
        let message = (err as BusinessError).message;
        console.error(\`startAbility failed, code is ${code}, message is ${message}\`);
      }
    }).catch((err: BusinessError) => {
      console.error(\`createPixelMap failed, code is ${err.code}, message is ${err.message}\`);
    });
  }
}
