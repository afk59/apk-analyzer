# Enums

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ed/v3/6eB216Y8SXu_hESvyY1D_g/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062427Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=FD9E9935E7B9F846E71886A6C7AFAD7FE71DC8B5FF233CF572A8ABFF4F655854)

The initial APIs of this module are supported since API version 10. Newly added APIs will be marked with a superscript to indicate their earliest API version.

#### CameraPosition

Enumerates the camera positions.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Multimedia.Camera.Core

| Name | Value | Description |
| :-- | :-- | :-- |
| CAMERA\_POSITION\_UNSPECIFIED | 0 | A camera that does not have a fixed orientation relative to the device screen. |
| CAMERA\_POSITION\_BACK | 1 | Rear camera. |
| CAMERA\_POSITION\_FRONT | 2 | Front camera. |
| CAMERA\_POSITION\_FOLD\_INNER(deprecated) | 3 | 
Folded camera.

This API is supported since API version 11 and deprecated since API version 12.

 |

#### CameraType

Enumerates the camera types.

**Atomic service API**: This API can be used in atomic services since API version 19.

**System capability**: SystemCapability.Multimedia.Camera.Core

| Name | Value | Description |
| :-- | :-- | :-- |
| CAMERA\_TYPE\_DEFAULT | 0 | Default camera type. |
| CAMERA\_TYPE\_WIDE\_ANGLE | 1 | Wide camera. |
| CAMERA\_TYPE\_ULTRA\_WIDE | 2 | Ultra-wide camera. |
| CAMERA\_TYPE\_TELEPHOTO | 3 | Telephoto camera. |
| CAMERA\_TYPE\_TRUE\_DEPTH | 4 | Camera with depth of field information. |

#### ConnectionType

Enumerates the camera connection types.

**Atomic service API**: This API can be used in atomic services since API version 19.

**System capability**: SystemCapability.Multimedia.Camera.Core

| Name | Value | Description |
| :-- | :-- | :-- |
| CAMERA\_CONNECTION\_BUILT\_IN | 0 | Built-in camera. |
| CAMERA\_CONNECTION\_USB\_PLUGIN | 1 | Camera connected using USB. |
| CAMERA\_CONNECTION\_REMOTE | 2 | Remote camera. |

#### HostDeviceType15+

Enumerates the remote camera types.

**Atomic service API**: This API can be used in atomic services since API version 19.

**System capability**: SystemCapability.Multimedia.Camera.Core

| Name | Value | Description |
| :-- | :-- | :-- |
| UNKNOWN\_TYPE | 0 | Unknown type. |
| PHONE | 0x0E | Mobile phone. |
| TABLET | 0x11 | Tablet. |

#### CameraStatus

Enumerates the camera statuses.

**Atomic service API**: This API can be used in atomic services since API version 19.

**System capability**: SystemCapability.Multimedia.Camera.Core

| Name | Value | Description |
| :-- | :-- | :-- |
| CAMERA\_STATUS\_APPEAR | 0 | A camera appears. |
| CAMERA\_STATUS\_DISAPPEAR | 1 | The camera disappears. |
| CAMERA\_STATUS\_AVAILABLE | 2 | The camera is available. |
| CAMERA\_STATUS\_UNAVAILABLE | 3 | The camera is unavailable. |

#### FoldStatus12+

Enumerates the fold states available for a fordable device.

**Atomic service API**: This API can be used in atomic services since API version 19.

**System capability**: SystemCapability.Multimedia.Camera.Core

| Name | Value | Description |
| :-- | :-- | :-- |
| NON\_FOLDABLE | 0 | The device is not foldable. |
| EXPANDED | 1 | The device is fully unfolded. |
| FOLDED | 2 | The device is folded. |

#### SceneMode11+

Enumerates the camera scene modes.

**Atomic service API**: This API can be used in atomic services since API version 19.

**System capability**: SystemCapability.Multimedia.Camera.Core

| Name | Value | Description |
| :-- | :-- | :-- |
| NORMAL\_PHOTO | 1 | Normal photo mode. For details, see [PhotoSession](../interface-photosession/document.md). |
| NORMAL\_VIDEO | 2 | Normal record mode. For details, see [VideoSession](../interface-videosession/document.md). |
| SECURE\_PHOTO12+ | 12 | Secure mode. For details, see [SecureSession](../interface-securesession/document.md). |

