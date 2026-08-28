# ArkUI\_NativeDialogAPI\_2

typedef struct {...} ArkUI\_NativeDialogAPI\_2

#### Overview

Provides a collection of native-side custom dialog box APIs provided by ArkUI.

**Since**: 15

**Related module**: [ArkUI\_NativeModule](../../modules/arkui-nativemodule/document.md)

**Header file**: [native\_dialog.h](../../header-files/native-dialog-h/document.md)

#### Summary

#### \[h2\]Member Variables

| Name | Description |
| :-- | :-- |
| [ArkUI\_NativeDialogAPI\_1](../arkui-nativedialogapi-1/document.md) nativeDialogAPI1 | 
Collection of native-side custom dialog box APIs provided by ArkUI, covering the scope of [ArkUI\_NativeDialogAPI\_1](../arkui-nativedialogapi-1/document.md).

**Since**: 15

 |

#### \[h2\]Member Functions

| Name | Description |
| :-- | :-- |
| [int32\_t (\*setKeyboardAvoidDistance)(ArkUI\_NativeDialogHandle handle, float distance, ArkUI\_LengthMetricUnit unit)](#setkeyboardavoiddistance) | Distance between the dialog box and the keyboard after keyboard avoidance is applied. |
| [int32\_t (\*setLevelMode)(ArkUI\_NativeDialogHandle handle, ArkUI\_LevelMode levelMode)](#setlevelmode) | Sets the display level of a dialog box. |
| [int32\_t (\*setLevelUniqueId)(ArkUI\_NativeDialogHandle handle, int32\_t uniqueId)](#setleveluniqueid) | Sets the ID of the node under the dialog box's display level. |
| [int32\_t (\*setImmersiveMode)(ArkUI\_NativeDialogHandle handle, ArkUI\_ImmersiveMode immersiveMode)](#setimmersivemode) | Sets the display area of the embedded dialog box overlay. |

#### Member Function Description

#### \[h2\]setKeyboardAvoidDistance()

int32\_t (\*setKeyboardAvoidDistance)(ArkUI\_NativeDialogHandle handle, float distance, ArkUI\_LengthMetricUnit unit)

**Description**

Distance between the dialog box and the keyboard after keyboard avoidance is applied.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/76/v3/rsscwRyqS0S_KmFIhnRLMQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062305Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=BF26218025E29085EAAC8B3D85581F4338BC44FC615B2E2E1C353B69E7708DD7)

This API must be called before the [show](../arkui-nativedialogapi-1/document.md#show) API is invoked.

**Since**: 15

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_NativeDialogHandle](../arkui-nativedialog--00020177/document.md) handle | Pointer to the custom dialog box controller. |
| float distance | Distance to avoid the keyboard, in vp by default. |
| [ArkUI\_LengthMetricUnit](../../header-files/native-type-h/document.md#arkui_lengthmetricunit) unit | Unit of the avoidance distance. The parameter type is [ArkUI\_LengthMetricUnit](../../header-files/native-type-h/document.md#arkui_lengthmetricunit). |

**Returns**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Result code.

Returns [ARKUI\_ERROR\_CODE\_NO\_ERROR](../../header-files/native-type-h/document.md#arkui_errorcode) if the operation is successful.

Returns [ARKUI\_ERROR\_CODE\_CAPI\_INIT\_ERROR](../../header-files/native-type-h/document.md#arkui_errorcode) if API initialization failed.

Returns [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](../../header-files/native-type-h/document.md#arkui_errorcode) if a parameter error occurs.

 |

#### \[h2\]setLevelMode()

int32\_t (\*setLevelMode)(ArkUI\_NativeDialogHandle handle, ArkUI\_LevelMode levelMode)

**Description**

Sets the display level of a dialog box.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b4/v3/KBMRYVRmSqWoo_RhmoJ-bA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062305Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=BD6E891B29670486251FDA719D34440DD2B364B10AA098EDBFDE690AEEC531BF)

This API must be called before the [show](../arkui-nativedialogapi-1/document.md#show) API is invoked.

**Since**: 15

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_NativeDialogHandle](../arkui-nativedialog--00020177/document.md) handle | Pointer to the custom dialog box controller. |
| [ArkUI\_LevelMode](../../header-files/native-dialog-h/document.md#arkui_levelmode) levelMode | Display level to set, specified by an enumerated value of [ArkUI\_LevelMode](../../header-files/native-dialog-h/document.md#arkui_levelmode). |

**Returns**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Result code.

Returns [ARKUI\_ERROR\_CODE\_NO\_ERROR](../../header-files/native-type-h/document.md#arkui_errorcode) if the operation is successful.

Returns [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](../../header-files/native-type-h/document.md#arkui_errorcode) if a parameter error occurs.

 |

#### \[h2\]setLevelUniqueId()

int32\_t (\*setLevelUniqueId)(ArkUI\_NativeDialogHandle handle, int32\_t uniqueId)

**Description**

Sets the ID of the node under the dialog box's display level.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/32/v3/580xqBWKRxCp5tfYy8_JnA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062305Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=569891273109A6050401368D5C887734759314047B00E5C18E0D34969142DA99)

This API must be called before the [setLevelMode](#setlevelmode) API is invoked.

**Since**: 15

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_NativeDialogHandle](../arkui-nativedialog--00020177/document.md) handle | Pointer to the custom dialog box controller. |
| int32\_t uniqueId | ID of the node under the dialog box's display level. The dialog box will be displayed on the same page as this node. |

**Returns**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Result code.

Returns [ARKUI\_ERROR\_CODE\_NO\_ERROR](../../header-files/native-type-h/document.md#arkui_errorcode) if the operation is successful.

Returns [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](../../header-files/native-type-h/document.md#arkui_errorcode) if a parameter error occurs.

 |

#### \[h2\]setImmersiveMode()

int32\_t (\*setImmersiveMode)(ArkUI\_NativeDialogHandle handle, ArkUI\_ImmersiveMode immersiveMode)

**Description**

Sets the display area of the embedded dialog box overlay.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/47/v3/fRJi-SmuQ_6RFDi5B6gd8A/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062305Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=AEE98F20491C69640D3834AF7C083AD45F2991DED7DB4C2B2233E071FAB1B7DE)

This API must be called before the [show](../arkui-nativedialogapi-1/document.md#show) API is invoked.

**Since**: 15

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_NativeDialogHandle](../arkui-nativedialog--00020177/document.md) handle | Pointer to the custom dialog box controller. |
| [ArkUI\_ImmersiveMode](../../header-files/native-dialog-h/document.md#arkui_immersivemode) immersiveMode | Display area, specified by an enumerated value of [ArkUI\_ImmersiveMode](../../header-files/native-dialog-h/document.md#arkui_immersivemode). |

**Returns**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Result code.

Returns [ARKUI\_ERROR\_CODE\_NO\_ERROR](../../header-files/native-type-h/document.md#arkui_errorcode) if the operation is successful.

Returns [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](../../header-files/native-type-h/document.md#arkui_errorcode) if a parameter error occurs.

 |
