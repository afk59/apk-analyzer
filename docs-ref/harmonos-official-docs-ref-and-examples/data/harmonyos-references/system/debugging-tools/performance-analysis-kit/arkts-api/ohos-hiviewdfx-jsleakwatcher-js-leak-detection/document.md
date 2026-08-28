# @ohos.hiviewdfx.jsLeakWatcher (JS Leak Detection)

This module provides the capability of monitoring whether JS objects are leaked.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/67/v3/LIvbejJfTGC7CYUJQaGlkA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062414Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=5C1044B70A2B581C63C23A7BD68D9C529778487B6F61D67AB4B3CB7C3024B213)

The initial APIs of this module are supported since API version 12. Newly added APIs will be marked with a superscript to indicate their earliest API version.

#### Modules to Import

import { jsLeakWatcher } from '@kit.PerformanceAnalysisKit';

#### jsLeakWatcher.enable

enable(isEnable: boolean): void

Enables the detection for JS object leaks. This function is disabled by default.

**System capability**: SystemCapability.HiviewDFX.HiChecker

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| isEnable | boolean | Yes | Whether to enable **jsLeakWatcher**. **true**: yes; **false**: no. |

**Example**

jsLeakWatcher.enable(true);

#### jsLeakWatcher.watch

watch(obj: object, msg: string): void

Registers the object to be checked.

**System capability**: SystemCapability.HiviewDFX.HiChecker

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| obj | object | Yes | 
Name of the object to be checked.

Note: You can pass objects of any type.

 |
| msg | string | Yes | Custom object information. |

**Example**

let obj:Object = new Object();
jsLeakWatcher.watch(obj, "Trace Object");

#### jsLeakWatcher.check

check(): string

Obtains the list of objects that are leaked and registered using **jsLeakWatcher.watch()**. Objects that are not reclaimed after GC is triggered are marked as leaked.

**System capability**: SystemCapability.HiviewDFX.HiChecker

**Return value**

| Type | Description |
| :-- | :-- |
| string | 
List of leaked objects that are not reclaimed after GC is triggered.

Note: If this API is successful, a list of leaked objects in JSON format is returned. Otherwise, an empty string is returned.

 |

**Example**

let leakObjlist:string = jsLeakWatcher.check();

#### jsLeakWatcher.dump

dump(filePath: string): Array<string>

Exports the list of leaked objects and VM memory snapshot.

**System capability**: SystemCapability.HiviewDFX.HiChecker

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| filePath | string | Yes | Path for storing exported information files. |

**Return value**

| Type | Description |
| :-- | :-- |
| Array<string> | 
Export result. The file name extension is **.jsleaklist** for the list of leaked objects and **.heapsnapshot** for the VM memory snapshot.

Note: If the dump is successful, the path of the leaked object list file and the VM memory snapshot path are returned. Otherwise, an empty array is returned.

 |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. The filepath is invalid. |

**Example**

let context = this.getUIContext().getHostContext();
let files: Array<string> = jsLeakWatcher.dump(context?.filesDir);

#### jsLeakWatcher.enableLeakWatcher20+

enableLeakWatcher(isEnabled: boolean, configs: Array<string>, callback: Callback<Array<string>>): void

Enables the detection for JS object leaks. This function is disabled by default.

This API can detect the JS object memory leak, which is simpler than the method that needs to call the **enable**, **watch**, **check**, and **dump** functions.

If a memory leak occurs, the leaked file is returned through the callback.

**System capability**: SystemCapability.HiviewDFX.HiChecker

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| isEnabled | boolean | Yes | Whether to enable the detection for JS object memory leaks. **true**: yes; **false**: no. |
| configs | Array<string> | Yes | 
Configuration item. Each element in the array indicates a specific object type to monitor.

Options: **XComponent**, **NodeContainer**, **Window**, **CustomComponent**, and **Ability**.

Note: An empty array indicates that all the preceding objects are monitored.

 |
| callback | Callback<Array<string>> | Yes | 

Callback used to receive the memory-leaked object returned by the **jsLeakWatcher.enableLeakWatcher** API.

You need to input an array object in the callback. Index **0** is the name of the leak list file, whose extension is **.jsleaklist**. Index **1** is the name of the VM memory snapshot file, whose extension is **.rawheap**.

 |

**Error codes**

For details, see [JsLeakWatcher Error Codes](../../error-codes/jsleakwatcher-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 10801001 | The parameter isEnabled is invalid. |
| 10801002 | The parameter config is invalid. |
| 10801003 | The parameter callback is invalid. Input parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types; 3.Parameter verification failed. |

**Example**

let config: Array<string> = \['XComponent'\];
// Monitor the memory leak of the JS object XComponent.
// If an empty array is passed, all objects are monitored.
jsLeakWatcher.enableLeakWatcher(true, config, (filePath: Array<string>) => {
    console.info('JsLeakWatcher leaklistFileName:' + filePath\[0\]);
    console.info('JsLeakWatcher heapDumpFileName:' + filePath\[1\]);
});
