# Getting Started with ArkTS

ArkTS is the preferred programming language for HarmonyOS application development. Built on the [TypeScript](https://www.typescriptlang.org/) (TS) ecosystem, ArkTS extends its functionality while maintaining the basic style of TS. It enhances static check and analysis during development through standardized definitions, improving program execution stability and performance.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/53/v3/-eVQ7QZ9QEyERUUh2fuhmw/en-us_image_0000002537764342.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061913Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=F3E138464FA03DC9247E1C93B6C535BC38C08967FFF51B92AEF5D9B4C9E9DB66)

For further learning, see [ArkTS learning pathways](https://developer.huawei.com/consumer/en/arkts/) and [ArkTS online courses](https://developer.huawei.com/consumer/en/training/course/video/C101740620697641580).

Since API version 10, ArkTS further strengthens its static check and analysis in terms of the following aspects. For more details about the differences between standard TS and ArkTS, see [TypeScript to ArkTS Cookbook](../migration-from-typescript-to-arkts/typescript-to-arkts-cookbook/document.md).

-   Forced use of static types: Static typing is one of the most important features of ArkTS. With static typing, the types of variables in the program are definite. In addition, because all types are known at compile time, the compiler can verify the code correctness, thereby reducing the type check at run time and helping improve performance.
    
-   Forbidden object layout at runtime: To achieve maximum performance, ArkTS requires that the object layout remain unchanged during program execution.
    
-   Restricted operator semantics: For performance and code readability purposes, ArkTS restricts the semantics of some operators. For example, it confines the use of unary plus operators to numbers.
    
-   Structural typing not supported: The support for structural typing requires a lot of considerations and careful implementation in the language, compiler, and runtime. Currently, ArkTS does not support this feature. Whether to support structural typing will be reconsidered based on the actual requirements and feedback.
    

ArkTS is compatible with the TS and JavaScript (JS) ecosystem, so that you can write new code or reuse existing code in TS or JS for development. For details about how the HarmonyOS system supports TS or JS language, see [ArkCompiler Runtime Compatibility with TS/JS](../migration-from-typescript-to-arkts/arkts-migration-background/document.md#arkcompiler-runtime-compatibility-with-tsjs).

ArkTS will continue to accommodate ever-changing application development and running requirements, and gradually provides more features, such as enhanced parallelization and concurrency, improved system, and distributed development paradigm.

For details about ArkTS, see [Introduction to ArkTS](../../../application-framework/arkts/about-this-kit/document.md).
