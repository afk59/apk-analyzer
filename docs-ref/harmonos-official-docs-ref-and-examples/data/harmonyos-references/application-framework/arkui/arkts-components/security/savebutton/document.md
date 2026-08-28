# SaveButton

**SaveButton** is a security component that provides a save button. After it is integrated into your application and is used for the first time, a dialog box is displayed to ask for user authorization. If the user taps **Allow**, the application automatically obtains the permission to access the media library within a short period of time. No more dialog box is displayed for authorization. For API version 19 and earlier, the authorization duration is 10 seconds. For API version 20 and later, the authorization duration is 1 minute.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5f/v3/9dZjtzp9RCuzNGWFzP2rfg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062248Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=17D4CBBBA38100E2ED5165C24680AF53D988179D0EB086D0047F8100F03894FC)

This component is supported since API version 10. Updates will be marked with a superscript to indicate their earliest API version.

#### Child Components

Not supported

#### APIs

#### \[h2\]SaveButton

SaveButton()

Creates a **SaveButton** component with an icon, text, and background.

You may want to learn the [restrictions on security component styles](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/security-component-overview#constraints) to avoid authorization failures caused by incompliant styles.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

#### \[h2\]SaveButton

SaveButton(options: SaveButtonOptions)

Creates a **SaveButton** component that contains the specified elements.

You may want to learn the [restrictions on security component styles](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/security-component-overview#constraints) to avoid authorization failures caused by incompliant styles.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| options | [SaveButtonOptions](#savebuttonoptions) | Yes | Options for creating the **SaveButton** component. |

#### SaveButtonOptions

Describes the icon, text, and other specific elements for the **SaveButton** component.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/26/v3/sRIS2Rk_SeCAwjl6fF8QDg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062248Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=BBB6B75A810587DA2C84E082F4B0A9E34DDD2170ADD0D2760AA40243D079C6DB)

-   At least one of **icon** or **text** must be provided.
    
-   If neither **icon** nor **text** is provided, the **options** parameter in [SaveButton](#savebutton-1) will not take effect, and the created **SaveButton** component will use the default style:
    
    The default value of **SaveIconStyle** is **FULL\_FILLED**.
    
    The default style of **SaveDescription** is **DOWNLOAD**.
    
    The default value of **ButtonType** is **Capsule**.
    
-   The **icon**, **text**, and **buttonType** parameters do not support dynamic modification.
    

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| icon | [SaveIconStyle](#saveiconstyle) | No | Yes | 
Icon style of the **SaveButton** component.

If this parameter is not specified, there is no icon.

 |
| text | [SaveDescription](#savedescription) | No | Yes | 

Text on the **SaveButton** component.

If this parameter is not specified, there is no text description.

 |
| buttonType | [ButtonType](../security-component-universal-attributes/document.md#buttontype) | No | Yes | 

Background type of the **SaveButton** component.

If this parameter is not specified, the system uses a capsule-type button as the **SaveButton** component.

 |

#### SaveIconStyle

Enumerates icon styles of the **SaveButton** component.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Value | Description |
| :-- | :-- | :-- |
| FULL\_FILLED | 0 | Filled style icon. |
| LINES | 1 | Line style icon. |

#### SaveDescription

Enumerates text descriptions of the **SaveButton** component.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Value | Description |
| :-- | :-- | :-- |
| DOWNLOAD | 0 | 
The text on the **SaveButton** component is **Download**.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| DOWNLOAD\_FILE | 1 | 

The text on the **SaveButton** component is **Download file**.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| SAVE | 2 | 

The text on the **SaveButton** component is **Save**.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| SAVE\_IMAGE | 3 | 

The text on the **SaveButton** component is **Save image**.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| SAVE\_FILE | 4 | 

The text on the **SaveButton** component is **Save file**.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| DOWNLOAD\_AND\_SHARE | 5 | 

The text on the **SaveButton** component is **Download & share**.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| RECEIVE | 6 | 

The text on the **SaveButton** component is **Receive**.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| CONTINUE\_TO\_RECEIVE | 7 | 

The text on the **SaveButton** component is **Continue**.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| SAVE\_TO\_GALLERY12+ | 8 | 

The text on the **SaveButton** component is **Save to Gallery**.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| EXPORT\_TO\_GALLERY12+ | 9 | 

The text on the **SaveButton** component is **Export**.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| QUICK\_SAVE\_TO\_GALLERY12+ | 10 | 

The text on the **SaveButton** component is **Save to Gallery**.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| RESAVE\_TO\_GALLERY12+ | 11 | 

The text on the **SaveButton** component is **Resave**.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| SAVE\_ALL18+ | 12 | 

The text on the **SaveButton** component is **Save all**.

**Atomic service API**: This API can be used in atomic services since API version 18.

 |

#### SaveButtonOnClickResult

Enumerates the authorization results after the **SaveButton** component is tapped.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Value | Description |
| :-- | :-- | :-- |
| SUCCESS | 0 | 
Authorization is successful.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| TEMPORARY\_AUTHORIZATION\_FAILED | 1 | 

Authorization fails.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| CANCELED\_BY\_USER21+ | 2 | 

Authorization is canceled by the user through a dialog box after the **SaveButton** component is tapped.

**Atomic service API**: This API can be used in atomic services since API version 21.

 |

#### SaveButtonCallback18+

type SaveButtonCallback = (event: ClickEvent, result: SaveButtonOnClickResult, error?: BusinessError<void>) => void

Triggered when the **SaveButton** component is clicked.

**Atomic service API**: This API can be used in atomic services since API version 18.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| event | [ClickEvent](../../universal-events/interaction-response-events/click-event/document.md#clickevent) | Yes | See **ClickEvent**. |
| result | [SaveButtonOnClickResult](#savebuttononclickresult) | Yes | Authorization result. |
| error | [BusinessError<void>](../../../../../system/basic-functions/basic-services-kit/arkts-apis/others/ohos-base-public-callback-information/document.md#businesserror) | No | 
Error code and message when the component is clicked.

Error code 0 indicates that the authorization is successful or the user cancels the authorization.

Error code 1 indicates an internal system error, including but not limited to:

1\. IPC failed.

2\. Failed to display the security component dialog box.

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

#### SaveButtonAttribute

SaveButtonAttribute provides methods for setting attributes such as custom icon (setIcon), custom text (setText), icon size (iconSize), icon corner radius (iconBorderRadius), and pressed state effect (stateEffect).

**Atomic service API**: This API can be used in atomic services since API version 11.

#### \[h2\]setIcon20+

setIcon(icon: Resource)

Sets the icon of the **SaveButton** component.

**Required permissions**: ohos.permission.CUSTOMIZE\_SAVE\_BUTTON

**Atomic service API**: This API can be used in atomic services since API version 20.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| icon | [Resource](../../common-definitions/basic-types/document.md#resource) | Yes | 
Custom icon resource information. Only data sources of the Resource type are supported.

Images in the following formats are supported: PNG, JPG, JPEG, BMP, SVG, WebP, GIF, and HEIF. For details about the supported image formats, see [Image](../../images-and-videos/image/document.md). If the resource is not an image resource or the format is not supported, the icon is displayed as blank.

If the application does not have the ohos.permission.CUSTOMIZE\_SAVE\_BUTTON permission, the custom icon setting does not take effect, and the **SaveButton** component retains the default style. For details, see [SaveButtonOptions](#savebuttonoptions).

 |

#### \[h2\]setText20+

setText(text: string | Resource)

Sets the text of the **SaveButton** component.

**Required permissions**: ohos.permission.CUSTOMIZE\_SAVE\_BUTTON

**Atomic service API**: This API can be used in atomic services since API version 20.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| text | string | [Resource](../../common-definitions/basic-types/document.md#resource) | Yes | 
Custom text.

If the application does not have the ohos.permission.CUSTOMIZE\_SAVE\_BUTTON permission, the custom text setting does not take effect, and the **SaveButton** component retains the default style. For details, see [SaveButtonOptions](#savebuttonoptions).

 |

#### \[h2\]iconSize20+

iconSize(size: Dimension | SizeOptions)

Sets the icon size of the **SaveButton** component.

**Atomic service API**: This API can be used in atomic services since API version 20.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| size | [Dimension](../../common-definitions/basic-types/document.md#dimension10) | [SizeOptions](../../common-definitions/basic-types/document.md#sizeoptions) | Yes | 
Icon size. The default width and height are both 16 vp.

Percentage strings are not supported. If a percentage string is specified for a Dimension type parameter, the icon will be displayed with the default size. If either the **width** or **height** property of a SizeOptions type parameter is set to a percentage string, the icon will be displayed with a size of 0.

For the system icons provided by the **SaveButton** component:

\- Dimension type: Width and height are both set to the specified value.

\- SizeOptions type: If width and height are different, the smaller value is used for both. If only one value is specified, it applies to both dimensions.

For custom icons:

\- Dimension type: Width and height are both set to the specified value.

\- SizeOptions type: It is recommended that you set both width and height explicitly; if only one value is set, it applies to both dimensions.

\- If the specified size's aspect ratio does not match the custom icon's original ratio, the icon displays in [ImageFit.Cover](../../common-definitions/enums/document.md#imagefit) mode.

 |

#### \[h2\]iconBorderRadius20+

iconBorderRadius(radius: Dimension | BorderRadiuses)

Sets the corner radius of the **SaveButton** component.

**Required permissions**: ohos.permission.CUSTOMIZE\_SAVE\_BUTTON

**Atomic service API**: This API can be used in atomic services since API version 20.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| radius | [Dimension](../../common-definitions/basic-types/document.md#dimension10) | [BorderRadiuses](../../common-definitions/basic-types/document.md#borderradiuses9) | Yes | 
Corner radius of the **SaveButton** component. You can set the radius for each of the four corners individually.

If the application does not have the ohos.permission.CUSTOMIZE\_SAVE\_BUTTON permission, the corner radius setting does not take effect.

 |

#### \[h2\]stateEffect20+

stateEffect(enabled: boolean)

Sets the press effect of the **SaveButton** component.

**Required permissions**: ohos.permission.CUSTOMIZE\_SAVE\_BUTTON

**Atomic service API**: This API can be used in atomic services since API version 20.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| enabled | boolean | Yes | 
Whether to enable the press effect. **true** to enable, **false** otherwise.

Default value: **true**.

If the application does not have the ohos.permission.CUSTOMIZE\_SAVE\_BUTTON permission, the setting does not take effect.

 |

#### \[h2\]userCancelEvent21+

userCancelEvent(enabled: boolean)

Sets the user authorization cancellation event for the **SaveButton** component.

**Atomic service API**: This API can be used in atomic services since API version 21.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| enabled | boolean | Yes | 
Whether to receive the user authorization cancellation event for the save button. The options are true (yes) and false (no).

Default value: **false**.

 |

#### Attributes

This component can only inherit the [universal attributes of security components](../security-component-universal-attributes/document.md).

#### Events

Only the following events are supported.

#### \[h2\]onClick

onClick(event: SaveButtonCallback)

Called when a click event occurs.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| event | [SaveButtonCallback](#savebuttoncallback18) | Yes | 
See **SaveButtonCallback**.

In API versions 10 to 17, the parameter type is (event: [ClickEvent](../../universal-events/interaction-response-events/click-event/document.md#clickevent), result: [SaveButtonOnClickResult](#savebuttononclickresult)) => void.

Since API version 18, the parameter type changes into SaveButtonCallback.

 |

#### Example 1

// xxx.ets
import { photoAccessHelper } from '@kit.MediaLibraryKit';
import { fileIo } from '@kit.CoreFileKit';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct Index {
  handleSaveButtonClick: SaveButtonCallback =
    async (event: ClickEvent, result: SaveButtonOnClickResult, error?: BusinessError) => {
      if (result === SaveButtonOnClickResult.SUCCESS) {
        try {
          const context = this.getUIContext().getHostContext();
          let helper = photoAccessHelper.getPhotoAccessHelper(context);
          let uri = await helper.createAsset(photoAccessHelper.PhotoType.IMAGE, 'png');
          // Open the file based on its URI. The write process is not time bound.
          let file = await fileIo.open(uri, fileIo.OpenMode.READ\_WRITE | fileIo.OpenMode.CREATE);
          // Write to the file.
          await fileIo.write(file.fd, "context");
          // Close the file.
          await fileIo.close(file.fd);
        } catch (error) {
          console.error(\`errCode: ${error.code}, errMessage: ${error.message}\`);
        }
      } else if (result === SaveButtonOnClickResult.CANCELED\_BY\_USER) {
        console.info("errCode: " + error?.code);
        console.info("errMessage: " + error?.message);
      } else {
        console.error("errCode: " + error?.code);
        console.error("errMessage: " + error?.message);
      }
    };

  build() {
    Row() {
      Column({ space: 10 }) {
        // Create a default button with an icon, text, and background.
        SaveButton().onClick((this.handleSaveButtonClick))
        // Whether the button has an icon, text, and background depends on whether the corresponding parameter is passed in. If buttonType is not passed in, the button uses the ButtonType.Capsule settings.
        SaveButton({ icon: SaveIconStyle.FULL\_FILLED })
        // Create a button with only an icon and background. If the alpha value of the most significant eight bits of the background color is less than 0x1a, the system forcibly adjusts the alpha value to 0xff.
        SaveButton({ icon: SaveIconStyle.FULL\_FILLED, buttonType: ButtonType.Capsule })
          .backgroundColor(0x10007dff)
        // Create a button with an icon, text, and background. If the alpha value of the most significant eight bits of the background color is less than 0x1a, the system forcibly adjusts the alpha value to 0xff.
        SaveButton({ icon: SaveIconStyle.FULL\_FILLED, text: SaveDescription.DOWNLOAD, buttonType: ButtonType.Capsule })
        // Create a button with an icon, text, and background. If the set width is less than the minimum allowed, the button's text will wrap to guarantee full text display.
        SaveButton({ icon: SaveIconStyle.FULL\_FILLED, text: SaveDescription.DOWNLOAD, buttonType: ButtonType.Capsule })
          .fontSize(16)
          .width(30)
        // Create a button with an icon, text, and background. If the set width is less than the minimum allowed, the button's text will wrap to guarantee full text display.
        SaveButton({ icon: SaveIconStyle.FULL\_FILLED, text: SaveDescription.DOWNLOAD, buttonType: ButtonType.Capsule })
          .fontSize(16)
          .size({ width: 30, height: 30 })
        // Create a button with an icon, text, and background. If the set width is less than the minimum allowed, the button's text will wrap to guarantee full text display.
        SaveButton({ icon: SaveIconStyle.FULL\_FILLED, text: SaveDescription.DOWNLOAD, buttonType: ButtonType.Capsule })
          .fontSize(16)
          .constraintSize({
            minWidth: 0,
            maxWidth: 30,
            minHeight: 0,
            maxHeight: 30
          })
        // Configure the SaveButton component to receive the user authorization cancellation event.
        SaveButton({ icon: SaveIconStyle.FULL\_FILLED, text: SaveDescription.DOWNLOAD })
          .onClick((this.handleSaveButtonClick))
          .userCancelEvent(true)
      }.width('100%')
    }.height('100%')
  }
}

#### Example 2

The application requires the ohos.permission.CUSTOMIZE\_SAVE\_BUTTON permission.

// xxx.ets
@Entry
@Component
struct SetIcon {
  build() {
    Row() {
      Column({ space: 10 }) {
        // Set icon to the resource type. The icon is displayed when permission is granted.
        SaveButton({ icon: SaveIconStyle.FULL\_FILLED, text: SaveDescription.DOWNLOAD })
          .setIcon($r('app.media.startIcon'))
        // Set text to the string type. The text is displayed when permission is granted.
        SaveButton({ icon: SaveIconStyle.FULL\_FILLED, text: SaveDescription.DOWNLOAD })
          .setText("SaveButton Set Text")
        // Set text to the resource type. The resource text is displayed when permission is granted.
        SaveButton({ icon: SaveIconStyle.FULL\_FILLED, text: SaveDescription.DOWNLOAD })
          .setText($r('app.string.app\_name'))
        // Set the icon size for the SaveButton component. The input parameter is of the Dimension type.
        SaveButton({ icon: SaveIconStyle.FULL\_FILLED, text: SaveDescription.DOWNLOAD })
          .iconSize(28)
        // Set the default icon size for the SaveButton component. The input parameter is of the SizeOptions type. It uses smaller value between width and height as the default icon size.
        SaveButton({ icon: SaveIconStyle.FULL\_FILLED, text: SaveDescription.DOWNLOAD })
          .iconSize({ width: 20, height: 40 })
        // Set the custom icon size for the SaveButton component. The input parameter is SizeOptions type. The image is displayed based on the configured width and height.
        SaveButton({ icon: SaveIconStyle.FULL\_FILLED, text: SaveDescription.DOWNLOAD })
          .setIcon($r('app.media.startIcon'))
          .iconSize({ width: 30, height: 40 })
        // Set the custom icon size for the SaveButton component. The input parameter is of the SizeOptions type with a single value. The image is displayed based on the configured width and height.
        SaveButton({ icon: SaveIconStyle.FULL\_FILLED, text: SaveDescription.DOWNLOAD })
          .setIcon($r('app.media.startIcon'))
          .iconSize({ width: 40 })
        // Set the corner radius of the SaveButton component icon. The input parameter is of the Dimension type. All four corners use the input parameter value.
        SaveButton({ icon: SaveIconStyle.FULL\_FILLED, text: SaveDescription.DOWNLOAD })
          .backgroundColor(Color.Orange)
          .setIcon($r('app.media.background'))
          .iconSize(30)
          .iconBorderRadius(6)
        // Set the square icon corner radius greater than half side length to display as circle.
        SaveButton({ icon: SaveIconStyle.FULL\_FILLED, buttonType: ButtonType.Circle })
          .backgroundColor(Color.Orange)
          .setIcon($r('app.media.foreground'))
          .iconSize(30)
          .iconBorderRadius(30)
          .padding(0)
        // Set iconBorderRadius to circle, background color to transparent, and add border.
        SaveButton({ icon: SaveIconStyle.FULL\_FILLED, buttonType:ButtonType.Circle })
          .setIcon($r('app.media.background'))
          .backgroundColor(Color.Transparent)
          .iconSize(40)
          .iconBorderRadius(30)
          .borderWidth(1)
          .borderColor(Color.Black)
          .borderStyle(BorderStyle.Solid)
          .padding(10)
        // Set the border radius for the SaveButton component corners. The input parameter is of the BorderRadiuses type. Each corner uses the corresponding input parameter value. Unset corners remain square.
        SaveButton({ icon: SaveIconStyle.FULL\_FILLED, text: SaveDescription.DOWNLOAD })
          .backgroundColor(Color.Orange)
          .setIcon($r('app.media.background'))
          .iconSize(30)
          .iconBorderRadius({ topLeft: 10, topRight: 16, bottomRight: 20 })
        // Disable the pressed state effect for the SaveButton component.
        SaveButton({ icon: SaveIconStyle.FULL\_FILLED, text: SaveDescription.DOWNLOAD })
          .stateEffect(false)
      }.width('100%')
    }.height('100%')
  }
}
