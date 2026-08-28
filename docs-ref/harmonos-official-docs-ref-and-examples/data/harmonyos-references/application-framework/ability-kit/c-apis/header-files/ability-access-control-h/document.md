# ability\_access\_control.h

#### Overview

Declares the APIs for implementing application access control.

**Library**: ability\_access\_control.so

**File to include**: <accesstoken/ability\_access\_control.h>

**System capability**: SystemCapability.Security.AccessToken

**Since**: 12

**Related module**: [AbilityAccessControl](../../modules/abilityaccesscontrol/document.md)

#### Summary

#### \[h2\]Functions

| Name | Description |
| :-- | :-- |
| [bool OH\_AT\_CheckSelfPermission(const char \*permission)](#oh_at_checkselfpermission) | Checks whether a permission is granted to this application. |

#### Function Description

#### \[h2\]OH\_AT\_CheckSelfPermission()

bool OH\_AT\_CheckSelfPermission(const char \*permission)

**Description**

Checks whether a permission is granted to this application.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| const char \*permission | Pointer to the permission to check. For details about the permission, see the application permission list. |

**Returns**

| Type | Description |
| :-- | :-- |
| bool | 
Returns **true** if the permission has been granted to the application.

Returns **false** otherwise.

 |
