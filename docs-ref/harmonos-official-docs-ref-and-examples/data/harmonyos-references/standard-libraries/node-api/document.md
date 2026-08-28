# Node-API

#### Introduction

Node-API provides APIs to encapsulate JavaScript (JS) capabilities as native addons. It is independent of the underlying JS and is maintained as part of Node.js.

#### Supported Capabilities

Node-API insulates addons from changes in the underlying JS engine and allows the modules compiled for one major version to run on later major versions without recompilation.

The HarmonyOS Node-API component optimizes the Node-API implementation and provides interaction with underlying engines such as ArkJS. Currently, the HarmonyOS Node-API component does not support all Node-API APIs.

#### Including Node-API Capabilities

To use Node-API, include the following header file:

#include <napi/native\_api.h>

Add the following dynamic link library to **CMakeLists.txt**:

libace\_napi.z.so

#### Symbols Exported from the Node-API Library

The APIs exported from the native Node-API library feature usage and behaviors based on [Node.js](https://nodejs.org/docs/latest-v12.x/api/n-api.html) and have incorporated [extended capabilities](#node-api-extended-symbols).

| Symbol Type | Symbol | Description | Start API Version |
| :-- | :-- | :-- | :-- |
| FUNC | napi\_module\_register | Registers a native module. | 10 |
| FUNC | napi\_get\_last\_error\_info | Obtains the napi\_extended\_error\_info struct, which contains the latest error information. | 10 |
| FUNC | napi\_throw | Throws a JS value. | 10 |
| FUNC | napi\_throw\_error | Throws a JS **Error** with text information. | 10 |
| FUNC | napi\_throw\_type\_error | Throws a JS **TypeError** with text information. | 10 |
| FUNC | napi\_throw\_range\_error | Throws a JS **RangeError** with text information. | 10 |
| FUNC | napi\_is\_error | Checks whether **napi\_value** indicates an error object. | 10 |
| FUNC | napi\_create\_error | Creates a JS **Error** with text information. | 10 |
| FUNC | napi\_create\_type\_error | Creates a JS **TypeError** with text information. | 10 |
| FUNC | napi\_create\_range\_error | Creates a JS **RangeError** with text information. | 10 |
| FUNC | napi\_get\_and\_clear\_last\_exception | Obtains and clears the latest exception. | 10 |
| FUNC | napi\_is\_exception\_pending | Checks whether an exception occurs. | 10 |
| FUNC | napi\_fatal\_error | Raises a fatal error to terminate the process immediately. | 10 |
| FUNC | napi\_open\_handle\_scope | Opens a scope. | 10 |
| FUNC | napi\_close\_handle\_scope | Closes the scope passed in. After the scope is closed, all references declared in it are closed. | 10 |
| FUNC | napi\_open\_escapable\_handle\_scope | Opens an escapable handle scope, from which the declared values can be returned to the parent scope. | 10 |
| FUNC | napi\_close\_escapable\_handle\_scope | Closes the escapable handle scope passed in. | 10 |
| FUNC | napi\_escape\_handle | Promotes the handle to the input JS object so that it is valid for the lifespan of its outer scope. | 10 |
| FUNC | napi\_create\_reference | Creates a reference for an **Object** to extend its lifespan. The caller needs to manage the reference lifespan. | 10 |
| FUNC | napi\_delete\_reference | Deletes the reference passed in. | 10 |
| FUNC | napi\_reference\_ref | Increments the reference count for the reference passed in and returns the count. | 10 |
| FUNC | napi\_reference\_unref | Decrements the reference count for the reference passed in and returns the count. | 10 |
| FUNC | napi\_get\_reference\_value | Obtains the JS **Object** associated with the reference. | 10 |
| FUNC | napi\_create\_array | Creates a JS array. | 10 |
| FUNC | napi\_create\_array\_with\_length | Creates a JS array of the specified length. | 10 |
| FUNC | napi\_create\_arraybuffer | Creates a JS **ArrayBuffer** of the specified size. | 10 |
| FUNC | napi\_create\_external | Allocates a JS value with external data. | 10 |
| FUNC | napi\_create\_external\_arraybuffer | Allocates a JS **ArrayBuffer** with external data. | 10 |
| FUNC | napi\_create\_object | Creates a default JS object. | 10 |
| FUNC | napi\_create\_symbol | Creates a JS symbol. | 10 |
| FUNC | napi\_create\_typedarray | Creates a JS **TypeArray** from an existing **ArrayBuffer**. | 10 |
| FUNC | napi\_create\_dataview | Creates a JS **DataView** from an existing **ArrayBuffer**. | 10 |
| FUNC | napi\_create\_int32 | Creates a JS number from C int32\_t data. | 10 |
| FUNC | napi\_create\_uint32 | Creates a JS number from C uint32\_t data. | 10 |
| FUNC | napi\_create\_int64 | Creates a JS number from C int64\_t data. | 10 |
| FUNC | napi\_create\_double | Creates a JS number from C double data. | 10 |
| FUNC | napi\_create\_string\_latin1 | Creates a JS string from an ISO-8859-1-encoded C string. | 10 |
| FUNC | napi\_create\_string\_utf8 | Creates a JS string from a UTF8-encoded C string. | 10 |
| FUNC | napi\_create\_string\_utf16 | Creates a JS string from a UTF16-encoded C string. | 10 |
| FUNC | napi\_get\_array\_length | Obtains the array length. | 10 |
| FUNC | napi\_get\_arraybuffer\_info | Obtains the underlying data buffer of an **ArrayBuffer** and its length. | 10 |
| FUNC | napi\_get\_prototype | Obtains the prototype of a JS object. | 10 |
| FUNC | napi\_get\_typedarray\_info | Obtains properties of a **TypedArray**. | 10 |
| FUNC | napi\_get\_dataview\_info | Obtains properties of a **DataView**. | 10 |
| FUNC | napi\_get\_value\_bool | Obtains the C Boolean equivalent of a JS Boolean value. | 10 |
| FUNC | napi\_get\_value\_double | Obtains the C double equivalent of a JS number. | 10 |
| FUNC | napi\_get\_value\_external | Obtains the external data pointer previously passed through **napi\_create\_external()**. | 10 |
| FUNC | napi\_get\_value\_int32 | Obtains the C int32 equivalent of a JS number. | 10 |
| FUNC | napi\_get\_value\_int64 | Obtains the C int64 equivalent of a JS number. | 10 |
| FUNC | napi\_get\_value\_string\_latin1 | Obtains the ISO-8859-1-encoded string corresponding to the given JS value. | 10 |
| FUNC | napi\_get\_value\_string\_utf8 | Obtains the UTF8-encoded string corresponding to the given JS value. | 10 |
| FUNC | napi\_get\_value\_string\_utf16 | Obtains the UTF16-encoded string corresponding to the given JS value. | 10 |
| FUNC | napi\_get\_value\_uint32 | Obtains the C uint32 equivalent of a JS number. | 10 |
| FUNC | napi\_get\_boolean | Obtains a JS Boolean object based on a C Boolean value. | 10 |
| FUNC | napi\_get\_global | Obtains the global object. | 10 |
| FUNC | napi\_get\_null | Obtains the null object. | 10 |
| FUNC | napi\_get\_undefined | Obtains the undefined object. | 10 |
| FUNC | napi\_coerce\_to\_bool | Forcibly converts a JS value to a JS Boolean value. | 10 |
| FUNC | napi\_coerce\_to\_number | Forcibly converts a JS value to a JS number. | 10 |
| FUNC | napi\_coerce\_to\_object | Forcibly converts a JS value to a JS object. | 10 |
| FUNC | napi\_coerce\_to\_string | Forcibly converts a JS value to a JS string. | 10 |
| FUNC | napi\_typeof | Obtains the JS type of a JS value. | 10 |
| FUNC | napi\_instanceof | Checks whether an object is an instance of the specified constructor. | 10 |
| FUNC | napi\_is\_array | Checks whether a JS value is an array. | 10 |
| FUNC | napi\_is\_arraybuffer | Checks whether a JS value is an ArrayBuffer. | 10 |
| FUNC | napi\_is\_typedarray | Checks whether a JS value is a TypedArray. | 10 |
| FUNC | napi\_is\_dataview | Checks whether a JS value is a DataView. | 10 |
| FUNC | napi\_is\_date | Checks whether a JS value is a JS Date object. | 10 |
| FUNC | napi\_strict\_equals | Checks whether two JS values are strictly equal. | 10 |
| FUNC | napi\_get\_property\_names | Obtains the names of the enumerable properties of an object in an array of strings. | 10 |
| FUNC | napi\_set\_property | Sets a property for an object. | 10 |
| FUNC | napi\_get\_property | Obtains the requested property of an object. | 10 |
| FUNC | napi\_has\_property | Checks whether an object has the specified property. | 10 |
| FUNC | napi\_delete\_property | Deletes the **key** property from an object. | 10 |
| FUNC | napi\_has\_own\_property | Checks whether an object has the own property named **key**. | 10 |
| FUNC | napi\_set\_named\_property | Sets a property with the given name for an object. | 10 |
| FUNC | napi\_get\_named\_property | Obtains the property with the given name in an object. | 10 |
| FUNC | napi\_has\_named\_property | Checks whether an object has the property with the given name. | 10 |
| FUNC | napi\_set\_element | Sets an element at the specified index of an object. | 10 |
| FUNC | napi\_get\_element | Obtains the element at the specified index of an object. | 10 |
| FUNC | napi\_has\_element | Obtains the element if the object has an element at the specified index. | 10 |
| FUNC | napi\_delete\_element | Deletes the element at the specified index of an object. | 10 |
| FUNC | napi\_define\_properties | Defines multiple properties for an object. | 10 |
| FUNC | napi\_type\_tag\_object | Associates the value of a tag pointer with an object. | 10 |
| FUNC | napi\_check\_object\_type\_tag | Checks whether a tag pointer is associated with a JS object. | 10 |
| FUNC | napi\_call\_function | Calls a JS function object in a native method, that is, native calls JS. | 10 |
| FUNC | napi\_create\_function | Creates a function object in native code for JS to call. | 10 |
| FUNC | napi\_get\_cb\_info | Obtains detailed information about the call, such as the parameters and **this** pointer, from the given callback information. | 10 |
| FUNC | napi\_get\_new\_target | Obtains the **new.target** of the constructor call. | 10 |
| FUNC | napi\_new\_instance | Creates an instance based on the given constructor. | 10 |
| FUNC | napi\_define\_class | Defines a JS class corresponding to the C++ class. | 10 |
| FUNC | napi\_wrap | Wraps a native instance in a JS object. | 10 |
| FUNC | napi\_unwrap | Unwraps the native instance from a JS object. | 10 |
| FUNC | napi\_remove\_wrap | Removes the native instance from the JS object. | 10 |
| FUNC | napi\_create\_async\_work | Creates a work object that executes logic asynchronously. | 10 |
| FUNC | napi\_delete\_async\_work | Releases an async work object. | 10 |
| FUNC | napi\_queue\_async\_work | Adds an async work object to the queue so that it can be scheduled for execution. | 10 |
| FUNC | napi\_cancel\_async\_work | Cancels the queued async work if it has not been started. | 10 |
| FUNC | napi\_async\_init | Creates an async context. The capabilities related to **async\_hook** are not supported. | 11 |
| FUNC | napi\_make\_callback | Allows a JS function to be called in the async context. The capabilities related to **async\_hook** are not supported. | 11 |
| FUNC | napi\_async\_destroy | Destroys an async context. The capabilities related to **async\_hook** are not supported. | 11 |
| FUNC | napi\_open\_callback\_scope | Opens a callback scope. The capabilities related to **async\_hook** are not supported. | 11 |
| FUNC | napi\_close\_callback\_scope | Closes a callback scope. The capabilities related to **async\_hook** are not supported. | 11 |
| FUNC | napi\_get\_node\_version | Obtains the current Node-API version. | 10 |
| FUNC | napi\_get\_version | Obtains the latest Node-API version supported when the Node.js runtime. | 10 |
| FUNC | napi\_create\_promise | Creates a deferred object and a JS promise. | 10 |
| FUNC | napi\_resolve\_deferred | Resolves a deferred object that is associated with a JS promise. | 10 |
| FUNC | napi\_reject\_deferred | Rejects a deferred object that is associated with a JS promise. | 10 |
| FUNC | napi\_is\_promise | Checks whether the given JS value is a promise object. | 10 |
| FUNC | napi\_get\_uv\_event\_loop | Obtains the current libuv loop instance. | 10 |
| FUNC | napi\_create\_threadsafe\_function | Creates a thread-safe function. | 10 |
| FUNC | napi\_get\_threadsafe\_function\_context | Obtains the context of a thread-safe function. | 10 |
| FUNC | napi\_call\_threadsafe\_function | Calls a thread-safe function. | 10 |
| FUNC | napi\_acquire\_threadsafe\_function | Acquires a thread-safe function. | 10 |
| FUNC | napi\_release\_threadsafe\_function | Releases a thread-safe function. | 10 |
| FUNC | napi\_ref\_threadsafe\_function | Creates a reference to a thread-safe function. The event loop running on the main thread should not exit until the thread-safe function is destroyed. | 10 |
| FUNC | napi\_unref\_threadsafe\_function | Releases the reference to a thread-safe function. The event loop running on the main thread may exit before the thread-safe function is destroyed. | 10 |
| FUNC | napi\_create\_date | Creates a JS Date object from C double data. | 10 |
| FUNC | napi\_get\_date\_value | Obtains the C double equivalent of the given JS Date. | 10 |
| FUNC | napi\_create\_bigint\_int64 | Creates a JS BigInt from C int64 data. | 10 |
| FUNC | napi\_create\_bigint\_uint64 | Creates a JS BigInt from C uint64 data. | 10 |
| FUNC | napi\_create\_bigint\_words | Creates a single JS BigInt from a C uint64 array. | 10 |
| FUNC | napi\_get\_value\_bigint\_int64 | Obtains the C int64 equivalent of the given JS BigInt. | 10 |
| FUNC | napi\_get\_value\_bigint\_uint64 | Obtains the C uint64 equivalent of the given JS BigInt. | 10 |
| FUNC | napi\_get\_value\_bigint\_words | Obtains information from the given JS BigInt, including the sign bit, 64-bit little-endian array, and number of elements in the array. | 10 |
| FUNC | napi\_create\_buffer | Creates a JS Buffer instance of the specified size. | 10 |
| FUNC | napi\_create\_buffer\_copy | Creates a JS Buffer instance of the specified size, and initializes it with data copied from the passed-in buffer. | 10 |
| FUNC | napi\_create\_external\_buffer | Creates a JS Buffer instance of the specified size, and initializes it with the given data. The Buffer instance created can include extra. | 10 |
| FUNC | napi\_get\_buffer\_info | Obtains the underlying data of Buffer and its length. | 10 |
| FUNC | napi\_is\_buffer | Checks whether the given JS value is a Buffer object. | 10 |
| FUNC | napi\_object\_freeze | Freezes the given object. | 10 |
| FUNC | napi\_object\_seal | Seals the given object. | 10 |
| FUNC | napi\_get\_all\_property\_names | Obtains an array containing the names of all the available properties of this object. | 10 |
| FUNC | napi\_detach\_arraybuffer | Detaches the underlying data of the given ArrayBuffer. | 10 |
| FUNC | napi\_is\_detached\_arraybuffer | Checks whether the given ArrayBuffer has been detached. | 10 |
| FUNC | napi\_run\_script | Runs an object as JS code. Currently, this API is an empty implementation. For security purposes, you are advised to use **napi\_run\_script\_path**. | 10 |
| FUNC | napi\_set\_instance\_data | Associates data with the currently running environment. | 11 |
| FUNC | napi\_get\_instance\_data | Retrieves the data that was previously associated with the currently running environment. | 11 |
| FUNC | napi\_add\_env\_cleanup\_hook | Registers a clean-up hook for releasing resources when the environment exits. | 11 |
| FUNC | napi\_remove\_env\_cleanup\_hook | Unregisters the clean-up hook. | 11 |
| FUNC | napi\_add\_async\_cleanup\_hook | Registers an async clean-up hook for releasing resources when the environment exits. | 11 |
| FUNC | napi\_remove\_async\_cleanup\_hook | Unregisters the async clean-up hook. | 11 |
| FUNC | node\_api\_get\_module\_file\_name | Obtains the absolute path of the location, from which the addon is loaded. | 11 |
| FUNC | napi\_add\_finalizer | Adds a **napi\_finalize** callback, which will be called when the JS object in **js\_Object** is garbage-collected. | 11 |
| FUNC | napi\_fatal\_exception | Throws **UncaughtException** to JS. | 12 |

#### Differences Between the Exported Symbols and the Symbols in the Native Library

For ease of description, the symbol exported to HarmonyOS is referred to as "exported symbol" and the symbol in the native library is referred to as "native symbol".

## napi\_throw\_error

**Return value**

-   If **code** is a null pointer, the native symbol returns **napi\_invalid\_arg**, whereas the exported symbol does not check the validity of **code**.
    
-   The exported symbol permits a failure in setting **code**.
    

## napi\_throw\_type\_error

**Return value**

-   If **code** is a null pointer, the native symbol returns **napi\_invalid\_arg**, whereas the exported symbol does not check the validity of **code**.
    
-   The exported symbol permits a failure in setting **code**.
    

## napi\_throw\_range\_error

**Return value**

-   If **code** is a null pointer, the native symbol returns **napi\_invalid\_arg**, whereas the exported symbol does not check the validity of **code**.
    
-   The exported symbol permits a failure in setting **code**.
    

## napi\_create\_error

**Parameters**

-   **code**: The value type can be string or number in the exported symbol.

**Return value**

-   If the code type is incorrect, the exported symbol returns **napi\_invalid\_arg**.
    
-   The exported symbol permits a failure in setting **code**.
    

## napi\_create\_type\_error

**Parameters**

-   **code**: In HarmonyOS, the value type can be string or number. However, in the standard library interface, the value type can only be string.

**Return value**

-   If the **code** type is incorrect, the HarmonyOS interface returns napi\_invalid\_arg, whereas the standard library interface returns napi\_string\_expected.
    
-   The HarmonyOS export interface allows the **code** property to fail without error, whereas the standard library interface evaluates the setting. If the setting fails, it returns napi\_genetic\_failure.
    
-   The error type created in HarmonyOS is Error, whereas that created in the standard library is TypeError.
    

## napi\_create\_range\_error

**Parameters**

-   **code**: In HarmonyOS, the value type can be string or number. However, in the standard library interface, the value type can only be string.

**Return value**

-   If the **code** type is incorrect, the HarmonyOS interface returns napi\_invalid\_arg, whereas the standard library interface returns napi\_string\_expected.
    
-   The HarmonyOS export interface allows the **code** property to fail without error, whereas the standard library interface evaluates the setting. If the setting fails, it returns napi\_genetic\_failure.
    
-   The error type created in HarmonyOS is Error, whereas that created in the standard library is RangeError.
    

## napi\_create\_reference

**Parameters**

-   **value**: The HarmonyOS API does not restrict the value type. The standard library supports only object, function, and symbol types.

## napi\_delete\_reference

**NOTE**

-   In HarmonyOS, if the **napi\_finalize** callback is registered when a strong reference is created, calling this API will trigger the **napi\_finalize** callback.

## napi\_create\_symbol

**Return value**

-   The exported symbol returns **napi\_invalid\_arg** if **description** is not empty and is not a string.

## napi\_create\_typedarray

**Return value**

-   The exported symbol returns **napi\_arraybuffer\_expected** if **arraybuffer** is not empty and is not an ArrayBuffer object.

## napi\_create\_dataview

**Return value**

-   The exported symbol returns **napi\_arraybuffer\_expected** if **arraybuffer** is not empty and is not an ArrayBuffer object.
    
-   If the sum of **byte\_offset** and **byte\_length** is greater than the size of **arraybuffer**, the export API throws a **RangeError** exception and returns **napi\_pending\_exception**.
    

## napi\_get\_typedarray\_info

**Parameters**

-   **object**: The exported symbol supports TypedArray or Sendable TypedArray ([Int8Array](../../application-framework/arkts/arkts-apis/arkts-collections-arkts-collections/class-int8array/document.md), [Uint8Array](../../application-framework/arkts/arkts-apis/arkts-collections-arkts-collections/class-uint8array/document.md), [Int16Array](../../application-framework/arkts/arkts-apis/arkts-collections-arkts-collections/class-int16array/document.md), [Uint16Array](../../application-framework/arkts/arkts-apis/arkts-collections-arkts-collections/class-uint16array/document.md), [Int32Array](../../application-framework/arkts/arkts-apis/arkts-collections-arkts-collections/class-int32array/document.md), [Uint32Array](../../application-framework/arkts/arkts-apis/arkts-collections-arkts-collections/class-uint32array/document.md), [Uint8ClampedArray](../../application-framework/arkts/arkts-apis/arkts-collections-arkts-collections/class-uint8clampedarray/document.md), and [Float32Array](../../application-framework/arkts/arkts-apis/arkts-collections-arkts-collections/class-float32array/document.md)).

**Return value**

-   The native symbol returns the number of elements in TypedArray via the **length** parameter; while the exported symbol returns length of the elements in TypedArray, in bytes.

## napi\_coerce\_to\_object

**Return value**

-   If **value** is **undefined** or null, the exported symbol returns **napi\_ok** and **undefined** in **result**.

## napi\_instanceof

**Return value**

-   If **object** is not an object, the exported symbol returns **napi\_object\_expected** with **result** unprocessed.
    
-   If **constructor** is not a function object, the exported symbol returns **napi\_function\_expected** without throwing any exception.
    

## napi\_is\_typedarray

**Parameters**

-   **value**: The exported symbol also supports Sendable TypedArray ([Int8Array](../../application-framework/arkts/arkts-apis/arkts-collections-arkts-collections/class-int8array/document.md), [Uint8Array](../../application-framework/arkts/arkts-apis/arkts-collections-arkts-collections/class-uint8array/document.md), [Int16Array](../../application-framework/arkts/arkts-apis/arkts-collections-arkts-collections/class-int16array/document.md), [Uint16Array](../../application-framework/arkts/arkts-apis/arkts-collections-arkts-collections/class-uint16array/document.md), [Int32Array](../../application-framework/arkts/arkts-apis/arkts-collections-arkts-collections/class-int32array/document.md), [Uint32Array](../../application-framework/arkts/arkts-apis/arkts-collections-arkts-collections/class-uint32array/document.md), [Uint8ClampedArray](../../application-framework/arkts/arkts-apis/arkts-collections-arkts-collections/class-uint8clampedarray/document.md) and [Float32Array](../../application-framework/arkts/arkts-apis/arkts-collections-arkts-collections/class-float32array/document.md)).

## napi\_get\_property\_names

**Return value**

-   If **object** is not an object or a function, the exported symbol returns **napi\_object\_expected**.

## napi\_set\_property

**Return value**

-   If **object** is not an object or a function, the exported symbol returns **napi\_object\_expected**.

## napi\_get\_property

**Return value**

-   If **object** is not an object or a function, the exported symbol returns **napi\_object\_expected**.

## napi\_has\_property

**Return value**

-   If **object** is not an object or a function, the exported symbol returns **napi\_object\_expected**.

## napi\_delete\_property

**Return value**

-   If **object** is not an object or a function, the exported symbol returns **napi\_object\_expected**.

## napi\_has\_own\_property

**Return value**

-   If **object** is not an object or a function, the exported symbol returns **napi\_object\_expected**.

## napi\_set\_named\_property

**Return value**

-   If **object** is not an object or a function, the exported symbol returns **napi\_object\_expected**.

## napi\_get\_named\_property

**Return value**

-   If **object** is not an object or a function, the exported symbol returns **napi\_object\_expected**.

## napi\_has\_named\_property

**Return value**

-   If **object** is not an object or a function, the exported symbol returns **napi\_object\_expected**.

## napi\_set\_element

**Return value**

-   If **object** is not an object or a function, the exported symbol returns **napi\_object\_expected**.
    
-   If the **index** value is too large, the native symbol throws an exception and interrupts the process. HarmonyOS attempts to allocate memory. If the memory allocation fails, **object** will not be modified.
    

## napi\_get\_element

**Return value**

-   If **object** is not an object or a function, the exported symbol returns **napi\_object\_expected**.

## napi\_has\_element

**Return value**

-   If **object** is not an object or a function, the exported symbol returns **napi\_object\_expected**.

## napi\_delete\_element

**Return value**

-   If **object** is not an object or a function, the exported symbol returns **napi\_object\_expected**.

## napi\_define\_properties

**Return value**

-   If **object** is not an object or a function, the exported symbol returns **napi\_object\_expected**.
    
-   If an exception is triggered during property traversal, the native symbol throws the exception, whereas the exported symbol clears the exception and continues the execution.
    

## napi\_type\_tag\_object

**Return value**

-   If **js\_object** is not an object or a function, the exported symbol returns **napi\_object\_expected**.

## napi\_check\_object\_type\_tag

**Return value**

-   If **js\_object** is not an object or a function, the exported symbol returns **napi\_object\_expected**.

## napi\_call\_function

**Return value**

-   The export symbol does not check whether the **recv** parameter is **nullptr**.
    
-   If **func** is not a function, the export symbol returns **napi\_function\_expected**.
    

## napi\_new\_instance

**Return value**

-   If **constructor** is not a function, the export symbol returns **napi\_function\_expected**.

## napi\_define\_class

**Return value**

-   If **length** is not **NAPI\_AUTO\_LENGTH** and is greater than **INT\_MAX**, the exported symbol returns **napi\_object\_expected**.

## napi\_wrap

**Parameters**

-   **finalize\_cb**: It can be empty in the native symbol. If this parameter is empty, the exported symbol returns **napi\_invalid\_arg**.
-   **result**: The native symbol returns a weak reference, whereas the exported symbol returns a strong reference if **result** is not empty.

**Return value**

-   If **js\_object** is not an object or a function, the exported symbol returns **napi\_object\_expected**.

## napi\_unwrap

**Return value**

-   If **js\_object** is not an object or a function, the exported symbol returns **napi\_object\_expected**.

## napi\_remove\_wrap

**Return value**

-   If **js\_object** is not an object or a function, the exported symbol returns **napi\_object\_expected**.

**NOTE**

-   If the wrap is associated with the **finalize** callback, the export symbol will call **finalize()** before removing the wrap.

## napi\_create\_async\_work

**Parameters**

-   The exported symbol does not support **async\_hooks**.
    
-   The exported symbol does not verify whether the input parameter **async\_resource\_name** is of the string type. A value of string type is recommended. If **async\_resource\_name** is of the string type, the trace information contains the string. Otherwise, the trace information does not contain it.
    
-   The exported symbol does not process the input parameter **async\_resource** because it does not support **async\_hooks**.
    

## napi\_delete\_async\_work

**Parameters**

-   The exported symbol does not support **async\_hooks**.

## napi\_queue\_async\_work

**Parameters**

-   The exported symbol does not support **async\_hooks**.

## napi\_cancel\_async\_work

**Return value**

-   If the task fails to be canceled due to the underlying UV, the native symbol returns **napi\_generic\_failure**, **napi\_invalid\_arg**, or **napi\_cancelled** based on the failure cause. The exported symbol does not verify the UV return value. You can check whether the task fails to be canceled based on log information.

## napi\_async\_init

**NOTE**

-   Currently, HarmonyOS does not support **async\_hooks**. After the exported symbol is called, operations related to **async\_hooks** will not be performed.

## napi\_make\_callback

**NOTE**

-   Currently, HarmonyOS does not support **async\_hooks**. After the exported symbol is called, operations related to **async\_hooks** will not be performed.

## napi\_async\_destroy

**NOTE**

-   Currently, HarmonyOS does not support **async\_hooks**. After the exported symbol is called, operations related to **async\_hooks** will not be performed.

## napi\_get\_node\_version

**NOTE**

-   HarmonyOS does not need to obtain the node version. Therefore, the export symbol is an empty implementation.

## napi\_resolve\_deferred

**NOTE**

-   When an exception occurs in the **resolve** or **reject** callback of the **then()** method of the promise, if the promise does not have a catch block, the code execution continues. If the promise has a catch block, the exception will be captured by the catch block.

## napi\_reject\_deferred

**NOTE**

-   When an exception occurs in the **resolve** or **reject** callback of the **then()** method of the promise, if the promise does not have a catch block, the code execution continues. If the promise has a catch block, the exception will be captured by the catch block.

## napi\_create\_threadsafe\_function

**Parameters**

-   **initial\_thread\_count**: The maximum value is **128** in the exported symbol.
    
-   **async\_resource**: There is no type restriction for this parameter in the exported symbol.
    
-   **async\_resource\_name**: There is no type restriction for this parameter in the exported symbol.
    
-   **func**: There is no type restriction for this parameter in the exported symbol.
    

**NOTE**

-   In HarmonyOS, the **cleanup hook** method is not registered when a thread-safe function is created. You can call **napi\_add\_env\_cleanup\_hook** if required.

## napi\_call\_threadsafe\_function

**NOTE**

-   Before **uv\_async\_send** is called in HarmonyOS, **env** is checked.
    
-   If **uv\_async\_send** fails to be called, the exported symbol returns **napi\_generic\_failure**.
    

## napi\_release\_threadsafe\_function

**NOTE**

-   Before **uv\_async\_send** is called in HarmonyOS, **env** is checked.
    
-   If **ThreadCount** is **0**, the exported symbol returns **napi\_generic\_failure**.
    

## napi\_ref\_threadsafe\_function

**NOTE**

-   The exported symbol checks whether **func** and **env** belong to the same ArkTS thread. If not, **napi\_generic\_failure** is returned.

## napi\_unref\_threadsafe\_function

**NOTE**

-   The exported symbol checks whether **func** and **env** belong to the same ArkTS thread. If not, **napi\_generic\_failure** is returned.

## napi\_create\_date

**Return value**

-   If the input parameters are correct but **date** fails to be created, the native symbol returns **napi\_generic\_failure**. In HarmonyOS, an exception is thrown, and the exported symbol returns **napi\_pending\_exception**.

## napi\_create\_bigint\_words

**Return value**

-   If the input parameters are correct but bigInt fails to be created, the native symbol returns **napi\_generic\_failure**. In HarmonyOS, an exception is thrown, and the exported symbol returns **napi\_pending\_exception**.

## napi\_get\_value\_bigint\_words

**Return value**

-   If **value** is not a BigInt object, the exported symbol returns **napi\_object\_expected**.

## napi\_create\_buffer

**Return value**

-   The buffer created in HarmonyOS is of the ArrayBufferLike type.
    
-   If **size** is less than or equal to **0**, the exported symbol returns **napi\_invalid\_arg**.
    
-   If **size** is greater than **2097152**, the exported symbol returns **napi\_invalid\_arg** and logs an error.
    
-   If **data** is **nullptr**, the exported symbol returns **napi\_invalid\_arg**.
    
-   If an exception occurs before the native symbol is called or exited, **napi\_pending\_exception** is returned. There is no such verification in HarmonyOS.
    

## napi\_create\_buffer\_copy

**Return value**

-   The buffer created in HarmonyOS is of the ArrayBufferLike type.
    
-   If **length** is less than or equal to **0**, the exported symbol returns **napi\_invalid\_arg**.
    
-   If **length** is greater than **2097152**, the exported symbol returns **napi\_invalid\_arg** and logs an error.
    
-   If **data** is **nullptr**, the exported symbol returns **napi\_invalid\_arg**.
    
-   If an exception occurs before the native symbol is called or exited, **napi\_pending\_exception** is returned. There is no such verification in HarmonyOS.
    

## napi\_create\_external\_buffer

**Return value**

-   The buffer created in HarmonyOS is of the ArrayBufferLike type.
    
-   If **length** is less than or equal to **0**, the exported symbol returns **napi\_invalid\_arg**.
    
-   If **length** is greater than **2097152**, the exported symbol returns **napi\_invalid\_arg** and logs an error.
    
-   If the buffer fails to be created due to an identified cause, the native symbol returns **napi\_generic\_failure**, whereas the exported symbol returns **napi\_pending\_exception**.
    

## napi\_get\_buffer\_info

**Return value**

-   HarmonyOS checks whether the value belongs to **buffer**. If not, **napi\_arraybuffer\_expected** is returned.

## napi\_detach\_arraybuffer

**Return value**

-   If **arraybuffer** is not an object, the exported symbol returns **napi\_object\_expected**. If **arraybuffer** is an object but not an ArrayBuffer object, it returns **napi\_invalid\_arg**.

## napi\_add\_env\_cleanup\_hook

**NOTE**

-   If data is registered with **env**, HarmonyOS prints only error logs.

## napi\_add\_finalizer

**Return value**

-   If **js\_object** is not an object, the exported symbol returns **napi\_object\_expected**.

**NOTE**

-   When a strong reference is deleted, HarmonyOS immediately triggers a callback, whereas the standard library does so during object destruction.
    
-   If a callback throws an exception, HarmonyOS will cause a JSCrash, but the standard library will not trigger a crash.
    
-   HarmonyOS creates a strong reference when the result is non-empty, whereas the standard library opts for a weak reference in such cases.
    

## napi\_fatal\_exception

**Parameters**

-   **err**: The exported symbol supports only the **Error** type. If the type does not match, **napi\_invalid\_arg** is returned.

## napi\_get\_uv\_event\_loop

**Return value**

-   If **env** is not a valid **napi\_env** (for example, it is a released **env**), the exported symbol returns **napi\_generic\_failure**.

## napi\_create\_array\_with\_length

**Return value**

-   If **length** is too large, the native symbol throws an exception and interrupts the process. HarmonyOS attempts to allocate memory. If the memory allocation fails, an exception is thrown and an array with length of 0 is returned.

## napi\_create\_arraybuffer

**Return value**

-   If **length** is too large, the native symbol throws an exception and interrupts the process. HarmonyOS attempts to allocate memory. If the memory allocation fails, an exception is thrown and **undefined** is returned.

#### Symbols Not Exported from the Node-API Library

| Symbol Type | Symbol | Description |
| :-- | :-- | :-- |
| FUNC | napi\_adjust\_external\_memory | Adjusts the external memory held by a JS object. |

#### Node-API Extended Symbols

| Symbol Type | Symbol | Description | Start API Version |
| :-- | :-- | :-- | :-- |
| FUNC | napi\_queue\_async\_work\_with\_qos | Adds an async work object to the queue so that it can be scheduled for execution based on the QoS priority passed in. | 10 |
| FUNC | napi\_run\_script\_path | Runs an ABC file. | 10 |
| FUNC | napi\_load\_module | Loads an .abc file as a module. This API returns the namespace of the module. | 11 |
| FUNC | napi\_create\_object\_with\_properties | Creates a JS object using the given **napi\_property\_descriptor**. The key of the descriptor must be a string and cannot be converted into a number. | 11 |
| FUNC | napi\_create\_object\_with\_named\_properties | Creates a JS object using the given **napi\_value** and key. The key must be a string and cannot be converted into a number. | 11 |
| FUNC | napi\_coerce\_to\_native\_binding\_object | Forcibly binds a JS object and a native object. | 11 |
| FUNC | napi\_create\_ark\_runtime | Creates an ArkTS runtime environment. | 12 |
| FUNC | napi\_destroy\_ark\_runtime | Destroys the ArkTS runtime environment. | 12 |
| FUNC | napi\_run\_event\_loop | Runs the underlying event loop. | 12 |
| FUNC | napi\_stop\_event\_loop | Stops the underlying event loop. | 12 |
| FUNC | napi\_load\_module\_with\_info | Loads an .abc file as a module. This API returns the namespace of the module. It can be used in a newly created ArkTS runtime environment. | 12 |
| FUNC | napi\_serialize | Converts an ArkTS object into native data. | 12 |
| FUNC | napi\_deserialize | Converts native data into an ArkTS object. | 12 |
| FUNC | napi\_delete\_serialization\_data | Deletes serialized data. | 12 |
| FUNC | napi\_call\_threadsafe\_function\_with\_priority | Calls a task with the specified priority and enqueuing mode into the ArkTS main thread. | 12 |
| FUNC | napi\_is\_sendable | Checks whether the given JS value is sendable. | 12 |
| FUNC | napi\_define\_sendable\_class | Creates a sendable class. | 12 |
| FUNC | napi\_create\_sendable\_object\_with\_properties | Creates a sendable object with the given **napi\_property\_descriptor**. | 12 |
| FUNC | napi\_create\_sendable\_array | Creates a sendable array. | 12 |
| FUNC | napi\_create\_sendable\_array\_with\_length | Creates a sendable array of the specified length. | 12 |
| FUNC | napi\_create\_sendable\_arraybuffer | Creates a sendable **ArrayBuffer**. | 12 |
| FUNC | napi\_create\_sendable\_typedarray | Creates a sendable **TypedArray**. | 12 |
| FUNC | napi\_wrap\_sendable | Wraps a native instance into an ArkTS object. | 12 |
| FUNC | napi\_wrap\_sendable\_with\_size | Wraps a native instance into an ArkTS object with the specified size. | 12 |
| FUNC | napi\_unwrap\_sendable | Unwraps the native instance from an ArkTS object. | 12 |
| FUNC | napi\_remove\_wrap\_sendable | Removes and obtains the native instance wrapped by an ArkTS object. After removal, the callback will no longer be triggered and must be manually deleted to free memory. | 12 |
| FUNC | napi\_wrap\_enhance | Wraps a Node-API instance into an ArkTS object and specifies the instance size. You can specify whether to execute the registered callback asynchronously (if asynchronous, it must be thread-safe). | 18 |
| FUNC | napi\_create\_ark\_context | Creates a new runtime context environment. | 20 |
| FUNC | napi\_switch\_ark\_context | Switches to the specified runtime context environment. | 20 |
| FUNC | napi\_destroy\_ark\_context | Destroys a context environment created by **napi\_create\_ark\_context**. | 20 |
| FUNC | napi\_create\_strong\_sendable\_reference | Creates a Sendable strong reference to a Sendable ArkTS object. | 22 |
| FUNC | napi\_delete\_strong\_sendable\_reference | Deletes a Sendable strong reference. | 22 |
| FUNC | napi\_get\_strong\_sendable\_reference\_value | Obtains the ArkTS object value associated with a Sendable strong reference. | 22 |

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/28/v3/oJM-I0R4Rw2mDtRtKbUd5A/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062528Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=08769DDE83EB0E123766626E87F1F8976A1110EEAABF7CCAA214FBC6CB2F2F77)

