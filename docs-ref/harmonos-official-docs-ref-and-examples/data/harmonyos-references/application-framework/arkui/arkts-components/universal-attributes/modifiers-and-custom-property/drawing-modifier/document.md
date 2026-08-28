# Drawing Modifier

If the drawn content of some components does not meet the requirements, you can use the custom drawing features to draw part or all of the components to achieve the expected effect. For example, you can create buttons in special shapes or icons that mix text and imagery. The drawing modifier offers higher flexibility in your custom drawing.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fe/v3/-hBmV2zxSP26MsP-yNTRPw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062236Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=039F934BBDA945C36E97D30078BC4D15F40F3A97170B5FBC8697ABE8B18B797F)

The initial APIs of this module are supported since API version 12. Updates will be marked with a superscript to indicate their earliest API version.

#### drawModifier

drawModifier(modifier: DrawModifier | undefined): T

Creates a drawing modifier.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a3/v3/l526PZZzTCC6WvAfPrdKJg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062236Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=71BC85E6522384C66569C656B42DB559F77A8938316696903B682302C973168A)

This API cannot be called within [attributeModifier](../attribute-modifier/document.md#attributemodifier).

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Supported components:**

[AlphabetIndexer](../../../information-display/alphabetindexer/document.md), [Badge](../../../information-display/badge/document.md), [Blank](../../../blank-and-divider/blank/document.md), [Button](../../../buttons-and-selections/button/document.md), [CalendarPicker](../../../buttons-and-selections/calendarpicker/document.md), [Checkbox](../../../buttons-and-selections/checkbox/document.md), [CheckboxGroup](../../../buttons-and-selections/checkboxgroup/document.md), [Circle](../../../graphic-drawing/circle/document.md), [Column](../../../rows-columns-and-stacking/column/document.md), [ColumnSplit](../../../grid-and-column-layout/columnsplit/document.md), [Counter](../../../information-display/counter/document.md), [DataPanel](../../../information-display/datapanel/document.md), [DatePicker](../../../buttons-and-selections/datepicker/document.md), [Ellipse](../../../graphic-drawing/ellipse/document.md), [Flex](../../../rows-columns-and-stacking/flex/document.md), [FlowItem](../../../scroll-and-swipe/flowitem/document.md), [FolderStack](../../../system-preset-ui-component-library/folderstack/document.md), [FormLink](../../../service-widgets/formlink/document.md), [Gauge](../../../information-display/gauge/document.md), [Grid](../../../scroll-and-swipe/grid/document.md), [GridCol](../../../grid-and-column-layout/gridcol/document.md), [GridItem](../../../scroll-and-swipe/griditem/document.md), [GridRow](../../../grid-and-column-layout/gridrow/document.md), [Hyperlink](../../../text-and-input/hyperlink/document.md), [Image](../../../images-and-videos/image/document.md), [ImageAnimator](../../../images-and-videos/imageanimator/document.md), [ImageSpan](../../../text-and-input/imagespan/document.md), [Line](../../../graphic-drawing/line/document.md), [List](../../../scroll-and-swipe/list/document.md), [ListItem](../../../scroll-and-swipe/listitem/document.md), [ListItemGroup](../../../scroll-and-swipe/listitemgroup/document.md), [LoadingProgress](../../../information-display/loadingprogress/document.md), [Marquee](../../../information-display/marquee/document.md), [Menu](../../../menus/menu/document.md), [MenuItem](../../../menus/menuitem/document.md), [MenuItemGroup](../../../menus/menuitemgroup/document.md), [NavDestination](../../../navigation-and-switching/navdestination/document.md), [Navigation](../../../navigation-and-switching/navigation/document.md), [Navigator](../../../components-and-apis-no-longer-maintained/navigator/document.md), [NavRouter](../../../components-and-apis-no-longer-maintained/navrouter/document.md), [NodeContainer](../../../custom-placeholder-components/nodecontainer/document.md), [Path](../../../graphic-drawing/path/document.md), [PatternLock](../../../information-display/patternlock/document.md), [Polygon](../../../graphic-drawing/polygon/document.md), [Polyline](../../../graphic-drawing/polyline/document.md), [Progress](../../../information-display/progress/document.md), [QRCode](../../../information-display/qrcode/document.md), [Radio](../../../buttons-and-selections/radio/document.md), [Rating](../../../buttons-and-selections/rating/document.md), [Rect](../../../graphic-drawing/rect/document.md), [Refresh](../../../scroll-and-swipe/refresh/document.md), [RelativeContainer](../../../rows-columns-and-stacking/relativecontainer/document.md), [RichEditor](../../../text-and-input/richeditor/document.md), [Row](../../../rows-columns-and-stacking/row/document.md), [RowSplit](../../../grid-and-column-layout/rowsplit/document.md), [Scroll](../../../scroll-and-swipe/scroll/document.md), [ScrollBar](../../../scroll-and-swipe/scrollbar/document.md), [Search](../../../text-and-input/search/document.md), [Select](../../../buttons-and-selections/select/document.md), [Shape](../../../graphic-drawing/shape/document.md), [SideBarContainer](../../../grid-and-column-layout/sidebarcontainer/document.md), [Slider](../../../buttons-and-selections/slider/document.md), [Stack](../../../rows-columns-and-stacking/stack/document.md), [Stepper](../../../components-and-apis-no-longer-maintained/stepper/document.md), [StepperItem](../../../components-and-apis-no-longer-maintained/stepperitem/document.md), [Swiper](../../../scroll-and-swipe/swiper/document.md), [SymbolGlyph](../../../text-and-input/symbolglyph/document.md), [TabContent](../../../navigation-and-switching/tabcontent/document.md), [Tabs](../../../navigation-and-switching/tabs/document.md), [Text](../../../text-and-input/text/document.md), [TextArea](../../../text-and-input/textarea/document.md), [TextClock](../../../information-display/textclock/document.md), [TextInput](../../../text-and-input/textinput/document.md), [TextPicker](../../../buttons-and-selections/textpicker/document.md), [TextTimer](../../../information-display/texttimer/document.md), [TimePicker](../../../buttons-and-selections/timepicker/document.md), [Toggle](../../../buttons-and-selections/toggle/document.md), [WaterFlow](../../../scroll-and-swipe/waterflow/document.md), [XComponent](../../../rendering-drawing/xcomponent/document.md)

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| modifier | [DrawModifier](#drawmodifier-1) | undefined | Yes | 
Custom drawing modifier, which defines the logic of custom drawing.

Default value: **undefined**

**NOTE**

A custom modifier applies only to the [FrameNode](../../../../arkts-api/ui/arkui/framenode/document.md) of the currently bound component, not to its subnodes.

 |

**Return value**

| Type | Description |
| :-- | :-- |
| T | Current component. |

#### DrawModifier

Implements a **DrawModifier** instance for using the **drawForeground**, **drawFront**, **drawContent**, and **drawBehind** APIs for custom drawing as well as the [invalidate](#invalidate) API for redrawing. Each **DrawModifier** instance can be set for only one component. Repeated setting is not allowed.

The figure below shows the custom drawing layers.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e5/v3/jG8HM0g4QtKsdeGyMc6D1w/en-us_image_0000002568685201.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062236Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=5F2B89BFF960AEA9A966BA029172D3B5E8C60E5B4D9888833BC057353DEF2BFA)

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

#### \[h2\]drawFront

drawFront?(drawContext: DrawContext): void

Draws the content foreground. Override this method to implement custom content foreground drawing.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| drawContext | [DrawContext](#drawcontext) | Yes | Graphics drawing context. |

**Example**

See [Example 1: Implementing Custom Drawing Through DrawModifier](#example-1-implementing-custom-drawing-through-drawmodifier).

#### \[h2\]drawContent

drawContent?(drawContext: DrawContext): void

Draws the content. Override this method to implement custom content drawing, which will replace the component's default content drawing function.

Note: The Canvas provided in the [DrawContext](../../../../arkts-api/ui/arkui/graphics/document.md#drawcontext) parameter is a temporary command-recording canvas, not the actual rendering canvas of the node. For usage instructions, see [Adjusting the Transformation Matrix of the Custom Drawing Canvas](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/arkts-user-defined-extension-drawmodifier#adjusting-the-transformation-matrix-of-the-custom-drawing-canvas).

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| drawContext | [DrawContext](#drawcontext) | Yes | Graphics drawing context. |

**Example**

See [Example 1: Implementing Custom Drawing Through DrawModifier](#example-1-implementing-custom-drawing-through-drawmodifier).

#### \[h2\]drawBehind

drawBehind?(drawContext: DrawContext): void

Draws the background. Override this method to implement custom background drawing operations.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| drawContext | [DrawContext](#drawcontext) | Yes | Graphics drawing context. |

**Example**

See [Example 1: Implementing Custom Drawing Through DrawModifier](#example-1-implementing-custom-drawing-through-drawmodifier).

#### \[h2\]drawForeground20+

drawForeground(drawContext: DrawContext): void

Draws the foreground. Override this method to implement custom drawing operations on the foreground layer of the component.

**Atomic service API**: This API can be used in atomic services since API version 20.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| drawContext | [DrawContext](#drawcontext) | Yes | Graphics drawing context. |

**Example**

See [Example 2: Implementing Custom Foreground Drawing for a Container Through DrawModifier](#example-2-implementing-custom-foreground-drawing-for-a-container-through-drawmodifier).

#### \[h2\]invalidate

invalidate(): void

Triggers redrawing of the bound component. No overloading is allowed or needed.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Example**

See [Example 1: Implementing Custom Drawing Through DrawModifier](#example-1-implementing-custom-drawing-through-drawmodifier).

#### \[h2\]DrawContext

type DrawContext = DrawContext

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Type | Description |
| :-- | :-- |
| [DrawContext](../../../../arkts-api/ui/arkui/graphics/document.md#drawcontext) | Graphics drawing context. |

#### Example

## Example 1: Implementing Custom Drawing Through DrawModifier

This example demonstrates how to implement custom drawing for the [Text](../../../text-and-input/text/document.md) component through **DrawModifier**.

// xxx.ets
import { drawing } from '@kit.ArkGraphics2D';
import { AnimatorResult } from '@kit.ArkUI';

// Implement a custom drawing controller by extending DrawModifier.
class MyFullDrawModifier extends DrawModifier {
  public scaleX: number = 1;
  public scaleY: number = 1;
  uiContext: UIContext;

  constructor(uiContext: UIContext) {
    super();
    this.uiContext = uiContext;
  }

  // Override the drawBehind API for custom background drawing.
  drawBehind(context: DrawContext): void {
    const brush = new drawing.Brush();
    brush.setColor({
      alpha: 255,
      red: 255,
      green: 0,
      blue: 0
    });
    context.canvas.attachBrush(brush);
    const halfWidth = context.size.width / 2;
    const halfHeight = context.size.height / 2;
    context.canvas.drawRect({
      left: this.uiContext.vp2px(halfWidth - 50 \* this.scaleX),
      top: this.uiContext.vp2px(halfHeight - 50 \* this.scaleY),
      right: this.uiContext.vp2px(halfWidth + 50 \* this.scaleX),
      bottom: this.uiContext.vp2px(halfHeight + 50 \* this.scaleY)
    });
  }

  // Override the drawContent API for custom content drawing.
  drawContent(context: DrawContext): void {
    const brush = new drawing.Brush();
    brush.setColor({
      alpha: 255,
      red: 0,
      green: 255,
      blue: 0
    });
    context.canvas.attachBrush(brush);
    const halfWidth = context.size.width / 2;
    const halfHeight = context.size.height / 2;
    context.canvas.drawRect({
      left: this.uiContext.vp2px(halfWidth - 30 \* this.scaleX),
      top: this.uiContext.vp2px(halfHeight - 30 \* this.scaleY),
      right: this.uiContext.vp2px(halfWidth + 30 \* this.scaleX),
      bottom: this.uiContext.vp2px(halfHeight + 30 \* this.scaleY)
    });
  }

  // Override the drawFront API for custom foreground drawing.
  drawFront(context: DrawContext): void {
    const brush = new drawing.Brush();
    brush.setColor({
      alpha: 255,
      red: 0,
      green: 0,
      blue: 255
    });
    context.canvas.attachBrush(brush);
    const halfWidth = context.size.width / 2;
    const halfHeight = context.size.height / 2;
    const radiusScale = (this.scaleX + this.scaleY) / 2;
    context.canvas.drawCircle(this.uiContext.vp2px(halfWidth), this.uiContext.vp2px(halfHeight),
      this.uiContext.vp2px(20 \* radiusScale));
  }
}

// Implement a custom drawing controller by extending DrawModifier, supporting only custom foreground drawing.
class MyFrontDrawModifier extends DrawModifier {
  public scaleX: number = 1;
  public scaleY: number = 1;
  uiContext: UIContext;

  constructor(uiContext: UIContext) {
    super();
    this.uiContext = uiContext;
  }

  drawFront(context: DrawContext): void {
    const brush = new drawing.Brush();
    brush.setColor({
      alpha: 255,
      red: 0,
      green: 0,
      blue: 255
    });
    context.canvas.attachBrush(brush);
    const halfWidth = context.size.width / 2;
    const halfHeight = context.size.height / 2;
    const radiusScale = (this.scaleX + this.scaleY) / 2;
    context.canvas.drawCircle(this.uiContext.vp2px(halfWidth), this.uiContext.vp2px(halfHeight),
      this.uiContext.vp2px(20 \* radiusScale));
  }
}

@Entry
@Component
struct DrawModifierExample {
  private fullModifier: MyFullDrawModifier = new MyFullDrawModifier(this.getUIContext());
  private frontModifier: MyFrontDrawModifier = new MyFrontDrawModifier(this.getUIContext());
  private drawAnimator: AnimatorResult | undefined = undefined;
  @State modifier: DrawModifier = new MyFrontDrawModifier(this.getUIContext());
  private count = 0;

  // Create an Animator object and set the animation.
  create() {
    let self = this;
    this.drawAnimator = this.getUIContext().createAnimator({
      duration: 1000,
      easing: 'ease',
      delay: 0,
      fill: 'forwards',
      direction: 'normal',
      iterations: 1,
      begin: 0,
      end: 2
    });
    this.drawAnimator.onFrame = (value: number) => {
      console.info('frame value =', value);
      const tempModifier = self.modifier as MyFullDrawModifier | MyFrontDrawModifier;
      tempModifier.scaleX = Math.abs(value - 1);
      tempModifier.scaleY = Math.abs(value - 1);
      // Manually trigger redraw.
      self.modifier.invalidate();
    };
  }

  build() {
    Column() {
      Row() {
        Text('test text')
          .width(100)
          .height(100)
          .margin(10)
          .backgroundColor(Color.Gray)
          .onClick(() => {
            const tempModifier = this.modifier as MyFullDrawModifier | MyFrontDrawModifier;
            tempModifier.scaleX -= 0.1;
            tempModifier.scaleY -= 0.1;
          })
          .drawModifier(this.modifier)
      }

      Row() {
        Button('create')
          .width(100)
          .height(100)
          .borderRadius(50)
          .margin(10)
          .onClick(() => {
            this.create();
          })
        Button('play')
          .width(100)
          .height(100)
          .borderRadius(50)
          .margin(10)
          .onClick(() => {
            if (this.drawAnimator) {
              this.drawAnimator.play();
            }
          })
        Button('changeModifier')
          .width(100)
          .height(100)
          .borderRadius(50)
          .margin(10)
          .onClick(() => {
            this.count += 1;
            if (this.count % 2 === 1) {
              console.info('change to full modifier');
              this.modifier = this.fullModifier;
            } else {
              console.info('change to front modifier');
              this.modifier = this.frontModifier;
            }
          })
      }
    }
    .width('100%')
    .height('100%')
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e1/v3/MGsCVkN7S-mCmj4SxxlAYQ/en-us_image_0000002568765211.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062236Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=E4C9560011F5BA089C85ACA816BC66CEB821FCF3FA62F23310198D6D6C4FF10D)

## Example 2: Implementing Custom Foreground Drawing for a Container Through DrawModifier

This example demonstrates how to implement custom foreground drawing for a [Column](../../../rows-columns-and-stacking/column/document.md) container using **DrawModifier**.

// xxx.ets
import { drawing } from '@kit.ArkGraphics2D';

class MyForegroundDrawModifier extends DrawModifier {
  public scaleX: number = 3;
  public scaleY: number = 3;
  uiContext: UIContext;

  constructor(uiContext: UIContext) {
    super();
    this.uiContext = uiContext;
  }

  // Override the drawForeground method to customize foreground drawing.
  drawForeground(context: DrawContext): void {
    const brush = new drawing.Brush();
    brush.setColor({
      alpha: 255,
      red: 0,
      green: 50,
      blue: 100
    });
    context.canvas.attachBrush(brush);
    const halfWidth = context.size.width / 2;
    const halfHeight = context.size.height / 2;
    context.canvas.drawRect({
      left: this.uiContext.vp2px(halfWidth - 30 \* this.scaleX),
      top: this.uiContext.vp2px(halfHeight - 30 \* this.scaleY),
      right: this.uiContext.vp2px(halfWidth + 30 \* this.scaleX),
      bottom: this.uiContext.vp2px(halfHeight + 30 \* this.scaleY)
    });
  }
}

@Entry
@Component
struct DrawModifierExample {
  // Instantiate the foreground drawing class, passing the UIContext instance.
  private foregroundModifier: MyForegroundDrawModifier = new MyForegroundDrawModifier(this.getUIContext());

  build() {
    Column() {
      Text('Here is a child node')
        .fontSize(36)
        .width('100%')
        .height('100%')
        .textAlign(TextAlign.Center)
    }
    .margin(50)
    .width(280)
    .height(300)
    .backgroundColor(0x87CEEB)
    // Apply custom foreground drawing by passing the DrawModifier instance.
    .drawModifier(this.foregroundModifier)
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/54/v3/OnVC6-wLRz6bddzVCz46NA/en-us_image_0000002537765486.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062236Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=F3F448A52C0F898AA9D93D75E407A62B8C36019B2EC597E9BB2F32E32225E915)
