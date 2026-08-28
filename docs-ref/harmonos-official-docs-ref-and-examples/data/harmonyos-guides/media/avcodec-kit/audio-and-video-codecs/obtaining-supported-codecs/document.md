# Obtaining Supported Codecs

Due to differences in sources, codec protocols, and device capabilities, the available codecs and their capabilities vary across different devices.

To ensure that codec behavior meets expectations, use the audio and video codec capability interface to query the codecs supported by the system and their capabilities, select codecs that align with your development requirements, and configure parameters correctly.

#### General Development

1.  Link the dynamic libraries in the CMake script.
    
    target\_link\_libraries(sample PUBLIC libnative\_media\_codecbase.so)
    target\_link\_libraries(sample PUBLIC libnative\_media\_core.so)
    target\_link\_libraries(sample PUBLIC libnative\_media\_venc.so)
    target\_link\_libraries(sample PUBLIC libnative\_media\_vdec.so)
    target\_link\_libraries(sample PUBLIC libnative\_media\_acodec.so)
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e1/v3/OQGruAaYRJiRBP7teLrAsA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062035Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=4DF3D2AD286E8C2D64A1C1F7EE2139B525B2D9FF5242767D00E1C187D3F61A85)
    
    The word **sample** in the preceding code snippet is only an example. Use the actual project directory name.
    
2.  Add the header files.
    
    #include <algorithm>
    #include <multimedia/player\_framework/native\_avcapability.h>
    #include <multimedia/player\_framework/native\_avcodec\_audiocodec.h>
    #include <multimedia/player\_framework/native\_avcodec\_videoencoder.h>
    #include <multimedia/player\_framework/native\_avcodec\_videodecoder.h>
    
3.  Obtain an audio/video codec capability instance.
    
    You can use either of the following methods to obtain the instance:
    
    Method 1: Call **OH\_AVCodec\_GetCapability** to obtain the codec capability instance recommended by the system. The recommendation policy is the same as that of the **OH\_XXX\_CreateByMime** series APIs.
    
    // Obtain the AAC decoder capability instance recommended by the system.
    OH\_AVCapability \*capability = OH\_AVCodec\_GetCapability(OH\_AVCODEC\_MIMETYPE\_AUDIO\_AAC, false);
    
    Method 2: Call **OH\_AVCodec\_GetCapabilityByCategory** to obtain the codec capability instance for the specified software or hardware.
    
    // Obtain the AVC encoder capability instance for the specified hardware.
    OH\_AVCapability \*capability = OH\_AVCodec\_GetCapabilityByCategory(OH\_AVCODEC\_MIMETYPE\_VIDEO\_AVC, true, HARDWARE);
    
    After obtaining the codec capability instance, you can move on to the next steps. There is no need to manually release the instance. The system automatically reclaims the instance when it is no longer needed.
    
4.  Call the query APIs as required. For details, see [AudioCodec](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-native-avcapability-h).
    

#### Scenario-based Development

This section provides examples to illustrate the use of capability query interfaces in specific scenarios that may be encountered during development.

## Creating a Codec with the Specified Name

If there are multiple codecs of the same MIME type, use the **OH\_XXX\_CreateByMime** series APIs to create the system-recommended codec. To create other codecs, you must first obtain their name and then call **OH\_XXX\_CreateByName** series APIs to create the codec with the specified name.

| API | Description |
| :-- | :-- |
| OH\_AVCapability\_GetName | Obtains the name of a codec corresponding to a capability instance. |

The following is an example of creating an H.264 software decoder when both the H.264 software decoder and H.264 hardware decoder exist:

// 1. Obtain an H.264 software decoder capability instance.
OH\_AVCapability \*capability = OH\_AVCodec\_GetCapabilityByCategory(OH\_AVCODEC\_MIMETYPE\_VIDEO\_AVC, false, SOFTWARE);
if (capability != nullptr) {
   // 2. Obtain the name of the H.264 software decoder.
   const char \*codecName = OH\_AVCapability\_GetName(capability);
   // 3. Create an H.264 software decoder instance.
   OH\_AVCodec \*videoDec = OH\_VideoDecoder\_CreateByName(codecName);
}

## Setting Codec Parameters by Software or Hardware

The definitions of software codecs and hardware codecs are as follows:

-   **Software codec**: a codec that runs on the CPU, featuring flexible iteration, good compatibility, and strong expandability.
    
-   **Hardware codec**: a codec that runs on dedicated hardware, featuring low-power consumption, high performance, and reduced CPU load.
    

When hardware codecs are sufficient and meet capability requirements, prioritize their use; otherwise, use software codecs. You can configure different codec parameters based on the codec category.

| API | Description |
| :-- | :-- |
| OH\_AVCapability\_IsHardware | Checks whether a codec capability instance describes a hardware codec. |

The following is an example of differentiated frame rate configuration for video encoding based on hardware/software categories.

