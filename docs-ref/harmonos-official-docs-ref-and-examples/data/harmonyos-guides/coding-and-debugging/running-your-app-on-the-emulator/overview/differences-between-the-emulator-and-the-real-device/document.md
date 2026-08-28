# Differences Between the Emulator and the Real Device

The Emulator is a convenient tool for developing and debugging HarmonyOS apps and atomic services. For example, you can develop and debug atomic services without configuring the server domain name. In most cases, pushing packages for debugging on the Emulator does not require signing; however, some Kits still require signing to run properly. For specific requirements, see the corresponding Kit development guides.

Due to differences in hardware and capabilities between the Emulator and real devices, some functional scenarios still need to be tested on real devices. This document helps you to determine which features to test on the Emulator and which on real devices.

#### General Differences

The Emulator is a virtual machine app running on a macOS or Windows computer. It uses the computer's hardware resources, including CPUs, memory, and network connections. These resources may differ significantly from those of real devices in terms of capacity and speed. Therefore, the Emulator is not suitable for testing the performance (for example, data processing, graphics rendering, and network speed) or resource usage (for example, memory, CPU, and power consumption) of apps/atomic services. Performance test results from the Emulator can only be used to evaluate relative differences in app functionalities. To obtain user experience data in real scenarios, you are advised to conduct tests on real devices.

#### Display Effect Differences

-   The Emulator uses the computer's display, which differs from the screen of real devices. This may cause jagged edges on text and images displayed in the Emulator. Enlarging the Emulator window can make text and images clearer.
-   The color gamut range of computer screens may differ from that of mobile devices, leading to inaccurate color display.
-   The Emulator does not support screen brightness adjustment.

#### Graphics API Differences

-   OpenGL ES 3.1 and 3.2 APIs are not supported.
-   Vulkan APIs are not supported.

#### Kit Differences

Some kits cannot be used on the Emulator. For details, see the following description. Some Kits are restricted by device types and regions. For details, see the corresponding Kit guide.

