# Module Description

This module provides the web control capability. For details about the web page display capability, see [Components](../../../arkts-components/web/components/document.md).

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f7/v3/NvmNU8vJTHe6H4SvTTFgoQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062312Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=A1E71D6BF8832FFE4CEDCB2974673EC1678B4DACD86FD49FCEBC12DAB3E25AF6)

-   The initial APIs of this module are supported since API version 9. Updates will be marked with a superscript to indicate their earliest API version.
    
-   The sample effect is subject to the actual device.
    
-   Static methods must be used on the user interface (UI) thread.
    

This module provides the following common functionalities for web control:

-   [AdsBlockManager](../class-adsblockmanager/document.md): Ad filtering configuration.
-   [BackForwardCacheOptions](../class-backforwardcacheoptions/document.md): Forward and backward cache configuration.
-   [BackForwardCacheSupportedFeatures](../class-backforwardcachesupportedfeatures/document.md): Forward and backward cache feature configuration.
-   [GeolocationPermissions](../class-geolocationpermissions/document.md): Geolocation permission configuration.
-   [JsMessageExt](../class-jsmessageext/document.md): JavaScript execution result.
-   [MediaSourceInfo](../class-mediasourceinfo/document.md): Media source information configuration.
-   [NativeMediaPlayerSurfaceInfo](../class-nativemediaplayersurfaceinfo/document.md): Rendering information when the application takes over media playback.
-   [PdfData](../class-pdfdata/document.md): Generated PDF output data.
-   [ProxyConfig](../class-proxyconfig/document.md): Network proxy configuration.
-   [ProxyController](../class-proxycontroller/document.md): Network proxy controller.
-   [WebviewController](../class-webviewcontroller/document.md): **Web** component controller.
-   [WebCookieManager](../class-webcookiemanager/document.md): Cookie management.
-   [WebDataBase](../class-webdatabase/document.md): Database management.
-   [WebDownloadDelegate](../class-webdownloaddelegate/document.md): Download task status event.
-   [WebDownloadItem](../class-webdownloaditem/document.md): Download task.
-   [WebDownloadManager](../class-webdownloadmanager/document.md): Download task management.
-   [WebHttpBodyStream](../class-webhttpbodystream/document.md): HTTP request body.
-   [WebMessageExt](../class-webmessageext/document.md): Data object for communication between the frontend and application.
-   [WebResourceHandler](../class-webresourcehandler/document.md): Resource loading control.
-   [WebSchemeHandler](../class-webschemehandler/document.md): Request interceptor of a specified scheme.
-   [WebSchemeHandlerRequest](../class-webschemehandlerrequest/document.md): Request intercepted by the interceptor.
-   [WebSchemeHandlerResponse](../class-webschemehandlerresponse/document.md): Custom responses for intercepted requests.
-   [WebStorage](../class-webstorage/document.md): Storage operation API of the **Web** component.
-   [BackForwardList](../interface-backforwardlist/document.md): History information list.
-   [NativeMediaPlayerBridge](../interface-nativemediaplayerbridge/document.md): Bridge API for taking over web media players.
-   [NativeMediaPlayerHandler](../interface-nativemediaplayerhandler/document.md): Event API for taking over web media players.
-   [WebMessagePort](../interface-webmessageport/document.md): Message port between the web page and application.

#### Required Permissions

**ohos.permission.INTERNET**, required for accessing online web pages. For details about how to apply for a permission, see [Declaring Permissions](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/declare-permissions).

#### Modules to Import

import { webview } from '@kit.ArkWeb';

**System capability**: SystemCapability.Web.Webview.Core
