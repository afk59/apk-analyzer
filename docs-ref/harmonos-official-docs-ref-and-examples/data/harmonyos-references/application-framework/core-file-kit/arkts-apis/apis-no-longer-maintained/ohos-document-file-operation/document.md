# @ohos.document (File Operation)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4f/v3/-E0IccfmRTa7v_MzM_SIFg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062320Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=20C9EE1AFF2B7C5A8E56F33A96F98BED47BF45E374C32C974B2780F14EE57F4C)

-   The initial APIs of this module are supported since API version 6. Newly added APIs will be marked with a superscript to indicate their earliest API version.
-   The APIs of this module have been deprecated since API version 9 and are not recommended for use. An exception will be thrown if any of the APIs is called.

#### Modules to Import

import document from '@ohos.document';

#### document.choose(deprecated)

choose(types?: string\[\]): Promise<string>

Chooses files of the specified types. This API uses a promise to return the result.

**System capability**: SystemCapability.FileManagement.UserFileService

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| types | string\[\] | No | Types of the files to choose. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<string> | Promise used to return the result. An error code is returned. |

**Example**

let types: Array<string> = \[\];
document.choose(types);

#### document.choose(deprecated)

choose(callback:AsyncCallback<string>): void

Chooses a file. This API uses an asynchronous callback to return the result.

**System capability**: SystemCapability.FileManagement.UserFileService

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | AsyncCallback<string> | Yes | Callback used to return the result. An error code is returned. |

**Example**

let uri: string = "";
document.choose((err: TypeError, uri: string) => {
  // Do something with the URI.
});

#### document.choose(deprecated)

choose(types:string\[\], callback:AsyncCallback<string>): void

Chooses files of the specified types. This API uses an asynchronous callback to return the result.

**System capability**: SystemCapability.FileManagement.UserFileService

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| types | string\[\] | Yes | Types of the files to choose. |
| callback | AsyncCallback<string> | Yes | Callback used to return the result. An error code is returned. |

**Example**

let types: Array<string> = \[\];
let uri: string = "";
document.choose(types, (err: TypeError, uri: string) => {
  // Do something with the URI.
});

#### document.show(deprecated)

show(uri:string, type:string):Promise<void>

Opens a file. This API uses a promise to return the result.

**System capability**: SystemCapability.FileManagement.UserFileService

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| uri | string | Yes | URI of the file to open. |
| type | string | Yes | Type of the file to open. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise used to return the result. An error code is returned. |

**Example**

let type: string = "";
let uri: string = "";
document.show(uri, type);

#### document.show(deprecated)

show(uri:string, type:string, callback:AsyncCallback<void>): void

Opens a file. This API uses an asynchronous callback to return the result.

**System capability**: SystemCapability.FileManagement.UserFileService

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| uri | string | Yes | URI of the file to open. |
| type | string | Yes | Type of the file to open. |
| callback | AsyncCallback<void> | Yes | Callback used to return the result. An error code is returned. |

**Example**

let type: string = "";
let uri: string = "";
document.show(uri, type, (err: TypeError) => {
  //do something
});
