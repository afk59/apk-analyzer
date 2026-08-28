# Autofill of Accounts and Passwords

Password Vault allows autofill of the saved username and password when a user logs in to an application or changes the password.

**Trigger conditions and precautions:**

-   The lock screen password has been set, and **Save & autofill** has been enabled in **Password Vault**.
-   The page has two **TextInput** components, with **type** set to **InputType.USER\_NAME** for username input and to **InputType.password** for common password input.
    
    For details, see [Description of input box types](../../quick-adaptation/document.md#section158542054105219).
    
-   The **enableAutoFill** attribute of the **TextInput** component is set to **true** (default).
-   The username and password of the current application are stored in **Password Vault**.
-   When a user taps the username or password input box for the first time, an autofill dialog box is displayed.

#### Login

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c3/v3/8DFbEDp5RKGBceP1SQG7ew/en-us_image_0000002220851053.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061959Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=B40638F169C910DC8DBB81E6C80D56009B2F6B37091D8D10D95617B16AD186F7 "Click to enlarge")

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
      Column() {
      Text("Account login")
          .commonTitleStyles()

      TextInput({ placeholder: 'Account' })
          .commonInputStyles()
           .type(InputType.USER\_NAME)// The USER\_NAME attribute is used for the username text box.
          .onChange((value: string) => {
            this.ReserveAccount = value;
          })

      TextInput({ placeholder: 'Password' })
          .showPasswordIcon(true)
          .commonInputStyles()
          .type(InputType.Password)// The Password attribute is used for the password text box.
          .onChange((value: string) => {
            this.ReservePassword = value;
          })

        Button('Log in')
          .commonButtonStyles()
          .enabled((this.ReserveAccount !== '') && (this.ReservePassword !== ''))
          .onClick(() => {
            this.pathInfos.pushPathByName('home\_page', null)
          })
      }
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

#### Password Change

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/97/v3/KbrXOiYlTlGZG5AJWY3LqA/en-us_image_0000002220776621.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061959Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=CFFE19B41D99D1476058D5F4B4B1B03338C59E9529667A58C74560C5AE4F652B "Click to enlarge")

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

      TextInput({ placeholder: 'Account' })
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
