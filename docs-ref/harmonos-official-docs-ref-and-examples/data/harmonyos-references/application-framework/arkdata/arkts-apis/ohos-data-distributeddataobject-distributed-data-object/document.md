# @ohos.data.distributedDataObject (Distributed Data Object)

The **distributedDataObject** module provides basic data object management, including creating, querying, deleting, modifying, and subscribing to data objects, and distributed data object collaboration for the same application among multiple devices. Although this module does not parse user data, you are advised not to transfer sensitive personal data or privacy data due to low-level security of storage path.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/09/v3/Xj7iLvhkTGqmWrMTU5MT7w/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062215Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=4C949C99FC63281EF81680B138759C4EC6B0CE2AC3DED2888F18120E445F860E)

The initial APIs of this module are supported since API version 8. Newly added APIs will be marked with a superscript to indicate their earliest API version.

#### Modules to Import

import { distributedDataObject } from '@kit.ArkData';

#### distributedDataObject.create9+

create(context: Context, source: object): DataObject

Creates a distributed data object. The object properties support basic types (number, Boolean, and string) and complex types (array and nested basic types).

**System capability**: SystemCapability.DistributedDataManager.DataObject.DistributedObject

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| context | Context | Yes | 
Application context.

For details about the application context of the FA model, see [Context](../../../ability-kit/arkts-apis/fa-model/app/context-context-base-class-of-the-fa-model/document.md).

For details about the application context of the stage model, see [Context](../../../ability-kit/arkts-apis/dependent-elements-and-definitions/application/uiabilitycontext/document.md).

 |
| source | object | Yes | Properties of the distributed data object. |

**Return value**

