# Toggle

The **Toggle** component provides a clickable element in the check box, button, or switch type, typically used to switch between two states. For details, see [Toggle](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ts-basic-components-toggle).

#### Creating a Toggle

A toggle is created using [ToggleOptions](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ts-basic-components-toggle#toggleoptions18). The syntax is as follows:

Toggle(options: { type: ToggleType, isOn?: boolean })

In this API, **ToggleType** indicates the toggle type, which can be **Button**, **Checkbox**, or **Switch**, and **isOn** specifies whether the toggle is turned on.

Since API version 11, the default style of the **Checkbox** component is changed from rounded square to circle.

The API can be called in either of the following ways:

-   Create a toggle that does not contain child components.
    
    This can be achieved by calling the API with **ToggleType** set to **Checkbox** or **Switch**.
    
    Toggle({ type: ToggleType.Checkbox, isOn: false }).id('toggle1') // Replace the value of id with the actual ID.
    Toggle({ type: ToggleType.Checkbox, isOn: true }).id('toggle2') // Replace the value of id with the actual ID.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3a/v3/9bdRIGw0SBibxoe4k4qD5w/en-us_image_0000002537764710.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061935Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=E5D31643EFF2D9F5E6AE14AD137425F37A659AE87DAD7BF0850CED9E49309486)
    
    Toggle({ type: ToggleType.Switch, isOn: false }).id('toggle3') // Replace the value of id with the actual ID.
    Toggle({ type: ToggleType.Switch, isOn: true }).id('toggle4') // Replace the value of id with the actual ID.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8f/v3/W2NbhbgRS_yqYCiRvZBaVw/en-us_image_0000002537924650.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061935Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=8C401CC24B126FD5D0D0D5F2A048150557F72B6653F23BC8058519321DA05FDA)
    
-   Create a toggle that contains a child component.
    
    When **ToggleType** is set to **Button**, only one child component is allowed. If the child component has text set, the text content is displayed on the button.
    
    Toggle({ type: ToggleType.Button, isOn: false }) {
      Text('status button')
        .fontColor('#182431')
        .fontSize(12)
    }.width(100).id('toggle5') // Replace the value of id with the actual ID.
    
    Toggle({ type: ToggleType.Button, isOn: true }) {
      Text('status button')
        .fontColor('#182431')
        .fontSize(12)
    }.width(100).id('toggle6') // Replace the value of id with the actual ID.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/64/v3/WaRyVF7BSFmCBz2q6q1knQ/en-us_image_0000002568684427.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061935Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=0E9F7FA707B15DA1F954452E51C60EA4085B60A305C8551601AC08DE598CB5FB)
    

#### Setting Styles

-   Use the **selectedColor** attribute to set the background color of the toggle for when it is turned on.
    
      Toggle({ type: ToggleType.Button, isOn: true }) {
        Text('status button')
          .fontColor('#182431')
          .fontSize(12)
      }.width(100)
      .selectedColor(Color.Pink)
    // ···
    
      Toggle({ type: ToggleType.Checkbox, isOn: true })
        .selectedColor(Color.Pink)
        // ···
      Toggle({ type: ToggleType.Switch, isOn: true })
        .selectedColor(Color.Pink)
        // ···
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/dc/v3/mUQ6BKN-RQCxzq6_fsLk0w/en-us_image_0000002568764437.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061935Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=8FD091894B4D859E106E284672C0A28AB6D517F0044EFDF61D0F637E0F4D3BF4)
    
-   Use the **switchPointColor** attribute to set the color of the circular slider. This attribute is valid only when **type** of the toggle is set to **ToggleType.Switch**.
    
    Toggle({ type: ToggleType.Switch, isOn: false })
      .switchPointColor(Color.Pink)
      // ···
    Toggle({ type: ToggleType.Switch, isOn: true })
      .switchPointColor(Color.Pink)
      // ···
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/37/v3/l6xcPcvqSv-5fT6nHXwKXw/en-us_image_0000002537764712.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061935Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=D792AA63CA2BF689DD375648AC3E5B03FCC3B132498C218D6FD001EFEDBC2BF3)
    

#### Adding Events

The **Toggle** component supports the [universal events](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ts-component-general-events). In addition, it can be bound to the **onChange** event so that it responds with custom behavior after being turned on or off.

Toggle({ type: ToggleType.Switch, isOn: false })
  .onChange((isOn: boolean) => {
    if(isOn) {
      // Operation
      // ···
    }
  })

#### Example Scenario

In this example, the **Toggle** component is used to enable or disable Bluetooth.

// xxx.ets
import { promptAction } from '@kit.ArkUI';

@Entry
@Component
export struct ToggleSample {
  @State message: string = 'off';
  pathStack: NavPathStack = new NavPathStack();

  build() {
    // ...
      Column({ space: 8 }) {
        Column({ space: 8 }) {
          Text('Bluetooth Mode: ' + this.message)
            .id('message')
          Row() {
            Text('Bluetooth')
            Blank()
            Toggle({ type: ToggleType.Switch })
              .id('toggle') // Replace the value of id with the actual ID.
              .onChange((isOn: boolean) => {
                if (isOn) {
                  this.message = 'on';
                  promptAction.openToast({ 'message': 'Bluetooth is on.' });
                } else {
                  this.message = 'off';
                  promptAction.openToast({ 'message': 'Bluetooth is off.' });
                }
              })
          }.width('100%')
        }
        .alignItems(HorizontalAlign.Start)
        .backgroundColor('#fff')
        .borderRadius(12)
        .padding(12)
        .width('100%')
      }
      .width('100%')
      .height('100%')
      .padding({ left: 12, right: 12 })
    // ...
    .backgroundColor('#f1f2f3')
    // Replace $r('app.string.ToggleCaseExample\_title') with the actual resource file. In this example, the value in the resource file is "Bluetooth."
    .title($r('app.string.ToggleCaseExample\_title'))
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0f/v3/tNbqAUC6RwmEO4WQUajhXQ/en-us_image_0000002537924652.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061935Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=2EFA2AD8AA08BB8C7ECD0068FE81A1785411630D4048AA7154F30E4664D48E33)
