# Image

The **Image** component is usually used to display images in applications. It supports data sources of the following types: [PixelMap](../../../../../media/image-kit/arkts-apis/ohos-multimedia-image-image-processing/interface-pixelmap/document.md), [ResourceStr](../../common-definitions/basic-types/document.md#resourcestr), and [DrawableDescriptor](#drawabledescriptor10). Supported image formats include PNG, JPG, JPEG, BMP, SVG, WEBP, GIF, and HEIF. Note that the APNG and SVGA formats are not supported.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d5/v3/4sOtq2e2Rqa-Sogw3fHyiQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062243Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=EEE5FECAE26AB1AC4555DC04EE22640E613CA510166ED8A3D5A783761DBF614B)

This component is supported since API version 7. Updates will be marked with a superscript to indicate their earliest API version.

When keyboard shortcuts are used to copy an **Image** component, the **Image** component must be in a focused state. For instructions on how to set focus, see [Setting Whether a Component Is Focusable](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/arkts-common-events-focus-event#setting-whether-a-component-is-focusable). By default, the **Image** component is not focusable. To enable it to gain focus, set both the [focusable](../../universal-attributes/interaction-properties/focus-control/document.md#focusable) and [focusOnTouch](../../universal-attributes/interaction-properties/focus-control/document.md#focusontouch9) attributes to **true**.

The **Image** component supports SVG image sources. For details about SVG tags, see [SVG Tags](../svg-tags/document.md).

For animated images, animation playback is disabled by default and depends on the visibility of the **Image** component. When the component is visible, the animation is started through the callback. When the component is invisible, the animation is stopped. The visibility status of the **Image** component can be identified through the [onVisibleAreaChange](../../universal-events/component-change-events/visible-area-change-event/document.md#onvisibleareachange) event. If the value of **ratios** is greater than 0, the component is visible.

For details about how to resolve white block issues during image loading, see [Solution to White Image Blocks](https://developer.huawei.com/consumer/en/doc/best-practices/bpta-image-white-lump-solution). For details about how to address slow image loading, see [Optimizing Preset Image Loading](https://developer.huawei.com/consumer/en/doc/best-practices/bpta-texture-compression-improve-performance).

#### Required Permissions

The **ohos.permission.INTERNET** permission is required for using online images. For details about how to apply for a permission, see [Declaring Permissions](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/declare-permissions).

#### Child Components

Not supported

#### APIs

#### \[h2\]Image

Image(src: PixelMap | ResourceStr | DrawableDescriptor)

Obtains an image from the specified source for subsequent rendering and display.

If the **Image** component fails to obtain the image or the obtained image size is 0, the **Image** component is automatically resized to 0 and does not follow the layout constraints of its parent component.

By default, the **Image** component crops images to keep their center. For example, if the component has the same width and height, it crops any image whose width and height are different, so as to keep its center.

If the **Image** component does not have its width and height set, its size adapts to that of its parent component once the image is successfully loaded.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/86/v3/Ikq4m_2rQJ2CQ7UD7vjq-w/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062243Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=8250AA2270575A4F28069EE400943A95C60756E6C431D19543A23A2C8BFDF2D8)

-   Passing a URL directly to an **Image** component may lead to potential performance issues, such as: (1) Large images cannot be downloaded in advance during loading, resulting in a long display time of white blocks; (2) Small images set to load synchronously may block the UI thread in a weak network environment, causing screen freezes; (3) In a rapidly scrolling waterfall flow, images that are about to be displayed cannot be downloaded in advance, resulting in many white blocks during scrolling. Performance issues may manifest differently in different scenarios. To minimize these issues, separate the network download part from the display of the **Image** component, and download in advance or asynchronously. For details about how to resolve white block issues during image loading, see [Solution to White Image Blocks](https://developer.huawei.com/consumer/en/doc/best-practices/bpta-image-white-lump-solution). For details about how to address slow image loading, see [Optimizing Preset Image Loading](https://developer.huawei.com/consumer/en/doc/best-practices/bpta-texture-compression-improve-performance).
    
-   When **src** is switched from a valid value (an image resource that can be parsed and loaded correctly) to an invalid value (an image path that cannot be parsed or loaded), the component retains the previously successfully loaded image content without clearing or resetting it.
    
-   If the input parameter is of the [PixelMap](../../../../../media/image-kit/arkts-apis/ohos-multimedia-image-image-processing/interface-pixelmap/document.md) type, the **Image** component can detect data changes only when the **PixelMap** object is updated to point to a new instance. If modifications are made to the content of the **PixelMap** object, such as pixel values, but the reference to the object remains the same, the **Image** component will not recognize these modifications as a data change.
    
-   If the input parameter of the **Image** component is a Base64 string, the standard format of the Base64 string is **data:image/subtype;base64,Base64EncodedData**. In this format, **subtype** indicates the type declaration, **Base64EncodedData** indicates the Base64-encoded data, and other values are fixed strings. For example, the input parameter of a PNG image is **data:image/png;base64,iVBORw0KGgo...**.
    
    1.  **image/subType** declares the data type. The **Image** component does not enforce that the declared type exactly matches the actual image format decoded from Base64. In some scenarios, the image may still display correctly even if the declared type does not match the actual format. To prevent future behavior changes or unknown issues, it is recommended that the declared type always match the actual image format.
        
    2.  The **Image** component does not support the wildcard syntax: **data:image/\*;base64,Base64EncodedData**. The **subType** must explicitly declare the specific image type.
        
    3.  The **Image** component does not support loading SVG images in Base64 string format.
        

**Widget capability**: This API can be used in ArkTS widgets since API version 9.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| src | [PixelMap](../image-analysis-types/document.md#pixelmap) | [ResourceStr](../../common-definitions/basic-types/document.md#resourcestr)| [DrawableDescriptor](#drawabledescriptor10) | Yes | 
Data source of the image. Local and online sources are supported. For details about how to reference an image, see [Loading Image Resources](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/arkts-graphics-display#loading-image-resources).

1\. **PixelMap**: a pixel map storing graphical information, commonly used for image editing scenarios.

2\. **ResourceStr**: a string or a Resource object.

The string type can be used to load local images and, more frequently, online images. When [using a local image referenced using a relative path](#example-25-displaying-an-image-using-a-relative-path), the **Image** component cannot be called across bundles or modules. If an image needs to be used globally, you are advised to use the Resource format.

Since DevEco Studio 6.0.0 Beta2, resources in non-**resource** directories are not packaged by default for new projects or modules. To enable packaging, go to **buildOption** > **resOptions** > **copyCodeResource** to set **enable** to **true** in the module's **build-profile.json5** file. For details, see [resOptions](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/ide-hvigor-build-profile#table1476161719356).

\- Base64 strings are supported.

\- When providing an HTTPS network image URL, refer to [Example 2: Downloading and Displaying Static Online Images](#example-2-downloading-and-displaying-static-online-images) for implementation guidance.

\- Strings prefixed with the **file://** path are supported (application sandbox URI: **file://<bundleName>/<sandboxPath>**). For details about how to construct the application sandbox path URI, see [constructor](../../../../core-file-kit/arkts-apis/ohos-file-fileuri-file-uri/document.md#constructor10). The sandbox path must be converted to an application sandbox URI using the [fileUri.getUriFromPath(path)](../../../../core-file-kit/arkts-apis/ohos-file-fileuri-file-uri/document.md#fileurigeturifrompath) API before being passed in for display. In addition, ensure that the application has the read permission to the files in the specified path.

The Resource format allows for access across bundles and modules. It is recommended for accessing local images. For details, see [Cross-HAP/HSP Resources](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/resource-categories-and-access#cross-haphsp-resources).

3\. **DrawableDescriptor**: an object created when the passed resource ID or name belongs to a common image. The [AnimatedDrawableDescriptor](../../../arkts-api/ui/ohos-arkui-drawabledescriptor-drawabledescriptor/document.md#animateddrawabledescriptor12) type can be passed to play animations from a **PixelMap** array.

**NOTE**

\- ArkTS widgets support GIF animations, but the animations only play once on display.

\- ArkTS widgets do not support the strings with the **http://** or **file://** prefix.

 |

#### \[h2\]Image12+

Image(src: PixelMap | ResourceStr | DrawableDescriptor | ImageContent)

Obtains an image. The [ImageContent](#imagecontent12) type allows you to specify the image content.

**Widget capability**: This API can be used in ArkTS widgets since API version 12.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| src | [PixelMap](../image-analysis-types/document.md#pixelmap) | [ResourceStr](../../common-definitions/basic-types/document.md#resourcestr)| [DrawableDescriptor](#drawabledescriptor10)| [ImageContent](#imagecontent12) | Yes | 
Data source of the image. Local and online sources are supported. For details about how to reference an image, see [Loading Image Resources](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/arkts-graphics-display#loading-image-resources).

For details about how to use **PixelMap**, **ResourceStr**, and **DrawableDescriptor**, see the **src** parameter description of [Image](#image-1).

[ImageContent](#imagecontent12): image content.

**NOTE**

\- ArkTS widgets support GIF animations, but the animations only play once on display.

\- ArkTS widgets do not support the strings with the **http://** or **file://** prefix.

 |

#### \[h2\]Image12+

Image(src: PixelMap | ResourceStr | DrawableDescriptor, imageAIOptions: ImageAIOptions)

Obtains an image. The [imageAIOptions](../image-analysis-types/document.md#imageaioptions12) parameter allows you to set AI image analysis options.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| src | [PixelMap](../image-analysis-types/document.md#pixelmap) | [ResourceStr](../../common-definitions/basic-types/document.md#resourcestr)| [DrawableDescriptor](#drawabledescriptor10) | Yes | 
Data source of the image. Local and online sources are supported. For details about how to reference an image, see [Loading Image Resources](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/arkts-graphics-display#loading-image-resources).

For details about how to use **PixelMap**, **ResourceStr**, and **DrawableDescriptor**, see the **src** parameter description of [Image](#image-1).

**NOTE**

\- ArkTS widgets support GIF animations, but the animations only play once on display.

\- ArkTS widgets do not support the strings with the **http://** or **file://** prefix.

 |
| imageAIOptions | [ImageAIOptions](../image-analysis-types/document.md#imageaioptions12) | Yes | AI image analysis options. You can configure the analysis type or bind an analyzer controller through this parameter. |

#### Attributes

For details about how to use the attributes, see [Setting Attributes](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/arkts-graphics-display#setting-attributes). In addition to the [universal attributes](../../universal-attributes/document.md), the following attributes are supported.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/16/v3/Iqb67_IcS_CtiB59lCGc6A/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062243Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=9F49329D8343C04CC4BD1A4BD9E030B49012A1E79BD27060B6B1C3C04E2BD132)

The **Image** component does not support the universal attribute [foregroundColor](../../universal-attributes/visual-effects/foreground-color/document.md#foregroundcolor). Instead, you can set the fill color using the component's [fillColor](#fillcolor) attribute.

#### \[h2\]alt

alt(value: string | Resource | PixelMap)

Sets the placeholder image displayed during image loading.

The placeholder image supports configuration of [objectFit](#objectfit) for setting the fill effect, which is consistent with the fill effect of the image.

This attribute does not take effect when the parameter type of the component is [AnimatedDrawableDescriptor](../../../arkts-api/ui/ohos-arkui-drawabledescriptor-drawabledescriptor/document.md#animateddrawabledescriptor12).

**Widget capability**: This API can be used in ArkTS widgets since API version 9.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | string | [Resource](../../common-definitions/basic-types/document.md#resource) | [PixelMap](../../../../../media/image-kit/arkts-apis/ohos-multimedia-image-image-processing/interface-pixelmap/document.md)12+ | Yes | 
Placeholder image displayed during loading. Local images (in PNG, JPG, BMP, SVG, GIF, or HEIF format) and [PixelMap](../../../../../media/image-kit/arkts-apis/ohos-multimedia-image-image-processing/interface-pixelmap/document.md) objects are supported, but online images are not.

\- Base64 strings are supported.

\- Strings prefixed with the **file://** path are supported (application sandbox URI: **file://<bundleName>/<sandboxPath>**). For details about how to construct the application sandbox path URI, see [constructor](../../../../core-file-kit/arkts-apis/ohos-file-fileuri-file-uri/document.md#constructor10). The sandbox path must be converted to an application sandbox URI using the [fileUri.getUriFromPath(path)](../../../../core-file-kit/arkts-apis/ohos-file-fileuri-file-uri/document.md#fileurigeturifrompath) API before being passed in for display. In addition, ensure that the application has the read permission to the files in the specified path.

Default value: **null**

When the value is switched from a valid one (an image resource that can be parsed and loaded correctly) to an invalid one (an image path that cannot be parsed or loaded), the component retains the previously successfully loaded image content without clearing or resetting it.

 |

#### \[h2\]alt22+

alt(src: ResourceStr | PixelMap | ImageAlt)

Sets the placeholder image displayed during image loading and when image loading fails.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ae/v3/Shn0jIOeQqWJZb0z_xp9VQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062243Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=52C99C2E3FF168340CFF3D44954958607863C27042C1204556B2C96539E2724B)

When a placeholder image is configured via [ImageAlt](#imagealt22), **Image** takes effect based on the placeholder image sources configured for the loading and load-failure states. If no placeholder image is configured, it is not displayed by default.

The placeholder image supports configuration of [objectFit](#objectfit) for setting the fill effect, which is consistent with the fill effect of the image.

This attribute does not take effect when the parameter type of the component is [AnimatedDrawableDescriptor](../../../arkts-api/ui/ohos-arkui-drawabledescriptor-drawabledescriptor/document.md#animateddrawabledescriptor12).

**Widget capability**: This API can be used in ArkTS widgets since API version 22.

**Atomic service API**: This API can be used in atomic services since API version 22.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| src | [ResourceStr](../../common-definitions/basic-types/document.md#resourcestr) | [PixelMap](../../../../../media/image-kit/arkts-apis/ohos-multimedia-image-image-processing/interface-pixelmap/document.md)| [ImageAlt](#imagealt22) | Yes | 
Placeholder image displayed during loading or in case of loading failure. Local images (in PNG, JPG, BMP, SVG, GIF, or HEIF format) and [PixelMap](../../../../../media/image-kit/arkts-apis/ohos-multimedia-image-image-processing/interface-pixelmap/document.md) objects are supported, but online images are not.

\- Base64 strings are supported.

\- Strings prefixed with the **file://** path are supported (application sandbox URI: **file://<bundleName>/<sandboxPath>**). For details about how to construct the application sandbox path URI, see [constructor](../../../../core-file-kit/arkts-apis/ohos-file-fileuri-file-uri/document.md#constructor10). The sandbox path must be converted to an application sandbox URI using the [fileUri.getUriFromPath(path)](../../../../core-file-kit/arkts-apis/ohos-file-fileuri-file-uri/document.md#fileurigeturifrompath) API before being passed in for display. In addition, ensure that the application has the read permission to the files in the specified path.

 |

#### \[h2\]objectFit

objectFit(value: ImageFit)

Sets how the image is resized to fit its container. If the attribute is not set, the default value is **ImageFit.Cover**, which scales the image up or down while maintaining its aspect ratio.

**Widget capability**: This API can be used in ArkTS widgets since API version 9.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | [ImageFit](../../common-definitions/enums/document.md#imagefit) | Yes | How the image is resized to fit its container. |

#### \[h2\]imageMatrix15+

imageMatrix(matrix: ImageMatrix)

Sets the transformation matrix of the image. This API allows you to use the functions provided by the [ImageMatrix](#imagematrix15) object, such as translate, rotate, and scale, to achieve the optimal display of grid thumbnails. This attribute is not applicable to SVG images.

This attribute does not take effect when [resizable](#resizable11) and [objectRepeat](#objectrepeat) are set. This attribute only processes the image source and does not trigger any callback events of the **Image** component.

This attribute is strongly associated with [objectFit](#objectfit) and takes effect only when [objectFit](#objectfit) is set to **ImageFit.MATRIX**.

**Atomic service API**: This API can be used in atomic services since API version 15.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| matrix | [ImageMatrix](#imagematrix15) | Yes | Transformation matrix of the image. |

#### \[h2\]objectRepeat

objectRepeat(value: ImageRepeat)

Sets how the image is repeated. When set to repeat, the image is repeated from the center to edges. The last image will be clipped if it does not fit in the component. This attribute is not applicable to SVG images.

This attribute does not take effect when the parameter type of the component is [AnimatedDrawableDescriptor](../../../arkts-api/ui/ohos-arkui-drawabledescriptor-drawabledescriptor/document.md#animateddrawabledescriptor12).

**Widget capability**: This API can be used in ArkTS widgets since API version 9.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | [ImageRepeat](../../common-definitions/enums/document.md#imagerepeat) | Yes | 
How the image is repeated.

Default value: **ImageRepeat.NoRepeat**

 |

#### \[h2\]interpolation

interpolation(value: ImageInterpolation)

Defines the image interpolation effect. This attribute mitigates aliasing during image scaling. This attribute is not applicable to SVG images.

This attribute does not take effect when the parameter type of the component is [AnimatedDrawableDescriptor](../../../arkts-api/ui/ohos-arkui-drawabledescriptor-drawabledescriptor/document.md#animateddrawabledescriptor12).

**Widget capability**: This API can be used in ArkTS widgets since API version 9.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | [ImageInterpolation](#imageinterpolation) | Yes | 
Interpolation effect of the image.

Default value: **ImageInterpolation.Low**

When set to **undefined**, the value is treated as **ImageInterpolation.None**.

 |

#### \[h2\]renderMode

renderMode(value: ImageRenderMode)

Sets the rendering mode of the image. This attribute is not applicable to SVG images.

This attribute does not take effect when [ColorFilter](#colorfilter9) is set.

This attribute does not take effect when the parameter type of the component is [AnimatedDrawableDescriptor](../../../arkts-api/ui/ohos-arkui-drawabledescriptor-drawabledescriptor/document.md#animateddrawabledescriptor12).

**Widget capability**: This API can be used in ArkTS widgets since API version 9.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | [ImageRenderMode](#imagerendermode) | Yes | 
Rendering mode of the image, which can be **Original** or **Template** (monochrome).

Default value: **ImageRenderMode.Original**

 |

#### \[h2\]sourceSize

sourceSize(value: ImageSourceSize)

Sets the decoding size of the image. This attribute works only when the target size is smaller than the source size. This attribute is not applicable to SVG images or **PixelMap** objects.

This attribute does not take effect when the parameter type of the component is [AnimatedDrawableDescriptor](../../../arkts-api/ui/ohos-arkui-drawabledescriptor-drawabledescriptor/document.md#animateddrawabledescriptor12).

**Widget capability**: This API can be used in ArkTS widgets since API version 9.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | [ImageSourceSize](#imagesourcesize18) | Yes | Decoding size of the image. This parameter can be used to reduce the image resolution when the image display size needs to be smaller than the component size. When this parameter is used with **ImageFit.None** of the [objectFit](#objectfit) API, a small image can be displayed in the component. |

#### \[h2\]matchTextDirection

matchTextDirection(value: boolean)

Specifies whether the image follows the system language direction, displaying a mirrored effect in a right-to-left (RTL) language environments.

This attribute does not take effect when the parameter type of the component is [AnimatedDrawableDescriptor](../../../arkts-api/ui/ohos-arkui-drawabledescriptor-drawabledescriptor/document.md#animateddrawabledescriptor12).

**Widget capability**: This API can be used in ArkTS widgets since API version 9.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | boolean | Yes | 
Whether the image follows the system language direction, displaying a mirrored effect in an RTL language environment.

Default value: **false**

The value **true** means that the image follows the system language direction, displaying a mirrored effect in an RTL language environment, and **false** means the opposite.

 |

#### \[h2\]fitOriginalSize

fitOriginalSize(value: boolean)

Specifies whether the image display size follows the size of the image source.

This attribute does not take effect when the component has the **width** and **height** attributes set.

This attribute does not take effect when the parameter type of the component is [AnimatedDrawableDescriptor](../../../arkts-api/ui/ohos-arkui-drawabledescriptor-drawabledescriptor/document.md#animateddrawabledescriptor12).

**Widget capability**: This API can be used in ArkTS widgets since API version 9.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | boolean | Yes | 
Whether the image display size follows the size of the image source.

Default value: **false**

**NOTE**

**false** or not set: The image display size does not follow the size of the image source.

**true**: The image display size follows the size of the image source.

 |

#### \[h2\]fillColor

fillColor(value: ResourceColor)

Fill color to be superimposed on the image. This attribute applies only to SVG images. Once set, the fill color will replace the fill colors of all drawable elements within the SVG image. To set the fill color for a PNG image, use [colorFilter](#colorfilter9).

This attribute does not take effect when the parameter type of the component is [AnimatedDrawableDescriptor](../../../arkts-api/ui/ohos-arkui-drawabledescriptor-drawabledescriptor/document.md#animateddrawabledescriptor12).

**Widget capability**: This API can be used in ArkTS widgets since API version 9.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | [ResourceColor](../../common-definitions/basic-types/document.md#resourcecolor) | Yes | 
Fill color to be superimposed on the image.

**NOTE**

By default, no fill color is applied. If an invalid value is passed, the system uses the default theme color: black in light mode and white in dark mode.

Since API version 21, when [supportSvg2](#supportsvg221) is set to **true**, **fillColor** depends on the **fill** attribute configuration in the SVG image source. If the **fill** attribute in the SVG image source is set to **'none'**, **fillColor** does not take effect. When **supportSvg2** is set to **false**, **fillColor** takes effect and replaces the fill colors of all drawable elements in the SVG image.

 |

#### \[h2\]fillColor15+

fillColor(color: ResourceColor|ColorContent)

Fill color to be superimposed on the image. This attribute applies only to SVG images. Once set, the fill color will replace the fill colors of all drawable elements within the SVG image. To set the fill color for a PNG image, use [colorFilter](#colorfilter9). To reset the fill color, pass a value of the [ColorContent](#colorcontent15) type.

This attribute does not take effect when the parameter type of the component is [AnimatedDrawableDescriptor](../../../arkts-api/ui/ohos-arkui-drawabledescriptor-drawabledescriptor/document.md#animateddrawabledescriptor12).

**Atomic service API**: This API can be used in atomic services since API version 15.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| color | [ResourceColor](../../common-definitions/basic-types/document.md#resourcecolor)|[ColorContent](#colorcontent15) | Yes | 
Fill color to be superimposed on the image.

**NOTE**

By default, no fill color is applied. If an invalid value is passed, the system uses the default theme color: black in light mode and white in dark mode.

Since API version 21, when [supportSvg2](#supportsvg221) is set to **true**, **fillColor** depends on the **fill** attribute configuration in the SVG image source. If the **fill** attribute in the SVG image source is set to **'none'**, **fillColor** does not take effect.

 |

#### \[h2\]fillColor20+

fillColor(color: ResourceColor|ColorContent|ColorMetrics)

Fill color to be superimposed on the image. This attribute applies only to SVG images. Once set, the fill color will replace the fill colors of all drawable elements within the SVG image. To set the fill color for a PNG image, use [colorFilter](#colorfilter9). To reset the fill color, pass a value of the [ColorContent](#colorcontent15) type. You can set P3 color gamut values by passing in the [ColorMetrics](../../../arkts-api/ui/arkui/graphics/document.md#colormetrics12) type, which can achieve richer color performance on devices that support high color gamut.

This attribute does not take effect when the parameter type of the component is [AnimatedDrawableDescriptor](../../../arkts-api/ui/ohos-arkui-drawabledescriptor-drawabledescriptor/document.md#animateddrawabledescriptor12).

**Atomic service API**: This API can be used in atomic services since API version 20.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| color | [ResourceColor](../../common-definitions/basic-types/document.md#resourcecolor)|[ColorContent](#colorcontent15)|[ColorMetrics](../../../arkts-api/ui/arkui/graphics/document.md#colormetrics12) | Yes | 
Fill color to be superimposed on the image.

**NOTE**

By default, no fill color is applied. If an invalid value is passed, the system uses the default theme color: black in light mode and white in dark mode.

Since API version 21, when [supportSvg2](#supportsvg221) is set to **true**, **fillColor** depends on the **fill** attribute configuration in the SVG image source. If the **fill** attribute in the SVG image source is set to **'none'**, **fillColor** does not take effect.

 |

#### \[h2\]autoResize

autoResize(value: boolean)

Specifies whether to resize the image source based on the size of the display area during image decoding. As downsampling images results in some loss of information, it may reduce the image quality, causing issues such as aliasing. To retain the original image quality, set **autoResize** to **false**, but this may increase the memory usage.

If the original image size does not match the display size, the image may be distorted or blurred. Recommended configuration for the optimal definition:

When the image is scaled down: .autoResize(false) + .interpolation(.Medium)

When the image is scaled up: .interpolation(.High)

This attribute does not take effect when the parameter type of the component is [AnimatedDrawableDescriptor](../../../arkts-api/ui/ohos-arkui-drawabledescriptor-drawabledescriptor/document.md#animateddrawabledescriptor12) or the image format is SVG.

**Widget capability**: This API can be used in ArkTS widgets since API version 9.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | boolean | Yes | 
Whether to resize the image source based on the size of the display area during image decoding. This resizing can help reduce the memory usage. For example, if the original image size is 800 x 1200 and the display area size is 200 x 200, the image will be decoded to 200 x 300 at a downsampled resolution (the actual result may vary depending on the scaling and fill type configurations used in the calculation), greatly reducing the memory occupied by the image.

Default value: **false**

**true**: Enable resizing.

**false**: Disable resizing.

 |

#### \[h2\]syncLoad8+

syncLoad(value: boolean)

Specifies whether to load the image synchronously. When loading a small local image, you are advised to set **syncLoad** to **true** so that the image loading can be quickly completed on the main thread.

This attribute does not take effect when the parameter type of the component is [AnimatedDrawableDescriptor](../../../arkts-api/ui/ohos-arkui-drawabledescriptor-drawabledescriptor/document.md#animateddrawabledescriptor12).

If image flickering occurs during loading, set **syncLoad** to **true**. For details, see [Optimizing Concurrent Tasks](https://developer.huawei.com/consumer/en/doc/best-practices/bpta-click-to-click-response-optimization#section715115119192).

**Widget capability**: This API can be used in ArkTS widgets since API version 9.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | boolean | Yes | 
Whether to load the image synchronously. By default, the image is loaded asynchronously. During synchronous loading, the UI thread is blocked and the placeholder image is not displayed.

Default value: **false**

**true**: Load the image synchronously.

**false**: Load the image asynchronously.

If the main thread is blocked for more than 6s, AppFreeze will occur. For details, see [Application Freeze Detection](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/appfreeze-guidelines).

 |

#### \[h2\]copyOption9+

copyOption(value: CopyOptions)

Specifies whether the image can be copied. When **copyOption** is set to a value other than **CopyOptions.None**, the image can be copied through multiple interactions, such as long press, right-click, or Ctrl+C. SVG images cannot be copied.

This attribute does not take effect when the parameter type of the component is [AnimatedDrawableDescriptor](../../../arkts-api/ui/ohos-arkui-drawabledescriptor-drawabledescriptor/document.md#animateddrawabledescriptor12).

**Widget capability**: This API can be used in ArkTS widgets since API version 9.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | [CopyOptions](../../common-definitions/enums/document.md#copyoptions9) | Yes | 
Specifies whether the image can be copied.

Default value: **CopyOptions.None**

 |

#### \[h2\]colorFilter9+

colorFilter(value: ColorFilter | DrawingColorFilter)

Sets the color filter for the image.

When this attribute is set, [renderMode](#rendermode) is not effective.

**Widget capability**: This API can be used in ArkTS widgets since API version 9.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | [ColorFilter](../../common-definitions/basic-types/document.md#colorfilter9) | [DrawingColorFilter12+](#drawingcolorfilter12) | Yes | 
1\. Color filter of the image. The input parameter is a 4 x 5 RGBA transformation matrix.

2\. The ColorFilter type of **@ohos.graphics.drawing** can be used as an input parameter since API version 12.

**NOTE**

This parameter is not available for SVG images in API version 11 and earlier versions.

The DrawingColorfilter type can be used in atomic services since API version 12. For SVG sources, the effect only applies when the **stroke** property is set (regardless of the value).

Since API version 21, when [supportSvg2](#supportsvg221) is set to **true**, **colorFilter** takes effect on the entire SVG image source.

 |

The color filter is applied to the image using a 4 x 5 matrix. The first row of the matrix represents the vector values for the R (red) channel, the second row represents the vector values for the G (green) channel, the third row represents the vector values for the B (blue) channel, and the fourth row represents the vector values for the A (alpha) channel. Each of the four rows corresponds to the vector values of a distinct RGBA channel.

When the values on the matrix diagonal are **1** and all other values are **0**, the original colors of the image are preserved.

**Calculation rule:**

The following example shows the input filter matrix.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5b/v3/sLYeSwhQRAG_593oRJy9WA/en-us_image_0000002537925628.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062243Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=2EB64457BD6A7428F685519E2E449490521122EA5C7D74617B40597C3FB28A05)

The pixel is represented as \[R, G, B, A\], with color values in the \[0, 255\] range.

The filtered color will be \[R', G', B', A'\].

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e8/v3/D6uNBHBYTnyTQSDthmPH5Q/en-us_image_0000002568685405.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062243Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=5C34635397AD3B07EF8F4C6913DEDD8ED2685E8FB93A861E550A9ADC972BF4C7)

For details about how to use this attribute, see [Example 9](#example-9-setting-a-color-filter-for-an-image).

#### \[h2\]draggable9+

draggable(value: boolean)

Specifies whether the image is draggable.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | boolean | Yes | 
Whether the image is draggable. The value **true** means that the image is draggable, in which case the bound long press gesture will not take effect.

Default value:

API version 9 and earlier: **false**

Since API version 10: **true**

To bind custom gestures to the component, set **draggable** to **false**. With the value **false**, drag-related events are not triggered.

 |

#### \[h2\]enableAnalyzer11+

enableAnalyzer(enable: boolean)

Sets whether to enable the AI image analyzer, which supports subject recognition, text recognition, and object lookup.For details, see [AI Image Recognition](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/vision-imageanalyzer).

This attribute cannot be used together with the [overlay](../../universal-attributes/basic-attributes/overlay-control/document.md#overlay) attribute. If they are set at the same time, the [CustomBuilder](../../common-definitions/basic-types/document.md#custombuilder8) attribute in **overlay** has no effect. This feature also depends on device capabilities.

Images to be analyzed must be static, non-vector images. That is, SVG and GIF images cannot be analyzed. [Pixel maps](../../../../../media/image-kit/arkts-apis/ohos-multimedia-image-image-processing/interface-pixelmap/document.md) in [RGBA\_8888](../../../../../media/image-kit/arkts-apis/ohos-multimedia-image-image-processing/enums/document.md#pixelmapformat7) format can be passed in for analysis. For details, see [Example 5: Enabling the AI Image Analyzer](#example-5-enabling-the-ai-image-analyzer).

The [alt](#alt) placeholder image does not support analysis. The [objectRepeat](#objectrepeat) attribute supports analysis only when it is set to **ImageRepeat.NoRepeat**. Analysis is not supported when the [obscured](../../universal-attributes/basic-attributes/obscuring/document.md#obscured) attribute is enabled.

Analysis is performed based on the complete original image. Even if the settings of the [clip](../../universal-attributes/visual-effects/shape-clipping/document.md#clip12), [margin](../../universal-attributes/layout-and-borders/sizing/document.md#margin), [borderRadius](../../universal-attributes/layout-and-borders/border-styling/document.md#borderradius), [position](../../universal-attributes/layout-and-borders/location/document.md#position), and [objectFit](#objectfit) attributes cause incomplete image display, or if a mask layer is set via [renderMode](#rendermode), analysis will still be conducted on the complete original image. The [copyOption](#copyoption9) attribute does not affect the AI image analyzer functionality.

This attribute does not take effect when the parameter type of the component is [AnimatedDrawableDescriptor](../../../arkts-api/ui/ohos-arkui-drawabledescriptor-drawabledescriptor/document.md#animateddrawabledescriptor12).

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9c/v3/2B59nzm9T122BZlPMXlHaQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062243Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=9AFB7A362B81305413CC5BF690722B438A0AD6473A894E4017A7B347907AA4EE)

-   The **ohos.permission.INTERNET** permission is required.
    
-   This API can be called within [attributeModifier](../../universal-attributes/modifiers-and-custom-property/attribute-modifier/document.md#attributemodifier) since API version 12.
    

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| enable | boolean | Yes | 
Whether the **Image** component supports AI analysis.

When this parameter is set to **true**, the **Image** component supports AI analysis. When this parameter is set to **false**, the **Image** component does not support AI analysis.

Default value: **false**

 |

#### \[h2\]resizable11+

resizable(value: ResizableOptions)

Sets the resizable image options. Resizing is effective for drag previews and placeholder images.

When a valid [ResizableOptions](#resizableoptions11) is set, the **objectRepeat** and **orientation** attributes do not take effect.

When the sum of the values of **top** and **bottom** is greater than the source image height, or the sum of the values of **left** and **right** is greater than the source image width, the [ResizableOptions](#resizableoptions11) attribute does not take effect.

This attribute does not take effect when the parameter type of the component is [AnimatedDrawableDescriptor](../../../arkts-api/ui/ohos-arkui-drawabledescriptor-drawabledescriptor/document.md#animateddrawabledescriptor12) or the image format is SVG.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b1/v3/gUYvROZGTlKC62hwI1JvtA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062243Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=E758F2019EE7AF21C5A30DB4202BD41E03DEF2B5929CB6314C04F9E104D04916)

This API can be called in [attributeModifier](../../universal-attributes/modifiers-and-custom-property/attribute-modifier/document.md#attributemodifier) since API version 20.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | [ResizableOptions](#resizableoptions11) | Yes | Resizable image options. |

#### \[h2\]privacySensitive12+

privacySensitive(supported: boolean)

Sets whether to secure sensitive information on widgets.

**Widget capability**: This API can be used in ArkTS widgets since API version 12.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| supported | boolean | Yes | 
Whether to secure sensitive information on widgets.

**false** (default): Do not secure sensitive information on widgets.

**true**: Secure sensitive information on widgets, obscuring the image with a semi-transparent background style in privacy mode.

**NOTE**

If this parameter is set to **null**, the image is not obscured.

Privacy mode requires support from the widget framework.

 |

#### \[h2\]dynamicRangeMode12+

dynamicRangeMode(value: DynamicRangeMode)

Sets the dynamic range of the image to be displayed. This attribute is not applicable to SVG images.

**Device behavior difference**: This API takes effect on mobile phones, PCs, 2-in-1 devices, and tablets, but not on other device types.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | [DynamicRangeMode](#dynamicrangemode12) | Yes | 
Dynamic range of the image.

Default value: **DynamicRangeMode.STANDARD**

 |

#### \[h2\]orientation14+

orientation(orientation: ImageRotateOrientation)

Sets the display orientation of the image content.

This attribute does not apply to placeholder images specified by [alt](#alt).

**Atomic service API**: This API can be used in atomic services since API version 14.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| orientation | [ImageRotateOrientation](#imagerotateorientation14) | Yes | 
Display orientation of the image content.

Only static pixel map display is supported.

For images containing rotation or flip information, use **ImageRotateOrientation.AUTO**.

Default value: **ImageRotateOrientation.UP**

When this parameter is set to **undefined** or **null**, the value is **ImageRotateOrientation.AUTO**.

 |

#### \[h2\]hdrBrightness19+

hdrBrightness(brightness: number)

Sets the brightness of HDR images displayed by the component.

This attribute is not applicable to SVG images.

If this attribute and the [dynamicRangeMode](#dynamicrangemode12) attribute are both set, [dynamicRangeMode](#dynamicrangemode12) does not take effect.

**Atomic service API**: This API can be used in atomic services since API version 19.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| brightness | number | Yes | 
Brightness of HDR images displayed by the component. This API only takes effect for HDR image sources.

Default value: **1.0**

Value range: \[0.0,1.0\]. Values less than 0 or greater than 1.0 are clamped to **1.0**. **0**: The image is displayed at SDR brightness.

**1.0**: The image is displayed at the highest allowed HDR brightness.

 |

#### \[h2\]supportSvg221+

supportSvg2(enable: boolean)

Sets whether to enable [enhanced SVG tag parsing](../enhanced-svg-tag-parsing/document.md). When this feature is enabled, SVG image rendering behavior changes accordingly.

After the **Image** component is created, the value of this attribute cannot be dynamically changed.

**Widget capability**: This API can be used in ArkTS widgets since API version 21.

**Atomic service API**: This API can be used in atomic services since API version 21.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| enable | boolean | Yes | 
Determines whether to enable the enhanced SVG tag parsing feature.

Default value: **false**

**true**: Enable enhanced SVG parsing.

**false**: Use original SVG parsing.

 |

#### \[h2\]contentTransition21+

contentTransition(transition: ContentTransitionEffect)

Triggers transition animations when the image content changes.

**Atomic service API**: This API can be used in atomic services since API version 21.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| transition | [ContentTransitionEffect](../image-analysis-types/document.md#contenttransitioneffect21) | Yes | 
Type of transition animation.

The value **ContentTransitionEffect.OPACITY** indicates the fade-in/fade-out effect, and the value **ContentTransitionEffect.IDENTITY** indicates no animation effect.

Default value: **ContentTransitionEffect.IDENTITY**

When this parameter is set to **undefined** or **null**, the value defaults to **ContentTransitionEffect.IDENTITY**.

Note: This parameter does not take effect for dynamic image resources.

 |

#### ImageContent12+

Defines the image content.

**Widget capability**: This API can be used in ArkTS widgets since API version 12.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Value | Description |
| :-- | :-- | :-- |
| EMPTY | 0 | Empty image. |

#### ImageInterpolation

Interpolation effect of the image.

**Widget capability**: This API can be used in ArkTS widgets since API version 9.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Value | Description |
| :-- | :-- | :-- |
| None | 0 | Nearest neighbor interpolation. |
| Low | 1 | Bilinear interpolation. |
| Medium | 2 | MipMap interpolation. |
| High | 3 | Cubic interpolation. This mode produces scaled images of the highest possible quality, but may require more image rendering time. |

#### ImageRenderMode

Enumerates the rendering modes of images.

**Widget capability**: This API can be used in ArkTS widgets since API version 9.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Value | Description |
| :-- | :-- | :-- |
| Original | 0 | Render image pixels as they are in the original source image. |
| Template | 1 | Render image pixels to create a monochrome template image. |

#### ResizableOptions11+

Defines the resizable image options.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| slice | [EdgeWidths](../../common-definitions/basic-types/document.md#edgewidths9) | No | Yes | 
Edge widths in different directions of a component.

**NOTE**

This attribute takes effect only when both **bottom** and **right** are greater than 0.

When **top** is set, the top part of the image is stretched while the pixel values of the image remain unchanged.

When **right** is set, the right part of the image is stretched while the pixel values of the image remain unchanged.

When **bottom** is set, the bottom part of the image is stretched while the pixel values of the image remain unchanged.

When **left** is set, the left part of the image is stretched while the pixel values of the image remain unchanged.

The default width of each direction is **0**. The default unit is vp.

The effect of setting **EdgeWidths** is shown in Figure 1 (Effect of Setting EdgeWidths).

 |
| lattice12+ | [DrawingLattice](#drawinglattice12) | No | Yes | 

Lattice object, which is used to divide the image by lattice.

**NOTE**

Use the [createImageLattice](../../../../../graphics/arkgraphics-2d/arkts-apis/ohos-graphics-drawing-drawing-module/class-lattice/document.md#createimagelattice12) API of **@ohos.graphics.drawing** to create a **Lattice** type as the input parameter. Lattices located at both even columns and even rows are fixed; those at other positions are stretched according to **slice**.

This parameter does not take effect for the [backgroundImageResizable](../../universal-attributes/basic-attributes/background/document.md#backgroundimageresizable12) API.

When a number is passed, the default unit is px.

 |

**Figure 1** Effect of Setting EdgeWidths

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/82/v3/8tU6m7KCTfufhRaBfBJgeA/en-us_image_0000002537925644.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062243Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=3B848C1BE867C607309D9E15518915B4B0372B02CE74EF1D9214E55A787C0524)

#### ImageAlt22+

Sets the placeholder image.

**Widget capability**: This API can be used in ArkTS widgets since API version 22.

**Atomic service API**: This API can be used in atomic services since API version 22.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| placeholder | [ResourceStr](../../common-definitions/basic-types/document.md#resourcestr) | [PixelMap](../../../../../media/image-kit/arkts-apis/ohos-multimedia-image-image-processing/interface-pixelmap/document.md) | No | Yes | Placeholder image displayed during loading. |
| error | [ResourceStr](../../common-definitions/basic-types/document.md#resourcestr) | [PixelMap](../../../../../media/image-kit/arkts-apis/ohos-multimedia-image-image-processing/interface-pixelmap/document.md) | No | Yes | Placeholder image displayed when loading fails. |

#### DynamicRangeMode12+

Describes the dynamic range of the image to be displayed.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Value | Description |
| :-- | :-- | :-- |
| HIGH | 0 | Unrestricted dynamic range, which allows for the maximum brightening of an image. |
| CONSTRAINT | 1 | Restricted dynamic range, which brightens an image within certain constraints. |
| STANDARD | 2 | Standard dynamic range, which does not brighten an image. |

#### ImageRotateOrientation14+

Describes the desired display orientation for image content.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Value | Description |
| :-- | :-- | :-- |
| AUTO | 0 | 
Use EXIF metadata for display orientation, with support for rotation and mirroring.

Images of the [PixelMap](../../../../../media/image-kit/arkts-apis/ohos-multimedia-image-image-processing/interface-pixelmap/document.md) and [DrawableDescriptor](#drawabledescriptor10) types do not contain header information. When this API is called, the image display effect remains unchanged.

**Atomic service API**: This API can be used in atomic services since API version 14.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ad/v3/w1bvspOHSHC53WTkMU_MVg/en-us_image_0000002568685421.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062243Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=9F232452AD6CCABAD04F1B85341B979A4D59384961F4CEBA92A1984A1AE6C1E8)

 |
| UP | 1 | 

Display original pixel data without transformation.

**Atomic service API**: This API can be used in atomic services since API version 14.

 |
| RIGHT | 2 | 

Display the image after rotating it 90 degrees clockwise.

**Atomic service API**: This API can be used in atomic services since API version 14.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5c/v3/oQPZ5O_6S4SSU-eXtV4dFg/en-us_image_0000002568765431.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062243Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=B7BD5C9170629F801562C82A1CFAD6B26647C1476FA3E9C1A0C7DCE72EC0624D)

 |
| DOWN | 3 | 

Display the image after rotating it 180 degrees clockwise.

**Atomic service API**: This API can be used in atomic services since API version 14.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/62/v3/FxScm-kxR-SecJfa-QGxrA/en-us_image_0000002537765706.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062243Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=4CF85EC7C80EBA967AA84121FE56302FFBA2B5E9133DF95E4E20F9E02A86DA3B)

 |
| LEFT | 4 | 

Display the image after rotating it 270 degrees clockwise.

**Atomic service API**: This API can be used in atomic services since API version 14.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/39/v3/Q8BL3cdOShWK7Kj-iANjxQ/en-us_image_0000002537925646.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062243Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=478BFE83D7F0C5D6FC462292AEDB79EA3DCDF3F0FA6CB517B29CF3059703D197)

 |
| UP\_MIRRORED20+ | 5 | 

Display the image after flipping it horizontally.

**Atomic service API**: This API can be used in atomic services since API version 20.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/83/v3/r_wALm5vTX2eWs0T20Vlhg/en-us_image_0000002568685423.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062243Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=17DB2888206290DA3E77B0E44FD73ED0D8E02B14484E64BCB2D8A4932BB3C346)

 |
| RIGHT\_MIRRORED20+ | 6 | 

Display the image after flipping it horizontally and then rotating it 90 degrees clockwise.

**Atomic service API**: This API can be used in atomic services since API version 20.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/50/v3/NsgwwBtJTwebYH_eb1w7Aw/en-us_image_0000002568765433.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062243Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=9873937CF1AEAD876BB690E1F372F8DD3BA633F37D12B49AAEFE39CDC7999F66)

 |
| DOWN\_MIRRORED20+ | 7 | 

Display the image after flipping it vertically.

**Atomic service API**: This API can be used in atomic services since API version 20.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4a/v3/eOyStPXsSkyCnFM7_K82bg/en-us_image_0000002537765708.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062243Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=EA73C3AE81543323E2507BCF17E2CAAEA94D78646EB368D6FF4AE99FCE9E702A)

 |
| LEFT\_MIRRORED20+ | 8 | 

Display the image after flipping it horizontally and then rotating it 270 degrees clockwise.

**Atomic service API**: This API can be used in atomic services since API version 20.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ad/v3/f-re9BNLQ0uanj3FEr8z4w/en-us_image_0000002537925648.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062243Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=622DB0F3E4BE437905D69EA6DA6ABEA1A83726535420C9BB75B0342BFEA45FEB)

 |

#### ImageSourceSize18+

Provides the image decoding size.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9a/v3/8mtISpLSS8qLeCt9cLKDjQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062243Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=B385E749173F6D128937CF93454FA3490C3D9A9DA889CCE56D03E12726B1ECB3)

To standardize anonymous object definitions, the element definitions here have been revised in API version 18. While historical version information is preserved for anonymous objects, there may be cases where the outer element's @since version number is higher than inner elements'. This does not affect interface usability.

**Widget capability**: This API can be used in ArkTS widgets since API version 18.

**Atomic service API**: This API can be used in atomic services since API version 18.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| width7+ | number | No | No | 
Width of the decoded image.

Unit: vp.

**Widget capability**: This API can be used in ArkTS widgets since API version 9.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| height7+ | number | No | No | 

Height of the decoded image.

Unit: vp.

**Widget capability**: This API can be used in ArkTS widgets since API version 9.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |

#### DrawableDescriptor10+

type DrawableDescriptor = DrawableDescriptor

Represents a parameter object for the **Image** component.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Type | Description |
| :-- | :-- |
| [DrawableDescriptor](../../../arkts-api/ui/ohos-arkui-drawabledescriptor-drawabledescriptor/document.md#drawabledescriptor) | **DrawableDescriptor** object. |

#### DrawingColorFilter12+

type DrawingColorFilter = ColorFilter

Represents a color filter object.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Type | Description |
| :-- | :-- |
| [ColorFilter](../../../../../graphics/arkgraphics-2d/arkts-apis/ohos-graphics-drawing-drawing-module/class-colorfilter/document.md) | Color filter created. |

#### DrawingLattice12+

type DrawingLattice = Lattice

Represents a matrix grid object that divides an image into a rectangular grid.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Type | Description |
| :-- | :-- |
| [Lattice](../../../../../graphics/arkgraphics-2d/arkts-apis/ohos-graphics-drawing-drawing-module/class-lattice/document.md) | Matrix grid object used to divide the image into a rectangular grid. |

#### ImageMatrix15+

type ImageMatrix = Matrix4Transit

Represents the current matrix object.

**Atomic service API**: This API can be used in atomic services since API version 15.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Type | Description |
| :-- | :-- |
| [Matrix4Transit](../../../arkts-api/ui/ohos-matrix4-matrix-transformation/document.md#matrix4transit) | Current matrix object. |

#### ColorContent15+

Defines the content for color filling.

**Atomic service API**: This API can be used in atomic services since API version 15.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| ORIGIN | ColorContent | Yes | No | Resets the [fillColor](#fillcolor) API, effectively the same as not setting [fillColor](#fillcolor). |

#### Events

In addition to the [universal events](../../universal-events/document.md), the following events are supported.

#### \[h2\]onComplete

onComplete(callback: (event?: { width: number, height: number, componentWidth: number, componentHeight: number, loadingStatus: number,contentWidth: number, contentHeight: number, contentOffsetX: number, contentOffsetY: number }) => void)

Triggered when an image is successfully loaded or decoded. The size of the loaded image is returned.

This event is not triggered if the parameter type of the component is [AnimatedDrawableDescriptor](../../../arkts-api/ui/ohos-arkui-drawabledescriptor-drawabledescriptor/document.md#animateddrawabledescriptor12).

**Widget capability**: This API can be used in ArkTS widgets since API version 9.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| width | number | Yes | 
Width of the image.

Unit: px

**Widget capability**: This API can be used in ArkTS widgets since API version 9.

 |
| height | number | Yes | 

Height of the image.

Unit: px

**Widget capability**: This API can be used in ArkTS widgets since API version 9.

 |
| componentWidth | number | Yes | 

Width of the component.

Unit: px

**Widget capability**: This API can be used in ArkTS widgets since API version 9.

 |
| componentHeight | number | Yes | 

Height of the component.

Unit: px

**Widget capability**: This API can be used in ArkTS widgets since API version 9.

 |
| loadingStatus | number | Yes | 

Loading status of the image.

**NOTE**

If the return value is **0**, the image is successfully loaded. If the return value is **1**, the image is successfully decoded.

**Widget capability**: This API can be used in ArkTS widgets since API version 9.

 |
| contentWidth10+ | number | Yes | 

Actual rendered width of the image.

Unit: px

**NOTE**

This parameter is valid only when the return value of **loadingStatus** is **1**.

**Widget capability**: This API can be used in ArkTS widgets since API version 10.

 |
| contentHeight10+ | number | Yes | 

Actual rendered height of the image.

Unit: px

**NOTE**

This parameter is valid only when the return value of **loadingStatus** is **1**.

**Widget capability**: This API can be used in ArkTS widgets since API version 10.

 |
| contentOffsetX10+ | number | Yes | 

Offset of the rendered content relative to the component on the x-axis.

Unit: px

**NOTE**

This parameter is valid only when the return value of **loadingStatus** is **1**.

**Widget capability**: This API can be used in ArkTS widgets since API version 10.

 |
| contentOffsetY10+ | number | Yes | 

Offset of the rendered content relative to the component on the y-axis

Unit: px

**NOTE**

This parameter is valid only when the return value of **loadingStatus** is **1**.

**Widget capability**: This API can be used in ArkTS widgets since API version 10.

 |

#### \[h2\]onError9+

onError(callback: ImageErrorCallback)

Triggered when an error occurs during image loading.

This event is not triggered if the parameter type of the component is [AnimatedDrawableDescriptor](../../../arkts-api/ui/ohos-arkui-drawabledescriptor-drawabledescriptor/document.md#animateddrawabledescriptor12).

**Widget capability**: This API can be used in ArkTS widgets since API version 9.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | [ImageErrorCallback](#imageerrorcallback9) | Yes | 
Callback triggered when an error occurs during image loading.

**NOTE**

You are advised to use this callback to quickly identify the cause of image loading failures. For details, see the [ImageError](#imageerror9) error codes.

 |

#### \[h2\]onFinish

onFinish(event: () => void)

Triggered when the animation playback in the loaded SVG image is complete. If the animation is an infinite loop, this callback is not triggered.

Only images in SVG format are supported. This event is not triggered if the parameter type of the component is [AnimatedDrawableDescriptor](../../../arkts-api/ui/ohos-arkui-drawabledescriptor-drawabledescriptor/document.md#animateddrawabledescriptor12).

**Widget capability**: This API can be used in ArkTS widgets since API version 9.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| event | () => void | Yes | Triggered when the animation playback in the loaded SVG image is complete. If the animation is an infinite loop, this callback is not triggered. |

#### ImageErrorCallback9+

type ImageErrorCallback = (error: ImageError) => void

Triggered when an error occurs during image loading.

This event is not triggered if the parameter type of the component is [AnimatedDrawableDescriptor](../../../arkts-api/ui/ohos-arkui-drawabledescriptor-drawabledescriptor/document.md#animateddrawabledescriptor12).

**Widget capability**: This API can be used in ArkTS widgets since API version 9.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| error | [ImageError](#imageerror9) | Yes | Object returned by the callback triggered when an exception occurs during image loading. |

#### ImageError9+

Describes the object returned by the image loading error callback.

This event is not triggered if the parameter type of the component is [AnimatedDrawableDescriptor](../../../arkts-api/ui/ohos-arkui-drawabledescriptor-drawabledescriptor/document.md#animateddrawabledescriptor12).

**Widget capability**: This API can be used in ArkTS widgets since API version 9.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| componentWidth | number | No | No | 
Width of the component.

Unit: px

**Widget capability**: This API can be used in ArkTS widgets since API version 9.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| componentHeight | number | No | No | 

Height of the component.

Unit: px

**Widget capability**: This API can be used in ArkTS widgets since API version 9.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| message10+ | string | No | No | 

Error information.

**Widget capability**: This API can be used in ArkTS widgets since API version 10.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| error20+ | [BusinessError<void>](#businesserror20) | No | Yes | 

Error information returned when an error occurs during image loading, where **code** represents the error code and **message** indicates the error message. For details, see the error code reference below.

Default value: **{ code : -1, message : "" }**

**Widget capability**: This API can be used in ArkTS widgets since API version 20.

**Atomic service API**: This API can be used in atomic services since API version 20.

 |

#### BusinessError20+

type BusinessError<T = void> = BusinessError<T>

Represents the error information returned when an error occurs during image loading.

**Widget capability**: This API can be used in ArkTS widgets since API version 20.

**Atomic service API**: This API can be used in atomic services since API version 20.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Type | Description |
| :-- | :-- |
| [BusinessError<T>](../../../../../system/basic-functions/basic-services-kit/arkts-apis/others/ohos-base-public-callback-information/document.md#businesserror) | Error information returned when an error occurs during image loading. |

The table below describes the **ImageError** error codes. The **error** property of **ImageError** contains error details with **code** and **message** fields, representing the error code and error message, respectively.

| ID | Error Message | Stage of Occurrence | Image Type |
| :-- | :-- | :-- | :-- |
| 101000 | unknown source type. | Data loading | Unknown |
| 102010 | sync http task of uri cancelled. | Data loading | Network file |
| 102011 | sync http task of uri failed. | Data loading | Network file |
| 102012 | async http task of uri cancelled. | Data loading | Network file |
| 102013 | async http task of uri failed. | Data loading | Network file |
| 102030 | wrong code format. | Data loading | Base64 string file |
| 102031 | decode base64 image failed. | Data loading | Base64 string file |
| 102050 | path is too long. | Data loading | Sandbox file |
| 102051 | read data failed. | Data loading | Sandbox file |
| 102070 | get image data by name failed. | Data loading | Resource file |
| 102071 | get image data by id failed. | Data loading | Resource file |
| 102072 | uri is invalid. | Data loading | Resource file |
| 102090 | uri is invalid. | Data loading | In-package file |
| 102091 | get asset failed. | Data loading | In-package file |
| 102110 | open file failed. | Data loading | Media library file |
| 102111 | get file stat failed. | Data loading | Media library file |
| 102112 | read file failed. | Data loading | Media library file |
| 102130 | decoded data is empty. | Data loading | Media library thumbnail |
| 102131 | load shared memory image data timeout. | Data loading | Shared memory file |
| 103100 | make svg dom failed. | Data loading | Vector graphics file |
| 103200 | image data size is invalid. | Data loading | Pixel map file |
| 111000 | image source create failed. | Data decoding | Pixel map file |
| 111001 | pixelmap create failed. | Data decoding | Pixel map file |

#### Example

## Example 1: Loading Images of Basic Types

This example demonstrates how to load images of basic types, such as PNG, GIF, SVG, and JPG, by passing in [Resource](../../common-definitions/basic-types/document.md#resource) resources.

@Entry
@Component
struct ImageExample1 {
  build() {
    Column() {
      Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Start }) {
        Row() {
          // Load a PNG image.
          // Replace $r('app.media.ic\_camera\_master\_ai\_leaf') with the image resource file you use.
          Image($r('app.media.ic\_camera\_master\_ai\_leaf'))
            .width(110).height(110).margin(15)
            .overlay('png', { align: Alignment.Bottom, offset: { x: 0, y: 20 } })
          // Load a GIF image.
          // Replace $r('app.media.loading') with the image resource file you use.
          Image($r('app.media.loading'))
            .width(110).height(110).margin(15)
            .overlay('gif', { align: Alignment.Bottom, offset: { x: 0, y: 20 } })
        }
        Row() {
          // Load an SVG image.
          // Replace $r('app.media.ic\_camera\_master\_ai\_clouded') with the image resource file you use.
          Image($r('app.media.ic\_camera\_master\_ai\_clouded'))
            .width(110).height(110).margin(15)
            .overlay('svg', { align: Alignment.Bottom, offset: { x: 0, y: 20 } })
          // Load a JPG image.
          // Replace $r('app.media.ic\_public\_favor\_filled') with the image resource file you use.
          Image($r('app.media.ic\_public\_favor\_filled'))
            .width(110).height(110).margin(15)
            .overlay('jpg', { align: Alignment.Bottom, offset: { x: 0, y: 20 } })
        }
      }
    }.height(320).width(360).padding({ right: 10, top: 10 })
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/99/v3/Z8uPGmd9RRyMca-DJP5nzw/en-us_image_0000002568685425.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062243Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=3773DD6E731EFC757CF4041C999299F3BE0BEF4E3F165D97E0F2DD0E94423BC4)

## Example 2: Downloading and Displaying Static Online Images

The default timeout is 5 minutes for loading online images. When using an online image, you are advised to use **alt** to configure a placeholder image displayed during loading. You can use [HTTP](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/http-request) to send a network request, and then decode the returned data into a **PixelMap** object for the **Image** component. Note that a GIF image loaded into a **PixelMap** object will be displayed as a static image. For details about image development, see the [Image Kit](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/image-overview) overview.

The **ohos.permission.INTERNET** permission is required for using online images. For details about how to apply for a permission, see [Declaring Permissions](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/declare-permissions).

import { http } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { image } from '@kit.ImageKit';

@Entry
@Component
struct ImageExample2 {
  @State pixelMapImg: PixelMap | undefined = undefined;

  aboutToAppear() {
    this.requestImageUrl('https://www.example.com/xxx.png'); // Enter a specific online image URL.
  }

  requestImageUrl(url: string) {
    http.createHttp().request(url, (error: BusinessError, data: http.HttpResponse) => {
      if (error) {
        console.error(\`request image failed: url: ${url}, code: ${error.code}, message: ${error.message}\`);
      } else {
        let imgData: ArrayBuffer = data.result as ArrayBuffer;
        console.info(\`request image success, size: ${imgData.byteLength}\`);
        let imgSource: image.ImageSource = image.createImageSource(imgData);
        class sizeTmp {
          height: number = 100;
          width: number = 100;
        }
        let options: Record<string, number | boolean | sizeTmp> = {
          'alphaType': 0,
          'editable': false,
          'pixelFormat': 3,
          'scaleMode': 1,
          'size': { height: 100, width: 100 }
        }
        imgSource.createPixelMap(options).then((pixelMap: PixelMap) => {
          console.error('image createPixelMap success');
          this.pixelMapImg = pixelMap;
          imgSource.release();
        }).catch(() => {
          imgSource.release();
        })
      }
    })
  }

  build() {
    Column() {
      Image(this.pixelMapImg)
        // Replace $r('app.media.img') with the image resource file you use.
        .alt($r('app.media.img'))
        .objectFit(ImageFit.None)
        .width('100%')
        .height('100%')
    }
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a0/v3/PqTagpPsRfar4ZB1xIHi-g/en-us_image_0000002568765435.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062243Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=EC6DF006503605BAF046CC760E5E1B42E021452F101552B5BCF0C85C4D1D9F84)

## Example 3: Downloading and Displaying Online GIF Images

This example shows how to use the [cacheDownload.download](../../../../../system/basic-functions/basic-services-kit/arkts-apis/data-file-processing/ohos-request-cachedownload-download-and-cache/document.md#cachedownloaddownload) API to download online GIF images.

The **ohos.permission.INTERNET** permission is required for using online images. For details about how to apply for a permission, see [Declaring Permissions](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/declare-permissions).

import { cacheDownload } from '@kit.BasicServicesKit';

@Entry
@Component
struct Index {
  @State src: string = 'https://www.example.com/xxx.gif'; // Enter a specific online image URL.

  async aboutToAppear(): Promise<void> {
    // Provide configuration options for the cached download task.
    let options: cacheDownload.CacheDownloadOptions = {};
    try {
      // Perform cached download. If the download is successful, the resource will be cached to the specified file in the application memory or sandbox directory.
      cacheDownload.download(this.src, options);
      console.info(\`success to download the resource. \`);
    } catch (err) {
      console.error(\`Failed to download the resource: code: ${err.code}, message: ${err.message}\`);
    }
  }

  build() {
    Column() {
      // If src specifies an online image that has been successfully downloaded and cached, the image will be displayed without requiring re-downloading.
      Image(this.src)
        .width(100)
        .height(100)
        .objectFit(ImageFit.Cover)
        .borderWidth(1)
    }
    .height('100%')
    .width('100%')
  }
}

## Example 4: Adding Events to an Image

This example demonstrates how to add the [onClick](../../universal-events/interaction-response-events/click-event/document.md#onclick) and [onFinish](#onfinish) events to an image.

@Entry
@Component
struct ImageExample3 {
  // Replace $r('app.media.earth') with the image resource file you use.
  private imageOne: Resource = $r('app.media.earth');
  // Replace $r('app.media.star') with the image resource file you use.
  private imageTwo: Resource = $r('app.media.star');
  // Replace $r('app.media.moveStar') with the image resource file you use.
  private imageThree: Resource = $r('app.media.moveStar');
  @State src: Resource = this.imageOne;
  @State src2: Resource = this.imageThree;
  build(){
    Column(){
      // Add a click event so that a specific image is loaded upon clicking.
      Image(this.src)
        .width(100)
        .height(100)
        .onClick(() => {
          this.src = this.imageTwo;
        })

      // When the image to be loaded is in SVG format:
      Image(this.src2)
        .width(100)
        .height(100)
        .onFinish(() => {
          // Load another image when the SVG image has finished its animation.
          this.src2 = this.imageOne;
        })
    }.width('100%').height('100%')
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7e/v3/sc0usJwJRQ-ybfVnp3lGWQ/en-us_image_0000002537765710.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062243Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=563CD275553A0C9A7A0E09348B74C55BBCB79E1D0745A6B18D7CF078E5C90C06)

## Example 5: Enabling the AI Image Analyzer

This example shows how to enable the AI image analyzer using the [enableAnalyzer](#enableanalyzer11) API.

import { image } from '@kit.ImageKit'

@Entry
@Component
struct ImageExample4 {
  @State imagePixelMap: image.PixelMap | undefined = undefined
  private aiController: ImageAnalyzerController = new ImageAnalyzerController()
  private options: ImageAIOptions = {
    types: \[ImageAnalyzerType.SUBJECT, ImageAnalyzerType.TEXT\],
    aiController: this.aiController
  }

  async aboutToAppear() {
    this.imagePixelMap = await this.getPixmapFromMedia($r('app.media.img'))
  }

  build() {
    Column() {
      Image(this.imagePixelMap, this.options)
        .enableAnalyzer(true)
        .objectFit(ImageFit.Contain)
        .width(200)
        .height(300)
        .margin({left: 10})
      Button('getTypes')
        .onClick(() => {
          this.aiController.getImageAnalyzerSupportTypes()
        })
    }
  }
  private async getPixmapFromMedia(resource: Resource) {
    let unit8Array = await this.getUIContext().getHostContext()?.resourceManager?.getMediaContent({
      bundleName: resource.bundleName,
      moduleName: resource.moduleName,
      id: resource.id
    })
    let imageSource = image.createImageSource(unit8Array?.buffer.slice(0, unit8Array.buffer.byteLength))
    let createPixelMap: image.PixelMap = await imageSource.createPixelMap({
      desiredPixelFormat: image.PixelMapFormat.RGBA\_8888
    })
    await imageSource.release()
    return createPixelMap
  }
}

## Example 6: Stretching an Image Using slice

This example demonstrates how to stretch an image in different directions using the **slice** option of the [resizable](#resizable11) attribute.

@Entry
@Component
struct Index {
  @State top: number = 10;
  @State bottom: number = 10;
  @State left: number = 10;
  @State right: number = 10;

  build() {
    Column({ space: 5 }) {
      // Original image effect
      // Replace $r('app.media.landscape') with the image resource file you use.
      Image($r('app.media.landscape'))
        .width(200).height(200)
        .border({ width: 2, color: Color.Pink })
        .objectFit(ImageFit.Contain)

      // Set the resizable attribute to stretch the image in different directions.
      // Replace $r('app.media.landscape') with the image resource file you use.
      Image($r('app.media.landscape'))
        .resizable({
          slice: {
            // When a number is passed in, it uses the default vp unit, which is parsed into different px sizes on different devices. Choose the unit based on your needs.
            left: \`${this.left}px\`,
            right: \`${this.right}px\`,
            top: \`${this.top}px\`,
            bottom: \`${this.bottom}px\`
          }
        })
        .width(200)
        .height(200)
        .border({ width: 2, color: Color.Pink })
        .objectFit(ImageFit.Contain)

      Row() {
        Button('add top to ' + this.top).fontSize(10)
          .onClick(() => {
            this.top += 10;
          })
        Button('add bottom to ' + this.bottom).fontSize(10)
          .onClick(() => {
            this.bottom += 10;
          })
      }

      Row() {
        Button('add left to ' + this.left).fontSize(10)
          .onClick(() => {
            this.left += 10;
          })
        Button('add right to ' + this.right).fontSize(10)
          .onClick(() => {
            this.right += 10;
          })
      }

    }
    .justifyContent(FlexAlign.Start).width('100%').height('100%')
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bc/v3/iK1KKtjITPehBl-HTHwDtg/en-us_image_0000002537925650.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062243Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=F90F81DFCC8D3E9C4CC202955BCCC944A93B86EA7755E11A224C7C309BE631C6)

## Example 7: Stretching an Image Using lattice

This example demonstrates how to stretch an image using the **lattice** option of the [resizable](#resizable11) attribute with a rectangular lattice object.

import { drawing } from '@kit.ArkGraphics2D';

@Entry
@Component
struct drawingLatticeTest {
  private xDivs: Array<number> = \[1, 2, 200\];
  private yDivs: Array<number> = \[1, 2, 200\];
  private fXCount: number = 3;
  private fYCount: number = 3;
  private drawingLatticeFirst: DrawingLattice =
    drawing.Lattice.createImageLattice(this.xDivs, this.yDivs, this.fXCount, this.fYCount);

  build() {
    Scroll() {
      Column({ space: 10 }) {
        Text('Original Image').fontSize(20).fontWeight(700)
        Column({ space: 10 }) {
          // Replace $r('app.media.mountain') with the image resource file you use.
          Image($r('app.media.mountain'))
            .width(260).height(260)
        }.width('100%')

        Text('Resize by lattice').fontSize(20).fontWeight(700)
        Column({ space: 10 }) {
          // Replace $r('app.media.mountain') with the image resource file you use.
          Image($r('app.media.mountain'))
            .objectRepeat(ImageRepeat.X)
            .width(260)
            .height(260)
            .resizable({
              lattice: this.drawingLatticeFirst
            })
        }.width('100%')
      }.width('100%')
    }
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/38/v3/dxBeX2WqTK6BHcxhNsNfeg/en-us_image_0000002568685427.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062243Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=BA17FD9D4E0E4871D32E90508F98703FED7B38AD32F2EF2879E1C9D93A7C27A7)

## Example 8: Playing a PixelMap Array Animation

This example demonstrates how to play an animation using a **PixelMap** array through an [AnimatedDrawableDescriptor](../../../arkts-api/ui/ohos-arkui-drawabledescriptor-drawabledescriptor/document.md#animateddrawabledescriptor12) object.

import { AnimationOptions, AnimatedDrawableDescriptor } from '@kit.ArkUI';
import { image } from '@kit.ImageKit';

@Entry
@Component
struct ImageExample {
  pixelMaps: PixelMap\[\] = \[\];
  @State options: AnimationOptions = { iterations: 1 };
  @State animated: AnimatedDrawableDescriptor | undefined = undefined;

  async aboutToAppear() {
    this.pixelMaps = await this.getPixelMaps();
    this.animated = new AnimatedDrawableDescriptor(this.pixelMaps, this.options);
  }

  build() {
    Column() {
      Row() {
        Image(this.animated)
          .width('500px').height('500px')
          .onFinish(() => {
            console.info('finish');
          })
      }.height('50%')

      Row() {
        Button('once').width(100).padding(5).onClick(() => {
          this.options = { iterations: 1 };
          this.animated = new AnimatedDrawableDescriptor(this.pixelMaps, this.options);
        }).margin(5)
        Button('infinite').width(100).padding(5).onClick(() => {
          this.options = { iterations: -1 };
          this.animated = new AnimatedDrawableDescriptor(this.pixelMaps, this.options);
        }).margin(5)
      }
    }.width('50%')
  }

  private async getPixmapListFromMedia(resource: Resource) {
    let unit8Array = await this.getUIContext().getHostContext()?.resourceManager?.getMediaContent(resource.id);
    let imageSource = image.createImageSource(unit8Array?.buffer.slice(0, unit8Array.buffer.byteLength));
    let createPixelMap: image.PixelMap\[\] = await imageSource.createPixelMapList({
      desiredPixelFormat: image.PixelMapFormat.RGBA\_8888
    });
    await imageSource.release();
    return createPixelMap;
  }

  private async getPixmapFromMedia(resource: Resource) {
    let unit8Array = await this.getUIContext().getHostContext()?.resourceManager?.getMediaContent(resource.id);
    let imageSource = image.createImageSource(unit8Array?.buffer.slice(0, unit8Array.buffer.byteLength));
    let createPixelMap: image.PixelMap = await imageSource.createPixelMap({
      desiredPixelFormat: image.PixelMapFormat.RGBA\_8888
    });
    await imageSource.release();
    return createPixelMap;
  }

  private async getPixelMaps() {
    // Replace $r('app.media.mountain') with the image resource file you use.
    let myPixelMaps: PixelMap\[\] = await this.getPixmapListFromMedia($r('app.media.mountain')); // Add the image.
    // Replace $r('app.media.sky') with the image resource file you use.
    myPixelMaps.push(await this.getPixmapFromMedia($r('app.media.sky')));
    // Replace $r('app.media.clouds') with the image resource file you use.
    myPixelMaps.push(await this.getPixmapFromMedia($r('app.media.clouds')));
    // Replace $r('app.media.landscape') with the image resource file you use.
    myPixelMaps.push(await this.getPixmapFromMedia($r('app.media.landscape')));
    return myPixelMaps;
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/44/v3/yJDG6HJmTYW9SRmjkziRgg/en-us_image_0000002568765437.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062243Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=6C6030C466A558F2AA3BE5070EA3D943089650013CEC6B4139894B331B4B464F)

## Example 9: Setting a Color Filter for an Image

This example shows how to set a color filter for an image using the [colorFilter](#colorfilter9) attribute.

import { drawing, common2D } from '@kit.ArkGraphics2D';

@Entry
@Component
struct ImageExample3 {
  // When the image to be loaded is in SVG format:
  // Replace $r('app.media.svg1') with the image resource file you use.
  private imageOne: Resource = $r('app.media.svg1');
  // Replace $r('app.media.1') with the image resource file you use.
  private imageTwo: Resource = $r('app.media.1');
  @State src: Resource = this.imageOne;
  @State src2: Resource = this.imageTwo;
  private colorFilterMatrix: number\[\] = \[1, 0, 0, 0, 0.5,
                                         0, 1, 0, 0, 0,
                                         0, 0, 1, 0, 0,
                                         0, 0, 0, 1, 0\];
  private color: common2D.Color = {
    alpha: 255,
    red: 255,
    green: 0,
    blue: 0
  };
  @State drawingColorFilterFirst: ColorFilter | undefined = undefined;
  @State drawingColorFilterSecond: ColorFilter | undefined = undefined;
  @State drawingColorFilterThird: ColorFilter | undefined = undefined;

  build() {
    Column() {
      Image(this.src)
        .width(100)
        .height(100)
        .colorFilter(this.drawingColorFilterFirst)
        .onClick(()=>{
          this.drawingColorFilterFirst =
            drawing.ColorFilter.createBlendModeColorFilter(this.color, drawing.BlendMode.SRC\_IN);
        })

      Image(this.src2)
        .width(100)
        .height(100)
        .colorFilter(this.drawingColorFilterSecond)
        .onClick(()=>{
          this.drawingColorFilterSecond = new ColorFilter(this.colorFilterMatrix);
        })

      // When the image to be loaded is in SVG format:
      // Replace $r('app.media.svg2') with the image resource file you use.
      Image($r('app.media.svg2'))
        .width(110)
        .height(110)
        .margin(15)
        .colorFilter(this.drawingColorFilterThird)
        .onClick(()=>{
          this.drawingColorFilterThird =
            drawing.ColorFilter.createBlendModeColorFilter(this.color, drawing.BlendMode.SRC\_IN);
        })
    }
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/47/v3/8_kr2r5STLK7B3Sbg2pdiA/en-us_image_0000002537765712.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062243Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=44BDEA39BBA9E9BC2D8A1FAAF5E6D17FB0F795C0BD0F40034EA6853C871133B1)

## Example 10: Setting the Fill Effect for an Image

This example shows how to use the [objectFit](#objectfit) attribute to specify how an image is resized to fit its container.

@Entry
@Component
struct ImageExample{
  build() {
    Column() {
      Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Start }) {
        Row() {
          // Load a PNG image.
          // Replace $r('app.media.sky') with the image resource file you use.
          Image($r('app.media.sky'))
            .width(110).height(110).margin(15)
            .overlay('png', { align: Alignment.Bottom, offset: { x: 0, y: 20 } })
            .border({ width: 2, color: Color.Pink })
            .objectFit(ImageFit.TOP\_START)
          // Load a GIF image.
          // Replace $r('app.media.loading') with the image resource file you use.
          Image($r('app.media.loading'))
            .width(110).height(110).margin(15)
            .overlay('gif', { align: Alignment.Bottom, offset: { x: 0, y: 20 } })
            .border({ width: 2, color: Color.Pink })
            .objectFit(ImageFit.BOTTOM\_START)
        }
        Row() {
          // Load an SVG image.
          // Replace $r('app.media.svg') with the image resource file you use.
          Image($r('app.media.svg'))
            .width(110).height(110).margin(15)
            .overlay('svg', { align: Alignment.Bottom, offset: { x: 0, y: 20 } })
            .border({ width: 2, color: Color.Pink })
            .objectFit(ImageFit.TOP\_END)
          // Load a JPG image.
          // Replace $r('app.media.jpg') with the image resource file you use.
          Image($r('app.media.jpg'))
            .width(110).height(110).margin(15)
            .overlay('jpg', { align: Alignment.Bottom, offset: { x: 0, y: 20 } })
            .border({ width: 2, color: Color.Pink })
            .objectFit(ImageFit.CENTER)
        }
      }
    }.height(320).width(360).padding({ right: 10, top: 10 })
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cc/v3/kK0Ug0g0TJCE8p0TDmdgLA/en-us_image_0000002537925652.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062243Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=D0B1B5D72714021FB529502ED2201628EA3943253904DAD1BBD1006CE41D8725)

## Example 11: Switching Between Different Types of Images

This example demonstrates the effect of displaying images with [ResourceStr](../../common-definitions/basic-types/document.md#resourcestr) and [ImageContent](#imagecontent12) as types of data sources.

@Entry
@Component
struct ImageContentExample {
  @State imageSrcIndex: number = 0;
  // Replace $r('app.media.app\_icon') with the image resource file you use.
  @State imageSrcList: (ResourceStr | ImageContent)\[\] = \[$r('app.media.app\_icon'), ImageContent.EMPTY\];

  build() {
    Column({ space: 10 }) {
      Image(this.imageSrcList\[this.imageSrcIndex\])
        .width(100)
        .height(100)
      Button('Change Image src', { type: ButtonType.Capsule, stateEffect: false })
        .height(50)
        .onClick(() => {
          this.imageSrcIndex = (this.imageSrcIndex + 1) % this.imageSrcList.length;
        })
    }.width('100%')
    .padding(20)
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fe/v3/VjRklbhUQ0WbMUoIiAdpSQ/en-us_image_0000002568685429.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062243Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=F3A0CB803A44C9FAD7EFA276E32C8340A6D447ABEA2F70C71538ADD8F5DB4436)

## Example 12: Securing Sensitive Information

This example shows how to secure sensitive information on widgets using the [privacySensitive](#privacysensitive12) attribute. The display requires widget framework support.

@Entry
@Component
struct ImageExample {
  build() {
    Column({ space: 10 }) {
      // Replace $r('app.media.startIcon') with the image resource file you use.
      Image($r('app.media.startIcon'))
        .width(50)
        .height(50)
        .margin({top :30})
        .privacySensitive(true)
    }
    .alignItems(HorizontalAlign.Center)
    .width('100%')
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6d/v3/B3Q1m8WBQtuFzryUhlSHLQ/en-us_image_0000002568765439.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062243Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=350DBD02948C6B167E8B74A25340789210BC52F4ADD5D3E325EA2C5565DD0843)

## Example 13: Setting the Scan Effect for an Image

This example shows how to enable the scan effect for an image using [linearGradient](../../information-display/datapanel/document.md#lineargradient10) and [animateTo()](../../../arkts-api/ui/ohos-arkui-uicontext-uicontext/class-uicontext/document.md#animateto).

import { curves } from '@kit.ArkUI';

@Entry
@Component
struct ImageExample11 {
  private curve = curves.cubicBezierCurve(0.33, 0, 0.67, 1);
  @State moveImg: string\[\] = \['imageScanEffect'\];
  @State moveImgVisible: Visibility = Visibility.Visible;
  @State durationTime: number = 1500;
  @State iterationsTimes: number = -1;
  @State private opacityValue: number = 0.5;
  @State imageWidth: number = 450;
  @State visible: Visibility = Visibility.Hidden;
  @State stackBackgroundColor: string = '#E1E4E9';
  @State linePositionX: number = 0 - this.imageWidth;
  @State linePositionY: number = 0;
  @State imgResource: Resource | undefined = undefined;

  startupAnimate() {
    this.moveImg.pop();
    this.moveImg.push('imageScanEffect');
    setTimeout(() => {
      // Replace $r('app.media.img') with the image resource file you use.
      this.imgResource = $r('app.media.img');
    }, 3000);
    this.getUIContext()?.animateTo({
      duration: this.durationTime,
      curve: this.curve,
      tempo: 1,
      iterations: this.iterationsTimes,
      delay: 0
    }, () => {
      this.linePositionX = this.imageWidth;
    })
  }

  build() {
    Column() {
      Row() {
        Stack() {
          Image(this.imgResource)
            .width(this.imageWidth)
            .height(200)
            .objectFit(ImageFit.Contain)
            .visibility(this.visible)
            .onComplete(() => {
              this.visible = Visibility.Visible;
              this.moveImg.pop();
            })
            .onError(() =>{
              setTimeout(() => {
                this.visible = Visibility.Visible;
                this.moveImg.pop();
              }, 2600)
            })
          ForEach(this.moveImg, (item: string) => {
            Row()
              .width(this.imageWidth)
              .height(200)
              .visibility(this.moveImgVisible)
              .position({ x: this.linePositionX, y: this.linePositionY })
              .linearGradient({
                direction: GradientDirection.Right,
                repeating: false,
                colors: \[\[0xE1E4E9, 0\], \[0xFFFFFF, 0.75\], \[0xE1E4E9, 1\]\]
              })
              .opacity(this.opacityValue)
          })
        }
        .backgroundColor(this.visible ? this.stackBackgroundColor : undefined)
        .margin({top: 20, left: 20, right: 20})
        .borderRadius(20)
        .clip(true)
        .onAppear(() => {
          this.startupAnimate();
        })
      }
    }
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/67/v3/3o4oHecKSQyLWXqixnvOug/en-us_image_0000002537765714.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062243Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=34A04F582B0B78249A492A85B064267E4AC08F761BD92E8C3C9DFCE0B71C3A6B)

## Example 14: Adding Transform Effects to an Image

This example demonstrates how to apply rotation and translation effects to an image using the [imageMatrix](#imagematrix15) and [objectFit](#objectfit) attributes.

The **imageMatrix** attribute is added since API version 15.

import { matrix4 } from '@kit.ArkUI';

@Entry
@Component
struct Test {
  private matrix1 = matrix4.identity()
    .translate({ x: -400, y: -750 })
    .scale({ x: 0.5, y: 0.5 })
    .rotate({
      x: 2,
      y: 0.5,
      z: 3,
      centerX: 10,
      centerY: 10,
      angle: -10
    })

  build() {
    Row() {
      Column({ space: 50 }) {
        Column({ space: 5 }) {
          // Replace $r('app.media.example') with the image resource file you use.
          Image($r('app.media.example'))
            .border({ width:2, color: Color.Black })
            .objectFit(ImageFit.Contain)
            .width(150)
            .height(150)
          Text('No transformation')
            .fontSize('25px')
        }
        Column({ space: 5 }) {
          // Replace $r('app.media.example') with the image resource file you use.
          Image($r('app.media.example'))
            .border({ width:2, color: Color.Black })
            .objectFit(ImageFit.None)
            .translate({ x: 10, y: 10 })
            .scale({ x: 0.5, y: 0.5 })
            .width(100)
            .height(100)
          Text('Direct transformation on the image, with the upper left corner of the image source displayed by default')
            .fontSize('25px')
        }
        Column({ space: 5 }) {
          // Replace $r('app.media.example') with the image resource file you use.
          Image($r('app.media.example'))
            .objectFit(ImageFit.MATRIX)
            .imageMatrix(this.matrix1)
            .border({ width:2, color: Color.Black })
            .width(150)
            .height(150)
          Text('Transformation using imageMatrix to adjust the source position for optimal display')
            .fontSize('25px')
        }
      }
      .width('100%')
    }
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8e/v3/73-If6ZgSt6NMTzX51I9rA/en-us_image_0000002537925654.jpeg?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062243Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=0327180F145909D5FEA8D9DA7862487D6DF6D6BACF374FDE71DA30446F66DFAA)

## Example 15: Setting the Image Decoding Size Using sourceSize

This example uses the [sourceSize](#sourcesize) API to customize the image decoding size.

@Entry
@Component
struct Index {
  @State borderRadiusValue: number = 10;
  build() {
    Column() {
      // Replace $r('app.media.sky') with the image resource file you use.
      Image($r('app.media.sky'))
        .sourceSize({width:1393, height:1080})
        .height(300)
        .width(300)
        .objectFit(ImageFit.Contain)
        .borderWidth(1)
      // Replace $r('app.media.sky') with the image resource file you use.
      Image($r('app.media.sky'))
        .sourceSize({width:13, height:10})
        .height(300)
        .width(300)
        .objectFit(ImageFit.Contain)
        .borderWidth(1)
    }
    .height('100%')
    .width('100%')
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bd/v3/01MyZOVdRl-TF5K-1_dnNQ/en-us_image_0000002568685431.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062243Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=ECDD363EBDC8A6D1F305D07E73AD34C26224197176C40F1338C58B5E8EDE4D35)

## Example 16: Setting the Image Rendering Mode Using renderMode

This example uses the [renderMode](#rendermode) API to set the image rendering mode to grayscale.

@Entry
@Component
struct Index {
  @State borderRadiusValue: number = 10;
  build() {
    Column() {
      // Replace $r('app.media.sky') with the image resource file you use.
      Image($r('app.media.sky'))
        .renderMode(ImageRenderMode.Template)
        .height(300)
        .width(300)
        .objectFit(ImageFit.Contain)
        .borderWidth(1)
    }
    .height('100%')
    .width('100%')
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/81/v3/soq7U4msSTWGiTEtlib41Q/en-us_image_0000002568765441.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062243Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=0F8F83DBB3810979767560289D1FBABF23BA377CB80EB8D7A3A1C68948F1FC1F)

## Example 17: Setting the Image Repeat Pattern Using objectRepeat

This example uses the [objectRepeat](#objectrepeat) API to repeat the image along the vertical axis.

@Entry
@Component
struct Index {
  @State borderRadiusValue: number = 10;
  build() {
    Column() {
      // Replace $r('app.media.sky') with the image resource file you use.
      Image($r('app.media.sky'))
        .objectRepeat(ImageRepeat.Y)
        .height('90%')
        .width('90%')
        .objectFit(ImageFit.Contain)
        .borderWidth(1)
    }
    .height('100%')
    .width('100%')
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4c/v3/mcBR_6fwS7GoTcM6FXjavg/en-us_image_0000002537765716.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062243Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=37489461E371A290B258C00BE6ABAFA4AC6B3C091787EC6D297E0EEA8FA9550C)

## Example 18: Setting the Fill Color for an SVG Image

This example shows how to set different fill colors for an SVG image using the [fillColor](#fillcolor15) attribute.

@Entry
@Component
struct Index {
  build() {
    Column() {
      Text('FillColor not set')
      // Replace $r('app.media.svgExample') with the image resource file you use.
      Image($r('app.media.svgExample'))
        .height(100)
        .width(100)
        .objectFit(ImageFit.Contain)
        .borderWidth(1)
      Text('fillColor set to ColorContent.ORIGIN')
      // Replace $r('app.media.svgExample') with the image resource file you use.
      Image($r('app.media.svgExample'))
        .height(100)
        .width(100)
        .objectFit(ImageFit.Contain)
        .borderWidth(1)
        .fillColor(ColorContent.ORIGIN)
      Text('fillColor set to Color.Blue')
      // Replace $r('app.media.svgExample') with the image resource file you use.
      Image($r('app.media.svgExample'))
        .height(100)
        .width(100)
        .objectFit(ImageFit.Contain)
        .borderWidth(1)
        .fillColor(Color.Blue)
      Text('fillColor set to undefined')
      // Replace $r('app.media.svgExample') with the image resource file you use.
      Image($r('app.media.svgExample'))
        .height(100)
        .width(100)
        .objectFit(ImageFit.Contain)
        .borderWidth(1)
        .fillColor(undefined)
    }
    .height('100%')
    .width('100%')
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0/v3/10FzNMDkStOXF3WFzNvmKA/en-us_image_0000002537925656.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062243Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=70C3956899C61374092E7DDF80126BFA58A20E647CCDB6DE844C2771AA12C829)

## Example 19: Adjusting HDR Image Brightness

This example demonstrates how to adjust the HDR image brightness using the [hdrBrightness](#hdrbrightness19) attribute, changing the value from **0** to **1**.

The **hdrBrightness** attribute is added since API version 19.

import { image } from '@kit.ImageKit';

const TAG = 'AceImage';

@Entry
@Component
struct Index {
  // Replace 'img\_1' with the image resource file you use.
  @State imgUrl: string = 'img\_1';
  @State bright: number = 0; // The default brightness is 0.
  aboutToAppear(): void {
    // Obtain media resources from the resource manager.
    let img = this.getUIContext().getHostContext()?.resourceManager.getMediaByNameSync(this.imgUrl);
    // Create an image source and obtain image information.
    if (img && img.buffer) {
      let imageSource = image.createImageSource(img?.buffer.slice(0));
      let imageInfo = imageSource.getImageInfoSync();
      // Check whether the image information is obtained successfully.
      if (imageInfo == undefined) {
        console.error(TAG, 'Failed to obtain the image information.');
      } else {
        // After the image information is obtained successfully, print the HDR status.
        console.info(TAG, 'imageInfo.isHdr:' + imageInfo.isHdr);
      }
    } else {
      console.error(TAG, 'Failed to obtain the image buffer.');
    }
  }

  build() {
    Column() {
      // Replace $r('app.media.img\_1') with the image resource file you use.
      Image($r('app.media.img\_1')).width('50%')
        .height('auto')
        .margin({ top: 160 })
        .hdrBrightness(this.bright) // Set the HDR image brightness controlled by the bright state.
      Button('Adjust Brightness 0 -> 1')
        .onClick(() => {
          // Animation transition for brightness changes
          this.getUIContext()?.animateTo({}, () => {
            this.bright = 1.0 - this.bright;
          });
        })
    }
    .height('100%')
    .width('100%')
  }
}

## Example 20: Setting Whether the Image Follows the System Language Direction

This example shows how to use the [matchTextDirection](#matchtextdirection) API to set whether the image should be mirrored when the device system language is set to Uyghur.

@Entry
@Component
struct Index {
  build() {
    Column() {
      Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Start }) {
        Row() {
          // The image does not follow the system language direction.
          // Replace $r('app.media.ocean') with the image resource file you use.
          Image($r('app.media.ocean'))
            .width(110).height(110).margin(15)
            .matchTextDirection(false)
        }
        Row() {
          // The image follows the system language direction.
          // Replace $r('app.media.ocean') with the image resource file you use.
          Image($r('app.media.ocean'))
            .width(110).height(110).margin(15)
            .matchTextDirection(true)
        }
      }
    }.height(320).width(360).padding({ right: 10, top: 10 })
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/14/v3/4vrjUZ0YTwSatu5SbA29qg/en-us_image_0000002568685433.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062243Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=5DF7F20F1662DD5ED908B1C4813AD26965FA341FC765D4ED625D8478B9BB2194)

## Example 21: Setting Image Display Orientation

This example shows how to configure different image display orientations using the [orientation](#orientation14) attribute.

@Entry
@Component
struct OrientationExample {
  build() {
    Column() {
      Row({ space: 25 }) {
        Column() {
          Text('AUTO')
          // Replace $r('app.media.hello') with the image resource file you use.
          Image($r('app.media.hello'))
            .width(125).height(125)
            .orientation(ImageRotateOrientation.AUTO)
        }

        Column() {
          Text('UP')
          // Replace $r('app.media.hello') with the image resource file you use.
          Image($r('app.media.hello'))
            .width(125).height(125)
            .orientation(ImageRotateOrientation.UP)
        }

        Column() {
          Text('RIGHT')
          // Replace $r('app.media.hello') with the image resource file you use.
          Image($r('app.media.hello'))
            .width(125).height(125)
            .orientation(ImageRotateOrientation.RIGHT)
        }
      }

      Row({ space: 25 }) {
        Column() {
          Text('DOWN')
          // Replace $r('app.media.hello') with the image resource file you use.
          Image($r('app.media.hello'))
            .width(125).height(125)
            .orientation(ImageRotateOrientation.DOWN)
        }

        Column() {
          Text('LEFT')
          // Replace $r('app.media.hello') with the image resource file you use.
          Image($r('app.media.hello'))
            .width(125).height(125)
            .orientation(ImageRotateOrientation.LEFT)
        }

        Column() {
          Text('UP\_MIRRORED')
          // Replace $r('app.media.hello') with the image resource file you use.
          Image($r('app.media.hello'))
            .width(125).height(125)
            .orientation(ImageRotateOrientation.UP\_MIRRORED)
        }
      }

      Row({ space: 15 }) {
        Column() {
          Text('RIGHT\_MIRRORED')
          // Replace $r('app.media.hello') with the image resource file you use.
          Image($r('app.media.hello'))
            .width(125).height(125)
            .orientation(ImageRotateOrientation.RIGHT\_MIRRORED)
        }

        Column() {
          Text('DOWN\_MIRRORED')
          // Replace $r('app.media.hello') with the image resource file you use.
          Image($r('app.media.hello'))
            .width(125).height(125)
            .orientation(ImageRotateOrientation.DOWN\_MIRRORED)
        }

        Column() {
          Text('LEFT\_MIRRORED')
          // Replace $r('app.media.hello') with the image resource file you use.
          Image($r('app.media.hello'))
            .width(125).height(125)
            .orientation(ImageRotateOrientation.LEFT\_MIRRORED)
        }
      }
    }
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a2/v3/Tapy8S7pQSu8A0F0BM2J0g/en-us_image_0000002568765443.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062243Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=DE8CE735F69DD23334DF15876A82B2B102EDE6D825D3B5ED2A8932B2BFE8994C)

## Example 22: Using EXIF Metadata for Image Display Orientation

This example demonstrates how to use the [getImageProperty](../../../../../media/image-kit/arkts-apis/ohos-multimedia-image-image-processing/interface-imagesource/document.md#getimageproperty11) API to obtain the EXIF metadata of an image, and then set the image display orientation through the [orientation](#orientation14) attribute based on the obtained EXIF metadata.

import { image } from '@kit.ImageKit';
import { resourceManager } from '@kit.LocalizationKit';

@Entry
@Component
struct Example {
  @State rotateOrientation: ImageRotateOrientation = ImageRotateOrientation.UP;
  @State pixelMap: image.PixelMap | undefined = undefined;
  @State text1: string = 'The exif orientation is ';
  @State text2: string = 'Set orientation to ';

  // Convert EXIF orientation information into ImageRotateOrientation.
  getOrientation(orientation: string): ImageRotateOrientation {
    if (orientation == 'Top-right') {
      this.text2 = this.text2 + 'UP\_MIRRORED';
      return ImageRotateOrientation.UP\_MIRRORED;
    } else if (orientation == 'Bottom-right') {
      this.text2 = this.text2 + 'DOWN';
      return ImageRotateOrientation.DOWN;
    } else if (orientation == 'Bottom-left') {
      this.text2 = this.text2 + 'DOWN\_MIRRORED';
      return ImageRotateOrientation.DOWN\_MIRRORED;
    } else if (orientation == 'Left-top') {
      this.text2 = this.text2 + 'LEFT\_MIRRORED';
      return ImageRotateOrientation.LEFT\_MIRRORED;
    } else if (orientation == 'Right-top') {
      this.text2 = this.text2 + 'RIGHT';
      return ImageRotateOrientation.RIGHT;
    } else if (orientation == 'Right-bottom') {
      this.text2 = this.text2 + 'RIGHT\_MIRRORED';
      return ImageRotateOrientation.RIGHT\_MIRRORED;
    } else if (orientation == 'Left-bottom') {
      this.text2 = this.text2 + 'LEFT';
      return ImageRotateOrientation.LEFT;
    } else if (orientation == 'Top-left') {
      this.text2 = this.text2 + 'UP';
      return ImageRotateOrientation.UP;
    } else {
      this.text2 = this.text2 + 'UP';
      return ImageRotateOrientation.UP;
    }
  }

  async getFileBuffer(context: Context): Promise<ArrayBuffer | undefined> {
    try {
      const resourceMgr: resourceManager.ResourceManager = context.resourceManager;
      // Obtain the content of the resource file with EXIF data as Uint8Array.
      // Replace 'hello.jpg' with the image resource file you use.
      const fileData: Uint8Array = await resourceMgr.getRawFileContent('hello.jpg');
      console.info('Successfully get RawFileContent');
      // Convert the array to an ArrayBuffer and return the ArrayBuffer.
      const buffer: ArrayBuffer = fileData.buffer.slice(0);
      return buffer;
    } catch (error) {
      console.error('Failed to get RawFileContent');
      return undefined;
    }
  }

  aboutToAppear() {
    let context = this.getUIContext().getHostContext();
    if (!context) {
      return;
    }
    this.getFileBuffer(context).then((buf: ArrayBuffer | undefined) => {
      let imageSource = image.createImageSource(buf);
      if (!imageSource) {
        return;
      }
      // Obtain EXIF orientation information.
      imageSource.getImageProperty(image.PropertyKey.ORIENTATION).then((orientation) => {
        this.rotateOrientation = this.getOrientation(orientation);
        this.text1 = this.text1 + orientation;
        let options: image.DecodingOptions = {
          'editable': true,
          'desiredPixelFormat': image.PixelMapFormat.RGBA\_8888,
        }
        imageSource.createPixelMap(options).then((pixelMap: image.PixelMap) => {
          this.pixelMap = pixelMap;
          imageSource.release();
        });
      }).catch(() => {
        imageSource.release();
      });
    })
  }

  build() {
    Column({ space: 40 }) {
      Column({ space: 10 }) {
        Text('before').fontSize(20).fontWeight(700)
        // Replace 'hello.jpg' with the image resource file you use.
        Image($rawfile('hello.jpg'))
          .width(100)
          .height(100)
        Text(this.text1)
      }

      Column({ space: 10 }) {
        Text('after').fontSize(20).fontWeight(700)
        Image(this.pixelMap)
          .width(100)
          .height(100)
          .orientation(this.rotateOrientation)
        Text(this.text2)
      }
    }
    .height('80%')
    .width('100%')
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/32/v3/yAxPPT39RH-MUOPbjR6nkQ/en-us_image_0000002537765718.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062243Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=CFE37EE9F03AB1E1A6219F4E728C5F591FE31B4EF5A252366F2BA6EB7407B99D)

## Example 23: Dynamically Switching an SVG Image Between Fill Colors

This example demonstrates how to dynamically switch an SVG Image between fill colors across different color spaces using [ColorMetrics](../../../arkts-api/ui/arkui/graphics/document.md#colormetrics12).

import { ColorMetrics } from '@kit.ArkUI';
@Entry
@Component
struct fillColorMetricsDemo {
  @State p3Red: ColorMetrics = ColorMetrics.colorWithSpace(ColorSpace.DISPLAY\_P3, 0.631, 0.0392, 0.1294);
  @State sRGBRed: ColorMetrics = ColorMetrics.colorWithSpace(ColorSpace.SRGB, 0.631, 0.0392, 0.1294);
  @State p3Green: ColorMetrics = ColorMetrics.colorWithSpace(ColorSpace.DISPLAY\_P3, 0.09, 0.662 ,0.552);
  @State sRGBGreen: ColorMetrics = ColorMetrics.colorWithSpace(ColorSpace.SRGB, 0.09, 0.662 ,0.552);
  @State p3Blue: ColorMetrics = ColorMetrics.colorWithSpace(ColorSpace.DISPLAY\_P3, 0, 0.290 ,0.686);
  @State sRGBBlue: ColorMetrics = ColorMetrics.colorWithSpace(ColorSpace.SRGB, 0, 0.290 ,0.686);
  @State colorArray: (Color|undefined|ColorMetrics|ColorContent)\[\] = \[
    this.p3Red, this.sRGBRed, this.p3Green, this.sRGBGreen, this.p3Blue,
    this.sRGBBlue, ColorContent.ORIGIN, Color.Gray, undefined
  \]
  @State colorArrayStr: string\[\] = \[
    'P3 Red', 'SRGB Red', 'P3 Green', 'SRGB Green',
    'P3 Blue', 'SRGB Blue', 'ORIGIN', 'Gray', 'undefined'
  \]
  @State arrayIdx: number = 0
  build() {
    Column() {
      Text('FillColor is ' + this.colorArrayStr\[this.arrayIdx\])
      // Replace $r('app.media.svgExample') with the image resource file you use.
      Image($r('app.media.svgExample'))
        .width(110).height(110).margin(15)
        .fillColor(this.colorArray\[this.arrayIdx\])
      Button('ChangeFillColor')
        .onClick(()=>{
          this.arrayIdx = (this.arrayIdx + 1) % this.colorArray.length
        })
      Blank().height(30).width('100%')
      Text('FillColor is SRGB Red')
      // Replace $r('app.media.svgExample') with the image resource file you use.
      Image($r('app.media.svgExample'))
        .width(110).height(110).margin(15)
        .fillColor(this.sRGBRed)
      Blank().height(30).width('100%')
      Text('FillColor is SRGB Green')
      // Replace $r('app.media.svgExample') with the image resource file you use.
      Image($r('app.media.svgExample'))
        .width(110).height(110).margin(15)
        .fillColor(this.sRGBGreen)
      Blank().height(30).width('100%')
      Text('FillColor is SRGB Blue')
      // Replace $r('app.media.svgExample') with the image resource file you use.
      Image($r('app.media.svgExample'))
        .width(110).height(110).margin(15)
        .fillColor(this.sRGBBlue)
    }
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d2/v3/Y0FSeinlTtat9OJYodKO6Q/en-us_image_0000002537925658.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062243Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=322429614FA8B13329FA430D93850E4FC9B8034415A0D7061BCA27D2E96B7102)

## Example 24: Displaying an Image Using an Application Sandbox Path

This example demonstrates how to display an image using the application sandbox path, where a preloaded image named **cloud.png** is placed in the **haps/entry/files** directory of the current application.

import { fileUri } from '@kit.CoreFileKit';

@Entry
@Component
struct Index {
  private getSandBoxUri(): string {
    let context = this.getUIContext().getHostContext();
    if (!context) {
      return '';
    }
    // /data/storage/el2/base/haps/entry/files/cloud.png
    // Obtain the URI from the file path in the application sandbox.
    // Replace '/cloud.png' with the image resource file you use.
    return fileUri.getUriFromPath(context.filesDir + '/cloud.png');
  }

  build() {
    Column() {
      Image(this.getSandBoxUri())
        .width(150)
        .height(150)
    }
    .height('100%')
    .width('100%')
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/39/v3/GLMu-ZXIQKGe1FIg1DNnWg/en-us_image_0000002568685435.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062243Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=310D713AD9FFA96FA875742BC4147836327578B35B6F27E786B731A3A7AB1E59)

## Example 25: Displaying an Image Using a Relative Path

This example demonstrates how to display an image using a relative path. First, create a common directory at the same level as the project's **pages** directory. Then, place a preloaded image named **cloud1.png** in the **common** directory and display it using the relative path.

@Entry
@Component
struct Index {
  build() {
    Column({ space: 10 }) {
      Image('common/cloud1.png')
        .width(100)
        .height(100)
    }
    .height('100%')
    .width('100%')
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4f/v3/Mr91FEC4S2WDlSov-CQ3QA/en-us_image_0000002568685435.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062243Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=D1BC36D44435F8EE13A3E14192042B864ADF60D9F7954118FB76223807CB5B6D)

## Example 26: Displaying an SVG Image Using supportSvg2

In this example, the [supportSvg2](#supportsvg221) attribute is set to enable the enhanced SVG tag parsing feature.

The **supportSvg2** attribute is added since API version 21.

@Entry
@Component
struct Index {
  build() {
    Row() {
      Column() {
        Text('supportSvg2 is set to true.')
        // Replace $rawfile('image.svg') with the image resource file you use.
        Image($rawfile('image.svg'))
          .width(200)
          .height(200)
          .border({ width: 2, color: 'red' })
          .supportSvg2(true)
          .margin({ bottom: 30 })
        Text('supportSvg2 is set to false (default value).')
        // Replace $rawfile('image.svg') with the image resource file you use.
        Image($rawfile('image.svg'))
          .width(200)
          .height(200)
          .border({ width: 2, color: 'red' })
      }
      .width('100%')
    }
    .height('100%')
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7e/v3/wuMyiLTXQ8SfTXXprMrI2w/en-us_image_0000002568765445.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062243Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=9956C74E54620C1A208A4C4047327D05C036E5F12C8C5EF580DDA7D96D6EE907)

## Example 27: Implementing Fade-in/Fade-out Transition Effects for Images Using ContentTransition

This example demonstrates how to use the [contentTransition](#contenttransition21) attribute to implement the fade-in/fade-out effect for smooth image transitions when the image source is switched on a click. This attribute is supported since API version 21.

@Entry
@Component
struct ImageExample {
  // Replace $r('app.media.icon') with the image resource file you use.
  @State imageResource: Resource = $r('app.media.icon');

  build() {
    Row() {
      Column() {
        Image(this.imageResource)
          .width(200)
          .height(200)
          // Enable the fade-in/fade-out transition effect.
          .contentTransition(ContentTransitionEffect.OPACITY)
          .onClick(() => {
            // Replace $r('app.media.cloud1') with the image resource file you use.
            this.imageResource = $r('app.media.cloud1')
          })
      }
      .width('100%')
    }
    .height('100%')
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d5/v3/GZ0XYWqRT8qadwszTsaNfg/en-us_image_0000002537765720.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062243Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=5D9A9080892CE32C99C496EE360FAC071EB26EA829180021B7232164B21ACD5F)

## Example 28: Setting Loading and Load-Failure Images Using alt

This example demonstrates how to display specified images during image loading and when image loading fails by setting the [alt](#alt22) attribute.

@Entry
@Component
struct ImageExample {
  build() {
      Column() {
      Text('Both placeholder and error attributes set')
      // Set an invalid URL to trigger the placeholder and error attributes of alt.
      Image("https://www.example.com/xxx.png")
      // Replace $r('app.media.startIcon') and $r('app.media.example') with the image resource file you use.
        .alt({ placeholder: $r('app.media.startIcon'), error: $r('app.media.example') })
        .width(100)
        .height(100)
        .margin(20)
      Text('Only placeholder attribute set')
      Image("https://www.example.com/xxx.png")
        .alt({ placeholder: $r('app.media.startIcon')})
        .width(100)
        .height(100)
        .margin(20)
      Text('Only error attribute set')
      Image("https://www.example.com/xxx.png")
        .alt({error: $r('app.media.example')})
        .width(100)
        .height(100)
        .margin(20)
      }
    .width('100%')
    .height('100%')
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e3/v3/UY8K7yluS12R4_7GQTekxw/en-us_image_0000002537925660.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062243Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=E5250544AA84F8C417EDD09F30BC4B92490388F4B4E8EDCFB8C5D609EFB6144E)
