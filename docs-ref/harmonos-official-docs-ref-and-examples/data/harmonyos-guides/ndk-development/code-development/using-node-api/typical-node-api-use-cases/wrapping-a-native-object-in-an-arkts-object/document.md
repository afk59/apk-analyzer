# Wrapping a Native Object in an ArkTS Object

#### When to Use

You can use **napi\_wrap** to wrap a C++ object in an ArkTS object, and use **napi\_unwrap** to retrieve the C++ object previously wrapped in the ArkTS object for subsequent operations.

#### Example

1.  Declare the APIs, configure compile settings, and register the modules.
    
    **Declare the APIs.**
    
    // index.d.ts
    export class MyObject {
       constructor(arg: number);
       plusOne: () => number;
    
       public get value();
       public set value(newVal: number);
    }
    
    **Configure compile settings.**
    
    \# Minimum version of CMake.
    cmake\_minimum\_required(VERSION 3.5.0)
    project(napi\_wrap\_demo)
    
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
    
    **Register modules.**
    
    // napi\_init.cpp
    #include "napi/native\_api.h"
    #include "hilog/log.h"
    
    class MyObject {
     public:
      static napi\_value Init(napi\_env env, napi\_value exports);
      static void Destructor(napi\_env env, void\* nativeObject, void\* finalize\_hint);
    
     private:
      explicit MyObject(double value\_ = 0);
      ~MyObject();
    
      static napi\_value New(napi\_env env, napi\_callback\_info info);
      static napi\_value GetValue(napi\_env env, napi\_callback\_info info);
      static napi\_value SetValue(napi\_env env, napi\_callback\_info info);
      static napi\_value PlusOne(napi\_env env, napi\_callback\_info info);
    
      double value\_;
      napi\_env env\_;
      napi\_ref wrapper\_;
    };
    
    MyObject::MyObject(double value)
        : value\_(value), env\_(nullptr), wrapper\_(nullptr) {}
    
    MyObject::~MyObject()
    {
      napi\_delete\_reference(env\_, wrapper\_);
    }
    
    void MyObject::Destructor(napi\_env env,
                              void\* nativeObject,
                              \[\[maybe\_unused\]\] void\* finalize\_hint)
    {
      OH\_LOG\_INFO(LOG\_APP, "MyObject::Destructor called");
      delete reinterpret\_cast<MyObject\*>(nativeObject);
    }
    
    napi\_value MyObject::Init(napi\_env env, napi\_value exports)
    {
      napi\_property\_descriptor properties\[\] = {
          { "value", 0, 0, GetValue, SetValue, 0, napi\_default, 0 },
          { "plusOne", nullptr, PlusOne, nullptr, nullptr, nullptr, napi\_default, nullptr }
      };
    
      napi\_value cons;
      napi\_define\_class(env, "MyObject", NAPI\_AUTO\_LENGTH, New, nullptr, 2,
                               properties, &cons);
    
      napi\_set\_named\_property(env, exports, "MyObject", cons);
      return exports;
    }
    
    EXTERN\_C\_START
    static napi\_value Init(napi\_env env, napi\_value exports)
    {
        MyObject::Init(env, exports);
        return exports;
    }
    EXTERN\_C\_END
    
    static napi\_module nativeModule = {
        .nm\_version = 1,
        .nm\_flags = 0,
        .nm\_filename = nullptr,
        .nm\_register\_func = Init,
        .nm\_modname = "entry",
        .nm\_priv = nullptr,
        .reserved = { 0 },
    };
    
    extern "C" \_\_attribute\_\_((constructor)) void RegisterObjectWrapModule()
    {
        napi\_module\_register(&nativeModule);
    }
    
