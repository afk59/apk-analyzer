# @security/no-unsafe-3des

Disallow the use of insecure 3DES encryption modes, such as 3DES|ECB. It is recommended that you use secure 3DES encryption modes, for example, 3DES|CBC. For details, see [3DES](../../../../../../system/security/crypto-architecture-kit/encryption-and-decryption/encryption-and-decryption-algorithm-specifications/symmetric-key-encryption-and-decryption-algorithm-specifications/document.md#section3des).

#### Rule Configuration

// code-linter.json5
{
  "rules": {
    "@security/no-unsafe-3des": "error"
  }
}

#### Options

This rule is not configurable.

#### Example of Correct Code

import cryptoFramework from '@ohos.security.cryptoFramework';
cryptoFramework.createCipher('3DES|CBC');

#### Example of Incorrect Code

import cryptoFramework from '@ohos.security.cryptoFramework';
cryptoFramework.createCipher('3DES|ECB');

#### Rule Set

plugin:@security/recommended
plugin:@security/all

For details about how to configure Code Linter check rules, see [Running Code Linter](../../../running-code-linter/document.md).
