# AVCastPicker Development

The system provides AVCastPicker, a unified casting component for audio and video casting. It is used as a system-level entry for users to select a device for switching and casting in the media controller. By integrating this component, your application can cast audio and video resources to remote devices using either the Cast+ or DLNA protocol, both within the application itself and through the media controller.

This document provides guidance for cross-device audio and video casting.

#### Restrictions

Carry out the development only when the following conditions are met:

-   **Device restrictions**
    
    Local device: smartphone or tablet running HarmonyOS 5.0.0 or later
    
    Remote device: 2-in-1 device running HarmonyOS 5.0.0 or later, HUAWEI Vision running HarmonyOS 3.1 or later, or device that supports the standard DLNA protocol
    

-   **Usage restrictions**
    -   Bluetooth and Wi-Fi are enabled on both the local and remote devices, and the devices can access the Internet.

#### Available APIs

Read the API reference to obtain the detailed API description.

-   [AVCastPicker](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ohos-multimedia-avcastpicker): casting component, which provides a unified entry for device discovery, authentication, and connection.
-   [AVCastController](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-avsession-avcastcontroller): casting controller, which is used to control playback and listen for remote playback state changes in casting scenarios.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d/v3/bC0190u-QPCFFpaBMqUxOw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062037Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=3390814EBA4F2EBB4A0DB0305620D411655DBCA7CA95D32971C78ED7115DB803)
    
    The AVCastController is obtained and returned by the system when the device is connected. It cannot be used after the device is disconnected. Otherwise, an exception is reported.
    
    To support online DRM video casting, register a callback for DRM media key request events. After obtaining a media key, call the API to process the response to the media key request.
    
    | 
    API Class
    
     | 
    
    API
    
     | 
    
    Description
    
     |
    | :-- | :-- | :-- |
    | 
    
    AVSession
    
     | 
    
    setAVMetadata(data: AVMetadata, callback: AsyncCallback<void>): void
    
     | 
    
    Configures media information, including the ID, title, author, and DRM scheme.
    
     |
    | 
    
    on(type: 'outputDeviceChange', callback: (state: ConnectionState, device: OutputDeviceInfo) => void): void
    
     | 
    
    Registers a callback to listen for device changes, including device connection state changes.
    
     |
    | 
    
    getAVCastController(callback: AsyncCallback<AVCastController>): void
    
     | 
    
    Obtains the control interface for remote casting.
    
     |
    | 
    
    AVCastController
    
     | 
    
    sendControlCommand(command: AVCastControlCommand, callback: AsyncCallback<void>): void
    
     | 
    
    Controls a casting session and executes various playback control commands during the casting.
    
     |
    | 
    
    prepare(item: AVQueueItem, callback: AsyncCallback<void>): void
    
     | 
    
    Prepares for playback, loads and buffers resources, and does not trigger playback.
    
     |
    | 
    
    start(item: AVQueueItem, callback: AsyncCallback<void>): void
    
     | 
    
    Starts to play a media asset.
    
     |
    | 
    
    processMediaKeyResponse(assetId: string, response: Uint8Array): Promise<void>
    
     | 
    
    Provides the key required by the DRM resource.
    
     |
    | 
    
    on(type: 'keyRequest', callback: KeyRequestCallback): void
    
     | 
    
    Registers a callback to listen for a media key request.
    
     |
    | 
    
    on(type: 'playbackStateChange', filter: Array<string> | 'all', callback: (state: AVPlaybackState) => void): void
    
     | 
    
    Registers a callback function to listen for playback state changes.
    
     |
    | 
    
    on(type: 'mediaItemChange', callback: Callback<AVQueueItem>): void
    
     | 
    
    Registers a callback to listen for media item changes. The content being played is returned.
    
     |
    

#### How to Develop

