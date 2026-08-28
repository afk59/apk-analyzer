# Managing User Authorization

#### Scenario

Your app can only access data upon user authorization on the HUAWEI ID sign-in screen and authorization screen. Users can select the data range to be authorized and grant only some data permissions.

The data that your app can access is both approved by Health Service Kit and granted by users.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7c/v3/uGik8cWlQsiGAzWu4ZJlXA/en-us_image_0000002509454481.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062106Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=4C0CC60594B73E9D29339A6BEA512BC5661DA8BDC27F4F7D037AAE016456D678)

#### API Description

| 
API Name

 | 

Description

 |
| :-- | :-- |
| 

[requestAuthorizations](https://developer.huawei.com/consumer/en/doc/harmonyos-references/health-api-healthstore#section19461855171619)(context: [common.UIAbilityContext](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-application-uiabilitycontext#uiabilitycontext-1), request: [AuthorizationRequest](https://developer.huawei.com/consumer/en/doc/harmonyos-references/health-api-healthstore#en-us_topic_0000001768344397_section1956619544498)): Promise<[AuthorizationResponse](https://developer.huawei.com/consumer/en/doc/harmonyos-references/health-api-healthstore#en-us_topic_0000001768344397_section963483625117)\>

 | 

Requests user authorization. When calling this API, pass the UIAbility context and [AuthorizationRequest](https://developer.huawei.com/consumer/en/doc/harmonyos-references/health-api-healthstore#en-us_topic_0000001768344397_section1956619544498). Add the data types to be read and written, display the HUAWEI ID authorization screen, and instruct users to complete the authorization. The scopes matching the list of data types returned are the intersection of [the scopes you have applied for](../../getting-started/applying-for-health-service-kit/document.md) and those granted by users.

 |
| 

[getAuthorizations](https://developer.huawei.com/consumer/en/doc/harmonyos-references/health-api-healthstore#section68141073254)(request: [AuthorizationRequest](https://developer.huawei.com/consumer/en/doc/harmonyos-references/health-api-healthstore#en-us_topic_0000001768344397_section1956619544498)): Promise<[AuthorizationResponse](https://developer.huawei.com/consumer/en/doc/harmonyos-references/health-api-healthstore#en-us_topic_0000001768344397_section963483625117)\>

 | 

Queries user authorization. When calling this API, pass [AuthorizationRequest](https://developer.huawei.com/consumer/en/doc/harmonyos-references/health-api-healthstore#en-us_topic_0000001768344397_section1956619544498) and add data types to query whether users have granted the authorization for these data types. The scopes matching the list of data types returned are the intersection of [the scopes you have applied for](../../getting-started/applying-for-health-service-kit/document.md) and those granted by users.

 |
| 

[cancelAuthorizations](https://developer.huawei.com/consumer/en/doc/harmonyos-references/health-api-healthstore#section18660141352811)(): Promise<void>

 | 

Cancels all authorization.

 |

#### Before Getting Started

-   Complete [Applying for Health Service Kit](../../getting-started/applying-for-health-service-kit/document.md) and [Configuring the Client ID](../../getting-started/configuring-the-client-id/document.md).
-   An API must be called within the lifecycle of a page or custom component. Before calling an API for the first time, call the [init](https://developer.huawei.com/consumer/en/doc/harmonyos-references/health-api-healthstore#section1571935817328) method to perform initialization.
-   For details about error codes, refer to [ArkTS API Error Codes](https://developer.huawei.com/consumer/en/doc/harmonyos-references/errorcode-healthservice). For FAQs, see [FAQs About Health Service Kit](../../../faqs-about-health-service-kit/document.md).

#### Development Procedure

## User Authorization

1.  Import the Health Service Kit functional module and related public modules.
    
    import { healthStore } from '@kit.HealthServiceKit';
    import { common } from '@kit.AbilityKit';
    import { hilog } from '@kit.PerformanceAnalysisKit';
    
2.  Create an authorization request. Make sure you have applied for the scopes specified in the authorization parameters during your Health Service Kit application. For details about the scopes, refer to [Scope Description](../../data-types/scope-description/document.md).
    
    let authorizationParameter: healthStore.AuthorizationRequest = {
      readDataTypes: \[healthStore.exerciseSequenceHelper.DATA\_TYPE, healthStore.samplePointHelper.heartRate.DATA\_TYPE\],
      writeDataTypes: \[healthStore.exerciseSequenceHelper.DATA\_TYPE, healthStore.samplePointHelper.heartRate.DATA\_TYPE\]
    }
    
3.  Call [requestAuthorizations](https://developer.huawei.com/consumer/en/doc/harmonyos-references/health-api-healthstore#section19461855171619) to request sign-in authorization and process the returned result.
    
    try {
      let authorizationResponse = await healthStore.requestAuthorizations(this.getUIContext().getHostContext() as common.UIAbilityContext, authorizationParameter);
      hilog.info(0x0000, 'testTag', 'Succeeded in requesting authorization.');
      authorizationResponse.writeDataTypes.forEach(dataType => {
        hilog.info(0x0000, 'testTag', \`grantedWriteDataType is : ${dataType.name}\`);
      });
      authorizationResponse.readDataTypes.forEach(dataType => {
        hilog.info(0x0000, 'testTag', \`grantedReadDataTypes is : ${dataType.name}\`);  
      });
    } catch (err) {
      hilog.error(0x0000, 'testTag', \`Failed to request authorization. Code: ${err.code}, message: ${err.message}\`);
    }
    

## Querying Authorization

1.  Import the Health Service Kit functional module and related public modules.
    
    import { healthStore } from '@kit.HealthServiceKit';
    import { hilog } from '@kit.PerformanceAnalysisKit';
    
2.  Create an authorization query request.
    
    let queryAuthorizationRequest: healthStore.AuthorizationRequest = {
      readDataTypes: \[healthStore.exerciseSequenceHelper.DATA\_TYPE, healthStore.samplePointHelper.heartRate.DATA\_TYPE\],
      writeDataTypes: \[healthStore.exerciseSequenceHelper.DATA\_TYPE, healthStore.samplePointHelper.heartRate.DATA\_TYPE\]
    }
    
3.  Call [getAuthorizations](https://developer.huawei.com/consumer/en/doc/harmonyos-references/health-api-healthstore#section68141073254) to query the authorization and process the returned result.
    
    try {
      let queryAuthorizationResponse = await healthStore.getAuthorizations(queryAuthorizationRequest);
      hilog.info(0x0000, 'testTag', 'Succeeded in getting authorization.');
      queryAuthorizationResponse.writeDataTypes.forEach(dataType => {
        hilog.info(0x0000, 'testTag', \`grantedWriteDataType is : ${dataType.name}\`);
      });
      queryAuthorizationResponse.readDataTypes.forEach(dataType => {
        hilog.info(0x0000, 'testTag', \`grantedReadDataTypes is : ${dataType.name}\`);
      });
    } catch (err) {
      hilog.error(0x0000, 'testTag', \`Failed to get authorization. Code: ${err.code}, message: ${err.message}\`);
    }
    

## Canceling Authorization

1.  Import the Health Service Kit functional module and related public modules.
    
    import { healthStore } from '@kit.HealthServiceKit';
    import { hilog } from '@kit.PerformanceAnalysisKit';
    
2.  Call [cancelAuthorizations](https://developer.huawei.com/consumer/en/doc/harmonyos-references/health-api-healthstore#section18660141352811) to revoke the authorization and process the returned result.
    
    try {
      await healthStore.cancelAuthorizations();
      hilog.info(0x0000, 'testTag', 'Succeeded in canceling authorization.');
    } catch (err) {
      hilog.error(0x0000, 'testTag', \`Failed to cancel authorization. Code: ${err.code}, message: ${err.message}\`);
    }
