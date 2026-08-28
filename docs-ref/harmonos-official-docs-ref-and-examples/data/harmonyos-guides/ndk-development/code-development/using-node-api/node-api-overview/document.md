# Node-API Overview

#### When to Use

Developed based on the Node.js 18.x LTS [Node-API](https://nodejs.org/docs/latest-v12.x/api/n-api.html), HarmonyOS Node-API allows interaction between ArkTS/JS and C/C++ modules. It provides a set of stable APIs that can be used on different operating systems.

Unless otherwise specified, Node-API in this document refers to HarmonyOS Node-API.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0d/v3/PdBBHT_4TlKudG9a9LA_7Q/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062130Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=C74EAD3BBAB5FD41F562049D8A5D4276E319E30F33D7043F6B34092E70A0F0C2)

For details about the differences between HarmonyOS Node-API and Node.js 18.x LTS Node-API, see [Node-API](https://developer.huawei.com/consumer/en/doc/harmonyos-references/napi).

Generally, ArkTS/JS is used for HarmonyOS application development. However, in compute-intensive scenarios, such as games and physical simulations, the existing C/C++ libraries are required to meet the requirements for performance and efficiency. Node-API encapsulates I/O, CPU-intensive, and OS underlying capabilities and exposes these capabilities in the form of C APIs. It uses the C/C++ module registration mechanism to mount properties and methods to ArkTS/JS objects to implement interaction between ArkTS/JS and C/C++. Node-API provides the following benefits:

-   The system can open rich module functionalities of the framework layer to ArkTS/JS through the module registration mechanism of Node-API, and open the C/C++ capabilities to the ArkTS/JS layer of applications.
    
-   You can encapsulate core capabilities in C/C++ and use them with ArkTS/JS APIs to improve the execution efficiency of your application.
    

#### Node-API Architecture

**Figure 1** Node-API architecture

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ce/v3/wRaFrpWpS_OujfqbthLA8g/en-us_image_0000002568685007.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062130Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=F3706F728D168836B547DA090F24A1156918085EE03B8F6BB15CA8E2CB73E1DE)

-   Native module: a module developed using Node-API and imported to ArkTS.
    
-   Node-API: implements the logic for interaction between ArkTS and C/C++ code.
    
-   ModuleManager: manages native modules, including loading and locating native modules.
    
-   ScopeManager: manages the lifecycle of **napi\_value**.
    
-   ReferenceManager: manages the lifecycle of **napi\_ref**.
    
-   Native engine: ArkTS engine abstraction layer, which unifies the API behavior of the ArkTS engine at the Node-API layer.
    
-   ArkCompiler ArkTS Runtime: ArkTS runtime.
    

#### Key Interaction Process of Node-API

**Figure 2** Key interaction process of Node-API

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f/v3/tk-N_6VaQqCUShfv2D_eag/en-us_image_0000002568765017.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062130Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=B9049B7F3546C192CA8E69A2DEDBA461861F4B89DC82F8D1FCD268A76A0939F7)

The interaction between ArkTS and C++ consists of the following two steps:

1.  Initialization: When a native module is imported to ArkTS, the ArkTS engine calls the ModuleManager to load the .so file and dependencies of the module. When the module is loaded for the first time, the module registration is triggered. Then, the method properties defined by the module are embedded to an **exports** object and the object is returned.
    
2.  Invocation: When an ArkTS method is called using the **exports** object, the ArkTS engine locates and calls the embedded C/C++ method.
