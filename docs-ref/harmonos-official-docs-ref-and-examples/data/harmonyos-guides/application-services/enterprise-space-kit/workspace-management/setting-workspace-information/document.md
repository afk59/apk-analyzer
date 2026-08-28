# Setting Workspace Information

#### Use Cases

Enterprise Space Kit provides the capability of setting workspace information for enterprise apps. When an enterprise's system is initialized, you need to set workspace information to enable domain account binding.

#### API Description

For details about the API, please refer to [setWorkspaceInfo](https://developer.huawei.com/consumer/en/doc/harmonyos-references/enterprisespace-spacemanager#section15245021163318).

| 
API

 | 

Description

 |
| :-- | :-- |
| 

[setWorkspaceInfo](https://developer.huawei.com/consumer/en/doc/harmonyos-references/enterprisespace-spacemanager#section15245021163318)(workspaceId: number, domainInfo: [WorkspaceDomainInfo](https://developer.huawei.com/consumer/en/doc/harmonyos-references/enterprisespace-spacemanager#section1457564515610)): Promise<void>

 | 

Sets workspace information. This API returns the result asynchronously through a promise.

 |

#### Development Procedure

1.  Import the Enterprise Space Kit module.
    
    import { spaceManager } from '@kit.EnterpriseSpaceKit';
    
2.  Call the [setWorkspaceInfo](https://developer.huawei.com/consumer/en/doc/harmonyos-references/enterprisespace-spacemanager#section15245021163318) API to set workspace information, and check the output.
    
    const workspaceId: number = 100;
    const domainInfo: spaceManager.WorkspaceDomainInfo = {
      domain: 'test1',
      workspaceName: 'test2',
      accountId: 'test3',
      isAuthenticated: false,
      serverConfigId: 'test4',
      workspaceEnterpriseName: 'default'
    };
    
    try {
      await spaceManager.setWorkspaceInfo(workspaceId, domainInfo);
      console.info('Succeeded in setting workspace info');
    } catch (err) {
      console.error(\`Failed to set workspace info. Code: ${err.code}, message: ${err.message}\`);
    }
