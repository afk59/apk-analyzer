# OH\_Huks\_KeyMaterialDsa

struct OH\_Huks\_KeyMaterialDsa {...}

#### Overview

Defines the struct for a DSA key.

**Since**: 9

**Related module**: [HuksTypeApi](../../modules/hukstypeapi/document.md)

**Header file**: [native\_huks\_type.h](../../header-files/native-huks-type-h/document.md)

#### Summary

#### \[h2\]Member Variables

| Name | Description |
| :-- | :-- |
| enum [OH\_Huks\_KeyAlg](../../header-files/native-huks-type-h/document.md#oh_huks_keyalg) keyAlg | Algorithm of the key. |
| uint32\_t keySize | Length of the key. |
| uint32\_t xSize | Length of **x**. |
| uint32\_t ySize | Length of **y**. |
| uint32\_t pSize | Length of **p**. |
| uint32\_t qSize | Length of **q**. |
| uint32\_t gSize | Length of **g**. |
