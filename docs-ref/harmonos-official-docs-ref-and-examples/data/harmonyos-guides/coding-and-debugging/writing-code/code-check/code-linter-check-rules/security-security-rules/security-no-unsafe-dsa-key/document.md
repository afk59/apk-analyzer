# @security/no-unsafe-dsa-key

Disallow the use of insecure DSA keys, such as DSA modulus length less than 2048 bits.

#### Rule Configuration

// code-linter.json5
{
  "rules": {
    "@security/no-unsafe-dsa-key": "error"
  }
}

#### Options

This rule is not configurable.

#### Example of Correct Code

import cryptoFramework from '@ohos.security.cryptoFramework';
cryptoFramework.createAsyKeyGenerator('DSA3072');

#### Example of Incorrect Code

import cryptoFramework from '@ohos.security.cryptoFramework';
cryptoFramework.createAsyKeyGenerator('DSA1024');

#### Rule Set

plugin:@security/recommended
plugin:@security/all

For details about how to configure Code Linter check rules, see [Running Code Linter](../../../running-code-linter/document.md).
