# devicePicker (Device Selection Controller)

This module provides a device selection controller and panel. No API is available to directly display the device selection panel. However, the panel is automatically displayed after [CollaborationDevicePicker (Hopping Control)](../collaborationdevicepicker-hopping-control/document.md) is touched. A user can interact with the device selection panel through the device selection controller. The device selection panel displays the app description and the list of discovered devices with the same HUAWEI ID signed in and Wi-Fi and Bluetooth enabled (currently, only trusted devices can be displayed in the device list) are displayed.

After a user chooses a device, an API of the device selection controller is called, and information about the selected device is returned. The app can process the distributed service based on the obtained device information. For example, the app can start **UIAbility** on the remote device using **startAbility**. After the **UIAbility** on the remote device is successfully started, the [updateState](#section1543619272133) API can be called to update the service status. The specified status is then displayed on the app screen.

**Start version**: 4.0.0(10)

#### Module Import

import { devicePicker } from '@kit.ServiceCollaborationKit'

#### DeviceEvent

type DeviceEvent = 'deviceSelected' | 'deviceUnselected' | 'selectedDeviceOffline'

Device event type, which can be device selection, cancellation of a device selection, or a selected device going offline.

**System capability**: SystemCapability.Collaboration.DevicePicker

**Start version**: 4.0.0(10)

| 
Event

 | 

Description

 |
| :-- | :-- |
| 

'deviceSelected'

 | 

Device selection.

This event is triggered when a user taps a device in idle state.

 |
| 

'deviceUnselected'

 | 

Cancellation of a device selection.

This event is triggered when a user taps a device in successful service state. When device A is in successful service state, the **deviceUnselected** event of device A will also be triggered if device B is tapped.

 |
| 

'selectedDeviceOffline'

 | 

A selected device going offline.

This event is triggered when a device in successful state goes offline.

 |

#### createDevicePickerController

createDevicePickerController(): DevicePickerController

Creates a device selection controller. Users can interact with the device selection panel through the APIs provided by the controller.

**System capability**: SystemCapability.Collaboration.DevicePicker

**Start version**: 4.0.0(10)

**Returns**:

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

[DevicePickerController](#section132821135550)

 | 

Returns the device selection controller instance. This API can be used together with [CollaborationDevicePicker (Hopping Control)](../collaborationdevicepicker-hopping-control/document.md).

 |

**Example**:

import { devicePicker, CollaborationDevicePicker } from '@kit.ServiceCollaborationKit'

@Entry
@Component
struct Index {
  controller: devicePicker.DevicePickerController = devicePicker.createDevicePickerController()

  build() {
    Column() {
      // Hopping control, which is the entry for app hopping
      CollaborationDevicePicker({
        controller: this.controller, attribute: {
          abilityName: 'Hopping test',
          abilityDesc: 'Hopping test control',
          abilityIcon: $r('sys.media.ohos\_app\_icon'),
          businessDesc: 'Hop to'
        }
      })
    }.width('100%').alignItems(HorizontalAlign.Center)
  }
}

#### DevicePickerController

Provides APIs for interacting with the device selection panel.

**System capability**: SystemCapability.Collaboration.DevicePicker

**Start version**: 4.0.0(10)

#### \[h2\]on('deviceSelected' | 'deviceUnselected' | 'selectedDeviceOffline')

on(event: DeviceEvent, callback: Callback<distributedDeviceManager.DeviceBasicInfo>): void

Registers callbacks for device-related events. Currently, the following events are supported: device selection, selection cancellation of a device, and go-offline of a selected device.

**System capability**: SystemCapability.Collaboration.DevicePicker

**Start version**: 4.0.0(10)

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

event

 | 

[DeviceEvent](#section43691981888)

 | 

Yes

 | 

Device-related event, which can be device selection, selection cancellation of a device, or go-offline of a selected device.

 |
| 

callback

 | 

Callback<[distributedDeviceManager.DeviceBasicInfo](../../../distributed-service-kit/arkts-apis/ohos-distributeddevicemanager-device-management/document.md#devicebasicinfo)\>

 | 

Yes

 | 

Callback that returns the information about the device on which the corresponding event occurs. The returned device information can be used in the callback to start the app ability component on the remote device.

 |

**Example**:

import { common, Want } from '@kit.AbilityKit'
import { CollaborationDevicePicker, devicePicker } from '@kit.ServiceCollaborationKit'
import { distributedDeviceManager } from '@kit.DistributedServiceKit'
import { hilog } from '@kit.PerformanceAnalysisKit'

@Entry
@Component
struct CustomControls {
  // Create a device selection controller.
  controller: devicePicker.DevicePickerController = devicePicker.createDevicePickerController()
  // Obtain the context of the ability.
  context: common.UIAbilityContext = this.getUIContext().getHostContext() as common.UIAbilityContext
  abilityId: number = 0

  aboutToAppear() {
    // Register the device selection event.
    this.controller.on('deviceSelected', (device: distributedDeviceManager.DeviceBasicInfo) => {
      let want: Want = {
        // Obtain the device ID through **device**.
        deviceId: device.networkId,
        // The values of **bundleName** and **abilityName** specified here are only examples. The **bundleName** and **abilityName** that actually exist on the remote device shall be passed to start the specified service.
        bundleName: 'com.example.myapplication',
        abilityName: 'ExtensionAbility'
      }
      this.getUIContext().getPromptAction().showToast({ message: 'device selected' })
      this.context.startAbility(want).then(() => {
        hilog.info(0x0000, 'testTag', '%{public}s', 'Succeeded in starting Ability')
        // Update the device status.
        this.controller.updateState(device.networkId, devicePicker.BusinessState.SUCCESSFUL)
      }).catch(() => {
        hilog.error(0x0000, 'testTag', '%{public}s', 'Failed to startAbility')
        // Update the device status and add the failure cause which will be displayed below the device name.
        this.controller.updateState(device.networkId, devicePicker.BusinessState.FAILED, 'the remote device is busy')
      })
    })

    // Register the device selection cancellation event.
    this.controller.on('deviceUnselected', (device: distributedDeviceManager.DeviceBasicInfo) => {
      this.getUIContext().getPromptAction().showToast({ message: 'device unselected' })
    })
  }

  build() {
    Column() {
      CollaborationDevicePicker({
        controller: this.controller, attribute: {
          abilityName: 'Hopping test',
          abilityDesc: 'Hopping test control',
          abilityIcon: $r('sys.media.ohos\_app\_icon'),
          businessDesc: 'Hop to'
        }
      })
    }.width('100%').alignItems(HorizontalAlign.Center);
  }
}

#### \[h2\]off('deviceSelected' | 'deviceUnselected' | 'selectedDeviceOffline')

off(event: DeviceEvent, callback?: Callback<distributedDeviceManager.DeviceBasicInfo>): void

Unregisters callbacks for device-related events. Currently, the following events are supported: device selection, selection cancellation of a device, and go-offline of a selected device.

**System capability**: SystemCapability.Collaboration.DevicePicker

**Start version**: 4.0.0(10)

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

event

 | 

[DeviceEvent](#section43691981888)

 | 

Yes

 | 

Device-related event, which can be device selection, selection cancellation of a device, or go-offline of a selected device.

 |
| 

callback

 | 

Callback<[distributedDeviceManager.DeviceBasicInfo](../../../distributed-service-kit/arkts-apis/ohos-distributeddevicemanager-device-management/document.md#devicebasicinfo)\>

 | 

No

 | 

Callback that returns the information about the device on which the specified event occurs. The **off** API corresponds to the [on('deviceSelected' | 'deviceUnselected' | 'selectedDeviceOffline')](#section1476010417818) API and can be called when the device events do not need to be listened to. For example, if the **on** API is called for event registration when the **aboutToAppear()** method is implemented, the **off** API can be called when the **aboutToDisappear()** method is implemented to cancel the registration.

 |

**Example**:

import { common } from '@kit.AbilityKit'
import { distributedDeviceManager } from '@kit.DistributedServiceKit'
import { CollaborationDevicePicker, devicePicker } from '@kit.ServiceCollaborationKit'

@Entry
@Component
struct CustomControls {
  // Create a device selection controller.
  controller: devicePicker.DevicePickerController = devicePicker.createDevicePickerController()
  // Obtain the context of the ability.
  context: common.UIAbilityContext = this.getUIContext().getHostContext() as common.UIAbilityContext

  aboutToDisappear() {
    // Unregister the device selection event.
    this.controller.off('deviceSelected', (device: distributedDeviceManager.DeviceBasicInfo) => {
      this.getUIContext().getPromptAction().showToast({ message: 'off device selected' })
    })

    // Unregister the device selection cancellation event.
    this.controller.off('deviceUnselected', (device: distributedDeviceManager.DeviceBasicInfo) => {
      this.getUIContext().getPromptAction().showToast({ message: 'device unselected' })
    })
  }

  build() {
    Column() {
      CollaborationDevicePicker({
        controller: this.controller, attribute: {
          abilityName: 'Hopping test',
          abilityDesc: 'Hopping test control',
          abilityIcon: $r('sys.media.ohos\_app\_icon'),
          businessDesc: 'Hop to'
        }
      })
    }.width('100%').alignItems(HorizontalAlign.Center)
  }
}

#### \[h2\]updateState

updateState(networkId: string, state: BusinessState, desc?: ResourceStr): void

Updates the service status of a device. The updated status will be displayed on the device selection panel. When a service fails, the failure description can be passed and displayed together with the status.

**System capability**: SystemCapability.Collaboration.DevicePicker

**Start version**: 4.0.0(10)

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

networkId

 | 

string

 | 

Yes

 | 

Network ID of a device.

 |
| 

state

 | 

[BusinessState](#section843420618418)

 | 

Yes

 | 

Service status, which can be **IDLE**, **SUCCESSFUL**, or **FAILED**.

 |
| 

desc

 | 

[ResourceStr](../../../../../application-framework/arkui/arkts-components/common-definitions/basic-types/document.md#resourcestr)

 | 

No

 | 

Description of a service failure. This parameter can be passed when a service fails and will be displayed under the specified device name. The value contains 1 to 128 characters.

 |

**Example**:

import { common, Want } from '@kit.AbilityKit'
import { CollaborationDevicePicker, devicePicker } from '@kit.ServiceCollaborationKit'
import { distributedDeviceManager } from '@kit.DistributedServiceKit'
import { hilog } from '@kit.PerformanceAnalysisKit'

@Entry
@Component
struct CustomControls {
  // Create a device selection controller.
  controller: devicePicker.DevicePickerController = devicePicker.createDevicePickerController()
  // Obtain the context of the ability.
  context: common.UIAbilityContext = this.getUIContext().getHostContext() as common.UIAbilityContext
  abilityId: number = 0

  aboutToAppear() {
    // Register the device selection event.
    this.controller.on('deviceSelected', (device: distributedDeviceManager.DeviceBasicInfo) => {
      let want: Want = {
        // Obtain the device ID through **device**.
        deviceId: device.networkId,
        // The values of **bundleName** and **abilityName** specified here are only examples. The **bundleName** and **abilityName** that actually exist on the remote device shall be passed to start the specified service.
        bundleName: 'com.example.myapplication',
        abilityName: 'ExtensionAbility'
      }
      this.getUIContext().getPromptAction().showToast({ message: 'device selected' })
      this.context.startAbility(want).then(() => {
        hilog.info(0x0000, 'testTag', '%{public}s', 'Succeeded in starting Ability')
        // Update the device status.
        this.controller.updateState(device.networkId, devicePicker.BusinessState.SUCCESSFUL)
      }).catch(() => {
        hilog.error(0x0000, 'testTag', '%{public}s', 'Failed to startAbility')
        // Update the device status and add the failure cause which will be displayed below the device name.
        this.controller.updateState(device.networkId, devicePicker.BusinessState.FAILED, 'the remote device is busy')
      })
    })

    // Register the device selection cancellation event.
    this.controller.on('deviceUnselected', (device: distributedDeviceManager.DeviceBasicInfo) => {
      this.getUIContext().getPromptAction().showToast({ message: 'device unselected' })
    })
  }

  build() {
    Column() {
      CollaborationDevicePicker({
        controller: this.controller, attribute: {
          abilityName: 'Hopping test',
          abilityDesc: 'Hopping test control',
          abilityIcon: $r('sys.media.ohos\_app\_icon'),
          businessDesc: 'Hop to'
        }
      })
    }.width('100%').alignItems(HorizontalAlign.Center);
  }
}

#### \[h2\]release

release(): void

Releases the device selection controller. It is opposite to the [createDevicePickerController](#section25961963517) method.

When an app does not need the device selection controller, **release()** can be called to release the controller. For example, a controller is created through [createDevicePickerController](#section25961963517) when the **onCreate()** method is implemented, and **release()** can be called when the **onDestroy()** method is implemented to release the controller.

**System capability**: SystemCapability.Collaboration.DevicePicker

**Start version**: 4.0.0(10)

**Example**:

import { hilog } from '@kit.PerformanceAnalysisKit'
import { UIAbility, AbilityConstant, Want } from '@kit.AbilityKit'
import { devicePicker } from '@kit.ServiceCollaborationKit'

export default class EntryAbility extends UIAbility {
  // Create a device selection controller.
  controller: devicePicker.DevicePickerController = devicePicker.createDevicePickerController()

  onCreate(want: Want, launchParam: AbilityConstant.LaunchParam) {
    hilog.info(0x0000, 'testTag', '%{public}s', 'Ability onCreate')
  }

  onDestroy() {
    hilog.info(0x0000, 'testTag', '%{public}s', 'Ability onDestroy')
    //  Release the device selection controller.
    this.controller.release()
  }
}

#### DevicePickerAttribute

Attribute class for the device selection controller. The configured information will be displayed in the app information part of the device selection panel. If no attribute is set, the tag information in the ability configuration file of the caller will be used. This class is used together with [CollaborationDevicePicker](../collaborationdevicepicker-hopping-control/document.md).

**System capability**: SystemCapability.Collaboration.DevicePicker

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

abilityIcon

 | 

[ResourceStr](../../../../../application-framework/arkui/arkts-components/common-definitions/basic-types/document.md#resourcestr)

 | 

No

 | 

Yes

 | 

Ability icon displayed to users in the app information part on the device selection panel. If this attribute is not set, **icon** in **module.json5** is used by default.

 |
| 

abilityName

 | 

[ResourceStr](../../../../../application-framework/arkui/arkts-components/common-definitions/basic-types/document.md#resourcestr)

 | 

No

 | 

Yes

 | 

Ability name displayed to users in the app information part on the device selection panel. If this attribute is not set, **label** in **module.json5** is used by default.

 |
| 

abilityDesc

 | 

[ResourceStr](../../../../../application-framework/arkui/arkts-components/common-definitions/basic-types/document.md#resourcestr)

 | 

No

 | 

Yes

 | 

Ability description, which is displayed in the app information part on the device selection panel. If this attribute is not set, **description** in **module.json5** is used by default.

 |
| 

businessDesc

 | 

[ResourceStr](../../../../../application-framework/arkui/arkts-components/common-definitions/basic-types/document.md#resourcestr)

 | 

No

 | 

Yes

 | 

Description of a distributed service, for example, **Hop to** for the hopping service, and **Cast to** for the screen casting service. If this attribute is not set, **Hop to** is displayed by default.

 |

#### BusinessState

Enumeration class of service status.

**System capability**: SystemCapability.Collaboration.DevicePicker

**Start version**: 4.0.0(10)

| 
Name

 | 

Value

 | 

Description

 |
| :-- | :-- | :-- |
| 

IDLE

 | 

0

 | 

Idle.

 |
| 

SUCCESSFUL

 | 

1

 | 

Successful.

 |
| 

FAILED

 | 

2

 | 

Failed.

 |
