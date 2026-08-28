# CollaborationDevicePicker (Hopping Control)

This module provides the hopping entry component, and the device selection panel is displayed after the component is touched.

This module should be used together with devicePicker.[createDevicePickerController](../devicepicker-device-selection-controller/document.md#section25961963517) to enable users to interact with the device selection panel through the created controller.

**Start version**: 4.0.0(10)

#### Module Import

import { CollaborationDevicePicker } from '@kit.ServiceCollaborationKit'

#### CollaborationDevicePicker

**Decorator type**: @Component

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

controller

 | 

devicePicker.[DevicePickerController](../devicepicker-device-selection-controller/document.md#section132821135550)

 | 

No

 | 

No

 | 

Device selection controller, which is used to interact with the device selection screen.

 |
| 

attribute

 | 

devicePicker.[DevicePickerAttribute](../devicepicker-device-selection-controller/document.md#section13112135131715)

 | 

No

 | 

No

 | 

Attributes for device selection, which determine how an app is displayed on the device selection screen. If this parameter is not set, the information in the ability configuration file of the caller is used by default.

 |

#### \[h2\]build

build(): void

Default constructor of a struct. You cannot directly call this method.

**System capability**: SystemCapability.Collaboration.DevicePicker

**Start version**: 4.0.0(10)

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
