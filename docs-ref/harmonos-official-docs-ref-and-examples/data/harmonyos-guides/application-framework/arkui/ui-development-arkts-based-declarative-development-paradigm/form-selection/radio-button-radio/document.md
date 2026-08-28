# Radio Button (Radio)

The **Radio** component allows users to select from a set of mutually exclusive options. Only one radio button in a given group can be selected at the same time. For details, see [Radio](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ts-basic-components-radio).

#### Creating a Radio Button

A radio button is created using the **Radio** component with [RadioOptions](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ts-basic-components-radio#radiooptions). The following example demonstrates how to use the **value** and **group** properties in **RadioOptions**:

Radio(options: {value: string, group: string})

In this API, **value** indicates the name of the radio button, and **group** indicates the name of the group to which the radio button belongs. You can use the **checked** attribute to specify whether the radio button is selected. Setting it to **true** means that the radio button is selected.

In addition, you can customize the style of the radio button for both the selected and unselected states.

Radio({ value: 'Radio1', group: 'radioGroup' })
  .checked(false)
Radio({ value: 'Radio2', group: 'radioGroup' })
  .checked(true)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ab/v3/D_jo_isRQQyj6L9dRnaS5w/en-us_image_0000002568684425.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061934Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=D792A87F4E5A9496B3E9C778FEC6295D29937376E188B08A4725E19017DC4428)

#### Adding Events

The **Radio** component supports the [universal events](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ts-component-general-events). In addition, it can be bound to the **onChange** event to execute custom logic when the selection changes.

Radio({ value: 'Radio1', group: 'radioGroup' })
  .onChange((isChecked: boolean) => {
    if(isChecked) {
      // Operation
      // ···
    }
  })
Radio({ value: 'Radio2', group: 'radioGroup' })
  .onChange((isChecked: boolean) => {
    if(isChecked) {
      // Operation
      // ···
    }
  })

#### Example Scenario

In this example, the **Radio** components are used to switch between sound modes.

// xxx.ets
import { promptAction } from '@kit.ArkUI';

@Entry
@Component
export struct RadioExample {
  @State rst: promptAction.ShowToastOptions = { 'message': 'Ringing mode.' };
  @State vst: promptAction.ShowToastOptions = { 'message': 'Vibration mode.' };
  @State sst: promptAction.ShowToastOptions = { 'message': 'Silent mode.' };

  build() {
    // ···
      Row() {
        Column() {
          Radio({ value: 'Ringing', group: 'radioGroup' }).checked(true)
            .height(50)
            .width(50)
            .onChange((isChecked: boolean) => {
              if (isChecked) {
                // Switch to the ringing mode.
                this.getUIContext().getPromptAction().openToast(this.rst);
              }
            })
          Text('Ringing')
        }

        Column() {
          Radio({ value: 'Vibration', group: 'radioGroup' })
            .height(50)
            .width(50)
            .onChange((isChecked: boolean) => {
              if (isChecked) {
                // Switch to the vibration mode.
                this.getUIContext().getPromptAction().openToast(this.vst);
              }
            })
          Text('Vibration')
        }

        Column() {
          Radio({ value: 'Silent', group: 'radioGroup' })
            .height(50)
            .width(50)
            .onChange((isChecked: boolean) => {
              if (isChecked) {
                // Switch to the silent mode.
                this.getUIContext().getPromptAction().openToast(this.sst);
              }
            })
          Text('Silent')
        }
      }.height('100%').width('100%').justifyContent(FlexAlign.Center)
    // ···
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b6/v3/-E7yYLi4SQe6xxEQrLrPVA/en-us_image_0000002568764435.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061934Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=77220DAE831F84729F5A4957820DDEC69CA41C5414F4066705C7E45A91270478)
