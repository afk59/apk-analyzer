# ROI Video Encoding

#### Basic Concepts

Region of Interest (ROI) video encoding has been supported since API version 20. This feature is an advanced optimization technology extended based on the hardware H.264/H.265 encoding capability. Its core logic is to allocate more encoding resources to the specified key regions in the frame to achieve high-quality encoding. It ensures the clear presentation of content in ROI regions under limited bandwidth, which significantly enhances the overall visual experience.

You can define ROI regions in the video frame (for example, human faces in live streaming, license plates in video security, etc.), and adjust the encoding quality difference between ROI and non-ROI regions by setting quality offset parameters, thus realizing the differentiated allocation of encoding resources.

#### When to Use

ROI video encoding applies to scenarios where the bit rate cannot meet the video quality requirements due to limited network bandwidth, and the key frame content (ROI regions) can be clearly defined. Examples include video calls, live video streaming, video security, and more.

Recommended ROI regions for each scenario are as follows:

-   Live fashion shows: Set the anchor's facial region as the ROI to optimize facial details (e.g., skin tone and facial feature contours), enhancing the audience's immersive viewing experience.
-   Outdoor live streaming: Set the anchor's main body/core shooting scenes (for example, natural scenery and core areas of sports event footage) as the ROI to ensure the clarity of core content when the mobile network bandwidth fluctuates.
-   E-commerce live streaming: Set the product display area (for example, makeup color testing and electronic product details) as the ROI to clearly present the product's appearance, material, and functional details, helping to improve product conversion rates.
-   Online course videos: Set the areas of courseware text, lecture notes charts, and blackboard writing content as the ROI to ensure the clear readability of knowledge points, reduce visual fatigue, and improve teaching effectiveness.
-   Video security: Set key regions in the camera frame (for example, human faces, license plates, entrances and exits) as the ROI to improve the clarity of capture, facilitating subsequent identification and analysis.

To support different encoding scenarios, three types of ROI encoding development samples are provided. You can select samples based on the actual service and technical architecture.

