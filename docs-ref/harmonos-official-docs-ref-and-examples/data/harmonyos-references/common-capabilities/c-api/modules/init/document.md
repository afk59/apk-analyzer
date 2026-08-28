# Init

#### Overview

Provides the API for querying the support for a SystemCapability (SysCap), which refers to a standalone feature in the operating system. Different devices support different SysCap sets. Each SysCap corresponds to one or more APIs.

The result is returned after the SysCap configuration file is checked.

**Since**

8

#### Summary

#### \[h2\]Files

| Name | Description |
| :-- | :-- |
| [syscap\_ndk.h](../../header-files/syscap-ndk-h/document.md) | 
Provides the API for querying whether a SysCap is supported.

**File to include**: <syscap\_ndk.h>

**Library**: libdeviceinfo\_ndk.z.so

 |

#### \[h2\]Functions

| Name | Description |
| :-- | :-- |
| [canIUse](#caniuse) (const char \*cap) | Checks whether a SysCap is supported. |

#### Function Description

#### \[h2\]canIUse()

bool canIUse (const char \* cap)

**Description**

Checks whether a SysCap is supported.

**Parameters**

| Name | Description |
| :-- | :-- |
| cap | Pointer to the SysCap to check. |

**Returns**

| Type | Description |
| :-- | :-- |
| bool | Returns **true** if the SysCap is supported; returns **false** otherwise. |
