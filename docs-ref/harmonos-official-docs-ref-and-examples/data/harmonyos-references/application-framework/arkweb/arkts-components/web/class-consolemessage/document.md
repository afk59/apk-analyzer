# Class (ConsoleMessage)

Implements the **ConsoleMessage** object. For details about the sample code, see [onConsole](../events/document.md#onconsole).

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/55/v3/Twzg4V5nSI2Y-EP4daC9ig/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062315Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=03E7C5EAAB463829272C92541A5703962F3E139E3EB092AC5D21C39D8D5255BC)

-   The initial APIs of this component are supported since API version 8. Updates will be marked with a superscript to indicate their earliest API version.
    
-   The initial APIs of this class are supported since API version 8.
    
-   The sample effect is subject to the actual device.
    

#### constructor(deprecated)

constructor(message: string, sourceId: string, lineNumber: number, messageLevel: MessageLevel)

Constructs a **ConsoleMessage** object.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2c/v3/OvY7KQs4SW--T-FMB-2fdA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062315Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=DF22FAAA003C0B197BD36E755D64D46AB40FA8F1F9CC90DD5CF5B4767BA4571D)

This API is supported since API version 8 and deprecated since API version 9. You are advised to use [constructor](#constructor9) instead.

**System capability**: SystemCapability.Web.Webview.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| message | string | Yes | Log output information of **ConsoleMessage**. |
| sourceId | string | Yes | Path and name of the web page source file. |
| lineNumber | number | Yes | Line number of **ConsoleMessage**. |
| messageLevel | [MessageLevel](../enums/document.md#messagelevel) | Yes | Log level of **ConsoleMessage**. |

#### constructor9+

constructor()

Constructs a **ConsoleMessage** object.

**System capability**: SystemCapability.Web.Webview.Core

#### getLineNumber

getLineNumber(): number

Obtains the number of rows in this console message.

**System capability**: SystemCapability.Web.Webview.Core

**Return value**

| Type | Description |
| :-- | :-- |
| number | Number of rows in the console message. |

#### getMessage

getMessage(): string

Obtains the log information of this console message.

**System capability**: SystemCapability.Web.Webview.Core

**Return value**

| Type | Description |
| :-- | :-- |
| string | Log information of the console message. |

#### getMessageLevel

getMessageLevel(): MessageLevel

Obtains the level of this console message.

**System capability**: SystemCapability.Web.Webview.Core

**Return value**

| Type | Description |
| :-- | :-- |
| [MessageLevel](../enums/document.md#messagelevel) | Level of the console message. |

#### getSourceId

getSourceId(): string

Obtains the path and name of the web page source file.

**System capability**: SystemCapability.Web.Webview.Core

**Return value**

| Type | Description |
| :-- | :-- |
| string | Path and name of the web page source file. |