#### CameraErrorCode

Enumerates the camera error codes,

which are returned when an API call is incorrect or the **on()** API is used to listen for the error status.

**Atomic service API**: This API can be used in atomic services since API version 19.

**System capability**: SystemCapability.Multimedia.Camera.Core

| Name | Value | Description |
| :-- | :-- | :-- |
| INVALID\_ARGUMENT | 7400101 | A parameter is missing or the parameter type is incorrect. |
| OPERATION\_NOT\_ALLOWED | 7400102 | The operation is not allowed. |
| SESSION\_NOT\_CONFIG | 7400103 | The session is not configured. |
| SESSION\_NOT\_RUNNING | 7400104 | The session is not running. |
| SESSION\_CONFIG\_LOCKED | 7400105 | The session configuration is locked. |
| DEVICE\_SETTING\_LOCKED | 7400106 | The device setting is locked. |
| CONFLICT\_CAMERA | 7400107 | The device is already started. |
| DEVICE\_DISABLED | 7400108 | The camera is disabled for security reasons. |
| DEVICE\_PREEMPTED | 7400109 | The camera is preempted. |
| UNRESOLVED\_CONFLICTS\_WITH\_CURRENT\_CONFIGURATIONS12+ | 7400110 | The configuration conflicts with the current configuration. |
| SERVICE\_FATAL\_ERROR | 7400201 | The camera service is abnormal. |

#### TorchMode11+

Enumerates the flashlight modes.

**Atomic service API**: This API can be used in atomic services since API version 19.

**System capability**: SystemCapability.Multimedia.Camera.Core

| Name | Value | Description |
| :-- | :-- | :-- |
| OFF | 0 | The flashlight is off. |
| ON | 1 | The flashlight is on. |
| AUTO | 2 | The system automatically adjusts the flashlight brightness according to the environment. |

#### CameraFormat

Enumerates the camera output formats.

**Atomic service API**: This API can be used in atomic services since API version 19.

**System capability**: SystemCapability.Multimedia.Camera.Core

| Name | Value | Description |
| :-- | :-- | :-- |
| CAMERA\_FORMAT\_RGBA\_8888 | 3 | RGBA\_8888 image. |
| CAMERA\_FORMAT\_YUV\_420\_SP | 1003 | YUV\_420\_SP image, which corresponds to the NV21 image. |
| CAMERA\_FORMAT\_JPEG | 2000 | JPEG image. |
| CAMERA\_FORMAT\_YCBCR\_P01011+ | 2001 | YCBCR\_P010 image. |
| CAMERA\_FORMAT\_YCRCB\_P01011+ | 2002 | YCRCB\_P010 image. |
| CAMERA\_FORMAT\_HEIC13+ | 2003 | HEIF image. |

#### VideoCodecType13+

Enumerates the video codec types.

**Atomic service API**: This API can be used in atomic services since API version 19.

**System capability**: SystemCapability.Multimedia.Camera.Core

| Name | Value | Description |
| :-- | :-- | :-- |
| AVC | 0 | AVC. |
| HEVC | 1 | HEVC. |

#### CameraConcurrentType18+

Enumerates the camera concurrency types.

**Atomic service API**: This API can be used in atomic services since API version 19.

**System capability**: SystemCapability.Multimedia.Camera.Core

| Name | Value | Description |
| :-- | :-- | :-- |
| CAMERA\_LIMITED\_CAPABILITY | 0 | Limited camera concurrency. |
| CAMERA\_FULL\_CAPABILITY | 1 | Full camera concurrency. |

#### ImageRotation

Enumerates the image rotation angles.

**Atomic service API**: This API can be used in atomic services since API version 19.

**System capability**: SystemCapability.Multimedia.Camera.Core

| Name | Value | Description |
| :-- | :-- | :-- |
| ROTATION\_0 | 0 | The image rotates 0 degrees. |
| ROTATION\_90 | 90 | The image rotates 90 degrees. |
| ROTATION\_180 | 180 | The image rotates 180 degrees. |
| ROTATION\_270 | 270 | The image rotates 270 degrees. |

#### QualityLevel

Enumerates the image quality levels.

**Atomic service API**: This API can be used in atomic services since API version 19.

