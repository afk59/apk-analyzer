# image

The **<image>** component is used to render and display images.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1b/v3/-looeex5TyeHohXTiwlqrA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062301Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=7AF547518CB6773EF896D4C28C7F137C114FADFA9D454D8790E0494E61ECB4F0)

The APIs of this module are supported since API version 8. Updates will be marked with a superscript to indicate their earliest API version.

#### Child Components

Not supported

#### Attributes

In addition to the [universal attributes](../../universal-components/universal-attributes/document.md), the following attributes are supported.

| Name | Type | Default Value | Mandatory | Description |
| :-- | :-- | :-- | :-- | :-- |
| src | string | \- | No | 
Image path.

\- The local path is supported. Supported formats are as follows: PNG, JPG, BMP, SVG, and GIF.

\- The path to the in-memory image is also supported in the scheme format of **memory://**.

**NOTE**

To display an online image, download it and then access it with its in-memory path. Do not use URLs.

 |
| alt | string | \- | No | Placeholder image displayed during image loading. |

#### Styles

In addition to the [universal styles](../../universal-components/universal-styles/document.md), the following styles are supported.

| Name | Type | Default Value | Mandatory | Description |
| :-- | :-- | :-- | :-- | :-- |
| object-fit | string | cover | No | Image scale type. For details about available values, see **object-fit**. This style is not supported for SVG images. |
| match-text-direction | boolean | false | No | Whether image orientation changes with the text direction. This style is not supported for SVG images. |
| fit-original-size | boolean | false | No | Whether the **<image>** component adapts to the image source size when its width and height are not set. If this style is set to **true**, **object-fit** will not take effect. This style is not supported for SVG images. |

**Table 1** object-fit

| Type | Description |
| :-- | :-- |
| cover | The image is scaled with its aspect ratio retained for both sides to be greater than or equal to the display boundaries and displayed in the middle. |
| contain | The image is scaled with the aspect ratio retained for the image to be completely displayed within the display boundaries and displayed in the middle. |
| fill | The image is scaled to fill the display area, and its aspect ratio is not retained. |
| none | The image is displayed in the middle with its aspect ratio and size retained. |
| scale-down | The image is displayed in the middle with its aspect ratio retained, in the size equal to or smaller than the original size. |

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e9/v3/URzb8G48ShqwmZIJxjpE6w/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062301Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=FB7E41E898330A647377AAE4603D996AFFD55050E48165887C8621A30600D060)

When using an SVG image, note that:

-   The SVG image will not be drawn if the length or width of the parent component is infinity. Therefore, you are advised to set the length and width for the **<image>** component.
    
-   If the image length and width are not specified in the SVG description, the SVG image fills the **<image>** component area.
    
-   If the image length and width are specified in the SVG description, the following rules are adopted to decide the final display effect:
    
    -   If the **<image>** component is too small to afford the SVG image, the SVG image is cropped and only its upper left part is displayed in the component.
        
    -   If the **<image>** component is big enough to afford the SVG image, the SVG image is displayed in the upper left corner of the component.
        

#### Events

| Name | Parameter | Description |
| :-- | :-- | :-- |
| click | \- | Triggered when the component is clicked. |
| complete | \- | Triggered when the image is successfully loaded. |
| error | \- | Triggered when an exception occurs during image loading. |

#### Example

<!-- xxx.hml -->
<stack class="content">
    <image src="https://developer.huawei.com/common/bg3.jpg" class="img"></image>
</stack>

/\* xxx.css \*/
.img{
  object-fit: contain
}

**4 x 4 widget**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7a/v3/sq7ewM7URW-UWepGfk2bdw/en-us_image_0000002568766017.jpg?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062301Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=554529CFA81A86C0A219D73A540A88B535D0D9524538F6AA79B6EAAC639817EF)
