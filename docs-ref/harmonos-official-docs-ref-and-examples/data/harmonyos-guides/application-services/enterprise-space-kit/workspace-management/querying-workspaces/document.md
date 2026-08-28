# Querying Workspaces

#### Use Cases

Enterprise Space Kit provides the capability of querying workspaces for enterprise apps.

#### API Description

For details about the API, please refer to [queryWorkspace](https://developer.huawei.com/consumer/en/doc/harmonyos-references/enterprisespace-spacemanager#section6592656143118).

| 
API

 | 

Description

 |
| :-- | :-- |
| 

[queryWorkspace](https://developer.huawei.com/consumer/en/doc/harmonyos-references/enterprisespace-spacemanager#section6592656143118)(queryFlag: [QueryType](https://developer.huawei.com/consumer/en/doc/harmonyos-references/enterprisespace-spacemanager#section87287517554)): Promise<WorkspaceInfo\[\]>

 | 

Queries workspace information and returns the result. This API returns the result asynchronously through a promise.

 |

#### Development Procedure

1.  Import the Enterprise Space Kit module.
    
    import { spaceManager } from '@kit.EnterpriseSpaceKit';
    
2.  Call the [queryWorkspace](https://developer.huawei.com/consumer/en/doc/harmonyos-references/enterprisespace-spacemanager#section6592656143118) API to query workspaces, and check the output.
    
    const queryFlag: spaceManager.QueryType = 0;
    try {
      const spaces: spaceManager.WorkspaceInfo\[\] = await spaceManager.queryWorkspace(queryFlag);
      console.info(\`Succeeded in querying workspace\` + JSON.stringify(spaces));
    } catch (err) {
      console.error(\`Failed to query workspace. Code: ${err.code}, message: ${err.message}\`);
    }
