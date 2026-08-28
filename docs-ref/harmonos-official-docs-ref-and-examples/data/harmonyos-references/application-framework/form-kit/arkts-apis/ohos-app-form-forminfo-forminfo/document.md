# @ohos.app.form.formInfo (formInfo)

The **formInfo** module provides types and enums related to the widget information and state.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9b/v3/AJYjnY3VRH-975lzwXD3Rg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062323Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=DFF935075B15CD8D4740BBEBC125C2843B713A2A79E8E387B6C121B67B936ADE)

The initial APIs of this module are supported since API version 9. Newly added APIs will be marked with a superscript to indicate their earliest API version.

#### Modules to Import

import { formInfo } from '@kit.FormKit';

#### FormInfo

Defines the widget information.

**System capability**: SystemCapability.Ability.Form

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| bundleName | string | No | No | 
Name of the bundle to which the widget belongs.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| moduleName | string | No | No | 

Name of the module to which the widget belongs.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| abilityName | string | No | No | 

Name of the ability to which the widget belongs.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| name | string | No | No | 

Widget name.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| displayName11+ | string | No | No | 

Widget display name.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| displayNameId11+ | number | No | No | 

ID of the widget name displayed during widget preview.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| description | string | No | No | 

Description of the widget.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| descriptionId10+ | number | No | No | 

