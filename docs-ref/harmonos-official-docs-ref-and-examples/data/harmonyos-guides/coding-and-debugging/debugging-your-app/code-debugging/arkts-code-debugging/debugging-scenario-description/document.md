# Debugging Scenario Description

DevEco Studio supports debugging of ArkTS code in the following scenarios:

-   Debug code in [Worker/TaskPool](../../../../../application-framework/arkts/arkts-concurrency/multithreaded-concurrency/overview-of-multithreaded-concurrency/document.md) by adding breakpoints.
-   Debug lifecycle functions of [Extension Ability](../../../../../application-framework/ability-kit/stage-model-development/stage-model-application-components/extensionability-component/document.md). For details, see [Using Extension Debugging](../using-extension-debugging/document.md).
-   Debug UIAbility by running it as an independent process on supported devices. For details, see [Multi-Process Debugging](../using-multi-process-debugging/document.md).
-   Debug ArkTS code (when ArkTS methods are called by native code via the [ArkTS runtime instance](../../../../../ndk-development/code-development/using-node-api/typical-node-api-use-cases/creating-an-arkts-runtime-environment-using-node-api/document.md)) by adding breakpoints. (The device system version must be 6.0.0.35 or later.)
