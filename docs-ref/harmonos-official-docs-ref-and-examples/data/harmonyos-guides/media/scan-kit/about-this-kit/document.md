# About This Kit

Scan Kit provides the system-level barcode scanning service that collaborates software and hardware. It innovatively introduces a simpler "scan-to-access" capability. You can utilize the system's scanning capability to achieve seamless redirection to your app with minimal integration workload, eliminating the need to develop a dedicated code scanning module within your app itself. The kit also offers barcode recognition and barcode image generation capabilities for all kinds of scenarios in your app.

Leveraging multiple computer vision technologies and AI algorithms, Scan Kit can automatically scan barcodes that are far away from the camera and recognize barcodes in low-light environments as well as barcodes that are damaged, unclear, or in a hard-to-read position for accurate scanning in all kinds of environments. This leads to a higher barcode recognition rate and improved user experience.

To make it easier for you to integrate the capability, a detailed [demo project](https://gitcode.com/HarmonyOS_Samples/scan-kit_-sample-code_-clientdemo_-arkts) is provided for your reference.

#### Use Cases

Scan Kit provides two capabilities: scan-to-access capability and in-app barcode scanning capability. You need to integrate the scan-to-access capability first to achieve one-step direct access to your app service with minimal effort.

-   Scan-to-access capability: allows users to access a specified page in your app by scanning a 2D code or 1D code via a system-level entry such as Control Panel. This streamlines the access process, letting users reach the desired service page within your app in a single step.
-   Barcode scanning by default UI: offers a consistent scanning UI at the system level, which includes a camera preview stream, a scanning entry for the photo gallery, a prompt to turn on the flash light in dim light conditions, and pre-authorization for the camera. This function is easy to be integrated and is suitable for general scanning scenarios.
-   Barcode scanning by custom UI: provides scanning capabilities and supports rendering the camera preview stream on the specified control. You need to implement the scanning UI and apply for camera permissions. This is suitable for scenarios that require a personalized scanning UI.
-   Image-based barcode recognition: scans and recognizes barcode images or images in the photo gallery.
-   Barcode image generation: generates a barcode image from text or a byte array.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cd/v3/F6iuZ12VQJSTTVmQvUKZ_g/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062045Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=AB80FC556C4F0CE1ABFD4FF5A00A05A1351F81269476551E6117B14F7780DEAA)

Scan Kit supports recognition and generation for barcodes of 13 mainstream formats in the world, as well as recognition for the multifunctional code. Currently, the following barcode formats are supported: QR Code, Data Matrix, PDF417, Aztec, EAN-8, EAN-13, UPC-A, UPC-E, Codabar, Code 39, Code 93, Code 128, and ITF-14.

#### Restrictions

| 
Capability

 | 

Restriction

 |
| :-- | :-- |
| 

Scan-to-access capability

 | 

1.  This capability currently supports only HTTPS-based links. If you need to use other access modes, such as HTTP, [submit a ticket](https://developer.huawei.com/consumer/en/support/feedback/#/) to contact us.
2.  Currently, this capability is available only in the Chinese mainland.

 |
| 

Barcode scanning by default UI

 | 

The floating window and split-screen scenarios are supported since version 6.0.0(20). Gallery-based barcode scanning can only recognize one barcode at a time. The default UI does not support custom settings.

 |
| 

Barcode scanning by custom UI

 | 

This capability requires the camera permission and needs you to implement the interactive scanning UI by yourself.

 |
| 

Barcode image generation

 | 

If the data that Scan Kit recognizes from a barcode image generated based on a byte array is garbled characters, a dedicated decoder is required to decode the byte array. Such cases include barcode recognition of subway turnstiles.

 |

## Supported Devices

-   The scan-to-access, barcode scan by default UI, barcode scan by custom UI, and image-based barcode recognition capabilities support only phones and tablets.
-   The barcode image generation capability supports phones, tablets, wearables, 2-in-1 devices, and TVs. Specifically, wearables are supported since version 5.1.0(18), and 2-in-1 devices and TVs are supported since version 5.1.1(19).

#### Emulator Support

This kit supports the Emulator, but there are some differences in feature support between real devices and the Emulator:

-   General differences: For details, please refer to [Differences Between the Emulator and the Real Device](../../../coding-and-debugging/running-your-app-on-the-emulator/overview/differences-between-the-emulator-and-the-real-device/document.md#section1227613205203).
-   Since version 6.0.0(20), using the Emulator for developing the function of barcode scanning on the default UI is supported. On the Emulator, the camera stream on the default scanning UI is flipped horizontally, and black borders will appear at the top and bottom of the scanning UI due to the fixed resolution of the camera stream.
-   Some APIs regarding barcode scanning by custom UI support Emulator-based development.
    -   Since version 6.0.0(20), Emulator-based development is available for certain APIs regarding barcode scanning by custom UI (including [init](https://developer.huawei.com/consumer/en/doc/harmonyos-references/scan-customscan-api#section447114223245), [start](https://developer.huawei.com/consumer/en/doc/harmonyos-references/scan-customscan-api#section38711535114711), [stop](https://developer.huawei.com/consumer/en/doc/harmonyos-references/scan-customscan-api#section6949611114915), [release](https://developer.huawei.com/consumer/en/doc/harmonyos-references/scan-customscan-api#section1109456134917), and [rescan](https://developer.huawei.com/consumer/en/doc/harmonyos-references/scan-customscan-api#section19244173211169)), which are enough for implementing basic functions of this barcode scanning scenario.
    -   On the Emulator, barcode scanning by custom UI supports only 1280 x 720 px. Other resolutions will be converted to 1280 x 720 px.
-   The Emulator does not support image-based barcode recognition or barcode image generation.

#### Sample Code

Scan Kit provides the [sample code](https://gitcode.com/HarmonyOS_Samples/scan-kit_-sample-code_-clientdemo_-arkts) related to functions including barcode scanning by default UI, barcode scanning by custom UI, image-based barcode recognition, and barcode image generation. You can refer to the sample code to implement desired functions.
