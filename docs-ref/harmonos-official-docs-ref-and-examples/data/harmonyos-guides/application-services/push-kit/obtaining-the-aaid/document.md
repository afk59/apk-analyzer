# Obtaining the AAID

Anonymous Application Identifier (AAID): identifies an app instance running on a mobile smart device. Only the app instance identified by an AAID can access the AAID. The AAID is involved only in app installation and contains 36 digits. Compared with the device-level hardware ID that cannot be reset, the AAID features higher privacy.

To be specific, an AAID has the following features:

-   Anonymous, no privacy risk: An AAID is not associated with any existing identifiers. Besides, each app can only access its own AAID.
-   For apps from the same developer, which are running on the same device, each of them has its own AAID.
-   For apps from different developers, which are running on the same device, each of them has its own AAID.
-   For different apps from the same developer, which are running on different devices, each of them has its own AAID.
-   For apps from different developers, which are running on different devices, each of them has its own AAID.

#### Use Cases

Scenarios where the AAID may change include but are not limited to the following:

-   An app is reinstalled.
-   An app calls the API for deleting the AAID.
-   The user restores the device to its factory settings.
-   A user clears the app data.

#### Restrictions

The capability of obtaining an AAID is supported on phones, tablets, PCs/2-in-1 devices, (since 5.1.0(18)) wearables, and (since 5.1.1(19)) TVs.

#### API Description

The APIs use either a callback or promise to return the result. The table below lists only the APIs that use a promise. The APIs that use a callback provide the same functions as their counterparts that use a promise.

| 
API

 | 

Description

 |
| :-- | :-- |
| 

[getAAID](https://developer.huawei.com/consumer/en/doc/harmonyos-references/push-aaid-api#section573317917425)(): Promise<string>

 | 

Obtains an AAID. This API returns the result asynchronously through a promise.

 |
| 

[deleteAAID](https://developer.huawei.com/consumer/en/doc/harmonyos-references/push-aaid-api#section18269336164311)(): Promise<void>

 | 

Deletes an AAID. This API returns the result asynchronously through a promise.

 |

#### Obtaining an AAID

1.  Import the **AAID** module and related common modules.
    
    import { AAID } from '@kit.PushKit';
    import { AbilityConstant, UIAbility, Want } from '@kit.AbilityKit';
    import { BusinessError } from '@kit.BasicServicesKit';
    import { hilog } from '@kit.PerformanceAnalysisKit';
    
2.  Call the AAID.[getAAID](https://developer.huawei.com/consumer/en/doc/harmonyos-references/push-aaid-api#section573317917425)() method to obtain an AAID.
    
    export default class EntryAbility extends UIAbility {
      // The input parameters **want** and **launchParam** are not actually used. They are defined during project initialization.
      async onCreate(want: Want, launchParam: AbilityConstant.LaunchParam): Promise<void> {
        // Obtain an AAID
        try {
          const aaid: string = await AAID.getAAID();
          hilog.info(0x0000, 'testTag', 'Succeeded in getting AAID.');
        } catch (err) {
          let e: BusinessError = err as BusinessError;
          hilog.error(0x0000, 'testTag', 'Failed to get AAID: %{public}d %{public}s', e.code, e.message);
        }
      }
    }
