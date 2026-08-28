# AVSession Provider

An audio and video application needs to access the AVSession service as a provider in order to display media information in the controller (for example, Media Controller) and respond to playback control commands delivered by the controller.

#### Basic Concepts

-   AVMetadata: media data related attributes, including the IDs of the current media asset (assetId), previous media asset (previousAssetId), and next media asset (nextAssetId), title, author, album, writer, and duration.
    
-   AVPlaybackState: playback state attributes, including the playback state, position, speed, buffered time, loop mode, media item being played (activeItemId), custom media data (extras), and whether the media asset is favorited (isFavorite).
    

#### Available APIs

The table below lists the key APIs used by the provider. The APIs use either a callback or promise to return the result. The APIs listed below use a callback. They provide the same functions as their counterparts that use a promise.

For details about the APIs, see [Module Description](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-avsession).

| API | Description |
| :-- | :-- |
| createAVSession(context: Context, tag: string, type: AVSessionType, callback: AsyncCallback<AVSession>): void10+ | 
Creates an AVSession.

Only one AVSession can be created for a UIAbility.

 |
| setAVMetadata(data: AVMetadata, callback: AsyncCallback<void>): void10+ | Sets AVSession metadata. |
| setAVPlaybackState(state: AVPlaybackState, callback: AsyncCallback<void>): void10+ | Sets the AVSession playback state. |
| setLaunchAbility(ability: WantAgent, callback: AsyncCallback<void>): void10+ | Starts a UIAbility. |
| getController(callback: AsyncCallback<AVSessionController>): void10+ | Obtains the controller of the AVSession. |
| getOutputDevice(callback: AsyncCallback<OutputDeviceInfo>): void10+ | Obtains the output device information. |
| activate(callback: AsyncCallback<void>): void10+ | Activates the AVSession. |
| deactivate(callback: AsyncCallback<void>): void10+ | Deactivates this session. |
| destroy(callback: AsyncCallback<void>): void10+ | Destroys the AVSession. |
| setAVQueueItems(items: Array<AVQueueItem>, callback: AsyncCallback<void>): void 10+ | Sets a playlist. |
| setAVQueueTitle(title: string, callback: AsyncCallback<void>): void10+ | Sets a name for the playlist. |
| dispatchSessionEvent(event: string, args: {\[key: string\]: Object}, callback: AsyncCallback<void>): void10+ | Dispatches a custom session event. |
| setExtras(extras: {\[key: string\]: Object}, callback: AsyncCallback<void>): void10+ | Sets a custom media packet in the form of a key-value pair. |
| getOutputDeviceSync(): OutputDeviceInfo10+ | Obtains the output device information. This API is a synchronous API. |

#### How to Develop

To enable an audio and video application to access the AVSession service as a provider, proceed as follows:

