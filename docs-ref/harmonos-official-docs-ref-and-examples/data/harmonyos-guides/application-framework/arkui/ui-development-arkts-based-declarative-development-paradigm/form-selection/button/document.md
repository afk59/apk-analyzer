# Button

The **Button** component is usually activated by user clicks to perform a specific action. It comes in four types: capsule, circle, normal, and rounded rectangle. When used as a container, the **Button** component accepts child components such as text and images. For details, see [Button](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ts-basic-components-button).

#### Creating a Button

You can create a button using the following methods:

-   Creating a button without child components using **label** and [ButtonOptions](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ts-basic-components-button#buttonoptions)
    
    For example, using **type** and **stateEffect** in **ButtonOptions**:
    
    Button(label?: ResourceStr, options?: { type?: ButtonType, stateEffect?: boolean })
    
    In this API, **label** indicates the button text, **type** indicates the button type, and **stateEffect** specifies whether to enable the pressed effect on the click of the button.
    
    Button('Ok', { type: ButtonType.Normal, stateEffect: true })
      .borderRadius(8)
      .backgroundColor(0x317aff)
      .width(90)
      .height(40)
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cb/v3/V7YqpMHCTI-gZUFzOCDDOw/en-us_image_0000002568764425.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061934Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=5F12B9726B861417EF22C182D36A61AC0CC4B6EA3209D355C92388DA3BF77206)
    
-   Creating a button with child components using [ButtonOptions](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ts-basic-components-button#buttonoptions)
    
    For example, using **type** and **stateEffect** in **ButtonOptions**:
    
    Button(options?: {type?: ButtonType, stateEffect?: boolean})
    
    The child component contained can either be a basic component or a container component.
    
    Button({ type: ButtonType.Normal, stateEffect: true }) {
      Row() {
        // Replace $r('app.media.loading') with the actual resource file.
        Image($r('app.media.loading')).width(20).height(40).margin({ left: 12 })
        Text('loading').fontSize(12).fontColor(0xffffff).margin({ left: 5, right: 12 })
      }.alignItems(VerticalAlign.Center)
    }.borderRadius(8).backgroundColor(0x317aff).width(90).height(40)
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/22/v3/wP2aC12aTwKmhS-7LvEBuQ/en-us_image_0000002537764700.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061934Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=97427AD90B8B574ECC057BEA392C4162589461960F239E83D757A8F56B29D30D)
    

#### Setting the Button Type

Buttons comes in four types, set using the **type** parameter: Capsule, Circle, Normal, and ROUNDED\_RECTANGLE.

-   Capsule button (default type)
    
    Buttons of this type have rounded corners whose radius is automatically set to half of the button height. The rounded corners cannot be reset through the **borderRadius** attribute.
    
    Button('Disable', { type: ButtonType.Capsule, stateEffect: false })
      .backgroundColor(0x317aff)
      .width(90)
      .height(40)
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3e/v3/Cbd0-GRXSqKzlSc64e_vsw/en-us_image_0000002537924640.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061934Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=4AC5FA52025DDA89C7DB92D1708986AE5719DEB568A6948D5F40B60CFEFF4702)
    
-   Circle button
    
    Buttons of this type are round. The rounded corners cannot be reset through the **borderRadius** attribute.
    
    Button('Circle', { type: ButtonType.Circle, stateEffect: false })
      .backgroundColor(0x317aff)
      .width(90)
      .height(90)
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c7/v3/iMqqj0kKT0uNKjxCd0vLkg/en-us_image_0000002568684417.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061934Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=96206E9299F5D6A92C5A668E430956FA59CD3DDDCABA4A181E60301847DEDF73)
    
-   Normal button
    
    Buttons of this type have rounded corners set to 0. The rounded corners can be reset through the **borderRadius** attribute.
    
    Button('Ok', { type: ButtonType.Normal, stateEffect: true })
      .borderRadius(8)
      .backgroundColor(0x317aff)
      .width(90)
      .height(40)
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/36/v3/PQLHZotIRimfWUz8mulSmA/en-us_image_0000002568764427.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061934Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=44A0F92A78C14E9A42DD922B27E20453D696DC6F1D9D761784BE1401E53EA7AF)
    
-   Rounded rectangle button
    
    The rounded rectangle button has a default corner radius of 20 vp when [controlSize](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ts-basic-components-button#controlsize11) is **NORMAL**, and 14 vp when [controlSize](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ts-basic-components-button#controlsize11) is **SMALL**. You can define custom corner radius settings through **borderRadius**.
    
    Button('Disable', { type: ButtonType.ROUNDED\_RECTANGLE, stateEffect: true })
      .backgroundColor(0x317aff)
      .width(90)
      .height(40)
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/28/v3/DepuZhahRtm1LJ38PBuV6g/en-us_image_0000002537924640.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061934Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=0C141E99F46AE925D005BCD14E5DD2F7EE4B590B34442EBC5285E785588C8C89)
    

