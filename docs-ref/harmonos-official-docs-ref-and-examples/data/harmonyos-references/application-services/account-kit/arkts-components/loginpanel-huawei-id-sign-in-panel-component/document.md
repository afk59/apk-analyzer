# LoginPanel (HUAWEI ID Sign-in Panel Component)

This module provides the **LoginPanel** component. You can integrate this component into your app to implement the HUAWEI ID sign-in function.

The **LoginPanel** component must be used with [loginComponentManager](../logincomponentmanager-huawei-id-sign-in-component-management/document.md) to implement the HUAWEI ID sign-in function. The button text in **LoginPanel** supports multiple languages by default.

**Start version**: 4.1.0(11)

#### Module Import

import { LoginPanel, loginComponentManager } from '@kit.AccountKit';

#### LoginPanel

Displays the sign-in panel.

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

show

 | 

boolean

 | 

Yes

 | 

@Link

 | 

Indicates whether to display the **LoginPanel** component.

**false**: no

**true**: yes (used when your service needs to use the **LoginPanel** component)

NOTE:

-   This parameter must be a local variable decorated by @State.
-   **LoginPanel** can be used only on screens. Dialog boxes and sub-windows are not supported.

 |
| 

params

 | 

[LoginPanelParams](../logincomponentmanager-huawei-id-sign-in-component-management/document.md#section29582063177)

 | 

Yes

 | 

\-

 | 

**LoginPanel** component parameters.

 |
| 

controller

 | 

[LoginPanelController](../logincomponentmanager-huawei-id-sign-in-component-management/document.md#section1419019854714)

 | 

Yes

 | 

\-

 | 

**LoginPanel** component controller, which is used to receive tap events in the component.

 |

#### \[h2\]build

build(): void

Constructor used to create a [LoginPanel](#section72281234181611) object.

**Model restriction**: This API can be used only in the stage model.

**System capability**: SystemCapability.AuthenticationServices.HuaweiID.UIComponent

**Start version**: 4.1.0(11)

**Example**:

import { LoginPanel, loginComponentManager } from '@kit.AccountKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct PreviewLoginPanelPage {
  // Indicates whether to display the **LoginPanel** component.
  @State show: boolean = true;
  // Define privacy-related text of the **LoginPanel** component, including the _Privacy Policy_, _User Service Agreement_, and _HUAWEI ID User Authentication Agreement_.
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
  // Define other sign-in icons displayed in the **LoginPanel** component.
  iconArray: loginComponentManager.LoginIcon\[\] = \[{
    // This is a sample icon. You can replace it with a real icon to ensure proper compilation and execution.
    icon: $r('app.media.app\_icon'),
    tag: 'Other sign-in options'
  }\];
  // Construct the controller of **LoginPanel**.
  controller: loginComponentManager.LoginPanelController = new loginComponentManager.LoginPanelController()
    // When the sign-in type is not **QUICK\_LOGIN** and no agreement is set, to display your custom agreement dialog box, set the agreement status to **NOT\_ACCEPTED**.
    .setAgreementStatus(loginComponentManager.AgreementStatus.NOT\_ACCEPTED)
    // Display the privacy policy dialog box when a user taps another sign-in option.
    .setShowAgreementForOptionalLogin()
    .onClickLoginWithHuaweiIDButton((error: BusinessError, response: loginComponentManager.HuaweiIDCredential) => {
      hilog.info(0x0000, 'testTag', 'onClickLoginWithHuaweiIDButton');
      if (error) {
        this.dealAllError(error);
        return;
      }
      if (response) {
        // Send the obtained authorization code to the app server.
        const authorizationCode = response.authorizationCode;
        hilog.info(0x0000, 'testTag', 'Succeeded in getting response.');
        this.show = false;
        return;
      }
    })
    .onClickOptionalLoginButton(() => {
      hilog.info(0x0000, 'testTag', 'onClickOptionalLoginButton');
      this.show = false;
    })
    .onClickOptionalLoginIcon((error: BusinessError, tag: string) => {
      if (error) {
        this.dealAllError(error);
        return;
      }
      hilog.info(0x0000, 'testTag', \`onClickOptionalLoginIcon tag: ${tag}\`);
      this.show = false;
    })
    .onClickPrivacyText((error: BusinessError, tag: string) => {
      if (error) {
        this.dealAllError(error);
        return;
      }
      // The app needs to implement the agreement redirection logic based on **tag**.
      hilog.info(0x0000, 'testTag', \`onClickPrivacyText tag: ${tag}\`);
    })
    .onClickCloseButton(() => {
      hilog.info(0x0000, 'testTag', 'onClickCloseButton');
      this.show = false;
    })
    .onChangeAgreementStatus((error: BusinessError, agreementStatus: loginComponentManager.AgreementStatus) => {
      if (error) {
        this.dealAllError(error);
        return;
      }
      hilog.info(0x0000, 'testTag', \`onChangeAgreementStatus agreementStatus: ${agreementStatus}\`);
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
    if (this.show) {
      Stack() {
        LoginPanel({
          show: this.show,
          params: {
            appInfo: {
              // This is a sample icon. You can replace it with a real icon to ensure proper compilation and execution.
              appIcon: $r('app.media.app\_icon'),
              appName:'App name',
            },
            privacyText: this.privacyText,
            // Obtain the anonymous mobile number by referring to the _Account Kit Development Guide_.
            anonymousPhoneNumber: '139\*\*\*\*\*\*99',
            loginType: loginComponentManager.LoginType.QUICK\_LOGIN,
            // If both **optionalLoginAreaAttr** and **optionalLoginButtonAttr** exist, **optionalLoginAreaAttr** is displayed first.
            optionalLoginAreaAttr: { iconArray: this.iconArray },
            optionalLoginButtonAttr: { text: 'Other sign-in options' }
          },
          controller: this.controller
        })
      }
      .height('100%')
      .width('100%')
    }
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
