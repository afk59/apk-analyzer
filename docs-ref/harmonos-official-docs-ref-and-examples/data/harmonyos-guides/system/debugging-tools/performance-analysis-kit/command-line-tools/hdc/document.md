# hdc

HarmonyOS Device Connector (hdc) is a command line tool used to interact with devices for debugging, data transfer, log viewing, and application installation. It can run on Windows, Linux, and MacOS to provide efficient and convenient device debugging capabilities.

hdc consists of three parts:

**client**: A process running on the PC. It starts when you run the hdc command and exits after the command is complete.

**server**: A background service process running on the PC. It manages data interaction and device discovery between the client process and the daemon process on the device.

**daemon**: A process running on the device for debugging. It is used to respond to requests sent by server.

The following figure shows the relationship.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c2/v3/hj9hA_PkQned6HD99xNVcQ/en-us_image_0000002537765122.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062030Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=2ACB67B8917E06B9ADFA44CA26DEFF08BEC1CD47BDBB83634CF9CD6C3AE515E6)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b5/v3/mpt3-EOqQFqj5TCCxmfNHw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062030Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=B4D19800EF20FC74709A8FD08E50F9C5799FE5C01C82FDE7D6867D79BD5BD0F7)

When the client starts, it checks whether the server is running by default. If not, a new hdc process is started as a server process and runs in the background.

When the server is running, it listens for port 8710 on the computer by default. You can set the system environment variable **OHOS\_HDC\_SERVER\_PORT** to listen for a port number ranging from 1 to 65535.

#### Environment Setup

You can obtain hdc in any of the following ways:

