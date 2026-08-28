# textToSpeech (Text to Speech)

This module converts text into speech and plays the speech, enabling real-time interaction between users and devices.

Currently, this service supports Chinese and English. The supported timbres include Ling Xiaoshan female voice, Laura female voice for English (US), and Ling Feizhe male voice.

**Start version**: 4.1.0(11)

#### Module Import

import { textToSpeech } from '@kit.CoreSpeechKit';

#### textToSpeech.createEngine

createEngine(createEngineParams: CreateEngineParams, callback: AsyncCallback<TextToSpeechEngine>): void

Creates a [TextToSpeechEngine](#section185526396124) instance and initializes the engine. This API returns the result asynchronously through a callback.

**System capability**: SystemCapability.AI.TextToSpeech

**Start version**: 4.1.0(11)

**Parameters**:

| 
Name

 | 

Type

 | 

Mandatory

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

createEngineParams

 | 

[CreateEngineParams](#section1638144844811)

 | 

Yes

 | 

Parameters for creating an engine instance.

 |
| 

callback

 | 

[AsyncCallback](../../../../system/basic-functions/basic-services-kit/arkts-apis/others/ohos-base-public-callback-information/document.md#asynccallback)<[TextToSpeechEngine](#section185526396124)\>

 | 

Yes

 | 

Callback of an engine instance.

 |

**Error codes**:

For details about the error codes, please refer to [ArkTS API Error Codes](../arkts-api-error-codes/document.md).

| 
Error Code

 | 

Error Message

 |
| :-- | :-- |
| 

401

 | 

Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed.

 |
| 

1002300002

 | 

The language is not supported.

 |
| 

1002300003

 | 

The person is not supported.

 |
| 

1002300005

 | 

Create engine failed.

 |

**Example**:

import { BusinessError } from '@kit.BasicServicesKit';
import { textToSpeech } from '@kit.CoreSpeechKit';

// Parameters for creating an engine instance.
let ttsEngine: textToSpeech.TextToSpeechEngine;
let extraParam: Record<string, Object> = {"style": 'interaction-broadcast', "locate": 'CN', "name": 'EngineName'};
let initParamsInfo: textToSpeech.CreateEngineParams = {
  language: 'zh-CN',
  person: 0,
  online: 1,
  extraParams: extraParam
};
// Call the API for creating an engine instance.
textToSpeech.createEngine(initParamsInfo, (err: BusinessError, textToSpeechEngine: textToSpeech.TextToSpeechEngine) => {
  if (!err) {
    console.info('Succeeded in creating engine.');
    // Obtain the engine instance.
    ttsEngine = textToSpeechEngine;
  } else {
    console.error(\`Failed to create engine. Code: ${err.code}, message: ${err.message}.\`);
  }
});

@Entry
@Component
struct Page {

  build() {
    // ...
  }
}

#### textToSpeech.createEngine

createEngine(createEngineParams: CreateEngineParams): Promise<TextToSpeechEngine>

Creates a [TextToSpeechEngine](#section185526396124) instance and initializes the engine. This API returns the result asynchronously through a promise.

**System capability**: SystemCapability.AI.TextToSpeech

**Start version**: 4.1.0(11)

**Parameters**:

| 
Name

 | 

Type

 | 

Mandatory

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

createEngineParams

 | 

[CreateEngineParams](#section1638144844811)

 | 

Yes

 | 

Parameters for creating an engine instance.

 |

**Returns**:

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

Promise<[TextToSpeechEngine](#section185526396124)\>

 | 

Promise that returns the engine instance created.

 |

**Error codes**:

For details about the error codes, please refer to [ArkTS API Error Codes](../arkts-api-error-codes/document.md).

| 
Error Code

 | 

Error Message

 |
| :-- | :-- |
| 

401

 | 

Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed.

 |
| 

1002300002

 | 

The language is not supported.

 |
| 

1002300003

 | 

The person is not supported.

 |
| 

1002300005

 | 

Create engine failed.

 |

**Example**:

import { BusinessError } from '@kit.BasicServicesKit';
import { textToSpeech } from '@kit.CoreSpeechKit';

let ttsEngine: textToSpeech.TextToSpeechEngine;
// Parameters for creating an engine instance.
let extraParam: Record<string, Object> = {"style": 'interaction-broadcast', "locate": 'CN', "name": 'EngineName'};
let initParamsInfo: textToSpeech.CreateEngineParams = {
  language: 'zh-CN',
  person: 0,
  online: 1,
  extraParams: extraParam
};

// Call the **createEngine** method.
textToSpeech.createEngine(initParamsInfo).then((res: textToSpeech.TextToSpeechEngine) => {
  // Obtain the engine instance.
  ttsEngine = res;
  console.info(\`Succeeded in creating engine.\`);
}).catch((err: BusinessError) =>{
  console.error(\`Failed to create engine. Code: ${err.code}, message: ${err.message}.\`);
});

@Entry
@Component
struct Page {

  build() {
    // ...
  }
}

#### textToSpeech.listVoices

listVoices(queryParams: VoiceQuery): Promise<VoiceInfo\[\]>

Queries the supported languages and timbres and returns the result asynchronously through a promise.

**System capability**: SystemCapability.AI.TextToSpeech

**Start version**: 5.1.1(19)

**Parameters**:

| 
Name

 | 

Type

 | 

Mandatory

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

queryParams

 | 

[VoiceQuery](#section235272615215)

 | 

Yes

 | 

Request parameters for querying languages and timbres.

 |

**Returns**:

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

Promise<[VoiceInfo](#section85771521101910)\[\]>

 | 

Promise that returns the query result.

 |

**Error codes**:

For details about the error codes, please refer to [ArkTS API Error Codes](../arkts-api-error-codes/document.md).

| 
Error Code

 | 

Error Message

 |
| :-- | :-- |
| 

401

 | 

Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed.

 |

**Example**:

import { BusinessError } from '@kit.BasicServicesKit';
import { textToSpeech } from '@kit.CoreSpeechKit';

// Set query parameters.
let voicesQuery: textToSpeech.VoiceQuery = {
  requestId: '123456', // **requestId** can be used only once in the same instance. Do not set it repeatedly.
  online: 1
}

@Entry
@Component
struct Page {
  build() {
    Button()
      .id('Button')
      .onClick( () => {
        // Call the **listVoices** method.
        textToSpeech.listVoices(voicesQuery).then((res: textToSpeech.VoiceInfo\[\]) => {
          // Obtain information such as the supported languages and timbres.
          console.info(\`Succeeded in listing voices, result: ${JSON.stringify(res)}.\`);
        }).catch((err: BusinessError) =>{
          console.error(\`Failed to list voices. Code: ${err.code}, message: ${err.message}.\`);
        });
      })
  }
}

#### textToSpeech.downloadVoice

downloadVoice(downloadParams: VoiceDownload, callback: AsyncCallback<DownloadResponse>): void

Downloads supported languages and timbres. This API returns the result asynchronously through a callback.

**System capability**: SystemCapability.AI.TextToSpeech

**Device behavior differences**: This API is supported on phones and tablets. On other devices, error code 1002300008 is returned when a user clicks the download button in a download dialog box.

**Start version**: 5.1.1(19)

**Parameters**:

| 
Name

 | 

Type

 | 

Mandatory

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

downloadParams

 | 

[VoiceDownload](#section10297014134719)

 | 

Yes

 | 

Parameter for requesting to download languages and timbres.

 |
| 

callback

 | 

[AsyncCallback](../../../../system/basic-functions/basic-services-kit/arkts-apis/others/ohos-base-public-callback-information/document.md#asynccallback)<[DownloadResponse](#section037913322072)\>

 | 

Yes

 | 

Callback that returns the downloaded timbre models and related information.

 |

**Error codes**:

For details about the error codes, please refer to [ArkTS API Error Codes](../arkts-api-error-codes/document.md).

| 
Error Code

 | 

Error Message

 |
| :-- | :-- |
| 

1002300008

 | 

Failed to download voice.

 |
| 

1002300009

 | 

Parameter error. Possible causes:

1\. Mandatory parameters are left unspecified.

2\. Incorrect parameter types.

3\. Parameter verification failed.

 |
| 

1002300010

 | 

Voice has already been downloaded.

 |

**Example**:

import { BusinessError, Callback, ErrorCallback } from '@kit.BasicServicesKit';
import { textToSpeech } from '@kit.CoreSpeechKit';

// Set parameters for downloading timbres.
let voicesDownload: textToSpeech.VoiceDownload = {
  requestId: '12345678-b', // Request ID, which must be unique.
  language: 'en-US',
  person: 8,
  style: 'interaction-broadcast'
};

@Entry
@Component
struct Page {
  build() {
    Button()
      .id('Button')
      .onClick(() => {
        // Call the **downloadVoice** method.
        textToSpeech.downloadVoice(voicesDownload,
          (error: BusinessError, downloadResponse: textToSpeech.DownloadResponse) => {
            if (error) {
              console.error(\`Failed to download voice. code: ${error.code}, message: ${error.message}\`);
              return;
            }
            if (!downloadResponse) {
              console.error(\`Failed to download voice. downloadResponse is null\`);
              return
            }
            let requestId: string = downloadResponse.requestId;

            // Define the function.
            let startCallback: Callback<string> = (info: string) => {
              // Callback triggered when the download starts.
              console.info(\`download voice start, requestId: ${requestId}, info:${info}}\`);
            }

            // Define the function.
            let progressCallback: Callback<string> = (schedule: string) => {
              // Callback for the download progress.
              console.info(\`download voice schedule, requestId: ${requestId} scheduleInfo: ${schedule}\`);
            }

            // Define the function.
            let completeCallback: Callback<textToSpeech.VoiceInfo> = (voiceInfo: textToSpeech.VoiceInfo) => {
              // Callback triggered when the download is complete.
              console.info(\`download voice complete, requestId: ${requestId} voiceInfo: ${JSON.stringify(voiceInfo)}\`);
              // Unregister the callback for the download start event.
              downloadResponse.off('start', startCallback);
              // Unregister the callback for the download progress event.
              downloadResponse.off('progress',progressCallback);
              // Unregister the callback for the download completion event.
              downloadResponse.off('complete',completeCallback);
              // Unregister the callback for the download cancellation event.
              downloadResponse.off('cancel',cancelCallback);
              // Unregister the callback for the download error event.
              downloadResponse.off('error',errorCallback);
            }

            // Define the function.
            let cancelCallback: Callback<string> = (cancelInfo: string) => {
              // Callback triggered when the user cancels the download.
              console.error(\`download voice cancel, requestId: ${requestId} cancelInfo: ${cancelInfo}\`);
            }

            // Define the function.
            let errorCallback: ErrorCallback<BusinessError> = (err: BusinessError) => {
              // Callback triggered when an error occurs during download.
              console.error(\`download voice error, requestId: ${requestId} errorCode: ${err.code} errorMessage: ${err.message}\`);
            }

            // Register the callback for the download start event.
            downloadResponse.on('start', startCallback);
            // Register the callback for the download progress event.
            downloadResponse.on('progress', progressCallback);
            // Register the callback for the download completion event.
            downloadResponse.on('complete', completeCallback);
            // Register the callback for the download cancellation event.
            downloadResponse.on('cancel', cancelCallback);
            // Register the callback for the download error event.
            downloadResponse.on('error', errorCallback);
          })
      })
  }
}

#### TextToSpeechEngine

Text-to-speech class, which is used to perform operations related to text-to-speech conversion. Before calling any method of **TextToSpeechEngine**, you need to call [createEngine](#section53411946183318) to create a [TextToSpeechEngine](#section185526396124) instance.

**System capability**: SystemCapability.AI.TextToSpeech

**Start version**: 4.1.0(11)

#### \[h2\]listVoices

listVoices(params: VoiceQuery, callback: AsyncCallback<Array<VoiceInfo>>): void

Queries the supported languages and timbres. This API returns the result asynchronously through a callback.

**System capability**: SystemCapability.AI.TextToSpeech

**Start version**: 4.1.0(11)

**Parameters**:

| 
Name

 | 

Type

 | 

Mandatory

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

params

 | 

[VoiceQuery](#section235272615215)

 | 

Yes

 | 

Request parameters for querying languages and timbres.

 |
| 

callback

 | 

[AsyncCallback](../../../../system/basic-functions/basic-services-kit/arkts-apis/others/ohos-base-public-callback-information/document.md#asynccallback)<Array<[VoiceInfo](#section85771521101910)\>>

 | 

Yes

 | 

Callback that receives the returned query result.

 |

**Error codes**:

For details about the error codes, please refer to [ArkTS API Error Codes](../arkts-api-error-codes/document.md).

| 
Error Code

 | 

Error Message

 |
| :-- | :-- |
| 

401

 | 

Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed.

 |

**Example**:

import { BusinessError } from '@kit.BasicServicesKit';
import { textToSpeech } from '@kit.CoreSpeechKit';

let ttsEngine: textToSpeech.TextToSpeechEngine;
// Set query parameters.
let voicesQuery: textToSpeech.VoiceQuery = {
  requestId: '123456', // **requestId** can be used only once in the same instance. Do not set it repeatedly.
  online: 1
}

@Entry
@Component
struct Page {
  build() {
    Button()
      .id('Button')
      .onClick( () => {
        // Call **listVoices**. The result will be returned through a callback.
        ttsEngine.listVoices(voicesQuery, (err: BusinessError, voiceInfo: textToSpeech.VoiceInfo\[\]) => {
          if (!err) {
            // Receive information such as the supported languages and timbres.
            console.info(\`Succeeded in listing voices, voiceInfo is ${JSON.stringify(voiceInfo)}.\`);
          } else {
            console.error(\`Failed to list voices. Code: ${err.code}, message: ${err.message}.\`);
          }
        });
      })
  }
}

#### \[h2\]listVoices

listVoices(params: VoiceQuery): Promise<Array<VoiceInfo>>

Queries the supported languages and timbres. This API returns the result asynchronously through a promise.

**System capability**: SystemCapability.AI.TextToSpeech

**Start version**: 4.1.0(11)

**Parameters**:

| 
Name

 | 

Type

 | 

Mandatory

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

params

 | 

[VoiceQuery](#section235272615215)

 | 

Yes

 | 

Request parameters for querying languages and timbres.

 |

**Returns**:

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

Promise<Array<[VoiceInfo](#section85771521101910)\>>

 | 

Promise that returns the query result.

 |

**Error codes**:

For details about the error codes, please refer to [ArkTS API Error Codes](../arkts-api-error-codes/document.md).

| 
Error Code

 | 

Error Message

 |
| :-- | :-- |
| 

401

 | 

Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed.

 |

**Example**:

import { BusinessError } from '@kit.BasicServicesKit';
import { textToSpeech } from '@kit.CoreSpeechKit';

let ttsEngine: textToSpeech.TextToSpeechEngine;
// Set query parameters.
let voicesQuery: textToSpeech.VoiceQuery = {
  requestId: '123456', // **requestId** can be used only once in the same instance. Do not set it repeatedly.
  online: 1
}

@Entry
@Component
struct Page {
  build() {
    Button()
      .id('Button')
      .onClick( () => {
        // Call the **listVoices** method.
        ttsEngine.listVoices(voicesQuery).then((res: textToSpeech.VoiceInfo\[\]) => {
          // Obtain information such as the supported languages and timbres.
          console.info(\`Succeeded in listing voices, result: ${JSON.stringify(res)}.\`);
        }).catch((err: BusinessError) =>{
          console.error(\`Failed to list voices. Code: ${err.code}, message: ${err.message}.\`);
        });
      })
  }
}

#### \[h2\]setListener

setListener(listener: SpeakListener): void

Sets the synthesis and playback callback.

**System capability**: SystemCapability.AI.TextToSpeech

**Start version**: 4.1.0(11)

**Parameters**:

| 
Name

 | 

Type

 | 

Mandatory

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

listener

 | 

[SpeakListener](#section115395631614)

 | 

Yes

 | 

Callback of events related to speech synthesis or playback.

 |

**Example**:

import { textToSpeech } from '@kit.CoreSpeechKit';

let ttsEngine: textToSpeech.TextToSpeechEngine;
// Define the callback methods for **speakListener**.
let speakListener: textToSpeech.SpeakListener = {
  // Callback triggered when playback starts.
  onStart(requestId: string, response: textToSpeech.StartResponse) {
    console.info(\`onStart, requestId: ${requestId} response: ${JSON.stringify(response)}\`);
  },
  // Callback triggered upon completion of speech synthesis or playback.
  onComplete(requestId: string, response: textToSpeech.CompleteResponse) {
    console.info(\`onComplete, requestId: ${requestId} response: ${JSON.stringify(response)}\`);
  },
  // Callback triggered when playback stops.
  onStop(requestId: string, response: textToSpeech.StopResponse) {
    console.info(\`onStop, requestId: ${requestId} response: ${JSON.stringify(response)}\`);
  },
  // Callback triggered when the audio stream is returned.
  onData(requestId: string, audio: ArrayBuffer, response: textToSpeech.SynthesisResponse) {
    console.info(\`onData, requestId: ${requestId} sequence: ${JSON.stringify(response)} audio: ${JSON.stringify(audio)}\`);
  },
  // Callback triggered when an error occurs.
  onError(requestId: string, errorCode: number, errorMessage: string) {
    console.error(\`onError, requestId: ${requestId} errorCode: ${errorCode} errorMessage: ${errorMessage}\`);
  }
};

@Entry
@Component
struct Page {
  build() {
    Button()
      .id('Button')
      .onClick( () => {
        // Set callbacks.
        ttsEngine.setListener(speakListener);
      })
  }
}

#### \[h2\]speak

speak(text: string, speakParams: SpeakParams): void

Synthesizes text to be played. Call [setListener](#section143821952181910) first. Otherwise, the speech synthesis or playback callback cannot be received.

**System capability**: SystemCapability.AI.TextToSpeech

**Start version**: 4.1.0(11)

**Parameters**:

| 
Name

 | 

Type

 | 

Mandatory

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

text

 | 

string

 | 

Yes

 | 

Text for playback. You can set the word pronunciation mode, digit playback policy, specified Chinese character pronunciation, and mute pause during playback based on the actual requirements of scenarios. For details, please refer to [Setting a Playback Policy](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/texttospeech-guide#section137481719163910).

The text contains no more than 10,000 characters.

 |
| 

speakParams

 | 

[SpeakParams](#section7843122735210)

 | 

Yes

 | 

Parameters for speech synthesis and playback.

 |

**Error codes**:

For details about the error codes, please refer to [ArkTS API Error Codes](../arkts-api-error-codes/document.md).

| 
Error Code

 | 

Error Message

 |
| :-- | :-- |
| 

401

 | 

Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed.

 |
| 

1002300001

 | 

The length of text is out of range or empty.

 |

**Example**:

import { textToSpeech } from '@kit.CoreSpeechKit';

let ttsEngine: textToSpeech.TextToSpeechEngine;
let originalText: string = "\\n\\t\\t _Text to be converted into speech_ \\n\\t\\t" +
  "_Text to be converted into speech_ \\n\\t\\t";

// Parameters for synthesis and playback.
let extraParam: Record<string, Object> = {"speed": 1, "volume": 2, "pitch": 1, "languageContext": 'zh-CN', "audioType": "pcm"}
let speakParams: textToSpeech.SpeakParams = {
  requestId: '123456', // **requestId** can be used only once in the same instance. Do not set it repeatedly.
  extraParams: extraParam
}

@Entry
@Component
struct Page {
  build() {
    Button()
      .id('Button')
      .onClick( () => {
        // Pass the text (specified by **originalText**) to call the **speak** method.
        ttsEngine.speak(originalText, speakParams);
      })
  }
}

#### \[h2\]stop

stop(): void

Stops synthesis and playback at the same time. You need to call [setListener](#section143821952181910) first. Otherwise, the callback for the stop event cannot be received.

**System capability**: SystemCapability.AI.TextToSpeech

**Start version**: 4.1.0(11)

**Example**:

import { textToSpeech } from '@kit.CoreSpeechKit';

let ttsEngine: textToSpeech.TextToSpeechEngine;
let originalText: string = "\\n\\t\\t _Text to be converted into speech_ \\n\\t\\t" +
  "_Text to be converted into speech_ \\n\\t\\t";

// Parameters for synthesis and playback.
let extraParam: Record<string, Object> = {"speed": 1, "volume": 2, "pitch": 1, "languageContext": 'zh-CN', "audioType": "pcm"}
let speakParams: textToSpeech.SpeakParams = {
  requestId: '123456', // **requestId** can be used only once in the same instance. Do not set it repeatedly.
  extraParams: extraParam
}

@Entry
@Component
struct Page {
  build() {
    Column(){
      Button()
        .id('Button')
        .onClick( () => {
          // Pass the text (specified by **originalText**) to call the **speak** API.
          ttsEngine.speak(originalText, speakParams);
        })

      Button()
        .id('Stop')
        .onClick( () => {
          // Call the **stop** API.
          ttsEngine.stop();
        })
    }
  }
}

#### \[h2\]isBusy

isBusy(): boolean

Checks whether the engine is currently synthesizing or playing. Call [setListener](#section143821952181910) first. Otherwise, the callback for errors related to **isBusy()** cannot be received.

**System capability**: SystemCapability.AI.TextToSpeech

**Start version**: 4.1.0(11)

**Returns**:

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

boolean

 | 

Indicates whether speech synthesis or playback is in progress.

-   **true**: The engine is performing speech synthesis or playback.
-   **false**: The engine is not performing speech synthesis or playback.

 |

**Example**:

import { textToSpeech } from '@kit.CoreSpeechKit';

let ttsEngine: textToSpeech.TextToSpeechEngine;
let originalText: string = "\\n\\t\\t _Text to be converted into speech_ \\n\\t\\t" +
  "_Text to be converted into speech_ \\n\\t\\t";

// Parameters for synthesis and playback.
let extraParam: Record<string, Object> = {"speed": 1, "volume": 2, "pitch": 1, "languageContext": 'zh-CN', "audioType": "pcm"}
let speakParams: textToSpeech.SpeakParams = {
  requestId: '123456', // **requestId** can be used only once in the same instance. Do not set it repeatedly.
  extraParams: extraParam
}

@Entry
@Component
struct Page {
  build() {
    Column(){
      Button()
        .id('Button')
        .onClick( () => {
          // Pass the text (specified by **originalText**) to call the **speak** method.
          ttsEngine.speak(originalText, speakParams);
        })

      Button()
        .id('isBusy')
        .onClick( () => {
          // Call the **isBusy** method.
          let isBusy = ttsEngine.isBusy();
          console.info(\`isBusy: ${isBusy}\`);
        })
    }
  }
}

#### \[h2\]shutdown

shutdown(): void

Disables the engine to free up engine resources.

**System capability**: SystemCapability.AI.TextToSpeech

**Start version**: 4.1.0(11)

**Example**:

import { textToSpeech } from '@kit.CoreSpeechKit';

let ttsEngine: textToSpeech.TextToSpeechEngine;
let originalText: string = "\\n\\t\\t _Text to be converted into speech_ \\n\\t\\t" +
  "_Text to be converted into speech_ \\n\\t\\t";

// Parameters for synthesis and playback.
let extraParam: Record<string, Object> = {"speed": 1, "volume": 2, "pitch": 1, "languageContext": 'zh-CN', "audioType": "pcm"}
let speakParams: textToSpeech.SpeakParams = {
  requestId: '123456', // **requestId** can be used only once in the same instance. Do not set it repeatedly.
  extraParams: extraParam
}

@Entry
@Component
struct Page {
  build() {
    Column(){
      Button()
        .id('Button')
        .onClick( () => {
          // Pass the text (specified by **originalText**) to call the **speak** method.
          ttsEngine.speak(originalText, speakParams);
        })

      Button()
        .id('shutdown')
        .onClick( () => {
          // Call the **shutdown** method.
          ttsEngine.shutdown();
        })
    }
  }
}

#### SpeakListener

Callback object for the synthesis and playback process. It returns status of the process, such as when the synthesis and playback process starts, when synthesis or playback is complete, and when playback stops.

**System capability**: SystemCapability.AI.TextToSpeech

**Start version**: 4.1.0(11)

#### \[h2\]onStart

onStart(requestId: string, response: StartResponse): void

Called when playback starts, to return the request ID and playback parameters, such as the channel number, sampling rate, and bit depth.

**System capability**: SystemCapability.AI.TextToSpeech

**Start version**: 4.1.0(11)

**Parameters**:

| 
Name

 | 

Type

 | 

Mandatory

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

requestId

 | 

string

 | 

Yes

 | 

Request ID. This parameter uniquely identifies a request.

The value contains only letters, digits, and Chinese characters, with no length restrictions.

 |
| 

response

 | 

[StartResponse](#section270311282525)

 | 

Yes

 | 

Playback parameters.

 |

**Example**:

import { textToSpeech } from '@kit.CoreSpeechKit';

let ttsEngine: textToSpeech.TextToSpeechEngine;
// Define the callback methods for **speakListener**.
let speakListener: textToSpeech.SpeakListener = {
  // Callback triggered when playback starts.
  onStart(requestId: string, response: textToSpeech.StartResponse) {
    console.info(\`onStart, requestId: ${requestId} response: ${JSON.stringify(response)}\`);
  },
  // Callback triggered upon completion of speech synthesis or playback.
  onComplete(requestId: string, response: textToSpeech.CompleteResponse) {
    console.info(\`onComplete, requestId: ${requestId} response: ${JSON.stringify(response)}\`);
  },
  // Callback triggered when playback stops.
  onStop(requestId: string, response: textToSpeech.StopResponse) {
    console.info(\`onStop, requestId: ${requestId} response: ${JSON.stringify(response)}\`);
  },
  // Callback triggered when the audio stream is returned.
  onData(requestId: string, audio: ArrayBuffer, response: textToSpeech.SynthesisResponse) {
    console.info(\`onData, requestId: ${requestId} sequence: ${JSON.stringify(response)} audio: ${JSON.stringify(audio)}\`);
  },
  // Callback triggered when an error occurs.
  onError(requestId: string, errorCode: number, errorMessage: string) {
    console.error(\`onError, requestId: ${requestId} errorCode: ${errorCode} errorMessage: ${errorMessage}\`);
  }
};

@Entry
@Component
struct Page {
  build() {
    Button()
      .id('Button')
      .onClick( () => {
        // Set callbacks.
        ttsEngine.setListener(speakListener);
      })
  }
}

#### \[h2\]onStop

onStop(requestId: string, response: StopResponse): void

Called when **stop()** is called, indicating that synthesis or playback has stopped.

**System capability**: SystemCapability.AI.TextToSpeech

**Start version**: 4.1.0(11)

**Parameters**:

| 
Name

 | 

Type

 | 

Mandatory

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

requestId

 | 

string

 | 

Yes

 | 

Request ID. This parameter uniquely identifies a request.

The value contains only letters, digits, and Chinese characters, with no length restrictions.

 |
| 

response

 | 

[StopResponse](#section892952965214)

 | 

Yes

 | 

Message indicating the stop result.

 |

**Example**:

import { textToSpeech } from '@kit.CoreSpeechKit';

let ttsEngine: textToSpeech.TextToSpeechEngine;
// Define the callback methods for **speakListener**.
let speakListener: textToSpeech.SpeakListener = {
  // Callback triggered when playback starts.
  onStart(requestId: string, response: textToSpeech.StartResponse) {
    console.info(\`onStart, requestId: ${requestId} response: ${JSON.stringify(response)}\`);
  },
  // Callback triggered upon completion of speech synthesis or playback.
  onComplete(requestId: string, response: textToSpeech.CompleteResponse) {
    console.info(\`onComplete, requestId: ${requestId} response: ${JSON.stringify(response)}\`);
  },
  // Callback triggered when playback stops.
  onStop(requestId: string, response: textToSpeech.StopResponse) {
    console.info(\`onStop, requestId: ${requestId} response: ${JSON.stringify(response)}\`);
  },
  // Callback triggered when the audio stream is returned.
  onData(requestId: string, audio: ArrayBuffer, response: textToSpeech.SynthesisResponse) {
    console.info(\`onData, requestId: ${requestId} sequence: ${JSON.stringify(response)} audio: ${JSON.stringify(audio)}\`);
  },
  // Callback triggered when an error occurs.
  onError(requestId: string, errorCode: number, errorMessage: string) {
    console.error(\`onError, requestId: ${requestId} errorCode: ${errorCode} errorMessage: ${errorMessage}\`);
  }
};

@Entry
@Component
struct Page {
  build() {
    Button()
      .id('Button')
      .onClick( () => {
        // Set callbacks.
        ttsEngine.setListener(speakListener);
      })
  }
}

#### \[h2\]onComplete

onComplete(requestId: string, response: CompleteResponse): void

Called when synthesis or playback is complete, to return the request ID and playback completion message.

**System capability**: SystemCapability.AI.TextToSpeech

**Start version**: 4.1.0(11)

**Parameters**:

| 
Name

 | 

Type

 | 

Mandatory

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

requestId

 | 

string

 | 

Yes

 | 

Request ID. This parameter uniquely identifies a request.

The value contains only letters, digits, and Chinese characters, with no length restrictions.

 |
| 

response

 | 

[CompleteResponse](#section26265304523)

 | 

Yes

 | 

Playback completion message.

 |

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/db/v3/4zOsb4VZTSKnr7Jcmo-pqg/caution_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062522Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=7217311B8E8B50005C88128589F8BB38C02D237DB321A624E540A5DCAEFB457E)

The result returned through the **onData** callback may be incomplete. Continue receiving the result.

**Example**:

import { textToSpeech } from '@kit.CoreSpeechKit';

let ttsEngine: textToSpeech.TextToSpeechEngine;
// Define the callback methods for **speakListener**.
let speakListener: textToSpeech.SpeakListener = {
  // Callback triggered when playback starts.
  onStart(requestId: string, response: textToSpeech.StartResponse) {
    console.info(\`onStart, requestId: ${requestId} response: ${JSON.stringify(response)}\`);
  },
  // Callback triggered upon completion of speech synthesis or playback.
  onComplete(requestId: string, response: textToSpeech.CompleteResponse) {
    console.info(\`onComplete, requestId: ${requestId} response: ${JSON.stringify(response)}\`);
  },
  // Callback triggered when playback stops.
  onStop(requestId: string, response: textToSpeech.StopResponse) {
    console.info(\`onStop, requestId: ${requestId} response: ${JSON.stringify(response)}\`);
  },
  // Callback triggered when the audio stream is returned.
  onData(requestId: string, audio: ArrayBuffer, response: textToSpeech.SynthesisResponse) {
    console.info(\`onData, requestId: ${requestId} sequence: ${JSON.stringify(response)} audio: ${JSON.stringify(audio)}\`);
  },
  // Callback triggered when an error occurs.
  onError(requestId: string, errorCode: number, errorMessage: string) {
    console.error(\`onError, requestId: ${requestId} errorCode: ${errorCode} errorMessage: ${errorMessage}\`);
  }
};

@Entry
@Component
struct Page {
  build() {
    Button()
      .id('Button')
      .onClick( () => {
        // Set callbacks.
        ttsEngine.setListener(speakListener);
      })
  }
}

#### \[h2\]onData

onData?: OnDataCallback

Called during synthesis and playback, to return the request ID, audio stream information, and additional audio information such as the format and duration. To return audio stream information, implement this API.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/03/v3/A0m7ExghSHOKAknkS3nItw/caution_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062522Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=E80307F2EEB5617D42E47DBFC67A4A449BC07AC14B3FE734DCED9D328CC60BD1)

Asynchronous inter-process communication (IPC) may lead to a minor sequencing issue in the audio stream received in the **onData** callback. The caller is required to sort the audio stream by sequence before playback.

**System capability**: SystemCapability.AI.TextToSpeech

**Start version**: 4.1.0(11)

**Parameters**:

| 
Name

 | 

Type

 | 

Mandatory

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

onData

 | 

[OnDataCallback](#section0818167184314)

 | 

No

 | 

Callback for synthesis. The audio data is returned through the **audio** parameter.

 |

**Example**:

import { textToSpeech } from '@kit.CoreSpeechKit';

let ttsEngine: textToSpeech.TextToSpeechEngine;
// Define the callback methods for **speakListener**.
let speakListener: textToSpeech.SpeakListener = {
  // Callback triggered when playback starts.
  onStart(requestId: string, response: textToSpeech.StartResponse) {
    console.info(\`onStart, requestId: ${requestId} response: ${JSON.stringify(response)}\`);
  },
  // Callback triggered upon completion of speech synthesis or playback.
  onComplete(requestId: string, response: textToSpeech.CompleteResponse) {
    console.info(\`onComplete, requestId: ${requestId} response: ${JSON.stringify(response)}\`);
  },
  // Callback triggered when playback stops.
  onStop(requestId: string, response: textToSpeech.StopResponse) {
    console.info(\`onStop, requestId: ${requestId} response: ${JSON.stringify(response)}\`);
  },
  // Callback triggered when the audio stream is returned.
  onData(requestId: string, audio: ArrayBuffer, response: textToSpeech.SynthesisResponse) {
    console.info(\`onData, requestId: ${requestId} sequence: ${JSON.stringify(response)} audio: ${JSON.stringify(audio)}\`);
  },
  // Callback triggered when an error occurs.
  onError(requestId: string, errorCode: number, errorMessage: string) {
    console.error(\`onError, requestId: ${requestId} errorCode: ${errorCode} errorMessage: ${errorMessage}\`);
  }
};

@Entry
@Component
struct Page {
  build() {
    Button()
      .id('Button')
      .onClick( () => {
        // Set callbacks.
        ttsEngine.setListener(speakListener);
      })
  }
}

#### \[h2\]onError

onError(requestId: string, errorCode: number, errorMessage: string): void

Called when an error occurs during speech synthesis and playback, to return the request ID, error code, and error message.

**System capability**: SystemCapability.AI.TextToSpeech

**Start version**: 4.1.0(11)

**Parameters**:

| 
Name

 | 

Type

 | 

Mandatory

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

requestId

 | 

string

 | 

Yes

 | 

Request ID. This parameter uniquely identifies a request.

The value contains only letters, digits, and Chinese characters, with no length restrictions.

 |
| 

errorCode

 | 

number

 | 

Yes

 | 

Returned error code.

401 Parameter Check Failed

1002300001 Invalid Text Length

1002300002 Unsupported Language

1002300003 Unsupported Timbre

1002300009 Invalid Download Parameters

For details about the error codes, please refer to [ArkTS API Error Codes](../arkts-api-error-codes/document.md).

 |
| 

errorMessage

 | 

string

 | 

Yes

 | 

Error message.

 |

**Example**:

import { textToSpeech } from '@kit.CoreSpeechKit';

let ttsEngine: textToSpeech.TextToSpeechEngine;
// Define the callback methods for **speakListener**.
let speakListener: textToSpeech.SpeakListener = {
  // Callback triggered when playback starts.
  onStart(requestId: string, response: textToSpeech.StartResponse) {
    console.info(\`onStart, requestId: ${requestId} response: ${JSON.stringify(response)}\`);
  },
  // Callback triggered upon completion of speech synthesis or playback.
  onComplete(requestId: string, response: textToSpeech.CompleteResponse) {
    console.info(\`onComplete, requestId: ${requestId} response: ${JSON.stringify(response)}\`);
  },
  // Callback triggered when playback stops.
  onStop(requestId: string, response: textToSpeech.StopResponse) {
    console.info(\`onStop, requestId: ${requestId} response: ${JSON.stringify(response)}\`);
  },
  // Callback triggered when the audio stream is returned.
  onData(requestId: string, audio: ArrayBuffer, response: textToSpeech.SynthesisResponse) {
    console.info(\`onData, requestId: ${requestId} sequence: ${JSON.stringify(response)} audio: ${JSON.stringify(audio)}\`);
  },
  // Callback triggered when an error occurs.
  onError(requestId: string, errorCode: number, errorMessage: string) {
    console.error(\`onError, requestId: ${requestId} errorCode: ${errorCode} errorMessage: ${errorMessage}\`);
  }
};

@Entry
@Component
struct Page {
  build() {
    Button()
      .id('Button')
      .onClick( () => {
        // Set callbacks.
        ttsEngine.setListener(speakListener);
      })
  }
}

#### OnDataCallback

type OnDataCallback = (requestId: string, audio: ArrayBuffer, response: SynthesisResponse) => void

Callback for synthesis. The audio data is returned through the **audio** parameter.

**System capability**: SystemCapability.AI.TextToSpeech

**Start version**: 5.1.1(19)

**Parameters**:

| 
Name

 | 

Type

 | 

Mandatory

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

requestId

 | 

string

 | 

Yes

 | 

Request ID. This parameter uniquely identifies a request.

The value contains only letters, digits, and Chinese characters, with no length restrictions.

 |
| 

audio

 | 

ArrayBuffer

 | 

Yes

 | 

Audio stream.

 |
| 

response

 | 

[SynthesisResponse](#section8985194614315)

 | 

Yes

 | 

Returned information about the audio stream.

 |

#### CreateEngineParams

Parameters for creating an engine instance, including the language, mode, timbre, and style.

**System capability**: SystemCapability.AI.TextToSpeech

**Start version**: 4.1.0(11)

| 
Name

 | 

Type

 | 

Read-Only

 | 

Optional

 | 

Description

 |
| :-- | :-- | :-- | :-- | :-- |
| 

language

 | 

string

 | 

No

 | 

No

 | 

Language. Currently, Chinese and English are supported.

**zh-CN** is recommended for Chinese. **zh\_CN** can also be used.

For the English language, **en-US** is recommended and **en\_US** can also be used.

 |
| 

online

 | 

number

 | 

No

 | 

No

 | 

Mode.

**0**: online mode, which is not supported currently; **1**: offline mode, which is supported.

 |
| 

person

 | 

number

 | 

No

 | 

No

 | 

Timbre.

For Chinese, **13** indicates Ling Xiaoshan female voice (**13** is recommended and **0** can also be used) and **21** indicates Ling Feizhe male voice (download required).

For English, **8** indicates Laura female voice for English (US) (download required).

 |
| 

extraParams

 | 

Record<string, Object>

 | 

No

 | 

Yes

 | 

-   **<'style', string>**: style.

Optional. If this parameter is not set, the default value **interaction-broadcast** will be used. Currently, only **interaction-broadcast** is supported.

**interaction-broadcast**: broadcast style.

-   **<'locate', string>**: region information.

Optional. If this parameter is not set, the default value **CN** will be used. Currently, only **CN** is supported.

**CN**: China

-   **<'name', string>**: engine name.

Optional. The value cannot be a random number. If this parameter is not set, it will be empty by default. Currently, you can create multiple instances for multiple apps. A maximum of three instances are supported for all apps on the same device.

-   **<'isBackStage', boolean>**: whether playback in the background is supported.

Optional. If this parameter is not set, playback in the background is not supported by default. If **isBackStage** is set to **true**, the TTS supports playback in the background.

 |

**Example**:

import { textToSpeech } from '@kit.CoreSpeechKit';

// Set the parameters for creating an engine.
let extraParam: Record<string, Object> = {"style": 'interaction-broadcast', "locate": 'CN', "name": 'EngineName','isBackStage': true};
let initParamsInfo: textToSpeech.CreateEngineParams = {
  language: 'zh-CN',
  person: 0,
  online: 1,
  extraParams: extraParam
};

@Entry
@Component
struct Page {

  build() {
    // ...
  }
}

#### VoiceQuery

Parameters for querying timbre and language information. For example, to query the timbre information supported by the offline mode and the Chinese language, set **online** to **1** and **language** to **zh-CN**.

**System capability**: SystemCapability.AI.TextToSpeech

**Start version**: 4.1.0(11)

| 
Name

 | 

Type

 | 

Read-Only

 | 

Optional

 | 

Description

 |
| :-- | :-- | :-- | :-- | :-- |
| 

requestId

 | 

string

 | 

No

 | 

No

 | 

Request ID. This parameter uniquely identifies a request.

The value contains only letters, digits, and Chinese characters, with no length restrictions.

 |
| 

online

 | 

number

 | 

No

 | 

No

 | 

Mode.

**0**: online mode, which is not supported currently; **1**: offline mode, which is supported.

 |
| 

extraParams

 | 

Record<string, Object>

 | 

No

 | 

Yes

 | 

-   **<'language', string>**: language to be queried.

Optional. The options are **zh-CN** (Chinese) and **en-US** (English). If this parameter is empty, the full list will be queried.

-   **<'person', number>**: timbre to be queried.

Optional. If this parameter is specified, **language** is mandatory. If this parameter is empty, the full list will be queried.

Options for Chinese:

13\. Ling Xiaoshan female voice (**13** is recommended and **0** can also be used)

21\. Ling Feizhe male voice (download required)

Options for English:

8\. Laura female voice for English (US) (download required)

 |

**Example**:

import { textToSpeech } from '@kit.CoreSpeechKit';

// Set the parameters for creating an engine.
let extraParam: Record<string, Object> = {"language": 'zh-CN', "person": 0};
let voiceQuery: textToSpeech.VoiceQuery= {
  requestId: '12345678', // **requestId** can be used only once in the same instance. Do not set it repeatedly.
  online: 1,
  extraParams: extraParam
};

@Entry
@Component
struct Page {

  build() {
    // ...
  }
}

#### VoiceDownload

Parameters for downloading timbres. All parameters are obtained through the **listVoices** API.

**System capability**: SystemCapability.AI.TextToSpeech

**Start version**: 5.1.1(19)

| 
Name

 | 

Type

 | 

Read-Only

 | 

Optional

 | 

Description

 |
| :-- | :-- | :-- | :-- | :-- |
| 

requestId

 | 

string

 | 

No

 | 

No

 | 

Request ID. This parameter uniquely identifies a request.

The value contains only letters, digits, and Chinese characters, with no length restrictions.

 |
| 

language

 | 

string

 | 

No

 | 

No

 | 

Language that supports the download. The valid range can be obtained through [listVoices (returning the result asynchronously through a callback)](#section813761871119) and [listVoices (returning the result asynchronously through a promise)](#section125219451411).

 |
| 

person

 | 

number

 | 

No

 | 

No

 | 

Timbre that can be downloaded. The valid range can be obtained through [listVoices (returning the result asynchronously through a callback)](#section813761871119) and [listVoices (returning the result asynchronously through a promise)](#section125219451411).

 |
| 

style

 | 

string

 | 

No

 | 

No

 | 

Style that supports the download. The valid range can be obtained through [listVoices (returning the result asynchronously through a callback)](#section813761871119) and [listVoices (returning the result asynchronously through a promise)](#section125219451411).

 |

**Example**:

import { textToSpeech } from '@kit.CoreSpeechKit';

// Set parameters for downloading timbres.
let voicesDownload: textToSpeech.VoiceDownload = {
  requestId: '12345678-b', // Request ID, which must be unique.
  language: 'en-US',
  person: 8,
  style: 'interaction-broadcast'
};

#### DownloadResponse

Callback object for downloading timbres and languages.

**System capability**: SystemCapability.AI.TextToSpeech

**Start version**: 5.1.1(19)

**Parameters**:

| 
Name

 | 

Type

 | 

Read-Only

 | 

Optional

 | 

Description

 |
| :-- | :-- | :-- | :-- | :-- |
| 

requestId

 | 

string

 | 

No

 | 

No

 | 

Request ID. This parameter uniquely identifies a request.

The value contains only letters, digits, and Chinese characters, with no length restrictions.

 |

#### \[h2\]on('start')

on(type: 'start', callback: Callback<string>): void

Called when a timbre starts to be downloaded. The download start information will be returned through this method.

**System capability**: SystemCapability.AI.TextToSpeech

**Start version**: 5.1.1(19)

**Parameters**:

| 
Name

 | 

Type

 | 

Mandatory

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

type

 | 

string

 | 

Yes

 | 

Fix the value to **start** to listen to the timbre download start event.

 |
| 

callback

 | 

[Callback](../../../../system/basic-functions/basic-services-kit/arkts-apis/others/ohos-base-public-callback-information/document.md#callback)<string>

 | 

Yes

 | 

Callback that receives the download start information.

 |

**Example**:

// Define the function.
let startCallback: Callback<string> = (info: string) => {
  // Callback triggered when the download starts.
  console.info(\`download voice start, info:${info}}\`);
}
// **downloadResponse** can be obtained through the [textToSpeech.downloadVoice](#section376811290229) API.
// Register the callback for the download start event.
downloadResponse.on('start', startCallback);
// Unregister the callback for the download start event.
downloadResponse.off('start', startCallback);

#### \[h2\]on('progress')

on(type: 'progress', callback: Callback<string>): void

Called during the download of a timbre. The download progress information will be returned through this method.

**System capability**: SystemCapability.AI.TextToSpeech

**Start version**: 5.1.1(19)

**Parameters**:

| 
Name

 | 

Type

 | 

Mandatory

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

type

 | 

string

 | 

Yes

 | 

Fix the value to **progress** to listen to the download progress event.

 |
| 

callback

 | 

[Callback](../../../../system/basic-functions/basic-services-kit/arkts-apis/others/ohos-base-public-callback-information/document.md#callback)<string>

 | 

Yes

 | 

Callback that receives the download progress information.

 |

**Example**:

// Define the function.
let progressCallback: Callback<string> = (schedule: string) => {
  // Callback for the download progress.
  console.info(\`download voice schedule, scheduleInfo: ${schedule}\`);
}
// **downloadResponse** can be obtained through the [textToSpeech.downloadVoice](#section376811290229) API.
// Register the callback for the download progress event.
downloadResponse.on('progress', progressCallback);
// Unregister the callback for the download progress event.
downloadResponse.off('progress',progressCallback);

#### \[h2\]on('complete')

on(type: 'complete', callback: Callback<VoiceInfo>): void

Called when a timbre is completely downloaded. The download completion information will be returned through this method.

**System capability**: SystemCapability.AI.TextToSpeech

**Start version**: 5.1.1(19)

**Parameters**:

| 
Name

 | 

Type

 | 

Mandatory

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

type

 | 

string

 | 

Yes

 | 

Fix the value to **complete** to listen to the download completion event.

 |
| 

callback

 | 

[Callback](../../../../system/basic-functions/basic-services-kit/arkts-apis/others/ohos-base-public-callback-information/document.md#callback)<[VoiceInfo](#section85771521101910)\>

 | 

Yes

 | 

Callback that receives the timbre information after the download is complete.

 |

**Example**:

import { textToSpeech } from '@kit.CoreSpeechKit';
// Define the function.
let completeCallback: Callback<textToSpeech.VoiceInfo> = (voiceInfo: textToSpeech.VoiceInfo) => {
  // Callback triggered when the download is complete.
  console.info(\`download voice complete, voiceInfo: ${JSON.stringify(voiceInfo)}\`);
}
// **downloadResponse** can be obtained through the [textToSpeech.downloadVoice](#section376811290229) API.
// Register the callback for the download completion event.
downloadResponse.on('complete', completeCallback);
// Unregister the callback for the download completion event.
downloadResponse.off('complete',completeCallback);

#### \[h2\]on('cancel')

on(type: 'cancel', callback: Callback<string>): void

Called when the user taps the close button on the progress bar to cancel the download. The download cancellation information will be returned through this method.

**System capability**: SystemCapability.AI.TextToSpeech

**Start version**: 5.1.1(19)

**Parameters**:

| 
Name

 | 

Type

 | 

Mandatory

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

type

 | 

string

 | 

Yes

 | 

Fix the value to **cancel** to listen to the timbre download cancellation event.

 |
| 

callback

 | 

[Callback](../../../../system/basic-functions/basic-services-kit/arkts-apis/others/ohos-base-public-callback-information/document.md#callback)<string>

 | 

Yes

 | 

Callback that receives the download cancellation information.

 |

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/27/v3/obQN77ykRSufyIq3YRsQgQ/caution_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062522Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=1D67E020D2F7C58A5165702347430D6F7FA1446F8C64F5245679F5F792C423A6)

Tapping the cancellation button on the download confirmation pop-up will not trigger this callback.

**Example**:

// Define the function.
let cancelCallback: Callback<string> = (cancelInfo: string) => {
  // Callback triggered when the user cancels the download.
  console.info(\`download voice cancel, cancelInfo: ${cancelInfo}\`);
}
// **downloadResponse** can be obtained through the [textToSpeech.downloadVoice](#section376811290229) API.
// Register the callback for the download cancellation event.
downloadResponse.on('cancel', cancelCallback);
// Unregister the callback for the download cancellation event.
downloadResponse.off('cancel',cancelCallback);

#### \[h2\]on('error')

on(type: 'error', callback: ErrorCallback<BusinessError>): void

Called when a timbre download error occurs. The download error information will be returned through this method.

**System capability**: SystemCapability.AI.TextToSpeech

**Start version**: 5.1.1(19)

**Parameters**:

| 
Name

 | 

Type

 | 

Mandatory

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

type

 | 

string

 | 

Yes

 | 

Fix the value to **error** to listen to the download error event.

 |
| 

callback

 | 

[ErrorCallback](../../../../system/basic-functions/basic-services-kit/arkts-apis/others/ohos-base-public-callback-information/document.md#errorcallback)<[BusinessError](../../../../system/basic-functions/basic-services-kit/arkts-apis/others/ohos-base-public-callback-information/document.md#businesserror)\>

 | 

Yes

 | 

Callback that receives the download error information.

 |

**Example**:

import { BusinessError, ErrorCallback } from '@kit.BasicServicesKit';
// Define the function.
let errorCallback: ErrorCallback<BusinessError> = (err: BusinessError) => {
  // Callback triggered when an error occurs during download.
  console.error(\`download voice error, errorCode: ${err.code} errorMessage: ${err.message}\`);
}
// **downloadResponse** can be obtained through the [textToSpeech.downloadVoice](#section376811290229) API.
// Register the callback for the download error event.
downloadResponse.on('error', errorCallback);
// Unregister the callback for the download error event.
downloadResponse.off('error',errorCallback);

#### \[h2\]off('start')

off(type: 'start', callback?: Callback<string>): void

Stops listening to the timbre download start event.

**System capability**: SystemCapability.AI.TextToSpeech

**Start version**: 5.1.1(19)

**Parameters**:

| 
Name

 | 

Type

 | 

Mandatory

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

type

 | 

string

 | 

Yes

 | 

Fix the value to **start** to stop listening to the download start event.

 |
| 

callback

 | 

[Callback](../../../../system/basic-functions/basic-services-kit/arkts-apis/others/ohos-base-public-callback-information/document.md#callback)<string>

 | 

No

 | 

Callback to be unregistered, which must be the same as that passed for listening to the event. If this parameter is not set, all callbacks will be unregistered.

 |

**Example**:

// Define the function.
let startCallback: Callback<string> = (info: string) => {
  // Callback triggered when the download starts.
  console.info(\`download voice start, info:${info}}\`);
}
// **downloadResponse** can be obtained through the [textToSpeech.downloadVoice](#section376811290229) API.
// Register the callback for the download start event.
downloadResponse.on('start', startCallback);
// Unregister the callback for the download start event.
downloadResponse.off('start', startCallback);

#### \[h2\]off('progress')

off(type: 'progress', callback?: Callback<string>): void

Stops listening to the timbre download progress event.

**System capability**: SystemCapability.AI.TextToSpeech

**Start version**: 5.1.1(19)

**Parameters**:

| 
Name

 | 

Type

 | 

Mandatory

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

type

 | 

string

 | 

Yes

 | 

Fix the value to **progress** to stop listening to the download progress event.

 |
| 

callback

 | 

[Callback](../../../../system/basic-functions/basic-services-kit/arkts-apis/others/ohos-base-public-callback-information/document.md#callback)<string>

 | 

No

 | 

Callback to be unregistered, which must be the same as that passed for listening to the event. If this parameter is not set, all callbacks will be unregistered.

 |

**Example**:

// Define the function.
let progressCallback: Callback<string> = (schedule: string) => {
  // Callback for the download progress.
  console.info(\`download voice schedule, scheduleInfo: ${schedule}\`);
}
// **downloadResponse** can be obtained through the [textToSpeech.downloadVoice](#section376811290229) API.
// Register the callback for the download progress event.
downloadResponse.on('progress', progressCallback);
// Unregister the callback for the download progress event.
downloadResponse.off('progress',progressCallback);

#### \[h2\]off('complete')

off(type: 'complete', callback?: Callback<VoiceInfo>): void

Stops listening to the timbre download completion event.

**System capability**: SystemCapability.AI.TextToSpeech

**Start version**: 5.1.1(19)

**Parameters**:

| 
Name

 | 

Type

 | 

Mandatory

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

type

 | 

string

 | 

Yes

 | 

Fix the value to **complete** to stop listening to the download completion event.

 |
| 

callback

 | 

[Callback](../../../../system/basic-functions/basic-services-kit/arkts-apis/others/ohos-base-public-callback-information/document.md#callback)<[VoiceInfo](#section85771521101910)\>

 | 

No

 | 

Callback to be unregistered, which must be the same as that passed for listening to the event. If this parameter is not set, all callbacks will be unregistered.

 |

**Example**:

import { textToSpeech } from '@kit.CoreSpeechKit';
// Define the function.
let completeCallback: Callback<textToSpeech.VoiceInfo> = (voiceInfo: textToSpeech.VoiceInfo) => {
  // Callback triggered when the download is complete.
  console.info(\`download voice complete, voiceInfo: ${JSON.stringify(voiceInfo)}\`);
}
// **downloadResponse** can be obtained through the [textToSpeech.downloadVoice](#section376811290229) API.
// Register the callback for the download completion event.
downloadResponse.on('complete', completeCallback);
// Unregister the callback for the download completion event.
downloadResponse.off('complete',completeCallback);

#### \[h2\]off('cancel')

off(type: 'cancel', callback?: Callback<string>): void

Stops listening to the timbre download cancellation event.

**System capability**: SystemCapability.AI.TextToSpeech

**Start version**: 5.1.1(19)

**Parameters**:

| 
Name

 | 

Type

 | 

Mandatory

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

type

 | 

string

 | 

Yes

 | 

Fix the value to **cancel** to stop listening to the download cancellation event.

 |
| 

callback

 | 

[Callback](../../../../system/basic-functions/basic-services-kit/arkts-apis/others/ohos-base-public-callback-information/document.md#callback)<string>

 | 

No

 | 

Callback to be unregistered, which must be the same as that passed for listening to the event. If this parameter is not set, all callbacks will be unregistered.

 |

**Example**:

// Define the function.
let cancelCallback: Callback<string> = (cancelInfo: string) => {
  // Callback triggered when the user cancels the download.
  console.info(\`download voice cancel, cancelInfo: ${cancelInfo}\`);
}
// **downloadResponse** can be obtained through the [textToSpeech.downloadVoice](#section376811290229) API.
// Register the callback for the download cancellation event.
downloadResponse.on('cancel', cancelCallback);
// Unregister the callback for the download cancellation event.
downloadResponse.off('cancel',cancelCallback);

#### \[h2\]off('error')

off(type: 'error', callback?: ErrorCallback<BusinessError>): void

Stops listening to the timbre download error event.

**System capability**: SystemCapability.AI.TextToSpeech

**Start version**: 5.1.1(19)

**Parameters**:

| 
Name

 | 

Type

 | 

Mandatory

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

type

 | 

string

 | 

Yes

 | 

Fix the value to **error** to stop listening to the download error event.

 |
| 

callback

 | 

[ErrorCallback](../../../../system/basic-functions/basic-services-kit/arkts-apis/others/ohos-base-public-callback-information/document.md#errorcallback)<[BusinessError](../../../../system/basic-functions/basic-services-kit/arkts-apis/others/ohos-base-public-callback-information/document.md#businesserror)\>

 | 

No

 | 

Callback to be unregistered, which must be the same as that passed for listening to the event. If this parameter is not set, all callbacks will be unregistered.

 |

**Example**:

import { BusinessError, ErrorCallback } from '@kit.BasicServicesKit';
// Define the function.
let errorCallback: ErrorCallback<BusinessError> = (err: BusinessError) => {
  // Callback triggered when an error occurs during download.
  console.error(\`download voice error, errorCode: ${err.code} errorMessage: ${err.message}\`);
}
// **downloadResponse** can be obtained through the [textToSpeech.downloadVoice](#section376811290229) API.
// Register the callback for the download error event.
downloadResponse.on('error', errorCallback);
// Unregister the callback for the download error event.
downloadResponse.off('error',errorCallback);

#### SpeakParams

Parameters for audio stream synthesis and playback, including the speech speed, volume, pitch, and synthesis type.

**System capability**: SystemCapability.AI.TextToSpeech

**Start version**: 4.1.0(11)

| 
Name

 | 

Type

 | 

Read-Only

 | 

Optional

 | 

Description

 |
| :-- | :-- | :-- | :-- | :-- |
| 

requestId

 | 

string

 | 

No

 | 

No

 | 

Request ID, which must be unique globally.

The value contains only letters, digits, and Chinese characters, and has no length restrictions. It is used to distinguish between different requests.

 |
| 

extraParams

 | 

Record<string, Object>

 | 

No

 | 

Yes

 | 

-   **<'speed', number>**: speech speed.

Optional. The value ranges from **0.5** to **2**. If this parameter is not passed, the default value **1** is used, indicating that the audio stream is synthesized at 1x speed.

-   **<'volume', number>**: volume.

Optional. The value ranges from **0** to **2**. If this parameter is not passed, the default value **1** is used, indicating that the audio stream is synthesized at 1x volume.

-   **<'pitch', number>**: pitch.

Optional. The value ranges from **0.5** to **2**. If this parameter is not passed, the default value **1** is used, indicating that the audio stream is synthesized at normal pitch.

-   **<'languageContext', string>**: language in which Arabic numerals are played.

Optional. Currently, only **zh-CN** (Chinese) and **en-US** (English) are supported. If this parameter is not passed, the default value **zh-CN** will be used.

-   **<'audioType', string>**: audio type.

Optional. Currently, only **pcm** is supported. If this parameter is left empty, **pcm** will be used by default, which indicates Pulse Code Modulation.

-   **<'playType', number>**: synthesis type.

Optional. If this parameter is left empty, **1** will be used by default.

**0**: Perform only speech synthesis and return the audio stream without playing the speech.

**1**: Perform speech synthesis and playback, without returning the audio stream.

-   **<'soundChannel', number>**: broadcast channel

Optional. For details about the value range, please refer to [audio stream usage](../../../../media/audio-kit/arkts-apis/ohos-multimedia-audio-audio-management/enums/document.md#streamusage) and select an appropriate audio scenario. If the value is out of the range, an exception will occur.

If this parameter is left empty, **3** will be used by default, indicating the voice assistant channel.

NOTE:

If channel 1 or 12 is used, audio truncation will occur when the device screen is off because the system enters the [low-power mode](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/power-saving-for-playback) for audio playback.

-   **<'queueMode', number>**: playback mode.

Optional. If this parameter is left empty, **0** will be used by default.

**0**: queue mode

**1**: preemption mode

 |

**Example**:

import { textToSpeech } from '@kit.CoreSpeechKit';

// Set playback parameters.
let extraParam: Record<string, Object> = {"queueMode": 0, "speed": 1, "volume": 2, "pitch": 1, "languageContext": 'zh-CN', "audioType": "pcm", "soundChannel": 3, "playType":1};
let speakParams: textToSpeech.SpeakParams = {
  requestId: '123456', // **requestId** can be used only once in the same instance. Do not set it repeatedly.
  extraParams: extraParam
}

@Entry
@Component
struct Page {

  build() {
    // ...
  }
}

#### VoiceInfo

Returned parameters related to the query result.

**System capability**: SystemCapability.AI.TextToSpeech

**Start version**: 4.1.0(11)

| 
Name

 | 

Type

 | 

Read-Only

 | 

Optional

 | 

Description

 |
| :-- | :-- | :-- | :-- | :-- |
| 

language

 | 

string

 | 

No

 | 

No

 | 

Supported languages. Currently, Chinese and English are supported.

**zh-CN** is recommended for Chinese. **zh\_CN** can also be used.

For the English language, **en-US** is recommended and **en\_US** can also be used.

 |
| 

person

 | 

number

 | 

No

 | 

No

 | 

Supported timbres.

For Chinese, **13** indicates Ling Xiaoshan female voice (**13** is recommended and **0** can also be used) and **21** indicates Ling Feizhe male voice (download required).

For English, **8** indicates Laura female voice for English (US) (download required).

 |
| 

style

 | 

string

 | 

No

 | 

No

 | 

Style.

-   **interaction-broadcast**: broadcast in Mandarin Chinese

 |
| 

gender

 | 

string

 | 

No

 | 

No

 | 

Gender.

-   **Male**: male
-   **Female**: female

 |
| 

description

 | 

string

 | 

No

 | 

No

 | 

Voice description, such as the role attributes and emotions.

 |
| 

status

 | 

string

 | 

No

 | 

Yes

 | 

Timbre model status.

-   **GA**: downloadable
-   **INSTALLED**: downloaded
-   **EOM**: unavailable

**Start version**: 5.1.1(19)

 |

#### StartResponse

Playback parameters returned.

**System capability**: SystemCapability.AI.TextToSpeech

**Start version**: 4.1.0(11)

| 
Name

 | 

Type

 | 

Read-Only

 | 

Optional

 | 

Description

 |
| :-- | :-- | :-- | :-- | :-- |
| 

audioType

 | 

string

 | 

No

 | 

No

 | 

Audio type. Currently, only **pcm** (indicating PCM, short for Pulse Code Modulation) is supported.

 |
| 

sampleRate

 | 

number

 | 

No

 | 

No

 | 

Sampling rate of the audio. Currently, only **16000** is supported.

 |
| 

sampleBit

 | 

number

 | 

No

 | 

No

 | 

Bit depth of the audio. Currently, only **16** is supported.

 |
| 

audioChannel

 | 

number

 | 

No

 | 

No

 | 

Channel number of the audio. The value depends on the input channel information.

 |
| 

compressRate

 | 

number

 | 

No

 | 

No

 | 

Compression rate of the audio. The default value is **0** for the PCM format.

 |

#### StopResponse

Parameters returned when playback has stopped.

**System capability**: SystemCapability.AI.TextToSpeech

**Start version**: 4.1.0(11)

| 
Name

 | 

Type

 | 

Read-Only

 | 

Optional

 | 

Description

 |
| :-- | :-- | :-- | :-- | :-- |
| 

type

 | 

number

 | 

No

 | 

No

 | 

Stop type.

-   **0**: Stop both the synthesis and playback.
-   **1**: Stop only the playback.

 |
| 

message

 | 

string

 | 

No

 | 

No

 | 

Message.

The value contains 0 to 30 characters.

 |

#### CompleteResponse

Parameters returned when playback is complete.

**System capability**: SystemCapability.AI.TextToSpeech

**Start version**: 4.1.0(11)

| 
Name

 | 

Type

 | 

Read-Only

 | 

Optional

 | 

Description

 |
| :-- | :-- | :-- | :-- | :-- |
| 

type

 | 

number

 | 

No

 | 

No

 | 

Indicates which process has been complete, synthesis or playback.

-   **0**: Synthesis has been complete.
-   **1**: Playback has been complete.

 |
| 

message

 | 

string

 | 

No

 | 

No

 | 

Message.

The value contains 0 to 30 characters.

 |

#### SynthesisResponse

Returned information about the audio stream.

**System capability**: SystemCapability.AI.TextToSpeech

**Start version**: 4.1.0(11)

| 
Name

 | 

Type

 | 

Read-Only

 | 

Optional

 | 

Description

 |
| :-- | :-- | :-- | :-- | :-- |
| 

sequence

 | 

number

 | 

No

 | 

No

 | 

Sequence of the returned audio data.

It starts from **0** and increments by 1 each time.

The value ranges from 0 to 100000.

 |
| 

audioType

 | 

string

 | 

No

 | 

No

 | 

Type of the returned audio. Currently, only **pcm** is supported.

 |
