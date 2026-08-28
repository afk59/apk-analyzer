# Reuse Options

The **reuse** attribute is used to specify reuse options for custom components decorated with @ReusableV2.

This document is solely for API reference. For details about the usage guidelines and constraints, see [@ReusableV2 Decorator: Reusing V2 Components](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/arkts-new-reusablev2).

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fd/v3/hnXPgouVRhOURVzTzwiKTQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062236Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=705D839C0C758260B4BC0BBCEA30C1C30CAF6E437FC8B38F87FD4492F895D212)

The initial APIs of this module are supported since API version 18. Newly added APIs will be marked with a superscript to indicate their earliest API version.

#### reuse

reuse(options: ReuseOptions): T

Sets the reuse options for custom components decorated with @ReusableV2.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ef/v3/C-W-srViRG6CmhMEiXH2hw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062236Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=32E6C14536FDD834F406F658F81F4587F855FEFFDC8A3BCA4A760025E959C28C)

This API cannot be called within [attributeModifier](../../modifiers-and-custom-property/attribute-modifier/document.md#attributemodifier).

**Atomic service API**: This API can be used in atomic services since API version 18.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| options | [ReuseOptions](#reuseoptions) | Yes | Custom reuse configuration. |

**Return value**

| Type | Description |
| :-- | :-- |
| T | Current component. |

#### ReuseOptions

Defines the reuse options.

#### \[h2\]Properties

**Atomic service API**: This API can be used in atomic services since API version 18.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| reuseId | [ReuseIdCallback](#reuseidcallback) | No | Yes | Reuse ID. Components with same **reuseId** will be mutually reused. The default reuse ID is the component name. |

#### ReuseIdCallback

type ReuseIdCallback = () => string

Defines the callback used to obtain the reuse ID.

**Atomic service API**: This API can be used in atomic services since API version 18.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Return value**

| Type | Description |
| :-- | :-- |
| string | 
Developer-specified reuse ID.

It uses the component name if unspecified or if an empty string **''** is provided.

 |

#### Example

@Entry
@ComponentV2
struct Index {
  build() {
    Column() {
      ReusableV2Component()
        .reuse({reuseId: () => 'reuseComponent'}) // Use 'reuseComponent' as reuseId.
      ReusableV2Component()
        .reuse({reuseId: () => ''}) // If an empty string is used, the component name 'ReusableV2Component' is used as reuseId.
      ReusableV2Component() // If reuseId is not specified, the component name 'ReusableV2Component' is used as reuseId.
    }
  }
}
@ReusableV2
@ComponentV2
struct ReusableV2Component {
  build() {
  }
}
