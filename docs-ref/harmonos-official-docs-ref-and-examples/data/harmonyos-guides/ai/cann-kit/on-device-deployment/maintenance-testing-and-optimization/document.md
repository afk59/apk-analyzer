# Maintenance, Testing, and Optimization

#### Overview

CANN Kit provides the capabilities of collecting AI model performance statistics and obtaining performance data. Currently, the [HiAI\_OmType](https://developer.huawei.com/consumer/en/doc/harmonyos-references/cannkit#hiai_omtype) API supports rapid acquisition of profiling and dump data based on an AI model and randomly generated input files. Then you can use this data to analyze the performance of both the model and individual operators, as well as use layer-wise accuracy comparison for issue localization.

#### Capability Overview

**Profiling mode:**

-   Supports obtaining the profiling performance data of both the entire network model and individual operators, facilitating their execution time analysis.
-   Supports profiling performance data visualization.

**Dump mode:**

-   Supports obtaining the layer-wise output of the model.

#### How to Use

You can obtain the performance data by referring to [CANN Kit Codelab](https://developer.huawei.com/consumer/cn/codelabsPortal/carddetails/tutorials_CANNKit-Optimize). Currently, this feature is supported only on Huawei phones running HarmonyOS 6.0.0(20) or later. The corresponding developer suite which includes DevEco Studio and the SDK can be found in the [version description](https://developer.huawei.com/consumer/en/doc/harmonyos-releases/overview-allversion).
