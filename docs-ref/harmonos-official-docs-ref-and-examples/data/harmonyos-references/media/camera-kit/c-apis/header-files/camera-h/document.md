# camera.h

#### Overview

Defines the basic APIs of the camera.

**File to include**: <ohcamera/camera.h>

**Library**: libohcamera.so

**System capability**: SystemCapability.Multimedia.Camera.Core

**Since**: 11

**Related module**: [OH\_Camera](../../modules/oh-camera/document.md)

#### Summary

#### \[h2\]Structs

| Name | typedef Keyword | Description |
| :-- | :-- | :-- |
| [Camera\_Size](../../structs/camera-size/document.md) | Camera\_Size | Describes the parameters related to the size. |
| [Camera\_Profile](../../structs/camera-profile/document.md) | Camera\_Profile | Describes the profile of a camera stream. |
| [Camera\_FrameRateRange](../../structs/camera-frameraterange/document.md) | Camera\_FrameRateRange | Describes the frame rate range. |
| [Camera\_VideoProfile](../../structs/camera-videoprofile/document.md) | Camera\_VideoProfile | Describes the video profile. |
| [Camera\_OutputCapability](../../structs/camera-outputcapability/document.md) | Camera\_OutputCapability | Describes the camera output capability. |
| [Camera\_Device](../../structs/camera-device/document.md) | Camera\_Device | Describes the camera device. |
| [Camera\_StatusInfo](../../structs/camera-statusinfo/document.md) | Camera\_StatusInfo | Describes the camera status information. |
| [Camera\_Point](../../structs/camera-point/document.md) | Camera\_Point | Describes the parameters related to a point. |
| [Camera\_Location](../../structs/camera-location/document.md) | Camera\_Location | Describes the location where the photo is taken. |
| [Camera\_PhotoCaptureSetting](../../structs/camera-photocapturesetting/document.md) | Camera\_PhotoCaptureSetting | Describes the parameters related to photo capture. |
| [Camera\_FrameShutterInfo](../../structs/camera-frameshutterinfo/document.md) | Camera\_FrameShutterInfo | Describes the frame shutter information. |
| [Camera\_CaptureEndInfo](../../structs/camera-captureendinfo/document.md) | Camera\_CaptureEndInfo | Describes the capture end information. |
| [Camera\_Rect](../../structs/camera-rect/document.md) | Camera\_Rect | 
Defines the rectangle.

The detection point must be in the coordinate system (0-1), where the top-left corner is (0, 0) and the bottom-right corner is (1, 1).

The coordinate system is based on the horizontal device direction with the device's charging port on the right.

If the layout of the preview screen of an application is based on the vertical direction with the charging port on the lower side, the layout width and height are {w, h}, and the returned point is {x, y}, then the coordinate point after conversion is (1-y, x).

 |
| [Camera\_MetadataObject](../../structs/camera-metadataobject/document.md) | Camera\_MetadataObject | Describes the camera metadata. |
| [Camera\_TorchStatusInfo](../../structs/camera-torchstatusinfo/document.md) | Camera\_TorchStatusInfo | Describes the flashlight status information. |
| [Camera\_SmoothZoomInfo](../../structs/camera-smoothzoominfo/document.md) | Camera\_SmoothZoomInfo | Describes the smooth zoom information. |
| [Camera\_CaptureStartInfo](../../structs/camera-capturestartinfo/document.md) | Camera\_CaptureStartInfo | Describes the capture start information. |
| [Camera\_FrameShutterEndInfo](../../structs/camera-frameshutterendinfo/document.md) | Camera\_FrameShutterEndInfo | Describes the frame shutter end information during capture. |
| [Camera\_FoldStatusInfo](../../structs/camera-foldstatusinfo/document.md) | Camera\_FoldStatusInfo | Describes the fold status information of the camera. |
| [Camera\_AutoDeviceSwitchStatusInfo](../../structs/camera-autodeviceswitchstatusinfo/document.md) | Camera\_AutoDeviceSwitchStatusInfo | Describes the automatic device switching status information. |
| [Camera\_ConcurrentInfo](../../structs/camera-concurrentinfo/document.md) | Camera\_ConcurrentInfo | Describes the camera's concurrency information. |
| [Camera\_ControlCenterStatusInfo](../../structs/camera-controlcenterstatusinfo/document.md) | Camera\_ControlCenterStatusInfo | Describes the effect status information of a camera controller. |
| [Camera\_Manager](../../structs/camera-manager/document.md) | Camera\_Manager | 

