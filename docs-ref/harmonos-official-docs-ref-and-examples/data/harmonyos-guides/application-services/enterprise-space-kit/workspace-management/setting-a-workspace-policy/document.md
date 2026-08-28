# Setting a Workspace Policy

#### Use Cases

Starting from 6.0.2(22), the capability of setting workspace policies is supported.

Apps can leverage this capability to set workspace policies, such as the security lockdown policy.

#### API Description

For details about the API, please refer to [setWorkspacePolicy](https://developer.huawei.com/consumer/en/doc/harmonyos-references/enterprisespace-spacemanager#section3829226193112).

| 
API

 | 

Description

 |
| :-- | :-- |
| 

[setWorkspacePolicy](https://developer.huawei.com/consumer/en/doc/harmonyos-references/enterprisespace-spacemanager#section3829226193112)(key: string, value: number, workspaceId?: number): Promise<void>

 | 

Sets a workspace policy. This API returns the result asynchronously through a promise.

 |

#### Development Procedure

1.  Import the Enterprise Space Kit module and dependent modules.
    
    import { spaceManager } from '@kit.EnterpriseSpaceKit';
    
2.  Call the [setWorkspacePolicy](https://developer.huawei.com/consumer/en/doc/harmonyos-references/enterprisespace-spacemanager#section3829226193112) API to set a workspace policy, and check the output.
    
    const key: string = 'lockdown';
    const value: spaceManager.LockdownModePolicy = spaceManager.LockdownModePolicy.OFF;
    const workspaceId: number = 100;
    try {
      await spaceManager.setWorkspacePolicy(key, value, workspaceId);
      console.info(\`Succeeded in setting workspace policy.\`);
    } catch (err) {
      console.error(\`Failed to set workspace policy. Code: ${err.code}, message: ${err.message}\`);
    }