| Type | Description |
| :-- | :-- |
| [DataObject](#dataobject) | Distributed data object created. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |

**Example**

FA model:

// Import the module.
import { featureAbility } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';
// Obtain the context.
let context = featureAbility.getContext();
class SourceObject {
    name: string
    age: number
    isVis: boolean

    constructor(name: string, age: number, isVis: boolean) {
        this.name = name;
        this.age = age;
        this.isVis = isVis;
    }
}

let source: SourceObject = new SourceObject("jack", 18, false);
let g\_object: distributedDataObject.DataObject = distributedDataObject.create(context, source);

Stage model:

// Import the module.
import { UIAbility } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { window } from '@kit.ArkUI';

let g\_object: distributedDataObject.DataObject|null = null;
class SourceObject {
    name: string
    age: number
    isVis: boolean

    constructor(name: string, age: number, isVis: boolean) {
        this.name = name;
        this.age = age;
        this.isVis = isVis;
    }
}

class EntryAbility extends UIAbility {
    onWindowStageCreate(windowStage: window.WindowStage) {
        let source: SourceObject = new SourceObject("jack", 18, false);
        g\_object = distributedDataObject.create(this.context, source);
    }
}

#### distributedDataObject.genSessionId

genSessionId(): string

Creates a random session ID.

**System capability**: SystemCapability.DistributedDataManager.DataObject.DistributedObject

**Return value**

| Type | Description |
| :-- | :-- |
| string | Session ID created. |

**Example**

let sessionId: string = distributedDataObject.genSessionId();

#### SaveSuccessResponse9+

Represents the information returned by the callback of [save](#save9).

**System capability**: SystemCapability.DistributedDataManager.DataObject.DistributedObject

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| sessionId | string | No | No | Unique ID for multi-device collaboration. |
| version | number | No | No | Version of the saved object, which is a non-negative integer. |
| deviceId | string | No | No | ID of the device where the distributed data object is stored. The value **local** indicates a local device. |

#### RevokeSaveSuccessResponse9+

Represents the information returned by the callback of [revokeSave](#revokesave9).

**System capability**: SystemCapability.DistributedDataManager.DataObject.DistributedObject

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| sessionId | string | No | No | Unique ID for multi-device collaboration. |

#### BindInfo11+

Represents the information about the joint asset in the RDB store to bind. Currently, only the RDB stores are supported.

**System capability**: SystemCapability.DistributedDataManager.DataObject.DistributedObject

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| storeName | string | No | No | RDB store to which the target asset (asset to bind) belongs. |
| tableName | string | No | No | Table to which the target asset is located in the RDB store. |
| primaryKey | [commonType.ValuesBucket](../ohos-data-commontype-common-data-types/document.md#valuesbucket) | No | No | Primary key of the target asset in the RDB store. |
| field | string | No | No | Column in which the target asset is located in the RDB store. |
| assetName | string | No | No | Name of the target asset in the RDB store. |

#### DataObserver20+

type DataObserver = (sessionId: string, fields: Array<string>) => void

Defines an observer for obtaining the data change of a distributed object.

**System capability**: SystemCapability.DistributedDataManager.DataObject.DistributedObject

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| sessionId | string | Yes | Session ID of the distributed data object, with a maximum length of 128 bytes. The value can contain only letters, digits, and underscores (\_). |
| fields | Array<string> | Yes | Changed properties of the distributed data object, with a maximum length of 128 bytes. The value can be customized and must be a non-empty string. |

#### StatusObserver20+

type StatusObserver = (sessionId: string, networkId: string, status: string) => void

Defines an observer for obtaining the status change of a distributed object.

**System capability**: SystemCapability.DistributedDataManager.DataObject.DistributedObject

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| sessionId | string | Yes | Session ID of the distributed data object, with a maximum length of 128 bytes. The value can contain only letters, digits, and underscores (\_). |
| networkId | string | Yes | Network ID of the peer device, with a maximum of 255 bytes. The value must be a non-empty string. |
| status | string | Yes | Status of the distributed object. The value can be **online**, **offline**, or **restore.** |

#### ProgressObserver20+

type ProgressObserver = (sessionId: string, progress: number) => void

Defines an observer for obtaining the transfer progress.

**System capability**: SystemCapability.DistributedDataManager.DataObject.DistributedObject

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| sessionId | string | Yes | Session ID of the distributed data object, with a maximum length of 128 bytes. The value can contain only letters, digits, and underscores (\_). |
| progress | number | Yes | Asset transfer progress. The value is an integer ranging from -1 to 100. The value **\-1** indicates that the progress fails to be obtained, and the value **100** indicates that the transfer is complete. |

#### DataObject

Provides APIs for managing a distributed data object. Before using any API of this class, use [create()](#distributeddataobjectcreate9) to create a **DataObject** object.

#### \[h2\]setSessionId9+

setSessionId(sessionId: string, callback: AsyncCallback<void>): void

Sets a session ID. This API uses an asynchronous callback to return the result. For the devices in the collaboration state in a trusted network, data of the distributed objects with the same session ID can be automatically synced across devices.

**Required permissions**: ohos.permission.DISTRIBUTED\_DATASYNC

**System capability**: SystemCapability.DistributedDataManager.DataObject.DistributedObject

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| sessionId | string | Yes | ID of a distributed data object on a trusted network. The value can contain only letters, digits, and underscores (\_), and cannot exceed 128 characters. If this parameter is set to **""** or **null**, the distributed data object exits the network. |
| callback | AsyncCallback<void> | Yes | Asynchronous callback invoked when the session ID is successfully set. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md) and [Distributed Data Object Error Codes](../../error-codes/distributed-data-object-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 201 | Permission verification failed. |
| 401 | Parameter error. Possible causes: 1. Incorrect parameter types; 2. The sessionId allows only letters, digits, and underscores(\_), and cannot exceed 128 in length. |
| 15400001 | Failed to create the in-memory database. |

**Example**

// Add g\_object to the distributed network.
g\_object.setSessionId(distributedDataObject.genSessionId(), ()=>{
    console.info("join session");
});
// g\_object exits the distributed network.
g\_object.setSessionId("", ()=>{
    console.info("leave all session");
});

#### \[h2\]setSessionId9+

setSessionId(callback: AsyncCallback<void>): void

Exits all sessions. This API uses an asynchronous callback to return the result.

**System capability**: SystemCapability.DistributedDataManager.DataObject.DistributedObject

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | AsyncCallback<void> | Yes | Callback invoked when the distributed data object exits all sessions. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md) and [Distributed Data Object Error Codes](../../error-codes/distributed-data-object-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Incorrect parameter types. |
| 15400001 | Failed to create the in-memory database. |

**Example**

// Add g\_object to the distributed network.
g\_object.setSessionId(distributedDataObject.genSessionId(), ()=>{
    console.info("join session");
});
// Exit the distributed network.
g\_object.setSessionId(() => {
    console.info("leave all session.");
});

#### \[h2\]setSessionId9+

setSessionId(sessionId?: string): Promise<void>

Sets a session ID or exits the distributed network. This API uses a promise to return the result. If this parameter is set to **""** or **null**, or left empty, the distributed data object exits the network. For the devices in the collaboration state in a trusted network, data of the distributed objects with the same session ID can be automatically synced across devices.

**Required permissions**: ohos.permission.DISTRIBUTED\_DATASYNC

**System capability**: SystemCapability.DistributedDataManager.DataObject.DistributedObject

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| sessionId | string | No | ID of a distributed data object on a trusted network. The value can contain only letters, digits, and underscores (\_), and cannot exceed 128 characters. If this parameter is set to **""** or **null**, or left empty, the distributed data object exits the network. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md) and [Distributed Data Object Error Codes](../../error-codes/distributed-data-object-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 201 | Permission verification failed. |
| 401 | Parameter error. Possible causes: 1. Incorrect parameter types; 2. The sessionId allows only letters, digits, and underscores(\_), and cannot exceed 128 in length. |
| 15400001 | Failed to create the in-memory database. |

**Example**

// Add g\_object to the distributed network.
g\_object.setSessionId(distributedDataObject.genSessionId()).then (()=>{
    console.info("join session.");
    }).catch((error: BusinessError)=>{
        console.error("error:" + error.code + error.message);
});
// Exit the distributed network.
g\_object.setSessionId().then (()=>{
    console.info("leave all session.");
    }).catch((error: BusinessError)=>{
        console.error("error:" + error.code + error.message);
});

#### \[h2\]on('change')9+

on(type: 'change', callback: (sessionId: string, fields: Array<string>) => void): void

Subscribes to data changes of this distributed data object.

**System capability**: SystemCapability.DistributedDataManager.DataObject.DistributedObject

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Event type. The value is **'change'**, which indicates data changes. |
| callback | (sessionId: string, fields: Array<string>) => void | Yes | 
Callback used to return the changes of the distributed data object.

**sessionId** indicates the session ID of the distributed data object.

**fields** indicates the changed properties of the distributed data object.

 |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |

**Example**

g\_object.on("change", (sessionId: string, fields: Array<string>) => {
    console.info("change" + sessionId);
    if (g\_object != null && fields != null && fields != undefined) {
        for (let index: number = 0; index < fields.length; index++) {
            console.info("changed !" + fields\[index\] + " " + g\_object\[fields\[index\]\]);
        }
    }
});

#### \[h2\]off('change')9+

off(type: 'change', callback?: (sessionId: string, fields: Array<string>) => void): void

Unsubscribes from data changes of this distributed data object.

**System capability**: SystemCapability.DistributedDataManager.DataObject.DistributedObject

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Event type. The value is **'change'**, which indicates data changes. |
| callback | (sessionId: string, fields: Array<string>) => void | No | 
Callback to unregister. If this parameter is not specified, this API unsubscribes from all callbacks for data changes of this distributed object.

**sessionId** indicates the session ID of the distributed data object.

**fields** indicates the changed properties of the distributed data object.

 |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |

**Example**

// Unregister the specified data change callback.
g\_object.off("change", (sessionId: string, fields: Array<string>) => {
    console.info("change" + sessionId);
    if (g\_object != null && fields != null && fields != undefined) {
        for (let index: number = 0; index < fields.length; index++) {
            console.info("changed !" + fields\[index\] + " " + g\_object\[fields\[index\]\]);
        }
    }
});
// Unregister all data change callbacks.
g\_object.off("change");

#### \[h2\]on('status')9+

on(type: 'status', callback: (sessionId: string, networkId: string, status: 'online' | 'offline' ) => void): void

Subscribes to status changes of this distributed data object.

**System capability**: SystemCapability.DistributedDataManager.DataObject.DistributedObject

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Event type. The value is **'status'**, which indicates the status change (online or offline) of the distributed object. |
| callback | (sessionId: string, networkId: string, status: 'online' | 'offline' ) => void | Yes | 
Callback used to return the status change.

**sessionId** indicates the session ID of the distributed data object.

**networkId** identifies the device.

**status** indicates the object status, which can be online or offline.

 |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |

**Example**

g\_object.on("status", (sessionId: string, networkId: string, status: 'online' | 'offline') => {
    console.info("status changed " + sessionId + " " + status + " " + networkId);
});

#### \[h2\]off('status')9+

off(type: 'status', callback?:(sessionId: string, networkId: string, status: 'online' | 'offline') => void): void

Unsubscribes from the status change of this distributed data object.

**System capability**: SystemCapability.DistributedDataManager.DataObject.DistributedObject

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Event type. The value is **'status'**, which indicates the status change (online or offline) of the distributed object. |
| callback | (sessionId: string, networkId: string, status: 'online' | 'offline' ) => void | No | 
Callback to unregister. If this parameter is not specified, this API unsubscribes from all callbacks for status changes of this distributed object.

**sessionId** indicates the session ID of the distributed data object.

**networkId** identifies the distributed data object.

**status** indicates the object status, which can be online or offline.

 |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |

**Example**

// Unregister the specified status change callback.
g\_object.off("status", (sessionId: string, networkId: string, status: 'online' | 'offline') => {
    console.info("status changed " + sessionId + " " + status + " " + networkId);
});
// Unregister all status change callbacks.
g\_object.off("status");

#### \[h2\]save9+

save(deviceId: string, callback: AsyncCallback<SaveSuccessResponse>): void

Saves a distributed data object. This API uses an asynchronous callback to return the result.

If the application is active, the saved data will not be released. When the application exits and restarts, the data saved on the device will be restored.

The saved data will be released in the following cases:

-   The data is stored for more than 24 hours.
-   The application has been uninstalled.
-   Data is successfully restored.

**System capability**: SystemCapability.DistributedDataManager.DataObject.DistributedObject

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| deviceId | string | Yes | ID of the device where the data is stored. The value **local** indicates a local device. |
| callback | AsyncCallback<[SaveSuccessResponse](#savesuccessresponse9)\> | Yes | Callback used to return **SaveSuccessResponse**, which contains information such as session ID, version, and device ID. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |
| 801 | Capability not supported. |

**Example**

g\_object.setSessionId("123456");
g\_object.save("local", (err: BusinessError, result:distributedDataObject.SaveSuccessResponse) => {
    if (err) {
        console.error("save failed, error code = " + err.code);
        console.error("save failed, error message: " + err.message);
        return;
    }
    console.info("save callback");
    console.info("save sessionId: " + result.sessionId);
    console.info("save version: " + result.version);
    console.info("save deviceId:  " + result.deviceId);
});

#### \[h2\]save9+

save(deviceId: string): Promise<SaveSuccessResponse>

Saves a distributed data object. This API uses a promise to return the result.

If the application is active, the saved data will not be released. When the application exits and restarts, the data saved on the device will be restored.

The saved data will be released in the following cases:

-   The data is stored for more than 24 hours.
-   The application has been uninstalled.
-   Data is successfully restored.

**System capability**: SystemCapability.DistributedDataManager.DataObject.DistributedObject

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| deviceId | string | Yes | ID of the device where the data is saved. The default value is **local**, which indicates a local device. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<[SaveSuccessResponse](#savesuccessresponse9)\> | Promise used to return **SaveSuccessResponse**, which contains information such as session ID, version, and device ID. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |
| 801 | Capability not supported. |

**Example**

g\_object.setSessionId("123456");
g\_object.save("local").then((callbackInfo: distributedDataObject.SaveSuccessResponse) => {
    console.info("save callback");
    console.info("save sessionId " + callbackInfo.sessionId);
    console.info("save version " + callbackInfo.version);
    console.info("save deviceId " + callbackInfo.deviceId);
}).catch((err: BusinessError) => {
    console.error("save failed, error code = " + err.code);
    console.error("save failed, error message: " + err.message);
});

#### \[h2\]revokeSave9+

revokeSave(callback: AsyncCallback<RevokeSaveSuccessResponse>): void

Revokes the data of this distributed data object saved. This API uses an asynchronous callback to return the result.

If the object is saved on the local device, the data saved on all trusted devices will be deleted.

If the object is stored on another device, the data on the local device will be deleted.

**System capability**: SystemCapability.DistributedDataManager.DataObject.DistributedObject

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | AsyncCallback<[RevokeSaveSuccessResponse](#revokesavesuccessresponse9)\> | Yes | Callback used to return **RevokeSaveSuccessResponse**, which contains the session ID. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Incorrect parameter types. |
| 801 | Capability not supported. |

**Example**

g\_object.setSessionId("123456");
// Save data for persistence.
g\_object.save("local", (err: BusinessError, result: distributedDataObject.SaveSuccessResponse) => {
    if (err) {
        console.error("save failed, error code = " + err.code);
        console.error("save failed, error message: " + err.message);
        return;
    }
    console.info("save callback");
    console.info("save sessionId: " + result.sessionId);
    console.info("save version: " + result.version);
    console.info("save deviceId:  " + result.deviceId);
});
// Delete the persistence data.
g\_object.revokeSave((err: BusinessError, result: distributedDataObject.RevokeSaveSuccessResponse) => {
    if (err) {
      console.error("revokeSave failed, error code = " + err.code);
      console.error("revokeSave failed, error message: " + err.message);
      return;
    }
    console.info("revokeSave callback");
    console.info("revokeSave sessionId " + result.sessionId);
});

#### \[h2\]revokeSave9+

revokeSave(): Promise<RevokeSaveSuccessResponse>

Revokes the data of this distributed data object saved. This API uses a promise to return the result.

If the object is saved on the local device, the data saved on all trusted devices will be deleted.

If the object is stored on another device, the data on the local device will be deleted.

**System capability**: SystemCapability.DistributedDataManager.DataObject.DistributedObject

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<[RevokeSaveSuccessResponse](#revokesavesuccessresponse9)\> | Promise used to return **RevokeSaveSuccessResponse**, which contains the session ID. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 801 | Capability not supported. |

**Example**

g\_object.setSessionId("123456");
// Save data for persistence.
g\_object.save("local").then((result: distributedDataObject.SaveSuccessResponse) => {
    console.info("save callback");
    console.info("save sessionId " + result.sessionId);
    console.info("save version " + result.version);
    console.info("save deviceId " + result.deviceId);
}).catch((err: BusinessError) => {
    console.error("save failed, error code = " + err.code);
    console.error("save failed, error message: " + err.message);
});
// Delete the persistence data.
g\_object.revokeSave().then((result: distributedDataObject.RevokeSaveSuccessResponse) => {
    console.info("revokeSave callback");
    console.info("sessionId" + result.sessionId);
}).catch((err: BusinessError)=> {
    console.error("revokeSave failed, error code = " + err.code);
    console.error("revokeSave failed, error message = " + err.message);
});

#### \[h2\]bindAssetStore11+

bindAssetStore(assetKey: string, bindInfo: BindInfo, callback: AsyncCallback<void>): void

Binds joint assets. Currently, only the binding between an asset in a distributed data object and an asset in an RDB store is supported. This API uses an asynchronous callback to return the result.

When an asset in a distributed object and an asset in an RDB store point to the same entity asset file, that is, the URIs of the two assets are the same, a conflict occurs. Such assets are called joint assets. To resolve the conflict, bind the joint assets. The binding is automatically released when the application exits the session.

**System capability**: SystemCapability.DistributedDataManager.DataObject.DistributedObject

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| assetKey | string | Yes | Key of the joint asset in the distributed data object. |
| bindInfo | [BindInfo](#bindinfo11) | Yes | Information about the joint asset in the RDB store, including the RDB store name, table name, primary key, column name, and asset name in the RDB store. |
| callback | AsyncCallback<void> | Yes | Callback used to return the result. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |
| 801 | Capability not supported. |

**Example**

import { UIAbility } from '@kit.AbilityKit';
import { window } from '@kit.ArkUI';
import { commonType } from '@kit.ArkData';
import { BusinessError } from '@kit.BasicServicesKit';

class Note {
  title: string | undefined
  text: string | undefined
  attachment: commonType.Asset | undefined

  constructor(title: string | undefined, text: string | undefined, attachment: commonType.Asset | undefined) {
    this.title = title;
    this.text = text;
    this.attachment = attachment;
  }
}

class EntryAbility extends UIAbility {
  onWindowStageCreate(windowStage: window.WindowStage) {
    let attachment: commonType.Asset = {
      name: 'test\_img.jpg',
      uri: 'file://com.example.myapplication/data/storage/el2/distributedfiles/dir/test\_img.jpg',
      path: '/dir/test\_img.jpg',
      createTime: '2024-01-02 10:00:00',
      modifyTime: '2024-01-02 10:00:00',
      size: '5',
      status: commonType.AssetStatus.ASSET\_NORMAL
    }
    let note: Note = new Note('test', 'test', attachment);
    let g\_object: distributedDataObject.DataObject = distributedDataObject.create(this.context, note);
    g\_object.setSessionId('123456');

    const bindInfo: distributedDataObject.BindInfo = {
      storeName: 'notepad',
      tableName: 'note\_t',
      primaryKey: {
        'uuid': '00000000-0000-0000-0000-000000000000'
      },
      field: 'attachment',
      assetName: attachment.name as string
    }

    g\_object.bindAssetStore('attachment', bindInfo, (err: BusinessError) => {
      if (err) {
        console.error('bindAssetStore failed.');
      }
      console.info('bindAssetStore success.');
    });
  }
}

#### \[h2\]bindAssetStore11+

bindAssetStore(assetKey: string, bindInfo: BindInfo): Promise<void>

Binds joint assets. Currently, only the binding between an asset in a distributed data object and an asset in an RDB store is supported. This API uses a promise to return the result.

When an asset in a distributed object and an asset in an RDB store point to the same entity asset file, that is, the URIs of the two assets are the same, a conflict occurs. Such assets are called joint assets. To resolve the conflict, bind the joint assets. The binding is automatically released when the application exits the session.

**System capability**: SystemCapability.DistributedDataManager.DataObject.DistributedObject

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| assetKey | string | Yes | Key of the joint asset in the distributed data object. |
| bindInfo | [BindInfo](#bindinfo11) | Yes | Information about the joint asset in the RDB store, including the RDB store name, table name, primary key, column name, and asset name in the RDB store. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |
| 801 | Capability not supported. |

**Example**

import { UIAbility } from '@kit.AbilityKit';
import { window } from '@kit.ArkUI';
import { commonType } from '@kit.ArkData';
import { BusinessError } from '@kit.BasicServicesKit';

class Note {
  title: string | undefined
  text: string | undefined
  attachment: commonType.Asset | undefined

  constructor(title: string | undefined, text: string | undefined, attachment: commonType.Asset | undefined) {
    this.title = title;
    this.text = text;
    this.attachment = attachment;
  }
}

class EntryAbility extends UIAbility {
  onWindowStageCreate(windowStage: window.WindowStage) {
    let attachment: commonType.Asset = {
      name: 'test\_img.jpg',
      uri: 'file://com.example.myapplication/data/storage/el2/distributedfiles/dir/test\_img.jpg',
      path: '/dir/test\_img.jpg',
      createTime: '2024-01-02 10:00:00',
      modifyTime: '2024-01-02 10:00:00',
      size: '5',
      status: commonType.AssetStatus.ASSET\_NORMAL
    }
    let note: Note = new Note('test', 'test', attachment);
    let g\_object: distributedDataObject.DataObject = distributedDataObject.create(this.context, note);
    g\_object.setSessionId('123456');

    const bindInfo: distributedDataObject.BindInfo = {
      storeName: 'notepad',
      tableName: 'note\_t',
      primaryKey: {
        'uuid': '00000000-0000-0000-0000-000000000000'
      },
      field: 'attachment',
      assetName: attachment.name as string
    }

    g\_object.bindAssetStore("attachment", bindInfo).then(() => {
      console.info('bindAssetStore success.');
    }).catch((err: BusinessError) => {
      console.error("bindAssetStore failed, error code = " + err.code);
    });
  }
}

#### \[h2\]on('change')20+

on(type: 'change', callback: DataObserver): void

Subscribes to data changes of this distributed data object.

**System capability**: SystemCapability.DistributedDataManager.DataObject.DistributedObject

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Event type. The value is **'change'**, which indicates data changes. |
| callback | [DataObserver](#dataobserver20) | Yes | Callback used to listen for data changes of a distributed object. |

**Example**

const changeCallback1: distributedDataObject.DataObserver = (sessionId: string, fields: Array<string>) => {
  console.info("change callback1 " + sessionId);
  if (fields != null && fields != undefined) {
      for (let index: number = 0; index < fields.length; index++) {
          console.info("change !" + fields\[index\]);
      }
  }
}
try {
  g\_object.on("change", changeCallback1);
} catch (error) {
  console.error("Execute failed, error code =  " + error.code);
}

#### \[h2\]off('change')20+

off(type: 'change', callback?: DataObserver): void

Unsubscribes from data changes of this distributed object.

**System capability**: SystemCapability.DistributedDataManager.DataObject.DistributedObject

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Event type. The value is **'change'**, which indicates data changes. |
| callback | [DataObserver](#dataobserver20) | No | Callback to unregister. If this parameter is not specified, this API unsubscribes from all callbacks for data changes of this distributed object. |

**Example**

const changeCallback1: distributedDataObject.DataObserver = (sessionId: string, fields: Array<string>) => {
  console.info("change callback1 " + sessionId);
  if (fields != null && fields != undefined) {
      for (let index: number = 0; index < fields.length; index++) {
          console.info("change !" + fields\[index\]);
      }
  }
}

const changeCallback2: distributedDataObject.DataObserver = (sessionId: string, fields: Array<string>) => {
  console.info("change callback2 " + sessionId);
  if (fields != null && fields != undefined) {
      for (let index: number = 0; index < fields.length; index++) {
          console.info("change !" + fields\[index\]);
      }
  }
}

try {
  // Unregister a single data change callback function.
  g\_object.on("change", changeCallback1);
  g\_object.off("change", changeCallback1);

  // Unregister all data change callback functions.
  g\_object.on("change", changeCallback1);
  g\_object.on("change", changeCallback2);
  g\_object.off("change");
} catch (error) {
  console.error("Execute failed, error code =  " + error.code);
}

#### \[h2\]on('status')20+

on(type: 'status', callback: StatusObserver): void

Subscribes to the status changes of this distributed object.

**System capability**: SystemCapability.DistributedDataManager.DataObject.DistributedObject

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Event type. The value is **'status'**, which indicates the status changes of a distributed object. |
| callback | [StatusObserver](#statusobserver20) | Yes | Callback used to listen for status changes of a distributed object. |

**Example**

const statusCallback1: distributedDataObject.StatusObserver = (sessionId: string, networkId: string, status: string) => {
  console.info("status callback " + sessionId);
}
try {
  g\_object.on("status", statusCallback1);
} catch (error) {
  console.error("Execute failed, error code =  " + error.code);
}

#### \[h2\]off('status')20+

off(type: 'status', callback?: StatusObserver): void

Unsubscribes from status changes of this distributed object.

**System capability**: SystemCapability.DistributedDataManager.DataObject.DistributedObject

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Event type. The value is **'status'**, which indicates the status changes of a distributed object. |
| callback | [StatusObserver](#statusobserver20) | No | Callback to unregister. If this parameter is not specified, this API unsubscribes from all callbacks for status changes of this distributed object. |

**Example**

const statusCallback1: distributedDataObject.StatusObserver = (sessionId: string, networkId: string, status: string) => {
  console.info("status callback1" + sessionId);
}

const statusCallback2: distributedDataObject.StatusObserver = (sessionId: string, networkId: string, status: string) => {
  console.info("status callback2" + sessionId);
}
try {
  // Unregister a single status change callback function.
  g\_object.on("status", statusCallback1);
  g\_object.off("status", statusCallback1);

  // Unregister all status change callback functions.
  g\_object.on("status", statusCallback1);
  g\_object.on("status", statusCallback2);
  g\_object.off("status");
} catch (error) {
  console.error("Execute failed, error code =  " + error.code);
}

#### \[h2\]on('progressChanged')20+

on(type: 'progressChanged', callback: ProgressObserver): void

Subscribes to the asset transfer progress changes.

**System capability**: SystemCapability.DistributedDataManager.DataObject.DistributedObject

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Event type. The value is **'progressChanged'**, which indicates the asset transfer progress changes. |
| callback | [ProgressObserver](#progressobserver20) | Yes | Callback used to listen for the asset transfer progress changes. |

**Example**

const progressChangedCallback: distributedDataObject.ProgressObserver = (sessionId: string, progress: number) => {
  console.info("progressChanged callback" + sessionId);
  console.info("progressChanged callback" + progress);
}
try {
  g\_object.on("progressChanged", progressChangedCallback);
} catch (error) {
  console.error("Execute failed, error code =  " + error.code);
}

#### \[h2\]off('progressChanged')20+

off(type: 'progressChanged', callback?: ProgressObserver): void

Unsubscribes from asset transfer progress changes.

**System capability**: SystemCapability.DistributedDataManager.DataObject.DistributedObject

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Event type. The value is **'progressChanged'**, which indicates the asset transfer progress changes. |
| callback | [ProgressObserver](#progressobserver20) | No | Callback to unregister. If this parameter is not specified, this API unsubscribes from all callbacks for progress changes of this distributed object. |

**Example**

const progressChangedCallback1: distributedDataObject.ProgressObserver = (sessionId: string, progress: number) => {
  console.info("progressChanged callback1" + sessionId);
  console.info("progressChanged callback1" + progress);
}

const progressChangedCallback2: distributedDataObject.ProgressObserver = (sessionId: string, progress: number) => {
  console.info("progressChanged callback2" + sessionId);
  console.info("progressChanged callback2" + progress);
}
try {
  g\_object.on("progressChanged", progressChangedCallback1);
  // Unsubscribes from the asset transfer progress changes.
  g\_object.off("progressChanged", progressChangedCallback1);

  g\_object.on("progressChanged", progressChangedCallback1);
  g\_object.on("progressChanged", progressChangedCallback2);
  // Unsubscribes from all asset transfer progress changes.
  g\_object.off("progressChanged");
} catch (error) {
  console.error("Execute failed, error code =  " + error.code);
}

#### \[h2\]setAsset20+

setAsset(assetKey: string, uri: string): Promise<void>

Sets the property information about a single asset in a distributed object. This API must be called before the [setSessionId](#setsessionid9-2) API is called. This API uses a promise to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5/v3/zBv5GPm_TZqGAP-zrkKRlw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062215Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=A26BA4E3B1921C67F612B6B293E17D27668809AA447FE648D063E2319048827C)

When setting an asset, ensure that the **assetKey** file exists and is of the asset type. Otherwise, the peer device may fail to receive the asset.

When setting an asset, ensure that the URI is a correct and actual distributed path. Otherwise, the peer device may fail to receive the asset.

The following table lists the exception scenarios.

| Scenario | Execution Results |
| :-- | :-- |
| The [setAsset](#setasset20) API is called to set an asset after the [setSessionId](#setsessionid9-2) API is called to set a session ID. | Error code 15400003 is thrown, indicating the asset setting failure. |
| The value of **assetKey** is invalid, for example, **null**, **undefined**, or '' (empty). | Error code 15400002 is thrown, indicating the asset setting failure. |
| **assetKey** exists, but the corresponding file is not of the asset type. | The system forcibly changes the file type to asset and sets the asset field. As a result, the actual asset may fail to be synchronized to the peer device. |
| The value of **uri** is invalid, for example, **null**, **undefined**, or '' (empty). | Error code 15400002 is thrown, indicating the asset setting failure. |

**System capability**: SystemCapability.DistributedDataManager.DataObject.DistributedObject

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| assetKey | string | Yes | 
Property name of the asset in the distributed object.

**Constraints**

(1) The corresponding **assetKey** file must exist and be of the [Asset](../ohos-data-commontype-common-data-types/document.md#asset) type. Otherwise, an asset setting error may occur.

(2) In the collaboration or continuation scenario, the corresponding **assetKey** file must exist and be of the asset type at both devices so that the asset can be synchronized to the peer device.

 |
| uri | string | Yes | URI of the new asset to be set, indicating the distributed path for storing the asset. The value must correspond to an existing asset. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Error codes**

For details about the error codes, see [Distributed Data Object Error Codes](../../error-codes/distributed-data-object-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 15400002 | Parameter error. Possible causes: 1. The assetKey is invalid, such as ""; 2. The uri is invalid, such as "". |
| 15400003 | The sessionId of the distributed object has been set. |

**Example**:

import { UIAbility } from '@kit.AbilityKit';
import { window } from '@kit.ArkUI';
import { BusinessError } from '@kit.BasicServicesKit';
import { commonType, distributedDataObject } from '@kit.ArkData';

class Note {
  title: string | undefined
  text: string | undefined
  attachment: commonType.Asset | undefined

  constructor(title: string | undefined, text: string | undefined, attachment: commonType.Asset | undefined) {
    this.title = title;
    this.text = text;
    this.attachment = attachment;
  }
}

class EntryAbility extends UIAbility {
  onWindowStageCreate(windowStage: window.WindowStage) {
    let attachment: commonType.Asset = {
      name: 'test\_img.jpg',
      uri: 'file://com.example.myapplication/data/storage/el2/distributedfiles/dir/test\_img.jpg',
      path: '/dir/test\_img.jpg',
      createTime: '2024-01-02 10:00:00',
      modifyTime: '2024-01-02 10:00:00',
      size: '5',
      status: commonType.AssetStatus.ASSET\_NORMAL
    }
    let note: Note = new Note('test', 'test', attachment);
    let g\_object: distributedDataObject.DataObject = distributedDataObject.create(this.context, note);

    let uri = "file://test/test.img";
    g\_object.setAsset("attachment", uri).then(() => {
      console.info('setAsset success.');
    }).catch((err: BusinessError) => {
      console.error("setAsset failed, error code = " + err.code);
    });
  }
}

#### \[h2\]setAssets20+

setAssets(assetsKey: string, uris: Array<string>): Promise<void>

Sets the property information about multiple assets in a distributed object. This API must be called before the [setSessionId](#setsessionid9-2) API is called. The number of values contained in the **uris** array ranges from 1 to 50. This API uses a promise to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fd/v3/EaFBJWZNSouvgFO7rrlT_w/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062215Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=DDEC3CE31574E47FE5319AD0F675B14C0EAC1334994C6A2A428D593DD7383B77)

When setting an asset, ensure that the **assetsKey** file exists and is of the asset type. Otherwise, the peer device may fail to receive the assets.

When setting an asset, ensure that the URIs in the array are correct and actual distributed paths. Otherwise, the peer device may fail to receive the assets.

The following table lists the exception scenarios.

| Scenario | Execution Results |
| :-- | :-- |
| The [setAssets](#setassets20) API is called to set an asset after the [setSessionId](#setsessionid9-2) API is called to set a session ID. | Error code 15400003 is thrown, indicating the asset setting failure. |
| The value of **assetsKey** is invalid, for example, **null**, **undefined**, or '' (empty). | Error code 15400002 is thrown, indicating the asset setting failure. |
| **assetsKey** exists, but the corresponding file is not of the asset type. | The system forcibly changes the file type to asset and sets the asset field. As a result, the actual asset may fail to be synchronized to the peer device. |
| **assetsKey** exists and the corresponding file is of the asset type. | The asset is set successfully, and the URI information is updated. |
| The number of URI elements in the **uris** array is 0 or greater than 50. | Error code 15400002 is thrown, indicating the asset setting failure. |
| The number of URI elements in the **uris** array ranges from 1 to 50, and one or more URIs are invalid, for example, **null**, **undefined**, or '' (empty). | Error code 15400002 is thrown, indicating the asset setting failure. |

**System capability**: SystemCapability.DistributedDataManager.DataObject.DistributedObject

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| assetsKey | string | Yes | 
Property name of the assets in the distributed object.

**Constraints**

(1) The corresponding **assetsKey** file must exist and be of the [Asset](../ohos-data-commontype-common-data-types/document.md#asset) type. Otherwise, an asset setting error may occur.

(2) In the collaboration or continuation scenario, the corresponding **assetsKey** file must exist and be of the asset type at both devices so that the asset array can be synchronized to the peer device.

 |
| uris | Array<string> | Yes | URIs of the new asset array to be set, indicating the distributed paths for storing each element of the asset. The number of array elements ranges from 1 to 50. The URI of an element must be the distributed path corresponding to an actual asset. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Error codes**

For details about the error codes, see [Distributed Data Object Error Codes](../../error-codes/distributed-data-object-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 15400002 | Parameter error. Possible causes:1. The assetsKey is invalid, such as ""; 2. The uris is invalid, such as the length of uris is more than 50. |
| 15400003 | The sessionId of the distributed object has been set. |

**Example**:

import { UIAbility } from '@kit.AbilityKit';
import { window } from '@kit.ArkUI';
import { BusinessError } from '@kit.BasicServicesKit';
import { commonType, distributedDataObject } from '@kit.ArkData';

class Note {
  title: string | undefined
  text: string | undefined
  attachment: commonType.Asset | undefined

  constructor(title: string | undefined, text: string | undefined, attachment: commonType.Asset | undefined) {
    this.title = title;
    this.text = text;
    this.attachment = attachment;
  }
}

class EntryAbility extends UIAbility {
  onWindowStageCreate(windowStage: window.WindowStage) {
    let attachment: commonType.Asset = {
      name: 'test\_img.jpg',
      uri: 'file://com.example.myapplication/data/storage/el2/distributedfiles/dir/test\_img.jpg',
      path: '/dir/test\_img.jpg',
      createTime: '2024-01-02 10:00:00',
      modifyTime: '2024-01-02 10:00:00',
      size: '5',
      status: commonType.AssetStatus.ASSET\_NORMAL
    }
    let note: Note = new Note('test', 'test', attachment);
    let g\_object: distributedDataObject.DataObject = distributedDataObject.create(this.context, note);

    let uris: Array<string> = \["file://test/test\_1.txt", "file://test/test\_2.txt"\];
    g\_object.setAssets("attachment", uris).then(() => {
      console.info('setAssets success.');
    }).catch((err: BusinessError) => {
      console.error("setAssets failed, error code = " + err.code);
    });
  }
}

#### distributedDataObject.createDistributedObject(deprecated)

createDistributedObject(source: object): DistributedObject

Creates a distributed data object.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/54/v3/cXOhvfDjTGyw0dB1a7jJag/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062215Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=7E3355641DABAEB36C23FEA37673A23FCEFDC13FD10BED50B0161CD0776B303F)

This API is supported since API version 8 and deprecated since API version 9. You are advised to use [distributedDataObject.create](#distributeddataobjectcreate9) instead.

**System capability**: SystemCapability.DistributedDataManager.DataObject.DistributedObject

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| source | object | Yes | Properties of the distributed data object. |

**Return value**

| Type | Description |
| :-- | :-- |
| [DistributedObject](#distributedobjectdeprecated) | Distributed data object created. |

**Example**

class SourceObject {
    name: string
    age: number
    isVis: boolean

    constructor(name: string, age: number, isVis: boolean) {
        this.name = name
        this.age = age
        this.isVis = isVis
    }
}

let source: SourceObject = new SourceObject("jack", 18, false);
let g\_object: distributedDataObject.DistributedObject = distributedDataObject.createDistributedObject(source);

#### DistributedObject(deprecated)

Provides APIs for managing a distributed data object. Before using any API of this class, use [createDistributedObject()](#distributeddataobjectcreatedistributedobjectdeprecated) to create a **DistributedObject** object.

#### \[h2\]setSessionId(deprecated)

setSessionId(sessionId?: string): boolean

Sets a session ID. For the devices in the collaboration state in a trusted network, data of the distributed objects with the same session ID can be automatically synced across devices.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c1/v3/FTt2W5h3QOyYtyX-9CV0gw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062215Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=4E7EDA1202EEE88AF7F3AAA90DA205D99F4323964EF636E485EB443B0F0AA664)

This API is supported since API version 8 and deprecated since API version 9. You are advised to use [setSessionId](#setsessionid9) instead.

**Required permissions**: ohos.permission.DISTRIBUTED\_DATASYNC

**System capability**: SystemCapability.DistributedDataManager.DataObject.DistributedObject

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| sessionId | string | No | ID of a distributed data object on a trusted network. To remove a distributed data object from the network, set this parameter to **""** or leave it empty. |

**Return value**

| Type | Description |
| :-- | :-- |
| boolean | 
Returns **true** if the session ID is set successfully;

returns **false** otherwise.

 |

**Example**

class SourceObject {
    name: string
    age: number
    isVis: boolean

    constructor(name: string, age: number, isVis: boolean) {
        this.name = name
        this.age = age
        this.isVis = isVis
    }
}

let source: SourceObject = new SourceObject("jack", 18, false);
let g\_object: distributedDataObject.DistributedObject = distributedDataObject.createDistributedObject(source);
// Add g\_object to the distributed network.
g\_object.setSessionId(distributedDataObject.genSessionId());
// Remove g\_object from the distributed network.
g\_object.setSessionId("");

#### \[h2\]on('change')(deprecated)

on(type: 'change', callback: (sessionId: string, fields: Array<string>) => void): void

Subscribes to data changes of this distributed data object.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/88/v3/s42eq_dFQpaAa9Lu8qfb8g/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062215Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=851655FB052756EFA3DF3B5EAD4A8CBF91BFC0498C3CAF11C43873397A343335)

This API is supported since API version 8 and deprecated since API version 9. You are advised to use [on('change')](#onchange9) instead.

**System capability**: SystemCapability.DistributedDataManager.DataObject.DistributedObject

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Event type. The value is **'change'**, which indicates data changes. |
| callback | (sessionId: string, fields: Array<string>) => void | Yes | 
Callback used to return the changes of the distributed data object.

**sessionId** indicates the session ID of the distributed data object.

**fields** indicates the changed properties of the distributed data object.

 |

**Example**

class SourceObject {
    name: string
    age: number
    isVis: boolean

    constructor(name: string, age: number, isVis: boolean) {
        this.name = name
        this.age = age
        this.isVis = isVis
    }
}

let source: SourceObject = new SourceObject("jack", 18, false);
let g\_object: distributedDataObject.DistributedObject = distributedDataObject.createDistributedObject(source);
g\_object.on("change", (sessionId: string, fields: Array<string>) => {
    console.info("change" + sessionId);
    if (fields != null && fields != undefined) {
        for (let index: number = 0; index < fields.length; index++) {
            console.info("changed !" + fields\[index\] + " " + g\_object\[fields\[index\]\]);
        }
    }
});

#### \[h2\]off('change')(deprecated)

off(type: 'change', callback?: (sessionId: string, fields: Array<string>) => void): void

Unsubscribes from data changes of this distributed data object.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5/v3/tJKDdqEyS9Cwo6lAWQMJ_g/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062215Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=29DDA1828D90F0C0B680D9C8EB11675FB321DE6CEB1810339DFDF3B7F6822E06)

This API is supported since API version 8 and deprecated since API version 9. You are advised to use [off('change')](#offchange9) instead.

**System capability**: SystemCapability.DistributedDataManager.DataObject.DistributedObject

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Event type. The value is **'change'**, which indicates data changes. |
| callback | (sessionId: string, fields: Array<string>) => void | No | 
Callback to unregister. If this parameter is not specified, this API unsubscribes from all callbacks for data changes of this distributed object.

**sessionId** indicates the session ID of the distributed data object.

**fields** indicates the changed properties of the distributed data object.

 |

**Example**

class SourceObject {
    name: string
    age: number
    isVis: boolean

    constructor(name: string, age: number, isVis: boolean) {
        this.name = name
        this.age = age
        this.isVis = isVis
    }
}

let source: SourceObject = new SourceObject("jack", 18, false);
let g\_object: distributedDataObject.DistributedObject = distributedDataObject.createDistributedObject(source);
// Unregister the specified data change callback.
g\_object.off("change", (sessionId: string, fields: Array<string>) => {
    console.info("change" + sessionId);
    if (fields != null && fields != undefined) {
        for (let index: number = 0; index < fields.length; index++) {
            console.info("changed !" + fields\[index\] + " " + g\_object\[fields\[index\]\]);
        }
    }
});
// Unregister all data change callbacks.
g\_object.off("change");

#### \[h2\]on('status')(deprecated)

on(type: 'status', callback: (sessionId: string, networkId: string, status: 'online' | 'offline' ) => void): void

Subscribes to status changes of this distributed data object.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4c/v3/wwUzN78kT8eHZRjDSSbYlg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062215Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=4603EE1AD672FFA7D8C0FED495237BE136AD341254D5102C38D2FE8016851CEB)

This API is supported since API version 8 and deprecated since API version 9. You are advised to use [on('status')](#onstatus9) instead.

**System capability**: SystemCapability.DistributedDataManager.DataObject.DistributedObject

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Event type. The value is **'status'**, which indicates the status change (online or offline) of the distributed object. |
| callback | (sessionId: string, networkId: string, status: 'online' | 'offline' ) => void | Yes | 
Callback used to return the status change.

**sessionId** indicates the session ID of the distributed data object.

**networkId** identifies the device.

**status** indicates the object status, which can be online or offline.

 |

**Example**

class SourceObject {
    name: string
    age: number
    isVis: boolean

    constructor(name: string, age: number, isVis: boolean) {
        this.name = name
        this.age = age
        this.isVis = isVis
    }
}

let source: SourceObject = new SourceObject("jack", 18, false);
let g\_object: distributedDataObject.DistributedObject = distributedDataObject.createDistributedObject(source);

g\_object.on("status", (sessionId: string, networkId: string, status: 'online' | 'offline') => {
    console.info("status changed " + sessionId + " " + status + " " + networkId);
});

#### \[h2\]off('status')(deprecated)

off(type: 'status', callback?: (sessionId: string, networkId: string, status: 'online' | 'offline' ) => void): void

Unsubscribes from the status change of this distributed data object.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/46/v3/qQoxvhm9Qm-qvmi9sQgGMg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062215Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=7C1E45EF660331296E0FBDF3C4A0F6935A21DD76DD0F1A81DAEC687ED8E94B1F)

This API is supported since API version 8 and deprecated since API version 9. You are advised to use [off('status')](#offstatus9) instead.

**System capability**: SystemCapability.DistributedDataManager.DataObject.DistributedObject

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Event type. The value is **'status'**, which indicates the status change (online or offline) of the distributed object. |
| callback | (sessionId: string, networkId: string, status: 'online' | 'offline' ) => void | No | 
Callback to unregister. If this parameter is not specified, this API unsubscribes from all callbacks for status changes of this distributed object.

**sessionId** indicates the session ID of the distributed data object.

**networkId** identifies the distributed data object.

**status** indicates the object status, which can be online or offline.

 |

**Example**

class SourceObject {
    name: string
    age: number
    isVis: boolean

    constructor(name: string, age: number, isVis: boolean) {
        this.name = name
        this.age = age
        this.isVis = isVis
    }
}

let source: SourceObject = new SourceObject("jack", 18, false);
let g\_object: distributedDataObject.DistributedObject = distributedDataObject.createDistributedObject(source);
// Unregister the specified status change callback.
g\_object.off("status", (sessionId: string, networkId: string, status: 'online' | 'offline') => {
    console.info("status changed " + sessionId + " " + status + " " + networkId);
});
// Unregister all status change callbacks.
g\_object.off("status");
