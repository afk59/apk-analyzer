# How do I compress videos?

**Symptom**

Video compression is one of the typical scenarios in audio and video entertainment applications. For example, when there are size limits for uploading, sending, or saving videos, it is necessary to compress the video to ensure that its quality and size meet user needs.

**Solution**

**Solution 1**

1.  You can use the video compression feature of the third-party library videocompressor to compress videos. The procedure is as follows:
    
    static async selectVideo(selectNumber: number): Promise<photoAccessHelper.PhotoSelectResult> {
      let photoSelectOptions = new photoAccessHelper.PhotoSelectOptions();
      // Set the media file type that can be selected.
      photoSelectOptions.MIMEType = photoAccessHelper.PhotoViewMIMETypes.VIDEO\_TYPE;
      // Set the maximum number of files that can be selected.
      photoSelectOptions.maxSelectNumber = selectNumber;
      let photoPicker = new photoAccessHelper.PhotoViewPicker();
      // The select method of PhotoViewPicker can read images or videos without special permissions.
      return await photoPicker.select(photoSelectOptions);
    }
    
    // Obtain the video path.
    async selectAndCompressVideo() {
      let selectResult: photoAccessHelper.PhotoSelectResult = await PictureUtils.selectVideo(1);
      // Obtain the URI of the selected video.
      this.videoPath = selectResult.photoUris\[0\];
      hilog.info(0x0000, TAG, 'videoCompressor select selectFilePath:' + this.videoPath)
    }
    
