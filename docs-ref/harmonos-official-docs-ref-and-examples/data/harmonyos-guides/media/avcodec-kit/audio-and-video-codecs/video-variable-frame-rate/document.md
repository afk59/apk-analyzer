# Video Variable Frame Rate

Starting from API version 15, the video variable refresh rate feature is supported.

With the C APIs related to the video variable refresh rate feature, you can dynamically adjust the screen refresh rate based on the video content during playback. This helps save display power while maintaining smooth video playback.

#### When to Use

The video variable refresh rate feature is ideal for video sources with high frame rates (>30 fps). For video sources with frame rates at or below 30 fps, a refresh rate of 30 Hz is recommended. The figure below demonstrates the playback of a 60 fps video. The algorithm adjusts the screen refresh rate in real-time based on the video content. If the refresh rate drops below the video frame rate, some frames will be discarded to save power.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/40/v3/L9SlvDTFQ7y92KHUKbKVuA/en-us_image_0000002537765170.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062036Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=59109C2BE2809E3101E1A8CB068A7E864788E24D2465C0910805AD024F55AB03)

#### Constraints

1.  This feature is available only for the scenario where the video is directly sent for display after hardware decoding.
2.  The overall screen refresh rate will change. It is recommended that you use this feature in full-screen playback scenarios without bullet comments or animations, as the feature may affect their smoothness.
3.  This feature depends on the decoding frame rate configuration. The **OH\_MD\_KEY\_FRAME\_RATE** property must be correctly set before use.
4.  This feature is platform-dependent. If the platform does not support this feature, the API calls do not report an error, but the feature does not take effect. Normal decoding and playback still function.

#### How to Develop

This section describes only the steps that are different from the basic decoding process. You can learn the basic decoding process in [Video Decoding](../video-decoding/document.md).

1.  Enable the video variable frame rate feature during decoder configuration.
    
    In the code snippet below, the following variables are used:
    
    **videoDec**: pointer to the video decoder instance. For details, see [Creating a Decoder Instance in Surface Mode](../video-decoding/document.md#surface-mode).
    
    OH\_AVFormat \*format = OH\_AVFormat\_Create();
    int32\_t width = 1280; // Video frame width.
    int32\_t height = 720; // Video frame height.
    int32\_t fps = 60; // Video frame rate.
    OH\_AVFormat\_SetIntValue(format, OH\_MD\_KEY\_WIDTH, width);
    OH\_AVFormat\_SetIntValue(format, OH\_MD\_KEY\_HEIGHT, height);
    OH\_AVFormat\_SetIntValue(format, OH\_MD\_KEY\_FRAME\_RATE, fps);
    OH\_AVFormat\_SetIntValue(format, OH\_MD\_KEY\_VIDEO\_DECODER\_OUTPUT\_ENABLE\_VRR, 1);
    int32\_t ret = OH\_VideoDecoder\_Configure(videoDec, format);
    if (ret != AV\_ERR\_OK) {
        // Handle exceptions.
    }
    OH\_AVFormat\_Destroy(format);
    
2.  (Optional) Dynamically enable or disable the variable frame rate feature during video playback.
    
    If bullet comments are enabled during playback, you can disable the variable frame rate feature to avoid wasting resources, since the refresh rate adjustments are not applied.
    
    The following code snippet is used to dynamically disable the feature:
    
    OH\_AVFormat \*format = OH\_AVFormat\_Create();
    OH\_AVFormat\_SetIntValue(format, OH\_MD\_KEY\_VIDEO\_DECODER\_OUTPUT\_ENABLE\_VRR, 0);
    OH\_VideoDecoder\_SetParameter(videoDec, format);
    OH\_AVFormat\_Destroy(format);
    
    The following code snippet is used to dynamically enable the feature:
    
    OH\_AVFormat \*format = OH\_AVFormat\_Create();
    OH\_AVFormat\_SetIntValue(format, OH\_MD\_KEY\_FRAME\_RATE, fps);
    OH\_AVFormat\_SetIntValue(format, OH\_MD\_KEY\_VIDEO\_DECODER\_OUTPUT\_ENABLE\_VRR, 1);
    OH\_VideoDecoder\_SetParameter(videoDec, format);
    OH\_AVFormat\_Destroy(format);
