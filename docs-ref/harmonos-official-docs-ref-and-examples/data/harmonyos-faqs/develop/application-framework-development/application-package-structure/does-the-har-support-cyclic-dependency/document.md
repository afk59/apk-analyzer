# Does the HAR support cyclic dependency?

No. Cyclic dependency is not supported. You can place common parts in a shared package, or [use dynamic imports to decouple dependencies](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/arkts-dynamic-import#decoupling-dynamic-imports-between-har-modules).