2.  Call the **compressVideo** method and specify the compression quality.
    
    compressVideo(quality: CompressQuality, qualityTag: string) {
      this.quantity = qualityTag;
      let videoCompressor = new VideoCompressor();
      // Call the compressVideo method and specify the compression quality.
      videoCompressor.compressVideo(this.uiContext.getHostContext()!, this.videoPath, quality)
        .then((data) => {
          if (data.code == CompressorResponseCode.SUCCESS) {
            hilog.info(0x0000, TAG,
              'videoCompressor ' + qualityTag + ' message:' + data.message + '--outputPath:' + data.outputPath);
            // Obtain the compressed video file located in the application sandbox path and click the save button to save the file to the album.
            this.buffer = PictureUtils.compressVideo(data.outputPath);
            hilog.info(0x0000, TAG, \`The buffer: ${JSON.stringify(this.buffer)}\`);
            this.uiContext.showAlertDialog({ message: 'Compressed. You can download it!' });
          } else {
            hilog.info(0x0000, TAG,
              'videoCompressor ' + qualityTag + ' code:' + data.code + '--error message:' + data.message);
          }
        }).catch((err: Error) => {
        hilog.info(0x0000, TAG, 'videoCompressor ' + qualityTag + ' get error message' + err.message);
      })
    }
    
3.  After compression is completed, the video is saved to the sandbox.
    
    try {
      let parentDir = this.uiContext.getHostContext()!.filesDir;
      let fileName: string = Date.now() + '-' + this.quantity + '.mp4';
      this.fileDir = parentDir + '/' + fileName;
      let file = await fs.open(this.fileDir, fs.OpenMode.READ\_WRITE | fs.OpenMode.CREATE);
      // Write to file.
      await fs.write(file.fd, this.buffer);
      this.compressedSize = (await fs.stat(file.fd)).size;
      // Close the file.
      await fs.close(file.fd);
      this.uiContext.showAlertDialog({ message: 'Saved successfully!' });
    } catch (error) {
      hilog.error(0x0000, TAG, 'error is' + JSON.stringify(error));
      this.uiContext.showAlertDialog({ message: 'Failed to save!' });
    }
    

**Solution 2**

Use the video encoding feature of AVCodec Kit to transmit uncompressed video data to the video encoder for encoding. By setting the required parameters such as encoding format, bit rate, and frame rate, and controlling the encoding output, the purpose of compressing video files is achieved. For the range of encoder parameter configurations, see [Obtaining Supported Codecs](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/obtain-supported-codecs)

int32\_t VideoEncoder::Configure(const SampleInfo &sampleInfo) {
    OH\_AVFormat \*format = OH\_AVFormat\_Create();
    CHECK\_AND\_RETURN\_RET\_LOG(format != nullptr, AVCODEC\_SAMPLE\_ERR\_ERROR, "AVFormat create failed");

    OH\_AVFormat\_SetIntValue(format, OH\_MD\_KEY\_WIDTH, sampleInfo.videoWidth);
    OH\_AVFormat\_SetIntValue(format, OH\_MD\_KEY\_HEIGHT, sampleInfo.videoHeight);
    OH\_AVFormat\_SetDoubleValue(format, OH\_MD\_KEY\_FRAME\_RATE, sampleInfo.frameRate);
    OH\_AVFormat\_SetIntValue(format, OH\_MD\_KEY\_PIXEL\_FORMAT, sampleInfo.pixelFormat);
    OH\_AVFormat\_SetIntValue(format, OH\_MD\_KEY\_VIDEO\_ENCODE\_BITRATE\_MODE, sampleInfo.bitrateMode);
    OH\_AVFormat\_SetLongValue(format, OH\_MD\_KEY\_BITRATE, sampleInfo.bitrate);
    OH\_AVFormat\_SetIntValue(format, OH\_MD\_KEY\_PROFILE, sampleInfo.hevcProfile);
    // Setting HDRVivid-related parameters
    if (sampleInfo.isHDRVivid) {
        OH\_AVFormat\_SetIntValue(format, OH\_MD\_KEY\_I\_FRAME\_INTERVAL, sampleInfo.iFrameInterval);
        OH\_AVFormat\_SetIntValue(format, OH\_MD\_KEY\_RANGE\_FLAG, sampleInfo.rangFlag);
        OH\_AVFormat\_SetIntValue(format, OH\_MD\_KEY\_COLOR\_PRIMARIES, sampleInfo.primary);
        OH\_AVFormat\_SetIntValue(format, OH\_MD\_KEY\_TRANSFER\_CHARACTERISTICS, sampleInfo.transfer);
        OH\_AVFormat\_SetIntValue(format, OH\_MD\_KEY\_MATRIX\_COEFFICIENTS, sampleInfo.matrix);
    }
    // ...

    // Setting the Encoder
    int ret = OH\_VideoEncoder\_Configure(encoder\_, format);
    OH\_AVFormat\_Destroy(format);
    format = nullptr;
    CHECK\_AND\_RETURN\_RET\_LOG(ret == AV\_ERR\_OK, AVCODEC\_SAMPLE\_ERR\_ERROR, "Config failed, ret: %{public}d", ret);
    return AVCODEC\_SAMPLE\_ERR\_OK;
}

Sample code: [AVCodec Based Video Codec](https://gitcode.com/HarmonyOS_Samples/AVCodecVideo).

**Solution 3**

For scenarios during video recording, you can use **AVRecorder** to set up a video recording output stream and adjust custom parameters, thereby adjusting the bit rate and resolution of the video file and effectively managing the size of the video file.

let videoProfilesArray: Array<camera.VideoProfile> = cameraOutputCap.videoProfiles;
if (!videoProfilesArray) {
  Logger.error(TAG, 'createOutput videoProfilesArray === null || undefined');
}
// ...

let aVRecorderProfile: media.AVRecorderProfile = {
  // ...
  fileFormat: media.ContainerFormatType.CFT\_MPEG\_4,
  videoBitrate: 2000000,
  videoCodec: media.CodecMimeType.VIDEO\_AVC,
  videoFrameWidth: videoSize.width,
  videoFrameHeight: videoSize.height,
  videoFrameRate: 30
};

let aVRecorderConfig: media.AVRecorderConfig = {
  // ...
  videoSourceType: media.VideoSourceType.VIDEO\_SOURCE\_TYPE\_SURFACE\_YUV,
  profile: aVRecorderProfile,
  url: this.url,
  rotation: 90,
  // ...
};

Sample code: [CameraKit Based Video Recording Using AVRecorder](https://gitcode.com/harmonyos_samples/camera-kit-avrecorder).

**Solution 4**

ArkTS provides the **AVTranscoder** API for video transcoding. The bit rate and resolution of a video are key factors that affect the video quality and file size. The **AVTranscoder** can be used to transcode videos to save video storage space and improve device compatibility of video files.

For details about how to use the **AVTranscoder** and FAQs, see [Using AVTranscoder to Transcode Videos](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/using-avtranscoder-for-transcodering).