| Scenario | Live Streaming/Video Call | Video Recording | Editing & Export/Content Publishing |
| :-- | :-- | :-- | :-- |
| **ROI information producer** | Camera | Camera | Application |
| **ROI information obtaining method** | Obtained via camera metadata callback | Obtained via camera metadata callback | Self-managed by the application |
| **Direct producer of encoded video frames** | Graphics | Camera | Application |
| **Encoding mode** | Surface mode | Surface mode | Buffer mode |
| **ROI management & alignment method** | Matched based on timestamp | Matched based on callback timing | Self-selected |
| **ROI parameter configuration method** | NativeBuffer metadata configuration | Encoding input parameter callback configuration | Encoding input buffer callback configuration |
| **Example** | [Configuring ROI via the NativeBuffer API in Surface Mode](#configuring-roi-via-the-nativebuffer-api-in-surface-mode) | [Configuring ROI via the Encoding Input Callback API in Surface Mode](#configuring-roi-via-the-encoding-input-callback-api-in-surface-mode) | [Configuring ROI in Buffer Mode](#configuring-roi-in-buffer-mode) |

#### Constraints

**Supported encoders**: H.264 8-bit hardware encoding, H.265 8-bit hardware encoding, and H.265 10-bit hardware encoding

Supported bit rate control modes: variable bit rate (VBR), constant bit rate (CBR) and stable quality rate control (SQR)

**ROI detection and identification capability dependency**: The encoder does not have built-in ROI detection and recognition capability, so the effectiveness of ROI encoding technology relies on the ROI information input by developers. You can design and implement ROI recognition capability according to service scenarios, or reduce development costs by calling the face region information provided by the system camera module. For details, see the [camera face ROI acquisition example](../../../camera-kit/fundamental-capabilities-for-camera-application-development-c-c/camera-metadata-c-c/document.md#status-listening).

#### Parameter Requirements

You candeliver ROI parameters in the form of strings, which must comply with the format: "Top,Left-Bottom,Right=DeltaQp". All parameters are integers.

-   An ROI is a rectangular region. **Top**, **Left**, **Bottom**, and **Right** define the coordinates of the top-left and bottom-right corners of the ROI region in the image (as shown in figure 1).
-   **DeltaQp** specifies the difference value of the encoding quantization parameter (QP). The larger the absolute value of **DeltaQp**, the greater the difference in encoding quality between the ROI region and non-ROI regions. A negative **DeltaQp** indicates that the encoding quality of the ROI region is better than that of non-ROI regions. The segment "**\=DeltaQp**" can be omitted; if omitted, the default parameter (**\=-3**) will be used.
-   Multiple ROI parameters are connected by semicolons (;). An example of multi-ROI configuration is: **"Top1,Left1-Bottom1,Right1=DeltaQp1;Top2,Left2-Bottom2,Right2=DeltaQp2"**.
-   A maximum of 6 ROI regions are supported per frame. Excess ROI regions will be ignored in the order of configuration. The total area of ROIs must not exceed 1/5 of the image area. The areas are accumulated in the order of configuration, and only the ROI regions whose accumulated area is within the limit will take effect.

**Figure 1: ROI coordinates and maximum allowed area ratio**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/60/v3/SjwFzANWQ5WLDkMhXEuE5g/en-us_image_0000002537925106.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062036Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=37C02DEC28FD452C01E1C433DB12DEC67901183162CD249F671B18B1B560B2A3)

#### Effectiveness Mechanism

Two methods are supported for ROI configuration: **NativeBuffer metadata configuration** and **encoding input callback configuration**. The encoding input callback configuration method includes encoding input parameter callback (Surface mode) and encoding input buffer callback (Buffer mode).

-   (Recommended) NativeBuffer metadata configuration: Starting from API version 22, the ROI enumeration **OH\_REGION\_OF\_INTEREST\_METADATA** of **OH\_NativeBuffer\_MetaDataKey** can be used to configure ROI parameters in the NativeBuffer metadata.
-   Encoding input callback configuration method: The video encoding parameter **OH\_MD\_KEY\_VIDEO\_ENCODER\_ROI\_PARAMS** is used to configure ROI parameters in the encoding input callback.

**General effectiveness mechanism:**

1.  ROI parameters support frame-by-frame delivery and take effect in real time. You do not need to query capabilities or configure global switches.
2.  If the system encoder does not support ROI encoding, the encoder ignores ROI parameters and performs normal encoding.
3.  The valid range of **DeltaQp** is \[-51, 51\]. The encoder overlays **DeltaQp** on the QP of the ROI region, and then limit the result to the range \[minQp, maxQp\] to obtain the final QP.
4.  When no ROI parameters are configured for a frame, if ROI encoding takes effect for the previous frame, the ROI information of the previous frame is reused for ROI encoding of the current frame. If normal encoding is used for the previous frame, normal encoding is performed for the current frame.
5.  If the ROI parameters configured for a frame fail to parse any valid ROI information, normal encoding will be performed.
6.  If multiple ROI regions overlap, only the first configured ROI region will take effect at the overlapping area in the order of configuration.

**Unique mechanism of NativeBuffer metadata configuration method**: A maximum of 256 bytes of character length is supported; the excess part will be truncated.

**Differences in empty string processing:**

-   NativeBuffer metadata configuration method: Empty strings are not allowed to be configured. An empty string is regarded as no ROI parameters configured, and the current frame will inherit the historical frame information for ROI encoding.
-   Encoding input callback configuration method: Empty strings are allowed to be configured, but since no valid ROI information can be parsed, normal encoding will be performed actually.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/89/v3/cXH5TvgFSImgSEXtTbS9-A/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062036Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=23C662C4A0D6930D22D514C63665B54E04B167B67DDED605E5DF7DB62907FE98)

Due to the differences in empty string processing, you are advised not to configure empty strings. If you need to disable ROI encoding for a frame, you can configure a string without position information (for example, **"Clear"** or **";"**).

**Effectiveness priority**: If ROI parameters are configured via both methods for a frame, only the ROI parameters delivered via the encoding input callback configuration method will take effect, regardless of whether valid ROI information can be parsed from them.

#### Development Example

## Configuring ROI via the NativeBuffer API in Surface Mode

The API for the system camera to obtain video frames and the API to obtain ROI information are two independent callback APIs. Data synchronization and matching must be performed based on the video timestamp and the ROI information timestamp, and ROI configuration for the corresponding frame must be completed before encoding.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/58/v3/WEpMzDJ6QZmNGsJEb8XApw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062036Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=CD92DE6250C1544C6DE2E3B4DDA06A290520EB5B85888314035759DD33C0FB80)

