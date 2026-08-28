# Subscribing to HUAWEI ID Sign-in/Sign-out Events

#### Use Case

You can subscribe to the HUAWEI ID sign-in/sign-out events provided by Account Kit for your app when it is running in the foreground, to obtain the HUAWEI ID sign-in status, helping implement the sign-in and sign-out logic. The app can also query the HUAWEI ID sign-in status in real time through [getHuaweiIDState](https://developer.huawei.com/consumer/en/doc/harmonyos-references/account-api-authentication#section102884586336).

#### Event Description

The table below lists the events broadcasted for HUAWEI ID sign-in and sign-out on the device.

| 
Event

 | 

Description

 |
| :-- | :-- |
| 

[COMMON\_EVENT\_DISTRIBUTED\_ACCOUNT\_LOGIN](https://developer.huawei.com/consumer/en/doc/harmonyos-references/commoneventmanager-definitions#common_event_distributed_account_login)

 | 

Successful sign-in of a HUAWEI ID. This event is broadcasted when a HUAWEI ID is successfully signed in.

 |
| 

[COMMON\_EVENT\_DISTRIBUTED\_ACCOUNT\_LOGOUT](https://developer.huawei.com/consumer/en/doc/harmonyos-references/commoneventmanager-definitions#common_event_distributed_account_logout)

 | 

Successful sign-out of a HUAWEI ID. This event is broadcasted when a HUAWEI ID is successfully signed out.

 |

#### Prerequisites

Before coding, make sure that you have [configured the signing information and fingerprint](../../getting-started/configuring-signing-information-and-fingerprint/document.md) and also [set the client ID](../../getting-started/configuring-the-client-id/document.md). No additional scope or permission needs to be requested for the scenario described in this topic.

#### Development Procedure

1.  Import the [commonEventManager](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-commoneventmanager) module and related common modules.
    
    import { hilog } from '@kit.PerformanceAnalysisKit';
    import { BusinessError, commonEventManager } from '@kit.BasicServicesKit';
    
2.  Create a subscriber and process the subscription result.
    
    // Subscriber information.
    const subscribeInfo: commonEventManager.CommonEventSubscribeInfo = {
      events: \[commonEventManager.Support.COMMON\_EVENT\_DISTRIBUTED\_ACCOUNT\_LOGIN,
        commonEventManager.Support.COMMON\_EVENT\_DISTRIBUTED\_ACCOUNT\_LOGOUT\]
    };
    let subscriber: commonEventManager.CommonEventSubscriber;
    
    // Create a subscriber.
    commonEventManager.createSubscriber(subscribeInfo)
      .then((commonEventSubscriber: commonEventManager.CommonEventSubscriber) => {
        subscriber = commonEventSubscriber;
        // Subscribe to common events.
        commonEventManager.subscribe(subscriber,
          (error: BusinessError, data: commonEventManager.CommonEventData) => {
            if (error) {
              hilog.error(0x0000, 'testTag',
                \`Failed to subscribe , code is ${error.code}, message is ${error.message}\`);
            } else {
              if (data.event === commonEventManager.Support.COMMON\_EVENT\_DISTRIBUTED\_ACCOUNT\_LOGIN) {
                // Subscribe to the HUAWEI ID sign-in event.
              }
              if (data.event === commonEventManager.Support.COMMON\_EVENT\_DISTRIBUTED\_ACCOUNT\_LOGOUT) {
                // Subscribe to the HUAWEI ID sign-out event.
              }
            }
          });
      })
      .catch((err: BusinessError) => {
        hilog.error(0x0000, 'testTag', \`Failed to createSubscriber. Code: ${err.code}, message: ${err.message}\`);
      });
