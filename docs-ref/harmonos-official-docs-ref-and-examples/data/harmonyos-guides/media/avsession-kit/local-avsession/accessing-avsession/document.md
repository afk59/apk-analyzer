# Accessing AVSession

In addition to the implementation of audio and video playback, media applications may need to access AVSession provided by AVSession Kit for display and control purposes. This topic describes typical display and control scenarios of accessing AVSession.

In different access scenarios, different UIs are displayed in the controller of the system, and different specifications are posed for application access processing.

#### Scenarios That Require AVSession Access

AVSession restricts background audio playback and VoIP calls. As such, applications that provide long-duration audio or video playback, audiobook applications, and VoIP applications need to access AVSession. If such an application does not access AVSession, the system stops its audio playback or mutes the ongoing call when detecting that the application is running in the background. In this way, the application behavior is restricted. You can verify the restriction locally before the application is released.

For applications that may use audio playback, such as gaming and live broadcast applications, accessing AVSession is optional. However, if they want to continue audio playback after switching to the background, they must access AVSession.

To implement background playback, the application must also use [Background Tasks Kit](../../../../application-framework/background-tasks-kit/about-this-kit/document.md) to request a continuous task to avoid being suspended.

#### Access Process

The process for implementing AVSession access is as follows:

1.  Determine the type of AVSession to be created for the application, and then [create one](#creating-avsession). The AVSession type determines the style of the control template displayed in the controller.
2.  [Create a background task](#creating-a-background-task).
3.  [Set necessary metadata](#setting-metadata), which is the response information displayed in the controller. The metadata includes the IDs of the current media asset (assetId), previous media asset (previousAssetId), and next media asset (nextAssetId), title, author, album, writer, and duration.
4.  [Set playback state information](#setting-playback-state-information). The information includes the playback state, position, speed, buffered time, loop mode, media item being played (activeItemId), custom media data (extras), and whether the media asset is favorited (isFavorite).
5.  [Register control commands](#registering-control-commands). The control commands include **play**, **pause**, **previous**, **next**, **fastForward**, **rewind**, **toggleFavorite**, **setLoopMode**, and **seek**.
6.  Destroy AVSession when the application exits or stops providing service.

#### Creating AVSession

[AVSessionType](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-avsession-t#avsessiontype10) in the constructor determines the type of AVSession to create. Different AVSession types represent the control capabilities in various scenarios and display different control templates in the controller.

-   For audio AVSession, the controller provides the following control buttons: favorite, previous, play/pause, next, and loop mode.
    
-   For video AVSession, the controller provides the following control buttons: rewind, previous, play/pause, next, and fast-forward.
    
-   For voice\_call AVSession, the application is not displayed in the controller.
    

Refer to the code snippet below:

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b3/v3/FG2CZYO_T52d4M7xYFIM-A/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062037Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=0D79BBE243F27B18294084AB6B97CFA2916C2915DB47039A39EC33481DD5FC87)

The sample code below demonstrates only the API call for creating an AVSession object. When actually using it, the application must ensure that the AVSession object remains throughout the application's background playback activities. This prevents the system from reclaiming or releasing it, which could lead to playback being controlled by the system.

import { avSession as AVSessionManager } from '@kit.AVSessionKit';
// ...

@Entry
@Component
struct Index {
  @State message: string = 'hello world';
  // ...

  build() {
    Column() {
      // ...
      Text(this.message)
        .onClick(async () => {
          // Start to create and activate an AVSession object.
          // Create an AVSession object.
          let context = this.getUIContext().getHostContext() as Context;
          let type: AVSessionManager.AVSessionType = 'audio';
          let session = await AVSessionManager.createAVSession(context, 'SESSION\_NAME', type);
          // Call activate() after the metadata and control commands are registered.
          await session.activate();
          console.info(\`session create done : sessionId : ${session.sessionId}\`);
          // ...
        })
    }
    .width('100%')
    .height('100%')
  }
}

#### Creating a Background Task

To implement background playback, the application must also use [Background Tasks Kit](../../../../application-framework/background-tasks-kit/about-this-kit/document.md) to request a continuous task to avoid being suspended.

Media playback applications must request a continuous task of the [AUDIO\_PLAYBACK](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-resourceschedule-backgroundtaskmanager#backgroundmode) background mode.

#### Setting Metadata

## Setting Common Metadata

The application can call **setAVMetadata()** to set AVSession metadata to the system so that the metadata can be displayed in the controller. The metadata includes but not limited to the IDs of the current media asset (**assetId**), previous media asset (**previousAssetId**), and next media asset (**nextAssetId**), title, author, album, writer, and duration.

import { avSession as AVSessionManager } from '@kit.AVSessionKit';
import { BusinessError } from '@kit.BasicServicesKit';
// ...

@Entry
@Component
struct Index {
  @State message: string = 'hello world';
  // ...

  build() {
    Column() {
      // ...
      Text(this.message)
        .onClick(async () => {
          try {
            let context = this.getUIContext().getHostContext() as Context;
            // It is assumed that an AVSession object has been created. For details about how to create an AVSession object, see the node snippet above.
            let session = await AVSessionManager.createAVSession(context, 'SESSION\_NAME', 'audio');
            // Set necessary AVSession metadata.
            let metadata: AVSessionManager.AVMetadata = {
              assetId: '0', // Specified by the application, used to identify the media asset in the application media library.
              title: 'TITLE',
              mediaImage: 'IMAGE',
              artist: 'ARTIST',
            };
            session.setAVMetadata(metadata).then(() => {
              console.info(\`SetAVMetadata successfully\`);
              // ...
            }).catch((err: BusinessError) => {
              console.error(\`Failed to set AVMetadata. Code: ${err.code}, message: ${err.message}\`);
              // ...
            });
          } catch (err) {
            if (err) {
              console.error(\`AVSession create Error: Code: ${err.code}, message: ${err.message}\`);
              // ...
            }
          }
        })
    }
    .width('100%')
    .height('100%')
  }
}

## Setting Lyrics

The controller provides the UI to show lyrics. The application only needs to set the lyrics content. The controller parses the lyrics content and displays it based on the playback progress.

import { avSession as AVSessionManager } from '@kit.AVSessionKit';
import { BusinessError } from '@kit.BasicServicesKit';
// ...

@Entry
@Component
struct Index {
  @State message: string = 'hello world';
  // ...

  build() {
    Column() {
      // ...
      Text(this.message)
        .onClick(async () => {
          let context = this.getUIContext().getHostContext() as Context;
          // It is assumed that an AVSession object has been created. For details about how to create an AVSession object, see the node snippet above.
          let type: AVSessionManager.AVSessionType = 'audio';
          let session = await AVSessionManager.createAVSession(context, 'SESSION\_NAME', type);

          // Set the lyric to AVSession.
          let metadata: AVSessionManager.AVMetadata = {
            assetId: '0',
            title: 'TITLE',
            mediaImage: 'IMAGE',
            // The LRC contains two types of elements: time tag + lyrics, and ID tag.
            // Example: \[00:25.44\]xxx\\r\\n\[00:26.44\]xxx\\r\\n
            lyric: "Lyrics in LRC format",
            // The singleLyricText field stores a single line of lyric text without timestamps.
            // Example: "Content of a single lyric line"
            singleLyricText: "Content of a single lyric line",
          };
          session.setAVMetadata(metadata).then(() => {
            console.info(\`SetAVMetadata successfully\`);
            // ...
          }).catch((err: BusinessError) => {
            console.error(\`Failed to set AVMetadata. Code: ${err.code}, message: ${err.message}\`);
            // ...
          });
          // ...
        })
    }
    .width('100%')
    .height('100%')
  }
}

## Historical Playlists

For music and audiobook applications, the media controller provides a series of quick playback capabilities, including instant cold start playback and access to the historical playlist. The supported audio content for the playlist includes music tracks, audiobook collections, and podcast series. Video and live streaming media do not support the playlist feature. To integrate the mentioned features, the application should register and adapt the [playback intent](../../../../ai/intents-kit/habit-based-recommendation-solution/integration-solution/document.md) on the device for the background launch mode.

You can refer to the code snippet below to register the playback intent, set playlist information, and start intent-based playback.

**Registering the Playback Intent**

The application registers either the PlayMusicList intent (for music applications) or PlayAudio intent (for audiobook applications) based on service requirements. To implement the registration, edit the corresponding intent configuration in the PROJECT\_HOME/entry/src/main/resources/base/profile/insight\_intent.json file.

The following is an example of intent registration:

{
  // List of intents supported by the application.
  "insightIntents": \[
    {
      // Intent name.
      // The name must comply with the Intents Kit specifications. Currently, only predefined intents for specific vertical domains are supported.
      // The intent name must be unique in the application.
      "intentName": "PlayMusicList", // PlayMusicList intent for music applications; PlayAudio intent for audiobook applications.
      // Vertical domain to which the intent belongs.
      "domain": "MusicDomain", // MusicDomain for music applications; AudioDomain for audiobook applications.
      // Intent version number.
      // The version number is verified when a plugin references the intent. The intent can be called only when the version number is the same as that defined by the plugin.
      "intentVersion": "1.0.1",
      // Entry to the intent call logic.
      "srcEntry": "./ets/entryability/InsightIntentExecutorImpl.ets",
      "uiAbility": {
        // Module and ability to which the intent belongs, as well as the relative path entry of the code.
        "ability": "EntryAbility",
        // UIAbility supports two execution modes: foreground and background.
        "executeMode": \[
          "background", // The features of instant cold start playback and access to the historical playlist require the application to support the background launch mode.
          "foreground"
        \]
      }
    }
  \]
}

**Setting Playlist Information**

Call the [setAVMetadata](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-avsession-avsession#setavmetadata10) API to set the playlist information for the content that is being played. The playlist information consists of the following fields:

-   avQueueName: playlist name, which is mandatory for playlist access.
-   avQueueId: playlist ID, which is mandatory for playlist access.
-   avQueueImage: playlist image resource, which is mandatory for playlist access.

The system updates the media information in real time based on the information reported by the application. Therefore, once accessing a playlist, the application must keep reporting the playlist data in [AVMetadata](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-avsession-i#avmetadata10).

import { avSession as AVSessionManager } from '@kit.AVSessionKit';
import { BusinessError } from '@kit.BasicServicesKit';

let context: Context = getContext(this);
async function setListener() {
  // Assume that an AVSession has been created. For details about how to create an AVSession, see the previous cases.
  let type: AVSessionManager.AVSessionType = 'audio';
  let session = await AVSessionManager.createAVSession(context, 'SESSION\_NAME', type);
  // Set the playlist information on AVSession.
  let metadata: AVSessionManager.AVMetadata = {
  // The following content is set by the application.
  assetId: 'musicid123',
  avQueueName: 'myQueue',
  avQueueId: 'myQueue123',
  avQueueImage: "PIXELMAP\_OBJECT",
  };
  session.setAVMetadata(metadata).then(() => {
  console.info(\`SetAVMetadata successfully\`);
  }).catch((err: BusinessError) => {
    console.error(\`Failed to set AVMetadata. Code: ${err.code}, message: ${err.message}\`);
  });
  // Report the playback state. For details, see the playback state.
}

**Implementing Intent-based Playback**

After the application integrates the playlist feature, users can play its playlists on the media controller. If the application process is terminated, users can initiate background playback via the media controller.

-   When users trigger playlist playback, the system sends the unique ID of the playlist to the application. The application parses entityId in intentParam to obtain the playlist ID and plays the corresponding playlist.
-   When users trigger cold-start playback, the system includes an empty playlist ID in intentParam, meaning the parsed entityId is an empty string. In this case, the application itself determines the playback content, thereby resuming the last playback content.
-   **To implement background cold-start playback, the application must configure [AVMetadata](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-avsession-i#avmetadata10) prior to playback, register [playback control callbacks](#registering-control-commands), and request a continuous playback task.**

import { insightIntent, InsightIntentExecutor } from '@kit.AbilityKit';
import { window } from '@kit.ArkUI';
import { BusinessError } from '@kit.BasicServicesKit';

  /\*\*
   \* Intent call example
   \*/
  export default class InsightIntentExecutorImpl extends InsightIntentExecutor {
    /\*\*
     \* Override the background UIAbility launch intent.
     \*
     \* @param intentName Intent name.
     \* @param intentParam Intent parameter.
     \* @returns Returns the intent call result.
     \*/
    async onExecuteInUIAbilityBackgroundMode(intentName: string, intentParam: Record<string, Object>):
      Promise<insightIntent.ExecuteResult> {
      // Distribute the processing logic based on the intent name.
      switch (intentName) {
        case 'PlayMusicList':
          // Parse PlayMusicList as follows:
          let entityId: string = (intentParam.items as Array<object>)?.\[0\]?.\['entityId'\];
          return this.playFunc(entityId);
        case 'PlayAudio':
          // Parse PlayAudio as follows:
          let data = intentParam as Record<string, string>;
          return this.playFunc(data.entityId);
        default:
          break;
      }
      return Promise.resolve({
        code: -1,
        result: {
          message: 'unknown intent'
        }
      } as insightIntent.ExecuteResult)
    }

    /\*\*
     \* Implement the playback.
     \*
     \* @param entityId ID of the content to play.
     \*/
    private playFunc(entityId: string): Promise<insightIntent.ExecuteResult> {
      // If entityId is not empty, the content (playlist or album) specified by the user will be played.
      // If entityId is empty (entityId.length == 0), the application determines the content to be played, which can be a historical or recommended playlist.
      // The application is launched in the background for playback. It needs to initialize the playback resources, set AVMetadata, register playback control callbacks, and request a continuous playback task.
      // TODO: Implement the specific playback service.
      return Promise.resolve({
        code: 0,
        result: {
          message: 'Intent execute succeed'
        }
      } as insightIntent.ExecuteResult)
    }
}

## Display Tags of Media Assets

The controller displays a special type identifier for long-duration media assets. Currently, only the Audio Vivid identifier is displayed.

The application notifies the system of the display tag of the media asset through the AVMetadata during the access, and the controller displays the tag when the media asset is being played.

import { avSession as AVSessionManager } from '@kit.AVSessionKit';
import { BusinessError } from '@kit.BasicServicesKit';
// ...

@Entry
@Component
struct Index {
  @State message: string = 'hello world';
  // ...

  build() {
    Column() {
      // ...
      Text(this.message)
        .onClick(async () => {
          let context = this.getUIContext().getHostContext() as Context;
          // It is assumed that an AVSession object has been created. For details about how to create an AVSession object, see the node snippet above.
          let type: AVSessionManager.AVSessionType = 'audio';
          let session = await AVSessionManager.createAVSession(context, 'SESSION\_NAME', type);

          // Set the media audio source information to AVSession.
          let metadata: AVSessionManager.AVMetadata = {
            assetId: '0',
            title: 'TITLE',
            mediaImage: 'IMAGE',
            // The display tag of the audio source is Audio Vivid.
            displayTags: AVSessionManager.DisplayTag.TAG\_AUDIO\_VIVID,
          };
          session.setAVMetadata(metadata).then(() => {
            console.info(\`SetAVMetadata successfully\`);
            // ...
          }).catch((err: BusinessError) => {
            console.error(\`Failed to set AVMetadata. Code: ${err.code}, message: ${err.message}\`);
            // ...
          });
          // ...
        })
    }
    .width('100%')
    .height('100%')
  }
}

#### Setting Playback State Information

## Setting General State Information

The application can call [setAVPlaybackState](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-avsession-avsession#setavplaybackstate10) to set the playback state information to the system so that the information can be displayed in the controller.

Generally, the playback state information includes the playback state, position, speed, buffered time, loop mode, media item being played (activeItemId), custom media data (extras), and whether the media asset is favorited (isFavorite). It changes during the playback.

import { avSession as AVSessionManager } from '@kit.AVSessionKit';
import { BusinessError } from '@kit.BasicServicesKit';
// ...

@Entry
@Component
struct Index {
  @State message: string = 'hello world';
  // ...

  build() {
    Column() {
      // ...
      Text(this.message)
        .onClick(async () => {
          let context = this.getUIContext().getHostContext() as Context;
          // It is assumed that an AVSession object has been created. For details about how to create an AVSession object, see the node snippet above.
          let session = await AVSessionManager.createAVSession(context, 'SESSION\_NAME', 'audio');

          // The player logic that triggers changes in the session metadata and playback state is omitted here.
          // Set the playback state to paused and set isFavorite to false.
          let playbackState: AVSessionManager.AVPlaybackState = {
            state: AVSessionManager.PlaybackState.PLAYBACK\_STATE\_PAUSE,
            isFavorite: false
          };
          session.setAVPlaybackState(playbackState, (err: BusinessError) => {
            if (err) {
              console.error(\`Failed to set AVPlaybackState. Code: ${err.code}, message: ${err.message}\`);
              // ...
            } else {
              console.info(\`SetAVPlaybackState successfully\`);
              // ...
            }
          });
          // ...
        })
    }
    .width('100%')
    .height('100%')
  }
}

## Setting the Progress Bar

To display a progress bar in the controller, the application must set the duration, playback state (pause or play), playback position, and playback speed. The controller displays the progress bar based on the information.

import { avSession as AVSessionManager } from '@kit.AVSessionKit';
import { BusinessError } from '@kit.BasicServicesKit';
// ...

@Entry
@Component
struct Index {
  @State message: string = 'hello world';
  // ...

  build() {
    Column() {
      // ...
      Text(this.message)
        .onClick(async () => {
          let context = this.getUIContext().getHostContext() as Context;
          // It is assumed that an AVSession object has been created. For details about how to create an AVSession object, see the node snippet above.
          let type: AVSessionManager.AVSessionType = 'audio';
          let session = await AVSessionManager.createAVSession(context, 'SESSION\_NAME', type);

          // Set the media resource duration.
          let metadata: AVSessionManager.AVMetadata = {
            assetId: '0',
            title: 'TITLE',
            mediaImage: 'IMAGE',
            duration: 23000, // Duration of the media asset, in milliseconds.
          };
          session.setAVMetadata(metadata).then(() => {
            console.info(\`SetAVMetadata successfully\`);
            // ...
          }).catch((err: BusinessError) => {
            console.error(\`Failed to set AVMetadata. Code: ${err.code}, message: ${err.message}\`);
            // ...
          });

          // Set the playback state information, including the playback state, position, speed, and buffered time.
          let playbackState: AVSessionManager.AVPlaybackState = {
            state: AVSessionManager.PlaybackState.PLAYBACK\_STATE\_PLAY, // Playing state.
            position: {
              elapsedTime: 1000, // Playback position, in milliseconds.
              updateTime: new Date().getTime(), // Timestamp when the application updates the current position, in milliseconds.
            },
            speed: 1.0, // Optional. The default value is 1.0. The playback speed is set based on the speed supported by the application. The system does not verify the speed.
            bufferedTime: 14000, // Optional. Buffered time, in milliseconds.
          };
          session.setAVPlaybackState(playbackState, (err) => {
            if (err) {
              console.error(\`Failed to set AVPlaybackState. Code: ${err.code}, message: ${err.message}\`);
              // ...
            } else {
              console.info(\`SetAVPlaybackState successfully\`);
              // ...
            }
          });
          // ...
        })
    }
    .width('100%')
    .height('100%')
  }
}

The system's playback control center calculates the playback progress automatically based on the information set by the application, and the application does not need to update the playback progress in real time. However, to avoid calculation errors, the application must update AVPlaybackState when the following states change:

-   state
-   position
-   speed

The application reports the start position of the progress once the actual playback starts. If the playback is in the buffer state, the application can report **AVSessionManager.PlaybackState.PLAYBACK\_STATE\_BUFFERING** to instruct the system not to update the progress.

Certain special processing is required when setting the progress bar.

1.  Songs that can be previewed
    
    (1) The application sets the preview duration, rather than the total duration, for a song. In this case, when the user performs progress control in the controller, the application receives the relative timestamp within the preview duration, rather than that within the total duration. The application needs to calculate the absolute timestamp from the very beginning of the song.
    
    (2) The application sets the total duration for a song but requires the system to provide preview, the application can report the start position of the progress when the playback starts, and report the end position when the received seek instruction is not within the preview duration. In the latter case, the playback control progress of the system rebounds.
    
2.  Songs that do not support preview
    
    If a song cannot be previewed, it cannot be displayed by the application. In this case, the application should set the duration to **\-1**, so the system does not display the actual duration.
    
3.  Special contents such as ads
    
    For media assets with pre-roll or post-roll ads, you are advised to:
    
    -   Set the ad duration separately.
    -   Set a new duration for the actual content, to distinguish it from the ad.

#### Registering Control Commands

The application can register different control commands through **on()** to implement control operations in the controller.

For details, see the [API reference](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-avsession-avsession#onplay10).

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/75/v3/bH7S1z7aQmKVm7qPpztwtw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062037Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=08AE25EC32BDFAE5CA01F337C080F56AD3132C2B7E80AB0F32AA4D388CFD4775)

After an AVSession object is created, register control commands supported by the application before activating the object.

The table below lists the control commands supported by media assets.

| Control Command | Description |
| :-- | :-- |
| play | Plays the media. |
| pause | Pauses the playback. |
| stop | Stops the playback. |
| playNext | Plays the next media asset. |
| playPrevious | Plays the previous media asset. |
| fastForward | Fast-forwards. |
| rewind | Rewinds. |
| playFromAssetId | Plays a media asset with a given asset ID. |
| seek | Seeks to a playback position. |
| setSpeed | Sets the playback speed. |
| setLoopMode | Sets the loop mode. |
| toggleFavorite | Favorites or unfavorites a media asset. |
| skipToQueueItem | Selects an item in the playlist. |
| handleKeyEvent | Sets a key event. |
| commonCommand | Customizes a control command. |

The table below lists the control commands for calling applications.

| Control Command | Description |
| :-- | :-- |
| answer | Answers a call. |
| hangUp | Ends a call. |
| toggleCallMute | Mutes or unmutes a call. |

## Handling Unsupported Commands

If the application does not support a control command supported by the system, for example, the **playPrevious** command, it can use **off()** to deregister the control command. Then the controller grays out the control page accordingly, so that users know that the control command is not supported.

import { avSession as AVSessionManager } from '@kit.AVSessionKit';

@Entry
@Component
struct Index {
  @State message: string = 'hello world';

  build() {
    Column() {
      Text(this.message)
        .onClick(async () => {
          let context = this.getUIContext().getHostContext() as Context;
          // It is assumed that an AVSession object has been created. For details about how to create an AVSession object, see the node snippet above.
          let type: AVSessionManager.AVSessionType = 'audio';
          let session = await AVSessionManager.createAVSession(context, 'SESSION\_NAME', type);

          // Cancel the listener of the AVSession object.
          session.off('play');
          session.off('pause');
          session.off('stop');
          session.off('playNext');
          session.off('playPrevious');
          // ...
        })
    }
    .width('100%')
    .height('100%')
  }
}

## Setting Fast-Forward/Rewind

The application can call APIs to set the fast-forward/rewind intervals in three different ways. It also registers the fast-forward/rewind control command to respond to user operations.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5a/v3/MqHsMFhGSx-4dGToBWeBZQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062037Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=AC21B42BD8384F3B45B92DBF8369751C7C4CE99A89DEA8762788A1671BA47D2D)

When applications register commands for fast-forward/rewind and next/previous track switching, there are differences in the display on the controller.

-   When **AVSessionType** is **audio**:
    
    | Registered Event Combination | Controller Buttons | Button Availability |
    | :-- | :-- | :-- |
    | No events registered | **Previous**, **Next** | All buttons are unavailable. |
    | Previous/Next events registered | **Previous**, **Next** | 
    If previous events registered, the **Previous** button is available.
    
    If next events registered, the **Next** button is available.
    
    Buttons corresponding to unregistered events are unavailable.
    
     |
    | Fast-forward/rewind events registered | **Previous**, **Next** | All buttons are unavailable. |
    | Previous/Next and fast-forward/rewind events registered | **Previous**, **Next** | 
    
    If previous events registered, the **Previous** button is available.
    
    If next events registered, the **Next** button is available.
    
    Buttons corresponding to unregistered events are unavailable.
    
     |
    
-   When **AVSessionType** is **video**:
    
    | Registered Event Combination | Controller Buttons | Button Availability |
    | :-- | :-- | :-- |
    | No events registered | **Fast-Forward**, **Rewind** | All buttons are unavailable. |
    | Previous/Next events registered | **Previous**, **Next** | 
    If previous events registered, the **Previous** button is available.
    
    If next events registered, the **Next** button is available.
    
    Buttons corresponding to unregistered events are unavailable.
    
     |
    | Fast-forward/rewind events registered | **Fast-Forward**, **Rewind** | 
    
    If fast-forward events are registered, the **Fast-Forward** button is available.
    
    If rewind events are registered, the **Rewind** button is available.
    
    Buttons corresponding to unregistered events are unavailable.
    
     |
    | Previous/Next and fast-forward/rewind events registered | **Fast-Forward**, **Rewind** | 
    
    If fast-forward events are registered, the **Fast-Forward** button is available.
    
    If rewind events are registered, the **Rewind** button is available.
    
    Buttons corresponding to unregistered events are unavailable.
    
     |
    
    import { avSession as AVSessionManager } from '@kit.AVSessionKit';
    import { BusinessError } from '@kit.BasicServicesKit';
    // ...
    
    @Entry
    @Component
    struct Index {
      @State message: string = 'hello world';
      // ...
    
      build() {
        Column() {
          // ...
          Text(this.message)
            .onClick(async () => {
              let context = this.getUIContext().getHostContext() as Context;
              // It is assumed that an AVSession object has been created. For details about how to create an AVSession object, see the node snippet above.
              let type: AVSessionManager.AVSessionType = 'audio';
              let session = await AVSessionManager.createAVSession(context, 'SESSION\_NAME', type);
              // ...
    
              // Set the supported fast-forward or rewind duration for AVSession.
              let metadata: AVSessionManager.AVMetadata = {
                assetId: '0', // Specified by the application, used to identify the media asset in the application media library.
                title: 'TITLE',
                mediaImage: 'IMAGE',
                skipIntervals: AVSessionManager.SkipIntervals.SECONDS\_10,
              };
              session.setAVMetadata(metadata).then(() => {
                console.info(\`SetAVMetadata successfully\`);
                // ...
              }).catch((err: BusinessError) => {
                console.error(\`Failed to set AVMetadata. Code: ${err.code}, message: ${err.message}\`);
                // ...
              });
    
              session.on('fastForward', (time ?: number) => {
                console.info(\`on fastForward , do fastForward task\`);
                // ...
                // do some tasks ···
              });
              session.on('rewind', (time ?: number) => {
                console.info(\`on rewind , do rewind task\`);
                // ...
                // do some tasks ···
              });
              // ...
            })
        }
        .width('100%')
        .height('100%')
      }
    }
    

## Favoriting Media Assets

For a music application to implement the favorite function, it needs to register the control response for favorite toggling via [on('toggleFavorite')](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-avsession-avsession#ontogglefavorite10).

import { avSession as AVSessionManager } from '@kit.AVSessionKit';
import { BusinessError } from '@kit.BasicServicesKit';
// ...

@Entry
@Component
struct Index {
  @State message: string = 'hello world';
  // ...

  build() {
    Column() {
      // ...
      Text(this.message)
        .onClick(async () => {
          let context = this.getUIContext().getHostContext() as Context;
          // It is assumed that an AVSession object has been created. For details about how to create an AVSession object, see the node snippet above.
          let type: AVSessionManager.AVSessionType = 'audio';
          let session = await AVSessionManager.createAVSession(context, 'SESSION\_NAME', type);
          // ...
          session.on('toggleFavorite', (assetId) => {
            console.info(\`on toggleFavorite \`);
            // ...
            // The application receives the toggleFavorite command and favorites or unfavorites the media asset.

            // Set the new state to AVSession after the application finishes favoriting or unfavoriting.
            let playbackState: AVSessionManager.AVPlaybackState = {
              isFavorite: true,
            };
            session.setAVPlaybackState(playbackState).then(() => {
              console.info(\`SetAVPlaybackState successfully\`);
              // ...
            }).catch((err: BusinessError) => {
              console.error(\`SetAVPlaybackState BusinessError: code: ${err.code}, message: ${err.message}\`);
              // ...
            });
          });
          // ...
        })
    }
    .width('100%')
    .height('100%')
  }
}

## Setting the Loop Mode

For music applications, the controller displays control operations in loop mode by default. Currently, the system supports four fixed [loop modes](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-avsession-e#loopmode10),

namely, shuffle, sequential playback, single loop, and playlist loop. After switching the loop mode as instructed, the application needs to report the new loop mode.

Even if the application does not support the four fixed loop modes, it must report one of them to the system.

Refer to the code snippet below:

import { avSession as AVSessionManager } from '@kit.AVSessionKit';
import { BusinessError } from '@kit.BasicServicesKit';
// ...

@Entry
@Component
struct Index {
  @State message: string = 'hello world';
  // ...

  build() {
    Column() {
      // ...
      Text(this.message)
        .onClick(async () => {
          let context = this.getUIContext().getHostContext() as Context;
          // It is assumed that an AVSession object has been created. For details about how to create an AVSession object, see the node snippet above.
          let type: AVSessionManager.AVSessionType = 'audio';
          let session = await AVSessionManager.createAVSession(context, 'SESSION\_NAME', type);
          // ...

          // When the application starts or switches the loop mode, it sets the loop mode in use to the AVSession.
          let playBackState: AVSessionManager.AVPlaybackState = {
            loopMode: AVSessionManager.LoopMode.LOOP\_MODE\_SINGLE,
          };
          session.setAVPlaybackState(playBackState).then(() => {
            console.info(\`set AVPlaybackState successfully\`);
            // ...
          }).catch((err: BusinessError) => {
            console.error(\`Failed to set AVPlaybackState. Code: ${err.code}, message: ${err.message}\`);
            // ...
          });

          // The application listens for loop mode changes.
          session.on('setLoopMode', (mode) => {
            console.info(\`on setLoopMode ${mode}\`);
            // ...
            // After receiving the instruction for setting the loop mode, the application determines the next mode. After the switching is complete, the application reports the new loop mode through AVPlaybackState.
            let playBackState: AVSessionManager.AVPlaybackState = {
              loopMode: AVSessionManager.LoopMode.LOOP\_MODE\_SINGLE,
            };
            session.setAVPlaybackState(playBackState).then(() => {
              console.info(\`set AVPlaybackState successfully\`);
              // ...
            }).catch((err: BusinessError) => {
              console.error(\`Failed to set AVPlaybackState. Code: ${err.code}, message: ${err.message}\`);
              // ...
            });
          });
          // ...
        })
    }
    .width('100%')
    .height('100%')
  }
}

## Performing Progress Control

An application that supports progress display can further support progress control. To support progress control, the application must respond to the **seek** control command. When users drag the progress bar in the controller, the application receives a callback. Refer to the code snippet below:

import { avSession as AVSessionManager } from '@kit.AVSessionKit';
// ...

@Entry
@Component
struct Index {
  @State message: string = 'hello world';
  // ...

  build() {
    Column() {
      // ...
      Text(this.message)
        .onClick(async () => {
          let context = this.getUIContext().getHostContext() as Context;
          // It is assumed that an AVSession object has been created. For details about how to create an AVSession object, see the node snippet above.
          let type: AVSessionManager.AVSessionType = 'audio';
          let session = await AVSessionManager.createAVSession(context, 'SESSION\_NAME', type);
          // ...

          session.on('seek', (position: number) => {
            console.info(\`on seek , the time is ${JSON.stringify(position)}\`);
            // ...

            // The seek operation may trigger a long buffering time. You can set the playback state to PLAYBACK\_STATE\_BUFFERING.
            let playbackState: AVSessionManager.AVPlaybackState = {
              state: AVSessionManager.PlaybackState.PLAYBACK\_STATE\_BUFFERING, // Buffering state.
            };
            session.setAVPlaybackState(playbackState, (err) => {
              if (err) {
                console.error(\`Failed to set AVPlaybackState. Code: ${err.code}, message: ${err.message}\`);
                // ...
              } else {
                console.info(\`SetAVPlaybackState successfully\`);
                // ...
              }
            });

            // The application responds to the seek command and seeks to the specified position.

            // After seeking to the specified position, the application synchronizes the new position to the system.
            playbackState.state = AVSessionManager.PlaybackState.PLAYBACK\_STATE\_PLAY; // Playing state.
            playbackState.position = {
              elapsedTime: position, // Playback position, in milliseconds.
              updateTime: new Date().getTime(), // Timestamp when the application updates the current position, in milliseconds.
            }
            session.setAVPlaybackState(playbackState, (err) => {
              if (err) {
                console.error(\`Failed to set AVPlaybackState. Code: ${err.code}, message: ${err.message}\`);
                // ...
              } else {
                console.info(\`SetAVPlaybackState successfully\`);
                // ...
              }
            });
          });

          // ...
        })
    }
    .width('100%')
    .height('100%')
  }
}

#### Adapting to Media Notification

Currently, the system does not provide APIs for proactively sending control notifications to applications. When an application that has integrated the media controller enters the playing state, the system automatically sends a notification and displays the notification in the notification center and on the lock screen.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f9/v3/wSVWjfXSTpmVW_UXSfmbjw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062037Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=78AD321619113E9834D3CD4AB40C80F56389A22B4FC12E357F9A841C5FDC2B2B)

The system sends playback control widgets in the notification center and on the lock screen and controls their lifecycle.

#### Adapting to Bluetooth and Wired Key Events

Currently, the system does not provide APIs for listening for multimodal key events for applications. If an application needs to listen for media key events from Bluetooth and wired headsets, the application can register control commands with AVSession. AVSession provides the following two methods for implementation:

-   Method 1 (recommended)
    
    Integrate the media controller based on service requirements, [register the required control commands](#registering-control-commands), and implement the corresponding functionalities. AVSession listens for multimodal key events, converts them into AVSession control commands, and sends them to the application. The application does not need to differentiate between various key events. Instead, it processes the key events based on the callback of AVSession. Implementing play and pause functions through this method also adapts to the wear detection of Bluetooth headsets, with play and pause commands received upon wearing or removing both earpieces. Currently, the following AVSession control commands can be converted:
    
    | Control Command | Description |
    | :-- | :-- |
    | play | Plays the media. |
    | pause | Pauses the playback. |
    | stop | Stops the playback. |
    | playNext | Plays the next media asset. |
    | playPrevious | Plays the previous media asset. |
    | fastForward | Fast-forwards. |
    | rewind | Rewinds. |
    
    import { avSession as AVSessionManager } from '@kit.AVSessionKit';
    import { BusinessError } from '@kit.BasicServicesKit';
    // ...
    
    @Entry
    @Component
    struct Index {
      @State message: string = 'hello world';
      // ...
    
      build() {
        Column() {
          // ...
          Text(this.message)
            .onClick(async () => {
              try {
                let context = this.getUIContext().getHostContext() as Context;
                let type: AVSessionManager.AVSessionType = 'audio';
                let session = await AVSessionManager.createAVSession(context, 'SESSION\_NAME', type);
                // ...
                // Set the necessary media information. This step is mandatory. Otherwise, the application cannot receive control events.
                let metadata: AVSessionManager.AVMetadata = {
                  assetId: '0', // Specified by the application, used to identify the media asset in the application media library.
                  title: 'TITLE',
                  mediaImage: 'IMAGE',
                  artist: 'ARTIST'
                };
                session.setAVMetadata(metadata).then(() => {
                  console.info(\`SetAVMetadata successfully\`);
                  // ...
                }).catch((err: BusinessError) => {
                  console.error(\`Failed to set AVMetadata. Code: ${err.code}, message: ${err.message}\`);
                  // ...
                });
                // Generally, logic processing on the player is implemented in the listener.
                // After the processing is complete, use the setter to synchronize the playback information. For details, see the code snippet above.
                session.on('play', () => {
                  console.info(\`on play , do play task\`);
                  // ...
                  // If this command is not supported, do not register it. If the command has been registered but is not used temporarily, use session.off('play') to cancel listening.
                  // After the processing is complete, call setAVPlayState to report the playback state.
                });
                session.on('pause', () => {
                  console.info(\`on pause , do pause task\`);
                  // ...
                  // If this command is not supported, do not register it. If the command has been registered but is not used temporarily, use session.off('pause') to cancel listening.
                  // After the processing is complete, call setAVPlayState to report the playback state.
                });
                // ...
              } catch (err) {
                if (err) {
                  console.error(\`AVSession create Error: Code: ${err.code}, message: ${err.message}\`);
                  // ...
                }
              }
            })
        }
        .width('100%')
        .height('100%')
      }
    }
    
-   Method 2
    
    Register the [HandleMediaKeyEvent](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-avsession-avsession#onhandlekeyevent10) callback through AVSession. The callback directly forwards the [KeyEvent](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-keyevent). The application is required to identify the type of the key event and implement the corresponding functionalities. Currently, the following key events can be forwarded:
    
    | Key Type ([KeyCode](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-keycode#keycode)) | Description |
    | :-- | :-- |
    | KEYCODE\_MEDIA\_PLAY\_PAUSE | Play/Pause key. |
    | KEYCODE\_MEDIA\_STOP | Stop key. |
    | KEYCODE\_MEDIA\_NEXT | Next key. |
    | KEYCODE\_MEDIA\_PREVIOUS | Previous key. |
    | KEYCODE\_MEDIA\_REWIND | Rewind key. |
    | KEYCODE\_MEDIA\_FAST\_FORWARD | Fast-forward key. |
    | KEYCODE\_MEDIA\_PLAY | Play key. |
    | KEYCODE\_MEDIA\_PAUSE | Pause key. |
    
    import { avSession as AVSessionManager } from '@kit.AVSessionKit';
    import { BusinessError } from '@kit.BasicServicesKit';
    // ...
    
    @Entry
    @Component
    struct Index {
      @State message: string = 'hello world';
      // ...
    
      build() {
        Column() {
          // ...
          Text(this.message)
            .onClick(async () => {
              let context = this.getUIContext().getHostContext() as Context;
              let type: AVSessionManager.AVSessionType = 'audio';
              let session = await AVSessionManager.createAVSession(context, 'SESSION\_NAME', type);
              // ...
              // Set the necessary media information. This step is mandatory. Otherwise, the application cannot receive key events.
              let metadata: AVSessionManager.AVMetadata = {
                assetId: '0', // Specified by the application, used to identify the media asset in the application media library.
                title: 'TITLE',
                mediaImage: 'IMAGE',
                artist: 'ARTIST'
              };
              session.setAVMetadata(metadata).then(() => {
                console.info(\`SetAVMetadata successfully\`);
                // ...
              }).catch((err: BusinessError) => {
                console.error(\`Failed to set AVMetadata. Code: ${err.code}, message: ${err.message}\`);
                // ...
              });
              session.on('handleKeyEvent', (event) => {
                // Parse the key code. The application must perform logic processing on the player based on the key code.
                console.info(\`on handleKeyEvent, keyCode=${event.key.code}\`);
                // ...
              });
              // ...
            })
        }
        .width('100%')
        .height('100%')
      }
    }
    

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c5/v3/aJfhBluiTYK3LSHTPKAujw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062037Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=F2639F5717CC1FBA2F051B0D21F7BEFDB37FC119291C7BA66126C1E7019D492B)

1.  Both methods require the accurate configuration of media information AVMetadata and the registration of corresponding control interfaces to receive control commands and key events.
2.  Choose either method for integration. Method 1 is recommended.
