# Updates of Accounts and Passwords

During autosave of an account and password, if the same account already exists in **Password Vault**, a dialog box will be displayed, asking the user whether to update password. The user can tap **Update** to update the password for that account in **Password Vault**.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5/v3/Xcs30Fp2Q_mUp0TfOUDGfw/en-us_image_0000002220776609.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061959Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=872E88A6B49F7D6245C618D52023F63B675CBC5D0DB4D49CA3F399061ECA0893 "Click to enlarge")

A password update is triggered when users change a password or manually enter a password for a saved account during login.

For details about the login scenario, see [Login](../autosave-of-accounts-and-passwords/document.md#section13679181143915). The following describes how to change the account password.

The trigger conditions and precautions are the same as those in [Autosave of Accounts and Passwords](../autosave-of-accounts-and-passwords/document.md).

#### Password Change

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a2/v3/4ap3IkBASh-UzWVXXvURmg/en-us_image_0000002220851049.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061959Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=A761F4E2604A1907642082CBDBBE3C4BD9AB2FCE5CB276452106F996D839724C "Click to enlarge")

Example:

@Entry
@Component
struct RegisterExample {
  pathInfos: NavPathStack = new NavPathStack();
  @State ReserveAccount: string = '';
  @State ReservePassword: string = '';
  @State enAbleAutoFill: boolean = true;

  onBackPress() {
    // Set enAbleAutoFill to false to disable the autofill feature when navigating back due to unsuccessful login or other transitions.
    this.enAbleAutoFill = false;
    return false;
  }

  @Builder
  PageMap(name: string) {
    if (name === 'register\_result\_page') {
      RegisterResultPage()
    }
  }

  build() {
    Navigation(this.pathInfos) {
      Column() {
        Text('Change password')
          .commonTitleStyles()

      TextInput({ placeholder: 'Username' })
          .commonInputStyles()
           .type(InputType.USER\_NAME) // The USER\_NAME attribute is used for the username text box.
          .onChange((value: string) => {
            this.ReserveAccount = value;
          })

      TextInput({ placeholder: 'Password' })
          .showPasswordIcon(true)
          .commonInputStyles()
          .type(InputType.Password)
          .onChange((value: string) => {
            this.ReservePassword = value;
          })

      TextInput({ placeholder: 'New password' })
          .showPasswordIcon(true)
          .commonInputStyles()
          .type(InputType.NEW\_PASSWORD) // The NEW\_PASSWORD attribute is used to trigger strong password generation.
          .enableAutoFill(this.enAbleAutoFill)
          .passwordRules('begin:\[upper\],special:\[yes\],len:\[maxlen:32,minlen:12\]')
          .onChange((value: string) => {
            this.ReservePassword = value;
          })

        Button('Page redirection')
          .commonButtonStyles()
          .enabled((this.ReserveAccount !== '') && (this.ReservePassword !== ''))
          .onClick(() => {
            this.pathInfos.pushPathByName('register\_result\_page', null)
          })

        Button('Page redirection(Disable autofill before redirection)')
          .commonButtonStyles()
          .enabled((this.ReserveAccount !== '') && (this.ReservePassword !== ''))
          .onClick(() => {
            this.enAbleAutoFill = false;
            this.pathInfos.pushPathByName('register\_result\_page', null)
          })
      }
    }
    .navDestination(this.PageMap)
    .height('100%')
    .width('100%')
  }
}

@Component
struct RegisterResultPage {
  pathInfos: NavPathStack = new NavPathStack();

  build() {
    NavDestination() {
      Column() {
        Text("Result Page").commonTitleStyles()
      }.width('100%').height('100%')
    }.title("Result Page")
    .onReady((context: NavDestinationContext) => {
      this.pathInfos = context.pathStack;
    })
  }
}

@Extend(Text)
function commonTitleStyles() {
  .fontSize(24)
  .fontColor('#000000')
  .fontWeight(FontWeight.Medium)
  .margin({ top: 24, bottom: 16 })
}

@Extend(TextInput)
function commonInputStyles() {
  .placeholderColor(0x182431)
  .width('100%')
  .opacity(0.6)
  .placeholderFont({ size: 16, weight: FontWeight.Regular })
  .margin({ top: 16 })
}

@Extend(Button)
function commonButtonStyles() {
  .width('100%')
  .height(40)
  .borderRadius(20)
  .margin({ top: 24 })
}
