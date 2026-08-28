# ArkTS API Error Codes

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2c/v3/0COMaaQBQzett81kG5zszg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062445Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=15427819328D7F8071BB138D6EFBF97494B287DD7736850CC581E463E1548A29)

This section describes only module-specific error codes. For details about universal error codes, please refer to [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

#### 1000500001 Internal Error

#### \[h2\]Algorithm Exception

**Message**

-   Internal error. Failed to encode.
-   Internal error. Failed to decode.
-   Internal error. Failed to decode image.

**Description**

This error code is reported when an algorithm exception occurs.

**Possible causes**

An algorithm exception occurs during barcode image generation or image-based barcode recognition.

**Solution**

Call the barcode image generation or image-based barcode recognition API again.

#### \[h2\]Barcode Image Generation Failed

**Message**

Internal error. Failed to create pixelMap.

**Description**

This error code is reported when the pixelMap fails to be created during barcode image generation.

**Possible causes**

The image creation logic is abnormal.

**Solution**

Call the barcode image generation API again.

#### \[h2\]Failed to Obtain the Image

**Message**

Internal error. Failed to read file.

**Description**

This error code is reported when a file fails to be read.

**Possible causes**

The input URI is invalid.

**Solution**

Check the URI passed.

#### \[h2\]Failed to Obtain the System Context

**Message**

-   Internal error. Get UI content failed.
-   Internal error. Get context failed.

**Description**

This error code is reported when the system context fails to be obtained.

**Possible causes**

The context passed in is incorrect.

**Solution**

Check the context input parameter.

#### \[h2\]Failed to Obtain the Callback

**Message**

Internal error. Get callback failed.

**Description**

This error code is reported when the callback fails to be obtained.

**Possible causes**

The callback passed in is abnormal.

**Solution**

Check the callback input parameter.

#### \[h2\]Incorrect API Call Sequence

**Message**

-   Internal error. This interface must be invoked after the customScan.start interface.
-   Internal error. This interface cannot be used after the camera session is paused.
-   Internal error. ScanOption is null, please call customScan.init first.

**Description**

This error code is reported when the API call sequence is incorrect.

**Possible causes**

APIs are not called in the correct sequence. For example, the **customScan.start** API is called before **customScan.init**.

**Solution**

Adjust the sequence for calling APIs. For example, call the **customScan.init** API first and then the **customScan.start** API.

#### \[h2\]API Call Not Allowed

**Message**

Internal error. The interface can't be used in promise interface.

**Description**

This error code is reported when the API is called using a promise in **customScan.start**.

**Possible causes**

The **customScan.rescan** API is called using a promise in **customScan.start**.

**Solution**

Call the **customScan.rescan** API using a callback in **customScan.start**.

#### \[h2\]Unmatched Resolution

**Message**

Internal error. The width and height of viewControl do not match the width and height supported by the camera.

**Description**

This error code is reported when the aspect ratio of the ViewControl does not match the camera resolution.

**Possible causes**

The aspect ratio of the ViewControl does not match the camera resolution.

**Solution**

Check the aspect ratio of the ViewControl.

#### \[h2\]Camera Error

**Message**

-   Internal error. CustomScan stop session failed.
-   Internal error. Open camera flash failed.
-   Internal error. Close camera flash failed.
-   Internal error. Camera setZoom failed.
-   Internal error. Camera getZoom failed.
-   Internal error. Camera setFocusPoint failed.
-   Internal error. Reset focus mode failed.
-   Internal error. Camera config captureSession failed.
-   Internal error. Camera create cameraManager failed.
-   Internal error. Camera create camera session failed.
-   Internal error. Camera restart camera session failed.
-   Internal error. Camera create preview output failed.

**Description**

This error code is reported when a camera error occurs.

**Possible causes**

-   Failed to pause the camera stream.
-   Failed to turn on the flash light.
-   Failed to turn off the flash light.
-   Failed to set the zoom ratio.
-   Failed to obtain the zoom ratio.
-   Failed to set the focus.
-   Failed to reset the focus mode.
-   Failed to configure the stream for the camera.
-   Failed to create **cameraManager**.
-   Failed to create a session.
-   Failed to restart the camera.
-   Failed to create the camera preview stream.

**Solution**

Create the service again.

#### 1000500002 Scanning Canceled by User

**Message**

The user canceled the barcode scanning.

**Description**

This error code is reported when a user cancels scanning.

**Possible causes**

The user tapped the close button or swiped back to cancel scanning.

**Solution**

This error code is reported in the scenario where [scanBarcode.startScanForResult](../scanbarcode-scanning-barcodes-using-the-default-ui/document.md#section829511911349) is called. Handle the subsequent business process after a user cancels scanning.
