# How do I use runtime annotation in ArkTS?

You can use the third-party TS library reflect-metadata to obtain functions similar to Java runtime annotations. See [reflect-metadata](https://gitcode.com/openharmony-tpc/openharmony_tpc_samples/tree/master/reflect-metadata#https://gitee.com/openharmony-tpc/docs/blob/master/OpenHarmony_har_usage.md).

The decorators provided by reflect-metadata allow you to define metadata for classes, properties, and methods. They also provide APIs for obtaining the metadata at runtime.

import "reflect-metadata";

// The ability of third-party packaging is exposed in Reflect
@Reflect.metadata("TargetClass", 'classData')
  // Tag class, key is "targetClass", data is classData
class MyClass {
  @Reflect.metadata("TargetMethod", 'methodData')
  // Tag method, key is' Target Method ', data is' methodData'
  myMethod() {
  }

  @Reflect.metadata("Static", 'staticData')
  static invoke() {
  }
}

// Retrieve tag information at runtime
console.info(Reflect.getMetadata("TargetClass", MyClass)); //classData
console.info(Reflect.getMetadata("TargetMethod", new MyClass(), "myMethod")); //methodData
console.info(Reflect.getMetadata("Static", MyClass, "invoke")); // staticData
