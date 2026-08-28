# Device Interconnectivity (RichEditor Control)

The [RichEditor](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ts-basic-components-richeditor) control has integrated the Device Interconnectivity capability, which can be used by right-clicking the control. Device Interconnectivity enables a tablet or 2-in-1 device to use the camera, scanning, gallery, and other functions of a phone.

#### Use Case

You can leverage this capability to implement cross-device interaction and enable the use of camera, scanning, and gallery functions of different devices.

#### Restrictions

This capability is available only when the following conditions are met:

-   **Restrictions on devices**
    -   Local device: a tablet or 2-in-1 device running HarmonyOS NEXT or later
    -   Remote device: a phone or tablet that runs HarmonyOS NEXT or later and supports the camera function
-   **Restrictions on usage**
    -   The same HUAWEI ID is signed in on both devices.
    -   Device Interconnectivity APIs can be used to invoke devices based on specific invoking policies: A 2-in-1 device can invoke tablets and phones, while a tablet can only invoke phones. The local device and remote device cannot be of the same type.
    -   Wi-Fi and Bluetooth are enabled on both devices.
        
        It is recommended that the two devices be connected to the same LAN to improve the camera wake-up speed.
        

#### Development Procedure

-   Add the [RichEditor](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ts-basic-components-richeditor) component. Right-click the component and choose a required function of a device from the shortcut menu to import images. The **onWillChange** attribute is used to process the returned images.
    
    @Entry
    @Component
    struct Index {
      controller: RichEditorController = new RichEditorController()
      options: RichEditorOptions = { controller: this.controller }
    
      build() {
        Column() {
          Column() {
            RichEditor(this.options)
              .onWillChange((value: RichEditorChangeValue) => {
                if (value?.replacedImageSpans\[0\]?.imageStyle?.objectFit != 0) {
                  return true;
                }
                for(let item of value.replacedImageSpans) {
                  this.controller.addImageSpan(item.valuePixelMap, {
                    imageStyle: {
                      size: \["500px", "500px"\],
                      layoutStyle: {
                        borderRadius: '10px',
                      }
                    }
                  })
                }
                return false;
              })
              .borderWidth(1)
              .borderColor(Color.Green)
              .width("100%")
              .height("100%")
          }
          .borderWidth(1)
          .borderColor(Color.Red)
          .width("100%")
          .height("70%")
        }
      }
    }
    

The usage process is outlined as follows:

1\. Right-click the **RichEditor** component.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5/v3/MHZqYA7xTfmgs9SqTXgT8A/en-us_image_0000002453064537.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062019Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=BC4816A76193EBC3775D96E7C89B27D56E2ED78DE3F8426AEC0B93384EAA8794)

2\. Select the capability to be used.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/50/v3/TQREXcSoR3e-VvhMkh1JLA/en-us_image_0000002419505708.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062019Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=B9E608929C0E55466E5E94929627329F0F502FF668279F689AAA2334ADC15B9B)

3\. Wait for the remote device to send back the photo taken.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4c/v3/674OcX7BTumKx0Blpa79UQ/en-us_image_0000002453064721.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062019Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=DD809249AD81FBE8C69DCE24170E66CC38122C0CA24514AA50ACF44E4B19E5CF)

4\. View the image sent back.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7e/v3/pPDCHsSUTmK85WH1zsppYA/en-us_image_0000002361551566.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062019Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=2614D33FEFA72DB05C5667B4C7A56C4F969A946398FE9ACE9DDE45396BE7891D)

#### Disabling Device Interconnectivity of RichEditor

To disable the Device Interconnectivity capability integrated by RichEditor (shown in the shortcut menu), you can remove the relevant menu items through the **editMenuOptions** attribute. The following is the sample code:

@Entry
@Component
struct Index {
  controller: RichEditorController = new RichEditorController()
  options: RichEditorOptions = { controller: this.controller }

  build() {
    Column() {
      Column() {
        RichEditor(this.options)
          .editMenuOptions({
            onCreateMenu: (menuItems: Array<TextMenuItem>) => {
              if (menuItems.length === 0) {
                return menuItems;
              }
              let newMenuItems: TextMenuItem\[\] = \[\];
              menuItems.forEach((item, index) => {
                if(!item.id.equals(TextMenuItemId.COLLABORATION\_SERVICE)) {
                  newMenuItems.push(item);
                }
              })
              return newMenuItems;
            },
            onMenuItemClick: (menuItem: TextMenuItem, textRange: TextRange) => {
              return false;
            }
          })
          .borderWidth(1)
          .borderColor(Color.Green)
          .width("100%")
          .height("100%")
      }
      .borderWidth(1)
      .borderColor(Color.Red)
      .width("100%")
      .height("70%")
    }
  }
}
