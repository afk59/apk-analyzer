# native\_interface\_accessibility.h

#### Overview

Declares the APIs for accessing Native Accessibility features.

**File to include**: <arkui/native\_interface\_accessibility.h>

**Library**: libace\_ndk.z.so

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Since**: 13

**Related module**: [ArkUI\_Accessibility](../../modules/arkui-accessibility/document.md)

**Sample**: [AccessibilityCapi](https://gitcode.com/openharmony/applications_app_samples/tree/master/code/DocsSample/ArkUISample/AccessibilityCapi)

#### Summary

#### \[h2\]Structs

| Name | typedef Keyword | Description |
| :-- | :-- | :-- |
| [ArkUI\_AccessibleAction](../../structs/arkui-accessibleaction/document.md) | ArkUI\_AccessibleAction | Defines a struct for accessibility actions. |
| [ArkUI\_AccessibleRect](../../structs/arkui-accessiblerect/document.md) | ArkUI\_AccessibleRect | Provides the bounding rectangle coordinates of the node. |
| [ArkUI\_AccessibleRangeInfo](../../structs/arkui-accessiblerangeinfo/document.md) | ArkUI\_AccessibleRangeInfo | Configures the current value, minimum value, and maximum value for specific components including **Slider**, **Rating**, and **Progress**. |
| [ArkUI\_AccessibleGridInfo](../../structs/arkui-accessiblegridinfo/document.md) | ArkUI\_AccessibleGridInfo | Configures the number of rows, number of columns, and selection mode for specific components including **List**, **Flex**, **Select**, and **Swiper**. |
| [ArkUI\_AccessibleGridItemInfo](../../structs/arkui-accessiblegriditeminfo/document.md) | ArkUI\_AccessibleGridItemInfo | Configures attributes for specific components including **List**, **Flex**, **Select**, and **Swiper**. |
| [ArkUI\_AccessibilityProviderCallbacks](../../structs/arkui-accessibilityprovidercallbacks/document.md) | ArkUI\_AccessibilityProviderCallbacks | Defines a struct for third-party accessibility provider callback functions, which third-party platforms need to implement. These functions are registered with the system side through **OH\_ArkUI\_AccessibilityProviderRegisterCallback**. |
| [ArkUI\_AccessibilityProviderCallbacksWithInstance](../../structs/arkui-accessibilityprovidercallbackswithinstance/document.md) | ArkUI\_AccessibilityProviderCallbacksWithInstance | Defines the callback function struct for third-party accessibility providers in multi-instance scenarios. These functions should be implemented by third-party platforms and registered with the system using **OH\_ArkUI\_AccessibilityProviderRegisterCallbackWithInstance**. |
| [ArkUI\_AccessibilityElementInfo](../../structs/arkui-accessibilityelementinfo/document.md) | ArkUI\_AccessibilityElementInfo | Provides accessibility node information for accessibility services and assistive applications (such as screen readers). |
| [ArkUI\_AccessibilityEventInfo](../../structs/arkui-accessibilityeventinfo/document.md) | ArkUI\_AccessibilityEventInfo | Describes the accessibility event information. After a component completes an action requested by an accessibility service or application, it needs to send a success event to confirm the operation. |
| [ArkUI\_AccessibilityProvider](../../structs/arkui-accessibilityprovider/document.md) | ArkUI\_AccessibilityProvider | Defines a third-party accessibility provider to implement callback functions. |
| [ArkUI\_AccessibilityActionArguments](../../structs/arkui-accessibilityactionarguments/document.md) | ArkUI\_AccessibilityActionArguments | Sets the parameters of accessibility actions. |
| [ArkUI\_AccessibilityElementInfoList](../../structs/arkui-accessibilityelementinfolist/document.md) | ArkUI\_AccessibilityElementInfoList | Provides a list instance of the encapsulated **ArkUI\_AccessibilityElementInfo**. |

#### \[h2\]Enums

| Name | typedef Keyword | Description |
| :-- | :-- | :-- |
| [ArkUI\_Accessibility\_ActionType](#arkui_accessibility_actiontype) | ArkUI\_Accessibility\_ActionType | Enumerates accessibility action types. |
| [ArkUI\_AccessibilityEventType](#arkui_accessibilityeventtype) | ArkUI\_AccessibilityEventType | Enumerates accessibility event types. |
| [ArkUI\_AcessbilityErrorCode](#arkui_acessbilityerrorcode) | ArkUI\_AcessbilityErrorCode | Enumerates accessibility error codes. |
| [ArkUI\_AccessibilitySearchMode](#arkui_accessibilitysearchmode) | ArkUI\_AccessibilitySearchMode | Enumerates accessibility search modes. |
| [ArkUI\_AccessibilityFocusType](#arkui_accessibilityfocustype) | ArkUI\_AccessibilityFocusType | Enumerates accessibility focus types. |
| [ArkUI\_AccessibilityFocusMoveDirection](#arkui_accessibilityfocusmovedirection) | ArkUI\_AccessibilityFocusMoveDirection | Enumerates accessibility focus movement directions. |

#### \[h2\]Functions

| Name | Description |
| :-- | :-- |
| [int32\_t OH\_ArkUI\_AccessibilityProviderRegisterCallback(ArkUI\_AccessibilityProvider\* provider, ArkUI\_AccessibilityProviderCallbacks\* callbacks)](#oh_arkui_accessibilityproviderregistercallback) | Defines a struct for third-party accessibility provider callback functions, which third-party platforms need to implement. These functions are registered with the system side through **OH\_ArkUI\_AccessibilityProviderRegisterCallback**. |
| [int32\_t OH\_ArkUI\_AccessibilityProviderRegisterCallbackWithInstance(const char\* instanceId,ArkUI\_AccessibilityProvider\* provider, ArkUI\_AccessibilityProviderCallbacksWithInstance\* callbacks)](#oh_arkui_accessibilityproviderregistercallbackwithinstance) | Registers accessibility provider callback functions for third-party platforms in multi-instance scenarios. |
| [void OH\_ArkUI\_SendAccessibilityAsyncEvent(ArkUI\_AccessibilityProvider\* provider, ArkUI\_AccessibilityEventInfo\* eventInfo,void (\*callback)(int32\_t errorCode))](#oh_arkui_sendaccessibilityasyncevent) | Proactively sends an event to notify the accessibility service. |
| [ArkUI\_AccessibilityElementInfo\* OH\_ArkUI\_AddAndGetAccessibilityElementInfo(ArkUI\_AccessibilityElementInfoList\* list)](#oh_arkui_addandgetaccessibilityelementinfo) | Adds an **ArkUI\_AccessibilityElementInfo** member to the specified list and returns the **ArkUI\_AccessibilityElementInfo** struct. |
| [int32\_t OH\_ArkUI\_AccessibilityElementInfoSetElementId(ArkUI\_AccessibilityElementInfo\* elementInfo, int32\_t elementId)](#oh_arkui_accessibilityelementinfosetelementid) | Sets the component ID for an **ArkUI\_AccessibilityElementInfo** object. |
| [int32\_t OH\_ArkUI\_AccessibilityElementInfoSetParentId(ArkUI\_AccessibilityElementInfo\* elementInfo, int32\_t parentId)](#oh_arkui_accessibilityelementinfosetparentid) | Sets the parent ID for an **ArkUI\_AccessibilityElementInfo** object. |
| [int32\_t OH\_ArkUI\_AccessibilityElementInfoSetComponentType(ArkUI\_AccessibilityElementInfo\* elementInfo, const char\* componentType)](#oh_arkui_accessibilityelementinfosetcomponenttype) | Sets the component type for the **ArkUI\_AccessibilityElementInfo** object. |
| [int32\_t OH\_ArkUI\_AccessibilityElementInfoSetContents(ArkUI\_AccessibilityElementInfo\* elementInfo, const char\* contents)](#oh_arkui_accessibilityelementinfosetcontents) | Sets the component text content for the **ArkUI\_AccessibilityElementInfo** object. |
| [int32\_t OH\_ArkUI\_AccessibilityElementInfoSetHintText(ArkUI\_AccessibilityElementInfo\* elementInfo, const char\* hintText)](#oh_arkui_accessibilityelementinfosethinttext) | Sets the hint text for an **ArkUI\_AccessibilityElementInfo** object. |
| [int32\_t OH\_ArkUI\_AccessibilityElementInfoSetAccessibilityText(ArkUI\_AccessibilityElementInfo\* elementInfo, const char\* accessibilityText)](#oh_arkui_accessibilityelementinfosetaccessibilitytext) | Sets the accessibility text for an **ArkUI\_AccessibilityElementInfo** object. |
| [int32\_t OH\_ArkUI\_AccessibilityElementInfoSetAccessibilityDescription(ArkUI\_AccessibilityElementInfo\* elementInfo, const char\* accessibilityDescription)](#oh_arkui_accessibilityelementinfosetaccessibilitydescription) | Sets the accessibility description for an **ArkUI\_AccessibilityElementInfo** object. |
| [int32\_t OH\_ArkUI\_AccessibilityElementInfoSetChildNodeIds(ArkUI\_AccessibilityElementInfo\* elementInfo, int32\_t childCount, int64\_t\* childNodeIds)](#oh_arkui_accessibilityelementinfosetchildnodeids) | Sets the child node count and IDs for an **ArkUI\_AccessibilityElementInfo** object. |
| [int32\_t OH\_ArkUI\_AccessibilityElementInfoSetOperationActions(ArkUI\_AccessibilityElementInfo\* elementInfo,int32\_t operationCount, ArkUI\_AccessibleAction\* operationActions)](#oh_arkui_accessibilityelementinfosetoperationactions) | Sets the supported operations for an **ArkUI\_AccessibilityElementInfo** object. |
| [int32\_t OH\_ArkUI\_AccessibilityElementInfoSetScreenRect(ArkUI\_AccessibilityElementInfo\* elementInfo, ArkUI\_AccessibleRect\* screenRect)](#oh_arkui_accessibilityelementinfosetscreenrect) | Sets the screen coordinates for an **ArkUI\_AccessibilityElementInfo** object. |
| [int32\_t OH\_ArkUI\_AccessibilityElementInfoSetCheckable(ArkUI\_AccessibilityElementInfo\* elementInfo, bool checkable)](#oh_arkui_accessibilityelementinfosetcheckable) | Sets whether the **ArkUI\_AccessibilityElementInfo** object is checkable. |
| [int32\_t OH\_ArkUI\_AccessibilityElementInfoSetChecked(ArkUI\_AccessibilityElementInfo\* elementInfo, bool checked)](#oh_arkui_accessibilityelementinfosetchecked) | Sets whether the **ArkUI\_AccessibilityElementInfo** object is checked. |
| [int32\_t OH\_ArkUI\_AccessibilityElementInfoSetFocusable(ArkUI\_AccessibilityElementInfo\* elementInfo, bool focusable)](#oh_arkui_accessibilityelementinfosetfocusable) | Sets whether the **ArkUI\_AccessibilityElementInfo** object is focusable. |
| [int32\_t OH\_ArkUI\_AccessibilityElementInfoSetFocused(ArkUI\_AccessibilityElementInfo\* elementInfo, bool isFocused)](#oh_arkui_accessibilityelementinfosetfocused) | Sets whether the **ArkUI\_AccessibilityElementInfo** object is focused. |
| [int32\_t OH\_ArkUI\_AccessibilityElementInfoSetVisible(ArkUI\_AccessibilityElementInfo\* elementInfo, bool isVisible)](#oh_arkui_accessibilityelementinfosetvisible) | Sets whether an **ArkUI\_AccessibilityElementInfo** object is visible. |
| [int32\_t OH\_ArkUI\_AccessibilityElementInfoSetAccessibilityFocused(ArkUI\_AccessibilityElementInfo\* elementInfo, bool accessibilityFocused)](#oh_arkui_accessibilityelementinfosetaccessibilityfocused) | Sets whether the element is focused for accessibility purposes for an **ArkUI\_AccessibilityElementInfo** object. |
| [int32\_t OH\_ArkUI\_AccessibilityElementInfoSetSelected(ArkUI\_AccessibilityElementInfo\* elementInfo, bool selected)](#oh_arkui_accessibilityelementinfosetselected) | Sets whether the **ArkUI\_AccessibilityElementInfo** object is selected. |
| [int32\_t OH\_ArkUI\_AccessibilityElementInfoSetClickable(ArkUI\_AccessibilityElementInfo\* elementInfo, bool clickable)](#oh_arkui_accessibilityelementinfosetclickable) | Sets whether the **ArkUI\_AccessibilityElementInfo** object is clickable. |
| [int32\_t OH\_ArkUI\_AccessibilityElementInfoSetLongClickable(ArkUI\_AccessibilityElementInfo\* elementInfo, bool longClickable)](#oh_arkui_accessibilityelementinfosetlongclickable) | Sets whether the **ArkUI\_AccessibilityElementInfo** object supports long-press gestures. |
| [int32\_t OH\_ArkUI\_AccessibilityElementInfoSetEnabled(ArkUI\_AccessibilityElementInfo\* elementInfo, bool isEnabled)](#oh_arkui_accessibilityelementinfosetenabled) | Sets whether the **ArkUI\_AccessibilityElementInfo** object is enabled. |
| [int32\_t OH\_ArkUI\_AccessibilityElementInfoSetIsPassword(ArkUI\_AccessibilityElementInfo\* elementInfo, bool isPassword)](#oh_arkui_accessibilityelementinfosetispassword) | Sets whether the **ArkUI\_AccessibilityElementInfo** object is a password. |
| [int32\_t OH\_ArkUI\_AccessibilityElementInfoSetScrollable(ArkUI\_AccessibilityElementInfo\* elementInfo, bool scrollable)](#oh_arkui_accessibilityelementinfosetscrollable) | Sets whether the **ArkUI\_AccessibilityElementInfo** object is scrollable. |
| [int32\_t OH\_ArkUI\_AccessibilityElementInfoSetEditable(ArkUI\_AccessibilityElementInfo\* elementInfo, bool editable)](#oh_arkui_accessibilityelementinfoseteditable) | Sets whether the **ArkUI\_AccessibilityElementInfo** object is editable. |
| [int32\_t OH\_ArkUI\_AccessibilityElementInfoSetIsHint(ArkUI\_AccessibilityElementInfo\* elementInfo, bool isHint)](#oh_arkui_accessibilityelementinfosetishint) | Sets the hint status for an **ArkUI\_AccessibilityElementInfo** object. |
| [int32\_t OH\_ArkUI\_AccessibilityElementInfoSetRangeInfo(ArkUI\_AccessibilityElementInfo\* elementInfo, ArkUI\_AccessibleRangeInfo\* rangeInfo)](#oh_arkui_accessibilityelementinfosetrangeinfo) | Sets the range information for an **ArkUI\_AccessibilityElementInfo** object. |
| [int32\_t OH\_ArkUI\_AccessibilityElementInfoSetGridInfo(ArkUI\_AccessibilityElementInfo\* elementInfo, ArkUI\_AccessibleGridInfo\* gridInfo)](#oh_arkui_accessibilityelementinfosetgridinfo) | Sets the grid information for an **ArkUI\_AccessibilityElementInfo** object. |
| [int32\_t OH\_ArkUI\_AccessibilityElementInfoSetGridItemInfo(ArkUI\_AccessibilityElementInfo\* elementInfo, ArkUI\_AccessibleGridItemInfo\* gridItem)](#oh_arkui_accessibilityelementinfosetgriditeminfo) | Sets a single-item container within a grid container for an **ArkUI\_AccessibilityElementInfo** object. |
| [int32\_t OH\_ArkUI\_AccessibilityElementInfoSetSelectedTextStart(ArkUI\_AccessibilityElementInfo\* elementInfo, int32\_t selectedTextStart)](#oh_arkui_accessibilityelementinfosetselectedtextstart) | Sets the start position of the selected text for an **ArkUI\_AccessibilityElementInfo** object. |
| [int32\_t OH\_ArkUI\_AccessibilityElementInfoSetSelectedTextEnd(ArkUI\_AccessibilityElementInfo\* elementInfo, int32\_t selectedTextEnd)](#oh_arkui_accessibilityelementinfosetselectedtextend) | Sets the end position of the selected text for an **ArkUI\_AccessibilityElementInfo** object. |
| [int32\_t OH\_ArkUI\_AccessibilityElementInfoSetCurrentItemIndex(ArkUI\_AccessibilityElementInfo\* elementInfo, int32\_t currentItemIndex)](#oh_arkui_accessibilityelementinfosetcurrentitemindex) | Sets the position information of the currently focused component for an **ArkUI\_AccessibilityElementInfo** object. |
| [int32\_t OH\_ArkUI\_AccessibilityElementInfoSetStartItemIndex(ArkUI\_AccessibilityElementInfo\* elementInfo, int32\_t startItemIndex)](#oh_arkui_accessibilityelementinfosetstartitemindex) | Sets the position information of the first element displayed on the current screen for an **ArkUI\_AccessibilityElementInfo** object. |
| [int32\_t OH\_ArkUI\_AccessibilityElementInfoSetEndItemIndex(ArkUI\_AccessibilityElementInfo\* elementInfo, int32\_t endItemIndex)](#oh_arkui_accessibilityelementinfosetenditemindex) | Sets the position information of the last element displayed on the current screen for an **ArkUI\_AccessibilityElementInfo** object. |
| [int32\_t OH\_ArkUI\_AccessibilityElementInfoSetItemCount(ArkUI\_AccessibilityElementInfo\* elementInfo, int32\_t itemCount)](#oh_arkui_accessibilityelementinfosetitemcount) | Sets the total number of elements of a specific component for an **ArkUI\_AccessibilityElementInfo** object. |
| [int32\_t OH\_ArkUI\_AccessibilityElementInfoSetAccessibilityOffset(ArkUI\_AccessibilityElementInfo\* elementInfo, int32\_t offset)](#oh_arkui_accessibilityelementinfosetaccessibilityoffset) | Sets the scrolling pixel offset of the content area relative to the top coordinate of the element for an **ArkUI\_AccessibilityElementInfo** object. |
| [int32\_t OH\_ArkUI\_AccessibilityElementInfoSetAccessibilityGroup(ArkUI\_AccessibilityElementInfo\* elementInfo, bool accessibilityGroup)](#oh_arkui_accessibilityelementinfosetaccessibilitygroup) | Sets whether the **ArkUI\_AccessibilityElementInfo** object should be treated as an accessibility group. |
| [int32\_t OH\_ArkUI\_AccessibilityElementInfoSetAccessibilityLevel(ArkUI\_AccessibilityElementInfo\* elementInfo, const char\* accessibilityLevel)](#oh_arkui_accessibilityelementinfosetaccessibilitylevel) | Sets the accessibility level for the **ArkUI\_AccessibilityElementInfo** object. |
| [int32\_t OH\_ArkUI\_AccessibilityElementInfoSetZIndex(ArkUI\_AccessibilityElementInfo\* elementInfo, int32\_t zIndex)](#oh_arkui_accessibilityelementinfosetzindex) | Sets the z-order of the component for the **ArkUI\_AccessibilityElementInfo** object. |
| [int32\_t OH\_ArkUI\_AccessibilityElementInfoSetAccessibilityOpacity(ArkUI\_AccessibilityElementInfo\* elementInfo, float opacity)](#oh_arkui_accessibilityelementinfosetaccessibilityopacity) | Sets the opacity for the **ArkUI\_AccessibilityElementInfo** object. |
| [int32\_t OH\_ArkUI\_AccessibilityElementInfoSetBackgroundColor(ArkUI\_AccessibilityElementInfo\* elementInfo, const char\* backgroundColor)](#oh_arkui_accessibilityelementinfosetbackgroundcolor) | Sets the background color for the **ArkUI\_AccessibilityElementInfo** object. |
| [int32\_t OH\_ArkUI\_AccessibilityElementInfoSetBackgroundImage(ArkUI\_AccessibilityElementInfo\* elementInfo, const char\* backgroundImage)](#oh_arkui_accessibilityelementinfosetbackgroundimage) | Sets the background image for the **ArkUI\_AccessibilityElementInfo** object. |
| [int32\_t OH\_ArkUI\_AccessibilityElementInfoSetBlur(ArkUI\_AccessibilityElementInfo\* elementInfo, const char\* blur)](#oh_arkui_accessibilityelementinfosetblur) | Sets the blur value for the **ArkUI\_AccessibilityElementInfo** object. |
| [int32\_t OH\_ArkUI\_AccessibilityElementInfoSetHitTestBehavior(ArkUI\_AccessibilityElementInfo\* elementInfo, const char\* hitTestBehavior)](#oh_arkui_accessibilityelementinfosethittestbehavior) | Sets the response logic and node blocking rules for the hit test for an **ArkUI\_AccessibilityElementInfo** object. |
| [ArkUI\_AccessibilityElementInfo\* OH\_ArkUI\_CreateAccessibilityElementInfo(void)](#oh_arkui_createaccessibilityelementinfo) | Creates an **ArkUI\_AccessibilityElementInfo** object, which must be destroyed with **OH\_ArkUI\_DestoryAccessibilityElementInfo**. |
| [void OH\_ArkUI\_DestoryAccessibilityElementInfo(ArkUI\_AccessibilityElementInfo\* elementInfo)](#oh_arkui_destoryaccessibilityelementinfo) | Destroys an **ArkUI\_AccessibilityElementInfo** object. |
| [ArkUI\_AccessibilityEventInfo\* OH\_ArkUI\_CreateAccessibilityEventInfo(void)](#oh_arkui_createaccessibilityeventinfo) | Creates an **ArkUI\_AccessibilityEventInfo** object, which must be destroyed with **OH\_ArkUI\_DestoryAccessibilityEventInfo**. |
| [void OH\_ArkUI\_DestoryAccessibilityEventInfo(ArkUI\_AccessibilityEventInfo\* eventInfo)](#oh_arkui_destoryaccessibilityeventinfo) | Destroys an **ArkUI\_AccessibilityEventInfo** object. |
| [int32\_t OH\_ArkUI\_AccessibilityEventSetEventType(ArkUI\_AccessibilityEventInfo\* eventInfo, ArkUI\_AccessibilityEventType eventType)](#oh_arkui_accessibilityeventseteventtype) | Sets the event type for an **ArkUI\_AccessibilityEventInfo** object. |
| [int32\_t OH\_ArkUI\_AccessibilityEventSetTextAnnouncedForAccessibility(ArkUI\_AccessibilityEventInfo\* eventInfo, const char\* textAnnouncedForAccessibility)](#oh_arkui_accessibilityeventsettextannouncedforaccessibility) | Sets the content for auto-broadcasting for the **ArkUI\_AccessibilityEventInfo** object. |
| [int32\_t OH\_ArkUI\_AccessibilityEventSetRequestFocusId(ArkUI\_AccessibilityEventInfo\* eventInfo, int32\_t requestFocusId)](#oh_arkui_accessibilityeventsetrequestfocusid) | Sets the focus request ID for an **ArkUI\_AccessibilityEventInfo** object. |
| [int32\_t OH\_ArkUI\_AccessibilityEventSetElementInfo(ArkUI\_AccessibilityEventInfo\* eventInfo, ArkUI\_AccessibilityElementInfo\* elementInfo)](#oh_arkui_accessibilityeventsetelementinfo) | Sets the element information for an **ArkUI\_AccessibilityEventInfo** object. |
| [int32\_t OH\_ArkUI\_FindAccessibilityActionArgumentByKey(ArkUI\_AccessibilityActionArguments\* arguments, const char\* key, char\*\* value)](#oh_arkui_findaccessibilityactionargumentbykey) | Obtains the value associated with the specified key in **ArkUI\_AccessibilityActionArguments**. |

#### Enum Description

#### \[h2\]ArkUI\_Accessibility\_ActionType

enum ArkUI\_Accessibility\_ActionType

**Description**

Enumerates accessibility action types.

**Since**: 13

| Value | Description |
| :-- | :-- |
| ARKUI\_ACCESSIBILITY\_NATIVE\_ACTION\_TYPE\_INVALID = 0 | Invalid value. |
| ARKUI\_ACCESSIBILITY\_NATIVE\_ACTION\_TYPE\_CLICK = 0x00000010 | Triggers the component's click event handling. |
| ARKUI\_ACCESSIBILITY\_NATIVE\_ACTION\_TYPE\_LONG\_CLICK = 0x00000020 | Triggers the component's long-click event handling. |
| ARKUI\_ACCESSIBILITY\_NATIVE\_ACTION\_TYPE\_GAIN\_ACCESSIBILITY\_FOCUS = 0x00000040 | Requests accessibility focus for the component. |
| ARKUI\_ACCESSIBILITY\_NATIVE\_ACTION\_TYPE\_CLEAR\_ACCESSIBILITY\_FOCUS = 0x00000080 | Clears accessibility focus from the component. |
| ARKUI\_ACCESSIBILITY\_NATIVE\_ACTION\_TYPE\_SCROLL\_FORWARD = 0x00000100 | Initiates forward scrolling in scrollable containers. |
| ARKUI\_ACCESSIBILITY\_NATIVE\_ACTION\_TYPE\_SCROLL\_BACKWARD = 0x00000200 | Initiates backward scrolling in scrollable containers. |
| ARKUI\_ACCESSIBILITY\_NATIVE\_ACTION\_TYPE\_COPY = 0x00000400 | Copies the current text selection. |
| ARKUI\_ACCESSIBILITY\_NATIVE\_ACTION\_TYPE\_PASTE = 0x00000800 | Pastes content to the text component. |
| ARKUI\_ACCESSIBILITY\_NATIVE\_ACTION\_TYPE\_CUT = 0x00001000 | Cuts the current text selection to the pasteboard. |
| ARKUI\_ACCESSIBILITY\_NATIVE\_ACTION\_TYPE\_SELECT\_TEXT = 0x00002000 | Selects a range of text within an editable area in a text component. Selects a range of text within an editable area by using **ArkUI\_AccessibilityActionArguments** and setting **selectTextBegin** (indicates the start position of the selection), **selectTextEnd** (indicates the end position of the selection), and **selectTextInForWard** (**true** indicates to select text forward, and **false** indicates to select text backward). |
| ARKUI\_ACCESSIBILITY\_NATIVE\_ACTION\_TYPE\_SET\_TEXT = 0x00004000 | Sets the text content of the text component. |
| ARKUI\_ACCESSIBILITY\_NATIVE\_ACTION\_TYPE\_SET\_CURSOR\_POSITION = 0x00100000 | Sets the cursor position where the text can be entered for the text component. This API is used together with **ArkUI\_AccessibilityActionArguments**. |
| ARKUI\_ACCESSIBILITY\_NATIVE\_ACTION\_TYPE\_NEXT\_HTML\_ITEM = 0x02000000 | 
Moves focus to the next focusable component. Note: "HTML" indicates the web-like navigation capability, not actual web elements. This attribute is available only when the [findNextFocusAccessibilityNode](../../structs/arkui-accessibilityprovidercallbacks/document.md#findnextfocusaccessibilitynode) capability is implemented.

**Since**: 15

 |
| ARKUI\_ACCESSIBILITY\_NATIVE\_ACTION\_TYPE\_PREVIOUS\_HTML\_ITEM = 0x04000000 | 

Moves focus to the previous focusable component. Note: "HTML" indicates the web-like navigation capability, not actual web elements. This API requires implementation of **findNextFocusAccessibilityNode**.

**Since**: 15

 |

#### \[h2\]ArkUI\_AccessibilityEventType

enum ArkUI\_AccessibilityEventType

**Description**

Enumerates accessibility event types.

**Since**: 13

| Value | Description |
| :-- | :-- |
| ARKUI\_ACCESSIBILITY\_NATIVE\_EVENT\_TYPE\_INVALID = 0 | Invalid value. |
| ARKUI\_ACCESSIBILITY\_NATIVE\_EVENT\_TYPE\_CLICKED = 0x00000001 | Click event, sent after the UI component responds. |
| ARKUI\_ACCESSIBILITY\_NATIVE\_EVENT\_TYPE\_LONG\_CLICKED = 0x00000002 | Long-click event, sent after the UI component responds. |
| ARKUI\_ACCESSIBILITY\_NATIVE\_EVENT\_TYPE\_SELECTED = 0x00000004 | Selection event, sent after the UI component responds. |
| ARKUI\_ACCESSIBILITY\_NATIVE\_EVENT\_TYPE\_TEXT\_UPDATE = 0x00000010 | Text update event, sent when text is updated. |
| ARKUI\_ACCESSIBILITY\_NATIVE\_EVENT\_TYPE\_PAGE\_STATE\_UPDATE = 0x00000020 | Page state update event, sent on page navigation, switching, resizing, or movement. |
| ARKUI\_ACCESSIBILITY\_NATIVE\_EVENT\_TYPE\_PAGE\_CONTENT\_UPDATE = 0x00000800 | Page content update event, sent when the page content changes. |
| ARKUI\_ACCESSIBILITY\_NATIVE\_EVENT\_TYPE\_SCROLLED = 0x000001000 | Scroll event, sent when scrolling occurs on scrollable components. |
| ARKUI\_ACCESSIBILITY\_NATIVE\_EVENT\_TYPE\_ACCESSIBILITY\_FOCUSED = 0x00008000 | Accessibility focus event, sent after the UI component receives focus. |
| ARKUI\_ACCESSIBILITY\_NATIVE\_EVENT\_TYPE\_ACCESSIBILITY\_FOCUS\_CLEARED = 0x00010000 | Accessibility focus cleared event, sent after the UI component loses focus. |
| ARKUI\_ACCESSIBILITY\_NATIVE\_EVENT\_TYPE\_REQUEST\_ACCESSIBILITY\_FOCUS = 0x02000000 | Event to actively requests focus for the specified node. |
| ARKUI\_ACCESSIBILITY\_NATIVE\_EVENT\_TYPE\_PAGE\_OPEN = 0x20000000 | Page open event reported by the UI component. |
| ARKUI\_ACCESSIBILITY\_NATIVE\_EVENT\_TYPE\_PAGE\_CLOSE = 0x08000000 | Page close event reported by the UI component. |
| ARKUI\_ACCESSIBILITY\_NATIVE\_EVENT\_TYPE\_ANNOUNCE\_FOR\_ACCESSIBILITY = 0x10000000 | Announcement event, indicating a request to proactively announce specified content. |
| ARKUI\_ACCESSIBILITY\_NATIVE\_EVENT\_TYPE\_FOCUS\_NODE\_UPDATE = 0x10000001 | Focus update event, used in the focus update scenarios. |

#### \[h2\]ArkUI\_AcessbilityErrorCode

enum ArkUI\_AcessbilityErrorCode

**Description**

Enumerates accessibility error codes.

**Since**: 13

| Value | Description |
| :-- | :-- |
| ARKUI\_ACCESSIBILITY\_NATIVE\_RESULT\_SUCCESSFUL = 0 | The operation is successful. |
| ARKUI\_ACCESSIBILITY\_NATIVE\_RESULT\_FAILED = -1 | The operation failed. |
| ARKUI\_ACCESSIBILITY\_NATIVE\_RESULT\_BAD\_PARAMETER = -2 | Invalid parameter. |
| ARKUI\_ACCESSIBILITY\_NATIVE\_RESULT\_OUT\_OF\_MEMORY = -3 | Insufficient memory. |

#### \[h2\]ArkUI\_AccessibilitySearchMode

enum ArkUI\_AccessibilitySearchMode

**Description**

Enumerates accessibility search modes.

**Since**: 13

| Value | Description |
| :-- | :-- |
| ARKUI\_ACCESSIBILITY\_NATIVE\_SEARCH\_MODE\_PREFETCH\_CURRENT = 0 | Searches the current node. |
| ARKUI\_ACCESSIBILITY\_NATIVE\_SEARCH\_MODE\_PREFETCH\_PREDECESSORS = 1 << 0 | Searches parent nodes. |
| ARKUI\_ACCESSIBILITY\_NATIVE\_SEARCH\_MODE\_PREFETCH\_SIBLINGS = 1 << 1 | Searches sibling nodes. |
| ARKUI\_ACCESSIBILITY\_NATIVE\_SEARCH\_MODE\_PREFETCH\_CHILDREN = 1 << 2 | Searches immediate child nodes. |
| ARKUI\_ACCESSIBILITY\_NATIVE\_SEARCH\_MODE\_PREFETCH\_RECURSIVE\_CHILDREN = 1 << 3 | Searches all child nodes. |

#### \[h2\]ArkUI\_AccessibilityFocusType

enum ArkUI\_AccessibilityFocusType

**Description**

Enumerates accessibility focus types.

**Since**: 13

| Value | Description |
| :-- | :-- |
| ARKUI\_ACCESSIBILITY\_NATIVE\_FOCUS\_TYPE\_INVALID = -1 | Invalid value. |
| ARKUI\_ACCESSIBILITY\_NATIVE\_FOCUS\_TYPE\_INPUT = 1 << 0 | Input focus type. |
| ARKUI\_ACCESSIBILITY\_NATIVE\_FOCUS\_TYPE\_ACCESSIBILITY = 1 << 1 | Accessibility focus type. |

#### \[h2\]ArkUI\_AccessibilityFocusMoveDirection

enum ArkUI\_AccessibilityFocusMoveDirection

**Description**

Enumerates accessibility focus movement directions.

**Since**: 13

| Value | Description |
| :-- | :-- |
| ARKUI\_ACCESSIBILITY\_NATIVE\_DIRECTION\_INVALID = 0 | Invalid value. |
| ARKUI\_ACCESSIBILITY\_NATIVE\_DIRECTION\_UP = 0x00000001 | Moves focus up. |
| ARKUI\_ACCESSIBILITY\_NATIVE\_DIRECTION\_DOWN = 0x00000002 | Moves focus down. |
| ARKUI\_ACCESSIBILITY\_NATIVE\_DIRECTION\_LEFT = 0x00000004 | Moves focus left. |
| ARKUI\_ACCESSIBILITY\_NATIVE\_DIRECTION\_RIGHT = 0x00000008 | Moves focus right. |
| ARKUI\_ACCESSIBILITY\_NATIVE\_DIRECTION\_FORWARD = 0x00000010 | Moves focus to the next focusable node (relative to the reference node in query). |
| ARKUI\_ACCESSIBILITY\_NATIVE\_DIRECTION\_BACKWARD = 0x00000020 | Moves focus to the previous focusable node (relative to the reference node in query). |

#### Function Description

#### \[h2\]OH\_ArkUI\_AccessibilityProviderRegisterCallback()

int32\_t OH\_ArkUI\_AccessibilityProviderRegisterCallback(ArkUI\_AccessibilityProvider\* provider, ArkUI\_AccessibilityProviderCallbacks\* callbacks)

**Description**

Defines a struct for third-party accessibility provider callback functions, which third-party platforms need to implement. These functions are registered with the system side through **OH\_ArkUI\_AccessibilityProviderRegisterCallback**.

**Since**: 13

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_AccessibilityProvider](../../structs/arkui-accessibilityprovider/document.md)\* provider | Pointer to an **ArkUI\_AccessibilityProvider** instance. |
| [ArkUI\_AccessibilityProviderCallbacks](../../structs/arkui-accessibilityprovidercallbacks/document.md)\* callbacks | Pointer to an **ArkUI\_AccessibilityProviderCallbacks** struct that contains the set of callback functions implemented by the third-party platform. |

**Returns**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Returns [ARKUI\_ACCESSIBILITY\_NATIVE\_RESULT\_SUCCESSFUL](#arkui_acessbilityerrorcode) if the operation is successful.

Returns [ARKUI\_ACCESSIBILITY\_NATIVE\_RESULT\_BAD\_PARAMETER](#arkui_acessbilityerrorcode) if a parameter error occurs.

 |

#### \[h2\]OH\_ArkUI\_AccessibilityProviderRegisterCallbackWithInstance()

int32\_t OH\_ArkUI\_AccessibilityProviderRegisterCallbackWithInstance(const char\* instanceId, ArkUI\_AccessibilityProvider\* provider, ArkUI\_AccessibilityProviderCallbacksWithInstance\* callbacks)

**Description**

Registers accessibility provider callback functions for third-party platforms in multi-instance scenarios.

**Since**: 15

**Parameters**

| Name | Description |
| :-- | :-- |
| const char\* instanceId | Pointer to the instance ID for third-party platform integration, used to distinguish between different instances in multi-instance scenarios. The ID is assigned and maintained by the third-party platform. |
| [ArkUI\_AccessibilityProvider](../../structs/arkui-accessibilityprovider/document.md)\* provider | Handle to the third-party platform provider. |
| [ArkUI\_AccessibilityProviderCallbacksWithInstance](../../structs/arkui-accessibilityprovidercallbackswithinstance/document.md)\* callbacks | Pointer to an **ArkUI\_AccessibilityProviderCallbacksWithInstance** instance. |

**Returns**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Returns [ARKUI\_ACCESSIBILITY\_NATIVE\_RESULT\_SUCCESSFUL](#arkui_acessbilityerrorcode) if the operation is successful.

Returns [ARKUI\_ACCESSIBILITY\_NATIVE\_RESULT\_BAD\_PARAMETER](#arkui_acessbilityerrorcode) if a parameter error occurs.

 |

#### \[h2\]OH\_ArkUI\_SendAccessibilityAsyncEvent()

void OH\_ArkUI\_SendAccessibilityAsyncEvent(ArkUI\_AccessibilityProvider\* provider, ArkUI\_AccessibilityEventInfo\* eventInfo, void (\*callback)(int32\_t errorCode))

**Description**

Proactively sends an event to notify the accessibility service.

**Since**: 13

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_AccessibilityProvider](../../structs/arkui-accessibilityprovider/document.md)\* provider | Handle to the third-party platform provider. |
| [ArkUI\_AccessibilityEventInfo](../../structs/arkui-accessibilityeventinfo/document.md)\* eventInfo | Pointer to the accessibility event information. |
| void (\*callback)(int32\_t errorCode) | Callback that receives the asynchronous operation result. |

#### \[h2\]OH\_ArkUI\_AddAndGetAccessibilityElementInfo()

ArkUI\_AccessibilityElementInfo\* OH\_ArkUI\_AddAndGetAccessibilityElementInfo(ArkUI\_AccessibilityElementInfoList\* list)

**Description**

Adds an **ArkUI\_AccessibilityElementInfo** member to the specified list and returns the **ArkUI\_AccessibilityElementInfo** struct.

**Since**: 13

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_AccessibilityElementInfoList](../../structs/arkui-accessibilityelementinfolist/document.md)\* list | **ArkUI\_AccessibilityElementInfoList** struct to which the newly created **ArkUI\_AccessibilityElementInfo** member is added and then returned to the function caller. |

**Returns**

| Type | Description |
| :-- | :-- |
| [ArkUI\_AccessibilityElementInfo](../../structs/arkui-accessibilityelementinfo/document.md)\* | Pointer to the created **ArkUI\_AccessibilityElementInfo** struct; returns **NULL** if creation fails. |

#### \[h2\]OH\_ArkUI\_AccessibilityElementInfoSetElementId()

int32\_t OH\_ArkUI\_AccessibilityElementInfoSetElementId(ArkUI\_AccessibilityElementInfo\* elementInfo, int32\_t elementId)

**Description**

Sets the component ID for an **ArkUI\_AccessibilityElementInfo** object.

**Since**: 13

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_AccessibilityElementInfo](../../structs/arkui-accessibilityelementinfo/document.md)\* elementInfo | Pointer to an **ArkUI\_AccessibilityElementInfo** object. |
| int32\_t elementId | Unique ID of the accessibility element. |

**Returns**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Returns [ARKUI\_ACCESSIBILITY\_NATIVE\_RESULT\_SUCCESSFUL](#arkui_acessbilityerrorcode) if the operation is successful.

Returns [ARKUI\_ACCESSIBILITY\_NATIVE\_RESULT\_BAD\_PARAMETER](#arkui_acessbilityerrorcode) if a parameter error occurs.

 |

#### \[h2\]OH\_ArkUI\_AccessibilityElementInfoSetParentId()

int32\_t OH\_ArkUI\_AccessibilityElementInfoSetParentId(ArkUI\_AccessibilityElementInfo\* elementInfo, int32\_t parentId)

**Description**

Sets the parent ID for an **ArkUI\_AccessibilityElementInfo** object.

**Since**: 13

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_AccessibilityElementInfo](../../structs/arkui-accessibilityelementinfo/document.md)\* elementInfo | Pointer to the target **ArkUI\_AccessibilityElementInfo** object. |
| int32\_t parentId | Accessibility ID of the element's parent component. |

**Returns**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Returns [ARKUI\_ACCESSIBILITY\_NATIVE\_RESULT\_SUCCESSFUL](#arkui_acessbilityerrorcode) if the operation is successful.

Returns [ARKUI\_ACCESSIBILITY\_NATIVE\_RESULT\_BAD\_PARAMETER](#arkui_acessbilityerrorcode) if a parameter error occurs.

 |

#### \[h2\]OH\_ArkUI\_AccessibilityElementInfoSetComponentType()

int32\_t OH\_ArkUI\_AccessibilityElementInfoSetComponentType(ArkUI\_AccessibilityElementInfo\* elementInfo, const char\* componentType)

**Description**

Sets the component type for the **ArkUI\_AccessibilityElementInfo** object.

**Since**: 13

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_AccessibilityElementInfo](../../structs/arkui-accessibilityelementinfo/document.md)\* elementInfo | Pointer to the target **ArkUI\_AccessibilityElementInfo** object. |
| const char\* componentType | Pointer to the component type of the element. |

**Returns**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Returns [ARKUI\_ACCESSIBILITY\_NATIVE\_RESULT\_SUCCESSFUL](#arkui_acessbilityerrorcode) if the operation is successful.

Returns [ARKUI\_ACCESSIBILITY\_NATIVE\_RESULT\_BAD\_PARAMETER](#arkui_acessbilityerrorcode) if a parameter error occurs.

 |

#### \[h2\]OH\_ArkUI\_AccessibilityElementInfoSetContents()

int32\_t OH\_ArkUI\_AccessibilityElementInfoSetContents(ArkUI\_AccessibilityElementInfo\* elementInfo, const char\* contents)

**Description**

Sets the component text content for the **ArkUI\_AccessibilityElementInfo** object.

**Since**: 13

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_AccessibilityElementInfo](../../structs/arkui-accessibilityelementinfo/document.md)\* elementInfo | Pointer to the target **ArkUI\_AccessibilityElementInfo** object. |
| const char\* contents | Pointer to the text content recognized by accessibility services for the element. |

**Returns**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Returns [ARKUI\_ACCESSIBILITY\_NATIVE\_RESULT\_SUCCESSFUL](#arkui_acessbilityerrorcode) if the operation is successful.

Returns [ARKUI\_ACCESSIBILITY\_NATIVE\_RESULT\_BAD\_PARAMETER](#arkui_acessbilityerrorcode) if a parameter error occurs.

 |

#### \[h2\]OH\_ArkUI\_AccessibilityElementInfoSetHintText()

int32\_t OH\_ArkUI\_AccessibilityElementInfoSetHintText(ArkUI\_AccessibilityElementInfo\* elementInfo, const char\* hintText)

**Description**

Sets the hint text for an **ArkUI\_AccessibilityElementInfo** object.

**Since**: 13

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_AccessibilityElementInfo](../../structs/arkui-accessibilityelementinfo/document.md)\* elementInfo | Pointer to the target **ArkUI\_AccessibilityElementInfo** object. |
| const char\* hintText | Pointer to the hint text. The default value is **""**. |

**Returns**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Returns [ARKUI\_ACCESSIBILITY\_NATIVE\_RESULT\_SUCCESSFUL](#arkui_acessbilityerrorcode) if the operation is successful.

Returns [ARKUI\_ACCESSIBILITY\_NATIVE\_RESULT\_BAD\_PARAMETER](#arkui_acessbilityerrorcode) if a parameter error occurs.

 |

#### \[h2\]OH\_ArkUI\_AccessibilityElementInfoSetAccessibilityText()

int32\_t OH\_ArkUI\_AccessibilityElementInfoSetAccessibilityText(ArkUI\_AccessibilityElementInfo\* elementInfo, const char\* accessibilityText)

**Description**

Sets the accessibility text for an **ArkUI\_AccessibilityElementInfo** object.

**Since**: 13

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_AccessibilityElementInfo](../../structs/arkui-accessibilityelementinfo/document.md)\* elementInfo | Pointer to the target **ArkUI\_AccessibilityElementInfo** object. |
| const char\* accessibilityText | Pointer to the accessibility text. The default value is **""**. |

**Returns**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Returns [ARKUI\_ACCESSIBILITY\_NATIVE\_RESULT\_SUCCESSFUL](#arkui_acessbilityerrorcode) if the operation is successful.

Returns [ARKUI\_ACCESSIBILITY\_NATIVE\_RESULT\_BAD\_PARAMETER](#arkui_acessbilityerrorcode) if a parameter error occurs.

 |

#### \[h2\]OH\_ArkUI\_AccessibilityElementInfoSetAccessibilityDescription()

int32\_t OH\_ArkUI\_AccessibilityElementInfoSetAccessibilityDescription(ArkUI\_AccessibilityElementInfo\* elementInfo, const char\* accessibilityDescription)

**Description**

Sets the accessibility description for an **ArkUI\_AccessibilityElementInfo** object.

**Since**: 13

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_AccessibilityElementInfo](../../structs/arkui-accessibilityelementinfo/document.md)\* elementInfo | Pointer to the target **ArkUI\_AccessibilityElementInfo** object. |
| const char\* accessibilityDescription | Pointer to the accessibility description. The default value is **""**. |

**Returns**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Returns [ARKUI\_ACCESSIBILITY\_NATIVE\_RESULT\_SUCCESSFUL](#arkui_acessbilityerrorcode) if the operation is successful.

Returns [ARKUI\_ACCESSIBILITY\_NATIVE\_RESULT\_BAD\_PARAMETER](#arkui_acessbilityerrorcode) if a parameter error occurs.

 |

#### \[h2\]OH\_ArkUI\_AccessibilityElementInfoSetChildNodeIds()

int32\_t OH\_ArkUI\_AccessibilityElementInfoSetChildNodeIds(ArkUI\_AccessibilityElementInfo\* elementInfo, int32\_t childCount, int64\_t\* childNodeIds)

**Description**

Sets the child node count and IDs for an **ArkUI\_AccessibilityElementInfo** object.

**Since**: 13

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_AccessibilityElementInfo](../../structs/arkui-accessibilityelementinfo/document.md)\* elementInfo | Pointer to the target **ArkUI\_AccessibilityElementInfo** object. |
| int32\_t childCount | Child node count. The default value is **0**. |
| int64\_t\* childNodeIds | Pointer to the array of child node IDs. |

**Returns**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Returns [ARKUI\_ACCESSIBILITY\_NATIVE\_RESULT\_SUCCESSFUL](#arkui_acessbilityerrorcode) if the operation is successful.

Returns [ARKUI\_ACCESSIBILITY\_NATIVE\_RESULT\_BAD\_PARAMETER](#arkui_acessbilityerrorcode) if a parameter error occurs.

 |

#### \[h2\]OH\_ArkUI\_AccessibilityElementInfoSetOperationActions()

int32\_t OH\_ArkUI\_AccessibilityElementInfoSetOperationActions(ArkUI\_AccessibilityElementInfo\* elementInfo,int32\_t operationCount, ArkUI\_AccessibleAction\* operationActions)

**Description**

Sets the supported operations for an **ArkUI\_AccessibilityElementInfo** object.

**Since**: 13

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_AccessibilityElementInfo](../../structs/arkui-accessibilityelementinfo/document.md)\* elementInfo | Pointer to the target **ArkUI\_AccessibilityElementInfo** object. |
| int32\_t\* operationCount | Pointer to the number of actions supported by the component. |
| [ArkUI\_AccessibleAction](../../structs/arkui-accessibleaction/document.md)\* operationActions | Pointer to the array of actions supported by the component. |

**Returns**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Returns [ARKUI\_ACCESSIBILITY\_NATIVE\_RESULT\_SUCCESSFUL](#arkui_acessbilityerrorcode) if the operation is successful.

Returns [ARKUI\_ACCESSIBILITY\_NATIVE\_RESULT\_BAD\_PARAMETER](#arkui_acessbilityerrorcode) if a parameter error occurs.

 |

#### \[h2\]OH\_ArkUI\_AccessibilityElementInfoSetScreenRect()

int32\_t OH\_ArkUI\_AccessibilityElementInfoSetScreenRect(ArkUI\_AccessibilityElementInfo\* elementInfo, ArkUI\_AccessibleRect\* screenRect)

**Description**

Sets the screen coordinates for an **ArkUI\_AccessibilityElementInfo** object.

**Since**: 13

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_AccessibilityElementInfo](../../structs/arkui-accessibilityelementinfo/document.md)\* elementInfo | Pointer to the target **ArkUI\_AccessibilityElementInfo** object. |
| [ArkUI\_AccessibleRect](../../structs/arkui-accessiblerect/document.md)\* screenRect | Pointer to the screen coordinates. |

**Returns**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Returns [ARKUI\_ACCESSIBILITY\_NATIVE\_RESULT\_SUCCESSFUL](#arkui_acessbilityerrorcode) if the operation is successful.

Returns [ARKUI\_ACCESSIBILITY\_NATIVE\_RESULT\_BAD\_PARAMETER](#arkui_acessbilityerrorcode) if a parameter error occurs.

 |

#### \[h2\]OH\_ArkUI\_AccessibilityElementInfoSetCheckable()

int32\_t OH\_ArkUI\_AccessibilityElementInfoSetCheckable(ArkUI\_AccessibilityElementInfo\* elementInfo, bool checkable)

**Description**

Sets whether the **ArkUI\_AccessibilityElementInfo** object is checkable.

**Since**: 13

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_AccessibilityElementInfo](../../structs/arkui-accessibilityelementinfo/document.md)\* elementInfo | Pointer to the target **ArkUI\_AccessibilityElementInfo** object. |
| bool checkable | Whether the object is checkable. **true**: checkable; **false**: not checkable. The default value is **false**. |

**Returns**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Returns [ARKUI\_ACCESSIBILITY\_NATIVE\_RESULT\_SUCCESSFUL](#arkui_acessbilityerrorcode) if the operation is successful.

Returns [ARKUI\_ACCESSIBILITY\_NATIVE\_RESULT\_BAD\_PARAMETER](#arkui_acessbilityerrorcode) if a parameter error occurs.

 |

#### \[h2\]OH\_ArkUI\_AccessibilityElementInfoSetChecked()

int32\_t OH\_ArkUI\_AccessibilityElementInfoSetChecked(ArkUI\_AccessibilityElementInfo\* elementInfo, bool checked)

**Description**

Sets whether the **ArkUI\_AccessibilityElementInfo** object is checked.

**Since**: 13

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_AccessibilityElementInfo](../../structs/arkui-accessibilityelementinfo/document.md)\* elementInfo | Pointer to the target **ArkUI\_AccessibilityElementInfo** object. |
| bool checked | Whether the object is checked. **true**: checked; **false**: unchecked. The default value is **false**. |

**Returns**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Returns [ARKUI\_ACCESSIBILITY\_NATIVE\_RESULT\_SUCCESSFUL](#arkui_acessbilityerrorcode) if the operation is successful.

Returns [ARKUI\_ACCESSIBILITY\_NATIVE\_RESULT\_BAD\_PARAMETER](#arkui_acessbilityerrorcode) if a parameter error occurs.

 |

#### \[h2\]OH\_ArkUI\_AccessibilityElementInfoSetFocusable()

int32\_t OH\_ArkUI\_AccessibilityElementInfoSetFocusable(ArkUI\_AccessibilityElementInfo\* elementInfo, bool focusable)

**Description**

Sets whether the **ArkUI\_AccessibilityElementInfo** object is focusable.

**Since**: 13

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_AccessibilityElementInfo](../../structs/arkui-accessibilityelementinfo/document.md)\* elementInfo | Pointer to the target **ArkUI\_AccessibilityElementInfo** object. |
| bool focusable | Whether the object is focusable. **true**: focusable; **false**: not focusable. The default value is **false**. |

**Returns**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Returns [ARKUI\_ACCESSIBILITY\_NATIVE\_RESULT\_SUCCESSFUL](#arkui_acessbilityerrorcode) if the operation is successful.

Returns [ARKUI\_ACCESSIBILITY\_NATIVE\_RESULT\_BAD\_PARAMETER](#arkui_acessbilityerrorcode) if a parameter error occurs.

 |

#### \[h2\]OH\_ArkUI\_AccessibilityElementInfoSetFocused()

int32\_t OH\_ArkUI\_AccessibilityElementInfoSetFocused(ArkUI\_AccessibilityElementInfo\* elementInfo, bool isFocused)

**Description**

Sets whether the **ArkUI\_AccessibilityElementInfo** object is focused.

**Since**: 13

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_AccessibilityElementInfo](../../structs/arkui-accessibilityelementinfo/document.md)\* elementInfo | Pointer to the target **ArkUI\_AccessibilityElementInfo** object. |
| bool isFocused | Whether the object is focused. **true**: focused; **false**: not focused. The default value is **false**. |

**Returns**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Returns [ARKUI\_ACCESSIBILITY\_NATIVE\_RESULT\_SUCCESSFUL](#arkui_acessbilityerrorcode) if the operation is successful.

Returns [ARKUI\_ACCESSIBILITY\_NATIVE\_RESULT\_BAD\_PARAMETER](#arkui_acessbilityerrorcode) if a parameter error occurs.

 |

#### \[h2\]OH\_ArkUI\_AccessibilityElementInfoSetVisible()

int32\_t OH\_ArkUI\_AccessibilityElementInfoSetVisible(ArkUI\_AccessibilityElementInfo\* elementInfo, bool isVisible)

**Description**

Sets whether an **ArkUI\_AccessibilityElementInfo** object is visible.

**Since**: 13

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_AccessibilityElementInfo](../../structs/arkui-accessibilityelementinfo/document.md)\* elementInfo | Pointer to the target **ArkUI\_AccessibilityElementInfo** object. |
| bool isVisible | Whether the element is visible. **true**: visible; **false**: not visible. The default value is **false**. |

**Returns**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Returns [ARKUI\_ACCESSIBILITY\_NATIVE\_RESULT\_SUCCESSFUL](#arkui_acessbilityerrorcode) if the operation is successful.

Returns [ARKUI\_ACCESSIBILITY\_NATIVE\_RESULT\_BAD\_PARAMETER](#arkui_acessbilityerrorcode) if a parameter error occurs.

 |

#### \[h2\]OH\_ArkUI\_AccessibilityElementInfoSetAccessibilityFocused()

int32\_t OH\_ArkUI\_AccessibilityElementInfoSetAccessibilityFocused(ArkUI\_AccessibilityElementInfo\* elementInfo, bool accessibilityFocused)

**Description**

Sets whether the element is focused for accessibility purposes for an **ArkUI\_AccessibilityElementInfo** object.

**Since**: 13

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_AccessibilityElementInfo](../../structs/arkui-accessibilityelementinfo/document.md)\* elementInfo | Pointer to the target **ArkUI\_AccessibilityElementInfo** object. |
| bool accessibilityFocused | Accessibility focus state. **true**: Accessibility focus is set. **false**: Accessibility focus is not set. The default value is **false**. |

**Returns**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Returns [ARKUI\_ACCESSIBILITY\_NATIVE\_RESULT\_SUCCESSFUL](#arkui_acessbilityerrorcode) if the operation is successful.

Returns [ARKUI\_ACCESSIBILITY\_NATIVE\_RESULT\_BAD\_PARAMETER](#arkui_acessbilityerrorcode) if a parameter error occurs.

 |

#### \[h2\]OH\_ArkUI\_AccessibilityElementInfoSetSelected()

int32\_t OH\_ArkUI\_AccessibilityElementInfoSetSelected(ArkUI\_AccessibilityElementInfo\* elementInfo, bool selected)

**Description**

Sets whether the **ArkUI\_AccessibilityElementInfo** object is selected.

**Since**: 13

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_AccessibilityElementInfo](../../structs/arkui-accessibilityelementinfo/document.md)\* elementInfo | Pointer to the target **ArkUI\_AccessibilityElementInfo** object. |
| bool selected | Whether the object is selected. **true**: selected; **false**: not selected. The default value is **false**. |

**Returns**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Returns [ARKUI\_ACCESSIBILITY\_NATIVE\_RESULT\_SUCCESSFUL](#arkui_acessbilityerrorcode) if the operation is successful.

Returns [ARKUI\_ACCESSIBILITY\_NATIVE\_RESULT\_BAD\_PARAMETER](#arkui_acessbilityerrorcode) if a parameter error occurs.

 |

#### \[h2\]OH\_ArkUI\_AccessibilityElementInfoSetClickable()

int32\_t OH\_ArkUI\_AccessibilityElementInfoSetClickable(ArkUI\_AccessibilityElementInfo\* elementInfo, bool clickable)

**Description**

Sets whether the **ArkUI\_AccessibilityElementInfo** object is clickable.

**Since**: 13

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_AccessibilityElementInfo](../../structs/arkui-accessibilityelementinfo/document.md)\* elementInfo | Pointer to the target **ArkUI\_AccessibilityElementInfo** object. |
| bool clickable | Whether the object is clickable. **true**: supported; **false**: not supported. The default value is **false**. |

**Returns**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Returns [ARKUI\_ACCESSIBILITY\_NATIVE\_RESULT\_SUCCESSFUL](#arkui_acessbilityerrorcode) if the operation is successful.

Returns [ARKUI\_ACCESSIBILITY\_NATIVE\_RESULT\_BAD\_PARAMETER](#arkui_acessbilityerrorcode) if a parameter error occurs.

 |

#### \[h2\]OH\_ArkUI\_AccessibilityElementInfoSetLongClickable()

int32\_t OH\_ArkUI\_AccessibilityElementInfoSetLongClickable(ArkUI\_AccessibilityElementInfo\* elementInfo, bool longClickable)

**Description**

Sets whether the **ArkUI\_AccessibilityElementInfo** object supports long-press gestures.

**Since**: 13

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_AccessibilityElementInfo](../../structs/arkui-accessibilityelementinfo/document.md)\* elementInfo | Pointer to the target **ArkUI\_AccessibilityElementInfo** object. |
| bool longClickable | Whether long-press gestures are supported. **true**: supported; **false**: not supported. The default value is **false**. |

**Returns**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Returns [ARKUI\_ACCESSIBILITY\_NATIVE\_RESULT\_SUCCESSFUL](#arkui_acessbilityerrorcode) if the operation is successful.

Returns [ARKUI\_ACCESSIBILITY\_NATIVE\_RESULT\_BAD\_PARAMETER](#arkui_acessbilityerrorcode) if a parameter error occurs.

 |

#### \[h2\]OH\_ArkUI\_AccessibilityElementInfoSetEnabled()

int32\_t OH\_ArkUI\_AccessibilityElementInfoSetEnabled(ArkUI\_AccessibilityElementInfo\* elementInfo, bool isEnabled)

**Description**

Sets whether the **ArkUI\_AccessibilityElementInfo** object is enabled.

**Since**: 13

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_AccessibilityElementInfo](../../structs/arkui-accessibilityelementinfo/document.md)\* elementInfo | Pointer to the target **ArkUI\_AccessibilityElementInfo** object. |
| bool isEnabled | Whether the object is enabled. **true**: enabled; **false**: not enabled. The default value is **false**. |

**Returns**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Returns [ARKUI\_ACCESSIBILITY\_NATIVE\_RESULT\_SUCCESSFUL](#arkui_acessbilityerrorcode) if the operation is successful.

Returns [ARKUI\_ACCESSIBILITY\_NATIVE\_RESULT\_BAD\_PARAMETER](#arkui_acessbilityerrorcode) if a parameter error occurs.

 |

#### \[h2\]OH\_ArkUI\_AccessibilityElementInfoSetIsPassword()

int32\_t OH\_ArkUI\_AccessibilityElementInfoSetIsPassword(ArkUI\_AccessibilityElementInfo\* elementInfo, bool isPassword)

**Description**

Sets whether the **ArkUI\_AccessibilityElementInfo** object is a password.

**Since**: 13

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_AccessibilityElementInfo](../../structs/arkui-accessibilityelementinfo/document.md)\* elementInfo | Pointer to the target **ArkUI\_AccessibilityElementInfo** object. |
| bool isPassword | Whether the object is a password. **true**: The object is a password. **false**: The object is not a password. The default value is **false**. |

**Returns**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Returns [ARKUI\_ACCESSIBILITY\_NATIVE\_RESULT\_SUCCESSFUL](#arkui_acessbilityerrorcode) if the operation is successful.

Returns [ARKUI\_ACCESSIBILITY\_NATIVE\_RESULT\_BAD\_PARAMETER](#arkui_acessbilityerrorcode) if a parameter error occurs.

 |

#### \[h2\]OH\_ArkUI\_AccessibilityElementInfoSetScrollable()

int32\_t OH\_ArkUI\_AccessibilityElementInfoSetScrollable(ArkUI\_AccessibilityElementInfo\* elementInfo, bool scrollable)

**Description**

Sets whether the **ArkUI\_AccessibilityElementInfo** object is scrollable.

**Since**: 13

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_AccessibilityElementInfo](../../structs/arkui-accessibilityelementinfo/document.md)\* elementInfo | Pointer to the target **ArkUI\_AccessibilityElementInfo** object. |
| bool scrollable | Whether scrolling is supported. **true**: supported; **false**: not supported. The default value is **false**. |

**Returns**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Returns [ARKUI\_ACCESSIBILITY\_NATIVE\_RESULT\_SUCCESSFUL](#arkui_acessbilityerrorcode) if the operation is successful.

Returns [ARKUI\_ACCESSIBILITY\_NATIVE\_RESULT\_BAD\_PARAMETER](#arkui_acessbilityerrorcode) if a parameter error occurs.

 |

#### \[h2\]OH\_ArkUI\_AccessibilityElementInfoSetEditable()

int32\_t OH\_ArkUI\_AccessibilityElementInfoSetEditable(ArkUI\_AccessibilityElementInfo\* elementInfo, bool editable)

**Description**

Sets whether the **ArkUI\_AccessibilityElementInfo** object is editable.

**Since**: 13

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_AccessibilityElementInfo](../../structs/arkui-accessibilityelementinfo/document.md)\* elementInfo | Pointer to the target **ArkUI\_AccessibilityElementInfo** object. |
| bool editable | Whether editing is supported. **true**: supported; **false**: not supported. The default value is **false**. |

**Returns**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Returns [ARKUI\_ACCESSIBILITY\_NATIVE\_RESULT\_SUCCESSFUL](#arkui_acessbilityerrorcode) if the operation is successful.

Returns [ARKUI\_ACCESSIBILITY\_NATIVE\_RESULT\_BAD\_PARAMETER](#arkui_acessbilityerrorcode) if a parameter error occurs.

 |

#### \[h2\]OH\_ArkUI\_AccessibilityElementInfoSetIsHint()

int32\_t OH\_ArkUI\_AccessibilityElementInfoSetIsHint(ArkUI\_AccessibilityElementInfo\* elementInfo, bool isHint)

**Description**

Sets the hint status for an **ArkUI\_AccessibilityElementInfo** object.

**Since**: 13

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_AccessibilityElementInfo](../../structs/arkui-accessibilityelementinfo/document.md)\* elementInfo | Pointer to the target **ArkUI\_AccessibilityElementInfo** object. |
| bool isHint | Whether the object represents a hint. **true** if the object represents a hint, **false** otherwise. The **hintText** information is obtained only when the object is in the hint state. |

**Returns**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Returns [ARKUI\_ACCESSIBILITY\_NATIVE\_RESULT\_SUCCESSFUL](#arkui_acessbilityerrorcode) if the operation is successful.

Returns [ARKUI\_ACCESSIBILITY\_NATIVE\_RESULT\_BAD\_PARAMETER](#arkui_acessbilityerrorcode) if a parameter error occurs.

 |

#### \[h2\]OH\_ArkUI\_AccessibilityElementInfoSetRangeInfo()

int32\_t OH\_ArkUI\_AccessibilityElementInfoSetRangeInfo(ArkUI\_AccessibilityElementInfo\* elementInfo, ArkUI\_AccessibleRangeInfo\* rangeInfo)

**Description**

Sets the range information for an **ArkUI\_AccessibilityElementInfo** object.

**Since**: 13

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_AccessibilityElementInfo](../../structs/arkui-accessibilityelementinfo/document.md)\* elementInfo | Pointer to the target **ArkUI\_AccessibilityElementInfo** object. |
| [ArkUI\_AccessibleRangeInfo](../../structs/arkui-accessiblerangeinfo/document.md)\* rangeInfo | Pointer to the current value, maximum value, and minimum value of the specific component. |

**Returns**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Returns [ARKUI\_ACCESSIBILITY\_NATIVE\_RESULT\_SUCCESSFUL](#arkui_acessbilityerrorcode) if the operation is successful.

Returns [ARKUI\_ACCESSIBILITY\_NATIVE\_RESULT\_BAD\_PARAMETER](#arkui_acessbilityerrorcode) if a parameter error occurs.

 |

#### \[h2\]OH\_ArkUI\_AccessibilityElementInfoSetGridInfo()

int32\_t OH\_ArkUI\_AccessibilityElementInfoSetGridInfo(ArkUI\_AccessibilityElementInfo\* elementInfo, ArkUI\_AccessibleGridInfo\* gridInfo)

**Description**

Sets the grid information for an **ArkUI\_AccessibilityElementInfo** object.

**Since**: 13

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_AccessibilityElementInfo](../../structs/arkui-accessibilityelementinfo/document.md)\* elementInfo | Pointer to the target **ArkUI\_AccessibilityElementInfo** object. |
| [ArkUI\_AccessibleGridInfo](../../structs/arkui-accessiblegridinfo/document.md)\* gridInfo | Pointer to the number of rows, number of columns, and selection mode of the specific component. |

**Returns**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Returns [ARKUI\_ACCESSIBILITY\_NATIVE\_RESULT\_SUCCESSFUL](#arkui_acessbilityerrorcode) if the operation is successful.

Returns [ARKUI\_ACCESSIBILITY\_NATIVE\_RESULT\_BAD\_PARAMETER](#arkui_acessbilityerrorcode) if a parameter error occurs.

 |

#### \[h2\]OH\_ArkUI\_AccessibilityElementInfoSetGridItemInfo()

int32\_t OH\_ArkUI\_AccessibilityElementInfoSetGridItemInfo(ArkUI\_AccessibilityElementInfo\* elementInfo, ArkUI\_AccessibleGridItemInfo\* gridItem)

**Description**

Sets a single-item container within a grid container for an **ArkUI\_AccessibilityElementInfo** object.

**Since**: 13

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_AccessibilityElementInfo](../../structs/arkui-accessibilityelementinfo/document.md)\* elementInfo | Pointer to the target **ArkUI\_AccessibilityElementInfo** object. |
| [ArkUI\_AccessibleGridItemInfo](../../structs/arkui-accessiblegriditeminfo/document.md)\* gridItem | Pointer to the attribute values for the specific component. |

**Returns**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Returns [ARKUI\_ACCESSIBILITY\_NATIVE\_RESULT\_SUCCESSFUL](#arkui_acessbilityerrorcode) if the operation is successful.

Returns [ARKUI\_ACCESSIBILITY\_NATIVE\_RESULT\_BAD\_PARAMETER](#arkui_acessbilityerrorcode) if a parameter error occurs.

 |

#### \[h2\]OH\_ArkUI\_AccessibilityElementInfoSetSelectedTextStart()

int32\_t OH\_ArkUI\_AccessibilityElementInfoSetSelectedTextStart(ArkUI\_AccessibilityElementInfo\* elementInfo, int32\_t selectedTextStart)

**Description**

Sets the start position of the selected text for an **ArkUI\_AccessibilityElementInfo** object.

**Since**: 13

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_AccessibilityElementInfo](../../structs/arkui-accessibilityelementinfo/document.md)\* elementInfo | Pointer to the target **ArkUI\_AccessibilityElementInfo** object. |
| int32\_t selectedTextStart | Start position of the selected text. Applicable to text components. |

**Returns**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Returns [ARKUI\_ACCESSIBILITY\_NATIVE\_RESULT\_SUCCESSFUL](#arkui_acessbilityerrorcode) if the operation is successful.

Returns [ARKUI\_ACCESSIBILITY\_NATIVE\_RESULT\_BAD\_PARAMETER](#arkui_acessbilityerrorcode) if a parameter error occurs.

 |

#### \[h2\]OH\_ArkUI\_AccessibilityElementInfoSetSelectedTextEnd()

int32\_t OH\_ArkUI\_AccessibilityElementInfoSetSelectedTextEnd(ArkUI\_AccessibilityElementInfo\* elementInfo, int32\_t selectedTextEnd)

**Description**

Sets the end position of the selected text for an **ArkUI\_AccessibilityElementInfo** object.

**Since**: 13

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_AccessibilityElementInfo](../../structs/arkui-accessibilityelementinfo/document.md)\* elementInfo | Pointer to the target **ArkUI\_AccessibilityElementInfo** object. |
| int32\_t selectedTextEnd | End position of the selected text. Applicable to text components. |

**Returns**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Returns [ARKUI\_ACCESSIBILITY\_NATIVE\_RESULT\_SUCCESSFUL](#arkui_acessbilityerrorcode) if the operation is successful.

Returns [ARKUI\_ACCESSIBILITY\_NATIVE\_RESULT\_BAD\_PARAMETER](#arkui_acessbilityerrorcode) if a parameter error occurs.

 |

#### \[h2\]OH\_ArkUI\_AccessibilityElementInfoSetCurrentItemIndex()

int32\_t OH\_ArkUI\_AccessibilityElementInfoSetCurrentItemIndex(ArkUI\_AccessibilityElementInfo\* elementInfo, int32\_t currentItemIndex)

**Description**

Sets the position information of the currently focused component for an **ArkUI\_AccessibilityElementInfo** object.

**Since**: 13

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_AccessibilityElementInfo](../../structs/arkui-accessibilityelementinfo/document.md)\* elementInfo | Pointer to the target **ArkUI\_AccessibilityElementInfo** object. |
| int32\_t currentItemIndex | Position information of the currently focused component. |

**Returns**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Returns [ARKUI\_ACCESSIBILITY\_NATIVE\_RESULT\_SUCCESSFUL](#arkui_acessbilityerrorcode) if the operation is successful.

Returns [ARKUI\_ACCESSIBILITY\_NATIVE\_RESULT\_BAD\_PARAMETER](#arkui_acessbilityerrorcode) if a parameter error occurs.

 |

#### \[h2\]OH\_ArkUI\_AccessibilityElementInfoSetStartItemIndex()

int32\_t OH\_ArkUI\_AccessibilityElementInfoSetStartItemIndex(ArkUI\_AccessibilityElementInfo\* elementInfo, int32\_t startItemIndex)

**Description**

Sets the position information of the first element displayed on the current screen for an **ArkUI\_AccessibilityElementInfo** object.

**Since**: 13

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_AccessibilityElementInfo](../../structs/arkui-accessibilityelementinfo/document.md)\* elementInfo | Pointer to the target **ArkUI\_AccessibilityElementInfo** object. |
| int32\_t startItemIndex | Index of the first item displayed on the current screen. Applicable to components such as **List**, **Select**, **Swiper**, and **Tab\_Bar**. |

**Returns**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Returns [ARKUI\_ACCESSIBILITY\_NATIVE\_RESULT\_SUCCESSFUL](#arkui_acessbilityerrorcode) if the operation is successful.

Returns [ARKUI\_ACCESSIBILITY\_NATIVE\_RESULT\_BAD\_PARAMETER](#arkui_acessbilityerrorcode) if a parameter error occurs.

 |

#### \[h2\]OH\_ArkUI\_AccessibilityElementInfoSetEndItemIndex()

int32\_t OH\_ArkUI\_AccessibilityElementInfoSetEndItemIndex(ArkUI\_AccessibilityElementInfo\* elementInfo, int32\_t endItemIndex)

**Description**

Sets the position information of the last element displayed on the current screen for an **ArkUI\_AccessibilityElementInfo** object.

**Since**: 13

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_AccessibilityElementInfo](../../structs/arkui-accessibilityelementinfo/document.md)\* elementInfo | Pointer to the target **ArkUI\_AccessibilityElementInfo** object. |
| int32\_t endItemIndex | Index of the last item displayed on the current screen. Applicable to components such as **List**, **Select**, **Swiper**, and **Tab\_Bar**. |

**Returns**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Returns [ARKUI\_ACCESSIBILITY\_NATIVE\_RESULT\_SUCCESSFUL](#arkui_acessbilityerrorcode) if the operation is successful.

Returns [ARKUI\_ACCESSIBILITY\_NATIVE\_RESULT\_BAD\_PARAMETER](#arkui_acessbilityerrorcode) if a parameter error occurs.

 |

#### \[h2\]OH\_ArkUI\_AccessibilityElementInfoSetItemCount()

int32\_t OH\_ArkUI\_AccessibilityElementInfoSetItemCount(ArkUI\_AccessibilityElementInfo\* elementInfo, int32\_t itemCount)

**Description**

Sets the total number of elements of a specific component for an **ArkUI\_AccessibilityElementInfo** object.

**Since**: 13

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_AccessibilityElementInfo](../../structs/arkui-accessibilityelementinfo/document.md)\* elementInfo | Pointer to the target **ArkUI\_AccessibilityElementInfo** object. |
| int32\_t itemCount | Total count of items of the specific component. Applicable to components such as **List**, **Select**, **Swiper**, and **Tab\_Bar**. |

**Returns**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Returns [ARKUI\_ACCESSIBILITY\_NATIVE\_RESULT\_SUCCESSFUL](#arkui_acessbilityerrorcode) if the operation is successful.

Returns [ARKUI\_ACCESSIBILITY\_NATIVE\_RESULT\_BAD\_PARAMETER](#arkui_acessbilityerrorcode) if a parameter error occurs.

 |

#### \[h2\]OH\_ArkUI\_AccessibilityElementInfoSetAccessibilityOffset()

int32\_t OH\_ArkUI\_AccessibilityElementInfoSetAccessibilityOffset(ArkUI\_AccessibilityElementInfo\* elementInfo, int32\_t offset)

**Description**

Sets the scrolling pixel offset of the content area relative to the top coordinate of the element for an **ArkUI\_AccessibilityElementInfo** object.

**Since**: 13

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_AccessibilityElementInfo](../../structs/arkui-accessibilityelementinfo/document.md)\* elementInfo | Pointer to the target **ArkUI\_AccessibilityElementInfo** object. |
| int32\_t offset | Scrolling pixel offset of the content area relative to the top coordinate of the element for scrollable controls, such as [List](../../../arkts-components/scroll-and-swipe/list/document.md) and [Grid](../../../arkts-components/scroll-and-swipe/grid/document.md). |

**Returns**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Returns [ARKUI\_ACCESSIBILITY\_NATIVE\_RESULT\_SUCCESSFUL](#arkui_acessbilityerrorcode) if the operation is successful.

Returns [ARKUI\_ACCESSIBILITY\_NATIVE\_RESULT\_BAD\_PARAMETER](#arkui_acessbilityerrorcode) if a parameter error occurs.

 |

#### \[h2\]OH\_ArkUI\_AccessibilityElementInfoSetAccessibilityGroup()

int32\_t OH\_ArkUI\_AccessibilityElementInfoSetAccessibilityGroup(ArkUI\_AccessibilityElementInfo\* elementInfo, bool accessibilityGroup)

**Description**

Sets whether the **ArkUI\_AccessibilityElementInfo** object should be treated as an accessibility group.

**Since**: 13

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_AccessibilityElementInfo](../../structs/arkui-accessibilityelementinfo/document.md)\* elementInfo | Pointer to the target **ArkUI\_AccessibilityElementInfo** object. |
| bool accessibilityGroup | Whether to enable accessibility group behavior for the object. **true**: enable; **false**: disable. |

**Returns**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Returns [ARKUI\_ACCESSIBILITY\_NATIVE\_RESULT\_SUCCESSFUL](#arkui_acessbilityerrorcode) if the operation is successful.

Returns [ARKUI\_ACCESSIBILITY\_NATIVE\_RESULT\_BAD\_PARAMETER](#arkui_acessbilityerrorcode) if a parameter error occurs.

 |

#### \[h2\]OH\_ArkUI\_AccessibilityElementInfoSetAccessibilityLevel()

int32\_t OH\_ArkUI\_AccessibilityElementInfoSetAccessibilityLevel(ArkUI\_AccessibilityElementInfo\* elementInfo, const char\* accessibilityLevel)

**Description**

Sets the accessibility level for the **ArkUI\_AccessibilityElementInfo** object.

**Since**: 13

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_AccessibilityElementInfo](../../structs/arkui-accessibilityelementinfo/document.md)\* elementInfo | Pointer to the target **ArkUI\_AccessibilityElementInfo** object. |
| const char\* accessibilityLevel | 
Pointer to the accessibility level of the component, which is used to decide whether the component is recognized by accessibility services.

\- **auto**: The system automatically determines the component's importance based on its attributes and decides whether to allow accessibility services to recognize it.

\- **yes**: The component is important and allows recognition by accessibility services.

\- **no**: The component is not important and prohibits recognition by accessibility services.

\- **no-hide-descendants**: The component and its descendant nodes are not important, and prohibits recognition of the component and its descendants by accessibility services.

 |

**Returns**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Returns [ARKUI\_ACCESSIBILITY\_NATIVE\_RESULT\_SUCCESSFUL](#arkui_acessbilityerrorcode) if the operation is successful.

Returns [ARKUI\_ACCESSIBILITY\_NATIVE\_RESULT\_BAD\_PARAMETER](#arkui_acessbilityerrorcode) if a parameter error occurs.

 |

#### \[h2\]OH\_ArkUI\_AccessibilityElementInfoSetZIndex()

int32\_t OH\_ArkUI\_AccessibilityElementInfoSetZIndex(ArkUI\_AccessibilityElementInfo\* elementInfo, int32\_t zIndex)

**Description**

Sets the z-order of the component for the **ArkUI\_AccessibilityElementInfo** object.

**Since**: 13

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_AccessibilityElementInfo](../../structs/arkui-accessibilityelementinfo/document.md)\* elementInfo | Pointer to the target **ArkUI\_AccessibilityElementInfo** object. |
| int32\_t zIndex | Z-order of the component, used to control the position of the component along the z-axis perpendicular to the screen. This parameter is required for [UiTest](../../../../../system/debugging-tools/test-kit/arkts-api/ohos-uitest/document.md). |

**Returns**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Returns [ARKUI\_ACCESSIBILITY\_NATIVE\_RESULT\_SUCCESSFUL](#arkui_acessbilityerrorcode) if the operation is successful.

Returns [ARKUI\_ACCESSIBILITY\_NATIVE\_RESULT\_BAD\_PARAMETER](#arkui_acessbilityerrorcode) if a parameter error occurs.

 |

#### \[h2\]OH\_ArkUI\_AccessibilityElementInfoSetAccessibilityOpacity()

int32\_t OH\_ArkUI\_AccessibilityElementInfoSetAccessibilityOpacity(ArkUI\_AccessibilityElementInfo\* elementInfo, float opacity)

**Description**

Sets the opacity for the **ArkUI\_AccessibilityElementInfo** object.

**Since**: 13

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_AccessibilityElementInfo](../../structs/arkui-accessibilityelementinfo/document.md)\* elementInfo | Pointer to the target **ArkUI\_AccessibilityElementInfo** object. |
| float opacity | Opacity. The value ranges from 0 to 1, where **1** indicates opaque and **0** indicates completely transparent. This parameter is required for [UiTest](../../../../../system/debugging-tools/test-kit/arkts-api/ohos-uitest/document.md). |

**Returns**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Returns [ARKUI\_ACCESSIBILITY\_NATIVE\_RESULT\_SUCCESSFUL](#arkui_acessbilityerrorcode) if the operation is successful.

Returns [ARKUI\_ACCESSIBILITY\_NATIVE\_RESULT\_BAD\_PARAMETER](#arkui_acessbilityerrorcode) if a parameter error occurs.

 |

#### \[h2\]OH\_ArkUI\_AccessibilityElementInfoSetBackgroundColor()

int32\_t OH\_ArkUI\_AccessibilityElementInfoSetBackgroundColor(ArkUI\_AccessibilityElementInfo\* elementInfo, const char\* backgroundColor)

**Description**

Sets the background color for the **ArkUI\_AccessibilityElementInfo** object.

**Since**: 13

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_AccessibilityElementInfo](../../structs/arkui-accessibilityelementinfo/document.md)\* elementInfo | Pointer to the target **ArkUI\_AccessibilityElementInfo** object. |
| const char\* backgroundColor | Pointer to the background color. The value is in the **#ARGB** format. For example, the value for non-transparent white is **"#FFFFFFFF"**. This parameter is required for [UiTest](../../../../../system/debugging-tools/test-kit/arkts-api/ohos-uitest/document.md). |

**Returns**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Returns [ARKUI\_ACCESSIBILITY\_NATIVE\_RESULT\_SUCCESSFUL](#arkui_acessbilityerrorcode) if the operation is successful.

Returns [ARKUI\_ACCESSIBILITY\_NATIVE\_RESULT\_BAD\_PARAMETER](#arkui_acessbilityerrorcode) if a parameter error occurs.

 |

#### \[h2\]OH\_ArkUI\_AccessibilityElementInfoSetBackgroundImage()

int32\_t OH\_ArkUI\_AccessibilityElementInfoSetBackgroundImage(ArkUI\_AccessibilityElementInfo\* elementInfo, const char\* backgroundImage)

**Description**

Sets the background image for the **ArkUI\_AccessibilityElementInfo** object.

**Since**: 13

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_AccessibilityElementInfo](../../structs/arkui-accessibilityelementinfo/document.md)\* elementInfo | Pointer to the target **ArkUI\_AccessibilityElementInfo** object. |
| const char\* backgroundImage | Pointer to the background image. This parameter is required for [UiTest](../../../../../system/debugging-tools/test-kit/arkts-api/ohos-uitest/document.md). |

**Returns**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Returns [ARKUI\_ACCESSIBILITY\_NATIVE\_RESULT\_SUCCESSFUL](#arkui_acessbilityerrorcode) if the operation is successful.

Returns [ARKUI\_ACCESSIBILITY\_NATIVE\_RESULT\_BAD\_PARAMETER](#arkui_acessbilityerrorcode) if a parameter error occurs.

 |

#### \[h2\]OH\_ArkUI\_AccessibilityElementInfoSetBlur()

int32\_t OH\_ArkUI\_AccessibilityElementInfoSetBlur(ArkUI\_AccessibilityElementInfo\* elementInfo, const char\* blur)

**Description**

Sets the blur value for the **ArkUI\_AccessibilityElementInfo** object.

**Since**: 13

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_AccessibilityElementInfo](../../structs/arkui-accessibilityelementinfo/document.md)\* elementInfo | Pointer to the target **ArkUI\_AccessibilityElementInfo** object. |
| const char\* blur | Pointer to the blur value. This parameter is required for [UiTest](../../../../../system/debugging-tools/test-kit/arkts-api/ohos-uitest/document.md). |

**Returns**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Returns [ARKUI\_ACCESSIBILITY\_NATIVE\_RESULT\_SUCCESSFUL](#arkui_acessbilityerrorcode) if the operation is successful.

Returns [ARKUI\_ACCESSIBILITY\_NATIVE\_RESULT\_BAD\_PARAMETER](#arkui_acessbilityerrorcode) if a parameter error occurs.

 |

#### \[h2\]OH\_ArkUI\_AccessibilityElementInfoSetHitTestBehavior()

int32\_t OH\_ArkUI\_AccessibilityElementInfoSetHitTestBehavior(ArkUI\_AccessibilityElementInfo\* elementInfo, const char\* hitTestBehavior)

**Description**

Sets the response logic and node blocking rules for the hit test for an **ArkUI\_AccessibilityElementInfo** object.

**Since**: 13

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_AccessibilityElementInfo](../../structs/arkui-accessibilityelementinfo/document.md)\* elementInfo | Pointer to the target **ArkUI\_AccessibilityElementInfo** object. |
| const char\* hitTestBehavior | Pointer to the hit test mode. For details about the value range, see [HitTestMode](../../../arkts-components/common-definitions/enums/document.md#hittestmode9). |

**Returns**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Returns [ARKUI\_ACCESSIBILITY\_NATIVE\_RESULT\_SUCCESSFUL](#arkui_acessbilityerrorcode) if the operation is successful.

Returns [ARKUI\_ACCESSIBILITY\_NATIVE\_RESULT\_BAD\_PARAMETER](#arkui_acessbilityerrorcode) if a parameter error occurs.

 |

#### \[h2\]OH\_ArkUI\_CreateAccessibilityElementInfo()

ArkUI\_AccessibilityElementInfo\* OH\_ArkUI\_CreateAccessibilityElementInfo(void)

**Description**

Creates an **ArkUI\_AccessibilityElementInfo** object, which must be destroyed with **OH\_ArkUI\_DestoryAccessibilityElementInfo**.

**Since**: 13

**Returns**

| Type | Description |
| :-- | :-- |
| [ArkUI\_AccessibilityElementInfo](../../structs/arkui-accessibilityelementinfo/document.md)\* | Pointer to the **ArkUI\_AccessibilityElementInfo** object. |

#### \[h2\]OH\_ArkUI\_DestoryAccessibilityElementInfo()

void OH\_ArkUI\_DestoryAccessibilityElementInfo(ArkUI\_AccessibilityElementInfo\* elementInfo)

**Description**

Destroys an **ArkUI\_AccessibilityElementInfo** object.

**Since**: 13

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_AccessibilityElementInfo](../../structs/arkui-accessibilityelementinfo/document.md)\* elementInfo | Pointer to the target **ArkUI\_AccessibilityElementInfo** object. |

#### \[h2\]OH\_ArkUI\_CreateAccessibilityEventInfo()

ArkUI\_AccessibilityEventInfo\* OH\_ArkUI\_CreateAccessibilityEventInfo(void)

**Description**

Creates an **ArkUI\_AccessibilityEventInfo** object, which must be destroyed with **OH\_ArkUI\_DestoryAccessibilityEventInfo**.

**Since**: 13

**Returns**

| Type | Description |
| :-- | :-- |
| [ArkUI\_AccessibilityEventInfo](../../structs/arkui-accessibilityeventinfo/document.md)\* | Pointer to the **ArkUI\_AccessibilityEventInfo** object. |

#### \[h2\]OH\_ArkUI\_DestoryAccessibilityEventInfo()

void OH\_ArkUI\_DestoryAccessibilityEventInfo(ArkUI\_AccessibilityEventInfo\* eventInfo)

**Description**

Destroys an **ArkUI\_AccessibilityEventInfo** object.

**Since**: 13

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_AccessibilityEventInfo](../../structs/arkui-accessibilityeventinfo/document.md)\* eventInfo | Pointer to the **ArkUI\_AccessibilityEventInfo** object to destroy. |

#### \[h2\]OH\_ArkUI\_AccessibilityEventSetEventType()

int32\_t OH\_ArkUI\_AccessibilityEventSetEventType(ArkUI\_AccessibilityEventInfo\* eventInfo,  ArkUI\_AccessibilityEventType eventType)

**Description**

Sets the event type for an **ArkUI\_AccessibilityEventInfo** object.

**Since**: 13

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_AccessibilityEventInfo](../../structs/arkui-accessibilityeventinfo/document.md)\* eventInfo | Pointer to an **ArkUI\_AccessibilityEventInfo** object. |
| [ArkUI\_AccessibilityEventType](#arkui_accessibilityeventtype) eventType | Event type. |

**Returns**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Returns [ARKUI\_ACCESSIBILITY\_NATIVE\_RESULT\_SUCCESSFUL](#arkui_acessbilityerrorcode) if the operation is successful.

Returns [ARKUI\_ACCESSIBILITY\_NATIVE\_RESULT\_BAD\_PARAMETER](#arkui_acessbilityerrorcode) if a parameter error occurs.

 |

#### \[h2\]OH\_ArkUI\_AccessibilityEventSetTextAnnouncedForAccessibility()

int32\_t OH\_ArkUI\_AccessibilityEventSetTextAnnouncedForAccessibility(ArkUI\_AccessibilityEventInfo\* eventInfo,  const char\* textAnnouncedForAccessibility)

**Description**

Sets the content for auto-broadcasting for the **ArkUI\_AccessibilityEventInfo** object.

**Since**: 13

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_AccessibilityEventInfo](../../structs/arkui-accessibilityeventinfo/document.md)\* eventInfo | Pointer to an **ArkUI\_AccessibilityEventInfo** object. |
| const char\* textAnnouncedForAccessibility | Pointer to the content for auto-broadcasting. |

**Returns**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Returns [ARKUI\_ACCESSIBILITY\_NATIVE\_RESULT\_SUCCESSFUL](#arkui_acessbilityerrorcode) if the operation is successful.

Returns [ARKUI\_ACCESSIBILITY\_NATIVE\_RESULT\_BAD\_PARAMETER](#arkui_acessbilityerrorcode) if a parameter error occurs.

 |

#### \[h2\]OH\_ArkUI\_AccessibilityEventSetRequestFocusId()

int32\_t OH\_ArkUI\_AccessibilityEventSetRequestFocusId(ArkUI\_AccessibilityEventInfo\* eventInfo,  int32\_t requestFocusId)

**Description**

Sets the focus request ID for an **ArkUI\_AccessibilityEventInfo** object.

**Since**: 13

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_AccessibilityEventInfo](../../structs/arkui-accessibilityeventinfo/document.md)\* eventInfo | Pointer to an **ArkUI\_AccessibilityEventInfo** object. |
| int32\_t requestFocusId | Focus request ID. |

**Returns**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Returns [ARKUI\_ACCESSIBILITY\_NATIVE\_RESULT\_SUCCESSFUL](#arkui_acessbilityerrorcode) if the operation is successful.

Returns [ARKUI\_ACCESSIBILITY\_NATIVE\_RESULT\_BAD\_PARAMETER](#arkui_acessbilityerrorcode) if a parameter error occurs.

 |

#### \[h2\]OH\_ArkUI\_AccessibilityEventSetElementInfo()

int32\_t OH\_ArkUI\_AccessibilityEventSetElementInfo(ArkUI\_AccessibilityEventInfo\* eventInfo,  ArkUI\_AccessibilityElementInfo\* elementInfo)

**Description**

Sets the element information for an **ArkUI\_AccessibilityEventInfo** object.

**Since**: 13

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_AccessibilityEventInfo](../../structs/arkui-accessibilityeventinfo/document.md)\* eventInfo | Pointer to an **ArkUI\_AccessibilityEventInfo** object. |
| [ArkUI\_AccessibilityElementInfo](../../structs/arkui-accessibilityelementinfo/document.md)\* elementInfo | Pointer to an **ArkUI\_AccessibilityElementInfo** object. |

**Returns**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Returns [ARKUI\_ACCESSIBILITY\_NATIVE\_RESULT\_SUCCESSFUL](#arkui_acessbilityerrorcode) if the operation is successful.

Returns [ARKUI\_ACCESSIBILITY\_NATIVE\_RESULT\_BAD\_PARAMETER](#arkui_acessbilityerrorcode) if a parameter error occurs.

 |

#### \[h2\]OH\_ArkUI\_FindAccessibilityActionArgumentByKey()

int32\_t OH\_ArkUI\_FindAccessibilityActionArgumentByKey(ArkUI\_AccessibilityActionArguments\* arguments, const char\* key, char\*\* value)

**Description**

Obtains the value associated with a specified key in an **ArkUI\_AccessibilityActionArguments** struct.

**Since**: 13

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_AccessibilityActionArguments](../../structs/arkui-accessibilityactionarguments/document.md)\* arguments | Pointer to an **ArkUI\_AccessibilityActionArguments** object. |
| const char\* key | Pointer to the key. |
| char\*\* value | Pointer to the value. |

**Returns**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Returns [ARKUI\_ACCESSIBILITY\_NATIVE\_RESULT\_SUCCESSFUL](#arkui_acessbilityerrorcode) if the operation is successful.

Returns [ARKUI\_ACCESSIBILITY\_NATIVE\_RESULT\_BAD\_PARAMETER](#arkui_acessbilityerrorcode) if a parameter error occurs.

 |
