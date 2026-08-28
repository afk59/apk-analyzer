# LoginWithHuaweiIDButton (HUAWEI ID Sign-in Button Component)

This module provides the **LoginWithHuaweiIDButton** component. You can integrate this component into your app to implement the HUAWEI ID sign-in function.

The **LoginWithHuaweiIDButton** component must be used with [loginComponentManager](../logincomponentmanager-huawei-id-sign-in-component-management/document.md) to implement the HUAWEI ID sign-in function. The text content of the **LoginWithHuaweiIDButton** component supports multiple languages by default.

**Start version**: 4.1.0(11)

#### Module Import

import { LoginWithHuaweiIDButton, loginComponentManager } from '@kit.AccountKit';

#### LoginWithHuaweiIDButton

Displays the HUAWEI ID sign-in button.

**Model restriction**: This API can be used only in the stage model.

**Decorator type**: @Component

**System capability**: SystemCapability.AuthenticationServices.HuaweiID.UIComponent

**Start version**: 4.1.0(11)

**Parameters**:

| 
Name

 | 

Type

 | 

Mandatory

 | 

Decorator Type

 | 

Description

 |
| :-- | :-- | :-- | :-- | :-- |
| 

params

 | 

[LoginWithHuaweiIDButtonParams](../logincomponentmanager-huawei-id-sign-in-component-management/document.md#section4717249182518)

 | 

Yes

 | 

\-

 | 

**LoginWithHuaweiIDButton** component parameters.

 |
| 

controller

 | 

[LoginWithHuaweiIDButtonController](../logincomponentmanager-huawei-id-sign-in-component-management/document.md#section6921622144614)

 | 

Yes

 | 

\-

 | 

**LoginWithHuaweiIDButton** component controller, which is used to receive tap events in the component.

 |

#### \[h2\]build

build(): void

Constructor used to create a [LoginWithHuaweiIDButton](#section1624716107193) object.

**Model restriction**: This API can be used only in the stage model.

**System capability**: SystemCapability.AuthenticationServices.HuaweiID.UIComponent

**Start version**: 4.1.0(11)

**Example**:

import { loginComponentManager, LoginWithHuaweiIDButton } from '@kit.AccountKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

@Entry
@Component
struct QuickLoginButtonComponent {
  logTag: string = 'QuickLoginButtonComponent';
  domainId: number = 0x0000;
  // Obtain the anonymous mobile number by referring to the _Account Kit Development Guide_.
  @State quickLoginAnonymousPhone: string = '';
  // Display the _Privacy Policy_, _User Service Agreement_, and _HUAWEI ID User Authentication Agreement_.
  privacyText: loginComponentManager.PrivacyText\[\] = \[{
    text: 'I have read and agree to the',
    type: loginComponentManager.TextType.PLAIN\_TEXT
  }, {
    text: 'User Service Agreement',
    tag: 'User Service Agreement',
    type: loginComponentManager.TextType.RICH\_TEXT
  }, {
    text: 'Privacy Policy',
    tag: 'Privacy Policy',
    type: loginComponentManager.TextType.RICH\_TEXT
  }, {
    text: 'and',
    type: loginComponentManager.TextType.PLAIN\_TEXT
  }, {
    text: 'HUAWEI ID User Authentication Agreement',
    tag: 'HUAWEI ID User Authentication Agreement',
    type: loginComponentManager.TextType.RICH\_TEXT
  }\];
  // Construct the controller of **LoginWithHuaweiIDButton**.
  controller: loginComponentManager.LoginWithHuaweiIDButtonController =
    new loginComponentManager.LoginWithHuaweiIDButtonController()
      /\*\*
       \* For an app with a custom sign-in UI, if the user does not accept the agreements, set the agreement status to **NOT\_ACCEPTED**.
       \* Set the agreement status to **ACCEPTED** once the user accepts the agreements. The one-tap HUAWEI ID sign-in function is available only when the agreement status is **ACCEPTED**.
       \*/
      .setAgreementStatus(loginComponentManager.AgreementStatus.NOT\_ACCEPTED)
      .onClickLoginWithHuaweiIDButton((error: BusinessError, response: loginComponentManager.HuaweiIDCredential) => {
        if (error) {
          this.dealAllError(error);
          return;
        }
        if (response) {
          // Obtain the authorization code.
          const authorizationCode = response.authorizationCode;
          hilog.info(0x0000, 'testTag', 'Succeeded in getting response.');
          return;
        }
      })
      .onClickEvent((error: BusinessError, clickEvent: loginComponentManager.ClickEvent) => {
        if (error) {
          this.dealAllError(error);
          return;
        }
        hilog.info(0x0000, 'testTag', \`onClickEvent clickEvent: ${clickEvent}\`);
      });

  // Handle the error.
  dealAllError(error: BusinessError): void {
    hilog.error(0x0000, 'testTag', \`Failed to login, errorCode=${error.code}, errorMsg=${error.message}\`);
    // In sign-in scenarios involving UI interactions, it is advised to guide users with the following error code prompts:
    if (error.code === ErrorCode.ERROR\_CODE\_LOGIN\_OUT) {
      // HUAWEI ID not signed in. Use a HUAWEI ID to sign in and try again, or sign in to the app in another way.
    } else if (error.code === ErrorCode.ERROR\_CODE\_NETWORK\_ERROR) {
      // A network exception occurs. Check the current network status and try again, or sign in to the app in another way.
    } else if (error.code === ErrorCode.ERROR\_CODE\_INTERNAL\_ERROR) {
      // Failed to sign in. Try another way.
    } else if (error.code === ErrorCode.ERROR\_CODE\_USER\_CANCEL) {
      // Authorization canceled.
    } else if (error.code === ErrorCode.ERROR\_CODE\_SYSTEM\_SERVICE) {
      // System service exception. Try again later or sign in to the app in another way.
    } else if (error.code === ErrorCode.ERROR\_CODE\_REQUEST\_REFUSE) {
      // Repeated request. No further action is needed.
    } else if (error.code === ErrorCode.ERROR\_CODE\_AGREEMENT\_STATUS\_NOT\_ACCEPTED) {
      // The user does not accept the agreements.
    } else {
      // Failed to sign in. Try another way.
    }
  }

  build() {
    Scroll() {
      Column() {
        Column() {
          Column() {
            // This is a sample icon. You can replace it with a real icon to ensure proper compilation and execution.
            Image($r('app.media.app\_icon'))
              .width(48)
              .height(48)
              .draggable(false)
              .copyOption(CopyOptions.None)
              .onComplete(() => {
                hilog.info(0x0000, 'testTag', 'appIcon loading success');
              })
              .onError(() => {
                hilog.error(0x0000, 'testTag', 'appIcon loading fail');
              })

            Text($r('app.string.app\_name'))
              .fontFamily($r('sys.string.ohos\_id\_text\_font\_family\_medium'))
              .fontWeight(FontWeight.Medium)
              .fontWeight(FontWeight.Bold)
              .maxFontSize($r('sys.float.ohos\_id\_text\_size\_headline8'))
              .minFontSize($r('sys.float.ohos\_id\_text\_size\_body1'))
              .maxLines(1)
              .fontColor($r('sys.color.ohos\_id\_color\_text\_primary'))
              .constraintSize({ maxWidth: '100%' })
              .margin({
                top: 12,
              })

            Text('App description')
              .fontSize($r('sys.float.ohos\_id\_text\_size\_body2'))
              .fontColor($r('sys.color.ohos\_id\_color\_text\_secondary'))
              .fontFamily($r('sys.string.ohos\_id\_text\_font\_family\_regular'))
              .fontWeight(FontWeight.Regular)
              .constraintSize({ maxWidth: '100%' })
              .margin({
                top: 8,
              })
          }.margin({
            top: 100
          })

          Column() {
            Text(this.quickLoginAnonymousPhone)
              .fontSize(36)
              .fontColor($r('sys.color.ohos\_id\_color\_text\_primary'))
              .fontFamily($r('sys.string.ohos\_id\_text\_font\_family\_medium'))
              .fontWeight(FontWeight.Bold)
              .lineHeight(48)
              .textAlign(TextAlign.Center)
              .maxLines(1)
              .constraintSize({ maxWidth: '100%', minHeight: 48 })

            Text('Mobile number bound to a HUAWEI ID')
              .fontSize($r('sys.float.ohos\_id\_text\_size\_body2'))
              .fontColor($r('sys.color.ohos\_id\_color\_text\_secondary'))
              .fontFamily($r('sys.string.ohos\_id\_text\_font\_family\_regular'))
              .fontWeight(FontWeight.Regular)
              .lineHeight(19)
              .textAlign(TextAlign.Center)
              .maxLines(1)
              .constraintSize({ maxWidth: '100%' })
              .margin({
                top: 8
              })
          }.margin({
            top: 64
          })

          Column() {
            LoginWithHuaweiIDButton({
              params: {
                // Styles supported by **LoginWithHuaweiIDButton**.
                style: loginComponentManager.Style.BUTTON\_RED,
                // The one-tap HUAWEI ID sign-in button is in loading state during user sign-in.
                extraStyle: {
                  buttonStyle: new loginComponentManager.ButtonStyle().loadingStyle({
                    show: true
                  })
                },
                // Rounded corner radius of **LoginWithHuaweiIDButton**.
                borderRadius: 24,
                // Sign-in types supported by **LoginWithHuaweiIDButton**.
                loginType: loginComponentManager.LoginType.QUICK\_LOGIN,
                // The button style of **LoginWithHuaweiIDButton** supports switching along with the change between light and dark modes of the device system.
                supportDarkMode: true
              },
              controller: this.controller
            })
          }
          .height(40)
          .width('100%')
          .margin({
            top: 56
          })

          Column() {
            Button({
              type: ButtonType.Capsule,
              stateEffect: true
            }) {
            Text('Other sign-in options')
                .fontColor($r('sys.color.ohos\_id\_color\_text\_primary\_activated'))
                .fontFamily($r('sys.string.ohos\_id\_text\_font\_family\_medium'))
                .fontWeight(FontWeight.Medium)
                .fontSize($r('sys.float.ohos\_id\_text\_size\_button1'))
                .focusable(true)
                .focusOnTouch(true)
                .textOverflow({ overflow: TextOverflow.Ellipsis })
                .maxLines(1)
                .padding({ left: 8, right: 8 })
            }
            .fontColor($r('sys.color.ohos\_id\_color\_text\_primary\_activated'))
            .fontFamily($r('sys.string.ohos\_id\_text\_font\_family\_medium'))
            .fontWeight(FontWeight.Medium)
            .backgroundColor($r('sys.color.ohos\_id\_color\_button\_normal'))
            .focusable(true)
            .focusOnTouch(true)
            .constraintSize({ minHeight: 40 })
            .width('100%')
            .onClick(() => {
              hilog.info(this.domainId, this.logTag, 'click optionalLoginButton.');
            })
          }.margin({ top: 16 })
        }.width('100%')

        Row() {
          Row() {
            Checkbox({ name: 'privacyCheckbox', group: 'privacyCheckboxGroup' })
              .width(24)
              .height(24)
              .focusable(true)
              .focusOnTouch(true)
              .margin({ top: 0 })
              .onChange((value: boolean) => {
                if (value) {
                  this.controller.setAgreementStatus(loginComponentManager.AgreementStatus.ACCEPTED);
                } else {
                  this.controller.setAgreementStatus(loginComponentManager.AgreementStatus.NOT\_ACCEPTED);
                }
                hilog.info(0x0000, 'testTag', \`agreementChecked: ${value}\`);
              })
          }

          Row() {
            Text() {
              ForEach(this.privacyText, (item: loginComponentManager.PrivacyText) => {
                if (item?.type === loginComponentManager.TextType.PLAIN\_TEXT && item?.text) {
                  Span(item?.text)
                    .fontColor($r('sys.color.ohos\_id\_color\_text\_secondary'))
                    .fontFamily($r('sys.string.ohos\_id\_text\_font\_family\_regular'))
                    .fontWeight(FontWeight.Regular)
                    .fontSize($r('sys.float.ohos\_id\_text\_size\_body3'))
                } else if (item?.type === loginComponentManager.TextType.RICH\_TEXT && item?.text) {
                  Span(item?.text)
                    .fontColor($r('sys.color.ohos\_id\_color\_text\_primary\_activated'))
                    .fontFamily($r('sys.string.ohos\_id\_text\_font\_family\_medium'))
                    .fontWeight(FontWeight.Medium)
                    .fontSize($r('sys.float.ohos\_id\_text\_size\_body3'))
                    .onClick(() => {
                      // The app needs to implement the agreement redirection logic based on **item.tag**.
                      hilog.info(0x0000, 'testTag', \`click privacy text tag: ${item.tag}\`);
                    })
                }
              }, (item: loginComponentManager.PrivacyText) => item.text.toString())
            }
            .width('100%')
          }
          .margin({ left: 12 })
          .layoutWeight(1)
          .constraintSize({ minHeight: 24 })
        }
        .alignItems(VerticalAlign.Top)
        .margin({
          top: 16,
          bottom: 16
        })
      }
      .justifyContent(FlexAlign.SpaceBetween)
      .constraintSize({ minHeight: '100%' })
      .margin({
        left: 16,
        right: 16
      })
    }
    .width('100%')
    .height('100%')
  }
}

export enum ErrorCode {
  // The HUAWEI ID is not signed in.
  ERROR\_CODE\_LOGIN\_OUT = 1001502001,
  // Network error.
  ERROR\_CODE\_NETWORK\_ERROR = 1001502005,
  // Internal error.
  ERROR\_CODE\_INTERNAL\_ERROR = 1001502009,
  // Authorization canceled.
  ERROR\_CODE\_USER\_CANCEL = 1001502012,
  // System service error.
  ERROR\_CODE\_SYSTEM\_SERVICE = 12300001,
  // The user does not accept the agreements.
  ERROR\_CODE\_AGREEMENT\_STATUS\_NOT\_ACCEPTED = 1005300001,
  // Repeated request.
  ERROR\_CODE\_REQUEST\_REFUSE = 1001500002
}
