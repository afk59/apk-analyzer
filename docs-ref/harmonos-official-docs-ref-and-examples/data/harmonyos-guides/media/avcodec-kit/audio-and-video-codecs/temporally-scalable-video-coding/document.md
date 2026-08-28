# Temporally Scalable Video Coding

#### Basic Concepts

## Introduction to Temporally Scalable Video Coding

Scalable video coding is an extended standard for video coding. SVC (short for Scalable Video Coding, an extension of the H.264 standard) and SHVC (short for Scalable High Efficiency Video Coding, an extension of the H.265 standard) are popular nowadays.

Scalable video coding allows conveyance of information structured in a hierarchical manner of spatial scalability, temporal scalability, and quality scalability.

Temporally scalable video coding refers to the process of encoding a video sequence into a set of layers that provide an increasing temporal resolution. The following figure shows the structure of a bitstream that contains four temporal layers and is constructed based on the reference relationship.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b6/v3/lrIq-zVpQn-5Dl2iqswOtw/en-us_image_0000002537765164.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062036Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=BF009D57957F40E1867C9684CDB13BE76EEA94BEF345A4C0045ED489FDA9421D)

In scenarios where the channel condition is poor, frames can be dropped layer by layer in descending order (L3- > L2- > L1) to meet the changing requirements of transmission and decoding capabilities.

The figure below shows the new bitstream structure when the frames at L3 are dropped. The bitstream can be normally decoded while the frame rate is reduced by half. Dropping can occur at other layers in a similar way.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a7/v3/VnU9uujYQNmohoywnMTV0g/en-us_image_0000002537925104.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062036Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=432EE9CDA43B7DF454BF368E90C3550978B8DDD0B6300DF3D2559AF266488E6A)

## Structure of a Temporally Scalable Bitstream

A bitstream is organized by one or more Group of Pictures (GOPs). A GOP is a collection of consecutive pictures that can be independently decoded. It measures the distance between two I-frames (also named key frames).

A GOP can be further divided into one or more Temporal Group of Pictures (TGOPs), and each TGOP is composed by a base layer (BL) and one or more associated enhancement layers (ELs). For example, frame 0 to frame 7 in the foregoing four-layer temporally scalable bitstream form a TGOP.

-   BL: bottom layer (L0) in the GOP. In temporal scalability, this layer is encoded at the lowest frame rate.
    
-   EL: layers above the BL. There are L1, L2, and L3 in ascending order. In temporal scalability, the lowest EL encodes, based on the BL, the frames at a higher frame rate; a higher EL encodes, based on the BL or a lower EL, the frames at a higher frame rate.
    

## How to Implement the Structure of a Temporally Scalable Bitstream

The temporally scalable bitstream structure is implemented by specifying reference frames, which are classified into the following types based on the duration of residence in a Decoded Picture Buffer (DPB):

-   Short-Term Reference (STR): a reference frame that cannot reside in the DPB for a long period of time. It adopts the First In First Out (FIFO) approach, which means that the oldest STR is removed from the DPB once the DPB is full.
    
-   Long-Term Reference (LTR): a reference frame that can reside in the DPB for a long period of time. It stays in the DPB until it is replaced by another decoded picture with the same ID.
    

Although a specific cross-frame reference structure can be implemented when there is more than one STR, the span supported by temporal scalability is limited due to an excessively short validity period. This problem does not exist when coming to the LTR, which also covers the cross-frame scenario of the STR. Therefore, the LTR is preferably used to implement the structure of a temporally scalable bitstream.

#### When to Use

You are advised to use temporal scalability in the following scenarios:

-   Real-time encoding and transmission scenarios with no cache or low cache on the playback side, for example, video conferencing, live streaming, and collaborative office.
    
-   Video encoding and recording scenario that requires video preview or multi-speed playback.
    

