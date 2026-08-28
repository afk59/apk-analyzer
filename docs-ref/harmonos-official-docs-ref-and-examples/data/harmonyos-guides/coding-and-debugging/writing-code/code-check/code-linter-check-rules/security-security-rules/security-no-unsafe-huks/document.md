# @security/no-unsafe-huks

Disallow the use of insecure ECB encryption mode, insecure hash algorithms MD5 and SHA1, and padding algorithms NONE and PKCS1-V1\_5 in HUKS. The AES-GCM algorithm of HUKS is recommended.

#### Rule Configuration

// code-linter.json5
{
  "rules": {
    "@security/no-unsafe-huks": "warn"
  }
}

#### Options

This rule is not configurable.

#### Example of Correct Code

import {huks} from '@kit.UniversalKeystoreKit';  
let keyAlias: string = 'keyAlias'; 
let properties: Array<huks.HuksParam> = \[
  { 
    tag: huks.HuksTag.HUKS\_TAG\_ALGORITHM,
    value: huks.HuksKeyAlg.HUKS\_ALG\_ECC
  },
  {
    tag: huks.HuksTag.HUKS\_TAG\_KEY\_SIZE,
    value: huks.HuksKeySize.HUKS\_ECC\_KEY\_SIZE\_256
  },
  {
    tag: huks.HuksTag.HUKS\_TAG\_PURPOSE,
    value:
       huks.HuksKeyPurpose.HUKS\_KEY\_PURPOSE\_SIGN |
       huks.HuksKeyPurpose.HUKS\_KEY\_PURPOSE\_VERIFY
  },
  {
    tag: huks.HuksTag.HUKS\_TAG\_BLOCK\_MODE,
    value: huks.HuksCipherMode.HUKS\_MODE\_CBC
  }, 
  {
    tag: huks.HuksTag.HUKS\_TAG\_DIGEST, 
    value: huks.HuksKeyDigest.HUKS\_DIGEST\_SHA256
  },
  {
   tag: huks.HuksTag.HUKS\_TAG\_PADDING,
   value: huks.HuksKeyPadding.HUKS\_PADDING\_PKCS7
  }
\]; 
let options: huks.HuksOptions = {
    properties: properties
}; 
huks.generateKeyItem(keyAlias, options);

#### Example of Incorrect Code

import {huks} from '@kit.UniversalKeystoreKit';  
let keyAlias: string = 'keyAlias'; 
let properties: Array<huks.HuksParam> = \[
  { 
    tag: huks.HuksTag.HUKS\_TAG\_ALGORITHM,
    value: huks.HuksKeyAlg.HUKS\_ALG\_ECC
  },
  {
    tag: huks.HuksTag.HUKS\_TAG\_KEY\_SIZE,
    value: huks.HuksKeySize.HUKS\_ECC\_KEY\_SIZE\_256
  },
  {
    tag: huks.HuksTag.HUKS\_TAG\_PURPOSE,
    value:
       huks.HuksKeyPurpose.HUKS\_KEY\_PURPOSE\_SIGN |
       huks.HuksKeyPurpose.HUKS\_KEY\_PURPOSE\_VERIFY
  },
  {
    tag: huks.HuksTag.HUKS\_TAG\_BLOCK\_MODE,
    value: huks.HuksCipherMode.HUKS\_MODE\_ECB
  }, 
  {
    tag: huks.HuksTag.HUKS\_TAG\_DIGEST, 
    value: huks.HuksKeyDigest.HUKS\_DIGEST\_SHA1
  },
  {
   tag: huks.HuksTag.HUKS\_TAG\_PADDING,
   value: huks.HuksKeyPadding.HUKS\_PADDING\_NONE
  }
\]; 
let options: huks.HuksOptions = {
    properties: properties
}; 
huks.generateKeyItem(keyAlias, options);

#### Rule Set

plugin:@security/all

For details about how to configure Code Linter check rules, see [Running Code Linter](../../../running-code-linter/document.md).
