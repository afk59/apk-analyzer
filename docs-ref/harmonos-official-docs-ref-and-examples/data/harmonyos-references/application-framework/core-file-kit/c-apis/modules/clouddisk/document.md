# CloudDisk

#### Overview

This module provides APIs and error codes for cloud disk management. When an application registers a sync path as the root node, all subdirectories within this path are included in the sync scope, and this parent directory is referred to as the "sync root path".

Under this sync root path, you can listen for file changes, obtain the file change history, and set or query the file sync state.

**Since**: 21

#### Files

| Name | Description |
| :-- | :-- |
| [cloud\_disk\_error\_code.h](../../header-files/cloud-disk-error-code-h/document.md) | Defines the error codes for the cloud disk management module. |
| [oh\_cloud\_disk\_manager.h](../../header-files/oh-cloud-disk-manager-h/document.md) | Defines the APIs for the cloud disk management module. |