If your application does not involve dynamic adjustment of the temporal reference structure and the hierarchical structure is simple, you are advised to use [global temporal scalability](#global-temporal-scalability). Otherwise, enable [LTR](#ltr).

#### Constraints

-   The global temporal scalability and LTR features are mutually exclusive.
    
    The two features cannot be both enabled because they have normalized bottom-layer implementation.
    
-   When using the forcible IDR configuration along with the two features, use the frame channel configuration.
    
    The reference frame is valid only in the GOP. After an I-frame is refreshed, the DPB is cleared, so does the reference frame. In other words, the I-frame refresh location has a great impact on the reference relationship.
    
    When temporal scalability is enabled, to temporarily request the I-frame through **OH\_MD\_KEY\_REQUEST\_I\_FRAME**, you must configure the frame channel with a determined effective time to notify the system of the I-frame refresh location, so as to avoid disorder of the reference relationship. For details, see the configuration guide of the frame channel. Do not use **OH\_VideoEncoder\_SetParameter**, which uses an uncertain effective time. For details, see step 4 in [Video Encoding in Surface Mode](../video-encoding/document.md#surface-mode).
    
-   The callback using **OH\_AVBuffer** is supported, but the callback using **OH\_AVMemory** is not.
    
    Temporal scalability depends on the frame feature. Do not use **OH\_AVMemory** to trigger **OH\_AVCodecAsyncCallback**. Instead, use **OH\_AVBuffer** to trigger **OH\_AVCodecCallback**.
    
-   Temporal scalability employs P-pictures, but not B-pictures.
    
    Temporal scalability can be hierarchical-P or hierarchical-B. Currently, this feature can only be hierarchical-P.
    
-   In the case of **UNIFORMLY\_SCALED\_REFERENCE**, TGOP can only be 2 or 4.
    

#### Global Temporal Scalability

## Available APIs

Global temporal scalability is suitable for encoding frames into a stable and simple temporal structure. Its initial configuration takes effect globally and cannot be dynamically modified. The configuration parameters are as follows:

| Parameter | Description |
| :-- | :-- |
| OH\_MD\_KEY\_VIDEO\_ENCODER\_ENABLE\_TEMPORAL\_SCALABILITY | Enabled status of the global temporal scalability feature. |
| OH\_MD\_KEY\_VIDEO\_ENCODER\_TEMPORAL\_GOP\_SIZE | TGOP size of the global temporal scalability feature. |
| OH\_MD\_KEY\_VIDEO\_ENCODER\_TEMPORAL\_GOP\_REFERENCE\_MODE | TGOP reference mode of the global temporal scalability feature. |

-   **OH\_MD\_KEY\_VIDEO\_ENCODER\_ENABLE\_TEMPORAL\_SCALABILITY**: This parameter is set in the configuration phase. The feature can be successfully enabled only when it is supported.
    
-   **OH\_MD\_KEY\_VIDEO\_ENCODER\_TEMPORAL\_GOP\_SIZE**: This parameter is optional and specifies the distance between two I-frames. You need to customize the I-frame density based on the frame extraction requirements. The value range is \[2, GopSize). If no value is passed in, the default value is used.
    
-   **OH\_MD\_KEY\_VIDEO\_ENCODER\_TEMPORAL\_GOP\_REFERENCE\_MODE**: This parameter is optional and affects the reference mode of non-I-frames. The value can be **ADJACENT\_REFERENCE**, **JUMP\_REFERENCE**, or **UNIFORMLY\_SCALED\_REFERENCE**. **ADJACENT\_REFERENCE** provides better compression performance, whereas **JUMP\_REFERENCE** is more flexible in dropping frames. **UNIFORMLY\_SCALED\_REFERENCE** enables streams to be distributed more evenly in the case of frame loss. If no value is passed in, the default value is used.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/95/v3/U4FH4KF4TY-Ea40z70fing/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062036Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=C05B470A80D2E11A99F4346EEDACA40832DF2F6F0B9C7935970079872248B9B0)
    
    In the case of **UNIFORMLY\_SCALED\_REFERENCE**, TGOP can only be 2 or 4.
    

Example 1: ADJACENT\_REFERENCE in TGOP=4

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e1/v3/Ft0MRfVzRXeDHvqGiCkyjw/en-us_image_0000002568684881.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062036Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=7184FA59FD40B3273EC1493114AF4ABBBD791F6F4A4A58683FDAEF80B4B56746)

Example 2: JUMP\_REFERENCE in TGOP=4

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7a/v3/48UT23rRSWShTUGAUuCzVA/en-us_image_0000002568764891.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062036Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=4F3A07AD72896CBC67E0B2BF70532434CBF4B121D5400CA2E1249AF8B17591D2)

Example 3: UNIFORMLY\_SCALED\_REFERENCE in TGOP = 4

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1f/v3/I3-ti1bNTwu-1AG2IrUa8g/en-us_image_0000002537765166.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062036Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=2BF0CDA23B40188A3C360159877F5DBC665D9831B3E44820F22172ACA23AB196)

## How to Develop

You can learn the basic encoding process in [Video Encoding](../video-encoding/document.md). This section describes the differences from the basic video encoding process.

