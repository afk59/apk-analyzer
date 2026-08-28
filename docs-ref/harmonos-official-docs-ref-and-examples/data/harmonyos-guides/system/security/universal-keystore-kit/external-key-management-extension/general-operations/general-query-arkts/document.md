# General Query (ArkTS)

From API version 22, **huksExternalCrypto** provides the general query API. This API can be used to obtain the device ID, application ID, and other general properties from an UKey. For details about the scenarios, see [General Query Overview and Specifications](../general-query-overview-and-specifications/document.md).

#### How to Develop

**Obtaining properties**

1.  Obtain [keyUri](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-certmanagerdialog#certreference22) as **resourceId** by calling the [certificate selection API](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-certmanagerdialog#certificatemanagerdialogopenauthorizedialog22) provided by the certificate management system, and [open the resource](../../resource-management/opening-and-closing-resources-c-c/document.md#opening-resources).
    
2.  Construct the input parameter **propertyId** and optional input parameter [HuksExternalCryptoParam](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-huksexternalcrypto#huksexternalcryptoparam).
    
3.  Call [getProperty](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-huksexternalcrypto#huksexternalcryptogetproperty) to obtain the property information.
    

#### Development Cases

import { huksExternalCrypto } from '@kit.UniversalKeystoreKit';
import { BusinessError } from '@kit.BasicServicesKit';

async function getProperty(): Promise<Array<huksExternalCrypto.HuksExternalCryptoParam>> {
  // 1. Obtain resourceId. Assume that resourceId is as follows and the resource has been opened:
  const testResourceId = JSON.stringify({
    providerName: "testProviderName",
    bundleName: "com.example.cryptoapplication",
    abilityName: "CryptoExtension",
    index: {
      key: "testKey"
    } as ESObject
  });

  // 2. Construct the input parameter propertyId and optional parameter HuksExternalCryptoParam.
  let propertyId = "SKF\_EnumDev";
  const extProperties: Array<huksExternalCrypto.HuksExternalCryptoParam> = \[\];

  // 3. Call getProperty to obtain the property information.
  console.info(\`promise: await huksExternalCrypto getProperty\`);
  try {
    await huksExternalCrypto.getProperty(testResourceId, propertyId, extProperties)
      .then((data) => {
        console.info(\`promise: getProperty success, data: \` + JSON.stringify(data));
      }).catch((error: BusinessError) => {
        console.error(\`promise: getProperty failed, errCode : ${error.code}, errMsg : ${error.message}\`);
      })
  } catch (error) {
    console.error(\`promise: getProperty failed, errCode : ${error.code}, errMsg : ${error.message}\`);
  }
  return extProperties;
}
