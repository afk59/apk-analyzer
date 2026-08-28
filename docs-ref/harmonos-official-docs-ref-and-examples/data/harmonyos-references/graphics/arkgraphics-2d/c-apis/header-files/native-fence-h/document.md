# native\_fence.h

#### Overview

This file declares the functions for obtaining and using **NativeFence**.

**Header file**: <native\_fence/native\_fence.h>

**Library**: libnative\_fence.so

**Since**: 20

**System capability**: SystemCapability.Graphic.Graphic2D.NativeWindow

**Related module**: [NativeFence](../../modules/nativefence/document.md)

#### Summary

#### \[h2\]Functions

| Name | Description |
| :-- | :-- |
| [bool OH\_NativeFence\_IsValid(int fenceFd)](#oh_nativefence_isvalid) | Checks whether **fenceFd** is valid. |
| [bool OH\_NativeFence\_Wait(int fenceFd, uint32\_t timeout)](#oh_nativefence_wait) | Blocks the input **fenceFd**. The maximum blocking time is determined by the timeout parameter. The input **fenceFd** needs to be closed by yourself. |
| [bool OH\_NativeFence\_WaitForever(int fenceFd)](#oh_nativefence_waitforever) | Permanently blocks the input **fenceFd**. The input **fenceFd** needs to be closed by yourself. |
| [void OH\_NativeFence\_Close(int fenceFd)](#oh_nativefence_close) | Closes **fenceFd**. |

#### Function Description

#### \[h2\]OH\_NativeFence\_IsValid()

bool OH\_NativeFence\_IsValid(int fenceFd)

**Description**

Checks whether **fenceFd** is valid.

**Since**: 20

**Parameters**

| Name | Description |
| :-- | :-- |
| int fenceFd | File descriptor for periodic sync. |

**Returns**

| Type | Description |
| :-- | :-- |
| bool | Returns **true** if **fenceFd** is valid; **false** otherwise. |

#### \[h2\]OH\_NativeFence\_Wait()

bool OH\_NativeFence\_Wait(int fenceFd, uint32\_t timeout)

**Description**

Blocks the input **fenceFd**. The maximum blocking time is determined by the timeout parameter. The input **fenceFd** needs to be closed by yourself.

**Since**: 20

**Parameters**

| Name | Description |
| :-- | :-- |
| int fenceFd | File descriptor for periodic sync. |
| uint32\_t timeout | Wait time. The unit is millisecond. The value **\-1** indicates that the API waits permanently, and the value **0** indicates that the API returns a response immediately. |

**Returns**

| Type | Description |
| :-- | :-- |
| bool | 
Returns **true** if the corresponding **fenceFd** has a signal triggered.

Returns **false** in the following cases:

1\. The input **fenceFd** is a negative integer.

2\. No signal is triggered within the specified timeout period.

3\. The underlying **poll** API fails to be called.

4\. The timeout period is set to **0**.

5\. The file descriptor fails to be copied in the API.

 |

#### \[h2\]OH\_NativeFence\_WaitForever()

bool OH\_NativeFence\_WaitForever(int fenceFd)

**Description**

Permanently blocks the input **fenceFd**. The input **fenceFd** needs to be closed by yourself.

**Since**: 20

**Parameters**

| Name | Description |
| :-- | :-- |
| int fenceFd | File descriptor for periodic sync. |

**Returns**

| Type | Description |
| :-- | :-- |
| bool | 
Returns **true** if the corresponding **fenceFd** has a signal triggered.

Returns **false** in the following cases:

1\. The input **fenceFd** is a negative integer.

2\. No signal is triggered within the specified timeout period, and the API waits permanently.

3\. The file descriptor fails to be copied in the API.

 |

#### \[h2\]OH\_NativeFence\_Close()

void OH\_NativeFence\_Close(int fenceFd)

**Description**

Closes **fenceFd**.

**Since**: 20

**Parameters**

| Name | Description |
| :-- | :-- |
| int fenceFd | File descriptor for periodic sync. The value is a non-negative integer. |
