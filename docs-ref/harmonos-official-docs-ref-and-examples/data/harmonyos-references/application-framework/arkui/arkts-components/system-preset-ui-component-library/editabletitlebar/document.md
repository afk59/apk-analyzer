# EditableTitleBar

The editable title bar is a title bar that comes with button icons, typically **Cancel** on the left and **Confirm** on the right, on a multi-select or editing page.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3d/v3/Nc4xv7S6RHi1egsQqce7yw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062250Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=19658C4B29494AD12197FCDF77E4785D7FB6CE2474AF4BFC60EDB4325AFAFA3B)

This component is supported since API version 10. Updates will be marked with a superscript to indicate their earliest API version.

#### Modules to Import

import { EditableTitleBar } from '@kit.ArkUI';

#### Child Components

Not supported

#### Attributes

The [universal attributes](../../universal-attributes/document.md) are not supported.

#### EditableTitleBar

EditableTitleBar({leftIconStyle: EditableLeftIconType, imageItem?: EditableTitleBarItem, title: ResourceStr, subtitle?: ResourceStr, menuItems?: Array<EditableTitleBarMenuItem>, isSaveIconRequired: boolean, onSave?: () => void, onCancel?: () =>void, options: EditableTitleBarOptions, contentMargin?: LocalizedMargin, leftIconDefaultFocus?: boolean, saveIconDefaultFocus?: boolean})

**Decorator**: @Component

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Device behavior differences**: On wearables, calling this API results in a runtime exception indicating that the API is undefined. On other devices, the API works correctly.

