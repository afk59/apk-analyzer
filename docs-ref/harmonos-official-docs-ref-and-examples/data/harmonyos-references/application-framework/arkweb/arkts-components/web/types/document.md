# Types

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1c/v3/sYGG1iZgQ6moMVfIfT-4nw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062316Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=F325EE8F89418FC0AB22B6DB4C89C0FB5F306AD4119E6AEE8FF2D4A8853A1ADC)

-   The initial APIs of this component are supported since API version 8. Updates will be marked with a superscript to indicate their earliest API version.
    
-   The sample effect is subject to the actual device.
    

#### WebviewController9+

type WebviewController = WebviewController

Defines methods for the web controller.

**System capability**: SystemCapability.Web.Webview.Core

| Type | Description |
| :-- | :-- |
| [WebviewController](../../../arkts-api/ohos-web-webview-webview/class-webviewcontroller/document.md) | Used to control the behavior of the **Web** component. A **WebviewController** object can control only one **Web** component. Methods (except static methods) on the **WebviewController** can be called only after the **Web** component is bound to the **WebviewController**. |

#### OnAdsBlockedCallback12+

type OnAdsBlockedCallback = (details: AdsBlockedDetails) => void

Defines a callback invoked when ads are blocked on the web page.

**System capability**: SystemCapability.Web.Webview.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| details | [AdsBlockedDetails](../interfaces-others/document.md#adsblockeddetails12) | Yes | Detailed information about the blocked ads when ads are blocked. |

#### OnSslErrorEventCallback12+

type OnSslErrorEventCallback = (sslErrorEvent: SslErrorEvent) => void

Defines a callback invoked when an SSL error occurs during resource loading.

**System capability**: SystemCapability.Web.Webview.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| sslErrorEvent | [SslErrorEvent](../interfaces-others/document.md#sslerrorevent12) | Yes | Details about the callback invoked when an SSL error occurs during resource loading. |

#### OnVerifyPinCallback22+

type OnVerifyPinCallback = (verifyPinEvent: VerifyPinEvent) => void

Callback triggered to notify the user of PIN authentication.

**System capability**: SystemCapability.Web.Webview.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| verifyPinEvent | [VerifyPinEvent](../interfaces-others/document.md#verifypinevent22) | Yes | Details of the callback triggered to notify the user of PIN authentication. |

#### OnContextMenuHideCallback11+

type OnContextMenuHideCallback = () => void

Defines a callback invoked when the context menu is hidden.

**System capability**: SystemCapability.Web.Webview.Core

#### OnRenderProcessNotRespondingCallback12+

type OnRenderProcessNotRespondingCallback = (data : RenderProcessNotRespondingData) => void

Defines a callback invoked when the rendering process does not respond.

**System capability**: SystemCapability.Web.Webview.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| data | [RenderProcessNotRespondingData](../interfaces-others/document.md#renderprocessnotrespondingdata12) | Yes | Detailed information about the unresponsive rendering process. |

#### OnRenderProcessRespondingCallback12+

type OnRenderProcessRespondingCallback = () => void

Defines a callback invoked when the rendering process transitions back to a normal operating state from an unresponsive state.

**System capability**: SystemCapability.Web.Webview.Core

#### OnViewportFitChangedCallback12+

type OnViewportFitChangedCallback = (viewportFit: ViewportFit) => void

Defines a callback invoked when the **viewport-fit** configuration in the web page's **<meta>** tag changes.

**System capability**: SystemCapability.Web.Webview.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| viewportFit | [ViewportFit](../enums/document.md#viewportfit12) | Yes | Viewport type for **viewport-fit** in the web page **<meta>** tag. |

#### OnNativeEmbedVisibilityChangeCallback12+

type OnNativeEmbedVisibilityChangeCallback = (nativeEmbedVisibilityInfo: NativeEmbedVisibilityInfo) => void

Defines a callback invoked when the visibility of a same-layer tag changes.

**System capability**: SystemCapability.Web.Webview.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| nativeEmbedVisibilityInfo | [NativeEmbedVisibilityInfo](../interfaces-others/document.md#nativeembedvisibilityinfo12) | Yes | Visibility information about the same-layer tag. |

#### OnFullScreenEnterCallback12+

type OnFullScreenEnterCallback = (event: FullScreenEnterEvent) => void

Defines a callback invoked when the **Web** component enters full screen mode.

**System capability**: SystemCapability.Web.Webview.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| event | [FullScreenEnterEvent](../interfaces-others/document.md#fullscreenenterevent12) | Yes | Callback event for the **Web** component to enter full screen mode. |

#### OnFirstMeaningfulPaintCallback12+

type OnFirstMeaningfulPaintCallback = (firstMeaningfulPaint: [FirstMeaningfulPaint](../interfaces-others/document.md#firstmeaningfulpaint12)) => void

Defines a callback invoked when the first meaningful paint occurs on the page.

**System capability**: SystemCapability.Web.Webview.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| firstMeaningfulPaint | [FirstMeaningfulPaint](../interfaces-others/document.md#firstmeaningfulpaint12) | Yes | Information about the first meaningful paint. |

#### OnLargestContentfulPaintCallback12+

type OnLargestContentfulPaintCallback = (largestContentfulPaint: [LargestContentfulPaint](../interfaces-others/document.md#largestcontentfulpaint12)) => void

Defines a callback invoked when the largest content paint occurs on the web page.

**System capability**: SystemCapability.Web.Webview.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| largestContentfulPaint | [LargestContentfulPaint](../interfaces-others/document.md#largestcontentfulpaint12) | Yes | Information about the largest content paint. |

#### OnNavigationEntryCommittedCallback11+

type OnNavigationEntryCommittedCallback = (loadCommittedDetails: [LoadCommittedDetails](../interfaces-others/document.md#loadcommitteddetails11)) => void

Defines a callback invoked when a navigation entry is submitted.

**System capability**: SystemCapability.Web.Webview.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| loadCommittedDetails | [LoadCommittedDetails](../interfaces-others/document.md#loadcommitteddetails11) | Yes | Detailed information about the web page that has been submitted for redirection. |

#### OnSafeBrowsingCheckResultCallback11+

type OnSafeBrowsingCheckResultCallback = (threatType: ThreatType) => void

Defines a callback invoked by a website safe browsing check.

**System capability**: SystemCapability.Web.Webview.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| threatType | [ThreatType](../enums/document.md#threattype11) | Yes | Website threat type. |

#### OnIntelligentTrackingPreventionCallback12+

type OnIntelligentTrackingPreventionCallback = (details: IntelligentTrackingPreventionDetails) => void

Defines a callback invoked when the tracker cookie is intercepted.

**System capability**: SystemCapability.Web.Webview.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| details | [IntelligentTrackingPreventionDetails](../interfaces-others/document.md#intelligenttrackingpreventiondetails12) | Yes | Detailed information about intelligent tracking prevention. |

#### OnOverrideUrlLoadingCallback12+

type OnOverrideUrlLoadingCallback = (webResourceRequest: WebResourceRequest) => boolean

Defines a callback for **onOverrideUrlLoading**.

**System capability**: SystemCapability.Web.Webview.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| webResourceRequest | [WebResourceRequest](../class-webresourcerequest/document.md) | Yes | Information about the URL request. |

**Return value**

| Type | Description |
| :-- | :-- |
| boolean | Whether the loading is blocked. **true** is returned if the loading is blocked; otherwise, **false** is returned. |

#### WebKeyboardCallback12+

type WebKeyboardCallback = (keyboardCallbackInfo: WebKeyboardCallbackInfo) => WebKeyboardOptions

Defines a callback to intercept the soft keyboard initiated from editable elements on a web page. This event is typically called when the **<input>** tag on the web page is clicked.

**System capability**: SystemCapability.Web.Webview.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| keyboardCallbackInfo | [WebKeyboardCallbackInfo](../interfaces-others/document.md#webkeyboardcallbackinfo12) | Yes | Input parameter of the callback used to intercept the soft keyboard initiated from editable elements on a web page, including [WebKeyboardController](../class-webkeyboardcontroller/document.md) and editable element attributes. |

**Return value**

| Type | Description |
| :-- | :-- |
| [WebKeyboardOptions](../interfaces-others/document.md#webkeyboardoptions12) | [WebKeyboardOptions](../interfaces-others/document.md#webkeyboardoptions12) instance, which is used to determine which type of soft keyboard to start by the ArkWeb kernel. |

#### OnOverrideErrorPageCallback20+

type OnOverrideErrorPageCallback = (errorPageEvent: OnErrorReceiveEvent) => string

Defines a callback of **onOverrideErrorPage**. This callback is triggered when a web page fails to be loaded.

**System capability**: SystemCapability.Web.Webview.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| errorPageEvent | [OnErrorReceiveEvent](../interfaces-others/document.md#onerrorreceiveevent12) | Yes | Information returned when an error occurs during web page loading. |

**Return value**

| Type | Description |
| :-- | :-- |
| string | Base64-encoded HTML text content. |

#### MouseInfoCallback20+

type MouseInfoCallback = (event: NativeEmbedMouseInfo) => void

Defines a callback triggered when a same-layer tag is clicked using the mouse or touchpad.

**System capability**: SystemCapability.Web.Webview.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| event | [NativeEmbedMouseInfo](../interfaces-others/document.md#nativeembedmouseinfo20) | Yes | Detailed information about clicking or touching and holding a same-layer tag using the mouse or touchpad. |

**Example**

For details about the sample code, see [onNativeEmbedMouseEvent](../events/document.md#onnativeembedmouseevent20).

#### OnNativeEmbedObjectParamChangeCallback21+

type OnNativeEmbedObjectParamChangeCallback = (event: NativeEmbedParamDataInfo) => void

Defines a callback triggered when the **param** element embedded in the same-layer rendered **object** tag is added, modified, or deleted.

**System capability**: SystemCapability.Web.Webview.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| event | [NativeEmbedParamDataInfo](../interfaces-others/document.md#nativeembedparamdatainfo21) | Yes | Detailed information about the changes of the **param** element embedded in the **object** tag. |

**Example**

For details about the sample code, see [onNativeEmbedObjectParamChange](../events/document.md#onnativeembedobjectparamchange21).

#### OnDetectBlankScreenCallback22+

type OnDetectBlankScreenCallback = (event: BlankScreenDetectionEventInfo) => void

Defines a callback triggered when a blank screen is detected.

**System capability**: SystemCapability.Web.Webview.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| event | [BlankScreenDetectionEventInfo](../interfaces-others/document.md#blankscreendetectioneventinfo22) | Yes | Detailed information when a blank screen is detected. |

**Example**

For details about the sample code, see [onDetectedBlankScreen](../events/document.md#ondetectedblankscreen22).