// 1. Check whether the recommended H.264 encoder is a hardware codec.
OH\_AVCapability \*capability = OH\_AVCodec\_GetCapability(OH\_AVCODEC\_MIMETYPE\_VIDEO\_AVC, true);
if (capability == nullptr) {
   // Handle exceptions.
}
bool isHardware = OH\_AVCapability\_IsHardware(capability);
// 2. Carry out differentiated configuration based on the software or hardware type.
OH\_AVCodec \*videoEnc = OH\_VideoEncoder\_CreateByMime(OH\_AVCODEC\_MIMETYPE\_VIDEO\_AVC);
if (videoEnc == nullptr) {
   // Handle exceptions.
}
OH\_AVFormat \*format = OH\_AVFormat\_CreateVideoFormat(OH\_AVCODEC\_MIMETYPE\_VIDEO\_AVC, 1920, 1080);
if (format == nullptr) {
   // Handle exceptions.
}
double frameRate = isHardware ? 60.0 : 30.0;
if (!OH\_AVFormat\_SetDoubleValue(format, OH\_MD\_KEY\_FRAME\_RATE, frameRate)) {
   // Handle exceptions.
}
if (OH\_VideoEncoder\_Configure(videoEnc, format) != AV\_ERR\_OK) {
   // Handle exceptions.
}
OH\_AVFormat\_Destroy(format);

## Creating a Multi-Channel Codec

Multiple codecs are required in certain scenarios. However, the number of codec instances that can be created is limited due to constraints on system resources such as memory, processor, and bandwidth.

| API | Description |
| :-- | :-- |
| OH\_AVCapability\_GetMaxSupportedInstances | Obtains the maximum number of codec instances corresponding to the capability instance. The actual number of codec instances created is also constrained by system resources like memory, processor, and bandwidth. |

Prioritize creating hardware decoder instances; if resources are insufficient, create software decoder instances. An example is as follows:

constexpr int32\_t NEEDED\_VDEC\_NUM = 8;
// 1. Create hardware decoder instances.
OH\_AVCapability \*capHW = OH\_AVCodec\_GetCapabilityByCategory(OH\_AVCODEC\_MIMETYPE\_VIDEO\_AVC, false, HARDWARE);
if (capHW == nullptr) {
   // Handle exceptions.
}
int32\_t vDecNumHW = std::min(OH\_AVCapability\_GetMaxSupportedInstances(capHW), NEEDED\_VDEC\_NUM);
int32\_t createdVDecNum = 0;
for (int i = 0; i < vDecNumHW; i++) {
   OH\_AVCodec \*videoDec = OH\_VideoDecoder\_CreateByName(OH\_AVCapability\_GetName(capHW));
   if (videoDec != nullptr) {
      // Maintained in videoDecVector.
      createdVDecNum++;
   }
}
if (createdVDecNum < NEEDED\_VDEC\_NUM) {
   // 2. If the hardware decoder instances cannot fully meet the project requirements, create software decoder instances.
   OH\_AVCapability \*capSW = OH\_AVCodec\_GetCapabilityByCategory(OH\_AVCODEC\_MIMETYPE\_VIDEO\_AVC, false, SOFTWARE);
   if (capSW == nullptr) {
      // Handle exceptions.
   }
   int32\_t vDecNumSW = std::min(OH\_AVCapability\_GetMaxSupportedInstances(capSW), NEEDED\_VDEC\_NUM - createdVDecNum);
   for (int i = 0; i < vDecNumSW; i++) {
      OH\_AVCodec \*videoDec = OH\_VideoDecoder\_CreateByName(OH\_AVCapability\_GetName(capSW));
      if (videoDec != nullptr) {
         // Maintained in videoDecVector.
         createdVDecNum++;
      }
   }
}

## Controlling the Encoding Quality

Four bit rate modes are available: Constant Bit Rate (CBR), Dynamic Bit Rate (VBR), Constant Quality (CQ), and Stable Quality (SQR).

-   For CBR and VBR, the encoding quality is determined by the bit rate parameters.
-   For CQ, the encoding quality is determined by the quality parameters.
-   For SQR, the encoding quality is determined by the SQR factor and the maximum bit rate. Currently, only H.265 (HEVC) encoding is supported.

| API | Description |
| :-- | :-- |
| OH\_AVCapability\_IsEncoderBitrateModeSupported | Checks whether an encoder supports the specified bit rate mode. |
| OH\_AVCapability\_GetEncoderBitrateRange | Obtains the bit rate range supported by an encoder. It applies to CBR, VBR, and SQR modes. |
| OH\_AVCapability\_GetEncoderQualityRange | Obtains the quality range supported by an encoder. It applies to CQ mode. |

The code snippet below shows the configuration in CBR or VBR mode.

