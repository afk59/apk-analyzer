# Manual Data Synchronization

#### Scenario

The Huawei Health app may fail to sync data to the cloud in a timely manner. As a result, your app may not obtain the user's latest health and fitness data from the Health Service Kit cloud promptly. To address this issue, we allow users to manually trigger data syncing once your app obtains their authorization.

#### OAuth Scope

To apply for the required scopes, go to **Data Synchronization** > **Manual Data Synchronization** on the Console of HUAWEI Developers.

| 
Scope

 | 

Description

 |
| :-- | :-- |
| 

https://www.huawei.com/healthkit/huaweihealthdata.cloudsync

 | 

Allows Huawei Health to sync personal data to the cloud (based on data syncing settings in Huawei Health).

 |

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/33/v3/mihQtjKuRl6v9nF21Te7CA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062106Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=DB6D8A3250721A3C686FF3EAC852B1BD17049EE0450AE42D934476DC78AE4772)

This scope is available only to enterprise developer accounts.

#### API Description

| 
API Name

 | 

Description

 |
| :-- | :-- |
| 

[syncAll](https://developer.huawei.com/consumer/en/doc/harmonyos-references/health-api-healthstore#section7421175995618)(): Promise<void>

 | 

Proactively triggers data syncing.

 |

#### Before Getting Started

-   Complete [Applying for Health Service Kit](../../getting-started/applying-for-health-service-kit/document.md) and [Configuring the Client ID](../../getting-started/configuring-the-client-id/document.md).
-   Before calling an API for the first time, call the [init](https://developer.huawei.com/consumer/en/doc/harmonyos-references/health-api-healthstore#section1571935817328) method to perform initialization.
-   Use the [User Authorization](../managing-user-authorization/document.md#section0247115178) API to guide the user to grant authorization. For details, refer to the **scopes** parameter in [AuthorizationRequest](https://developer.huawei.com/consumer/en/doc/harmonyos-references/health-api-healthstore#en-us_topic_0000001768344397_section1956619544498). Call the manual data synchronization API after the user has authorized the data synchronization permission.
-   For details about error codes, refer to [ArkTS API Error Codes](https://developer.huawei.com/consumer/en/doc/harmonyos-references/errorcode-healthservice). For FAQs, click [FAQs About Health Service Kit](../../../faqs-about-health-service-kit/document.md).

#### Development Procedure

1.  Import the Health Service Kit functional module and related public modules.
    
    import { healthStore } from '@kit.HealthServiceKit';
    import { hilog } from '@kit.PerformanceAnalysisKit';
    
2.  Call [syncAll](https://developer.huawei.com/consumer/en/doc/harmonyos-references/health-api-healthstore#section7421175995618) to sync data and process the returned result.
    
    try {
      await healthStore.syncAll();
      hilog.info(0x0000, 'testTag', 'Succeeded in synchronizing data.');
    **}** catch (err) {
      hilog.error(0x0000, 'testTag', \`Failed to synchronize data. Code: ${err.code}, message: ${err.message}\`);
    }