ID of the widget description.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| type | [FormType](#formtype) | No | No | 

Type of the widget. Currently, JS and ArkTS widgets are supported.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| jsComponentName | string | No | No | 

Name of the component used in the JS widget.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| colorMode(deprecated) | [ColorMode](#colormodedeprecated) | No | No | 

Color mode of the widget.

**Atomic service API**: This API can be used in atomic services since API version 11.

**NOTE**

This API is supported since API version 9 and deprecated since API version 20. The application widget needs to support both dark and light modes. No alternative API is available.

 |
| isDefault | boolean | No | No | 

Whether the widget is the default one.

\- **true**: The widget is the default one.

\- **false**: The widget is not the default one.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| updateEnabled | boolean | No | No | 

Whether the widget is updatable.

\- **true**: The widget can be updated periodically.

\- **false**: The widget cannot be updated periodically.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| formVisibleNotify | boolean | No | No | 

Whether to send a notification when the widget is visible.

\- **true**: The widget provider is notified of the status change.

\- **false**: The widget provider is not notified of the status change.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| scheduledUpdateTime | string | No | No | 

Time when the widget was updated.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| formConfigAbility | string | No | No | 

Configuration ability of the widget, that is, the ability corresponding to the option in the selection box displayed when the widget is long pressed.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| updateDuration | number | No | No | 

Update period of the widget.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| defaultDimension | number | No | No | 

Widget specifications.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| supportDimensions | Array<number> | No | No | 

Dimensions supported by the widget. For details, see [FormDimension](#formdimension).

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| customizeData | Record<string, string> | No | No | 

Custom data of the widget.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| isDynamic10+ | boolean | No | No | 

Whether the widget is a dynamic widget.

ArkTS widgets are classified into dynamic and static widgets. JS widgets are all dynamic widgets.

\- **true**: The widget is a dynamic widget.

\- **false**: The widget is a static widget.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| transparencyEnabled11+ | boolean | No | No | 

Whether the widget supports the setting of the background transparency.

For ArkTS widgets, the support for the background transparency setting depends on user configurations. For JS widgets, the background transparency setting is not supported.

\- **true**: The widget is transparent.

\- **false**: The widget is not transparent.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| supportedShapes12+ | Array<number> | No | No | 

Shapes supported by the widget. For details about the available shapes, see [FormShape12+](#formshape12).

**Atomic service API**: This API can be used in atomic services since API version 12.

 |

#### FormType

Enumerates the widget types.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Ability.Form

| Name | Value | Description |
| :-- | :-- | :-- |
| JS | 1 | JS widget. |
| eTS | 2 | ArkTS widget. |

#### ColorMode(deprecated)

Enumerates the color modes supported by the widget. The widget theme style follows the system color mode.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/99/v3/30FO6bKgSsOdCXHn8r5OzA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062323Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=534CA1278478468C5133131E8C5F8EE7C2D5D5E44365BE0360EECCBC03905CA2)

This API is supported since API version 9 and deprecated since API version 20. The application widget needs to support both dark and light modes. No alternative API is available.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Ability.Form

| Name | Value | Description |
| :-- | :-- | :-- |
| MODE\_AUTO | \-1 | Auto mode. |
| MODE\_DARK | 0 | Dark mode. |
| MODE\_LIGHT | 1 | Light mode. |

#### FormStateInfo

Describes the widget state information.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Ability.Form

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| formState | [FormState](#formstate) | No | No | Widget state. |
| want | [Want](../../../ability-kit/arkts-apis/both-models-recommended/ohos-app-ability-want-want/document.md) | No | No | Want text. |

#### FormState

Enumerates the widget states.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Ability.Form

| Name | Value | Description |
| :-- | :-- | :-- |
| UNKNOWN | \-1 | Unknown state. |
| DEFAULT | 0 | Default state. |
| READY | 1 | Ready state. |

#### FormParam

Enumerates the widget parameters.

**System capability**: SystemCapability.Ability.Form

| Name | Value | Description |
| :-- | :-- | :-- |
| IDENTITY\_KEY | 'ohos.extra.param.key.form\_identity' | 
Widget ID.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| DIMENSION\_KEY | 'ohos.extra.param.key.form\_dimension' | 

Widget dimension. For details, see [FormDimension](#formdimension).

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| NAME\_KEY | 'ohos.extra.param.key.form\_name' | 

Widget name.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| MODULE\_NAME\_KEY | 'ohos.extra.param.key.module\_name' | 

Name of the module to which the widget belongs.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| WIDTH\_KEY | 'ohos.extra.param.key.form\_width' | 

Widget width.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| HEIGHT\_KEY | 'ohos.extra.param.key.form\_height' | 

Widget height.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| TEMPORARY\_KEY | 'ohos.extra.param.key.form\_temporary' | 

Temporary widget.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| ABILITY\_NAME\_KEY | 'ohos.extra.param.key.ability\_name' | 

Ability name.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| BUNDLE\_NAME\_KEY | 'ohos.extra.param.key.bundle\_name' | 

Bundle name.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| LAUNCH\_REASON\_KEY10+ | 'ohos.extra.param.key.form\_launch\_reason' | 

Reason for creating the widget.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| PARAM\_FORM\_CUSTOMIZE\_KEY10+ | 'ohos.extra.param.key.form\_customize' | 

Custom data.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| FORM\_RENDERING\_MODE\_KEY11+ | 'ohos.extra.param.key.form\_rendering\_mode' | 

Widget rendering mode.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| HOST\_BG\_INVERSE\_COLOR\_KEY12+ | 'ohos.extra.param.key.host\_bg\_inverse\_color' | 

Inverse background color of the widget client.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| FORM\_LOCATION\_KEY12+ | 'ohos.extra.param.key.form\_location' | 

Widget location.

OTHER -1 (other locations)

DESKTOP 0 (home screen)

FORM\_CENTER 1 (widget center of the home screen)

FORM\_MANAGER 2 (widget manager of the home screen)

NEGATIVE\_SCREEN 3 (HUAWEI Assistant·TODAY)

FORM\_CENTER\_NEGATIVE\_SCREEN 4 (widget center of HUAWEI Assistant·TODAY)

FORM\_MANAGER\_NEGATIVE\_SCREEN 5 (widget manager of HUAWEI Assistant·TODAY)

SCREEN\_LOCK 6 (screen lock)

AI\_SUGGESTION 7 (AI Suggestions)

 |
| FORM\_PERMISSION\_NAME\_KEY12+ | 'ohos.extra.param.key.permission\_name' | 

Name of the permission.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| FORM\_PERMISSION\_GRANTED\_KEY12+ | 'ohos.extra.param.key.permission\_granted' | 

Whether the permission is granted.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| ORIGINAL\_FORM\_KEY20+ | 'ohos.extra.param.key.original\_form\_id' | 

Original widget ID. When a group of widgets associated by **groupId** is resized, new-sized widgets are created before old-sized widgets are deleted. When a new-sized widget is created, the old-sized widget ID is passed through this key in the **want** parameter.

**Atomic service API**: This API can be used in atomic services since API version 20.

 |
| EDIT\_FORM\_KEY22+ | 'ohos.extra.param.key.edit\_form\_id' | 

ID of the edited widget. In the widget editing of the semi-modal page, this key is passed through the **onAddForm** callback to indicate the ID of the edited widget, ensuring that the preview widget and the edited widget are synchronized. If the **onAddForm** callback of the widget carries this key, the widget is a preview widget in the semi-modal page, and the content of the preview widget needs to be filtered based on the edited widget.

**Atomic service API**: This API can be used in atomic services since API version 22.

 |

#### FormDimension

Enumerates the widget dimensions.

**System capability**: SystemCapability.Ability.Form

| Name | Value | Description |
| :-- | :-- | :-- |
| Dimension\_1\_2 | 1 | 
1 x 2.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| Dimension\_2\_2 | 2 | 

2 x 2.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| Dimension\_2\_4 | 3 | 

2 x 4.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| Dimension\_4\_4 | 4 | 

4 x 4.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| Dimension\_2\_1(deprecated) | 5 | 

2 x 1.

**Atomic service API**: This API can be used in atomic services since API version 11.

**Note**: This field is supported since API version 9 and deprecated since API version 20.

 |
| DIMENSION\_1\_111+ | 6 | 

1 x 1.

**Atomic service API**: This API can be used in atomic services since API version 11.

**Note**: This dimension takes effect only on lock screen widgets.

 |
| DIMENSION\_6\_412+ | 7 | 

6 x 4.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| DIMENSION\_2\_318+ | 8 | 

2 x 3.

**Atomic service API**: This API can be used in atomic services since API version 18.

**Device behavior differences**: This field takes effect only on wearables.

 |
| DIMENSION\_3\_318+ | 9 | 

3 x 3.

**Atomic service API**: This API can be used in atomic services since API version 18.

**Device behavior differences**: This field takes effect only on wearables.

 |

#### FormShape12+

Enumerates the widget shapes.

**System capability**: SystemCapability.Ability.Form

| Name | Value | Description |
| :-- | :-- | :-- |
| RECT | 1 | 
Rectangle.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| CIRCLE | 2 | 

Circle.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |

#### FormInfoFilter

Defines the widget information filter. Only the widget information that meets the filter is returned.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Ability.Form

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| moduleName | string | No | Yes | 
Only the information about the widget whose **moduleName** is the same as the provided value is returned.

If this parameter is not set, **moduleName** is not used for filtering.

 |

#### VisibilityType

Enumerates the visibility types of the widget.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Ability.Form

| Name | Value | Description |
| :-- | :-- | :-- |
| UNKNOWN10+ | 0 | The visibility type of the widget is unknown. |
| FORM\_VISIBLE | 1 | The widget is visible. |
| FORM\_INVISIBLE | 2 | The widget is invisible. |

#### LaunchReason10+

Enumerates the reasons for creating a widget.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Ability.Form

| Name | Value | Description |
| :-- | :-- | :-- |
| FORM\_DEFAULT | 1 | The widget is created by default. |
| FORM\_SHARE | 2 | The widget is created for sharing. |
| FORM\_SIZE\_CHANGE20+ | 3 | 
The widget is created due to dimension changes.

**Atomic service API**: This API can be used in atomic services since API version 20.

 |

#### OverflowInfo20+

Describes the widget animation information.

**Atomic service API**: This API can be used in atomic services since API version 20.

**System capability**: SystemCapability.Ability.Form

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| area | [Rect](#rect20) | No | No | Overflow animation area. The upper-left corner of the widget is used as the origin, in vp. |
| duration | number | No | No | Animation duration, in ms. The value is an integer greater than 0, and the value cannot exceed 3500. |
| useDefaultAnimation | boolean | No | Yes | 
Whether to enable the default animation provided by the system when the interactive widget state is switched. The default value is **true**.

\- **true**: enable the system-provided default transition animation.

\- **false**: disable the system-provided default transition animation. The widget state switches directly with no animation applied, which is applicable for scenarios where the widget UI is identical in both inactive and active states during switching.

 |

#### Rect20+

Defines the common rectangular area information, including the widget position and animation area.

**Atomic service API**: This API can be used in atomic services since API version 20.

**System capability**: SystemCapability.Ability.Form

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| left | number | No | No | X coordinate of the upper left vertex of the rectangle, in vp. |
| top | number | No | No | Y coordinate of the upper left vertex of the rectangle, in vp. |
| width | number | No | No | Width of the rectangle, in vp. |
| height | number | No | No | Height of the rectangle, in vp. |

#### FormLocation20+

Enumerates the widget locations.

**Atomic service API**: This API can be used in atomic services since API version 20.

**System capability**: SystemCapability.Ability.Form

| Name | Value | Description |
| :-- | :-- | :-- |
| DESKTOP | 0 | The widget is located on the home screen. |
| FORM\_CENTER | 1 | The widget is located in the widget center of the home screen. |
| FORM\_MANAGER | 2 | The widget is located in the Widget Manager of the home screen. |
| NEGATIVE\_SCREEN | 3 | The widget is located on the minus 1 screen. |
| SCREEN\_LOCK | 6 | The widget is located on the lock screen. |
| AI\_SUGGESTION | 7 | The widget is located in the area of Celia Suggestions. |

#### RunningFormInfo20+

Information about the widget that has been added to the home screen.

**Atomic service API**: This API can be used in atomic services since API version 20.

**System capability**: SystemCapability.Ability.Form

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| formId | string | Yes | No | Widget ID. |
| bundleName | string | Yes | No | Name of the bundle to which the widget provider belongs. |
| moduleName | string | Yes | No | Name of the module to which the widget belongs. |
| abilityName | string | Yes | No | Name of the ability to which the widget belongs. |
| formName | string | Yes | No | Widget name. |
| dimension | number | Yes | No | Widget dimension. For details about the values and meanings, see [FormDimension](#formdimension). |
| formLocation | [FormLocation](#formlocation20) | Yes | No | Location of the widget. |
