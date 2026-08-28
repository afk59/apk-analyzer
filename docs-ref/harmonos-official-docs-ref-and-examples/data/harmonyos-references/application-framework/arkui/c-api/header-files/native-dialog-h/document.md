# native\_dialog.h

#### Overview

Declares a set of custom dialog box APIs of ArkUI on the native side.

**File to include**: <arkui/native\_dialog.h>

**Library**: libace\_ndk.z.so

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Since**: 12

**Related module**: [ArkUI\_NativeModule](../../modules/arkui-nativemodule/document.md)

**Sample**: [NativeDialogSample](https://gitcode.com/openharmony/applications_app_samples/tree/master/code/DocsSample/ArkUISample/NativeDialogSample)

#### Summary

#### \[h2\]Structs

| Name | typedef Keyword | Description |
| :-- | :-- | :-- |
| [ArkUI\_NativeDialogAPI\_1](../../structs/arkui-nativedialogapi-1/document.md) | ArkUI\_NativeDialogAPI\_1 | Provides a collection of native-side custom dialog box APIs provided by ArkUI. |
| [ArkUI\_NativeDialogAPI\_2](../../structs/arkui-nativedialogapi-2/document.md) | ArkUI\_NativeDialogAPI\_2 | Provides a collection of native-side custom dialog box APIs provided by ArkUI. |
| [ArkUI\_NativeDialogAPI\_3](../../structs/arkui-nativedialogapi-3/document.md) | ArkUI\_NativeDialogAPI\_3 | Provides a collection of native-side custom dialog box APIs provided by ArkUI. |
| [ArkUI\_DialogDismissEvent](../../structs/arkui-dialogdismissevent/document.md) | ArkUI\_DialogDismissEvent | Defines a struct for a dialog box dismiss event. |
| [ArkUI\_CustomDialogOptions](../../structs/arkui-customdialogoptions/document.md) | ArkUI\_CustomDialogOptions | Defines a struct for custom dialog box options. |

#### \[h2\]Enums

| Name | typedef Keyword | Description |
| :-- | :-- | :-- |
| [ArkUI\_DismissReason](#arkui_dismissreason) | ArkUI\_DismissReason | Enumerates the actions for triggering closure of the dialog box. |
| [ArkUI\_LevelMode](#arkui_levelmode) | ArkUI\_LevelMode | Enumerates the display level modes of the dialog box. |
| [ArkUI\_ImmersiveMode](#arkui_immersivemode) | ArkUI\_ImmersiveMode | Enumerates the display areas of the embedded dialog box overlay. |
| [ArkUI\_DialogState](#arkui_dialogstate) | ArkUI\_DialogState | Enumerates the dialog box status. |

#### \[h2\]Functions

| Name | typedef Keyword | Description |
| :-- | :-- | :-- |
| [typedef bool (\*ArkUI\_OnWillDismissEvent)(int32\_t reason)](#arkui_onwilldismissevent) | ArkUI\_OnWillDismissEvent | Defines a pointer to the callback invoked when the dialog box is closed. |
| [void OH\_ArkUI\_DialogDismissEvent\_SetShouldBlockDismiss(ArkUI\_DialogDismissEvent\* event, bool shouldBlockDismiss)](#oh_arkui_dialogdismissevent_setshouldblockdismiss) | \- | Sets whether to block the system behavior of dismissing a dialog box. |
| [void\* OH\_ArkUI\_DialogDismissEvent\_GetUserData(ArkUI\_DialogDismissEvent\* event)](#oh_arkui_dialogdismissevent_getuserdata) | \- | Obtains the pointer to user data in a dialog box dismiss event object. |
| [int32\_t OH\_ArkUI\_DialogDismissEvent\_GetDismissReason(ArkUI\_DialogDismissEvent\* event)](#oh_arkui_dialogdismissevent_getdismissreason) | \- | Obtains the dismissal reason from a dialog box dismiss event object. |
| [int32\_t OH\_ArkUI\_CustomDialog\_OpenDialog(ArkUI\_CustomDialogOptions\* options, void (\*callback)(int32\_t dialogId))](#oh_arkui_customdialog_opendialog) | \- | Displays a custom dialog box. |
| [int32\_t OH\_ArkUI\_CustomDialog\_UpdateDialog(ArkUI\_CustomDialogOptions\* options, void (\*callback)(int32\_t dialogId))](#oh_arkui_customdialog_updatedialog) | \- | Updates a custom dialog box. |
| [int32\_t OH\_ArkUI\_CustomDialog\_CloseDialog(int32\_t dialogId)](#oh_arkui_customdialog_closedialog) | \- | Closes a custom dialog box. |
| [ArkUI\_CustomDialogOptions\* OH\_ArkUI\_CustomDialog\_CreateOptions(ArkUI\_NodeHandle content)](#oh_arkui_customdialog_createoptions) | \- | Creates custom dialog box options. |
| [void OH\_ArkUI\_CustomDialog\_DisposeOptions(ArkUI\_CustomDialogOptions\* options)](#oh_arkui_customdialog_disposeoptions) | \- | Disposes of the custom dialog box options. |
| [int32\_t OH\_ArkUI\_CustomDialog\_SetLevelMode(ArkUI\_CustomDialogOptions\* options, ArkUI\_LevelMode levelMode)](#oh_arkui_customdialog_setlevelmode) | \- | Sets the display level of the dialog box. |
| [int32\_t OH\_ArkUI\_CustomDialog\_SetLevelUniqueId(ArkUI\_CustomDialogOptions\* options, int32\_t uniqueId)](#oh_arkui_customdialog_setleveluniqueid) | \- | Sets the ID of the node under the dialog box's display level. |
| [int32\_t OH\_ArkUI\_CustomDialog\_SetImmersiveMode(ArkUI\_CustomDialogOptions\* options, ArkUI\_ImmersiveMode immersiveMode)](#oh_arkui_customdialog_setimmersivemode) | \- | Sets the display area of the embedded dialog box overlay. |
| [int32\_t OH\_ArkUI\_CustomDialog\_SetBackgroundColor(ArkUI\_CustomDialogOptions\* options, uint32\_t backgroundColor)](#oh_arkui_customdialog_setbackgroundcolor) | \- | Sets the background color of a dialog box. |
| [int32\_t OH\_ArkUI\_CustomDialog\_SetCornerRadius(ArkUI\_CustomDialogOptions\* options, float topLeft, float topRight, float bottomLeft, float bottomRight)](#oh_arkui_customdialog_setcornerradius) | \- | Sets the corner radius for a custom dialog box. |
| [int32\_t OH\_ArkUI\_CustomDialog\_SetBorderWidth(ArkUI\_CustomDialogOptions\* options, float top, float right, float bottom, float left, ArkUI\_LengthMetricUnit unit)](#oh_arkui_customdialog_setborderwidth) | \- | Sets the border width of a dialog box. |
| [int32\_t OH\_ArkUI\_CustomDialog\_SetBorderColor(ArkUI\_CustomDialogOptions\* options, uint32\_t top, uint32\_t right, uint32\_t bottom, uint32\_t left)](#oh_arkui_customdialog_setbordercolor) | \- | Sets the border color of the dialog box. |
| [int32\_t OH\_ArkUI\_CustomDialog\_SetBorderStyle(ArkUI\_CustomDialogOptions\* options, int32\_t top, int32\_t right, int32\_t bottom, int32\_t left)](#oh_arkui_customdialog_setborderstyle) | \- | Sets the border style of a dialog box. |
| [int32\_t OH\_ArkUI\_CustomDialog\_SetWidth(ArkUI\_CustomDialogOptions\* options, float width, ArkUI\_LengthMetricUnit unit)](#oh_arkui_customdialog_setwidth) | \- | Sets the width of the dialog box background. |
| [int32\_t OH\_ArkUI\_CustomDialog\_SetHeight(ArkUI\_CustomDialogOptions\* options, float height, ArkUI\_LengthMetricUnit unit)](#oh_arkui_customdialog_setheight) | \- | Sets the height of the dialog box background. |
| [int32\_t OH\_ArkUI\_CustomDialog\_SetShadow(ArkUI\_CustomDialogOptions\* options, ArkUI\_ShadowStyle shadow)](#oh_arkui_customdialog_setshadow) | \- | Sets the shadow of the dialog box background. |
| [int32\_t OH\_ArkUI\_CustomDialog\_SetCustomShadow(ArkUI\_CustomDialogOptions\* options, const ArkUI\_AttributeItem\* customShadow)](#oh_arkui_customdialog_setcustomshadow) | \- | Sets the shadow of the dialog box background. |
| [int32\_t OH\_ArkUI\_CustomDialog\_SetBackgroundBlurStyle(ArkUI\_CustomDialogOptions\* options, ArkUI\_BlurStyle blurStyle)](#oh_arkui_customdialog_setbackgroundblurstyle) | \- | Sets the background blur style of the dialog box. |
| [int32\_t OH\_ArkUI\_CustomDialog\_SetAlignment(ArkUI\_CustomDialogOptions\* options, int32\_t alignment, float offsetX, float offsetY)](#oh_arkui_customdialog_setalignment) | \- | Sets the alignment mode of a dialog box. |
| [int32\_t OH\_ArkUI\_CustomDialog\_SetModalMode(ArkUI\_CustomDialogOptions\* options, bool isModal)](#oh_arkui_customdialog_setmodalmode) | \- | Sets the modal mode for a custom dialog box. |
| [int32\_t OH\_ArkUI\_CustomDialog\_SetAutoCancel(ArkUI\_CustomDialogOptions\* options, bool autoCancel)](#oh_arkui_customdialog_setautocancel) | \- | Specifies whether to allow users to touch the mask to dismiss the custom dialog box. |
| [int32\_t OH\_ArkUI\_CustomDialog\_SetSubwindowMode(ArkUI\_CustomDialogOptions\* options, bool showInSubwindow)](#oh_arkui_customdialog_setsubwindowmode) | \- | Sets whether to display the dialog box in a subwindow. |
| [int32\_t OH\_ArkUI\_CustomDialog\_SetMask(ArkUI\_CustomDialogOptions\* options, uint32\_t maskColor, const ArkUI\_Rect\* maskRect)](#oh_arkui_customdialog_setmask) | \- | Sets the mask for a custom dialog box. |
| [int32\_t OH\_ArkUI\_CustomDialog\_SetKeyboardAvoidMode(ArkUI\_CustomDialogOptions\* options, ArkUI\_KeyboardAvoidMode keyboardAvoidMode)](#oh_arkui_customdialog_setkeyboardavoidmode) | \- | Sets the keyboard avoidance mode of a dialog box. |
| [int32\_t OH\_ArkUI\_CustomDialog\_SetHoverModeEnabled(ArkUI\_CustomDialogOptions\* options, bool enabled)](#oh_arkui_customdialog_sethovermodeenabled) | \- | Sets whether to enable the hover mode for a dialog box. |
| [int32\_t OH\_ArkUI\_CustomDialog\_SetHoverModeArea(ArkUI\_CustomDialogOptions\* options, ArkUI\_HoverModeAreaType hoverModeAreaType)](#oh_arkui_customdialog_sethovermodearea) | \- | Sets the default display area of a dialog box in hover mode. |
| [int32\_t OH\_ArkUI\_CustomDialog\_RegisterOnWillDismissCallback(ArkUI\_CustomDialogOptions\* options, void\* userData, void (\*callback)(ArkUI\_DialogDismissEvent\* event))](#oh_arkui_customdialog_registeronwilldismisscallback) | \- | Registers a callback for the dismissal event of a custom dialog box. |
| [int32\_t OH\_ArkUI\_CustomDialog\_RegisterOnWillAppearCallback(ArkUI\_CustomDialogOptions\* options, void\* userData, void (\*callback)(void\* userData))](#oh_arkui_customdialog_registeronwillappearcallback) | \- | Registers a callback to be invoked when the specified custom dialog box is about to appear. |
| [int32\_t OH\_ArkUI\_CustomDialog\_RegisterOnDidAppearCallback(ArkUI\_CustomDialogOptions\* options, void\* userData, void (\*callback)(void\* userData))](#oh_arkui_customdialog_registerondidappearcallback) | \- | Registers a callback to be invoked when the specified custom dialog box appears. |
| [int32\_t OH\_ArkUI\_CustomDialog\_RegisterOnWillDisappearCallback(ArkUI\_CustomDialogOptions\* options, void\* userData, void (\*callback)(void\* userData))](#oh_arkui_customdialog_registeronwilldisappearcallback) | \- | Registers a callback to be invoked when the specified custom dialog box is about to disappear. |
| [int32\_t OH\_ArkUI\_CustomDialog\_RegisterOnDidDisappearCallback(ArkUI\_CustomDialogOptions\* options, void\* userData, void (\*callback)(void\* userData))](#oh_arkui_customdialog_registerondiddisappearcallback) | \- | Registers a callback to be invoked when the specified custom dialog box disappears. |
| [int32\_t OH\_ArkUI\_CustomDialog\_GetState(ArkUI\_NativeDialogHandle handle, ArkUI\_DialogState\* state)](#oh_arkui_customdialog_getstate) | \- | Obtains the state of a dialog box. |
| [int32\_t OH\_ArkUI\_CustomDialog\_SetBackgroundBlurStyleOptions(ArkUI\_CustomDialogOptions\* options, const ArkUI\_AttributeItem\* backgroundBlurStyleOptions)](#oh_arkui_customdialog_setbackgroundblurstyleoptions) | \- | Sets the background blur effect for a dialog box. |
| [int32\_t OH\_ArkUI\_CustomDialog\_SetBackgroundEffect(ArkUI\_CustomDialogOptions\* options, const ArkUI\_AttributeItem\* backgroundEffect)](#oh_arkui_customdialog_setbackgroundeffect) | \- | Sets the background effect parameters for a dialog box. |

#### Enum Description

#### \[h2\]ArkUI\_DismissReason

enum ArkUI\_DismissReason

**Description**

Enumerates the actions for triggering closure of the dialog box.

**Since**: 12

| Value | Description |
| :-- | :-- |
| DIALOG\_DISMISS\_BACK\_PRESS = 0 | Touching the Back button, swiping left or right on the screen, or pressing the Esc key. |
| DIALOG\_DISMISS\_TOUCH\_OUTSIDE = 1 | Touching the mask. |
| DIALOG\_DISMISS\_CLOSE\_BUTTON = 2 | Touching the Close button. |
| DIALOG\_DISMISS\_SLIDE\_DOWN = 3 | Sliding down. |

#### \[h2\]ArkUI\_LevelMode

enum ArkUI\_LevelMode

**Description**

Enumerates the display level modes of the dialog box.

**Since**: 15

| Value | Description |
| :-- | :-- |
| ARKUI\_LEVEL\_MODE\_OVERLAY = 0 | The dialog box is displayed above all other application content. |
| ARKUI\_LEVEL\_MODE\_EMBEDDED = 1 | The dialog box is embedded within the application's page content. |

#### \[h2\]ArkUI\_ImmersiveMode

enum ArkUI\_ImmersiveMode

**Description**

Enumerates the display areas of the embedded dialog box overlay.

**Since**: 15

| Value | Description |
| :-- | :-- |
| ARKUI\_IMMERSIVE\_MODE\_DEFAULT = 0 | The dialog box overlay follows the layout constraints of its parent node. |
| ARKUI\_IMMERSIVE\_MODE\_EXTEND = 1 | The dialog box overlay can extend to cover the status bar and navigation bar for a more immersive look. |

#### \[h2\]ArkUI\_DialogState

enum ArkUI\_DialogState

**Description**

Enumerates the dialog box status.

**Since**: 20

| Value | Description |
| :-- | :-- |
| DIALOG\_UNINITIALIZED = 0 | State before the controller is bound to the dialog box. |
| DIALOG\_INITIALIZED = 1 | State after the controller is bound to the dialog box. |
| DIALOG\_APPEARING = 2 | State during the dialog box appearance animation. |
| DIALOG\_APPEARED = 3 | State after the dialog display appearance ends. |
| DIALOG\_DISAPPEARING = 4 | State during the dialog box disappearance animation. |
| DIALOG\_DISAPPEARED = 5 | State after the dialog box disappearance animation ends. |

#### Function Description

#### \[h2\]ArkUI\_OnWillDismissEvent()

typedef bool (\*ArkUI\_OnWillDismissEvent)(int32\_t reason)

**Description**

Defines a pointer to the callback invoked when the dialog box is closed.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| reason | Reason for dialog box dismissal. |

**Return value**

| Type | Description |
| :-- | :-- |
| bool | Any return value indicates that the dialog box will not be closed. |

#### \[h2\]OH\_ArkUI\_DialogDismissEvent\_SetShouldBlockDismiss()

void OH\_ArkUI\_DialogDismissEvent\_SetShouldBlockDismiss(ArkUI\_DialogDismissEvent\* event, bool shouldBlockDismiss)

**Description**

Sets whether to block the system behavior of dismissing a dialog box.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_DialogDismissEvent](../../structs/arkui-dialogdismissevent/document.md)\* event | Pointer to a dialog box dismiss event object. |
| bool shouldBlockDismiss | Whether to block the system behavior of dismissing the dialog box. The value **true** means to block the system behavior, and **false** means the opposite. |

#### \[h2\]OH\_ArkUI\_DialogDismissEvent\_GetUserData()

void\* OH\_ArkUI\_DialogDismissEvent\_GetUserData(ArkUI\_DialogDismissEvent\* event)

**Description**

Obtains the pointer to user data in a dialog box dismiss event object.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_DialogDismissEvent](../../structs/arkui-dialogdismissevent/document.md)\* event | Pointer to a dialog box dismiss event object. |

**Returns**

| Type | Description |
| :-- | :-- |
| void\* | Pointer to user data. |

#### \[h2\]OH\_ArkUI\_DialogDismissEvent\_GetDismissReason()

int32\_t OH\_ArkUI\_DialogDismissEvent\_GetDismissReason(ArkUI\_DialogDismissEvent\* event)

**Description**

Obtains the dismissal reason from a dialog box dismiss event object.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_DialogDismissEvent](../../structs/arkui-dialogdismissevent/document.md)\* event | Pointer to a dialog box dismiss event object. |

**Returns**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Dismissal reason, or **\-1** if an exception occurs.

[DIALOG\_DISMISS\_BACK\_PRESS](#arkui_dismissreason): touching the Back button, swiping left or right on the screen, or pressing the Esc key.

[DIALOG\_DISMISS\_TOUCH\_OUTSIDE](#arkui_dismissreason): touching the mask.

[DIALOG\_DISMISS\_CLOSE\_BUTTON](#arkui_dismissreason): touching the close button.

[DIALOG\_DISMISS\_SLIDE\_DOWN](#arkui_dismissreason): swiping down.

 |

#### \[h2\]OH\_ArkUI\_CustomDialog\_OpenDialog()

int32\_t OH\_ArkUI\_CustomDialog\_OpenDialog(ArkUI\_CustomDialogOptions\* options, void (\*callback)(int32\_t dialogId))

**Description**

Displays a custom dialog box.

**Since**: 19

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_CustomDialogOptions](../../structs/arkui-customdialogoptions/document.md)\* options | Dialog box parameters. |
| void (\*callback)(int32\_t dialogId) | Callback invoked when the dialog box is displayed. The parameter is the dialog box ID. |

**Returns**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Result code.

Returns [ARKUI\_ERROR\_CODE\_NO\_ERROR](../native-type-h/document.md#arkui_errorcode) if the operation is successful.

Returns [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](../native-type-h/document.md#arkui_errorcode) if a parameter error occurs.

 |

#### \[h2\]OH\_ArkUI\_CustomDialog\_UpdateDialog()

int32\_t OH\_ArkUI\_CustomDialog\_UpdateDialog(ArkUI\_CustomDialogOptions\* options, void (\*callback)(int32\_t dialogId))

**Description**

Updates a custom dialog box.

**Since**: 19

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_CustomDialogOptions](../../structs/arkui-customdialogoptions/document.md)\* options | Dialog box parameters. |
| void (\*callback)(int32\_t dialogId) | Callback invoked when the dialog box is updated. The parameter is the dialog box ID. |

**Returns**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Result code.

Returns [ARKUI\_ERROR\_CODE\_NO\_ERROR](../native-type-h/document.md#arkui_errorcode) if the operation is successful.

Returns [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](../native-type-h/document.md#arkui_errorcode) if a parameter error occurs.

 |

#### \[h2\]OH\_ArkUI\_CustomDialog\_CloseDialog()

int32\_t OH\_ArkUI\_CustomDialog\_CloseDialog(int32\_t dialogId)

**Description**

Closes a custom dialog box.

**Since**: 19

**Parameters**

| Name | Description |
| :-- | :-- |
| int32\_t dialogId | ID of the dialog box to close. |

**Returns**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Result code.

Returns [ARKUI\_ERROR\_CODE\_NO\_ERROR](../native-type-h/document.md#arkui_errorcode) if the operation is successful.

Returns [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](../native-type-h/document.md#arkui_errorcode) if a parameter error occurs.

 |

#### \[h2\]OH\_ArkUI\_CustomDialog\_CreateOptions()

ArkUI\_CustomDialogOptions\* OH\_ArkUI\_CustomDialog\_CreateOptions(ArkUI\_NodeHandle content)

**Description**

Creates custom dialog box options.

**Since**: 19

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_NodeHandle](../../structs/arkui-node--00020177/document.md) content | Content of the custom dialog box. |

**Returns**

| Type | Description |
| :-- | :-- |
| [ArkUI\_CustomDialogOptions](../../structs/arkui-customdialogoptions/document.md)\* | Pointer to the custom dialog box configuration. |

#### \[h2\]OH\_ArkUI\_CustomDialog\_DisposeOptions()

void OH\_ArkUI\_CustomDialog\_DisposeOptions(ArkUI\_CustomDialogOptions\* options)

**Description**

Disposes of the custom dialog box options.

**Since**: 19

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_CustomDialogOptions](../../structs/arkui-customdialogoptions/document.md)\* options | Pointer to the custom dialog box configuration. |

#### \[h2\]OH\_ArkUI\_CustomDialog\_SetLevelMode()

int32\_t OH\_ArkUI\_CustomDialog\_SetLevelMode(ArkUI\_CustomDialogOptions\* options, ArkUI\_LevelMode levelMode)

**Description**

Sets the display level of the dialog box.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/16/v3/RXeBe53NQ0uKipn-yCa5bQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062302Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=7E1024B7F0E0F1BAE4AAA03000CB194A973E4D174307D1C5956D93841C3D8CCA)

This API must be called before the [OH\_ArkUI\_CustomDialog\_OpenDialog](#oh_arkui_customdialog_opendialog) API is invoked.

**Since**: 19

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_CustomDialogOptions](../../structs/arkui-customdialogoptions/document.md)\* options | Pointer to the custom dialog box options. |
| [ArkUI\_LevelMode](#arkui_levelmode) levelMode | Display level to set, specified by an enumerated value of [ArkUI\_LevelMode](#arkui_levelmode). |

**Returns**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Result code.

Returns [ARKUI\_ERROR\_CODE\_NO\_ERROR](../native-type-h/document.md#arkui_errorcode) if the operation is successful.

Returns [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](../native-type-h/document.md#arkui_errorcode) if a parameter error occurs.

 |

#### \[h2\]OH\_ArkUI\_CustomDialog\_SetLevelUniqueId()

int32\_t OH\_ArkUI\_CustomDialog\_SetLevelUniqueId(ArkUI\_CustomDialogOptions\* options, int32\_t uniqueId)

**Description**

Sets the ID of the node under the dialog box's display level.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/67/v3/wFw7D5D9SGeEswomZLO6nQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062302Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=FC61958847BE999580B55341FB825A13B11E2A08DE7C91C64538CC9940FDDD1F)

This API must be called before the [OH\_ArkUI\_CustomDialog\_OpenDialog](#oh_arkui_customdialog_opendialog) API is invoked.

**Since**: 19

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_CustomDialogOptions](../../structs/arkui-customdialogoptions/document.md)\* options | Pointer to the custom dialog box options. |
| int32\_t uniqueId | ID of the node under the dialog box's display level. The dialog box will be displayed on the same page as this node. |

**Returns**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Result code.

Returns [ARKUI\_ERROR\_CODE\_NO\_ERROR](../native-type-h/document.md#arkui_errorcode) if the operation is successful.

Returns [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](../native-type-h/document.md#arkui_errorcode) if a parameter error occurs.

 |

#### \[h2\]OH\_ArkUI\_CustomDialog\_SetImmersiveMode()

int32\_t OH\_ArkUI\_CustomDialog\_SetImmersiveMode(ArkUI\_CustomDialogOptions\* options, ArkUI\_ImmersiveMode immersiveMode)

**Description**

Sets the display area of the embedded dialog box overlay.

**Since**: 19

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_CustomDialogOptions](../../structs/arkui-customdialogoptions/document.md)\* options | Pointer to the custom dialog box options. |
| [ArkUI\_ImmersiveMode](#arkui_immersivemode) immersiveMode | Display area, specified by an enumerated value of [ArkUI\_ImmersiveMode](#arkui_immersivemode). |

**Returns**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Result code.

Returns [ARKUI\_ERROR\_CODE\_NO\_ERROR](../native-type-h/document.md#arkui_errorcode) if the operation is successful.

Returns [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](../native-type-h/document.md#arkui_errorcode) if a parameter error occurs.

 |

#### \[h2\]OH\_ArkUI\_CustomDialog\_SetBackgroundColor()

int32\_t OH\_ArkUI\_CustomDialog\_SetBackgroundColor(ArkUI\_CustomDialogOptions\* options, uint32\_t backgroundColor)

**Description**

Sets the background color of a dialog box.

**Since**: 19

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_CustomDialogOptions](../../structs/arkui-customdialogoptions/document.md)\* options | Dialog box parameters. |
| uint32\_t backgroundColor | Background color of the dialog box, in 0xARGB format. |

**Returns**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Result code.

Returns [ARKUI\_ERROR\_CODE\_NO\_ERROR](../native-type-h/document.md#arkui_errorcode) if the operation is successful.

Returns [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](../native-type-h/document.md#arkui_errorcode) if a parameter error occurs.

 |

#### \[h2\]OH\_ArkUI\_CustomDialog\_SetCornerRadius()

int32\_t OH\_ArkUI\_CustomDialog\_SetCornerRadius(ArkUI\_CustomDialogOptions\* options, float topLeft, float topRight, float bottomLeft, float bottomRight)

**Description**

Sets the corner radius for a custom dialog box.

**Since**: 19

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_CustomDialogOptions](../../structs/arkui-customdialogoptions/document.md)\* options | Dialog box parameters. |
| float topLeft | Radius of the upper left corner of the dialog box, in vp. Default value: 32 vp since API version 12; 24 vp in API version 11 and earlier versions. |
| float topRight | Radius of the upper right corner of the dialog box, in vp. Default value: 32 vp since API version 12; 24 vp in API version 11 and earlier versions. |
| float bottomLeft | Radius of the lower left corner of the dialog box, in vp. Default value: 32 vp since API version 12; 24 vp in API version 11 and earlier versions. |
| float bottomRight | Radius of the lower right corner of the dialog box, in vp. Default value: 32 vp since API version 12; 24 vp in API version 11 and earlier versions. |

**Returns**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Result code.

Returns [ARKUI\_ERROR\_CODE\_NO\_ERROR](../native-type-h/document.md#arkui_errorcode) if the operation is successful.

Returns [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](../native-type-h/document.md#arkui_errorcode) if a parameter error occurs.

 |

#### \[h2\]OH\_ArkUI\_CustomDialog\_SetBorderWidth()

int32\_t OH\_ArkUI\_CustomDialog\_SetBorderWidth(ArkUI\_CustomDialogOptions\* options, float top, float right, float bottom, float left, ArkUI\_LengthMetricUnit unit)

**Description**

Sets the border width of a dialog box.

**Since**: 19

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_CustomDialogOptions](../../structs/arkui-customdialogoptions/document.md)\* options | Dialog box parameters. |
| float top | Width of the top border of the dialog box. |
| float right | Width of the right border of the dialog box. |
| float bottom | Width of the bottom border of the dialog box. |
| float left | Width of the left border of the dialog box. |
| [ArkUI\_LengthMetricUnit](../native-type-h/document.md#arkui_lengthmetricunit) unit | Unit of the width. The default value is vp. |

**Returns**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Result code.

Returns [ARKUI\_ERROR\_CODE\_NO\_ERROR](../native-type-h/document.md#arkui_errorcode) if the operation is successful.

Returns [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](../native-type-h/document.md#arkui_errorcode) if a parameter error occurs.

 |

#### \[h2\]OH\_ArkUI\_CustomDialog\_SetBorderColor()

int32\_t OH\_ArkUI\_CustomDialog\_SetBorderColor(ArkUI\_CustomDialogOptions\* options, uint32\_t top, uint32\_t right, uint32\_t bottom, uint32\_t left)

**Description**

Sets the border color of the dialog box.

**Since**: 19

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_CustomDialogOptions](../../structs/arkui-customdialogoptions/document.md)\* options | Dialog box parameters. |
| uint32\_t top | Color of the top border of the dialog box, in 0xARGB format. |
| uint32\_t right | Color of the right border of the dialog box, in 0xARGB format. |
| uint32\_t bottom | Color of the bottom border of the dialog box, in 0xARGB format. |
| uint32\_t left | Color of the left border of the dialog box, in 0xARGB format. |

**Returns**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Result code.

Returns [ARKUI\_ERROR\_CODE\_NO\_ERROR](../native-type-h/document.md#arkui_errorcode) if the operation is successful.

Returns [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](../native-type-h/document.md#arkui_errorcode) if a parameter error occurs.

 |

#### \[h2\]OH\_ArkUI\_CustomDialog\_SetBorderStyle()

int32\_t OH\_ArkUI\_CustomDialog\_SetBorderStyle(ArkUI\_CustomDialogOptions\* options, int32\_t top, int32\_t right, int32\_t bottom, int32\_t left)

**Description**

Sets the border style of a dialog box.

**Since**: 19

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_CustomDialogOptions](../../structs/arkui-customdialogoptions/document.md)\* options | Dialog box parameters. |
| int32\_t top | Style of the top border of the dialog box. The parameter type is [ArkUI\_BorderStyle](../native-type-h/document.md#arkui_borderstyle). The default value is **ARKUI\_BORDER\_STYLE\_SOLID**. |
| int32\_t right | Style of the right border of the dialog box. The parameter type is [ArkUI\_BorderStyle](../native-type-h/document.md#arkui_borderstyle). The default value is **ARKUI\_BORDER\_STYLE\_SOLID**. |
| int32\_t bottom | Style of the bottom border of the dialog box. The parameter type is [ArkUI\_BorderStyle](../native-type-h/document.md#arkui_borderstyle). The default value is **ARKUI\_BORDER\_STYLE\_SOLID**. |
| int32\_t left | Style of the left border of the dialog box. The parameter type is [ArkUI\_BorderStyle](../native-type-h/document.md#arkui_borderstyle). The default value is **ARKUI\_BORDER\_STYLE\_SOLID**. |

**Returns**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Result code.

Returns [ARKUI\_ERROR\_CODE\_NO\_ERROR](../native-type-h/document.md#arkui_errorcode) if the operation is successful.

Returns [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](../native-type-h/document.md#arkui_errorcode) if a parameter error occurs.

 |

#### \[h2\]OH\_ArkUI\_CustomDialog\_SetWidth()

int32\_t OH\_ArkUI\_CustomDialog\_SetWidth(ArkUI\_CustomDialogOptions\* options, float width, ArkUI\_LengthMetricUnit unit)

**Description**

Sets the width of the dialog box background.

**Since**: 19

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_CustomDialogOptions](../../structs/arkui-customdialogoptions/document.md)\* options | Dialog box parameters. |
| float width | Width of the dialog box background. |
| [ArkUI\_LengthMetricUnit](../native-type-h/document.md#arkui_lengthmetricunit) unit | Unit of the width. The default value is vp. |

**Returns**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Result code.

Returns [ARKUI\_ERROR\_CODE\_NO\_ERROR](../native-type-h/document.md#arkui_errorcode) if the operation is successful.

Returns [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](../native-type-h/document.md#arkui_errorcode) if a parameter error occurs.

 |

#### \[h2\]OH\_ArkUI\_CustomDialog\_SetHeight()

int32\_t OH\_ArkUI\_CustomDialog\_SetHeight(ArkUI\_CustomDialogOptions\* options, float height, ArkUI\_LengthMetricUnit unit)

**Description**

Sets the height of the dialog box background.

**Since**: 19

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_CustomDialogOptions](../../structs/arkui-customdialogoptions/document.md)\* options | Dialog box parameters. |
| float height | Height of the dialog box background. |
| [ArkUI\_LengthMetricUnit](../native-type-h/document.md#arkui_lengthmetricunit) unit | Unit of the height. The default value is vp. |

**Returns**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Result code.

Returns [ARKUI\_ERROR\_CODE\_NO\_ERROR](../native-type-h/document.md#arkui_errorcode) if the operation is successful.

Returns [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](../native-type-h/document.md#arkui_errorcode) if a parameter error occurs.

 |

#### \[h2\]OH\_ArkUI\_CustomDialog\_SetShadow()

int32\_t OH\_ArkUI\_CustomDialog\_SetShadow(ArkUI\_CustomDialogOptions\* options, ArkUI\_ShadowStyle shadow)

**Description**

Sets the shadow of the dialog box background.

**Since**: 19

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_CustomDialogOptions](../../structs/arkui-customdialogoptions/document.md)\* options | Dialog box parameters. |
| [ArkUI\_ShadowStyle](../native-type-h/document.md#arkui_shadowstyle) shadow | Shadow style of the background, specified by an enumerated value. |

**Returns**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Result code.

Returns [ARKUI\_ERROR\_CODE\_NO\_ERROR](../native-type-h/document.md#arkui_errorcode) if the operation is successful.

Returns [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](../native-type-h/document.md#arkui_errorcode) if a parameter error occurs.

 |

#### \[h2\]OH\_ArkUI\_CustomDialog\_SetCustomShadow()

int32\_t OH\_ArkUI\_CustomDialog\_SetCustomShadow(ArkUI\_CustomDialogOptions\* options, const ArkUI\_AttributeItem\* customShadow)

**Description**

Sets the shadow of the dialog box background.

**Since**: 19

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_CustomDialogOptions](../../structs/arkui-customdialogoptions/document.md)\* options | Dialog box parameters. |
| [const ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md)\* customShadow | Custom shadow parameters. The format is consistent with the **NODE\_CUSTOM\_SHADOW** property in [ArkUI\_NodeAttributeType](../native-node-h/document.md#arkui_nodeattributetype). |

**Returns**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Result code.

Returns [ARKUI\_ERROR\_CODE\_NO\_ERROR](../native-type-h/document.md#arkui_errorcode) if the operation is successful.

Returns [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](../native-type-h/document.md#arkui_errorcode) if a parameter error occurs.

 |

#### \[h2\]OH\_ArkUI\_CustomDialog\_SetBackgroundBlurStyle()

int32\_t OH\_ArkUI\_CustomDialog\_SetBackgroundBlurStyle(ArkUI\_CustomDialogOptions\* options, ArkUI\_BlurStyle blurStyle)

**Description**

Sets the background blur style of the dialog box.

**Since**: 19

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_CustomDialogOptions](../../structs/arkui-customdialogoptions/document.md)\* options | Dialog box parameters. |
| [ArkUI\_BlurStyle](../native-type-h/document.md#arkui_blurstyle) blurStyle | Background blur style, specified by an enumerated value. |

**Returns**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Result code.

Returns [ARKUI\_ERROR\_CODE\_NO\_ERROR](../native-type-h/document.md#arkui_errorcode) if the operation is successful.

Returns [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](../native-type-h/document.md#arkui_errorcode) if a parameter error occurs.

 |

#### \[h2\]OH\_ArkUI\_CustomDialog\_SetAlignment()

int32\_t OH\_ArkUI\_CustomDialog\_SetAlignment(ArkUI\_CustomDialogOptions\* options, int32\_t alignment, float offsetX, float offsetY)

**Description**

Sets the alignment mode of a dialog box.

**Since**: 19

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_CustomDialogOptions](../../structs/arkui-customdialogoptions/document.md)\* options | Dialog box parameters. |
| int32\_t alignment | Alignment mode of the dialog box. The parameter type is [ArkUI\_Alignment](../native-type-h/document.md#arkui_alignment). |
| float offsetX | Horizontal offset of the dialog box. The value is a floating point number, in vp. |
| float offsetY | Vertical offset of the dialog box. The value is a floating point number, in vp. |

**Returns**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Result code.

Returns [ARKUI\_ERROR\_CODE\_NO\_ERROR](../native-type-h/document.md#arkui_errorcode) if the operation is successful.

Returns [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](../native-type-h/document.md#arkui_errorcode) if a parameter error occurs.

 |

#### \[h2\]OH\_ArkUI\_CustomDialog\_SetModalMode()

int32\_t OH\_ArkUI\_CustomDialog\_SetModalMode(ArkUI\_CustomDialogOptions\* options, bool isModal)

**Description**

Sets the modal mode for a custom dialog box.

**Since**: 19

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_CustomDialogOptions](../../structs/arkui-customdialogoptions/document.md)\* options | Dialog box parameters. |
| bool isModal | 
Whether the dialog box is a modal. A modal dialog box has a mask applied, while a non-modal dialog box does not. The value **true** means that the dialog box is a modal, and **false** means the opposite.

Default value: **false**.

 |

**Returns**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Result code.

Returns [ARKUI\_ERROR\_CODE\_NO\_ERROR](../native-type-h/document.md#arkui_errorcode) if the operation is successful.

Returns [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](../native-type-h/document.md#arkui_errorcode) if a parameter error occurs.

 |

#### \[h2\]OH\_ArkUI\_CustomDialog\_SetAutoCancel()

int32\_t OH\_ArkUI\_CustomDialog\_SetAutoCancel(ArkUI\_CustomDialogOptions\* options, bool autoCancel)

**Description**

Specifies whether to allow users to touch the mask to dismiss the custom dialog box.

**Since**: 19

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_CustomDialogOptions](../../structs/arkui-customdialogoptions/document.md)\* options | Dialog box parameters. |
| bool autoCancel | 
Whether to allow users to touch the mask to dismiss the dialog box. The value **true** means to allow users to do so, and **false** means the opposite.

Default value: **true**

 |

**Returns**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Result code.

Returns [ARKUI\_ERROR\_CODE\_NO\_ERROR](../native-type-h/document.md#arkui_errorcode) if the operation is successful.

Returns [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](../native-type-h/document.md#arkui_errorcode) if a parameter error occurs.

 |

#### \[h2\]OH\_ArkUI\_CustomDialog\_SetSubwindowMode()

int32\_t OH\_ArkUI\_CustomDialog\_SetSubwindowMode(ArkUI\_CustomDialogOptions\* options, bool showInSubwindow)

**Description**

Sets whether to display the dialog box in a subwindow.

**Since**: 19

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_CustomDialogOptions](../../structs/arkui-customdialogoptions/document.md)\* options | Dialog box parameters. |
| bool showInSubwindow | 
Whether to show the dialog box in a subwindow when the dialog box needs to be displayed outside the main window. If the value is **true**, the dialog box can be displayed in an independent subwindow outside the main window. If the value is **false**, the dialog box is displayed within the application, not in an independent subwindow.

Default value: **false**.

 |

**Returns**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Result code.

Returns [ARKUI\_ERROR\_CODE\_NO\_ERROR](../native-type-h/document.md#arkui_errorcode) if the operation is successful.

Returns [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](../native-type-h/document.md#arkui_errorcode) if a parameter error occurs.

 |

#### \[h2\]OH\_ArkUI\_CustomDialog\_SetMask()

int32\_t OH\_ArkUI\_CustomDialog\_SetMask(ArkUI\_CustomDialogOptions\* options, uint32\_t maskColor, const ArkUI\_Rect\* maskRect)

**Description**

Sets the mask for a custom dialog box.

**Since**: 19

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_CustomDialogOptions](../../structs/arkui-customdialogoptions/document.md)\* options | Dialog box parameters. |
| uint32\_t maskColor | Mask color, in 0xargb format. |
| [const ArkUI\_Rect](../../structs/arkui-rect/document.md)\* maskRect | Pointer to the mask area. Events outside the mask area are transparently transmitted, and events within the mask area are not. The parameter type is [ArkUI\_Rect](../../structs/arkui-rect/document.md). |

**Returns**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Result code.

Returns [ARKUI\_ERROR\_CODE\_NO\_ERROR](../native-type-h/document.md#arkui_errorcode) if the operation is successful.

Returns [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](../native-type-h/document.md#arkui_errorcode) if a parameter error occurs.

 |

#### \[h2\]OH\_ArkUI\_CustomDialog\_SetKeyboardAvoidMode()

int32\_t OH\_ArkUI\_CustomDialog\_SetKeyboardAvoidMode(ArkUI\_CustomDialogOptions\* options, ArkUI\_KeyboardAvoidMode keyboardAvoidMode)

**Description**

Sets the keyboard avoidance mode of a dialog box.

**Since**: 19

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_CustomDialogOptions](../../structs/arkui-customdialogoptions/document.md)\* options | Dialog box parameters. |
| [ArkUI\_KeyboardAvoidMode](../native-type-h/document.md#arkui_keyboardavoidmode) keyboardAvoidMode | Keyboard avoidance mode, specified by an enumerated value. |

**Returns**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Result code.

Returns [ARKUI\_ERROR\_CODE\_NO\_ERROR](../native-type-h/document.md#arkui_errorcode) if the operation is successful.

Returns [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](../native-type-h/document.md#arkui_errorcode) if a parameter error occurs.

 |

#### \[h2\]OH\_ArkUI\_CustomDialog\_SetHoverModeEnabled()

int32\_t OH\_ArkUI\_CustomDialog\_SetHoverModeEnabled(ArkUI\_CustomDialogOptions\* options, bool enabled)

**Description**

Sets whether to enable the hover mode for a dialog box.

**Since**: 19

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_CustomDialogOptions](../../structs/arkui-customdialogoptions/document.md)\* options | Dialog box parameters. |
| bool enabled | Whether to respond when the device is in semi-folded mode. The default value is **false**. The value **true** means to respond when the device is in semi-folded mode, and **false** means the opposite. |

**Returns**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Result code.

Returns [ARKUI\_ERROR\_CODE\_NO\_ERROR](../native-type-h/document.md#arkui_errorcode) if the operation is successful.

Returns [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](../native-type-h/document.md#arkui_errorcode) if a parameter error occurs.

 |

#### \[h2\]OH\_ArkUI\_CustomDialog\_SetHoverModeArea()

int32\_t OH\_ArkUI\_CustomDialog\_SetHoverModeArea(ArkUI\_CustomDialogOptions\* options, ArkUI\_HoverModeAreaType hoverModeAreaType)

**Description**

Sets the default display area of a dialog box in hover mode.

**Since**: 19

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_CustomDialogOptions](../../structs/arkui-customdialogoptions/document.md)\* options | Dialog box parameters. |
| [ArkUI\_HoverModeAreaType](../native-type-h/document.md#arkui_hovermodeareatype) hoverModeAreaType | Display area in hover mode, specified by an enumerated value. |

**Returns**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Result code.

Returns [ARKUI\_ERROR\_CODE\_NO\_ERROR](../native-type-h/document.md#arkui_errorcode) if the operation is successful.

Returns [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](../native-type-h/document.md#arkui_errorcode) if a parameter error occurs.

 |

#### \[h2\]OH\_ArkUI\_CustomDialog\_RegisterOnWillDismissCallback()

int32\_t OH\_ArkUI\_CustomDialog\_RegisterOnWillDismissCallback(ArkUI\_CustomDialogOptions\* options, void\* userData, void (\*callback)(ArkUI\_DialogDismissEvent\* event))

**Description**

Registers a callback for the dismissal event of a custom dialog box.

**Since**: 19

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_CustomDialogOptions](../../structs/arkui-customdialogoptions/document.md)\* options | Dialog box parameters. |
| void\* userData | Pointer to user data. |
| void (\*callback)(ArkUI\_DialogDismissEvent\* event) | 
Callback for the dismissal event of the custom dialog box.

\- **event**: input parameter of the callback, which captures the reason for dismissal.

 |

**Returns**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Result code.

Returns [ARKUI\_ERROR\_CODE\_NO\_ERROR](../native-type-h/document.md#arkui_errorcode) if the operation is successful.

Returns [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](../native-type-h/document.md#arkui_errorcode) if a parameter error occurs.

 |

#### \[h2\]OH\_ArkUI\_CustomDialog\_RegisterOnWillAppearCallback()

int32\_t OH\_ArkUI\_CustomDialog\_RegisterOnWillAppearCallback(ArkUI\_CustomDialogOptions\* options, void\* userData, void (\*callback)(void\* userData))

**Description**

Registers a callback to be invoked when the specified custom dialog box is about to appear.

**Since**: 19

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_CustomDialogOptions](../../structs/arkui-customdialogoptions/document.md)\* options | Dialog box parameters. |
| void\* userData | Pointer to user data. |
| void (\*callback)(void\* userData) | Event callback before the dialog box appearance animation. |

**Returns**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Result code.

Returns [ARKUI\_ERROR\_CODE\_NO\_ERROR](../native-type-h/document.md#arkui_errorcode) if the operation is successful.

Returns [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](../native-type-h/document.md#arkui_errorcode) if a parameter error occurs.

 |

#### \[h2\]OH\_ArkUI\_CustomDialog\_RegisterOnDidAppearCallback()

int32\_t OH\_ArkUI\_CustomDialog\_RegisterOnDidAppearCallback(ArkUI\_CustomDialogOptions\* options, void\* userData, void (\*callback)(void\* userData))

**Description**

Registers a callback to be invoked when the specified custom dialog box appears.

**Since**: 19

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_CustomDialogOptions](../../structs/arkui-customdialogoptions/document.md)\* options | Dialog box parameters. |
| void\* userData | Pointer to user data. |
| void (\*callback)(void\* userData) | Event callback after the dialog box appears. |

**Returns**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Result code.

Returns [ARKUI\_ERROR\_CODE\_NO\_ERROR](../native-type-h/document.md#arkui_errorcode) if the operation is successful.

Returns [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](../native-type-h/document.md#arkui_errorcode) if a parameter error occurs.

 |

#### \[h2\]OH\_ArkUI\_CustomDialog\_RegisterOnWillDisappearCallback()

int32\_t OH\_ArkUI\_CustomDialog\_RegisterOnWillDisappearCallback(ArkUI\_CustomDialogOptions\* options, void\* userData, void (\*callback)(void\* userData))

**Description**

Registers a callback to be invoked when the specified custom dialog box is about to disappear.

**Since**: 19

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_CustomDialogOptions](../../structs/arkui-customdialogoptions/document.md)\* options | Dialog box parameters. |
| void\* userData | Pointer to user data. |
| void (\*callback)(void\* userData) | Event callback before the dialog box disappearance animation. |

**Returns**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Result code.

Returns [ARKUI\_ERROR\_CODE\_NO\_ERROR](../native-type-h/document.md#arkui_errorcode) if the operation is successful.

Returns [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](../native-type-h/document.md#arkui_errorcode) if a parameter error occurs.

 |

#### \[h2\]OH\_ArkUI\_CustomDialog\_RegisterOnDidDisappearCallback()

int32\_t OH\_ArkUI\_CustomDialog\_RegisterOnDidDisappearCallback(ArkUI\_CustomDialogOptions\* options, void\* userData, void (\*callback)(void\* userData))

**Description**

Registers a callback to be invoked when the specified custom dialog box disappears.

**Since**: 19

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_CustomDialogOptions](../../structs/arkui-customdialogoptions/document.md)\* options | Dialog box parameters. |
| void\* userData | Pointer to user data. |
| void (\*callback)(void\* userData) | Event callback when the dialog box disappears. |

**Returns**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Result code.

Returns [ARKUI\_ERROR\_CODE\_NO\_ERROR](../native-type-h/document.md#arkui_errorcode) if the operation is successful.

Returns [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](../native-type-h/document.md#arkui_errorcode) if a parameter error occurs.

 |

#### \[h2\]OH\_ArkUI\_CustomDialog\_GetState()

int32\_t OH\_ArkUI\_CustomDialog\_GetState(ArkUI\_NativeDialogHandle handle, ArkUI\_DialogState\* state)

**Description**

Obtains the state of a dialog box.

**Since**: 20

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_NativeDialogHandle](../../structs/arkui-nativedialog--00020177/document.md) handle | Pointer to the custom dialog box controller. |
| [ArkUI\_DialogState](#arkui_dialogstate)\* state | Enumerates states of the custom dialog box. |

**Returns**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Result code.

Returns [ARKUI\_ERROR\_CODE\_NO\_ERROR](../native-type-h/document.md#arkui_errorcode) if the operation is successful.

Returns [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](../native-type-h/document.md#arkui_errorcode) if a parameter error occurs.

 |

#### \[h2\]OH\_ArkUI\_CustomDialog\_SetBackgroundBlurStyleOptions()

int32\_t OH\_ArkUI\_CustomDialog\_SetBackgroundBlurStyleOptions(ArkUI\_CustomDialogOptions\* options, const ArkUI\_AttributeItem\* backgroundBlurStyleOptions)

**Description**

Sets the background blur effect for a dialog box.

**Since**: 19

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_CustomDialogOptions](../../structs/arkui-customdialogoptions/document.md)\* options | Dialog box parameters. |
| [const ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md)\* backgroundBlurStyleOptions | 
Background blur effect for the dialog box. The format of the [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md) parameter is as follows:

.value\[0\].i32: color mode, specified by an enumerated value of [ArkUI\_ColorMode](../native-type-h/document.md#arkui_colormode).

.value\[1\]?.i32: adaptive color mode, specified by an enumerated value of [ArkUI\_AdaptiveColor](../native-type-h/document.md#arkui_adaptivecolor).

.value\[2\]?.f32: blur degree. The value range is \[0.0, 1.0\]. If the value is out of the valid range, the boundary value is used.

.value\[3\]?.u32: brightness of black in the grayscale blur. The value range is \[0, 127\]. If the value is out of the valid range, **0** is used.

.value\[4\]?.u32: darkening degree of white in the grayscale blur. The value range is \[0, 127\]. If the value is out of the valid range, **0** is used.

.value\[5\]?.i32: blur activation policy, specified by an enumerated value of [ArkUI\_BlurStyleActivePolicy](../native-type-h/document.md#arkui_blurstyleactivepolicy).

.value\[6\]?.u32: background color, in 0xARGB format, of the components within the window after the window loses focus (in which case, the blur effect on the components within the window is removed).

 |

**Returns**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Result code.

Returns [ARKUI\_ERROR\_CODE\_NO\_ERROR](../native-type-h/document.md#arkui_errorcode) if the operation is successful.

Returns [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](../native-type-h/document.md#arkui_errorcode) if a parameter error occurs.

 |

#### \[h2\]OH\_ArkUI\_CustomDialog\_SetBackgroundEffect()

int32\_t OH\_ArkUI\_CustomDialog\_SetBackgroundEffect(ArkUI\_CustomDialogOptions\* options, const ArkUI\_AttributeItem\* backgroundEffect)

**Description**

Sets the background effect parameters for a dialog box.

**Since**: 19

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_CustomDialogOptions](../../structs/arkui-customdialogoptions/document.md)\* options | Dialog box parameters. |
| [const ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md)\* backgroundEffect | 
Background effect of the dialog box. The format of the [ArkUI\_AttributeItem](../../structs/arkui-attributeitem/document.md) parameter is as follows:

.value\[0\].f32: blur radius, in vp.

.value\[1\]?.f32: saturation.

.value\[2\]?.f32: brightness.

.value\[3\]?.u32: color, in 0xARGB format.

.value\[4\]?.i32: adaptive color mode, specified by an enumerated value of [ArkUI\_AdaptiveColor](../native-type-h/document.md#arkui_adaptivecolor).

.value\[5\]?.u32: brightness of black in the grayscale blur. The value range is \[0, 127\]. If the value is out of the valid range, **0** is used.

.value\[6\]?.u32: darkening degree of white in the grayscale blur. The value range is \[0, 127\]. If the value is out of the valid range, **0** is used.

.value\[7\]?.i32: blur activation policy, specified by an enumerated value of [ArkUI\_BlurStyleActivePolicy](../native-type-h/document.md#arkui_blurstyleactivepolicy).

.value\[8\]?.u32: background color, in 0xARGB format, of the components within the window after the window loses focus (in which case, the blur effect on the components within the window is removed).

 |

**Returns**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Result code.

Returns [ARKUI\_ERROR\_CODE\_NO\_ERROR](../native-type-h/document.md#arkui_errorcode) if the operation is successful.

Returns [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](../native-type-h/document.md#arkui_errorcode) if a parameter error occurs.

 |
