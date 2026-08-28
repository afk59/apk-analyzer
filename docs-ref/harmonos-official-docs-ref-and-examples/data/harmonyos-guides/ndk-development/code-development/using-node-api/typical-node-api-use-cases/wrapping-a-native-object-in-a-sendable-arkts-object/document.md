# Wrapping a Native Object in a Sendable ArkTS Object

#### When to Use

You can call **napi\_wrap\_sendable** to bind an ArkTS [Sendable](../../../../../application-framework/arkts/arkts-concurrency/inter-thread-communication/inter-thread-communication-objects/sendable-object/overview-of-sendable-objects/document.md) object to a native C++ object. Then, call **napi\_unwrap\_sendable** to obtain the C++ object bound to the ArkTS object and perform operations on the C++ object.

#### Example

1.  Declare the APIs, configure compile settings, and register the module.
    
    **Declare the APIs.**
    
    // index.d.ets
    @Sendable
    export class MyObject {
    constructor(arg: number);
    plusOne(): number;
    
    public get value();
    public set value(newVal: number);
    }
    
    **Configure compile settings.**
    
    \# the minimum version of CMake.
    cmake\_minimum\_required(VERSION 3.5.0)
    project(napi\_wrap\_sendable\_demo)
    
    set(NATIVERENDER\_ROOT\_PATH ${CMAKE\_CURRENT\_SOURCE\_DIR})
    
    if(DEFINED PACKAGE\_FIND\_FILE)
        include(${PACKAGE\_FIND\_FILE})
    endif()
    
    include\_directories(${NATIVERENDER\_ROOT\_PATH}
                        ${NATIVERENDER\_ROOT\_PATH}/include)
    
    add\_definitions("-DLOG\_DOMAIN=0x0000")
    add\_definitions("-DLOG\_TAG=\\"testTag\\"")
    
    add\_library(entry SHARED napi\_init.cpp)
    target\_link\_libraries(entry PUBLIC libace\_napi.z.so libhilog\_ndk.z.so)
    
    **Register the module.**
    
    // napi\_init.cpp
    #include "napi/native\_api.h"
    #include "hilog/log.h"
    
    // A native class. Its instance is wrapped in a Sendable ArkTS object.
    class MyObject {
    public:
        static napi\_value Init(napi\_env env, napi\_value exports);
        static void Destructor(napi\_env env, void \*nativeObject, void \*finalize\_hint);
    
    private:
        explicit MyObject(double value\_ = 0);
        ~MyObject();
    
        static napi\_value New(napi\_env env, napi\_callback\_info info);
        static napi\_value GetValue(napi\_env env, napi\_callback\_info info);
        static napi\_value SetValue(napi\_env env, napi\_callback\_info info);
        static napi\_value PlusOne(napi\_env env, napi\_callback\_info info);
    
        double value\_;
        napi\_env env\_;
    };
    
    static thread\_local napi\_ref g\_ref = nullptr;
    
    MyObject::MyObject(double value) : value\_(value), env\_(nullptr) {}
    
    MyObject::~MyObject() {}
    
    void MyObject::Destructor(napi\_env env, void \*nativeObject, \[\[maybe\_unused\]\] void \*finalize\_hint) {
        OH\_LOG\_INFO(LOG\_APP, "MyObject::Destructor called");
        reinterpret\_cast<MyObject \*>(nativeObject)->~MyObject();
    }
    
    napi\_value MyObject::Init(napi\_env env, napi\_value exports) {
        napi\_value num;
        napi\_create\_double(env, 0, &num);
        napi\_property\_descriptor properties\[\] = {
            {"value", nullptr, nullptr, GetValue, SetValue, nullptr, napi\_default, nullptr},
            {"plusOne", nullptr, PlusOne, nullptr, nullptr, nullptr, napi\_default, nullptr},
        };
    
        napi\_value cons;
        // Define a Sendable class MyObject.
        napi\_define\_sendable\_class(env, "MyObject", NAPI\_AUTO\_LENGTH, New, nullptr,
                                sizeof(properties) / sizeof(properties\[0\]), properties, nullptr, &cons);
    
        napi\_create\_reference(env, cons, 1, &g\_ref);
        // Mount the MyObject class to the exports object.
        napi\_set\_named\_property(env, exports, "MyObject", cons);
        return exports;
    }
    
    EXTERN\_C\_START
    // Initialize the module.
    static napi\_value Init(napi\_env env, napi\_value exports) {
        MyObject::Init(env, exports);
        return exports;
    }
    EXTERN\_C\_END
    
    // Information about the module. Record information such as the Init() function and module name.
    static napi\_module nativeModule = {
        .nm\_version = 1,
        .nm\_flags = 0,
        .nm\_filename = nullptr,
        .nm\_register\_func = Init,
        .nm\_modname = "entry",
        .nm\_priv = nullptr,
        .reserved = {0},
    };
    
    // When the .so file is loaded, this function is automatically called to register the nativeModule module with the system.
    extern "C" \_\_attribute\_\_((constructor)) void RegisterObjectWrapModule() { napi\_module\_register(&nativeModule); }
    
