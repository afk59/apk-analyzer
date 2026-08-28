# task.h

#### Overview

The **task.h** file declares the task APIs in C.

**File to include**: <ffrt/task.h>

**Library**: libffrt.z.so

**System capability**: SystemCapability.Resourceschedule.Ffrt.Core

**Since**: 10

**Related module**: [FFRT](../../modules/ffrt/document.md)

#### Summary

#### \[h2\]Function

| Name | Description |
| :-- | :-- |
| [FFRT\_C\_API int ffrt\_task\_attr\_init(ffrt\_task\_attr\_t\* attr)](#ffrt_task_attr_init) | Initializes a task attribute. |
| [FFRT\_C\_API void ffrt\_task\_attr\_set\_name(ffrt\_task\_attr\_t\* attr, const char\* name)](#ffrt_task_attr_set_name) | Sets a task name. |
| [FFRT\_C\_API const char\* ffrt\_task\_attr\_get\_name(const ffrt\_task\_attr\_t\* attr)](#ffrt_task_attr_get_name) | Obtains a task name. |
| [FFRT\_C\_API void ffrt\_task\_attr\_destroy(ffrt\_task\_attr\_t\* attr)](#ffrt_task_attr_destroy) | Destroys a task attribute. |
| [FFRT\_C\_API void ffrt\_task\_attr\_set\_qos(ffrt\_task\_attr\_t\* attr, ffrt\_qos\_t qos)](#ffrt_task_attr_set_qos) | Sets the task QoS. |
| [FFRT\_C\_API ffrt\_qos\_t ffrt\_task\_attr\_get\_qos(const ffrt\_task\_attr\_t\* attr)](#ffrt_task_attr_get_qos) | Obtains the task QoS. |
| [FFRT\_C\_API void ffrt\_task\_attr\_set\_delay(ffrt\_task\_attr\_t\* attr, uint64\_t delay\_us)](#ffrt_task_attr_set_delay) | 
Sets the task delay time.

After the scheduling delay is set, the input and output dependencies of the task will not take effect.

 |
| [FFRT\_C\_API uint64\_t ffrt\_task\_attr\_get\_delay(const ffrt\_task\_attr\_t\* attr)](#ffrt_task_attr_get_delay) | Obtains the task delay time. |
| [FFRT\_C\_API void ffrt\_task\_attr\_set\_queue\_priority(ffrt\_task\_attr\_t\* attr, ffrt\_queue\_priority\_t priority)](#ffrt_task_attr_set_queue_priority) | Sets the task priority in the queue. |
| [FFRT\_C\_API ffrt\_queue\_priority\_t ffrt\_task\_attr\_get\_queue\_priority(const ffrt\_task\_attr\_t\* attr)](#ffrt_task_attr_get_queue_priority) | Obtains the task priority in the queue. |
| [FFRT\_C\_API void ffrt\_task\_attr\_set\_stack\_size(ffrt\_task\_attr\_t\* attr, uint64\_t size)](#ffrt_task_attr_set_stack_size) | Sets the task stack size. |
| [FFRT\_C\_API uint64\_t ffrt\_task\_attr\_get\_stack\_size(const ffrt\_task\_attr\_t\* attr)](#ffrt_task_attr_get_stack_size) | Obtains the task stack size. |
| [FFRT\_C\_API int ffrt\_this\_task\_update\_qos(ffrt\_qos\_t qos)](#ffrt_this_task_update_qos) | Updates the task QoS. |
| [FFRT\_C\_API ffrt\_qos\_t ffrt\_this\_task\_get\_qos(void)](#ffrt_this_task_get_qos) | Obtains the task QoS. |
| [FFRT\_C\_API uint64\_t ffrt\_this\_task\_get\_id(void)](#ffrt_this_task_get_id) | Obtains the ID of this task. |
| [FFRT\_C\_API void \*ffrt\_alloc\_auto\_managed\_function\_storage\_base(ffrt\_function\_kind\_t kind)](#ffrt_alloc_auto_managed_function_storage_base) | Applies for memory for the task execution function struct. |
| [FFRT\_C\_API void ffrt\_submit\_base(ffrt\_function\_header\_t\* f, const ffrt\_deps\_t\* in\_deps, const ffrt\_deps\_t\* out\_deps, const ffrt\_task\_attr\_t\* attr)](#ffrt_submit_base) | Submits a task. |
| [FFRT\_C\_API ffrt\_task\_handle\_t ffrt\_submit\_h\_base(ffrt\_function\_header\_t\* f, const ffrt\_deps\_t\* in\_deps, const ffrt\_deps\_t\* out\_deps, const ffrt\_task\_attr\_t\* attr)](#ffrt_submit_h_base) | Submits a task, and obtains the task handle. |
| [FFRT\_C\_API void ffrt\_submit\_f(ffrt\_function\_t func, void\* arg, const ffrt\_deps\_t\* in\_deps, const ffrt\_deps\_t\* out\_deps, const ffrt\_task\_attr\_t\* attr)](#ffrt_submit_f) | Submits a task. It is a simplified wrapper of **ffrt\_submit\_base**. This API assumes that the callback function does not need to be destroyed. The task function and parameters are encapsulated into a general task structure, which is then passed to **ffrt\_submit\_base** along with other parameters. |
| [FFRT\_C\_API ffrt\_task\_handle\_t ffrt\_submit\_h\_f(ffrt\_function\_t func, void\* arg, const ffrt\_deps\_t\* in\_deps, const ffrt\_deps\_t\* out\_deps, const ffrt\_task\_attr\_t\* attr)](#ffrt_submit_h_f) | Submits a task, and obtains the task handle. It is a simplified wrapper of **ffrt\_submit\_h\_base**. This API assumes that the callback function does not need to be destroyed. The task function and parameters are encapsulated into a general task structure, which is then passed to **ffrt\_submit\_h\_base** along with other parameters. |
| [FFRT\_C\_API uint32\_t ffrt\_task\_handle\_inc\_ref(ffrt\_task\_handle\_t handle)](#ffrt_task_handle_inc_ref) | Increases the number of task handle references. |
| [FFRT\_C\_API uint32\_t ffrt\_task\_handle\_dec\_ref(ffrt\_task\_handle\_t handle)](#ffrt_task_handle_dec_ref) | Decreases the number of task handle references. |
| [FFRT\_C\_API void ffrt\_task\_handle\_destroy(ffrt\_task\_handle\_t handle)](#ffrt_task_handle_destroy) | Destroys a task handle. |
| [FFRT\_C\_API void ffrt\_wait\_deps(const ffrt\_deps\_t\* deps)](#ffrt_wait_deps) | Waits until the dependent tasks are complete. |
| [FFRT\_C\_API void ffrt\_wait(void)](#ffrt_wait) | Waits until all submitted tasks are complete. |

#### Function Description

#### \[h2\]ffrt\_task\_attr\_init()

FFRT\_C\_API int ffrt\_task\_attr\_init(ffrt\_task\_attr\_t\* attr)

**Description**

Initializes a task attribute.

**Since**: 10

**Parameters**

| Name | Description |
| :-- | :-- |
| [ffrt\_task\_attr\_t](../../structs/ffrt-task-attr-t/document.md)\* attr | Pointer to the task attribute. |

**Returns**

| Type | Description |
| :-- | :-- |
| FFRT\_C\_API int | Returns **0** if the task attribute is initialized; returns **\-1** otherwise. |

#### \[h2\]ffrt\_task\_attr\_set\_name()

FFRT\_C\_API void ffrt\_task\_attr\_set\_name(ffrt\_task\_attr\_t\* attr, const char\* name)

**Description**

Sets a task name.

**Since**: 10

**Parameters**

| Name | Description |
| :-- | :-- |
| [ffrt\_task\_attr\_t](../../structs/ffrt-task-attr-t/document.md)\* attr | Pointer to the task attribute. |
| const char\* name | Pointer to the task name. |

#### \[h2\]ffrt\_task\_attr\_get\_name()

FFRT\_C\_API const char\* ffrt\_task\_attr\_get\_name(const ffrt\_task\_attr\_t\* attr)

**Description**

Obtains a task name.

**Since**: 10

**Parameters**

| Name | Description |
| :-- | :-- |
| [const ffrt\_task\_attr\_t](../../structs/ffrt-task-attr-t/document.md)\* attr | Pointer to the task attribute. |

**Returns**

| Type | Description |
| :-- | :-- |
| FFRT\_C\_API const char\* | Returns a non-null pointer to the task name if the name is obtained; returns a null pointer otherwise. |

#### \[h2\]ffrt\_task\_attr\_destroy()

FFRT\_C\_API void ffrt\_task\_attr\_destroy(ffrt\_task\_attr\_t\* attr)

**Description**

Destroys a task attribute.

**Since**: 10

**Parameters**

| Name | Description |
| :-- | :-- |
| [ffrt\_task\_attr\_t](../../structs/ffrt-task-attr-t/document.md)\* attr | Pointer to the task attribute. |

#### \[h2\]ffrt\_task\_attr\_set\_qos()

FFRT\_C\_API void ffrt\_task\_attr\_set\_qos(ffrt\_task\_attr\_t\* attr, ffrt\_qos\_t qos)

**Description**

Sets the task QoS.

**Since**: 10

**Parameters**

| Name | Description |
| :-- | :-- |
| [ffrt\_task\_attr\_t](../../structs/ffrt-task-attr-t/document.md)\* attr | Pointer to the task attribute. |
| [ffrt\_qos\_t](../type-def-h/document.md#variables) qos | Task QoS. |

#### \[h2\]ffrt\_task\_attr\_get\_qos()

FFRT\_C\_API ffrt\_qos\_t ffrt\_task\_attr\_get\_qos(const ffrt\_task\_attr\_t\* attr)

**Description**

Obtains the task QoS.

**Since**: 10

**Parameters**

| Name | Description |
| :-- | :-- |
| [const ffrt\_task\_attr\_t](../../structs/ffrt-task-attr-t/document.md)\* attr | Pointer to the task attribute. |

**Returns**

| Type | Description |
| :-- | :-- |
| FFRT\_C\_API [ffrt\_qos\_t](../type-def-h/document.md#variables) | Returns the QoS, which is **ffrt\_qos\_default** by default. |

#### \[h2\]ffrt\_task\_attr\_set\_delay()

FFRT\_C\_API void ffrt\_task\_attr\_set\_delay(ffrt\_task\_attr\_t\* attr, uint64\_t delay\_us)

**Description**

Sets the task delay time.

After the scheduling delay is set, the input and output dependencies of the task will not take effect.

**Since**: 10

**Parameters**

| Name | Description |
| :-- | :-- |
| [ffrt\_task\_attr\_t](../../structs/ffrt-task-attr-t/document.md)\* attr | Pointer to the task attribute. |
| uint64\_t delay\_us | Delay time, in microseconds. |

#### \[h2\]ffrt\_task\_attr\_get\_delay()

FFRT\_C\_API uint64\_t ffrt\_task\_attr\_get\_delay(const ffrt\_task\_attr\_t\* attr)

**Description**

Obtains the task delay time.

**Since**: 10

**Parameters**

| Name | Description |
| :-- | :-- |
| [const ffrt\_task\_attr\_t](../../structs/ffrt-task-attr-t/document.md)\* attr | Pointer to the task attribute. |

**Returns**

| Type | Description |
| :-- | :-- |
| FFRT\_C\_API uint64\_t | Returns the delay time. |

#### \[h2\]ffrt\_task\_attr\_set\_queue\_priority()

FFRT\_C\_API void ffrt\_task\_attr\_set\_queue\_priority(ffrt\_task\_attr\_t\* attr, ffrt\_queue\_priority\_t priority)

**Description**

Sets the task priority in the queue.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [ffrt\_task\_attr\_t](../../structs/ffrt-task-attr-t/document.md)\* attr | Pointer to the task attribute. |
| [ffrt\_queue\_priority\_t](../type-def-h/document.md#ffrt_queue_priority_t) priority | Task priority. |

#### \[h2\]ffrt\_task\_attr\_get\_queue\_priority()

FFRT\_C\_API ffrt\_queue\_priority\_t ffrt\_task\_attr\_get\_queue\_priority(const ffrt\_task\_attr\_t\* attr)

**Description**

Obtains the task priority in the queue.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [const ffrt\_task\_attr\_t](../../structs/ffrt-task-attr-t/document.md)\* attr | Pointer to the task attribute. |

**Returns**

| Type | Description |
| :-- | :-- |
| FFRT\_C\_API [ffrt\_queue\_priority\_t](../type-def-h/document.md#ffrt_queue_priority_t) | Returns the task priority. |

#### \[h2\]ffrt\_task\_attr\_set\_stack\_size()

FFRT\_C\_API void ffrt\_task\_attr\_set\_stack\_size(ffrt\_task\_attr\_t\* attr, uint64\_t size)

**Description**

Sets the task stack size.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [ffrt\_task\_attr\_t](../../structs/ffrt-task-attr-t/document.md)\* attr | Pointer to the task attribute. |
| uint64\_t size | Size of the task stack, in bytes. |

#### \[h2\]ffrt\_task\_attr\_get\_stack\_size()

FFRT\_C\_API uint64\_t ffrt\_task\_attr\_get\_stack\_size(const ffrt\_task\_attr\_t\* attr)

**Description**

Obtains the task stack size.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [const ffrt\_task\_attr\_t](../../structs/ffrt-task-attr-t/document.md)\* attr | Pointer to the task attribute. |

**Returns**

| Type | Description |
| :-- | :-- |
| FFRT\_C\_API uint64\_t | Returns the task stack size, in bytes. |

#### \[h2\]ffrt\_this\_task\_update\_qos()

FFRT\_C\_API int ffrt\_this\_task\_update\_qos(ffrt\_qos\_t qos)

**Description**

Updates the task QoS.

**Since**: 10

**Parameters**

| Name | Description |
| :-- | :-- |
| [ffrt\_qos\_t](../type-def-h/document.md#variables) qos | QoS to be updated. |

**Returns**

| Type | Description |
| :-- | :-- |
| FFRT\_C\_API int | Returns **0** if the QoS is updated; returns **\-1** otherwise. |

#### \[h2\]ffrt\_this\_task\_get\_qos()

FFRT\_C\_API ffrt\_qos\_t ffrt\_this\_task\_get\_qos(void)

**Description**

Obtains the task QoS.

**Since**: 12

**Returns**

| Type | Description |
| :-- | :-- |
| FFRT\_C\_API [ffrt\_qos\_t](../type-def-h/document.md#variables) | Returns the task QoS. |

#### \[h2\]ffrt\_this\_task\_get\_id()

FFRT\_C\_API uint64\_t ffrt\_this\_task\_get\_id(void)

**Description**

Obtains the ID of this task.

**Since**: 10

**Returns**

| Type | Description |
| :-- | :-- |
| FFRT\_C\_API uint64\_t | Returns the ID. |

#### \[h2\]ffrt\_alloc\_auto\_managed\_function\_storage\_base()

FFRT\_C\_API void \*ffrt\_alloc\_auto\_managed\_function\_storage\_base(ffrt\_function\_kind\_t kind)

**Description**

Applies for memory for the task execution function struct.

**Since**: 10

**Parameters**

| Name | Description |
| :-- | :-- |
| [ffrt\_function\_kind\_t](../type-def-h/document.md#ffrt_function_kind_t) kind | Type of the task execution function, which can be general or queue. |

**Returns**

| Type | Description |
| :-- | :-- |
| FFRT\_C\_API void \* | Returns a non-null pointer if the memory is allocated; returns a null pointer otherwise. |

#### \[h2\]ffrt\_submit\_base()

FFRT\_C\_API void ffrt\_submit\_base(ffrt\_function\_header\_t\* f, const ffrt\_deps\_t\* in\_deps, const ffrt\_deps\_t\* out\_deps, const ffrt\_task\_attr\_t\* attr)

**Description**

Submits a task.

**Since**: 10

**Parameters**

| Name | Description |
| :-- | :-- |
| [ffrt\_function\_header\_t](../../structs/ffrt-function-header-t/document.md)\* f | Pointer to the task execution function. |
| [const ffrt\_deps\_t](../../structs/ffrt-deps-t/document.md)\* in\_deps | Pointer to the input dependencies. |
| [const ffrt\_deps\_t](../../structs/ffrt-deps-t/document.md)\* out\_deps | Pointer to the output dependencies. |
| [const ffrt\_task\_attr\_t](../../structs/ffrt-task-attr-t/document.md)\* attr | Pointer to the task attribute. |

#### \[h2\]ffrt\_submit\_h\_base()

FFRT\_C\_API ffrt\_task\_handle\_t ffrt\_submit\_h\_base(ffrt\_function\_header\_t\* f, const ffrt\_deps\_t\* in\_deps, const ffrt\_deps\_t\* out\_deps, const ffrt\_task\_attr\_t\* attr)

**Description**

Submits a task, and obtains the task handle.

**Since**: 10

**Parameters**

| Name | Description |
| :-- | :-- |
| [ffrt\_function\_header\_t](../../structs/ffrt-function-header-t/document.md)\* f | Pointer to the task execution function. |
| [const ffrt\_deps\_t](../../structs/ffrt-deps-t/document.md)\* in\_deps | Pointer to the input dependencies. |
| [const ffrt\_deps\_t](../../structs/ffrt-deps-t/document.md)\* out\_deps | Pointer to the output dependencies. |
| [const ffrt\_task\_attr\_t](../../structs/ffrt-task-attr-t/document.md)\* attr | Pointer to the task attribute. |

**Returns**

| Type | Description |
| :-- | :-- |
| FFRT\_C\_API [ffrt\_task\_handle\_t](../../structs/ffrt-task-handle-t/document.md) | Returns a non-null task handle if the task is submitted; returns a null pointer otherwise. |

#### \[h2\]ffrt\_submit\_f()

FFRT\_C\_API void ffrt\_submit\_f(ffrt\_function\_t func, void\* arg, const ffrt\_deps\_t\* in\_deps, const ffrt\_deps\_t\* out\_deps, const ffrt\_task\_attr\_t\* attr)

**Description**

Submits a task. It is a simplified wrapper of **ffrt\_submit\_base**. This API assumes that the callback function does not need to be destroyed. The task function and parameters are encapsulated into a general task structure, which is then passed to **ffrt\_submit\_base** along with other parameters.

**Since**: 20

**Parameters**

| Name | Description |
| :-- | :-- |
| [ffrt\_function\_t](../type-def-h/document.md#ffrt_function_t) func | Task function. |
| void\* arg | Pointer to the argument. |
| [const ffrt\_deps\_t](../../structs/ffrt-deps-t/document.md)\* in\_deps | Pointer to the input dependencies. |
| [const ffrt\_deps\_t](../../structs/ffrt-deps-t/document.md)\* out\_deps | Pointer to the output dependencies. |
| [const ffrt\_task\_attr\_t](../../structs/ffrt-task-attr-t/document.md)\* attr | Pointer to the task attribute. |

**References**

[ffrt\_submit\_base](#ffrt_submit_base)

#### \[h2\]ffrt\_submit\_h\_f()

FFRT\_C\_API ffrt\_task\_handle\_t ffrt\_submit\_h\_f(ffrt\_function\_t func, void\* arg, const ffrt\_deps\_t\* in\_deps, const ffrt\_deps\_t\* out\_deps, const ffrt\_task\_attr\_t\* attr)

**Description**

Submits a task, and obtains the task handle. It is a simplified wrapper of **ffrt\_submit\_h\_base**. This API assumes that the callback function does not need to be destroyed. The task function and parameters are encapsulated into a general task structure, which is then passed to **ffrt\_submit\_h\_base** along with other parameters.

**Since**: 20

**Parameters**

| Name | Description |
| :-- | :-- |
| [ffrt\_function\_t](../type-def-h/document.md#ffrt_function_t) func | Task function. |
| void\* arg | Pointer to the argument. |
| [const ffrt\_deps\_t](../../structs/ffrt-deps-t/document.md)\* in\_deps | Pointer to the input dependencies. |
| [const ffrt\_deps\_t](../../structs/ffrt-deps-t/document.md)\* out\_deps | Pointer to the output dependencies. |
| [const ffrt\_task\_attr\_t](../../structs/ffrt-task-attr-t/document.md)\* attr | Pointer to the task attribute. |

**Returns**

| Type | Description |
| :-- | :-- |
| FFRT\_C\_API [ffrt\_task\_handle\_t](../../structs/ffrt-task-handle-t/document.md) | Returns a non-null task handle if the task is submitted; returns a null pointer otherwise. |

**References**

[ffrt\_submit\_h\_base](#ffrt_submit_h_base)

#### \[h2\]ffrt\_task\_handle\_inc\_ref()

FFRT\_C\_API uint32\_t ffrt\_task\_handle\_inc\_ref(ffrt\_task\_handle\_t handle)

**Description**

Increases the number of task handle references.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [ffrt\_task\_handle\_t](../../structs/ffrt-task-handle-t/document.md) handle | Task handle. |

**Returns**

| Type | Description |
| :-- | :-- |
| FFRT\_C\_API uint32\_t | Returns the original number of task handle references. |

#### \[h2\]ffrt\_task\_handle\_dec\_ref()

FFRT\_C\_API uint32\_t ffrt\_task\_handle\_dec\_ref(ffrt\_task\_handle\_t handle)

**Description**

Decreases the number of task handle references.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [ffrt\_task\_handle\_t](../../structs/ffrt-task-handle-t/document.md) handle | Task handle. |

**Returns**

| Type | Description |
| :-- | :-- |
| FFRT\_C\_API uint32\_t | Returns the original number of task handle references. |

#### \[h2\]ffrt\_task\_handle\_destroy()

FFRT\_C\_API void ffrt\_task\_handle\_destroy(ffrt\_task\_handle\_t handle)

**Description**

Destroys a task handle.

**Since**: 10

**Parameters**

| Name | Description |
| :-- | :-- |
| [ffrt\_task\_handle\_t](../../structs/ffrt-task-handle-t/document.md) handle | Task handle. |

#### \[h2\]ffrt\_wait\_deps()

FFRT\_C\_API void ffrt\_wait\_deps(const ffrt\_deps\_t\* deps)

**Description**

Waits until the dependent tasks are complete.

**Since**: 10

**Parameters**

| Name | Description |
| :-- | :-- |
| [const ffrt\_deps\_t](../../structs/ffrt-deps-t/document.md)\* deps | Pointer to the dependencies. |

#### \[h2\]ffrt\_wait()

FFRT\_C\_API void ffrt\_wait(void)

**Description**

Waits until all submitted tasks are complete.

**Since**: 10
