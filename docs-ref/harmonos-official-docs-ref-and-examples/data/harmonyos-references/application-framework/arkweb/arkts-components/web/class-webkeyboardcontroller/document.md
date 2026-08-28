# Class (WebKeyboardController)

Implements a controller to control the input, deletion, and closure of the custom keyboard. For details about the sample code, see [onInterceptKeyboardAttach](../events/document.md#oninterceptkeyboardattach12).

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4c/v3/9i0YF87dRm2yfVYyuBZJlQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062315Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=E73FB81B26B5E861EC525AE90F03DF5C5663B7C72A528029BC9F8046803B7EF0)

-   The initial APIs of this component are supported since API version 8. Updates will be marked with a superscript to indicate their earliest API version.
    
-   The initial APIs of this class are supported since API version 12.
    
-   The sample effect is subject to the actual device.
    

#### constructor12+

constructor()

Constructs a **WebKeyboardController** API.

**System capability**: SystemCapability.Web.Webview.Core

#### insertText12+

insertText(text: string): void

Inserts characters into the **Web** component text box.

**System capability**: SystemCapability.Web.Webview.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| text | string | Yes | Characters to insert into the **Web** component text box. |

#### deleteForward12+

deleteForward(length: number): void

Deletes a specified number of characters forward in a **Web** component text box.

**System capability**: SystemCapability.Web.Webview.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| length | number | Yes | 
Length of characters to delete forward in a **Web** component text box.

Value range: \[-2147483648, 2147483647\]. If the parameter value exceeds the character length, all characters before the cursor are deleted by default. If the parameter value is a negative number, the deletion is not performed.

 |

#### deleteBackward12+

deleteBackward(length: number): void

Deletes a specified number of characters backward in a **Web** component text box.

**System capability**: SystemCapability.Web.Webview.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| length | number | Yes | 
Length of characters to delete backward in a **Web** component text box.

Value range: \[-2147483648, 2147483647\]. If the parameter value exceeds the character length, all characters after the cursor are deleted by default. If the parameter value is a negative number, the deletion is not performed.

 |

#### sendFunctionKey12+

sendFunctionKey(key: number): void

Inserts a function key. Currently, only the Enter key type is supported. For details about the value, see [EnterKeyType](../../../../ime-kit/arkts-apis/ohos-inputmethod-input-method-framework/document.md#enterkeytype10).

**System capability**: SystemCapability.Web.Webview.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| key | number | Yes | Function key to insert into the **Web** component text box. Currently, only the Enter key is supported. |

#### close12+

close(): void

Closes this custom keyboard.

**System capability**: SystemCapability.Web.Webview.Core
