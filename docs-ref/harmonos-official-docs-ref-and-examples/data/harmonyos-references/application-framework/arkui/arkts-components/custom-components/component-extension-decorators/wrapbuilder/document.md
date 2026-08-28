# wrapBuilder

The **wrapBuilder** function encapsulates global @Builder functions to improve code maintainability. For details, see [wrapBuilder: Encapsulating Global @Builder](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/arkts-wrapbuilder).

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/83/v3/Z6ENAqmUSjOSg98rYcuhOQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062249Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=796859392C0C6CD62BA169E77527975D53584298C14D76530B4E07F821D928C8)

The initial APIs of this module are supported since API version 11.

Newly added APIs will be marked with a superscript to indicate their earliest API version.

#### wrapBuilder

wrapBuilder<Args extends Object\[\]>(builder: (...args: Args) => void): WrappedBuilder<Args>

A template function that returns a **WrappedBuilder** object. The template parameter **Args extends Object\[\]** represents the parameter list of the builder function to be encapsulated.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| builder | (...args: Args) => void | Yes | Global function decorated with @Builder. |

**Return value**

| Type | Description |
| :-- | :-- |
| [WrappedBuilder<Args>](#wrappedbuilder) | **WrappedBuilder** object. |

**Example**

@Builder
function MyBuilder(value: string, size: number) {
  Text(value)
    .fontSize(size)
}
let builderVar: WrappedBuilder<\[string, number\]> = wrapBuilder(MyBuilder);

#### WrappedBuilder

Implements the encapsulation class for @Builder functions. The template parameter **Args extends Object\[\]** must match the parameter type list of the @Builder function.

#### \[h2\]Properties

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| builder | (...args: Args) => void | No | No | Global function decorated with @Builder. |

#### \[h2\]constructor

constructor(builder: (...args: Args) => void)

A constructor used to create a **WrappedBuilder** instance.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| builder | (...args: Args) => void | Yes | Global function decorated with @Builder. |

**Example**

@Builder
function MyBuilder(value: string, size: number) {
  Text(value)
    .fontSize(size)
}
let builderVar: WrappedBuilder<\[string, number\]> = new WrappedBuilder<\[string, number\]>(MyBuilder);
