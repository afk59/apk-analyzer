# How do I convert an HSP into a HAR?

To convert an [HSP](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/in-app-hsp) into a [HAR](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/har-package), perform the following steps:

1.  In the **module.json5** file of the HSP, change **"type": "shared"** to **"type": "har"** and delete the **deliveryWithInstall** and **pages** fields.
2.  Remove the pages from the HSP. If you want to use them as pages, change them to use named routing or the **Navigation** component.
3.  Find the **hvigorfile.ts** file in the HSP directory and change **hspTasks** to **harTasks**.
4.  Compile the module. If any other errors occur during compilation, follow the error messages to locate and fix the corresponding issues.
