# @security/no-unsafe-dh

Disallow the use of the insecure Diffie-Hellman (DH) key exchange algorithm, for example, a modulus length less than 2048 bits.

#### Rule Configuration

// code-linter.json5
{
  "rules": {
    "@security/no-unsafe-dh": "error"
  }
}

#### Options

This rule is not configurable.

#### Example of Correct Code

import cryptoFramework from '@ohos.security.cryptoFramework';
cryptoFramework.createKeyAgreement('DH\_modp3072');

#### Example of Incorrect Code

import cryptoFramework from '@ohos.security.cryptoFramework';
cryptoFramework.createKeyAgreement('DH\_modp1536');

#### Rule Set

plugin:@security/recommended
plugin:@security/all

For details about how to configure Code Linter check rules, see [Running Code Linter](../../../running-code-linter/document.md).
