# Interfaces (Others)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fe/v3/DlY4irxITYG2OzCfHVXpZw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062427Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=60D61E0BE35EB37C45561B579793CEF5F9D8144027022FDE181AFEC68005D410)

The initial APIs of this module are supported since API version 10. Newly added APIs will be marked with a superscript to indicate their earliest API version.

#### CameraDevice

Describes the camera device information.

**Atomic service API**: This API can be used in atomic services since API version 19.

**System capability**: SystemCapability.Multimedia.Camera.Core

| Name | Type | Read-only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| cameraId | string | Yes | No | Camera ID. |
| cameraPosition | [CameraPosition](../enums/document.md#cameraposition) | Yes | No | Camera position. |
| cameraType | [CameraType](../enums/document.md#cameratype) | Yes | No | Camera type. |
| connectionType | [ConnectionType](../enums/document.md#connectiontype) | Yes | No | Camera connection type. |
| cameraOrientation12+ | number | Yes | No | Camera installation angle, which does not change as the screen rotates. The value range is \[0, 360\], in degrees. |
| hostDeviceName15+ | string | Yes | No | Remote device name. If no remote device is available, null is returned. |
| hostDeviceType15+ | [HostDeviceType](../enums/document.md#hostdevicetype15) | Yes | No | Remote device type. |

#### CameraStatusInfo

Describes the camera status information.

**Atomic service API**: This API can be used in atomic services since API version 19.

**System capability**: SystemCapability.Multimedia.Camera.Core

| Name | Type | Read-only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| camera | [CameraDevice](#cameradevice) | No | No | Camera device. |
| status | [CameraStatus](../enums/document.md#camerastatus) | No | No | Camera status. |

#### FoldStatusInfo12+

Describes the fold state information about a foldable device.

**Atomic service API**: This API can be used in atomic services since API version 19.

**System capability**: SystemCapability.Multimedia.Camera.Core

| Name | Type | Read-only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| supportedCameras | [Array<CameraDevice>](#cameradevice) | Yes | No | List of cameras supported in the current fold state. |
| foldStatus | [FoldStatus](../enums/document.md#foldstatus12) | Yes | No | Fold state. |

#### Profile

Describes the camera profile.

**Atomic service API**: This API can be used in atomic services since API version 19.

**System capability**: SystemCapability.Multimedia.Camera.Core

| Name | Type | Read-only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| format | [CameraFormat](../enums/document.md#cameraformat) | Yes | No | Output format. |
| size | [Size](#size) | Yes | No | 
Resolution.

The size setting corresponds to the camera's resolution width and height, rather than the actual dimensions of the output image.

 |

#### FrameRateRange

Describes the frame rate range.

**Atomic service API**: This API can be used in atomic services since API version 19.

**System capability**: SystemCapability.Multimedia.Camera.Core

| Name | Type | Read-only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| min | number | Yes | No | Minimum frame rate, in fps. |
| max | number | Yes | No | Maximum frame rate, in fps. |

#### VideoProfile

Describes the video configuration information. It inherits from [Profile](#profile).

**Atomic service API**: This API can be used in atomic services since API version 19.

**System capability**: SystemCapability.Multimedia.Camera.Core

| Name | Type | Read-only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| frameRateRange | [FrameRateRange](#frameraterange) | Yes | No | Frame rate range, in units of frames per second (FPS). |

#### CameraOutputCapability

Describes the camera output capability.

**Atomic service API**: This API can be used in atomic services since API version 19.

**System capability**: SystemCapability.Multimedia.Camera.Core

| Name | Type | Read-only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| previewProfiles | Array<[Profile](#profile)\> | Yes | No | Supported preview profiles. |
| photoProfiles | Array<[Profile](#profile)\> | Yes | No | Supported photo profiles. |
| videoProfiles | Array<[VideoProfile](#videoprofile)\> | Yes | No | Supported video profiles. |
| supportedMetadataObjectTypes | Array<[MetadataObjectType](../enums/document.md#metadataobjecttype)\> | Yes | No | Supported metadata object types. |

#### TorchStatusInfo11+

Describes the flashlight status information.

**Atomic service API**: This API can be used in atomic services since API version 19.

**System capability**: SystemCapability.Multimedia.Camera.Core

| Name | Type | Read-only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| isTorchAvailable | boolean | Yes | No | Whether the flashlight is available. **true** if available, **false** otherwise. |
| isTorchActive | boolean | Yes | No | Whether the flashlight is activated. **true** if activated, **false** otherwise. |
| torchLevel | number | Yes | No | Flashlight brightness level. The value range is \[0, 1\]. A larger value indicates a greater luminance. |

#### Size

Describes the image dimensions.

**Atomic service API**: This API can be used in atomic services since API version 19.

**System capability**: SystemCapability.Multimedia.Camera.Core

| Name | Type | Read-only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| height | number | No | No | Image height, in pixels. |
| width | number | No | No | Image width, in pixels. |

#### Point

Describes the point coordinates, which are used for focus and exposure configuration.

**Atomic service API**: This API can be used in atomic services since API version 19.

**System capability**: SystemCapability.Multimedia.Camera.Core

| Name | Type | Read-only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| x | number | No | No | X coordinate of a point. |
| y | number | No | No | Y coordinate of a point. |

#### CameraConcurrentInfo18+

Describes the camera's concurrency information.

**Atomic service API**: This API can be used in atomic services since API version 19.

**System capability**: SystemCapability.Multimedia.Camera.Core

| Name | Type | Read-only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| device | [CameraDevice](#cameradevice) | Yes | No | Concurrent camera device. |
| type | [CameraConcurrentType](../enums/document.md#cameraconcurrenttype18) | Yes | No | Concurrency type. |
| modes | Array<[SceneMode](../enums/document.md#scenemode11) > | Yes | No | Scene mode. |
| outputCapabilities | Array<[CameraOutputCapability](#cameraoutputcapability) > | Yes | No | Output capabilities of the camera. |

#### Location

Describes the geolocation information.

**Atomic service API**: This API can be used in atomic services since API version 19.

**System capability**: SystemCapability.Multimedia.Camera.Core

| Name | Type | Read-only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| latitude | number | No | No | Latitude, in degrees, within the range \[-90, 90\]. |
| longitude | number | No | No | Longitude, in degrees, within the range \[-180, 180\]. |
| altitude | number | No | No | Altitude, in meters. |

#### PhotoCaptureSetting

Describes the settings for taking an image.

**Atomic service API**: This API can be used in atomic services since API version 19.

**System capability**: SystemCapability.Multimedia.Camera.Core

| Name | Type | Read-only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| quality | [QualityLevel](../enums/document.md#qualitylevel) | No | Yes | Image quality (low by default). |
| rotation | [ImageRotation](../enums/document.md#imagerotation) | No | Yes | Rotation angle of the image. The default value is **0**, indicating clockwise rotation. |
| location | [Location](#location) | No | Yes | Geolocation information of the image (depending on the device hardware information by default). |
| mirror | boolean | No | Yes | Whether mirror photography is enabled (disabled by default). Before using this enumerated value, call [isMirrorSupported](../interface-photooutput/document.md#ismirrorsupported) to check whether mirror photography is supported. **true** if enabled, **false** otherwise. |

#### FrameShutterInfo

Describes the frame shutter information.

**Atomic service API**: This API can be used in atomic services since API version 19.

**System capability**: SystemCapability.Multimedia.Camera.Core

| Name | Type | Read-only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| captureId | number | No | No | ID of this capture action. |
| timestamp | number | No | No | Timestamp of the shutter, in milliseconds. |

#### FrameShutterEndInfo12+

Describes the frame shutter end information during capture.

**Atomic service API**: This API can be used in atomic services since API version 19.

**System capability**: SystemCapability.Multimedia.Camera.Core

| Name | Type | Read-only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| captureId | number | No | No | ID of this capture action. |

#### CaptureStartInfo11+

Describes the capture start information.

**Atomic service API**: This API can be used in atomic services since API version 19.

**System capability**: SystemCapability.Multimedia.Camera.Core

| Name | Type | Read-only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| captureId | number | No | No | ID of this capture action. |
| time | number | No | No | Estimated duration when the sensor captures frames at the bottom layer in a single capture. If **–1** is reported, there is no estimated duration. |

#### CaptureEndInfo

Describes the capture end information.

**Atomic service API**: This API can be used in atomic services since API version 19.

**System capability**: SystemCapability.Multimedia.Camera.Core

| Name | Type | Read-only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| captureId | number | No | No | ID of this capture action. |
| frameCount | number | No | No | Number of frames captured. |

#### AutoDeviceSwitchStatus13+

Describes the information about the automatic camera switch status.

**Atomic service API**: This API can be used in atomic services since API version 19.

**System capability**: SystemCapability.Multimedia.Camera.Core

| Name | Type | Read-only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| isDeviceSwitched | boolean | Yes | No | Whether the camera is automatically switched. **true** if auto-switched, **false** otherwise. |
| isDeviceCapabilityChanged | boolean | Yes | No | Whether the camera capability is changed after the camera is automatically switched. **true** if changed, **false** otherwise. |

#### Rect

Describes a rectangle. The coordinate system for the returned detection points is based on the landscape device orientation, with the charging port on the right. In this coordinate system, the top-left corner is (0, 0), and the bottom-right corner is (1, 1). Here, **topLeftX** and **topLeftY** represent the coordinates of the top-left corner of the rectangle, whereas **width** and **height** represent the width and height of the rectangle, respectively. When cropping or selecting a face region based on specific requirements, the x and y coordinates of the rectangle must be multiplied by the width and height of the actual camera preview output stream to obtain the cropped face region.

The width and height of the actual preview stream refer to the resolution of the camera output stream. For details, see **size** in [profile](#profile).

For details about how to obtain the preview stream data, see [Dual-Channel Preview (ArkTS)](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/camera-dual-channel-preview).

**Atomic service API**: This API can be used in atomic services since API version 19.

**System capability**: SystemCapability.Multimedia.Camera.Core

| Name | Type | Read-only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| topLeftX | number | No | No | X coordinate of the top-left corner of the rectangle, in the range of \[0, 1\]. |
| topLeftY | number | No | No | Y coordinate of the top-left corner of the rectangle, in the range of \[0, 1\]. |
| width | number | No | No | Width of the rectangle, in the range of \[0, 1\]. |
| height | number | No | No | Height of the rectangle, in the range of \[0, 1\]. |

#### MetadataObject

Describes the camera metadata, which is the data source of [CameraInput](../interface-camerainput/document.md). The metadata is obtained through **metadataOutput.on('metadataObjectsAvailable')**.

**Atomic service API**: This API can be used in atomic services since API version 19.

**System capability**: SystemCapability.Multimedia.Camera.Core

| Name | Type | Read-only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| type | [MetadataObjectType](../enums/document.md#metadataobjecttype) | Yes | No | Metadata object type. |
| timestamp | number | Yes | No | Current timestamp, in nanoseconds (ns). |
| boundingBox | [Rect](#rect) | Yes | No | Metadata rectangle. |

#### SmoothZoomInfo11+

Describes the smooth zoom information.

**Atomic service API**: This API can be used in atomic services since API version 19.

**System capability**: SystemCapability.Multimedia.Camera.Core

| Name | Type | Read-only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| duration | number | No | No | Total duration of smooth zoom, in ms. |

#### ControlCenterStatusInfo20+

Describes the effect status information of a camera controller.

**Atomic service API**: This API can be used in atomic services since API version 20.

**System capability**: SystemCapability.Multimedia.Camera.Core

| Name | Type | Read-only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| effectType | [ControlCenterEffectType](../enums/document.md#controlcentereffecttype20) | Yes | No | Effect type of the camera controller. |
| isActive | boolean | Yes | No | Whether the camera controller is activated. **true** if activated, **false** otherwise. |

#### IsoInfo22+

Describes the information about the sensitivity (ISO) settings.

**Atomic service API**: This API can be used in atomic services since API version 22.

**System capability**: SystemCapability.Multimedia.Camera.Core

| Name | Type | Read-only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| iso | number | Yes | Yes | ISO. |
