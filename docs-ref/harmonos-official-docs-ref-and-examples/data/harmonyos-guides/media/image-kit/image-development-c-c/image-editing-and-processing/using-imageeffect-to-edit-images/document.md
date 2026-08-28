# Using ImageEffect to Edit Images

#### When to Use

The **ImageEffect** class provides a series of APIs for editing an image. You can use the APIs to implement various filter effects on images of different input types (pixel map, native window, native buffer, or URI).

With the native APIs provided by **ImageEffect**, you can:

-   Add a filter or filter chain, set an input image, and make the filter effective on the image.
-   Customize a filter.
-   Use a system defined filter.

#### **Available APIs**

For details about the APIs, see [ImageEffect](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-imageeffect).

#### How to Develop

**Adding Dynamic Link Libraries**

Add the following libraries to **CMakeLists.txt**.

target\_link\_libraries(entry PUBLIC
    libace\_ndk.z.so
    libimage\_effect.so
    libpixelmap.so
    libnative\_window.so
    libnative\_buffer.so
)

Add the following dynamic link libraries based on the image type: **libpixelmap.so** for the pixel map type, **libnative\_window.so** for the native window type, and **libnative\_buffer.so** for the native buffer type.

**Adding the Header Files**

#include <hilog/log.h>
#include <multimedia/image\_effect/image\_effect.h>
#include <multimedia/image\_effect/image\_effect\_filter.h>
#include <multimedia/image\_effect/image\_effect\_errors.h>

## Making a Filter Effective

1.  Create an ImageEffect instance.
    
    // Create an ImageEffect instance, with the alias set to ImageEdit.
    OH\_ImageEffect \*imageEffect = OH\_ImageEffect\_Create("ImageEdit");
    
2.  Add a filter.
    
    // Add a filter to obtain an OH\_EffectFilter instance. You can call this API multiple times to add multiple filters to form a filter chain.
    OH\_EffectFilter \*filter = OH\_ImageEffect\_AddFilter(imageEffect, OH\_EFFECT\_BRIGHTNESS\_FILTER);
    if (filter == nullptr) {
        OH\_LOG\_ERROR(LOG\_APP, "OH\_ImageEffect\_AddFilter fail!");
        return;
    }
    // Set a filter parameter. For example, set the intensity to 50.
    ImageEffect\_Any value = { .dataType = ImageEffect\_DataType::EFFECT\_DATA\_TYPE\_FLOAT, .dataValue.floatValue = 50.f };
    ImageEffect\_ErrorCode errorCode = OH\_EffectFilter\_SetValue(filter, OH\_EFFECT\_FILTER\_INTENSITY\_KEY, &value);
    
