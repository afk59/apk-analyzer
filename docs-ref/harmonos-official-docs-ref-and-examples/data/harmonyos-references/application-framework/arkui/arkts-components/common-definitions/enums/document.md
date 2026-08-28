# Enums

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d7/v3/Ctp2SfWUSsigys8sgp-daA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062252Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=F602D7133803E2844E3DFF94A69806C81CCCF9297A531B66E82D3666329F6588)

The initial APIs of this module are supported since API version 7. Newly added APIs will be marked with a superscript to indicate their earliest API version.

#### AccessibilityHoverType12+

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Value | Description |
| :-- | :-- | :-- |
| HOVER\_ENTER | 0 | A finger is pressed. |
| HOVER\_MOVE | 1 | The touch moves. |
| HOVER\_EXIT | 2 | A finger is lifted. |
| HOVER\_CANCEL | 3 | The current event is canceled. |

#### Alignment

Defines the alignment mode for child elements in the container drawing area.

**Widget capability**: This API can be used in ArkTS widgets since API version 9.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Value | Description |
| :-- | :-- | :-- |
| TopStart | 0 | Top start. |
| Top | 1 | Horizontally centered on the top. |
| TopEnd | 2 | Top end. |
| Start | 3 | Vertically centered start. |
| Center | 4 | Horizontally and vertically centered. |
| End | 5 | Vertically centered end. |
| BottomStart | 6 | Bottom start. |
| Bottom | 7 | Horizontally centered on the bottom. |
| BottomEnd | 8 | Bottom end. |

#### AnimationPropertyType20+

Enumerates animatable property types for component animations.

**Atomic service API**: This API can be used in atomic services since API version 20.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Value | Description |
| :-- | :-- | :-- |
| ROTATION | 0 | Rotation angles for the x, y, and z axes. Parameters: 3. Unit: degrees (°). |
| TRANSLATION | 1 | Translation offsets for the x and y axes. Parameters: 2. Unit: px. |
| SCALE | 2 | Scale factors for the x and y axes. Parameters: 2. Value range: (-∞, +∞). |
| OPACITY | 3 | Opacity value. Parameters: 1. Value range: \[0, 1\]. |

#### AnimationStatus

Sets the animation playback status.

**Widget capability**: This API can be used in ArkTS widgets since API version 10.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Value | Description |
| :-- | :-- | :-- |
| Initial | 0 | The animation is in the initial state. |
| Running | 1 | The animation is being played. |
| Paused | 2 | The animation is paused. |
| Stopped | 3 | The animation is stopped. |

#### AppRotation12+

Defines the rotation angle of the application's orientation.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Value | Description |
| :-- | :-- | :-- |
| ROTATION\_0 | 0 | 0 degrees. |
| ROTATION\_90 | 1 | 90 degrees. |
| ROTATION\_180 | 2 | 180 degrees. |
| ROTATION\_270 | 3 | 270 degrees. |

#### ArrowPointPosition11+

Sets the position of the bubble arrow.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Value | Description |
| :-- | :-- | :-- |
| START | 'Start' | On the leftmost side of the parent component in the horizontal layout; on the top of the parent component in the vertical layout. |
| CENTER | 'Center' | In the center of the parent component. |
| END | 'End' | On the rightmost side of the parent component in the horizontal layout; at the bottom of the parent component in the vertical layout. |

#### Axis

Defines the axis direction.

**Widget capability**: This API can be used in ArkTS widgets since API version 9.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Value | Description |
| :-- | :-- | :-- |
| Vertical | 0 | Vertical direction. |
| Horizontal | 1 | Horizontal direction. |

#### AxisAction17+

Enumerates the types of axis actions for axis events.

**Atomic service API**: This API can be used in atomic services since API version 17.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Value | Description |
| :-- | :-- | :-- |
| NONE | 0 | No axis event. |
| BEGIN | 1 | The axis event begins. |
| UPDATE | 2 | The axis event is in progress. |
| END | 3 | The axis event ends. |
| CANCEL | 4 | The axis event is canceled. |

#### AxisModel15+

Enumerates the axis types for focus axis events.

**Atomic service API**: This API can be used in atomic services since API version 15.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Value | Description |
| :-- | :-- | :-- |
| ABS\_X | 0 | Game controller x-axis. |
| ABS\_Y | 1 | Game controller y-axis. |
| ABS\_Z | 2 | Game controller z-axis. |
| ABS\_RZ | 3 | Game controller rz-axis. |
| ABS\_GAS | 4 | Game controller GAS-axis. |
| ABS\_BRAKE | 5 | Game controller BRAKE-axis. |
| ABS\_HAT0X | 6 | Game controller HAT0X-axis. |
| ABS\_HAT0Y | 7 | Game controller HAT0Y-axis. |

#### AxisType22+

Enumerates the axis types for axis events.

**Atomic service API**: This API can be used in atomic services since API version 22.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Value | Description |
| :-- | :-- | :-- |
| VERTICAL\_AXIS | 0 | Vertical scroll axis. |
| HORIZONTAL\_AXIS | 1 | Horizontal scroll axis. |
| PINCH\_AXIS | 2 | Pinch axis. |

#### BarState

Sets the scroll bar status.

**Widget capability**: This API can be used in ArkTS widgets since API version 9.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Value | Description |
| :-- | :-- | :-- |
| Off | 0 | Not displayed. |
| Auto | 1 | Displayed when the screen is touched and hidden after 2s. |
| On | 2 | Always displayed. |

#### BorderStyle

Sets the border style of an element.

**Widget capability**: This API can be used in ArkTS widgets since API version 9.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Value | Description |
| :-- | :-- | :-- |
| Dotted | 0 | Dotted border. The radius of a dot is half of **borderWidth**. |
| Dashed | 1 | Dashed border. |
| Solid | 2 | Solid border. |

#### ClickEffectLevel10+

Sets the click effect level and animation parameters.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Description | Animation Settings | Default Zoom Ratio |
| :-- | :-- | :-- | :-- |
| LIGHT | Small area (light) | Spring effect, with stiffness of 410, damping of 38, and initial velocity of 1. | 90% |
| MIDDLE | Medium area (stable) | Spring effect, with stiffness of 350, damping of 35, and initial velocity of 0.5. | 95% |
| HEAVY | Large area (heavy) | Spring effect, with stiffness of 240, damping of 28, and initial velocity of 0. | 95% |

#### Color

Sets the color type.

**Widget capability**: This API can be used in ArkTS widgets since API version 9.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Value | Description |
| :-- | :-- | :-- |
| Black | 0x000000 | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/12/v3/GZtYbswnSSiBLeNVnol15g/en-us_image_0000002537925946.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062252Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=5D852F1FA5EA8507A34607BC96ADCDA7B3C32159A5220869D4A8C75E6FD0A652) |
| Blue | 0x0000ff | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/81/v3/ATk6h0IXSQOijf5rsEGeFQ/en-us_image_0000002568685723.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062252Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=C034E420D80CF766A8EA94D5DA023738F52BDF4C4403E176577EB94D13C82347) |
| Brown | 0xa52a2a | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f/v3/2yrOYdglQ4qqUMVGyQeoDQ/en-us_image_0000002568765733.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062252Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=1419CE160556FBA86C6E149B17BF764F00D24FCB621226B530219BBAC975B8D2) |
| Gray | 0x808080 | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/44/v3/6TZ1T2NcT76hi5ZqwI274A/en-us_image_0000002537766008.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062252Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=6560AD3AC5E46846183E0C27C8126BFD97F82403682E9D62FD3B7A602F329C43) |
| Grey | 0x808080 | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d6/v3/nOePPj-nRVqSCLMbCFELvw/en-us_image_0000002537766008.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062252Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=EDD454888459D10CE3C9FA0B14A9801BFBFEB7C546122CB5C7DEBEBE495CA66B) |
| Green | 0x008000 | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d4/v3/AMDXDcUYRWe4TQOZacD_9Q/en-us_image_0000002537925948.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062252Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=2D2911EF4ACEC667BC8CD728CDCA988AB0880E2AEFB42682BF3960F5A209D020) |
| Orange | 0xffa500 | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/09/v3/3QCfWAlaRPyVrRHHwlAkhw/en-us_image_0000002568685725.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062252Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=F73FD3D8AD90FD65142FDC073D237EE995211B2847AEC16E47EC74E6FD51C778) |
| Pink | 0xffc0cb | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f8/v3/bdWzdv1QTWO9SMbF9xQ2aw/en-us_image_0000002568765735.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062252Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=957F8438C940A68E73EF4463B18AF5476E62E90119A6D3520252B08A204A170E) |
| Red | 0xff0000 | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b1/v3/ey6heN6dSHCdT6uzwlY8nQ/en-us_image_0000002537766010.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062252Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=298667B263A8EBAB08A2097535B9CB4DB7491647923FE02B98BB5983FD6554BB) |
| White | 0xffffff | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/19/v3/L2UkQDJZQgW1fYoypkh3zA/en-us_image_0000002537925950.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062252Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=C30E3708295942D40D7413A58D296E59A6C79D9D39BC3443D8FCD9F154CA1973) |
| Yellow | 0xffff00 | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d6/v3/rarZbf83Rvum7g72wz7QKg/en-us_image_0000002568685727.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062252Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=F9B68EE1492A26E3F5FC8CEB810F1798BD4111419FFB3FC16D3D12C8FB93AF37) |
| Transparent9+ | rgba(0,0,0,0) | Transparent |

