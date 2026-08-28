# Overview

Share Kit provides the Tap to Transfer feature, allowing users to initiate cross-device sharing simply by tapping the tops of the sending and receiving devices together. This feature enables image transfer, Wi-Fi sharing, and more.

#### Use Case

-   A host app displays a page with a shareable item, for example, when a user opens or selects a file, a memo, a contact's details, or a personal hotspot/Wi-Fi.
-   A host app displays a page with multiple shareable items, for example, when a user selects multiple images.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5/v3/Q_EaV435THm7wn0Uuhv5Hw/en-us_image_0000002513289509.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062122Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=B52BEBFFA367762CDCDC54A5D1638B74374C5BCD2EBBEB7E8B00028CBCA977A6 "Click to enlarge")

#### Service Process

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fe/v3/blHvPuFzSvWdh1E7HfIo3Q/en-us_image_0000002481169652.jpg?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062122Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=82E2F38EA1D8C1815ECCEF543F603A219C7C5830C665562F0F922410E4A15C9C "Click to enlarge")

The process is as follows:

1.  The host app registers a Tap to Transfer event listener and is tapped against a screen-on, unlocked target device.
2.  The host app detects the target device, calls the Tap to Transfer event callback, constructs the data to be shared in the callback event, and sends the data.
3.  The target device receives and processes the shared data.
4.  The host app unregisters the Tap to Transfer event listener.

#### Restrictions

To initiate the Tap to Transfer function from a mobile app, both devices must be **unlocked with the screen on**, and have the Huawei Share service enabled (enabled by default). A gentle tap at the tops of the devices will trigger the sharing process. If a user has manually disabled Huawei Share, the user will receive a system notification when a Tap to Transfer event is triggered, asking them to enable Huawei Share.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e2/v3/Z-l7XTU2TCynGM29EF21Mg/en-us_image_0000002513409483.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062122Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=06A184D85FD749BECE3C92048EA3CD8A2F445BE2DB65141C5FB8D20FB4CE0C30 "Click to enlarge")

Processing mechanism of Share Kit:

-   If either device does not support the Tap to Transfer function, there will be no response when the tops of two devices are tapped together.
-   Share Kit does not send sharing results to host apps. Instead, Share Kit notifies the users who initiate sharing of the sharing result (accepted or rejected) through system notifications.

#### Environment Requirements

-   Supported phone systems: HarmonyOS NEXT Release or later. You can use [canIUse](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-syscap#caniuse) to check whether a system capability is supported.
    
    if (canIUse('SystemCapability.Collaboration.HarmonyShare')) {
      // Support the Tap to Transfer capability.
    }
    

-   Integrated development environment: DevEco Studio NEXT Beta1 or later.
