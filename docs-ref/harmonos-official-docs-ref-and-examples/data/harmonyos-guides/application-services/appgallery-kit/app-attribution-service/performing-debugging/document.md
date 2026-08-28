# Performing Debugging

The app attribution service provides the debugging capability. You can perform debugging by calling the debugging API to ensure a smooth interworking process and verify the basic capabilities of attribution postback, thereby improving efficiency.

#### Use Cases

The debugging capability supports the following scenarios:

-   Verify the correctness of an API call.
    
    The debugging API can be called to verify the API request and service logic, for example, to verify parameters and signatures. Error codes are provided for you to locate any problems.
    
-   Trigger attribution result postback.
    
    After configuring attribution data, you can call the debugging API to trigger attribution result postback in real time, thereby verifying the complete attribution process.
    

#### API Description

The app attribution service provides the following debugging-related APIs. For details, please refer to the [API reference](https://developer.huawei.com/consumer/en/doc/harmonyos-references/store-attributiontestmanager).

| 
API

 | 

**Description**

 |
| :-- | :-- |
| 

validateSource(adSourceInfo: AdSourceInfo, publicKey: string): Promise<void>

 | 

Verifies the attribution sources; used by media apps and distribution platforms to verify the validity of the input parameter **adSourceInfo**.

 |
| 

setPostback(postbackInfo: PostbackInfo): Promise<void>

 | 

Sets the attribution result, allowing you to:

-   Verify the validity of **triggerData**.
-   Configure the postback data used for debugging.

 |
| 

flushPostbacks(adTechId: string): Promise<void>

 | 

Triggers attribution postback in a proactive and real-time manner, allowing you to verify the logic for receiving and processing postback data.

 |

#### Development Procedure

## Verifying Attribution Sources

1.  Import required modules.
    
    import { attributionTestManager } from '@kit.AppGalleryKit';
    import { hilog } from '@kit.PerformanceAnalysisKit';
    import { BusinessError } from '@kit.BasicServicesKit';
    
2.  Construct input parameters: [AdSourceInfo](https://developer.huawei.com/consumer/en/doc/harmonyos-references/store-attributiontestmanager#section1262013338292) and **publickey**.
    
    // Public key provided for the cloud platform of the app attribution service during attribution role registration.
    let publicKey: string = '';
    let adSourceInfo: attributionTestManager.AdSourceInfo = {
      // You can enter a virtual **adTechId**.
      adTechId: '2\*\*\*\*\*\*8',
      campaignId: '1\*\*\*\*6',
      destinationId: '1\*\*\*\*\*\*\*8',
      sourceType: attributionTestManager.SourceType.IMPRESSION,
      mmpIds: \['1\*\*\*\*\*\*8', '2\*\*\*\*\*\*9'\],
      serviceTag: 'testServiceTag',
      nonce: '123\*\*\*2',
      timestamp: Date.now(),
      signature: 'MEQCIEQlmZ\*\*\*\*zKBSE8QnhLTIHZZZ\*\*\*\*ZpRqRxHss65Ko\*\*\*\*JgJKjdrWdkL\*\*\*\*juEx2RmFS7da\*\*\*\*ZRVZ8RyMyUXg=='
    }
    
3.  Call the [attributionTestManager.validateSource](https://developer.huawei.com/consumer/en/doc/harmonyos-references/store-attributiontestmanager#section193411799297) method to verify attribution sources.
    
    attributionTestManager.validateSource(adSourceInfo, publicKey).then(() => {
      hilog.info(0, "testTag", 'Succeeded in validating source.');
    }).catch((error: BusinessError) => {
      hilog.error(0, "testTag", \`testValidateSource failed.code is ${error.code}, message is ${error.message}\`);
    })
    

## Configuring Attribution Result Postback

1.  Import required modules.
    
    import { attributionTestManager } from '@kit.AppGalleryKit';
    import { hilog } from '@kit.PerformanceAnalysisKit';
    import { BusinessError } from '@kit.BasicServicesKit';
    
2.  Construct an input parameter [PostbackInfo](https://developer.huawei.com/consumer/en/doc/harmonyos-references/store-attributiontestmanager#section1812319373298).
    
    let postbackInfo: attributionTestManager.PostbackInfo = {
      adTechId: '1\*\*\*\*\*\*8',
      campaignId: '1\*\*\*\*6',
      sourceId: '1\*\*\*\*\*\*\*8',
      destinationId: '1\*\*\*\*\*\*\*8',
      serviceTag: 'testServiceTag',
      businessScene: 5,
      triggerData: 123,
      postbackUrl: 'https://xxx.com'
    };
    
3.  Call the [attributionTestManager.setPostback](https://developer.huawei.com/consumer/en/doc/harmonyos-references/store-attributiontestmanager#section16797112811814) method to configure the postback data.
    
    attributionTestManager.setPostback(postbackInfo).then(() => {
      hilog.info(0, "testTag", 'Succeeded in setting postback.');
    }).catch((error: BusinessError) => {
      hilog.error(0, "testTag", \`setPostback onError.code is ${error.code}, message is ${error.message}\`);
    }) 
    

## Triggering Attribution Result Postback

1.  Import required modules.
    
    import { attributionTestManager } from '@kit.AppGalleryKit';
    import { hilog } from '@kit.PerformanceAnalysisKit';
    import { BusinessError } from '@kit.BasicServicesKit';
    
2.  Construct a parameter **adTechId**.
    
    let adTechId: string = '1\*\*\*\*\*\*8';
    
3.  Call the [attributionTestManager.flushPostbacks](https://developer.huawei.com/consumer/en/doc/harmonyos-references/store-attributiontestmanager#section1890815407320) method to trigger the postback of attribution results.
    
    attributionTestManager.flushPostbacks(adTechId).then(() => {
      hilog.info(0, "testTag", 'Succeeded in flushing postbacks.');
    }).catch((error: BusinessError) => {
      hilog.error(0, "testTag", \`flushPostbacks onError.code is ${error.code}, message is ${error.message}\`);
    })
