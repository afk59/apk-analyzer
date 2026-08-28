# Class (PrefetchOptions)

Defines the prefetch behavior of web pages, including whether to ignore **Cache-Control: no-store** in the response header and the minimum interval between two prefetches.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c4/v3/zpP0B5bDT4OntRLwm8AzJw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062312Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=A73FBADB3A351F81AFE2E662B8092433FEFD114FEDC340D7E5B1366E9A7DA9C3)

-   The initial APIs of this module are supported since API version 9. Updates will be marked with a superscript to indicate their earliest API version.
    
-   The initial APIs of this class are supported since API version 21.
    
-   The sample effect is subject to the actual device.
    

#### Attributes

**System capability**: SystemCapability.Web.Webview.Core

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| minTimeBetweenPrefetchesMs21+ | number | No | No | 
Minimum interval between two web page prefetches.

The interval between two web page prefetches is calculated. If it is less than the specified value, the current prefetch is canceled.

The default value is **500**, and the maximum value is **500**.

If the value is set to a negative number, the default value **0** is used.

Unit: ms.

 |
| ignoreCacheControlNoStore21+ | boolean | No | No | 

Whether to ignore **Cache-Control: no-store** in the response header.

Default value: **false**.

The value **true** means to ignore **Cache-Control: no-store** in the response header, and **false** means the opposite.

 |

#### constructor21+

constructor()

A constructor used to create a **PrefetchOptions** instance.

**System capability**: SystemCapability.Web.Webview.Core
