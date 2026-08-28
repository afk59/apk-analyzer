# Optimizing Memory for Image Decoding (C/C++)

When an application decodes images, it must allocate the necessary memory for the decoding process. This guide describes different types of memory and how to allocate them.

The application obtains a PixelMap through the decoding API and passes it to the **Image** component for display.

If the PixelMap consumes a significant amount of memory and relies on shared memory, the RenderScript main thread may face an extended texture upload time, leading to noticeable lag. To mitigate this, the graphics subsystem offers a Direct Memory Access (DMA) zero-copy feature, which helps eliminate this overhead during image rendering.

#### Memory Types

The memory types for the PixelMap are as follows:

-   SHARE\_MEMORY: shared memory. Texture upload is required.
-   DMA\_ALLOC: DMA memory. Texture upload is not required.

You can call [OH\_ImageSourceNative\_CreatePixelmapUsingAllocator](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-image-source-native-h#oh_imagesourcenative_createpixelmapusingallocator) to customize the memory allocation type for decoding.

## Differences Between SHARE\_MEMORY and DMA\_ALLOC

| Item | SHARE\_MEMORY | DMA\_ALLOC |
| :-- | :-- | :-- |
| Definition | Shared memory (such as ashmem/anonymous sharing) provided by the operating system, allowing multiple processes to read/write the same physical pages. | Buffers allocated for direct DMA access by peripherals, GPU, or display pipelines. Common implementations include dmabuf and SurfaceBuffer, designed for zero-copy operations. |
| Working principle | Processes access a shared memory region via the CPU. Transferring this data to GPU or display pipelines typically requires a copy. | Data is written directly to the buffer (for example, by a decoder via DMA), which the GPU or display pipelines can then access without any copying. |
| Use case | Inter-process or inter-thread data sharing (for example, exchanging intermediate results in algorithms or post-processing). | High-bandwidth data transfer scenarios such as hardware decoding of images/videos, camera preview, and display rendering. |
| CPU usage | The CPU is involved in managing and synchronizing shared memory (for example, locking and unlocking), which incurs additional overhead. | Extremely low CPU usage: The CPU is only involved in the configuration of the DMA controller, with no intervention in actual data transfer. |
| Hardware dependency | Dependent on the shared memory mechanism of the operating system. | Strongly dependent on the hardware DMA controller. |
| Memory allocation and access permissions | The system allocates physical or virtual memory areas for shared memory, with access requiring user or kernel mapping operations. | The DMA controller directly operates the physical memory, requiring pre-allocated DMA buffers (usually contiguous memory). |
| Advantages | High flexibility. Supports simultaneous data sharing by multiple threads or processes, facilitating image post-processing and collaboration. | High efficiency and low latency, suitable for transfer of large data volumes and continuous data blocks. |
| Disadvantages | Shared memory operations require additional synchronization mechanisms, increasing programming complexity and CPU load. | Hardware support is required, and the data transfer range is limited by DMA address space (usually requiring contiguous physical memory). |

## Advantages of Using DMA\_ALLOC Memory

-   **Reduced texture upload time**
    
    When SHARE\_MEMORY is used, image data needs to be copied to GPU memory through the CPU, increasing the texture upload time. With DMA\_ALLOC, data is directly stored in memory that is accessible by the GPU, avoiding the time-consuming copy process.
    
    -   SHARE\_MEMORY time consumption: Single-frame rendering of a 4K image takes about 20 ms.
    -   DMA\_ALLOC time consumption: The time of single-frame rendering for a 4K image can be reduced to about 4 ms. This optimization is particularly significant in scenarios involving the display of large images and frequent dynamic image loading.
-   **Reduced CPU load**
    
    DMA\_ALLOC allows the GPU to directly access decoded data, reducing the load caused by memory copying.
    

#### Default Memory Allocation Method

When [OH\_ImageSourceNative\_CreatePixelmap](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-image-source-native-h#oh_imagesourcenative_createpixelmap) is called for decoding, different memory allocation types are used in different scenarios.

DMA\_ALLOC is used in the following scenarios:

-   Decoding HDR images.
-   Decoding HEIF images.
-   Decoding JPEG images, when the original image's width and height are both between 1024 pixels and 8192 pixels, [PIXEL\_FORMAT](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-pixelmap-native-h#pixel_format) is **PIXEL\_FORMAT\_RGBA\_8888** or **PIXEL\_FORMAT\_NV21**, and the number of concurrent tasks in the system does not exceed 3.
-   Decoding images in other formats. The value of [desiredSize](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-image-nativemodule-oh-decodingoptions) must be greater than or equal to 512 \* 512 pixels (consider the original image size if **desiredSize** is not set), and the width must be a multiple of 64.

In all other cases, SHARE\_MEMORY is used.

#### Custom Memory Allocation Method

By default, the system selects the optimal memory allocation method for performance. In specific scenarios, applications can use a specified memory allocation method.

When you call [OH\_ImageSourceNative\_CreatePixelmapUsingAllocator](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-image-source-native-h#oh_imagesourcenative_createpixelmapusingallocator) for decoding, the system automatically selects hardware or software decoding based on the [decoding options](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-image-nativemodule-oh-decodingoptions) and [memory application type](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-image-source-native-h#image_allocator_type).

When creating a PixelMap, the system determines whether to use DMA\_ALLOC or SHARE\_MEMORY based on the user-specified allocator type.

## Restrictions

The current image decoding feature has the following restrictions on memory allocation modes:

-   HDR image decoding supports only DMA\_ALLOC.
-   Hardware decoding supports only DMA\_ALLOC.
-   SVG image decoding supports only SHARE\_MEMORY.

When [OH\_ImageSourceNative\_CreatePixelmapUsingAllocator](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-image-source-native-h#oh_imagesourcenative_createpixelmapusingallocator) is used for decoding, if the specified memory allocation mode does not match the image format or decoding method, an exception indicating a memory allocation failure is thrown.

If the allocation type is set to AUTO, the system determines whether to use DMA\_ALLOC or SHARE\_MEMORY based on the decoding and rendering time.

Different memory allocation strategies can result in differences in the stride of the image. For memory allocated by using DMA\_ALLOC, the stride must be used for operations such as editing on the PixelMap. The following describes how to obtain the stride.

## Obtaining the Stride

The stride describes the storage width of each row of pixel data of an image in memory. It is an important parameter in the image drawing process and is used to correctly locate the layout of the image data in the memory.

When memory is allocated using DMA\_ALLOC, the stride must meet the hardware alignment requirements.

-   The stride value must be an integer multiple of the number of bytes required by the hardware platform.
    
-   If the stride does not meet the alignment requirements, the system automatically pads the data.
    
    The stride value can be obtained by calling [OH\_PixelmapNative\_GetImageInfo](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-pixelmap-native-h#oh_pixelmapnative_getimageinfo).
    

1.  Call [OH\_PixelmapNative\_GetImageInfo](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-pixelmap-native-h#oh_pixelmapnative_getimageinfo) to obtain an OH\_Pixelmap\_ImageInfo object.
2.  Call [OH\_PixelmapImageInfo\_GetRowStride](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-pixelmap-native-h#oh_pixelmapimageinfo_getrowstride) to obtain the stride value.

The sample code for obtaining and operating the stride by the C APIs is as follows: Open the **src/main/cpp/CMakeLists.txt** file of the native project, add **libimage\_packer.so** and **libhilog\_ndk.z.so** (on which the log APIs depend) to the **target\_link\_libraries** dependency.

target\_link\_libraries(entry PUBLIC libhilog\_ndk.z.so libimage\_source.so libimage\_packer.so libpixelmap.so)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c0/v3/qIf94n5IRtOjWF5I4zVWAA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062041Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=52EC7005FD132EF8C04E89D95DC084ECC92B46F5D49CAF7C5A2A66AF009A4FE6)

Certain APIs are supported only in API version 20 or later. You should select an appropriate API version during development.

1.  Create the **GetJsResult** function to process the NAPI return value.
    
    // Process the NAPI return value.
    napi\_value GetJsResult(napi\_env env, int result)
    {
        napi\_value resultNapi = nullptr;
        napi\_create\_int32(env, result, &resultNapi);
        return resultNapi;
    }
    
2.  Obtain and operate the stride value.
    
    #include <cstring>
    #include <hilog/log.h>
    #include <multimedia/image\_framework/image/image\_common.h>
    #include <multimedia/image\_framework/image/pixelmap\_native.h>
    #include <multimedia/image\_framework/image/image\_source\_native.h>
    // ...
    
    // Return the number of bytes per pixel based on the pixel format.
    int32\_t GetPixelFormatBytes(int32\_t pixelFormat)
    {
        switch (pixelFormat) {
            case PIXEL\_FORMAT\_RGB\_565:
                return 2; // 2 bytes per pixel.
            case PIXEL\_FORMAT\_RGBA\_8888:
            case PIXEL\_FORMAT\_BGRA\_8888:
                return 4; // 4 bytes per pixel.
            case PIXEL\_FORMAT\_RGB\_888:
                return 3; // 3 bytes per pixel.
            case PIXEL\_FORMAT\_ALPHA\_8:
                return 1; // 1 byte per pixel.
            case PIXEL\_FORMAT\_RGBA\_F16:
                return 8; // 8 bytes per pixel (since there are 16-bit floating-point number per channel and 4 channels in total).
            case PIXEL\_FORMAT\_NV21:
            case PIXEL\_FORMAT\_NV12:
                // The NV21 and NV12 formats are YUV 4:2:0 semi-planar formats. 2 is returned as the number of bytes per pixel.
                return 2; // 2 bytes per pixel (simplified processing).
            case PIXEL\_FORMAT\_RGBA\_1010102:
                return 4; // 4 bytes per pixel.
            case PIXEL\_FORMAT\_YCBCR\_P010:
            case PIXEL\_FORMAT\_YCRCB\_P010:
                return 2; // 2 bytes per pixel.
            default:
                return 0; // If the pixel format is unknown, 0 is returned.
        }
    }
    
    struct PixelmapInfo {
        uint32\_t width = 0;
        uint32\_t height = 0;
        uint32\_t rowStride = 0;
        int32\_t pixelFormat = 0;
        uint32\_t byteCount = 0;
        uint32\_t allocationByteCount = 0;
    };
    
    static void GetPixelmapInfo(OH\_PixelmapNative \*pixelmap, PixelmapInfo \*info)
    {
        OH\_Pixelmap\_ImageInfo \*srcInfo = nullptr;
        OH\_PixelmapImageInfo\_Create(&srcInfo);
        OH\_PixelmapNative\_GetImageInfo(pixelmap, srcInfo);
        OH\_PixelmapImageInfo\_GetWidth(srcInfo, &info->width);
        OH\_PixelmapImageInfo\_GetHeight(srcInfo, &info->height);
        OH\_PixelmapImageInfo\_GetRowStride(srcInfo, &info->rowStride);
        OH\_PixelmapImageInfo\_GetPixelFormat(srcInfo, &info->pixelFormat);
        OH\_PixelmapImageInfo\_Release(srcInfo);
        srcInfo = nullptr;
        return;
    }
    
    static void GetPixelmapAddrInfo(OH\_PixelmapNative \*pixelmap, PixelmapInfo \*info)
    {
        OH\_PixelmapNative\_GetByteCount(pixelmap, &info->byteCount);
        OH\_PixelmapNative\_GetAllocationByteCount(pixelmap, &info->allocationByteCount);
        return;
    }
    
    void DataCopy(OH\_PixelmapNative \*pixelmap, OH\_ImageSourceNative\* imageSource, OH\_DecodingOptions \*options,
                  IMAGE\_ALLOCATOR\_TYPE allocatorType)
    {
        PixelmapInfo srcInfo;
        GetPixelmapInfo(pixelmap, &srcInfo);
        GetPixelmapAddrInfo(pixelmap, &srcInfo);
    
        void \*pixels = nullptr;
        OH\_PixelmapNative\_AccessPixels(pixelmap, &pixels);
        OH\_PixelmapNative \*newPixelmap = nullptr;
        OH\_ImageSourceNative\_CreatePixelmap(imageSource, options, &newPixelmap);
        uint32\_t dstRowStride = srcInfo.width \* GetPixelFormatBytes(srcInfo.pixelFormat);
        void \*newPixels = nullptr;
        OH\_PixelmapNative\_AccessPixels(newPixelmap, &newPixels);
        uint8\_t \*src = reinterpret\_cast<uint8\_t \*>(pixels);
        uint8\_t \*dst = reinterpret\_cast<uint8\_t \*>(newPixels);
        uint32\_t dstSize = srcInfo.byteCount;
        uint32\_t rowSize;
        if (allocatorType == IMAGE\_ALLOCATOR\_TYPE::IMAGE\_ALLOCATOR\_TYPE\_DMA) {
            rowSize = srcInfo.rowStride;
        } else {
            rowSize = dstRowStride;
        }
        for (uint32\_t i = 0; i < srcInfo.height; ++i) {
            if (dstSize >= dstRowStride) {
                std::copy(src, src + dstRowStride, dst);
            } else {
                break;
            }
            src += rowSize;
            dst += dstRowStride;
            dstSize -= dstRowStride;
        }
        OH\_PixelmapNative\_UnaccessPixels(newPixelmap);
        OH\_PixelmapNative\_UnaccessPixels(pixelmap);
        OH\_DecodingOptions\_Release(options);
        options = nullptr;
        OH\_ImageSourceNative\_Release(imageSource);
        imageSource = nullptr;
        OH\_PixelmapNative\_Release(pixelmap);
        pixelmap = nullptr;
        OH\_PixelmapNative\_Release(newPixelmap);
        newPixelmap = nullptr;
    }
    
    napi\_value TestStrideWithAllocatorType(napi\_env env, napi\_callback\_info info)
    {
        napi\_value argValue\[1\] = {nullptr};
        size\_t argCount = 1;
        if (napi\_get\_cb\_info(env, info, &argCount, argValue, nullptr, nullptr) != napi\_ok || argCount < 1 ||
            argValue\[0\] == nullptr) {
            OH\_LOG\_ERROR(LOG\_APP, "CreateImageSource napi\_get\_cb\_info failed!");
            return GetJsResult(env, IMAGE\_BAD\_PARAMETER);
        }
        
        const size\_t maxPathLength = 1024;
        char filePath\[maxPathLength\];
        size\_t pathSize = maxPathLength;
        napi\_get\_value\_string\_utf8(env, argValue\[0\], filePath, maxPathLength, &pathSize);
    
        OH\_ImageSourceNative\* imageSource = nullptr;
        Image\_ErrorCode image\_ErrorCode = OH\_ImageSourceNative\_CreateFromUri(filePath, pathSize, &imageSource);
        OH\_DecodingOptions \*options = nullptr;
        OH\_DecodingOptions\_Create(&options);
        IMAGE\_ALLOCATOR\_TYPE allocatorType = IMAGE\_ALLOCATOR\_TYPE::IMAGE\_ALLOCATOR\_TYPE\_DMA;  // Use DMA to create a PixelMap.
        OH\_PixelmapNative \*pixelmap = nullptr;
        image\_ErrorCode = OH\_ImageSourceNative\_CreatePixelmapUsingAllocator(imageSource, options, allocatorType, &pixelmap);
        DataCopy(pixelmap, imageSource, options, allocatorType);
        return GetJsResult(env, image\_ErrorCode);
    }
    

#### Memory Restrictions for Decoding a Single Image

To prevent system crashes from memory overflow, the system enforces memory restrictions on processes. For details, see [Application-Killed Issues Detection](https://developer.huawei.com/consumer/en/doc/best-practices/bpta-stability-runtime-appkilled-detection).

The image framework imposes a 2 GB memory limit for decoding a single image. Processes should actively manage their memory usage. To avoid process termination, you are advised to release [OH\_PixelmapNative](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-image-nativemodule-oh-pixelmapnative) when it is no longer needed.

Applications can use [onMemoryLevel](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-app-ability-abilitystage#onmemorylevel) to listen for system memory changes.

The calculation rule for PixelMap memory allocation is as follows:

pixels\_size (pixel memory size) = stride (image pixel storage width) \* height (image pixel height)

For images with original pixel memory exceeding 2 GB and supporting downsampling, you are advised to use [OH\_ImageSourceNative\_CreatePixelmap](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-image-source-native-h#oh_imagesourcenative_createpixelmap) or [OH\_ImageSourceNative\_CreatePixelmapUsingAllocator](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-image-source-native-h#oh_imagesourcenative_createpixelmapusingallocator) and set **desiredSize** in [OH\_DecodingOptions](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-image-nativemodule-oh-decodingoptions) for downsampling decoding.

Starting from API version 21, for images that support downsampling decoding, when **desiredSize** (expected output size) is set, the decoder calculates PixelMap pixel memory at the optimal downsampling rate with a base gradient of 1/8. This means that it selects the highest clarity sampling rate among 7/8, 6/8, ..., 1/8.

The table below lists the downsampling decoding support for different image formats in the image framework.

| Support for Downsampling | Image Format |
| :-- | :-- |
| Supported | .jpg, .png, .heic (Refer to the device specification document for specific support.) |
| Not supported | .gif, .bmp, .webp, .dng, .svg, .ico |
