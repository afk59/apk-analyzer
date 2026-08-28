# ArkUI\_NativeDialogAPI\_3

typedef struct {...} ArkUI\_NativeDialogAPI\_3

#### Overview

Provides a collection of native-side custom dialog box APIs provided by ArkUI.

**Since**: 19

**Related module**: [ArkUI\_NativeModule](../../modules/arkui-nativemodule/document.md)

**Header file**: [native\_dialog.h](../../header-files/native-dialog-h/document.md)

#### Summary

#### \[h2\]Member Variables

| Name | Description |
| :-- | :-- |
| [ArkUI\_NativeDialogAPI\_1](../arkui-nativedialogapi-1/document.md) nativeDialogAPI1 | 
Collection of native-side custom dialog box APIs provided by ArkUI, covering the scope of [ArkUI\_NativeDialogAPI\_1](../arkui-nativedialogapi-1/document.md).

**Since**: 19

 |
| [ArkUI\_NativeDialogAPI\_2](../arkui-nativedialogapi-2/document.md) nativeDialogAPI2 | 

Collection of native-side custom dialog box APIs provided by ArkUI, covering the scope of [ArkUI\_NativeDialogAPI\_2](../arkui-nativedialogapi-2/document.md).

**Since**: 19

 |

#### \[h2\]Member Functions

