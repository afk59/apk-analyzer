# Does ArkTS support anonymous classes?

ArkTS does not support anonymous classes. Use nested classes instead.

The type of an object created using an anonymous class is unknown. This conflicts with the ArkTS rule [Recipe: Structural Typing Is Not Supported](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/typescript-to-arkts-migration-guide#recipe-structural-typing-is-not-supported) and the type of object literals. The restriction is to minimize the performance overhead at runtime. Therefore, explicitly declare the class type.

**Reference**

[Class Literals Are Not Supported](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/typescript-to-arkts-migration-guide#class-literals-are-not-supported)
