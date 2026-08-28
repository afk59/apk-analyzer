# Reuse ID

**reuseId** is an ID that identifies the reuse group of a custom component. The reuse framework identifies and groups reusable custom components based on their reuse IDs.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b6/v3/H6lyzm6GQ3mFnssolBGUPg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062236Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=6B353D5BEF032DB70B19566F53457A11A036789A8511792316386C224878C480)

The initial APIs of this module are supported since API version 10. Newly added APIs will be marked with a superscript to indicate their earliest API version.

#### reuseId

reuseId(id: string): T

Sets the ID that identifies the reuse group of the component.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/38/v3/3FlF2THHSXarbjfh8yc-sQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062236Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=687DAE36D9111968E9FB28EC65CB8AB265C4180BB7F3C211E28D6CE7847E68F2)

-   Set **reuseId** flexibly based on different scenarios to achieve optimal reuse effects. For best practices, see [Using reuseId to Mark Components with Layout Changes](https://developer.huawei.com/consumer/en/doc/best-practices/bpta-component-reuse#section1239555818211).
    
-   This API cannot be called within [attributeModifier](../../modifiers-and-custom-property/attribute-modifier/document.md#attributemodifier).
    

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| id | string | Yes | ID that identifies the reuse group of the component. |

**Return value**

| Type | Description |
| :-- | :-- |
| T | Current component. |

#### Example

This example demonstrates how to use **reuseId** to identify the reuse group of a custom component.

// xxx.ets
@Entry
@Component
struct MyComponent {
  @State switch: boolean = true;
  private type: string = "type1";

  build() {
    Column() {
      Button("ChangeType")
        .onClick(() => {
          this.type = "type2"
        })
      Button("Switch")
        .onClick(() => {
          this.switch = !this.switch
        })
      if (this.switch) {
        ReusableChildComponent({ type: this.type })
          .reuseId(this.type)
      }
    }
    .width('100%')
    .height('100%')
  }
}

@Reusable
@Component
struct ReusableChildComponent {
  @State type: string = ''

  aboutToAppear() {
    console.info(\`ReusableChildComponent Appear ${this.type}\`)
  }

  aboutToReuse(params: ESObject) {
    console.info(\`ReusableChildComponent Reuse ${this.type}\`)
    this.type = params.type;
  }

  build() {
    Row() {
      Text(this.type)
        .fontSize(20)
        .margin({ left: 10 })
    }.margin({ left: 10, right: 10 })
  }
}
