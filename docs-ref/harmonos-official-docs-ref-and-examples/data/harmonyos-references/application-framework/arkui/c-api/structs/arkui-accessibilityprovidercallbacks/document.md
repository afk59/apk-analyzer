# ArkUI\_AccessibilityProviderCallbacks

typedef struct {...} ArkUI\_AccessibilityProviderCallbacks

#### Overview

Defines a callback function struct of a third-party operation [provider](../arkui-accessibilityprovider/document.md). The functions that need to be implemented by the third-party platform are registered with the system through [OH\_ArkUI\_AccessibilityProviderRegisterCallback](../../header-files/native-interface-accessibility-h/document.md#oh_arkui_accessibilityproviderregistercallback).

**Since**: 13

**Related module**: [ArkUI\_Accessibility](../../modules/arkui-accessibility/document.md)

**Header file**: [native\_interface\_accessibility.h](../../header-files/native-interface-accessibility-h/document.md)

#### Summary

#### \[h2\]Member Functions

| Name | Description |
| :-- | :-- |
| [int32\_t (\*findAccessibilityNodeInfosById)(int64\_t elementId, ArkUI\_AccessibilitySearchMode mode, int32\_t requestId, ArkUI\_AccessibilityElementInfoList\* elementList)](#findaccessibilitynodeinfosbyid) | Finds node information for the specified node. Callback function implemented by the third-party platform and registered with the system. |
| [int32\_t (\*findAccessibilityNodeInfosByText)(int64\_t elementId, const char\* text, int32\_t requestId,ArkUI\_AccessibilityElementInfoList\* elementList)](#findaccessibilitynodeinfosbytext) | Finds the nodes that contain specific text content. Callback function implemented by the third-party platform and registered with the system. |
| [int32\_t (\*findFocusedAccessibilityNode)(int64\_t elementId, ArkUI\_AccessibilityFocusType focusType, int32\_t requestId, ArkUI\_AccessibilityElementInfo\* elementInfo)](#findfocusedaccessibilitynode) | Finds the node that has obtained the focus based on the focus type and returns the element information of the node. Callback function implemented by the third-party platform and registered with the system. |
| [int32\_t (\*findNextFocusAccessibilityNode)(int64\_t elementId, ArkUI\_AccessibilityFocusMoveDirection direction, int32\_t requestId, ArkUI\_AccessibilityElementInfo\* elementInfo)](#findnextfocusaccessibilitynode) | Called to find the next focusable node based on the reference node, in the specified mode and direction. |
| [int32\_t (\*executeAccessibilityAction)(int64\_t elementId, ArkUI\_Accessibility\_ActionType action,ArkUI\_AccessibilityActionArguments \*actionArguments, int32\_t requestId)](#executeaccessibilityaction) | Called to execute a specified action on a specified node. |
| [int32\_t (\*clearFocusedFocusAccessibilityNode)()](#clearfocusedfocusaccessibilitynode) | Called to clear the focus state of the current focused node. |
| [int32\_t (\*getAccessibilityNodeCursorPosition)(int64\_t elementId, int32\_t requestId, int32\_t\* index)](#getaccessibilitynodecursorposition) | Called to query the current cursor position of the specified node. |

#### Member Function Description

#### \[h2\]findAccessibilityNodeInfosById()

int32\_t (\*findAccessibilityNodeInfosById)(int64\_t elementId, ArkUI\_AccessibilitySearchMode mode,int32\_t requestId, ArkUI\_AccessibilityElementInfoList\* elementList)

**Description**

Finds node information for the specified node. Callback function implemented by the third-party platform and registered with the system.

**Since**: 13

**Parameters**

| Name | Description |
| :-- | :-- |
| int64\_t elementId | Unique ID of the accessibility element. |
| [ArkUI\_AccessibilitySearchMode](../../header-files/native-interface-accessibility-h/document.md#arkui_accessibilitysearchmode) mode | Accessibility search mode. |
| int32\_t requestId | Request ID. |
| [ArkUI\_AccessibilityElementInfoList](../arkui-accessibilityelementinfolist/document.md)\* elementList | Accessibility element information list. |

**Returns**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Returns [ARKUI\_ACCESSIBILITY\_NATIVE\_RESULT\_SUCCESSFUL](../../header-files/native-interface-accessibility-h/document.md#arkui_acessbilityerrorcode) if the operation is successful.

Returns [ARKUI\_ACCESSIBILITY\_NATIVE\_RESULT\_BAD\_PARAMETER](../../header-files/native-interface-accessibility-h/document.md#arkui_acessbilityerrorcode) if a parameter error occurs.

 |

#### \[h2\]findAccessibilityNodeInfosByText()

int32\_t (\*findAccessibilityNodeInfosByText)(int64\_t elementId, const char\* text, int32\_t requestId,ArkUI\_AccessibilityElementInfoList\* elementList)

**Description**

Finds the nodes that contain specific text content. Callback function implemented by the third-party platform and registered with the system.

**Since**: 13

**Parameters**

| Name | Description |
| :-- | :-- |
| int64\_t elementId | Unique ID of the accessibility element. |
| const char\* text | Accessibility text. |
| int32\_t requestId | Request ID. |
| [ArkUI\_AccessibilityElementInfoList](../arkui-accessibilityelementinfolist/document.md)\* elementList | Accessibility element information list. |

**Returns**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Returns [ARKUI\_ACCESSIBILITY\_NATIVE\_RESULT\_SUCCESSFUL](../../header-files/native-interface-accessibility-h/document.md#arkui_acessbilityerrorcode) if the operation is successful.

Returns [ARKUI\_ACCESSIBILITY\_NATIVE\_RESULT\_BAD\_PARAMETER](../../header-files/native-interface-accessibility-h/document.md#arkui_acessbilityerrorcode) if a parameter error occurs.

 |

#### \[h2\]findFocusedAccessibilityNode()

int32\_t (\*findFocusedAccessibilityNode)(int64\_t elementId, ArkUI\_AccessibilityFocusType focusType, int32\_t requestId, ArkUI\_AccessibilityElementInfo\* elementInfo)

**Description**

Finds the node that has obtained the focus based on the focus type and returns the element information of the node. Callback function implemented by the third-party platform and registered with the system.

**Since**: 13

**Parameters**

| Name | Description |
| :-- | :-- |
| int64\_t elementId | Unique ID of the accessibility element. |
| [ArkUI\_AccessibilityFocusType](../../header-files/native-interface-accessibility-h/document.md#arkui_accessibilityfocustype) focusType | Focus type. |
| int32\_t requestId | Request ID. |
| [ArkUI\_AccessibilityElementInfo](../arkui-accessibilityelementinfo/document.md)\* elementInfo | Accessibility element information. |

**Returns**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Returns [ARKUI\_ACCESSIBILITY\_NATIVE\_RESULT\_SUCCESSFUL](../../header-files/native-interface-accessibility-h/document.md#arkui_acessbilityerrorcode) if the operation is successful.

Returns [ARKUI\_ACCESSIBILITY\_NATIVE\_RESULT\_BAD\_PARAMETER](../../header-files/native-interface-accessibility-h/document.md#arkui_acessbilityerrorcode) if a parameter error occurs.

 |

#### \[h2\]findNextFocusAccessibilityNode()

int32\_t (\*findNextFocusAccessibilityNode)(int64\_t elementId, ArkUI\_AccessibilityFocusMoveDirection direction, int32\_t requestId, ArkUI\_AccessibilityElementInfo\* elementInfo)

**Description**

Called to find the next focusable node based on the reference node mode and search direction.

**Since**: 13

**Parameters**

| Name | Description |
| :-- | :-- |
| int64\_t elementId | Unique ID of the accessibility element. |
| [ArkUI\_AccessibilityFocusMoveDirection](../../header-files/native-interface-accessibility-h/document.md#arkui_accessibilityfocusmovedirection) direction | Search direction. |
| int32\_t requestId | Request ID. |
| [ArkUI\_AccessibilityElementInfo](../arkui-accessibilityelementinfo/document.md)\* elementInfo | Information about the found accessibility element. |

**Returns**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Returns [ARKUI\_ACCESSIBILITY\_NATIVE\_RESULT\_SUCCESSFUL](../../header-files/native-interface-accessibility-h/document.md#arkui_acessbilityerrorcode) if the operation is successful.

Returns [ARKUI\_ACCESSIBILITY\_NATIVE\_RESULT\_BAD\_PARAMETER](../../header-files/native-interface-accessibility-h/document.md#arkui_acessbilityerrorcode) if a parameter error occurs.

 |

#### \[h2\]executeAccessibilityAction()

int32\_t (\*executeAccessibilityAction)(int64\_t elementId, ArkUI\_Accessibility\_ActionType action,ArkUI\_AccessibilityActionArguments \*actionArguments, int32\_t requestId)

**Description**

Executes an accessibility action on the specified accessibility node.

**Since**: 13

**Parameters**

| Name | Description |
| :-- | :-- |
| int64\_t elementId | Unique ID of the accessibility element. |
| [ArkUI\_Accessibility\_ActionType](../../header-files/native-interface-accessibility-h/document.md#arkui_accessibility_actiontype) action | Action to execute. |
| [ArkUI\_AccessibilityActionArguments](../arkui-accessibilityactionarguments/document.md) \*actionArguments | Action parameters. |
| int32\_t requestId | Request ID. |

**Returns**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Returns [ARKUI\_ACCESSIBILITY\_NATIVE\_RESULT\_SUCCESSFUL](../../header-files/native-interface-accessibility-h/document.md#arkui_acessbilityerrorcode) if the operation is successful.

Returns [ARKUI\_ACCESSIBILITY\_NATIVE\_RESULT\_BAD\_PARAMETER](../../header-files/native-interface-accessibility-h/document.md#arkui_acessbilityerrorcode) if a parameter error occurs.

 |

#### \[h2\]clearFocusedFocusAccessibilityNode()

int32\_t (\*clearFocusedFocusAccessibilityNode)()

**Description**

Called to clear the focus state of the current focused node.

**Since**: 13

**Returns**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Returns [ARKUI\_ACCESSIBILITY\_NATIVE\_RESULT\_SUCCESSFUL](../../header-files/native-interface-accessibility-h/document.md#arkui_acessbilityerrorcode) if the operation is successful.

Returns [ARKUI\_ACCESSIBILITY\_NATIVE\_RESULT\_BAD\_PARAMETER](../../header-files/native-interface-accessibility-h/document.md#arkui_acessbilityerrorcode) if a parameter error occurs.

 |

#### \[h2\]getAccessibilityNodeCursorPosition()

int32\_t (\*getAccessibilityNodeCursorPosition)(int64\_t elementId, int32\_t requestId, int32\_t\* index)

**Description**

Called to query the current cursor position of the specified node.

**Since**: 13

**Parameters**

| Name | Description |
| :-- | :-- |
| int64\_t elementId | Unique ID of the accessibility element. |
| int32\_t requestId | Request ID. |
| int32\_t\* index | Index of the cursor position. |

**Returns**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Returns [ARKUI\_ACCESSIBILITY\_NATIVE\_RESULT\_SUCCESSFUL](../../header-files/native-interface-accessibility-h/document.md#arkui_acessbilityerrorcode) if the operation is successful.

Returns [ARKUI\_ACCESSIBILITY\_NATIVE\_RESULT\_BAD\_PARAMETER](../../header-files/native-interface-accessibility-h/document.md#arkui_acessbilityerrorcode) if a parameter error occurs.

 |
