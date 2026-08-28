# ArkUI\_AccessibilityProviderCallbacksWithInstance

typedef struct {...} ArkUI\_AccessibilityProviderCallbacksWithInstance

#### Overview

Defines a callback function struct of a third-party operation [provider](../arkui-accessibilityprovider/document.md) in the multi-instance scenario. The functions that need to be implemented by the third-party platform are registered with the system through [OH\_ArkUI\_AccessibilityProviderRegisterCallbackWithInstance](../../header-files/native-interface-accessibility-h/document.md#oh_arkui_accessibilityproviderregistercallbackwithinstance).

**Since**: 15

**Related module**: [ArkUI\_Accessibility](../../modules/arkui-accessibility/document.md)

**Header file**: [native\_interface\_accessibility.h](../../header-files/native-interface-accessibility-h/document.md)

#### Summary

#### \[h2\]Member Functions

| Name | Description |
| :-- | :-- |
| [int32\_t (\*findAccessibilityNodeInfosById)(const char\* instanceId, int64\_t elementId,ArkUI\_AccessibilitySearchMode mode, int32\_t requestId, ArkUI\_AccessibilityElementInfoList\* elementList)](#findaccessibilitynodeinfosbyid) | Finds the information about an accessibility node based on the specified node ID. Multi-instance scenarios are supported. Callback function implemented by the third-party platform and registered with the system. |
| [int32\_t (\*findAccessibilityNodeInfosByText)(const char\* instanceId, int64\_t elementId, const char\* text,int32\_t requestId, ArkUI\_AccessibilityElementInfoList\* elementList)](#findaccessibilitynodeinfosbytext) | Finds the node information matching the specified text content. Multi-instance scenarios are supported. Callback function implemented by the third-party platform and registered with the system. |
| [int32\_t (\*findFocusedAccessibilityNode)(const char\* instanceId, int64\_t elementId,ArkUI\_AccessibilityFocusType focusType, int32\_t requestId, ArkUI\_AccessibilityElementInfo\* elementInfo)](#findfocusedaccessibilitynode) | Finds the node that currently has focus within a given node. Callback function implemented by the third-party platform and registered with the system. Multi-instance scenarios are supported. |
| [int32\_t (\*findNextFocusAccessibilityNode)(const char\* instanceId, int64\_t elementId, ArkUI\_AccessibilityFocusMoveDirection direction,int32\_t requestId, ArkUI\_AccessibilityElementInfo\* elementInfo)](#findnextfocusaccessibilitynode) | Finds the next node in a specified direction from a given node. Callback function implemented by the third-party platform and registered with the system. Multi-instance scenarios are supported. |
| [int32\_t (\*executeAccessibilityAction)(const char\* instanceId, int64\_t elementId,ArkUI\_Accessibility\_ActionType action, ArkUI\_AccessibilityActionArguments \*actionArguments, int32\_t requestId)](#executeaccessibilityaction) | Performs a specified action on a specified node. Callback function implemented by the third-party platform and registered with the system. Multi-instance scenarios are supported. |
| [int32\_t (\*clearFocusedFocusAccessibilityNode)(const char\* instanceId)](#clearfocusedfocusaccessibilitynode) | Removes focus from the current node. Callback function implemented by the third-party platform and registered with the system. Multi-instance scenarios are supported. |
| [int32\_t (\*getAccessibilityNodeCursorPosition)(const char\* instanceId, int64\_t elementId,int32\_t requestId, int32\_t\* index)](#getaccessibilitynodecursorposition) | Obtains the cursor position within a text component of the current accessibility node. Callback function implemented by the third-party platform and registered with the system. Multi-instance scenarios are supported. |

#### Member Function Description

#### \[h2\]findAccessibilityNodeInfosById()

int32\_t (\*findAccessibilityNodeInfosById)(const char\* instanceId, int64\_t elementId,ArkUI\_AccessibilitySearchMode mode, int32\_t requestId, ArkUI\_AccessibilityElementInfoList\* elementList)

**Description**

Finds the information about an accessibility node based on the specified node ID. Callback function implemented by the third-party platform and registered with the system. Multi-instance scenarios are supported.

**Since**: 15

**Parameters**

| Name | Description |
| :-- | :-- |
| const char\* instanceId | Instance ID of the third-party framework. |
| int64\_t elementId | Unique ID of the accessibility element. |
| [ArkUI\_AccessibilitySearchMode](../../header-files/native-interface-accessibility-h/document.md#arkui_accessibilitysearchmode) mode | Search mode for accessibility services. |
| int32\_t requestId | Request ID, which is used to associate the request process. It is recommended that this ID be logged to facilitate fault locating. |
| [ArkUI\_AccessibilityElementInfoList](../arkui-accessibilityelementinfolist/document.md)\* elementList | List of all accessibility elements found. |

**Returns**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Returns [ARKUI\_ACCESSIBILITY\_NATIVE\_RESULT\_SUCCESSFUL](../../header-files/native-interface-accessibility-h/document.md#arkui_acessbilityerrorcode) if the operation is successful.

Returns [ARKUI\_ACCESSIBILITY\_NATIVE\_RESULT\_BAD\_PARAMETER](../../header-files/native-interface-accessibility-h/document.md#arkui_acessbilityerrorcode) if a parameter error occurs.

 |

#### \[h2\]findAccessibilityNodeInfosByText()

int32\_t (\*findAccessibilityNodeInfosByText)(const char\* instanceId, int64\_t elementId, const char\* text,int32\_t requestId, ArkUI\_AccessibilityElementInfoList\* elementList)

**Description**

Finds the node information matching the specified text content. Callback function implemented by the third-party platform and registered with the system. Multi-instance scenarios are supported.

**Since**: 15

**Parameters**

| Name | Description |
| :-- | :-- |
| const char\* instanceId | Instance ID of the third-party framework. |
| int64\_t elementId | Unique ID of the accessibility element. |
| const char\* text | Text content to match in the component. |
| int32\_t requestId | Request ID for identifying the request process. It is recommended for logging to aid troubleshooting. |
| [ArkUI\_AccessibilityElementInfoList](../arkui-accessibilityelementinfolist/document.md)\* elementList | List of all accessibility elements found. |

**Returns**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Returns [ARKUI\_ACCESSIBILITY\_NATIVE\_RESULT\_SUCCESSFUL](../../header-files/native-interface-accessibility-h/document.md#arkui_acessbilityerrorcode) if the operation is successful.

Returns [ARKUI\_ACCESSIBILITY\_NATIVE\_RESULT\_BAD\_PARAMETER](../../header-files/native-interface-accessibility-h/document.md#arkui_acessbilityerrorcode) if a parameter error occurs.

 |

#### \[h2\]findFocusedAccessibilityNode()

int32\_t (\*findFocusedAccessibilityNode)(const char\* instanceId, int64\_t elementId,ArkUI\_AccessibilityFocusType focusType, int32\_t requestId, ArkUI\_AccessibilityElementInfo\* elementInfo)

**Description**

Finds the node that currently has focus within a given node. Callback function implemented by the third-party platform and registered with the system. Multi-instance scenarios are supported.

**Since**: 15

**Parameters**

| Name | Description |
| :-- | :-- |
| const char\* instanceId | Instance ID of the third-party framework. |
| int64\_t elementId | Unique ID of the accessibility element. |
| [ArkUI\_AccessibilityFocusType](../../header-files/native-interface-accessibility-h/document.md#arkui_accessibilityfocustype) focusType | Focus type. |
| int32\_t requestId | Request ID, which is used to associate the request process. It is recommended that this ID be logged to facilitate fault locating. |
| [ArkUI\_AccessibilityElementInfo](../arkui-accessibilityelementinfo/document.md)\* elementInfo | List of all accessibility elements found. |

**Returns**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Returns [ARKUI\_ACCESSIBILITY\_NATIVE\_RESULT\_SUCCESSFUL](../../header-files/native-interface-accessibility-h/document.md#arkui_acessbilityerrorcode) if the operation is successful.

Returns [ARKUI\_ACCESSIBILITY\_NATIVE\_RESULT\_BAD\_PARAMETER](../../header-files/native-interface-accessibility-h/document.md#arkui_acessbilityerrorcode) if a parameter error occurs.

 |

#### \[h2\]findNextFocusAccessibilityNode()

int32\_t (\*findNextFocusAccessibilityNode)(const char\* instanceId, int64\_t elementId, ArkUI\_AccessibilityFocusMoveDirection direction,int32\_t requestId, ArkUI\_AccessibilityElementInfo\* elementInfo)

**Description**

Finds the next node in a specified direction from a given node. Callback function implemented by the third-party platform and registered with the system. Multi-instance scenarios are supported.

**Since**: 15

**Parameters**

| Name | Description |
| :-- | :-- |
| const char\* instanceId | Instance ID of the third-party framework. |
| int64\_t elementId | Unique ID of the accessibility element. |
| [ArkUI\_AccessibilityFocusMoveDirection](../../header-files/native-interface-accessibility-h/document.md#arkui_accessibilityfocusmovedirection) direction | Search direction. |
| int32\_t requestId | Request ID for identifying the request process. It is recommended for logging to aid troubleshooting. |
| [ArkUI\_AccessibilityElementInfo](../arkui-accessibilityelementinfo/document.md)\* elementInfo | List of all accessibility elements found. |

**Returns**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Returns [ARKUI\_ACCESSIBILITY\_NATIVE\_RESULT\_SUCCESSFUL](../../header-files/native-interface-accessibility-h/document.md#arkui_acessbilityerrorcode) if the operation is successful.

Returns [ARKUI\_ACCESSIBILITY\_NATIVE\_RESULT\_BAD\_PARAMETER](../../header-files/native-interface-accessibility-h/document.md#arkui_acessbilityerrorcode) if a parameter error occurs.

 |

#### \[h2\]executeAccessibilityAction()

int32\_t (\*executeAccessibilityAction)(const char\* instanceId, int64\_t elementId,ArkUI\_Accessibility\_ActionType action, ArkUI\_AccessibilityActionArguments \*actionArguments, int32\_t requestId)

**Description**

Performs a specified action on a specified node. Callback function implemented by the third-party platform and registered with the system. Multi-instance scenarios are supported.

**Since**: 15

**Parameters**

| Name | Description |
| :-- | :-- |
| const char\* instanceId | Instance ID of the third-party framework. |
| int64\_t elementId | Unique ID of the accessibility element. |
| [ArkUI\_Accessibility\_ActionType](../../header-files/native-interface-accessibility-h/document.md#arkui_accessibility_actiontype) action | Action to perform, such as focus, click, or long press. |
| [ArkUI\_AccessibilityActionArguments](../arkui-accessibilityactionarguments/document.md) \*actionArguments | Parameters controlling the action. |
| int32\_t requestId | Request ID for identifying the request process. It is recommended for logging to aid troubleshooting. |

**Returns**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Returns [ARKUI\_ACCESSIBILITY\_NATIVE\_RESULT\_SUCCESSFUL](../../header-files/native-interface-accessibility-h/document.md#arkui_acessbilityerrorcode) if the operation is successful.

Returns [ARKUI\_ACCESSIBILITY\_NATIVE\_RESULT\_BAD\_PARAMETER](../../header-files/native-interface-accessibility-h/document.md#arkui_acessbilityerrorcode) if a parameter error occurs.

 |

#### \[h2\]clearFocusedFocusAccessibilityNode()

int32\_t (\*clearFocusedFocusAccessibilityNode)(const char\* instanceId)

**Description**

Removes focus from the current node. Callback function implemented by the third-party platform and registered with the system. Multi-instance scenarios are supported.

**Since**: 15

**Parameters**

| Name | Description |
| :-- | :-- |
| const char\* instanceId | Instance ID of the third-party framework. |

**Returns**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Returns [ARKUI\_ACCESSIBILITY\_NATIVE\_RESULT\_SUCCESSFUL](../../header-files/native-interface-accessibility-h/document.md#arkui_acessbilityerrorcode) if the operation is successful.

Returns [ARKUI\_ACCESSIBILITY\_NATIVE\_RESULT\_BAD\_PARAMETER](../../header-files/native-interface-accessibility-h/document.md#arkui_acessbilityerrorcode) if a parameter error occurs.

 |

#### \[h2\]getAccessibilityNodeCursorPosition()

int32\_t (\*getAccessibilityNodeCursorPosition)(const char\* instanceId, int64\_t elementId,int32\_t requestId, int32\_t\* index)

**Description**

Obtains the cursor position within a text component of the current accessibility node. Callback function implemented by the third-party platform and registered with the system. Multi-instance scenarios are supported.

**Since**: 15

**Parameters**

| Name | Description |
| :-- | :-- |
| const char\* instanceId | Instance ID of the third-party framework. |
| int64\_t elementId | Unique ID of the accessibility element. |
| int32\_t requestId | Request ID for identifying the request process. It is recommended for logging to aid troubleshooting. |
| int32\_t\* index | Cursor position result. |

**Returns**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Returns [ARKUI\_ACCESSIBILITY\_NATIVE\_RESULT\_SUCCESSFUL](../../header-files/native-interface-accessibility-h/document.md#arkui_acessbilityerrorcode) if the operation is successful.

Returns [ARKUI\_ACCESSIBILITY\_NATIVE\_RESULT\_BAD\_PARAMETER](../../header-files/native-interface-accessibility-h/document.md#arkui_acessbilityerrorcode) if a parameter error occurs.

 |
