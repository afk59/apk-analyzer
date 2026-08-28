# FolderStack

**FolderStack** extends the [Stack](../../rows-columns-and-stacking/stack/document.md) container, adding the [Semi-Folded State of Foldable Screens](https://developer.huawei.com/consumer/en/doc/best-practices/bpta-folded-hover) capability. Child components specified in the **upperItems** array of [FolderStackOptions](#folderstackoptions18) automatically avoid the screen crease area and reposition to the upper display.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f8/v3/PVMvPEkQRzq75OUu7RpnTA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062250Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=C20662BDBB2CF67B61D7D4CF6BF3155C732D8FE2B832B0E5A7DC3141C127052B)

This component is supported since API version 11. Updates will be marked with a superscript to indicate their earliest API version.

The hover capability is designed for and only works on .

When the component's parent is an [if/else conditional render](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/arkts-rendering-control-ifelse) node, the foldable hover feature is disabled.

#### Child Components

Multiple child components are supported.

#### APIs

FolderStack(options?: FolderStackOptions)

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Device behavior differences**: On wearables, calling this API results in a runtime exception indicating that the API is undefined. On other devices, the API works correctly.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| options | [FolderStackOptions](#folderstackoptions18) | No | Configuration of the **FolderStack** component. |

#### FolderStackOptions18+

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/db/v3/Mf-ZsvFtRgCJMJ0CuJV_WQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062250Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=D296CE1E9FBC0FCD35EAE1ED70344DE091A092E5063D071FDD0A161853F07228)

To standardize anonymous object definitions, the element definitions here have been revised in API version 18. While historical version information is preserved for anonymous objects, there may be cases where the outer element's @since version number is higher than inner elements'. This does not affect interface usability.

**Atomic service API**: This API can be used in atomic services since API version 18.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Device behavior differences**: On wearables, calling this API results in a runtime exception indicating that the API is undefined. On other devices, the API works correctly.

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| upperItems11+ | Array<string> | No | Yes | 
Array of IDs of child components that will be moved to the upper half screen in the hover state.

On hover, child components with IDs in this array automatically shift away from the crease area and move to the upper half screen, while other components are stacked in the lower half screen.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |

#### Attributes

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fe/v3/X2m28X23T3eX7HJ769P4jQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062250Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=EEF973436B354C302CE2F86264054F390B37130DB386A7E8C441940E32EA3288)

Setting the **offset** and **margin** attributes may cause the upper and lower half screens to block the crease area. Therefore, avoid setting these attributes with this component.

In addition to the [universal attributes](../../universal-attributes/document.md), the following attributes are supported.

#### \[h2\]alignContent

alignContent(value: Alignment)

