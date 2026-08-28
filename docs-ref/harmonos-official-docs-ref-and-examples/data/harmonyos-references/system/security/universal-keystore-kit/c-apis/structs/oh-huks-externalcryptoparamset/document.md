# OH\_Huks\_ExternalCryptoParamSet

typedef struct OH\_Huks\_ExternalCryptoParamSet {...} OH\_Huks\_ExternalCryptoParamSet

#### Overview

Defines an external cryptographic parameter set.

**Since**: 22

**Related module**: [HuksExternalCryptoTypeApi](../../modules/huksexternalcryptotypeapi/document.md)

**Header file**: [native\_huks\_external\_crypto\_type.h](../../header-files/native-huks-external-crypto-type-h/document.md)

#### Summary

#### \[h2\]Member Variables

| Name | Description |
| :-- | :-- |
| uint32\_t paramSetSize | 
Size of the parameter set, in bytes.

**Since**: 22

 |
| uint32\_t paramsCnt | 

Number of parameters in the parameter set.

**Since**: 22

 |
| [OH\_Huks\_ExternalCryptoParam](../oh-huks-externalcryptoparam/document.md) params\[\] | 

Parameter array. The size is determined by **paramSetSize** and **paramsCnt**.

**Since**: 22

 |
