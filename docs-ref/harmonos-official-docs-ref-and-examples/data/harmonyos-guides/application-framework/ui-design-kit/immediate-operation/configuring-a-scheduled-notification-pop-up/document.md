# Configuring a Scheduled Notification Pop-up

#### Use Case

The function of configuring a scheduled notification pop-up is available since version 6.0.0(20) Beta1.

The [HdsSnackBar](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ui-design-hdssnackbar) component allows you to configure a scheduled notification pop-up. To do this, call the **show** method of the **HdsSnackBar** component to display the pop-up and set **duration** to a specified period (greater than 0 and default to 5000 milliseconds) after which the pop-up will disappear.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/69/v3/nY7ZNPscRnq0RrriD0Mt3w/en-us_image_0000002532304113.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061957Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=8F23C7CDA6CFC1485CA9B50652C5D0B12388FBEB3BC0FA71FB010F0422480DA3 "Click to enlarge")

#### Development Procedure

1.  Import required modules.
    
    import {
      HdsSnackBar,
      SnackBarIconOptions,
      SnackBarMessageOptions,
      SnackBarOperationOptions,
      SnackBarStyleOptions,
      SnackBarOperationType
    } from '@kit.UIDesignKit'
    
2.  Create the **UIContext**, create an **HdsSnackBar** object, namely, **hdsSnackBar**, and call the **show** method of the **HdsSnackBar** object to display the **HdsSnackBar** pop-up. The input parameters include **icon** (icon on the left), **message** (text displayed in the middle), **operation** (operation area on the right), and **style**. The operation area on the right contains a text button with a right arrow icon. In the **style** attribute, set **duration**, for example, **2000**, indicating that the **HdsSnackBar** pop-up will disappear after two seconds (2000 milliseconds).
3.  You can set **arrowButtonId** and **nextFocusId** to customize the focus shift capability of the tabs.
    
    @Entry
    @ComponentV2
    struct TestSnackBar02 {
      uiContext: UIContext = this.getUIContext();
      hdsSnackBar: HdsSnackBar = new HdsSnackBar(this.uiContext);
      icon: SnackBarIconOptions = {
        icon: $r('sys.symbol.checkmark\_circle')
      }
      message: SnackBarMessageOptions = {
        title: $r('sys.string.ohos\_id\_text\_location\_button\_description\_current\_position'),
        content: $r('sys.string.ohos\_id\_text\_save\_button\_description\_save')
      }
      operation: SnackBarOperationOptions = {
        operationType: SnackBarOperationType.TEXT\_WITH\_ARROW,
        content: $r('sys.string.ohos\_id\_text\_save\_button\_description\_save\_image'),
        arrowButtonId: 'snackBarArrowButton'
      }
      style: SnackBarStyleOptions = {
        nextFocusId: 'button',
        duration: 2000
      }
    
      build() {
        Column() {
          Blank()
            .height(400)
          Button('SnackBar pop-up with a text button and a right arrow icon, which disappears after 2s')
            .onClick(() => {
              this.hdsSnackBar.show(this.icon, this.message, this.operation, this.style);
            })
            .id("button")
    
          Button('Follow')
            .nextFocus({
              // The forward ID must be the same as the **arrowButtonId** passed in **SnackBarOperationOptions**.
              forward: 'snackBarArrowButton'
            })
        }
        .width('100%')
        .height('100%')
        .backgroundColor(0xF1F3F5)
      }
    }
