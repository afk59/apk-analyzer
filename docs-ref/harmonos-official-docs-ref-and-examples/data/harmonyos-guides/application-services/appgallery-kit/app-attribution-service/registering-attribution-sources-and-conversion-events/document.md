# Registering Attribution Sources and Conversion Events

#### Use Cases

The app attribution service provides the capability for media apps and distribution platforms to register attribution sources (for example, an app impression or a click) and for developers' apps to register conversion events with the device-side app attribution service.

According to system rules, the device-side app attribution service completes attribution calculation based on the attribution sources registered by media apps and conversion events registered by developers' apps.

#### API Description

The app attribution service provides the following APIs. For details, please refer to the [API reference](https://developer.huawei.com/consumer/en/doc/harmonyos-references/store-attributionmanager).

| 
API

 | 

**Description**

 |
| :-- | :-- |
| 

registerSource(adSourceInfo: AdSourceInfo): Promise<void>

 | 

Registers attribution sources.

 |
| 

registerTrigger(adTriggerInfo: AdTriggerInfo): Promise<void>

 | 

Registers conversion events.

 |

#### Development Procedure

## Registering Attribution Sources

1.  Import required modules.
    
    import { attributionManager } from '@kit.AppGalleryKit';
    import { hilog } from '@kit.PerformanceAnalysisKit';
    import { BusinessError } from '@kit.BasicServicesKit';
    
2.  Construct a parameter [AdSourceInfo](https://developer.huawei.com/consumer/en/doc/harmonyos-references/store-attributionmanager#section0594928105511).
    
    const adSourceInfo: attributionManager.AdSourceInfo = {
      // Allocated by the app attribution service during role registration on the cloud platform of the app attribution service.
      adTechId: '20\*\*\*\*e8',
      campaignId: '',
      // ID of the developer's app released on AppGallery, without letter C.
      destinationId: '10\*\*\*\*\*\*',
      sourceType: attributionManager.SourceType.IMPRESSION,
      // ID of the attribution monitoring platform.
      mmpIds: \['2f\*\*\*\*5','2f7\*\*\*5'\],
      // Business information that the distribution platform focuses on.
      serviceTag: '123\*\*\*2',
      // Random number without hyphens (-), used for signature calculations.
      nonce: '123\*\*\*2',
      timestamp: Date.now(),
      // Signature.
      signature: 'MEQCIEQlmZ\*\*\*\*zKBSE8QnhLTIHZZZ\*\*\*\*ZpRqRxHss65Ko\*\*\*\*JgJKjdrWdkL\*\*\*\*juEx2RmFS7da\*\*\*\*ZRVZ8RyMyUXg=='
    }
    
3.  Call the [attributionManager.registerSource](https://developer.huawei.com/consumer/en/doc/harmonyos-references/store-attributionmanager#section359424018307) method to register attribution sources.
    
    try {
      attributionManager.registerSource(adSourceInfo).then(() => {
        hilog.info(0, 'TAG', 'Succeeded in registering source.');
      }).catch((error: BusinessError) => {
        hilog.error(0, 'TAG', \`registerSource error.code is ${error.code}, message is ${error.message}\`);
      })
    } catch (error) {
      hilog.error(0, 'TAG', \`registerSource error.code is ${error.code}, message is ${error.message}\`);
    }
    

## Registering Conversion Events

1.  Import required modules.
    
    import { attributionManager } from '@kit.AppGalleryKit';
    import { hilog } from '@kit.PerformanceAnalysisKit';
    import { BusinessError } from '@kit.BasicServicesKit';
    
2.  Construct a parameter [AdTriggerInfo](https://developer.huawei.com/consumer/en/doc/harmonyos-references/store-attributionmanager#section6127112918554).
    
    const adTriggerInfo: attributionManager.AdTriggerInfo = {
      businessScene: 5,
      // Conversion event ID, which is obtained from the cloud platform of the app attribution service.
      triggerData: 123
    }
    
3.  Call the [attributionManager.registerTrigger](https://developer.huawei.com/consumer/en/doc/harmonyos-references/store-attributionmanager#section13414543616) method to register conversion events.
    
    try {
      attributionManager.registerTrigger(adTriggerInfo).then(() => {
        hilog.info(0, 'TAG', 'Succeeded in registering triggerdata.');
      }).catch((error: BusinessError) => {
        hilog.error(0, 'TAG', \`registerTrigger error.code is ${error.code}, message is ${error.message}\`);
      })
    } catch (error) {
      hilog.error(0, 'TAG', \`registerTrigger error.code is ${error.code}, message is ${error.message}\`);
    }
