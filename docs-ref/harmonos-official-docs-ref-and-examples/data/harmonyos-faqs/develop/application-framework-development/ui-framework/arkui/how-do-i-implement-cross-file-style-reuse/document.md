# How do I implement cross-file style reuse?

In application development, you may need to use the same functionality and styles for ArkUI components across different files. For example, you might use the same style for **Button** components or **Text** components across multiple pages, such as in a shopping application. To reduce redundancy, a common practice is to extract shared styles or encapsulate them into custom components and add them to a common component library.

If you need to provide custom styles for individual components, adopt the cross-file style reuse solution by performing the following steps:

1\. The provider creates the implementation class of the **AttributeModifier** API.

/\*
  Customize class to implement AttributeModifier interface for Text
\*/
export class CommodityText implements AttributeModifier<TextAttribute> {
  textType: TextType = TextType.TYPE\_ONE;
  textSize: number = 15;

  constructor( textType: TextType, textSize: number) {
    this.textType = textType;
    this.textSize = textSize;
  }

  applyNormalAttribute(instance: TextAttribute): void {
    if (typeof this.textSize !== 'number' || this.textSize <= 0) {
      throw new Error('Invalid textSize')
    }

    if (this.textType === TextType.TYPE\_ONE) {
      instance.fontSize(this.textSize);
      instance.fontColor(Color.Orange);
      instance.fontWeight(FontWeight.Bolder);
      instance.width(200);
    } else if (this.textType === TextType.TYPE\_TWO) {
      instance.fontSize(this.textSize);
      instance.fontWeight(FontWeight.Bold);
      instance.fontColor(Color.Blue);
      instance.width(200);
    } else if (this.textType === TextType.TYPE\_THREE) {
      instance.fontColor(Color.Gray);
      instance.fontSize(this.textSize);
      instance.fontWeight(FontWeight.Normal);
      instance.width(200);
    } else if (this.textType === TextType.TYPE\_FOUR) {
      instance.fontSize(this.textSize);
      instance.fontColor(Color.Orange);
      instance.textAlign(TextAlign.Center);
      instance.border({ width: 1, color: Color.Orange, style: BorderStyle.Solid });
      instance.margin({ right: 10 });
    } else {
     console.log(\`TYPE is ${this.textType}\`);
    }
  }
}
/\*
 \*  Enumerate text types
 \*/
export enum TextType {
  TYPE\_ONE,
  TYPE\_TWO,
  TYPE\_THREE,
  TYPE\_FOUR
}

2\. The user creates an instance of the provider's **AttributeModifier** implementation class and passes it as a parameter of the **attributeModifier** attribute method to the system component.

import { CommodityText, TextType } from './attributeModifier';

@Entry
@Component
export struct Details {
  // User creates an AttributeModifier implementation class instance for the provider
  @State textOne: CommodityText = new CommodityText(TextType.TYPE\_FOUR, 15);

  build(){
    Row(){
      Text($r('app.string.app\_name'))
        .attributeModifier(this.textOne)
        .textAlign(TextAlign.Center)
    }
    .width('100%')
    .height('100%')
    .alignItems(VerticalAlign.Center)
    .justifyContent(FlexAlign.Center)
  }
}

**Reference**

[attributeModifier](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-attribute-modifier#attributemodifier)
