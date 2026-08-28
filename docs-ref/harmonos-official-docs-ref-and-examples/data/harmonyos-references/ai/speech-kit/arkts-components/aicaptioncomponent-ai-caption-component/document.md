# AICaptionComponent (AI Caption Component)

The AICaption control uses AI capabilities to convert voice into text in real time, translate the text, and display the source and target texts. This feature is applicable to audio and video content apps. It helps users efficiently obtain information through captions in scenarios where audio content cannot be directly browsed or users are unfamiliar with audio source languages.

**Start version**: 5.0.0(12)

#### Module Import

import { 
  AICaptionComponent, AudioInfo, AudioData, AICaptionOptions, AICaptionController
} from "@kit.SpeechKit";

#### AICaptionComponent

AI caption component, which can be loaded as a dynamic component.

**Decorator type**: @Component

**System capability**: SystemCapability.AI.AICaption

**Start version**: 5.0.0(12)

**Parameters**:

| 
Name

 | 

Type

 | 

Mandatory

 | 

Decorator Type

 | 

Description

 |
| :-- | :-- | :-- | :-- | :-- |
| 

isShown

 | 

boolean

 | 

Yes

 | 

@Link

 | 

Indicates whether to display captions.

**true**: yes (Automatic audio recognition and caption generation are supported since version 5.1.0(18).)

**false**: no

 |
| 

controller

 | 

