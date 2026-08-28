# Attribute Modifier

With the attribute modifier, you can dynamically set component attributes, complete with the **if/else** syntax and polymorphic style.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3f/v3/1I6JhgDkTkuUpU_whS3AaA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062236Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=404033AFEC45CF9213A59DF03E2DEE582D6FB76E087C1E29AD18590EC186755C)

-   This feature is supported since API version 11. Updates will be marked with a superscript to indicate their earliest API version.
    
-   Ensure that the attributes set in **attributeModifier** are different from those set in other methods. Otherwise, **attributeModifier** does not take effect when the page is refreshed.
    
-   For simple scenarios requiring conditional assignment of a single component attribute, [ternary operators](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/arkts-declarative-ui-description#configuring-attributes) provide a concise alternative. Example: **.width(isFullScreen ? 200 : 100)**.
    
-   **attributeModifier** supports custom components since API version 20.
    

#### attributeModifier

attributeModifier(modifier: AttributeModifier<T>): T

Creates an attribute modifier.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| modifier | [AttributeModifier<T>](#attributemodifiert) | Yes | 
Modifier for dynamically setting attributes on the current component. The **if/else** syntax is supported.

**modifier**: attribute modifier. You need to customize classes to implement the **AttributeModifier** API.

 |

**Return value**

| Type | Description |
| :-- | :-- |
| T | Current component. |

#### AttributeModifier<T>

You need a custom class to implement the **AttributeModifier** API.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/08/v3/wrydzutpTEaGxY6U_9f1RA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062236Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=8F248B74DFDFCD1FC25F12E1FB14B18F0A6345E3850AB8F1A259E36EFDE4A823)

In the following APIs, setting the same value or object for the same attribute of the **instance** object will not trigger an update.

#### \[h2\]applyNormalAttribute

applyNormalAttribute?(instance: T): void

Applies the style of a component in the normal state.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| instance | T | Yes | Component attribute class, which identifies the type of component to which attributes will be applied, for example, [ButtonAttribute](../../../buttons-and-selections/button/document.md#attributes) for the [Button](../../../buttons-and-selections/button/document.md) component and [TextAttribute](../../../text-and-input/text/document.md#attributes) for the [Text](../../../text-and-input/text/document.md) component. |

#### \[h2\]applyPressedAttribute

applyPressedAttribute?(instance: T): void

Applies the style of a component in the pressed state. For implementation examples, see [Example 2: Implementing the Pressed State Effect with a Modifier](#example-2-implementing-the-pressed-state-effect-with-a-modifier) and [Example 8: Implementing the Pressed State Effect for a Custom Component with a Modifier](#example-8-implementing-the-pressed-state-effect-for-a-custom-component-with-a-modifier).

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| instance | T | Yes | Component attribute class, which identifies the type of component to which attributes will be applied, for example, [ButtonAttribute](../../../buttons-and-selections/button/document.md#attributes) for the [Button](../../../buttons-and-selections/button/document.md) component and [TextAttribute](../../../text-and-input/text/document.md#attributes) for the [Text](../../../text-and-input/text/document.md) component. |

#### \[h2\]applyFocusedAttribute

applyFocusedAttribute?(instance: T): void

Applies the style of a component in the focused state. For the implementation example, see [Example 5: Setting the Focused State Style with a Modifier](#example-5-setting-the-focused-state-style-with-a-modifier).

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| instance | T | Yes | Component attribute class, which identifies the type of component to which attributes will be applied, for example, [ButtonAttribute](../../../buttons-and-selections/button/document.md#attributes) for the [Button](../../../buttons-and-selections/button/document.md) component and [TextAttribute](../../../text-and-input/text/document.md#attributes) for the [Text](../../../text-and-input/text/document.md) component. |

#### \[h2\]applyDisabledAttribute

applyDisabledAttribute?(instance: T): void

Applies the style of a component in the disabled state. For the implementation example, see [Example 6: Setting the Disabled State Style with a Modifier](#example-6-setting-the-disabled-state-style-with-a-modifier).

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| instance | T | Yes | Component attribute class, which identifies the type of component to which attributes will be applied, for example, [ButtonAttribute](../../../buttons-and-selections/button/document.md#attributes) for the [Button](../../../buttons-and-selections/button/document.md) component and [TextAttribute](../../../text-and-input/text/document.md#attributes) for the [Text](../../../text-and-input/text/document.md) component. |

#### \[h2\]applySelectedAttribute

applySelectedAttribute?(instance: T): void

Applies the style of a component in the selected state.

In the preceding APIs, **instance** indicates the component type. You can customize these APIs and use them with the \*\*if/else \*\*syntax. For the implementation example, see [Example 7: Setting the Selected State Style with a Modifier](#example-7-setting-the-selected-state-style-with-a-modifier).

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| instance | T | Yes | Component attribute class, which identifies the type of component to which attributes will be applied, for example, [ButtonAttribute](../../../buttons-and-selections/button/document.md#attributes) for the [Button](../../../buttons-and-selections/button/document.md) component and [TextAttribute](../../../text-and-input/text/document.md#attributes) for the [Text](../../../text-and-input/text/document.md) component. |

**Value range of the instance parameter**

[AlphabetIndexerAttribute](../../../information-display/alphabetindexer/document.md#attributes), [BadgeAttribute](../../../information-display/badge/document.md#attributes), [BlankAttribute](../../../blank-and-divider/blank/document.md#attributes), [ButtonAttribute](../../../buttons-and-selections/button/document.md#attributes), [CalendarPickerAttribute](../../../buttons-and-selections/calendarpicker/document.md#attributes), [CanvasAttribute](../../../canvas-drawing/canvas/document.md#attributes), [CheckboxAttribute](../../../buttons-and-selections/checkbox/document.md#attributes), [CheckboxGroupAttribute](../../../buttons-and-selections/checkboxgroup/document.md#attributes), [CircleAttribute](../../../graphic-drawing/circle/document.md#attributes), [ColumnAttribute](../../../rows-columns-and-stacking/column/document.md#attributes), [ColumnSplitAttribute](../../../grid-and-column-layout/columnsplit/document.md#attributes), [ShapeAttribute](../../../graphic-drawing/shape/document.md#attributes), [CommonAttribute](../../document.md), [CounterAttribute](../../../information-display/counter/document.md#attributes), [DataPanelAttribute](../../../information-display/datapanel/document.md#attributes), [DatePickerAttribute](../../../buttons-and-selections/datepicker/document.md#attributes), [DividerAttribute](../../../blank-and-divider/divider/document.md#attributes), [EllipseAttribute](../../../graphic-drawing/ellipse/document.md#attributes), [FlexAttribute](../../../rows-columns-and-stacking/flex/document.md#attributes), [FlowItemAttribute](../../../scroll-and-swipe/flowitem/document.md#attributes), [FormLinkAttribute](../../../service-widgets/formlink/document.md#attributes), [GaugeAttribute](../../../information-display/gauge/document.md#attributes), [GridAttribute](../../../scroll-and-swipe/grid/document.md#attributes), [GridColAttribute](../../../grid-and-column-layout/gridcol/document.md#attributes), [ColumnAttribute](../../../rows-columns-and-stacking/column/document.md#attributes), [GridItemAttribute](../../../scroll-and-swipe/griditem/document.md#attributes), [GridRowAttribute](../../../grid-and-column-layout/gridrow/document.md#attributes), [HyperlinkAttribute](../../../text-and-input/hyperlink/document.md#attributes), [IndicatorComponentAttribute](../../../navigation-and-switching/indicator/document.md#attributes), [ImageAttribute](../../../images-and-videos/image/document.md#attributes), [ImageAnimatorAttribute](../../../images-and-videos/imageanimator/document.md#attributes), [ImageSpanAttribute](../../../text-and-input/imagespan/document.md#attributes), [LineAttribute](../../../graphic-drawing/line/document.md#attributes), [ListAttribute](../../../scroll-and-swipe/list/document.md#attributes), [ListItemAttribute](../../../scroll-and-swipe/listitem/document.md#attributes), [ListItemGroupAttribute](../../../scroll-and-swipe/listitemgroup/document.md#attributes), [LoadingProgressAttribute](../../../information-display/loadingprogress/document.md#attributes), [MarqueeAttribute](../../../information-display/marquee/document.md#attributes), [MenuAttribute](../../../menus/menu/document.md#attributes), [MenuItemAttribute](../../../menus/menuitem/document.md#attributes), [MenuItemGroupAttribute](../../../menus/menuitemgroup/document.md), [NavDestinationAttribute](../../../navigation-and-switching/navdestination/document.md#attributes), [NavigationAttribute](../../../navigation-and-switching/navigation/document.md#attributes), [NavigatorAttribute](../../../components-and-apis-no-longer-maintained/navigator/document.md#attributes), [NavRouterAttribute](../../../components-and-apis-no-longer-maintained/navrouter/document.md#attributes), [PanelAttribute](../../../components-and-apis-no-longer-maintained/panel/document.md#attributes), [PathAttribute](../../../graphic-drawing/path/document.md#attributes), [PatternLockAttribute](../../../information-display/patternlock/document.md#attributes), [PolygonAttribute](../../../graphic-drawing/polygon/document.md#attributes), [PolylineAttribute](../../../graphic-drawing/polyline/document.md#attributes), [ProgressAttribute](../../../information-display/progress/document.md#attributes), [QRCodeAttribute](../../../information-display/qrcode/document.md#attributes), [RadioAttribute](../../../buttons-and-selections/radio/document.md#attributes), [RatingAttribute](../../../buttons-and-selections/rating/document.md#attributes), [RectAttribute](../../../graphic-drawing/rect/document.md#attributes), [RefreshAttribute](../../../scroll-and-swipe/refresh/document.md#attributes), [RelativeContainerAttribute](../../../rows-columns-and-stacking/relativecontainer/document.md#attributes), [RichEditorAttribute](../../../text-and-input/richeditor/document.md#attributes), [RichTextAttribute](../../../text-and-input/richtext/document.md#attributes), [RowAttribute](../../../rows-columns-and-stacking/row/document.md#attributes), [RowSplitAttribute](../../../grid-and-column-layout/rowsplit/document.md#attributes), [ScrollAttribute](../../../scroll-and-swipe/scroll/document.md#attributes), [ScrollBarAttribute](../../../scroll-and-swipe/scrollbar/document.md#attributes), [SearchAttribute](../../../text-and-input/search/document.md#attributes), [SelectAttribute](../../../buttons-and-selections/select/document.md#attributes), [ShapeAttribute](../../../graphic-drawing/shape/document.md#attributes), [SideBarContainerAttribute](../../../grid-and-column-layout/sidebarcontainer/document.md#attributes), [SliderAttribute](../../../buttons-and-selections/slider/document.md#attributes), [SpanAttribute](../../../text-and-input/span/document.md#attributes), [StackAttribute](../../../rows-columns-and-stacking/stack/document.md#attributes), [StepperAttribute](../../../components-and-apis-no-longer-maintained/stepper/document.md#attributes), [StepperItemAttribute](../../../components-and-apis-no-longer-maintained/stepperitem/document.md#attributes), [SwiperAttribute](../../../scroll-and-swipe/swiper/document.md#attributes), [SymbolGlyphAttribute](../../../text-and-input/symbolglyph/document.md#attributes), [TabContentAttribute](../../../navigation-and-switching/tabcontent/document.md#attributes), [TabsAttribute](../../../navigation-and-switching/tabs/document.md#attributes), [TextAttribute](../../../text-and-input/text/document.md#attributes), [TextAreaAttribute](../../../text-and-input/textarea/document.md#attributes), [TextClockAttribute](../../../information-display/textclock/document.md#attributes), [TextInputAttribute](../../../text-and-input/textinput/document.md#attributes), [TextPickerAttribute](../../../buttons-and-selections/textpicker/document.md#attributes), [TextTimerAttribute](../../../information-display/texttimer/document.md#attributes), [TimePickerAttribute](../../../buttons-and-selections/timepicker/document.md#attributes), [ToggleAttribute](../../../buttons-and-selections/toggle/document.md#attributes), [VideoAttribute](../../../images-and-videos/video/document.md#attributes), [WaterFlowAttribute](../../../scroll-and-swipe/waterflow/document.md#attributes), [XComponentAttribute](../../../rendering-drawing/xcomponent/document.md#attributes), [ParticleAttribute](../../../animation/particle-animation-particle/document.md#attributes), [UIPickerComponentAttribute](../../../buttons-and-selections/uipickercomponent/document.md#attributes)

**Supported attributes**

1.  Attributes that accept or return a [CustomBuilder](../../../common-definitions/basic-types/document.md#custombuilder8) are not supported.
2.  Attributes that accept a [modifier](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/arkts-user-defined-modifier) type, such as [attributeModifier](#attributemodifier), [drawModifier](../drawing-modifier/document.md), and [gestureModifier](../gesture-modifier/document.md), are not supported.
3.  Attribute related to [animation](../../../animation/property-animation-animation/document.md) are not supported.
4.  Attributes of the [gesture](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/arkts-gesture-events-binding) type are not supported.
5.  Attribute related to [stateStyles](../../polymorphic-style/document.md) are not supported.
6.  Deprecated attributes are not supported.

When unsupported or unimplemented attributes are used, exceptions such as "Method not implemented.", "is not callable", or "Builder is not supported." are thrown. For details about the supported modifiers, see [attributeModifier Support for Attributes and Events](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/arkts-user-defined-extension-attributemodifier#attributemodifier-support-for-attributes-and-events).

#### Custom Modifier

Custom modifiers can be used in building components and configuring attributes since API version 12. Through the custom modifiers, you can call the attribute and style APIs of encapsulated components.

**Supported custom modifiers**

CommonModifier, ColumnModifier, ColumnSplitModifier, RowModifier, RowSplitModifier, SideBarContainerModifier, BlankModifier, DividerModifier, GridColModifier, GridRowModifier, NavDestinationModifier, NavigatorModifier, StackModifier, NavigationModifier, NavRouterModifier, StepperItemModifier, TabsModifier, GridModifier, GridItemModifier, ListModifier, ListItemModifier, ListItemGroupModifier, ScrollModifier, SwiperModifier, WaterFlowModifier, ButtonModifier, CounterModifier, TextPickerModifier, TimePickerModifier, ToggleModifier, CalendarPickerModifier, CheckboxModifier, CheckboxGroupModifier, DatePickerModifier, RadioModifier, RatingModifier, SelectModifier, SliderModifier, PatternLockModifier, SpanModifier, RichEditorModifier, RefreshModifier, SearchModifier, TextAreaModifier, TextModifier, TextInputModifier, ImageSpanModifier, ImageAnimatorModifier, ImageModifier, VideoModifier, DataPanelModifier, GaugeModifier, LoadingProgressModifier, MarqueeModifier, ProgressModifier, QRCodeModifier, TextClockModifier, TextTimerModifier, LineModifier, PathModifier, PolygonModifier, PolylineModifier, RectModifier, ShapeModifier, AlphabetIndexerModifier, FormComponentModifier, HyperlinkModifier, MenuModifier, MenuItemModifier, PanelModifier, SymbolGlyphModifier, ParticleModifier, and UIPickerComponentModifier

**CommonModifier** can be used for unexposed components.

**Precautions**

1.  When a custom modifier is applied to a component, the corresponding attribute of the component takes effect.
2.  Updating the attribute value of a custom modifier changes the corresponding attribute of the component to which the modifier is applied. The custom modifier is a base class, and the constructed object is a child class object. When using the object, use **as** to assert the type as a child class.
3.  With a custom modifier applied to two components, updating the attribute value of the custom modifier changes the corresponding attributes of both components.
4.  If attributes A and B are set through a custom modifier, and then attributes C and D are set through other means, all the four attributes take effect on the component.
5.  Custom modifiers do not support change detection of state data decorated with @State. For details, see [Example 3: Understanding Custom Modifiers Do Not Support State Data Changes)](#example-3-understanding-custom-modifiers-do-not-support-state-data-changes).
6.  If you use **attributeModifier** to set attributes multiple times, all the set attributes take effect, and those attributes that are set multiple times take effect based on the configuration sequence.

#### Example

## Example 1: Switching the Background Color with a Modifier

This example demonstrates how to switch the background color of a **Button** component by binding it to a modifier.

// xxx.ets
// Set the custom AttributeModifier for the Button component attributes.
class MyButtonModifier implements AttributeModifier<ButtonAttribute> {
  public isDark: boolean = false;

  applyNormalAttribute(instance: ButtonAttribute): void {
    if (this.isDark) {
      instance.backgroundColor(Color.Black);
    } else {
      instance.backgroundColor(Color.Red);
    }
  }
}

@Entry
@Component
struct attributeDemo {
  @State modifier: MyButtonModifier = new MyButtonModifier();

  build() {
    Row() {
      Column() {
        Button("Button")
          .attributeModifier(this.modifier)
          .onClick(() => {
            this.modifier.isDark = !this.modifier.isDark;
          })
      }
      .width('100%')
    }
    .height('100%')
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/73/v3/S0TUesMvQBiLwRfnxW2fCw/en-us_image_0000002537925420.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062236Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=793CB1D2E6E31E540F800D4A5ADF94ABB2C4EE4214A2263EDCC7CE168B036F14)

## Example 2: Implementing the Pressed State Effect with a Modifier

This example demonstrates how to implement a pressed state effect for a **Button** component by binding it to a modifier. For details about how to use the attribute modifier with state management V2, see [Modifier](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/arkts-v1-v2-migration-inner-object#modifier).

// xxx.ets
// Set the custom AttributeModifier for the Button component attributes.
class MyButtonModifier implements AttributeModifier<ButtonAttribute> {
  applyNormalAttribute(instance: ButtonAttribute): void {
    instance.backgroundColor(Color.Black);
  }

  applyPressedAttribute(instance: ButtonAttribute): void {
    instance.backgroundColor(Color.Red);
  }
}

@Entry
@Component
struct attributePressedDemo {
  @State modifier: MyButtonModifier = new MyButtonModifier();

  build() {
    Row() {
      Column() {
        Button("Button")
          .attributeModifier(this.modifier)
      }
      .width('100%')
    }
    .height('100%')
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f5/v3/4cTltJSJSRymt7sON6bOwQ/en-us_image_0000002537925420.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062236Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=371CA34B2B4DED4CE6BA9D0BA481CB4E54F9D11C2C9C782664DD280BC792E195)

## Example 3: Understanding Custom Modifiers Do Not Support State Data Changes

This example shows how to set the width of a custom modifier using state data. Custom modifiers do not support observing changes in data decorated with the @State decorator. Therefore, the width does not change when the button is clicked.

import { CommonModifier } from "@kit.ArkUI";

const TEST\_TAG: string = "AttributeModifier";

// Set the custom AttributeModifier for the universal component attributes.
class MyModifier extends CommonModifier {
  applyNormalAttribute(instance: CommonAttribute): void {
    super.applyNormalAttribute?.(instance);
  }
}

@Component
struct MyImage1 {
  @Link modifier: CommonModifier;

  build() {
    Image($r("app.media.startIcon")).attributeModifier(this.modifier as MyModifier)
  }
}

@Entry
@Component
struct Index {
  index: number = 0;
  @State width1: number = 100;
  @State height1: number = 100;
  @State myModifier: CommonModifier = new MyModifier().width(this.width1).height(this.height1).margin(10);

  build() {
    Column() {
      Button($r("app.string.EntryAbility\_label"))
        .margin(10)
        .onClick(() => {
          console.info(TEST\_TAG, "onClick");
          this.index++;
          if (this.index % 2 === 1) {
            this.width1 = 10;
            console.info(TEST\_TAG, "setGroup1");
          } else {
            this.height1 = 10;
            console.info(TEST\_TAG, "setGroup2");
          }
        })
      MyImage1({ modifier: this.myModifier })
    }
    .width('100%')
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/47/v3/PU-QaNvYQo61-IumHpLxzg/en-us_image_0000002568685197.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062236Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=4230DC830C5A6F18867E5F231F59B8F3512BB3B757B3E0CEA24D86CCC723170A)

## Example 4: Combining Modifier and Custom Modifier Attributes

This example demonstrates how to set **width** and **height** through a custom modifier. When the button is clicked, [borderStyle](../../../common-definitions/enums/document.md#borderstyle) and [borderWidth](../../layout-and-borders/border-styling/document.md#borderwidth) are configured, with all four attributes taking effect simultaneously.

import { CommonModifier } from "@kit.ArkUI";

const TEST\_TAG: string = "AttributeModifier";

// Set the custom AttributeModifier for the universal component attributes.
class MyModifier extends CommonModifier {
  applyNormalAttribute(instance: CommonAttribute): void {
    super.applyNormalAttribute?.(instance);
  }

  public setGroup1(): void {
    this.borderStyle(BorderStyle.Dotted);
    this.borderWidth(8);
  }

  public setGroup2(): void {
    this.borderStyle(BorderStyle.Dashed);
    this.borderWidth(8);
  }
}

@Component
struct MyImage1 {
  @Link modifier: CommonModifier;

  build() {
    Image($r("app.media.startIcon")).attributeModifier(this.modifier as MyModifier)
  }
}

@Entry
@Component
struct Index {
  @State myModifier: CommonModifier = new MyModifier().width(100).height(100).margin(10);
  index: number = 0;

  build() {
    Column() {
      Button($r("app.string.EntryAbility\_label"))
        .margin(10)
        .onClick(() => {
          console.info(TEST\_TAG, "onClick");
          this.index++;
          if (this.index % 2 === 1) {
            (this.myModifier as MyModifier).setGroup1();
            console.info(TEST\_TAG, "setGroup1");
          } else {
            (this.myModifier as MyModifier).setGroup2();
            console.info(TEST\_TAG, "setGroup2");
          }
        })
      MyImage1({ modifier: this.myModifier })
    }
    .width('100%')
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a7/v3/1zHAf0oJRTy-JSgffAelqQ/en-us_image_0000002568765207.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062236Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=A545D5EB365BF246571D19CEB8E82BCAEC7796C3A86E82CF453E69EA3CB46BCC)

## Example 5: Setting the Focused State Style with a Modifier

This example demonstrates how to implement a focused state style for a **Button** component by binding it to a modifier. After **Button2** is clicked, the **Button** component displays the focused style when it has focus.

// Set the custom AttributeModifier for the Button component attributes.
class MyButtonModifier implements AttributeModifier<ButtonAttribute> {

  applyNormalAttribute(instance: ButtonAttribute): void {
    instance.backgroundColor(Color.Blue);
  }
  applyFocusedAttribute(instance: ButtonAttribute): void {
    instance.backgroundColor(Color.Green);
  }
}

@Entry
@Component
struct attributeDemo {
  @State modifier: MyButtonModifier = new MyButtonModifier();
  @State isDisable: boolean = true;

  build() {
    Row() {
      Column() {
        Button("Button")
          .attributeModifier(this.modifier)
          .enabled(this.isDisable)
          .id("app")
        Divider().vertical(false).strokeWidth(15).color(Color.Transparent)
        Button("Button2")
          .onClick(() => {
            this.getUIContext().getFocusController().activate(true);
            this.getUIContext().getFocusController().requestFocus("app");
          })
      }
      .width('100%')
    }
    .height('100%')
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6f/v3/W3uPLyQdTh64F-4h3o8oIA/en-us_image_0000002537765482.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062236Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=6A2443BD45DB9BF7F9D5FBEAE4E2D64C3EC0B3ED15888ECD9379D5508E560971)

## Example 6: Setting the Disabled State Style with a Modifier

This example demonstrates how to implement a disabled state style for a **Button** component by binding it to a modifier. After **Button2** is clicked, the **Button** component displays the disabled style when it is disabled.

// Set the custom AttributeModifier for the Button component attributes.
class MyButtonModifier implements AttributeModifier<ButtonAttribute> {
  applyDisabledAttribute(instance: ButtonAttribute): void {
    instance.width(200);
  }
}

@Entry
@Component
struct attributeDemo {
  @State modifier: MyButtonModifier = new MyButtonModifier();
  @State isDisable: boolean = true;

  build() {
    Row() {
      Column() {
        Button("Button")
          .attributeModifier(this.modifier)
          .enabled(this.isDisable)
        Divider().vertical(false).strokeWidth(15).color(Color.Transparent)
        Button("Button2")
          .onClick(() => {
            this.isDisable = !this.isDisable;
          })
      }
      .width('100%')
    }
    .height('100%')
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/70/v3/KCM7dmeOQC2HqG20dX53Zg/en-us_image_0000002537925422.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062236Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=2FD22799DBFCDA0E4A22963BA2325ECD849ED9FF4FA509B9960D8DEB6EBD212E)

## Example 7: Setting the Selected State Style with a Modifier

This example demonstrates how to implement a selected state style for a **Radio** component by binding it to a modifier.

// Set the custom AttributeModifier for the Radio component attributes.
class MyRadioModifier implements AttributeModifier<RadioAttribute> {
  applyNormalAttribute(instance: RadioAttribute): void {
    instance.backgroundColor(Color.Blue);
  }

  applySelectedAttribute(instance: RadioAttribute): void {
    instance.backgroundColor(Color.Red);
    instance.borderWidth(2);
  }
}

@Entry
@Component
struct attributeDemo {
  @State modifier: MyRadioModifier = new MyRadioModifier();
  @State value: boolean = false;
  @State value2: boolean = false;

  build() {
    Row() {
      Column() {
        Radio({ value: 'Radio1', group: 'radioGroup1' })
          .checked(this.value)
          .height(50)
          .width(50)
          .borderWidth(0)
          .borderRadius(30)
          .onClick(() => {
            this.value = !this.value;
          })
          .attributeModifier(this.modifier)
      }
      .width('100%')
    }
    .height('100%')
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ee/v3/4E4pj9KdReiWo7in10X0cw/en-us_image_0000002568685199.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062236Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=22557819584C9C684A7B3BE4769DAB3CEEF05CD61C457D7CCBE31F01EAA88E56)

## Example 8: Implementing the Pressed State Effect for a Custom Component with a Modifier

This example demonstrates how to implement a pressed state effect for a custom component (**Common**) by binding it to a modifier.

// xxx.ets
// Set the custom AttributeModifier for the custom component attributes.
class CustomModifier implements AttributeModifier<CommonAttribute> {
  applyNormalAttribute(instance: CommonAttribute): void {
    instance.backgroundColor(Color.Blue)
  }

  applyPressedAttribute(instance: CommonAttribute): void {
    instance.backgroundColor(Color.Gray)
  }
}

@Entry
@Component
struct attributePressedDemo {
  @State modifier: CustomModifier = new CustomModifier()

  build() {
    Row() {
      Column() {
        ChildComponent()
          .attributeModifier(this.modifier)
      }
      .width('100%')
    }
    .height('100%')
  }
}

// Custom component
@Component
struct ChildComponent {
  build() {
    Text("common")
      .fontColor(Color.White)
      .fontSize(28)
      .textAlign(TextAlign.Center)
      .width('35%')
      .height('10%')
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a/v3/p-C4j3viRkG0l3DEutbG_Q/en-us_image_0000002568765209.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062236Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=AE3D6CD60DD0EEECFD7E4DF40C58BAAF8A91868F5E9D14773F4972583361229A)