For details about the sendable feature, see [Sendable Object Overview](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/arkts-sendable).

## napi\_qos\_t

typedef enum {
    napi\_qos\_background = 0,      // Low priority for works invisible to users, such as data synchronization and backup.
    napi\_qos\_utility = 1, // Medium priority for works that do not require immediate response, such as downloading or importing data.
    napi\_qos\_default = 2,  // Default priority.
    napi\_qos\_user\_initiated = 3, // High priority for user-triggered works with visible progress, for example, opening a file.
} napi\_qos\_t;

**Description**

Enumerates the QoS levels, which determine the priority of thread scheduling.

## napi\_event\_mode

typedef enum {
    napi\_event\_mode\_default = 0, // Run the underlying event loop while blocking the current thread, and exit the event loop only when there is no task in the loop.
    napi\_event\_mode\_nowait = 1, // Run the underlying event loop without blocking the current thread. Process a task and exit the event loop after the task is complete. If there is no task in the event loop, exit the event loop immediately.
} napi\_event\_mode;

**Description**

Enumerates the modes for running the underlying event loop.

## napi\_queue\_async\_work\_with\_qos

napi\_status napi\_queue\_async\_work\_with\_qos(napi\_env env,
                                           napi\_async\_work work,
                                           napi\_qos\_t qos);

