# @security/no-unsafe-sm4

Disallow the use of insecure SM4 encryption modes, such as ECB. You are advised to use secure variants of SM4 such as SM4\_CBC\_PKCS5Padding.

#### Rule Configuration

// code-linter.json5
{
  "rules": {
    "@security/no-unsafe-sm4": "warn"
  }
}

#### Options

This rule is not configurable.

#### Example of Correct Code

import cryptoFramework from '@ohos.security.cryptoFramework';
cryptoFramework.createKdf('SM4\_128|CBC|PKCS7')

#### Example of Incorrect Code

import cryptoFramework from '@ohos.security.cryptoFramework';
cryptoFramework.createCipher('SM4\_128|ECB|PKCS7')

#### Rule Set

plugin:@security/all

For details about how to configure Code Linter check rules, see [Running Code Linter](../../../running-code-linter/document.md).
