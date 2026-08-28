# Health Records

#### Scenario

Health records record basic information including the start time, end time, data type, field value, and detailed data. You can write, read, or delete health records. Each health record must be associated with a data source.

#### API Description

| 
API Name

 | 

Description

 |
| :-- | :-- |
| 

[saveData](https://developer.huawei.com/consumer/en/doc/harmonyos-references/health-api-healthstore#en-us_topic_0000001768344397_section1840517577188)(healthSequence: [HealthSequence](https://developer.huawei.com/consumer/en/doc/harmonyos-references/health-api-healthstore#section1038711561532)\[\] | [HealthSequence](https://developer.huawei.com/consumer/en/doc/harmonyos-references/health-api-healthstore#section1038711561532)): Promise<void>

 | 

Saves health records. The input parameter is a [HealthSequence](https://developer.huawei.com/consumer/en/doc/harmonyos-references/health-api-healthstore#section1038711561532) or a [HealthSequence](https://developer.huawei.com/consumer/en/doc/harmonyos-references/health-api-healthstore#section1038711561532) array.

 |
| 

[readData](https://developer.huawei.com/consumer/en/doc/harmonyos-references/health-api-healthstore#en-us_topic_0000001768344397_section85773683317)<T extends [HealthSequence](https://developer.huawei.com/consumer/en/doc/harmonyos-references/health-api-healthstore#section1038711561532)\>(request: [HealthSequenceReadRequest](https://developer.huawei.com/consumer/en/doc/harmonyos-references/health-api-healthstore#section11615192919718)): Promise<T\[\]>

 | 

Queries health records. You can use [HealthSequenceReadRequest](https://developer.huawei.com/consumer/en/doc/harmonyos-references/health-api-healthstore#section11615192919718) to set query conditions and query data by data type, field, or time range.

 |
| 

[deleteData](https://developer.huawei.com/consumer/en/doc/harmonyos-references/health-api-healthstore#section15631966119)(healthSequence: [HealthSequence](https://developer.huawei.com/consumer/en/doc/harmonyos-references/health-api-healthstore#section1038711561532) | [HealthSequence](https://developer.huawei.com/consumer/en/doc/harmonyos-references/health-api-healthstore#section1038711561532)\[\]): Promise<void>

 | 

Deletes specific health records based on the input parameter, which can be a [HealthSequence](https://developer.huawei.com/consumer/en/doc/harmonyos-references/health-api-healthstore#section1038711561532) or a [HealthSequence](https://developer.huawei.com/consumer/en/doc/harmonyos-references/health-api-healthstore#section1038711561532) array.

 |
| 

[deleteData](https://developer.huawei.com/consumer/en/doc/harmonyos-references/health-api-healthstore#section8621134581112)(request: [HealthSequenceDeleteRequest](https://developer.huawei.com/consumer/en/doc/harmonyos-references/health-api-healthstore#section1779165141119) | [HealthSequenceDeleteRequest](https://developer.huawei.com/consumer/en/doc/harmonyos-references/health-api-healthstore#section1779165141119)\[\]): Promise<void>

 | 

Deletes health records by [HealthSequenceDeleteRequest](https://developer.huawei.com/consumer/en/doc/harmonyos-references/health-api-healthstore#section1779165141119). You can delete data by data type, time range, or data source.

 |

#### Before Getting Started

-   Complete [Applying for Health Service Kit](../../../getting-started/applying-for-health-service-kit/document.md) and [Configuring the Client ID](../../../getting-started/configuring-the-client-id/document.md).
-   Before calling an API for the first time, call the [init](https://developer.huawei.com/consumer/en/doc/harmonyos-references/health-api-healthstore#section1571935817328) method to perform initialization.
-   Make sure that you have obtained users' authorization for your app to access specific data types by calling [User Authorization](../../managing-user-authorization/document.md#section0247115178), before calling the relevant APIs to access those data types.
-   For details about error codes, refer to [ArkTS API Error Codes](https://developer.huawei.com/consumer/en/doc/harmonyos-references/errorcode-healthservice). For FAQs, click [FAQs About Health Service Kit](../../../../faqs-about-health-service-kit/document.md).

#### Development Procedure

## Saving Health Records

1.  Import the Health Service Kit functional module and related public modules.
    
    import { healthStore } from '@kit.HealthServiceKit';
    import { hilog } from '@kit.PerformanceAnalysisKit';
    
2.  Obtain **dataSourceId**. Refer to [Managing Data Sources](../../managing-data-sources/document.md) to insert a new data source or read an existing data source.
3.  Create a health record.
    
    let healthSequence: healthStore.healthSequenceHelper.sleepRecord.Model = {
      summaries: {
        fallAsleepTime: 1695740400000, // 2023-09-26 23:00:00
        wakeupTime: 1695769200000, // 2023-09-27 7:00:00
        sleepScore: 80,
        wakeCount: 2,
        sleepType: 1,
        shallowDuration: 14400,
        deepDuration: 7200,
        dreamDuration: 7200,
        wakeDuration: 0,
        duration: 28800
      },
      dataType: healthStore.healthSequenceHelper.sleepRecord.DATA\_TYPE,
    // Pass the value of **dataSourceId** returned when you call **insertDataSource** to insert a new data source, or read the value of **dataSourceId** of an existing data source.
      dataSourceId: 'xxx',
      localDate: '09/26/2023',
      startTime: 1695740400000,
      endTime: 1695769200000,
      timeZone: '+0800',
      modifiedTime: 1695769200000,
      details: {
        sleepSegment: \[
          {
            startTime: 1695740400000, // 2023-09-26 23:00:00
            endTime: 1695747600000, // 2023-09-27 01:00:00
            sleepStatus: 2
          },
          {
            startTime: 1695747600000, // 2023-09-27 01:00:00
            endTime: 1695754800000, // 2023-09-27 03:00:00
            sleepStatus: 1
          },
          {
            startTime: 1695754800000, // 2023-09-27 03:00:00
            endTime: 1695762000000, // 2023-09-27 05:00:00
            sleepStatus: 3
          },
          {
            startTime: 1695762000000, // 2023-09-27 05:00:00
            endTime: 1695769200000, // 2023-09-27 07:00:00
            sleepStatus: 2
          }
        \]
      }
    }
    
4.  Call [saveData](https://developer.huawei.com/consumer/en/doc/harmonyos-references/health-api-healthstore#en-us_topic_0000001768344397_section1840517577188) to save the data and process the returned result.
    
    try {
      await healthStore.saveData(healthSequence);
      hilog.info(0x0000, 'testTag', 'Succeeded in saving data.');
    } catch (err) {
      hilog.error(0x0000, 'testTag', \`Failed to save data. Code: ${err.code}, message: ${err.message}\`);
    }
    

## Reading Health Records

1.  Import the Health Service Kit functional module and related public modules.
    
    import { healthStore } from '@kit.HealthServiceKit';
    import { hilog } from '@kit.PerformanceAnalysisKit';
    
2.  Create a request for querying health records.
    
    let healthSequenceReadRequest: healthStore.HealthSequenceReadRequest = {
      healthSequenceDataType: healthStore.healthSequenceHelper.sleepRecord.DATA\_TYPE,
      startTime: 1695740400000,
      endTime: 1695769200000,
      readOptions: {
        withDetails: true
      }
    }
    
3.  Call [readData](https://developer.huawei.com/consumer/en/doc/harmonyos-references/health-api-healthstore#en-us_topic_0000001768344397_section85773683317) to query the data and process the returned result.
    
    try {
      const healthSequences = await healthStore.readData(healthSequenceReadRequest);
      hilog.info(0x0000, 'testTag', 'Succeeded in reading data.'); 
      healthSequences.forEach((healthSequence) => {
        hilog.info(0x0000, 'testTag', \`the start time is ${healthSequence.startTime}.\`);
        hilog.info(0x0000, 'testTag', \`the end time is ${healthSequence.endTime}.\`);
        Object.keys(healthSequence.summaries).forEach((key) => {
          hilog.info(0x0000, 'testTag', \`the summaries of ${key} is ${healthSequence.summaries\[key\]}.\`);
        });
      });
    } catch (err) {
      hilog.error(0x0000, 'testTag', \`Failed to read data. Code: ${err.code}, message: ${err.message}\`);
    }
    

## Deleting Specific Health Records

1.  Import the Health Service Kit functional module and related public modules.
    
    import { healthStore } from '@kit.HealthServiceKit';
    import { hilog } from '@kit.PerformanceAnalysisKit';
    
2.  Query the health records to be deleted.
    
    let healthSequenceReadRequest: healthStore.HealthSequenceReadRequest = {
      healthSequenceDataType: healthStore.healthSequenceHelper.sleepRecord.DATA\_TYPE,
      startTime: 1695740400000,
      endTime: 1695769200000
    }
    const healthSequences = await healthStore.readData(healthSequenceReadRequest);
    
3.  Call [deleteData](https://developer.huawei.com/consumer/en/doc/harmonyos-references/health-api-healthstore#section15631966119) to delete the data and process the returned result.
    
    try {
      for (let index = 0; index < healthSequences.length; index++) {
        const healthSequence = healthSequences\[index\];
        await healthStore.deleteData(healthSequence);
      }
      hilog.info(0x0000, 'testTag', 'Succeeded in deleting data.');
    } catch (err) {
      hilog.error(0x0000, 'testTag', \`Failed to delete data. Code: ${err.code}, message: ${err.message}\`);
    }
    

## Deleting Health Records as Requested

1.  Import the Health Service Kit functional module and related public modules.
    
    import { healthStore } from '@kit.HealthServiceKit';
    import { hilog } from '@kit.PerformanceAnalysisKit';
    
2.  Create a request for deleting health records.
    
    const healthSequenceDeleteRequest: healthStore.HealthSequenceDeleteRequest= {
      healthSequenceDataType: healthStore.healthSequenceHelper.sleepRecord.DATA\_TYPE,
      startTime: 1695740400000,
      endTime: 1695769200000
    }
    
3.  Call [deleteData](https://developer.huawei.com/consumer/en/doc/harmonyos-references/health-api-healthstore#section8621134581112) to delete the data and process the returned result.
    
    try {
      await healthStore.deleteData(healthSequenceDeleteRequest);
      hilog.info(0x0000, 'testTag', 'Succeeded in deleting data.');
    } catch (err) {
      hilog.error(0x0000, 'testTag', \`Failed to delete data. Code: ${err.code}, message: ${err.message}\`);
    }