Describes the camera manager.

You can call [OH\_Camera\_GetCameraManager](#oh_camera_getcameramanager) to create such an object.

 |

#### \[h2\]Enums

| Name | typedef Keyword | Description |
| :-- | :-- | :-- |
| [Camera\_ErrorCode](#camera_errorcode) | Camera\_ErrorCode | Enumerates the camera error codes. |
| [Camera\_Status](#camera_status) | Camera\_Status | Enumerates the camera statuses. |
| [Camera\_SceneMode](#camera_scenemode) | Camera\_SceneMode | Enumerates the camera scene modes. |
| [Camera\_Position](#camera_position) | Camera\_Position | Enumerates the camera positions. |
| [Camera\_Type](#camera_type) | Camera\_Type | Enumerates the camera types. |
| [Camera\_Connection](#camera_connection) | Camera\_Connection | Enumerates the camera connection types. |
| [Camera\_Format](#camera_format) | Camera\_Format | Enumerates the camera output formats. |
| [Camera\_FlashMode](#camera_flashmode) | Camera\_FlashMode | Enumerates the flash modes. |
| [Camera\_ExposureMode](#camera_exposuremode) | Camera\_ExposureMode | Enumerates the exposure modes. |
| [Camera\_FocusMode](#camera_focusmode) | Camera\_FocusMode | Enumerates the focus modes. |
| [Camera\_FocusState](#camera_focusstate) | Camera\_FocusState | Enumerates the focus states. |
| [Camera\_VideoStabilizationMode](#camera_videostabilizationmode) | Camera\_VideoStabilizationMode | Enumerates the video stabilization modes. |
| [Camera\_ImageRotation](#camera_imagerotation) | Camera\_ImageRotation | Enumerates the image rotation angles. |
| [Camera\_QualityLevel](#camera_qualitylevel) | Camera\_QualityLevel | Enumerates the image quality levels. |
| [Camera\_MetadataObjectType](#camera_metadataobjecttype) | Camera\_MetadataObjectType | Enumerates the metadata object types. |
| [Camera\_TorchMode](#camera_torchmode) | Camera\_TorchMode | Enumerates the flashlight modes. |
| [Camera\_SmoothZoomMode](#camera_smoothzoommode) | Camera\_SmoothZoomMode | Enumerates the smooth zoom modes. |
| [Camera\_SystemPressureLevel](#camera_systempressurelevel) | Camera\_SystemPressureLevel | Enumerates the system pressure levels. |
| [Camera\_PreconfigType](#camera_preconfigtype) | Camera\_PreconfigType | Enumerates the preconfigured photo resolution types. |
| [Camera\_PreconfigRatio](#camera_preconfigratio) | Camera\_PreconfigRatio | Enumerates the preconfigured photo aspect ratios. |
| [Camera\_HostDeviceType](#camera_hostdevicetype) | Camera\_HostDeviceType | Enumerates the remote device types. |
| [Camera\_FoldStatus](#camera_foldstatus) | Camera\_FoldStatus | Enumerates the fold statuses. |
| [Camera\_QualityPrioritization](#camera_qualityprioritization) | Camera\_QualityPrioritization | Enumerates the priority levels for video recording quality. |
| [Camera\_ConcurrentType](#camera_concurrenttype) | Camera\_ConcurrentType | Enumerates the camera's concurrency types. |
| [Camera\_WhiteBalanceMode](#camera_whitebalancemode) | Camera\_WhiteBalanceMode | Enumerates the white balance modes. |
| [Camera\_ControlCenterEffectType](#camera_controlcentereffecttype) | Camera\_ControlCenterEffectType | Enumerates the effect types of a camera controller. |
| [Camera\_PhotoQualityPrioritization](#camera_photoqualityprioritization) | Camera\_PhotoQualityPrioritization | Enumerates the photo quality prioritization strategies. |

#### \[h2\]Functions

| Name | Description |
| :-- | :-- |
| [Camera\_ErrorCode OH\_Camera\_GetCameraManager(Camera\_Manager\*\* cameraManager)](#oh_camera_getcameramanager) | Obtains a Camera\_Manager instance. |
| [Camera\_ErrorCode OH\_Camera\_DeleteCameraManager(Camera\_Manager\* cameraManager)](#oh_camera_deletecameramanager) | Deletes a Camera\_Manager instance. |

#### Enum Description

#### \[h2\]Camera\_ErrorCode

enum Camera\_ErrorCode

**Description**

Enumerates the camera error codes.

**Since**: 11

| Enum Item | Description |
| :-- | :-- |
| CAMERA\_OK = 0 | The camera is normal. |
| CAMERA\_INVALID\_ARGUMENT = 7400101 | A parameter is missing or the parameter type is incorrect. |
| CAMERA\_OPERATION\_NOT\_ALLOWED = 7400102 | The operation is not allowed. |
| CAMERA\_SESSION\_NOT\_CONFIG = 7400103 | The session is not configured. |
| CAMERA\_SESSION\_NOT\_RUNNING = 7400104 | The session is not running. |
| CAMERA\_SESSION\_CONFIG\_LOCKED = 7400105 | The session configuration is locked. |
| CAMERA\_DEVICE\_SETTING\_LOCKED = 7400106 | The device setting is locked. |
| CAMERA\_CONFLICT\_CAMERA = 7400107 | The device is already started. |
| CAMERA\_DEVICE\_DISABLED = 7400108 | The camera is disabled for security reasons. |
| CAMERA\_DEVICE\_PREEMPTED = 7400109 | The camera is preempted. |
| CAMERA\_UNRESOLVED\_CONFLICTS\_WITH\_CURRENT\_CONFIGURATIONS = 7400110 | 
The configuration conflicts with the current configuration.

**Since**: 12

 |
| CAMERA\_SERVICE\_FATAL\_ERROR = 7400201 | 

A fatal error occurs in the camera service,

for example, no camera permission, camera service restart, or abnormal cross-process invocation.

 |

#### \[h2\]Camera\_Status

enum Camera\_Status

**Description**

Enumerates the camera statuses.

**Since**: 11

| Enum Item | Description |
| :-- | :-- |
| CAMERA\_STATUS\_APPEAR = 0 | A camera appears. |
| CAMERA\_STATUS\_DISAPPEAR = 1 | The camera disappears. |
| CAMERA\_STATUS\_AVAILABLE = 2 | The camera is available. |
| CAMERA\_STATUS\_UNAVAILABLE = 3 | The camera is unavailable. |

#### \[h2\]Camera\_SceneMode

enum Camera\_SceneMode

**Description**

Enumerates the camera scene modes.

**Since**: 12

| Enum Item | Description |
| :-- | :-- |
| NORMAL\_PHOTO = 1 | Normal photo mode. |
| NORMAL\_VIDEO = 2 | Normal video mode. |
| SECURE\_PHOTO = 12 | Secure mode, which is mainly provided for high-security applications like banking that require features such as biometric verification. The secure mode requires the encryption algorithm framework and trusted application services. For details, see [Device Certificate Kit](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/device-certificate-kit-intro). |

#### \[h2\]Camera\_Position

enum Camera\_Position

**Description**

Enumerates the camera positions.

**Since**: 11

| Enum Item | Description |
| :-- | :-- |
| CAMERA\_POSITION\_UNSPECIFIED = 0 | A camera that does not have a fixed orientation relative to the device screen. |
| CAMERA\_POSITION\_BACK = 1 | Rear camera. |
| CAMERA\_POSITION\_FRONT = 2 | Front camera. |

#### \[h2\]Camera\_Type

enum Camera\_Type

**Description**

Enumerates the camera types.

**Since**: 11

| Enum Item | Description |
| :-- | :-- |
| CAMERA\_TYPE\_DEFAULT = 0 | Default camera type. |
| CAMERA\_TYPE\_WIDE\_ANGLE = 1 | Wide camera. |
| CAMERA\_TYPE\_ULTRA\_WIDE = 2 | Ultra-wide camera. |
| CAMERA\_TYPE\_TELEPHOTO = 3 | Telephoto camera. |
| CAMERA\_TYPE\_TRUE\_DEPTH = 4 | Camera with depth of field information. |

#### \[h2\]Camera\_Connection

enum Camera\_Connection

**Description**

Enumerates the camera connection types.

**Since**: 11

| Enum Item | Description |
| :-- | :-- |
| CAMERA\_CONNECTION\_BUILT\_IN = 0 | Built-in camera. |
| CAMERA\_CONNECTION\_USB\_PLUGIN = 1 | Camera connected using USB. |
| CAMERA\_CONNECTION\_REMOTE = 2 | Remote camera. |

#### \[h2\]Camera\_Format

enum Camera\_Format

**Description**

Enumerates the camera output formats.

**Since**: 11

| Enum Item | Description |
| :-- | :-- |
| CAMERA\_FORMAT\_RGBA\_8888 = 3 | RGBA 8888. |
| CAMERA\_FORMAT\_YUV\_420\_SP = 1003 | YUV 420 SP. |
| CAMERA\_FORMAT\_JPEG = 2000 | JPEG. |
| CAMERA\_FORMAT\_YCBCR\_P010 = 2001 | 
YCBCR P010.

**Since**: 12

 |
| CAMERA\_FORMAT\_YCRCB\_P010 = 2002 | 

YCRCB P010.

**Since**: 12

 |

#### \[h2\]Camera\_FlashMode

enum Camera\_FlashMode

**Description**

Enumerates the flash modes.

**Since**: 11

| Enum Item | Description |
| :-- | :-- |
| FLASH\_MODE\_CLOSE = 0 | The flash is off. |
| FLASH\_MODE\_OPEN = 1 | The flash is on. |
| FLASH\_MODE\_AUTO = 2 | The flash is auto. |
| FLASH\_MODE\_ALWAYS\_OPEN = 3 | The flash is steady on. |

#### \[h2\]Camera\_ExposureMode

enum Camera\_ExposureMode

**Description**

Enumerates the exposure modes.

**Since**: 11

| Enum Item | Description |
| :-- | :-- |
| EXPOSURE\_MODE\_LOCKED = 0 | 
Exposure locked. The metering point cannot be set.

After this mode is used, the exposure will be locked by default for each photo capture.

 |
| EXPOSURE\_MODE\_AUTO = 1 | 

Auto exposure. The metering point can be set by calling [OH\_CaptureSession\_SetMeteringPoint](../capture-session-h/document.md#oh_capturesession_setmeteringpoint).

After this mode is used, it takes effect only for the first photo capture.

 |
| EXPOSURE\_MODE\_CONTINUOUS\_AUTO = 2 | 

Continuous auto exposure.

After this mode is used, the camera system automatically adjusts the exposure based on the environment changes each time.

 |

#### \[h2\]Camera\_FocusMode

enum Camera\_FocusMode

**Description**

Enumerates the focus modes.

**Since**: 11

| Enum Item | Description |
| :-- | :-- |
| FOCUS\_MODE\_MANUAL = 0 | Manual focus. |
| FOCUS\_MODE\_CONTINUOUS\_AUTO = 1 | Continuous auto focus. |
| FOCUS\_MODE\_AUTO = 2 | Auto focus. |
| FOCUS\_MODE\_LOCKED = 3 | Focus locked. |

#### \[h2\]Camera\_FocusState

enum Camera\_FocusState

**Description**

Enumerates the focus states.

**Since**: 11

| Enum Item | Description |
| :-- | :-- |
| FOCUS\_STATE\_SCAN = 0 | Focusing. |
| FOCUS\_STATE\_FOCUSED = 1 | Focused. |
| FOCUS\_STATE\_UNFOCUSED = 2 | Unfocused. |

#### \[h2\]Camera\_VideoStabilizationMode

enum Camera\_VideoStabilizationMode

**Description**

Enumerates the video stabilization modes.

**Since**: 11

| Enum Item | Description |
| :-- | :-- |
| STABILIZATION\_MODE\_OFF = 0 | Video stabilization is disabled. |
| STABILIZATION\_MODE\_LOW = 1 | The basic video stabilization algorithm is used. |
| STABILIZATION\_MODE\_MIDDLE = 2 | A video stabilization algorithm with a stabilization effect better than that of the **LOW** type is used. |
| STABILIZATION\_MODE\_HIGH = 3 | A video stabilization algorithm with a stabilization effect better than that of the **MIDDLE** type is used. |
| STABILIZATION\_MODE\_AUTO = 4 | Automatic video stabilization is used. This value is available for HDF cameras. |

#### \[h2\]Camera\_ImageRotation

enum Camera\_ImageRotation

**Description**

Enumerates the image rotation angles.

**Since**: 11

| Enum Item | Description |
| :-- | :-- |
| IAMGE\_ROTATION\_0 = 0 | The image rotates 0 degrees. |
| IAMGE\_ROTATION\_90 = 90 | The image rotates 90 degrees. |
| IAMGE\_ROTATION\_180 = 180 | The image rotates 180 degrees. |
| IAMGE\_ROTATION\_270 = 270 | The image rotates 270 degrees. |

#### \[h2\]Camera\_QualityLevel

enum Camera\_QualityLevel

**Description**

Enumerates the image quality levels.

**Since**: 11

| Enum Item | Description |
| :-- | :-- |
| QUALITY\_LEVEL\_HIGH = 0 | High image quality. |
| QUALITY\_LEVEL\_MEDIUM = 1 | Medium image quality. |
| QUALITY\_LEVEL\_LOW = 2 | Low image quality. |

#### \[h2\]Camera\_MetadataObjectType

enum Camera\_MetadataObjectType

**Description**

Enumerates the metadata object types.

**Since**: 11

| Enum Item | Description |
| :-- | :-- |
| FACE\_DETECTION = 0 | Metadata object used for face detection. |

#### \[h2\]Camera\_TorchMode

enum Camera\_TorchMode

**Description**

Enumerates the flashlight modes.

**Since**: 12

| Enum Item | Description |
| :-- | :-- |
| OFF = 0 | The flashlight is always off. |
| ON = 1 | The flashlight is always on. |
| AUTO = 2 | The flashlight will be turned on automatically based on the ambient lighting level. |

#### \[h2\]Camera\_SmoothZoomMode

enum Camera\_SmoothZoomMode

**Description**

Enumerates the smooth zoom modes.

**Since**: 12

| Enum Item | Description |
| :-- | :-- |
| NORMAL = 0 | Bessel curve mode. |

#### \[h2\]Camera\_SystemPressureLevel

enum Camera\_SystemPressureLevel

**Description**

Enumerates the system pressure levels.

**Since**: 20

| Enum Item | Description |
| :-- | :-- |
| SYSTEM\_PRESSURE\_NORMAL = 0 | The system pressure is normal. |
| SYSTEM\_PRESSURE\_MILD = 1 | The system pressure is elevated but not actively managed by the system. |
| SYSTEM\_PRESSURE\_SEVERE = 2 | The system pressure may affect the overall image quality and performance. |
| SYSTEM\_PRESSURE\_CRITICAL = 3 | The system pressure has a significant impact on the image quality and performance. |
| SYSTEM\_PRESSURE\_SHUTDOWN = 4 | The system pressure is too high, causing the system to shut down. |

#### \[h2\]Camera\_PreconfigType

enum Camera\_PreconfigType

**Description**

Enumerates the preconfigured photo resolution types.

**Since**: 12

| Enum Item | Description |
| :-- | :-- |
| PRECONFIG\_720P = 0 | 720p resolution. |
| PRECONFIG\_1080P = 1 | 1080p resolution. |
| PRECONFIG\_4K = 2 | 4K resolution. |
| PRECONFIG\_HIGH\_QUALITY = 3 | High-quality photos. |

#### \[h2\]Camera\_PreconfigRatio

enum Camera\_PreconfigRatio

**Description**

Enumerates the preconfigured photo aspect ratios.

**Since**: 12

| Enum Item | Description |
| :-- | :-- |
| PRECONFIG\_RATIO\_1\_1 = 0 | 1:1 aspect ratio. |
| PRECONFIG\_RATIO\_4\_3 = 1 | 4:3 aspect ratio. |
| PRECONFIG\_RATIO\_16\_9 = 2 | 16:9 aspect ratio. |

#### \[h2\]Camera\_HostDeviceType

enum Camera\_HostDeviceType

**Description**

Enumerates the remote device types.

**Since**: 15

| Enum Item | Description |
| :-- | :-- |
| HOST\_DEVICE\_TYPE\_UNKNOWN\_TYPE = 0 | Unknown type. |
| HOST\_DEVICE\_TYPE\_PHONE = 0x0E | Mobile phone. |
| HOST\_DEVICE\_TYPE\_TABLET = 0x11 | Tablet. |

#### \[h2\]Camera\_FoldStatus

enum Camera\_FoldStatus

**Description**

Enumerates the fold statuses.

**Since**: 13

| Enum Item | Description |
| :-- | :-- |
| NON\_FOLDABLE = 0 | Unfoldable. |
| EXPANDED = 1 | Unfolded. |
| FOLDED = 2 | Folded. |

#### \[h2\]Camera\_QualityPrioritization

enum Camera\_QualityPrioritization

**Description**

Enumerates the priority levels for video recording quality.

**Since**: 14

| Enum Item | Description |
| :-- | :-- |
| HIGH\_QUALITY = 0 | Prioritizes high-quality video recording. |
| POWER\_BALANCE = 1 | Prioritizes video recording quality while balancing power consumption. |

#### \[h2\]Camera\_ConcurrentType

enum Camera\_ConcurrentType

**Description**

Enumerates the camera's concurrency types.

**Since**: 18

| Enum Item | Description |
| :-- | :-- |
| CAMERA\_CONCURRENT\_TYPE\_LIMITED\_CAPABILITY = 0 | Limited camera concurrency. |
| CAMERA\_CONCURRENT\_TYPE\_FULL\_CAPABILITY = 1 | Full camera concurrency. |

#### \[h2\]Camera\_WhiteBalanceMode

enum Camera\_WhiteBalanceMode

**Description**

Enumerates the white balance modes.

**Since**: 20

| Enum Item | Description |
| :-- | :-- |
| CAMERA\_WHITE\_BALANCE\_MODE\_AUTO = 0 | Automatic. |
| CAMERA\_WHITE\_BALANCE\_MODE\_CLOUDY = 1 | Cloudy. |
| CAMERA\_WHITE\_BALANCE\_MODE\_INCANDESCENT = 2 | Incandescent light. |
| CAMERA\_WHITE\_BALANCE\_MODE\_FLUORESCENT = 3 | Fluorescence light. |
| CAMERA\_WHITE\_BALANCE\_MODE\_DAYLIGHT = 4 | Daylight. |
| CAMERA\_WHITE\_BALANCE\_MODE\_MANUAL = 5 | Manual. |
| CAMERA\_WHITE\_BALANCE\_MODE\_LOCKED = 6 | Locked. |

#### \[h2\]Camera\_ControlCenterEffectType

enum Camera\_ControlCenterEffectType

**Description**

Enumerates the effect types of a camera controller.

**Since**: 20

| Enum Item | Description |
| :-- | :-- |
| CONTROL\_CENTER\_EFFECT\_TYPE\_BEAUTY = 0 | Beauty effect. |
| CONTROL\_CENTER\_EFFECT\_TYPE\_PORTRAIT = 1 | Portrait blur effect. |

#### \[h2\]Camera\_PhotoQualityPrioritization

enum Camera\_PhotoQualityPrioritization

**Description**

Enumerates the photo quality prioritization strategies.

**Since**: 21

| Enum Item | Description |
| :-- | :-- |
| CAMERA\_PHOTO\_QUALITY\_PRIORITIZATION\_HIGH\_QUALITY = 0 | Focuses on image quality, which may increase the time required for capturing photos to ensure high-quality output. |
| CAMERA\_PHOTO\_QUALITY\_PRIORITIZATION\_SPEED = 1 | Focuses on performance, trading off image quality for faster capture times. |

#### Function Description

#### \[h2\]OH\_Camera\_GetCameraManager()

Camera\_ErrorCode OH\_Camera\_GetCameraManager(Camera\_Manager\*\* cameraManager)

**Description**

Obtains a Camera\_Manager instance.

**Since**: 11

**Parameters**

| Name | Description |
| :-- | :-- |
| [Camera\_Manager](../../structs/camera-manager/document.md)\*\* cameraManager | Double pointer to the Camera\_Manager instance created, if the function is successfully called. |

**Returns**

| Type | Description |
| :-- | :-- |
| [Camera\_ErrorCode](#camera_errorcode) | 
**CAMERA\_OK**: The operation is successful.

**CAMERA\_INVALID\_ARGUMENT**: A parameter is missing or the parameter type is incorrect.

**CAMERA\_SERVICE\_FATAL\_ERROR**: The camera service is abnormal.

 |

#### \[h2\]OH\_Camera\_DeleteCameraManager()

Camera\_ErrorCode OH\_Camera\_DeleteCameraManager(Camera\_Manager\* cameraManager)

**Description**

Deletes a Camera\_Manager instance.

**Since**: 11

**Parameters**

| Name | Description |
| :-- | :-- |
| [Camera\_Manager](../../structs/camera-manager/document.md)\* cameraManager | Pointer to the target Camera\_Manager instance. |

**Returns**

| Type | Description |
| :-- | :-- |
| [Camera\_ErrorCode](#camera_errorcode) | 
**CAMERA\_OK**: The operation is successful.

**CAMERA\_INVALID\_ARGUMENT**: A parameter is missing or the parameter type is incorrect.

**CAMERA\_SERVICE\_FATAL\_ERROR**: The camera service is abnormal.

 |
