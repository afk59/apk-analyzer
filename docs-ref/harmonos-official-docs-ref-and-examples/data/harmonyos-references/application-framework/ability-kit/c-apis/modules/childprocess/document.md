# ChildProcess

#### Overview

The module provides APIs to manage child processes. You can call the APIs to create a native child process and establish an IPC channel between the parent and child processes to implement multi-process application development.

The created child process does not support the UI or the calling of context-related APIs. A maximum of 512 child processes can be started through this module and [childProcessManager](../../../arkts-apis/stage-model/ohos-app-ability-childprocessmanager-child-process-management/document.md) (in non-SELF\_FORK mode).

**System capability**: SystemCapability.Ability.AbilityRuntime.Core

**Since**: 12

#### Files

| Name | Description |
| :-- | :-- |
| [native\_child\_process.h](../../header-files/native-child-process-h/document.md) | 
Declares the APIs used to create a native child process and establish an IPC channel between the main process and child process.

File to include: <AbilityKit/native\_child\_process.h>

Library: libchild\_process.so

 |