If an app crashes due to unsupported Kits, [import Kits dynamically](../../../../application-framework/arkts/arkts-runtime/arkts-modularization/dynamic-import/document.md#implementation-of-dynamic-import).

Example of an error message caused by unsupported Kits:

LastFatalMessage:\[default\] \[LoadJSPandaFile:00\] resolveBufferCallback get hsp buffer failed,hsp path:/data/storage/el1/bundle/com.huawei.hmos.{KitName}.kit

## App Framework

The Emulator does not support:

-   Ability Kit: launching vertical app panels, inter-application jumps using App Linking, and launching atomic services in installation-free mode.
-   Accessibility Kit: features except ScreenReader.
-   Background Tasks Kit: suspending short tasks.
-   Data Augmentation Kit
-   UI Design Kit: sidebar style setting, sidebar menu style setting, bleeding style setting for bottom tab icons, instant operation setting, core operation bar setting, list setting, custom symbol loading, and visual effect.

## Security

The Emulator does not support:

-   Data Protection Kit
-   Device Security Kit
-   Enterprise Data Guard Kit
-   Online Authentication Kit
-   Secure GPS positioning, face recognition, and device certificates

## Network

The Emulator does not support:

-   Distributed Service Kit
-   NearLink Kit
-   Network Boost Kit
-   Service Collaboration Kit
-   Telephony Kit

## Basic Features

-   Input Kit: operations such as changing the cursor style.
-   MDM Kit

## Hardware

The Emulator does not support:

-   Car Kit
-   Driver Development Kit
-   Mechanic Kit
-   Multimodal Awareness Kit
-   Pen Kit
-   Sensor Service Kit: partially supported. For details, see [Virtual Sensor](../../using-the-emulator/using-extended-features/document.md#section830415558395).
-   Wear Engine Kit

## Media

The Emulator does not support:

-   Camera Kit: features except preview and photo taking
-   DRM Kit
-   Scan Kit: code image generation and image data recognition
-   Images in HEIF format
-   Video files that are not in H.264 format or not in RGBA pixel format
-   Video recording, transcoding, processing, and screen recording

## Graphics

The Emulator does not support:

-   AR Engine
-   ArkGraphics 3D
-   Graphics Accelerate Kit
-   Spatial Recon Kit
-   XEngine Kit

## App Services

The Emulator does not support:

-   AppGallery Kit: digital goods service, AppGallery recommendations, ecosystem inquiry service, AppGallery updates, app review service, icon management service, and device-cloud interaction
-   App Linking Kit
-   Call Service Kit
-   Enterprise Space Kit
-   Game Service Kit
-   Health Service Kit: wearable app development, health data linking service, real-time activity rings data, manual data synchronization, Health app capabilities, and default privacy authorization.
-   IAP Kit
-   Location Kit: geofences
-   Map Kit: 3D maps and map screenshots
-   Payment Kit
-   PDF Kit: x86 emulator version
-   Preview Kit: preview of .pdf/.pptx/.xlsx/.docx files
-   Push Kit: push of authorized subscription messages, notification extension messages, live view messages, and in-app call messages
-   Reader Kit
-   Scenario Fusion Kit: For details, see [Emulator Support](../../../../application-services/scenario-fusion-kit/about-this-kit/document.md#section1901742183715).
-   Share Kit: cross-device sharing and sharing based on Intents Kit
-   Wallet Kit
-   Weather Service Kit

## AI

The Emulator does not support:

-   CANN Kit
-   Core Vision Kit
-   Agent Framework Kit
-   Intents Kit
-   MindSpore Lite Kit: features except image classification
-   Natural Language Kit
-   Neural Network Runtime Kit
-   Speech Kit
-   Vision Kit

#### Other Differences

**Table 1**
| 
Significant Difference

 | 

Affected Scenario

 |
| :-- | :-- |
| 

SIM card

 | 

Does not support making calls or sending text messages.

 |
| 

USB

 | 

Does not support connection or data transfer.

 |
| 

Bluetooth

 | 

Does not support Bluetooth device scanning, connection, or data transfer.

 |
| 

NearLink

 | 

Does not support NearLink device scanning, connection, data transfer, or distributed capabilities.

 |
| 

NFC

 | 

Does not support NFC card read, write, or tapping.

 |
| 

Trusted Execution Environment (TEE)

 | 

Does not support certain security-related Kits temporarily. For details, see [Kit Differences](#section147193483010).

 |
| 

NPU

 | 

Does not support certain AI-related Kits temporarily. For details, see [Kit Differences](#section1155211435325).

 |
| 

Biometrics

 | 

Does not support fingerprint or face authentication.

 |
| 

Camera/Microphone

 | 

Relies on computer devices; does not support multi-camera switching (wide-angle/telephoto), flash, or noise reduction algorithms.

 |
| 

Power

 | 

Emulates power supply; does not support scenarios such as screen on/off, temperature control, or fast charging.

 |

#### Kit Support Changes

## DevEco Studio 6.0.2 Beta1

-   Health Service Kit: user authorization management, data source management, and health data management (including sampled data, workout records, and health records) within phone/tablet apps, as well as default privacy authorization of Health.

## DevEco Studio 6.0.1 Release

-   Ringtone Kit

## DevEco Studio 6.0.0 Beta5

The Emulator supports:

-   Ads Kit
-   AppGallery Kit: on-demand distribution of product features, app attribution, and APIs that do not involve device-cloud interaction in privacy management
-   Cloud Foundation Kit: Cloud Functions, Cloud DB, and Cloud Storage. For details, see [Debugging on the Emulator](../../../../application-services/cloud-foundation-kit/debugging-on-the-emulator/document.md).

## DevEco Studio 6.0.0 Beta3

-   Screen Time Guard Kit

## DevEco Studio 6.0.0 Beta2

-   Accessibility Kit: ScreenReader

## DevEco Studio 6.0.0 Beta1

The Emulator supports:

-   Core Speech Kit
-   Scan Kit: code scanning via computer cameras

## DevEco Studio 5.1.1 Beta1

-   Native Development Kit: JSVM supported on the x86 version

## DevEco Studio 5.1.0 Release

The Emulator supports:

-   PDF Kit: ARM emulator version
-   Map Kit: features except 3D maps and map screenshots
-   Camera Kit: preview and photo taking
-   Share Kit: features except cross-device sharing and sharing based on Intents Kit
