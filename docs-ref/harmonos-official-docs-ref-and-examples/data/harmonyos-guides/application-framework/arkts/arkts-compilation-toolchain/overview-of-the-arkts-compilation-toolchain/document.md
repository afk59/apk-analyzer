# Overview of the ArkTS Compilation Toolchain

The ArkTS SDK provides a comprehensive toolchain for compiling ArkTS applications. Integrated with the [Hvigor](../../../../building-an-app/overview/document.md) task orchestration tool, this toolchain compiles ArkTS/TS/JS source code into Ark bytecode files (\*.abc).

During compilation, the toolchain first performs syntax transformation, including syntax checking and UI transformation. To ensure source code security, it uses [ArkGuard](../arkguard-for-source-code-obfuscation/arkguard-principles-and-capabilities-for-source-code-obfuscation/document.md) for source code obfuscation. Before the bytecode is written to disk, the toolchain checks whether [custom bytecode modifications](../ark-bytecode/customizing-ark-bytecode-during-compilation/document.md) are required. If modifications are required, custom modification code is loaded and executed. After generating the bytecode file, the [Disassembler](../disassembler/document.md) tool is used to inspect the file content. For details about the bytecode, see [Ark Bytecode File Format](../ark-bytecode/ark-bytecode-file-format/document.md).

The ArkTS compiler toolchain currently provides the following features:

1.  Syntax check: checks whether the ArkTS/TS syntax is correct.
    
2.  UI transformation: converts UI declarative paradigm syntax to standard TS syntax.
    
3.  Source code obfuscation: uses the ArkGuard tool to obfuscate the source code. You can enable this feature based on service requirements.
    
4.  Bytecode compilation: The Ark compiler generates Ark bytecode files (\*.abc).
    
5.  Custom bytecode modification: provides an entry for you to modify bytecode before it is written to disk.
    
6.  Disassembly: uses the Disassembler tool to convert bytecode into human-readable assembly instructions.
    

The following figure shows how the ArkTS compilation toolchain builds a HAP.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ae/v3/oXDxWVjJQRafHD9f82CqfA/en-us_image_0000002537764392.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061925Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=3C6015C148A4EF0419C25FBAC145F768D80FE85E5852925B46BA36444BA213CC)
