# Using the Daemon Process

A daemon process is a program that runs in the background, other than one under the direct control of users. The Hvigor daemon process is a persistent background process that helps to reduce the build time.

#### Understanding the Daemon Process

The Hvigor client sends build information such as command line arguments, project directories, and environment variables to the daemon process to facilitate build execution. The communication between the client and daemon process is done through a local socket connection. A maximum of eight daemon processes can run concurrently. Within this limit, no more than six processes are allowed to be in the active state (that is, neither stopped nor interrupted).

#### Enabling or Disabling Usage of the Daemon Process

Usage of the daemon process is enabled in Hvigor by default. You can manage the settings using the following methods:

-   Using the menu bar of DevEco Studio
    -   Choose **File** > **Settings** (**DevEco Studio** > **Preferences**/**Settings** on macOS) > **Build, Execution, Deployment** > **Build Tools** > **Hvigor** and select or deselect **Enable the Daemon for tasks**.
-   Using commands
    -   Run the following command (replace **<task>** with the actual task name):
        
        // Enable usage of the daemon process.
        hvigorw <task> --daemon
        // Disable usage of the daemon process.
        hvigorw <task> --no-daemon
        
    -   Configure **execution.daemon** in [hvigor-config.json5](../../configuration-files/hvigor-config-json5-file/document.md).

#### Setting the Daemon Memory

The maximum old-generation memory allocated to the daemon process defaults to 8192 MB, which is sufficient for most builds. To customize the maximum old-generation memory allocated to the daemon process, use either of the following methods. You are advised to adjust the settings based on your available local memory. The settings configured through the CLI mode have a higher priority than those of the **hvigor-config.json5** file.

-   Modify the **nodeOptions.maxOldSpaceSize** settings in the [hvigor-config.json5](../../configuration-files/hvigor-config-json5-file/document.md) file.
-   Run the command to change the daemon memory. For example:
    
    hvigorw assembleHap --max-old-space-size=12345
    

The maximum semi-space size of the young-generation memory for the daemon process defaults to 16 MB. By modifying this value, you can control garbage collection frequency, which directly impacts performance and memory usage. You can use either of the following methods to modify the settings. The CLI method has a higher priority than the **hvigor-config.json5** file.

This feature is supported since DevEco Studio 5.1.0 Release.

-   Modify the **nodeOptions.maxSemiSpaceSize** settings in the [hvigor-config.json5](../../configuration-files/hvigor-config-json5-file/document.md) file.
-   Run the command to change the daemon memory. For example:
    
    hvigorw assembleHap --max-semi-space-size=32
    

#### Checking the Status of the Daemon Process

To get a list of running daemon processes and their status, you can use the following command:

hvigorw --status-daemon

\> hvigor PID    STATUS  PORT    ROOT\_PATH
> hvigor 11072  idle    45001   D:\\Demo1
> hvigor 18836  stopped 45000   D:\\Demo2

| 
Status

 | 

Description

 |
| :-- | :-- |
| 

idle

 | 

Idle

 |
| 

half\_busy

 | 

Half busy

 |
| 

busy

 | 

Busy

 |
| 

canceled

 | 

Canceled

 |
| 

stopReq

 | 

Stopped as requested.

 |
| 

stopped

 | 

Stopped

 |
| 

broken

 | 

Interrupted

 |

#### Stopping a Daemon Process

It is necessary to restart a daemon process when changing the memory settings or debugging faults.

You can use the following command to stop a daemon process:

hvigorw --stop-daemon

If you want to stop all daemon processes, run the following command:

hvigorw --stop-daemon-all

#### Performance Impact

The daemon process can significantly reduce the time for repeated builds of the same project. For multiple builds, the daemon process loads Hvigor into the memory only once, instead of for every build.
