# Class (MediaQuery)

Provides different styles for different media types.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ba/v3/Mv37cuYdQfSgjZBOEXzxhA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062227Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=8C3EA6E51FA79646461802F1DE9074478A5907E924B0C1862E5E1F1409FD6616)

-   The initial APIs of this module are supported since API version 10. Newly added APIs will be marked with a superscript to indicate their earliest API version.
    
-   The initial APIs of this class are supported since API version 10.
    
-   In the following API examples, you must first use [getMediaQuery()](../class-uicontext/document.md#getmediaquery) in **UIContext** to obtain a **MediaQuery** instance, and then call the APIs using the obtained instance.
    

#### matchMediaSync

matchMediaSync(condition: string): mediaQuery.MediaQueryListener

Sets the media query criteria and returns the corresponding listening handle.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| condition | string | Yes | Media query condition. For details, see [Syntax](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/arkts-layout-development-media-query#syntax). |

**Return value**

| Type | Description |
| :-- | :-- |
| [mediaQuery.MediaQueryListener](../../ohos-mediaquery-media-query/document.md#mediaquerylistener) | Listening handle to a media event, which is used to register or unregister the listening callback. |

**Example**

See the example for [mediaquery](../../ohos-mediaquery-media-query/document.md#example).