| Name | Description |
| :-- | :-- |
| [int32\_t (\*setLevelOrder)(ArkUI\_NativeDialogHandle handle, double levelOrder)](#setlevelorder) | Sets the display order of the custom dialog box. |
| [int32\_t (\*registerOnWillAppear)(ArkUI\_NativeDialogHandle handle, void\* userData, void (\*callback)(void\* userData))](#registeronwillappear) | Registers a callback function that is triggered before the custom dialog box appears. |
| [int32\_t (\*registerOnDidAppear)(ArkUI\_NativeDialogHandle handle, void\* userData, void (\*callback)(void\* userData))](#registerondidappear) | Registers a callback function that is triggered after the custom dialog box appears. |
| [int32\_t (\*registerOnWillDisappear)(ArkUI\_NativeDialogHandle handle, void\* userData, void (\*callback)(void\* userData))](#registeronwilldisappear) | Registers a callback function that is triggered before the custom dialog box disappears. |
| [int32\_t (\*registerOnDidDisappear)(ArkUI\_NativeDialogHandle handle, void\* userData, void (\*callback)(void\* userData))](#registerondiddisappear) | Registers a callback function that is triggered after the custom dialog box disappears. |
| [int32\_t (\*setBorderWidth)(ArkUI\_NativeDialogHandle handle, float top, float right, float bottom, float left, ArkUI\_LengthMetricUnit unit)](#setborderwidth) | Sets the border width of the custom dialog box. |
| [int32\_t (\*setBorderColor)(ArkUI\_NativeDialogHandle handle, uint32\_t top, uint32\_t right, uint32\_t bottom, uint32\_t left)](#setbordercolor) | Sets the border color of the custom dialog box. |
| [int32\_t (\*setBorderStyle)(ArkUI\_NativeDialogHandle handle, int32\_t top, int32\_t right, int32\_t bottom, int32\_t left)](#setborderstyle) | Sets the border style of the custom dialog box. |
| [int32\_t (\*setWidth)(ArkUI\_NativeDialogHandle handle, float width, ArkUI\_LengthMetricUnit unit)](#setwidth) | Sets the backdrop width of the custom dialog box. |
| [int32\_t (\*setHeight)(ArkUI\_NativeDialogHandle handle, float height, ArkUI\_LengthMetricUnit unit)](#setheight) | Sets the backdrop height of the custom dialog box. |
| [int32\_t (\*setShadow)(ArkUI\_NativeDialogHandle handle, ArkUI\_ShadowStyle shadow)](#setshadow) | Sets the shadow of the custom dialog box's backdrop. |
| [int32\_t (\*setCustomShadow)(ArkUI\_NativeDialogHandle handle, const ArkUI\_AttributeItem\* customShadow)](#setcustomshadow) | Sets the shadow of the custom dialog box's backdrop. |
| [int32\_t (\*setBackgroundBlurStyle)(ArkUI\_NativeDialogHandle handle, ArkUI\_BlurStyle blurStyle)](#setbackgroundblurstyle) | Sets the backdrop blur style of the custom dialog box. |
| [int32\_t (\*setKeyboardAvoidMode)(ArkUI\_NativeDialogHandle handle, ArkUI\_KeyboardAvoidMode keyboardAvoidMode)](#setkeyboardavoidmode) | Sets the keyboard avoidance mode of the custom dialog box. |
| [int32\_t (\*enableHoverMode)(ArkUI\_NativeDialogHandle handle, bool enableHoverMode)](#enablehovermode) | Sets whether the custom dialog box responds when the device is in semi-folded mode. |
| [int32\_t (\*setHoverModeArea)(ArkUI\_NativeDialogHandle handle, ArkUI\_HoverModeAreaType hoverModeAreaType)](#sethovermodearea) | Sets the default display area of the custom dialog box in hover mode. |
| [int32\_t (\*setFocusable)(ArkUI\_NativeDialogHandle handle, bool focusable)](#setfocusable) | Sets whether the custom dialog box can gain focus. |
| [int32\_t (\*setBackgroundBlurStyleOptions)(ArkUI\_NativeDialogHandle handle, const ArkUI\_AttributeItem\* backgroundBlurStyleOptions)](#setbackgroundblurstyleoptions) | Sets the background blur effect of the custom dialog box. |
| [int32\_t (\*setBackgroundEffect)(ArkUI\_NativeDialogHandle handle, const ArkUI\_AttributeItem\* backgroundEffect)](#setbackgroundeffect) | Sets the background effect parameters of the custom dialog box. |

#### Member Function Description

#### \[h2\]setLevelOrder()

int32\_t (\*setLevelOrder)(ArkUI\_NativeDialogHandle handle, double levelOrder)

**Description**

Sets the display order of the custom dialog box.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c2/v3/_fSfBWjRR3OKNfqAoYlZYg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062305Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=0CEDF9E5E0777EEAD890C9C6A95C814176FE3B3729E187C2927F71F8A7BE1FCA)

This API must be called before the [show](../arkui-nativedialogapi-1/document.md#show) API is invoked.

**Since**: 19

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_NativeDialogHandle](../arkui-nativedialog--00020177/document.md) handle | Pointer to the custom dialog box controller. |
| double levelOrder | 
Display order of the custom dialog box.

Default value: **0**. Value range: \[-100000.0, 100000.0\]. If the value is out of the range, the setting does not take effect.

 |

**Returns**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Result code.

Returns [ARKUI\_ERROR\_CODE\_NO\_ERROR](../../header-files/native-type-h/document.md#arkui_errorcode) if the operation is successful.

Returns [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](../../header-files/native-type-h/document.md#arkui_errorcode) if a parameter error occurs.

 |

#### \[h2\]registerOnWillAppear()

int32\_t (\*registerOnWillAppear)(ArkUI\_NativeDialogHandle handle, void\* userData, void (\*callback)(void\* userData))

**Description**

Registers a callback function that is triggered before the custom dialog box appears.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/33/v3/mSMGUqrrSjG-gIcE1kSEwA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062305Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=57901C9DD91585E681696DFC80622029E91509778C97D6DFF08B99EECDF395D1)

This API must be called before the [show](../arkui-nativedialogapi-1/document.md#show) API is invoked.

**Since**: 19

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_NativeDialogHandle](../arkui-nativedialog--00020177/document.md) handle | Pointer to the custom dialog box controller. |
| void\* userData | Custom data. |
| callback | Callback function that is triggered before the custom dialog box appears. |

**Returns**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Result code.

Returns [ARKUI\_ERROR\_CODE\_NO\_ERROR](../../header-files/native-type-h/document.md#arkui_errorcode) if the operation is successful.

Returns [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](../../header-files/native-type-h/document.md#arkui_errorcode) if a parameter error occurs.

 |

#### \[h2\]registerOnDidAppear()

int32\_t (\*registerOnDidAppear)(ArkUI\_NativeDialogHandle handle, void\* userData, void (\*callback)(void\* userData))

**Description**

Registers a callback function that is triggered after the custom dialog box appears.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5b/v3/DAjCFU9wSGO9c9Hv__IA9w/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062305Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=2906002F8CF4903885F190F8031EEA24203DB4BE3311961582E52E0D9B5B20DF)

This API must be called before the [show](../arkui-nativedialogapi-1/document.md#show) API is invoked.

**Since**: 19

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_NativeDialogHandle](../arkui-nativedialog--00020177/document.md) handle | Pointer to the custom dialog box controller. |
| void\* userData | Custom data. |
| callback | Callback function that is triggered after the custom dialog box appears. |

**Returns**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Result code.

Returns [ARKUI\_ERROR\_CODE\_NO\_ERROR](../../header-files/native-type-h/document.md#arkui_errorcode) if the operation is successful.

Returns [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](../../header-files/native-type-h/document.md#arkui_errorcode) if a parameter error occurs.

 |

#### \[h2\]registerOnWillDisappear()

int32\_t (\*registerOnWillDisappear)(ArkUI\_NativeDialogHandle handle, void\* userData, void (\*callback)(void\* userData))

**Description**

Registers a callback function that is triggered before the custom dialog box disappears.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/88/v3/1VEZKvmBQKW-ut3UMr2vsg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062305Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=69BED53565AE17B3A257C55AEF25C34BD40BC36EE3F3DD6F8BC9DB05C981DDE2)

This API must be called before the [show](../arkui-nativedialogapi-1/document.md#show) API is invoked.

**Since**: 19

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_NativeDialogHandle](../arkui-nativedialog--00020177/document.md) handle | Pointer to the custom dialog box controller. |
| void\* userData | Custom data. |
| callback | Callback function that is triggered before the custom dialog box disappears. |

**Returns**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Result code.

Returns [ARKUI\_ERROR\_CODE\_NO\_ERROR](../../header-files/native-type-h/document.md#arkui_errorcode) if the operation is successful.

Returns [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](../../header-files/native-type-h/document.md#arkui_errorcode) if a parameter error occurs.

 |

#### \[h2\]registerOnDidDisappear()

int32\_t (\*registerOnDidDisappear)(ArkUI\_NativeDialogHandle handle, void\* userData, void (\*callback)(void\* userData))

**Description**

Registers a callback function that is triggered after the custom dialog box disappears.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b4/v3/ducp1He-Sfe0w28sQxo1Mg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062305Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=65C6DD16EE41181E7AE04D0BB68E5CEDC903B1A1772C561F82421AC92840E91D)

This API must be called before the [show](../arkui-nativedialogapi-1/document.md#show) API is invoked.

**Since**: 19

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_NativeDialogHandle](../arkui-nativedialog--00020177/document.md) handle | Pointer to the custom dialog box controller. |
| void\* userData | Custom data. |
| callback | Callback function that is triggered after the custom dialog box disappears. |

**Returns**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Result code.

Returns [ARKUI\_ERROR\_CODE\_NO\_ERROR](../../header-files/native-type-h/document.md#arkui_errorcode) if the operation is successful.

Returns [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](../../header-files/native-type-h/document.md#arkui_errorcode) if a parameter error occurs.

 |

#### \[h2\]setBorderWidth()

int32\_t (\*setBorderWidth)(ArkUI\_NativeDialogHandle handle, float top, float right, float bottom, float left, ArkUI\_LengthMetricUnit unit)

**Description**

Sets the border width of the custom dialog box.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7b/v3/Xe48eWQgRwOdAA7XG_b1gg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062305Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=562F615708903FAE725A6C0B033785271F9F2E406CD92B20FE6AC7EE723EB4EB)

This API must be called before the [show](../arkui-nativedialogapi-1/document.md#show) API is invoked.

**Since**: 19

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_NativeDialogHandle](../arkui-nativedialog--00020177/document.md) handle | Pointer to the custom dialog box controller. |
| float top | Top border width. |
| float right | Right border width. |
| float bottom | Bottom border width. |
| float left | Left border width. |
| [ArkUI\_LengthMetricUnit](../../header-files/native-type-h/document.md#arkui_lengthmetricunit) unit | Unit of the width. The default value is vp. |

**Returns**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Result code.

Returns [ARKUI\_ERROR\_CODE\_NO\_ERROR](../../header-files/native-type-h/document.md#arkui_errorcode) if the operation is successful.

Returns [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](../../header-files/native-type-h/document.md#arkui_errorcode) if a parameter error occurs.

 |

#### \[h2\]setBorderColor()

int32\_t (\*setBorderColor)(ArkUI\_NativeDialogHandle handle, uint32\_t top, uint32\_t right, uint32\_t bottom, uint32\_t left)

**Description**

Sets the border color of the custom dialog box.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6b/v3/uFEJa3NJRr60G2cWmH8k1Q/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062305Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=AF9F967C98F4DD34022D46BB9191F632E3E380EF38B904E9A772787A600A6217)

This API must be called before the [show](../arkui-nativedialogapi-1/document.md#show) API is invoked.

**Since**: 19

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_NativeDialogHandle](../arkui-nativedialog--00020177/document.md) handle | Pointer to the custom dialog box controller. |
| uint32\_t top | Top border color. |
| uint32\_t right | Right border color. |
| uint32\_t bottom | Bottom border color. |
| uint32\_t left | Left border color. |

**Returns**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Result code.

Returns [ARKUI\_ERROR\_CODE\_NO\_ERROR](../../header-files/native-type-h/document.md#arkui_errorcode) if the operation is successful.

Returns [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](../../header-files/native-type-h/document.md#arkui_errorcode) if a parameter error occurs.

 |

#### \[h2\]setBorderStyle()

int32\_t (\*setBorderStyle)(ArkUI\_NativeDialogHandle handle, int32\_t top, int32\_t right, int32\_t bottom, int32\_t left)

**Description**

Sets the border style of the custom dialog box.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e/v3/vYZFCAKPQT2pZbMqggtFtQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062305Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=A817420CB25ED707A7173486C9B7E8B53125DF8693FBDBBE3E951C176ECE7C95)

This API must be called before the [show](../arkui-nativedialogapi-1/document.md#show) API is invoked.

**Since**: 19

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_NativeDialogHandle](../arkui-nativedialog--00020177/document.md) handle | Pointer to the custom dialog box controller. |
| int32\_t top | Top border style. The parameter type is [ArkUI\_BorderStyle](../../header-files/native-type-h/document.md#arkui_borderstyle). The default value is **ARKUI\_BORDER\_STYLE\_SOLID**. |
| int32\_t right | Right border style. The parameter type is [ArkUI\_BorderStyle](../../header-files/native-type-h/document.md#arkui_borderstyle). The default value is **ARKUI\_BORDER\_STYLE\_SOLID**. |
| int32\_t bottom | Bottom border style. The parameter type is [ArkUI\_BorderStyle](../../header-files/native-type-h/document.md#arkui_borderstyle). The default value is **ARKUI\_BORDER\_STYLE\_SOLID**. |
| int32\_t left | Left border style. The parameter type is [ArkUI\_BorderStyle](../../header-files/native-type-h/document.md#arkui_borderstyle). The default value is **ARKUI\_BORDER\_STYLE\_SOLID**. |

**Returns**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Result code.

Returns [ARKUI\_ERROR\_CODE\_NO\_ERROR](../../header-files/native-type-h/document.md#arkui_errorcode) if the operation is successful.

Returns [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](../../header-files/native-type-h/document.md#arkui_errorcode) if a parameter error occurs.

 |

#### \[h2\]setWidth()

int32\_t (\*setWidth)(ArkUI\_NativeDialogHandle handle, float width, ArkUI\_LengthMetricUnit unit)

**Description**

Sets the backdrop width of the custom dialog box.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d0/v3/4G9kgtWmRDi4N6AUhiw7iw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062305Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=428208D50A2C2C3D15DD9080D79921738A373398CE1F47196752AF3F7867AE91)

This API must be called before the [show](../arkui-nativedialogapi-1/document.md#show) API is invoked.

**Since**: 19

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_NativeDialogHandle](../arkui-nativedialog--00020177/document.md) handle | Pointer to the custom dialog box controller. |
| float width | Backdrop width. |
| [ArkUI\_LengthMetricUnit](../../header-files/native-type-h/document.md#arkui_lengthmetricunit) unit | Unit of the width. The default value is vp. |

**Returns**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Result code.

Returns [ARKUI\_ERROR\_CODE\_NO\_ERROR](../../header-files/native-type-h/document.md#arkui_errorcode) if the operation is successful.

Returns [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](../../header-files/native-type-h/document.md#arkui_errorcode) if a parameter error occurs.

 |

#### \[h2\]setHeight()

int32\_t (\*setHeight)(ArkUI\_NativeDialogHandle handle, float height, ArkUI\_LengthMetricUnit unit)

**Description**

Sets the backdrop height of the custom dialog box.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ec/v3/-Ppuh3zwSBmAgGYHnJN-2A/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062305Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=43FC058921BACD4E6F40A8CA759B0662F55EDA6C5A09F06FEC904670441A95E4)

This API must be called before the [show](../arkui-nativedialogapi-1/document.md#show) API is invoked.

**Since**: 19

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_NativeDialogHandle](../arkui-nativedialog--00020177/document.md) handle | Pointer to the custom dialog box controller. |
| float height | Backdrop height. |
| [ArkUI\_LengthMetricUnit](../../header-files/native-type-h/document.md#arkui_lengthmetricunit) unit | Unit of the height. The default value is vp. |

**Returns**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Result code.

Returns [ARKUI\_ERROR\_CODE\_NO\_ERROR](../../header-files/native-type-h/document.md#arkui_errorcode) if the operation is successful.

Returns [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](../../header-files/native-type-h/document.md#arkui_errorcode) if a parameter error occurs.

 |

#### \[h2\]setShadow()

int32\_t (\*setShadow)(ArkUI\_NativeDialogHandle handle, ArkUI\_ShadowStyle shadow)

**Description**

Sets the shadow of the custom dialog box's backdrop.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/df/v3/DYB9C-teQJGkiEWhj7nJBg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062305Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=E5AFC10780F89D729F04E46EBBAC1787BD5EADAA6EAA927149C147988EF39CE6)

This API must be called before the [show](../arkui-nativedialogapi-1/document.md#show) API is invoked.

**Since**: 19

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_NativeDialogHandle](../arkui-nativedialog--00020177/document.md) handle | Pointer to the custom dialog box controller. |
| [ArkUI\_ShadowStyle](../../header-files/native-type-h/document.md#arkui_shadowstyle) shadow | Backdrop shadow style, specified by an enumerated value. |

**Returns**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Result code.

Returns [ARKUI\_ERROR\_CODE\_NO\_ERROR](../../header-files/native-type-h/document.md#arkui_errorcode) if the operation is successful.

Returns [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](../../header-files/native-type-h/document.md#arkui_errorcode) if a parameter error occurs.

 |

#### \[h2\]setCustomShadow()

int32\_t (\*setCustomShadow)(ArkUI\_NativeDialogHandle handle, const ArkUI\_AttributeItem\* customShadow)

**Description**

Sets the shadow of the custom dialog box's backdrop.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5b/v3/gHLsEAU-StCY3Off_55e1w/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062305Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=4DBC84C1D37369A25F86B169DCCC7E9214A726F9BADCBCA4712BE21120CD828B)

This API must be called before the [show](../arkui-nativedialogapi-1/document.md#show) API is invoked.

**Since**: 19

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_NativeDialogHandle](../arkui-nativedialog--00020177/document.md) handle | Pointer to the custom dialog box controller. |
| const [ArkUI\_AttributeItem](../arkui-attributeitem/document.md)\* customShadow | Custom shadow parameters. The format is consistent with the **NODE\_SHADOW** property in [ArkUI\_NodeAttributeType](../../header-files/native-node-h/document.md#arkui_nodeattributetype). |

**Returns**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Result code.

Returns [ARKUI\_ERROR\_CODE\_NO\_ERROR](../../header-files/native-type-h/document.md#arkui_errorcode) if the operation is successful.

Returns [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](../../header-files/native-type-h/document.md#arkui_errorcode) if a parameter error occurs.

 |

#### \[h2\]setBackgroundBlurStyle()

int32\_t (\*setBackgroundBlurStyle)(ArkUI\_NativeDialogHandle handle, ArkUI\_BlurStyle blurStyle)

**Description**

Sets the backdrop blur style of the custom dialog box.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c1/v3/-5kzJIg3QT2eGJVoBeLfAQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062305Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=D728E2BB7B7B6F0079F76078737365F1850605ED7E65610BE20AF121799D41A4)

This API must be called before the [show](../arkui-nativedialogapi-1/document.md#show) API is invoked.

**Since**: 19

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_NativeDialogHandle](../arkui-nativedialog--00020177/document.md) handle | Pointer to the custom dialog box controller. |
| [ArkUI\_BlurStyle](../../header-files/native-type-h/document.md#arkui_blurstyle) blurStyle | Backdrop blur material, specified by an enumerated value. |

**Returns**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Result code.

Returns [ARKUI\_ERROR\_CODE\_NO\_ERROR](../../header-files/native-type-h/document.md#arkui_errorcode) if the operation is successful.

Returns [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](../../header-files/native-type-h/document.md#arkui_errorcode) if a parameter error occurs.

 |

#### \[h2\]setKeyboardAvoidMode()

int32\_t (\*setKeyboardAvoidMode)(ArkUI\_NativeDialogHandle handle, ArkUI\_KeyboardAvoidMode keyboardAvoidMode)

**Description**

Sets the keyboard avoidance mode of the custom dialog box.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/da/v3/KqHTTy5TQ9q2gLqYHjgUYw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062305Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=723EB09B6BA9F1F969FD5EC3E0437C41B2B38B2157CB48A93E520072F7C93E2B)

This API must be called before the [show](../arkui-nativedialogapi-1/document.md#show) API is invoked.

**Since**: 19

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_NativeDialogHandle](../arkui-nativedialog--00020177/document.md) handle | Pointer to the custom dialog box controller. |
| [ArkUI\_KeyboardAvoidMode](../../header-files/native-type-h/document.md#arkui_keyboardavoidmode) keyboardAvoidMode | Keyboard avoidance mode, specified by an enumerated value. |

**Returns**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Result code.

Returns [ARKUI\_ERROR\_CODE\_NO\_ERROR](../../header-files/native-type-h/document.md#arkui_errorcode) if the operation is successful.

Returns [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](../../header-files/native-type-h/document.md#arkui_errorcode) if a parameter error occurs.

 |

#### \[h2\]enableHoverMode()

int32\_t (\*enableHoverMode)(ArkUI\_NativeDialogHandle handle, bool enableHoverMode)

**Description**

Sets whether the custom dialog box responds when the device is in semi-folded mode.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e9/v3/JEmk6UrTSpKX7VancYqQnQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062305Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=778E999F9E9729B068AE95E936D35790796AAA7478C3FC08E8EED2231708F937)

This API must be called before the [show](../arkui-nativedialogapi-1/document.md#show) API is invoked.

**Since**: 19

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_NativeDialogHandle](../arkui-nativedialog--00020177/document.md) handle | Pointer to the custom dialog box controller. |
| bool enableHoverMode | Whether to respond when the device is in semi-folded mode. The default value is **false**. The value **true** means to respond when the device is in semi-folded mode, and **false** means the opposite. |

**Returns**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Result code.

Returns [ARKUI\_ERROR\_CODE\_NO\_ERROR](../../header-files/native-type-h/document.md#arkui_errorcode) if the operation is successful.

Returns [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](../../header-files/native-type-h/document.md#arkui_errorcode) if a parameter error occurs.

 |

#### \[h2\]setHoverModeArea()

int32\_t (\*setHoverModeArea)(ArkUI\_NativeDialogHandle handle, ArkUI\_HoverModeAreaType hoverModeAreaType)

**Description**

Sets the default display area of the custom dialog box in hover mode.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/16/v3/3qEoc6WOTcC-5mOn7KPRjg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062305Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=42F45EC7F068147427706C85409283E1C51F8652C35DE80051411B14F555E54A)

This API must be called before the [show](../arkui-nativedialogapi-1/document.md#show) API is invoked.

**Since**: 19

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_NativeDialogHandle](../arkui-nativedialog--00020177/document.md) handle | Pointer to the custom dialog box controller. |
| [ArkUI\_HoverModeAreaType](../../header-files/native-type-h/document.md#arkui_hovermodeareatype) hoverModeAreaType | Display area in hover mode, specified by an enumerated value. |

**Returns**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Result code.

Returns [ARKUI\_ERROR\_CODE\_NO\_ERROR](../../header-files/native-type-h/document.md#arkui_errorcode) if the operation is successful.

Returns [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](../../header-files/native-type-h/document.md#arkui_errorcode) if a parameter error occurs.

 |

#### \[h2\]setFocusable()

int32\_t (\*setFocusable)(ArkUI\_NativeDialogHandle handle, bool focusable)

**Description**

Sets whether the custom dialog box can gain focus.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d7/v3/QQuWRApGQt-5GXTEMLVuMQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062305Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=DB55D960ADB858131BBB2A77BC1074FB059E33E295D58A36D9403B1B6A90867A)

This API must be called before the [show](../arkui-nativedialogapi-1/document.md#show) API is invoked.

**Since**: 19

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_NativeDialogHandle](../arkui-nativedialog--00020177/document.md) handle | Pointer to the custom dialog box controller. |
| bool focusable | Whether the custom dialog box can gain focus. The value **true** means that the custom dialog box can gain focus, and **false** means the opposite. The preset value is **true**. |

**Returns**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Result code.

Returns [ARKUI\_ERROR\_CODE\_NO\_ERROR](../../header-files/native-type-h/document.md#arkui_errorcode) if the operation is successful.

Returns [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](../../header-files/native-type-h/document.md#arkui_errorcode) if a parameter error occurs.

 |

#### \[h2\]setBackgroundBlurStyleOptions()

int32\_t (\*setBackgroundBlurStyleOptions)(ArkUI\_NativeDialogHandle handle, const ArkUI\_AttributeItem\* backgroundBlurStyleOptions)

**Description**

Sets the background blur effect of the custom dialog box.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d3/v3/3h90YP7lQa-Q0uHqCuN6bA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062305Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=9E5B43B027C77610F8C36C786ED165DAC0CD2CE09934D8A194428C429CCDC514)

This API must be called before the [show](../arkui-nativedialogapi-1/document.md#show) API is invoked.

**Since**: 19

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_NativeDialogHandle](../arkui-nativedialog--00020177/document.md) handle | Pointer to the custom dialog box controller. |
| const [ArkUI\_AttributeItem](../arkui-attributeitem/document.md)\* backgroundBlurStyleOptions | 
Options for customizing the background blur effect. The format of the [ArkUI\_AttributeItem](../arkui-attributeitem/document.md) parameter is as follows:

.value\[0\].i32: color mode, specified by an enumerated value of [ArkUI\_ColorMode](../../header-files/native-type-h/document.md#arkui_colormode).

.value\[1\]?.i32: adaptive color mode, specified by an enumerated value of [ArkUI\_AdaptiveColor](../../header-files/native-type-h/document.md#arkui_adaptivecolor).

.value\[2\]?.f32: blur degree. The value range is \[0.0, 1.0\]. If the value is out of the valid range, the boundary value is used.

.value\[3\]?.u32: brightness of black in the grayscale blur. The value range is \[0, 127\]. If the value is out of the valid range, **0** is used.

.value\[4\]?.u32: darkening degree of white in the grayscale blur. The value range is \[0, 127\]. If the value is out of the valid range, **0** is used.

.value\[5\]?.i32: blur activation policy, specified by an enumerated value of [ArkUI\_BlurStyleActivePolicy](../../header-files/native-type-h/document.md#arkui_blurstyleactivepolicy).

.value\[6\]?.u32: background color, in 0xARGB format, of the components within the window after the window loses focus (in which case, the blur effect on the components within the window is removed).

 |

**Returns**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Result code.

Returns [ARKUI\_ERROR\_CODE\_NO\_ERROR](../../header-files/native-type-h/document.md#arkui_errorcode) if the operation is successful.

Returns [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](../../header-files/native-type-h/document.md#arkui_errorcode) if a parameter error occurs.

 |

#### \[h2\]setBackgroundEffect()

int32\_t (\*setBackgroundEffect)(ArkUI\_NativeDialogHandle handle, const ArkUI\_AttributeItem\* backgroundEffect)

**Description**

Sets the background effect parameters of the custom dialog box.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/91/v3/ZUmBqno5SoOCGWZgaKiElw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062305Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=67949C3E52211755BBB79F706A1D4424F4451F4AB733E1AB198D24DC3EC1CD3F)

This API must be called before the [show](../arkui-nativedialogapi-1/document.md#show) API is invoked.

**Since**: 19

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_NativeDialogHandle](../arkui-nativedialog--00020177/document.md) handle | Pointer to the custom dialog box controller. |
| const [ArkUI\_AttributeItem](../arkui-attributeitem/document.md)\* backgroundEffect | 
Background effect parameters. The format of the [ArkUI\_AttributeItem](../arkui-attributeitem/document.md) parameter is as follows:

.value\[0\].f32: blur radius, in vp.

.value\[1\]?.f32: saturation.

.value\[2\]?.f32: brightness.

.value\[3\]?.u32: color, in 0xARGB format.

.value\[4\]?.i32: adaptive color mode, specified by an enumerated value of [ArkUI\_AdaptiveColor](../../header-files/native-type-h/document.md#arkui_adaptivecolor).

.value\[5\]?.u32: brightness of black in the grayscale blur. The value range is \[0, 127\]. If the value is out of the valid range, **0** is used.

.value\[6\]?.u32: darkening degree of white in the grayscale blur. The value range is \[0, 127\]. If the value is out of the valid range, **0** is used.

.value\[7\]?.i32: blur activation policy, specified by an enumerated value of [ArkUI\_BlurStyleActivePolicy](../../header-files/native-type-h/document.md#arkui_blurstyleactivepolicy).

.value\[8\]?.u32: background color, in 0xARGB format, of the components within the window after the window loses focus (in which case, the blur effect on the components within the window is removed).

 |

**Returns**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Result code.

Returns [ARKUI\_ERROR\_CODE\_NO\_ERROR](../../header-files/native-type-h/document.md#arkui_errorcode) if the operation is successful.

Returns [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](../../header-files/native-type-h/document.md#arkui_errorcode) if a parameter error occurs.

 |
