# Updating the Enterprise Public Key Certificate

#### Use Case

Enterprise Data Guard Kit allows an app to update the enterprise public key certificate timely in scenarios such as certificate leakage or expiration.

#### API Description

For details about these APIs, please refer to the [API Reference](https://developer.huawei.com/consumer/en/doc/harmonyos-references/dataguard-recoverykey).

| 
API

 | 

Description

 |
| :-- | :-- |
| 

[updateEnterpriseCertificate](https://developer.huawei.com/consumer/en/doc/harmonyos-references/dataguard-recoverykey#en-us_topic_0000001983615174_section1483871653813)(signature: Uint8Array, cert: Uint8Array): Promise<number>

 | 

Updates the enterprise public key certificate using a promise.

 |

#### Development Procedure

1.  Import the required modules.
    
    import { recoveryKey } from '@kit.EnterpriseDataGuardKit';
    import { BusinessError } from '@kit.BasicServicesKit';
    
2.  Call the [getAuthChallenge](https://developer.huawei.com/consumer/en/doc/harmonyos-references/dataguard-recoverykey#en-us_topic_0000001983615174_section41041418113717) API to obtain a challenge and [sign it](../signing-a-challenge/document.md). Then call the [updateEnterpriseCertificate](https://developer.huawei.com/consumer/en/doc/harmonyos-references/dataguard-recoverykey#en-us_topic_0000001983615174_section1483871653813) API and pass the challenge signature and enterprise public key certificate to update the certificate.
    
    function testUpdateEnterpriseCertificate() {
      let signature: Uint8Array = new Uint8Array(\[0\]);
      let cert: Uint8Array = new Uint8Array(\[0\]);
      recoveryKey.updateEnterpriseCertificate(signature, cert).then((ret: number) => {
        console.info(\`Succeeded in updating certificate.\`);
      }).catch((error: BusinessError) => {
        console.error(\`Failed to update certificate. Code: ${error.code}, message: ${error.message}\`);
      });
    }
