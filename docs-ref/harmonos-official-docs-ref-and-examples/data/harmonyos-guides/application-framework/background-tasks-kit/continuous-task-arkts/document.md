# Continuous Task (ArkTS)

#### Overview

## Introduction

If an application has a perceivable task that needs to run in an extended period of time in the background, it can request a continuous task to prevent itself from being suspended. Examples of continuous tasks include music playback and navigation in the background. Within a continuous task, the application can concurrently request multiple types of tasks and update the task types. When the application operates in the background, the system performs consistency check to ensure that the application is executing the corresponding continuous task. Upon successful request for a continuous task, the notification panel displays the message associated with the task. If the user deletes the message, the system automatically terminates the task.

## Use Cases

The table below lists the types of continuous tasks, which are used in various scenarios. You can select a task type suitable for your case based on the description.

**Table 1** Continuous task types

| Name | Description | Item | Example Scenario |
| :-- | :-- | :-- | :-- |
| DATA\_TRANSFER | Data transfer. | dataTransfer | Non-hosting uploading and downloading operations, like those occurring in the background of a web browser for data transfer. |
| AUDIO\_PLAYBACK | Audio and video playback. | audioPlayback | 
Audio and video playback in the background; audio and video casting.

**Note**: It can be used in atomic services.

 |
| AUDIO\_RECORDING | Recording. | audioRecording | Recording and screen capture in the background. |
| LOCATION | Positioning and navigation. | location | Positioning and navigation. |
| BLUETOOTH\_INTERACTION | Bluetooth-related services. | bluetoothInteraction | An application transitions into the background during the process of file transfer using Bluetooth. |
| MULTI\_DEVICE\_CONNECTION | Multi-device connection. | multiDeviceConnection | 

Distributed service connection and casting.

**Note**: It can be used in atomic services.

 |
| VOIP | 

Audio and video calls.

**Note**: It is supported since API version 13.

 | voip | Chat applications (with audio and video services) transition into the background during audio and video calls. |
| TASK\_KEEPING | 

Computing tasks.

