# About This Kit

With the APIs provided by Camera Kit, you can develop a camera application. The application accesses and operates the camera device to implement basic operations, such as preview, photo capture, and video recording. It can also combine APIs to perform advanced operations such as controlling flash and exposure time, focusing, or zooming.

#### When to Use

When you want to develop a camera application or develop a camera module in an application, you can refer to the development model described below to understand the working process of the camera before the development.

If you only need to start the system camera to take a photo or record a video, you can directly use the CameraPicker module, without applying for the camera permission. For details, see [Camera Picker](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-camerapicker).

#### Development Model

The camera application invokes the camera device to collect and process image and video data, and output images and videos. It can be used when there are multiple lenses (such as wide-angle lens, long-focus lens, and ToF lens) in various service scenarios (such as different requirements on the resolution, format, and effect).

The workflow for camera application development is shown in Figure 1, which can be summarized into three parts: camera device management, camera session management, and camera output management.

-   A camera application invokes the camera device to collect data, which serves as the camera input stream.
    
-   Camera session management allows configuration of the input stream, for example, selecting the appropriate camera lens (front or rear camera) for shooting. You can also set parameters, such as the flash, exposure time, focus, and focus adjustment, to implement different shooting effects in various service scenarios. The application can switch between sessions to meet service requirements in different scenarios.
    
-   Camera output management configures the output streams of the camera, that is, outputting image content as preview streams, photo streams, or video streams.
    

**Figure 1** Camera working process

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fd/v3/fjZ5jgcORV-UUSvZCpGVFQ/en-us_image_0000002568764897.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062037Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=CAD77C60D4DEAAD20CC22045F6DBAA1A781CDB38E460FBAD73F63CA909FC4F87)

To help you better develop camera applications, you are advised to first understand the camera development workflow, then learn about the camera development model (as shown in Figure 2).

The camera application controls the camera device to implement basic operations such as image display (preview), photo saving (photo capture), and video recording. During the implementation of these basic operations, the camera service controls the camera device to collect and output data. The collected image data is processed by the Image Signal Processor (ISP) and then directly transmitted to specific functional modules for processing through the Hardware Device Interfaces (HDI) of the underlying camera layer, using a buffer queue. You do not need to focus on the buffer queue during application development; it is used to promptly deliver the underlying processed data to the upper layer for image display.

Take video recording as an example: the camera service can control the camera device to collect video data and generate a video stream. After the collected data is processed by the underlying camera HDI, the video stream is transmitted to the media recording service via Surface, and finally the media recording service processes the video data and saves it as a video file to complete video recording.

**Figure 2** Camera development model

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a7/v3/GiywI2nvQ4K8KG3m_a2fWQ/en-us_image_0000002537765172.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062037Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=D3FA5ABD87C9512E27462C73D9E73DFF2C4C3847F0A82601553DF49F7A0CA744)
