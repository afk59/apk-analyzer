# Device Interconnectivity Development Guide

Device Interconnectivity enables a tablet or 2-in-1 device to use the camera, scanning, gallery, and other functions of a phone.

#### Use Case

You can leverage this capability to implement cross-device interaction and enable the use of camera, scanning, and gallery functions of different devices.

#### Restrictions

This feature is available only when the following conditions are met:

-   **Restrictions on devices**
    -   Local device: a tablet or 2-in-1 device running HarmonyOS NEXT or later
    -   Remote device: a phone or tablet that runs HarmonyOS NEXT or later and supports the camera function
-   **Restrictions on usage**
    -   The same HUAWEI ID is signed in on both devices.
    -   Device Interconnectivity APIs can be used to invoke devices based on specific invoking policies: A 2-in-1 device can invoke tablets and phones, while a tablet can only invoke phones. The local device and remote device cannot be of the same type.
    -   Wi-Fi and Bluetooth are enabled on both devices.
        
        It is recommended that the two devices be connected to the same LAN to improve the camera wake-up speed.
        

#### API Description

Please read the [API reference](https://developer.huawei.com/consumer/en/doc/harmonyos-references/servicecollaboration-collaborationservice) before developing a specific function.

| 
API

 | 

Description

 |
| :-- | :-- |
| 

[createCollaborationServiceMenuItems](https://developer.huawei.com/consumer/en/doc/harmonyos-references/servicecollaboration-collaborationservice#section1633482912443)

 | 

Device-specific capability selector. Obtains a list of devices with required capabilities of Device Interconnectivity on the network.

 |
| 

[CollaborationServiceStateDialog](https://developer.huawei.com/consumer/en/doc/harmonyos-references/servicecollaboration-collaborationservice#section158671330145417)

 | 

Displays a dialog box to show the status of the matched service on the remote device.

 |

#### Development Procedure

1.  Import required modules.
    
    import { createCollaborationServiceMenuItems, CollaborationServiceStateDialog, CollaborationServiceFilter } from '@kit.ServiceCollaborationKit';
    
    [createCollaborationServiceMenuItems](https://developer.huawei.com/consumer/en/doc/harmonyos-references/servicecollaboration-collaborationservice#section1633482912443) is the device-specific capability menu module, which passes the enumerated values of [CollaborationServiceFilter](https://developer.huawei.com/consumer/en/doc/harmonyos-references/servicecollaboration-collaborationservice#section12639651397). [CollaborationServiceStateDialog](https://developer.huawei.com/consumer/en/doc/harmonyos-references/servicecollaboration-collaborationservice#section158671330145417) is the status dialog box module.
    
2.  Call createCollaborationServiceMenuItems in Menu to add a device-specific capability selector. A device-specific capability list is displayed in the menu.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7b/v3/JDS5lNO0TfadWWVHVb7v7A/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062019Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=DE97FDF103B3F3CCE09462937C26D8A20D78ADAF1C95EA7C5FF4C18113EF4CC7)
    
    Before calling the [createCollaborationServiceMenuItems](https://developer.huawei.com/consumer/en/doc/harmonyos-references/servicecollaboration-collaborationservice#section1633482912443), you need to know that:
    
    -   This method needs to be called in the [Menu](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ts-basic-components-menu) component.
    -   This method is a custom builder function. You need to know the knowledge of [@Builder](../../../../../application-framework/arkui/ui-development-arkts-based-declarative-development-paradigm/basic-syntax-of-ui-paradigms/component-extension/builder-decorator-custom-builder-function/document.md) before using it.
    
3.  The corresponding capabilities can be used only after the enumerated values (of the array type) of [CollaborationServiceFilter](https://developer.huawei.com/consumer/en/doc/harmonyos-references/servicecollaboration-collaborationservice#section12639651397) is passed. Currently, **ALL**, **TAKE\_PHOTO**, **SCAN\_DOCUMENT**, **IMAGE\_PICKER**, **VIDEO\_PICKER**, and **IMAGE\_VIDEO\_PICKER** are supported.
    
    **ALL** is reserved, which matches cross-device photographing, document scanning, and image selector. The functions will be expanded in the future. **TAKE\_PHOTO** matches the cross-device photographing capability; **SCAN\_DOCUMENT** matches the cross-device scanning capability; **IMAGE\_PICKER** matches the cross-device gallery access capability; **VIDEO\_PICKER** matches the cross-device video selector; and **IMAGE\_VIDEO\_PICKER** matches the image and video selector.
    
    @Builder
    MyTestMenu() {
      Menu() {
        createCollaborationServiceMenuItems(\[CollaborationServiceFilter.ALL\]) 
      }
    }
    
4.  Add [CollaborationServiceStateDialog](https://developer.huawei.com/consumer/en/doc/harmonyos-references/servicecollaboration-collaborationservice#section158671330145417) in the **build** method to display the shooting status of the remote device and send data back to the local device. The [onState](https://developer.huawei.com/consumer/en/doc/harmonyos-references/servicecollaboration-collaborationservice#section33027582114) method needs to be implemented. [CollaborationServiceStateDialog](https://developer.huawei.com/consumer/en/doc/harmonyos-references/servicecollaboration-collaborationservice#section158671330145417) displays a global dialog box and does not affect the original layout.
5.  Bind and implement the [onState](https://developer.huawei.com/consumer/en/doc/harmonyos-references/servicecollaboration-collaborationservice#section33027582114) method for the dialog box component to receive and process photo data.
    
    The input parameter **stateCode** indicates the service completion status, and **buffer** indicates the data content sent back. The [onState](https://developer.huawei.com/consumer/en/doc/harmonyos-references/servicecollaboration-collaborationservice#section33027582114) method needs to be implemented based on the status and data content, as well as the service logic.
    
    CollaborationServiceStateDialog({
      onState: (stateCode: number, bufferType: string, buffer: ArrayBuffer):void => this.doInsertPicture(stateCode, bufferType, buffer)
    })
    

#### Complete Sample Code for Device Interconnectivity

Refer to the sample code below to call a remote camera to take a photo.

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
      createCollaborationServiceMenuItems(\[CollaborationServiceFilter.ALL\])
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

#### Sample Code

-   [Device Interconnectivity](https://gitcode.com/HarmonyOS_Samples/service-collaboration-kit-sample-code-arkts)
