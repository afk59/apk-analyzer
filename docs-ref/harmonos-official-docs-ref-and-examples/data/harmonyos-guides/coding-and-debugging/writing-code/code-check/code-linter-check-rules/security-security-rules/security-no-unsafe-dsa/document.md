# @security/no-unsafe-dsa

Disallow the use of the insecure DSA signature algorithm, such as DSA with a modulus length less than 2048 bits, and the use of the insecure SHA-1 hashing algorithm in the digest.

#### Rule Configuration

// code-linter.json5
{
  "rules": {
    "@security/no-unsafe-dsa": "error"
  }
}

#### Options

This rule is not configurable.

#### Example of Correct Code

import cryptoFramework from '@ohos.security.cryptoFramework';
cryptoFramework.createSign('DSA3072|SHA256');
cryptoFramework.createVerify('DSA3072|SHA256');

#### Example of Incorrect Code

import cryptoFramework from '@ohos.security.cryptoFramework';
cryptoFramework.createSign('DSA1024|SHA256');
cryptoFramework.createVerify('DSA1024|SHA256');

#### Rule Set

plugin:@security/recommended
plugin:@security/all

For details about how to configure Code Linter check rules, see [Running Code Linter](../../../running-code-linter/document.md).
