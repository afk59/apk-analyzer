# arkweb\_interface.h

#### Overview

Declares ArkWeb APIs for obtaining native APIs and the basic native API types.

**File to include**: <web/arkweb\_interface.h>

**Library**: libohweb.so

**System capability**: SystemCapability.Web.Webview.Core

**Since**: 12

**Related module**: [Web](../../modules/web/document.md)

#### Summary

#### \[h2\]Structs

| Name | typedef Keyword | Description |
| :-- | :-- | :-- |
| [ArkWeb\_AnyNativeAPI](../../structs/arkweb-anynativeapi/document.md) | ArkWeb\_AnyNativeAPI | Defines the basic native API types. |

#### \[h2\]Enums

| Name | typedef Keyword | Description |
| :-- | :-- | :-- |
| [ArkWeb\_NativeAPIVariantKind](#arkweb_nativeapivariantkind) | ArkWeb\_NativeAPIVariantKind | Enumerates the native API types. |

#### \[h2\]Functions

| Name | Description |
| :-- | :-- |
| [ArkWeb\_AnyNativeAPI\* OH\_ArkWeb\_GetNativeAPI(ArkWeb\_NativeAPIVariantKind type)](#oh_arkweb_getnativeapi) | Obtains the native API struct based on the transferred API type. |
| [bool OH\_ArkWeb\_RegisterScrollCallback(const char\* webTag, ArkWeb\_OnScrollCallback callback, void\* userData)](#oh_arkweb_registerscrollcallback) | Registers a callback for the scroll event. |

#### Enum Description

#### \[h2\]ArkWeb\_NativeAPIVariantKind

enum ArkWeb\_NativeAPIVariantKind

**Description**

Enumerates the native API types.

**Since**: 12

| Enumerated Value | Description |
| :-- | :-- |
| ARKWEB\_NATIVE\_COMPONENT | APIs related to the **Web** component. |
| ARKWEB\_NATIVE\_CONTROLLER | APIs related to controller. |
| ARKWEB\_NATIVE\_WEB\_MESSAGE\_PORT | APIs related to **webMessagePort**. |
| ARKWEB\_NATIVE\_WEB\_MESSAGE | APIs related to **webMessage**. |
| ARKWEB\_NATIVE\_COOKIE\_MANAGER | APIs related to **cookieManager**. |
| ARKWEB\_NATIVE\_JAVASCRIPT\_VALUE | 
APIs related to **JavaScriptValue**.

**Since**: 18

 |

#### Function Description

#### \[h2\]OH\_ArkWeb\_GetNativeAPI()

ArkWeb\_AnyNativeAPI\* OH\_ArkWeb\_GetNativeAPI(ArkWeb\_NativeAPIVariantKind type)

**Description**

Obtains the native API struct based on the transferred API type.

**System capability**: SystemCapability.Web.Webview.Core

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [ArkWeb\_NativeAPIVariantKind](#arkweb_nativeapivariantkind) type | The native API types supported by ArkWeb. |

**Returns**

| Type | Description |
| :-- | :-- |
| [ArkWeb\_AnyNativeAPI](../../structs/arkweb-anynativeapi/document.md)\* | Native API struct pointer corresponding to the input API type. The first member of the struct is the size of the struct. |

#### \[h2\]OH\_ArkWeb\_RegisterScrollCallback()

bool OH\_ArkWeb\_RegisterScrollCallback(const char\* webTag, ArkWeb\_OnScrollCallback callback, void\* userData)

**Description**

Sets a callback for the scroll event.

**System capability**: SystemCapability.Web.Webview.Core

**Since**: 18

**Parameters**

| Name | Description |
| :-- | :-- |
| const char\* webTag | Name of the **Web** component. |
| [ArkWeb\_OnScrollCallback](../arkweb-type-h/document.md#arkweb_onscrollcallback) callback | Callback used when a page is scrolled. |
| void\* userData | Pointer to user-defined data. |

**Returns**

| Type | Description |
| :-- | :-- |
| bool | **true** is returned if the operation is successful; otherwise, **false** is returned. |
