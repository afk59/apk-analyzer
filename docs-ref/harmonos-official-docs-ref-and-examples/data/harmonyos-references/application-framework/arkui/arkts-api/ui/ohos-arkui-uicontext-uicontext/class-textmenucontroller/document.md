# Class (TextMenuController)

Provides the capability to control text menus.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/14/v3/OymzRgOQReO4-RGs_GfWCg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062228Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=8B9AACDF6BC52BB1E69EB6824F2AE07CAEF00A7DA7840D7A434F8B956D386A84)

-   The initial APIs of this module are supported since API version 10. Newly added APIs will be marked with a superscript to indicate their earliest API version.
    
-   The initial APIs of this class are supported since API version 16.
    
-   In the following non-static API examples, you must first use [getTextMenuController()](../class-uicontext/document.md#gettextmenucontroller16) in **UIContext** to obtain a **TextMenuController** instance, and then call the APIs using the obtained instance.
    

#### setMenuOptions16+

setMenuOptions(options: TextMenuOptions): void

Sets menu options.

**Atomic service API**: This API can be used in atomic services since API version 16.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| options | [TextMenuOptions](../../../../arkts-components/text-and-input/text-component-common-apis/document.md#textmenuoptions16) | Yes | 
Menu options.

Default value: **{showMode: TextMenuShowMode.DEFAULT}**

 |

**Example**

// xxx.ets
@Entry
@Component
struct Index {
  aboutToAppear(): void {
    // Set the UIContext to preferentially display the context menu on selection in a separate window.
    this.getUIContext()
      .getTextMenuController()
      .setMenuOptions(
        {
          showMode: TextMenuShowMode.PREFER\_WINDOW
        }
      );
  }

  build() {
    Row() {
      Column() {
        TextInput({ text: "This is a TextInput. Long press to display the text selection menu." })
          .height(60)
          .fontStyle(FontStyle.Italic)
          .fontWeight(FontWeight.Bold)
          .textAlign(TextAlign.Center)
          .caretStyle({ width: '4vp' })

        Text("This is a Text. Long press to display the text selection menu.")
          .height(60)
          .copyOption(CopyOptions.InApp)
          .fontStyle(FontStyle.Italic)
          .fontWeight(FontWeight.Bold)
          .textAlign(TextAlign.Center)
      }.width('100%')
    }
    .height('100%')
  }
}

#### disableSystemServiceMenuItems20+

static disableSystemServiceMenuItems(disable: boolean): void

Disables all system service menu items in the text selection menu.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9f/v3/Ewhy5WYBRreRyjeg-2K2Bg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062228Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=84A1821AA71B2EB8F043736A4AB4054ADB198CF304FF6C5420B10FBFA1C3F3FC)

-   This API takes effect globally for the entire application process after being called.
    
-   This API can be used in [UIAbility](../../../../../ability-kit/arkts-apis/stage-model/ohos-app-ability-uiability-ability-with-ui/document.md).
    
-   After this API is called, the [editMenuOptions](../../../../arkts-components/text-and-input/text/document.md#editmenuoptions12) API of text components will be affected. The parameter list of its [onCreateMenu](../../../../arkts-components/text-and-input/text-component-common-apis/document.md#oncreatemenu12) callback will not include the disabled menu options.
    
-   Components involving text selection menus include the following: [Text](../../../../arkts-components/text-and-input/text/document.md), [TextArea](../../../../arkts-components/text-and-input/textarea/document.md), [TextInput](../../../../arkts-components/text-and-input/textinput/document.md), [Search](../../../../arkts-components/text-and-input/search/document.md), [RichEditor](../../../../arkts-components/text-and-input/richeditor/document.md), and [Web](../../../../../arkweb/arkts-components/web/components/document.md).
    
-   System service menu items refer to menu items other than copy, cut, select all, and paste in [TextMenuItemId](../../../../arkts-components/text-and-input/text-component-common-apis/document.md#textmenuitemid12).
    
-   When both **disableSystemServiceMenuItems** and **disableMenuItems** are set, the earlier-set **disableSystemServiceMenuItems** takes precedence.
    
-   This API takes effect globally, and multiple calls are subject to the last call.
    
-   Disabled menus can be restored in the following ways:
    
    -   If only **disableSystemServiceMenuItems(true)** is used to disable menus, set it to **false** to restore.
    -   If only **disableMenuItems** is used to disable menus, set it to an empty array to restore.
    -   If both **disableSystemServiceMenuItems** and **disableMenuItems** are used, set the former to **false** and the latter to an empty array to restore.

**Atomic service API**: This API can be used in atomic services since API version 20.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| disable | boolean | Yes | 
Whether to disable system service menu items. The value **true** means to disable system service menu items, and **false** means the opposite.

Default value: **false**.

 |

**Example**

import { TextMenuController } from '@kit.ArkUI';

// xxx.ets
@Entry
@Component
struct Index {
  aboutToAppear(): void {
    // Disable all system service menu items.
    TextMenuController.disableSystemServiceMenuItems(true)
  }

  aboutToDisappear(): void {
    // Restore system service menu items when the page disappears.
    TextMenuController.disableSystemServiceMenuItems(false)
  }

  build() {
    Row() {
      Column() {
        TextInput({ text: "This is a TextInput. Long press to display the text selection menu." })
          .height(60)
          .fontStyle(FontStyle.Italic)
          .fontWeight(FontWeight.Bold)
          .textAlign(TextAlign.Center)
          .caretStyle({ width: '4vp' })
          .editMenuOptions({
            onCreateMenu: (menuItems: Array<TextMenuItem>) => {
                // menuItems does not contain the disabled system menu items.
                return menuItems
            },
            onMenuItemClick: (menuItem: TextMenuItem, textRange: TextRange) => {
                return false
            }
          })
      }.width('100%')
    }
    .height('100%')
  }
}

#### disableMenuItems20+

static disableMenuItems(items: Array<TextMenuItemId>): void

Disables specified system service menu items in the text selection menu.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2f/v3/dNLqto6vQ3yEuf1gObS7Ng/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062228Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=A9709B0AF8D3C717AB3D59DF48C7F1E29CCDA88E7482B3E2F1F2297137FB6E74)

-   This API takes effect globally for the entire application process after being called.
    
-   This API can be used in [UIAbility](../../../../../ability-kit/arkts-apis/stage-model/ohos-app-ability-uiability-ability-with-ui/document.md).
    
-   After this API is called, the [editMenuOptions](../../../../arkts-components/text-and-input/text/document.md#editmenuoptions12) API of text components will be affected. The parameter list of its [onCreateMenu](../../../../arkts-components/text-and-input/text-component-common-apis/document.md#oncreatemenu12) callback will not include the disabled menu options.
    
-   Components involving text selection menus include the following: [Text](../../../../arkts-components/text-and-input/text/document.md), [TextArea](../../../../arkts-components/text-and-input/textarea/document.md), [TextInput](../../../../arkts-components/text-and-input/textinput/document.md), [Search](../../../../arkts-components/text-and-input/search/document.md), [RichEditor](../../../../arkts-components/text-and-input/richeditor/document.md), and [Web](../../../../../arkweb/arkts-components/web/components/document.md).
    
-   System service menu items refer to menu items other than copy, cut, select all, and paste in [TextMenuItemId](../../../../arkts-components/text-and-input/text-component-common-apis/document.md#textmenuitemid12).
    
-   When both **disableSystemServiceMenuItems** and **disableMenuItems** are set, the earlier-set **disableSystemServiceMenuItems** takes precedence.
    
-   This API takes effect globally, and multiple calls are subject to the last call.
    
-   Disabled menus can be restored in the following ways:
    
    -   If only **disableSystemServiceMenuItems(true)** is used to disable menus, set it to **false** to restore.
    -   If only **disableMenuItems** is used to disable menus, set it to an empty array to restore.
    -   If both **disableSystemServiceMenuItems** and **disableMenuItems** are used, set the former to **false** and the latter to an empty array to restore.

**Atomic service API**: This API can be used in atomic services since API version 20.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| items | Array<[TextMenuItemId](../../../../arkts-components/text-and-input/text-component-common-apis/document.md#textmenuitemid12)\> | Yes | 
List of menu items to disable.

Default value: **\[\]**.

By default, no menu item is disabled.

 |

**Example**

import { TextMenuController } from '@kit.ArkUI';

// xxx.ets
@Entry
@Component
struct Index {
  aboutToAppear(): void {
    // Disable search and translate menu items.
    TextMenuController.disableMenuItems(\[TextMenuItemId.SEARCH, TextMenuItemId.TRANSLATE\])
  }

  aboutToDisappear(): void {
    // Restore system service menu items.
    TextMenuController.disableMenuItems(\[\])
  }

  build() {
    Row() {
      Column() {
        TextInput({ text: "This is a TextInput. Long press to display the text selection menu." })
          .height(60)
          .fontStyle(FontStyle.Italic)
          .fontWeight(FontWeight.Bold)
          .textAlign(TextAlign.Center)
          .caretStyle({ width: '4vp' })
          .editMenuOptions({
            onCreateMenu: (menuItems: Array<TextMenuItem>) => {
                // menuItems does not contain search and translate options.
                return menuItems;
            },
            onMenuItemClick: (menuItem: TextMenuItem, textRange: TextRange) => {
                return false
            }
          })
      }.width('100%')
    }
    .height('100%')
  }
}
