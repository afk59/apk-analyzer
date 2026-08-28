# Does the ArkWeb component support deep copy?

**Question**

Does the **Web** component support deep copy? That is, after the **Web** component A is deeply copied to the **Web** component B, B can still use the resources in A even if A is closed or exits from the route stack.

**Answer**

Currently, this capability is not supported. You can dynamically create **Web** components to construct a **Web** component pool. The **Web** component that you want to use can be directly obtained from the pool and displayed in the node tree.

**Reference**

[Loading Pages](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/web-page-loading-with-web-components)
