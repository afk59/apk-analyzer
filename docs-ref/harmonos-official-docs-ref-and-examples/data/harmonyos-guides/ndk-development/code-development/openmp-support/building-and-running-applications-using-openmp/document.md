# Building and Running Applications Using OpenMP

The HarmonyOS NDK provides dynamic and static library files of OpenMP so that you can use OpenMP in native applications. This topic guides you through on how to call library files in [DevEco Studio](https://developer.huawei.com/consumer/en/deveco-studio/) to use OpenMP. For details about the APIs and examples, see [clang-OpenMPSupport](https://clang.llvm.org/docs/OpenMPSupport.html).

#### How to Develop

## Creating a Native C++ Project

[Creating an NDK Project](../../../creating-an-ndk-project/document.md)

## Adding Dependencies

There are two ways to incorporate the OpenMP library: static linking and dynamic linking.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/de/v3/d1lMMC-BQWKlNcaOgUcsdA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062135Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=4C5B3D8F0BB0C0F2A73BC0A6A2C77D0A1FB8CE5DEC51D0831AC672B6F0FD1783)

The [OpenMP Tools Interface (OMPT)](https://www.openmp.org/spec-html/5.0/openmpsu15.html#x25-240001.5.1) tool can be used only for static linking.

**Static Linking**

(1) Open the **entry/src/main/cpp/CMakeLists.txt** file, and add the static library **libomp.a** and log dependency **libhilog\_ndk.z.so** to **target\_link\_libraries**.

target\_link\_libraries(entry PUBLIC libomp.a libace\_napi.z.so libhilog\_ndk.z.so)

(2) Open the **entry/build-profile.json5** file, and add **\-static-openmp -fopenmp** to **cppFlags** under **buildOption** > **externalNativeOptions**.

"buildOption": {
    "externalNativeOptions": {
      "path": "./src/main/cpp/CMakeLists.txt",
      "arguments": "",
      "cppFlags": "-static-openmp -fopenmp",
    }
  }

**Dynamic linking**

(1) Open the **entry/src/main/cpp/CMakeLists.txt** file, and add the dynamic library **libomp.so** and log dependency **libhilog\_ndk.z.so** to **target\_link\_libraries**.

target\_link\_libraries(entry PUBLIC libomp.so libace\_napi.z.so libhilog\_ndk.z.so)

(2) Open the **entry/build-profile.json5** file, and add **\-fopenmp** to **cppFlags** under **buildOption** > **externalNativeOptions**.

"buildOption": {
    "externalNativeOptions": {
      "path": "./src/main/cpp/CMakeLists.txt",
      "arguments": "",
      "cppFlags": "-fopenmp",
    }
  }

(3) Copy the dynamic library file **libomp.so** in the {SDK installation directory}{Version number}**\\HarmonyOS\\native\\llvm\\lib\\aarch64-linux-ohos** directory to the **entry/libs/arm64-v8a** directory of the project.

## Modifying Source Files

(1) In **entry/src/main/cpp/napi\_init.cpp**, include the **omp.h** header file, and add the **OmpTest** function.

#include "napi/native\_api.h"
#include "omp.h"
#include "hilog/log.h"

#undef LOG\_DOMAIN
#undef LOG\_TAG
#define LOG\_DOMAIN 0x3200 // Global domain, which identifies the service domain.
#define LOG\_TAG "MY\_TAG"  // Global tag, which identifies the module log tag.

static napi\_value OmpTest(napi\_env env, napi\_callback\_info info)
{

    OH\_LOG\_INFO(LOG\_APP, "=================Hello OpenMP test.====================");
    #pragma omp parallel
    {
        OH\_LOG\_INFO(LOG\_APP, "Hello OpenMP!");
    }
    return nullptr;
}

EXTERN\_C\_START
static napi\_value Init(napi\_env env, napi\_value exports)
{
    napi\_property\_descriptor desc\[\] = {
        { "ompTest", nullptr, OmpTest, nullptr, nullptr, nullptr, napi\_default, nullptr }
    };
    napi\_define\_properties(env, exports, sizeof(desc) / sizeof(desc\[0\]), desc);
    return exports;
}
EXTERN\_C\_END

static napi\_module demoModule = {
    .nm\_version = 1,
    .nm\_flags = 0,
    .nm\_filename = nullptr,
    .nm\_register\_func = Init,
    .nm\_modname = "entry",
    .nm\_priv = ((void\*)0),
    .reserved = { 0 },
};

extern "C" \_\_attribute\_\_((constructor)) void RegisterEntryModule(void)
{
    napi\_module\_register(&demoModule);
}

(2) In **entry/src/main/cpp/types/libentry/Index.d.ts**, export the **ompTest** function.

export const ompTest: () => null;

(3) In **entry/src/main/ets/pages/Index.ets**, call the **ompTest** function.

import testNapi from 'libentry.so';

@Entry
@Component
struct Index {
  @State message: string = 'Hello OpenMP';

  build() {
    Row() {
      Column() {
        Text(this.message)
          .fontSize(50)
          .fontWeight(FontWeight.Bold)
          .onClick(() => {
            testNapi.ompTest();
          })
      }
      .width('100%')
    }
    .height('100%')
  }
}

## Running the Application and Verifying the Result

Check the device connection and [sign the application](https://developer.huawei.com/consumer/en/doc/harmonyos-guides-V5/ide-signing-V5) information. Click the **Run** button in the upper right corner of DevEco Studio. After the application is started, the **Hello OpenMP** page is displayed on the device. Tap **Hello OpenMP** and view the **Log** page on DevEco Studio. You can see multiple "Hello OpenMP!" messages.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/50/v3/gwZFy6VdQ9u_g5E9X5Nqrg/en-us_image_0000002568765027.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062135Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=82073F250B4B1EEAEB0337E5B6720992490EF7A176F071C5C5FFDB12254FAC47)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/64/v3/zHW8-lweTaKH0QADkEBe4Q/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062135Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=63995CC2DD175E727341F33DE3C5E79B4DF8F8AE1C567467FB3FA6BD07D6ADAE)

When an OpenMP application is running, the error message "dlopen\_impl load library header failed for libarcher.so" will be displayed in HiLog, as shown in the following figure. The **libarcher.so** file in the error information is used only when the OpenMP application has Tsan enabled. Currently, HarmonyOS does not support Tsan of OpenMP applications. Therefore, this error message does not affect the normal running of the application and can be ignored.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/14/v3/TAe0yc9IQOGjCeHHafM9iw/en-us_image_0000002537765302.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062135Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=9EB838D3DE0FDE433A0E2D05E77BE0C0E686BD61A2DDFA1F7E18A9024418373C)
