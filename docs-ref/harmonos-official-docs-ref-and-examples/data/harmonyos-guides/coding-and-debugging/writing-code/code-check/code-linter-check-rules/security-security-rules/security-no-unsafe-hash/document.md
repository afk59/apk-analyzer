# @security/no-unsafe-hash

Disallow the use of insecure hash algorithms, such as MD5 and SHA-1.

#### Rule Configuration

// code-linter.json5
{
  "rules": {
    "@security/no-unsafe-hash": "error"
  }
}

#### Options

This rule is not configurable.

#### Example of Correct Code

// Example 1 (correct code)
import cryptoFramework from '@ohos.security.cryptoFramework';
cryptoFramework.createMd('SHA256');

// Example 2 (correct code)
/\*\*
 \* Run ohpm install @ohos/crypto-js to download the [crypto-js](https://gitcode.com/openharmony-sig/ohos_crypto_js) dependency.
 \*/
import { CryptoJS } from '@ohos/crypto-js';
CryptoJS.SHA256('Message').toString();

#### Example of Incorrect Code

// Example 1.1 (incorrect code)
import cryptoFramework from '@ohos.security.cryptoFramework';
cryptoFramework.createMd('MD5');

// Example 1.2 (incorrect code)
import cryptoFramework from '@ohos.security.cryptoFramework';
cryptoFramework.createMd('SHA1');

// Example 2.1 (incorrect code)
import { CryptoJS } from '@ohos/crypto-js';
CryptoJS.MD5('Message').toString();

// Example 2.2 (incorrect code)
import { CryptoJS } from '@ohos/crypto-js';
CryptoJS.SHA1('Message').toString();

#### Rule Set

plugin:@security/recommended
plugin:@security/all

For details about how to configure Code Linter check rules, see [Running Code Linter](../../../running-code-linter/document.md).
