# How do I export APIs from multiple C++ source files?

**Symptom**

The default C++ project created in DevEco Studio has only one **hello.cpp** file. How do I add an **a.cpp** file in C++ and export the APIs from **a.cpp** for ArkTS to call?

**Solution**

Include the header file **a.h** of **a.cpp**, map the APIs in **Init()**, and export the APIs from the **index.d.ts** file.

Sample code:

Implement the **Add()** function in the **NumberType.cpp** file.

#include "NumberType.h" // Import header file
// NumberType is the class name, and Add is its function 
napi\_value NumberType::Add(napi\_env env, napi\_callback\_info info) {
    // ... Business Function Implementation Code
    // ...
}

Include the header file to **hello.cpp** and map the native and ArkTS APIs in **Init()**.

#include "NumberType.h"
#include "napi/native\_api.h"

EXTERN\_C\_START
static napi\_value Init(napi\_env env, napi\_value exports)
{
    /\* Associate the externally provided interface with the written method, for example, associate add with the Add 
     \* method. 
    \*/ 
    napi\_property\_descriptor desc\[\] = {
        { "add", nullptr, NumberType::Add, nullptr, nullptr, nullptr, napi\_default, nullptr }
    };
    // napi\_define\_properties construct a return value that contains a list of methods that correspond. 
    napi\_define\_properties(env, exports, sizeof(desc) / sizeof(desc\[0\]), desc);
    return exports;
}
EXTERN\_C\_END

Export the API to ArkTS from the API declaration file **index.d.ts**.

export const add: (a: number, b: number) => number;

**Reference**

[Implementing Image rendering Using XComponent](https://developer.huawei.com/consumer/en/codelabsPortal/carddetails/tutorials_NEXT-XComponent)
