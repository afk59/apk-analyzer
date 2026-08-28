# FormMenu

The **FormMenu** component encapsulates an **Add to home screen** menu, which allows users to long-press a component in the application to add it to their home screen for direct access. During application usage, this component acts as a portal for retention and re-engagement, encouraging users to conveniently add features to their home screen.

This component facilitates the quick addition of service widgets to the home screen through a long-press menu within the application:

1.  You pass the widget data and the ID of the in-application functional component to the service widget framework.
    
2.  The click event captures a snapshot and the position of the in-application functional component based on the component ID, which is used for the transition animation when the widget is added to the home screen.
    
3.  The service widget framework triggers the addition of the service widget to the home screen by sending the addition data to the home screen, initiating the service widget placement operation.
    

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/63/v3/GkGD30GUQQGZjSpfPQp5hg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062250Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=D2325549D29DFC3FF6F4E4209EAD8BE947CF7DA63CCF3D08F0FEB52B9CECF88A)

This component is supported since API version 12. Updates will be marked with a superscript to indicate their earliest API version.

This component is not supported on wearables.

For details about how to develop a service widget, see the [service widget development guidelines](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/formkit-overview).

#### Modules to Import

import { AddFormMenuItem } from '@kit.ArkUI';

#### Child Components

Not supported

#### Attributes

The [universal attributes](../../universal-attributes/document.md) are not supported.

#### AddFormMenuItem

AddFormMenuItem(
  want: Want,
  componentId: string,
  options?: AddFormOptions
): void

**Decorator**: @Builder

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| want | [Want](../../../../ability-kit/arkts-apis/both-models-recommended/ohos-app-ability-want-want/document.md#want) | Yes | Want information of the functional component. |
| componentId | string | Yes | In-application functional component ID, which corresponds to a UI similar to the UI of the service widget to add. |
| options | [AddFormOptions](#addformoptions) | No | Options for adding the service widget. |

#### AddFormOptions

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| formBindingData | [formBindingData.FormBindingData](../../../../form-kit/arkts-apis/ohos-app-form-formbindingdata-formbindingdata/document.md#formbindingdata) | No | Yes | Service widget data. |
| callback | AsyncCallback<string> | No | Yes | Callback used to return the result. The value **0** means that the service widget is added successfully, and a non-zero value means that the service widget fails to be added. For details about the error codes, see [Form Error Codes](../../../../form-kit/error-codes/widget-error-codes/document.md). |
| style | [FormMenuItemStyle](#formmenuitemstyle) | No | Yes | Custom menu style. |

#### FormMenuItemStyle

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| options | [MenuItemOptions](../../menus/menuitem/document.md#menuitemoptions) | No | Yes | Information about the menu item. |

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bf/v3/Ox5O6b9aS-CLR2pfEl5-qA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062250Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=5FEE8CC40B1B4E6F625E1A8017AFB9BAA7399022D471012E184DF2ABB0FEF8D3)

If **style** is left empty or unspecified, the default icon and menu text are applied.

#### Events

Menu click events are supported.

#### Example

// index.ets
import { AddFormMenuItem } from '@kit.ArkUI';
import { formBindingData } from '@kit.FormKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

const tag = 'AddFormMenuItem';

@Entry
@Component
struct Index {
  @State message: string = 'Long press show menu';
  private compId: string = 'addforms@d46313145';

  @Builder
  MyMenu() {
    Menu() {
      AddFormMenuItem(
        {
          bundleName: 'com.example.myapplication', // Bundle name
          abilityName: 'EntryFormAbility', // Module ability name.
          parameters: {
            'ohos.extra.param.key.form\_dimension': 2, // Widget size: 1 for 1 x 2, 2 for 2 x 2, 3 for 2 x 4, 4 for 4 x 4, 7 for 6 x 4.
            'ohos.extra.param.key.form\_name': 'widget', // Widget name.
            'ohos.extra.param.key.module\_name': 'entry' // Module name of the widget.
          },
        },
        this.compId,
        {
          formBindingData: formBindingData.createFormBindingData({}),
          // formBindingData: formBindingData.createFormBindingData({ data: 'share' }),
          callback: (error, formId) => {
            hilog.info(0x3900, tag, \`callback info: formId = ${formId}\`);
            if (error?.code === 0) {
              hilog.info(0x3900, tag, "Added to the home screen.")
            } else {
              hilog.error(0x3900, tag, \`Failed to add to the home screen. Try another method. Error code: ${error?.code}, error message: ${error?.message}\`)
            }
          },
          style: {
            // options: {
            // startIcon: $r("app.media.icon"), // Menu icon, which can be provided by yourself. The default value is "sys.media.ic\_public\_add."
            //   content: "Add to home screen",  // Menu content, which can be provided by yourself. The default value is "sys.string.ohos\_add\_form\_to\_desktop."
            //   endIcon: $r("app.media.icon") // Menu icon, which can be provided by yourself.
            // }
          }
        }
      )
    }
  }

  build() {
    Row() {
      Column() {
        Image($r("app.media.startIcon"))   // Custom image.
          .id(this.compId)
          .width(200)
          .height(200)
          .bindContextMenu(this.MyMenu, ResponseType.LongPress, {
            placement: Placement.TopLeft
          })
      }
      .width('100%')
    }
    .height('100%')
  }
}

// WidgetCard.ets
const local = new LocalStorage()

@Entry(local)
@Component
struct WidgetCard {
  @LocalStorageProp('data') data: string = 'defaultdata'; // Define the service widget data to be updated.
  /\*
   \* The action type.
   \*/
  readonly ACTION\_TYPE: string = 'router';
  /\*
   \* The ability name.
   \*/
  readonly ABILITY\_NAME: string = 'EntryAbility';
  /\*
   \* The message.
   \*/
  readonly MESSAGE: string = 'add detail';
  /\*
   \* The width percentage setting.
   \*/
  readonly FULL\_WIDTH\_PERCENT: string = '100%';
  /\*
   \* The height percentage setting.
   \*/
  readonly FULL\_HEIGHT\_PERCENT: string = '100%';

  build() {
    Row() {
      Column() {
        Text(this.data)
          .fontSize($r('app.float.font\_size'))
          .fontWeight(FontWeight.Medium)
          .fontColor($r('app.color.item\_title\_font'))
      }
      .width(this.FULL\_WIDTH\_PERCENT)
    }
    .height(this.FULL\_HEIGHT\_PERCENT)
    .backgroundImage($r('app.media.startIcon'))
    .backgroundImageSize({ width: '100%', height: '100%' })
    .onClick(() => {
      postCardAction(this, {
        action: this.ACTION\_TYPE,
        abilityName: this.ABILITY\_NAME,
        params: {
          message: this.MESSAGE
        }
      });
    })
  }
}

**UI of the FormMenu component**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e3/v3/U4BKFjMtRPysgT7s0HfA5Q/en-us_image_0000002568765707.jpeg?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062250Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=A1984B4D312EECB5218D20243B2BDE8516305033C12A03290D6E834C78AB7B79)

**Result of using Add to home screen with the FormMenu component**

The figure below shows the results when **formbindingdata** is empty (left), and when it is set to **{ data: 'share' }** (right).

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bb/v3/kMOSUQ1ATESXuM0H6dWX3g/en-us_image_0000002537765982.jpeg?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062250Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=F278A221271FEF1ABBEA3EE123E346B55DA3A835930D788BCFC3E1B668CAE5A9)