OH\_BitrateMode bitrateMode = BITRATE\_MODE\_CBR;
int32\_t bitrate = 3000000;
OH\_AVCapability \*capability = OH\_AVCodec\_GetCapability(OH\_AVCODEC\_MIMETYPE\_VIDEO\_AVC, true);
if (capability == nullptr) {
   // Handle exceptions.
}
// 1. Check whether a bit rate mode is supported.
bool isSupported = OH\_AVCapability\_IsEncoderBitrateModeSupported(capability, bitrateMode);
if (!isSupported) {
   // Handle exceptions.
}
// 2. Obtain the bit rate range and check whether the bit rate to be configured is within the range.
OH\_AVRange bitrateRange = {-1, -1};
int32\_t ret = OH\_AVCapability\_GetEncoderBitrateRange(capability, &bitrateRange);
if (ret != AV\_ERR\_OK || bitrateRange.maxVal <= 0) {
   // Handle exceptions.
}
if (bitrate > bitrateRange.maxVal || bitrate < bitrateRange.minVal) {
   // 3. (Optional) Adjust the bit rate parameters to be configured.
}
// 4. Set the encoding parameters.
OH\_AVCodec \*videoEnc = OH\_VideoEncoder\_CreateByMime(OH\_AVCODEC\_MIMETYPE\_VIDEO\_AVC);
if (videoEnc == nullptr) {
   // Handle exceptions.
}
OH\_AVFormat \*format = OH\_AVFormat\_CreateVideoFormat(OH\_AVCODEC\_MIMETYPE\_VIDEO\_AVC, 1920, 1080);
if (format == nullptr) {
   // Handle exceptions.
}
if (!OH\_AVFormat\_SetIntValue(format, OH\_MD\_KEY\_VIDEO\_ENCODE\_BITRATE\_MODE, bitrateMode) ||
   !OH\_AVFormat\_SetLongValue(format, OH\_MD\_KEY\_BITRATE, static\_cast<int64\_t>(bitrate))) {
   // Handle exceptions.
}
if (OH\_VideoEncoder\_Configure(videoEnc, format) != AV\_ERR\_OK) {
   // Handle exceptions.
}
OH\_AVFormat\_Destroy(format);

The code snippet below shows the configuration in CQ mode.

OH\_BitrateMode bitrateMode = BITRATE\_MODE\_CQ;
int32\_t quality = 0;
OH\_AVCapability \*capability = OH\_AVCodec\_GetCapability(OH\_AVCODEC\_MIMETYPE\_VIDEO\_AVC, true);
if (capability == nullptr) {
   // Handle exceptions.
}
// 1. Check whether a bit rate mode is supported.
bool isSupported = OH\_AVCapability\_IsEncoderBitrateModeSupported(capability, bitrateMode);
if (!isSupported) {
   // Handle exceptions.
}
// 2. Obtain the quality range and determine whether the quality parameters to be configured are within the range.
OH\_AVRange qualityRange = {-1, -1};
int32\_t ret = OH\_AVCapability\_GetEncoderQualityRange(capability, &qualityRange);
if (ret != AV\_ERR\_OK || qualityRange.maxVal < 0) {
   // Handle exceptions.
}
if (quality > qualityRange.maxVal || quality < qualityRange.minVal) {
   // 3. (Optional) Adjust the quality parameters to be configured.
}
// 4. Set the encoding parameters.
OH\_AVCodec \*videoEnc = OH\_VideoEncoder\_CreateByMime(OH\_AVCODEC\_MIMETYPE\_VIDEO\_AVC);
if (videoEnc == nullptr) {
   // Handle exceptions.
}
OH\_AVFormat \*format = OH\_AVFormat\_CreateVideoFormat(OH\_AVCODEC\_MIMETYPE\_VIDEO\_AVC, 1920, 1080);
if (format == nullptr) {
   // Handle exceptions.
}
if (!OH\_AVFormat\_SetIntValue(format, OH\_MD\_KEY\_VIDEO\_ENCODE\_BITRATE\_MODE, bitrateMode) ||
   !OH\_AVFormat\_SetIntValue(format, OH\_MD\_KEY\_QUALITY, quality)) {
   // Handle exceptions.
}
if (OH\_VideoEncoder\_Configure(videoEnc, format) != AV\_ERR\_OK) {
   // Handle exceptions.
}
OH\_AVFormat\_Destroy(format);

The code snippet below shows the configuration in SQR mode.

OH\_BitrateMode bitrateMode = BITRATE\_MODE\_SQR;
int32\_t sqrFactor = 30; // SQR factor.
int32\_t maxBitrate = 20000000; // Maximum bit rate.
OH\_AVCapability \*capability = OH\_AVCodec\_GetCapability(OH\_AVCODEC\_MIMETYPE\_VIDEO\_HEVC, true);
if (capability == nullptr) {
   // Handle exceptions.
}
// 1. Check whether a bit rate mode is supported.
bool isSupported = OH\_AVCapability\_IsEncoderBitrateModeSupported(capability, bitrateMode);
if (!isSupported) {
   // Handle exceptions.
}
// 2. Obtain the bit rate range and check whether the maximum bit rate to be configured is within the range.
OH\_AVRange bitrateRange = {-1, -1};
// The value range of the maximum bit rate is the same as that of the bit rate. Therefore, OH\_AVCapability\_GetEncoderBitrateRange is reused to obtain the value range.
int32\_t ret = OH\_AVCapability\_GetEncoderBitrateRange(capability, &bitrateRange);
if (ret != AV\_ERR\_OK || bitrateRange.maxVal <= 0) {
   // Handle exceptions.
}

// The value range of the SQR factor is \[0, 51\] (same as the QP).
if (sqrFactor > 51 || sqrFactor < 0) {
   // 3. (Optional) Adjust the SQR factor to be configured.
}

if (maxBitrate > bitrateRange.maxVal || maxBitrate < bitrateRange.minVal) {
   // 4. (Optional) Adjust the maximum bit rate parameters to be configured.
}