**Description**

Adds an async work object to the queue so that it can be scheduled for execution based on the QoS priority passed in.

**Parameters**

-   **env**: environment, in which the API is invoked.
    
-   **work**: handle to the async work object to schedule. This object is created by **napi\_create\_async\_work**.
    
-   **qos**: priority of the task to schedule.
    

**Return value**

**napi\_ok** if the operation is successful.

## napi\_run\_script\_path

napi\_status napi\_run\_script\_path(napi\_env env,
                                 const char\* abcPath,
                                 napi\_value\* result);

**Description**

Runs an .abc file.

**Parameters**

-   **env**: environment, in which the API is invoked.
    
-   **abcPath**: JS path of the script to run. The value is a string that specifies the location of the script file to run.
    
-   **result**: pointer to **napi\_value**, which holds the script execution result.
    

**Return value**

**napi\_ok** if the operation is successful.

## napi\_load\_module

napi\_status napi\_load\_module(napi\_env env,
                             const char\* path,
                             napi\_value\* result);

**Description**

Loads a system module or a customized module. This API returns the namespace of the module loaded.

**Parameters**

-   **env**: environment, in which the API is invoked.
    
-   **path**: name of the system module to load or path of the customized module to load.
    
-   **result**: pointer to **napi\_value**, which holds the module loading result.
    

