# @Entry: Page Entry Declaration

The custom component decorated with @Entry is used as the entry of the UI page.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f1/v3/-hwrrcoHRYCmG2tRH73L8g/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062249Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=1240F3DC2B7D461E882A1D094362CA4484744395723368A65A5F929549F1A8C8)

The initial APIs of this module are supported since API version 7. Newly added APIs will be marked with a superscript to indicate their earliest API version.

#### @Entry

A single page can only have one @Entry decorated custom component serving as its entry.

**Widget capability**: This API can be used in ArkTS widgets since API version 9.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Example**

@Entry
@Component
struct Index {
  build() {
    Text('@Entry Test')
  }
}

#### EntryOptions10+

Describes the named route options.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| routeName | string | No | Yes | 
Name of the target named route.

**Widget capability**: This API can be used in ArkTS widgets since API version 10.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| storage | [LocalStorage](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/arkts-localstorage) | No | Yes | 

Stores page-level UI status. If no value is passed, the framework creates a new **LocalStorage** instance as the default value.

**Widget capability**: This API can be used in ArkTS widgets since API version 10.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| useSharedStorage12+ | boolean | No | Yes | 

Whether to use the **LocalStorage** instance passed by [loadContent](../../../../arkts-api/window-manager/ohos-window-window/interface-windowstage/document.md#loadcontent9). The default value is **false**. **true**: Use the shared **LocalStorage** instance. **false**: Do not use the shared **LocalStorage** instance.

**Widget capability**: This API can be used in ArkTS widgets since API version 12.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |

**Example**

@Entry({ routeName: 'myPage' })
@Component
struct Index {
  build() {
    Text('Index')
  }
}
