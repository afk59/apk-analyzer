# Overview

Performance Analysis Kit provides comprehensive capabilities such as fault detection and exception handling. As faults vary in causes and symptoms, application stability deteriorates, affecting application development efficiency, delivery costs, and user experience. Therefore, you need to improve quality by designing a fault management system, which includes the detection, analysis, locating and rectification of faults, and quality measurement.

To help you quickly locate and rectify application faults, this topic describes the detection principles, log specifications, log obtaining methods, and restrictions of faults such as process crash, address out-of-bounds, application freeze, resource leak, task execution timeout, and application termination.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8c/v3/9K8PPk5pTcK1h90vGtWofA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062026Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=A448A69828D99394E1B0A10ABCD08E692801968400B3A6C46940C46C157A427E)

The following faults cause unexpected application or system process exit:

1.  Native code does not process crash exception signals, and C++ crash logs are generated. For details, see [Cpp Crash (Process Crash) Detection](../crash-detection/c-crash-process-crash-detection/document.md).
    
2.  JS/ArkTS code does not process exceptions, and JS crash logs are generated. For details, see [JS Crash (Process Crash) Detection](../crash-detection/js-crash-process-crash-detection/document.md).
    
3.  The application is freezing and AppFreeze logs are generated. For details, see [Application Freeze Detection](../application-freeze-detection/document.md).
    
4.  The application process is terminated by the system, and the application exits unexpectedly. For details, see [Application Killed Detection](../application-killed-detection/document.md).
