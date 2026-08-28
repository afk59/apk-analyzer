# @system.mediaquery (Media Query)

The **mediaquery** module provides different styles for different media types.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/49/v3/_MvR2G77SX6KFhlX2x9LhQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062231Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=F0746B940FA9C6618A1187B7C787C859C960656C34C4F6F476962DEA1EE8F3F4)

-   The APIs of this module are no longer maintained since API version 7. You are advised to use [@ohos.mediaquery](../../ui/ohos-mediaquery-media-query/document.md) instead.
-   The initial APIs of this module are supported since API version 3. Newly added APIs will be marked with a superscript to indicate their earliest API version.

#### Modules to Import

import mediaquery from '@system.mediaquery';

#### MediaQuery

Defines the MediaQuery API.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

#### \[h2\]matchMedia

matchMedia(condition: string): MediaQueryList

Creates a **MediaQueryList** object based on the query condition.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| condition | string | Yes | Query condition. |

**Return value**

| Type | Description |
| :-- | :-- |
| [MediaQueryList](#mediaquerylist) | Attributes of the **MediaQueryList** object created. For details, see the descriptions below. |

**Example**

let mMediaQueryList = mediaquery.matchMedia('(max-width: 466)');

#### MediaQueryEvent

Defines a media query event.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Type | Optional | Description |
| :-- | :-- | :-- | :-- |
| matches | boolean | No | Matching result. The value **true** means that the query condition is met, and **false** means the opposite. |

#### MediaQueryList

Represents media query list information.

#### \[h2\]Properties

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| media | string | Yes | Yes | Serialized media query condition. |
| matches | boolean | Yes | Yes | Matching result. The value **true** means that the query condition is met, and **false** means the opposite. |
| onchange | (matches: boolean) => void | Yes | Yes | Callback invoked when the match result changes. **matches** indicates whether the media query condition is met. The value **true** means that the query condition is met, and **false** means the opposite. |

#### \[h2\]MediaQueryList.addListener

addListener(callback: (event: MediaQueryEvent) => void): void

Adds a listener for this **MediaQueryList** object. The listener must be added before **onShow** is called, that is, it must be added in the **onInit** or **onReady** API.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | (event: MediaQueryEvent) => void | Yes | Callback invoked when the query condition changes. |

**Example**

import mediaquery, { MediaQueryEvent } from '@system.mediaquery';
let mMediaQueryList = mediaquery.matchMedia('(max-width: 466)');

function maxWidthMatch(e: MediaQueryEvent): void {
  if(e.matches){
    // do something
  }
}
mMediaQueryList.addListener(maxWidthMatch);

#### \[h2\]MediaQueryList.removeListener

removeListener(callback: (event: MediaQueryEvent) => void): void

Removes the listener for this **MediaQueryList** object.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | (event: MediaQueryEvent) => void | Yes | Callback invoked when the query condition changes. |

**Example**

import mediaquery, { MediaQueryEvent } from '@system.mediaquery';
let mMediaQueryList = mediaquery.matchMedia('(max-width: 466)');

function maxWidthMatch(e: MediaQueryEvent): void {
  if(e.matches){
    // do something
  }
}
mMediaQueryList.removeListener(maxWidthMatch);
