# What Should I Do If the Plaintext Mobile Number Cannot Be Obtained in the One-Tap Sign-In Scenario?

Before reading this section, ensure that the anonymous mobile number can be successfully obtained in the HUAWEI ID one-tap sign-in scenario. Perform the following steps if the plaintext anonymous mobile number cannot be obtained in the one-tap sign-in scenario.

1.  Check whether a mobile number is bound to the HUAWEI ID. If not, show the sign-in screen that contains other sign-in options.
2.  The HUAWEI ID used for one-tap sign-in must be from the Chinese mainland.
3.  Only the app server deployed in the Chinese mainland is allowed to request the mobile number bound to a HUAWEI ID.
4.  Ensure that **authCode** used by your app to obtain the mobile phone from the server is obtained through the one-tap HUAWEI ID sign-in component. For details, please refer to [App-Side Development](../../sign-in/signing-in-with-huawei-id-through-just-one-tap-obtaining-the-mobile-number-union/document.md#section834212543125).
