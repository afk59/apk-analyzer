# Setting Review Information

#### Use Cases

Outbound file transfer requires a review process. Enterprise Space Kit provides apps with the capability of setting review information, including the review ID, user ID, user name, review time, review comments, and review status.

#### API Description

For details about the API, please refer to [setAuditInfo](https://developer.huawei.com/consumer/en/doc/harmonyos-references/enterprisespace-spacedatatransfer#section1285414104597).

| 
API

 | 

Description

 |
| :-- | :-- |
| 

[setAuditInfo](https://developer.huawei.com/consumer/en/doc/harmonyos-references/enterprisespace-spacedatatransfer#section1285414104597)(transactionNum: string, info: [AuditInfo](https://developer.huawei.com/consumer/en/doc/harmonyos-references/enterprisespace-spacedatatransfer#section14605182931520)): number

 | 

Sets review information and returns the result.

 |

#### Development Procedure

1.  Import the Enterprise Space Kit module.
    
    import { fileTransfer } from '@kit.EnterpriseSpaceKit';
    
2.  Call the [setAuditInfo](https://developer.huawei.com/consumer/en/doc/harmonyos-references/enterprisespace-spacedatatransfer#section1285414104597) API to set review information.
    
    const transactionNum: string = '1111111';
    const info: fileTransfer.AuditInfo = {
      auditId: '123456',
      userId: '100',
      userName: 'test',
      time: Date.now(),
      comments: 'Waiting approval',
      status: '1'
    };
    try {
      const ret: number = fileTransfer.setAuditInfo(transactionNum, info);
      console.info(\`Succeeded in setting audit info, number:\`, ret);
    } catch (err) {
      console.error(\`Failed to set audit info. Code: ${err.code}, message: ${err.message}\`);
    }
