# os\_account.h

#### Overview

Defines the APIs for accessing and managing system account information.

**Library**: libos\_account\_ndk.so

**Header file**: <BasicServicesKit/os\_account.h>

**System capability**: SystemCapability.Account.OsAccount

**Since**: 12

**Related module**: [OsAccount](../../modules/osaccount/document.md)

#### Summary

#### \[h2\]Functions

| Name | Description |
| :-- | :-- |
| [OsAccount\_ErrCode OH\_OsAccount\_GetName(char \*buffer, size\_t buffer\_size)](#oh_osaccount_getname) | Obtains the name of the system account to which the caller process belongs. |

#### Function Description

#### \[h2\]OH\_OsAccount\_GetName()

OsAccount\_ErrCode OH\_OsAccount\_GetName(char \*buffer, size\_t buffer\_size)

**Description**

Obtains the name of the system account to which the caller process belongs.

**System capability**: SystemCapability.Account.OsAccount

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| char \*buffer | Pointer to the system account name, which including the name of the maximum length (**LOGIN\_NAME\_MAX**) and the end character (**\\0**). |
| size\_t buffer\_size | Length of the system account name. |

**Returns**

| Type | Description |
| :-- | :-- |
| [OsAccount\_ErrCode](../os-account-common-h/document.md#osaccount_errcode) | 
**OS\_ACCOUNT\_ERR\_OK**: Operation successful.

**OS\_ACCOUNT\_ERR\_INTERNAL\_ERROR**: Internal error.

**OS\_ACCOUNT\_ERR\_INVALID\_PARAMETER**: Invalid parameter, indicating that the buffer is a null pointer, or the length of the system account name (excluding **\\0**) is greater than or equal to the buffer size.

 |
