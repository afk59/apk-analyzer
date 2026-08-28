# Vibrator Development (C/C++)

#### When to Use

You can set different vibration effects as needed, for example, customizing the vibration intensity, frequency, and duration for button touches, alarm clocks, and incoming calls.

For details about the APIs, see [Vibrator](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-vibrator).

#### Function Description

| Name | Description |
| :-- | :-- |
| OHOS::Sensors::OH\_Vibrator\_PlayVibration(int32\_t duration, Vibrator\_Attribute attribute) | Controls the vibrator to vibrate continuously for a given duration. |
| OHOS::Sensors::OH\_Vibrator\_PlayVibrationCustom(Vibrator\_FileDescription fileDescription, Vibrator\_Attribute vibrateAttribute) | Configures the vibrator to vibrate with the custom sequence. |
| OHOS::Sensors::OH\_Vibrator\_Cancel() | Stops the vibration. |

#### Vibration Effect Description

Currently, two types of vibration effects are supported.

## Fixed-Duration Vibration

Only a fixed duration is passed in, and the device vibrates based on the default intensity and frequency.

## Custom Vibration

Custom vibration enables you to design desired vibration effects by customizing a vibration configuration file and orchestrating vibration forms based on the corresponding rules.

#### How to Develop

1.  Create a native C++ project.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7a/v3/Isp0xO7DQL-gUr1T14ZF_g/en-us_image_0000002568684829.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062025Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=CF4B3F891CD4A41BA389F17724D60664FF2A2342EE6E6EFC27D6EF4F41A3AFE9)
    
2.  Before using the vibrator on a device, you must declare the **ohos.permission.VIBRATE** permission. For details, see [Declaring Permissions](../../../../security/application-access-control/application-permission-management/requesting-application-permissions/declaring-permissions/document.md).
    
    "requestPermissions": \[
      {
        "name": "ohos.permission.VIBRATE"
      }
    \]
    
3.  Add the dynamic dependency libraries into the **CMakeLists.txt** file.
    
    target\_link\_libraries(entry PUBLIC libace\_napi.z.so)
    target\_link\_libraries(entry PUBLIC libhilog\_ndk.z.so)
    target\_link\_libraries(entry PUBLIC libohvibrator.z.so)
    target\_link\_libraries(entry PUBLIC librawfile.z.so)
    
4.  Import modules.
    
    #include <sensors/vibrator.h>
    #include "napi/native\_api.h"
    #include "hilog/log.h"
    #include <thread>
    #include <fcntl.h>
    #include <unistd.h>
    #include <sys/stat.h>
    #include <rawfile/raw\_file\_manager.h>
    
5.  Define constants.
    
    const int VIBRATOR\_LOG\_DOMAIN = 0xD002701;
    const char \*TAG = "\[NativeVibratorTest\]";
    constexpr int32\_t TIME\_WAIT\_FOR\_OP = 2;
    
6.  Configure the vibrator to vibrate continuously for a given duration.
    
    static napi\_value PlayVibrationInDuration(napi\_env env, napi\_callback\_info info)
    {
        Vibrator\_Attribute vibrateAttribute;
        vibrateAttribute.usage = VIBRATOR\_USAGE\_ALARM;
        // Control the vibrator to vibrate continuously for a given duration.
        int32\_t ret = OH\_Vibrator\_PlayVibration(2000, vibrateAttribute);
        if (ret != 0) {
            OH\_LOG\_Print(LOG\_APP, LOG\_ERROR, VIBRATOR\_LOG\_DOMAIN, TAG, "vibration fail");
            return nullptr;
        }
        OH\_LOG\_Print(LOG\_APP, LOG\_INFO, VIBRATOR\_LOG\_DOMAIN, TAG, "vibration successful");
        std::this\_thread::sleep\_for(std::chrono::milliseconds(TIME\_WAIT\_FOR\_OP));
        // Stop the vibration.
        ret = OH\_Vibrator\_Cancel();
        if (ret != 0) {
            OH\_LOG\_Print(LOG\_APP, LOG\_ERROR, VIBRATOR\_LOG\_DOMAIN, TAG, "cancel vibration fail");
            return nullptr;
        }
        return nullptr;
    }
    
