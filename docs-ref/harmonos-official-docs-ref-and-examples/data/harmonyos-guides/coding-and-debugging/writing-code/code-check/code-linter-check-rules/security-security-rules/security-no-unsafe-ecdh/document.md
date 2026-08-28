# @security/no-unsafe-ecdh

Disallow the use of insecure ECC asymmetric key types. The ECC256 algorithm is recommended.

#### Rule Configuration

// code-linter.json5
{
  "rules": {
    "@security/no-unsafe-ecdh": "warn"
  }
}

#### Options

This rule is not configurable.

#### Example of Correct Code

import cryptoFramework from '@ohos.security.cryptoFramework';
cryptoFramework.createAsyKeyGenerator('ECC256');

#### Example of Incorrect Code

import cryptoFramework from '@ohos.security.cryptoFramework';
cryptoFramework.createAsyKeyGenerator('ECC');

#### Rule Set

plugin:@security/all

For details about how to configure Code Linter check rules, see [Running Code Linter](../../../running-code-linter/document.md).