#### Setting Styles

-   Setting the border radius
    
    You can use universal attributes to define the button styles. For example, you can use the **borderRadius** attribute to set the border radius.
    
    Button('circle border', { type: ButtonType.Normal })
      .borderRadius(20)
      .height(40)
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8b/v3/SGujFBkCRNKtFnzv99Y1zg/en-us_image_0000002537764702.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061934Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=1CD7ABD0A07EBAE9EE4389EC6F19D699AB00CADFFC09BD38B323C453F080E847)
    
-   Setting the text style
    
    Add text style attributes for the button.
    
    Button('font style', { type: ButtonType.Normal })
      .fontSize(20)
      .fontColor(Color.Pink)
      .fontWeight(800)
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/24/v3/TJmIQfllRIWekfqa3wY_Tw/en-us_image_0000002537924642.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061934Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=253C34A2212520DBEA76CC1C50D27144703C4E7F49480EC60E0B743F1324BC1A)
    
-   Setting the background color
    
    Add the **backgroundColor** attribute for the button.
    
    Button('background color').backgroundColor(0xF55A42)
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/21/v3/n5INCZZNS0Olt9j0NKMIkw/en-us_image_0000002568684419.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061934Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=67325E1487CFA2B8C4ABE64DAA7D70C31C7E8C89BA2CA761E2041C75753EE051)
    
-   Assigning a function to the button
    
    For example, to create a delete button:
    
    Button({ type: ButtonType.Circle, stateEffect: true }) {
      // Replace $r('app.media.ic\_public\_delete\_filled3') with the actual resource file.
      Image($r('app.media.ic\_public\_delete\_filled')).width(30).height(30)
    }.width(55).height(55).margin({ 'left': 20 }).backgroundColor(0xF55A42)
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/02/v3/YR2X-xfiTAOY75Hr4IJAmw/en-us_image_0000002568764429.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061934Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=A3C3E59EBF83CE5126F1A7D3558AB83123D711191D141A82A18D1B3187D21B18)
    

#### Adding Events

The **Button** component is usually used to trigger actions. You can bind the **onClick** event to the button to have it respond with custom behavior after being clicked.

Button('Ok', { type: ButtonType.Normal, stateEffect: true })
  .onClick(()=>{
    hilog.info(DOMAIN, 'testTag', 'Button onClick');
  }).margin(10)

#### Example

