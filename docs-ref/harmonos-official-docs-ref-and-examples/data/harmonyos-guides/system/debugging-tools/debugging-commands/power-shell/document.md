# power-shell

power-shell is a tool used to convert the power status of a device. It provides basic capabilities such as turning off the screen, waking up the device, and setting the power mode.

#### Environment Setup

Before using this tool, enable the developer mode, obtain the [hdc tool](../../performance-analysis-kit/command-line-tools/hdc/document.md), and run hdc shell.

#### Commands

| Command | Description |
| :-- | :-- |
| help | Obtains the help information about the commands supported by power-shell. |
| setmode | Sets the power mode of the current device. |
| wakeup | Wakes up the system and turns on the screen. |
| suspend | Suspends the system and turns off the screen. |
| timeout | Overwrites or restores the automatic screen-off time in system settings. |

#### help

\# Display the help information.
power-shell help

#### setmode

power-shell setmode

**Commands**

| Command | Description |
| :-- | :-- |
| power-shell setmode -h | Displays the parameters supported by the **setmode** command. |
| power-shell setmode 600 | Enables the normal power mode. |
| power-shell setmode 601 | Enables the power saving mode. |
| power-shell setmode 602 | Enables the performance mode. |
| power-shell setmode 603 | Enables the ultra power saving mode. |

Example:

\# Enable the normal power mode.
power-shell setmode 600
# Enable the power saving mode.
power-shell setmode 601
# Enable the performance mode.
power-shell setmode 602
# Enable the ultra power saving mode.
power-shell setmode 603

#### wakeup

power-shell wakeup

**Commands**

| Command | Description |
| :-- | :-- |
| power-shell wakeup | Turns on the screen. |

Example:

\# Run the shell command to turn on the screen.
power-shell wakeup

#### suspend

power-shell suspend

**Commands**

| Command | Description |
| :-- | :-- |
| power-shell suspend | Turns off the screen. |

Example:

\# Run the shell command to turn off the screen.
power-shell suspend

#### timeout

power-shell timeout

**Parameters**

| Parameter | Description |
| :-- | :-- |
| \-o <time> | Sets the automatic screen-off time, in milliseconds. This parameter is mandatory. |
| \-r | Restores the automatic screen-off time in the current system settings. This parameter is mandatory. |

Example:

\# The automatic screen-off time is set to 30s in the current system settings.
# Run the shell command to set the automatic screen-off time to 15000 ms.
power-shell timeout -o 15000
# Restore the automatic screen-off time set by the system, which is 30s.
power-shell timeout -r
