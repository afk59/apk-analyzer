# Setting the Deep Freeze Exemption List

#### Use Cases

From 6.0.2 (22), the capability of setting the deep freeze exemption list is supported.

Enterprise apps can leverage this capability to add specific apps to the deep freeze exemption list. Apps on the list can function properly in the background without being frozen.

#### API Description

For details about the API, please refer to [setLockdownExemptionApps](https://developer.huawei.com/consumer/en/doc/harmonyos-references/enterprisespace-spacemanager#section65245634612).

| 
API

 | 

Description

 |
| :-- | :-- |
| 

[setLockdownExemptionApps](https://developer.huawei.com/consumer/en/doc/harmonyos-references/enterprisespace-spacemanager#section65245634612)(appIds: string\[\], workspaceId?: number): Promise<void>

 | 

Sets the deep freeze exemption list. This API returns the result asynchronously through a promise.

 |

#### Development Procedure

1.  Import the Enterprise Space Kit module and dependent modules.
    
    import { spaceManager } from '@kit.EnterpriseSpaceKit';
    
2.  Call the [setLockdownExemptionApps](https://developer.huawei.com/consumer/en/doc/harmonyos-references/enterprisespace-spacemanager#section65245634612) API to set the deep freeze exemption list, and check the output.
    
    const workspaceId: number = 100;
    const appIds = \[
        'com.example.enterprisespacekit\_samplecode\_clientdemo\_arkts1',
        'com.example.enterprisespacekit\_samplecode\_clientdemo\_arkts2'
      \];
    try {
      await spaceManager.setLockdownExemptionApps(appIds, workspaceId);
      console.info(\`Succeeded in setting lockdown exemption apps.\`);
    } catch (err) {
      console.error(\`Failed to set lockdown exemption apps. Code: ${err.code}, message: ${err.message}\`);
    }
