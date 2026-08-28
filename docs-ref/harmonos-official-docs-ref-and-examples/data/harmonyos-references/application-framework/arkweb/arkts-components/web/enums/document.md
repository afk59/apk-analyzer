# Enums

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/75/v3/m6RRLcPfQq2i4Lqeigyxxw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062316Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=03E50200A4F5363685F9396465D533E1BC03B22382D7572E385D27D447785130)

The initial APIs of this component are supported since API version 8. Updates will be marked with a superscript to indicate their earliest API version.

#### MessageLevel

Enumerates the information levels of the console messages.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4a/v3/ziwJ1v-KRJSDcrOhyqoHdg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062316Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=4DC844DF00C57CE7769585AA854561C4268484F87822CC4EB013215C6A3D78E0)

-   On the HTML5 side, the information level of **ConsoleMessage** corresponding to **console.log** or **console.info** is **MessageLevel.Info**.

**System capability**: SystemCapability.Web.Webview.Core

| Name | Value | Description |
| :-- | :-- | :-- |
| Debug | 1 | Debug level. |
| Error | 4 | Error level. |
| Info | 2 | Information level. |
| Log | 5 | Log level. |
| Warn | 3 | Warning level. |

#### MixedMode

Enumerates the mixed content modes.

**System capability**: SystemCapability.Web.Webview.Core

| Name | Value | Description |
| :-- | :-- | :-- |
| All | 0 | Loose mode: HTTP and HTTPS hybrid content can be loaded. This means that all insecure content can be loaded. |
| Compatible | 1 | Compatible mode: HTTP and HTTPS hybrid content can be loaded in compatibility mode. This means that some insecure content may be loaded. |
| None | 2 | Strict mode: HTTP and HTTPS hybrid content cannot be loaded. |

#### HitTestType(deprecated)

Enumerates the test result types of the click event.

**System capability**: SystemCapability.Web.Webview.Core

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7d/v3/Ea20agvQTiSvtTfSreu2DQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062316Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=F5E3C8AF6D510AD7B65DEA4C259B8E662316505E9FA2EA2E5068CFD76AC62716)

