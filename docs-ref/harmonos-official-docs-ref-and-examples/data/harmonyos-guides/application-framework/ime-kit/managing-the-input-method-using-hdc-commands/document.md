# Managing the Input Method Using hdc Commands

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c4/v3/_ur-pVYVSnmwuIIJ08FfCQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061954Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=C4347A3171BBE5898DA3D1922111CE0262A40DC77F49E47BA07985439098F646)

The IME tool is supported since API version 20.

**How to Use**

hdc shell ime \[option\] \[parameter\]

**Commands**

| Option | Parameter | Description |
| :-- | :-- | :-- |
| \-e | bundle \[-b /-f\] | 
Enables an input method as a specified mode. If **\-b** or **\-f** is not set, **\-b** defaults to the basic mode, and **\-f** indicates the full experience mode.

**Note**: The enabling status of the preset default input method cannot be changed.

 |
| \-d | bundle | 

Disables a specified input method.

**Note**: The preset default input method cannot be disabled.

 |
| \-s | bundle | 

Switches to a specified input method.

**Note**: You are not allowed to switch to another input method when the screen is locked or the password is being entered.

 |
| \-g | NA | Obtains the current input method. |
| \-l | NA | Lists all input methods. |
| \-h | NA | Displays the help information. |

#### Managing Input Methods Using IME Tool

1.  Enabling an input method. You can enable a third-party input method as basic mode or full experience mode.
    
     # Input: Use an hdc command to enable an input method.
     # Processing: Check if it is an hdc shell command, and call the corresponding system API for managing input methods.
     # Output: The effect is equivalent to a direct API call.
     # Basic mode
     hdc shell ime -e com.xxx.yyy
     # Full experience mode
     hdc shell ime -e com.xxx.yyy -f
    
2.  Disabling an input method. You can disable a third-party input method.
    
     # Input: Use an hdc command to disable an input method.
     # Processing: Check if it is an hdc shell command, and call the corresponding API for disabling.
     # Output: The effect is equivalent to a direct API call.
     hdc shell ime -d com.xxx.yyy
    
3.  Switching to a specified input method.
    
     # Input: Use an hdc command to switch the input method.
     # Processing: Check if it is an hdc shell command, and call the corresponding API for switching.
     # Output: The effect is equivalent to a direct API call.
     hdc shell ime -s com.xxx.yyy
    
4.  Obtaining the current input method.
    
     # Input: Use an hdc command to obtain the current input method.
     # Processing: Check if it is an hdc shell command, and call the corresponding API for obtaining.
     # Output: The effect is equivalent to a direct API call.
     hdc shell ime -g
    
5.  Listing all input methods. The enabling status of the preset default input method is not displayed.
    
     # Input: Use an hdc command to list all input methods.
     # Processing: Check if it is an hdc shell command, and call the corresponding API for listing.
     # Output: The effect is equivalent to a direct API call.
     hdc shell ime -l
    
6.  Displaying the help information.
    
     # Input: Use an hdc command to display the help information.
     # Output: Display the help information.
     hdc shell ime -h
