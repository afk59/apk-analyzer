# What are the use cases of ArkTS custom annotations?

When you use custom annotations, the annotation information is written into the generated Ark bytecode file during compilation. The ArkCompiler toolchain provides the capability of modifying the Ark bytecode during compilation.

With this capability, you can use the [AbcKit](https://gitcode.com/openharmony/arkcompiler_runtime_core/tree/master/libabckit) library provided by the community to analyze and modify Ark bytecode files. libabckit can scan the annotation information in the bytecode and modify the bytecode based on the information. For details, see [libabckit files](https://gitcode.com/openharmony/arkcompiler_runtime_core/tree/master/libabckit/doc) and [Router table](https://gitcode.com/openharmony/arkcompiler_runtime_core/tree/master/libabckit/tests/clean_scenarios/c_api/dynamic/router_table) provided by libabckit.

**Reference**

[Customizing Ark Bytecode During Compilation](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/customize-bytecode-during-compilation)