3.  Set the data to be processed.
    
    **Scenario 1: Set the OH\_PixelmapNative input type.**
    
    For details about how to use OH\_PixelmapNative, see [PixelMap Data Processing (C/C++)](../../../image-development-dependent-on-js-objects-not-recommended/pixelmap-operation/document.md).
    
    // Set an input pixel map.
    errorCode = OH\_ImageEffect\_SetInputPixelmap(imageEffect, inputPixelmap);
    if (errorCode != ImageEffect\_ErrorCode::EFFECT\_SUCCESS) {
        OH\_LOG\_ERROR(LOG\_APP, "OH\_ImageEffect\_SetInputPixelmap fail!");
        return;
    }
    
    // (Optional) Set an output pixel map. If this API is not called, the filter effect directly takes effect on the input pixel map.
    errorCode = OH\_ImageEffect\_SetOutputPixelmap(imageEffect, outputPixelmap);
    if (errorCode != ImageEffect\_ErrorCode::EFFECT\_SUCCESS) {
        OH\_LOG\_ERROR(LOG\_APP, "OH\_ImageEffect\_SetOutputPixelmap fail!");
        return;
    }
    
    **Scenario 2: Set the OH\_NativeBuffer input type.**
    
    For details about how to use OH\_NativeBuffer, see [Native Buffer Development (C/C++)](../../../../../graphics/arkgraphics-2d/nativebuffer-development-c-c/document.md).
    
    // Set an input native buffer.
    errorCode = OH\_ImageEffect\_SetInputNativeBuffer(imageEffect, inputNativeBuffer);
    if (errorCode != ImageEffect\_ErrorCode::EFFECT\_SUCCESS) {
        OH\_LOG\_ERROR(LOG\_APP, "OH\_ImageEffect\_SetInputNativeBuffer fail!");
        return;
    }
    
    // (Optional) Set an output native buffer. If this API is not called, the filter effect directly takes effect on the input native buffer.
    errorCode = OH\_ImageEffect\_SetOutputNativeBuffer(imageEffect, outputNativeBuffer);
    if (errorCode != ImageEffect\_ErrorCode::EFFECT\_SUCCESS) {
        OH\_LOG\_ERROR(LOG\_APP, "OH\_ImageEffect\_SetOutputNativeBuffer fail!");
        return;
    }
    
    **Scenario 3: Set the URI input type.**
    
    // Set an input URI.
    errorCode = OH\_ImageEffect\_SetInputUri(imageEffect, inputUri);
    if (errorCode != ImageEffect\_ErrorCode::EFFECT\_SUCCESS) {
        OH\_LOG\_ERROR(LOG\_APP, "OH\_ImageEffect\_SetInputUri fail!");
        return;
    }
    // (Optional) Set an output URI. If this API is not called, the filter effect directly takes effect on the input URI.
    errorCode = OH\_ImageEffect\_SetOutputUri(imageEffect, outputUri);
    if (errorCode != ImageEffect\_ErrorCode::EFFECT\_SUCCESS) {
        OH\_LOG\_ERROR(LOG\_APP, "OH\_ImageEffect\_SetOutputUri fail!");
        return;
    }
    
    **Scenario 4: Set the texture input type.**
    
    In the texture input scenario, the GPU is used for rendering. In this scenario, the application needs to provide a valid OpenGL context environment, set parameters, and perform rendering operations in the correct environment.
    
    // Set the input texture ID.
    errorCode = OH\_ImageEffect\_SetInputTextureId(imageEffect, inputTex, ColorSpaceName::SRGB);
    if (errorCode != ImageEffect\_ErrorCode::EFFECT\_SUCCESS) {
        OH\_LOG\_ERROR(LOG\_APP, "OH\_ImageEffect\_SetInputTextureId fail!");
        return;
    }
    
    // Set the output texture ID. Note that the output texture ID cannot be the same as the input texture ID. Otherwise, rendering exceptions may occur.
    errorCode = OH\_ImageEffect\_SetOutputTextureId(imageEffect, outputTex);
    if (errorCode != ImageEffect\_ErrorCode::EFFECT\_SUCCESS) {
        OH\_LOG\_ERROR(LOG\_APP, "OH\_ImageEffect\_SetOutputTextureId fail!");
        return;
    }
    
    **Scenario 5: Set the OHNativeWindow input type.**
    
    The following uses camera preview as an example to describe the scenario. The surface ID provided by the **XComponent** for camera preview streams can be converted into an OHNativeWindow instance at the native C++ layer.
    
    For details about how to use the **XComponent**, see [XComponent](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ts-basic-components-xcomponent).
    
    For details about how to use the native window module, see [OHNativeWindow](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-nativewindow).
    
    For details about how to use the camera, see [Camera Preview (C/C++)](../../../../camera-kit/fundamental-capabilities-for-camera-application-development-c-c/preview-c-c/document.md).
    
    (1) Add an **XComponent** to the .ets file.
    
    XComponent({
       id: 'xcomponentId',
       type: 'surface',
       controller: this.mXComponentController,
       libraryname: 'entry'
    })
    .onLoad(() => {
       // Obtain the surface ID of the XComponent.
       this.mSurfaceId = this.mXComponentController.getXComponentSurfaceId()
    
       // Obtain the input surface ID.
       this.mSurfaceId = imageEffect.getSurfaceId(this.mSurfaceId)
    
       // Call the camera API to start preview and transfer the input surface ID to the camera framework.
       // ...
    })
    .width('100%')
    .height('100%')
    
    (2) Implement **imageEffect.getSurfaceId** at the native C++ layer.
    
    // Create a NativeWindow instance based on the surface ID. Note that the instance must be released by calling OH\_NativeWindow\_DestroyNativeWindow when it is no longer needed.
    uint64\_t outputSurfaceId;
    std::istrstream iss(outputSurfaceIdStr);
    issue >> outputSurfaceId;
    OHNativeWindow \*outputNativeWindow = nullptr;
    int32\_t res = OH\_NativeWindow\_CreateNativeWindowFromSurfaceId(outputSurfaceId, &outputNativeWindow);
    if (res != 0) {
        OH\_LOG\_ERROR(LOG\_APP, "OH\_NativeWindow\_CreateNativeWindowFromSurfaceId fail!");
        return;
    }
    
    // Set an output surface.
    ImageEffect\_ErrorCode errorCode = OH\_ImageEffect\_SetOutputSurface(imageEffect, outputNativeWindow);
    if (res != 0) {
        OH\_LOG\_ERROR(LOG\_APP, "OH\_ImageEffect\_SetOutputSurface fail!");
        return;
    }
    // Obtain the input surface. Note that the obtained inputNativeWindow instance must be released by calling OH\_NativeWindow\_DestroyNativeWindow when it is no longer needed.
    OHNativeWindow \*inputNativeWindow = nullptr;
    errorCode = OH\_ImageEffect\_GetInputSurface(imageEffect, &inputNativeWindow);
    if (errorCode != ImageEffect\_ErrorCode::EFFECT\_SUCCESS) {
        OH\_LOG\_ERROR(LOG\_APP, "OH\_ImageEffect\_GetInputSurface fail!");
        return;
    }
    
    // Obtain the surface ID from the inputNativeWindow instance.
    uint64\_t inputSurfaceId = 0;
    res = OH\_NativeWindow\_GetSurfaceId(inputNativeWindow, &inputSurfaceId);
    if (res != 0) {
        OH\_LOG\_ERROR(LOG\_APP, "OH\_NativeWindow\_GetSurfaceId fail!");
        return;
    }
    
    // Convert the surface ID to a string and return the string.
    std::string inputSurfaceIdStr = std::to\_string(inputSurfaceId);
    
