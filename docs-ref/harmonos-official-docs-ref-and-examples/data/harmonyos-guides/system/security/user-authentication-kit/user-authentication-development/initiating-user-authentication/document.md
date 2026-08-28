# Initiating User Authentication

A user authentication is required before an application accesses a critical functionality or sensitive data. This topic walks you through the process.

#### Available APIs

For details about the parameters, return values, and error codes, see [User Authentication](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-useriam-userauth#userauthgetuserauthinstance10).

| API | Description |
| :-- | :-- |
| getUserAuthInstance(authParam: AuthParam, widgetParam: WidgetParam): UserAuthInstance | Obtains the **UserAuthInstance** object to perform user identity authentication and support the use of the [unified user authentication widget](#unified-user-authentication-widget-introduction). |
| on(type: 'result', callback: IAuthCallback): void | Subscribes to the user authentication result. |
| off(type: 'result', callback?: IAuthCallback): void | Unsubscribes from the user authentication result. |
| start(): void | Starts user authentication. |

#### Unified User Authentication Widget Introduction

The system provides a unified user authentication widget, which stands out with following features:

-   The user authentication widget identifies and authenticates user information and returns the authentication result to the application. The overall process is secure and controllable.
    
-   The widget comes with a unified UI component style to elevate user experience.
    

The following figure shows the style of the user authentication widget, which can be set via the [WidgetParam](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-useriam-userauth#widgetparam10) parameter.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c5/v3/HxhrjmRuRM2BMBub56S6Cw/en-us_image_0000002568684805.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062013Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=6FECDD416DC49293478AE363EF26FB7C26987C528AC4878271CB3614DD771A3A)

-   ①: Title (**WidgetParam.title**) of the user authentication page, which cannot be empty or exceed 500 characters. You are advised to set the title to the authentication purpose, for example, payment and application login.
    
-   ②: If biometric authentication fails, a button is displayed. The user can tap the button to switch to another authentication type (AuthParam.authType).
    
    If you want to [apply custom authentication](../applying-custom-authentication/document.md), configure the text on the navigation button (WidgetParam.navigationButtonText), which cannot exceed 60 characters. It can be configured only in single fingerprint or facial authentication scenarios in API versions 10 to 17. Since API version 18, it can also be configured in the combined fingerprint and facial authentication.
    

The user authentication widget supports the following types of authentication:

-   Lock screen password authentication
    
-   Facial authentication
    
-   Fingerprint authentication
    
-   Facial + lock screen password authentication
    
-   Fingerprint + lock screen password authentication
    
-   Facial + fingerprint + lock screen password authentication
    
-   Facial authentication + custom navigation button
    
-   Fingerprint authentication + custom navigation button
    
-   Facial authentication + fingerprint authentication + custom navigation button18+
    

#### How to Develop

1.  Check that the application has the ohos.permission.ACCESS\_BIOMETRIC permission. For details about how to request permissions, see [Requesting Permissions](../before-you-start/document.md#requesting-permissions).
    
2.  Set [AuthParam](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-useriam-userauth#authparam10) (including the challenge, [UserAuthType](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-useriam-userauth#userauthtype8), and [AuthTrustLevel](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-useriam-userauth#authtrustlevel8)), configure [WidgetParam](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-useriam-userauth#widgetparam10), and use [getUserAuthInstance](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-useriam-userauth#userauthgetuserauthinstance10) to obtain a **UserAuthInstance** instance.
    
3.  Use [UserAuthInstance.on](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-useriam-userauth#on10) to subscribe to the authentication result.
    
4.  Use [UserAuthInstance.start](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-useriam-userauth#start10) to start authentication. The authentication result [UserAuthResult](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-useriam-userauth#userauthresult10) is returned through [IAuthCallback](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-useriam-userauth#iauthcallback10). If the authentication is successful, [UserAuthType](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-useriam-userauth#userauthtype8) and token information (**AuthToken**) are returned.
    

**Example 1**

Initiate facial + fingerprint + lock screen password authentication at ATL3 or higher.

  initiatingUserAuthentication1() {
    try {
      const randData = getRandData();
      if (!randData) {
        return;
      }
      // Set authentication parameters.
      const authParam: userAuth.AuthParam = {
        challenge: randData,
        authType: \[userAuth.UserAuthType.PIN, userAuth.UserAuthType.FACE, userAuth.UserAuthType.FINGERPRINT\],
        authTrustLevel: userAuth.AuthTrustLevel.ATL3,
      };
      // Set the authentication page.
      const widgetParam: userAuth.WidgetParam = {
        title: resourceToString($r('app.string.title')),
      };
      // Obtain an authentication object.
      const userAuthInstance = userAuth.getUserAuthInstance(authParam, widgetParam);
      Logger.info('get userAuth instance success');
      // Subscribe to the authentication result.
      userAuthInstance.on('result', {
        onResult: (result: userAuth.UserAuthResult) => {
          try {
            Logger.info(\`userAuthInstance callback result: ${JSON.stringify(result)}\`);
            this.result\[ResultIndex.EXAMPLE\_1\] = (\`${result.result}\`);
            // Unsubscribe from the authentication result if required.
            userAuthInstance.off('result');
          } catch (error) {
            const err: BusinessError = error as BusinessError;
            Logger.error(\`onResult catch error. Code: ${err?.code}, Message: ${err?.message}\`);
          }
        }
      });
      // Start authentication.
      userAuthInstance.start();
      Logger.info('auth start success');
    } catch (error) {
      const err: BusinessError = error as BusinessError;
      Logger.error(\`auth catch error, code is ${err?.code}, message is ${err?.message}\`);
    }
  }

**Example 2**

Initiate facial authentication at ATL3 or higher, and enable the device unlock result to be reused for the same type of authentication within the specified time.

  initiatingUserAuthentication2() {
    // Set authentication parameters.
    let reuseUnlockResult: userAuth.ReuseUnlockResult = {
      reuseMode: userAuth.ReuseMode.AUTH\_TYPE\_RELEVANT,
      reuseDuration: userAuth.MAX\_ALLOWABLE\_REUSE\_DURATION,
    };
    try {
      const randData = getRandData();
      if (!randData) {
        return;
      }
      const authParam: userAuth.AuthParam = {
        challenge: randData,
        authType: \[userAuth.UserAuthType.PIN, userAuth.UserAuthType.FACE, userAuth.UserAuthType.FINGERPRINT\],
        authTrustLevel: userAuth.AuthTrustLevel.ATL3,
        reuseUnlockResult: reuseUnlockResult,
      };
      // Set the authentication page.
      const widgetParam: userAuth.WidgetParam = {
        title: resourceToString($r('app.string.title')),
      };
      // Obtain an authentication object.
      const userAuthInstance = userAuth.getUserAuthInstance(authParam, widgetParam);
      Logger.info('get userAuth instance success');
      // Subscribe to the authentication result.
      userAuthInstance.on('result', {
        onResult: (result: userAuth.UserAuthResult) => {
          try {
            Logger.info(\`userAuthInstance callback result: ${JSON.stringify(result)}\`);
            this.result\[ResultIndex.EXAMPLE\_2\] = (\`${result.result}\`);
            // Unsubscribe from the authentication result if required.
            userAuthInstance.off('result');
          } catch (error) {
            const err: BusinessError = error as BusinessError;
            Logger.error(\`onResult catch error. Code: ${err?.code}, Message: ${err?.message}\`);
          }
        }
      });
      // Start authentication.
      userAuthInstance.start();
      Logger.info('auth start success');
    } catch (error) {
      const err: BusinessError = error as BusinessError;
      Logger.error(\`auth catch error, code is ${err?.code}, message is ${err?.message}\`);
    }
  }

**Example 3**

Initiate facial authentication at ATL3 or higher, and enable the device unlock result to be reused for any type of authentication within the maximum authentication validity of any application.

  initiatingUserAuthentication3() {
    // Set authentication parameters.
    let reuseUnlockResult: userAuth.ReuseUnlockResult = {
      reuseMode: userAuth.ReuseMode.CALLER\_IRRELEVANT\_AUTH\_TYPE\_RELEVANT,
      reuseDuration: userAuth.MAX\_ALLOWABLE\_REUSE\_DURATION,
    };
    try {
      const randData = getRandData();
      if (!randData) {
        return;
      }
      const authParam: userAuth.AuthParam = {
        challenge: randData,
        authType: \[userAuth.UserAuthType.PIN, userAuth.UserAuthType.FACE, userAuth.UserAuthType.FINGERPRINT\],
        authTrustLevel: userAuth.AuthTrustLevel.ATL3,
        reuseUnlockResult: reuseUnlockResult,
      };
      // Set the authentication page.
      const widgetParam: userAuth.WidgetParam = {
        title: resourceToString($r('app.string.title')),
      };
      // Obtain an authentication object.
      const userAuthInstance = userAuth.getUserAuthInstance(authParam, widgetParam);
      Logger.info('get userAuth instance success');
      // Subscribe to the authentication result.
      userAuthInstance.on('result', {
        onResult: (result: userAuth.UserAuthResult) => {
          try {
            Logger.info(\`userAuthInstance callback result: ${JSON.stringify(result)}\`);
            this.result\[ResultIndex.EXAMPLE\_3\] = (\`${result.result}\`);
            // Unsubscribe from the authentication result if required.
            userAuthInstance.off('result');
          } catch (error) {
            const err: BusinessError = error as BusinessError;
            Logger.error(\`onResult catch error. Code: ${err?.code}, Message: ${err?.message}\`);
          }
        }
      });
      // Start authentication.
      userAuthInstance.start();
      Logger.info('auth start success');
    } catch (error) {
      const err: BusinessError = error as BusinessError;
      Logger.error(\`auth catch error, code is ${err?.code}, message is ${err?.message}\`);
    }
  }

**Example 4**

Start the user authentication widget in modal application mode.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/02/v3/QVzOvwjdQ4mnVYk0KumoRg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062013Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=FFF8C025CD03779F867B7F72C3B04982235473E2A744B395D47A8747FAE35E0A)

On PCs/2-in-1 devices, if an application initiates authentication in modal application mode (that is, a valid **uiContext** is passed when the user API parameter [widgetParam](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-useriam-userauth#widgetparam10) is configured), and if other windows need to be displayed after the authentication result is received, the application should obtain the flag message for releasing the widget pop-up window first, and subscribe to the widget release message (**authTipInfo.tipCode = UserAuthTipCode.WIDGET\_RELEASED**) through the [on('authTip')](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-useriam-userauth#on20) API.

  initiatingUserAuthentication4() {
    // Set authentication parameters.
    try {
      const randData = getRandData();
      if (!randData) {
        return;
      }
      const authParam: userAuth.AuthParam = {
        challenge: randData,
        authType: \[userAuth.UserAuthType.PIN, userAuth.UserAuthType.FACE, userAuth.UserAuthType.FINGERPRINT\],
        authTrustLevel: userAuth.AuthTrustLevel.ATL3,
      };
      // Set the authentication page.
      const widgetParam: userAuth.WidgetParam = {
        title: resourceToString($r('app.string.title')),
        uiContext: this.getUIContext().getHostContext()
      };
      // Obtain an authentication object.
      const userAuthInstance = userAuth.getUserAuthInstance(authParam, widgetParam);
      Logger.info('get userAuth instance success');
      // Subscribe to the authentication result.
      userAuthInstance.on('result', {
        onResult: (result: userAuth.UserAuthResult) => {
          try {
            Logger.info(\`userAuthInstance callback result: ${JSON.stringify(result)}\`);
            this.result\[ResultIndex.EXAMPLE\_4\] = (\`${result.result}\`);
            // Unsubscribe from the authentication result if required.
            userAuthInstance.off('result');
          } catch (error) {
            const err: BusinessError = error as BusinessError;
            Logger.error(\`onResult catch error. Code: ${err?.code}, Message: ${err?.message}\`);
          }
        }
      });
      // Start authentication.
      userAuthInstance.start();
      Logger.info('auth start success');
    } catch (error) {
      const err: BusinessError = error as BusinessError;
      Logger.error(\`auth catch error, code is ${err?.code}, message is ${err?.message}\`);
    }
  }

#### Sample Code

-   [Initiating authentication](https://gitcode.com/openharmony/applications_app_samples/blob/master/code/DocsSample/UserAuthentication)
