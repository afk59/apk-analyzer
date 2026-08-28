# Canceling User Authentication

Use **cancel()** to terminate the authentication process when needed.

#### Available APIs

For details about the parameters, return value, and error codes, see [cancel](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-useriam-userauth#cancel10).

This topic describes only the API for canceling authentication. For details about the APIs for initiating authentication, see [Initiating Authentication](../initiating-user-authentication/document.md) and [User Authentication](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-useriam-userauth).

| API | Description |
| :-- | :-- |
| cancel(): void | Cancels this user authentication. |

#### How to Develop

1.  Check that the application has the ohos.permission.ACCESS\_BIOMETRIC permission. For details about how to request permissions, see [Requesting Permissions](../before-you-start/document.md#requesting-permissions).
    
2.  Set [AuthParam](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-useriam-userauth#authparam10) (including the challenge value, [UserAuthType](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-useriam-userauth#userauthtype8), and [AuthTrustLevel](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-useriam-userauth#authtrustlevel8)), obtain a [UserAuthInstance](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-useriam-userauth#userauthinstance10) instance, and call [UserAuthInstance.start](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-useriam-userauth#start10) to start authentication. For details, see [Initiating Authentication](../initiating-user-authentication/document.md).
    
3.  Call [UserAuthInstance.cancel](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-useriam-userauth#cancel10) with the **UserAuthInstance** instance that has initiated the authentication to terminate the authentication process.
    

Example: Initiate facial and lock screen password authentication at ATL3 or higher and then cancel it.

  handleAuthResultAndCanceling(userAuthInstance: userAuth.UserAuthInstance, exampleNumber: number) {
    // ···
      // Start authentication.
      userAuthInstance.start();
      Logger.info('auth start success');
    // ···
        // Cancel the authentication.
        userAuthInstance.cancel();
        Logger.info('auth cancel success');
        // ···
  }

  /\*
   \* cancel-authentication.md
   \* Initiate facial and lock screen password authentication at ATL3 or higher and then cancel it.
   \* \*/
  cancelingUserAuthentication() {
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
      this.handleAuthResultAndCanceling(userAuthInstance, ResultIndex.CANCEL);
    } catch (error) {
      const err: BusinessError = error as BusinessError;
      Logger.error(\`auth catch error, code is ${err?.code as number}, message is ${err?.message}\`);
    }
  }

#### Sample Code

-   [Cancel authentication in progress](https://gitcode.com/openharmony/applications_app_samples/blob/master/code/DocsSample/UserAuthentication)
