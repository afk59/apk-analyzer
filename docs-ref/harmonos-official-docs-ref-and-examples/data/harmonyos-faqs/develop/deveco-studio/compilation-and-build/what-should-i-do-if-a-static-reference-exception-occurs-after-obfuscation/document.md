# What should I do if a static reference exception occurs after obfuscation?

**Question**

If the **index** file is referenced during static import, will all contents in this file be loaded at a time? In addition, if a specific path is referenced during static import, once the component is obfuscated, the specific path disappears and becomes the obfuscated path. How to resolve this issue? Is there any optimization method for importing references?

**Answer**

Yes. All content in the **index** file is loaded at a time. You can use dynamic import instead of static reference. Dynamic import allows dynamically loading modules during runtime instead of statically loading modules during compilation. In this way, the correct module path can be retained after code obfuscation.

**Reference**

[Dynamic Import](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/arkts-dynamic-import)
