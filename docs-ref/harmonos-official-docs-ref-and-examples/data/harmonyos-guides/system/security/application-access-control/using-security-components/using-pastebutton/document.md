# Using PasteButton

The **PasteButton** component comes with the pasteboard (also called clipboard) read privilege, which allows an application to silently read data from the pasteboard.

After the component integrated into your application is tapped, no authorization dialog box will be displayed when your application reads data from the pasteboard. You can use this component for any application that needs to read data from the pasteboard, while eliminating the pop-up windows.

For example, if a user needs to copy a verification code (received from the Messaging application) to another application, the user has to touch and hold the input box, and select **Paste** from the options displayed. With the **PasteButton** component integrated into your application, the user only needs to tap the **Paste** button.

The following figure shows the effect of **PasteButton** component.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/49/v3/zP8p_2S9QDam4c6_3ZWjvg/en-us_image_0000002568684795.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061958Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=1A6A1F4B12E3058305893F02EAD21A855B7CB440B6FA198A9722FECB1F8FFEBA)

#### Constraints

-   The temporary authorization will be automatically revoked when the screen turns off, the application switches to the background, or the application exits.
    
-   During the authorization period, there is no limit on the number of API calls.
    
-   The **PasteButton** component must be visible and legible to users. You need to properly configure the component attributes such as the size and color to prevent authorization failures. If the authorization fails due to invalid component style, check the device error logs.
    

#### How to Develop

The following procedure shows how to make entering a verification code easier: After **Paste** is tapped, the text is pasted to the text box. See the figure above.

1.  Import the dependency **pasteboard**.
    
    import { pasteboard } from '@kit.BasicServicesKit';
    
2.  Add the text boxes and **PasteButton** component.
    
    **PasteButton** is a button-like component consisting of an icon, text, and background. The background is mandatory, and at least one of the icon and text must be selected. The icon and text cannot be customized. You can only select from the existing options.
    
    When declaring the API for creating a security component, you can determine whether to pass in parameters. If no parameter is passed in, a component with default icon, text, and background is created. If parameters are passed in, the component is created based on the specified parameters and elements that are not configured are not contained.
    
    The following example uses the default parameters. For details, see [PasteButton](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ts-security-components-pastebutton). In addition, all security components inherit the [Security Component Universal Attributes](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ts-securitycomponent-attributes), which can be used to customize styles.
    
    import { pasteboard, BusinessError } from '@kit.BasicServicesKit';
    
    @Entry
    @Component
    struct Index {
      @State message: string = '';
    
      build() {
        Row() {
          Column({ space: 10 }) {
            TextInput({ placeholder: $r('app.string.input\_verify\_code'), text: this.message })
              .onChange((val: string) => {
                this.message = val;
              })
            PasteButton()
              .padding({top: 12, bottom: 12, left: 24, right: 24})
              .onClick((event: ClickEvent, result: PasteButtonOnClickResult) => {
                if (PasteButtonOnClickResult.SUCCESS === result) {
                  pasteboard.getSystemPasteboard().getData((err: BusinessError, pasteData: pasteboard.PasteData) => {
                    if (err) {
                      console.error(\`Failed to get paste data. Code is ${err.code}, message is ${err.message}\`);
                      return;
                    }
                    this.message = pasteData.getPrimaryText();
                  });
                }
              })
          }
          .width('100%')
        }
        .height('100%')
      }
    }