**Note**: Starting from API version 21, this capability is available for 2-in-1 devices, and non-2-in-1 devices that have obtained the ACL permission [ohos.permission.KEEP\_BACKGROUND\_RUNNING\_SYSTEM](../../../system/security/application-access-control/application-permission-management/application-permissions/restricted-permissions/document.md#ohospermissionkeep_background_running_system). In API version 20 and earlier versions, this task type is limited to PCs/2-in-1 devices only.

 | taskKeeping | Antivirus software is running. |
| MODE\_AV\_PLAYBACK\_AND\_RECORD | 

Multimedia services.

**Note**: It is supported since API version 22.

 | avPlaybackAndRecord | When an application is in the background during audio/video playback, recording, or audio/video calls, you can select either this task type or the corresponding continuous task type for these three scenarios. For example, in the audio/video playback scenario, you can choose either **AUDIOPLAYBACK** or **MODE\_AVPLAYBACK\_AND\_RECORD**. |
| MODE\_SPECIAL\_SCENARIO\_PROCESSING22+ | 

Special scenarios. (Available only for smartphones, tablets, PCs/2-in-1 devices.)

**Note**: It is supported since API version 22.

 | specialScenarioProcessing | Exporting media files in the background, and using third-party casting components for background casting. |

Description of **DATA\_TRANSFER**:

-   During data transfer, if an application uses the [@ohos.request (Upload and Download)](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-request) to hand over tasks to the system, the application will be suspended in the background even if it has requested the continuous task of the **DATA\_TRANSFER** type.
    
-   During data transfer, the application needs to update the progress. If the progress is not updated for a long time (more than 10 minutes after the first update), the continuous task of the **DATA\_TRANSFER** type will be canceled. The notification type of the progress update must be live view. For details, see the example in [startBackgroundRunning()](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-resourceschedule-backgroundtaskmanager#backgroundtaskmanagerstartbackgroundrunning12).
    

Description of **AUDIO\_PLAYBACK**:

-   Casting audio and video involves transmitting content from one device to another for playback purposes. If the application transitions to the background while casting, the continuous task checks the audio and video playback and casting services. The task will persist as long as either the audio and video playback or casting service is running properly.
    
-   If the application needs to play media (STREAM\_USAGE\_MUSIC, STREAM\_USAGE\_MOVIE, or STREAM\_USAGE\_AUDIOBOOK) or games (STREAM\_USAGE\_GAME) in the background, it must access the [AVSession](../../../media/avsession-kit/about-this-kit/document.md) service and request a continuous task of the AUDIO\_PLAYBACK type.
    
-   In addition to the aforementioned playback types, when an application needs to run other user-perceptible tasks in the background for a long time, it must request continuous tasks of the **AUDIO\_PLAYBACK** type, without accessing AVSession.
    
-   If the application does not comply with the preceding access specifications, it will be muted and suspended by the system when switched to the background. It can resume playback only when it returns to the foreground.
    
-   Starting from API version 20, if a continuous task of the **AUDIO\_PLAYBACK** type is requested without being connected to AVSession, a notification will appear in the notification panel once the task is successfully requested. Once AVSession is connected, the background task module will no longer send notifications; instead, notifications will be sent by AVSession. For API version 19 and earlier versions, the background task module does not display notifications in the notification panel.
    
-   The system may freeze an application that requests a continuous task of the **AUDIO\_PLAYBACK** type if no audio is playing while the application is in the background.
    

## Constraints

**Ability restrictions**: In the stage model, only the UIAbility can request continuous tasks. In the FA model, only the ServiceAbility can request continuous tasks. Continuous tasks can be requested by the current application on the current device or across devices or by other applications. However, the capability to make cross-device or cross-application requests is restricted to system applications.

**Quantity restrictions**:

-   Since API version 21, a single UIAbility can request multiple continuous tasks simultaneously, with a maximum limit of 10. For details, see [startBackgroundRunning()](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-resourceschedule-backgroundtaskmanager#backgroundtaskmanagerstartbackgroundrunning21). For API version 20 and earlier versions, a UIAbility (ServiceAbility in the FA model) can only request one continuous task at a time. If a UIAbility already has an ongoing continuous task, it can only submit a new request after the existing task is completed. If an application needs to request multiple continuous tasks simultaneously, it must create multiple UIAbilities.
-   If an application has multiple UIAbilities, once one UIAbility successfully requests a continuous task, all processes of the entire application will not be suspended.

**Running restrictions**:

-   If an application requests a continuous task but does not carry out the relevant service, the system imposes restrictions on the application. For example, if the system detects that an application has requested a continuous task of the AUDIO\_PLAYBACK type but does not play audio, the application will be suspended when it returns to the background.
    
-   If an application requests a continuous task but carries out a service that does not match the requested type, the system imposes restrictions on the application. The application will be suspended when it returns to the background. For example, if the system detects that an application requests a continuous task of the AUDIO\_PLAYBACK type, but the application is playing audio (corresponding to the AUDIO\_PLAYBACK type) and recording (corresponding to the AUDIO\_RECORDING type), the system enforces management measures.
    
-   When an application's operations are completed after a continuous task request, the system imposes restrictions on the application. The application will be suspended when it returns to the background.
    
-   If the background load of the process that runs a continuous task is higher than the corresponding typical load for a long period of time, the system performs certain control. The application will be suspended or terminated when it is switched to the background.
    

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/02/v3/2CO6OSL-SGGluhEei4oaKg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061950Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=3C2CDEEC568C040F48AA16F4C75E2E45F21B0FE26AAA3D9A75002842AA2E653A)

An application must proactively cancel a continuous task once the task is completed. Otherwise, the application will be suspended when moved to the background. For example, when a user taps the UI to pause music playback, the application must cancel the continuous task in a timely manner. When the user taps the UI again to continue music playback, the application needs to request a continuous task.

If an application that plays an audio in the background is [interrupted](../../../media/audio-kit/audio-focus-and-audio-session-management/introduction-to-audio-focus/document.md), the system automatically detects and stops the continuous task. The application must request a continuous task again to restart the playback.

When an application that plays audio in the background stops a continuous task, it must suspend or stop the audio stream. Otherwise, the application will be forcibly terminated by the system.

#### Available APIs

**Table 2** Main APIs for continuous tasks

The table below uses promise as an example to describe the APIs used for developing continuous tasks. For details about more APIs and their usage, see [Background Task Management](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-resourceschedule-backgroundtaskmanager).

| API | Description |
| :-- | :-- |
| [startBackgroundRunning(context: Context, bgMode: BackgroundMode, wantAgent: WantAgent): Promise<void>](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-resourceschedule-backgroundtaskmanager#backgroundtaskmanagerstartbackgroundrunning-1) | Requests a continuous task. A UIAbility can apply for only one continuous task at a time. If a UIAbility already has an ongoing continuous task, it can only submit a new request after the existing task is completed. |
| [stopBackgroundRunning(context: Context): Promise<void>](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-resourceschedule-backgroundtaskmanager#backgroundtaskmanagerstopbackgroundrunning-1) | Cancels a continuous task. |
| [startBackgroundRunning(context: Context, request: ContinuousTaskRequest): Promise<ContinuousTaskNotification>](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-resourceschedule-backgroundtaskmanager#backgroundtaskmanagerstartbackgroundrunning21) | Requests multiple continuous tasks. This API enables a UIAbility to request multiple continuous tasks simultaneously, with a maximum limit of 10. |
| [stopBackgroundRunning(context: Context, continuousTaskId: number): Promise<void>](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-resourceschedule-backgroundtaskmanager#backgroundtaskmanagerstopbackgroundrunning21) | Cancels a continuous task with the specified ID. |

#### How to Develop

The following walks you through how to request a continuous task for recording to implement the following functionalities:

-   When a user touches **Request Continuous Task**, the application requests a continuous task for recording, and a message is displayed in the notification bar, indicating that a recording task is running.
    
-   When a user touches **Cancel Continuous Task**, the application cancels the continuous task, and the notification message is removed.
    

## Stage Model

1.  Declare the **ohos.permission.KEEP\_BACKGROUND\_RUNNING** permission. For details, see [Declaring Permissions](../../../system/security/application-access-control/application-permission-management/requesting-application-permissions/declaring-permissions/document.md).
    
2.  Declare the continuous task type.
    
    Declare the type of the continuous task for the target UIAbility under **abilities** in the [module.json5 file](../../../getting-started/development-fundamentals/application-configuration-files-in-stage-model/module-json5-configuration-file/document.md). Set the corresponding [configuration item](#use-cases) in the configuration file.
    
     "module": {
         "abilities": \[
             {
                 "backgroundModes": \[
                  // Configuration item of the continuous task type
                 "audioRecording",
                 "bluetoothInteraction",
                 "audioPlayback"
                 \]
             }
         \],
         // ...
     }
    
3.  Import the modules.
    
    Import the modules related to continuous tasks: @ohos.resourceschedule.backgroundTaskManager and @ohos.app.ability.wantAgent. Import other modules based on the project requirements.
    
     import { backgroundTaskManager } from '@kit.BackgroundTasksKit';
     import { BusinessError } from '@kit.BasicServicesKit';
     import { wantAgent, WantAgent } from '@kit.AbilityKit';
     // In atomic services, please remove the WantAgent import.
    
4.  Request and cancel a continuous task.
    
    The code snippet below shows how an application requests and cancels a continuous task for itself.
    
    Since API version 15, you can use [on('continuousTaskCancel')](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-resourceschedule-backgroundtaskmanager#backgroundtaskmanageroncontinuoustaskcancel15) to listen for the cancellation of a continuous task.
    
    Since API version 16, you can use [BackgroundSubMode](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-resourceschedule-backgroundtaskmanager#backgroundsubmode16) to implement the Bluetooth car key function.
    
    function callback(info: backgroundTaskManager.ContinuousTaskCancelInfo) {
      // ID of a continuous task.
      console.info('OnContinuousTaskCancel callback id ' + info.id);
      // Reason for canceling the continuous task.
      console.info('OnContinuousTaskCancel callback reason ' + info.reason);
    }
    
    @Entry
    @Component
    struct Index {
      @State message: string = 'ContinuousTask';
      // Obtain the UIAbility context of the page by calling getUIContext().getHostContext().
      private context: Context | undefined = this.getUIContext().getHostContext();
    
      // ...
    
      OnContinuousTaskCancel() {
        try {
          backgroundTaskManager.on('continuousTaskCancel', callback);
          console.info(\`Succeeded in operationing OnContinuousTaskCancel.\`);
        } catch (error) {
          console.error(\`Operation OnContinuousTaskCancel failed. code is ${(error as BusinessError).code} message is ${(error as BusinessError).message}\`);
        }
      }
    
      OffContinuousTaskCancel() {
        try {
          // If the callback parameter is not passed, all callbacks associated with the specified event are canceled.
          backgroundTaskManager.off('continuousTaskCancel', callback);
          console.info(\`Succeeded in operationing OffContinuousTaskCancel.\`);
        } catch (error) {
          console.error(\`Operation OffContinuousTaskCancel failed. code is ${(error as BusinessError).code} message is ${(error as BusinessError).message}\`);
        }
      }
    
      // Request a continuous task using .then().
      startContinuousTask() {
        let wantAgentInfo: wantAgent.WantAgentInfo = {
          // List of operations to be executed after the notification is clicked.
          // Add the bundleName and abilityName of the application to start.
          wants: \[
            {
              bundleName: 'ohos.samples.continuoustask',
              abilityName: 'MainAbility'
            }
          \],
          // Specify the action to perform (starting the ability) after the notification message is clicked.
          actionType: wantAgent.OperationType.START\_ABILITY,
          // Custom request code.
          requestCode: 0,
          // Execution attribute of the operation to perform after the notification is clicked.
          actionFlags: \[wantAgent.WantAgentFlags.UPDATE\_PRESENT\_FLAG\],
          // CAR\_KEY subtype, which takes effect only when a continuous task of the bluetoothInteraction type is requested. This subtype is supported since API version 16.
          // Ensure that the key value in the extraInfo parameter is backgroundTaskManager.BackgroundModeType.SUB\_MODE. Otherwise, the subtype does not take effect.
          // extraInfo: {
            // \[backgroundTaskManager.BackgroundModeType.SUB\_MODE\] :backgroundTaskManager.BackgroundSubMode.CAR\_KEY
          // }
        };
    
        try {
          // Obtain the WantAgent object by using the getWantAgent API of the wantAgent module.
          // In atomic services, replace the following line of code with wantAgent.getWantAgent(wantAgentInfo).then((wantAgentObj: object) => {.
          wantAgent.getWantAgent(wantAgentInfo).then((wantAgentObj: WantAgent) => {
            try {
              let list: string\[\] = \['audioPlayback'\];
              // let list: string\[\] = \['bluetoothInteraction'\]; The bluetoothInteraction type is included in the continuous task, and the CAR\_KEY subtype is valid.
              backgroundTaskManager.startBackgroundRunning(this.context, list, wantAgentObj).
                then((res: backgroundTaskManager.ContinuousTaskNotification) => {
                console.info('Operation startBackgroundRunning succeeded');
                // Execute the continuous task logic, for example, audio playback.
                // The system checks the authenticity of the service scenario. If the corresponding service is not executed, the system may cancel the continuous task and suspend the application.
                // ...
              }).catch((error: BusinessError) => {
                console.error(\`Failed to Operation startBackgroundRunning. code is ${error.code} message is ${error.message}\`);
              });
            } catch (error) {
              console.error(\`Failed to Operation startBackgroundRunning. code is ${(error as BusinessError).code} message is ${(error as BusinessError).message}\`);
            }
          });
        } catch (error) {
          console.error(\`Failed to Operation getWantAgent. code is ${(error as BusinessError).code} message is ${(error as BusinessError).message}\`);
        }
      }
    
      // Cancel a continuous task using .then().
      stopContinuousTask() {
        backgroundTaskManager.stopBackgroundRunning(this.context).then(() => {
          console.info(\`Succeeded in operationing stopBackgroundRunning.\`);
          // ...
        }).catch((err: BusinessError) => {
          console.error(\`Failed to operation stopBackgroundRunning. Code is ${err.code}, message is ${err.message}\`);
        });
      }
    
      build() {
        Row() {
          Column() {
            Text('Index')
              .fontSize(50)
              .fontWeight(FontWeight.Bold)
    
            Button() {
              Text('Request a continuous task').fontSize(25).fontWeight(FontWeight.Bold)
            }
            .type(ButtonType.Capsule)
            .margin({ top: 10 })
            .backgroundColor('#0D9FFB')
            .width(250)
            .height(40)
            .id('applyContinuousTask')
            .onClick(() => {
              // Request a continuous task by clicking a button.
              this.startContinuousTask();
            })
    
            Button() {
              Text('Cancel the continuous task').fontSize (25).fontWeight (FontWeight.Bold)
            }
            .type(ButtonType.Capsule)
            .margin({ top: 10 })
            .backgroundColor('#0D9FFB')
            .width(250)
            .height(40)
            .id('resetContinuousTask')
            .onClick(() => {
              // Stop the continuous task.
    
              // Cancel the continuous task through a button.
              this.stopContinuousTask();
            })
    
            Button() {
              Text('Register a callback for canceling a continuous task').fontSize (25).fontWeight(FontWeight.Bold)
            }
            .type(ButtonType.Capsule)
            .margin({ top: 10 })
            .backgroundColor('#0D9FFB')
            .width(250)
            .height(40)
            .onClick(() => {
              // Use a button to register a callback for canceling a continuous task.
              this.OnContinuousTaskCancel();
            })
    
            Button() {
              Text('Unregister a callback for canceling the continuous task').fontSize (25).fontWeight(FontWeight.Bold)
            }
            .type(ButtonType.Capsule)
            .margin({ top: 10 })
            .backgroundColor('#0D9FFB')
            .width(250)
            .height(40)
            .onClick(() => {
              // Use a button to unregister a callback for canceling a continuous task.
              this.OffContinuousTaskCancel();
            })
            // ...
          }
          .width('100%')
        }
        .height('100%')
      }
    }
    
5.  Request and cancel a continuous task using **async**/**await**.
    
    The code snippet below shows how an application requests and cancels a continuous task using **async**/**await** for itself.
    
    Since API version 15, you can use [on('continuousTaskCancel')](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-resourceschedule-backgroundtaskmanager#backgroundtaskmanageroncontinuoustaskcancel15) to listen for the cancellation of a continuous task.
    
    Since API version 16, you can use [BackgroundSubMode](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-resourceschedule-backgroundtaskmanager#backgroundsubmode16) to implement the Bluetooth car key function.
    
    @Entry
    @Component
    struct IndexAsyncAndAwait {
      @State message: string = 'ContinuousTask';
      // Obtain the UIAbility context of the page by calling getUIContext().getHostContext().
      private context: Context | undefined = this.getUIContext().getHostContext();
    
      // ...
    
      // Request a continuous task using async/await.
      async startContinuousTask() {
        let wantAgentInfo: wantAgent.WantAgentInfo = {
          // List of operations to be executed after the notification is clicked.
          // Add the bundleName and abilityName of the application to start.
          wants: \[
            {
              bundleName: 'ohos.samples.continuoustask',
              abilityName: 'MainAbility'
            }
          \],
          // Specify the action to perform (starting the ability) after the notification message is clicked.
          actionType: wantAgent.OperationType.START\_ABILITY,
          // Custom request code.
          requestCode: 0,
          // Execution attribute of the operation to perform after the notification is clicked.
          actionFlags: \[wantAgent.WantAgentFlags.UPDATE\_PRESENT\_FLAG\],
          // CAR\_KEY subtype, which takes effect only when a continuous task of the bluetoothInteraction type is requested. This subtype is supported since API version 16.
          // Ensure that the key value in the extraInfo parameter is backgroundTaskManager.BackgroundModeType.SUB\_MODE. Otherwise, the subtype does not take effect.
          // extraInfo: {
            // \[backgroundTaskManager.BackgroundModeType.SUB\_MODE\] :backgroundTaskManager.BackgroundSubMode.CAR\_KEY
          // }
        };
    
        try {
          // Obtain the WantAgent object by using the getWantAgent API of the wantAgent module.
          // In atomic services, replace the following line of code with const wantAgentObj: object = await wantAgent.getWantAgent(wantAgentInfo);.
          const wantAgentObj: WantAgent = await wantAgent.getWantAgent(wantAgentInfo);
          try {
            let list: string\[\] = \['audioPlayback'\];
            // let list: string\[\] = \['bluetoothInteraction'\]; The bluetoothInteraction type is included in the continuous task, and the CAR\_KEY subtype is valid.
            // In atomic services, let list: Array<string> = \["audioPlayback"\];
            const res: backgroundTaskManager.ContinuousTaskNotification =
              await backgroundTaskManager.startBackgroundRunning(this.context as Context, list, wantAgentObj);
            console.info(\`Operation startBackgroundRunning succeeded, notificationId: ${res.notificationId}\`);
            // Execute the continuous task logic, for example, audio playback.
            // ...
          } catch (error) {
            console.error(\`Failed to Operation startBackgroundRunning. Code is ${(error as BusinessError).code}, message is ${(error as BusinessError).message}\`);
          }
        } catch (error) {
          console.error(\`Failed to Operation getWantAgent. Code is ${(error as BusinessError).code}, message is ${(error as BusinessError).message}\`);
        }
      }
    
      // Cancel a continuous task using async/await.
      async stopContinuousTask() {
        try {
          await backgroundTaskManager.stopBackgroundRunning(this.context);
          console.info(\`Succeeded in operationing stopBackgroundRunning.\`);
          // ...
        } catch (error) {
          console.error(\`Failed to operation stopBackgroundRunning. Code is ${(error as BusinessError).code}, message is ${(error as BusinessError).message}\`)
        }
      }
    
      build() {
        Row() {
          Column() {
            Text('Index')
              .fontSize(50)
              .fontWeight(FontWeight.Bold)
    
            Button() {
              Text('Request a continuous task').fontSize(25).fontWeight(FontWeight.Bold)
            }
            .type(ButtonType.Capsule)
            .margin({ top: 10 })
            .backgroundColor('#0D9FFB')
            .width(250)
            .height(40)
            .id('applyContinuousTask')
            .onClick(() => {
              // Request a continuous task by clicking a button.
              this.startContinuousTask();
            })
    
            Button() {
              Text('Cancel the continuous task').fontSize (25).fontWeight (FontWeight.Bold)
            }
            .type(ButtonType.Capsule)
            .margin({ top: 10 })
            .backgroundColor('#0D9FFB')
            .width(250)
            .height(40)
            .id('resetContinuousTask')
            .onClick(() => {
              // Stop the continuous task.
    
              // Cancel the continuous task through a button.
              this.stopContinuousTask();
            })
            // ...
          }
          .width('100%')
        }
        .height('100%')
      }
    }
