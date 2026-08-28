# HdsListItem

This module allows you to configure the swipe effect of list items and can bear the **HdsListItemCard** component.

**Start version**: 6.0.0(20)

#### Modules to Import

import { HdsListItem } from '@kit.UIDesignKit';

#### API

HdsListItem({customItemBuilder?: CustomBuilder, hdsListItemCard?: HdsListItemCardOptions, swipeActionOptions?: HdsSwipeActionOptions | SwipeActionOptions, listItemModifier?: ListItemModifier})

Provides a list component.

**Decorator type**: @Component

**System capability**: SystemCapability.UIDesign.HDSPattern.Standard

**Abnormal device behavior**: The styles implemented by this API are inconsistent with the UX specifications for TVs. For example, a focused and hovered component cannot be enlarged, the background color of the focused component does not change, and the text default color within a button is different. This API can work properly for other device types.

**Start version**: 6.0.0(20)

| 
Parameter

 | 

Type

 | 

Mandatory

 | 

Decorator Type

 | 

Description

 |
| :-- | :-- | :-- | :-- | :-- |
| 

customItemBuilder

 | 

[CustomBuilder](../../../arkui/arkts-components/common-definitions/basic-types/document.md#custombuilder8)

 | 

No

 | 

@BuilderParam

 | 

Custom list item card.

 |
| 

hdsListItemCard

 | 

[HdsListItemCardOptions](../hdslistitemcard/document.md#section6323195713321)

 | 

No

 | 

\-

 | 

List item card.

 |
| 

swipeActionOptions

 | 

[HdsSwipeActionOptions](#section10384044394) | [SwipeActionOptions](../../../arkui/arkts-components/scroll-and-swipe/listitem/document.md#swipeactionoptions9)

 | 

No

 | 

\-

 | 

Options of the animation triggered by swiping.

**HdsSwipeActionOptions** represents the horizontal swipe effect type after **HdsListItem** has been encapsulated. **SwipeActionOptions** supports custom horizontal swipe effect types for **ListItem**.

 |
| 

listItemModifier

 | 

[ListItemModifier](../../../arkui/arkts-components/universal-attributes/modifiers-and-custom-property/attribute-modifier/document.md#custom-modifier)

 | 

No

 | 

\-

 | 

ListItem style modifier.

**Start version**: 6.0.1(21)

 |

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/32/v3/tJr4_hR1S728qqPpf8CJhw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062328Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=0857BA3AF62642597B1AED805EEB0BA794F09725DFCD5D5F6480184AA568DAA3)

The priority of **customItemBuilder** is higher than that of **hdsListItemCard**. If both **customItemBuilder** and **hdsListItemCard** are set, only **customItemBuilder** takes effect.

#### HdsSwipeActionOptions

Sets the styles for the icons that appear after swiping.

**System capability**: SystemCapability.UIDesign.HDSPattern.Standard

**Start version**: 6.0.0(20)

| 
Name

 | 

Type

 | 

Read-Only

 | 

Optional

 | 

Description

 |
| :-- | :-- | :-- | :-- | :-- |
| 

icons

 | 

Array<[SwipeIconConfigurations](#section113942388296)\>

 | 

No

 | 

Yes

 | 

Styles of the other three icons besides the delete icon.

 |
| 

deleteIconOptions

 | 

[DeleteIconOptions](#section17257185014306)

 | 

No

 | 

Yes

 | 

Style of the delete icon.

 |
| 

fullDeleteOptions

 | 

[FullDeleteOptions](#section184131316173219)

 | 

No

 | 

Yes

 | 

Action triggered when the swipe distance exceeds the component size.

 |

#### IconOptions

Sets whether to enable an icon and the icon's accessibility information.

**System capability**: SystemCapability.UIDesign.HDSPattern.Standard

**Start version**: 6.0.0(20)

| 
Name

 | 

Type

 | 

Read-Only

 | 

Optional

 | 

Description

 |
| :-- | :-- | :-- | :-- | :-- |
| 

enable

 | 

boolean

 | 

No

 | 

Yes

 | 

Indicates whether to enable an icon.

**true**: yes

**false**: no

The default value is **true**.

 |
| 

accessibilityText

 | 

[ResourceStr](../../../arkui/arkts-components/common-definitions/basic-types/document.md#resourcestr)

 | 

No

 | 

Yes

 | 

Accessibility text of an icon.

If a component does not contain text information, it will not be announced by the screen reader when selected. In this case, the screen reader user cannot know which component is selected. To solve this problem, you can set accessibility text for components without text information. When such a component is selected, the screen reader announces the specified accessibility text, informing the user which component is selected.

Default value: **""**

 |
| 

accessibilityDescription

 | 

[ResourceStr](../../../arkui/arkts-components/common-definitions/basic-types/document.md#resourcestr)

 | 

No

 | 

Yes

 | 

Accessibility description of an icon.

You can provide comprehensive text explanations to help users understand the operation they are about to perform and its potential consequences, especially when these cannot be inferred from the component's attributes and accessibility text alone. If a component contains both text information and the accessible description, the text is announced first and then the accessible description, when the component is selected.

Default value: **"Double-tap to activate"**

 |
| 

accessibilityLevel

 | 

string

 | 

No

 | 

Yes

 | 

Accessibility level of an icon, which specifies whether this component can be recognized by accessibility services.

The options are as follows:

**"auto"**: This option is treated as "yes" by the system for this component.

**"yes"**: The component can be recognized by accessibility services.

**"no"**: The component cannot be recognized by accessibility services.

**"no-hide-descendants"**: Neither the component nor its child components can be recognized by accessibility services.

The default value is **"auto"**.

 |

#### SwipeIconConfigurations

Sets the styles and functions for icons besides the delete icon that appear after swiping.

**System capability**: SystemCapability.UIDesign.HDSPattern.Standard

**Start version**: 6.0.0(20)

| 
Name

 | 

Type

 | 

Read-Only

 | 

Optional

 | 

Description

 |
| :-- | :-- | :-- | :-- | :-- |
| 

icon

 | 

[SwipeIconType](#section2930111714251)

 | 

No

 | 

No

 | 

Icon resource, which can be of the symbol or image type.

 |
| 

iconOptions

 | 

[IconOptions](#section1486115401)

 | 

No

 | 

Yes

 | 

Options of an icon.

 |
| 

backgroundColor

 | 

[ResourceColor](../../../arkui/arkts-components/common-definitions/basic-types/document.md#resourcecolor)

 | 

No

 | 

Yes

 | 

Icon background color.

 |
| 

onAction

 | 

[SwipeActionCallback](#section812564671318)

 | 

No

 | 

Yes

 | 

Tap callback.

 |

#### DeleteIconOptions

Sets the attributes for the delete icon.

**System capability**: SystemCapability.UIDesign.HDSPattern.Standard

**Start version**: 6.0.0(20)

| 
Name

 | 

Type

 | 

Read-Only

 | 

Optional

 | 

Description

 |
| :-- | :-- | :-- | :-- | :-- |
| 

backgroundColor

 | 

[ResourceColor](../../../arkui/arkts-components/common-definitions/basic-types/document.md#resourcecolor)

 | 

No

 | 

Yes

 | 

Background color of the delete icon.

 |
| 

iconColor

 | 

[ResourceColor](../../../arkui/arkts-components/common-definitions/basic-types/document.md#resourcecolor)

 | 

No

 | 

Yes

 | 

Color of the delete icon.

 |
| 

iconOptions

 | 

[IconOptions](#section1486115401)

 | 

No

 | 

Yes

 | 

Options of the delete icon.

 |
| 

onAction

 | 

[SwipeActionCallback](#section812564671318)

 | 

No

 | 

Yes

 | 

Tap callback.

 |

#### FullDeleteOptions

Sets whether swiping again will delete the corresponding list item and defines the deletion callback.

**System capability**: SystemCapability.UIDesign.HDSPattern.Standard

**Start version**: 6.0.0(20)

| 
Name

 | 

Type

 | 

Read-Only

 | 

Optional

 | 

Description

 |
| :-- | :-- | :-- | :-- | :-- |
| 

isFullDelete

 | 

boolean

 | 

No

 | 

Yes

 | 

Indicates whether swiping again will delete the corresponding list item.

-   **true**: yes
-   **false**: no

The default value is **false**.

 |
| 

onFullDeleteAction

 | 

[SwipeActionCallback](#section812564671318)

 | 

No

 | 

Yes

 | 

Triggered upon the deletion of a list item.

 |

#### SwipeIconType

type SwipeIconType = SymbolGlyphModifier | ImageOptions

Defines the resource type of icons that appear after swiping.

**System capability**: SystemCapability.UIDesign.HDSPattern.Standard

**Start version**: 6.0.0(20)

**Returns**:

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

[SymbolGlyphModifier](../../../arkui/arkts-components/universal-attributes/modifiers-and-custom-property/attribute-modifier/document.md#custom-modifier)

 | 

Symbol resource type.

 |
| 

[ImageOptions](../hdslistitemcard/document.md#section3582112115362)

 | 

Image resource type.

 |

#### SwipeActionCallback

type SwipeActionCallback = () => void

Callback function triggered by a list swipe event.

**System capability**: SystemCapability.UIDesign.HDSPattern.Standard

**Start version**: 6.0.0(20)

#### Example

Set a list with horizontal swipe animation.

import { promptAction, SymbolGlyphModifier, TextModifier } from '@kit.ArkUI';
import { HdsListItem } from '@kit.UIDesignKit';

@Entry
@Component
struct HdsListItemExample {
  @State dataSource: LazyDataSource<Item> = new LazyDataSource();
  @State dataArr: Array<Item> = \[\];
  @State EndOffset: number = 0;
  private scroller: Scroller = new Scroller();

  build() {
    Column() {
      List({ space: 10, scroller: this.scroller }) {
        LazyForEach(this.dataSource, (item: Item) => {
          HdsListItem({
            hdsListItemCard: {
              textItem: {
                primaryText: {
                  text: 'Primary Text',
                  modifier: new TextModifier().fontColor(Color.Orange).fontSize(16),
                }
              }
            },
            swipeActionOptions: {
              icons: \[
                {
                  icon: new SymbolGlyphModifier($r('sys.symbol.share')).fontColor(\[Color.Red\]).fontSize(16),
                  backgroundColor: Color.Green,
                  onAction: () => {
                    promptAction.openToast({ message: 'Tap share button', duration: 100 });
                  },
                },
                {
                  icon: new SymbolGlyphModifier($r('sys.symbol.plus\_square\_on\_square')),
                  backgroundColor: Color.Orange,
                  onAction: () => {
                    promptAction.openToast({ message: 'Tap copy button', duration: 100 });
                  },
                },
                {
                  icon: new SymbolGlyphModifier($r('sys.symbol.plus\_square\_dashed\_on\_square'))
                          .symbolEffect(new BounceSymbolEffect(), true),
                  onAction: () => {
                    promptAction.openToast({ message: 'Tap paste button', duration: 100 });
                  },
                },
              \],
              deleteIconOptions: {
                backgroundColor: Color.Red, //  ---Change the background color.
                iconColor: Color.Gray, //  ---- Change the color of the trash can.
                onAction: () => {
                  promptAction.openToast({ message: 'Tap delete button', duration: 100 });
                }, //   --Tap action callback.
              },
              fullDeleteOptions: {
                isFullDelete: true, // --- Indicates whether to automatically trigger deletion when the swipe distance exceeds the component size. The default value is **false**.
                onFullDeleteAction: () => {
                  promptAction.openToast({ message: 'Trigger automatic deletion', duration: 100 });
                  this.getUIContext()?.animateTo({
                    duration: 350,
                  }, () => {
                    this.dataSource.deleteItem(item)
                  });
                }, //   -- Callback upon deletion.
              },
            }
          })
        }, (item: Item) => item.data)
      }
      .scrollBar(BarState.Off)
      .onDidScroll((scrollOffset: number) => {
        this.EndOffset = scrollOffset
      })
      .margin(10)
      .width('100%')
      .height('100%')
    }
    .backgroundColor('#0D182431')
    .width('100%')
    .height('100%')
  }

  aboutToAppear() {
    for (let i = 0; i < 2; i++) {
      this.dataSource.pushItem(new Item(i + ''));
      this.dataArr.push(new Item(i + ''));
    }
  }
}

class Item {
  constructor(data: string) {
    this.data = data;
  }

  public data: string = '';
}

export class LazyDataSource<T> implements IDataSource {
  private elements: T\[\];
  private listeners: Set<DataChangeListener>;

  constructor(elements: T\[\] = \[\]) {
    this.elements = elements;
    this.listeners = new Set();
  }

  public totalCount(): number {
    return this.elements.length;
  }

  public getData(index: number): T {
    return this.elements\[index\];
  }

  public indexOf(item: T): number {
    return this.elements.indexOf(item);
  }

  public pinItem(item: T, index: number): void {
    this.elements.splice(index, 1);
    this.elements.unshift(item);
    this.listeners.forEach(listener => listener.onDataReloaded());
  }

  public pushItem(item: T) {
    this.elements.push(item);
    this.listeners.forEach(listener => listener.onDataAdd(this.elements.length - 1));
  }

  public deleteItem(item: T): void {
    const index = this.elements.indexOf(item);
    if (index < 0) {
      return;
    }
    this.elements.splice(index, 1);
    this.listeners.forEach(listener => listener.onDataDelete(index));
  }

  public deleteItemByIndex(index: number): void {
    this.elements.splice(index, 1);
    this.listeners.forEach(listener => listener.onDataDelete(index));
  }

  public registerDataChangeListener(listener: DataChangeListener): void {
    this.listeners.add(listener);
  }

  public unregisterDataChangeListener(listener: DataChangeListener): void {
    this.listeners.delete(listener);
  }
}

Display effect:

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1a/v3/9aGg1FUKTICTJu_gTcWFgw/en-us_image_0000002532304111.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062328Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=3C1B5C82FE9F38FEF6CA2624FC2C5A094758AF605DB051379A68591746329465 "Click to enlarge")