**System capability**: SystemCapability.Multimedia.Camera.Core

| Name | Value | Description |
| :-- | :-- | :-- |
| QUALITY\_LEVEL\_HIGH | 0 | High image quality. |
| QUALITY\_LEVEL\_MEDIUM | 1 | Medium image quality. |
| QUALITY\_LEVEL\_LOW | 2 | Low image quality. |

#### MetadataObjectType

Enumerates the metadata object types.

**Atomic service API**: This API can be used in atomic services since API version 19.

**System capability**: SystemCapability.Multimedia.Camera.Core

| Name | Value | Description |
| :-- | :-- | :-- |
| FACE\_DETECTION | 0 | Metadata object used for face detection. |

#### FlashMode

Enumerates the flash modes.

**Atomic service API**: This API can be used in atomic services since API version 19.

**System capability**: SystemCapability.Multimedia.Camera.Core

| Name | Value | Description |
| :-- | :-- | :-- |
| FLASH\_MODE\_CLOSE | 0 | The flash is off. |
| FLASH\_MODE\_OPEN | 1 | The flash is on. |
| FLASH\_MODE\_AUTO | 2 | The flash mode is auto, indicating that the flash fires automatically depending on the photo capture conditions. |
| FLASH\_MODE\_ALWAYS\_OPEN | 3 | The flash is steady on. |

#### ExposureMode

Enumerates the exposure modes.

**Atomic service API**: This API can be used in atomic services since API version 19.

**System capability**: SystemCapability.Multimedia.Camera.Core

| Name | Value | Description |
| :-- | :-- | :-- |
| EXPOSURE\_MODE\_LOCKED | 0 | 
Exposure locked. The metering point cannot be set.

After this mode is used, the exposure will be locked by default for each photo capture.

 |
| EXPOSURE\_MODE\_AUTO | 1 | 

