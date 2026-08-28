# JSVM

#### Overview

This module provides standard JavaScript (JS) engine capabilities. The standard JS engine is a JS code execution engine that strictly complies with the ECMAScript. It supports the standard libraries defined by [ECMAScript](https://tc39.es/ecma262/) and provides complete [native APIs](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/jsvm-introduction) to implement interaction between C++ and JS modules. Just-In-Time (JIT) compiler is used to accelerate code execution and provide secure and efficient JS execution capabilities for applications. The capabilities of the standard JS engine are provided through a stable set of application binary interfaces (ABIs), that is, JSVM-APIs. They can be dynamically linked to JS engine libraries of different versions to shield the differences between engine interfaces. JSVM-APIs provide capabilities such as engine lifecycle management, JS context management, JS code execution, JS/C++ interoperability, execution environment snapshot, and code cache.

Platform: ARM64.

Usage: Link **libjsvm.so** in the SDK and include the **ark\_runtime/jsvm.h** file in the C++ code.

**Since**: 11

#### Files

| Name | Description |
| :-- | :-- |
| [jsvm.h](../../header-files/jsvm-h/document.md) | Defines JSVM-APIs. These APIs are used to provide independent, standard, and complete JS engine capabilities, including managing the engine lifecycle, compiling and running JS code, implementing JS/C++ cross-language calls, and taking snapshots. |
| [jsvm\_types.h](../../header-files/jsvm-types-h/document.md) | Defines JSVM-API types. These APIs are used to provide independent, standard, and complete JS engine capabilities, including managing the engine lifecycle, compiling and running JS code, implementing JS/C++ cross-language calls, and taking snapshots. |
