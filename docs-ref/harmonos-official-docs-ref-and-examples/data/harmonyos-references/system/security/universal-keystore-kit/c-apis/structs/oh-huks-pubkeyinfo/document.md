# OH\_Huks\_PubKeyInfo

#### Overview

Defines the struct of a public key.

**Since**: 9

**Related module**: [HuksTypeApi](../../modules/hukstypeapi/document.md)

**Header file**: [native\_huks\_type.h](../../header-files/native-huks-type-h/document.md)

#### Summary

#### \[h2\]Member Variables

| Name | Description |
| :-- | :-- |
| enum [OH\_Huks\_KeyAlg](../../header-files/native-huks-type-h/document.md#oh_huks_keyalg) keyAlg | Algorithm of the public key. |
| uint32\_t keySize | Length of the public key. |
| uint32\_t nOrXSize | Length of **n** or **X**. |
| uint32\_t eOrYSize | Length of **e** or **Y**. |
| uint32\_t placeHolder | Placeholder size. |
