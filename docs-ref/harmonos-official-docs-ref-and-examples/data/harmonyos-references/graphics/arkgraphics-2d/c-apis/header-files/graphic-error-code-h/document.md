# graphic\_error\_code.h

#### Overview

Defines error codes.

**File to include**: <native\_window/graphic\_error\_code.h>

**Library**: libnative\_window.so

**System capability**: SystemCapability.Graphic.Graphic2D.NativeWindow

**Since**: 12

**Related module**: [NativeWindow](../../modules/nativewindow/document.md)

#### Summary

#### \[h2\]Enumerated value

| Name | typedef Keyword | Description |
| :-- | :-- | :-- |
| [OHNativeErrorCode](#ohnativeerrorcode) | OHNativeErrorCode | Defines an enum for the error codes. |

#### Enum Description

#### \[h2\]OHNativeErrorCode

enum OHNativeErrorCode

**Description**

Defines an enum for the error codes.

**Since**: 12

| Value | Description |
| :-- | :-- |
| NATIVE\_ERROR\_OK = 0 | Operation successful. |
| NATIVE\_ERROR\_MEM\_OPERATION\_ERROR = 30001000 | 
An error occurs during memory manipulation.

**Since**: 15

 |
| NATIVE\_ERROR\_INVALID\_ARGUMENTS = 40001000 | An input parameter is invalid. |
| NATIVE\_ERROR\_NO\_PERMISSION = 40301000 | You do not have the permission to perform the operation. |
| NATIVE\_ERROR\_NO\_BUFFER = 40601000 | No buffer is available. |
| NATIVE\_ERROR\_NO\_CONSUMER = 41202000 | The consumer does not exist. |
| NATIVE\_ERROR\_NOT\_INIT = 41203000 | Not initialized. |
| NATIVE\_ERROR\_CONSUMER\_CONNECTED = 41206000 | The consumer is connected. |
| NATIVE\_ERROR\_BUFFER\_STATE\_INVALID = 41207000 | The buffer status does not meet the expectation. |
| NATIVE\_ERROR\_BUFFER\_IN\_CACHE = 41208000 | The buffer is already in the buffer queue. |
| NATIVE\_ERROR\_BUFFER\_QUEUE\_FULL = 41209000 | The queue is full. |
| NATIVE\_ERROR\_BUFFER\_NOT\_IN\_CACHE = 41210000 | The buffer is not in the buffer queue. |
| NATIVE\_ERROR\_CONSUMER\_DISCONNECTED = 41211000 | The consumer is disconnected. |
| NATIVE\_ERROR\_CONSUMER\_NO\_LISTENER\_REGISTERED = 41212000 | No listener is registered on the consumer side. |
| NATIVE\_ERROR\_UNSUPPORTED = 50102000 | The device or platform does not support the operation. |
| NATIVE\_ERROR\_UNKNOWN = 50002000 | Unknown error. Check the log. |
| NATIVE\_ERROR\_HDI\_ERROR = 50007000 | Failed to call the HDI. |
| NATIVE\_ERROR\_BINDER\_ERROR = 50401000 | Cross-process communication failed. |
| NATIVE\_ERROR\_EGL\_STATE\_UNKNOWN = 60001000 | The EGL environment is abnormal. |
| NATIVE\_ERROR\_EGL\_API\_FAILED = 60002000 | Failed to call the EGL APIs. |
