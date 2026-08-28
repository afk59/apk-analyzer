# OH\_Huks\_ExternalCryptoParam

typedef struct {...} OH\_Huks\_ExternalCryptoParam

#### Overview

Defines a single parameter in a parameter set.

**Since**: 22

**Related module**: [HuksExternalCryptoTypeApi](../../modules/huksexternalcryptotypeapi/document.md)

**Header file**: [native\_huks\_external\_crypto\_type.h](../../header-files/native-huks-external-crypto-type-h/document.md)

#### Summary

#### \[h2\]Member Variables

| Name | Description |
| :-- | :-- |
| uint32\_t tag | Tag value. |
| 
union {

bool boolParam;

int32\_t int32Param;

uint32\_t uint32Param;

uint64\_t uint64Param;

[struct OH\_Huks\_Blob](../oh-huks-blob/document.md) blob;

}

 | 

Tag content.

**boolParam**: Boolean-type parameter.

**int32Param**: int32\_t-type parameter.

**uint32Param**: uint32\_t-type parameter.

**uint64Param**: uint64\_t-type parameter.

**blob**: OH\_Huks\_Blob-type parameter.

 |