#### ColorSpace20+

Enumerates color space types for specifying color rendering modes.

**Atomic service API**: This API can be used in atomic services since API version 20.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Value | Description |
| :-- | :-- | :-- |
| SRGB | 0 | Standard RGB color space, suitable for most display devices. |
| DISPLAY\_P3 | 1 | Display P3 color space with wider gamut, designed for high-end display devices. |

#### ColoringStrategy10+

Enumerates the coloring strategies.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Value | Description |
| :-- | :-- | :-- |
| INVERT | invert | 
The foreground colors are the inverse of the component background colors. This strategy is only applicable when set within the [foregroundColor](../../universal-attributes/visual-effects/foreground-color/document.md#foregroundcolor) attribute.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| AVERAGE11+ | average | 

The shadow colors of the component are the average color obtained from the component background shadow area. This strategy is only applicable when set within the [shadow](../../universal-attributes/visual-effects/image-effect/document.md#shadow) attribute whose input parameter type is ShadowOptions.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| PRIMARY11+ | primary | 

The shadow colors of the component are the primary color obtained from the component background shadow area. This strategy is only applicable when set within the [shadow](../../universal-attributes/visual-effects/image-effect/document.md#shadow) attribute whose input parameter type is ShadowOptions.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |

#### CopyOptions9+

Sets the copy options.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Value | Description |
| :-- | :-- | :-- |
| None | 0 | 
Copy disabled.

**Widget capability**: This API can be used in ArkTS widgets since API version 9.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| InApp | 1 | 

Copy and paste within the current application only.

**Widget capability**: This API can be used in ArkTS widgets since API version 9.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| LocalDevice | 2 | 

Copy and paste across all applications on the device.

**Widget capability**: This API can be used in ArkTS widgets since API version 9.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| CROSS\_DEVICE(deprecated) | 3 | 

Cross-device copy.

**Widget capability**: This API can be used in ArkTS widgets since API version 11.

Note: This API is supported since API version 11 and deprecated since API version 12.

 |

#### CheckBoxShape11+

Sets the shape of check boxes.

**Widget capability**: This API can be used in ArkTS widgets since API version 11.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Value | Description |
| :-- | :-- | :-- |
| CIRCLE | 0 | Circle. |
| ROUNDED\_SQUARE | 1 | Rounded square. |

#### CrownAction18+

Enumerates the crown actions.

**Atomic service API**: This API can be used in atomic services since API version 18.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Value | Description |
| :-- | :-- | :-- |
| BEGIN | 0 | The crown starts to rotate. |
| UPDATE | 1 | The crown is rotating. |
| END | 2 | The crown stops rotating. |

#### CrownSensitivity18+

Enumerates the sensitivity levels for crown rotation.

**Atomic service API**: This API can be used in atomic services since API version 18.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Value | Description |
| :-- | :-- | :-- |
| LOW | 0 | Low sensitivity. |
| MEDIUM | 1 | Medium sensitivity. |
| HIGH | 2 | High sensitivity. |

#### Curve

Enumerates the interpolation curves. For details about the animation, see [Bezier Curve](https://developer.huawei.com/consumer/en/doc/design-guides/animation-attributes-0000001797117229#section18901156102713).

**Widget capability**: This API can be used in ArkTS widgets since API version 9.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Value | Description |
| :-- | :-- | :-- |
| Linear | 0 | The animation maintains a constant speed throughout the process. |
| Ease | 1 | The animation starts slowly, accelerates, and then decelerates before ending. The curve is CubicBezier(0.25, 0.1, 0.25, 1.0). |
| EaseIn | 2 | The animation starts at a low speed and then picks up speed until the end. The cubic-bezier curve (0.42, 0.0, 1.0, 1.0) is used. |
| EaseOut | 3 | The animation ends at a low speed. The cubic-bezier curve (0.0, 0.0, 0.58, 1.0) is used. |
| EaseInOut | 4 | The animation starts and ends at a low speed. The cubic-bezier curve (0.42, 0.0, 0.58, 1.0) is used. |
| FastOutSlowIn | 5 | The animation uses the standard cubic-bezier curve (0.4, 0.0, 0.2, 1.0). |
| LinearOutSlowIn | 6 | The animation uses the deceleration cubic-bezier curve (0.0, 0.0, 0.2, 1.0). |
| FastOutLinearIn | 7 | The animation uses the acceleration cubic-bezier curve (0.4, 0.0, 1.0, 1.0). |
| ExtremeDeceleration | 8 | The animation uses the extreme deceleration cubic-bezier curve (0.0, 0.0, 0.0, 1.0). |
| Sharp | 9 | The animation uses the sharp cubic-bezier curve (0.33, 0.0, 0.67, 1.0). |
| Rhythm | 10 | The animation uses the rhythm cubic-bezier curve (0.7, 0.0, 0.2, 1.0). |
| Smooth | 11 | The animation uses the smooth cubic-bezier curve (0.4, 0.0, 0.4, 1.0). |
| Friction | 12 | The animation uses the friction cubic-bezier curve (0.2, 0.0, 0.2, 1.0). |

#### DialogButtonStyle10+

Sets the button style for dialog boxes.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Value | Description |
| :-- | :-- | :-- |
| DEFAULT | 0 | Blue text on white background (black background under the dark theme). |
| HIGHLIGHT | 1 | White text on blue background. |

#### Direction

Defines the horizontal layout direction of elements.

**Widget capability**: This API can be used in ArkTS widgets since API version 9.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Value | Description |
| :-- | :-- | :-- |
| Ltr | 0 | Components are arranged from left to right. |
| Rtl | 1 | Components are arranged from right to left. |
| Auto | 2 | The default layout direction is used. |

#### DividerMode19+

Enumerates divider modes.

**Atomic service API**: This API can be used in atomic services since API version 19.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Value | Description |
| :-- | :-- | :-- |
| FLOATING\_ABOVE\_MENU | 0 | The divider floats above the menu without affecting the layout height. This is the default mode. |
| EMBEDDED\_IN\_MENU | 1 | The divider is embedded in the menu and affects the layout height. |

#### Edge

Controls the alignment position of the scrollable component in the layout.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Value | Description |
| :-- | :-- | :-- |
| Top | 0 | 
Top edge in the vertical direction.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| Center(deprecated) | 1 | 

Center position in the vertical direction.

This API is deprecated since API version 9.

 |
| Bottom | 2 | 

Bottom edge in the vertical direction.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| Baseline(deprecated) | 3 | 

Text baseline position in the cross axis direction.

This API is deprecated since API version 9.

 |
| Start | 4 | 

Start position in the horizontal direction.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| Middle(deprecated) | 5 | 

Center position in the horizontal direction.

This API is deprecated since API version 9.

 |
| End | 6 | 

End position in the horizontal direction.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |

#### EdgeEffect

Defines the sliding effect of the scrollable container.

**Widget capability**: This API can be used in ArkTS widgets since API version 9.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Value | Description |
| :-- | :-- | :-- |
| Spring | 0 | Spring effect. When at one of the edges, the component can move beyond the bounds through touches, and produces a bounce effect when the user releases their finger. |
| Fade | 1 | Fade effect. When at one of the edges, the component produces a fade effect. |
| None | 2 | No effect when the component is at one of the edges. |

#### EllipsisMode11+

Sets the position of ellipsis.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Value | Description |
| :-- | :-- | :-- |
| START | 0 | An ellipsis is used at the start of the line of text. |
| CENTER | 1 | An ellipsis is used at the center of the line of text. |
| END | 2 | An ellipsis is used at the end of the line of text. |

#### EmbeddedType12+

Enumerates the types of the providers that can be started by the **EmbeddedComponent**.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Value | Description |
| :-- | :-- | :-- |
| EMBEDDED\_UI\_EXTENSION | 0 | EmbeddedUIExtensionAbility. |

#### EventQueryType19+

Enumerates interaction event types that can be queried.

**Atomic service API**: This API can be used in atomic services since API version 19.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Value | Description |
| :-- | :-- | :-- |
| ON\_CLICK | 0 | Click event. |

#### FunctionKey10+

Enumerates the input method function keys.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Value | Description |
| :-- | :-- | :-- |
| ESC | 0 | 
Esc key on the keyboard.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| F1 | 1 | 

F1 key on the keyboard.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| F2 | 2 | 

F2 key on the keyboard.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| F3 | 3 | 

F3 key on the keyboard.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| F4 | 4 | 

F4 key on the keyboard.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| F5 | 5 | 

F5 key on the keyboard.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| F6 | 6 | 

F6 key on the keyboard.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| F7 | 7 | 

F7 key on the keyboard.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| F8 | 8 | 

F8 key on the keyboard.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| F9 | 9 | 

F9 key on the keyboard.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| F10 | 10 | 

F10 key on the keyboard.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| F11 | 11 | 

F11 key on the keyboard.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| F12 | 12 | 

F12 key on the keyboard.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| TAB12+ | 13 | 

Tab key on the keyboard.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| DPAD\_UP12+ | 14 | 

Up arrow key on the keyboard.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| DPAD\_DOWN12+ | 15 | 

Down arrow key on the keyboard.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| DPAD\_LEFT12+ | 16 | 

Left arrow key on the keyboard.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| DPAD\_RIGHT12+ | 17 | 

Right arrow key on the keyboard.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |

#### FillMode

Sets the status before and after execution of the animation in the current playback direction. The status after execution of the animation is jointly determined by the **fillMode** and **reverse** attributes. For example, if **fillMode** is set to **Forwards**, the target will retain the state defined by the last keyframe encountered during execution. In this case, if **reverse** is set to **false**, the target will retain the state defined by the last keyframe encountered in the forward direction, that is, the last image; if **reverse** is set to **true**, the target will retain the state defined by the last keyframe encountered in the backward direction, that is, the first image.

**Widget capability**: This API can be used in ArkTS widgets since API version 10.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Value | Description |
| :-- | :-- | :-- |
| None | 0 | If the animation is not executed, no style is applied to the target. After the animation is played, the initial default state is restored. |
| Forwards | 1 | The target component retains the state set by the last keyframe encountered during execution of the animation. |
| Backwards | 2 | The animation applies the values defined in the first relevant keyframe once it is applied to the target component, and retains the values during the period set by **delay**. The first relevant keyframe depends on the value of **playMode**. If **playMode** is **Normal** or **Alternate**, the first relevant keyframe is in the **from** state. If **playMode** is **Reverse** or **AlternateReverse**, the first relevant keyframe is in the **to** state. |
| Both | 3 | The animation follows the rules for both **Forwards** and **Backwards**, extending the animation attributes in both directions. |

#### FlexAlign

Sets the alignment mode of an element on the main axis of the container.

**Widget capability**: This API can be used in ArkTS widgets since API version 9.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Description |
| :-- | :-- |
| Start | The child components are aligned with the start edge of the main axis. The first component is aligned with the main-start, and subsequent components are aligned with the previous one. |
| Center | The child components are aligned in the center of the main axis. The space between the first component and the main-start is the same as that between the last component and the main-end. |
| End | The child components are aligned with the end edge of the main axis. The last component is aligned with the main-end, and other components are aligned with the next one. |
| SpaceBetween | The child components are evenly distributed along the main axis. The space between any two adjacent components is the same. The first component is aligned with the main-start, the last component is aligned with the main-end, and the remaining components are distributed so that the space between any two adjacent components is the same. |
| SpaceAround | The child components are evenly distributed along the main axis. The space between any two adjacent components is the same. The space between the first component and main-start, and that between the last component and cross-main are both half the size of the space between two adjacent components. |
| SpaceEvenly | The child components are evenly distributed along the main axis. The space between the first component and main-start, the space between the last component and main-end, and the space between any two adjacent components are the same. |

#### FlexDirection

Sets the direction in which child components are arranged in the **Flex** component, that is, the direction of the main axis.

**Widget capability**: This API can be used in ArkTS widgets since API version 9.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Description |
| :-- | :-- |
| Row | The child components are arranged in the same direction as the main axis runs along the rows. |
| RowReverse | The child components are arranged opposite to the **Row** direction. |
| Column | The child components are arranged in the same direction as the main axis runs down the columns. |
| ColumnReverse | The child components are arranged opposite to the **Column** direction. |

#### FlexWrap

Sets whether elements are arranged in a single row/column or multiple rows/columns in the **Flex** container.

**Widget capability**: This API can be used in ArkTS widgets since API version 9.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Description |
| :-- | :-- |
| NoWrap | The child components in the flex container are arranged in a single line. If any of them have minimum size constraints applied, the flex container does not forcibly shrink them when overflow occurs. |
| Wrap | The child components in the flex container are arranged in multiple lines, and they may overflow. |
| WrapReverse | The child components in the flex container are reversely arranged in multiple lines, and they may overflow. |

#### FontStyle

Sets the font style.

**Widget capability**: This API can be used in ArkTS widgets since API version 9.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Value | Description |
| :-- | :-- | :-- |
| Normal | 0 | Standard font style. |
| Italic | 1 | Italic font style. |

#### FontWeight

Sets the font weight.

**Widget capability**: This API can be used in ArkTS widgets since API version 9.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Value | Description |
| :-- | :-- | :-- |
| Lighter | \- | 100 font weight (thin). |
| Normal | \- | 400 font weight (normal). |
| Regular | \- | 400 font weight (normal), which is the same as the Normal effect. |
| Medium | \- | 500 font weight (medium). |
| Bold | \- | 700 font weight (bold). |
| Bolder | \- | 900 font weight (extra bold). |

**FontWeight** is one of the types of the input parameter **value** of the [fontWeight](../../text-and-input/text/document.md#fontweight) attribute. When **value** is of the **FontWeight**, **number**, or [ResourceStr](../basic-types/document.md#resourcestr) type, the mapping is as follows:

| FontWeight | number | ResourceStr |
| :-- | :-- | :-- |
| Lighter | 100 | 'lighter' |
| Normal | 400 | 'normal' |
| Regular | 400 | 'regular' |
| Medium | 500 | 'medium' |
| Bold | 700 | 'bold' |
| Bolder | 900 | 'bolder' |

#### FoldStatus11+

Sets the folding status of the device.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Value | Description |
| :-- | :-- | :-- |
| FOLD\_STATUS\_UNKNOWN | 0 | The folding status of the device is unknown. |
| FOLD\_STATUS\_EXPANDED | 1 | The device is fully open. |
| FOLD\_STATUS\_FOLDED | 2 | The device is folded (completely closed). |
| FOLD\_STATUS\_HALF\_FOLDED | 3 | The device is half-folded, somewhere between fully open and completely folded. |

#### FocusDrawLevel19+

Enumerates the drawing levels of the focus box for a node.

**Widget capability**: This API can be used in ArkTS widgets since API version 19.

**Atomic service API**: This API can be used in atomic services since API version 19.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Value | Description |
| :-- | :-- | :-- |
| SELF | 0 | The focus box is drawn on the node's own layer. |
| TOP | 1 | The focus box is drawn on the topmost layer of the current instance's z-order. |

#### FocusWrapMode20+

Enumerates focus wrapping modes for cross-axis directional navigation.

**Atomic service API**: This API can be used in atomic services since API version 20.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Value | Description |
| :-- | :-- | :-- |
| DEFAULT | 0 | Cross-axis directional navigation does not wrap focus. |
| WRAP\_WITH\_ARROW | 1 | 
Cross-axis directional navigation wraps focus.

In irregular grid layouts, when moving focus along the cross axis, the system prioritizes focusable items within the same row.

 |

#### GradientDirection

Sets the direction of the linear gradient.

**Widget capability**: This API can be used in ArkTS widgets since API version 9.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Description |
| :-- | :-- |
| Left | From right to left. |
| Top | From bottom to top. |
| Right | From left to right. |
| Bottom | From top to bottom. |
| LeftTop | From upper left to lower right. |
| LeftBottom | From lower left to upper right. |
| RightTop | From upper right to lower left. |
| RightBottom | From lower right to upper left. |
| None | None. |

#### HorizontalAlign

Sets the horizontal alignment mode of child components.

**Widget capability**: This API can be used in ArkTS widgets since API version 9.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Description |
| :-- | :-- |
| Start | Aligned with the start edge in the same direction as the language in use. |
| Center | Aligned with the center. This is the default alignment mode. |
| End | Aligned with the end edge in the same direction as the language in use. |

#### HoverEffect8+

Sets the hover effect of the component.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Value | Description |
| :-- | :-- | :-- |
| None | 0 | No effect. |
| Scale | 2 | Zoom-in and zoom-out effect. |
| Highlight | 3 | Background fade-in and fade-out effect. |
| Auto | 4 | Default hover effect. |

#### HitTestMode9+

Sets the response logic and node blocking rules for the hit test.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/07/v3/7c_inpn7QU-D4bh_umLbog/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062252Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=4300924E2C76956E6003FDDEA67C08E2744D1D5FAE748F7EC590A8BA9C17BCF7)

When multiple nodes in a **Stack** component have overlapping touch areas, if the touch point hits a child component of the topmost node, only the topmost node will undergo hit testing by default. In this case, touch testing for lower-layer nodes can only be triggered by setting the [hitTestBehavior](../../universal-attributes/interaction-properties/touch-interactions/hit-test-control/document.md#hittestbehavior) of the topmost node to **HitTestMode.Transparent**.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Value | Description |
| :-- | :-- | :-- |
| Default | 0 | 
Default hit test mode. The node itself and its child nodes respond to the hit test, but block the hit test of sibling nodes. It does not affect the hit test of ancestor nodes.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| Block | 1 | 

The node itself responds to the hit test and blocks the hit test of child nodes, sibling nodes, and ancestor nodes.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| Transparent | 2 | 

Both the node itself and its child nodes respond to the hit test and do not block the hit test of sibling nodes and ancestor nodes.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| None | 3 | 

The node itself does not respond to the hit test and does not block the hit test of child nodes, sibling nodes, and ancestor nodes.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| BLOCK\_HIERARCHY20+ | 4 | 

The node itself and its child nodes respond to the hit test, preventing all sibling nodes and parent nodes with lower priority from participating in the hit test.

**Atomic service API**: This API can be used in atomic services since API version 20.

 |
| BLOCK\_DESCENDANTS20+ | 5 | 

The node itself does not respond to the hit test, and all its descendants (children, grandchildren, and more) also do not respond to the hit test. It does not affect the hit test of ancestor nodes.

**Atomic service API**: This API can be used in atomic services since API version 20.

 |

#### HeightBreakpoint13+

Enumerates the height breakpoint values corresponding to different window aspect ratio thresholds. The values are returned through [getWindowHeightBreakpoint](../../../arkts-api/ui/ohos-arkui-uicontext-uicontext/class-uicontext/document.md#getwindowheightbreakpoint13).

**Atomic service API**: This API can be used in atomic services since API version 13.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

The following table lists default aspect ratio breakpoint thresholds for typical devices, serving as a reference for responsive layout design based on window aspect ratios. Device manufacturers may customize these thresholds through product-specific configurations when needed.

| Name | Value | Description |
| :-- | :-- | :-- |
| HEIGHT\_SM | 0 | The window aspect ratio is less than 0.8. |
| HEIGHT\_MD | 1 | The window aspect ratio is greater than or equal to 0.8 and less than 1.2. |
| HEIGHT\_LG | 2 | The window aspect ratio is greater than or equal to 1.2. |

#### ImageFit

Sets the image filling effect.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Value | Description |
| :-- | :-- | :-- |
| Fill | 0 | 
The image or video is scaled without maintaining the aspect ratio to fill the display boundaries, with horizontal center alignment.

**Widget capability**: This API can be used in ArkTS widgets since API version 9.

**Atomic service API**: This API can be used in atomic services since API version 11.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6d/v3/jvkZChocTL2k8iSYztYrYw/en-us_image_0000002568765737.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062252Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=F9CC13A914B2F2C6008A944F9AB0237DF74D09CAA8B44F7602F315903B4D6BC9)

 |
| Contain | 1 | 

The image or video is scaled with its aspect ratio retained to fit entirely within the display boundaries, with horizontal center alignment.

**Widget capability**: This API can be used in ArkTS widgets since API version 9.

**Atomic service API**: This API can be used in atomic services since API version 11.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2c/v3/u4zpjsHeQJ2oI7yXrXZbww/en-us_image_0000002537766012.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062252Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=F0334AEF0978D88083B67D2711D92F3549E17332F57219D2D17938DB04FCB076)

 |
| Cover | 2 | 

The image or video is scaled while maintaining the aspect ratio so that both sides are greater than or equal to the display boundaries, aligned horizontally in the center.

**Widget capability**: This API can be used in ArkTS widgets since API version 9.

**Atomic service API**: This API can be used in atomic services since API version 11.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/27/v3/vq0gsxb1QMmWZ9d1Q7OsRw/en-us_image_0000002537925952.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062252Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=E3BD310655B1D32B51AC67B86DFCED6C712A109BD79D08AA145D93C154C902F9)

 |
| Auto | 3 | 

The image or video is scaled appropriately based on its own dimensions and the component's size to fill the view while maintaining the aspect ratio, aligned horizontally in the center.

**Widget capability**: This API can be used in ArkTS widgets since API version 9.

**Atomic service API**: This API can be used in atomic services since API version 11.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b5/v3/sYLid7KPTuu5MgwPsg_HHQ/en-us_image_0000002568685729.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062252Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=0708FF1657972609CC94E1D0AFD5B4923E893B3C5375C405B5219466587D3AA5)

 |
| None | 5 | 

The image is displayed at its original size, aligned horizontally in the center.

**Widget capability**: This API can be used in ArkTS widgets since API version 9.

**Atomic service API**: This API can be used in atomic services since API version 11.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/69/v3/jN9W0D-_QaW4Kz7QchzX_g/en-us_image_0000002568765739.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062252Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=98CF0E88F482CA85472D4AC733552DDC150CC7162120A2DC1335043AB19B5B1D)

 |
| ScaleDown | 6 | 

The image or video is displayed while maintaining the aspect ratio, only scaling down or keeping the original size, aligned horizontally in the center.

**Widget capability**: This API can be used in ArkTS widgets since API version 9.

**Atomic service API**: This API can be used in atomic services since API version 11.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1e/v3/a5r7AQMgRcmMUZkxduYhog/en-us_image_0000002537766014.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062252Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=C25A62C5680527378181137787A6EF9611643F7065DB3E974959401E607A1951)

 |
