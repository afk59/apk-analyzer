# @security/no-unsafe-rsa-key

Disallow the use of insecure RSA keys, such as RSA modulus length less than 2048 bits. The secure RSA signature APIs provided by the Petal Aegis SDK are preferred.

#### Rule Configuration

// code-linter.json5
{
  "rules": {
    "@security/no-unsafe-rsa-key": "error"
  }
}

#### Options

This rule is not configurable.

#### Example of Correct Code

import cryptoFramework from '@ohos.security.cryptoFramework';
cryptoFramework.createAsyKeyGenerator('RSA3072|PRIMES\_2');

#### Example of Incorrect Code

import cryptoFramework from '@ohos.security.cryptoFramework';
cryptoFramework.createAsyKeyGenerator('RSA512|PRIMES\_2');

#### Rule Set

plugin:@security/recommended
plugin:@security/all

For details about how to configure Code Linter check rules, see [Running Code Linter](../../../running-code-linter/document.md).
