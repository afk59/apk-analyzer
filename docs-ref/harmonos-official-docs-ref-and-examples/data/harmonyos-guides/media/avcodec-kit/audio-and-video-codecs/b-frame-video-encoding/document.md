# B-Frame Video Encoding

Starting from API version 20, B-frame video encoding is supported.

B-frames, short for Bidirectional Predictive Frames, are one of the primary frame types defined in video encoding standards. The main difference between B-frames and P-frames is that while P-frames support only forward prediction, B-frames support bidirectional prediction.

The prediction process in B-frame encoding utilizes information from both preceding and succeeding frames, which can significantly reduce temporal redundancy in the signal and achieve higher compression efficiency.

Enabling B-frames has the following impacts:

-   Enabling B-frames increases the distance between reference frames for P-frame encoding, which may affect the compression ratio and visual quality of P-frames. Generally, in scenarios with complex temporal dynamics, the combined impact of P-frames and B-frames should be considered.
-   Enabling B-frames also increases the end-to-end latency for both encoding and decoding.

#### When to Use

-   Video recording
-   Editing and exporting
-   Video transcoding
-   Non-low-latency live streaming

#### Constraints

-   **Supported platforms**: This feature is platform-dependent. You can query the support using the [OH\_AVCapability\_IsFeatureSupported](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-native-avcapability-h#oh_avcapability_isfeaturesupported) API.
-   **Supported API versions**: API version 20 and later.
-   **Supported encoders**: This feature is encoder-dependent. You can query the support using the [OH\_AVCodec\_GetCapabilityByCategory](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-native-avcapability-h#oh_avcodec_getcapabilitybycategory) API.
-   **Supported bit rate control modes**: VBR, CBR, SQR, and CQ.
-   B-frame encoding is not supported alongside temporally scalable video encoding.
-   B-frame encoding is not supported alongside long-term reference frames.

#### Available APIs

B-frame encoding must be configured at the initialization phase and takes effect throughout the process. Dynamic modification is not supported.

The configuration parameters are as follows:

| Parameter | Description | Format |
| :-- | :-- | :-- |
| OH\_MD\_KEY\_VIDEO\_ENCODER\_ENABLE\_B\_FRAME | 
Enabled status of B-frame video recording.

B-frame encoding can be enabled only when it is supported.

 | int |
| OH\_MD\_KEY\_VIDEO\_ENCODER\_MAX\_B\_FRAMES | 

Maximum number of B-frames supported by video encoding.

It is used only for query.

 | int |

#### How to Develop

For details about basic encoding functionality, see [Video Encoding](../video-encoding/document.md). The following are specific instructions for B-frame encoding.

1.  When creating an encoder instance, check whether the video encoder supports B-frame encoding.
    
    // 1.1 Obtain the video encoder capability instance. The following uses H.265 as an example.
    OH\_AVCapability \*cap = OH\_AVCodec\_GetCapabilityByCategory(OH\_AVCODEC\_MIMETYPE\_VIDEO\_HEVC, true, HARDWARE);
    if (cap != nullptr) {
        OH\_LOG\_INFO("Get codec Capability success!");
        // 1.2 Check whether B-frame encoding is supported.
        bool isSupported = OH\_AVCapability\_IsFeatureSupported(cap, VIDEO\_ENCODER\_B\_FRAME);
        int32\_t supportedMaxBFrameCount = 0;
        if (isSupported) {
            OH\_LOG\_INFO("Feature VIDEO\_ENCODER\_B\_FRAME is Supported!");
            // 1.3 Query the maximum number of B-frames that can be supported.
            OH\_AVFormat \*property = OH\_AVCapability\_GetFeatureProperties(cap, VIDEO\_ENCODER\_B\_FRAME);
            OH\_AVFormat\_GetIntValue(property, OH\_MD\_KEY\_VIDEO\_ENCODER\_MAX\_B\_FRAMES, &supportedMaxBFrameCount);
            OH\_LOG\_INFO("Get supportedMaxBFrameCount,value is %{public}d!", supportedMaxBFrameCount);
            // 1.4 Destroy the temporary AVFormat.
            OH\_AVFormat\_Destroy(property);
        } else {
            OH\_LOG\_ERROR("Feature VIDEO\_ENCODER\_B\_FRAME is not Supported!");
        }
    } else {
        OH\_LOG\_ERROR("codec Capability is null!");
    }
    
    If B-frame encoding is supported, you can enable it.
    
2.  Configure B-frame encoding during the configuration phase.
    
    // 2.1 Create a temporary AVFormat used for configuration.
    OH\_AVFormat \*format = OH\_AVFormat\_Create();
    // 2.2 Fill in the key-value pair of the parameter used to enable the feature.
    OH\_AVFormat\_SetIntValue(format, OH\_MD\_KEY\_VIDEO\_ENCODER\_ENABLE\_B\_FRAME, 1);
    // 2.3 Set parameters.
    int32\_t ret = OH\_VideoEncoder\_Configure(videoEnc, format);
    if (ret != AV\_ERR\_OK) {
        // Handle exceptions.
    }
    // 2.4 Destroy the temporary AVFormat after the configuration is complete.
    OH\_AVFormat\_Destroy(format);
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bb/v3/zLMSj9v7RFar50ibEAA4fQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062036Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=07F218B69A83CD0A11965603372B85C5C9E3BE785DEDF0D4F0007F91A52D49AD)
    
    -   Enabling B-frame encoding is weakly checked during the configure phase. If the parameter configuration is incorrect or the encoder does not support the feature, **AV\_ERR\_OK** is returned, with a warning message printed. Check whether the feature is truly enabled based on the encoded stream and runtime logs.
    -   When B-frame encoding is enabled, the actual B-frame structure and number of B-frames in the encoded stream depend on the platform's capabilities.