ROI information must be strictly aligned with the camera video frame information. In actual applications, if the two APIs are not processed synchronously, it may lead to misalignment of ROI calls. In high-load scenarios, an exception may also occur where the ROI timestamps of two consecutive frames are the same. Even if the above situations occur, the encoding function is not affected. You can determine whether to continue ROI encoding based on the evaluated encoding quality.

In specific service scenarios, the video frames obtained by the camera will undergo a series of image processing, such as beautification, filtering, and enhancement (as shown in figure 2). You can add or delete modules based on the actual service requirements.

**Figure 2: ROI configuration process via the NativeBuffer metadata API**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e9/v3/Gp4JYVrMTQqN59yx8HAUVg/en-us_image_0000002568684883.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062036Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=38AD88DC4349C3AB82C2336604785BC450562CAE7505C04CDF6600305BD8D89F)

The development procedure is as follows:

1.  Link dynamic libraries in **CMakeList.txt**.
    
    set(BASE\_LIBRARY
        libnative\_media\_codecbase.so libnative\_media\_core.so libnative\_media\_venc.so libnative\_window.so
        libnative\_buffer.so libnative\_image.so libEGL.so libGLESv3.so
    )
    target\_link\_libraries(recorder PUBLIC ${BASE\_LIBRARY})
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5c/v3/17WfYERBSPCBG4gPZZi6eQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062036Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=04CECF2D4B0CCE4312D1CF9F4D6B05163BE68AF970A0B95DFB27C5F598460D66)
    
    Replace **recorder** with the actual target name of the CMake project.
    
