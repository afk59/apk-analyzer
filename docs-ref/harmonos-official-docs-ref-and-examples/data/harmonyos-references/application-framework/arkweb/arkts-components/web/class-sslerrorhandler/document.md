# Class (SslErrorHandler)

Implements an **SslErrorHandler** object to handle SSL error notification events returned by the **Web** component. For details about the sample code, see the [onSslErrorEvent](../events/document.md#onsslerrorevent12) event.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c0/v3/A6gsPgirSaKgOOewtxGnyQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062315Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=B5546361FA6A76C3E162071D1EFAC3B72E6290A70237087F69AF2BEA8B502A8F)

-   The initial APIs of this component are supported since API version 8. Updates will be marked with a superscript to indicate their earliest API version.
    
-   The initial APIs of this class are supported since API version 9.
    
-   The sample effect is subject to the actual device.
    

#### constructor9+

constructor()

Constructs a **SslErrorHandler** object.

**System capability**: SystemCapability.Web.Webview.Core

#### handleCancel9+

handleCancel(): void

Cancels this request.

**System capability**: SystemCapability.Web.Webview.Core

#### handleConfirm9+

handleConfirm(): void

Continues using the SSL certificate.

**System capability**: SystemCapability.Web.Webview.Core

#### handleCancel20+

handleCancel(abortLoading: boolean): void

Cancels this request and determines whether to stop loading based on the **abortLoading** parameter.

**System capability**: SystemCapability.Web.Webview.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| abortLoading | boolean | Yes | 
Whether to stop loading the page after the request is canceled.

The value **true** means to stop loading the page, and **false** means to continue loading the page.

The default value is **false**.

 |