[AICaptionController](#section816451553012)

 | 

Yes

 | 

\-

 | 

Caption controller.

 |
| 

options

 | 

[AICaptionOptions](#section15787428226)

 | 

Yes

 | 

\-

 | 

Caption initialization parameters.

 |

#### \[h2\]build

build(): void

Constructor used to create an [AICaptionComponent](#section7266241469) object.

**System capability**: SystemCapability.AI.AICaption

**Start version**: 5.0.0(12)

**Example**:

import { AICaptionComponent, AICaptionController, AICaptionOptions } from '@kit.SpeechKit';

@Entry
@Component
struct Index {
  private captionOption?: AICaptionOptions;
  private controller = new AICaptionController();
  @State isShow: boolean = false;

  aboutToAppear(): void {
    this.captionOption = {
      initialOpacity: 1,
      onPrepared: () => {
      },
      onError: () => {
      }
    }
  }

  build() {
    Column() {
      // Call the **AICaptionComponent** component to initialize captions.
      AICaptionComponent({
        isShown: this.isShow,
        controller: this.controller,
        options: this.captionOption
      })
    }
  }
}

#### AICaptionController

Main function entry class of the AI caption control.

**System capability**: SystemCapability.AI.AICaption

**Start version**: 5.0.0(12)

**Example**:

import { AICaptionComponent, AICaptionOptions, AICaptionController } from '@kit.SpeechKit';

@Entry
@Component
struct Index {
  private options?: AICaptionOptions;
  private controller = new AICaptionController();
  @State isShown: boolean = false;

  aboutToAppear(): void {
    this.options = {
      initialOpacity: 1,
      onPrepared: () => {
      },
      onError: () => {
      }
    }
  }

  build() {
    Column() {
      // Call the **AICaptionComponent** component to initialize captions.
      AICaptionComponent({
        isShown: this.isShown,
        controller: this.controller,
        options: this.options
      })
    }
  }
}

#### \[h2\]getAudioInfo

getAudioInfo(): AudioInfo

Obtains the audio information to be recognized.

**System capability**: SystemCapability.AI.AICaption

**Start version**: 5.0.0(12)

**Returns**:

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

[AudioInfo](#section73559613164)

 | 

Audio information supported by the caption currently in use.

 |

**Example**:

import { AICaptionController, AudioInfo } from '@kit.SpeechKit';

try {
  let controller = new AICaptionController();
  let audioInfo: AudioInfo = controller.getAudioInfo();
} catch (e) {
  console.error(\`GetAudioInfo failed. Code: ${e.code}, message: ${e.message}\`);
}

#### \[h2\]writeAudio

writeAudio(audioData: AudioData): void

Writes audio data. The audio stream data needs to be obtained through the [getAudioInfo](#section16367173452) method. (When this API is called, the app's audio will no longer be automatically obtained for caption generation. Instead, the written audio stream will be used.)

**System capability**: SystemCapability.AI.AICaption

**Start version**: 5.0.0(12)

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

audioData

 | 

[AudioData](#section1869988122518)

 | 

Yes

 | 

Audio data.

 |

**Error codes**:

For details about the error codes, please refer to [ArkTS API Error Codes](../../arkts-api-error-codes/document.md).

| 
Error Code

 | 

Error Message

 |
| :-- | :-- |
| 

401

 | 

Parameter error.

 |
| 

1012900012

 | 

Audio recognition failed.

 |

**Example**:

import { AICaptionController } from '@kit.SpeechKit';
import { AudioData } from '@kit.SpeechKit';

let audioData: AudioData = {
  data: new Uint8Array()
}
try {
  let controller = new AICaptionController();
  controller.writeAudio(audioData)
} catch (e) {
  console.error(\`WriteAudio failed. Code: ${e.code}, message: ${e.message}\`);
}

#### AudioInfo

Audio stream information.

**System capability**: SystemCapability.AI.AICaption

**Start version**: 5.0.0(12)

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

Currently, only PCM encoding is supported.

 |
| 

sampleRate

 | 

audio.[AudioSamplingRate](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-audio-e#audiosamplingrate8)[AudioSamplingRate](../../../../media/audio-kit/arkts-apis/ohos-multimedia-audio-audio-management/enums/document.md#audiosamplingrate8)

 | 

No

 | 

No

 | 

Audio sampling rate.

Currently, only **16000** is supported.

 |
| 

soundChannel

 | 

audio.[AudioChannel](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-audio-e#audiochannel8)[AudioChannel](../../../../media/audio-kit/arkts-apis/ohos-multimedia-audio-audio-management/enums/document.md#audiochannel8)

 | 

No

 | 

No

 | 

Audio channel.

Currently, only one channel is supported.

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

Number of audio sampling bits.

Currently, only **16** is supported.

 |

#### AudioData

Audio data.

**System capability**: SystemCapability.AI.AICaption

**Start version**: 5.0.0(12)

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

data

 | 

Uint8Array

 | 

No

 | 

No

 | 

Audio data.

Currently, the audio data can contain only 640 or 1280 bytes. It is recommended that the interval for sending each request be 20 ms (when the length of the audio to be transmitted is 640 bytes) or 40 ms (when the length of the audio to be transmitted is 1280 bytes).

 |

#### AICaptionOptions

Caption initialization options.

**System capability**: SystemCapability.AI.AICaption

**Start version**: 5.0.0(12)

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

initialOpacity

 | 

number

 | 

No

 | 

Yes

 | 

Opacity of the panel background in simplified caption mode.

-   For phones and tablets, the value ranges from 0 to 1. **1** indicates fully opaque and **0** indicates fully transparent (that is, a component is hidden but still occupies space in the layout). The default value is **0**.
-   For 2-in-1 devices, the values are **0** (fully transparent), **0.5** (semi-transparent), and **1** (fully opaque). The default value is **0**.

 |
| 

onPrepared

 | 

Callback<void>

 | 

No

 | 

No

 | 

Callback for listening to the completion of control initialization.

 |
| 

onError

 | 

ErrorCallback

 | 

No

 | 

No

 | 

Callback for listening to control errors.

 |

**Error codes**:

For details about the error codes, please refer to [ArkTS API Error Codes](../../arkts-api-error-codes/document.md).

| 
Error Code

 | 

Error Message

 |
| :-- | :-- |
| 

1012900010

 | 

AI caption service is busy.

 |
| 

1012900011

 | 

AI caption controller initialized failed.

 |
