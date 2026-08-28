# Workout Records

#### Scenario

Workout records record basic information of a workout, including start time, end time, workout type, statistics, and details. You can write, read, or delete workout records. Each workout record must be associated with a data source.

#### API Description

| 
API Name

 | 

Description

 |
| :-- | :-- |
| 

[saveData](https://developer.huawei.com/consumer/en/doc/harmonyos-references/health-api-healthstore#en-us_topic_0000001768344397_section1924917579222)(exerciseSequence: [ExerciseSequence](https://developer.huawei.com/consumer/en/doc/harmonyos-references/health-api-healthstore#section17704373316)\[\] | [ExerciseSequence](https://developer.huawei.com/consumer/en/doc/harmonyos-references/health-api-healthstore#section17704373316)): Promise<void>

 | 

Saves workout records. The input parameter is an [ExerciseSequence](https://developer.huawei.com/consumer/en/doc/harmonyos-references/health-api-healthstore#section17704373316) or an [ExerciseSequence](https://developer.huawei.com/consumer/en/doc/harmonyos-references/health-api-healthstore#section17704373316) array.

 |
| 

[readData](https://developer.huawei.com/consumer/en/doc/harmonyos-references/health-api-healthstore#en-us_topic_0000001768344397_section410015582312)<T extends [ExerciseSequence](https://developer.huawei.com/consumer/en/doc/harmonyos-references/health-api-healthstore#section17704373316)\>(request: [ExerciseSequenceReadRequest](https://developer.huawei.com/consumer/en/doc/harmonyos-references/health-api-healthstore#section17500162113363)): Promise<T\[\]>

 | 

Queries workout records. You can use [ExerciseSequenceReadRequest](https://developer.huawei.com/consumer/en/doc/harmonyos-references/health-api-healthstore#section17500162113363) to set query conditions and query data by data type, field, or time range.

 |
| 

[deleteData](https://developer.huawei.com/consumer/en/doc/harmonyos-references/health-api-healthstore#section9995200190)(exerciseSequence: [ExerciseSequence](https://developer.huawei.com/consumer/en/doc/harmonyos-references/health-api-healthstore#section17704373316) | [ExerciseSequence](https://developer.huawei.com/consumer/en/doc/harmonyos-references/health-api-healthstore#section17704373316)\[\]): Promise<void>

 | 

Deletes specific workout records based on the input parameter, which can be an [ExerciseSequence](https://developer.huawei.com/consumer/en/doc/harmonyos-references/health-api-healthstore#section17704373316) or an [ExerciseSequence](https://developer.huawei.com/consumer/en/doc/harmonyos-references/health-api-healthstore#section17704373316) array.

 |
| 

[deleteData](https://developer.huawei.com/consumer/en/doc/harmonyos-references/health-api-healthstore#section14926161311104)(request: [ExerciseSequenceDeleteRequest](https://developer.huawei.com/consumer/en/doc/harmonyos-references/health-api-healthstore#section207708111867) | [ExerciseSequenceDeleteRequest](https://developer.huawei.com/consumer/en/doc/harmonyos-references/health-api-healthstore#section207708111867)\[\]): Promise<void>

 | 

Deletes workout records by [ExerciseSequenceDeleteRequest](https://developer.huawei.com/consumer/en/doc/harmonyos-references/health-api-healthstore#section207708111867). You can delete data by data type, time range, or data source.

 |

#### Before Getting Started

-   Complete [Applying for Health Service Kit](../../../getting-started/applying-for-health-service-kit/document.md) and [Configuring the Client ID](../../../getting-started/configuring-the-client-id/document.md).
-   Before calling an API for the first time, call the [init](https://developer.huawei.com/consumer/en/doc/harmonyos-references/health-api-healthstore#section1571935817328) method to perform initialization.
-   Make sure that you have obtained users' authorization for your app to access specific data types by calling [User Authorization](../../managing-user-authorization/document.md#section0247115178), before calling the relevant APIs to access those data types.
-   For details about error codes, refer to [ArkTS API Error Codes](https://developer.huawei.com/consumer/en/doc/harmonyos-references/errorcode-healthservice). For FAQs, click [FAQs About Health Service Kit](../../../../faqs-about-health-service-kit/document.md).

#### Development Procedure

## Saving Workout Records

1.  Import the Health Service Kit functional module and related public modules.
    
    import { healthStore } from '@kit.HealthServiceKit';
    import { hilog } from '@kit.PerformanceAnalysisKit';
    
2.  Obtain **dataSourceId**. Refer to [Managing Data Sources](../../managing-data-sources/document.md) to insert a new data source or read an existing data source.
3.  Create a workout record.
    
    // Construct a running record.
    const startTime = 1698040800000; // 2023-10-23 14:00:00
    const endTime = 1698042600000; // 2023-10-23 14:30:00
    
    const runningSequence: healthStore.exerciseSequenceHelper.running.Model = {
      dataType: healthStore.exerciseSequenceHelper.DATA\_TYPE,
    // Pass the value of **dataSourceId** returned when you call **insertDataSource** to insert a new data source, or read the value of **dataSourceId** of an existing data source.
      dataSourceId: 'xxx',
      startTime: startTime, // 2023-10-23 14:00:00
      endTime: endTime, // 2023-10-23 14:30:00
      localDate: '10/23/2023',
      timeZone: '+0800',
      modifiedTime: new Date().getTime(),
      exerciseType: healthStore.exerciseSequenceHelper.running.EXERCISE\_TYPE,
      duration: 1800,
      summaries: {
        distance: {
          totalDistance: 2000
        },
        calorie: {
          totalCalories: 20
        },
        speed: {
          avg: 5,
          max: 6
        }
      },
      details: {
        exerciseHeartRate: \[
          {
            startTime: startTime,
            bpm: 88
          },
          {
            startTime: startTime + 5000,
            bpm: 89
          }
        \],
        speed: \[
          {
            startTime: startTime,
            speed: 2.5
          }, 
          {
            startTime: startTime + 5000,
            speed: 2.3
          }
        \],
        altitude: \[
          {
            startTime: startTime,
            altitude: 100
          }, 
          {
            startTime: startTime + 5000,
            altitude: 101
          }
        \]
      }
    };
    
4.  Call [saveData](https://developer.huawei.com/consumer/en/doc/harmonyos-references/health-api-healthstore#en-us_topic_0000001768344397_section1924917579222) to save the data and process the returned result.
    
    try {
      await healthStore.saveData(runningSequence);
      hilog.info(0x0000, 'testTag', 'Succeeded in saving data.');
    } catch (err) {
      hilog.error(0x0000, 'testTag', \`Failed to save data. Code: ${err.code}, message: ${err.message}\`);
    }
    

## Reading Workout Records

1.  Import the Health Service Kit functional module and related public modules.
    
    import { healthStore } from '@kit.HealthServiceKit';
    import { hilog } from '@kit.PerformanceAnalysisKit';
    
2.  Create a query request.
    
    // Query running records.
    const sequenceReadRequest: healthStore.ExerciseSequenceReadRequest<healthStore.exerciseSequenceHelper.running.DetailFields> = {
      startTime: 1698040800000,
      endTime: 1698042600000,
      exerciseType: healthStore.exerciseSequenceHelper.running.EXERCISE\_TYPE,
      count: 1,
      sortOrder: 1,
      readOptions: {
        withPartialDetails: \['exerciseHeartRate', 'altitude'\] 
     }
    };
    
3.  Call [readData](https://developer.huawei.com/consumer/en/doc/harmonyos-references/health-api-healthstore#en-us_topic_0000001768344397_section410015582312) to query the data and process the returned result.
    
    try {
      const runningSequences = await healthStore.readData<healthStore.exerciseSequenceHelper.running.Model>(sequenceReadRequest);
      hilog.info(0x0000, 'testTag', 'Succeeded in reading data.');
      runningSequences.forEach((runningSequence) => {
        hilog.info(0x0000, 'testTag', \`the start time is ${runningSequence.startTime}.\`);
        hilog.info(0x0000, 'testTag', \`the end time is ${runningSequence.endTime}.\`);
        Object.keys(runningSequence.summaries).forEach((key) => {
          Object.keys(runningSequence.summaries\[key\]).forEach((fieldName) => {
            hilog.info(0x0000, 'testTag', \`the summaries of ${key} field ${fieldName} is ${runningSequence.summaries\[key\]\[fieldName\]}.\`);
          });
        });
      });
    } catch (err) {
      hilog.error(0x0000, 'testTag', \`Failed to read data. Code: ${err.code}, message: ${err.message}\`);
    }
    

## Deleting Specific Workout Records

1.  Import the Health Service Kit functional module and related public modules.
    
    import { healthStore } from '@kit.HealthServiceKit';
    import { hilog } from '@kit.PerformanceAnalysisKit';
    
2.  Query the workout record to be deleted.
    
    // Query running records.
    const sequenceReadRequest: healthStore.ExerciseSequenceReadRequest<healthStore.exerciseSequenceHelper.running.DetailFields> = {
      startTime: 1698040800000,
      endTime: 1698042600000,
      exerciseType: healthStore.exerciseSequenceHelper.running.EXERCISE\_TYPE
    };
    const runningSequences = await healthStore.readData<healthStore.exerciseSequenceHelper.running.Model>(sequenceReadRequest);
    
3.  Call [deleteData](https://developer.huawei.com/consumer/en/doc/harmonyos-references/health-api-healthstore#section9995200190) to delete the data and process the returned result.
    
    try {
      for (let index = 0; index < runningSequences.length; index++) {
        const runningSequence = runningSequences\[index\];
        await healthStore.deleteData(runningSequence);
      }
      hilog.info(0x0000, 'testTag', 'Succeeded in deleting data.');
    } catch (err) {
      hilog.error(0x0000, 'testTag', \`Failed to delete data. Code: ${err.code}, message: ${err.message}\`);
    }
    

## Deleting Workout Records as Requested

1.  Import the Health Service Kit functional module and related public modules.
    
    import { healthStore } from '@kit.HealthServiceKit';
    import { hilog } from '@kit.PerformanceAnalysisKit';
    
2.  Create a deletion request.
    
    let exerciseSequenceDeleteRequest: healthStore.ExerciseSequenceDeleteRequest= {
      exerciseType: healthStore.exerciseSequenceHelper.running.EXERCISE\_TYPE,
      startTime: 1698633801000,
      endTime: 1698633801000
    }
    
3.  Call [deleteData](https://developer.huawei.com/consumer/en/doc/harmonyos-references/health-api-healthstore#section14926161311104) to delete the data and process the returned result.
    
    try {
      await healthStore.deleteData(exerciseSequenceDeleteRequest);
      hilog.info(0x0000, 'testTag', 'Succeeded in deleting data.');
    } catch (err) {
      hilog.error(0x0000, 'testTag', \`Failed to delete data. Code: ${err.code}, message: ${err.message}\`);
    }
