# About This Kit

Service Collaboration Kit provides the capability of multi-device collaboration based on the same account.

#### Use Case

| 
Use Case

 | 

Description

 |
| :-- | :-- |
| 

Scenarios to which Device Interconnectivity applies

 | 

Users can leverage this capability to implement cross-device interaction and use the camera, scanning, and gallery functions of different devices.

 |

#### Basic Concepts

Device Interconnectivity enables a tablet or 2-in-1 device to use the camera, scanning, gallery, and other functions of a phone.

#### Supported Devices

Device Interconnectivity (ArkTS) supports phones, tablets, and PCs/2-in-1 devices. Device Interconnectivity (NDK) supports phones, tablets, PCs/2-in-1 devices, and TVs. Currently, this feature is not supported on the Emulator.

#### Function Restrictions

| 
Capability

 | 

Restriction

 |
| :-- | :-- |
| 

Device Interconnectivity

 | 

-   A HUAWEI ID should be signed in on both the local and remote devices, and Wi-Fi and Bluetooth must be enabled on the devices.
-   The local device should be a tablet or 2-in-1 device running HarmonyOS NEXT or later. The remote device should be a phone or tablet running HarmonyOS NEXT or later and supporting the camera function.
-   Device Interconnectivity APIs can be used to invoke devices based on specific invoking policies: A 2-in-1 device can invoke tablets and phones, while a tablet can only invoke phones. The local device and remote device cannot be of the same type.

 |
