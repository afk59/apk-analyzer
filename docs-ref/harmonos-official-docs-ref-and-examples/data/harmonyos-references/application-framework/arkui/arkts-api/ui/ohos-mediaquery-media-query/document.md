# @ohos.mediaquery (Media Query)

The **mediaquery** module provides different styles for different media types.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b9/v3/v0AkXFG_Q9C89LGQxFgp9w/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062229Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=9DCA7CE17931488EBCD0C57A8E4DE676BE5FFE7F2401E1DF9D5AA846D998980C)

-   The initial APIs of this module are supported since API version 7. Newly added APIs will be marked with a superscript to indicate their earliest API version.
    
-   This module cannot be used in the file declaration of the [UIAbility](../../../../ability-kit/arkts-apis/stage-model/ohos-app-ability-uiability-ability-with-ui/document.md). In other words, the APIs of this module can be used only after a component instance is created; they cannot be called in the lifecycle of the UIAbility.
    
-   The functionality of this module depends on UI context. This means that the APIs of this module cannot be used where [the UI context is ambiguous](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/arkts-global-interface#ambiguous-ui-context). For details, see [UIContext](../ohos-arkui-uicontext-uicontext/class-uicontext/document.md).
    

#### Modules to Import

import { mediaquery } from '@kit.ArkUI';

#### mediaquery.matchMediaSync(deprecated)

matchMediaSync(condition: string): MediaQueryListener

Sets the media query condition. This API returns the corresponding media query listener.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/93/v3/azZ-suOwTLa3GJGRCGG1pg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062229Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=1B63595DBBFAA1A509F42D4EDF8415875F7191F694093A694A29B862B4325C26)

-   This API is supported since API version 7 and deprecated since API version 18. You are advised to use [matchMediaSync](../ohos-arkui-uicontext-uicontext/class-mediaquery/document.md#matchmediasync) instead. Before calling this API, you need to obtain the [MediaQuery](../ohos-arkui-uicontext-uicontext/class-mediaquery/document.md) object using the [getMediaQuery](../ohos-arkui-uicontext-uicontext/class-uicontext/document.md#getmediaquery) method in [UIContext](../ohos-arkui-uicontext-uicontext/class-uicontext/document.md).
    
-   Since API version 10, you can use the [getMediaQuery](../ohos-arkui-uicontext-uicontext/class-uicontext/document.md#getmediaquery) API in [UIContext](../ohos-arkui-uicontext-uicontext/class-uicontext/document.md) to obtain the [MediaQuery](../ohos-arkui-uicontext-uicontext/class-mediaquery/document.md) object associated with the current UI context.
    

**Widget capability**: This API can be used in ArkTS widgets since API version 12.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| condition | string | Yes | Media query condition. For details, see [Syntax](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/arkts-layout-development-media-query#syntax). |

**Return value**

| Type | Description |
| :-- | :-- |
| [MediaQueryListener](#mediaquerylistener) | Media query listener, which is used to register or deregister the listening callback. |

**Example**

import { mediaquery } from '@kit.ArkUI';

let listener: mediaquery.MediaQueryListener = mediaquery.matchMediaSync('(orientation: landscape)'); // Listen for landscape events.

#### MediaQueryListener

Implements the media query listener, including the first query result when the listener is applied for. The specified media query condition, for example, **'(width <= 600vp)'**, is compared system information. If related information is not initialized during the first query, **matches** returns **false**.

Inherits from [MediaQueryResult](#mediaqueryresult).

**Widget capability**: This API can be used in ArkTS widgets since API version 12.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

#### \[h2\]on('change')

on(type: 'change', callback: Callback<MediaQueryResult>): void

Registers a media query listener. The callback is triggered when the media attributes change.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/af/v3/Wb3k1vQJQA6Lu2ko3121-w/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062229Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=AB0233455614B1E6F4CCA6FDF27ACA581D363E2C0E4529C3D1B766D3D267A0C2)

The **on** or **off** function cannot be called in the registered callback.

**Widget capability**: This API can be used in ArkTS widgets since API version 12.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Listener type. The value is fixed at **'change'**. |
| callback | Callback<[MediaQueryResult](#mediaqueryresult)\> | Yes | Callback registered with media query. |

**Example**

For details, see [off('change')](#offchange).

#### \[h2\]off('change')

off(type: 'change', callback?: Callback<MediaQueryResult>): void

Deregisters a media query listener, so that no callback is triggered when the media attributes change.

**Widget capability**: This API can be used in ArkTS widgets since API version 12.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Listener type. The value is fixed at **'change'**. |
| callback | Callback<[MediaQueryResult](#mediaqueryresult)\> | No | Callback to unregister. If this parameter is not specified, all callbacks under this handle are unregistered. |

**Example**

import { mediaquery } from '@kit.ArkUI';

let listener: mediaquery.MediaQueryListener = mediaquery.matchMediaSync('(orientation: landscape)'); // Listen for landscape events.
function onPortrait(mediaQueryResult:mediaquery.MediaQueryResult) {
  if (mediaQueryResult.matches) {
    // do something here
  } else {
    // do something here
  }
}
listener.on('change', onPortrait) // Register the media query listener.
listener.off('change', onPortrait) // Unregister the callback.

#### MediaQueryResult

Provides the media query result.

**Widget capability**: This API can be used in ArkTS widgets since API version 12.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

## Attributes

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| matches | boolean | Yes | No | Whether the media query condition is met. The value **true** means that the query conditions are met, and **false** means the opposite. |
| media | string | Yes | No | Media query condition. |

## Example

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ae/v3/waWHg2GVTYilqf780Fknuw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062229Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=CB1929C91708C6C565292D865AF585E7345D87E747DD0E01D3255518EE7376D8)

You are advised to use the [getMediaQuery](../ohos-arkui-uicontext-uicontext/class-uicontext/document.md#getmediaquery) API in [UIContext](../ohos-arkui-uicontext-uicontext/class-uicontext/document.md) to obtain the [MediaQuery](../ohos-arkui-uicontext-uicontext/class-mediaquery/document.md) object associated with the current UI context.

import { mediaquery } from '@kit.ArkUI';

@Entry
@Component
struct MediaQueryExample {
  @State color: string = '#DB7093'
  @State text: string = 'Portrait'
  listener: mediaquery.MediaQueryListener = this.getUIContext().getMediaQuery().matchMediaSync('(orientation: landscape)'); // Listen for landscape events. The mediaquery.matchMediaSync API is deprecated. You are advised to use this.getUIContext().getMediaQuery().matchMediaSync() instead.

  onPortrait(mediaQueryResult:mediaquery.MediaQueryResult) {
    if (mediaQueryResult.matches) {
      this.color = '#FFD700'
      this.text = 'Landscape'
    } else {
      this.color = '#DB7093'
      this.text = 'Portrait'
    }
  }

  aboutToAppear() {
    let portraitFunc = (mediaQueryResult: mediaquery.MediaQueryResult): void => this.onPortrait(mediaQueryResult)
    // Register the callback.
    this.listener.on('change', portraitFunc);
  }

  aboutToDisappear() {
    // Unregister the callback.
    this.listener.off('change');
  }

  build() {
    Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
      Text(this.text).fontSize(24).fontColor(this.color)
    }
    .width('100%').height('100%')
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a9/v3/2yMS0vsKSESBxOmBkWFuqg/en-us_image_0000002568765061.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062229Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=D6A6CD72D2656D3C4E0A8F3A2AAAF3F6787164D588B5019EB79A927FEE22FF49)