2.  Listen for the camera metadata callback API to obtain the face position information.
    
    For details, see [Camera Metadata Status Listening](../../../camera-kit/fundamental-capabilities-for-camera-application-development-arkts/camera-metadata-arkts/document.md#status-listening).
    
    import { camera } from '@kit.CameraKit'
    import { BusinessError } from '@kit.BasicServicesKit'
    import recorder from 'librecorder.so';
    
    interface FaceBoundingBox {
        topLeftX: number;
        topLeftY: number;
        width: number;
        height: number;
    }
    
    onMetadataObjectsAvailable(metadataOutput: camera.MetadataOutput): void {
        metadataOutput.on('metadataObjectsAvailable', (err: BusinessError, metadataObjectArr: Array<camera.MetadataObject>) => {
            if (err !== undefined && err.code !== 0) {
                return;
            }
            const faceBoundingBoxes: Array<FaceBoundingBox> = \[\];
            let unifiedTimestamp = 0;
            let timestampSet = false;
     
            for (const metadataObject of metadataObjectArr) {
                if (metadataObject.type === camera.MetadataObjectType.FACE\_DETECTION) {
                    if (!timestampSet) {
                        unifiedTimestamp = metadataObject.timestamp;
                        timestampSet = true;
                    }
                    faceBoundingBoxes.push({
                        topLeftX: metadataObject.boundingBox.topLeftX,
                        topLeftY: metadataObject.boundingBox.topLeftY,
                        width: metadataObject.boundingBox.width,
                        height: metadataObject.boundingBox.height
                    })
                }
            }
            if (faceBoundingBoxes.length > 0) {
                // Deliver the face position information to the Native layer (this.nativeRecorderObj is a native-layer instance).
                recorder.UpdateFaceRect(this.nativeRecorderObj, unifiedTimestamp, faceBoundingBoxes);
            }
        });
    }
    
3.  The Native layer parses the face position information transferred by the TS layer.
    
    struct FaceRect {
        double topLeftX;
        double topLeftY;
        double width;
        double height;
    };
    
    static napi\_value UpdateFaceRect(napi\_env env, napi\_callback\_info info)
    {
        size\_t argc = 3;
        napi\_value args\[3\] = {nullptr};
        napi\_get\_cb\_info(env, info, &argc, args, nullptr, nullptr);
        if (argc < 3) {
            return nullptr;
        }
        // Parse the native instance.
        int64\_t addrValue = 0;
        bool flag = false;
        napi\_get\_value\_bigint\_int64(env, args\[0\], &addrValue, &flag);
        Recorder \*recorder = reinterpret\_cast<Recorder \*>(addrValue);
        if (recorder == nullptr) {
            return nullptr;
        }
        // Parse the timestamp.
        int64\_t timestamp = 0;
        napi\_get\_value\_int64(env, args\[1\], &timestamp);
        // Parse the face rectangle.
        napi\_value faceRectArray = args\[2\];
        bool isArray;
        napi\_is\_array(env, faceRectArray, &isArray);
        if (!isArray) {
            return nullptr;
        }
        uint32\_t arrayLength;
        napi\_get\_array\_length(env, faceRectArray, &arrayLength);
        std::vector<FaceRect> faceRectVec;
        for (uint32\_t i = 0; i < arrayLength; i++) {
            FaceRect item = {0};
            napi\_value faceRectObj;
            napi\_get\_element(env, faceRectArray, i, &faceRectObj);
            napi\_value propValue;
            napi\_get\_named\_property(env, faceRectObj, "topLeftX", &propValue);
            napi\_get\_value\_double(env, propValue, &item.topLeftX);
            napi\_get\_named\_property(env, faceRectObj, "topLeftY", &propValue);
            napi\_get\_value\_double(env, propValue, &item.topLeftY);
            napi\_get\_named\_property(env, faceRectObj, "width", &propValue);
            napi\_get\_value\_double(env, propValue, &item.width);
            napi\_get\_named\_property(env, faceRectObj, "topLeftX", &propValue);
            napi\_get\_value\_double(env, propValue, &item.height);
            faceRectVec.push\_back(item);
        }
        recorder->ConvertToRoi(timestamp, faceRectVec);
        return nullptr;
    }
    
4.  Convert the ROI information into a character string and save the string.
    
    #include <map>
    #include <mutex>
    #include <sstream>
    #include <string>
    
    const int width = 1920; // Video frame width.
    const int height = 1080; // Video frame height.
    const int qpOffset = -6; // QP offset.
    std::map<int64\_t, std::string> g\_roiStrMap; // Timestamp and ROI information mapping.
    std::mutex g\_roiMutex;
    
    void Recorder::ConvertToRoi(int64\_t timestamp, std::vector<FaceRect>\* faceRectVec)
    {
        std::string mergedRoiStr;
        // Traverse all faceRect objects.
        for (const auto& faceRect : faceRectVec) {
            // Convert normalized coordinates to pixel coordinates.
            int left = static\_cast<int32\_t>(faceRect.topLeftX \* width);
            int top = static\_cast<int32\_t>(faceRect.topLeftY \* height);
            int right = static\_cast<int32\_t>(faceRect.width \* width) + left;
            int bottom = static\_cast<int32\_t>(faceRect.height \* height) + top;
    
            // Concatenate the format string for the current face frame (top,left-bottom,right=QpOffset;).
            std::ostringstream oss;
            oss << mergedRoiStr; // Concatenate the existing segments.
            oss << top << "," << left << "-" << bottom << "," << right << "=" << qpOffset << ";";
            mergedRoiStr = oss.str();
        }
    
        if (!mergedRoiStr.empty()) {
            std::lock\_guard<std::mutex> lock(g\_roiMutex);
            // In this scenario, the video frame timestamp can be obtained for matching.
            g\_roiStrMap\[timestamp\] = mergedRoiStr;
        }
    }
    
5.  Look up the matching ROI information based on the video frame timestamp.
    
    Include required header files.
    
    #include <EGL/egl.h>
    #include <EGL/eglext.h>
    #include <GLES3/gl3.h>
    #include <GLES2/gl2ext.h>
    #include <native\_image/native\_image.h>
    
    Create a **NativeImage** instance to receive video frames.
    
    GLuint textureId;
    glGenTextures(1, &textureId);
    // Create a NativeImage instance and associate it with the texture.
    OH\_NativeImage\* image = OH\_NativeImage\_Create(textureId, GL\_TEXTURE\_EXTERNAL\_OES);
    
    Obtain the **NativeWindow** corresponding to the **NativeImage** instance as the target window of the camera preview stream, and register callback **OH\_OnFrameAvailableListener** via **OH\_NativeImage\_SetOnFrameAvailableListener** to obtain video frame updates.
    
    // Update the NativeImage instance after the callback.
    int32\_t ret = OH\_NativeImage\_UpdateSurfaceImage(image);
    if (ret != 0) {
        // Handle exceptions.
    }
    // Obtain the video frame timestamp.
    int64\_t imageTimeStamp = OH\_NativeImage\_GetTimestamp(image);
    // Use the video frame timestamp to find the ROI information.
    std::lock\_guard<std::mutex> lock(g\_roiMutex);
    auto it = g\_roiStrMap.find(imageTimeStamp);
    std::string noRoiStr = ";"; // Similar to metadata configuration, a non-empty invalid string can be configured to disable ROI encoding for the current video frame.
    std::string roiInfo = (it != g\_roiStrMap.end()) ? it->second : noRoiStr;
    
6.  Set the ROI information to the NativeBuffer metadata of the video frame.
    
    Include required header files.
    
    #include <multimedia/player\_framework/native\_avcodec\_videoencoder.h>
    #include <multimedia/player\_framework/native\_avcodec\_base.h>
    #include <native\_window/external\_window.h> 
    #include <native\_buffer/native\_buffer.h>
    
    After a series of EGL processing, the video frame texture used for encoding is generated. You need to use the **eglSwapBuffers** function to draw the texture into the input **NativeWindow** of the encoder. The following describes how to obtain the **NativeWindow**.
    
    OH\_AVCodec \*codec = OH\_VideoEncoder\_CreateByMime(OH\_AVCODEC\_MIMETYPE\_VIDEO\_HEVC);
    OHNativeWindow \*nativeWindow = nullptr;
    OH\_VideoEncoder\_GetSurface(codec, &nativeWindow);
    
    Obtain the latest NativeBuffer and configure ROI information before drawing. For details about the drawing process, see [OpenGL ES Example](https://developer.huawei.com/consumer/en/doc/harmonyos-references/opengles#example). Finally, send the drawn data to the encoder for encoding via **eglSwapBuffers**.
    
    int fenceFd = -1;
    OHNativeWindowBuffer \*winBuffer = nullptr;
    // Request a frame of OHNativeWindowBuffer from the surface.
    int32\_t ret = OH\_NativeWindow\_NativeWindowRequestBuffer(nativeWindow, &winBuffer, &fenceFd);
    if (ret != 0) {
        // Handle exceptions.
    }
    // Convert the OHNativeWindowBuffer to NativeBuffer.
    OH\_NativeBuffer \*nativeBuffer = nullptr;
    OH\_NativeBuffer\_FromNativeWindowBuffer(winBuffer, &nativeBuffer);
    // Configure the ROI information to the NativeBuffer metadata.
    int32\_t ret = OH\_NativeBuffer\_SetMetaDataValue(nativeBuffer,
        OH\_NativeBuffer\_MetaDataKey::OH\_REGION\_OF\_INTEREST\_METADATA, roiInfo.size,
        reinterpret\_cast<uint8\_t \*>(roiInfo.data()));
    if (ret != 0) {
        // Handle exceptions.
    }
    

## Configuring ROI via the Encoding Input Callback API in Surface Mode

In this scenario, video frames are directly sent to the encoder window (as shown in figure 3).

The timestamps of the video frames output by the camera and the metadata (if any) are close. After the callback for encoding input parameters is set, the callback is triggered when the encoder receives video frames. In the callback, if the ROI information is successfully obtained, the video frame contains the matched ROI information. If the obtaining times out, the video frame does not contain the matched ROI information.

**Figure 3: ROI configuration process via the encoding input parameter callback API**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ad/v3/NmR9Fsl2QLOyQEjXHnAlEA/en-us_image_0000002568764893.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062036Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=052A3912DD04029A19A37125E6B8FE8D0B882F4CFE283D1F0E7FA83B77EF64B4)

The development procedure is as follows:

1.  Link dynamic libraries in **CMakeList.txt**.
    
    set(BASE\_LIBRARY
        libnative\_media\_codecbase.so libnative\_media\_core.so libnative\_media\_venc.so
    )
    target\_link\_libraries(recorder PUBLIC ${BASE\_LIBRARY})
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/34/v3/UORbXNBUQzGqWJPUTddhUw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062036Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=807E6AB41F4A78E751F0D5E4DCF40FEACABFB2590AD51A7588C076D32FEEF35E)
    
    Replace **recorder** with the actual target name of the CMake project.
    