**Return value**

**napi\_ok** if the operation is successful.

## napi\_create\_object\_with\_properties

napi\_status napi\_create\_object\_with\_properties(napi\_env env,
                                               napi\_value\* result,
                                               size\_t property\_count,
                                               const napi\_property\_descriptor\* properties);

**Description**

Creates a JS object using the given **napi\_property\_descriptor**.

**napi\_property\_descriptor** defines a property, including the property attributes and the methods used to obtain and set the property. By passing **napi\_property\_descriptor**, you can define the properties when creating an object.

The key in **napi\_property\_descriptor** must be a string that cannot be converted into a number.

**Parameters**

-   **env**: environment, in which the API is invoked.
    
-   **result**: pointer to **napi\_value**, which holds the created object.
    
-   **property\_count**: number of properties to be added to the object.
    
-   **properties**: pointer to a **napi\_property\_descriptor** array containing information about the properties to be added to the object.
    

**Return value**

**napi\_ok** if the operation is successful.

## napi\_create\_object\_with\_named\_properties

napi\_status napi\_create\_object\_with\_named\_properties(napi\_env env,
                                                     napi\_value\* result,
                                                     size\_t property\_count,
                                                     const char\*\* keys,
                                                     const napi\_value\* values);

**Description**

Creates a JS object using the given **napi\_value**s and keys. The key must be a string and cannot be converted into a number.

