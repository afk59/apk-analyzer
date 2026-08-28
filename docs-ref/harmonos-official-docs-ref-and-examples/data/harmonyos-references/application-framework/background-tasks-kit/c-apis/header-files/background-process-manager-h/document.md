# background\_process\_manager.h

#### Overview

The **background\_process\_manager.h** file declares the APIs for background child process management. You can use these APIs to suppress and unsuppress child processes to prevent child processes from occupying too many system resources and causing system stuttering. The APIs take effect only for the child processes created through **OH\_Ability\_StartNativeChildProcess**.

**File to include**: <background\_process\_manager/background\_process\_manager.h>

**Library**: libbackground\_process\_manager.z.so

**System capability**: SystemCapability.Resourceschedule.BackgroundProcessManager

**Since**: 17

**Related module**: [BackgroundProcessManager](../../modules/backgroundprocessmanager/document.md)

#### Summary

#### \[h2\]Enums

| Name | typedef Keyword | Description |
| :-- | :-- | :-- |
| [BackgroundProcessManager\_ProcessPriority](#backgroundprocessmanager_processpriority) | BackgroundProcessManager\_ProcessPriority | Enumerates child process priorities. |
| [BackgroundProcessManager\_ErrorCode](#backgroundprocessmanager_errorcode) | BackgroundProcessManager\_ErrorCode | Enumerates the error codes used by the background child process management. |

#### \[h2\]Functions

| Name | Description |
| :-- | :-- |
| [int OH\_BackgroundProcessManager\_SetProcessPriority(int pid, BackgroundProcessManager\_ProcessPriority priority)](#oh_backgroundprocessmanager_setprocesspriority) | Sets the child process priority. After a child process is suppressed, the CPU resources that can be obtained will be limited. If the scheduling policy of the main process changes, for example, from the background to the foreground, the child process changes with the main process. To suppress the child process, call this API again. |
| [int OH\_BackgroundProcessManager\_ResetProcessPriority(int pid)](#oh_backgroundprocessmanager_resetprocesspriority) | Unsuppresses the child process. In this case, the child process follows the scheduling policy of the main process. If the scheduling policy of the main process changes, for example, from the background to the foreground, the child process changes with the main process. The effect is the same as calling **resetProcessPriority**. |

#### Enum Description

#### \[h2\]BackgroundProcessManager\_ProcessPriority

enum BackgroundProcessManager\_ProcessPriority

**Description**

Enumerates child process priorities.

**Since**: 17

| Enum | Description |
| :-- | :-- |
| PROCESS\_BACKGROUND = 1 | Compared with **PROCESS\_INACTIVE**, this priority has a more obvious suppression effect. Child processes can obtain less CPU resources. You are advised to set this priority when executing background child processes that cannot be perceived by users, such as background image-text pages. |
| PROCESS\_INACTIVE = 2 | You are advised to set this priority when executing background child processes that can be perceived by users, such as audio playback and navigation. |

#### \[h2\]BackgroundProcessManager\_ErrorCode

enum BackgroundProcessManager\_ErrorCode

**Description**

Enumerates the error codes used by the background child process management.

**Since**: 17

| Enum | Description |
| :-- | :-- |
| ERR\_BACKGROUND\_PROCESS\_MANAGER\_SUCCESS = 0 | The suppression parameter is sent successfully. |
| ERR\_BACKGROUND\_PROCESS\_MANAGER\_INVALID\_PARAM = 401 | Parameter check fails. |
| ERR\_BACKGROUND\_PROCESS\_MANAGER\_REMOTE\_ERROR = 31800001 | The client process fails to obtain the system service. |

#### Function Description

#### \[h2\]OH\_BackgroundProcessManager\_SetProcessPriority()

int OH\_BackgroundProcessManager\_SetProcessPriority(int pid, BackgroundProcessManager\_ProcessPriority priority)

**Description**

Sets the child process priority. After a child process is suppressed, the CPU resources that can be obtained will be limited. If the scheduling policy of the main process changes, for example, from the background to the foreground, the child process changes with the main process. To suppress the child process, call this API again.

**Since**: 17

**Parameters**

| Name | Description |
| :-- | :-- |
| int pid | ID of the child process to be suppressed, which is returned when the child process is created through **OH\_Ability\_StartNativeChildProcess**. |
| [BackgroundProcessManager\_ProcessPriority](#backgroundprocessmanager_processpriority) priority | Suppression priority. |

**Return value**

| Type | Description |
| :-- | :-- |
| int | 
[ERR\_BACKGROUND\_PROCESS\_MANAGER\_SUCCESS](#backgroundprocessmanager_errorcode) is returned if the suppression parameter is sent successfully.

[ERR\_BACKGROUND\_PROCESS\_MANAGER\_INVALID\_PARAM](#backgroundprocessmanager_errorcode) is returned if the parameter check fails.

 |

#### \[h2\]OH\_BackgroundProcessManager\_ResetProcessPriority()

int OH\_BackgroundProcessManager\_ResetProcessPriority(int pid)

**Description**

Unsuppresses the child process. In this case, the child process follows the scheduling policy of the main process. If the scheduling policy of the main process changes, for example, from the background to the foreground, the child process changes with the main process. The effect is the same as calling **resetProcessPriority**.

**Since**: 17

**Parameters**

| Name | Description |
| :-- | :-- |
| int pid | Child process ID, which is returned when the child process is created through **OH\_Ability\_StartNativeChildProcess**. |

**Return value**

| Type | Description |
| :-- | :-- |
| int | [ERR\_BACKGROUND\_PROCESS\_MANAGER\_SUCCESS](#backgroundprocessmanager_errorcode) is returned if the suppression parameter is sent successfully. |