| Name | Type | Mandatory | Decorator | Description |
| :-- | :-- | :-- | :-- | :-- |
| leftIconStyle | [EditableLeftIconType](#editablelefticontype) | Yes | \- | 
Type of the icon on the left.

Default value: **EditableLeftIconType.Back**

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| imageItem12+ | [EditableTitleBarItem](#editabletitlebaritem12) | No | \- | 

A single menu item for the profile picture on the left.

Default value: **undefined**.

Note: Accessibility properties are not supported.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| title | [ResourceStr](../../common-definitions/basic-types/document.md#resourcestr) | Yes | \- | 

Title.

Default value: **''**, indicating that the title is empty

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| subtitle12+ | [ResourceStr](../../common-definitions/basic-types/document.md#resourcestr) | No | \- | 

Subtitle.

Default value: **''**, indicating that the subtitle is empty

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| menuItems | Array<[EditableTitleBarMenuItem](#editabletitlebarmenuitem)\> | No | \- | 

List of menu items on the right.

Default value: **undefined**.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| isSaveIconRequired12+ | boolean | Yes | \- | 

Whether the save button on the right is required.

Default value: **true**, indicating that the save button on the right is required.

**NOTE**

If not decorated by @Require, this parameter is not subject to mandatory validation during construction.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| onSave | () => void | No | \- | 

Save button click event.

Default value: **() => void**

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| onCancel | () => void | No | \- | 

Cancel action event, which is triggered when the left button is of the Cancel type.

Default value: **() => void**

Back action event, which is triggered when the left button is of the Back type, since API version 12.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| options12+ | [EditableTitleBarOptions](#editabletitlebaroptions12) | Yes | \- | 

Title style.

Default value:

{

safeAreaTypes: \[SafeAreaType.SYSTEM\],

safeAreaEdges: \[SafeAreaEdge.TOP\],

backgroundColor: '#00000000'

}

**NOTE**

If not decorated by @Require, this parameter is not subject to mandatory validation during construction.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| contentMargin12+ | [LocalizedMargin](../../common-definitions/basic-types/document.md#localizedmargin12) | No | @Prop | 

Content margin. Negative numbers are not supported.

Default value:

{start: LengthMetrics.resource($r('sys.float.margin\_left')), end: LengthMetrics.resource($r('sys.float.margin\_right'))}

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| leftIconDefaultFocus18+ | boolean | No | \- | 

Whether the left icon is the default focus.

Default value: **false**, indicating that the left icon is not the default focus.

**Atomic service API**: This API can be used in atomic services since API version 18.

 |
| saveIconDefaultFocus18+ | boolean | No | \- | 

Whether the save icon is the default focus.

Default value: **false**, indicating that the save icon is not the default focus.

**Atomic service API**: This API can be used in atomic services since API version 18.

 |

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9a/v3/m4gNdGIATI69sn116zP6sg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062250Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=C7E13FC09937CD9435DB8478A1805AB2839DC2C125042987890D58804DCD8AE5)

The input parameter cannot be **undefined**, that is, calling **EditableTitleBar(undefined)** is not allowed.

If multiple operable areas are set as default focus, the first one in the display order that is set as the default focus will be the default focus.

#### EditableLeftIconType

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Device behavior differences**: On wearables, calling this API results in a runtime exception indicating that the API is undefined. On other devices, the API works correctly.

| Name | Value | Description |
| :-- | :-- | :-- |
| Back | 0 | Back. |
| Cancel | 1 | Cancel. |

#### EditableTitleBarMenuItem

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Device behavior differences**: On wearables, calling this API results in a runtime exception indicating that the API is undefined. On other devices, the API works correctly.

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| value | [ResourceStr](../../common-definitions/basic-types/document.md#resourcestr) | No | No | 
Icon resource.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| symbolStyle18+ | [SymbolGlyphModifier](../../universal-attributes/modifiers-and-custom-property/symbol-glyph-modifier/document.md#symbolglyphmodifier) | No | Yes | 

Symbol icon resource, which has higher priority than **value**.

**Atomic service API**: This API can be used in atomic services since API version 18.

 |
| label12+ | [ResourceStr](../../common-definitions/basic-types/document.md#resourcestr) | No | Yes | 

Icon label.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| isEnabled | boolean | No | Yes | 

Whether to enable the item. Default value: **true**.

**true**: The item is enabled.

**false**: The item is disabled.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| action | () => void | No | Yes | 

Right-side custom button click event of the title bar.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| accessibilityLevel18+ | string | No | Yes | 

Accessibility level. It determines whether the component can be recognized by accessibility services.

The options are as follows:

**"auto"**: This option is treated as "yes" by the system for this component.

**"yes"**: The component can be recognized by accessibility services.

**"no"**: The component cannot be recognized by accessibility services.

**"no-hide-descendants"**: Neither the component nor its child components can be recognized by accessibility services.

Default value: **"auto"**

**Atomic service API**: This API can be used in atomic services since API version 18.

 |
| accessibilityText18+ | [ResourceStr](../../common-definitions/basic-types/document.md#resourcestr) | No | Yes | 

Accessibility text, that is, accessible label name. If a component does not contain text information, it will not be announced by the screen reader when selected. In this case, the screen reader user cannot know which component is selected. To solve this problem, you can set accessibility text for components without text information. When such a component is selected, the screen reader announces the specified accessibility text, informing the user which component is selected.

Default value: value of the **label** property if it is set and an empty string otherwise.

**Atomic service API**: This API can be used in atomic services since API version 18.

 |
| accessibilityDescription18+ | [ResourceStr](../../common-definitions/basic-types/document.md#resourcestr) | No | Yes | 

Accessible description. You can provide comprehensive text explanations to help users understand the operation they are about to perform and its potential consequences, especially when these cannot be inferred from the component's attributes and accessibility text alone. If a component contains both text information and the accessible description, the text is announced first and then the accessible description, when the component is selected.

Default value: **"Double-tap to activate"**

**Atomic service API**: This API can be used in atomic services since API version 18.

 |
| defaultFocus18+ | boolean | No | Yes | 

Whether to set the item as the default focus.

**true**: Set the item as the default focus.

**false**: Do not set the item as the default focus.

Default value: **false**

The **defaultFocus** property requires the **isEnabled** property to be set to **true** beforehand; otherwise, **defaultFocus** will be treated as **false**.

**Atomic service API**: This API can be used in atomic services since API version 18.

 |

#### EditableTitleBarItem12+

type EditableTitleBarItem = EditableTitleBarMenuItem

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Device behavior differences**: On wearables, calling this API results in a runtime exception indicating that the API is undefined. On other devices, the API works correctly.

| Type | Description |
| :-- | :-- |
| [EditableTitleBarMenuItem](#editabletitlebarmenuitem) | A single menu item for the profile picture on the left. |

#### EditableTitleBarOptions12+

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Device behavior differences**: On wearables, calling this API results in a runtime exception indicating that the API is undefined. On other devices, the API works correctly.

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| backgroundColor | [ResourceColor](../../common-definitions/basic-types/document.md#resourcecolor) | No | Yes | 
Background color of the title bar.

Default value: **'#00000000'**

 |
| backgroundBlurStyle | [BlurStyle](../../universal-attributes/basic-attributes/background/document.md#blurstyle9) | No | Yes | 

Background blur style of the title bar.

Default value: **BlurStyle.NONE**

 |
| safeAreaTypes | Array <[SafeAreaType](../../universal-attributes/layout-and-borders/safe-area/document.md#safeareatype)\> | No | Yes | 

Types of the expanded safe areas.

Default value: **\[SafeAreaType.SYSTEM\]**

 |
| safeAreaEdges | Array <[SafeAreaEdge](../../universal-attributes/layout-and-borders/safe-area/document.md#safeareaedge)\> | No | Yes | 

Edges for expanding the safe area.

Default value: **\[SafeAreaEdge.TOP\]**

 |

#### Events

The [universal events](../../universal-events/document.md) are not supported.

#### Example

## Example 1: Implementing an Editable Title Bar with a Custom Right Icon

This example demonstrates how to implement an editable title bar with a left icon, main title, and custom right icon area.

import { EditableLeftIconType, EditableTitleBar, Prompt } from '@kit.ArkUI';

@Entry
@Component
struct Index {
  build() {
    Row() {
      Column() {
        Divider().height(2).color(0xCCCCCC)
        // Cancel button on the left and save button on the right.
        EditableTitleBar({
          leftIconStyle: EditableLeftIconType.Cancel,
          title: 'Edit',
          menuItems: \[\],
          onCancel: () => {
            Prompt.showToast({ message: 'on cancel' });
          },
          onSave: () => {
            Prompt.showToast({ message: 'on save' });
          }
        })
        Divider().height(2).color(0xCCCCCC)
        // Back button on the left, and custom cancel (disabled) and save buttons on the right.
        EditableTitleBar({
          leftIconStyle: EditableLeftIconType.Back,
          title: 'Edit',
          menuItems: \[
            {
              value: $r('sys.media.ohos\_ic\_public\_cancel'),
              isEnabled: false,
              action: () => {
                Prompt.showToast({ message: 'show toast index 2' });
              }
            }
          \],
          onSave: () => {
            Prompt.showToast({ message: 'on save' })
          }
        })
        Divider().height(2).color(0xCCCCCC)
      }.width('100%')
    }.height('100%')
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b8/v3/ObuF9vUPR2SPBzMESD0jSw/en-us_image_0000002537765968.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062250Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=D22BFA0F2662A0B0E11326F5096066DA39350368A9B0CF57072B4311EA2D5EDD)

## Example 2: Implementing an Editable Title Bar with Background Blur and a Profile Picture

This example shows how to implement an editable title bar with background blur, a profile picture, and custom margins.

import { EditableLeftIconType, EditableTitleBar, LengthMetrics, Prompt } from '@kit.ArkUI';

@Entry
@Component
struct Index {
  @State titleBarMargin: LocalizedMargin = {
    start: LengthMetrics.vp(35),
    end: LengthMetrics.vp(35),
  };

  build() {
    Row() {
      Column() {
        EditableTitleBar({
          leftIconStyle: EditableLeftIconType.Cancel,
          title: 'Main title',
          subtitle: 'Subtitle',
          // Set the background blur effect.
          options: {
            backgroundBlurStyle: BlurStyle.COMPONENT\_THICK,
          },
          onSave: () => {
            Prompt.showToast({ message: "on save" });
          },
        })
        Divider().height(2).color(0xCCCCCC);
        EditableTitleBar({
          leftIconStyle: EditableLeftIconType.Cancel,
          title: 'Main title',
          subtitle: 'Subtitle',
          // Remove the save button on the right.
          isSaveIconRequired: false,
        })
        Divider().height(2).color(0xCCCCCC);
        EditableTitleBar({
          leftIconStyle: EditableLeftIconType.Back,
          title: 'Main title',
          subtitle: 'Subtitle',
          isSaveIconRequired: false,
          onCancel: () => {
            this.getUIContext()?.getRouter()?.back();
          },
        })
        Divider().height(2).color(0xCCCCCC);
        EditableTitleBar({
          leftIconStyle: EditableLeftIconType.Back,
          title: 'Main title',
          subtitle: 'Subtitle',
          menuItems: \[
            {
              value: $r('sys.media.ohos\_ic\_public\_remove'),
              isEnabled: true,
              action: () => {
                Prompt.showToast({ message: "show toast index 1" });
              }
            }
          \],
          isSaveIconRequired: false,
          // Action triggered when the Back icon on the left is clicked.
          onCancel: () => {
            this.getUIContext()?.getRouter()?.back();
          },
        })
        Divider().height(2).color(0xCCCCCC);
        EditableTitleBar({
          leftIconStyle: EditableLeftIconType.Back,
          title: 'Main title',
          subtitle: 'Subtitle',
          // Set a clickable profile picture.
          imageItem: {
            value: $r('sys.media.ohos\_ic\_normal\_white\_grid\_image'),
            isEnabled: true,
            action: () => {
              Prompt.showToast({ message: "show toast index 2" });
            }
          },
          // Set the content margin of the title bar.
          contentMargin: this.titleBarMargin,
          // Configure the icon on the right.
          menuItems: \[
            {
              value: $r('sys.media.ohos\_ic\_public\_remove'),
              isEnabled: true,
              action: () => {
                Prompt.showToast({ message: "show toast index 3" });
              }
            }
          \],
          onCancel: () => {
            this.getUIContext()?.getRouter()?.back();
          },
        })
      }
    }
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/77/v3/_6i27BroQUyvypXIAu37sA/en-us_image_0000002537925908.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062250Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=818244DC610A5EBDCBCC6F680F0DA63BF97917A22E64FB337C5D3FB2BD450639)

## Example 3: Implementing Screen Reader Announcement for the Custom Button on the Right Side

This example customizes the screen reader announcement text by setting the **accessibilityText**, **accessibilityDescription**, and **accessibilityLevel** properties of the custom button on the right side of the title bar. This functionality is supported since API version 18.

import { Prompt, EditableLeftIconType, EditableTitleBar } from '@kit.ArkUI';

@Entry
@Component
struct Index1 {
  build() {
    Row() {
      Column() {
        Divider().height(2).color(0xCCCCCC)
        EditableTitleBar({
          leftIconStyle: EditableLeftIconType.Cancel,
          title: 'Edit',
          menuItems: \[\],
          onCancel: () => {
            Prompt.showToast({ message: 'on cancel' });
          },
          onSave: () => {
            Prompt.showToast({ message: 'on save' });
          }
        })
        Divider().height(2).color(0xCCCCCC)
        EditableTitleBar({
          // The profile picture and custom buttons are unavailable.
          leftIconStyle: EditableLeftIconType.Back,
          title: 'Main title',
          subtitle: 'Subtitle',
          imageItem: {
            value: $r('sys.media.ohos\_ic\_normal\_white\_grid\_image'),
            isEnabled: true,
            action: () => {
              Prompt.showToast({ message: "show toast index 1" });
            }
          },
          menuItems: \[
            {
              value: $r('sys.media.ohos\_ic\_public\_remove'),
              label: 'Cancel',
              isEnabled: false,
              accessibilityText: 'Delete',
              accessibilityDescription: 'Tap to delete',
              action: () => {
                Prompt.showToast({ message: "show toast index 2" });
              }
            }
          \],
          onCancel: () => {
            this.getUIContext()?.getRouter()?.back();
          },
        })
        Divider().height(2).color(0xCCCCCC)
      }
    }
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1c/v3/KMIObUQyRSKXX3Heeeixcg/en-us_image_0000002568685685.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062250Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=A2F3D11B1AA30C7FE8CDB6E0338330C1CFD302CAB5F6B8BE0DA3A6A7D9A470E5)

## Example 4: Setting the Left Icon as the Default Focus

This example demonstrates how to set the **leftIconDefaultFocus** property in **EditableTitleBar** to ensure the left icon obtains focus by default in the focused state.

The **leftIconDefaultFocus** API is added to [EditableTitleBar](#editabletitlebar-1) since API version 18.

import { Prompt, EditableLeftIconType, EditableTitleBar } from '@kit.ArkUI';

@Entry
@Component
struct Index {
  build() {
    Column() {
      EditableTitleBar({
        leftIconStyle: EditableLeftIconType.Back,
        leftIconDefaultFocus: true, // Set the left icon as the default focus.
        title: 'Edit',
        menuItems: \[\],
        onSave: () => {
          Prompt.showToast({ message: 'on save' });
        }
      })
    }
    .height('100%')
    .width('100%')
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/64/v3/uxhr9NsTRN2NbStlBmxKEg/en-us_image_0000002568765695.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062250Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=66990ED9CA01F15CC8CBAFD2414F360E1217E8B731EEEAA8898D6F48BF249CD0)

## Example 5: Setting a Custom Right Icon as the Default Focus

This example demonstrates how to set the **leftIconDefaultFocus** property in **EditableTitleBar** to ensure the right icon obtains focus by default in the focused state.

The **defaultFocus** API is added to [EditableTitleBarMenuItem](#editabletitlebarmenuitem) since API version 18.

import { Prompt, EditableLeftIconType, EditableTitleBar } from '@kit.ArkUI';

@Entry
@Component
struct Index {
  build() {
    Column() {
      EditableTitleBar({
        leftIconStyle: EditableLeftIconType.Back,
        title: 'Main title',
        subtitle: 'Subtitle',
        // Configure the icon on the right.
        menuItems: \[
          {
            value: $r('sys.media.ohos\_ic\_public\_remove'),
            isEnabled: true,
            action: () => {
              Prompt.showToast({ message: "show toast index 1" });
            }
          },
          {
            value: $r('sys.media.ohos\_ic\_public\_remove'),
            isEnabled: true,
            defaultFocus: true,
            action: () => {
              Prompt.showToast({ message: "show toast index 2" });
            }
          }
        \],
        onCancel: () => {
          this.getUIContext()?.getRouter()?.back();
        },
      })
    }
    .height('100%')
    .width('100%')
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a6/v3/1-5IiIOKRI2YWIZFdyiTcA/en-us_image_0000002537765970.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062250Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=1AA1C9F11DC7A7C0F6338F8839CD65007FFBAE848BED82D35F0EF78AE532B474)

## Example 6: Setting the Symbol Icon

This example demonstrates how to use **symbolStyle** in **EditableTitleBarMenuItem** to set custom symbol icons. This functionality is supported since API version 18.

import { EditableLeftIconType, EditableTitleBar, Prompt, SymbolGlyphModifier } from '@kit.ArkUI';

@Entry
@Component
struct Index {
  build() {
    Row() {
      Column() {
        Divider().height(2).color(0xCCCCCC)
        EditableTitleBar({
          leftIconStyle: EditableLeftIconType.Cancel,
          title: 'Main title',
          subtitle: 'Subtitle',
          menuItems: \[
            {
              value: $r('sys.symbol.house'),
              isEnabled: true,
              action: () => {
                Prompt.showToast({ message: 'show toast index 2' });
              }
            },
            {
              value: $r('sys.symbol.car'),
              isEnabled: false,
            }
          \],
        })
        Divider().height(2).color(0xCCCCCC)
        EditableTitleBar({
          leftIconStyle: EditableLeftIconType.Back,
          title: 'Main title',
          subtitle: 'Subtitle',
          imageItem: {
            value: $r('sys.media.ohos\_app\_icon'),
            isEnabled: true,
            action: () => {
              Prompt.showToast({ message: "show toast index 1" });
            }
          },
          menuItems: \[
            {
              value: $r('sys.symbol.house'),
              symbolStyle: new SymbolGlyphModifier($r('sys.symbol.bell')).fontColor(\[Color.Red\]),
              isEnabled: true,
              action: () => {
                Prompt.showToast({ message: 'show toast index 2' });
              }
            },
            {
              value: $r('sys.symbol.car'),
              symbolStyle: new SymbolGlyphModifier($r('sys.symbol.heart')).fontColor(\[Color.Blue\]),
              isEnabled: false,
            }
          \],
        })
        Divider().height(2).color(0xCCCCCC)
      }.width('100%')
    }.height('100%')
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3f/v3/02iWHQlfQwCJ6HTq1CAUwA/en-us_image_0000002537925910.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062250Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=E8D436C70133585D14129D417B8F312A259E3AB9BF56FAE888CAB23DC9EED75F)
