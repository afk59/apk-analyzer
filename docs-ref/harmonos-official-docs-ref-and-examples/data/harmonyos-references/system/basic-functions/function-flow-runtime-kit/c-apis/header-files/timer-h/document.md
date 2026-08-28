# timer.h

#### Overview

The **timer.h** file declares the timer APIs in C.

**File to include**: <ffrt/timer.h>

**Library**: libffrt.z.so

**System capability**: SystemCapability.Resourceschedule.Ffrt.Core

**Since**: 12

**Related module**: [FFRT](../../modules/ffrt/document.md)

#### Summary

#### \[h2\]Function

| Name | Description |
| :-- | :-- |
| [FFRT\_C\_API ffrt\_timer\_t ffrt\_timer\_start(ffrt\_qos\_t qos, uint64\_t timeout, void\* data, ffrt\_timer\_cb cb, bool repeat)](#ffrt_timer_start) | Starts the timer. |
| [FFRT\_C\_API int ffrt\_timer\_stop(ffrt\_qos\_t qos, ffrt\_timer\_t handle)](#ffrt_timer_stop) | Stops the timer. |

#### Function Description

#### \[h2\]ffrt\_timer\_start()

FFRT\_C\_API ffrt\_timer\_t ffrt\_timer\_start(ffrt\_qos\_t qos, uint64\_t timeout, void\* data, ffrt\_timer\_cb cb, bool repeat)

**Description**

Starts the timer.

You are not advised to call the exit function in cb. Otherwise, undefined behavior may occur.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [ffrt\_qos\_t](../type-def-h/document.md#variables) qos | QoS. |
| uint64\_t timeout | Timeout, in milliseconds. |
| void\* data | Pointer to the input parameter in the callback function invoked upon a timeout. |
| [ffrt\_timer\_cb](../type-def-h/document.md#ffrt_timer_cb) cb | Callback function invoked upon a timeout. |
| bool repeat | Whether to repeat the timer (not supported yet). |

**Returns**

| Type | Description |
| :-- | :-- |
| FFRT\_C\_API [ffrt\_timer\_t](../type-def-h/document.md#variables) | Returns the timer handle. |

#### \[h2\]ffrt\_timer\_stop()

FFRT\_C\_API int ffrt\_timer\_stop(ffrt\_qos\_t qos, ffrt\_timer\_t handle)

**Description**

Stops the timer.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f7/v3/wFl7AooSShO8F1odg5nJnQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062402Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=25F262C002DABA3FEC39F1048BF88047CEFC45469CAA9917C0260B47A5041942)

-   This is a blocking API and must not be used inside callback functions to prevent deadlocks or synchronization issues.
    
-   If the callback corresponding to the passed handle is being executed, this function will wait for the callback to complete before resuming its own execution.
    

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| ffrt\_qos\_t qos | QoS. |
| ffrt\_timer\_t handle | Handle to the timer. |

**Returns**

| Type | Description |
| :-- | :-- |
| FFRT\_C\_API int | Returns **0** if the timer is stopped successfully; returns **\-1** otherwise. |