7.  Configure the vibrator to vibrate with the custom sequence.
    
    static napi\_value PlayVibrationCustom(napi\_env env, napi\_callback\_info info)
    {
        size\_t argc = 1;
        napi\_value argv\[1\] = { nullptr };
        // Obtain arguments of the native API.
        napi\_get\_cb\_info(env, info, &argc, argv, nullptr, nullptr);
    
        // argv\[0\] is the first parameter of the function, which is a JS resource object. The  OH\_ResourceManager\_InitNativeResourceManager function converts this JS resource object into a native object.
        NativeResourceManager \*mNativeResMgr = OH\_ResourceManager\_InitNativeResourceManager(env, argv\[0\]);
        if (mNativeResMgr == nullptr) {
            OH\_LOG\_Print(LOG\_APP, LOG\_ERROR, VIBRATOR\_LOG\_DOMAIN, TAG, "Get native resourceMagr failed");
            return nullptr;
        }
        // Obtain the rawFile pointer object.
        std::string fileName = "coin\_drop.json";
        RawFile \*rawFile = OH\_ResourceManager\_OpenRawFile(mNativeResMgr, fileName.c\_str());
        if (rawFile == nullptr) {
            OH\_ResourceManager\_ReleaseNativeResourceManager(mNativeResMgr);
            OH\_LOG\_Print(LOG\_APP, LOG\_ERROR, VIBRATOR\_LOG\_DOMAIN, TAG, "Get native rawFile failed");
            return nullptr;
        }
        // Obtain the FD of the rawfile, that is, RawFileDescriptor {fd, offset, length}.
        RawFileDescriptor descriptor;
        OH\_ResourceManager\_GetRawFileDescriptor(rawFile, descriptor);
        Vibrator\_FileDescription fileDescription = {
            .fd = descriptor.fd,
            .offset = descriptor.start,
            .length = descriptor.length
        };
        Vibrator\_Attribute vibrateAttribute = {
            .usage = VIBRATOR\_USAGE\_RING
        };
        // Configure the vibrator to vibrate with the custom sequence.
        int32\_t ret = OH\_Vibrator\_PlayVibrationCustom(fileDescription, vibrateAttribute);
        bool isSuccess = ((ret == 0) || (ret == UNSUPPORTED));
        if (!isSuccess) {
            OH\_LOG\_Print(LOG\_APP, LOG\_INFO, VIBRATOR\_LOG\_DOMAIN, TAG, "Vibratecustom fail");
        } else {
            OH\_LOG\_Print(LOG\_APP, LOG\_INFO, VIBRATOR\_LOG\_DOMAIN, TAG, "Vibratecustom successful");
        }
        std::this\_thread::sleep\_for(std::chrono::milliseconds(TIME\_WAIT\_FOR\_OP));
        // Stop the vibration.
        OH\_Vibrator\_Cancel();
        // Close the rawFile pointer object.
        OH\_ResourceManager\_CloseRawFile(rawFile);
        OH\_ResourceManager\_ReleaseNativeResourceManager(mNativeResMgr);
        return nullptr;
    }
    
8.  Add related APIs to the **Init** function.
    
    EXTERN\_C\_START
    static napi\_value Init(napi\_env env, napi\_value exports)
    {
        napi\_property\_descriptor desc\[\] = {
            {"playVibrationInDuration", nullptr, PlayVibrationInDuration, nullptr, nullptr, nullptr, napi\_default, nullptr},
            {"playVibrationCustom", nullptr, PlayVibrationCustom, nullptr, nullptr, nullptr, napi\_default, nullptr}
        };
        napi\_define\_properties(env, exports, sizeof(desc) / sizeof(desc\[0\]), desc);
        return exports;
    }
    EXTERN\_C\_END
    
9.  Introduce the NAPI APIs to the **index.d.ts** file in **types/libentry**.
    
    export const playVibrationInDuration: () => object;
    export const playVibrationCustom: (resmgr: object) => object;
    
10.  Write the application entry call code.
     
     import { BusinessError } from '@kit.BasicServicesKit';
     import { hilog } from '@kit.PerformanceAnalysisKit';
     import { resourceManager } from '@kit.LocalizationKit';
     import vibratorCapi from 'libentry.so';
     
     const DOMAIN = 0xD002701;
     // ...
               try {
                 vibratorCapi.playVibrationInDuration();
                 // ...
               } catch (error) {
                 let e: BusinessError = error as BusinessError;
                 hilog.error(DOMAIN, 'testTag', \`Failed to invoke playVibrationInDuration. Code: ${e.code}, message: ${e.message}\`);
               }
               // ...
               try {
                 vibratorCapi.playVibrationCustom(this.getUIContext().getHostContext()?.resourceManager);
                 // ...
               } catch (error) {
                 let e: BusinessError = error as BusinessError;
                 hilog.error(DOMAIN, 'testTag', \`Failed to invoke playVibrationCustom. Code: ${e.code}, message: ${e.message}\`);
               }
