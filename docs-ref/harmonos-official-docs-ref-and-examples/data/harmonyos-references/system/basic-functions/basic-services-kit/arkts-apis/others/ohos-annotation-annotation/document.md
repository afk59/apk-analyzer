# @ohos.annotation (Annotation)

The **annotation** module defines the annotation types of HarmonyOS ArkTS APIs, such as the minimum available version of the lifecycle.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5b/v3/qQeIOGPmQH-wKCNE_mVIFw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062357Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=D68E8E939D82F38DBC347AE3B7FF4F3FE96A1862BFD9982DEA1C5848066B8C4F)

-   The initial APIs of this module are supported since API version 22. Newly added APIs will be marked with a superscript to indicate their earliest API version.

#### Modules to Import

import { Available } from '@kit.BasicServicesKit';

#### Available

@interface Available { minApiVersion: string = '' }

Annotates the minimum available version supported by an API. This annotation capability is provided by the system and can be used on classes, APIs, variables, types, modules, and enums. After the annotation is added to the source code, the compilation tool checks for potential compatibility issues. If the value of **minApiVersion** is greater than that of **compatibleSDKVersion** specified in **build-profile.json5**, a compatibility warning is reported.

**Widget capability**: This API can be used in ArkTS widgets since API version 22.

**Atomic service API**: This API can be used in atomic services since API version 22.

**Model restriction**: This API can be used only in the stage model.

**System capability**: SystemCapability.Base

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| minApiVersion | string | No | No | Minimum available version, which consists of two parts: system type and version number. The system type can be omitted only when it is HarmonyOS, for example, **'HarmonyOS 20'** or **'20'**. |

**Example**

import { Available, deviceInfo } from '@kit.BasicServicesKit';

@Available({minApiVersion: 'HarmonyOS 22'}) // Annotates the minimum available version of the function.
function myFunc() {}

@Available({minApiVersion: '22'}) // Annotates the minimum available version of the class. The default system type is HarmonyOS.
class MyClass {}

// Not recommended: If the compatibleSdkVersion value set in the build-profile.json5 file in the project root directory is less than 22 and the myFunc method is directly called without version check, the compiler throws a warning at the call of myFunc, indicating that the method may fail to run on devices of earlier versions.
myFunc();

// Recommended approach 1: Use deviceInfo.sdkApiVersion to obtain the API version of system software for judgment, which can prevent exceptions on devices of earlier versions and eliminate compilation warnings.
if (deviceInfo.sdkApiVersion >= 22) {
  myFunc();
} else {
  // Select an approach for devices of earlier versions based on the service logic.
}

// Recommended approach 2: Annotate the start version information of @Available on the parent function (or class) where myFunc is called. If the new version number is not lower than the minimum available version of myFunc, the compilation warning is cleared.
@Available({minApiVersion: 'HarmonyOS 22'})
function myNewFunc() {
  myFunc();
}