Sets the alignment of child components in the container. When both this attribute and the [align](../../universal-attributes/layout-and-borders/location/document.md#align) attribute are set, whichever is set last takes effect.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/24/v3/a6_JKrwMRqOj7gjJ8mVnGw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062250Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=E40DD90D3DBA8A6DE3369028578234735CA090B3F6469E8C07027A56EC41A1C3)

This API can be called within [attributeModifier](../../universal-attributes/modifiers-and-custom-property/attribute-modifier/document.md#attributemodifier) since API version 12.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Device behavior differences**: On wearables, calling this API results in a runtime exception indicating that the API is undefined. On other devices, the API works correctly.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | [Alignment](../../common-definitions/enums/document.md#alignment) | Yes | 
Alignment of child components in the container.

Default value: **Alignment.Center**

Invalid values are treated as the default value.

 |

#### \[h2\]enableAnimation

enableAnimation(value: boolean)

Sets whether to enable the default animation.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/22/v3/jLOVPm-0SEGkUhnEEi7Ozw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062250Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=5BB94D49EB2CDFDEEB673F6FB0D1AF864023371C8B38D3678636FC5052768AD5)

This API can be called within [attributeModifier](../../universal-attributes/modifiers-and-custom-property/attribute-modifier/document.md#attributemodifier) since API version 12.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Device behavior differences**: On wearables, calling this API results in a runtime exception indicating that the API is undefined. On other devices, the API works correctly.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | boolean | Yes | 
Whether to enable the default animation.

Default value: **true**. **true**: Enable the default animation. **false**: Disable the default animation.

Invalid values are treated as the default value.

 |

#### \[h2\]autoHalfFold

autoHalfFold(value: boolean)

Sets whether to enable auto rotation. This attribute is effective only when auto rotation is disabled in device system settings.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3c/v3/Av1x52I_SH-cMZfrZTO9bg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062250Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=FC1BEBEBA959BEED1456B0B428A9216F66299200AEB6F9C4B76DC305443A4F92)

This API can be called within [attributeModifier](../../universal-attributes/modifiers-and-custom-property/attribute-modifier/document.md#attributemodifier) since API version 12.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Device behavior differences**: On wearables, calling this API results in a runtime exception indicating that the API is undefined. On other devices, the API works correctly.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | boolean | Yes | 
Whether to enable auto rotation.

Default value: **true**. **true**: Enable auto rotation when the **FolderStack** component is in [half-folded state](../../common-definitions/enums/document.md#foldstatus11). **false**: Disable auto rotation. This setting applies uniformly across all device types.

Invalid values are treated as the default value.

 |

#### Events

In addition to the [universal events](../../universal-events/document.md), the following events are supported.

#### \[h2\]onFolderStateChange

onFolderStateChange(callback: OnFoldStatusChangeCallback)

Triggered when the fold state of the device changes. This API takes effect only in landscape mode.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/da/v3/2gyNYx9ESFaOzGVMouyxvQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062250Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=27142DBC8E173004CFA180ED5DC0360031EDF9C8706C60723AF0CC55E4D99FDF)

This API can be called within [attributeModifier](../../universal-attributes/modifiers-and-custom-property/attribute-modifier/document.md#attributemodifier) since API version 20.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Device behavior differences**: On wearables, calling this API results in a runtime exception indicating that the API is undefined. On other devices, the API works correctly.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | [OnFoldStatusChangeCallback](#onfoldstatuschangecallback18) | Yes | Callback invoked when the fold state of the device changes. |

#### \[h2\]onHoverStatusChange12+

onHoverStatusChange(handler: OnHoverStatusChangeCallback)

Triggered when the hover state of the device changes.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a6/v3/d2xPpVeETXu6K9xeizsshQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062250Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=41D7BB19BEAEAB8B29B6FF6001EEE3AD7AFDE537B60B0532BD02558329832D04)

This API can be called within [attributeModifier](../../universal-attributes/modifiers-and-custom-property/attribute-modifier/document.md#attributemodifier) since API version 20.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Device behavior differences**: On wearables, calling this API results in a runtime exception indicating that the API is undefined. On other devices, the API works correctly.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| handler | [OnHoverStatusChangeCallback](#onhoverstatuschangecallback18) | Yes | Callback invoked when the hover state of the device changes. |

#### OnHoverStatusChangeCallback18+

type OnHoverStatusChangeCallback = (param: HoverEventParam) => void

Defines the current allback invoked when the hover state of the device changes.

**Atomic service API**: This API can be used in atomic services since API version 18.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Device behavior differences**: On wearables, calling this API results in a runtime exception indicating that the API is undefined. On other devices, the API works correctly.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| param | [HoverEventParam](#hovereventparam12) | Yes | Parameters related to the hover state of the device, including the fold state, hover state, application orientation, and window mode enumeration of the device. |

#### OnFoldStatusChangeCallback18+

type OnFoldStatusChangeCallback = (event: OnFoldStatusChangeInfo) => void

Current fold state of the device.

**Atomic service API**: This API can be used in atomic services since API version 18.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Device behavior differences**: On wearables, calling this API results in a runtime exception indicating that the API is undefined. On other devices, the API works correctly.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| event | [OnFoldStatusChangeInfo](#onfoldstatuschangeinfo18) | Yes | Current fold state of the device. |

#### OnFoldStatusChangeInfo18+

Called when the folding state changes. This API takes effect only in landscape mode.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f6/v3/vP7q1x1USjmGRc2uco77Qw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062250Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=675BF51E99E1E47B27B2E9968220AB0E8E6173682D55531A538AA2AFA977A239)

To standardize anonymous object definitions, the element definitions here have been revised in API version 18. While historical version information is preserved for anonymous objects, there may be cases where the outer element's @since version number is higher than inner elements'. This does not affect interface usability.

**Atomic service API**: This API can be used in atomic services since API version 18.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Device behavior differences**: On wearables, calling this API results in a runtime exception indicating that the API is undefined. On other devices, the API works correctly.

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| foldStatus11+ | [FoldStatus](../../common-definitions/enums/document.md#foldstatus11) | No | No | 
Current fold state of the device.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |

#### HoverEventParam12+

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Device behavior differences**: On wearables, calling this API results in a runtime exception indicating that the API is undefined. On other devices, the API works correctly.

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| foldStatus | [FoldStatus](../../common-definitions/enums/document.md#foldstatus11) | No | No | Current fold state of the device. |
| isHoverMode | boolean | No | No | Whether hover mode is enabled. **true**: Hover mode is enabled. **false**: Hover mode is disabled. |
| appRotation | [AppRotation](../../common-definitions/enums/document.md#approtation12) | No | No | Current orientation. |
| windowStatusType | [WindowStatusType](#windowstatustype12) | No | No | Window mode. |

#### WindowStatusType12+

type WindowStatusType = WindowStatusType

Enumerates the window modes.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Device behavior differences**: On wearables, calling this API results in a runtime exception indicating that the API is undefined. On other devices, the API works correctly.

| Type | Description |
| :-- | :-- |
| [WindowStatusType](../../../arkts-api/window-manager/ohos-window-window/enums/document.md#windowstatustype11) | Window mode. |

#### Example

## Example 1: Implementing the Foldable Device Hover Capability with FolderStack

This example implements the foldable device hover capability.

@Entry
@Component
struct Index {
  build() {
    Column() {
      // Set upperItems to IDs of the child components to be moved to the upper half screen in the hover state. Other components are stacked in the lower half screen.
      FolderStack({ upperItems: \["upperitemsId"\] }) {
        // This column is automatically moved up to the upper half screen.
        Column() {
          Text("video zone").height("100%").width("100%").textAlign(TextAlign.Center).fontSize(25)
        }.backgroundColor('rgb(0, 74, 175)').width("100%").height("100%").id("upperitemsId")

        // The following two columns are stacked in the lower half screen.
        Column() {
          Text("video title")
            .width("100%")
            .height(50)
            .textAlign(TextAlign.Center)
            .backgroundColor('rgb(213, 213, 213)')
            .fontSize(25)
        }.width("100%").height("100%").justifyContent(FlexAlign.Start)

        Column() {
          Text("video bar ")
            .width("100%")
            .height(50)
            .textAlign(TextAlign.Center)
            .backgroundColor('rgb(213, 213, 213)')
            .fontSize(25)
        }.width("100%").height("100%").justifyContent(FlexAlign.End)
      }
      .backgroundColor('rgb(39, 135, 217)')
      // Set whether to enable animation.
      .enableAnimation(true)
      // Set whether to enable auto-rotate.
      .autoHalfFold(true)
      // Called when the folding status changes.
      .onFolderStateChange((msg) => {
        if (msg.foldStatus === FoldStatus.FOLD\_STATUS\_EXPANDED) {
          console.info("The device is currently in the expanded state")
        } else if (msg.foldStatus === FoldStatus.FOLD\_STATUS\_HALF\_FOLDED) {
          console.info("The device is currently in the half folded state")
        } else {
          // .............
        }
      })
      // The hoverStatusChange callback is invoked when the hover status changes.
      .onHoverStatusChange((msg) => {
        console.info('this foldStatus:' + msg.foldStatus);
        console.info('this isHoverMode:' + msg.isHoverMode);
        console.info('this appRotation:' + msg.appRotation);
        console.info('this windowStatusType:' + msg.windowStatusType);
      })
      // If the folderStack component does not occupy the full screen, it is used as a common stack.
      .alignContent(Alignment.Bottom)
      .height("100%")
      .width("100%")
      .backgroundColor('rgb(39, 135, 217)')

    }
    .height("100%")
    .width("100%")
    .borderWidth(1)
    .borderColor('rgb(213, 213, 213)')
    .backgroundColor('rgb(0, 74, 175)')
    .expandSafeArea(\[SafeAreaType.SYSTEM\], \[SafeAreaEdge.BOTTOM\])
  }
}

**Figure 1** Expanded state in landscape mode

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ba/v3/b-Hup9FQQWy2erYxRjOAxQ/en-us_image_0000002568685689.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062250Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=E88C7432100FEA683A2FF57CB0C724B7008697E5A742849F8595978945BE1D29)

**Figure 2** Half-folded state in landscape mode

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4c/v3/2SsBu2bORJOnBw9DsRuiOw/en-us_image_0000002568765699.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062250Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=E783B19D5B1BFB3ECCCFBAC4A94F1C5E63BD3B0A0CCAC1BA75F8924788EEDFD6)

## Example 2: Dynamically Setting Attributes and Methods of the FolderStack Component Using attributeModifier

This example demonstrates how to dynamically set the **onFolderStateChange** and **onHoverStatusChange** methods of the **FolderStack** component using **attributeModifier**.

// xxx.ets
class MyFolderStackModifier implements AttributeModifier<FolderStackAttribute> {
  applyNormalAttribute(instance: FolderStackAttribute): void {
    // Called when the folding status changes.
    instance.onFolderStateChange((msg) => {
      if (msg.foldStatus === FoldStatus.FOLD\_STATUS\_EXPANDED) {
        console.info("The device is currently in the expanded state")
      } else if (msg.foldStatus === FoldStatus.FOLD\_STATUS\_HALF\_FOLDED) {
        console.info("The device is currently in the half folded state")
      } else if (msg.foldStatus === FoldStatus.FOLD\_STATUS\_FOLDED) {
        console.info("The device is currently in the folded state")
      } else {
        // .............
      }
    })
    // The hoverStatusChange callback is invoked when the hover status changes.
    instance.onHoverStatusChange((msg) => {
      console.info('this foldStatus:' + msg.foldStatus);
      console.info('this isHoverMode:' + msg.isHoverMode);
      console.info('this appRotation:' + msg.appRotation);
      console.info('this windowStatusType:' + msg.windowStatusType);
    })
  }
}

@Entry
@Component
struct attributeDemo {
  @State modifier: MyFolderStackModifier = new MyFolderStackModifier()

  build() {
    Column() {
      // Set upperItems to IDs of the child components to be moved to the upper half screen in the hover state. Other components are stacked in the lower half screen.
      FolderStack({ upperItems: \["upperitemsId"\] }) {
        // This column is automatically moved up to the upper half screen.
        Column() {
          Text("video zone").height("100%").width("100%").textAlign(TextAlign.Center).fontSize(25)
        }.backgroundColor('rgb(0, 74, 175)').width("100%").height("100%").id("upperitemsId")

        // The following two columns are stacked in the lower half screen.
        Column() {
          Text("video title")
            .width("100%")
            .height(50)
            .textAlign(TextAlign.Center)
            .backgroundColor('rgb(213, 213, 213)')
            .fontSize(25)
        }.width("100%").height("100%").justifyContent(FlexAlign.Start)

        Column() {
          Text("video bar ")
            .width("100%")
            .height(50)
            .textAlign(TextAlign.Center)
            .backgroundColor('rgb(213, 213, 213)')
            .fontSize(25)
        }.width("100%").height("100%").justifyContent(FlexAlign.End)
      }
      .backgroundColor('rgb(39, 135, 217)')
      // Set whether to enable animation.
      .enableAnimation(true)
      // Set whether to enable auto-rotate.
      .autoHalfFold(true)
      .attributeModifier(this.modifier)
      // If the folderStack component does not occupy the full screen, it is used as a common stack.
      .alignContent(Alignment.Bottom)
      .height("100%")
      .width("100%")
      .backgroundColor('rgb(39, 135, 217)')
    }
    .height("100%")
    .width("100%")
    .borderWidth(1)
    .borderColor('rgb(213, 213, 213)')
    .backgroundColor('rgb(0, 74, 175)')
    .expandSafeArea(\[SafeAreaType.SYSTEM\], \[SafeAreaEdge.BOTTOM\])
  }
}

**Figure 1** Expanded state in landscape mode

Expected log:

The device is currently in the expanded state

this foldStatus:1

this isHoverMode:0

this appRotation:3

this windowStatusType:1

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/26/v3/TNE3mt2WSUSx7BJzudNPxw/en-us_image_0000002537765974.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062250Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=3F18EFA54BF2B7889CF909AD346D9731FF25FC01CAB6F0DA3D2FB19F62A7DDA5)

**Figure 2** Half-folded state in landscape mode

Expected log:

The device is currently in the half folded state

this foldStatus:3

this isHoverMode:1

this appRotation:3

this windowStatusType:1

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1c/v3/AJ9M52E5QqmC55hg-0rVQg/en-us_image_0000002537925914.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062250Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=1450F90C5BC9689CEAC01A9903549950428B41669EF5595A2687B8185B67D214)
