# Class (JsMessageExt)

Implements a **JsMessageExt** object that is returned after the [runJavaScriptExt](../class-webviewcontroller/document.md#runjavascriptext10) API is invoked.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5f/v3/8D7MWKI8RbqBBbIFvRrvUQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062312Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=7920728E846433B0C226DB6BB1E519E3F80B206D2A2290783018A618719637F6)

-   The initial APIs of this module are supported since API version 9. Updates will be marked with a superscript to indicate their earliest API version.
    
-   The initial APIs of this class are supported since API version 10.
    
-   The sample effect is subject to the actual device.
    

#### getType10+

getType(): JsMessageType

Obtains the type of the data object. For details about the sample code, see [runJavaScriptExt](../class-webviewcontroller/document.md#runjavascriptext10).

**System capability**: SystemCapability.Web.Webview.Core

**Return value**

| Type | Description |
| :-- | :-- |
| [JsMessageType](../enums/document.md#jsmessagetype10) | Data type of the result returned after the [runJavaScriptExt](../class-webviewcontroller/document.md#runjavascriptext10) API is executed. |

#### getString10+

getString(): string

Obtains string-type data of the data object. For details about the sample code, see [runJavaScriptExt](../class-webviewcontroller/document.md#runjavascriptext10).

**System capability**: SystemCapability.Web.Webview.Core

**Return value**

| Type | Description |
| :-- | :-- |
| string | Data of the string type. |

**Error codes**

For details about the error codes, see [Webview Error Codes](../../../error-codes/webview-error-codes/document.md).

| Error Code | Error Message |
| :-- | :-- |
| 17100014 | The type and value of the message do not match. |

#### getNumber10+

getNumber(): number

Obtains number-type data of the data object. For details about the sample code, see [runJavaScriptExt](../class-webviewcontroller/document.md#runjavascriptext10).

**System capability**: SystemCapability.Web.Webview.Core

**Return value**

| Type | Description |
| :-- | :-- |
| number | Data of the number type. |

**Error codes**

For details about the error codes, see [Webview Error Codes](../../../error-codes/webview-error-codes/document.md).

| Error Code | Error Message |
| :-- | :-- |
| 17100014 | The type and value of the message do not match. |

#### getBoolean10+

getBoolean(): boolean

Obtains Boolean-type data of the data object. For details about the sample code, see [runJavaScriptExt](../class-webviewcontroller/document.md#runjavascriptext10).

**System capability**: SystemCapability.Web.Webview.Core

**Return value**

| Type | Description |
| :-- | :-- |
| boolean | Data of the Boolean type. |

**Error codes**

For details about the error codes, see [Webview Error Codes](../../../error-codes/webview-error-codes/document.md).

| Error Code | Error Message |
| :-- | :-- |
| 17100014 | The type and value of the message do not match. |

#### getArrayBuffer10+

getArrayBuffer(): ArrayBuffer

Obtains raw binary data of the data object. For details about the sample code, see [runJavaScriptExt](../class-webviewcontroller/document.md#runjavascriptext10).

**System capability**: SystemCapability.Web.Webview.Core

**Return value**

| Type | Description |
| :-- | :-- |
| ArrayBuffer | Raw binary data. |

**Error codes**

For details about the error codes, see [Webview Error Codes](../../../error-codes/webview-error-codes/document.md).

| Error Code | Error Message |
| :-- | :-- |
| 17100014 | The type and value of the message do not match. |

#### getArray10+

getArray(): Array<string | number | boolean>

Obtains array-type data of the data object. For details about the sample code, see [runJavaScriptExt](../class-webviewcontroller/document.md#runjavascriptext10).

**System capability**: SystemCapability.Web.Webview.Core

**Return value**

| Type | Description |
| :-- | :-- |
| Array<string | number | boolean> | Data of the array type. |

**Error codes**

For details about the error codes, see [Webview Error Codes](../../../error-codes/webview-error-codes/document.md).

| Error Code | Error Message |
| :-- | :-- |
| 17100014 | The type and value of the message do not match. |

#### getErrorDescription22+

getErrorDescription(): string | null

Obtains the error information about the JavaScript execution. For details about the sample code, see [runJavaScriptExt](../class-webviewcontroller/document.md#runjavascriptext10).

**System capability**: SystemCapability.Web.Webview.Core

**Return value**

| Type | Description |
| :-- | :-- |
| string | null | If an exception occurs during JavaScript execution or the return value is of the object type, **"Not support type: <{exception\\object}>"** is returned. |
