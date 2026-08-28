# PasteButton

**PasteButton** is a security component that provides paste functionality. When users tap this component, the application temporarily gains pasteboard read permissions.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ab/v3/7BXKZj8vRSWGo7FoEa_o6g/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062248Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=8DCDD29E93313991D66EFC7D8E00A3512AEBC876F530206FA23E3890F2F4EFBA)

This component is supported since API version 10. Updates will be marked with a superscript to indicate their earliest API version.

#### Child Components

Not supported

#### APIs

#### \[h2\]PasteButton

PasteButton()

Creates a **PasteButton** component with an icon, text, and background by default.

You may want to learn the [restrictions on security component styles](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/security-component-overview#constraints) to avoid authorization failures caused by incompliant styles.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

#### \[h2\]PasteButton

PasteButton(options: PasteButtonOptions)

Creates a **PasteButton** component containing the specified element.

You may want to learn the [restrictions on security component styles](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/security-component-overview#constraints) to avoid authorization failures caused by incompliant styles.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| options | [PasteButtonOptions](#pastebuttonoptions) | Yes | 
Options for creating the **PasteButton** component.

Default value:

{

icon: PasteIconStyle.LINES,

text: PasteDescription.PASTE,

buttonType: ButtonType.Capsule

}

 |

#### PasteButtonOptions

Describes the icon, text, and other specific elements for the **PasteButton** component.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/74/v3/aEpC7yjZQMGrnVYGb_aT9w/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062248Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=9CECC09DF4158D3A15FDD19DAC8DC4673F84B0477860AD5F78E9C8537860A2A3)

-   At least one of **icon** or **text** must be provided.
    
-   If neither **icon** nor **text** is provided, the **options** parameter in [PasteButton](#pastebutton-1) will not take effect, and the created **PasteButton** will be in the default style.
    
    -   The default value of **PasteIconStyle** is **LINES**.
        
    -   The default style of **PasteDescription** is **PASTE**.
        
    -   The default value of **ButtonType** is **Capsule**.
        
-   The **icon**, **text**, and **buttonType** parameters do not support dynamic modification.
    

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| icon | [PasteIconStyle](#pasteiconstyle) | No | Yes | 
Icon style of the **PasteButton** component.

If this parameter is not specified, there is no icon.

 |
| text | [PasteDescription](#pastedescription) | No | Yes | 

Text on the **PasteButton** component.

If this parameter is not specified, there is no text description.

 |
| buttonType | [ButtonType](../security-component-universal-attributes/document.md#buttontype) | No | Yes | 

Background style of the **PasteButton** component.

If this parameter is not specified, the system uses a capsule-type button.

 |

#### Attributes

This component can only inherit the [universal attributes of security components](../security-component-universal-attributes/document.md).

#### PasteIconStyle

Enumerates icon styles of the **PasteButton** component.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Value | Description |
| :-- | :-- | :-- |
| LINES | 0 | Line style icon. |

#### PasteDescription

Enumerates text descriptions of the **PasteButton** component.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Value | Description |
| :-- | :-- | :-- |
| PASTE | 0 | The text on the **PasteButton** component is **Paste**. |

#### PasteButtonOnClickResult

Enumerates the authorization results after the **PasteButton** component is tapped.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Value | Description |
| :-- | :-- | :-- |
| SUCCESS | 0 | Authorization is successful. |
| TEMPORARY\_AUTHORIZATION\_FAILED | 1 | Authorization fails. |

#### PasteButtonCallback18+

type PasteButtonCallback = (event: ClickEvent, result: PasteButtonOnClickResult, error?: BusinessError<void>) => void

Triggered when the **PasteButton** component is clicked.

**Atomic service API**: This API can be used in atomic services since API version 18.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| event | [ClickEvent](../../universal-events/interaction-response-events/click-event/document.md#clickevent) | Yes | See **ClickEvent**. |
| result | [PasteButtonOnClickResult](#pastebuttononclickresult) | Yes | Authorization result. After the authorization, the pasteboard content can be read. |
| error | [BusinessError<void>](../../../../../system/basic-functions/basic-services-kit/arkts-apis/others/ohos-base-public-callback-information/document.md#businesserror) | No | 
Error code and message when the component is clicked.

Error code 0 indicates successful authorization.

Error code 1 indicates an internal system error.

Error code 2 indicates attribute setting errors, including but not limited to:

1\. The font or icon size is too small.

2\. The font or icon color is too similar to the background color.

3\. The font or icon color is too transparent.

4\. The padding is negative.

5\. The component is obscured by other components or windows.

6\. The text exceeds the background range.

7\. The component exceeds the window or screen bounds.

8\. The component size is too large.

9\. The component text is truncated and not fully displayed.

10\. Related attribute settings affect the display of security components.

 |

#### Events

Only the following events are supported.

#### \[h2\]onClick

onClick(event: PasteButtonCallback)

Called when a click event occurs.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| event | [PasteButtonCallback](#pastebuttoncallback18) | Yes | 
See **PasteButtonCallback**.

In API versions 10 to 17, the parameter type is (event: [ClickEvent](../../universal-events/interaction-response-events/click-event/document.md#clickevent), result: [PasteButtonOnClickResult](#pastebuttononclickresult)) => void.

Since API version 18, the parameter type changes into PasteButtonCallback.

 |

#### Example

// xxx.ets
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct Index {
  handlePasteButtonClick: PasteButtonCallback =
    (event: ClickEvent, result: PasteButtonOnClickResult, error?: BusinessError<void>) => {
      if (result === PasteButtonOnClickResult.SUCCESS) {
        console.info("success");
      } else {
        console.error("errCode: " + error?.code);
        console.error("errMessage: " + error?.message);
      }
    };

  build() {
    Row() {
      Column({ space: 10 }) {
        // Create a default SaveButton component with an icon, text, and background.
        PasteButton().onClick(this.handlePasteButtonClick)
        // Whether an element is contained depends on whether the parameter corresponding to the element is specified. If buttonType is not passed in, the button uses the ButtonType.Capsule settings.
        PasteButton({ icon: PasteIconStyle.LINES })
        // Create a button with only an icon and background. If the alpha value of the most significant eight bits of the background color is less than 0x1a, the system forcibly adjusts the alpha value to 0xff.
        PasteButton({ icon: PasteIconStyle.LINES, buttonType: ButtonType.Capsule })
          .backgroundColor(0x10007dff)
        // Create a button with an icon, text, and background. If the alpha value of the most significant eight bits of the background color is less than 0x1a, the system forcibly adjusts the alpha value to 0xff.
        PasteButton({ icon: PasteIconStyle.LINES, text: PasteDescription.PASTE, buttonType: ButtonType.Capsule })
        // Create a button with an icon, text, and background. If the set width is less than the minimum allowed, the button's text will wrap to guarantee full text display.
        PasteButton({ icon: PasteIconStyle.LINES, text: PasteDescription.PASTE, buttonType: ButtonType.Capsule })
          .fontSize(16)
          .width(30)
        // Create a button with an icon, text, and background. If the set width is less than the minimum allowed, the button's text will wrap to guarantee full text display.
        PasteButton({ icon: PasteIconStyle.LINES, text: PasteDescription.PASTE, buttonType: ButtonType.Capsule })
          .fontSize(16)
          .size({ width: 30, height: 30 })
        // Create a button with an icon, text, and background. If the set width is less than the minimum allowed, the button's text will wrap to guarantee full text display.
        PasteButton({ icon: PasteIconStyle.LINES, text: PasteDescription.PASTE, buttonType: ButtonType.Capsule })
          .fontSize(16)
          .constraintSize({
            minWidth: 0,
            maxWidth: 30,
            minHeight: 0,
            maxHeight: 30
          })
      }.width('100%')
    }.height('100%')
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9e/v3/n6otlDImTf6Vo3BC9OJ4CA/en-us_image_0000002568685657.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062248Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=55CD117773BE619C716901564CAFAB7129DC32B7099A96FE76DE3F78C1E7CAF0)