**Parameters**

-   **env**: environment, in which the API is invoked.
    
-   **result**: pointer to **napi\_value**, which holds the created object.
    
-   **property\_count**: number of properties to be added to the object.
    
-   **keys**: pointer to a const char array containing the keys of the properties to add.
    
-   **values**: pointer to a **napi\_value** array containing the properties to add. The keys and properties are in one-to-one mapping.
    

**Return value**

**napi\_ok** if the operation is successful.

## napi\_coerce\_to\_native\_binding\_object

napi\_status napi\_coerce\_to\_native\_binding\_object(napi\_env env,
                                                 napi\_value js\_object,
                                                 napi\_native\_binding\_detach\_callback detach\_cb,
                                                 napi\_native\_binding\_attach\_callback attach\_cb,
                                                 void\* native\_object,
                                                 void\* hint);

**Description**

Converts a JS object into an object carrying native information by forcibly binding callbacks and callback data to the JS object.

**Parameters**

-   **env**: environment, in which the API is invoked.
    
-   **js\_object**: JS object to convert.
    
-   **detach\_cb**: callback to be invoked to perform cleanup operations when the object is detached during serialization.
    
-   **attach\_cb**: callback to be invoked when the object is attached during serialization.
    
-   **native\_object**: parameters to be passed to the callbacks. This object cannot be empty.
    