| TOP\_START12+ | 7 | 

The image or video is displayed at the top start position of the component in the original size.

**Widget capability**: This API can be used in ArkTS widgets since API version 12.

**Atomic service API**: This API can be used in atomic services since API version 12.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/91/v3/CM3TlGYmS4aDNAWBtTE85w/en-us_image_0000002537925954.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062252Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=B4DEA4A0DED1BF486557B3411B13B0BEE68ACFE3EF38A1A14006A0729679BDC7)

 |
| TOP12+ | 8 | 

The image or video is displayed at the top center position of the component in the original size.

**Widget capability**: This API can be used in ArkTS widgets since API version 12.

**Atomic service API**: This API can be used in atomic services since API version 12.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e1/v3/faoxmtVHTi-VJfyK89JUEQ/en-us_image_0000002568685731.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062252Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=69F31DEBF93E221C164C96748618058BFE997D0AFCA54721D4798B693308CFE9)

 |
| TOP\_END12+ | 9 | 

The image or video is displayed at the top end position of the component in the original size.

**Widget capability**: This API can be used in ArkTS widgets since API version 12.

**Atomic service API**: This API can be used in atomic services since API version 12.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6b/v3/U5UVUMemRIqy4Oj-LW1rpQ/en-us_image_0000002568765741.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062252Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=F52FD81953F24121BCAB7B502B2BAE2A57882497F7234B8A2F8D305FEE2498A7)

 |
