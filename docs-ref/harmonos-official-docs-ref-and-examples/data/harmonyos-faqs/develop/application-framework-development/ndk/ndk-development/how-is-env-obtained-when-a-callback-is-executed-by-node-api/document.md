# How is env obtained when a callback is executed by Node-API?

libuv saves the **env** when registering a JavaScript callback. Based on the **env** in the callback, the loop of the JavaScript thread is obtained. Then, a libuv API is called to throw the JavaScript task to the loop for execution.

Calling **napi\_create\_thread\_safe\_function** triggers **napi\_threadsafe\_function\_call\_js** in the parameter to obtain the **env** and execute it in a JavaScript thread.

Sample code:

#include "napi/native\_api.h" 
#include <thread> 
#include "hilog/log.h" 

napi\_ref cbObj = nullptr; 
// Thread safety function
napi\_threadsafe\_function tsfn; 
// Native side Value Value
static int cValue; 

// Subthread running function 
static void CallJs(napi\_env env, napi\_value js\_cb, void \*context, void \*data) { 
    std::thread::id this\_id = std::this\_thread::get\_id(); 
    OH\_LOG\_INFO(LOG\_APP, "threadId3 is +%{public}d", this\_id); 
    // Get reference value 
    napi\_get\_reference\_value(env, cbObj, &js\_cb); 

    // Create an ArkTS number as an input parameter for the ArkTS function.
    napi\_value argv; 
    napi\_create\_int32(env, cValue, &argv); 

    napi\_value result = nullptr; 
    napi\_call\_function(env, nullptr, js\_cb, 1, &argv, &result); 

    napi\_get\_value\_int32(env, result, &cValue); 

    napi\_delete\_reference(env, cbObj); 
} 

// Native main thread
static napi\_value ThreadsTest(napi\_env env, napi\_callback\_info info) { 
    // The number of parameters obtained from ArkTS side
    size\_t argc = 1; 
    napi\_value js\_cb, work\_name; 

    // Get ArkTS parameters
    napi\_get\_cb\_info(env, info, &argc, &js\_cb, nullptr, nullptr); 

    // Napi\_ref cbObj pointing to napi\_value js\_cb
    napi\_create\_reference(env, js\_cb, 1, &cbObj); 

    // Create workname using UTF8 encoded C string data 
    napi\_create\_string\_utf8(env, "Work Item", NAPI\_AUTO\_LENGTH, &work\_name); 

    // Create thread safe function
    napi\_create\_threadsafe\_function(env, js\_cb, NULL, work\_name, 0, 1, NULL, NULL, NULL, CallJs, &tsfn); 

    std::thread::id this\_id = std::this\_thread::get\_id(); 
    OH\_LOG\_INFO(LOG\_APP, "threadId1 is +%{public}d", this\_id); 

    // Calling thread safe functions in other threads
    std::thread t(\[\]() { 
        // Can obtain thread ID
        std::thread::id this\_id = std::this\_thread::get\_id(); 
        OH\_LOG\_INFO(LOG\_APP, "threadId2 is +%{public}d", this\_id); 
        napi\_acquire\_threadsafe\_function(tsfn); 
        napi\_call\_threadsafe\_function(tsfn, NULL, napi\_tsfn\_blocking); 
    }); 
    t.detach(); 

    return NULL; 
}