2.  Listen for the camera metadata callback API to obtain the face position information.
    
    Same as step 2 in [Configuring ROI via the NativeBuffer API in Surface Mode](#configuring-roi-via-the-nativebuffer-api-in-surface-mode).
    
3.  The Native layer parses the face position information transferred by the TS layer.
    
    Same as step 3 in [Configuring ROI via the NativeBuffer API in Surface Mode](#configuring-roi-via-the-nativebuffer-api-in-surface-mode).
    
4.  Convert the ROI information into a character string and save the string.
    
    The timestamp field of video frames is not included in the design of the encoding parameter callback. To facilitate subsequent alignment, it is necessary to use a thread-safe first-in-first-out (FIFO) queue to manage ROI information. The following is a reference implementation.
    
    // RoiFifoQueue.h
    #include <queue>
    #include <string>
    #include <mutex>
    #include <condition\_variable>
    #include <chrono>
    
    class RoiFifoQueue {
    public:
        void push(const std::string& roiStr) {
            std::lock\_guard<std::mutex> lock(mtx);
            roiQueue.push(roiStr);
            cv.notify\_one(); // Notify the thread that waits for the data.
        }
    
        bool pop(std::string& outRoiStr, const std::chrono::milliseconds& timeout) {
            std::unique\_lock<std::mutex> lock(mtx);
            if (!cv.wait\_for(lock, timeout, \[this\]() {
                return !roiQueue.empty() || isStopped;
            })) {
                return false; // No ROI information is returned if a timeout occurs.
            }
            if (isStopped || roiQueue.empty()) {
                return false;
            }
            outRoiStr = roiQueue.front();
            roiQueue.pop();
            return true;
        }
    
        void clear() {
            std::lock\_guard<std::mutex> lock(mtx);
            while (!roiQueue.empty()) {
                roiQueue.pop();
            }
        }
    
        void stop() {
            std::lock\_guard<std::mutex> lock(mtx);
            isStopped = true;
            cv.notify\_all(); // Wake up all waiting threads.
        }
    
        ~RoiFifoQueue() {
            stop();
        }
    };
    private:
        std::queue<std::string> roiQueue;    // Store the merged complete ROI string.
        std::mutex mtx;                      // Mutex lock to protect the queue.
        std::condition\_variable cv;          // Condition variable used for timeout waiting.
        bool isStopped = false;              // Stop flag.
    
    Convert the data into the ROI information format and store it in the queue.
    
    #include <sstream>
    #include "RoiFifoQueue.h"
    
    const int width = 1920; // Video frame width.
    const int height = 1080; // Video frame height.
    const int qpOffset = -6; // QP offset.
    RoiFifoQueue g\_roiStrQueue;
    
    void Recorder::ConvertToRoi(int64\_t timestamp, std::vector<FaceRect>\* faceRectVec)
    {
        std::string mergedRoiStr;
        // Traverse all faceRect objects.
        for (const auto& faceRect : faceRectVec) {
            // Convert normalized coordinates to pixel coordinates.
            int left = static\_cast<int32\_t>(faceRect.topLeftX \* width);
            int top = static\_cast<int32\_t>(faceRect.topLeftY \* height);
            int right = static\_cast<int32\_t>(faceRect.width \* width) + left;
            int bottom = static\_cast<int32\_t>(faceRect.height \* height) + top;
    
            // Concatenate the format string for the current face frame (top,left-bottom,right=QpOffset;).
            std::ostringstream oss;
            oss << mergedRoiStr; // Concatenate the existing segments.
            oss << top << "," << left << "-" << bottom << "," << right << "=" << qpOffset << ";";
            mergedRoiStr = oss.str();
        }
    
        if (!mergedRoiStr.empty()) {
            std::lock\_guard<std::mutex> lock(g\_roiMutex);
            // In this scenario, the video frame timestamp can be obtained for matching.
            g\_roiStrQueue.push(mergedRoiStr);
        }
    }
    
5.  Configure ROI information in the encoding input parameter callback.
    
    Include required header files.
    
    #include <multimedia/player\_framework/native\_avcodec\_videoencoder.h>
    #include <multimedia/player\_framework/native\_avcodec\_base.h>
    #include <multimedia/player\_framework/native\_avformat.h>
    #include <multimedia/player\_framework/native\_avbuffer.h>
    
    Create an encoder.
    
    OH\_AVCodec \*codec = OH\_VideoEncoder\_CreateByMime(OH\_AVCODEC\_MIMETYPE\_VIDEO\_HEVC);
    
    For details about the video encoding procedure, see [Synchronous Video Encoding](../video-encoding/document.md). The following describes only ROI encoding.
    
    const std::chrono::milliseconds ROI\_WAIT\_TIMEOUT = std::chrono::milliseconds(4); // 4 ms timeout.
    static void OnNeedInputParameter(OH\_AVCodec \*codec, uint32\_t index, OH\_AVFormat \*parameter, void \*userData)
    {
        (void)codec;
        (void)userData;
        std::string roiInfo = "";
        if (!g\_roiStrQueue.pop(roiInfo, ROI\_WAIT\_TIMEOUT)) {
            roiInfo = ";"; // Align with the NativeBuffer path.
        }
        // If ROI configuration is found, ROI encoding takes effect. Otherwise, normal encoding takes effect.
        OH\_AVFormat\_SetStringValue(parameter, OH\_MD\_KEY\_VIDEO\_ENCODER\_ROI\_PARAMS, roiInfo.c\_str());
        OH\_VideoEncoder\_PushInputParameter(codec, index);
    }
    
    // Register the per-frame parameter callback.
    OH\_VideoEncoder\_OnNeedInputParameter inParaCb = OnNeedInputParameter;
    OH\_VideoEncoder\_RegisterParameterCallback(codec, inParaCb, nullptr);
    

## Configuring ROI in Buffer Mode

In this scenario, video frames and ROI information are provided by the application, and encoding is performed in buffer mode. You can align the ROI with video frames based on the timestamp or callback timing, and configure ROI parameters in the encoding input buffer callback (as shown in figure 4).

**Figure 4: ROI configuration process via the encoding input buffer callback API**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/19/v3/deUrQ2eNSoKzGUMFfYmigw/en-us_image_0000002537765168.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062036Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=BB18D990F8EFA4B255024AE0A8308E1A422EF75A2DD57F13C2B41787A9535D3E)

The preparation procedure is the same as steps 1 to 4 in [Configuring ROI via the Encoding Input Callback API in Surface Mode](#configuring-roi-via-the-encoding-input-callback-api-in-surface-mode). The following only describes the configuration differences.

Configure ROI information in the encoding input buffer callback.

static void OnNeedInputBuffer(OH\_AVCodec \*codec, uint32\_t index, OH\_AVBuffer \*buffer, void \*userData)
{
    (void)codec;
    (void)userData;
    auto format = std::shared\_ptr<OH\_AVFormat>(OH\_AVBuffer\_GetParameter(buffer), OH\_AVFormat\_Destroy);
    if (format == nullptr) {
        // Handle exceptions.
    }
    std::string roiInfo = "";
    if (!g\_roiStrQueue.pop(roiInfo, ROI\_WAIT\_TIMEOUT)) {
        roiInfo = ";"; // Align with the NativeBuffer path.
    }
    OH\_AVFormat\_SetStringValue(format.get(), OH\_MD\_KEY\_VIDEO\_ENCODER\_ROI\_PARAMS, roiInfo.c\_str());

    // Video frame filling is required, which is omitted here.
    // Notify the encoder that the buffer input is complete.
    OH\_VideoEncoder\_PushInputBuffer(codec, index);
}

static void OnStreamChanged(OH\_AVCodec \*codec, OH\_AVFormat \*format, void \*userData)
{
    // Only the definition is provided here, and the implementation is omitted.
}

static void OnError(OH\_AVCodec \*codec, int32\_t errorCode, void \*userData)
{
    // Only the definition is provided here, and the implementation is omitted.
}

static void OnNewOutputBuffer(OH\_AVCodec \*codec, uint32\_t index, OH\_AVBuffer \*buffer, void \*userData)
{
    // Only the definition is provided here, and the implementation is omitted.
}

OH\_AVCodecCallback cb = {&OnError, &OnStreamChanged, &OnNeedInputBuffer, &OnNewOutputBuffer};
OH\_AVErrCode ret = OH\_VideoEncoder\_RegisterCallback(videoEnc, cb, nullptr);
