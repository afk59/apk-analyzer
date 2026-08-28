# Autofill of Strong Passwords

Password Vault allows a strong password to be automatically generated when a user needs to enter a new password. When the user chooses to use the generated strong password, the password is automatically filled in the new password input box.

**Trigger conditions and precautions:**

-   The lock screen password has been set, and **Save & autofill** has been enabled in **Password Vault**.
-   The page has two **TextInput** components, with **type** set to **InputType.USER\_NAME** for username input and to **InputType.NEW\_PASSWORD** for new password input.
    
    For details, see [Description of input box types](../../quick-adaptation/document.md#section158542054105219).
    
-   The **enableAutoFill** attribute of the **TextInput** component is set to **true** (default).
-   When a user taps the new password input box for the first time, a strong password dialog box is displayed. The user can tap the **Use suggested password** button to automatically fill the recommended strong password in the new password input box.
-   You can define [the rules for generating strong passwords](../suggestions-on-automatically-generating-strong-passwords-for-applications/document.md).

#### Registration

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ad/v3/fXHHU0KpSk-B1Is5iu39OQ/en-us_image_0000002185570530.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061959Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=AAB544C79F3E7E669AF2F17193ED1D0F9A63CB499C32E9966EBB87708A627D7F "Click to enlarge")

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
        Text('Register account')
          .commonTitleStyles()

      TextInput({ placeholder: 'Username' })
          .commonInputStyles()
          .type(InputType.USER\_NAME) // The USER\_NAME attribute is used for the username text box.
          .onChange((value: string) => {
            this.ReserveAccount = value;
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

#### Password Change

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/92/v3/HP31P2jlQhCm1xJVc1AYiw/en-us_image_0000002185410870.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061959Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=1B41F2CD816F5FD8444BCE0B0C8B0DF7124A961CDA360A705029161B32AFE42A "Click to enlarge")

Example:

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
