# How do I query the PID of an application process?

You can obtain the information in either of the following ways:

-   Method 1: Run shell commands.
    
    To view information about all running processes, run the **hdc shell** command to enter the CLI of the device, and then run the **ps -ef** command.
    
-   Method 2: Call the [process](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-process) related API.
    
    import { process } from '@kit.ArkTS';
    
    let pid = process.pid;
