# @security/no-unsafe-kdf

Disallow the use of insecure KDF algorithms, including PBKDF2|SHA1 and HKDF|SHA1. You are advised to use PBKDF2|SHA256 and HKDF|SHA256.

#### Rule Configuration

// code-linter.json5
{
  "rules": {
    "@security/no-unsafe-kdf": "warn"
  }
}

#### Options

This rule is not configurable.

#### Example of Correct Code

import cryptoFramework from '@ohos.security.cryptoFramework';
cryptoFramework.createKdf('PBKDF2|SHA256');
import cryptoFramework from '@ohos.security.cryptoFramework';
cryptoFramework.createKdf('HKDF|SHA256');

#### Example of Incorrect Code

import cryptoFramework from '@ohos.security.cryptoFramework';
cryptoFramework.createKdf('PBKDF2|SHA1');
import cryptoFramework from '@ohos.security.cryptoFramework';
cryptoFramework.createKdf('HKDF|SHA1');

#### Rule Set

plugin:@security/all

For details about how to configure Code Linter check rules, see [Running Code Linter](../../../running-code-linter/document.md).