// 5. Set the encoding parameters.
OH\_AVCodec \*videoEnc = OH\_VideoEncoder\_CreateByMime(OH\_AVCODEC\_MIMETYPE\_VIDEO\_HEVC);
if (videoEnc == nullptr) {
   // Handle exceptions.
}
OH\_AVFormat \*format = OH\_AVFormat\_CreateVideoFormat(OH\_AVCODEC\_MIMETYPE\_VIDEO\_HEVC, 1920, 1080);
if (format == nullptr) {
   // Handle exceptions.
}
if (!OH\_AVFormat\_SetIntValue(format, OH\_MD\_KEY\_VIDEO\_ENCODE\_BITRATE\_MODE, bitrateMode) ||
   !OH\_AVFormat\_SetIntValue(format, OH\_MD\_KEY\_SQR\_FACTOR, sqrFactor) ||
   !OH\_AVFormat\_SetIntValue(format, OH\_MD\_KEY\_MAX\_BITRATE, maxBitrate)) {
   // Handle exceptions.
}
if (OH\_VideoEncoder\_Configure(videoEnc, format) != AV\_ERR\_OK) {
   // Handle exceptions.
}
OH\_AVFormat\_Destroy(format);

// 6. Start the encoder.
ret = OH\_VideoEncoder\_Prepare(videoEnc);
if (ret != AV\_ERR\_OK) {
   // Handle exceptions.
}
ret = OH\_VideoEncoder\_Start(videoEnc);
if (ret != AV\_ERR\_OK) {
   // Handle exceptions.
}

// 7. (Optional) Use OH\_VideoEncoder\_SetParameter() to dynamically configure the SQR factor and maximum bit rate during the running.
OH\_AVFormat \*dynamicFormat = OH\_AVFormat\_Create();
// SQR supports dynamic configuration of the maximum bit rate and SQR factor.
sqrFactor = 25; // Update the SQR factor.
maxBitrate = 10000000; // Update the maximum bit rate.
OH\_AVFormat\_SetLongValue(dynamicFormat, OH\_MD\_KEY\_MAX\_BITRATE, maxBitrate);
OH\_AVFormat\_SetIntValue(dynamicFormat, OH\_MD\_KEY\_SQR\_FACTOR, sqrFactor);
ret = OH\_VideoEncoder\_SetParameter(videoEnc, dynamicFormat);
if (ret != AV\_ERR\_OK) {
   // Handle exceptions.
}
OH\_AVFormat\_Destroy(dynamicFormat);

## Checking the Complexity Range Supported

The complexity range determines the number of tools used by the encoder. However, not all encoders support this feature.

| API | Description |
| :-- | :-- |
| OH\_AVCapability\_GetEncoderComplexityRange | Obtains the complexity range supported by an encoder. |

OH\_AVCapability \*capability = OH\_AVCodec\_GetCapability(OH\_AVCODEC\_MIMETYPE\_AUDIO\_AAC, true);
if (capability == nullptr) {
   // Handle exceptions.
}
// Check the supported encoding complexity range.
OH\_AVRange complexityRange = {-1, -1};
int32\_t ret = OH\_AVCapability\_GetEncoderComplexityRange(capability, &complexityRange);

## Setting Correct Audio Codec Parameters

In audio encoding and decoding scenarios, you need to set the sample rate and number of channels. For audio encoding, you also need to set the bit rate.

| API | Description |
| :-- | :-- |
| OH\_AVCapability\_GetAudioSupportedSampleRateRanges | Obtains the sample rates supported by an audio codec. |
| OH\_AVCapability\_GetAudioChannelCountRange | Obtains the count range of channels supported by an audio codec. |
| OH\_AVCapability\_GetEncoderBitrateRange | Obtains the bit rate range supported by an encoder. |

The following is an example of querying audio codec parameters:

