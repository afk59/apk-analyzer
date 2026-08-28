# Deployment Process

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bb/v3/KWVgA6YJR5SnqkvhQxh0Xw/en-us_image_0000002528648513.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062124Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=AD99A629BCF8B99AB5CA11E98A4816CE0C5618114C174E9E9EE12B30161CAB54 "Click to enlarge")

#### Offline Model Conversion

You can convert Caffe, TensorFlow, ONNX, or MindSpore models into model formats supported by CANN Kit, and quantize models or perform AIPP on the models.

-   AIPP
    
    Use AIPP to preprocess images on the hardware, including resizing, color gamut or image format conversion, and image pixel adjustment by subtracting the average value or multiplying a coefficient, so that the data formats can be converted into a format supported by the inference computing platform, without the model being retrained. You can complete adaptation simply by configuring AIPP parameters or calling AIPP APIs at the software layer. In addition, AIPP improves the inference performance as it is dedicated to hardware. For details, please refer to [Model Conversion with AIPP](../../model-conversion/offline-model-conversion/model-conversion-example/document.md#section146407211881).
    
-   Quantization
    
    Convert 32-bit floating point (FP32) models into low-bit models to save network storage space, reduce transmission delay, and improve computing efficiency. For details, please refer to [Model Conversion with Quantization](../../model-conversion/offline-model-conversion/model-conversion-example/document.md#section29012331976).
    

#### App Integration

The app integration process includes project creation, NAPI configuration, and model integration, among which model integration includes model loading, model compilation, model input pre-processing, model running, and model output post-processing.