1.  When creating an encoder instance, check whether the video encoder supports the global temporal scalability feature.
    
    // 1.1 Obtain the video encoder capability instance. The following uses H.264 as an example.
    OH\_AVCapability \*cap = OH\_AVCodec\_GetCapability(OH\_AVCODEC\_MIMETYPE\_VIDEO\_AVC, true);
    // 1.2 Check whether the global temporal scalability feature is supported.
    bool isSupported = OH\_AVCapability\_IsFeatureSupported(cap, VIDEO\_ENCODER\_TEMPORAL\_SCALABILITY);
    
    If the feature is supported, it can be enabled.
    
    // Create a hardware encoder instance.
    OH\_AVCodec \*videoEnc = OH\_VideoEncoder\_CreateByMime(OH\_AVCODEC\_MIMETYPE\_VIDEO\_AVC);
    
2.  In the configuration phase, configure the parameters related to the global temporal scalability feature.
    
    constexpr int32\_t TGOP\_SIZE = 3;
    // 2.1 Create a temporary AVFormat used for configuration.
    auto format = std::shared\_ptr<OH\_AVFormat>(OH\_AVFormat\_Create(), OH\_AVFormat\_Destroy);
    if (format == nullptr) {
        // Handle exceptions.
    }
    // 2.2 Fill in the key-value pair of the parameter used to enable the feature.
    OH\_AVFormat\_SetIntValue(format.get(), OH\_MD\_KEY\_VIDEO\_ENCODER\_ENABLE\_TEMPORAL\_SCALABILITY, 1);
    // 2.3 (Optional) Fill in the key-value pairs of the parameters that specify the TGOP size and reference mode.
    OH\_AVFormat\_SetIntValue(format.get(), OH\_MD\_KEY\_VIDEO\_ENCODER\_TEMPORAL\_GOP\_SIZE, TGOP\_SIZE);
    OH\_AVFormat\_SetIntValue(format.get(), OH\_MD\_KEY\_VIDEO\_ENCODER\_TEMPORAL\_GOP\_REFERENCE\_MODE, ADJACENT\_REFERENCE);
    // 2.4 Configure the parameters.
    int32\_t ret = OH\_VideoEncoder\_Configure(videoEnc, format.get());
    if (ret != AV\_ERR\_OK) {
        // Handle exceptions.
    }
    
3.  (Optional) During output rotation, obtain the temporal layer information corresponding to the bitstream.
    
    You can obtain the temporal layer information based on the configured TGOP parameters and the number of encoded frames.
    
    The sample code is as follows:
    
    constexpr int32\_t TGOP\_SIZE = 3;
    uint32\_t outPoc = 0;
    // Obtain the relative position in the TGOP based on the number of valid frames in the output callback and determine the layer based on the configuration.
    static void OnNewOutputBuffer(OH\_AVCodec \*codec, uint32\_t index, OH\_AVBuffer \*buffer, void \*userData)
    {
        struct OH\_AVCodecBufferAttr attr;
        OH\_AVErrCode ret = OH\_AVBuffer\_GetBufferAttr(buffer, &attr);
        if (ret != AV\_ERR\_OK) {
            // Handle exceptions.
        }
        // Set POC to 0 after the I-frame is refreshed.
        if (attr.flags & AVCODEC\_BUFFER\_FLAGS\_SYNC\_FRAME) {
            outPoc = 0;
        }
        // Skip this step only for the XPS output.
        if (attr.flags != AVCODEC\_BUFFER\_FLAGS\_CODEC\_DATA) {
            int32\_t tGopInner = outPoc % TGOP\_SIZE;
            if (tGopInner == 0) {
                // I-frames cannot be dropped in subsequent transmission and decoding processes.
            } else {
                // Non-I-frames can be dropped in subsequent transmission and decoding processes.
            }
            outPoc++;
        }
    }
    
4.  (Optional) During output rotation, use the temporal layer information obtained for adaptive transmission or decoding.
    
    Based on the temporally scalable bitstream and layer information, select a required layer for transmission, or carry the information to the peer for adaptive decoding.
    

#### LTR

## Available APIs

The LTR feature provides a configuration of the frame-level reference relationship. It is suitable for flexible and complex temporally hierarchical structures.

| Parameter | Description |
| :-- | :-- |
| OH\_MD\_KEY\_VIDEO\_ENCODER\_LTR\_FRAME\_COUNT | Number of LTR frames. |
| OH\_MD\_KEY\_VIDEO\_ENCODER\_PER\_FRAME\_MARK\_LTR | Marked as an LTR frame. |
| OH\_MD\_KEY\_VIDEO\_ENCODER\_PER\_FRAME\_USE\_LTR | POC number of the LTR frame referenced by the current frame. |

