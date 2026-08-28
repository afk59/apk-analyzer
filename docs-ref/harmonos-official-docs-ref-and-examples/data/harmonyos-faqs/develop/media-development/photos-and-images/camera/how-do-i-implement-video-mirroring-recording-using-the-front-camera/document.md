# How do I implement video mirroring recording using the front camera?

To record video using the front camera, you need to enable the mirroring feature. Call [enableMirror()](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-camera-videooutput#enablemirror15) to enable or disable mirroring.

Before enabling mirroring, you need to call [isMirrorSupported](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-camera-videooutput#ismirrorsupported15) to check whether the device supports mirroring. The sample code is as follows:

function testIsMirrorSupported(videoOutput: camera.VideoOutput): boolean {
  let isSupported: boolean = videoOutput.isMirrorSupported();
  return isSupported;
}

-   If mirroring is supported, you can call [enableMirror()](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-camera-videooutput#enablemirror15) to enable or disable mirroring. The sample code is as follows:
    
    import { camera } from '@kit.CameraKit';
    import { media } from '@kit.MediaKit';
    import { BusinessError } from '@kit.BasicServicesKit';
    
    // ...
    
    function enableMirror(videoOutput: camera.VideoOutput, mirrorMode: boolean): void {
      try {
        videoOutput.enableMirror(mirrorMode);
      } catch (error) {
        let err = error as BusinessError;
      }
    }
    
    After enabling or disabling mirroring, call [getVideoRotation](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-camera-videooutput#getvideorotation12) and [updateRotation](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-media-avrecorder#updaterotation12) to update the rotation angle.
    
-   If mirroring is not supported, you can use [rotate](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ts-universal-attributes-transformation#rotate) to implement the component flipping effect, mirror the preview stream to facilitate users in previewing the video content, and then process the video file separately. Use the third-party library FFmpeg to implement content mirroring for the video file.
    1.  For the settings of the recording preview stream, use **rotate** to perform mirror flipping on the preview stream component **XComponent**. The code example is as follows:
        
        // Flip Angle
        @State angle: number = 180;
        // Use rotate to control whether the preview stream component XComponent is mirrored
        XComponent({
          type: XComponentType.SURFACE,
          controller: this.mXComponentController,
          imageAIOptions: {
            types: \[ImageAnalyzerType.SUBJECT\],
            aiController: this.aiController
          }
        })
          .onLoad(() => {
            // The aspect ratio of the preview stream must match that of the recording output stream
            this.mXComponentController.setXComponentSurfaceRect({
              surfaceWidth: this.videoSize.width,
              surfaceHeight: this.videoSize.height
            });
            this.surfaceId = this.mXComponentController.getXComponentSurfaceId()
          })
          .width(StyleConstants.FULL\_WIDTH)
          .height(StyleConstants.XCOMPONENT\_HEIGHT)
          .rotate({ y: 1, angle: this.angle, })
        
    2.  Use the FFmpeg third-party library to mirror the recording file content. Before mirroring, you need to install the FFmpeg third-party library. For details, see [FFmpeg](https://ohpm.openharmony.cn/#/en/detail/@sj%2Fffmpeg) official website. The code for mirroring is as follows:
        
        import { FFProgressMessageParser, FFmpeg } from '@sj/ffmpeg';
        
        let commands = \["ffmpeg", "-i", inputPath, "-vf", "hflip", outputPath\];
        FFmpeg.execute(commands, {
          logCallback: (logLevel: number, logMessage: string) => console.log(\`\[${logLevel}\]${logMessage}\`),
          progressCallback: (message: string) =>  console.log(\`\[progress\]${JSON.stringify(FFProgressMessageParser.parse(message))}\`),
        }).then(() => {
          console.info("FFmpeg execution succeeded.");
        }).catch((error: Error) => {
          console.error("FFmpeg execution failed with error: ${error.message}");
        });