-   Using the button for triggering actions
    
    You can use the button for any UI element that requires user-initiated actions. The button triggers the predefined event based on user interactions. For example, you can use a button in the **List** container to navigate to another page.
    
    const DOMAIN = 0x0000;
    // xxx.ets
    @Entry
    @Component
    export struct ButtonCaseTouch {
      pathStack: NavPathStack = new NavPathStack();
    
      @Builder
      PageMap(name: string) {
        if (name === 'first\_page') {
          pageOneTmp()
        } else if (name === 'second\_page') {
          pageTwoTmp()
        } else if (name === 'third\_page') {
          pageThreeTmp()
        }
      }
    
      build() {
        NavDestination() {
          Navigation(this.pathStack) {
            List({ space: 4 }) {
              ListItem() {
                Button('First').onClick(() => {
                  this.pathStack.pushPath({ name: 'first\_page' });
                })
                  .width('100%')
              }
    
              ListItem() {
                Button('Second').onClick(() => {
                  this.pathStack.pushPath({ name: 'second\_page' });
                })
                  .width('100%')
              }
    
              ListItem() {
                Button('Third').onClick(() => {
                  this.pathStack.pushPath({ name: 'third\_page' });
                })
                  .width('100%')
              }
            }
            .listDirection(Axis.Vertical)
            .backgroundColor(0xDCDCDC).padding(20)
          }
          .mode(NavigationMode.Stack)
          .navDestination(this.PageMap)
        }
      }
    }
    
    // pageOne
    @Component
    export struct pageOneTmp {
      pathStack: NavPathStack = new NavPathStack();
    
      build() {
        NavDestination() {
          Column() {
            Text('first\_page')
          }.width('100%').height('100%')
        }.title('pageOne')
        .onBackPressed(() => {
          const popDestinationInfo = this.pathStack.pop(); // Pop the top element out of the navigation stack.
          // Replace $r('app.string.return\_value') with the actual resource file. In this example, the value in the resource file is "Return value."
          hilog.info(DOMAIN, 'testTag', 'pop' + $r('app.string.return\_value') + JSON.stringify(popDestinationInfo));
          return true;
        })
        .onReady((context: NavDestinationContext) => {
          this.pathStack = context.pathStack;
        })
      }
    }
    
    // pageTwo
    @Component
    export struct pageTwoTmp {
      pathStack: NavPathStack = new NavPathStack();
    
      build() {
        NavDestination() {
          Column() {
            Text('second\_page')
          }.width('100%').height('100%')
        }.title('pageTwo')
        .onBackPressed(() => {
          const popDestinationInfo = this.pathStack.pop(); // Pop the top element out of the navigation stack.
          // Replace $r('app.string.return\_value') with the actual resource file. In this example, the value in the resource file is "Return value."
          hilog.info(DOMAIN, 'testTag', 'pop' + $r('app.string.return\_value') + JSON.stringify(popDestinationInfo));
          return true;
        })
        .onReady((context: NavDestinationContext) => {
          this.pathStack = context.pathStack;
        })
      }
    }
    
    // pageThree
    @Component
    export struct pageThreeTmp {
      pathStack: NavPathStack = new NavPathStack();
    
      build() {
        NavDestination() {
          Column() {
            Text('third\_page')
          }.width('100%').height('100%')
        }.title('pageThree')
        .onBackPressed(() => {
          const popDestinationInfo = this.pathStack.pop(); // Pop the top element out of the navigation stack.
          /// Replace $r('app.string.return\_value') with the actual resource file. In this example, the value in the resource file is "Return value."
          hilog.info(DOMAIN, 'testTag', 'pop' + $r('app.string.return\_value') + JSON.stringify(popDestinationInfo));
          return true;
        })
        .onReady((context: NavDestinationContext) => {
          this.pathStack = context.pathStack;
        })
      }
    }
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7e/v3/RShrYP2pT1eNoZKo1gGjaQ/en-us_image_0000002537764704.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061934Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=7BA11A9A5BE3830889C4BF45DFDA5665982B096500C3E3A083978CE0BA153D31)
    
-   Using the button for submitting forms
    
    On the user login/registration page, you can use a button to submit a login or registration request.
    
    // xxx.ets
    const DOMAIN = 0x0000;
    @Entry
    @Component
    export struct ButtonCaseLogin {
      build() {
        NavDestination() {
          Column() {
            TextInput({ placeholder: 'input your username' }).margin({ top: 20 })
            TextInput({ placeholder: 'input your password' }).type(InputType.Password).margin({ top: 20 })
            Button('Register').width(300).margin({ top: 20 })
              .onClick(() => {
                // Operation
              })
            // ···
          }.padding(20)
        }
      }
    }
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/90/v3/QFF1QZZPRWmC87CiWhe9Kw/en-us_image_0000002537924644.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061934Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=BC8508205974A26F1F76C5F79708CFFD64963F7AC3698FDD113EE31284BDAE6A)
    
-   Configuring the button to float
    
    The button can remain floating when the user swipes on the screen.
    
    // xxx.ets
    @Entry
    @Component
    export struct HoverButtonExample {
      private arr: number\[\] = \[0, 1, 2, 3, 4, 5, 6, 7, 8, 9\];
      build() {
        NavDestination() {
          Stack() {
            List({ space: 20, initialIndex: 0 }) {
              ForEach(this.arr, (item: number) => {
                ListItem() {
                  Text('' + item)
                    .width('100%')
                    .height(100)
                    .fontSize(16)
                    .textAlign(TextAlign.Center)
                    .borderRadius(10)
                    .backgroundColor(0xFFFFFF)
                }
              }, (item: number) => item.toString())
            }.width('90%')
    
            Button() {
              // Replace $r('app.media.ic\_public\_add') with the actual resource file.
              Image($r('app.media.ic\_public\_add'))
               .width(50)
               .height(50)
            }
            .width(60)
            .height(60)
            .position({ x: '80%', y: 600 })
            .shadow({ radius: 10 })
            .onClick(() => {
              // Operation
            })
          }
          .width('100%')
          .height('100%')
          .backgroundColor(0xDCDCDC)
          .padding({ top: 5 })
        }
      }
    }
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/55/v3/s1wjnWcDRpWCNJ_dFxVr0Q/en-us_image_0000002568684421.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061934Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=EE7BB6E3C9B87167EA30C84DC58A8524B39D167AFF08D0E78EE9935647B37DE3)
