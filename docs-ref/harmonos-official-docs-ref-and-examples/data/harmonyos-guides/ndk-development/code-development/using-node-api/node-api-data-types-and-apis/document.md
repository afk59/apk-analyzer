# Node-API Data Types and APIs

#### Data Types

## napi\_status

Defines an enum for the execution statuses of a Node-API call.

Each time a Node-API function is called, a value of **napi\_status** is returned indicating the execution result.

typedef enum {
    napi\_ok,
    napi\_invalid\_arg,
    napi\_object\_expected,
    napi\_string\_expected,
    napi\_name\_expected,
    napi\_function\_expected,
    napi\_number\_expected,
    napi\_boolean\_expected,
    napi\_array\_expected,
    napi\_generic\_failure,
    napi\_pending\_exception,
    napi\_cancelled,
    napi\_escape\_called\_twice,
    napi\_handle\_scope\_mismatch,
    napi\_callback\_scope\_mismatch,
    napi\_queue\_full,
    napi\_closing,
    napi\_bigint\_expected,
    napi\_date\_expected,
    napi\_arraybuffer\_expected,
    napi\_detachable\_arraybuffer\_expected,
    napi\_would\_deadlock, /\* unused \*/
    napi\_no\_external\_buffers\_allowed,
    napi\_cannot\_run\_js
} napi\_status;

## napi\_extended\_error\_info

Defines a struct that represents detailed error information when a Node-API call fails.

typedef struct {
    const char \*error\_message;
    void \*engine\_reserved;
    uint32\_t engine\_error\_code;
    napi\_status error\_code;
} napi\_extended\_error\_info;

## napi\_value

