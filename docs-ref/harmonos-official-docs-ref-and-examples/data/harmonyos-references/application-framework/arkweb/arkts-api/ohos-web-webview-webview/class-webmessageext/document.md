# Class (WebMessageExt)

Implements a **WebMessageExt** object that received and sent by the [WebMessagePort](../interface-webmessageport/document.md) API.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/73/v3/tPkxw9RARO-zxXt5gCEKEQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062313Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=F8211B1A06397CCF3EF63800244E54939D0066E3D0881E5DEB36993EB402ADE6)

-   The initial APIs of this module are supported since API version 9. Updates will be marked with a superscript to indicate their earliest API version.
    
-   The initial APIs of this class are supported since API version 10.
    
-   The sample effect is subject to the actual device.
    

#### getType10+

getType(): WebMessageType

Obtains the type of the data object. For details about the sample code, see [onMessageEventExt](../interface-webmessageport/document.md#onmessageeventext10).

**System capability**: SystemCapability.Web.Webview.Core

**Return value**

| Type | Description |
| :-- | :-- |
| [WebMessageType](../enums/document.md#webmessagetype10) | Data types supported by the [webMessagePort](../interface-webmessageport/document.md) API. |

#### getString10+

getString(): string

Obtains string-type data of the data object. For details about the sample code, see [onMessageEventExt](../interface-webmessageport/document.md#onmessageeventext10).

**System capability**: SystemCapability.Web.Webview.Core

**Return value**

| Type | Description |
| :-- | :-- |
| string | Data of the string type. |

**Error codes**

For details about the error codes, see [Webview Error Codes](../../../error-codes/webview-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 17100014 | The type and value of the message do not match. |

#### getNumber10+

getNumber(): number

Obtains number-type data of the data object. For details about the sample code, see [onMessageEventExt](../interface-webmessageport/document.md#onmessageeventext10).

**System capability**: SystemCapability.Web.Webview.Core

**Return value**

| Type | Description |
| :-- | :-- |
| number | Data of the number type. |

**Error codes**

For details about the error codes, see [Webview Error Codes](../../../error-codes/webview-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 17100014 | The type and value of the message do not match. |

#### getBoolean10+

getBoolean(): boolean

Obtains Boolean-type data of the data object. For details about the sample code, see [onMessageEventExt](../interface-webmessageport/document.md#onmessageeventext10).

**System capability**: SystemCapability.Web.Webview.Core

**Return value**

| Type | Description |
| :-- | :-- |
| boolean | Data of the Boolean type. |

**Error codes**

For details about the error codes, see [Webview Error Codes](../../../error-codes/webview-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 17100014 | The type and value of the message do not match. |

#### getArrayBuffer10+

getArrayBuffer(): ArrayBuffer

Obtains raw binary data of the data object. For details about the sample code, see [onMessageEventExt](../interface-webmessageport/document.md#onmessageeventext10).

**System capability**: SystemCapability.Web.Webview.Core

**Return value**

| Type | Description |
| :-- | :-- |
| ArrayBuffer | Raw binary data. |

**Error codes**

For details about the error codes, see [Webview Error Codes](../../../error-codes/webview-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 17100014 | The type and value of the message do not match. |

#### getArray10+

getArray(): Array<string | number | boolean>

Obtains array-type data of the data object. For details about the sample code, see [onMessageEventExt](../interface-webmessageport/document.md#onmessageeventext10).

**System capability**: SystemCapability.Web.Webview.Core

**Return value**

| Type | Description |
| :-- | :-- |
| Array<string | number | boolean> | Data of the array type. |

**Error codes**

For details about the error codes, see [Webview Error Codes](../../../error-codes/webview-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 17100014 | The type and value of the message do not match. |

#### getError10+

getError(): Error

Obtains the error-object-type data of the data object. For details about the sample code, see [onMessageEventExt](../interface-webmessageport/document.md#onmessageeventext10).

**System capability**: SystemCapability.Web.Webview.Core

**Return value**

| Type | Description |
| :-- | :-- |
| Error | Data of the error object type. |

**Error codes**

For details about the error codes, see [Webview Error Codes](../../../error-codes/webview-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 17100014 | The type and value of the message do not match. |

#### setType10+

setType(type: WebMessageType): void

Sets the type for the data object. For details about the sample code, see [onMessageEventExt](../interface-webmessageport/document.md#onmessageeventext10).

**System capability**: SystemCapability.Web.Webview.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | [WebMessageType](../enums/document.md#webmessagetype10) | Yes | Data types supported by the [webMessagePort](../interface-webmessageport/document.md) API. |

**Error codes**

For details about the error codes, see [Webview Error Codes](../../../error-codes/webview-error-codes/document.md) and [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 17100014 | The type and value of the message do not match. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3.Parameter verification failed. |

#### setString10+

setString(message: string): void

Sets the string-type data of the data object. For details about the sample code, see [onMessageEventExt](../interface-webmessageport/document.md#onmessageeventext10).

**System capability**: SystemCapability.Web.Webview.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| message | string | Yes | String type. |

**Error codes**

For details about the error codes, see [Webview Error Codes](../../../error-codes/webview-error-codes/document.md) and [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 17100014 | The type and value of the message do not match. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3.Parameter verification failed. |

#### setNumber10+

setNumber(message: number): void

Sets the number-type data of the data object. For details about the sample code, see [onMessageEventExt](../interface-webmessageport/document.md#onmessageeventext10).

**System capability**: SystemCapability.Web.Webview.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| message | number | Yes | Data of the number type. |

**Error codes**

For details about the error codes, see [Webview Error Codes](../../../error-codes/webview-error-codes/document.md) and [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 17100014 | The type and value of the message do not match. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3.Parameter verification failed. |

#### setBoolean10+

setBoolean(message: boolean): void

Sets the Boolean-type data for the data object. For details about the sample code, see [onMessageEventExt](../interface-webmessageport/document.md#onmessageeventext10).

**System capability**: SystemCapability.Web.Webview.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| message | boolean | Yes | Data of the Boolean type. |

**Error codes**

For details about the error codes, see [Webview Error Codes](../../../error-codes/webview-error-codes/document.md) and [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 17100014 | The type and value of the message do not match. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3.Parameter verification failed. |

#### setArrayBuffer10+

setArrayBuffer(message: ArrayBuffer): void

Sets the raw binary data for the data object. For details about the sample code, see [onMessageEventExt](../interface-webmessageport/document.md#onmessageeventext10).

**System capability**: SystemCapability.Web.Webview.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| message | ArrayBuffer | Yes | Raw binary data. |

**Error codes**

For details about the error codes, see [Webview Error Codes](../../../error-codes/webview-error-codes/document.md) and [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 17100014 | The type and value of the message do not match. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3.Parameter verification failed. |

#### setArray10+

setArray(message: Array<string | number | boolean>): void

Sets the array-type data for the data object. For details about the sample code, see [onMessageEventExt](../interface-webmessageport/document.md#onmessageeventext10).

**System capability**: SystemCapability.Web.Webview.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| message | Array<string | number | boolean> | Yes | Data of the array type. |

**Error codes**

For details about the error codes, see [Webview Error Codes](../../../error-codes/webview-error-codes/document.md) and [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 17100014 | The type and value of the message do not match. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3.Parameter verification failed. |

#### setError10+

setError(message: Error): void

Sets the error-object-type data for the data object. For details about the sample code, see [onMessageEventExt](../interface-webmessageport/document.md#onmessageeventext10).

**System capability**: SystemCapability.Web.Webview.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| message | Error | Yes | Data of the error object type. |

**Error codes**

For details about the error codes, see [Webview Error Codes](../../../error-codes/webview-error-codes/document.md) and [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 17100014 | The type and value of the message do not match. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3.Parameter verification failed. |
