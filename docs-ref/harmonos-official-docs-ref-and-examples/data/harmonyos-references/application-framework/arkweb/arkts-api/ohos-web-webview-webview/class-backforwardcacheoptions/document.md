# Class (BackForwardCacheOptions)

Implements a **BackForwardCacheOptions** object to set back-forward cache options of the **Web** component.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/30/v3/8FcRWz43St-wuiLQLx8QOw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062312Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=2A51074E1577F0F4C0ECD372A20E5E7EEF7040870CFBD0E1800DB731B197CCC3)

-   The initial APIs of this module are supported since API version 9. Updates will be marked with a superscript to indicate their earliest API version.
    
-   The initial APIs of this class are supported since API version 12.
    
-   The sample effect is subject to the actual device.
    

**System capability**: SystemCapability.Web.Webview.Core

#### Attributes

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| size12+ | number | No | No | 
The maximum number of pages that can be cached in a **Web** component.

The default value is **1**, and the maximum value is **50**.

If this parameter is set to **0** or a negative value, the back-forward cache is disabled.

The **Web** component reclaims the cache for memory pressure.

 |
| timeToLive12+ | number | No | No | 

The time that a **Web** component allows a page to stay in the back-forward cache.

If this parameter is set to **0** or a negative value, the back-forward cache is disabled.

Default value: **600**

Unit: second

 |

#### constructor12+

constructor()

Constructs a **BackForwardCacheOptions** object.

**System capability**: SystemCapability.Web.Webview.Core
