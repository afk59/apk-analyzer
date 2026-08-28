# Class (BackForwardCacheSupportedFeatures)

Implements a **BackForwardCacheSupportedFeatures** object to allow a page that uses any of the following features to enter the back-forward cache. For details about the sample code, see [enableBackForwardCache](../class-webviewcontroller/document.md#enablebackforwardcache12).

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d7/v3/qWriqOrLTjmFFhG8MdIJow/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062312Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=27663161344ACD9A86969DEADC5F2E5330824C172ED07C10591DAF0F58963D03)

-   The initial APIs of this module are supported since API version 9. Updates will be marked with a superscript to indicate their earliest API version.
    
-   The initial APIs of this class are supported since API version 12.
    
-   The sample effect is subject to the actual device.
    

#### Attributes

**System capability**: SystemCapability.Web.Webview.Core

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| nativeEmbed12+ | boolean | No | No | 
Whether to allow the page that uses same-layer rendering to enter the back-forward cache.

When the value is set to **true**, you need to maintain the lifecycle of system components created for the same-layer rendering elements to avoid resource leak.

The value **true** means to allow the page that uses same-layer rendering to enter the back-forward cache, and **false** means the opposite.

Default value: **false**.

 |
| mediaTakeOver12+ | boolean | No | No | 

Whether to allow a page using the media playback takeover feature to the back-forward cache.

When the value is set to **true**, you need to maintain the lifecycle of system components created for video elements to avoid resource leak.

The value **true** means to allow a page using the media playback takeover feature to enter the back-forward cache, and **false** means the opposite.

Default value: **false**.

 |

#### constructor12+

constructor()

Constructs a **BackForwardCacheSupportedFeatures** object.

**System capability**: SystemCapability.Web.Webview.Core
