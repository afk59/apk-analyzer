# Subscribing to Workspace Events

#### Use Cases

Enterprise Space Kit provides the capability of subscribing to workspace events for enterprise apps. Currently, the workspace switch event is supported. After subscribing to the workspace switch event, your app will be notified of workspace switches when they occur and can then perform the corresponding custom actions.

#### API Description

For details about the API, please refer to [subscribeEvent](https://developer.huawei.com/consumer/en/doc/harmonyos-references/enterprisespace-spacemanager#section53038113910).

| 
API

 | 

Description

 |
| :-- | :-- |
| 

[subscribeEvent](https://developer.huawei.com/consumer/en/doc/harmonyos-references/enterprisespace-spacemanager#section53038113910)(eventId: [EventType](https://developer.huawei.com/consumer/en/doc/harmonyos-references/enterprisespace-spacemanager#section3338122511597)\[\], callback: AsyncCallback<[EventData](https://developer.huawei.com/consumer/en/doc/harmonyos-references/enterprisespace-spacemanager#section1831382917492)\>): number

 | 

Subscribes to workspace events. Your app will be notified of the events when they are triggered. This API returns the result asynchronously through a callback.

 |

#### Development Procedure

1.  Import the Enterprise Space Kit module and dependent modules.
    
    import { spaceManager } from '@kit.EnterpriseSpaceKit';
    import { BusinessError } from '@kit.BasicServicesKit';
    
2.  Call the [subscribeEvent](https://developer.huawei.com/consumer/en/doc/harmonyos-references/enterprisespace-spacemanager#section53038113910) API to subscribe to a workspace event, and check the output.
    
    try {
      const subscribeId = spaceManager.subscribeEvent(\[0\],
        (error: BusinessError, data: spaceManager.EventData) => {
          if (error) {
            console.error(\`error info:${error?.code}, err message:${error?.message}\`);
          } else {
            console.info(\`event: ${data.event},currentWorkSpaceId: ${data.currentWorkspaceId}\`);
          }
        });
      console.info(\`Succeeded in subscribing event. subscribeId: ${subscribeId}\`);
    } catch (err) {
      console.error(\`Failed to subscribe event. Code: ${err.code}, message: ${err.message}\`);
    }
