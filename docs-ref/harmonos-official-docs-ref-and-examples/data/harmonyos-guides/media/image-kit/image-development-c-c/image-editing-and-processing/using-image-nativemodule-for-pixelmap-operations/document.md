# Using Image\_NativeModule for PixelMap Operations

You can use the **Pixelmap** class to create, operate, and release a PixelMap, and obtain its width, height, pixel format, alpha type, and row stride.

#### How to Develop

## Adding a Link Library

Open the **src/main/cpp/CMakeLists.txt** file of the native project, add **libpixelmap.so** and **libhilog\_ndk.z.so** (on which the log APIs depend) to the **target\_link\_libraries** dependency.

target\_link\_libraries(entry PUBLIC libhilog\_ndk.z.so libpixelmap.so)

## Calling the Native APIs

For details about the APIs, see [Image\_NativeModule](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-image-nativemodule).

Create a native C++ application in DevEco Studio. The project created by default contains the **index.ets** file, and a **hello.cpp** or **napi\_init.cpp** file is generated in the **entry\\src\\main\\cpp** directory. In this example, the generated file is **hello.cpp**. Implement the C APIs in **hello.cpp**. Refer to the sample code below.

**Example of Using the Pixelmap APIs**

Create a Pixelmap instance after parameter initialization, read and write pixel data, and perform operations such as scaling, translating, flipping, rotating, and cropping on the image.

#include <hilog/log.h>
#include <multimedia/image\_framework/image/pixelmap\_native.h>

#undef LOG\_DOMAIN
#undef LOG\_TAG
#define LOG\_DOMAIN 0x3200
#define LOG\_TAG "MY\_TAG"

Image\_ErrorCode PixelmapTest()
{
    uint8\_t data\[96\];
    size\_t dataSize = 96;
    for (int i = 0; i < dataSize; i++) {
        data\[i\] = i + 1;
    }

    // Create a parameter structure instance and set parameters.
    OH\_Pixelmap\_InitializationOptions \*createOpts;
    OH\_PixelmapInitializationOptions\_Create(&createOpts);
    OH\_PixelmapInitializationOptions\_SetWidth(createOpts, 6);
    OH\_PixelmapInitializationOptions\_SetHeight(createOpts, 4);
    OH\_PixelmapInitializationOptions\_SetPixelFormat(createOpts, PIXEL\_FORMAT\_RGBA\_8888);
    OH\_PixelmapInitializationOptions\_SetAlphaType(createOpts, PIXELMAP\_ALPHA\_TYPE\_UNKNOWN);

    // Create a Pixelmap instance.
    OH\_PixelmapNative \*pixelmap = nullptr;
    Image\_ErrorCode errCode = OH\_PixelmapNative\_CreatePixelmap(data, dataSize, createOpts, &pixelmap);

    // Read the image pixel data and write the data to the array.
    uint8\_t destination\[96\];
    size\_t destinationSize = 96;
    errCode = OH\_PixelmapNative\_ReadPixels(pixelmap, destination, &destinationSize);
    if (errCode != IMAGE\_SUCCESS) {
        OH\_LOG\_ERROR(LOG\_APP, "ImagePixelmapNativeCTest pixelmapTest OH\_PixelmapNative\_ReadPixels failed, errCode: %{public}d.", errCode);
        return errCode;
    }

    // Read the image data in the buffer and write the data to the Pixelmap instance.
    uint8\_t source\[96\];
    size\_t sourceSize = 96;
    for (int i = 0; i < sourceSize; i++) {
        source\[i\] = i + 1;
    }
    errCode = OH\_PixelmapNative\_WritePixels(pixelmap, source, sourceSize);
    if (errCode != IMAGE\_SUCCESS) {
        OH\_LOG\_ERROR(LOG\_APP, "ImagePixelmapNativeCTest pixelmapTest OH\_PixelmapNative\_WritePixels failed, errCode: %{public}d.", errCode);
        return errCode;
    }

    // Create an image information instance and obtain the pixel information.
    OH\_Pixelmap\_ImageInfo \*imageInfo;
    OH\_PixelmapImageInfo\_Create(&imageInfo);
    errCode = OH\_PixelmapNative\_GetImageInfo(pixelmap, imageInfo);
    if (errCode != IMAGE\_SUCCESS) {
        OH\_LOG\_ERROR(LOG\_APP, "ImagePixelmapNativeCTest pixelmapTest OH\_PixelmapNative\_GetImageInfo failed, errCode: %{public}d.", errCode);
        return errCode;
    }

    // Obtain the width, height, pixel format, and alpha type of the image.
    uint32\_t width, height, rowStride;
    int32\_t pixelFormat, alphaType;
    OH\_PixelmapImageInfo\_GetWidth(imageInfo, &width);
    OH\_PixelmapImageInfo\_GetHeight(imageInfo, &height);
    OH\_PixelmapImageInfo\_GetRowStride(imageInfo, &rowStride);
    OH\_PixelmapImageInfo\_GetPixelFormat(imageInfo, &pixelFormat);
    OH\_PixelmapImageInfo\_GetAlphaType(imageInfo, &alphaType);
    OH\_PixelmapImageInfo\_Release(imageInfo);
    OH\_LOG\_INFO(LOG\_APP, "ImagePixelmapNativeCTest pixelmapTest GetImageInfo success, width: %{public}d, height: %{public}d, rowStride: %{public}d, pixelFormat: %{public}d, alphaType: %{public}d.", width, height, rowStride, pixelFormat, alphaType);

    // Set the opacity rate to enable the image to achieve the corresponding opacity effect.
    errCode = OH\_PixelmapNative\_Opacity(pixelmap, 0.5);
    if (errCode != IMAGE\_SUCCESS) {
        OH\_LOG\_ERROR(LOG\_APP, "ImagePixelmapNativeCTest pixelmapTest OH\_PixelmapNative\_Opacity failed, errCode: %{public}d.", errCode);
        return errCode;
    }

    // Scale the image.
    errCode = OH\_PixelmapNative\_Scale(pixelmap, 2.0, 1.0);
    if (errCode != IMAGE\_SUCCESS) {
        OH\_LOG\_ERROR(LOG\_APP, "ImagePixelmapNativeCTest pixelmapTest OH\_PixelmapNative\_Scale failed, errCode: %{public}d.", errCode);
        return errCode;
    }

    // Translate the image.
    errCode = OH\_PixelmapNative\_Translate(pixelmap, 50.0, 10.0);
    if (errCode != IMAGE\_SUCCESS) {
        OH\_LOG\_ERROR(LOG\_APP, "ImagePixelmapNativeCTest pixelmapTest OH\_PixelmapNative\_Translate failed, errCode: %{public}d.", errCode);
        return errCode;
    }

    // Rotate the image.
    errCode = OH\_PixelmapNative\_Rotate(pixelmap, 90.0);
    if (errCode != IMAGE\_SUCCESS) {
        OH\_LOG\_ERROR(LOG\_APP, "ImagePixelmapNativeCTest pixelmapTest OH\_PixelmapNative\_Rotate failed, errCode: %{public}d.", errCode);
        return errCode;
    }

    // Flip the image.
    errCode = OH\_PixelmapNative\_Flip(pixelmap, true, true);
    if (errCode != IMAGE\_SUCCESS) {
        OH\_LOG\_ERROR(LOG\_APP, "ImagePixelmapNativeCTest pixelmapTest OH\_PixelmapNative\_Flip failed, errCode: %{public}d.", errCode);
        return errCode;
    }

    // Crop the image.
    Image\_Region region;
    region.x = 100;
    region.y = 100;
    region.width = 6;
    region.height = 4;
    errCode = OH\_PixelmapNative\_Crop(pixelmap, &region);
    if (errCode != IMAGE\_SUCCESS) {
        OH\_LOG\_ERROR(LOG\_APP, "ImagePixelmapNativeCTest pixelmapTest OH\_PixelmapNative\_Crop failed, errCode: %{public}d.", errCode);
        return errCode;
    }

    // Release the Pixelmap and InitializationOptions instances.
    OH\_PixelmapNative\_Release(pixelmap);
    OH\_PixelmapInitializationOptions\_Release(createOpts);
    return IMAGE\_SUCCESS;
}

