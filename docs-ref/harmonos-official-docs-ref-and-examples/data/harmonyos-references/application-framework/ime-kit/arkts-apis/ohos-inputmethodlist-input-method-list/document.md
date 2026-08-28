# @ohos.inputMethodList (Input Method List)

The **inputMethodList** module is oriented to system applications and input method applications. It provides APIs for implementing an input method list. This list displays the default input method subtypes and third-party input methods. Users can use this list to switch from the default input method to another input method.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b9/v3/K549MOGLQJGC5vqGWqHW9g/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062324Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=94C131C460F2C83FE124FC0FB0E1B12E07B7FF4FA0C43799A83D1EA55D89EDED)

This component is supported since API version 11. Updates will be marked with a superscript to indicate their earliest API version.

#### Modules to Import

import { InputMethodListDialog } from '@kit.IMEKit';

#### Child Components

Not supported

#### Attributes

The [universal attributes](../../../arkui/arkts-components/universal-attributes/document.md) are not supported.

#### InputMethodListDialog

InputMethodListDialog({controller: CustomDialogController, patternOptions?: PatternOptions})

Implements a dialog box showing the input method list.

**Decorator type**: @CustomDialog

**System capability**: SystemCapability.MiscServices.InputMethodFramework

**Parameters**

| Name | Type | Mandatory | Decorator | Description |
| :-- | :-- | :-- | :-- | :-- |
| controller | [CustomDialogController](../../../arkui/arkts-components/dialog-boxes/custom-dialog-box-customdialog/document.md#customdialogcontroller) | Yes | \- | Controller for the dialog box showing the input method list. |
| patternOptions | [PatternOptions](#patternoptions) | No | \- | Input method pattern options (for the system input method only). |

#### PatternOptions

**System capability**: SystemCapability.MiscServices.InputMethodFramework

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| defaultSelected | number | No | Yes | Optional. Default selected pattern. |
| patterns | Array<[Pattern](#pattern)\> | No | No | Mandatory. Resource of the pattern option. |
| action | (index: number) => void | No | No | Mandatory. Callback invoked when the pattern option changes. |

#### Pattern

**System capability**: SystemCapability.MiscServices.InputMethodFramework

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| icon | [Resource](../../../arkui/arkts-components/common-definitions/basic-types/document.md#resource) | No | No | Mandatory. Default icon. |
| selectedIcon | [Resource](../../../arkui/arkts-components/common-definitions/basic-types/document.md#resource) | No | No | Mandatory. Icon for the selected option. |

#### Events

The [universal events](../../../arkui/arkts-components/universal-events/document.md) are not supported.

#### Example

import { Pattern, PatternOptions } from '@kit.IMEKit';

@Entry
// Configure the component.
@Component
struct SettingsItem {
  @State defaultPattern: number = 1;
  private oneHandAction: PatternOptions = {
    defaultSelected: this.defaultPattern,
    patterns: \[
      {
        icon: $r('app.media.hand\_icon'),
        selectedIcon: $r('app.media.hand\_icon\_selected')
      },
      {
        icon: $r('app.media.hand\_icon1'),
        selectedIcon: $r('app.media.hand\_icon\_selected1')
      },
      {
        icon: $r('app.media.hand\_icon2'),
        selectedIcon: $r('app.media.hand\_icon\_selected2'),
      }\],
    action:(index: number)=>{
      console.info(\`pattern is changed, current is ${index}\`);
      this.defaultPattern = index;
    }
  };
  private listController: CustomDialogController = new CustomDialogController({
    builder: InputMethodListDialog({ patternOptions: this.oneHandAction }),
    customStyle: true,
    maskColor: '#00000000'
  });

  build() {
    Column() {
      Flex({ direction: FlexDirection.Column,
        alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
        Text("Input Method List").fontSize(20)
      }
    }
    .width("13%")
    .id('bindInputMethod')
    .onClick((event?: ClickEvent) => {
      this.listController.open();
    })
  }
}

Effect

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/21/v3/UbUNnOCNToSCOo9a593KGg/en-us_image_0000002537766376.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062324Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=E019AE04CCBC42CEC04C2ADDF4046C1790F65D1BF9A373F9210533085233E44A)
