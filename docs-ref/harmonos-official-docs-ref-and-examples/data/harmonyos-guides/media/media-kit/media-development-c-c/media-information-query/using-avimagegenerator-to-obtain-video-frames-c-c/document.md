# Using AVImageGenerator to Obtain Video Frames (C/C++)

You can use the AVImageGenerator to obtain the video frame at the specified time from the raw media asset.

The full process of obtaining the video frame includes creating an AVImageGenerator instance, setting resources, obtaining the video frame, and releasing the instance.

#### How to Develop

Link the dynamic libraries in the CMake script.

target\_link\_libraries(entry PUBLIC libavimage\_generator.so libace\_napi.z.so)

To use [OH\_PixelmapNative\_ConvertPixelmapNativeToNapi()](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-pixelmap-native-h#oh_pixelmapnative_convertpixelmapnativetonapi) to convert a nativePixelMap object into a PixelMapnapi object and use [OH\_PixelmapNative\_Release()](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-pixelmap-native-h#oh_pixelmapnative_release) to release the OH\_PixelmapNative object, include the following header file:

#include <multimedia/image\_framework/image/pixelmap\_native.h>

In addition, link the following dynamic libraries in the CMake script:

target\_link\_libraries(entry PUBLIC libpixelmap.so libpixelmap\_ndk.z.so)

To use system logging, include the following header file:

#include <hilog/log.h>

In addition, link the following dynamic libraries in the CMake script:

target\_link\_libraries(entry PUBLIC libhilog\_ndk.z.so)

(Optional) You can use [OH\_AVMetadataExtractor\_FetchMetadata()](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-avmetadata-extractor-h#oh_avmetadataextractor_fetchmetadata) to obtain the duration information of the media resource (OH\_AVMETADATA\_EXTRACTOR\_DURATION, ../../reference/apis-media-kit/capi-avmetadata-extractor-base-h.md#variables), and specify the time to obtain a video frame. Include the following header files:

#include "multimedia/player\_framework/avmetadata\_extractor.h"
#include "multimedia/player\_framework/avmetadata\_extractor\_base.h"

In addition, link the following dynamic libraries in the CMake script:

target\_link\_libraries(entry PUBLIC libavmetadata\_extractor.so libnative\_media\_core.so)

You can use the APIs related to video frame retrieval by including the header files [avimage\_generator.h](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-avimage-generator-h), [avimage\_generator\_base.h](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-avimage-generator-base-h), and [native\_averrors.h](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-native-averrors-h).

Read [AVImageGenerator](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-avimagegenerator) for the API reference.

1.  Call [OH\_AVImageGenerator\_Create()](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-avimage-generator-h#oh_avimagegenerator_create) to create an instance.
    
    #include <multimedia/player\_framework/avimage\_generator.h>
    // Create an OH\_AVImageGenerator instance.
    OH\_AVImageGenerator\* generator = OH\_AVImageGenerator\_Create();
    
2.  Call [OH\_AVImageGenerator\_SetFDSource()](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-avimage-generator-h#oh_avimagegenerator_setfdsource) to set the file descriptor of a video resource.
    
    #include "napi/native\_api.h"
    #include <multimedia/player\_framework/avimage\_generator.h>
    #include <multimedia/player\_framework/native\_averrors.h>
    
    int64\_t offset = 0; // Offset of the media source in the file descriptor.
    int32\_t fileDescribe = -1; // File descriptor of the media file.
    int32\_t fileSize = 0; // Size of the media file.
        
    // Set the file descriptor of the video resource.
    OH\_AVErrCode avErrCode = OH\_AVImageGenerator\_SetFDSource(generator, fileDescribe, offset, fileSize);
    // Handle exceptions.
    if (avErrCode != AV\_ERR\_OK) {
        OH\_AVImageGenerator\_Release(generator);
        napi\_throw\_error(env, "EFAILED", "SetFDSource failed");
        return nullptr;
    }
    
3.  (Optional) Obtain the duration information of the media resource and specify the time to obtain the video frame.
    
    #include "napi/native\_api.h"
    #include "multimedia/player\_framework/avmetadata\_extractor.h"
    #include "multimedia/player\_framework/avmetadata\_extractor\_base.h"
    static napi\_value OhAVMetadataExtractorGetDuration(napi\_env env, napi\_callback\_info info)
    {
        int64\_t offset = 0;
        int32\_t fileDescribe = -1;
        int64\_t fileSize = 0;
        // Use helper functions to obtain input parameters. For details, see the complete example.
        if (!GetGetDurationParams(env, info, offset, fileDescribe, fileSize)) {
            return nullptr;
        }
        OH\_AVMetadataExtractor\* mainExtractor = OH\_AVMetadataExtractor\_Create();
        if (!mainExtractor) {
            napi\_throw\_error(env, "EFAILED", "Create metadata extractor failed");
            return nullptr;
        }
        OH\_AVErrCode avErrCode = OH\_AVMetadataExtractor\_SetFDSource(mainExtractor, fileDescribe, offset, fileSize);
        if (avErrCode != AV\_ERR\_OK) {
            OH\_AVMetadataExtractor\_Release(mainExtractor);
            napi\_throw\_error(env, "EFAILED", "SetFDSource for metadata extractor failed");
            return nullptr;
        }
        OH\_AVFormat\* avMetadata = OH\_AVFormat\_Create();
        // Obtain the metadata of the resource file.
        avErrCode = OH\_AVMetadataExtractor\_FetchMetadata(mainExtractor, avMetadata);
        if (avErrCode != AV\_ERR\_OK) {
            OH\_AVFormat\_Destroy(avMetadata);
            OH\_AVMetadataExtractor\_Release(mainExtractor);
            napi\_throw\_error(env, "EFAILED", "Fetch metadata failed");
            return nullptr;
        }
        int64\_t out;
        // Obtain the duration of the resource file from the metadata.
        if (!OH\_AVFormat\_GetLongValue(avMetadata, OH\_AVMETADATA\_EXTRACTOR\_DURATION, &out)) {
            OH\_AVFormat\_Destroy(avMetadata);
            OH\_AVMetadataExtractor\_Release(mainExtractor);
            napi\_throw\_error(env, "EFAILED", "Get duration failed");
            return nullptr;
        }
        napi\_value duration;
        napi\_create\_int64(env, out, &duration);
        OH\_AVFormat\_Destroy(avMetadata);
        OH\_AVMetadataExtractor\_Release(mainExtractor);
        return duration;
    }
    
4.  Call [OH\_AVImageGenerator\_FetchFrameByTime()](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-avimage-generator-h#oh_avimagegenerator_fetchframebytime) to obtain the video frame at a specified time, which is an OH\_PixelmapNative object.
    
    When the object is no longer required, call **OH\_PixelmapNative\_Release** to release the object. For details, see [Image\_NativeModule](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-pixelmap-native-h#oh_pixelmapnative_release).
    
    #include "napi/native\_api.h"
    #include <multimedia/image\_framework/image/pixelmap\_native.h>
    #include <multimedia/player\_framework/avimage\_generator.h>
    #include <multimedia/player\_framework/avimage\_generator\_base.h>
    #include <multimedia/player\_framework/native\_averrors.h>
    
    // Input parameters for FetchFrameByTime.
    struct FetchFrameParams {
        int64\_t timeUs = 0; // Specified time (in us).
        int64\_t offset = 0; // Offset of the media source in the file descriptor.
        int32\_t fileDescribe = -1; // File descriptor of the media file.
        int32\_t fileSize = 0; // Size of the media file.
        int32\_t options = OH\_AVIMAGE\_GENERATOR\_QUERY\_CLOSEST; // OH\_AVIMAGE\_GENERATOR\_QUERY\_CLOSEST means that the key frame closest to the specified time is selected.
    };
    
    static napi\_value OhAvImageGeneratorFetchFrameByTime(napi\_env env, napi\_callback\_info info)
    {
        FetchFrameParams fetchFrameParams;
        // Use helper functions to obtain input parameters. For details, see the complete example.
        if (!GetFetchFrameByTimeParams(env, info, fetchFrameParams)) {
            return nullptr;
        }
        int64\_t timeUs = fetchFrameParams.timeUs;
        int64\_t offset = fetchFrameParams.offset;
        int32\_t fileDescribe = fetchFrameParams.fileDescribe;
        int32\_t fileSize = fetchFrameParams.fileSize;
        int32\_t options = fetchFrameParams.options;
        // Create an OH\_AVImageGenerator instance.
        OH\_AVImageGenerator\* generator = OH\_AVImageGenerator\_Create();
        // Handle exceptions.
        if (!generator) {
            napi\_throw\_error(env, "EFAILED", "Create generator failed");
            return nullptr;
        }
        // Set the file descriptor of the video resource.
        OH\_AVErrCode avErrCode = OH\_AVImageGenerator\_SetFDSource(generator, fileDescribe, offset, fileSize);
        // Handle exceptions.
        if (avErrCode != AV\_ERR\_OK) {
            OH\_AVImageGenerator\_Release(generator);
            napi\_throw\_error(env, "EFAILED", "SetFDSource failed");
            return nullptr;
        }
        // Obtain the video frame at a specified time.
        OH\_PixelmapNative\* pixelMap = nullptr;
        avErrCode = OH\_AVImageGenerator\_FetchFrameByTime(generator, timeUs,
            (OH\_AVImageGenerator\_QueryOptions)options, &pixelMap);
        // Handle exceptions.
        if (avErrCode != AV\_ERR\_OK || !pixelMap) {
            OH\_AVImageGenerator\_Release(generator);
            napi\_throw\_error(env, "EFAILED", "FetchFrameByTime failed");
            return nullptr;
        }
        // Convert the nativePixelMap object into a PixelMapnapi object.
        napi\_value pixelmapNapi = nullptr;
        Image\_ErrorCode errCode = OH\_PixelmapNative\_ConvertPixelmapNativeToNapi(env, pixelMap, &pixelmapNapi);
        // Release the OH\_PixelmapNative resource.
        OH\_PixelmapNative\_Release(pixelMap);
        // Release the OH\_AVImageGenerator resource.
        OH\_AVImageGenerator\_Release(generator);
        // Handle exceptions.
        if (errCode != IMAGE\_SUCCESS) {
            napi\_throw\_error(env, "EFAILED", "Convert PixelMap failed");
            return nullptr;
        }
        return pixelmapNapi;
    }
    
5.  Call [OH\_AVImageGenerator\_Release()](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-avimage-generator-h#oh_avimagegenerator_release) to destroy the instance and release resources.
    
    // Release the OH\_AVImageGenerator resource.
    OH\_AVImageGenerator\_Release(generator);
    

#### Running the Sample Project

Refer to the sample project to obtain the video frame at a specified time.

1.  Create a project, download the [sample project](https://gitcode.com/openharmony/applications_app_samples/tree/master/code/DocsSample/Media/AVImageGenerator/AVImageGeneratorNDK), and copy its resources to the corresponding directories.
    
    AVImageGeneratorNDK
    entry/src/main/ets/
    └── pages
        └── Index.ets (Thumbnail retrieval UI)
    entry/src/main/
    ├── cpp
    │   ├── types
    │   │   └── libentry
    │   │       └── Index.d.ts (JavaScript mapping of NDK functions)
    │   ├── CMakeLists.txt (CMake script)
    │   └── napi\_init.cpp (NDK functions)
    └── resources
        ├── base
        │   ├── element
        │   │   ├── color.json
        │   │   ├── float.json
        │   │   └── string.json
        │   └── media
        │
        └── rawfile
            └── H264\_AAC.mp4 (Video resource)
    
2.  Compile and run the project.
