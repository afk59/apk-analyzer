# Types

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/35/v3/o_rY4f69Q--xMjO_7QOcpw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062443Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=9A6A270A0B05418D6CA25625D974EFB025F5A19009D5C2A1A0D1509846D3F08C)

The initial APIs of this module are supported since API version 10. Newly added APIs will be marked with a superscript to indicate their earliest API version.

#### MemberType

type MemberType = number | string | boolean

Defines the types of the PhotoAsset members.

The member types are the union of the types listed in the following table.

**System capability**: SystemCapability.FileManagement.PhotoAccessHelper.Core

| Type | Description |
| :-- | :-- |
| number | The member value is any number. |
| string | The member value is any string. |
| boolean | The member value is true or false. |

#### PhotoAssetParams21+

type PhotoAssetParams = Record<string, MemberType>\[\]

Defines the array of record types that map file property names to their values.

**System capability**: SystemCapability.FileManagement.PhotoAccessHelper.Core

| Type | Description |
| :-- | :-- |
| Record<string, [MemberType](#membertype)\>\[\] | Array of record types that map file property names to their values. |

#### OperationValueType22+

type OperationValueType = number | string | boolean

Defines the values needed for matching different predicates.

**Model restriction**: This API can be used only in the stage model.

**Atomic service API**: This API can be used in atomic services since API version 22.

**System capability**: SystemCapability.FileManagement.PhotoAccessHelper.Core

| Type | Description |
| :-- | :-- |
| number | Used for numeric fields. It can be any value. |
| string | Used for string fields. It can be any value. |
| boolean | Used for boolean fields. |
