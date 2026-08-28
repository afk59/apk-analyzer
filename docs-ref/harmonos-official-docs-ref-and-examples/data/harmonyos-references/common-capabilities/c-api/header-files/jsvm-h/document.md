# jsvm.h

#### Overview

Defines JSVM-APIs. These APIs are used to provide independent, standard, and complete JS engine capabilities, including managing the engine lifecycle, compiling and running JS code, implementing JS/C++ cross-language calls, and taking snapshots.

**Reference file**: <ark\_runtime/jsvm.h>

**Library**: libjsvm.so

**System capability**: SystemCapability.ArkCompiler.JSVM

**Since**: 11

**Related module**: [JSVM](../../modules/jsvm/document.md)

#### Summary

#### \[h2\]Macros

| Name | Description |
| :-- | :-- |
| **JSVM\_VERSION\_EXPERIMENTAL** 2147483647 | Defines the experimental JSVM version number. |
| **JSVM\_VERSION** 8 | Defines the JSVM version number. |
| **JSVM\_EXTERN **attribute****((visibility("default"))) | Defines the symbol that is externally visible. |
| **JSVM\_AUTO\_LENGTH** SIZE\_MAX | Defines the automatic length. |
| **EXTERN\_C\_START** | 
Defines the segment start identifier for a compiler to compile the following code segment as C code.

When **\_\_cplusplus** detects that a C++ compiler is being used, the value **"extern "C" {"** is assigned to **EXTERN\_C\_START**, indicating that the subsequent code is C code. If a C++ compiler is not being used, no tag is required.

 |
| **EXTERN\_C\_END** | 

Defines the segment end identifier for a compiler to compile the following code segment as C code.

When **\_\_cplusplus** detects that a C++ compiler is being used, the value **"}"** is assigned to **EXTERN\_C\_START**, indicating that the C code ends here. If a C++ compiler is not being used, no tag is required.

 |

#### \[h2\]Functions

| Name | Description |
| :-- | :-- |
| [JSVM\_EXTERN JSVM\_Status OH\_JSVM\_Init(const JSVM\_InitOptions\* options)](#oh_jsvm_init) | Initializes a JavaScript VM. |
| [JSVM\_EXTERN JSVM\_Status OH\_JSVM\_CreateVM(const JSVM\_CreateVMOptions\* options,JSVM\_VM\* result)](#oh_jsvm_createvm) | Creates a VM instance. |
| [JSVM\_EXTERN JSVM\_Status OH\_JSVM\_SetMicrotaskPolicy(JSVM\_VM vm,JSVM\_MicrotaskPolicy policy)](#oh_jsvm_setmicrotaskpolicy) | Sets the microtask execution policy for a VM instance. If this method is not called, the default policy **JSVM\_MicrotaskPolicy::JSVM\_MICROTASK\_AUTO** is used. |
| [JSVM\_EXTERN JSVM\_Status OH\_JSVM\_DestroyVM(JSVM\_VM vm)](#oh_jsvm_destroyvm) | Destroys a VM instance. |
| [JSVM\_EXTERN JSVM\_Status OH\_JSVM\_CreateProxy(JSVM\_Env env,JSVM\_Value target,JSVM\_Value handler,JSVM\_Value\* result)](#oh_jsvm_createproxy) | Creates a JavaScript proxy. This API is equivalent to calling **new Proxy(target, handler)** in JS. |
| [JSVM\_EXTERN JSVM\_Status OH\_JSVM\_IsProxy(JSVM\_Env env,JSVM\_Value value,bool\* isProxy)](#oh_jsvm_isproxy) | Checks whether the input value is a JavaScript proxy. |
| [JSVM\_EXTERN JSVM\_Status OH\_JSVM\_ProxyGetTarget(JSVM\_Env env,JSVM\_Value value,JSVM\_Value\* result)](#oh_jsvm_proxygettarget) | Obtains the target object in the JavaScript Proxy. |
| [JSVM\_EXTERN JSVM\_Status OH\_JSVM\_OpenVMScope(JSVM\_VM vm,JSVM\_VMScope\* result)](#oh_jsvm_openvmscope) | Opens a new VM scope for a VM instance. |
| [JSVM\_EXTERN JSVM\_Status OH\_JSVM\_CloseVMScope(JSVM\_VM vm,JSVM\_VMScope scope)](#oh_jsvm_closevmscope) | Closes the VM scope of a VM instance. |
| [JSVM\_EXTERN JSVM\_Status OH\_JSVM\_CreateEnv(JSVM\_VM vm,size\_t propertyCount,const JSVM\_PropertyDescriptor\* properties,JSVM\_Env\* result)](#oh_jsvm_createenv) | Creates a new environment based on the optional properties of the new context. |
| [JSVM\_EXTERN JSVM\_Status OH\_JSVM\_CreateEnvFromSnapshot(JSVM\_VM vm,size\_t index,JSVM\_Env\* result)](#oh_jsvm_createenvfromsnapshot) | Creates a new environment based on the startup snapshot of the VM. |
| [JSVM\_EXTERN JSVM\_Status OH\_JSVM\_DestroyEnv(JSVM\_Env env)](#oh_jsvm_destroyenv) | Destroys the environment. |
| [JSVM\_EXTERN JSVM\_Status OH\_JSVM\_OpenEnvScope(JSVM\_Env env,JSVM\_EnvScope\* result)](#oh_jsvm_openenvscope) | Opens a new environment scope. |
| [JSVM\_EXTERN JSVM\_Status OH\_JSVM\_CloseEnvScope(JSVM\_Env env,JSVM\_EnvScope scope)](#oh_jsvm_closeenvscope) | Closes the environment scope. |
| [JSVM\_EXTERN JSVM\_Status OH\_JSVM\_GetVM(JSVM\_Env env,JSVM\_VM\* result)](#oh_jsvm_getvm) | Obtains a VM instance. |
| [JSVM\_EXTERN JSVM\_Status OH\_JSVM\_CompileScript(JSVM\_Env env,JSVM\_Value script,const uint8\_t\* cachedData,size\_t cacheDataLength,bool eagerCompile,bool\* cacheRejected,JSVM\_Script\* result)](#oh_jsvm_compilescript) | Compiles a JavaScript code snippet and returns the compiled script. |
| [JSVM\_EXTERN JSVM\_Status OH\_JSVM\_CompileScriptWithOrigin(JSVM\_Env env,JSVM\_Value script,const uint8\_t\* cachedData,size\_t cacheDataLength,bool eagerCompile,bool\* cacheRejected,JSVM\_ScriptOrigin\* origin,JSVM\_Script\* result)](#oh_jsvm_compilescriptwithorigin) | Compiles a JavaScript code snippet that contains source map information and returns the compiled script. |
| [JSVM\_EXTERN JSVM\_Status OH\_JSVM\_CompileScriptWithOptions(JSVM\_Env env,JSVM\_Value script,size\_t optionCount,JSVM\_CompileOptions options\[\],JSVM\_Script\* result)](#oh_jsvm_compilescriptwithoptions) | Compiles a JavaScript code snippet and returns the compiled script. |
| [JSVM\_EXTERN JSVM\_Status OH\_JSVM\_CreateCodeCache(JSVM\_Env env,JSVM\_Script script,const uint8\_t\*\* data,size\_t\* length)](#oh_jsvm_createcodecache) | Creates a code cache for the compiled script. |
| [JSVM\_EXTERN JSVM\_Status OH\_JSVM\_RunScript(JSVM\_Env env,JSVM\_Script script,JSVM\_Value\* result)](#oh_jsvm_runscript) | Runs a JavaScript code snippet and returns its result, including the following precautions: Unlike eval, this function does not allow the script to access the current lexical scope, and therefore does not allow the script to access the module scope. This means that pseudo-global variables such as **require** will be unavailable. The script can access the global scope. The functions and variable declarations in the script will be added to the global object. Variable declarations using **let** and **const** are globally visible, but are not added to the global object. The value of **this** is **global** in the script. Without the JIT permission, the script containing WebAssembly fails to be executed. The performance varies in specific scenarios, and a log is printed to notify you. |
| [JSVM\_EXTERN JSVM\_Status OH\_JSVM\_SetInstanceData(JSVM\_Env env,void\* data,JSVM\_Finalize finalizeCb,void\* finalizeHint)](#oh_jsvm_setinstancedata) | Sets instance data so that it is associated with the currently running JSVM environment. You can use **OH\_JSVM\_GetInstanceData()** to obtain data later. Any existing data set by a previous call to **OH\_JSVM\_SetInstanceData()** will be overwritten. If **finalizeCb** was previously provided, it will not be called. |
| [JSVM\_EXTERN JSVM\_Status OH\_JSVM\_GetInstanceData(JSVM\_Env env,void\*\* data)](#oh_jsvm_getinstancedata) | Obtains instance data that has been set by **OH\_JSVM\_SetInstanceData()**. If no associated data is set, this function is called successfully and **data** is set to **NULL**. |
| [JSVM\_EXTERN JSVM\_Status OH\_JSVM\_GetLastErrorInfo(JSVM\_Env env,const JSVM\_ExtendedErrorInfo\*\* result)](#oh_jsvm_getlasterrorinfo) | Obtains the **JSVM\_ExtendedErrorInfo** struct that contains the last error. The content of **JSVM\_ExtendedErrorInfo** returned is valid only before the JSVM-API function is called for the same environment. This includes a call to **OH\_JSVM\_IsExceptionPending**, so you may need to copy information for later use. The pointer returned in **error\_message** points to a statically defined string, so if you copy it from the **error\_message** field (which will be overwritten) before calling another JSVM-API function, you can safely use the pointer. |
| [JSVM\_EXTERN JSVM\_Status OH\_JSVM\_Throw(JSVM\_Env env,JSVM\_Value error)](#oh_jsvm_throw) | Throws the provided JavaScript value. |
| [JSVM\_EXTERN JSVM\_Status OH\_JSVM\_ThrowError(JSVM\_Env env,const char\* code,const char\* msg)](#oh_jsvm_throwerror) | Throws a JavaScript Error with the provided text. |
| [JSVM\_EXTERN JSVM\_Status OH\_JSVM\_ThrowTypeError(JSVM\_Env env,const char\* code,const char\* msg)](#oh_jsvm_throwtypeerror) | Throws a JavaScript TypeError with the provided text. |
| [JSVM\_EXTERN JSVM\_Status OH\_JSVM\_ThrowRangeError(JSVM\_Env env,const char\* code,const char\* msg)](#oh_jsvm_throwrangeerror) | Throws a JavaScript RangeError with the provided text. |
| [JSVM\_EXTERN JSVM\_Status OH\_JSVM\_ThrowSyntaxError(JSVM\_Env env,const char\* code,const char\* msg)](#oh_jsvm_throwsyntaxerror) | Throws a JavaScript SyntaxError with the provided text. |
| [JSVM\_EXTERN JSVM\_Status OH\_JSVM\_IsError(JSVM\_Env env,JSVM\_Value value,bool\* result)](#oh_jsvm_iserror) | Checks whether the given **JSVM\_Value** indicates an error. |
| [JSVM\_EXTERN JSVM\_Status OH\_JSVM\_CreateError(JSVM\_Env env,JSVM\_Value code,JSVM\_Value msg,JSVM\_Value\* result)](#oh_jsvm_createerror) | Creates a JavaScript Error with the provided text. |
| [JSVM\_EXTERN JSVM\_Status OH\_JSVM\_CreateTypeError(JSVM\_Env env,JSVM\_Value code,JSVM\_Value msg,JSVM\_Value\* result)](#oh_jsvm_createtypeerror) | Creates a JavaScript TypeError with the provided text. |
| [JSVM\_EXTERN JSVM\_Status OH\_JSVM\_CreateRangeError(JSVM\_Env env,JSVM\_Value code,JSVM\_Value msg,JSVM\_Value\* result)](#oh_jsvm_createrangeerror) | Creates a JavaScript RangeError with the provided text. |
| [JSVM\_EXTERN JSVM\_Status OH\_JSVM\_CreateSyntaxError(JSVM\_Env env,JSVM\_Value code,JSVM\_Value msg,JSVM\_Value\* result)](#oh_jsvm_createsyntaxerror) | Creates a JavaScript SyntaxError with the provided text. |
| [JSVM\_EXTERN JSVM\_Status OH\_JSVM\_GetAndClearLastException(JSVM\_Env env,JSVM\_Value\* result)](#oh_jsvm_getandclearlastexception) | Obtains and clears the last exception. If pending occurs, a JavaScript exception is returned. Otherwise, **NULL** is returned. |
| [JSVM\_EXTERN JSVM\_Status OH\_JSVM\_IsExceptionPending(JSVM\_Env env,bool\* result)](#oh_jsvm_isexceptionpending) | Checks whether the last exception is caused by pending. If yes, **true** is returned. Otherwise, **false** is returned. |
| [JSVM\_EXTERN JSVM\_Status OH\_JSVM\_OpenHandleScope(JSVM\_Env env,JSVM\_HandleScope\* result)](#oh_jsvm_openhandlescope) | Opens a new handle scope. |
| [JSVM\_EXTERN JSVM\_Status OH\_JSVM\_CloseHandleScope(JSVM\_Env env,JSVM\_HandleScope scope)](#oh_jsvm_closehandlescope) | (Mandatory) Closes the handle scope in the reverse order of opening it. |
| [JSVM\_EXTERN JSVM\_Status OH\_JSVM\_OpenEscapableHandleScope(JSVM\_Env env,JSVM\_EscapableHandleScope\* result)](#oh_jsvm_openescapablehandlescope) | Opens an escapable handle scope. |
| [JSVM\_EXTERN JSVM\_Status OH\_JSVM\_CloseEscapableHandleScope(JSVM\_Env env,JSVM\_EscapableHandleScope scope)](#oh_jsvm_closeescapablehandlescope) | (Mandatory) Closes the escapable handle scope in the reverse order of opening it. This JSVM\_API can be called even if there is a pending JavaScript exception. |
| [JSVM\_EXTERN JSVM\_Status OH\_JSVM\_EscapeHandle(JSVM\_Env env,JSVM\_EscapableHandleScope scope,JSVM\_Value escapee,JSVM\_Value\* result)](#oh_jsvm_escapehandle) | Escapes a handle of a JavaScript object so that it is valid through the lifecycle of the outer scope. Each scope can be called only once. If it is called for multiple times, an error is returned. |
| [JSVM\_EXTERN JSVM\_Status OH\_JSVM\_CreateReference(JSVM\_Env env,JSVM\_Value value,uint32\_t initialRefcount,JSVM\_Ref\* result)](#oh_jsvm_createreference) | Creates a reference with the specified reference count for the input value. |
| [JSVM\_EXTERN JSVM\_Status OH\_JSVM\_DeleteReference(JSVM\_Env env,JSVM\_Ref ref)](#oh_jsvm_deletereference) | Deletes the input reference. |
| [JSVM\_EXTERN JSVM\_Status OH\_JSVM\_ReferenceRef(JSVM\_Env env,JSVM\_Ref ref,uint32\_t\* result)](#oh_jsvm_referenceref) | Increases the reference count and returns the new reference count. |
| [JSVM\_EXTERN JSVM\_Status OH\_JSVM\_ReferenceUnref(JSVM\_Env env,JSVM\_Ref ref,uint32\_t\* result)](#oh_jsvm_referenceunref) | Decreases the reference count and returns the new reference count. |
| [JSVM\_EXTERN JSVM\_Status OH\_JSVM\_GetReferenceValue(JSVM\_Env env,JSVM\_Ref ref,JSVM\_Value\* result)](#oh_jsvm_getreferencevalue) | Obtains the **JSVM\_Value** returned by the JSVM-API, which is the JavaScript value associated with **JSVM\_Ref**. If the value is invalid, **NULL** is returned. |
| [JSVM\_EXTERN JSVM\_Status OH\_JSVM\_CreateArray(JSVM\_Env env,JSVM\_Value\* result)](#oh_jsvm_createarray) | Creates an array. This API returns the JSVM-API value of the JavaScript Array type. |
| [JSVM\_EXTERN JSVM\_Status OH\_JSVM\_CreateArrayWithLength(JSVM\_Env env,size\_t length,JSVM\_Value\* result)](#oh_jsvm_createarraywithlength) | Creates an array with a specified length. This API returns the JSVM-API value of the JavaScript Array type. The **length** property of the array is set to the input **length** parameter. However, there is no guarantee that the underlying buffer is pre-allocated by the VM when the array is created. This behavior is implemented by the underlying VM. |
| [JSVM\_EXTERN JSVM\_Status OH\_JSVM\_CreateArraybuffer(JSVM\_Env env,size\_t byteLength,void\*\* data,JSVM\_Value\* result)](#oh_jsvm_createarraybuffer) | Creates an array buffer. This API returns the JSVM-API value of the JavaScript ArrayBuffer type. ArrayBuffer is used to represent a fixed-length binary data buffer. It is usually used as the backup buffer of the **TypedArray** object. The allocated ArrayBuffer has an underlying byte buffer whose size is determined by the **length** parameter. The underlying buffer can be returned to and operated by the caller. This buffer can only be written directly from the native code. To write data from JavaScript to this buffer, you need to create a **TypedArray** or **DataView** object. |
| [JSVM\_EXTERN JSVM\_Status OH\_JSVM\_AllocateArrayBufferBackingStoreData(size\_t byteLength,JSVM\_InitializedFlag initialized,void \*\*data)](#oh_jsvm_allocatearraybufferbackingstoredata) | Allocates a segment of BackingStore memory to the array buffer. |
| [JSVM\_EXTERN JSVM\_Status OH\_JSVM\_FreeArrayBufferBackingStoreData(void \*data)](#oh_jsvm_freearraybufferbackingstoredata) | Frees the BackingStore memory allocated by **OH\_JSVM\_AllocateArrayBufferBackingStoreData**. |
| [JSVM\_EXTERN JSVM\_Status OH\_JSVM\_CreateArrayBufferFromBackingStoreData(JSVM\_Env env,void \*data,size\_t backingStoreSize,size\_t offset,size\_t arrayBufferSize,JSVM\_Value \*result)](#oh_jsvm_createarraybufferfrombackingstoredata) | Creates an array buffer in the allocated BackingStore memory. |
| [JSVM\_EXTERN JSVM\_Status OH\_JSVM\_CreateDate(JSVM\_Env env,double time,JSVM\_Value\* result)](#oh_jsvm_createdate) | Creates a date. This API ignores leap seconds because ECMAScript complies with the POSIX time specifications. |
| [JSVM\_EXTERN JSVM\_Status OH\_JSVM\_CreateExternal(JSVM\_Env env,void\* data,JSVM\_Finalize finalizeCb,void\* finalizeHint,JSVM\_Value\* result)](#oh_jsvm_createexternal) | Creates a JavaScript value with external data. This is used to pass external data through JavaScript code. You can use **OH\_JSVM\_GetValueExternal** to retrieve the value from the native code. This API adds a **JSVM\_Finalize** callback, which will be called when the newly created JavaScript object is garbage-collected. The created value is not an object, so it does not support additional properties. It is considered as a unique value type: Calling **OH\_JSVM\_Typeof()** with an external value generates **JSVM\_EXTERNAL**. |
| [JSVM\_EXTERN JSVM\_Status OH\_JSVM\_CreateObject(JSVM\_Env env,JSVM\_Value\* result)](#oh_jsvm_createobject) | Creates a default JavaScript object. This function is equivalent to executing **new Object()** in JavaScript. |
| [JSVM\_EXTERN JSVM\_Status OH\_JSVM\_CreateSymbol(JSVM\_Env env,JSVM\_Value description,JSVM\_Value\* result)](#oh_jsvm_createsymbol) | Creates a JavaScript symbol value with a UTF-8-encoded C string. |
| [JSVM\_EXTERN JSVM\_Status OH\_JSVM\_SymbolFor(JSVM\_Env env,const char\* utf8description,size\_t length,JSVM\_Value\* result)](#oh_jsvm_symbolfor) | Searches the global registry for an existing symbol with the given description. This API returns the symbol if it already exists; otherwise, a symbol is created in the registry. |
| [JSVM\_EXTERN JSVM\_Status OH\_JSVM\_CreateTypedarray(JSVM\_Env env,JSVM\_TypedarrayType type,size\_t length,JSVM\_Value arraybuffer,size\_t byteOffset,JSVM\_Value\* result)](#oh_jsvm_createtypedarray) | Creates a JavaScript **TypedArray** object based on an existing **ArrayBuffer** object. The **TypedArray** object provides an array-like view on the underlying data buffer, where each element has the same underlying binary scalar data type. The value of "**length** × element scalar bytes + **byteOffset**" must not be greater than the value of **ByteLength()** of the input array. Otherwise, a range error is thrown. |
| [JSVM\_EXTERN JSVM\_Status OH\_JSVM\_CreateDataview(JSVM\_Env env,size\_t length,JSVM\_Value arraybuffer,size\_t byteOffset,JSVM\_Value\* result)](#oh_jsvm_createdataview) | Creates a JavaScript **DataView** object based on an existing **ArrayBuffer** object. The **DataView** object provides an array-like view on the underlying data buffer, where elements can have different sizes and types. The sum of the binary length and byte offset cannot be greater than the size (in bytes) of the input array. Otherwise, a range error is thrown. |
| [JSVM\_EXTERN JSVM\_Status OH\_JSVM\_CreateInt32(JSVM\_Env env,int32\_t value,JSVM\_Value\* result)](#oh_jsvm_createint32) | Converts a value of the C int32\_t type to a value of the JavaScript number type. |
| [JSVM\_EXTERN JSVM\_Status OH\_JSVM\_CreateUint32(JSVM\_Env env,uint32\_t value,JSVM\_Value\* result)](#oh_jsvm_createuint32) | Converts a value of the C uint32\_t type to a value of the JavaScript number type. |
| [JSVM\_EXTERN JSVM\_Status OH\_JSVM\_CreateInt64(JSVM\_Env env,int64\_t value,JSVM\_Value\* result)](#oh_jsvm_createint64) | Converts a value of the C int64\_t type to a value of the JavaScript number type. |
| [JSVM\_EXTERN JSVM\_Status OH\_JSVM\_CreateDouble(JSVM\_Env env,double value,JSVM\_Value\* result)](#oh_jsvm_createdouble) | Converts a value of the C double type to a value of the JavaScript number type. |
| [JSVM\_EXTERN JSVM\_Status OH\_JSVM\_CreateBigintInt64(JSVM\_Env env,int64\_t value,JSVM\_Value\* result)](#oh_jsvm_createbigintint64) | Converts a value of the C int64\_t type to a value of the JavaScript BigInt type. |
| [JSVM\_EXTERN JSVM\_Status OH\_JSVM\_CreateBigintUint64(JSVM\_Env env,uint64\_t value,JSVM\_Value\* result)](#oh_jsvm_createbigintuint64) | Converts a value of the C uint64\_t type to a value of the JavaScript BigInt type. |
| [JSVM\_EXTERN JSVM\_Status OH\_JSVM\_CreateBigintWords(JSVM\_Env env,int signBit,size\_t wordCount,const uint64\_t\* words,JSVM\_Value\* result)](#oh_jsvm_createbigintwords) | Converts a group of 64-bit unsigned bits to a single BigInt value. |
| [JSVM\_EXTERN JSVM\_Status OH\_JSVM\_CreateStringLatin1(JSVM\_Env env,const char\* str,size\_t length,JSVM\_Value\* result)](#oh_jsvm_createstringlatin1) | Converts an ISO-8859-1-encoded C string to a JavaScript string. A native string is copied. |
| [JSVM\_EXTERN JSVM\_Status OH\_JSVM\_CreateStringUtf16(JSVM\_Env env,const char16\_t\* str,size\_t length,JSVM\_Value\* result)](#oh_jsvm_createstringutf16) | Converts a UTF-16LE-encoded C string to a JavaScript string. A native string is copied. |
| [JSVM\_EXTERN JSVM\_Status OH\_JSVM\_CreateStringUtf8(JSVM\_Env env,const char\* str,size\_t length,JSVM\_Value\* result)](#oh_jsvm_createstringutf8) | Creates a JavaScript string using a UTF-8-encoded C string. A native string is copied. |
| [JSVM\_EXTERN JSVM\_Status OH\_JSVM\_GetArrayLength(JSVM\_Env env,JSVM\_Value value,uint32\_t\* result)](#oh_jsvm_getarraylength) | Obtains the length of an array. |
| [JSVM\_EXTERN JSVM\_Status OH\_JSVM\_GetArraybufferInfo(JSVM\_Env env,JSVM\_Value arraybuffer,void\*\* data,size\_t\* byteLength)](#oh_jsvm_getarraybufferinfo) | Obtains the underlying data buffer of the **ArrayBuffer** and its length. |
| [JSVM\_EXTERN JSVM\_Status OH\_JSVM\_GetPrototype(JSVM\_Env env,JSVM\_Value object,JSVM\_Value\* result)](#oh_jsvm_getprototype) | Obtains the prototype of an object. |
| [JSVM\_EXTERN JSVM\_Status OH\_JSVM\_GetTypedarrayInfo(JSVM\_Env env,JSVM\_Value typedarray,JSVM\_TypedarrayType\* type,size\_t\* length,void\*\* data,JSVM\_Value\* arraybuffer,size\_t\* byteOffset)](#oh_jsvm_gettypedarrayinfo) | Obtains the properties of a typed array. If any property is not required, its output parameter can be **NULL**. |
| [JSVM\_EXTERN JSVM\_Status OH\_JSVM\_GetDataviewInfo(JSVM\_Env env,JSVM\_Value dataview,size\_t\* bytelength,void\*\* data,JSVM\_Value\* arraybuffer,size\_t\* byteOffset)](#oh_jsvm_getdataviewinfo) | Obtains the proprieties of a **DataView**. If any property is not required, its output parameter can be **NULL**. |
| [JSVM\_EXTERN JSVM\_Status OH\_JSVM\_GetDateValue(JSVM\_Env env,JSVM\_Value value,double\* result)](#oh_jsvm_getdatevalue) | Obtains the C double-precision primitive equivalent of a given JavaScript date. If this API call is successfully, **JSVM\_OK** is returned. If a **JSVM\_Value** of a non-JavaScript date type is passed in, **JSVM\_DATA\_EXPECTED** is returned. |
| [JSVM\_EXTERN JSVM\_Status OH\_JSVM\_GetValueBool(JSVM\_Env env,JSVM\_Value value,bool\* result)](#oh_jsvm_getvaluebool) | Obtains the C Boolean primitive equivalent of a given JavaScript Boolean value. |
| [JSVM\_EXTERN JSVM\_Status OH\_JSVM\_GetValueDouble(JSVM\_Env env,JSVM\_Value value,double\* result)](#oh_jsvm_getvaluedouble) | Obtains the C double-precision primitive equivalent of a given JavaScript number. |
| [JSVM\_EXTERN JSVM\_Status OH\_JSVM\_GetValueBigintInt64(JSVM\_Env env,JSVM\_Value value,int64\_t\* result,bool\* lossless)](#oh_jsvm_getvaluebigintint64) | Obtains the C int64\_t primitive equivalent of a given JavaScript BigInt value. If necessary, it truncates the value and sets **lossless** to **false**. |
| [JSVM\_EXTERN JSVM\_Status OH\_JSVM\_GetValueBigintUint64(JSVM\_Env env,JSVM\_Value value,uint64\_t\* result,bool\* lossless)](#oh_jsvm_getvaluebigintuint64) | Obtains the C uint64\_t primitive equivalent of a given JavaScript BigInt value. If necessary, it truncates the value and sets **lossless** to **false**. |
| [JSVM\_EXTERN JSVM\_Status OH\_JSVM\_GetValueBigintWords(JSVM\_Env env,JSVM\_Value value,int\* signBit,size\_t\* wordCount,uint64\_t\* words)](#oh_jsvm_getvaluebigintwords) | Converts a BigInt value to the sign bit, 64-bit little-endian array, and number of elements in the array. Both **signBit** and **words** can be set to **NULL**. In this case, only **wordCount** is obtained. |
| [JSVM\_EXTERN JSVM\_Status OH\_JSVM\_GetValueExternal(JSVM\_Env env,JSVM\_Value value,void\*\* result)](#oh_jsvm_getvalueexternal) | Obtains the external data pointer previously passed to **OH\_JSVM\_CreateExternal()**. |
| [JSVM\_EXTERN JSVM\_Status OH\_JSVM\_GetValueInt32(JSVM\_Env env,JSVM\_Value value,int32\_t\* result)](#oh_jsvm_getvalueint32) | Obtains the C int32 primitive equivalent of a given JavaScript number. |
| [JSVM\_EXTERN JSVM\_Status OH\_JSVM\_GetValueInt64(JSVM\_Env env,JSVM\_Value value,int64\_t\* result)](#oh_jsvm_getvalueint64) | Obtains the C int64 primitive equivalent of a given JavaScript number. |
| [JSVM\_EXTERN JSVM\_Status OH\_JSVM\_GetValueStringLatin1(JSVM\_Env env,JSVM\_Value value,char\* buf,size\_t bufsize,size\_t\* result)](#oh_jsvm_getvaluestringlatin1) | Obtains the ISO-8859-1-encoded string corresponding to the input value. |
| [JSVM\_EXTERN JSVM\_Status OH\_JSVM\_GetValueStringUtf8(JSVM\_Env env,JSVM\_Value value,char\* buf,size\_t bufsize,size\_t\* result)](#oh_jsvm_getvaluestringutf8) | Obtains the UTF-8-encoded string corresponding to the input value. |
| [JSVM\_EXTERN JSVM\_Status OH\_JSVM\_GetValueStringUtf16(JSVM\_Env env,JSVM\_Value value,char16\_t\* buf,size\_t bufsize,size\_t\* result)](#oh_jsvm_getvaluestringutf16) | Obtains the UTF-16-encoded string corresponding to the input value. |
| [JSVM\_EXTERN JSVM\_Status OH\_JSVM\_GetValueUint32(JSVM\_Env env,JSVM\_Value value,uint32\_t\* result)](#oh_jsvm_getvalueuint32) | Obtains the C uint\_32 primitive equivalent of a given JavaScript number. |
| [JSVM\_EXTERN JSVM\_Status OH\_JSVM\_GetBoolean(JSVM\_Env env,bool value,JSVM\_Value\* result)](#oh_jsvm_getboolean) | Obtains a JavaScript singleton object that is used to represent the given Boolean value. |
| [JSVM\_EXTERN JSVM\_Status OH\_JSVM\_GetGlobal(JSVM\_Env env,JSVM\_Value\* result)](#oh_jsvm_getglobal) | Obtains the global object. |
| [JSVM\_EXTERN JSVM\_Status OH\_JSVM\_GetNull(JSVM\_Env env,JSVM\_Value\* result)](#oh_jsvm_getnull) | Obtains the null object. |
| [JSVM\_EXTERN JSVM\_Status OH\_JSVM\_GetUndefined(JSVM\_Env env,JSVM\_Value\* result)](#oh_jsvm_getundefined) | Obtains the undefined object. |
| [JSVM\_EXTERN JSVM\_Status OH\_JSVM\_CoerceToBool(JSVM\_Env env,JSVM\_Value value,JSVM\_Value\* result)](#oh_jsvm_coercetobool) | Implements the abstract operation **ToBoolean()**. |
| [JSVM\_EXTERN JSVM\_Status OH\_JSVM\_CoerceToNumber(JSVM\_Env env,JSVM\_Value value,JSVM\_Value\* result)](#oh_jsvm_coercetonumber) | Implements the abstract operation **ToNumber()**. If the input value is an object, the function may run JavaScript code. |
| [JSVM\_EXTERN JSVM\_Status OH\_JSVM\_CoerceToObject(JSVM\_Env env,JSVM\_Value value,JSVM\_Value\* result)](#oh_jsvm_coercetoobject) | Implements the abstract operation **ToObject()**. |
| [JSVM\_EXTERN JSVM\_Status OH\_JSVM\_CoerceToString(JSVM\_Env env,JSVM\_Value value,JSVM\_Value\* result)](#oh_jsvm_coercetostring) | Implements the abstract operation **ToString()**. If the input value is an object, the function may run JavaScript code. |
| [JSVM\_EXTERN JSVM\_Status OH\_JSVM\_Typeof(JSVM\_Env env,JSVM\_Value value,JSVM\_ValueType\* result)](#oh_jsvm_typeof) | Provides a behavior similar to calling the **typeof** operator on a defined object. The difference is that this function supports the detection of external values; it detects null as a separate type, while ECMAScript **typeof** is used to detect objects. If the value type is invalid, an error is returned. |
| [JSVM\_EXTERN JSVM\_Status OH\_JSVM\_Instanceof(JSVM\_Env env,JSVM\_Value object,JSVM\_Value constructor,bool\* result)](#oh_jsvm_instanceof) | Provides a behavior similar to calling the **instanceof** operator on an object. |
| [JSVM\_EXTERN JSVM\_Status OH\_JSVM\_IsArray(JSVM\_Env env,JSVM\_Value value,bool\* result)](#oh_jsvm_isarray) | Provides a behavior similar to calling **IsArray** on an object. |
| [JSVM\_EXTERN JSVM\_Status OH\_JSVM\_IsArraybuffer(JSVM\_Env env,JSVM\_Value value,bool\* result)](#oh_jsvm_isarraybuffer) | Checks whether the input object is an **ArrayBuffer**. |
| [JSVM\_EXTERN JSVM\_Status OH\_JSVM\_IsDate(JSVM\_Env env,JSVM\_Value value,bool\* isDate)](#oh_jsvm_isdate) | Checks whether the input object is a date. |
| [JSVM\_EXTERN JSVM\_Status OH\_JSVM\_IsTypedarray(JSVM\_Env env,JSVM\_Value value,bool\* result)](#oh_jsvm_istypedarray) | Checks whether the input object is a typed array. |
| [JSVM\_EXTERN JSVM\_Status OH\_JSVM\_IsDataview(JSVM\_Env env,JSVM\_Value value,bool\* result)](#oh_jsvm_isdataview) | Checks whether the input object is **DataView**. |
| [JSVM\_EXTERN JSVM\_Status OH\_JSVM\_StrictEquals(JSVM\_Env env,JSVM\_Value lhs,JSVM\_Value rhs,bool\* result)](#oh_jsvm_strictequals) | Provides a behavior similar to calling the strict equality algorithm. |
| [JSVM\_EXTERN JSVM\_Status OH\_JSVM\_Equals(JSVM\_Env env,JSVM\_Value lhs,JSVM\_Value rhs,bool\* result)](#oh_jsvm_equals) | Provides a behavior similar to calling the loose equality algorithm. Regardless of the JavaScript value type, **true** is returned as long as the values are equal. |
| [JSVM\_EXTERN JSVM\_Status OH\_JSVM\_DetachArraybuffer(JSVM\_Env env,JSVM\_Value arraybuffer)](#oh_jsvm_detacharraybuffer) | Provides a behavior similar to calling the **detach** operation of **ArrayBuffer**. |
| [JSVM\_EXTERN JSVM\_Status OH\_JSVM\_IsDetachedArraybuffer(JSVM\_Env env,JSVM\_Value value,bool\* result)](#oh_jsvm_isdetachedarraybuffer) | Provides a behavior similar to calling the **IsDetachedBuffer** operation of **ArrayBuffer**. |
| [JSVM\_EXTERN JSVM\_Status OH\_JSVM\_GetPropertyNames(JSVM\_Env env,JSVM\_Value object,JSVM\_Value\* result)](#oh_jsvm_getpropertynames) | Obtains the names of enumerable properties of an object as an array of characters. The properties of the object whose key is a symbol are not included. |
| [JSVM\_EXTERN JSVM\_Status OH\_JSVM\_GetAllPropertyNames(JSVM\_Env env,JSVM\_Value object,JSVM\_KeyCollectionMode keyMode,JSVM\_KeyFilter keyFilter,JSVM\_KeyConversion keyConversion,JSVM\_Value\* result)](#oh_jsvm_getallpropertynames) | Obtains all available property names of the object. |
| [JSVM\_EXTERN JSVM\_Status OH\_JSVM\_SetProperty(JSVM\_Env env,JSVM\_Value object,JSVM\_Value key,JSVM\_Value value)](#oh_jsvm_setproperty) | Sets the **key** property for the input object. |
| [JSVM\_EXTERN JSVM\_Status OH\_JSVM\_GetProperty(JSVM\_Env env,JSVM\_Value object,JSVM\_Value key,JSVM\_Value\* result)](#oh_jsvm_getproperty) | Obtains the **key** property from the input object. |
| [JSVM\_EXTERN JSVM\_Status OH\_JSVM\_HasProperty(JSVM\_Env env,JSVM\_Value object,JSVM\_Value key,bool\* result)](#oh_jsvm_hasproperty) | Checks whether the input object has the **key** property. |
| [JSVM\_EXTERN JSVM\_Status OH\_JSVM\_DeleteProperty(JSVM\_Env env,JSVM\_Value object,JSVM\_Value key,bool\* result)](#oh_jsvm_deleteproperty) | Deletes the **key** property from the object. |
| [JSVM\_EXTERN JSVM\_Status OH\_JSVM\_HasOwnProperty(JSVM\_Env env,JSVM\_Value object,JSVM\_Value key,bool\* result)](#oh_jsvm_hasownproperty) | Checks whether the input object has the **key** property. The key must be a string or symbol. Otherwise, an error is thrown. The JSVM-API does not perform any conversion between data types. |
| [JSVM\_EXTERN JSVM\_Status OH\_JSVM\_SetNamedProperty(JSVM\_Env env,JSVM\_Value object,const char\* utf8name,JSVM\_Value value)](#oh_jsvm_setnamedproperty) | Sets a property with a specified name. This method is equivalent to calling **OH\_JSVM\_SetProperty** to set the **utf8Name** property. |
| [JSVM\_EXTERN JSVM\_Status OH\_JSVM\_GetNamedProperty(JSVM\_Env env,JSVM\_Value object,const char\* utf8name,JSVM\_Value\* result)](#oh_jsvm_getnamedproperty) | Obtains the named property. This method is equivalent to calling **OH\_JSVM\_GetProperty** to obtain the **utf8Name** property. |
| [JSVM\_EXTERN JSVM\_Status OH\_JSVM\_HasNamedProperty(JSVM\_Env env,JSVM\_Value object,const char\* utf8name,bool\* result)](#oh_jsvm_hasnamedproperty) | Checks whether an object has the named property. This method is equivalent to calling **OH\_JSVM\_HasProperty** to check whether the object has the **utf8Name** property. |
| [JSVM\_EXTERN JSVM\_Status OH\_JSVM\_SetElement(JSVM\_Env env,JSVM\_Value object,uint32\_t index,JSVM\_Value value)](#oh_jsvm_setelement) | Sets an element for the input object. |
| [JSVM\_EXTERN JSVM\_Status OH\_JSVM\_GetElement(JSVM\_Env env,JSVM\_Value object,uint32\_t index,JSVM\_Value\* result)](#oh_jsvm_getelement) | Obtains the element at the requested index. |
| [JSVM\_EXTERN JSVM\_Status OH\_JSVM\_HasElement(JSVM\_Env env,JSVM\_Value object,uint32\_t index,bool\* result)](#oh_jsvm_haselement) | Checks whether an input object has an element at the specified index. If yes, the JSVM-API returns **true**. |
| [JSVM\_EXTERN JSVM\_Status OH\_JSVM\_DeleteElement(JSVM\_Env env,JSVM\_Value object,uint32\_t index,bool\* result)](#oh_jsvm_deleteelement) | Deletes the element at the specified index from an object. |
| [JSVM\_EXTERN JSVM\_Status OH\_JSVM\_DefineProperties(JSVM\_Env env,JSVM\_Value object,size\_t propertyCount,const JSVM\_PropertyDescriptor\* properties)](#oh_jsvm_defineproperties) | Defines properties on a given object by using property descriptors. Through an array of property descriptors, this API sets the properties in the array in turn for the object. |
| [JSVM\_EXTERN JSVM\_Status OH\_JSVM\_ObjectFreeze(JSVM\_Env env,JSVM\_Value object)](#oh_jsvm_objectfreeze) | Freezes a JavaScript object. Once a JavaScript object is frozen, new properties cannot be added to it, existing properties cannot be removed, the enumerability, configurability, or writability of existing properties cannot be changed, and the values of existing properties and object prototypes cannot be changed. |
| [JSVM\_EXTERN JSVM\_Status OH\_JSVM\_ObjectSeal(JSVM\_Env env,JSVM\_Value object)](#oh_jsvm_objectseal) | Encapsulates a specified object, which prevents additions of properties and marks existing properties non-configurable. |
| [JSVM\_EXTERN JSVM\_Status OH\_JSVM\_CallFunction(JSVM\_Env env,JSVM\_Value recv,JSVM\_Value func,size\_t argc,const JSVM\_Value\* argv,JSVM\_Value\* result)](#oh_jsvm_callfunction) | Supports calling JavaScript function objects from native code, which is the main mechanism for JavaScript to call native code. |
| [JSVM\_EXTERN JSVM\_Status OH\_JSVM\_CreateFunction(JSVM\_Env env,const char\* utf8name,size\_t length,JSVM\_Callback cb,JSVM\_Value\* result)](#oh_jsvm_createfunction) | Supports creating function objects in native code, which is the main mechanism for JavaScript to call native code. After this call, the newly created function is no longer automatically visible in the script. Instead, you should explicitly set properties on any visible object in JavaScript to access the function from the script. |
| [JSVM\_EXTERN JSVM\_Status OH\_JSVM\_GetCbInfo(JSVM\_Env env,JSVM\_CallbackInfo cbinfo,size\_t\* argc,JSVM\_Value\* argv,JSVM\_Value\* thisArg,void\*\* data)](#oh_jsvm_getcbinfo) | Obtains detailed information about the callback, such as the parameter from the given callback information and the **this** pointer. |
| [JSVM\_EXTERN JSVM\_Status OH\_JSVM\_GetNewTarget(JSVM\_Env env,JSVM\_CallbackInfo cbinfo,JSVM\_Value\* result)](#oh_jsvm_getnewtarget) | Obtains the new target called by the constructor. If the current callback is not called by a constructor, the result is **NULL**. |
| [JSVM\_EXTERN JSVM\_Status OH\_JSVM\_NewInstance(JSVM\_Env env,JSVM\_Value constructor,size\_t argc,const JSVM\_Value\* argv,JSVM\_Value\* result)](#oh_jsvm_newinstance) | Instantiates a new JavaScript value by using the constructor represented by the given **JSVM\_Value**. |
| [JSVM\_EXTERN JSVM\_Status OH\_JSVM\_DefineClass(JSVM\_Env env,const char\* utf8name,size\_t length,JSVM\_Callback constructor,size\_t propertyCount,const JSVM\_PropertyDescriptor\* properties,JSVM\_Value\* result)](#oh_jsvm_defineclass) | Defines a JavaScript class. |
| [JSVM\_EXTERN JSVM\_Status OH\_JSVM\_Wrap(JSVM\_Env env,JSVM\_Value jsObject,void\* nativeObject,JSVM\_Finalize finalizeCb,void\* finalizeHint,JSVM\_Ref\* result)](#oh_jsvm_wrap) | Wraps a native instance in a JavaScript object, which can be retrieved using **OH\_JSVM\_Unwrap()** later. |
| [JSVM\_EXTERN JSVM\_Status OH\_JSVM\_Unwrap(JSVM\_Env env,JSVM\_Value jsObject,void\*\* result)](#oh_jsvm_unwrap) | Unwraps a native instance in a JavaScript object. When the JavaScript code calls a method of a class or property accessor, the corresponding **JSVM\_Callback** is called. If the callback is for an instance method or accessor, the **this** parameter of the callback is the wrapper object. Then you can obtain the C++ instance as the call target by calling **OH\_JSVM\_Unwrap()** of the wrapper object. |
| [JSVM\_EXTERN JSVM\_Status OH\_JSVM\_RemoveWrap(JSVM\_Env env,JSVM\_Value jsObject,void\*\* result)](#oh_jsvm_removewrap) | Removes the wrap of the native instance, which is previously wrapped in **js\_object** by **OH\_JSVM\_Wrap()**. If the **finalize** callback is associated with wrap, it will not be called when the JavaScript object is garbage-collected. |
| [JSVM\_EXTERN JSVM\_Status OH\_JSVM\_TypeTagObject(JSVM\_Env env,JSVM\_Value value,const JSVM\_TypeTag\* typeTag)](#oh_jsvm_typetagobject) | Associates the value of the **typeTag** pointer with a JavaScript object or an external value. You can call **OH\_JSVM\_CheckObjectTypeTag()** to check the type of the tag attached to the object to ensure that the object type is correct. If the object already has an associated type tag, **JSVM\_INVALID\_ARG** is returned. |
| [JSVM\_EXTERN JSVM\_Status OH\_JSVM\_CheckObjectTypeTag(JSVM\_Env env,JSVM\_Value value,const JSVM\_TypeTag\* typeTag,bool\* result)](#oh_jsvm_checkobjecttypetag) | Checks the **typeTag** with the tag on a JavaScript object or external value. If they are the same tag, **result** is set to **true**. Otherwise, **result** is set to **false**. |
| [JSVM\_EXTERN JSVM\_Status OH\_JSVM\_AddFinalizer(JSVM\_Env env,JSVM\_Value jsObject,void\* finalizeData,JSVM\_Finalize finalizeCb,void\* finalizeHint,JSVM\_Ref\* result)](#oh_jsvm_addfinalizer) | Adds the **JSVM\_Finalize** callback to a JavaScript object. This callback is called when the JavaScript object is garbage-collected. **OH\_JSVM\_AddFinalizer** can be called multiple times on a single JavaScript object. |
| [JSVM\_EXTERN JSVM\_Status OH\_JSVM\_GetVersion(JSVM\_Env env,uint32\_t\* result)](#oh_jsvm_getversion) | Obtains the latest JSVM-API version supported by the JSVM runtime. New JSVM-API APIs will be added to support more features. With this API, the new features of a certain JSVM version can be used, or callbacks are provided if a feature is not supported. |
| [JSVM\_EXTERN JSVM\_Status OH\_JSVM\_GetVMInfo(JSVM\_VMInfo\* result)](#oh_jsvm_getvminfo) | Obtains the VM information. |
| [JSVM\_EXTERN JSVM\_Status OH\_JSVM\_AdjustExternalMemory(JSVM\_Env env,int64\_t changeInBytes,int64\_t\* result)](#oh_jsvm_adjustexternalmemory) | Notifies the underlying VM of the size of externally allocated memory that remains active due to the JavaScript object. Registering externally allocated memory triggers global garbage collection more frequently than in other ways. |
| [JSVM\_EXTERN JSVM\_Status OH\_JSVM\_MemoryPressureNotification(JSVM\_Env env,JSVM\_MemoryPressureLevel level)](#oh_jsvm_memorypressurenotification) | Notifies the VM of insufficient system memory and selectively triggers garbage collection. |
| [JSVM\_EXTERN JSVM\_Status OH\_JSVM\_CreatePromise(JSVM\_Env env,JSVM\_Deferred\* deferred,JSVM\_Value\* promise)](#oh_jsvm_createpromise) | Creates a deferred object and a JavaScript promise. |
| [JSVM\_EXTERN JSVM\_Status OH\_JSVM\_ResolveDeferred(JSVM\_Env env,JSVM\_Deferred deferred,JSVM\_Value resolution)](#oh_jsvm_resolvedeferred) | Resolves a JavaScript promise by using the associated deferred object. It can only be used to resolve the JavaScript promise of the corresponding available deferred object. This means that promise must be created using **OH\_JSVM\_CreatePromise()**, and the object returned from this call must be retained so that it can be passed to this API. |
| [JSVM\_EXTERN JSVM\_Status OH\_JSVM\_RejectDeferred(JSVM\_Env env,JSVM\_Deferred deferred,JSVM\_Value rejection)](#oh_jsvm_rejectdeferred) | Rejects a JavaScript promise by using the associated deferred object. It can only be used to reject the JavaScript promise of the corresponding available deferred object. This means that promise must be created using **OH\_JSVM\_CreatePromise()**, and the object returned from this call must be retained so that it can be passed to this API. |
| [JSVM\_EXTERN JSVM\_Status OH\_JSVM\_IsPromise(JSVM\_Env env,JSVM\_Value value,bool\* isPromise)](#oh_jsvm_ispromise) | Checks whether a promise object is native. |
| [JSVM\_EXTERN JSVM\_Status OH\_JSVM\_PromiseRegisterHandler(JSVM\_Env env,JSVM\_Value promise,JSVM\_Value onFulfilled,JSVM\_Value onRejected,JSVM\_Value\* result)](#oh_jsvm_promiseregisterhandler) | Registers a handler for processing promise fulfillment and rejection. |
| [JSVM\_EXTERN JSVM\_Status OH\_JSVM\_JsonParse(JSVM\_Env env,JSVM\_Value jsonString,JSVM\_Value\* result)](#oh_jsvm_jsonparse) | Parses a JSON string and returns the parsed value. |
| [JSVM\_EXTERN JSVM\_Status OH\_JSVM\_JsonStringify(JSVM\_Env env,JSVM\_Value jsonObject,JSVM\_Value\* result)](#oh_jsvm_jsonstringify) | Converts an object into a JSON string and returns the converted string. |
| [JSVM\_EXTERN JSVM\_Status OH\_JSVM\_CreateSnapshot(JSVM\_VM vm,size\_t contextCount,const JSVM\_Env\* contexts,const char\*\* blobData,size\_t\* blobSize)](#oh_jsvm_createsnapshot) | Creates a VM startup snapshot. |
| [JSVM\_EXTERN JSVM\_Status OH\_JSVM\_GetHeapStatistics(JSVM\_VM vm,JSVM\_HeapStatistics\* result)](#oh_jsvm_getheapstatistics) | Obtains heap statistics of a VM. |
| [JSVM\_EXTERN JSVM\_Status OH\_JSVM\_StartCpuProfiler(JSVM\_VM vm,JSVM\_CpuProfiler\* result)](#oh_jsvm_startcpuprofiler) | Creates and starts a CPU profiler instance. |
| [JSVM\_EXTERN JSVM\_Status OH\_JSVM\_StopCpuProfiler(JSVM\_VM vm,JSVM\_CpuProfiler profiler,JSVM\_OutputStream stream,void\* streamData)](#oh_jsvm_stopcpuprofiler) | Stops the CPU profiler and outputs the result to a stream. |
| [JSVM\_EXTERN JSVM\_Status OH\_JSVM\_TakeHeapSnapshot(JSVM\_VM vm,JSVM\_OutputStream stream,void\* streamData)](#oh_jsvm_takeheapsnapshot) | Obtains a snapshot of the current heap and outputs it to a stream. |
| [JSVM\_EXTERN JSVM\_Status OH\_JSVM\_OpenInspector(JSVM\_Env env,const char\* host,uint16\_t port)](#oh_jsvm_openinspector) | Opens an inspector instance on the specified host and port for debugging JS code. |
| [JSVM\_EXTERN JSVM\_Status OH\_JSVM\_CloseInspector(JSVM\_Env env)](#oh_jsvm_closeinspector) | Closes all remaining inspector connections. |
| [JSVM\_EXTERN JSVM\_Status OH\_JSVM\_WaitForDebugger(JSVM\_Env env,bool breakNextLine)](#oh_jsvm_waitfordebugger) | Waits for the host to set up a socket connection with an inspector. After the connection is set up, the application continues to run. **Runtime.runIfWaitingForDebugger** is sent. |
| [JSVM\_EXTERN JSVM\_Status OH\_JSVM\_DefineClassWithPropertyHandler(JSVM\_Env env,const char\* utf8name,size\_t length,JSVM\_Callback constructor,size\_t propertyCount,const JSVM\_PropertyDescriptor\* properties,JSVM\_PropertyHandlerCfg propertyHandlerCfg,JSVM\_Callback callAsFunctionCallback,JSVM\_Value\* result)](#oh_jsvm_defineclasswithpropertyhandler) | Defines a set of JavaScript class property handlers including **getter**, **setter**, **deleter**, and **enumerator** with the given class name, constructor, properties, and callback, which are called as callbacks. |
| [JSVM\_EXTERN JSVM\_Status OH\_JSVM\_IsLocked(JSVM\_Env env, bool\* isLocked)](#oh_jsvm_islocked) | Checks whether the current thread holds a lock of the specified environment. Only the thread that holds the lock can use the environment. |
| [JSVM\_EXTERN JSVM\_Status OH\_JSVM\_AcquireLock(JSVM\_Env env)](#oh_jsvm_acquirelock) | Obtains a lock. Only the thread that holds the lock can use the environment. |
| [JSVM\_EXTERN JSVM\_Status OH\_JSVM\_ReleaseLock(JSVM\_Env env)](#oh_jsvm_releaselock) | Releases a lock. Only the thread that holds the lock can use the environment. |
| [JSVM\_EXTERN JSVM\_Status OH\_JSVM\_IsUndefined(JSVM\_Env env,JSVM\_Value value,bool\* isUndefined)](#oh_jsvm_isundefined) | Checks whether the input value is **Undefined**. This API is equivalent to **value === undefined** in JavaScript code. |
| [JSVM\_EXTERN JSVM\_Status OH\_JSVM\_IsNull(JSVM\_Env env,JSVM\_Value value,bool\* isNull)](#oh_jsvm_isnull) | Checks whether the input value is a **Null** object. This API is equivalent to **value === null** in JavaScript code. |
| [JSVM\_EXTERN JSVM\_Status OH\_JSVM\_IsNullOrUndefined(JSVM\_Env env,JSVM\_Value value,bool\* isNullOrUndefined)](#oh_jsvm_isnullorundefined) | Checks whether the input value is **Null** or **Undefined**. This API is equivalent to **value == null** in JavaScript code. |
| [JSVM\_EXTERN JSVM\_Status OH\_JSVM\_IsBoolean(JSVM\_Env env,JSVM\_Value value,bool\* isBoolean)](#oh_jsvm_isboolean) | Checks whether the input value is a Boolean value. This API is equivalent to **typeof value ==='boolean'** in JavaScript code. |
| [JSVM\_EXTERN JSVM\_Status OH\_JSVM\_IsNumber(JSVM\_Env env,JSVM\_Value value,bool\* isNumber)](#oh_jsvm_isnumber) | Checks whether the input value is a number. This API is equivalent to **typeof value === 'number'** in JavaScript code. |
| [JSVM\_EXTERN JSVM\_Status OH\_JSVM\_IsString(JSVM\_Env env,JSVM\_Value value,bool\* isString)](#oh_jsvm_isstring) | Checks whether the input value is a string. This API is equivalent to **typeof value === 'string'** in JavaScript code. |
| [JSVM\_EXTERN JSVM\_Status OH\_JSVM\_IsSymbol(JSVM\_Env env,JSVM\_Value value,bool\* isSymbol)](#oh_jsvm_issymbol) | Checks whether the input value is a symbol. This API is equivalent to **typeof value === 'symbol'** in JavaScript code. |
| [JSVM\_EXTERN JSVM\_Status OH\_JSVM\_IsFunction(JSVM\_Env env,JSVM\_Value value,bool\* isFunction)](#oh_jsvm_isfunction) | Checks whether the input value is a function. This API is equivalent to **typeof value === 'function'** in JavaScript code. |
| [JSVM\_EXTERN JSVM\_Status OH\_JSVM\_IsObject(JSVM\_Env env,JSVM\_Value value,bool\* isObject)](#oh_jsvm_isobject) | Checks whether the input value is an object. |
| [JSVM\_EXTERN JSVM\_Status OH\_JSVM\_IsBigInt(JSVM\_Env env,JSVM\_Value value,bool\* isBigInt)](#oh_jsvm_isbigint) | Checks whether the input value is a BigInt value. This API is equivalent to **typeof value === 'bigint'** in JavaScript code. |
| [JSVM\_EXTERN JSVM\_Status OH\_JSVM\_CreateMap(JSVM\_Env env, JSVM\_Value\* result)](#oh_jsvm_createmap) | Creates a JavaScript value of the Map type. |
| [JSVM\_EXTERN JSVM\_Status OH\_JSVM\_IsMap(JSVM\_Env env,JSVM\_Value value,bool\* isMap)](#oh_jsvm_ismap) | Checks whether the input value is of the Map type. |
| [JSVM\_EXTERN JSVM\_Status OH\_JSVM\_IsConstructor(JSVM\_Env env,JSVM\_Value value,bool\* isConstructor)](#oh_jsvm_isconstructor) | Checks whether the input value is a constructor. |
| [JSVM\_EXTERN JSVM\_Status OH\_JSVM\_CreateRegExp(JSVM\_Env env,JSVM\_Value value,JSVM\_RegExpFlags flags,JSVM\_Value\* result)](#oh_jsvm_createregexp) | Creates a regular expression object corresponding to the input JavaScript string. This API may throw an exception. |
| [JSVM\_EXTERN JSVM\_Status OH\_JSVM\_ObjectGetPrototypeOf(JSVM\_Env env,JSVM\_Value object,JSVM\_Value\* result)](#oh_jsvm_objectgetprototypeof) | Obtains the prototype of a JavaScript object. |
| [JSVM\_EXTERN JSVM\_Status OH\_JSVM\_ObjectSetPrototypeOf(JSVM\_Env env,JSVM\_Value object,JSVM\_Value prototype)](#oh_jsvm_objectsetprototypeof) | Sets the prototype of a JavaScript object. |
| [JSVM\_EXTERN JSVM\_Status OH\_JSVM\_CreateSet(JSVM\_Env env,JSVM\_Value\* result)](#oh_jsvm_createset) | Creates a JavaScript value of the Set type. |
| [JSVM\_EXTERN JSVM\_Status OH\_JSVM\_IsSet(JSVM\_Env env,JSVM\_Value value,bool\* isSet)](#oh_jsvm_isset) | Checks whether the specified object is of the Set type. |
| [JSVM\_EXTERN JSVM\_Status OH\_JSVM\_CoerceToBigInt(JSVM\_Env env,JSVM\_Value value,JSVM\_Value\* result)](#oh_jsvm_coercetobigint) | Implements the abstract operation **ToBigInt()**. |
| [JSVM\_EXTERN JSVM\_Status OH\_JSVM\_IsRegExp(JSVM\_Env env,JSVM\_Value value,bool\* result)](#oh_jsvm_isregexp) | Checks whether the input value is a JavaScript RegExp object. |
| [JSVM\_EXTERN JSVM\_Status OH\_JSVM\_CreateFunctionWithScript(JSVM\_Env env,const char\* funcName,size\_t length,size\_t argc,const JSVM\_Value\* argv,JSVM\_Value script,JSVM\_Value\* result)](#oh_jsvm_createfunctionwithscript) | Creates a function with the given JavaScript as the function body. |
| [JSVM\_EXTERN JSVM\_Status OH\_JSVM\_PumpMessageLoop(JSVM\_VM vm,bool\* result)](#oh_jsvm_pumpmessageloop) | Starts the message loop in the VM. This message loop can be executed through the external event loop. |
| [JSVM\_EXTERN JSVM\_Status OH\_JSVM\_PerformMicrotaskCheckpoint(JSVM\_VM vm)](#oh_jsvm_performmicrotaskcheckpoint) | Checks whether there are microtasks waiting in the queue. If yes, execute them. |
| [JSVM\_EXTERN JSVM\_Status OH\_JSVM\_IsCallable(JSVM\_Env env, JSVM\_Value value, bool\* isCallable)](#oh_jsvm_iscallable) | Checks whether the input value is callable. |
| [JSVM\_EXTERN JSVM\_Status OH\_JSVM\_RetainScript(JSVM\_Env env, JSVM\_Script script)](#oh_jsvm_retainscript) | Retains a **JSVM\_Script** and extends its lifecycle beyond the current scope. |
| [JSVM\_EXTERN JSVM\_Status OH\_JSVM\_ReleaseScript(JSVM\_Env env, JSVM\_Script script)](#oh_jsvm_releasescript) | Releases the script retained by **OH\_JSVM\_RetainScript**. The released script cannot be used again. |
| [JSVM\_EXTERN JSVM\_Status OH\_JSVM\_OpenInspectorWithName(JSVM\_Env env,int pid,const char\* name)](#oh_jsvm_openinspectorwithname) | Opens the **name** inspector and its corresponding Unix Domain port with the specified PID. |
| [JSVM\_EXTERN JSVM\_Status OH\_JSVM\_CompileWasmModule(JSVM\_Env env,const uint8\_t \*wasmBytecode,size\_t wasmBytecodeLength,const uint8\_t \*cacheData,size\_t cacheDataLength,bool \*cacheRejected,JSVM\_Value \*wasmModule)](#oh_jsvm_compilewasmmodule) | Compiles the WebAssembly bytecode to obtain a WebAssembly module. If the WebAssembly cache is provided, it will be deserialized first. If this API does not have the JIT permission, a log is printed to notify you. |
| [JSVM\_EXTERN JSVM\_Status OH\_JSVM\_CompileWasmFunction(JSVM\_Env env,JSVM\_Value wasmModule,uint32\_t functionIndex,JSVM\_WasmOptLevel optLevel)](#oh_jsvm_compilewasmfunction) | Compiles a WebAssembly function with the specified index at a specified optimization level. If this API does not have the JIT permission, a log is printed to notify you. |
| [JSVM\_EXTERN JSVM\_Status OH\_JSVM\_IsWasmModuleObject(JSVM\_Env env,JSVM\_Value value,bool\* result)](#oh_jsvm_iswasmmoduleobject) | Checks whether the given **JSVM\_Value** is a WebAssembly module. |
| [JSVM\_EXTERN JSVM\_Status OH\_JSVM\_CreateWasmCache(JSVM\_Env env,JSVM\_Value wasmModule,const uint8\_t\*\* data,size\_t\* length)](#oh_jsvm_createwasmcache) | Creates a WebAssembly cache. If this API does not have the JIT permission, a log is printed to notify you. |
| [JSVM\_EXTERN JSVM\_Status OH\_JSVM\_ReleaseCache(JSVM\_Env env,const uint8\_t\* cacheData,JSVM\_CacheType cacheType)](#oh_jsvm_releasecache) | Releases the cache of a specified type. |
| [JSVM\_EXTERN JSVM\_Status OH\_JSVM\_IsBigIntObject(JSVM\_Env env,JSVM\_Value value,bool\* result)](#oh_jsvm_isbigintobject) | Checks whether the given **JSVM\_Value** is a BigInt object. |
| [JSVM\_EXTERN JSVM\_Status OH\_JSVM\_IsBooleanObject(JSVM\_Env env,JSVM\_Value value,bool\* result)](#oh_jsvm_isbooleanobject) | Checks whether the given **JSVM\_Value** is a Boolean object. |
| [JSVM\_EXTERN JSVM\_Status OH\_JSVM\_IsStringObject(JSVM\_Env env,JSVM\_Value value,bool\* result)](#oh_jsvm_isstringobject) | Checks whether the given **JSVM\_Value** is a string object. |
| [JSVM\_EXTERN JSVM\_Status OH\_JSVM\_IsNumberObject(JSVM\_Env env,JSVM\_Value value,bool\* result)](#oh_jsvm_isnumberobject) | Checks whether the given **JSVM\_Value** is a number object. |
| [JSVM\_EXTERN JSVM\_Status OH\_JSVM\_IsSymbolObject(JSVM\_Env env,JSVM\_Value value,bool\* result)](#oh_jsvm_issymbolobject) | Checks whether the given **JSVM\_Value** is a symbol object. |
| [JSVM\_EXTERN JSVM\_Status OH\_JSVM\_GetSymbolAsyncIterator(JSVM\_Env env, JSVM\_Value\* result)](#oh_jsvm_getsymbolasynciterator) | Obtains the **Symbol.AsyncIterator** capability from the well-known symbol. |
| [JSVM\_EXTERN JSVM\_Status OH\_JSVM\_GetSymbolHasInstance(JSVM\_Env env, JSVM\_Value\* result)](#oh_jsvm_getsymbolhasinstance) | Obtains the **Symbol.HasInstance** capability from the well-known symbol. |
| [JSVM\_EXTERN JSVM\_Status OH\_JSVM\_GetSymbolIsConcatSpreadable(JSVM\_Env env, JSVM\_Value\* result)](#oh_jsvm_getsymbolisconcatspreadable) | Obtains the **Symbol.IsConcatSpreadable** capability from the well-known symbol. |
| [JSVM\_EXTERN JSVM\_Status OH\_JSVM\_GetSymbolMatch(JSVM\_Env env, JSVM\_Value\* result)](#oh_jsvm_getsymbolmatch) | Obtains the **Symbol.Match** capability of the well-known symbol. |
| [JSVM\_EXTERN JSVM\_Status OH\_JSVM\_GetSymbolReplace(JSVM\_Env env, JSVM\_Value\* result)](#oh_jsvm_getsymbolreplace) | Obtains the **Symbol.Replace** capability of the well-known symbol. |
| [JSVM\_EXTERN JSVM\_Status OH\_JSVM\_GetSymbolSearch(JSVM\_Env env, JSVM\_Value\* result)](#oh_jsvm_getsymbolsearch) | Obtains the **Symbol.Search** capability of the well-known symbol. |
| [JSVM\_EXTERN JSVM\_Status OH\_JSVM\_GetSymbolSplit(JSVM\_Env env, JSVM\_Value\* result)](#oh_jsvm_getsymbolsplit) | Obtains the **Symbol.Split** capability of the well-known symbol. |
| [JSVM\_EXTERN JSVM\_Status OH\_JSVM\_GetSymbolToPrimitive(JSVM\_Env env, JSVM\_Value\* result)](#oh_jsvm_getsymboltoprimitive) | Obtains the **Symbol.ToPrimitive** capability of the well-known symbol. |
| [JSVM\_EXTERN JSVM\_Status OH\_JSVM\_GetSymbolUnscopables(JSVM\_Env env, JSVM\_Value\* result)](#oh_jsvm_getsymbolunscopables) | Obtains the **Symbol.Unscopables** capability of the well-known symbol. |
| [JSVM\_EXTERN JSVM\_Status OH\_JSVM\_GetSymbolToStringTag(JSVM\_Env env, JSVM\_Value\* result)](#oh_jsvm_getsymboltostringtag) | Obtains the **Symbol.ToStringTag** capability of the well-known symbol. |
| [JSVM\_EXTERN JSVM\_Status OH\_JSVM\_GetSymbolIterator(JSVM\_Env env, JSVM\_Value\* result)](#oh_jsvm_getsymboliterator) | Obtains the **Symbol.Iterator** capability of the well-known symbol. |
| [JSVM\_EXTERN JSVM\_Status OH\_JSVM\_TraceStart(size\_t count,const JSVM\_TraceCategory\* categories,const char\* tag,size\_t eventsCount)](#oh_jsvm_tracestart) | Starts collecting information of the specified trace categories for all JSVM runtime instances (thread-unsafe). |
| [JSVM\_EXTERN JSVM\_Status OH\_JSVM\_TraceStop(JSVM\_OutputStream stream, void\* streamData)](#oh_jsvm_tracestop) | Stops collecting information of a specified trace category for all JSVM runtime instances (thread-unsafe). |
| [JSVM\_EXTERN JSVM\_Status OH\_JSVM\_AddHandlerForGC(JSVM\_VM vm,JSVM\_CBTriggerTimeForGC triggerTime,JSVM\_HandlerForGC handler,JSVM\_GCType gcType,void\* userData)](#oh_jsvm_addhandlerforgc) | Adds a handler for GC to the VM. |
| [JSVM\_EXTERN JSVM\_Status OH\_JSVM\_RemoveHandlerForGC(JSVM\_VM vm,JSVM\_CBTriggerTimeForGC triggerTime,JSVM\_HandlerForGC handler,void\* userData)](#oh_jsvm_removehandlerforgc) | Removes the handler for GC from the VM. |
| [JSVM\_EXTERN JSVM\_Status OH\_JSVM\_SetHandlerForOOMError(JSVM\_VM vm,JSVM\_HandlerForOOMError handler)](#oh_jsvm_sethandlerforoomerror) | Sets a handler for OOM errors. If the API is called repeatedly, only the last call takes effect. If the input handler is null, the previous setting is canceled. |
| [JSVM\_EXTERN JSVM\_Status OH\_JSVM\_SetDebugOption(JSVM\_Env env, JSVM\_DebugOption debugOption, bool isEnabled)](#oh_jsvm_setdebugoption) | Enables or disables a specific debugging option for a JSVM environment. |
| [JSVM\_EXTERN JSVM\_Status OH\_JSVM\_SetHandlerForFatalError(JSVM\_VM vm,JSVM\_HandlerForFatalError handler)](#oh_jsvm_sethandlerforfatalerror) | Sets a handler for fatal errors. If the API is called repeatedly, only the last call takes effect. If the input handler is null, the previous setting is canceled. |
| [JSVM\_EXTERN JSVM\_Status OH\_JSVM\_SetHandlerForPromiseReject(JSVM\_VM vm,JSVM\_HandlerForPromiseReject handler)](#oh_jsvm_sethandlerforpromisereject) | Sets a handler for the PromiseReject error. If the API is called repeatedly, only the last call takes effect. If the input handler is null, the previous setting is canceled. |
| [JSVM\_EXTERN JSVM\_Status OH\_JSVM\_DefineClassWithOptions(JSVM\_Env env,const char\* utf8name,size\_t length,JSVM\_Callback constructor,size\_t propertyCount,const JSVM\_PropertyDescriptor\* properties,JSVM\_Value parentClass,size\_t option\_count,JSVM\_DefineClassOptions options\[\],JSVM\_Value\* result)](#oh_jsvm_defineclasswithoptions) | Defines a class with options. When a C++ class is encapsulated, the C++ constructor callback passed through the constructor should be a static method in the class. This method calls the actual class constructor, encapsulates a new C++ instance into a JavaScript object based on the input options, and returns the encapsulated object. |
| [JSVM\_EXTERN JSVM\_Status OH\_JSVM\_CreateExternalStringLatin1(JSVM\_Env env,char\* str,size\_t length,JSVM\_Finalize finalizeCallback,void\* finalizeHint,JSVM\_Value\* result,bool\* copied)](#oh_jsvm_createexternalstringlatin1) | Creates an external JavaScript string with an ISO-8859-1-encoded C string. If the creation fails, the original native string is copied. |
| [JSVM\_EXTERN JSVM\_Status OH\_JSVM\_CreateExternalStringUtf16(JSVM\_Env env,char16\_t\* str,size\_t length,JSVM\_Finalize finalizeCallback,void\* finalizeHint,JSVM\_Value\* result,bool\* copied)](#oh_jsvm_createexternalstringutf16) | Creates an external JavaScript string with a UTF-16LE-encoded C string. If the creation fails, the original native string is copied. |
| [JSVM\_EXTERN JSVM\_Status OH\_JSVM\_CreatePrivate(JSVM\_Env env,JSVM\_Value description,JSVM\_Data\* result)](#oh_jsvm_createprivate) | Creates a JavaScript private key object. |
| [JSVM\_EXTERN JSVM\_Status OH\_JSVM\_SetPrivate(JSVM\_Env env,JSVM\_Value object,JSVM\_Data key,JSVM\_Value value)](#oh_jsvm_setprivate) | Sets the **private** property for an input object. |
| [JSVM\_EXTERN JSVM\_Status OH\_JSVM\_GetPrivate(JSVM\_Env env,JSVM\_Value object,JSVM\_Data key,JSVM\_Value \*result)](#oh_jsvm_getprivate) | Obtains the **private** property of an input object based on the private key. |
| [JSVM\_EXTERN JSVM\_Status OH\_JSVM\_DeletePrivate(JSVM\_Env env,JSVM\_Value object,JSVM\_Data key)](#oh_jsvm_deleteprivate) | Deletes the **private** property corresponding to the private key from the input object. |
| [JSVM\_EXTERN JSVM\_Status OH\_JSVM\_CreateDataReference(JSVM\_Env env,JSVM\_Data data,uint32\_t initialRefcount,JSVM\_Ref\* result)](#oh_jsvm_createdatareference) | Creates a reference to a given **JSVM\_Data** object. The initial reference count is the input value of **initialRefcount**. |
| [JSVM\_EXTERN JSVM\_Status OH\_JSVM\_GetReferenceData(JSVM\_Env env,JSVM\_Ref ref,JSVM\_Data\* result)](#oh_jsvm_getreferencedata) | Obtains the **JSVM\_Data** (a JavaScript value associated with the JSVM reference) through the **result** parameter if the reference is still valid. Otherwise, the result is null. |

#### Function Description

#### \[h2\]OH\_JSVM\_Init()

JSVM\_EXTERN JSVM\_Status OH\_JSVM\_Init(const JSVM\_InitOptions\* options)

**Description**

Initializes a JavaScript VM.

**Since**: 11

**Parameters**

| Name | Description |
| :-- | :-- |
| [const JSVM\_InitOptions](../../structs/jsvm-initoptions/document.md)\* options | Pointer to the options for initializing the JavaScript VM. |

**Returns**

| Type | Description |
| :-- | :-- |
| JSVM\_EXTERN [JSVM\_Status](../jsvm-types-h/document.md#jsvm_status) | 
Returns a JSVM status code.

[JSVM\_OK](../jsvm-types-h/document.md#jsvm_status): operation successful.

[JSVM\_GENERIC\_FAILURE](../jsvm-types-h/document.md#jsvm_status): generic failure. This code is returned if the operation fails, indicating that JSVM initialization is complete and that repeated execution is not required.

 |

#### \[h2\]OH\_JSVM\_CreateVM()

JSVM\_EXTERN JSVM\_Status OH\_JSVM\_CreateVM(const JSVM\_CreateVMOptions\* options,JSVM\_VM\* result)

**Description**

Creates a VM instance.

**Since**: 11

**Parameters**

| Name | Description |
| :-- | :-- |
| [const JSVM\_CreateVMOptions](../../structs/jsvm-createvmoptions/document.md)\* options | Pointer to the options for creating a VM instance. |
| [JSVM\_VM](../../structs/jsvm-vm/document.md)\* result | Pointer to the new VM instance. |

**Returns**

| Type | Description |
| :-- | :-- |
| JSVM\_EXTERN [JSVM\_Status](../jsvm-types-h/document.md#jsvm_status) | 
Returns a JSVM status code.

[JSVM\_OK](../jsvm-types-h/document.md#jsvm_status): operation successful.

[JSVM\_INVALID\_ARG](../jsvm-types-h/document.md#jsvm_status): invalid argument.

 |

#### \[h2\]OH\_JSVM\_SetMicrotaskPolicy()

JSVM\_EXTERN JSVM\_Status OH\_JSVM\_SetMicrotaskPolicy(JSVM\_VM vm,JSVM\_MicrotaskPolicy policy)

**Description**

Sets the microtask execution policy for a VM instance. If this method is not called, the default policy **JSVM\_MicrotaskPolicy::JSVM\_MICROTASK\_AUTO** is used.

**Since**: 18

**Parameters**

| Name | Description |
| :-- | :-- |
| [JSVM\_VM](../../structs/jsvm-vm/document.md) vm | Target VM instance. |
| [JSVM\_MicrotaskPolicy](../jsvm-types-h/document.md#jsvm_microtaskpolicy) policy | Policy for executing microtasks. |

**Returns**

| Type | Description |
| :-- | :-- |
| JSVM\_EXTERN [JSVM\_Status](../jsvm-types-h/document.md#jsvm_status) | 
Returns **JSVM\_OK** if this API call is successful.

[JSVM\_OK](../jsvm-types-h/document.md#jsvm_status): operation successful.

[JSVM\_INVALID\_ARG](../jsvm-types-h/document.md#jsvm_status): invalid argument.

 |

#### \[h2\]OH\_JSVM\_DestroyVM()

JSVM\_EXTERN JSVM\_Status OH\_JSVM\_DestroyVM(JSVM\_VM vm)

**Description**

Destroys a VM instance.

**Since**: 11

**Parameters**

| Name | Description |
| :-- | :-- |
| [JSVM\_VM](../../structs/jsvm-vm/document.md) vm | VM instance to be destroyed. |

**Returns**

| Type | Description |
| :-- | :-- |
| JSVM\_EXTERN [JSVM\_Status](../jsvm-types-h/document.md#jsvm_status) | 
Returns a JSVM status code.

[JSVM\_OK](../jsvm-types-h/document.md#jsvm_status): operation successful.

[JSVM\_INVALID\_ARG](../jsvm-types-h/document.md#jsvm_status): invalid argument.

 |

#### \[h2\]OH\_JSVM\_CreateProxy()

JSVM\_EXTERN JSVM\_Status OH\_JSVM\_CreateProxy(JSVM\_Env env,JSVM\_Value target,JSVM\_Value handler,JSVM\_Value\* result)

**Description**

Creates a JavaScript proxy. This API is equivalent to calling **new Proxy(target, handler)** in JS.

**Since**: 18

**Parameters**

| Name | Description |
| :-- | :-- |
| [JSVM\_Env](../../structs/jsvm-env/document.md) env | Environment for calling the JSVM-API. |
| [JSVM\_Value](../../structs/jsvm-value/document.md) target | JavaScript object used to create a proxy. |
| [JSVM\_Value](../../structs/jsvm-value/document.md) handler | Handler that defines the operations to be intercepted and how to handle intercepted operations. |
| [JSVM\_Value](../../structs/jsvm-value/document.md)\* result | JavaScript proxy created. |

**Returns**

| Type | Description |
| :-- | :-- |
| JSVM\_EXTERN [JSVM\_Status](../jsvm-types-h/document.md#jsvm_status) | 
Returns a JSVM status code.

[JSVM\_OK](../jsvm-types-h/document.md#jsvm_status): operation successful.

[JSVM\_OBJECT\_EXPECTED](../jsvm-types-h/document.md#jsvm_status): object expected. This code is returned if the target or handler is not a JavaScript object.

[JSVM\_GENERIC\_FAILURE](../jsvm-types-h/document.md#jsvm_status): generic failure due to unknown reasons.

 |

#### \[h2\]OH\_JSVM\_IsProxy()

JSVM\_EXTERN JSVM\_Status OH\_JSVM\_IsProxy(JSVM\_Env env,JSVM\_Value value,bool\* isProxy)

**Description**

Checks whether the input value is a JavaScript proxy.

**Since**: 18

**Parameters**

| Name | Description |
| :-- | :-- |
| [JSVM\_Env](../../structs/jsvm-env/document.md) env | Environment for calling the JSVM-API. |
| [JSVM\_Value](../../structs/jsvm-value/document.md) value | Value to check. |
| bool\* isProxy | Pointer to the check result, indicating whether the value is a JavaScript Proxy. The value **true** indicates the value is a JavaScript Proxy, and **false** indicates the opposite. |

**Returns**

| Type | Description |
| :-- | :-- |
| [JSVM\_Status](../jsvm-types-h/document.md#jsvm_status) JSVM\_CDECL | 
Returns a JSVM status code.

[JSVM\_OK](../jsvm-types-h/document.md#jsvm_status): operation successful.

[JSVM\_INVALID\_ARG](../jsvm-types-h/document.md#jsvm_status): invalid argument.

 |

#### \[h2\]OH\_JSVM\_ProxyGetTarget()

JSVM\_EXTERN JSVM\_Status OH\_JSVM\_ProxyGetTarget(JSVM\_Env env,JSVM\_Value value,JSVM\_Value\* result)

**Description**

Obtains the target object in the JavaScript Proxy.

**Since**: 18

**Parameters**

| Name | Description |
| :-- | :-- |
| [JSVM\_Env](../../structs/jsvm-env/document.md) env | Environment for calling the JSVM-API. |
| [JSVM\_Value](../../structs/jsvm-value/document.md) value | Proxy of the target object. |
| [JSVM\_Value](../../structs/jsvm-value/document.md)\* result | Pointer to the target object. |

**Returns**

| Type | Description |
| :-- | :-- |
| [JSVM\_Status](../jsvm-types-h/document.md#jsvm_status) JSVM\_CDECL | 
Returns a JSVM status code.

[JSVM\_OK](../jsvm-types-h/document.md#jsvm_status): operation successful.

[JSVM\_INVALID\_ARG](../jsvm-types-h/document.md#jsvm_status): invalid argument.

[JSVM\_INVALID\_TYPE](../jsvm-types-h/document.md#jsvm_status): invalid type. This code is returned if the value is not a JavaScript Proxy.

 |

#### \[h2\]OH\_JSVM\_OpenVMScope()

JSVM\_EXTERN JSVM\_Status OH\_JSVM\_OpenVMScope(JSVM\_VM vm,JSVM\_VMScope\* result)

**Description**

Opens a new VM scope for a VM instance.

**Since**: 11

**Parameters**

| Name | Description |
| :-- | :-- |
| [JSVM\_VM](../../structs/jsvm-vm/document.md) vm | Target VM instance. |
| [JSVM\_VMScope](../../structs/jsvm-vmscope/document.md)\* result | Pointer to the new VM scope. |

**Returns**

| Type | Description |
| :-- | :-- |
| JSVM\_EXTERN [JSVM\_Status](../jsvm-types-h/document.md#jsvm_status) | 
Returns a JSVM status code.

[JSVM\_OK](../jsvm-types-h/document.md#jsvm_status): operation successful.

 |

#### \[h2\]OH\_JSVM\_CloseVMScope()

JSVM\_EXTERN JSVM\_Status OH\_JSVM\_CloseVMScope(JSVM\_VM vm,JSVM\_VMScope scope)

**Description**

Closes the VM scope of a VM instance.

**Since**: 11

**Parameters**

| Name | Description |
| :-- | :-- |
| [JSVM\_VM](../../structs/jsvm-vm/document.md) vm | Target VM instance. |
| [JSVM\_VMScope](../../structs/jsvm-vmscope/document.md) scope | VM scope to be closed. |

**Returns**

| Type | Description |
| :-- | :-- |
| JSVM\_EXTERN [JSVM\_Status](../jsvm-types-h/document.md#jsvm_status) | 
Returns a JSVM status code.

[JSVM\_OK](../jsvm-types-h/document.md#jsvm_status): operation successful.

 |

#### \[h2\]OH\_JSVM\_CreateEnv()

JSVM\_EXTERN JSVM\_Status OH\_JSVM\_CreateEnv(JSVM\_VM vm,size\_t propertyCount,const JSVM\_PropertyDescriptor\* properties,JSVM\_Env\* result)

**Description**

Creates a new environment based on the optional properties of the new context.

**Since**: 11

**Parameters**

| Name | Description |
| :-- | :-- |
| [JSVM\_VM](../../structs/jsvm-vm/document.md) vm | VM instance, in which the new environment will be created. |
| size\_t propertyCount | Number of elements in the property array. |
| [const JSVM\_PropertyDescriptor](../../structs/jsvm-propertydescriptor/document.md)\* properties | Pointer to the array of property descriptors. |
| [JSVM\_Env](../../structs/jsvm-env/document.md)\* result | Pointer to the new environment. |

**Returns**

| Type | Description |
| :-- | :-- |
| JSVM\_EXTERN [JSVM\_Status](../jsvm-types-h/document.md#jsvm_status) | 
Returns a JSVM status code.

[JSVM\_OK](../jsvm-types-h/document.md#jsvm_status): operation successful.

 |

#### \[h2\]OH\_JSVM\_CreateEnvFromSnapshot()

JSVM\_EXTERN JSVM\_Status OH\_JSVM\_CreateEnvFromSnapshot(JSVM\_VM vm,size\_t index,JSVM\_Env\* result)

**Description**

Creates a new environment based on the startup snapshot of the VM.

**Since**: 11

**Parameters**

| Name | Description |
| :-- | :-- |
| [JSVM\_VM](../../structs/jsvm-vm/document.md) vm | VM instance, in which the new environment will be created. |
| size\_t index | Index of the environment in the snapshot. |
| [JSVM\_Env](../../structs/jsvm-env/document.md)\* result | Pointer to the new environment. |

**Returns**

| Type | Description |
| :-- | :-- |
| JSVM\_EXTERN [JSVM\_Status](../jsvm-types-h/document.md#jsvm_status) | 
Returns a JSVM status code.

[JSVM\_OK](../jsvm-types-h/document.md#jsvm_status): operation successful.

[JSVM\_GENERIC\_FAILURE](../jsvm-types-h/document.md#jsvm_status): generic failure due to unknown reasons.

 |

#### \[h2\]OH\_JSVM\_DestroyEnv()

JSVM\_EXTERN JSVM\_Status OH\_JSVM\_DestroyEnv(JSVM\_Env env)

**Description**

Destroys the environment.

**Since**: 11

**Parameters**

| Name | Description |
| :-- | :-- |
| [JSVM\_Env](../../structs/jsvm-env/document.md) env | Environment to be destroyed. |

**Returns**

| Type | Description |
| :-- | :-- |
| JSVM\_EXTERN [JSVM\_Status](../jsvm-types-h/document.md#jsvm_status) | 
Returns a JSVM status code.

[JSVM\_OK](../jsvm-types-h/document.md#jsvm_status): operation successful.

 |

#### \[h2\]OH\_JSVM\_OpenEnvScope()

JSVM\_EXTERN JSVM\_Status OH\_JSVM\_OpenEnvScope(JSVM\_Env env,JSVM\_EnvScope\* result)

**Description**

Opens a new environment scope.

**Since**: 11

**Parameters**

| Name | Description |
| :-- | :-- |
| [JSVM\_Env](../../structs/jsvm-env/document.md) env | Target environment in which the JSVM-API will be called. |
| [JSVM\_EnvScope](../../structs/jsvm-envscope/document.md)\* result | Pointer to the new environment scope. |

**Returns**

| Type | Description |
| :-- | :-- |
| JSVM\_EXTERN [JSVM\_Status](../jsvm-types-h/document.md#jsvm_status) | 
Returns a JSVM status code.

[JSVM\_OK](../jsvm-types-h/document.md#jsvm_status): operation successful.

 |

#### \[h2\]OH\_JSVM\_CloseEnvScope()

JSVM\_EXTERN JSVM\_Status OH\_JSVM\_CloseEnvScope(JSVM\_Env env,JSVM\_EnvScope scope)

**Description**

Closes the environment scope.

**Since**: 11

**Parameters**

| Name | Description |
| :-- | :-- |
| [JSVM\_Env](../../structs/jsvm-env/document.md) env | Target environment in which the JSVM-API will be called. |
| [JSVM\_EnvScope](../../structs/jsvm-envscope/document.md) scope | Environment scope to be closed. |

**Returns**

| Type | Description |
| :-- | :-- |
| JSVM\_EXTERN [JSVM\_Status](../jsvm-types-h/document.md#jsvm_status) | 
Returns a JSVM status code.

[JSVM\_OK](../jsvm-types-h/document.md#jsvm_status): operation successful.

 |

#### \[h2\]OH\_JSVM\_GetVM()

JSVM\_EXTERN JSVM\_Status OH\_JSVM\_GetVM(JSVM\_Env env,JSVM\_VM\* result)

**Description**

Obtains a VM instance.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [JSVM\_Env](../../structs/jsvm-env/document.md) env | Target environment in which the JSVM-API will be called. |
| [JSVM\_VM](../../structs/jsvm-vm/document.md)\* result | Pointer to the VM instance of the specified environment. |

**Returns**

| Type | Description |
| :-- | :-- |
| JSVM\_EXTERN [JSVM\_Status](../jsvm-types-h/document.md#jsvm_status) | 
Returns a JSVM status code.

[JSVM\_OK](../jsvm-types-h/document.md#jsvm_status): operation successful.

 |

#### \[h2\]OH\_JSVM\_CompileScript()

JSVM\_EXTERN JSVM\_Status OH\_JSVM\_CompileScript(JSVM\_Env env,JSVM\_Value script,const uint8\_t\* cachedData,size\_t cacheDataLength,bool eagerCompile,bool\* cacheRejected,JSVM\_Script\* result)

**Description**

Compiles a JavaScript code snippet and returns the compiled script.

**Since**: 11

**Parameters**

| Name | Description |
| :-- | :-- |
| [JSVM\_Env](../../structs/jsvm-env/document.md) env | Target environment in which the JSVM-API will be called. |
| [JSVM\_Value](../../structs/jsvm-value/document.md) script | JavaScript code that includes the script to be compiled. |
| const uint8\_t\* cachedData | (Optional) Pointer to the code cache data of the script. |
| size\_t cacheDataLength | Length of the **cachedData** array. |
| bool eagerCompile | Whether to compile the script immediately. The value **true** indicates that the script should be compiled immediately, and **false** indicates the opposite. |
| bool\* cacheRejected | Pointer to the Boolean value, indicating whether the code cache is rejected. The value **true** indicates the code cache is rejected, and **false** indicates the opposite. |
| [JSVM\_Script](../../structs/jsvm-script/document.md)\* result | Pointer to the compiled script. |

**Returns**

| Type | Description |
| :-- | :-- |
| JSVM\_EXTERN [JSVM\_Status](../jsvm-types-h/document.md#jsvm_status) | 
Returns a JSVM status code.

[JSVM\_OK](../jsvm-types-h/document.md#jsvm_status): operation successful.

[JSVM\_INVALID\_ARG](../jsvm-types-h/document.md#jsvm_status): invalid argument. This code is returned if the input data is a null pointer. [JSVM\_STRING\_EXPECTED](../jsvm-types-h/document.md#jsvm_status): string expected. This code is returned if the input parameter is not of the string type.

[JSVM\_GENERIC\_FAILURE](../jsvm-types-h/document.md#jsvm_status): generic failure due to unknown reasons.

[JSVM\_CANNOT\_RUN\_JS](../jsvm-types-h/document.md#jsvm_status): JS execution failed.

[JSVM\_PENDING\_EXCEPTION](../jsvm-types-h/document.md#jsvm_status): pending exception.

 |

#### \[h2\]OH\_JSVM\_CompileScriptWithOrigin()

JSVM\_EXTERN JSVM\_Status OH\_JSVM\_CompileScriptWithOrigin(JSVM\_Env env,JSVM\_Value script,const uint8\_t\* cachedData,size\_t cacheDataLength,bool eagerCompile,bool\* cacheRejected,JSVM\_ScriptOrigin\* origin,JSVM\_Script\* result)

**Description**

Compiles a JavaScript code snippet that contains source map information and returns the compiled script.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [JSVM\_Env](../../structs/jsvm-env/document.md) env | Target environment in which the JSVM-API will be called. |
| [JSVM\_Value](../../structs/jsvm-value/document.md) script | JavaScript code that includes the script to be compiled. |
| const uint8\_t\* cachedData | (Optional) Pointer to the code cache data of the script. |
| size\_t cacheDataLength | Length of the **cachedData** array. |
| bool eagerCompile | Whether to compile the script immediately. The value **true** indicates that the script should be compiled immediately, and **false** indicates the opposite. |
| bool\* cacheRejected | Pointer to the Boolean value, indicating whether the code cache is rejected. The value **true** indicates the code cache is rejected, and **false** indicates the opposite. |
| [JSVM\_ScriptOrigin](../../structs/jsvm-scriptorigin/document.md)\* origin | Pointer to the source code information, including the source map location and source code file name. |
| [JSVM\_Script](../../structs/jsvm-script/document.md)\* result | Pointer to the compiled script. |

**Returns**

| Type | Description |
| :-- | :-- |
| JSVM\_EXTERN [JSVM\_Status](../jsvm-types-h/document.md#jsvm_status) | 
Returns a JSVM status code.

[JSVM\_OK](../jsvm-types-h/document.md#jsvm_status): operation successful.

[JSVM\_INVALID\_ARG](../jsvm-types-h/document.md#jsvm_status): invalid argument. This code is returned if the input data is a null pointer. [JSVM\_STRING\_EXPECTED](../jsvm-types-h/document.md#jsvm_status): string expected. This code is returned if the input parameter is not of the string type.

[JSVM\_GENERIC\_FAILURE](../jsvm-types-h/document.md#jsvm_status): generic failure.

[JSVM\_CANNOT\_RUN\_JS](../jsvm-types-h/document.md#jsvm_status): JS execution failed.

[JSVM\_PENDING\_EXCEPTION](../jsvm-types-h/document.md#jsvm_status): pending exception.

 |

#### \[h2\]OH\_JSVM\_CompileScriptWithOptions()

JSVM\_EXTERN JSVM\_Status OH\_JSVM\_CompileScriptWithOptions(JSVM\_Env env,JSVM\_Value script,size\_t optionCount,JSVM\_CompileOptions options\[\],JSVM\_Script\* result)

**Description**

Compiles a JavaScript code snippet and returns the compiled script.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [JSVM\_Env](../../structs/jsvm-env/document.md) env | Target environment in which the JSVM-API will be called. |
| [JSVM\_Value](../../structs/jsvm-value/document.md) script | JavaScript code that includes the script to be compiled. |
| size\_t optionCount | Length of the input options array. |
| JSVM\_CompileOptions options\[\] | Array of options, which stores all compilation options. |
| [JSVM\_Script](../../structs/jsvm-value/document.md)\* result | Pointer to the compiled script. |

**Returns**

| Type | Description |
| :-- | :-- |
| JSVM\_EXTERN [JSVM\_Status](../jsvm-types-h/document.md#jsvm_status) | 
Returns a JSVM status code.

[JSVM\_OK](../jsvm-types-h/document.md#jsvm_status): operation successful.

[JSVM\_INVALID\_ARG](../jsvm-types-h/document.md#jsvm_status): invalid argument. This code is returned if the input data is a null pointer.

[JSVM\_STRING\_EXPECTED](../jsvm-types-h/document.md#jsvm_status): string expected. This code is returned if the input parameter is not of the string type.

[JSVM\_GENERIC\_FAILURE](../jsvm-types-h/document.md#jsvm_status): generic failure due to unknown reasons.

[JSVM\_PENDING\_EXCEPTION](../jsvm-types-h/document.md#jsvm_status): pending exception.

 |

#### \[h2\]OH\_JSVM\_CreateCodeCache()

JSVM\_EXTERN JSVM\_Status OH\_JSVM\_CreateCodeCache(JSVM\_Env env,JSVM\_Script script,const uint8\_t\*\* data,size\_t\* length)

**Description**

Creates a code cache for the compiled script.

**Since**: 11

**Parameters**

| Name | Description |
| :-- | :-- |
| [JSVM\_Env](../../structs/jsvm-env/document.md) env | Target environment in which the JSVM-API will be called. |
| [JSVM\_Script](../../structs/jsvm-script/document.md) script | Target script. |
| const uint8\_t\*\* data | Double pointer to the code cache data. |
| size\_t\* length | Pointer to the length of the code cache data. |

**Returns**

| Type | Description |
| :-- | :-- |
| JSVM\_EXTERN [JSVM\_Status](../jsvm-types-h/document.md#jsvm_status) | 
Returns a JSVM status code.

[JSVM\_OK](../jsvm-types-h/document.md#jsvm_status): operation successful.

[JSVM\_GENERIC\_FAILURE](../jsvm-types-h/document.md#jsvm_status): generic failure.

 |

#### \[h2\]OH\_JSVM\_RunScript()

JSVM\_EXTERN JSVM\_Status OH\_JSVM\_RunScript(JSVM\_Env env,JSVM\_Script script,JSVM\_Value\* result)

**Description**

Runs a JavaScript code snippet and returns its result, including the following precautions: Unlike eval, this function does not allow the script to access the current lexical scope, and therefore does not allow the script to access the module scope. This means that pseudo-global variables such as **require** will be unavailable. The script can access the global scope. The functions and variable declarations in the script will be added to the global object. Variable declarations using **let** and **const** are globally visible, but are not added to the global object. The value of **this** is **global** in the script. Without the JIT permission, the script containing WebAssembly fails to be executed. The performance varies in specific scenarios, and a log is printed to notify you.

**Since**: 11

**Parameters**

| Name | Description |
| :-- | :-- |
| [JSVM\_Env](../../structs/jsvm-env/document.md) env | Environment for calling the JSVM-API. |
| [JSVM\_Script](../../structs/jsvm-script/document.md) script | JavaScript string that includes the script to be executed. |
| [JSVM\_Value](../../structs/jsvm-value/document.md)\* result | Pointer to the value generated after the script is executed. |

**Returns**

| Type | Description |
| :-- | :-- |
| JSVM\_EXTERN [JSVM\_Status](../jsvm-types-h/document.md#jsvm_status) | 
Returns a JSVM status code.

[JSVM\_OK](../jsvm-types-h/document.md#jsvm_status): operation successful.

[JSVM\_GENERIC\_FAILURE](../jsvm-types-h/document.md#jsvm_status): generic failure.

[JSVM\_PENDING\_EXCEPTION](../jsvm-types-h/document.md#jsvm_status): pending exception.

 |

#### \[h2\]OH\_JSVM\_SetInstanceData()

JSVM\_EXTERN JSVM\_Status OH\_JSVM\_SetInstanceData(JSVM\_Env env,void\* data,JSVM\_Finalize finalizeCb,void\* finalizeHint)

**Description**

Sets instance data so that it is associated with the currently running JSVM environment. You can use **OH\_JSVM\_GetInstanceData()** to obtain data later. Any existing data set by a previous call to **OH\_JSVM\_SetInstanceData()** will be overwritten. If **finalizeCb** was previously provided, it will not be called.

**Since**: 11

**Parameters**

| Name | Description |
| :-- | :-- |
| [JSVM\_Env](../../structs/jsvm-env/document.md) env | Environment for calling the JSVM-API. |
| void\* data | Pointer to the data bound for this instance. |
| [JSVM\_Finalize](../jsvm-types-h/document.md#jsvm_finalize) finalizeCb | Function for destroying the environment. |
| void\* finalizeHint | Pointer to the optional hint passed to the **finalize** callback during garbage collection. |

**Returns**

| Type | Description |
| :-- | :-- |
| JSVM\_EXTERN [JSVM\_Status](../jsvm-types-h/document.md#jsvm_status) | 
Returns a JSVM status code.

[JSVM\_OK](../jsvm-types-h/document.md#jsvm_status): operation successful.

 |

#### \[h2\]OH\_JSVM\_GetInstanceData()

JSVM\_EXTERN JSVM\_Status OH\_JSVM\_GetInstanceData(JSVM\_Env env,void\*\* data)

**Description**

Obtains instance data that has been set by **OH\_JSVM\_SetInstanceData()**. If no associated data is set, this function is called successfully and **data** is set to **NULL**.

**Since**: 11

**Parameters**

| Name | Description |
| :-- | :-- |
| [JSVM\_Env](../../structs/jsvm-env/document.md) env | Environment for calling the JSVM-API. |
| void\*\* data | Double pointer to the data that has been set by **OH\_JSVM\_SetInstanceData()**, associated with the current JSVM environment. |

**Returns**

| Type | Description |
| :-- | :-- |
| JSVM\_EXTERN [JSVM\_Status](../jsvm-types-h/document.md#jsvm_status) | 
Returns a JSVM status code.

[JSVM\_OK](../jsvm-types-h/document.md#jsvm_status): operation successful.

 |

#### \[h2\]OH\_JSVM\_GetLastErrorInfo()

JSVM\_EXTERN JSVM\_Status OH\_JSVM\_GetLastErrorInfo(JSVM\_Env env,const JSVM\_ExtendedErrorInfo\*\* result)

**Description**

Obtains the **JSVM\_ExtendedErrorInfo** struct that contains the last error. The content of **JSVM\_ExtendedErrorInfo** returned is valid only before the JSVM-API function is called for the same environment. This includes a call to **OH\_JSVM\_IsExceptionPending**, so you may need to copy information for later use. The pointer returned in **error\_message** points to a statically defined string, so if you copy it from the **error\_message** field (which will be overwritten) before calling another JSVM-API function, you can safely use the pointer.

**Since**: 11

**Parameters**

| Name | Description |
| :-- | :-- |
| [JSVM\_Env](../../structs/jsvm-env/document.md) env | Environment for calling the JSVM-API. |
| [const JSVM\_ExtendedErrorInfo](../../structs/jsvm-extendederrorinfo/document.md)\*\* result | Double pointer to the **JSVM\_ExtendedErrorInfo** struct that contains more information about the error. |

**Returns**

| Type | Description |
| :-- | :-- |
| JSVM\_EXTERN [JSVM\_Status](../jsvm-types-h/document.md#jsvm_status) | 
Returns a JSVM status code.

[JSVM\_OK](../jsvm-types-h/document.md#jsvm_status): operation successful.

 |

#### \[h2\]OH\_JSVM\_Throw()

JSVM\_EXTERN JSVM\_Status OH\_JSVM\_Throw(JSVM\_Env env,JSVM\_Value error)

**Description**

Throws the provided JavaScript value.

**Since**: 11

**Parameters**

| Name | Description |
| :-- | :-- |
| [JSVM\_Env](../../structs/jsvm-env/document.md) env | Environment for calling the JSVM-API. |
| [JSVM\_Value](../../structs/jsvm-value/document.md) error | JavaScript error to be thrown. |

**Returns**

| Type | Description |
| :-- | :-- |
| JSVM\_EXTERN [JSVM\_Status](../jsvm-types-h/document.md#jsvm_status) | 
Returns a JSVM status code.

[JSVM\_OK](../jsvm-types-h/document.md#jsvm_status): operation successful.

 |

#### \[h2\]OH\_JSVM\_ThrowError()

JSVM\_EXTERN JSVM\_Status OH\_JSVM\_ThrowError(JSVM\_Env env,const char\* code,const char\* msg)

**Description**

Throws a JavaScript Error with the provided text.

**Since**: 11

**Parameters**

| Name | Description |
| :-- | :-- |
| [JSVM\_Env](../../structs/jsvm-env/document.md) env | Environment for calling the JSVM-API. |
| const char\* code | Pointer to the optional error code to be set on the error. |
| const char\* msg | Pointer to the C string representing the text associated with the error. |

**Returns**

| Type | Description |
| :-- | :-- |
| JSVM\_EXTERN [JSVM\_Status](../jsvm-types-h/document.md#jsvm_status) | 
Returns a JSVM status code.

[JSVM\_OK](../jsvm-types-h/document.md#jsvm_status): operation successful.

 |

#### \[h2\]OH\_JSVM\_ThrowTypeError()

JSVM\_EXTERN JSVM\_Status OH\_JSVM\_ThrowTypeError(JSVM\_Env env,const char\* code,const char\* msg)

**Description**

Throws a JavaScript TypeError with the provided text.

**Since**: 11

**Parameters**

| Name | Description |
| :-- | :-- |
| [JSVM\_Env](../../structs/jsvm-env/document.md) env | Environment for calling the JSVM-API. |
| const char\* code | Pointer to the optional error code to be set on the error. |
| const char\* msg | Pointer to the C string representing the text associated with the error. |

**Returns**

| Type | Description |
| :-- | :-- |
| JSVM\_EXTERN [JSVM\_Status](../jsvm-types-h/document.md#jsvm_status) | 
Returns a JSVM status code.

[JSVM\_OK](../jsvm-types-h/document.md#jsvm_status): operation successful.

 |

#### \[h2\]OH\_JSVM\_ThrowRangeError()

JSVM\_EXTERN JSVM\_Status OH\_JSVM\_ThrowRangeError(JSVM\_Env env,const char\* code,const char\* msg)

**Description**

Throws a JavaScript RangeError with the provided text.

**Since**: 11

**Parameters**

| Name | Description |
| :-- | :-- |
| [JSVM\_Env](../../structs/jsvm-env/document.md) env | Environment for calling the JSVM-API. |
| const char\* code | Pointer to the optional error code to be set on the error. |
| const char\* msg | Pointer to the C string representing the text associated with the error. |

**Returns**

| Type | Description |
| :-- | :-- |
| JSVM\_EXTERN [JSVM\_Status](../jsvm-types-h/document.md#jsvm_status) | 
Returns a JSVM status code.

[JSVM\_OK](../jsvm-types-h/document.md#jsvm_status): operation successful.

 |

#### \[h2\]OH\_JSVM\_ThrowSyntaxError()

JSVM\_EXTERN JSVM\_Status OH\_JSVM\_ThrowSyntaxError(JSVM\_Env env,const char\* code,const char\* msg)

**Description**

Throws a JavaScript SyntaxError with the provided text.

**Since**: 11

**Parameters**

| Name | Description |
| :-- | :-- |
| [JSVM\_Env](../../structs/jsvm-env/document.md) env | Environment for calling the JSVM-API. |
| const char\* code | Pointer to the optional error code to be set on the error. |
| const char\* msg | Pointer to the C string representing the text associated with the error. |

**Returns**

| Type | Description |
| :-- | :-- |
| JSVM\_EXTERN [JSVM\_Status](../jsvm-types-h/document.md#jsvm_status) | 
Returns a JSVM status code.

[JSVM\_OK](../jsvm-types-h/document.md#jsvm_status): operation successful.

 |

#### \[h2\]OH\_JSVM\_IsError()

JSVM\_EXTERN JSVM\_Status OH\_JSVM\_IsError(JSVM\_Env env,JSVM\_Value value,bool\* result)

**Description**

Checks whether the given **JSVM\_Value** indicates an error.

**Since**: 11

**Parameters**

| Name | Description |
| :-- | :-- |
| [JSVM\_Env](../../structs/jsvm-env/document.md) env | Environment for calling the JSVM-API. |
| [JSVM\_Value](../../structs/jsvm-value/document.md) value | **JSVM\_Value** to be checked. |
| bool\* result | Pointer to the check result. The value **true** means the **JSVM\_Value** indicates an error, and **false** means the opposite. |

**Returns**

| Type | Description |
| :-- | :-- |
| JSVM\_EXTERN [JSVM\_Status](../jsvm-types-h/document.md#jsvm_status) | 
Returns a JSVM status code.

[JSVM\_OK](../jsvm-types-h/document.md#jsvm_status): operation successful.

 |

#### \[h2\]OH\_JSVM\_CreateError()

JSVM\_EXTERN JSVM\_Status OH\_JSVM\_CreateError(JSVM\_Env env,JSVM\_Value code,JSVM\_Value msg,JSVM\_Value\* result)

**Description**

Creates a JavaScript Error with the provided text.

**Since**: 11

**Parameters**

| Name | Description |
| :-- | :-- |
| [JSVM\_Env](../../structs/jsvm-env/document.md) env | Environment for calling the JSVM-API. |
| [JSVM\_Value](../../structs/jsvm-value/document.md) code | Optional **JSVM\_Value**, which is a string with the associated error code. |
| [JSVM\_Value](../../structs/jsvm-value/document.md) msg | Message that references the JavaScript string as an error. |
| [JSVM\_Value](../../structs/jsvm-value/document.md)\* result | Pointer to the creation error. |

**Returns**

| Type | Description |
| :-- | :-- |
| JSVM\_EXTERN [JSVM\_Status](../jsvm-types-h/document.md#jsvm_status) | 
Returns a JSVM status code.

[JSVM\_OK](../jsvm-types-h/document.md#jsvm_status): operation successful.

[JSVM\_STRING\_EXPECTED](../jsvm-types-h/document.md#jsvm_status): string expected. This code is returned if the input parameter is not of the string type.

 |

#### \[h2\]OH\_JSVM\_CreateTypeError()

JSVM\_EXTERN JSVM\_Status OH\_JSVM\_CreateTypeError(JSVM\_Env env,JSVM\_Value code,JSVM\_Value msg,JSVM\_Value\* result)

**Description**

Creates a JavaScript TypeError with the provided text.

**Since**: 11

**Parameters**

| Name | Description |
| :-- | :-- |
| [JSVM\_Env](../../structs/jsvm-env/document.md) env | Environment for calling the JSVM-API. |
| [JSVM\_Value](../../structs/jsvm-value/document.md) code | Optional **JSVM\_Value**, which is a string with the associated error code. |
| [JSVM\_Value](../../structs/jsvm-value/document.md) msg | Message that references the JavaScript string as an error. |
| [JSVM\_Value](../../structs/jsvm-value/document.md)\* result | Pointer to the creation error. |

**Returns**

| Type | Description |
| :-- | :-- |
| JSVM\_EXTERN [JSVM\_Status](../jsvm-types-h/document.md#jsvm_status) | 
Returns a JSVM status code.

[JSVM\_OK](../jsvm-types-h/document.md#jsvm_status): operation successful.

[JSVM\_STRING\_EXPECTED](../jsvm-types-h/document.md#jsvm_status): string expected. This code is returned if the input parameter is not of the string type.

 |

#### \[h2\]OH\_JSVM\_CreateRangeError()

JSVM\_EXTERN JSVM\_Status OH\_JSVM\_CreateRangeError(JSVM\_Env env,JSVM\_Value code,JSVM\_Value msg,JSVM\_Value\* result)

**Description**

Creates a JavaScript RangeError with the provided text.

**Since**: 11

**Parameters**

| Name | Description |
| :-- | :-- |
| [JSVM\_Env](../../structs/jsvm-env/document.md) env | Environment for calling the JSVM-API. |
| [JSVM\_Value](../../structs/jsvm-value/document.md) code | Optional **JSVM\_Value**, which is a string with the associated error code. |
| [JSVM\_Value](../../structs/jsvm-value/document.md) msg | Message that references the JavaScript string as an error. |
| [JSVM\_Value](../../structs/jsvm-value/document.md)\* result | Pointer to the creation error. |

**Returns**

| Type | Description |
| :-- | :-- |
| JSVM\_EXTERN [JSVM\_Status](../jsvm-types-h/document.md#jsvm_status) | 
Returns a JSVM status code.

[JSVM\_OK](../jsvm-types-h/document.md#jsvm_status): operation successful.

[JSVM\_STRING\_EXPECTED](../jsvm-types-h/document.md#jsvm_status): string expected. This code is returned if the input parameter is not of the string type.

 |

#### \[h2\]OH\_JSVM\_CreateSyntaxError()

JSVM\_EXTERN JSVM\_Status OH\_JSVM\_CreateSyntaxError(JSVM\_Env env,JSVM\_Value code,JSVM\_Value msg,JSVM\_Value\* result)

**Description**

Creates a JavaScript SyntaxError with the provided text.

**Since**: 11

**Parameters**

| Name | Description |
| :-- | :-- |
| [JSVM\_Env](../../structs/jsvm-env/document.md) env | Environment for calling the JSVM-API. |
| [JSVM\_Value](../../structs/jsvm-value/document.md) code | Optional **JSVM\_Value**, which is a string with the associated error code. |
| [JSVM\_Value](../../structs/jsvm-value/document.md) msg | Message that references the JavaScript string as an error. |
| [JSVM\_Value](../../structs/jsvm-value/document.md)\* result | Pointer to the creation error. |

**Returns**

| Type | Description |
| :-- | :-- |
| JSVM\_EXTERN [JSVM\_Status](../jsvm-types-h/document.md#jsvm_status) | 
Returns a JSVM status code.

[JSVM\_OK](../jsvm-types-h/document.md#jsvm_status): operation successful.

[JSVM\_STRING\_EXPECTED](../jsvm-types-h/document.md#jsvm_status): string expected. This code is returned if the input parameter is not of the string type.

 |

#### \[h2\]OH\_JSVM\_GetAndClearLastException()

JSVM\_EXTERN JSVM\_Status OH\_JSVM\_GetAndClearLastException(JSVM\_Env env,JSVM\_Value\* result)

**Description**

Obtains and clears the last exception. If pending occurs, a JavaScript exception is returned. Otherwise, **NULL** is returned.

**Since**: 11

**Parameters**

| Name | Description |
| :-- | :-- |
| [JSVM\_Env](../../structs/jsvm-env/document.md) env | Environment for calling the JSVM-API. |
| [JSVM\_Value](../../structs/jsvm-value/document.md)\* result | Pointer to the exception. An exception is returned if pending occurs. Otherwise, **NULL** is returned. |

**Returns**

| Type | Description |
| :-- | :-- |
| JSVM\_EXTERN [JSVM\_Status](../jsvm-types-h/document.md#jsvm_status) | 
Returns a JSVM status code.

[JSVM\_OK](../jsvm-types-h/document.md#jsvm_status): operation successful.

 |

#### \[h2\]OH\_JSVM\_IsExceptionPending()

JSVM\_EXTERN JSVM\_Status OH\_JSVM\_IsExceptionPending(JSVM\_Env env,bool\* result)

**Description**

Checks whether the last exception is caused by pending. If yes, **true** is returned. Otherwise, **false** is returned.

**Since**: 11

**Parameters**

| Name | Description |
| :-- | :-- |
| [JSVM\_Env](../../structs/jsvm-env/document.md) env | Environment for calling the JSVM-API. |
| bool\* result | Pointer to the exception. The value **true** indicates the last exception is caused by pending, and **false** indicates the opposite. |

**Returns**

| Type | Description |
| :-- | :-- |
| JSVM\_EXTERN [JSVM\_Status](../jsvm-types-h/document.md#jsvm_status) | 
Returns a JSVM status code.

[JSVM\_OK](../jsvm-types-h/document.md#jsvm_status): operation successful.

 |

#### \[h2\]OH\_JSVM\_OpenHandleScope()

JSVM\_EXTERN JSVM\_Status OH\_JSVM\_OpenHandleScope(JSVM\_Env env,JSVM\_HandleScope\* result)

**Description**

Opens a new handle scope.

**Since**: 11

**Parameters**

| Name | Description |
| :-- | :-- |
| [JSVM\_Env](../../structs/jsvm-env/document.md) env | Environment for calling the JSVM-API. |
| [JSVM\_HandleScope](../../structs/jsvm-handlescope/document.md)\* result | Pointer to the new handle scope. |

**Returns**

| Type | Description |
| :-- | :-- |
| JSVM\_EXTERN [JSVM\_Status](../jsvm-types-h/document.md#jsvm_status) | 
Returns a JSVM status code.

[JSVM\_OK](../jsvm-types-h/document.md#jsvm_status): operation successful.

 |

#### \[h2\]OH\_JSVM\_CloseHandleScope()

JSVM\_EXTERN JSVM\_Status OH\_JSVM\_CloseHandleScope(JSVM\_Env env,JSVM\_HandleScope scope)

**Description**

(Mandatory) Closes the handle scope in the reverse order of opening it.

**Since**: 11

**Parameters**

| Name | Description |
| :-- | :-- |
| [JSVM\_Env](../../structs/jsvm-env/document.md) env | Environment for calling the JSVM-API. |
| [JSVM\_HandleScope](../../structs/jsvm-handlescope/document.md) scope | Handle scope to be closed. |

**Returns**

| Type | Description |
| :-- | :-- |
| JSVM\_EXTERN [JSVM\_Status](../jsvm-types-h/document.md#jsvm_status) | 
Returns a JSVM status code.

[JSVM\_OK](../jsvm-types-h/document.md#jsvm_status): operation successful.

[JSVM\_HANDLE\_SCOPE\_MISMATCH](../jsvm-types-h/document.md#jsvm_status): handle scope mismatch.

 |

#### \[h2\]OH\_JSVM\_OpenEscapableHandleScope()

JSVM\_EXTERN JSVM\_Status OH\_JSVM\_OpenEscapableHandleScope(JSVM\_Env env,JSVM\_EscapableHandleScope\* result)

**Description**

Opens an escapable handle scope.

**Since**: 11

**Parameters**

| Name | Description |
| :-- | :-- |
| [JSVM\_Env](../../structs/jsvm-env/document.md) env | Environment for calling the JSVM-API. |
| [JSVM\_EscapableHandleScope](../../structs/jsvm-escapablehandlescope/document.md)\* result | Pointer to the new escapable handle scope. |

**Returns**

| Type | Description |
| :-- | :-- |
| JSVM\_EXTERN [JSVM\_Status](../jsvm-types-h/document.md#jsvm_status) | 
Returns a JSVM status code.

[JSVM\_OK](../jsvm-types-h/document.md#jsvm_status): operation successful.

 |

#### \[h2\]OH\_JSVM\_CloseEscapableHandleScope()

JSVM\_EXTERN JSVM\_Status OH\_JSVM\_CloseEscapableHandleScope(JSVM\_Env env,JSVM\_EscapableHandleScope scope)

**Description**

(Mandatory) Closes the escapable handle scope in the reverse order of opening it. This JSVM\_API can be called even if there is a pending JavaScript exception.

**Since**: 11

**Parameters**

| Name | Description |
| :-- | :-- |
| [JSVM\_Env](../../structs/jsvm-env/document.md) env | Environment for calling the JSVM-API. |
| [JSVM\_EscapableHandleScope](../../structs/jsvm-escapablehandlescope/document.md) scope | Escapable handle scope to be closed. |

**Returns**

| Type | Description |
| :-- | :-- |
| JSVM\_EXTERN [JSVM\_Status](../jsvm-types-h/document.md#jsvm_status) | 
Returns a JSVM status code.

[JSVM\_OK](../jsvm-types-h/document.md#jsvm_status): operation successful.

[JSVM\_HANDLE\_SCOPE\_MISMATCH](../jsvm-types-h/document.md#jsvm_status): handle scope mismatch.

 |

#### \[h2\]OH\_JSVM\_EscapeHandle()

JSVM\_EXTERN JSVM\_Status OH\_JSVM\_EscapeHandle(JSVM\_Env env,JSVM\_EscapableHandleScope scope,JSVM\_Value escapee,JSVM\_Value\* result)

**Description**

Escapes a handle of a JavaScript object so that it is valid through the lifecycle of the outer scope. Each scope can be called only once. If it is called for multiple times, an error is returned.

**Since**: 11

**Parameters**

| Name | Description |
| :-- | :-- |
| [JSVM\_Env](../../structs/jsvm-env/document.md) env | Environment for calling the JSVM-API. |
| [JSVM\_EscapableHandleScope](../../structs/jsvm-escapablehandlescope/document.md) scope | Current scope. |
| [JSVM\_Value](../../structs/jsvm-value/document.md) escapee | JavaScript object to be escaped. |
| [JSVM\_Value](../../structs/jsvm-value/document.md)\* result | Pointer to the handle to be escaped. |

**Returns**

| Type | Description |
| :-- | :-- |
| JSVM\_EXTERN [JSVM\_Status](../jsvm-types-h/document.md#jsvm_status) | 
Returns a JSVM status code.

[JSVM\_OK](../jsvm-types-h/document.md#jsvm_status): operation successful.

[JSVM\_ESCAPE\_CALLED\_TWICE](../jsvm-types-h/document.md#jsvm_status): escape called twice. This code is returned if the scope object is closed.

 |

#### \[h2\]OH\_JSVM\_CreateReference()

JSVM\_EXTERN JSVM\_Status OH\_JSVM\_CreateReference(JSVM\_Env env,JSVM\_Value value,uint32\_t initialRefcount,JSVM\_Ref\* result)

**Description**

Creates a reference with the specified reference count for the input value.

**Since**: 11

**Parameters**

| Name | Description |
| :-- | :-- |
| [JSVM\_Env](../../structs/jsvm-env/document.md) env | Environment for calling the JSVM-API. |
| [JSVM\_Value](../../structs/jsvm-value/document.md) value | JSVM value for which a reference is being created. |
| uint32\_t initialRefcount | Initial reference count of a new reference. |
| [JSVM\_Ref](../../structs/jsvm-ref/document.md)\* result | Pointer to a new reference. |

**Returns**

| Type | Description |
| :-- | :-- |
| JSVM\_EXTERN [JSVM\_Status](../jsvm-types-h/document.md#jsvm_status) | 
Returns a JSVM status code.

[JSVM\_OK](../jsvm-types-h/document.md#jsvm_status): operation successful.

 |

#### \[h2\]OH\_JSVM\_DeleteReference()

JSVM\_EXTERN JSVM\_Status OH\_JSVM\_DeleteReference(JSVM\_Env env,JSVM\_Ref ref)

**Description**

Deletes the input reference.

**Since**: 11

**Parameters**

| Name | Description |
| :-- | :-- |
| [JSVM\_Env](../../structs/jsvm-env/document.md) env | Environment for calling the JSVM-API. |
| [JSVM\_Ref](../../structs/jsvm-ref/document.md) ref | Reference to be deleted. |

**Returns**

| Type | Description |
| :-- | :-- |
| JSVM\_EXTERN [JSVM\_Status](../jsvm-types-h/document.md#jsvm_status) | 
Returns a JSVM status code.

[JSVM\_OK](../jsvm-types-h/document.md#jsvm_status): operation successful.

 |

#### \[h2\]OH\_JSVM\_ReferenceRef()

JSVM\_EXTERN JSVM\_Status OH\_JSVM\_ReferenceRef(JSVM\_Env env,JSVM\_Ref ref,uint32\_t\* result)

**Description**

Increases the reference count and returns the new reference count.

**Since**: 11

**Parameters**

| Name | Description |
| :-- | :-- |
| [JSVM\_Env](../../structs/jsvm-env/document.md) env | Environment for calling the JSVM-API. |
| [JSVM\_Ref](../../structs/jsvm-ref/document.md) ref | Input reference. Its reference count will increase. |
| uint32\_t\* result | Pointer to the new reference count. |

**Returns**

| Type | Description |
| :-- | :-- |
| JSVM\_EXTERN [JSVM\_Status](../jsvm-types-h/document.md#jsvm_status) | 
Returns a JSVM status code.

[JSVM\_OK](../jsvm-types-h/document.md#jsvm_status): operation successful.

 |

#### \[h2\]OH\_JSVM\_ReferenceUnref()

JSVM\_EXTERN JSVM\_Status OH\_JSVM\_ReferenceUnref(JSVM\_Env env,JSVM\_Ref ref,uint32\_t\* result)

**Description**

Decreases the reference count and returns the new reference count.

**Since**: 11

**Parameters**

| Name | Description |
| :-- | :-- |
| [JSVM\_Env](../../structs/jsvm-env/document.md) env | Environment for calling the JSVM-API. |
| [JSVM\_Ref](../../structs/jsvm-ref/document.md) ref | Input reference. Its reference count will decrease. |
| uint32\_t\* result | Pointer to the new reference count. |

**Returns**

| Type | Description |
| :-- | :-- |
| JSVM\_EXTERN [JSVM\_Status](../jsvm-types-h/document.md#jsvm_status) | 
Returns a JSVM status code.

[JSVM\_OK](../jsvm-types-h/document.md#jsvm_status): operation successful.

[JSVM\_GENERIC\_FAILURE](../jsvm-types-h/document.md#jsvm_status): generic failure.

 |

#### \[h2\]OH\_JSVM\_GetReferenceValue()

JSVM\_EXTERN JSVM\_Status OH\_JSVM\_GetReferenceValue(JSVM\_Env env,JSVM\_Ref ref,JSVM\_Value\* result)

**Description**

Obtains the **JSVM\_Value** returned by the JSVM-API, which is the JavaScript value associated with **JSVM\_Ref**. If the value is invalid, **NULL** is returned.

**Since**: 11

**Parameters**

| Name | Description |
| :-- | :-- |
| [JSVM\_Env](../../structs/jsvm-env/document.md) env | Environment for calling the JSVM-API. |
| [JSVM\_Ref](../../structs/jsvm-ref/document.md) ref | JSVM reference for requesting the corresponding value. |
| [JSVM\_Value](../../structs/jsvm-value/document.md)\* result | Pointer to the **JSVM\_Value** referenced by **JSVM\_Ref**. |

**Returns**

| Type | Description |
| :-- | :-- |
| JSVM\_EXTERN [JSVM\_Status](../jsvm-types-h/document.md#jsvm_status) | 
Returns a JSVM status code.

[JSVM\_OK](../jsvm-types-h/document.md#jsvm_status): operation successful.

 |

#### \[h2\]OH\_JSVM\_CreateArray()

JSVM\_EXTERN JSVM\_Status OH\_JSVM\_CreateArray(JSVM\_Env env,JSVM\_Value\* result)

**Description**

Creates an array. This API returns the JSVM-API value of the JavaScript Array type.

**Since**: 11

**Parameters**

| Name | Description |
| :-- | :-- |
| [JSVM\_Env](../../structs/jsvm-env/document.md) env | Environment for calling the JSVM-API. |
| [JSVM\_Value](../../structs/jsvm-value/document.md)\* result | Pointer to the JSVM value of the JavaScript Array type. |

**Returns**

| Type | Description |
| :-- | :-- |
| JSVM\_EXTERN [JSVM\_Status](../jsvm-types-h/document.md#jsvm_status) | 
Returns a JSVM status code.

[JSVM\_OK](../jsvm-types-h/document.md#jsvm_status): operation successful.

 |

#### \[h2\]OH\_JSVM\_CreateArrayWithLength()

JSVM\_EXTERN JSVM\_Status OH\_JSVM\_CreateArrayWithLength(JSVM\_Env env,size\_t length,JSVM\_Value\* result)

**Description**

Creates an array with a specified length. This API returns the JSVM-API value of the JavaScript Array type. The **length** property of the array is set to the input **length** parameter. However, there is no guarantee that the underlying buffer is pre-allocated by the VM when the array is created. This behavior is implemented by the underlying VM.

**Since**: 11

**Parameters**

| Name | Description |
| :-- | :-- |
| [JSVM\_Env](../../structs/jsvm-env/document.md) env | Environment for calling the JSVM-API. |
| size\_t length | Initial length of the array. |
| [JSVM\_Value](../../structs/jsvm-value/document.md)\* result | Pointer to the JSVM value of the JavaScript Array type. |

**Returns**

| Type | Description |
| :-- | :-- |
| JSVM\_EXTERN [JSVM\_Status](../jsvm-types-h/document.md#jsvm_status) | 
Returns a JSVM status code.

[JSVM\_OK](../jsvm-types-h/document.md#jsvm_status): operation successful.

 |

#### \[h2\]OH\_JSVM\_CreateArraybuffer()

JSVM\_EXTERN JSVM\_Status OH\_JSVM\_CreateArraybuffer(JSVM\_Env env,size\_t byteLength,void\*\* data,JSVM\_Value\* result)

**Description**

Creates an array buffer. This API returns the JSVM-API value of the JavaScript ArrayBuffer type. ArrayBuffer is used to represent a fixed-length binary data buffer. It is usually used as the backup buffer of the **TypedArray** object. The allocated ArrayBuffer has an underlying byte buffer whose size is determined by the **length** parameter. The underlying buffer can be returned to and operated by the caller. This buffer can only be written directly from the native code. To write data from JavaScript to this buffer, you need to create a **TypedArray** or **DataView** object.

**Since**: 11

**Parameters**

| Name | Description |
| :-- | :-- |
| [JSVM\_Env](../../structs/jsvm-env/document.md) env | Environment for calling the JSVM-API. |
| size\_t byteLength | Length of the array buffer to be created, in bytes. |
| void\*\* data | Double pointer to the underlying byte buffer of the ArrayBuffer. **data** can be ignored by passing **NULL** to it. |
| [JSVM\_Value](../../structs/jsvm-value/document.md)\* result | Pointer to the JSVM value of the JavaScript ArrayBuffer. |

**Returns**

| Type | Description |
| :-- | :-- |
| JSVM\_EXTERN [JSVM\_Status](../jsvm-types-h/document.md#jsvm_status) | 
Returns a JSVM status code.

[JSVM\_OK](../jsvm-types-h/document.md#jsvm_status): operation successful.

[JSVM\_PENDING\_EXCEPTION](../jsvm-types-h/document.md#jsvm_status): pending exception.

 |

#### \[h2\]OH\_JSVM\_AllocateArrayBufferBackingStoreData()

JSVM\_EXTERN JSVM\_Status OH\_JSVM\_AllocateArrayBufferBackingStoreData(size\_t byteLength,JSVM\_InitializedFlag initialized,void \*\*data)

**Description**

Allocates a segment of BackingStore memory to the array buffer.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| size\_t byteLength | Size of the BackingStore memory. |
| [JSVM\_InitializedFlag](../jsvm-types-h/document.md#jsvm_initializedflag) initialized | Mode of initializing the BackingStore memory. |
| void \*\*data | Double pointer to the address of allocated BackingStore memory. |

**Returns**

| Type | Description |
| :-- | :-- |
| [JSVM\_Status](../jsvm-types-h/document.md#jsvm_status) JSVM\_CDECL | 
Returns a JSVM status code.

[JSVM\_OK](../jsvm-types-h/document.md#jsvm_status): operation successful.

[JSVM\_INVALID\_ARG](../jsvm-types-h/document.md#jsvm_status): invalid argument. This code is returned if the input data is a null pointer.

[JSVM\_GENERIC\_FAILURE](../jsvm-types-h/document.md#jsvm_status): generic failure. This code is returned if the memory application fails.

 |

#### \[h2\]OH\_JSVM\_FreeArrayBufferBackingStoreData()

JSVM\_EXTERN JSVM\_Status OH\_JSVM\_FreeArrayBufferBackingStoreData(void \*data)

**Description**

Frees the BackingStore memory allocated by **OH\_JSVM\_AllocateArrayBufferBackingStoreData**.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| void \*data | Pointer to the allocated BackingStore memory. |

**Returns**

| Type | Description |
| :-- | :-- |
| [JSVM\_Status](../jsvm-types-h/document.md#jsvm_status) JSVM\_CDECL | 
Returns a JSVM status code.

[JSVM\_OK](../jsvm-types-h/document.md#jsvm_status): operation successful.

[JSVM\_INVALID\_ARG](../jsvm-types-h/document.md#jsvm_status): invalid argument. This code is returned if the input data is a null pointer.

 |

#### \[h2\]OH\_JSVM\_CreateArrayBufferFromBackingStoreData()

JSVM\_EXTERN JSVM\_Status OH\_JSVM\_CreateArrayBufferFromBackingStoreData(JSVM\_Env env,void \*data,size\_t backingStoreSize,size\_t offset,size\_t arrayBufferSize,JSVM\_Value \*result)

**Description**

Creates an array buffer in the allocated BackingStore memory.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [JSVM\_Env](../../structs/jsvm-env/document.md) env | Environment for calling the JSVM-API. |
| void \*data | Pointer to the allocated BackingStore memory. |
| size\_t backingStoreSize | Size of the BackingStore memory. |
| size\_t offset | Relative offset between the start position of the array buffer in the memory and the memory header, in bytes. |
| size\_t arrayBufferSize | Size of the array buffer, in bytes. |
| [JSVM\_Value](../../structs/jsvm-value/document.md) \*result | Pointer to the array buffer address. |

**Returns**

| Type | Description |
| :-- | :-- |
| [JSVM\_Status](../jsvm-types-h/document.md#jsvm_status) JSVM\_CDECL | 
Returns a JSVM status code.

[JSVM\_OK](../jsvm-types-h/document.md#jsvm_status): operation successful.

[JSVM\_INVALID\_ARG](../jsvm-types-h/document.md#jsvm_status): invalid argument. This code is returned if one of the following exceptions occurs:

1\. The sum of **offset** and **arrayBufferSize** is larger than **backingStoreSize**.

2\. The value of **backingStoreSize** or **arrayBufferSize** is **0**.

3\. **data** or **result** is null.

 |

#### \[h2\]OH\_JSVM\_CreateDate()

JSVM\_EXTERN JSVM\_Status OH\_JSVM\_CreateDate(JSVM\_Env env,double time,JSVM\_Value\* result)

**Description**

Creates a date. This API ignores leap seconds because ECMAScript complies with the POSIX time specifications.

**Since**: 11

**Parameters**

| Name | Description |
| :-- | :-- |
| [JSVM\_Env](../../structs/jsvm-env/document.md) env | Environment for calling the JSVM-API. |
| double time | ECMAScript time since 00:00:00 UTC on January 1, 1970, in milliseconds. |
| [JSVM\_Value](../../structs/jsvm-value/document.md)\* result | Pointer to the **JSVM\_Value** of the JavaScript **Date** object. |

**Returns**

| Type | Description |
| :-- | :-- |
| JSVM\_EXTERN [JSVM\_Status](../jsvm-types-h/document.md#jsvm_status) | 
Returns a JSVM status code.

[JSVM\_OK](../jsvm-types-h/document.md#jsvm_status): operation successful.

[JSVM\_GENERIC\_FAILURE](../jsvm-types-h/document.md#jsvm_status): generic failure.

[JSVM\_PENDING\_EXCEPTION](../jsvm-types-h/document.md#jsvm_status): pending exception.

 |

#### \[h2\]OH\_JSVM\_CreateExternal()

JSVM\_EXTERN JSVM\_Status OH\_JSVM\_CreateExternal(JSVM\_Env env,void\* data,JSVM\_Finalize finalizeCb,void\* finalizeHint,JSVM\_Value\* result)

**Description**

Creates a JavaScript value with external data. This is used to pass external data through JavaScript code. You can use **OH\_JSVM\_GetValueExternal** to retrieve the value from the native code. This API adds a **JSVM\_Finalize** callback, which will be called when the newly created JavaScript object is garbage-collected. The created value is not an object, so it does not support additional properties. It is considered as a unique value type: Calling **OH\_JSVM\_Typeof()** with an external value generates **JSVM\_EXTERNAL**.

**Since**: 11

**Parameters**

| Name | Description |
| :-- | :-- |
| [JSVM\_Env](../../structs/jsvm-env/document.md) env | Environment for calling the JSVM-API. |
| void\* data | Raw pointer to external data. |
| [JSVM\_Finalize](../jsvm-types-h/document.md#jsvm_finalize) finalizeCb | Optional callback used to collect external values. **JSVM\_Finalize** provides more details. |
| void\* finalizeHint | Pointer to the optional hint passed to the **finalize** callback during garbage collection. |
| [JSVM\_Value](../../structs/jsvm-value/document.md)\* result | Pointer to the **JSVM\_Value** of an external value. |

**Returns**

| Type | Description |
| :-- | :-- |
| JSVM\_EXTERN [JSVM\_Status](../jsvm-types-h/document.md#jsvm_status) | 
Returns a JSVM status code.

[JSVM\_OK](../jsvm-types-h/document.md#jsvm_status): operation successful.

 |

#### \[h2\]OH\_JSVM\_CreateObject()

JSVM\_EXTERN JSVM\_Status OH\_JSVM\_CreateObject(JSVM\_Env env,JSVM\_Value\* result)

**Description**

Creates a default JavaScript object. This function is equivalent to executing **new Object()** in JavaScript.

**Since**: 11

**Parameters**

| Name | Description |
| :-- | :-- |
| [JSVM\_Env](../../structs/jsvm-env/document.md) env | Environment for calling the JSVM-API. |
| [JSVM\_Value](../../structs/jsvm-value/document.md)\* result | Pointer to the **JSVM\_Value** of the JavaScript object. |

**Returns**

| Type | Description |
| :-- | :-- |
| JSVM\_EXTERN [JSVM\_Status](../jsvm-types-h/document.md#jsvm_status) | 
Returns a JSVM status code.

[JSVM\_OK](../jsvm-types-h/document.md#jsvm_status): operation successful.

 |

#### \[h2\]OH\_JSVM\_CreateSymbol()

JSVM\_EXTERN JSVM\_Status OH\_JSVM\_CreateSymbol(JSVM\_Env env,JSVM\_Value description,JSVM\_Value\* result)

**Description**

Creates a JavaScript symbol value with a UTF-8-encoded C string.

**Since**: 11

**Parameters**

| Name | Description |
| :-- | :-- |
| [JSVM\_Env](../../structs/jsvm-env/document.md) env | Environment for calling the JSVM-API. |
| [JSVM\_Value](../../structs/jsvm-value/document.md) description | Optional **JSVM\_Value**, which refers to the JavaScript string to be set to the symbol description. |
| [JSVM\_Value](../../structs/jsvm-value/document.md)\* result | Pointer to the **JSVM\_Value** of the JavaScript symbol. |

**Returns**

| Type | Description |
| :-- | :-- |
| JSVM\_EXTERN [JSVM\_Status](../jsvm-types-h/document.md#jsvm_status) | 
Returns a JSVM status code.

[JSVM\_OK](../jsvm-types-h/document.md#jsvm_status): operation successful.

[JSVM\_STRING\_EXPECTED](../jsvm-types-h/document.md#jsvm_status): string expected. This code is returned if the input parameter is not of the string type.

 |

#### \[h2\]OH\_JSVM\_SymbolFor()

JSVM\_EXTERN JSVM\_Status OH\_JSVM\_SymbolFor(JSVM\_Env env,const char\* utf8description,size\_t length,JSVM\_Value\* result)

**Description**

Searches the global registry for an existing symbol with the given description. This API returns the symbol if it already exists; otherwise, a symbol is created in the registry.

**Since**: 11

**Parameters**

| Name | Description |
| :-- | :-- |
| [JSVM\_Env](../../structs/jsvm-env/document.md) env | Environment for calling the JSVM-API. |
| const char\* utf8description | Pointer to the symbol description that is in a UTF-8-encoded C string. |
| size\_t length | Length of the description string, in bytes. If it is null-terminated, the value is **JSVM\_AUTO\_LENGTH**. |
| [JSVM\_Value](../../structs/jsvm-value/document.md)\* result | Pointer to the **JSVM\_Value** of the JavaScript symbol. |

**Returns**

| Type | Description |
| :-- | :-- |
| JSVM\_EXTERN [JSVM\_Status](../jsvm-types-h/document.md#jsvm_status) | 
Returns a JSVM status code.

[JSVM\_OK](../jsvm-types-h/document.md#jsvm_status): operation successful.

 |

#### \[h2\]OH\_JSVM\_CreateTypedarray()

JSVM\_EXTERN JSVM\_Status OH\_JSVM\_CreateTypedarray(JSVM\_Env env,JSVM\_TypedarrayType type,size\_t length,JSVM\_Value arraybuffer,size\_t byteOffset,JSVM\_Value\* result)

**Description**

Creates a JavaScript **TypedArray** object based on an existing **ArrayBuffer** object. The **TypedArray** object provides an array-like view on the underlying data buffer, where each element has the same underlying binary scalar data type. The value of "**length** × element scalar bytes + **byteOffset**" must not be greater than the value of **ByteLength()** of the input array. Otherwise, a range error is thrown.

**Since**: 11

**Parameters**

| Name | Description |
| :-- | :-- |
| [JSVM\_Env](../../structs/jsvm-env/document.md) env | Environment for calling the JSVM-API. |
| [JSVM\_TypedarrayType](../jsvm-types-h/document.md#jsvm_typedarraytype) type | Scalar data type of an element in **TypedArray**. |
| size\_t length | Number of elements in **TypedArray**. |
| [JSVM\_Value](../../structs/jsvm-value/document.md) arraybuffer | ArrayBuffer, which is the basis of **TypedArray**. |
| size\_t byteOffset | Byte offset for the start position of mapping **TypedArray** in the ArrayBuffer. |
| [JSVM\_Value](../../structs/jsvm-value/document.md)\* result | Pointer to the **JSVM\_Value** of the JavaScript **TypedArray**. |

**Returns**

| Type | Description |
| :-- | :-- |
| JSVM\_EXTERN [JSVM\_Status](../jsvm-types-h/document.md#jsvm_status) | 
Returns a JSVM status code.

[JSVM\_OK](../jsvm-types-h/document.md#jsvm_status): operation successful.

[JSVM\_INVALID\_ARG](../jsvm-types-h/document.md#jsvm_status): invalid argument.

[JSVM\_PENDING\_EXCEPTION](../jsvm-types-h/document.md#jsvm_status): pending exception.

 |

#### \[h2\]OH\_JSVM\_CreateDataview()

JSVM\_EXTERN JSVM\_Status OH\_JSVM\_CreateDataview(JSVM\_Env env,size\_t length,JSVM\_Value arraybuffer,size\_t byteOffset,JSVM\_Value\* result)

**Description**

Creates a JavaScript **DataView** object based on an existing **ArrayBuffer** object. The **DataView** object provides an array-like view on the underlying data buffer, where elements can have different sizes and types. The sum of the binary length and byte offset cannot be greater than the size (in bytes) of the input array. Otherwise, a range error is thrown.

**Since**: 11

**Parameters**

| Name | Description |
| :-- | :-- |
| [JSVM\_Env](../../structs/jsvm-env/document.md) env | Environment for calling the JSVM-API. |
| size\_t length | Number of elements in **DataView**. |
| [JSVM\_Value](../../structs/jsvm-value/document.md) arraybuffer | ArrayBuffer at the bottom layer of the **DataView**. |
| size\_t byteOffset | Byte offset in the ArrayBuffer, indicating the start position of mapping a **DataView**. |
| [JSVM\_Value](../../structs/jsvm-value/document.md)\* result | Pointer to the **JSVM\_Value** of the JavaScript **DataView** object. |

**Returns**

| Type | Description |
| :-- | :-- |
| JSVM\_EXTERN [JSVM\_Status](../jsvm-types-h/document.md#jsvm_status) | 
Returns a JSVM status code.

[JSVM\_OK](../jsvm-types-h/document.md#jsvm_status): operation successful.

[JSVM\_INVALID\_ARG](../jsvm-types-h/document.md#jsvm_status): invalid argument.

[JSVM\_PENDING\_EXCEPTION](../jsvm-types-h/document.md#jsvm_status): pending exception.

 |

#### \[h2\]OH\_JSVM\_CreateInt32()

JSVM\_EXTERN JSVM\_Status OH\_JSVM\_CreateInt32(JSVM\_Env env,int32\_t value,JSVM\_Value\* result)

**Description**

Converts a value of the C int32\_t type to a value of the JavaScript number type.

**Since**: 11

**Parameters**

| Name | Description |
| :-- | :-- |
| [JSVM\_Env](../../structs/jsvm-env/document.md) env | Environment for calling the JSVM-API. |
| int32\_t value | Integer value to be represented in JavaScript. |
| [JSVM\_Value](../../structs/jsvm-value/document.md)\* result | Pointer to the **JSVM\_Value** of the JavaScript number type. |

**Returns**

| Type | Description |
| :-- | :-- |
| JSVM\_EXTERN [JSVM\_Status](../jsvm-types-h/document.md#jsvm_status) | 
Returns a JSVM status code.

[JSVM\_OK](../jsvm-types-h/document.md#jsvm_status): operation successful.

 |

#### \[h2\]OH\_JSVM\_CreateUint32()

JSVM\_EXTERN JSVM\_Status OH\_JSVM\_CreateUint32(JSVM\_Env env,uint32\_t value,JSVM\_Value\* result)

**Description**

Converts a value of the C uint32\_t type to a value of the JavaScript number type.

**Since**: 11

**Parameters**

| Name | Description |
| :-- | :-- |
| [JSVM\_Env](../../structs/jsvm-env/document.md) env | Environment for calling the JSVM-API. |
| uint32\_t value | Unsigned integer value to be represented in JavaScript. |
| [JSVM\_Value](../../structs/jsvm-value/document.md)\* result | Pointer to the **JSVM\_Value** of the JavaScript number type. |

**Returns**

| Type | Description |
| :-- | :-- |
| JSVM\_EXTERN [JSVM\_Status](../jsvm-types-h/document.md#jsvm_status) | 
Returns a JSVM status code.

[JSVM\_OK](../jsvm-types-h/document.md#jsvm_status): operation successful.

 |

#### \[h2\]OH\_JSVM\_CreateInt64()

JSVM\_EXTERN JSVM\_Status OH\_JSVM\_CreateInt64(JSVM\_Env env,int64\_t value,JSVM\_Value\* result)

**Description**

Converts a value of the C int64\_t type to a value of the JavaScript number type.

**Since**: 11

**Parameters**

| Name | Description |
| :-- | :-- |
| [JSVM\_Env](../../structs/jsvm-env/document.md) env | Environment for calling the JSVM-API. |
| int64\_t value | Integer value to be represented in JavaScript. |
| [JSVM\_Value](../../structs/jsvm-value/document.md)\* result | Pointer to the **JSVM\_Value** of the JavaScript number type. |

**Returns**

| Type | Description |
| :-- | :-- |
| JSVM\_EXTERN [JSVM\_Status](../jsvm-types-h/document.md#jsvm_status) | 
Returns a JSVM status code.

[JSVM\_OK](../jsvm-types-h/document.md#jsvm_status): operation successful.

 |

#### \[h2\]OH\_JSVM\_CreateDouble()

JSVM\_EXTERN JSVM\_Status OH\_JSVM\_CreateDouble(JSVM\_Env env,double value,JSVM\_Value\* result)

**Description**

Converts a value of the C double type to a value of the JavaScript number type.

**Since**: 11

**Parameters**

| Name | Description |
| :-- | :-- |
| [JSVM\_Env](../../structs/jsvm-env/document.md) env | Environment for calling the JSVM-API. |
| double value | Double-precision value to be represented in JavaScript. |
| [JSVM\_Value](../../structs/jsvm-value/document.md)\* result | Pointer to the **JSVM\_Value** of the JavaScript number type. |

**Returns**

| Type | Description |
| :-- | :-- |
| JSVM\_EXTERN [JSVM\_Status](../jsvm-types-h/document.md#jsvm_status) | 
Returns a JSVM status code.

[JSVM\_OK](../jsvm-types-h/document.md#jsvm_status): operation successful.

 |

#### \[h2\]OH\_JSVM\_CreateBigintInt64()

JSVM\_EXTERN JSVM\_Status OH\_JSVM\_CreateBigintInt64(JSVM\_Env env,int64\_t value,JSVM\_Value\* result)

**Description**

Converts a value of the C int64\_t type to a value of the JavaScript BigInt type.

**Since**: 11

**Parameters**

| Name | Description |
| :-- | :-- |
| [JSVM\_Env](../../structs/jsvm-env/document.md) env | Environment for calling the JSVM-API. |
| int64\_t value | Integer value to be represented in JavaScript. |
| [JSVM\_Value](../../structs/jsvm-value/document.md)\* result | Pointer to the **JSVM\_Value** of the JavaScript BigInt type. |

**Returns**

| Type | Description |
| :-- | :-- |
| JSVM\_EXTERN [JSVM\_Status](../jsvm-types-h/document.md#jsvm_status) | 
Returns a JSVM status code.

[JSVM\_OK](../jsvm-types-h/document.md#jsvm_status): operation successful.

 |

#### \[h2\]OH\_JSVM\_CreateBigintUint64()

JSVM\_EXTERN JSVM\_Status OH\_JSVM\_CreateBigintUint64(JSVM\_Env env,uint64\_t value,JSVM\_Value\* result)

**Description**

Converts a value of the C uint64\_t type to a value of the JavaScript BigInt type.

**Since**: 11

**Parameters**

| Name | Description |
| :-- | :-- |
| [JSVM\_Env](../../structs/jsvm-env/document.md) env | Environment for calling the JSVM-API. |
| uint64\_t value | Unsigned integer value to be represented in JavaScript. |
| [JSVM\_Value](../../structs/jsvm-value/document.md)\* result | Pointer to the **JSVM\_Value** of the JavaScript BigInt type. |

**Returns**

| Type | Description |
| :-- | :-- |
| JSVM\_EXTERN [JSVM\_Status](../jsvm-types-h/document.md#jsvm_status) | 
Returns a JSVM status code.

[JSVM\_OK](../jsvm-types-h/document.md#jsvm_status): operation successful.

 |

#### \[h2\]OH\_JSVM\_CreateBigintWords()

JSVM\_EXTERN JSVM\_Status OH\_JSVM\_CreateBigintWords(JSVM\_Env env,int signBit,size\_t wordCount,const uint64\_t\* words,JSVM\_Value\* result)

**Description**

Converts a group of 64-bit unsigned bits to a single BigInt value.

**Since**: 11

**Parameters**

| Name | Description |
| :-- | :-- |
| [JSVM\_Env](../../structs/jsvm-env/document.md) env | Environment for calling the JSVM-API. |
| int signBit | Whether the generated BigInt value is positive or negative. |
| size\_t wordCount | Length of the words array. |
| const uint64\_t\* words | Pointer to the uint64\_t little-endian words array. |
| [JSVM\_Value](../../structs/jsvm-value/document.md)\* result | Pointer to the **JSVM\_Value** of the JavaScript BigInt type. |

**Returns**

| Type | Description |
| :-- | :-- |
| JSVM\_EXTERN [JSVM\_Status](../jsvm-types-h/document.md#jsvm_status) | 
Returns a JSVM status code.

[JSVM\_OK](../jsvm-types-h/document.md#jsvm_status): operation successful.

[JSVM\_INVALID\_ARG](../jsvm-types-h/document.md#jsvm_status): invalid argument.

[JSVM\_GENERIC\_FAILURE](../jsvm-types-h/document.md#jsvm_status): generic failure due to unknown reasons.

 |

#### \[h2\]OH\_JSVM\_CreateStringLatin1()

JSVM\_EXTERN JSVM\_Status OH\_JSVM\_CreateStringLatin1(JSVM\_Env env,const char\* str,size\_t length,JSVM\_Value\* result)

**Description**

Converts an ISO-8859-1-encoded C string to a JavaScript string. A native string is copied.

**Since**: 11

**Parameters**

| Name | Description |
| :-- | :-- |
| [JSVM\_Env](../../structs/jsvm-env/document.md) env | Environment for calling the JSVM-API. |
| const char\* str | Pointer to the buffer of an ISO-8859-1-encoded string. |
| size\_t length | Length of a string, in bytes. If it is null-terminated, the value is **JSVM\_AUTO\_LENGTH**. |
| [JSVM\_Value](../../structs/jsvm-value/document.md)\* result | Pointer to the **JSVM\_Value** of the JavaScript string. |

**Returns**

| Type | Description |
| :-- | :-- |
| JSVM\_EXTERN [JSVM\_Status](../jsvm-types-h/document.md#jsvm_status) | 
Returns a JSVM status code.

[JSVM\_OK](../jsvm-types-h/document.md#jsvm_status): operation successful.

[JSVM\_GENERIC\_FAILURE](../jsvm-types-h/document.md#jsvm_status): generic failure due to unknown reasons.

 |

#### \[h2\]OH\_JSVM\_CreateStringUtf16()

JSVM\_EXTERN JSVM\_Status OH\_JSVM\_CreateStringUtf16(JSVM\_Env env,const char16\_t\* str,size\_t length,JSVM\_Value\* result)

**Description**

Converts a UTF-16LE-encoded C string to a JavaScript string. A native string is copied.

**Since**: 11

**Parameters**

| Name | Description |
| :-- | :-- |
| [JSVM\_Env](../../structs/jsvm-env/document.md) env | Environment for calling the JSVM-API. |
| const char16\_t\* str | Pointer to the buffer of a UTF-16LE-encoded string. |
| size\_t length | Length of a string in 2-byte code. If it is null-terminated, the value is **JSVM\_AUTO\_LENGTH**. |
| [JSVM\_Value](../../structs/jsvm-value/document.md)\* result | Pointer to the **JSVM\_Value** of the JavaScript string. |

**Returns**

| Type | Description |
| :-- | :-- |
| JSVM\_EXTERN [JSVM\_Status](../jsvm-types-h/document.md#jsvm_status) | 
Returns a JSVM status code.

[JSVM\_OK](../jsvm-types-h/document.md#jsvm_status): operation successful.

[JSVM\_GENERIC\_FAILURE](../jsvm-types-h/document.md#jsvm_status): generic failure due to unknown reasons.

 |

#### \[h2\]OH\_JSVM\_CreateStringUtf8()

JSVM\_EXTERN JSVM\_Status OH\_JSVM\_CreateStringUtf8(JSVM\_Env env,const char\* str,size\_t length,JSVM\_Value\* result)

**Description**

Creates a JavaScript string using a UTF-8-encoded C string. A native string is copied.

**Since**: 11

**Parameters**

| Name | Description |
| :-- | :-- |
| [JSVM\_Env](../../structs/jsvm-env/document.md) env | Environment for calling the JSVM-API. |
| const char\* str | Pointer to the buffer of a UTF-8-encoded string. |
| size\_t length | Length of a string, in bytes. If it is null-terminated, the value is **JSVM\_AUTO\_LENGTH**. |
| [JSVM\_Value](../../structs/jsvm-value/document.md)\* result | Pointer to the **JSVM\_Value** of the JavaScript string. |

**Returns**

| Type | Description |
| :-- | :-- |
| JSVM\_EXTERN [JSVM\_Status](../jsvm-types-h/document.md#jsvm_status) | 
Returns a JSVM status code.

[JSVM\_OK](../jsvm-types-h/document.md#jsvm_status): operation successful.

[JSVM\_GENERIC\_FAILURE](../jsvm-types-h/document.md#jsvm_status): generic failure due to unknown reasons.

 |

#### \[h2\]OH\_JSVM\_GetArrayLength()

JSVM\_EXTERN JSVM\_Status OH\_JSVM\_GetArrayLength(JSVM\_Env env,JSVM\_Value value,uint32\_t\* result)

**Description**

Obtains the length of an array.

**Since**: 11

**Parameters**

| Name | Description |
| :-- | :-- |
| [JSVM\_Env](../../structs/jsvm-env/document.md) env | Environment for calling the JSVM-API. |
| [JSVM\_Value](../../structs/jsvm-value/document.md) value | JavaScript array whose length is to be queried. |
| uint32\_t\* result | Pointer to the length of a uint32-encoded array. |

**Returns**

| Type | Description |
| :-- | :-- |
| JSVM\_EXTERN [JSVM\_Status](../jsvm-types-h/document.md#jsvm_status) | 
Returns a JSVM status code.

[JSVM\_OK](../jsvm-types-h/document.md#jsvm_status): operation successful.

[JSVM\_ARRAY\_EXPECTED](../jsvm-types-h/document.md#jsvm_status): array expected. This code is returned if the input parameter is not of the array type.

[JSVM\_PENDING\_EXCEPTION](../jsvm-types-h/document.md#jsvm_status): pending exception.

 |

#### \[h2\]OH\_JSVM\_GetArraybufferInfo()

JSVM\_EXTERN JSVM\_Status OH\_JSVM\_GetArraybufferInfo(JSVM\_Env env,JSVM\_Value arraybuffer,void\*\* data,size\_t\* byteLength)

**Description**

Obtains the underlying data buffer of the **ArrayBuffer** and its length.

**Since**: 11

**Parameters**

| Name | Description |
| :-- | :-- |
| [JSVM\_Env](../../structs/jsvm-env/document.md) env | Environment for calling the JSVM-API. |
| [JSVM\_Value](../../structs/jsvm-value/document.md) arraybuffer | ArrayBuffer to be queried. |
| void\*\* data | Double pointer to the underlying data buffer of the ArrayBuffer. If **byte\_length** is **0**, this value may be **NULL** or any other pointer value. |
| size\_t\* byteLength | Pointer to the length of the underlying data buffer, in bytes. |

**Returns**

| Type | Description |
| :-- | :-- |
| JSVM\_EXTERN [JSVM\_Status](../jsvm-types-h/document.md#jsvm_status) | 
Returns a JSVM status code.

[JSVM\_OK](../jsvm-types-h/document.md#jsvm_status): operation successful.

[JSVM\_INVALID\_ARG](../jsvm-types-h/document.md#jsvm_status): invalid argument.

 |

#### \[h2\]OH\_JSVM\_GetPrototype()

JSVM\_EXTERN JSVM\_Status OH\_JSVM\_GetPrototype(JSVM\_Env env,JSVM\_Value object,JSVM\_Value\* result)

**Description**

Obtains the prototype of an object.

**Since**: 11

**Parameters**

| Name | Description |
| :-- | :-- |
| [JSVM\_Env](../../structs/jsvm-env/document.md) env | Environment for calling the JSVM-API. |
| [JSVM\_Value](../../structs/jsvm-value/document.md) object | JavaScript object whose prototype is to be returned. This will return the equivalent value of **Object.getPrototypeOf** (different from the **prototype** property of the function). |
| [JSVM\_Value](../../structs/jsvm-value/document.md)\* result | Pointer to the prototype of a given object. |

**Returns**

| Type | Description |
| :-- | :-- |
| JSVM\_EXTERN [JSVM\_Status](../jsvm-types-h/document.md#jsvm_status) | 
Returns a JSVM status code.

[JSVM\_OK](../jsvm-types-h/document.md#jsvm_status): operation successful.

[JSVM\_PENDING\_EXCEPTION](../jsvm-types-h/document.md#jsvm_status): pending exception.

 |

#### \[h2\]OH\_JSVM\_GetTypedarrayInfo()

JSVM\_EXTERN JSVM\_Status OH\_JSVM\_GetTypedarrayInfo(JSVM\_Env env,JSVM\_Value typedarray,JSVM\_TypedarrayType\* type,size\_t\* length,void\*\* data,JSVM\_Value\* arraybuffer,size\_t\* byteOffset)

**Description**

Obtains the properties of a typed array. If any property is not required, its output parameter can be **NULL**.

**Since**: 11

**Parameters**

| Name | Description |
| :-- | :-- |
| [JSVM\_Env](../../structs/jsvm-env/document.md) env | Environment for calling the JSVM-API. |
| [JSVM\_Value](../../structs/jsvm-value/document.md) typedarray | **TypedArray** whose properties are to be queried. |
| [JSVM\_TypedarrayType](../jsvm-types-h/document.md#jsvm_typedarraytype)\* type | Pointer to the scalar data type of an element in **TypedArray**. |
| size\_t\* length | Pointer to the number of elements in **TypedArray**. |
| void\*\* data | Double pointer to the first element in **TypedArray**. The underlying data buffer of the **TypedArray** is adjusted by **byte\_offset** so that it points to the first element. If the array length is **0**, **data** may be NULL or any other pointer value. |
| [JSVM\_Value](../../structs/jsvm-value/document.md)\* arraybuffer | Pointer to the **ArrayBuffer** under **TypedArray**. |
| size\_t\* byteOffset | Pointer to the byte offset of the first **TypedArray** element in the native array. **data** points to the first element in the array after its value has been adjusted. Therefore, the first byte of the native array is located at (data - byte\_offset). |

**Returns**

| Type | Description |
| :-- | :-- |
| JSVM\_EXTERN [JSVM\_Status](../jsvm-types-h/document.md#jsvm_status) | 
Returns a JSVM status code.

[JSVM\_OK](../jsvm-types-h/document.md#jsvm_status): operation successful.

[JSVM\_INVALID\_ARG](../jsvm-types-h/document.md#jsvm_status): invalid argument.

 |

#### \[h2\]OH\_JSVM\_GetDataviewInfo()

JSVM\_EXTERN JSVM\_Status OH\_JSVM\_GetDataviewInfo(JSVM\_Env env,JSVM\_Value dataview,size\_t\* bytelength,void\*\* data,JSVM\_Value\* arraybuffer,size\_t\* byteOffset)

**Description**

Obtains the proprieties of a **DataView**. If any property is not required, its output parameter can be **NULL**.

**Since**: 11

**Parameters**

| Name | Description |
| :-- | :-- |
| [JSVM\_Env](../../structs/jsvm-env/document.md) env | Environment for calling the JSVM-API. |
| [JSVM\_Value](../../structs/jsvm-value/document.md) dataview | **DataView** whose properties are to be queried. |
| size\_t\* bytelength | Pointer to the number of bytes in **DataView**. |
| void\*\* data | Double pointer to the data buffer in **DataView**. If **bytelength** is **0**, this value may be **NULL** or any other pointer value. |
| [JSVM\_Value](../../structs/jsvm-value/document.md)\* arraybuffer | Pointer to the **ArrayBuffer**, which is the basis of **DataView**. |
| size\_t\* byteOffset | Pointer to the byte offset for the start position of mapping **DataView** in the data buffer. |

**Returns**

| Type | Description |
| :-- | :-- |
| JSVM\_EXTERN [JSVM\_Status](../jsvm-types-h/document.md#jsvm_status) | 
Returns a JSVM status code.

[JSVM\_OK](../jsvm-types-h/document.md#jsvm_status): operation successful.

[JSVM\_INVALID\_ARG](../jsvm-types-h/document.md#jsvm_status): invalid argument. This code is returned if the input argument is not an external **JSVM\_Value**.

 |

#### \[h2\]OH\_JSVM\_GetDateValue()

JSVM\_EXTERN JSVM\_Status OH\_JSVM\_GetDateValue(JSVM\_Env env,JSVM\_Value value,double\* result)

**Description**

Obtains the C double-precision primitive equivalent of a given JavaScript date. If this API call is successfully, **JSVM\_OK** is returned. If a **JSVM\_Value** of a non-JavaScript date type is passed in, **JSVM\_DATA\_EXPECTED** is returned.

**Since**: 11

**Parameters**

| Name | Description |
| :-- | :-- |
| [JSVM\_Env](../../structs/jsvm-env/document.md) env | Environment for calling the JSVM-API. |
| [JSVM\_Value](../../structs/jsvm-value/document.md) value | JavaScript date. |
| double\* result | Pointer to the time value of the double type, expressed as the number of milliseconds since 00:00:00 UTC on January 1, 1970. |

**Returns**

| Type | Description |
| :-- | :-- |
| JSVM\_EXTERN [JSVM\_Status](../jsvm-types-h/document.md#jsvm_status) | 
Returns a JSVM status code.

[JSVM\_OK](../jsvm-types-h/document.md#jsvm_status): operation successful.

[JSVM\_DATE\_EXPECTED](../jsvm-types-h/document.md#jsvm_status): date expected. This code is returned if the input argument is not of the date type.

[JSVM\_PENDING\_EXCEPTION](../jsvm-types-h/document.md#jsvm_status): pending exception.

 |

#### \[h2\]OH\_JSVM\_GetValueBool()

JSVM\_EXTERN JSVM\_Status OH\_JSVM\_GetValueBool(JSVM\_Env env,JSVM\_Value value,bool\* result)

**Description**

Obtains the C Boolean primitive equivalent of a given JavaScript Boolean value.

**Since**: 11

**Parameters**

| Name | Description |
| :-- | :-- |
| [JSVM\_Env](../../structs/jsvm-env/document.md) env | Environment for calling the JSVM-API. |
| [JSVM\_Value](../../structs/jsvm-value/document.md) value | Input JavaScript Boolean object. |
| bool\* result | Pointer to the Boolean value equivalent to the given JavaScript Boolean object. If the value of the **value** object is **true**, **true** is returned; otherwise, **false** is returned. |

**Returns**

| Type | Description |
| :-- | :-- |
| JSVM\_EXTERN [JSVM\_Status](../jsvm-types-h/document.md#jsvm_status) | 
Returns a JSVM status code.

[JSVM\_OK](../jsvm-types-h/document.md#jsvm_status): operation successful.

[JSVM\_BOOLEAN\_EXPECTED](../jsvm-types-h/document.md#jsvm_status): Boolean expected. This code is returned if the input parameter is not of the Boolean type.

 |

#### \[h2\]OH\_JSVM\_GetValueDouble()

JSVM\_EXTERN JSVM\_Status OH\_JSVM\_GetValueDouble(JSVM\_Env env,JSVM\_Value value,double\* result)

**Description**

Obtains the C double-precision primitive equivalent of a given JavaScript number.

**Since**: 11

**Parameters**

| Name | Description |
| :-- | :-- |
| [JSVM\_Env](../../structs/jsvm-env/document.md) env | Environment for calling the JSVM-API. |
| [JSVM\_Value](../../structs/jsvm-value/document.md) value | JavaScript number. |
| double\* result | Pointer to the C double-precision primitive equivalent of a given JavaScript number. |

**Returns**

| Type | Description |
| :-- | :-- |
| JSVM\_EXTERN [JSVM\_Status](../jsvm-types-h/document.md#jsvm_status) | 
Returns a JSVM status code.

[JSVM\_OK](../jsvm-types-h/document.md#jsvm_status): operation successful.

[JSVM\_NUMBER\_EXPECTED](../jsvm-types-h/document.md#jsvm_status): number expected. This code is returned if the input parameter is not of the number type.

 |

#### \[h2\]OH\_JSVM\_GetValueBigintInt64()

JSVM\_EXTERN JSVM\_Status OH\_JSVM\_GetValueBigintInt64(JSVM\_Env env,JSVM\_Value value,int64\_t\* result,bool\* lossless)

**Description**

Obtains the C int64\_t primitive equivalent of a given JavaScript BigInt value. If necessary, it truncates the value and sets **lossless** to **false**.

**Since**: 11

**Parameters**

| Name | Description |
| :-- | :-- |
| [JSVM\_Env](../../structs/jsvm-env/document.md) env | Environment for calling the JSVM-API. |
| [JSVM\_Value](../../structs/jsvm-value/document.md) value | JavaScript BigInt value. |
| int64\_t\* result | Pointer to the C int64\_t primitive equivalent of the given JavaScript BigInt value. |
| bool\* lossless | Pointer to the Boolean value. The value **true** indicates the BigInt value is losslessly converted, and **false** indicates the opposite. |

**Returns**

| Type | Description |
| :-- | :-- |
| JSVM\_EXTERN [JSVM\_Status](../jsvm-types-h/document.md#jsvm_status) | 
Returns a JSVM status code.

[JSVM\_OK](../jsvm-types-h/document.md#jsvm_status): operation successful.

[JSVM\_BIGINT\_EXPECTED](../jsvm-types-h/document.md#jsvm_status): BigInt expected. This code is returned if the input parameter is not of the BigInt type.

 |

#### \[h2\]OH\_JSVM\_GetValueBigintUint64()

JSVM\_EXTERN JSVM\_Status OH\_JSVM\_GetValueBigintUint64(JSVM\_Env env,JSVM\_Value value,uint64\_t\* result,bool\* lossless)

**Description**

Obtains the C uint64\_t primitive equivalent of a given JavaScript BigInt value. If necessary, it truncates the value and sets **lossless** to **false**.

**Since**: 11

**Parameters**

| Name | Description |
| :-- | :-- |
| [JSVM\_Env](../../structs/jsvm-env/document.md) env | Environment for calling the JSVM-API. |
| [JSVM\_Value](../../structs/jsvm-value/document.md) value | JavaScript BigInt value. |
| uint64\_t\* result | Pointer to the C uint64\_t primitive equivalent of the given JavaScript BigInt value. |
| bool\* lossless | Pointer to the Boolean value. The value **true** indicates the BigInt value is losslessly converted, and **false** indicates the opposite. |

**Returns**

| Type | Description |
| :-- | :-- |
| JSVM\_EXTERN [JSVM\_Status](../jsvm-types-h/document.md#jsvm_status) | 
Returns a JSVM status code.

[JSVM\_OK](../jsvm-types-h/document.md#jsvm_status): operation successful.

[JSVM\_BIGINT\_EXPECTED](../jsvm-types-h/document.md#jsvm_status): BigInt expected. This code is returned if the input parameter is not of the BigInt type.

 |

#### \[h2\]OH\_JSVM\_GetValueBigintWords()

JSVM\_EXTERN JSVM\_Status OH\_JSVM\_GetValueBigintWords(JSVM\_Env env,JSVM\_Value value,int\* signBit,size\_t\* wordCount,uint64\_t\* words)

**Description**

Converts a BigInt value to the sign bit, 64-bit little-endian array, and number of elements in the array. Both **signBit** and **words** can be set to **NULL**. In this case, only **wordCount** is obtained.

**Since**: 11

**Parameters**

| Name | Description |
| :-- | :-- |
| [JSVM\_Env](../../structs/jsvm-env/document.md) env | Environment for calling the JSVM-API. |
| [JSVM\_Value](../../structs/jsvm-value/document.md) value | JavaScript BigInt value. |
| int\* signBit | Pointer to the JavaScript BigInt value, indicating a positive or negative integer. |
| size\_t\* wordCount | Pointer to the length of the words array. It will be set to the actual number of words required to store this BigInt. |
| uint64\_t\* words | Pointer to the pre-allocated 64-bit words array. |

**Returns**

| Type | Description |
| :-- | :-- |
| JSVM\_EXTERN [JSVM\_Status](../jsvm-types-h/document.md#jsvm_status) | 
Returns a JSVM status code.

[JSVM\_OK](../jsvm-types-h/document.md#jsvm_status): operation successful.

[JSVM\_BIGINT\_EXPECTED](../jsvm-types-h/document.md#jsvm_status): BigInt expected. This code is returned if the input parameter is not of the BigInt type.

 |

#### \[h2\]OH\_JSVM\_GetValueExternal()

JSVM\_EXTERN JSVM\_Status OH\_JSVM\_GetValueExternal(JSVM\_Env env,JSVM\_Value value,void\*\* result)

**Description**

Obtains the external data pointer previously passed to **OH\_JSVM\_CreateExternal()**.

**Since**: 11

**Parameters**

| Name | Description |
| :-- | :-- |
| [JSVM\_Env](../../structs/jsvm-env/document.md) env | Environment for calling the JSVM-API. |
| [JSVM\_Value](../../structs/jsvm-value/document.md) value | JavaScript external value. |
| void\*\* result | Double pointer to the data wrapped by the JavaScript external value. |

**Returns**

| Type | Description |
| :-- | :-- |
| JSVM\_EXTERN [JSVM\_Status](../jsvm-types-h/document.md#jsvm_status) | 
Returns a JSVM status code.

[JSVM\_OK](../jsvm-types-h/document.md#jsvm_status): operation successful.

[JSVM\_INVALID\_ARG](../jsvm-types-h/document.md#jsvm_status): invalid argument. This code is returned if the input argument is not an external **JSVM\_Value**.

 |

#### \[h2\]OH\_JSVM\_GetValueInt32()

JSVM\_EXTERN JSVM\_Status OH\_JSVM\_GetValueInt32(JSVM\_Env env,JSVM\_Value value,int32\_t\* result)

**Description**

Obtains the C int32 primitive equivalent of a given JavaScript number.

**Since**: 11

**Parameters**

| Name | Description |
| :-- | :-- |
| [JSVM\_Env](../../structs/jsvm-env/document.md) env | Environment for calling the JSVM-API. |
| [JSVM\_Value](../../structs/jsvm-value/document.md) value | JavaScript number. |
| int32\_t\* result | Pointer to the C int32 primitive equivalent of the given JavaScript number. |

**Returns**

| Type | Description |
| :-- | :-- |
| JSVM\_EXTERN [JSVM\_Status](../jsvm-types-h/document.md#jsvm_status) | 
Returns a JSVM status code.

[JSVM\_OK](../jsvm-types-h/document.md#jsvm_status): operation successful.

[JSVM\_NUMBER\_EXPECTED](../jsvm-types-h/document.md#jsvm_status): number expected. This code is returned if the input parameter is not of the number type.

 |

#### \[h2\]OH\_JSVM\_GetValueInt64()

JSVM\_EXTERN JSVM\_Status OH\_JSVM\_GetValueInt64(JSVM\_Env env,JSVM\_Value value,int64\_t\* result)

**Description**

Obtains the C int64 primitive equivalent of a given JavaScript number.

**Since**: 11

**Parameters**

| Name | Description |
| :-- | :-- |
| [JSVM\_Env](../../structs/jsvm-env/document.md) env | Environment for calling the JSVM-API. |
| [JSVM\_Value](../../structs/jsvm-value/document.md) value | JavaScript number. |
| int64\_t\* result | Pointer to the C int64 primitive equivalent of the given JavaScript number. |

**Returns**

| Type | Description |
| :-- | :-- |
| JSVM\_EXTERN [JSVM\_Status](../jsvm-types-h/document.md#jsvm_status) | 
Returns a JSVM status code.

[JSVM\_OK](../jsvm-types-h/document.md#jsvm_status): operation successful.

[JSVM\_NUMBER\_EXPECTED](../jsvm-types-h/document.md#jsvm_status): number expected. This code is returned if the input parameter is not of the number type.

 |

#### \[h2\]OH\_JSVM\_GetValueStringLatin1()

JSVM\_EXTERN JSVM\_Status OH\_JSVM\_GetValueStringLatin1(JSVM\_Env env,JSVM\_Value value,char\* buf,size\_t bufsize,size\_t\* result)

**Description**

Obtains the ISO-8859-1-encoded string corresponding to the input value.

**Since**: 11

**Parameters**

| Name | Description |
| :-- | :-- |
| [JSVM\_Env](../../structs/jsvm-env/document.md) env | Environment for calling the JSVM-API. |
| [JSVM\_Value](../../structs/jsvm-value/document.md) value | JavaScript number. |
| char\* buf | Pointer to the buffer to which an ISO-8859-1 encoded string is written. If **NULL** is passed, the length of the string (in bytes, excluding the **null** terminator) is returned in **result**. |
| size\_t bufsize | Size of the destination buffer. If the size is insufficient, the returned string is truncated and terminated with **null**. |
| size\_t\* result | Pointer to the number of bytes copied to the buffer, excluding the null terminator. |

**Returns**

| Type | Description |
| :-- | :-- |
| JSVM\_EXTERN [JSVM\_Status](../jsvm-types-h/document.md#jsvm_status) | 
Returns a JSVM status code.

[JSVM\_OK](../jsvm-types-h/document.md#jsvm_status): operation successful.

[JSVM\_STRING\_EXPECTED](../jsvm-types-h/document.md#jsvm_status): string expected. This code is returned if the input parameter is not of the string type.

 |

#### \[h2\]OH\_JSVM\_GetValueStringUtf8()

JSVM\_EXTERN JSVM\_Status OH\_JSVM\_GetValueStringUtf8(JSVM\_Env env,JSVM\_Value value,char\* buf,size\_t bufsize,size\_t\* result)

**Description**

Obtains the UTF-8-encoded string corresponding to the input value.

**Since**: 11

**Parameters**

| Name | Description |
| :-- | :-- |
| [JSVM\_Env](../../structs/jsvm-env/document.md) env | Environment for calling the JSVM-API. |
| [JSVM\_Value](../../structs/jsvm-value/document.md) value | JavaScript string. |
| char\* buf | Pointer to the buffer to which a UTF-8-encoded string is written. If **NULL** is passed, the length of the string in bytes is returned in **result**, excluding the null terminator. |
| size\_t bufsize | Size of the destination buffer. If the size is insufficient, the returned string is truncated and terminated with **null**. |
| size\_t\* result | Pointer to the number of bytes copied to the buffer, excluding the null terminator. |

**Returns**

| Type | Description |
| :-- | :-- |
| JSVM\_EXTERN [JSVM\_Status](../jsvm-types-h/document.md#jsvm_status) | 
Returns a JSVM status code.

[JSVM\_OK](../jsvm-types-h/document.md#jsvm_status): operation successful.

[JSVM\_STRING\_EXPECTED](../jsvm-types-h/document.md#jsvm_status): string expected. This code is returned if the input parameter is not of the string type.

 |

#### \[h2\]OH\_JSVM\_GetValueStringUtf16()

JSVM\_EXTERN JSVM\_Status OH\_JSVM\_GetValueStringUtf16(JSVM\_Env env,JSVM\_Value value,char16\_t\* buf,size\_t bufsize,size\_t\* result)

**Description**

Obtains the UTF-16-encoded string corresponding to the input value.

**Since**: 11

**Parameters**

| Name | Description |
| :-- | :-- |
| [JSVM\_Env](../../structs/jsvm-env/document.md) env | Environment for calling the JSVM-API. |
| [JSVM\_Value](../../structs/jsvm-value/document.md) value | JavaScript string. |
| char16\_t\* buf | Pointer to the buffer to which a UTF-16LE-encoded string is written. If **NULL** is passed, the length of the string in 2-byte code is returned, excluding the null terminator. |
| size\_t bufsize | Size of the destination buffer. If the size is insufficient, the returned string is truncated and terminated with **null**. |
| size\_t\* result | Pointer to the number of the 2-byte code units copied to the buffer, excluding the null terminator. |

**Returns**

| Type | Description |
| :-- | :-- |
| JSVM\_EXTERN [JSVM\_Status](../jsvm-types-h/document.md#jsvm_status) | 
Returns a JSVM status code.

[JSVM\_OK](../jsvm-types-h/document.md#jsvm_status): operation successful.

[JSVM\_STRING\_EXPECTED](../jsvm-types-h/document.md#jsvm_status): string expected. This code is returned if the input parameter is not of the string type.

 |

#### \[h2\]OH\_JSVM\_GetValueUint32()

JSVM\_EXTERN JSVM\_Status OH\_JSVM\_GetValueUint32(JSVM\_Env env,JSVM\_Value value,uint32\_t\* result)

**Description**

Obtains the C uint\_32 primitive equivalent of a given JavaScript number.

**Since**: 11

**Parameters**

| Name | Description |
| :-- | :-- |
| [JSVM\_Env](../../structs/jsvm-env/document.md) env | Environment for calling the JSVM-API. |
| [JSVM\_Value](../../structs/jsvm-value/document.md) value | JavaScript number. |
| uint32\_t\* result | Pointer to the C uint32\_t primitive equivalent of a given **JSVM\_Value**. |

**Returns**

| Type | Description |
| :-- | :-- |
| JSVM\_EXTERN [JSVM\_Status](../jsvm-types-h/document.md#jsvm_status) | 
Returns a JSVM status code.

[JSVM\_OK](../jsvm-types-h/document.md#jsvm_status): operation successful.

[JSVM\_NUMBER\_EXPECTED](../jsvm-types-h/document.md#jsvm_status): number expected. This code is returned if the input parameter is not of the number type.

 |

#### \[h2\]OH\_JSVM\_GetBoolean()

JSVM\_EXTERN JSVM\_Status OH\_JSVM\_GetBoolean(JSVM\_Env env,bool value,JSVM\_Value\* result)

**Description**

Obtains a JavaScript singleton object that is used to represent the given Boolean value.

**Since**: 11

**Parameters**

| Name | Description |
| :-- | :-- |
| [JSVM\_Env](../../structs/jsvm-env/document.md) env | Environment for calling the JSVM-API. |
| bool value | Boolean value to be retrieved. The value can be **true** or **false**. |
| [JSVM\_Value](../../structs/jsvm-value/document.md)\* result | Pointer to the JavaScript Boolean singleton to be retrieved. |

**Returns**

| Type | Description |
| :-- | :-- |
| JSVM\_EXTERN [JSVM\_Status](../jsvm-types-h/document.md#jsvm_status) | 
Returns a JSVM status code.

[JSVM\_OK](../jsvm-types-h/document.md#jsvm_status): operation successful.

 |

#### \[h2\]OH\_JSVM\_GetGlobal()

JSVM\_EXTERN JSVM\_Status OH\_JSVM\_GetGlobal(JSVM\_Env env,JSVM\_Value\* result)

**Description**

Obtains the global object.

**Since**: 11

**Parameters**

| Name | Description |
| :-- | :-- |
| [JSVM\_Env](../../structs/jsvm-env/document.md) env | Environment for calling the JSVM-API. |
| [JSVM\_Value](../../structs/jsvm-value/document.md)\* result | Pointer to the JavaScript global object. |

**Returns**

| Type | Description |
| :-- | :-- |
| JSVM\_EXTERN [JSVM\_Status](../jsvm-types-h/document.md#jsvm_status) | 
Returns a JSVM status code.

[JSVM\_OK](../jsvm-types-h/document.md#jsvm_status): operation successful.

 |

#### \[h2\]OH\_JSVM\_GetNull()

JSVM\_EXTERN JSVM\_Status OH\_JSVM\_GetNull(JSVM\_Env env,JSVM\_Value\* result)

**Description**

Obtains the null object.

**Since**: 11

**Parameters**

| Name | Description |
| :-- | :-- |
| [JSVM\_Env](../../structs/jsvm-env/document.md) env | Environment for calling the JSVM-API. |
| [JSVM\_Value](../../structs/jsvm-value/document.md)\* result | Pointer to the JavaScript null object. |

**Returns**

| Type | Description |
| :-- | :-- |
| JSVM\_EXTERN [JSVM\_Status](../jsvm-types-h/document.md#jsvm_status) | 
Returns a JSVM status code.

[JSVM\_OK](../jsvm-types-h/document.md#jsvm_status): operation successful.

 |

#### \[h2\]OH\_JSVM\_GetUndefined()

JSVM\_EXTERN JSVM\_Status OH\_JSVM\_GetUndefined(JSVM\_Env env,JSVM\_Value\* result)

**Description**

Obtains the undefined object.

**Since**: 11

**Parameters**

| Name | Description |
| :-- | :-- |
| [JSVM\_Env](../../structs/jsvm-env/document.md) env | Environment for calling the JSVM-API. |
| [JSVM\_Value](../../structs/jsvm-value/document.md)\* result | Pointer to the JavaScript undefined value. |

**Returns**

| Type | Description |
| :-- | :-- |
| JSVM\_EXTERN [JSVM\_Status](../jsvm-types-h/document.md#jsvm_status) | 
Returns a JSVM status code.

[JSVM\_OK](../jsvm-types-h/document.md#jsvm_status): operation successful.

 |

#### \[h2\]OH\_JSVM\_CoerceToBool()

JSVM\_EXTERN JSVM\_Status OH\_JSVM\_CoerceToBool(JSVM\_Env env,JSVM\_Value value,JSVM\_Value\* result)

**Description**

Implements the abstract operation **ToBoolean()**.

**Since**: 11

**Parameters**

| Name | Description |
| :-- | :-- |
| [JSVM\_Env](../../structs/jsvm-env/document.md) env | Environment for calling the JSVM-API. |
| [JSVM\_Value](../../structs/jsvm-value/document.md) value | JavaScript value to be forcibly converted. |
| [JSVM\_Value](../../structs/jsvm-value/document.md)\* result | Pointer to the JavaScript Boolean value. |

**Returns**

| Type | Description |
| :-- | :-- |
| JSVM\_EXTERN [JSVM\_Status](../jsvm-types-h/document.md#jsvm_status) | 
Returns a JSVM status code.

[JSVM\_OK](../jsvm-types-h/document.md#jsvm_status): operation successful.

[JSVM\_PENDING\_EXCEPTION](../jsvm-types-h/document.md#jsvm_status): pending exception.

 |

#### \[h2\]OH\_JSVM\_CoerceToNumber()

JSVM\_EXTERN JSVM\_Status OH\_JSVM\_CoerceToNumber(JSVM\_Env env,JSVM\_Value value,JSVM\_Value\* result)

**Description**

Implements the abstract operation **ToNumber()**. If the input value is an object, the function may run JavaScript code.

**Since**: 11

**Parameters**

| Name | Description |
| :-- | :-- |
| [JSVM\_Env](../../structs/jsvm-env/document.md) env | Environment for calling the JSVM-API. |
| [JSVM\_Value](../../structs/jsvm-value/document.md) value | JavaScript value to be forcibly converted. |
| [JSVM\_Value](../../structs/jsvm-value/document.md)\* result | Pointer to the JavaScript number. |

**Returns**

| Type | Description |
| :-- | :-- |
| JSVM\_EXTERN [JSVM\_Status](../jsvm-types-h/document.md#jsvm_status) | 
Returns a JSVM status code.

[JSVM\_OK](../jsvm-types-h/document.md#jsvm_status): operation successful.

[JSVM\_NUMBER\_EXPECTED](../jsvm-types-h/document.md#jsvm_status): number expected. This code is returned if the input JavaScript value cannot be converted to a number.

 |

#### \[h2\]OH\_JSVM\_CoerceToObject()

JSVM\_EXTERN JSVM\_Status OH\_JSVM\_CoerceToObject(JSVM\_Env env,JSVM\_Value value,JSVM\_Value\* result)

**Description**

Implements the abstract operation **ToObject()**.

**Since**: 11

**Parameters**

| Name | Description |
| :-- | :-- |
| [JSVM\_Env](../../structs/jsvm-env/document.md) env | Environment for calling the JSVM-API. |
| [JSVM\_Value](../../structs/jsvm-value/document.md) value | JavaScript value to be forcibly converted. |
| [JSVM\_Value](../../structs/jsvm-value/document.md)\* result | Pointer to the JavaScript object. |

**Returns**

| Type | Description |
| :-- | :-- |
| JSVM\_EXTERN [JSVM\_Status](../jsvm-types-h/document.md#jsvm_status) | 
Returns a JSVM status code.

[JSVM\_OK](../jsvm-types-h/document.md#jsvm_status): operation successful.

[JSVM\_OBJECT\_EXPECTED](../jsvm-types-h/document.md#jsvm_status): object expected. This code is returned if the input JavaScript value cannot be converted to an object.

 |

#### \[h2\]OH\_JSVM\_CoerceToString()

JSVM\_EXTERN JSVM\_Status OH\_JSVM\_CoerceToString(JSVM\_Env env,JSVM\_Value value,JSVM\_Value\* result)

**Description**

Implements the abstract operation **ToString()**. If the input value is an object, the function may run JavaScript code.

**Since**: 11

**Parameters**

| Name | Description |
| :-- | :-- |
| [JSVM\_Env](../../structs/jsvm-env/document.md) env | Environment for calling the JSVM-API. |
| [JSVM\_Value](../../structs/jsvm-value/document.md) value | JavaScript value to be forcibly converted. |
| [JSVM\_Value](../../structs/jsvm-value/document.md)\* result | Pointer to the JavaScript string. |

**Returns**

| Type | Description |
| :-- | :-- |
| JSVM\_EXTERN [JSVM\_Status](../jsvm-types-h/document.md#jsvm_status) | 
Returns a JSVM status code.

[JSVM\_OK](../jsvm-types-h/document.md#jsvm_status): operation successful.

[JSVM\_STRING\_EXPECTED](../jsvm-types-h/document.md#jsvm_status): string expected. This code is returned if the input JavaScript value cannot be converted to a string.

 |

#### \[h2\]OH\_JSVM\_Typeof()

JSVM\_EXTERN JSVM\_Status OH\_JSVM\_Typeof(JSVM\_Env env,JSVM\_Value value,JSVM\_ValueType\* result)

**Description**

Provides a behavior similar to calling the **typeof** operator on a defined object. The difference is that this function supports the detection of external values; it detects null as a separate type, while ECMAScript **typeof** is used to detect objects. If the value type is invalid, an error is returned.

**Since**: 11

**Parameters**

| Name | Description |
| :-- | :-- |
| [JSVM\_Env](../../structs/jsvm-env/document.md) env | Environment for calling the JSVM-API. |
| [JSVM\_Value](../../structs/jsvm-value/document.md) value | JavaScript value whose type is to be queried. |
| [JSVM\_ValueType](../jsvm-types-h/document.md#jsvm_valuetype)\* result | Pointer to the type of the JavaScript value. |

**Returns**

| Type | Description |
| :-- | :-- |
| JSVM\_EXTERN [JSVM\_Status](../jsvm-types-h/document.md#jsvm_status) | 
Returns a JSVM status code.

[JSVM\_OK](../jsvm-types-h/document.md#jsvm_status): operation successful.

[JSVM\_INVALID\_ARG](../jsvm-types-h/document.md#jsvm_status): invalid argument.

 |

#### \[h2\]OH\_JSVM\_Instanceof()

JSVM\_EXTERN JSVM\_Status OH\_JSVM\_Instanceof(JSVM\_Env env,JSVM\_Value object,JSVM\_Value constructor,bool\* result)

**Description**

Provides a behavior similar to calling the **instanceof** operator on an object.

**Since**: 11

**Parameters**

| Name | Description |
| :-- | :-- |
| [JSVM\_Env](../../structs/jsvm-env/document.md) env | Environment for calling the JSVM-API. |
| [JSVM\_Value](../../structs/jsvm-value/document.md) object | JavaScript value to be checked. |
| [JSVM\_Value](../../structs/jsvm-value/document.md) constructor | Constructor to be checked. |
| bool\* result | Pointer to the check result. The value **true** indicates that **object instanceof constructor** is **true**, and **false** indicates the opposite. |

**Returns**

| Type | Description |
| :-- | :-- |
| JSVM\_EXTERN [JSVM\_Status](../jsvm-types-h/document.md#jsvm_status) | 
Returns a JSVM status code.

[JSVM\_OK](../jsvm-types-h/document.md#jsvm_status): operation successful.

[JSVM\_FUNCTION\_EXPECTED](../jsvm-types-h/document.md#jsvm_status): function expected. This code is returned if the input parameter is not of the function type.

[JSVM\_GENERIC\_FAILURE](../jsvm-types-h/document.md#jsvm_status): generic failure due to unknown reasons.

[JSVM\_PENDING\_EXCEPTION](../jsvm-types-h/document.md#jsvm_status): pending exception.

 |

#### \[h2\]OH\_JSVM\_IsArray()

JSVM\_EXTERN JSVM\_Status OH\_JSVM\_IsArray(JSVM\_Env env,JSVM\_Value value,bool\* result)

**Description**

Provides a behavior similar to calling **IsArray** on an object.

**Since**: 11

**Parameters**

| Name | Description |
| :-- | :-- |
| [JSVM\_Env](../../structs/jsvm-env/document.md) env | Environment for calling the JSVM-API. |
| [JSVM\_Value](../../structs/jsvm-value/document.md) value | JavaScript value to be checked. |
| bool\* result | Pointer to the check result. The value **true** indicates that the given object is an array, and **false** indicates the opposite. |

**Returns**

| Type | Description |
| :-- | :-- |
| JSVM\_EXTERN [JSVM\_Status](../jsvm-types-h/document.md#jsvm_status) | 
Returns a JSVM status code.

[JSVM\_OK](../jsvm-types-h/document.md#jsvm_status): operation successful.

 |

#### \[h2\]OH\_JSVM\_IsArraybuffer()

JSVM\_EXTERN JSVM\_Status OH\_JSVM\_IsArraybuffer(JSVM\_Env env,JSVM\_Value value,bool\* result)

**Description**

Checks whether the input object is an **ArrayBuffer**.

**Since**: 11

**Parameters**

| Name | Description |
| :-- | :-- |
| [JSVM\_Env](../../structs/jsvm-env/document.md) env | Environment for calling the JSVM-API. |
| [JSVM\_Value](../../structs/jsvm-value/document.md) value | JavaScript value to be checked. |
| bool\* result | Pointer to the check result. The value **true** indicates that the specified object is an **ArrayBuffer**, and **false** indicates the opposite. |

**Returns**

| Type | Description |
| :-- | :-- |
| JSVM\_EXTERN [JSVM\_Status](../jsvm-types-h/document.md#jsvm_status) | 
Returns a JSVM status code.

[JSVM\_OK](../jsvm-types-h/document.md#jsvm_status): operation successful.

 |

#### \[h2\]OH\_JSVM\_IsDate()

JSVM\_EXTERN JSVM\_Status OH\_JSVM\_IsDate(JSVM\_Env env,JSVM\_Value value,bool\* isDate)

**Description**

Checks whether the input object is a date.

**Since**: 11

**Parameters**

| Name | Description |
| :-- | :-- |
| [JSVM\_Env](../../structs/jsvm-env/document.md) env | Environment for calling the JSVM-API. |
| [JSVM\_Value](../../structs/jsvm-value/document.md) value | JavaScript value to be checked. |
| bool\* isDate | Pointer to the check result. The value **true** indicates that the given **JSVM\_Value** is a JavaScript **Date** object, and **false** indicates the opposite. |

**Returns**

| Type | Description |
| :-- | :-- |
| JSVM\_EXTERN [JSVM\_Status](../jsvm-types-h/document.md#jsvm_status) | 
Returns a JSVM status code.

[JSVM\_OK](../jsvm-types-h/document.md#jsvm_status): operation successful.

 |

#### \[h2\]OH\_JSVM\_IsTypedarray()

JSVM\_EXTERN JSVM\_Status OH\_JSVM\_IsTypedarray(JSVM\_Env env,JSVM\_Value value,bool\* result)

**Description**

Checks whether the input object is a typed array.

**Since**: 11

**Parameters**

| Name | Description |
| :-- | :-- |
| [JSVM\_Env](../../structs/jsvm-env/document.md) env | Environment for calling the JSVM-API. |
| [JSVM\_Value](../../structs/jsvm-value/document.md) value | JavaScript value to be checked. |
| bool\* result | Pointer to the check result. The value **true** indicates that the given **JSVM\_Value** is a typed array, and **false** indicates the opposite. |

**Returns**

| Type | Description |
| :-- | :-- |
| JSVM\_EXTERN [JSVM\_Status](../jsvm-types-h/document.md#jsvm_status) | 
Returns a JSVM status code.

[JSVM\_OK](../jsvm-types-h/document.md#jsvm_status): operation successful.

 |

#### \[h2\]OH\_JSVM\_IsDataview()

JSVM\_EXTERN JSVM\_Status OH\_JSVM\_IsDataview(JSVM\_Env env,JSVM\_Value value,bool\* result)

**Description**

Checks whether the input object is **DataView**.

**Since**: 11

**Parameters**

| Name | Description |
| :-- | :-- |
| [JSVM\_Env](../../structs/jsvm-env/document.md) env | Environment for calling the JSVM-API. |
| [JSVM\_Value](../../structs/jsvm-value/document.md) value | JavaScript value to be checked. |
| bool\* result | Pointer to the check result. The value **true** indicates that the given **JSVM\_Value** is a **DataView**, and **false** indicates the opposite. |

**Returns**

| Type | Description |
| :-- | :-- |
| JSVM\_EXTERN [JSVM\_Status](../jsvm-types-h/document.md#jsvm_status) | 
Returns a JSVM status code.

[JSVM\_OK](../jsvm-types-h/document.md#jsvm_status): operation successful.

 |

#### \[h2\]OH\_JSVM\_StrictEquals()

JSVM\_EXTERN JSVM\_Status OH\_JSVM\_StrictEquals(JSVM\_Env env,JSVM\_Value lhs,JSVM\_Value rhs,bool\* result)

**Description**

Provides a behavior similar to calling the strict equality algorithm (===).

**Since**: 11

**Parameters**

| Name | Description |
| :-- | :-- |
| [JSVM\_Env](../../structs/jsvm-env/document.md) env | Environment for calling the JSVM-API. |
| [JSVM\_Value](../../structs/jsvm-value/document.md) lhs | JavaScript value to be checked. |
| [JSVM\_Value](../../structs/jsvm-value/document.md) rhs | JavaScript value to be checked. |
| bool\* result | Pointer to the check result. The value **true** indicates that two **JSVM\_Value** objects are strictly equal, and **false** indicates the opposite. |

**Returns**

| Type | Description |
| :-- | :-- |
| JSVM\_EXTERN [JSVM\_Status](../jsvm-types-h/document.md#jsvm_status) | 
Returns a JSVM status code.

[JSVM\_OK](../jsvm-types-h/document.md#jsvm_status): operation successful.

[JSVM\_PENDING\_EXCEPTION](../jsvm-types-h/document.md#jsvm_status): pending exception.

 |

#### \[h2\]OH\_JSVM\_Equals()

JSVM\_EXTERN JSVM\_Status OH\_JSVM\_Equals(JSVM\_Env env,JSVM\_Value lhs,JSVM\_Value rhs,bool\* result)

**Description**

Provides a behavior similar to calling the loose equality algorithm (==). Regardless of the JavaScript value type, **true** is returned as long as the values are equal.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [JSVM\_Env](../../structs/jsvm-env/document.md) env | Environment for calling the JSVM-API. |
| [JSVM\_Value](../../structs/jsvm-value/document.md) lhs | JavaScript value to be checked. |
| [JSVM\_Value](../../structs/jsvm-value/document.md) rhs | JavaScript value to be checked. |
| bool\* result | Pointer to the check result. The value **true** indicates that two **JSVM\_Value** objects are loosely equal, and **false** indicates the opposite. |

**Returns**

| Type | Description |
| :-- | :-- |
| JSVM\_EXTERN [JSVM\_Status](../jsvm-types-h/document.md#jsvm_status) | 
Returns a JSVM status code.

[JSVM\_OK](../jsvm-types-h/document.md#jsvm_status): operation successful.

[JSVM\_PENDING\_EXCEPTION](../jsvm-types-h/document.md#jsvm_status): pending exception.

 |

#### \[h2\]OH\_JSVM\_DetachArraybuffer()

JSVM\_EXTERN JSVM\_Status OH\_JSVM\_DetachArraybuffer(JSVM\_Env env,JSVM\_Value arraybuffer)

**Description**

Provides a behavior similar to calling the **detach** operation of **ArrayBuffer**.

**Since**: 11

**Parameters**

| Name | Description |
| :-- | :-- |
| [JSVM\_Env](../../structs/jsvm-env/document.md) env | Environment for calling the JSVM-API. |
| [JSVM\_Value](../../structs/jsvm-value/document.md) arraybuffer | JavaScript **ArrayBuffer** to be detached. |

**Returns**

| Type | Description |
| :-- | :-- |
| JSVM\_EXTERN [JSVM\_Status](../jsvm-types-h/document.md#jsvm_status) | 
Returns a JSVM status code.

[JSVM\_OK](../jsvm-types-h/document.md#jsvm_status): operation successful.

[JSVM\_DETACHABLE\_ARRAYBUFFER\_EXPECTED](../jsvm-types-h/document.md#jsvm_status): ArrayBuffer expected. This code is returned if the input parameter is not an analyzable **ArrayBuffer**.

 |

#### \[h2\]OH\_JSVM\_IsDetachedArraybuffer()

JSVM\_EXTERN JSVM\_Status OH\_JSVM\_IsDetachedArraybuffer(JSVM\_Env env,JSVM\_Value value,bool\* result)

**Description**

Provides a behavior similar to calling the **IsDetachedBuffer** operation of **ArrayBuffer**.

**Since**: 11

**Parameters**

| Name | Description |
| :-- | :-- |
| [JSVM\_Env](../../structs/jsvm-env/document.md) env | Environment for calling the JSVM-API. |
| [JSVM\_Value](../../structs/jsvm-value/document.md) value | JavaScript **ArrayBuffer** to be checked. |
| bool\* result | Pointer to the check result. The value **true** indicates that the **ArrayBuffer** is detached, and **false** indicates the opposite. |

**Returns**

| Type | Description |
| :-- | :-- |
| JSVM\_EXTERN [JSVM\_Status](../jsvm-types-h/document.md#jsvm_status) | 
Returns a JSVM status code.

[JSVM\_OK](../jsvm-types-h/document.md#jsvm_status): operation successful.

 |

#### \[h2\]OH\_JSVM\_GetPropertyNames()

JSVM\_EXTERN JSVM\_Status OH\_JSVM\_GetPropertyNames(JSVM\_Env env,JSVM\_Value object,JSVM\_Value\* result)

**Description**

Obtains the names of enumerable properties of an object as an array of characters. The properties of the object whose key is a symbol are not included.

**Since**: 11

**Parameters**

| Name | Description |
| :-- | :-- |
| [JSVM\_Env](../../structs/jsvm-env/document.md) env | Environment for calling the JSVM-API. |
| [JSVM\_Value](../../structs/jsvm-value/document.md) object | Object whose property is to be retrieved. |
| [JSVM\_Value](../../structs/jsvm-value/document.md)\* result | Pointer to an array of property names of the object. You can use **OH\_JSVM\_GetArrayLength** and **OH\_JSVM\_GetElement** to iterate the result. |

**Returns**

| Type | Description |
| :-- | :-- |
| JSVM\_EXTERN [JSVM\_Status](../jsvm-types-h/document.md#jsvm_status) | 
Returns a JSVM status code.

[JSVM\_OK](../jsvm-types-h/document.md#jsvm_status): operation successful.

[JSVM\_INVALID\_ARG](../jsvm-types-h/document.md#jsvm_status): invalid argument.

[JSVM\_GENERIC\_FAILURE](../jsvm-types-h/document.md#jsvm_status): generic failure due to unknown reasons.

 |

#### \[h2\]OH\_JSVM\_GetAllPropertyNames()

JSVM\_EXTERN JSVM\_Status OH\_JSVM\_GetAllPropertyNames(JSVM\_Env env,JSVM\_Value object,JSVM\_KeyCollectionMode keyMode,JSVM\_KeyFilter keyFilter,JSVM\_KeyConversion keyConversion,JSVM\_Value\* result)

**Description**

Obtains all available property names of the object.

**Since**: 11

**Parameters**

| Name | Description |
| :-- | :-- |
| [JSVM\_Env](../../structs/jsvm-env/document.md) env | Environment for calling the JSVM-API. |
| [JSVM\_Value](../../structs/jsvm-value/document.md) object | Object from which the properties are retrieved. |
| [JSVM\_KeyCollectionMode](../jsvm-types-h/document.md#jsvm_keycollectionmode) keyMode | Key collection mode for retrieving the prototype properties. |
| [JSVM\_KeyFilter](../jsvm-types-h/document.md#jsvm_keyfilter) keyFilter | Key filter for properties to be retrieved (enumerable/readable/writable). |
| [JSVM\_KeyConversion](../jsvm-types-h/document.md#jsvm_keyconversion) keyConversion | Key conversion mode, which determines whether to convert a number to a string. |
| [JSVM\_Value](../../structs/jsvm-value/document.md)\* result | Pointer to an array of property names of the object. You can use **OH\_JSVM\_GetArrayLength** and **OH\_JSVM\_GetElement** to iterate the result. |

**Returns**

| Type | Description |
| :-- | :-- |
| JSVM\_EXTERN [JSVM\_Status](../jsvm-types-h/document.md#jsvm_status) | 
Returns a JSVM status code.

[JSVM\_OK](../jsvm-types-h/document.md#jsvm_status): operation successful.

[JSVM\_INVALID\_ARG](../jsvm-types-h/document.md#jsvm_status): invalid argument.

[JSVM\_GENERIC\_FAILURE](../jsvm-types-h/document.md#jsvm_status): generic failure due to unknown reasons.

 |

#### \[h2\]OH\_JSVM\_SetProperty()

JSVM\_EXTERN JSVM\_Status OH\_JSVM\_SetProperty(JSVM\_Env env,JSVM\_Value object,JSVM\_Value key,JSVM\_Value value)

**Description**

Sets the **key** property for the input object.

**Since**: 11

**Parameters**

| Name | Description |
| :-- | :-- |
| [JSVM\_Env](../../structs/jsvm-env/document.md) env | Environment for calling the JSVM-API. |
| [JSVM\_Value](../../structs/jsvm-value/document.md) object | Object whose property is to be set. |
| [JSVM\_Value](../../structs/jsvm-value/document.md) key | Name of the property to be set. |
| [JSVM\_Value](../../structs/jsvm-value/document.md) value | Property value. |

**Returns**

| Type | Description |
| :-- | :-- |
| JSVM\_EXTERN [JSVM\_Status](../jsvm-types-h/document.md#jsvm_status) | 
Returns a JSVM status code.

[JSVM\_OK](../jsvm-types-h/document.md#jsvm_status): operation successful.

[JSVM\_GENERIC\_FAILURE](../jsvm-types-h/document.md#jsvm_status): generic failure due to unknown reasons.

[JSVM\_PENDING\_EXCEPTION](../jsvm-types-h/document.md#jsvm_status): pending exception.

 |

#### \[h2\]OH\_JSVM\_GetProperty()

JSVM\_EXTERN JSVM\_Status OH\_JSVM\_GetProperty(JSVM\_Env env,JSVM\_Value object,JSVM\_Value key,JSVM\_Value\* result)

**Description**

Obtains the **key** property from the input object.

**Since**: 11

**Parameters**

| Name | Description |
| :-- | :-- |
| [JSVM\_Env](../../structs/jsvm-env/document.md) env | Environment for calling the JSVM-API. |
| [JSVM\_Value](../../structs/jsvm-value/document.md) object | Object from which the property is retrieved. |
| [JSVM\_Value](../../structs/jsvm-value/document.md) key | Name of the property to be retrieved. |
| [JSVM\_Value](../../structs/jsvm-value/document.md)\* result | Pointer to the property value. |

**Returns**

| Type | Description |
| :-- | :-- |
| JSVM\_EXTERN [JSVM\_Status](../jsvm-types-h/document.md#jsvm_status) | 
Returns a JSVM status code.

[JSVM\_OK](../jsvm-types-h/document.md#jsvm_status): operation successful.

[JSVM\_GENERIC\_FAILURE](../jsvm-types-h/document.md#jsvm_status): generic failure due to unknown reasons.

[JSVM\_PENDING\_EXCEPTION](../jsvm-types-h/document.md#jsvm_status): pending exception.

 |

#### \[h2\]OH\_JSVM\_HasProperty()

JSVM\_EXTERN JSVM\_Status OH\_JSVM\_HasProperty(JSVM\_Env env,JSVM\_Value object,JSVM\_Value key,bool\* result)

**Description**

Checks whether the input object has the **key** property.

**Since**: 11

**Parameters**

| Name | Description |
| :-- | :-- |
| [JSVM\_Env](../../structs/jsvm-env/document.md) env | Environment for calling the JSVM-API. |
| [JSVM\_Value](../../structs/jsvm-value/document.md) object | Object to be checked. |
| [JSVM\_Value](../../structs/jsvm-value/document.md) key | Name of the property to be checked. |
| bool\* result | Pointer to the check result. The value **true** indicates that the input object has the **key** property, and **false** indicates the opposite. |

**Returns**

| Type | Description |
| :-- | :-- |
| JSVM\_EXTERN [JSVM\_Status](../jsvm-types-h/document.md#jsvm_status) | 
Returns a JSVM status code.

[JSVM\_OK](../jsvm-types-h/document.md#jsvm_status): operation successful.

[JSVM\_GENERIC\_FAILURE](../jsvm-types-h/document.md#jsvm_status): generic failure due to unknown reasons.

[JSVM\_PENDING\_EXCEPTION](../jsvm-types-h/document.md#jsvm_status): pending exception.

 |

#### \[h2\]OH\_JSVM\_DeleteProperty()

JSVM\_EXTERN JSVM\_Status OH\_JSVM\_DeleteProperty(JSVM\_Env env,JSVM\_Value object,JSVM\_Value key,bool\* result)

**Description**

Deletes the **key** property from the object.

**Since**: 11

**Parameters**

| Name | Description |
| :-- | :-- |
| [JSVM\_Env](../../structs/jsvm-env/document.md) env | Environment for calling the JSVM-API. |
| [JSVM\_Value](../../structs/jsvm-value/document.md) object | Object to be checked. |
| [JSVM\_Value](../../structs/jsvm-value/document.md) key | Name of the property to be deleted. |
| bool\* result | Pointer to the operation result. The value **true** indicates that the property deletion is successful, and **false** indicates the opposite. **result** can be ignored by passing **NULL** to it. |

**Returns**

| Type | Description |
| :-- | :-- |
| JSVM\_EXTERN [JSVM\_Status](../jsvm-types-h/document.md#jsvm_status) | 
Returns a JSVM status code.

[JSVM\_OK](../jsvm-types-h/document.md#jsvm_status): operation successful.

[JSVM\_GENERIC\_FAILURE](../jsvm-types-h/document.md#jsvm_status): generic failure due to unknown reasons.

[JSVM\_PENDING\_EXCEPTION](../jsvm-types-h/document.md#jsvm_status): pending exception.

 |

#### \[h2\]OH\_JSVM\_HasOwnProperty()

JSVM\_EXTERN JSVM\_Status OH\_JSVM\_HasOwnProperty(JSVM\_Env env,JSVM\_Value object,JSVM\_Value key,bool\* result)

**Description**

Checks whether the input object has the **key** property. The key must be a string or symbol. Otherwise, an error is thrown. The JSVM-API does not perform any conversion between data types.

**Since**: 11

**Parameters**

| Name | Description |
| :-- | :-- |
| [JSVM\_Env](../../structs/jsvm-env/document.md) env | Environment for calling the JSVM-API. |
| [JSVM\_Value](../../structs/jsvm-value/document.md) object | Object to be checked. |
| [JSVM\_Value](../../structs/jsvm-value/document.md) key | Name of the property to be checked. |
| bool\* result | Pointer to the check result. The value **true** indicates that the input object has the **key** property, and **false** indicates the opposite. |

**Returns**

| Type | Description |
| :-- | :-- |
| JSVM\_EXTERN [JSVM\_Status](../jsvm-types-h/document.md#jsvm_status) | 
Returns a JSVM status code.

[JSVM\_OK](../jsvm-types-h/document.md#jsvm_status): operation successful.

[JSVM\_GENERIC\_FAILURE](../jsvm-types-h/document.md#jsvm_status): generic failure due to unknown reasons.

[JSVM\_NAME\_EXPECTED](../jsvm-types-h/document.md#jsvm_status): name expected. This code is returned if the input name is invalid.

[JSVM\_PENDING\_EXCEPTION](../jsvm-types-h/document.md#jsvm_status): pending exception.

 |

#### \[h2\]OH\_JSVM\_SetNamedProperty()

JSVM\_EXTERN JSVM\_Status OH\_JSVM\_SetNamedProperty(JSVM\_Env env,JSVM\_Value object,const char\* utf8name,JSVM\_Value value)

**Description**

Sets a property with a specified name. This method is equivalent to calling **OH\_JSVM\_SetProperty** to set the **utf8Name** property.

**Since**: 11

**Parameters**

| Name | Description |
| :-- | :-- |
| [JSVM\_Env](../../structs/jsvm-env/document.md) env | Environment for calling the JSVM-API. |
| [JSVM\_Value](../../structs/jsvm-value/document.md) object | Object whose property is to be set. |
| const char\* utf8name | Pointer to the name of the property to be set. |
| [JSVM\_Value](../../structs/jsvm-value/document.md) value | Property value. |

**Returns**

| Type | Description |
| :-- | :-- |
| JSVM\_EXTERN [JSVM\_Status](../jsvm-types-h/document.md#jsvm_status) | 
Returns a JSVM status code.

[JSVM\_OK](../jsvm-types-h/document.md#jsvm_status): operation successful.

[JSVM\_GENERIC\_FAILURE](../jsvm-types-h/document.md#jsvm_status): generic failure due to unknown reasons.

[JSVM\_PENDING\_EXCEPTION](../jsvm-types-h/document.md#jsvm_status): pending exception.

 |

#### \[h2\]OH\_JSVM\_GetNamedProperty()

JSVM\_EXTERN JSVM\_Status OH\_JSVM\_GetNamedProperty(JSVM\_Env env,JSVM\_Value object,const char\* utf8name,JSVM\_Value\* result)

**Description**

Obtains the named property. This method is equivalent to calling **OH\_JSVM\_GetProperty** to obtain the **utf8Name** property.

**Since**: 11

**Parameters**

| Name | Description |
| :-- | :-- |
| [JSVM\_Env](../../structs/jsvm-env/document.md) env | Environment for calling the JSVM-API. |
| [JSVM\_Value](../../structs/jsvm-value/document.md) object | Object from which the property is retrieved. |
| const char\* utf8name | Pointer to the name of the property to be obtained. |
| [JSVM\_Value](../../structs/jsvm-value/document.md)\* result | Pointer to the property value. |

**Returns**

| Type | Description |
| :-- | :-- |
| JSVM\_EXTERN [JSVM\_Status](../jsvm-types-h/document.md#jsvm_status) | 
Returns a JSVM status code.

[JSVM\_OK](../jsvm-types-h/document.md#jsvm_status): operation successful.

[JSVM\_GENERIC\_FAILURE](../jsvm-types-h/document.md#jsvm_status): generic failure due to unknown reasons.

[JSVM\_PENDING\_EXCEPTION](../jsvm-types-h/document.md#jsvm_status): pending exception.

 |

#### \[h2\]OH\_JSVM\_HasNamedProperty()

JSVM\_EXTERN JSVM\_Status OH\_JSVM\_HasNamedProperty(JSVM\_Env env,JSVM\_Value object,const char\* utf8name,bool\* result)

**Description**

Checks whether an object has the named property. This method is equivalent to calling **OH\_JSVM\_HasProperty** to check whether the object has the **utf8Name** property.

**Since**: 11

**Parameters**

| Name | Description |
| :-- | :-- |
| [JSVM\_Env](../../structs/jsvm-env/document.md) env | Environment for calling the JSVM-API. |
| [JSVM\_Value](../../structs/jsvm-value/document.md) object | Object to be checked. |
| const char\* utf8name | Pointer to the name of the property to be checked. |
| bool\* result | Pointer to the check result. The value **true** indicates that the input object has the **key** property, and **false** indicates the opposite. |

**Returns**

| Type | Description |
| :-- | :-- |
| JSVM\_EXTERN [JSVM\_Status](../jsvm-types-h/document.md#jsvm_status) | 
Returns a JSVM status code.

[JSVM\_OK](../jsvm-types-h/document.md#jsvm_status): operation successful.

[JSVM\_GENERIC\_FAILURE](../jsvm-types-h/document.md#jsvm_status): generic failure due to unknown reasons.

[JSVM\_PENDING\_EXCEPTION](../jsvm-types-h/document.md#jsvm_status): pending exception.

 |

#### \[h2\]OH\_JSVM\_SetElement()

JSVM\_EXTERN JSVM\_Status OH\_JSVM\_SetElement(JSVM\_Env env,JSVM\_Value object,uint32\_t index,JSVM\_Value value)

**Description**

Sets an element for the input object.

**Since**: 11

**Parameters**

| Name | Description |
| :-- | :-- |
| [JSVM\_Env](../../structs/jsvm-env/document.md) env | Environment for calling the JSVM-API. |
| [JSVM\_Value](../../structs/jsvm-value/document.md) object | Object whose property is to be set. |
| uint32\_t index | Index of the property to be set. |
| [JSVM\_Value](../../structs/jsvm-value/document.md) value | Property value. |

**Returns**

| Type | Description |
| :-- | :-- |
| JSVM\_EXTERN [JSVM\_Status](../jsvm-types-h/document.md#jsvm_status) | 
Returns a JSVM status code.

[JSVM\_OK](../jsvm-types-h/document.md#jsvm_status): operation successful.

[JSVM\_GENERIC\_FAILURE](../jsvm-types-h/document.md#jsvm_status): generic failure due to unknown reasons.

[JSVM\_PENDING\_EXCEPTION](../jsvm-types-h/document.md#jsvm_status): pending exception.

 |

#### \[h2\]OH\_JSVM\_GetElement()

JSVM\_EXTERN JSVM\_Status OH\_JSVM\_GetElement(JSVM\_Env env,JSVM\_Value object,uint32\_t index,JSVM\_Value\* result)

**Description**

Obtains the element at the requested index.

**Since**: 11

**Parameters**

| Name | Description |
| :-- | :-- |
| [JSVM\_Env](../../structs/jsvm-env/document.md) env | Environment for calling the JSVM-API. |
| [JSVM\_Value](../../structs/jsvm-value/document.md) object | Object whose property is to be retrieved. |
| uint32\_t index | Index of the property to be obtained. |
| [JSVM\_Value](../../structs/jsvm-value/document.md)\* result | Pointer to the property value. |

**Returns**

| Type | Description |
| :-- | :-- |
| JSVM\_EXTERN [JSVM\_Status](../jsvm-types-h/document.md#jsvm_status) | 
Returns a JSVM status code.

[JSVM\_OK](../jsvm-types-h/document.md#jsvm_status): operation successful.

[JSVM\_GENERIC\_FAILURE](../jsvm-types-h/document.md#jsvm_status): generic failure due to unknown reasons.

[JSVM\_PENDING\_EXCEPTION](../jsvm-types-h/document.md#jsvm_status): pending exception.

 |

#### \[h2\]OH\_JSVM\_HasElement()

JSVM\_EXTERN JSVM\_Status OH\_JSVM\_HasElement(JSVM\_Env env,JSVM\_Value object,uint32\_t index,bool\* result)

**Description**

Checks whether an input object has an element at the specified index. If yes, the JSVM-API returns **true**.

**Since**: 11

**Parameters**

| Name | Description |
| :-- | :-- |
| [JSVM\_Env](../../structs/jsvm-env/document.md) env | Environment for calling the JSVM-API. |
| [JSVM\_Value](../../structs/jsvm-value/document.md) object | Object to be checked. |
| uint32\_t index | Index to be checked. |
| bool\* result | Pointer to the check result. The value **true** indicates that the input object has the **key** property, and **false** indicates the opposite. |

**Returns**

| Type | Description |
| :-- | :-- |
| JSVM\_EXTERN [JSVM\_Status](../jsvm-types-h/document.md#jsvm_status) | 
Returns a JSVM status code.

[JSVM\_OK](../jsvm-types-h/document.md#jsvm_status): operation successful.

[JSVM\_GENERIC\_FAILURE](../jsvm-types-h/document.md#jsvm_status): generic failure due to unknown reasons.

[JSVM\_PENDING\_EXCEPTION](../jsvm-types-h/document.md#jsvm_status): pending exception.

 |

#### \[h2\]OH\_JSVM\_DeleteElement()

JSVM\_EXTERN JSVM\_Status OH\_JSVM\_DeleteElement(JSVM\_Env env,JSVM\_Value object,uint32\_t index,bool\* result)

**Description**

Deletes the element at the specified index from an object.

**Since**: 11

**Parameters**

| Name | Description |
| :-- | :-- |
| [JSVM\_Env](../../structs/jsvm-env/document.md) env | Environment for calling the JSVM-API. |
| [JSVM\_Value](../../structs/jsvm-value/document.md) object | Object to be checked. |
| uint32\_t index | Index of the element to be deleted. |
| bool\* result | Pointer to the operation result. The value **true** indicates that the element deletion is successful, and **false** indicates the opposite. |

**Returns**

| Type | Description |
| :-- | :-- |
| JSVM\_EXTERN [JSVM\_Status](../jsvm-types-h/document.md#jsvm_status) | 
Returns a JSVM status code.

[JSVM\_OK](../jsvm-types-h/document.md#jsvm_status): operation successful.

[JSVM\_GENERIC\_FAILURE](../jsvm-types-h/document.md#jsvm_status): generic failure due to unknown reasons.

[JSVM\_PENDING\_EXCEPTION](../jsvm-types-h/document.md#jsvm_status): pending exception.

 |

#### \[h2\]OH\_JSVM\_DefineProperties()

JSVM\_EXTERN JSVM\_Status OH\_JSVM\_DefineProperties(JSVM\_Env env,JSVM\_Value object,size\_t propertyCount,const JSVM\_PropertyDescriptor\* properties)

**Description**

Defines properties on a given object by using property descriptors. Through an array of property descriptors, this API sets the properties in the array in turn for the object.

**Since**: 11

**Parameters**

| Name | Description |
| :-- | :-- |
| [JSVM\_Env](../../structs/jsvm-env/document.md) env | Environment for calling the JSVM-API. |
| [JSVM\_Value](../../structs/jsvm-value/document.md) object | Object whose property is to be retrieved. |
| size\_t propertyCount | Pointer to the number of elements in the properties array. |
| [const JSVM\_PropertyDescriptor](../../structs/jsvm-propertydescriptor/document.md)\* properties | Pointer to the array of property descriptors. |

**Returns**

| Type | Description |
| :-- | :-- |
| JSVM\_EXTERN [JSVM\_Status](../jsvm-types-h/document.md#jsvm_status) | 
Returns a JSVM status code.

[JSVM\_OK](../jsvm-types-h/document.md#jsvm_status): operation successful.

[JSVM\_INVALID\_ARG](../jsvm-types-h/document.md#jsvm_status): invalid argument.

[JSVM\_GENERIC\_FAILURE](../jsvm-types-h/document.md#jsvm_status): generic failure due to unknown reasons.

[JSVM\_PENDING\_EXCEPTION](../jsvm-types-h/document.md#jsvm_status): pending exception.

 |

#### \[h2\]OH\_JSVM\_ObjectFreeze()

JSVM\_EXTERN JSVM\_Status OH\_JSVM\_ObjectFreeze(JSVM\_Env env,JSVM\_Value object)

**Description**

Freezes a JavaScript object. Once a JavaScript object is frozen, new properties cannot be added to it, existing properties cannot be removed, the enumerability, configurability, or writability of existing properties cannot be changed, and the values of existing properties and object prototypes cannot be changed.

**Since**: 11

**Parameters**

| Name | Description |
| :-- | :-- |
| [JSVM\_Env](../../structs/jsvm-env/document.md) env | Environment for calling the JSVM-API. |
| [JSVM\_Value](../../structs/jsvm-value/document.md) object | Object to be frozen. |

**Returns**

| Type | Description |
| :-- | :-- |
| JSVM\_EXTERN [JSVM\_Status](../jsvm-types-h/document.md#jsvm_status) | 
Returns a JSVM status code.

[JSVM\_OK](../jsvm-types-h/document.md#jsvm_status): operation successful.

[JSVM\_GENERIC\_FAILURE](../jsvm-types-h/document.md#jsvm_status): generic failure due to unknown reasons.

 |

#### \[h2\]OH\_JSVM\_ObjectSeal()

JSVM\_EXTERN JSVM\_Status OH\_JSVM\_ObjectSeal(JSVM\_Env env,JSVM\_Value object)

**Description**

Encapsulates a specified object, which prevents additions of properties and marks existing properties non-configurable.

**Since**: 11

**Parameters**

| Name | Description |
| :-- | :-- |
| [JSVM\_Env](../../structs/jsvm-env/document.md) env | Environment for calling the JSVM-API. |
| [JSVM\_Value](../../structs/jsvm-value/document.md) object | Object to be encapsulated. |

**Returns**

| Type | Description |
| :-- | :-- |
| JSVM\_EXTERN [JSVM\_Status](../jsvm-types-h/document.md#jsvm_status) | 
Returns a JSVM status code.

[JSVM\_OK](../jsvm-types-h/document.md#jsvm_status): operation successful.

[JSVM\_GENERIC\_FAILURE](../jsvm-types-h/document.md#jsvm_status): generic failure due to unknown reasons.

 |

#### \[h2\]OH\_JSVM\_CallFunction()

JSVM\_EXTERN JSVM\_Status OH\_JSVM\_CallFunction(JSVM\_Env env,JSVM\_Value recv,JSVM\_Value func,size\_t argc,const JSVM\_Value\* argv,JSVM\_Value\* result)

**Description**

Supports calling JavaScript function objects from native code, which is the main mechanism for JavaScript to call native code.

**Since**: 11

**Parameters**

| Name | Description |
| :-- | :-- |
| [JSVM\_Env](../../structs/jsvm-env/document.md) env | Environment for calling the JSVM-API. |
| [JSVM\_Value](../../structs/jsvm-value/document.md) recv | Value of **this** passed to the callee. |
| [JSVM\_Value](../../structs/jsvm-value/document.md) func | JavaScript function to be called. |
| size\_t argc | Number of elements in the argv array. |
| [const JSVM\_Value](../../structs/jsvm-value/document.md)\* argv | Pointer to the **JSVM\_values** array, representing the JavaScript values to be passed to the function as arguments. |
| [JSVM\_Value](../../structs/jsvm-value/document.md)\* result | Pointer to the returned JavaScript object. |

**Returns**

| Type | Description |
| :-- | :-- |
| JSVM\_EXTERN [JSVM\_Status](../jsvm-types-h/document.md#jsvm_status) | 
Returns a JSVM status code.

[JSVM\_OK](../jsvm-types-h/document.md#jsvm_status): operation successful.

[JSVM\_PENDING\_EXCEPTION](../jsvm-types-h/document.md#jsvm_status): pending exception.

[JSVM\_GENERIC\_FAILURE](../jsvm-types-h/document.md#jsvm_status): generic failure due to unknown reasons.

 |

#### \[h2\]OH\_JSVM\_CreateFunction()

JSVM\_EXTERN JSVM\_Status OH\_JSVM\_CreateFunction(JSVM\_Env env,const char\* utf8name,size\_t length,JSVM\_Callback cb,JSVM\_Value\* result)

**Description**

Supports creating function objects in native code, which is the main mechanism for JavaScript to call native code. After this call, the newly created function is no longer automatically visible in the script. Instead, you should explicitly set properties on any visible object in JavaScript to access the function from the script.

**Since**: 11

**Parameters**

| Name | Description |
| :-- | :-- |
| [JSVM\_Env](../../structs/jsvm-env/document.md) env | Environment for calling the JSVM-API. |
| const char\* utf8name | Pointer to the optional UTF-8-encoded name of the function. This is visible in JavaScript as the **name** property of the new function object. |
| size\_t length | Length of **utf8name** (in bytes) or **JSVM\_AUTO\_LENGTH** (if null-terminated). |
| [JSVM\_Callback](../../structs/jsvm-callbackstruct/document.md) cb | Native function to be called when the function object is called. For details, see [JSVM\_Callback](../../structs/jsvm-callbackstruct/document.md). |
| [JSVM\_Value](../../structs/jsvm-value/document.md)\* result | Pointer to the JavaScript function object of the newly created function. |

**Returns**

| Type | Description |
| :-- | :-- |
| JSVM\_EXTERN [JSVM\_Status](../jsvm-types-h/document.md#jsvm_status) | 
Returns a JSVM status code.

[JSVM\_OK](../jsvm-types-h/document.md#jsvm_status): operation successful.

[JSVM\_PENDING\_EXCEPTION](../jsvm-types-h/document.md#jsvm_status): pending exception.

 |

#### \[h2\]OH\_JSVM\_GetCbInfo()

JSVM\_EXTERN JSVM\_Status OH\_JSVM\_GetCbInfo(JSVM\_Env env,JSVM\_CallbackInfo cbinfo,size\_t\* argc,JSVM\_Value\* argv,JSVM\_Value\* thisArg,void\*\* data)

**Description**

Obtains detailed information about the callback, such as the parameter from the given callback information and the **this** pointer.

**Since**: 11

**Parameters**

| Name | Description |
| :-- | :-- |
| [JSVM\_Env](../../structs/jsvm-env/document.md) env | Environment for calling the JSVM-API. |
| [JSVM\_CallbackInfo](../../structs/jsvm-callbackinfo/document.md) cbinfo | Callback information. |
| size\_t\* argc | Pointer to the length of the provided **argv** array and actual number of input arguments. **argc** can be ignored by passing **NULL** to it. |
| [JSVM\_Value](../../structs/jsvm-value/document.md)\* argv | Pointer to the C array of **JSVM\_Value**, which is used to store copied arguments. If the number of arguments exceeds the provided number, only a requested number of arguments are copied. If fewer arguments are provided than declared, the rest of **argv** is filled with undefined **JSVM\_Value**s. **argv** can be ignored by passing **NULL** to it. |
| [JSVM\_Value](../../structs/jsvm-value/document.md)\* thisArg | Pointer to the JavaScript **this** argument. **thisArg** can be ignored by passing **NULL** to it. |
| void\*\* data | Double pointer to the callback data. **data** can be ignored by passing **NULL** to it. |

**Returns**

| Type | Description |
| :-- | :-- |
| JSVM\_EXTERN [JSVM\_Status](../jsvm-types-h/document.md#jsvm_status) | 
Returns a JSVM status code.

[JSVM\_OK](../jsvm-types-h/document.md#jsvm_status): operation successful.

 |

#### \[h2\]OH\_JSVM\_GetNewTarget()

JSVM\_EXTERN JSVM\_Status OH\_JSVM\_GetNewTarget(JSVM\_Env env,JSVM\_CallbackInfo cbinfo,JSVM\_Value\* result)

**Description**

Obtains the new target called by the constructor. If the current callback is not called by a constructor, the result is **NULL**.

**Since**: 11

**Parameters**

| Name | Description |
| :-- | :-- |
| [JSVM\_Env](../../structs/jsvm-env/document.md) env | Environment for calling the JSVM-API. |
| [JSVM\_CallbackInfo](../../structs/jsvm-callbackinfo/document.md) cbinfo | Callback information. |
| [JSVM\_Value](../../structs/jsvm-value/document.md)\* result | Pointer to the new target called by the constructor. |

**Returns**

| Type | Description |
| :-- | :-- |
| JSVM\_EXTERN [JSVM\_Status](../jsvm-types-h/document.md#jsvm_status) | 
Returns a JSVM status code.

[JSVM\_OK](../jsvm-types-h/document.md#jsvm_status): operation successful.

 |

#### \[h2\]OH\_JSVM\_NewInstance()

JSVM\_EXTERN JSVM\_Status OH\_JSVM\_NewInstance(JSVM\_Env env,JSVM\_Value constructor,size\_t argc,const JSVM\_Value\* argv,JSVM\_Value\* result)

**Description**

Instantiates a new JavaScript value by using the constructor represented by the given **JSVM\_Value**.

**Since**: 11

**Parameters**

| Name | Description |
| :-- | :-- |
| [JSVM\_Env](../../structs/jsvm-env/document.md) env | Environment for calling the JSVM-API. |
| [JSVM\_Value](../../structs/jsvm-value/document.md) constructor | JavaScript function that will be called as a constructor. |
| size\_t argc | Number of elements in the argv array. |
| [const JSVM\_Value](../../structs/jsvm-value/document.md)\* argv | Pointer to the JavaScript value array. **JSVM\_Value** indicates the parameter of the constructor. If **argc** is 0, **argc** can be ignored by passing **NULL** to it. |
| [JSVM\_Value](../../structs/jsvm-value/document.md)\* result | Pointer to the returned JavaScript object, which is the constructed object. |

**Returns**

| Type | Description |
| :-- | :-- |
| JSVM\_EXTERN [JSVM\_Status](../jsvm-types-h/document.md#jsvm_status) | 
Returns a JSVM status code.

[JSVM\_OK](../jsvm-types-h/document.md#jsvm_status): operation successful.

[JSVM\_PENDING\_EXCEPTION](../jsvm-types-h/document.md#jsvm_status): pending exception.

 |

#### \[h2\]OH\_JSVM\_DefineClass()

JSVM\_EXTERN JSVM\_Status OH\_JSVM\_DefineClass(JSVM\_Env env,const char\* utf8name,size\_t length,JSVM\_Callback constructor,size\_t propertyCount,const JSVM\_PropertyDescriptor\* properties,JSVM\_Value\* result)

**Description**

Defines a JavaScript class.

**Since**: 11

**Parameters**

| Name | Description |
| :-- | :-- |
| [JSVM\_Env](../../structs/jsvm-env/document.md) env | Environment for calling the JSVM-API. |
| const char\* utf8name | Pointer to the name of the JavaScript constructor. You are advised to use the C++ class name when wrapping a C++ class. |
| size\_t length | Length of **utf8name** (in bytes) or **JSVM\_AUTO\_LENGTH** (if null-terminated). |
| [JSVM\_Callback](../../structs/jsvm-callbackstruct/document.md) constructor | Callback of the constructor used to create class. When a C++ class is wrapped, this method must comply with **JSVM\_Callback**. It is a static member of the callback signature. C++ class constructors cannot be used. For details, see [JSVM\_Callback](../../structs/jsvm-callbackstruct/document.md). |
| size\_t propertyCount | Number of properties in the array. |
| [const JSVM\_PropertyDescriptor](../../structs/jsvm-propertydescriptor/document.md)\* properties | Pointer to the property descriptors, which are used to define the properties and methods of a class. |
| [JSVM\_Value](../../structs/jsvm-value/document.md)\* result | Pointer to the **JSVM\_Value** of the constructor of a class. |

**Returns**

| Type | Description |
| :-- | :-- |
| JSVM\_EXTERN [JSVM\_Status](../jsvm-types-h/document.md#jsvm_status) | 
Returns a JSVM status code.

[JSVM\_OK](../jsvm-types-h/document.md#jsvm_status): operation successful.

[JSVM\_PENDING\_EXCEPTION](../jsvm-types-h/document.md#jsvm_status): pending exception.

 |

#### \[h2\]OH\_JSVM\_Wrap()

JSVM\_EXTERN JSVM\_Status OH\_JSVM\_Wrap(JSVM\_Env env,JSVM\_Value jsObject,void\* nativeObject,JSVM\_Finalize finalizeCb,void\* finalizeHint,JSVM\_Ref\* result)

**Description**

Wraps a native instance in a JavaScript object, which can be retrieved using **OH\_JSVM\_Unwrap()** later.

**Since**: 11

**Parameters**

| Name | Description |
| :-- | :-- |
| [JSVM\_Env](../../structs/jsvm-env/document.md) env | Environment for calling the JSVM-API. |
| [JSVM\_Value](../../structs/jsvm-value/document.md) jsObject | JavaScript object that will wrap a native object. |
| void\* nativeObject | Pointer to the native instance wrapped in a JavaScript object. |
| [JSVM\_Finalize](../jsvm-types-h/document.md#jsvm_finalize) finalizeCb | Optional native callback, which can be used to release the native instance when the JavaScript object is garbage-collected. |
| void\* finalizeHint | Pointer to the optional context hint passed to the **finalize** callback. |
| [JSVM\_Ref](../../structs/jsvm-ref/document.md)\* result | Pointer to the optional reference to the wrapped object. |

**Returns**

| Type | Description |
| :-- | :-- |
| JSVM\_EXTERN [JSVM\_Status](../jsvm-types-h/document.md#jsvm_status) | 
Returns a JSVM status code.

[JSVM\_OK](../jsvm-types-h/document.md#jsvm_status): operation successful.

[JSVM\_INVALID\_ARG](../jsvm-types-h/document.md#jsvm_status): invalid argument.

[JSVM\_PENDING\_EXCEPTION](../jsvm-types-h/document.md#jsvm_status): pending exception.

 |

#### \[h2\]OH\_JSVM\_Unwrap()

JSVM\_EXTERN JSVM\_Status OH\_JSVM\_Unwrap(JSVM\_Env env,JSVM\_Value jsObject,void\*\* result)

**Description**

Unwraps a native instance in a JavaScript object. When the JavaScript code calls a method of a class or property accessor, the corresponding **JSVM\_Callback** is called. If the callback is for an instance method or accessor, the **this** parameter of the callback is the wrapper object. Then you can obtain the C++ instance as the call target by calling **OH\_JSVM\_Unwrap()** of the wrapper object.

**Since**: 11

**Parameters**

| Name | Description |
| :-- | :-- |
| [JSVM\_Env](../../structs/jsvm-env/document.md) env | Environment for calling the JSVM-API. |
| [JSVM\_Value](../../structs/jsvm-value/document.md) jsObject | Object associated with the native instance. |
| void\*\* result | Double pointer to the wrapped native instance. |

**Returns**

| Type | Description |
| :-- | :-- |
| JSVM\_EXTERN [JSVM\_Status](../jsvm-types-h/document.md#jsvm_status) | 
Returns a JSVM status code.

[JSVM\_OK](../jsvm-types-h/document.md#jsvm_status): operation successful.

[JSVM\_INVALID\_ARG](../jsvm-types-h/document.md#jsvm_status): invalid argument.

[JSVM\_PENDING\_EXCEPTION](../jsvm-types-h/document.md#jsvm_status): pending exception.

 |

#### \[h2\]OH\_JSVM\_RemoveWrap()

JSVM\_EXTERN JSVM\_Status OH\_JSVM\_RemoveWrap(JSVM\_Env env,JSVM\_Value jsObject,void\*\* result)

**Description**

Removes the wrap of the native instance, which is previously wrapped in **js\_object** by **OH\_JSVM\_Wrap()**. If the **finalize** callback is associated with wrap, it will not be called when the JavaScript object is garbage-collected.

**Since**: 11

**Parameters**

| Name | Description |
| :-- | :-- |
| [JSVM\_Env](../../structs/jsvm-env/document.md) env | Environment for calling the JSVM-API. |
| [JSVM\_Value](../../structs/jsvm-value/document.md) jsObject | Object associated with the native instance. |
| void\*\* result | Double pointer to the wrapped native instance. |

**Returns**

| Type | Description |
| :-- | :-- |
| JSVM\_EXTERN [JSVM\_Status](../jsvm-types-h/document.md#jsvm_status) | 
Returns a JSVM status code.

[JSVM\_OK](../jsvm-types-h/document.md#jsvm_status): operation successful.

[JSVM\_INVALID\_ARG](../jsvm-types-h/document.md#jsvm_status): invalid argument.

[JSVM\_PENDING\_EXCEPTION](../jsvm-types-h/document.md#jsvm_status): pending exception.

 |

#### \[h2\]OH\_JSVM\_TypeTagObject()

JSVM\_EXTERN JSVM\_Status OH\_JSVM\_TypeTagObject(JSVM\_Env env,JSVM\_Value value,const JSVM\_TypeTag\* typeTag)

**Description**

Associates the value of the **typeTag** pointer with a JavaScript object or an external value. You can call **OH\_JSVM\_CheckObjectTypeTag()** to check the type of the tag attached to the object to ensure that the object type is correct. If the object already has an associated type tag, **JSVM\_INVALID\_ARG** is returned.

**Since**: 11

**Parameters**

| Name | Description |
| :-- | :-- |
| [JSVM\_Env](../../structs/jsvm-env/document.md) env | Environment for calling the JSVM-API. |
| [JSVM\_Value](../../structs/jsvm-value/document.md) value | JavaScript object or external value to be tagged. |
| [const JSVM\_TypeTag](../../structs/jsvm-typetag/document.md)\* typeTag | Pointer to the type tag. |

**Returns**

| Type | Description |
| :-- | :-- |
| JSVM\_EXTERN [JSVM\_Status](../jsvm-types-h/document.md#jsvm_status) | 
Returns a JSVM status code.

[JSVM\_OK](../jsvm-types-h/document.md#jsvm_status): operation successful.

[JSVM\_INVALID\_ARG](../jsvm-types-h/document.md#jsvm_status): invalid argument.

[JSVM\_GENERIC\_FAILURE](../jsvm-types-h/document.md#jsvm_status): generic failure due to unknown reasons.

 |

#### \[h2\]OH\_JSVM\_CheckObjectTypeTag()

JSVM\_EXTERN JSVM\_Status OH\_JSVM\_CheckObjectTypeTag(JSVM\_Env env,JSVM\_Value value,const JSVM\_TypeTag\* typeTag,bool\* result)

**Description**

Checks the **typeTag** with the tag on a JavaScript object or external value. If they are the same tag, **result** is set to **true**. Otherwise, **result** is set to **false**.

**Since**: 11

**Parameters**

| Name | Description |
| :-- | :-- |
| [JSVM\_Env](../../structs/jsvm-env/document.md) env | Environment for calling the JSVM-API. |
| [JSVM\_Value](../../structs/jsvm-value/document.md) value | JavaScript object or external value to be checked. |
| [const JSVM\_TypeTag](../../structs/jsvm-typetag/document.md)\* typeTag | Pointer to the type tag used to compare any tags found on an object. |
| bool\* result | Pointer to the check result, indicating whether the specified type tag matches that on the object. If they are the same tag, **result** is set to **true**. Otherwise, **result** is set to **false**. |

**Returns**

| Type | Description |
| :-- | :-- |
| JSVM\_EXTERN [JSVM\_Status](../jsvm-types-h/document.md#jsvm_status) | 
Returns a JSVM status code.

[JSVM\_OK](../jsvm-types-h/document.md#jsvm_status): operation successful.

[JSVM\_GENERIC\_FAILURE](../jsvm-types-h/document.md#jsvm_status): generic failure due to unknown reasons.

 |

#### \[h2\]OH\_JSVM\_AddFinalizer()

JSVM\_EXTERN JSVM\_Status OH\_JSVM\_AddFinalizer(JSVM\_Env env,JSVM\_Value jsObject,void\* finalizeData,JSVM\_Finalize finalizeCb,void\* finalizeHint,JSVM\_Ref\* result)

**Description**

Adds the **JSVM\_Finalize** callback to a JavaScript object. This callback is called when the JavaScript object is garbage-collected. **OH\_JSVM\_AddFinalizer** can be called multiple times on a single JavaScript object.

**Since**: 11

**Parameters**

| Name | Description |
| :-- | :-- |
| [JSVM\_Env](../../structs/jsvm-env/document.md) env | Environment for calling the JSVM-API. |
| [JSVM\_Value](../../structs/jsvm-value/document.md) jsObject | JavaScript object associated with native data. |
| void\* finalizeData | Pointer to the optional data to be passed to **finalizeCb**. |
| [JSVM\_Finalize](../jsvm-types-h/document.md#jsvm_finalize) finalizeCb | Native callback used to release native data when a JavaScript object is garbage-collected. **JSVM\_Finalize** provides more details. |
| void\* finalizeHint | Pointer to the optional context hint passed to the **finalize** callback. |
| [JSVM\_Ref](../../structs/jsvm-ref/document.md)\* result | Pointer to the optional reference to a JavaScript object. |

**Returns**

| Type | Description |
| :-- | :-- |
| JSVM\_EXTERN [JSVM\_Status](../jsvm-types-h/document.md#jsvm_status) | 
Returns a JSVM status code.

[JSVM\_OK](../jsvm-types-h/document.md#jsvm_status): operation successful.

[JSVM\_INVALID\_ARG](../jsvm-types-h/document.md#jsvm_status): invalid argument.

 |

#### \[h2\]OH\_JSVM\_GetVersion()

JSVM\_EXTERN JSVM\_Status OH\_JSVM\_GetVersion(JSVM\_Env env,uint32\_t\* result)

**Description**

Obtains the latest JSVM-API version supported by the JSVM runtime. New JSVM-API APIs will be added to support more features. With this API, the new features of a certain JSVM version can be used, or callbacks are provided if a feature is not supported.

**Since**: 11

**Parameters**

| Name | Description |
| :-- | :-- |
| [JSVM\_Env](../../structs/jsvm-env/document.md) env | Environment for calling the JSVM-API. |
| uint32\_t\* result | Pointer to the JSVM-API of the latest version. |

**Returns**

| Type | Description |
| :-- | :-- |
| JSVM\_EXTERN [JSVM\_Status](../jsvm-types-h/document.md#jsvm_status) | 
Returns a JSVM status code.

[JSVM\_OK](../jsvm-types-h/document.md#jsvm_status): operation successful.

 |

#### \[h2\]OH\_JSVM\_GetVMInfo()

JSVM\_EXTERN JSVM\_Status OH\_JSVM\_GetVMInfo(JSVM\_VMInfo\* result)

**Description**

Obtains the VM information.

**Since**: 11

**Parameters**

| Name | Description |
| :-- | :-- |
| [JSVM\_VMInfo](../../structs/jsvm-vminfo/document.md)\* result | Pointer to the VM information. |

**Returns**

| Type | Description |
| :-- | :-- |
| JSVM\_EXTERN [JSVM\_Status](../jsvm-types-h/document.md#jsvm_status) | 
Returns a JSVM status code.

[JSVM\_OK](../jsvm-types-h/document.md#jsvm_status): operation successful.

 |

#### \[h2\]OH\_JSVM\_AdjustExternalMemory()

JSVM\_EXTERN JSVM\_Status OH\_JSVM\_AdjustExternalMemory(JSVM\_Env env,int64\_t changeInBytes,int64\_t\* result)

**Description**

Notifies the underlying VM of the size of externally allocated memory that remains active due to the JavaScript object. Registering externally allocated memory triggers global garbage collection more frequently than in other ways.

**Since**: 11

**Parameters**

| Name | Description |
| :-- | :-- |
| [JSVM\_Env](../../structs/jsvm-env/document.md) env | Environment for calling the JSVM-API. |
| int64\_t changeInBytes | Change in the size of externally allocated memory that remains active due to the JavaScript object. |
| int64\_t\* result | Pointer to the adjusted value. |

**Returns**

| Type | Description |
| :-- | :-- |
| JSVM\_EXTERN [JSVM\_Status](../jsvm-types-h/document.md#jsvm_status) | 
Returns a JSVM status code.

[JSVM\_OK](../jsvm-types-h/document.md#jsvm_status): operation successful.

 |

#### \[h2\]OH\_JSVM\_MemoryPressureNotification()

JSVM\_EXTERN JSVM\_Status OH\_JSVM\_MemoryPressureNotification(JSVM\_Env env,JSVM\_MemoryPressureLevel level)

**Description**

Notifies the VM of insufficient system memory and selectively triggers garbage collection.

**Since**: 11

**Parameters**

| Name | Description |
| :-- | :-- |
| [JSVM\_Env](../../structs/jsvm-env/document.md) env | Environment for calling the JSVM-API. |
| [JSVM\_MemoryPressureLevel](../jsvm-types-h/document.md#jsvm_memorypressurelevel) level | Memory pressure level to be set for the current VM. |

**Returns**

| Type | Description |
| :-- | :-- |
| JSVM\_EXTERN [JSVM\_Status](../jsvm-types-h/document.md#jsvm_status) | 
Returns a JSVM status code.

[JSVM\_OK](../jsvm-types-h/document.md#jsvm_status): operation successful.

 |

#### \[h2\]OH\_JSVM\_CreatePromise()

JSVM\_EXTERN JSVM\_Status OH\_JSVM\_CreatePromise(JSVM\_Env env,JSVM\_Deferred\* deferred,JSVM\_Value\* promise)

**Description**

Creates a deferred object and a JavaScript promise.

**Since**: 11

**Parameters**

| Name | Description |
| :-- | :-- |
| [JSVM\_Env](../../structs/jsvm-env/document.md) env | Environment for calling the JSVM-API. |
| [JSVM\_Deferred](../../structs/jsvm-deferred/document.md)\* deferred | Pointer to the new deferred object, which can be passed to **OH\_JSVM\_ResolveDeferred()** or **OH\_JSVM\_RejectDeferred()** to resolve **resp** or reject the promise. |
| [JSVM\_Value](../../structs/jsvm-value/document.md)\* promise | Pointer to the JavaScript promise associated with the deferred object. |

**Returns**

| Type | Description |
| :-- | :-- |
| JSVM\_EXTERN [JSVM\_Status](../jsvm-types-h/document.md#jsvm_status) | 
Returns a JSVM status code.

[JSVM\_OK](../jsvm-types-h/document.md#jsvm_status): operation successful.

[JSVM\_PENDING\_EXCEPTION](../jsvm-types-h/document.md#jsvm_status): pending exception.

[JSVM\_GENERIC\_FAILURE](../jsvm-types-h/document.md#jsvm_status): generic failure due to unknown reasons.

 |

#### \[h2\]OH\_JSVM\_ResolveDeferred()

JSVM\_EXTERN JSVM\_Status OH\_JSVM\_ResolveDeferred(JSVM\_Env env,JSVM\_Deferred deferred,JSVM\_Value resolution)

**Description**

Resolves a JavaScript promise by using the associated deferred object. It can only be used to resolve the JavaScript promise of the corresponding available deferred object. This means that promise must be created using **OH\_JSVM\_CreatePromise()**, and the object returned from this call must be retained so that it can be passed to this API.

**Since**: 11

**Parameters**

| Name | Description |
| :-- | :-- |
| [JSVM\_Env](../../structs/jsvm-env/document.md) env | Environment for calling the JSVM-API. |
| [JSVM\_Deferred](../../structs/jsvm-deferred/document.md) deferred | Deferred object whose associated promise is to be parsed. |
| [JSVM\_Value](../../structs/jsvm-value/document.md) resolution | Value used to resolve a promise. |

**Returns**

| Type | Description |
| :-- | :-- |
| JSVM\_EXTERN [JSVM\_Status](../jsvm-types-h/document.md#jsvm_status) | 
Returns a JSVM status code.

[JSVM\_OK](../jsvm-types-h/document.md#jsvm_status): operation successful.

[JSVM\_GENERIC\_FAILURE](../jsvm-types-h/document.md#jsvm_status): generic failure due to unknown reasons.

[JSVM\_PENDING\_EXCEPTION](../jsvm-types-h/document.md#jsvm_status): pending exception.

 |

#### \[h2\]OH\_JSVM\_RejectDeferred()

JSVM\_EXTERN JSVM\_Status OH\_JSVM\_RejectDeferred(JSVM\_Env env,JSVM\_Deferred deferred,JSVM\_Value rejection)

**Description**

Rejects a JavaScript promise by using the associated deferred object. It can only be used to reject the JavaScript promise of the corresponding available deferred object. This means that promise must be created using **OH\_JSVM\_CreatePromise()**, and the object returned from this call must be retained so that it can be passed to this API.

**Since**: 11

**Parameters**

| Name | Description |
| :-- | :-- |
| [JSVM\_Env](../../structs/jsvm-env/document.md) env | Environment for calling the JSVM-API. |
| [JSVM\_Deferred](../../structs/jsvm-deferred/document.md) deferred | Deferred object whose associated promise is to be parsed. |
| [JSVM\_Value](../../structs/jsvm-value/document.md) rejection | Value used to reject a promise. |

**Returns**

| Type | Description |
| :-- | :-- |
| JSVM\_EXTERN [JSVM\_Status](../jsvm-types-h/document.md#jsvm_status) | 
Returns a JSVM status code.

[JSVM\_OK](../jsvm-types-h/document.md#jsvm_status): operation successful.

[JSVM\_GENERIC\_FAILURE](../jsvm-types-h/document.md#jsvm_status): generic failure due to unknown reasons.

[JSVM\_PENDING\_EXCEPTION](../jsvm-types-h/document.md#jsvm_status): pending exception.

 |

#### \[h2\]OH\_JSVM\_IsPromise()

JSVM\_EXTERN JSVM\_Status OH\_JSVM\_IsPromise(JSVM\_Env env,JSVM\_Value value,bool\* isPromise)

**Description**

Checks whether a promise object is native.

**Since**: 11

**Parameters**

| Name | Description |
| :-- | :-- |
| [JSVM\_Env](../../structs/jsvm-env/document.md) env | Environment for calling the JSVM-API. |
| [JSVM\_Value](../../structs/jsvm-value/document.md) value | Value to be checked. |
| bool\* isPromise | Pointer to the check result. The value **true** indicates that the promise is a native promise object (which is created by the underlying engine), and **false** indicates the opposite. |

**Returns**

| Type | Description |
| :-- | :-- |
| JSVM\_EXTERN [JSVM\_Status](../jsvm-types-h/document.md#jsvm_status) | 
Returns a JSVM status code.

[JSVM\_OK](../jsvm-types-h/document.md#jsvm_status): operation successful.

 |

#### \[h2\]OH\_JSVM\_PromiseRegisterHandler()

JSVM\_EXTERN JSVM\_Status OH\_JSVM\_PromiseRegisterHandler(JSVM\_Env env,JSVM\_Value promise,JSVM\_Value onFulfilled,JSVM\_Value onRejected,JSVM\_Value\* result)

**Description**

Registers a handler for processing promise fulfillment and rejection.

**Since**: 18

**Parameters**

| Name | Description |
| :-- | :-- |
| [JSVM\_Env](../../structs/jsvm-env/document.md) env | Environment for calling the JSVM-API. |
| [JSVM\_Value](../../structs/jsvm-value/document.md) promise | Promise for which a handler needs to be registered. |
| [JSVM\_Value](../../structs/jsvm-value/document.md) onFulfilled | Handler to be invoked after the promise is fulfilled. |
| [JSVM\_Value](../../structs/jsvm-value/document.md) onRejected | Handler to be invoked after the promise is rejected. |
| [JSVM\_Value](../../structs/jsvm-value/document.md)\* result | Pointer to the new promise generated after a promise calls the **then** or **catch** API. |

**Returns**

| Type | Description |
| :-- | :-- |
| JSVM\_EXTERN [JSVM\_Status](../jsvm-types-h/document.md#jsvm_status) | 
Returns a JSVM status code.

[JSVM\_OK](../jsvm-types-h/document.md#jsvm_status): operation successful.

[JSVM\_INVALID\_ARG](../jsvm-types-h/document.md#jsvm_status): invalid argument. This code is returned if **env** or **promise** is empty, or **onFulfilled** and **onRejected** are both empty.

[JSVM\_INVALID\_TYPE](../jsvm-types-h/document.md#jsvm_status): invalid type. This code is returned if the promise, **onFulfilled**, or **onRejected** is not of the JavaScript type.

[JSVM\_PENDING\_EXCEPTION](../jsvm-types-h/document.md#jsvm_status): pending exception.

[JSVM\_GENERIC\_FAILURE](../jsvm-types-h/document.md#jsvm_status): generic failure. This code is returned if API execution error occurs.

 |

#### \[h2\]OH\_JSVM\_JsonParse()

JSVM\_EXTERN JSVM\_Status OH\_JSVM\_JsonParse(JSVM\_Env env,JSVM\_Value jsonString,JSVM\_Value\* result)

**Description**

Parses a JSON string and returns the parsed value.

**Since**: 11

**Parameters**

| Name | Description |
| :-- | :-- |
| [JSVM\_Env](../../structs/jsvm-env/document.md) env | Environment for calling the JSVM-API. |
| [JSVM\_Value](../../structs/jsvm-value/document.md) jsonString | String to be parsed. |
| [JSVM\_Value](../../structs/jsvm-value/document.md)\* result | Pointer to the value obtained by parsing. |

**Returns**

| Type | Description |
| :-- | :-- |
| JSVM\_EXTERN [JSVM\_Status](../jsvm-types-h/document.md#jsvm_status) | 
Returns a JSVM status code.

[JSVM\_OK](../jsvm-types-h/document.md#jsvm_status): operation successful.

[JSVM\_STRING\_EXPECTED](../jsvm-types-h/document.md#jsvm_status): string expected. This code is returned if the input parameter is not of the string type.

[JSVM\_GENERIC\_FAILURE](../jsvm-types-h/document.md#jsvm_status): generic failure due to unknown reasons.

[JSVM\_PENDING\_EXCEPTION](../jsvm-types-h/document.md#jsvm_status): pending exception.

 |

#### \[h2\]OH\_JSVM\_JsonStringify()

JSVM\_EXTERN JSVM\_Status OH\_JSVM\_JsonStringify(JSVM\_Env env,JSVM\_Value jsonObject,JSVM\_Value\* result)

**Description**

Converts an object into a JSON string and returns the converted string.

**Since**: 11

**Parameters**

| Name | Description |
| :-- | :-- |
| [JSVM\_Env](../../structs/jsvm-env/document.md) env | Environment for calling the JSVM-API. |
| [JSVM\_Value](../../structs/jsvm-value/document.md) jsonObject | Object to be stringified. |
| [JSVM\_Value](../../structs/jsvm-value/document.md)\* result | Pointer to the converted string. |

**Returns**

| Type | Description |
| :-- | :-- |
| JSVM\_EXTERN [JSVM\_Status](../jsvm-types-h/document.md#jsvm_status) | 
Returns a JSVM status code.

[JSVM\_OK](../jsvm-types-h/document.md#jsvm_status): operation successful.

[JSVM\_GENERIC\_FAILURE](../jsvm-types-h/document.md#jsvm_status): generic failure due to unknown reasons.

[JSVM\_PENDING\_EXCEPTION](../jsvm-types-h/document.md#jsvm_status): pending exception.

 |

#### \[h2\]OH\_JSVM\_CreateSnapshot()

JSVM\_EXTERN JSVM\_Status OH\_JSVM\_CreateSnapshot(JSVM\_VM vm,size\_t contextCount,const JSVM\_Env\* contexts,const char\*\* blobData,size\_t\* blobSize)

**Description**

Creates a VM startup snapshot.

**Since**: 11

**Parameters**

| Name | Description |
| :-- | :-- |
| [JSVM\_VM](../../structs/jsvm-vm/document.md) vm | Target environment in which the API will be called. |
| size\_t contextCount | Number of contexts. |
| [const JSVM\_Env](../../structs/jsvm-env/document.md)\* contexts | Pointer to the array of contexts to be added to the snapshot. |
| const char\*\* blobData | Double pointer to the snapshot data. |
| size\_t\* blobSize | Pointer to the size of snapshot data. |

**Returns**

| Type | Description |
| :-- | :-- |
| JSVM\_EXTERN [JSVM\_Status](../jsvm-types-h/document.md#jsvm_status) | 
Returns a JSVM status code.

[JSVM\_OK](../jsvm-types-h/document.md#jsvm_status): operation successful.

[JSVM\_GENERIC\_FAILURE](../jsvm-types-h/document.md#jsvm_status): generic failure due to unknown reasons.

 |

#### \[h2\]OH\_JSVM\_GetHeapStatistics()

JSVM\_EXTERN JSVM\_Status OH\_JSVM\_GetHeapStatistics(JSVM\_VM vm,JSVM\_HeapStatistics\* result)

**Description**

Obtains heap statistics of a VM.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [JSVM\_VM](../../structs/jsvm-vm/document.md) vm | VM that returns heap statistics. |
| [JSVM\_HeapStatistics](../../structs/jsvm-heapstatistics/document.md)\* result | Pointer to the heap statistics. |

**Returns**

| Type | Description |
| :-- | :-- |
| JSVM\_EXTERN [JSVM\_Status](../jsvm-types-h/document.md#jsvm_status) | 
Returns a JSVM status code.

[JSVM\_OK](../jsvm-types-h/document.md#jsvm_status): operation successful.

 |

#### \[h2\]OH\_JSVM\_StartCpuProfiler()

JSVM\_EXTERN JSVM\_Status OH\_JSVM\_StartCpuProfiler(JSVM\_VM vm,JSVM\_CpuProfiler\* result)

**Description**

Creates and starts a CPU profiler instance.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [JSVM\_VM](../../structs/jsvm-vm/document.md) vm | VM for starting the CPU profiler. |
| [JSVM\_CpuProfiler](../../structs/jsvm-cpuprofiler/document.md)\* result | Pointer to the CPU profiler. |

**Returns**

| Type | Description |
| :-- | :-- |
| JSVM\_EXTERN [JSVM\_Status](../jsvm-types-h/document.md#jsvm_status) | 
Returns a JSVM status code.

[JSVM\_OK](../jsvm-types-h/document.md#jsvm_status): operation successful.

 |

#### \[h2\]OH\_JSVM\_StopCpuProfiler()

JSVM\_EXTERN JSVM\_Status OH\_JSVM\_StopCpuProfiler(JSVM\_VM vm,JSVM\_CpuProfiler profiler,JSVM\_OutputStream stream,void\* streamData)

**Description**

Stops the CPU profiler and outputs the result to a stream.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [JSVM\_VM](../../structs/jsvm-vm/document.md) vm | VM for starting the CPU profiler. |
| [JSVM\_CpuProfiler](../../structs/jsvm-cpuprofiler/document.md) profiler | CPU profiler to be stopped. |
| [JSVM\_OutputStream](../jsvm-types-h/document.md#jsvm_outputstream) stream | Callback for the output stream. |
| void\* streamData | Pointer to the optional data passed to the output stream. For example, it can be a file stream that writes the sample data passed in the output stream to a file. |

**Returns**

| Type | Description |
| :-- | :-- |
| JSVM\_EXTERN [JSVM\_Status](../jsvm-types-h/document.md#jsvm_status) | 
Returns a JSVM status code.

[JSVM\_OK](../jsvm-types-h/document.md#jsvm_status): operation successful.

 |

#### \[h2\]OH\_JSVM\_TakeHeapSnapshot()

JSVM\_EXTERN JSVM\_Status OH\_JSVM\_TakeHeapSnapshot(JSVM\_VM vm,JSVM\_OutputStream stream,void\* streamData)

**Description**

Obtains a snapshot of the current heap and outputs it to a stream.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [JSVM\_VM](../../structs/jsvm-vm/document.md) vm | VM whose heap snapshot is to be obtained. |
| [JSVM\_OutputStream](../jsvm-types-h/document.md#jsvm_outputstream) stream | Callback for the output stream. |
| void\* streamData | Pointer to the optional data passed to the output stream. For example, it can be a file stream that writes the sample data passed in the output stream to a file. |

**Returns**

| Type | Description |
| :-- | :-- |
| JSVM\_EXTERN [JSVM\_Status](../jsvm-types-h/document.md#jsvm_status) | 
Returns a JSVM status code.

[JSVM\_OK](../jsvm-types-h/document.md#jsvm_status): operation successful.

 |

#### \[h2\]OH\_JSVM\_OpenInspector()

JSVM\_EXTERN JSVM\_Status OH\_JSVM\_OpenInspector(JSVM\_Env env,const char\* host,uint16\_t port)

**Description**

Opens an inspector instance on the specified host and port for debugging JS code.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [JSVM\_Env](../../structs/jsvm-env/document.md) env | Environment for calling the JSVM-API. |
| const char\* host | Pointer to the IP address of the host for listening for the inspector connection. |
| uint16\_t port | Port for listening for the inspector connection. |

**Returns**

| Type | Description |
| :-- | :-- |
| JSVM\_EXTERN [JSVM\_Status](../jsvm-types-h/document.md#jsvm_status) | 
Returns a JSVM status code.

[JSVM\_OK](../jsvm-types-h/document.md#jsvm_status): operation successful.

[JSVM\_PENDING\_EXCEPTION](../jsvm-types-h/document.md#jsvm_status): pending exception.

[JSVM\_GENERIC\_FAILURE](../jsvm-types-h/document.md#jsvm_status): generic failure due to unknown reasons.

 |

#### \[h2\]OH\_JSVM\_CloseInspector()

JSVM\_EXTERN JSVM\_Status OH\_JSVM\_CloseInspector(JSVM\_Env env)

**Description**

Closes all remaining inspector connections.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [JSVM\_Env](../../structs/jsvm-env/document.md) env | Environment for calling the JSVM-API. |

**Returns**

| Type | Description |
| :-- | :-- |
| JSVM\_EXTERN [JSVM\_Status](../jsvm-types-h/document.md#jsvm_status) | 
Returns a JSVM status code.

[JSVM\_OK](../jsvm-types-h/document.md#jsvm_status): operation successful.

[JSVM\_PENDING\_EXCEPTION](../jsvm-types-h/document.md#jsvm_status): pending exception.

[JSVM\_GENERIC\_FAILURE](../jsvm-types-h/document.md#jsvm_status): generic failure due to unknown reasons.

 |

#### \[h2\]OH\_JSVM\_WaitForDebugger()

JSVM\_EXTERN JSVM\_Status OH\_JSVM\_WaitForDebugger(JSVM\_Env env,bool breakNextLine)

**Description**

Waits for the host to set up a socket connection with an inspector. After the connection is set up, the application continues to run. **Runtime.runIfWaitingForDebugger** is sent.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [JSVM\_Env](../../structs/jsvm-env/document.md) env | Environment for calling the JSVM-API. |
| bool breakNextLine | Whether to break in the next line of JavaScript code. If this parameter is set to **true**, the next line of JavaScript code is suspended. You need to use the debugger to control the execution of the JavaScript code. If this parameter is set to **false**, the next line of JavaScript code is not interrupted. |

**Returns**

| Type | Description |
| :-- | :-- |
| JSVM\_EXTERN [JSVM\_Status](../jsvm-types-h/document.md#jsvm_status) | 
Returns a JSVM status code.

[JSVM\_OK](../jsvm-types-h/document.md#jsvm_status): operation successful.

[JSVM\_PENDING\_EXCEPTION](../jsvm-types-h/document.md#jsvm_status): pending exception.

[JSVM\_GENERIC\_FAILURE](../jsvm-types-h/document.md#jsvm_status): generic failure due to unknown reasons.

 |

#### \[h2\]OH\_JSVM\_DefineClassWithPropertyHandler()

JSVM\_EXTERN JSVM\_Status OH\_JSVM\_DefineClassWithPropertyHandler(JSVM\_Env env,const char\* utf8name,size\_t length,JSVM\_Callback constructor,size\_t propertyCount,const JSVM\_PropertyDescriptor\* properties,JSVM\_PropertyHandlerCfg propertyHandlerCfg,JSVM\_Callback callAsFunctionCallback,JSVM\_Value\* result)

**Description**

Defines a set of JavaScript class property handlers including **getter**, **setter**, **deleter**, and **enumerator** with the given class name, constructor, properties, and callback, which are called as callbacks.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [JSVM\_Env](../../structs/jsvm-env/document.md) env | Environment for calling the JSVM-API. |
| const char\* utf8name | Pointer to the name of the JavaScript class constructor. |
| size\_t length | Length of **utf8name** (in bytes) or **JSVM\_AUTO\_LENGTH** (if null-terminated). |
| [JSVM\_Callback](../../structs/jsvm-callbackstruct/document.md) constructor | Callback of the constructor used to create class. This method must be of the **JSVM\_Callback** type. The callback of the constructor must be a static member. C++ class constructors cannot be used. For details, see [JSVM\_Callback](../../structs/jsvm-callbackstruct/document.md). |
| size\_t propertyCount | Number of properties in the array. |
| [const JSVM\_PropertyDescriptor](../../structs/jsvm-propertydescriptor/document.md)\* properties | Pointer to the property descriptors of static data and instance data. For details about the properties, accessors, and methods of a class, see **JSVM\_PropertyDescriptor**. |
| [JSVM\_PropertyHandlerCfg](../../structs/jsvm-propertyhandlerconfigurationstruct/document.md) propertyHandlerCfg | Callback to be invoked when an instance object property is accessed. |
| [JSVM\_Callback](../../structs/jsvm-callbackstruct/document.md) callAsFunctionCallback | Callback to be invoked when an instance object is called as a function. |
| [JSVM\_Value](../../structs/jsvm-value/document.md)\* result | Pointer to the **JSVM\_Value** of the constructor of a JavaScript class. |

**Returns**

| Type | Description |
| :-- | :-- |
| JSVM\_EXTERN [JSVM\_Status](../jsvm-types-h/document.md#jsvm_status) | 
Returns a JSVM status code.

[JSVM\_OK](../jsvm-types-h/document.md#jsvm_status): operation successful.

[JSVM\_PENDING\_EXCEPTION](../jsvm-types-h/document.md#jsvm_status): pending exception.

[JSVM\_GENERIC\_FAILURE](../jsvm-types-h/document.md#jsvm_status): generic failure due to unknown reasons.

 |

#### \[h2\]OH\_JSVM\_IsLocked()

JSVM\_EXTERN JSVM\_Status OH\_JSVM\_IsLocked(JSVM\_Env env, bool\* isLocked)

**Description**

Checks whether the current thread holds a lock of the specified environment. Only the thread that holds the lock can use the environment.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [JSVM\_Env](../../structs/jsvm-env/document.md) env | Environment for calling the API. |
| bool\* isLocked | Pointer to the result indicating whether the current thread holds the environment lock. The value **true** indicates that the environment lock is held, and the value **false** indicates the opposite. |

**Returns**

| Type | Description |
| :-- | :-- |
| JSVM\_EXTERN [JSVM\_Status](../jsvm-types-h/document.md#jsvm_status) | 
Returns a JSVM status code.

[JSVM\_OK](../jsvm-types-h/document.md#jsvm_status): operation successful.

 |

#### \[h2\]OH\_JSVM\_AcquireLock()

JSVM\_EXTERN JSVM\_Status OH\_JSVM\_AcquireLock(JSVM\_Env env)

**Description**

Obtains a lock. Only the thread that holds the lock can use the environment.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [JSVM\_Env](../../structs/jsvm-env/document.md) env | Environment for calling the API. |

**Returns**

| Type | Description |
| :-- | :-- |
| JSVM\_EXTERN [JSVM\_Status](../jsvm-types-h/document.md#jsvm_status) | 
Returns a JSVM status code.

[JSVM\_OK](../jsvm-types-h/document.md#jsvm_status): operation successful.

 |

#### \[h2\]OH\_JSVM\_ReleaseLock()

JSVM\_EXTERN JSVM\_Status OH\_JSVM\_ReleaseLock(JSVM\_Env env)

**Description**

Releases a lock. Only the thread that holds the lock can use the environment.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [JSVM\_Env](../../structs/jsvm-env/document.md) env | Environment for calling the API. |

**Returns**

| Type | Description |
| :-- | :-- |
| JSVM\_EXTERN [JSVM\_Status](../jsvm-types-h/document.md#jsvm_status) | 
Returns a JSVM status code.

[JSVM\_OK](../jsvm-types-h/document.md#jsvm_status): operation successful.

 |

#### \[h2\]OH\_JSVM\_IsUndefined()

JSVM\_EXTERN JSVM\_Status OH\_JSVM\_IsUndefined(JSVM\_Env env,JSVM\_Value value,bool\* isUndefined)

**Description**

Checks whether the input value is **Undefined**. This API is equivalent to **value === undefined** in JavaScript code.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [JSVM\_Env](../../structs/jsvm-env/document.md) env | Environment for calling the JSVM-API. |
| [JSVM\_Value](../../structs/jsvm-value/document.md) value | **JSVM\_Value** to be checked. |
| bool\* isUndefined | Pointer to the check result. The value **true** indicates that the **JSVM\_Value** is **Undefined**, and **false** indicates the opposite. |

**Returns**

| Type | Description |
| :-- | :-- |
| JSVM\_EXTERN [JSVM\_Status](../jsvm-types-h/document.md#jsvm_status) | 
Returns a JSVM status code.

[JSVM\_OK](../jsvm-types-h/document.md#jsvm_status): operation successful.

 |

#### \[h2\]OH\_JSVM\_IsNull()

JSVM\_EXTERN JSVM\_Status OH\_JSVM\_IsNull(JSVM\_Env env,JSVM\_Value value,bool\* isNull)

**Description**

Checks whether the input value is a **Null** object. This API is equivalent to **value === null** in JavaScript code.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [JSVM\_Env](../../structs/jsvm-env/document.md) env | Environment for calling the JSVM-API. |
| [JSVM\_Value](../../structs/jsvm-value/document.md) value | **JSVM\_Value** to be checked. |
| bool\* isNull | Pointer to the check result. The value **true** indicates that the **JSVM\_Value** is **Null**, and **false** indicates the opposite. |

**Returns**

| Type | Description |
| :-- | :-- |
| JSVM\_EXTERN [JSVM\_Status](../jsvm-types-h/document.md#jsvm_status) | 
Returns a JSVM status code.

[JSVM\_OK](../jsvm-types-h/document.md#jsvm_status): operation successful.

 |

#### \[h2\]OH\_JSVM\_IsNullOrUndefined()

JSVM\_EXTERN JSVM\_Status OH\_JSVM\_IsNullOrUndefined(JSVM\_Env env,JSVM\_Value value,bool\* isNullOrUndefined)

**Description**

Checks whether the input value is **Null** or **Undefined**. This API is equivalent to **value == null** in JavaScript code.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [JSVM\_Env](../../structs/jsvm-env/document.md) env | Environment for calling the JSVM-API. |
| [JSVM\_Value](../../structs/jsvm-value/document.md) value | **JSVM\_Value** to be checked. |
| bool\* isNullOrUndefined | Pointer to the check result. The value **true** indicates that the **JSVM\_Value** is **Null** or **Undefined**, and **false** indicates the opposite. |

**Returns**

| Type | Description |
| :-- | :-- |
| JSVM\_EXTERN [JSVM\_Status](../jsvm-types-h/document.md#jsvm_status) | 
Returns a JSVM status code.

[JSVM\_OK](../jsvm-types-h/document.md#jsvm_status): operation successful.

 |

#### \[h2\]OH\_JSVM\_IsBoolean()

JSVM\_EXTERN JSVM\_Status OH\_JSVM\_IsBoolean(JSVM\_Env env,JSVM\_Value value,bool\* isBoolean)

**Description**

Checks whether the input value is a Boolean value. This API is equivalent to **typeof value ==='boolean'** in JavaScript code.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [JSVM\_Env](../../structs/jsvm-env/document.md) env | Environment for calling the JSVM-API. |
| [JSVM\_Value](../../structs/jsvm-value/document.md) value | **JSVM\_Value** to be checked. |
| bool\* isBoolean | Pointer to the check result. The value **true** indicates that the **JSVM\_Value** is of the Boolean type, and **false** indicates the opposite. |

**Returns**

| Type | Description |
| :-- | :-- |
| JSVM\_EXTERN [JSVM\_Status](../jsvm-types-h/document.md#jsvm_status) | 
Returns a JSVM status code.

[JSVM\_OK](../jsvm-types-h/document.md#jsvm_status): operation successful.

 |

#### \[h2\]OH\_JSVM\_IsNumber()

JSVM\_EXTERN JSVM\_Status OH\_JSVM\_IsNumber(JSVM\_Env env,JSVM\_Value value,bool\* isNumber)

**Description**

Checks whether the input value is a number. This API is equivalent to **typeof value === 'number'** in JavaScript code.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [JSVM\_Env](../../structs/jsvm-env/document.md) env | Environment for calling the JSVM-API. |
| [JSVM\_Value](../../structs/jsvm-value/document.md) value | **JSVM\_Value** to be checked. |
| bool\* isNumber | Pointer to the check result. The value **true** indicates that the **JSVM\_Value** is a number, and **false** indicates the opposite. |

**Returns**

| Type | Description |
| :-- | :-- |
| JSVM\_EXTERN [JSVM\_Status](../jsvm-types-h/document.md#jsvm_status) | 
Returns a JSVM status code.

[JSVM\_OK](../jsvm-types-h/document.md#jsvm_status): operation successful.

 |

#### \[h2\]OH\_JSVM\_IsString()

JSVM\_EXTERN JSVM\_Status OH\_JSVM\_IsString(JSVM\_Env env,JSVM\_Value value,bool\* isString)

**Description**

Checks whether the input value is a string. This API is equivalent to **typeof value === 'string'** in JavaScript code.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [JSVM\_Env](../../structs/jsvm-env/document.md) env | Environment for calling the JSVM-API. |
| [JSVM\_Value](../../structs/jsvm-value/document.md) value | **JSVM\_Value** to be checked. |
| bool\* isString | Pointer to the check result. The value **true** indicates that the **JSVM\_Value** is a string, and **false** indicates the opposite. |

**Returns**

| Type | Description |
| :-- | :-- |
| JSVM\_EXTERN [JSVM\_Status](../jsvm-types-h/document.md#jsvm_status) | 
Returns a JSVM status code.

[JSVM\_OK](../jsvm-types-h/document.md#jsvm_status): operation successful.

 |

#### \[h2\]OH\_JSVM\_IsSymbol()

JSVM\_EXTERN JSVM\_Status OH\_JSVM\_IsSymbol(JSVM\_Env env,JSVM\_Value value,bool\* isSymbol)

**Description**

Checks whether the input value is a symbol. This API is equivalent to **typeof value === 'symbol'** in JavaScript code.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [JSVM\_Env](../../structs/jsvm-env/document.md) env | Environment for calling the JSVM-API. |
| [JSVM\_Value](../../structs/jsvm-value/document.md) value | **JSVM\_Value** to be checked. |
| bool\* isSymbol | Pointer to the check result. The value **true** indicates that the **JSVM\_Value** is a symbol, and **false** indicates the opposite. |

**Returns**

| Type | Description |
| :-- | :-- |
| JSVM\_EXTERN [JSVM\_Status](../jsvm-types-h/document.md#jsvm_status) | 
Returns a JSVM status code.

[JSVM\_OK](../jsvm-types-h/document.md#jsvm_status): operation successful.

 |

#### \[h2\]OH\_JSVM\_IsFunction()

JSVM\_EXTERN JSVM\_Status OH\_JSVM\_IsFunction(JSVM\_Env env,JSVM\_Value value,bool\* isFunction)

**Description**

Checks whether the input value is a function. This API is equivalent to **typeof value === 'function'** in JavaScript code.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [JSVM\_Env](../../structs/jsvm-env/document.md) env | Environment for calling the JSVM-API. |
| [JSVM\_Value](../../structs/jsvm-value/document.md) value | **JSVM\_Value** to be checked. |
| bool\* isFunction | Pointer to the check result. The value **true** indicates that the **JSVM\_Value** is a function, and **false** indicates the opposite. |

**Returns**

| Type | Description |
| :-- | :-- |
| JSVM\_EXTERN [JSVM\_Status](../jsvm-types-h/document.md#jsvm_status) | 
Returns a JSVM status code.

[JSVM\_OK](../jsvm-types-h/document.md#jsvm_status): operation successful.

 |

#### \[h2\]OH\_JSVM\_IsObject()

JSVM\_EXTERN JSVM\_Status OH\_JSVM\_IsObject(JSVM\_Env env,JSVM\_Value value,bool\* isObject)

**Description**

Checks whether the input value is an object.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [JSVM\_Env](../../structs/jsvm-env/document.md) env | Environment for calling the JSVM-API. |
| [JSVM\_Value](../../structs/jsvm-value/document.md) value | **JSVM\_Value** to be checked. |
| bool\* isObject | Pointer to the check result. The value **true** indicates that the given value is an object, and **false** indicates the opposite. |

**Returns**

| Type | Description |
| :-- | :-- |
| JSVM\_EXTERN [JSVM\_Status](../jsvm-types-h/document.md#jsvm_status) | 
Returns a JSVM status code.

[JSVM\_OK](../jsvm-types-h/document.md#jsvm_status): operation successful.

 |

#### \[h2\]OH\_JSVM\_IsBigInt()

JSVM\_EXTERN JSVM\_Status OH\_JSVM\_IsBigInt(JSVM\_Env env,JSVM\_Value value,bool\* isBigInt)

**Description**

Checks whether the input value is a BigInt value. This API is equivalent to **typeof value === 'bigint'** in JavaScript code.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [JSVM\_Env](../../structs/jsvm-env/document.md) env | Environment for calling the JSVM-API. |
| [JSVM\_Value](../../structs/jsvm-value/document.md) value | **JSVM\_Value** to be checked. |
| bool\* isBigInt | Pointer to the check result. The value **true** indicates that the **JSVM\_Value** is of the BigInt type, and **false** indicates the opposite. |

**Returns**

| Type | Description |
| :-- | :-- |
| JSVM\_EXTERN [JSVM\_Status](../jsvm-types-h/document.md#jsvm_status) | 
Returns a JSVM status code.

[JSVM\_OK](../jsvm-types-h/document.md#jsvm_status): operation successful.

 |

#### \[h2\]OH\_JSVM\_CreateMap()

JSVM\_EXTERN JSVM\_Status OH\_JSVM\_CreateMap(JSVM\_Env env, JSVM\_Value\* result)

**Description**

Creates a JavaScript value of the Map type.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [JSVM\_Env](../../structs/jsvm-env/document.md) env | Environment for calling the JSVM-API. |
| [JSVM\_Value](../../structs/jsvm-value/document.md)\* result | Pointer to the **JSVM\_Value** of the JavaScript Map type. |

**Returns**

| Type | Description |
| :-- | :-- |
| [JSVM\_Status](../jsvm-types-h/document.md#jsvm_status) JSVM\_CDECL | 
Returns a JSVM status code.

[JSVM\_OK](../jsvm-types-h/document.md#jsvm_status): operation successful.

[JSVM\_INVALID\_ARG](../jsvm-types-h/document.md#jsvm_status): invalid argument.

 |

#### \[h2\]OH\_JSVM\_IsMap()

JSVM\_EXTERN JSVM\_Status OH\_JSVM\_IsMap(JSVM\_Env env,JSVM\_Value value,bool\* isMap)

**Description**

Checks whether the input value is of the Map type.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [JSVM\_Env](../../structs/jsvm-env/document.md) env | Environment for calling the JSVM-API. |
| [JSVM\_Value](../../structs/jsvm-value/document.md) value | **JSVM\_Value** to be checked. |
| bool\* isMap | Pointer to the check result. The value **true** indicates that the input value is of the Map type, and **false** indicates the opposite. |

**Returns**

| Type | Description |
| :-- | :-- |
| [JSVM\_Status](../jsvm-types-h/document.md#jsvm_status) JSVM\_CDECL | 
Returns a JSVM status code.

[JSVM\_OK](../jsvm-types-h/document.md#jsvm_status): operation successful.

[JSVM\_INVALID\_ARG](../jsvm-types-h/document.md#jsvm_status): invalid argument.

 |

#### \[h2\]OH\_JSVM\_IsConstructor()

JSVM\_EXTERN JSVM\_Status OH\_JSVM\_IsConstructor(JSVM\_Env env,JSVM\_Value value,bool\* isConstructor)

**Description**

Checks whether the input value is a constructor.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [JSVM\_Env](../../structs/jsvm-env/document.md) env | Environment for calling the JSVM-API. |
| [JSVM\_Value](../../structs/jsvm-value/document.md) value | **JSVM\_Value** to be checked. |
| bool\* isConstructor | Pointer to the check result. The value **true** indicates that the input value is a constructor, and **false** indicates the opposite. |

**Returns**

| Type | Description |
| :-- | :-- |
| [JSVM\_Status](../jsvm-types-h/document.md#jsvm_status) JSVM\_CDECL | 
Returns a JSVM status code.

[JSVM\_OK](../jsvm-types-h/document.md#jsvm_status): operation successful.

[JSVM\_INVALID\_ARG](../jsvm-types-h/document.md#jsvm_status): invalid argument.

 |

#### \[h2\]OH\_JSVM\_CreateRegExp()

JSVM\_EXTERN JSVM\_Status OH\_JSVM\_CreateRegExp(JSVM\_Env env,JSVM\_Value value,JSVM\_RegExpFlags flags,JSVM\_Value\* result)

**Description**

Creates a regular expression object corresponding to the input JavaScript string. This API may throw an exception.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [JSVM\_Env](../../structs/jsvm-env/document.md) env | Environment for calling the JSVM-API. |
| [JSVM\_Value](../../structs/jsvm-value/document.md) value | JavaScript string to be converted to a regular expression. |
| [JSVM\_RegExpFlags](../jsvm-types-h/document.md#jsvm_regexpflags) flags | Regular expression flags. |
| [JSVM\_Value](../../structs/jsvm-value/document.md)\* result | Pointer to the **JSVM\_Value** of JavaScript RegExp. |

**Returns**

| Type | Description |
| :-- | :-- |
| [JSVM\_Status](../jsvm-types-h/document.md#jsvm_status) JSVM\_CDECL | 
Returns a JSVM status code.

[JSVM\_OK](../jsvm-types-h/document.md#jsvm_status): operation successful.

[JSVM\_INVALID\_ARG](../jsvm-types-h/document.md#jsvm_status): invalid argument.

[JSVM\_PENDING\_EXCEPTION](../jsvm-types-h/document.md#jsvm_status): pending exception. This code is returned if an exception is thrown during API running.

 |

#### \[h2\]OH\_JSVM\_ObjectGetPrototypeOf()

JSVM\_EXTERN JSVM\_Status OH\_JSVM\_ObjectGetPrototypeOf(JSVM\_Env env,JSVM\_Value object,JSVM\_Value\* result)

**Description**

Obtains the prototype of a JavaScript object.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [JSVM\_Env](../../structs/jsvm-env/document.md) env | Environment for calling the JSVM-API. |
| [JSVM\_Value](../../structs/jsvm-value/document.md) object | JavaScript object whose prototype is to be returned. |
| [JSVM\_Value](../../structs/jsvm-value/document.md)\* result | Pointer to the prototype of a given object. |

**Returns**

| Type | Description |
| :-- | :-- |
| JSVM\_EXTERN [JSVM\_Status](../jsvm-types-h/document.md#jsvm_status) | 
Returns a JSVM status code.

[JSVM\_OK](../jsvm-types-h/document.md#jsvm_status): operation successful.

[JSVM\_INVALID\_ARG](../jsvm-types-h/document.md#jsvm_status): invalid argument.

[JSVM\_PENDING\_EXCEPTION](../jsvm-types-h/document.md#jsvm_status): pending exception. This code is returned if an exception is thrown during API running.

 |

#### \[h2\]OH\_JSVM\_ObjectSetPrototypeOf()

JSVM\_EXTERN JSVM\_Status OH\_JSVM\_ObjectSetPrototypeOf(JSVM\_Env env,JSVM\_Value object,JSVM\_Value prototype)

**Description**

Sets the prototype of a JavaScript object.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [JSVM\_Env](../../structs/jsvm-env/document.md) env | Environment for calling the JSVM-API. |
| [JSVM\_Value](../../structs/jsvm-value/document.md) object | JavaScript object whose prototype needs to be set. |
| [JSVM\_Value](../../structs/jsvm-value/document.md) prototype | Object prototype. |

**Returns**

| Type | Description |
| :-- | :-- |
| JSVM\_EXTERN [JSVM\_Status](../jsvm-types-h/document.md#jsvm_status) | 
Returns a JSVM status code.

[JSVM\_OK](../jsvm-types-h/document.md#jsvm_status): operation successful.

[JSVM\_INVALID\_ARG](../jsvm-types-h/document.md#jsvm_status): invalid argument.

[JSVM\_GENERIC\_FAILURE](../jsvm-types-h/document.md#jsvm_status): generic failure. This code is returned if the prototype fails to be set. For example, cyclically setting the prototype will trigger the failure.

[JSVM\_PENDING\_EXCEPTION](../jsvm-types-h/document.md#jsvm_status): pending exception. This code is returned if an exception is thrown during API running.

 |

#### \[h2\]OH\_JSVM\_CreateSet()

JSVM\_EXTERN JSVM\_Status OH\_JSVM\_CreateSet(JSVM\_Env env,JSVM\_Value\* result)

**Description**

Creates a JavaScript value of the Set type.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [JSVM\_Env](../../structs/jsvm-env/document.md) env | Environment for calling the JSVM-API. |
| [JSVM\_Value](../../structs/jsvm-value/document.md)\* result | Pointer to the created JavaScript value of the Set type. |

**Returns**

| Type | Description |
| :-- | :-- |
| JSVM\_EXTERN [JSVM\_Status](../jsvm-types-h/document.md#jsvm_status) | 
Returns a JSVM status code.

[JSVM\_OK](../jsvm-types-h/document.md#jsvm_status): operation successful.

[JSVM\_INVALID\_ARG](../jsvm-types-h/document.md#jsvm_status): invalid argument.

 |

#### \[h2\]OH\_JSVM\_IsSet()

JSVM\_EXTERN JSVM\_Status OH\_JSVM\_IsSet(JSVM\_Env env,JSVM\_Value value,bool\* isSet)

**Description**

Checks whether the specified object is of the Set type.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [JSVM\_Env](../../structs/jsvm-env/document.md) env | Environment for calling the JSVM-API. |
| [JSVM\_Value](../../structs/jsvm-value/document.md) value | Object to be checked. |
| bool\* isSet | Pointer to the check result. The value **true** indicates that the given object is of the Set type, and **false** indicates the opposite. |

**Returns**

| Type | Description |
| :-- | :-- |
| JSVM\_EXTERN [JSVM\_Status](../jsvm-types-h/document.md#jsvm_status) | 
Returns a JSVM status code.

[JSVM\_OK](../jsvm-types-h/document.md#jsvm_status): operation successful.

[JSVM\_INVALID\_ARG](../jsvm-types-h/document.md#jsvm_status): invalid argument.

 |

#### \[h2\]OH\_JSVM\_CoerceToBigInt()

JSVM\_EXTERN JSVM\_Status OH\_JSVM\_CoerceToBigInt(JSVM\_Env env,JSVM\_Value value,JSVM\_Value\* result)

**Description**

Implements the abstract operation **ToBigInt()**.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [JSVM\_Env](../../structs/jsvm-env/document.md) env | Environment for calling the JSVM-API. |
| [JSVM\_Value](../../structs/jsvm-value/document.md) value | JavaScript value to be forcibly converted. |
| [JSVM\_Value](../../structs/jsvm-value/document.md)\* result | Pointer to the converted JavaScript value. |

**Returns**

| Type | Description |
| :-- | :-- |
| JSVM\_EXTERN [JSVM\_Status](../jsvm-types-h/document.md#jsvm_status) | 
Returns a JSVM status code.

[JSVM\_OK](../jsvm-types-h/document.md#jsvm_status): operation successful.

[JSVM\_BIGINT\_EXPECTED](../jsvm-types-h/document.md#jsvm_status): BigInt expected. This code is returned if the input JavaScript value cannot be converted to a BigInt value.

 |

#### \[h2\]OH\_JSVM\_IsRegExp()

JSVM\_EXTERN JSVM\_Status OH\_JSVM\_IsRegExp(JSVM\_Env env,JSVM\_Value value,bool\* result)

**Description**

Checks whether the input value is a JavaScript RegExp object.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [JSVM\_Env](../../structs/jsvm-env/document.md) env | Environment for calling the JSVM-API. |
| [JSVM\_Value](../../structs/jsvm-value/document.md) value | **JSVM\_Value** to be checked. |
| bool\* result | Pointer to the check result. The value **true** indicates that the input value is a JavaScript RegExp object, and **false** indicates the opposite. |

**Returns**

| Type | Description |
| :-- | :-- |
| JSVM\_EXTERN [JSVM\_Status](../jsvm-types-h/document.md#jsvm_status) | 
Returns a JSVM status code.

[JSVM\_OK](../jsvm-types-h/document.md#jsvm_status): operation successful.

 |

#### \[h2\]OH\_JSVM\_CreateFunctionWithScript()

JSVM\_EXTERN JSVM\_Status OH\_JSVM\_CreateFunctionWithScript(JSVM\_Env env,const char\* funcName,size\_t length,size\_t argc,const JSVM\_Value\* argv,JSVM\_Value script,JSVM\_Value\* result)

**Description**

Creates a function with the given JavaScript as the function body.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [JSVM\_Env](../../structs/jsvm-env/document.md) env | Environment for calling the JSVM-API. |
| const char\* funcName | Pointer to the string containing the function name. If **NULL** is passed to it, an anonymous function is created. |
| size\_t length | Length of **funcName** (in bytes) or **JSVM\_AUTO\_LENGTH** (if null-terminated). |
| size\_t argc | Number of elements in the argv array. |
| [const JSVM\_Value](../../structs/jsvm-value/document.md)\* argv | Pointer to the **JSVM\_values** array, representing the JavaScript values to be passed to the function as arguments. |
| [JSVM\_Value](../../structs/jsvm-value/document.md) script | JavaScript string that is used as the function body. |
| [JSVM\_Value](../../structs/jsvm-value/document.md)\* result | Pointer to the JavaScript function object of the newly created function. |

**Returns**

| Type | Description |
| :-- | :-- |
| JSVM\_EXTERN [JSVM\_Status](../jsvm-types-h/document.md#jsvm_status) | 
Returns a JSVM status code.

[JSVM\_OK](../jsvm-types-h/document.md#jsvm_status): operation successful.

[JSVM\_GENERIC\_FAILURE](../jsvm-types-h/document.md#jsvm_status): generic failure. This code is returned if the input JavaScript cannot be compiled.

 |

#### \[h2\]OH\_JSVM\_PumpMessageLoop()

JSVM\_EXTERN JSVM\_Status OH\_JSVM\_PumpMessageLoop(JSVM\_VM vm,bool\* result)

**Description**

Starts the message loop in the VM. This message loop can be executed through the external event loop.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [JSVM\_VM](../../structs/jsvm-vm/document.md) vm | VM instance for starting a message loop. |
| bool\* result | Pointer to the operation result. The value **true** indicates that the message loop is started successfully, and **false** indicates the opposite. |

**Returns**

| Type | Description |
| :-- | :-- |
| JSVM\_EXTERN [JSVM\_Status](../jsvm-types-h/document.md#jsvm_status) | 
Returns a JSVM status code.

[JSVM\_OK](../jsvm-types-h/document.md#jsvm_status): operation successful.

 |

#### \[h2\]OH\_JSVM\_PerformMicrotaskCheckpoint()

JSVM\_EXTERN JSVM\_Status OH\_JSVM\_PerformMicrotaskCheckpoint(JSVM\_VM vm)

**Description**

Checks whether there are microtasks waiting in the queue. If yes, execute them.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [JSVM\_VM](../../structs/jsvm-vm/document.md) vm | VM instance in which microtasks are to be checked. |

**Returns**

| Type | Description |
| :-- | :-- |
| JSVM\_EXTERN [JSVM\_Status](../jsvm-types-h/document.md#jsvm_status) | 
Returns a JSVM status code.

[JSVM\_OK](../jsvm-types-h/document.md#jsvm_status): operation successful.

 |

#### \[h2\]OH\_JSVM\_IsCallable()

JSVM\_EXTERN JSVM\_Status OH\_JSVM\_IsCallable(JSVM\_Env env, JSVM\_Value value, bool\* isCallable)

**Description**

Checks whether the input value is callable.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [JSVM\_Env](../../structs/jsvm-env/document.md) env | Environment for calling the API. |
| [JSVM\_Value](../../structs/jsvm-value/document.md) value | JavaScript value to be checked. |
| bool\* isCallable | Pointer to the result indicating whether the given value is callable. The value **true** indicates that the given value is callable, and the value **false** indicates the opposite. |

**Returns**

| Type | Description |
| :-- | :-- |
| JSVM\_EXTERN [JSVM\_Status](../jsvm-types-h/document.md#jsvm_status) | 
Returns a JSVM status code.

[JSVM\_OK](../jsvm-types-h/document.md#jsvm_status): operation successful.

 |

#### \[h2\]OH\_JSVM\_RetainScript()

JSVM\_EXTERN JSVM\_Status OH\_JSVM\_RetainScript(JSVM\_Env env, JSVM\_Script script)

**Description**

Retains a **JSVM\_Script** and extends its lifecycle beyond the current scope.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [JSVM\_Env](../../structs/jsvm-env/document.md) env | Environment for calling the API. |
| [JSVM\_Script](../../structs/jsvm-script/document.md) script | JavaScript script to be retained. |

**Returns**

| Type | Description |
| :-- | :-- |
| JSVM\_EXTERN [JSVM\_Status](../jsvm-types-h/document.md#jsvm_status) | 
Returns a JSVM status code.

[JSVM\_OK](../jsvm-types-h/document.md#jsvm_status): operation successful.

[JSVM\_INVALID\_ARG](../jsvm-types-h/document.md#jsvm_status): invalid argument. This code is returned if the script is empty or has been retained.

 |

#### \[h2\]OH\_JSVM\_ReleaseScript()

JSVM\_EXTERN JSVM\_Status OH\_JSVM\_ReleaseScript(JSVM\_Env env, JSVM\_Script script)

**Description**

Releases the script retained by **OH\_JSVM\_RetainScript**. The released script cannot be used again.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [JSVM\_Env](../../structs/jsvm-env/document.md) env | Environment for calling the API. |
| [JSVM\_Script](../../structs/jsvm-script/document.md) script | JavaScript string that includes the script to be released. |

**Returns**

| Type | Description |
| :-- | :-- |
| JSVM\_EXTERN [JSVM\_Status](../jsvm-types-h/document.md#jsvm_status) | 
Returns a JSVM status code.

[JSVM\_OK](../jsvm-types-h/document.md#jsvm_status): operation successful.

[JSVM\_INVALID\_ARG](../jsvm-types-h/document.md#jsvm_status): invalid argument. This code is returned if the script is empty or has not been retained.

 |

#### \[h2\]OH\_JSVM\_OpenInspectorWithName()

JSVM\_EXTERN JSVM\_Status OH\_JSVM\_OpenInspectorWithName(JSVM\_Env env,int pid,const char\* name)

**Description**

Opens the **name** inspector and its corresponding Unix Domain port with the specified PID.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [JSVM\_Env](../../structs/jsvm-env/document.md) env | Environment for calling the API. |
| int pid | PID for identifying the inspector connection. |
| const char\* name | Pointer to the name of an inspector. If **nullptr** is passed in, the default name **jsvm** is used. |

**Returns**

| Type | Description |
| :-- | :-- |
| JSVM\_EXTERN [JSVM\_Status](../jsvm-types-h/document.md#jsvm_status) | 
Returns a JSVM status code.

[JSVM\_OK](../jsvm-types-h/document.md#jsvm_status): operation successful.

[JSVM\_PENDING\_EXCEPTION](../jsvm-types-h/document.md#jsvm_status): pending exception.

 |

#### \[h2\]OH\_JSVM\_CompileWasmModule()

JSVM\_EXTERN JSVM\_Status OH\_JSVM\_CompileWasmModule(JSVM\_Env env,const uint8\_t \*wasmBytecode,size\_t wasmBytecodeLength,const uint8\_t \*cacheData,size\_t cacheDataLength,bool \*cacheRejected,JSVM\_Value \*wasmModule)

**Description**

Compiles the WebAssembly bytecode to obtain a WebAssembly module. If the WebAssembly cache is provided, it will be deserialized first. If this API does not have the JIT permission, a log is printed to notify you.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [JSVM\_Env](../../structs/jsvm-env/document.md) env | Environment for calling the JSVM-API. |
| const uint8\_t \*wasmBytecode | Pointer to the WebAssembly bytecode. |
| size\_t wasmBytecodeLength | Length of the WebAssembly bytecode, in bytes. |
| const uint8\_t \*cacheData | Pointer to the optional WebAssembly cache. |
| size\_t cacheDataLength | Optional WebAssembly cache length, in bytes. |
| bool \*cacheRejected | Pointer to the operation result. The value **true** indicates that the provided WebAssembly cache is rejected by the engine, and **false** indicates the opposite. |
| [JSVM\_Value](../../structs/jsvm-value/document.md) \*wasmModule | Pointer to the generated WebAssembly module. |

**Returns**

| Type | Description |
| :-- | :-- |
| JSVM\_EXTERN [JSVM\_Status](../jsvm-types-h/document.md#jsvm_status) | 
Returns a JSVM status code.

[JSVM\_OK](../jsvm-types-h/document.md#jsvm_status): operation successful.

[JSVM\_INVALID\_ARG](../jsvm-types-h/document.md#jsvm_status): invalid argument. This code is returned if the **env** or **wasmBytecode** parameter is empty, or the input data length parameter is invalid.

[JSVM\_GENERIC\_FAILURE](../jsvm-types-h/document.md#jsvm_status): generic failure. This code is returned if the compilation fails.

[JSVM\_PENDING\_EXCEPTION](../jsvm-types-h/document.md#jsvm_status): pending exception.

[JSVM\_JIT\_MODE\_EXPECTED](../jsvm-types-h/document.md#jsvm_status): JIT mode expected.

 |

#### \[h2\]OH\_JSVM\_CompileWasmFunction()

JSVM\_EXTERN JSVM\_Status OH\_JSVM\_CompileWasmFunction(JSVM\_Env env,JSVM\_Value wasmModule,uint32\_t functionIndex,JSVM\_WasmOptLevel optLevel)

**Description**

Compiles a WebAssembly function with the specified index at a specified optimization level. If this API does not have the JIT permission, a log is printed to notify you.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [JSVM\_Env](../../structs/jsvm-env/document.md) env | Environment for calling the JSVM-API. |
| [JSVM\_Value](../../structs/jsvm-value/document.md) wasmModule | WebAssembly module where the function to be compiled is located. |
| uint32\_t functionIndex | Index of the function to be compiled. The index must be within the valid range. |
| [JSVM\_WasmOptLevel](../jsvm-types-h/document.md#jsvm_wasmoptlevel) optLevel | Optimization level. Currently, only the high optimization level is supported. |

**Returns**

| Type | Description |
| :-- | :-- |
| JSVM\_EXTERN [JSVM\_Status](../jsvm-types-h/document.md#jsvm_status) | 
Returns a JSVM status code.

[JSVM\_OK](../jsvm-types-h/document.md#jsvm_status): operation successful.

[JSVM\_INVALID\_ARG](../jsvm-types-h/document.md#jsvm_status): invalid argument. This code is returned if the **env** or **wasmModule** parameter is empty, or **wasmModule** is not a real WebAssembly module.

[JSVM\_GENERIC\_FAILURE](../jsvm-types-h/document.md#jsvm_status): generic failure. This code is returned if the function index is out of range or the compilation fails.

[JSVM\_PENDING\_EXCEPTION](../jsvm-types-h/document.md#jsvm_status): pending exception.

[JSVM\_JIT\_MODE\_EXPECTED](../jsvm-types-h/document.md#jsvm_status): JIT mode expected.

 |

#### \[h2\]OH\_JSVM\_IsWasmModuleObject()

JSVM\_EXTERN JSVM\_Status OH\_JSVM\_IsWasmModuleObject(JSVM\_Env env,JSVM\_Value value,bool\* result)

**Description**

Checks whether the given **JSVM\_Value** is a WebAssembly module.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [JSVM\_Env](../../structs/jsvm-env/document.md) env | Environment for calling the JSVM-API. |
| [JSVM\_Value](../../structs/jsvm-value/document.md) value | JavaScript value to be checked. |
| bool\* result | Pointer to the check result. The value **true** indicates that the given value is a WebAssembly module, and **false** indicates the opposite. |

**Returns**

| Type | Description |
| :-- | :-- |
| JSVM\_EXTERN [JSVM\_Status](../jsvm-types-h/document.md#jsvm_status) | 
Returns a JSVM status code.

[JSVM\_OK](../jsvm-types-h/document.md#jsvm_status): operation successful.

[JSVM\_INVALID\_ARG](../jsvm-types-h/document.md#jsvm_status): invalid argument. This code is returned if a null pointer argument is passed in.

 |

#### \[h2\]OH\_JSVM\_CreateWasmCache()

JSVM\_EXTERN JSVM\_Status OH\_JSVM\_CreateWasmCache(JSVM\_Env env,JSVM\_Value wasmModule,const uint8\_t\*\* data,size\_t\* length)

**Description**

Creates a WebAssembly cache. If this API does not have the JIT permission, a log is printed to notify you.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [JSVM\_Env](../../structs/jsvm-env/document.md) env | Environment for calling the JSVM-API. |
| [JSVM\_Value](../../structs/jsvm-value/document.md) wasmModule | Compiled WebAssembly module. |
| const uint8\_t\*\* data | Double pointer to the generated WebAssembly cache. |
| size\_t\* length | Pointer to the length of the generated WebAssembly cache, in bytes. |

**Returns**

| Type | Description |
| :-- | :-- |
| JSVM\_EXTERN [JSVM\_Status](../jsvm-types-h/document.md#jsvm_status) | 
Returns a JSVM status code.

[JSVM\_OK](../jsvm-types-h/document.md#jsvm_status): operation successful.

[JSVM\_INVALID\_ARG](../jsvm-types-h/document.md#jsvm_status): invalid argument. This code is returned if a null pointer argument is passed in.

[JSVM\_GENERIC\_FAILURE](../jsvm-types-h/document.md#jsvm_status): generic failure. This code is returned if the cache fails to be generated.

[JSVM\_JIT\_MODE\_EXPECTED](../jsvm-types-h/document.md#jsvm_status): JIT mode expected.

 |

#### \[h2\]OH\_JSVM\_ReleaseCache()

JSVM\_EXTERN JSVM\_Status OH\_JSVM\_ReleaseCache(JSVM\_Env env,const uint8\_t\* cacheData,JSVM\_CacheType cacheType)

**Description**

Releases the cache of a specified type.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [JSVM\_Env](../../structs/jsvm-env/document.md) env | Environment for calling the JSVM-API. |
| const uint8\_t\* cacheData | Pointer to the cache data to be released. Repeated release is an undefined behavior. |
| [JSVM\_CacheType](../jsvm-types-h/document.md#jsvm_cachetype) cacheType | Cache type. A generated cache can be released accordingly. |

**Returns**

| Type | Description |
| :-- | :-- |
| JSVM\_EXTERN [JSVM\_Status](../jsvm-types-h/document.md#jsvm_status) | 
Returns a JSVM status code.

[JSVM\_OK](../jsvm-types-h/document.md#jsvm_status): operation successful.

[JSVM\_INVALID\_ARG](../jsvm-types-h/document.md#jsvm_status): invalid argument. This code is returned if a null pointer argument is passed in or the **cacheType** argument is invalid.

 |

#### \[h2\]OH\_JSVM\_IsBigIntObject()

JSVM\_EXTERN JSVM\_Status OH\_JSVM\_IsBigIntObject(JSVM\_Env env,JSVM\_Value value,bool\* result)

**Description**

Checks whether the given **JSVM\_Value** is a BigInt object.

**Since**: 18

**Parameters**

| Name | Description |
| :-- | :-- |
| [JSVM\_Env](../../structs/jsvm-env/document.md) env | Environment for calling the JSVM-API. |
| [JSVM\_Value](../../structs/jsvm-value/document.md) value | JavaScript value to be checked. |
| bool\* result | Pointer to the check result. The value **true** indicates that the given value is a BigInt object, and **false** indicates the opposite. |

**Returns**

| Type | Description |
| :-- | :-- |
| JSVM\_EXTERN [JSVM\_Status](../jsvm-types-h/document.md#jsvm_status) | 
Returns a JSVM status code.

[JSVM\_OK](../jsvm-types-h/document.md#jsvm_status): operation successful.

[JSVM\_INVALID\_ARG](../jsvm-types-h/document.md#jsvm_status): invalid argument. This code is returned if a null pointer argument is passed in.

 |

#### \[h2\]OH\_JSVM\_IsBooleanObject()

JSVM\_EXTERN JSVM\_Status OH\_JSVM\_IsBooleanObject(JSVM\_Env env,JSVM\_Value value,bool\* result)

**Description**

Checks whether the given **JSVM\_Value** is a Boolean object.

**Since**: 18

**Parameters**

| Name | Description |
| :-- | :-- |
| [JSVM\_Env](../../structs/jsvm-env/document.md) env | Environment for calling the JSVM-API. |
| [JSVM\_Value](../../structs/jsvm-value/document.md) value | JavaScript value to be checked. |
| bool\* result | Pointer to the check result. The value **true** indicates that the given value is a Boolean object, and **false** indicates the opposite. |

**Returns**

| Type | Description |
| :-- | :-- |
| JSVM\_EXTERN [JSVM\_Status](../jsvm-types-h/document.md#jsvm_status) | 
Returns a JSVM status code.

[JSVM\_OK](../jsvm-types-h/document.md#jsvm_status): operation successful.

[JSVM\_INVALID\_ARG](../jsvm-types-h/document.md#jsvm_status): invalid argument. This code is returned if a null pointer argument is passed in.

 |

#### \[h2\]OH\_JSVM\_IsStringObject()

JSVM\_EXTERN JSVM\_Status OH\_JSVM\_IsStringObject(JSVM\_Env env,JSVM\_Value value,bool\* result)

**Description**

Checks whether the given **JSVM\_Value** is a string object.

**Since**: 18

**Parameters**

| Name | Description |
| :-- | :-- |
| [JSVM\_Env](../../structs/jsvm-env/document.md) env | Environment for calling the JSVM-API. |
| [JSVM\_Value](../../structs/jsvm-value/document.md) value | JavaScript value to be checked. |
| bool\* result | Pointer to the check result. The value **true** indicates that the given value is a string object, and **false** indicates the opposite. |

**Returns**

| Type | Description |
| :-- | :-- |
| JSVM\_EXTERN [JSVM\_Status](../jsvm-types-h/document.md#jsvm_status) | 
Returns a JSVM status code.

[JSVM\_OK](../jsvm-types-h/document.md#jsvm_status): operation successful.

[JSVM\_INVALID\_ARG](../jsvm-types-h/document.md#jsvm_status): invalid argument. This code is returned if a null pointer argument is passed in.

 |

#### \[h2\]OH\_JSVM\_IsNumberObject()

JSVM\_EXTERN JSVM\_Status OH\_JSVM\_IsNumberObject(JSVM\_Env env,JSVM\_Value value,bool\* result)

**Description**

Checks whether the given **JSVM\_Value** is a number object.

**Since**: 18

**Parameters**

| Name | Description |
| :-- | :-- |
| [JSVM\_Env](../../structs/jsvm-env/document.md) env | Environment for calling the JSVM-API. |
| [JSVM\_Value](../../structs/jsvm-value/document.md) value | JavaScript value to be checked. |
| bool\* result | Pointer to the check result. The value **true** indicates that the given value is a number object, and **false** indicates the opposite. |

**Returns**

| Type | Description |
| :-- | :-- |
| JSVM\_EXTERN [JSVM\_Status](../jsvm-types-h/document.md#jsvm_status) | 
Returns a JSVM status code.

[JSVM\_OK](../jsvm-types-h/document.md#jsvm_status): operation successful.

[JSVM\_INVALID\_ARG](../jsvm-types-h/document.md#jsvm_status): invalid argument. This code is returned if a null pointer argument is passed in.

 |

#### \[h2\]OH\_JSVM\_IsSymbolObject()

JSVM\_EXTERN JSVM\_Status OH\_JSVM\_IsSymbolObject(JSVM\_Env env,JSVM\_Value value,bool\* result)

**Description**

Checks whether the given **JSVM\_Value** is a symbol object.

**Since**: 18

**Parameters**

| Name | Description |
| :-- | :-- |
| [JSVM\_Env](../../structs/jsvm-env/document.md) env | Environment for calling the JSVM-API. |
| [JSVM\_Value](../../structs/jsvm-value/document.md) value | JavaScript value to be checked. |
| bool\* result | Pointer to the check result. The value **true** indicates that the given value is a symbol object, and **false** indicates the opposite. |

**Returns**

| Type | Description |
| :-- | :-- |
| JSVM\_EXTERN [JSVM\_Status](../jsvm-types-h/document.md#jsvm_status) | 
Returns a JSVM status code.

[JSVM\_OK](../jsvm-types-h/document.md#jsvm_status): operation successful.

[JSVM\_INVALID\_ARG](../jsvm-types-h/document.md#jsvm_status): invalid argument. This code is returned if a null pointer argument is passed in.

 |

#### \[h2\]OH\_JSVM\_GetSymbolAsyncIterator()

JSVM\_EXTERN JSVM\_Status OH\_JSVM\_GetSymbolAsyncIterator(JSVM\_Env env, JSVM\_Value\* result)

**Description**

Obtains the **Symbol.AsyncIterator** capability from the well-known symbol.

**Since**: 18

**Parameters**

| Name | Description |
| :-- | :-- |
| [JSVM\_Env](../../structs/jsvm-env/document.md) env | Environment for calling the JSVM-API. |
| [JSVM\_Value](../../structs/jsvm-value/document.md)\* result | Pointer to **Symbol.AsyncIterator** of the well-known symbol. |

**Returns**

| Type | Description |
| :-- | :-- |
| JSVM\_EXTERN [JSVM\_Status](../jsvm-types-h/document.md#jsvm_status) | 
Returns a JSVM status code.

[JSVM\_OK](../jsvm-types-h/document.md#jsvm_status): operation successful.

[JSVM\_INVALID\_ARG](../jsvm-types-h/document.md#jsvm_status): invalid argument. This code is returned if a null pointer argument is passed in.

 |

#### \[h2\]OH\_JSVM\_GetSymbolHasInstance()

JSVM\_EXTERN JSVM\_Status OH\_JSVM\_GetSymbolHasInstance(JSVM\_Env env, JSVM\_Value\* result)

**Description**

Obtains the **Symbol.HasInstance** capability from the well-known symbol.

**Since**: 18

**Parameters**

| Name | Description |
| :-- | :-- |
| [JSVM\_Env](../../structs/jsvm-env/document.md) env | Environment for calling the JSVM-API. |
| [JSVM\_Value](../../structs/jsvm-value/document.md)\* result | Pointer to **Symbol.HasInstance** of the well-Known symbol. |

**Returns**

| Type | Description |
| :-- | :-- |
| JSVM\_EXTERN [JSVM\_Status](../jsvm-types-h/document.md#jsvm_status) | 
Returns a JSVM status code.

[JSVM\_OK](../jsvm-types-h/document.md#jsvm_status): operation successful.

[JSVM\_INVALID\_ARG](../jsvm-types-h/document.md#jsvm_status): invalid argument. This code is returned if a null pointer argument is passed in.

 |

#### \[h2\]OH\_JSVM\_GetSymbolIsConcatSpreadable()

JSVM\_EXTERN JSVM\_Status OH\_JSVM\_GetSymbolIsConcatSpreadable(JSVM\_Env env, JSVM\_Value\* result)

**Description**

Obtains the **Symbol.IsConcatSpreadable** capability from the well-known symbol.

**Since**: 18

**Parameters**

| Name | Description |
| :-- | :-- |
| [JSVM\_Env](../../structs/jsvm-env/document.md) env | Environment for calling the JSVM-API. |
| [JSVM\_Value](../../structs/jsvm-value/document.md)\* result | Pointer to **Symbol.IsConcatSpreadable** of the well-Known symbol. |

**Returns**

| Type | Description |
| :-- | :-- |
| JSVM\_EXTERN [JSVM\_Status](../jsvm-types-h/document.md#jsvm_status) | 
Returns a JSVM status code.

[JSVM\_OK](../jsvm-types-h/document.md#jsvm_status): operation successful.

[JSVM\_INVALID\_ARG](../jsvm-types-h/document.md#jsvm_status): invalid argument. This code is returned if a null pointer argument is passed in.

 |

#### \[h2\]OH\_JSVM\_GetSymbolMatch()

JSVM\_EXTERN JSVM\_Status OH\_JSVM\_GetSymbolMatch(JSVM\_Env env, JSVM\_Value\* result)

**Description**

Obtains the **Symbol.Match** capability of the well-known symbol.

**Since**: 18

**Parameters**

| Name | Description |
| :-- | :-- |
| [JSVM\_Env](../../structs/jsvm-env/document.md) env | Environment for calling the JSVM-API. |
| [JSVM\_Value](../../structs/jsvm-value/document.md)\* result | Pointer to **Symbol.Match** of the well-known symbol. |

**Returns**

| Type | Description |
| :-- | :-- |
| JSVM\_EXTERN [JSVM\_Status](../jsvm-types-h/document.md#jsvm_status) | 
Returns a JSVM status code.

[JSVM\_OK](../jsvm-types-h/document.md#jsvm_status): operation successful.

[JSVM\_INVALID\_ARG](../jsvm-types-h/document.md#jsvm_status): invalid argument. This code is returned if a null pointer argument is passed in.

 |

#### \[h2\]OH\_JSVM\_GetSymbolReplace()

JSVM\_EXTERN JSVM\_Status OH\_JSVM\_GetSymbolReplace(JSVM\_Env env, JSVM\_Value\* result)

**Description**

Obtains the **Symbol.Replace** capability of the well-known symbol.

**Since**: 18

**Parameters**

| Name | Description |
| :-- | :-- |
| [JSVM\_Env](../../structs/jsvm-env/document.md) env | Environment for calling the JSVM-API. |
| [JSVM\_Value](../../structs/jsvm-value/document.md)\* result | Pointer to **Symbol.Replace** of the well-known symbol. |

**Returns**

| Type | Description |
| :-- | :-- |
| JSVM\_EXTERN [JSVM\_Status](../jsvm-types-h/document.md#jsvm_status) | 
Returns a JSVM status code.

[JSVM\_OK](../jsvm-types-h/document.md#jsvm_status): operation successful.

[JSVM\_INVALID\_ARG](../jsvm-types-h/document.md#jsvm_status): invalid argument. This code is returned if a null pointer argument is passed in.

 |

#### \[h2\]OH\_JSVM\_GetSymbolSearch()

JSVM\_EXTERN JSVM\_Status OH\_JSVM\_GetSymbolSearch(JSVM\_Env env, JSVM\_Value\* result)

**Description**

Obtains the **Symbol.Search** capability of the well-known symbol.

**Since**: 18

**Parameters**

| Name | Description |
| :-- | :-- |
| [JSVM\_Env](../../structs/jsvm-env/document.md) env | Environment for calling the JSVM-API. |
| [JSVM\_Value](../../structs/jsvm-value/document.md)\* result | Pointer to **Symbol.Search** of the well-known symbol. |

**Returns**

| Type | Description |
| :-- | :-- |
| JSVM\_EXTERN [JSVM\_Status](../jsvm-types-h/document.md#jsvm_status) | 
Returns a JSVM status code.

[JSVM\_OK](../jsvm-types-h/document.md#jsvm_status): operation successful.

[JSVM\_INVALID\_ARG](../jsvm-types-h/document.md#jsvm_status): invalid argument. This code is returned if a null pointer argument is passed in.

 |

#### \[h2\]OH\_JSVM\_GetSymbolSplit()

JSVM\_EXTERN JSVM\_Status OH\_JSVM\_GetSymbolSplit(JSVM\_Env env, JSVM\_Value\* result)

**Description**

Obtains the **Symbol.Split** capability of the well-known symbol.

**Since**: 18

**Parameters**

| Name | Description |
| :-- | :-- |
| [JSVM\_Env](../../structs/jsvm-env/document.md) env | Environment for calling the JSVM-API. |
| [JSVM\_Value](../../structs/jsvm-value/document.md)\* result | Pointer to **Symbol.Split** of the well-known symbol. |

**Returns**

| Type | Description |
| :-- | :-- |
| JSVM\_EXTERN [JSVM\_Status](../jsvm-types-h/document.md#jsvm_status) | 
Returns a JSVM status code.

[JSVM\_OK](../jsvm-types-h/document.md#jsvm_status): operation successful.

[JSVM\_INVALID\_ARG](../jsvm-types-h/document.md#jsvm_status): invalid argument. This code is returned if a null pointer argument is passed in.

 |

#### \[h2\]OH\_JSVM\_GetSymbolToPrimitive()

JSVM\_EXTERN JSVM\_Status OH\_JSVM\_GetSymbolToPrimitive(JSVM\_Env env, JSVM\_Value\* result)

**Description**

Obtains the **Symbol.ToPrimitive** capability of the well-known symbol.

**Since**: 18

**Parameters**

| Name | Description |
| :-- | :-- |
| [JSVM\_Env](../../structs/jsvm-env/document.md) env | Environment for calling the JSVM-API. |
| [JSVM\_Value](../../structs/jsvm-value/document.md)\* result | Pointer to **Symbol.ToPrimitive** of the well-Known symbol. |

**Returns**

| Type | Description |
| :-- | :-- |
| JSVM\_EXTERN [JSVM\_Status](../jsvm-types-h/document.md#jsvm_status) | 
Returns a JSVM status code.

[JSVM\_OK](../jsvm-types-h/document.md#jsvm_status): operation successful.

[JSVM\_INVALID\_ARG](../jsvm-types-h/document.md#jsvm_status): invalid argument. This code is returned if a null pointer argument is passed in.

 |

#### \[h2\]OH\_JSVM\_GetSymbolUnscopables()

JSVM\_EXTERN JSVM\_Status OH\_JSVM\_GetSymbolUnscopables(JSVM\_Env env, JSVM\_Value\* result)

**Description**

Obtains the **Symbol.Unscopables** capability of the well-known symbol.

**Since**: 18

**Parameters**

| Name | Description |
| :-- | :-- |
| [JSVM\_Env](../../structs/jsvm-env/document.md) env | Environment for calling the JSVM-API. |
| [JSVM\_Value](../../structs/jsvm-value/document.md)\* result | Pointer to **Symbol.Unscopables** of the well-Known symbol. |

**Returns**

| Type | Description |
| :-- | :-- |
| JSVM\_EXTERN [JSVM\_Status](../jsvm-types-h/document.md#jsvm_status) | 
Returns a JSVM status code.

[JSVM\_OK](../jsvm-types-h/document.md#jsvm_status): operation successful.

[JSVM\_INVALID\_ARG](../jsvm-types-h/document.md#jsvm_status): invalid argument. This code is returned if a null pointer argument is passed in.

 |

#### \[h2\]OH\_JSVM\_GetSymbolToStringTag()

JSVM\_EXTERN JSVM\_Status OH\_JSVM\_GetSymbolToStringTag(JSVM\_Env env, JSVM\_Value\* result)

**Description**

Obtains the **Symbol.ToStringTag** capability of the well-known symbol.

**Since**: 18

**Parameters**

| Name | Description |
| :-- | :-- |
| [JSVM\_Env](../../structs/jsvm-env/document.md) env | Environment for calling the JSVM-API. |
| [JSVM\_Value](../../structs/jsvm-value/document.md)\* result | Pointer to **Symbol.ToStringTag** of the well-Known symbol. |

**Returns**

| Type | Description |
| :-- | :-- |
| JSVM\_EXTERN [JSVM\_Status](../jsvm-types-h/document.md#jsvm_status) | 
Returns a JSVM status code.

[JSVM\_OK](../jsvm-types-h/document.md#jsvm_status): operation successful.

[JSVM\_INVALID\_ARG](../jsvm-types-h/document.md#jsvm_status): invalid argument. This code is returned if a null pointer argument is passed in.

 |

#### \[h2\]OH\_JSVM\_GetSymbolIterator()

JSVM\_EXTERN JSVM\_Status OH\_JSVM\_GetSymbolIterator(JSVM\_Env env, JSVM\_Value\* result)

**Description**

Obtains the **Symbol.Iterator** capability of the well-known symbol.

**Since**: 18

**Parameters**

| Name | Description |
| :-- | :-- |
| [JSVM\_Env](../../structs/jsvm-env/document.md) env | Environment for calling the JSVM-API. |
| [JSVM\_Value](../../structs/jsvm-value/document.md)\* result | Pointer to **Symbol.Iterator** of the well-known symbol. |

**Returns**

| Type | Description |
| :-- | :-- |
| JSVM\_EXTERN [JSVM\_Status](../jsvm-types-h/document.md#jsvm_status) | 
Returns a JSVM status code.

[JSVM\_OK](../jsvm-types-h/document.md#jsvm_status): operation successful.

[JSVM\_INVALID\_ARG](../jsvm-types-h/document.md#jsvm_status): invalid argument. This code is returned if a null pointer argument is passed in.

 |

#### \[h2\]OH\_JSVM\_TraceStart()

JSVM\_EXTERN JSVM\_Status OH\_JSVM\_TraceStart(size\_t count,const JSVM\_TraceCategory\* categories,const char\* tag,size\_t eventsCount)

**Description**

Starts collecting information of the specified trace categories for all JSVM runtime instances (thread-unsafe).

**Since**: 18

**Parameters**

| Name | Description |
| :-- | :-- |
| size\_t count | Number of trace categories. |
| [const JSVM\_TraceCategory](../jsvm-types-h/document.md#jsvm_tracecategory)\* categories | Pointer to the array of trace categories. |
| const char\* tag | Pointer to the tag defined and assigned to trace data. |
| size\_t eventsCount | Maximum number of trace events that can be stored. |

**Returns**

| Type | Description |
| :-- | :-- |
| JSVM\_EXTERN [JSVM\_Status](../jsvm-types-h/document.md#jsvm_status) | 
Returns a JSVM status code.

[JSVM\_OK](../jsvm-types-h/document.md#jsvm_status): operation successful.

[JSVM\_INVALID\_ARG](../jsvm-types-h/document.md#jsvm_status): invalid argument. This code is returned if **categories** or **count** is invalid.

 |

#### \[h2\]OH\_JSVM\_TraceStop()

JSVM\_EXTERN JSVM\_Status OH\_JSVM\_TraceStop(JSVM\_OutputStream stream, void\* streamData)

**Description**

Stops collecting information of a specified trace category for all JSVM runtime instances (thread-unsafe).

**Since**: 18

**Parameters**

| Name | Description |
| :-- | :-- |
| [JSVM\_OutputStream](../jsvm-types-h/document.md#jsvm_outputstream) stream | Callback for the output stream, which is used to receive trace data. |
| void\* streamData | Pointer to the output stream, which is used by the output stream callback to output data. |

**Returns**

| Type | Description |
| :-- | :-- |
| JSVM\_EXTERN [JSVM\_Status](../jsvm-types-h/document.md#jsvm_status) | 
Returns a JSVM status code.

[JSVM\_OK](../jsvm-types-h/document.md#jsvm_status): operation successful.

[JSVM\_INVALID\_ARG](../jsvm-types-h/document.md#jsvm_status): invalid argument. This code is returned if **stream** or **streamData** is empty.

 |

#### \[h2\]OH\_JSVM\_AddHandlerForGC()

JSVM\_EXTERN JSVM\_Status OH\_JSVM\_AddHandlerForGC(JSVM\_VM vm,JSVM\_CBTriggerTimeForGC triggerTime,JSVM\_HandlerForGC handler,JSVM\_GCType gcType,void\* userData)

**Description**

Adds a handler for GC to the VM.

**Since**: 18

**Parameters**

| Name | Description |
| :-- | :-- |
| [JSVM\_VM](../../structs/jsvm-vm/document.md) vm | Environment for calling the JSVM-API. |
| [JSVM\_CBTriggerTimeForGC](../jsvm-types-h/document.md#jsvm_cbtriggertimeforgc) triggerTime | Time when the GC callback is triggered. |
| [JSVM\_HandlerForGC](../jsvm-types-h/document.md#jsvm_handlerforgc) handler | Handler to be invoked when GC is triggered. |
| [JSVM\_GCType](../jsvm-types-h/document.md#jsvm_gctype) gcType | GC type. |
| void\* userData | Pointer to the native user data. |

**Returns**

| Type | Description |
| :-- | :-- |
| JSVM\_EXTERN [JSVM\_Status](../jsvm-types-h/document.md#jsvm_status) | 
Returns a JSVM status code.

[JSVM\_OK](../jsvm-types-h/document.md#jsvm_status): operation successful.

[JSVM\_INVALID\_ARG](../jsvm-types-h/document.md#jsvm_status): invalid argument. This code is returned if **vm** or **handler** is empty or the handler has been added.

 |

#### \[h2\]OH\_JSVM\_RemoveHandlerForGC()

JSVM\_EXTERN JSVM\_Status OH\_JSVM\_RemoveHandlerForGC(JSVM\_VM vm,JSVM\_CBTriggerTimeForGC triggerTime,JSVM\_HandlerForGC handler,void\* userData)

**Description**

Removes the handler for GC from the VM.

**Since**: 18

**Parameters**

| Name | Description |
| :-- | :-- |
| [JSVM\_VM](../../structs/jsvm-vm/document.md) vm | Environment for calling the JSVM-API. |
| [JSVM\_CBTriggerTimeForGC](../jsvm-types-h/document.md#jsvm_cbtriggertimeforgc) triggerTime | Time when the GC callback is triggered. |
| [JSVM\_HandlerForGC](../jsvm-types-h/document.md#jsvm_handlerforgc) handler | Handler to be invoked when GC is triggered. |
| void\* userData | Pointer to the native user data. |

**Returns**

| Type | Description |
| :-- | :-- |
| JSVM\_EXTERN [JSVM\_Status](../jsvm-types-h/document.md#jsvm_status) | 
Returns a JSVM status code.

[JSVM\_OK](../jsvm-types-h/document.md#jsvm_status): operation successful.

[JSVM\_INVALID\_ARG](../jsvm-types-h/document.md#jsvm_status): invalid argument. This code is returned if **vm** or **handler** is empty, the handler has been removed,

or the handler has never been added.

 |

#### \[h2\]OH\_JSVM\_SetHandlerForOOMError()

JSVM\_EXTERN JSVM\_Status OH\_JSVM\_SetHandlerForOOMError(JSVM\_VM vm,JSVM\_HandlerForOOMError handler)

**Description**

Sets a handler for OOM errors. If the API is called repeatedly, only the last call takes effect. If the input handler is null, the previous setting is canceled.

**Since**: 18

**Parameters**

| Name | Description |
| :-- | :-- |
| [JSVM\_VM](../../structs/jsvm-vm/document.md) vm | Environment for calling the JSVM-API. |
| [JSVM\_HandlerForOOMError](../jsvm-types-h/document.md#jsvm_handlerforoomerror) handler | Handler for OOM errors. |

**Returns**

| Type | Description |
| :-- | :-- |
| JSVM\_EXTERN [JSVM\_Status](../jsvm-types-h/document.md#jsvm_status) | 
Returns a JSVM status code.

[JSVM\_OK](../jsvm-types-h/document.md#jsvm_status): operation successful.

[JSVM\_INVALID\_ARG](../jsvm-types-h/document.md#jsvm_status): invalid argument. This code is returned if **vm** is empty.

 |

#### \[h2\]OH\_JSVM\_SetDebugOption()

JSVM\_EXTERN JSVM\_Status OH\_JSVM\_SetDebugOption(JSVM\_Env env, JSVM\_DebugOption debugOption, bool isEnabled)

**Description**

Enables or disables a specific debugging option for a JSVM environment.

**Since**: 20

**Parameters**

| Name | Description |
| :-- | :-- |
| [JSVM\_Env](../../structs/jsvm-env/document.md) env | Environment for calling the JSVM-API. |
| [JSVM\_DebugOption](../jsvm-types-h/document.md#jsvm_debugoption) debugOption | Debugging option. |
| bool isEnabled | Whether to enable or disable the debugging option. The value **true** indicates yes, and **false** indicates the opposite. |

**Returns**

| Type | Description |
| :-- | :-- |
| JSVM\_EXTERN [JSVM\_Status](../jsvm-types-h/document.md#jsvm_status) | 
Returns a JSVM status code.

[JSVM\_OK](../jsvm-types-h/document.md#jsvm_status): operation successful.

[JSVM\_INVALID\_ARG](../jsvm-types-h/document.md#jsvm_status): invalid argument. This code is returned if the input **env** is a null pointer.

 |

#### \[h2\]OH\_JSVM\_SetHandlerForFatalError()

JSVM\_EXTERN JSVM\_Status OH\_JSVM\_SetHandlerForFatalError(JSVM\_VM vm,JSVM\_HandlerForFatalError handler)

**Description**

Sets a handler for fatal errors. If the API is called repeatedly, only the last call takes effect. If the input handler is null, the previous setting is canceled.

**Since**: 18

**Parameters**

| Name | Description |
| :-- | :-- |
| [JSVM\_VM](../../structs/jsvm-vm/document.md) vm | Environment for calling the JSVM-API. |
| [JSVM\_HandlerForFatalError](../jsvm-types-h/document.md#jsvm_handlerforfatalerror) handler | Handler for fatal errors. |

**Returns**

| Type | Description |
| :-- | :-- |
| JSVM\_EXTERN [JSVM\_Status](../jsvm-types-h/document.md#jsvm_status) | 
Returns a JSVM status code.

[JSVM\_OK](../jsvm-types-h/document.md#jsvm_status): operation successful.

[JSVM\_INVALID\_ARG](../jsvm-types-h/document.md#jsvm_status): invalid argument. This code is returned if **vm** is empty.

 |

#### \[h2\]OH\_JSVM\_SetHandlerForPromiseReject()

JSVM\_EXTERN JSVM\_Status OH\_JSVM\_SetHandlerForPromiseReject(JSVM\_VM vm,JSVM\_HandlerForPromiseReject handler)

**Description**

Sets a handler for the PromiseReject error. If the API is called repeatedly, only the last call takes effect. If the input handler is null, the previous setting is canceled.

**Since**: 18

**Parameters**

| Name | Description |
| :-- | :-- |
| [JSVM\_VM](../../structs/jsvm-vm/document.md) vm | Environment for calling the JSVM-API. |
| [JSVM\_HandlerForPromiseReject](../jsvm-types-h/document.md#jsvm_handlerforpromisereject) handler | Handler for PromiseReject errors. |

**Returns**

| Type | Description |
| :-- | :-- |
| JSVM\_EXTERN [JSVM\_Status](../jsvm-types-h/document.md#jsvm_status) | 
Returns a JSVM status code.

[JSVM\_OK](../jsvm-types-h/document.md#jsvm_status): operation successful.

[JSVM\_INVALID\_ARG](../jsvm-types-h/document.md#jsvm_status): invalid argument. This code is returned if **vm** is empty.

 |

#### \[h2\]OH\_JSVM\_DefineClassWithOptions()

JSVM\_EXTERN JSVM\_Status OH\_JSVM\_DefineClassWithOptions(JSVM\_Env env,const char\* utf8name,size\_t length,JSVM\_Callback constructor,size\_t propertyCount,const JSVM\_PropertyDescriptor\* properties,JSVM\_Value parentClass,size\_t option\_count,JSVM\_DefineClassOptions options\[\],JSVM\_Value\* result)

**Description**

Defines a class with options. When a C++ class is encapsulated, the C++ constructor callback passed through the constructor should be a static method in the class. This method calls the actual class constructor, encapsulates a new C++ instance into a JavaScript object based on the input options, and returns the encapsulated object.

**Since**: 18

**Parameters**

| Name | Description |
| :-- | :-- |
| [JSVM\_Env](../../structs/jsvm-env/document.md) env | Environment for calling the JSVM-API. |
| const char\* utf8name | Pointer to the name of the JavaScript constructor. You are advised to use the C++ class name when wrapping a C++ class. |
| size\_t length | Length of **utf8name** (in bytes) or **JSVM\_AUTO\_LENGTH** (if null-terminated). |
| [JSVM\_Callback](../../structs/jsvm-callbackstruct/document.md) constructor | Callback of the constructor used to create class. When a C++ class is wrapped, this method must comply with **JSVM\_Callback**. It is a static member of the callback signature. C++ class constructors cannot be used. For details, see [JSVM\_Callback](../../structs/jsvm-callbackstruct/document.md). |
| size\_t propertyCount | Number of properties in the array. |
| [const JSVM\_PropertyDescriptor](../../structs/jsvm-propertydescriptor/document.md)\* properties | Pointer to the property descriptors, which are used to define the properties and methods of a class. |
| [JSVM\_Value](../../structs/jsvm-value/document.md) parentClass | Parent class of the defined class. |
| size\_t option\_count | Number of options in the array. |
| [JSVM\_DefineClassOptions](../../structs/jsvm-defineclassoptions/document.md) options\[\] | Array of options used to define the class. |
| [JSVM\_Value](../../structs/jsvm-value/document.md)\* result | Pointer to the **JSVM\_Value** of the constructor of a class. |

**Returns**

| Type | Description |
| :-- | :-- |
| JSVM\_EXTERN [JSVM\_Status](../jsvm-types-h/document.md#jsvm_status) | 
Returns a JSVM status code.

[JSVM\_OK](../jsvm-types-h/document.md#jsvm_status): operation successful.

[JSVM\_INVALID\_ARG](../jsvm-types-h/document.md#jsvm_status): invalid argument. This code is returned if the input pointer contains a null pointer.

[JSVM\_GENERIC\_FAILURE](../jsvm-types-h/document.md#jsvm_status): generic failure. This code is returned if the execution fails due to invalid **utf8name**,

 |

#### \[h2\]OH\_JSVM\_CreateExternalStringLatin1()

JSVM\_EXTERN JSVM\_Status OH\_JSVM\_CreateExternalStringLatin1(JSVM\_Env env, char\* str, size\_t length, JSVM\_Finalize finalizeCallback, void\* finalizeHint, JSVM\_Value\* result, bool\* copied)

**Description**

Creates an external JavaScript string with an ISO-8859-1-encoded C string. If the creation fails, the original native string is copied.

**Since**: 18

**Parameters**

| Name | Description |
| :-- | :-- |
| [JSVM\_Env](../../structs/jsvm-env/document.md) env | Environment for calling the JSVM-API. |
| char\* str | Pointer to the ISO-8859-1-encoded string. |
| size\_t length | Length of the string. If the string is a null-terminated string, you can directly pass it in **JSVM\_AUTO\_LENGTH**. |
| [JSVM\_Finalize](../jsvm-types-h/document.md#jsvm_finalize) finalizeCallback | (Optional) Callback to be invoked when the created string is reclaimed by the GC. For details, see the description of **JSVM\_Finalize**. |
| void\* finalizeHint | (Optional) Pointer to the finalize hint. This will be passed to the triggered **finalize** callback when a string is reclaimed. |
| [JSVM\_Value](../../structs/jsvm-value/document.md)\* result | Pointer to the created JavaScript external string, which is of the **JSVM\_Value** type. |
| bool\* copied | Pointer to the operation result. The value **true** indicates that the external string creation fails and a native JavaScript string is returned, and **false** indicates that the external string creation succeeds. |

**Returns**

| Type | Description |
| :-- | :-- |
| JSVM\_EXTERN [JSVM\_Status](../jsvm-types-h/document.md#jsvm_status) | 
Returns a JSVM status code.

[JSVM\_OK](../jsvm-types-h/document.md#jsvm_status): operation successful.

[JSVM\_INVALID\_ARG](../jsvm-types-h/document.md#jsvm_status): invalid argument. This code is returned if any value of **env**, **str**, or **copied** is empty.

 |

#### \[h2\]OH\_JSVM\_CreateExternalStringUtf16()

JSVM\_EXTERN JSVM\_Status OH\_JSVM\_CreateExternalStringUtf16(JSVM\_Env env, char16\_t\* str, size\_t length, JSVM\_Finalize finalizeCallback, void\* finalizeHint, JSVM\_Value\* result, bool\* copied)

**Description**

Creates an external JavaScript string with a UTF-16LE-encoded C string. If the creation fails, the original native string is copied.

**Since**: 18

**Parameters**

| Name | Description |
| :-- | :-- |
| [JSVM\_Env](../../structs/jsvm-env/document.md) env | Environment for calling the JSVM-API. |
| char16\_t\* str | Pointer to the UTF-16LE-encoded string. |
| size\_t length | Length of the string. If the string is a null-terminated string, you can directly pass it in **JSVM\_AUTO\_LENGTH**. |
| [JSVM\_Finalize](../jsvm-types-h/document.md#jsvm_finalize) finalizeCallback | (Optional) Callback to be invoked when the created string is reclaimed by the GC. For details, see the description of **JSVM\_Finalize**. |
| void\* finalizeHint | (Optional) Pointer to the finalize hint. This will be passed to the triggered **finalize** callback when a string is reclaimed. |
| [JSVM\_Value](../../structs/jsvm-value/document.md)\* result | Pointer to the created JavaScript external string, which is of the **JSVM\_Value** type. |
| bool\* copied | Pointer to the operation result. The value **true** indicates that the external string creation fails and a native JavaScript string is returned, and **false** indicates that the external string creation succeeds. |

**Returns**

| Type | Description |
| :-- | :-- |
| JSVM\_EXTERN [JSVM\_Status](../jsvm-types-h/document.md#jsvm_status) | 
Returns a JSVM status code.

[JSVM\_OK](../jsvm-types-h/document.md#jsvm_status): operation successful.

[JSVM\_INVALID\_ARG](../jsvm-types-h/document.md#jsvm_status): invalid argument. This code is returned if any value of **env**, **str**, or **copied** is empty.

 |

#### \[h2\]OH\_JSVM\_CreatePrivate()

JSVM\_EXTERN JSVM\_Status OH\_JSVM\_CreatePrivate(JSVM\_Env env,JSVM\_Value description,JSVM\_Data\* result)

**Description**

Creates a JavaScript private key object.

**Since**: 18

**Parameters**

| Name | Description |
| :-- | :-- |
| [JSVM\_Env](../../structs/jsvm-env/document.md) env | Environment for calling the JSVM-API. |
| [JSVM\_Value](../../structs/jsvm-value/document.md) description | (Optional) JavaScript description of the private key. |
| [JSVM\_Data](../../structs/jsvm-data/document.md)\* result | Pointer to the created JavaScript private key object. |

**Returns**

| Type | Description |
| :-- | :-- |
| JSVM\_EXTERN [JSVM\_Status](../jsvm-types-h/document.md#jsvm_status) | 
Returns a JSVM status code.

[JSVM\_OK](../jsvm-types-h/document.md#jsvm_status): operation successful.

[JSVM\_INVALID\_ARG](../jsvm-types-h/document.md#jsvm_status): invalid argument. This code is returned if either **env** or **result** is empty.

[JSVM\_STRING\_EXPECTED](../jsvm-types-h/document.md#jsvm_status): string expected. This code is returned if the input description is not a string.

 |

#### \[h2\]OH\_JSVM\_SetPrivate()

JSVM\_EXTERN JSVM\_Status OH\_JSVM\_SetPrivate(JSVM\_Env env,JSVM\_Value object,JSVM\_Data key,JSVM\_Value value)

**Description**

Sets the **private** property for an input object.

**Since**: 18

**Parameters**

| Name | Description |
| :-- | :-- |
| [JSVM\_Env](../../structs/jsvm-env/document.md) env | Environment for calling the JSVM-API. |
| [JSVM\_Value](../../structs/jsvm-value/document.md) object | Target object. |
| [JSVM\_Data](../../structs/jsvm-data/document.md) key | Private key object of the **private** property. |
| [JSVM\_Value](../../structs/jsvm-value/document.md) value | Value of the **private** property. |

**Returns**

| Type | Description |
| :-- | :-- |
| JSVM\_EXTERN [JSVM\_Status](../jsvm-types-h/document.md#jsvm_status) | 
Returns a JSVM status code.

[JSVM\_OK](../jsvm-types-h/document.md#jsvm_status): operation successful.

[JSVM\_INVALID\_ARG](../jsvm-types-h/document.md#jsvm_status): invalid argument. This code is returned if any input parameter is empty or the key is not a private key object.

[JSVM\_OBJECT\_EXPECTED](../jsvm-types-h/document.md#jsvm_status): object expected. This code is returned if the input object is not a real JavaScript object.

[JSVM\_GENERIC\_FAILURE](../jsvm-types-h/document.md#jsvm_status): generic failure. This code is returned if the **private** property fails to be set and no exception occurs.

[JSVM\_PENDING\_EXCEPTION](../jsvm-types-h/document.md#jsvm_status): pending exception.

 |

#### \[h2\]OH\_JSVM\_GetPrivate()

JSVM\_EXTERN JSVM\_Status OH\_JSVM\_GetPrivate(JSVM\_Env env,JSVM\_Value object,JSVM\_Data key,JSVM\_Value \*result)

**Description**

Obtains the **private** property of an input object based on the private key.

**Since**: 18

**Parameters**

| Name | Description |
| :-- | :-- |
| [JSVM\_Env](../../structs/jsvm-env/document.md) env | Environment for calling the JSVM-API. |
| [JSVM\_Value](../../structs/jsvm-value/document.md) object | Target object. |
| [JSVM\_Data](../../structs/jsvm-data/document.md) key | Private key object of the **private** property. |
| [JSVM\_Value](../../structs/jsvm-value/document.md) \*result | Value of the **private** property. |

**Returns**

| Type | Description |
| :-- | :-- |
| JSVM\_EXTERN [JSVM\_Status](../jsvm-types-h/document.md#jsvm_status) | 
Returns a JSVM status code.

[JSVM\_OK](../jsvm-types-h/document.md#jsvm_status): operation successful.

[JSVM\_INVALID\_ARG](../jsvm-types-h/document.md#jsvm_status): invalid argument. This code is returned if any input parameter is empty or the key is not a private key object.

[JSVM\_OBJECT\_EXPECTED](../jsvm-types-h/document.md#jsvm_status): object expected. This code is returned if the input object is not a real JavaScript object.

[JSVM\_GENERIC\_FAILURE](../jsvm-types-h/document.md#jsvm_status): generic failure. This code is returned if the **private** property fails to be obtained and no exception occurs.

[JSVM\_PENDING\_EXCEPTION](../jsvm-types-h/document.md#jsvm_status): pending exception.

 |

#### \[h2\]OH\_JSVM\_DeletePrivate()

JSVM\_EXTERN JSVM\_Status OH\_JSVM\_DeletePrivate(JSVM\_Env env,JSVM\_Value object,JSVM\_Data key)

**Description**

Deletes the **private** property corresponding to the private key from the input object.

**Since**: 18

**Parameters**

| Name | Description |
| :-- | :-- |
| [JSVM\_Env](../../structs/jsvm-env/document.md) env | Environment for calling the JSVM-API. |
| [JSVM\_Value](../../structs/jsvm-value/document.md) object | Target object. |
| [JSVM\_Data](../../structs/jsvm-data/document.md) key | Private key object of the **private** property. |

**Returns**

| Type | Description |
| :-- | :-- |
| JSVM\_EXTERN [JSVM\_Status](../jsvm-types-h/document.md#jsvm_status) | 
Returns a JSVM status code.

[JSVM\_OK](../jsvm-types-h/document.md#jsvm_status): operation successful.

[JSVM\_INVALID\_ARG](../jsvm-types-h/document.md#jsvm_status): invalid argument. This code is returned if any input parameter is empty or the key is not a private key object.

[JSVM\_OBJECT\_EXPECTED](../jsvm-types-h/document.md#jsvm_status): object expected. This code is returned if the input object is not a real JavaScript object.

[JSVM\_GENERIC\_FAILURE](../jsvm-types-h/document.md#jsvm_status): generic failure. This code is returned if the **private** property fails to be deleted and no exception occurs.

[JSVM\_PENDING\_EXCEPTION](../jsvm-types-h/document.md#jsvm_status): pending exception.

 |

#### \[h2\]OH\_JSVM\_CreateDataReference()

JSVM\_EXTERN JSVM\_Status OH\_JSVM\_CreateDataReference(JSVM\_Env env,JSVM\_Data data,uint32\_t initialRefcount,JSVM\_Ref\* result)

**Description**

Creates a reference to a given **JSVM\_Data** object. The initial reference count is the input value of **initialRefcount**.

**Since**: 18

**Parameters**

| Name | Description |
| :-- | :-- |
| [JSVM\_Env](../../structs/jsvm-env/document.md) env | Environment for calling the JSVM-API. |
| [JSVM\_Data](../../structs/jsvm-data/document.md) data | Target **JSVM\_Data** object. |
| uint32\_t initialRefcount | Initial reference count. |
| [JSVM\_Ref](../../structs/jsvm-ref/document.md)\* result | Pointer to the created object reference. |

**Returns**

| Type | Description |
| :-- | :-- |
| JSVM\_EXTERN [JSVM\_Status](../jsvm-types-h/document.md#jsvm_status) | 
Returns a JSVM status code.

[JSVM\_OK](../jsvm-types-h/document.md#jsvm_status): operation successful.

 |

#### \[h2\]OH\_JSVM\_GetReferenceData()

JSVM\_EXTERN JSVM\_Status OH\_JSVM\_GetReferenceData(JSVM\_Env env,JSVM\_Ref ref,JSVM\_Data\* result)

**Description**

Obtains the **JSVM\_Data** (a JavaScript value associated with the JSVM reference) through the **result** parameter if the reference is still valid. Otherwise, the result is null.

**Since**: 18

**Parameters**

| Name | Description |
| :-- | :-- |
| [JSVM\_Env](../../structs/jsvm-env/document.md) env | Environment for calling the JSVM-API. |
| [JSVM\_Ref](../../structs/jsvm-ref/document.md) ref | JSVM reference for requesting the corresponding value. |
| [JSVM\_Data](../../structs/jsvm-data/document.md)\* result | Pointer to the **JSVM\_Data** referenced by **JSVM\_Ref**. |

**Returns**

| Type | Description |
| :-- | :-- |
| JSVM\_EXTERN [JSVM\_Status](../jsvm-types-h/document.md#jsvm_status) | 
Returns a JSVM status code.

[JSVM\_OK](../jsvm-types-h/document.md#jsvm_status): operation successful.

[JSVM\_INVALID\_ARG](../jsvm-types-h/document.md#jsvm_status): invalid argument.

 |
