# Model Integration

Implement model loading, compilation, and inference at the native layer, and use the application layer for data transfer and display.

Pre-process the input data into the desired model input before model inference, and process the model output into the desired results. In addition, the SDK provides APIs for setting model compilation and running for you to use as needed.

The following describes the procedure for the utilization of a single model in synchronous mode at the application layer and native layer. For information about APIs, please refer to [API Reference](https://developer.huawei.com/consumer/en/doc/harmonyos-references/cannkit). For functional examples, see the [sample code](https://gitcode.com/HarmonyOS_Samples/cannkit-samplecode-clientdemo-cpp). The provided sample app supports the loading of offline models for image object classification. The app's running effect is shown as follows.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a3/v3/paj2apHoQyeZ0HzUaETvCA/en-us_image_0000002528408537.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062125Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=0E7B4674F27DAB1D35704686D43500EB51F13B6DAF08FF3EADAC32DAA3E0B6A3 "Click to enlarge")

#### Presetting the Model

In order for the app to read the model file and process the inference result, you need to preset the offline model and the inference result label file in the **entry/src/main/resources/rawfile** directory of the project.

For details about how to convert and generate an offline model used in the demo, see [Caffe Model Conversion](../../../model-conversion/offline-model-conversion/model-conversion-example/document.md#section329315242618).

#### Loading the Offline Model

Load the model and read the inference result label file when creating the app.

1.  Call the **LoadModel** function at the NAPI layer to read the model buffer.
2.  (Optional) Call the [HMS\_HiAIOptions\_SetOmOptions](https://developer.huawei.com/consumer/en/doc/harmonyos-references/cannkit#hms_hiaioptions_setomoptions) API as required to enable maintenance and debugging (such as Profiling).
3.  Pass the model buffer to the **HIAIModelManager::LoadModelFromBuffer** API of the **HIAIModelManager** class. This API calls [OH\_NNCompilation\_ConstructWithOfflineModelBuffer](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-neural-network-core-h#oh_nncompilation_constructwithofflinemodelbuffer) to create a model compilation instance.
4.  Set the **deviceID** of the model.
    
    size\_t deviceID = 0;
    const size\_t \*allDevicesID = nullptr;
    uint32\_t deviceCount = 0;
    // Obtain the IDs of all connected devices.
    OH\_NN\_ReturnCode ret = OH\_NNDevice\_GetAllDevicesID(&allDevicesID, &deviceCount);
    if (ret != OH\_NN\_SUCCESS || allDevicesID == nullptr) {
        OH\_LOG\_ERROR(LOG\_APP, "OH\_NNDevice\_GetAllDevicesID failed");
        return OH\_NN\_FAILED;
    }
    // Obtain the ID of the device named HIAI\_F.
    for (uint32\_t i = 0; i < deviceCount; i++) {
        const char \*name = nullptr;
    // Obtain the name of the specified device.
        ret = OH\_NNDevice\_GetName(allDevicesID\[i\], &name);
        if (ret != OH\_NN\_SUCCESS || name == nullptr) {
            OH\_LOG\_ERROR(LOG\_APP, "OH\_NNDevice\_GetName failed");
            return OH\_NN\_FAILED;
        }
        if (std::string(name) == "HIAI\_F") {
            deviceID = allDevicesID\[i\];
            break;
        }
    }
    
    // **modelData** and **modelSize** indicate the memory address and size of the model. For details about how to create a compilation, see [CANN Kit Codelab](https://developer.huawei.com/consumer/en/codelabsPortal/carddetails/tutorials_CANNKit-Image-classification).
    OH\_NNCompilation \*compilation = OH\_NNCompilation\_ConstructWithOfflineModelBuffer(modelData, modelSize); 
    // Set the device ID of the compiler to HIAI\_F.
    ret = OH\_NNCompilation\_SetDevice(compilation, deviceID); 
    if (ret != OH\_NN\_SUCCESS) {
        OH\_LOG\_ERROR(LOG\_APP, "OH\_NNCompilation\_SetDevice failed");
        return OH\_NN\_FAILED;
    }
    
5.  Compile the model by calling [OH\_NNCompilation\_Build](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-neural-network-core-h#oh_nncompilation_build).
6.  Create a model executor by calling [OH\_NNExecutor\_Construct](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-neural-network-core-h#oh_nnexecutor_construct).
7.  Release the model compilation instance by calling [OH\_NNCompilation\_Destroy](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-neural-network-core-h#oh_nncompilation_destroy).

For details, see the **LoadModel** function in **entry/src/main/cpp/Classification.cpp** and the **HIAIModelManager::LoadModelFromBuffer** function in **entry/src/main/cpp/HIAIModelManager.cpp** in the [sample code](https://gitcode.com/HarmonyOS_Samples/cannkit-samplecode-clientdemo-cpp).

#### Preparing Input and Output Data

1.  Process the model input. For example, as the model input in the demo is 1 x 3 x 227 x 227 float data, the input image needs to be converted into this format before being passed to the NAPI layer.
2.  Create the input and output tensors of the model, and fill the input tensors with data passed by the application layer.
    
    // Create input data.
    size\_t inputCount = 0;
    std::vector<NN\_Tensor\*> inputTensors;
    OH\_NN\_ReturnCode ret = OH\_NNExecutor\_GetInputCount(executor, &inputCount); // Create an executor by referring to [CANN Kit Codelab](https://developer.huawei.com/consumer/en/codelabsPortal/carddetails/tutorials_CANNKit-Image-classification).
    if (ret != OH\_NN\_SUCCESS || inputCount != inputData.size()) { // **inputData** refers to the input data you have created.
        OH\_LOG\_ERROR(LOG\_APP, "OH\_NNExecutor\_GetInputCount failed, size mismatch");
        return OH\_NN\_FAILED;
    }
    for (size\_t i = 0; i < inputCount; ++i) {
        NN\_TensorDesc \*tensorDesc = OH\_NNExecutor\_CreateInputTensorDesc(executor, i); // Create an executor by referring to [CANN Kit Codelab](https://developer.huawei.com/consumer/en/codelabsPortal/carddetails/tutorials_CANNKit-Image-classification).
        NN\_Tensor \*tensor = OH\_NNTensor\_Create(deviceID, tensorDesc); // Refer to Step 3 in [Loading the Offline Model](#section1377917334217) or [CANN Kit Codelab](https://developer.huawei.com/consumer/en/codelabsPortal/carddetails/tutorials_CANNKit-Image-classification) to obtain the **deviceID**.
        if (tensor != nullptr) {
            inputTensors.push\_back(tensor);
        }
        OH\_NNTensorDesc\_Destroy(&tensorDesc);
    }
    if (inputTensors.size() != inputCount) {
        OH\_LOG\_ERROR(LOG\_APP, "input size mismatch");
        DestroyTensors(inputTensors); // **DestroyTensors** is the function for releasing tensor memory. For details, see [CANN Kit Codelab](https://developer.huawei.com/consumer/en/codelabsPortal/carddetails/tutorials_CANNKit-Image-classification).
        return OH\_NN\_FAILED;
    }
    
    // Initialize the input data.
    for (size\_t i = 0; i < inputTensors.size(); ++i) {
        void \*data = OH\_NNTensor\_GetDataBuffer(inputTensors\[i\]);
        size\_t dataSize = 0;
        OH\_NNTensor\_GetSize(inputTensors\[i\], &dataSize);
        if (data == nullptr || dataSize != inputData\[i\].size()) { // **inputData** refers to the model's input data. For details, see [CANN Kit Codelab](https://developer.huawei.com/consumer/en/codelabsPortal/carddetails/tutorials_CANNKit-Image-classification).
            OH\_LOG\_ERROR(LOG\_APP, "invalid data or dataSize");
            return OH\_NN\_FAILED;
        }
        memcpy(data, inputData\[i\].data(), inputData\[i\].size()); // **inputData** refers to the model's input data. For details, see [CANN Kit Codelab](https://developer.huawei.com/consumer/en/codelabsPortal/carddetails/tutorials_CANNKit-Image-classification).
    }
    
    // Create the output data the same way as how you have created the input data.
    size\_t outputCount = 0;
    std::vector<NN\_Tensor\*> outputTensors;
    ret = OH\_NNExecutor\_GetOutputCount(executor, &outputCount); // Create an executor by referring to [CANN Kit Codelab](https://developer.huawei.com/consumer/en/codelabsPortal/carddetails/tutorials_CANNKit-Image-classification).
    if (ret != OH\_NN\_SUCCESS) {
        OH\_LOG\_ERROR(LOG\_APP, "OH\_NNExecutor\_GetOutputCount failed");
        DestroyTensors(inputTensors); // **DestroyTensors** is the function for releasing tensor memory. For details, see [CANN Kit Codelab](https://developer.huawei.com/consumer/en/codelabsPortal/carddetails/tutorials_CANNKit-Image-classification).
        return OH\_NN\_FAILED;
    }
    for (size\_t i = 0; i < outputCount; i++) {
        NN\_TensorDesc \*tensorDesc = OH\_NNExecutor\_CreateOutputTensorDesc(executor, i); // Create an executor by referring to [CANN Kit Codelab](https://developer.huawei.com/consumer/en/codelabsPortal/carddetails/tutorials_CANNKit-Image-classification).
        NN\_Tensor \*tensor = OH\_NNTensor\_Create(deviceID, tensorDesc); // Refer to Step 3 in [Loading the Offline Model](#section1377917334217) or [CANN Kit Codelab](https://developer.huawei.com/consumer/en/codelabsPortal/carddetails/tutorials_CANNKit-Image-classification) to obtain the **deviceID**.
        if (tensor != nullptr) {
            outputTensors.push\_back(tensor);
        }
        OH\_NNTensorDesc\_Destroy(&tensorDesc);
    }
    if (outputTensors.size() != outputCount) {
        DestroyTensors(inputTensors); // **DestroyTensors** is the function for releasing tensor memory. For details, see [CANN Kit Codelab](https://developer.huawei.com/consumer/en/codelabsPortal/carddetails/tutorials_CANNKit-Image-classification).
        DestroyTensors(outputTensors); // **DestroyTensors** is the function for releasing tensor memory. For details, see [CANN Kit Codelab](https://developer.huawei.com/consumer/en/codelabsPortal/carddetails/tutorials_CANNKit-Image-classification).
        OH\_LOG\_ERROR(LOG\_APP, "output size mismatch");
        return OH\_NN\_FAILED;
    }
    

For details, see the **InitIOTensors** function in **entry/src/main/cpp/Classification.cpp** and the **HIAIModelManager::InitIOTensors** function in **entry/src/main/cpp/HIAIModelManager.cpp** in the [sample code](https://gitcode.com/HarmonyOS_Samples/cannkit-samplecode-clientdemo-cpp).

#### Synchronous Offline Model Inference

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/43/v3/54R6DfWlQFy-9I3yKCvWvg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062125Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=9342DCE7DBD0C5711649C3C0B9D02AD975092A2527FD52BF9F09D677EB339259)

If the model is not changed, inference can be performed for multiple times after the model is compiled and loaded for the first time.

Call [OH\_NNExecutor\_RunSync](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-neural-network-core-h#oh_nnexecutor_runsync) to perform synchronous model inference.

For details, see the **RunModel** function in **entry/src/main/cpp/Classification.cpp** and the **HIAIModelManager::RunModel** function in **entry/src/main/cpp/HIAIModelManager.cpp** in the [sample code](https://gitcode.com/HarmonyOS_Samples/cannkit-samplecode-clientdemo-cpp).

#### Post-processing of Model Output

1.  Obtain the output tensor by calling [OH\_NNTensor\_GetDataBuffer](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-neural-network-core-h#oh_nntensor_getdatabuffer). The output tensor contains the model's output data.
2.  Process the output data to get the expected result.
    
    For example, in the demo, the model outputs the probabilities of 1000 labels, and the output data is processed to get the labels with the three largest probabilities.
    
3.  [Destroy the tensors and executor instance.](../../model-inference/document.md#li172172195213)

See the **GetResult** and **UnloadModel** functions in **entry/src/main/cpp/Classification.cpp** and the **HIAIModelManager::GetResult** and **HIAIModelManager::UnloadModel** functions in **entry/src/main/cpp/HIAIModelManager.cpp** in the [sample code](https://gitcode.com/HarmonyOS_Samples/cannkit-samplecode-clientdemo-cpp) for details.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e4/v3/sRAaRPXVRnC3VWOnZcW0FA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062125Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=18CD1ED04E6D6EDE077DF8296A5405F2505ECE5C07571D794919C6BA5725CDFB)

You can set the model inference priority as needed. The [OH\_NNCompilation\_SetPriority](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-neural-network-core-h#oh_nncompilation_setpriority) API defaults to **OH\_NN\_PRIORITY\_NONE**. Call this API before model inference.
