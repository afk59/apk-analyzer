# oh\_display\_capture.h

#### Overview

The file declares the capability to take screenshots.

**File to include**: <window\_manager/oh\_display\_capture.h>

**Library**: libnative\_display\_manager.so

**System capability**: SystemCapability.WindowManager.WindowManager.Core

**Since**: 14

**Related module**: [OH\_DisplayManager](../../modules/oh-displaymanager/document.md)

#### Summary

#### \[h2\]Function

| Name | Description |
| :-- | :-- |
| [NativeDisplayManager\_ErrorCode OH\_NativeDisplayManager\_CaptureScreenPixelmap(uint32\_t displayId,OH\_PixelmapNative \*\*pixelMap)](#oh_nativedisplaymanager_capturescreenpixelmap) | Takes a screenshot of the entire screen. This function can be used to capture a full-screen screenshot on the specified display. |

#### Function Description

#### \[h2\]OH\_NativeDisplayManager\_CaptureScreenPixelmap()

NativeDisplayManager\_ErrorCode OH\_NativeDisplayManager\_CaptureScreenPixelmap(uint32\_t displayId,OH\_PixelmapNative \*\*pixelMap)

**Description**

Takes a screenshot of the entire screen. This function can be used to capture a full-screen screenshot on the specified display.

**Required permissions**: ohos.permission.CUSTOM\_SCREEN\_CAPTURE

**Since**: 14

**Device behavior differences**: In versions earlier than API version 21, this API can be properly called on 2-in-1 devices and tablets. If it is called on other device types, error code 801 is returned. Starting from API version 21, this API can be properly called on phones, 2-in-1 devices, and tablets. If it is called on other device types, error code 801 is returned.

**Parameters**

| Parameter | Description |
| :-- | :-- |
| uint32\_t displayId | ID of the display. The value must be a non-negative integer. |
| [OH\_PixelmapNative](../../../../../media/image-kit/c-apis/structs/oh-pixelmapnative/document.md) \*\*pixelMap | Double pointer to an OH\_PixelmapNative object, which is the screenshot taken. |

**Return value**

| Type | Description |
| :-- | :-- |
| [NativeDisplayManager\_ErrorCode](../oh-display-info-h/document.md#nativedisplaymanager_errorcode) | Status code defined in [NativeDisplayManager\_ErrorCode](../oh-display-info-h/document.md#nativedisplaymanager_errorcode). |