Auto exposure. The metering point can be set by calling [AutoExposure.setMeteringPoint](../interface-autoexposure/document.md#setmeteringpoint11).

After this mode is used, it takes effect only for the first photo capture.

 |
| EXPOSURE\_MODE\_CONTINUOUS\_AUTO | 2 | 

Continuous auto exposure. The metering point cannot be set.

After this mode is used, the camera system automatically adjusts the exposure based on the environment changes each time.

 |

#### FocusMode

Enumerates the focus modes.

**Atomic service API**: This API can be used in atomic services since API version 19.

**System capability**: SystemCapability.Multimedia.Camera.Core

| Name | Value | Description |
| :-- | :-- | :-- |
| FOCUS\_MODE\_MANUAL | 0 | Manual focus. The focal length of the camera can be manually set to change the focus position. However, the focal point cannot be set. |
| FOCUS\_MODE\_CONTINUOUS\_AUTO | 1 | Continuous auto focus. The focal point cannot be set. |
| FOCUS\_MODE\_AUTO | 2 | Auto focus. The focal point can be set by calling [Focus.setFocusPoint](../interface-focus/document.md#setfocuspoint11), and auto focus is performed once based on the focal point. |
| FOCUS\_MODE\_LOCKED | 3 | Focus locked. The focal point cannot be set. |

#### FocusState

Enumerates the focus states.

**Atomic service API**: This API can be used in atomic services since API version 19.

**System capability**: SystemCapability.Multimedia.Camera.Core

| Name | Value | Description |
| :-- | :-- | :-- |
| FOCUS\_STATE\_SCAN | 0 | Focusing. |
| FOCUS\_STATE\_FOCUSED | 1 | Focused. |
| FOCUS\_STATE\_UNFOCUSED | 2 | Unfocused. |

#### VideoStabilizationMode

Enumerates the video stabilization modes.

**Atomic service API**: This API can be used in atomic services since API version 19.

**System capability**: SystemCapability.Multimedia.Camera.Core

| Name | Value | Description |
| :-- | :-- | :-- |
| OFF | 0 | Video stabilization is disabled. |
| LOW | 1 | The basic video stabilization algorithm is used. |
| MIDDLE | 2 | A video stabilization algorithm with a stabilization effect better than that of the **LOW** type is used. |
| HIGH | 3 | A video stabilization algorithm with a stabilization effect better than that of the **MIDDLE** type is used. |
| AUTO | 4 | The system automatically selects a video stabilization algorithm. |

#### SmoothZoomMode11+

Enumerates the smooth zoom modes.

**Atomic service API**: This API can be used in atomic services since API version 19.

**System capability**: SystemCapability.Multimedia.Camera.Core

| Name | Value | Description |
| :-- | :-- | :-- |
| NORMAL | 0 | Bessel curve mode. |

#### PreconfigType12+

Enumerates the preconfigured resolution types.

**Atomic service API**: This API can be used in atomic services since API version 19.

**System capability**: SystemCapability.Multimedia.Camera.Core

| Name | Value | Description |
| :-- | :-- | :-- |
| PRECONFIG\_720P | 0 | 720p resolution. |
| PRECONFIG\_1080P | 1 | 1080p resolution. |
| PRECONFIG\_4K | 2 | 4K resolution. |
| PRECONFIG\_HIGH\_QUALITY | 3 | High-quality resolution. |

#### PreconfigRatio12+

Enumerates the preconfigured aspect ratios.

**Atomic service API**: This API can be used in atomic services since API version 19.

**System capability**: SystemCapability.Multimedia.Camera.Core

| Name | Value | Description |
| :-- | :-- | :-- |
| PRECONFIG\_RATIO\_1\_1 | 0 | 1:1 aspect ratio. |
| PRECONFIG\_RATIO\_4\_3 | 1 | 4:3 aspect ratio. |
| PRECONFIG\_RATIO\_16\_9 | 2 | 16:9 aspect ratio. |

#### QualityPrioritization14+

Enumerates the priority levels for video recording quality.

**Atomic service API**: This API can be used in atomic services since API version 19.

**System capability**: SystemCapability.Multimedia.Camera.Core

| Name | Value | Description |
| :-- | :-- | :-- |
| HIGH\_QUALITY | 0 | Prioritizes high-quality video recording. |
| POWER\_BALANCE | 1 | Prioritizes video recording quality while balancing power consumption. |

#### WhiteBalanceMode20+

Enumerates the white balance modes.

**Atomic service API**: This API can be used in atomic services since API version 20.

**System capability**: SystemCapability.Multimedia.Camera.Core

| Name | Value | Description |
| :-- | :-- | :-- |
| AUTO | 0 | Automatic. |
| CLOUDY | 1 | Cloudy. |
| INCANDESCENT | 2 | Incandescent light. |
| FLUORESCENT | 3 | Fluorescence light. |
| DAYLIGHT | 4 | Daylight. |
| MANUAL | 5 | Manual. |
| LOCKED | 6 | Locked. |

#### SystemPressureLevel20+

Enumerates the system pressure levels.

**Atomic service API**: This API can be used in atomic services since API version 20.

**System capability**: SystemCapability.Multimedia.Camera.Core

| Name | Value | Description |
| :-- | :-- | :-- |
| SYSTEM\_PRESSURE\_NORMAL | 0 | The system pressure is normal. |
| SYSTEM\_PRESSURE\_MILD | 1 | The system pressure is elevated but not actively managed by the system. |
| SYSTEM\_PRESSURE\_SEVERE | 2 | The system pressure may affect the overall image quality and performance. |
| SYSTEM\_PRESSURE\_CRITICAL | 3 | The system pressure has a significant impact on the image quality and performance. |
| SYSTEM\_PRESSURE\_SHUTDOWN | 4 | The system pressure is too high, causing the system to shut down. |

#### ControlCenterEffectType20+

Enumerates the effect types supported by the camera controller.

**Atomic service API**: This API can be used in atomic services since API version 20.

**System capability**: SystemCapability.Multimedia.Camera.Core

| Name | Value | Description |
| :-- | :-- | :-- |
| BEAUTY | 0 | Beauty effect. |
| PORTRAIT | 1 | Portrait blur effect. |

#### PhotoQualityPrioritization21+

Enumerates the photo quality prioritization strategies.

**Atomic service API**: This API can be used in atomic services since API version 21.

**System capability**: SystemCapability.Multimedia.Camera.Core

| Name | Value | Description |
| :-- | :-- | :-- |
| HIGH\_QUALITY | 0 | Focuses on image quality, which may increase the time required for capturing photos to ensure high-quality output. |
| SPEED | 1 | Focuses on performance, trading off image quality for faster capture times. |
