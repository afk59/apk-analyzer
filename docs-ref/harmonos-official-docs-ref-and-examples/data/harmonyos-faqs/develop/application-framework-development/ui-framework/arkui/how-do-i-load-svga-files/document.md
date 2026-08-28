# How do I load SVGA files?

**Question**

I need to use SVGA files to play pictures, motions, and animations on multiple pages in an application. How do I load SVGA animations in HarmonyOS?

**Answer**

Currently, there is no HarmonyOS native API available for loading SVGA files. You can load SVGA files as follows:

-   Convert the SVGA files to formats supported by [lottie](https://gitcode.com/openharmony-tpc/lottieArkTS) and [@tencent/libpag](https://ohpm.openharmony.cn/#/en/detail/@tencent%2Flibpag).
-   Use the [Web](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ts-basic-components-web) component to access an HTML5 page, and use the related player in the HTML5 page to load SVGA files.

You are advised to use **svga2lottie** or other conversion tools to convert the format.
