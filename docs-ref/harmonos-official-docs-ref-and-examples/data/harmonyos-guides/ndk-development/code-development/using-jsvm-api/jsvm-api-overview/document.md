# JSVM-API Overview

#### Introduction

HarmonyOS JSVM-API provides a set of stable APIs based on the standard JavaScript (JS) engine. It supports key functionalities such as creating and destroying engines, executing JS code, and implementing interaction between JS and C/C++ modules.

HarmonyOS JSVM-API provides a set of APIs written in C programming language that complies with C99.

HarmonyOS JSVM-API is not thread-safe. You need to ensure the thread safety of JSVM-API.

JSVM-API allows dynamically loaded JS code to be directly run during application runtime. With JSVM-API, you can also use C/C++ to implement core functionalities that demand high performance or closely rely on underlying system invocation, register C++ methods in JS code, and directly call the JS code to improve the execution speed.

Unless otherwise specified, JSVM-API in this document refers to HarmonyOS JSVM-API.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/74/v3/Iuxp77HhRDqDNj9-Gmo14g/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062132Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=31D5D8AA84ECFDADA028319C0E608BA53866A017F081B10028BF7C482B076417)

JSVM-API supports only the interaction between JS and C/C++. If you need to implement the interaction between ArkTS and C/C++, see [Node-API Overview](../../using-node-api/node-api-overview/document.md).

#### JSVM-API Architecture

**Figure 1** JSVM-API architecture

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ba/v3/Gfb5DwMITGOYhjCmv6NG0g/en-us_image_0000002537765296.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062132Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=9E8261CB98F8E190F17EB94B28F0F2362BD455EE55D49860FFAC3E1CA701C862)

-   Native Module: module developed using JSVM-API in C/C++.
    
-   VM Life Cycle Manager: manages the JSVM\_VM lifecycle.
    
-   JS Context Manager: manages the JSVM\_Env lifecycle.
    
-   Context Snapshot: manages context snapshots to shorten the time used to create JS context.
    
-   JS Code Execute: executes JS code.
    
-   JS/C++ Interaction: implements interaction between JS and C++.
    
-   Code Cache: caches the JS code to shorten the startup time for JS code execution.
    
-   Debugger: debugs JS code.
    
-   CPU Profiler: records the JS code execution time and helps analyze the JS code performance bottlenecks.
    
-   Heap Snapshot: helps you perform JS heap memory analysis, identify memory issues, and make improvements.
    
-   Heap Statistics: provides JS heap statistics, including the memory size and context count.
    
-   Memory Adjustment: adjusts the external memory size and VM memory pressure to accelerate GC triggering.
    
-   VM Information: manages JSVM\_VM information.
    
-   Standard JS Engine: standard JS engine.
    

#### JSVM-API Interaction Process

**Figure 2** Key interaction process of JSVM-API

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f1/v3/c_PPDyuxTyeb-MtJov047Q/en-us_image_0000002537925236.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062132Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=3A3D52B9349A24380EA13061CBC142DFF694B540F7C9C33D2D6830062999AF53)

The interaction between JSVM-API and a native module is as follows:

1.  **Initialization**: Initialize the JSVM and JS context on the native module and register native functions in JS code. The native functions are hooked to **GlobalThis**, which is the global context of the JS execution environment.
    
2.  **Invocation**: Call JS APIs to invoke the native functions that are registered in **GlobalThis** using JSVM-API. The JS engine calls the corresponding C/C++ functions.