2.  Wrap a C++ object in a Sendable ArkTS object in a constructor.
    
    napi\_value MyObject::New(napi\_env env, napi\_callback\_info info) {
        OH\_LOG\_INFO(LOG\_APP, "MyObject::New called");
    
        napi\_value newTarget;
        napi\_get\_new\_target(env, info, &newTarget);
        if (newTarget != nullptr) {
            // Invoked as the constructor \`new MyObject(...)\`.
            size\_t argc = 1;
            napi\_value args\[1\];
            napi\_value jsThis;
            napi\_get\_cb\_info(env, info, &argc, args, &jsThis, nullptr);
    
            double value = 0.0;
            napi\_valuetype valuetype;
            napi\_typeof(env, args\[0\], &valuetype);
            if (valuetype != napi\_undefined) {
                napi\_get\_value\_double(env, args\[0\], &value);
            }
    
            MyObject \*obj = new MyObject(value);
    
            obj->env\_ = env;
            // Use napi\_wrap\_sendable to wrap obj (the C++ object) in jsThis (the Sendable ArkTS object).
            napi\_wrap\_sendable(env, jsThis, reinterpret\_cast<void \*>(obj), MyObject::Destructor, nullptr);
    
            return jsThis;
        } else {
            // Invoked as the plain function \`MyObject(...)\`.
            size\_t argc = 1;
            napi\_value args\[1\];
            napi\_get\_cb\_info(env, info, &argc, args, nullptr, nullptr);
    
            napi\_value cons;
            napi\_get\_reference\_value(env, g\_ref, &cons);
            napi\_value instance;
            napi\_new\_instance(env, cons, argc, args, &instance);
    
            return instance;
        }
    }
    
3.  Retrieve the C++ object from the Sendable ArkTS object and perform subsequent operations on the C++ object.
    
    napi\_value MyObject::GetValue(napi\_env env, napi\_callback\_info info) {
        OH\_LOG\_INFO(LOG\_APP, "MyObject::GetValue called");
    
        napi\_value jsThis;
        napi\_get\_cb\_info(env, info, nullptr, nullptr, &jsThis, nullptr);
    
        MyObject \*obj;
        // Use napi\_unwrap\_sendable to retrieve obj (the C++ object) previously wrapped in jsThis (the Sendable ArkTS object), and perform subsequent operations.
        napi\_unwrap\_sendable(env, jsThis, reinterpret\_cast<void \*\*>(&obj));
        napi\_value num;
        napi\_create\_double(env, obj->value\_, &num);
    
        return num;
    }
    
    napi\_value MyObject::SetValue(napi\_env env, napi\_callback\_info info) {
        OH\_LOG\_INFO(LOG\_APP, "MyObject::SetValue called");
    
        size\_t argc = 1;
        napi\_value value;
        napi\_value jsThis;
    
        napi\_get\_cb\_info(env, info, &argc, &value, &jsThis, nullptr);
    
        MyObject \*obj;
        // Use napi\_unwrap\_sendable to retrieve obj (the C++ object) previously wrapped in jsThis (the Sendable ArkTS object), and perform subsequent operations.
        napi\_unwrap\_sendable(env, jsThis, reinterpret\_cast<void \*\*>(&obj));
        napi\_get\_value\_double(env, value, &obj->value\_);
    
        return nullptr;
    }
    
    napi\_value MyObject::PlusOne(napi\_env env, napi\_callback\_info info) {
        OH\_LOG\_INFO(LOG\_APP, "MyObject::PlusOne called");
    
        napi\_value jsThis;
        napi\_get\_cb\_info(env, info, nullptr, nullptr, &jsThis, nullptr);
    
        MyObject \*obj;
        // Use napi\_unwrap\_sendable to retrieve obj (the C++ object) previously wrapped in jsThis (the Sendable ArkTS object), and perform subsequent operations.
        napi\_unwrap\_sendable(env, jsThis, reinterpret\_cast<void \*\*>(&obj));
        obj->value\_ += 1;
        napi\_value num;
        napi\_create\_double(env, obj->value\_, &num);
    
        return num;
    }
    
4.  ArkTS code:
    
    import { hilog } from '@kit.PerformanceAnalysisKit';
    import { MyObject } from 'libentry.so';
    
    let object : MyObject = new MyObject(0);
    object.value = 1023;
    hilog.info(0x0000, 'testTag', 'MyObject value after set: %{public}d', object.value);
    hilog.info(0x0000, 'testTag', 'MyObject plusOne: %{public}d', object.plusOne());
