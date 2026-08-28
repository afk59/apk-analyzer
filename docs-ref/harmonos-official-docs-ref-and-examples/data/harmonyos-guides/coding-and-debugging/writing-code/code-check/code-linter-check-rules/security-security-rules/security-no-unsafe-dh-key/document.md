# @security/no-unsafe-dh-key

Disallow the use of insecure Diffie-Hellman (DH) keys, such as DH modulus length less than 2048 bits.

#### Rule Configuration

// code-linter.json5
{
  "rules": {
    "@security/no-unsafe-dh-key": "error"
  }
}

#### Options

This rule is not configurable.

#### Example of Correct Code

import cryptoFramework from '@ohos.security.cryptoFramework';
cryptoFramework.createAsyKeyGenerator('DH\_modp3072');

#### Example of Incorrect Code

import cryptoFramework from '@ohos.security.cryptoFramework';
cryptoFramework.createAsyKeyGenerator('DH\_modp1536');

#### Rule Set

plugin:@security/recommended
plugin:@security/all

For details about how to configure Code Linter check rules, see [Running Code Linter](../../../running-code-linter/document.md).
