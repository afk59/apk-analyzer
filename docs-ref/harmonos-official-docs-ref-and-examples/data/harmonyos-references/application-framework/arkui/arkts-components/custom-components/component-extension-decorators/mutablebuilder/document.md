# mutableBuilder

Use **mutableBuilder** to wrap a global @Builder function and enable dynamic switching between different global @Builder functions. For details about the development guide, see [mutableBuilder: Implementing Dynamic Update of Global @Builder](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/arkts-mutablebuilder).

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/63/v3/aEnGpyefQlyikipq3xTFvQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062249Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=D91FE8C46B4F12134634F1383BC9798F56AF698DCAB6C245BCE86C3D6CD5D1BB)

The initial APIs of this module are supported since API version 22.

Newly added APIs will be marked with a superscript to indicate their earliest API version.

#### mutableBuilder

mutableBuilder<Args extends Object\[\]>(builder: BuilderCallback): MutableBuilder<Args>

**mutableBuilder** is a template function. It returns a **MutableBuilder** object and accepts only a single global @Builder function as its parameter.

In the returned [MutableBuilder](#mutablebuilder-1) object, the builder attribute method can be used only inside custom components.

**Atomic service API**: This API can be used in atomic services since API version 22.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| builder | [BuilderCallback](#buildercallback) | Yes | Global function decorated with @Builder. |

**Return value**

| Type | Description |
| :-- | :-- |
| [MutableBuilder<Args>](#mutablebuilder-1) | Instance of the MutableBuilder<Args&gt class, which is used for assignment and passing of wrapped [global @Builder functions](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/arkts-builder#global-custom-builder-function) and enables dynamic updates of the global @Builder. |

**Example**

class TextContent {
  text: string = '';
}

@Builder
function textBuilder(p: TextContent) {
  Text(p.text).margin(20)
}

@Builder
function buttonBuilder(p: TextContent) {
  Button(p.text).margin(20)
}

let counter: number = 1;
@Entry
@ComponentV2
struct MyApp {
  @Local message: string = 'init';
  @Local switchingBuilder: MutableBuilder<\[TextContent\]> = mutableBuilder(textBuilder);
  build() {
    Column() {
      this.switchingBuilder.builder({ text: this.message })
      Button('Click to change')
      .onClick(() => {
        counter++; // Increment the counter on each button click to dynamically switch the global @Builder.
        if(counter % 2 === 0) {
          this.message += 'B';
          this.switchingBuilder = mutableBuilder(buttonBuilder); // textBuilder--->buttonBuilder
        } else {
          this.message += 'T';
          this.switchingBuilder = mutableBuilder(textBuilder); // buttonBuilder--->textBuilder
        }
      })
    }.position({x: 120, y: 60})
  }
}

#### MutableBuilder

class MutableBuilder<Args extends Object\[\]> extends WrappedBuilder<Args> { }

Represents the class used to dynamically switch the wrapped [global @Builder](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/arkts-builder#global-custom-builder-function). **MutableBuilder** inherits from [WrappedBuilder](../wrapbuilder/document.md). The template parameter **Args extends Object\[\]** corresponds to the parameter list of the @Builder function. The [mutableBuilder](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/arkts-mutablebuilder) function returns a **MutableBuilder** object.

**Atomic service API**: This API can be used in atomic services since API version 22.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

#### BuilderCallback

type BuilderCallback = (...args: Args) => void

Defines the input parameter type for the **mutableBuilder** function, representing a global @Builder function.

**Atomic service API**: This API can be used in atomic services since API version 22.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| ...args | Args | No | Input parameters of the global @Builder function. **Args** indicates that the function can accept any number of parameters. |

**Example**

@Builder
function MyBuilder(value: string, size: number) {
  Text(value)
    .fontSize(size)
}
let builderVar: MutableBuilder<\[string, number\]> = mutableBuilder(MyBuilder); // Declare builderVar as type MutableBuilder.
