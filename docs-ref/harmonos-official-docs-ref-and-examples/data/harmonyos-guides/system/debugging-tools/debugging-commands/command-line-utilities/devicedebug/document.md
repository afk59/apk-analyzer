# devicedebug

devicedebug provides the capability of sending signals to applications for debugging purposes. Currently, signals can be sent only to processes of debuggable applications managed by AMS to terminate these processes.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c4/v3/lJ4ICPpAR66mi9NPWIxInQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062033Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=ED22F8622ED331C4C970F92155F90E365F674C71427629792042EC1883D78523)

Before using this tool, you must obtain hdc and run the **hdc shell** command.

**Table 1** devicedebug commands

| Command | Description |
| :-- | :-- |
| help/-h | Displays the commands supported by the devicedebug tool. |
| kill | Kills a process with a specified PID. |

#### help

devicedebug help

**Table 2** Help command

| Command | Description |
| :-- | :-- |
| devicedebug help | Displays the commands supported by devicedebug. |

Example:

\# Display the help information.
devicedebug help

#### kill

devicedebug kill

Sends the signal (1-64) to a debug-type application process. After receiving the signal, the application terminates the corresponding process.

**Table 3** Kill command parameters

| Command | Description |
| :-- | :-- |
| help/-h | Help information. |
| \-<signal> <pid> | **signal** (1-64) indicates the kill signal, which is used to kill a process of the debuggable application with a specified PID. This field is mandatory. |

**Return value**

If the process corresponding to the PID is a non-application process, "devicedebug: kill: {pid}: No such app process" is returned. If the corresponding process is not a debuggable application process, "devicedebug: kill: process: {pid} is not debuggable app" is returned.

Example:

\# Kill the 12111 process using signal 9.
devicedebug kill -9 12111
