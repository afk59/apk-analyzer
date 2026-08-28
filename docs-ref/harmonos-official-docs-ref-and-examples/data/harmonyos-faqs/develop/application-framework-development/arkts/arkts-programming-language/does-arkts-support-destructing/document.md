# Does ArkTS support destructing?

ArkTS is a statically typed language and does not support destructing. Destructing is a dynamic feature that depends on structural compatibility of objects, and the names in the destructing statement must be the same as the property names in the objects.

-   Destructing assignments are not supported. As an alternative, you can use temporary variables to achieve similar results.
-   Variable declaration through destructing is not supported either. The names in the destructing statement should match the property names in the object being destructed.
-   Function declaration does not support parameter destructing. ArkTS requires explicit pass of arguments to function parameters without destructing.

**Reference**

[TypeScript to ArkTS Cookbook](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/typescript-to-arkts-migration-guide)