int32\_t sampleRate = 44100;
int32\_t channelCount = 2;
int32\_t bitrate = 261000;
OH\_AVCapability \*capability = OH\_AVCodec\_GetCapability(OH\_AVCODEC\_MIMETYPE\_AUDIO\_AAC, true);
if (capability == nullptr) {
   // Handle exceptions.
}
// 1. Check whether the sample rate to be configured is supported.
OH\_AVRange \*sampleRateRanges = nullptr;
uint32\_t rangesNum = 0;
int32\_t ret = OH\_AVCapability\_GetAudioSupportedSampleRateRanges(capability, &sampleRateRanges, &rangesNum);
if (ret != AV\_ERR\_OK || sampleRateRanges == nullptr || rangesNum == 0) {
   // Handle exceptions.
}
bool isMatched = false;
for (uint32\_t i = 0; i < rangesNum; i++) {
   if (sampleRate >= sampleRateRanges\[i\].minVal && sampleRate <= sampleRateRanges\[i\].maxVal) {
      isMatched = true;
      break;
   }
}
if (!isMatched) {
   // 2. (Optional) Adjust the sample rate to be configured.
}
// 3. Obtain the count range of channels and check whether the number of channels to be configured is within the range.
OH\_AVRange channelRange = {-1, -1};
ret = OH\_AVCapability\_GetAudioChannelCountRange(capability, &channelRange);
if (ret != AV\_ERR\_OK || channelRange.maxVal <= 0) {
   // Handle exceptions.
}
if (channelCount > channelRange.maxVal || channelCount < channelRange.minVal ) {
   //4. (Optional) Adjust the number of channels to be configured.
}
// 5. Obtain the bit rate range and check whether the bit rate to be configured is within the range.
OH\_AVRange bitrateRange = {-1, -1};
ret = OH\_AVCapability\_GetEncoderBitrateRange(capability, &bitrateRange);
if (ret != AV\_ERR\_OK || bitrateRange.maxVal <= 0) {
   // Handle exceptions.
}
if (bitrate > bitrateRange.maxVal || bitrate < bitrateRange.minVal ) {
   // 6. (Optional) Adjust the bit rate to be configured.
}
// 7. Set the encoding parameters.
OH\_AVCodec \*audioEnc = OH\_AudioCodec\_CreateByMime(OH\_AVCODEC\_MIMETYPE\_AUDIO\_AAC, true);
if (audioEnc == nullptr) {
   // Handle exceptions.
}
OH\_AVFormat \*format = OH\_AVFormat\_Create();
if (format == nullptr) {
   // Handle exceptions.
}
if (!OH\_AVFormat\_SetIntValue(format, OH\_MD\_KEY\_AUD\_SAMPLE\_RATE, sampleRate) ||
   !OH\_AVFormat\_SetIntValue(format, OH\_MD\_KEY\_AUD\_CHANNEL\_COUNT, channelCount) ||
   !OH\_AVFormat\_SetLongValue(format, OH\_MD\_KEY\_BITRATE, static\_cast<int64\_t>(bitrate))) {
   // Handle exceptions.
}
if (OH\_AudioCodec\_Configure(audioEnc, format) != AV\_ERR\_OK) {
   // Handle exceptions.
}
OH\_AVFormat\_Destroy(format);

## Checking the Codec Profile and Level Supported

