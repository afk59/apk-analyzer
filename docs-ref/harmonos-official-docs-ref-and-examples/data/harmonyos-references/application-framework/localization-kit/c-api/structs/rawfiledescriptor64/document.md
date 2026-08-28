# RawFileDescriptor64

#### Overview

Defines the file descriptor of a large rawfile. **RawFileDescriptor64** is an output parameter of [OH\_ResourceManager\_GetRawFileDescriptor64](../../header-files/raw-file-h/document.md#oh_resourcemanager_getrawfiledescriptor64). It contains the file descriptor of a rawfile and the start position and length of the rawfile in the HAP.

**Since**: 11

**Related module**: [rawfile](../../modules/rawfile/document.md)

**Header file**: [raw\_file.h](../../header-files/raw-file-h/document.md)

#### Summary

#### \[h2\]Member Variables

| Name | Description |
| :-- | :-- |
| int fd | File descriptor of the rawfile, in int. |
| int64\_t start | Start position of the rawfile in the HAP, in int64\_t. |
| int64\_t length | Length of the rawfile in the HAP, in int64\_t. |
