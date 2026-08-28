# How do I use a custom PIN (6–16 digits) to unlock a key?

Set **HUKS\_TAG\_USER\_AUTH\_TYPE** to **HUKS\_USER\_AUTH\_TYPE\_PIN**.

To ensure secure access to keys, user identity authentication is required. Currently, only the lock screen password authentication and biometric authentication are supported.

1\. For security-sensitive service keys, lock screen password authentication or biometric authentication is required before the service keys are used. The service key can be used only after the authentication is successful.

2\. For security-insensitive service keys, a password (not the lock screen password) verification is required. The application needs to implement the password authentication.

**Reference**

[HuksAuthAccessType](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-huks#huksauthaccesstype9)