The codec standard contains multiple encoding tools, which are applicable to different encoding scenarios. Codec standards include multiple encoding tools, which are applicable to different encoding scenarios. For specific scenarios, the codec standard uses the codec profile to specify the enabled status of these encoding tools. For example, for H.264, there are baseline, main, and high profiles. For details, see [OH\_AVCProfile](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-native-avcodec-base-h#oh_avcprofile).

Codec levels define the processing capability and storage space required by the codec. For example, for H.264, there are 20 levels ranging from 1 to 6.2. For details, see [OH\_AVCLevel](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-native-avcodec-base-h#oh_avclevel).

| API | Description |
| :-- | :-- |
| OH\_AVCapability\_GetSupportedProfiles | Obtains the profiles supported by a codec. |
| OH\_AVCapability\_GetSupportedLevelsForProfile | Obtains the codec levels supported by a profile. |
| OH\_AVCapability\_AreProfileAndLevelSupported | Checks whether a codec supports the combination of a profile and level. |

The code snippet below checks whether a profile is supported and obtains the supported levels.

OH\_AVCProfile profile = AVC\_PROFILE\_MAIN;
OH\_AVCapability \*capability = OH\_AVCodec\_GetCapability(OH\_AVCODEC\_MIMETYPE\_VIDEO\_AVC, true);
if (capability == nullptr) {
   // Handle exceptions.
}
// 1. Check whether the profile to be configured is supported.
const int32\_t \*profiles = nullptr;
uint32\_t profileNum = 0;
int32\_t ret = OH\_AVCapability\_GetSupportedProfiles(capability, &profiles, &profileNum);
if (ret != AV\_ERR\_OK || profiles == nullptr || profileNum == 0) {
   // Handle exceptions.
}
bool isMatched = false;
for (int i = 0; i < profileNum; i++) {
   if (profiles\[i\] == profile) {
      isMatched = true;
      break;
   }
}
// 2. Obtain the codec levels supported by the profile.
const int32\_t \*levels = nullptr;
uint32\_t levelNum = 0;
ret = OH\_AVCapability\_GetSupportedLevelsForProfile(capability, profile, &levels, &levelNum);
if (ret != AV\_ERR\_OK || levels == nullptr || levelNum == 0) {
   // Handle exceptions.
}
OH\_AVCLevel maxLevel = static\_cast<OH\_AVCLevel>(levels\[0\]);
for (int32\_t i = 1; i < levelNum; i++) {
   OH\_AVCLevel tmp = static\_cast<OH\_AVCLevel>(levels\[i\]);
   if (tmp > maxLevel) {
      maxLevel = tmp;
   }
}
// 3. (Optional) Use different service logic based on the maximum level supported.
if (maxLevel >= AVC\_LEVEL\_51) {
   // For levels above 5.1, the width and height can be configured to 3840\*2160.
} else if (maxLevel >= AVC\_LEVEL\_4) {
   // For levels above 4.0, the width and height can be configured to 1920\*1080.
} else if (maxLevel >= AVC\_LEVEL\_31) {
   // For levels above 3.1, the width and height can be configured to 1280\*720.
} else {
   // An error is reported and no encoding is performed.
}
// 4. Set the profile parameters.
OH\_AVCodec \*videoEnc = OH\_VideoEncoder\_CreateByMime(OH\_AVCODEC\_MIMETYPE\_VIDEO\_AVC);
if (videoEnc == nullptr) {
   // Handle exceptions.
}
OH\_AVFormat \*format = OH\_AVFormat\_CreateVideoFormat(OH\_AVCODEC\_MIMETYPE\_VIDEO\_AVC, 1920, 1080);
if (format == nullptr) {
   // Handle exceptions.
}
if (!OH\_AVFormat\_SetIntValue(format, OH\_MD\_KEY\_PROFILE, profile)) {
   // Handle exceptions.
}
if (OH\_VideoEncoder\_Configure(videoEnc, format) != AV\_ERR\_OK) {
   // Handle exceptions.
}
OH\_AVFormat\_Destroy(format);

If you already know the required profile and level combination, use the code snippet below to check whether the combination is supported.

// 1. Obtain an H.264 encoder capability instance.
OH\_AVCapability \*capability = OH\_AVCodec\_GetCapability(OH\_AVCODEC\_MIMETYPE\_VIDEO\_AVC, true);
if (capability == nullptr) {
   // Handle exceptions.
}
// 2. Check whether the combination of the profile and level is supported.
bool isSupported = OH\_AVCapability\_AreProfileAndLevelSupported(capability, AVC\_PROFILE\_MAIN, AVC\_LEVEL\_51);

## Setting the Correct Video Width and Height

Video codecs have alignment constraints on width and height. For example, mainstream codecs use YUV420 series as the default codec pixel format, where UV components are downsampled to half the original size in both width and height directions. Therefore, the width and height of video codecs must be aligned to at least 2. Other factors may also lead to more strict alignment constraints.

The width and height of video codecs are not only limited by frame-level codec capabilities but also by protocol-level constraints on frame-level capabilities. Taking H.264 as an example, AVC\_LEVEL\_51 limits the maximum number of macroblocks per frame to 36864.

The formula for calculating the maximum video width based on the video height is as follows:

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0a/v3/QewMnCNdSy2juMIbwcLWRA/en-us_image_0000002568684875.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062035Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=3D83198164E696E830C1CB441D8681D4FACD74C715219F3947EEE9ACD3F8AA2B)

**MaxMBsPerFrameLevelLimits** refers to the maximum number of macroblocks per frame of the codec limited by the protocol, and **MaxMBsPerFrameSubmit** refers to the maximum number of macroblocks per frame reported by the codec. The actual capability is the minimum of the two.

| API | Description |
| :-- | :-- |
| OH\_AVCapability\_GetVideoWidthAlignment | Obtains the video width alignment supported by a video codec. |
| OH\_AVCapability\_GetVideoHeightAlignment | Obtains the video height alignment supported by a video codec. |
| OH\_AVCapability\_GetVideoWidthRange | Obtains the video width range supported by a video codec. |
| OH\_AVCapability\_GetVideoHeightRange | Obtains the video height range supported by a video codec. |
| OH\_AVCapability\_GetVideoWidthRangeForHeight | Obtains the video width range of a video codec based on a given height. |
| OH\_AVCapability\_GetVideoHeightRangeForWidth | Obtains the video height range of a video codec based on a given width. |
| OH\_AVCapability\_IsVideoSizeSupported | Checks whether a video codec supports the combination of a given width and height. |

The following example shows how to check whether the video height and width are supported:

int32\_t width = 1920;
int32\_t height = 1080;
OH\_AVCapability \*capability = OH\_AVCodec\_GetCapability(OH\_AVCODEC\_MIMETYPE\_VIDEO\_AVC, true);
if (capability == nullptr) {
   // Handle exceptions.
}
// 1. Check whether the video width and height are supported.
bool isSupported = OH\_AVCapability\_IsVideoSizeSupported(capability, width, height);
if (!isSupported) {
   // 2. (Optional) Query detailed restrictions based on the video height and width and adjust the video height and width to use.
}

If the verification of video height and width fails or the configuration fails, you can try the following methods to determine the correct video width and height range.

If the video width is known, you can find the correct size configuration as shown in the following example:

int32\_t width = 1920;
OH\_AVCapability \*capability = OH\_AVCodec\_GetCapability(OH\_AVCODEC\_MIMETYPE\_VIDEO\_AVC, true);
if (capability == nullptr) {
   // Handle exceptions.
}
// 1. Check whether the video width meets the width alignment requirements.
int32\_t widthAlignment = 0;
int32\_t ret = OH\_AVCapability\_GetVideoWidthAlignment(capability, &widthAlignment);
if (ret != AV\_ERR\_OK || widthAlignment <= 0) {
   // Handle exceptions.
} else if (width % widthAlignment != 0) {
   // 2. (Optional) Align the video width.
   width = (width + widthAlignment - 1) / widthAlignment \* widthAlignment;
}
// 3. Check whether the video width is within the supported range.
OH\_AVRange widthRange = {-1, -1};
ret = OH\_AVCapability\_GetVideoWidthRange(capability, &widthRange);
if (ret != AV\_ERR\_OK || widthRange.maxVal <= 0) {
   // Handle exceptions.
} else if (width < widthRange.minVal || width > widthRange.maxVal) {
   // 4. (Optional) Adjust the video width.
   width = std::min(std::max(width, widthRange.minVal), widthRange.maxVal);
}
// 5. Obtain the range of available video heights based on the video width.
OH\_AVRange heightRange = {-1, -1};
ret = OH\_AVCapability\_GetVideoHeightRangeForWidth(capability, width, &heightRange);
if (ret != AV\_ERR\_OK || heightRange.maxVal <= 0) {
   // Handle exceptions.
}
// 6. Select a proper video height from the range.

If the video height is known, you can find the correct size configuration as shown in the following example:

int32\_t height = 1080;
OH\_AVCapability \*capability = OH\_AVCodec\_GetCapability(OH\_AVCODEC\_MIMETYPE\_VIDEO\_AVC, true);
if (capability == nullptr) {
   // Handle exceptions.
}
// 1. Check whether the video height meets the high alignment requirements.
int32\_t heightAlignment = 0;
int32\_t ret = OH\_AVCapability\_GetVideoHeightAlignment(capability, &heightAlignment);
if (ret != AV\_ERR\_OK || heightAlignment <= 0) {
   // Handle exceptions.
} else if (height % heightAlignment != 0) {
   // 2. (Optional) Align the video height.
   height = (height + heightAlignment - 1) / heightAlignment \* heightAlignment;
}
// 3. Check whether the video height is within the supported range.
OH\_AVRange heightRange = {-1, -1};
ret = OH\_AVCapability\_GetVideoHeightRange(capability, &heightRange);
if (ret != AV\_ERR\_OK || heightRange.maxVal <= 0) {
   // Handle exceptions.
} else if (height < heightRange.minVal || height > heightRange.maxVal) {
   // 4. (Optional) Adjust the video height.
   height = std::min(std::max(height, heightRange.minVal), heightRange.maxVal);
}
// 5. Obtain the range of available video widths based on the video height.
OH\_AVRange widthRange = {-1, -1};
ret = OH\_AVCapability\_GetVideoWidthRangeForHeight(capability, height, &widthRange);
if (ret != AV\_ERR\_OK || widthRange.maxVal <= 0) {
   // Handle exceptions.
}
// 6. Select a proper video width from the range.

## Setting the Correct Video Frame Rate

The frame rate of a video codec is limited by the codec's per-second codec capability and the protocol-level per-second processing capability. For example, AVC\_LEVEL\_51 of H.264 limits the maximum number of macroblocks per second to 983040.

The formula for calculating the maximum frame rate based on the video width and height is as follows:

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/25/v3/etzMrakfSYqUeAxEQstslQ/en-us_image_0000002568764885.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062035Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=518F01FB2D66EA3E0D04B1E9649D3C210C39421C974591A616C7D71118D2BA9A)