// Example of converting between premultiplied and non-premultiplied formats in PixelMap.
Image\_ErrorCode PixelmapConvertAlphaTypeTest()
{
    uint8\_t data\[96\];
    size\_t dataSize = 96;
    for (int i = 0; i < dataSize; i++) {
        data\[i\] = i + 1;
    }

    // Create a parameter structure instance and set parameters.
    OH\_Pixelmap\_InitializationOptions \*createOpts;
    OH\_PixelmapInitializationOptions\_Create(&createOpts);
    OH\_PixelmapInitializationOptions\_SetWidth(createOpts, 6);
    OH\_PixelmapInitializationOptions\_SetHeight(createOpts, 4);
    OH\_PixelmapInitializationOptions\_SetSrcPixelFormat(createOpts, PIXEL\_FORMAT\_RGBA\_8888);
    OH\_PixelmapInitializationOptions\_SetPixelFormat(createOpts, PIXEL\_FORMAT\_RGBA\_8888);
    OH\_PixelmapInitializationOptions\_SetAlphaType(createOpts, PIXELMAP\_ALPHA\_TYPE\_UNPREMULTIPLIED);

    // Create a Pixelmap instance in non-premultiplied format.
    OH\_PixelmapNative \*SrcPixelmap = nullptr;
    Image\_ErrorCode errCode = OH\_PixelmapNative\_CreatePixelmap(data, dataSize, createOpts, &SrcPixelmap);
    if (errCode != IMAGE\_SUCCESS) {
        OH\_LOG\_ERROR(LOG\_APP, "PixelmapConvertAlphaTypeTest CreateSrcPixelMap failed, errCode: %{public}d.", errCode);
    }

    // Create a Pixelmap instance in premultiplied format. DstPixelmap is used to store the data after the alpha type of SrcPixelmap is converted.
    OH\_PixelmapNative \*DstPixelmap = nullptr;
    OH\_PixelmapInitializationOptions\_SetAlphaType(createOpts, PIXELMAP\_ALPHA\_TYPE\_PREMULTIPLIED);
    errCode = OH\_PixelmapNative\_CreatePixelmap(data, dataSize, createOpts, &DstPixelmap);
    if (errCode != IMAGE\_SUCCESS) {
        OH\_LOG\_ERROR(LOG\_APP, "PixelmapConvertAlphaTypeTest CreateDstPixelMap failed, errCode: %{public}d.", errCode);
    }

    // Convert the alpha type. The data of SrcPixelmap is converted to premultiplied format and saved to DstPixelmap.
    errCode = OH\_PixelmapNative\_ConvertAlphaFormat(SrcPixelmap, DstPixelmap, true);
    if (errCode != IMAGE\_SUCCESS) {
        OH\_LOG\_ERROR(LOG\_APP, "PixelmapConvertAlphaTypeTest ConvertAlphaFormat failed, errCode: %{public}d.", errCode);
    }

    // Release the Pixelmap and InitializationOptions instances.
    OH\_PixelmapNative\_Release(SrcPixelmap);
    OH\_PixelmapNative\_Release(DstPixelmap);
    OH\_PixelmapInitializationOptions\_Release(createOpts);
    return errCode;
}
