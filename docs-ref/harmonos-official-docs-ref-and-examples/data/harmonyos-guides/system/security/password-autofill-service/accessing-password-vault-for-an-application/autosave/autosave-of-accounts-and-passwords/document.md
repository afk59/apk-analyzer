# Autosave of Accounts and Passwords

Password Vault allows accounts and passwords to be automatically saved in scenarios such as login, registration, and password change.

The saved accounts and passwords can be automatically filled in the corresponding input boxes when users log in to the application next time or change the passwords. Users can view, modify, add notes, and delete the saved accounts and passwords in **Password Vault**.

If the account does not exist in **Password Vault** when the application UI triggers autosave of an account and password, a dialog box will be displayed, asking the user whether to save the username and password. The user can tap **Save** to save the username and password to **Password Vault**.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a3/v3/TqQ0OArZRrmaHXOr_14fuw/en-us_image_0000002185570526.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061959Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=648D04208AF54F8A206B7FD0BAC49143F6FC727F77D205DC4F866D8E8C6C12C1 "Click to enlarge")

Autosave is triggered during account login or registration. The following describes the adaptation in these two scenarios.

**Trigger conditions and precautions:**

1.  The lock screen password has been set, and **Save & autofill** has been enabled in **Password Vault**.
2.  The **enableAutoFill** attribute of the **TextInput** component is set to **true** (default).
3.  Autosave of Password Vault can be used only to save the username and password. Therefore, the UI must have both the username and password input boxes. For details, see [Description of input box types](../../quick-adaptation/document.md#section158542054105219).
    
    The **type** attribute of the **TextInput** component for username input is set to **InputType.USER\_NAME**.
    
    The **type** attribute of the **TextInput** component for password input is set to **InputType.Password** or **InputType.NEW\_PASSWORD**.
    
    **InputType.Password** indicates a common password input box, which is used for entering the password on the login page or entering the old password on the password change page.
    
    **InputType.NEW\_PASSWORD** indicates a new password input box, which is used for entering the new password on the registration page or password change page.
    
4.  The username and password fields cannot be empty or exceed the length limit. The username cannot exceed 128 characters, and the password cannot exceed 256 characters.
5.  Autosave is triggered by page navigation.
6.  The autosave and update functions will not be triggered when there are only two **TextInput** components with **type** set to **InputType.USER\_NAME** and **InputType.Password** and the username and password autofilled in [the password change scenario](../../autofill/autofill-of-accounts-and-passwords/document.md#section7236636819) remain unchanged.

#### Login

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cd/v3/QrNridn9RIShgV4DWnizXg/en-us_image_0000002185410866.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061959Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=B51484207D7AE1EDC477B505BB11E6ED3162B584812683CB1FEE7B9FEE5D33DF "Click to enlarge")

Example:

@Entry
@Component
struct LoginExample {
  pathInfos: NavPathStack = new NavPathStack();
  @State ReserveAccount: string = '';
  @State ReservePassword: string = '';

  @Builder
  PageMap(name: string) {
    if (name === 'home\_page') {
      HomePage()
    }
  }

  build() {
    Navigation(this.pathInfos) {
      Column({ space: 16 }) {
        Text("Account login").commonTitleStyles()

      TextInput({ placeholder: 'Account' })
          .commonInputStyles()
           .type(InputType.USER\_NAME) // The USER\_NAME attribute is used for the username text box.
          .onChange((value: string) => {
            this.ReserveAccount = value;
          })

      TextInput({ placeholder: 'Password' })
          .showPasswordIcon(true)
          .commonInputStyles()
          .type(InputType.Password) // The Password attribute is used for the password text box.
          .onChange((value: string) => {
            this.ReservePassword = value;
          })

        Button('Log in')
          .width('100%')
          .enabled((this.ReserveAccount !== '') && (this.ReservePassword !== ''))
          .onClick(() => {
            this.pathInfos.pushPathByName('home\_page', null)
          })
      }
      .padding(16)
    }
    .navDestination(this.PageMap)
    .height('100%')
    .width('100%')
  }
}

@Component
struct HomePage {
  pathInfos: NavPathStack = new NavPathStack();

  build() {
    NavDestination() {
      Column() {
        Text("Home Page").commonTitleStyles()
      }.width('100%').height('100%')
    }.title("Home Page")
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

#### Registration

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/64/v3/zaqPky22TKykk7Zmcrjauw/en-us_image_0000002220851041.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061959Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=6D28F9CDEC659A251AC7861E06FAE7CC4A16D9312C0E0C71B813767F9E4244CB "Click to enlarge")

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

      TextInput({ placeholder: 'Account' })
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
