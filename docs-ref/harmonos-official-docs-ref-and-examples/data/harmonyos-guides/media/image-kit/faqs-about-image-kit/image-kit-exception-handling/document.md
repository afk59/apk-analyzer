# Image Kit Exception Handling

[Image Kit](../../about-this-kit/document.md) provides **ArkTS APIs** and **C APIs**. In special circumstances (such as invalid input parameters, insufficient memory, or functions unable to process requests), the system reports errors through exceptions (for ArkTS APIs) or error codes (for C APIs). You need to properly capture and handle these errors at the application level to prevent application crashes or undefined behavior. The [Image Error Codes](https://developer.huawei.com/consumer/en/doc/harmonyos-references/errorcode-image) topic provides corresponding error messages, possible causes, and handling procedure for Image Kit error codes. However, since some scenarios have more complex causes for errors, you need to further locate issues with logs. For example, 401 parameter error may be due to invalid function parameters or lack of specific file read/write permissions, causing the failure to access or modify image files. (Image Kit does not perceive permissions, which manifests as an abnormal parameter error for the input file.)

#### Handling ArkTS API Exceptions

When calling an ArkTS API, if the input parameters do not meet the requirements or unrecoverable errors occur during execution, the system returns or throws a [BusinessError](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-base#businesserror) exception, or returns a rejected [Promise](../../../../application-framework/arkts/arkts-concurrency/asynchronous-concurrency-promise-and-async-await/document.md#promise) in asynchronous scenarios. If you ignore exception handling, it may lead to functional issues, data loss, or even direct application crashes.

The following describes typical forms of ArkTS APIs, API examples, and handling methods.

| API Form | Example API | Handling Method |
| :-- | :-- | :-- |
| **Promise asynchronous APIs** | getImageInfo(): Promise<ImageInfo>, modifyImageProperty(key: PropertyKey, value: string): Promise<void> | Use await+try/catch or promise.catch to capture BusinessError exceptions. |
| **AsyncCallback asynchronous APIs** | getImageInfo(callback: AsyncCallback<ImageInfo>): void | Use parameters of the [AsyncCallback](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-base#asynccallback) callback function to capture BusinessError exceptions. |
| **Synchronous APIs** | getImageInfoSync(): ImageInfo | Use try/catch to capture synchronous BusinessError exceptions. |

1.  Example of an AsyncCallback asynchronous API
    
    import { image } from '@kit.ImageKit';
    import { BusinessError } from '@kit.BasicServicesKit';
    
    function getImageInfoByCallback(pixelMap: image.PixelMap): void {
      if (!pixelMap) {
        console.error("pixelMap is null or undefined");
        return;
      }
      pixelMap.getImageInfo((err: BusinessError, info: image.ImageInfo) => {
        if (err) {
          console.error(\`getImageInfo callback failed, code=${err.code}, msg=${err.message}\`);
          return;
        }
        console.info(\`Image width=${info.size.width}, height=${info.size.height}\`);
      });
    }
    
2.  Example of a Promise asynchronous API
    
    import { image } from '@kit.ImageKit';
    import { BusinessError } from '@kit.BasicServicesKit';
    
    // getImageInfo(): Promise<ImageInfo>
    async function getImageInfoByPromise(pixelMap: image.PixelMap): Promise<void> {
      try {
        const info = await pixelMap.getImageInfo();
        console.info(\`Image width=${info.size.width}, height=${info.size.height}\`);
      } catch (err) {
        const e = err as BusinessError;
        console.error(\`getImageInfo promise failed, code=${e.code}, msg=${e.message}\`);
      }
    }
    
    // modifyImageProperty(key: PropertyKey, value: string): Promise<void>
    function modifyImagePropertyPromise(imageSource: image.ImageSource): void {
      imageSource.modifyImageProperty(image.PropertyKey.ORIENTATION, 'Top-left').then(() => {
        console.info('modifyImageProperty success');
      }).catch((err: BusinessError) => {
        console.error(\`modifyImageProperty failed, code=${err.code}, msg=${err.message}\`);
      });
    }
    
3.  Example of a synchronous API
    
    import { image } from '@kit.ImageKit';
    import { BusinessError } from '@kit.BasicServicesKit';
    
    function getImageInfoBySync(pixelMap: image.PixelMap): void {
      try {
        const info = pixelMap.getImageInfoSync();
        console.info(\`Image width=${info.size.width}, height=${info.size.height}\`);
      } catch (err) {
        const e = err as BusinessError;
        console.error(\`getImageInfoSync failed, code=${e.code}, msg=${e.message}\`);
      }
    }
    

#### Handling C API Exceptions

The C APIs uniformly use [Image Error Codes](https://developer.huawei.com/consumer/en/doc/harmonyos-references/errorcode-image) to represent the execution results of functions. A return value of **IMAGE\_SUCCESS (0)** indicates successful execution, whereas a non-zero value indicates an error. You should immediately check the return value after calling and perform necessary error handling, such as logging and resource release. A typical example of C API exception handling is as follows:

1.  Obtain image information through ImageInfo.
    
    Image\_ErrorCode OH\_PixelmapNative\_GetImageInfo(OH\_PixelmapNative \*pixelmap, OH\_Pixelmap\_ImageInfo \*imageInfo)
    
    // Link the .so library file in the src/main/cpp/CMakeLists.txt file: target\_link\_libraries(entry PUBLIC libhilog\_ndk.z.so libpixelmap.so).
    #include <hilog/log.h>
    #include <multimedia/image\_framework/image/pixelmap\_native.h>
    
    #undef LOG\_DOMAIN
    #undef LOG\_TAG
    #define LOG\_DOMAIN 0x02b6
    #define LOG\_TAG "ImageKitDemo"
    
    void GetImageInfoExample(OH\_PixelmapNative \*pixelmap) {
        if (!pixelmap) {
            OH\_LOG\_ERROR(LOG\_APP, "GetImageInfoExample: pixelmap is nullptr");
            return;
        }
        OH\_Pixelmap\_ImageInfo \*imageInfo;
        Image\_ErrorCode errCode = OH\_PixelmapImageInfo\_Create(&imageInfo);
        if (errCode != IMAGE\_SUCCESS) {
            OH\_LOG\_ERROR(LOG\_APP, "OH\_PixelmapNative\_Create failed, errCode: %{public}d.", errCode);
            return;
        }
        OH\_PixelmapNative\_GetImageInfo(pixelmap, imageInfo);
        if (errCode != IMAGE\_SUCCESS) {
            OH\_LOG\_ERROR(LOG\_APP, "OH\_PixelmapNative\_GetImageInfo failed, errCode: %{public}d.", errCode);
            return;
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
        OH\_LOG\_INFO(LOG\_APP,
                    "GetImageInfo success, width: %{public}d, height: %{public}d, "
                    "rowStride: %{public}d, pixelFormat: %{public}d, alphaType: %{public}d.",
                    width, height, rowStride, pixelFormat, alphaType);
    }
    
2.  Modify the EXIF information.
    
    Image\_ErrorCode OH\_ImageSourceNative\_ModifyImageProperty(OH\_ImageSourceNative \*source, Image\_String \*key, Image\_String \*value)
    
    // Link the .so library file in the src/main/cpp/CMakeLists.txt file: target\_link\_libraries(entry PUBLIC libhilog\_ndk.z.so libimage\_source.so).
    #include <string>
    #include <hilog/log.h>
    #include <multimedia/image\_framework/image/image\_source\_native.h>
    
    #undef LOG\_DOMAIN
    #undef LOG\_TAG
    #define LOG\_DOMAIN 0x02b6
    #define LOG\_TAG "ImageKitDemo"
    
    void ModifyImagePropertyExample(OH\_ImageSourceNative \*source) {
        if (!source) {
            OH\_LOG\_ERROR(LOG\_APP, "ModifyImagePropertyExample: source is nullptr");
            return;
        }
        const std::string keyStr = OHOS\_IMAGE\_PROPERTY\_ORIENTATION;
        const std::string valueStr = "Top-left";
        Image\_String key{const\_cast<char \*>(keyStr.c\_str()), keyStr.length()};
        Image\_String value{const\_cast<char \*>(valueStr.c\_str()), valueStr.length()};
    
        Image\_ErrorCode ret = OH\_ImageSourceNative\_ModifyImageProperty(source, &key, &value);
        if (ret != IMAGE\_SUCCESS) {
            OH\_LOG\_ERROR(LOG\_APP, "ModifyImageProperty failed, code=%{public}d", ret);
            return;
        }
    
        OH\_LOG\_INFO(LOG\_APP, "ModifyImageProperty success, key=%{public}s, value=%{public}s", keyStr.c\_str(),
                    valueStr.c\_str());
    }
