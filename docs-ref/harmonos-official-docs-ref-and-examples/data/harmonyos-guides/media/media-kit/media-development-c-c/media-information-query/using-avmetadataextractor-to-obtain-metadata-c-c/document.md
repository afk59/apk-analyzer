# Using AVMetadataExtractor to Obtain Metadata (C/C++)

You can use the AVMetadataExtractor to obtain metadata from a raw media asset. This topic walks you through on how to obtain the metadata of a media asset.

The full process of obtaining the metadata of a media asset includes creating an AVMetadataExtractor instance, setting resources, obtaining the metadata, and releasing the instance.

#### How to Develop

Link the dynamic library in the CMake script.

target\_link\_libraries(entry PUBLIC libavmetadata\_extractor.so libace\_napi.z.so )

To use [OH\_AVFormat](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-native-avformat-h) APIs, include the following header file:

#include <multimedia/player\_framework/native\_avformat.h>

In addition, link the following dynamic library in the CMake script:

target\_link\_libraries(entry PUBLIC libnative\_media\_core.so)

To use [OH\_PixelmapNative\_ConvertPixelmapNativeToNapi()](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-pixelmap-native-h#oh_pixelmapnative_convertpixelmapnativetonapi) to convert a nativePixelMap object into a PixelMapnapi object and use [OH\_PixelmapNative\_Release()](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-pixelmap-native-h#oh_pixelmapnative_release) to release the OH\_PixelmapNative object, include the following header file:

#include <multimedia/image\_framework/image/pixelmap\_native.h>

In addition, link the following dynamic library in the CMake script:

target\_link\_libraries(entry PUBLIC libpixelmap.so libpixelmap\_ndk.z.so)

To use system logging, include the following header file:

#include <hilog/log.h>

In addition, link the following dynamic library in the CMake script:

target\_link\_libraries(entry PUBLIC libhilog\_ndk.z.so)

You can use the APIs related to metadata retrieval by including the header files [avmetadata\_extractor.h](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-avmetadata-extractor-h), [avmetadata\_extractor\_base.h](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-avmetadata-extractor-base-h), and [native\_averrors.h](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-native-averrors-h).

Read [AVMetadataExtractor](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-avmetadataextractor) for the API reference.

1.  Call [OH\_AVMetadataExtractor\_Create()](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-avmetadata-extractor-h#oh_avmetadataextractor_create) to create an instance.
    
    #include <multimedia/player\_framework/avmetadata\_extractor.h>
    // Create an OH\_AVMetadataExtractor instance.
    OH\_AVMetadataExtractor\* mainExtractor = OH\_AVMetadataExtractor\_Create();
    
2.  Call [OH\_AVMetadataExtractor\_SetFDSource()](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-avmetadata-extractor-h#oh_avmetadataextractor_setfdsource) to set the file descriptor of a media resource.
    
    If different AVMetadataExtractor or [AVImageGenerator](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-avimagegenerator) instances need to operate the same resource, the file descriptor needs to be opened for multiple times. Therefore, do not share a file descriptor.
    
    #include "napi/native\_api.h"
    #include <multimedia/player\_framework/avmetadata\_extractor.h>
    int64\_t offset = 0; // Offset of the media source in the file descriptor.
    int32\_t fileDescribe = -1; // File descriptor of the media file.
    int32\_t fileSize = 0; // Size of the media file.
    
    // GetInputParams is a helper function used to obtain the input parameters of FetchAlbumCover and FetchMetadata. For details, see the complete example.
    if (!GetInputParams(env, info, offset, fileDescribe, fileSize)) {
        return nullptr;
    }
     // Set the file descriptor of the media resource.
    OH\_AVErrCode avErrCode = OH\_AVMetadataExtractor\_SetFDSource(mainExtractor, fileDescribe, offset, fileSize);
    // Handle exceptions.
    if (avErrCode != AV\_ERR\_OK) {
        OH\_AVMetadataExtractor\_Release(mainExtractor);
        napi\_throw\_error(env, "EFAILED", "SetFDSource for metadata extractor failed");
        return nullptr;
    }
    
3.  Call [OH\_AVMetadataExtractor\_FetchMetadata()](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-avmetadata-extractor-h#oh_avmetadataextractor_fetchmetadata) to obtain metadata.
    
    First, call **OH\_AVFormat\_Create()** to create an OH\_AVFormat object and obtain the metadata by accessing the key-value pairs of the object. When the object is no longer required, call **OH\_AVFormat\_Destroy** to release the object to prevent memory leakage. For details, see [OH\_AVFormat](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-native-avformat-h).
    
    // Obtain the metadata.
    avErrCode = OH\_AVMetadataExtractor\_FetchMetadata(mainExtractor, avMetadata);
    
4.  For a video resource, you can use **OH\_AVMetadataExtractor\_FetchMetadata** to obtain the metadata such as width and height from the OH\_AVFormat object, using functions like **OH\_AVFormat\_GetIntValue** and **GetStringValueFromAVFormat**.
    
    // Parse the width and height of the video resource from the OH\_AVFormat object as int32\_t.
    int32\_t width = 0;
    int32\_t height = 0;
    OH\_AVFormat\_GetIntValue(avMetadata, OH\_AVMETADATA\_EXTRACTOR\_VIDEO\_WIDTH, &width);
    OH\_AVFormat\_GetIntValue(avMetadata, OH\_AVMETADATA\_EXTRACTOR\_VIDEO\_HEIGHT, &height);
    
5.  For an audio resource, in addition to obtaining metadata such as the title and duration of the audio resource through the OH\_AVFormat object, you can retrieve the album cover by calling [OH\_AVMetadataExtractor\_FetchAlbumCover()](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-avmetadata-extractor-h#oh_avmetadataextractor_fetchalbumcover).
    
    When the object is no longer required, call **OH\_PixelmapNative\_Release** to release the object. For details, see [Image\_NativeModule](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-pixelmap-native-h#oh_pixelmapnative_release).
    
    #include <multimedia/image\_framework/image/pixelmap\_native.h>
    #include <multimedia/player\_framework/avmetadata\_extractor.h>
    
    #include <hilog/log.h>
    // Obtain the album cover.
    OH\_PixelmapNative\* pixelMap = nullptr;
    avErrCode = OH\_AVMetadataExtractor\_FetchAlbumCover(mainExtractor, &pixelMap);
    
6.  Call [OH\_AVMetadataExtractor\_Release()](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-avmetadata-extractor-h#oh_avmetadataextractor_release) to destroy the instance and release resources.
    
    // Release the OH\_AVMetadataExtractor resource.
    OH\_AVMetadataExtractor\_Release(mainExtractor);
    

#### Running the Sample Project

Refer to the sample project to obtain audio metadata and album cover.

1.  Create a project, download the [sample project](https://gitcode.com/openharmony/applications_app_samples/tree/master/code/DocsSample/Media/AVMetadataExtractor/AVMetadataExtractorNDK), and copy its resources to the corresponding directories.
    
    AVMetadataExtractorNDK
    entry/src/main/ets/
    └── pages
        └── Index.ets (metadata retrieval UI)
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
            └── test.mp3 (audio resource)
    
2.  Compile and run the project.
