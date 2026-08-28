# @security/no-unsafe-mac

Disallow the use of insecure hash algorithms, such as SHA-1, in Message Authentication Code (MAC) algorithms.

#### Rule Configuration

// code-linter.json5
{
  "rules": {
    "@security/no-unsafe-mac": "warn"
  }
}

#### Options

This rule is not configurable.

#### Example of Correct Code

import cryptoFramework from '@ohos.security.cryptoFramework';
import { CryptoJS } from '@ohos/crypto-js';
cryptoFramework.createMac('SHA256');
CryptoJS.HmacSHA256('Message').toString();

#### Example of Incorrect Code

import cryptoFramework from '@ohos.security.cryptoFramework';
import { CryptoJS } from '@ohos/crypto-js';
cryptoFramework.createMac('SHA1');
CryptoJS.HmacSHA1('Message').toString();

#### Rule Set

plugin:@security/recommended
plugin:@security/all

For details about how to configure Code Linter check rules, see [Running Code Linter](../../../running-code-linter/document.md).
