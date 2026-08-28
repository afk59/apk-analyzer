# How do I import a third-party library in ArkTS?

**Solution**

To reference a third-party library in ArkTS, you must have **xxx.so**, **index.d.ts**, and **oh-package.json5**. You can find **index.d.ts** and **oh-package.json5** in the C++ template or create them manually. In the **oh-package.json5** file in the root directory of the module to be called, declare the root directory of the third-party library. Then, use the import statement to reference the third-party library declared in **oh-package.json5**. Note that only the .so library that is adapted for the native environment can be referenced in this way. When building the .so library, you need to implement the service functions, register the native functions, and provide the native interface file **index.d.ts** and configuration file **oh-package.json5**.

1.  Move the .so file to the directory of the corresponding architecture in the **libs** folder. In a pure ArkTS project, move the **libc++\\\_xxx.so** file generated during third-party library compilation to this directory.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c1/v3/uqp0bIlNTG6hbqPceRlIVA/en-us_image_0000002194318516.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062545Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=EDCAF56B4B98A3801A272AFD1A05C84642D05816E59A97A9130F35072D54D14C "Click to enlarge")
    
2.  Create a directory in **src/main/cpp/types** and place **index.d.ts** and **oh-package.json5** to the directory.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/84/v3/uuf51l7iQY2HeBytYQlr-A/en-us_image_0000002229604289.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062545Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=891FE127749A08C87BCDDA0BE12FDA4C175717502D96658E2FC8CEC90300C403 "Click to enlarge")
    
3.  In the **oh-package.json5** file of the module, declare the root directory of the third-party library.
    
    "dependencies": {
      "libimportthirdpartylibraries.so": "file:./src/main/cpp/types/libimportthirdpartylibraries",
      "libapplication.so": "file:./src/main/cpp/types/libapplication"
    },
    
4.  Reference and call the dependencies declared in **oh-package.json5** in the code.
    
    import testNapi from 'libimportthirdpartylibraries.so';
    import myNapi from 'libapplication.so';
    
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
                console.info(\`MyTest NAPI 2 + 3 = ${myNapi.add(2, 3)}\`);
                console.info(\`MyTest NAPI 2 - 3 = ${testNapi.sub(2, 3)}\`);
              })
          }
          .width('100%')
        }
        .height('100%')
      }
    }
    

Check the execution result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e3/v3/JOgDURGdQ1-IydqPGLa5_g/en-us_image_0000002229758785.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062545Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=5DD1BA11197E04D763E1754241BD112ADABD93AF5856B40ED5EBF7379414C32A "Click to enlarge")

**Reference**

[Referencing a Third-Party .so Library on the ArkTS Side](https://developer.huawei.com/consumer/en/doc/best-practices/bpta-dynamic-link-library#section166546365376)
