# Loading Modules Using Node-API

Node-API provides multiple methods for you to load in-project modules and files on the C++ side. The **napi\_load\_module\_with\_info** API is recommended.

#### napi\_load\_module\_with\_info

Loads the HAP, HSP, HAR, or native module in the main thread or child thread. When using this API, you must specify the information of the package to be loaded. It supports various scenarios.

For details, see [napi\_load\_module\_with\_info](../../../../../ndk-development/code-development/using-node-api/typical-node-api-use-cases/loading-a-module-using-node-api/document.md).

#### napi\_load\_module

Loads the HAP, HSP, HAR, or native module in the main thread, facilitating parameter transfer. The loading scenario is restricted. For example, this API cannot be used in a child thread.

For details, see [napi\_load\_module](../../../../../ndk-development/code-development/using-node-api/typical-node-api-use-cases/loading-a-module-in-the-main-thread-using-node-api/document.md).