1.  Create a player and an AVSession.
    
    Creates and activates an AVSession through the AVSessionManager.
    
    For details about how to obtain the context in the example, see [Obtaining the Context of the UIAbility](../../../../../application-framework/ability-kit/stage-model-development/stage-model-application-components/uiability-component/uiability-usage/document.md#obtaining-the-context-of-uiability).
    
    import  { avSession }  from '@kit.AVSessionKit'; // Import the AVSession module.
    
    // Declare the global AVSession object. This declaration is added outside the class. If the global variable needs to be declared in the class, delete export let.
    export let session: avSession.AVSession;
    // Create an AVSession object.
    async createSession(context: Context) {
      // The AVSession object can be used in the basic playback control and casting scenarios.
      session = await avSession.createAVSession(context, 'video\_test', 'video'); // 'audio' indicates an audio application, and 'video' indicates a video application.
      await session.activate();
      // Set the following parameters to notify the system that the application supports casting.
      session.setExtras({
        requireAbilityList: \['url-cast'\],
      }); 
      console.info(\`Session created. sessionId: ${session.sessionId}\`);
    }
    
2.  Configure media resource information, register basic playback control callbacks, and integrate with the basic playback control services of the media controller.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f1/v3/LtxspLAgQqOeIKdQsu9qzg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062037Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=3CC9B7ACD7A96D76CF0B2C2B47943FB5C7AC0C2F8140595ECC918DDACD87ADBC)
    
    -   Applications can use the **filter** field to specify the protocol types for device discovery and filtering, so as to match the desired casting devices.
        
        After casting, when the application player switches episodes, the **filter** parameter can control whether the media controller displays a list of castable devices. If this parameter is set to **0**, the media controller determines that casting is not supported and hides the display of castable devices. This prevents users from casting content from the media controller while the application resources are unavailable.
        
    -   To display only devices that support DRM content casting in the AVCastPicker, explicitly set **drmSchemes** in **AVMetadata**.
    
    // Import the AVSession module if your code is not in the same file as the AVSession declaration.
    import  { avSession }  from '@kit.AVSessionKit'; // Import the AVSession module.
    export let session: avSession.AVSession;
    @Entry
    @Component
    struct Index{
      public setAVMetadata(playInfo: avSession.AVMediaDescription): Promise<void> {
        const metadata: avSession.AVMetadata = {
            assetId: playInfo.assetId, // Set an actual ID.
            title: playInfo.title, // Play the title of media resource.
            subtitle: playInfo.subtitle,// Play the subtitle of media resource.
            // Discover cast+ streams and DLNA-compliant devices. TYPE\_CAST\_PLUS\_STREAM is required by default.
            filter: avSession.ProtocolType.TYPE\_CAST\_PLUS\_STREAM|avSession.ProtocolType.TYPE\_DLNA,
            mediaImage: playInfo.mediaImage,
            artist: playInfo.artist,
            // For DRM resources, configure the supported DRM UUIDs for device filtering.
            drmSchemes: \['3d5e6d35-9b9a-41e8-b843-dd3c6e72c42c'\]
          };
        return session.setAVMetadata(metadata);
      }
      public setSessionListener() {
       // Register and implement basic playback control commands as required based on the access checklist. The following is an example:
        session?.on('play', () => {
        });
        session?.on('pause', () => {
        });
      }
      build(){
        Column()
      }
    }
    
3.  Create the AVCastPicker on the playback page that requires casting.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ef/v3/qzXcUm0fQBe5m0gXJwqV1w/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062037Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=8BF4EBF1ABFDE78B5F47F35FC9DEF05D795100B08FCCDB1E1EFEF2E73FFD4878)
    
    -   If the page is not displayed after the AVCastPicker is created or if the Picker appears blank upon opening, check whether you have completed steps 1 and 2 for integrating with the basic playback control services of the media controller and accurately configured the **AVMetadata** and **Extras** parameters.
    -   The AVCastPicker provides the **CustomerPicker** parameter, which enables applications to customize the appearance of the Picker. For details, see [Implementing a Custom Style](../../using-the-call-device-switching-component/document.md#implementing-a-custom-style).
    
    import { AVCastPicker, AVCastPickerState } from '@kit.AVSessionKit';
    
    // Applications can use onStateChange to listen for the component shown/hidden state. When the component appears, do not destroy the display of the AVCastPicker. When the component disappears, hide the AVCastPicker based on service requirements.
    private onStateChange(state: AVCastPickerState) {
      if (state == AVCastPickerState.STATE\_APPEARING) {
        console.log('The picker starts showing.');
      } else if (state == AVCastPickerState.STATE\_DISAPPEARING) {
        console.log('The picker finishes presenting.');
      }
    }
    
    // Create the component and set its size.
    build() {
      Row() {
        Column() {
          AVCastPicker({
            normalColor: Color.Red,
            onStateChange: this.onStateChange
          })
            .width('40vp')
            .height('40vp')
            .border({ width: 1, color: Color.Red })
        }.height('50%')
      }.width('50%')
    }
    
4.  Register the AVSession casting control callback to sense the device connection.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2/v3/5_sahUaQReqD9AIqrAf7zQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062037Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=9CD6F3FD53E559A0FCF4ECB985D23958D2A6661425282F29AB05BAF51536A8D5)
    
    The following code shows the processing after the device is connected.
    
    -   After the connection is successful, the AVCastController is obtained through the AVSession for subsequent playback control.
    -   The application listens for the **on('outputDeviceChange')** callback. When receiving a message indicating a casting to the remote device, the application refreshes its playback screen to display the casting or remote control page and pauses playback on the local device. Conversely, when the application receives a message indicating a switching back to the local device, it refreshes the playback screen to display the local playback page and resumes playback on the local device.
    -   If DRM online resources need to be pushed, the corresponding resource is obtained from the server based on the DRM capability supported by the remote device.
    -   After the DRM resource is pushed, the media key request event should be registered. After a media key is obtained from the server, it is provided to the remote device by processing the response to the media key request.
    
    import { BusinessError } from '@kit.BasicServicesKit';
    import { avSession } from '@kit.AVSessionKit';
    import { session } from './xxx'; // AVSession declaration file.
    
      castController: avSession.AVCastController | undefined = undefined;
      getAVCastController() {
        // If casting is supported, use the following API to listen for device connection state changes:
        session.on('outputDeviceChange', async (connectState: avSession.ConnectionState,
                                                     device: avSession.OutputDeviceInfo) => {
          // Update the playback screen within the application based on the current device and device connection state.
          let currentDevice: avSession.DeviceInfo = device?.devices?.\[0\];
          if (currentDevice.castCategory === avSession.AVCastCategory.CATEGORY\_REMOTE && connectState === avSession.ConnectionState.STATE\_CONNECTED) { // Device connected.
            console.info(\`Device connected: ${device}\`);
            this.castController = await session.getAVCastController();
            console.info('Succeeded in getting a cast controller');
            // Query the current playback state.
            let avPlaybackState = await this.castController?.getAVPlaybackState();
            console.info(\`Succeeded in AVPlaybackState resource obtained: ${avPlaybackState}\`);
            // Listen for playback state changes.
            this.castController?.on('playbackStateChange', 'all', (state: avSession.AVPlaybackState) => {
              console.info(\`Succeeded in Playback state changed: ${state}\`);
            });
            if (currentDevice.supportedProtocols === avSession.ProtocolType.TYPE\_CAST\_PLUS\_STREAM) {
              // The device supports the cast+ protocol.
            } else if (currentDevice.supportedProtocols === avSession.ProtocolType.TYPE\_DLNA) {
              // The device supports the DLNA protocol.
            }
            // The device supports chinaDRM and listens for the media key request event. The event can be listened for before the device initiates a DRM resource casting.
            if (currentDevice.supportedDrmCapabilities?.includes('3d5e6d35-9b9a-41e8-b843-dd3c6e72c42c')) {
              this.castController?.on('keyRequest', this.keyRequestCallback);
            }
          }
        })
      }
    
      // Process the DRM media key request event.
      private keyRequestCallback: avSession.KeyRequestCallback = async (assetId: string, requestData: Uint8Array) => {
        // Obtain the DRM URL based on the asset ID.
        let drmUrl: string = 'http://license.xxx.xxx.com:8080/drmproxy/getLicense';
        // Obtain a media key from the server. For details, see the appendix.
        let licenseResponseData = await this.getLicense(drmUrl, requestData); 
        try {
          // Process the response to the DRM media key request.
          await this.castController?.processMediaKeyResponse(assetId, licenseResponseData);
        } catch (error) {
          console.error(\`Failed to process the response corresponding to the media key. Error: ${error}\`);
        }
      }
    
5.  Use the AVCastController to play the media asset.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cf/v3/wDlZ1NogRwOEYYA0QWZZXg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062037Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=30E8AD72D02612814B8213258090F484258D09DF935A5E8CCEF4FA70ACA785CC)
    
    The URL in the code snippet below is for reference only. You need to check the media asset validity and set the URL based on service requirements.
    
    -   If local files are used for playback, ensure that the files are available and use the application sandbox path to access the files. For details, see [Obtaining Application File Paths](../../../../../application-framework/ability-kit/stage-model-development/stage-model-application-components/context-stage-model/document.md#obtaining-application-file-paths). For details about the application sandbox and how to push files to the application sandbox, see [File Management](../../../../../application-framework/core-file-kit/application-files/application-sandbox/document.md).
    -   To use the user file through the FilePicker, see [Selecting User Files](../../../../../application-framework/core-file-kit/user-files/selecting-and-saving-user-files/selecting-user-files/document.md).
    -   If a network playback path is used, [request the permission](../../../../../system/security/application-access-control/application-permission-management/requesting-application-permissions/declaring-permissions/document.md) ohos.permission.INTERNET.
    -   To use DRM resources, set the **drmSchemes** field.
    
    playItem() {
        // Set playback parameters.
        let playItem : avSession.AVQueueItem = {
          itemId: 0,
          description: {
            assetId: 'VIDEO-1',
            title: 'ExampleTitle',
            artist: 'ExampleArtist',
            // For network resource casting, set mediaUri. For local resource casting, set fdSrc to the file descriptor after a local file is opened.
            mediaUri: 'https://xxx.xxx.com/example.mp4',
            // The value of the mediaType parameter should be capitalized, which can be AUDIO or VIDEO.
            mediaType: 'VIDEO',
            mediaSize: 1000,
            // startPosition indicates the casting progress. Set this parameter to synchronize the local playback progress to the remote device.
            startPosition: 0,
            // Playback duration of the casting resource. Set this parameter to synchronize the local playback duration to the remote device.
            duration: 100000,
            albumCoverUri: 'https://www.example.jpeg',
            albumTitle: 'ExampleAlbum',
            appName: 'ExampleApp',
            // DRM resource. The supported DRM scheme must be configured. The following uses chinaDRM as an example.
            drmScheme: '3d5e6d35-9b9a-41e8-b843-dd3c6e72c42c',
          }
        };
        // Prepare for playback. This operation triggers loading and buffering, but not the actual playback.
        this.castController?.prepare(playItem, () => {
          console.info('Preparation done');
          // Start playback to trigger playback on the remote device. Call the start API after the preparation is successful.
          this.castController?.start(playItem, () => {
            console.info('Playback started');
          });
        });
      }
    
6.  Use the AVCastController to listen for control commands and control the playback.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b/v3/0RLqWNr6TyuFgWCab-Ju2A/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062037Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=B4516CA0E52225316E558C23958B14F93777FC3C09EBB81D1B54A2F2F21AAC79)
    
    -   Applications can use the specified listening and control commands to implement control over casting devices and respond to controls from the remote device or media controller.
    -   The media controller dynamically enables or disables buttons on the control widget based on the registered listeners of the application.
    -   Currently, the system does not support clarity adjustment. If an application wants to provide a clarity adjustment option, it must re-deliver resources based on the new clarity level when users choose a different clarity setting.
    
      playControl() {
        // Record the remote controller this.castController obtained from the AVSession.
        // The application sends the play command to the remote device.
        let avCommand: avSession.AVCastControlCommand = {command:'play'};
        this.castController?.sendControlCommand(avCommand);
    
        // The application sends the pause command to the remote device.
        avCommand = {command:'pause'};
        this.castController?.sendControlCommand(avCommand);
    
        // The application adjusts the volume on the remote device.
        avCommand = {
          command: 'setVolume',
          parameter: 1
        };
        this.castController?.sendControlCommand(avCommand);
        
        // The application adjusts the playback position on the remote device.
        avCommand = {
          command: 'seek',
          parameter: 1
        };
        this.castController?.sendControlCommand(avCommand);
       // For more control commands, see [AVCastControlCommand](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-avsession-i#avcastcontrolcommand10).
      }
      controlListener() {
        // The application listens for the next/previous track or episode switches initiated by the remote device or media controller.
        this.castController?.on('playPrevious', () => {
          console.info('PlayPrevious done');
        });
        this.castController?.on('playNext', () => {
          console.info('PlayNext done');
        });
    
        // The application listens for the playback state, real-time position, and volume change events of the remote device or media controller.
        this.castController?.on('playbackStateChange', (playbackState: avSession.AVPlaybackState)=>{
          if (playbackState?.state) {
            // Handle playback state changes.
          }
          if (playbackState?.position) {
             // Handle position changes. The playback position on the remote device is determined based on position.
          }
          if (playbackState?.volume) {
            // Handle volume changes.
          }
        });
    
        // The application listens for the playback completion event on the remote device. The event callback should be implemented in one of the following modes based on the service. Otherwise, a black screen occurs on the remote device.
        // 1. Automatically switches to the next episode (if available) by calling prepare and start with a new URL (refer to Step 5).
        // 2. Loops the current episode by calling prepare and start again with the current URL (refer to Step 5).
        // 3. Disconnects casting if the service logic no longer supports it (refer to Step 9).
        this.castController?.on('endOfStream', () => {
          // Service-specific processing
        });
        
        // The application listens for the position adjustment completion events (for example, fast forward, rewind, or seek bar dragging) from the remote device or media controller.
        this.castController?.on('seekDone', (position: number) => {
          // seekDone indicates that the position adjustment is completed. After receiving this callback, refresh the progress bar in the application based on the position in the 'playbackStateChange' callback.
          // When the application calls seek to adjust the remote playback position, wait for the seekDone callback before refreshing for more accuracy.
         });
      }
    
7.  Request a continuous casting task to prevent the application from being frozen by the system when the application switches to the background.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/db/v3/7NyFXlmgQ4SNh_nkxH9NUg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062037Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=A13DCF4A72741890D25F51D22870140DB1412F4D075F751559BA14F1B1C14951)
    
    When requesting a continuous task, perform the following operations on the **module.json5** file:
    
    1.  Configure the continuous task permission **ohos.permission.KEEP\_BACKGROUND\_RUNNING**.
    2.  Declare the background mode type **AUDIO\_PLAYBACK** for the UIAbility that needs to use the continuous task. Choosing either option ensures uninterrupted audio playback when the application is running in the background, during screen lock, or while casting with the screen off.
    
    import { backgroundTaskManager } from '@kit.BackgroundTasksKit';
    import { wantAgent } from '@kit.AbilityKit';
    import { BusinessError } from '@kit.BasicServicesKit';
    
    let context: Context = getContext(this);
    
    function startContinuousTask() {
        let wantAgentInfo: wantAgent.WantAgentInfo = {
            // List of operations to perform after the notification is clicked.
            wants: \[
              {
                bundleName: "com.example.myapplication",
                abilityName: "EntryAbility",
              }
            \],
            // Type of the operation to perform after the notification is clicked.
            operationType: wantAgent.OperationType.START\_ABILITY,
            // Custom request code.
            requestCode: 0,
            // Execution attribute of the operation to perform after the notification is clicked.
            wantAgentFlags: \[wantAgent.WantAgentFlags.UPDATE\_PRESENT\_FLAG\]
        };
    
        // Obtain WantAgent by using the getWantAgent API of the wantAgent module.
        try {
            wantAgent.getWantAgent(wantAgentInfo).then((wantAgentObj) => {
                try {
                    backgroundTaskManager.startBackgroundRunning(context,
                        backgroundTaskManager.BackgroundMode.AUDIO\_PLAYBACK, wantAgentObj).then(() => {
                        console.info('Succeeded in requesting to start running in background');
                    }).catch((error: BusinessError) => {
                        console.error(\`Failed to request to start running in background. Code: ${error.code}, message: ${error.message}\`);
                    });
                } catch (error) {
                    console.error(\`Failed to request to start running in background. Error: ${error}\`);
                }
            });
        } catch (error) {
            console.error(\`Failed to get WantAgent. Error: ${error}\`);
        }
    }
    
8.  Switch resources after casting.
    -   After starting the cast, the application can check whether casting is still active by calling **getOutputDevice()** to obtain the current playback device when re-entering the playback details page.
        
        import  { avSession }  from '@kit.AVSessionKit'; // Import the AVSession module.
        // Import the AVSession module if your code is not in the same file as the AVSession declaration.
        import { session } from './xxx'; // AVSession declaration file.
        this.session?.getOutputDevice().then((outputDeviceInfo: avSession.OutputDeviceInfo) => {
          // If castCategory of the current device is Remote, casting is ongoing.
          let isCasting = outputDeviceInfo.devices\[0\].castCategory === avSession.AVCastCategory.CATEGORY\_REMOTE;
        }).catch((err: BusinessError) => {
          console.error(\`GetOutputDevice BusinessError: code: ${err.code}, message: ${err.message}\`);
        });
        
    -   When casting has started and the user exits the playback details page to return to the application's home page, you are not advised to call **stopCasting** to stop casting. Instead, offer users a way to go back to the casting page.
    -   If the user exits the details page during casting and selects another video to play, the application should determine whether the new resource can be cast. The following two cases are available:
        -   Case 1: The new video can be cast.
            
            Direct switch: The application calls **prepare** and **start** to switch the casting resource. See step 5. The remote device plays the new video, and the local screen updates to the casting page. Users are not required to disconnect and then restart casting.
            
            Manual switch: The application does not switch the casting resource automatically. Instead, it shows the casting button normally, but does not create an AVCastPicker instance. After the button is touched, the application calls **prepare** and **start** to switch the casting resource, and the local screen updates to the casting page. Users are not required to disconnect and then restart casting.
            
        -   Case 2: The new video cannot be cast. The application plays the video locally and hides the casting buttons.
9.  Handle audio focus. For details, see [Audio Playback Concurrency Policy](../../../../audio-kit/audio-focus-and-audio-session-management/introduction-to-audio-focus/document.md).
    
    After the application enters the casting state, the application needs to unregister the focus processing event to avoid being affected by the focus request of other applications.
    
10.  Stop casting.
     
     -   When the remote device is disconnected, the application receives an event and the system automatically disconnects from the remote device.
     -   The application can also call the API to proactively disconnect from the casting.
         
         async release() {
           // Generally, when the application exits and you do not want to continue the playback, you can call the API to end the playback.
           await session.stopCasting();
         }
         
     
     -   It is recommended that the application listen for the **AVCastController.on('playbackStateChange')** callback and save the position in the callback. When the casting is disconnected, the application can refresh the local playback details page to continue the playback on the local device and adjust the local playback position based on the position.

#### Automatic Switching to Resource Casting

A user turns on wireless casting to cast their phone or other device's screen onto a large screen. Then the user opens a video application and plays a video on the large screen. To achieve this, some extra adaptation work is required.

1.  After opening the playback page, the application needs to check for a screen-mirroring device and avoid conflicts with other applications.
    
    import  { avSession }  from '@kit.AVSessionKit'; // Import the AVSession module.
    import { BusinessError } from '@kit.BasicServicesKit';
      
    let session: avSession.AVSession; // Declare a global AVSession object. This declaration is added outside the class. If the global variable needs to be declared in the class, delete let.
    **let** currentAVSession: avSession.AVSession | undefined = undefined;
    async checkOtherCast() { 
      try {
        let currentOutputDevice: avSession.OutputDeviceInfo = currentAVSession.getOutputDeviceSync(); 
      } catch (err) {
        let error = err as BusinessError; 
        console.error(\`getOutputDeviceSync error, error code: ${error.code}, error message: ${error.message}\`); 
      } 
    }
    
    1.  If the return value is null, no screen-mirroring device is available, or another application is already casting. In this case, the application should play the content on the local device.
    2.  If the return value is not null, the application should traverse the devices to find a device with **castCategory** set to **CATEGORY\_REMOTE** and **supportedProtocols** based on the returned **OutputDeviceInfo**. (The determination logic is the same as that in the preceding casting process.) If such a device is found, the application can cast the video playback page onto that device.
2.  After casting, the application still listens for the device state (for example, disconnected). For details, see [How to Develop](#开发步骤).

## Appendix

**Obtain a media key from the server**

You need to obtain a media key based on the actual resource and service address. The following sample code is for reference only.

import { http } from '@kit.NetworkKit';

 // Obtain a media key based on the actual resource and service address. The following sample code is for reference only.
  async getLicense(drmUrl: string, requestData: Uint8Array): Promise<Uint8Array | undefined> {
    let licenseRequestStr: string = this.byteToString(requestData);
    let licenseResponseStr: string = 'defaultStr';
    let httpRequest = http.createHttp();
    try {
      let response: http.HttpResponse = await httpRequest.request(drmUrl, {
        method: http.RequestMethod.POST,
        header: {
          'Content-Type': 'application/json',
          'Accept-Encoding': 'gzip, deflate',
        },
        extraData: licenseRequestStr,
        expectDataType: http.HttpDataType.STRING,
      });
      if (response?.responseCode == http.ResponseCode.OK) {
        if (typeof response.result == 'string') {
          licenseResponseStr = response.result;
        }
      }
      httpRequest.destroy();
    } catch (error) {
      console.error(\`Failed to request Http. Error: ${error}\`);
      return undefined;
    }
    return this.stringToByte(licenseResponseStr);
  }

  /\*\*
   \* Uint8Array to string
   \* @param arr Uint8Array
   \* @returns string
   \*/
  byteToString(arr: Uint8Array): string {
    let str: string = ''
    let \_arr: Uint8Array = arr

    for (let i = 0; i < \_arr.length; i++) {
      // Convert the value to a binary string.
      let binaryStr: string = \_arr\[i\].toString(2)
      let matchArray = binaryStr.match(new RegExp('/^1+?(?=0)/'))
      if (matchArray && binaryStr.length == 8) {
        let bytesLength: number = matchArray\[0\].length
        let store: string = \_arr\[i\].toString(2).slice(7 - bytesLength)

        for (let j = 1; j < bytesLength; j++) {
          store += \_arr\[j + i\].toString(2).slice(2)
        }
        str += String.fromCharCode(Number.parseInt(store, 2))
        i += bytesLength - 1
      } else {
        str += String.fromCharCode(\_arr\[i\])
      }
    }
    return str
  }

  /\*\*
   \* Convert the string into a Uint8Array.
   \* @param str string
   \* @returns Uint8Array
   \*/
  stringToByte(str: string): Uint8Array {
    let bytes: number\[\] = new Array()
    let unicode: number

    for (let i = 0; i < str.length; i++) {
      unicode = str.charCodeAt(i)
      if (unicode >= 0x010000 && unicode <= 0x10FFFF) {
        bytes.push(((unicode >> 18) & 0x07) | 0xf0)
        bytes.push(((unicode >> 12) & 0x3F) | 0x80)
        bytes.push(((unicode >> 6) & 0x3F) | 0x80)
        bytes.push((unicode & 0x3F) | 0x80)
      } else if (unicode >= 0x000800 && unicode <= 0x00FFF) {
        bytes.push(((unicode >> 12) & 0x07) | 0xf0)
        bytes.push(((unicode >> 6) & 0x3F) | 0x80)
        bytes.push((unicode & 0x3F) | 0x80)
      } else if (unicode >= 0x000800 && unicode <= 0x0007FF) {
        bytes.push(((unicode >> 6) & 0x3F) | 0x80)
        bytes.push((unicode & 0x3F) | 0x80)
      } else {
        bytes.push(unicode & 0xFF)
      }
    }
    return new Uint8Array(bytes);
  }
