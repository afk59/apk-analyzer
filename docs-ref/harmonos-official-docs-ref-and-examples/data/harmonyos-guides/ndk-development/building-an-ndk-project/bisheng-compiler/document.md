# BiSheng Compiler

#### Introduction

The BiSheng Compiler is a native compiler developed based on the open-source LLVM for C/C++ languages. It can compile and link C/C++ code projects into binary files that can run on devices. Compared with mainstream open-source compilers like LLVM and GCC in the industry, the BiSheng Compiler delivers stronger optimization capabilities without requiring changes to user code. This results in compiled and linked binary files with shorter runtime and fewer instructions, helping improve the smoothness of applications running on devices.

#### Capability Scope

The BiSheng Compiler provides basic capabilities of compiling and linking C/C++ code projects into binary files that can run on devices, including:

-   Compiling capability: compiles C/C++ source files into assembly files, which refer to files written in assembly language.
-   Assembling capability: assembles assembly files into relocatable files, which are ELF-format binary files but cannot be directly executed on devices.
-   Linking capability: links one or more relocatable files together into an executable binary file.

#### Highlights

The BiSheng Compiler outperforms LLVM and GCC in terms of the following:

-   **Loop distribution optimization of the BiSheng Compiler**

The BiSheng Compiler provides optimization in scenario identification and structure transformation in loop compilation. For example, the BiSheng Compiler can identify the data dependency and the difference in the number of iterations between different code blocks in a loop, which further optimizes the loop distribution of the open-source LLVM compiler.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e7/v3/Ttj1vtV2THae0rhiAhqP2w/en-us_image_0000002562118713.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062129Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=024A172DC4DE4D77ACB2ECE9C01A1143600345288CB34C916ECD15797DDB0BE6 "Click to enlarge")

-   **Vectorization optimization of the BiSheng Compiler**

Compared with the open-source LLVM compiler, the BiSheng Compiler can not only perform vector conversion on more loops, but also select vector instructions more efficiently. As indicated by the following figure, the BiSheng Compiler outperforms the open-source LLVM compiler in binary code running efficiency by reducing the vectorization instructions from 5 to 2.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/10/v3/rA048hvkRUu9yfcaRVe7aQ/en-us_image_0000002531038792.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062129Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=CB8F5B8D2BD394C695DC03BB2A80685F475289E1D392D035A0E3F0EE226E0547)

#### Usage Guide

**Using the BiSheng Compiler in DevEco Studio**

-   If you use DevEco Studio 5.1.1 release or later, the BiSheng Compiler is used by default when you create a C/C++ project. When you open an existing C/C++ project, a dialog box is displayed. You can click **Try Now** to switch to the BiSheng Compiler to build the C/C++ code of the HarmonyOS project.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2a/v3/xFJlrdu_RAGLxwj6hiG6BQ/en-us_image_0000002531158752.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062129Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=3ECB4A7245C5CF51723FB5EB4D89E3C0C29F277F38D2F4D784EEFA9B29E0EC06 "Click to enlarge")

-   If you use DevEco Studio 5.1.1 beta or earlier, configure the project-level **build-profile.json5** file of the HarmonyOS application: When **runtimeOS** is **HarmonyOS**, set **nativeCompiler** to **BiSheng**. Then, you can use the BiSheng Compiler to build the C/C++ code of the HarmonyOS project.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/34/v3/GoiaF0__Sdya68FIqgbuTw/en-us_image_0000002561998719.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062129Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=5DDF4E74415762BCE225C4D3149C3643519FB866E15D5E04B47EC830A61D8779)

When you configure the pipeline to switch to the BiSheng Compiler, you may encounter an error indicating that the header file cannot be found. To resolve this, add the sysroot path option (replace _xxx_ with the SDK path):

\--sysroot=xxx/sdk/default/openharmony/native/sysroot

#### Compilation Optimization Features

-   **IClang**

IClang is an incremental compilation optimization technique. Building upon incremental compilation, it further enables function-level compilation reuse by leveraging previous compilation results, significantly improving compilation speed.

**1\. Usage instructions**

To enable IClang, add the **\-iclang** option during compilation. For example, in a CMake build system, add the following to **CMakeLists.txt**: **add\_compile\_options(-iclang)**.

**2\. Data maintained by IClang**

IClang automatically creates a **.iclang** subdirectory in the same directory as the target file to store its runtime data. For instance, during the compilation of **test.o**, a **test.o.iclang** directory is created.