-   **hint**: pointer to the additional information to be passed to the callbacks.
    

**Return value**

**napi\_ok** if the operation is successful.

## napi\_create\_ark\_runtime

napi\_status napi\_create\_ark\_runtime(napi\_env \*env)

**Description**

Creates a runtime environment. A process allows up to 64 instances, and the total number of child threads, including those created by [Worker](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/worker-introduction), cannot exceed 80.

**Parameters**

-   **env**: environment, in which the API is invoked.

**Return value**

**napi\_ok** if the operation is successful.

## napi\_destroy\_ark\_runtime

napi\_status napi\_destroy\_ark\_runtime(napi\_env \*env)

**Description**

Destroys an ArkTS runtime environment.

**Parameters**

-   **env**: environment, in which the API is invoked.

**Return value**

**napi\_ok** if the operation is successful.

## napi\_run\_event\_loop

napi\_status napi\_run\_event\_loop(napi\_env env, napi\_event\_mode mode)

**Description**

Runs the underlying event loop.

**Parameters**

-   **env**: environment, in which the API is invoked.
-   **mode**: event mode for running the event loop.

**Return value**

**napi\_ok** if the operation is successful.

## napi\_stop\_event\_loop

napi\_status napi\_stop\_event\_loop(napi\_env env)

**Description**

Stops the underlying event loop.

**Parameters**

-   **env**: environment, in which the API is invoked.

**Return value**

**napi\_ok** if the operation is successful.

## napi\_load\_module\_with\_info

napi\_status napi\_load\_module\_with\_info(napi\_env env,
                                       const char\* path,
                                       const char\* module\_info,
                                       napi\_value\* result)

**Description**

Loads an .abc file as a module. This API returns the namespace of the module. It can be used in a newly created ArkTS runtime environment.

**Parameters**

-   **env**: environment, in which the API is invoked.
    
-   **path**: path of the module to load.
    
-   **module\_info**: module information. The value is a string containing module information. The module information contains detailed module information, such as the version, author, and related description.
    
-   **result**: pointer to **napi\_value**, which holds the module loading result.
    

**Return value**

**napi\_ok** if the operation is successful.

## napi\_serialize

napi\_status napi\_serialize(napi\_env env,
                           napi\_value object,
                           napi\_value transfer\_list,
                           napi\_value clone\_list,
                           void\*\* result)

**Description**

Converts an ArkTS object into native data.

**Parameters**

-   **env**: environment, in which the API is invoked.
    
-   **object**: JS object to be serialized.
    
-   **transfer\_list**: list of JS objects to be passed during serialization.
    
-   **clone\_list**: list of JS objects to be cloned during serialization.
    
-   **result**: pointer to the serialization result. After the call is complete, the pointer to the native data converted is stored in this position.
    

