# TextReader (Reading Control)

The reading control uses AI capabilities to convert text into speech in real time and read it aloud. It can be integrated into apps used for browsing text content such as news, helping users efficiently access information through text-to-speech in scenarios where direct reading is restricted.

**Start version**: 5.0.0(12)

#### Module Import

import { TextReader } from '@kit.SpeechKit';

#### Precautions

Before calling the reading control APIs, you must call [init](#section173751154134515) to initialize the reading control. Otherwise, an error will be reported.

#### init

init(context: common.BaseContext, readParams: ReaderParam): Promise<void>

Initializes the reading control, that is, the TTS engine and underlying player. If the initialization fails, an error code will be returned.

This API returns the result asynchronously through a promise. To configure long-duration permissions, please refer to [step 9 in the development guide](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/speech-textreader-guide#li56192364816).

**Atomic service API**: This API can be used in atomic services since API version 5.0.3(15).

**Required permission**: ohos.permission.KEEP\_BACKGROUND\_RUNNING

**System capability**: SystemCapability.AI.Component.TextReader

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

context

 | 

[common.BaseContext](../../../../application-framework/ability-kit/arkts-apis/dependent-elements-and-definitions/application/basecontext/document.md)

 | 

Yes

 | 

App context.

 |
| 

readParams

 | 

[ReaderParam](#section6129163245310)

 | 

Yes

 | 

Reading parameters.

 |

**Returns**:

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

Promise<void>

 | 

**Promise** object. No result is returned.

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

201

 | 

Permission denied. Interface caller does not have permission ohos.permission.KEEP\_BACKGROUND\_RUNNING.

 |
| 

401

 | 

Parameter error.

 |
| 

1010600011

 | 

Initialize failed.

 |

**Example**:

import { TextReader } from '@kit.SpeechKit';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct Index {
  // Obtain the app context.

  async aboutToAppear(): Promise<void> {
    let context: Context | undefined = this.getUIContext().getHostContext();
    if (context) {
      // Set reading parameters.
      const readerParams: TextReader.ReaderParam = {
        isVoiceBrandVisible: true,
        businessBrandInfo: {
          panelName: 'AI Reader',
          panelIcon: $r('app.media.startIcon')
        }
      };
      // Initialize the reading control.
      await TextReader.init(context, readerParams).then(() => {
        console.info(\`TextReader succeeded in initializing.\`);
      }).catch((e: BusinessError) => {
        console.error(\`TextReader failed to initialize. Code: ${e.code}, message: ${e.message}\`);
      })
    }
  }

  build() {
  }
}

#### start

start(readInfoList: ReadInfo\[\], articleId?: string): Promise<void>

Starts playback through the reading control. If the playback fails, an error code will be returned.

This API returns the result asynchronously through a promise.

**Atomic service API**: This API can be used in atomic services since API version 5.0.3(15).

**System capability**: SystemCapability.AI.Component.TextReader

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

readInfoList

 | 

[ReadInfo](#section129918404172)\[\]

 | 

Yes

 | 

List of articles to read.

-   If the first article in the list has a category (that is, the **category** or **categoryObject** field is specified for the article) and the following articles do not, the following articles will be categorized under **Others**.
-   If the first article in the list does not have a category, the following articles, even with a category specified, will not be categorized.

 |
| 

articleId

 | 

string

 | 

No

 | 

Article ID. If **articleId** is not passed, the playback starts from the first article in the article list by default. If **articleId** is passed, the playback starts from this specified article. (The article ID must be unique. Otherwise, the first article with the same ID will be automatically read when you access the articles with the same ID from the list.)

 |

**Returns**:

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

Promise<void>

 | 

**Promise** object. No result is returned.

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

1010600012

 | 

The TextReader is not initialized.

 |
| 

1010600013

 | 

Text-to-speech engine error.

 |
| 

1010600014

 | 

AudioRenderer play error.

 |
| 

1010600015

 | 

Audio decode error.

 |
| 

1010600016

 | 

AVSession error.

 |
| 

1010600017

 | 

Other error.

 |

**Example**:

import { TextReader } from '@kit.SpeechKit';
import { BusinessError } from '@kit.BasicServicesKit';

const readInfoList: TextReader.ReadInfo\[\] = \[{
  id: '001',
  title: {
    text:'_Title of the text to read_',
    isClickable:true
  },
  author:{
    text:'_Author of the text to read_',
    isClickable:true
  },
  date: {
    text:'2024/01/01',
    isClickable:false
  },
  bodyInfo: '_Text body to read_'
}\];
// Start the reading control.
TextReader.start(readInfoList).then(() => {
  console.info(\`TextReader succeeded in starting\`);
}).catch((e: BusinessError) => {
  console.error(\`TextReader failed to start. Code: ${e.code}, message: ${e.message}\`);
})

#### start

start(readInfoList: ReadInfo\[\], articleId: string | undefined, startParams: StartParams): Promise<void>

Starts playback through the reading control. You can set **startParams** to hide the minibar. If the playback fails, an error code will be returned.

This API returns the result asynchronously through a promise.

**Atomic service API**: This API can be used in atomic services since API version 5.0.3(15).

**System capability**: SystemCapability.AI.Component.TextReader

**Start version**: 5.0.2(14)

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

readInfoList

 | 

[ReadInfo](#section129918404172)\[\]

 | 

Yes

 | 

List of articles to read.

-   If the first article in the list has a category (that is, the **category** or **categoryObject** field is specified for the article) and the following articles do not, the following articles will be categorized under **Others**.
-   If the first article in the list does not have a category, the following articles, even with a category specified, will not be categorized.

 |
| 

articleId

 | 

string | undefined

 | 

Yes

 | 

Article ID. (The article ID must be unique; otherwise, the first article with the same ID in the list will be automatically selected.) If **articleId** is not passed, the first article in the list will be played by default, followed by the next. If **articleId** is passed, the specified article will be played, followed by the next.

 |
| 

startParams

 | 

[StartParams](#section6254122715301)

 | 

Yes

 | 

Parameters for starting playback through the reading control.

 |

**Returns**:

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

Promise<void>

 | 

Promise that returns no result.

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

1010600012

 | 

The TextReader is not initialized.

 |
| 

1010600013

 | 

Text-to-speech engine error.

 |
| 

1010600014

 | 

AudioRenderer play error.

 |
| 

1010600015

 | 

Audio decode error.

 |
| 

1010600016

 | 

AVSession error.

 |
| 

1010600017

 | 

Other error.

 |

**Example**:

import { TextReader } from '@kit.SpeechKit';
import { BusinessError } from '@kit.BasicServicesKit';

const readInfoList: TextReader.ReadInfo\[\] = \[{
  id: '001',
  title: {
    text:'_Title of the text to read_',
    isClickable:true
  },
  author:{
    text:'_Author of the text to read_',
    isClickable:true
  },
  date: {
    text:'2024/01/01',
    isClickable:false
  },
  bodyInfo: '_Text body to read_'
}\];
const startParams: TextReader.StartParams = {
  isMinibarHidden: false,
  callbackParam: '0'
}
// Start the reading control.
TextReader.start(readInfoList, undefined, startParams).then(() => {
  console.info(\`TextReader succeeded in starting\`);
}).catch((e: BusinessError) => {
  console.error(\`TextReader failed to start. Code: ${e.code}, message: ${e.message}\`);
})

#### stop

stop(): Promise<void>

Stops reading, closes the playback panel, unregisters the listeners, and resets parameters.

This API returns the result asynchronously through a promise.

**Atomic service API**: This API can be used in atomic services since API version 5.0.3(15).

**System capability**: SystemCapability.AI.Component.TextReader

**Start version**: 5.0.0(12)

**Returns**:

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

Promise<void>

 | 

**Promise** object. No result is returned.

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

1010600012

 | 

The TextReader is not initialized.

 |

**Example**:

import { TextReader } from '@kit.SpeechKit';
import { BusinessError } from '@kit.BasicServicesKit';

TextReader.stop().then(() => {
  console.info(\`TextReader succeeded in stopping.\`);
}).catch((e: BusinessError) => {
  console.error(\`TextReader failed to stop. Code: ${e.code}, message: ${e.message}\`);
})

#### resetParam

resetParam(paramName: ResetParamType) : void

Resets initialization parameters and clears the playlist.

**Atomic service API**: This API can be used in atomic services since API version 5.0.3(15).

**System capability**: SystemCapability.AI.Component.TextReader

**Start version**: 5.0.2(14)

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

paramName

 | 

[ResetParamType](#section192921653104)

 | 

Yes

 | 

Type of parameters to be reset.

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

**Example**:

import { TextReader } from '@kit.SpeechKit';

try {
  TextReader.resetParam(TextReader.ResetParamType.BAR\_PARAM)
  console.info(\`TextReader succeeded in resetParam.\`);
} catch (e) {
  console.error(\`TextReader failed to resetParam. Code: ${e.code}, message: ${e.message}\`);
}

#### release

release(): Promise<void>

Releases all resources of the reading control.

This API returns the result asynchronously through a promise.

**Atomic service API**: This API can be used in atomic services since API version 5.0.3(15).

**System capability**: SystemCapability.AI.Component.TextReader

**Start version**: 5.0.0(12)

**Returns**:

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

Promise<void>

 | 

**Promise** object. No result is returned.

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

1010600012

 | 

The TextReader is not initialized.

 |
| 

1010600020

 | 

Release error.

 |

**Example**:

import { TextReader } from '@kit.SpeechKit';
import { BusinessError } from '@kit.BasicServicesKit';

TextReader.release().then(() => {
  console.info(\`TextReader succeeded in releasing.\`);
}).catch((e: BusinessError) => {
  console.error(\`TextReader failed to release. Code: ${e.code}, message: ${e.message}\`);
})

#### pause

pause(): void

Pauses playback.

**Atomic service API**: This API can be used in atomic services since API version 5.0.3(15).

**System capability**: SystemCapability.AI.Component.TextReader

**Start version**: 5.0.0(12)

**Error codes**:

For details about the error codes, please refer to [ArkTS API Error Codes](../../arkts-api-error-codes/document.md).

| 
Error Code

 | 

Error Message

 |
| :-- | :-- |
| 

1010600012

 | 

The TextReader is not initialized.

 |

**Example**:

import { TextReader } from '@kit.SpeechKit';

try {
  TextReader.pause();
} catch (e) {
  console.error(\`TextReader failed to pause. Code: ${e.code}, message: ${e.message}\`);
}

#### resume

resume(): void

Resumes playback.

**Atomic service API**: This API can be used in atomic services since API version 5.0.3(15).

**System capability**: SystemCapability.AI.Component.TextReader

**Start version**: 5.0.0(12)

**Error codes**:

For details about the error codes, please refer to [ArkTS API Error Codes](../../arkts-api-error-codes/document.md).

| 
Error Code

 | 

Error Message

 |
| :-- | :-- |
| 

1010600012

 | 

The TextReader is not initialized.

 |
| 

1010600013

 | 

Text-to-speech engine error.

 |
| 

1010600014

 | 

AudioRenderer play error.

 |
| 

1010600015

 | 

Audio decode error.

 |
| 

1010600016

 | 

AVSession error.

 |

**Example**:

import { TextReader } from '@kit.SpeechKit';

try {
  TextReader.resume();
} catch (e) {
  console.error(\`TextReader failed to resume. Code: ${e.code}, message: ${e.message}\`);
}

#### playPrev

playPrev(): void

Plays the previous article.

**Atomic service API**: This API can be used in atomic services since API version 5.0.3(15).

**System capability**: SystemCapability.AI.Component.TextReader

**Start version**: 5.0.0(12)

**Error codes**:

For details about the error codes, please refer to [ArkTS API Error Codes](../../arkts-api-error-codes/document.md).

| 
Error Code

 | 

Error Message

 |
| :-- | :-- |
| 

1010600012

 | 

The TextReader is not initialized.

 |
| 

1010600018

 | 

playPrev failed.

 |

**Example**:

import { TextReader } from '@kit.SpeechKit';

try {
  TextReader.playPrev();
} catch (e) {
  console.error(\`TextReader failed to play previous article. Code: ${e.code}, message: ${e.message}\`);
}

#### playNext

playNext(): void

Plays the next article.

**Atomic service API**: This API can be used in atomic services since API version 5.0.3(15).

**System capability**: SystemCapability.AI.Component.TextReader

**Start version**: 5.0.0(12)

**Error codes**:

For details about the error codes, please refer to [ArkTS API Error Codes](../../arkts-api-error-codes/document.md).

| 
Error Code

 | 

Error Message

 |
| :-- | :-- |
| 

1010600012

 | 

The TextReader is not initialized.

 |
| 

1010600019

 | 

playNext failed.

 |

**Example**:

import { TextReader } from '@kit.SpeechKit';

try {
  TextReader.playNext();
} catch (e) {
  console.error(\`TextReader failed to play next article. Code: ${e.code}, message: ${e.message}\`);
}

#### hidePanel

hidePanel(): void

Hides the playback panel.

**Atomic service API**: This API can be used in atomic services since API version 5.0.3(15).

**System capability**: SystemCapability.AI.Component.TextReader

**Start version**: 5.0.0(12)

**Error codes**:

For details about the error codes, please refer to [ArkTS API Error Codes](../../arkts-api-error-codes/document.md).

| 
Error Code

 | 

Error Message

 |
| :-- | :-- |
| 

1010600012

 | 

The TextReader is not initialized.

 |

**Example**:

import { TextReader } from '@kit.SpeechKit';

try {
  TextReader.hidePanel();
} catch (e) {
  console.error(\`TextReader failed to hide panel. Code: ${e.code}, message: ${e.message}\`);
}

#### showPanel

showPanel(): void

Shows the playback panel.

**Atomic service API**: This API can be used in atomic services since API version 5.0.3(15).

**System capability**: SystemCapability.AI.Component.TextReader

**Start version**: 5.0.0(12)

**Error codes**:

For details about the error codes, please refer to [ArkTS API Error Codes](../../arkts-api-error-codes/document.md).

| 
Error Code

 | 

Error Message

 |
| :-- | :-- |
| 

1010600012

 | 

The TextReader is not initialized.

 |

**Example**:

import { TextReader } from '@kit.SpeechKit';

try {
  TextReader.showPanel();
} catch (e) {
  console.error(\`TextReader failed to show panel. Code: ${e.code}, message: ${e.message}\`);
}

#### showMinibar

showMinibar(): void

Shows the minibar.

**Atomic service API**: This API can be used in atomic services since API version 5.0.3(15).

**System capability**: SystemCapability.AI.Component.TextReader

**Start version**: 5.0.2(14)

**Error codes**:

For details about the error codes, please refer to [ArkTS API Error Codes](../../arkts-api-error-codes/document.md).

| 
Error Code

 | 

Error Message

 |
| :-- | :-- |
| 

1010600012

 | 

The TextReader is not initialized.

 |

**Example**:

import { TextReader } from '@kit.SpeechKit';

try {
  TextReader.showMinibar();
} catch (e) {
  console.error(\`TextReader failed to show Minibar. Code: ${e.code}, message: ${e.message}\`);
}

#### hideMinibar

hideMinibar(): void

Hides the minibar.

**Atomic service API**: This API can be used in atomic services since API version 5.0.3(15).

**System capability**: SystemCapability.AI.Component.TextReader

**Start version**: 5.0.2(14)

**Error codes**:

For details about the error codes, please refer to [ArkTS API Error Codes](../../arkts-api-error-codes/document.md).

| 
Error Code

 | 

Error Message

 |
| :-- | :-- |
| 

1010600012

 | 

The TextReader is not initialized.

 |

**Example**:

import { TextReader } from '@kit.SpeechKit';

try {
  TextReader.hideMinibar();
} catch (e) {
  console.error(\`TextReader failed to hide Minibar. Code: ${e.code}, message: ${e.message}\`);
}

#### queryReadState

queryReadState(id?: string): ReadState

Queries the article reading status.

**Atomic service API**: This API can be used in atomic services since API version 5.0.3(15).

**System capability**: SystemCapability.AI.Component.TextReader

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

id

 | 

string

 | 

No

 | 

Article ID. The default value is the ID of the article that is being read.

 |

**Returns**:

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

[ReadState](#section178743012141)

 | 

Article reading status.

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

**Example**:

import { TextReader } from '@kit.SpeechKit';

try {
  let readState = TextReader.queryReadState('article\_01');
  console.info(\`Succeeded in querying read state, read state: ${JSON.stringify(readState)}\`);
} catch(e) {
  console.error(\`TextReader failed to queryReadState. Code: ${e.code}, message: ${e.message}\`);
}

#### setArticleContent

setArticleContent(id: string, content?: string): void

Sets the article content.

**Atomic service API**: This API can be used in atomic services since API version 5.0.3(15).

**System capability**: SystemCapability.AI.Component.TextReader

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

id

 | 

string

 | 

Yes

 | 

Article ID.

 |
| 

content

 | 

string

 | 

No

 | 

Article content. If **content** is not passed or is left empty, the content control screen will show a loading failure message when the article with a specific ID is to be played. If **content** is passed, it indicates the content of the article with the specified ID.

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

**Example**:

import { TextReader } from '@kit.SpeechKit';

try {
  TextReader.setArticleContent('article\_01', '_Text body to read_');
} catch (e) {
  console.error(\`TextReader failed to setArticleContent. Code: ${e.code}, message: ${e.message}\`);
}

#### setArticle

setArticle(readInfo: ReadInfo): void

Sets the information about a specified article and plays the article immediately.

**Atomic service API**: This API can be used in atomic services since API version 5.0.3(15).

**System capability**: SystemCapability.AI.Component.TextReader

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

readInfo

 | 

[ReadInfo](#section129918404172)

 | 

Yes

 | 

Article information. Only parameters **image**, **imageUrl**, **bodyInfo**, and **bodyInfoObject** need to be updated. If the article ID is not in the list, the article cannot be played.

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

**Example**:

import { TextReader } from '@kit.SpeechKit';
import { image } from '@kit.ImageKit';

const readInfo: TextReader.ReadInfo = {
  id: '001',
  title: {
    text:'_Title of the text to read_',
    isClickable:true
  },
  author:{
    text:'_Author of the text to read_',
    isClickable:true
  },
  date: {
    text:'2024/01/01',
    isClickable:false
  },
  bodyInfo: '_Text body to read_',
  image: {} as image.PixelMap
};
try {
  TextReader.setArticle(readInfo);
} catch (e) {
  console.error(\`TextReader failed to setArticle. Code: ${e.code}, message: ${e.message}\`);
}

#### loadMore

loadMore(readInfos: ReadInfo\[\], isEnd: boolean): void

Loads more articles to the article list. This API must be called after **init** and **start** are called in the project. You are advised to use this API in the **'requestMore'** action listener.

**Atomic service API**: This API can be used in atomic services since API version 5.0.3(15).

**System capability**: SystemCapability.AI.Component.TextReader

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

readInfos

 | 

[ReadInfo](#section129918404172)\[\]

 | 

Yes

 | 

List of articles to load.

 |
| 

isEnd

 | 

boolean

 | 

Yes

 | 

Indicates whether more content needs to be loaded.

-   **true**: All content has been loaded.
-   **false**: Some content is not completely loaded.

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

**Example**:

import { ReadStateCode, TextReader, TextReaderIcon } from '@kit.SpeechKit';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct Index {

  @State readInfoList: TextReader.ReadInfo\[\] = \[\];
  @State readState: ReadStateCode = ReadStateCode.WAITING;
  @State isInit: boolean = false;
  @State selectedReadInfo: TextReader.ReadInfo = this.readInfoList\[0\];
  async aboutToAppear(){
    let context: Context | undefined = this.getUIContext().getHostContext();
    if (!context) {
      console.error(\`context is undefined.\`);
      return;
    }

    // Set reading parameters.
    const readerParams: TextReader.ReaderParam = {
      isVoiceBrandVisible: true,
      businessBrandInfo: {
        panelName: 'AI Reader',
        panelIcon: $r('app.media.startIcon')
      }
    };

    // Initialize the reading control.
    TextReader.init(context, readerParams).then(() => {
      console.info(\`TextReader succeeded in initializing.\`);
    }).catch((e: BusinessError) => {
      console.error(\`TextReader failed to initialize. Code: ${e.code}, message: ${e.message}\`);
    })

    /\*\*
     \* Load the data.
     \*/
    console.info(\`ReadStateCode: ${JSON.stringify(this.readState)}\`);
    let readInfoList: TextReader.ReadInfo\[\] = \[{
      id: '001',
      title: {
        text:'_Title of the text to read_',
        isClickable:true
      },
      author:{
        text:'_Author of the text to read_',
        isClickable:true
      },
      date: {
        text:'2024/01/01',
        isClickable:false
      },
      bodyInfo: '_Text body to read_'
    }\];
    this.readInfoList = readInfoList;
    this.selectedReadInfo = this.readInfoList\[0\];
  }

  // Set an action listener.
  setActionListener() {
    // ...
    TextReader.on('requestMore', () => {
      console.info(\`requestMore\`);
      try {
        console.info(\`loadMore\`);
        TextReader.loadMore(this.readInfoList, true);
      } catch (e) {
        console.error(\`TextReader failed to loadMore. Code: ${e.code}, message: ${e.message}\`);
      }
    });
  }

  build() {
    Column() {
      TextReaderIcon({ readState: this.readState })
        .margin({ right: 20 })
        .width(32)
        .height(32)
        .onClick(async () => {
          try {
            this.setActionListener();
            await TextReader.start(this.readInfoList, this.selectedReadInfo?.id);
          } catch(e) {
            console.error(\`TextReader failed to start\`);
          }
        })
    }
    .height('100%')
  }
}

#### queryReadStateByCategoryId

queryReadStateByCategoryId(categoryId: string): ReadState

Queries the article status based on the category ID and checks whether the current category contains the article that is being played.

**Atomic service API**: This API can be used in atomic services since API version 5.0.3(15).

**System capability**: SystemCapability.AI.Component.TextReader

**Start version**: 5.0.2(14)

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

categoryId

 | 

string

 | 

Yes

 | 

Category ID of the article that is being played.

 |

**Returns**:

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

[ReadState](#section178743012141)

 | 

Article reading status.

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

import { TextReader } from '@kit.SpeechKit';

try {
  let readState = TextReader.queryReadStateByCategoryId('categoryId\_01');
  console.info(\`Succeeded in querying read state by category id, read state: ${JSON.stringify(readState)}\`);
} catch(e) {
  console.error(\`TextReader failed to queryReadStateByCategoryId. Code: ${e.code}, message: ${e.message}\`);
}

#### on(type: 'setArticle')

on(type: 'setArticle', callback: Callback<string>): void

Registers a callback for article setting, which will be triggered if the target article is empty (**bodyInfo** being empty) when an article is tapped or switched. When multiple callbacks are registered for the same event, only the first one takes effect.

**Atomic service API**: This API can be used in atomic services since API version 5.0.3(15).

**System capability**: SystemCapability.AI.Component.TextReader

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

type

 | 

string

 | 

Yes

 | 

Event type. The **'setArticle'** event type is supported and will be triggered if the target article is empty (**bodyInfo** being empty) when an article is set.

 |
| 

callback

 | 

Callback<string>

 | 

Yes

 | 

Callback executed when an article is tapped or switched, with the article ID passed.

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

**Example**:

import { TextReader } from '@kit.SpeechKit';

try {
  TextReader.on('setArticle', (id: string) => {
    console.info(\`Succeeded in setting setArticleListener: ${id}\`);
  });
} catch (e) {
  console.error(\`TextReader failed to set eventListener. Code: ${e.code}, message: ${e.message}\`);
}

#### off(type: 'setArticle')

off(type: 'setArticle', callback?: Callback<string>): void

Unregisters a callback for article setting, and will be used after **on(type: 'setArticle')** is called. You can register a new callback after the current one is unregistered.

**Atomic service API**: This API can be used in atomic services since API version 5.0.3(15).

**System capability**: SystemCapability.AI.Component.TextReader

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

type

 | 

string

 | 

Yes

 | 

Event type. The **'setArticle'** event type is supported and will be triggered when an article is set.

 |
| 

callback

 | 

Callback<string>

 | 

No

 | 

Callback to be canceled, which must be the same as that passed upon subscription. If this parameter is not specified, all callbacks for listening to the event will be canceled. (Currently only one callback is used.)

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

**Example**:

import { TextReader } from '@kit.SpeechKit';

try {
  TextReader.off('setArticle');
} catch (e) {
  console.error(\`TextReader failed to unset eventListener. Code: ${e.code}, message: ${e.message}\`);
}

#### on(type: 'clickArticle' | 'clickAuthor' | 'clickNotification')

on(type: 'clickArticle' | 'clickAuthor' | 'clickNotification', callback: Callback<string>): void

Registers a callback for the tap event, which will be triggered when the title, author, or notification bar is tapped. When multiple callbacks are registered for the same event, only the first one takes effect.

**Atomic service API**: This API can be used in atomic services since API version 5.0.3(15).

**System capability**: SystemCapability.AI.Component.TextReader

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

type

 | 

string

 | 

Yes

 | 

Event type.

-   **'clickArticle'**: The article title is tapped.
-   **'clickAuthor'**: The article author is tapped.
-   **'clickNotification'**: The notification bar is tapped. Reserved value, which is not supported currently.

 |
| 

callback

 | 

Callback<string>

 | 

Yes

 | 

Callback for the tap event, with the article ID passed.

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

**Example**:

import { TextReader } from '@kit.SpeechKit';

try {
  TextReader.on('clickArticle', (id: string) => {
    console.info(\`Succeeded in setting clickArticleListener: ${id}\`);
  });
  TextReader.on('clickAuthor', (id: string) => {
    console.info(\`Succeeded in setting clickAuthorListener: ${id}\`);
  });
  TextReader.on('clickNotification', (id: string) => {
    console.info(\`Succeeded in setting clickNotificationListener: ${id}\`);
  });
} catch (e) {
  console.error(\`TextReader failed to set eventListener. Code: ${e.code}, message: ${e.message}\`);
}

#### off(type: 'clickArticle' | 'clickAuthor' | 'clickNotification')

off(type: 'clickArticle' | 'clickAuthor' | 'clickNotification', callback?: Callback<string>): void

Unregisters a callback for the tap event, and will be used after **on(type: 'clickArticle' | 'clickAuthor' | 'clickNotification')** is called. You can register a new callback after the current one is unregistered.

**Atomic service API**: This API can be used in atomic services since API version 5.0.3(15).

**System capability**: SystemCapability.AI.Component.TextReader

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

type

 | 

string

 | 

Yes

 | 

Event type.

-   **'clickArticle'**: The article title is tapped.
-   **'clickAuthor'**: The article author is tapped.
-   **'clickNotification'**: The notification bar is tapped.

 |
| 

callback

 | 

Callback<string>

 | 

No

 | 

Callback to be canceled, which must be the same as that passed upon subscription. If this parameter is not specified, all callbacks for listening to the event will be canceled. (Currently only one callback is used.)

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

**Example**:

import { TextReader } from '@kit.SpeechKit';

try {
  TextReader.off('clickArticle');
  TextReader.off('clickAuthor');
  TextReader.off('clickNotification');
} catch (e) {
  console.error(\`TextReader failed to unset eventListener. Code: ${e.code}, message: ${e.message}\`);
}

#### on(type: 'showPanel' | 'hidePanel')

on(type: 'showPanel' | 'hidePanel', callback: Callback<void>): void

Registers a callback for the playback panel showing or hiding event, which will be triggered when the playback panel is shown or hidden. When multiple callbacks are registered for the same event, only the first one takes effect.

**Atomic service API**: This API can be used in atomic services since API version 5.0.3(15).

**System capability**: SystemCapability.AI.Component.TextReader

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

type

 | 

string

 | 

Yes

 | 

Event type.

-   **'showPanel'**: The panel is shown.
-   **'hidePanel'**: The panel is hidden.

 |
| 

callback

 | 

Callback<void>

 | 

Yes

 | 

Panel event callback.

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

**Example**:

import { TextReader } from '@kit.SpeechKit';

try {
  TextReader.on('showPanel', () => {
    console.info(\`Succeeded in setting showPanelListener.\`);
  });
  TextReader.on('hidePanel', () => {
    console.info(\`Succeeded in setting hidePanelListener.\`);
  });
} catch (e) {
  console.error(\`TextReader failed to set eventListener. Code: ${e.code}, message: ${e.message}\`);
}

#### off(type: 'showPanel' | 'hidePanel')

off(type: 'showPanel' | 'hidePanel', callback?: Callback<void>): void

Unregisters a callback for the playback panel showing or hiding event, and will be used after **on(type: 'showPanel' | 'hidePanel')** is called. You can register a new callback after the current one is unregistered.

**Atomic service API**: This API can be used in atomic services since API version 5.0.3(15).

**System capability**: SystemCapability.AI.Component.TextReader

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

type

 | 

string

 | 

Yes

 | 

Event type.

-   **'showPanel'**: The panel is shown.
-   **'hidePanel'**: The panel is hidden.

 |
| 

callback

 | 

Callback<void>

 | 

No

 | 

Callback to be canceled, which must be the same as that passed upon subscription. If this parameter is not specified, all callbacks for listening to the event will be canceled. (Currently only one callback is used.)

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

**Example**:

import { TextReader } from '@kit.SpeechKit';

try {
  TextReader.off('showPanel');
  TextReader.off('hidePanel');
} catch (e) {
  console.error(\`TextReader failed to unset eventListener. Code: ${e.code}, message: ${e.message}\`);
}

#### on(type: 'stop' | 'release')

on(type: 'stop' | 'release', callback: Callback<void>): void

Registers a callback for the **stop/release** event, which will be triggered when the **stop/release** API is called. When multiple callbacks are registered for the same event, only the first one takes effect.

**Atomic service API**: This API can be used in atomic services since API version 5.0.3(15).

**System capability**: SystemCapability.AI.Component.TextReader

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

type

 | 

string

 | 

Yes

 | 

Event type.

-   **'stop'**: The **stop** API is called.
-   **'release'**: The **release** API is called to release resources.

 |
| 

callback

 | 

Callback<void>

 | 

Yes

 | 

Callback of the **stop**/**release** event.

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

**Example**:

import { TextReader } from '@kit.SpeechKit';

try {
  TextReader.on('stop', () => {
    console.info(\`Succeeded in setting stopListener.\`);
  });
  TextReader.on('release', () => {
    console.info(\`Succeeded in setting releaseListener.\`);
  });
} catch (e) {
  console.error(\`TextReader failed to set eventListener. Code: ${e.code}, message: ${e.message}\`);
}

#### off(type: 'stop' | 'release')

off(type: 'stop' | 'release', callback?: Callback<void>): void

Unregisters a callback for the **stop/release** event, and will be used after **on(type: 'stop' | 'release')** is called. You can register a new callback after the current one is unregistered.

**Atomic service API**: This API can be used in atomic services since API version 5.0.3(15).

**System capability**: SystemCapability.AI.Component.TextReader

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

type

 | 

string

 | 

Yes

 | 

Event type.

-   **'stop'**: The **stop** API is called or a user exits by swiping the notification bar.
-   **'release'**: The **release** API is called to release resources.

 |
| 

callback

 | 

Callback<void>

 | 

No

 | 

Callback to be canceled, which must be the same as that passed upon subscription. If this parameter is not specified, all callbacks for listening to the event will be canceled. (Currently only one callback is used.)

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

**Example**:

import { TextReader } from '@kit.SpeechKit';

try {
  TextReader.off('stop');
  TextReader.off('release');
} catch (e) {
  console.error(\`TextReader failed to unset eventListener. Code: ${e.code}, message: ${e.message}\`);
}

#### on(type: 'stateChange')

on(type: 'stateChange', callback: Callback<ReadState>): void

Registers a callback for the status change event, which will be triggered when the status of the article that is being played changes. When multiple callbacks are registered for the same event, only the first one takes effect.

**Atomic service API**: This API can be used in atomic services since API version 5.0.3(15).

**System capability**: SystemCapability.AI.Component.TextReader

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

type

 | 

string

 | 

Yes

 | 

Event type. The **'stateChange'** event type is supported and will be triggered when the status of the article that is being played changes.

 |
| 

callback

 | 

Callback<[ReadState](#section178743012141)\>

 | 

Yes

 | 

Callback executed when the status of the article that is being played changes.

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

**Example**:

import { TextReader } from '@kit.SpeechKit';

try {
  TextReader.on('stateChange', (state: TextReader.ReadState) => {
    console.info(\`Succeeded in setting stateChangeListener: ${JSON.stringify(state)}\`);
  });
} catch (e) {
  console.error(\`TextReader failed to set eventListener. Code: ${e.code}, message: ${e.message}\`);
}

#### off(type: 'stateChange')

off(type: 'stateChange', callback?: Callback<ReadState>): void

Unregisters a callback for the article (that is being played) status change event, and will be used after **on(type: 'stateChange')** is called. You can register a new callback after the current one is unregistered.

**Atomic service API**: This API can be used in atomic services since API version 5.0.3(15).

**System capability**: SystemCapability.AI.Component.TextReader

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

type

 | 

string

 | 

Yes

 | 

Event type. The **'stateChange'** event type is supported and will be triggered when the status of the article that is being played changes.

 |
| 

callback

 | 

Callback<[ReadState](#section178743012141)\>

 | 

No

 | 

Callback to be canceled, which must be the same as that passed upon subscription. If this parameter is not specified, all callbacks for listening to the event will be canceled. (Currently only one callback is used.)

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

**Example**:

import { TextReader } from '@kit.SpeechKit';

try {
  TextReader.off('stateChange');
} catch (e) {
  console.error(\`TextReader failed to unset on(type: 'requestMore')eventListener. Code: ${e.code}, message: ${e.message}\`);
}

#### on(type: 'requestMore')

on(type: 'requestMore', callback: Callback<void>): void

Registers a callback for the event of requesting more articles, which will be triggered when the reading list is swiped to the bottom or the last article is played. When multiple callbacks are registered for the same event, only the first one takes effect.

**Atomic service API**: This API can be used in atomic services since API version 5.0.3(15).

**System capability**: SystemCapability.AI.Component.TextReader

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

type

 | 

string

 | 

Yes

 | 

Event type. The **'requestMore'** event type is supported and will be triggered when more articles are requested.

 |
| 

callback

 | 

Callback<void>

 | 

Yes

 | 

Callback triggered when the reading list is swiped to the bottom or the last article is played.

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

**Example**:

import { TextReader } from '@kit.SpeechKit';

try {
  TextReader.on('requestMore', () => {
    console.info(\`Succeeded in setting requestMoreListener.\`);
  });
} catch (e) {
  console.error(\`TextReader failed to set eventListener. Code: ${e.code}, message: ${e.message}\`);
}

#### on(type: 'requestMore')

on(type: 'requestMore', callback: Callback<string>): void

Registers a callback for the event of requesting more articles, which will be triggered when the reading list is swiped to the bottom or the last article is played. User-defined parameters will be returned through the callback. When multiple callbacks are registered for the same event, only the first one takes effect.

**Atomic service API**: This API can be used in atomic services since API version 5.0.3(15).

**System capability**: SystemCapability.AI.Component.TextReader

**Start version**: 5.0.2(14)

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

Event type. The **'requestMore'** event type is supported and will be triggered when the reading list is swiped to the bottom and more articles are requested.

 |
| 

callback

 | 

Callback<string>

 | 

Yes

 | 

Callback triggered when the reading list is swiped to the bottom or the last article is played. The returned custom parameters will be set through **callbackParam** of [StartParams](#section6254122715301).

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

import { TextReader } from '@kit.SpeechKit';

try {
  TextReader.on('requestMore', (callback) => {
    console.info(\`Succeeded in setting requestMoreListener. Callback is ${callback}\`);
  });
} catch (e) {
  console.error(\`TextReader failed to set eventListener. Code: ${e.code}, message: ${e.message}\`);
}

#### off(type: 'requestMore')

off(type: 'requestMore', callback?: Callback<void>): void

Unregisters a callback for the event of swiping the reading list to the bottom or playing the last article, and will be used after **on(type: 'requestMore')** is called. You can register a new callback after the current one is unregistered.

**Atomic service API**: This API can be used in atomic services since API version 5.0.3(15).

**System capability**: SystemCapability.AI.Component.TextReader

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

type

 | 

string

 | 

Yes

 | 

Event type. The **'requestMore'** event type is supported and will be triggered when more articles are requested.

 |
| 

callback

 | 

Callback<void>

 | 

No

 | 

Callback to be canceled, which must be the same as that passed upon subscription. If this parameter is not specified, all callbacks for listening to the event will be canceled. (Currently only one callback is used.)

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

**Example**:

import { TextReader } from '@kit.SpeechKit';

try {
  TextReader.off('requestMore');
} catch (e) {
  console.error(\`TextReader failed to unset eventListener. Code: ${e.code}, message: ${e.message}\`);
}

#### off(type: 'requestMore')

off(type: 'requestMore', callback: Callback<string>): void

Unregisters a callback (with user-defined parameters passed) for the event of swiping the reading list to the bottom or playing the last article, and will be used after **on(type: 'requestMore')** is called. You can register a new callback after the current one is unregistered.

**Atomic service API**: This API can be used in atomic services since API version 5.0.3(15).

**System capability**: SystemCapability.AI.Component.TextReader

**Start version**: 5.0.3(15)

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

Event type. The **'requestMore'** event type is supported and will be triggered when more articles are requested.

 |
| 

callback

 | 

Callback<string>

 | 

Yes

 | 

Callback to be canceled, which must be the same as that passed upon subscription.

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

**Example**:

import { TextReader } from '@kit.SpeechKit';

try {
  TextReader.off('requestMore', (callback:string) => {
    console.info(\`Succeeded in setting requestMoreListener. Callback is ${callback}\`);
  });
} catch (e) {
  console.error(\`TextReader failed to unset eventListener. Code: ${e.code}, message: ${e.message}\`);
}

#### on(type: 'eventNotification' | 'eventPanel')

on(type: 'eventNotification' | 'eventPanel', callback: Callback<NotificationEvent| PanelEvent>): void

Registers a callback for the media controller/playback panel status change event, which will be triggered when the status of the media controller or playback panel changes. When multiple callbacks are registered for the same event, only the first one takes effect.

**Atomic service API**: This API can be used in atomic services since API version 5.0.3(15).

**System capability**: SystemCapability.AI.Component.TextReader

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

type

 | 

string

 | 

Yes

 | 

Event type.

-   **'eventNotification'**: The media controller status changes.
-   **'eventPanel'**: The playback panel status changes. The callback for the **BPC\_10 click** event in [PanelEvent](#section13718113213211) supports only mobile phones.

 |
| 

callback

 | 

Callback<[NotificationEvent](#section1612119431629) | [PanelEvent](#section13718113213211)\>

 | 

Yes

 | 

Callback triggered when the status of the media controller or playback panel changes.

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

**Example**:

import { TextReader } from '@kit.SpeechKit';

try {
  TextReader.on('eventNotification', (ne: TextReader.NotificationEvent) => {
    console.info(\`Succeeded in setting eventNotificationListener: ${JSON.stringify(ne)}\`);
  });
  TextReader.on('eventPanel', (pe: TextReader.PanelEvent) => {
    console.info(\`Succeeded in setting eventPanelListener: ${JSON.stringify(pe)}\`);
  });
} catch (e) {
  console.error(\`TextReader failed to set eventListener. Code: ${e.code}, message: ${e.message}\`);
}

#### off(type: 'eventNotification' | 'eventPanel')

off(type: 'eventNotification' | 'eventPanel', callback?: Callback<NotificationEvent | PanelEvent>): void

Unregisters a callback for the media controller/playback panel status change event, and will be used after **on(type: 'eventNotification' | 'eventPanel')** is called. You can register a new callback after the current one is unregistered.

**Atomic service API**: This API can be used in atomic services since API version 5.0.3(15).

**System capability**: SystemCapability.AI.Component.TextReader

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

type

 | 

string

 | 

Yes

 | 

Event type.

-   **'eventNotification'**: The media controller status changes.
-   **'eventPanel'**: The playback panel status changes.

 |
| 

callback

 | 

Callback<[NotificationEvent](#section1612119431629) | [PanelEvent](#section13718113213211)\>

 | 

No

 | 

Callback to be canceled, which must be the same as that passed upon subscription. If this parameter is not specified, all callbacks for listening to the event will be canceled. (Currently only one callback is used.)

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

**Example**:

import { TextReader } from '@kit.SpeechKit';

try {
  TextReader.off('eventNotification');
  TextReader.off('eventPanel');
} catch (e) {
  console.error(\`TextReader failed to unset eventListener. Code: ${e.code}, message: ${e.message}\`);
}

#### on(type: 'eventReadList')

on(type: 'eventReadList', callback: Callback<Array<ListEventState>>): void

Registers a callback for the reading list event, which will be triggered when the reading list icon is tapped. When multiple callbacks are registered for the same event, only the first one takes effect.

**Atomic service API**: This API can be used in atomic services since API version 5.0.3(15).

**System capability**: SystemCapability.AI.Component.TextReader

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

type

 | 

string

 | 

Yes

 | 

Event type. The **'eventReadList'** event type is supported.

 |
| 

callback

 | 

Callback<Array<[ListEventState](#section63451441422)\>>

 | 

Yes

 | 

Callback executed when an interaction with a reading list occurs.

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

**Example**:

import { TextReader } from '@kit.SpeechKit';

try {
  TextReader.on('eventReadList', (list: Array<TextReader.ListEventState>) => {
    list.forEach((id) => {
      console.info(\`Succeeded in setting eventReadListListener, article id: ${id}\`);
    })
  });
} catch (e) {
  console.error(\`TextReader failed to set eventListener. Code: ${e.code}, message: ${e.message}\`);
}

#### off(type: 'eventReadList')

off(type: 'eventReadList', callback?: Callback<Array<ListEventState>>): void

Unregisters a callback for the reading list event, and will be used after **on(type: 'eventReadList')** is called. You can register a new callback after the current one is unregistered.

**Atomic service API**: This API can be used in atomic services since API version 5.0.3(15).

**System capability**: SystemCapability.AI.Component.TextReader

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

type

 | 

string

 | 

Yes

 | 

Event type. The **'eventReadList'** event type is supported.

 |
| 

callback

 | 

Callback<Array<[ListEventState](#section63451441422)\>>

 | 

No

 | 

Callback to be canceled, which must be the same as that passed upon subscription. If this parameter is not specified, all callbacks for listening to the event will be canceled. (Currently only one callback is used.)

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

**Example**:

import { TextReader } from '@kit.SpeechKit';

try {
  TextReader.off('eventReadList');
} catch (e) {
  console.error(\`TextReader failed to unset eventListener. Code: ${e.code}, message: ${e.message}\`);
}

#### on(type: 'readProgress')

on(type: 'readProgress', callback: Callback<ReadProgress>): void

Registers a callback for the playback progress event, which will be triggered when an interaction related to the playback progress occurs. When multiple callbacks are registered for the same event, only the first one takes effect.

**Atomic service API**: This API can be used in atomic services since API version 5.0.3(15).

**System capability**: SystemCapability.AI.Component.TextReader

**Start version**: 5.0.2(14)

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

Event type. The **'readProgress'** event type is supported.

 |
| 

callback

 | 

Callback<[ReadProgress](#section1841441192115)\>

 | 

Yes

 | 

Callback triggered when an interaction related to the playback progress occurs.

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

**Example**:

import { TextReader } from '@kit.SpeechKit';

try {
  TextReader.on('readProgress', (readProgress: TextReader.ReadProgress) => {
    console.info(\`Succeeded in setting readProgressListener: ${JSON.stringify(readProgress)}\`);
  });
} catch (e) {
  console.error(\`TextReader failed to set readProgressListener. Code: ${e.code}, message: ${e.message}\`);
}

#### off(type: 'readProgress')

off(type: 'readProgress', callback?: Callback<ReadProgress>): void

Unregisters a callback for the playback progress event, and will be used after **on(type: 'readProgress')** is called. You can register a new callback after the current one is unregistered.

**Atomic service API**: This API can be used in atomic services since API version 5.0.3(15).

**System capability**: SystemCapability.AI.Component.TextReader

**Start version**: 5.0.2(14)

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

Event type. The **'readProgress'** event type is supported.

 |
| 

callback

 | 

Callback<[ReadProgress](#section1841441192115)\>

 | 

No

 | 

Callback to be canceled, which must be the same as that passed upon subscription. If this parameter is not specified, all callbacks for listening to the event will be canceled. (Currently only one callback is used.)

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

**Example**:

import { TextReader } from '@kit.SpeechKit';

try {
  TextReader.off('readProgress');
} catch (e) {
  console.error(\`TextReader failed to unset readProgressListener. Code: ${e.code}, message: ${e.message}\`);
}

#### Person

Tone and style of a person.

**Atomic service API**: This API can be used in atomic services since API version 5.0.3(15).

**System capability**: SystemCapability.AI.Component.TextReader

**Start version**: 5.0.2(14)

| 
Name

 | 

**Type**

 | 

Read-Only

 | 

Optional

 | 

Description

 |
| :-- | :-- | :-- | :-- | :-- |
| 

tone

 | 

number

 | 

No

 | 

No

 | 

Tone of a person.

-   **0**: female

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

Style of a person.

-   **reading**: reading style (not supported currently)
-   **interaction-oral**: oral style (not supported currently)

-   **interaction-broadcast**: broadcast style

 |

#### ReaderParam

Reading parameters.

**Atomic service API**: This API can be used in atomic services since API version 5.0.3(15).

**System capability**: SystemCapability.AI.Component.TextReader

**Start version**: 5.0.0(12)

| 
Name

 | 

**Type**

 | 

Read-Only

 | 

Optional

 | 

Description

 |
| :-- | :-- | :-- | :-- | :-- |
| 

isVoiceBrandVisible

 | 

boolean

 | 

No

 | 

No

 | 

Indicates whether to display the brand information.

-   **false** (default): no
-   **true**: yes

 |
| 

businessBrandInfo

 | 

[BusinessBrandInfo](#section472059101210)

 | 

No

 | 

Yes

 | 

Brand information.

-   AI Reader is used by default.

 |
| 

isFastForward

 | 

boolean

 | 

No

 | 

Yes

 | 

Fast-forward and rewind logic.

-   **false** (default): by sentence
-   **true**: by 15 seconds

 |
| 

keepBackgroundRunning

 | 

boolean

 | 

No

 | 

Yes

 | 

Indicates whether the control keeps running in the background.

Reserved parameter, which is not supported currently.

To run the control in the background, set [the permission for a long-duration task](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/speech-textreader-guide#li56192364816).

 |
| 

online

 | 

number

 | 

No

 | 

Yes

 | 

Synthesis mode. The offline synthesis mode is used by default.

**0**: online (not supported currently); **1**: offline

 |
| 

person

 | 

[Person](#section114621915195719)

 | 

No

 | 

Yes

 | 

Tone and style of the speaker. The default settings are as follows:

{ tone: 0, style: 'interaction-broadcast' }

**Start version**: 5.0.2(14)

 |
| 

isMinibarNeeded

 | 

boolean

 | 

No

 | 

Yes

 | 

Indicates whether to use the minibar function.

-   **true** (default): yes
-   **false**: no. In this case, the **hideMinibar** and **showMinibar** methods cannot take effect.

**Start version**: 5.0.2(14)

 |
| 

minibarParams

 | 

[MinibarParams](#section1179835142719)

 | 

No

 | 

Yes

 | 

Minibar position setting. By default, it is set to attach to the left.

**Start version**: 5.0.2(14)

 |
| 

customFeatures

 | 

[CustomFeature\[\]](#section6103123551)

 | 

No

 | 

Yes

 | 

Custom features of the reading control. The parameter is empty by default.

**Start version**: 5.0.2(14)

 |
| 

displayTab

 | 

[DisplayTab](#section83763132116)

 | 

No

 | 

Yes

 | 

Tab page display configuration. By default, the cover and content pages are displayed.

**Start version**: 5.0.2(14)

 |
| 

reportProgressPeriod

 | 

number

 | 

No

 | 

Yes

 | 

Interval for returning the playback progress log information. The default value is **0**, indicating that no callback will be triggered.

Unit: millisecond

**Start version**: 5.0.2(14)

 |

#### StartParams

Parameters for starting playback through the reading control.

**System capability**: SystemCapability.AI.Component.TextReader

**Start version**: 5.0.2(14)

| 
Name

 | 

**Type**

 | 

Read-Only

 | 

Optional

 | 

Description

 |
| :-- | :-- | :-- | :-- | :-- |
| 

isMinibarHidden

 | 

boolean

 | 

No

 | 

Yes

 | 

Indicates whether to hide the minibar.

-   **false** (default): no
-   **true**: yes

**Atomic service API**: This API can be used in atomic services since API version 5.0.3(15).

 |
| 

callbackParam

 | 

string

 | 

No

 | 

Yes

 | 

Scene parameter that you can define, which will be returned through the callback for the **requestMore** event. It is empty by default.

**Atomic service API**: This API can be used in atomic services since API version 5.0.3(15).

 |
| 

startPercent

 | 

number

 | 

No

 | 

Yes

 | 

Start position of the playback. The value ranges from 0 to 100. The default value is **0**.

**Atomic service API**: This API can be used in atomic services since API version 6.0.1(21).

**Start version**: 6.0.1(21)

 |

#### MinibarParams

Parameters for controlling the minibar during playback startup. You can set the initial position of the minibar and the distance between the minibar and the bottom edge.

**System capability**: SystemCapability.AI.Component.TextReader

**Start version**: 5.0.2(14)

| 
Name

 | 

**Type**

 | 

Read-Only

 | 

Optional

 | 

Description

 |
| :-- | :-- | :-- | :-- | :-- |
| 

defaultAlignment

 | 

[BarAlignment](#section1031013101325)

 | 

No

 | 

No

 | 

Default attaching position of the minibar.

**Atomic service API**: This API can be used in atomic services since API version 5.0.3(15).

 |
| 

bottom

 | 

number

 | 

No

 | 

Yes

 | 

Distance between the minibar and the bottom edge. You can only drag the minibar leftward or rightward, not vertically.

The value must be greater than or equal to 0. The default value is **50**, in vp. The minibar will not be displayed if its position exceeds the screen area.

**Atomic service API**: This API can be used in atomic services since API version 5.0.3(15).

 |
| 

isSpeedIconVisible

 | 

boolean

 | 

No

 | 

Yes

 | 

Indicates whether the minibar displays the playback speed control button.

The default value **true** indicates yes.

The value **false** indicates no.

**Atomic service API**: This API can be used in atomic services since API version 6.0.1(21).

**Start version**: 6.0.1(21)

 |
| 

isNextIconVisible

 | 

boolean

 | 

No

 | 

Yes

 | 

Indicates whether the minibar displays the next article button.

The value **true** indicates yes.

The default value **false** indicates no.

**Atomic service API**: This API can be used in atomic services since API version 6.0.1(21).

**Start version**: 6.0.1(21)

 |

#### BusinessBrandInfo

Brand information.

**Atomic service API**: This API can be used in atomic services since API version 5.0.3(15).

**System capability**: SystemCapability.AI.Component.TextReader

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

panelName

 | 

string

 | 

No

 | 

Yes

 | 

-   Service name displayed on the top of the playback panel. Based on the standard system font size, each English character counts as one character and each Chinese character counts as two characters. If the total length exceeds 24 characters, the exceeding part will not be displayed. (When the system font size changes, the displayed length will change as well.)
-   The name will not be displayed on Pura X devices.

 |
| 

panelIcon

 | 

[ResourceStr](../../../../application-framework/arkui/arkts-components/common-definitions/basic-types/document.md#resourcestr)

 | 

No

 | 

Yes

 | 

Service icon displayed on the top of the playback panel.

Reserved parameter, which is not supported currently.

 |
| 

notificationIcon

 | 

[ResourceStr](../../../../application-framework/arkui/arkts-components/common-definitions/basic-types/document.md#resourcestr)

 | 

No

 | 

Yes

 | 

Service icon displayed on the notification bar.

Reserved parameter, which is not supported currently.

 |
| 

notificationName

 | 

string

 | 

No

 | 

Yes

 | 

Service name displayed on the notification bar.

Reserved parameter, which is not supported currently.

 |

#### ReadState

Reading status.

**Atomic service API**: This API can be used in atomic services since API version 5.0.3(15).

**System capability**: SystemCapability.AI.Component.TextReader

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

id

 | 

string

 | 

No

 | 

No

 | 

Article ID.

 |
| 

state

 | 

[ReadStateCode](../readstatecode-reading-status/document.md)

 | 

No

 | 

No

 | 

Current reading status.

 |
| 

categoryId

 | 

string

 | 

No

 | 

Yes

 | 

Article category ID.

**Start version**: 5.0.2(14)

 |
| 

isLastArticle

 | 

boolean

 | 

No

 | 

Yes

 | 

Playback by category:

Indicates whether the article being played is the last article in the category.

**true**: yes; **false**: no

Playback not by category:

Indicates whether it is the last article in the list.

**true**: yes; **false**: no

**Start version**: 5.0.2(14)

 |

#### CustomFeature

Custom features on the reading control panel.

**Atomic service API**: This API can be used in atomic services since API version 5.0.3(15).

**System capability**: SystemCapability.AI.Component.TextReader

**Start version**: 5.0.2(14)

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

[CustomFeatureType](#section1544534622617)

 | 

No

 | 

No

 | 

Type of a custom feature, which could be a system feature or a developer-defined feature.

 |
| 

name

 | 

string

 | 

No

 | 

No

 | 

Name of a custom feature.

When **type** is set to **CustomFeatureType.SYSTEM**, options for the supported system features include:

-   **favorite** (adding to favorites)
-   **countdown** (timer)

 |
| 

icon

 | 

[ResourceStr](../../../../application-framework/arkui/arkts-components/common-definitions/basic-types/document.md#resourcestr)

 | 

No

 | 

Yes

 | 

Icon of a custom feature, supporting formats such as URLs and local resources.

The value is empty by default.

When **type** is set to **CustomFeatureType.SYSTEM**, the icon for the system feature is fixed and does not need to be specified.

 |
| 

callback

 | 

Callback<string>

 | 

No

 | 

Yes

 | 

Callback of a custom feature. The callback parameter is the ID of the article that is being played.

 |

**Example**:

import { TextReader } from '@kit.SpeechKit';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct Index {
  // Obtain the app context.
  async aboutToAppear(): Promise<void> {
    const customFeaturesToAdd: TextReader.CustomFeature\[\] = \[
      {
        type: TextReader.CustomFeatureType.SYSTEM,
        name: 'countdown',
        icon: '',
        callback: (id) => {
          console.info(\`Custom feature callback.\`)
        }
      }
    \]
    const readerParams: TextReader.ReaderParam = {
      // Other field configurations.
      customFeatures: customFeaturesToAdd,
      isVoiceBrandVisible: false
    }
    let context: Context | undefined = this.getUIContext().getHostContext();
    if (context) {
      TextReader.init(context, readerParams).then(() => {
        console.info(\`TextReader succeeded in initializing.\`);
      }).catch((e: BusinessError) => {
        console.error(\`TextReader failed to initialize. Code: ${e.code}, message: ${e.message}\`);
      })
    }
  }

  build() {
  }
}

#### ReadInfo

Reading information.

**Atomic service API**: This API can be used in atomic services since API version 5.0.3(15).

**System capability**: SystemCapability.AI.Component.TextReader

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

id

 | 

string

 | 

No

 | 

No

 | 

Article ID, which cannot be an empty string.

 |
| 

title

 | 

[TextInfo](#section132871429177)

 | 

No

 | 

No

 | 

Title.

 |
| 

category

 | 

string

 | 

No

 | 

Yes

 | 

Category, which is empty by default.

 |
| 

author

 | 

[TextInfo](#section132871429177)

 | 

No

 | 

Yes

 | 

Author of an article, which is empty by default.

 |
| 

date

 | 

[TextInfo](#section132871429177)

 | 

No

 | 

Yes

 | 

Time of an article. Example: Mon Jul 08 2024 21:25:41 GMT+0800

Reserved parameter, which is not supported currently.

 |
| 

image

 | 

[image.PixelMap](../../../../media/image-kit/arkts-apis/ohos-multimedia-image-image-processing/interface-pixelmap/document.md)

 | 

No

 | 

Yes

 | 

Cover image. The maximum size of the image after being converted into PixelMap is 8 MB.

If this parameter is not passed, the default cover image will be used.

 |
| 

imageUrl

 | 

string

 | 

No

 | 

Yes

 | 

URL of the article cover image.

If this parameter is not passed, the default cover image will be used. If the image dimensions (width x height) exceed 1024 x 2048, the image will be compressed.

When both **image** and **imageUrl** are passed, the **image** parameter takes effect.

**Start version**: 5.0.2(14)

 |
| 

bodyInfo

 | 

string

 | 

No

 | 

Yes

 | 

This parameter is mandatory for the [setArticle](#section1658111564332) and [loadMore](#section1736815283116) APIs.

Body information for real-time reading.

If the body does not contain punctuations or newline characters, its length must be less than or equal to 10,000 characters.

 |
| 

bodyInfoObject

 | 

[BodyInfo](#section10646171225714)

 | 

No

 | 

Yes

 | 

Body content information, which is empty by default.

**Start version**: 5.0.2(14)

 |
| 

categoryObject

 | 

[CategoryInfo](#section13846143116387)

 | 

No

 | 

Yes

 | 

Article category information, which is empty by default.

**Start version**: 5.0.2(14)

 |
| 

audioInfo

 | 

[AudioInfo](#section12182184315243)\[\]

 | 

No

 | 

Yes

 | 

Audio information, which is empty by default.

If this parameter is set, the corresponding audio will be preferentially used for playback.

**Start version**: 5.0.2(14)

 |
| 

isFavorite

 | 

boolean

 | 

No

 | 

Yes

 | 

Indicates whether the article has been liked or added to favorites.

**true**: yes; **false**: no

The default value is **false**.

**Start version**: 5.0.2(14)

 |

#### CategoryInfo

Article category information.

**Atomic service API**: This API can be used in atomic services since API version 5.0.3(15).

**System capability**: SystemCapability.AI.Component.TextReader

**Start version**: 5.0.2(14)

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

id

 | 

string

 | 

No

 | 

No

 | 

Article category ID.

 |
| 

name

 | 

string

 | 

No

 | 

No

 | 

Article category name.

 |
| 

image

 | 

[image.PixelMap](../../../../media/image-kit/arkts-apis/ohos-multimedia-image-image-processing/interface-pixelmap/document.md) | string

 | 

No

 | 

No

 | 

Image (or the image URL) of an article category, whose priority is higher than that of the article cover image.

 |

#### TextInfo

Text information.

**Atomic service API**: This API can be used in atomic services since API version 5.0.3(15).

**System capability**: SystemCapability.AI.Component.TextReader

**Start version**: 5.0.0(12)

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

text

 | 

string

 | 

No

 | 

No

 | 

Text.

 |
| 

isClickable

 | 

boolean

 | 

No

 | 

No

 | 

Indicates whether the playback panel can be hidden through a tap.

-   **true**: yes
-   **false**: no

 |

#### BodyInfo

Body content of **readInfo**.

**Atomic service API**: This API can be used in atomic services since API version 5.0.3(15).

**System capability**: SystemCapability.AI.Component.TextReader

**Start version**: 5.0.2(14)

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

type

 | 

[BodyInfoType](#section1742241575911)

 | 

No

 | 

No

 | 

Type

 |
| 

body

 | 

string

 | 

No

 | 

Yes

 | 

Body content, which is empty by default.

 |

#### AudioInfo

Audio information in the reading control.

**Atomic service API**: This API can be used in atomic services since API version 5.0.3(15).

**System capability**: SystemCapability.AI.Component.TextReader

**Start version**: 5.0.2(14)

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

format

 | 

string

 | 

No

 | 

No

 | 

Audio format. For example, MP3, MP4A, WMA, and WAV.

 |
| 

duration

 | 

number

 | 

No

 | 

No

 | 

Audio duration, in seconds.

 |
| 

size

 | 

number

 | 

No

 | 

No

 | 

Audio information size, in bytes.

 |
| 

person

 | 

[Person](#section114621915195719)

 | 

No

 | 

Yes

 | 

Audio characteristics, including the timbre, style, and language.

The default values are as follows:

{ tone: 3, style: 'interaction-broadcast' }

 |
| 

url

 | 

string

 | 

No

 | 

No

 | 

Audio URL.

 |

#### ReadProgress

Audio information in the reading control.

**System capability**: SystemCapability.AI.Component.TextReader

**Start version**: 5.0.2(14)

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

id

 | 

string

 | 

No

 | 

No

 | 

ID of the article that is being played.

**Atomic service API**: This API can be used in atomic services since API version 5.0.3(15).

 |
| 

categoryId

 | 

string

 | 

No

 | 

No

 | 

Article category ID.

**Atomic service API**: This API can be used in atomic services since API version 5.0.3(15).

 |
| 

readProgressType

 | 

[ReadProgressType](#section6549172112810)

 | 

No

 | 

No

 | 

Periodical report type.

**Atomic service API**: This API can be used in atomic services since API version 5.0.3(15).

 |
| 

person

 | 

[Person](#section114621915195719)

 | 

No

 | 

No

 | 

Timbre used for the article being played.

**Atomic service API**: This API can be used in atomic services since API version 5.0.3(15).

 |
| 

maxPercent

 | 

number

 | 

No

 | 

No

 | 

Maximum playback percentage that the user has reached when this event callback is triggered, rather than the current playback percentage.

The value ranges from 0 to 100.

\[Calculation method\]

Maximum percentage of audio playback progress, which is rounded to the nearest whole percent. For example, when the audio playback progress has reached 80% and the user reverted the playback bar to 20% and then stopped the playback, it would be reported as **80**.

The value will be reset during replay.

**Atomic service API**: This API can be used in atomic services since API version 5.0.3(15).

 |
| 

currentPercent

 | 

number

 | 

No

 | 

No

 | 

Current playback percentage of the user when this event callback is triggered. The value ranges from 0 to 100. It can be used to record the last playback position and, together with the [start](#section147237941810) API, resume playback from where the user left off.

**Atomic service API**: This API can be used in atomic services since API version 6.0.1(21).

**Start version**: 6.0.1(21)

 |

#### PanelEvent

Playback panel event.

**Atomic service API**: This API can be used in atomic services since API version 5.0.3(15).

**System capability**: SystemCapability.AI.Component.TextReader

**Start version**: 5.0.0(12)

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

id

 | 

string

 | 

No

 | 

No

 | 

Article ID.

 |
| 

click

 | 

string

 | 

No

 | 

No

 | 

-   **BPC\_01**: tapping the playback button
-   **BPC\_02**: tapping the pause button
-   **BPC\_03**: tapping the previous button
-   **BPC\_04**: tapping the next button
-   **BPC\_05**: tapping the speed button
-   **BPC\_06**: tapping the timbre button
-   **BPC\_07**: tapping the reading list
-   **BPC\_08**: tapping the title
-   **BPC\_09**: tapping the author
-   **BPC\_10**: exiting the panel by tapping the arrow in the upper left corner or swiping down

 |
| 

categoryId

 | 

string

 | 

No

 | 

Yes

 | 

Article category ID.

**Start version**: 5.0.2(14)

 |

#### NotificationEvent

Notification bar event.

**Atomic service API**: This API can be used in atomic services since API version 5.0.3(15).

**System capability**: SystemCapability.AI.Component.TextReader

**Start version**: 5.0.0(12)

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

id

 | 

string

 | 

No

 | 

No

 | 

Article ID.

 |
| 

type

 | 

number

 | 

No

 | 

No

 | 

**1**: notification bar tap callback

**2**: media controller tap callback

 |
| 

click

 | 

string

 | 

No

 | 

No

 | 

-   **NBC\_01**: tapping the playback button
-   **NBC\_02**: tapping the pause button or removing the media controller from the notification bar
-   **NBC\_03**: tapping the close button (reserved and not supported for now)
-   **NBC\_04**: tapping the previous button
-   **NBC\_05**: tapping the next button
-   **NBC\_06**: tapping an image in an article (reserved)
-   **NBC\_07**: tapping the title of an article (reserved)

 |
| 

categoryId

 | 

string

 | 

No

 | 

Yes

 | 

Article category ID.

**Start version**: 5.0.2(14)

 |

#### ListEventState

List event status.

**Atomic service API**: This API can be used in atomic services since API version 5.0.3(15).

**System capability**: SystemCapability.AI.Component.TextReader

**Start version**: 5.0.0(12)

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

id

 | 

string

 | 

No

 | 

No

 | 

Article ID.

 |
| 

categoryId

 | 

string

 | 

No

 | 

Yes

 | 

Article category ID.

**Start version**: 5.0.2(14)

 |

#### ResetParamType

Enumeration class used to determine the reset type.

**Atomic service API**: This API can be used in atomic services since API version 5.0.3(15).

**System capability**: SystemCapability.AI.Component.TextReader

**Start version**: 5.0.2(14)

| 
Name

 | 

Value

 | 

Description

 |
| :-- | :-- | :-- |
| 

BAR\_PARAM

 | 

1

 | 

Minibar parameters.

 |
| 

ALL

 | 

2

 | 

All local data, including minibar parameters and the article list.

 |
| 

READ\_LIST

 | 

3

 | 

Article list.

 |

#### DisplayTab

Enumeration class used to determine the tabs displayed on the playback panel and their content.

**Atomic service API**: This API can be used in atomic services since API version 5.0.3(15).

**System capability**: SystemCapability.AI.Component.TextReader

**Device behavior differences**: This API has no effect on PCs/2-in-1 devices, but works properly on other devices.

**Start version**: 5.0.2(14)

| 
Name

 | 

Value

 | 

Description

 |
| :-- | :-- | :-- |
| 

COVER\_AND\_CONTENT

 | 

1

 | 

Cover page and content page, with tabs displayed.

 |
| 

CONTENT

 | 

2

 | 

Only the content page, without tabs.

 |
| 

COVER

 | 

3

 | 

Only the cover page, without tabs.

 |

#### BarAlignment

Enumeration class used to determine the default attaching position of the minibar.

**Atomic service API**: This API can be used in atomic services since API version 5.0.3(15).

**System capability**: SystemCapability.AI.Component.TextReader

**Start version**: 5.0.2(14)

| 
Name

 | 

Value

 | 

Description

 |
| :-- | :-- | :-- |
| 

LEFT

 | 

1

 | 

Attached to the left.

 |
| 

RIGHT

 | 

2

 | 

Attached to the right.

 |

#### BodyInfoType

Enumeration class used to determine the type of body information.

**Atomic service API**: This API can be used in atomic services since API version 5.0.3(15).

**System capability**: SystemCapability.AI.Component.TextReader

**Start version**: 5.0.2(14)

| 
Name

 | 

Value

 | 

Description

 |
| :-- | :-- | :-- |
| 

CONTENT

 | 

1

 | 

Body content.

 |
| 

FILE\_PATH

 | 

2

 | 

File path.

 |

#### CustomFeatureType

Enumeration class used to determine the type of a custom feature.

**Atomic service API**: This API can be used in atomic services since API version 5.0.3(15).

**System capability**: SystemCapability.AI.Component.TextReader

**Start version**: 5.0.2(14)

| 
Name

 | 

Value

 | 

Description

 |
| :-- | :-- | :-- |
| 

SYSTEM

 | 

1

 | 

Developer-defined feature.

 |
| 

USER

 | 

2

 | 

Custom feature.

 |

#### ReadProgressType

Enumeration class used to determine the type for reporting the playback progress.

**Atomic service API**: This API can be used in atomic services since API version 5.0.3(15).

**System capability**: SystemCapability.AI.Component.TextReader

**Start version**: 5.0.2(14)

| 
Name

 | 

Value

 | 

Description

 |
| :-- | :-- | :-- |
| 

PROGRESS

 | 

1

 | 

Reported periodically during playback.

 |
| 

PAUSE

 | 

2

 | 

Reported when the playback is paused.

 |
| 

STOP

 | 

3

 | 

Reported when the playback is stopped.

 |
| 

COMPLETED

 | 

4

 | 

Reported when the article is read completely.

 |
