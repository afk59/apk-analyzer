# Why cannot **napi\_env** be cached?

**napi\_env** indicates the running status and context information of an application. The value of **napi\_env** may change in different call contexts, execution environments, during Node-API module initialization or destruction, and in multi-threaded environments. **napi\_env** should be safely accessed and manipulated through the APIs provided by Node-API.

The reasons for prohibiting caching of **napi\_env** are as follows:

1.  Maintain context consistency: If **napi\_env** is cached, the cached data may become inconsistent with that in the latest environment. For example, if certain variables in the environment are modified during an API call but the cached data is not updated, unexpected result may be returned, leading to logical errors or exceptions in the application.
2.  Avoid cross-thread use: **napi\_env** cannot be shared or passed between different threads. If it is cached and used in different threads, thread safety issues may occur. However, **napi\_env** can be cached if it is used only in the main thread.
3.  Improve application reliability and stability: Prohibiting the caching of **napi\_env** ensures that the latest and valid context environment is used each time a Node-API function is called, avoiding potential errors and exceptions.