**Return value**

**napi\_ok** if the operation is successful.

## napi\_deserialize

napi\_status napi\_deserialize(napi\_env env, void\* buffer, napi\_value\* object)

**Description**

Converts native data into an ArkTS object.

**Parameters**

-   **env**: environment, in which the API is invoked.
    
-   **buffer**: pointer to the binary data, which needs to be deserialized into a JS object.
    
-   **object**: pointer to the deserialized JS object.
    

**Return value**

**napi\_ok** if the operation is successful.

## napi\_delete\_serialization\_data

napi\_status napi\_delete\_serialization\_data(napi\_env env, void\* buffer)

**Description**

Deletes serialized data.

**Parameters**

-   **env**: environment, in which the API is invoked.
    
-   **buffer**: pointer to the buffer that contains the serialized data to delete. If the serialized data is no longer required, you can use this API to delete the data and release the memory occupied.
    

**Return value**

**napi\_ok** if the operation is successful.

## napi\_call\_threadsafe\_function\_with\_priority

napi\_status napi\_call\_threadsafe\_function\_with\_priority(napi\_threadsafe\_function func,
                                                        void \*data,
                                                        napi\_task\_priority priority,
                                                        bool isTail)

**Description**

Calls a task with the specified priority and enqueuing mode into the ArkTS main thread.

**Parameters**

-   **func**: thread-safe function object, which is returned when a thread-safe function is created.
    
-   **data**: pointer to the data to be passed to the JS callback function.
    
-   **priority**: priority of the task that calls the JS callback function.
    
-   **isTail**: whether the task is added to the tail of the task queue. If the value is **true**, the task will be added to the tail of the event loop. If it is **false**, the task will be executed immediately.
    

**Return value**

**napi\_ok** if the operation is successful.

## napi\_is\_sendable

napi\_status napi\_is\_sendable(napi\_env env, napi\_value value, bool\* result)

**Description**

Checks whether the given JS value is sendable.

**Parameters**

-   **env**: environment, in which the API is invoked.
    
-   **value**: JS value to check.
    
-   **result**: pointer of the bool type, indicating whether the JS value is sendable.
    

**Return value**

**napi\_ok** if the operation is successful.

## napi\_define\_sendable\_class

napi\_status napi\_define\_sendable\_class(napi\_env env,
                                       const char\* utf8name,
                                       size\_t length,
                                       napi\_callback constructor,
                                       void\* data,
                                       size\_t property\_count,
                                       const napi\_property\_descriptor\* properties,
                                       napi\_value parent,
                                       napi\_value\* result)

**Description**

Creates a sendable class.

**Parameters**

-   **env**: environment, in which the API is invoked.
    
-   **utf8name**: pointer to the name of the class to create. This parameter is of the const char\* type.
    
-   **length**: length of the class name, in bytes. This parameter is of the size\_t type.
    
-   **constructor**: constructor of the class. This parameter is of the napi\_callback type.
    
-   **data**: (optional) pointer to the additional data of the constructor. This parameter is of the void\* type.
    
-   **property\_count**: number of properties of the class. This parameter is of the size\_t type.
    
-   **properties**: (optional) pointer to the descriptors of the properties. This parameter of the const napi\_property\_descriptor\* type.
    
-   **parent**: (optional) parent class of the class to create. This parameter is of the napi\_value type.
    
-   **result**: pointer to the sendable class created. This parameter is of the napi\_value type.
    

**Return value**

**napi\_ok** if the operation is successful.

## napi\_create\_sendable\_object\_with\_properties

napi\_status napi\_create\_sendable\_object\_with\_properties(napi\_env env,
                                                        size\_t property\_count,
                                                        const napi\_property\_descriptor\* properties,
                                                        napi\_value\* result)

**Description**

Creates a sendable object with the given **napi\_property\_descriptor**.

**Parameters**

-   **env**: environment, in which the API is invoked.
    
-   **property\_count**: number of properties of the class. This parameter is of the size\_t type.
    
-   **properties**: pointer to the descriptors of the properties. This parameter of the const napi\_property\_descriptor\* type.
    
-   **result**: pointer to the sendable class created. This parameter is of the napi\_value type.
    

**Return value**

**napi\_ok** if the operation is successful.

## napi\_create\_sendable\_array

napi\_status napi\_create\_sendable\_array(napi\_env env, napi\_value\* result)

**Description**

Creates a sendable array.

**Parameters**

-   **env**: environment, in which the API is invoked.
    
-   **result**: pointer to the sendable array created. This parameter is of the napi\_value type.
    

**Return value**

**napi\_ok** if the operation is successful.

## napi\_create\_sendable\_array\_with\_length

napi\_status napi\_create\_sendable\_array\_with\_length(napi\_env env, size\_t length, napi\_value\* result)

**Description**

Creates a sendable array of the specified length.

**Parameters**

-   **env**: environment, in which the API is invoked.
    
-   **length**: length of the sendable array to create.
    
-   **result**: pointer to the sendable array created. This parameter is of the napi\_value type.
    

**Return value**

**napi\_ok** if the operation is successful.

## napi\_create\_sendable\_arraybuffer

napi\_status napi\_create\_sendable\_arraybuffer(napi\_env env, size\_t byte\_length, void\*\* data, napi\_value\* result)

**Description**

Creates a sendable **ArrayBuffer**.

**Parameters**

-   **env**: environment, in which the API is invoked.
    
-   **byte\_length**: length of the ArrayBuffer to create.
    
-   **data**: pointer to the byte buffer for storing the ArrayBuffer created.
    
-   **result**: pointer to the ArrayBuffer created. This parameter is of the napi\_value type.
    

**Return value**

**napi\_ok** if the operation is successful.

## napi\_create\_sendable\_typedarray

napi\_status napi\_create\_sendable\_typedarray(napi\_env env,
                                            napi\_typedarray\_type type,
                                            size\_t length,
                                            napi\_value arraybuffer,
                                            size\_t byte\_offset,
                                            napi\_value\* result);

**Description**

Creates a sendable **TypedArray**.

**Parameters**

-   **env**: environment, in which the API is invoked.
    
-   **type**: type of the TypedArray to create.
    
-   **length**: length of the TypedArray to create.
    
-   **arraybuffer**: ArrayBuffer instance to create.
    
-   **byte\_offset**: offset of the ArrayBuffer.
    
-   **result**: pointer to the TypedArray created. This parameter is of the napi\_value type.
    

**Return value**

**napi\_ok** if the operation is successful.

## napi\_wrap\_sendable

napi\_status napi\_wrap\_sendable(napi\_env env,
                               napi\_value js\_object,
                               void\* native\_object,
                               napi\_finalize finalize\_cb,
                               void\* finalize\_hint);

**Description**

Wraps a native instance into an ArkTS object.

**Parameters**

-   **env**: environment, in which the API is invoked.
    
-   **js\_object**: ArkTS object.
    
-   **native\_object**: pointer to the native instance to be wrapped in the ArkTS object.
    
-   **napi\_finalize**: (optional) callback to be invoked when the ArkTS object is destroyed.
    
-   **finalize\_hint**: (optional) pointer to the callback context, which will be passed to the callback.
    

**Return value**

**napi\_ok** if the operation is successful.

## napi\_wrap\_sendable\_with\_size

napi\_status napi\_wrap\_sendable\_with\_size(napi\_env env,
                                         napi\_value js\_object,
                                         void\* native\_object,
                                         napi\_finalize finalize\_cb,
                                         void\* finalize\_hint,
                                         size\_t native\_binding\_size);

**Description**

Wraps a native instance into an ArkTS object with the specified size.

**Parameters**

-   **env**: environment, in which the API is invoked.
    
-   **js\_object**: ArkTS object.
    
-   **native\_object**: pointer to the native instance to be wrapped in the ArkTS object.
    
-   **napi\_finalize**: (optional) callback to be invoked when the ArkTS object is destroyed.
    