-   **OH\_MD\_KEY\_VIDEO\_ENCODER\_LTR\_FRAME\_COUNT**: This parameter is set in the configuration phase. The value of this parameter must not be greater than the maximum number of supported LTR frames. For details, see step 3 below.
-   \*\*OH\_MD\_KEY\_VIDEO\_ENCODER\_PER\_FRAME\_MARK\_LTR \*\*: The BL layer and the EL layer to skip are marked as an LTR frame.
-   **OH\_MD\_KEY\_VIDEO\_ENCODER\_PER\_FRAME\_USE\_LTR**: POC number of the frame marked as the LTR frame.

For example, to implement the four-layer temporally hierarchical structure described in [Introduction to Temporally Scalable Video Coding](#introduction-to-temporally-scalable-video-coding), perform the following steps:

1.  In the configuration phase, set **OH\_MD\_KEY\_VIDEO\_ENCODER\_LTR\_FRAME\_COUNT** to **5**.
    
2.  In the input rotation of the running phase, configure the LTR parameters according to the following table, where \*\*\*\* means that no configuration is required.
    
    | Configuration\\POC | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 | 15 | 16 |
    | :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- |
    | MARK\_LTR | 1 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 1 |
    | USE\_LTR | \\ | \\ | 0 | \\ | 0 | \\ | 4 | \\ | 0 | \\ | 8 | \\ | 8 | \\ | 12 | \\ | 8 |
    

## How to Develop

This section describes only the steps that are different from the basic encoding process. You can learn the basic encoding process in [Video Encoding](../video-encoding/document.md).

1.  When creating an encoder instance, check whether the video encoder supports the LTR feature.
    
    constexpr int32\_t NEEDED\_LTR\_COUNT = 5;
    bool isSupported = false;
    int32\_t supportedLTRCount = 0;
    // 1.1 Obtain the encoder capability instance. The following uses H.264 as an example.
    OH\_AVCapability \*cap = OH\_AVCodec\_GetCapability(OH\_AVCODEC\_MIMETYPE\_VIDEO\_AVC, true);
    // 1.2 Check whether the LTR feature is supported.
    isSupported = OH\_AVCapability\_IsFeatureSupported(cap, VIDEO\_ENCODER\_LONG\_TERM\_REFERENCE);
    // 1.3 Determine the number of supported LTR frames.
    if (isSupported) {
        OH\_AVFormat \*properties = OH\_AVCapability\_GetFeatureProperties(cap, VIDEO\_ENCODER\_LONG\_TERM\_REFERENCE);
        if (!OH\_AVFormat\_GetIntValue(properties, OH\_FEATURE\_PROPERTY\_KEY\_VIDEO\_ENCODER\_MAX\_LTR\_FRAME\_COUNT, &supportedLTRCount)) {
            // Handle exceptions.
        }
        OH\_AVFormat\_Destroy(properties);
        // 1.4 Check whether the number of supported LTR frames meets the structure requirements.
        isSupported = supportedLTRCount >= NEEDED\_LTR\_COUNT;
    }
    
    If the LTR feature is supported and the number of LTR frames meets the requirements, the feature can be enabled.
    
2.  Register the frame channel callback functions.
    
    The following is an example of the configuration in buffer input mode:
    
    // 2.1 Implement the OH\_AVCodecOnNeedInputBuffer callback function.
    static void OnNeedInputBuffer(OH\_AVCodec \*codec, uint32\_t index, OH\_AVBuffer \*buffer, void \*userData)
    {
        // The index of the input frame buffer is sent to InIndexQueue.
        // The input frame data (specified by buffer) is sent to InBufferQueue.
        // Perform data processing. For details, see:
        // - Write the stream to encode.
        // - Notify the encoder of EOS.
        // - Write the frame parameter.
        auto format = std::shared\_ptr<OH\_AVFormat>(OH\_AVBuffer\_GetParameter(buffer), OH\_AVFormat\_Destroy);
        if (format == nullptr) {
            // Handle exceptions.
        }
        OH\_AVFormat\_SetIntValue(format.get(), OH\_MD\_KEY\_VIDEO\_ENCODER\_PER\_FRAME\_MARK\_LTR, 1);
        OH\_AVFormat\_SetIntValue(format.get(), OH\_MD\_KEY\_VIDEO\_ENCODER\_PER\_FRAME\_USE\_LTR, 4);
        OH\_AVBuffer\_SetParameter(buffer, format.get());
        // Notify the encoder that the buffer input is complete.
        OH\_VideoEncoder\_PushInputBuffer(codec, index);
    }
    
    // 2.2 Implement the OH\_AVCodecOnNewOutputBuffer callback function.
    static void OnNewOutputBuffer(OH\_AVCodec \*codec, uint32\_t index, OH\_AVBuffer \*buffer, void \*userData)
    {
        // The index of the output frame buffer is sent to outIndexQueue.
        // The encoded frame data (specified by buffer) is sent to outBufferQueue.
        // Perform data processing. For details, see:
        // - Release the encoded frame.
        // - Record POC and the enabled status of LTR.
    }
    
    // 2.3 Register the callback functions.
    OH\_AVCodecCallback cb;
    cb.onNeedInputBuffer = OnNeedInputBuffer;
    cb.onNewOutputBuffer = OnNewOutputBuffer;
    OH\_VideoEncoder\_RegisterCallback(videoEnc, cb, nullptr);
    
    The following is an example of the configuration in surface input mode:
    
    // 2.1 Implement the OH\_VideoEncoder\_OnNeedInputParameter callback function.
    static void OnNeedInputParameter(OH\_AVCodec \*codec, uint32\_t index, OH\_AVFormat \*parameter, void \*userData)
    {
        // The index of the input frame buffer is sent to InIndexQueue.
        // The input frame data (specified by avformat) is sent to InFormatQueue.
        // Perform data processing. For details, see:
        // - Write the stream to encode.
        // - Notify the encoder of EOS.
        // - Write the frame parameter.
        OH\_AVFormat\_SetIntValue(parameter, OH\_MD\_KEY\_VIDEO\_ENCODER\_PER\_FRAME\_MARK\_LTR, 1);
        OH\_AVFormat\_SetIntValue(parameter, OH\_MD\_KEY\_VIDEO\_ENCODER\_PER\_FRAME\_USE\_LTR, 4);
        // Notify the encoder that the frame input is complete.
        OH\_VideoEncoder\_PushInputParameter(codec, index);
    }
    
    // 2.2 Implement the OH\_AVCodecOnNewOutputBuffer callback function.
    static void OnNewOutputBuffer(OH\_AVCodec \*codec, uint32\_t index, OH\_AVBuffer \*buffer, void \*userData)
    {
        // The index of the output frame buffer is sent to outIndexQueue.
        // The encoded frame data (specified by buffer) is sent to outBufferQueue.
        // Perform data processing. For details, see:
        // - Release the encoded frame.
        // - Record POC and the enabled status of LTR.
    }
    
    // 2.3 Register the callback functions.
    OH\_AVCodecCallback cb;
    cb.onNewOutputBuffer = OnNewOutputBuffer;
    OH\_VideoEncoder\_RegisterCallback(videoEnc, cb, nullptr);
    // 2.4 Register the frame channel callback functions.
    OH\_VideoEncoder\_OnNeedInputParameter inParaCb = OnNeedInputParameter;
    OH\_VideoEncoder\_RegisterParameterCallback(videoEnc, inParaCb, nullptr);
    
3.  In the configuration phase, configure the maximum number of LTR frames.
    
    constexpr int32\_t NEEDED\_LTR\_COUNT = 5;
    // 3.1 Create a temporary AVFormat used for configuration.
    auto format = std::shared\_ptr<OH\_AVFormat>(OH\_AVFormat\_Create(), OH\_AVFormat\_Destroy);
    if (format == nullptr) {
        // Handle exceptions.
    }
    // 3.2 Fill in the key-value pair of the parameter that specifies the number of LTR frames.
    OH\_AVFormat\_SetIntValue(format.get(), OH\_MD\_KEY\_VIDEO\_ENCODER\_LTR\_FRAME\_COUNT, NEEDED\_LTR\_COUNT);
    // 3.3 Configure the parameters.
    int32\_t ret = OH\_VideoEncoder\_Configure(videoEnc, format.get());
    if (ret != AV\_ERR\_OK) {
        // Handle exceptions.
    }
    
4.  (Optional) During output rotation, obtain the temporal layer information corresponding to the bitstream.
    
    This procedure is the same as that described in the global temporal scalability feature.
    
    The LTR parameters are configured in the input rotation. You can also record the LTR parameters in the input rotation and find the corresponding input parameters in the output rotation.
    
5.  (Optional) During output rotation, use the temporal layer information obtained for adaptive transmission or decoding.
    
    This procedure is the same as that described in the global temporal scalability feature.