| START12+ | 10 | 

The image or video is displayed at the start position (vertically centered) of the component in the original size.

**Widget capability**: This API can be used in ArkTS widgets since API version 12.

**Atomic service API**: This API can be used in atomic services since API version 12.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/eb/v3/_BEM6sJSSHuJFyYmSOJYSQ/en-us_image_0000002537766016.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062252Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=A6C6061C924AE8C08F9C1FC7B1EAC7E2145819E02C99533B044ACF95E99C0BFD)

 |
| CENTER12+ | 11 | 

The image or video is displayed at the center position of the component in the original size.

**Widget capability**: This API can be used in ArkTS widgets since API version 12.

**Atomic service API**: This API can be used in atomic services since API version 12.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5d/v3/2fXvA5IoS32LIoRnp-YMsw/en-us_image_0000002537925956.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062252Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=6A514BA7BA60B52A09AF4BFBC31ED8C343E1B2BB1F3704349C7723B6C24073D0)

 |
| END12+ | 12 | 

The image or video is displayed at the end position (vertically centered) of the component in the original size.

**Widget capability**: This API can be used in ArkTS widgets since API version 12.

**Atomic service API**: This API can be used in atomic services since API version 12.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0/v3/nzQm7zk_RlOGg6A6cQBq9g/en-us_image_0000002568685733.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062252Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=DD08895DB14897EF64D308231C1AEDB43184630D9CBBB04F4E9AC1022F3DC20E)

 |
| BOTTOM\_START12+ | 13 | 

The image or video is displayed at the bottom start position of the component in the original size.

**Widget capability**: This API can be used in ArkTS widgets since API version 12.

**Atomic service API**: This API can be used in atomic services since API version 12.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/30/v3/oDvJUsLmR3yGrFQ1faf5vQ/en-us_image_0000002568765743.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062252Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=8C4D6A4CF959F8C0C5716A23E6CFDDDE4BF29AFA64A3EC3DF94268961352AC0B)

 |
| BOTTOM12+ | 14 | 

The image or video is displayed at the bottom center position of the component in the original size.

**Widget capability**: This API can be used in ArkTS widgets since API version 12.

