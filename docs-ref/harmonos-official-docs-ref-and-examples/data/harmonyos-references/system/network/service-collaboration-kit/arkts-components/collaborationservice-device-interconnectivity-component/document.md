# CollaborationService (Device Interconnectivity Component)

This module provides the [createCollaborationServiceMenuItems](#section1633482912443) and [CollaborationServiceFilter](#section12639651397) components, which need to be used together to implement distributed cross-device capabilities. For example, a 2-in-1 device can call the camera of a phone.

The [createCollaborationServiceMenuItems](#section1633482912443) component is used to obtain a list of devices with required capabilities on the network. Users can then select a device to start the corresponding app. The [CollaborationServiceStateDialog](#section158671330145417) component is used to display a dialog box to show the status of the app on the remote device.

**Start version**: 5.0.0(12)

#### Module Import

import { CollaborationServiceStateDialog, createCollaborationServiceMenuItems, CollaborationServiceFilter} from '@kit.ServiceCollaborationKit';

#### createCollaborationServiceMenuItems

createCollaborationServiceMenuItems(businessFilter?: Array<CollaborationServiceFilter>): void

Creates a selector that displays a list of devices with required capabilities on the network. It is called in the [Menu](../../../../../application-framework/arkui/arkts-components/menus/menu/document.md) component.

This method is a custom builder function. You need to learn about [@Builder](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/arkts-builder) before using this method.

**Decorator type**: @Builder

**System capability**: SystemCapability.Collaboration.Service

**Device behavior differences**: This API can be called on PCs/2-in-1 devices and tablets. However, on other devices, the device list cannot be displayed, and the Device Interconnectivity capability cannot be used.

**Start version**: 5.0.0(12)

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

Array<[CollaborationServiceFilter](#section12639651397)\>

 | 

No

 | 

Capability type. The default value is **ALL**, which matches cross-device photographing, document scanning, and image selector.

For API 6.0.0(20) and later versions, cross-device photographing, document scanning, image selector, video selector, and image and video selector are supported. For versions earlier than API 6.0.0(20), only cross-device photographing, document scanning, and image selector are supported.

 |

**Example**:

@Builder
MyTestMenu() {
  Menu() {
    createCollaborationServiceMenuItems(\[CollaborationServiceFilter.ALL\]) 
  }
}

#### createCollaborationServiceMenuItems

createCollaborationServiceMenuItems(businessFilter: Array<CollaborationServiceFilter>, canReceiveNumber: number): void

Creates a selector that displays a list of devices with required capabilities on the network. It is called in the [Menu](../../../../../application-framework/arkui/arkts-components/menus/menu/document.md) component. This API can be used to customize the number of images that can be selected in the gallery of the remote device and passed to the local device.

This method is a custom builder function. You need to learn about [@Builder](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/arkts-builder) before using this method.

**Decorator type**: @Builder

**System capability**: SystemCapability.Collaboration.Service

**Device behavior differences**: This API can be called on PCs/2-in-1 devices and tablets. However, on other devices, the device list cannot be displayed, and the Device Interconnectivity capability cannot be used.

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

businessFilter

 | 

Array<[CollaborationServiceFilter](#section12639651397)\>

 | 

Yes

 | 

Capability type. The default value is **ALL**, which matches cross-device photographing, document scanning, and image selector.

For API 6.0.0(20) and later versions, cross-device photographing, document scanning, image selector, video selector, and image and video selector are supported. For versions earlier than API 6.0.0(20), only cross-device photographing, document scanning, and image selector are supported.

 |
| 

canReceiveNumber

 | 

number

 | 

Yes

 | 

Maximum number of photos that can be passed. The value ranges from 1 to 50. If the value is less than or equal to 0, the capability of the called device will not be started. If the value is greater than 50, the value **50** is used.

 |

**Example**:

@Builder
MyTestMenu() {
  Menu() {
    createCollaborationServiceMenuItems(\[CollaborationServiceFilter.ALL\], 30) 
  }
}

#### CollaborationServiceFilter

Enumerated values of the capability type.

**System capability**: SystemCapability.Collaboration.Service

**Device behavior differences**: This API can be called on PCs/2-in-1 devices and tablets. However, on other devices, the device list cannot be displayed, and the Device Interconnectivity capability cannot be used.

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

ALL

 | 

0

 | 

Matches cross-device photographing, document scanning, and image selector.

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

 |
| 

IMAGE\_PICKER

 | 

3

 | 

Matches the image selector.

 |
| 

VIDEO\_PICKER

 | 

5

 | 

Matches the video selector.

**Start version**: 6.0.0(20)

 |
| 

IMAGE\_VIDEO\_PICKER

 | 

6

 | 

Matches the image and video selector.

**Start version**: 6.0.0(20)

 |

**Example**:

@Builder
MyTestMenu() {
  Menu() {
    createCollaborationServiceMenuItems(\[CollaborationServiceFilter.ALL\], 30) 
  }
}

#### CollaborationServiceStateDialog

Displays a dialog box to show the status of the matched app on the remote device.

You need to implement the [onState](#section33027582114) method and define this dialog box component on the page. The collaboration framework calls this method to complete the services.

This component is a custom component. You need to learn about [@Component](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/arkts-create-custom-components#component) before using it.

**Decorator type**: @Component

**System capability**: SystemCapability.Collaboration.Service

**Device behavior differences**: This API can be called on PCs/2-in-1 devices and tablets. However, on other devices, the device list cannot be displayed, and the Device Interconnectivity capability cannot be used.

**Start version**: 5.0.0(12)

#### \[h2\]onState

onState: (stateCode: number, bufferType: string, buffer: ArrayBuffer) => void

Callback function used to receive data. **stateCode** indicates the service completion status, **bufferType** indicates the type of the returned data, and **buffer** indicates the returned data content. You need to implement the **onState** method based on the status and data, as well as the service logic.

**System capability**: SystemCapability.Collaboration.Service

**Device behavior differences**: This API can be called on PCs/2-in-1 devices and tablets. However, on other devices, the device list cannot be displayed, and the Device Interconnectivity capability cannot be used.

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

stateCode

 | 

number

 | 

Yes

 | 

Service completion status. For details, refer to the result code table below.

 |
| 

bufferType

 | 

string

 | 

Yes

 | 

Type of the data returned.

**general.image**: image.

**general.fileName**: document name.

**general.video**: video.

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

**Result codes**

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
| 

1001202006

 | 

Returned file name.

 |
| 

1001202007

 | 

If the value of **canReceiveNumber** passed to [createCollaborationServiceMenuItems](#section149271552154711) is less than or equal to 0, the capability of the called device will not be started.

 |

#### \[h2\]build

build(): void

Default constructor of a struct. You cannot directly call this method.

**System capability**: SystemCapability.Collaboration.Service

**Device behavior differences**: This API can be called by components on PCs/2-in-1 devices and tablets. However, on other devices, the device list cannot be displayed, and the Device Interconnectivity capability cannot be used.

**Start version**: 5.0.0(12)

**Example**

Refer to the sample code below to call an app on the remote device.

For details about Device Interconnectivity, please refer to [Introduction to Device Intertconnectivity](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/servicecollaboration-service-overview).

import {
  createCollaborationServiceMenuItems,
  CollaborationServiceStateDialog,
  CollaborationServiceFilter
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
      createCollaborationServiceMenuItems(\[CollaborationServiceFilter.ALL\], 30)
    }
  }

  build() {
    Column({ space: 20 }) {
      CollaborationServiceStateDialog({
        onState: (stateCode: number, bufferType: string, buffer: ArrayBuffer): void => this.doInsertPicture(stateCode, bufferType, buffer)
      })
      Button ('Use remote device to take photos')
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

  doInsertPicture(stateCode: number, bufferType: string, buffer: ArrayBuffer): void {
    if (stateCode != 0) {
      return
    }
    if (bufferType == "general.image") {
      let imageSource = image.createImageSource(buffer)
      imageSource.createPixelMap().then((pixelMap) => {
        this.picture = pixelMap;
      })
    }
  }
}