**MaxMBsPerSecondLevelLimits** refers to the maximum number of macroblocks per second of the codec limited by the protocol, and **MaxMBsPerSecondSubmit** refers to the maximum number of macroblocks per second reported by the codec. The actual capability is the minimum of the two.

| API | Description |
| :-- | :-- |
| OH\_AVCapability\_GetVideoFrameRateRange | Obtains the video frame rate range supported by a video codec. |
| OH\_AVCapability\_GetVideoFrameRateRangeForSize | Obtains the video frame rate range of a video codec based on a given video size. |
| OH\_AVCapability\_AreVideoSizeAndFrameRateSupported | Checks whether a video codec supports the combination of a video size and frame rate. |

When there is a requirement about the target frame rate, check whether the frame rate is within the optional range. An example is as follows:

int32\_t frameRate = 120;
OH\_AVCapability \*capability = OH\_AVCodec\_GetCapability(OH\_AVCODEC\_MIMETYPE\_VIDEO\_AVC, true);
if (capability == nullptr) {
   // Handle exceptions.
}
// 1. Obtain the supported frame rate range.
OH\_AVRange frameRateRange = {-1, -1};
int32\_t ret = OH\_AVCapability\_GetVideoFrameRateRange(capability, &frameRateRange);
if (ret != AV\_ERR\_OK || frameRateRange.maxVal <= 0) {
   // Handle exceptions.
}
// 2. Check whether the frame rate is within the range.
bool isSupported = frameRate >= frameRateRange.minVal && frameRate <= frameRateRange.maxVal;

The code snippet below shows how to select a proper frame rate configuration based on a given video size.

constexpr int32\_t width = 1920;
constexpr int32\_t height = 1080;
int32\_t frameRate = 120;
OH\_AVCapability \*capability = OH\_AVCodec\_GetCapability(OH\_AVCODEC\_MIMETYPE\_VIDEO\_AVC, true);
if (capability == nullptr) {
   // Handle exceptions.
}
// 1. Check whether the video size to be configured can reach the ideal frame rate.
bool isSupported = OH\_AVCapability\_AreVideoSizeAndFrameRateSupported(capability, width, height, frameRate);
if (!isSupported) {
   // 2. Query the supported frame rate range based on the video size, and adjust the frame rate to be configured based on the query result.
   OH\_AVRange frameRateRange = {-1, -1};
   int32\_t ret = OH\_AVCapability\_GetVideoFrameRateRangeForSize(capability, width, height, &frameRateRange);
   if (ret != AV\_ERR\_OK || frameRateRange.maxVal <= 0) {
      // Handle exceptions.
   }
   frameRate = std::min(std::max(frameRate, frameRateRange.minVal), frameRateRange.maxVal);
}

