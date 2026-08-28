# OH\_NN\_Memory

#### Overview

Defines the memory structure.

**Since**: 9

**Deprecated from**: 11

**Substitute**: [NN\_Tensor](../nn-tensor/document.md)

**Related module**: [NeuralNetworkRuntime](../../modules/neuralnetworkruntime/document.md)

**Header file**: [neural\_network\_runtime\_type.h](../../header-files/neural-network-runtime-type-h/document.md)

#### Summary

#### \[h2\]Member Variables

| Name | Description |
| :-- | :-- |
| void \* const data | Pointer to the shared memory. The shared memory is usually applied for by the underlying hardware driver. |
| const size\_t length | Length of the shared memory, in bytes. |