**Atomic service API**: This API can be used in atomic services since API version 12.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f1/v3/LNfblU8FQDCDQglSqfffAw/en-us_image_0000002537766018.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062252Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=036F02D889710A26870D21E25299780C767A9FAF6ADF72C164908E19A81EBC2A)

 |
| BOTTOM\_END12+ | 15 | 

The image or video is displayed at the bottom end position of the component in the original size.

**Widget capability**: This API can be used in ArkTS widgets since API version 12.

**Atomic service API**: This API can be used in atomic services since API version 12.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/62/v3/ykcEwNl1T8OVC0gHf2BiQw/en-us_image_0000002537925958.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062252Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=C657952EC83F6E0F1BDD5F6AA13238C514B771D0D49C85D605E3CB57DC8AA38A)

 |
| MATRIX15+ | 16 | 

The image, with the use of [imageMatrix](../../images-and-videos/image/document.md#imagematrix15), is displayed in the specified position of the **Image component**, keeping its original size. SVG images are not supported.

**Atomic service API**: This API can be used in atomic services since API version 15.

 |

#### ItemAlign

Sets the alignment mode of an element on the cross axis of the container.

**Widget capability**: This API can be used in ArkTS widgets since API version 9.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Description |
| :-- | :-- |
| Auto | The default configuration of the flex container is used. |
| Start | The items in the flex container are aligned with the cross-start edge. |
| Center | The items in the flex container are centered along the cross axis. |
| End | The items in the flex container are aligned with the cross-end edge. |
| Stretch | The items in the flex container are stretched and padded along the cross axis. If the flex container has the **Wrap** attribute set to **FlexWrap.Wrap** or **FlexWrap.WrapReverse**, the items are stretched to the cross size of the widest element on the current row or column. In other cases, the items are stretched to the container size regardless of whether their size is set. |
| Baseline | The items in the flex container are aligned in such a manner that their text baselines are aligned along the cross axis. |

#### ImageRepeat

Sets the image repeat pattern.

**Widget capability**: This API can be used in ArkTS widgets since API version 9.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Value | Description |
| :-- | :-- | :-- |
| NoRepeat | 0 | The image is not repeatedly drawn. |
| X | 1 | The image is repeatedly drawn only along the horizontal axis. |
| Y | 2 | Images are repeatedly drawn only on the vertical axis. |
| XY | 3 | The image is repeatedly drawn along both axes. |

#### ImageSize

Sets the width and height effect of an image.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Value | Description |
| :-- | :-- | :-- |
| Cover | 1 | 
The image is scaled with its aspect ratio retained for both sides to be greater than or equal to the display boundaries.

**Widget capability**: This API can be used in ArkTS widgets since API version 9.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| Contain | 2 | 

The image is scaled with its aspect ratio retained for the content to be completely displayed within the display boundaries.

**Widget capability**: This API can be used in ArkTS widgets since API version 9.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| Auto | 0 | 

The original image aspect ratio is retained.

**Widget capability**: This API can be used in ArkTS widgets since API version 9.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| FILL12+ | 3 | 

The image is scaled to fill the display area, and its aspect ratio is not retained.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |

#### ImageSpanAlignment10+

Sets the alignment mode of the image relative to the line height.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Value | Description |
| :-- | :-- | :-- |
| TOP | 1 | 
The image is top aligned with the line.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| CENTER | 2 | 

The image is centered aligned with the line.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| BOTTOM | 3 | 

The image is bottom aligned with the line.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| BASELINE | 4 | 

The image is bottom aligned with the text baseline.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| FOLLOW\_PARAGRAPH20+ | 5 | 

The alignment mode follows the parent component of the **Text** component.

**Atomic service API**: This API can be used in atomic services since API version 20.

 |

#### InteractionHand15+

Enumerates how an input event is triggered.

**Atomic service API**: This API can be used in atomic services since API version 15.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Value | Description |
| :-- | :-- | :-- |
| NONE | 0 | Unspecified. |
| LEFT | 1 | Left-hand interaction. |
| RIGHT | 2 | Right-hand interaction. |

#### KeySource

Sets the device type that triggers the button event.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Value | Description |
| :-- | :-- | :-- |
| Unknown | 0 | Unknown input device. |
| Keyboard | 4 | The input device is a keyboard. |
| JOYSTICK15+ | 5 | 
The input device is a joystick.

**Atomic service API**: This API can be used in atomic services since API version 15.

 |

#### KeyType

Sets the status type of a button operation.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Value | Description |
| :-- | :-- | :-- |
| Down | 0 | The key is pressed. |
| Up | 1 | The key is released. |

#### LineJoinStyle

Sets the line connection style.

**Widget capability**: This API can be used in ArkTS widgets since API version 9.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Value | Description |
| :-- | :-- | :-- |
| Miter | 0 | Miter is used to connect paths. |
| Round | 1 | Round is used to connect paths. |
| Bevel | 2 | Bevel is used to connect paths. |

#### LocalizedAlignment20+

Enumerated type that supports the align and [layoutGravity](../../universal-attributes/layout-and-borders/location/document.md#layoutgravity20) attributes.

**Widget capability**: This API can be used in ArkTS widgets since API version 20.

**Atomic service API**: This API can be used in atomic services since API version 20.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Value | Description |
| :-- | :-- | :-- |
| TOP\_START | 'top\_start' | Top start. |
| TOP | 'top' | Horizontally centered on the top. |
| TOP\_END | 'top\_end' | Top end. |
| START | 'start' | Vertically centered start. |
| CENTER | 'center' | Horizontally and vertically centered. |
| END | 'end' | Vertically centered end. |
| BOTTOM\_START | 'bottom\_start' | Bottom start. |
| BOTTOM | 'bottom' | Horizontally centered on the bottom. |
| BOTTOM\_END | 'bottom\_end' | Bottom end. |

#### LineCapStyle

Sets the line endpoint style.

**Widget capability**: This API can be used in ArkTS widgets since API version 9.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Value | Description |
| :-- | :-- | :-- |
| Butt | 0 | The ends of the line are squared off, and the line does not extend beyond its two endpoints. |
| Round | 1 | The line is extended at the endpoints by a half circle whose diameter is equal to the line width. |
| Square | 2 | The line is extended at the endpoints by a rectangle whose width is equal to half the line width and height equal to the line width. |

#### LineBreakStrategy12+

Sets the line break rule.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Value | Description |
| :-- | :-- | :-- |
| GREEDY | 0 | Places as many words on a line as possible and moves to the next line only if no more words can fit into the same line. |
| HIGH\_QUALITY | 1 | Fills in lines as much as possible on the basis of **BALANCED**, which may results in a large blank area on the last line. |
| BALANCED | 2 | Without splitting words, the width of each line in a paragraph is the same as much as possible. |

#### MouseButton8+

Enumerates the mouse button types.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Value | Description |
| :-- | :-- | :-- |
| Left | 1 | Left button on the mouse. |
| Right | 2 | Right button on the mouse. |
| Middle | 4 | Middle button on the mouse. |
| Back | 8 | Back button on the left of the mouse. |
| Forward | 16 | Forward button on the left of the mouse. |
| None | 0 | No button. |

#### MouseAction8+

Sets the action type of a mouse operation.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/49/v3/sgKJUM8fSq60yQinZkfbCQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062252Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=86FE72E21F1FB7C09FE00A649E38152D7A74F15BD0383323C4078FD426C7F681)

You may receive values outside the defined enumeration range for this attribute and these values can be ignored.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Value | Description |
| :-- | :-- | :-- |
| Press | 1 | 
The mouse button is pressed.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| Release | 2 | 

The mouse button is released.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| Move | 3 | 

The mouse cursor moves.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| Hover | 4 | 

The mouse pointer is hovered on an element.

Note: This value has no effect.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| CANCEL18+ | 13 | 

The mouse button action is canceled. It is triggered in the following scenarios:

1\. Component focus loss: This action is triggered when a currently focused component loses focus due to a system event (such as pop-up interruption or app switching).

2\. Event interruption: During a mouse operation, if a higher-priority event occurs (such as a system-level gesture or forced event stream recycling), causing the current mouse operation to be forcibly terminated.

3\. Abnormal state exit: In scenarios such as component destruction or abnormal rendering environment, unfinished mouse events are marked as canceled.

**Atomic service API**: This API can be used in atomic services since API version 18.

 |

#### ModifierKey10+

Enumerates the input method modifier keys.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Value | Description |
| :-- | :-- | :-- |
| CTRL | 0 | Ctrl key on the keyboard. |
| SHIFT | 1 | Shift key on the keyboard. |
| ALT | 2 | Alt key on the keyboard. |

#### MarqueeUpdateStrategy12+

Sets the scrolling strategy for the marquee after its attributes are updated.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Value | Description |
| :-- | :-- | :-- |
| DEFAULT | 0 | After the marquee attributes are updated, the marquee scrolls from the start position. |
| PRESERVE\_POSITION | 1 | After the marquee attributes are updated, the marquee scrolls from the current position. |

#### NestedScrollMode10+

Sets the nested mode of a nested scrollable component.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Value | Description |
| :-- | :-- | :-- |
| SELF\_ONLY | 0 | The scrolling is contained within the component, and no scroll chaining occurs, that is, the parent component does not scroll when the component scrolling reaches the boundary. |
| SELF\_FIRST | 1 | The component scrolls first, and when it hits the boundary, the parent component scrolls. When the parent component hits the boundary, its edge effect is displayed. If no edge effect is specified for the parent component, the edge effect of the child component is displayed instead. |
| PARENT\_FIRST | 2 | The parent component scrolls first, and when it hits the boundary, the component scrolls. When the component hits the boundary, its edge effect is displayed. If no edge effect is specified for the component, the edge effect of the parent component is displayed instead. |
| PARALLEL | 3 | The component and its parent component scroll at the same time. When both the component and its parent component hit the boundary, the edge effect of the component is displayed. If no edge effect is specified for the component, the edge effect of the parent component is displayed instead. |

#### Nullable<T>11+

type Nullable<T> = T | undefined

This type allows for an object of a custom type or **undefined**.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Type | Description |
| :-- | :-- |
| T | The object can be of any custom type. |
| undefined | The object can be **undefined**. |

#### ObscuredReasons10+

Sets how the component content is obscured.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Value | Description |
| :-- | :-- | :-- |
| PLACEHOLDER | 0 | The content is replaced by a placeholder. |

#### OptionWidthMode11+

Sets the width mode of the drop-down menu.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Value | Description |
| :-- | :-- | :-- |
| FIT\_CONTENT | 'fit\_content' | If this value is set, the width of the drop-down menu is 2 columns by default. |
| FIT\_TRIGGER | 'fit\_trigger' | Inherits the width of the drop-down list button. |

#### PlayMode

Sets the animation playback mode.

**Widget capability**: This API can be used in ArkTS widgets since API version 9.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Value | Description |
| :-- | :-- | :-- |
| Normal | 0 | The animation is played forwards. |
| Reverse | 1 | The animation is played backwards. |
| Alternate | 2 | The animation is played forwards for an odd number of times (1, 3, 5...) and backwards for an even number of times (2, 4, 6...). |
| AlternateReverse | 3 | The animation is played backwards for an odd number of times (1, 3, 5...) and forwards for an even number of times (2, 4, 6...). |

#### Placement8+

Sets the position of a bubble.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Description |
| :-- | :-- |
| Left | The popup is on the left of the component, vertically aligned with the component on the left. |
| Right | The popup is on the right of the component, vertically aligned with the component on the right. |
| Top | The popup is at the top of the component, horizontally aligned with the component at the top. |
| Bottom | The popup is at the bottom of the component, horizontally aligned with the component at the bottom. |
| TopLeft | The popup is at the top of the component and, since API version 9, aligned with the left of the component. |
| TopRight | The popup is at the top of the component and, since API version 9, aligned with the right of the component. |
| BottomLeft | The popup is at the bottom of the component and, since API version 9, aligned with the left of the component. |
| BottomRight | The popup is at the bottom of the component and, since API version 9, aligned with the right of the component. |
| LeftTop9+ | The popup is on the left of the component and aligned with the top of the component. |
| LeftBottom9+ | The popup is on the left of the component and aligned with the bottom of the component. |
| RightTop9+ | The popup is on the right of the component and aligned with the top of the component. |
| RightBottom9+ | The popup is on the right of the component and aligned with the bottom of the component. |

#### PixelRoundCalcPolicy11+

Enumerates the pixel rounding policies for component boundaries.

**Widget capability**: This API can be used in ArkTS widgets since API version 11.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Value | Description |
| :-- | :-- | :-- |
| NO\_FORCE\_ROUND | 0 | The value is not rounded off. |
| FORCE\_CEIL | 1 | Rounded-up calculation. |
| FORCE\_FLOOR | 2 | Rounded-down calculation. |

#### PageFlipMode15+

Enumerates the modes for flipping pages using the mouse wheel.

**Widget capability**: This API can be used in ArkTS widgets since API version 15.

**Atomic service API**: This API can be used in atomic services since API version 15.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Value | Description |
| :-- | :-- | :-- |
| CONTINUOUS | 0 | Continuous page flipping mode where multiple pages are turned continuously when the user scrolls the mouse wheel without interruption. |
| SINGLE | 1 | Single-page flipping mode where the mouse wheel event is ignored until the current page flipping animation is complete. |

#### PixelRoundMode18+

Enumerates pixel rounding modes.

**Widget capability**: This API can be used in ArkTS widgets since API version 18.

**Atomic service API**: This API can be used in atomic services since API version 18.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Value | Description |
| :-- | :-- | :-- |
| PIXEL\_ROUND\_ON\_LAYOUT\_FINISH | 0 | Performs pixel rounding after the component finishes measuring its size and position. Default value. |
| PIXEL\_ROUND\_AFTER\_MEASURE | 1 | Performs pixel rounding after the component finishes measuring its size. |

#### PresetFillType22+

Enumerates column count policies for different [breakpoints](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/arkts-layout-development-grid-layout#breakpoints).

**Atomic service API**: This API can be used in atomic services since API version 22.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Value | Description |
| :-- | :-- | :-- |
| BREAKPOINT\_DEFAULT | 0 | 
**List** or **Swiper** component: 1 column (SM or smaller), 2 columns (MD), 3 columns (LG or larger).

**Grid** or **WaterFlow** component: 2 columns (SM or smaller), 3 columns (MD), 5 columns (LG or larger).

 |
| BREAKPOINT\_SM1MD2LG3 | 1 | 1 column (SM or smaller), 2 columns (MD), 3 columns (LG or larger). |
| BREAKPOINT\_SM2MD3LG5 | 2 | 2 columns (SM or smaller), 3 columns (MD), 5 columns (LG or larger). |

#### RelateType

Sets the padding mode of a child component.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Value | Description |
| :-- | :-- | :-- |
| FILL | 0 | The current child component is scaled to fill the parent component. |
| FIT | 1 | The current child component is scaled to adapt to the parent component. |

#### ResponseRegionSupportedTool22+

Sets the type of the input tool applicable to the touch target.

**Atomic service API**: This API can be used in atomic services since API version 22.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Value | Description |
| :-- | :-- | :-- |
| ALL | 0 | All input tool types. |
| FINGER | 1 | Finger. |
| PEN | 2 | Stylus. |
| MOUSE | 3 | Mouse. |

#### ResponseType8+

Sets how menu display is triggered.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Description |
| :-- | :-- |
| LongPress | The menu is displayed when the component is long-pressed. |
| RightClick | Shows the shortcut menu by right-clicking the text. |

#### RenderFit10+

Enumerates the modes in which the final state of the component's content is rendered during its width and height animation process.

**Widget capability**: This API can be used in ArkTS widgets since API version 18.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Value | Description |
| :-- | :-- | :-- |
| CENTER | 0 | The component's content stays at the final size and always aligned with the center of the component. ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6/v3/bbILVTopTGCUiqQTsqp7Hw/en-us_image_0000002568685735.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062252Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=D9FFE1EDFCD450406F4AD6BD1566BF6ABB93B62453D39552557E6F76886C0DF8) |
| TOP | 1 | The component's content stays at the final size and always aligned with the top center of the component. ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5b/v3/-FWWsIU4R6WIonDHiHVu1g/en-us_image_0000002568765745.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062252Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=AD6CDB3B5E12D0BE66E3822E698F2761E512398686925B8A0A0201E7D7E54511) |
| BOTTOM | 2 | The component's content stays at the final size and always aligned with the bottom center of the component. ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7/v3/Muint9evTy2QfCpGZEgzIw/en-us_image_0000002537766020.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062252Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=35E9FB0BDF98E7038A2A32244B882363156C0C63DB4A3FC9D5E619AD4A210A9F) |
| LEFT | 3 | The component's content stays at the final size and always aligned with the left of the component. ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2b/v3/_IfEyl1OSkOEy_cLAkwAgg/en-us_image_0000002537925960.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062252Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=ADD4BC313C1611FB045F47844AADF58E86B30207CD2D14D6972628C53828294B) |
| RIGHT | 4 | The component's content stays at the final size and always aligned with the right of the component. ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/46/v3/fYwCqbS0Sf2Alr2XvrG_JA/en-us_image_0000002568685737.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062252Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=78F08878EFCBFF41BD817A415A5589ECFE8C080CC008F1C8348A012FD030AA7C) |
| TOP\_LEFT | 5 | The component's content stays at the final size and always aligned with the upper left corner of the component. ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fe/v3/KuPdPWMnSWukfjE7LiB0jg/en-us_image_0000002568765747.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062252Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=8BD7D4ECB539C21EECD7A64545A2DA2E1083F85AEF72DF6A727D802CD9882DA9) |
| TOP\_RIGHT | 6 | The component's content stays at the final size and always aligned with the upper right corner of the component. ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/af/v3/ZTfmhI0KRhSAD8rzJfy-eg/en-us_image_0000002537766022.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062252Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=EBC1184CEDCDCCC64094D83D90262B441A8613A47ED001C3FEED7FCFD8DFBF40) |
| BOTTOM\_LEFT | 7 | The component's content stays at the final size and always aligned with the lower left corner of the component. ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3b/v3/0VNBZzeZQra0ORwvWotNow/en-us_image_0000002537925962.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062252Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=D83AE503925AF9688D9E713355E601D972E51DDCCB83CF56C70E426A108B6872) |
| BOTTOM\_RIGHT | 8 | The component's content stays at the final size and always aligned with the lower right corner of the component. ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/08/v3/4k2VIFcxTHiiTQx7VDgUrA/en-us_image_0000002568685739.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062252Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=66D166AF4AB13D134A60E94C0DD3AC1B57909CC9140DA4F63FB3AD6C37191200) |
| RESIZE\_FILL | 9 | The component's content is always resized to fill the component's content box, without considering its aspect ratio in the final state. ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/06/v3/SePqVPy-TCmgWOLNoybjQA/en-us_image_0000002568765749.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062252Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=054CE4C35F6553A1F1BED0F08C3CD3802A4C022253588B5DEE07770634DD1282) |
| RESIZE\_CONTAIN | 10 | While maintaining its aspect ratio in the final state, the component's content is scaled to fit within the component's content box. It is always aligned with the center of the component. ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/de/v3/upPuzURYRbqwYN1QfkVODw/en-us_image_0000002537766024.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062252Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=18CB818EC3E509E5CDC4D5D69584EF01ECD4509068536A01CC9825A293CFDCC9) |
| RESIZE\_CONTAIN\_TOP\_LEFT | 11 | While maintaining its aspect ratio in the final state, the component's content is scaled to fit within the component's content box. When there is remaining space in the width direction of the component, the content is left-aligned with the component. When there is remaining space in the height direction of the component, the content is top-aligned with the component. ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/23/v3/9-iOOpn8RQekCwk7gs1hAw/en-us_image_0000002537925964.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062252Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=88FFC912EC7E0D9D04120510F2E4B67AE0E63839D387550BD67441F4C666C1AE) |
| RESIZE\_CONTAIN\_BOTTOM\_RIGHT | 12 | While maintaining its aspect ratio in the final state, the component's content is scaled to fit within the component's content box. When there is remaining space in the width direction of the component, the content is right-aligned with the component. When there is remaining space in the height direction of the component, the content is bottom-aligned with the component. ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/36/v3/c9_nzyXgQVWI960-t3gdqg/en-us_image_0000002568685741.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062252Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=C813E0F36C9BCC429849BBE035805363E3D60216DD69E11FF7A1E9605E331AE8) |
| RESIZE\_COVER | 13 | While maintaining its aspect ratio in the final state, the component's content is scaled to cover the component's entire content box. It is always aligned with the center of the component, so that its middle part is displayed. ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ed/v3/ZbVhXZCURl6kozRfSz6CTQ/en-us_image_0000002568765751.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062252Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=D35514ED4457564542EF2DED91CA4C2B083568C9BDAFA36BEC620C7B85B6C560) |
| RESIZE\_COVER\_TOP\_LEFT | 14 | While maintaining its aspect ratio in the final state, the component's content is scaled to cover the component's entire content box. When there is remaining space in the width direction, the content is left-aligned with the component, so that its left part is displayed. When there is remaining space in the height direction, the content is top-aligned with the component, so that its top part is displayed. ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/50/v3/YpAfkd0TTLSE2XM5bcd7lw/en-us_image_0000002537766026.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062252Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=9626A1BE435329E1EC25896522D4D6A4EC04F2C2BD183C0113F62D249E43C121) |
| RESIZE\_COVER\_BOTTOM\_RIGHT | 15 | While maintaining its aspect ratio in the final state, the component's content is scaled to cover the component's entire content box. When there is remaining space in the width direction, the content is right-aligned with the component, so that its right part is displayed. When there is remaining space in the height direction, the content is bottom-aligned with the component, so that its bottom part is displayed. ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5/v3/CPLNRRjeSECc5dtW015Xdw/en-us_image_0000002537925966.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062252Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=6D3739958F5764FCF882A02C3FE1485C3A613A16E231FD9CC85A5D0927739C99) |

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/36/v3/0afqBH_aTlaWErvPWcHZBA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062252Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=6876100CCCCE6F5C5DB6F45F674BBDEDAD823DC68F8ACBBF17C59D0F66EEE8B7)

