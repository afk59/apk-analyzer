# How do I obtain an ArkTS class instance on the native side?

You can create a class in ArkTS and pass it to the native side. Then, use **napi\_call\_function** to call the functions in the ArkTS class.

// Declare Demo class
class Demo {
  add(a: number, b: number): number {
    return a + b;
  }

  sub(a: number, b: number): number {
    return a - b;
  }
}

export default new Demo();

ArkTS:

// Pass the parameters to the native side
import testNapi from 'libentry.so';
import demo from './interface/ClassDemo1'

@Entry
@Component
struct Index {
  @State message: string = 'Hello World';

  build() {
    Row() {
      Column() {
        Text(this.message)
          .fontSize(50)
          .fontWeight(FontWeight.Bold)
          .onClick(() => {
            let flag:Boolean = false;
            console.info(\`Test NAPI Result is ${testNapi.cal(2, 3, demo, true)}\`)
            console.info(\`Num is  ${demo.add(3,2)}\`)
          })
      }
      .width('100%')
    }
    .height('100%')
  }
}

Native:

// Get class information and call class functions
#include "CGetArkTSObject.h" 
napi\_value CGetArkTSObject::Cal(napi\_env env, napi\_callback\_info info) { 
    size\_t argc = 4; 
    napi\_value args\[4\] = {nullptr}; 
    napi\_get\_cb\_info(env, info, &argc, args, nullptr, nullptr); 
 
    double value0; 
    napi\_get\_value\_double(env, args\[0\], &value0); 
 
    double value1; 
    napi\_get\_value\_double(env, args\[1\], &value1); 
 
    // Construct class instances
    napi\_value demo; 
    napi\_create\_object(env, &demo); 
    napi\_coerce\_to\_object(env, args\[2\], &demo); 
 
    bool flag; 
    napi\_get\_value\_bool(env, args\[3\], &flag); 
 
    // Obtain the add and sub functions of the class instance
    napi\_value add, sub, num; 
    napi\_get\_named\_property(env, demo, "add", &add); 
    napi\_get\_named\_property(env, demo, "sub", &sub); 
 
    // Call the ArkTS function
    napi\_value result; 
    if (flag) { 
        napi\_call\_function(env, nullptr, add, 2, args, &result); 
    } else { 
        napi\_call\_function(env, nullptr, sub, 2, args, &result); 
    } 
 
    return result; 
}
