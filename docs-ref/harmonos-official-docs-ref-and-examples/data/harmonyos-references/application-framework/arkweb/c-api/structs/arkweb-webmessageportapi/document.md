# ArkWeb\_WebMessagePortAPI

typedef struct {...} ArkWeb\_WebMessagePortAPI

#### Overview

Defines a native API struct of the post message. Before calling this API, you are advised to use [ARKWEB\_MEMBER\_MISSING](../../header-files/arkweb-type-h/document.md#macros) to check whether the function struct has the corresponding pointer to avoid crash caused by mismatch between the SDK and the device ROM. The WebMessagePort APIs must be called on the UI thread through **OH\_ArkWeb\_GetNativeAPI**.

**Since**: 12

**Related module**: [Web](../../modules/web/document.md)

**Header file**: [arkweb\_type.h](../../header-files/arkweb-type-h/document.md)

#### Summary

#### \[h2\]Member Variables

| Name | Description |
| :-- | :-- |
| size\_t size | Size of the struct. |

#### \[h2\]Member Functions

| Name | Description |
| :-- | :-- |
| [ArkWeb\_ErrorCode (\*postMessage)(const ArkWeb\_WebMessagePortPtr webMessagePort, const char\* webTag, const ArkWeb\_WebMessagePtr webMessage)](#postmessage) | Sends a message to the HTML page. |
| [void (\*close)(const ArkWeb\_WebMessagePortPtr webMessagePort, const char\* webTag)](#close) | Closes a message port. |
| [void (\*setMessageEventHandler)(const ArkWeb\_WebMessagePortPtr webMessagePort, const char\* webTag, ArkWeb\_OnMessageEventHandler messageEventHandler, void\* userData)](#setmessageeventhandler) | Sets a callback for receiving HTML messages. |

#### Member Function Description

#### \[h2\]postMessage()

ArkWeb\_ErrorCode (\*postMessage)(const ArkWeb\_WebMessagePortPtr webMessagePort, const char\* webTag, const ArkWeb\_WebMessagePtr webMessage)

**Description**

Sends a message to the HTML page.

**Parameters**

| Name | Description |
| :-- | :-- |
| const [ArkWeb\_WebMessagePortPtr](../arkweb-webmessageport/document.md) webMessagePort | Pointer to the message port. |
| const char\* webTag | Name of the **Web** component. |
| const [ArkWeb\_WebMessagePtr](../arkweb-webmessage/document.md) webMessage | Message to send. |

**Returns**

| Type | Description |
| :-- | :-- |
| [ArkWeb\_ErrorCode](../../header-files/arkweb-error-code-h/document.md#arkweb_errorcode) | 
[ARKWEB\_SUCCESS](../../header-files/arkweb-error-code-h/document.md#arkweb_errorcode): The operation is successful.

[ARKWEB\_INVALID\_PARAM](../../header-files/arkweb-error-code-h/document.md#arkweb_errorcode): The parameter is invalid.

[ARKWEB\_INIT\_ERROR](../../header-files/arkweb-error-code-h/document.md#arkweb_errorcode): The initialization fails because the **Web** component bound to **webTag** is not found.

 |

#### \[h2\]close()

void (\*close)(const ArkWeb\_WebMessagePortPtr webMessagePort, const char\* webTag)

**Description**

Closes a message port.

**Parameters**

| Name | Description |
| :-- | :-- |
| const [ArkWeb\_WebMessagePortPtr](../arkweb-webmessageport/document.md) webMessagePort | Pointer to the message port. |
| const char\* webTag | Name of the **Web** component. |

#### \[h2\]setMessageEventHandler()

void (\*setMessageEventHandler)(const ArkWeb\_WebMessagePortPtr webMessagePort, const char\* webTag,
        ArkWeb\_OnMessageEventHandler messageEventHandler, void\* userData)

**Description**

Sets a callback for receiving HTML messages.

**Parameters**

| Name | Description |
| :-- | :-- |
| const [ArkWeb\_WebMessagePortPtr](../arkweb-webmessageport/document.md) webMessagePort | Pointer to the message port. |
| const char\* webTag | Name of the **Web** component. |
| [ArkWeb\_OnMessageEventHandler](../../header-files/arkweb-type-h/document.md#arkweb_onmessageeventhandler) messageEventHandler | Callback used to handle messages. |
| void\* userData | User-defined data. |
