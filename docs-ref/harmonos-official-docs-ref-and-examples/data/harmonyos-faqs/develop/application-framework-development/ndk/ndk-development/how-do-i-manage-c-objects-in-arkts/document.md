# How do I manage C++ objects in ArkTS?

**Question**

How do I manage C++ objects in ArkTS?

**Answer**

Define a class object in C++, pass the address of the object to ArkTS. In ArkTS, use the **number** property of a custom class object to store the address passed from C++. When the C++ object needs to be processed in ArkTS, an API is called to pass the address of C++ object to the C++ layer for processing.

Declare TestClass.

class TestClass { 
public: 
    int GetValue() { 
        return this->value; 
    } 
    void SetValue(int value) { 
        this->value = value; 
    } 
private: 
    int value = 999; 
};

Send the object address defined in C++ to ArkTS.

#include "napi/native\_api.h" 
#include "TestClass.h" 
#include "hilog/log.h"
#define LOG\_TAG "MY\_TAG"
 
static napi\_value DefineObject(napi\_env env, napi\_callback\_info info) { 
    OH\_LOG\_INFO(LOG\_APP, "enter DefineObject"); 
     
    napi\_value result; 
    auto a = new TestClass(); 
    int64\_t addrValue = (int64\_t)a; 
    napi\_create\_bigint\_int64(env, addrValue, &result); 
    OH\_LOG\_INFO(LOG\_APP, "end DefineObject, addrValue:%{public}ld", addrValue); 
    return result; 
}

Complete the service in C++ based on the object address obtained.

static napi\_value CallObject(napi\_env env, napi\_callback\_info info) { 
    OH\_LOG\_INFO(LOG\_APP, "enter CallObject"); 
    size\_t argc = 1; 
    napi\_value args\[1\] = {nullptr}; 
    napi\_get\_cb\_info(env, info, &argc, args, nullptr, nullptr); 
    int64\_t addrValue = 0; 
    bool flag = false; 
    napi\_get\_value\_bigint\_int64(env, args\[0\], &addrValue, &flag); 
    TestClass \*a = (TestClass \*)addrValue; 
    OH\_LOG\_INFO(LOG\_APP, "CallObject, addrValue:%{public}ld", addrValue); 
    OH\_LOG\_INFO(LOG\_APP, "CallObject, value:%{public}d", a->GetValue()); 
    a->SetValue(888); 
    return nullptr; 
}

Call APIs from ArkTS.

import testNapi from 'libentry.so';

@Entry
@Component
struct Index {
  @State message: string = 'DefineObject';
  @State message2: string = 'CallObject';
  addr: number = 0;

  build() {
    Column() {
      Button(this.message)
        .fontSize(16)
        .fontWeight(FontWeight.Bold)
        .onClick(() => {
          this.addr = testNapi.defineObject();
          console.log('testTag:' + this.addr.toString());
        })
      Button(this.message2)
        .fontSize(16)
        .fontWeight(FontWeight.Bold)
        .onClick(() => {
          if (this.addr != 0) {
            testNapi.callObject(this.addr);
            this.message2 = 'CallObject';
          } else {
            this.message2 = 'want define Object';
          }
        })
    }
    .justifyContent(FlexAlign.Center)
    .height('100%')
    .width('100%')
  }
}
