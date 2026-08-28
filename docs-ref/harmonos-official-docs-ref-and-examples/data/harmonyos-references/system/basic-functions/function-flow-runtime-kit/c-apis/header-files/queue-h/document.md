# queue.h

#### Overview

The **queue.h** file declares the queue APIs in C.

**File to include**: <ffrt/queue.h>

**Library**: libffrt.z.so

**System capability**: SystemCapability.Resourceschedule.Ffrt.Core

**Since**: 10

**Related module**: [FFRT](../../modules/ffrt/document.md)

#### Summary

#### \[h2\]Structs

| Name | Description |
| :-- | :-- |
| [ffrt\_queue\_t](../../structs/ffrt-queue-t/document.md) | Queue handle. |

#### \[h2\]Enums

| Name | typedef Keyword | Description |
| :-- | :-- | :-- |
| [ffrt\_queue\_type\_t](#ffrt_queue_type_t) | ffrt\_queue\_type\_t | Enumerates the queue types. |

#### \[h2\]Function

| Name | Description |
| :-- | :-- |
| [FFRT\_C\_API int ffrt\_queue\_attr\_init(ffrt\_queue\_attr\_t\* attr)](#ffrt_queue_attr_init) | Initializes the queue attribute. |
| [FFRT\_C\_API void ffrt\_queue\_attr\_destroy(ffrt\_queue\_attr\_t\* attr)](#ffrt_queue_attr_destroy) | Destroys the queue attribute. |
| [FFRT\_C\_API void ffrt\_queue\_attr\_set\_qos(ffrt\_queue\_attr\_t\* attr, ffrt\_qos\_t qos)](#ffrt_queue_attr_set_qos) | Sets the queue QoS. |
| [FFRT\_C\_API ffrt\_qos\_t ffrt\_queue\_attr\_get\_qos(const ffrt\_queue\_attr\_t\* attr)](#ffrt_queue_attr_get_qos) | Obtains the queue QoS. |
| [FFRT\_C\_API void ffrt\_queue\_attr\_set\_timeout(ffrt\_queue\_attr\_t\* attr, uint64\_t timeout\_us)](#ffrt_queue_attr_set_timeout) | Sets the queue timeout. The minimum timeout value is 1 ms. Any value set below this threshold will default to 1 ms. |
| [FFRT\_C\_API uint64\_t ffrt\_queue\_attr\_get\_timeout(const ffrt\_queue\_attr\_t\* attr)](#ffrt_queue_attr_get_timeout) | Obtains the queue timeout. |
| [FFRT\_C\_API void ffrt\_queue\_attr\_set\_callback(ffrt\_queue\_attr\_t\* attr, ffrt\_function\_header\_t\* f)](#ffrt_queue_attr_set_callback) | 
Sets a callback that is invoked when a queue task times out.

You are not advised to call the exit function in f. Otherwise, undefined behavior may occur.

 |
| [FFRT\_C\_API ffrt\_function\_header\_t\* ffrt\_queue\_attr\_get\_callback(const ffrt\_queue\_attr\_t\* attr)](#ffrt_queue_attr_get_callback) | Obtains the callback that is invoked when a queue task times out. |
| [FFRT\_C\_API void ffrt\_queue\_attr\_set\_max\_concurrency(ffrt\_queue\_attr\_t\* attr, const int max\_concurrency)](#ffrt_queue_attr_set_max_concurrency) | Sets the maximum concurrency for a queue, which must be a concurrent queue. |
| [FFRT\_C\_API int ffrt\_queue\_attr\_get\_max\_concurrency(const ffrt\_queue\_attr\_t\* attr)](#ffrt_queue_attr_get_max_concurrency) | Obtains the maximum concurrency of a queue, which must be a concurrent queue. |
| [FFRT\_C\_API void ffrt\_queue\_attr\_set\_thread\_mode(ffrt\_queue\_attr\_t\* attr, bool mode)](#ffrt_queue_attr_set_thread_mode) | Sets the running mode of tasks in the queue. By default, the coroutine mode is used. |
| [FFRT\_C\_API bool ffrt\_queue\_attr\_get\_thread\_mode(const ffrt\_queue\_attr\_t\* attr)](#ffrt_queue_attr_get_thread_mode) | Obtains the running mode of tasks in the queue. |
| [FFRT\_C\_API ffrt\_queue\_t ffrt\_queue\_create(ffrt\_queue\_type\_t type, const char\* name, const ffrt\_queue\_attr\_t\* attr)](#ffrt_queue_create) | Creates a queue. |
| [FFRT\_C\_API void ffrt\_queue\_destroy(ffrt\_queue\_t queue)](#ffrt_queue_destroy) | Destroys a queue. |
| [FFRT\_C\_API void ffrt\_queue\_submit(ffrt\_queue\_t queue, ffrt\_function\_header\_t\* f, const ffrt\_task\_attr\_t\* attr)](#ffrt_queue_submit) | Submits a task to a queue. |
| [FFRT\_C\_API ffrt\_task\_handle\_t ffrt\_queue\_submit\_h(ffrt\_queue\_t queue, ffrt\_function\_header\_t\* f, const ffrt\_task\_attr\_t\* attr)](#ffrt_queue_submit_h) | Submits a task to a queue, and obtains the task handle. |
| [FFRT\_C\_API void ffrt\_queue\_submit\_f(ffrt\_queue\_t queue, ffrt\_function\_t func, void\* arg, const ffrt\_task\_attr\_t\* attr)](#ffrt_queue_submit_f) | Submits a task to a queue. It is a simplified wrapper of **ffrt\_queue\_submit**. This API assumes that the callback function does not need to be destroyed. The task function and parameters are encapsulated into a queue task structure, which is then passed to **ffrt\_queue\_submit** along with other parameters. |
| [FFRT\_C\_API ffrt\_task\_handle\_t ffrt\_queue\_submit\_h\_f(ffrt\_queue\_t queue, ffrt\_function\_t func, void\* arg, const ffrt\_task\_attr\_t\* attr)](#ffrt_queue_submit_h_f) | Submits a task to a queue, and obtains the task handle. It is a simplified wrapper of **ffrt\_queue\_submit\_h**. This API assumes that the callback function does not need to be destroyed. The task function and parameters are encapsulated into a queue task structure, which is then passed to **ffrt\_queue\_submit\_h** along with other parameters. |
| [FFRT\_C\_API void ffrt\_queue\_wait(ffrt\_task\_handle\_t handle)](#ffrt_queue_wait) | Waits until a task in the queue is complete. |
| [FFRT\_C\_API int ffrt\_queue\_cancel(ffrt\_task\_handle\_t handle)](#ffrt_queue_cancel) | Cancels a task in the queue. |
| [FFRT\_C\_API ffrt\_queue\_t ffrt\_get\_main\_queue(void)](#ffrt_get_main_queue) | Obtains the main thread queue. |
| [FFRT\_C\_API ffrt\_queue\_t ffrt\_get\_current\_queue(void)](#ffrt_get_current_queue) | Obtains the ArkTS Worker thread queue. (It is deprecated since API version 18.) |

#### Enum Description

#### \[h2\]ffrt\_queue\_type\_t

enum ffrt\_queue\_type\_t

**Description**

Enumerates the queue types.

**Since**: 12

| Enum Item | Description |
| :-- | :-- |
| ffrt\_queue\_serial | Serial queue. |
| ffrt\_queue\_concurrent | Concurrent queue. |
| ffrt\_queue\_max | Invalid queue type. |

#### Function Description

#### \[h2\]ffrt\_queue\_attr\_init()

FFRT\_C\_API int ffrt\_queue\_attr\_init(ffrt\_queue\_attr\_t\* attr)

**Description**

Initializes the queue attribute.

**Since**: 10

**Parameters**

| Name | Description |
| :-- | :-- |
| [ffrt\_queue\_attr\_t](../../structs/ffrt-queue-attr-t/document.md)\* attr | Pointer to the queue attribute. |

**Returns**

| Type | Description |
| :-- | :-- |
| FFRT\_C\_API int | 
Returns **0** if the queue attribute is initialized;

returns **\-1** otherwise.

 |

#### \[h2\]ffrt\_queue\_attr\_destroy()

FFRT\_C\_API void ffrt\_queue\_attr\_destroy(ffrt\_queue\_attr\_t\* attr)

**Description**

Destroys the queue attribute.

**Since**: 10

**Parameters**

| Name | Description |
| :-- | :-- |
| [ffrt\_queue\_attr\_t](../../structs/ffrt-queue-attr-t/document.md)\* attr | Pointer to the queue attribute. |

#### \[h2\]ffrt\_queue\_attr\_set\_qos()

FFRT\_C\_API void ffrt\_queue\_attr\_set\_qos(ffrt\_queue\_attr\_t\* attr, ffrt\_qos\_t qos)

**Description**

Sets the queue QoS.

**Since**: 10

**Parameters**

| Name | Description |
| :-- | :-- |
| [ffrt\_queue\_attr\_t](../../structs/ffrt-queue-attr-t/document.md)\* attr | Pointer to the queue attribute. |
| [ffrt\_qos\_t](../type-def-h/document.md#variables) qos | QoS. |

#### \[h2\]ffrt\_queue\_attr\_get\_qos()

FFRT\_C\_API ffrt\_qos\_t ffrt\_queue\_attr\_get\_qos(const ffrt\_queue\_attr\_t\* attr)

**Description**

Obtains the queue QoS.

**Since**: 10

**Parameters**

| Name | Description |
| :-- | :-- |
| [const ffrt\_queue\_attr\_t](../../structs/ffrt-queue-attr-t/document.md)\* attr | Pointer to the queue attribute. |

**Returns**

| Type | Description |
| :-- | :-- |
| FFRT\_C\_API [ffrt\_qos\_t](../type-def-h/document.md#variables) | Returns the queue QoS. |

#### \[h2\]ffrt\_queue\_attr\_set\_timeout()

FFRT\_C\_API void ffrt\_queue\_attr\_set\_timeout(ffrt\_queue\_attr\_t\* attr, uint64\_t timeout\_us)

**Description**

Sets the serial queue timeout. The minimum timeout value is 1 ms. Any value set below this threshold will default to 1 ms.

**Since**: 10

**Parameters**

| Name | Description |
| :-- | :-- |
| [ffrt\_queue\_attr\_t](../../structs/ffrt-queue-attr-t/document.md)\* attr | Pointer to the serial queue attribute. |
| uint64\_t timeout\_us | Serial queue timeout, in microseconds. |

#### \[h2\]ffrt\_queue\_attr\_get\_timeout()

FFRT\_C\_API uint64\_t ffrt\_queue\_attr\_get\_timeout(const ffrt\_queue\_attr\_t\* attr)

**Description**

Obtains the serial queue timeout.

**Since**: 10

**Parameters**

| Name | Description |
| :-- | :-- |
| [const ffrt\_queue\_attr\_t](../../structs/ffrt-queue-attr-t/document.md)\* attr | Pointer to the serial queue attribute. |

**Returns**

| Type | Description |
| :-- | :-- |
| FFRT\_C\_API uint64\_t | Returns the serial queue timeout. |

#### \[h2\]ffrt\_queue\_attr\_set\_callback()

FFRT\_C\_API void ffrt\_queue\_attr\_set\_callback(ffrt\_queue\_attr\_t\* attr, ffrt\_function\_header\_t\* f)

**Description**

Sets a callback that is invoked when a queue task times out.

You are not advised to call the exit function in f. Otherwise, undefined behavior may occur.

**Since**: 10

**Parameters**

| Name | Description |
| :-- | :-- |
| [ffrt\_queue\_attr\_t](../../structs/ffrt-queue-attr-t/document.md)\* attr | Pointer to the serial queue attribute. |
| [ffrt\_function\_header\_t](../../structs/ffrt-function-header-t/document.md)\* f | Pointer to the callback function invoked upon a timeout. |

#### \[h2\]ffrt\_queue\_attr\_get\_callback()

FFRT\_C\_API ffrt\_function\_header\_t\* ffrt\_queue\_attr\_get\_callback(const ffrt\_queue\_attr\_t\* attr)

**Description**

Obtains the callback that is invoked when a queue task times out.

**Since**: 10

**Parameters**

| Name | Description |
| :-- | :-- |
| [const ffrt\_queue\_attr\_t](../../structs/ffrt-queue-attr-t/document.md)\* attr | Pointer to the serial queue attribute. |

**Returns**

| Type | Description |
| :-- | :-- |
| FFRT\_C\_API [ffrt\_function\_header\_t](../../structs/ffrt-function-header-t/document.md)\* | Returns the callback. |

#### \[h2\]ffrt\_queue\_attr\_set\_max\_concurrency()

FFRT\_C\_API void ffrt\_queue\_attr\_set\_max\_concurrency(ffrt\_queue\_attr\_t\* attr, const int max\_concurrency)

**Description**

Sets the maximum concurrency for a concurrent queue.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [ffrt\_queue\_attr\_t](../../structs/ffrt-queue-attr-t/document.md)\* attr | Pointer to the queue attribute. |
| const int max\_concurrency | Maximum concurrency. |

#### \[h2\]ffrt\_queue\_attr\_get\_max\_concurrency()

FFRT\_C\_API int ffrt\_queue\_attr\_get\_max\_concurrency(const ffrt\_queue\_attr\_t\* attr)

**Description**

Obtains the maximum concurrency of a concurrent queue.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [const ffrt\_queue\_attr\_t](../../structs/ffrt-queue-attr-t/document.md)\* attr | Pointer to the queue attribute. |

**Returns**

| Type | Description |
| :-- | :-- |
| FFRT\_C\_API int | Returns the maximum concurrency. |

#### \[h2\]ffrt\_queue\_attr\_set\_thread\_mode()

FFRT\_C\_API void ffrt\_queue\_attr\_set\_thread\_mode(ffrt\_queue\_attr\_t\* attr, bool mode)

**Description**

Sets the running mode of tasks in the queue. By default, the coroutine mode is used.

**Since**: 20

**Parameters**

| Name | Description |
| :-- | :-- |
| [ffrt\_queue\_attr\_t](../../structs/ffrt-queue-attr-t/document.md)\* attr | Pointer to the queue attribute. |
| bool mode | Sets the running mode of the queue task. The value **true** indicates the thread mode, and the value **false** indicates the coroutine mode. |

#### \[h2\]ffrt\_queue\_attr\_get\_thread\_mode()

FFRT\_C\_API bool ffrt\_queue\_attr\_get\_thread\_mode(const ffrt\_queue\_attr\_t\* attr)

**Description**

Obtains the running mode of tasks in the queue.

**Since**: 20

**Parameters**

| Name | Description |
| :-- | :-- |
| [const ffrt\_queue\_attr\_t](../../structs/ffrt-queue-attr-t/document.md)\* attr | Pointer to the queue attribute. |

**Returns**

| Type | Description |
| :-- | :-- |
| FFRT\_C\_API bool | The value **true** indicates the thread mode, and the value **false** indicates the coroutine mode. |

#### \[h2\]ffrt\_queue\_create()

FFRT\_C\_API ffrt\_queue\_t ffrt\_queue\_create(ffrt\_queue\_type\_t type, const char\* name, const ffrt\_queue\_attr\_t\* attr)

**Description**

Creates a queue.

**Since**: 10

**Parameters**

| Name | Description |
| :-- | :-- |
| [ffrt\_queue\_type\_t](#ffrt_queue_type_t) type | Queue type. |
| const char\* name | Pointer to the queue name. |
| [const ffrt\_queue\_attr\_t](../../structs/ffrt-queue-attr-t/document.md)\* attr | Pointer to the queue attribute. |

**Returns**

| Type | Description |
| :-- | :-- |
| FFRT\_C\_API [ffrt\_queue\_t](../../structs/ffrt-queue-t/document.md) | 
Returns a non-null queue handle if the queue is created;

returns a null pointer otherwise.

 |

#### \[h2\]ffrt\_queue\_destroy()

FFRT\_C\_API void ffrt\_queue\_destroy(ffrt\_queue\_t queue)

**Description**

Destroys a queue.

**Since**: 10

**Parameters**

| Name | Description |
| :-- | :-- |
| [ffrt\_queue\_t](../../structs/ffrt-queue-t/document.md) queue | Queue handle. |

#### \[h2\]ffrt\_queue\_submit()

FFRT\_C\_API void ffrt\_queue\_submit(ffrt\_queue\_t queue, ffrt\_function\_header\_t\* f, const ffrt\_task\_attr\_t\* attr)

**Description**

Submits a task to a queue.

**Since**: 10

**Parameters**

| Name | Description |
| :-- | :-- |
| [ffrt\_queue\_t](../../structs/ffrt-queue-t/document.md) queue | Queue handle. |
| [ffrt\_function\_header\_t](../../structs/ffrt-function-header-t/document.md)\* f | Pointer to the task execution function. |
| [const ffrt\_task\_attr\_t](../../structs/ffrt-task-attr-t/document.md)\* attr | Pointer to the task attribute. |

#### \[h2\]ffrt\_queue\_submit\_h()

FFRT\_C\_API ffrt\_task\_handle\_t ffrt\_queue\_submit\_h(ffrt\_queue\_t queue, ffrt\_function\_header\_t\* f, const ffrt\_task\_attr\_t\* attr)

**Description**

Submits a task to a queue, and obtains the task handle.

**Since**: 10

**Parameters**

| Name | Description |
| :-- | :-- |
| [ffrt\_queue\_t](../../structs/ffrt-queue-t/document.md) queue | Queue handle. |
| [ffrt\_function\_header\_t](../../structs/ffrt-function-header-t/document.md)\* f | Pointer to the task execution function. |
| [const ffrt\_task\_attr\_t](../../structs/ffrt-task-attr-t/document.md)\* attr | Pointer to the task attribute. |

**Returns**

| Type | Description |
| :-- | :-- |
| FFRT\_C\_API [ffrt\_task\_handle\_t](../../structs/ffrt-task-handle-t/document.md) | 
Returns a non-null task handle if the task is submitted;

returns a null pointer otherwise.

 |

#### \[h2\]ffrt\_queue\_submit\_f()

FFRT\_C\_API void ffrt\_queue\_submit\_f(ffrt\_queue\_t queue, ffrt\_function\_t func, void\* arg, const ffrt\_task\_attr\_t\* attr)

**Description**

Submits a task to a queue. It is a simplified wrapper of **ffrt\_queue\_submit**. This API assumes that the callback function does not need to be destroyed. The task function and parameters are encapsulated into a queue task structure, which is then passed to **ffrt\_queue\_submit** along with other parameters.

**Since**: 20

**Parameters**

| Name | Description |
| :-- | :-- |
| [ffrt\_queue\_t](../../structs/ffrt-queue-t/document.md) queue | Queue handle. |
| [ffrt\_function\_t](../type-def-h/document.md#ffrt_function_t) func | Task function. |
| void\* arg | Pointer to the argument. |
| [const ffrt\_task\_attr\_t](../../structs/ffrt-task-attr-t/document.md)\* attr | Pointer to the task attribute. |

**References**

[ffrt\_queue\_submit](#ffrt_queue_submit)

#### \[h2\]ffrt\_queue\_submit\_h\_f()

FFRT\_C\_API ffrt\_task\_handle\_t ffrt\_queue\_submit\_h\_f(ffrt\_queue\_t queue, ffrt\_function\_t func, void\* arg, const ffrt\_task\_attr\_t\* attr)

**Description**

Submits a task to a queue, and obtains the task handle. It is a simplified wrapper of **ffrt\_queue\_submit\_h**. This API assumes that the callback function does not need to be destroyed. The task function and parameters are encapsulated into a queue task structure, which is then passed to **ffrt\_queue\_submit\_h** along with other parameters.

**Since**: 20

**Parameters**

| Name | Description |
| :-- | :-- |
| [ffrt\_queue\_t](../../structs/ffrt-queue-t/document.md) queue | Queue handle. |
| [ffrt\_function\_t](../type-def-h/document.md#ffrt_function_t) func | Task function. |
| void\* arg | Pointer to the argument. |
| [const ffrt\_task\_attr\_t](../../structs/ffrt-task-attr-t/document.md)\* attr | Pointer to the task attribute. |

**Returns**

| Type | Description |
| :-- | :-- |
| FFRT\_C\_API [ffrt\_task\_handle\_t](../../structs/ffrt-task-handle-t/document.md) | 
Returns a non-null task handle if the task is submitted;

returns a null pointer otherwise.

 |

**References**

[ffrt\_queue\_submit\_h](#ffrt_queue_submit_h)

#### \[h2\]ffrt\_queue\_wait()

FFRT\_C\_API void ffrt\_queue\_wait(ffrt\_task\_handle\_t handle)

**Description**

Waits until a task in the queue is complete.

**Since**: 10

**Parameters**

| Name | Description |
| :-- | :-- |
| [ffrt\_task\_handle\_t](../../structs/ffrt-task-handle-t/document.md) handle | Task handle. |

#### \[h2\]ffrt\_queue\_cancel()

FFRT\_C\_API int ffrt\_queue\_cancel(ffrt\_task\_handle\_t handle)

**Description**

Cancels a task in the queue.

**Since**: 10

**Parameters**

| Name | Description |
| :-- | :-- |
| [ffrt\_task\_handle\_t](../../structs/ffrt-task-handle-t/document.md) handle | Task handle. |

**Returns**

| Type | Description |
| :-- | :-- |
| FFRT\_C\_API int | 
Returns **0** if the task is canceled;

returns **\-1** otherwise.

 |

#### \[h2\]ffrt\_get\_main\_queue()

FFRT\_C\_API ffrt\_queue\_t ffrt\_get\_main\_queue(void)

**Description**

Obtains the main thread queue.

**Since**: 12

**Returns**

| Type | Description |
| :-- | :-- |
| FFRT\_C\_API [ffrt\_queue\_t](../../structs/ffrt-queue-t/document.md) | Returns the handle to the main thread queue. |

#### \[h2\]ffrt\_get\_current\_queue()

FFRT\_C\_API ffrt\_queue\_t ffrt\_get\_current\_queue(void)

**Description**

Obtains the ArkTS Worker thread queue.

**Since**: 12

**Deprecated from**: 18

**Returns**

| Type | Description |
| :-- | :-- |
| FFRT\_C\_API ffrt\_queue\_t | Returns the handle to the thread queue. |
