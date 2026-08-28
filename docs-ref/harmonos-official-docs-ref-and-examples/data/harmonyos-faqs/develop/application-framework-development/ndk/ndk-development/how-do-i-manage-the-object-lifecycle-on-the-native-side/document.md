# How do I manage the object lifecycle on the native side?

**Answer**

As Node-API calls are made, handles to objects in the VM heap may be returned as **napi\_value**s. These handles control the lifetime of the objects. In addition, the handle of an object is associated with a scope. By default, the lifecycle of a scope is associated with the lifecycle of a native method. Therefore, the object associated with the handle remains alive during the lifecycle of the native method call.

In many cases, handles must remain valid for a shorter or longer lifetime than native methods. The following describes how to manage the lifecycle of an object.

1.  Shorten the lifecycle of the **napi\_value** object so that the lifecycle of the handle is shorter than that of the native method.
    
    Sample code:
    
    Use a **for** loop to traverse large arrays. This method creates a large number of handles, consuming lots of resources.
    
    To solve this problem, use Node-API to create a new scope and associate it with the handles. Once these handles are no longer needed, close the scope. Then, all handles associated with the scope will be invalid. You can use **napi\_open\_handle\_scope** to open a scope, and use **napi\_close\_handle\_scope** to close a scope.
    
    The scope in Node-API is of a nested hierarchy. There is only one active scope at any time, and all new handles are associated with the scope when it is active. Scopes must be closed in the reverse order of opening. All scopes created in the native method must be closed before the method is returned.
    
    For more information, see [Lifecycle Management](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/napi-guidelines#lifecycle-management).
    
    When a scope is nested, sometimes handles from the internal scope need to exceed the life of the scope. In this case, you can use Node-API **escapable scope**, which allows a handle to be promoted so that it escapes from the current scope and changes the lifetime of the handle from the current scope to an external scope. You can use **napi\_open\_escapable\_handle\_scope** to open an escapable scope, and use **napi\_close\_escapable\_handle\_scope** close an escapable scope.
    
    The request for elevating a handle is sent through **napi\_escape\_handle**, which can be called only once.
    
2.  To extend the lifecycle of a **napi\_value** object, you can create and reference the **napi\_value object** outside the native method.
    
    Node-API provides methods for creating persistent object references, which are applicable to multi-thread development scenarios. The lifecycle of a common handle is managed by the scope, which is closed before the native function ends. Each reference has a count greater than or equal to 0. When the count is 0, the reference will be garbage-collected, which is usually called weak references. If the count is greater than 0, the reference will not be garbage-collected.
    
    For example, if you want to use a constructor to create instances when required, you can create a reference to the constructor.
    
    **napi\_ref**: reference to **napi\_value**, which allows you to manage the lifecycle of JS values.
    
    You can use **napi\_create\_reference(napi\_env env, napi\_value value, uint32\_t initial\_refcount, napi\_ref\* result);** to create a reference to the **napi\_value** object to extend its lifecycle. The caller needs to manage the reference lifespan.
    
    You can use **napi\_delete\_reference(napi\_env env, napi\_ref ref);** to delete a reference.
    
    Use **napi\_reference\_ref(napi\_env env, napi\_ref ref, uint32\_t \*result);** to increment the reference count of a reference and obtain a new count.
    
    Use **napi\_reference\_unref(napi\_env env, napi\_ref ref, uint32\_t \*result);** to decrement the reference count of a reference and obtain a new count.
    
    Use **napi\_get\_reference\_value(napi\_env env, napi\_ref ref, napi\_value \*result);** to obtain the **napi\_value** object associated with the reference.
    
    For details, see [Example (Callback)](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/use-napi-asynchronous-task#example-callback).
