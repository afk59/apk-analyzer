# Resource

Provides APIs for accessing application and system resources. For details about resource types and usage, see [Resource Categories and Access](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/resource-categories-and-access).

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bc/v3/apHN5Pp2SGSI-VCXA3j3pw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062230Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=49D7445E6B3B6E8E6496CDB7AB001B0E17AFB1A10F2A088BFFCDEAC804F2499F)

The initial APIs of this module are supported since API version 7. Newly added APIs will be marked with a superscript to indicate their earliest API version.

#### $r

$r(value: string, ...params: any\[\]): Resource

Accesses application or system resources. During compilation, the toolchain converts $r into a [Resource](../../../../../localization-kit/arkts-apis/ohos-resourcemanager-resource-management/document.md#resource9) object. For details about how to access application or system resources using $r, see [Resource Categories and Access](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/resource-categories-and-access).

**Widget capability**: This API can be used in ArkTS widgets since API version 9.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | string | Yes | 
Resource identifier in the format belonging.type.name.

**belonging**: resource source. Values: **sys**, **app**, or **\[hsp\_name\]**.

**type**: resource type. Values: **boolean**, **color**, **float**, **intarray**, **integer**, **pattern**, **plural**, **strarray**, **string**, or **media**.

**name**: resource name. Application resource names are defined in the project's **resources** directory. For details about system resource names, see [Resource Categories and Access](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/resource-categories-and-access).

 |
| ...params | any\[\] | No | Additional parameters passed by you. |

**Return value**

| Type | Description |
| :-- | :-- |
| [Resource](../../../../../localization-kit/arkts-apis/ohos-resourcemanager-resource-management/document.md#resource9) | Resource object containing the package name, module name, resource ID, and more. |

**Example**

@Entry
@Component
struct Page {
  build() {
    Row() {
      Column() {
        Text($r('app.string.app\_name'))
      }
      .width('100%')
    }
    .height('100%')
  }
}

For details about how to access HSP resources, see [Cross-HAP/HSP Resources](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/resource-categories-and-access#cross-haphsp-resources).

#### $rawfile

$rawfile(value: string): Resource

Accesses resources in the **rawfile** directory of the project. During compilation, the toolchain converts $rawfile into a [Resource](../../../../../localization-kit/arkts-apis/ohos-resourcemanager-resource-management/document.md#resource9) object. For details about how to access application or system resources using $rawfile, see [Resource Categories and Access](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/resource-categories-and-access).

**Widget capability**: This API can be used in ArkTS widgets since API version 9.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | string | Yes | Relative path in the **rawfile** directory. The file name must contain an extension, and the path cannot start with a slash (/). |

**Return value**

| Type | Description |
| :-- | :-- |
| [Resource](../../../../../localization-kit/arkts-apis/ohos-resourcemanager-resource-management/document.md#resource9) | Resource object containing the package name, module name, resource ID, and more. |

// Add startIcon.png to the src/main/resources/rawfile directory.

@Entry
@Component
struct Page {
  build() {
    Row() {
      Column() {
        Image($rawfile("startIcon.png"))
      }
      .width('100%')
    }
    .height('100%')
  }
}

For details about how to access HSP resources, see [Cross-HAP/HSP Resources](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/resource-categories-and-access#cross-haphsp-resources).
