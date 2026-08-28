# Removing a Workspace

#### Use Cases

Enterprise Space Kit provides the capability of removing a workspace for enterprise apps.

#### API Description

For details about the API, please refer to [removeWorkspace](https://developer.huawei.com/consumer/en/doc/harmonyos-references/enterprisespace-spacemanager#section1285414104597).

| 
API

 | 

Description

 |
| :-- | :-- |
| 

[removeWorkspace](https://developer.huawei.com/consumer/en/doc/harmonyos-references/enterprisespace-spacemanager#section1285414104597)(localId: number): Promise<void>

 | 

Removes a workspace. This API returns the result asynchronously through a promise.

 |

#### Development Procedure

1.  Import the Enterprise Space Kit module.
    
    import { spaceManager } from '@kit.EnterpriseSpaceKit';
    
2.  Call the [removeWorkspace](https://developer.huawei.com/consumer/en/doc/harmonyos-references/enterprisespace-spacemanager#section1285414104597) API to remove a workspace, and check the output.
    
    const workspaceId: number = 100;
    try {
      await spaceManager.removeWorkspace(workspaceId);
      console.info('Succeeded in removing workspace');
    } catch (err) {
      console.error(\`Failed to remove workspace. Code: ${err.code}, message: ${err.message}\`);
    }
