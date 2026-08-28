# Deleting an Enterprise Recovery Key

#### Use Case

Enterprise Data Guard Kit allows an app to delete an existing enterprise recovery key in scenarios where related data needs to be deleted when the enterprise recovery key is leaked or disabled.

#### API Description

For details about these APIs, please refer to the [API Reference](https://developer.huawei.com/consumer/en/doc/harmonyos-references/dataguard-recoverykey).

| 
API

 | 

Description

 |
| :-- | :-- |
| 

[deleteEnterpriseRecoveryKey](https://developer.huawei.com/consumer/en/doc/harmonyos-references/dataguard-recoverykey#en-us_topic_0000001983615174_section1927015514386)(userId: number, signature: Uint8Array): Promise<number>

 | 

Deletes data related to the enterprise recovery key using a promise.

 |

#### Development Procedure

1.  Import the required modules.
    
    import { recoveryKey } from '@kit.EnterpriseDataGuardKit';
    import { BusinessError, osAccount } from '@kit.BasicServicesKit';
    
2.  Call the [getAuthChallenge](https://developer.huawei.com/consumer/en/doc/harmonyos-references/dataguard-recoverykey#en-us_topic_0000001983615174_section41041418113717) API to obtain a challenge and [sign it](../signing-a-challenge/document.md). Then call the [deleteEnterpriseRecoveryKey](https://developer.huawei.com/consumer/en/doc/harmonyos-references/dataguard-recoverykey#en-us_topic_0000001983615174_section1927015514386) API and pass the user ID of the enterprise recovery key to be deleted and the signature of the challenge.
    
    async function testDeleteEnterpriseRecoveryKey() {
      try {
        let accountManager: osAccount.AccountManager = osAccount.getAccountManager();
        let userId: number = await accountManager.getOsAccountLocalId();
        let signature: Uint8Array = new Uint8Array(\[0\]);
        recoveryKey.deleteEnterpriseRecoveryKey(userId, signature).then((ret: number) => {
          console.info(\`Succeeded in deleting enterprise recovery key.\`);
        }).catch((err: BusinessError) => {
          console.error(\`Failed to delete enterprise recovery key. Code: ${err.code}, message: ${err.message}\`);
        });
      } catch (e) {
        console.error(\`Failed to testDeleteEnterpriseRecoveryKey. Code: ${e.code}, message: ${e.message}\`);
      }
    }