4.  Start the image effector.
    
    // Start the image effector.
    errorCode = OH\_ImageEffect\_Start(imageEffect);
    if (errorCode != ImageEffect\_ErrorCode::EFFECT\_SUCCESS) {
        OH\_LOG\_ERROR(LOG\_APP, "OH\_ImageEffect\_Start fail!");
        return;
    }
    
5.  (Optional) Stop the image effector. This operation is required only in the input surface scenario.
    
    // Stop the image effector.
    errorCode = OH\_ImageEffect\_Stop(imageEffect);
    if (errorCode != ImageEffect\_ErrorCode::EFFECT\_SUCCESS) {
        OH\_LOG\_ERROR(LOG\_APP, "OH\_ImageEffect\_Stop fail!");
        return;
    }
    
6.  (Optional) Serialize the image effector.
    
    char \*info = nullptr;
    errorCode = OH\_ImageEffect\_Save(imageEffect, &info);
    if (errorCode != ImageEffect\_ErrorCode::EFFECT\_SUCCESS) {
        OH\_LOG\_ERROR(LOG\_APP, "OH\_ImageEffect\_Save fail!");
        return;
    }
    
7.  Destroy the ImageEffect instance.
    
    // Release the ImageEffect instance.
    errorCode = OH\_ImageEffect\_Release(imageEffect);
    if (errorCode != ImageEffect\_ErrorCode::EFFECT\_SUCCESS) {
        OH\_LOG\_ERROR(LOG\_APP, "OH\_ImageEffect\_Release fail!");
        return;
    }
    

## Customizing a Filter

To implement and register a custom filter, perform the following steps:

