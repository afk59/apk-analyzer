# Functions

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f2/v3/bZyc3VAKTgeVG8mRawmqRA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062423Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=91B9812D27252E367451899D392391C9C066982B461185057E724CDE2ED27458)

The initial APIs of this module are supported since API version 9. Newly added APIs will be marked with a superscript to indicate their earliest API version.

#### Modules to Import

import { avSession } from '@kit.AVSessionKit';

#### avSession.createAVSession10+

createAVSession(context: Context, tag: string, type: AVSessionType): Promise<AVSession>

Creates an AVSession. This API uses a promise to return the result. An application process can have only one AVSession, and repeated calling of this API fails.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Multimedia.AVSession.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| context | [Context](../../../../../application-framework/ability-kit/arkts-apis/fa-model/app/context-context-base-class-of-the-fa-model/document.md) | Yes | Context of the UIAbility, which is used to obtain information about the application component. |
| tag | string | Yes | Custom session name. |
| type | [AVSessionType](../types/document.md#avsessiontype10) | Yes | Session type. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<[AVSession](../interface-avsession/document.md)\> | Promise used to return the AVSession obtained, which can be used to obtain the session ID, set the metadata and playback state information, and send key events. |

**Error codes**

For details about the error codes, see [AVSession Management Error Codes](../../../error-codes/avsession-management-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | parameter check failed. 1.Mandatory parameters are left unspecified. 2.Parameter verification failed. |
| 6600101 | Session service exception. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';
import { avSession } from '@kit.AVSessionKit';
@Entry
@Component
struct Index {
  @State message: string = 'hello world';

  build() {
    Column() {
        Text(this.message)
          .onClick(()=>{
            let currentAVSession: avSession.AVSession;
            let tag = "createNewSession";
            let context: Context = this.getUIContext().getHostContext() as Context;
            let sessionId: string;  // Used as an input parameter of subsequent functions.

            avSession.createAVSession(context, tag, "audio").then(async (data: avSession.AVSession) => {
            currentAVSession = data;
            sessionId = currentAVSession.sessionId;
            console.info(\`CreateAVSession : SUCCESS : sessionId = ${sessionId}\`);
            }).catch((err: BusinessError) => {
            console.error(\`CreateAVSession BusinessError: code: ${err.code}, message: ${err.message}\`);
            });
          })
      }
    .width('100%')
    .height('100%')
  }
}

#### avSession.createAVSession10+

createAVSession(context: Context, tag: string, type: AVSessionType, callback: AsyncCallback<AVSession>): void

Creates an AVSession. This API uses an asynchronous callback to return the result. An application process can have only one AVSession, and repeated calling of this API fails.

**System capability**: SystemCapability.Multimedia.AVSession.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| context | [Context](../../../../../application-framework/ability-kit/arkts-apis/fa-model/app/context-context-base-class-of-the-fa-model/document.md) | Yes | Context of the UIAbility, which is used to obtain information about the application component. |
| tag | string | Yes | Custom session name. |
| type | [AVSessionType](../types/document.md#avsessiontype10) | Yes | Session type. |
| callback | AsyncCallback<[AVSession](../interface-avsession/document.md)\> | Yes | Callback used to return the AVSession obtained, which can be used to obtain the session ID, set the metadata and playback state information, and send key events. |

**Error codes**

For details about the error codes, see [AVSession Management Error Codes](../../../error-codes/avsession-management-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | parameter check failed. 1.Mandatory parameters are left unspecified. 2.Parameter verification failed. |
| 6600101 | Session service exception. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';
import { avSession } from '@kit.AVSessionKit';
@Entry
@Component
struct Index {
  @State message: string = 'hello world';

  build() {
    Column() {
      Text(this.message)
        .onClick(()=>{
          let currentAVSession: avSession.AVSession;
          let tag = "createNewSession";
          let context: Context = this.getUIContext().getHostContext() as Context;
          let sessionId: string;  // Used as an input parameter of subsequent functions.

          avSession.createAVSession(context, tag, "audio", async (err: BusinessError, data: avSession.AVSession) => {
            if (err) {
              console.error(\`CreateAVSession BusinessError: code: ${err.code}, message: ${err.message}\`);
            } else {
              currentAVSession = data;
              sessionId = currentAVSession.sessionId;
              console.info(\`CreateAVSession : SUCCESS : sessionId = ${sessionId}\`);
            }
          });
        })
    }
    .width('100%')
    .height('100%')
  }
}

#### avSession.getAVSession22+

getAVSession(context: Context): Promise<AVSession>

Obtains an AVSession object. This API uses a promise to return the result.

This API returns an existing AVSession object that was previously created in the current process. If no AVSession object exists, the call fails and an exception is thrown.

**Atomic service API**: This API can be used in atomic services since API version 22.

**System capability**: SystemCapability.Multimedia.AVSession.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| context | [Context](../../../../../application-framework/ability-kit/arkts-apis/fa-model/app/context-context-base-class-of-the-fa-model/document.md) | Yes | Context of the UIAbility, which is used to obtain information about the application component. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<[AVSession](../interface-avsession/document.md)\> | Promise used to return the AVSession obtained, which can be used to obtain the session ID, set the metadata and playback state information, and send key events. |

**Error codes**

For details about the error codes, see [AVSession Management Error Codes](../../../error-codes/avsession-management-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 6600101 | Session service exception. |
| 6600102 | The session does not exist. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';
import { avSession } from '@kit.AVSessionKit';
@Entry
@Component
struct Index {
  @State message: string = 'hello world';

  build() {
    Column() {
        Text(this.message)
          .onClick(()=>{
            let currentAVSession: avSession.AVSession;
            let context: Context = this.getUIContext().getHostContext() as Context;
            let sessionId: string;  // Used as an input parameter of subsequent functions.
            let sessionTag: string;

            avSession.getAVSession(context).then(async (data: avSession.AVSession) => {
              currentAVSession = data;
              sessionId = currentAVSession.sessionId;
              sessionTag = currentAVSession.sessionTag;
              console.info(\`GetAVSession : SUCCESS : sessionId=${sessionId}, sessionTag=${sessionTag}\`);
            }).catch((err: BusinessError) => {
              console.error(\`GetAVSession BusinessError: code: ${err.code}, message: ${err.message}\`);
            });
          })
      }
    .width('100%')
    .height('100%')
  }
}