// 3. Set the video size and frame rate.
OH\_AVCodec \*videoEnc = OH\_VideoEncoder\_CreateByMime(OH\_AVCODEC\_MIMETYPE\_VIDEO\_AVC);
if (videoEnc == nullptr) {
   // Handle exceptions.
}
OH\_AVFormat \*format = OH\_AVFormat\_CreateVideoFormat(OH\_AVCODEC\_MIMETYPE\_VIDEO\_AVC, width, height);
if (format == nullptr) {
   // Handle exceptions.
}
if (!OH\_AVFormat\_SetDoubleValue(format, OH\_MD\_KEY\_FRAME\_RATE, static\_cast<double>(frameRate))) {
   // Handle exceptions.
}
if (OH\_VideoEncoder\_Configure(videoEnc, format) != AV\_ERR\_OK) {
   // Handle exceptions.
}
OH\_AVFormat\_Destroy(format);

## Setting the Correct Video Pixel Format

The video pixel format determines the pixel layout of an image that is encoded as input or decoded as output. For details, see [OH\_AVPixelFormat](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-native-avformat-h#oh_avpixelformat).

| API | Description |
| :-- | :-- |
| OH\_AVCapability\_GetVideoSupportedPixelFormats | Obtains the video pixel formats supported by a video codec. |

constexpr OH\_AVPixelFormat DEFAULT\_PIXELFORMAT = AV\_PIXEL\_FORMAT\_NV12;
OH\_AVCapability \*capability = OH\_AVCodec\_GetCapability(OH\_AVCODEC\_MIMETYPE\_VIDEO\_AVC, true);
if (capability == nullptr) {
   // Handle exceptions.
}
// 1. Obtain the video pixel formats supported by the video codec.
const int32\_t \*pixFormats = nullptr;
uint32\_t pixFormatNum = 0;
int32\_t ret = OH\_AVCapability\_GetVideoSupportedPixelFormats(capability, &pixFormats, &pixFormatNum);
if (ret != AV\_ERR\_OK || pixFormats == nullptr || pixFormatNum == 0) {
   // Handle exceptions.
}
// 2. Check whether the pixel format to be configured is supported.
bool isMatched = false;
for (int i = 0; i < pixFormatNum; i++) {
   if (pixFormats\[i\] == DEFAULT\_PIXELFORMAT) {
      isMatched = true;
      break;
   }
}
if (!isMatched) {
   // 3. Replace an unsupported pixel format or select another codec.
}

## Checking Whether a Codec Feature Is Supported and Obtaining Its Properties

Codec features refer to optional features used in specific codec scenarios, such as temporal scalable encoding and low-latency codec in video encoding scenarios. For details, see [OH\_AVCapabilityFeature](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-native-avcapability-h#oh_avcapabilityfeature).

| API | Description |
| :-- | :-- |
| OH\_AVCapability\_IsFeatureSupported | Checks whether a codec supports a given feature. |
| OH\_AVCapability\_GetFeatureProperties | Obtains the properties of a specified feature supported by a codec. |

The code snippet below is an example of querying whether the H.264 encoder supports the long-term reference frame feature:

constexpr int32\_t NEEDED\_LTR\_NUM = 2;
OH\_AVFormat \*format = OH\_AVFormat\_CreateVideoFormat(OH\_AVCODEC\_MIMETYPE\_VIDEO\_AVC, 1920, 1080);
OH\_AVCapability \*capability = OH\_AVCodec\_GetCapability(OH\_AVCODEC\_MIMETYPE\_VIDEO\_AVC, true);
if (capability == nullptr) {
   // Handle exceptions.
}
// 1. Check whether the long-term reference frame feature is supported.
bool isSupported = OH\_AVCapability\_IsFeatureSupported(capability,VIDEO\_ENCODER\_LONG\_TERM\_REFERENCE);
if (isSupported) {
   // 2. Obtain the number of supported long-term reference frames.
   OH\_AVFormat \*properties = OH\_AVCapability\_GetFeatureProperties(capability, VIDEO\_ENCODER\_LONG\_TERM\_REFERENCE);
   if (properties == nullptr) {
      // Handle exceptions.
   }
   int32\_t maxLTRCount = -1;
   bool ret = OH\_AVFormat\_GetIntValue(properties, OH\_FEATURE\_PROPERTY\_KEY\_VIDEO\_ENCODER\_MAX\_LTR\_FRAME\_COUNT, &maxLTRCount);
   if (ret && maxLTRCount >= NEEDED\_LTR\_NUM) {
      if (!OH\_AVFormat\_SetIntValue(format, OH\_MD\_KEY\_VIDEO\_ENCODER\_LTR\_FRAME\_COUNT, NEEDED\_LTR\_NUM)) {
         // Handle exceptions.
      }
   }
}
// 3. Create and configure an encoder.
OH\_AVCodec \*videoEnc = OH\_VideoEncoder\_CreateByMime(OH\_AVCODEC\_MIMETYPE\_VIDEO\_AVC);
if (OH\_VideoEncoder\_Configure(videoEnc, format) != AV\_ERR\_OK) {
   // Handle exceptions.
}
