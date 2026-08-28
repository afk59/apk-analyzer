# NeuralNetworkRuntime

#### Overview

Provides APIs for accelerating the Neural Network Runtime (NNRt) model inference.

**Since**: 9

#### Files

| Name | Description |
| :-- | :-- |
| [neural\_network\_core.h](../../header-files/neural-network-core-h/document.md) | 
Defines APIs for the Neural Network Core module. The AI inference framework uses the native interfaces provided by Neural Network Core to build models and perform inference and computing on acceleration hardware.

Some API definitions have been moved from **neural\_network\_runtime.h** to this file for unified presentation. These APIs are supported since API version 11 and can be used in all later versions.

Currently, the APIs of Neural Network Core do not support multi-thread calling.

 |
| [neural\_network\_runtime.h](../../header-files/neural-network-runtime-h/document.md) | 

Defines APIs for Neural Network Runtime. The AI inference framework uses the native APIs provided by the Neural Network Runtime to construct and build models.

Currently, the APIs of Neural Network Runtime do not support multi-thread calling.

 |
| [neural\_network\_runtime\_type.h](../../header-files/neural-network-runtime-type-h/document.md) | Defines the structs and enums for NNRt. |
