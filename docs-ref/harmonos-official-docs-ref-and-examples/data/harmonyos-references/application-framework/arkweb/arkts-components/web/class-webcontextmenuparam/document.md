# Class (WebContextMenuParam)

Implements a **WebContextMenuParam** object, which is displayed after the user clicks the right mouse button or long presses a specific element, such as an image or a link. For details about the sample code, see [onContextMenuShow](../events/document.md#oncontextmenushow9).

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/41/v3/BONI8oJqScqTT0JLGsy9SQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062315Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=7ED1DE5C8DDF6CF5B4C8A7A3864D1C6D1B90B92FC5970CF83031C2C0512F8FB7)

-   The initial APIs of this component are supported since API version 8. Updates will be marked with a superscript to indicate their earliest API version.
    
-   The initial APIs of this class are supported since API version 9.
    
-   The sample effect is subject to the actual device.
    

#### constructor9+

constructor()

Constructs a **WebContextMenuParam** object.

**System capability**: SystemCapability.Web.Webview.Core

#### x9+

x(): number

Obtains the X coordinate of the context menu.

**System capability**: SystemCapability.Web.Webview.Core

**Return value**

| Type | Description |
| :-- | :-- |
| number | 
If the display is normal, a non-negative integer is returned. Otherwise, **\-1** is returned.

Unit: vp.

 |

#### y9+

y(): number

Obtains the Y coordinate of the context menu.

**System capability**: SystemCapability.Web.Webview.Core

**Return value**

| Type | Description |
| :-- | :-- |
| number | 
If the display is normal, a non-negative integer is returned. Otherwise, **\-1** is returned.

Unit: vp.

 |

#### getLinkUrl9+

getLinkUrl(): string

Obtains the URL that has passed the security check.

**System capability**: SystemCapability.Web.Webview.Core

**Return value**

| Type | Description |
| :-- | :-- |
| string | If it is a link that is being long pressed, the URL that has passed the security check is returned. |

#### getUnfilteredLinkUrl9+

getUnfilteredLinkUrl(): string

Obtains the original URL.

**System capability**: SystemCapability.Web.Webview.Core

**Return value**

| Type | Description |
| :-- | :-- |
| string | If it is a link that is being long pressed, the original URL is returned. |

#### getSourceUrl9+

getSourceUrl(): string

Obtains the source URL.

**System capability**: SystemCapability.Web.Webview.Core

**Return value**

| Type | Description |
| :-- | :-- |
| string | If the selected element has the **src** attribute, the URL in the **src** is returned. The maximum size of the returned URL is 2 MB. If the size exceeds the upper limit, an empty string is returned. |

#### existsImageContents9+

existsImageContents(): boolean

Checks whether image content exists.

**System capability**: SystemCapability.Web.Webview.Core

**Return value**

| Type | Description |
| :-- | :-- |
| boolean | The value **true** means that there is image content in the element being long pressed, and **false** means the opposite. |

#### getMediaType9+

getMediaType(): ContextMenuMediaType

Obtains the media type of this web page element.

**System capability**: SystemCapability.Web.Webview.Core

**Return value**

| Type | Description |
| :-- | :-- |
| [ContextMenuMediaType](../enums/document.md#contextmenumediatype9) | Media type of the web page element. |

#### getSelectionText9+

getSelectionText(): string

Obtains the selected text.

**System capability**: SystemCapability.Web.Webview.Core

**Return value**

| Type | Description |
| :-- | :-- |
| string | Selected text for the context menu. If no text is selected, null is returned. |

#### getSourceType9+

getSourceType(): ContextMenuSourceType

Obtains the event source of the context menu.

**System capability**: SystemCapability.Web.Webview.Core

**Return value**

| Type | Description |
| :-- | :-- |
| [ContextMenuSourceType](../enums/document.md#contextmenusourcetype9) | Event source of the context menu. |

#### getInputFieldType9+

getInputFieldType(): ContextMenuInputFieldType

Obtains the input field type of this web page element.

**System capability**: SystemCapability.Web.Webview.Core

**Return value**

| Type | Description |
| :-- | :-- |
| [ContextMenuInputFieldType](../enums/document.md#contextmenuinputfieldtype9) | Input field type. |

#### isEditable9+

isEditable(): boolean

Checks whether this web page element is editable.

**System capability**: SystemCapability.Web.Webview.Core

**Return value**

| Type | Description |
| :-- | :-- |
| boolean | **true** is returned if the web page element is editable; otherwise, **false** is returned. |

#### getEditStateFlags9+

getEditStateFlags(): number

Obtains the edit state flag of this web page element.

**System capability**: SystemCapability.Web.Webview.Core

**Return value**

| Type | Description |
| :-- | :-- |
| number | Edit state flag of the web page element. For details, see [ContextMenuEditStateFlags](../enums/document.md#contextmenueditstateflags9). |

#### getPreviewWidth13+

getPreviewWidth(): number

Obtains the width of a preview image.

**System capability**: SystemCapability.Web.Webview.Core

**Return value**

| Type | Description |
| :-- | :-- |
| number | 
Width of a preview image.

Unit: vp.

 |

#### getPreviewHeight13+

getPreviewHeight(): number

Obtains the height of a preview image.

**System capability**: SystemCapability.Web.Webview.Core

**Return value**

| Type | Description |
| :-- | :-- |
| number | 
Height of a preview image.

Unit: vp.

 |

#### getContextMenuMediaType22+

getContextMenuMediaType(): ContextMenuDataMediaType

Obtains the type of the web page element that the user taps when the context menu event is reported.

**System capability**: SystemCapability.Web.Webview.Core

**Return value**

| Type | Description |
| :-- | :-- |
| [ContextMenuDataMediaType](../enums/document.md#contextmenudatamediatype22) | Media type of the web page element. |
