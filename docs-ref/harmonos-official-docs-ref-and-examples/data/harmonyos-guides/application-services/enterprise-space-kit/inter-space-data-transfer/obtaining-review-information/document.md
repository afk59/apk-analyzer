# Obtaining Review Information

#### Use Cases

Enterprise Space Kit provides the capability of obtaining review information for apps. Outbound file transfer requires a review process. In this scenario, you can call the review status synchronization API to obtain the review result in real time. Upon approval, files can be sent externally to personal workspaces. However, if the review request is rejected or canceled, outgoing file transfer is prohibited.

#### API Description

For details about the API, please refer to [getAuditInfo](https://developer.huawei.com/consumer/en/doc/harmonyos-references/enterprisespace-spacedatatransfer#section5740142017119).

| 
API

 | 

Description

 |
| :-- | :-- |
| 

[getAuditInfo](https://developer.huawei.com/consumer/en/doc/harmonyos-references/enterprisespace-spacedatatransfer#section5740142017119)(transactionNum: string): [AuditInfo](https://developer.huawei.com/consumer/en/doc/harmonyos-references/enterprisespace-spacedatatransfer#section14605182931520)

 | 

Obtains review information.

 |

#### Development Procedure

1.  Import the Enterprise Space Kit module.
    
    import { fileTransfer } from '@kit.EnterpriseSpaceKit';
    
2.  Call the [getAuditInfo](https://developer.huawei.com/consumer/en/doc/harmonyos-references/enterprisespace-spacedatatransfer#section5740142017119) API to obtain review information, and check the output.
    
    const transactionNum: string = '1111111';
    try {
      const auditInfo: fileTransfer.AuditInfo = fileTransfer.getAuditInfo(transactionNum);
      console.info(\`Succeeded in getting audit info:\` + JSON.stringify(auditInfo));
    } catch (err) {
      console.error(\`Failed to get audit info. Code: ${err.code}, message: ${err.message}\`);
    }
