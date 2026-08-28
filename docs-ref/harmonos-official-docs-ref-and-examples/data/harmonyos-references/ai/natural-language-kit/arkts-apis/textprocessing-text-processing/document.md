# textProcessing (Text Processing)

Natural Language Kit annotates all input plain text as part-of-speech tags, indicating whether each word is a noun, verb, adjective, or other part of speech.

It also extracts entities from the input text and classifies them into different types. The output results contain the entity type, location of an entity in the input text, original text of the entity, and other parameters obtained in entity parsing. For details about entity parameters, please refer to [EntityType](#section4298938144913).

**Start version**: 5.0.0(12)

#### Module Import

import { textProcessing, EntityType } from '@kit.NaturalLanguageKit';

#### WordSegment

Word segmentation output, including words and parts of speech.

**System capability**: SystemCapability.AI.NaturalLanguage.TextProcessing

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

word

 | 

string

 | 

No

 | 

No

 | 

Word.

 |
| 

wordTag

 | 

string

 | 

No

 | 

No

 | 

Part-of-speech. **wordTag** is applicable only to Chinese texts. It is for reference only when it comes to English texts.

 |

#### EntityConfig

Entity type, which is optional.

**System capability**: SystemCapability.AI.NaturalLanguage.TextProcessing

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

entityTypes

 | 

[EntityType](#section4298938144913)\[\]

 | 

No

 | 

Yes

 | 

Type of an entity.

By default, all options are selected.

 |

#### EntityType

Entity type enumeration class.

**System capability**: SystemCapability.AI.NaturalLanguage.TextProcessing

**Start version**: 5.0.0(12)

| 
Name

 | 

Value

 | 

Description

 |
| :-- | :-- | :-- |
| 

DATETIME

 | 

datetime

 | 

Date and time.

 |
| 

EMAIL

 | 

email

 | 

Email address.

 |
| 

EXPRESS\_NO

 | 

expressNo

 | 

Courier number.

 |
| 

FLIGHT\_NO

 | 

flightNo

 | 

Flight number.

 |
| 

LOCATION

 | 

location

 | 

Location.

 |
| 

NAME

 | 

name

 | 

Name.

 |
| 

PHONE\_NO

 | 

phoneNo

 | 

Mobile number.

 |
| 

URL

 | 

url

 | 

URL.

 |
| 

VERIFICATION\_CODE

 | 

verificationCode

 | 

Verification code.

 |
| 

ID\_NO

 | 

idNo

 | 

ID card number.

 |

#### Entity

Entity extraction result.

**System capability**: SystemCapability.AI.NaturalLanguage.TextProcessing

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

text

 | 

string

 | 

No

 | 

No

 | 

Original text.

 |
| 

charOffset

 | 

number

 | 

No

 | 

No

 | 

Location of an entity in the original text. The location is calculated in characters.

 |
| 

type

 | 

[EntityType](#section4298938144913)

 | 

No

 | 

No

 | 

Type of an entity.

 |
| 

jsonObject

 | 

string

 | 

No

 | 

No

 | 

Other parameters about an entity.

**jsonObject** is applicable only to Chinese texts. It is for reference only when it comes to English texts.

 |

#### textProcessing.getWordSegment

getWordSegment(text: string): Promise<Array<WordSegment>>

Creates a word segmentation instance and initializes the engine. This API returns the result asynchronously through a promise.

**System capability**: SystemCapability.AI.NaturalLanguage.TextProcessing

**Start version**: 5.0.0(12)

**Parameters**:

| 
Parameter

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

Text to be analyzed. For details about the specifications, please refer to [Restrictions](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/natural-language-introduction#section1454714381942).

 |

**Returns**:

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

Promise<Array<[WordSegment](#section12706154134017)\>>

 | 

Promise object, which returns a set of word segmentation results.

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

200

 | 

Run timed out, please try again later.

 |
| 

401

 | 

The parameter check failed.

 |
| 

1011200001

 | 

Failed to run, please try again.

 |
| 

1011200002

 | 

The service is abnormal.

 |

**Example**:

import { textProcessing } from '@kit.NaturalLanguageKit'
import { BusinessError } from '@kit.BasicServicesKit';

function testWordSegment(inputText: string) {
  textProcessing.getWordSegment(inputText)
    .then(result => {
      let outputText = formatWordSegmentResult(result);
      console.info('NLUDemo', \`getWordSegment result:${outputText}\`);
    })
    .catch((err: BusinessError) => {
      console.error('NLUDemo', \`getWordSegment errorCode: ${err.code} errorMessage: ${err.message}\`);
    });
}

function formatWordSegmentResult(segments: textProcessing.WordSegment\[\]): string {
  let output = 'Word Segments:\\n';
  segments.forEach((segment, index) => {
    output += \`Word\[${index}\]: ${segment.word}, Tag: ${segment.wordTag}\\n\`;
  });
  return output;
}

@Entry
@Component
struct Page {

  build() {
    Column(){
      Button('Start').onClick(() => {
// Test text word segmentation.
        let inputText = 'test for nlp word segment';
        testWordSegment(inputText);
      })
    }
  }
}

#### textProcessing.getEntity

getEntity(text: string, entityConfig?: EntityConfig): Promise<Array<Entity>>

Creates an entity extraction instance and initializes the engine. This API returns the result asynchronously through a promise.

**System capability**: SystemCapability.AI.NaturalLanguage.TextProcessing

**Start version**: 5.0.0(12)

**Parameters:**

| 
Parameter

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

Input string. For details about the specifications, please refer to [Restrictions](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/natural-language-introduction#section1454714381942).

 |
| 

entityConfig

 | 

[EntityConfig](#section7467975499)

 | 

No

 | 

Entity type.

By default, all options are selected. You are advised to load entity types on demand to improve app performance.

 |

**Returns**:

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

Promise<Array<[Entity](#section1518613358392)\>>

 | 

Promise object, which returns the entity set.

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

200

 | 

Run timed out, please try again later.

 |
| 

401

 | 

The parameter check failed.

 |
| 

1011200001

 | 

Failed to run, please try again.

 |
| 

1011200002

 | 

The service is abnormal.

 |

**Example**:

import { textProcessing, EntityType } from '@kit.NaturalLanguageKit';
import { BusinessError } from '@kit.BasicServicesKit';

function testEntityRecognition(inputText: string) {
  textProcessing.getEntity(inputText, {
    entityTypes: \[EntityType.NAME\]
  }).then(result => {
    let outputText = formatEntityResult(result);
    console.info('NLUDemo', \`getEntity result:${outputText}\`);
  }).catch((err: BusinessError) => {
    console.error('NLUDemo', \`getEntity errorCode: ${err.code} errorMessage: ${err.message}\`);
  })
}

function formatEntityResult(entities: textProcessing.Entity\[\]): string {
  if (!entities || !entities.length) {
    return 'No entities found.';
  }

  let output = 'Entities:\\n';
  for (let i = 0; i < entities.length; i++) {
    let entity = entities\[i\];
    output += \`Entity\[${i}\]:\\n\`;
    output += \`  oriText: ${entity.text}\\n\`;
    output += \`  charOffset: ${entity.charOffset}\\n\`;
    output += \`  entityType: ${entity.type}\\n\`;
    output += \`  jsonObject: ${entity.jsonObject}\\n\\n\`;
  }
  return output;
}

@Entry
@Component
struct Page {

  build() {
    Column(){
      Button('Start').onClick(() => {
// Test entity recognition.
        let inputText = 'test for nlp getEntity. Mary, Bob and Mike.';
        testEntityRecognition(inputText);
      })
    }
  }
}

#### textProcessing.init

init(): Promise<boolean>

Initializes the natural language processing engine. This API returns the result asynchronously through a promise.

**System capability**: SystemCapability.AI.NaturalLanguage.TextProcessing

**Start version**: 5.0.0(12)

**Returns**:

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

Promise<boolean>

 | 

Promise object, indicating whether initialization is successful. The values are **true** (yes) and **false** (no).

 |

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ec/v3/OcnY8iXATmOMXefoDPYKYA/caution_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062524Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=D04A7DA334BA2F2A2DA31F5D854DC0F46622A206B26FB0F8290FED44E493DF5A)

The initialization API is optional. If you are using the API proactively, call this API in advance to reduce the delay for calling the text processing capability for the first time.

**Error codes**:

For details about the error codes, please refer to [ArkTS API Error Codes](../arkts-api-error-codes/document.md).

| 
Error Code

 | 

Error Message

 |
| :-- | :-- |
| 

200

 | 

Run timed out, please try again later.

 |
| 

1011200001

 | 

Failed to run, please try again.

 |
| 

1011200002

 | 

The service is abnormal.

 |

**Example**:

import { textProcessing } from '@kit.NaturalLanguageKit';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct Page {

  build() {
    Column(){
      Button('init').onClick(() => {
        textProcessing.init().then(result => {
        console.info(\`textProcess init result: ${result}\`)
      }).catch((err: BusinessError) => {
        console.error(\`textProcess init failed errorCode: ${err.code} errorMessage: ${err.message}\`);
      })
      })
    }
  }
}

#### textProcessing.release

release(): Promise<boolean>

Releases the engine. This API returns the result asynchronously through a promise.

**System capability**: SystemCapability.AI.NaturalLanguage.TextProcessing

**Start version**: 5.0.0(12)

**Returns**:

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

Promise<boolean>

 | 

Promise object, which indicates whether the engine is successfully released. The values are **true** (yes) and **false** (no).

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

200

 | 

Run timed out, please try again later.

 |
| 

1011200001

 | 

Failed to run, please try again.

 |
| 

1011200002

 | 

The service is abnormal.

 |

**Example**:

import { textProcessing } from '@kit.NaturalLanguageKit';

async function runTextProcessing() {
  await textProcessing.init();
  console.info('Text processing initialized successfully');

  try {
    const result = await textProcessing.release();
    console.info(\`textProcess release result: ${result}\`);
  } catch (err) {
    console.error(\`textProcess release failed errorCode: ${err.code} errorMessage: ${err.message}\`);
  }
}

@Entry
@Component
struct Page {

  build() {
    Column(){
      Button('Start').onClick(() => {
        void runTextProcessing()
      })
    }
  }
}
