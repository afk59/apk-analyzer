# @security/no-unsafe-rsa-sign

Disallow the use of insecure RSA signature algorithms, such as RSA with a modulus length less than 2048 bits, and the use of insecure MD5 or SHA-1 hash algorithms in digests or mask digests. The secure RSA signature APIs provided by the Petal Aegis SDK are preferred.

#### Rule Configuration

// code-linter.json5
{
  "rules": {
    "@security/no-unsafe-rsa-sign": "error"
  }
}

#### Options

This rule is not configurable.

#### Example of Correct Code

import cryptoFramework from '@ohos.security.cryptoFramework';
cryptoFramework.createSign('RSA3072|PSS|SHA256|MGF1\_SHA256');
cryptoFramework.createVerify('RSA3072|PSS|SHA256|MGF1\_SHA256');

#### Example of Incorrect Code

import cryptoFramework from '@ohos.security.cryptoFramework';
cryptoFramework.createSign('RSA512|PKCS1|MD5');
cryptoFramework.createVerify('RSA512|PKCS1|MD5');

#### Rule Set

plugin:@security/recommended
plugin:@security/all

For details about how to configure Code Linter check rules, see [Running Code Linter](../../../running-code-linter/document.md).
