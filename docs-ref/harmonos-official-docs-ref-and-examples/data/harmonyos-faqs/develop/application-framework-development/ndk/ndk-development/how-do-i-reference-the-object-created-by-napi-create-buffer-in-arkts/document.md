# How do I reference the object created by **napi\_create\_buffer** in ArkTS?

**Question**

How do I use **napi\_create\_buffer** and pass the object created between ArkTS and native?

**Answer**

1.  Create a buffer instance and write data on the native side.
    
    #include "CreateBuffer.h"
    napi\_value CreateBuffer::TestBuffer(napi\_env env, napi\_callback\_info) {
        size\_t length = 100;
        char \*data = nullptr;
        napi\_value result = nullptr;
        napi\_create\_buffer(env, length, reinterpret\_cast<void \*\*>(&data), &result);
    
    
        char buf\[50\] = {0};
        for (int i = 0; i < 50; i++) {
            buf\[i\] = i + 2;
        }
        napi\_create\_buffer\_copy(env, 50, buf, reinterpret\_cast<void \*\*>(&data), &result);
        return result;
    }
    
2.  Declare the APIs in the **index.d.ts** file.
    
    export const testBuffer: () => ArrayBuffer;
    
3.  Obtains the buffer information on the ArkTS side.
    
    import testNapi from 'libentry.so';
    
    
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
                let arr = testNapi.testBuffer();
                let result = new Uint8Array(arr);
                for (let index = 0; index < result.byteLength; index++) {
                  console.info(\`res\[${index}\] = ${result\[index\]}\`)
                }
              })
          }
          .width('100%')
        }
        .height('100%')
      }
    }