1.  Obtain the hdc tool through HarmonyOS SDK. HarmonyOS SDK is embedded in [DevEco Studio](https://developer.huawei.com/consumer/en/deveco-studio/). No additional configuration is required. hdc is installed in **DevEco Studio/sdk/default/HarmonyOS/toolchains** by default. On macOS, the SDK is installed in **DevEco Studio/Contents**.
    
2.  SDK directory of [Command Line Tools](https://developer.huawei.com/consumer/en/download/). hdc is installed in Command Line **Tools/sdk/default/HarmonyOS/toolchains** by default.
    

hdc supports both USB and wireless connections. You can enable or disable debugging in **Settings** > **System** > **Developer options** on the device. The setting takes effect immediately without restarting the device. If **Developer options** is not enabled, enable it by referring to [Developer Options](../../../../../coding-and-debugging/debugging-your-app/developer-options/document.md#section530763213432). For details about the connection mode and procedure, see [USB Connection](#usb-connection) and [TCP Connection](#tcp-connection).

## (Optional) Running hdc on CLI

**Perform debugging in the installation directory**

1.  You can run hdc commands in the **toolchains** subdirectory of the HarmonyOS SDK to debug devices.
    
2.  hdc can run independently. You can save the hdc executable file and **libusb\_shared** dependency file in the **toolchains** subdirectory to a custom directory and run the hdc command in the custom directory to implement independent debugging.
    

**Add hdc to the system environment variables**

1.  On Windows:
    
    -   Press the **Windows** key, enter **Settings** in the search box, and click to enter the **Settings** screen.
        
    -   Search for **Advanced system settings**. Choose **Environment Variables** > **System Variables** > **Path**, and click **Edit** to add the directory of **hdc.exe** to **Path**. After the environment variables are configured, restart the computer and run the hdc command in the CLI.
        
2.  On Linux/macOS:
    
    -   Start the terminal tool and run the following command:
        
        echo $SHELL
        
        -   If the command output is **bin/bash**, open the **.bashrc** file.
            
            vi ~/.bashrc
            
        -   If the command output is **/bin/zsh**, open the **.zshrc** file.
            
            vi ~/.zshrc
            
    -   Switch to the English input method and press **i** to enter the Insert mode.
        
    -   Add the **PATH** information to the end of the file.
        
        export PATH={DevEco Studio}/sdk/default/HarmonyOS/toolchains:$PATH
        
        Replace **{DevEco Studio}** with the absolute path of the DevEco Studio installation directory, for example, **/home/DevEco-Studio**.
        
    -   After the editing is complete, press **Esc** to exit the Insert mode, input **:wq**, and press **Enter** to save the file.
        
    -   Run the following command for the environment variable to take effect.
        
        -   If the **.bashrc** file is opened in **1**, run the following command:
            
            source ~/.bashrc
            
        -   If the **.zshrc** file is opened in **1**, run the following command:
            
            source ~/.zshrc
            
    -   After the environment variables are configured, restart the system.
        

## (Optional) Configuring Server

You can configure system environment variables to modify the listening port of the **server** process, logging level, or feature switch. For details, see [Options](#options).

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b6/v3/452m-7fhRGaaJZ-aPd2Sgg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062030Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=8D5B64918EF65088BABFA106682B7AEA94DBD47F23021F1A68C9A492D2B322CE)

After the environment variables are configured, restart the CLI or other software that uses HarmonyOS SDK for the new environment variable to take effect.

#### hdc Commands

## Global Parameters

Global parameters can be added between hdc and the command to be executed. For example, you can use the **\-t** parameter to specify a device to run the command.

hdc -t connect-key shell echo "Hello world"

| Parameter | Description |
| :-- | :-- |
| [\-t](#connecting-to-the-specified-target-device) | Connects to a specified target device based on the device ID. This parameter is optional when one device is connected and mandatory when multiple devices are connected. |
| [\-l](#server-logs) | (Optional) Specifies the log level when the device is running. The value ranges from 0 to 6. The default value is **3** (**LOG\_INFO**). |
| [\-s](#remote-connection) | (Optional) Specifies the IP and port in **IP:port** format for listening when the client connects to the server. |
| [\-p](#quick-command-execution) | (Optional) Executes a client command without querying the server process. |
| [\-m](#starting-a-server-in-the-foreground) | (Optional) Starts the server process in the foreground. |
| [\-e](#creating-a-local-port-forwarding) | 
(Optional) Specifies the IP address for listening on the local host when TCP port forwarding is performed. The default value is **127.0.0.1**. This parameter must be used together with **\-m**.

If the **\-e** parameter is used to specify the listening address, and the address is not the local loopback address (for example, **127.0.0.1**), pay attention to the access security.

Note: This API is supported since API version 20.

 |

## Commands

| Command | Description |
| :-- | :-- |
| [list targets](#displaying-devices) | Displays all connected target devices. |
| [wait](#waiting-for-device-connection) | Waits until the device is properly connected. |
| [tmode usb](#switching-between-usb-debugging-and-wireless-debugging) | Since version 3.1.0e, this command is deprecated. You need to set the USB debugging on the device setting page. |
| [tmode port](#enabling-the-network-connection-channel) | Enables the network connection channel of the device. |
| [tmode port close](#disabling-the-network-connection-channel) | Disables the network connection channel of the device. |
| [tconn](#connecting-to-a-device-over-tcp) | Specifies the device to connect based on **IP:port**. |
| [shell](#running-interactive-commands) | Runs a command on the device, for example, **hdc shell ls**. If no command parameter is specified, you can run commands on the device terminal. |
| [install](#installing-an-application) | Installs an application. |
| [uninstall](#uninstalling-an-application) | Uninstalls a specified application. |
| [file send](#sending-a-file-to-a-remote-device) | Sends a local file to a remote device. |
| [file recv](#receiving-a-file-from-a-remote-device) | Receives a file from a remote device. |
| [fport ls](#querying-the-port-forwarding-task-list) | Lists all port forwarding tasks. |
| [fport](#creating-a-local-port-forwarding) | Sets up a local port forwarding, which forwards data from a local port to a remote port. |
| [rport](#creating-a-remote-port-forwarding) | Sets up a remote port forwarding, which forwards data from a remote port to a local port. |
| [fport rm](#deleting-a-port-forwarding-task) | Deletes a port forwarding task. |
| [start](#starting-a-service) | Starts the hdc server process. |
| [kill](#terminating-a-service) | Terminates the hdc server process. |
| [hilog](#printing-device-logs) | Obtains device log information. |
| [jpid](#displaying-pids-of-started-applications) | Displays the PIDs of started applications on the device. |
| [track-jpid](#displaying-pids-and-names-of-started-applications-in-real-time) | Displays the PIDs and names of started applications on the device in real time. |
| [target boot](#restarting-the-target-device) | Restarts the target device. |
| [keygen](#security-commands) | Generates a new key pair. |
| [version](#querying-the-hdc-version) | Displays the hdc version information. You can also run the **hdc -v** command to display the version information. |
| [checkserver](#querying-the-client-and-server-versions) | Obtains the version information about the client process and server process. |
| [bugreport](#exporting-system-information) | Exports system information. |

#### Basic Commands

To use the USB debugging mode, enable the USB debugging functionality on the device and connect the device to the computer using a USB cable before running the command.

## Displaying Connected Devices

hdc list targets

## Running the Shell command

hdc shell echo "Hello world"

## Obtaining the Help Information

Display the hdc help information.

hdc -h \[verbose\]
hdc help

| Name | Description |
| :-- | :-- |
| \-h verbose | Displays the help information about the hdc command. The optional parameter **verbose** can be used to display detailed help information. |
| help | Displays the help information about the hdc command. |

**Return value**

| Value | Description |
| :-- | :-- |
| 
OpenHarmony device connector(hdc) ...

\---------------------------------global commands:----------------------------------

\-h/help \[verbose\] - Print hdc help, 'verbose' for more other cmds

... (Detailed information is omitted here.)

 | Help information for hdc commands. |

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1a/v3/7O0FfiETSmuKpADD_92aAQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062030Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=839D7CD2E31800AA4E0DD921998811984EAB652FDABED83959746DB2ED05F737)

If an exception occurs, run the **hdc kill -r** command to terminate the process and restart the hdc service.

If the **hdc list targets** command cannot obtain the device information, see [What should I do if the device cannot be identified](#what-should-i-do-if-the-device-cannot-be-identified).

#### Managing Device Connections

## Displaying Devices

hdc list targets \[-v\]

**Parameters**

| Name | Description |
| :-- | :-- |
| \-v | Displays more details about the device. |

**Return value**

| Value | Description |
| :-- | :-- |
| Device ID list | 
List of IDs of connected devices.

You can add the **\-v** parameter to the command to view the following information: device ID, connection mode (TCP/USB), connection status (**Unknown**/**Ready**/**Connected**/**Offline**/**Unauthorized**), device name, and hdc identifier.

 |
| Device ID Unauthorized | The device is unauthorized. |
| \[Empty\] | No device is found. |

**Usage**

$ hdc list targets
connect-key1
...

$ hdc list targets -v
connect-key1            USB     Connected       localhost       hdc
127.0.0.1:5555          TCP     Offline         localhost       hdc
connect-key2            USB     Offline         localhost       hdc
...

## Connecting to the Specified Target Device

hdc -t \[connect-key\] \[command\]

**Parameters**

| Name | Description |
| :-- | :-- |
| \-t | 
Connects to a specified target device based on the device ID.

This parameter is optional when one device is connected and mandatory when multiple devices are connected.

 |
| command | Command to be executed. |

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3f/v3/bcPpJRPwQwqMSV95l1tbVQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062030Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=6E9DF0E3C05C02EC8900A80CA842C88CECABD7A0F56698468D82FADB5547BE44)

The connect-key uniquely identifies a device. If the device is connected through USB, the connect-key is the USB SN. If the device is connected over the network, the connect-key is IP:port.

**Return value**

| Value | Description |
| :-- | :-- |
| Normal command output. For details, see [Commands](#commands). | \- |
| \[Fail\]Not match target founded, check connect-key please. | The **\-t** parameter is used to match the connect-key that does not exist. Check whether the connect-key is correct. |
| \[Fail\]Device not founded or connected. | The device is not found or connected. |
| \[Fail\]ExecuteCommand need connect-key? please confirm a device by help info. | Ensure that the device is connected and the debugging functionality is enabled. |
| Unknown operation command... | The command is not supported. |

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4/v3/AoBqDV-7RXyrrqc9HuhjiQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062030Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=5F1FCCF1242FE7AA7589A2DA1E7BD94E42050278F88F29EC68028B3AF4C1A2C9)

The error information is for reference only and may be optimized. Do not use the error information for logic judgment of automated scripts or programs. In practice, you are advised to use standard error codes provided by the system. For details, see [hdc Error Codes](#hdc-error-codes).

**Usage**

This option must be used with a command. The following uses the **shell** command as an example.

$ hdc list targets
connect-key1
...

$ hdc -t connect-key1 shell echo "hello world!"
hello world!

## Waiting for Device Connection

hdc wait # Wait for the device to connect.
hdc -t \[connect-key\] wait # Wait for the specified device to connect. Replace connect-key with the specified device ID.

**Parameters**

| Name | Description |
| :-- | :-- |
| \-t connect-key | 
This parameter is added in version 3.1.0a.

When a single device is connected, it is optional.

When multiple devices are connected, it is mandatory.

 |

**Return value**

| Value | Description |
| :-- | :-- |
| None | The **hdc wait** command ends when a properly connected device is identified. |

**Usage**

\# If the device is connected properly, the command executes with no printed output.
$ hdc wait # Connect to a single device.
$ hdc -t connect-key1 wait # Use -t to specify the device to be connected when there are multiple devices.

## USB Connection

**Check the environment**

| Item | Normal | Exception Handling |
| :-- | :-- | :-- |
| USB debugging | USB debugging is enabled. | If the USB debugging mode is not automatically enabled, restart the device. |
| USB data cable connection | The PC used for debugging is connected to the device USB port using a USB cable. | If you use a USB cable with low bandwidth and no data communication function, the device may fail to be identified. You are advised to use an original charging cable. |
| USB port | A USB port on the mainboard (USB port on the rear panel of a desktop computer or USB port on a laptop computer) is used. | If you use a conversion adapter, docking station, or USB port on the front panel of a desktop computer, issues such as low bandwidth and USB sync problems may occur, which results in frequent disconnections. Therefore, direct connection between the PC and the device is recommended. |
| hdc environment variable | The help information is displayed after the **hdc -h** command is executed. | For details, see [Environment Setup](#environment-setup). |
| Driver | After the device is connected via hdc, **HDC Device** or **HDC Interface** is displayed in **Device Manager**. | For details, see [What should I do if the device cannot be identified](#what-should-i-do-if-the-device-cannot-be-identified). |

**Procedure**

1.  Connect to the device through a USB port.
    
2.  Run the following command to check the connected device:
    
    hdc list targets
    
    If the returned information contains the device ID, the USB connection is successful.
    
3.  After the device is found, run commands to interact with the device. If you want to perform hdc commands without the device ID, ensure that the device is not in TCP connection mode (the device information displayed by running the **hdc list targets** command does not contain **IP:port**) and directly connect to the device. For example:
    
    hdc shell
    

## TCP Connection

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e3/v3/EMwG2aoZRwydL3Z9mzzVEw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062030Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=26E7929497462503C1D1EA5E9B2CF694103D304DCA2D90834635436728D5AE0D)

The TCP debugging mode is not stable. You are advised to use it only in the test environment.

**Check the environment**

| Item | Normal | Exception Handling |
| :-- | :-- | :-- |
| Network connection | The PC and the device are on the same network. | Connect the PC and device to the same Wi-Fi network. |
| Network Status | Use **telnet IP:port** to check that the network connection between the PC and the device is normal. | Use a stable network. |
| hdc environment variable | The help information is displayed after the **hdc -h** command is executed. | For details, see [Environment Setup](#environment-setup). |

**Procedure**

1.  Go to **Settings** > **System** > **Developer options** and enable **Wireless debugging**.
    
2.  Record the IP address and port number displayed on the device in format **IP:port**.
    
3.  Connect to the device over TCP.
    
    hdc tconn IP:port
    
    If **Connect OK** is displayed, the connection is successful.
    
4.  Check the connection.
    
    hdc list targets
    
    The returned information is in format **IP:port**.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/98/v3/vyp48I9LRTOAe_u18phFTA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062030Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=925F3D5DBFB658CF5F24F4D1BD995040F13F377F9801C650BAEE42FEF1F6BC0B)
    
    To disable the TCP connection mode, disable **Wireless debugging** on the device or disconnect the network.
    

## Remote Connection

In a remote connection, the client (typically a local PC) connects over the network to the server (typically a server or development machine connected to the target device) to debug, control, and manage the target device remotely.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/54/v3/NMNJRDZSQhmRIMNk4T2oMA/en-us_image_0000002537925062.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062030Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=953D1565D3BA7471789104F17FB00FFF2F37D49A3B171E5B44488331C981DAF6)

Use the **\-s** parameter to specify the IP address and port number of the server. The setting is valid only when the current command is executed.

hdc -s \[IP:\]port \[command\]

| Command | Description |
| :-- | :-- |
| \-s | Specifies the IP address and port number of the current server process to listen for. |

**Parameters**

| Parameter | Description |
| :-- | :-- |
| IP | IP address to listen for. Both IPv4 and IPv6 addresses are supported. This parameter is optional. If no IP address is specified, the default IP address **127.0.0.1** is listened for. |
| port | Port to listen for. The value ranges from 1 to 65535. |
| command | Commands supported hdc. For details, see [hdc Commands](#hdc-commands). |

**Return value**

| Value | Description |
| :-- | :-- |
| Connect server failed. | Failed to connect to the server. |
| \-s content port incorrect. | The port number is out of range (1 to 65535). |

**Usage**

\# Run the command to obtain the device information in the server process of 127.0.0.1:8710:
$ hdc -s 127.0.0.1:8710 list targets

**Procedure**

1.  Configure the server
    
    After the server is connected to the corresponding hdc device through USB, run the following commands:
    
    $ hdc kill          # Terminate the local hdc service.
    $ hdc -s IP:8710 -m # Enable the hdc service for network forwarding.
                        # IP indicates the IP address of the server. To query the IP address, you can run the ipconfig command on Windows and run the ifconfig command on Unix.
                        # 8710 is the default port number. You can also set it to another port number, for example, 18710.
                        # After startup, the server prints logs.
    
2.  Connect to the client
    
    Ensure that the client can connect to the server IP address, and then run the following command:
    
    $ hdc -s IP:8710 \[command\] # IP indicates the IP address of the server, and 8710 indicates the port number set in step 1.
                               # If the port number changes, change the port number in this command accordingly.
                               # command can be any available hdc command, for example, list targets.
    

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c/v3/_hHc4sZBRvmAyRx21QLsRA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062030Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=0EE8B663D96903540092DF70179F67CA1BEC83A4E20CC84CB90BDE16827FB9D6)

If the **\-s** parameter is used to specify a server port, the system ignores the port set in the **OHOS\_HDC\_SERVER\_PORT** environment variable. If the **\-s** parameter is used to specify the server address, and the listening address is not the local loopback address (for example, **127.0.0.1**), pay attention to the access security.

## Switching Between USB Debugging and Wireless Debugging

The following table lists the commands for switching the connection mode.

| Command | Description |
| :-- | :-- |
| tmode usb | This command is invalid and cannot be used to enable the USB connection channel. You need to enable it on the device setting page. |
| tmode port \[port-number\] | Enables the network connection channel of the device. Then the daemon process on the device restarts, and the established connection is interrupted. You need to reconnect the device. |
| tmode port close | Disables the network connection channel of the device. Then the daemon process on the device restarts, and the established connection is interrupted. You need to reconnect the device. |
| tconn IP:port \[-remove\] | Connects to a specified device using **IP:port** and disconnects the device using the **\-remove** parameter. |

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fd/v3/2dIWNdOmR1CQDsWjNXMeIA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062030Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=76784D805E8D7BFBB904CF380944A8B1BDA8540A975C8691096ED52F6EA50F80)

You are advised to enable or disable the USB debugging and wireless debugging on the device.

## Enabling the Network Connection Channel

Run the following commands:

hdc tmode port \[port-number\]

**Parameters**

| Parameter | Description |
| :-- | :-- |
| port-number | Port number of the connection. The value ranges from 1 to 65535. |

**Return value**

| Value | Description |
| :-- | :-- |
| Set device run mode successful. | The operation is successful. |
| \[Fail\]ExecuteCommand need connect-key. | Failed to enable the network connection channel because no device exists in the list. |
| \[Fail\]Incorrect port range. | The port number is out of range (1 to 65535). |

**Usage**

$ hdc tmode port 65512
Set device run mode successful.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/35/v3/OBVnmc3DSW674msJzzCqgg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062030Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=3F1C4117062B544AE138A5135D8957D0E84A63C6FF4121325C5D42B6CC212BBF)

Before switching, ensure that the remote device and the local computer are on the same network. You can run the **ping** command to check the network connection.

1.  On the local PC, run the **ping** command.
    
2.  If the remote device returns response packets, the remote device and the local PC are on the same network.
    

Otherwise, do not run this command.

After the command is executed, the remote daemon exits and restarts. You need to reconnect to it.

## Disabling the Network Connection Channel

Run the following commands:

hdc tmode port close

**Return value**

| Value | Description |
| :-- | :-- |
| \[Fail\]ExecuteCommand need connect-key. | The command cannot be executed because the device list is empty. |

**Usage**

hdc tmode port close

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/04/v3/sgP7N_FwSn2F1u-14S-QZg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062030Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=722278DB5323EEF3BCBC59B380701B47FE559EF64F2457F10AF0FE5F21B9C81B)

After the command is executed, the remote daemon exits and restarts. You need to reconnect to it.

## Connecting to a Device over TCP

Connect to the specified device over TCP.

hdc tconn IP:port \[-remove\]

**Parameters**

| Parameter | Description |
| :-- | :-- |
| IP:port | IP address and port number of the device. |
| \-remove | An optional parameter used to disconnect a specified device. |

**Return value**

| Value | Description |
| :-- | :-- |
| Connect OK. | Device connected. |
| \[Info\]Target is connected, repeat operation. | The device is already connected. |
| \[Fail\]Connect failed. | Failed to connect the specified device. |

**Usage**

$ hdc tconn 192.168.0.1:8888
Connect OK

# Disconnect from the specified device.
$ hdc tconn 192.168.0.1:8888 -remove

#### Running Interactive Commands

hdc shell \[-b bundlename\] \[command\]

**Parameters**

| Parameter | Description |
| :-- | :-- |
| \-b bundlename | 
This parameter is added in 3.1.0e. The bundle name of a debug-type application. The command is executed in non-interactive mode in the data directory of the debug-type application.

For details, see [Accessing the App Sandbox in CLI Mode](../../../../../coding-and-debugging/debugging-your-app/device-file-access/document.md#section48216711204)

Currently, this parameter can be used only in non-interactive mode, and the **command** parameter must be specified to enter an interactive shell session.

Otherwise, commands are executed in the system root directory by default.

 |
| command | 

A single command to execute on the device. The command varies depending on the system type or version. You can run the **hdc shell ls /system/bin** command to obtain the supported command list. Currently, most commands are provided by [toybox](../../../debugging-commands/command-line-utilities/toybox/document.md). You can run the **hdc shell toybox --help** command to obtain the help information.

If this parameter is not specified, hdc starts an interactive shell session, in which you can enter commands such as **ls**, **cd**, and **pwd** at the command prompt.

 |

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/aa/v3/b8CzPul8S3qMbOJD3f-48g/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062030Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=1C6BE8A8FD95184B788BDB47FA8B8E17FD783E96EEDDB190C244B77F58A9A965)

If the **\[-b bundlename\]** parameter is specified, the installed application corresponding to the bundle name must be signed using the debug certificate and started on the device. For details about how to request and use the debug certificate, see [Requesting a Debug Certificate](https://developer.huawei.com/consumer/en/doc/app/agc-help-add-debugcert-0000001914263178).

**Return value**

| Value | Description |
| :-- | :-- |
| Command execution result. | Execution result of the command. For details, see the corresponding command output. |
| /bin/sh: XXX : inaccessible or not found. | The specified command is not supported. |
| \[Fail\]Error information. | The execution fails. For details, see [hdc Error Codes](#hdc-error-codes). |

**Usage**

\# Enter the interactive mode to run a command.
$ hdc shell
$

# Run the command in non-interactive mode.
$ hdc shell "ps -ef | grep hdcd"
shell         39491      1 1 14:40:58 ?     00:00:00 hdcd

# Query all available commands.
$ hdc shell help -a
---toybox---------------------------------------------------------------------

usage: toybox \[--long | --help | --version | \[command\] \[arguments...\]\]

With no arguments, shows available commands. First argument is
name of a command to run, followed by any arguments to that command.

--long  Show path to each command
...

# Specify the bundle name of an application to run the command in non-interactive mode in its data directory. The \*\*touch\*\*, \*\*rm\*\*, \*\*ls\*\*, \*\*stat\*\*, \*\*cat\*\* and \*\*mkdir\*\* commands are supported.
$ hdc shell -b com.example.myapplication ls data/storage/el2/base/

**Common Debugging Tools**

| Command | Description |
| :-- | :-- |
| [aa](../../../debugging-commands/ability-assistant/document.md) | Application debugging tool |
| [bm](../../../debugging-commands/bundle-manager/document.md) | Bundle manager |
| [cem](../../../debugging-commands/common-event-manager/document.md) | Common event manager |
| [anm](../../../debugging-commands/advanced-notification-manager/document.md) | Notification manager |
| [edm](../../../debugging-commands/enterprise-device-manager/document.md) | Enterprise device manager |
| [param](../../../debugging-commands/param/document.md) | Operating system parameter manager |
| [power-shell](../../../debugging-commands/power-shell/document.md) | Device power status conversion tool |
| [atm](../../../debugging-commands/access-token-manager/document.md) | Access token manager |
| [hilog](../hilog/document.md) | Log manager |
| [hidumper](../hidumper/hidumper/document.md) | System information export tool |
| [hitrace](../hitrace/document.md) | System logging and collection tool |
| [hiperf](../hiperf/document.md) | Performance analysis tool |
| [mediatool](../../../debugging-commands/command-line-utilities/mediatool/document.md) | Media resource library tool |
| [devicedebug](../../../debugging-commands/command-line-utilities/devicedebug/document.md) | Debugging application signal sending tool |
| [rawheap-translator](../../../debugging-commands/command-line-utilities/rawheap-translator/document.md) | .rawheap file parsing tool |

#### Managing Applications

| Command | Description |
| :-- | :-- |
| install src | Installs an application. |
| uninstall bundlename | Uninstalls an application. |

## Installing an Application

The [install command](../../../debugging-commands/bundle-manager/document.md#install) of the bm module is integrated into the device, which simplifies the application installation process. You can run the command on the PC to install applications. Run the following commands:

hdc install \[-cwd path|-r|-s|-w waitingTime|-u userId|-p|-h\] src

**Parameters**

| Name | Description |
| :-- | :-- |
| src | Used to specify the path of the application installation package. You can install [HAP](../../../../../getting-started/development-fundamentals/application-package-fundamentals/application-package-development-and-usage/hap/document.md) and inter-application [HSP](../../../../../getting-started/development-fundamentals/application-package-fundamentals/application-package-development-and-usage/hsp/document.md). Since API version 22, [APP](../../../../../getting-started/development-fundamentals/application-package-glossary/document.md#app) can be installed. |
| \-cwd | 
Used to modify the working directory.

This parameter is used to switch the **src** directory to the specified path during application installation. For example, when the new application is **test.hap** and the directory is **C:\\**, the actual installation file path is **C:\\test.hap**. If **\-cwd "D:\\"** is executed, the actual installation file path is **D:\\test.hap**.

 |
| \-r | Used to overwrite an existing HAP or HSP file. This parameter is optional. This parameter is not specified by default, indicating that the existing file will be overwritten. |
| \-s | Used to specify the path of the HSP for applications to be installed. This parameter is mandatory when installing an application HSP, and optional in all other scenarios. Each directory can contain only one HSP file. |
| \-w | Used to specify the wait time for the bm tool when installing the HAP. This parameter is optional. The minimum wait time is 180 seconds, the maximum is 600 seconds, and the default value is 180 seconds. |
| \-u | Used to specify the [user](../../../debugging-commands/bundle-manager/document.md#userid). By default, the application is installed for the current active user. This parameter is optional. |
| \-p | Used to specify the path of the HAP or HSP file to be installed. This parameter is optional. If multiple HAPs or HSPs are required, you can specify the folder path of the HAPs or HSPs. Since API version 22, you can specify the path of the APP file to be installed or the folder path of only one APP. |
| \-h | Used to display the help information about the [install command](../../../debugging-commands/bundle-manager/document.md#install) of the bm module. This parameter is optional. |

**Return value**

| Value | Description |
| :-- | :-- |
| 
\[Info\]App install path:XXX msg:install bundle successfully.

AppMod finish.

 | The installation is successful. |
| Error information. | The installation fails. |

**Usage**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/20/v3/e_w9h3cWRMCbD9eJiuV2xA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062030Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=3BF5DF9B7421F2926C9034D58066B29303B9337ED9DC08370C39610A79A46A06)

When the **install** command is executed to use the command parameters of the bm module, if the -w and -u parameters require combined use with their values, you must enclose the parameter variables and their values in quotation marks (for example, **"-w 180"** and **"-u 100"**). This prevents command execution failures caused by abnormal parameter parsing.

\# Install the example.hap file.
$ hdc install D:\\example.hap
\[Info\]App install path:D:\\example.hap msg:install bundle successfully.
AppMod finish

# Install the example.app file.
$ hdc install D:\\example.app
\[Info\]App install path:D:\\example.app msg:install bundle successfully.
AppMod finish

# Install the example.hap file (-r is supported by the install command of the bm module, which is used for overwrite installation).
$ hdc install -r D:\\example.hap
\[Info\]App install path:D:\\example.hap msg:install bundle successfully.
AppMod finish

# Install the example.hsp file (-s is supported by the install command of the bm module, which is mandatory for installing the HSP file).
$ hdc install -s D:\\example.hsp
\[Info\]App install path:D:\\example.hsp msg:install bundle successfully.
AppMod finish

# Install the example.hap file (-w is supported by the install command of the bm module, which specifies the wait time of the bm tool).
$ hdc "-w 180" install D:\\example.hap
\[Info\]App install path:D:\\example.hap msg:install bundle successfully.
AppMod finish

# Install the example.hap file (-u is supported by the install command of the bm module, which specifies the user ID).
$ hdc "-u 100" install D:\\example.hap
\[Info\]App install path:D:\\example.hap msg:install bundle successfully.
AppMod finish

# Install the application in D:\\hap\_dir (-p is supported by the install command of the bm module, which specifies the installation path).
$ hdc -p install D:\\hap\_dir
\[Info\]App install path:D:\\hap\_dir msg:install bundle successfully.
AppMod finish

## Uninstalling an Application

The [uninstall command](../../../debugging-commands/bundle-manager/document.md#uninstall) is integrated into the bm module on the device, which simplifies the uninstallation process. You can run the command on the PC to uninstall applications. Run the following commands:

hdc uninstall \[-n|-k|-s|-h\] bundlename

**Parameters**

| Name | Description |
| :-- | :-- |
| bundlename | Application installation package. |
| \-n | Used to uninstall an application with a specified bundle name. This parameter is optional. |
| \-k | Used to uninstall an application with or without retaining the application data. This parameter is optional. By default, the application data is deleted along the uninstall. |
| \-s | Used to uninstall an HSP. This parameter is mandatory only for the HSP uninstallation. |
| \-h | Used to display the help information about the [uninstall command](../../../debugging-commands/bundle-manager/document.md#uninstall) of the bm module. This parameter is optional. |

**Return value**

| Value | Description |
| :-- | :-- |
| 
\[Info\]App uninstall path: msg:uninstall bundle successfully.

AppMod finish.

 | The uninstallation is successful. |
| Reason why the uninstallation fails. | The uninstallation failed. |

**Usage**

\# Uninstall the com.ohos.example file.
$ hdc uninstall com.ohos.example
\[Info\]App uninstall path: msg:uninstall bundle successfully.
AppMod finish

# Uninstall the com.ohos.example file (-n is supported by the uninstall command of the bm module, which specifies the bundle name).
$ hdc uninstall -n com.ohos.example
\[Info\]App uninstall path: msg:uninstall bundle successfully.
AppMod finish

# Uninstall the com.ohos.example file (-k is supported by the uninstall command of the bm module, which is used to save application data during uninstallation).
$ hdc uninstall -k com.ohos.example
\[Info\]App uninstall path: msg:uninstall bundle successfully.
AppMod finish

# Uninstall the com.ohos.example file (-s is supported by the uninstall command of the bm module, which is mandatory during HSP uninstallation).
$ hdc uninstall -s com.ohos.example
\[Info\]App uninstall path: msg:uninstall bundle successfully.
AppMod finish

#### Transferring Files

| Command | Description |
| :-- | :-- |
| file send SOURCE DEST | Sends a local file to a remote device. |
| file recv DEST SOURCE | Receives a file from a remote device. |

## Sending a File to a Remote Device

Run the following commands:

hdc file send \[-a|-sync|-z|-m|-cwd path|-b bundlename\] SOURCE DEST

**Parameters**

| Name | Description |
| :-- | :-- |
| SOURCE | Path of the file to send. |
| DEST | 
Path of the target file.

Since API version 21, some operations on the media library file can be performed through hdc. (In earlier versions, "\[Fail\]Error opening file: ..." is displayed.)

Path of the media library file: **/mnt/data/<uid>/media\_fuse/Photo/** directory and its subdirectories. **<uid>** is the ID of the current user.

For details about how to operate the media library through hdc, see [mediatool](../../../debugging-commands/command-line-utilities/mediatool/document.md#hdc-commands).

 |
| \-a | Used to retain the file modification timestamp. |
| \-sync | 

Used to transfer only the files whose **mtime** is updated.

**mtime** (modified timestamp): timestamp after modification.

 |
| \-z | Used to compress and transmit files in LZ4 format. This parameter is unavailable. |
| \-m | 

Used to synchronize the DAC permission, UID, GID, and MAC permission during file transfer.

**DAC** (Discretionary Access Control): discretionary access control;

**uid** (User identifier): user identifier (or user ID);

**gid** (Group identifier): group identifier (or group ID);

**MAC** (Mandatory Access Control): mandatory access control (or non-discretionary access control).

 |
| \-cwd | 

Modifies the working directory.

This parameter is used to switch the **SOURCE** to a specified path during file transfer. For example, if the file is **test** and the directory is **/data**, the actual file path is **/data/test**. If **\-cwd "/user/"** is used, the actual file path is **/user/test**.

 |
| \-b | 

Used to specify the bundle name of the debug-type application. This parameter is added in 3.1.0e (If this parameter is used in an earlier version, the message "\[Fail\]Unknown file option: -b" is displayed).

For details, see [Accessing the App Sandbox in CLI Mode](../../../../../coding-and-debugging/debugging-your-app/device-file-access/document.md#section48216711204).

 |
| bundlename | Bundle name of the debug-type application. |

**Return value**

| Value | Description |
| :-- | :-- |
| FileTransfer finish, Size:1, File count = 1, time:10ms rate:0.00kB/s | A success message is displayed if the file is sent successfully. |
| Reason for the file sending failure | Error information is displayed if the file fails to be sent. |

**Usage**

$ hdc file send test /test/
FileTransfer finish, Size:xxx, File...

$ hdc file send -b com.example.myapplication test /test/ # Import the test file to the com.example.myapplication sandbox.
FileTransfer finish, Size:xxx, File...

$ hdc file send D:\\dest\\Camera/mnt/data/100/media\_fuse/Photo/ # Media library operation. Import all files in D:\\dest\\Camera to /mnt/data/100/media\_fuse/Photo/Camera/.
FileTransfer finish, Size:xxx, File...

$ hdc file send D:\\dest\\New directory/mnt/data/100/media\_fuse/Photo/Camera/ # Media library operation. Directories cannot be created in the media library.
\[Fail\]\[E005005\] Error create directory: ..., path:/mnt/data/100/media\_fuse/Photo/Camera//New directory

## Receiving a File from a Remote Device

Run the following commands:

hdc file recv \[-a|-sync|-z|-m|-cwd path|-b bundlename\] DEST SOURCE

**Parameters**

| Name | Description |
| :-- | :-- |
| SOURCE | Destination path on the local device. |
| DEST | 
Path of the file to send.

Since API version 21, some operations on the media library file can be performed through hdc. (In earlier versions, "\[Fail\]Error opening file: ..." is displayed.)

Path of the media library file: **/mnt/data/<uid>/media\_fuse/Photo/** directory and its subdirectories. **<uid>** is the ID of the current user.

For details about media library operations, see [mediatool](../../../debugging-commands/command-line-utilities/mediatool/document.md#hdc-commands).

 |
| \-a | Used to retain the file modification timestamp. |
| \-sync | 

Used to transfer only the files whose **mtime** is updated.

**mtime** (modified timestamp): timestamp after modification.

 |
| \-z | Used to compress and transmit files in LZ4 format. This parameter is unavailable. |
| \-m | 

Used to synchronize the DAC permission, UID, GID, and MAC permission during file transfer.

**DAC** (Discretionary Access Control): discretionary access control;

**uid** (User identifier): user identifier (or user ID);

**gid** (Group identifier): group identifier (or group ID);

**MAC** (Mandatory Access Control): mandatory access control (or non-discretionary access control).

 |
| \-cwd | 

Modifies the working directory.

This parameter is used to switch the **SOURCE** to a specified path during file transfer. For example, if the initial directory for receiving files is **/data/** but **\-cwd "/user/"** is used, the actual directory for receiving files is **/user/**.

 |
| \-b | 

Used to send files in the data directory of a specified debug-type application process. This parameter is added in version 3.1.0e.

For details, see [Accessing the App Sandbox in CLI Mode](../../../../../coding-and-debugging/debugging-your-app/device-file-access/document.md#section48216711204).

 |
| bundlename | Bundle name of the debug-type application process. |

**Return value**

| Value | Description |
| :-- | :-- |
| FileTransfer finish, Size:1, File count = 1, time:10ms rate:0.00kB/s | A success message is displayed if the file is received successfully. |
| Reason for the file receiving failure | Error information is displayed if the file fails to be received. |

**Usage**

$ hdc file recv /test/test ./
FileTransfer finish, Size:xxx, File...

$ hdc file recv -b com.example.myapplication /test/test # Export the sandbox file test/test of com.example.myapplication.
FileTransfer finish, Size:xxx, File...

$ hdc file recv /mnt/data/100/media\_fuse/Photo/Camera/File A # Export file A.
FileTransfer finish, Size:xxx, File...

$ hdc file recv /mnt/data/100/media\_fuse/Photo/Camera # Export the Camera directory and files in the directory.
FileTransfer finish, Size:xxx, File...

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/89/v3/PpqDJgLiSRWx-UtQKJCUqw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062030Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=8D024810E673F345721B14D7EF653DE5923F8749EDB4137A2603C193E2D99FB6)

To use the **\[-b bundlename\]** parameter, ensure that the installed application is signed by a debug certificate and started. For details about how to request and use the debug certificate, see [Requesting a Debug Certificate](https://developer.huawei.com/consumer/en/doc/app/agc-help-add-debugcert-0000001914263178).

**Version updates**: Since version 3.1.0a, Chinese characters can be used as file transfer command parameters, which facilitates the use in multi-language environments.

#### Port Forwarding

| Command | Description |
| :-- | :-- |
| fport ls | Displays all port forwarding tasks. |
| fport localnode remotenode | Sets a local port forwarding, which listens for requests from the local node and forwards the requests to the remote node. The task format is **\[/topic/body/section/table/tgroup/tbody/row/entry/b/forwarding {""}) :\[/topic/body/section/table/tgroup/tbody/row/entry/b/forwarding/forwarding {""}) (forwarding\] (forwarding\]**, for example, **tcp:1234**. |
| rport remotenode localnode | Sets a remote port forwarding, which listens for requests from the remote node and forwards the requests to the local node. The task format is **\[/topic/body/section/table/tgroup/tbody/row/entry/b/forwarding {""}) :\[/topic/body/section/table/tgroup/tbody/row/entry/b/forwarding/forwarding {""}) (forwarding\] (forwarding\]**, for example, **tcp:1234**. |
| fport rm taskstr | Deletes a port forwarding task. |

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2b/v3/VX_cluu5TV6KGt7hV1WB6w/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062030Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=1AB273AF00A1F237E5CE1362F58EA646B6D1687AF468B517ED434D755CA4D601)

Port forwarding type supported by the computer: TCP.

Port forwarding types supported by the device: TCP, dev, localabstract, localreserved, localfilesystem, jdwp, ark.

## Querying the Port Forwarding Task List

Query all local and remote port forwarding tasks.

hdc fport ls

**Return value**

| Value | Description |
| :-- | :-- |
| tcp:1234 tcp:1080 \[Forward\] | Local port forwarding. |
| tcp:2080 tcp:2345 \[Reverse\] | Remote port forwarding. |
| \[Empty\] | No port forwarding. |

**Usage**

$ hdc fport ls
connect-key tcp:2080 tcp:2345 \[Reverse\]
connect-key tcp:1234 tcp:1080 \[Forward\]

## Creating a Local Port Forwarding

Set a local port forwarding, which forwards data from the local node to the remote node.

hdc fport localnode remotenode

**Return value**

| Value | Description |
| :-- | :-- |
| Forwardport result:OK. | The port forwarding is set up properly. |
| \[Fail\]Incorrect forward command. | Failed to set up the port forwarding due to parameter errors. |
| \[Fail\]TCP Port listen failed at XXXX. | Failed to set up the port forwarding because the local port is in use. |
| \[Fail\]Forward parament failed. | The port forwarding format is incorrect, or the forwarding port protocol or port range is incorrect. |
| \[Fail\]Not support forward-type. | The current platform does not support the forwarding port protocol used in the parameter. |

**Usage**

$ hdc fport tcp:1234 tcp:1080
Forwardport result:OK

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4d/v3/yL9xunLnQoWa6wg28Vc4dA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062030Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=ED613B24173F8B340FEEAA6BB23DBEFA1894F5BE6C78035F6F5CF04662937A53)

When creating a local port forwarding task, the PC uses the TCP protocol and the specified **port**. By default, **127.0.0.1:port** is listened for. If the **\-e** parameter is used to specify the IP address of the host that to be listened when the service process starts, the PC listens for the **IP:port** specified by **\-e**.

## Creating a Remote Port Forwarding

Set up a remote port forwarding, which forwards data from a remote port to a local port.

hdc rport remotenode localnode

**Return value**

| Value | Description |
| :-- | :-- |
| Forwardport result:OK. | The port forwarding is set up properly. |
| \[Fail\]Incorrect forward command. | Failed to set up the port forwarding due to parameter errors. |
| \[Fail\]TCP Port listen failed at XXXX. | Failed to set up the port forwarding because the local port is in use. |
| \[Fail\]Forward parament failed. | The port forwarding format is incorrect, or the forwarding port protocol or port range is incorrect. |

**Usage**

$ hdc rport tcp:1234 tcp:1080
Forwardport result:OK

## Deleting a Port Forwarding Task

Delete a specified local port forwarding task or remote port forwarding task.

hdc fport rm taskstr

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/82/v3/1dUx3GkHTauBNUpg1flrIQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062030Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=B17B67F4BBE84435EEE139940C02B43ABC3CC6BDEE37BFCEA50640C939A8C35D)

**taskstr** specifies the local or remote port forwarding task to be deleted. You are advised to run the **hdc fport ls** command to query the task and then delete it.

**Parameters**

| Parameter | Description |
| :-- | :-- |
| taskstr | Port forwarding task, in the format of **tcp:XXXX tcp:XXXX**. |

**Return value**

| Value | Description |
| :-- | :-- |
| Remove forward ruler success, ruler:tcp:XXXX tcp:XXXX. | The port forwarding is removed successfully. |
| \[Fail\]Remove forward ruler failed, ruler is not exist tcp:XXXX tcp:XXXX. | Failed to remove the port forwarding task because it does not exist. |

**Usage**

$ hdc fport rm tcp:1234 tcp:1080
Remove forward ruler success, ruler:tcp:1234 tcp:1080

#### Managing Server Processes

| Command | Description |
| :-- | :-- |
| start \[-r\] | Starts the hdc process. You can use the **\-r** option to restart the process. |
| kill \[-r\] | Terminates the hdc process. You can use the **\-r** option to restart the process. |
| \-p | Executes a client command without querying the server process. |
| \-m | 
Starts a server process in the foreground.

Foreground startup mode (with the **\-m** parameter): Service logs are printed to the client window in real time.

Background startup mode (without the **\-m** parameter): The client does not print service logs. The log content is written to a local disk file. For details about the file storage path, see [Server Process Logs](#server-logs).

 |
| \-e | Specifies the local listening IP address in TCP port forwarding. The default value is **127.0.0.1**. This parameter must be used together with **\-m**. |

## Starting a Service

Start the hdc server.

hdc start \[-r\]

**Return value**

| Value | Description |
| :-- | :-- |
| No returned information | The server is started successfully. |

**Usage**

hdc start -r # Restart the server.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a8/v3/U87xHq5ORpa2Jj5eNmwKXg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062030Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=115677DE031AA88C15BAFB36998A39DDAF740C8EB154DE6DAB8EB3160A76CC0D)

When the hdc server is started and the system does not detect any running server, the log level setting priority is as follows: If the **\-l** parameter and the **OHOS\_HDC\_LOG\_LEVEL** environment variable are specified in the same command, the environment variable takes effect. If only the **\-l** parameter is specified, the log level specified by it is used. If neither parameter is specified, the server is started at the default log level **LOG\_INFO**.

## Terminating a Service

Run the following commands:

hdc kill \[-r\]

**Return value**

| Value | Description |
| :-- | :-- |
| Kill server finish. | The server is terminated successfully. |
| \[Fail\]Error information. | Failed to terminate the server. |

**Usage**

$ hdc kill -r # Terminate and restart the server. You can run the hdc -l 5 kill -r command to view the detailed restart log.
Kill server finish

$ hdc kill # Terminate the server.
Kill server finish

## Quick Command Execution

Executes a client command without querying the server process. If the service is not started, running this command does not restart the service. Before using the parameter, ensure that the service has been started. Run the following commands:

hdc -p \[command\]

**Parameters**

| Parameter | Description |
| :-- | :-- |
| command | Command to be executed. |

**Return value**

| Value | Description |
| :-- | :-- |
| Connect server failed. | Failed to connect to the server. |

**Usage**

$ hdc start # Start the server process.

$ hdc -p list targets # Execute the command without checking.
connect-key1
connect-key2
...

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/43/v3/prsLupPESM-z99wIzQ1Vdg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062030Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=8A3161A8281CA87CB98024EFCBC2F05769E1BB671EA22B72F6C44A2FE9C1723C)

When a command is executed without the **\-p** parameter specified, the client first checks whether a server process is running locally. If the system does not detect a running server process, the client automatically starts a server process and sets up a connection to transfer commands. If the system detects a running server process, the client directly connects to the server process and transfers commands.

## Starting a Server in the Foreground

Start the server process in the foreground.

hdc -m

**Return value**

| Value | Description |
| :-- | :-- |
| Initial failed. | The server process fails to be initialized. |
| 
\[I\]\[1970-01-01 00:00:00.000\] Program running. Ver: X.X.Xx Pid:XXX.

...

 | Logs of the corresponding level are printed to display the activity status of the server. |

**Usage**

$ hdc -s 127.0.0.1:8710 -m # Specify the network listening parameters of the current server process and start the server process.
\[I\]\[1970-01-01 00:00:00.000\]\[4f28\]\[xxxx.xxx:123\] Program running. Ver: 3.1.0e Pid:12345
...
$ hdc -e 0.0.0.0 -m # Set the local listening IP address to 0.0.0.0 for port forwarding and start the server process.
\[I\]\[1970-01-01 00:00:00.000\]\[4f28\]\[xxxx.xxx:123\] Program running. Ver: 3.2.0b Pid:12345
...

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ce/v3/jBYslOd1RcOJp4D29icOEw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062030Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=E9E005B0A00BE3A93C668906CD9E11E15817C2AE1A0F25B77420B30DAD4BC76C)

1.  In foreground startup mode, you can use the **\-s** parameter to specify the network listening parameters of the server process. If no IP address and port number are specified using the **\-s** parameter and the environment variable **OHOS\_HDC\_SERVER\_PORT** is not set, the system uses the default IP address and port number **127.0.0.1:8710**. You can also use the **\-e** parameter to specify the IP address for which the local host should listen during port forwarding. If **\-e** is omitted, it defaults to **127.0.0.1**.
    
2.  If the server process is started in the foreground, the default log output level is **LOG\_DEBUG**. To change the log level, use the **\-l** parameter.
    
3.  Only one server process instance is allowed in the running environment. If a server is running, a new server process instance cannot be started in the foreground.
    

#### Operating the Device

| Command | Description |
| :-- | :-- |
| hilog \[-h\] | Displays the log information of the device. You can run the **hdc hilog -h** command to obtain the supported parameters. |
| jpid | Displays the PIDs of started applications on the device. |
| track-jpid \[-a|-p\] | Displays the PIDs and bundle names of started applications on the device in real time. Only applications with the **debug** tag can be debugged. If no parameter is specified, only the PIDs and bundle names of started debug-type applications are displayed. If the\*\*-a\*\* parameter is used, the process tags of debug- and release-type applications are displayed. If the\*\*-p\*\* parameter is used, the process tags of debug- and release-type applications are not displayed. |
| target boot \[-bootloader|-recovery\] | Restarts the target device. You can use the **\-bootloader** option to enter the fastboot mode and the **\-recovery** option to enter the recovery mode. |
| target boot \[MODE\] | Restarts the target device. You can add a parameter to use the corresponding mode. **MODE** is a parameter supported by reboot in the **/bin/begetctl** command. You can run the \*\*hdc shell "/bin/begetctl -h |

## Printing Device Logs

Run the following commands:

hdc hilog \[-h\]

**Parameters**

| Parameter | Description |
| :-- | :-- |
| \-h | Parameters supported by HiLog. You can run the **hdc hilog -h** command to obtain the parameter list. |

**Return value**

| Value | Description |
| :-- | :-- |
| Returned value | Log information obtained. |

**Usage**

$ hdc hilog -h
Usage:
-h --help
  Show all help information.
  Show single help information with option:
...

## Displaying PIDs of Started Applications

Run the following commands:

hdc jpid

**Return value**

| Value | Description |
| :-- | :-- |
| PID list | PIDs of started applications on the device. |
| \[Empty\] | No process is started on the device. |

**Usage**

$ hdc jpid
1234
1080
...

## Displaying PIDs and Names of Started Applications in Real Time

Display the PIDs and names of the started applications on the device in real time.

hdc track-jpid \[-a|-p\]

**Parameters**

| Parameter | Description |
| :-- | :-- |
| Not specified | Displays the PIDs and bundle names of started debug-type applications only. |
| \-a | Displays the PIDs, bundle names, and process names of the debug-type and release-type applications, as well as the **debug** and **release** tags. |
| \-p | Displays the PIDs, bundle names, and process names of the **debug** and **release** applications, but does not display the **debug** and **release** tags. |

**Return value**

| Value | Description |
| :-- | :-- |
| PID and bundle/process name list | If no parameter is specified, only the PIDs of the started applications are displayed. If the **\-p** parameter is specified, the bundle names of the applications are displayed. If the **\-a** parameter is specified, both **debug** and **release** tags are displayed. |
| \[Empty\] | No JDWP-enabled application process is found. |

**Usage**

$ hdc track-jpid -a
1234 com.example.hello release
...

$ hdc track-jpid -p
1234 com.example.hello
...

## Restarting the Target Device

Run the following commands:

hdc target boot \[-bootloader|-recovery\]
hdc target boot \[MODE\]

**Parameters**

| Name | Description |
| :-- | :-- |
| Not specified | Used to restart a device. |
| \-bootloader | Used to restart a device to enter the **fastboot** mode. |
| \-recovery | Used to restart a device to enter the **recovery** mode. |
| MODE | Used to restart a device to enter the **MODE** mode. **MODE** is a parameter supported by **reboot** in the **/bin/begetctl** command. |

**Usage**

hdc target boot -bootloader  # Restart the device to enter the fastboot mode.
hdc target boot -recovery    # Restart the device to enter the recovery mode.
hdc target boot shutdown     # Shut down the device.

#### Security Commands

| Command | Description |
| :-- | :-- |
| keygen FILE | Generates a new key pair and saves the private key and public key to **FILE** and **FILE.pub**, respectively. **FILE** indicates the custom file name. You can specify the directory. The default directory is the current working directory. |

Run the following commands:

hdc keygen FILE

**Parameters**

| Parameter | Description |
| :-- | :-- |
| FILE | Custom file name. |

**Usage**

\# Generate the key and key.pub files in the current directory.
$ hdc keygen key

#### Querying the hdc Version

| Command | Description |
| :-- | :-- |
| \-v | Prints the client version information. |
| version | Prints the server process version information. |
| checkserver | Obtains the client and server process versions. |

## Querying the Client Version

Query the hdc client version.

hdc -v

**Return value**

| Value | Description |
| :-- | :-- |
| Ver: X.X.Xx. | hdc (SDK) client version information. |

**Usage**

$ hdc -v
Ver: 3.1.0e

## Querying the Server Version

Query the server version.

hdc version

**Return value**

| Value | Description |
| :-- | :-- |
| Ver: X.X.Xx. | hdc (SDK) server version information. |

**Usage**

$ hdc version
Ver: 3.1.0e

## Querying the Client and Server Versions

Run the following commands:

hdc checkserver

**Return value**

| Value | Description |
| :-- | :-- |
| Client version: Ver: X.X.Xx, Server version: Ver: X.X.Xx. | The client and server versions. |

**Usage**

$ hdc checkserver
Client version: Ver: 3.1.0e, Server version: Ver: 3.1.0e

#### Exporting System Information

Run the following commands:

hdc bugreport \[FILE\]

**Parameters**

| Parameter | Description |
| :-- | :-- |
| FILE | Specifies the name of the system information file. This parameter is optional. You can specify the storage directory. The default directory is the current working directory. |

**Return value**

| Value | Description |
| :-- | :-- |
| 
\-------------------------------\[base\]-------------------------------

BuildId: xxx

RleaseType: xxx

OsVersion: default/default/default/default/xxx

DeviceType: default

Manufacture: default

\-----

 | Defines basic device information. |

**Usage**

$ hdc bugreport
-------------------------------\[base\]-------------------------------

BuildId: xxx
RleaseType: xxx
OsVersion: default/default/default/default/xxx
DeviceType: default
Manufacture: default
-----

#### hdc Debugging Logs

## Server Logs

**Specify the log level at runtime**

Specify the hdc log level. The default value is **LOG\_INFO**.

hdc -l \[level\] \[command\]

**Parameters**

| Parameter | Description |
| :-- | :-- |
| \[level\] | 
Used to specify the log level at runtime. The level increases with the number. When a log level is set, the current level and lower levels are enabled. For example, if the log level is set to 3, logs of levels 1 to 3 can be printed.

0: LOG\_OFF

1: LOG\_FATAL

2: LOG\_WARN

3: LOG\_INFO

4: LOG\_DEBUG

5: LOG\_ALL

6: LOG\_LIBUSB

 |
| command | Command to be executed. |

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/91/v3/yreXDpAUT92ynRtKXy7Obg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062030Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=7DB01345085AA881D063F6C5952A19672F734ED6CC7FC69BC1B6EF90300F7BA7)

1.  When the log level is set to **6** (**LOG\_LIBUSB**), incremental logs related to libusb are generated. The incremental logs are detailed and contain a large amount of data, which helps accurately diagnose USB-related exceptions in server processes. You are advised to set the log level as required. USB-related operations are mainly performed by server processes. Therefore, incremental logs are available only for server processes. Accordingly, the client logs almost do not contain incremental log information.
    
2.  You can change only the log levels of the current client and server.
    

**Return value**

| Value | Description |
| :-- | :-- |
| Log information. | Logs of the specified level. |

**Usage**

\# Run the shell ls command to print logs of the LOG\_DEBUG level and lower levels on the client.
$ hdc -l 5 shell ls
\[D\]\[1970-01-01 00:00:00.000\]\[12dc\]\[xxxx.xxx:123\] Mallocchannel:1234567
...

# Start the server in the foreground and specify the log level to LOG\_LIBUSB.
$ hdc kill && hdc -l 6 -m
Kill server finish
\[I\]\[1970-01-01 00:00:00.000\]\[4f28\]\[xxxx.xxx:123\] Program running. Ver: 3.1.0e Pid:12345
...

# Start the server in the background and specify the log level to LOG\_LIBUSB.
$ hdc kill && hdc -l 6 start
Kill server finish
\[D\]\[1970-01-01 00:00:00.000\]\[12dc\]\[xxxx.xxx:123\] Mallocchannel:1234567
...

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ed/v3/puU2LQXDQGC63mBGr7ajSw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062030Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=942618146EDAB76B46132D70155493B9C5848422345770DE0F9ECE3EA16EFAFE)

You can use the **\-m** parameter to start the server in the foreground and view its log output directly. To exit the process, press **Ctrl+C**.

If the server is started in the background, you can view the log output in **hdc.log**.

**Obtain logs**

Run the following command to enable the functionality of obtaining logs:

hdc kill
hdc -l 5 start

The collected logs are stored in the following path.

| OS | Path | Remarks |
| :-- | :-- | :-- |
| Windows | %temp%\\ | 
Example: **C:\\Users\\Username\\AppData\\Local\\Temp**.

Replace Username with the actual one.

 |
| Linux | /tmp/ | \- |
| macOS | $TMPDIR/ | You can run the **echo $TMPDIR** command to view the actual path, and **cd $TMPDIR** to go to the corresponding directory. |

The log file types are as follows.

| Type | Name Format | Functionality | Remarks |
| :-- | :-- | :-- | :-- |
| Real-time log | hdc.log | Records server logs in real time. | Each time the hdc server is restarted, the original log is renamed and a new **hdc.log** is recorded. |
| Temporary historical log | hdc-%Y%m%d-%H%M%S.log | Dumps intermediate files generated during historical log archiving. | For example, if the time is 16:18:57.921 on September 19, 2024, the time format is **20240919-161857921**, and the name of the generated temporary log file is **hdc-20240919-161857921.log**. |
| Archived historical logs | hdc-%Y%m%d-%H%M%S.log.tgz | Compresses and stores historical logs. | The archive file is a compressed file of the **.tgz** type. You can use a decompression tool to obtain the file. For example, if the temporary name of a historical log file is **hdc-20240919-161857921.log**, the name of the corresponding archived historical log file is **hdc-20240919-161857921.log.tgz**. After the archived historical log file is generated, the corresponding temporary historical log file is automatically deleted. |
| Temporary real-time log | .hdc.cache.log | Records temporary caches generated by real-time logs. | \- |

## Device Logs

Use HiLog to obtain the corresponding logs.

hdc shell hilog -w start                              # Enable HiLog log flushing. Executing this command again when the HiLog tool is already enabled will result in an error.
hdc shell hilog -w stop                               # Disable HiLog log flushing. Executing this command again when the HiLog tool is already disabled will result in an error.
hdc shell ls /data/log/hilog                          # View the flushed HiLog logs.
hdc file recv /data/log/hilog {local\_path}            # Obtain the flushed HiLog logs (including kernel logs). {local\_path} varies according to the system. Replace it with the actual path.

#### Options

## OHOS\_HDC\_SERVER\_PORT

Used to set the listening port number when the server is running. This port is used for data communication between the client and the server.

When the server starts, it listens to port **8710** of the PC by default. The client uses TCP to connect to the server through this port. If port 8710 of the PC has been used or you want to use another port, you can add the environment variable **OHOS\_HDC\_SERVER\_PORT** to the system environment variable to listen for any unoccupied port when the server starts. You can set the port number to a value ranging from 1 to 65535.

For example, set **OHOS\_HDC\_SERVER\_PORT** to **18710**.

## OHOS\_HDC\_LOG\_LEVEL

Used to set the log level for the server. For details, see [Server Logs](#server-logs).

## OHOS\_HDC\_HEARTBEAT

Used to set whether to enable the heartbeat functionality for the server and daemon. This functionality is enabled by default.

After the server and daemon are started, they send heartbeat packets to each other and record the heartbeat packets in hdc logs for checking the device connection status.

When the environment variable OHOS\_HDC\_HEARTBEAT is set to **1** for the server, its heartbeat functionality is disabled. When the device is connected to the PC, the server notifies the daemon that the heartbeat functionality is disabled and does not send heartbeat packets to each other.

When OHOS\_HDC\_HEARTBEAT is set to other values, the heartbeat functionality is enabled.

## OHOS\_HDC\_CMD\_RECORD

Sets whether to enable the hdc command recording functionality. This functionality is enabled by default. This functionality records only the executed hdc commands but not the command execution results.

When this parameter is set to **1**, the command recording functionality is enabled. When it is not set or set to any other number, the command recording functionality is disabled.

This parameter is supported since API version 20.

The recording log files are stored in the following paths:

| OS | Path | Remarks |
| :-- | :-- | :-- |
| Windows | %temp%\\hdc\_cmd\\ | Example: **C:\\Users\\Username\\AppData\\Local\\Temp\\hdc\_cmd<br/>** (Replace the user name with the actual one.) |
| Linux | /tmp/hdc\_cmd/ | \- |
| macOS | $TMPDIR/hdc\_cmd/ | \- |

## OHOS\_HDC\_ENCRYPT\_CHANNEL

Used to set the encryption functionality of the TCP connection channel between the server and the daemon. By default, the encryption functionality is disabled.

When this parameter is set to **1**, the channel encryption functionality is enabled. When it is not set or set to any other number, this functionality is disabled.

This parameter is supported since API version 20.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ea/v3/Gfuz4o5HQeuMAnaqEkTymQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062030Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=F049ADCB4C75B3D363A2B08D48616A85EACAC68A7EBC6D6DDA0E6AB77925E137)

When the server is running, it listens for port 8710 of the PC by default. You can customize the listening port by setting the system environment variable **OHOS\_HDC\_SERVER\_PORT**.

## Configuring Environment Variables

The following example describes how to set environment variables by setting **OHOS\_HDC\_LOG\_LEVEL** to 5. For details, see [Environment Setup](#environment-setup).

| OS | Configuration Method |
| :-- | :-- |
| Windows | In **Settings**, search for **View advanced system settings**. In **Environment Variables** > **System Variables** > **Path**, click **Edit** to add the environment variable **OHOS\_HDC\_LOG\_LEVEL** whose value is **5**. After the configuration is complete, click **OK**. Restart the CLI or other software that uses HarmonyOS SDK for the new environment variable to take effect. |
| Linux | Add **export OHOS\_HDC\_LOG\_LEVEL=5** to the end of the **~/.bash\_profile** file, save the file, and run the **source ~/.bash\_profile** command for the current environment variable to take effect. |
| macOS | Add **export OHOS\_HDC\_LOG\_LEVEL=5** to the end of the **~/.zshrc** file, save the file, and run the **source ~/.zshrc** command for the current environment variable to take effect. Restart the CLI or other software that uses HarmonyOS SDK for the new environment variable to take effect. |

#### hdc Version Mappings

| hdc Version | API Version | New Features |
| :-- | :-- | :-- |
| 3.1.0a | 12 | The **wait** command supports the **\-t** parameter. For details, see [Waiting for Device Connection](#waiting-for-device-connection). |
| 3.1.0e | 15 or later | 
\- The **file send** command supports the **\-b** parameter. For details, see [Transferring Files](#transferring-files).

\- The **file recv** command supports the **\-b** parameter. For details, see [Transferring Files](#transferring-files).

\- The **shell** command supports the **\-b** parameter. For details, see [Running Interactive Commands](#running-interactive-commands).

 |
| 3.2.0b | 20 | \- The port forwarding task can listen for the IP address of the remote host. For details, see [Creating a Local Port Forwarding](#creating-a-local-port-forwarding). |

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f0/v3/qrJg6m3yQ_SFnU4C-O6cxg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062030Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=99CCFE29745974755E89ED99D901908F6858DF3EA72B3C8462007C84AFA26231)

If the current hdc version is too early, the compatibility of some functionalities may be affected. You can download the latest version based on the API version description.

#### FAQs

## What should I do if the device cannot be identified

**Symptom**

After the **hdc list targets** command is executed, the command output is **\[Empty\]**.

**Possible Causes and Solution**

**Scenario 1**

Check whether the target device is displayed in **Device Manager**.

Windows:

Check whether **HDC Device** (for a single-port device) or **HDC Interface** (for a composite-port device) exists under **Universal Serial Bus Controllers** in **Device Manager**.

Linux:

Run the **lsusb** command. Check whether **HDC Device** or **HDC Interface** is displayed in the command output.

macOS:

Check the system information or system overview of the USB device as follows:

1.  Press and hold the **Option** key, and click the menu (usually in the upper left corner of the screen).
    
2.  Choose **System Information** or **System Overview**.
    
3.  Select **USB** on the left.
    
4.  Check whether **HDC Device** or **HDC Interface** exists in the device tree.
    

**Solution**

If the hdc device is not displayed in the preceding environments, it is not correctly identified. You can try the following methods to solve the problem:

1.  Use another physical USB port.
    
2.  Change the USB cable.
    
3.  Use another PC.
    
4.  Enable USB debugging on the device.
    
5.  When the trust confirmation prompt is displayed, select **Trust** or **Always trust**.
    
6.  Restore the device to its factory settings.
    

**Scenario 2**

A USB device exists, but the driver is damaged. **HDC Device** with a warning icon in yellow is displayed.

Symptom: This problem usually occurs in Windows. In **Device Manager/Universal Serial Bus Device**, **HDC Device** is displayed with a yellow warning icon, indicating that the device cannot work properly. To resolve the problem, reinstall the driver. If the problem persists, use another USB cable, docking station, or USB port.

To reinstall the driver, perform the following steps:

1.  Open **Device Manager**, and right-click the **HDC Device** with a warning icon.
    
2.  In the displayed menu, choose **Update driver**.
    
3.  In the first prompt window, click **Browse my computer for drivers**.
    
4.  In the second prompt window, click **Let me pick from a list of available drivers on my computer**.
    
5.  In the third prompt window, deselect **Show compatible hardware**, select **WinUsb Device** for **Manufacture** and **WinUsb Device** for **Model**, and click **Next**.
    

**Scenario 3**

If "\[Fail\]Failed to communicate with daemon" is displayed when the device is connected, the possible causes are:

Symptom: After the hdc command is executed on the CLI, "\[Fail\]Failed to communicate with daemon" is returned.

Possible causes are as follows:

1.  The hdc or SDK does not match the device. If the device is the latest version, update the hdc or SDK tool to the latest version.
    
2.  The port is occupied.
    

When hdc and hdc\_std use the same port simultaneously, the port set by **OHOS\_HDC\_SERVER\_PORT** will cause a conflict. (If the variable is not set, the default port **8710** is used, resulting in the same conflict.) This problem also occurs when other software occupies the default hdc port.

**Scenario 4**

"Connect server failed" is displayed when the device is connected.

The possible causes are as follows:

**Port preemption**

Solution:

1.  Check the software processes that have the built-in hdc functionality.
    
    If the software (DevEco Studio or DevEco Testing) that has the built-in hdc functionality is running, stop these software processes and run hdc commands.
    
2.  Check hdc port status.
    
    For example, if **OHOS\_HDC\_SERVER\_PORT** is set to **8710**, run the following commands to check the port status.
    
    Unix:
    
    netstat -an |grep 8710
    
    Windows:
    
    netstat -an |findstr 8710
    
    If the port is used by another software, stop the software process or change the **OHOS\_HDC\_SERVER\_PORT** environment variable to another port number.
    
3.  Make sure the server of any other version is stopped.
    
    Windows:
    
    Choose **Task Manager** > **Details**, right-click the **hdc.exe** process and choose **Open file location**. Check whether the location is the same as that configured in the environment variable. If not, stop the **hdc.exe** process by running the **hdc kill** command or terminating the process in **Task Manager**. Then, run the hdc command again. (After the server is stopped, running the hdc command will restart it.)
    
    Unix:
    
    Run the **ps -ef |grep hdc** command to query the hdc server and check whether the process startup location is the hdc file location set by the environment variable **Path**. If not, stop the hdc process by running the **hdc kill** or **kill -9 hdc** PID command, and run the hdc command again. (After the server is stopped, running the hdc command will restart it.)
    

**Registry exception**

Solution: Clear the registry. The procedure is as follows:

1.  Press **Win+R** to open the **Run** dialog box, and enter **regedit** to open the registry.
    
2.  Enter the following address in the address bar, and press **Enter** to access the registry of the USB device driver.
    
    Computer\\HKEY\_LOCAL\_MACHINE\\SYSTEM\\CurrentControlSet\\Control\\Class\\{88bae032-5a81-49f0-bc3d-a4ff138216d6}
    
3.  Right-click **UpperFilters** and choose **Modify** from the shortcut menu. Back up and clear the value data in the file. If the fault persists, restore the data.
    
4.  Refresh the **Device Manager**, remove and reconnect the USB cable to the USB port, or restart the PC.
    

## What should I do if a non-root user cannot find the device when running the hdc command on Linux or macOS?

**Symptom**

After a non-root user connects the device to the PC through USB on Linux or macOS, the device cannot be found by running the **hdc list targets** command.

**Possible Causes and Solution**

By default, a non-root user does not have the permission to operate USB devices. To enable the permission, perform the following steps:

1.  On masOS, stop the hdc service and run the **sudo** command to restart it.
    
    sudo hdc kill
    sudo hdc start
    
2.  On Linux:
    
    -   To temporarily grant the full operation permission on a USB device, run the following command:
        
        sudo chmod -R 777 /dev/bus/usb/
        
    -   To permanently change the operation permission on a USB device, do as follows:
        
        -   Run the **lsusb** command to obtain the vendorID and productID of the USB device.
            
        -   Create an **udev** rule.
            
            Edit the **udev** loading rule and replace the default **idVendor** and **idProduct** values of the device with the values obtained in the previous step.
            
            **MODE="0666"** indicates the permissions of **GROUP** (the user group) for the USB device. Ensure that the login user is in the user group.
            
            $ sudo vim /etc/udev/rules.d/90-myusb.rules
            SUBSYSTEMS=="usb", ATTRS{idVendor}=="067b", ATTRS{idProduct}=="2303", GROUP="users", MODE="0666"
            
        -   Restart the computer or reload the **udev** rule.
            
            sudo udevadm control --reload
            

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2b/v3/nl0J1qeSRVCx1kZAXzhKkQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062030Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=415A1158CA91EAE062EDD7C9DBEB013F897AC044DE07D9350CA60D77188BCF5B)

Enabling the USB device operation permission for non-root users can solve the problem that the device cannot be found due to insufficient permission when hdc is used in Linux. However, granting the permission may cause potential security issues. You are advised to evaluate whether to enable the permission based on the application scenario.

## What should I do if hdc cannot run?

**Symptom**

The hdc commands cannot be executed on the CLI.

**Possible Causes and Solution**

1.  The operating environment is abnormal.
    
    Linux: 64-bit Ubuntu 18.04 or later is recommended. If a libc++.so reference error occurs, run the **ldd** or **readelf** command to check the library reference.
    
    macOS: macOS 11 or later is recommended.
    
    Windows: Windows 10 or Windows 11 64-bit is recommended. If the WinUSB library or driver is missing in an earlier version, use [Zadig](https://github.com/pbatard/libwdi/releases) to update it. For devices that require driver installation, use Zadig to install the libusb-win32 driver. For details, see [Zadig](https://github.com/pbatard/libwdi/releases).
    
2.  Improper running mode: Use the correct command to run the hdc tool instead of double-clicking the file.
    

## What should I do if garbled characters are displayed when the hdc file send/recv command is used to transfer Chinese files?

**Symptom**

Garbled characters are displayed when the **hdc file send/recv** command is executed. For example, when the **file recv** command is used to send a file with a Chinese name from the device to the local host, the error message "\[Fail\]Error opening file: no such file or directory, path:XXXXX" is displayed, and the path contains garbled characters.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d3/v3/VwInYHXwSnS5cokwKGMxtw/en-us_image_0000002568684839.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062030Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=68581A5D35E830C290DE6C09680F4A306CEBC205EB249316323B89FDE34F687C)

**Possible Causes and Solution**

Since 3.1.0a, the file transfer command supports Chinese characters in the parameter path. Update the version to the latest version.

Run the **hdc checkserver** command to check the current version. If the version is earlier than 3.1.0a, upgrade the SDK to API version 12 or later.

## What should I do if "Unauthorized" is displayed after the hdc list targets command is executed?

**Symptom**

When the **hdc list targets** command is executed to query the connected devices, "Unauthorized" is displayed next to the device ID.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d3/v3/68tpCCn8R_yRC6IhkoHcCw/en-us_image_0000002568764849.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062030Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=69AD0D3C2C1F51E4C4C60166083F8D8BF338F7B5D82087B87DABE08E285D205D)

**Possible Causes and Solution**

1.  Unauthorized first connection: After the device is connected and unlocked, the trust confirmation prompt appears. Select **Always trust** or **Trust** to complete authorization.
    
2.  Authorization prompt closed or authorization denied: The authorization prompt on the device will close after timeout, or you may have selected **Distrust** to reject authorization. To re-authorize, go to **Settings** > **System** > **Developer options** > **USB debugging/Wireless debugging**, disable the debugging function, or run the **hdc kill -r** command to restart the server process. Then the trust confirmation dialog will appear again. Select **Always trust** or **Trust** to complete authorization.
    

## What should I do if "CryptAcquireContext second failed" is displayed when a hdc command is executed?

**Symptom**

When a hdc command is executed, the error message "CryptAcquireContext second failed XXX" is displayed?

**Possible Causes and Solution**

Modify the registry information in the PC as follows:

1.  Press **Win+R** to open the **Run** dialog box, and enter **regedit** to open the registry.
    
2.  Enter the following address in the address bar, and press **Enter**.
    
    **Computer\\HKEY\_LOCAL\_MACHINE\\SOFTWARE\\Microsoft\\Cryptography\\Protect\\Providers\\df9d8cd0-1501-11d1-8c7a-00c04fc297eb**;
    
3.  Right-click to create a DWORD (32-bit) value (D), set its name to **ProtectionPolicy** and value to **1** (hexadecimal), and click **OK**.
    
4.  Restart the computer. The problem is solved.
    

## What should I do if "Unknown USB Device (Device Descriptor Request Failed)" is displayed in Windows Device Manager?

**Symptom**

When a device is connected using USB, "Unknown USB Device (Device Descriptor Request Failed)" is displayed in **Universal Serial Bus controllers** of **Device Manager** on the PC.

**Possible Causes and Solution**

1.  Go to the Windows Service Management page (by inputting **services.msc**) and restart the **Plug and Play** service.
    
2.  Uninstall the faulty USB device in Device Manager and remove the USB cable.
    
3.  Restart the computer.
    

If this problem persists after these steps or after you connect the device to another computer, the driver of the USB device may be faulty. In this case, replace the USB cable.

## What should I do if the hdc command fails to be executed?

**Symptom**

If the hdc command output is not as expected, the possible causes are as follows:

1.  Scenario 1: When the hdc command is executed, the message "Connect server failed" is displayed.
    
2.  Scenario 2: When the hdc command is executed, the message "connect failed status:-4078" is displayed.
    
3.  Scenario 3: No output is displayed after the hdc command is executed.
    

**Possible Causes and Solution**

To solve the port exception problem, perform the following steps:

1.  Check the software processes that come with hdc, including software with built-in hdc, such as DevEco Studio and DevEco Testing. If such software exists, close it and then run the hdc commands.
    
2.  Check hdc port status. For example, if **OHOS\_HDC\_SERVER\_PORT** is set to **8710**, run the following command to check the port status.
    
    Unix:
    
    netstat -an |grep 8710
    
    Windows:
    
    netstat -an |findstr 8710
    
    If the port is used by another software, terminate the software process or change the **OHOS\_HDC\_SERVER\_PORT** environment variable to another port number.
    
3.  Make sure the server of any other version is stopped.
    
    Windows: Choose **Task Manager** > **Details**, right-click the **hdc.exe** process and choose **Open file location**. Check whether the location is the same as that configured in the environment variable. If not, stop the **hdc.exe** process by running the **hdc kill** command or terminating the process in **Task Manager**. Then, run the hdc command again. (After the server is stopped, running the hdc command will restart it.)
    
    Unix: Run the **ps -ef | grep hdc** command to query the hdc server process running in the background and check whether the process startup location is the hdc file location set by the environment variable **Path**. If not, stop the hdc process by running the **hdc kill** or **kill -9 hdc** PID command, and run the hdc command again. (After the server is stopped, running the hdc command will restart it.)
    

## Common Procedure for Troubleshooting Other Problems

1.  Run the **hdc list targets** command.
    
2.  Check whether **HDC Device** exists in device management.
    
3.  Run the **hdc kill** command to stop the server and run the **hdc -l5 start** command to collect logs. (The **hdc.log** file is stored in the **TEMP** directory on the execution end. The directory varies depending on the operating system. For details, see [Server Logs](#server-logs).)
    
4.  Locate the problem based on the **hdc.log** file.
    

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d9/v3/8JLCptsfTieQxXHrbDl-fQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062030Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=A9F37BD92C71CA8C540A081A014BE1316EF5371F062C36F75946C9B5FB619435)

For more FAQs, see [FAQs](https://developer.huawei.com/consumer/en/doc/harmonyos-faqs/faqs-performance-analysis-kit).

#### hdc Error Codes

## E000001 hdc Version Too Early

**Error Message**

The sdk hdc.exe version is too low, please upgrade to the latest version.

**Symptom**

The hdc version is too early. You need to update it to the latest version.

**Possible Causes**

If the client version is earlier than 3.0.0b, authorization is not supported and the client cannot access the system.

**Solution**

Update the hdc to the latest version by referring to [hdc Version Mappings](#hdc-version-mappings).

## E000002 Unauthorized Device

**Error Message**

The device unauthorized.

This server's public key is not set.

Please check for a confirmation dialog on your device.

Otherwise try 'hdc kill' if that seems wrong.

**Symptom**

The device is not authorized. Check whether the device has been authorized on the trust confirmation prompt. If the device has been authorized, run the **hdc kill** command and then run the debugging command again.

**Possible Causes**

1.  Scenario 1: When the device is connected for the first time, the debugging computer is not authorized on the device.
    
2.  Scenario 2: If the trust confirmation prompt is displayed and you select **Trust** instead of **Always trust**, you need to authorize the device again after reconnecting to the device.
    

**Solution**

1.  Scenario 1: In the trust confirmation prompt displayed on the device, select **Trust**.
    
2.  Scenario 2: Go to **Settings** > **System** > **Developer options**, re-enable **Debugging**, and re-connect the device to authorize it. Alternatively, run the **hdc kill -r** command to restart hdc to trigger the trust confirmation prompt again, and select **Always trust**.
    

## E000003 Unauthorized User on the Device

**Error Message**

The device unauthorized.

The user denied the access for the device.

Please execute 'hdc kill' and redo your command,

then check for a confirmation dialog on your device.

**Symptom**

The device is not authorized. If the device rejects the debugging authorization, run the **hdc kill** command and run the debugging command again. Then check the trust confirmation prompt on the device.

**Possible Causes**

1.  The trust confirmation prompt on the device is automatically closed due to timeout, and the authorization is not confirmed.
    
2.  You have selected **Don't trust** to reject the authorization.
    

**Solution**

Go to **Settings** > **System** > **Developer options**, re-enable **Debugging**, and re-connect the device to authorize it. Alternatively, run the **hdc kill -r** command to restart hdc to trigger the trust confirmation prompt again, and select **Always trust**.

## E000004 Unstable Communication Connection

**Error Message**

The communication channel is being established.

Please wait for several seconds and try again.

**Symptom**

It indicates that the communication channel is not established and asks you to try again after several seconds.

**Possible Causes**

The network or USB connection is not established or unstable.

**Solution**

After the device is connected, wait for about 10 seconds. After the connection is established, debug the device.

## E001000 tmode Does Not Support USB Debugging

**Error Message**

For USB debugging, please set it on the device's Settings UI.

**Symptom**

The **hdc tmode** command cannot be used to set USB debugging.

**Possible Causes**

The **hdc tmode usb** command is deprecated. For details, see [Switching Between USB Debugging and Wireless Debugging](#switching-between-usb-debugging-and-wireless-debugging).

**Solution**

For details about the **tmode usb** command, see [Switching Between USB Debugging and Wireless Debugging](#switching-between-usb-debugging-and-wireless-debugging).

## E001001 Unknown Command

**Error Message**

Unknown command.

**Symptom**

The **hdc tmode** command is incorrect.

**Possible Causes**

Parameters are missing or incorrect in the **hdc tmode** command.

**Solution**

Complete the command by referring to [Switching Between USB Debugging and Wireless Debugging](#switching-between-usb-debugging-and-wireless-debugging).

## E001003 USB Connection Error

**Error Message**

USB communication abnormal, please check the USB communication link.

**Symptom**

The USB communication is abnormal. Check the USB communication link.

**Possible Causes**

1.  The USB cable is loose or disconnected.
    
2.  After the **hdc shell reboot** command is executed, the device restarts and is disconnected. In this case, no action is required.
    
3.  After the **hdc tmode port XXX** command is executed, the USB debugging mode is switched to the wireless debugging mode, and the device is disconnected. In this case, no action is required.
    

**Solution**

1.  Ensure that the USB cable is securely connected to the device and computer. If the connection is normal but the issue persists, change the USB cable or USB port.
    
2.  Update the hdc to the latest version by referring to [hdc Version Mappings](#hdc-version-mappings).
    

## E001104 Invalid IP Address in the tconn Command

**Error Message**

IP address incorrect.

**Symptom**

The IP address format is incorrect.

**Possible Causes**

When the **tconn** command is used for wireless debugging connection, the input IP address is not in IPv4 format.

**Solution**

Check whether the input IP address is valid by referring to the correct format **127.0.0.1:8888**. If invalid characters exist, correct the IP address and re-establish the connection.

## E001005 Unknown or Disconnected Device

**Error Message**

Device not found or connected.

**Symptom**

No connected device is found or the device is not connected.

**Possible Causes**

The device is disconnected.

**Solution**

For details, see [What should I do if the device cannot be identified](#what-should-i-do-if-the-device-cannot-be-identified).

## E001300 Emulator Does Not Support the tmode Command

**Error Message**

Not support tmode for Emulator.

**Symptom**

The Emulator does not support the **hdc tmode** command.

**Possible Causes**

The Emulator in DevEco Studio does not support the **hdc tmode** command.

**Solution**

To use tmode-related commands, connect to a physical device.

## E002101 Failed to Terminate the Server

**Error Message**

Terminal hdc process failed, please terminal the hdc process in the task manager first.

**Symptom**

The server cannot be terminated.

**Possible Causes**

After the **.hdcserver.pid** file is deleted, the server cannot be terminated by the **hdc kill** command because the server PID cannot be obtained.

**Solution**

Terminate the hdc server in Task Manager.

## E002105 Command Not Supported

**Error Message**

Unsupport command.

**Symptom**

The command is not supported.

**Possible Causes**

The device version is too early to support debugging commands.

**Solution**

Upgrade the device version or check whether the command is correct by referring to [hdc Commands](#hdc-commands).

## E002106 Device Communication Exception

**Error Message**

Failed to communicate with daemon.

**Symptom**

The communication between the server and the daemon on the device is abnormal.

**Possible Causes**

1.  The USB is disconnected.
    
2.  The network is unstable over TCP.
    

**Solution**

1.  Verify that the device is properly connected.
    
2.  Check the network status. After the network becomes stable, try again.
    

## E003001 Invalid Bundle Name

**Error Message**

Invalid bundle name: bundlename.

**Symptom**

The **bundlename** specified in the **hdc shell \[-b bundlename\] \[command\]** command does not belong to an installed and started debug-type application, or the application directory does not exist.

**Possible Causes**

1.  Scenario 1: The specified application is not installed on the device.
    
2.  Scenario 2: The specified application is not a debug-type application.
    
3.  Scenario 3: The specified application is not started.
    

**Solution**

1.  Scenario 1: Ensure that the application specified in the command has been installed on the device.
    
    Run the **hdc shell "bm dump -a | grep bundlename"** command to check whether the application corresponding to the bundle name has been installed on the device. The expected result is **bundlename**.
    
    For example, if the bundle name is **com.example.myapplication**, run the following command:
    
    hdc shell "bm dump -a | grep com.example.myapplication"
    
    If the bundle has been installed on the device, the following information is returned:
    
    com.example.myapplication
    
2.  Scenario 2: Check whether the application specified by the command is a debug-type application.
    
    -   Run the **hdc shell "bm dump -n bundlename | grep appProvisionType"** command. The expected result is **"appProvisionType": "debug"**.
        
        For example, run the following command to check the bundle name **com.example.myapplication**:
        
        hdc shell "bm dump -n com.example.myapplication | grep appProvisionType"
        
        If the application is a debug-type application, the following information is displayed:
        
        "appProvisionType": "debug",
        
    -   To build a debug-type application, you need to sign the application using a debug certificate. For details, see [Requesting a Debug Certificate](https://developer.huawei.com/consumer/en/doc/app/agc-help-add-debugcert-0000001914263178).
        
3.  Scenario 3: Ensure that the bundle specified by the command has been started.
    
    -   After the application starts, the system mounts the corresponding resource directory. You can run the **hdc shell "mount |grep bundlename"** command to query the resource directory mounting status after the application starts.
        
        For example, to check the bundle name **com.example.myapplication**, run the following command:
        
        hdc shell "mount |grep com.example.myapplication"
        
        If the corresponding resource directory has been mounted, mounting information is expected to be returned. (The returned information varies according to the actual mounting status and is not displayed here.)
        
        If the corresponding resource directory is not mounted, no information is returned.
        
    -   If the corresponding resource directory is not mounted, you can click the application or run the **aa** command to start the application.
        
        For example, to start the application whose name is **com.example.myapplication** and module name is **EntryAbility**, run the following command:
        
        hdc shell aa start -b com.example.myapplication -a EntryAbility
        
        For details, see [aa Commands](../../../debugging-commands/ability-assistant/document.md).
        

## E003002 Command Parameter Does Not Support the Interactive Mode

**Error Message**

Unsupport interactive shell command option.

**Symptom**

The **hdc shell \[-b bundlename\] \[command\]** command does not support the interactive option.

**Possible Causes**

The **command** parameter specified by **hdc shell \[-b bundlename\] \[command\]** cannot be empty.

**Solution**

Ensure that the **command** parameter is not empty. For details, see [Running Interactive Commands](#running-interactive-commands).

## E003003 Interactive Command Parameters Not Supported

**Error Message**

Unsupport shell option: XXX.

**Symptom**

The **hdc shell \[-b bundlename\] \[command\]** command contains unsupported parameters, for example, **\-f** and **\-B**.

**Possible Causes**

The parameters are case insensitive, or unsupported parameters are used.

**Solution**

Use the command parameters supported by the current version, for example, the **\-b** parameter. For details, see [Running Interactive Commands](#running-interactive-commands).

## E003004 Parameter Not Supported by the Device

**Error Message**

Device does not support this shell option.

**Symptom**

The device does not support the **hdc shell \[-b bundlename\] \[command\]** command.

**Possible Causes**

The device version is too early to support new command parameters.

**Solution**

Upgrade the device OS to the latest version. For details, see [hdc Version Mappings](#hdc-version-mappings).

## E003005 Incorrect Command Parameters

**Error Message**

The parameter is missing, correct your input by referring below: Usage...

**Symptom**

The\*\* hdc shell xxx\*\* command is not supported on the device.

**Possible Causes**

The system version of the device is too early to support the new command parameters.

**Solution**

Upgrade the device OS to the latest version. For details, see [hdc Version Mappings](#hdc-version-mappings).

## E005003 Parameter Missing in File Transfer

**Error Message**

The parameter is missing, correct your input by referring below: Usage...

**Symptom**

1.  Mandatory parameters are missing in the **hdc file send \[-b bundlename\]\[SOURCE\]\[DEST\]** command.
    
2.  Mandatory parameters are missing in the **hdc file recv \[-b bundlename\]\[DEST\]\[SOURCE\]** command.
    

**Possible Causes**

When the **\-b** parameter is specified, the **bundlename**, **SOURCE**, and **DEST** parameters are missing. For details about the command, see [Transferring Files](#transferring-files).

**Solution**

Ensure that the **bundlename**, **SOURCE**, and **DEST** parameters are not empty.

## E005004 SDK or Device System Does Not Support the -b Parameter

**Error Message**

SDK/Device ROM doesn't support -b option.

**Symptom**

The **hdc file send/recv** command contains the **\-b** option, but the hdc in SDK or device system version does not support this option.

**Possible Causes**

1.  Scenario 1: When the **hdc file send \[-b bundlename\] \[SOURCE\] \[DEST\]** command is executed, the device system does not support the **\-b** option.
    
2.  Scenario 2: When the **hdc file recv \[-b bundlename\] \[DEST\] \[SOURCE\]** command is executed, the hdc in SDK does not support the **\-b** option.
    

**Solution**

1.  Scenario 1: Upgrade the system to the latest version. For details, see [hdc Version Mappings](#hdc-version-mappings).
    
2.  Scenario 2: Upgrade the SDK to the latest version. For details, see [hdc Version Mappings](#hdc-version-mappings).
    

## E005005 Failed to Create a Directory

**Error Message**

Error create directory: xxx, path: xxx.

**Symptom**

Failed to create a directory.

**Possible Causes**

When the **hdc file send** command is executed to send a file, the corresponding directory on the device is an unauthorized directory or a read-only system directory.

**Solution**

Change the target directory for sending files, and ensure that it has the write permission.

## E005101 Invalid Bundle Name During File Transfer

Same as the error code [E003001 Invalid Bundle Name](#e003001-invalid-bundle-name).

## E005102 Invalid Remote Path

**Error Message**

Remote path: xxx is invalid, no such file/directory or it's out of the application directory.

**Symptom**

1.  The path specified by **DEST** in the **hdc file send \[-b bundlename\]\[SOURCE\]\[DEST\]** command does not exist or exceeds the application data directory.
    
2.  The path specified by **DEST** in the **hdc file recv \[-b bundlename\]\[SOURCE\]\[DEST\]** command does not exist or exceeds the application data directory.
    

**Possible Causes**

1.  Scenario 1: The remote path does not exist.
    
2.  Scenario 2: The **DEST** parameter contains the **..** redirection symbol. After resolving the path traversal, the actual directory falls outside the application's data root directory.
    

**Solution**

Check whether the relative path of the application data directory specified by **DEST** exists.

## E006001 Invalid Installation Package Path

**Error Message**

Not any installation package was found.

**Symptom**

No installation package is found.

**Possible Causes**

The installation package parameter is missing when the **hdc install** command is executed.

**Solution**

For details, see [Managing Applications](#managing-applications).

## E007100 Unsupported Command

**Error Message**

Operate need running under debug mode.

**Symptom**

The command can be executed only in debug mode.

**Possible Causes**

The command is not supported.

**Solution**

No operation is required.

## E005008 Unsupported File Transfer Operation

**Error Message**

Operation not allowed.

**Symptom**

The command operation is not allowed.

**Possible Causes**

Operations on sensitive files (such as system configuration files and log files) are not allowed.

**Solution**

No operation is required.

## E001106 Incorrect IP Address Specified by -e

**Error Message**

\-e content IP incorrect.

**Symptom**

\-The IP address specified by **\-e** is incorrect.

**Possible Causes**

The IP address format is invalid.

**Solution**

Ensure that the entered IP address is valid and the IP address belongs to the local host.

## E00C001 hdc client/server Debugging Interception

**Error Message**

Operation restricted by the organization.

**Symptom**

The operation is blocked by the organization.

**Possible Causes**

The hdc client/server debugging functionality in the PC/2-in-1 device is disabled by the organization.

**Solution**

Contact the organization device administrator to query the hdc debugging policy configuration of the PC/2-in-1 device.
