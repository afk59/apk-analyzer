# How do I implement cross-file component reuse?

In application development, you may need to use the same functionality and styles for ArkUI components across different files. For example, you might use the same style for **Button** components or **Text** components across multiple pages, such as in a shopping application. To reduce redundancy, a common practice is to extract shared styles or encapsulate them into custom components and add them to a common component library.

If you need to combine multiple built-in components, such as **Image** and **Text** in a composite custom component, use a cross-file component reuse solution

by performing the following steps:

1\. The provider creates a custom component **ImageText** in the **CommonText** library, which supports an external **attributeModifier**.

// Set Image width & height
export class ImageModifier implements AttributeModifier<ImageAttribute> {
  width: number = 60;
  height: number = 60;

  constructor(width: number, height: number) {
    this.width = width;
    this.height = height
  }

  applyNormalAttribute(instance: ImageAttribute): void {
    instance.width(this.width);
    instance.height(this.height);
  }
}

/\*
  Custom class implementation of the AttributeModifier interface for text, used for initialization
\*/
// Set Text textSize
export class TextModifier implements AttributeModifier<TextAttribute> {
  textSize: number = 12;

  constructor(textSize: number) {
    this.textSize = textSize;
  }

  applyNormalAttribute(instance: TextAttribute): void {
    instance.fontSize(this.textSize);
    instance.fontColor(Color.Orange);
    instance.textAlign(TextAlign.Center);
    instance.border({ width: 1, color: Color.Orange, style: BorderStyle.Solid });
    instance.margin({ right: 10 });
  }
}

/\*
  Customize class to implement the AttributeModifier interface for the checkbox, used for initialization
\*/
export class CheckboxModifier implements AttributeModifier<CheckboxAttribute> {
  size: number = 15;

  constructor(size: number) {
    if (size < 0) {
      size = 15;
    }
    this.size = size;
  }

  applyNormalAttribute(instance: CheckboxAttribute): void {
    instance.width(this.size);
    instance.height(this.size);
  }
}

/\*\*
 \* Customize encapsulated graphic and text components
 \*/
@Component
export struct ImageText {
  @State textContent: string | Resource = 'default';
  @State imageSrc: PixelMap | ResourceStr | DrawableDescriptor = $r('app.media.icon');
  //Accept externally passed AttributeModifier class instances, which can customize only some components and selectively pass parameters.
  @State textModifier: AttributeModifier<TextAttribute> = new TextModifier(12);
  @State imageModifier: AttributeModifier<ImageAttribute> = new ImageModifier(60, 60);
  @State checkboxModifier: AttributeModifier<CheckboxAttribute> = new CheckboxModifier(15);

  build() {
    Row() {
      Checkbox()
        .attributeModifier(this.checkboxModifier)

      Image(this.imageSrc)
        .attributeModifier(this.imageModifier)
        .margin({ right: 10 })

      Text(this.textContent)
        .attributeModifier(this.textModifier)
        .fontColor(Color.Orange)
    }
    .padding({ top: 5 })
    .margin({ right: 10, bottom: 15 })
    .width(200)
    .height(100)
  }
}

2\. The user implements the **AttributeModifier** API for the **Image**, **Text**, and **Checkbox** components, and then uses the custom **ImageText** component and parameters to achieve cross-file component reuse.

import { ImageText, ImageModifier, TextModifier, CheckboxModifier } from './CommonText';

@Entry
@Component
struct Details {
  // User creates an AttributeModifier implementation class instance for the provider
  @State textOne: TextModifier = new TextModifier(36);
  @State imageModifier: ImageModifier = new ImageModifier(100, 100);
  @State checkboxModifier: CheckboxModifier = new CheckboxModifier(20);

  build(){
    Row(){
      ImageText({
        textOne: this.textOne,
        imageModifier: this.imageModifier,
        imageSrc: $r('app.media.icon'),
        checkboxModifier: this.checkboxModifier,
        textOneContent: 'hello'
      })
    }
    .width('100%')
    .height('100%')
    .alignItems(VerticalAlign.Center)
    .justifyContent(FlexAlign.Center)
  }
}

**Reference**

[attributeModifier](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-attribute-modifier#attributemodifier)
