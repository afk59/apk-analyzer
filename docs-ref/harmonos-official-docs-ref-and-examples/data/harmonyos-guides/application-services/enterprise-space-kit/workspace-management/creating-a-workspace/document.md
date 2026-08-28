# Creating a Workspace

#### Use Cases

Enterprise Space Kit provides the capability of creating workspaces for enterprise apps.

#### API Description

For details about the API, please refer to [createWorkspace](https://developer.huawei.com/consumer/en/doc/harmonyos-references/enterprisespace-spacemanager#section174311747184814).

| 
API

 | 

Description

 |
| :-- | :-- |
| 

[createWorkspace](https://developer.huawei.com/consumer/en/doc/harmonyos-references/enterprisespace-spacemanager#section174311747184814)(localName: string, workspaceType: [WorkspaceType](https://developer.huawei.com/consumer/en/doc/harmonyos-references/enterprisespace-spacemanager#section3637177173919), params?: [CreateWorkspaceParams](https://developer.huawei.com/consumer/en/doc/harmonyos-references/enterprisespace-spacemanager#section2818219505)): Promise<[WorkspaceInfo](https://developer.huawei.com/consumer/en/doc/harmonyos-references/enterprisespace-spacemanager#section1528202625516)\>

 | 

Creates a workspace and returns the result. This API returns the result asynchronously through a promise.

 |

#### Development Procedure

1.  Import the Enterprise Space Kit module.
    
    import { spaceManager } from '@kit.EnterpriseSpaceKit';
    
2.  Call the [createWorkspace](https://developer.huawei.com/consumer/en/doc/harmonyos-references/enterprisespace-spacemanager#section174311747184814) API to create a workspace, and check the output.
    
    const localName: string = '111111';
    const workspaceType: spaceManager.WorkspaceType = 0;
    const params: spaceManager.CreateWorkspaceParams = {
      shortName: 'test'
    };
    try {
      const workspaceInfo: spaceManager.WorkspaceInfo = await spaceManager.createWorkspace(localName, workspaceType, params);
      console.info(\`Succeeded in creating workspace, workspaceInfo:\` + JSON.stringify(workspaceInfo));
    } catch (err) {
      console.error(\`Failed to create workspace. Code: ${err.code}, message: ${err.message}\`);
    }
