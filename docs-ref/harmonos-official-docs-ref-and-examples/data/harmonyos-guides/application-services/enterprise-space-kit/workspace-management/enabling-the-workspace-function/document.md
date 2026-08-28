# Enabling the Workspace Function

#### Use Cases

Enterprise Space Kit provides the capability of enabling the enterprise and personal workspace function for enterprise apps. Before creating a personal workspace, you must enable the workspace function first.

#### API Description

For details about the API, please refer to [enableWorkspace](https://developer.huawei.com/consumer/en/doc/harmonyos-references/enterprisespace-spacemanager#section85743218296).

| 
API

 | 

Description

 |
| :-- | :-- |
| 

[enableWorkspace](https://developer.huawei.com/consumer/en/doc/harmonyos-references/enterprisespace-spacemanager#section85743218296)(enable: boolean): Promise<void>

 | 

Enables the workspace function. This API returns the result asynchronously through a promise.

 |

#### Development Procedure

1.  Import the Enterprise Space Kit module.
    
    import { spaceManager } from '@kit.EnterpriseSpaceKit';
    
2.  Call the [enableWorkspace](https://developer.huawei.com/consumer/en/doc/harmonyos-references/enterprisespace-spacemanager#section85743218296) API to enable the workspace function, and check the output.
    
    const enable: boolean = true;
    try {
      await spaceManager.enableWorkspace(enable);
      console.info('Succeeded in enabling workspace');
    } catch (err) {
      console.error(\`Failed to enable workspace. Code: ${err.code}, message: ${err.message}\`);
    }
