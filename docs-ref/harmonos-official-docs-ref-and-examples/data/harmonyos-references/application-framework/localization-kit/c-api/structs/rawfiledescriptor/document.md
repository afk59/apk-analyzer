# RawFileDescriptor

#### Overview

Defines the file descriptor of a rawfile. **RawFileDescriptor** is an output parameter of [OH\_ResourceManager\_GetRawFileDescriptor](../../header-files/raw-file-h/document.md#oh_resourcemanager_getrawfiledescriptor). It contains the file descriptor of a rawfile and the start position and length of the rawfile in the HAP.

**Since**: 8

**Related module**: [rawfile](../../modules/rawfile/document.md)

**Header file**: [raw\_file.h](../../header-files/raw-file-h/document.md)

#### Summary

#### \[h2\]Member Variables

| Name | Description |
| :-- | :-- |
| int fd | File descriptor of the rawfile, in int. |
| long start | Start position of the rawfile in the HAP, in long. |
| long length | Length of the rawfile in the HAP, in long. |
