# How do I export custom C++ classes and call their APIs in ArkTS?

You can use **napi\_define\_class** to define an ArkTS class in native code (C/C++) and add the object to **export**. Then, define the APIs of the ArkTS class in the **index.d.ts** file to implement API invocation.

Sample code:

Define the C++ class.

// MyDemo.h Define C++classes
class MyDemo { 
  public: 
    MyDemo(std::string m\_name); 
    MyDemo(); 
    ~MyDemo();   
    std::string name; 
    int add(int a, int b); 
    int sub(int a, int b); 
};

In **hello.cpp**, create the mapping between the ArkTS class and the C++ class, and add the object to **export**.

// ArkTS Object Constructor
static napi\_value JsConstructor(napi\_env env, napi\_callback\_info info) {
    // Create Napi object
    napi\_value jDemo = nullptr;
    size\_t argc = 0;
    napi\_value args\[1\] = {0};
    // Get constructor input parameters
    napi\_get\_cb\_info(env, info, &argc, args, &jDemo, nullptr);
    // Parameters passed in args \[0\] js
    char name\[50\];
    size\_t result = 0;
    napi\_get\_value\_string\_utf8(env, args\[0\], name, sizeof(name) + 1, &result);
    // Create C++objects
    MyDemo \*cDemo = new MyDemo(name);
    OH\_LOG\_INFO(LOG\_APP, "%{public}s", (cDemo->name).c\_str());
    // Set the JS object name attribute
    napi\_set\_named\_property(env, jDemo, "name", args\[0\]);
    // Binding JS objects with C++objects
    napi\_wrap(
        env, jDemo, cDemo,
        // Define callback function for recycling JS objects, used to destroy C++objects and prevent memory leaks
        \[\](napi\_env env, void \*finalize\_data, void \*finalize\_hint) {
            MyDemo \*cDemo = (MyDemo \*)finalize\_data;
            delete cDemo;
            cDemo = nullptr;
        },
        nullptr, nullptr);
    return jDemo;
}
// ArkTS object add function
static napi\_value JsAdd(napi\_env env, napi\_callback\_info info) {
    size\_t argc = 2;
    napi\_value args\[2\] = {nullptr};
    napi\_value jDemo = nullptr;
    napi\_get\_cb\_info(env, info, &argc, args, &jDemo, nullptr);
    MyDemo \*cDemo = nullptr;
    // Convert ArkTS object to c object
    napi\_unwrap(env, jDemo, (void \*\*)&cDemo);
    // Get parameters passed by ArkTS
    int value0;
    napi\_get\_value\_int32(env, args\[0\], &value0);
    int value1;
    napi\_get\_value\_int32(env, args\[1\], &value1);
    int cResult = cDemo->add(value0, value1);
    napi\_value jResult;
    napi\_create\_int32(env, cResult, &jResult);
    return jResult;
}
// ArkTS object sub function
static napi\_value JsSub(napi\_env env, napi\_callback\_info info) {
    size\_t argc = 2;
    napi\_value args\[2\] = {nullptr};
    napi\_value jDemo = nullptr;
    napi\_get\_cb\_info(env, info, &argc, args, &jDemo, nullptr);
    MyDemo \*cDemo = nullptr;
    // Convert ArkTS object to c object
    napi\_unwrap(env, jDemo, (void \*\*)&cDemo);
    // Get parameters passed by ArkTS
    int value0;
    napi\_get\_value\_int32(env, args\[0\], &value0);
    int value1;
    napi\_get\_value\_int32(env, args\[1\], &value1);
    int cResult = cDemo->sub(value0, value1);
    napi\_value jResult;
    napi\_create\_int32(env, cResult, &jResult);
    return jResult;
}
static napi\_value Add(napi\_env env, napi\_callback\_info info) {
    size\_t requireArgc = 2;
    size\_t argc = 2;
    napi\_value args\[2\] = {nullptr};
    napi\_get\_cb\_info(env, info, &argc, args, nullptr, nullptr);
    napi\_valuetype valuetype0;
    napi\_typeof(env, args\[0\], &valuetype0);
    napi\_valuetype valuetype1;
    napi\_typeof(env, args\[1\], &valuetype1);
    int value0;
    napi\_get\_value\_int32(env, args\[0\], &value0);
    int value1;
    napi\_get\_value\_int32(env, args\[1\], &value1);
    MyDemo \*demo = new MyDemo();
    // Call functions in so to perform operations
    int result = demo->add(value0, value1);
    napi\_value sum;
    napi\_create\_int32(env, result, &sum);
    delete demo;
    return sum;
}
static napi\_value Sub(napi\_env env, napi\_callback\_info info) {
    size\_t argc = 2;
    napi\_value args\[2\] = {nullptr};
    napi\_get\_cb\_info(env, info, &argc, args, nullptr, nullptr);
    napi\_valuetype valuetype0;
    napi\_typeof(env, args\[0\], &valuetype0);
    napi\_valuetype valuetype1;
    napi\_typeof(env, args\[1\], &valuetype1);
    int value0;
    napi\_get\_value\_int32(env, args\[0\], &value0);
    int value1;
    napi\_get\_value\_int32(env, args\[1\], &value1);
    MyDemo \*demo = new MyDemo();
    // Call functions in so to perform operations
    int result = demo->sub(value0, value1);
    napi\_value num;
    napi\_create\_int32(env, result, &num);
    delete demo;
    return num;
}

EXTERN\_C\_START
static napi\_value Init(napi\_env env, napi\_value exports) {
    // Define the methods that modules need to be exposed externally
    napi\_property\_descriptor desc\[\] = {{"add", nullptr, Add, nullptr, nullptr, nullptr, napi\_default, nullptr},
                                       {"sub", nullptr, Sub, nullptr, nullptr, nullptr, napi\_default, nullptr}};
    napi\_define\_properties(env, exports, sizeof(desc) / sizeof(desc\[0\]), desc);
    // Establish the mapping relationship between ArkTS class and C++side through napi\_fine\_class, and then mount the corresponding object onto export
    napi\_property\_descriptor classProp\[\] = {{"add", nullptr, JsAdd, nullptr, nullptr, nullptr, napi\_default, nullptr},
                                            {"sub", nullptr, JsSub, nullptr, nullptr, nullptr, napi\_default, nullptr}};
    napi\_value jDemo = nullptr;
    const char \*jDemoName = "MyDemo";
    // Establish an association between ArkTS constructor and C++methods, specifying 2 props
    napi\_define\_class(env, jDemoName, sizeof(jDemoName), JsConstructor, nullptr,
                      sizeof(classProp) / sizeof(classProp\[0\]), classProp, &jDemo);
    napi\_set\_named\_property(env, exports, jDemoName, jDemo);
    return exports;
}
EXTERN\_C\_END

Define the ArkTS class in the **index.d.ts** file.

declare namespace testNapi {
  const add: (a: number, b: number) => number;
  const sub: (a: number, b: number) => number;
  // Defining the ArkTS Interface
  class MyDemo {
    constructor(name:string)
    name: string
    add(a: number, b: number): number
    sub(a: number, b: number): number
  }
}
export default testNapi;

Call C++ APIs from ArkTS.

import testNapi from 'libentry.so';
// ...
  // ...
  new testNapi.MyDemo('abc');
  hilog.info(0x0000, 'testTag', 'Test NAPI 2 + 3 = %{public}d', testNapi.add(2, 3));
  hilog.info(0x0000, 'testTag', 'Test NAPI 2 - 3 = %{public}d', testNapi.sub(2, 3));
  // ...