A C struct pointer acting as a reference to an ArkTS or JS object. A **napi\_value** holds a ArkTS/JS object. [napi\_handle\_scope](#memory-management-types) is used to manage the lifetime of **napi\_value** handles. The JS object held by a **napi\_value** in the scope will not be released. If the **napi\_value** is out of the scope, it becomes invalid and will no longer hold the ArkTS/JS object.

## napi\_env

-   Context used by the underlying Node-API implementation. It is passed to the native functions when they are invoked, and must be passed back when Node-API calls are made.
    
-   **napi\_env** is bound to the context of the ArkTS/JS thread. Each **napi\_env** has an independent runtime context. After an ArkTS/JS thread exits, the corresponding **napi\_env** becomes invalid.
    
-   **napi\_env** cannot be cached, nor can it be passed between threads.
    

## napi\_threadsafe\_function

[Pointer](../typical-node-api-use-cases/thread-safety-development-using-node-api/document.md) that represents an ArkTS/JS function that can be called asynchronously from multiple threads. It can be used to pass the asynchronous (async for short) operation result to the ArkTS/JS environment, such as reading data from another thread or performing compute-intensive operations. The thread-safe function callback is executed only in the ArkTS thread that creates the thread-safe function. By using **napi\_threadsafe\_function**, you can implement efficient interaction between ArkTS/JS and C++ code while maintaining thread safety.

## napi\_threadsafe\_function\_release\_mode

Defines an enum for two constants that specify how thread-safe functions are released.

typedef enum {
  napi\_tsfn\_release,
  napi\_tsfn\_abort
} napi\_threadsafe\_function\_release\_mode;

Its value is passed to **napi\_release\_threadsafe\_function**.

napi\_release\_threadsafe\_function(napi\_threadsafe\_function func,
                                 napi\_threadsafe\_function\_release\_mode mode);

-   If the **mode** value is **napi\_tsfn\_release**, the number of threads held by the thread-safe function is reduced by one. When the number of threads is reduced to 0, the thread-safe function is destroyed.
    
-   If the value is **napi\_tsfn\_abort**, this thread-safe function is disabled and cannot be called.
    
    If **napi\_tsfn\_abort** is set, calling this thread-safe function using **napi\_call\_threadsafe\_function** may cause a UAF issue. When **napi\_tsfn\_abort** is set, the thread-safe function is disabled and cannot be called. If **napi\_call\_threadsafe\_function** is called, the system may return **napi\_closing**, indicating that the thread-safe function is being disabled, and the data passed to the thread-safe function is not put into the queue. This means that the data may not be correctly processed. If the memory to which data points has been freed (for example, the thread-safe function resources have been freed), but the caller still tries to access or use data, a Use-After-Free (UAF) issue may occur.
    

## napi\_threadsafe\_function\_call\_mode

Defines an enum for whether the call should be blocked when the queue associated with the thread-safe function is full.

The data struct is as follows:

typedef enum {
  napi\_tsfn\_nonblocking,
  napi\_tsfn\_blocking
} napi\_threadsafe\_function\_call\_mode;

-   **napi\_tsfn\_nonblocking**: Leave **napi\_call\_threadsafe\_function** unblocked. If the queue is full, **napi\_queue\_full** is returned to prevent data from being added to the queue.
    
-   **napi\_tsfn\_blocking**: Block **napi\_call\_threadsafe\_function** until there is available space in the queue.
    

## Memory Management Types

Node-API provides the following memory management types:

**napi\_handle\_scope**

Data used to manage the lifecycle of ArkTS/JS objects. It allows ArkTS/JS objects to remain active within a certain range for use in ArkTS/JS code. When **napi\_handle\_scope** is created, all ArkTS/JS objects created in this range remain active until the end. This minimizes their lifecycles and [prevents memory leaks](../node-api-development-specifications/document.md#lifecycle-management). For details about **napi\_handle\_scope**, see Precautions for Lifecycle Management.

**napi\_escapable\_handle\_scope**

-   It is created by **napi\_open\_escapable\_handle\_scope** and closed by **napi\_close\_escapable\_handle\_scope**.
    
-   It is a special type of handle range used to return values created within the scope of **escapable\_handle\_scope** to a parent scope.
    
-   It is used by **napi\_escape\_handle** to escape ArkTS/JS objects to a parent scope so that the objects are valid for the lifetime of the outer scope.
    

**napi\_ref**

Reference to **napi\_value**, which allows you to manage the lifecycle of ArkTS/JS values.

**napi\_type\_tag**

Defines a struct that contains two unsigned 64-bit integers to identify the type of a Node-API value.

typedef struct {
  uint64\_t lower;
  uint64\_t upper;
} napi\_type\_tag;

-   It is a 128-bit value stored as two unsigned 64-bit integers. It is used to tag ArkTS/JS objects to ensure that they are of a certain type.
    
-   This is a stronger check than **napi\_instanceof** because **napi\_instanceof** may report a false positive if the object's prototype is manipulated.
    
-   The combination of **type\_tag** and **napi\_wrap** is useful because it ensures that the pointer retrieved from a wrapped object can be safely converted to the native type corresponding to the type tag that had been previously applied to the JS object.
    

**napi\_async\_cleanup\_hook\_handle**

A mechanism used in Node-API to manage the lifecycle of asynchronous resources. It allows you to register a cleanup hook, which is called only when the lifecycle of the current **napi\_env** ends. It ensures that some asynchronous resources are properly released before the environment is destroyed, thereby avoiding resource leaks. In addition, in the Node-API implementation, if the structure is not released, the destruction of the entire **napi\_env** is delayed. In HarmonyOS, the behavior of this API is almost the same as that of the cleanup hook related to the env lifecycle, except that it allows the same context data to be repeatedly registered.

**napi\_critical\_scope (Extended Capability)**

A mechanism used in Node-API to create the execution environment of critical APIs. It is created by **napi\_open\_critical\_scope** and closed by **napi\_close\_critical\_scope**.

Critical API: An API that needs to be executed within the critical scope. Specifically, the API name contains the keyword **critical**.

**napi\_strong\_ref (Extended Capability)**

Reference to **napi\_value**, which allows you to manage the lifecycle of ArkTS objects.

Note: Compared with **napi\_ref**, **napi\_strong\_ref** is more efficient in creation but supports limited functionalities (for example, strong and weak reference conversion is not supported).

**napi\_sendable\_ref (Extended Capability)**

Reference to **napi\_value**, which allows the caller to manage the lifecycle of the Sendable ArkTS object. **napi\_sendable\_ref** can be operated across ArkTS threads.

Note: Unlike **napi\_ref**, **napi\_sendable\_ref** supports operations across ArkTS threads. (For example, you can create **napi\_sendable\_ref** in thread A, obtain **napi\_value** using **napi\_sendable\_ref** in thread B, and delete **napi\_sendable\_ref** in thread C. You must ensure the correct call sequence.) However, the referenced **napi\_value** must be Sendable, and strong and weak reference conversion is not supported.

## Callback Types

Node-API provides the following callback types:

**napi\_callback\_info**

Data type passed to **napi\_get\_cb\_info** to obtain JS input parameters.

**napi\_callback**

User-defined native function exposed to ArkTS/JS. Specifically, no handle or callback scope is created in this callback.

The basic usage is as follows:

typedef napi\_value (\*napi\_callback)(napi\_env, napi\_callback\_info);

**napi\_finalize**

Function pointer passed to **napi\_create\_threadsafe\_function**, **napi\_set\_instance\_data**, **napi\_wrap** and **napi\_add\_finalizer**. **napi\_finalize** is called when an object is reclaimed.

**napi\_async\_execute\_callback**

Function pointer used in **napi\_create\_async\_work**.

-   An async native function is called from a worker pool thread and can be executed in parallel with the event loop thread.
    
-   Avoid calling non-thread-safe Node-APIs when implementing this callback.
    
-   Node-API calls should be executed in **napi\_async\_complete\_callback**.
    

**napi\_async\_complete\_callback**

Function pointer used when an async operation is complete. When an async operation is required, you can use **napi\_create\_async\_work** to create an async work and specify **napi\_async\_complete\_callback**. When the async work is complete, the callback will be automatically invoked for subsequent processing. Parameters of the callback include the status of the async operation and a return value, based on which corresponding processing can be performed.

**napi\_threadsafe\_function\_call\_js**

Function pointer used in the event loop thread to interact with ArkTS/JS to implement more complex scenarios. It is used in **napi\_create\_threadsafe\_function(napi\_env env,…,napi\_threadsafe\_function\_call\_js call\_js\_cb,...)**.

**napi\_cleanup\_hook**

Function pointer used with **napi\_add\_env\_cleanup\_hook**. It will be called when the environment is destroyed.

**napi\_async\_cleanup\_hook**

Function pointer used with **napi\_add\_async\_cleanup\_hook**. It will be called when the environment is destroyed.

## QoS

Defines an enum for the thread scheduling priority.

typedef enum {
    napi\_qos\_background = 0,
    napi\_qos\_utility = 1,
    napi\_qos\_default = 2,
    napi\_qos\_user\_initiated = 3,
} napi\_qos\_t;

| QoS | Use Scenario |
| :-- | :-- |
| napi\_qos\_background | Low priority for works invisible to users, such as data synchronization and backup. |
| napi\_qos\_utility | Medium priority for works that do not require immediate response, such as downloading or importing data. |
| napi\_qos\_default | Default priority. |
| napi\_qos\_user\_initiated | High priority for user-triggered works with visible progress, for example, opening a file. |

## Event Loop Modes

Node-API provides two modes for running the underlying event loop. The two modes are defined as follows:

typedef enum {
    napi\_event\_mode\_default = 0,
    napi\_event\_mode\_nowait = 1,
} napi\_event\_mode;

| Event Loop Mode | Description |
| :-- | :-- |
| napi\_event\_mode\_default | Run the underlying event loop while blocking the current thread, and exit the event loop only when there is no active **uv\_handle** in the loop. |
| napi\_event\_mode\_nowait | Run the underlying event loop without blocking the current thread. Process a task and exit the event loop after the task is complete. If there is no task in the event loop, exit the event loop immediately. |

## Thread-safe Task Priority

Node-API defines the priorities of thread-safe tasks, as listed below. The tasks in the underlying task queue are executed in sequence based on their priorities.

typedef enum {
    napi\_priority\_immediate = 0,
    napi\_priority\_high = 1,
    napi\_priority\_low = 2,
    napi\_priority\_idle = 3,
} napi\_task\_priority;

| Task Priority | Description |
| :-- | :-- |
| napi\_priority\_immediate | Highest priority. |
| napi\_priority\_high | Priority lower than **napi\_priority\_immediate**. |
| napi\_priority\_low | Priority lower than **napi\_priority\_high**. |
| napi\_priority\_idle | Lowest priority. |

#### APIs

Node-API is extended based on the native modules provided by Node.js. The following lists the APIs supported currently.

## Async Thread-Safe APIs

| API | Description |
| :-- | :-- |
| napi\_create\_threadsafe\_function | Creates a thread-safe function. |
| napi\_get\_threadsafe\_function\_context | Obtains the context of a thread-safe function. |
| napi\_call\_threadsafe\_function | Calls a thread-safe function. |
| napi\_acquire\_threadsafe\_function | Acquires a thread-safe function. |
| napi\_release\_threadsafe\_function | Releases a thread-safe function. |
| napi\_ref\_threadsafe\_function | Indicates that the event loop running on the main thread should not exit until the thread-safe function is destroyed. |
| napi\_unref\_threadsafe\_function | Indicates that the event loop running on the main thread may exit before the thread-safe function is destroyed. |

## Buffer

| API | Description |
| :-- | :-- |
| napi\_create\_buffer | Creates an ArkTS Buffer instance of the specified size. |
| napi\_create\_buffer\_copy | Creates an ArkTS Buffer instance of the specified size, and initializes it with data copied from the passed-in buffer. |
| napi\_create\_external\_buffer | Creates an ArkTS Buffer instance of the specified size, and uses the specified data as its underlying buffer. You can use this API to add extra data to the buffer. |
| napi\_get\_buffer\_info | Obtains the underlying data of a JS **Buffer** and its length. |
| napi\_is\_buffer | Checks whether the given JS value is a **Buffer** object. |
| napi\_create\_external\_arraybuffer | Creates a JS **ArrayBuffer** with external data. |

## String

| API | Description |
| :-- | :-- |
| napi\_create\_string\_utf16 | Creates an ArkTS string from a UTF16-encoded C string. |
| napi\_get\_value\_string\_utf16 | Obtains the UTF16-encoded string corresponding to the given ArkTS value. |
| napi\_create\_string\_latin1 | Creates an ArkTS string from an ISO-8859-1-encoded C string. |
| napi\_create\_string\_utf8 | Creates an ArkTS string from a UTF8-encoded C string. |
| napi\_get\_value\_string\_latin1 | Obtains the ISO-8859-1-encoded string corresponding to the given ArkTS value. |
| napi\_get\_value\_string\_utf8 | Obtains the UTF8-encoded string corresponding to the given ArkTS value. |
| napi\_create\_external\_string\_utf16 | Creates an ArkTS string from a UTF-16-encoded string buffer, without performing memory copy operations. |
| napi\_create\_external\_string\_ascii | Creates an ArkTS string from an ASCII-encoded string buffer, without performing memory copy operations. |

## Date

| API | Description |
| :-- | :-- |
| napi\_create\_date | Creates an ArkTS Date object from C double data. |
| napi\_get\_date\_value | Obtains the C double equivalent of the given ArkTS Date object. |
| napi\_is\_date | Checks whether an ArkTS value is an ArkTS Date object. |

## ArrayBuffer

| API | Description |
| :-- | :-- |
| napi\_get\_arraybuffer\_info | Obtains the underlying buffer of an ArrayBuffer and its length. |
| napi\_is\_arraybuffer | Checks whether the given ArkTS value is an ArrayBuffer object. |
| napi\_detach\_arraybuffer | Detaches the underlying data of the given **ArrayBuffer**. |
| napi\_is\_detached\_arraybuffer | Checks whether the given **ArrayBuffer** has been detached. |
| napi\_create\_arraybuffer | Creates a JS **ArrayBuffer** object of the specified size. |

## Module

| API | Description |
| :-- | :-- |
| napi\_module\_register | Registers a native module. |

## Lifecycle Management

| API | Description |
| :-- | :-- |
| napi\_open\_handle\_scope | Creates a **napi\_handle\_scope**. You can use **napi\_close\_handle\_scope** to close it. |
| napi\_close\_handle\_scope | Closes a **napi\_handle\_scope**. After it is closed, all **napi\_value**s generated in it are closed. |
| napi\_open\_escapable\_handle\_scope | Opens an escapable handle scope, from which the declared values can be returned to the parent scope. You can use **napi\_close\_escapable\_handle\_scope** to close it. |
| napi\_close\_escapable\_handle\_scope | Closes the escapable handle scope passed in. |
| napi\_escape\_handle | Promotes the handle to the JS object so that it is valid for the lifetime of the parent scope. |
| napi\_create\_reference | Creates a **napi\_ref** for an object. The caller needs to manage the **napi\_ref** lifespan. |
| napi\_delete\_reference | Deletes a **napi\_ref**. |
| napi\_reference\_ref | Increments the **napi\_ref** count passed in and returns the new count. |
| napi\_reference\_unref | Decrements the **napi\_ref** count passed in and returns the new count. |
| napi\_get\_reference\_value | Obtains the JS object associated with **napi\_ref**. |
| napi\_add\_finalizer | Adds a **napi\_finalize** callback, which will be called when the ArkTS object is garbage-collected. |

## Promise

| API | Description |
| :-- | :-- |
| napi\_create\_promise | Creates a **Promise** object. |
| napi\_resolve\_deferred | Resolves a promise by using the **deferred** object associated with it. |
| napi\_reject\_deferred | Rejects a promise by using the **deferred** object associated with it. |
| napi\_is\_promise | Checks whether the given **napi\_value** is a **Promise** object. |

## Array

| API | Description |
| :-- | :-- |
| napi\_create\_array | Creates an ArkTS array. |
| napi\_create\_array\_with\_length | Creates an ArkTS array of the specified length. |
| napi\_get\_array\_length | Obtains the length of an array. |
| napi\_is\_array | Checks whether the given ArkTS value is an array. |
| napi\_set\_element | Sets the element value at the specified index of a given object. |
| napi\_get\_element | Obtains the element at the specified index of the given **Object**. |
| napi\_has\_element | Checks whether the given object has an element at the specified index. |
| napi\_delete\_element | Deletes the element at the specified index of the given **Object**. |
| napi\_create\_typedarray | Creates an ArkTS TypedArray from an existing ArrayBuffer. |
| napi\_is\_typedarray | Checks whether an ArkTS value is a TypeArray object. |
| napi\_get\_typedarray\_info | Obtains the properties of a TypedArray, such as the type, length, byte offset, and ArrayBuffer. |
| napi\_create\_dataview | Creates an ArkTS **DataView** from an existing ArrayBuffer. |
| napi\_is\_dataview | Checks whether an ArkTS value is a **DataView** object. |
| napi\_get\_dataview\_info | Obtains the properties of a **DataView**. |

## Primitives

| API | Description |
| :-- | :-- |
| napi\_get\_boolean | Obtains a JS Boolean object based on the given C Boolean value. |
| napi\_get\_global | Obtains the **global** object. |
| napi\_get\_null | Obtains the **null** object. |
| napi\_get\_undefined | Obtains the **undefined** object. |
| napi\_coerce\_to\_bool | Forcibly converts a JS value into a JS Boolean value. |
| napi\_coerce\_to\_number | Forcibly converts a JS value into a JS number. |
| napi\_coerce\_to\_object | Forcibly converts a JS value into a JS object. |
| napi\_coerce\_to\_string | Forcibly converts a JS value into a JS string. |

## Class

| API | Description |
| :-- | :-- |
| napi\_new\_instance | Creates an instance based on the given constructor. |
| napi\_get\_new\_target | Obtains the **new.target** of the constructor call. |
| napi\_define\_class | Defines a JS class corresponding to the C++ class. |
| napi\_wrap | Wraps a native object into an ArkTS object. This API allows the native methods and properties to be called from ArkTS. |
| napi\_unwrap | Unwraps the native object from an ArkTS object. |
| napi\_remove\_wrap | Removes the wrapping after the native object is unwrapped from an ArkTS object. |

## Object

| API | Description |
| :-- | :-- |
| napi\_get\_prototype | Obtains the prototype of an ArkTS object. |
| napi\_create\_object | Creates a default ArkTS object. |
| napi\_object\_freeze | Freezes an object. |
| napi\_object\_seal | Seals an object. |
| napi\_typeof | Obtains the type of an ArkTS value. |
| napi\_instanceof | Checks whether the given object is an instance of the specified constructor. |
| napi\_type\_tag\_object | Associates the value of the tag pointer with a JS object. |
| napi\_check\_object\_type\_tag | Checks whether a tag pointer is associated with an ArkTS object. |
| napi\_create\_symbol | Creates an ArkTS **Symbol** object. |
| napi\_create\_external | Creates an ArkTS external object, which can be used to pass custom data structs or objects in C/C++ to JS so that it can be accessible from ArkTS. |
| napi\_get\_value\_external | Obtains the ArkTS data from the external object created by **napi\_create\_external**. This API can be used to pass data between ArkTS and C/C++. |

## Basic Data Types

| API | Description |
| :-- | :-- |
| napi\_create\_int32 | Creates a JS number from a C int32 value. |
| napi\_create\_uint32 | Creates a JS number from a C uint32 value. |
| napi\_create\_int64 | Creates a JS number from a C int64 value. |
| napi\_create\_double | Creates a JS number from a C double value. |
| napi\_get\_value\_int32 | Obtains the C int32 equivalent of a JS number. |
| napi\_get\_value\_uint32 | Obtains the C uint32 equivalent of a JS number. |
| napi\_get\_value\_int64 | Obtains the C int64 equivalent of a JS number. |
| napi\_get\_value\_double | Obtains the C double equivalent of a JS number. |
| napi\_get\_value\_bool | Obtains the C bool equivalent of a JS Boolean value. |

## BigInt

| API | Description |
| :-- | :-- |
| napi\_create\_bigint\_int64 | Creates a JS BigInt from C int64 data. |
| napi\_create\_bigint\_uint64 | Creates a JS BigInt from C uint64 data. |
| napi\_create\_bigint\_words | Creates a single JS BigInt from a C uint64 array. |
| napi\_get\_value\_bigint\_int64 | Obtains the C int64 equivalent of a JS BigInt. |
| napi\_get\_value\_bigint\_uint64 | Obtains the C uint64 equivalent of a JS BigInt. |
| napi\_get\_value\_bigint\_words | Obtains information from a JS BigInt, including the sign bit, 64-bit little-endian array, and number of elements in the array. |

## Exceptions and Errors

| API | Description |
| :-- | :-- |
| napi\_throw | Throws a JS value. |
| napi\_throw\_error | Throws an ArkTS **Error** object with text information. |
| napi\_throw\_type\_error | Throws an ArkTS type error with text information. |
| napi\_throw\_range\_error | Throws an ArkTS range error with text information. |
| napi\_is\_error | Checks whether **napi\_value** indicates an error object. |
| napi\_create\_error | Creates an ArkTS error object with text information. |
| napi\_create\_type\_error | Creates an ArkTS error object with text information. |
| napi\_create\_range\_error | Creates an ArkTS error object with text information. |
| napi\_get\_and\_clear\_last\_exception | Obtains and clears the latest exception. |
| napi\_is\_exception\_pending | Checks whether an exception occurs. |
| napi\_fatal\_error | Raises a fatal error to terminate the process immediately. |
| napi\_get\_last\_error\_info | Obtains the **napi\_extended\_error\_info** struct, which contains the latest error information. |
| napi\_fatal\_exception | Throws a fatal exception, terminates the process, and generates a crash log. |

## Property

| API | Description |
| :-- | :-- |
| napi\_get\_property\_names | Obtains the names of the enumerable properties of an object in an array of strings. |
| napi\_set\_property | Sets a property for an object. |
| napi\_get\_property | Obtains the requested property of an object. |
| napi\_has\_property | Checks whether an object has the specified property. |
| napi\_delete\_property | Deletes a property from an object. |
| napi\_has\_own\_property | Checks whether an object has the own property specified by **key**. |
| napi\_set\_named\_property | Sets a property with the specified name for an object. |
| napi\_get\_named\_property | Obtains the property with the specified name in an object. |
| napi\_has\_named\_property | Checks whether an object has the property with the specified name. |
| napi\_define\_properties | Defines multiple properties for an object. |
| napi\_get\_all\_property\_names | Obtains an array containing the names of all the available properties of this object. |

## Async Works

| API | Description |
| :-- | :-- |
| napi\_create\_async\_work | Creates a work object that executes logic asynchronously. |
| napi\_delete\_async\_work | Releases an async work object. |
| napi\_queue\_async\_work | Adds an async work object to the queue so that it can be scheduled for execution. |
| napi\_cancel\_async\_work | Cancels a queued async work if it has not been started. |

## Custom Async Operations

| API | Description |
| :-- | :-- |
| napi\_async\_init | Creates an async context. The capabilities related to **async\_hook** are not supported. |
| napi\_make\_callback | Allows a JS function to be called in the async context. The capabilities related to **async\_hook** are not supported. |
| napi\_async\_destroy | Destroys the previously created async context. The capabilities related to **async\_hook** are not supported. |
| napi\_open\_callback\_scope | Opens a callback scope. The capabilities related to **async\_hook** are not supported. |
| napi\_close\_callback\_scope | Closes the callback scope. The capabilities related to **async\_hook** are not supported. |

## UV

| API | Description |
| :-- | :-- |
| napi\_get\_uv\_event\_loop | Obtains the current libuv loop instance. |

## Function Invocation

| API | Description |
| :-- | :-- |
| napi\_call\_function | Calls a JS function from a C/C++ addon. |
| napi\_get\_cb\_info | Obtains detailed information about the call, such as the parameters and **this** pointer, from the given callback info. |

## Environment Lifecycle

| API | Description |
| :-- | :-- |
| napi\_set\_instance\_data | Associates data with the currently running environment. |
| napi\_get\_instance\_data | Retrieves the data that was previously associated with the currently running environment. |

## Object Lifetime Management

| API | Description |
| :-- | :-- |
| napi\_add\_env\_cleanup\_hook | Adds a cleanup hook function for releasing resources when the environment exits. |
| napi\_remove\_env\_cleanup\_hook | Removes a cleanup hook function. |
| napi\_add\_async\_cleanup\_hook | Adds an async cleanup hook function for releasing resources when the environment exits. |
| napi\_remove\_async\_cleanup\_hook | Removes an async cleanup hook function. |

## Extended Capabilities

[Node-API Extended Symbols](https://developer.huawei.com/consumer/en/doc/harmonyos-references/napi#node-api-extended-symbols)

| API | Description |
| :-- | :-- |
| napi\_queue\_async\_work\_with\_qos | Adds an async work object to the queue and schedules it based on the QoS passed in. |
| napi\_run\_script\_path | Runs an .abc file. |
| napi\_load\_module | Loads an .abc file as a module. This API returns the namespace of the module. |
| napi\_load\_module\_with\_info | Loads an .abc file as a module. This API returns the namespace of the module, which can be used in the ArkTS runtime environment. |
| napi\_create\_object\_with\_properties | Creates a JS object using the given **napi\_property\_descriptor**. The key in **napi\_property\_descriptor** must be a string and cannot be converted into a number. |
| napi\_create\_object\_with\_named\_properties | Creates a JS object using the given **napi\_value**s and keys. The key must be a string and cannot be converted into a number. |
| napi\_coerce\_to\_native\_binding\_object | Forcibly binds a JS object and a native object. |
| napi\_create\_ark\_runtime | Creates an ArkTS runtime environment. |
| napi\_destroy\_ark\_runtime | Destroys an ArkTS runtime environment. |
| napi\_run\_event\_loop | Starts an underlying event loop. |
| napi\_stop\_event\_loop | Stops the underlying event loop. |
| napi\_serialize | Serializes an ArkTS object into native data. |
| napi\_deserialize | Deserializes native data into an ArkTS object. |
| napi\_delete\_serialization\_data | Deletes serialized data. |
| napi\_call\_threadsafe\_function\_with\_priority | Delivers a task to the ArkTS main thread based on the specified priority and enqueuing policy. |
| napi\_is\_sendable | Checks whether the given JS value is sendable. |
| napi\_define\_sendable\_class | Creates a sendable class. |
| napi\_create\_sendable\_object\_with\_properties | Creates a sendable object with the given **napi\_property\_descriptor**. |
| napi\_create\_sendable\_array | Creates a sendable array. |
| napi\_create\_sendable\_array\_with\_length | Creates a sendable array of the specified length. |
| napi\_create\_sendable\_arraybuffer | Creates a sendable ArrayBuffer. |
| napi\_create\_sendable\_typedarray | Creates a sendable TypedArray. |
| napi\_wrap\_sendable | Wraps a native instance into an ArkTS object. |
| napi\_wrap\_sendable\_with\_size | Wraps a native instance into an ArkTS object with the specified size. |
| napi\_unwrap\_sendable | Unwraps the native instance from an ArkTS object. |
| napi\_remove\_wrap\_sendable | Removes and obtains the native instance wrapped by an ArkTS object. After removal, the callback will no longer be triggered and must be manually deleted to free memory. |
| napi\_wrap\_enhance | Wraps a native instance of the specified size into an ArkTS object. During runtime, the instance size is counted and accumulated. When the accumulated size reaches the GC triggering threshold, the garbage collection process is started. You can specify whether to execute the registered callback asynchronously (if asynchronous, it must be thread-safe). |
| napi\_create\_ark\_context | Creates a context. |
| napi\_switch\_ark\_context | Switches to the specified runtime context environment. |
| napi\_destroy\_ark\_context | Destroys the context created by **napi\_create\_ark\_context**. |
| napi\_open\_critical\_scope | Opens a critical scope. |
| napi\_close\_critical\_scope | Closes a critical scope. |
| napi\_get\_buffer\_string\_utf16\_in\_critical\_scope | Obtains the UTF-16 encoding memory buffer data of an ArkTS string. |
| napi\_create\_strong\_reference | Creates a strong reference to an ArkTS object. |
| napi\_delete\_strong\_reference | Deletes a strong reference. |
| napi\_get\_strong\_reference\_value | Obtains the ArkTS object value associated with a strong reference object. |
| napi\_create\_strong\_sendable\_reference | Creates a Sendable strong reference to a Sendable ArkTS object. |
| napi\_delete\_strong\_sendable\_reference | Deletes a Sendable strong reference. |
| napi\_get\_strong\_sendable\_reference\_value | Obtains the ArkTS object value associated with a Sendable strong reference. |

**napi\_queue\_async\_work\_with\_qos**

napi\_status napi\_queue\_async\_work\_with\_qos(napi\_env env,
                                           napi\_async\_work work,
                                           napi\_qos\_t qos);

This API has the same usage as **napi\_queue\_async\_work**. The difference is you can specify the QoS for the work to run. For details about how to use **napi\_queue\_async\_work\_with\_qos**, see "Prioritizing Asynchronous Tasks". For details about QoS, see [QoS Development](../../thread-scheduling/qos-development/document.md).

**napi\_run\_script\_path**

napi\_status napi\_run\_script\_path(napi\_env env,
                                 const char\* abcPath,
                                 napi\_value\* result);

**Note**: For details about the restrictions, see [What should I observe when using napi\_run\_script\_path() to execute the abc files in a package](https://developer.huawei.com/consumer/en/doc/harmonyos-faqs/faqs-ndk-65).

**napi\_load\_module**

napi\_status napi\_load\_module(napi\_env env,
                             const char\* path,
                             napi\_value\* result);

**napi\_create\_object\_with\_properties**

napi\_status napi\_create\_object\_with\_properties(napi\_env env,
                                               napi\_value\* result,
                                               size\_t property\_count,
                                               const napi\_property\_descriptor\* properties);

**napi\_create\_object\_with\_named\_properties**

napi\_status napi\_create\_object\_with\_named\_properties(napi\_env env,
                                                     napi\_value\* result,
                                                     size\_t property\_count,
                                                     const char\*\* keys,
                                                     const napi\_value\* values);

**napi\_coerce\_to\_native\_binding\_object**

napi\_status napi\_coerce\_to\_native\_binding\_object(napi\_env env,
                                                 napi\_value js\_object,
                                                 napi\_native\_binding\_detach\_callback detach\_cb,
                                                 napi\_native\_binding\_attach\_callback attach\_cb,
                                                 void\* native\_object,
                                                 void\* hint);

**napi\_create\_ark\_runtime**

napi\_status napi\_create\_ark\_runtime(napi\_env \*env);

[Creating an ArkTS Runtime Environment Using napi\_create\_ark\_runtime and napi\_destroy\_ark\_runtime](../typical-node-api-use-cases/creating-an-arkts-runtime-environment-using-node-api/document.md)

**napi\_destroy\_ark\_runtime**

napi\_status napi\_destroy\_ark\_runtime(napi\_env \*env);

**napi\_run\_event\_loop**

napi\_status napi\_run\_event\_loop(napi\_env env, napi\_event\_mode mode);

You can call the **napi\_run\_event\_loop** and **napi\_stop\_event\_loop** APIs only in the ArkTS runtime environment created using **napi\_create\_ark\_runtime**. For details, see [Running or Stopping an Event Loop in an Asynchronous Thread Using Node-API Extension APIs](../typical-node-api-use-cases/running-or-stopping-an-event-loop-in-an-asynchronous-thread-using-node-api-exten/document.md).

**napi\_stop\_event\_loop**

napi\_status napi\_stop\_event\_loop(napi\_env env);

**napi\_serialize**

napi\_status napi\_serialize(napi\_env env,
                           napi\_value object,
                           napi\_value transfer\_list,
                           napi\_value clone\_list,
                           void\*\* result);

**napi\_deserialize**

napi\_status napi\_deserialize(napi\_env env, void\* buffer, napi\_value\* object);

**napi\_delete\_serialization\_data**

napi\_status napi\_delete\_serialization\_data(napi\_env env, void\* buffer);

**napi\_call\_threadsafe\_function\_with\_priority**

napi\_status napi\_call\_threadsafe\_function\_with\_priority(napi\_threadsafe\_function func,
                                                        void \*data,
                                                        napi\_task\_priority priority,
                                                        bool isTail);

**napi\_is\_sendable**

napi\_status napi\_is\_sendable(napi\_env env, napi\_value value, bool\* result);

**napi\_define\_sendable\_class**

napi\_status napi\_define\_sendable\_class(napi\_env env,
                                       const char\* utf8name,
                                       size\_t length,
                                       napi\_callback constructor,
                                       void\* data,
                                       size\_t property\_count,
                                       const napi\_property\_descriptor\* properties,
                                       napi\_value parent,
                                       napi\_value\* result);

**napi\_create\_sendable\_object\_with\_properties**

napi\_status napi\_create\_sendable\_object\_with\_properties(napi\_env env,
                                                        size\_t property\_count,
                                                        const napi\_property\_descriptor\* properties,
                                                        napi\_value\* result);

**napi\_create\_sendable\_array**

napi\_status napi\_create\_sendable\_array(napi\_env env, napi\_value\* result);

**napi\_create\_sendable\_array\_with\_length**

napi\_status napi\_create\_sendable\_array\_with\_length(napi\_env env, size\_t length, napi\_value\* result);

**napi\_create\_sendable\_arraybuffer**

napi\_status napi\_create\_sendable\_arraybuffer(napi\_env env, size\_t byte\_length, void\*\* data, napi\_value\* result);

**napi\_create\_sendable\_typedarray**

napi\_status napi\_create\_sendable\_typedarray(napi\_env env,
                                            napi\_typedarray\_type type,
                                            size\_t length,
                                            napi\_value arraybuffer,
                                            size\_t byte\_offset,
                                            napi\_value\* result);

**napi\_wrap\_sendable**

napi\_status napi\_wrap\_sendable(napi\_env env,
                               napi\_value js\_object,
                               void\* native\_object,
                               napi\_finalize finalize\_cb,
                               void\* finalize\_hint);

**napi\_wrap\_sendable\_with\_size**

napi\_status napi\_wrap\_sendable\_with\_size(napi\_env env,
                                         napi\_value js\_object,
                                         void\* native\_object,
                                         napi\_finalize finalize\_cb,
                                         void\* finalize\_hint,
                                         size\_t native\_binding\_size);

**napi\_unwrap\_sendable**

napi\_status napi\_unwrap\_sendable(napi\_env env, napi\_value js\_object, void\*\* result);

**napi\_remove\_wrap\_sendable**

napi\_status napi\_remove\_wrap\_sendable(napi\_env env, napi\_value js\_object, void\*\* result);

**napi\_wrap\_enhance**

napi\_status napi\_wrap\_enhance(napi\_env env,
                              napi\_value js\_object,
                              void\* native\_object,
                              napi\_finalize finalize\_cb,
                              bool async\_finalizer,
                              void\* finalize\_hint,
                              size\_t native\_binding\_size,
                              napi\_ref\* result);

**napi\_create\_ark\_context**

napi\_status napi\_create\_ark\_context(napi\_env env,
                                    napi\_env\* newEnv);

**napi\_switch\_ark\_context**

napi\_status napi\_switch\_ark\_context(napi\_env env);

**napi\_destroy\_ark\_context**

napi\_status napi\_destroy\_ark\_context(napi\_env env);

**napi\_open\_critical\_scope**

napi\_status napi\_open\_critical\_scope(napi\_env env, napi\_critical\_scope\* scope);

**napi\_close\_critical\_scope**

napi\_status napi\_close\_critical\_scope(napi\_env env, napi\_critical\_scope scope);

**napi\_get\_buffer\_string\_utf16\_in\_critical\_scope**

napi\_status napi\_get\_buffer\_string\_utf16\_in\_critical\_scope(napi\_env env,
                                                           napi\_value value,
                                                           const char16\_t\*\* buffer,
                                                           size\_t\* length);

**napi\_create\_strong\_reference**

napi\_status napi\_create\_strong\_reference(napi\_env env, napi\_value value, napi\_strong\_ref\* result);

**napi\_delete\_strong\_reference**

napi\_status napi\_delete\_strong\_reference(napi\_env env, napi\_strong\_ref ref)

**napi\_get\_strong\_reference\_value**

napi\_status napi\_get\_strong\_reference\_value(napi\_env env, napi\_strong\_ref ref, napi\_value\* result)

**napi\_create\_external\_string\_utf16**

napi\_status napi\_create\_external\_string\_utf16(napi\_env env,
                                              const char16\_t\* str,
                                              size\_t length,
                                              napi\_finalize\_callback finalize\_callback,
                                              void\* finalize\_hint,
                                              napi\_value\* result);

**napi\_create\_external\_string\_ascii**

napi\_status napi\_create\_external\_string\_ascii(napi\_env env,
                                              const char\* str,
                                              size\_t length,
                                              napi\_finalize\_callback finalize\_callback,
                                              void\* finalize\_hint,
                                              napi\_value\* result);

**napi\_create\_strong\_sendable\_reference**

napi\_status napi\_create\_strong\_sendable\_reference(napi\_env env,
                                                  napi\_value value,
                                                  napi\_sendable\_ref\* result);

**napi\_delete\_strong\_sendable\_reference**

napi\_status napi\_delete\_strong\_sendable\_reference(napi\_env env, napi\_sendable\_ref ref);

**napi\_get\_strong\_sendable\_reference\_value**

napi\_status napi\_get\_strong\_sendable\_reference\_value(napi\_env env,
                                                     napi\_sendable\_ref ref,
                                                     napi\_value\* result);

## Other Utilities

| API | Description |
| :-- | :-- |
| napi\_get\_version | Obtains the latest Node-API version supported by the node runtime. |
| node\_api\_get\_module\_file\_name | Obtains the absolute path of the module to be loaded. |
| napi\_strict\_equals | Compares whether two values are strictly equal, that is, whether they are of the same type and have the same value. |