1.  Call an API in the **AVSessionManager** class to create and activate an AVSession object.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1f/v3/oRfgZwnQQdSErSkqzp-mXQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062037Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=DEED1611AB92ECD718F0D4AAFECEC6BC18AAE68A7E5357E8C2F9CA9BDFD69817)
    
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
              try {
                // Start to create and activate an AVSession object.
                // Create an AVSession object.
                let context = this.getUIContext().getHostContext() as Context;
                let type: AVSessionManager.AVSessionType = 'audio';
                let session = await AVSessionManager.createAVSession(context, 'SESSION\_NAME', type);
                await session.activate();
                console.info(\`session create done : sessionId : ${session.sessionId}\`);
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
    
2.  Set AVSession information, which includes:
    
    -   AVMetadata
    -   AVPlaybackState
    
    The controller will call an API in the **AVSessionController** class to obtain the information and display or process the information.
    
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
              // It is assumed that an AVSession object has been created. For details about how to create an AVSession object, see the node snippet in step 1.
              let session = await AVSessionManager.createAVSession(context, 'SESSION\_NAME', 'audio');
              // The player logic that triggers changes in the session metadata and playback state is omitted here.
              // Set necessary AVSession metadata.
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
              // Set the playback state to paused and set isFavorite to false.
              let playbackState: AVSessionManager.AVPlaybackState = {
                state: AVSessionManager.PlaybackState.PLAYBACK\_STATE\_PAUSE,
                isFavorite: false
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
              // Set a playlist.
              let queueItemDescription1: AVSessionManager.AVMediaDescription = {
                assetId: '001',
                title: 'music\_name',
                subtitle: 'music\_sub\_name',
                description: 'music\_description',
                mediaImage: 'PIXELMAP\_OBJECT',
                extras: { 'extras': 'any' }
              };
              let queueItem1: AVSessionManager.AVQueueItem = {
                itemId: 1,
                description: queueItemDescription1
              };
              let queueItemDescription2: AVSessionManager.AVMediaDescription = {
                assetId: '002',
                title: 'music\_name',
                subtitle: 'music\_sub\_name',
                description: 'music\_description',
                mediaImage: 'PIXELMAP\_OBJECT',
                extras: { 'extras': 'any' }
              };
              let queueItem2: AVSessionManager.AVQueueItem = {
                itemId: 2,
                description: queueItemDescription2
              };
              let queueItemsArray = \[queueItem1, queueItem2\];
              session.setAVQueueItems(queueItemsArray).then(() => {
                console.info(\`SetAVQueueItems successfully\`);
                // ...
              }).catch((err: BusinessError) => {
                console.error(\`Failed to set AVQueueItem, error code: ${err.code}, error message: ${err.message}\`);
                // ...
              });
              // Set a name for the playlist.
              let queueTitle = 'QUEUE\_TITLE';
              session.setAVQueueTitle(queueTitle).then(() => {
                console.info(\`SetAVQueueTitle successfully\`);
                // ...
              }).catch((err: BusinessError) => {
                console.error(\`Failed to set AVQueueTitle, error code: ${err.code}, error message: ${err.message}\`);
                // ...
              });
              // ...
            })
        }
        .width('100%')
        .height('100%')
      }
    }
    
3.  Set the UIAbility to be started by the controller. The UIAbility configured here is started when a user operates the UI of the controller, for example, clicking a widget in Media Controller.
    
    The UIAbility is set through the **WantAgent** API. For details, see [WantAgent](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-app-ability-wantagent).
    
    import { avSession as AVSessionManager } from '@kit.AVSessionKit';
    import { wantAgent } from '@kit.AbilityKit';
    
    @Entry
    @Component
    struct Index {
      @State message: string = 'hello world';
    
      build() {
        Column() {
          Text(this.message)
            .onClick(async () => {
              let context = this.getUIContext().getHostContext() as Context;
              let type: AVSessionManager.AVSessionType = 'audio';
              // It is assumed that an AVSession object has been created. For details about how to create an AVSession object, see the node snippet in step 1.
              let session = await AVSessionManager.createAVSession(context, 'SESSION\_NAME', type);
              let wantAgentInfo: wantAgent.WantAgentInfo = {
                wants: \[
                  {
                    bundleName: 'com.example.musicdemo',
                    abilityName: 'MainAbility'
                  }
                \],
                // OperationType.START\_ABILITIES
                operationType: 2,
                requestCode: 0,
                wantAgentFlags: \[wantAgent.WantAgentFlags.UPDATE\_PRESENT\_FLAG\]
              }
              wantAgent.getWantAgent(wantAgentInfo).then((agent) => {
                session.setLaunchAbility(agent);
              })
              // ...
            })
        }
        .width('100%')
        .height('100%')
      }
    }
    
4.  Set a custom session event. The controller performs an operation after receiving the event.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/03/v3/VgEwxO9YT8eieCy93FQIog/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062037Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=534AC624A3C18091B731D33E70DBCFE96D93702506378EB4040874CAC52264E7)
    
    The data set through **dispatchSessionEvent** is not saved in the AVSession object or AVSession service.
    
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
              // It is assumed that an AVSession object has been created. For details about how to create an AVSession object, see the node snippet in step 1.
              let type: AVSessionManager.AVSessionType = 'audio';
              let session = await AVSessionManager.createAVSession(context, 'SESSION\_NAME', type);
              let eventName = 'dynamic\_lyric';
              await session.dispatchSessionEvent(eventName, { lyric: 'This is my lyric' }).then(() => {
                console.info(\`Dispatch session event successfully\`);
                // ...
              }).catch((err: BusinessError) => {
                console.error(\`Failed to dispatch session event. Code: ${err.code}, message: ${err.message}\`);
                // ...
              })
              // ...
            })
        }
        .width('100%')
        .height('100%')
      }
    }
    
5.  Set a custom media packet. The controller performs an operation after receiving the event.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/79/v3/c_oNlmqwRR-YYjq3VmmZ-A/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062037Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=B8C13500BA7BC4EBAF356532292883E2391904CEE9D30A6B3A3A965B3285DD35)
    
    The data set by using **setExtras** is stored in the AVSession service. The data lifecycle is the same as that of the AVSession object, and the controller corresponding to the object can use **getExtras** to obtain the data.
    
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
              // It is assumed that an AVSession object has been created. For details about how to create an AVSession object, see the node snippet in step 1.
              let type: AVSessionManager.AVSessionType = 'audio';
              let session = await AVSessionManager.createAVSession(context, 'SESSION\_NAME', type);
              await session.setExtras({ extra: 'This is my custom media packet' }).then(() => {
                console.info(\`Set extras successfully\`);
                // ...
              }).catch((err: BusinessError) => {
                console.error(\`Failed to set extras. Code: ${err.code}, message: ${err.message}\`);
                // ...
              })
              // ...
            })
        }
        .width('100%')
        .height('100%')
      }
    }
    
6.  Listen for playback control commands or events delivered by the controller, for example, Media Controller.
    
    Both fixed playback control commands and advanced playback control events can be listened for.
    
    6.1 Listen for fixed playback control commands.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/47/v3/5XquLi4VSHyPP3dmdya40Q/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062037Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=EF17C88FDBB625A33715300C5AB7E6EFC28721421D008003F82AE47480085472)
    
    After the provider registers a listener for fixed playback control commands, the commands will be reflected in **getValidCommands()** of the controller. In other words, the controller determines that the command is valid and triggers the corresponding event (not used temporarily) as required. To ensure that the playback control commands delivered by the controller can be executed normally, the provider should not use a null implementation for listening.
    
    Fixed playback control commands on the session side include basic operation commands such as play, pause, previous, and next. For details, see [AVControlCommand](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-avsession-i#avcontrolcommand10).
    
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
              // It is assumed that an AVSession object has been created. For details about how to create an AVSession object, see the node snippet in step 1.
              let type: AVSessionManager.AVSessionType = 'audio';
              let session = await AVSessionManager.createAVSession(context, 'SESSION\_NAME', type);
              // ...
              // Generally, logic processing on the player is implemented in the listener.
              // After the processing is complete, use the setter to synchronize the playback information. For details, see the code snippet above.
              session.on('play', () => {
                console.info(\`on play , do play task\`);
                // ...
                // If this command is not supported, do not register it. If the command has been registered but is not used temporarily, use session.off('play') to cancel listening.
                // After the processing is complete, call SetAVPlaybackState to report the playback state.
              });
              session.on('pause', () => {
                console.info(\`on pause , do pause task\`);
                // ...
                // If this command is not supported, do not register it. If the command has been registered but is not used temporarily, use session.off('pause') to cancel listening.
                // After the processing is complete, call SetAVPlaybackState to report the playback state.
              });
              session.on('stop', () => {
                console.info(\`on stop , do stop task\`);
                // ...
                // If this command is not supported, do not register it. If the command has been registered but is not used temporarily, use session.off('stop') to cancel listening.
                // After the processing is complete, call SetAVPlaybackState to report the playback state.
              });
              session.on('playNext', () => {
                console.info(\`on playNext , do playNext task\`);
                // ...
                // If this command is not supported, do not register it. If the command has been registered but is not used temporarily, use session.off('playNext') to cancel listening.
                // After the processing is complete, call SetAVPlaybackState to report the playback state and call SetAVMetadata to report the media information.
              });
              session.on('playPrevious', () => {
                console.info(\`on playPrevious , do playPrevious task\`);
                // ...
                // If this command is not supported, do not register it. If the command has been registered but is not used temporarily, use session.off('playPrevious') to cancel listening.
                // After the processing is complete, call SetAVPlaybackState to report the playback state and call SetAVMetadata to report the media information.
              });
              session.on('fastForward', () => {
                console.info(\`on fastForward , do fastForward task\`);
                // ...
                // If this command is not supported, do not register it. If the command has been registered but is not used temporarily, use session.off('fastForward') to cancel listening.
                // After the processing is complete, call SetAVPlaybackState to report the playback state and position.
              });
              session.on('rewind', () => {
                console.info(\`on rewind , do rewind task\`);
                // ...
                // If this command is not supported, do not register it. If the command has been registered but is not used temporarily, use session.off('rewind') to cancel listening.
                // After the processing is complete, call SetAVPlaybackState to report the playback state and position.
              });
              session.on('seek', (time) => {
                console.info(\`on seek , the seek time is ${time}\`);
                // ...
                // If this command is not supported, do not register it. If the command has been registered but is not used temporarily, use session.off('seek') to cancel listening.
                // After the processing is complete, call SetAVPlaybackState to report the playback state and position.
              });
              session.on('setSpeed', (speed) => {
                console.info(\`on setSpeed , the speed is ${speed}\`);
                // ...
                // Implement the specific feature.
              });
              session.on('setLoopMode', (mode) => {
                console.info(\`on setLoopMode , the loop mode is ${mode}\`);
                // ...
                // If this command is not supported, do not register it. If the command has been registered but is not used temporarily, use session.off('setLoopMode') to cancel listening.
                // The application determines the next loop mode. After the processing is complete, call SetAVPlaybackState to report the new loop mode.
              });
              session.on('toggleFavorite', (assetId) => {
                console.info(\`on toggleFavorite , the target asset Id is ${assetId}\`);
                // ...
                // If this command is not supported, do not register it. If the command has been registered but is not used temporarily, use session.off('toggleFavorite') to cancel listening.
                // After the processing is complete, call SetAVPlaybackState to report the value of isFavorite.
              });
              // ...
            })
        }
        .width('100%')
        .height('100%')
      }
    }
    
    6.2 Listen for advanced playback control events.
    
    The following advanced playback control events can be listened for:
    
    -   **skipToQueueItem**: triggered when an item in the playlist is selected.
    -   **handleKeyEvent**: triggered when a key is pressed.
    -   **outputDeviceChange**: triggered when the output device changes.
    -   **commonCommand**: triggered when a custom playback control command changes.
    
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
              try {
                let context = this.getUIContext().getHostContext() as Context;
                // It is assumed that an AVSession object has been created. For details about how to create an AVSession object, see the node snippet in step 1.
                let type: AVSessionManager.AVSessionType = 'audio';
                let session = await AVSessionManager.createAVSession(context, 'SESSION\_NAME', type);
                // ...
                // Generally, logic processing on the player is implemented in the listener.
                // After the processing is complete, use the setter to synchronize the playback information. For details, see the code snippet above.
                session.on('skipToQueueItem', (itemId) => {
                  console.info(\`on skipToQueueItem , do skip task\`);
                  // ...
                  // Implement the specific feature.
                });
                session.on('handleKeyEvent', (event) => {
                  console.info(\`on handleKeyEvent , the event is ${JSON.stringify(event)}\`);
                  // ...
                  // Implement the specific feature.
                });
                session.on('outputDeviceChange', (device) => {
                  console.info(\`on outputDeviceChange , the device info is ${JSON.stringify(device)}\`);
                  // ...
                  // Implement the specific feature.
                });
                session.on('commonCommand', (commandString, args) => {
                  console.info(\`on commonCommand , command is ${commandString}, args are ${JSON.stringify(args)}\`);
                  // ...
                  // Implement the specific feature.
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
    
7.  Obtain an AVSessionController object for this AVSession object for interaction.
    
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
              try {
                let context = this.getUIContext().getHostContext() as Context;
                // It is assumed that an AVSession object has been created. For details about how to create an AVSession object, see the node snippet in step 1.
                let type: AVSessionManager.AVSessionType = 'audio';
                let session = await AVSessionManager.createAVSession(context, 'SESSION\_NAME', type);
    
                // Obtain an AVSessionController object for this AVSession object.
                let controller = await session.getController();
                // ...
    
                // The AVSessionController object can interact with the AVSession object, for example, by delivering a playback control command.
                let avCommand: AVSessionManager.AVControlCommand = { command: 'play' };
                controller.sendControlCommand(avCommand);
    
                // Alternatively, listen for state changes.
                controller.on('playbackStateChange', 'all', (state) => {
    
                  // do some things.
                });
                // ...
              } catch (err) {
                if (err) {
                  console.error(\`AVSession create or getController Error: Code: ${err.code}, message: ${err.message}\`);
                  // ...
                }
              }
            })
        }
        .width('100%')
        .height('100%')
      }
    }
    
8.  When the audio and video application exits and does not need to continue playback, cancel the listener and destroy the AVSession object.
    
    The code snippet below is used for canceling the listener for playback control commands:
    
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
              // It is assumed that an AVSession object has been created. For details about how to create an AVSession object, see the node snippet in step 1.
              let type: AVSessionManager.AVSessionType = 'audio';
              let session = await AVSessionManager.createAVSession(context, 'SESSION\_NAME', type);
    
              // Cancel the listener of the AVSession object.
              session.off('play');
              session.off('pause');
              session.off('stop');
              session.off('playNext');
              session.off('playPrevious');
              session.off('skipToQueueItem');
              session.off('handleKeyEvent');
              session.off('outputDeviceChange');
              session.off('commonCommand');
              // ...
            })
        }
        .width('100%')
        .height('100%')
      }
    }
    
    The code snippet below is used for destroying the AVSession object:
    
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
              // It is assumed that an AVSession object has been created. For details about how to create an AVSession object, see the node snippet in step 1.
              let type: AVSessionManager.AVSessionType = 'audio';
              let session = await AVSessionManager.createAVSession(context, 'SESSION\_NAME', type);
              // Destroy the AVSession object.
              session.destroy((err) => {
                if (err) {
                  console.error(\`Failed to destroy session. Code: ${err.code}, message: ${err.message}\`);
                  // ...
                } else {
                  console.info(\`Destroy : SUCCESS \`);
                  // ...
                }
              });
            })
        }
        .width('100%')
        .height('100%')
      }
    }
