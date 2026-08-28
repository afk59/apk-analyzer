# Overview of Device Interconnectivity NDKs

Device Interconnectivity enables a TV, tablet, or 2-in-1 device to use the camera, scanning, gallery, and other functions of a phone.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/de/v3/GhZHXcqpRDmDnB23LyeJbw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062019Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=5993DFE119EF7EB7E0DB52640924675F33ED8F63736BE19E7A54B8E0E81A7038)

This section details how to use the photographing function. The operations relating to scanning and gallery functions are similar to the photographing operations.

A user may need to take some photos as material when using a rich text editing app (such as a memo or note app, or an email app) on a TV, tablet, or 2-in-1 device. However, it can be inconvenient to use the current device to take photos. In this case, the user can leverage the photographing capability of Device Interconnectivity to specify a tablet or a phone in the app on the current device and open the camera of the tablet or phone to take photos. A phone or tablet is more suitable for photo-taking thanks to its mobility, support for easy framing, and powerful camera capabilities. The photos taken can be quickly sent back to the rich text editing app on the TV, tablet, or 2-in-1 device, helping the user efficiently design documents with images and text.

If there are multiple phones or tablets on the same network, the user can select different devices for photo-taking.

#### Operations Mechanism

Based on the distributed collaboration framework, the [HMS\_ServiceCollaboration\_GetCollaborationDeviceInfos](https://developer.huawei.com/consumer/en/doc/harmonyos-references/servicecollaboration-capi-module#gaeffea1546cbe64aeba533e5b72bca7ba) (listing devices), [HMS\_ServiceCollaboration\_StartCollaboration](https://developer.huawei.com/consumer/en/doc/harmonyos-references/servicecollaboration-capi-module#section4531193410296) (starting Device Interconnectivity), and [HMS\_ServiceCollaboration\_StopCollaboration](https://developer.huawei.com/consumer/en/doc/harmonyos-references/servicecollaboration-capi-module#section67211235132913) (stopping Device Interconnectivity) APIs are provided for cross-device photographing. You only need to call the three APIs to implement cross-device photographing, rather than focusing on details such as data transmission and command control in distributed scenarios.

1.  **Cross-device automatic link establishment based on the distributed collaboration framework of the system**
    
    Through the distributed collaboration framework of the system, the local device (2-in-1 device/tablet) is automatically connected to the remote device (phone/tablet) if the same account is signed in on both devices. The system automatically completes processes such as device discovery, connection, and authentication, provides information about available remote devices with camera, scanning, and gallery capabilities through [HMS\_ServiceCollaboration\_GetCollaborationDeviceInfos](https://developer.huawei.com/consumer/en/doc/harmonyos-references/servicecollaboration-capi-module#gaeffea1546cbe64aeba533e5b72bca7ba), starts the corresponding capability of Device Interconnectivity through [HMS\_ServiceCollaboration\_StartCollaboration](https://developer.huawei.com/consumer/en/doc/harmonyos-references/servicecollaboration-capi-module#section4531193410296), and terminates the capability through [HMS\_ServiceCollaboration\_StopCollaboration](https://developer.huawei.com/consumer/en/doc/harmonyos-references/servicecollaboration-capi-module#section67211235132913).
    
2.  **User's photo-taking with the remote device**
    1.  The user uses the remote device to take photos and confirm the photos, which are then sent back to the app on the local device.
    2.  Camera on the remote device is automatically closed, and the device returns to its original state.
