# harmonyShare (Huawei Share)

This module provides Huawei Share event registration.

**Model restriction**: APIs of this module can be used only in the stage model.

**Start version**: 5.0.0(12)

#### Module Import

import { harmonyShare } from '@kit.ShareKit';

#### SharableErrorCode

Reason for rejecting a sharing callback. The user will be informed of the reason through a system notification.

**Model restriction**: This API can be used only in the stage model.

**System capability**: SystemCapability.Collaboration.HarmonyShare

**Start version**: 5.0.3(15)

| 
Name

 | 

Value

 | 

Description

 |
| :-- | :-- | :-- |
| 

NO\_CONTENT\_ERROR

 | 

1

 | 

Used when no content is shared.

 |
| 

NO\_INTERNET\_ERROR

 | 

2

 | 

Used when there is no network connection available.

 |
| 

DOWNLOAD\_ERROR

 | 

3

 | 

Used when download fails.

 |

#### ReceivableErrorCode

Reason for rejecting a callback for receiving data in sandbox mode. The user will be informed of the reason through a system notification.

**Model restriction**: This API can be used only in the stage model.

**System capability**: SystemCapability.Collaboration.HarmonyShare

**Start version**: 6.0.0(20)

| 
Name

 | 

Value

 | 

Description

 |
| :-- | :-- | :-- |
| 

NO\_RECEIVABLE\_ERROR

 | 

1

 | 

Used when data cannot be received.

 |

#### ShareResultCode

Result for data reception in the sandbox (success or cause of failure).

**Model restriction**: This API can be used only in the stage model.

**System capability**: SystemCapability.Collaboration.HarmonyShare

**Start version**: 6.0.0(20)

| 
Name

 | 

Value

 | 

Description

 |
| :-- | :-- | :-- |
| 

SHARE\_SUCCESS

 | 

0

 | 

Data received successfully in the sandbox.

 |
| 

SEND\_FAILED

 | 

1

 | 

Data transfer failed.

 |
| 

CANCEL\_BY\_SENDER

 | 

2

 | 

The sender canceled the sending.

 |
| 

CANCEL\_BY\_RECEIVER

 | 

3

 | 

The receiver canceled the reception.

 |

#### SharableTarget

Callback parameter after a Huawei Share event is triggered. This parameter can be used for cross-device sharing.

**Model restriction**: This API can be used only in the stage model.

**System capability**: SystemCapability.Collaboration.HarmonyShare

**Start version**: 5.0.0(12)

#### \[h2\]share

share(data: systemShare.SharedData): Promise<void>

Shares data across devices. This API returns the result asynchronously through a promise.

**Model restriction**: This API can be used only in the stage model.

**System capability**: SystemCapability.Collaboration.HarmonyShare

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

data

 | 

