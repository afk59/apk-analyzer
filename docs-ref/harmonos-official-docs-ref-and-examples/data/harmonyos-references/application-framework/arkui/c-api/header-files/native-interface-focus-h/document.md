# native\_interface\_focus.h

#### Overview

Declares APIs for focus management, mainly used for actively transferring focus, managing the default focus transfer behavior, and controlling the focus activation state.

**File to include**: <arkui/native\_interface\_focus.h>

**Library**: libace\_ndk.z.so

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Since**: 15

**Related module**: [ArkUI\_NativeModule](../../modules/arkui-nativemodule/document.md)

**Sample**: [NdkFocus](https://gitcode.com/openharmony/applications_app_samples/tree/master/code/DocsSample/ArkUISample/NdkFocus)

#### Summary

#### \[h2\]Enums

| Name | typedef Keyword | Description |
| :-- | :-- | :-- |
| [ArkUI\_KeyProcessingMode](#arkui_keyprocessingmode) | ArkUI\_KeyProcessingMode | Enumerates the key event processing priority modes. |

#### \[h2\]Functions

| Name | Description |
| :-- | :-- |
| [ArkUI\_ErrorCode OH\_ArkUI\_FocusRequest(ArkUI\_NodeHandle node)](#oh_arkui_focusrequest) | Requests focus for a specific node. |
| [void OH\_ArkUI\_FocusClear(ArkUI\_ContextHandle uiContext)](#oh_arkui_focusclear) | Clears the focus to the root container node. |
| [void OH\_ArkUI\_FocusActivate(ArkUI\_ContextHandle uiContext, bool isActive, bool isAutoInactive)](#oh_arkui_focusactivate) | Sets the focus activation state for the current page. When activated, the focused node displays a focus box. |
| [void OH\_ArkUI\_FocusSetAutoTransfer(ArkUI\_ContextHandle uiContext, bool autoTransfer)](#oh_arkui_focussetautotransfer) | Configures the focus transfer behavior when pages are switched. |
| [void OH\_ArkUI\_FocusSetKeyProcessingMode(ArkUI\_ContextHandle uiContext, ArkUI\_KeyProcessingMode mode)](#oh_arkui_focussetkeyprocessingmode) | Sets the mode for processing key events. |

#### Enum Description

#### \[h2\]ArkUI\_KeyProcessingMode

enum ArkUI\_KeyProcessingMode

**Description**

Enumerates the key event processing priority modes.

**Since**: 15

| Value | Description |
| :-- | :-- |
| ARKUI\_KEY\_PROCESSING\_MODE\_FOCUS\_NAVIGATION = 0 | Key events are used for focus navigation. |
| ARKUI\_KEY\_PROCESSING\_MODE\_FOCUS\_ANCESTOR\_EVENT = 1 | Key events are passed up to ancestor components. |

#### Function Description

#### \[h2\]OH\_ArkUI\_FocusRequest()

ArkUI\_ErrorCode OH\_ArkUI\_FocusRequest(ArkUI\_NodeHandle node)

**Description**

Requests focus for a specific node.

**Since**: 15

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_NodeHandle](../../structs/arkui-node--00020177/document.md) node | Node. |

**Return value**

| Type | Description |
| :-- | :-- |
| [ArkUI\_ErrorCode](../native-type-h/document.md#arkui_errorcode) | 
Result code.

Returns [ARKUI\_ERROR\_CODE\_NO\_ERROR](../native-type-h/document.md#arkui_errorcode) if the operation is successful.

Returns [ARKUI\_ERROR\_CODE\_FOCUS\_NON\_FOCUSABLE](../native-type-h/document.md#arkui_errorcode) if the node cannot receive focus.

Returns [ARKUI\_ERROR\_CODE\_FOCUS\_NON\_FOCUSABLE\_ANCESTOR](../native-type-h/document.md#arkui_errorcode) if the ancestor node cannot receive focus.

Returns [ARKUI\_ERROR\_CODE\_FOCUS\_NON\_EXISTENT](../native-type-h/document.md#arkui_errorcode) if the node does not exist.

 |

#### \[h2\]OH\_ArkUI\_FocusClear()

void OH\_ArkUI\_FocusClear(ArkUI\_ContextHandle uiContext)

**Description**

Clears the focus to the root container node.

**Since**: 15

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_ContextHandle](../../structs/arkui-context--00020177/document.md) uiContext | UI instance object pointer. |

#### \[h2\]OH\_ArkUI\_FocusActivate()

void OH\_ArkUI\_FocusActivate(ArkUI\_ContextHandle uiContext, bool isActive, bool isAutoInactive)

**Description**

Sets the focus activation state for the current page. When activated, the focused node displays a focus box.

**Since**: 15

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_ContextHandle](../../structs/arkui-context--00020177/document.md) uiContext | UI instance object pointer. |
| bool isActive | Whether to enter or exit the focus activation state. The value **true** means to enter the focus activation state, and **false** means to exit the focus activation state. |
| bool isAutoInactive | Whether to automatically exit the focus active state on touch or mouse down events. **true**: Automatically exit the focus active state. **false**: Maintain the current state until the corresponding setting API is called. |

#### \[h2\]OH\_ArkUI\_FocusSetAutoTransfer()

void OH\_ArkUI\_FocusSetAutoTransfer(ArkUI\_ContextHandle uiContext, bool autoTransfer)

**Description**

Configures the focus transfer behavior when pages are switched.

**Since**: 15

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_ContextHandle](../../structs/arkui-context--00020177/document.md) uiContext | UI instance object pointer. |
| bool autoTransfer | Whether to automatically transfer focus when pages are switched. The value **true** means to automatically transfer focus when pages are switched, and **false** means the opposite. |

#### \[h2\]OH\_ArkUI\_FocusSetKeyProcessingMode()

void OH\_ArkUI\_FocusSetKeyProcessingMode(ArkUI\_ContextHandle uiContext, ArkUI\_KeyProcessingMode mode)

**Description**

Sets the mode for processing key events.

**Since**: 15

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_ContextHandle](../../structs/arkui-context--00020177/document.md) uiContext | UI instance object pointer. |
| [ArkUI\_KeyProcessingMode](#arkui_keyprocessingmode) mode | Key event processing priority mode. |
