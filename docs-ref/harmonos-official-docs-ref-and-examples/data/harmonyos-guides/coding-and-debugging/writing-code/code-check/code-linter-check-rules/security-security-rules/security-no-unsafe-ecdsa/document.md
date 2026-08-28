# @security/no-unsafe-ecdsa

Disallow the use of the insecure SHA1 digest algorithm in the ECDSA signature algorithm. The secure ECDSA APIs provided by the Petal Aegis SDK are preferred.

#### Rule Configuration

// code-linter.json5
{
  "rules": {
    "@security/no-unsafe-ecdsa": "error"
  }
}

#### Options

This rule is not configurable.

#### Example of Correct Code

import cryptoFramework from '@ohos.security.cryptoFramework';
cryptoFramework.createSign('ECC256|SHA256');
cryptoFramework.createVerify('ECC256|SHA256');

#### Example of Incorrect Code

import cryptoFramework from '@ohos.security.cryptoFramework';
cryptoFramework.createSign('ECC224|SHA1');
cryptoFramework.createVerify('ECC224|SHA1');

#### Rule Set

plugin:@security/recommended
plugin:@security/all

For details about how to configure Code Linter check rules, see [Running Code Linter](../../../running-code-linter/document.md).
