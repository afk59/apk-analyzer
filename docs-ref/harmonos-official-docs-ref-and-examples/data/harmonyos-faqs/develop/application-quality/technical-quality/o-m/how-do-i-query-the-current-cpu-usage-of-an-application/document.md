# How do I query the current CPU usage of an application?

You can query the current CPU usage using either of the following methods:

In the code:

Use the **hidebug.getCpuUsage** API. The code snippet is as follows:

let cpuUsage: number = hidebug.getCpuUsage();

In the CLI:

-   Complete [Environment Setup](https://developer.huawei.com/consumer/en/doc/harmonyos-guides-V14/hdc-V14#environment-setup) for HarmonyOS Device Connector (hdc).
-   Connect the devices properly.
    
    hidumper --cpuusage <pid>
    hidumper --cpuusage
    

**Reference**

[hidebug.getCpuUsage](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-hidebug#hidebuggetcpuusage9)

[hidumper](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/hidumper)
