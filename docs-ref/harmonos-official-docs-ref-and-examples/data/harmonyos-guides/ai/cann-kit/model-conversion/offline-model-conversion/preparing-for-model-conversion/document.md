# Preparing for Model Conversion

Currently, CANN Kit supports the conversion of only the Caffe, TensorFlow, ONNX, and MindSpore models to offline models. You need to convert models in other formats to the formats supported by CANN Kit by yourself.

1.  Prepare a trained Caffe, TensorFlow, or ONNX model, for example, [Caffe SqueezeNet V1.0](https://github.com/forresti/SqueezeNet).
2.  Click [here](../../../getting-started/document.md#section152959341125) to download the tools. Decompress the package and use the offline model generator (OMG) to convert the TensorFlow or Caffe model into an IR model. For details, please refer to [Model Conversion Example](../model-conversion-example/document.md).

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bb/v3/EoBu2dlgST2wVYmGwFRPvw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062124Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=87745CE4DA1648713411029C47375140300E66BEC17B4ED612425DB3ED1A2D57)

If the TensorFlow or Caffe model is too large, you can use the size reduction [tool](../../../getting-started/document.md#section152959341125) before OMG-based conversion. For details, please refer to [Model Size Reduction](../../../model-optimization/model-size-reduction/overview/document.md).
