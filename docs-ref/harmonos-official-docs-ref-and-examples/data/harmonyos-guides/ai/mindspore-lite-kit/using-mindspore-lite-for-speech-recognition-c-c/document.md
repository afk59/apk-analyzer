# Using MindSpore Lite for Speech Recognition (C/C++)

#### When to Use

You can use [MindSpore](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-mindspore) to quickly deploy AI algorithms into your application to perform AI model inference for speech recognition.

Speech recognition can convert an audio file into text, which is widely used in intelligent voice assistants, voice input, and voice search.

#### Environment Configuration

If you want to execute the sample on an emulator, see [Running Your App on the Emulator](../../../coding-and-debugging/running-your-app-on-the-emulator/document.md).

#### Basic Concepts

-   N-API: a set of native APIs used to build ArkTS components. N-APIs can be used to encapsulate C/C++ libraries into ArkTS modules.

#### How to Develop

1.  Select a speech recognition model.
2.  Use the MindSpore Lite inference model on the device to implement speech recognition.

#### Development Procedure

This section uses the inference of a speech recognition model as an example to demonstrate how to implement a speech recognition application using MindSpore Lite.

## Selecting an Appropriate Model

The speech recognition model files **tiny-encoder.ms**, **tiny-decoder-main.ms**, and **tiny-decoder-loop.ms** used in this sample application are stored in the **entry/src/main/resources/rawfile** directory.

## Writing the Code for Audio Playback

Call [@ohos.multimedia.media](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-media) and [@ohos.multimedia.audio](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-audio) to play audio.

// player.ets
import { media } from '@kit.MediaKit';
import { common } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { audio } from '@kit.AudioKit';
import { UIContext } from '@kit.ArkUI';
import { hilog } from '@kit.PerformanceAnalysisKit';

const TAG = 'MindSporeLite';

