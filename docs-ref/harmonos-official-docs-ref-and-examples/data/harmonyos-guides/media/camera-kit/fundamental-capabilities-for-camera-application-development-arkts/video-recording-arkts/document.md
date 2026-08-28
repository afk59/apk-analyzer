# Video Recording (ArkTS)

Before developing a camera application, you must [request required permissions](../../requesting-camera-development-permissions/document.md).

A camera application invokes and controls a camera device to perform basic operations such as preview, photo capture, and video recording.

As another important function of the camera application, video recording is the process of cyclic frame capture. For the custom configuration of video recording, you can refer to step 4 in [Photo Capture](../photo-capture-arkts/document.md) to set information such as resolution, flash, focal length, photo quality, and rotation angle.

#### How to Develop

Read [Camera](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-camera) for the API reference.

1.  Import the media module.
    
    The [APIs](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-media) provided by this module are used to obtain the surface ID and create a video output stream.
    
    import { BusinessError } from '@kit.BasicServicesKit';
    import { camera } from '@kit.CameraKit';
    import { media } from '@kit.MediaKit';
    
2.  Create a surface.
    
    Call createAVRecorder() of the media module to create an [AVRecorder](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-media-avrecorder) instance, and call [getInputSurface](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-media-avrecorder#getinputsurface9) of the instance to obtain the surface ID, which is associated with the video output stream to process the stream data.
    
    async function getVideoSurfaceId(aVRecorderConfig: media.AVRecorderConfig): Promise<string | undefined> {  // For details about aVRecorderConfig, see step 3 "Create a video output stream" below.
      let avRecorder: media.AVRecorder | undefined = undefined;
      let videoSurfaceId: string | undefined = undefined;
      try {
        avRecorder = await media.createAVRecorder();
        if (avRecorder === undefined) {
          return videoSurfaceId;
        }
        await avRecorder.prepare(aVRecorderConfig);
        videoSurfaceId = await avRecorder.getInputSurface();
      } catch (error) {
        let err = error as BusinessError;
        console.error(\`createAVRecorder call failed. error code: ${err.code}\`);
      }
      return videoSurfaceId;
    }
    
3.  Create a video output stream.
    
    Obtain the video output streams supported by the current device from **videoProfiles** in [CameraOutputCapability](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-camera-i#cameraoutputcapability). Then, define video recording parameters and use [createVideoOutput](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-camera-cameramanager#createvideooutput) to create a video output stream.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2a/v3/C8DhCdLZRaq0Zkkj9D-IJg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062038Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=B51C8135F529F55AC681D60D935C545552BE3FB66A068F0670C7132FD0060536)
    
    1.  The preview stream and video output stream must have the same aspect ratio of the resolution. For example, the aspect ratio in the code snippet below is 640:480 (which is equal to 4:3), then the aspect ratio of the resolution of the preview stream must also be 4:3. This means that the resolution can be 640:480, 960:720, 1440:1080, or the like.
        
    2.  Before setting the resolution width and height of the preview output stream, call [AVRecorderProfile](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-media-i#avrecorderprofile9) to obtain the configurable width and height range for video frames.
        
    3.  To obtain the video rotation angle (specified by **rotation**), call [getVideoRotation](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-camera-videooutput#getvideorotation12) in [VideoOutput](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-camera-videooutput).
        
    4.  To configure the frame rate for a video output stream, select a suitable **videoProfile** from **videoProfiles** of [CameraOutputCapability](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-camera-i#cameraoutputcapability). Ensure that [frameRateRange](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-camera-i#frameraterange) of the selected profile meets your service requirements.
        
    
    async function getVideoOutput(cameraManager: camera.CameraManager, videoSurfaceId: string, cameraOutputCapability: camera.CameraOutputCapability): Promise<camera.VideoOutput | undefined> {
      if (!cameraManager || !videoSurfaceId || !cameraOutputCapability || !cameraOutputCapability.videoProfiles) {
        return;
      }
      let videoProfilesArray: Array<camera.VideoProfile> = cameraOutputCapability.videoProfiles;
      if (!videoProfilesArray || videoProfilesArray.length === 0) {
        console.error("videoProfilesArray is null or \[\]");
        return undefined;
      }
      // AVRecorderProfile.
      let aVRecorderProfile: media.AVRecorderProfile = {
        fileFormat: media.ContainerFormatType.CFT\_MPEG\_4, // Video file container format. Only MP4 is supported.
        videoBitrate: 100000, // Video bit rate.
        videoCodec: media.CodecMimeType.VIDEO\_AVC, // Video file encoding format. AVC is supported.
        videoFrameWidth: 640, // Video frame width.
        videoFrameHeight: 480, // Video frame height.
        videoFrameRate: 30 // Video frame rate.
      };
      // Define video recording parameters. The ratio of the resolution width (videoFrameWidth) to the resolution height (videoFrameHeight) of the video output stream must be the same as that of the preview stream.
      let avMetadata: media.AVMetadata = {
       videoOrientation: '90' // The value of rotation is 90, which is obtained through getVideoRotation.
      }
      
      let aVRecorderConfig: media.AVRecorderConfig = {
        videoSourceType: media.VideoSourceType.VIDEO\_SOURCE\_TYPE\_SURFACE\_YUV,
        profile: aVRecorderProfile,
        url: 'fd://35', // This is an example. Replace it with the actual path.
        metadata: avMetadata
      };
      // Create an AVRecorder object and set video recording parameters.
      let avRecorder: media.AVRecorder | undefined = undefined;
      try {
        avRecorder = await media.createAVRecorder();
        if (avRecorder === undefined) {
          return undefined;
        }
        await avRecorder.prepare(aVRecorderConfig);
      } catch (error) {
        let err = error as BusinessError;
        console.error(\`createAVRecorder call failed. error code: ${err.code}\`);
        await avRecorder?.release();
        return;
      }
    
      // Create a VideoOutput instance.
      let videoOutput: camera.VideoOutput | undefined = undefined;
      // The width and height of the videoProfile object passed in by createVideoOutput must be the same as those of aVRecorderProfile.
      let videoProfile: undefined | camera.VideoProfile = videoProfilesArray.find((profile: camera.VideoProfile) => {
        return profile.size.width === aVRecorderProfile.videoFrameWidth && profile.size.height === aVRecorderProfile.videoFrameHeight;
      });
      if (!videoProfile) {
        console.error('videoProfile is not found');
        await avRecorder.release();
        return undefined;
      }
      try {
        videoOutput = cameraManager.createVideoOutput(videoProfile, videoSurfaceId);
      } catch (error) {
        let err = error as BusinessError;
        console.error('Failed to create the videoOutput instance. errorCode = ' + err.code);
        await avRecorder.release();
      }
      return videoOutput;
    }
    
4.  Start video recording.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f5/v3/Y60dDR6HTLy7wtk0gpgRog/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062038Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=AE9FC89A1D665581E6BD322B3942E417926BC2BA769092BC3EEF2E07B0D3527A)
    
    -   When setting the frame rate of the preview stream, you must first query the frame rate of the video stream by calling [getActiveFrameRate](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-camera-previewoutput#getactiveframerate12).
        
    -   If the video stream uses a range of frame rates, the preview stream must be set to the same range.
        
    -   If the video stream uses a fixed frame rate, the preview stream must be set to a fixed rate that is a divisor of the video frame rate.
        
    
    Call [start](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-camera-videooutput#start-1) of the VideoOutput instance to start the video output stream, and then call [start](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-media-avrecorder#start9) of the AVRecorder instance to start recording.
    
    async function startVideo(videoOutput: camera.VideoOutput, avRecorder: media.AVRecorder): Promise<void> {
     try {
       await videoOutput.start();
     } catch (error) {
       let err = error as BusinessError;
       console.error(\`start videoOutput failed, error: ${err.code}\`);
     }
     avRecorder.start(async (err: BusinessError) => {
     if (err) {
       console.error(\`Failed to start the video output ${err.message}\`);
       return;
     }
     console.info('Callback invoked to indicate the video output start success.');
     });
    }
    
5.  Stop video recording.
    
    Call [stop](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-media-avrecorder#stop9-1) of the AVRecorder instance to stop recording, and then call [stop](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-camera-videooutput#stop-1) of the VideoOutput instance to stop the video output stream.
    
    async function stopVideo(videoOutput: camera.VideoOutput, avRecorder: media.AVRecorder): Promise<void> {
      avRecorder.stop((err: BusinessError) => {
      if (err) {
        console.error(\`Failed to stop the video output ${err.message}\`);
        return;
      }
      console.info('Callback invoked to indicate the video output stop success.');
      });
      await videoOutput.stop();
    }
    

#### Status Listening

During camera application development, you can listen for the status of the video output stream, including recording start, recording end, and video output errors.

-   Register the **'frameStart'** event to listen for recording start events. This event can be registered when a VideoOutput instance is created and is triggered when the bottom layer starts exposure for recording for the first time. Video recording starts as long as a result is returned.
    
    function onVideoOutputFrameStart(videoOutput: camera.VideoOutput): void {
      videoOutput.on('frameStart', (err: BusinessError) => {
        if (err !== undefined && err.code !== 0) {
          return;
        }
        console.info('Video frame started');
      });
    }
    
-   Register the **'frameEnd'** event to listen for recording end events. This event can be registered when a VideoOutput instance is created and is triggered when the last frame of recording ends. Video recording ends as long as a result is returned.
    
    function onVideoOutputFrameEnd(videoOutput: camera.VideoOutput): void {
      videoOutput.on('frameEnd', (err: BusinessError) => {
        if (err !== undefined && err.code !== 0) {
          return;
        }
        console.info('Video frame ended');
      });
    }
    
-   Register the **'error'** event to listen for video output errors. The callback function returns an error code when an API is incorrectly used. For details about the error code types, see [CameraErrorCode](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-camera-e#cameraerrorcode).
    
    function onVideoOutputError(videoOutput: camera.VideoOutput): void {
      videoOutput.on('error', (error: BusinessError) => {
        console.error(\`Video output error code: ${error.code}\`);
      });
    }
