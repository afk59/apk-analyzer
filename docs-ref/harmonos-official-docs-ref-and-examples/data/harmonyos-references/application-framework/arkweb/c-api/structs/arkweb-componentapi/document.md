# ArkWeb\_ComponentAPI

typedef struct {...} ArkWeb\_ComponentAPI

#### Overview

Defines a native component API.

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
| [void (\*onControllerAttached)(const char\* webTag, ArkWeb\_OnComponentCallback callback, void\* userData)](#oncontrollerattached) | Triggered when a controller is attached to the **Web** component. |
| [void (\*onPageBegin)(const char\* webTag, ArkWeb\_OnComponentCallback callback, void\* userData)](#onpagebegin) | Triggered when the web page starts to be loaded. This callback is called only for the main frame content, and not for the iframe or frameset content. |
| [void (\*onPageEnd)(const char\* webTag, ArkWeb\_OnComponentCallback callback, void\* userData)](#onpageend) | Triggered when the web page loading is finished. This callback is called only for the main frame content, and not for the iframe or frameset content. |
| [void (\*onDestroy)(const char\* webTag, ArkWeb\_OnComponentCallback callback, void\* userData)](#ondestroy) | Triggered when this **Web** component is destroyed. |

#### Member Function Description

#### \[h2\]onControllerAttached()

void (\*onControllerAttached)(const char\* webTag, ArkWeb\_OnComponentCallback callback, void\* userData)

**Description**

Triggered when a controller is attached to the **Web** component.

**Parameters**

| Name | Description |
| :-- | :-- |
| const char\* webTag | Name of the **Web** component. |
| ArkWeb\_OnComponentCallback callback | Callback of **onControllerAttached**. |
| void\* userData | User-defined data. |

#### \[h2\]onPageBegin()

void (\*onPageBegin)(const char\* webTag, ArkWeb\_OnComponentCallback callback, void\* userData)

**Description**

Triggered when the web page starts to be loaded. This callback is called only for the main frame content, and not for the iframe or frameset content.

**Parameters**

| Name | Description |
| :-- | :-- |
| const char\* webTag | Name of the **Web** component. |
| ArkWeb\_OnComponentCallback callback | Callback of **onPageBegin**. |
| void\* userData | User-defined data. |

#### \[h2\]onPageEnd()

void (\*onPageEnd)(const char\* webTag, ArkWeb\_OnComponentCallback callback, void\* userData)

**Description**

Triggered when the web page loading is finished. This callback is called only for the main frame content, and not for the iframe or frameset content.

**Parameters**

| Name | Description |
| :-- | :-- |
| const char\* webTag | Name of the **Web** component. |
| ArkWeb\_OnComponentCallback callback | Callback of **onPageEnd**. |
| void\* userData | User-defined data. |

#### \[h2\]onDestroy()

void (\*onDestroy)(const char\* webTag, ArkWeb\_OnComponentCallback callback, void\* userData)

**Description**

Triggered when this **Web** component is destroyed.

**Parameters**

| Name | Description |
| :-- | :-- |
| const char\* webTag | Name of the **Web** component. |
| ArkWeb\_OnComponentCallback callback | Callback of **onDestroy**. |
| void\* userData | User-defined data. |
