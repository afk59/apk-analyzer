# @security/no-unsafe-aes

Disallow the use of the insecure ECB mode in the AES algorithm. The secure AES APIs provided by the Petal Aegis SDK are preferred.

#### Rule Configuration

// code-linter.json5
{
  "rules": {
    "@security/no-unsafe-aes": "error"
  }
}

#### Options

This rule is not configurable.

#### Example of Correct Code

import cryptoFramework from '@ohos.security.cryptoFramework';
cryptoFramework.createCipher('AES128|CBC|PKCS5');

#### Example of Incorrect Code

import cryptoFramework from '@ohos.security.cryptoFramework';
cryptoFramework.createCipher('AES128|ECB|NoPadding');

#### Rule Set

plugin:@security/recommended
plugin:@security/all

For details about how to configure Code Linter check rules, see [Running Code Linter](../../../running-code-linter/document.md).
