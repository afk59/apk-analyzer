# Configuring a Persistent Notification Pop-up

#### Use Case

The function of configuring a persistent notification pop-up is available since version 6.0.0(20) Beta1.

The [HdsSnackBar](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ui-design-hdssnackbar) component allows you to configure a persistent notification pop-up. To do this, call the **show** method of the **HdsSnackBar** component to display the pop-up and set **duration** to **\-1** to make the pop-up displayed in persistent mode.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6d/v3/PFShvngKSB6dAT9kIltj6A/en-us_image_0000002500424088.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061957Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=9913B2C6F982126E4F5CE2813818FD8BC59732F831513981701958DF110EA4DF "Click to enlarge")

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
    
2.  Create the **UIContext**, create an **HdsSnackBar** object, namely, **hdsSnackBar**, and call the **show** method of the **HdsSnackBar** object to display the **HdsSnackBar** pop-up. The input parameters include **icon** (icon on the left), **message** (text displayed in the middle), **operation** (operation area on the right), and **style**. The operation area on the right contains a text button with a close icon. For the **style** attribute, set **duration** to **\-1**, indicating a persistent **HdsSnackBar** pop-up.
3.  You can set **textButtonId** and **nextFocusId** to customize the focus shift capability of the tabs.
    
    @Entry
    @ComponentV2
    struct TestSnackBar {
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
        operationType: SnackBarOperationType.TEXT\_WITH\_CLOSE,
        content: $r('sys.string.ohos\_id\_text\_save\_button\_description\_save\_image'),
        textButtonId: 'snackBarTextButton'
      }
      style: SnackBarStyleOptions = {
        nextFocusId: 'button',
        duration: -1
      }
    
      build() {
        Column() {
          Blank()
            .height(400)
          Button('SnackBar pop-up with a text button and a close icon in the right operation area, persistent')
            .onClick(() => {
              this.hdsSnackBar.show(this.icon, this.message, this.operation, this.style);
            })
            .id("button")
    
          Button('Follow')
            .nextFocus({
              // The forward ID must be the same as the **textButtonId** passed in **SnackBarOperationOptions**.
              forward: 'snackBarTextButton'
            })
        }
        .width('100%')
        .height('100%')
        .backgroundColor(0xF1F3F5)
      }
    }