This enum is supported since API version 9 and deprecated since API version 21. You are advised to use [WebHitTestType](../../../arkts-api/ohos-web-webview-webview/enums/document.md#webhittesttype) instead.

| Name | Value | Description |
| :-- | :-- | :-- |
| EditText | 0 | Editable area. |
| Email | 1 | Email address. |
| HttpAnchor | 2 | Hyperlink whose **src** is **http**. |
| HttpAnchorImg | 3 | Image with a hyperlink, where **src** is **http**. |
| Img | 4 | HTML::img tag. |
| Map | 5 | Geographical address. |
| Phone | 6 | Phone number. |
| Unknown | 7 | Unknown content. |

#### CacheMode

Enumerates the cache modes.

**System capability**: SystemCapability.Web.Webview.Core

| Name | Value | Description |
| :-- | :-- | :-- |
| Default9+ | 0 | The cache that has not expired is preferentially used to load resources. If the cache is invalid or no cache is available, resources are obtained from the Internet. |
| None | 1 | The cache (including expired resources) is preferentially used to load resources. If no cache is available, resources are obtained from the network. |
| Online | 2 | The cache is not used to load the resources. All resources are forcibly obtained from the Internet. |
| Only | 3 | The local cache alone is used to load the resources. |

#### OverScrollMode11+

Enumerates whether to enable overscroll mode.

**System capability**: SystemCapability.Web.Webview.Core

| Name | Value | Description |
| :-- | :-- | :-- |
| NEVER | 0 | The overscroll mode is disabled. |
| ALWAYS | 1 | The overscroll mode is enabled. |

#### BlurOnKeyboardHideMode14+

Enumerates whether the **Web** component loses focus when the soft keyboard is hidden.

**System capability**: SystemCapability.Web.Webview.Core

**Parameters**

| Name | Value | Description |
| :-- | :-- | :-- |
| SILENT | 0 | The **Web** component does not lose focus when the soft keyboard is hidden. |
| BLUR | 1 | The **Web** component loses focus when the soft keyboard is hidden, and the focus moves from the text box to the web body. |

#### WebDarkMode9+

Enumerates whether to enable web dark mode.

**System capability**: SystemCapability.Web.Webview.Core

| Name | Value | Description |
| :-- | :-- | :-- |
| Off | 0 | The web dark mode is disabled. |
| On | 1 | The web dark mode is enabled. |
| Auto | 2 | The web dark mode setting follows the system setting. |

#### WebCaptureMode10+

Enumerates the web screen capture modes.

**System capability**: SystemCapability.Web.Webview.Core

| Name | Value | Description |
| :-- | :-- | :-- |
| HOME\_SCREEN | 0 | Home screen capture mode. |

#### ThreatType11+

Enumerates the website threat types.

**System capability**: SystemCapability.Web.Webview.Core

| Name | Value | Description |
| :-- | :-- | :-- |
| THREAT\_ILLEGAL | 0 | Illegal website. |
| THREAT\_FRAUD | 1 | Fraudulent website. |
| THREAT\_RISK | 2 | Website that poses security risks. |
| THREAT\_WARNING | 3 | Website suspected to contain unsafe content. |
| THREAT\_NONE21+ | 4 | Website that passes the security check and no risk is found. |
| THREAT\_UNPROCESSED21+ | 5 | Website that does not perform security check. |

#### RenderExitReason9+

Enumerates the reasons why the rendering process exits.

**System capability**: SystemCapability.Web.Webview.Core

| Name | Value | Description |
| :-- | :-- | :-- |
| ProcessAbnormalTermination | 0 | The rendering process exits abnormally. |
| ProcessWasKilled | 1 | The rendering process receives a SIGKILL message or is manually terminated. |
| ProcessCrashed | 2 | The rendering process crashes due to segmentation or other errors. |
| ProcessOom | 3 | The program memory is insufficient. |
| ProcessExitUnknown | 4 | Other reason. |

#### SslError9+

Enumerates the error codes returned by **onSslErrorEventReceive** API.

**System capability**: SystemCapability.Web.Webview.Core

| Name | Value | Description |
| :-- | :-- | :-- |
| Invalid | 0 | Minor error. |
| HostMismatch | 1 | The host name does not match. |
| DateInvalid | 2 | The certificate has an invalid date. |
| Untrusted | 3 | The certificate issuer is not trusted. |

#### FileSelectorMode9+

Enumerates the modes of the file selector.

**System capability**: SystemCapability.Web.Webview.Core

| Name | Value | Description |
| :-- | :-- | :-- |
| FileOpenMode | 0 | Open and upload a file. |
| FileOpenMultipleMode | 1 | Open and upload multiple files. |
| FileOpenFolderMode | 2 | Open and upload a folder. |
| FileSaveMode | 3 | Save a file. |

#### WebLayoutMode11+

Enumerates the web layout modes.

**System capability**: SystemCapability.Web.Webview.Core

| Name | Value | Description |
| :-- | :-- | :-- |
| NONE | 0 | The web layout follows the system. |
| FIT\_CONTENT | 1 | The web layout adapts to the page size. |

#### RenderProcessNotRespondingReason12+

Enumerates the reasons why the rendering process does not respond.

**System capability**: SystemCapability.Web.Webview.Core

| Name | Value | Description |
| :-- | :-- | :-- |
| INPUT\_TIMEOUT | 0 | The input event response sent to the rendering process times out. |
| NAVIGATION\_COMMIT\_TIMEOUT | 1 | The navigation for loading a new web page times out. |

#### ProtectedResourceType9+

**System capability**: SystemCapability.Web.Webview.Core

| Name | Value | Description | Available Permission |
| :-- | :-- | :-- | :-- |
| MidiSysex | TYPE\_MIDI\_SYSEX | 
MIDI SYSEX resource.

Currently, only permission events can be reported. MIDI devices are not yet supported.

 | Currently, the permission related to the Musical Instrument Digital Interface (MIDI) device cannot be requested. |
| VIDEO\_CAPTURE10+ | TYPE\_VIDEO\_CAPTURE | Video capture resource, such as a camera. | Camera permission: **ohos.permission.CAMERA**. |
| AUDIO\_CAPTURE10+ | TYPE\_AUDIO\_CAPTURE | Audio capture resource, such as a microphone. | Microphone permission: **ohos.permission.MICROPHONE**. |
| SENSOR12+ | TYPE\_SENSOR | Sensor resource, such as an acceleration sensor. | 

Acceleration sensor permission: **ohos.permission.ACCELEROMETER**,

Gyroscope sensor permission: **ohos.permission.GYROSCOPE**.

 |

#### ContextMenuSourceType9+

Enumerates the event source types that trigger the context menu.

**System capability**: SystemCapability.Web.Webview.Core

| Name | Value | Description |
| :-- | :-- | :-- |
| None | 0 | Other event sources. |
| Mouse | 1 | Mouse event. |
| LongPress | 2 | Long press event. |

#### ContextMenuMediaType9+

Enumerates the media types that trigger the context menu.

**System capability**: SystemCapability.Web.Webview.Core

| Name | Value | Description |
| :-- | :-- | :-- |
| None | 0 | Other non-image media types. |
| Image | 1 | Image. |

#### ContextMenuDataMediaType22+

Enumerates the media types that trigger the context menu (enhanced type obtaining capability).

**System capability**: SystemCapability.Web.Webview.Core

| Name | Value | Description |
| :-- | :-- | :-- |
| NONE | 0 | Default value, indicating that the current context menu is not associated with any media type (for example, right-click text or blank area). |
| IMAGE | 1 | Image. |
| VIDEO | 2 | Video. |
| AUDIO | 3 | Audio. |
| CANVAS | 4 | Canvas. |

#### ContextMenuInputFieldType9+

Enumerates the input field types.

**System capability**: SystemCapability.Web.Webview.Core

| Name | Value | Description |
| :-- | :-- | :-- |
| None | 0 | Non-input field. |
| PlainText | 1 | Plain text field, such as the text, search, or email field. |
| Password | 2 | Password field. |
| Number | 3 | Number field. |
| Telephone | 4 | Phone number field. |
| Other | 5 | Field of any other type. |

#### NativeEmbedStatus11+

Enumerates the lifecycles of the same-layer tag. When a same-layer tag exists on the loaded page, **CREATE** is triggered. When a same-layer tag is moved or is enlarged, **UPDATE** is triggered. When the page exits, **DESTROY** is triggered.

**System capability**: SystemCapability.Web.Webview.Core

| Name | Value | Description |
| :-- | :-- | :-- |
| CREATE | 0 | The same-layer tag is created. |
| UPDATE | 1 | The same-layer tag is updated. |
| DESTROY | 2 | The same-layer tag is destroyed. |
| ENTER\_BFCACHE12+ | 3 | The same-layer tag enters BFCache. |
| LEAVE\_BFCACHE12+ | 4 | The same-layer tag leaves BFCache. |

#### NativeEmbedParamStatus21+

Enumerates the status change types of the **param** element embedded in the same-layer rendering tag **object**. **ADD** is triggered when the **param** element is added, **UPDATE** is triggered when it is modified, and **DELETE** is triggered when it is deleted.

**System capability**: SystemCapability.Web.Webview.Core

| Name | Value | Description |
| :-- | :-- | :-- |
| ADD | 0 | Triggered when a **param** element is added. |
| UPDATE | 1 | Triggered when a **param** element is modified. |
| DELETE | 2 | Triggered when a **param** element is deleted. |

#### ContextMenuEditStateFlags9+

Enumerates the context menu edit state flags. This enum can be used in bitwise OR mode. For example, to support **CAN\_CUT**, **CAN\_COPY**, and **CAN\_SELECT\_ALL** at the same time, use **CAN\_CUT | CAN\_COPY | CAN\_SELECT\_ALL** or **11**.

**System capability**: SystemCapability.Web.Webview.Core

| Name | Value | Description |
| :-- | :-- | :-- |
| NONE | 0 | Editing is not allowed. |
| CAN\_CUT | 1 << 0 | Cutting is supported. |
| CAN\_COPY | 1 << 1 | Copying is supported. |
| CAN\_PASTE | 1 << 2 | Pasting is supported. |
| CAN\_SELECT\_ALL | 1 << 3 | Selecting all is supported. |

#### WebNavigationType11+

Enumerates the navigation types.

**System capability**: SystemCapability.Web.Webview.Core

| Name | Value | Description |
| :-- | :-- | :-- |
| UNKNOWN | 0 | Unknown type. |
| MAIN\_FRAME\_NEW\_ENTRY | 1 | Navigation to a new history entry from the main document. |
| MAIN\_FRAME\_EXISTING\_ENTRY | 2 | Navigation to an existing history entry from the main document. |
| NAVIGATION\_TYPE\_NEW\_SUBFRAME | 4 | User-triggered navigation from a subdocument. |
| NAVIGATION\_TYPE\_AUTO\_SUBFRAME | 5 | Non-user-triggered navigation from a subdocument. |

#### RenderMode12+

Enumerates the rendering modes of the **Web** component. By default, the asynchronous rendering mode is used.

The asynchronous rendering mode is recommended because it has better performance and lower power consumption.

**System capability**: SystemCapability.Web.Webview.Core

| Name | Value | Description |
| :-- | :-- | :-- |
| ASYNC\_RENDER | 0 | The **Web** component as a graphic surface node is rendered asynchronously and displayed independently. The maximum width of the **Web** component is 7,680 px (physical pixel). |
| SYNC\_RENDER | 1 | The **Web** component as a graphic canvas node is rendered synchronously and displayed together with the system component. The maximum width of the **Web** component is 500,000 px (physical pixel). |

#### ViewportFit12+

Enumerates the viewport types available for **viewport-fit** in the web page **<meta>** tag.

**System capability**: SystemCapability.Web.Webview.Core

| Name | Value | Description |
| :-- | :-- | :-- |
| AUTO | 0 | The entire web page is visible. Default value. |
| CONTAINS | 1 | The initial layout viewport and the visual viewport fit within the largest rectangle that adapts to the device's display screen. |
| COVER | 2 | The initial layout viewport and the visual viewport are confined within the bounding rectangle of the device's physical screen. |

#### WebKeyboardAvoidMode12+

Enumerates the soft keyboard avoidance modes.

**System capability**: SystemCapability.Web.Webview.Core

| Name | Value | Description |
| :-- | :-- | :-- |
| RESIZE\_VISUAL | 0 | For soft keyboard avoidance, the visual viewport is resized, but not the layout viewport. |
| RESIZE\_CONTENT | 1 | For soft keyboard avoidance, both the visual viewport and layout viewport are resized. Default value. |
| OVERLAYS\_CONTENT | 2 | No viewport is resized, and soft keyboard avoidance is not triggered. |
| RETURN\_TO\_UICONTEXT22+ | 3 | The soft keyboard avoidance behavior of the **Web** component follows the [KeyboardAvoidMode](../../../../arkui/arkts-api/ui/ohos-arkui-uicontext-uicontext/enums/document.md#keyboardavoidmode11) set by UIcontext. The **Web** component does not process the avoidance behavior of the component. |

#### WebElementType13+

Enumerates the web element types.

**System capability**: SystemCapability.Web.Webview.Core

**Parameters**

| Name | Value | Description |
| :-- | :-- | :-- |
| IMAGE | 1 | Image. |
| LINK20+ | 2 | Hyperlink. |
| TEXT21+ | 3 | Text or editable area. |

#### WebResponseType13+

Enumerates the response types of the menu.

**System capability**: SystemCapability.Web.Webview.Core

**Parameters**

| Name | Value | Description |
| :-- | :-- | :-- |
| LONG\_PRESS | 1 | The menu is displayed when the component is long-pressed. |
| RIGHT\_CLICK21+ | 2 | The menu is displayed when the component is right-clicked. |

#### AudioSessionType20+

Enumerates the web audio types in the application.

**System capability**: SystemCapability.Web.Webview.Core

**Parameters**

| Name | Value | Description |
| :-- | :-- | :-- |
| AMBIENT | 3 | Web game sounds and system music can be played at the same time. This value is applicable to web game scenarios. Its corresponding system audio stream type is **STREAM\_USAGE\_GAME**. |

#### GestureFocusMode20+

Enumerates the focus modes.

**System capability**: SystemCapability.Web.Webview.Core

| Name | Value | Description |
| :-- | :-- | :-- |
| DEFAULT | 0 | The **Web** component applies for the focus when it is touched, long-pressed, swiped, or zoomed. |
| GESTURE\_TAP\_AND\_LONG\_PRESS | 1 | The **Web** component applies for the focus only when it is touched and long-pressed. The swipe and zoom gestures do not apply for the focus. |

#### WebRotateEffect22+

Enumerates the modes in which the component's content is rendered to fit the new size during its width and height animation process when the component is rotated.

**System capability**: SystemCapability.Web.Webview.Core

| Name | Value | Description |
| :-- | :-- | :-- |
| TOPLEFT\_EFFECT | 0 | The component's content stays at the final size and always aligned with the upper left corner of the component. This value is used by default. |
| RESIZE\_COVER\_EFFECT | 1 | While maintaining its aspect ratio in the final state, the component's content is scaled to cover the component's entire content box. It is always aligned with the center of the component, so that its middle part is displayed. |

#### WebBypassVsyncCondition20+

Enumerates whether to allow the rendering process to bypass the vsync scheduling.

**System capability**: SystemCapability.Web.Webview.Core

| Name | Value | Description |
| :-- | :-- | :-- |
| NONE | 0 | The rendering process does not bypass the vsync scheduling. Default value. |
| SCROLLBY\_FROM\_ZERO\_OFFSET | 1 | When **scrollby** is used (only the scrolling offset is supported) and the scrolling offset of the web page is **0**, the rendering process bypasses the vsync scheduling. |

#### PdfLoadResult20+

Enumerates the PDF page loading results.

**System capability**: SystemCapability.Web.Webview.Core

| Name | Value | Description |
| :-- | :-- | :-- |
| LOAD\_SUCCESS | 0 | The PDF file is successfully loaded. |
| PARSE\_ERROR\_FILE | 1 | The PDF file fails to be loaded. |
| PARSE\_ERROR\_FORMAT | 2 | The PDF file format is not supported. |
| PARSE\_ERROR\_PASSWORD | 3 | The PDF file password is incorrect. |
| PARSE\_ERROR\_HANDLER | 4 | The PDF file fails to be processed. |

#### DetectedBlankScreenReason22+

Enumerates the reasons for the blank screen.

**System capability**: SystemCapability.Web.Webview.Core

| Name | Value | Description |
| :-- | :-- | :-- |
| NO\_CONTENTFUL\_NODES | 0 | 
No contentful node is detected.

This may be triggered when the detection policy is **DETECTION\_CONTENTFUL\_NODES\_SEVENTEEN**.

 |
| SUB\_THRESHOLD\_CONTENTFUL\_NODES | 1 | 

The number of contentful nodes detected is less than or equal to the threshold.

This may be triggered when the detection policy is **DETECTION\_CONTENTFUL\_NODES\_SEVENTEEN** and **contentfulNodesCountThreshold** is set.

 |

#### BlankScreenDetectionMethod22+

Enumerates the methods for the blank screen detection.

**System capability**: SystemCapability.Web.Webview.Core

| Name | Value | Description |
| :-- | :-- | :-- |
| DETECTION\_CONTENTFUL\_NODES\_SEVENTEEN | 0 | 
The page is detected using the 17-point detection method. When a rendered and contentful node is detected by a detection point, it is considered that the detection point is hit. A contentful node refers to an image, video, or text node.

If no contentful node is detected or the number of contentful nodes is less than the threshold, a blank or near-blank screen is displayed.

The 17 detection points are as follows:

Center point (1): The center point is at the geometric center of the page.

Internal grid intersection points (16): A 5 × 5 uniform grid is defined in the page area. The 16 points are the intersection points of four vertical equal division lines and four horizontal equal division lines in the page.

 |

#### CredentialType22+

Enumerates the credential types.

**System capability**: SystemCapability.Web.Webview.Core

| Name | Value | Description |
| :-- | :-- | :-- |
| CREDENTIAL\_USER | 2 | User credential. |
| CREDENTIAL\_APP | 3 | Application credential. |
| CREDENTIAL\_UKEY | 4 | UKey credential. |

#### PinVerifyResult22+

Enumerates the PIN verification results.

**System capability**: SystemCapability.Web.Webview.Core

| Name | Value | Description |
| :-- | :-- | :-- |
| PIN\_VERIFICATION\_SUCCESS | 0 | Verification successful. |
| PIN\_VERIFICATION\_FAILED | 1 | Verification failed. |
