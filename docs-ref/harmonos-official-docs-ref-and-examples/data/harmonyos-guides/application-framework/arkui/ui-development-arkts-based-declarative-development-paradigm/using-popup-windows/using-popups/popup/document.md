# Popup

You can bind the **Popup** attribute to a component to create a popup, specifying its content and interaction logic, and display state. It is mainly used for screen recording and message notification.

Popups can be defined with [PopupOptions](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ts-universal-attributes-popup#popupoptions) or [CustomPopupOptions](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ts-universal-attributes-popup#custompopupoptions8). In **PopupOptions**, you can set **primaryButton** and **secondaryButton** to include buttons in the popup. In **CustomPopupOptions**, you can create a custom popup using [builder](../../../basic-syntax-of-ui-paradigms/component-extension/builder-decorator-custom-builder-function/document.md). For **PopupOptions**, the maximum font scale factor is 2.

You can configure the modality of a popup through [mask](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ts-universal-attributes-popup#popupoptions). Setting **mask** to **true** or a color value makes the popup a modal, and setting **mask** to **false** makes the popup a non-modal.

When multiple popups are displayed at the same time, popups displayed in child windows have a higher z-index than those in the main window. When in the same window, popups displayed later have a higher z-index than those displayed earlier.

#### Creating a Text Popup

Text popups are usually used to display informational text messages, suitable for non-interactive scenarios. Bind the **Popup** attribute to a component. When the **show** parameter of **bindPopup** is set to **true**, a popup is displayed.

In the example below, with the **Popup** attribute bound to a **Button** component, each click toggles the boolean value in **handlePopup**. When the value becomes **true**, it triggers **bindPopup** to display the popup.

@Entry
@Component
export struct TextPopupExample {
  @State handlePopup: boolean = false;

  build() {
    NavDestination() {
      Column() {
        Button('PopupOptions')
          .id('PopupOptions')
          .margin({ top: 300 })
          .onClick(() => {
            this.handlePopup = !this.handlePopup;
          })
          .bindPopup(this.handlePopup, {
            message: 'This is a popup with PopupOptions',
          })
      }.width('100%').padding({ top: 5 })
    }
    // ...
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f8/v3/lxAZNNnpQhCe_AL9yVv8Mw/en-us_image_0000002537924680.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061936Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=96E4B5C4D0F7FE215D701FE594B261893C2DB4BCD8379EA5F437E0AF9C7322F2)

#### Adding an Event Listener for Popup State Changes

You can use the **onStateChange** parameter of [PopupOptions](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ts-universal-attributes-popup#popupoptions) to add an event callback for popup state changes, so as to determine the current state of the popup.

@Entry
@Component
export struct StatePopupExample {
  @State handlePopup: boolean = false;

  build() {
    NavDestination() {
        Column() {
          Button('PopupOptions')
            .id('PopupOptions')
            .margin({ top: 300 })
            .onClick(() => {
              this.handlePopup = !this.handlePopup;
            })
            .bindPopup(this.handlePopup, {
              message: 'This is a popup with PopupOptions',
              onStateChange: (e)=> {// Return the current popup state.
                if (!e.isVisible) {
                  this.handlePopup = false;
                }
              }
            })
        }.width('100%').padding({ top: 5 })
    }
    // ...
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6d/v3/zeSwK9pzQ1KkncMydd60fQ/en-us_image_0000002568684457.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061936Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=5A2BCD120FA3174B88B8D0328E56EBE8F956B46BC8EF0B02C40FFA06E92159F2)

#### Creating a Popup with Buttons

You can add a maximum of two buttons to a popup through the **primaryButton** and **secondaryButton** attributes of [PopupOptions](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ts-universal-attributes-popup#popupoptions). For each of the buttons, you can set the action parameter to specify the operation to be triggered.

import { hilog } from '@kit.PerformanceAnalysisKit';

@Entry
@Component
export struct ButtonPopupExample {
  @State handlePopup: boolean = false;

  build() {
    NavDestination() {
        Column() {
          Button('PopupOptions').margin({ top: 300 })
            .id('PopupOptions')
            .onClick(() => {
              this.handlePopup = !this.handlePopup;
            })
            .bindPopup(this.handlePopup, {
              message: 'This is a popup with PopupOptions',
              primaryButton: {
                value: 'Confirm',
                action: () => {
                  this.handlePopup = !this.handlePopup;
                  hilog.info(0xFF00, 'DialogProject', 'confirm Button click');
                }
              },
              secondaryButton: {
                value: 'Cancel',
                action: () => {
                  this.handlePopup = !this.handlePopup;
                }
              },
              onStateChange: (e) => {
                if (!e.isVisible) {
                  this.handlePopup = false;
                }
              }
            })
        }.width('100%').padding({ top: 5 })
    }
    // ...
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b1/v3/uTfbJFf8TzuU7a1UEYOAsA/en-us_image_0000002568764467.jpeg?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061936Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=80511FBE59569C4949A052986DCFF71733BA204AAB7ACA9982CF7705D2062A08)

#### Implementing Popup Animation

You can implement the entrance and exit animation effects of popups through **transition** of [PopupOptions](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ts-universal-attributes-popup#popupoptions) or [CustomPopupOptions](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ts-universal-attributes-popup#custompopupoptions8).

// xxx.ets
@Entry
@Component
export struct AnimationPopupExample {
  @State handlePopup: boolean = false;
  @State customPopup: boolean = false;

  // Define the popup content in the popup builder.
  @Builder
  popupBuilder() {
    Row() {
      Text('Custom Popup with transitionEffect').fontSize(10)
    }.height(50).padding(5)
  }

  build() {
    NavDestination() {
      Flex({ direction: FlexDirection.Column }) {
        // PopupOptions for setting the popup
        Button('PopupOptions')
          .id('PopupOptions')
          .onClick(() => {
            this.handlePopup = !this.handlePopup;
          })
          .bindPopup(this.handlePopup, {
            message: 'This is a popup with transitionEffect',
            placement: Placement.Top,
            showInSubWindow: false,
            onStateChange: (e) => {
              if (!e.isVisible) {
                this.handlePopup = false;
              }
            },
            // Set the popup animation to a combination of opacity and translation effects, with no exit animation.
            transition: TransitionEffect.asymmetric(
              TransitionEffect.OPACITY.animation({ duration: 1000, curve: Curve.Ease }).combine(
                TransitionEffect.translate({ x: 50, y: 50 })),
              TransitionEffect.IDENTITY)
          })
          .position({ x: 100, y: 150 })

        // CustomPopupOptions for setting the popup
        Button('CustomPopupOptions')
          .id('CustomPopupOptions')
          .onClick(() => {
            this.customPopup = !this.customPopup;
          })
          .bindPopup(this.customPopup, {
            builder: this.popupBuilder,
            placement: Placement.Top,
            showInSubWindow: false,
            onStateChange: (e) => {
              if (!e.isVisible) {
                this.customPopup = false;
              }
            },
            // Set the popup entrance and exit animations to be a scaling effect.
            transition: TransitionEffect.scale({ x: 1, y: 0 }).animation({ duration: 500, curve: Curve.Ease })
          })
          .position({ x: 80, y: 300 })
      }.width('100%').padding({ top: 5 })
    }
    // ...
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9e/v3/OziZZaw2Shum5pqFb14Hww/en-us_image_0000002537764742.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061936Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=4D8785D789F74AA979E7EFC80C934F386691A635237F8E8A8E51769C178347E5)

#### Creating a Custom Popup

You can create a custom popup with **builder** in [CustomPopupOptions](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ts-universal-attributes-popup#custompopupoptions8), defining custom content in @Builder. In addition, you can use parameters such as **popupColor** to control the popup style.

// Replace $r('app.media.xxx') with the actual resource file.
@Entry
@Component
export struct CustomPopupExample {
  @State customPopup: boolean = false;

  // Define the popup content in the popup builder.
  @Builder
  popupBuilder() {
    Row({ space: 2 }) {
      Image($r('app.media.app\_icon')).width(24).height(24).margin({ left: 5 })
      Text('This is Custom Popup').fontSize(15)
    }.width(200).height(50).padding(5)
  }

  build() {
    NavDestination() {
        Column() {
          Button('CustomPopupOptions')
            .id('CustomPopupOptions')
            .margin({ top: 300 })
            .onClick(() => {
              this.customPopup = !this.customPopup;
            })
            .bindPopup(this.customPopup, {
              builder: this.popupBuilder, // Content of the popup.
              placement: Placement.Bottom, // Position of the popup.
              popupColor: Color.Pink, // Popup background color
              onStateChange: (e) => {
                if (!e.isVisible) {
                  this.customPopup = false
                }
              }
            })
        }
        .height('100%')
    }
    // ...
  }
}

To place the popup in a specific position, set the **placement** parameter. The popup builder triggers a popup message to instruct the user to complete the operation.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/61/v3/rp4xP_VIQm67dfTYV2fecA/en-us_image_0000002537924682.jpeg?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061936Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=E336D0BF8A850DDD310FD9223EE59D78D07A9114FA1E377766585C2881CD9465)

#### Defining the Popup Style

You can define the popup style using both builder-based customization and through specific API configurations.

Background color: While popups initially come with a transparent background, they have a blur effect, which is **COMPONENT\_ULTRA\_THICK** on phones.

Mask style: Popups come with a default mask that is transparent.

Size: The size of a popup is determined by the content within the builder or the length of the message it holds.

Position: Popups are located below their host component by default. You can control the display position and alignment using the **Placement** attribute of [PopupOptions](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ts-universal-attributes-popup#popupoptions).

The following example demonstrates how to configure a popup's style using **popupColor**, **mask**, **width**, and **placement** of [PopupOptions](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ts-universal-attributes-popup#popupoptions).

// xxx.ets

@Entry
@Component
export struct StylePopupExample {
  @State handlePopup: boolean = false;

  build() {
    NavDestination() {
      Column({ space: 100 }) {
        Button('PopupOptions')
          .onClick(() => {
            this.handlePopup = !this.handlePopup;
          })
          .bindPopup(this.handlePopup, {
            width: 200,
            message: 'This is a popup.',
            popupColor: Color.Red, // Set the background color for the popup.
            mask: {
              color: '#33d9d9d9'
            },
            placement: Placement.Top,
            backgroundBlurStyle: BlurStyle.NONE // Remove the blur effect for the popup.
          })
      }
      .width('100%')
    }
    // ...
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d0/v3/s4oDsDGATIufcs4qQ55pdA/en-us_image_0000002568684459.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061936Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=1802C854942B0684B3D1C7A3663936CFF82AE2D44FF5994E1AAF4852AFB47788)

#### Enabling the Popup to Avoid the Soft Keyboard

By default, popups do not avoid the soft keyboard and may be obscured by it. To enable keyboard avoidance, set **keyboardAvoidMode** (supported since API version 15) of [CustomPopupOptions](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ts-universal-attributes-popup#custompopupoptions8) to **KeyboardAvoidMode.DEFAULT**. If there is insufficient space, the popup will shift from its default position to overlay its host component.

// xxx.ets
@Entry
@Component
export struct AvoidSoftKeyboardPopupExample {
  @State handlePopup: boolean = false;

  @Builder
  popupBuilder() {
    Column({ space: 2 }) {
      Text('Custom Popup').fontSize(20)
        .borderWidth(2)
      TextInput()
    }.width(200).padding(5)
  }

  build() {
    NavDestination() {
      Column({ space: 100 }) {
        TextInput()
        Button('PopupOptions')
          .id('PopupOptions')
          .onClick(() => {
            this.handlePopup = !this.handlePopup;
          })
          .bindPopup(this.handlePopup!!, {
            width: 200,
            builder: this.popupBuilder(),
            placement: Placement.Bottom,
            mask: false,
            autoCancel: false,
            keyboardAvoidMode: KeyboardAvoidMode.DEFAULT
          })
          .position({ x: 100, y: 300 })
      }
      .width('100%')
    }
    // ...
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/aa/v3/IYkScVIeRh-tooniGhWS3A/en-us_image_0000002568764469.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061936Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=988FEB4640B6451BC8F04962C1CE9A0EC502D32B6ED5E8EC7560774EEBAF09B5)

#### Setting Polymorphic Effects in the Popup

When @Builder is used for custom popup content, polymorphic styles are not supported by default. To achieve background color changes on press, implement a component with @Component.

// Replace $r('app.media.xxx') with the actual resource file.
@Entry
@Component
export struct PolymorphicEffectPopupExample {
  // Configure the resource whose name is 'xxx' and value is a non-empty string in the resources\\base\\element\\string.json file.
  @State scan: string =
    this.getUIContext().getHostContext()?.resourceManager.getStringByNameSync('Scan\_title') as string;
  @State createGroupChat: string =
    this.getUIContext().getHostContext()?.resourceManager.getStringByNameSync('Create\_group\_chat') as string;
  @State electronicWorkCard: string =
    this.getUIContext().getHostContext()?.resourceManager.getStringByNameSync('Electronic\_work\_card') as string;
  private menus: Array<string> = \[this.scan, this.createGroupChat, this.electronicWorkCard\];

  // Define the popup content in the popup builder.
  @Builder
  popupItemBuilder(name: string, action: string) {
    PopupItemChild({ childName: name, childAction: action })
  }

  // Define the popup content in the popup builder.
  @Builder
  popupBuilder() {
    Column() {
      ForEach(
        this.menus,
        (item: string, index) => {
          this.popupItemBuilder(item, String(index))
        },
        (item: string, index) => {
          return item
        })
    }
    .padding(8)
  }

  @State customPopup: boolean = false;

  build() {
    NavDestination() {
      Column() {
        Button('click me')
          .id('click me')
          .onClick(() => {
            this.customPopup = !this.customPopup
          })
          .bindPopup(
            this.customPopup,
            {
              builder: this.popupBuilder, // Content of the popup.
              placement: Placement.Bottom, // Position of the popup.
              popupColor: Color.White, // Background color of the popup.
              onStateChange: (event) => {
                if (!event.isVisible) {
                  this.customPopup = false
                }
              }
            })
      }
      .width('100%')
      .justifyContent(FlexAlign.Center)
    }
    // ...
  }
}

@Component
struct PopupItemChild {
  @Prop childName: string = '';
  @Prop childAction: string = '';
  @State selected: string =
    this.getUIContext().getHostContext()?.resourceManager.getStringByNameSync('Selected') as string;

  build() {
    Row({ space: 8 }) {
      Image($r('app.media.startIcon'))
        .width(24)
        .height(24)
      Text(this.childName)
        .fontSize(16)
    }
    .width(130)
    .height(50)
    .padding(8)
    .onClick(() => {
      this.getUIContext().getPromptAction().showToast({ message: this.selected + this.childName })
    })
    .stateStyles({
      normal: {
        .backgroundColor(Color.White)
      },
      pressed: {
        .backgroundColor('#d4f1ff')
      }
    })
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4d/v3/3YmrEywMRR6aoivFGJzZqQ/en-us_image_0000002537764744.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061936Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=7BB16D484BA0295BA3F0A9A6D9F13CEADB667C3E3CADB21FFED89D7556B439DF)

#### Implementing Axis Avoidance

Since API version 18, popups support center axis avoidance. Since API version 20, it is enabled by default on 2-in-1 devices (avoidance only occurs when the window is in waterfall mode). You can control whether to enable axis avoidance through the **enableHoverMode** property in [PopupOptions](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ts-universal-attributes-popup#popupoptions).

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/85/v3/CaObgOyhTWCCF4pzp9VG_g/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061936Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=BE0D04D4B115E58A32A3FF64A8715EB46E1DBCCD31E635D1E4F1373C55AFDF08)

-   Popups will not avoid the center axis if clicked in the axis area.
-   On 2-in-1 devices, axis avoidance occurs only when the window is in waterfall mode.

@Entry
@Component
export struct SupportedAvoidAxisPopupExample {
  // Configure the resource whose name is 'xxx' and value is a non-empty string in the resources\\base\\element\\string.json file.
  @State upScreen: string =
    this.getUIContext().getHostContext()?.resourceManager.getStringByNameSync('Upper\_half\_screen') as string;
  @State middleAxle: string =
    this.getUIContext().getHostContext()?.resourceManager.getStringByNameSync('Middle\_axle') as string;
  @State lowerScreen: string =
    this.getUIContext().getHostContext()?.resourceManager.getStringByNameSync('Lower\_half\_screen') as string;
  @State subwindowDisplay: string =
    this.getUIContext().getHostContext()?.resourceManager.getStringByNameSync('Subwindow\_display') as string;
  @State subwindow: string =
    this.getUIContext().getHostContext()?.resourceManager.getStringByNameSync('Subwindow') as string;
  @State nonSubwindow: string =
    this.getUIContext().getHostContext()?.resourceManager.getStringByNameSync('Non\_Subwindow') as string;
  @State zone: string =
    this.getUIContext().getHostContext()?.resourceManager.getStringByNameSync('zone') as string;
  @State hoverModeStart: string =
    this.getUIContext().getHostContext()?.resourceManager.getStringByNameSync('hoverMode\_start') as string;

  @State message: string = 'Hello World';
  @State index: number = 0;
  @State arrayStr: Array<string> = \[this.upScreen, this.middleAxle, this.lowerScreen\];
  @State enableHoverMode: boolean | undefined = true;
  @State showInSubwindow: boolean = false;
  @State placement: Placement | undefined = undefined;
  @State isShow: boolean = false;

  build() {
    NavDestination() {
      RelativeContainer() {
        Column() {
          Button(this.zone + this.arrayStr\[this.index\])
            .onClick(() => {
              if (this.index < 2) {
                this.index++
              } else {
                this.index = 0
              }
            })

          Button(this.subwindowDisplay + (this.showInSubwindow ? this.subwindow : this.nonSubwindow))
            .onClick(() => {
              this.showInSubwindow = !this.showInSubwindow
            })

          Button(this.hoverModeStart + this.enableHoverMode)
            .onClick(() => {
              if (this.enableHoverMode === undefined) {
                this.enableHoverMode = true
              } else if (this.enableHoverMode === true) {
                this.enableHoverMode = false
              } else {
                this.enableHoverMode = undefined
              }
            })
        }

        Row() {
          Button('Popup')
            .id('Popup')
            .fontWeight(FontWeight.Bold)
            .bindPopup(this.isShow, {
              message: 'popup',
              enableHoverMode: this.enableHoverMode,
              showInSubWindow: this.showInSubwindow,
            })
            .onClick(() => {
              this.isShow = !this.isShow
            })
        }
        .alignRules({
          center: { anchor: '\_\_container\_\_', align: VerticalAlign.Center },
          middle: { anchor: '\_\_container\_\_', align: HorizontalAlign.Center }
        })
        .margin({
          top: this.index === 2 ? 330 : this.index === 1 ? 50 : 0,
          bottom: this.index === 0 ? 330 : 0
        })
      }
      .height('100%')
      .width('100%')
    }
    // ...
  }
}
