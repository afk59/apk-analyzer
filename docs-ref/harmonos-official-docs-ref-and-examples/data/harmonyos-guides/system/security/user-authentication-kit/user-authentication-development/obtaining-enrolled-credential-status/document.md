# Obtaining Enrolled Credential Status

Use **getEnrolledState()** to obtain the change in the credentials (face, fingerprint, and password) enrolled by a user.

#### Available APIs

For details about the parameters, return values, and error codes, see [getEnrolledState](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-useriam-userauth#userauthgetenrolledstate12).

| API | Description |
| :-- | :-- |
| getEnrolledState(authType : UserAuthType): EnrolledState | Obtains the status of the enrolled credentials based on the specified authentication type. |

#### How to Develop

1.  Check that the application has the ohos.permission.ACCESS\_BIOMETRIC permission. For details about how to request permissions, see [Requesting Permissions](../before-you-start/document.md#requesting-permissions).
    
2.  Specify the authentication type ([UserAuthType](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-useriam-userauth#userauthtype8)) and call [getEnrolledState](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-useriam-userauth#userauthgetenrolledstate12) to obtain the status of the credentials enrolled by the user.
    

Example: Obtain information about the credentials enrolled for facial authentication.

  obtainingEnrolledCredentialInformation() {
    try {
      let enrolledState = userAuth.getEnrolledState(userAuth.UserAuthType.PIN);
      Logger.info(\`get current enrolled state success, enrolledState: ${JSON.stringify(enrolledState)}\`);
      return enrolledState.credentialDigest;
    } catch (error) {
      const err: BusinessError = error as BusinessError;
      Logger.error(\`get current enrolled state failed, Code is ${err?.code}, message is ${err?.message}\`);
      return false;
    }
  }

#### Sample Code

-   [Querying the status of a user registration credential](https://gitcode.com/openharmony/applications_app_samples/blob/master/code/DocsSample/UserAuthentication)