1.  Define **ImageEffect\_FilterDelegate**.
    
    // Image information struct.
    struct EffectBufferInfo {
        void \*addr = nullptr;
        int32\_t width = 0;
        int32\_t height = 0;
        int32\_t rowSize = 0;
        ImageEffect\_Format format = ImageEffect\_Format::EFFECT\_PIXEL\_FORMAT\_UNKNOWN;
    };
    
    // Implement a custom filter.
    ImageEffect\_FilterDelegate filterDelegate = {
        .setValue = \[\](OH\_EffectFilter \*filter, const char \*key, const ImageEffect\_Any \*value) {
            // Verify the parameters. If the verification is successful, true is returned. Otherwise, false is returned.
            // ...
            return true;
        },
        .render = \[\](OH\_EffectFilter \*filter, OH\_EffectBufferInfo \*info, OH\_EffectFilterDelegate\_PushData pushData) {
            return Render(filter, info, pushData);
        },
        .save = \[\](OH\_EffectFilter \*filter, char \*\*info) {
            // Obtain the custom filter parameter. In this example, Brightness is the key of the custom filter.
            ImageEffect\_Any value;
            ImageEffect\_ErrorCode errorCode = OH\_EffectFilter\_GetValue(filter, "Brightness", &value);
            if (errorCode != ImageEffect\_ErrorCode::EFFECT\_SUCCESS) {
            OH\_LOG\_ERROR(LOG\_APP, "OH\_EffectFilter\_GetValue fail!");
            return false;
            }
             
            // Generate a key-value pair.
            json values;
            values\["Brightness"\] = value.dataValue.floatValue;
            json root;
            root\["name"\] = "CustomBrightness";
            root\["values"\] = values;
    
            // Convert the JSON object to the string infoStr.
            // ...
    
            // Assign a serialized string address to \*info.
            \*info = infoStr;
            return true;
        },
        .restore = \[\](const char \*info) {
            // Create an OH\_EffectFilter instance, in which CustomBrightness is the name of the custom filter.
            OH\_EffectFilter \*filter = OH\_EffectFilter\_Create("CustomBrightness");
            // Parse the JSON string info to obtain the key and value.
            // ...
    
            // Set a filter parameter. value is the parameter parsed based on the JSON string in info.
            ImageEffect\_ErrorCode errorCode = OH\_EffectFilter\_SetValue(filter, "Brightness", &value);
    
            // ...
            return filter;
        }
    };
    
    You can implement the **Render** API in two scenarios.
    
    **Scenario 1: The custom algorithm can directly modify the pixel data in info (for example, the brightness filter).**
    
    bool Render(OH\_EffectFilter \*filter, OH\_EffectBufferInfo \*info, OH\_EffectFilterDelegate\_PushData pushData)
    {
        // Obtain the image information.
        EffectBufferInfo inputBufferInfo;
        OH\_EffectBufferInfo\_GetAddr(info, &inputBufferInfo.addr);
        OH\_EffectBufferInfo\_GetWidth(info, &inputBufferInfo.width);
        OH\_EffectBufferInfo\_GetHeight(info, &inputBufferInfo.height);
        OH\_EffectBufferInfo\_GetRowSize(info, &inputBufferInfo.rowSize);
        OH\_EffectBufferInfo\_GetEffectFormat(info, &inputBufferInfo.format);
    
        // Invoke the custom filter algorithm.
        ApplyCustomAlgo(inputBufferInfo);
    
        // After the editing is complete, call pushData to directly transfer the original image.
        pushData(filter, info);
        return true;
    }
    
    **Scenario 2: The custom algorithm cannot directly modify the pixel data in info (for example, the crop filter).**
    
    bool Render(OH\_EffectFilter \*filter, OH\_EffectBufferInfo \*info, OH\_EffectFilterDelegate\_PushData pushData)
    {
        // Obtain the image information.
        EffectBufferInfo inputBufferInfo;
        OH\_EffectBufferInfo\_GetAddr(info, &inputBufferInfo.addr);
        OH\_EffectBufferInfo\_GetWidth(info, &inputBufferInfo.width);
        OH\_EffectBufferInfo\_GetHeight(info, &inputBufferInfo.height);
        OH\_EffectBufferInfo\_GetRowSize(info, &inputBufferInfo.rowSize);
        OH\_EffectBufferInfo\_GetEffectFormat(info, &inputBufferInfo.format);
    
        // Create output pixel information.
        EffectBufferInfo outputBufferInfo = CreateOutputBufferInfo(inputBufferInfo);
    
        // Invoke the custom filter algorithm.
        ApplyCustomAlgo(inputBufferInfo, outputBufferInfo);
    
        // Generate outputOhInfo.
        OH\_EffectBufferInfo \*outputOhInfo = OH\_EffectBufferInfo\_Create();
        OH\_EffectBufferInfo\_SetAddr(outputOhInfo, outputBufferInfo.addr);
        OH\_EffectBufferInfo\_SetWidth(outputOhInfo, outputBufferInfo.width);
        OH\_EffectBufferInfo\_SetHeight(outputOhInfo, outputBufferInfo.height);
        OH\_EffectBufferInfo\_SetRowSize(outputOhInfo, outputBufferInfo.rowSize);
        OH\_EffectBufferInfo\_SetEffectFormat(outputOhInfo, outputBufferInfo.format);
    
        // Call pushData to transfer outputOhInfo after editing.
        pushData(filter, outputOhInfo);
    
        // Release resources.
        OH\_EffectBufferInfo\_Release(outputOhInfo);
        ReleaseOutputBuffer(outputBufferInfo.addr);
    
        return true;
    }
    
