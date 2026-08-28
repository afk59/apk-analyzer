# insightIntent

As a module of Intents Kit, **insightIntent** empowers apps and atomic services with the intent openness capabilities, including sharing and deleting **InsightIntent**. Apps or atomic services can call APIs of this module to share data with the system. Intents Kit analyzes shared data to identify patterns and recommends **InsightIntent** to users at the right time through the system access point. When users tap the recommended content, the system navigates to the corresponding page using an **InsightIntent** API declared by the app or atomic service.

For example, a video app uses **InsightIntent** to provide Intents Kit with the shared data (such as the time when a user watches videos every day and the video information) and the **InsightIntent** API. Intents Kit then recommends videos to the user via widgets at the scheduled time. After the user taps a widget, Intents Kit calls the **InsightIntent** API to play the video.

**Start version**: 4.0.0(10)

#### Module Import

import { insightIntent } from '@kit.IntentsKit';

#### InsightIntent

Represents an **InsightIntent** object, which includes the intent name, version number, identifier, action information, and entity information.

**Atomic service API**: This API can be used in atomic services since API version 5.0.0(12).

**System capability**: SystemCapability.AI.InsightIntent

**Start version**: 4.0.0(10)

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

intentName

 | 

string

 | 

No

 | 

No

 | 

Intent name, for example, **PlayMusic**.

 |
| 

intentVersion

 | 

string

 | 

No

 | 

No

 | 

Intent version. The current version is the initial version 1.0.

 |
| 

identifier

 | 

string

 | 

No

 | 

No

 | 

Intent identifier. It will be used as the unique identifier for a single data sharing record. You can customize intent identifiers based on your service requirements. You can generate an identifier using the UUID generation method, or create a random string based on the timestamp. Example: **52dac3b0-6520-4974-81e5-25f0879449b5**

 |
| 

intentActionInfo

 | 

