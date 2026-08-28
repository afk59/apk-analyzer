# ArkUI\_NativeDialogAPI\_1

typedef struct {...} ArkUI\_NativeDialogAPI\_1

#### Overview

Provides a collection of native-side custom dialog box APIs provided by ArkUI.

**Since**: 12

**Related module**: [ArkUI\_NativeModule](../../modules/arkui-nativemodule/document.md)

**Header file**: [native\_dialog.h](../../header-files/native-dialog-h/document.md)

#### Summary

#### \[h2\]Member Functions

| Name | Description |
| :-- | :-- |
| [ArkUI\_NativeDialogHandle (\*create)()](#create) | Creates a custom dialog box and returns the pointer to the created dialog box. |
| [void (\*dispose)(ArkUI\_NativeDialogHandle handle)](#dispose) | Destroys a custom dialog box. |
| [int32\_t (\*setContent)(ArkUI\_NativeDialogHandle handle, ArkUI\_NodeHandle content)](#setcontent) | Sets the content for a custom dialog box. |
| [int32\_t (\*removeContent)(ArkUI\_NativeDialogHandle handle)](#removecontent) | Removes the content of a custom dialog box. |
| [int32\_t (\*setContentAlignment)(ArkUI\_NativeDialogHandle handle, int32\_t alignment, float offsetX, float offsetY)](#setcontentalignment) | Sets the alignment mode of a custom dialog box. |
| [int32\_t (\*resetContentAlignment)(ArkUI\_NativeDialogHandle handle)](#resetcontentalignment) | Resets the alignment mode of a custom dialog box to its default settings. |
| [int32\_t (\*setModalMode)(ArkUI\_NativeDialogHandle handle, bool isModal)](#setmodalmode) | Sets the modal mode for a custom dialog box. |
| [int32\_t (\*setAutoCancel)(ArkUI\_NativeDialogHandle handle, bool autoCancel)](#setautocancel) | Specifies whether to allow users to touch the mask to dismiss a custom dialog box. |
| [int32\_t (\*setMask)(ArkUI\_NativeDialogHandle handle, uint32\_t maskColor, const ArkUI\_Rect\* maskRect)](#setmask) | Sets the mask for a custom dialog box. |
| [int32\_t (\*setBackgroundColor)(ArkUI\_NativeDialogHandle handle, uint32\_t backgroundColor)](#setbackgroundcolor) | Sets the background color for a custom dialog box. |
| [int32\_t (\*setCornerRadius)(ArkUI\_NativeDialogHandle handle, float topLeft, float topRight,float bottomLeft, float bottomRight)](#setcornerradius) | Sets the background corner radius for a custom dialog box. |
| [int32\_t (\*setGridColumnCount)(ArkUI\_NativeDialogHandle handle, int32\_t gridCount)](#setgridcolumncount) | Sets the number of grid columns occupied by a custom dialog box. |
| [int32\_t (\*enableCustomStyle)(ArkUI\_NativeDialogHandle handle, bool enableCustomStyle)](#enablecustomstyle) | Specifies whether to use a custom style for the custom dialog box. |
| [int32\_t (\*enableCustomAnimation)(ArkUI\_NativeDialogHandle handle, bool enableCustomAnimation)](#enablecustomanimation) | Specifies whether to use a custom animation for a custom dialog box. |
| [int32\_t (\*registerOnWillDismiss)(ArkUI\_NativeDialogHandle handle, ArkUI\_OnWillDismissEvent eventHandler)](#registeronwilldismiss) | Registers a callback for a custom dialog box so that the user can decide whether to close the dialog box after they touch the back button or press the Esc key. |
| [int32\_t (\*show)(ArkUI\_NativeDialogHandle handle, bool showInSubWindow)](#show) | Shows a custom dialog box. |
| [int32\_t (\*close)(ArkUI\_NativeDialogHandle handle)](#close) | Closes a custom dialog box. If the dialog box has been closed, this API does not take effect. This API is executed asynchronously in the background. The dialog box node is removed from the tree only after the dismissal animation is complete. If you want to open the dialog box again after closing it, wait for 300 ms and then perform the operation again. |
| [int32\_t (\*registerOnWillDismissWithUserData)(ArkUI\_NativeDialogHandle handle, void\* userData, void (\*callback)(ArkUI\_DialogDismissEvent\* event))](#registeronwilldismisswithuserdata) | Registers a callback for the dismissal event of a custom dialog box. |

#### Member Function Description

#### \[h2\]create()

ArkUI\_NativeDialogHandle (\*create)()

**Description**

Creates a custom dialog box and returns the pointer to the created dialog box.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f0/v3/4Vz7GeP_Ti--OF8CQ-H2zA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062305Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=40DC6320A95C2F8CF5AA0C036674316080EE48F08AFA981E708F54B5FF265992)

This API must be called before the [show](#show) API is invoked.

**Returns**

| Type | Description |
| :-- | :-- |
| [ArkUI\_NativeDialogHandle](../arkui-nativedialog--00020177/document.md) | Pointer to the custom dialog box, or a null pointer if the creation fails. |

#### \[h2\]dispose()

void (\*dispose)(ArkUI\_NativeDialogHandle handle)

**Description**

Destroys a custom dialog box.

| Name | Description |
| :-- | :-- |
| [ArkUI\_NativeDialogHandle](../arkui-nativedialog--00020177/document.md) handle | Pointer to the custom dialog box controller. |

#### \[h2\]setContent()

int32\_t (\*setContent)(ArkUI\_NativeDialogHandle handle, ArkUI\_NodeHandle content)

**Description**

Sets the content for a custom dialog box.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3c/v3/W4UeQ59SRjipQZkr0VDtEQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062305Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=E0B3ECB41AC1D231189E4FFFC32DDB0B9287BD919F9D36A05254BC3A2ED9BAE9)

This API must be called before the [show](#show) API is invoked.

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_NativeDialogHandle](../arkui-nativedialog--00020177/document.md) handle | Pointer to the custom dialog box controller. |
| [ArkUI\_NodeHandle](../arkui-node--00020177/document.md) content | Pointer to the root node of the custom dialog box content. |

**Returns**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Result code.

Returns [ARKUI\_ERROR\_CODE\_NO\_ERROR](../../header-files/native-type-h/document.md#arkui_errorcode) if the operation is successful.

Returns [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](../../header-files/native-type-h/document.md#arkui_errorcode) if a parameter error occurs.

 |

#### \[h2\]removeContent()

int32\_t (\*removeContent)(ArkUI\_NativeDialogHandle handle)

**Description**

Removes the content of a custom dialog box.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1b/v3/-jAlryK9QgGlUcLwQd9AbQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062305Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=86ADC57236983455406C0A61C8347AFF8BB7AFB1A7C23198ED2578AEC045E9F5)

This API must be called before the [show](#show) API is invoked.

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_NativeDialogHandle](../arkui-nativedialog--00020177/document.md) handle | Pointer to the custom dialog box controller. |

**Returns**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Result code.

Returns [ARKUI\_ERROR\_CODE\_NO\_ERROR](../../header-files/native-type-h/document.md#arkui_errorcode) if the operation is successful.

Returns [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](../../header-files/native-type-h/document.md#arkui_errorcode) if a parameter error occurs.

 |

#### \[h2\]setContentAlignment()

int32\_t (\*setContentAlignment)(ArkUI\_NativeDialogHandle handle, int32\_t alignment, float offsetX, float offsetY)

**Description**

Sets the alignment mode of a custom dialog box.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/67/v3/7ltfvARVRx2FSwu0lIzR4w/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062305Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=13575488CAF496D2032AF66A61A076C53C8BD28A33FE354120663D5C95F5F0B3)

This API must be called before the [show](#show) API is invoked.

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_NativeDialogHandle](../arkui-nativedialog--00020177/document.md) handle | Pointer to the custom dialog box controller. |
| int32\_t alignment | Alignment mode. The parameter type is [ArkUI\_Alignment](../../header-files/native-type-h/document.md#arkui_alignment). |
| float offsetX | Horizontal offset of the dialog box. The value is a floating point number, in vp. |
| float offsetY | Vertical offset of the dialog box. The value is a floating point number, in vp. |

**Returns**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Result code.

Returns [ARKUI\_ERROR\_CODE\_NO\_ERROR](../../header-files/native-type-h/document.md#arkui_errorcode) if the operation is successful.

Returns [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](../../header-files/native-type-h/document.md#arkui_errorcode) if a parameter error occurs.

 |

#### \[h2\]resetContentAlignment()

int32\_t (\*resetContentAlignment)(ArkUI\_NativeDialogHandle handle)

**Description**

Resets the alignment mode of a custom dialog box to its default settings. The default value is **ARKUI\_ALIGNMENT\_TOP\_START**. For details, see [ArkUI\_Alignment](../../header-files/native-type-h/document.md#arkui_alignment).

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fe/v3/1AwByg-gTYuR_ZvaoE950Q/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062305Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=E47686E2BBD5327A460C6AC1A9662D046C9971E663E9ADDC9BE4802A9C807457)

This API must be called before the [show](#show) API is invoked.

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_NativeDialogHandle](../arkui-nativedialog--00020177/document.md) handle | Pointer to the custom dialog box controller. |

**Returns**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Result code.

Returns [ARKUI\_ERROR\_CODE\_NO\_ERROR](../../header-files/native-type-h/document.md#arkui_errorcode) if the operation is successful.

Returns [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](../../header-files/native-type-h/document.md#arkui_errorcode) if a parameter error occurs.

 |

#### \[h2\]setModalMode()

int32\_t (\*setModalMode)(ArkUI\_NativeDialogHandle handle, bool isModal)

**Description**

Sets the modal mode for a custom dialog box.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cc/v3/4ZzRtlBiS4ORP9yAFAkROg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062305Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=A0DBE93FFFC3E9817058C5073410F6BE4578C256454CDE6797C7FCADF2CD278E)

This API must be called before the [show](#show) API is invoked.

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_NativeDialogHandle](../arkui-nativedialog--00020177/document.md) handle | Pointer to the custom dialog box controller. |
| bool isModal | Whether the custom dialog box is a modal, which has a mask applied. The value **true** means that the custom dialog box is a modal, and **false** means the opposite. |

**Returns**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Result code.

Returns [ARKUI\_ERROR\_CODE\_NO\_ERROR](../../header-files/native-type-h/document.md#arkui_errorcode) if the operation is successful.

Returns [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](../../header-files/native-type-h/document.md#arkui_errorcode) if a parameter error occurs.

 |

#### \[h2\]setAutoCancel()

int32\_t (\*setAutoCancel)(ArkUI\_NativeDialogHandle handle, bool autoCancel)

**Description**

Specifies whether to allow users to touch the mask to dismiss a custom dialog box.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ca/v3/pVAHFclAR2e3qCz_nvldKQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062305Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=D29E6DF45819D18EB7851AB593B5547FFF93DD6E72559E0CDF6C6377B6B16A95)

This API must be called before the [show](#show) API is invoked.

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_NativeDialogHandle](../arkui-nativedialog--00020177/document.md) handle | Pointer to the custom dialog box controller. |
| bool autoCancel | Whether to allow users to touch the mask to dismiss the dialog box. The value **true** means to allow users to do so, and **false** means the opposite. |

**Returns**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Result code.

Returns [ARKUI\_ERROR\_CODE\_NO\_ERROR](../../header-files/native-type-h/document.md#arkui_errorcode) if the operation is successful.

Returns [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](../../header-files/native-type-h/document.md#arkui_errorcode) if a parameter error occurs.

 |

#### \[h2\]setMask()

int32\_t (\*setMask)(ArkUI\_NativeDialogHandle handle, uint32\_t maskColor, const ArkUI\_Rect\* maskRect)

**Description**

Sets the mask for a custom dialog box.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3e/v3/tLYNkY8VQu2-MhNBnb_zYA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062305Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=DCD60C5780C39CB36CB43EA4AB0751DB6E5A8D2CC079F649BEEC72132B8A4433)

This API must be called before the [show](#show) API is invoked.

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_NativeDialogHandle](../arkui-nativedialog--00020177/document.md) handle | Pointer to the custom dialog box controller. |
| uint32\_t maskColor | Mask color, in 0xARGB format. |
| const [ArkUI\_Rect](../arkui-rect/document.md)\* maskRect | Pointer to the mask area. Events outside the mask area are transparently transmitted, and events within the mask area are not. The parameter type is [ArkUI\_Rect](../arkui-rect/document.md). |

**Returns**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Result code.

Returns [ARKUI\_ERROR\_CODE\_NO\_ERROR](../../header-files/native-type-h/document.md#arkui_errorcode) if the operation is successful.

Returns [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](../../header-files/native-type-h/document.md#arkui_errorcode) if a parameter error occurs.

 |

#### \[h2\]setBackgroundColor()

int32\_t (\*setBackgroundColor)(ArkUI\_NativeDialogHandle handle, uint32\_t backgroundColor)

**Description**

Sets the background color for a custom dialog box.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fb/v3/3BmwAU7MRQugRVBuN45OQA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062305Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=41468F72CB3DDC608D132B7B52CA900FA3082757A937EE2F51A977BA8BDE03A2)

This API must be called before the [show](#show) API is invoked.

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_NativeDialogHandle](../arkui-nativedialog--00020177/document.md) handle | Pointer to the custom dialog box controller. |
| uint32\_t backgroundColor | Background color of the custom dialog box, in 0xARGB format. |

**Returns**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Result code.

Returns [ARKUI\_ERROR\_CODE\_NO\_ERROR](../../header-files/native-type-h/document.md#arkui_errorcode) if the operation is successful.

Returns [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](../../header-files/native-type-h/document.md#arkui_errorcode) if a parameter error occurs.

 |

#### \[h2\]setCornerRadius()

int32\_t (\*setCornerRadius)(ArkUI\_NativeDialogHandle handle, float topLeft, float topRight,float bottomLeft, float bottomRight)

**Description**

Sets the background corner radius for a custom dialog box.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a7/v3/1MvHwxLMQ-qg4oJzhxGEKw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062305Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=63974865B365040358ACA39DFF9948CEDF659928204EEAB9562E722A899D5F06)

This API must be called before the [show](#show) API is invoked.

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_NativeDialogHandle](../arkui-nativedialog--00020177/document.md) handle | Pointer to the custom dialog box controller. |
| float topLeft | Radius of the upper left corner of the background for the custom dialog box, in vp. Default value: 32 vp since API version 12; 24 vp in API version 11 and earlier versions. |
| float topRight | Radius of the upper right corner of the background for the custom dialog box, in vp. Default value: 32 vp since API version 12; 24 vp in API version 11 and earlier versions. |
| float bottomLeft | Radius of the lower left corner of the background for the custom dialog box, in vp. Default value: 32 vp since API version 12; 24 vp in API version 11 and earlier versions. |
| float bottomRight | Radius of the lower right corner of the background for the custom dialog box, in vp. Default value: 32 vp since API version 12; 24 vp in API version 11 and earlier versions. |

**Returns**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Result code.

Returns [ARKUI\_ERROR\_CODE\_NO\_ERROR](../../header-files/native-type-h/document.md#arkui_errorcode) if the operation is successful.

Returns [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](../../header-files/native-type-h/document.md#arkui_errorcode) if a parameter error occurs.

 |

#### \[h2\]setGridColumnCount()

int32\_t (\*setGridColumnCount)(ArkUI\_NativeDialogHandle handle, int32\_t gridCount)

**Description**

Sets the number of grid columns occupied by a custom dialog box.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/61/v3/dcQolLr4Qwmz3LM1rHe-3g/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062305Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=E1852F9917ADC2F985557D5458C92A59945ADAE050A67CF450E38DFB4E036F15)

This API must be called before the [show](#show) API is invoked.

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_NativeDialogHandle](../arkui-nativedialog--00020177/document.md) handle | Pointer to the custom dialog box controller. |
| int32\_t gridCount | 
Number of grids. The default value is subject to the window size, and the maximum value is the [maximum number of columns supported by the system](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/arkts-layout-development-grid-layout#columns).

The value is an integer greater than or equal to 0.

 |

**Returns**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Result code.

Returns [ARKUI\_ERROR\_CODE\_NO\_ERROR](../../header-files/native-type-h/document.md#arkui_errorcode) if the operation is successful.

Returns [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](../../header-files/native-type-h/document.md#arkui_errorcode) if a parameter error occurs.

 |

#### \[h2\]enableCustomStyle()

int32\_t (\*enableCustomStyle)(ArkUI\_NativeDialogHandle handle, bool enableCustomStyle)

**Description**

Specifies whether to use a custom style for the custom dialog box.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/38/v3/HRb3lrfhSLWz_bliWbA91g/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062305Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=8B7EFB75BCBBAC939FF94DC02D23D1EB80E0B789F6423A6BF9BB756C5177BF56)

This API must be called before the [show](#show) API is invoked.

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_NativeDialogHandle](../arkui-nativedialog--00020177/document.md) handle | Pointer to the custom dialog box controller. |
| bool enableCustomStyle | 
Whether to use a custom style for the dialog box.

Default value: **false**.

**true**: The dialog box cannot use a custom style. Its width adapts to its child components, with zero corner radius and a transparent background.

**false**: The dialog box can use a custom style. Its height adapts to its child components and its width is defined by the grid system. The rounded corner radius is 24 vp. On PC and 2-in-1 devices, it automatically avoids screen edges and window title bars.

 |

**Returns**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Result code.

Returns [ARKUI\_ERROR\_CODE\_NO\_ERROR](../../header-files/native-type-h/document.md#arkui_errorcode) if the operation is successful.

Returns [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](../../header-files/native-type-h/document.md#arkui_errorcode) if a parameter error occurs.

 |

#### \[h2\]enableCustomAnimation()

int32\_t (\*enableCustomAnimation)(ArkUI\_NativeDialogHandle handle, bool enableCustomAnimation)

**Description**

Specifies whether to use a custom animation for a custom dialog box.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/27/v3/xBu-_k4lQY6ib96QhL0EvQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062305Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=39C2CD67552918245B74AECA36761820A98115ADAB37017A91C9FA318627CF48)

This API must be called before the [show](#show) API is invoked.

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_NativeDialogHandle](../arkui-nativedialog--00020177/document.md) handle | Pointer to the custom dialog box controller. |
| bool enableCustomAnimation | Whether to use a custom animation. The value **true** means to use a custom animation, and **false** means to use the default animation. |

**Returns**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Result code.

Returns [ARKUI\_ERROR\_CODE\_NO\_ERROR](../../header-files/native-type-h/document.md#arkui_errorcode) if the operation is successful.

Returns [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](../../header-files/native-type-h/document.md#arkui_errorcode) if a parameter error occurs.

 |

#### \[h2\]registerOnWillDismiss()

int32\_t (\*registerOnWillDismiss)(ArkUI\_NativeDialogHandle handle, ArkUI\_OnWillDismissEvent eventHandler)

**Description**

Registers a callback for a custom dialog box so that the user can decide whether to close the dialog box after they touch the back button or press the Esc key.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5c/v3/GqUAnL24ScC7qVVDCXUw9Q/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062305Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=31A0EFDAE76237A3307BCCE7D9CA296AA113FFC830D96319BB039ABD05872696)

This API must be called before the [show](#show) API is invoked.

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_NativeDialogHandle](../arkui-nativedialog--00020177/document.md) handle | Pointer to the custom dialog box controller. |
| [ArkUI\_OnWillDismissEvent](../../header-files/native-dialog-h/document.md#arkui_onwilldismissevent) eventHandler | Callback for dialog box dismissal. |

**Returns**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Result code.

Returns [ARKUI\_ERROR\_CODE\_NO\_ERROR](../../header-files/native-type-h/document.md#arkui_errorcode) if the operation is successful.

Returns [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](../../header-files/native-type-h/document.md#arkui_errorcode) if a parameter error occurs.

 |

#### \[h2\]show()

int32\_t (\*show)(ArkUI\_NativeDialogHandle handle, bool showInSubWindow)

**Description**

Shows a custom dialog box.

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_NativeDialogHandle](../arkui-nativedialog--00020177/document.md) handle | Pointer to the custom dialog box controller. |
| bool showInSubWindow | Whether to show the dialog box in a subwindow. **true**: The dialog box is shown in a subwindow. **false**: The dialog box is not shown in a subwindow. |

**Returns**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Result code.

Returns [ARKUI\_ERROR\_CODE\_NO\_ERROR](../../header-files/native-type-h/document.md#arkui_errorcode) if the operation is successful.

Returns [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](../../header-files/native-type-h/document.md#arkui_errorcode) if a parameter error occurs.

 |

#### \[h2\]close()

int32\_t (\*close)(ArkUI\_NativeDialogHandle handle)

**Description**

Closes a custom dialog box. If the dialog box has been closed, this API does not take effect. This API is executed asynchronously in the background. The dialog box node is removed from the tree only after the dismissal animation is complete. If you want to open the dialog box again after closing it, wait for 300 ms and then perform the operation again.

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_NativeDialogHandle](../arkui-nativedialog--00020177/document.md) handle | Pointer to the custom dialog box controller. |

**Returns**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Result code.

Returns [ARKUI\_ERROR\_CODE\_NO\_ERROR](../../header-files/native-type-h/document.md#arkui_errorcode) if the operation is successful. This only indicates that the close command is successfully delivered, but does not indicate that the dialog box is completely closed.

Returns [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](../../header-files/native-type-h/document.md#arkui_errorcode) if a parameter error occurs.

 |

#### \[h2\]registerOnWillDismissWithUserData()

int32\_t (\*registerOnWillDismissWithUserData)(ArkUI\_NativeDialogHandle handle, void\* userData, void (\*callback)(ArkUI\_DialogDismissEvent\* event))

**Description**

Registers a callback for the dismissal event of a custom dialog box.

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkUI\_NativeDialogHandle](../arkui-nativedialog--00020177/document.md) handle | Pointer to the custom dialog box controller. |
| void\* userData | Pointer to user data. |
| callback | 
Callback for the dismissal event of the custom dialog box.

\- **event**: input parameter of the callback, which captures the reason for dismissal.

 |

**Returns**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Result code.

Returns [ARKUI\_ERROR\_CODE\_NO\_ERROR](../../header-files/native-type-h/document.md#arkui_errorcode) if the operation is successful.

Returns [ARKUI\_ERROR\_CODE\_PARAM\_INVALID](../../header-files/native-type-h/document.md#arkui_errorcode) if a parameter error occurs.

 |
