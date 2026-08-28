# HiDebug\_ProcessSamplerConfig

typedef struct HiDebug\_ProcessSamplerConfig {...} HiDebug\_ProcessSamplerConfig

#### Overview

Defines a struct for sampling configuration.

**Since**: 22

**Related module**: [HiDebug](../../modules/hidebug/document.md)

**Header file**: [hidebug\_type.h](../../header-files/hidebug-type-h/document.md)

#### Summary

#### \[h2\]Member Variables

| Name | Description |
| :-- | :-- |
| uint32\_t\* tids | Array of thread IDs to sample. A maximum of 10 threads can be sampled at the same time. If the array length exceeds 10, the first 10 threads are sampled. |
| uint32\_t size | Length of the array to which **tids** points. |
| uint32\_t frequency | Sampling frequency, in Hz. The value ranges from 1 to 200. If the value is out of the range, the default value **100** is used. |
| uint32\_t duration | Sampling duration, in ms. The value ranges from 1000 to 10000. If the value is less than 1000, the API call is abnormal. If the value is greater than 10000, 10000 is used. |
| uint32\_t reserved | Reserved. |
