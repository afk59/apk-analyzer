# Adaptation Suggestions for Custom Layouts

#### Login

In the login scenario, the input boxes for entering the username/account and password must be on the same page. For details, see [Login](../autosave/autosave-of-accounts-and-passwords/document.md#section13679181143915) and [Login](../autofill/autofill-of-accounts-and-passwords/document.md#section8767438719).

#### Registration

In the registration scenario, the input boxes for entering the username/account and new password must be on the same page. For details, see [Registration](../autosave/autosave-of-accounts-and-passwords/document.md#section1460672643910) and [Registration](../autofill/autofill-of-strong-passwords/document.md#section176891288111).

#### Password Change

In the password change scenario, the input boxes for entering the username/account, old password, and new password must be on the same page. For details, see [Password Change](../autosave/updates-of-accounts-and-passwords/document.md#section1660711384473) and [Password Change](../autofill/autofill-of-accounts-and-passwords/document.md#section7236636819).

#### Login or Registration Failure

When the login or registration is successful, the username and password will be saved to **Password Vault**. If the login or registration fails, the page navigates back via page routing (**router**). It is recommended that the **enableAutofill** attribute be set to **false** to avoid saving incorrect information.

Example:

@Entry
@Component
struct LoginExample {
  pathInfos: NavPathStack = new NavPathStack();
  @State ReserveAccount: string = '';
  @State ReservePassword: string = '';
  // Set the initial value of enAbleAutoFill to true.
  @State enAbleAutoFill: boolean = true;

  onBackPress() {
    // Set enAbleAutoFill to false to disable the autofill feature when navigating back due to unsuccessful login or other transitions.
    this.enAbleAutoFill = false;
    return false;
  }

  @Builder
  PageMap(name: string) {
    if (name === 'home\_page') {
      HomePage()
    }
  }

  build() {
    Navigation(this.pathInfos) {
      Column({ space: 16 }) {
      Text("Account login")
          .commonTitleStyles()

      TextInput({ placeholder: 'Username' })
          .commonInputStyles()
           .type(InputType.USER\_NAME)// The USER\_NAME attribute is used for the username text box.
          .enableAutoFill(this.enAbleAutoFill)// Set the enableAutoFill attributes.
          .onChange((value: string) => {
            this.ReserveAccount = value;
          })

      TextInput({ placeholder: 'Password' })
          .commonInputStyles()
          .showPasswordIcon(true)
          .type(InputType.Password)// The Password attribute is used for the password text box.
          .enableAutoFill(this.enAbleAutoFill)// Set the enableAutoFill attributes.
          .onChange((value: string) => {
            this.ReservePassword = value;
          })

      Button('Log in', { type: ButtonType.Capsule, stateEffect: false })
          .borderRadius(20)
          .width('100%')
          .height(40)
          .enabled((this.ReserveAccount !== '') && (this.ReservePassword !== ''))
          .onClick(() => {
          // Set enAbleAutoFill to true for a successful login to trigger Password Vault.
            this.enAbleAutoFill = true;
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
  .margin({ top: 18 })
}

@Extend(TextInput)
function commonInputStyles() {
  .placeholderColor(0x182431)
  .width('100%')
  .opacity(0.6)
  .placeholderFont({ size: 16, weight: FontWeight.Regular })
}

#### Unsupported Layouts

Except the preceding typical scenarios, the following UI layouts limit the use of Password Vault:

| 
Scenario

 | 

Layout

 | 

Autofill of Accounts and Passwords

 | 

Autofill of Strong Passwords

 | 

Autosave

 |
| :-- | :-- | :-- | :-- | :-- |
| 

Login

 | 

The username and password input boxes are not on the same page.

 | 

Not supported

 | 

Not supported

 | 

Not supported

 |
| 

Verification code login

 | 

Not supported

 | 

Not supported

 | 

Not supported

 |
| 

Registration

 | 

The username and password input boxes are not on the same page.

 | 

Not supported

 | 

Not supported

 | 

Not supported

 |
| 

Password change

 | 

There are only the username and new password input boxes on the page.

 | 

Not supported

 | 

Supported

 | 

Supported

 |
| 

There are only the old password and new password input boxes on the page.

 | 

Not supported

 | 

Not supported

 | 

Not supported

 |
| 

There is only the new password input box on the page.

 | 

Not supported

 | 

Not supported

 | 

Not supported

 |
