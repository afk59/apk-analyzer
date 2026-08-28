# About This Kit

ArkTS is the official high-level language for HarmonyOS application development.

Built on the [TypeScript](https://www.typescriptlang.org/) (TS) ecosystem, ArkTS extends its functionality while maintaining the basic style of TS. It enhances static check and analysis during development through standardized definitions, improving code robustness and achieving better program execution stability and performance. For details about the differences compared with standard TS, see [TypeScript to ArkTS Cookbook](../../../getting-started/learning-arkts/migration-from-typescript-to-arkts/typescript-to-arkts-cookbook/document.md). ArkTS also supports efficient interoperability with TS/JavaScript (JS).

The ArkTS common and container libraries enhance the language's basic functionalities, offering capabilities such as [high-precision floating-point operations](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-arkts-decimal), [binary buffers](../arkts-common-library/buffer-and-fastbuffer/document.md), and [XML generation, parsing, and conversion](../arkts-common-library/xml-generation-parsing-and-conversion/xml-overview/document.md), as well as various container libraries. These features help you simplify your work and improve development efficiency.

To address the limited concurrency support in TS/JS, ArkTS enhances concurrency programming APIs and capabilities. It provides two concurrency APIs, [TaskPool](../arkts-concurrency/multithreaded-concurrency/taskpool/document.md) and [Worker](../arkts-concurrency/multithreaded-concurrency/worker/document.md). In addition, ArkTS introduces the concept of Sendable to support object reference passing between concurrent instances, improving communication performance of ArkTS objects in concurrent environments.

ArkCompiler supports the compilation and execution of ArkTS, TS, and JS. Currently, it is divided into two main parts: the ArkTS compilation toolchain and the ArkTS runtime. The ArkTS compilation toolchain is responsible for compiling high-level languages into Ark bytecode files (\*.abc), whereas the ArkTS runtime runs the bytecode files on the device side to execute the program logic.

In the future, ArkTS will continue to evolve based on application development and runtime requirements, gradually introducing more features such as enhanced concurrency capabilities, enhanced system types, and distributed development paradigms.
