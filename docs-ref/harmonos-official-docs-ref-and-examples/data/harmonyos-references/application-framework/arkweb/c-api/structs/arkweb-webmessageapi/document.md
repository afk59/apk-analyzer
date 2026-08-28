# ArkWeb\_WebMessageAPI

typedef struct {...} ArkWeb\_WebMessageAPI

#### Overview

Defines a native API for the post message. Before calling this API, you are advised to use [ARKWEB\_MEMBER\_MISSING](../../header-files/arkweb-type-h/document.md#macros) to check whether the function struct has the corresponding pointer to avoid crash caused by mismatch between the SDK and the device ROM. The WebMessage APIs must be called on the UI thread through **OH\_ArkWeb\_GetNativeAPI**.

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
| [ArkWeb\_WebMessagePtr (\*createWebMessage)()](#createwebmessage) | Creates a message. |
| [void (\*destroyWebMessage)(ArkWeb\_WebMessagePtr\* webMessage)](#destroywebmessage) | Destroys a message. |
| [void (\*setType)(ArkWeb\_WebMessagePtr webMessage, ArkWeb\_WebMessageType type)](#settype) | Sets the message type. |
| [ArkWeb\_WebMessageType (\*getType)(ArkWeb\_WebMessagePtr webMessage)](#gettype) | Obtains the message type. |
| [void (\*setData)(ArkWeb\_WebMessagePtr webMessage, void\* data, size\_t dataLength)](#setdata) | Sets data. |
| [void\* (\*getData)(ArkWeb\_WebMessagePtr webMessage, size\_t\* dataLength)](#getdata) | Obtains data. |

#### Member Function Description

#### \[h2\]createWebMessage()

ArkWeb\_WebMessagePtr (\*createWebMessage)()

**Description**

Creates a message.

**Returns**

| Type | Description |
| :-- | :-- |
| [ArkWeb\_WebMessagePtr](../arkweb-webmessage/document.md) | Message struct. |

#### \[h2\]destroyWebMessage()

void (\*destroyWebMessage)(ArkWeb\_WebMessagePtr\* webMessage)

**Description**

Destroys a message.

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkWeb\_WebMessagePtr](../arkweb-webmessage/document.md)\* webMessage | Pointer to the message to destroy. |

#### \[h2\]setType()

void (\*setType)(ArkWeb\_WebMessagePtr webMessage, ArkWeb\_WebMessageType type)

**Description**

Sets the message type. @param webMessage Pointer to the message struct. @param type Message type.

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkWeb\_WebMessagePtr](../arkweb-webmessage/document.md) webMessage | Pointer to the message struct. |
| [ArkWeb\_WebMessageType](../../header-files/arkweb-type-h/document.md#arkweb_webmessagetype) type | Message type. |

#### \[h2\]getType()

ArkWeb\_WebMessageType (\*getType)(ArkWeb\_WebMessagePtr webMessage)

**Description**

Obtains the message type.

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkWeb\_WebMessagePtr](../arkweb-webmessage/document.md) webMessage | Pointer to the message struct. |

#### \[h2\]setData()

void (\*setData)(ArkWeb\_WebMessagePtr webMessage, void\* data, size\_t dataLength)

**Description**

Sets data.

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkWeb\_WebMessagePtr](../arkweb-webmessage/document.md) webMessage | Pointer to the message struct. |
| void\* data | Pointer to the data. |
| size\_t dataLength | Data length. |

#### \[h2\]getData()

void\* (\*getData)(ArkWeb\_WebMessagePtr webMessage, size\_t\* dataLength)

**Description**

Obtains data.

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkWeb\_WebMessagePtr](../arkweb-webmessage/document.md) webMessage | Pointer to the message struct. |
| size\_t\* dataLength | Data length, which is an output parameter. |

**Returns**

| Type | Description |
| :-- | :-- |
| void\* | Pointer to the data. |
