# Using MindSpore Lite for Image Classification (C/C++)

#### When to Use

You can use [MindSpore](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-mindspore) to quickly deploy AI algorithms into your application to perform AI model inference for image classification.

Image classification can be used to recognize objects in images and is widely used in areas such as medical image analysis, auto driving, e-commerce, and facial recognition.

#### Basic Concepts

-   N-API: a set of native APIs used to build ArkTS components. N-APIs can be used to encapsulate C/C++ libraries into ArkTS modules.

#### Development Process

1.  Select an image classification model.
2.  Use the MindSpore Lite inference model on the device to classify the selected images.

#### Environment Setup

Install DevEco Studio 4.1 or later, and update the SDK to API version 11 or later.

#### How to Develop

The following uses inference on an image in the album as an example to describe how to use MindSpore Lite to implement image classification.

## Selecting a Model

This sample application uses [mobilenetv2.ms](https://download.mindspore.cn/model_zoo/official/lite/mobilenetv2_openimage_lite/1.5/mobilenetv2.ms) as the image classification model. The model file is available in the **entry/src/main/resources/rawfile** project directory.

If you have other pre-trained models for image classification, convert the original model into the .ms format by referring to [Using MindSpore Lite for Model Conversion](../using-mindspore-lite-for-model-conversion/document.md).

## Writing Inference Code

In **entry/src/main/cpp/mslite\_napi.cpp**, call [MindSpore](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-mindspore) to implement on-device inference. The operation process is as follows:

1.  Include the corresponding header file.
    
    #include <iostream>
    #include <sstream>
    #include <cstdlib>
    #include <hilog/log.h>
    #include <rawfile/raw\_file\_manager.h>
    #include <mindspore/types.h>
    #include <mindspore/model.h>
    #include <mindspore/context.h>
    #include <mindspore/status.h>
    #include <mindspore/tensor.h>
    #include "napi/native\_api.h"
    
2.  Read the model file.
    
    #define LOGI(...) ((void)OH\_LOG\_Print(LOG\_APP, LOG\_INFO, LOG\_DOMAIN, "\[MSLiteNapi\]", \_\_VA\_ARGS\_\_))
    #define LOGD(...) ((void)OH\_LOG\_Print(LOG\_APP, LOG\_DEBUG, LOG\_DOMAIN, "\[MSLiteNapi\]", \_\_VA\_ARGS\_\_))
    #define LOGW(...) ((void)OH\_LOG\_Print(LOG\_APP, LOG\_WARN, LOG\_DOMAIN, "\[MSLiteNapi\]", \_\_VA\_ARGS\_\_))
    #define LOGE(...) ((void)OH\_LOG\_Print(LOG\_APP, LOG\_ERROR, LOG\_DOMAIN, "\[MSLiteNapi\]", \_\_VA\_ARGS\_\_))
    
    void \*ReadModelFile(NativeResourceManager \*nativeResourceManager, const std::string &modelName, size\_t \*modelSize)
    {
        auto rawFile = OH\_ResourceManager\_OpenRawFile(nativeResourceManager, modelName.c\_str());
        if (rawFile == nullptr) {
            LOGE("MS\_LITE\_ERR: Open model file failed");
            OH\_ResourceManager\_CloseRawFile(rawFile);
            return nullptr;
        }
        long fileSize = OH\_ResourceManager\_GetRawFileSize(rawFile);
        if (fileSize <= 0) {
            LOGE("MS\_LITE\_ERR: FileSize not correct");
        }
        void \*modelBuffer = malloc(fileSize);
        if (modelBuffer == nullptr) {
            LOGE("MS\_LITE\_ERR: malloc failed");
        }
        int ret = OH\_ResourceManager\_ReadRawFile(rawFile, modelBuffer, fileSize);
        if (ret == 0) {
            LOGE("MS\_LITE\_ERR: OH\_ResourceManager\_ReadRawFile failed");
            OH\_ResourceManager\_CloseRawFile(rawFile);
            return nullptr;
        }
        OH\_ResourceManager\_CloseRawFile(rawFile);
        \*modelSize = fileSize;
        return modelBuffer;
    }
    
3.  Create a context, set parameters such as the number of threads and device type, and load the model. The sample model does not support NNRt inference.
    
    void DestroyModelBuffer(void \*\*buffer)
    {
        if (buffer == nullptr) {
            return;
        }
        free(\*buffer);
        \*buffer = nullptr;
    }
    
    OH\_AI\_ContextHandle CreateMSLiteContext(void \*modelBuffer)
    {
        // Set executing context for model.
        auto context = OH\_AI\_ContextCreate();
        if (context == nullptr) {
            DestroyModelBuffer(&modelBuffer);
            LOGE("MS\_LITE\_ERR: Create MSLite context failed.\\n");
            return nullptr;
        }
        // The OH\_AI\_DeviceInfoCreate(OH\_AI\_DEVICETYPE\_NNRT) option is not supported.
        auto cpu\_device\_info = OH\_AI\_DeviceInfoCreate(OH\_AI\_DEVICETYPE\_CPU);
    
        OH\_AI\_DeviceInfoSetEnableFP16(cpu\_device\_info, true);
        OH\_AI\_ContextAddDeviceInfo(context, cpu\_device\_info);
        
        LOGI("MS\_LITE\_LOG: Build MSLite context success.\\n");
        return context;
    }
    
    OH\_AI\_ModelHandle CreateMSLiteModel(void \*modelBuffer, size\_t modelSize, OH\_AI\_ContextHandle context)
    {
        // Create model
        auto model = OH\_AI\_ModelCreate();
        if (model == nullptr) {
            DestroyModelBuffer(&modelBuffer);
            LOGE("MS\_LITE\_ERR: Allocate MSLite Model failed.\\n");
            return nullptr;
        }
    
        // Build model object
        auto build\_ret = OH\_AI\_ModelBuild(model, modelBuffer, modelSize, OH\_AI\_MODELTYPE\_MINDIR, context);
        DestroyModelBuffer(&modelBuffer);
        if (build\_ret != OH\_AI\_STATUS\_SUCCESS) {
            OH\_AI\_ModelDestroy(&model);
            LOGE("MS\_LITE\_ERR: Build MSLite model failed.\\n");
            return nullptr;
        }
        LOGI("MS\_LITE\_LOG: Build MSLite model success.\\n");
        return model;
    }
    
4.  Set the model input data and perform model inference.
    
    constexpr int K\_NUM\_PRINT\_OF\_OUT\_DATA = 20;
    
    // Set the model input data.
    int FillInputTensor(OH\_AI\_TensorHandle input, std::vector<float> input\_data)
    {
        if (OH\_AI\_TensorGetDataType(input) == OH\_AI\_DATATYPE\_NUMBERTYPE\_FLOAT32) {
            float \*data = (float \*)OH\_AI\_TensorGetMutableData(input);
            for (size\_t i = 0; i < OH\_AI\_TensorGetElementNum(input); i++) {
                data\[i\] = input\_data\[i\];
            }
            return OH\_AI\_STATUS\_SUCCESS;
        } else {
            return OH\_AI\_STATUS\_LITE\_ERROR;
        }
    }
    
    // Execute model inference.
    int RunMSLiteModel(OH\_AI\_ModelHandle model, std::vector<float> input\_data)
    {
        // Set input data for model.
        auto inputs = OH\_AI\_ModelGetInputs(model);
        auto ret = FillInputTensor(inputs.handle\_list\[0\], input\_data);
        if (ret != OH\_AI\_STATUS\_SUCCESS) {
            LOGE("MS\_LITE\_ERR: RunMSLiteModel set input error.\\n");
            return OH\_AI\_STATUS\_LITE\_ERROR;
        }
    
        // Get model output.
        auto outputs = OH\_AI\_ModelGetOutputs(model);
    
        // Predict model.
        auto predict\_ret = OH\_AI\_ModelPredict(model, inputs, &outputs, nullptr, nullptr);
        if (predict\_ret != OH\_AI\_STATUS\_SUCCESS) {
            LOGE("MS\_LITE\_ERR: MSLite Predict error.\\n");
            return OH\_AI\_STATUS\_LITE\_ERROR;
        }
        LOGI("MS\_LITE\_LOG: Run MSLite model Predict success.\\n");
    
        // Print output tensor data.
        LOGI("MS\_LITE\_LOG: Get model outputs:\\n");
        for (size\_t i = 0; i < outputs.handle\_num; i++) {
            auto tensor = outputs.handle\_list\[i\];
            LOGI("MS\_LITE\_LOG: - Tensor %{public}d name is: %{public}s.\\n", static\_cast<int>(i),
                 OH\_AI\_TensorGetName(tensor));
            LOGI("MS\_LITE\_LOG: - Tensor %{public}d size is: %{public}d.\\n", static\_cast<int>(i),
                 (int)OH\_AI\_TensorGetDataSize(tensor));
            LOGI("MS\_LITE\_LOG: - Tensor data is:\\n");
            auto out\_data = reinterpret\_cast<const float \*>(OH\_AI\_TensorGetData(tensor));
            std::stringstream outStr;
            for (int i = 0; (i < OH\_AI\_TensorGetElementNum(tensor)) && (i <= K\_NUM\_PRINT\_OF\_OUT\_DATA); i++) {
                outStr << out\_data\[i\] << " ";
            }
            LOGI("MS\_LITE\_LOG: %{public}s", outStr.str().c\_str());
        }
        return OH\_AI\_STATUS\_SUCCESS;
    }
    
5.  Implement a complete model inference process.
    
    static napi\_value RunDemo(napi\_env env, napi\_callback\_info info)
    {
        // run demo
        napi\_value error\_ret;
        napi\_create\_int32(env, -1, &error\_ret);
        // Process the input data.
        size\_t argc = 2;
        napi\_value argv\[2\] = {nullptr};
        napi\_get\_cb\_info(env, info, &argc, argv, nullptr, nullptr);
        bool isArray = false;
        napi\_is\_array(env, argv\[0\], &isArray);
        uint32\_t length = 0;
        // Obtain the length of the array.
        napi\_get\_array\_length(env, argv\[0\], &length);
        LOGI("MS\_LITE\_LOG: argv array length = %{public}d", length);
        std::vector<float> input\_data;
        double param = 0;
        for (int i = 0; i < length; i++) {
            napi\_value value;
            napi\_get\_element(env, argv\[0\], i, &value);
            napi\_get\_value\_double(env, value, &param);
            input\_data.push\_back(static\_cast<float>(param));
        }
        std::stringstream outstr;
        for (int i = 0; i < K\_NUM\_PRINT\_OF\_OUT\_DATA; i++) {
            outstr << input\_data\[i\] << " ";
        }
        LOGI("MS\_LITE\_LOG: input\_data = %{public}s", outstr.str().c\_str());
        // Read model file
        const std::string modelName = "mobilenetv2.ms";
        LOGI("MS\_LITE\_LOG: Run model: %{public}s", modelName.c\_str());
        size\_t modelSize;
        auto resourcesManager = OH\_ResourceManager\_InitNativeResourceManager(env, argv\[1\]);
        auto modelBuffer = ReadModelFile(resourcesManager, modelName, &modelSize);
        if (modelBuffer == nullptr) {
            LOGE("MS\_LITE\_ERR: Read model failed");
            return error\_ret;
        }
        LOGI("MS\_LITE\_LOG: Read model file success");
        
        auto context = CreateMSLiteContext(modelBuffer);
        if (context == nullptr) {
            LOGE("MS\_LITE\_ERR: MSLiteFwk Build context failed.\\n");
            return error\_ret;
        }
        auto model = CreateMSLiteModel(modelBuffer, modelSize, context);
        if (model == nullptr) {
            OH\_AI\_ContextDestroy(&context);
            LOGE("MS\_LITE\_ERR: MSLiteFwk Build model failed.\\n");
            return error\_ret;
        }
        int ret = RunMSLiteModel(model, input\_data);
        if (ret != OH\_AI\_STATUS\_SUCCESS) {
            OH\_AI\_ModelDestroy(&model);
            OH\_AI\_ContextDestroy(&context);
            LOGE("MS\_LITE\_ERR: RunMSLiteModel failed.\\n");
            return error\_ret;
        }
        napi\_value out\_data;
        napi\_create\_array(env, &out\_data);
        auto outputs = OH\_AI\_ModelGetOutputs(model);
        OH\_AI\_TensorHandle output\_0 = outputs.handle\_list\[0\];
        float \*output0Data = reinterpret\_cast<float \*>(OH\_AI\_TensorGetMutableData(output\_0));
        for (size\_t i = 0; i < OH\_AI\_TensorGetElementNum(output\_0); i++) {
            napi\_value element;
            napi\_create\_double(env, static\_cast<double>(output0Data\[i\]), &element);
            napi\_set\_element(env, out\_data, i, element);
        }
        OH\_AI\_ModelDestroy(&model);
        OH\_AI\_ContextDestroy(&context);
        LOGI("MS\_LITE\_LOG: Exit runDemo()");
        return out\_data;
    }
    
6.  Write the **CMake** script to link the MindSpore Lite dynamic library.
    
    \# the minimum version of CMake.
    cmake\_minimum\_required(VERSION 3.4.1)
    project(MindSporeLiteCDemo)
    
    set(NATIVERENDER\_PATH ${CMAKE\_CURRENT\_SOURCE\_DIR})
    
    if(DEFINED PACKAGE\_FIND\_FILE)
        include(${PACKAGE\_FIND\_FILE})
    endif()
    
    include\_directories(${NATIVERENDER\_PATH}
                        ${NATIVERENDER\_PATH}/include)
    
    add\_library(entry SHARED mslite\_napi.cpp)
    target\_link\_libraries(entry PUBLIC mindspore\_lite\_ndk)
    target\_link\_libraries(entry PUBLIC hilog\_ndk.z)
    target\_link\_libraries(entry PUBLIC rawfile.z)
    target\_link\_libraries(entry PUBLIC ace\_napi.z)
    

## Use N-APIs to encapsulate the C++ dynamic library into an ArkTS module.

1.  In **entry/src/main/cpp/types/libentry/Index.d.ts**, define the ArkTS API **runDemo ()**. The content is as follows:
    
    export const runDemo: (a: number\[\], b:Object) => Array<number>;
    
2.  In the **oh-package.json5** file, associate the API with the .so file to form a complete ArkTS module.
    
    {
      "name": "libentry.so",
      "types": "./Index.d.ts",
      "version": "1.0.0",
      "description": "MindSpore Lite inference module"
    }
    

## Implementing Image Input and Preprocessing and Performing Inference

1.  Call [@ohos.file.picker](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-file-picker) to pick up the desired image in the album.
2.  Based on the input image size, call \[[@ohos.multimedia.image](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-image) and [@ohos.file.fs](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-file-fs) to perform operations such as cropping the image, obtaining the image buffer, and standardizing the image.
3.  In **entry/src/main/ets/pages/Index.ets**, call the encapsulated ArkTS module to process the inference result.

// Index.ets
import msliteNapi from 'libentry.so';
import { photoAccessHelper } from '@kit.MediaLibraryKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { image } from '@kit.ImageKit';
import { fileIo } from '@kit.CoreFileKit';
import { abilityAccessCtrl, Permissions } from '@kit.AbilityKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

const TAG = 'MindSporeLite';
const PERMISSIONS: Permissions\[\] = \['ohos.permission.READ\_IMAGEVIDEO'\];

@Entry
@Component
struct Index {
  @State message: string = 'MindSporeLite C Demo';
  @State modelName: string = 'mobilenetv2.ms';
  @State modelInputHeight: number = 224;
  @State modelInputWidth: number = 224;
  @State uris: Array<string> = \[\];
  @State max: number = 0;
  @State maxIndex: number = 0;
  @State maxArray: Array<number> = \[\];
  @State maxIndexArray: Array<number> = \[\];

  build() {
    Row() {
      Column() {
        Text(this.message)
        Button() {
          Text('photo')
            .fontSize(30)
            .fontWeight(FontWeight.Bold)
        }
        .onClick(() => {
          let resMgr = this.getUIContext()?.getHostContext()?.getApplicationContext().resourceManager;
          if (resMgr === null || resMgr === undefined){
            hilog.error(0xFF00, TAG, '%{public}s', \`MS\_LITE\_ERR: get resMgr failed.\`);
            return
          }

          // Obtain images in an album.
          // 1. Create an image picker instance.
          let photoSelectOptions = new photoAccessHelper.PhotoSelectOptions();

          // 2. Set the media file type to IMAGE and set the maximum number of media files that can be selected.
          photoSelectOptions.MIMEType = photoAccessHelper.PhotoViewMIMETypes.IMAGE\_TYPE;
          photoSelectOptions.maxSelectNumber = 1;

          // 3. Create an album picker instance and call select() to open the album page for file selection. After file selection is done, the result set is returned through photoSelectResult.
          let photoPicker = new photoAccessHelper.PhotoViewPicker();
          photoPicker.select(photoSelectOptions,
            async (err: BusinessError, photoSelectResult: photoAccessHelper.PhotoSelectResult) => {
              if (err) {
                hilog.error(0xFF00, TAG, '%{public}s',
                  \`MS\_LITE\_ERR: PhotoViewPicker.select failed with err: ${JSON.stringify(err)}\`);
                return;
              }
              hilog.info(0xFF00, TAG, '%{public}s',
                \`MS\_LITE\_LOG: PhotoViewPicker.select successfully, uri: ${JSON.stringify(photoSelectResult)}\`);
              this.uris = photoSelectResult.photoUris;
              hilog.info(0xFF00, TAG, '%{public}s', \`MS\_LITE\_LOG: uri: ${this.uris}\`);

              // Preprocess the image data.
              try {
                // 1. Based on the specified URI, call fileIo.openSync to open the file to obtain the FD.
                let file = fileIo.openSync(this.uris\[0\], fileIo.OpenMode.READ\_ONLY);
                hilog.info(0xFF00, TAG, '%{public}s', \`MS\_LITE\_LOG: file fd: ${file.fd}\`);

                // 2. Based on the FD, call fileIo.readSync to read the data in the file.
                let inputBuffer = new ArrayBuffer(4096000);
                let readLen = fileIo.readSync(file.fd, inputBuffer);
                hilog.info(0xFF00, TAG, '%{public}s',
                  \`MS\_LITE\_LOG: readSync data to file succeed and inputBuffer size is: ${readLen}\`);

                // 3. Perform image preprocessing through PixelMap.
                let imageSource = image.createImageSource(file.fd);
                if (imageSource === undefined) {
                  hilog.error(0xFF00, TAG, '%{public}s', \`MS\_LITE\_ERR: createImageSource failed.\`);
                  return
                }
                imageSource.createPixelMap({ editable: true }).then((pixelMap) => {
                  pixelMap.getImageInfo().then((info) => {
                    hilog.info(0xFF00, TAG, '%{public}s',
                      \`MS\_LITE\_LOG: info.width = ${info.size.width}\`);
                    hilog.info(0xFF00, TAG, '%{public}s',
                      \`MS\_LITE\_LOG: info.height = ${info.size.height}\`);

                    // 4. Crop the image based on the input image size and obtain the image buffer readBuffer.
                    pixelMap.scale(256.0 / info.size.width, 256.0 / info.size.height).then(() => {
                      pixelMap.crop({
                        x: 16,
                        y: 16,
                        size: { height: this.modelInputHeight, width: this.modelInputWidth }
                      }).then(async () => {
                        let info = await pixelMap.getImageInfo();
                        hilog.info(0xFF00, TAG, '%{public}s',
                          \`MS\_LITE\_LOG: crop info.width = ${info.size.width}\`);
                        hilog.info(0xFF00, TAG, '%{public}s',
                          \`MS\_LITE\_LOG: crop info.height = ${info.size.height}\`);
                        // Set the size of readBuffer.
                        let readBuffer = new ArrayBuffer(this.modelInputHeight \* this.modelInputWidth \* 4);
                        await pixelMap.readPixelsToBuffer(readBuffer);
                        hilog.info(0xFF00, TAG, '%{public}s',
                          \`MS\_LITE\_LOG: Succeeded in reading image pixel data, buffer: ${readBuffer.byteLength}\`);
                        // Convert readBuffer to the float32 format, and standardize the image.
                        const imageArr =
                          new Uint8Array(readBuffer.slice(0, this.modelInputHeight \* this.modelInputWidth \* 4));
                        hilog.info(0xFF00, TAG, '%{public}s',
                          \`MS\_LITE\_LOG: imageArr length: ${imageArr.length}\`);

                        let means = \[0.485, 0.456, 0.406\];
                        let stds = \[0.229, 0.224, 0.225\];
                        let float32View = new Float32Array(this.modelInputHeight \* this.modelInputWidth \* 3);
                        let index = 0;
                        for (let i = 0; i < imageArr.length; i++) {
                          if ((i + 1) % 4 === 0) {
                            float32View\[index\] = (imageArr\[i - 3\] / 255.0 - means\[0\]) / stds\[0\]; // B
                            float32View\[index+1\] = (imageArr\[i - 2\] / 255.0 - means\[1\]) / stds\[1\]; // G
                            float32View\[index+2\] = (imageArr\[i - 1\] / 255.0 - means\[2\]) / stds\[2\]; // R
                            index += 3;
                          }
                        }
                        hilog.info(0xFF00, TAG, '%{public}s',
                          \`MS\_LITE\_LOG: float32View length: ${float32View.length}\`);
                        let printStr = 'float32View data:';
                        for (let i = 0; i < 20; i++) {
                          printStr += ' ' + float32View\[i\];
                        }
                        hilog.info(0xFF00, TAG, '%{public}s',
                          \`MS\_LITE\_LOG: float32View data: ${printStr}\`);

                        // Call the C++ runDemo.
                        hilog.info(0xFF00, TAG, '%{public}s',
                          \`MS\_LITE\_LOG: \*\*\* Start MSLite Demo \*\*\*\`);

                        let output: Array<number> = msliteNapi.runDemo(Array.from(float32View), resMgr);
                        hilog.info(0xFF00, TAG, '%{public}s',
                          \`MS\_LITE\_WARN: output length = ${output.length}, value = ${output.slice(0, 20)}\`);

                        // Obtain the top 5 maximum numbers of categories.
                        this.max = 0;
                        this.maxIndex = 0;
                        this.maxArray = \[\];
                        this.maxIndexArray = \[\];
                        let newArray = output.filter(value => value !== this.max);
                        for (let n = 0; n < 5; n++) {
                          this.max = output\[0\];
                          this.maxIndex = 0;
                          // Obtain the maximum value.
                          for (let m = 0; m < newArray.length; m++) {
                            if (newArray\[m\] > this.max) {
                              this.max = newArray\[m\];
                              this.maxIndex = m;
                            }
                          }
                          this.maxArray.push(Math.round(this.max \* 10000));
                          this.maxIndexArray.push(this.maxIndex);
                          // Call the array filter function.
                          newArray = newArray.filter(value => value !== this.max);
                        }
                        hilog.info(0xFF00, TAG, '%{public}s',
                          \`MS\_LITE\_LOG: max: ${this.maxArray}\`);
                        hilog.info(0xFF00, TAG, '%{public}s',
                          \`MS\_LITE\_LOG: maxIndex: ${this.maxIndexArray}\`);

                        hilog.info(0xFF00, TAG, '%{public}s',
                          \`MS\_LITE\_LOG: \*\*\* Finished MSLite Demo \*\*\*\`);
                      }).catch((error: BusinessError) => {
                        hilog.error(0xFF00, TAG, '%{public}s',
                          \`MS\_LITE\_ERR: getRawFileContent promise error is: ${error}\`);
                      })
                    })
                    // 5. Close the file.
                    fileIo.closeSync(file);
                  })
                })
              } catch (err) {
                hilog.error(0xFF00, TAG, '%{public}s',
                  \`MS\_LITE\_ERR: uri: open file fd failed. ${err}\`);
              }
            })
        })
      }.width('100%')
    }
    .height('100%')
  }
}

## Debugging and Verification

1.  On DevEco Studio, connect to the device, click **Run entry**, and build your own HAP.
    
    Launching com.samples.mindsporelitecdemo
    $ hdc shell aa force-stop com.samples.mindsporelitecdemo
    $ hdc shell mkdir data/local/tmp/xxx
    $ hdc file send C:\\Users\\xxx\\MindSporeLiteCDemo\\entry\\build\\default\\outputs\\default\\entry-default-signed.hap "data/local/tmp/xxx"
    $ hdc shell bm install -p data/local/tmp/xxx
    $ hdc shell rm -rf data/local/tmp/xxx
    $ hdc shell aa start -a EntryAbility -b com.samples.mindsporelitecdemo
    
2.  Touch the **photo** button on the device screen, select an image, and touch **OK**. The classification result of the selected image is displayed on the device screen. In the log printing result, filter images by the keyword **MS\_LITE**. The following information is displayed:
    
    08-05 17:15:52.001   4684-4684    A03d00/JSAPP                   pid-4684              I     MS\_LITE\_LOG: PhotoViewPicker.select successfully, photoSelectResult uri: {"photoUris":\["file://media/Photo/13/IMG\_1501955351\_012/plant.jpg"\]}
    ...
    08-05 17:15:52.627   4684-4684    A03d00/JSAPP                   pid-4684              I     MS\_LITE\_LOG: crop info.width = 224
    08-05 17:15:52.627   4684-4684    A03d00/JSAPP                   pid-4684              I     MS\_LITE\_LOG: crop info.height = 224
    08-05 17:15:52.628   4684-4684    A03d00/JSAPP                   pid-4684              I     MS\_LITE\_LOG: Succeeded in reading image pixel data, buffer: 200704
    08-05 17:15:52.971   4684-4684    A03d00/JSAPP                   pid-4684              I     MS\_LITE\_LOG: float32View data: float32View data: 1.2385478019714355 1.308123230934143 1.4722440242767334 1.2385478019714355 1.308123230934143 1.4722440242767334 1.2385478019714355 1.308123230934143 1.4722440242767334 1.2385478019714355 1.308123230934143 1.4722440242767334 1.2385478019714355 1.308123230934143 1.4722440242767334 1.2385478019714355 1.308123230934143 1.4722440242767334 1.2385478019714355 1.308123230934143
    08-05 17:15:52.971   4684-4684    A03d00/JSAPP                   pid-4684              I     MS\_LITE\_LOG: \*\*\* Start MSLite Demo \*\*\*
    08-05 17:15:53.454   4684-4684    A00000/\[MSLiteNapi\]            pid-4684              I     MS\_LITE\_LOG: Build MSLite model success.
    08-05 17:15:53.753   4684-4684    A00000/\[MSLiteNapi\]            pid-4684              I     MS\_LITE\_LOG: Run MSLite model Predict success.
    08-05 17:15:53.753   4684-4684    A00000/\[MSLiteNapi\]            pid-4684              I     MS\_LITE\_LOG: Get model outputs:
    08-05 17:15:53.753   4684-4684    A00000/\[MSLiteNapi\]            pid-4684              I     MS\_LITE\_LOG: - Tensor 0 name is: Default/head-MobileNetV2Head/Sigmoid-op466.
    08-05 17:15:53.753   4684-4684    A00000/\[MSLiteNapi\]            pid-4684              I     MS\_LITE\_LOG: - Tensor data is:
    08-05 17:15:53.753   4684-4684    A00000/\[MSLiteNapi\]            pid-4684              I     MS\_LITE\_LOG: 3.43385e-06 1.40285e-05 9.11969e-07 4.91007e-05 9.50266e-07 3.94537e-07 0.0434676 3.97196e-05 0.00054832 0.000246202 1.576e-05 3.6494e-06 1.23553e-05 0.196977 5.3028e-05 3.29346e-05 4.90475e-07 1.66109e-06 7.03273e-06 8.83677e-07 3.1365e-06
    08-05 17:15:53.781   4684-4684    A03d00/JSAPP                   pid-4684              W     MS\_LITE\_WARN: output length =  500 ;value =  0.0000034338463592575863,0.000014028532859811094,9.119685273617506e-7,0.000049100715841632336,9.502661555416125e-7,3.945370394831116e-7,0.04346757382154465,0.00003971960904891603,0.0005483203567564487,0.00024620210751891136,0.000015759984307806008,0.0000036493988773145247,0.00001235533181898063,0.1969769448041916,0.000053027983085485175,0.000032934600312728435,4.904751449430478e-7,0.0000016610861166554969,0.000007032729172351537,8.836767619868624e-7
    08-05 17:15:53.831   4684-4684    A03d00/JSAPP                   pid-4684              I     MS\_LITE\_LOG: max:9497,7756,1970,435,46
    08-05 17:15:53.831   4684-4684    A03d00/JSAPP                   pid-4684              I     MS\_LITE\_LOG: maxIndex:323,46,13,6,349
    08-05 17:15:53.831   4684-4684    A03d00/JSAPP                   pid-4684              I     MS\_LITE\_LOG: \*\*\* Finished MSLite Demo \*\*\*
    

## Effects

Touch the **photo** button on the device screen, select an image, and touch **OK**. The top 4 categories of the image are displayed below the image.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b0/v3/W7NbhnebQWygUtdpWeuCSQ/en-us_image_0000002568684995.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062128Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=EFB5349A12042B9E1134A931D0D070641921FF45FEA576ED4A48E2374C19D6FD) ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b5/v3/gl4fFz2hQ5eYZAuHJl-mqQ/en-us_image_0000002568765003.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062128Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=E1E4897D59A711369B498884B2818621AD3C7AE6673896E1E15A5D50A84CC3BA)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/11/v3/mTbIFb5FSvmtzh8IjvXUcg/en-us_image_0000002537765278.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062128Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=95A0C782325840FB29DBD6F7F3D5A43C5AFE4F42ED50B4817D0BEEF8C198DAB7) ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fd/v3/GSMrPTurTMiKG8QU7n1s_A/en-us_image_0000002568765005.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062128Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=FB70BDEDDCCF3EFC90DF413ADF960E9389C2512C8FB67506108814B8CF81B2B4)