2.  Wrap a C++ object in an ArkTS object in a constructor.
    
    napi\_value MyObject::New(napi\_env env, napi\_callback\_info info)
    {
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
    
        MyObject\* obj = new MyObject(value);
    
        obj->env\_ = env;
        // Use napi\_wrap to wrap the C++ object obj in the ArkTS object jsThis.
        napi\_status status = napi\_wrap(env,
                                       jsThis,
                                       reinterpret\_cast<void\*>(obj),
                                       MyObject::Destructor,
                                       nullptr,  // finalize\_hint
                                       &obj->wrapper\_);
        // If napi\_wrap fails, the allocated memory must be manually released to prevent memory leaks.
        if (status != napi\_ok) {
          OH\_LOG\_INFO(LOG\_APP, "Failed to bind native object to js object"
                      ", return code: %{public}d", status);
          delete obj;
          return jsThis;
        }
        // Obtain the napi\_ref behavior from result of napi\_wrap() to create a strong reference to jsThis.
        // If you do not want to manage the lifecycle of jsThis, pass nullptr in the last parameter of napi\_wrap
        // or call napi\_reference\_unref to convert napi\_ref to a weak reference.
        uint32\_t refCount = 0;
        napi\_reference\_unref(env, obj->wrapper\_, &refCount);
    
        return jsThis;
      } else {
        // Invoked as the plain function \`MyObject(...)\`.
        size\_t argc = 1;
        napi\_value args\[1\];
        napi\_value jsThis = nullptr;
        napi\_get\_cb\_info(env, info, &argc, args, &jsThis, nullptr);
    
        napi\_value cons;
        const char\* constructorName = "MyObject";
        napi\_get\_named\_property(env, jsThis, constructorName, &cons);
        napi\_value instance;
        napi\_new\_instance(env, cons, argc, args, &instance);
    
        return instance;
      }
    }
    
3.  Retrieve the C++ object from the ArkTS object and perform subsequent operations on the C++ object.
    
    napi\_value MyObject::GetValue(napi\_env env, napi\_callback\_info info)
    {
      OH\_LOG\_INFO(LOG\_APP, "MyObject::GetValue called");
    
      napi\_value jsThis;
      napi\_get\_cb\_info(env, info, nullptr, nullptr, &jsThis, nullptr);
    
      MyObject\* obj;
      // Use napi\_unwrap to retrieve obj (the C++ object) previously wrapped in jsThis (the ArkTS object), and perform subsequent operations.
      napi\_unwrap(env, jsThis, reinterpret\_cast<void\*\*>(&obj));
      napi\_value num;
      napi\_create\_double(env, obj->value\_, &num);
    
      return num;
    }
    
    napi\_value MyObject::SetValue(napi\_env env, napi\_callback\_info info)
    {
      OH\_LOG\_INFO(LOG\_APP, "MyObject::SetValue called");
    
      size\_t argc = 1;
      napi\_value value;
      napi\_value jsThis;
    
      napi\_get\_cb\_info(env, info, &argc, &value, &jsThis, nullptr);
    
      MyObject\* obj;
      // Use napi\_unwrap to retrieve obj (the C++ object) previously wrapped in jsThis (the ArkTS object), and perform subsequent operations.
      napi\_unwrap(env, jsThis, reinterpret\_cast<void\*\*>(&obj));
      napi\_get\_value\_double(env, value, &obj->value\_);
    
      return nullptr;
    }
    
    napi\_value MyObject::PlusOne(napi\_env env, napi\_callback\_info info)
    {
      OH\_LOG\_INFO(LOG\_APP, "MyObject::PlusOne called");
    
      napi\_value jsThis;
      napi\_get\_cb\_info(env, info, nullptr, nullptr, &jsThis, nullptr);
    
      MyObject\* obj;
      // Use napi\_unwrap to retrieve obj (the C++ object) previously wrapped in jsThis (the ArkTS object), and perform subsequent operations.
      napi\_unwrap(env, jsThis, reinterpret\_cast<void\*\*>(&obj));
      obj->value\_ += 1;
      napi\_value num;
      napi\_create\_double(env, obj->value\_, &num);
    
      return num;
    }
    
4.  The following provides the sample ArkTS code.
    
    import { hilog } from '@kit.PerformanceAnalysisKit';
    import { MyObject } from 'libentry.so';
    
    let object : MyObject = new MyObject(0);
    object.value = 1023;
    hilog.info(0x0000, 'testTag', 'MyObject value after set: %{public}d', object.value);
    hilog.info(0x0000, 'testTag', 'MyObject plusOne: %{public}d', object.plusOne());