-   **finalize\_hint**: (optional) pointer to the callback context, which will be passed to the callback.
    
-   **native\_binding\_size**: (optional) size of the native instance wrapped.
    

**Return value**

**napi\_ok** if the operation is successful.

## napi\_unwrap\_sendable

napi\_status napi\_unwrap\_sendable(napi\_env env, napi\_value js\_object, void\*\* result)

**Description**

Unwraps the native instance from an ArkTS object.

**Parameters**

-   **env**: environment, in which the API is invoked.
    
-   **js\_object**: ArkTS object.
    
-   **result**: double pointer to the native instance unwrapped.
    

**Return value**

**napi\_ok** if the operation is successful.

## napi\_remove\_wrap\_sendable

napi\_status napi\_remove\_wrap\_sendable(napi\_env env, napi\_value js\_object, void\*\* result)

**Description**

Removes and obtains the native instance wrapped by an ArkTS object. After removal, the callback will no longer be triggered and must be manually deleted to free memory.

**Parameters**

-   **env**: environment, in which the API is invoked.
    
-   **js\_object**: ArkTS object.
    
-   **result**: double pointer to the native instance unwrapped.
    

**Return value**

**napi\_ok** if the operation is successful.

## napi\_wrap\_enhance

napi\_status napi\_wrap\_enhance(napi\_env env,
                              napi\_value js\_object,
                              void\* native\_object,
                              napi\_finalize finalize\_cb,
                              bool async\_finalizer,
                              void\* finalize\_hint,
                              size\_t native\_binding\_size,
                              napi\_ref\* result);

**Description**

Wraps a Node-API instance into an ArkTS object and specifies the instance size. You can specify whether to execute the registered callback asynchronously (if asynchronous, it must be thread-safe).

**Parameters**

-   **env**: environment, in which the API is invoked.
    
-   **js\_object**: ArkTS object.
    
-   **native\_object**: pointer to the native instance to be wrapped in the ArkTS object.
    
-   **finalize\_cb**: (optional) callback to be called when the ArkTS object is destroyed. For details, see [napi\_finalize](#napi_finalize-description).
    
-   **async\_finalizer**: a Boolean value used to indicate whether to execute the **finalize\_cb** callback asynchronously. The value **true** means to execute the callback asynchronously. In this case, thread safety must be ensured. The value **false** means to execute the callback synchronously.
    
-   **finalize\_hint**: (optional) pointer to the callback context, which will be passed to the callback.
    
-   **native\_binding\_size**: (optional) size of the native instance wrapped.
    
-   **result**: (optional) pointer to the ArkTS object reference.
    

**Return value**

-   **napi\_ok**: The operation is successful.
    
-   **napi\_invalid\_arg**: The **env**, **js\_object**, or **native\_object** parameter is null.
    
-   **napi\_object\_expected**: The **js\_object** parameter is not an ArkTs object or function.
    
-   **napi\_pending\_exception**: An uncaught exception or an exception occurs during the execution.
    

## napi\_create\_ark\_context

napi\_status napi\_create\_ark\_context(napi\_env env, napi\_env\* newEnv);

**Description**

Creates a new runtime context environment.

Note the following when using this API:

1.  Only new context environments created through the initial context environment are supported. It is prohibited to create new context environments using the context environment created by this API.
2.  Currently, this API cannot be called on ArkTS threads that are not the main thread.
3.  Before calling this API, ensure that the current context environment is normal. Otherwise, the API call fails.
4.  The context environment created by this API can only load some native.so files of ArkUI. Loading application-specific native .so files and common basic library native so files is not supported.
5.  The multi-context runtime environment does not support the sendable feature.
6.  The runtime context environment created through **napi\_create\_ark\_context** does not support module capabilities such as console and timer.

**Parameters**

-   **env**: environment, in which the API is invoked.
    
-   newEnv: pointer to the new runtime context environment.
    

**Return value**

**napi\_ok** if the operation is successful.

## napi\_switch\_ark\_context

napi\_status napi\_switch\_ark\_context(napi\_env env)

**Description**

Switches to the specified runtime context environment. Note the following when using this API:

1.  Currently, this API does not support calls in ArkTS threads that are not the main thread.
2.  Before calling this API, ensure that the current context environment is normal. Otherwise, the API call fails.

**Parameters**

-   env: specified runtime context environment.

**Return value**

**napi\_ok** if the operation is successful.

## napi\_destroy\_ark\_context

napi\_status napi\_destroy\_ark\_context(napi\_env env)

**Description**

Destroys a context environment created by **napi\_create\_ark\_context**. Note the following when using this API:

1.  Currently, this API does not support calls in ArkTS threads that are not the main thread.
2.  This API can only be used to destroy runtime context environments created by calling **napi\_create\_ark\_context**.
3.  You cannot use this API to destroy a context environment that is currently in use.

**Parameters**

-   env: runtime context to be destroyed.

**Return value**

**napi\_ok** if the operation is successful.

## **napi\_finalize** Description

typedef void (\*napi\_finalize)(napi\_env env,
                              void\* finalize\_data,
                              void\* finalize\_hint);

**Description**

Called when the lifecycle of a Node-API object ends.

**Parameters**

-   **env**: environment, in which the API is invoked.
    
-   **finalize\_data**: pointer to the user data to be cleared.
    
-   **finalize\_hint**: context hint, which is used to assist the clear process.
    

**Return value**

-   **void**: no return value.

## napi\_create\_strong\_sendable\_reference

napi\_status napi\_create\_strong\_sendable\_reference(napi\_env env,
                                                  napi\_value value,
                                                  napi\_sendable\_ref\* result);

**Description**

Creates a Sendable strong reference to a Sendable ArkTS object. Note the following when using this API:

1.  **napi\_sendable\_ref** can be created only for [Sendable objects](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/arkts-sendable#sendable-data-types).
2.  **napi\_sendable\_ref** can be used across ArkTS threads. When performing multithreaded operations, the caller must manage the release timing to avoid issues related to using after release.
3.  Within the same process, a maximum of 51200 **napi\_sendable\_ref** instances can coexist.

**Parameters**

-   **env**: environment, in which the API is invoked.
-   **value**: Sendable ArkTS object to be referenced.
-   **result**: created Sendable strong reference.

**Return value**

**napi\_ok** if the operation is successful.

## napi\_delete\_strong\_sendable\_reference

napi\_status napi\_delete\_strong\_sendable\_reference(napi\_env env, napi\_sendable\_ref ref);

**Description**

Deletes a Sendable strong reference. Note the following when using this API:

1.  Do not forcibly cast other reference types (such as **napi\_ref** or **napi\_strong\_ref**) to **napi\_sendable\_ref** for use with this API. **napi\_delete\_strong\_sendable\_reference** accepts only **napi\_sendable\_ref** created by calling **napi\_create\_strong\_sendable\_reference**.

**Parameters**

-   **env**: environment, in which the API is invoked.
-   **ref**: reference to be deleted.

**Return value**

**napi\_ok** if the operation is successful.

## napi\_get\_strong\_sendable\_reference\_value

napi\_status napi\_get\_strong\_sendable\_reference\_value(napi\_env env,
                                                     napi\_sendable\_ref ref,
                                                     napi\_value\* result);

**Description**

Obtains the ArkTS object value associated with a Sendable strong reference. Note the following when using this API:

1.  Do not forcibly cast other reference types (such as **napi\_ref** or **napi\_strong\_ref**) to **napi\_sendable\_ref** for use with this API. **napi\_get\_strong\_sendable\_reference\_value** accepts only **napi\_sendable\_ref** created by calling **napi\_create\_strong\_sendable\_reference**.

**Parameters**

-   **env**: environment, in which the API is invoked.
-   **ref**: Sendable strong reference.
-   **result**: Sendable ArkTS object obtained from **ref**.

**Return value**

**napi\_ok** if the operation is successful.
