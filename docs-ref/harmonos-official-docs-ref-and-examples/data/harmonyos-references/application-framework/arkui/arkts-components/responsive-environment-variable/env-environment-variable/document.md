# @Env: Environment Variable

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a1/v3/0KGyG3YWQUi9iefzrw69sQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062252Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=ADF4433AE18FCB1491CF5D74F5E76714DEDAE6DF0CA3BA1CC9790663B9C9A463)

The initial APIs of this module are supported since API version 22. Newly added APIs will be marked with a superscript to indicate their earliest API version.

For details about the developer guide, see [@Env Developer Guide](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/arkts-env-system-property).

#### @Env

Env: EnvDecorator

**Atomic service API**: This API can be used in atomic services since API version 22.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Type | Description |
| :-- | :-- | :-- |
| Env | [EnvDecorator](#envdecorator) | Environment variable decorator. |

**Example**

import { uiObserver } from '@kit.ArkUI';

@Entry
@Component
struct Index {
  @Env(SystemProperties.BREAK\_POINT) breakpoint: uiObserver.WindowSizeLayoutBreakpointInfo;

  build() {}
}

#### EnvDecorator

type EnvDecorator = (value: SystemProperties) => PropertyDecorator

Defines the @Env decorator type.

**Model restriction**: This API can be used only in the stage model.

**Atomic service API**: This API can be used in atomic services since API version 22.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | [SystemProperties](#systemproperties) | Yes | Name of the environment variable. |

**Return value**

| Type | Description |
| :-- | :-- |
| PropertyDecorator | Property decorator. |

**Error codes**

For details, see [Environment Variable Error Codes](../../../error-codes/ui/environment-variable-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 140000 | Invalid key for @Env |

#### SystemProperties

Defines the enumerated values of the environment variable.

**Atomic service API**: This API can be used in atomic services since API version 22.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Value | Description |
| :-- | :-- | :-- |
| BREAK\_POINT | 'system.arkui.breakpoint' | 
[@Env](#env) variable parameter. You can obtain the [WindowSizeLayoutBreakpointInfo](../../../arkts-api/ui/ohos-arkui-observer-observer/document.md#windowsizelayoutbreakpointinfo22) instance through @Env(SystemProperties.BREAK\_POINT).

When this decorator is declared in [@Component](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/arkts-create-custom-components#component) or [@ComponentV2](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/arkts-create-custom-components#componentv2), it is used to obtain the size layout breakpoint information of the window where the current custom component is located.

 |