**3\. IClang compilation modes**

Since users typically modify only a subset of source files rather than the entire project, IClang generates reusable caches only for frequently modified source files. Specifically, compilation modes supported by IClang include:

(1) Initial mode: During the first compilation with **\-iclang**, IClang maintains only lightweight metadata to avoid affecting the performance of the user's full compilation.

(2) Warm-up mode: When a file is modified and recompiled for the first time, IClang identifies it as a frequently modified target and performs necessary analysis and cache construction. This mode may slightly affect the performance of the first incremental compilation for that file. The generated products are stored in the **.iclang** directory.

(3) Incremental compilation mode: After a file has been warmed up, subsequent incremental compilations following modifications to that file are accelerated. This mode is particularly suitable for scenarios where a specific source file is modified frequently.

**4\. Cache invalidation**

IClang reverts to the initial mode under the following circumstances:

(1) The binary products generated in the previous compilation are deleted, preventing binary function reuse.

(2) Header file contents or configurations change, making it impossible to determine which functions can be safely reused.

(3) The compilation command changes. In this case, IClang aligns with the build system's behavior (which typically triggers a full rebuild).

If an internal error occurs, a **.iclangtmp** directory is created within the relevant product directory. Upon detecting this directory, IClang enters the recovery mode, fully falling back to Clang to ensure successful compilation. This behavior should be reported to the IClang developers for verification and fixing. If necessary, users can attempt to manually delete the **.iclangtmp** directory, after which IClang will switch to the initial mode.

**5\. Compilation option restrictions**

(1) IClang only works with **\-c** compilations where the command has exactly one input file and one output file—a condition met by common build systems like CMake.

(2) Currently, IClang only supports the **\-O0** optimization option, which must be used in debug-mode development environments. If other optimization options are detected, IClang falls back to Clang and issues a warning: \[IClang Warning\] Please ensure that IClang is only enabled under -O0.

(3) To ensure correct binary file reuse, IClang adds the **\-ffunction-sections** and **\-fdata-sections** compilation options, which segment the code and data sections of the binary file by symbol.

**6\. Frontend restrictions**

For correctness, IClang may choose not to optimize functions containing certain syntax elements, including array instantiation types, function pointer instantiation types, virtual functions, and UniqueExternalLinkage.

**7\. Backend restrictions**

The binary products generated by IClang adhere to the X86-64 ELF specification, with the following additional constraints: only 64-bit little-endian is supported; binary files contain only Rela relocation tables (Rel tables are not supported); the linker must be lld (gnu ld is not supported).

-   **Profile guided optimization (PGO)**

PGO is an adaptive optimization technique. It collects performance data from actual code execution to accurately identify information such as which functions are frequently executed or which branches are frequently taken, guiding the compiler to make targeted optimizations. Compared to traditional PGO, BiSheng PGO offers greater accuracy and optimization potential.

The BiSheng Compiler triggers file writes via signals: a dynamic shared object (DSO) writes sampling information to a file upon receiving a specific signal and resets the corresponding counters. The main workflow is illustrated below: ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8e/v3/y6YDtzPdQC2Xt85iApwEBA/en-us_image_0000002562118715.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062129Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=2C7981D58320B419FD2D92D8C66D3CA3CF73D699B2A7CDF1E02164358B3B5ED9 "Click to enlarge")

This approach allows precise control over the sampling scope, addressing a key limitation of traditional PGO which relies on unified entry/exit points in the service logic and cannot perform precise sampling for specific code ranges.

The BiSheng PGO workflow aligns with that of open-source LLVM, consisting of three stages: instrumentation, profiling, and optimization.

**1\. Instrumentation**

Add the compilation option: **\-fprofile-generate=/data/storage/el2/base/files**. This path is within the sandbox; corresponding files are generated in its mapped path: **/data/app/el2/100/base/Application name/files**.

You can verify successful instrumentation by checking the compiled file for the **llvm\_prf** section or specific disassembly instruction sequences:

llvm-objdump -h xx.so # Check whether the llvm\_prf section exists.
llvm-objdump -d xx.so # Check disassembly for the ldr, add, store instruction sequence.

**2\. Profiling**

Profile data collection is performed via **lldb**.