-   In the illustrative diagrams, the blue area indicates the content, and the orange area indicates the component content box.
-   Different render fit modes create different effects during the width and height animation process. Choose the one that best fits your need.

#### RenderStrategy22+

Enumerates rendering strategies for drawing rounded corners.

**Atomic service API**: This API can be used in atomic services since API version 22.

**Widget capability**: This API can be used in ArkTS widgets since API version 22.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Value | Description |
| :-- | :-- | :-- |
| FAST | 0 | 
Online rendering mode. The content to be rendered is clipped with rounded corners and directly rendered to the main canvas.

Note: Online rendering may cause display anomalies in certain scenarios. For example, when blur effects are applied within rounded corner components, background colors may interact and create gradient overlay effects. For detailed behavior, see [Example 3: Configuring Offscreen Rounded Corners](../../universal-attributes/layout-and-borders/border-styling/document.md#example-3-configuring-offscreen-rounded-corners).

 |
| OFFSCREEN | 1 | 

Offscreen rendering mode. The content to be rendered is first rendered to the offscreen canvas without rounded corners, and then clipped with rounded corners and rendered to the main canvas.

**NOTE**

1\. Compared with online rendering, offscreen rendering requires additional performance overhead.

2\. In offscreen rendering, the content is first rendered on an additional canvas, and then rendered on the main canvas.

3\. Use offscreen rendering primarily for multi-layer components requiring rounded corners. For single components, it has effect only when the [clip](../../universal-attributes/visual-effects/shape-clipping/document.md#clip12) attribute, [background color](../../universal-attributes/basic-attributes/background/document.md), or [foreground color](../../universal-attributes/visual-effects/foreground-color/document.md) is configured.

 |

#### ScrollSource12+

Enumerates the sources of scroll operations.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Value | Description |
| :-- | :-- | :-- |
| DRAG | 0 | Drag event. |
| FLING | 1 | Inertia scrolling after the drag ends. |
| EDGE\_EFFECT | 2 | Edge scrolling effect with **EdgeEffect.Spring**. |
| OTHER\_USER\_INPUT | 3 | Other user inputs aside from dragging, such as those from the mouse wheel and keyboard events. |
| SCROLL\_BAR | 4 | Drag event from the scrollbar. |
| SCROLL\_BAR\_FLING | 5 | Inertia scrolling with velocity after the scrollbar is released. |
| SCROLLER | 6 | Non-animated methods of the **Scroller** object. |
| SCROLLER\_ANIMATION | 7 | Animated methods of the **Scroller** object. |

#### SharedTransitionEffectType

Sets the animation type.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Description |
| :-- | :-- |
| Static | 
The target page element remains in a fixed position, with configurable opacity animation.

Currently, this effect only takes effect when configured for redirection to the target page.

 |
| Exchange | The source page element moves to the position of the target page element and scales accordingly. |

#### TouchType

Sets the trigger status type of a touch operation.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Value | Description |
| :-- | :-- | :-- |
| Down | 0 | 
A finger is pressed.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| Up | 1 | 

A finger is lifted.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| Move | 2 | 

A finger moves on the screen in pressed state.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| Cancel | 3 | 

A touch event is canceled. Examples: 1. touching the home button to return to the home screen while keeping a finger on the screen; 2. folding a foldable phone to switch to the external screen while keeping a finger on the screen.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| HOVER\_ENTER20+ | 9 | 

A finger is pressed in accessibility mode.

**Atomic service API**: This API can be used in atomic services since API version 20.

 |
| HOVER\_MOVE20+ | 10 | 

The mouse pointer moves in accessibility mode.

**Atomic service API**: This API can be used in atomic services since API version 20.

 |
| HOVER\_EXIT20+ | 11 | 

The mouse pointer exits the component in accessibility mode.

**Atomic service API**: This API can be used in atomic services since API version 20.

 |
| HOVER\_CANCEL20+ | 12 | 

The triggered event is canceled in accessibility mode.

**Atomic service API**: This API can be used in atomic services since API version 20.

 |

#### TitleHeight9+

Sets the recommended height of the title bar.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Description |
| :-- | :-- |
| MainOnly | Recommended height (56 vp) of the title bar when only the main title is available. |
| MainWithSub | Recommended height (82 vp) of the title bar when both the main title and subtitle exist. |

#### TransitionType

Sets the transition type.

**Widget capability**: This API can be used in ArkTS widgets since API version 9.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Value | Description |
| :-- | :-- | :-- |
| All | 0 | The transition takes effect in all scenarios. |
| Insert | 1 | The transition takes effect when a component is inserted or displayed. |
| Delete | 2 | The transition takes effect when a component is deleted or hidden. |

#### TextAlign

Sets the horizontal alignment of the text.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Value | Description |
| :-- | :-- | :-- |
| Start | 0 | 
Aligned with the start.

**Widget capability**: This API can be used in ArkTS widgets since API version 9.

 |
| Center | 1 | 

Horizontally centered.

**Widget capability**: This API can be used in ArkTS widgets since API version 9.

 |
| End | 2 | 

Aligned with the end.

**Widget capability**: This API can be used in ArkTS widgets since API version 9.

 |
| JUSTIFY10+ | 3 | 

Aligned with both margins.

**Widget capability**: This API can be used in ArkTS widgets since API version 10.

 |

#### TextOverflow

Sets the display mode when the text is too long.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Value | Description |
| :-- | :-- | :-- |
| None | 0 | 
Overflowing content is clipped at the limit of the maximum line width.

**Widget capability**: This API can be used in ArkTS widgets since API version 9.

 |
| Clip | 1 | 

Overflowing content is clipped at the limit of the maximum line width. Same effect as **None**.

**Widget capability**: This API can be used in ArkTS widgets since API version 9.

 |
| Ellipsis | 2 | 

An ellipsis (...) is used to represent text overflow.

**Widget capability**: This API can be used in ArkTS widgets since API version 9.

 |
| MARQUEE10+ | 3 | Text continuously scrolls when text overflow occurs. |

#### TextDecorationType

Sets the text decoration type.

**Widget capability**: This API can be used in ArkTS widgets since API version 9.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Value | Description |
| :-- | :-- | :-- |
| None | 0 | No text decorations. |
| Underline | 1 | Line below the text. |
| Overline | 2 | Line above the text. |
| LineThrough | 3 | Line through the text. |

#### TextCase

Sets the text case.

**Widget capability**: This API can be used in ArkTS widgets since API version 9.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Value | Description |
| :-- | :-- | :-- |
| Normal | 0 | The original case of the text is retained. |
| LowerCase | 1 | All letters in the text are in lowercase. |
| UpperCase | 2 | All letters in the text are in uppercase. |

#### TextHeightAdaptivePolicy10+

Sets the mode of adjusting the text font size to adapt to the layout.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Value | Description |
| :-- | :-- | :-- |
| MAX\_LINES\_FIRST | 0 | Sets the text height adaptation mode to [maxLines](../../text-and-input/textarea/document.md#maxlines10) first. |
| MIN\_FONT\_SIZE\_FIRST | 1 | Prioritize the **minFontSize** settings. |
| LAYOUT\_CONSTRAINT\_FIRST | 2 | Prioritize the layout constraint settings in terms of height. |

#### TextContentStyle10+

Sets the polymorphic style of the text box.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Value | Description |
| :-- | :-- | :-- |
| DEFAULT | \- | Default style. The caret width is fixed at 1.5 vp, and the caret height is subject to the background height and font size of the selected text. |
| INLINE | \- | 
Inline input style. The background height of the selected text is the same as the height of the text box.

This style is used in scenarios where editing and non-editing states are obvious, for example, renaming in the file list view.

The **showError** attribute is not supported for this style.

This style does not allow for text dragging and dropping.

 |

#### TextSelectableMode12+

Sets whether text can be selected and focused on.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Value | Description |
| :-- | :-- | :-- |
| SELECTABLE\_UNFOCUSABLE | 0 | The text is selectable, but not focusable. Setting the **selection**, **bindSelectionMenu**, or **copyOption** attribute does not affect the behavior. |
| SELECTABLE\_FOCUSABLE | 1 | The text is selectable and focusable. It obtains focus when touched. |
| UNSELECTABLE | 2 | The text is not selectable nor focusable. The **selection**, **bindSelectionMenu**, and **copyOption** attributes do not work in this case. |

#### TextDecorationStyle12+

Sets the style of the text decoration.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Value | Description |
| :-- | :-- | :-- |
| SOLID | 0 | Single solid line (default value). |
| DOUBLE | 1 | Double solid line. |
| DOTTED | 2 | Dotted line. |
| DASHED | 3 | Dashed line. |
| WAVY | 4 | Wavy line. |

#### TipsAnchorType20+

Enumerates anchor types of the tooltip.

**Atomic service API**: This API can be used in atomic services since API version 20.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Description |
| :-- | :-- |
| TARGET | The tooltip follows the target component. |
| CURSOR | The tooltip follows the cursor position. |

#### VerticalAlign

Sets the vertical alignment mode of child components.

**Widget capability**: This API can be used in ArkTS widgets since API version 9.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Description |
| :-- | :-- |
| Top | Top aligned. |
| Center | Center aligned. This is the default alignment mode. |
| Bottom | Bottom aligned. |

#### Visibility

Defines the visibility and layout placeholder status of the component.

**Widget capability**: This API can be used in ArkTS widgets since API version 9.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Value | Description |
| :-- | :-- | :-- |
| Hidden | 1 | The component is hidden, and a placeholder is used for it in the layout. |
| Visible | 0 | The component is visible. |
| None | 2 | The component is hidden. It is not involved in the layout, and no placeholder is used for it. |

#### Week

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Description |
| :-- | :-- |
| Mon | Monday. |
| Tue | Tuesday. |
| Wed | Wednesday. |
| Thur | Thursday. |
| Fri | Friday. |
| Sat | Saturday. |
| Sun | Sunday. |

#### WidthBreakpoint13+

Enumerates the width breakpoint values corresponding to different window width thresholds. The values are returned through [getWindowWidthBreakpoint](../../../arkts-api/ui/ohos-arkui-uicontext-uicontext/class-uicontext/document.md#getwindowwidthbreakpoint13).

**Atomic service API**: This API can be used in atomic services since API version 13.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

The following table lists default width breakpoint thresholds for typical devices, serving as a reference for responsive layout design based on window width breakpoints. Device manufacturers may customize these thresholds through product-specific configurations when needed.

| Name | Value | Description |
| :-- | :-- | :-- |
| WIDTH\_XS | 0 | The window width is less than 320 vp. |
| WIDTH\_SM | 1 | The window width is greater than or equal to 320 vp and less than 600 vp. |
| WIDTH\_MD | 2 | The window width is greater than or equal to 600 vp and less than 840 vp. |
| WIDTH\_LG | 3 | The window width is greater than or equal to 840 vp and less than 1440 vp. |
| WIDTH\_XL | 4 | The window width is greater than or equal to 1440 vp. |

#### WordBreak11+

Sets the word break rule.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Value | Description |
| :-- | :-- | :-- |
| NORMAL | 0 | 
Word breaks can occur between any two characters for Chinese, Japanese, and Korean (CJK) text, but can occur only at a space character for non-CJK text (such as English).

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| BREAK\_ALL | 1 | 

Line breaks can occur between any two characters for non-CJK text. For CJK text, the effect is the same as that of **NORMAL**.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| BREAK\_WORD | 2 | 

This option has the same effect as **BREAK\_ALL** for non-CJK text, except that it preferentially wraps lines at appropriate characters (for example, spaces). If no breakpoints are found, it breaks between any two characters. For CJK text, the effect is the same as that of **NORMAL**.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| HYPHENATION18+ | 3 | 

Attempts are made to hyphenate words at the end of each line using a hyphen. If a hyphen cannot be added, this option behaves like **BREAK\_WORD**.

**Atomic service API**: This API can be used in atomic services since API version 18.

 |

#### XComponentType10+

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Description |
| :-- | :-- |
| SURFACE | 
The **XComponent** component is used for EGL/OpenGLES and media data input, where the custom content is displayed individually on the screen. When the background color is set to black, the display subsystem (DSS) is used.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| COMPONENT(deprecated) | 

The **XComponent** component is used as a container where non-UI logic can be executed to dynamically load the display content.

**NOTE**

This component is supported since API version 10 and deprecated since API version 12. You are advised to use other container components instead.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| TEXTURE | 

Supports EGL/OpenGLES and media data rendering. Custom drawing content is composited with XComponent's native content before display. Key features: 1. Maintains frame synchronization between GPU textures and ArkUI drawing commands. 2. Supports unified animation with built-in components. 3. Utilizes GPU composition, which may have higher power consumption than the SURFACE type using the display subsystem (DSS).

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| NODE(deprecated) | 

Serves as a container for native UI nodes, enabling display of natively developed page components.

**NOTE**

This component is supported since API version 12 and deprecated since API version 20. You are advised to use the [ContentSlot](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/arkts-rendering-control-contentslot) component.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
