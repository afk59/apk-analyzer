# Querying Workspace Policies

#### Use Cases

Starting from 6.0.2(22), the capability of querying workspace policies is supported.

Apps can leverage this capability to query workspace policies, such as the security lockdown policy.

#### API Description

For details about the API, please refer to [getWorkspacePolicy](https://developer.huawei.com/consumer/en/doc/harmonyos-references/enterprisespace-spacemanager#section56999719412).

| 
API

 | 

Description

 |
| :-- | :-- |
| 

[getWorkspacePolicy](https://developer.huawei.com/consumer/en/doc/harmonyos-references/enterprisespace-spacemanager#section56999719412)(key: string, workspaceId?: number): Promise<number>

 | 

Queries workspace policies and returns the result. This API returns the result asynchronously through a promise.

 |

#### Development Procedure

1.  Import the Enterprise Space Kit module and dependent modules.
    
    import { spaceManager } from '@kit.EnterpriseSpaceKit';
    
2.  Call the [getWorkspacePolicy](https://developer.huawei.com/consumer/en/doc/harmonyos-references/enterprisespace-spacemanager#section56999719412) API to query workspace policies, and check the output.
    
    const key: string = 'lockdown';
    const workspaceId: number = 100;
    try {
      const value: number = await spaceManager.getWorkspacePolicy(key, workspaceId);
      console.info(\`Succeeded in getting workspace policy. value: ${value}\`);
    } catch (err) {
      console.error(\`Failed to get workspace policy. Code: ${err.code}, message: ${err.message}\`);
    }
