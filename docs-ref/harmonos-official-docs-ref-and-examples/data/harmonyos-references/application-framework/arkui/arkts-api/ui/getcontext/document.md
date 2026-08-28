# getContext

To obtain the current Ability's Context within a page, call the **getContext** API to obtain the [UIAbilityContext](../../../../ability-kit/arkts-apis/dependent-elements-and-definitions/application/uiabilitycontext/document.md) or [ExtensionContext](../../../../ability-kit/arkts-apis/dependent-elements-and-definitions/application/extensioncontext/document.md) associated with the current page.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7d/v3/ttSvLPPZRfqGN9DZyWAQtg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062229Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=1E5E8EB39CEA513D4FDCA5E951C9C53821FDAF8EA58E2BF17682FEB0F01A6933)

-   The initial APIs of this module are supported since API version 9. Newly added APIs will be marked with a superscript to indicate their earliest API version.
-   This API applies only to the stage model.

#### getContext(deprecated)

getContext(component?: Object):Context

Obtains the **Context** object associated with an ability on the page.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/50/v3/_vUxGYueT6eWGbYEtV0y3A/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062229Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=9348D9C31DDBE8B4E224A9FAF3E69C13D1B063967651DF64C8ADDB66811B9AAE)

This API is supported since API version 9 and deprecated since API version 18. You are advised to use **getHostContext** instead. [getHostContext](../ohos-arkui-uicontext-uicontext/class-uicontext/document.md#gethostcontext12) has effect only after first a [UIContext](../ohos-arkui-uicontext-uicontext/class-uicontext/document.md) instance is obtained.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Model restriction**: This API can be used only in the stage model.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| component | Object | No | Ability instance. If no component is passed in or the passed-in parameter type is invalid, the default context is returned. The default context is the context obtained by tracing the call chain of the API. If this API is used in an asynchronous callback or not initially called on the current page, the context of the instance may fail to be traced. In this case, **undefined** is returned. |

**Return value**

| Type | Description |
| :-- | :-- |
| [Context](#context) | Context of the ability. The context type depends on the ability type. For example, if this API is called on a page of the UIAbility, the return value type is UIAbilityContext; if this API is called on a page of the ExtensionAbility, the return value type is ExtensionContext. |

#### Context

type Context = Context

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Model restriction**: This API can be used only in the stage model.

| Type | Description |
| :-- | :-- |
| [Context](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/application-context-stage) | Context of the ability. The context type depends on the ability type. For example, if this API is called on a page of the UIAbility, the return value type is UIAbilityContext; if this API is called on a page of the ExtensionAbility, the return value type is ExtensionContext. |

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/18/v3/dTg6Bc-aTxaULWAU4_KF0w/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062229Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=D925AC62FDF1551ED504086B9AD89E738C5E487E79FE618DE6EFE733C28D1B96)

Directly using **getContext** can lead to the issue of [ambiguous UI context](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/arkts-global-interface#ambiguous-ui-context). To avoid this, obtain a **UIContext** instance using **getUIContext()**, and then obtain the associated **Context** object using [getHostContext](../ohos-arkui-uicontext-uicontext/class-uicontext/document.md#gethostcontext12).

**Example**

Load a page by calling **windowStage.loadContent** in the UIAbility.

// EntryAbility.ets
import { UIAbility, AbilityConstant, Want } from '@kit.AbilityKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { window } from '@kit.ArkUI';

export default class EntryAbility extends UIAbility {
  onCreate(want: Want, launchParam: AbilityConstant.LaunchParam) {
    hilog.info(0x0000, 'testTag', '%{public}s', 'Ability onCreate');
  }

  onDestroy() {
    hilog.info(0x0000, 'testTag', '%{public}s', 'Ability onDestroy');
  }

  onWindowStageCreate(windowStage: window.WindowStage) {
    hilog.info(0x0000, 'testTag', '%{public}s', 'Ability onWindowStageCreate');

    windowStage.loadContent('pages/Index', (err, data) => {
      if (err.code) {
        hilog.error(0x0000, 'testTag', 'Failed to load the content. Cause: %{public}s', JSON.stringify(err) ?? '');
        return;
      }
      hilog.info(0x0000, 'testTag', 'Succeeded in loading the content. Data: %{public}s', JSON.stringify(data) ?? '');
    });
  }

  onWindowStageDestroy() {
    hilog.info(0x0000, 'testTag', '%{public}s', 'Ability onWindowStageDestroy');
  }

  onForeground() {
    hilog.info(0x0000, 'testTag', '%{public}s', 'Ability onForeground');
  }

  onBackground() {
    hilog.info(0x0000, 'testTag', '%{public}s', 'Ability onBackground');
  }
}

In **Index.ets**, **getContext** is used to obtain the context. In this example, the return value type is UIAbilityContext.

//pages/Index.ets
@Entry
@Component
struct Index {
  @State message: string = 'Hello World'

  build() {
    Row() {
      Column() {
        Text(this.message)
          .fontSize(50)
          .fontWeight(FontWeight.Bold)
          .onClick(() => {
            // You are advised to use this.getUIContext().getHostContext().
            let context: Context = getContext(this) as Context;
            console.info("CacheDir:" + context.cacheDir);
          })
      }
      .width('100%')
    }
    .height('100%')
  }
}
