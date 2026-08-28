# In-depth Fusion

In-depth fusion powered by hardware helps reduce DDR access and improve the energy efficiency ratio (EER) during model inference. When the shape is variable before model compilation (the only scenario supported currently), call [HMS\_HiAIOptions\_SetTuningStrategy](https://developer.huawei.com/consumer/en/doc/harmonyos-references/cannkit#hms_hiaioptions_settuningstrategy) to set the model tuning strategy to **HIAI\_TUNING\_STRATEGY\_ON\_DEVICE\_TUNING**.
