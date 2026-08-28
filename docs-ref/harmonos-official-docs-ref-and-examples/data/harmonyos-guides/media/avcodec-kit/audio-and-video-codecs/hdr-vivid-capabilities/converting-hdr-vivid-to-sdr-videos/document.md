# Converting HDR Vivid to SDR Videos

When sharing or editing an HDR Vivid video, you can call the AVCodec capability to convert the video to the SDR format.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c8/v3/cO57rDjYQXad2_oHT3yocw/en-us_image_0000002185420136.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062036Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=7490AE18D687D81B77632B8FAFF55A6F90497FA724C4FF094E4D0F781AB5E9F0 "Click to enlarge")

#### Constraints

1.  This feature is available only for hardware decoders.
2.  This feature is supported only in surface mode. For details about the output differences between the surface mode and buffer mode, see [Video Decoding](../../video-decoding/document.md).
3.  When this feature is enabled, the stream resolution cannot be changed, and the error code [AV\_ERR\_UNSUPPORT](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-native-averrors-h#oh_averrcode) is reported through the callback function **OH\_AVCodecOnError()**.
4.  After **OH\_VideoDecoder\_Configure** is successfully called and before **OH\_VideoDecoder\_Start** is called, you must call **OH\_VideoDecoder\_Prepare**.
5.  If **OH\_VideoDecoder\_Reset** is called to reset the decoder to the initial state, you must call **OH\_VideoDecoder\_Configure**, **OH\_VideoDecoder\_Prepare**, and **OH\_VideoDecoder\_SetSurface** again.
6.  You can configure **OH\_MD\_KEY\_VIDEO\_DECODER\_OUTPUT\_COLOR\_SPACE** to output SDR images after decoding. Currently, only HDR Vivid streams can be input, and only OH\_COLORSPACE\_BT709\_LIMIT streams can be output.

## Linking the Dynamic Libraries in the CMake Script

target\_link\_libraries(sample PUBLIC libnative\_media\_avsource.so)
target\_link\_libraries(sample PUBLIC libnative\_media\_vdec.so)
target\_link\_libraries(sample PUBLIC libnative\_media\_core.so)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f5/v3/8vekVYkdQTGzhpRHbyZUbQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062036Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=D0C2BA46CD8C4E2D73F84217AAE722650C4C85FBB92F74997ACE0DA85AA9B021)

The word **sample** in the preceding code snippet is only an example. Use the actual project directory name.

## How to Develop

1.  Add the header files.
    
    #include <multimedia/player\_framework/native\_avcodec\_videodecoder.h>
    #include <multimedia/player\_framework/native\_avcapability.h>
    #include <multimedia/player\_framework/native\_avcodec\_base.h>
    #include <multimedia/player\_framework/native\_avformat.h>
    #include <multimedia/player\_framework/native\_avbuffer.h>
    #include <fstream>
    
