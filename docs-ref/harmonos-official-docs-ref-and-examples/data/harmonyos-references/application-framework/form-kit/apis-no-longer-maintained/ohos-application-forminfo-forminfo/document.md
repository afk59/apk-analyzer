# @ohos.application.formInfo (formInfo)

The **formInfo** module provides types and enums related to the widget information and state.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8a/v3/sGgRL72cSOSRaS5CtFxHEw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062323Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=1F402645C132CEDF24A6C7B65C9D89522EE18F7A5BFB67CED575677BB53C059C)

-   The initial APIs of this module are supported since API version 8. Newly added APIs will be marked with a superscript to indicate their earliest API version.
-   This module is deprecated since API version 9. You are advised to use [formInfo](../../arkts-apis/ohos-app-form-forminfo-forminfo/document.md) instead.

#### Modules to Import

import { formInfo } from '@kit.FormKit';

#### FormInfo

Widget information.

**System capability**: SystemCapability.Ability.Form

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| bundleName | string | No | No | Name of the bundle to which the widget belongs. |
| moduleName | string | No | No | Name of the module to which the widget belongs. |
| abilityName | string | No | No | Name of the ability to which the widget belongs. |
| name | string | No | No | Widget name. |
| description | string | No | No | Description of the widget. |
| type | [FormType](#formtype) | No | No | Type of the widget. Currently, only JS widgets are supported. |
| jsComponentName | string | No | No | Component name of the JS widget. |
| colorMode | [ColorMode](#colormode) | No | No | Color mode of the widget. |
| isDefault | boolean | No | No | 
Whether the widget is the default one.

\- **true**: The widget is the default one.

\- **false**: The widget is not the default one.

 |
| updateEnabled | boolean | No | No | 

Whether the widget is updatable.

\- **true**: The widget can be updated periodically.

\- **false**: The widget cannot be updated periodically.

 |
| formVisibleNotify | boolean | No | No | 

Whether to send a notification when the widget is visible.

\- **true**: The widget provider is notified of the status change.

\- **false**: The widget provider is not notified of the status change.

 |
| relatedBundleName | string | No | No | Name of the associated bundle to which the widget belongs. |
| scheduledUpdateTime | string | No | No | Time when the widget was updated. |
| formConfigAbility | string | No | No | Configuration ability of the widget. |
| updateDuration | number | No | No | Update period of the widget. |
| defaultDimension | number | No | No | Default dimension of the widget. |
| supportDimensions | Array<number> | No | No | Dimensions supported by the widget. |
| customizeData | {\[key: string\]: \[value: string\]} | No | No | Custom data of the widget. |

#### FormType

Enumerates the widget types.

**System capability**: SystemCapability.Ability.Form

| Name | Value | Description |
| :-- | :-- | :-- |
| JS | 1 | JS widget. |

#### ColorMode

Enumerates the color modes supported by the widget.

**System capability**: SystemCapability.Ability.Form

| Name | Value | Description |
| :-- | :-- | :-- |
| MODE\_AUTO | \-1 | Auto mode. |
| MODE\_DARK | 0 | Dark mode. |
| MODE\_LIGHT | 1 | Light mode. |

#### FormStateInfo

Describes the widget state information.

**System capability**: SystemCapability.Ability.Form

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| formState | [FormState](#formstate) | No | No | Widget state. |
| want | [Want](../../../ability-kit/arkts-apis/both-models-recommended/ohos-app-ability-want-want/document.md) | No | No | Want text. |

#### FormState

Enumerates the widget states.

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
| DIMENSION\_KEY | 'ohos.extra.param.key.form\_dimension' | Widget dimension. |
| NAME\_KEY | 'ohos.extra.param.key.form\_name' | Widget name. |
| MODULE\_NAME\_KEY | 'ohos.extra.param.key.module\_name' | Name of the module to which the widget belongs. |
| WIDTH\_KEY | 'ohos.extra.param.key.form\_width' | Widget width. |
| HEIGHT\_KEY | 'ohos.extra.param.key.form\_height' | Widget height. |
| TEMPORARY\_KEY | 'ohos.extra.param.key.form\_temporary' | Temporary widget. |
