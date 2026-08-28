# speechRecognizer (Speech Recognition)

This module converts speech into text so that users can interact with their devices in real time through speech.

Currently, this service is available only in Chinese and supports only the offline model.

**Start version**: 4.1.0(11)

#### Module Import

import { speechRecognizer } from '@kit.CoreSpeechKit';

#### speechRecognizer.createEngine

createEngine(createEngineParams: CreateEngineParams, callback: AsyncCallback<SpeechRecognitionEngine>): void

Creates a **SpeechRecognitionEngine** instance and initializes the engine. This API returns the result asynchronously through a callback.

**System capability**: SystemCapability.AI.SpeechRecognizer

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

[AsyncCallback](../../../../system/basic-functions/basic-services-kit/arkts-apis/others/ohos-base-public-callback-information/document.md#asynccallback)<[SpeechRecognitionEngine](#section153101728203110)\>

 | 

Yes

 | 

Callback that returns the engine instance created.

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

1002200001

 | 

Create engine failed.

 |
| 

1002200006

 | 

The engine of SpeechRecognition is busy.

 |
| 

1002200008

 | 

The engine of SpeechRecognition is being destroyed.

 |
| 

1002200009

 | 

Internal Service Error.

 |

**Example**:

import { BusinessError } from '@kit.BasicServicesKit';
import { speechRecognizer } from '@kit.CoreSpeechKit';

let asrEngine: speechRecognizer.SpeechRecognitionEngine | undefined = undefined;

// Set the parameters for creating an engine.
let extraParams: Record<string, Object> = { "locate": "CN", "recognizerMode": "short" }
let initParamsInfo: speechRecognizer.CreateEngineParams = {
  language: 'zh-CN',
  online: 1,
  extraParams: extraParams
};

// Call the **createEngine** method.
speechRecognizer.createEngine(initParamsInfo, (err: BusinessError, speechRecognitionEngine: 
speechRecognizer.SpeechRecognitionEngine) => {
  if (!err) {
    // Receive the engine instance created.
    asrEngine = speechRecognitionEngine;
  } else {
      // Error code 1002200001: Engine creation failed due to reasons like unsupported language or mode, initialization timeout, or non-existent resources.
      // Error code 1002200006: The engine is busy, usually triggered when multiple apps are calling the speech recognition engine simultaneously.
      // Error code 1002200008 will be returned when the engine cannot be created. Cause: The engine has been destroyed.
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

#### speechRecognizer.createEngine

createEngine(createEngineParams: CreateEngineParams): Promise<SpeechRecognitionEngine>

Creates a **SpeechRecognitionEngine** instance and initializes the engine. This API returns the result asynchronously through a promise.

**System capability**: SystemCapability.AI.SpeechRecognizer

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

Promise<[SpeechRecognitionEngine](#section153101728203110)\>

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

1002200001

 | 

Create engine failed.

 |
| 

1002200006

 | 

The engine of SpeechRecognition is busy.

 |
| 

1002200008

 | 

The engine of SpeechRecognition is being destroyed.

 |
| 

1002200009

 | 

Internal Service Error.

 |

**Example**:

import { BusinessError } from '@kit.BasicServicesKit';
import { speechRecognizer } from '@kit.CoreSpeechKit';

let asrEngine: speechRecognizer.SpeechRecognitionEngine | undefined = undefined;

// Set the parameters for creating an engine.
let extraParams: Record<string, Object> = { "locate": "CN", "recognizerMode": "short" }
let initParamsInfo: speechRecognizer.CreateEngineParams = {
  language: 'zh-CN',
  online: 1,
  extraParams: extraParams
};

// Call the **createEngine** method.
speechRecognizer.createEngine(initParamsInfo).then((speechRecognitionEngine: speechRecognizer.SpeechRecognitionEngine) => {
  // Receive the engine instance.
  asrEngine = speechRecognitionEngine;
  console.info(\`Succeeded in creating engine.\`);
}).catch((err: BusinessError) => {
  console.error(\`Failed to create engine. Code: ${err.code}, message: ${err.message}.\`);
});

@Entry
@Component
struct Page {

  build() {
    // ...
  }
}

#### SpeechRecognitionEngine

Speech recognition class, which is used to perform operations related to speech recognition. Before calling any API of **SpeechRecognitionEngine**, you need to call [createEngine](#section53411946183318) to create a [SpeechRecognitionEngine](#section153101728203110) instance.

**System capability**: SystemCapability.AI.SpeechRecognizer

**Start version**: 4.1.0(11)

#### \[h2\]listLanguages

listLanguages(params: LanguageQuery, callback: AsyncCallback<Array<string>>): void

Queries the supported languages and returns the result asynchronously through a callback.

**System capability**: SystemCapability.AI.SpeechRecognizer

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

[LanguageQuery](#section235272615215)

 | 

Yes

 | 

Request parameters for querying languages.

 |
| 

callback

 | 

[AsyncCallback](../../../../system/basic-functions/basic-services-kit/arkts-apis/others/ohos-base-public-callback-information/document.md#asynccallback)<Array<string>>

 | 

Yes

 | 

Callback that returns the query result.

Currently, only Chinese is supported. The returned result is **\["zh-CN"\]**.

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

The parameter check failed.

 |
| 

1002200007

 | 

The engine is not initialized.

 |
| 

1002200009

 | 

Internal Service Error.

 |

**Example**:

import { BusinessError } from '@kit.BasicServicesKit';
import { speechRecognizer } from '@kit.CoreSpeechKit';

let asrEngine: speechRecognizer.SpeechRecognitionEngine | undefined = undefined;

@Entry
@Component
struct Page {
  // Query languages. The result will be returned through a callback.
  private queryLanguagesCallback() {
    // Set query parameters.
    let languageQuery: speechRecognizer.LanguageQuery = {
      sessionId: '123456'
    };
    // Call the **listLanguages** method.
    asrEngine?.listLanguages(languageQuery, (err: BusinessError, languages: Array<string>) => {
      if (!err) {
        // Receive information about the supported languages.
        console.info(\`Succeeded in listing languages, result: ${JSON.stringify(languages)}.\`);
      } else {
        console.error(\`Failed to list languages. Code: ${err.code}, message: ${err.message}.\`);
      }
    });
  }

  build() {
    // ...
  }
}

#### \[h2\]listLanguages

listLanguages(params: LanguageQuery): Promise<Array<string>>

Queries the supported languages and returns the result asynchronously through a promise.

**System capability**: SystemCapability.AI.SpeechRecognizer

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

[LanguageQuery](#section235272615215)

 | 

Yes

 | 

Request parameters for querying languages.

 |

**Returns**:

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

Promise<Array<string>>

 | 

Promise that returns the query result.

Currently, only Chinese is supported. The returned result is **\["zh-CN"\]**.

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

The parameter check failed.

 |
| 

1002200007

 | 

The engine is not initialized.

 |
| 

1002200009

 | 

Internal Service Error.

 |

**Example**:

import { BusinessError } from '@kit.BasicServicesKit';
import { speechRecognizer } from '@kit.CoreSpeechKit';

let asrEngine: speechRecognizer.SpeechRecognitionEngine | undefined = undefined;
// Set query parameters.
let languageQuery: speechRecognizer.LanguageQuery = {
  sessionId: '123456'
};

@Entry
@Component
struct Page {
  build() {
    Button()
      .id('Button')
      .fontSize(20)
      .onClick( () => {
        // Call the **listLanguages** method to query the languages supported by the engine. The result is returned through a promise.
        asrEngine?.listLanguages(languageQuery).then((res: Array<string>) => {
          console.info(\`Succeeded in listing languages, result: ${JSON.stringify(res)}.\`);
        }).catch((err: BusinessError) => {
          console.error(\`Failed to list languages. Code: ${err.code}, message: ${err.message}.\`);
        });
      })
  }
}

#### \[h2\]setListener

setListener(listener: RecognitionListener): void

Sets the speech recognition callback.

**System capability**: SystemCapability.AI.SpeechRecognizer

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

[RecognitionListener](#section845815011389)

 | 

Yes

 | 

Callback object. All callback information during recognition is returned through this object.

 |

**Example**:

import { speechRecognizer } from '@kit.CoreSpeechKit';

let asrEngine: speechRecognizer.SpeechRecognitionEngine | undefined = undefined;
// Create a callback object.
let setListener: speechRecognizer.RecognitionListener = {
  // Callback triggered when recognition successfully starts.
  onStart(sessionId: string, eventMessage: string) {
    console.info(\`onStart, sessionId: ${sessionId} eventMessage: ${eventMessage}\`);
  },
  // Callback triggered when an event occurs.
  onEvent(sessionId: string, eventCode: number, eventMessage: string) {
    console.info(\`onEvent, sessionId: ${sessionId} eventCode: ${eventCode} eventMessage: ${eventMessage}\`);
  },
  // Callback triggered when the recognition result is generated, including the intermediate result and final result.
  onResult(sessionId: string, result: speechRecognizer.SpeechRecognitionResult) {
    console.info(\`onResult, sessionId: ${sessionId} sessionId: ${JSON.stringify(result)}\`);
  },
  // Callback triggered when recognition is complete.
  onComplete(sessionId: string, eventMessage: string) {
    console.info(\`onComplete, sessionId: ${sessionId} eventMessage: ${eventMessage}\`);
  },
  // Callback triggered when an error occurs. The error code is returned through this method.
  // Error code 1002200002: Failed to start recognition. This error is triggered if the **startListening** method is repeatedly called.
  onError(sessionId: string, errorCode: number, errorMessage: string) {
    console.error(\`onError, sessionId: ${sessionId} errorCode: ${errorCode} errorMessage: ${errorMessage}\`);
  },
}

@Entry
@Component
struct Page {
  build() {
    Button()
      .id('Button')
      .onClick( () => {
        // Set callbacks.
        asrEngine?.setListener(setListener);
      })
  }
}

#### \[h2\]startListening

startListening(params: StartParams): void

Starts speech recognition.

**System capability**: SystemCapability.AI.SpeechRecognizer

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

[StartParams](#section7843122735210)

 | 

Yes

 | 

Parameters for starting speech recognition, including the session ID and audio configuration.

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

The parameter check failed.

 |
| 

1002200002

 | 

Start listening failed.

 |
| 

1002200007

 | 

The engine is not initialized.

 |

**Example**:

import { speechRecognizer } from '@kit.CoreSpeechKit';

let asrEngine: speechRecognizer.SpeechRecognitionEngine | undefined = undefined;
// Set parameters for starting recognition.
let recognizerParams: speechRecognizer.StartParams = {
  sessionId: '123456',
  audioInfo: { audioType: 'pcm', sampleRate: 16000, soundChannel: 1, sampleBit: 16 }
}

@Entry
@Component
struct Page {
  build() {
    Button()
      .id('Button')
      .onClick( () => {
        // Call the method for starting recognition.
        asrEngine?.startListening(recognizerParams);
      })
  }
}

#### \[h2\]writeAudio

writeAudio(sessionId: string, audio: Uint8Array): void

Writes audio streams. The maximum audio length is 60,000 ms. To ensure that the recognition result can be received, call [setListener](#section1745872517348) and [startListening](#section140216144119) first.

**System capability**: SystemCapability.AI.SpeechRecognizer

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

sessionId

 | 

string

 | 

Yes

 | 

Session ID.

The value contains only letters, digits, underscores (\_), and hyphens (-).

It is used to distinguish between different sessions and has no length restrictions.

 |
| 

audio

 | 

Uint8Array

 | 

Yes

 | 

Audio data to be recognized. Currently, the audio length can only be 640 bytes or 1280 bytes. The interval for sending each request must be 20 ms (when the length of the audio to be transmitted is 640 bytes) or 40 ms (when the length of the audio to be transmitted is 1280 bytes).

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

The parameter check failed.

 |
| 

1002200003

 | 

Exceeded the maximum audio length supported.

 |
| 

1002200007

 | 

The engine is not initialized.

 |
| 

1002200010

 | 

Write audio failed because the start listening is failed.

 |

**Example**:

import { speechRecognizer } from '@kit.CoreSpeechKit';

let asrEngine: speechRecognizer.SpeechRecognitionEngine | undefined = undefined;
let sessionId: string = '123456';
let uint8Array: Uint8Array = new Uint8Array();
// Audio streams can be obtained in either of the following ways: 1. Obtain audio streams through recording. 2. Read audio streams from audio files.
// 2. For details about how to read audio streams from audio files, please refer to the [demo](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/speechrecognizer-guide#section56481271497).

@Entry
@Component
struct Page {
  build() {
    Button()
      .id('Button')
      .onClick( () => {
        // Write an audio stream. The audio stream length can only be 640 bytes or 1280 bytes.
        asrEngine?.writeAudio(sessionId, uint8Array);
      })
  }
}

#### \[h2\]finish

finish(sessionId: string): void

Ends recognition. To ensure that the callback can be triggered upon an event, call [setListener](#section1745872517348) first.

**System capability**: SystemCapability.AI.SpeechRecognizer

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

sessionId

 | 

string

 | 

Yes

 | 

Session ID.

The value contains only letters, digits, underscores (\_), and hyphens (-).

It is used to distinguish between different sessions and has no length restrictions.

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

The parameter check failed.

 |
| 

1002200004

 | 

Finish recognition failed.

 |
| 

1002200007

 | 

The engine is not initialized.

 |

**Example**:

import { speechRecognizer } from '@kit.CoreSpeechKit';

let asrEngine: speechRecognizer.SpeechRecognitionEngine | undefined = undefined;
let sessionId: string = '123456';
let uint8Array: Uint8Array = new Uint8Array();
// Audio streams can be obtained in either of the following ways: 1. Obtain audio streams through recording. 2. Read audio streams from audio files.
// 2. For details about how to read audio streams from audio files, please refer to the [demo](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/speechrecognizer-guide#section56481271497).

@Entry
@Component
struct Page {
  build() {
    Column(){
      Button()
        .id('Button')
        .onClick( () => {
          // Write an audio stream. The audio stream length can only be 640 bytes or 1280 bytes.
          asrEngine?.writeAudio(sessionId, uint8Array);
        })

      Button() {
        Text("finish")
          .fontColor(Color.White)
          .fontSize(20)
      }
      .type(ButtonType.Capsule)
      .backgroundColor("#0x317AE7")
      .width("80%")
      .height(50)
      .margin(10)
      .onClick(() => {
        // End recognition.
        asrEngine?.finish(sessionId);
      })
    }
  }
}

#### \[h2\]cancel

cancel(sessionId: string): void

Cancels recognition. To ensure that the callback can be triggered upon an event, call [setListener](#section1745872517348) first.

**System capability**: SystemCapability.AI.SpeechRecognizer

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

sessionId

 | 

string

 | 

Yes

 | 

Session ID.

The value contains only letters, digits, underscores (\_), and hyphens (-).

It is used to distinguish between different sessions and has no length restrictions.

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

The parameter check failed.

 |
| 

1002200005

 | 

Cancel recognition failed.

 |
| 

1002200007

 | 

The engine is not initialized.

 |

**Example**:

import { speechRecognizer } from '@kit.CoreSpeechKit';

let asrEngine: speechRecognizer.SpeechRecognitionEngine | undefined = undefined;
let sessionId: string = '123456';
let uint8Array: Uint8Array = new Uint8Array();
// Audio streams can be obtained in either of the following ways: 1. Obtain audio streams through recording. 2. Read audio streams from audio files.
// 2. For details about how to read audio streams from audio files, please refer to the [demo](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/speechrecognizer-guide#section56481271497).

@Entry
@Component
struct Page {
  build() {
    Column(){
      Button()
        .id('Button')
        .onClick( () => {
          // Write an audio stream. The audio stream length can only be 640 bytes or 1280 bytes.
          asrEngine?.writeAudio(sessionId, uint8Array);
        })

      Button() {
        Text("cancel")
          .fontColor(Color.White)
          .fontSize(20)
      }
      .type(ButtonType.Capsule)
      .backgroundColor("#0x317AE7")
      .width("80%")
      .height(50)
      .margin(10)
      .onClick(() => {
        // Call the **cancel** method.
        asrEngine?.cancel('123456');
      })
    }
  }
}

#### \[h2\]isBusy

isBusy(): boolean

Checks whether the engine is busy.

**System capability**: SystemCapability.AI.SpeechRecognizer

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

Indicates whether the service is busy.

-   **true**: yes
-   **false**: no

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

1002200007

 | 

The engine is not initialized.

 |

**Example**:

import { speechRecognizer } from '@kit.CoreSpeechKit';

let asrEngine: speechRecognizer.SpeechRecognitionEngine | undefined = undefined;
let sessionId: string = '123456';
let uint8Array: Uint8Array = new Uint8Array();
// Audio streams can be obtained in either of the following ways: 1. Obtain audio streams through recording. 2. Read audio streams from audio files.
// 2. For details about how to read audio streams from audio files, please refer to the [demo](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/speechrecognizer-guide#section56481271497).

@Entry
@Component
struct Page {
  build() {
    Column() {
      Button()
        .id('Button')
        .onClick(() => {
          // Write an audio stream. The audio stream length can only be 640 bytes or 1280 bytes.
          asrEngine?.writeAudio(sessionId, uint8Array);
        })

      Button() {
        Text("cancel")
          .fontColor(Color.White)
          .fontSize(20)
      }
      .type(ButtonType.Capsule)
      .backgroundColor("#0x317AE7")
      .width("80%")
      .height(50)
      .margin(10)
      .onClick(() => {
        // Call the **isBusy** method.
        let isBusy = asrEngine?.isBusy();
        console.info(\`isBusy: ${isBusy}\`);
      })
    }
  }
}

#### \[h2\]shutdown

shutdown(): void

Disables the engine to free up engine resources.

**System capability**: SystemCapability.AI.SpeechRecognizer

**Start version**: 4.1.0(11)

**Example**:

import { speechRecognizer } from '@kit.CoreSpeechKit';

let asrEngine: speechRecognizer.SpeechRecognitionEngine | undefined = undefined;
let sessionId: string = '123456';
let uint8Array: Uint8Array = new Uint8Array();
// Audio streams can be obtained in either of the following ways: 1. Obtain audio streams through recording. 2. Read audio streams from audio files.
// 2. For details about how to read audio streams from audio files, please refer to the [demo](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/speechrecognizer-guide#section56481271497).

@Entry
@Component
struct Page {
  build() {
    Column() {
      Button()
        .id('Button')
        .onClick(() => {
          // Write an audio stream. The audio stream length can only be 640 bytes or 1280 bytes.
          asrEngine?.writeAudio(sessionId, uint8Array);
        })

      Button() {
        Text("cancel")
          .fontColor(Color.White)
          .fontSize(20)
      }
      .type(ButtonType.Capsule)
      .backgroundColor("#0x317AE7")
      .width("80%")
      .height(50)
      .margin(10)
      .onClick(() => {
        // Call the **shutdown** method.
        asrEngine?.shutdown();
      })
    }
  }
}

#### RecognitionListener

Speech recognition callback object, which returns the status of the recognition process, such as the initiation and completion of recognition, and the beginning or end of the speech-to-text process.

**System capability**: SystemCapability.AI.SpeechRecognizer

**Start version**: 4.1.0(11)

#### \[h2\]onStart

onStart(sessionId: string, eventMessage: string): void

Called when recognition starts.

**System capability**: SystemCapability.AI.SpeechRecognizer

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

sessionId

 | 

string

 | 

Yes

 | 

Session ID.

The value contains only letters, digits, underscores (\_), and hyphens (-).

It is used to distinguish between different sessions and has no length restrictions.

 |
| 

eventMessage

 | 

string

 | 

Yes

 | 

Message when recognition starts.

The return value is a sentence that indicates the result of starting recognition. If recognition successfully starts, "startListening success" will be returned.

 |

**Example**:

import { speechRecognizer } from '@kit.CoreSpeechKit';

let asrEngine: speechRecognizer.SpeechRecognitionEngine | undefined = undefined;
// Create a callback object.
let setListener: speechRecognizer.RecognitionListener = {
  // Callback triggered when recognition successfully starts.
  onStart(sessionId: string, eventMessage: string) {
    console.info(\`onStart, sessionId: ${sessionId} eventMessage: ${eventMessage}\`);
  },
  // Callback triggered when an event occurs.
  onEvent(sessionId: string, eventCode: number, eventMessage: string) {
    console.info(\`onEvent, sessionId: ${sessionId} eventCode: ${eventCode} eventMessage: ${eventMessage}\`);
  },
  // Callback triggered when the recognition result is generated, including the intermediate result and final result.
  onResult(sessionId: string, result: speechRecognizer.SpeechRecognitionResult) {
    console.info(\`onResult, sessionId: ${sessionId} sessionId: ${JSON.stringify(result)}\`);
  },
  // Callback triggered when recognition is complete.
  onComplete(sessionId: string, eventMessage: string) {
    console.info(\`onComplete, sessionId: ${sessionId} eventMessage: ${eventMessage}\`);
  },
  // Callback triggered when an error occurs. The error code is returned through this method.
  // Error code 1002200002: Failed to start recognition. This error is triggered if the **startListening** method is repeatedly called.
  onError(sessionId: string, errorCode: number, errorMessage: string) {
    console.error(\`onError, sessionId: ${sessionId} errorCode: ${errorCode} errorMessage: ${errorMessage}\`);
  },
}

@Entry
@Component
struct Page {
  build() {
    Button()
      .id('Button')
      .onClick( () => {
        // Set callbacks.
        asrEngine?.setListener(setListener);
      })
  }
}

#### \[h2\]onEvent

onEvent(sessionId: string, eventCode: number, eventMessage: string): void

Called when an event occurs during recognition, for example, the beginning or end of the speech-to-text process. This method will be triggered when **vadBegin** or **vadEnd** occurs.

**System capability**: SystemCapability.AI.SpeechRecognizer

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

sessionId

 | 

string

 | 

Yes

 | 

Session ID.

The value contains only letters, digits, underscores (\_), and hyphens (-).

It is used to distinguish between different sessions and has no length restrictions.

 |
| 

eventCode

 | 

number

 | 

Yes

 | 

Event code.

-   **1**: The speech-to-text process starts.
-   **3**: The speech-to-text process ends.

 |
| 

eventMessage

 | 

string

 | 

Yes

 | 

Event message.

The return value is a sentence that describes an event in the recognition process.

-   **speech started.**: The speech-to-text process starts.
-   **speech stopped.**: The speech-to-text process ends.

 |

**Example**:

import { speechRecognizer } from '@kit.CoreSpeechKit';

let asrEngine: speechRecognizer.SpeechRecognitionEngine | undefined = undefined;
// Create a callback object.
let setListener: speechRecognizer.RecognitionListener = {
  // Callback triggered when recognition successfully starts.
  onStart(sessionId: string, eventMessage: string) {
    console.info(\`onStart, sessionId: ${sessionId} eventMessage: ${eventMessage}\`);
  },
  // Callback triggered when an event occurs.
  onEvent(sessionId: string, eventCode: number, eventMessage: string) {
    console.info(\`onEvent, sessionId: ${sessionId} eventCode: ${eventCode} eventMessage: ${eventMessage}\`);
  },
  // Callback triggered when the recognition result is generated, including the intermediate result and final result.
  onResult(sessionId: string, result: speechRecognizer.SpeechRecognitionResult) {
    console.info(\`onResult, sessionId: ${sessionId} sessionId: ${JSON.stringify(result)}\`);
  },
  // Callback triggered when recognition is complete.
  onComplete(sessionId: string, eventMessage: string) {
    console.info(\`onComplete, sessionId: ${sessionId} eventMessage: ${eventMessage}\`);
  },
  // Callback triggered when an error occurs. The error code is returned through this method.
  // Error code 1002200002: Failed to start recognition. This error is triggered if the **startListening** method is repeatedly called.
  onError(sessionId: string, errorCode: number, errorMessage: string) {
    console.error(\`onError, sessionId: ${sessionId} errorCode: ${errorCode} errorMessage: ${errorMessage}\`);
  },
}

@Entry
@Component
struct Page {
  build() {
    Button()
      .id('Button')
      .onClick( () => {
        // Set callbacks.
        asrEngine?.setListener(setListener);
      })
  }
}

#### \[h2\]onResult

onResult(sessionId: string, result: SpeechRecognitionResult): void

Called to return the intermediate result and final result of recognition.

**System capability**: SystemCapability.AI.SpeechRecognizer

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

sessionId

 | 

string

 | 

Yes

 | 

Session ID.

The value contains only letters, digits, underscores (\_), and hyphens (-).

It is used to distinguish between different sessions and has no length restrictions.

 |
| 

result

 | 

[SpeechRecognitionResult](#section270311282525)

 | 

Yes

 | 

Recognition result.

 |

**Example**:

import { speechRecognizer } from '@kit.CoreSpeechKit';

let asrEngine: speechRecognizer.SpeechRecognitionEngine | undefined = undefined;
// Create a callback object.
let setListener: speechRecognizer.RecognitionListener = {
  // Callback triggered when recognition successfully starts.
  onStart(sessionId: string, eventMessage: string) {
    console.info(\`onStart, sessionId: ${sessionId} eventMessage: ${eventMessage}\`);
  },
  // Callback triggered when an event occurs.
  onEvent(sessionId: string, eventCode: number, eventMessage: string) {
    console.info(\`onEvent, sessionId: ${sessionId} eventCode: ${eventCode} eventMessage: ${eventMessage}\`);
  },
  // Callback triggered when the recognition result is generated, including the intermediate result and final result.
  onResult(sessionId: string, result: speechRecognizer.SpeechRecognitionResult) {
    console.info(\`onResult, sessionId: ${sessionId} sessionId: ${JSON.stringify(result)}\`);
  },
  // Callback triggered when recognition is complete.
  onComplete(sessionId: string, eventMessage: string) {
    console.info(\`onComplete, sessionId: ${sessionId} eventMessage: ${eventMessage}\`);
  },
  // Callback triggered when an error occurs. The error code is returned through this method.
  // Error code 1002200002: Failed to start recognition. This error is triggered if the **startListening** method is repeatedly called.
  onError(sessionId: string, errorCode: number, errorMessage: string) {
    console.error(\`onError, sessionId: ${sessionId} errorCode: ${errorCode} errorMessage: ${errorMessage}\`);
  },
}

@Entry
@Component
struct Page {
  build() {
    Button()
      .id('Button')
      .onClick( () => {
        // Set callbacks.
        asrEngine?.setListener(setListener);
      })
  }
}

#### \[h2\]onComplete

onComplete(sessionId: string, eventMessage: string): void

Called when recognition has been complete or the [finish](#section14433919171116) method is called to end recognition, to return the session ID and recognition completion message.

**System capability**: SystemCapability.AI.SpeechRecognizer

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

sessionId

 | 

string

 | 

Yes

 | 

Session ID.

The value contains only letters, digits, underscores (\_), and hyphens (-).

It is used to distinguish between different sessions and has no length restrictions.

 |
| 

eventMessage

 | 

string

 | 

Yes

 | 

Recognition completion message.

The return value is a sentence that indicates the status when the recognition is complete, for example, "recognize complete".

 |

**Example**:

import { speechRecognizer } from '@kit.CoreSpeechKit';

let asrEngine: speechRecognizer.SpeechRecognitionEngine | undefined = undefined;
// Create a callback object.
let setListener: speechRecognizer.RecognitionListener = {
  // Callback triggered when recognition successfully starts.
  onStart(sessionId: string, eventMessage: string) {
    console.info(\`onStart, sessionId: ${sessionId} eventMessage: ${eventMessage}\`);
  },
  // Callback triggered when an event occurs.
  onEvent(sessionId: string, eventCode: number, eventMessage: string) {
    console.info(\`onEvent, sessionId: ${sessionId} eventCode: ${eventCode} eventMessage: ${eventMessage}\`);
  },
  // Callback triggered when the recognition result is generated, including the intermediate result and final result.
  onResult(sessionId: string, result: speechRecognizer.SpeechRecognitionResult) {
    console.info(\`onResult, sessionId: ${sessionId} sessionId: ${JSON.stringify(result)}\`);
  },
  // Callback triggered when recognition is complete.
  onComplete(sessionId: string, eventMessage: string) {
    console.info(\`onComplete, sessionId: ${sessionId} eventMessage: ${eventMessage}\`);
  },
  // Callback triggered when an error occurs. The error code is returned through this method.
  // Error code 1002200002: Failed to start recognition. This error is triggered if the **startListening** method is repeatedly called.
  onError(sessionId: string, errorCode: number, errorMessage: string) {
    console.error(\`onError, sessionId: ${sessionId} errorCode: ${errorCode} errorMessage: ${errorMessage}\`);
  },
}

@Entry
@Component
struct Page {
  build() {
    Button()
      .id('Button')
      .onClick( () => {
        // Set callbacks.
        asrEngine?.setListener(setListener);
      })
  }
}

#### \[h2\]onError

onError(sessionId: string, errorCode: number, errorMessage: string): void

Called when an error occurs during recognition, to return the session ID, error code, and error message.

**System capability**: SystemCapability.AI.SpeechRecognizer

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

sessionId

 | 

string

 | 

Yes

 | 

Session ID.

The value contains only letters, digits, underscores (\_), and hyphens (-).

It is used to distinguish between different sessions and has no length restrictions.

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

1002200002 Failed to Start Recognition

1002200003 Audio Too Long

1002200004 Failed to End Recognition

1002200005 Failed to Cancel Recognition

1002200006 Service Busy

1002200007 Engine Not Initialized

1002200010 Speech Recognition Not Started

1002200011 Speech Recognition Exception

1002200012 No Microphone Permission

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

import { speechRecognizer } from '@kit.CoreSpeechKit';

let asrEngine: speechRecognizer.SpeechRecognitionEngine | undefined = undefined;
// Create a callback object.
let setListener: speechRecognizer.RecognitionListener = {
  // Callback triggered when recognition successfully starts.
  onStart(sessionId: string, eventMessage: string) {
    console.info(\`onStart, sessionId: ${sessionId} eventMessage: ${eventMessage}\`);
  },
  // Callback triggered when an event occurs.
  onEvent(sessionId: string, eventCode: number, eventMessage: string) {
    console.info(\`onEvent, sessionId: ${sessionId} eventCode: ${eventCode} eventMessage: ${eventMessage}\`);
  },
  // Callback triggered when the recognition result is generated, including the intermediate result and final result.
  onResult(sessionId: string, result: speechRecognizer.SpeechRecognitionResult) {
    console.info(\`onResult, sessionId: ${sessionId} sessionId: ${JSON.stringify(result)}\`);
  },
  // Callback triggered when recognition is complete.
  onComplete(sessionId: string, eventMessage: string) {
    console.info(\`onComplete, sessionId: ${sessionId} eventMessage: ${eventMessage}\`);
  },
  // Callback triggered when an error occurs. The error code is returned through this method.
  // Error code 1002200002: Failed to start recognition. This error is triggered if the **startListening** method is repeatedly called.
  onError(sessionId: string, errorCode: number, errorMessage: string) {
    console.error(\`onError, sessionId: ${sessionId} errorCode: ${errorCode} errorMessage: ${errorMessage}\`);
  },
}

@Entry
@Component
struct Page {
  build() {
    Button()
      .id('Button')
      .onClick( () => {
        // Set callbacks.
        asrEngine?.setListener(setListener);
      })
  }
}

#### CreateEngineParams

Parameters for creating an engine instance, including the language, mode, and region.

**System capability**: SystemCapability.AI.SpeechRecognizer

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

Language. Currently, only **zh-CN** is supported.

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

**1**: offline. Currently, only the offline mode is supported.

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

-   **<'locate', string>**: region information.

Optional. If this parameter is not set, the default value **CN** will be used. Currently, only **CN** is supported.

-   **<'recognizerMode', Object>**: speech mode.

Optional. If this parameter is not set, the default value **short** will be used. Currently, **short** and **long** are supported.

-   **<'sysGeneralLexicon, string\[\]>**: system hotwords. You can configure hotwords to improve the recognition rate. The configured hotwords are valid for the entire recognition process.

Optional. This parameter is empty by default when it is not set. You can configure up to 200 hotwords, each of which contains 2 to 20 characters.

 |

#### LanguageQuery

Parameters for querying languages. For example, to query the languages supported by the service in offline mode, set **online** to **1**.

**System capability**: SystemCapability.AI.SpeechRecognizer

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

sessionId

 | 

string

 | 

No

 | 

No

 | 

Session ID.

The value contains only letters, digits, underscores (\_), and hyphens (-).

It is used to distinguish between different sessions and has no length restrictions.

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

-   **<'online', number>**: mode.

Optional. **1**: offline. Currently, only the offline mode is supported.

 |

#### StartParams

Parameters for starting speech recognition, including the session ID and audio configuration.

**System capability**: SystemCapability.AI.SpeechRecognizer

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

sessionId

 | 

string

 | 

No

 | 

No

 | 

Session ID.

The value contains only letters, digits, underscores (\_), and hyphens (-).

It is used to distinguish between different sessions and has no length restrictions.

 |
| 

audioInfo

 | 

[AudioInfo](#section85771521101910)

 | 

No

 | 

No

 | 

Audio configuration.

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

-   **<'recognitionMode', number>**: mode of real-time speech recognition.

**0**: real-time recognition from recording. The recording permission **ohos.permission.MICROPHONE** must be enabled for the app. To end recognition, call the [finish](#section14433919171116) method.

**1**: real-time audio-to-text recognition. In this mode, you need to call the [writeAudio](#section72131731149) method to pass the audio stream to be recognized.

Optional. If this parameter is left empty, **1** will be used by default.

-   **<'vadBegin', number>**:

Start point of Voice Activity Detection (VAD). The value ranges from 500 to 10000.

Optional. If this parameter is left empty, **10000** will be used by default, indicating 10,000 ms.

-   **<'vadEnd', number>**:

End point of VAD. The value ranges from 500 to 10000.

Optional. If this parameter is left empty, **800** will be used by default, indicating 800 ms.

-   **<'maxAudioDuration', number>**: Maximum audio duration. If this parameter is left empty, 20000 ms is used by default.

In short speech mode, the value ranges from 20000 to 60000, in ms.

In long speech mode, the value ranges from 20000 to 28800000 (8 x 60 x 60 x 1000), in ms.

-   **<'recognizerOption', <'enablePartialResult', boolean>>**:

Indicates whether text is displayed in real time. (This mode can be enabled only for long speech.)

Optional. If this parameter is left empty, this mode is enabled by default.

To enable real-time text display:

"recognizerOption": recognizerOption = {

"enablePartialResult": true

}

To disable real-time text display:

"recognizerOption": recognizerOption = {

"enablePartialResult": false

}

-   **<'sessionGeneralLexicon': string\[\]>**

Session hotwords. You can configure hotwords to improve the recognition rate. Session hotwords have a higher priority than system hotwords and will be cleared when a session ends.

Optional. This parameter is empty by default when it is not set. You can configure up to 200 hotwords, each of which contains 2 to 20 characters.

 |

#### AudioInfo

Audio configuration.

**System capability**: SystemCapability.AI.SpeechRecognizer

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

Audio type.

Only **pcm** is supported currently.

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

Audio sampling rate.

Currently, only **16000** is supported.

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

Bit depth of the audio.

Currently, only **16** is supported.

 |
| 

soundChannel

 | 

number

 | 

No

 | 

No

 | 

Channel number of the audio.

Currently, only channel 1 is supported.

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

-   **<'compressRate', number>**: audio compression rate.

Optional. The default value is **0** for the PCM format. This parameter is reserved for future use.

 |

#### SpeechRecognitionResult

Speech recognition result.

**System capability**: SystemCapability.AI.SpeechRecognizer

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

isFinal

 | 

boolean

 | 

No

 | 

No

 | 

Indicates whether this is the final result for the current clause.

-   **true**: yes
-   **false**: no

 |
| 

isLast

 | 

boolean

 | 

No

 | 

No

 | 

Indicates whether a sentence is the last one.

-   **true**: yes
-   **false**: no

 |
| 

result

 | 

string

 | 

No

 | 

No

 | 

Optimal recognition result.

 |
