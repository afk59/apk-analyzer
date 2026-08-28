# FAQs About Buttons and Selection Components

This topic addresses frequently asked questions regarding buttons and selection components.

#### How Are the Slider Thumb and Track of the Slider Component Aligned?

The **Slider** component supports three display styles defined by [SliderStyle](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ts-basic-components-slider#sliderstyle). Both **SliderStyle.OutSet** and **SliderStyle.InSet** include visible slider thumbs. When the slider progress is at the minimum value, the alignment behavior differs between these two styles:

**SliderStyle.OutSet**: The thumb center aligns with the track endpoint.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fa/v3/8uSorjlQRqKlbjvAj5infg/en-us_image_0000002568684697.jpg?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061945Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=36ACE250779563494912A71DB8B3F811CA1AD1068D6912B0BB10DAC1EE91ACD9)

**SliderStyle.InSet**: The slider thumb aligns with the track centerline (midpoint of the track endpoint height).

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6c/v3/67yfvG5USuWA_LowrgYf-w/en-us_image_0000002568764707.jpg?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061945Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=D7667377C22F6F397F52B80CF09187A2C9DD37B14ACBA96C74436E62572CC8F6)

**Example**

@Entry
@Component
struct Index {
  build() {
    Column() {
      Slider({
        style: SliderStyle.OutSet
      })
        .blockSize({
          width: 20,
          height: 20
        })
        .trackThickness(50)
      Slider({
        style: SliderStyle.InSet
      })
        .blockSize({
          width: 20,
          height: 20
        })
        .trackThickness(50)
    }
    .height('100%')
    .width('100%')
  }
}

#### Inconsistent Default Font Weight When AttributeModifier Is Used to Set LabelStyle of a Button

**Symptom**

When **LabelStyle** is set for the **Button** component, the default font weight of the label text is inconsistent in different setting modes.

**Possible Causes**

There are two ways to set **LabelStyle**:

-   Set [LabelStyle](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ts-basic-components-button#labelstyle10) directly. In this case, the default value of the **weight** attribute in **font** is **FontWeight.Medium**, which corresponds to the value **500**.
-   Set **LabelStyle** through the [AttributeModifier](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ts-universal-attributes-attribute-modifier#attributemodifier) API. In this case, the default value of the **weight** attribute in **font** is **400**, which is different from the default value described in the **LabelStyle** description.

**Solution**

To avoid display differences caused by different setting ways, you are advised to explicitly specify the **weight** value when setting **LabelStyle** through the **AttributeModifier** API to ensure that the text style meets the expectation. The following is an example:

// pages/ButtonModifierFAQ.ets
class MyButtonModifier1 implements AttributeModifier<ButtonAttribute> {
  applyNormalAttribute(instance: ButtonAttribute): void {
    instance.labelStyle({});
  }
}

class MyButtonModifier2 implements AttributeModifier<ButtonAttribute> {
  applyNormalAttribute(instance: ButtonAttribute): void {
    instance.labelStyle({
      font: {
        weight: FontWeight.Medium
      }
    });
  }
}

@Entry
@Component
struct Index {
  @State modifier1: MyButtonModifier1 = new MyButtonModifier1();
  @State modifier2: MyButtonModifier2 = new MyButtonModifier2();

  build() {
    Column() {
      Text('normal')
      // Set labelStyle for the Button component. The default value of weight in the font attribute is 500.
      Button('DemoButtonTest')
        .width(100)
        .labelStyle({})
      Divider()
      // Set labelStyle via AttributeModifier. The default value of weight in the font attribute is 400.
      Text('modifier1')
      Button('DemoButtonTest')
        .width(100)
        .attributeModifier(this.modifier1)

      Text('modifier2')
      Button('DemoButtonTest')
        .width(100)
        .attributeModifier(this.modifier2)
    }.height('100%')
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/20/v3/Tb9k_pXORBG3yImx2ZplJg/en-us_image_0000002537764982.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061945Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=AA36D4538480C5D7DB6D1E9E7E068163F573BB17A494768BDC3C0E00B47C4B90)