[systemShare.SharedData](../systemshare-system-share/document.md#section816451553012)

 | 

Yes

 | 

Shared data.

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

**Promise** object. No result is returned.

 |

**Error codes:**

For details about the error codes, please refer to [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

| 
Error Code

 | 

Message

 |
| :-- | :-- |
| 

[401](../../../../api-reference-overview/universal-error-codes/document.md#section401-parameter-check-failed)

 | 

Parameter error.

 |

#### \[h2\]reject

reject(error: SharableErrorCode): Promise<void>

Rejects a sharing that cannot proceed for any reason upon receiving a callback. This API returns the result asynchronously through a promise.

**Model restriction**: This API can be used only in the stage model.

**System capability**: SystemCapability.Collaboration.HarmonyShare

**Start version**: 5.0.3(15)

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

error

 | 

[SharableErrorCode](#section98742174617)

 | 

Yes

 | 

Reason for rejecting the sharing. The user will be informed of the reason through a system message.

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

**Promise** object. No result is returned.

 |

**Error codes:**

For details about the error codes, please refer to [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

| 
Error Code

 | 

Message

 |
| :-- | :-- |
| 

[401](../../../../api-reference-overview/universal-error-codes/document.md#section401-parameter-check-failed)

 | 

Parameter error.

 |

#### \[h2\]updateShareData

updateShareData(data: UpdatedData): Promise<void>

Updates the preview image before the shared data is sent. This API returns the result asynchronously through a promise.

This API is only used for the Tap to Transfer feature.

**Model restriction**: This API can be used only in the stage model.

**System capability**: SystemCapability.Collaboration.HarmonyShare

**Start version**: 6.0.0(20)

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

data

 | 

[UpdatedData](#section108971112124018)

 | 

Yes

 | 

Target data for the update.

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

**Promise** object. No result is returned.

 |

#### \[h2\]clarifyNonShare

clarifyNonShare(info: SharableErrorInfo): Promise<void>

Notifies the user that no sharable content is available on the current page and provides appropriate guidance. This API can be called upon receiving a callback.

This API is only used for the Tap to Transfer feature.

**Model restriction**: This API can be used only in the stage model.

**System capability**: SystemCapability.Collaboration.HarmonyShare

**Start version**: 6.0.2(22)

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

info

 | 

[SharableErrorInfo](#section10176454018)

 | 

Yes

 | 

Message used to notify the user of the reason why the sharing is unavailable.

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

**Promise** object. No result is returned.

 |

#### ReceivableTarget

Parameter in the callback for receiving data in sandbox mode.

**Model restriction**: This API can be used only in the stage model.

**System capability**: SystemCapability.Collaboration.HarmonyShare

**Start version**: 6.0.0(20)

#### \[h2\]receive

receive(receiveUri: string, callback: ReceiveCallback): Promise<void>

Provides the URI of the sandbox directory for receiving data. The received files are saved to this directory. This API returns the result asynchronously through a promise.

**Model restriction**: This API can be used only in the stage model.

**System capability**: SystemCapability.Collaboration.HarmonyShare

**Start version**: 6.0.0(20)

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

receiveUri

 | 

string

 | 

Yes

 | 

Directory for storing data received by the sandbox. The directory must exist.

NOTE:

Share Kit will obtain authorization for this directory before the transfer starts and automatically revoke the authorization after the transfer is complete. You are advised to use an existing empty directory to ensure information security.

 |
| 

callback

 | 

[ReceiveCallback](#section496835162818)

 | 

Yes

 | 

Callback for receiving data in sandbox mode.

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

**Promise** object. No result is returned.

 |

#### \[h2\]reject

reject(error: ReceivableErrorCode): Promise<void>

Rejects a sharing if data reception cannot proceed for any reason upon receiving a callback. This API returns the result asynchronously through a promise.

**Model restriction**: This API can be used only in the stage model.

**System capability**: SystemCapability.Collaboration.HarmonyShare

**Start version**: 6.0.0(20)

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

error

 | 

[ReceivableErrorCode](#section1884011169111)

 | 

Yes

 | 

Reason for rejecting data reception in sandbox mode. The user will be informed of the reason through a system message.

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

**Promise** object. No result is returned.

 |

#### UpdatedData

Data sent by the Huawei Share event.

**Model restriction**: This API can be used only in the stage model.

**System capability**: SystemCapability.Collaboration.HarmonyShare

**Start version**: 6.0.0(20)

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

thumbnailUri

 | 

string

 | 

No

 | 

Yes

 | 

URI of a preview image.

 |

#### BaseCapabilityRegistry

Basic configuration for Huawei Share event registration.

**Model restriction**: This API can be used only in the stage model.

**System capability**: SystemCapability.Collaboration.HarmonyShare

**Start version**: 6.0.0(20)

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

windowId

 | 

number

 | 

No

 | 

No

 | 

Window ID.

 |

#### SendCapabilityRegistry

Window registration configuration item for the Huawei Share event. This API inherits from [BaseCapabilityRegistry](#section7252115555417).

**Model restriction**: This API can be used only in the stage model.

**System capability**: SystemCapability.Collaboration.HarmonyShare

**Start version**: 6.0.0(20)

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

sendOnly

 | 

boolean

 | 

No

 | 

Yes

 | 

Indicates whether only data sending is supported. The default value is **false**, indicating that data sending and reception are both supported. If this parameter is set to **true** for both devices, two-way sharing is not allowed.

NOTE:

This parameter applies only to the Tap to Transfer feature.

 |

#### RecvCapability

Sets the data reception capability for the sandbox, including the file types and the maximum number of files that can be received at a time.

**Model restriction**: This API can be used only in the stage model.

**System capability**: SystemCapability.Collaboration.HarmonyShare

**Start version**: 6.0.0(20)

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

utd

 | 

string

 | 

No

 | 

No

 | 

Uniform data type. For details, please refer to [@ohos.data.uniformTypeDescriptor (Uniform Data Definition and Description)](../../../../application-framework/arkdata/arkts-apis/ohos-data-uniformtypedescriptor-uniform-data-definition-and-description/document.md).

 |
| 

maxSupportedCount

 | 

number

 | 

No

 | 

No

 | 

Maximum number of files that can be received at a time. The value must be a positive integer.

 |

#### RecvCapabilityRegistry

Window registration configuration item for the event of receiving data in sandbox mode. This API inherits from [BaseCapabilityRegistry](#section7252115555417).

**Model restriction**: This API can be used only in the stage model.

**System capability**: SystemCapability.Collaboration.HarmonyShare

**Start version**: 6.0.0(20)

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

capabilities

 | 

[RecvCapability](#section5644182344013)\[\]

 | 

No

 | 

No

 | 

Data reception capability of the sandbox, including the supported data types and quantity that can be received at a time.

 |

#### TransferBaseResults

Callback function for file transfer completion when the sandbox receives files.

**Model restriction**: This API can be used only in the stage model.

**System capability**: SystemCapability.Collaboration.HarmonyShare

**Start version**: 6.0.0(20)

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

onResult

 | 

Callback<[ShareResultCode](#section943818433405)\>

 | 

No

 | 

Yes

 | 

Callback function for file transfer completion. It is used to notify the transfer result.

 |

#### ReceiveCallback

Callback function triggered when the sandbox completes file receiving. It can be used to listen for the completion event and process the received data. It inherits from [TransferBaseResults](#section54808149718).

**Model restriction**: This API can be used only in the stage model.

**System capability**: SystemCapability.Collaboration.HarmonyShare

**Start version**: 6.0.0(20)

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

onDataReceived

 | 

Callback<[systemShare.SharedData](../systemshare-system-share/document.md#section816451553012)\>

 | 

No

 | 

No

 | 

Callback function triggered when the sandbox completes file receiving. It is used to provide the list of files saved to the sandbox path.

 |

#### SharableErrorInfo

Message used to notify the user of the reason why the sharing is unavailable.

**Model restriction**: This API can be used only in the stage model.

**System capability**: SystemCapability.Collaboration.HarmonyShare

**Start version**: 6.0.2(22)

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

message

 | 

string

 | 

No

 | 

Yes

 | 

Message content.

 |

#### on('knockShare')

on(event: 'knockShare', callback: Callback<SharableTarget>): void

Registers a device tapping event listener.

**Model restriction**: This API can be used only in the stage model.

**System capability**: SystemCapability.Collaboration.HarmonyShare

**Device behavior**: This API has no effect on tablets and works on other devices.

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

event

 | 

string

 | 

Yes

 | 

Event callback type. The value is **knockShare**, indicating that the event is triggered by tapping devices together.

 |
| 

callback

 | 

Callback<[SharableTarget](#section9147845115614)\>

 | 

Yes

 | 

Event callback.

 |

**Error codes:**

For details about the error codes, please refer to [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

| 
Error Code

 | 

Message

 |
| :-- | :-- |
| 

[401](../../../../api-reference-overview/universal-error-codes/document.md#section401-parameter-check-failed)

 | 

Parameter error.

 |

**Example:**

import { uniformTypeDescriptor as utd } from '@kit.ArkData';
import { systemShare, harmonyShare } from '@kit.ShareKit';

// Register a **knockShare** event listener.
harmonyShare.on('knockShare', (sharableTarget: harmonyShare.SharableTarget) => {
  // Construct the data to be shared.
  let shareData: systemShare.SharedData = new systemShare.SharedData({
    utd: utd.UniformDataType.PLAIN\_TEXT,
    content: 'This is a piece of text.'
  });
  // Start sharing.
  sharableTarget.share(shareData);
});

#### off('knockShare')

off(event: 'knockShare', callback?: Callback<SharableTarget>): void

Unregisters a device tapping event listener.

**Model restriction**: This API can be used only in the stage model.

**System capability**: SystemCapability.Collaboration.HarmonyShare

**Device behavior**: This API has no effect on tablets and works on other devices.

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

event

 | 

string

 | 

Yes

 | 

Event callback type. The value is **knockShare**, indicating that the device tapping event listener is unregistered.

 |
| 

callback

 | 

Callback<[SharableTarget](#section9147845115614)\>

 | 

No

 | 

Callback function. You can pass the callback used in the **on** API to unregister the corresponding listener. If you do not pass the callback, you will unregister all listeners.

 |

**Error codes:**

For details about the error codes, please refer to [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

| 
Error Code

 | 

Message

 |
| :-- | :-- |
| 

[401](../../../../api-reference-overview/universal-error-codes/document.md#section401-parameter-check-failed)

 | 

Parameter error.

 |

**Example:**

// Unregister a **knockShare** event listener.
harmonyShare.off('knockShare');

#### on('knockShare')

on(event: 'knockShare', capability: SendCapabilityRegistry, callback: Callback<SharableTarget>): void

Registers a device tapping event listener.

**Model restriction**: This API can be used only in the stage model.

**System capability**: SystemCapability.Collaboration.HarmonyShare

**Device behavior**: This API has no effect on tablets and works on other devices.

**Start version**: 6.0.0(20)

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

event

 | 

string

 | 

Yes

 | 

Event callback type. The value is **knockShare**, indicating that the event is triggered by tapping devices together.

 |
| 

capability

 | 

[SendCapabilityRegistry](#section7361949172719)

 | 

Yes

 | 

Event attribute.

 |
| 

callback

 | 

Callback<[SharableTarget](#section9147845115614)\>

 | 

Yes

 | 

Event callback.

 |

**Example:**

import { uniformTypeDescriptor as utd } from '@kit.ArkData';
import { systemShare, harmonyShare } from '@kit.ShareKit';

let capabilityRegistry: harmonyShare.SendCapabilityRegistry = {
  windowId: 999, // This is only an example. Replace it with the correct window ID.
}
// Register a **knockShare** event listener.
harmonyShare.on('knockShare', capabilityRegistry, (sharableTarget: harmonyShare.SharableTarget) => {
  // Construct the data to be shared.
  let shareData: systemShare.SharedData = new systemShare.SharedData({
    utd: utd.UniformDataType.PLAIN\_TEXT,
    content: 'This is a piece of text.'
  });
  // Start sharing.
  sharableTarget.share(shareData);
});

#### off('knockShare')

off(event: 'knockShare', capability: SendCapabilityRegistry, callback?: Callback<SharableTarget>): void

Unregisters a device tapping event listener.

**Model restriction**: This API can be used only in the stage model.

**System capability**: SystemCapability.Collaboration.HarmonyShare

**Device behavior**: This API has no effect on tablets and works on other devices.

**Start version**: 6.0.0(20)

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

event

 | 

string

 | 

Yes

 | 

Event callback type. The value is **knockShare**, indicating that the device tapping event listener is unregistered.

 |
| 

capability

 | 

[SendCapabilityRegistry](#section7361949172719)

 | 

Yes

 | 

Event attribute.

 |
| 

callback

 | 

Callback<[SharableTarget](#section9147845115614)\>

 | 

No

 | 

Callback function. You can pass the callback used in the **on** API to unregister the corresponding listener. If you do not pass the callback, you will unregister all listeners.

 |

**Example:**

let capabilityRegistry: harmonyShare.SendCapabilityRegistry = {
  windowId: 999, // This is only an example. Replace it with the correct window ID.
}
// Unregister a **knockShare** event listener.
harmonyShare.off('knockShare', capabilityRegistry);

#### on('gesturesShare')

on(event: 'gesturesShare', callback: Callback<SharableTarget>): void

Registers a Grab & drop event listener.

**Model restriction**: This API can be used only in the stage model.

**System capability**: SystemCapability.Collaboration.HarmonyShare

**Start version**: 6.0.0(20)

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

event

 | 

string

 | 

Yes

 | 

Event callback type. The value is **gesturesShare**, indicating that the event is triggered by clenching the fist.

 |
| 

callback

 | 

Callback<[SharableTarget](#section9147845115614)\>

 | 

Yes

 | 

Event callback.

 |

**Example:**

import { uniformTypeDescriptor as utd } from '@kit.ArkData';
import { systemShare, harmonyShare } from '@kit.ShareKit';

// Register a gesturesShare event listener.
harmonyShare.on('gesturesShare', (sharableTarget: harmonyShare.SharableTarget) => {
  // Construct the data to be shared.
  let shareData: systemShare.SharedData = new systemShare.SharedData({
    utd: utd.UniformDataType.PLAIN\_TEXT,
    content: 'This is a piece of text.'
  });
  // Start sharing.
  sharableTarget.share(shareData);
});

#### off('gesturesShare')

off(event: 'gesturesShare', callback?: Callback<SharableTarget>): void

Unregisters a Grab & drop event listener.

**Model restriction**: This API can be used only in the stage model.

**System capability**: SystemCapability.Collaboration.HarmonyShare

**Start version**: 6.0.0(20)

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

event

 | 

string

 | 

Yes

 | 

Event callback type. The value is **gesturesShare**, indicating that the Grab & drop event listener is unregistered.

 |
| 

callback

 | 

Callback<[SharableTarget](#section9147845115614)\>

 | 

No

 | 

Callback function. You can pass the callback used in the **on** API to unregister the corresponding listener. If you do not pass the callback, you will unregister all listeners.

 |

**Example:**

// Unregister a gesturesShare event listener.
harmonyShare.off('gesturesShare');

#### on('gesturesShare')

on(event: 'gesturesShare', capability: SendCapabilityRegistry, callback: Callback<SharableTarget>): void

Registers a Grab & drop event listener.

**Model restriction**: This API can be used only in the stage model.

**System capability**: SystemCapability.Collaboration.HarmonyShare

**Start version**: 6.0.0(20)

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

event

 | 

string

 | 

Yes

 | 

Event callback type. The value is **gesturesShare**, indicating that the event is triggered by clenching the fist.

 |
| 

capability

 | 

[SendCapabilityRegistry](#section7361949172719)

 | 

Yes

 | 

Event attribute.

 |
| 

callback

 | 

Callback<[SharableTarget](#section9147845115614)\>

 | 

Yes

 | 

Event callback.

 |

**Example:**

import { uniformTypeDescriptor as utd } from '@kit.ArkData';
import { systemShare, harmonyShare } from '@kit.ShareKit';

let capabilityRegistry: harmonyShare.SendCapabilityRegistry = {
  windowId: 999, // This is only an example. Replace it with the correct window ID.
}
// Register a gesturesShare event listener.
harmonyShare.on('gesturesShare', capabilityRegistry, (sharableTarget: harmonyShare.SharableTarget) => {
  // Construct the data to be shared.
  let shareData: systemShare.SharedData = new systemShare.SharedData({
    utd: utd.UniformDataType.PLAIN\_TEXT,
    content: 'This is a piece of text.'
  });
  // Start sharing.
  sharableTarget.share(shareData);
});

#### off('gesturesShare')

off(event: 'gesturesShare', capability: SendCapabilityRegistry, callback?: Callback<SharableTarget>): void

Unregisters a Grab & drop event listener.

**Model restriction**: This API can be used only in the stage model.

**System capability**: SystemCapability.Collaboration.HarmonyShare

**Start version**: 6.0.0(20)

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

event

 | 

string

 | 

Yes

 | 

Event callback type. The value is **gesturesShare**, indicating that the Grab & drop event listener is unregistered.

 |
| 

capability

 | 

[SendCapabilityRegistry](#section7361949172719)

 | 

Yes

 | 

Event attribute.

 |
| 

callback

 | 

Callback<[SharableTarget](#section9147845115614)\>

 | 

No

 | 

Callback function. You can pass the callback used in the **on** API to unregister the corresponding listener. If you do not pass the callback, you will unregister all listeners.

 |

**Example:**

let capabilityRegistry: harmonyShare.SendCapabilityRegistry = {
  windowId: 999, // This is only an example. Replace it with the correct window ID.
}
// Unregister a gesturesShare event listener.
harmonyShare.off('gesturesShare', capabilityRegistry);

#### on('dataReceive')

on(event: 'dataReceive', capability: RecvCapabilityRegistry, callback: Callback<ReceivableTarget>): void

Registers an event listener for receiving data in sandbox mode. Only file data is supported. The original receiving logic is retained for text data (including links).

**Model restriction**: This API can be used only in the stage model.

**System capability**: SystemCapability.Collaboration.HarmonyShare

**Device behavior differences**: This API works on PCs/2-in-1 devices. On other devices, it returns error code 801.

**Start version**: 6.0.0(20)

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

event

 | 

string

 | 

Yes

 | 

Event callback type. The value is **dataReceive**, which is triggered when a phone lightly touches a PC/2-in-1 device screen.

 |
| 

capability

 | 

[RecvCapabilityRegistry](#section145341487280)

 | 

Yes

 | 

Event attribute.

 |
| 

callback

 | 

Callback<[ReceivableTarget](#section13539165583)\>

 | 

Yes

 | 

Event callback.

 |

**Example:**

import { uniformTypeDescriptor as utd } from '@kit.ArkData';
import { systemShare, harmonyShare } from '@kit.ShareKit';
import { common } from '@kit.AbilityKit';

let capabilityRegistry: harmonyShare.RecvCapabilityRegistry = {
  windowId: 999, // This is only an example. Replace it with the correct window ID.
  capabilities: \[{
    utd: utd.UniformDataType.IMAGE,
    maxSupportedCount: 1
  }\]
}
// Register a dataReceive event listener.
harmonyShare.on('dataReceive', capabilityRegistry, (receivableTarget: harmonyShare.ReceivableTarget) => {
  let uiContext: UIContext = this.getUIContext();
  let context = uiContext.getHostContext() as common.UIAbilityContext;
  receivableTarget.receive(context.filesDir, { // This is only an example. Replace it with the actual path.
    onDataReceived: (sharedData: systemShare.SharedData) => {
      let sharedRecords = sharedData.getRecords();
      sharedRecords.forEach((record: systemShare.SharedRecord) => {
        // Process the shared data.
      });
    },
    onResult(resultCode: harmonyShare.ShareResultCode) {
      if (resultCode === harmonyShare.ShareResultCode.SHARE\_SUCCESS) {
        // To do things.
      }
    }
  });
});

#### off('dataReceive')

off(event: 'dataReceive', capability: RecvCapabilityRegistry, callback?: Callback<ReceivableTarget>): void

Unregisters an event listener for receiving data in sandbox mode.

**Model restriction**: This API can be used only in the stage model.

**System capability**: SystemCapability.Collaboration.HarmonyShare

**Device behavior differences**: This API works on PCs/2-in-1 devices. On other devices, it returns error code 801.

**Start version**: 6.0.0(20)

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

event

 | 

string

 | 

Yes

 | 

Event callback type. The value is **dataReceive**, indicating that the event listener for receiving data in sandbox mode is unregistered.

 |
| 

capability

 | 

[RecvCapabilityRegistry](#section145341487280)

 | 

Yes

 | 

Event attribute.

 |
| 

callback

 | 

Callback<[ReceivableTarget](#section13539165583)\>

 | 

No

 | 

Callback function. You can pass the callback used in the **on** API to unregister the corresponding listener. If you do not pass the callback, you will unregister all listeners.

 |

**Example:**

let capabilityRegistry: harmonyShare.RecvCapabilityRegistry = {
  windowId: 999, // This is only an example. Replace it with the correct window ID.
  capabilities: \[{
    utd: utd.UniformDataType.IMAGE,
    maxSupportedCount: 1
  }\]
}
// Unregister a dataReceive event listener.
harmonyShare.off('dataReceive', capabilityRegistry);
