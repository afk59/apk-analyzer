# Obtaining Supported Authentication Capabilities

Different devices support different authentication capabilities (facial authentication, fingerprint authentication, and password authentication). Before you start coding, obtain the authentication capabilities supported by the target device.

#### Available APIs

For details about the parameters, return value, and error codes, see [getAvailableStatus](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-useriam-userauth#userauthgetavailablestatus9).

| API | Description |
| :-- | :-- |
| getAvailableStatus(authType : UserAuthType, authTrustLevel : AuthTrustLevel): void | Checks whether the specified authentication type and authentication trust level are supported by the device. |

#### How to Develop

1.  [Request](../before-you-start/document.md#requesting-permissions) the ohos.permission.ACCESS\_BIOMETRIC permission.
    
2.  Call [getAvailableStatus](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-useriam-userauth#userauthgetavailablestatus9) to check whether the device supports the specified authentication type ([UserAuthType](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-useriam-userauth#userauthtype8)) and authentication trust level ([AuthTrustLevel](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-useriam-userauth#authtrustlevel8)).
    
    For details about the authentication trust levels, see [Principles for Classifying Biometric Authentication Trust Levels](../../about-this-kit/document.md#principles-for-classifying-biometric-authentication-trust-levels).
    

Example: Check whether the device supports facial authentication of ATL3 or higher.

obtainingSupported() {
  try {
    // Check whether the specified authentication capabilities are supported.
    userAuth.getAvailableStatus(userAuth.UserAuthType.FACE, userAuth.AuthTrustLevel.ATL3);
    Logger.info('current auth trust level is supported');
    return true;
  } catch (error) {
    const err: BusinessError = error as BusinessError;
    Logger.error(\`current auth trust level is not supported, code is ${err?.code}, message is ${err?.message}\`);
    return false;
  }
}

#### Sample Code

-   [Querying supported authentication capabilities](https://gitcode.com/openharmony/applications_app_samples/blob/master/code/DocsSample/UserAuthentication)
