# OH\_NativeBundle\_ModuleMetadata

typedef struct OH\_NativeBundle\_ModuleMetadata {...} OH\_NativeBundle\_ModuleMetadata

#### Overview

The struct describes the metadata of a module.

**Since**: 20

**Related module**: [Native\_Bundle](../../modules/native-bundle/document.md)

**Header file**: [native\_interface\_bundle.h](../../header-files/native-interface-bundle-h/document.md)

#### Summary

#### \[h2\]Member Variables

| Name | Description |
| :-- | :-- |
| char\* moduleName | Pointer to the module name. |
| [OH\_NativeBundle\_Metadata\*](../oh-nativebundle-metadata/document.md) metadataArray | Pointer to an array containing the module's metadata. |
| size\_t metadataArraySize | Number of elements in the metadata array. |
