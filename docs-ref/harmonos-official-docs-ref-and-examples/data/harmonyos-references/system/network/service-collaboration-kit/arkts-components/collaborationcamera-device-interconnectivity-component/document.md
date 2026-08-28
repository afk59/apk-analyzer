# CollaborationCamera (Device Interconnectivity Component)

This module provides the [createCollaborationCameraMenuItems](#section1633482912443) and [CollaborationCameraStateDialog](#section158671330145417) components, which need to be used together to implement distributed cross-device capabilities. For example, a 2-in-1 device can call the camera of a phone.

The [createCollaborationCameraMenuItems](#section1633482912443) component is used to obtain a list of devices with required capabilities on the network. Users can then select a device to start the corresponding app. The [CollaborationCameraStateDialog](#section158671330145417) component is used to display a dialog box to show the status of the app on the remote device.

**Deprecation description**: This API is deprecated from API version 5.0.0(12). You are advised to use [CollaborationService](../collaborationservice-device-interconnectivity-component/document.md) instead.

**Start version**: 4.0.0(10)

#### Module Import

import { CollaborationCameraStateDialog, createCollaborationCameraMenuItems, CollaborationCameraBusinessFilter} from '@kit.ServiceCollaborationKit';

#### createCollaborationCameraMenuItems(deprecated)

createCollaborationCameraMenuItems(businessFilter?: Array<CollaborationCameraBusinessFilter>): void

Creates a selector that displays a list of devices with required capabilities on the network. It is called in the [Menu](../../../../../application-framework/arkui/arkts-components/menus/menu/document.md) component.

This method is a custom builder function. You need to learn about [@Builder](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/arkts-builder) before using this method.

**Deprecation description**: This API is deprecated from API version 5.0.0(12). You are advised to use [createCollaborationServiceMenuItems](../collaborationservice-device-interconnectivity-component/document.md#section1633482912443) instead.

**Decorator type**: @Builder

**System capability**: SystemCapability.Collaboration.Camera

**Device behavior differences**: This API can be called on PCs/2-in-1 devices and tablets. However, on other devices, the device list cannot be displayed, and the Device Interconnectivity capability cannot be used.

**Start version**: 4.0.0(10)

**Parameter**:

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

businessFilter

 | 

Array<[CollaborationCameraBusinessFilter](#section12639651397)\>

 | 

No

 | 

Capability type, which can be **ALL**, **TAKE\_PHOTO**, **SCAN\_DOCUMENT**, or **IMAGE\_PICKER**.

The default value is **ALL**, indicating all capabilities are supported.

 |

**Example**:

@Builder
MyTestMenu() {
  Menu() {
    createCollaborationCameraMenuItems(\[CollaborationCameraBusinessFilter.ALL\]) 
  }
}

#### CollaborationCameraBusinessFilter(deprecated)

Enumerated values of the capability type.

**Deprecation description**: This API is deprecated from API version 5.0.0(12). You are advised to use [CollaborationServiceFilter](../collaborationservice-device-interconnectivity-component/document.md#section12639651397) instead.

**System capability**: SystemCapability.Collaboration.Camera

**Device behavior differences**: This API can be called on PCs/2-in-1 devices and tablets. However, on other devices, the device list cannot be displayed, and the Device Interconnectivity capability cannot be used.

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

ALL

 | 

0

 | 

Matches all services.

 |
| 

TAKE\_PHOTO

 | 

1

 | 

Matches cross-device photographing.

 |
| 

SCAN\_DOCUMENT

 | 

2

 | 

Matches document scanning.

**Start version**: 4.1.0(11)

 |
| 

IMAGE\_PICKER

 | 

3

 | 

Matches the image selector.

**Start version**: 4.1.0(11)

 |

**Example**:

@Builder
MyTestMenu() {
  Menu() {
    createCollaborationCameraMenuItems(\[CollaborationCameraBusinessFilter.ALL\]) 
  }
}

#### CollaborationCameraStateDialog(deprecated)

Displays a dialog box to show the status of the matched app on the remote device.

You need to implement the [onState](#section33027582114) method and define this dialog box component on the page. The collaboration framework calls this method to complete the services.

This component is a custom component. You need to learn about [@Component](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/arkts-create-custom-components#component) before using it.

**Deprecation description**: This API is deprecated from API version 5.0.0(12). You are advised to use [CollaborationServiceStateDialog](../collaborationservice-device-interconnectivity-component/document.md#section158671330145417) instead.

**Decorator type**: @Component

**System capability**: SystemCapability.Collaboration.Camera

**Device behavior differences**: This API can be called on PCs/2-in-1 devices and tablets. However, on other devices, the device list cannot be displayed, and the Device Interconnectivity capability cannot be used.

**Start version**: 4.0.0(10)

#### \[h2\]onState(deprecated)

onState: (stateCode: number, buffer: ArrayBuffer) => void

Callback function used to receive data. **stateCode** indicates the service completion status, and **buffer** indicates the returned image data. You need to implement the **onState** method based on the status and image data, as well as the service logic.

**Deprecation description**: This API is deprecated from API version 5.0.0(12). You are advised to use [onState](../collaborationservice-device-interconnectivity-component/document.md#section33027582114) instead.

**System capability**: SystemCapability.Collaboration.Camera

**Device behavior differences**: This API can be called on PCs/2-in-1 devices and tablets. However, on other devices, the device list cannot be displayed, and the Device Interconnectivity capability cannot be used.

**Start version**: 4.0.0(10)

**Parameters**

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

stateCode

 | 

number

 | 

Yes

 | 

Service completion status. For details, refer to the result code table below.

 |
| 

buffer

 | 

ArrayBuffer

 | 

Yes

 | 

If the operation is successful, the requested data is returned. Otherwise, **Null** is returned.

 |

**Result codes**:

For details about the result codes, please refer to [ArkTS API Result Codes](../arkts-api-result-codes/document.md).

| 
Result Code

 | 

Message

 |
| :-- | :-- |
| 

0

 | 

Successful.

 |
| 

1001202001

 | 

Canceled on the remote device.

 |
| 

1001202002

 | 

An internal error occurs in the collaboration framework.

 |
| 

1001202003

 | 

Canceled on the local device.

 |
| 

1001202004

 | 

The capability of Device Interconnectivity is started.

 |
| 

1001202005

 | 

All images have been sent back.

 |

#### \[h2\]build(deprecated)

build(): void

Default constructor of a struct. You cannot directly call this method.

**Deprecation description**: This API is deprecated from API version 5.0.0(12). You are advised to use [build](../collaborationservice-device-interconnectivity-component/document.md#section41032414617) instead.

**System capability**: SystemCapability.Collaboration.Camera

**Device behavior differences**: This API can be called by components on PCs/2-in-1 devices and tablets. However, on other devices, the device list cannot be displayed, and the Device Interconnectivity capability cannot be used.

**Start version**: 4.0.0(10)

**Example**:

Refer to the sample code below to call an app on the remote device.

For details about Device Interconnectivity, please refer to [Introduction to Device Intertconnectivity](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/servicecollaboration-service-overview).

import {
  createCollaborationCameraMenuItems,
  CollaborationCameraStateDialog,
  CollaborationCameraBusinessFilter
} from '@kit.ServiceCollaborationKit';
import { image } from '@kit.ImageKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

@Entry
@Component
struct Index {
  @State picture: PixelMap | undefined = undefined;

  @Builder
  MyTestMenu() {
    Menu() {
      createCollaborationCameraMenuItems(\[CollaborationCameraBusinessFilter.ALL\]);
    }
  }

  build() {
    Column({ space: 20 }) {
      CollaborationCameraStateDialog({
        onState: (stateCode: number, buffer: ArrayBuffer): void => this.doInsertPicture(stateCode, buffer)
      })
      Button ('Use remote device to insert images')
        .type(ButtonType.Normal)
        .borderRadius(10)
        .bindMenu(this.MyTestMenu)

      if (this.picture) {
        Image(this.picture)
          .borderStyle(BorderStyle.Dotted)
          .borderWidth(1)
          .objectFit(ImageFit.Contain)
          .height('80%')
          .onComplete((event) => {
            if (event != undefined) {
              hilog.info(0, "MEMOMOCK", "onComplete " + event.loadingStatus)
            }
          })
      }
    }
    .padding(20)
    .width('100%')
    .alignItems(HorizontalAlign.Center)
  }

  doInsertPicture(stateCode: number, buffer: ArrayBuffer): void {
    if (stateCode != 0) {
      return
    }
    let imageSource = image.createImageSource(buffer)
    imageSource.createPixelMap().then((pixelMap) => {
      this.picture = pixelMap;
    })
  }
}
