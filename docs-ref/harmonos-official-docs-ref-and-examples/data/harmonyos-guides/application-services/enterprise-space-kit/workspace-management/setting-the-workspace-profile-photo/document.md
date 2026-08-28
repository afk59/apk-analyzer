# Setting the Workspace Profile Photo

#### Use Cases

Enterprise Space Kit provides the capability of setting the workspace profile photo for enterprise apps. You can set a profile photo for each workspace.

#### API Description

For details about the API, please refer to [setWorkspaceProfilePhoto](https://developer.huawei.com/consumer/en/doc/harmonyos-references/enterprisespace-spacemanager#section6531192033412).

| 
API

 | 

Description

 |
| :-- | :-- |
| 

[setWorkspaceProfilePhoto](https://developer.huawei.com/consumer/en/doc/harmonyos-references/enterprisespace-spacemanager#section6531192033412)(workspaceId: number, photo: string): Promise<void>

 | 

Sets the workspace profile photo. This API returns the result asynchronously through a promise.

 |

#### Development Procedure

1.  Import the Enterprise Space Kit module.
    
    import { spaceManager } from '@kit.EnterpriseSpaceKit';
    
2.  Call the [setWorkspaceProfilePhoto](https://developer.huawei.com/consumer/en/doc/harmonyos-references/enterprisespace-spacemanager#section6531192033412) API to set the workspace profile photo, and check the output.
    
    const workspaceId: number = 100;
    const photo: string = '{"type":0,"defaultImg":"data:image/png;base64,iVBO\*\*\*\*\*\*Jggg==}';
    try {
      await spaceManager.setWorkspaceProfilePhoto(workspaceId, photo);
      console.info('Succeeded in setting workspace profile photo');
    } catch (err) {
      console.error(\`Failed to set workspace profile photo. Code: ${err.code}, message: ${err.message}\`);
    }
