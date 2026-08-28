# How do I control the display level of CustomDialog?

**Symptom**

A custom dialog box (**CustomDialog**) is displayed on page A. If this dialog box is not closed and the user navigates from page A to page B, the dialog box remains visible above page B instead of being covered by it.

**Solution**

The issue arises because the default layer of **CustomDialog** is higher than the page itself. To resolve this, use the navigation approach, which is designed for page transitions both between pages and within components. With this approach, the page layers are managed by the navigation stack, and by default, the page opened last will appear on top of the previous one. During navigation transition, the system will automatically process the page hierarchy, including all dialog boxes on the previous page. Refer to the code snippet below.

@Component
struct PrivacyDetailPage {
  @State message: string = 'Hello World';

  build() {
    NavDestination() {
      Row() {
        Column() {
          Text(this.message)
            .fontSize(50)
            .fontWeight(FontWeight.Bold)
        }
        .width('100%')
      }
      .height('100%')
    }
    .onBackPressed(() => {
      this.getUIContext().getPromptAction().showToast({ message: '123' });
      return false;
    })
  }
}

@Entry
@Component
struct CustomDialogDisplayLevel {
  // Used for navigation stack management
  @Provide('pageInfos') pageInfos: NavPathStack = new NavPathStack();
  @State textValue: string = 'Input';
  // Visible and hidden control is set to not occupied
  @State visible: Visibility = Visibility.None;

  @Builder
  pageMap(name: string) {
    if (name === 'pageOne') {
      PrivacyDetailPage()
    }
  }

  build() {
    Navigation(this.pageInfos) {
      Column() {
        Stack() {
          Row() {
            Column() {
              Text('I am the first page')
                .fontSize(30)
                .fontWeight(FontWeight.Bold)
              Button('Button')
                .onClick(() => {
                  console.info('hit me!');
                  if (this.visible === Visibility.Visible) {
                    this.visible = Visibility.None;
                  } else {
                    this.visible = Visibility.Visible;
                  }
                })
                .backgroundColor(0x777474)
                .fontColor(0x000000)
            }
            .height('100%')
            .width('100%')
            .justifyContent(FlexAlign.Start)
            .alignItems(HorizontalAlign.Center)
          }
          .height('100%')
          .backgroundColor('#FFF')

          Text('')
            .onClick(() => {
              if (this.visible === Visibility.Visible) {
                this.visible = Visibility.None;
              } else {
                this.visible = Visibility.Visible;
              }
            })
            .width('100%')
            .height('100%')
            // set opacity
            .opacity(0.5)
            .backgroundColor(Color.Black)
            .visibility(this.visible)
          Column() {
            GridRow({
              columns: {
                xs: 1,
                sm: 4,
                md: 8,
                lg: 12
              },
              breakpoints: {
                value: \['400vp', '600vp', '800vp'\],
                reference: BreakpointsReference.WindowSize
              },
            }) {
              GridCol({
                span: {
                  xs: 1,
                  sm: 2,
                  md: 4,
                  lg: 8
                },
                offset: {
                  xs: 0,
                  sm: 1,
                  md: 2,
                  lg: 2
                }
              }) {
                Column() {
                  Text('Privacy')
                    .fontSize(20)
                    .margin({
                      top: 10,
                      bottom: 10
                    })
                  Text('Do you want to jump to the privacy details page?')
                    .fontSize(16)
                    .margin({ bottom: 10 })
                  Flex({ justifyContent: FlexAlign.SpaceAround }) {
                    Button('Cancel')
                      .onClick(() => {
                        if (this.visible === Visibility.Visible) {
                          this.visible = Visibility.None;
                        } else {
                          this.visible = Visibility.Visible;
                        }
                      })
                      .backgroundColor(0xffffff)
                      .fontColor(Color.Black)
                    Button('OK')
                      .onClick(() => {
                        try {
                          this.pageInfos.pushPath({ name: 'pageOne' });
                        } catch (error) {
                          let err = error as BusinessError;
                          hilog.error(0x00, 'PrivacyDetailPage', \`error code: ${err.code},message:${err.message}\`);
                        }
                      })
                      .backgroundColor(0xffffff)
                      .fontColor(Color.Red)
                  }
                  .margin({ bottom: 10 })
                }
                .backgroundColor(0xffffff)
                .visibility(this.visible)
                .clip(true)
                .borderRadius(20)
              }
            }
          }
          // set dialog width
          .width('100%')
        }
      }
      .width('100%')
      .margin({ top: 5 })
    }
    .navDestination(this.pageMap)
  }
}
