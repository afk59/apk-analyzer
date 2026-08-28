# How do I call ArkTS APIs from the native side (using C/C++)?

1\. In the **index.d.ts** file, declare the ArkTS APIs to be exposed to C/C++.

export const nativeCallArkTS: (a: object) => number;

2\. Implement the **NativeCallArkTS** API in C/C++.

static napi\_value NativeCallArkTS(napi\_env env, napi\_callback\_info info) 
{     
    size\_t argc = 1; 
    // Declaring parameter array ARG
    napi\_value args\[1\] = { nullptr }; 
 
    // Retrieve the passed parameters and place them in the parameter array 'rgs'
    napi\_get\_cb\_info(env, info, &argc, args , nullptr, nullptr); 
 
    // Create int as an input parameter for ArkTS
    napi\_value argv = nullptr;     
    napi\_create\_int32(env, 2, &argv ); 
 
    // Call the incoming callback and return the result
    napi\_value result = nullptr; 
    napi\_call\_function(env, nullptr, args\[0\], 1, &argv, &result); 
    return result; 
}

3\. Use **nativeModule.nativeCallArkTS()** to pass in the call function from ArkTS.

entry/src/main/ets/pages/Index.ets

// Introduce native capabilities through import.
import nativeModule from 'libentry.so'

@Entry
@Component
struct InvokeArkTSMethod {
  @State message: string = 'Test Node-API nativeCallArkTS result: ';

  build() {
    Row() {
      Column() {
        // Call the nativeCallArkTS method, corresponding to the Native NativeCallArkTS, and call the ArkTS function in Native.
        Text(this.message)
          .fontSize(50)
          .fontWeight(FontWeight.Bold)
          .onClick(() => {
            this.message += nativeModule.nativeCallArkTS((a: number) => {
              return a \* 2;
            });
          })
      }
      .width('100%')
    }
    .height('100%')
  }
}

**Reference**

[Node-API Use Cases](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/napi-scenarios)
