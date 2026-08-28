# Class (NativeMediaPlayerSurfaceInfo)

Implements a **NativeMediaPlayerSurfaceInfo** object to provide the surface information used for same-layer rendering [when the application takes over the media playback of the web page](../../../arkts-components/web/attributes/document.md#enablenativemediaplayer12).

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2d/v3/gEbhkm_vR1u81SyxRTvjJA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062312Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=EACDB62ABCCB08447570175721901511EADDED38A752A0E8DF07C79C91B4317D)

-   The initial APIs of this module are supported since API version 9. Updates will be marked with a superscript to indicate their earliest API version.
    
-   The initial APIs of this class are supported since API version 12.
    
-   The sample effect is subject to the actual device.
    

#### Attributes

**System capability**: SystemCapability.Web.Webview.Core

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| id12+ | string | No | No | 
Surface ID, which is the **psurfaceid** of the native image used for rendering at the same layer.

For details, see [NativeEmbedDataInfo](../../../arkts-components/web/interfaces-others/document.md#nativeembeddatainfo11).

 |
| rect12+ | [RectEvent](../interfaces-others/document.md#rectevent12) | No | No | Position of the surface. |
