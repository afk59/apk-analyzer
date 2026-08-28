# @security/no-unsafe-sm2-key

Disallow the insecure use of the SM2 asymmetric key algorithm. You are advised to use the SM2\_256|SHA256 algorithm and RSA algorithm. For details, see [Asymmetric Key Encryption and Decryption Algorithm Specifications](../../../../../../system/security/crypto-architecture-kit/encryption-and-decryption/encryption-and-decryption-algorithm-specifications/asymmetric-key-encryption-and-decryption-algorithm-specifications/document.md#rsa).

#### Rule Configuration

// code-linter.json5
{
  "rules": {
    "@security/no-unsafe-sm2-key": "warn"
  }
}

#### Options

This rule is not configurable.

#### Example of Correct Code

import cryptoFramework from '@ohos.security.cryptoFramework';
cryptoFramework.createAsyKeyGenerator('SM2\_256|SHA256')

#### Example of Incorrect Code

import cryptoFramework from '@ohos.security.cryptoFramework';
cryptoFramework.createAsyKeyGenerator('SM2|SHA256')

#### Rule Set

plugin:@security/all

For details about how to configure Code Linter check rules, see [Running Code Linter](../../../running-code-linter/document.md).