2.  Generate custom filter information.
    
    // Create an OH\_EffectFilterInfo instance.
    OH\_EffectFilterInfo \*customFilterInfo = OH\_EffectFilterInfo\_Create();
    if (customFilterInfo ==nullptr) {
        OH\_LOG\_ERROR(LOG\_APP, "OH\_EffectFilter\_GetValue fail!");
        return;
    }
    
    // Set the name of the custom filter.
    OH\_EffectFilterInfo\_SetFilterName(customFilterInfo, "CustomBrightness");
    
    // Set the buffer types supported by the custom filter.
    ImageEffect\_BufferType bufferTypeArray\[\] = { ImageEffect\_BufferType::EFFECT\_BUFFER\_TYPE\_PIXEL };
    OH\_EffectFilterInfo\_SetSupportedBufferTypes(customFilterInfo, sizeof(bufferTypeArray) / sizeof(ImageEffect\_BufferType), bufferTypeArray);
    
    // Set the pixel formats supported by the custom filter.
    ImageEffect\_Format formatArray\[\] = { ImageEffect\_Format::EFFECT\_PIXEL\_FORMAT\_RGBA8888 };
    OH\_EffectFilterInfo\_SetSupportedFormats(customFilterInfo, sizeof(formatArray) / sizeof(ImageEffect\_Format), formatArray);
    
3.  Register **ImageEffect\_FilterDelegate** with the image effector.
    
    // Register the custom filter.
    ImageEffect\_ErrorCode errorCode = OH\_EffectFilter\_Register(customFilterInfo, &filterDelegate);
    if (errorCode != ImageEffect\_ErrorCode::EFFECT\_SUCCESS) {
        OH\_LOG\_ERROR(LOG\_APP, "OH\_EffectFilter\_Register fail!");
        return;
    }
    

## Using a System Defined Filter

1.  Create a filter.
    
    // Create a filter, for example, a contrast filter.
    OH\_EffectFilter \*filter = OH\_EffectFilter\_Create(OH\_EFFECT\_CONTRAST\_FILTER);
    
2.  Set a filter parameter.
    
    // Set a filter parameter. For example, set the intensity to 50.
    ImageEffect\_Any value = {.dataType = ImageEffect\_DataType::EFFECT\_DATA\_TYPE\_FLOAT, .dataValue.floatValue = 50.f};
    ImageEffect\_ErrorCode errorCode = OH\_EffectFilter\_SetValue(filter, OH\_EFFECT\_FILTER\_INTENSITY\_KEY, &value);
    if (errorCode != ImageEffect\_ErrorCode::EFFECT\_SUCCESS) {
        OH\_LOG\_ERROR(LOG\_APP, "OH\_EffectFilter\_SetValue fail!");
        return;
    }
    
3.  Make the filter take effect.
    
    // Start rendering with the filter.
    errorCode = OH\_EffectFilter\_Render(filter, inputPixelmap, outputPixelmap);
    
4.  Destroy the filter instance.
    
    // Destroy the filter instance.
    errorCode = OH\_EffectFilter\_Release(filter);
    

## Query Capabilities

-   Query filter information based on the filter name.
    
    // Create an OH\_EffectFilterInfo instance.
    OH\_EffectFilterInfo \*filterInfo = OH\_EffectFilterInfo\_Create();
    if (filterInfo == nullptr) {
        OH\_LOG\_ERROR(LOG\_APP, "OH\_EffectFilterInfo\_Create fail!");
        return;
    }
    
    // Query the filter information based on the filter name.
    ImageEffect\_ErrorCode errorCode = OH\_EffectFilter\_LookupFilterInfo(OH\_EFFECT\_BRIGHTNESS\_FILTER, filterInfo);
    if (errorCode != ImageEffect\_ErrorCode::EFFECT\_SUCCESS) {
        OH\_LOG\_ERROR(LOG\_APP, "OH\_EffectFilter\_LookupFilterInfo fail!");
        return;
    }
    
    // Obtain the filter name from the filter information.
    char \*name = nullptr;
    OH\_EffectFilterInfo\_GetFilterName(filterInfo, &name);
    
    // Obtain the supported buffer types.
    uint32\_t supportedBufferTypesCnt = 0;
    ImageEffect\_BufferType \*bufferTypeArray = nullptr;
    OH\_EffectFilterInfo\_GetSupportedBufferTypes(filterInfo, &supportedBufferTypesCnt, &bufferTypeArray);
    
    // Obtain the supported pixel formats.
    uint32\_t supportedFormatsCnt = 0;
    ImageEffect\_Format \*formatArray = nullptr;
    OH\_EffectFilterInfo\_GetSupportedFormats(filterInfo, supportedFormatsCnt, &formatArray);
    
    // Destroy the OH\_EffectFilterInfo instance.
    OH\_EffectFilterInfo\_Release(filterInfo);
    
-   Query filters that meet given conditions.
    
    // Query all filters. Resources need to be released.
    ImageEffect\_FilterNames \*filterNames = OH\_EffectFilter\_LookupFilters("Default");
    
    // ...
    
    // Release virtual memory resources by filter names.
    OH\_EffectFilter\_ReleaseFilterNames();