[IntentActionInfo](#section13611343185915)

 | 

No

 | 

No

 | 

Intent execution information, for example, the time when an intent was executed or to be executed. For the sample code, please refer to that of [shareIntent](#section144826162913).

NOTE:

-   In version 4.0.0(10), the parameter type is **{\[key: string\]: Object}**.
-   Starting from version 5.0.0(12), the parameter type is [IntentActionInfo](#section13611343185915), which remains compatible with versions earlier than 5.0.0(12).

 |
| 

intentEntityInfo

 | 

[IntentEntityInfo](#section1934412225108)

 | 

No

 | 

No

 | 

Intent entity information, including the behavior and event. For the sample code, please refer to that of [shareIntent](#section144826162913).

NOTE:

-   In version 4.0.0(10), the parameter type is **{entityId: string; entityName: string; \[key: string\]: Object}**.
-   Starting from version 5.0.0(12), the parameter type is [IntentEntityInfo](#section1934412225108), which remains compatible with versions earlier than 5.0.0(12).

 |

#### IntentActionInfo

Represents the intent execution information.

**Atomic service API**: This API can be used in atomic services since API version 5.0.0(12).

**System capability**: SystemCapability.AI.InsightIntent

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

\[key: string\]

 | 

Object

 | 

No

 | 

No

 | 

Indicates that the value is an object containing one or more key-value pairs. The key is of the string type, and the value is of the Object type. The specific keys and values depend on the intent name. For details, please click [here](https://developer.huawei.com/consumer/cn/doc/service/intents-schema-0000001901962713).

 |

#### IntentEntityInfo

Represents intent entity information.

**Atomic service API**: This API can be used in atomic services since API version 5.0.0(12).

**System capability**: SystemCapability.AI.InsightIntent

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

entityId

 | 

string

 | 

No

 | 

No

 | 

Intent entity identifier. It will be used as the unique identifier for an entity. You can customize identifiers based on your service requirements. You can generate an identifier using the UUID generation method, or create a random string based on the timestamp. Example: **C10194368**

 |
| 

entityName

 | 

string

 | 

No

 | 

No

 | 

Intent entity name. For details about the value, please click [here](https://developer.huawei.com/consumer/cn/doc/service/intents-schema-0000001901962713).

 |
| 

\[key: string\]

 | 

Object

 | 

No

 | 

No

 | 

Other information about an intent entity, in the format of one or more key-value pairs. The key is of the string type, and the value is of the Object type. The specific keys and values depend on the intent name. For details, please click [here](https://developer.huawei.com/consumer/cn/doc/service/intents-schema-0000001901962713).

 |

#### insightIntent.shareIntent

shareIntent(context: common.BaseContext, intents: InsightIntent\[\], callback: AsyncCallback<void>): void

Shares an executed or expected **InsightIntent** object. This API returns the result asynchronously through a callback.

To prevent abuse of the sharing capability, each app can call the sharing API at most 20 times a day by default. If the number of sharings exceeds the upper limit, error code **1000101104** will be returned. The number of data records shared each time is not limited. However, the size of data shared each time cannot exceed 50 KB. If the data size shared each time exceeds the limit, error code **1000101105** will be returned. The maximum number of daily sharings for all callers is 3000. If this limit is exceeded, error code **1000101106** will be returned. You are advised to accumulate a certain amount of data and then share the accumulated data at a time. In addition, you need to control the number of sharings.

**Atomic service API**: This API can be used in atomic services since API version 5.0.0(12).

**System capability**: SystemCapability.AI.InsightIntent

**Start version**: 4.0.0(10)

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

context

 | 

common.[BaseContext](../../../../application-framework/ability-kit/arkts-apis/dependent-elements-and-definitions/application/basecontext/document.md)

 | 

Yes

 | 

App context.

 |
| 

intents

 | 

[InsightIntent](#section1081123302517)\[\]

 | 

Yes

 | 

**InsightIntent** object to share.

 |
| 

callback

 | 

AsyncCallback<void>

 | 

Yes

 | 

Callback function. When a specific operation (as described in the API function) is successful, **err** is **undefined**; otherwise, an error object is returned.

 |

**Error codes:**

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

1000101101

 | 

The application has not been registered with the InsightIntent.

 |
| 

1000101104

 | 

The number of sharing times exceeds the limit.

 |
| 

1000101105

 | 

The size of a single shared data exceeds the limit.

 |
| 

1000101106

 | 

Exceeded the maximum number of sharing times of all applications.

 |
| 

1000101201

 | 

The service is abnormal.

 |

**Example:**

let playMusicIntent: insightIntent.InsightIntent = {
  intentName: 'PlayMusic',
  intentVersion: '1.0',
  identifier: '52dac3b0-6520-4974-81e5-25f0879449b5',
  intentActionInfo: {
    actionMode: 'EXECUTED',
    currentPercentage: 50,
    executedTimeSlots: {
      executedEndTime: 1637393112000,
      executedStartTime: 1637393212000
    }
  },
  intentEntityInfo: {
    entityName: 'Music',
    entityId: 'C10194368',
    entityGroupId: 'Popular',
    displayName: 'Song name',
    description: 'Song description',
    logoURL: 'https://www-file.abc.com/-/media/corporate/images/home/logo/abc\_logo.png',
    keywords: \['HUAWEI Music','Makeup'\],
    rankingHint: 99,
    expirationDate: 1637393212000,
    metadataModificationDate: 1637393212000,
    activityType: \['1', '2', '3'\],
    artist: \['Tom','Jack'\],
    lyricist: \['Tom','Jack'\],
    composer: \['Tom','Jack'\],
    albumName: 'Album name',
    duration: 123456789,
    playCount: 456213123,
    musicalGenre: \['Folk style','Rock & roll'\],
    isPublicData: false
  }
}
try {
  // Share data.
  // Pass a proper context based on the code context.
  insightIntent.shareIntent(context, \[playMusicIntent\], (error) => {
    if (error?.code) {
      // Handle the business logic error.
      console.error(\`shareIntent failed, error.code: ${error?.code}, error.message: ${error?.message}\`);
      return;
    }
    // Execute the normal business logic.
    console.info('shareIntent succeed');
  });
} catch (error) {
  // Handle exceptions.
  console.error(\`error.code: ${error?.code}, error.message: ${error?.message}\`);
}

#### insightIntent.shareIntent

shareIntent(context: common.BaseContext, intents: InsightIntent\[\]): Promise<void>

Shares an executed or expected **InsightIntent** object. This API returns the result asynchronously through a promise.

To prevent abuse of the sharing capability, each app can call the sharing API at most 20 times a day by default. If the number of sharings exceeds the upper limit, error code **1000101104** will be returned. The number of data records shared each time is not limited. However, the size of data shared each time cannot exceed 50 KB. If the data size shared each time exceeds the limit, error code **1000101105** will be returned. The maximum number of daily sharings for all callers is 3000. If this limit is exceeded, error code **1000101106** will be returned. You are advised to accumulate a certain amount of data and then share the accumulated data at a time. In addition, you need to control the number of sharings.

**Atomic service API**: This API can be used in atomic services since API version 5.0.0(12).

**System capability**: SystemCapability.AI.InsightIntent

**Start version**: 4.0.0(10)

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

context

 | 

common.[BaseContext](../../../../application-framework/ability-kit/arkts-apis/dependent-elements-and-definitions/application/basecontext/document.md)

 | 

Yes

 | 

App context.

 |
| 

intents

 | 

[InsightIntent](#section1081123302517)\[\]

 | 

Yes

 | 

**InsightIntent** object to share.

 |

**Returns:**

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

Promise<void>

 | 

Promise that returns no value.

 |

**Error codes:**

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

1000101101

 | 

The application has not been registered with the InsightIntent.

 |
| 

1000101104

 | 

The number of sharing times exceeds the limit.

 |
| 

1000101105

 | 

The size of a single shared data exceeds the limit.

 |
| 

1000101106

 | 

Exceeded the maximum number of sharing times of all applications.

 |
| 

1000101201

 | 

The service is abnormal.

 |

**Example:**

import { BusinessError } from '@kit.BasicServicesKit';

let playMusicIntent: insightIntent.InsightIntent = {
  intentName: 'PlayMusic',
  intentVersion: '1.0',
  identifier: '52dac3b0-6520-4974-81e5-25f0879449b5',
  intentActionInfo: {
    actionMode: 'EXECUTED',
    currentPercentage: 50,
    executedTimeSlots: {
      executedEndTime: 1637393112000,
      executedStartTime: 1637393212000
    }
  },
  intentEntityInfo: {
    entityName: 'Music',
    entityId: 'C10194368',
    entityGroupId: 'Popular',
    displayName: 'Song name',
    description: 'Song description',
    logoURL: 'https://www-file.abc.com/-/media/corporate/images/home/logo/abc\_logo.png',
    keywords: \['HUAWEI Music','Makeup'\],
    rankingHint: 99,
    expirationDate: 1637393212000,
    metadataModificationDate: 1637393212000,
    activityType: \['1', '2', '3'\],
    artist: \['Tom','Jack'\],
    lyricist: \['Tom','Jack'\],
    composer: \['Tom','Jack'\],
    albumName: 'Album name',
    duration: 123456789,
    playCount: 456213123,
    musicalGenre: \['Folk style','Rock & roll'\],
    isPublicData: false
  }
}

// Share data.
// Pass a proper context based on the code context.
insightIntent.shareIntent(context, \[playMusicIntent\]).then(() => {
  console.info('shareIntent succeed');
}).catch((err: BusinessError) => {
  console.error(\`error.code: ${err?.code}, failed because ${err?.message}\`);
});

#### insightIntent.deleteIntent

deleteIntent(context: common.BaseContext, intentName: string, identifiers: string\[\], callback: AsyncCallback<void>): void

Deletes an **InsightIntent** object. If the **identifiers** parameter is set, the records corresponding to the specified identifiers under the intent name will be deleted. Otherwise, all records under the intent name will be deleted. This API returns the result through a callback.

**Atomic service API**: This API can be used in atomic services since API version 5.0.0(12).

**System capability**: SystemCapability.AI.InsightIntent

**Start version**: 4.0.0(10)

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

context

 | 

common.[BaseContext](../../../../application-framework/ability-kit/arkts-apis/dependent-elements-and-definitions/application/basecontext/document.md)

 | 

Yes

 | 

App context.

 |
| 

intentName

 | 

string

 | 

Yes

 | 

Intent name.

 |
| 

identifiers

 | 

string\[\]

 | 

Yes

 | 

Intent identifier.

 |
| 

callback

 | 

AsyncCallback<void>

 | 

Yes

 | 

Callback used to return the result.

 |

**Error codes:**

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

1000101101

 | 

The application has not been registered with the InsightIntent.

 |
| 

1000101201

 | 

The service is abnormal.

 |

**Example:**

try {
   // Delete certain records under the intent name.
  // Pass a proper context based on the code context.
  insightIntent.deleteIntent(context, 'PlayMusic', \['52dac3b0-6520-4974-81e5-25f0879449b5'\], (error) => {
    if (error?.code) {
      // Handle the business logic error.
      console.error(\`deleteIntent failed, error.code: ${error?.code}, error.message: ${error?.message}\`);
      return;
    }
    // Execute the normal business logic.
    console.info('deleteIntent succeed');
  });
} catch (error) {
  // Handle exceptions.
  console.error(\`error.code: ${error?.code}, error.message: ${error?.message}\`);
}

#### insightIntent.deleteIntent

deleteIntent(context: common.BaseContext, intentName: string, callback: AsyncCallback<void>): void

Deletes an **InsightIntent** object. All records under the intent name will be deleted. This API returns the result through a callback.

**Atomic service API**: This API can be used in atomic services since API version 5.0.0(12).

**System capability**: SystemCapability.AI.InsightIntent

**Start version**: 4.0.0(10)

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

context

 | 

common.[BaseContext](../../../../application-framework/ability-kit/arkts-apis/dependent-elements-and-definitions/application/basecontext/document.md)

 | 

Yes

 | 

App context.

 |
| 

intentName

 | 

string

 | 

Yes

 | 

Intent name.

 |
| 

callback

 | 

AsyncCallback<void>

 | 

Yes

 | 

Callback used to return the result.

 |

**Error codes:**

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

1000101101

 | 

The application has not been registered with the InsightIntent.

 |
| 

1000101201

 | 

The service is abnormal.

 |

**Example:**

try {
  // Delete all data of the intent.
  // Pass a proper context based on the code context.
  insightIntent.deleteIntent(context, 'PlayMusic', (error) => {
    if (error?.code) {
      // Handle the business logic error.
      console.error(\`deleteIntent failed, error.code: ${error?.code}, error.message: ${error?.message}\`);
      return;
    }
    // Execute the normal business logic.
    console.info('deleteIntent succeed');
  });
} catch (error) {
  // Handle exceptions.
  console.error(\`error.code: ${error?.code}, error.message: ${error?.message}\`);
}

#### insightIntent.deleteIntent

deleteIntent(context: common.BaseContext, intentName: string, identifiers?: string\[\]): Promise<void>

Deletes an **InsightIntent** object. If the **identifiers** parameter is set, the records corresponding to the specified identifiers under the intent name will be deleted. Otherwise, all records under the intent name will be deleted. This API returns the result through a promise.

**Atomic service API**: This API can be used in atomic services since API version 5.0.0(12).

**System capability**: SystemCapability.AI.InsightIntent

**Start version**: 4.0.0(10)

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

context

 | 

common.[BaseContext](../../../../application-framework/ability-kit/arkts-apis/dependent-elements-and-definitions/application/basecontext/document.md)

 | 

Yes

 | 

App context.

 |
| 

intentName

 | 

string

 | 

Yes

 | 

Intent name.

 |
| 

identifiers

 | 

string\[\]

 | 

No

 | 

Intent identifier. If this parameter is set, the records corresponding to the specified identifiers under the intent name will be deleted. Otherwise, all records under the intent name will be deleted.

 |

**Returns:**

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

Promise<void>

 | 

Promise that returns no value.

 |

**Error codes:**

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

1000101101

 | 

The application has not been registered with the InsightIntent.

 |
| 

1000101201

 | 

The service is abnormal.

 |

**Example:**

import { BusinessError } from '@kit.BasicServicesKit';

// Delete certain records under the intent name.
// Pass a proper context based on the code context.
insightIntent.deleteIntent(context, 'PlayMusic', \['52dac3b0-6520-4974-81e5-25f0879449b5'\]).then(() => {
  console.info('deleteIntent succeed');
}).catch((err: BusinessError) => {
  console.error(\`error.code: ${err?.code}, failed because ${err?.message}\`);
});

#### insightIntent.deleteEntity

deleteEntity(context: common.BaseContext, entityName: string, entityIds: string\[\], callback: AsyncCallback<void>): void

Deletes an **InsightIntent** entity by entity ID under an entity name. This API returns the result through a callback.

**Atomic service API**: This API can be used in atomic services since API version 5.0.0(12).

**System capability**: SystemCapability.AI.InsightIntent

**Start version**: 4.0.0(10)

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

context

 | 

common.[BaseContext](../../../../application-framework/ability-kit/arkts-apis/dependent-elements-and-definitions/application/basecontext/document.md)

 | 

Yes

 | 

App context.

 |
| 

entityName

 | 

string

 | 

Yes

 | 

Entity name.

 |
| 

entityIds

 | 

string\[\]

 | 

Yes

 | 

Entity ID.

 |
| 

callback

 | 

AsyncCallback<void>

 | 

Yes

 | 

Callback used to return the result.

 |

**Error codes:**

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

1000101101

 | 

The application has not been registered with the InsightIntent.

 |
| 

1000101201

 | 

The service is abnormal.

 |

**Example:**

try {
  // Delete entity data.
  // Pass a proper context based on the code context.
  insightIntent.deleteEntity(context, 'PlayMusic', \['a5c9e9e3-3d0a-4e6a-9f3d-6b7c6b8d6b9f'\], (error) => {
    if (error?.code) {
      // Handle the business logic error.
      console.error(\`deleteEntity failed, error.code: ${error?.code}, error.message: ${error?.message}\`);
      return;
    }
    // Execute the normal business logic.
    console.info('deleteEntity succeed');
  });
} catch (error) {
  // Handle exceptions.
  console.error(\`error.code: ${error?.code}, error.message: ${error?.message}\`);
}

#### insightIntent.deleteEntity

deleteEntity(context: common.BaseContext, entityName: string, entityIds: string\[\]): Promise<void>

Deletes an **InsightIntent** entity by entity ID under an entity name. This API returns the result asynchronously through a promise.

**Atomic service API**: This API can be used in atomic services since API version 5.0.0(12).

**System capability**: SystemCapability.AI.InsightIntent

**Start version**: 4.0.0(10)

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

context

 | 

common.[BaseContext](../../../../application-framework/ability-kit/arkts-apis/dependent-elements-and-definitions/application/basecontext/document.md)

 | 

Yes

 | 

App context.

 |
| 

entityName

 | 

string

 | 

Yes

 | 

Entity name.

 |
| 

entityIds

 | 

string\[\]

 | 

Yes

 | 

Entity ID.

 |

**Returns:**

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

Promise<void>

 | 

Promise that returns no value.

 |

**Error codes:**

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

1000101101

 | 

The application has not been registered with the InsightIntent.

 |
| 

1000101201

 | 

The service is abnormal.

 |

**Example:**

import { BusinessError } from '@kit.BasicServicesKit';

// Delete entity data.
// Pass a proper context based on the code context.
insightIntent.deleteEntity(context, 'PlayMusic', \['a5c9e9e3-3d0a-4e6a-9f3d-6b7c6b8d6b9f'\]).then(() => {
  console.info('deleteEntity succeed');
}).catch((err: BusinessError) => {
  console.error(\`error.code: ${err?.code}, failed because ${err?.message}\`);
});

#### insightIntent.getSid

getSid(context: common.BaseContext, renew: boolean): Promise<string>

Obtains the Service Open ID (SID). This API returns the result asynchronously through a promise.

**Atomic service API**: This API can be used in atomic services since API version 5.0.0(12).

**System capability**: SystemCapability.AI.InsightIntent

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

context

 | 

common.[BaseContext](../../../../application-framework/ability-kit/arkts-apis/dependent-elements-and-definitions/application/basecontext/document.md)

 | 

Yes

 | 

App context.

 |
| 

renew

 | 

boolean

 | 

Yes

 | 

Indicates whether to forcibly obtain a new SID from the cloud. If the value is **true**, a new SID will be obtained from the cloud. If the value is **false**, the locally stored one will be preferentially obtained.

 |

**Returns:**

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

Promise<string>

 | 

SID returned through a promise.

 |

**Error codes:**

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

1000101101

 | 

The application has not been registered with the InsightIntent.

 |
| 

1000101102

 | 

HUAWEI Assistant has stopped providing services.

 |
| 

1000101107

 | 

Too many Service Open ID renew requests.

 |
| 

1000101201

 | 

The service is abnormal.

 |

**Example:**

import { BusinessError } from '@kit.BasicServicesKit';

// Obtain the SID.
// Pass a proper context based on the code context.
insightIntent.getSid(context, false).then((sid: string) => {
  console.info('getSid succeed!');
}).catch((err: BusinessError) => {
  console.error(\`error.code: ${err?.code}, failed because ${err?.message}\`);
});
