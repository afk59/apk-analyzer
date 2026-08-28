# Querying the Deep Freeze Exemption List

#### Use Cases

From 6.0.2 (22), the capability of querying the deep freeze exemption list is supported.

Enterprise apps can leverage this capability to query the configured deep freeze exemption list.

#### API Description

For details about the API, please refer to [getLockdownExemptionApps](https://developer.huawei.com/consumer/en/doc/harmonyos-references/enterprisespace-spacemanager#section76466565311).

| 
API

 | 

Description

 |
| :-- | :-- |
| 

[getLockdownExemptionApps](https://developer.huawei.com/consumer/en/doc/harmonyos-references/enterprisespace-spacemanager#section76466565311)(workspaceId?: number): Promise<string\[\]>

 | 

Queries the deep freeze exemption list. This API returns the result asynchronously through a promise.

 |

#### Development Procedure

1.  Import the Enterprise Space Kit module and dependent modules.
    
    import { spaceManager } from '@kit.EnterpriseSpaceKit';
    
2.  Call the [getLockdownExemptionApps](https://developer.huawei.com/consumer/en/doc/harmonyos-references/enterprisespace-spacemanager#section76466565311) API to query the deep freeze exemption list, and check the output.
    
    const workspaceId: number = 100;
    try {
      const apps: string\[\] = await spaceManager.getLockdownExemptionApps(workspaceId);
      console.info(\`Succeeded in getting lockdown exemption apps. apps:\` + JSON.stringify(apps));
    } catch (err) {
      console.error(\`Failed to get lockdown exemption apps. Code: ${err.code}, message: ${err.message}\`);
    }
