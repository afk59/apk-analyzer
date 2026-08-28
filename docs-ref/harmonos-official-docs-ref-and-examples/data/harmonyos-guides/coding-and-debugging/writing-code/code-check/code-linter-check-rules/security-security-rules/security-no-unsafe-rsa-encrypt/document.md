# @security/no-unsafe-rsa-encrypt

Disallow the use of insecure RSA asymmetric encryption algorithms, such as RSA with a modulus length less than 2048 bits, PKCS1 padding mode, and the use of insecure MD5 or SHA-1 hash algorithms for digests or mask digests. The secure RSA encryption and decryption APIs provided by the Petal Aegis SDK are preferred.

#### Rule Configuration

// code-linter.json5
{
  "rules": {
    "@security/no-unsafe-rsa-encrypt": "error"
  }
}

#### Options

This rule is not configurable.

#### Example of Correct Code

import cryptoFramework from '@ohos.security.cryptoFramework';
cryptoFramework.createCipher('RSA3072|PKCS1\_OAEP|SHA256|MGF1\_SHA256');

#### Example of Incorrect Code

import cryptoFramework from '@ohos.security.cryptoFramework';
cryptoFramework.createCipher('RSA512|PKCS1');

#### Rule Set

plugin:@security/recommended
plugin:@security/all

For details about how to configure Code Linter check rules, see [Running Code Linter](../../../running-code-linter/document.md).