After compilation, push the APP package in debug mode using DevEco Studio.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/93/v3/j2z1J9pdT8WDjC6kX83dvw/en-us_image_0000002531038794.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062129Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=B43D989C5E6B19212F16533A85E0A98C26368B45056B010613B2A11964F172C5 "Click to enlarge")

A debug window should appear upon launch. Ensure it is in native debug mode; if not, modify **Debug type** to **Native**.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ad/v3/T8izrhXVTZOeXZc8wPBE2g/en-us_image_0000002531158754.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062129Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=F77170E6183AB429541618BD4AC088987828EFA5002CEA149A99103E9F6BCC79 "Click to enlarge")

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b8/v3/5-Gqw92cRv-ipEW6eGWpmA/en-us_image_0000002561998721.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062129Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=ABACBCE80772753B2DDFD86B5D6532E6F676D285A6D5366E6232DC4E12024AEC "Click to enlarge")

Once launched, locate the **lldb** tab for native debugging. Configure parameters within it to ensure normal service operation and prevent signals (typically sent by the application) from interfering with data collection. The setup procedure is as follows:

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/35/v3/PjL4ili6RZygIBPcAjy2BA/en-us_image_0000002562118717.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062129Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=517438B8310B3B0F54E3142ECCE617B29371A76BE19952FD6AF45E5A22BCF393 "Click to enlarge")

Since the application may pause due to signals without breakpoints, you can disable the pause mechanism for signals.

View signals by running the command:

(lldb) process handle

Disable pausing for all signals by running the command:

(lldb) process handle SIG\* -s false

(**SIG\*** is the signal name. Omit the name to disable pausing for all signals at once.)

Send the signal directly by running the command:

(lldb) process signal SIGUSR2

You can find **default\*\_profile** files in the corresponding directory (**/data/app/el2/100/base/_Application process name_/files**). Each signal sent generates a file. The data from the first signal covers the period from application launch until the moment that signal is sent. The data from the second signal covers the period between the first and second signal triggers, with subsequent signals following the same pattern. You can control the timing of sending signals to collect data for specific scenarios. The generated files cannot be deleted due to permission restrictions. Since files generated during a single application launch share the same name, each new file overwrites the previous one, ensuring that the collected data corresponds to the target scenario.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1c/v3/H9XO0AmiRp6R08uE3G_HYQ/en-us_image_0000002531038796.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062129Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=816D16B53A3A3F43FE7373EFC484646151BB2D023F565E09D5B5A16B75715A0F "Click to enlarge")

Use **hdc** to copy the file from the device to your computer. Then, use the **llvm-profdata.exe** tool located in the same directory as **clang** to merge profiles by running **llvm-profdata merge --output=lib.profdata default\_\*.profraw**. This produces **lib.profdata**.

**3\. Optimization**

Recompile the code, adding the compilation option **\-fprofile-use=lib.profdata**, where **lib.profdata** is the merged profile file.

-   **Link time optimization (LTO)**

LTO is a compiler optimization performed at link time across compilation units, aimed at improving application performance. BiSheng LTO follows the same usage as the open-source LLVM but includes enhancements in areas such as instruction prefetching, inline algorithms, thin LTO function import algorithms, and PLT-inline optimization, further boosting the execution efficiency of the generated code.

**1\. Usage instructions**

To enable LTO, add the **\-flto** option during compilation. For example, in a CMake build system, add the following to **CMakeLists.txt**: **add\_compile\_options(-flto)**.

**2\. Precautions**

**\-flto**: Enables the full LTO mode by default, which significantly increases compilation time but yields better performance.

**\-flto=thin**: Switches to the thin LTO mode to reduce the compilation time, though with less performance gain compared with full LTO. This offers a balance between the two.

If build time still increases significantly, specify the number of parallel tasks to accelerate the build via **\-flto-jobs=_xxx_**, where _**xxx**_ should be set based on the number of CPU cores.

-   **Floating-point optimization**

Floating-point optimization refers to a set of compiler options that control the semantics and behavior of floating-point operations. They govern whether the order of operations within floating-point expressions can be reassociated or combined to achieve higher performance or stronger predictability. The BiSheng Compiler disables this optimization feature by default. You can enable it for scenarios involving a substantial amount of floating-point operations.

**1\. Usage instructions**

To enable floating-point optimization, add the **\-ffp-contract=on** option during compilation. For example, in a CMake build system, add the following to **CMakeLists.txt**: **add\_compile\_options( -ffp-contract=on)**.
