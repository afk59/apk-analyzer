# Obtaining a Challenge

#### Use Case

Your app needs to obtain and sign a challenge before initiating the process to update the enterprise public key certificate or delete an existing enterprise recovery key to verify the enterprise's identity.

#### API Description

For details about these APIs, please refer to the [API Reference](https://developer.huawei.com/consumer/en/doc/harmonyos-references/dataguard-recoverykey).

| 
API

 | 

Description

 |
| :-- | :-- |
| 

[getAuthChallenge](https://developer.huawei.com/consumer/en/doc/harmonyos-references/dataguard-recoverykey#en-us_topic_0000001983615174_section41041418113717)(): Promise<Uint8Array>

 | 

Obtains a challenge using a promise.

 |

#### Development Procedure

1.  Import the required modules.
    
    import { recoveryKey } from '@kit.EnterpriseDataGuardKit';
    import { BusinessError } from '@kit.BasicServicesKit';
    
2.  Call the [getAuthChallenge](https://developer.huawei.com/consumer/en/doc/harmonyos-references/dataguard-recoverykey#en-us_topic_0000001983615174_section41041418113717) API to obtain a challenge.
    
    function testGetAuthChallenge() {
      recoveryKey.getAuthChallenge().then((challenge: Uint8Array) => {
        console.info(\`Succeeded in getting challenge.\`);
      }).catch((error: BusinessError) => {
        console.error(\`Failed to get challenge. Code: ${error.code}, message: ${error.message}\`);
      });
    }
