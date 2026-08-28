# wearEngine (Wearable Capabilities)

This module provides the interaction capability between phones and wearable devices. Apps can call the APIs to:

-   Obtain the list of connected devices and exchange messages and files with a peer device.
-   Query the status of a wearable device, send template-based notifications to a wearable device, and receive sensor data for a wearable device.

**Start version**: 5.0.0(12)

#### Module Import

import { wearEngine } from '@kit.WearEngine';

#### wearEngine.getAuthClient

getAuthClient(context: common.Context): AuthClient

Obtains the client for authorization management.

**Model restriction**: This API can be used only in the stage model.

**System capability**: SystemCapability.Health.WearEngine

**Device behavior differences**: This API is supported on phones and tablets. On other devices, it returns error code 801.

**Start version**: 5.0.0(12)

**Parameters:**

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

[common.Context](../../../../../application-framework/ability-kit/arkts-apis/dependent-elements-and-definitions/application/context-context-base-class-of-the-stage-model/document.md#context)

 | 

Yes

 | 

Context. Only the context that contains the **connectServiceExtensionAbility** method is supported (example: [UIAbilityContext](../../../../../application-framework/ability-kit/arkts-apis/dependent-elements-and-definitions/application/uiabilitycontext/document.md#uiabilitycontext-1)).

 |

**Returns**:

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

[AuthClient](#section876918413377)

 | 

Authorization management client, which stores methods related to the authorization module.

 |

**Error codes**:

For details about the error codes, please refer to [Wear Engine ArkTS API Error Codes](../../arkts-api-error-codes/document.md).

| 
Error Code

 | 

Error Message

 |
| :-- | :-- |
| 

[401](../../arkts-api-error-codes/document.md#section201741341307)

 | 

Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types.

 |
| 

[801](../../arkts-api-error-codes/document.md#section5941173162512)

 | 

Capability not supported.

 |
| 

[1008509999](../../arkts-api-error-codes/document.md#section93011432734)

 | 

Internal error.

 |

**Example:**

import { wearEngine } from '@kit.WearEngine';

let authClient: wearEngine.AuthClient = wearEngine.getAuthClient(this.getUIContext().getHostContext());
console.info(\`Succeeded in getting auth client\`);

#### AuthClient

Authorization management client class, which is returned by [wearEngine.getAuthClient](#section17606835182712).

**Model restriction**: This API can be used only in the stage model.

**System capability**: SystemCapability.Health.WearEngine

**Start version**: 5.0.0(12)

#### \[h2\]requestAuthorization

requestAuthorization(request: AuthorizationRequest): Promise<AuthorizationResponse>

Requests authorization from a phone user, and returns the permissions granted by the user. This API returns the result asynchronously through a promise.

**System capability**: SystemCapability.Health.WearEngine

**Device behavior differences**: This API is supported on phones and tablets. On other devices, it returns error code 801.

**Model restriction**: This API can be used only in the stage model.

**Start version**: 5.0.0(12)

**Parameters:**

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

request

 | 

[AuthorizationRequest](#section12513135291215)

 | 

Yes

 | 

Permission request class.

 |

**Returns**:

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

Promise<[AuthorizationResponse](#section1536013509131)\>

 | 

Promise object used to return the authorization response class.

 |

**Error codes**:

For details about the error codes, please refer to [Wear Engine ArkTS API Error Codes](../../arkts-api-error-codes/document.md).

| 
Error Code

 | 

Error Message

 |
| :-- | :-- |
| 

[401](../../arkts-api-error-codes/document.md#section201741341307)

 | 

Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed.

 |
| 

[1008500001](../../arkts-api-error-codes/document.md#section1047474644710)

 | 

Network error. The network is unavailable.

 |
| 

[1008500004](../../arkts-api-error-codes/document.md#section485113712218)

 | 

App has not applied for the Wear Engine service.

 |
| 

[1008500006](../../arkts-api-error-codes/document.md#section1461311549277)

 | 

User privacy is not agreed.

 |
| 

[1008500007](../../arkts-api-error-codes/document.md#section15917165718219)

 | 

The device capability is not supported.

 |
| 

[1008500008](../../arkts-api-error-codes/document.md#section612518413314)

 | 

Account error. The user has not logged in with HUAWEI ID.

 |
| 

[1008500009](../../arkts-api-error-codes/document.md#section94850224314)

 | 

Account error. Failed to obtain account information with HUAWEI ID.

 |
| 

[1008509999](../../arkts-api-error-codes/document.md#section93011432734)

 | 

Internal error.

 |

**Example:**

import { wearEngine } from '@kit.WearEngine';
import { BusinessError } from '@kit.BasicServicesKit';

let authClient: wearEngine.AuthClient = wearEngine.getAuthClient(this.getUIContext().getHostContext());

let request: wearEngine.AuthorizationRequest = {
  permissions: \[wearEngine.Permission.USER\_STATUS\]
}

authClient.requestAuthorization(request).then(result => {
  console.info(\`Succeeded in requesting authorize, authorized permissions is ${result.permissions}\`);
}).catch((error: BusinessError) => {
  console.error(\`Failed to request authorize. Code is ${error.code}, message is ${error.message}\`);
})

#### \[h2\]getAuthorization

getAuthorization(): Promise<AuthorizationResponse>

Obtains the permissions granted by a user. This API returns the result asynchronously through a promise.

**System capability**: SystemCapability.Health.WearEngine

**Device behavior differences**: This API is supported on phones and tablets. On other devices, it returns error code 801.

**Model restriction**: This API can be used only in the stage model.

**Start version**: 5.0.0(12)

**Returns**:

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

Promise<[AuthorizationResponse](#section1536013509131)\>

 | 

Promise object used to return the authorization response class.

 |

**Error codes**:

For details about the error codes, please refer to [Wear Engine ArkTS API Error Codes](../../arkts-api-error-codes/document.md).

| 
Error Code

 | 

Error Message

 |
| :-- | :-- |
| 

[1008500001](../../arkts-api-error-codes/document.md#section1047474644710)

 | 

Network error. The network is unavailable.

 |
| 

[1008500004](../../arkts-api-error-codes/document.md#section485113712218)

 | 

App has not applied for the Wear Engine service.

 |
| 

[1008500006](../../arkts-api-error-codes/document.md#section1461311549277)

 | 

User privacy is not agreed.

 |
| 

[1008500007](../../arkts-api-error-codes/document.md#section15917165718219)

 | 

The device capability is not supported.

 |
| 

[1008500008](../../arkts-api-error-codes/document.md#section612518413314)

 | 

Account error. The user has not logged in with HUAWEI ID.

 |
| 

[1008500009](../../arkts-api-error-codes/document.md#section94850224314)

 | 

Account error. Failed to obtain account information with HUAWEI ID.

 |
| 

[1008509999](../../arkts-api-error-codes/document.md#section93011432734)

 | 

Internal error.

 |

**Example:**

import { wearEngine } from '@kit.WearEngine';
import { BusinessError } from '@kit.BasicServicesKit';

let authClient: wearEngine.AuthClient = wearEngine.getAuthClient(this.getUIContext().getHostContext());

authClient.getAuthorization().then(result => {
  console.info(\`Succeeded in getting authorized permissions, authorized permissions is ${result.permissions}\`);
}).catch((error: BusinessError) => {
  console.error(\`Failed to get authorized permissions. Code is ${error.code}, message is ${error.message}\`);
})

#### AuthorizationBase

Base class for the input and output of the permission control module.

**System capability**: SystemCapability.Health.WearEngine

**Model restriction**: This API can be used only in the stage model.

**Start version**: 5.0.0(12)

| 
Name

 | 

Type

 | 

Read-only

 | 

Optional

 | 

Description

 |
| :-- | :-- | :-- | :-- | :-- |
| 

permissions

 | 

[Permission](#section09971113566)\[\]

 | 

No

 | 

No

 | 

Array of permission enums.

 |

#### Permission

Permission enums.

**System capability**: SystemCapability.Health.WearEngine

**Model restriction**: This API can be used only in the stage model.

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

USER\_STATUS

 | 

2

 | 

Permission to obtain user status, such as the wearing status of a wearable device.

 |
| 

MOTION\_SENSOR

 | 

3

 | 

Permission to obtain the motion sensor data of the peer device, such as the acceleration sensor data.

 |
| 

HEALTH\_SENSOR

 | 

4

 | 

Permission to obtain the human body sensor data of the peer device, such as the heart rate sensor data.

 |
| 

DEVICE\_IDENTIFIER

 | 

6

 | 

Permission to obtain the SN of the connected wearable device.

 |

#### AuthorizationRequest

Authorization request class inherited from [AuthorizationBase](#section3936113217535).

**Model restriction**: This API can be used only in the stage model.

**System capability**: SystemCapability.Health.WearEngine

**Start version**: 5.0.0(12)

#### AuthorizationResponse

Authorization response class inherited from [AuthorizationBase](#section3936113217535).

**Model restriction**: This API can be used only in the stage model.

**System capability**: SystemCapability.Health.WearEngine

**Start version**: 5.0.0(12)

#### wearEngine.getDeviceClient

getDeviceClient(context: common.Context): DeviceClient

Obtains the client of the Device module.

**Model restriction**: This API can be used only in the stage model.

**System capability**: SystemCapability.Health.WearEngine

**Start version**: 5.0.0(12)

**Parameters:**

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

[common.Context](../../../../../application-framework/ability-kit/arkts-apis/dependent-elements-and-definitions/application/context-context-base-class-of-the-stage-model/document.md#context)

 | 

Yes

 | 

Context. Only the context that contains the **connectServiceExtensionAbility** method is supported (example: [UIAbilityContext](../../../../../application-framework/ability-kit/arkts-apis/dependent-elements-and-definitions/application/uiabilitycontext/document.md#uiabilitycontext-1)).

 |

**Returns**:

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

[DeviceClient](#section126321419369)

 | 

Device client, which stores methods related to the Device module.

 |

**Error codes**:

For details about the error codes, please refer to [Wear Engine ArkTS API Error Codes](../../arkts-api-error-codes/document.md).

| 
Error Code

 | 

Error Message

 |
| :-- | :-- |
| 

[401](../../arkts-api-error-codes/document.md#section201741341307)

 | 

Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types.

 |
| 

[1008509999](../../arkts-api-error-codes/document.md#section93011432734)

 | 

Internal error.

 |

**Example:**

import { wearEngine } from '@kit.WearEngine';

let deviceClient: wearEngine.DeviceClient = wearEngine.getDeviceClient(this.getUIContext().getHostContext());
console.info(\`Succeeded in getting device client.\`);

#### DeviceClient

Device client class, which is returned by [wearEngine.getDeviceClient](#section1892394201117).

**Model restriction**: This API can be used only in the stage model.

**System capability**: SystemCapability.Health.WearEngine

**Start version**: 5.0.0(12)

#### \[h2\]getConnectedDevices

getConnectedDevices(): Promise<Device\[\]>

Obtains the connected devices that support Wear Engine capabilities.

**System capability**: SystemCapability.Health.WearEngine

**Model restriction**: This API can be used only in the stage model.

**Start version**: 5.0.0(12)

**Returns**:

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

Promise<[Device](#section385118379447)\[\]>

 | 

Promise object used to return the device list.

 |

**Error codes**:

For details about the error codes, please refer to [Wear Engine ArkTS API Error Codes](../../arkts-api-error-codes/document.md).

| 
Error Code

 | 

Error Message

 |
| :-- | :-- |
| 

[1008500001](../../arkts-api-error-codes/document.md#section1047474644710)

 | 

Network error. The network is unavailable.

 |
| 

[1008500004](../../arkts-api-error-codes/document.md#section485113712218)

 | 

App has not applied for the Wear Engine service.

 |
| 

[1008500006](../../arkts-api-error-codes/document.md#section1461311549277)

 | 

User privacy is not agreed.

 |
| 

[1008500008](../../arkts-api-error-codes/document.md#section612518413314)

 | 

Account error. The user has not logged in with HUAWEI ID.

 |
| 

[1008500009](../../arkts-api-error-codes/document.md#section94850224314)

 | 

Account error. Failed to obtain account information with HUAWEI ID.

 |
| 

[1008509999](../../arkts-api-error-codes/document.md#section93011432734)

 | 

Internal error.

 |

**Example:**

import { wearEngine } from '@kit.WearEngine';
import { BusinessError } from '@kit.BasicServicesKit';

let deviceClient: wearEngine.DeviceClient = wearEngine.getDeviceClient(this.getUIContext().getHostContext());
deviceClient.getConnectedDevices().then((devices) => {
  console.info(\`Succeeded in getting devices, devices number is ${devices.length}.\`);
}).catch((error: BusinessError) => {
  console.error(\`Failed to get devices. Code is ${error.code}, message is ${error.message}.\`);
})

#### Device

Wearable device information class, which is returned by [getConnectedDevices](#section1828213119411).

**Model restriction**: This API can be used only in the stage model.

**System capability**: SystemCapability.Health.WearEngine

**Start version**: 5.0.0(12)

#### \[h2\]Parameters

| 
Name

 | 

Type

 | 

Read-only

 | 

Optional

 | 

Description

 |
| :-- | :-- | :-- | :-- | :-- |
| 

randomId

 | 

string

 | 

No

 | 

No

 | 

Random and unique device identifier, which is automatically generated each time the device is linked.

 |
| 

category

 | 

[DeviceCategory](#section145591125155713)

 | 

No

 | 

Yes

 | 

Device type.

 |
| 

name

 | 

string

 | 

No

 | 

Yes

 | 

Device name.

 |
| 

softwareVersion

 | 

string

 | 

No

 | 

Yes

 | 

Device software version.

 |
| 

model

 | 

string

 | 

No

 | 

Yes

 | 

Device model.

 |
| 

isSmartWatch

 | 

boolean

 | 

No

 | 

Yes

 | 

Indicates whether the device is a smart watch. **true**: yes; **false**: no

 |
| 

osCategory

 | 

[OsCategory](#section8322015161010)

 | 

No

 | 

Yes

 | 

Operating system type of the device.

**Start version**: 5.1.0(18)

 |

#### \[h2\]isWearEngineCapabilitySupported

isWearEngineCapabilitySupported(capability: WearEngineCapability): Promise<boolean>

Checks whether the connected wearable device returned by [getConnectedDevices](#section1828213119411) supports a specified [WearEngineCapability](#section1639211301479). This API returns the result asynchronously through a promise.

**System capability**: SystemCapability.Health.WearEngine

**Device behavior differences**: This API is supported on phones and tablets. On other devices, it returns error code 801.

**Model restriction**: This API can be used only in the stage model.

**Start version**: 5.0.0(12)

**Parameters:**

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

capability

 | 

[WearEngineCapability](#section1639211301479)

 | 

Yes

 | 

Specified Wear Engine capability.

 |

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

Promise object used to return whether the specified capability is supported.

**true**: supported; **false**: not supported

 |

**Error codes**:

For details about the error codes, please refer to [Wear Engine ArkTS API Error Codes](../../arkts-api-error-codes/document.md).

| 
Error Code

 | 

Error Message

 |
| :-- | :-- |
| 

[401](../../arkts-api-error-codes/document.md#section201741341307)

 | 

Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types.

 |
| 

[801](../../arkts-api-error-codes/document.md#section5941173162512)

 | 

Capability not supported.

 |
| 

[1008500001](../../arkts-api-error-codes/document.md#section1047474644710)

 | 

Network error. The network is unavailable.

 |
| 

[1008500002](../../arkts-api-error-codes/document.md#section18859424615)

 | 

No device is bound.

 |
| 

[1008500003](../../arkts-api-error-codes/document.md#section11616131326)

 | 

Device disconnected.

 |
| 

[1008500004](../../arkts-api-error-codes/document.md#section485113712218)

 | 

App has not applied for the Wear Engine service.

 |
| 

[1008500006](../../arkts-api-error-codes/document.md#section1461311549277)

 | 

User privacy is not agreed.

 |
| 

[1008500008](../../arkts-api-error-codes/document.md#section612518413314)

 | 

Account error. The user has not logged in with HUAWEI ID.

 |
| 

[1008500009](../../arkts-api-error-codes/document.md#section94850224314)

 | 

Account error. Failed to obtain account information with HUAWEI ID.

 |
| 

[1008509999](../../arkts-api-error-codes/document.md#section93011432734)

 | 

Internal error.

 |

**Example:**

import { wearEngine } from '@kit.WearEngine';
import { BusinessError } from '@kit.BasicServicesKit';

let deviceClient: wearEngine.DeviceClient = wearEngine.getDeviceClient(this.getUIContext().getHostContext());
let devices: wearEngine.Device\[\] = await deviceClient.getConnectedDevices();

if (devices.length > 0) {
  // Select the target device from the obtained device list and define it as **device**. (Assume that there are connected devices in the array and the first one is the target device.)
  let device: wearEngine.Device = devices\[0\];

  device.isWearEngineCapabilitySupported(wearEngine.WearEngineCapability.P2P\_COMMUNICATION).then((isSupportP2P) => {
    console.info(\`Succeeded in checking p2p capability, result is ${isSupportP2P}\`);
  }).catch((error: BusinessError) => {
    console.error(\`Failed to check p2p capability. Code is ${error.code}, message is ${error.message}\`);
  })
}

#### \[h2\]isDeviceCapabilitySupported

isDeviceCapabilitySupported(capability: DeviceCapability): Promise<boolean>

Checks whether the connected wearable device returned by [getConnectedDevices](#section1828213119411) supports a specified [DeviceCapability](#section0965105510366). This API returns the result asynchronously through a promise.

**System capability**: SystemCapability.Health.WearEngine

**Device behavior differences**: This API is supported on phones and tablets. On other devices, it returns error code 801.

**Model restriction**: This API can be used only in the stage model.

**Start version**: 5.0.0(12)

**Parameters:**

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

capability

 | 

[DeviceCapability](#section0965105510366)

 | 

Yes

 | 

Specified device capability.

 |

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

Promise object used to return whether the specified capability is supported.

**true**: supported; **false**: not supported

 |

**Error codes**:

For details about the error codes, please refer to [Wear Engine ArkTS API Error Codes](../../arkts-api-error-codes/document.md).

| 
Error Code

 | 

Error Message

 |
| :-- | :-- |
| 

[401](../../arkts-api-error-codes/document.md#section201741341307)

 | 

Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types.

 |
| 

[801](../../arkts-api-error-codes/document.md#section5941173162512)

 | 

Capability not supported.

 |
| 

[1008500001](../../arkts-api-error-codes/document.md#section1047474644710)

 | 

Network error. The network is unavailable.

 |
| 

[1008500002](../../arkts-api-error-codes/document.md#section18859424615)

 | 

No device is bound.

 |
| 

[1008500003](../../arkts-api-error-codes/document.md#section11616131326)

 | 

Device disconnected.

 |
| 

[1008500004](../../arkts-api-error-codes/document.md#section485113712218)

 | 

App has not applied for the Wear Engine service.

 |
| 

[1008500006](../../arkts-api-error-codes/document.md#section1461311549277)

 | 

User privacy is not agreed.

 |
| 

[1008500008](../../arkts-api-error-codes/document.md#section612518413314)

 | 

Account error. The user has not logged in with HUAWEI ID.

 |
| 

[1008500009](../../arkts-api-error-codes/document.md#section94850224314)

 | 

Account error. Failed to obtain account information with HUAWEI ID.

 |
| 

[1008509999](../../arkts-api-error-codes/document.md#section93011432734)

 | 

Internal error.

 |

**Example:**

import { wearEngine } from '@kit.WearEngine';
import { BusinessError } from '@kit.BasicServicesKit';

let deviceClient: wearEngine.DeviceClient = wearEngine.getDeviceClient(this.getUIContext().getHostContext());
let devices: wearEngine.Device\[\] = await deviceClient.getConnectedDevices();

if (devices.length > 0) {
  // Select the target device from the obtained device list and define it as **device**. (Assume that there are connected devices in the array and the first one is the target device.)
  let device: wearEngine.Device = devices\[0\];

  device.isDeviceCapabilitySupported(wearEngine.DeviceCapability.CBT\_I).then((isSupportCBTI) => {
    console.info(\`Succeeded in checking CBTI capability, result is ${isSupportCBTI}\`);
  }).catch((error: BusinessError) => {
    console.error(\`Failed to check CBTI capability. Code is ${error.code}, message is ${error.message}\`);
  })
}

#### \[h2\]getSerialNumber

getSerialNumber(): Promise<string>

Checks the SN of the connected wearable device returned by [getConnectedDevices](#section1828213119411). This API returns the result asynchronously through a promise.

**System capability**: SystemCapability.Health.WearEngine

**Device behavior differences**: This API is supported on phones and tablets. On other devices, it returns error code 801.

**Model restriction**: This API can be used only in the stage model.

**Start version**: 5.0.0(12)

**Returns**:

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

Promise<string>

 | 

Promise object used to return the device SN.

 |

**Error codes**:

For details about the error codes, please refer to [Wear Engine ArkTS API Error Codes](../../arkts-api-error-codes/document.md).

| 
Error Code

 | 

Error Message

 |
| :-- | :-- |
| 

[801](../../arkts-api-error-codes/document.md#section5941173162512)

 | 

Capability not supported.

 |
| 

[1008500001](../../arkts-api-error-codes/document.md#section1047474644710)

 | 

Network error. The network is unavailable.

 |
| 

[1008500002](../../arkts-api-error-codes/document.md#section18859424615)

 | 

No device is bound.

 |
| 

[1008500003](../../arkts-api-error-codes/document.md#section11616131326)

 | 

Device disconnected.

 |
| 

[1008500004](../../arkts-api-error-codes/document.md#section485113712218)

 | 

App has not applied for the Wear Engine service.

 |
| 

[1008500005](../../arkts-api-error-codes/document.md#section665613120197)

 | 

The HUAWEI ID is not authorized.

 |
| 

[1008500006](../../arkts-api-error-codes/document.md#section1461311549277)

 | 

User privacy is not agreed.

 |
| 

[1008500008](../../arkts-api-error-codes/document.md#section612518413314)

 | 

Account error. The user has not logged in with HUAWEI ID.

 |
| 

[1008500009](../../arkts-api-error-codes/document.md#section94850224314)

 | 

Account error. Failed to obtain account information with HUAWEI ID.

 |
| 

[1008509999](../../arkts-api-error-codes/document.md#section93011432734)

 | 

Internal error.

 |

**Example:**

import { wearEngine } from '@kit.WearEngine';
import { BusinessError } from '@kit.BasicServicesKit';

let deviceClient: wearEngine.DeviceClient = wearEngine.getDeviceClient(this.getUIContext().getHostContext());
let devices: wearEngine.Device\[\] = await deviceClient.getConnectedDevices();

if (devices.length > 0) {
  // Select the target device from the obtained device list and define it as **device**. (Assume that there are connected devices in the array and the first one is the target device.)
  let device: wearEngine.Device = devices\[0\];

  device.getSerialNumber().then((sn) => {
    console.info(\`Succeeded in getting device SN, result is ${sn}\`);
  }).catch((error: BusinessError) => {
    console.error(\`Failed to get device SN. Code is ${error.code}, message is ${error.message}\`);
  })
}

#### WearEngineCapability

Wear Engine capability enums.

**System capability**: SystemCapability.Health.WearEngine

**Model restriction**: This API can be used only in the stage model.

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

P2P\_COMMUNICATION

 | 

1

 | 

Peer-to-peer (P2P) capability.

 |
| 

MONITOR

 | 

2

 | 

Monitor capability.

 |
| 

NOTIFICATION

 | 

3

 | 

Notify capability.

 |
| 

SENSOR

 | 

4

 | 

Sensor capability.

 |

#### DeviceCapability

Device capability enums.

**System capability**: SystemCapability.Health.WearEngine

**Model restriction**: This API can be used only in the stage model.

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

APP\_INSTALLATION

 | 

14

 | 

App installation capability.

 |
| 

CBT\_I

 | 

128

 | 

Digital Cognitive Behavioral Therapy for Insomnia (CBT-i) capability.

 |

#### DeviceCategory

Device type enums.

**System capability**: SystemCapability.Health.WearEngine

**Model restriction**: This API can be used only in the stage model.

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

DEFAULT

 | 

1

 | 

Phone or tablet.

 |
| 

WATCH

 | 

2

 | 

Watch.

 |
| 

BAND

 | 

3

 | 

Band.

 |
| 

OTHER\_DEVICES

 | 

255

 | 

Other device types.

 |

#### OsCategory

Device operating system type enums.

**System capability**: SystemCapability.Health.WearEngine

**Device behavior differences**: This API is supported only on wearables. Calls on other device types have no effect.

**Model restriction**: This API can be used only in the stage model.

**Start version**: 5.1.0(18)

| 
Name

 | 

Value

 | 

Description

 |
| :-- | :-- | :-- |
| 

HARMONYOS

 | 

1

 | 

HarmonyOS

 |
| 

IOS

 | 

2

 | 

IOS

 |
| 

OTHER\_OS

 | 

255

 | 

Other types.

 |

#### wearEngine.getMonitorClient

getMonitorClient(context: common.Context): MonitorClient

Obtains the client of the Monitor module.

**Model restriction**: This API can be used only in the stage model.

**System capability**: SystemCapability.Health.WearEngine

**Device behavior differences**: This API is supported on phones and tablets. On other devices, it returns error code 801.

**Start version**: 5.0.0(12)

**Parameters:**

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

[common.Context](../../../../../application-framework/ability-kit/arkts-apis/dependent-elements-and-definitions/application/context-context-base-class-of-the-stage-model/document.md#context)

 | 

Yes

 | 

Context. Only the context that contains the **connectServiceExtensionAbility** method is supported (example: [UIAbilityContext](../../../../../application-framework/ability-kit/arkts-apis/dependent-elements-and-definitions/application/uiabilitycontext/document.md#uiabilitycontext-1)).

 |

**Returns**:

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

[MonitorClient](#section178254313113)

 | 

Monitor client, which stores methods related to the Monitor module.

 |

**Error codes**:

For details about the error codes, please refer to [Wear Engine ArkTS API Error Codes](../../arkts-api-error-codes/document.md).

| 
Error Code

 | 

Error Message

 |
| :-- | :-- |
| 

[401](../../arkts-api-error-codes/document.md#section201741341307)

 | 

Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types.

 |
| 

[801](../../arkts-api-error-codes/document.md#section5941173162512)

 | 

Capability not supported.

 |
| 

[1008509999](../../arkts-api-error-codes/document.md#section93011432734)

 | 

Internal error.

 |

**Example:**

import { wearEngine } from '@kit.WearEngine';

let monitorClient: wearEngine.MonitorClient = wearEngine.getMonitorClient(this.getUIContext().getHostContext());
console.info(\`Succeeded in getting monitor client.\`);

#### MonitorClient

Monitor client class, which is returned by [wearEngine.getMonitorClient](#section068883315262).

**Model restriction**: This API can be used only in the stage model.

**System capability**: SystemCapability.Health.WearEngine

**Start version**: 5.0.0(12)

#### \[h2\]queryStatus

queryStatus(deviceRandomId: string, item: MonitorItem): Promise<MonitorData>

Queries the specified state of a specific device. This API returns the result asynchronously through a promise.

**System capability**: SystemCapability.Health.WearEngine

**Device behavior differences**: This API is supported on phones and tablets. On other devices, it returns error code 801.

**Model restriction**: This API can be used only in the stage model.

**Start version**: 5.0.0(12)

**Parameters:**

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

deviceRandomId

 | 

string

 | 

Yes

 | 

Random identifier of a [Device](#section385118379447), which specifies the device to be queried.

 |
| 

item

 | 

[MonitorItem](#section16422462613)

 | 

Yes

 | 

Device state enum, which specifies the state to be queried.

 |

**Returns**:

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

Promise<[MonitorData](#section12024822410)\>

 | 

Promise object used to return the query result. For details about each returned state, please refer to [MonitorItem](#section16422462613).

 |

**Error codes**:

For details about the error codes, please refer to [Wear Engine ArkTS API Error Codes](../../arkts-api-error-codes/document.md).

| 
Error Code

 | 

Error Message

 |
| :-- | :-- |
| 

[401](../../arkts-api-error-codes/document.md#section201741341307)

 | 

Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed.

 |
| 

[1008500001](../../arkts-api-error-codes/document.md#section1047474644710)

 | 

Network error. The network is unavailable.

 |
| 

[1008500002](../../arkts-api-error-codes/document.md#section18859424615)

 | 

No device is bound.

 |
| 

[1008500003](../../arkts-api-error-codes/document.md#section11616131326)

 | 

Device disconnected.

 |
| 

[1008500004](../../arkts-api-error-codes/document.md#section485113712218)

 | 

App has not applied for the Wear Engine service.

 |
| 

[1008500005](../../arkts-api-error-codes/document.md#section665613120197)

 | 

The HUAWEI ID is not authorized.

 |
| 

[1008500006](../../arkts-api-error-codes/document.md#section1461311549277)

 | 

User privacy is not agreed.

 |
| 

[1008500007](../../arkts-api-error-codes/document.md#section15917165718219)

 | 

The device capability is not supported.

 |
| 

[1008500008](../../arkts-api-error-codes/document.md#section612518413314)

 | 

Account error. The user has not logged in with HUAWEI ID.

 |
| 

[1008500009](../../arkts-api-error-codes/document.md#section94850224314)

 | 

Account error. Failed to obtain account information with HUAWEI ID.

 |
| 

[1008500010](../../arkts-api-error-codes/document.md#section411611281734)

 | 

Device ID is invalid.

 |
| 

[1008509999](../../arkts-api-error-codes/document.md#section93011432734)

 | 

Internal error.

 |

**Example:**

import { wearEngine } from '@kit.WearEngine';
import { BusinessError } from '@kit.BasicServicesKit';

let deviceClient: wearEngine.DeviceClient = wearEngine.getDeviceClient(this.getUIContext().getHostContext());
let monitorClient: wearEngine.MonitorClient = wearEngine.getMonitorClient(this.getUIContext().getHostContext());
let devices: wearEngine.Device\[\] = await deviceClient.getConnectedDevices();

if (devices.length > 0) {
  // Select the target device from the obtained device list and define it as **device**. (Assume that there are connected devices in the array and the first one is the target device.)
  let device: wearEngine.Device = devices\[0\];

  monitorClient.queryStatus(device.randomId, wearEngine.MonitorItem.WEAR\_STATUS).then((result) => {
    console.info(\`Succeeded in querying wear status, result is ${result.code}.\`);
  }).catch((error: BusinessError) => {
    console.error(\`Failed to query wear status. Code is ${error.code}, message is ${error.message}.\`);
  })
}

#### \[h2\]subscribeEvent

subscribeEvent(deviceRandomId: string, type: MonitorEvent, callback: Callback<MonitorEventData>): Promise<void>

Subscribes to the change event of a specific device's specified state. This API uses a callback to return the change event asynchronously, and uses a promise to return the subscription result asynchronously.

**Model restriction**: This API can be used only in the stage model.

**System capability**: SystemCapability.Health.WearEngine

**Device behavior differences**: This API is supported on phones and tablets. On other devices, it returns error code 801.

**Start version**: 5.0.0(12)

**Parameters:**

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

deviceRandomId

 | 

string

 | 

Yes

 | 

Random identifier of a [Device](#section385118379447), which specifies the device involved in the subscription.

 |
| 

type

 | 

[MonitorEvent](#section0407141762619)

 | 

Yes

 | 

Device state enum, which specifies the device state that you subscribe to.

 |
| 

callback

 | 

Callback<[MonitorEventData](#section38571246164212)\>

 | 

Yes

 | 

Callback function, which is executed after the state changes and is passed to [MonitorEventData](#section38571246164212). You are advised to ensure that the callback's lifecycle is extended until the subscription is canceled. For details, please refer to [unsubscribeEvent](#section182736075018).

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

Promise object. Promise that returns no value.

 |

**Error codes**:

For details about the error codes, please refer to [Wear Engine ArkTS API Error Codes](../../arkts-api-error-codes/document.md).

| 
Error Code

 | 

Error Message

 |
| :-- | :-- |
| 

[401](../../arkts-api-error-codes/document.md#section201741341307)

 | 

Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed.

 |
| 

[1008500001](../../arkts-api-error-codes/document.md#section1047474644710)

 | 

Network error. The network is unavailable.

 |
| 

[1008500002](../../arkts-api-error-codes/document.md#section18859424615)

 | 

No device is bound.

 |
| 

[1008500003](../../arkts-api-error-codes/document.md#section11616131326)

 | 

Device disconnected.

 |
| 

[1008500004](../../arkts-api-error-codes/document.md#section485113712218)

 | 

App has not applied for the Wear Engine service.

 |
| 

[1008500005](../../arkts-api-error-codes/document.md#section665613120197)

 | 

The HUAWEI ID is not authorized.

 |
| 

[1008500006](../../arkts-api-error-codes/document.md#section1461311549277)

 | 

User privacy is not agreed.

 |
| 

[1008500007](../../arkts-api-error-codes/document.md#section15917165718219)

 | 

The device capability is not supported.

 |
| 

[1008500008](../../arkts-api-error-codes/document.md#section612518413314)

 | 

Account error. The user has not logged in with HUAWEI ID.

 |
| 

[1008500009](../../arkts-api-error-codes/document.md#section94850224314)

 | 

Account error. Failed to obtain account information with HUAWEI ID.

 |
| 

[1008500010](../../arkts-api-error-codes/document.md#section411611281734)

 | 

Device ID is invalid.

 |
| 

[1008500012](../../arkts-api-error-codes/document.md#section1599615141614)

 | 

Too many callbacks of the same type.

 |
| 

[1008509999](../../arkts-api-error-codes/document.md#section93011432734)

 | 

Internal error.

 |

**Example:**

import { wearEngine } from '@kit.WearEngine';
import { BusinessError } from '@kit.BasicServicesKit';

let deviceClient: wearEngine.DeviceClient = wearEngine.getDeviceClient(this.getUIContext().getHostContext());
let monitorClient: wearEngine.MonitorClient = wearEngine.getMonitorClient(this.getUIContext().getHostContext());
let devices: wearEngine.Device\[\] = await deviceClient.getConnectedDevices();

if (devices.length > 0) {
  // Select the target device from the obtained device list and define it as **device**. (Assume that there are connected devices in the array and the first one is the target device.)
  let device: wearEngine.Device = devices\[0\];

  let callback = (monitorEventData: wearEngine.MonitorEventData) => {
    console.info(\`Succeeded in listening change of ${monitorEventData.event}, the new status is ${monitorEventData.data}.\`)
  }
  monitorClient.subscribeEvent(device.randomId, wearEngine.MonitorEvent.EVENT\_WEAR\_STATUS\_CHANGED, callback).then(() => {
    console.info(\`Succeeded in subscribing wear status.\`);
  }).catch((error: BusinessError) => {
    console.error(\`Failed to subscribe wear status. Code is ${error.code}, message is ${error.message}.\`);
  })
}

#### \[h2\]unsubscribeEvent

unsubscribeEvent(deviceRandomId: string, type: MonitorEvent, callback: Callback<MonitorEventData>): Promise<void>

Unsubscribes from the change event of a specific device's specified state. This API uses a promise to return the unsubscription result asynchronously.

**Model restriction**: This API can be used only in the stage model.

**System capability**: SystemCapability.Health.WearEngine

**Device behavior differences**: This API is supported on phones and tablets. On other devices, it returns error code 801.

**Start version**: 5.0.0(12)

**Parameters:**

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

deviceRandomId

 | 

string

 | 

Yes

 | 

Random identifier of a [Device](#section385118379447), which specifies the device involved in the unsubscription.

 |
| 

type

 | 

[MonitorEvent](#section0407141762619)

 | 

Yes

 | 

Device state enum, which specifies the device state that you unsubscribe from.

 |
| 

callback

 | 

Callback<[MonitorEventData](#section38571246164212)\>

 | 

Yes

 | 

Callback function, which must be the same as the callback function passed for calling [subscribeEvent](#section74368231248).

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

Promise object. Promise that returns no value.

 |

**Error codes**:

For details about the error codes, please refer to [Wear Engine ArkTS API Error Codes](../../arkts-api-error-codes/document.md).

| 
Error Code

 | 

Error Message

 |
| :-- | :-- |
| 

[401](../../arkts-api-error-codes/document.md#section201741341307)

 | 

Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed.

 |
| 

[1008500001](../../arkts-api-error-codes/document.md#section1047474644710)

 | 

Network error. The network is unavailable.

 |
| 

[1008500002](../../arkts-api-error-codes/document.md#section18859424615)

 | 

No device is bound.

 |
| 

[1008500003](../../arkts-api-error-codes/document.md#section11616131326)

 | 

Device disconnected.

 |
| 

[1008500004](../../arkts-api-error-codes/document.md#section485113712218)

 | 

App has not applied for the Wear Engine service.

 |
| 

[1008500005](../../arkts-api-error-codes/document.md#section665613120197)

 | 

The HUAWEI ID is not authorized.

 |
| 

[1008500006](../../arkts-api-error-codes/document.md#section1461311549277)

 | 

User privacy is not agreed.

 |
| 

[1008500007](../../arkts-api-error-codes/document.md#section15917165718219)

 | 

The device capability is not supported.

 |
| 

[1008500008](../../arkts-api-error-codes/document.md#section612518413314)

 | 

Account error. The user has not logged in with HUAWEI ID.

 |
| 

[1008500009](../../arkts-api-error-codes/document.md#section94850224314)

 | 

Account error. Failed to obtain account information with HUAWEI ID.

 |
| 

[1008500010](../../arkts-api-error-codes/document.md#section411611281734)

 | 

Device ID is invalid.

 |
| 

[1008509999](../../arkts-api-error-codes/document.md#section93011432734)

 | 

Internal error.

 |

**Example:**

import { wearEngine } from '@kit.WearEngine';
import { BusinessError } from '@kit.BasicServicesKit';

let deviceClient: wearEngine.DeviceClient = wearEngine.getDeviceClient(this.getUIContext().getHostContext());
let devices: wearEngine.Device\[\] = await deviceClient.getConnectedDevices();
let monitorClient: wearEngine.MonitorClient = wearEngine.getMonitorClient(this.getUIContext().getHostContext());

if (devices.length > 0) {
  // Select the target device from the obtained device list and define it as **device**. (Assume that there are connected devices in the array and the first one is the target device.)
  let device: wearEngine.Device = devices\[0\];

  // The callback function for deregistration must be the same as that for registration.
  let callback = (monitorEventData: wearEngine.MonitorEventData) => {
    console.info(\`Succeeded in listening change of ${monitorEventData.event}, the new status is ${monitorEventData.data}.\`)
  }
  // Create a subscription task to be deleted.
  await monitorClient.subscribeEvent(device.randomId, wearEngine.MonitorEvent.EVENT\_WEAR\_STATUS\_CHANGED, callback);
// Delete the subscription task you have created.
  monitorClient.unsubscribeEvent(device.randomId, wearEngine.MonitorEvent.EVENT\_WEAR\_STATUS\_CHANGED, callback).then(() => {
    console.info(\`Succeeded in unsubscribing wear status\`);
  }).catch((error: BusinessError) => {
    console.error(\`Failed to unsubscribe wear status. Code is ${error.code}, message is ${error.message}.\`);
  })
}

#### MonitorItem

Enumeration class of device status.

**Model restriction**: This API can be used only in the stage model.

**System capability**: SystemCapability.Health.WearEngine

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

WEAR\_STATUS

 | 

wearStatus

 | 

Wearing status. Return value:

**1**: The wearable is worn.

**2**: The wearable is not worn.

 |
| 

POWER\_STATUS

 | 

powerStatus

 | 

Battery level. Return value: ranges from **0** to **100**, indicating the remaining battery level.

 |
| 

CHARGE\_STATUS

 | 

chargeStatus

 | 

Charging status. Return value:

**1**: The device is being charged.

**2**: The device is not being charged.

**3**: The device has been fully charged.

 |
| 

AVAILABLE\_STORAGE\_SPACE

 | 

availableStorageSpace

 | 

Available storage space. The return value indicates the available space for a user (KB).

 |
| 

POWER\_MODE

 | 

powerMode

 | 

Power mode. Return value:

**\-1**: The device does not differentiate between power modes.

**0**: smart mode

**1**: ultra-long battery life mode

 |

#### MonitorEvent

Enumeration class of device status change events.

**Model restriction**: This API can be used only in the stage model.

**System capability**: SystemCapability.Health.WearEngine

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

EVENT\_CONNECTION\_STATUS\_CHANGED

 | 

connectionStatus

 | 

The device connection status changes.

Return value: **2**: connected; **3**: disconnected; **5**: unlinked

 |
| 

EVENT\_BATTERY\_LEVEL\_DROPPED

 | 

lowPower

 | 

The device battery level decreases.

Return value: ranges from **0** to **100**, indicating the remaining battery level.

 |
| 

EVENT\_WEAR\_STATUS\_CHANGED

 | 

wearStatus

 | 

The device wearing status changes.

Return value: **1**: worn; **2**: not worn.

 |
| 

EVENT\_HEART\_RATE\_ALARM

 | 

heartRateAlarm

 | 

A heart rate alert is reported.

Return value: **1**: resting heart rate too high; **2**: resting heart rate too low; **3**: exercise heart rate too high; **4**: exercise heart rate too low.

 |
| 

EVENT\_CHARGE\_STATUS\_CHANGED

 | 

chargeStatus

 | 

The charging status changes.

Return value: **1**: charging started; **2**: charging ended; **3**: charging completed.

 |
| 

EVENT\_POWER\_MODE\_CHANGED

 | 

powerMode

 | 

The device switches to another power mode.

Return value: **0**: to Smart mode; **1**: to Ultra-long Battery Life mode.

 |

#### MonitorData

Returns the device state information as the return value of [queryStatus](#section3383841153218) and the input parameter for [subscribeEvent](#section74368231248).

**Model restriction**: This API can be used only in the stage model.

**System capability**: SystemCapability.Health.WearEngine

**Start version**: 5.0.0(12)

| 
Name

 | 

Type

 | 

Read-only

 | 

Optional

 | 

Description

 |
| :-- | :-- | :-- | :-- | :-- |
| 

code

 | 

number

 | 

No

 | 

No

 | 

For details about the return value, refer to [MonitorItem](#section16422462613) if you call [queryStatus](#section3383841153218) to query the device status;

refer to [MonitorEvent](#section0407141762619) if you call [subscribeEvent](#section74368231248) to subscribe to events.

 |
| 

data

 | 

string

 | 

No

 | 

Yes

 | 

Extended field.

 |

#### MonitorEventData

Passes the updated device state to the callback function as an input parameter, when the event you subscribe to by calling [subscribeEvent](#section74368231248) is triggered.

**Model restriction**: This API can be used only in the stage model.

**System capability**: SystemCapability.Health.WearEngine

**Start version**: 5.0.0(12)

| 
Name

 | 

Type

 | 

Read-only

 | 

Optional

 | 

Description

 |
| :-- | :-- | :-- | :-- | :-- |
| 

event

 | 

[MonitorEvent](#section0407141762619)

 | 

No

 | 

No

 | 

Enum of subscription events registered in the callback function.

 |
| 

data

 | 

[MonitorData](#section12024822410)

 | 

No

 | 

No

 | 

Updated device state.

 |

#### wearEngine.getP2pClient

getP2pClient(context: common.Context): P2pClient

Obtains the client of the P2P module.

**Model restriction**: This API can be used only in the stage model.

**System capability**: SystemCapability.Health.WearEngine

**Start version**: 5.0.0(12)

**Parameters:**

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

[common.Context](../../../../../application-framework/ability-kit/arkts-apis/dependent-elements-and-definitions/application/context-context-base-class-of-the-stage-model/document.md#context)

 | 

Yes

 | 

Context. Only the context that contains the **connectServiceExtensionAbility** method is supported (example: [UIAbilityContext](../../../../../application-framework/ability-kit/arkts-apis/dependent-elements-and-definitions/application/uiabilitycontext/document.md#uiabilitycontext-1)).

 |

**Returns**:

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

[P2pClient](#section10175450143316)

 | 

P2P client, which stores methods related to the P2P module.

 |

**Error codes**:

For details about the error codes, please refer to [Wear Engine ArkTS API Error Codes](../../arkts-api-error-codes/document.md).

| 
Error Code

 | 

Error Message

 |
| :-- | :-- |
| 

[401](../../arkts-api-error-codes/document.md#section201741341307)

 | 

Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types.

 |
| 

[1008509999](../../arkts-api-error-codes/document.md#section93011432734)

 | 

Internal error.

 |

**Example:**

import { wearEngine } from '@kit.WearEngine';

let p2pClient: wearEngine.P2pClient = wearEngine.getP2pClient(this.getUIContext().getHostContext());
console.info(\`Succeeded in getting p2p client.\`);

#### P2pClient

P2P client class, which is returned by [wearEngine.getP2pClient](#section15604103515412).

**Model restriction**: This API can be used only in the stage model.

**System capability**: SystemCapability.Health.WearEngine

**Start version**: 5.0.0(12)

#### \[h2\]isRemoteAppInstalled

isRemoteAppInstalled(deviceRandomId: string, remoteBundleName: string): Promise<boolean>

Checks whether a specified app has been installed on the wearable device. This API returns the result asynchronously through a promise.

**Model restriction**: This API can be used only in the stage model.

**System capability**: SystemCapability.Health.WearEngine

**Start version**: 5.0.0(12)

**Parameters:**

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

deviceRandomId

 | 

string

 | 

Yes

 | 

Random identifier of a [Device](#section385118379447), which specifies the device involved in the subscription.

 |
| 

remoteBundleName

 | 

string

 | 

Yes

 | 

Name of the device-side app to be queried.

 |

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

Promise object, indicating whether a specified app is installed on the device. **true**: installed; **false**: not installed

 |

**Error codes**:

For details about the error codes, please refer to [Wear Engine ArkTS API Error Codes](../../arkts-api-error-codes/document.md).

| 
Error Code

 | 

Error Message

 |
| :-- | :-- |
| 

[401](../../arkts-api-error-codes/document.md#section201741341307)

 | 

Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed.

 |
| 

[1008500001](../../arkts-api-error-codes/document.md#section1047474644710)

 | 

Network error. The network is unavailable.

 |
| 

[1008500002](../../arkts-api-error-codes/document.md#section18859424615)

 | 

No device is bound.

 |
| 

[1008500003](../../arkts-api-error-codes/document.md#section11616131326)

 | 

Device disconnected.

 |
| 

[1008500004](../../arkts-api-error-codes/document.md#section485113712218)

 | 

App has not applied for the Wear Engine service.

 |
| 

[1008500005](../../arkts-api-error-codes/document.md#section665613120197)

 | 

The HUAWEI ID is not authorized.

 |
| 

[1008500006](../../arkts-api-error-codes/document.md#section1461311549277)

 | 

User privacy is not agreed.

 |
| 

[1008500007](../../arkts-api-error-codes/document.md#section15917165718219)

 | 

The device capability is not supported.

 |
| 

[1008500008](../../arkts-api-error-codes/document.md#section612518413314)

 | 

Account error. The user has not logged in with HUAWEI ID.

 |
| 

[1008500009](../../arkts-api-error-codes/document.md#section94850224314)

 | 

Account error. Failed to obtain account information with HUAWEI ID.

 |
| 

[1008500010](../../arkts-api-error-codes/document.md#section411611281734)

 | 

Device ID is invalid.

 |
| 

[1008509999](../../arkts-api-error-codes/document.md#section93011432734)

 | 

Internal error.

 |

**Example:**

import { wearEngine } from '@kit.WearEngine';
import { BusinessError } from '@kit.BasicServicesKit';

let deviceClient: wearEngine.DeviceClient = wearEngine.getDeviceClient(this.getUIContext().getHostContext());
let p2pClient: wearEngine.P2pClient = wearEngine.getP2pClient(this.getUIContext().getHostContext());
let deviceList: wearEngine.Device\[\] = await deviceClient.getConnectedDevices();

deviceList.forEach(async (device, idx, arr) => {
  // Select the device that supports app installation.
  if (await device.isDeviceCapabilitySupported(wearEngine.DeviceCapability.APP\_INSTALLATION)) {
    // Define the device-side app bundle name as **remoteBundleName**.
    let remoteBundleName: string = '';

    p2pClient.isRemoteAppInstalled(device.randomId, remoteBundleName).then((isInstall) => {
      console.info(\`Succeeded in checking remote app install, result is ${isInstall}.\`);
    }).catch((error: BusinessError) => {
      console.error(\`Failed to check remote app install. Code is ${error.code}, message is ${error.message}.\`);
    })
  }
  if (idx === deviceList.length - 1) {
    // An error is thrown if the target device does not exist.
    throw new Error('cannot find target device');
  }
})

#### \[h2\]getRemoteAppVersion

getRemoteAppVersion(deviceRandomId: string, remoteBundleName: string): Promise<number>

Obtains the version number of a specified app on the wearable device. This API returns the result asynchronously through a promise.

**Model restriction**: This API can be used only in the stage model.

**System capability**: SystemCapability.Health.WearEngine

**Device behavior differences**: This API is supported on phones and tablets. On other devices, it returns error code 801.

**Start version**: 5.0.0(12)

**Parameters:**

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

deviceRandomId

 | 

string

 | 

Yes

 | 

Random identifier of a [Device](#section385118379447), which specifies the device involved in the subscription.

 |
| 

remoteBundleName

 | 

string

 | 

Yes

 | 

Name of the device-side app whose version number is to be queried.

 |

**Returns**:

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

Promise<number>

 | 

Promise object, indicating the device-side app version number.

 |

**Error codes**:

For details about the error codes, please refer to [Wear Engine ArkTS API Error Codes](../../arkts-api-error-codes/document.md).

| 
Error Code

 | 

Error Message

 |
| :-- | :-- |
| 

[401](../../arkts-api-error-codes/document.md#section201741341307)

 | 

Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed.

 |
| 

[801](../../arkts-api-error-codes/document.md#section5941173162512)

 | 

Capability not supported.

 |
| 

[1008500001](../../arkts-api-error-codes/document.md#section1047474644710)

 | 

Network error. The network is unavailable.

 |
| 

[1008500002](../../arkts-api-error-codes/document.md#section18859424615)

 | 

No device is bound.

 |
| 

[1008500003](../../arkts-api-error-codes/document.md#section11616131326)

 | 

Device disconnected.

 |
| 

[1008500004](../../arkts-api-error-codes/document.md#section485113712218)

 | 

App has not applied for the Wear Engine service.

 |
| 

[1008500005](../../arkts-api-error-codes/document.md#section665613120197)

 | 

The HUAWEI ID is not authorized.

 |
| 

[1008500006](../../arkts-api-error-codes/document.md#section1461311549277)

 | 

User privacy is not agreed.

 |
| 

[1008500007](../../arkts-api-error-codes/document.md#section15917165718219)

 | 

The device capability is not supported.

 |
| 

[1008500008](../../arkts-api-error-codes/document.md#section612518413314)

 | 

Account error. The user has not logged in with HUAWEI ID.

 |
| 

[1008500009](../../arkts-api-error-codes/document.md#section94850224314)

 | 

Account error. Failed to obtain account information with HUAWEI ID.

 |
| 

[1008500010](../../arkts-api-error-codes/document.md#section411611281734)

 | 

Device ID is invalid.

 |
| 

[1008509999](../../arkts-api-error-codes/document.md#section93011432734)

 | 

Internal error.

 |

**Example:**

import { wearEngine } from '@kit.WearEngine';
import { BusinessError } from '@kit.BasicServicesKit';

let deviceClient: wearEngine.DeviceClient = wearEngine.getDeviceClient(this.getUIContext().getHostContext());
let p2pClient: wearEngine.P2pClient = wearEngine.getP2pClient(this.getUIContext().getHostContext());
let deviceList: wearEngine.Device\[\] = await deviceClient.getConnectedDevices();

deviceList.forEach(async (device, idx, arr) => {
  // Select the device that supports app installation.
  if (await device.isDeviceCapabilitySupported(wearEngine.DeviceCapability.APP\_INSTALLATION)) {
    // Define the device-side app bundle name as **remoteBundleName**.
    let remoteBundleName: string = '';

    p2pClient.getRemoteAppVersion(device.randomId, remoteBundleName).then((version) => {
      console.info(\`Succeeded in getting remote app version, version is ${version}.\`);
    }).catch((error: BusinessError) => {
      console.error(\`Failed to check get remote app version. Code is ${error.code}, message is ${error.message}.\`);
    })
  }
  if (idx === deviceList.length - 1) {
    // An error is thrown if the target device does not exist.
    throw new Error('cannot find target device');
  }
})

#### \[h2\]startRemoteApp

startRemoteApp(deviceRandomId: string, remoteBundleName: string, transformLocalBundleName?: boolean): Promise<P2pResult>

Starts a specified app on the wearable device. This API returns the result asynchronously through a promise.

**Model restriction**: This API can be used only in the stage model.

**System capability**: SystemCapability.Health.WearEngine

**Device behavior differences**: This API is supported on phones and tablets. On other devices, it returns error code 801.

**Start version**: 5.0.0(12)

**Parameters:**

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

deviceRandomId

 | 

string

 | 

Yes

 | 

Random identifier of a [Device](#section385118379447), which specifies the device involved in the subscription.

 |
| 

remoteBundleName

 | 

string

 | 

Yes

 | 

Name of the device-side app to be started.

 |
| 

transformLocalBundleName

 | 

boolean

 | 

No

 | 

Indicates whether to convert the local bundle name and fingerprint to match those stored on the cloud for compatible apps. Default value: **false**.

**true**: yes; **false**: no.

For details about how to set an app to a compatible one, please refer to [Applying for Integrating Wear Engine](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/wearengine_apply).

 |

**Returns**:

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

Promise<[P2pResult](#section75108813115)\>

 | 

Promise object. The **code** field in its attributes indicates the app startup result.

 |

**Error codes**:

For details about the error codes, please refer to [Wear Engine ArkTS API Error Codes](../../arkts-api-error-codes/document.md).

| 
Error Code

 | 

Error Message

 |
| :-- | :-- |
| 

[401](../../arkts-api-error-codes/document.md#section201741341307)

 | 

Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed.

 |
| 

[801](../../arkts-api-error-codes/document.md#section5941173162512)

 | 

Capability not supported.

 |
| 

[1008500001](../../arkts-api-error-codes/document.md#section1047474644710)

 | 

Network error. The network is unavailable.

 |
| 

[1008500002](../../arkts-api-error-codes/document.md#section18859424615)

 | 

No device is bound.

 |
| 

[1008500003](../../arkts-api-error-codes/document.md#section11616131326)

 | 

Device disconnected.

 |
| 

[1008500004](../../arkts-api-error-codes/document.md#section485113712218)

 | 

App has not applied for the Wear Engine service.

 |
| 

[1008500005](../../arkts-api-error-codes/document.md#section665613120197)

 | 

The HUAWEI ID is not authorized.

 |
| 

[1008500006](../../arkts-api-error-codes/document.md#section1461311549277)

 | 

User privacy is not agreed.

 |
| 

[1008500007](../../arkts-api-error-codes/document.md#section15917165718219)

 | 

The device capability is not supported.

 |
| 

[1008500008](../../arkts-api-error-codes/document.md#section612518413314)

 | 

Account error. The user has not logged in with HUAWEI ID.

 |
| 

[1008500009](../../arkts-api-error-codes/document.md#section94850224314)

 | 

Account error. Failed to obtain account information with HUAWEI ID.

 |
| 

[1008500010](../../arkts-api-error-codes/document.md#section411611281734)

 | 

Device ID is invalid.

 |
| 

[1008509999](../../arkts-api-error-codes/document.md#section93011432734)

 | 

Internal error.

 |

**Example:**

import { wearEngine } from '@kit.WearEngine';
import { BusinessError } from '@kit.BasicServicesKit';

let deviceClient: wearEngine.DeviceClient = wearEngine.getDeviceClient(this.getUIContext().getHostContext());
let p2pClient: wearEngine.P2pClient = wearEngine.getP2pClient(this.getUIContext().getHostContext());
let deviceList: wearEngine.Device\[\] = await deviceClient.getConnectedDevices();

deviceList.forEach(async (device, idx, arr) => {
  // Select the device that supports app installation.
  if (await device.isDeviceCapabilitySupported(wearEngine.DeviceCapability.APP\_INSTALLATION)) {
    // Define the device-side app bundle name as **remoteBundleName**.
    let remoteBundleName: string = '';

    // The default value of **transformLocalBundleName** is **false**.
    p2pClient.startRemoteApp(device.randomId, remoteBundleName).then((p2pResult) => {
      console.info(\`Succeeded in starting remote app, result is ${p2pResult.code}.\`);
    }).catch((error: BusinessError) => {
      console.error(\`Failed to start remote app. Code is ${error.code}, message is ${error.message}.\`);
    })
  }
  if (idx === deviceList.length - 1) {
    // An error is thrown if the target device does not exist.
    throw new Error('cannot find target device');
  }
})

#### \[h2\]sendMessage

sendMessage(deviceRandomId: string, appParam: P2pAppParam, message: P2pMessage): Promise<P2pResult>

Sends messages to a specified app on the peer device. This API returns the result asynchronously through a promise.

**Model restriction**: This API can be used only in the stage model.

**System capability**: SystemCapability.Health.WearEngine

**Start version**: 5.0.0(12)

**Parameters:**

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

deviceRandomId

 | 

string

 | 

Yes

 | 

Random identifier of a [Device](#section385118379447), which specifies the device involved in the subscription.

 |
| 

appParam

 | 

[P2pAppParam](#section7874153142020)

 | 

Yes

 | 

Parameters of a specified device-side app.

 |
| 

message

 | 

[P2pMessage](#section188531948121319)

 | 

Yes

 | 

Message content to be sent. Value range (in bytes): \[1, 4096).

 |

**Returns**:

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

Promise<[P2pResult](#section75108813115)\>

 | 

Promise object, which returns a [P2pResult](#section75108813115) object. The **code** field in its attributes indicates the message sending result.

 |

**Error codes**:

For details about the error codes, please refer to [Wear Engine ArkTS API Error Codes](../../arkts-api-error-codes/document.md).

| 
Error Code

 | 

Error Message

 |
| :-- | :-- |
| 

[401](../../arkts-api-error-codes/document.md#section201741341307)

 | 

Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed.

 |
| 

[1008500001](../../arkts-api-error-codes/document.md#section1047474644710)

 | 

Network error. The network is unavailable.

 |
| 

[1008500002](../../arkts-api-error-codes/document.md#section18859424615)

 | 

No device is bound.

 |
| 

[1008500003](../../arkts-api-error-codes/document.md#section11616131326)

 | 

Device disconnected.

 |
| 

[1008500004](../../arkts-api-error-codes/document.md#section485113712218)

 | 

App has not applied for the Wear Engine service.

 |
| 

[1008500005](../../arkts-api-error-codes/document.md#section665613120197)

 | 

The HUAWEI ID is not authorized.

 |
| 

[1008500006](../../arkts-api-error-codes/document.md#section1461311549277)

 | 

User privacy is not agreed.

 |
| 

[1008500007](../../arkts-api-error-codes/document.md#section15917165718219)

 | 

The device capability is not supported.

 |
| 

[1008500008](../../arkts-api-error-codes/document.md#section612518413314)

 | 

Account error. The user has not logged in with HUAWEI ID.

 |
| 

[1008500009](../../arkts-api-error-codes/document.md#section94850224314)

 | 

Account error. Failed to obtain account information with HUAWEI ID.

 |
| 

[1008500010](../../arkts-api-error-codes/document.md#section411611281734)

 | 

Device ID is invalid.

 |
| 

[1008509999](../../arkts-api-error-codes/document.md#section93011432734)

 | 

Internal error.

 |

**Example:**

import { wearEngine } from '@kit.WearEngine';
import { BusinessError } from '@kit.BasicServicesKit';
import { util } from '@kit.ArkTS';

let deviceClient: wearEngine.DeviceClient = wearEngine.getDeviceClient(this.getUIContext().getHostContext());
let p2pClient: wearEngine.P2pClient = wearEngine.getP2pClient(this.getUIContext().getHostContext());
let deviceList: wearEngine.Device\[\] = await deviceClient.getConnectedDevices();

deviceList.forEach(async (device, idx, arr) => {
  // Select the device that supports app installation.
  if (await device.isDeviceCapabilitySupported(wearEngine.DeviceCapability.APP\_INSTALLATION)) {
    // Set the device-side app information, including the bundle name and fingerprint.
    let appInfo: wearEngine.AppInfo = {
      bundleName: '',
      fingerprint: ''
    }
    // Define the device-side app parameter class as **appParam**.
    let appParam: wearEngine.P2pAppParam = {
      remoteApp: appInfo
      // The default value of **transformLocalAppInfo** is **false**, indicating that the bundle name and fingerprint are not converted.
    }

    // Set the message to be sent.
    let messageContent: string = 'this is message';
    let textEncoder: util.TextEncoder = new util.TextEncoder;
    let message: wearEngine.P2pMessage = {
      content: textEncoder.encodeInto(messageContent)
    }

    p2pClient.sendMessage(device.randomId, appParam, message).then((p2pResult) => {
      console.info(\`Succeeded in sending message, result is ${p2pResult.code}.\`);
    }).catch((error: BusinessError) => {
      console.error(\`Failed to send message. Code is ${error.code}, message is ${error.message}.\`);
    })
  }
  if (idx === deviceList.length - 1) {
    // An error is thrown if the target device does not exist.
    throw new Error('cannot find target device');
  }
})

#### \[h2\]transferFile

transferFile(deviceRandomId: string, appParam: P2pAppParam, file: P2pFile, callback: AsyncCallback<P2pResult>): void

Sends a file to a specified app on the peer device. This API returns the result asynchronously through a callback.

**Model restriction**: This API can be used only in the stage model.

**System capability**: SystemCapability.Health.WearEngine

**Start version**: 5.0.0(12)

**Parameters:**

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

deviceRandomId

 | 

string

 | 

Yes

 | 

Random identifier of a [Device](#section385118379447), which specifies the device involved in the subscription.

 |
| 

appParam

 | 

[P2pAppParam](#section7874153142020)

 | 

Yes

 | 

Parameters of a specified device-side app.

 |
| 

file

 | 

[P2pFile](#section1223384152)

 | 

Yes

 | 

File to be transferred.

 |
| 

callback

 | 

AsyncCallback<[P2pResult](#section75108813115)\>

 | 

Yes

 | 

General callback function that carries error parameters and asynchronous return values.

 |

**Error codes**:

For details about the error codes, please refer to [Wear Engine ArkTS API Error Codes](../../arkts-api-error-codes/document.md).

| 
Error Code

 | 

Error Message

 |
| :-- | :-- |
| 

[401](../../arkts-api-error-codes/document.md#section201741341307)

 | 

Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed.

 |
| 

[1008500001](../../arkts-api-error-codes/document.md#section1047474644710)

 | 

Network error. The network is unavailable.

 |
| 

[1008500002](../../arkts-api-error-codes/document.md#section18859424615)

 | 

No device is bound.

 |
| 

[1008500003](../../arkts-api-error-codes/document.md#section11616131326)

 | 

Device disconnected.

 |
| 

[1008500004](../../arkts-api-error-codes/document.md#section485113712218)

 | 

App has not applied for the Wear Engine service.

 |
| 

[1008500005](../../arkts-api-error-codes/document.md#section665613120197)

 | 

The HUAWEI ID is not authorized.

 |
| 

[1008500006](../../arkts-api-error-codes/document.md#section1461311549277)

 | 

User privacy is not agreed.

 |
| 

[1008500007](../../arkts-api-error-codes/document.md#section15917165718219)

 | 

The device capability is not supported.

 |
| 

[1008500008](../../arkts-api-error-codes/document.md#section612518413314)

 | 

Account error. The user has not logged in with HUAWEI ID.

 |
| 

[1008500009](../../arkts-api-error-codes/document.md#section94850224314)

 | 

Account error. Failed to obtain account information with HUAWEI ID.

 |
| 

[1008500010](../../arkts-api-error-codes/document.md#section411611281734)

 | 

Device ID is invalid.

 |
| 

[1008500011](../../arkts-api-error-codes/document.md#section4583155021811)

 | 

File is invalid.

 |
| 

[1008509999](../../arkts-api-error-codes/document.md#section93011432734)

 | 

Internal error.

 |

**Example:**

import { wearEngine } from '@kit.WearEngine';
import { BusinessError } from '@kit.BasicServicesKit';
import { fileIo } from '@kit.CoreFileKit';

let deviceClient: wearEngine.DeviceClient = wearEngine.getDeviceClient(this.getUIContext().getHostContext());
let p2pClient: wearEngine.P2pClient = wearEngine.getP2pClient(this.getUIContext().getHostContext());
let deviceList: wearEngine.Device\[\] = await deviceClient.getConnectedDevices();

deviceList.forEach(async (device, idx, arr) => {
  // Select the device that supports app installation.
  if (await device.isDeviceCapabilitySupported(wearEngine.DeviceCapability.APP\_INSTALLATION)) {
    // Set the device-side app information, including the bundle name and fingerprint.
    let appInfo: wearEngine.AppInfo = {
      bundleName: '',
      fingerprint: ''
    }
    // Define the device-side app parameter class as **appParam**.
    let appParam: wearEngine.P2pAppParam = {
      remoteApp: appInfo
      // The default value of **transformLocalAppInfo** is **false**, indicating that the bundle name and fingerprint are not converted.
    }
    // Set the file to be sent.
    let p2pFile: wearEngine.P2pFile = {
      file: fileIo.openSync('')
    }

    p2pClient.transferFile(device.randomId, appParam, p2pFile, (error: BusinessError, p2pResult: wearEngine.P2pResult) => {
      // Callback processing logic.
      if (error) {
        console.error(\`Failed to transfer file. Code is ${error.code}, message is ${error.message}.\`);
        return;
      }
      if (p2pResult.code) {
        if (p2pResult.code === wearEngine.P2pResultCode.COMMUNICATION\_SUCCESS) {
          console.info(\`Succeeded in transfering file, the result is ${p2pResult.code}.\`);
        }
        console.info(\`Failed to transfer file, the error code is ${p2pResult.code}.\`);
      }
      if (p2pResult.progress) {
        console.info(\`Succeeded in transfering file, the progress is ${p2pResult.progress}.\`);
      }
    });
    fileIo.close(p2pFile.file);
  }
  if (idx === deviceList.length - 1) {
    // An error is thrown if the target device does not exist.
    throw new Error('cannot find target device');
  }
})

#### \[h2\]cancelFileTransfer

cancelFileTransfer(deviceRandomId: string, appParam: P2pAppParam, file: P2pFile): Promise<P2pResult>

Cancels file transfer to a specified app on the peer device. This API returns the result asynchronously through a promise.

**Model restriction**: This API can be used only in the stage model.

**System capability**: SystemCapability.Health.WearEngine

**Device behavior differences**: This API is supported on phones and tablets. On other devices, it returns error code 801.

**Start version**: 5.0.0(12)

**Parameters:**

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

deviceRandomId

 | 

string

 | 

Yes

 | 

Random identifier of a [Device](#section385118379447), which specifies the device involved in the subscription.

 |
| 

appParam

 | 

[P2pAppParam](#section7874153142020)

 | 

Yes

 | 

Parameters of a specified device-side app.

 |
| 

file

 | 

[P2pFile](#section1223384152)

 | 

Yes

 | 

File to be transferred.

 |

**Returns**:

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

Promise<[P2pResult](#section75108813115)\>

 | 

Promise object. The **code** field in its attributes indicates the result of the file transfer cancellation.

 |

**Error codes**:

For details about the error codes, please refer to [Wear Engine ArkTS API Error Codes](../../arkts-api-error-codes/document.md).

| 
Error Code

 | 

Error Message

 |
| :-- | :-- |
| 

[401](../../arkts-api-error-codes/document.md#section201741341307)

 | 

Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed.

 |
| 

[801](../../arkts-api-error-codes/document.md#section5941173162512)

 | 

Capability not supported.

 |
| 

[1008500001](../../arkts-api-error-codes/document.md#section1047474644710)

 | 

Network error. The network is unavailable.

 |
| 

[1008500002](../../arkts-api-error-codes/document.md#section18859424615)

 | 

No device is bound.

 |
| 

[1008500003](../../arkts-api-error-codes/document.md#section11616131326)

 | 

Device disconnected.

 |
| 

[1008500004](../../arkts-api-error-codes/document.md#section485113712218)

 | 

App has not applied for the Wear Engine service.

 |
| 

[1008500005](../../arkts-api-error-codes/document.md#section665613120197)

 | 

The HUAWEI ID is not authorized.

 |
| 

[1008500006](../../arkts-api-error-codes/document.md#section1461311549277)

 | 

User privacy is not agreed.

 |
| 

[1008500007](../../arkts-api-error-codes/document.md#section15917165718219)

 | 

The device capability is not supported.

 |
| 

[1008500008](../../arkts-api-error-codes/document.md#section612518413314)

 | 

Account error. The user has not logged in with HUAWEI ID.

 |
| 

[1008500009](../../arkts-api-error-codes/document.md#section94850224314)

 | 

Account error. Failed to obtain account information with HUAWEI ID.

 |
| 

[1008500010](../../arkts-api-error-codes/document.md#section411611281734)

 | 

Device ID is invalid.

 |
| 

[1008500011](../../arkts-api-error-codes/document.md#section4583155021811)

 | 

File is invalid.

 |
| 

[1008509999](../../arkts-api-error-codes/document.md#section93011432734)

 | 

Internal error.

 |

**Example:**

import { wearEngine } from '@kit.WearEngine';
import { BusinessError } from '@kit.BasicServicesKit';
import { fileIo } from '@kit.CoreFileKit';

let deviceClient: wearEngine.DeviceClient = wearEngine.getDeviceClient(this.getUIContext().getHostContext());
let p2pClient: wearEngine.P2pClient = wearEngine.getP2pClient(this.getUIContext().getHostContext());
let deviceList: wearEngine.Device\[\] = await deviceClient.getConnectedDevices();

deviceList.forEach(async (device, idx, arr) => {
  // Select the device that supports app installation.
  if (await device.isDeviceCapabilitySupported(wearEngine.DeviceCapability.APP\_INSTALLATION)) {
    // Set the device-side app information, including the bundle name and fingerprint.
    let appInfo: wearEngine.AppInfo = {
      bundleName: '',
      fingerprint: ''
    }
    // Define the device-side app parameter class as **appParam**.
    let appParam: wearEngine.P2pAppParam = {
      remoteApp: appInfo
      // The default value of **transformLocalAppInfo** is **false**, indicating that the bundle name and fingerprint are not converted.
    }
    // Set information about the file to be sent.
    let p2pFile: wearEngine.P2pFile = {
      file: fileIo.openSync('')
    }

    p2pClient.transferFile(device.randomId, appParam, p2pFile, () => {
      // Execution logic of the callback function.
    })

    p2pClient.cancelFileTransfer(device.randomId, appParam, p2pFile).then((p2pResult) => {
      if (p2pResult.code === wearEngine.P2pResultCode.COMMUNICATION\_SUCCESS) {
        console.info(\`Succeeded in cancelling transfer file, the result is ${p2pResult.code}.\`);
      }
    }).catch((error: BusinessError) => {
      console.error(\`Failed to cancel transfer file. Code is ${error.code}, message is ${error.message}.\`);
    })
    fileIo.close(p2pFile.file);
  }
  if (idx === deviceList.length - 1) {
    // An error is thrown if the target device does not exist.
    throw new Error('cannot find target device');
  }
})

#### \[h2\]registerMessageReceiver

registerMessageReceiver(deviceRandomId: string, appParam: P2pAppParam, callback: Callback<P2pMessage>): Promise<void>

Subscribes to the event that an app on the peer device sends a message to the local device. This API uses a callback to return the event asynchronously when the local device receives the message sent by the app on the peer device, and uses a promise to return the subscription result asynchronously.

**Model restriction**: This API can be used only in the stage model.

**System capability**: SystemCapability.Health.WearEngine

**Start version**: 5.0.0(12)

**Parameters:**

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

deviceRandomId

 | 

string

 | 

Yes

 | 

Random identifier of a [Device](#section385118379447), which specifies the device involved in the subscription.

 |
| 

appParam

 | 

[P2pAppParam](#section7874153142020)

 | 

Yes

 | 

Device-side app parameters.

 |
| 

callback

 | 

Callback<[P2pMessage](#section188531948121319)\>

 | 

Yes

 | 

Callback function executed after the message sent by a device-side app is received.

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

Promise object. Promise that returns no value.

 |

**Error codes**:

For details about the error codes, please refer to [Wear Engine ArkTS API Error Codes](../../arkts-api-error-codes/document.md).

| 
Error Code

 | 

Error Message

 |
| :-- | :-- |
| 

[401](../../arkts-api-error-codes/document.md#section201741341307)

 | 

Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed.

 |
| 

[1008500001](../../arkts-api-error-codes/document.md#section1047474644710)

 | 

Network error. The network is unavailable.

 |
| 

[1008500002](../../arkts-api-error-codes/document.md#section18859424615)

 | 

No device is bound.

 |
| 

[1008500003](../../arkts-api-error-codes/document.md#section11616131326)

 | 

Device disconnected.

 |
| 

[1008500004](../../arkts-api-error-codes/document.md#section485113712218)

 | 

App has not applied for the Wear Engine service.

 |
| 

[1008500005](../../arkts-api-error-codes/document.md#section665613120197)

 | 

The HUAWEI ID is not authorized.

 |
| 

[1008500006](../../arkts-api-error-codes/document.md#section1461311549277)

 | 

User privacy is not agreed.

 |
| 

[1008500007](../../arkts-api-error-codes/document.md#section15917165718219)

 | 

The device capability is not supported.

 |
| 

[1008500008](../../arkts-api-error-codes/document.md#section612518413314)

 | 

Account error. The user has not logged in with HUAWEI ID.

 |
| 

[1008500009](../../arkts-api-error-codes/document.md#section94850224314)

 | 

Account error. Failed to obtain account information with HUAWEI ID.

 |
| 

[1008500010](../../arkts-api-error-codes/document.md#section411611281734)

 | 

Device ID is invalid.

 |
| 

[1008500012](../../arkts-api-error-codes/document.md#section1599615141614)

 | 

Too many callbacks of the same type.

 |
| 

[1008509999](../../arkts-api-error-codes/document.md#section93011432734)

 | 

Internal error.

 |

**Example:**

import { wearEngine } from '@kit.WearEngine';
import { BusinessError } from '@kit.BasicServicesKit';

let deviceClient: wearEngine.DeviceClient = wearEngine.getDeviceClient(this.getUIContext().getHostContext());
let p2pClient: wearEngine.P2pClient = wearEngine.getP2pClient(this.getUIContext().getHostContext());
let deviceList: wearEngine.Device\[\] = await deviceClient.getConnectedDevices();

deviceList.forEach(async (device, idx, arr) => {
  // Select the device that supports app installation.
  if (await device.isDeviceCapabilitySupported(wearEngine.DeviceCapability.APP\_INSTALLATION)) {
    // Set the device-side app information, including the bundle name and fingerprint.
    let appInfo: wearEngine.AppInfo = {
      bundleName: '',
      fingerprint: ''
    }
    // Define the device-side app parameter class as **appParam**.
    let appParam: wearEngine.P2pAppParam = {
      remoteApp: appInfo
      // The default value of **transformLocalAppInfo** is **false**, indicating that the bundle name is not converted.
    }
    // Set information about the file to be sent.
    let callback = (p2pMessage: wearEngine.P2pMessage) => {
      console.info(\`Succeeded in receiving message, the message is ${p2pMessage.content}.\`)
    }

    p2pClient.registerMessageReceiver(device.randomId, appParam, callback).then(() => {
      console.info(\`Succeeded in registering message receiver.\`);
    }).catch((error: BusinessError) => {
      console.error(\`Failed to register message receiver. Code is ${error.code}, message is ${error.message}.\`);
    })
  }
  if (idx === deviceList.length - 1) {
    // An error is thrown if the target device does not exist.
    throw new Error('cannot find target device');
  }
})

#### \[h2\]registerFileReceiver

registerFileReceiver(deviceRandomId: string, appParam: P2pAppParam, callback: Callback<P2pFile>): Promise<void>

Subscribes to the event that the peer device sends a file to the local device. This API uses a callback to return the event asynchronously when the local device receives the file sent by the peer device, and uses a promise to return the subscription result asynchronously.

**Model restriction**: This API can be used only in the stage model.

**System capability**: SystemCapability.Health.WearEngine

**Start version**: 5.0.0(12)

**Parameters:**

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

deviceRandomId

 | 

string

 | 

Yes

 | 

Random identifier of a [Device](#section385118379447), which specifies the device involved in the subscription.

 |
| 

appParam

 | 

[P2pAppParam](#section7874153142020)

 | 

Yes

 | 

Device-side app parameters.

 |
| 

callback

 | 

Callback<[P2pFile](#section1223384152)\>

 | 

Yes

 | 

Callback function executed after the file sent by a device-side app is received.

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

Promise object. Promise that returns no value.

 |

**Error codes**:

For details about the error codes, please refer to [Wear Engine ArkTS API Error Codes](../../arkts-api-error-codes/document.md).

| 
Error Code

 | 

Error Message

 |
| :-- | :-- |
| 

[401](../../arkts-api-error-codes/document.md#section201741341307)

 | 

Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed.

 |
| 

[1008500001](../../arkts-api-error-codes/document.md#section1047474644710)

 | 

Network error. The network is unavailable.

 |
| 

[1008500002](../../arkts-api-error-codes/document.md#section18859424615)

 | 

No device is bound.

 |
| 

[1008500003](../../arkts-api-error-codes/document.md#section11616131326)

 | 

Device disconnected.

 |
| 

[1008500004](../../arkts-api-error-codes/document.md#section485113712218)

 | 

App has not applied for the Wear Engine service.

 |
| 

[1008500005](../../arkts-api-error-codes/document.md#section665613120197)

 | 

The HUAWEI ID is not authorized.

 |
| 

[1008500006](../../arkts-api-error-codes/document.md#section1461311549277)

 | 

User privacy is not agreed.

 |
| 

[1008500007](../../arkts-api-error-codes/document.md#section15917165718219)

 | 

The device capability is not supported.

 |
| 

[1008500008](../../arkts-api-error-codes/document.md#section612518413314)

 | 

Account error. The user has not logged in with HUAWEI ID.

 |
| 

[1008500009](../../arkts-api-error-codes/document.md#section94850224314)

 | 

Account error. Failed to obtain account information with HUAWEI ID.

 |
| 

[1008500010](../../arkts-api-error-codes/document.md#section411611281734)

 | 

Device ID is invalid.

 |
| 

[1008500012](../../arkts-api-error-codes/document.md#section1599615141614)

 | 

Too many callbacks of the same type.

 |
| 

[1008509999](../../arkts-api-error-codes/document.md#section93011432734)

 | 

Internal error.

 |

**Example:**

import { wearEngine } from '@kit.WearEngine';
import { BusinessError } from '@kit.BasicServicesKit';

let deviceClient: wearEngine.DeviceClient = wearEngine.getDeviceClient(this.getUIContext().getHostContext());
let p2pClient: wearEngine.P2pClient = wearEngine.getP2pClient(this.getUIContext().getHostContext());
let deviceList: wearEngine.Device\[\] = await deviceClient.getConnectedDevices();

deviceList.forEach(async (device, idx, arr) => {
  // Select the device that supports app installation.
  if (await device.isDeviceCapabilitySupported(wearEngine.DeviceCapability.APP\_INSTALLATION)) {
    // Set the device-side app information, including the bundle name and fingerprint.
    let appInfo: wearEngine.AppInfo = {
      bundleName: '',
      fingerprint: ''
    }
    // Define the device-side app parameter class as **appParam**.
    let appParam: wearEngine.P2pAppParam = {
      remoteApp: appInfo
      // The default value of **transformLocalAppInfo** is **false**, indicating that the bundle name and fingerprint are not converted.
    }
    // Set information about the file to be sent.
    let callback = (p2pMessage: wearEngine.P2pFile) => {
      console.info(\`Succeeded in receiving file.\`)
    }

    p2pClient.registerFileReceiver(device.randomId, appParam, callback).then(() => {
      console.info(\`Succeeded in registering file receiver.\`)
    }).catch((error: BusinessError) => {
      console.error(\`Failed to register file receiver. Code is ${error.code}, message is ${error.message}.\`);
    })
  }
  if (idx === deviceList.length - 1) {
    // An error is thrown if the target device does not exist.
    throw new Error('cannot find target device');
  }
})

#### \[h2\]unregisterMessageReceiver

unregisterMessageReceiver(deviceRandomId: string, appParam: P2pAppParam, callback: Callback<P2pMessage>): Promise<void>

Unsubscribes from the event that an app on the peer device sends a message to the local device. This API uses a promise to return the unsubscription result asynchronously.

**Model restriction**: This API can be used only in the stage model.

**System capability**: SystemCapability.Health.WearEngine

**Start version**: 5.0.0(12)

**Parameters:**

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

deviceRandomId

 | 

string

 | 

Yes

 | 

Random identifier of a [Device](#section385118379447), which specifies the device involved in the subscription.

 |
| 

appParam

 | 

[P2pAppParam](#section7874153142020)

 | 

Yes

 | 

Device-side app parameters.

 |
| 

callback

 | 

Callback<[P2pMessage](#section188531948121319)\>

 | 

Yes

 | 

Callback function, which must be the same as the callback function used for subscription.

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

Promise object. Promise that returns no value.

 |

**Error codes**:

For details about the error codes, please refer to [Wear Engine ArkTS API Error Codes](../../arkts-api-error-codes/document.md).

| 
Error Code

 | 

Error Message

 |
| :-- | :-- |
| 

[401](../../arkts-api-error-codes/document.md#section201741341307)

 | 

Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed.

 |
| 

[1008500001](../../arkts-api-error-codes/document.md#section1047474644710)

 | 

Network error. The network is unavailable.

 |
| 

[1008500002](../../arkts-api-error-codes/document.md#section18859424615)

 | 

No device is bound.

 |
| 

[1008500003](../../arkts-api-error-codes/document.md#section11616131326)

 | 

Device disconnected.

 |
| 

[1008500004](../../arkts-api-error-codes/document.md#section485113712218)

 | 

App has not applied for the Wear Engine service.

 |
| 

[1008500005](../../arkts-api-error-codes/document.md#section665613120197)

 | 

The HUAWEI ID is not authorized.

 |
| 

[1008500006](../../arkts-api-error-codes/document.md#section1461311549277)

 | 

User privacy is not agreed.

 |
| 

[1008500007](../../arkts-api-error-codes/document.md#section15917165718219)

 | 

The device capability is not supported.

 |
| 

[1008500008](../../arkts-api-error-codes/document.md#section612518413314)

 | 

Account error. The user has not logged in with HUAWEI ID.

 |
| 

[1008500009](../../arkts-api-error-codes/document.md#section94850224314)

 | 

Account error. Failed to obtain account information with HUAWEI ID.

 |
| 

[1008500010](../../arkts-api-error-codes/document.md#section411611281734)

 | 

Device ID is invalid.

 |
| 

[1008509999](../../arkts-api-error-codes/document.md#section93011432734)

 | 

Internal error.

 |

**Example:**

import { wearEngine } from '@kit.WearEngine';
import { BusinessError } from '@kit.BasicServicesKit';

let deviceClient: wearEngine.DeviceClient = wearEngine.getDeviceClient(this.getUIContext().getHostContext());
let p2pClient: wearEngine.P2pClient = wearEngine.getP2pClient(this.getUIContext().getHostContext());
let deviceList: wearEngine.Device\[\] = await deviceClient.getConnectedDevices();

deviceList.forEach(async (device, idx, arr) => {
  // Select the device that supports app installation.
  if (await device.isDeviceCapabilitySupported(wearEngine.DeviceCapability.APP\_INSTALLATION)) {
    // Set the device-side app information, including the bundle name and fingerprint.
    let appInfo: wearEngine.AppInfo = {
      bundleName: '',
      fingerprint: ''
    }
    // Define the device-side app parameter class as **appParam**.
    let appParam: wearEngine.P2pAppParam = {
      remoteApp: appInfo
      // The default value of **transformLocalAppInfo** is **false**, indicating that the bundle name and fingerprint are not converted.
    }
    // Set information about the file to be sent.
    let callback = (p2pMessage: wearEngine.P2pMessage) => {
      console.info(\`Succeeded in receiving message, the message is ${p2pMessage.content}.\`)
    }

    p2pClient.registerMessageReceiver(device.randomId, appParam, callback).then(() => {
      console.info(\`Succeeded in registering message receiver.\`)
    }).catch((error: BusinessError) => {
      console.error(\`Failed to register message receiver. Code is ${error.code}, message is ${error.message}.\`);
    })

    p2pClient.unregisterMessageReceiver(device.randomId, appParam, callback).then(() => {
      console.info(\`Succeeded in unregistering message receiver.\`)
    }).catch((error: BusinessError) => {
      console.error(\`Failed to unregister message receiver. Code is ${error.code}, message is ${error.message}.\`);
    })
  }
  if (idx === deviceList.length - 1) {
    // An error is thrown if the target device does not exist.
    throw new Error('cannot find target device');
  }
})

#### \[h2\]unregisterFileReceiver

unregisterFileReceiver(deviceRandomId: string, appParam: P2pAppParam, callback: Callback<P2pFile>): Promise<void>

Unsubscribes from the event that an app on the peer device sends a file to the local device. This API uses a promise to return the unsubscription result asynchronously.

**Model restriction**: This API can be used only in the stage model.

**System capability**: SystemCapability.Health.WearEngine

**Start version**: 5.0.0(12)

**Parameters:**

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

deviceRandomId

 | 

string

 | 

Yes

 | 

Random identifier of a [Device](#section385118379447), which specifies the device involved in the subscription.

 |
| 

appParam

 | 

[P2pAppParam](#section7874153142020)

 | 

Yes

 | 

Device-side app parameters.

 |
| 

callback

 | 

Callback<[P2pFile](#section1223384152)\>

 | 

Yes

 | 

Callback function, which must be the same as the callback function used for subscription.

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

Promise object. Promise that returns no value.

 |

**Error codes**:

For details about the error codes, please refer to [Wear Engine ArkTS API Error Codes](../../arkts-api-error-codes/document.md).

| 
Error Code

 | 

Error Message

 |
| :-- | :-- |
| 

[401](../../arkts-api-error-codes/document.md#section201741341307)

 | 

Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed.

 |
| 

[1008500001](../../arkts-api-error-codes/document.md#section1047474644710)

 | 

Network error. The network is unavailable.

 |
| 

[1008500002](../../arkts-api-error-codes/document.md#section18859424615)

 | 

No device is bound.

 |
| 

[1008500003](../../arkts-api-error-codes/document.md#section11616131326)

 | 

Device disconnected.

 |
| 

[1008500004](../../arkts-api-error-codes/document.md#section485113712218)

 | 

App has not applied for the Wear Engine service.

 |
| 

[1008500005](../../arkts-api-error-codes/document.md#section665613120197)

 | 

The HUAWEI ID is not authorized.

 |
| 

[1008500006](../../arkts-api-error-codes/document.md#section1461311549277)

 | 

User privacy is not agreed.

 |
| 

[1008500007](../../arkts-api-error-codes/document.md#section15917165718219)

 | 

The device capability is not supported.

 |
| 

[1008500008](../../arkts-api-error-codes/document.md#section612518413314)

 | 

Account error. The user has not logged in with HUAWEI ID.

 |
| 

[1008500009](../../arkts-api-error-codes/document.md#section94850224314)

 | 

Account error. Failed to obtain account information with HUAWEI ID.

 |
| 

[1008500010](../../arkts-api-error-codes/document.md#section411611281734)

 | 

Device ID is invalid.

 |
| 

[1008509999](../../arkts-api-error-codes/document.md#section93011432734)

 | 

Internal error.

 |

**Example:**

import { wearEngine } from '@kit.WearEngine';
import { BusinessError } from '@kit.BasicServicesKit';

let deviceClient: wearEngine.DeviceClient = wearEngine.getDeviceClient(this.getUIContext().getHostContext());
let p2pClient: wearEngine.P2pClient = wearEngine.getP2pClient(this.getUIContext().getHostContext());
let deviceList: wearEngine.Device\[\] = await deviceClient.getConnectedDevices();

deviceList.forEach(async (device, idx, arr) => {
  // Select the device that supports app installation.
  if (await device.isDeviceCapabilitySupported(wearEngine.DeviceCapability.APP\_INSTALLATION)) {
    // Set the device-side app information, including the bundle name and fingerprint.
    let appInfo: wearEngine.AppInfo = {
      bundleName: '',
      fingerprint: ''
    }
    // Define the device-side app parameter class as **appParam**.
    let appParam: wearEngine.P2pAppParam = {
      remoteApp: appInfo
      // The default value of **transformLocalAppInfo** is **false**, indicating that the bundle name and fingerprint are not converted.
    }
    // Set information about the file to be sent.
    let callback = (p2pMessage: wearEngine.P2pFile) => {
      console.info(\`Succeeded in receiving file.\`)
    }

    p2pClient.registerFileReceiver(device.randomId, appParam, callback).then(() => {
      console.info(\`Succeeded in registering file receiver.\`);
    }).catch((error: BusinessError) => {
      console.error(\`Failed to register file receiver. Code is ${error.code}, message is ${error.message}.\`);
    })

    p2pClient.unregisterFileReceiver(device.randomId, appParam, callback).then(() => {
      console.info(\`Succeeded in unregistering file receiver.\`);
    }).catch((error: BusinessError) => {
      console.error(\`Failed to unregister file receiver. Code is ${error.code}, message is ${error.message}.\`);
    })
  }
  if (idx === deviceList.length - 1) {
    // An error is thrown if the target device does not exist.
    throw new Error('cannot find target device');
  }
})

#### AppInfo

Device-side app information class.

**Model restriction**: This API can be used only in the stage model.

**System capability**: SystemCapability.Health.WearEngine

**Start version**: 5.0.0(12)

| 
Name

 | 

Type

 | 

Read-only

 | 

Optional

 | 

Description

 |
| :-- | :-- | :-- | :-- | :-- |
| 

bundleName

 | 

string

 | 

No

 | 

No

 | 

App name.

 |
| 

fingerprint

 | 

string

 | 

No

 | 

No

 | 

Unique app identifier (app fingerprint or [app ID](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/wearengine_faq-9)).

**Note**: For wearables running HarmonyOS 5.0 or later versions, the app ID is passed; for all other devices, the app fingerprint is passed.

 |

#### P2pResultCode

Stores the return value enums of P2P communication.

**Model restriction**: This API can be used only in the stage model.

**System capability**: SystemCapability.Health.WearEngine

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

REMOTE\_APP\_NOT\_INSTALLED

 | 

200

 | 

The app is not installed on the device.

 |
| 

REMOTE\_APP\_NOT\_RUNNING

 | 

201

 | 

The app is not running on the device.

 |
| 

REMOTE\_APP\_RUNNING

 | 

202

 | 

The app is running on the device.

 |
| 

UNKNOWN\_ERROR

 | 

203

 | 

Unknown error.

 |
| 

COMMUNICATION\_FAILURE

 | 

206

 | 

The communication with the device-side app fails.

 |
| 

COMMUNICATION\_SUCCESS

 | 

207

 | 

The communication with the device-side app is successful.

 |

#### P2pResult

Stores the P2P communication result.

**Model restriction**: This API can be used only in the stage model.

**System capability**: SystemCapability.Health.WearEngine

**Start version**: 5.0.0(12)

| 
Name

 | 

Type

 | 

Read-only

 | 

Optional

 | 

Description

 |
| :-- | :-- | :-- | :-- | :-- |
| 

code

 | 

number

 | 

No

 | 

Yes

 | 

Used to return the P2P communication result except file transfer. For details about the return value, please refer to [P2pResultCode](#section34326155711).

 |
| 

progress

 | 

number

 | 

No

 | 

Yes

 | 

Only used to report the file transfer progress. The return value ranges from **0** to **100**.

 |

#### P2pMessage

Message class sent from an app the local device app to the peer device application.

**Model restriction**: This API can be used only in the stage model.

**System capability**: SystemCapability.Health.WearEngine

**Start version**: 5.0.0(12)

| 
Name

 | 

Type

 | 

Read-only

 | 

Optional

 | 

Description

 |
| :-- | :-- | :-- | :-- | :-- |
| 

content

 | 

Uint8Array

 | 

No

 | 

No

 | 

Content of the message to be transmitted, in Uint8Array (binary byte array) format.

 |

#### P2pFile

File class sent by the application on the local device to the application on the peer device.

**Model restriction**: This API can be used only in the stage model.

**System capability**: SystemCapability.Health.WearEngine

**Start version**: 5.0.0(12)

| 
Name

 | 

Type

 | 

Read-only

 | 

Optional

 | 

Description

 |
| :-- | :-- | :-- | :-- | :-- |
| 

file

 | 

[fs.File](../../../../../application-framework/core-file-kit/arkts-apis/ohos-file-fs-file-management/document.md#file)

 | 

No

 | 

No

 | 

File object.

 |

#### P2pAppParam

Device-side app parameter class that can be used during P2P communication.

**Model restriction**: This API can be used only in the stage model.

**System capability**: SystemCapability.Health.WearEngine

**Start version**: 5.0.0(12)

| 
Name

 | 

Type

 | 

Read-only

 | 

Optional

 | 

Description

 |
| :-- | :-- | :-- | :-- | :-- |
| 

remoteApp

 | 

[AppInfo](#section1357110221710)

 | 

No

 | 

No

 | 

Device-side app information class.

 |
| 

transformLocalAppInfo

 | 

boolean

 | 

No

 | 

Yes

 | 

Indicates whether to convert the local bundle name and fingerprint to match those stored on the cloud for compatible apps. Default value: **false**.

**true**: yes; **false**: no.

For details about how to set an app to a compatible one, please refer to [Applying for Integrating Wear Engine](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/wearengine_apply).

 |

#### wearEngine.getNotifyClient

getNotifyClient(context: common.Context): NotifyClient

Obtains the client of the Notify module.

**Model restriction**: This API can be used only in the stage model.

**System capability**: SystemCapability.Health.WearEngine

**Device behavior differences**: This API is supported on phones and tablets. On other devices, it returns error code 801.

**Start version**: 5.0.0(12)

**Parameters:**

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

[common.Context](../../../../../application-framework/ability-kit/arkts-apis/dependent-elements-and-definitions/application/context-context-base-class-of-the-stage-model/document.md#context)

 | 

Yes

 | 

Context. Only the context that contains the **connectServiceExtensionAbility** method is supported (example: [UIAbilityContext](../../../../../application-framework/ability-kit/arkts-apis/dependent-elements-and-definitions/application/uiabilitycontext/document.md#uiabilitycontext-1)).

 |

**Returns**:

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

[NotifyClient](#section82221754103913)

 | 

Template-based notification client, which stores the methods for sending template-based notifications.

 |

**Error codes**:

For details about the error codes, please refer to [Wear Engine ArkTS API Error Codes](../../arkts-api-error-codes/document.md).

| 
Error Code

 | 

Error Message

 |
| :-- | :-- |
| 

[401](../../arkts-api-error-codes/document.md#section201741341307)

 | 

Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types.

 |
| 

[801](../../arkts-api-error-codes/document.md#section5941173162512)

 | 

Capability not supported.

 |
| 

[1008509999](../../arkts-api-error-codes/document.md#section93011432734)

 | 

Internal error.

 |

**Example:**

import { wearEngine } from '@kit.WearEngine';

let notifyClient: wearEngine.NotifyClient = wearEngine.getNotifyClient(this.getUIContext().getHostContext());
console.info(\`Succeeded in getting notify client\`);

#### NotifyClient

Notify client class, which is returned by [wearEngine.getNotifyClient](#section552416431386).

**Model restriction**: This API can be used only in the stage model.

**System capability**: SystemCapability.Health.WearEngine

**Start version**: 5.0.0(12)

#### \[h2\]notify

notify(deviceRandomId: string, options: NotificationOptions): Promise<void>

Sends a template-based notification to a wearable device, and returns the sending result. This API returns the result asynchronously through a promise.

**System capability**: SystemCapability.Health.WearEngine

**Device behavior differences**: This API is supported on phones and tablets. On other devices, it returns error code 801.

**Model restriction**: This API can be used only in the stage model.

**Start version**: 5.0.0(12)

**Parameters:**

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

deviceRandomId

 | 

string

 | 

Yes

 | 

Random identifier of a [Device](#section385118379447), which specifies the device to be queried.

 |
| 

options

 | 

[NotificationOptions](#section0751457344)

 | 

Yes

 | 

Parameter class for the configuration of template-based notifications.

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

Promise object. Promise that returns no value.

 |

**Error codes**:

For details about the error codes, please refer to [Wear Engine ArkTS API Error Codes](../../arkts-api-error-codes/document.md).

| 
Error Code

 | 

Error Message

 |
| :-- | :-- |
| 

[401](../../arkts-api-error-codes/document.md#section201741341307)

 | 

Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed.

 |
| 

[1008500001](../../arkts-api-error-codes/document.md#section1047474644710)

 | 

Network error. The network is unavailable.

 |
| 

[1008500002](../../arkts-api-error-codes/document.md#section18859424615)

 | 

No device is bound.

 |
| 

[1008500003](../../arkts-api-error-codes/document.md#section11616131326)

 | 

Device disconnected.

 |
| 

[1008500004](../../arkts-api-error-codes/document.md#section485113712218)

 | 

App has not applied for the Wear Engine service.

 |
| 

[1008500005](../../arkts-api-error-codes/document.md#section665613120197)

 | 

The HUAWEI ID is not authorized.

 |
| 

[1008500006](../../arkts-api-error-codes/document.md#section1461311549277)

 | 

User privacy is not agreed.

 |
| 

[1008500007](../../arkts-api-error-codes/document.md#section15917165718219)

 | 

The device capability is not supported.

 |
| 

[1008500008](../../arkts-api-error-codes/document.md#section612518413314)

 | 

Account error. The user has not logged in with HUAWEI ID.

 |
| 

[1008500009](../../arkts-api-error-codes/document.md#section94850224314)

 | 

Account error. Failed to obtain account information with HUAWEI ID.

 |
| 

[1008500010](../../arkts-api-error-codes/document.md#section411611281734)

 | 

Device ID is invalid.

 |
| 

[1008509999](../../arkts-api-error-codes/document.md#section93011432734)

 | 

Internal error.

 |

**Example:**

import { wearEngine } from '@kit.WearEngine';
import { BusinessError } from '@kit.BasicServicesKit';

let notifyClient: wearEngine.NotifyClient = wearEngine.getNotifyClient(this.getUIContext().getHostContext());
let deviceClient: wearEngine.DeviceClient = wearEngine.getDeviceClient(this.getUIContext().getHostContext());
let devices: wearEngine.Device\[\] = await deviceClient.getConnectedDevices();

if (devices.length > 0) {
  // Select the target device from the obtained device list and define it as **device**. (Assume that there are connected devices in the array and the first one is the target device.)
  let device: wearEngine.Device = devices\[0\];

  let button1: wearEngine.NotificationButton = {
    buttonId: wearEngine.ButtonId.FIRST\_BUTTON,
    content: 'button\_1'
  }
  let type1Notification: wearEngine.Notification = {
    type: wearEngine.NotificationType.NOTIFICATION\_WITH\_ONE\_BUTTON,
    bundleName: 'bundleName',
    title: 'title',
    text: 'text',
    buttons: \[button1\]
  }
  let options: wearEngine.NotificationOptions = {
    notification: type1Notification,
    onAction: (feedback: wearEngine.NotificationFeedback) => {
      console.info(\`one button notify get feedback is ${feedback.action ? feedback.action : feedback.errorCode}\`);
    }
  }

  notifyClient.notify(device.randomId, options).then(result => {
    console.info(\`Succeeded in sending notification.\`);
  }).catch((error: BusinessError) => {
    console.error(\`Failed to send notification. Code is ${error.code}, message is ${error.message}\`);
  })
}

#### NotificationOptions

Parameter class for the configuration of template-based notifications.

**Model restriction**: This API can be used only in the stage model.

**System capability**: SystemCapability.Health.WearEngine

**Start version**: 5.0.0(12)

#### \[h2\]Parameters

| 
Name

 | 

Type

 | 

Read-only

 | 

Optional

 | 

Description

 |
| :-- | :-- | :-- | :-- | :-- |
| 

notification

 | 

[Notification](#section33797461644)

 | 

No

 | 

No

 | 

Parameter class for template-based notifications.

 |

#### \[h2\]onAction

onAction(feedback: NotificationFeedback): void

Callback function executed after an action is performed on the notification received on the device.

**Model restriction**: This API can be used only in the stage model.

**System capability**: SystemCapability.Health.WearEngine

**Device behavior differences**: This API is supported on phones and tablets. On other devices, it returns error code 801.

**Start version**: 5.0.0(12)

**Parameters:**

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

feedback

 | 

[NotificationFeedback](#section498821414418)

 | 

Yes

 | 

Feedback class for the action performed on the notification received on the device.

 |

#### Notification

Parameter class for template-based notifications.

**Model restriction**: This API can be used only in the stage model.

**System capability**: SystemCapability.Health.WearEngine

**Start version**: 5.0.0(12)

| 
Name

 | 

Type

 | 

Read-only

 | 

Optional

 | 

Description

 |
| :-- | :-- | :-- | :-- | :-- |
| 

type

 | 

[NotificationType](#section45813154136)

 | 

No

 | 

No

 | 

Notification template type.

 |
| 

bundleName

 | 

string

 | 

No

 | 

No

 | 

Bundle name of the app that sends the notification.

 |
| 

title

 | 

string

 | 

No

 | 

No

 | 

Notification title. Value range (in bytes): \[1, 28).

 |
| 

text

 | 

string

 | 

No

 | 

No

 | 

Notification content. Value range (in bytes): \[1, 400).

 |
| 

buttons

 | 

[NotificationButton](#section7336124218819)\[\]

 | 

No

 | 

Yes

 | 

Notification button information class. The value is left empty by default.

 |

#### NotificationType

Template type enum class for template-based notifications.

**Model restriction**: This API can be used only in the stage model.

**System capability**: SystemCapability.Health.WearEngine

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

NOTIFICATION\_WITHOUT\_BUTTONS

 | 

50

 | 

Notification without a button.

 |
| 

NOTIFICATION\_WITH\_ONE\_BUTTON

 | 

51

 | 

Notification with a button.

 |
| 

NOTIFICATION\_WITH\_TWO\_BUTTONS

 | 

52

 | 

Notification with two buttons.

 |
| 

NOTIFICATION\_WITH\_THREE\_BUTTONS

 | 

53

 | 

Notification with three buttons.

 |

#### NotificationButton

Notification button information class.

**Model restriction**: This API can be used only in the stage model.

**System capability**: SystemCapability.Health.WearEngine

**Start version**: 5.0.0(12)

| 
Name

 | 

Type

 | 

Read-only

 | 

Optional

 | 

Description

 |
| :-- | :-- | :-- | :-- | :-- |
| 

buttonId

 | 

[ButtonId](#section171882571499)

 | 

No

 | 

No

 | 

Button ID enum.

 |
| 

content

 | 

string

 | 

No

 | 

No

 | 

Text on a button. Value range (in bytes): \[1, 12).

 |

#### ButtonId

Button ID enum class for template-based notifications.

**Model restriction**: This API can be used only in the stage model.

**System capability**: SystemCapability.Health.WearEngine

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

FIRST\_BUTTON

 | 

firstButton

 | 

ID of the first button.

 |
| 

SECOND\_BUTTON

 | 

secondButton

 | 

ID of the second button.

 |
| 

THIRD\_BUTTON

 | 

thirdButton

 | 

ID of the third button.

 |

#### NotificationFeedback

Feedback class for the action performed on the notification received on the device.

**Model restriction**: This API can be used only in the stage model.

**System capability**: SystemCapability.Health.WearEngine

**Start version**: 5.0.0(12)

| 
Name

 | 

Type

 | 

Read-only

 | 

Optional

 | 

Description

 |
| :-- | :-- | :-- | :-- | :-- |
| 

action

 | 

[NotificationAction](#section924615208466)

 | 

No

 | 

Yes

 | 

Feedback enum class for the action performed on the notification received on the device.

 |
| 

errorCode

 | 

number

 | 

No

 | 

Yes

 | 

Error code. For details, please refer to [NotificationErrorCode](#section9782193965320).

 |

#### NotificationAction

Feedback enum class for the action performed on the notification received on the device.

**Model restriction**: This API can be used only in the stage model.

**System capability**: SystemCapability.Health.WearEngine

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

NOTIFICATION\_SWITCHED\_TO\_BACKGROUND

 | 

0

 | 

The user presses the Home button to exit or turn off the screen, and the notification switches to the background.

 |
| 

NOTIFICATION\_DELETED

 | 

1

 | 

The notification is deleted by the user.

 |
| 

FIRST\_BUTTON\_CLICKED

 | 

2

 | 

The user taps the first button in the notification.

 |
| 

SECOND\_BUTTON\_CLICKED

 | 

3

 | 

The user taps the second button in the notification.

 |
| 

THIRD\_BUTTON\_CLICKED

 | 

4

 | 

The user taps the third button in the notification.

 |

#### NotificationErrorCode

Error enum class for device-side notifications.

**Model restriction**: This API can be used only in the stage model.

**System capability**: SystemCapability.Health.WearEngine

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

INTERNAL\_ERROR

 | 

255

 | 

An internal error occurs in Wear Engine. [Submit a ticket online](https://developer.huawei.com/consumer/en/support/feedback/#/). Huawei technical support will get back to you as soon as possible.

 |

#### wearEngine.getSensorClient

getSensorClient(context: common.Context): SensorClient

Obtains the client of the Sensor module.

**Model restriction**: This API can be used only in the stage model.

**System capability**: SystemCapability.Health.WearEngine

**Device behavior differences**: This API is supported on phones and tablets. On other devices, it returns error code 801.

**Start version**: 5.0.0(12)

**Parameters:**

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

[common.Context](../../../../../application-framework/ability-kit/arkts-apis/dependent-elements-and-definitions/application/context-context-base-class-of-the-stage-model/document.md#context)

 | 

Yes

 | 

Context. Only the context that contains the **connectServiceExtensionAbility** method is supported (example: [UIAbilityContext](../../../../../application-framework/ability-kit/arkts-apis/dependent-elements-and-definitions/application/uiabilitycontext/document.md#uiabilitycontext-1)).

 |

**Returns**:

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

[SensorClient](#section1743102372015)

 | 

Sensor client, which stores methods related to the Sensor module.

 |

**Error codes**:

For details about the error codes, please refer to [Wear Engine ArkTS API Error Codes](../../arkts-api-error-codes/document.md).

| 
Error Code

 | 

Error Message

 |
| :-- | :-- |
| 

[401](../../arkts-api-error-codes/document.md#section201741341307)

 | 

Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types.

 |
| 

[801](../../arkts-api-error-codes/document.md#section5941173162512)

 | 

Capability not supported.

 |
| 

[1008509999](../../arkts-api-error-codes/document.md#section93011432734)

 | 

Internal error.

 |

**Example:**

import { wearEngine } from '@kit.WearEngine';

let sensorClient: wearEngine.SensorClient = wearEngine.getSensorClient(this.getUIContext().getHostContext());
console.info(\`Succeeded in getting sensor client\`);

#### SensorClient

Sensor client class, which is returned by [wearEngine.getSensorClient](#section1529943512113).

**Model restriction**: This API can be used only in the stage model.

**System capability**: SystemCapability.Health.WearEngine

**Start version**: 5.0.0(12)

#### \[h2\]getSensorList

getSensorList(deviceRandomId: string): Promise<Sensor\[\]>

Obtains the list of available sensors on the device. This API returns the result asynchronously through a promise.

**System capability**: SystemCapability.Health.WearEngine

**Device behavior differences**: This API is supported on phones and tablets. On other devices, it returns error code 801.

**Model restriction**: This API can be used only in the stage model.

**Start version**: 5.0.0(12)

**Parameters:**

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

deviceRandomId

 | 

string

 | 

Yes

 | 

Random identifier of a [Device](#section385118379447), which specifies the device.

 |

**Returns**:

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

Promise<[Sensor](#section19142203612579)\[\]>

 | 

Promise object used to return the list of available sensors on the device.

 |

**Error codes**:

For details about the error codes, please refer to [Wear Engine ArkTS API Error Codes](../../arkts-api-error-codes/document.md).

| 
Error Code

 | 

Error Message

 |
| :-- | :-- |
| 

[401](../../arkts-api-error-codes/document.md#section201741341307)

 | 

Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed.

 |
| 

[1008500001](../../arkts-api-error-codes/document.md#section1047474644710)

 | 

Network error. The network is unavailable.

 |
| 

[1008500002](../../arkts-api-error-codes/document.md#section18859424615)

 | 

No device is bound.

 |
| 

[1008500003](../../arkts-api-error-codes/document.md#section11616131326)

 | 

Device disconnected.

 |
| 

[1008500004](../../arkts-api-error-codes/document.md#section485113712218)

 | 

App has not applied for the Wear Engine service.

 |
| 

[1008500005](../../arkts-api-error-codes/document.md#section665613120197)

 | 

The HUAWEI ID is not authorized.

 |
| 

[1008500006](../../arkts-api-error-codes/document.md#section1461311549277)

 | 

User privacy is not agreed.

 |
| 

[1008500007](../../arkts-api-error-codes/document.md#section15917165718219)

 | 

The device capability is not supported.

 |
| 

[1008500008](../../arkts-api-error-codes/document.md#section612518413314)

 | 

Account error. The user has not logged in with HUAWEI ID.

 |
| 

[1008500009](../../arkts-api-error-codes/document.md#section94850224314)

 | 

Account error. Failed to obtain account information with HUAWEI ID.

 |
| 

[1008500010](../../arkts-api-error-codes/document.md#section411611281734)

 | 

Device ID is invalid.

 |
| 

[1008509999](../../arkts-api-error-codes/document.md#section93011432734)

 | 

Internal error.

 |

**Example:**

import { wearEngine } from '@kit.WearEngine';
import { BusinessError } from '@kit.BasicServicesKit';

let sensorClient: wearEngine.SensorClient = wearEngine.getSensorClient(this.getUIContext().getHostContext());
let deviceClient: wearEngine.DeviceClient = wearEngine.getDeviceClient(this.getUIContext().getHostContext());
let devices: wearEngine.Device\[\] = await deviceClient.getConnectedDevices();

if (devices.length > 0) {
  // Select the target device from the obtained device list and define it as **device**. (Assume that there are connected devices in the array and the first one is the target device.)
  let device: wearEngine.Device = devices\[0\];

  sensorClient.getSensorList(device.randomId).then((sensorList) => {
    console.info(\`Succeeded in getting sensor list, result is ${sensorList}\`);
  }).catch((error: BusinessError) => {
    console.error(\`Failed to get sensor list. Code is ${error.code}, message is ${error.message}\`);
  })
}

#### \[h2\]subscribeSensor

subscribeSensor(deviceRandomId: string, type: SensorType, callback: Callback<SensorResult>): Promise<void>

Subscribes to data reported by a specified sensor and returns a message indicating whether the subscription is successful. This API returns the result asynchronously through a promise.

**System capability**: SystemCapability.Health.WearEngine

**Device behavior differences**: This API is supported on phones and tablets. On other devices, it returns error code 801.

**Model restriction**: This API can be used only in the stage model.

**Start version**: 5.0.0(12)

**Parameters:**

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

deviceRandomId

 | 

string

 | 

Yes

 | 

Random identifier of a [Device](#section385118379447), which specifies the device involved in the subscription.

 |
| 

type

 | 

[SensorType](#section2420171225210)

 | 

Yes

 | 

Sensor type, which specifies the sensor to be subscribed to.

 |
| 

callback

 | 

Callback<[SensorResult](#section19118123861519)\>

 | 

Yes

 | 

Callback function used to process data reported by the sensor.

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

Promise object. Promise that returns no value.

 |

**Error codes**:

For details about the error codes, please refer to [Wear Engine ArkTS API Error Codes](../../arkts-api-error-codes/document.md).

| 
Error Code

 | 

Error Message

 |
| :-- | :-- |
| 

[401](../../arkts-api-error-codes/document.md#section201741341307)

 | 

Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed.

 |
| 

[1008500001](../../arkts-api-error-codes/document.md#section1047474644710)

 | 

Network error. The network is unavailable.

 |
| 

[1008500002](../../arkts-api-error-codes/document.md#section18859424615)

 | 

No device is bound.

 |
| 

[1008500003](../../arkts-api-error-codes/document.md#section11616131326)

 | 

Device disconnected.

 |
| 

[1008500004](../../arkts-api-error-codes/document.md#section485113712218)

 | 

App has not applied for the Wear Engine service.

 |
| 

[1008500005](../../arkts-api-error-codes/document.md#section665613120197)

 | 

The HUAWEI ID is not authorized.

 |
| 

[1008500006](../../arkts-api-error-codes/document.md#section1461311549277)

 | 

User privacy is not agreed.

 |
| 

[1008500007](../../arkts-api-error-codes/document.md#section15917165718219)

 | 

The device capability is not supported.

 |
| 

[1008500008](../../arkts-api-error-codes/document.md#section612518413314)

 | 

Account error. The user has not logged in with HUAWEI ID.

 |
| 

[1008500009](../../arkts-api-error-codes/document.md#section94850224314)

 | 

Account error. Failed to obtain account information with HUAWEI ID.

 |
| 

[1008500010](../../arkts-api-error-codes/document.md#section411611281734)

 | 

Device ID is invalid.

 |
| 

[1008500012](../../arkts-api-error-codes/document.md#section1599615141614)

 | 

Too many callbacks of the same type.

 |
| 

[1008509999](../../arkts-api-error-codes/document.md#section93011432734)

 | 

Internal error.

 |

**Example:**

import { wearEngine } from '@kit.WearEngine';
import { BusinessError } from '@kit.BasicServicesKit';

let sensorClient: wearEngine.SensorClient = wearEngine.getSensorClient(this.getUIContext().getHostContext());
let deviceClient: wearEngine.DeviceClient = wearEngine.getDeviceClient(this.getUIContext().getHostContext());
let devices: wearEngine.Device\[\] = await deviceClient.getConnectedDevices();

if (devices.length > 0) {
  // Select the target device from the obtained device list and define it as **device**. (Assume that there are connected devices in the array and the first one has the capability required.)
  let device: wearEngine.Device = devices\[0\];
  let sensorList: wearEngine.Sensor\[\] = await sensorClient.getSensorList(device.randomId);
  sensorList.forEach((sensor, idx, arr) => {
    if (sensor.type === wearEngine.SensorType.ACCELEROMETER) {
      let callback = (sensorResult: wearEngine.SensorResult) => {
        console.info(\`Succeeded in getting sensor result, result is ${sensorResult}\`);
      }
      // Subscribe to data reported by the acceleration sensor.
      sensorClient.subscribeSensor(device.randomId, wearEngine.SensorType.ACCELEROMETER, callback).then(() => {
        console.info(\`Succeeded in subscribing sensor data.\`);
      }).catch((error: BusinessError) => {
        console.error(\`Failed to subscribe sensor data. Code is ${error.code}, message is ${error.message}\`);
      })
    }
  })
}

#### \[h2\]unsubscribeSensor

unsubscribeSensor(deviceRandomId: string, type: SensorType, callback: Callback<SensorResult>): Promise<void>

Unsubscribes from data reported by a specified sensor and returns a message indicating whether the unsubscription is successful. This API returns the result asynchronously through a promise.

**System capability**: SystemCapability.Health.WearEngine

**Device behavior differences**: This API is supported on phones and tablets. On other devices, it returns error code 801.

**Model restriction**: This API can be used only in the stage model.

**Start version**: 5.0.0(12)

**Parameters:**

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

deviceRandomId

 | 

string

 | 

Yes

 | 

Random identifier of a [Device](#section385118379447), which specifies the device involved in the unsubscription.

 |
| 

type

 | 

[SensorType](#section2420171225210)

 | 

Yes

 | 

Sensor type, which specifies the sensor to be unsubscribed from.

 |
| 

callback

 | 

Callback<[SensorResult](#section19118123861519)\>

 | 

Yes

 | 

Callback function, which is used to process data reported by the sensor. The callback function must be the same as the one used for subscription.

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

Promise object. Promise that returns no value.

 |

**Error codes**:

For details about the error codes, please refer to [Wear Engine ArkTS API Error Codes](../../arkts-api-error-codes/document.md).

| 
Error Code

 | 

Error Message

 |
| :-- | :-- |
| 

[401](../../arkts-api-error-codes/document.md#section201741341307)

 | 

Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed.

 |
| 

[1008500001](../../arkts-api-error-codes/document.md#section1047474644710)

 | 

Network error. The network is unavailable.

 |
| 

[1008500002](../../arkts-api-error-codes/document.md#section18859424615)

 | 

No device is bound.

 |
| 

[1008500003](../../arkts-api-error-codes/document.md#section11616131326)

 | 

Device disconnected.

 |
| 

[1008500004](../../arkts-api-error-codes/document.md#section485113712218)

 | 

App has not applied for the Wear Engine service.

 |
| 

[1008500005](../../arkts-api-error-codes/document.md#section665613120197)

 | 

The HUAWEI ID is not authorized.

 |
| 

[1008500006](../../arkts-api-error-codes/document.md#section1461311549277)

 | 

User privacy is not agreed.

 |
| 

[1008500007](../../arkts-api-error-codes/document.md#section15917165718219)

 | 

The device capability is not supported.

 |
| 

[1008500008](../../arkts-api-error-codes/document.md#section612518413314)

 | 

Account error. The user has not logged in with HUAWEI ID.

 |
| 

[1008500009](../../arkts-api-error-codes/document.md#section94850224314)

 | 

Account error. Failed to obtain account information with HUAWEI ID.

 |
| 

[1008500010](../../arkts-api-error-codes/document.md#section411611281734)

 | 

Device ID is invalid.

 |
| 

[1008509999](../../arkts-api-error-codes/document.md#section93011432734)

 | 

Internal error.

 |

**Example:**

import { wearEngine } from '@kit.WearEngine';
import { BusinessError } from '@kit.BasicServicesKit';

let sensorClient: wearEngine.SensorClient = wearEngine.getSensorClient(this.getUIContext().getHostContext());
let deviceClient: wearEngine.DeviceClient = wearEngine.getDeviceClient(this.getUIContext().getHostContext());
let devices: wearEngine.Device\[\] = await deviceClient.getConnectedDevices();

if (devices.length > 0) {
  // Select the target device from the obtained device list and define it as **device**. (Assume that there are connected devices in the array and the first one has the capability required.)
  let device: wearEngine.Device = devices\[0\];
  let sensorList: wearEngine.Sensor\[\] = await sensorClient.getSensorList(device.randomId);
  sensorList.forEach((sensor, idx, arr) => {
    if (sensor.type === wearEngine.SensorType.ACCELEROMETER) {
      let callback = (sensorResult: wearEngine.SensorResult) => {
        console.info(\`Succeeded in getting sensor result, result is ${sensorResult}\`);
      }
      // Subscribe to data reported by the acceleration sensor.
      sensorClient.subscribeSensor(device.randomId, wearEngine.SensorType.ACCELEROMETER, callback).then(() => {
        console.info(\`Succeeded in subscribing sensor data.\`);
      }).catch((error: BusinessError) => {
        console.error(\`Failed to subscribe sensor data. Code is ${error.code}, message is ${error.message}\`);
      })
      // Cancel the data reporting from the acceleration sensor. Note that the callback function must be the same as the one used for subscription.
      sensorClient.unsubscribeSensor(device.randomId, wearEngine.SensorType.ACCELEROMETER, callback).then(() => {
        console.info(\`Succeeded in unsubscribing sensor data.\`);
      }).catch((error: BusinessError) => {
        console.error(\`Failed to unsubscribe sensor data. Code is ${error.code}, message is ${error.message}\`);
      })
    }
  })
}

#### SensorType

Sensor type.

**Model restriction**: This API can be used only in the stage model.

**System capability**: SystemCapability.Health.WearEngine

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

ELECTROCARDIOGRAPHY

 | 

0

 | 

Electrocardiograph (ECG) sensor.

 |
| 

PHOTOPLETHYSMOGRAPHY

 | 

1

 | 

Photoplethysmogram (PPG) sensor.

 |
| 

ACCELEROMETER

 | 

2

 | 

Acceleration sensor.

 |
| 

GYROSCOPE

 | 

3

 | 

Gyroscope sensor.

 |
| 

MAGNETIC\_FIELD

 | 

4

 | 

Magnetometer sensor.

 |
| 

HEART\_RATE

 | 

6

 | 

Heart rate sensor.

 |

#### Sensor

Sensor information class.

**Model restriction**: This API can be used only in the stage model.

**System capability**: SystemCapability.Health.WearEngine

**Start version**: 5.0.0(12)

| 
Name

 | 

Type

 | 

Read-only

 | 

Optional

 | 

Description

 |
| :-- | :-- | :-- | :-- | :-- |
| 

name

 | 

string

 | 

No

 | 

No

 | 

Sensor name.

 |
| 

id

 | 

number

 | 

No

 | 

No

 | 

Sensor ID.

 |
| 

type

 | 

[SensorType](#section2420171225210)

 | 

No

 | 

No

 | 

Sensor type.

 |
| 

accuracy

 | 

number

 | 

No

 | 

Yes

 | 

Sensor sampling interval, in milliseconds.

 |
| 

resolution

 | 

number

 | 

No

 | 

Yes

 | 

Sensor resolution. Currently, this parameter is used only as the return value of the **Sensor** object.

 |
| 

isUtcTimestampSupported

 | 

boolean

 | 

No

 | 

No

 | 

Indicates whether the sensor supports the Coordinated Universal Time (UTC) timestamp. **true**: supported; **false**: not supported

 |

#### SensorData

Sensor data class.

**Model restriction**: This API can be used only in the stage model.

**System capability**: SystemCapability.Health.WearEngine

**Start version**: 5.0.0(12)

| 
Name

 | 

Type

 | 

Read-only

 | 

Optional

 | 

Description

 |
| :-- | :-- | :-- | :-- | :-- |
| 

sensorType

 | 

[SensorType](#section2420171225210)

 | 

No

 | 

No

 | 

Sensor type.

 |
| 

data

 | 

number\[\]

 | 

No

 | 

No

 | 

Data content. For details about the format and description, refer to [Sensor Data Format and Sample of Wearable Devices](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/device_sensor#en-us_topic_0000001073426751_section18811142832216).

 |
| 

channel

 | 

number

 | 

No

 | 

Yes

 | 

Sensor channel ID, which is an integer greater than 0.

 |
| 

timestamp

 | 

number

 | 

No

 | 

Yes

 | 

Timestamp.

 |
| 

utcTimestamp

 | 

number

 | 

No

 | 

Yes

 | 

UTC timestamp.

 |

#### SensorErrorCode

Sensor type.

**Model restriction**: This API can be used only in the stage model.

**System capability**: SystemCapability.Health.WearEngine

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

DEVICE\_NOT\_BEING\_WORN

 | 

300

 | 

The device is not worn.

 |
| 

DEVICE\_LEAD\_OFF

 | 

301

 | 

The device lead is disconnected.

 |
| 

SENSOR\_TURNED\_OFF\_MANUALLY

 | 

302

 | 

The sensor is manually disabled.

 |
| 

SENSOR\_OCCUPIED

 | 

303

 | 

The sensor is occupied.

 |
| 

SENSOR\_NOT\_SUPPORTED

 | 

304

 | 

The sensor is not supported.

 |

#### SensorResult

Sensor reporting result.

**Model restriction**: This API can be used only in the stage model.

**System capability**: SystemCapability.Health.WearEngine

**Start version**: 5.0.0(12)

| 
Name

 | 

Type

 | 

Read-only

 | 

Optional

 | 

Description

 |
| :-- | :-- | :-- | :-- | :-- |
| 

data

 | 

[SensorData](#section1896124869)\[\]

 | 

No

 | 

Yes

 | 

Data reported by the sensor.

 |
| 

errorCode

 | 

number

 | 

No

 | 

Yes

 | 

Error code. For details, please refer to [SensorErrorCode](#section173105551894).

 |

#### On/Off Subscription Event

#### \[h2\]wearEngine.on

on(type: 'serviceDie', callback: Callback<void>): void

Subscribes to the server destruction event. If you call [wearEngine.destroy](#section890395942912) to destroy the server, the callback function won't be triggered.

**Model restriction**: This API can be used only in the stage model.

**System capability**: SystemCapability.Health.WearEngine

**Start version**: 5.0.0(12)

**Parameters:**

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

Type of the event that you subscribe to. The value can only be **serviceDie** (server destruction event).

 |
| 

callback

 | 

Callback<void>

 | 

Yes

 | 

Callback function.

 |

**Error codes**:

For details about the error codes, please refer to [Wear Engine ArkTS API Error Codes](../../arkts-api-error-codes/document.md).

| 
Error Code

 | 

Error Message

 |
| :-- | :-- |
| 

[401](../../arkts-api-error-codes/document.md#section201741341307)

 | 

Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types.

 |
| 

[1008500012](../../arkts-api-error-codes/document.md#section1599615141614)

 | 

Too many callbacks of the same type.

 |
| 

[1008509999](../../arkts-api-error-codes/document.md#section93011432734)

 | 

Internal error.

 |

**Example:**

import { wearEngine } from '@kit.WearEngine';
import { BusinessError } from '@kit.BasicServicesKit';

let callback = () => {
  console.info(\`The service destruction event\`);
}
try {
  wearEngine.on('serviceDie', callback);
  console.info(\`Succeeded in subscribing the service destruction event.\`);
} catch (error) {
  const err: BusinessError = error as BusinessError;
  console.error(\`Failed to subscribe the service destruction event. Code is ${err.code}, message is ${err.message}.\`);
}

#### \[h2\]wearEngine.off

off(type: 'serviceDie', callback?: Callback<void>): void

Unsubscribes from the server destruction event.

**Model restriction**: This API can be used only in the stage model.

**System capability**: SystemCapability.Health.WearEngine

**Start version**: 5.0.0(12)

**Parameters:**

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

Type of the event that you subscribe to. The value can only be **serviceDie** (server destruction event).

 |
| 

callback

 | 

Callback<void>

 | 

No

 | 

Callback function, which must be the same as the callback function used for subscription.

If this parameter is left blank, all previous subscriptions will be canceled.

 |

**Error codes**:

For details about the error codes, please refer to [Wear Engine ArkTS API Error Codes](../../arkts-api-error-codes/document.md).

| 
Error Code

 | 

Error Message

 |
| :-- | :-- |
| 

[401](../../arkts-api-error-codes/document.md#section201741341307)

 | 

Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types.

 |
| 

[1008509999](../../arkts-api-error-codes/document.md#section93011432734)

 | 

Internal error.

 |

**Example:**

import { wearEngine } from '@kit.WearEngine';
import { BusinessError } from '@kit.BasicServicesKit';

let callback = () => {
  console.info(\`The service destruction event\`);
}
wearEngine.on('serviceDie', callback);

try {
  wearEngine.off('serviceDie', callback);
  console.info(\`Succeeded in unsubscribing the service destruction event.\`);
} catch (error) {
  const err: BusinessError = error as BusinessError;
  console.error(\`Failed to unsubscribe the service destruction event. Code is ${err.code}, message is ${err.message}.\`);
}

#### wearEngine.destroy

destroy(): Promise<void>

Proactively destroys the server. This API returns the result asynchronously through a promise.

**Model restriction**: This API can be used only in the stage model.

**System capability**: SystemCapability.Health.WearEngine

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

Promise object. Promise that returns no value.

 |

**Error codes**:

For details about the error codes, please refer to [Wear Engine ArkTS API Error Codes](../../arkts-api-error-codes/document.md).

| 
Error Code

 | 

Error Message

 |
| :-- | :-- |
| 

[1008509999](../../arkts-api-error-codes/document.md#section93011432734)

 | 

Internal error.

 |

**Example:**

import { wearEngine } from '@kit.WearEngine';
import { BusinessError } from '@kit.BasicServicesKit';

wearEngine.destroy().then(() => {
  console.info(\`Succeeded in destroying wear engine channel.\`);
}).catch((error: BusinessError) => {
  console.error(\`Failed to destroy wear engine channel. Code is ${error.code}, message is ${error.message}.\`);
})