export default class AVPlayerDemo {
  private isSeek: boolean = false; // Disable the seek operation.
  // Set the AVPlayer callback.
  setAVPlayerCallback(avPlayer: media.AVPlayer) {
    // Callback for the seek operation.
    avPlayer.on('seekDone', (seekDoneTime: number) => {
      hilog.info(0xFF00, TAG, '%{public}s', \`MS\_LITE\_LOG: AVPlayer seek succeeded, seek time is ${seekDoneTime}\`);
    });
    // Callback invoked if an error occurs while the AVPlayer is playing audio. In such a case, reset() is called to reset the AVPlayer.
    avPlayer.on('error', (err: BusinessError) => {
      hilog.error(0xFF00, TAG, '%{public}s',
        \`MS\_LITE\_ERR: Invoke avPlayer failed, code is ${err.code}, message is ${err.message}\`);
      avPlayer.reset(); // Call reset() to reset the AVPlayer, which enters the idle state.
    });
    // Callback for state changes.
    avPlayer.on('stateChange', async (state: string, reason: media.StateChangeReason) => {
      switch (state) {
        case 'idle': // This state is reported upon a successful callback of reset().
          hilog.info(0xFF00, TAG, '%{public}s', 'MS\_LITE\_LOG: AVPlayer state idle called.');
          avPlayer.release(); // Call release() to release the instance.
          break;
        case 'initialized': // This state is reported when the AVPlayer sets the playback source.
          hilog.info(0xFF00, TAG, '%{public}s', 'MS\_LITE\_LOG: AVPlayer state initialized called.');
          avPlayer.audioRendererInfo = {
            usage: audio.StreamUsage.STREAM\_USAGE\_MUSIC, // Audio stream usage type: music. Set this parameter based on the service scenario.
            rendererFlags: 0 // Audio renderer flag.
          };
          avPlayer.prepare();
          break;
        case 'prepared': // This state is reported upon a successful callback of prepare().
          hilog.info(0xFF00, TAG, '%{public}s', 'MS\_LITE\_LOG: AVPlayer state prepared called.');
          avPlayer.play(); // Call play() to start playback.
          break;
        case 'playing': // This state is reported upon a successful callback of play().
          hilog.info(0xFF00, TAG, '%{public}s', 'MS\_LITE\_LOG: AVPlayer state playing called.');
          if (this.isSeek) {
            hilog.info(0xFF00, TAG, '%{public}s', 'MS\_LITE\_LOG: AVPlayer start to seek.');
            avPlayer.seek(0); // Move the playback position to the beginning of the audio.
          } else {
            // When the seek operation is not supported, the playback continues until it reaches the end.
            hilog.info(0xFF00, TAG, '%{public}s', 'MS\_LITE\_LOG: AVPlayer wait to play end.');
          }
          break;
        case 'paused': // This state is reported upon a successful callback of pause().
          hilog.info(0xFF00, TAG, '%{public}s', 'MS\_LITE\_LOG: AVPlayer state paused called.');
          setTimeout(() => {
            hilog.info(0xFF00, TAG, '%{public}s', 'MS\_LITE\_LOG: AVPlayer paused wait to play again');
            avPlayer.play(); // After the playback is paused for 3 seconds, call the play API again to start playback.
          }, 3000);
          break;
        case 'completed': // This state is reported upon the completion of the playback.
          hilog.info(0xFF00, TAG, '%{public}s', 'MS\_LITE\_LOG: AVPlayer state completed called.');
          avPlayer.stop(); // Call stop() to stop the playback.
          break;
        case 'stopped': // This state is reported upon a successful callback of stop().
          hilog.info(0xFF00, TAG, '%{public}s', 'MS\_LITE\_LOG: AVPlayer state stopped called.');
          avPlayer.reset(); // Call reset() to reset the AVPlayer.
          break;
        case 'released':
          hilog.info(0xFF00, TAG, '%{public}s', 'MS\_LITE\_LOG: AVPlayer state released called.');
          break;
        default:
          hilog.info(0xFF00, TAG, '%{public}s', 'MS\_LITE\_LOG: AVPlayer state unknown called.');
          break;
      }
    });
  }

  // Use the resource management API to obtain the audio file and play the audio file through the fdSrc attribute.
  async avPlayerFdSrcDemo() {
    // Create an AVPlayer instance.
    let avPlayer: media.AVPlayer = await media.createAVPlayer();
    // Create a callback for state changes.
    this.setAVPlayerCallback(avPlayer);
    // Call getRawFd of the resourceManager member of UIAbilityContext to obtain the media asset URL.
    // The return type is {fd,offset,length}, where fd indicates the file descriptor address of the HAP file, offset indicates the media asset offset, and length indicates the duration of the media asset to play.
    let context = new UIContext().getHostContext() as common.UIAbilityContext;
    let fileDescriptor = await context.resourceManager.getRawFd('zh.wav');
    let avFileDescriptor: media.AVFileDescriptor =
      { fd: fileDescriptor.fd, offset: fileDescriptor.offset, length: fileDescriptor.length };
    this.isSeek = true; // Enable the seek operation.
    // Assign a value to fdSrc to trigger the reporting of the initialized state.
    avPlayer.fdSrc = avFileDescriptor;
  }
}

## Writing the Code for Speech Recognition

In **entry/src/main/cpp/mslite\_napi.cpp**, call [MindSpore](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-mindspore) to perform inference on the three models in sequence. The inference process is as follows:

1.  Include the corresponding header files. You need to download third-party libraries. Wherein, **librosa** is accessible in [LibrosaCpp](https://github.com/ewan-xu/LibrosaCpp), and **libsamplerate** is accessible in [libsamplerate](https://github.com/libsndfile/libsamplerate). Download these libraries and save them to the **entry/src/main/cpp/third\_party** directory. Download **AudioFile.h** from [AudioFile](https://github.com/adamstark/AudioFile/blob/1.1.2/AudioFile.h) and **base64.h** and **base64.cpp** from [whisper.axera](https://github.com/ml-inory/whisper.axera/tree/main/cpp/src), and save the files to **entry/src/main/cpp/src**.
    
    #include "AudioFile.h"
    #include "base64.h"
    #include "napi/native\_api.h"
    #include "utils.h"
    #include <algorithm>
    #include <cstdlib>
    #include <fstream>
    #include <hilog/log.h>
    #include <iostream>
    #include <librosa/librosa.h>
    #include <mindspore/context.h>
    #include <mindspore/model.h>
    #include <mindspore/status.h>
    #include <mindspore/tensor.h>
    #include <mindspore/types.h>
    #include <numeric> 
    #include <rawfile/raw\_file\_manager.h>
    #include <sstream>
    #include <vector>
    
2.  Read related files such as audio files and model files, and converts them to buffer data.
    
    #define LOGI(...) ((void)OH\_LOG\_Print(LOG\_APP, LOG\_INFO, LOG\_DOMAIN, "\[MSLiteNapi\]", \_\_VA\_ARGS\_\_))
    #define LOGD(...) ((void)OH\_LOG\_Print(LOG\_APP, LOG\_DEBUG, LOG\_DOMAIN, "\[MSLiteNapi\]", \_\_VA\_ARGS\_\_))
    #define LOGW(...) ((void)OH\_LOG\_Print(LOG\_APP, LOG\_WARN, LOG\_DOMAIN, "\[MSLiteNapi\]", \_\_VA\_ARGS\_\_))
    #define LOGE(...) ((void)OH\_LOG\_Print(LOG\_APP, LOG\_ERROR, LOG\_DOMAIN, "\[MSLiteNapi\]", \_\_VA\_ARGS\_\_))
    
    using BinBuffer = std::pair<void \*, size\_t>;
    
    BinBuffer ReadBinFile(NativeResourceManager \*nativeResourceManager, const std::string &modelName)
    {
        auto rawFile = OH\_ResourceManager\_OpenRawFile(nativeResourceManager, modelName.c\_str());
        if (rawFile == nullptr) {
            LOGE("MS\_LITE\_ERR: Open model file failed");
            return BinBuffer(nullptr, 0);
        }
        long fileSize = OH\_ResourceManager\_GetRawFileSize(rawFile);
        if (fileSize <= 0) {
            LOGE("MS\_LITE\_ERR: FileSize not correct");
            return BinBuffer(nullptr, 0);
        }
        void \*buffer = malloc(fileSize);
        if (buffer == nullptr) {
            LOGE("MS\_LITE\_ERR: OH\_ResourceManager\_ReadRawFile failed");
            return BinBuffer(nullptr, 0);
        }
        int ret = OH\_ResourceManager\_ReadRawFile(rawFile, buffer, fileSize);
        if (ret == 0) {
            LOGE("MS\_LITE\_ERR: OH\_ResourceManager\_ReadRawFile failed");
            OH\_ResourceManager\_CloseRawFile(rawFile);
            return BinBuffer(nullptr, 0);
        }
        OH\_ResourceManager\_CloseRawFile(rawFile);
        return BinBuffer(buffer, fileSize);
    }
    
    BinBuffer ReadTokens(NativeResourceManager \*nativeResourceManager, const std::string &modelName)
    {
        auto rawFile = OH\_ResourceManager\_OpenRawFile(nativeResourceManager, modelName.c\_str());
        if (rawFile == nullptr) {
            LOGE("MS\_LITE\_ERR: Open model file failed");
            return BinBuffer(nullptr, 0);
        }
        long fileSize = OH\_ResourceManager\_GetRawFileSize(rawFile);
        if (fileSize <= 0) {
            LOGE("MS\_LITE\_ERR: FileSize not correct");
            return BinBuffer(nullptr, 0);
        }
        void \*buffer = malloc(fileSize);
        if (buffer == nullptr) {
            LOGE("MS\_LITE\_ERR: OH\_ResourceManager\_ReadRawFile failed");
            return BinBuffer(nullptr, 0);
        }
        int ret = OH\_ResourceManager\_ReadRawFile(rawFile, buffer, fileSize);
        if (ret == 0) {
            LOGE("MS\_LITE\_ERR: OH\_ResourceManager\_ReadRawFile failed");
            OH\_ResourceManager\_CloseRawFile(rawFile);
            return BinBuffer(nullptr, 0);
        }
        OH\_ResourceManager\_CloseRawFile(rawFile);
        BinBuffer res(buffer, fileSize);
        return res;
    }
    
3.  Create a context, set the device type, and load the model.
    
    void DestroyModelBuffer(void \*\*buffer)
    {
        if (buffer == nullptr) {
            return;
        }
        free(\*buffer);
        \*buffer = nullptr;
    }
    
    OH\_AI\_ModelHandle CreateMSLiteModel(BinBuffer &bin)
    {
        // Create and configure the context for model inference.
        auto context = OH\_AI\_ContextCreate();
        if (context == nullptr) {
            DestroyModelBuffer(&bin.first);
            LOGE("MS\_LITE\_ERR: Create MSLite context failed.\\n");
            return nullptr;
        }
        auto cpu\_device\_info = OH\_AI\_DeviceInfoCreate(OH\_AI\_DEVICETYPE\_CPU);
        OH\_AI\_DeviceInfoSetEnableFP16(cpu\_device\_info, false);
        OH\_AI\_ContextAddDeviceInfo(context, cpu\_device\_info);
    
        // Create a model.
        auto model = OH\_AI\_ModelCreate();
        if (model == nullptr) {
            DestroyModelBuffer(&bin.first);
            LOGE("MS\_LITE\_ERR: Allocate MSLite Model failed.\\n");
            return nullptr;
        }
    
        // Load and build the inference model. The model type is OH\_AI\_MODELTYPE\_MINDIR.
        auto build\_ret = OH\_AI\_ModelBuild(model, bin.first, bin.second, OH\_AI\_MODELTYPE\_MINDIR, context);
        DestroyModelBuffer(&bin.first);
        if (build\_ret != OH\_AI\_STATUS\_SUCCESS) {
            OH\_AI\_ModelDestroy(&model);
            LOGE("MS\_LITE\_ERR: Build MSLite model failed.\\n");
            return nullptr;
        }
        LOGI("MS\_LITE\_LOG: Build MSLite model success.\\n");
        return model;
    }
    
4.  Set the model input data, and perform model inference.
    
    constexpr int K\_NUM\_PRINT\_OF\_OUT\_DATA = 20;
    
    int FillInputTensor(OH\_AI\_TensorHandle input, const BinBuffer &bin)
    {
        if (OH\_AI\_TensorGetDataSize(input) != bin.second) {
            return OH\_AI\_STATUS\_LITE\_INPUT\_PARAM\_INVALID;
        }
        char \*data = (char \*)OH\_AI\_TensorGetMutableData(input);
        memcpy(data, (const char \*)bin.first, OH\_AI\_TensorGetDataSize(input));
        return OH\_AI\_STATUS\_SUCCESS;
    }
    
    // Perform model inference.
    int RunMSLiteModel(OH\_AI\_ModelHandle model, std::vector<BinBuffer> inputBins)
    {
        // Set the model input data.
        auto inputs = OH\_AI\_ModelGetInputs(model);
        for(int i = 0; i < inputBins.size(); i++)
        {
            auto ret = FillInputTensor(inputs.handle\_list\[i\], inputBins\[i\]);
            if (ret != OH\_AI\_STATUS\_SUCCESS) {
                LOGE("MS\_LITE\_ERR: set input %{public}d error.\\n", i);
                return OH\_AI\_STATUS\_LITE\_ERROR;
            }
        }
    
        // Obtain the output tensor of the model.
        auto outputs = OH\_AI\_ModelGetOutputs(model);
    
        // Model inference
        auto predict\_ret = OH\_AI\_ModelPredict(model, inputs, &outputs, nullptr, nullptr);
        if (predict\_ret != OH\_AI\_STATUS\_SUCCESS) {
            OH\_AI\_ModelDestroy(&model);
            LOGE("MS\_LITE\_ERR: MSLite Predict error.\\n");
            return OH\_AI\_STATUS\_LITE\_ERROR;
        }
        LOGD("MS\_LITE\_LOG: Run MSLite model Predict success.\\n");
    
        // Print the output data.
        LOGD("MS\_LITE\_LOG: Get model outputs:\\n");
        for (size\_t i = 0; i < outputs.handle\_num; i++) {
            auto tensor = outputs.handle\_list\[i\];
            LOGD("MS\_LITE\_LOG: - Tensor %{public}d name is: %{public}s.\\n", static\_cast<int>(i),
                 OH\_AI\_TensorGetName(tensor));
            LOGD("MS\_LITE\_LOG: - Tensor %{public}d size is: %{public}d.\\n", static\_cast<int>(i),
                 (int)OH\_AI\_TensorGetDataSize(tensor));
            LOGD("MS\_LITE\_LOG: - Tensor data is:\\n");
            auto out\_data = reinterpret\_cast<const float \*>(OH\_AI\_TensorGetData(tensor));
            std::stringstream outStr;
            for (int i = 0; (i < OH\_AI\_TensorGetElementNum(tensor)) && (i <= K\_NUM\_PRINT\_OF\_OUT\_DATA); i++) {
                outStr << out\_data\[i\] << " ";
            }
            LOGD("MS\_LITE\_LOG: %{public}s", outStr.str().c\_str());
        }
        return OH\_AI\_STATUS\_SUCCESS;
    }
    
5.  Repeat the preceding procedure for the remaining models.
    
    const float NEG\_INF = -std::numeric\_limits<float>::infinity();
    const int WHISPER\_SOT = 50258;
    const int WHISPER\_TRANSCRIBE = 50359;
    const int WHISPER\_TRANSLATE = 50358;
    const int WHISPER\_NO\_TIMESTAMPS = 50363;
    const int WHISPER\_EOT = 50257;
    const int WHISPER\_BLANK = 220;
    const int WHISPER\_NO\_SPEECH = 50362;
    const int WHISPER\_N\_TEXT\_CTX = 448;
    const int WHISPER\_N\_TEXT\_STATE = 384;
    constexpr int WHISPER\_SAMPLE\_RATE = 16000;
    
    BinBuffer GetMSOutput(OH\_AI\_TensorHandle output)
    {
        float \*outputData = reinterpret\_cast<float \*>(OH\_AI\_TensorGetMutableData(output));
        size\_t size = OH\_AI\_TensorGetDataSize(output);
        return {outputData, size};
    }
    
    void SuppressTokens(BinBuffer &logits, bool isInitial)
    {
        auto logits\_data = static\_cast<float \*>(logits.first);
        if (isInitial) {
            logits\_data\[WHISPER\_EOT\] = NEG\_INF;
            logits\_data\[WHISPER\_BLANK\] = NEG\_INF;
        }
    
        // Suppress other tokens.
        logits\_data\[WHISPER\_NO\_TIMESTAMPS\] = NEG\_INF;
        logits\_data\[WHISPER\_SOT\] = NEG\_INF;
        logits\_data\[WHISPER\_NO\_SPEECH\] = NEG\_INF;
        logits\_data\[WHISPER\_TRANSLATE\] = NEG\_INF;
    }
    
    std::vector<int> LoopPredict(const OH\_AI\_ModelHandle model, const BinBuffer &n\_layer\_cross\_k,
                                 const BinBuffer &n\_layer\_cross\_v, const BinBuffer &logits\_init,
                                 BinBuffer &out\_n\_layer\_self\_k\_cache, BinBuffer &out\_n\_layer\_self\_v\_cache,
                                 const BinBuffer &data\_embedding, const int loop, const int offset\_init)
    {
        BinBuffer logits{nullptr, 51865 \* sizeof(float)};
        logits.first = malloc(logits.second);
        if (!logits.first) {
            LOGE("MS\_LITE\_ERR: Fail to malloc!\\n");
            return {};
        }
        void \*logits\_init\_src = static\_cast<char \*>(logits\_init.first) + 51865 \* 3 \* sizeof(float);
        memcpy(logits.first, logits\_init\_src, logits.second);
        SuppressTokens(logits, true);
    
        std::vector<int> output\_token;
        float \*logits\_data = static\_cast<float \*>(logits.first);
        int max\_token\_id = 0;
        float max\_token = logits\_data\[0\];
        for (int i = 0; i < logits.second / sizeof(float); i++) {
            if (logits\_data\[i\] > max\_token) {
                max\_token\_id = i;
                max\_token = logits\_data\[i\];
            }
        }
    
        int offset = offset\_init;
        BinBuffer slice{nullptr, 0};
        slice.second = WHISPER\_N\_TEXT\_STATE \* sizeof(float);
        slice.first = malloc(slice.second);
        if (!slice.first) {
            LOGE("MS\_LITE\_ERR: Fail to malloc!\\n");
            return {};
        }
    
        auto out\_n\_layer\_self\_k\_cache\_new = out\_n\_layer\_self\_k\_cache;
        auto out\_n\_layer\_self\_v\_cache\_new = out\_n\_layer\_self\_v\_cache;
    
        for (size\_t i = 0; i < loop; i++) {
            if (max\_token\_id == WHISPER\_EOT) {
                break;
            }
            output\_token.push\_back(max\_token\_id);
            std::vector<float> mask(WHISPER\_N\_TEXT\_CTX, 0.0f);
            for (size\_t i = 0; i < WHISPER\_N\_TEXT\_CTX - offset - 1; ++i) {
                mask\[i\] = NEG\_INF;
            }
            BinBuffer tokens{&max\_token\_id, sizeof(int)};
    
            void \*data\_embedding\_src =
                static\_cast<char \*>(data\_embedding.first) + offset \* WHISPER\_N\_TEXT\_STATE \* sizeof(float);
            memcpy(slice.first, data\_embedding\_src, slice.second);
            BinBuffer mask\_bin(mask.data(), mask.size() \* sizeof(float));
            int ret = RunMSLiteModel(model, {tokens, out\_n\_layer\_self\_k\_cache\_new, out\_n\_layer\_self\_v\_cache\_new,
                                             n\_layer\_cross\_k, n\_layer\_cross\_v, slice, mask\_bin});
    
            auto outputs = OH\_AI\_ModelGetOutputs(model);
            logits = GetMSOutput(outputs.handle\_list\[0\]);
            out\_n\_layer\_self\_k\_cache\_new = GetMSOutput(outputs.handle\_list\[1\]);
            out\_n\_layer\_self\_v\_cache\_new = GetMSOutput(outputs.handle\_list\[2\]);
            offset++;
            SuppressTokens(logits, false);
            logits\_data = static\_cast<float \*>(logits.first);
            max\_token = logits\_data\[0\];
    
            for (int j = 0; j < logits.second / sizeof(float); j++) {
                if (logits\_data\[j\] > max\_token) {
                    max\_token\_id = j;
                    max\_token = logits\_data\[j\];
                }
            }
            LOGI("MS\_LITE\_LOG: run decoder loop %{public}d ok!\\n token = %{public}d", i, max\_token\_id);
        }
        return output\_token;
    }
    
    std::vector<std::string> ProcessDataLines(const BinBuffer token\_txt)
    {
        void \*data\_ptr = token\_txt.first;
        size\_t data\_size = token\_txt.second;
        std::vector<std::string> tokens;
    
        const char \*char\_data = static\_cast<const char \*>(data\_ptr);
        std::stringstream ss(std::string(char\_data, char\_data + data\_size));
        std::string line;
        while (std::getline(ss, line)) {
            size\_t space\_pos = line.find(' ');
            tokens.push\_back(line.substr(0, space\_pos));
        }
        return tokens;
    }
    
    static napi\_value RunDemo(napi\_env env, napi\_callback\_info info)
    {
        // Perform sample inference.
        napi\_value error\_ret;
        napi\_create\_int32(env, -1, &error\_ret);
        size\_t argc = 1;
        napi\_value argv\[1\] = {nullptr};
        napi\_get\_cb\_info(env, info, &argc, argv, nullptr, nullptr);
        auto resourcesManager = OH\_ResourceManager\_InitNativeResourceManager(env, argv\[0\]);
    
        // Data preprocessing
        AudioFile<float> audioFile;
        std::string filePath = "zh.wav";
        auto audioBin = ReadBinFile(resourcesManager, filePath);
        if (audioBin.first == nullptr) {
            LOGE("MS\_LITE\_ERR: Fail to read  %{public}s!", filePath.c\_str());
            return error\_ret;
        }
        size\_t dataSize = audioBin.second;
        uint8\_t \*dataBuffer = (uint8\_t \*)audioBin.first;
        bool ok = audioFile.loadFromMemory(std::vector<uint8\_t>(dataBuffer, dataBuffer + dataSize));
        if (!ok) {
            LOGE("MS\_LITE\_ERR: Fail to read  %{public}s!", filePath.c\_str());
            return error\_ret;
        }
        std::vector<float> data(audioFile.samples\[0\]);
        ResampleAudio(data, audioFile.getSampleRate(), WHISPER\_SAMPLE\_RATE, 1, SRC\_SINC\_BEST\_QUALITY);
        std::vector<float> audio(data);
    
        int padding = 480000;
        int sr = 16000;
        int n\_fft = 480;
        int n\_hop = 160;
        int n\_mel = 80;
        int fmin = 0; // Minimum frequency. The default value is 0.0 Hz.
        int fmax =
            sr /
            2.0; // Maximum frequency. The default value is half of the sampling rate (sr/2.0).
        audio.insert(audio.end(), padding, 0.0f);
        std::vector<std::vector<float>> mels\_T =
            librosa::Feature::melspectrogram(audio, sr, n\_fft, n\_hop, "hann", true, "reflect", 2.f, n\_mel, fmin, fmax);
        std::cout << "mels: " << std::endl;
    
        std::vector<std::vector<float>> mels = TransposeMel(mels\_T);
        ProcessMelSpectrogram(mels);
    
        std::vector<float> inputMels(mels.size() \* mels\[0\].size(), 0);
        for (int i = 0; i < mels.size(); i++) {
            std::copy(mels\[i\].begin(), mels\[i\].end(), inputMels.begin() + i \* mels\[0\].size());
        }
    
        BinBuffer inputMelsBin(inputMels.data(), inputMels.size() \* sizeof(float));
    
        // Run inference on tiny-encoder.ms.
        auto encoderBin = ReadBinFile(resourcesManager, "tiny-encoder.ms");
        if (encoderBin.first == nullptr) {
            free(dataBuffer);
            dataBuffer = nullptr;
            return error\_ret;
        }
    
        auto encoder = CreateMSLiteModel(encoderBin);
    
        int ret = RunMSLiteModel(encoder, {inputMelsBin});
        if (ret != OH\_AI\_STATUS\_SUCCESS) {
            OH\_AI\_ModelDestroy(&encoder);
            return error\_ret;
        }
        LOGI("MS\_LITE\_LOG: run encoder ok!\\n");
    
        auto outputs = OH\_AI\_ModelGetOutputs(encoder);
        auto n\_layer\_cross\_k = GetMSOutput(outputs.handle\_list\[0\]);
        auto n\_layer\_cross\_v = GetMSOutput(outputs.handle\_list\[1\]);
    
        // Run inference on tiny-decoder-main.ms.
        std::vector<int> SOT\_SEQUENCE = {WHISPER\_SOT,
                                         WHISPER\_SOT + 1 + 1,
                                         WHISPER\_TRANSCRIBE, WHISPER\_NO\_TIMESTAMPS};
        BinBuffer sotSequence(SOT\_SEQUENCE.data(), SOT\_SEQUENCE.size() \* sizeof(int));
    
        const std::string decoder\_main\_path = "tiny-decoder-main.ms";
        auto decoderMainBin = ReadBinFile(resourcesManager, decoder\_main\_path);
        if (decoderMainBin.first == nullptr) {
            OH\_AI\_ModelDestroy(&encoder);
            return error\_ret;
        }
        auto decoder\_main = CreateMSLiteModel(decoderMainBin);
        int ret2 = RunMSLiteModel(decoder\_main, {sotSequence, n\_layer\_cross\_k, n\_layer\_cross\_v});
    
        if (ret2 != OH\_AI\_STATUS\_SUCCESS) {
            OH\_AI\_ModelDestroy(&decoder\_main);
            return error\_ret;
        }
        LOGI("MS\_LITE\_LOG: run decoder\_main ok!\\n");
    
        auto decoderMainOut = OH\_AI\_ModelGetOutputs(decoder\_main);
        auto logitsBin = GetMSOutput(decoderMainOut.handle\_list\[0\]);
        auto out\_n\_layer\_self\_k\_cache\_Bin = GetMSOutput(decoderMainOut.handle\_list\[1\]);
        auto out\_n\_layer\_self\_v\_cache\_Bin = GetMSOutput(decoderMainOut.handle\_list\[2\]);
    
        // Run inference on tiny-decoder-loop.ms.
        const std::string modelName3 = "tiny-decoder-loop.ms";
        auto modelBuffer3 = ReadBinFile(resourcesManager, modelName3);
        auto decoder\_loop = CreateMSLiteModel(modelBuffer3);
    
        const std::string dataName\_embedding = "tiny-positional\_embedding.bin"; // Obtain the input data.
        auto data\_embedding = ReadBinFile(resourcesManager, dataName\_embedding);
        if (data\_embedding.first == nullptr) {
            OH\_AI\_ModelDestroy(&encoder);
            OH\_AI\_ModelDestroy(&decoder\_main);
            OH\_AI\_ModelDestroy(&decoder\_loop);
            return error\_ret;
        }
    
        int loop\_times = WHISPER\_N\_TEXT\_CTX - SOT\_SEQUENCE.size();
        int offset\_init = SOT\_SEQUENCE.size();
        auto output\_tokens =
            LoopPredict(decoder\_loop, n\_layer\_cross\_k, n\_layer\_cross\_v, logitsBin, out\_n\_layer\_self\_k\_cache\_Bin,
                        out\_n\_layer\_self\_v\_cache\_Bin, data\_embedding, loop\_times, offset\_init);
    
        std::vector<std::string> token\_tables = ProcessDataLines(ReadTokens(resourcesManager, "tiny-tokens.txt"));
        std::string result;
        for (const auto i : output\_tokens) {
            char str\[1024\];
            base64\_decode((const uint8 \*)token\_tables\[i\].c\_str(), (uint32)token\_tables\[i\].size(), str);
            result += str;
        }
        LOGI("MS\_LITE\_LOG: result is -> %{public}s", result.c\_str());
    
        OH\_AI\_ModelDestroy(&encoder);
        OH\_AI\_ModelDestroy(&decoder\_main);
        OH\_AI\_ModelDestroy(&decoder\_loop);
    
        napi\_value out\_data;
        napi\_create\_string\_utf8(env, result.c\_str(), result.length(), &out\_data);
        return out\_data;
    }
    
6.  Write the **CMake** script to link the MindSpore Lite dynamic library.
    
    \# the minimum version of CMake.
    cmake\_minimum\_required(VERSION 3.5.0)
    project(test)
    # AudioFile.h
    set(CMAKE\_CXX\_STANDARD 17)
    set(CMAKE\_CXX\_STANDARD\_REQUIRED TRUE)
    set(NATIVERENDER\_PATH ${CMAKE\_CURRENT\_SOURCE\_DIR})
    
    if(DEFINED PACKAGE\_FIND\_FILE)
        include(${PACKAGE\_FIND\_FILE})
    endif()
    
    include\_directories(${NATIVERENDER\_PATH}
                        ${NATIVERENDER\_PATH}/include)
    
    # libsamplerate
    set(LIBSAMPLERATE\_DIR ${NATIVERENDER\_PATH}/third\_party/libsamplerate)
    include\_directories(${LIBSAMPLERATE\_DIR}/include)
    add\_subdirectory(${LIBSAMPLERATE\_DIR})
    
    include\_directories(${NATIVERENDER\_PATH}/third\_party/opencc/include/opencc)
    # src
    aux\_source\_directory(src SRC\_DIR)
    include\_directories(${NATIVERENDER\_PATH}/src)
    
    include\_directories(${CMAKE\_SOURCE\_DIR}/third\_party)
    
    file(GLOB SRC src/\*.cc)
    
    add\_library(entry SHARED mslite\_napi.cpp ${SRC})
    target\_link\_libraries(entry PUBLIC samplerate)
    target\_link\_libraries(entry PUBLIC mindspore\_lite\_ndk)
    target\_link\_libraries(entry PUBLIC hilog\_ndk.z)
    target\_link\_libraries(entry PUBLIC rawfile.z)
    target\_link\_libraries(entry PUBLIC ace\_napi.z)
    

## Use N-APIs to encapsulate the C++ dynamic library into an ArkTS module.

1.  In **entry/src/main/cpp/types/libentry/Index.d.ts**, define the ArkTS API runDemo() by adding the following content:
    
    export const runDemo: (a: Object) => string;
    
2.  In the **oh-package.json5** file, associate the API with the .so file to form a complete ArkTS module.
    
    {
      "name": "libentry.so",
      "types": "./Index.d.ts",
      "version": "1.0.0",
      "description": "MindSpore Lite inference module."
    }
    

## Invoke the encapsulated ArkTS module to perform inference and output the result.

In **entry/src/main/ets/pages/Index.ets**, call the encapsulated ArkTS module to process the inference result. If the system displays a message indicating that @nutpi/chinese\_transverter does not exist, install @nutpi/chinese\_transverter by referring to the guide of the third-party library for the simplified and traditional chinese converter.

// Index.ets
import msliteNapi from 'libentry.so'
import AVPlayerDemo from './player';
import { transverter, TransverterType, TransverterLanguage } from "@nutpi/chinese\_transverter"
import { hilog } from '@kit.PerformanceAnalysisKit';

const TAG = 'MindSporeLite';

@Entry
@Component
struct Index {
  @State message: string = 'MSLite Whisper Demo';
  @State wavName: string = 'zh.wav';
  @State content: string = '';

  build() {
    Row() {
      Column() {
        Text(this.message)
          .fontSize(30)
          .fontWeight(FontWeight.Bold);
        Button() {
          Text('Play Audio')
            .fontSize(20)
            .fontWeight(FontWeight.Medium)
        }
        .type(ButtonType.Capsule)
        .margin({
          top: 20
        })
        .backgroundColor('#0D9FFB')
        .width('40%')
        .height('5%')
        .onClick(async () =>{
          // Invoke functions in the avPlayerFdSrcDemo class.
          hilog.info(0xFF00, TAG, '%{public}s', \`MS\_LITE\_LOG: begin to play wav.\`);
          let myClass = new AVPlayerDemo();
          myClass.avPlayerFdSrcDemo();
        })
        Button() {
          Text ('Recognize Audio')
            .fontSize(20)
            .fontWeight(FontWeight.Medium)
        }
        .type(ButtonType.Capsule)
        .margin({
          top: 20
        })
        .backgroundColor('#0D9FFB')
        .width('40%')
        .height('5%')
        .onClick(() => {
          let resMgr = this.getUIContext()?.getHostContext()?.getApplicationContext().resourceManager;
          if (resMgr === undefined || resMgr === null) {
            hilog.error(0xFF00, TAG, '%{public}s', \`MS\_LITE\_ERR: get resourceManager failed.\`);
            return
          }
          // Call the encapsulated runDemo function.
          hilog.info(0xFF00, TAG, '%{public}s', \`MS\_LITE\_LOG: \*\*\* Start MSLite Demo \*\*\*\`);
          let output = msliteNapi.runDemo(resMgr);
          if (output === null || output.length === 0) {
            hilog.error(0xFF00, TAG, '%{public}s', \`MS\_LITE\_ERR: runDemo failed.\`);
            return
          }
          hilog.info(0xFF00, TAG, '%{public}s',
            \`MS\_LITE\_LOG: output length = ${output.length}; value = ${output.slice(0, 20)}\`);
          this.content = output;
          hilog.info(0xFF00, TAG, '%{public}s', \`MS\_LITE\_LOG: \*\*\* Finished MSLite Demo \*\*\*\`);
        })

        // Display the recognized content.
        if (this.content) {
          Text ('Recognized content:\\n' + transverter({
            type: TransverterType.SIMPLIFIED,
            str: this.content,
            language: TransverterLanguage.ZH\_CN
          }) + '\\n').focusable(true).fontSize(20).height('20%')
        }
      }.width('100%')
    }
    .height('100%')
  }
}

## Verification

1.  On DevEco Studio, connect to the device, click **Run entry**, and build your own HAP.
    
    Launching com.samples.mindsporelitecdemoasr
    $ hdc shell aa force-stop com.samples.mindsporelitecdemoasr
    $ hdc shell mkdir data/local/tmp/xxx
    $ hdc file send E:\\xxx\\entry\\build\\default\\outputs\\default\\entry-default-signed.hap "data/local/tmp/xxx"
    $ hdc shell bm install -p data/local/tmp/xxx
    $ hdc shell rm -rf data/local/tmp/xxx
    $ hdc shell aa start -a EntryAbility -b com.samples.mindsporelitecdemoasr
    com.samples.mindsporelitecdemoasr successfully launched...
    
2.  Tap the Play Audio button on the device screen to play the sample audio file. After you tap the Recognize Audio button, the content of the sample audio file is displayed on the device screen. Filter the keyword **MS\_LITE\_LOG** in the log printing result. The following information is displayed:
    
    05-16 14:53:44.200   1679-1679     A03d00/JSAPP                    com.sampl...cdemoasr  I     MS\_LITE\_LOG: begin to play wav.
    05-16 14:53:44.210   1679-1679     A03d00/JSAPP                    com.sampl...cdemoasr  I     \[a92ab1e0f831191, 0, 0\] MS\_LITE\_LOG: AVPlayer state initialized called.
    05-16 14:53:44.228   1679-1679     A03d00/JSAPP                    com.sampl...cdemoasr  I     \[a92ab1e0f831191, 0, 0\] MS\_LITE\_LOG: AVPlayer state prepared called.
    05-16 14:53:44.242   1679-1679     A03d00/JSAPP                    com.sampl...cdemoasr  I     MS\_LITE\_LOG: AVPlayer state playing called.
    05-16 14:53:44.242   1679-1679     A03d00/JSAPP                    com.sampl...cdemoasr  I     MS\_LITE\_LOG: AVPlayer start to seek.
    05-16 14:53:44.372   1679-1679     A03d00/JSAPP                    com.sampl...cdemoasr  I     MS\_LITE\_LOG: AVPlayer seek succeeded, seek time is 0
    05-16 14:53:49.621   1679-1679     A03d00/JSAPP                    com.sampl...cdemoasr  I     MS\_LITE\_LOG: AVPlayer state completed called.
    05-16 14:53:49.646   1679-1679     A03d00/JSAPP                    com.sampl...cdemoasr  I     MS\_LITE\_LOG: AVPlayer state stopped called.
    05-16 14:53:49.647   1679-1679     A03d00/JSAPP                    com.sampl...cdemoasr  I     MS\_LITE\_LOG: AVPlayer state idle called.
    05-16 14:53:49.649   1679-1679     A03d00/JSAPP                    com.sampl...cdemoasr  I     MS\_LITE\_LOG: AVPlayer state released called.
    05-16 14:53:53.282   1679-1679     A03d00/JSAPP                    com.sampl...cdemoasr  I     MS\_LITE\_LOG: \*\*\* Start MSLite Demo \*\*\*
    05-16 14:53:53.926   1679-1679     A00000/\[MSLiteNapi\]             com.sampl...cdemoasr  I     MS\_LITE\_LOG: Build MSLite model success.
    05-16 14:53:54.260   1679-1679     A00000/\[MSLiteNapi\]             com.sampl...cdemoasr  D     MS\_LITE\_LOG: Run MSLite model Predict success.
    05-16 14:53:54.260   1679-1679     A00000/\[MSLiteNapi\]             com.sampl...cdemoasr  D     MS\_LITE\_LOG: Get model outputs:
    05-16 14:53:54.260   1679-1679     A00000/\[MSLiteNapi\]             com.sampl...cdemoasr  D     MS\_LITE\_LOG: - Tensor 0 name is: n\_layer\_cross\_k.
    05-16 14:53:54.260   1679-1679     A00000/\[MSLiteNapi\]             com.sampl...cdemoasr  D     MS\_LITE\_LOG: - Tensor 0 size is: 9216000.
    05-16 14:53:54.260   1679-1679     A00000/\[MSLiteNapi\]             com.sampl...cdemoasr  D     MS\_LITE\_LOG: - Tensor data is:
    05-16 14:53:54.260   1679-1679     A00000/\[MSLiteNapi\]             com.sampl...cdemoasr  D     MS\_LITE\_LOG: -1.14678 -2.30223 0.868679 0.284441 1.03233 -2.02062 0.688163 -0.732034 -1.10553 1.43459 0.083885 -0.116173 -0.772636 1.5466 -0.631993 -0.897929 -0.0501685 -1.62517 0.375988 -1.77772 -0.432178
    05-16 14:53:54.260   1679-1679     A00000/\[MSLiteNapi\]             com.sampl...cdemoasr  D     MS\_LITE\_LOG: - Tensor 1 name is: n\_layer\_cross\_v.
    05-16 14:53:54.260   1679-1679     A00000/\[MSLiteNapi\]             com.sampl...cdemoasr  D     MS\_LITE\_LOG: - Tensor 1 size is: 9216000.
    05-16 14:53:54.260   1679-1679     A00000/\[MSLiteNapi\]             com.sampl...cdemoasr  D     MS\_LITE\_LOG: - Tensor data is:
    05-16 14:53:54.260   1679-1679     A00000/\[MSLiteNapi\]             com.sampl...cdemoasr  D     MS\_LITE\_LOG: 0.0876085 -0.560317 -0.652518 -0.116969 -0.182608 -9.40531e-05 0.186293 0.123206 0.0127445 0.0708352 -0.489624 -0.226322 -0.0686949 -0.0341293 -0.0719619 0.103588 0.398025 -0.444261 0.396124 -0.347295 0.00541205
    05-16 14:53:54.430   1679-1679     A00000/\[MSLiteNapi\]             com.sampl...cdemoasr  I     MS\_LITE\_LOG: Build MSLite model success.
    05-16 14:53:54.462   1679-1679     A00000/\[MSLiteNapi\]             com.sampl...cdemoasr  D     MS\_LITE\_LOG: Run MSLite model Predict success.
    ......
    05-16 14:53:55.272   1679-1679     A00000/\[MSLiteNapi\]             com.sampl...cdemoasr  I     MS\_LITE\_LOG: run decoder loop 16 ok!
                                                                                                    token = 50257
    05-16 14:53:55.334   1679-1679     A03d00/JSAPP                    com.sampl...cdemoasr  I     MS\_LITE\_LOG: \*\*\* Finished MSLite Demo \*\*\*
    

## Effects

After you tap the **Play Audio** button on the device screen, the sample audio file is played. After you tap the **Recognize Audio** button, the content of the sample audio file is displayed on the device screen.

| Initial Page | Page with Recognized Content |
| :-- | :-- |
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bb/v3/DXWUq-mWQfe1pGu6OLROWg/en-us_image_0000002537765280.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062128Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=54FEF216431CEDDB30CB670C94EF60B9A2D2119CFD736357231A02E8F8C1011D) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b2/v3/zApXZNmoTFy_NnuE6FUx5g/en-us_image_0000002537925220.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062128Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=5A37517A26D0D0EEF55017D9F12CF6D257D173857DC8F4DD380931F81AEF53A2) |

#### Related Samples

The following sample is provided to help you better understand how to develop speech recognition applications using MindSpore Lite:

-   \[MindSpore Lite ASR Application Development Based on Native APIs (C/C++) (API 14)\] ([https://gitcode.com/openharmony/applications\_app\_samples/tree/master/code/DocsSample/MindSporeLiteKit/MindSporeLiteCDemoASR](https://gitcode.com/openharmony/applications_app_samples/tree/master/code/DocsSample/MindSporeLiteKit/MindSporeLiteCDemoASR))
