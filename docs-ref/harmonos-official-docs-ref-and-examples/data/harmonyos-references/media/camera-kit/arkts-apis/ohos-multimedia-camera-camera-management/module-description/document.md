# Module Description

The module provides a set of easy-to-use camera service APIs. With these APIs, you can create camera applications that access and control camera hardware to achieve basic functions like previewing, taking photos, and recording videos. In addition, you can combine these APIs to perform advanced operations, such as controlling the flash, exposure time, and focus.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/61/v3/MsjvnqBVTg2bd2bSjl3EoQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062425Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=1DCE84BEFE72468E8E2AA8A62FF498EE0E843CC53F63125D5DA520C877401275)

The initial APIs of this module are supported since API version 10. Newly added APIs will be marked with a superscript to indicate their earliest API version.

This module contains the following classes:

-   [AutoDeviceSwitch](../interface-autodeviceswitch/document.md) class, which provides the capabilities of checking the support for automatic camera switching and enabling or disabling automatic camera switching.
-   [AutoExposure](../interface-autoexposure/document.md) class, which provides the capabilities related to the device's automatic exposure feature, including setting or querying the exposure value, metering point, and exposure compensation.
-   [CameraInput](../interface-camerainput/document.md) class, which provides the capabilities of enabling or disabling the camera switch and listening for input stream exceptions.
-   [CameraManager](../interface-cameramanager/document.md) class, which provides the capabilities of obtaining camera device objects, creating input/output streams and sessions, and registering or unregistering listeners for camera states.
-   [ColorManagement](../interface-colormanagement/document.md) class, which provides the capabilities of checking the support for the color space and setting or querying color space parameters.
-   [ControlCenter](../interface-controlcenter/document.md) class, which provides the capabilities of checking the support for the camera controller and enabling the camera controller.
-   [Flash](../interface-flash/document.md) class, which provides the capabilities of checking the support for flash functionality and manipulating the flash device.
-   [Focus](../interface-focus/document.md) class, which provides the capabilities of checking the support for focus modes on the device and setting focus-related functionalities.
-   [Macro](../interface-macro/document.md) class, which provides the capabilities of checking the support for macro photography and enabling macro photography.
-   [MetadataOutput](../interface-metadataoutput/document.md) class, which provides the capabilities of registering or unregistering listeners for metadata and starting or stopping metadata streams.
-   [Photo](../interface-photo/document.md) class, which is a full-quality image object containing complete information about a photo.
-   [PhotoOutput](../interface-photooutput/document.md) class, which is used in photo sessions to provide photo-related capabilities, such as taking photos, enabling moving-photo capture, and obtaining photo rotation angles.
-   [PhotoSession](../interface-photosession/document.md) class, which is a regular photo mode session class and provides the capabilities for pre-configuration and session state monitoring.
-   [PreviewOutput](../interface-previewoutput/document.md) class, which provides the capabilities of setting the preview stream frame rate and preview rotation angle, and querying the current configuration.
-   [SecureSession](../interface-securesession/document.md) class, which is a secure mode session class and provides the capabilities of checking the support for secure mode and listening for session states.
-   [Session](../interface-session/document.md) class, which is the base class for sessions and provides a range of APIs from starting to stopping preview streams.
-   [Stabilization](../interface-stabilization/document.md) class, which provides the capabilities of checking the support for stabilization and obtaining or setting the device's stabilization types.
-   [VideoOutput](../interface-videooutput/document.md) class, which provides the capabilities of starting or stopping video streams, and configuring the frame rate and mirroring of video streams.
-   [VideoSession](../interface-videosession/document.md) class, which is a regular video mode session class and provides the capabilities for pre-configuration and session state monitoring.
-   [WhiteBalance](../interface-whitebalance/document.md) class, which provides the capabilities of checking the support for white balance modes and setting WB-related parameters.
-   [Zoom](../interface-zoom/document.md) class, which provides the capabilities of checking the support for zoom operations and performing zoom operations on the device.
-   [Others](../interfaces-others/document.md): property information of the camera device, including video configuration items, photo output capabilities, and flashlight.
-   [Enums](../enums/document.md): camera-related enums and their meanings, including the camera position, flash mode, and smooth zoom mode.

#### Modules to Import

import { camera } from '@kit.CameraKit';
