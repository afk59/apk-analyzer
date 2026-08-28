# loop.h

#### Overview

The **loop.h** file declares the loop APIs in C.

**File to include**: <ffrt/loop.h>

**Library**: libffrt.z.so

**System capability**: SystemCapability.Resourceschedule.Ffrt.Core

**Since**: 12

**Related module**: [FFRT](../../modules/ffrt/document.md)

#### Summary

#### \[h2\]Structs

| Name | Description |
| :-- | :-- |
| [ffrt\_loop\_t](../../structs/ffrt-loop-t/document.md) | Defines the handle to a loop. |

#### \[h2\]Function

| Name | Description |
| :-- | :-- |
| [FFRT\_C\_API ffrt\_loop\_t ffrt\_loop\_create(ffrt\_queue\_t queue)](#ffrt_loop_create) | Creates a loop. |
| [FFRT\_C\_API int ffrt\_loop\_destroy(ffrt\_loop\_t loop)](#ffrt_loop_destroy) | Destroys a loop. |
| [FFRT\_C\_API int ffrt\_loop\_run(ffrt\_loop\_t loop)](#ffrt_loop_run) | Runs a loop. |
| [FFRT\_C\_API void ffrt\_loop\_stop(ffrt\_loop\_t loop)](#ffrt_loop_stop) | Stops a loop. |
| [FFRT\_C\_API int ffrt\_loop\_epoll\_ctl(ffrt\_loop\_t loop, int op, int fd, uint32\_t events, void \*data, ffrt\_poller\_cb cb)](#ffrt_loop_epoll_ctl) | 
Manages listening events on a loop.

You are not advised to call the exit function in cb. Otherwise, undefined behavior may occur.

 |
| [FFRT\_C\_API ffrt\_timer\_t ffrt\_loop\_timer\_start(ffrt\_loop\_t loop, uint64\_t timeout, void\* data, ffrt\_timer\_cb cb, bool repeat)](#ffrt_loop_timer_start) | 

Starts the timer on a loop.

You are not advised to call the exit function in cb. Otherwise, undefined behavior may occur.

 |
| [FFRT\_C\_API int ffrt\_loop\_timer\_stop(ffrt\_loop\_t loop, ffrt\_timer\_t handle)](#ffrt_loop_timer_stop) | Stops the timer on a loop. |

#### Function Description

#### \[h2\]ffrt\_loop\_create()

FFRT\_C\_API ffrt\_loop\_t ffrt\_loop\_create(ffrt\_queue\_t queue)

**Description**

Creates a loop.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [ffrt\_queue\_t](../../structs/ffrt-queue-t/document.md) queue | Concurrent queue. |

**Returns**

| Type | Description |
| :-- | :-- |
| FFRT\_C\_API [ffrt\_loop\_t](../../structs/ffrt-loop-t/document.md) | 
Returns the **ffrt\_loop\_t** object if the loop is created;

returns a null pointer otherwise.

 |

#### \[h2\]ffrt\_loop\_destroy()

FFRT\_C\_API int ffrt\_loop\_destroy(ffrt\_loop\_t loop)

**Description**

Destroys a loop.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [ffrt\_loop\_t](../../structs/ffrt-loop-t/document.md) loop | Loop object. |

**Returns**

| Type | Description |
| :-- | :-- |
| FFRT\_C\_API int | 
Returns **0** if the loop is destroyed;

returns **\-1** otherwise.

 |

#### \[h2\]ffrt\_loop\_run()

FFRT\_C\_API int ffrt\_loop\_run(ffrt\_loop\_t loop)

**Description**

Runs a loop.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [ffrt\_loop\_t](../../structs/ffrt-loop-t/document.md) loop | Loop object. |

**Returns**

| Type | Description |
| :-- | :-- |
| FFRT\_C\_API int | 
Returns **0** if the loop runs successfully;

returns **\-1** otherwise.

 |

#### \[h2\]ffrt\_loop\_stop()

FFRT\_C\_API void ffrt\_loop\_stop(ffrt\_loop\_t loop)

**Description**

Stops a loop.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [ffrt\_loop\_t](../../structs/ffrt-loop-t/document.md) loop | Loop object. |

#### \[h2\]ffrt\_loop\_epoll\_ctl()

FFRT\_C\_API int ffrt\_loop\_epoll\_ctl(ffrt\_loop\_t loop, int op, int fd, uint32\_t events, void \*data, ffrt\_poller\_cb cb)

**Description**

Manages listening events on a loop.

You are not advised to call the exit function in cb. Otherwise, undefined behavior may occur.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [ffrt\_loop\_t](../../structs/ffrt-loop-t/document.md) loop | Loop object. |
| int op | Operation to be performed. |
| int fd | File descriptor. |
| uint32\_t events | Event. |
| void \*data | Pointer to the input parameter in the callback function invoked upon event changes. |
| [ffrt\_poller\_cb](../type-def-h/document.md#ffrt_poller_cb) cb | Callback function invoked upon event changes. |

**Returns**

| Type | Description |
| :-- | :-- |
| FFRT\_C\_API int | 
Returns **0** if the operation is successful;

returns **\-1** otherwise.

 |

#### \[h2\]ffrt\_loop\_timer\_start()

FFRT\_C\_API ffrt\_timer\_t ffrt\_loop\_timer\_start(ffrt\_loop\_t loop, uint64\_t timeout, void\* data, ffrt\_timer\_cb cb, bool repeat)

**Description**

Starts the timer on a loop.

You are not advised to call the exit function in cb. Otherwise, undefined behavior may occur.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [ffrt\_loop\_t](../../structs/ffrt-loop-t/document.md) loop | Loop object. |
| uint64\_t timeout | Timeout, in milliseconds. |
| void\* data | Pointer to the input parameter in the callback function invoked upon event changes. |
| [ffrt\_timer\_cb](../type-def-h/document.md#ffrt_timer_cb) cb | Callback function invoked upon event changes. |
| bool repeat | Whether to repeat the timer. |

**Returns**

| Type | Description |
| :-- | :-- |
| FFRT\_C\_API [ffrt\_timer\_t](../type-def-h/document.md#variables) | Returns the timer handle. |

#### \[h2\]ffrt\_loop\_timer\_stop()

FFRT\_C\_API int ffrt\_loop\_timer\_stop(ffrt\_loop\_t loop, ffrt\_timer\_t handle)

**Description**

Stops the timer on a loop.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| ffrt\_loop\_t loop | Loop object. |
| ffrt\_timer\_t handle | Timer handle. |

**Returns**

| Type | Description |
| :-- | :-- |
| FFRT\_C\_API int | 
Returns **0** if the operation is successful;

returns **\-1** otherwise.

 |
