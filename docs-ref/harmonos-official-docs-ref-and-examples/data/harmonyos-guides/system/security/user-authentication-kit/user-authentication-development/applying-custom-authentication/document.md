# Applying Custom Authentication

If the biometric authentication fails and the user taps the navigation button for a custom authentication, the unified user authentication framework will terminate the system authentication process and instruct the caller to launch the custom authentication page.

For example, if the facial or fingerprint authentication provided by the system fails in a payment process, the user can switch to the password authentication defined by the device vendor.

Since payment password authentication is not a system authentication capability, the application must provide explicit navigation button information, for example, **Use Payment Password**, when initiating authentication. This ensures that a **Use Payment Password** button is displayed on the authentication page.

When the user taps this button, the application that initiates the custom authentication request will receive a special authentication result returned by the user authentication framework, indicating that the system authentication process is ended and prompting the application to launch its custom authentication page. As a result, the payment password authentication page customized by the service is displayed.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d4/v3/3L3twTBeSh2vj0oVIcevXA/en-us_image_0000002568764815.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062014Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=5B4522489A8B615080BEDCC29E229EBAF9125134E067ECCAB2AC9603AEF5E0EC)

As shown in the following figure, the selected area is the **WidgetParam.navigationButtonText** field. You can configure this field to guide users to switch from biometric authentication to the service password authentication customized by the application.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1a/v3/HpVHd1YJSWOzd0VVT34dog/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062014Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=3A43B060392E0FB49339FB8CE73861D6346F4D3FF3DDA7F7CA4B8B46D97BC737)

The lock screen password authentication and custom authentication are mutually exclusive.

| Authentication Type | 
Switch to Custom Authentication

(√ indicates supported, x indicates not supported)

 |
| :-- | :-- |
| Lock screen password authentication | × |
| Facial authentication | √ |
| Fingerprint authentication | √ |
| Facial + fingerprint authentication18+ | √ |
| Facial + lock screen password authentication | × |
| Fingerprint + lock screen password authentication | × |
| Facial + fingerprint + lock screen password authentication | × |

#### Development Example

For details about how to initiate the authentication request in the transition from a system-supported authentication to a custom authentication, see [initiating authentication](../initiating-user-authentication/document.md). Ensure that the **widgetParam** parameter passed in must contain **navigationButtonText**.

This example only shows how to configure the UI and select the custom authentication UI. You need to add the code for launching the custom authentication page at the commented line in the example.

  handleCustomAuthResult(userAuthInstance: userAuth.UserAuthInstance, exampleNumber: number) {
    // ···
      userAuthInstance.on('result', {
        onResult: (result: userAuth.UserAuthResult) => {
        // ···
              Logger.info(\`userAuthInstance callback result: ${JSON.stringify(result)}\`);
            // ···
            if (result.result == userAuth.UserAuthResultCode.CANCELED\_FROM\_WIDGET ||
              result.result == userAuth.UserAuthResultCode.NOT\_ENROLLED) {
              // You need to implement the process of launching the custom authentication page.
            // ···
            }
            // ···
        }
      });
      // Start authentication.
      userAuthInstance.start();
      Logger.info('auth start success');
    // ···
  }

  /\*
   \* apply-custom-authentication.md
   \* This example shows how to configure the page and switch to the custom authorizer page. You need to implement the pages to be started and the corresponding pages.
   \* \*/
  applyingCustomAuthentication() {
    try {
      const randData = getRandData();
      if (!randData) {
        return;
      }
      const authParam: userAuth.AuthParam = {
        challenge: randData,
        authType: \[userAuth.UserAuthType.FACE\],
        authTrustLevel: userAuth.AuthTrustLevel.ATL3,
      };
      // Configure custom authentication and set the text on the navigation button.
      const widgetParam: userAuth.WidgetParam = {
        title: resourceToString($r('app.string.title')),
        navigationButtonText: resourceToString($r('app.string.navigationButtonText'))
      };
      // Obtain an authentication object.
      const userAuthInstance = userAuth.getUserAuthInstance(authParam, widgetParam);
      Logger.info('get userAuth instance success');
      // Subscribe to the authentication result.
      this.handleCustomAuthResult(userAuthInstance, ResultIndex.CUSTOMIZE);
    } catch (error) {
      const err: BusinessError = error as BusinessError;
      Logger.error(\`auth catch error, code is ${err?.code}, message is ${err?.message}\`);
    }
  }

#### Sample Code

-   [Switching to custom authentication](https://gitcode.com/openharmony/applications_app_samples/blob/master/code/DocsSample/UserAuthentication)
