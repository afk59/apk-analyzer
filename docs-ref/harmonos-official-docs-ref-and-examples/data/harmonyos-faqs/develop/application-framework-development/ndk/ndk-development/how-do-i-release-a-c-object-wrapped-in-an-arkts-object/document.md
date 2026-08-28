# How do I release a C++ object wrapped in an ArkTS object?

**Question**

In Java, objects can be automatically reclaimed by the garbage collection mechanism. Can the C++ object wrapped in an ArkTS object be automatically reclaimed by using a method like Java's **finalize()** without an explicit call?

**Answer**

C++ objects cannot be directly reclaimed in ArkTS. After the service is complete in ArkTS, the native side needs to be informed to release the C++ object.

Specifically, when **napi\_wrap** is used to bind an ArkTS object and a C++ object, define a callback to destroy the C++ object. This callback is the fourth parameter in the API. When the ArkTS object is reclaimed, the callback will be automatically invoked to destroy the C++ object.

Sample code:

napi\_wrap(
    env, ArkTSDemo, CDemo,
    // Define a callback function for ArkTS object recycling to destroy C++objects and prevent memory leaks
    \[\](napi\_env env, void \*finalize\_data, void \*finalize\_hint) {
        MyDemo \*cDemo = (MyDemo \*)finalize\_data;
        delete cDemo;
        cDemo = nullptr;
    },
    nullptr, nullptr);
