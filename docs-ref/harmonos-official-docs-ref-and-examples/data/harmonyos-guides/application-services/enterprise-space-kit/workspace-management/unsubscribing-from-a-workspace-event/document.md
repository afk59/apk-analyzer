# Unsubscribing from a Workspace Event

#### Use Cases

Enterprise Space Kit provides the capability of unsubscribing from a workspace event for enterprise apps. Your app can flexibly manage workspace event subscriptions in specific scenarios. For example, when your app is closed or a specific functional module will no longer be used, your app can call this API to unsubscribe from a specific workspace event.

#### API Description

For details about the API, please refer to [unsubscribeEvent](https://developer.huawei.com/consumer/en/doc/harmonyos-references/enterprisespace-spacemanager#section134241041398).

| 
API

 | 

Description

 |
| :-- | :-- |
| 

[unsubscribeEvent](https://developer.huawei.com/consumer/en/doc/harmonyos-references/enterprisespace-spacemanager#section134241041398)(subscribeId:number): void

 | 

Unsubscribes from a workspace event. Your app will no longer be notified of the event when it is triggered.

 |

#### Development Procedure

1.  Import the Enterprise Space Kit module.
    
    import { spaceManager } from '@kit.EnterpriseSpaceKit';
    
2.  Call the [unsubscribeEvent](https://developer.huawei.com/consumer/en/doc/harmonyos-references/enterprisespace-spacemanager#section134241041398) API to unsubscribe from a workspace event, and check the output.
    
    const subscribeId: number = 100;
    try {
      spaceManager.unsubscribeEvent(subscribeId);
      console.info('Succeeded in unsubscribing event');
    } catch (err) {
      console.error(\`Failed to unsubscribe event. Code: ${err.code}, message: ${err.message}\`);
    }
