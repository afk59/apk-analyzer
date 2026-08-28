# @ohos.resourceManager (Resource Management)

The **resourceManager** module provides the resource management functionality. It allows an application to obtain the best matched application resources or system resources based on the specified [configuration](#configuration). For details about the matching rules, see [Matching Resources](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/resource-categories-and-access#matching-resources).

The configuration includes language, region, screen orientation, mobile country code (MCC), mobile network code (MNC), device capability, and density.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8b/v3/AjjG0vNfR6qMDFsjoKg1IQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062326Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=65D2D98EA118925B7ED5E5675DBAC03832641B10CC62F63C6FEED8435E625A61)

The initial APIs of this module are supported since API version 6. Newly added APIs will be marked with a superscript to indicate their earliest API version.

#### Modules to Import

import { resourceManager } from '@kit.LocalizationKit';

#### How to Use

Since API version 9, the stage model allows an application to obtain a **ResourceManager** object via **Context**. You do not need to import the module.

In the FA model, you need to import the module and then call [getResourceManager](#resourcemanagergetresourcemanager) to obtain a **ResourceManager** object.

For details about how to reference context in the stage model, see [Context in the Stage Model](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/application-context-stage).

import { UIAbility } from '@kit.AbilityKit';
import { window } from '@kit.ArkUI';

export default class EntryAbility extends UIAbility {
  onWindowStageCreate(windowStage: window.WindowStage) {
    let context = this.context;
    let resourceManager = context.resourceManager;
  }
}

#### resourceManager.getResourceManager

getResourceManager(callback: AsyncCallback<ResourceManager>): void

Obtains the **ResourceManager** object of this application. This API uses an asynchronous callback to return the result.

**System capability**: SystemCapability.Global.ResourceManager

**Model restriction**: This API can be used only in the FA model.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | [AsyncCallback](#asynccallbackdeprecated)<[ResourceManager](#resourcemanager)\> | Yes | Callback used to return the **ResourceManager** object. |

**Example**

import resourceManager from '@ohos.resourceManager';
// Use this method to import the module in the FA model.

export default {
    onCreate() {
        resourceManager.getResourceManager((error, mgr) => {
            if (error != null) {
                console.error("error is " + error);
                return;
            }
            // Replace "test" with the actual resource name.
            mgr.getStringByName('test', (error, value) => {
                if (error) {
                    console.error("error is " + JSON.stringify(error));
                } else {
                    console.info("success is " + value);
                }

            });
        });
    }
};

#### resourceManager.getResourceManager

getResourceManager(bundleName: string, callback: AsyncCallback<ResourceManager>): void

Obtains the **ResourceManager** object of the specified application. This API uses an asynchronous callback to return the result.

**System capability**: SystemCapability.Global.ResourceManager

**Model restriction**: This API can be used only in the FA model.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| bundleName | string | Yes | Bundle name of the application. |
| callback | [AsyncCallback](#asynccallbackdeprecated)<[ResourceManager](#resourcemanager)\> | Yes | Callback used to return the **ResourceManager** object. |

**Example**

import resourceManager from '@ohos.resourceManager';
// Use this method to import the module in the FA model.

// Replace 'com.example.testapp' with the actual application package name.
const BUNDLE\_NAME = 'com.example.testapp';

export default {
    onCreate() {
        resourceManager.getResourceManager(BUNDLE\_NAME, (error, mgr) => {
            if (error != null) {
                console.error("getResourceManager error is " + error);
                return;
            }
            // Replace "test" with the actual resource name.
            mgr.getStringByName('test', (error, value) => {
                if (error) {
                    console.error("getResourceManager error is " + JSON.stringify(error));
                } else {
                    console.info("getResourceManager success is " + value);
                }
            });
        });
    }
};

#### resourceManager.getResourceManager

getResourceManager(): Promise<ResourceManager>

Obtains the **ResourceManager** object of this application. This API uses a promise to return the result.

**System capability**: SystemCapability.Global.ResourceManager

**Model restriction**: This API can be used only in the FA model.

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<[ResourceManager](#resourcemanager)\> | Promise used to return the **ResourceManager** object. |

**Example**

import resourceManager from '@ohos.resourceManager';
// Use this method to import the module in the FA model.

export default {
    onCreate() {
        resourceManager.getResourceManager().then(resMgr => {
            try {
                // Replace "test" with the actual resource name.
                let testStr = resMgr.getStringByNameSync('test')
                console.info("getResourceManager success is " + testStr);
            } catch (error) {
                console.error("getResourceManager error is " + JSON.stringify(error));
            }
        }).catch(error => {
            console.error("getResourceManager error is " + error);
        });
    }
};

#### resourceManager.getResourceManager

getResourceManager(bundleName: string): Promise<ResourceManager>

Obtains the **ResourceManager** object of the specified application. This API uses a promise to return the result.

**System capability**: SystemCapability.Global.ResourceManager

**Model restriction**: This API can be used only in the FA model.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| bundleName | string | Yes | Bundle name of the application. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<[ResourceManager](#resourcemanager)\> | Promise used to return the **ResourceManager** object. |

**Example**

import resourceManager from '@ohos.resourceManager';
// Use this method to import the module in the FA model.

// Replace 'com.example.testapp' with the actual application package name.
const BUNDLE\_NAME = 'com.example.testapp';

export default {
    onCreate() {
        resourceManager.getResourceManager(BUNDLE\_NAME).then(resMgr => {
            try {
                // Replace "test" with the actual resource name.
                let testStr = resMgr.getStringByNameSync('test')
                console.info("getResourceManager success is " + testStr);
            } catch (error) {
                console.error("getResourceManager error is " + JSON.stringify(error));
            }
        }).catch(error => {
            console.error("getResourceManager error is " + error);
        });
    }
};

#### resourceManager.getSysResourceManager20+

getSysResourceManager(): ResourceManager

Obtains a **ResourceManager** object.

**Atomic service API**: This API can be used in atomic services since API version 20.

**System capability**: SystemCapability.Global.ResourceManager

**Return value**

| Type | Description |
| :-- | :-- |
| [ResourceManager](#resourcemanager) | **ResourceManager** object. |

**Error codes**

For details about the error codes, see [Resource Manager Error Codes](../../error-codes/resource-manager-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 9001009 | Failed to access the system resource. which is not mapped to application sandbox, This error code will be thrown. |

**Example**

import { resourceManager } from '@kit.LocalizationKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let systemResourceManager = resourceManager.getSysResourceManager();
  // Replace 'sys.string.ohos\_lab\_vibrate' with the actual resource.
  systemResourceManager.getStringValue($r('sys.string.ohos\_lab\_vibrate').id).then((value: string) => {
    let str = value;
  }).catch((error: BusinessError) => {
    console.error(\`systemResourceManager getStringValue promise error: ${error}\`);
  });
} catch (error) {
  let code = (error as BusinessError).code;
  let message = (error as BusinessError).message;
  console.error(\`getSysResourceManager failed, error code: ${code}, message: ${message}.\`);
}

#### Direction

Enumerates the screen directions.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Global.ResourceManager

| Name | Value | Description |
| :-- | :-- | :-- |
| DIRECTION\_VERTICAL | 0 | Portrait |
| DIRECTION\_HORIZONTAL | 1 | Landscape |

#### DeviceType

Enumerates the device types.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Global.ResourceManager

| Name | Value | Description |
| :-- | :-- | :-- |
| DEVICE\_TYPE\_PHONE | 0x00 | Mobile phone |
| DEVICE\_TYPE\_TABLET | 0x01 | Tablet |
| DEVICE\_TYPE\_CAR | 0x02 | Car |
| DEVICE\_TYPE\_PC | 0x03 | PC |
| DEVICE\_TYPE\_TV | 0x04 | TV |
| DEVICE\_TYPE\_WEARABLE | 0x06 | Wearable |
| DEVICE\_TYPE\_2IN111+ | 0x07 | 2in1 device |

#### ScreenDensity

Enumerates the screen density types.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Global.ResourceManager

| Name | Value | Description |
| :-- | :-- | :-- |
| SCREEN\_SDPI | 120 | Small-scale DPI. |
| SCREEN\_MDPI | 160 | Medium-scale DPI. |
| SCREEN\_LDPI | 240 | Large-scale DPI. |
| SCREEN\_XLDPI | 320 | Extra-large-scale DPI. |
| SCREEN\_XXLDPI | 480 | Extra-extra-large-scale DPI. |
| SCREEN\_XXXLDPI | 640 | Extra-extra-extra-large-scale DPI. |

#### ColorMode12+

Defines the color mode of the current device.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Global.ResourceManager

| Name | Value | Description |
| :-- | :-- | :-- |
| DARK | 0 | Dark mode. |
| LIGHT | 1 | Light mode. |

#### Configuration

Defines the device configuration.

**System capability**: SystemCapability.Global.ResourceManager

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| direction | [Direction](#direction) | No | No | 
Screen orientation modes.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| locale | string | No | No | 

Language locale.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| deviceType12+ | [DeviceType](#devicetype) | No | No | 

Device type.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| screenDensity12+ | [ScreenDensity](#screendensity) | No | No | 

Screen density

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| colorMode12+ | [ColorMode](#colormode12) | No | No | 

Color mode.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| mcc12+ | number | No | No | 

Mobile country code (MCC).

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| mnc12+ | number | No | No | 

Mobile network code (MNC).

**Atomic service API**: This API can be used in atomic services since API version 12.

 |

#### DeviceCapability

Defines the device capability.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Global.ResourceManager

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| screenDensity | [ScreenDensity](#screendensity) | No | No | Screen density of the device. |
| deviceType | [DeviceType](#devicetype) | No | No | Device type. |

#### RawFileDescriptor9+

type RawFileDescriptor = \_RawFileDescriptor

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Global.ResourceManager

| Type | Description |
| :-- | :-- |
| [\_RawFileDescriptor](../global/rawfiledescriptor/document.md#rawfiledescriptor-1) | File descriptor (fd) of the HAP where the rawfile is located. |

#### Resource9+

type Resource = \_Resource

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Global.ResourceManager

| Type | Description |
| :-- | :-- |
| [\_Resource](../global/resource/document.md#resource-1) | Resource information, including the resource ID, application package name, and module name. Generally, you can use **$r** to obtain the resource information. |

#### ResourceManager

Provides APIs for accessing application resources and system resources.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/66/v3/PaFlkVTjRwC_IC9XsJXCoA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062326Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=5E6A128645FE38F3C3E165F1C8C6F652CA97C781F56DA1978B5A3D74CAB270AF)

-   The methods involved in **ResourceManager** are applicable only to the TypeScript-based declarative development paradigm.
    
-   Resource files are defined in the **resources** directory of the project. You can obtain resource values such as strings, string arrays, and colors based on the specified **resName**, **resId**, or **Resource** object. **resName** indicates the resource name, **resId** indicates the resource ID, which can be obtained through $r(\*resource-address\*).id, for example, $r('app.string.test').id.
    
-   No matter whether resources are in the same HAP or different HAPs or HSPs, you are advised to use the API with **resName** or **resId** specified. Using the **Resource** object will take a longer time. If the resources are in different HAPs or HSPs, you first need to use [createModuleContext](../../../ability-kit/arkts-apis/stage-model/ohos-app-ability-application-application-utility-class/document.md#applicationcreatemodulecontext) to create the context of the corresponding module and then call the API with **resName** or **resId** specified. For details, see [Accessing Resources](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/resource-categories-and-access#accessing-resources).
    
-   For details about the content of the test files used in the sample code, see [Appendix](#appendix).
    

#### \[h2\]getStringSync9+

getStringSync(resId: number): string

Obtains a string based on the specified resource ID. This API returns the result synchronously.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Global.ResourceManager

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| resId | number | Yes | Resource ID. |

**Return value**

| Type | Description |
| :-- | :-- |
| string | String corresponding to the specified resource ID. |

**Error codes**

For details about the error codes, see [Resource Manager Error Codes](../../error-codes/resource-manager-error-codes/document.md) and [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | If the input parameter invalid. Possible causes: Incorrect parameter types. |
| 9001001 | Invalid resource ID. |
| 9001002 | No matching resource is found based on the resource ID. |
| 9001006 | The resource is referenced cyclically. |

**Example**

// Resource file path: src/main/resources/base/element/string.json
{
  "string": \[
    {
      "name": "test",
      "value": "I'm a test string resource."
    }
  \]
}

import { AbilityConstant, UIAbility, Want } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

export default class EntryAbility extends UIAbility {
    onCreate(want: Want, launchParam: AbilityConstant.LaunchParam): void {
        try {
            // Replace 'app.string.test' with the actual resource.
            let testStr = this.context.resourceManager.getStringSync($r('app.string.test').id);
            console.info(\`getStringSync, result: ${testStr}\`);
            // Print the output result: getStringSync, result: I'm a test string resource.
        } catch (error) {
            let code = (error as BusinessError).code;
            let message = (error as BusinessError).message;
            console.error(\`getStringSync failed, error code: ${code}, message: ${message}.\`);
        }
    }
}

#### \[h2\]getStringSync10+

getStringSync(resId: number, ...args: Array<string | number>): string

Obtains a string based on the specified resource ID and formats the string based on **args**. This API returns the result synchronously.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Global.ResourceManager

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| resId | number | Yes | Resource ID. |
| ...args | Array<string | number> | No | 
Arguments for formatting strings.

Supported value types include %d, %f, %s, %%, %number$d, %number$f, and %number$s.

Note: %% is converted to %. **number** in %number$d indicates the sequence number of the parameter in **args**.

For example, %%d is converted to %d after formatting, and %1$d indicates that the first parameter is used.

 |

**Return value**

| Type | Description |
| :-- | :-- |
| string | Formatted string corresponding to the specified resource ID. |

**Error codes**

For details about the error codes, see [Resource Manager Error Codes](../../error-codes/resource-manager-error-codes/document.md) and [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | If the input parameter invalid. Possible causes: Incorrect parameter types. |
| 9001001 | Invalid resource ID. |
| 9001002 | No matching resource is found based on the resource ID. |
| 9001006 | The resource is referenced cyclically. |
| 9001007 | Failed to format the resource obtained based on the resource ID. |

**Example**

// Resource file path: src/main/resources/base/element/string.json
{
  "string": \[
    {
      "name": "test",
      "value": "I'm a %1$s, format int: %2$d, format float: %3$f."
    }
  \]
}

import { AbilityConstant, UIAbility, Want } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

export default class EntryAbility extends UIAbility {
    onCreate(want: Want, launchParam: AbilityConstant.LaunchParam): void {
        try {
            // Replace 'app.string.test' with the actual resource.
            let testStr = this.context.resourceManager.getStringSync($r('app.string.test').id, "format string", 10, 98.78);
            console.info(\`getStringSync, result: ${testStr}\`);
            // Print the output result: getStringSync, result: I'm a format string, format int: 10, format float: 98.78.
        } catch (error) {
            let code = (error as BusinessError).code;
            let message = (error as BusinessError).message;
            console.error(\`getStringSync failed, error code: ${code}, message: ${message}.\`);
        }
    }
}

#### \[h2\]getStringByNameSync9+

getStringByNameSync(resName: string): string

Obtains a string based on the specified resource name. This API returns the result synchronously.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Global.ResourceManager

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| resName | string | Yes | Resource name. |

**Return value**

| Type | Description |
| :-- | :-- |
| string | String corresponding to the specified resource name. |

**Error codes**

For details about the error codes, see [Resource Manager Error Codes](../../error-codes/resource-manager-error-codes/document.md) and [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | If the input parameter invalid. Possible causes: Incorrect parameter types. |
| 9001003 | Invalid resource name. |
| 9001004 | No matching resource is found based on the resource name. |
| 9001006 | The resource is referenced cyclically. |

**Example**

// Resource file path: src/main/resources/base/element/string.json
{
  "string": \[
    {
      "name": "test",
      "value": "I'm a test string resource."
    }
  \]
}

import { AbilityConstant, UIAbility, Want } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

export default class EntryAbility extends UIAbility {
    onCreate(want: Want, launchParam: AbilityConstant.LaunchParam): void {
        try {
            // Replace "test" with the actual resource.
            let testStr = this.context.resourceManager.getStringByNameSync("test");
            console.info(\`getStringByNameSync, result: ${testStr}\`);
            // Print the output result: getStringByNameSync, result: I'm a test string resource.
        } catch (error) {
            let code = (error as BusinessError).code;
            let message = (error as BusinessError).message;
            console.error(\`getStringByNameSync failed, error code: ${code}, message: ${message}.\`);
        }
    }
}

#### \[h2\]getStringByNameSync10+

getStringByNameSync(resName: string, ...args: Array<string | number>): string

Obtains a string based on the specified resource ame and formats the string based on **args**. This API returns the result synchronously.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Global.ResourceManager

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| resName | string | Yes | Resource name. |
| ...args | Array<string | number> | No | 
Arguments for formatting strings.

Supported value types include %d, %f, %s, %%, %number$d, %number$f, and %number$s.

Note: %% is converted to %. **number** in %number$d indicates the sequence number of the parameter in **args**.

For example, %%d is converted to %d after formatting, and %1$d indicates that the first parameter is used.

 |

**Return value**

| Type | Description |
| :-- | :-- |
| string | Formatted string corresponding to the specified resource name. |

**Error codes**

For details about the error codes, see [Resource Manager Error Codes](../../error-codes/resource-manager-error-codes/document.md) and [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | If the input parameter invalid. Possible causes: Incorrect parameter types. |
| 9001003 | Invalid resource name. |
| 9001004 | No matching resource is found based on the resource name. |
| 9001006 | The resource is referenced cyclically. |
| 9001008 | Failed to format the resource obtained based on the resource Name. |

**Example**

// Resource file path: src/main/resources/base/element/string.json
{
  "string": \[
    {
      "name": "test",
      "value": "I'm a %1$s, format int: %2$d, format float: %3$f."
    }
  \]
}

import { AbilityConstant, UIAbility, Want } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

export default class EntryAbility extends UIAbility {
    onCreate(want: Want, launchParam: AbilityConstant.LaunchParam): void {
        try {
            // Replace "test" with the actual resource.
            let testStr = this.context.resourceManager.getStringByNameSync("test", "format string", 10, 98.78);
            console.info(\`getStringByNameSync, result: ${testStr}\`);
            // Print the output result: getStringByNameSync, result: I'm a format string, format int: 10, format float: 98.78.
        } catch (error) {
            let code = (error as BusinessError).code;
            let message = (error as BusinessError).message;
            console.error(\`getStringByNameSync failed, error code: ${code}, message: ${message}.\`);
        }
    }
}

#### \[h2\]getStringValue9+

getStringValue(resId: number, callback: \_AsyncCallback<string>): void

Obtains a string based on the specified resource ID. This API uses an asynchronous callback to return the result.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Global.ResourceManager

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| resId | number | Yes | Resource ID. |
| callback | [\_AsyncCallback](../../../../system/basic-functions/basic-services-kit/arkts-apis/others/ohos-base-public-callback-information/document.md#asynccallback)<string> | Yes | Callback used to return the obtained string. |

**Error codes**

For details about the error codes, see [Resource Manager Error Codes](../../error-codes/resource-manager-error-codes/document.md) and [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | If the input parameter invalid. Possible causes: Incorrect parameter types. |
| 9001001 | Invalid resource ID. |
| 9001002 | No matching resource is found based on the resource ID. |
| 9001006 | The resource is referenced cyclically. |

**Example (stage)**

// Resource file path: src/main/resources/base/element/string.json
{
  "string": \[
    {
      "name": "test",
      "value": "I'm a test string resource."
    }
  \]
}

import { AbilityConstant, UIAbility, Want } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

export default class EntryAbility extends UIAbility {
    onCreate(want: Want, launchParam: AbilityConstant.LaunchParam): void {
        // Replace 'app.string.test' with the actual resource.
        this.context.resourceManager.getStringValue($r('app.string.test').id, (error: BusinessError, value: string) => {
            if (error != null) {
                console.error(\`callback getStringValue failed, error code: ${error.code}, message: ${error.message}.\`);
            } else {
                console.info(\`getStringValue, result: ${value}\`);
                // Print the output result: getStringValue, result: I'm a test string resource.
            }
        });
    }
}

#### \[h2\]getStringValue9+

getStringValue(resId: number): Promise<string>

Obtains a string based on the specified resource ID. This API uses a promise to return the result.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Global.ResourceManager

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| resId | number | Yes | Resource ID. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<string> | Promise used to return the obtained string. |

**Error codes**

For details about the error codes, see [Resource Manager Error Codes](../../error-codes/resource-manager-error-codes/document.md) and [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | If the input parameter invalid. Possible causes: Incorrect parameter types. |
| 9001001 | Invalid resource ID. |
| 9001002 | No matching resource is found based on the resource ID. |
| 9001006 | The resource is referenced cyclically. |

**Example**

// Resource file path: src/main/resources/base/element/string.json
{
  "string": \[
    {
      "name": "test",
      "value": "I'm a test string resource."
    }
  \]
}

import { AbilityConstant, UIAbility, Want } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

export default class EntryAbility extends UIAbility {
    onCreate(want: Want, launchParam: AbilityConstant.LaunchParam): void {
        // Replace 'app.string.test' with the actual resource.
        this.context.resourceManager.getStringValue($r('app.string.test').id).then((value: string) => {
            console.info(\`getStringValue, result: ${value}\`);
            // Print the output result: getStringValue, result: I'm a test string resource.
        }).catch((error: BusinessError) => {
            console.error(\`promise getStringValue failed, error code: ${error.code}, message: ${error.message}.\`);
        });
    }
}

#### \[h2\]getStringByName9+

getStringByName(resName: string, callback: \_AsyncCallback<string>): void

Obtains a string based on the specified resource name. This API uses an asynchronous callback to return the result.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Global.ResourceManager

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| resName | string | Yes | Resource name. |
| callback | [\_AsyncCallback](../../../../system/basic-functions/basic-services-kit/arkts-apis/others/ohos-base-public-callback-information/document.md#asynccallback)<string> | Yes | Callback used to return the result, which is the string corresponding to the specified resource ID. |

**Error codes**

For details about the error codes, see [Resource Manager Error Codes](../../error-codes/resource-manager-error-codes/document.md) and [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | If the input parameter invalid. Possible causes: Incorrect parameter types. |
| 9001003 | Invalid resource name. |
| 9001004 | No matching resource is found based on the resource name. |
| 9001006 | The resource is referenced cyclically. |

**Example**

// Resource file path: src/main/resources/base/element/string.json
{
  "string": \[
    {
      "name": "test",
      "value": "I'm a test string resource."
    }
  \]
}

import { AbilityConstant, UIAbility, Want } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

export default class EntryAbility extends UIAbility {
    onCreate(want: Want, launchParam: AbilityConstant.LaunchParam): void {
        // Replace "test" with the actual resource.
        this.context.resourceManager.getStringByName("test", (error: BusinessError, value: string) => {
            if (error != null) {
                console.error(\`callback getStringByName failed, error code: ${error.code}, message: ${error.message}.\`);
            } else {
                console.info(\`getStringByName, result: ${value}\`);
                // Print the output result: getStringByName, result: I'm a test string resource.
            }
        });
    }
}

#### \[h2\]getStringByName9+

getStringByName(resName: string): Promise<string>

Obtains a string based on the specified resource name. This API uses a promise to return the result.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Global.ResourceManager

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| resName | string | Yes | Resource name. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<string> | Promise used to return the obtained string. |

**Error codes**

For details about the error codes, see [Resource Manager Error Codes](../../error-codes/resource-manager-error-codes/document.md) and [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | If the input parameter invalid. Possible causes: Incorrect parameter types. |
| 9001003 | Invalid resource name. |
| 9001004 | No matching resource is found based on the resource name. |
| 9001006 | The resource is referenced cyclically. |

**Example**

// Resource file path: src/main/resources/base/element/string.json
{
  "string": \[
    {
      "name": "test",
      "value": "I'm a test string resource."
    }
  \]
}

import { AbilityConstant, UIAbility, Want } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

export default class EntryAbility extends UIAbility {
    onCreate(want: Want, launchParam: AbilityConstant.LaunchParam): void {
        // Replace "test" with the actual resource.
        this.context.resourceManager.getStringByName("test").then((value: string) => {
            console.info(\`getStringByName, result: ${value}\`);
            // Print the output result: getStringByName, result: I'm a test string resource.
        }).catch((error: BusinessError) => {
            console.error(\`promise getStringByName failed, error code: ${error.code}, message: ${error.message}.\`);
        });
    }
}

#### \[h2\]getStringArrayValueSync10+

getStringArrayValueSync(resId: number): Array<string>

Obtains a string array based on the specified resource ID. This API returns the result synchronously.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Global.ResourceManager

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| resId | number | Yes | Resource ID. |

**Return value**

| Type | Description |
| :-- | :-- |
| Array<string> | String array corresponding to the specified resource ID. |

**Error codes**

For details about the error codes, see [Resource Manager Error Codes](../../error-codes/resource-manager-error-codes/document.md) and [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | If the input parameter invalid. Possible causes: Incorrect parameter types. |
| 9001001 | Invalid resource ID. |
| 9001002 | No matching resource is found based on the resource ID. |
| 9001006 | The resource is referenced cyclically. |

**Example**

// Resource file path: src/main/resources/base/element/strarray.json
{
  "strarray": \[
    {
      "name": "test",
      "value": \[
        {
          "value": "I'm one of the array's values."
        }
      \]
    }
  \]
}

import { AbilityConstant, UIAbility, Want } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

export default class EntryAbility extends UIAbility {
    onCreate(want: Want, launchParam: AbilityConstant.LaunchParam): void {
        try {
            // Replace 'app.strarray.test' with the actual resource.
            let strArray: Array<string> = this.context.resourceManager.getStringArrayValueSync($r('app.strarray.test').id);
            console.info(\`getStringArrayValueSync, result: ${strArray\[0\]}\`);
            // Print the output result: getStringArrayValueSync, result: I'm one of the array's values.
        } catch (error) {
            let code = (error as BusinessError).code;
            let message = (error as BusinessError).message;
            console.error(\`getStringArrayValueSync failed, error code: ${code}, message: ${message}.\`);
        }
    }
}

#### \[h2\]getStringArrayByNameSync10+

getStringArrayByNameSync(resName: string): Array<string>

Obtains a string array based on the specified resource name. This API returns the result synchronously.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Global.ResourceManager

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| resName | string | Yes | Resource name. |

**Return value**

| Type | Description |
| :-- | :-- |
| Array<string> | String array corresponding to the specified resource name. |

**Error codes**

For details about the error codes, see [Resource Manager Error Codes](../../error-codes/resource-manager-error-codes/document.md) and [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | If the input parameter invalid. Possible causes: Incorrect parameter types. |
| 9001003 | Invalid resource name. |
| 9001004 | No matching resource is found based on the resource name. |
| 9001006 | The resource is referenced cyclically. |

**Example**

// Resource file path: src/main/resources/base/element/strarray.json
{
  "strarray": \[
    {
      "name": "test",
      "value": \[
        {
          "value": "I'm one of the array's values."
        }
      \]
    }
  \]
}

import { AbilityConstant, UIAbility, Want } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

export default class EntryAbility extends UIAbility {
    onCreate(want: Want, launchParam: AbilityConstant.LaunchParam): void {
        try {
            // Replace "test" with the actual resource.
            let strArray: Array<string> = this.context.resourceManager.getStringArrayByNameSync("test");
            console.info(\`getStringArrayByNameSync, result: ${strArray\[0\]}\`);
            // Print the output result: getStringArrayByNameSync, result: I'm one of the array's values.
        } catch (error) {
            let code = (error as BusinessError).code;
            let message = (error as BusinessError).message;
            console.error(\`getStringArrayByNameSync failed, error code: ${code}, message: ${message}.\`);
        }
    }
}

#### \[h2\]getStringArrayValue9+

getStringArrayValue(resId: number, callback: \_AsyncCallback<Array<string>>): void

Obtains a string array based on the specified resource ID. This API uses an asynchronous callback to return the result.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Global.ResourceManager

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| resId | number | Yes | Resource ID. |
| callback | [\_AsyncCallback](../../../../system/basic-functions/basic-services-kit/arkts-apis/others/ohos-base-public-callback-information/document.md#asynccallback)<Array<string>> | Yes | Callback used to return the obtained string array. |

**Error codes**

For details about the error codes, see [Resource Manager Error Codes](../../error-codes/resource-manager-error-codes/document.md) and [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | If the input parameter invalid. Possible causes: Incorrect parameter types. |
| 9001001 | Invalid resource ID. |
| 9001002 | No matching resource is found based on the resource ID. |
| 9001006 | The resource is referenced cyclically. |

**Example**

// Resource file path: src/main/resources/base/element/strarray.json
{
  "strarray": \[
    {
      "name": "test",
      "value": \[
        {
          "value": "I'm one of the array's values."
        }
      \]
    }
  \]
}

import { AbilityConstant, UIAbility, Want } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

export default class EntryAbility extends UIAbility {
    onCreate(want: Want, launchParam: AbilityConstant.LaunchParam): void {
        // Replace 'app.strarray.test' with the actual resource.
        this.context.resourceManager.getStringArrayValue($r('app.strarray.test').id,
            (error: BusinessError, value: Array<string>) => {
                if (error != null) {
                    console.error(\`callback getStringArrayValue failed, error code: ${error.code}, message: ${error.message}.\`);
                } else {
                    console.info(\`getStringArrayValue, result: ${value\[0\]}\`);
                    // Print the output result: getStringArrayValue, result: I'm one of the array's values.
                }
            });
    }
}

#### \[h2\]getStringArrayValue9+

getStringArrayValue(resId: number): Promise<Array<string>>

Obtains a string array based on the specified resource ID. This API uses a promise to return the result.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Global.ResourceManager

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| resId | number | Yes | Resource ID. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<Array<string>> | Promise used to return the obtained string array. |

**Error codes**

For details about the error codes, see [Resource Manager Error Codes](../../error-codes/resource-manager-error-codes/document.md) and [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | If the input parameter invalid. Possible causes: Incorrect parameter types. |
| 9001001 | Invalid resource ID. |
| 9001002 | No matching resource is found based on the resource ID. |
| 9001006 | The resource is referenced cyclically. |

**Example**

// Resource file path: src/main/resources/base/element/strarray.json
{
  "strarray": \[
    {
      "name": "test",
      "value": \[
        {
          "value": "I'm one of the array's values."
        }
      \]
    }
  \]
}

import { AbilityConstant, UIAbility, Want } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

export default class EntryAbility extends UIAbility {
    onCreate(want: Want, launchParam: AbilityConstant.LaunchParam): void {
        // Replace 'app.strarray.test' with the actual resource.
        this.context.resourceManager.getStringArrayValue($r('app.strarray.test').id)
            .then((value: Array<string>) => {
                console.info(\`getStringArrayValue, result: ${value\[0\]}\`);
                // Print the output result: getStringArrayValue, result: I'm one of the array's values.
            })
            .catch((error: BusinessError) => {
                console.error(\`promise getStringArrayValue failed, error code: ${error.code}, message: ${error.message}.\`);
            });
    }
}

#### \[h2\]getStringArrayByName9+

getStringArrayByName(resName: string, callback: \_AsyncCallback<Array<string>>): void

Obtains a string array based on the specified resource name. This API uses an asynchronous callback to return the result.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Global.ResourceManager

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| resName | string | Yes | Resource name. |
| callback | [\_AsyncCallback](../../../../system/basic-functions/basic-services-kit/arkts-apis/others/ohos-base-public-callback-information/document.md#asynccallback)<Array<string>> | Yes | Callback used to return the obtained string array. |

**Error codes**

For details about the error codes, see [Resource Manager Error Codes](../../error-codes/resource-manager-error-codes/document.md) and [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | If the input parameter invalid. Possible causes: Incorrect parameter types. |
| 9001003 | Invalid resource name. |
| 9001004 | No matching resource is found based on the resource name. |
| 9001006 | The resource is referenced cyclically. |

**Example**

// Resource file path: src/main/resources/base/element/strarray.json
{
  "strarray": \[
    {
      "name": "test",
      "value": \[
        {
          "value": "I'm one of the array's values."
        }
      \]
    }
  \]
}

import { AbilityConstant, UIAbility, Want } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

export default class EntryAbility extends UIAbility {
    onCreate(want: Want, launchParam: AbilityConstant.LaunchParam): void {
        // Replace "test" with the actual resource.
        this.context.resourceManager.getStringArrayByName("test", (error: BusinessError, value: Array<string>) => {
            if (error != null) {
                console.error(\`callback getStringArrayByName failed, error code: ${error.code}, message: ${error.message}.\`);
            } else {
                let strArray = value;
                console.info(\`getStringArrayByName, result: ${value\[0\]}\`);
                // Print the output result: getStringArrayByName, result: I'm one of the array's values.
            }
        });
    }
}

#### \[h2\]getStringArrayByName9+

getStringArrayByName(resName: string): Promise<Array<string>>

Obtains a string array based on the specified resource name. This API uses a promise to return the result.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Global.ResourceManager

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| resName | string | Yes | Resource name. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<Array<string>> | Promise used to return the obtained string array. |

**Error codes**

For details about the error codes, see [Resource Manager Error Codes](../../error-codes/resource-manager-error-codes/document.md) and [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | If the input parameter invalid. Possible causes: Incorrect parameter types. |
| 9001003 | Invalid resource name. |
| 9001004 | No matching resource is found based on the resource name. |
| 9001006 | The resource is referenced cyclically. |

**Example**

// Resource file path: src/main/resources/base/element/strarray.json
{
  "strarray": \[
    {
      "name": "test",
      "value": \[
        {
          "value": "I'm one of the array's values."
        }
      \]
    }
  \]
}

import { AbilityConstant, UIAbility, Want } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

export default class EntryAbility extends UIAbility {
    onCreate(want: Want, launchParam: AbilityConstant.LaunchParam): void {
        // Replace "test" with the actual resource.
        this.context.resourceManager.getStringArrayByName("test")
            .then((value: Array<string>) => {
                console.info(\`getStringArrayByName, result: ${value\[0\]}\`);
                // Print the output result: getStringArrayByName, result: I'm one of the array's values.
            })
            .catch((error: BusinessError) => {
                console.error(\`promise getStringArrayByName failed, error code: ${error.code}, message: ${error.message}.\`);
            });
    }
}

#### \[h2\]getIntPluralStringValueSync18+

getIntPluralStringValueSync(resId: number, num: number, ...args: Array<string | number>): string

Obtains a [singular/plural](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/l10n-singular-plural) string based on the specified resource ID and formats the string based on the **args** parameter. This API returns the result synchronously.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8a/v3/Xe-mXeZ9Q1ON8vaWKXrFzw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062326Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=4F3467FCC8B48BA03C7B30C08F6EDCA9BCBAA1DE857A2DAA8F7A3DABC524580C)

-   Strings distinguish between singular and plural forms in all languages except Chinese. For details, see [Language Plural Rules](https://www.unicode.org/cldr/charts/45/supplemental/language_plural_rules.html).
    
-   In languages such as English and German, singular/plural numbers are classified into cardinal numbers (for example, 1, 2, 3) and ordinal numbers (for example, 1st, 2nd, 3rd). This API applies only to cardinal numbers.
    

**Atomic service API**: This API can be used in atomic services since API version 18.

**System capability**: SystemCapability.Global.ResourceManager

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| resId | number | Yes | Resource ID. |
| num | number | Yes | Integer number used to obtain the corresponding string representation based on the current language's [plural rules](https://www.unicode.org/cldr/charts/45/supplemental/language_plural_rules.html). |
| ...args | Array<string | number> | No | 
Arguments for formatting strings.

Supported value types include %d, %f, %s, %%, %number$d, %number$f, and %number$s.

Note: %% is converted to %. **number** in %number$d indicates the sequence number of the parameter in **args**.

For example, %%d is converted to %d after formatting, and %1$d indicates that the first parameter is used.

 |

**Return value**

| Type | Description |
| :-- | :-- |
| string | Formatted string corresponding to the specified resource ID. |

**Error codes**

For details about the error codes, see [Resource Manager Error Codes](../../error-codes/resource-manager-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 9001001 | Invalid resource ID. |
| 9001002 | No matching resource is found based on the resource ID. |
| 9001006 | The resource is referenced cyclically. |
| 9001007 | Failed to format the resource obtained based on the resource ID. |

**Example**

// Resource file path: src/main/resources/base/element/plural.json
{
  "plural": \[
    {
      "name": "format\_test",
      "value": \[
        {
          "quantity": "one",
          "value": "There is %d apple in the %s, the total amount is %f kg."
        },
        {
          "quantity": "other",
          "value": "There are %d apples in the %s, the total amount is %f kg."
        }
      \]
    }
  \]
}

import { AbilityConstant, UIAbility, Want } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

export default class EntryAbility extends UIAbility {
    onCreate(want: Want, launchParam: AbilityConstant.LaunchParam): void {
        try {
            // If num is 1, the single/plural type is one in the English environment.
            // The quantity field in the resource file indicates the single/plural type. Therefore, the string whose quantity is one is obtained.
            // Replace 'app.plural.format\_test' with the actual resource.
            let pluralStr = this.context.resourceManager.getIntPluralStringValueSync($r('app.plural.format\_test').id, 1, 1, "basket", 0.3);
            console.info(\`getIntPluralStringValueSync, result: ${pluralStr}\`);
            // Print the output result: getIntPluralStringValueSync, result: There is 1 apple in the basket, the total amount is 0.3 kg.
        } catch (error) {
            let code = (error as BusinessError).code;
            let message = (error as BusinessError).message;
            console.error(\`getIntPluralStringValueSync failed, error code: ${code}, message: ${message}.\`);
        }
    }
}

#### \[h2\]getIntPluralStringByNameSync18+

getIntPluralStringByNameSync(resName: string, num: number, ...args: Array<string | number>): string

Obtains a [singular/plural](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/l10n-singular-plural) string based on the specified resource name and formats the string based on the **args** parameter. This API returns the result synchronously.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/db/v3/bE8dGbliRRSe50w4o3yIqg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062326Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=551BF320ABD480548A9C7A0FC68DE1B4CF5C06F586B7FC86D9673EA13ABC41AD)

-   Strings distinguish between singular and plural forms in all languages except Chinese. For details, see [Language Plural Rules](https://www.unicode.org/cldr/charts/45/supplemental/language_plural_rules.html).
    
-   In languages such as English and German, singular/plural numbers are classified into cardinal numbers (for example, 1, 2, 3) and ordinal numbers (for example, 1st, 2nd, 3rd). This API applies only to cardinal numbers.
    

**Atomic service API**: This API can be used in atomic services since API version 18.

**System capability**: SystemCapability.Global.ResourceManager

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| resName | string | Yes | Resource name. |
| num | number | Yes | Integer number used to obtain the corresponding string representation based on the current language's [plural rules](https://www.unicode.org/cldr/charts/45/supplemental/language_plural_rules.html). |
| ...args | Array<string | number> | No | 
Arguments for formatting strings.

Supported value types include %d, %f, %s, %%, %number$d, %number$f, and %number$s.

Note: %% is converted to %. **number** in %number$d indicates the sequence number of the parameter in **args**.

For example, %%d is converted to %d after formatting, and %1$d indicates that the first parameter is used.

 |

**Return value**

| Type | Description |
| :-- | :-- |
| string | Formatted string corresponding to the specified resource name. |

**Error codes**

For details about the error codes, see [Resource Manager Error Codes](../../error-codes/resource-manager-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 9001003 | Invalid resource name. |
| 9001004 | No matching resource is found based on the resource name. |
| 9001006 | The resource is referenced cyclically. |
| 9001008 | Failed to format the resource obtained based on the resource name. |

**Example**

// Resource file path: src/main/resources/base/element/plural.json
{
  "plural": \[
    {
      "name": "format\_test",
      "value": \[
        {
          "quantity": "one",
          "value": "There is %d apple in the %s, the total amount is %f kg."
        },
        {
          "quantity": "other",
          "value": "There are %d apples in the %s, the total amount is %f kg."
        }
      \]
    }
  \]
}

import { AbilityConstant, UIAbility, Want } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

export default class EntryAbility extends UIAbility {
    onCreate(want: Want, launchParam: AbilityConstant.LaunchParam): void {
        try {
            // If num is 1, the single/plural type is one in the English environment.
            // The quantity field in the resource file indicates the single/plural type. Therefore, the string whose quantity is one is obtained.
            // Replace "format\_test" with the actual resource.
            let pluralStr = this.context.resourceManager.getIntPluralStringByNameSync("format\_test", 1, 1, "basket", 0.3);
            console.info(\`getIntPluralStringByNameSync, result: ${pluralStr}\`);
            // Print the output result: getIntPluralStringByNameSync, result: There is 1 apple in the basket, the total amount is 0.3 kg.
        } catch (error) {
            let code = (error as BusinessError).code;
            let message = (error as BusinessError).message;
            console.error(\`getIntPluralStringByNameSync failed, error code: ${code}, message: ${message}.\`);
        }
    }
}

#### \[h2\]getDoublePluralStringValueSync18+

getDoublePluralStringValueSync(resId: number, num: number, ...args: Array<string | number>): string

Obtains a [singular/plural](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/l10n-singular-plural) string based on the specified resource ID and formats the string based on the **args** parameter. This API returns the result synchronously.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4e/v3/ZFyqOl9NSxGXxwImRxxeUA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062326Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=89AD9D613136CD18F89D877FB079E9D477EC5778E44B46547114CE374A1E466B)

-   Strings distinguish between singular and plural forms in all languages except Chinese. For details, see [Language Plural Rules](https://www.unicode.org/cldr/charts/45/supplemental/language_plural_rules.html).
    
-   In languages such as English and German, singular/plural numbers are classified into cardinal numbers (for example, 1, 2, 3) and ordinal numbers (for example, 1st, 2nd, 3rd). This API applies only to cardinal numbers.
    

**Atomic service API**: This API can be used in atomic services since API version 18.

**System capability**: SystemCapability.Global.ResourceManager

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| resId | number | Yes | Resource ID. |
| num | number | Yes | Quantity value (a floating point number), used to obtain the corresponding string representation based on the current language's [plural rules](https://www.unicode.org/cldr/charts/45/supplemental/language_plural_rules.html). |
| ...args | Array<string | number> | No | 
Arguments for formatting strings.

Supported value types include %d, %f, %s, %%, %number$d, %number$f, and %number$s.

Note: %% is converted to %. **number** in %number$d indicates the sequence number of the parameter in **args**.

For example, %%d is converted to %d after formatting, and %1$d indicates that the first parameter is used.

 |

**Return value**

| Type | Description |
| :-- | :-- |
| string | Formatted string corresponding to the specified resource ID. |

**Error codes**

For details about the error codes, see [Resource Manager Error Codes](../../error-codes/resource-manager-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 9001001 | Invalid resource ID. |
| 9001002 | No matching resource is found based on the resource ID. |
| 9001006 | The resource is referenced cyclically. |
| 9001007 | Failed to format the resource obtained based on the resource ID. |

**Example**

// Resource file path: src/main/resources/base/element/plural.json
{
  "plural": \[
    {
      "name": "format\_test",
      "value": \[
        {
          "quantity": "one",
          "value": "There is %d apple in the %s, the total amount is %f kg."
        },
        {
          "quantity": "other",
          "value": "There are %d apples in the %s, the total amount is %f kg."
        }
      \]
    }
  \]
}

import { AbilityConstant, UIAbility, Want } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

export default class EntryAbility extends UIAbility {
    onCreate(want: Want, launchParam: AbilityConstant.LaunchParam): void {
        try {
            // If num is 2.1, the single/plural type is other in the English environment.
            // The quantity field in the resource file indicates the single/plural type. Therefore, the string whose quantity is other is obtained.
            // Replace 'app.plural.format\_test' with the actual resource.
            let pluralStr = this.context.resourceManager.getDoublePluralStringValueSync($r('app.plural.format\_test').id, 2.1, 2, "basket", 0.6);
            console.info(\`getDoublePluralStringValueSync, result: ${pluralStr}\`);
            // Print the output result: getDoublePluralStringValueSync, result: There are 2 apples in the basket, the total amount is 0.6 kg.
        } catch (error) {
            let code = (error as BusinessError).code;
            let message = (error as BusinessError).message;
            console.error(\`getDoublePluralStringValueSync failed, error code: ${code}, message: ${message}.\`);
        }
    }
}

#### \[h2\]getDoublePluralStringByNameSync18+

getDoublePluralStringByNameSync(resName: string, num: number, ...args: Array<string | number>): string

Obtains a [singular/plural](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/l10n-singular-plural) string based on the specified resource name and formats the string based on the **args** parameter. This API returns the result synchronously.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c6/v3/2kdWd3muQ2KfMHMepptFoQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062326Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=621908BE261C63807F2F8E93D607C022E90CE079E52ADB71F755A65F3E3B939C)

-   Strings distinguish between singular and plural forms in all languages except Chinese. For details, see [Language Plural Rules](https://www.unicode.org/cldr/charts/45/supplemental/language_plural_rules.html).
    
-   In languages such as English and German, singular/plural numbers are classified into cardinal numbers (for example, 1, 2, 3) and ordinal numbers (for example, 1st, 2nd, 3rd). This API applies only to cardinal numbers.
    

**Atomic service API**: This API can be used in atomic services since API version 18.

**System capability**: SystemCapability.Global.ResourceManager

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| resName | string | Yes | Resource name. |
| num | number | Yes | Quantity value (a floating point number), used to obtain the corresponding string representation based on the current language's [plural rules](https://www.unicode.org/cldr/charts/45/supplemental/language_plural_rules.html). |
| ...args | Array<string | number> | No | 
Arguments for formatting strings.

Supported value types include %d, %f, %s, %%, %number$d, %number$f, and %number$s.

Note: %% is converted to %. **number** in %number$d indicates the sequence number of the parameter in **args**.

For example, %%d is converted to %d after formatting, and %1$d indicates that the first parameter is used.

 |

**Return value**

| Type | Description |
| :-- | :-- |
| string | Formatted string corresponding to the specified resource name. |

**Error codes**

For details about the error codes, see [Resource Manager Error Codes](../../error-codes/resource-manager-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 9001003 | Invalid resource name. |
| 9001004 | No matching resource is found based on the resource name. |
| 9001006 | The resource is referenced cyclically. |
| 9001008 | Failed to format the resource obtained based on the resource name. |

**Example**

// Resource file path: src/main/resources/base/element/plural.json
{
  "plural": \[
    {
      "name": "format\_test",
      "value": \[
        {
          "quantity": "one",
          "value": "There is %d apple in the %s, the total amount is %f kg."
        },
        {
          "quantity": "other",
          "value": "There are %d apples in the %s, the total amount is %f kg."
        }
      \]
    }
  \]
}

import { AbilityConstant, UIAbility, Want } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

export default class EntryAbility extends UIAbility {
    onCreate(want: Want, launchParam: AbilityConstant.LaunchParam): void {
        try {
            // If num is 2.1, the single/plural type is other in the English environment.
            // The quantity field in the resource file indicates the single/plural type. Therefore, the string whose quantity is other is obtained.
            // Replace "format\_test" with the actual resource.
            let pluralStr = this.context.resourceManager.getDoublePluralStringByNameSync("format\_test", 2.1, 2, "basket", 0.6);
            console.info(\`getDoublePluralStringByNameSync, result: ${pluralStr}\`);
            // Print the output result: getDoublePluralStringByNameSync, result: There are 2 apples in the basket, the total amount is 0.6 kg.
        } catch (error) {
            let code = (error as BusinessError).code;
            let message = (error as BusinessError).message;
            console.error(\`getDoublePluralStringByNameSync failed, error code: ${code}, message: ${message}.\`);
        }
    }
}

#### \[h2\]getMediaContentSync10+

getMediaContentSync(resId: number, density?: number): Uint8Array

Obtains the media file content for the default or specified screen density based on the specified resource ID. This API returns the result synchronously.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Global.ResourceManager

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| resId | number | Yes | Resource ID. |
| [density](#screendensity) | number | No | Screen density. The default value or value **0** indicates the default screen density. |

**Return value**

| Type | Description |
| :-- | :-- |
| Uint8Array | Content of the media file corresponding to the specified resource ID. |

**Error codes**

For details about the error codes, see [Resource Manager Error Codes](../../error-codes/resource-manager-error-codes/document.md) and [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | If the input parameter invalid. Possible causes: 1.Incorrect parameter types; 2.Parameter verification failed. |
| 9001001 | Invalid resource ID. |
| 9001002 | No matching resource is found based on the resource ID. |

**Example**

import { AbilityConstant, UIAbility, Want } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

export default class EntryAbility extends UIAbility {
    onCreate(want: Want, launchParam: AbilityConstant.LaunchParam): void {
        try {
            // Replace 'app.media.test' with the actual resource.
            this.context.resourceManager.getMediaContentSync($r('app.media.test').id); // Default screen density
        } catch (error) {
            let code = (error as BusinessError).code;
            let message = (error as BusinessError).message;
            console.error(\`getMediaContentSync failed, error code: ${code}, message: ${message}.\`);
        }

        try {
            // Replace 'app.media.test' with the actual resource.
            this.context.resourceManager.getMediaContentSync($r('app.media.test').id, 120); // Specified screen density
        } catch (error) {
            let code = (error as BusinessError).code;
            let message = (error as BusinessError).message;
            console.error(\`getMediaContentSync failed, error code: ${code}, message: ${message}.\`);
        }
    }
}

#### \[h2\]getMediaByNameSync10+

getMediaByNameSync(resName: string, density?: number): Uint8Array

Obtains the media file content for the default or specified screen density based on the specified resource name. This API returns the result synchronously.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Global.ResourceManager

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| resName | string | Yes | Resource name. |
| [density](#screendensity) | number | No | Screen density. The default value or value **0** indicates the default screen density. |

**Return value**

| Type | Description |
| :-- | :-- |
| Uint8Array | Promise used to return the result, which is the content of the media file corresponding to the specified resource name. |

**Error codes**

For details about the error codes, see [Resource Manager Error Codes](../../error-codes/resource-manager-error-codes/document.md) and [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | If the input parameter invalid. Possible causes: 1.Incorrect parameter types; 2.Parameter verification failed. |
| 9001003 | Invalid resource name. |
| 9001004 | No matching resource is found based on the resource name. |

**Example**

import { AbilityConstant, UIAbility, Want } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

export default class EntryAbility extends UIAbility {
    onCreate(want: Want, launchParam: AbilityConstant.LaunchParam): void {
        try {
            // Replace "test" with the actual resource.
            this.context.resourceManager.getMediaByNameSync("test"); // Default screen density
        } catch (error) {
            let code = (error as BusinessError).code;
            let message = (error as BusinessError).message;
            console.error(\`getMediaByNameSync failed, error code: ${code}, message: ${message}.\`);
        }

        try {
            // Replace "test" with the actual resource.
            this.context.resourceManager.getMediaByNameSync("test", 120); // Specified screen density
        } catch (error) {
            let code = (error as BusinessError).code;
            let message = (error as BusinessError).message;
            console.error(\`getMediaByNameSync failed, error code: ${code}, message: ${message}.\`);
        }
    }
}

#### \[h2\]getMediaContent9+

getMediaContent(resId: number, callback: \_AsyncCallback<Uint8Array>): void

Obtains media file content based on the specified resource ID. This API uses an asynchronous callback to return the result.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Global.ResourceManager

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| resId | number | Yes | Resource ID. |
| callback | [\_AsyncCallback](../../../../system/basic-functions/basic-services-kit/arkts-apis/others/ohos-base-public-callback-information/document.md#asynccallback)<Uint8Array> | Yes | Callback used to return the media file content. |

**Error codes**

For details about the error codes, see [Resource Manager Error Codes](../../error-codes/resource-manager-error-codes/document.md) and [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | If the input parameter invalid. Possible causes: Incorrect parameter types. |
| 9001001 | Invalid resource ID. |
| 9001002 | No matching resource is found based on the resource ID. |

**Example**

import { AbilityConstant, UIAbility, Want } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

export default class EntryAbility extends UIAbility {
    onCreate(want: Want, launchParam: AbilityConstant.LaunchParam): void {
        try {
            // Replace 'app.media.test' with the actual resource.
            this.context.resourceManager.getMediaContent($r('app.media.test').id,
                (error: BusinessError, value: Uint8Array) => {
                    if (error != null) {
                        console.error("error is " + error);
                    } else {
                        let media = value;
                    }
                });
        } catch (error) {
            let code = (error as BusinessError).code;
            let message = (error as BusinessError).message;
            console.error(\`callback getMediaContent failed, error code: ${code}, message: ${message}.\`);
        }
    }
}

#### \[h2\]getMediaContent10+

getMediaContent(resId: number, density: number, callback: \_AsyncCallback<Uint8Array>): void

Obtains the media file content for the specified screen density based on the specified resource ID. This API uses an asynchronous callback to return the result.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Global.ResourceManager

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| resId | number | Yes | Resource ID. |
| [density](#screendensity) | number | Yes | Screen density. The value **0** indicates the default screen density. |
| callback | [\_AsyncCallback](../../../../system/basic-functions/basic-services-kit/arkts-apis/others/ohos-base-public-callback-information/document.md#asynccallback)<Uint8Array> | Yes | Callback used to return the media file content. |

**Error codes**

For details about the error codes, see [Resource Manager Error Codes](../../error-codes/resource-manager-error-codes/document.md) and [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | If the input parameter invalid. Possible causes: 1.Incorrect parameter types; 2.Parameter verification failed. |
| 9001001 | Invalid resource ID. |
| 9001002 | No matching resource is found based on the resource ID. |

**Example**

import { AbilityConstant, UIAbility, Want } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

export default class EntryAbility extends UIAbility {
    onCreate(want: Want, launchParam: AbilityConstant.LaunchParam): void {
        try {
            // Replace 'app.media.test' with the actual resource.
            this.context.resourceManager.getMediaContent($r('app.media.test').id, 120, (error: BusinessError, value: Uint8Array) => {
                if (error != null) {
                    console.error(\`callback getMediaContent failed, error code: ${error.code}, message: ${error.message}.\`);
                } else {
                    let media = value;
                }
            });
        } catch (error) {
            let code = (error as BusinessError).code;
            let message = (error as BusinessError).message;
            console.error(\`callback getMediaContent failed, error code: ${code}, message: ${message}.\`);
        }
    }
}

#### \[h2\]getMediaContent9+

getMediaContent(resId: number): Promise<Uint8Array>

Obtains media file content based on the specified resource ID. This API uses a promise to return the result.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Global.ResourceManager

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| resId | number | Yes | Resource ID. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<Uint8Array> | Promise used to return the media file content. |

**Error codes**

For details about the error codes, see [Resource Manager Error Codes](../../error-codes/resource-manager-error-codes/document.md) and [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | If the input parameter invalid. Possible causes: Incorrect parameter types. |
| 9001001 | Invalid resource ID. |
| 9001002 | No matching resource is found based on the resource ID. |

**Example**

import { AbilityConstant, UIAbility, Want } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

export default class EntryAbility extends UIAbility {
    onCreate(want: Want, launchParam: AbilityConstant.LaunchParam): void {
        try {
            // Replace 'app.media.test' with the actual resource.
            this.context.resourceManager.getMediaContent($r('app.media.test').id).then((value: Uint8Array) => {
                let media = value;
            }).catch((error: BusinessError) => {
                console.error("getMediaContent promise error is " + error);
            });
        } catch (error) {
            let code = (error as BusinessError).code;
            let message = (error as BusinessError).message;
            console.error(\`promise getMediaContent failed, error code: ${code}, message: ${message}.\`);
        }
    }
}

#### \[h2\]getMediaContent10+

getMediaContent(resId: number, density: number): Promise<Uint8Array>

Obtains the media file content for the specified screen density based on the specified resource ID. This API uses a promise to return the result.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Global.ResourceManager

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| resId | number | Yes | Resource ID. |
| [density](#screendensity) | number | Yes | Screen density. The value **0** indicates the default screen density. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<Uint8Array> | Promise used to return the media file content. |

**Error codes**

For details about the error codes, see [Resource Manager Error Codes](../../error-codes/resource-manager-error-codes/document.md) and [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | If the input parameter invalid. Possible causes: 1.Incorrect parameter types; 2.Parameter verification failed. |
| 9001001 | Invalid resource ID. |
| 9001002 | No matching resource is found based on the resource ID. |

**Example**

import { AbilityConstant, UIAbility, Want } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

export default class EntryAbility extends UIAbility {
    onCreate(want: Want, launchParam: AbilityConstant.LaunchParam): void {
        try {
            // Replace 'app.media.test' with the actual resource.
            this.context.resourceManager.getMediaContent($r('app.media.test').id, 120).then((value: Uint8Array) => {
                let media = value;
            }).catch((error: BusinessError) => {
                console.error(\`promise getMediaContent failed, error code: ${error.code}, message: ${error.message}.\`);
            });
        } catch (error) {
            let code = (error as BusinessError).code;
            let message = (error as BusinessError).message;
            console.error(\`promise getMediaContent failed, error code: ${code}, message: ${message}.\`);
        }
    }
}

#### \[h2\]getMediaByName9+

getMediaByName(resName: string, callback: \_AsyncCallback<Uint8Array>): void

Obtains media file content based on the specified resource name. This API uses an asynchronous callback to return the result.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Global.ResourceManager

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| resName | string | Yes | Resource name. |
| callback | [\_AsyncCallback](../../../../system/basic-functions/basic-services-kit/arkts-apis/others/ohos-base-public-callback-information/document.md#asynccallback)<Uint8Array> | Yes | Callback used to return the media file content. |

**Error codes**

For details about the error codes, see [Resource Manager Error Codes](../../error-codes/resource-manager-error-codes/document.md) and [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | If the input parameter invalid. Possible causes: Incorrect parameter types. |
| 9001003 | Invalid resource name. |
| 9001004 | No matching resource is found based on the resource name. |

**Example**

import { AbilityConstant, UIAbility, Want } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

export default class EntryAbility extends UIAbility {
    onCreate(want: Want, launchParam: AbilityConstant.LaunchParam): void {
        try {
            // Replace "test" with the actual resource.
            this.context.resourceManager.getMediaByName("test", (error: BusinessError, value: Uint8Array) => {
                if (error != null) {
                    console.error("error is " + error);
                } else {
                    let media = value;
                }
            });
        } catch (error) {
            let code = (error as BusinessError).code;
            let message = (error as BusinessError).message;
            console.error(\`callback getMediaByName failed, error code: ${code}, message: ${message}.\`);
        }
    }
}

#### \[h2\]getMediaByName10+

getMediaByName(resName: string, density: number, callback: \_AsyncCallback<Uint8Array>): void

Obtains the media file content for the specified screen density based on the specified resource name. This API uses an asynchronous callback to return the result.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Global.ResourceManager

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| resName | string | Yes | Resource name. |
| [density](#screendensity) | number | Yes | Screen density. The value **0** indicates the default screen density. |
| callback | [\_AsyncCallback](../../../../system/basic-functions/basic-services-kit/arkts-apis/others/ohos-base-public-callback-information/document.md#asynccallback)<Uint8Array> | Yes | Callback used to return the media file content. |

**Error codes**

For details about the error codes, see [Resource Manager Error Codes](../../error-codes/resource-manager-error-codes/document.md) and [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | If the input parameter invalid. Possible causes: 1.Incorrect parameter types; 2.Parameter verification failed. |
| 9001003 | Invalid resource name. |
| 9001004 | No matching resource is found based on the resource name. |

**Example**

import { AbilityConstant, UIAbility, Want } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

export default class EntryAbility extends UIAbility {
    onCreate(want: Want, launchParam: AbilityConstant.LaunchParam): void {
        try {
            // Replace "test" with the actual resource.
            this.context.resourceManager.getMediaByName("test", 120, (error: BusinessError, value: Uint8Array) => {
                if (error != null) {
                    console.error(\`callback getMediaByName failed, error code: ${error.code}, message: ${error.message}.\`);
                } else {
                    let media = value;
                }
            });
        } catch (error) {
            let code = (error as BusinessError).code;
            let message = (error as BusinessError).message;
            console.error(\`callback getMediaByName failed, error code: ${code}, message: ${message}.\`);
        }
    }
}

#### \[h2\]getMediaByName9+

getMediaByName(resName: string): Promise<Uint8Array>

Obtains media file content based on the specified resource name. This API uses a promise to return the result.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Global.ResourceManager

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| resName | string | Yes | Resource name. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<Uint8Array> | Promise used to return the media file content. |

**Error codes**

For details about the error codes, see [Resource Manager Error Codes](../../error-codes/resource-manager-error-codes/document.md) and [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | If the input parameter invalid. Possible causes: Incorrect parameter types. |
| 9001003 | Invalid resource name. |
| 9001004 | No matching resource is found based on the resource name. |

**Example**

import { AbilityConstant, UIAbility, Want } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

export default class EntryAbility extends UIAbility {
    onCreate(want: Want, launchParam: AbilityConstant.LaunchParam): void {
        try {
            // Replace "test" with the actual resource.
            this.context.resourceManager.getMediaByName("test").then((value: Uint8Array) => {
                let media = value;
            }).catch((error: BusinessError) => {
                console.error("getMediaByName promise error is " + error);
            });
        } catch (error) {
            let code = (error as BusinessError).code;
            let message = (error as BusinessError).message;
            console.error(\`promise getMediaByName failed, error code: ${code}, message: ${message}.\`);
        }
    }
}

#### \[h2\]getMediaByName10+

getMediaByName(resName: string, density: number): Promise<Uint8Array>

Obtains the media file content for the specified screen density based on the specified resource name. This API uses a promise to return the result.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Global.ResourceManager

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| resName | string | Yes | Resource name. |
| [density](#screendensity) | number | Yes | Screen density. The value **0** indicates the default screen density. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<Uint8Array> | Promise used to return the media file content. |

**Error codes**

For details about the error codes, see [Resource Manager Error Codes](../../error-codes/resource-manager-error-codes/document.md) and [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | If the input parameter invalid. Possible causes: 1.Incorrect parameter types; 2.Parameter verification failed. |
| 9001003 | Invalid resource name. |
| 9001004 | No matching resource is found based on the resource name. |

**Example**

import { AbilityConstant, UIAbility, Want } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

export default class EntryAbility extends UIAbility {
    onCreate(want: Want, launchParam: AbilityConstant.LaunchParam): void {
        try {
            // Replace "test" with the actual resource.
            this.context.resourceManager.getMediaByName("test", 120).then((value: Uint8Array) => {
                let media = value;
            }).catch((error: BusinessError) => {
                console.error(\`promise getMediaByName failed, error code: ${error.code}, message: ${error.message}.\`);
            });
        } catch (error) {
            let code = (error as BusinessError).code;
            let message = (error as BusinessError).message;
            console.error(\`promise getMediaByName failed, error code: ${code}, message: ${message}.\`);
        }
    }
}

#### \[h2\]getMediaContentBase64Sync10+

getMediaContentBase64Sync(resId: number, density?: number): string

Obtains an image's Base64 code for the default or specified screen density based on the specified resource ID. This API returns the result synchronously.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Global.ResourceManager

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| resId | number | Yes | Resource ID. |
| [density](#screendensity) | number | No | Screen density. The default value or value **0** indicates the default screen density. |

**Return value**

| Type | Description |
| :-- | :-- |
| string | Base64 code of the image corresponding to the specified resource ID. |

**Error codes**

For details about the error codes, see [Resource Manager Error Codes](../../error-codes/resource-manager-error-codes/document.md) and [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | If the input parameter invalid. Possible causes: 1.Incorrect parameter types; 2.Parameter verification failed. |
| 9001001 | Invalid resource ID. |
| 9001002 | No matching resource is found based on the resource ID. |

**Example**

import { AbilityConstant, UIAbility, Want } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

export default class EntryAbility extends UIAbility {
    onCreate(want: Want, launchParam: AbilityConstant.LaunchParam): void {
        try {
            // Replace 'app.media.test' with the actual resource.
            this.context.resourceManager.getMediaContentBase64Sync($r('app.media.test').id); // Default screen density
        } catch (error) {
            let code = (error as BusinessError).code;
            let message = (error as BusinessError).message;
            console.error(\`getMediaContentBase64Sync failed, error code: ${code}, message: ${message}.\`);
        }

        try {
            // Replace 'app.media.test' with the actual resource.
            this.context.resourceManager.getMediaContentBase64Sync($r('app.media.test').id, 120); // Specified screen density
        } catch (error) {
            let code = (error as BusinessError).code;
            let message = (error as BusinessError).message;
            console.error(\`getMediaContentBase64Sync failed, error code: ${code}, message: ${message}.\`);
        }
    }
}

#### \[h2\]getMediaBase64ByNameSync10+

getMediaBase64ByNameSync(resName: string, density?: number): string

Obtains an image's Base64 code for the default or specified screen density based on the specified resource name. This API returns the result synchronously.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Global.ResourceManager

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| resName | string | Yes | Resource name. |
| [density](#screendensity) | number | No | Screen density. The default value or value **0** indicates the default screen density. |

**Return value**

| Type | Description |
| :-- | :-- |
| string | Base64 code of the image corresponding to the specified resource name. |

**Error codes**

For details about the error codes, see [Resource Manager Error Codes](../../error-codes/resource-manager-error-codes/document.md) and [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | If the input parameter invalid. Possible causes: 1.Incorrect parameter types; 2.Parameter verification failed. |
| 9001003 | Invalid resource name. |
| 9001004 | No matching resource is found based on the resource name. |

**Example**

import { AbilityConstant, UIAbility, Want } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

export default class EntryAbility extends UIAbility {
    onCreate(want: Want, launchParam: AbilityConstant.LaunchParam): void {
        try {
            // Replace "test" with the actual resource.
            this.context.resourceManager.getMediaBase64ByNameSync("test"); // Default screen density
        } catch (error) {
            let code = (error as BusinessError).code;
            let message = (error as BusinessError).message;
            console.error(\`getMediaBase64ByNameSync failed, error code: ${code}, message: ${message}.\`);
        }

        try {
            // Replace "test" with the actual resource.
            this.context.resourceManager.getMediaBase64ByNameSync("test", 120); // Specified screen density
        } catch (error) {
            let code = (error as BusinessError).code;
            let message = (error as BusinessError).message;
            console.error(\`getMediaBase64ByNameSync failed, error code: ${code}, message: ${message}.\`);
        }
    }
}

#### \[h2\]getMediaContentBase649+

getMediaContentBase64(resId: number, callback: \_AsyncCallback<string>): void

Obtains an image's Base64 code based on the specified resource ID. This API uses an asynchronous callback to return the result.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Global.ResourceManager

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| resId | number | Yes | Resource ID. |
| callback | [\_AsyncCallback](../../../../system/basic-functions/basic-services-kit/arkts-apis/others/ohos-base-public-callback-information/document.md#asynccallback)<string> | Yes | Callback used to return the Base64 code of the image. |

**Error codes**

For details about the error codes, see [Resource Manager Error Codes](../../error-codes/resource-manager-error-codes/document.md) and [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | If the input parameter invalid. Possible causes: Incorrect parameter types. |
| 9001001 | Invalid resource ID. |
| 9001002 | No matching resource is found based on the resource ID. |

**Example**

import { AbilityConstant, UIAbility, Want } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

export default class EntryAbility extends UIAbility {
    onCreate(want: Want, launchParam: AbilityConstant.LaunchParam): void {
        try {
            // Replace 'app.media.test' with the actual resource.
            this.context.resourceManager.getMediaContentBase64($r('app.media.test').id, (error: BusinessError, value: string) => {
                if (error != null) {
                    console.error("error is " + error);
                } else {
                    let media = value;
                }
            });
        } catch (error) {
            let code = (error as BusinessError).code;
            let message = (error as BusinessError).message;
            console.error(\`callback getMediaContentBase64 failed, error code: ${code}, message: ${message}.\`);
        }
    }
}

#### \[h2\]getMediaContentBase6410+

getMediaContentBase64(resId: number, density: number, callback: \_AsyncCallback<string>): void

Obtains an image's Base64 code for the specified screen density based on the specified resource ID. This API uses an asynchronous callback to return the result.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Global.ResourceManager

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| resId | number | Yes | Resource ID. |
| [density](#screendensity) | number | Yes | Screen density. The value **0** indicates the default screen density. |
| callback | [\_AsyncCallback](../../../../system/basic-functions/basic-services-kit/arkts-apis/others/ohos-base-public-callback-information/document.md#asynccallback)<string> | Yes | Callback used to return the Base64 code of the image. |

**Error codes**

For details about the error codes, see [Resource Manager Error Codes](../../error-codes/resource-manager-error-codes/document.md) and [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | If the input parameter invalid. Possible causes: 1.Incorrect parameter types; 2.Parameter verification failed. |
| 9001001 | Invalid resource ID. |
| 9001002 | No matching resource is found based on the resource ID. |

**Example**

import { AbilityConstant, UIAbility, Want } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

export default class EntryAbility extends UIAbility {
    onCreate(want: Want, launchParam: AbilityConstant.LaunchParam): void {
        try {
            // Replace 'app.media.test' with the actual resource.
            this.context.resourceManager.getMediaContentBase64($r('app.media.test').id, 120, (error: BusinessError, value: string) => {
                if (error != null) {
                    console.error(\`callback getMediaContentBase64 failed, error code: ${error.code}, message: ${error.message}.\`);
                } else {
                    let media = value;
                }
            });
        } catch (error) {
            let code = (error as BusinessError).code;
            let message = (error as BusinessError).message;
            console.error(\`callback getMediaContentBase64 failed, error code: ${code}, message: ${message}.\`);
        }
    }
}

#### \[h2\]getMediaContentBase649+

getMediaContentBase64(resId: number): Promise<string>

Obtains an image's Base64 code based on the specified resource ID. This API uses a promise to return the result.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Global.ResourceManager

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| resId | number | Yes | Resource ID. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<string> | Promise used to return the Base64 code of the image. |

**Error codes**

For details about the error codes, see [Resource Manager Error Codes](../../error-codes/resource-manager-error-codes/document.md) and [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | If the input parameter invalid. Possible causes: Incorrect parameter types. |
| 9001001 | Invalid resource ID. |
| 9001002 | No matching resource is found based on the resource ID. |

**Example**

import { AbilityConstant, UIAbility, Want } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

export default class EntryAbility extends UIAbility {
    onCreate(want: Want, launchParam: AbilityConstant.LaunchParam): void {
        try {
            // Replace 'app.media.test' with the actual resource.
            this.context.resourceManager.getMediaContentBase64($r('app.media.test').id).then((value: string) => {
                let media = value;
            }).catch((error: BusinessError) => {
                console.error("getMediaContentBase64 promise error is " + error);
            });
        } catch (error) {
            let code = (error as BusinessError).code;
            let message = (error as BusinessError).message;
            console.error(\`promise getMediaContentBase64 failed, error code: ${code}, message: ${message}.\`);
        }
    }
}

#### \[h2\]getMediaContentBase6410+

getMediaContentBase64(resId: number, density: number): Promise<string>

Obtains an image's Base64 code for the specified screen density based on the specified resource ID. This API uses a promise to return the result.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Global.ResourceManager

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| resId | number | Yes | Resource ID. |
| [density](#screendensity) | number | Yes | Screen density. The value **0** indicates the default screen density. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<string> | Promise used to return the Base64 code of the image. |

**Error codes**

For details about the error codes, see [Resource Manager Error Codes](../../error-codes/resource-manager-error-codes/document.md) and [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | If the input parameter invalid. Possible causes: 1.Incorrect parameter types; 2.Parameter verification failed. |
| 9001001 | Invalid resource ID. |
| 9001002 | No matching resource is found based on the resource ID. |

**Example**

import { AbilityConstant, UIAbility, Want } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

export default class EntryAbility extends UIAbility {
    onCreate(want: Want, launchParam: AbilityConstant.LaunchParam): void {
        try {
            // Replace 'app.media.test' with the actual resource.
            this.context.resourceManager.getMediaContentBase64($r('app.media.test').id, 120).then((value: string) => {
                let media = value;
            }).catch((error: BusinessError) => {
                console.error(\`promise getMediaContentBase64 failed, error code: ${error.code}, message: ${error.message}.\`);
            });
        } catch (error) {
            let code = (error as BusinessError).code;
            let message = (error as BusinessError).message;
            console.error(\`promise getMediaContentBase64 failed, error code: ${code}, message: ${message}.\`);
        }
    }
}

#### \[h2\]getMediaBase64ByName9+

getMediaBase64ByName(resName: string, callback: \_AsyncCallback<string>): void

Obtains an image's Base64 code based on the specified resource name. This API uses an asynchronous callback to return the result.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Global.ResourceManager

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| resName | string | Yes | Resource name. |
| callback | [\_AsyncCallback](../../../../system/basic-functions/basic-services-kit/arkts-apis/others/ohos-base-public-callback-information/document.md#asynccallback)<string> | Yes | Callback used to return the Base64 code of the image. |

**Error codes**

For details about the error codes, see [Resource Manager Error Codes](../../error-codes/resource-manager-error-codes/document.md) and [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | If the input parameter invalid. Possible causes: Incorrect parameter types. |
| 9001003 | Invalid resource name. |
| 9001004 | No matching resource is found based on the resource name. |

**Example**

import { AbilityConstant, UIAbility, Want } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

export default class EntryAbility extends UIAbility {
    onCreate(want: Want, launchParam: AbilityConstant.LaunchParam): void {
        try {
            // Replace "test" with the actual resource.
            this.context.resourceManager.getMediaBase64ByName("test", (error: BusinessError, value: string) => {
                if (error != null) {
                    console.error("error is " + error);
                } else {
                    let media = value;
                }
            });
        } catch (error) {
            let code = (error as BusinessError).code;
            let message = (error as BusinessError).message;
            console.error(\`callback getMediaBase64ByName failed, error code: ${code}, message: ${message}.\`);
        }
    }
}

#### \[h2\]getMediaBase64ByName10+

getMediaBase64ByName(resName: string, density: number, callback: \_AsyncCallback<string>): void

Obtains an image's Base64 code for the specified screen density based on the specified resource name. This API uses an asynchronous callback to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/59/v3/xDcS1u-cRAePttwm-r6qTg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062326Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=71D2C4B17F52B78F0907EA5E15F544A2FF888CC3734C68A695958BE5B8625DFF)

You are advised to use [getMediaBase64ByName](#getmediacontentbase6410) or [getMediaContentBase64](#getmediacontentbase6410). For details, see [ResourceManager](#resourcemanager).

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Global.ResourceManager

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| resName | string | Yes | Resource name. |
| [density](#screendensity) | number | Yes | Screen density. The value **0** indicates the default screen density. |
| callback | [\_AsyncCallback](../../../../system/basic-functions/basic-services-kit/arkts-apis/others/ohos-base-public-callback-information/document.md#asynccallback)<string> | Yes | Callback used to return the Base64 code of the image. |

**Error codes**

For details about the error codes, see [Resource Manager Error Codes](../../error-codes/resource-manager-error-codes/document.md) and [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | If the input parameter invalid. Possible causes: 1.Incorrect parameter types; 2.Parameter verification failed. |
| 9001003 | Invalid resource name. |
| 9001004 | No matching resource is found based on the resource name. |

**Example**

import { AbilityConstant, UIAbility, Want } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

export default class EntryAbility extends UIAbility {
    onCreate(want: Want, launchParam: AbilityConstant.LaunchParam): void {
        try {
            // Replace "test" with the actual resource.
            this.context.resourceManager.getMediaBase64ByName("test", 120, (error: BusinessError, value: string) => {
                if (error != null) {
                    console.error(\`callback getMediaBase64ByName failed, error code: ${error.code}, message: ${error.message}.\`);
                } else {
                    let media = value;
                }
            });
        } catch (error) {
            let code = (error as BusinessError).code;
            let message = (error as BusinessError).message;
            console.error(\`callback getMediaBase64ByName failed, error code: ${code}, message: ${message}.\`);
        }
    }
}

#### \[h2\]getMediaBase64ByName9+

getMediaBase64ByName(resName: string): Promise<string>

Obtains an image's Base64 code based on the specified resource name. This API uses a promise to return the result.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Global.ResourceManager

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| resName | string | Yes | Resource name. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<string> | Promise used to return the Base64 code of the image. |

**Error codes**

For details about the error codes, see [Resource Manager Error Codes](../../error-codes/resource-manager-error-codes/document.md) and [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | If the input parameter invalid. Possible causes: Incorrect parameter types. |
| 9001003 | Invalid resource name. |
| 9001004 | No matching resource is found based on the resource name. |

**Example**

import { AbilityConstant, UIAbility, Want } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

export default class EntryAbility extends UIAbility {
    onCreate(want: Want, launchParam: AbilityConstant.LaunchParam): void {
        try {
            // Replace "test" with the actual resource.
            this.context.resourceManager.getMediaBase64ByName("test").then((value: string) => {
                let media = value;
            }).catch((error: BusinessError) => {
                console.error("getMediaBase64ByName promise error is " + error);
            });
        } catch (error) {
            let code = (error as BusinessError).code;
            let message = (error as BusinessError).message;
            console.error(\`promise getMediaBase64ByName failed, error code: ${code}, message: ${message}.\`);
        }
    }
}

#### \[h2\]getMediaBase64ByName10+

getMediaBase64ByName(resName: string, density: number): Promise<string>

Obtains an image's Base64 code for the specified screen density based on the specified resource name. This API uses a promise to return the result.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Global.ResourceManager

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| resName | string | Yes | Resource name. |
| [density](#screendensity) | number | Yes | Screen density. The value **0** indicates the default screen density. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<string> | Promise used to return the Base64 code of the image. |

**Error codes**

For details about the error codes, see [Resource Manager Error Codes](../../error-codes/resource-manager-error-codes/document.md) and [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | If the input parameter invalid. Possible causes: 1.Incorrect parameter types; 2.Parameter verification failed. |
| 9001003 | Invalid resource name. |
| 9001004 | No matching resource is found based on the resource name. |

**Example**

import { AbilityConstant, UIAbility, Want } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

export default class EntryAbility extends UIAbility {
    onCreate(want: Want, launchParam: AbilityConstant.LaunchParam): void {
        try {
            // Replace "test" with the actual resource.
            this.context.resourceManager.getMediaBase64ByName("test", 120).then((value: string) => {
                let media = value;
            }).catch((error: BusinessError) => {
                console.error(\`promise getMediaBase64ByName failed, error code: ${error.code}, message: ${error.message}.\`);
            });
        } catch (error) {
            let code = (error as BusinessError).code;
            let message = (error as BusinessError).message;
            console.error(\`promise getMediaBase64ByName failed, error code: ${code}, message: ${message}.\`);
        }
    }
}

#### \[h2\]getDrawableDescriptor10+

getDrawableDescriptor(resId: number, density?: number, type?: number): DrawableDescriptor

Obtains a **DrawableDescriptor** object for icon display based on the specified resource ID. This API returns the result synchronously.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Global.ResourceManager

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| resId | number | Yes | Resource ID. |
| [density](#screendensity) | number | No | Screen density. The default value or value **0** indicates the default screen density. |
| type11+ | number | No | 
\- **1**: Layered icon resource of the application in the theme resource package.

\- **0** or default value: Icon resource of the application.

 |

**Return value**

| Type | Description |
| :-- | :-- |
| [DrawableDescriptor](../../../arkui/arkts-api/ui/ohos-arkui-drawabledescriptor-drawabledescriptor/document.md#drawabledescriptor) | **DrawableDescriptor** object corresponding to the specified resource ID. |

**Error codes**

For details about the error codes, see [Resource Manager Error Codes](../../error-codes/resource-manager-error-codes/document.md) and [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | If the input parameter invalid. Possible causes: 1.Incorrect parameter types; 2.Parameter verification failed. |
| 9001001 | Invalid resource ID. |
| 9001002 | No matching resource is found based on the resource ID. |

**Example**

import { AbilityConstant, UIAbility, Want } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { DrawableDescriptor } from '@kit.ArkUI';

export default class EntryAbility extends UIAbility {
    onCreate(want: Want, launchParam: AbilityConstant.LaunchParam): void {
        try {
            // Replace 'app.media.icon' with the actual resource.
            let drawableDescriptor:DrawableDescriptor = this.context.resourceManager.getDrawableDescriptor($r('app.media.icon').id);
        } catch (error) {
            let code = (error as BusinessError).code;
            let message = (error as BusinessError).message;
            console.error(\`getDrawableDescriptor failed, error code: ${code}, message: ${message}.\`);
        }
        try {
            // Replace 'app.media.icon' with the actual resource.
            let drawableDescriptor:DrawableDescriptor = this.context.resourceManager.getDrawableDescriptor($r('app.media.icon').id, 120);
        } catch (error) {
            let code = (error as BusinessError).code;
            let message = (error as BusinessError).message;
            console.error(\`getDrawableDescriptor failed, error code: ${code}, message: ${message}.\`);
        }
        try {
            // Replace 'app.media.icon' with the actual resource.
            let drawableDescriptor:DrawableDescriptor = this.context.resourceManager.getDrawableDescriptor($r('app.media.icon').id, 0, 1);
        } catch (error) {
            let code = (error as BusinessError).code;
            let message = (error as BusinessError).message;
            console.error(\`getDrawableDescriptor failed, error code: ${code}, message: ${message}.\`);
        }
    }
}

#### \[h2\]getDrawableDescriptorByName10+

getDrawableDescriptorByName(resName: string, density?: number, type?: number): DrawableDescriptor

Obtains a **DrawableDescriptor** object for icon display based on the specified resource name. This API returns the result synchronously.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Global.ResourceManager

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| resName | string | Yes | Resource name. |
| [density](#screendensity) | number | No | Screen density. The default value or value **0** indicates the default screen density. |
| type11+ | number | No | 
\- **1**: Layered icon resource of the application in the theme resource package.

\- **0** or default value: Icon resource of the application.

 |

**Return value**

| Type | Description |
| :-- | :-- |
| [DrawableDescriptor](../../../arkui/arkts-api/ui/ohos-arkui-drawabledescriptor-drawabledescriptor/document.md#drawabledescriptor) | **DrawableDescriptor** object. |

**Error codes**

For details about the error codes, see [Resource Manager Error Codes](../../error-codes/resource-manager-error-codes/document.md) and [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | If the input parameter invalid. Possible causes: 1.Incorrect parameter types; 2.Parameter verification failed. |
| 9001003 | Invalid resource name. |
| 9001004 | No matching resource is found based on the resource name. |

**Example**

import { AbilityConstant, UIAbility, Want } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { DrawableDescriptor } from '@kit.ArkUI';

export default class EntryAbility extends UIAbility {
    onCreate(want: Want, launchParam: AbilityConstant.LaunchParam): void {
        try {
            // Replace "icon" with the actual resource.
            let drawableDescriptor:DrawableDescriptor = this.context.resourceManager.getDrawableDescriptorByName('icon');
        } catch (error) {
            let code = (error as BusinessError).code;
            let message = (error as BusinessError).message;
            console.error(\`getDrawableDescriptorByName failed, error code: ${code}, message: ${message}.\`);
        }
        try {
            // Replace "icon" with the actual resource.
            let drawableDescriptor:DrawableDescriptor = this.context.resourceManager.getDrawableDescriptorByName('icon', 120);
        } catch (error) {
            let code = (error as BusinessError).code;
            let message = (error as BusinessError).message;
            console.error(\`getDrawableDescriptorByName failed, error code: ${code}, message: ${message}.\`);
        }
        try {
            // Replace "icon" with the actual resource.
            let drawableDescriptor:DrawableDescriptor = this.context.resourceManager.getDrawableDescriptorByName('icon', 0, 1);
        } catch (error) {
            let code = (error as BusinessError).code;
            let message = (error as BusinessError).message;
            console.error(\`getDrawableDescriptorByName failed, error code: ${code}, message: ${message}.\`);
        }
    }
}

#### \[h2\]getBoolean9+

getBoolean(resId: number): boolean

Obtains a Boolean value based on the specified resource ID. This API returns the result synchronously.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Global.ResourceManager

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| resId | number | Yes | Resource ID. |

**Return value**

| Type | Description |
| :-- | :-- |
| boolean | Boolean value. |

**Error codes**

For details about the error codes, see [Resource Manager Error Codes](../../error-codes/resource-manager-error-codes/document.md) and [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | If the input parameter invalid. Possible causes: Incorrect parameter types. |
| 9001001 | Invalid resource ID. |
| 9001002 | No matching resource is found based on the resource ID. |
| 9001006 | The resource is referenced cyclically. |

**Example**

// Resource file path: src/main/resources/base/element/boolean.json
{
  "boolean": \[
    {
      "name": "boolean\_test",
      "value": true
    }
  \]
}

import { AbilityConstant, UIAbility, Want } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

export default class EntryAbility extends UIAbility {
    onCreate(want: Want, launchParam: AbilityConstant.LaunchParam): void {
        try {
            // Replace 'app.boolean.boolean\_test' with the actual resource.
            let boolTest = this.context.resourceManager.getBoolean($r('app.boolean.boolean\_test').id);
            console.info(\`getBoolean, result: ${boolTest}\`);
            // Print the output result: getBoolean, result: true
        } catch (error) {
            let code = (error as BusinessError).code;
            let message = (error as BusinessError).message;
            console.error(\`getBoolean failed, error code: ${code}, message: ${message}.\`);
        }
    }
}

#### \[h2\]getBooleanByName9+

getBooleanByName(resName: string): boolean

Obtains a Boolean value based on the specified resource name. This API returns the result synchronously.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Global.ResourceManager

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| resName | string | Yes | Resource name. |

**Return value**

| Type | Description |
| :-- | :-- |
| boolean | Boolean value. |

**Error codes**

For details about the error codes, see [Resource Manager Error Codes](../../error-codes/resource-manager-error-codes/document.md) and [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | If the input parameter invalid. Possible causes: Incorrect parameter types. |
| 9001003 | Invalid resource name. |
| 9001004 | No matching resource is found based on the resource name. |
| 9001006 | The resource is referenced cyclically. |

**Example**

// Resource file path: src/main/resources/base/element/boolean.json
{
  "boolean": \[
    {
      "name": "boolean\_test",
      "value": true
    }
  \]
}

import { AbilityConstant, UIAbility, Want } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

export default class EntryAbility extends UIAbility {
    onCreate(want: Want, launchParam: AbilityConstant.LaunchParam): void {
        try {
            // Replace "boolean\_test" with the actual resource.
            let boolTest = this.context.resourceManager.getBooleanByName("boolean\_test");
            console.info(\`getBooleanByName, result: ${boolTest}\`);
            // Print the output result: getBooleanByName, result: true
        } catch (error) {
            let code = (error as BusinessError).code;
            let message = (error as BusinessError).message;
            console.error(\`getBooleanByName failed, error code: ${code}, message: ${message}.\`);
        }
    }
}

#### \[h2\]getNumber9+

getNumber(resId: number): number

Obtains an integer or float number based on the specified resource ID. This API returns the result synchronously.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Global.ResourceManager

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| resId | number | Yes | Resource ID. |

**Return value**

| Type | Description |
| :-- | :-- |
| number | 
Integer or float value corresponding to the specified resource ID.

An integer indicates the original value, and a float number without a unit indicates the original value and a float number with the unit of vp or fp indicates the px value. For details, see the sample code.

 |

**Error codes**

For details about the error codes, see [Resource Manager Error Codes](../../error-codes/resource-manager-error-codes/document.md) and [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | If the input parameter invalid. Possible causes: Incorrect parameter types. |
| 9001001 | Invalid resource ID. |
| 9001002 | No matching resource is found based on the resource ID. |
| 9001006 | The resource is referenced cyclically. |

**Example**

// Resource file path: src/main/resources/base/element/integer.json
{
  "integer": \[
    {
      "name": "integer\_test",
      "value": 100
    }
  \]
}

// Resource file path: src/main/resources/base/element/float.json
{
  "float": \[
    {
      "name": "float\_test",
      "value": "30.6vp"
    }
  \]
}

import { AbilityConstant, UIAbility, Want } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { display } from '@kit.ArkUI';

export default class EntryAbility extends UIAbility {
    onCreate(want: Want, launchParam: AbilityConstant.LaunchParam): void {
        try {
            // An integer refers to the original value.
            // Replace 'app.integer.integer\_test' with the actual resource.
            let intValue = this.context.resourceManager.getNumber($r('app.integer.integer\_test').id);
            console.info(\`getNumber, int value: ${intValue}\`);
            // Print the output result: getNumber, int value: 100
        } catch (error) {
            let code = (error as BusinessError).code;
            let message = (error as BusinessError).message;
            console.error(\`getNumber failed, error code: ${code}, message: ${message}.\`);
        }

        try {
            // A float number without a unit indicates the original value, and a float number with the unit of vp or fp indicates the px value (float number with the unit of vp or fp = original value x densityPixels).
            // Replace 'app.float.float\_test' with the actual resource.
            let floatValue = this.context.resourceManager.getNumber($r('app.float.float\_test').id);
            console.info(\`getNumber, densityPixels: ${display.getDefaultDisplaySync().densityPixels}, float value: ${floatValue}\`);
            // Print the output result: getNumber, densityPixels: 3.25, float value: 99.45000457763672
        } catch (error) {
            let code = (error as BusinessError).code;
            let message = (error as BusinessError).message;
            console.error(\`getNumber failed, error code: ${code}, message: ${message}.\`);
        }
    }
}

#### \[h2\]getNumberByName9+

getNumberByName(resName: string): number

Obtains an integer or float number based on the specified resource name. This API returns the result synchronously.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Global.ResourceManager

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| resName | string | Yes | Resource name. |

**Return value**

| Type | Description |
| :-- | :-- |
| number | 
Integer or float value corresponding to the specified resource name.

An integer indicates the original value, and a float number without a unit indicates the original value and a float number with the unit of vp or fp indicates the px value.

 |

**Error codes**

For details about the error codes, see [Resource Manager Error Codes](../../error-codes/resource-manager-error-codes/document.md) and [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | If the input parameter invalid. Possible causes: Incorrect parameter types. |
| 9001003 | Invalid resource name. |
| 9001004 | No matching resource is found based on the resource name. |
| 9001006 | The resource is referenced cyclically. |

**Example**

// Resource file path: src/main/resources/base/element/integer.json
{
  "integer": \[
    {
      "name": "integer\_test",
      "value": 100
    }
  \]
}

// Resource file path: src/main/resources/base/element/float.json
{
  "float": \[
    {
      "name": "float\_test",
      "value": "30.6vp"
    }
  \]
}

import { AbilityConstant, UIAbility, Want } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { display } from '@kit.ArkUI';

export default class EntryAbility extends UIAbility {
    onCreate(want: Want, launchParam: AbilityConstant.LaunchParam): void {
        try {
            // An integer refers to the original value.
            // Replace "integer\_test" with the actual resource.
            let intValue = this.context.resourceManager.getNumberByName("integer\_test");
            console.info(\`getNumberByName, int value: ${intValue}\`);
            // Print the output result: getNumberByName, int value: 100
        } catch (error) {
            let code = (error as BusinessError).code;
            let message = (error as BusinessError).message;
            console.error(\`getNumberByName failed, error code: ${code}, message: ${message}.\`);
        }

        try {
            // A float number without a unit indicates the original value, and a float number with the unit of vp or fp indicates the px value (float number with the unit of vp or fp = original value x densityPixels).
            // Replace "float\_test" with the actual resource.
            let floatValue = this.context.resourceManager.getNumberByName("float\_test");
            console.info(\`getNumberByName, densityPixels: ${display.getDefaultDisplaySync().densityPixels}, float value: ${floatValue}\`);
            // Print the output result: getNumberByName, densityPixels: 3.25, float value: 99.45000457763672
        } catch (error) {
            let code = (error as BusinessError).code;
            let message = (error as BusinessError).message;
            console.error(\`getNumberByName failed, error code: ${code}, message: ${message}.\`);
        }
    }
}

#### \[h2\]getColorSync10+

getColorSync(resId: number) : number

Obtains a color value based on the specified resource ID. This API returns the result synchronously.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Global.ResourceManager

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| resId | number | Yes | Resource ID. |

**Return value**

| Type | Description |
| :-- | :-- |
| number | Color value (decimal) corresponding to the specified resource ID. |

**Error codes**

For details about the error codes, see [Resource Manager Error Codes](../../error-codes/resource-manager-error-codes/document.md) and [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | If the input parameter invalid. Possible causes: Incorrect parameter types. |
| 9001001 | Invalid resource ID. |
| 9001002 | No matching resource is found based on the resource ID. |
| 9001006 | The resource is referenced cyclically. |

**Example**

// Resource file path: src/main/resources/base/element/color.json
{
  "color": \[
    {
      "name": "test",
      "value": "#FFFFFF"
    }
  \]
}

import { AbilityConstant, UIAbility, Want } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

export default class EntryAbility extends UIAbility {
    onCreate(want: Want, launchParam: AbilityConstant.LaunchParam): void {
        try {
            // Replace 'app.color.test' with the actual resource.
            let colorValue = this.context.resourceManager.getColorSync($r('app.color.test').id);
            console.info(\`getColorSync, result: ${colorValue}\`);
            // Print the output result: getColorSync, result: 4294967295
        } catch (error) {
            let code = (error as BusinessError).code;
            let message = (error as BusinessError).message;
            console.error(\`getColorSync failed, error code: ${code}, message: ${message}.\`);
        }
    }
}

#### \[h2\]getColorByNameSync10+

getColorByNameSync(resName: string) : number

Obtains a color value based on the specified resource name. This API returns the result synchronously.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Global.ResourceManager

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| resName | string | Yes | Resource name. |

**Return value**

| Type | Description |
| :-- | :-- |
| number | Color value (decimal) corresponding to the specified resource name. |

**Error codes**

For details about the error codes, see [Resource Manager Error Codes](../../error-codes/resource-manager-error-codes/document.md) and [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | If the input parameter invalid. Possible causes: Incorrect parameter types. |
| 9001003 | Invalid resource name. |
| 9001004 | No matching resource is found based on the resource name. |
| 9001006 | The resource is referenced cyclically. |

**Example**

// Resource file path: src/main/resources/base/element/color.json
{
  "color": \[
    {
      "name": "test",
      "value": "#FFFFFF"
    }
  \]
}

import { AbilityConstant, UIAbility, Want } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

export default class EntryAbility extends UIAbility {
    onCreate(want: Want, launchParam: AbilityConstant.LaunchParam): void {
        try {
            // Replace "test" with the actual resource.
            let colorValue = this.context.resourceManager.getColorByNameSync("test");
            console.info(\`getColorByNameSync, result: ${colorValue}\`);
            // Print the output result: getColorByNameSync, result: 4294967295
        } catch (error) {
            let code = (error as BusinessError).code;
            let message = (error as BusinessError).message;
            console.error(\`getColorByNameSync failed, error code: ${code}, message: ${message}.\`);
        }
    }
}

#### \[h2\]getColor10+

getColor(resId: number, callback: \_AsyncCallback<number>): void

Obtains a color value based on the specified resource ID. This API uses an asynchronous callback to return the result.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Global.ResourceManager

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| resId | number | Yes | Resource ID. |
| callback | [\_AsyncCallback](../../../../system/basic-functions/basic-services-kit/arkts-apis/others/ohos-base-public-callback-information/document.md#asynccallback)<number> | Yes | Callback used to return the color value (decimal). |

**Error codes**

For details about the error codes, see [Resource Manager Error Codes](../../error-codes/resource-manager-error-codes/document.md) and [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | If the input parameter invalid. Possible causes: Incorrect parameter types. |
| 9001001 | Invalid resource ID. |
| 9001002 | No matching resource is found based on the resource ID. |
| 9001006 | The resource is referenced cyclically. |

**Example (stage)**

// Resource file path: src/main/resources/base/element/color.json
{
  "color": \[
    {
      "name": "test",
      "value": "#FFFFFF"
    }
  \]
}

import { AbilityConstant, UIAbility, Want } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

export default class EntryAbility extends UIAbility {
    onCreate(want: Want, launchParam: AbilityConstant.LaunchParam): void {
        // Replace 'app.color.test' with the actual resource.
        this.context.resourceManager.getColor($r('app.color.test').id, (error: BusinessError, value: number) => {
            if (error != null) {
                console.error(\`callback getColor failed, error code: ${error.code}, message: ${error.message}.\`);
            } else {
                console.info(\`getColor, result: ${value}\`);
                // Print the output result: getColor, result: 4294967295
            }
        });
    }
}

#### \[h2\]getColor10+

getColor(resId: number): Promise<number>

Obtains a color value based on the specified resource ID. This API uses a promise to return the result.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Global.ResourceManager

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| resId | number | Yes | Resource ID. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<number> | Promise used to return the color value (decimal). |

**Error codes**

For details about the error codes, see [Resource Manager Error Codes](../../error-codes/resource-manager-error-codes/document.md) and [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | If the input parameter invalid. Possible causes: Incorrect parameter types. |
| 9001001 | Invalid resource ID. |
| 9001002 | No matching resource is found based on the resource ID. |
| 9001006 | The resource is referenced cyclically. |

**Example**

// Resource file path: src/main/resources/base/element/color.json
{
  "color": \[
    {
      "name": "test",
      "value": "#FFFFFF"
    }
  \]
}

import { AbilityConstant, UIAbility, Want } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

export default class EntryAbility extends UIAbility {
    onCreate(want: Want, launchParam: AbilityConstant.LaunchParam): void {
        // Replace 'app.color.test' with the actual resource.
        this.context.resourceManager.getColor($r('app.color.test').id)
            .then((value: number) => {
                console.info(\`getColor, result: ${value}\`);
                // Print the output result: getColor, result: 4294967295
            })
            .catch((error: BusinessError) => {
                console.error(\`promise getColor failed, error code: ${error.code}, message: ${error.message}.\`);
            });
    }
}

#### \[h2\]getColorByName10+

getColorByName(resName: string, callback: \_AsyncCallback<number>): void

Obtains a color value based on the specified resource name. This API uses an asynchronous callback to return the result.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Global.ResourceManager

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| resName | string | Yes | Resource name. |
| callback | [\_AsyncCallback](../../../../system/basic-functions/basic-services-kit/arkts-apis/others/ohos-base-public-callback-information/document.md#asynccallback)<number> | Yes | Callback used to return the color value (decimal). |

**Error codes**

For details about the error codes, see [Resource Manager Error Codes](../../error-codes/resource-manager-error-codes/document.md) and [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | If the input parameter invalid. Possible causes: Incorrect parameter types. |
| 9001003 | Invalid resource name. |
| 9001004 | No matching resource is found based on the resource name. |
| 9001006 | The resource is referenced cyclically. |

**Example**

// Resource file path: src/main/resources/base/element/color.json
{
  "color": \[
    {
      "name": "test",
      "value": "#FFFFFF"
    }
  \]
}

import { AbilityConstant, UIAbility, Want } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

export default class EntryAbility extends UIAbility {
    onCreate(want: Want, launchParam: AbilityConstant.LaunchParam): void {
        // Replace "test" with the actual resource.
        this.context.resourceManager.getColorByName("test", (error: BusinessError, value: number) => {
            if (error != null) {
                console.error(\`callback getColorByName failed, error code: ${error.code}, message: ${error.message}.\`);
            } else {
                console.info(\`getColorByName, result: ${value}\`);
                // Print the output result: getColorByName, result: 4294967295
            }
        });
    }
}

#### \[h2\]getColorByName10+

getColorByName(resName: string): Promise<number>

Obtains a color value based on the specified resource name. This API uses a promise to return the result.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Global.ResourceManager

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| resName | string | Yes | Resource name. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<number> | Promise used to return the color value (decimal). |

**Error codes**

For details about the error codes, see [Resource Manager Error Codes](../../error-codes/resource-manager-error-codes/document.md) and [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | If the input parameter invalid. Possible causes: Incorrect parameter types. |
| 9001003 | Invalid resource name. |
| 9001004 | No matching resource is found based on the resource name. |
| 9001006 | The resource is referenced cyclically. |

**Example**

// Resource file path: src/main/resources/base/element/color.json
{
  "color": \[
    {
      "name": "test",
      "value": "#FFFFFF"
    }
  \]
}

import { AbilityConstant, UIAbility, Want } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

export default class EntryAbility extends UIAbility {
    onCreate(want: Want, launchParam: AbilityConstant.LaunchParam): void {
        // Replace "test" with the actual resource.
        this.context.resourceManager.getColorByName("test")
            .then((value: number) => {
                console.info(\`getColorByName, result: ${value}\`);
                // Print the output result: getColorByName, result: 4294967295
            })
            .catch((error: BusinessError) => {
                console.error(\`promise getColorByName failed, error code: ${error.code}, message: ${error.message}.\`);
            });
    }
}

#### \[h2\]getRawFileContentSync10+

getRawFileContentSync(path: string): Uint8Array

Obtains the content of a rawfile in the **resources/rawfile** directory. This API returns the result synchronously.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Global.ResourceManager

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| path | string | Yes | Path of the rawfile. |

**Return value**

| Type | Description |
| :-- | :-- |
| Uint8Array | Content of the rawfile. |

**Error codes**

For details about the error codes, see [Resource Manager Error Codes](../../error-codes/resource-manager-error-codes/document.md) and [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | If the input parameter invalid. Possible causes: Incorrect parameter types. |
| 9001005 | Invalid relative path. |

**Example**

import { AbilityConstant, UIAbility, Want } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

export default class EntryAbility extends UIAbility {
    onCreate(want: Want, launchParam: AbilityConstant.LaunchParam): void {
        try {
            // Replace "test.txt" with the actual resource.
            this.context.resourceManager.getRawFileContentSync("test.txt");
        } catch (error) {
            let code = (error as BusinessError).code;
            let message = (error as BusinessError).message;
            console.error(\`getRawFileContentSync failed, error code: ${code}, message: ${message}.\`);
        }
    }
}

#### \[h2\]getRawFileContent9+

getRawFileContent(path: string, callback: \_AsyncCallback<Uint8Array>): void

Obtains the content of a rawfile in the **resources/rawfile** directory. This API uses an asynchronous callback to return the result.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Global.ResourceManager

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| path | string | Yes | Path of the rawfile. |
| callback | [\_AsyncCallback](../../../../system/basic-functions/basic-services-kit/arkts-apis/others/ohos-base-public-callback-information/document.md#asynccallback)<Uint8Array> | Yes | Callback used to return the content of the rawfile. |

**Error codes**

For details about the error codes, see [Resource Manager Error Codes](../../error-codes/resource-manager-error-codes/document.md) and [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | If the input parameter invalid. Possible causes: Incorrect parameter types. |
| 9001005 | Invalid relative path. |

**Example**

import { AbilityConstant, UIAbility, Want } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

export default class EntryAbility extends UIAbility {
    onCreate(want: Want, launchParam: AbilityConstant.LaunchParam): void {
        try {
            // Replace "test.txt" with the actual resource.
            this.context.resourceManager.getRawFileContent("test.txt", (error: BusinessError, value: Uint8Array) => {
                if (error != null) {
                    console.error("error is " + error);
                } else {
                    let rawFile = value;
                }
            });
        } catch (error) {
            let code = (error as BusinessError).code;
            let message = (error as BusinessError).message;
            console.error(\`callback getRawFileContent failed, error code: ${code}, message: ${message}.\`);
        }
    }
}

#### \[h2\]getRawFileContent9+

getRawFileContent(path: string): Promise<Uint8Array>

Obtains the content of a rawfile in the **resources/rawfile** directory. This API uses a promise to return the result.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Global.ResourceManager

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| path | string | Yes | Path of the rawfile. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<Uint8Array> | Promise used to return the content of the rawfile. |

**Error codes**

For details about the error codes, see [Resource Manager Error Codes](../../error-codes/resource-manager-error-codes/document.md) and [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | If the input parameter invalid. Possible causes: Incorrect parameter types. |
| 9001005 | Invalid relative path. |

**Example**

import { AbilityConstant, UIAbility, Want } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

export default class EntryAbility extends UIAbility {
    onCreate(want: Want, launchParam: AbilityConstant.LaunchParam): void {
        try {
            // Replace "test.txt" with the actual resource.
            this.context.resourceManager.getRawFileContent("test.txt").then((value: Uint8Array) => {
                let rawFile = value;
            }).catch((error: BusinessError) => {
                console.error("getRawFileContent promise error is " + error);
            });
        } catch (error) {
            let code = (error as BusinessError).code;
            let message = (error as BusinessError).message;
            console.error(\`promise getRawFileContent failed, error code: ${code}, message: ${message}.\`);
        }
    }
}

#### \[h2\]getRawFileListSync10+

getRawFileListSync(path: string): Array<string>

Obtains the list of folders and files in the **resources/rawfile** directory. This API returns the result synchronously.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/dd/v3/xd4lLaw6Rbip7rpsiH3LOg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062326Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=3DC48EAB7A30CBDD1BD467274EE2DDA87FC47A29AA0014378526622B56F927AA)

If there is no folder or file in the directory, an exception is thrown. If there are folders and files in the directory, the list of the folders and files is returned.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Global.ResourceManager

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| path | string | Yes | **rawfile** directory. |

**Return value**

| Type | Description |
| :-- | :-- |
| Array<string> | List of folders and files in the **rawfile** directory. |

**Error codes**

For details about the error codes, see [Resource Manager Error Codes](../../error-codes/resource-manager-error-codes/document.md) and [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | If the input parameter invalid. Possible causes: Incorrect parameter types. |
| 9001005 | Invalid relative path. |

**Example**

import { AbilityConstant, UIAbility, Want } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

export default class EntryAbility extends UIAbility {
    onCreate(want: Want, launchParam: AbilityConstant.LaunchParam): void {
        try {
            // Passing "" means to obtain the list of files in the root directory (that is, /rawfile). Assume that the test.txt file exists in the root directory.
            // Replace "" with the actual file path in the rawfile directory.
            let fileList: Array<string> = this.context.resourceManager.getRawFileListSync("");
            console.info(\`getRawFileListSync, result: ${JSON.stringify(fileList)}\`);
            // Print the output result: getRawFileListSync, result: \["test.txt"\]
        } catch (error) {
            let code = (error as BusinessError).code;
            let message = (error as BusinessError).message;
            console.error(\`getRawFileListSync failed, error code: ${code}, message: ${message}.\`);
        }
    }
}

#### \[h2\]getRawFileList10+

getRawFileList(path: string, callback: \_AsyncCallback<Array<string>>): void

Obtains the list of folders and files in the **resources/rawfile** directory. This API uses an asynchronous callback to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/38/v3/JTs7szxJR2qt4YeHJy4LHg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062326Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=AA25BA079F563D53ED82D19A8DB004459C10C1499385E6001416EAA7A6121167)

If there is no folder or file in the directory, an exception is thrown. If there are folders and files in the directory, the list of the folders and files is returned.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Global.ResourceManager

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| path | string | Yes | **rawfile** directory. |
| callback | [\_AsyncCallback](../../../../system/basic-functions/basic-services-kit/arkts-apis/others/ohos-base-public-callback-information/document.md#asynccallback)<Array<string>> | Yes | Callback used to return the list of folders and files. |

**Error codes**

For details about the error codes, see [Resource Manager Error Codes](../../error-codes/resource-manager-error-codes/document.md) and [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | If the input parameter invalid. Possible causes: Incorrect parameter types. |
| 9001005 | Invalid relative path. |

**Example**

import { AbilityConstant, UIAbility, Want } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

export default class EntryAbility extends UIAbility {
    onCreate(want: Want, launchParam: AbilityConstant.LaunchParam): void {
        // Passing "" means to obtain the list of files in the root directory (that is, /rawfile). Assume that the test.txt file exists in the root directory.
        // Replace "" with the actual file path in the rawfile directory.
        this.context.resourceManager.getRawFileList("", (error: BusinessError, value: Array<string>) => {
            if (error != null) {
                console.error(\`callback getRawFileList failed, error code: ${error.code}, message: ${error.message}.\`);
            } else {
                console.info(\`getRawFileList, result: ${JSON.stringify(value)}\`);
                // Print the output result: getRawFileList, result: \["test.txt"\].
            }
        });
    }
}

#### \[h2\]getRawFileList10+

getRawFileList(path: string): Promise<Array<string>>

Obtains the list of folders and files in the **resources/rawfile** directory. This API uses a promise to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a0/v3/_dn0madDSTKsFK_b43Xa5A/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062326Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=DFE233AD0F76C3D145445B5DF8871BA71796B7C4E27D60D1F1C814C7F550720C)

If there is no folder or file in the directory, an exception is thrown. If there are folders and files in the directory, the list of the folders and files is returned.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Global.ResourceManager

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| path | string | Yes | **rawfile** directory. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<Array<string>> | Promise used to return the list of folders and files. |

**Error codes**

For details about the error codes, see [Resource Manager Error Codes](../../error-codes/resource-manager-error-codes/document.md) and [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | If the input parameter invalid. Possible causes: Incorrect parameter types. |
| 9001005 | Invalid relative path. |

**Example**

import { AbilityConstant, UIAbility, Want } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

export default class EntryAbility extends UIAbility {
    onCreate(want: Want, launchParam: AbilityConstant.LaunchParam): void {
        // Passing "" means to obtain the list of files in the root directory (that is, /rawfile). Assume that the test.txt file exists in the root directory.
        // Replace "" with the actual file path in the rawfile directory.
        this.context.resourceManager.getRawFileList("")
            .then((value: Array<string>) => {
                console.info(\`getRawFileList, result: ${JSON.stringify(value)}\`);
                // Print the output result: getRawFileList, result: \["test.txt"\].
            })
            .catch((error: BusinessError) => {
                console.error(\`promise getRawFileList failed, error code: ${error.code}, message: ${error.message}.\`);
            });
    }
}

#### \[h2\]getRawFdSync10+

getRawFdSync(path: string): RawFileDescriptor

Obtains the file descriptor (fd) of the HAP where the rawfile file in the resources/rawfile directory is located. This API is called in synchronous mode.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2b/v3/3x8hrC5JTea39T_iXiSEbg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062326Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=263C233B7371779971C71F718E00ADF3BB492BE1A5DCBC525CBCF9ED5C3B4F38)

To prevent resource leakage, call [closeRawFdSync](#closerawfdsync10) or [closeRawFd](#closerawfd9) to close the fd after use.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Global.ResourceManager

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| path | string | Yes | Path of the rawfile. |

**Return value**

| Type | Description |
| :-- | :-- |
| [RawFileDescriptor](#rawfiledescriptor9) | fd of the HAP where the rawfile is located. |

**Error codes**

For details about the error codes, see [Resource Manager Error Codes](../../error-codes/resource-manager-error-codes/document.md) and [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | If the input parameter invalid. Possible causes: Incorrect parameter types. |
| 9001005 | Invalid relative path. |

**Example**

import { AbilityConstant, UIAbility, Want } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

export default class EntryAbility extends UIAbility {
    onCreate(want: Want, launchParam: AbilityConstant.LaunchParam): void {
        try {
            // Replace "test.txt" with the actual resource.
            this.context.resourceManager.getRawFdSync("test.txt");
        } catch (error) {
            let code = (error as BusinessError).code;
            let message = (error as BusinessError).message;
            console.error(\`getRawFdSync failed, error code: ${code}, message: ${message}.\`);
        }
    }
}

#### \[h2\]getRawFd9+

getRawFd(path: string, callback: \_AsyncCallback<RawFileDescriptor>): void

Obtains the fd of the HAP where a specific rawfile in the **resources/rawfile** directory is located. This API uses an asynchronous callback to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9b/v3/EbPC7AfkS1SxfgD9m54X0g/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062326Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=B688F8CA3DACDF5E0F217F1517770E61225FB62D8D55515AAB778F9C3AA49F4F)

To prevent resource leakage, call [closeRawFdSync](#closerawfdsync10) or [closeRawFd](#closerawfd9) to close the fd after use.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Global.ResourceManager

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| path | string | Yes | Path of the rawfile. |
| callback | [\_AsyncCallback](../../../../system/basic-functions/basic-services-kit/arkts-apis/others/ohos-base-public-callback-information/document.md#asynccallback)<[RawFileDescriptor](#rawfiledescriptor9)\> | Yes | Callback used to return the fd of the HAP. |

**Error codes**

For details about the error codes, see [Resource Manager Error Codes](../../error-codes/resource-manager-error-codes/document.md) and [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | If the input parameter invalid. Possible causes: Incorrect parameter types. |
| 9001005 | Invalid relative path. |

**Example**

import { AbilityConstant, UIAbility, Want } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { resourceManager } from '@kit.LocalizationKit';

export default class EntryAbility extends UIAbility {
    onCreate(want: Want, launchParam: AbilityConstant.LaunchParam): void {
        try {
            // Replace "test.txt" with the actual resource.
            this.context.resourceManager.getRawFd("test.txt", (error: BusinessError, value: resourceManager.RawFileDescriptor) => {
                if (error != null) {
                    console.error(\`callback getRawFd failed error code: ${error.code}, message: ${error.message}.\`);
                } else {
                    let fd = value.fd;
                    let offset = value.offset;
                    let length = value.length;
                }
            });
        } catch (error) {
            let code = (error as BusinessError).code;
            let message = (error as BusinessError).message;
            console.error(\`callback getRawFd failed, error code: ${code}, message: ${message}.\`);
        }
    }
}

#### \[h2\]getRawFd9+

getRawFd(path: string): Promise<RawFileDescriptor>

Obtains the fd of the HAP where a specific rawfile in the **resources/rawfile** directory is located. This API uses a promise to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/71/v3/FAnKgOBoQ8GjZLeF40b_Yg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062326Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=1DCC5C946528475BB746F38D2E00FB47BF17CCB7237AA945D4141884807BA448)

To prevent resource leakage, call [closeRawFdSync](#closerawfdsync10) or [closeRawFd](#closerawfd9) to close the fd after use.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Global.ResourceManager

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| path | string | Yes | Path of the rawfile. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<[RawFileDescriptor](#rawfiledescriptor9)\> | Promise used to return the fd of the HAP. |

**Error codes**

For details about the error codes, see [Resource Manager Error Codes](../../error-codes/resource-manager-error-codes/document.md) and [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | If the input parameter invalid. Possible causes: Incorrect parameter types. |
| 9001005 | Invalid relative path. |

**Example**

import { AbilityConstant, UIAbility, Want } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { resourceManager } from '@kit.LocalizationKit';

export default class EntryAbility extends UIAbility {
    onCreate(want: Want, launchParam: AbilityConstant.LaunchParam): void {
        try {
            // Replace "test.txt" with the actual resource.
            this.context.resourceManager.getRawFd("test.txt").then((value: resourceManager.RawFileDescriptor) => {
                let fd = value.fd;
                let offset = value.offset;
                let length = value.length;
            }).catch((error: BusinessError) => {
                console.error(\`promise getRawFd error error code: ${error.code}, message: ${error.message}.\`);
            });
        } catch (error) {
            let code = (error as BusinessError).code;
            let message = (error as BusinessError).message;
            console.error(\`promise getRawFd failed, error code: ${code}, message: ${message}.\`);
        }
    }
}

#### \[h2\]closeRawFdSync10+

closeRawFdSync(path: string): void

Obtains the fd of the HAP where a specific rawfile in the **resources/rawfile** directory is located. This API returns the result synchronously.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Global.ResourceManager

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| path | string | Yes | Path of the rawfile. |

**Error codes**

For details about the error codes, see [Resource Manager Error Codes](../../error-codes/resource-manager-error-codes/document.md) and [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | If the input parameter invalid. Possible causes: Incorrect parameter types. |
| 9001005 | Invalid relative path. |

**Example**

import { AbilityConstant, UIAbility, Want } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

export default class EntryAbility extends UIAbility {
  onCreate(want: Want, launchParam: AbilityConstant.LaunchParam): void {
    try {
      // Replace "test.txt" with the actual resource.
      let rawfile = this.context.resourceManager.getRawFdSync("test.txt");
      // Use rawfile resources based on the actual service scenario.

      this.context.resourceManager.closeRawFdSync("test.txt");
      console.info(\`closeRawFdSync test success.\`);
    } catch (error) {
      let code = (error as BusinessError).code;
      let message = (error as BusinessError).message;
      console.error(\`closeRawFdSync test failed, error code: ${code}, message: ${message}.\`);
    }
  }
}

#### \[h2\]closeRawFd9+

closeRawFd(path: string, callback: \_AsyncCallback<void>): void

Closes the fd of the HAP where a specific rawfile in the **resources/rawfile** directory is located. This API uses an asynchronous callback to return the result.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Global.ResourceManager

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| path | string | Yes | Path of the rawfile. |
| callback | [\_AsyncCallback](../../../../system/basic-functions/basic-services-kit/arkts-apis/others/ohos-base-public-callback-information/document.md#asynccallback)<void> | Yes | Callback used to return the result. If the operation is successful, **err** is **undefined**. Otherwise, **err** is an error object. |

**Error codes**

For details about the error codes, see [Resource Manager Error Codes](../../error-codes/resource-manager-error-codes/document.md) and [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | If the input parameter invalid. Possible causes: Incorrect parameter types. |
| 9001005 | Invalid relative path. |

**Example**

import { AbilityConstant, UIAbility, Want } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

export default class EntryAbility extends UIAbility {
  onCreate(want: Want, launchParam: AbilityConstant.LaunchParam): void {
    try {
      // Replace "test.txt" with the actual resource.
      let rawfile = this.context.resourceManager.getRawFdSync("test.txt");
      // Use rawfile resources based on the actual service scenario.
      this.context.resourceManager.closeRawFd("test.txt", (error: BusinessError) => {
        if (error != null) {
          console.error("error is " + error);
          return;
        }
        console.info('closeRawFd success.');
      });
    } catch (error) {
      let code = (error as BusinessError).code;
      let message = (error as BusinessError).message;
      console.error(\`callback closeRawFd failed, error code: ${code}, message: ${message}.\`);
    }
  }
}

#### \[h2\]closeRawFd9+

closeRawFd(path: string): Promise<void>

Closes the fd of the HAP where a specific rawfile in the **resources/rawfile** directory is located. This API uses a promise to return the result.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Global.ResourceManager

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| path | string | Yes | Path of the rawfile. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Error codes**

For details about the error codes, see [Resource Manager Error Codes](../../error-codes/resource-manager-error-codes/document.md) and [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | If the input parameter invalid. Possible causes: Incorrect parameter types. |
| 9001005 | Invalid relative path. |

**Example**

import { AbilityConstant, UIAbility, Want } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

export default class EntryAbility extends UIAbility {
  onCreate(want: Want, launchParam: AbilityConstant.LaunchParam): void {
    try {
      // Replace "test.txt" with the actual resource.
      let rawfile = this.context.resourceManager.getRawFdSync("test.txt");
      // Use rawfile resources based on the actual service scenario.
      this.context.resourceManager.closeRawFd("test.txt");
      console.info(\`closeRawFd test success.\`);
    } catch (error) {
      let code = (error as BusinessError).code;
      let message = (error as BusinessError).message;
      console.error(\`promise closeRawFd failed, error code: ${code}, message: ${message}.\`);
    }
  }
}

#### \[h2\]getConfigurationSync10+

getConfigurationSync(): Configuration

Obtains the device configuration. This API returns the result synchronously.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Global.ResourceManager

**Return value**

| Type | Description |
| :-- | :-- |
| [Configuration](#configuration) | Device configuration. |

**Example**

import { AbilityConstant, UIAbility, Want } from '@kit.AbilityKit';

export default class EntryAbility extends UIAbility {
    onCreate(want: Want, launchParam: AbilityConstant.LaunchParam): void {
        try {
            let value = this.context.resourceManager.getConfigurationSync();
            let direction = value.direction;
            let locale = value.locale;
        } catch (error) {
            console.error("getConfigurationSync error is " + error);
        }
    }
}

#### \[h2\]getConfiguration

getConfiguration(callback: \_AsyncCallback<Configuration>): void

Obtains the device configuration. This API uses an asynchronous callback to return the result.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Global.ResourceManager

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | [\_AsyncCallback](../../../../system/basic-functions/basic-services-kit/arkts-apis/others/ohos-base-public-callback-information/document.md#asynccallback)<[Configuration](#configuration)\> | Yes | Callback used to return the device configuration. |

**Example**

import { AbilityConstant, UIAbility, Want } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { resourceManager } from '@kit.LocalizationKit';

export default class EntryAbility extends UIAbility {
    onCreate(want: Want, launchParam: AbilityConstant.LaunchParam): void {
        try {
            this.context.resourceManager.getConfiguration((error: BusinessError, value: resourceManager.Configuration) => {
                if (error != null) {
                    console.error("getConfiguration callback error is " + error);
                } else {
                    let direction = value.direction;
                    let locale = value.locale;
                }
            });
        } catch (error) {
            console.error("getConfiguration callback error is " + error);
        }
    }
}

#### \[h2\]getConfiguration

getConfiguration(): Promise<Configuration>

Obtains the device configuration. This API uses a promise to return the result.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Global.ResourceManager

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<[Configuration](#configuration)\> | Promise used to return the device configuration. |

**Example**

import { AbilityConstant, UIAbility, Want } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { resourceManager } from '@kit.LocalizationKit';

export default class EntryAbility extends UIAbility {
    onCreate(want: Want, launchParam: AbilityConstant.LaunchParam): void {
        try {
            this.context.resourceManager.getConfiguration().then((value: resourceManager.Configuration) => {
                let direction = value.direction;
                let locale = value.locale;
            }).catch((error: BusinessError) => {
                console.error("getConfiguration promise error is " + error);
            });
        } catch (error) {
            console.error("getConfiguration promise error is " + error);
        }
    }
}

#### \[h2\]getDeviceCapabilitySync10+

getDeviceCapabilitySync(): DeviceCapability

Obtains the device capability. This API returns the result synchronously.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Global.ResourceManager

**Return value**

| Type | Description |
| :-- | :-- |
| [DeviceCapability](#devicecapability) | Device capability. |

**Example**

import { AbilityConstant, UIAbility, Want } from '@kit.AbilityKit';

export default class EntryAbility extends UIAbility {
    onCreate(want: Want, launchParam: AbilityConstant.LaunchParam): void {
        try {
            let value = this.context.resourceManager.getDeviceCapabilitySync();
            let screenDensity = value.screenDensity;
            let deviceType = value.deviceType;
        } catch (error) {
            console.error("getDeviceCapabilitySync error is " + error);
        }
    }
}

#### \[h2\]getDeviceCapability

getDeviceCapability(callback: \_AsyncCallback<DeviceCapability>): void

Obtains the device capability. This API uses an asynchronous callback to return the result.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Global.ResourceManager

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | [\_AsyncCallback](../../../../system/basic-functions/basic-services-kit/arkts-apis/others/ohos-base-public-callback-information/document.md#asynccallback)<[DeviceCapability](#devicecapability)\> | Yes | Callback used to return the device capability. |

**Example**

import { AbilityConstant, UIAbility, Want } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { resourceManager } from '@kit.LocalizationKit';

export default class EntryAbility extends UIAbility {
    onCreate(want: Want, launchParam: AbilityConstant.LaunchParam): void {
        try {
            this.context.resourceManager.getDeviceCapability((error: BusinessError, value: resourceManager.DeviceCapability) => {
                if (error != null) {
                    console.error("getDeviceCapability callback error is " + error);
                } else {
                    let screenDensity = value.screenDensity;
                    let deviceType = value.deviceType;
                }
            });
        } catch (error) {
            console.error("getDeviceCapability callback error is " + error);
        }
    }
}

#### \[h2\]getDeviceCapability

getDeviceCapability(): Promise<DeviceCapability>

Obtains the device capability. This API uses a promise to return the result.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Global.ResourceManager

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<[DeviceCapability](#devicecapability)\> | Promise used to return the device capability. |

**Example**

import { AbilityConstant, UIAbility, Want } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { resourceManager } from '@kit.LocalizationKit';

export default class EntryAbility extends UIAbility {
    onCreate(want: Want, launchParam: AbilityConstant.LaunchParam): void {
        try {
            this.context.resourceManager.getDeviceCapability().then((value: resourceManager.DeviceCapability) => {
                let screenDensity = value.screenDensity;
                let deviceType = value.deviceType;
            }).catch((error: BusinessError) => {
                console.error("getDeviceCapability promise error is " + error);
            });
        } catch (error) {
            console.error("getDeviceCapability promise error is " + error);
        }
    }
}

#### \[h2\]addResource10+

addResource(path: string): void

Loads resources from the specified path.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1c/v3/SEVxcUV9TFi9xgJul5xFAA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062326Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=7C92424217A84F81962AE505CA37726248239D07435496FBA980A00DFF496F16)

Resource overwriting is not supported for the **/rawfile** and **/resfile** directories.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Global.ResourceManager

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| path | string | Yes | Resource path. |

**Error codes**

For details about the error codes, see [Resource Manager Error Codes](../../error-codes/resource-manager-error-codes/document.md) and [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | If the input parameter invalid. Possible causes: Incorrect parameter types. |
| 9001010 | Invalid overlay path. |

**Example**

import { AbilityConstant, UIAbility, Want } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

export default class EntryAbility extends UIAbility {
    onCreate(want: Want, launchParam: AbilityConstant.LaunchParam): void {
        // Replace "/library1-default-signed.hsp" with the actual file path.
        let path = this.context.bundleCodeDir + "/library1-default-signed.hsp";
        try {
            this.context.resourceManager.addResource(path);
        } catch (error) {
            let code = (error as BusinessError).code;
            let message = (error as BusinessError).message;
            console.error(\`addResource failed, error code: ${code}, message: ${message}.\`);
        }
    }
}

#### \[h2\]removeResource10+

removeResource(path: string): void

Removes the resources loaded from the specified path to restore the original resources.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/05/v3/N1yP_FHjSiqMaKkVYPy3WA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062326Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=B9E7E7A8219841C4A30C2D24EA8F316DA411AC4A01CF5577656768748F64B03D)

Resource overwriting is not supported for the **/rawfile** and **/resfile** directories.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Global.ResourceManager

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| path | string | Yes | Resource path. |

**Error codes**

For details about the error codes, see [Resource Manager Error Codes](../../error-codes/resource-manager-error-codes/document.md) and [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | If the input parameter invalid. Possible causes: Incorrect parameter types. |
| 9001010 | Invalid overlay path. |

**Example**

import { AbilityConstant, UIAbility, Want } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

export default class EntryAbility extends UIAbility {
    onCreate(want: Want, launchParam: AbilityConstant.LaunchParam): void {
        // Replace "/library1-default-signed.hsp" with the actual file path.
        let path = this.context.bundleCodeDir + "/library1-default-signed.hsp";
        try {
            this.context.resourceManager.removeResource(path);
        } catch (error) {
            let code = (error as BusinessError).code;
            let message = (error as BusinessError).message;
            console.error(\`removeResource failed, error code: ${code}, message: ${message}.\`);
        }
    }
}

#### \[h2\]getLocales11+

getLocales(includeSystem?: boolean): Array<string>

Obtains the language list of an application.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Global.ResourceManager

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| includeSystem | boolean | No | 
Whether system resources are included. The default value is **false**.

\- **false**: Only application resources are included.

\- **true**: Both system and application resources are included.

If the value of **includeSystem** is invalid, the language list of system resources will be returned.

 |

**Return value**

| Type | Description |
| :-- | :-- |
| Array<string> | Language list. The strings in the list are comprised of the language, script (optional), and region (optional), which are connected by a hyphen (-). |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | If the input parameter invalid. Possible causes: Incorrect parameter types. |

**Example**

import { AbilityConstant, UIAbility, Want } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { resourceManager } from '@kit.LocalizationKit';

export default class EntryAbility extends UIAbility {
    onCreate(want: Want, launchParam: AbilityConstant.LaunchParam): void {
        try {
            this.context.resourceManager.getLocales(); // Obtain only the language list of application resources.
        } catch (error) {
            let code = (error as BusinessError).code;
            let message = (error as BusinessError).message;
            console.error(\`getLocales failed, error code: ${code}, message: ${message}.\`);
        }

        try {
            resourceManager.getSysResourceManager().getLocales(); // Obtain only the language list of system resources.
        } catch (error) {
            let code = (error as BusinessError).code;
            let message = (error as BusinessError).message;
            console.error(\`getLocales failed, error code: ${code}, message: ${message}.\`);
        }

        try {
            this.context.resourceManager.getLocales(true); // Obtain the language list of application resources and resources.
        } catch (error) {
            let code = (error as BusinessError).code;
            let message = (error as BusinessError).message;
            console.error(\`getLocales failed, error code: ${code}, message: ${message}.\`);
        }
    }
}

#### \[h2\]getSymbol11+

getSymbol(resId: number): number

Obtains the Unicode of a [symbol](https://developer.huawei.com/consumer/en/design/harmonyos-symbol) based on the specified resource ID. This API returns the result synchronously.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Global.ResourceManager

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| resId | number | Yes | Resource ID. |

**Return value**

| Type | Description |
| :-- | :-- |
| number | Unicode code (decimal) of the symbol. |

**Error codes**

For details about the error codes, see [Resource Manager Error Codes](../../error-codes/resource-manager-error-codes/document.md) and [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | If the input parameter invalid. Possible causes: Incorrect parameter types. |
| 9001001 | Invalid resource ID. |
| 9001002 | No matching resource is found based on the resource ID. |
| 9001006 | The resource is referenced cyclically. |

**Example**

import { AbilityConstant, UIAbility, Want } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

export default class EntryAbility extends UIAbility {
    onCreate(want: Want, launchParam: AbilityConstant.LaunchParam): void {
        try {
            // Replace 'sys.symbol.message' with the actual resource.
            let symbolValue = this.context.resourceManager.getSymbol($r('sys.symbol.message').id);
            console.info(\`getSymbol, result: ${symbolValue}\`);
            // Print the output result: getSymbol, result: 983183
        } catch (error) {
            let code = (error as BusinessError).code;
            let message = (error as BusinessError).message;
            console.error(\`getSymbol failed, error code: ${code}, message: ${message}.\`);
        }
    }
}

#### \[h2\]getSymbolByName11+

getSymbolByName(resName: string): number

Obtains the Unicode of a [symbol](https://developer.huawei.com/consumer/en/design/harmonyos-symbol) based on the specified resource name. This API returns the result synchronously.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Global.ResourceManager

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| resName | string | Yes | Resource name. |

**Return value**

| Type | Description |
| :-- | :-- |
| number | Unicode code (decimal) of the symbol. |

**Error codes**

For details about the error codes, see [Resource Manager Error Codes](../../error-codes/resource-manager-error-codes/document.md) and [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | If the input parameter invalid. Possible causes: Incorrect parameter types. |
| 9001003 | Invalid resource name. |
| 9001004 | No matching resource is found based on the resource name. |
| 9001006 | The resource is referenced cyclically. |

**Example**

import { AbilityConstant, UIAbility, Want } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

export default class EntryAbility extends UIAbility {
    onCreate(want: Want, launchParam: AbilityConstant.LaunchParam): void {
        try {
            // Replace "message" with the actual resource.
            let symbolValue = this.context.resourceManager.getSymbolByName("message");
            console.info(\`getSymbolByName, result: ${symbolValue}\`);
            // Print the output result: getSymbolByName, result: 983183
        } catch (error) {
            let code = (error as BusinessError).code;
            let message = (error as BusinessError).message;
            console.error(\`getSymbolByName failed, error code: ${code}, message: ${message}.\`);
        }
    }
}

#### \[h2\]isRawDir12+

isRawDir(path: string): boolean

Checks whether a path is a subdirectory in the **rawfile** directory. This API returns the result synchronously.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Global.ResourceManager

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| path | string | Yes | Path of a rawfile. |

**Return value**

| Type | Description |
| :-- | :-- |
| boolean | 
Whether the path is a subdirectory in the **rawfile** directory.

\- **true**: The path is a subdirectory in the **rawfile** directory.

\- **false**: The path is not a subdirectory in the **rawfile** directory.

 |

**Error codes**

For details about the error codes, see [Resource Manager Error Codes](../../error-codes/resource-manager-error-codes/document.md) and [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | If the input parameter invalid. Possible causes: Incorrect parameter types. |
| 9001005 | Invalid relative path. |

**Example**

import { AbilityConstant, UIAbility, Want } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

export default class EntryAbility extends UIAbility {
    onCreate(want: Want, launchParam: AbilityConstant.LaunchParam): void {
        try {
            // Assume that a non-empty folder named sub exists in the root directory (that is, /rawfile). The value of isRawDir is true in the return result.
            // Replace "sub" with the actual directory.
            let isRawDir = this.context.resourceManager.isRawDir("sub");
            // Print the output result: sub isRawDir, result: true
            console.info(\`sub isRawDir, result: ${isRawDir}\`);

            // If the test.txt file exists in the root directory, the value of isRawDir is false.
            // Replace "test.txt" with the actual resource.
            isRawDir = this.context.resourceManager.isRawDir("test.txt");
            // Print the output result: test.txt isRawDir, result: false
            console.info(\`test.txt isRawDir, result: ${isRawDir}\`);
        } catch (error) {
            let code = (error as BusinessError).code;
            let message = (error as BusinessError).message;
            console.error(\`isRawDir failed, error code: ${code}, message: ${message}.\`);
        }
    }
}

#### \[h2\]getOverrideResourceManager12+

getOverrideResourceManager(configuration?: Configuration): ResourceManager

Obtains a **ResourceManager** object for loading differentiated resources. This API returns the result synchronously.

The resource configuration (including the language, color mode, resolution, and orientation) obtained by a common **ResourceManager** object is determined by the system. With this API, an application can obtain resources of the specified configuration (that is, differentiated resources), for example, dark color resources in light color mode.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Global.ResourceManager

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| configuration | [Configuration](#configuration) | No | 
Resource configuration.

After obtaining the configuration of differentiated resources through [getOverrideConfiguration](#getoverrideconfiguration12), modify the configuration items as required, and then pass these items as input parameters to the API.

If no configuration is specified, the current system configuration is used.

 |

**Return value**

| Type | Description |
| :-- | :-- |
| ResourceManager | **ResourceManager** object for loading differentiated resources. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | If the input parameter invalid. Possible causes: Incorrect parameter types. |

**Example**

import { AbilityConstant, UIAbility, Want } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { resourceManager } from '@kit.LocalizationKit';

export default class EntryAbility extends UIAbility {
    onCreate(want: Want, launchParam: AbilityConstant.LaunchParam): void {
        try {
            let resMgr = this.context.resourceManager;
            let overrideConfig = resMgr.getOverrideConfiguration();
            overrideConfig.colorMode = resourceManager.ColorMode.DARK;
            let overrideResMgr = resMgr.getOverrideResourceManager(overrideConfig);
        } catch (error) {
            let code = (error as BusinessError).code;
            let message = (error as BusinessError).message;
            console.error(\`getOverrideResourceManager failed, error code: ${code}, message: ${message}.\`);
        }
    }
}

#### \[h2\]getOverrideConfiguration12+

getOverrideConfiguration(): Configuration

Obtains the configuration of differentiated resources. This API returns the result synchronously. This API allows a common **ResourceManager** object and a **ResourceManager** object obtained through [getOverrideResourceManager](#getoverrideresourcemanager12) to obtain the configuration of differentiated resources.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Global.ResourceManager

**Return value**

| Type | Description |
| :-- | :-- |
| [Configuration](#configuration) | Configuration of differentiated resources. |

**Example**

import { AbilityConstant, UIAbility, Want } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { resourceManager } from '@kit.LocalizationKit';

export default class EntryAbility extends UIAbility {
    onCreate(want: Want, launchParam: AbilityConstant.LaunchParam): void {
        try {
            let resMgr = this.context.resourceManager;
            let overrideConfig = resMgr.getOverrideConfiguration();
            overrideConfig.colorMode = resourceManager.ColorMode.DARK;
            let overrideResMgr = resMgr.getOverrideResourceManager(overrideConfig);
        } catch (error) {
            let code = (error as BusinessError).code;
            let message = (error as BusinessError).message;
            console.error(\`getOverrideResourceManager failed, error code: ${code}, message: ${message}.\`);
        }
    }
}

#### \[h2\]updateOverrideConfiguration12+

updateOverrideConfiguration(configuration: Configuration): void

Updated configuration of differentiated resources. This API allows a common **ResourceManager** object and a **ResourceManager** object obtained through [getOverrideResourceManager](#getoverrideresourcemanager12) to update the configuration of differentiated resources.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Global.ResourceManager

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| configuration | [Configuration](#configuration) | Yes | Configuration of differentiated resources. After obtaining the configuration of differentiated resources through [getOverrideConfiguration](#getoverrideconfiguration12), modify the configuration items as required, and then pass these items as input parameters to the API. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | If the input parameter invalid. Possible causes: Incorrect parameter types. |

**Example**

import { AbilityConstant, UIAbility, Want } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { resourceManager } from '@kit.LocalizationKit';

export default class EntryAbility extends UIAbility {
    onCreate(want: Want, launchParam: AbilityConstant.LaunchParam): void {
        try {
            let resMgr = this.context.resourceManager;
            let overrideConfig = resMgr.getOverrideConfiguration();
            overrideConfig.colorMode = resourceManager.ColorMode.DARK;
            let overrideResMgr = resMgr.updateOverrideConfiguration(overrideConfig);
        } catch (error) {
            let code = (error as BusinessError).code;
            let message = (error as BusinessError).message;
            console.error(\`updateOverrideConfiguration failed, error code: ${code}, message: ${message}.\`);
        }
    }
}

#### \[h2\]release(deprecated)

release()

Releases a **ResourceManager** object. This API is not supported currently.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/61/v3/jc3Mhe1MRtaAB1l8HEGS8g/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062326Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=DF6DAC893DDBC96AB647D772286E401167485A072C1CB0B50A00E554506495B1)

This API is supported since API version 7 and is deprecated since API version 12.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Global.ResourceManager

**Example**

try {
  this.context.resourceManager.release();
} catch (error) {
  console.error("release error is " + error);
}

#### \[h2\]getString(deprecated)

getString(resId: number, callback: AsyncCallback<string>): void

Obtains a string based on the specified resource ID. This API uses an asynchronous callback to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a6/v3/L-umwVmYQLO8zbxgLWbB5Q/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062326Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=C6D3ECD28E2457FC07F64BA663AC056C845D41A2769C81C3FF3D62B0A1654ECF)

This API is supported since API version 6 and is deprecated since API version 9. You are advised to use [getStringValue](#getstringvalue9).

**System capability**: SystemCapability.Global.ResourceManager

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| resId | number | Yes | Resource ID. |
| callback | [AsyncCallback](#asynccallbackdeprecated)<string> | Yes | Callback used to return the obtained string. |

**Example**

resourceManager.getResourceManager((error, mgr) => {
    mgr.getString($r('app.string.test').id, (error: Error, value: string) => {
        if (error != null) {
            console.error("error is " + error);
        } else {
            let str = value;
        }
    });
});

#### \[h2\]getString(deprecated)

getString(resId: number): Promise<string>

Obtains a string based on the specified resource ID. This API uses a promise to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/86/v3/a1aE2rxZSSC-YRMUy6nH9g/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062326Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=F2C25D5C9C1DDA9493B20C89FF8CEC4E425BA1F6811C377C998AB9AB007402C5)

This API is supported since API version 6 and is deprecated since API version 9. You are advised to use [getStringValue](#getstringvalue9-1).

**System capability**: SystemCapability.Global.ResourceManager

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| resId | number | Yes | Resource ID. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<string> | Promise used to return the obtained string. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

resourceManager.getResourceManager((error, mgr) => {
    mgr.getString($r('app.string.test').id).then((value: string) => {
        let str = value;
    }).catch((error: BusinessError) => {
        console.error("getstring promise error is " + error);
    });
});

#### \[h2\]getStringSync(deprecated)

getStringSync(resource: Resource): string

Obtains a string based on the specified resource object. This API returns the result synchronously.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/42/v3/yKLHbO2kTNGd0CctweKPaA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062326Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=151473B1469D5F2D8E3A812681A83752D35E1EF7A003668E786309802BB617A4)

This API is supported since API version 9 and is deprecated since API version 20. You are advised to use [getStringByNameSync](#getstringbynamesync9) or [getStringSync](#getstringsync9) instead.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Global.ResourceManager

**Model restriction**: This API can be used only in the stage model.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| resource | [Resource](#resource9) | Yes | Resource object. |

**Return value**

| Type | Description |
| :-- | :-- |
| string | String corresponding to the specified resource object. |

**Error codes**

For details about the error codes, see [Resource Manager Error Codes](../../error-codes/resource-manager-error-codes/document.md) and [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | If the input parameter invalid. Possible causes: Incorrect parameter types. |
| 9001001 | Invalid resource ID. |
| 9001002 | No matching resource is found based on the resource ID. |
| 9001006 | The resource is referenced cyclically. |

**Example**

// Resource file path: src/main/resources/base/element/string.json
{
  "string": \[
    {
      "name": "test",
      "value": "I'm a test string resource."
    }
  \]
}

import { resourceManager } from '@kit.LocalizationKit';
import { BusinessError } from '@kit.BasicServicesKit';

let resource: resourceManager.Resource = {
  bundleName: "com.example.myapplication",
  moduleName: "entry",
  id: $r('app.string.test').id
};
try {
  let testStr = this.context.resourceManager.getStringSync(resource);
  console.info(\`getStringSync, result: ${testStr}\`);
  // Print the output result: getStringSync, result: I'm a test string resource.
} catch (error) {
  let code = (error as BusinessError).code;
  let message = (error as BusinessError).message;
  console.error(\`getStringSync failed, error code: ${code}, message: ${message}.\`);
}

#### \[h2\]getStringSync(deprecated)

getStringSync(resource: Resource, ...args: Array<string | number>): string

Obtains a string based on the specified resource object and formats the string based on **args**. This API returns the result synchronously.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3b/v3/Go3EtLLoStudCYBmMgySVw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062326Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=929EB9A6BF5BDE5E076D6E4BBA06EAAB8118DD34E4321699EEC7A1162E19494D)

This API is supported since API version 10 and is deprecated since API version 20. You are advised to use [getStringByNameSync](#getstringbynamesync10) or [getStringSync](#getstringsync10) instead.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Global.ResourceManager

**Model restriction**: This API can be used only in the stage model.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| resource | [Resource](#resource9) | Yes | Resource object. |
| ...args | Array<string | number> | No | 
Arguments for formatting strings.

Supported value types include %d, %f, %s, %%, %number$d, %number$f, and %number$s.

Note: %% is converted to %. **number** in %number$d indicates the sequence number of the parameter in **args**.

For example, %%d is converted to %d after formatting, and %1$d indicates that the first parameter is used.

 |

**Return value**

| Type | Description |
| :-- | :-- |
| string | Formatted string corresponding to the specified resource object. |

**Error codes**

For details about the error codes, see [Resource Manager Error Codes](../../error-codes/resource-manager-error-codes/document.md) and [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | If the input parameter invalid. Possible causes: Incorrect parameter types. |
| 9001001 | Invalid resource ID. |
| 9001002 | No matching resource is found based on the resource ID. |
| 9001006 | The resource is referenced cyclically. |
| 9001007 | Failed to format the resource obtained based on the resource ID. |

**Example**

// Resource file path: src/main/resources/base/element/string.json
{
  "string": \[
    {
      "name": "test",
      "value": "I'm a %1$s, format int: %2$d, format float: %3$f."
    }
  \]
}

import { resourceManager } from '@kit.LocalizationKit';
import { BusinessError } from '@kit.BasicServicesKit';

let resource: resourceManager.Resource = {
  bundleName: "com.example.myapplication",
  moduleName: "entry",
  id: $r('app.string.test').id
};
try {
  let testStr = this.context.resourceManager.getStringSync(resource, "format string", 10, 98.78);
  console.info(\`getStringSync, result: ${testStr}\`);
  // Print the output result: getStringSync, result: I'm a format string, format int: 10, format float: 98.78.
} catch (error) {
  let code = (error as BusinessError).code;
  let message = (error as BusinessError).message;
  console.error(\`getStringSync failed, error code: ${code}, message: ${message}.\`);
}

#### \[h2\]getStringValue(deprecated)

getStringValue(resource: Resource, callback: \_AsyncCallback<string>): void

Obtains a string based on the specified resource object. This API uses an asynchronous callback to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/75/v3/wwp6UaJVRteExQfgExS4JQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062326Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=524DDB348D0478139506183CBA67EC01F278CFD27283BE07B6C4D2BAD41D9686)

This API is supported since API version 9 and is deprecated since API version 20. You are advised to use [getStringByName](#getstringbyname9) or [getStringValue](#getstringvalue9) instead.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Global.ResourceManager

**Model restriction**: This API can be used only in the stage model.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| resource | [Resource](#resource9) | Yes | Resource object. |
| callback | [\_AsyncCallback](../../../../system/basic-functions/basic-services-kit/arkts-apis/others/ohos-base-public-callback-information/document.md#asynccallback)<string> | Yes | Callback used to return the obtained string. |

**Error codes**

For details about the error codes, see [Resource Manager Error Codes](../../error-codes/resource-manager-error-codes/document.md) and [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | If the input parameter invalid. Possible causes: Incorrect parameter types. |
| 9001001 | Invalid resource ID. |
| 9001002 | No matching resource is found based on the resource ID. |
| 9001006 | The resource is referenced cyclically. |

**Example**

// Resource file path: src/main/resources/base/element/string.json
{
  "string": \[
    {
      "name": "test",
      "value": "I'm a test string resource."
    }
  \]
}

import { resourceManager } from '@kit.LocalizationKit';
import { BusinessError } from '@kit.BasicServicesKit';

let resource: resourceManager.Resource = {
  bundleName: "com.example.myapplication",
  moduleName: "entry",
  id: $r('app.string.test').id
};
this.context.resourceManager.getStringValue(resource, (error: BusinessError, value: string) => {
  if (error != null) {
    console.error(\`callback getStringValue failed, error code: ${error.code}, message: ${error.message}.\`);
  } else {
    console.info(\`getStringValue, result: ${value}\`);
    // Print the output result: getStringValue, result: I'm a test string resource.
  }
});

#### \[h2\]getStringValue(deprecated)

getStringValue(resource: Resource): Promise<string>

Obtains a string based on the specified resource object. This API uses a promise to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2c/v3/cTQlH9bFQzSGGi8jeXXK-A/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062326Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=A520CAD264BD8AFE046C4EBDD4D055BCE254FD0B3680C421DE3A136791E1C978)

This API is supported since API version 9 and is deprecated since API version 20. You are advised to use [getStringByName](#getstringbyname9-1) or [getStringValue](#getstringvalue9-1) instead.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Global.ResourceManager

**Model restriction**: This API can be used only in the stage model.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| resource | [Resource](#resource9) | Yes | Resource object. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<string> | Promise used to return the obtained string. |

**Error codes**

For details about the error codes, see [Resource Manager Error Codes](../../error-codes/resource-manager-error-codes/document.md) and [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | If the input parameter invalid. Possible causes: Incorrect parameter types. |
| 9001001 | Invalid resource ID. |
| 9001002 | No matching resource is found based on the resource ID. |
| 9001006 | The resource is referenced cyclically. |

**Example**

import { resourceManager } from '@kit.LocalizationKit';
import { BusinessError } from '@kit.BasicServicesKit';

let resource: resourceManager.Resource = {
  bundleName: "com.example.myapplication",
  moduleName: "entry",
  id: $r('app.string.test').id
};
this.context.resourceManager.getStringValue(resource, (error: BusinessError, value: string) => {
  if (error != null) {
    console.error(\`callback getStringValue failed, error code: ${error.code}, message: ${error.message}.\`);
  } else {
    console.info(\`getStringValue, result: ${value}\`);
    // Print the output result: getStringValue, result: I'm a test string resource.
  }
});

#### \[h2\]getStringArray(deprecated)

getStringArray(resId: number, callback: AsyncCallback<Array<string>>): void

Obtains a string array based on the specified resource ID. This API uses an asynchronous callback to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0/v3/Pmo__HFSQliCq0jvV0_Kpg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062326Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=66617F76AA1CD5F577877DB87CE82F1066BCF8ED303153BD186C879D26FF37BE)

This API is supported since API version 6 and is deprecated since API version 9. You are advised to use [getStringArrayValue](#getstringarrayvalue9).

**System capability**: SystemCapability.Global.ResourceManager

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| resId | number | Yes | Resource ID. |
| callback | [AsyncCallback](#asynccallbackdeprecated)<Array<string>> | Yes | Callback used to return the obtained string array. |

**Example**

resourceManager.getResourceManager((error, mgr) => {
    mgr.getStringArray($r('app.strarray.test').id, (error: Error, value: Array<string>) => {
        if (error != null) {
            console.error("error is " + error);
        } else {
            let strArray = value;
        }
    });
});

#### \[h2\]getStringArray(deprecated)

getStringArray(resId: number): Promise<Array<string>>

Obtains a string array based on the specified resource ID. This API uses a promise to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4b/v3/6XrlZDH3Rx6HOdg1YDevpw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062326Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=BA3DD2B59ADE631E7F0B98850244F6B4A7DFEBF59DCBF2038DE45BDAC976AE0E)

This API is supported since API version 6 and is deprecated since API version 9. You are advised to use [getStringArrayValue](#getstringarrayvalue9-1).

**System capability**: SystemCapability.Global.ResourceManager

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| resId | number | Yes | Resource ID. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<Array<string>> | Promise used to return the obtained string array. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

resourceManager.getResourceManager((error, mgr) => {
      mgr.getStringArray($r('app.strarray.test').id).then((value: Array<string>) => {
        let strArray = value;
    }).catch((error: BusinessError) => {
        console.error("getStringArray promise error is " + error);
    });
});

#### \[h2\]getStringArrayValueSync(deprecated)

getStringArrayValueSync(resource: Resource): Array<string>

Obtains a string array based on the specified resource object. This API returns the result synchronously.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/05/v3/IGNisxNURiW57-StgN_cHQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062326Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=A61A8CC7A1E643150CF213FBA69EE73A4CD4EDF3D710E63673081F5584C4A18C)

This method is supported since API version 10 and is deprecated since API version 20. You are advised to use [getStringArrayByNameSync](#getstringarraybynamesync10) or [getStringArrayValueSync](#getstringarrayvaluesync10) instead.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Global.ResourceManager

**Model restriction**: This API can be used only in the stage model.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| resource | [Resource](#resource9) | Yes | Resource object. |

**Return value**

| Type | Description |
| :-- | :-- |
| Array<string> | String array corresponding to the specified resource object. |

**Error codes**

For details about the error codes, see [Resource Manager Error Codes](../../error-codes/resource-manager-error-codes/document.md) and [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | If the input parameter invalid. Possible causes: Incorrect parameter types. |
| 9001001 | Invalid resource ID. |
| 9001002 | No matching resource is found based on the resource ID. |
| 9001006 | The resource is referenced cyclically. |

**Example**

// Resource file path: src/main/resources/base/element/strarray.json
{
  "strarray": \[
    {
      "name": "test",
      "value": \[
        {
          "value": "I'm one of the array's values."
        }
      \]
    }
  \]
}

import { resourceManager } from '@kit.LocalizationKit';
import { BusinessError } from '@kit.BasicServicesKit';

let resource: resourceManager.Resource = {
  bundleName: "com.example.myapplication",
  moduleName: "entry",
  id: $r('app.strarray.test').id
};
try {
  let strArray: Array<string> = this.context.resourceManager.getStringArrayValueSync(resource);
  console.info(\`getStringArrayValueSync, result: ${strArray\[0\]}\`);
  // Print the output result: getStringArrayValueSync, result: I'm one of the array's values.
} catch (error) {
  let code = (error as BusinessError).code;
  let message = (error as BusinessError).message;
  console.error(\`getStringArrayValueSync failed, error code: ${code}, message: ${message}.\`);
}

#### \[h2\]getStringArrayValue(deprecated)

getStringArrayValue(resource: Resource, callback: \_AsyncCallback<Array<string>>): void

Obtains a string array based on the specified resource object. This API uses an asynchronous callback to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/db/v3/mbDhzE7WRHOSF_W9SLoLUA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062326Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=75A0AD7B881728326C964A5DCA8040052D8CD422D06761751D179973E792CA0B)

This method is supported since API version 9 and is deprecated since API version 20. You are advised to use [getStringArrayByName](#getstringarraybyname9) or [getStringArrayValue](#getstringarrayvalue9) instead.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Global.ResourceManager

**Model restriction**: This API can be used only in the stage model.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| resource | [Resource](#resource9) | Yes | Resource object. |
| callback | [\_AsyncCallback](../../../../system/basic-functions/basic-services-kit/arkts-apis/others/ohos-base-public-callback-information/document.md#asynccallback)<Array<string>> | Yes | Callback used to return the obtained string array. |

**Error codes**

For details about the error codes, see [Resource Manager Error Codes](../../error-codes/resource-manager-error-codes/document.md) and [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | If the input parameter invalid. Possible causes: Incorrect parameter types. |
| 9001001 | Invalid resource ID. |
| 9001002 | No matching resource is found based on the resource ID. |
| 9001006 | The resource is referenced cyclically. |

**Example**

// Resource file path: src/main/resources/base/element/strarray.json
{
  "strarray": \[
    {
      "name": "test",
      "value": \[
        {
          "value": "I'm one of the array's values."
        }
      \]
    }
  \]
}

import { resourceManager } from '@kit.LocalizationKit';
import { BusinessError } from '@kit.BasicServicesKit';

let resource: resourceManager.Resource = {
  bundleName: "com.example.myapplication",
  moduleName: "entry",
  id: $r('app.strarray.test').id
};
this.context.resourceManager.getStringArrayValue(resource, (error: BusinessError, value: Array<string>) => {
  if (error != null) {
    console.error(\`callback getStringArrayValue failed, error code: ${error.code}, message: ${error.message}.\`);
  } else {
    console.info(\`getStringArrayValue, result: ${value\[0\]}\`);
    // Print the output result: getStringArrayValue, result: I'm one of the array's values.
  }
});

#### \[h2\]getStringArrayValue(deprecated)

getStringArrayValue(resource: Resource): Promise<Array<string>>

Obtains a string array based on the specified resource object. This API uses a promise to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b8/v3/7pPW9-vmSW2ikLD8_yBDvw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062326Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=DE253DBD98013E1CDFEB4309846623B1173ED35914100CF3554E456967E0E58F)

This method is supported since API version 9 and is deprecated since API version 20. You are advised to use [getStringArrayByName](#getstringarraybyname9-1) or [getStringArrayValue](#getstringarrayvalue9-1) instead.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Global.ResourceManager

**Model restriction**: This API can be used only in the stage model.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| resource | [Resource](#resource9) | Yes | Resource object. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<Array<string>> | Promise used to return the obtained string array. |

**Error codes**

For details about the error codes, see [Resource Manager Error Codes](../../error-codes/resource-manager-error-codes/document.md) and [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | If the input parameter invalid. Possible causes: Incorrect parameter types. |
| 9001001 | Invalid resource ID. |
| 9001002 | No matching resource is found based on the resource ID. |
| 9001006 | The resource is referenced cyclically. |

**Example**

// Resource file path: src/main/resources/base/element/strarray.json
{
  "strarray": \[
    {
      "name": "test",
      "value": \[
        {
          "value": "I'm one of the array's values."
        }
      \]
    }
  \]
}

import { resourceManager } from '@kit.LocalizationKit';
import { BusinessError } from '@kit.BasicServicesKit';

let resource: resourceManager.Resource = {
  bundleName: "com.example.myapplication",
  moduleName: "entry",
  id: $r('app.strarray.test').id
};
this.context.resourceManager.getStringArrayValue(resource)
  .then((value: Array<string>) => {
    console.info(\`getStringArrayValue, result: ${value\[0\]}\`);
    // Print the output result: getStringArrayValue, result: I'm one of the array's values.
  })
  .catch((error: BusinessError) => {
    console.error(\`promise getStringArrayValue failed, error code: ${error.code}, message: ${error.message}.\`);
  });

#### \[h2\]getMedia(deprecated)

getMedia(resId: number, callback: AsyncCallback<Uint8Array>): void

Obtains media file content based on the specified resource ID. This API uses an asynchronous callback to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8e/v3/9fv_GazwRuW7LVCW8598sw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062326Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=E1DA81E6BC572A0258202FEA40E037C45633DB35F9EB42DD44E7132CCD6D53F7)

This API is supported since API version 6 and is deprecated since API version 9. You are advised to use [getMediaContent](#getmediacontent9).

**System capability**: SystemCapability.Global.ResourceManager

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| resId | number | Yes | Resource ID. |
| callback | [AsyncCallback](#asynccallbackdeprecated)<Uint8Array> | Yes | Callback used to return the media file content. |

**Example**

resourceManager.getResourceManager((error, mgr) => {
    mgr.getMedia($r('app.media.test').id, (error: Error, value: Uint8Array) => {
        if (error != null) {
            console.error("error is " + error);
        } else {
            let media = value;
        }
    });
});

#### \[h2\]getMedia(deprecated)

getMedia(resId: number): Promise<Uint8Array>

Obtains media file content based on the specified resource ID. This API uses a promise to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e4/v3/r268l0TxRZmsBd8mW2EpHw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062326Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=B1CEB4B41341BB021E184055EC1CB7C3F99ADBBA0D3775A3680AF76C974AC6B4)

This API is supported since API version 6 and is deprecated since API version 9. You are advised to use [getMediaContent](#getmediacontent9-1).

**System capability**: SystemCapability.Global.ResourceManager

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| resId | number | Yes | Resource ID. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<Uint8Array> | Promise used to return the media file content. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

resourceManager.getResourceManager((error, mgr) => {
    mgr.getMedia($r('app.media.test').id).then((value: Uint8Array) => {
        let media = value;
    }).catch((error: BusinessError) => {
        console.error("getMedia promise error is " + error);
    });
});

#### \[h2\]getMediaContentSync(deprecated)

getMediaContentSync(resource: Resource, density?: number): Uint8Array

Obtains the media file content for the default or specified screen density based on the specified resource object. This API returns the result synchronously.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/43/v3/rVsCaRwYSNCOP5r0Wd_UHw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062326Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=9D22C489B9D5BED28A16B5E967FCF0644191883C39105D68BEC9F48790E534A3)

This API is supported since API version 10 and is deprecated since API version 20. You are advised to use [getMediaByNameSync](#getmediabynamesync10) or [getMediaContentSync](#getmediacontentsync10) instead.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Global.ResourceManager

**Model restriction**: This API can be used only in the stage model.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| resource | [Resource](#resource9) | Yes | Resource object. |
| [density](#screendensity) | number | No | Screen density. The default value or value **0** indicates the default screen density. |

**Return value**

| Type | Description |
| :-- | :-- |
| Uint8Array | Content of the media file corresponding to the specified resource object. |

**Error codes**

For details about the error codes, see [Resource Manager Error Codes](../../error-codes/resource-manager-error-codes/document.md) and [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | If the input parameter invalid. Possible causes: 1.Incorrect parameter types; 2.Parameter verification failed. |
| 9001001 | Invalid resource ID. |
| 9001002 | No matching resource is found based on the resource ID. |

**Example**

import { resourceManager } from '@kit.LocalizationKit';
import { BusinessError } from '@kit.BasicServicesKit';

let resource: resourceManager.Resource = {
  bundleName: "com.example.myapplication",
  moduleName: "entry",
  id: $r('app.media.test').id
};
try {
  this.context.resourceManager.getMediaContentSync(resource); // Default screen density
} catch (error) {
  let code = (error as BusinessError).code;
  let message = (error as BusinessError).message;
  console.error(\`getMediaContentSync failed, error code: ${code}, message: ${message}.\`);
}

try {
  this.context.resourceManager.getMediaContentSync(resource, 120); // Specified screen density
} catch (error) {
  let code = (error as BusinessError).code;
  let message = (error as BusinessError).message;
  console.error(\`getMediaContentSync failed, error code: ${code}, message: ${message}.\`);
}

#### \[h2\]getMediaContent(deprecated)

getMediaContent(resource: Resource, callback: \_AsyncCallback<Uint8Array>): void

Obtains media file content based on the specified resource object. This API uses an asynchronous callback to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c2/v3/VD25ErMDR6Sq53pt2j0xNw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062326Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=2188707C1D8B2C35DE2815058C92531707C6FEFAC3A798DFD876F4E15D7728D7)

This API is supported since API version 9 and is deprecated since API version 20. You are advised to use [getMediaByName](#getmediabyname9) or [getMediaContent](#getmediacontent9) instead.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Global.ResourceManager

**Model restriction**: This API can be used only in the stage model.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| resource | [Resource](#resource9) | Yes | Resource object. |
| callback | [\_AsyncCallback](../../../../system/basic-functions/basic-services-kit/arkts-apis/others/ohos-base-public-callback-information/document.md#asynccallback)<Uint8Array> | Yes | Callback used to return the media file content. |

**Error codes**

For details about the error codes, see [Resource Manager Error Codes](../../error-codes/resource-manager-error-codes/document.md) and [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | If the input parameter invalid. Possible causes: Incorrect parameter types. |
| 9001001 | Invalid resource ID. |
| 9001002 | No matching resource is found based on the resource ID. |

**Example**

import { resourceManager } from '@kit.LocalizationKit';
import { BusinessError } from '@kit.BasicServicesKit';

let resource: resourceManager.Resource = {
  bundleName: "com.example.myapplication",
  moduleName: "entry",
  id: $r('app.media.test').id
};
try {
  this.context.resourceManager.getMediaContent(resource, (error: BusinessError, value: Uint8Array) => {
    if (error != null) {
      console.error("error is " + error);
    } else {
      let media = value;
    }
  });
} catch (error) {
  let code = (error as BusinessError).code;
  let message = (error as BusinessError).message;
  console.error(\`callback getMediaContent failed, error code: ${code}, message: ${message}.\`);
}

#### \[h2\]getMediaContent(deprecated)

getMediaContent(resource: Resource, density: number, callback: \_AsyncCallback<Uint8Array>): void

Obtains media file content for the specified screen density based on the specified resource object. This API uses an asynchronous callback to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f2/v3/qVdKYwrTSLG_MslC6quEtA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062326Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=6D3F92ED459E25DC5C172DA4381442D5CEBA790BFD2A59CEC13C00A5D5B3F736)

This method is supported since API version 10 and is deprecated since API version 20. You are advised to use [getMediaByName](#getmediabyname10) or [getMediaContent](#getmediacontent10) instead.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Global.ResourceManager

**Model restriction**: This API can be used only in the stage model.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| resource | [Resource](#resource9) | Yes | Resource object. |
| [density](#screendensity) | number | Yes | Screen density. The value **0** indicates the default screen density. |
| callback | [\_AsyncCallback](../../../../system/basic-functions/basic-services-kit/arkts-apis/others/ohos-base-public-callback-information/document.md#asynccallback)<Uint8Array> | Yes | Callback used to return the media file content. |

**Error codes**

For details about the error codes, see [Resource Manager Error Codes](../../error-codes/resource-manager-error-codes/document.md) and [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | If the input parameter invalid. Possible causes: 1.Incorrect parameter types; 2.Parameter verification failed. |
| 9001001 | Invalid resource ID. |
| 9001002 | No matching resource is found based on the resource ID. |

**Example**

import { resourceManager } from '@kit.LocalizationKit';
import { BusinessError } from '@kit.BasicServicesKit';

let resource: resourceManager.Resource = {
  bundleName: "com.example.myapplication",
  moduleName: "entry",
  id: $r('app.media.test').id
};
try {
  this.context.resourceManager.getMediaContent(resource, 120, (error: BusinessError, value: Uint8Array) => {
    if (error != null) {
      console.error(\`callback getMediaContent failed, error code: ${error.code}, message: ${error.message}.\`);
    } else {
      let media = value;
    }
  });
} catch (error) {
  let code = (error as BusinessError).code;
  let message = (error as BusinessError).message;
  console.error(\`callback getMediaContent failed, error code: ${code}, message: ${message}.\`);
}

#### \[h2\]getMediaContent(deprecated)

getMediaContent(resource: Resource): Promise<Uint8Array>

Obtains media file content based on the specified resource object. This API uses a promise to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f1/v3/-d9xRvMbT56kka2siU9l1g/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062326Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=45BA7575A3002E0171F2BEB0549142EBF82CF911D3D84B5062001732A930310D)

This API is supported since API version 9 and is deprecated since API version 20. You are advised to use [getMediaByName](#getmediabyname9-1) or [getMediaContent](#getmediacontent9-1) instead.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Global.ResourceManager

**Model restriction**: This API can be used only in the stage model.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| resource | [Resource](#resource9) | Yes | Resource object. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<Uint8Array> | Promise used to return the media file content. |

**Error codes**

For details about the error codes, see [Resource Manager Error Codes](../../error-codes/resource-manager-error-codes/document.md) and [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | If the input parameter invalid. Possible causes: Incorrect parameter types. |
| 9001001 | Invalid resource ID. |
| 9001002 | No matching resource is found based on the resource ID. |

**Example**

import { resourceManager } from '@kit.LocalizationKit';
import { BusinessError } from '@kit.BasicServicesKit';

let resource: resourceManager.Resource = {
  bundleName: "com.example.myapplication",
  moduleName: "entry",
  id: $r('app.media.test').id
};
try {
  this.context.resourceManager.getMediaContent(resource).then((value: Uint8Array) => {
    let media = value;
  }).catch((error: BusinessError) => {
    console.error("getMediaContent promise error is " + error);
  });
} catch (error) {
  let code = (error as BusinessError).code;
  let message = (error as BusinessError).message;
  console.error(\`promise getMediaContent failed, error code: ${code}, message: ${message}.\`);
}

#### \[h2\]getMediaContent(deprecated)

getMediaContent(resource: Resource, density: number): Promise<Uint8Array>

Obtains media file content for the specified screen density based on the specified resource object. This API uses a promise to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/71/v3/z7N0G66YSZy-7gjmQDwojQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062326Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=20AE5EE1F27327E4D2AE66666D8D1E43CA6CDB35149503F91DAD29F572A12F14)

This API is supported since API version 10 and is deprecated since API version 20. You are advised to use [getMediaByName](#getmediabyname10-1) or [getMediaContent](#getmediacontent10-1) instead.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Global.ResourceManager

**Model restriction**: This API can be used only in the stage model.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| resource | [Resource](#resource9) | Yes | Resource object. |
| [density](#screendensity) | number | Yes | Screen density. The value **0** indicates the default screen density. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<Uint8Array> | Promise used to return the media file content. |

**Error codes**

For details about the error codes, see [Resource Manager Error Codes](../../error-codes/resource-manager-error-codes/document.md) and [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | If the input parameter invalid. Possible causes: 1.Incorrect parameter types; 2.Parameter verification failed. |
| 9001001 | Invalid resource ID. |
| 9001002 | No matching resource is found based on the resource ID. |

**Example**

import { resourceManager } from '@kit.LocalizationKit';
import { BusinessError } from '@kit.BasicServicesKit';

let resource: resourceManager.Resource = {
  bundleName: "com.example.myapplication",
  moduleName: "entry",
  id: $r('app.media.test').id
};
try {
  this.context.resourceManager.getMediaContent(resource, 120).then((value: Uint8Array) => {
    let media = value;
  }).catch((error: BusinessError) => {
    console.error(\`promise getMediaContent failed, error code: ${error.code}, message: ${error.message}.\`);
  });
} catch (error) {
  let code = (error as BusinessError).code;
  let message = (error as BusinessError).message;
  console.error(\`promise getMediaContent failed, error code: ${code}, message: ${message}.\`);
}

#### \[h2\]getMediaBase64(deprecated)

getMediaBase64(resId: number, callback: AsyncCallback<string>): void

Obtains an image's Base64 code based on the specified resource ID. This API uses an asynchronous callback to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a2/v3/PvWZoCwgTUmKlWCHDQkNkA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062326Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=84CFFF48679F28CEE3FB89F55EE81DAFBA30D449C551EA9D990163AF75F5E293)

This API is supported since API version 6 and is deprecated since API version 9. You are advised to use [getMediaContentBase64](#getmediacontentbase649).

**System capability**: SystemCapability.Global.ResourceManager

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| resId | number | Yes | Resource ID. |
| callback | [AsyncCallback](#asynccallbackdeprecated)<string> | Yes | Callback used to return the Base64 code of the image. |

**Example**

resourceManager.getResourceManager((error, mgr) => {
    mgr.getMediaBase64($r('app.media.test').id, ((error: Error, value: string) => {
        if (error != null) {
            console.error("error is " + error);
        } else {
            let media = value;
        }
    });
});

#### \[h2\]getMediaBase64(deprecated)

getMediaBase64(resId: number): Promise<string>

Obtains an image's Base64 code based on the specified resource ID. This API uses a promise to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/26/v3/6wfhV7G3Q1C71GDH7kv7Tg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062326Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=1896C38145A90BB40D45EB75DD58ED26FB80514A4D42596AD5EC235981ED6A9D)

This API is supported since API version 6 and is deprecated since API version 9. You are advised to use [getMediaContentBase64](#getmediacontentbase649-1).

**System capability**: SystemCapability.Global.ResourceManager

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| resId | number | Yes | Resource ID. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<string> | Promise used to return the Base64 code of the image. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

resourceManager.getResourceManager((error, mgr) => {
    mgr.getMediaBase64($r('app.media.test').id).then((value: string) => {
        let media = value;
    }).catch((error: BusinessError) => {
        console.error("getMediaBase64 promise error is " + error);
    });
});

#### \[h2\]getMediaContentBase64Sync(deprecated)

getMediaContentBase64Sync(resource: Resource, density?: number): string

Obtains an image's Base64 code for the default or specified screen density based on the specified resource object. This API returns the result synchronously.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/59/v3/fIPuT2_vRRu1lQ4jQ4ImsQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062326Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=4E6CBFD4D881496D6C91997BA63F46060C7860A7C3A8A3E506A839C5F3236CD9)

This API is supported since API version 10 and is deprecated since API version 20. You are advised to use [getMediaBase64ByNameSync](#getmediabase64bynamesync10) or [getMediaContentBase64Sync](#getmediacontentbase64sync10) instead.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Global.ResourceManager

**Model restriction**: This API can be used only in the stage model.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| resource | [Resource](#resource9) | Yes | Resource object. |
| [density](#screendensity) | number | No | Screen density. The default value or value **0** indicates the default screen density. |

**Return value**

| Type | Description |
| :-- | :-- |
| string | Base64 code of the image corresponding to the specified resource object. |

**Error codes**

For details about the error codes, see [Resource Manager Error Codes](../../error-codes/resource-manager-error-codes/document.md) and [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | If the input parameter invalid. Possible causes: 1.Incorrect parameter types; 2.Parameter verification failed. |
| 9001001 | Invalid resource ID. |
| 9001002 | No matching resource is found based on the resource ID. |

**Example**

import { resourceManager } from '@kit.LocalizationKit';
import { BusinessError } from '@kit.BasicServicesKit';

let resource: resourceManager.Resource = {
  bundleName: "com.example.myapplication",
  moduleName: "entry",
  id: $r('app.media.test').id
};
try {
  this.context.resourceManager.getMediaContentBase64Sync(resource); // Default screen density
} catch (error) {
  let code = (error as BusinessError).code;
  let message = (error as BusinessError).message;
  console.error(\`getMediaContentBase64Sync failed, error code: ${code}, message: ${message}.\`);
}

try {
  this.context.resourceManager.getMediaContentBase64Sync(resource, 120); // Specified screen density
} catch (error) {
  let code = (error as BusinessError).code;
  let message = (error as BusinessError).message;
  console.error(\`getMediaContentBase64Sync failed, error code: ${code}, message: ${message}.\`);
}

#### \[h2\]getMediaContentBase64(deprecated)

getMediaContentBase64(resource: Resource, callback: \_AsyncCallback<string>): void

Obtains an image's Base64 code based on the specified resource object. This API uses an asynchronous callback to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f1/v3/eMKdltDbQOe7YuTTyrqkvA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062326Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=CD8F2F8E95C432F01A05D0F27269F59DB693956F6B91DA4D9E9495A44384B3F5)

This API is supported since API version 9 and is deprecated since API version 20. You are advised to use [getMediaBase64ByName](#getmediabase64byname9) or [getMediaContentBase64](#getmediacontentbase649) instead.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Global.ResourceManager

**Model restriction**: This API can be used only in the stage model.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| resource | [Resource](#resource9) | Yes | Resource object. |
| callback | [\_AsyncCallback](../../../../system/basic-functions/basic-services-kit/arkts-apis/others/ohos-base-public-callback-information/document.md#asynccallback)<string> | Yes | Callback used to return the Base64 code of the image. |

**Error codes**

For details about the error codes, see [Resource Manager Error Codes](../../error-codes/resource-manager-error-codes/document.md) and [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | If the input parameter invalid. Possible causes: Incorrect parameter types. |
| 9001001 | Invalid resource ID. |
| 9001002 | No matching resource is found based on the resource ID. |

**Example**

import { resourceManager } from '@kit.LocalizationKit';
import { BusinessError } from '@kit.BasicServicesKit';

let resource: resourceManager.Resource = {
  bundleName: "com.example.myapplication",
  moduleName: "entry",
  id: $r('app.media.test').id
};
try {
  this.context.resourceManager.getMediaContentBase64(resource, (error: BusinessError, value: string) => {
    if (error != null) {
      console.error("error is " + error);
    } else {
      let media = value;
    }
  });
} catch (error) {
  let code = (error as BusinessError).code;
  let message = (error as BusinessError).message;
  console.error(\`callback getMediaContentBase64 failed, error code: ${code}, message: ${message}.\`);
}

#### \[h2\]getMediaContentBase64(deprecated)

getMediaContentBase64(resource: Resource, density: number, callback: \_AsyncCallback<string>): void

Obtains an image's Base64 code for the specified screen density based on the specified resource object. This API uses an asynchronous callback to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/81/v3/tBNoeSv6Qpe-bh6sbipeCA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062326Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=5B4269232C8B2D567100E4E71E60606970EA6E9D308BFBD6038661AB52CC32C4)

This API is supported since API version 10 and is deprecated since API version 20. You are advised to use [getMediaBase64ByName](#getmediabase64byname10) or [getMediaContentBase64](#getmediacontentbase6410) instead.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Global.ResourceManager

**Model restriction**: This API can be used only in the stage model.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| resource | [Resource](#resource9) | Yes | Resource object. |
| [density](#screendensity) | number | Yes | Screen density. The value **0** indicates the default screen density. |
| callback | [\_AsyncCallback](../../../../system/basic-functions/basic-services-kit/arkts-apis/others/ohos-base-public-callback-information/document.md#asynccallback)<string> | Yes | Callback used to return the Base64 code of the image. |

**Error codes**

For details about the error codes, see [Resource Manager Error Codes](../../error-codes/resource-manager-error-codes/document.md) and [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | If the input parameter invalid. Possible causes: 1.Incorrect parameter types; 2.Parameter verification failed. |
| 9001001 | Invalid resource ID. |
| 9001002 | No matching resource is found based on the resource ID. |

**Example**

import { resourceManager } from '@kit.LocalizationKit';
import { BusinessError } from '@kit.BasicServicesKit';

let resource: resourceManager.Resource = {
  bundleName: "com.example.myapplication",
  moduleName: "entry",
  id: $r('app.media.test').id
};
try {
  this.context.resourceManager.getMediaContentBase64(resource, 120, (error: BusinessError, value: string) => {
    if (error != null) {
      console.error(\`callback getMediaContentBase64 failed, error code: ${error.code}, message: ${error.message}.\`);
    } else {
      let media = value;
    }
  });
} catch (error) {
  let code = (error as BusinessError).code;
  let message = (error as BusinessError).message;
  console.error(\`callback getMediaContentBase64 failed, error code: ${code}, message: ${message}.\`);
}

#### \[h2\]getMediaContentBase64(deprecated)

getMediaContentBase64(resource: Resource): Promise<string>

Obtains an image's Base64 code based on the specified resource object. This API uses a promise to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7a/v3/vf7UasrHRFSjVac9q7HDkA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062326Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=DAA2C4E0A7E4705AF81D8649D48EE048BCB07C44D5D7C342CF02732EEB57C0CB)

This API is supported since API version 9 and is deprecated since API version 20. You are advised to use [getMediaBase64ByName](#getmediabase64byname9-1) or [getMediaContentBase64](#getmediacontentbase649-1).

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Global.ResourceManager

**Model restriction**: This API can be used only in the stage model.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| resource | [Resource](#resource9) | Yes | Resource object. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<string> | Promise used to return the Base64 code of the image. |

**Error codes**

For details about the error codes, see [Resource Manager Error Codes](../../error-codes/resource-manager-error-codes/document.md) and [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | If the input parameter invalid. Possible causes: Incorrect parameter types. |
| 9001001 | Invalid resource ID. |
| 9001002 | No matching resource is found based on the resource ID. |

**Example**

import { resourceManager } from '@kit.LocalizationKit';
import { BusinessError } from '@kit.BasicServicesKit';

let resource: resourceManager.Resource = {
  bundleName: "com.example.myapplication",
  moduleName: "entry",
  id: $r('app.media.test').id
};
try {
  this.context.resourceManager.getMediaContentBase64(resource).then((value: string) => {
    let media = value;
  }).catch((error: BusinessError) => {
    console.error("getMediaContentBase64 promise error is " + error);
  });
} catch (error) {
  let code = (error as BusinessError).code;
  let message = (error as BusinessError).message;
  console.error(\`promise getMediaContentBase64 failed, error code: ${code}, message: ${message}.\`);
}

#### \[h2\]getMediaContentBase64(deprecated)

getMediaContentBase64(resource: Resource, density: number): Promise<string>

Obtains an image's Base64 code for the specified screen density based on the specified resource object. This API uses a promise to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c3/v3/21Vunl3TTtefP85wYhWy7A/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062326Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=DA47FBDBEFC7651E8434FA542CB9BF08923C61CFFCC934584F4C87EB8641D0AB)

Supports versions from API version 10 and is deprecated in API version 20. You are advised to use [getMediaBase64ByName](#getmediabase64byname10-1) or [getMediaContentBase64](#getmediacontentbase6410-1) instead.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Global.ResourceManager

**Model restriction**: This API can be used only in the stage model.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| resource | [Resource](#resource9) | Yes | Resource object. |
| [density](#screendensity) | number | Yes | Screen density. The value **0** indicates the default screen density. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<string> | Promise used to return the Base64 code of the image. |

**Error codes**

For details about the error codes, see [Resource Manager Error Codes](../../error-codes/resource-manager-error-codes/document.md) and [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | If the input parameter invalid. Possible causes: 1.Incorrect parameter types; 2.Parameter verification failed. |
| 9001001 | Invalid resource ID. |
| 9001002 | No matching resource is found based on the resource ID. |

**Example**

import { resourceManager } from '@kit.LocalizationKit';
import { BusinessError } from '@kit.BasicServicesKit';

let resource: resourceManager.Resource = {
  bundleName: "com.example.myapplication",
  moduleName: "entry",
  id: $r('app.media.test').id
};
try {
  this.context.resourceManager.getMediaContentBase64(resource, 120).then((value: string) => {
    let media = value;
  }).catch((error: BusinessError) => {
    console.error(\`promise getMediaContentBase64 failed, error code: ${error.code}, message: ${error.message}.\`);
  });
} catch (error) {
  let code = (error as BusinessError).code;
  let message = (error as BusinessError).message;
  console.error(\`promise getMediaContentBase64 failed, error code: ${code}, message: ${message}.\`);
}

#### \[h2\]getDrawableDescriptor(deprecated)

getDrawableDescriptor(resource: Resource, density?: number, type?: number): DrawableDescriptor

Obtains a **DrawableDescriptor** object for icon display based on the specified resource object. This API returns the result synchronously.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/29/v3/_WlzAdXoSIuNsex2DH_qYQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062326Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=4C443D67F15DF01E9ACAA2D5CC6B7FBC06C9422AB8C4E09F6D7829A0427C8B13)

This API is supported since API version 10 and is deprecated since API version 20. You are advised to use [getDrawableDescriptorByName](#getdrawabledescriptorbyname10) or \[getDrawableDescriptor\] (#getdrawabledescriptor10) instead.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Global.ResourceManager

**Model restriction**: This API can be used only in the stage model.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| resource | [Resource](#resource9) | Yes | Resource object. |
| [density](#screendensity) | number | No | Screen density. The default value or value **0** indicates the default screen density. |
| type11+ | number | No | 
\- **1**: Layered icon resource of the application in the theme resource package.

\- **0** or default value: Icon resource of the application.

 |

**Return value**

| Type | Description |
| :-- | :-- |
| [DrawableDescriptor](../../../arkui/arkts-api/ui/ohos-arkui-drawabledescriptor-drawabledescriptor/document.md#drawabledescriptor) | **DrawableDescriptor** object corresponding to the specified resource ID. |

**Error codes**

For details about the error codes, see [Resource Manager Error Codes](../../error-codes/resource-manager-error-codes/document.md) and [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | If the input parameter invalid. Possible causes: 1.Incorrect parameter types; 2.Parameter verification failed. |
| 9001001 | Invalid resource ID. |
| 9001002 | No matching resource is found based on the resource ID. |

**Example**

import { resourceManager } from '@kit.LocalizationKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { DrawableDescriptor } from '@kit.ArkUI';

let resource: resourceManager.Resource = {
  bundleName: "com.example.myapplication",
  moduleName: "entry",
  id: $r('app.media.icon').id
};
try {
  let drawableDescriptor:DrawableDescriptor = this.context.resourceManager.getDrawableDescriptor(resource);
} catch (error) {
  let code = (error as BusinessError).code;
  let message = (error as BusinessError).message;
  console.error(\`getDrawableDescriptor failed, error code: ${code}, message: ${message}.\`);
}
try {
  let drawableDescriptor:DrawableDescriptor = this.context.resourceManager.getDrawableDescriptor(resource, 120);
} catch (error) {
  let code = (error as BusinessError).code;
  let message = (error as BusinessError).message;
  console.error(\`getDrawableDescriptor failed, error code: ${code}, message: ${message}.\`);
}
try {
  let drawableDescriptor:DrawableDescriptor = this.context.resourceManager.getDrawableDescriptor(resource, 0, 1);
} catch (error) {
  let code = (error as BusinessError).code;
  let message = (error as BusinessError).message;
  console.error(\`getDrawableDescriptor failed, error code: ${code}, message: ${message}.\`);
}

#### \[h2\]getIntPluralStringValueSync(deprecated)

getIntPluralStringValueSync(resource: Resource, num: number, ...args: Array<string | number>): string

Obtains a [singular/plural](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/l10n-singular-plural) string based on the specified resource object and formats the string based on the **args** parameter. This API returns the result synchronously.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/be/v3/GQM_4TKMQwWzuJzx0paeGg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062326Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=31493D2165497B4FD7A34F754E90E1D73652C664CDAFA9E2E791CE5BC15F19CB)

-   This API is supported since API version 18 and is deprecated since API version 20. You are advised to use [getIntPluralStringByNameSync](#getintpluralstringbynamesync18) or [getIntPluralStringValueSync](#getintpluralstringvaluesync18) instead.
    
-   Strings distinguish between singular and plural forms in all languages except Chinese. For details, see [Language Plural Rules](https://www.unicode.org/cldr/charts/45/supplemental/language_plural_rules.html).
    

**Atomic service API**: This API can be used in atomic services since API version 18.

**System capability**: SystemCapability.Global.ResourceManager

**Model restriction**: This API can be used only in the stage model.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| resource | [Resource](#resource9) | Yes | Resource object. |
| num | number | Yes | Integer number used to obtain the corresponding string representation based on the current language's [plural rules](https://www.unicode.org/cldr/charts/45/supplemental/language_plural_rules.html). |
| ...args | Array<string | number> | No | 
Arguments for formatting strings.

Supported value types include %d, %f, %s, %%, %number$d, %number$f, and %number$s.

Note: %% is converted to %. **number** in %number$d indicates the sequence number of the parameter in **args**.

For example, %%d is converted to %d after formatting, and %1$d indicates that the first parameter is used.

 |

**Return value**

| Type | Description |
| :-- | :-- |
| string | Formatted string corresponding to the specified resource object. |

**Error codes**

For details about the error codes, see [Resource Manager Error Codes](../../error-codes/resource-manager-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 9001001 | Invalid resource ID. |
| 9001002 | No matching resource is found based on the resource ID. |
| 9001006 | The resource is referenced cyclically. |
| 9001007 | Failed to format the resource obtained based on the resource ID. |

**Example**

// Resource file path: src/main/resources/base/element/plural.json
{
  "plural": \[
    {
      "name": "format\_test",
      "value": \[
        {
          "quantity": "one",
          "value": "There is %d apple in the %s, the total amount is %f kg."
        },
        {
          "quantity": "other",
          "value": "There are %d apples in the %s, the total amount is %f kg."
        }
      \]
    }
  \]
}

import { resourceManager } from '@kit.LocalizationKit';
import { BusinessError } from '@kit.BasicServicesKit';

let resource: resourceManager.Resource = {
  bundleName: "com.example.myapplication",
  moduleName: "entry",
  id: $r('app.plural.format\_test').id
};

try {
  // If num is 1, the single/plural type is one in the English environment.
  // The quantity field in the resource file indicates the single/plural type. Therefore, the string whose quantity is one is obtained.
  let pluralStr = this.context.resourceManager.getIntPluralStringValueSync(resource, 1, 1, "basket", 0.3);
  console.info(\`getIntPluralStringValueSync, result: ${pluralStr}\`);
  // Print the output result: getIntPluralStringValueSync, result: There is 1 apple in the basket, the total amount is 0.3 kg.
} catch (error) {
  let code = (error as BusinessError).code;
  let message = (error as BusinessError).message;
  console.error(\`getIntPluralStringValueSync failed, error code: ${code}, message: ${message}.\`);
}

#### \[h2\]getDoublePluralStringValueSync(deprecated)

getDoublePluralStringValueSync(resource: Resource, num: number, ...args: Array<string | number>): string

Obtains a [singular/plural](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/l10n-singular-plural) string based on the specified resource object and formats the string based on the **args** parameter. This API returns the result synchronously.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/43/v3/_kg7S-OiSw6MByWR4zKjvw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062326Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=68B51E7A4E9D266B198709BFC98AE98FA087CE8C66A54490B230ED1650706222)

-   This API is supported since API version 18 and is deprecated since API version 20. You are advised to use [getDoublePluralStringByNameSync](#getdoublepluralstringbynamesync18) or [getDoublePluralStringValueSync](#getdoublepluralstringvaluesync18) instead.
    
-   Strings distinguish between singular and plural forms in all languages except Chinese. For details, see [Language Plural Rules](https://www.unicode.org/cldr/charts/45/supplemental/language_plural_rules.html).
    

**Atomic service API**: This API can be used in atomic services since API version 18.

**System capability**: SystemCapability.Global.ResourceManager

**Model restriction**: This API can be used only in the stage model.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| resource | [Resource](#resource9) | Yes | Resource object. |
| num | number | Yes | Quantity value (a floating point number), used to obtain the corresponding string representation based on the current language's [plural rules](https://www.unicode.org/cldr/charts/45/supplemental/language_plural_rules.html). |
| ...args | Array<string | number> | No | 
Arguments for formatting strings.

Supported value types include %d, %f, %s, %%, %number$d, %number$f, and %number$s.

Note: %% is converted to %. **number** in %number$d indicates the sequence number of the parameter in **args**.

For example, %%d is converted to %d after formatting, and %1$d indicates that the first parameter is used.

 |

**Return value**

| Type | Description |
| :-- | :-- |
| string | Formatted string corresponding to the specified resource object. |

**Error codes**

For details about the error codes, see [Resource Manager Error Codes](../../error-codes/resource-manager-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 9001001 | Invalid resource ID. |
| 9001002 | No matching resource is found based on the resource ID. |
| 9001006 | The resource is referenced cyclically. |
| 9001007 | Failed to format the resource obtained based on the resource ID. |

**Example**

// Resource file path: src/main/resources/base/element/plural.json
{
  "plural": \[
    {
      "name": "format\_test",
      "value": \[
        {
          "quantity": "one",
          "value": "There is %d apple in the %s, the total amount is %f kg."
        },
        {
          "quantity": "other",
          "value": "There are %d apples in the %s, the total amount is %f kg."
        }
      \]
    }
  \]
}

import { resourceManager } from '@kit.LocalizationKit';
import { BusinessError } from '@kit.BasicServicesKit';

let resource: resourceManager.Resource = {
  bundleName: "com.example.myapplication",
  moduleName: "entry",
  id: $r('app.plural.format\_test').id
};

try {
  // If num is 2.1, the single/plural type is other in the English environment.
  // The quantity field in the resource file indicates the single/plural type. Therefore, the string whose quantity is other is obtained.
  let pluralStr = this.context.resourceManager.getDoublePluralStringValueSync(resource, 2.1, 2, "basket", 0.6);
  console.info(\`getDoublePluralStringValueSync, result: ${pluralStr}\`);
  // Print the output result: getIntPluralStringValueSync, result: There are 2 apples in the basket, the total amount is 0.6 kg.
} catch (error) {
  let code = (error as BusinessError).code;
  let message = (error as BusinessError).message;
  console.error(\`getDoublePluralStringValueSync failed, error code: ${code}, message: ${message}.\`);
}

#### \[h2\]getPluralStringValueSync(deprecated)

getPluralStringValueSync(resId: number, num: number): string

Obtains singular/plural strings based on the specified resource ID and quantity. This API returns the result synchronously.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6b/v3/NIHR-z_0SOmM0QrhrA9A9w/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062326Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=3283C37BB9BA3F0E5B93DB652C1E20FD8A1725EC689B58B773039FE0BBA0D334)

Strings distinguish between singular and plural forms in all languages except Chinese. For details, see [Language Plural Rules](https://www.unicode.org/cldr/charts/45/supplemental/language_plural_rules.html).

This API is supported since API version 10 and is deprecated since API version 18. You are advised to use [getIntPluralStringValueSync](#getintpluralstringvaluesync18) instead.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Global.ResourceManager

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| resId | number | Yes | Resource ID. |
| num | number | Yes | Quantity value, which is used to obtain the corresponding string representation based on the current language's plural rules. For details about the plural rules of a language, see [Language Plural Rules](https://www.unicode.org/cldr/charts/45/supplemental/language_plural_rules.html). |

**Return value**

| Type | Description |
| :-- | :-- |
| string | Singular/plural string corresponding to the specified quantity and resource ID. |

**Error codes**

For details about the error codes, see [Resource Manager Error Codes](../../error-codes/resource-manager-error-codes/document.md) and [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | If the input parameter invalid. Possible causes: Incorrect parameter types. |
| 9001001 | Invalid resource ID. |
| 9001002 | No matching resource is found based on the resource ID. |
| 9001006 | The resource is referenced cyclically. |

**Example**

// Resource file path: src/main/resources/base/element/plural.json
{
  "plural": \[
    {
      "name": "test",
      "value": \[
        {
          "quantity": "one",
          "value": "%d apple"
        },
        {
          "quantity": "other",
          "value": "%d apples"
        }
      \]
    }
  \]
}

import { BusinessError } from '@kit.BasicServicesKit';

try {
  // If num is 1, the single/plural type is one in the English environment.
  // The quantity field in the resource file indicates the single/plural type. Therefore, the string whose quantity is one is obtained.
  let pluralValue = this.context.resourceManager.getPluralStringValueSync($r('app.plural.test').id, 1);
  console.info(\`getPluralStringValueSync, result: ${pluralValue}\`);
  // Print the output result: getPluralStringValueSync, result: 1 apple
} catch (error) {
  let code = (error as BusinessError).code;
  let message = (error as BusinessError).message;
  console.error(\`getPluralStringValueSync failed, error code: ${code}, message: ${message}.\`);
}

#### \[h2\]getPluralStringValueSync(deprecated)

getPluralStringValueSync(resource: Resource, num: number): string

Obtains singular/plural strings based on the specified quantity and resource object. This API returns the result synchronously.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/58/v3/aM9Jv5I_RWqerzPyn4s6NA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062326Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=63554D1C93671F1A442CBBC7AB77363E53EC708F7CE62ED19A6D2B2985E52A5D)

Strings distinguish between singular and plural forms in all languages except Chinese. For details, see [Language Plural Rules](https://www.unicode.org/cldr/charts/45/supplemental/language_plural_rules.html).

This API is supported since API version 10 and deprecated since API version 18. You are advised to use [getIntPluralStringValueSync](#getintpluralstringvaluesync18) or [getIntPluralStringByNameSync](#getintpluralstringbynamesync18) instead.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Global.ResourceManager

**Model restriction**: This API can be used only in the stage model.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| resource | [Resource](#resource9) | Yes | Resource object. |
| num | number | Yes | Quantity value, which is used to obtain the corresponding string representation based on the current language's plural rules. For details about the plural rules of a language, see [Language Plural Rules](https://www.unicode.org/cldr/charts/45/supplemental/language_plural_rules.html). |

**Return value**

| Type | Description |
| :-- | :-- |
| string | Singular/plural string corresponding to the specified quantity and resource object. |

**Error codes**

For details about the error codes, see [Resource Manager Error Codes](../../error-codes/resource-manager-error-codes/document.md) and [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | If the input parameter invalid. Possible causes: Incorrect parameter types. |
| 9001001 | Invalid resource ID. |
| 9001002 | No matching resource is found based on the resource ID. |
| 9001006 | The resource is referenced cyclically. |

**Example**

// Resource file path: src/main/resources/base/element/plural.json
{
  "plural": \[
    {
      "name": "test",
      "value": \[
        {
          "quantity": "one",
          "value": "%d apple"
        },
        {
          "quantity": "other",
          "value": "%d apples"
        }
      \]
    }
  \]
}

import { resourceManager } from '@kit.LocalizationKit';
import { BusinessError } from '@kit.BasicServicesKit';

let resource: resourceManager.Resource = {
  bundleName: "com.example.myapplication",
  moduleName: "entry",
  id: $r('app.plural.test').id
};
try {
  // If num is 1, the single/plural type is one in the English environment.
  // The quantity field in the resource file indicates the single/plural type. Therefore, the string whose quantity is one is obtained.
  let pluralValue = this.context.resourceManager.getPluralStringValueSync(resource, 1);
  console.info(\`getPluralStringValueSync, result: ${pluralValue}\`);
  // Print the output result: getPluralStringValueSync, result: 1 apple
} catch (error) {
  let code = (error as BusinessError).code;
  let message = (error as BusinessError).message;
  console.error(\`getPluralStringValueSync failed, error code: ${code}, message: ${message}.\`);
}

#### \[h2\]getPluralStringByNameSync(deprecated)

getPluralStringByNameSync(resName: string, num: number): string

Obtains singular/plural strings based on the specified quantity and resource name. This API returns the result synchronously.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7e/v3/UppsT6OHQWK4rmNuarzRVA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062326Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=58A7249A5670826FBD3415E3EDB29B50041CD0D2F6F17D41BC2C6C07BB12C90A)

Strings distinguish between singular and plural forms in all languages except Chinese. For details, see [Language Plural Rules](https://www.unicode.org/cldr/charts/45/supplemental/language_plural_rules.html).

This API is supported since API version 10 and is deprecated since API version 18. You are advised to use [getIntPluralStringByNameSync](#getintpluralstringbynamesync18) instead.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Global.ResourceManager

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| resName | string | Yes | Resource name. |
| num | number | Yes | Quantity value, which is used to obtain the corresponding string representation based on the current language's plural rules. For details about the plural rules of a language, see [Language Plural Rules](https://www.unicode.org/cldr/charts/45/supplemental/language_plural_rules.html). |

**Return value**

| Type | Description |
| :-- | :-- |
| string | Singular/plural string corresponding to the specified quantity and resource name. |

**Error codes**

For details about the error codes, see [Resource Manager Error Codes](../../error-codes/resource-manager-error-codes/document.md) and [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | If the input parameter invalid. Possible causes: Incorrect parameter types. |
| 9001003 | Invalid resource name. |
| 9001004 | No matching resource is found based on the resource name. |
| 9001006 | The resource is referenced cyclically. |

**Example**

// Resource file path: src/main/resources/base/element/plural.json
{
  "plural": \[
    {
      "name": "test",
      "value": \[
        {
          "quantity": "one",
          "value": "%d apple"
        },
        {
          "quantity": "other",
          "value": "%d apples"
        }
      \]
    }
  \]
}

import { BusinessError } from '@kit.BasicServicesKit';

try {
  // If num is 1, the single/plural type is one in the English environment.
  // The quantity field in the resource file indicates the single/plural type. Therefore, the string whose quantity is one is obtained.
  let pluralValue = this.context.resourceManager.getPluralStringByNameSync("test", 1);
  console.info(\`getPluralStringByNameSync, result: ${pluralValue}\`);
  // Print the output result: getPluralStringByNameSync, result: 1 apple
} catch (error) {
  let code = (error as BusinessError).code;
  let message = (error as BusinessError).message;
  console.error(\`getPluralStringByNameSync failed, error code: ${code}, message: ${message}.\`);
}

#### \[h2\]getPluralStringValue(deprecated)

getPluralStringValue(resId: number, num: number, callback: \_AsyncCallback<string>): void

Obtains singular/plural strings based on the specified quantity and resource ID. This API uses an asynchronous callback to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/52/v3/ID5YZioZS5OyV_UnLoXn5g/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062326Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=4A23611E19F8E9E1F8218720D282978EE3698A560A253A8488B2E42EF404A41D)

Strings distinguish between singular and plural forms in all languages except Chinese. For details, see [Language Plural Rules](https://www.unicode.org/cldr/charts/45/supplemental/language_plural_rules.html).

This API is supported since API version 9 and is deprecated since API version 18. You are advised to use [getIntPluralStringValueSync](#getintpluralstringvaluesync18) instead.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Global.ResourceManager

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| resId | number | Yes | Resource ID. |
| num | number | Yes | Quantity value, which is used to obtain the corresponding string representation based on the current language's plural rules. For details about the plural rules of a language, see [Language Plural Rules](https://www.unicode.org/cldr/charts/45/supplemental/language_plural_rules.html). |
| callback | [\_AsyncCallback](../../../../system/basic-functions/basic-services-kit/arkts-apis/others/ohos-base-public-callback-information/document.md#asynccallback)<string> | Yes | Callback used to return the obtained singular/plural string. |

**Error codes**

For details about the error codes, see [Resource Manager Error Codes](../../error-codes/resource-manager-error-codes/document.md) and [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | If the input parameter invalid. Possible causes: Incorrect parameter types. |
| 9001001 | Invalid resource ID. |
| 9001002 | No matching resource is found based on the resource ID. |
| 9001006 | The resource is referenced cyclically. |

**Example**

// Resource file path: src/main/resources/base/element/plural.json
{
  "plural": \[
    {
      "name": "test",
      "value": \[
        {
          "quantity": "one",
          "value": "%d apple"
        },
        {
          "quantity": "other",
          "value": "%d apples"
        }
      \]
    }
  \]
}

import { BusinessError } from '@kit.BasicServicesKit';

// If num is 1, the single/plural type is one in the English environment.
// The quantity field in the resource file indicates the single/plural type. Therefore, the string whose quantity is one is obtained.
this.context.resourceManager.getPluralStringValue($r("app.plural.test").id, 1,
  (error: BusinessError, value: string) => {
    if (error != null) {
      console.error(\`callback getPluralStringValue failed, error code: ${error.code}, message: ${error.message}.\`);
    } else {
      console.info(\`getPluralStringValue, result: ${value}\`);
      // Print the output result: getPluralStringValue, result: 1 apple
    }
  });

#### \[h2\]getPluralStringValue(deprecated)

getPluralStringValue(resId: number, num: number): Promise<string>

Obtains singular/plural strings based on the specified quantity and resource ID. This API uses a promise to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e7/v3/4UCXyCeuRPuthMb-1R7ryg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062326Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=C682D57E1D23A4DF89AFC2C122398CE1A2AAA0E3F4F79B5456C720E9C822DF72)

Strings distinguish between singular and plural forms in all languages except Chinese. For details, see [Language Plural Rules](https://www.unicode.org/cldr/charts/45/supplemental/language_plural_rules.html).

This API is supported since API version 9 and is deprecated since API version 18. You are advised to use [getIntPluralStringValueSync](#getintpluralstringvaluesync18) instead.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Global.ResourceManager

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| resId | number | Yes | Resource ID. |
| num | number | Yes | Quantity value, which is used to obtain the corresponding string representation based on the current language's plural rules. For details about the plural rules of a language, see [Language Plural Rules](https://www.unicode.org/cldr/charts/45/supplemental/language_plural_rules.html). |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<string> | Promise used to return the obtained singular/plural string. |

**Error codes**

For details about the error codes, see [Resource Manager Error Codes](../../error-codes/resource-manager-error-codes/document.md) and [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | If the input parameter invalid. Possible causes: Incorrect parameter types. |
| 9001001 | Invalid resource ID. |
| 9001002 | No matching resource is found based on the resource ID. |
| 9001006 | The resource is referenced cyclically. |

**Example**

// Resource file path: src/main/resources/base/element/plural.json
{
  "plural": \[
    {
      "name": "test",
      "value": \[
        {
          "quantity": "one",
          "value": "%d apple"
        },
        {
          "quantity": "other",
          "value": "%d apples"
        }
      \]
    }
  \]
}

import { BusinessError } from '@kit.BasicServicesKit';

// If num is 1, the single/plural type is one in the English environment.
// The quantity field in the resource file indicates the single/plural type. Therefore, the string whose quantity is one is obtained.
this.context.resourceManager.getPluralStringValue($r("app.plural.test").id, 1)
  .then((value: string) => {
    console.info(\`getPluralStringValue, result: ${value}\`);
    // Print the output result: getPluralStringValue, result: 1 apple
  })
  .catch((error: BusinessError) => {
    console.error(\`promise getPluralStringValue failed, error code: ${error.code}, message: ${error.message}.\`);
  });

#### \[h2\]getPluralStringValue(deprecated)

getPluralStringValue(resource: Resource, num: number, callback: \_AsyncCallback<string>): void

Obtains singular/plural strings based on the specified quantity and resource object. This API uses an asynchronous callback to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e4/v3/nqY_T4c7Q7G7t_Z9_Plk0g/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062326Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=75C6758F9AFE9874986DF30A9868A7A16540F1E8778BE10D978612300F9F75F3)

Strings distinguish between singular and plural forms in all languages except Chinese. For details, see [Language Plural Rules](https://www.unicode.org/cldr/charts/45/supplemental/language_plural_rules.html).

This API is supported since API version 9 and deprecated since API version 18. You are advised to use [getIntPluralStringValueSync](#getintpluralstringvaluesync18) or [getIntPluralStringByNameSync](#getintpluralstringbynamesync18) instead.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Global.ResourceManager

**Model restriction**: This API can be used only in the stage model.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| resource | [Resource](#resource9) | Yes | Resource object. |
| num | number | Yes | Quantity value, which is used to obtain the corresponding string representation based on the current language's plural rules. For details about the plural rules of a language, see [Language Plural Rules](https://www.unicode.org/cldr/charts/45/supplemental/language_plural_rules.html). |
| callback | [\_AsyncCallback](../../../../system/basic-functions/basic-services-kit/arkts-apis/others/ohos-base-public-callback-information/document.md#asynccallback)<string> | Yes | Callback used to return the obtained singular/plural string. |

**Error codes**

For details about the error codes, see [Resource Manager Error Codes](../../error-codes/resource-manager-error-codes/document.md) and [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | If the input parameter invalid. Possible causes: Incorrect parameter types. |
| 9001001 | Invalid resource ID. |
| 9001002 | No matching resource is found based on the resource ID. |
| 9001006 | The resource is referenced cyclically. |

**Example**

// Resource file path: src/main/resources/base/element/plural.json
{
  "plural": \[
    {
      "name": "test",
      "value": \[
        {
          "quantity": "one",
          "value": "%d apple"
        },
        {
          "quantity": "other",
          "value": "%d apples"
        }
      \]
    }
  \]
}

import { resourceManager } from '@kit.LocalizationKit';
import { BusinessError } from '@kit.BasicServicesKit';

let resource: resourceManager.Resource = {
  bundleName: "com.example.myapplication",
  moduleName: "entry",
  id: $r('app.plural.test').id
};
// If num is 1, the single/plural type is one in the English environment.
// The quantity field in the resource file indicates the single/plural type. Therefore, the string whose quantity is one is obtained.
this.context.resourceManager.getPluralStringValue(resource, 1,
  (error: BusinessError, value: string) => {
    if (error != null) {
      console.error(\`callback getPluralStringValue failed, error code: ${error.code}, message: ${error.message}.\`);
    } else {
      console.info(\`getPluralStringValue, result: ${value}\`);
      // Print the output result: getPluralStringValue, result: 1 apple
    }
  });

#### \[h2\]getPluralStringValue(deprecated)

getPluralStringValue(resource: Resource, num: number): Promise<string>

Obtains singular/plural strings based on the specified quantity and resource object. This API uses a promise to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b9/v3/YYrE6lwJT62aR0nK9vWJFg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062326Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=CEC787DA6EB2AD084B50395DD4B8B2CD2836C31152911657B487EF5BA14E2D10)

Strings distinguish between singular and plural forms in all languages except Chinese. For details, see [Language Plural Rules](https://www.unicode.org/cldr/charts/45/supplemental/language_plural_rules.html).

This API is supported since API version 9 and deprecated since API version 18. You are advised to use [getIntPluralStringValueSync](#getintpluralstringvaluesync18) or [getIntPluralStringByNameSync](#getintpluralstringbynamesync18) instead.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Global.ResourceManager

**Model restriction**: This API can be used only in the stage model.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| resource | [Resource](#resource9) | Yes | Resource object. |
| num | number | Yes | Quantity value, which is used to obtain the corresponding string representation based on the current language's plural rules. For details about the plural rules of a language, see [Language Plural Rules](https://www.unicode.org/cldr/charts/45/supplemental/language_plural_rules.html). |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<string> | Promise used to return the obtained singular/plural string. |

**Error codes**

For details about the error codes, see [Resource Manager Error Codes](../../error-codes/resource-manager-error-codes/document.md) and [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | If the input parameter invalid. Possible causes: Incorrect parameter types. |
| 9001001 | Invalid resource ID. |
| 9001002 | No matching resource is found based on the resource ID. |
| 9001006 | The resource is referenced cyclically. |

**Example**

// Resource file path: src/main/resources/base/element/plural.json
{
  "plural": \[
    {
      "name": "test",
      "value": \[
        {
          "quantity": "one",
          "value": "%d apple"
        },
        {
          "quantity": "other",
          "value": "%d apples"
        }
      \]
    }
  \]
}

import { resourceManager } from '@kit.LocalizationKit';
import { BusinessError } from '@kit.BasicServicesKit';

let resource: resourceManager.Resource = {
  bundleName: "com.example.myapplication",
  moduleName: "entry",
  id: $r('app.plural.test').id
};
// If num is 1, the single/plural type is one in the English environment.
// The quantity field in the resource file indicates the single/plural type. Therefore, the string whose quantity is one is obtained.
this.context.resourceManager.getPluralStringValue(resource, 1)
  .then((value: string) => {
    console.info(\`getPluralStringValue, result: ${value}\`);
    // Print the output result: getPluralStringValue, result: 1 apple
  })
  .catch((error: BusinessError) => {
    console.error(\`promise getPluralStringValue failed, error code: ${error.code}, message: ${error.message}.\`);
  });

#### \[h2\]getPluralStringByName(deprecated)

getPluralStringByName(resName: string, num: number, callback: \_AsyncCallback<string>): void

Obtains singular/plural strings based on the specified quantity and resource name. This API uses an asynchronous callback to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/47/v3/EKSetU5qTX2W8bpdxt5GTQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062326Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=6D9D6E2622D12B1AB5A8CF3A7BB7BCF3D2A446CE7D7AF8A7C096633DD101A4C6)

Strings distinguish between singular and plural forms in all languages except Chinese. For details, see [Language Plural Rules](https://www.unicode.org/cldr/charts/45/supplemental/language_plural_rules.html).

This API is supported since API version 9 and is deprecated since API version 18. You are advised to use [getIntPluralStringByNameSync](#getintpluralstringbynamesync18) instead.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Global.ResourceManager

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| resName | string | Yes | Resource name. |
| num | number | Yes | Quantity value, which is used to obtain the corresponding string representation based on the current language's plural rules. For details about the plural rules of a language, see [Language Plural Rules](https://www.unicode.org/cldr/charts/45/supplemental/language_plural_rules.html). |
| callback | [\_AsyncCallback](../../../../system/basic-functions/basic-services-kit/arkts-apis/others/ohos-base-public-callback-information/document.md#asynccallback)<string> | Yes | Callback used to return the obtained singular/plural string. |

**Error codes**

For details about the error codes, see [Resource Manager Error Codes](../../error-codes/resource-manager-error-codes/document.md) and [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | If the input parameter invalid. Possible causes: Incorrect parameter types. |
| 9001003 | Invalid resource name. |
| 9001004 | No matching resource is found based on the resource name. |
| 9001006 | The resource is referenced cyclically. |

**Example**

// Resource file path: src/main/resources/base/element/plural.json
{
  "plural": \[
    {
      "name": "test",
      "value": \[
        {
          "quantity": "one",
          "value": "%d apple"
        },
        {
          "quantity": "other",
          "value": "%d apples"
        }
      \]
    }
  \]
}

import { BusinessError } from '@kit.BasicServicesKit';

// If num is 1, the single/plural type is one in the English environment.
// The quantity field in the resource file indicates the single/plural type. Therefore, the string whose quantity is one is obtained.
this.context.resourceManager.getPluralStringByName("test", 1, (error: BusinessError, value: string) => {
  if (error != null) {
    console.error(\`callback getPluralStringByName failed, error code: ${error.code}, message: ${error.message}.\`);
  } else {
    console.info(\`getPluralStringByName, result: ${value}\`);
    // Print the output result: getPluralStringByName, result: 1 apple
  }
});

#### \[h2\]getPluralStringByName(deprecated)

getPluralStringByName(resName: string, num: number): Promise<string>

Obtains singular/plural strings based on the specified quantity and resource name. This API uses a promise to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8b/v3/RpN4-R4yRliHQvCh_vO2AA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062326Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=1A14546540193443C9585DE5F61AAD820C9FE5186F1FAA3F694D4924D188AD41)

Strings distinguish between singular and plural forms in all languages except Chinese. For details, see [Language Plural Rules](https://www.unicode.org/cldr/charts/45/supplemental/language_plural_rules.html).

This API is supported since API version 9 and is deprecated since API version 18. You are advised to use [getIntPluralStringByNameSync](#getintpluralstringbynamesync18) instead.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Global.ResourceManager

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| resName | string | Yes | Resource name. |
| num | number | Yes | Quantity value, which is used to obtain the corresponding string representation based on the current language's plural rules. For details about the plural rules of a language, see [Language Plural Rules](https://www.unicode.org/cldr/charts/45/supplemental/language_plural_rules.html). |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<string> | Promise used to return the result, which is the singular/plural string corresponding to the specified resource name. |

**Error codes**

For details about the error codes, see [Resource Manager Error Codes](../../error-codes/resource-manager-error-codes/document.md) and [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | If the input parameter invalid. Possible causes: Incorrect parameter types. |
| 9001003 | Invalid resource name. |
| 9001004 | No matching resource is found based on the resource name. |
| 9001006 | The resource is referenced cyclically. |

**Example**

// Resource file path: src/main/resources/base/element/plural.json
{
  "plural": \[
    {
      "name": "test",
      "value": \[
        {
          "quantity": "one",
          "value": "%d apple"
        },
        {
          "quantity": "other",
          "value": "%d apples"
        }
      \]
    }
  \]
}

import { BusinessError } from '@kit.BasicServicesKit';

// If num is 1, the single/plural type is one in the English environment.
// The quantity field in the resource file indicates the single/plural type. Therefore, the string whose quantity is one is obtained.
this.context.resourceManager.getPluralStringByName("test", 1)
  .then((value: string) => {
    console.info(\`getPluralStringByName, result: ${value}\`);
    // Print the output result: getPluralStringByName, result: 1 apple
  })
  .catch((error: BusinessError) => {
    console.error(\`promise getPluralStringByName failed, error code: ${error.code}, message: ${error.message}.\`);
  });

#### \[h2\]getPluralString(deprecated)

getPluralString(resId: number, num: number): Promise<string>

Obtains singular/plural strings based on the specified quantity and resource ID. This API uses a promise to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a9/v3/moRxd-FMQ76oixo4jn7BXg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062326Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=9E64E14306145F22009082250FE816B4F5EA468016EE4A43DA2612BEBAC547B0)

Strings distinguish between singular and plural forms in all languages except Chinese. For details, see [Language Plural Rules](https://www.unicode.org/cldr/charts/45/supplemental/language_plural_rules.html).

This API is supported since API version 6 and deprecated since API version 9. You are advised to use [getPluralStringValue](#getpluralstringvaluedeprecated-1) instead.

**System capability**: SystemCapability.Global.ResourceManager

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| resId | number | Yes | Resource ID. |
| num | number | Yes | Quantity value, which is used to obtain the corresponding string representation based on the current language's plural rules. For details about the plural rules of a language, see [Language Plural Rules](https://www.unicode.org/cldr/charts/45/supplemental/language_plural_rules.html). |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<string> | Promise used to return the obtained singular/plural string. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

resourceManager.getResourceManager((error, mgr) => {
    mgr.getPluralString($r("app.plural.test").id, 1).then((value: string) => {
        let str = value;
    }).catch((error: BusinessError) => {
        console.error("getPluralString promise error is " + error);
    });
});

#### \[h2\]getPluralString(deprecated)

getPluralString(resId: number, num: number, callback: AsyncCallback<string>): void

Obtains singular/plural strings based on the specified quantity and resource ID. This API uses an asynchronous callback to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1b/v3/wpqMGQRNQ7aJblUZZRhZOg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062326Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=9ADD5B06FEB4CA185807DEBDAC3226E67EBA635AC9A76A54C7D330D34134648C)

Strings distinguish between singular and plural forms in all languages except Chinese. For details, see [Language Plural Rules](https://www.unicode.org/cldr/charts/45/supplemental/language_plural_rules.html).

This API is supported since API version 6 and deprecated since API version 9. You are advised to use [getPluralStringValue](#getpluralstringvaluedeprecated) instead.

**System capability**: SystemCapability.Global.ResourceManager

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| resId | number | Yes | Resource ID. |
| num | number | Yes | Quantity value, which is used to obtain the corresponding string representation based on the current language's plural rules. For details about the plural rules of a language, see [Language Plural Rules](https://www.unicode.org/cldr/charts/45/supplemental/language_plural_rules.html). |
| callback | [AsyncCallback](#asynccallbackdeprecated)<string> | Yes | Callback used to return the obtained singular/plural string. |

**Example**

import { resourceManager } from '@kit.LocalizationKit';

resourceManager.getResourceManager((error, mgr) => {
    mgr.getPluralString($r("app.plural.test").id, 1, (error: Error, value: string) => {
        if (error != null) {
            console.error("error is " + error);
        } else {
            let str = value;
        }
    });
});

#### \[h2\]getBoolean(deprecated)

getBoolean(resource: Resource): boolean

Obtains a Boolean value based on the specified resource object. This API returns the result synchronously.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b0/v3/PVKr93aHQOys3iWDgZf3pw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062326Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=1EFEFD12931B96EA5A70865E448BDCDCD0C21A6B017D7E6AB0428A463E2336FE)

This API is supported since API version 9 and is deprecated since API version 20. You are advised to use [getBooleanByName](#getbooleanbyname9) or [getBoolean](#getboolean9) instead.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Global.ResourceManager

**Model restriction**: This API can be used only in the stage model.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| resource | [Resource](#resource9) | Yes | Resource object. |

**Return value**

| Type | Description |
| :-- | :-- |
| boolean | Boolean value. |

**Error codes**

For details about the error codes, see [Resource Manager Error Codes](../../error-codes/resource-manager-error-codes/document.md) and [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | If the input parameter invalid. Possible causes: Incorrect parameter types. |
| 9001001 | Invalid resource ID. |
| 9001002 | No matching resource is found based on the resource ID. |
| 9001006 | The resource is referenced cyclically. |

**Example**

// Resource file path: src/main/resources/base/element/boolean.json
{
  "boolean": \[
    {
      "name": "boolean\_test",
      "value": true
    }
  \]
}

import { resourceManager } from '@kit.LocalizationKit';
import { BusinessError } from '@kit.BasicServicesKit';

let resource: resourceManager.Resource = {
  bundleName: "com.example.myapplication",
  moduleName: "entry",
  id: $r('app.boolean.boolean\_test').id
};
try {
  let boolTest = this.context.resourceManager.getBoolean(resource);
  console.info(\`getBoolean, result: ${boolTest}\`);
  // Print the output result: getBoolean, result: true
} catch (error) {
  let code = (error as BusinessError).code;
  let message = (error as BusinessError).message;
  console.error(\`getBoolean failed, error code: ${code}, message: ${message}.\`);
}

#### \[h2\]getNumber(deprecated)

getNumber(resource: Resource): number

Obtains an integer or float number based on the specified resource object. This API returns the result synchronously.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/37/v3/lYBbijmoTnOsBjUE8Rc_fA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062326Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=C49245E5D4E4E618C4FF5E3DD6263DD07FFF6D74B23AAB2EF9E072476606E914)

This API is supported since API version 9 and is deprecated since API version 20. You are advised to use [getNumberByName](#getnumberbyname9) or [getNumber](#getnumber9) instead.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Global.ResourceManager

**Model restriction**: This API can be used only in the stage model.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| resource | [Resource](#resource9) | Yes | Resource object. |

**Return value**

| Type | Description |
| :-- | :-- |
| number | 
Integer or float number.

An integer indicates the original value, and a float number without a unit indicates the original value and a float number with the unit of vp or fp indicates the px value.

 |

**Error codes**

For details about the error codes, see [Resource Manager Error Codes](../../error-codes/resource-manager-error-codes/document.md) and [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | If the input parameter invalid. Possible causes: Incorrect parameter types. |
| 9001001 | Invalid resource ID. |
| 9001002 | No matching resource is found based on the resource ID. |
| 9001006 | The resource is referenced cyclically. |

**Example**

// Resource file path: src/main/resources/base/element/integer.json
{
  "integer": \[
    {
      "name": "integer\_test",
      "value": 100
    }
  \]
}

import { resourceManager } from '@kit.LocalizationKit';
import { BusinessError } from '@kit.BasicServicesKit';

let resource: resourceManager.Resource = {
  bundleName: "com.example.myapplication",
  moduleName: "entry",
  id: $r('app.integer.integer\_test').id
};

try {
  let intValue = this.context.resourceManager.getNumber(resource);
  console.info(\`getNumber, int value: ${intValue}\`);
  // Print the output result: getNumber, int value: 100
} catch (error) {
  let code = (error as BusinessError).code;
  let message = (error as BusinessError).message;
  console.error(\`getNumber failed, error code: ${code}, message: ${message}.\`);
}

#### \[h2\]getColorSync(deprecated)

getColorSync(resource: Resource): number

Obtains a color value based on the specified resource object. This API returns the result synchronously.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a9/v3/Y3_kbeAQSC-n8sKBVC6NYA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062326Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=916AA842E8684153A599775201B3E40C0DD31D9F250CD8EC923B44DD96E3E9D3)

This API is supported since API version 10 and is deprecated since API version 20. You are advised to use [getColorByNameSync](#getcolorbynamesync10) or [getColorSync](#getcolorsync10) instead.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Global.ResourceManager

**Model restriction**: This API can be used only in the stage model.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| resource | [Resource](#resource9) | Yes | Resource object. |

**Return value**

| Type | Description |
| :-- | :-- |
| number | Color value (decimal) corresponding to the specified resource object. |

**Error codes**

For details about the error codes, see [Resource Manager Error Codes](../../error-codes/resource-manager-error-codes/document.md) and [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | If the input parameter invalid. Possible causes: Incorrect parameter types. |
| 9001001 | Invalid resource ID. |
| 9001002 | No matching resource is found based on the resource ID. |
| 9001006 | The resource is referenced cyclically. |

**Example**

// Resource file path: src/main/resources/base/element/color.json
{
  "color": \[
    {
      "name": "test",
      "value": "#FFFFFF"
    }
  \]
}

import { resourceManager } from '@kit.LocalizationKit';
import { BusinessError } from '@kit.BasicServicesKit';

let resource: resourceManager.Resource = {
  bundleName: "com.example.myapplication",
  moduleName: "entry",
  id: $r('app.color.test').id
};
try {
  let colorValue = this.context.resourceManager.getColorSync(resource);
  console.info(\`getColorSync, result: ${colorValue}\`);
  // Print the output result: getColorSync, result: 4294967295
} catch (error) {
  let code = (error as BusinessError).code;
  let message = (error as BusinessError).message;
  console.error(\`getColorSync failed, error code: ${code}, message: ${message}.\`);
}

#### \[h2\]getColor(deprecated)

getColor(resource: Resource, callback: \_AsyncCallback<number>): void

Obtains a color value based on the specified resource object. This API uses an asynchronous callback to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/66/v3/drfgv3oSTyyq8RT5RF5aig/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062326Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=BD49165229141A4D57EC1ACEBE26587B4FE288432A7BEBE29144674A5220C256)

This API is supported since API version 10 and is deprecated since API version 20. You are advised to use [getColorByName](#getcolorbyname10) or [getColor](#getcolor10) instead.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Global.ResourceManager

**Model restriction**: This API can be used only in the stage model.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| resource | [Resource](#resource9) | Yes | Resource object. |
| callback | [\_AsyncCallback](../../../../system/basic-functions/basic-services-kit/arkts-apis/others/ohos-base-public-callback-information/document.md#asynccallback)<number> | Yes | Callback used to return the color value (decimal). |

**Error codes**

For details about the error codes, see [Resource Manager Error Codes](../../error-codes/resource-manager-error-codes/document.md) and [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | If the input parameter invalid. Possible causes: Incorrect parameter types. |
| 9001001 | Invalid resource ID. |
| 9001002 | No matching resource is found based on the resource ID. |
| 9001006 | The resource is referenced cyclically. |

**Example**

// Resource file path: src/main/resources/base/element/color.json
{
  "color": \[
    {
      "name": "test",
      "value": "#FFFFFF"
    }
  \]
}

import { resourceManager } from '@kit.LocalizationKit';
import { BusinessError } from '@kit.BasicServicesKit';

let resource: resourceManager.Resource = {
  bundleName: "com.example.myapplication",
  moduleName: "entry",
  id: $r('app.color.test').id
};
this.context.resourceManager.getColor(resource, (error: BusinessError, value: number) => {
  if (error != null) {
    console.error(\`callback getColor failed, error code: ${error.code}, message: ${error.message}.\`);
  } else {
    console.info(\`getColor, result: ${value}\`);
    // Print the output result: getColor, result: 4294967295
  }
});

#### \[h2\]getColor(deprecated)

getColor(resource: Resource): Promise<number>

Obtains a color value based on the specified resource object. This API uses a promise to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3a/v3/ZvQnLz06QAmGKD1qQsWs5A/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062326Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=49D64948806EB4675634E8FB4BACFC203D2573DD8E415903693AE6A2D11E9D74)

This API is supported since API version 10 and is deprecated since API version 20. You are advised to use \[getColorByName\] (#getcolorbyname10-1) or \[getColor\] (#getcolor10-1) instead.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Global.ResourceManager

**Model restriction**: This API can be used only in the stage model.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| resource | [Resource](#resource9) | Yes | Resource object. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<number> | Promise used to return the color value (decimal). |

**Error codes**

For details about the error codes, see [Resource Manager Error Codes](../../error-codes/resource-manager-error-codes/document.md) and [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | If the input parameter invalid. Possible causes: Incorrect parameter types. |
| 9001001 | Invalid resource ID. |
| 9001002 | No matching resource is found based on the resource ID. |
| 9001006 | The resource is referenced cyclically. |

**Example**

// Resource file path: src/main/resources/base/element/color.json
{
  "color": \[
    {
      "name": "test",
      "value": "#FFFFFF"
    }
  \]
}

import { resourceManager } from '@kit.LocalizationKit';
import { BusinessError } from '@kit.BasicServicesKit';

let resource: resourceManager.Resource = {
  bundleName: "com.example.myapplication",
  moduleName: "entry",
  id: $r('app.color.test').id
};
this.context.resourceManager.getColor(resource)
  .then((value: number) => {
    console.info(\`getColor, result: ${value}\`);
    // Print the output result: getColor, result: 4294967295
  })
  .catch((error: BusinessError) => {
    console.error(\`promise getColor failed, error code: ${error.code}, message: ${error.message}.\`);
  });

#### \[h2\]getSymbol(deprecated)

getSymbol(resource: Resource): number

Obtains the Unicode of a [symbol](https://developer.huawei.com/consumer/en/design/harmonyos-symbol) based on the specified resource object. This API returns the result synchronously.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/07/v3/GaCOBd6IQoi-H8aChRfLOw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062326Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=7CB8F0AEE5337E6577ADF2C6F1870DBD9037D106026772E035D473C6778EBC20)

This API is supported since API version 11 and is deprecated since API version 20. You are advised to use [getSymbolByName](#getsymbolbyname11) or [getSymbol](#getsymbol11) instead.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Global.ResourceManager

**Model restriction**: This API can be used only in the stage model.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| resource | [Resource](#resource9) | Yes | Resource object. |

**Return value**

| Type | Description |
| :-- | :-- |
| number | Unicode code (decimal) of the symbol. |

**Error codes**

For details about the error codes, see [Resource Manager Error Codes](../../error-codes/resource-manager-error-codes/document.md) and [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | If the input parameter invalid. Possible causes: Incorrect parameter types. |
| 9001001 | Invalid resource ID. |
| 9001002 | No matching resource is found based on the resource ID. |
| 9001006 | The resource is referenced cyclically. |

**Example**

import { resourceManager } from '@kit.LocalizationKit';
import { BusinessError } from '@kit.BasicServicesKit';

let resource: resourceManager.Resource = {
  bundleName: "com.example.myapplication",
  moduleName: "entry",
  id: $r('sys.symbol.message').id
};
try {
  let symbolValue = this.context.resourceManager.getSymbol(resource);
  console.info(\`getSymbol, result: ${symbolValue}\`);
  // Print the output result: getSymbol, result: 983183
} catch (error) {
  let code = (error as BusinessError).code;
  let message = (error as BusinessError).message;
  console.error(\`getSymbol failed, error code: ${code}, message: ${message}.\`);
}

#### \[h2\]getRawFile(deprecated)

getRawFile(path: string, callback: AsyncCallback<Uint8Array>): void

Obtains the content of a rawfile in the **resources/rawfile** directory. This API uses an asynchronous callback to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2b/v3/K5xPe78QSjGRdDUEDPIw_Q/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062326Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=304FC60CFB6E1B70B87A2F478370F35540CF57F40A87BED238ACF33B9E795BD1)

This API is supported since API version 8 and is deprecated since API version 9. You are advised to use [getRawFileContent](#getrawfilecontent9) instead.

**System capability**: SystemCapability.Global.ResourceManager

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| path | string | Yes | Path of the rawfile. |
| callback | [AsyncCallback](#asynccallbackdeprecated)<Uint8Array> | Yes | Callback used to return the rawfile content. |

**Example**

import { resourceManager } from '@kit.LocalizationKit';

resourceManager.getResourceManager((error, mgr) => {
    mgr.getRawFile("test.txt", (error: Error, value: Uint8Array) => {
        if (error != null) {
            console.error("error is " + error);
        } else {
            let rawFile = value;
        }
    });
});

#### \[h2\]getRawFile(deprecated)

getRawFile(path: string): Promise<Uint8Array>

Obtains the content of a rawfile in the **resources/rawfile** directory. This API uses a promise to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/af/v3/LlaYuqJMR52ZoFD4g1ooEA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062326Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=893C32CBA7A61866DE5563219BF2F6340E09B34A296298C51F083EFD965C5718)

This API is supported since API version 8 and is deprecated since API version 9. You are advised to use [getRawFileContent](#getrawfilecontent9-1) instead.

**System capability**: SystemCapability.Global.ResourceManager

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| path | string | Yes | Path of the rawfile. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<Uint8Array> | Promise used to return the rawfile content. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

resourceManager.getResourceManager((error, mgr) => {
    mgr.getRawFile("test.txt").then((value: Uint8Array) => {
        let rawFile = value;
    }).catch((error: BusinessError) => {
        console.error("getRawFile promise error is " + error);
    });
});

#### \[h2\]getRawFileDescriptor(deprecated)

getRawFileDescriptor(path: string, callback: AsyncCallback<RawFileDescriptor>): void

Obtains the fd of the rawfile in the **resources/rawfile** directory. This API uses an asynchronous callback to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e9/v3/Aphe27_ASqiL7dp4gCzwvA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062326Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=E6485D7EBDE9F71F73BE98523077BCF7B15581FE6EC520E38D33FB41FAB2998A)

This API is supported since API version 8 and is deprecated since API version 9. You are advised to use [getRawFd](#getrawfd9) instead.

**System capability**: SystemCapability.Global.ResourceManager

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| path | string | Yes | Path of the rawfile. |
| callback | [AsyncCallback](#asynccallbackdeprecated)<[RawFileDescriptor](#rawfiledescriptor9)\> | Yes | Callback used to return the obtained fd. |

**Example**

import { resourceManager } from '@kit.LocalizationKit';

resourceManager.getResourceManager((error, mgr) => {
    mgr.getRawFileDescriptor("test.txt", (error: Error, value: resourceManager.RawFileDescriptor) => {
        if (error != null) {
            console.error("error is " + error);
        } else {
            let fd = value.fd;
            let offset = value.offset;
            let length = value.length;
        }
    });
});

#### \[h2\]getRawFileDescriptor(deprecated)

getRawFileDescriptor(path: string): Promise<RawFileDescriptor>

Obtains the fd of the rawfile in the **resources/rawfile** directory. This API uses a promise to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ef/v3/BlJdOWNERUCME5JWMicHvw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062326Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=32CD20D667195B5CE2D7EAA780CD3FFB10C5DE08AC7BAD903D49EC09322E594A)

This API is supported since API version 8 and is deprecated since API version 9. You are advised to use [getRawFd](#getrawfd9-1) instead.

**System capability**: SystemCapability.Global.ResourceManager

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| path | string | Yes | Path of the rawfile. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<[RawFileDescriptor](#rawfiledescriptor9)\> | Promise used to return the obtained fd. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

resourceManager.getResourceManager((error, mgr) => {
    mgr.getRawFileDescriptor("test.txt").then((value: resourceManager.RawFileDescriptor) => {
        let fd = value.fd;
        let offset = value.offset;
        let length = value.length;
    }).catch((error: BusinessError) => {
        console.error("getRawFileDescriptor promise error is " + error);
    });
});

#### \[h2\]closeRawFileDescriptor(deprecated)

closeRawFileDescriptor(path: string, callback: AsyncCallback<void>): void

Closes the fd of the rawfile in the **resources/rawfile** directory. This API uses an asynchronous callback to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/05/v3/pC85lJoKT7-rVf9DgrF-Ag/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062326Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=E0577EC9B249D7A73746375D7F117149FEE652BC5FF2CF9E99CBBAD8CB319F5C)

This API is supported since API version 8 and is deprecated since API version 9. You are advised to use [closeRawFd](#closerawfd9) instead.

**System capability**: SystemCapability.Global.ResourceManager

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| path | string | Yes | Path of the rawfile. |
| callback | [AsyncCallback](#asynccallbackdeprecated)<void> | Yes | Callback used to return the result. If the operation is successful, **err** is **undefined**. Otherwise, **err** is an error object. |

**Example**

import { resourceManager } from '@kit.LocalizationKit';

resourceManager.getResourceManager((error, mgr) => {
    mgr.closeRawFileDescriptor("test.txt", (error: Error) => {
        if (error != null) {
            console.error("error is " + error);
        }
    });
});

#### \[h2\]closeRawFileDescriptor(deprecated)

closeRawFileDescriptor(path: string): Promise<void>

Closes the fd of the rawfile in the **resources/rawfile** directory. This API uses a promise to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cd/v3/1lsV2TVpSbibwcS3Y4TZCA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062326Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=0E2E1DB7225BD02734E5D09E96D5A7A21E75CA0B7305B90B3CC42F60614E97E5)

This API is supported since API version 8 and is deprecated since API version 9. You are advised to use [closeRawFd](#closerawfd9-1) instead.

**System capability**: SystemCapability.Global.ResourceManager

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| path | string | Yes | Path of the rawfile. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Example**

import { resourceManager } from '@kit.LocalizationKit';

resourceManager.getResourceManager((error, mgr) => {
    mgr.closeRawFileDescriptor("test.txt");
});

#### resourceManager.getSystemResourceManager(deprecated)

getSystemResourceManager(): ResourceManager

Obtains a **ResourceManager** object.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8/v3/o4ulPgjtQLKTTnFKRyasbQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062326Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=04A86C8D1AFDC6E9FB1EB6531E329D5682D126C8EC186FE19E121A8795133732)

The **Configuration** field in the **ResourceManager** object obtained via this API uses the default value, which is as follows:

{"locale": "", "direction": -1, "deviceType": -1, "screenDensity": 0, "colorMode": 1, "mcc": 0, "mnc": 0}.

This API is supported since API version 10 and is deprecated since API version 20. You are advised to use [resourceManager.getSysResourceManager](#resourcemanagergetsysresourcemanager20) instead.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Global.ResourceManager

**Return value**

| Type | Description |
| :-- | :-- |
| [ResourceManager](#resourcemanager) | **ResourceManager** object. |

**Error codes**

For details about the error codes, see [Resource Manager Error Codes](../../error-codes/resource-manager-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 9001009 | Failed to access the system resource. which is not mapped to application sandbox, This error code will be thrown. |

**Example**

import { resourceManager } from '@kit.LocalizationKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let systemResourceManager = resourceManager.getSystemResourceManager();
  systemResourceManager.getStringValue($r('sys.string.ohos\_lab\_vibrate').id).then((value: string) => {
    let str = value;
  }).catch((error: BusinessError) => {
    console.error("systemResourceManager getStringValue promise error is " + error);
  });
} catch (error) {
  let code = (error as BusinessError).code;
  let message = (error as BusinessError).message;
  console.error(\`getSystemResourceManager failed, error code: ${code}, message: ${message}.\`);
}

#### AsyncCallback(deprecated)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ae/v3/Fo2l9Gt0TkaBhTGzTUT3wA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062326Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=6E45D109FC6AE0DE00FDB4304F193E56264DE6BEC826C4586DCDB2A169156676)

This API is supported since API version 6 and is deprecated since API version 9. You are advised to use [AsyncCallback](../../../../system/basic-functions/basic-services-kit/arkts-apis/others/ohos-base-public-callback-information/document.md#asynccallback) instead.

#### \[h2\](err: Error, data: T)(deprecated)

(err: Error, data: T): void;

Defines an asynchronous callback that carries an error parameter and asynchronous return value.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a6/v3/lCtHislcR5CoDSrflRcUgw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062326Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=39DB8ADDF5453DEDEA4DCFE277728E0C45CB308DD1E8A30832DE8D3B515A3E80)

This API is supported since API version 6 and is deprecated since API version 9. You are advised to use [AsyncCallback](../../../../system/basic-functions/basic-services-kit/arkts-apis/others/ohos-base-public-callback-information/document.md#asynccallback) instead.

**System capability**: SystemCapability.Global.ResourceManager

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| err | Error | Yes | Error message returned when the API fails to be called. |
| data | T | Yes | Callback invoked when the API is called. |

#### Appendix

-   Content of the **app.string.test** file:
    
    // Resource file path: src/main/resources/base/element/string.json
    {
      "string": \[
        {
          "name": "test",
          "value": "I'm a test string resource."
        }
      \]
    }
    
    // Resource file path: src/main/resources/base/element/string.json
    {
      "string": \[
        {
          "name": "test",
          "value": "I'm a %1$s, format int: %2$d, format float: %3$f."
        }
      \]
    }
    
-   Content of the **app.strarray.test** file:
    
    // Resource file path: src/main/resources/base/element/strarray.json
    {
      "strarray": \[
        {
          "name": "test",
          "value": \[
            {
              "value": "I'm one of the array's values."
            }
          \]
        }
      \]
    }
    
-   Content of the **app.plural.test** file:
    
    // Resource file path: src/main/resources/base/element/plural.json
    {
      "plural": \[
        {
          "name": "test",
          "value": \[
            {
              "quantity": "one",
              "value": "%d apple"
            },
            {
              "quantity": "other",
              "value": "%d apples"
            }
          \]
        }
      \]
    }
    
-   Content of the **app.plural.format\_test** file:
    
    // Resource file path: src/main/resources/base/element/plural.json
    {
      "plural": \[
        {
          "name": "format\_test",
          "value": \[
            {
              "quantity": "one",
              "value": "There is %d apple in the %s, the total amount is %f kg."
            },
            {
              "quantity": "other",
              "value": "There are %d apples in the %s, the total amount is %f kg."
            }
          \]
        }
      \]
    }
    
-   Content of the **app.boolean.boolean\_test** file:
    
    // Resource file path: src/main/resources/base/element/boolean.json
    {
      "boolean": \[
        {
          "name": "boolean\_test",
          "value": true
        }
      \]
    }
    
-   Content of the **integer\_test** and **float\_test** files:
    
    // Resource file path: src/main/resources/base/element/integer.json
    {
      "integer": \[
        {
          "name": "integer\_test",
          "value": 100
        }
      \]
    }
    
    // Resource file path: src/main/resources/base/element/float.json
    {
      "float": \[
        {
          "name": "float\_test",
          "value": "30.6vp"
        }
      \]
    }
    
-   Content of the **app.color.test** file:
    
    // Resource file path: src/main/resources/base/element/color.json
    {
      "color": \[
        {
          "name": "test",
          "value": "#FFFFFF"
        }
      \]
    }
