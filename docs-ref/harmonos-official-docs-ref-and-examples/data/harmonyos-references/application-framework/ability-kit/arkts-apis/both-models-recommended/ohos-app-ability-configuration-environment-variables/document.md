# @ohos.app.ability.Configuration (Environment Variables)

The module defines the environment variables for the application runtime, including language, dark/light color mode, screen orientation, and font size. You can subscribe to these environment variables to adapt to different user preferences and enhance the interaction experience.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/78/v3/IDPNDMYeQx2p4w5wXkGpcg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062207Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=6DF66388CCC3F1FF83461120B096C3E703E581B54604A7E939D27CE2A6923853)

The initial APIs of this module are supported since API version 9. Newly added APIs will be marked with a superscript to indicate their earliest API version.

#### Modules to Import

import { Configuration } from '@kit.AbilityKit';

#### Configuration

**System capability**: SystemCapability.Ability.AbilityBase

| Name | Type | Read-only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| language | string | No | Yes | 
Current language of the application, for example, **zh** (Chinese) or **en** (English).

You can [set the application language](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/subscribe-system-environment-variable-changes#setting-application-language).

For details about the value range, see [getSystemLanguages](../../../../localization-kit/arkts-apis/ohos-i18n-internationalization/document.md#getsystemlanguages9).

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| colorMode | [ConfigurationConstant.ColorMode](../ohos-app-ability-configurationconstant-constants-related-to-environment-variable/document.md#colormode) | No | Yes | 

Dark/Light color mode of the application. The light color mode is used by default.

You can [set the dark/light color mode for an application or a component](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/subscribe-system-environment-variable-changes#setting-darklight-color-mode).

The options are as follows:

\- **COLOR\_MODE\_NOT\_SET**: The color mode is not set.

\- **COLOR\_MODE\_LIGHT**: light mode.

\- **COLOR\_MODE\_DARK**: dark mode.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| direction | [ConfigurationConstant.Direction](../ohos-app-ability-configurationconstant-constants-related-to-environment-variable/document.md#direction) | No | Yes | 

Screen orientation of the application.

The options are as follows:

\- **DIRECTION\_NOT\_SET**: The screen orientation is not set.

\- **DIRECTION\_HORIZONTAL**: horizontal direction.

\- **DIRECTION\_VERTICAL**: vertical direction.

You can subscribe to changes to this environment variable in the [UIAbility](../../stage-model/ohos-app-ability-uiability-ability-with-ui/document.md) and [UIExtensionAbility](../../stage-model/ohos-app-ability-uiextensionability-extensionability-with-ui/document.md), but not in the [ApplicationContext](../../dependent-elements-and-definitions/application/applicationcontext-application-context/document.md) or [AbilityStage](../../stage-model/ohos-app-ability-abilitystage-abilitystage-component-manager/document.md).

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| screenDensity | [ConfigurationConstant.ScreenDensity](../ohos-app-ability-configurationconstant-constants-related-to-environment-variable/document.md#screendensity) | No | Yes | 

Screen density.

The options are as follows:

\- **SCREEN\_DENSITY\_NOT\_SET**: The pixel density is not set.

\- **SCREEN\_DENSITY\_SDPI**: 120.

\- **SCREEN\_DENSITY\_MDPI**: 160.

\- **SCREEN\_DENSITY\_LDPI**: 240.

\- **SCREEN\_DENSITY\_XLDPI**: 320.

\- **SCREEN\_DENSITY\_XXLDPI**: 480.

\- **SCREEN\_DENSITY\_XXXLDPI**: 640.

The font size is positively correlated with the screen pixel density. By monitoring changes in the screen pixel density, you can detect adjustments in the font size. Typically, for the same physical size, the higher the screen pixel density, the larger the font display effect.

You can subscribe to changes to this environment variable in the [UIAbility](../../stage-model/ohos-app-ability-uiability-ability-with-ui/document.md) and [UIExtensionAbility](../../stage-model/ohos-app-ability-uiextensionability-extensionability-with-ui/document.md), but not in the [ApplicationContext](../../dependent-elements-and-definitions/application/applicationcontext-application-context/document.md) or [AbilityStage](../../stage-model/ohos-app-ability-abilitystage-abilitystage-component-manager/document.md).

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| displayId | number | No | Yes | 

ID of the display where the application is located.

You can subscribe to changes to this environment variable in the [UIAbility](../../stage-model/ohos-app-ability-uiability-ability-with-ui/document.md) and [UIExtensionAbility](../../stage-model/ohos-app-ability-uiextensionability-extensionability-with-ui/document.md), but not in the [ApplicationContext](../../dependent-elements-and-definitions/application/applicationcontext-application-context/document.md) or [AbilityStage](../../stage-model/ohos-app-ability-abilitystage-abilitystage-component-manager/document.md).

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| hasPointerDevice | boolean | No | Yes | 

Whether a pointer device, such as a keyboard, mouse, or touchpad, is connected. **true** if connected, **false** otherwise.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| fontId14+ | string | No | Yes | 

Unique ID of the font.

**Atomic service API**: This API can be used in atomic services since API version 14.

 |
| fontSizeScale12+ | number | No | Yes | 

Font size scale ratio. The value is a non-negative number. The default value is **1**.

You can [set the font size for an application](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/subscribe-system-environment-variable-changes#setting-font-size).

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| fontWeightScale12+ | number | No | Yes | 

Font weight scale ratio. The value is a non-negative number. The default value is **1**.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| mcc12+ | string | No | Yes | 

Mobile country code.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| mnc12+ | string | No | Yes | 

Mobile network code.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| locale20+ | [Intl.Locale](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/Locale) | No | Yes | 

Locale.

The application automatically adjusts its behavior based on the current locale to meet the localization requirements of users. This property can be set by configuring the system language, system region, and application preferred language.

**Atomic service API**: This API can be used in atomic services since API version 20.

 |

**Example**

import { UIAbility, AbilityConstant, EnvironmentCallback, Want } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

export default class EntryAbility extends UIAbility {
  onCreate(want: Want, launchParam: AbilityConstant.LaunchParam) {
    let envCallback: EnvironmentCallback = {
      onConfigurationUpdated(config) {
        console.info(\`envCallback onConfigurationUpdated success: ${JSON.stringify(config)}\`);
        let language = config.language;
        let colorMode = config.colorMode;
        let direction = config.direction;
        let screenDensity = config.screenDensity;
        let displayId = config.displayId;
        let hasPointerDevice = config.hasPointerDevice;
        let fontId = config.fontId;
        let fontSizeScale = config.fontSizeScale;
        let fontWeightScale = config.fontWeightScale;
        let mcc = config.mcc;
        let mnc = config.mnc;
        let locale = config.locale;
      },
      onMemoryLevel(level) {
        console.info(\`onMemoryLevel level: ${level}\`);
      }
    };
    try {
      let applicationContext = this.context.getApplicationContext();
      let callbackId = applicationContext.on('environment', envCallback);
      console.info(\`callbackId: ${callbackId}\`);
    } catch (paramError) {
      console.error(\`error: ${(paramError as BusinessError).code}, ${(paramError as BusinessError).message}\`);
    }
  }
}