2.  Add the header files and the file to parse by referring to [HDR Vivid Video Playback](../hdr-vivid-video-playback/document.md), and check whether the video format is HDR Vivid.
    
    If the video format is not HDR Vivid, decode the video by referring to [Video Decoding](../../video-decoding/document.md).
    
    If the video format is HDR Vivid, proceed to the next step.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/90/v3/JXq-wrpTQf-1CRjanUXbJA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062036Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=A9225F691995DA75A036F6F068AE439DD0AAAD8E85061B0BD75093A255439219)
    
    If the input source is not HDR Vivid, the error code [AV\_ERR\_VIDEO\_UNSUPPORTED\_COLOR\_SPACE\_CONVERSION](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-native-averrors-h#oh_averrcode) is reported through the callback function [OH\_AVCodecOnError()](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-native-avcodec-base-h#oh_avcodeconerror).
    
3.  Create a decoder instance.
    
    Query the decoder capabilities supported by the system and create a hardware decoder based on the query result.
    
    In the code snippet below, the following variables are used:
    
    -   **videoDec**: pointer to the video decoder instance.
    -   **capability**: pointer to the decoder's capability.
    -   **OH\_AVCODEC\_MIMETYPE\_VIDEO\_HEVC**: HEVC video codec.
    
    // 3.1 Obtain the HEVC decoder capability of the specified hardware.
    OH\_AVCapability \*capability = OH\_AVCodec\_GetCapabilityByCategory(OH\_AVCODEC\_MIMETYPE\_VIDEO\_HEVC, false, HARDWARE); 
    if (capability == nullptr){ 
     // Handle exceptions.
    } 
    // 3.2 Obtain the name of an HEVC hardware decoder.
    const char \*name = OH\_AVCapability\_GetName(capability); 
    // 3.3 Create an HEVC hardware decoder instance.
    OH\_AVCodec \*videoDec = OH\_VideoDecoder\_CreateByName(name); 
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3e/v3/8hkzAxp2QeGhMLd_ysXCew/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062036Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=000F68CC2E0DFC8228159CB92FAD3EC0964A1B8596307A789248BBC76A9B41D9)
    
    Currently, this feature is available only for hardware decoders. Therefore, you must create a decoder by name.
    
4.  Call **OH\_VideoDecoder\_RegisterCallback()** to set callback functions.
    
    For details, see "Step 3: Configure the asynchronous callback function" in [Decoding an HDR Vivid Video](../hdr-vivid-video-playback/document.md#section182234161516).
    
5.  Call **OH\_VideoDecoder\_Configure()** to configure the decoder.
    
    The video frame width, video frame height, and video pixel format must be configured, and the output format must be SDR. The following is an example:
    
    -   **DEFAULT\_WIDTH**: 320 pixels
    -   **DEFAULT\_HEIGHT**: 240 pixels
    -   **DEFAULT\_PIXELFORMAT**: **AV\_PIXEL\_FORMAT\_NV12** (the pixel format of the YUV file is NV12)
        
        // Video frame width.
        int32\_t width = 320; 
        // Video frame height.
        int32\_t height = 240;
        // Video pixel format.
        constexpr OH\_AVPixelFormat DEFAULT\_PIXELFORMAT = AV\_PIXEL\_FORMAT\_NV12;
        OH\_AVFormat \*format = OH\_AVFormat\_Create();
        // 5.1 Configure the video width, height, and pixel format.
        OH\_AVFormat\_SetIntValue(format, OH\_MD\_KEY\_WIDTH, width);
        OH\_AVFormat\_SetIntValue(format, OH\_MD\_KEY\_HEIGHT, height);
        OH\_AVFormat\_SetIntValue(format, OH\_MD\_KEY\_PIXEL\_FORMAT, DEFAULT\_PIXELFORMAT);
        // 5.2 Specify the SDR output format.
        OH\_AVFormat\_SetIntValue(format, OH\_MD\_KEY\_VIDEO\_DECODER\_OUTPUT\_COLOR\_SPACE, OH\_COLORSPACE\_BT709\_LIMIT);
        // 5.3 Configure the decoder.
        int32\_t ret = OH\_VideoDecoder\_Configure(videoDec, format);
        if (ret != AV\_ERR\_OK) {
            // Handle exceptions.
        }
        OH\_AVFormat\_Destroy(format);
        
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8b/v3/8pacW2VeT-aSVCm_SU98eA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062036Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=422C656DCA3AAF29245049E8A8A55FD013FE48008D80119A30299D1E7AB07033)
    
    You can configure **OH\_MD\_KEY\_VIDEO\_DECODER\_OUTPUT\_COLOR\_SPACE** to output SDR images after decoding. Currently, only HDR Vivid streams can be input, and only OH\_COLORSPACE\_BT709\_LIMIT streams can be output.
    
6.  For details about the subsequent steps, see [Video Decoding in Surface Mode](../../video-decoding/document.md#surface-mode).
