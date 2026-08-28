# capture\_session.h

#### Overview

The file declares the capture session concepts.

**File to include**: <ohcamera/capture\_session.h>

**Library**: libohcamera.so

**System capability**: SystemCapability.Multimedia.Camera.Core

**Since**: 11

**Related module**: [OH\_Camera](../../modules/oh-camera/document.md)

#### Summary

#### \[h2\]Structs

| Name | typedef Keyword | Description |
| :-- | :-- | :-- |
| [CaptureSession\_Callbacks](../../structs/capturesession-callbacks/document.md) | CaptureSession\_Callbacks | Describes the callbacks used for a capture session. |
| [Camera\_CaptureSession](../../structs/camera-capturesession/document.md) | Camera\_CaptureSession | 
Describes the capture session object.

You can use [OH\_CameraManager\_CreateCaptureSession](../camera-manager-h/document.md#oh_cameramanager_createcapturesession) to create such an object.

 |

#### \[h2\]Functions

| Name | typedef Keyword | Description |
| :-- | :-- | :-- |
| [typedef void (\*OH\_CaptureSession\_OnFocusStateChange)(Camera\_CaptureSession\* session, Camera\_FocusState focusState)](#oh_capturesession_onfocusstatechange) | OH\_CaptureSession\_OnFocusStateChange | Defines the callback defined in the [CaptureSession\_Callbacks](../../structs/capturesession-callbacks/document.md) struct and used to report focus status changes of a capture session. |
| [typedef void (\*OH\_CaptureSession\_OnError)(Camera\_CaptureSession\* session, Camera\_ErrorCode errorCode)](#oh_capturesession_onerror) | OH\_CaptureSession\_OnError | Defines the callback defined in the [CaptureSession\_Callbacks](../../structs/capturesession-callbacks/document.md) struct and used to report capture session errors. |
| [typedef void (\*OH\_CaptureSession\_OnSmoothZoomInfo)(Camera\_CaptureSession\* session, Camera\_SmoothZoomInfo\* smoothZoomInfo)](#oh_capturesession_onsmoothzoominfo) | OH\_CaptureSession\_OnSmoothZoomInfo | Defines the callback invoked when smooth zoom is triggered for a capture session. |
| [typedef void (\*OH\_CaptureSession\_OnAutoDeviceSwitchStatusChange)(Camera\_CaptureSession\* session, Camera\_AutoDeviceSwitchStatusInfo\* autoDeviceSwitchStatusInfo)](#oh_capturesession_onautodeviceswitchstatuschange) | OH\_CaptureSession\_OnAutoDeviceSwitchStatusChange | Defines the callback used to listen for device switching events. |
| [typedef void (\*OH\_CaptureSession\_OnSystemPressureLevelChange)(Camera\_CaptureSession\* session, Camera\_SystemPressureLevel systemPressureLevel)](#oh_capturesession_onsystempressurelevelchange) | OH\_CaptureSession\_OnSystemPressureLevelChange | Defines the callback used to listen for capture system pressure level changes. |
| [typedef void (\*OH\_CaptureSession\_OnControlCenterEffectStatusChange)(Camera\_CaptureSession\* session, Camera\_ControlCenterStatusInfo\* controlCenterStatusInfo)](#oh_capturesession_oncontrolcentereffectstatuschange) | OH\_CaptureSession\_OnControlCenterEffectStatusChange | Defines the callback used to listen for effect status changes of a camera controller. |
| [Camera\_ErrorCode OH\_CaptureSession\_RegisterCallback(Camera\_CaptureSession\* session, CaptureSession\_Callbacks\* callback)](#oh_capturesession_registercallback) | \- | Registers a callback to listen for capture session events. |
| [Camera\_ErrorCode OH\_CaptureSession\_UnregisterCallback(Camera\_CaptureSession\* session, CaptureSession\_Callbacks\* callback)](#oh_capturesession_unregistercallback) | \- | Unregisters the callback used to listen for capture session events. |
| [Camera\_ErrorCode OH\_CaptureSession\_RegisterSmoothZoomInfoCallback(Camera\_CaptureSession\* session, OH\_CaptureSession\_OnSmoothZoomInfo smoothZoomInfoCallback)](#oh_capturesession_registersmoothzoominfocallback) | \- | Registers a callback to listen for smooth zoom events. |
| [Camera\_ErrorCode OH\_CaptureSession\_UnregisterSmoothZoomInfoCallback(Camera\_CaptureSession\* session, OH\_CaptureSession\_OnSmoothZoomInfo smoothZoomInfoCallback)](#oh_capturesession_unregistersmoothzoominfocallback) | \- | Unregisters the callback used to listen for smooth zoom events. |
| [Camera\_ErrorCode OH\_CaptureSession\_SetSessionMode(Camera\_CaptureSession\* session, Camera\_SceneMode sceneMode)](#oh_capturesession_setsessionmode) | \- | 
Sets a session mode.

This API cannot be called after [OH\_CaptureSession\_BeginConfig](#oh_capturesession_beginconfig).

You are advised to call this function immediately after [OH\_CameraManager\_CreateCaptureSession](../camera-manager-h/document.md#oh_cameramanager_createcapturesession).

 |
| [Camera\_ErrorCode OH\_CaptureSession\_AddSecureOutput(Camera\_CaptureSession\* session, Camera\_PreviewOutput\* previewOutput)](#oh_capturesession_addsecureoutput) | \- | Marks a preview output stream as secure output. |
| [Camera\_ErrorCode OH\_CaptureSession\_BeginConfig(Camera\_CaptureSession\* session)](#oh_capturesession_beginconfig) | \- | Starts the configuration for a capture session. |
| [Camera\_ErrorCode OH\_CaptureSession\_CommitConfig(Camera\_CaptureSession\* session)](#oh_capturesession_commitconfig) | \- | Commits the configuration for a capture session. |
| [Camera\_ErrorCode OH\_CaptureSession\_AddInput(Camera\_CaptureSession\* session, Camera\_Input\* cameraInput)](#oh_capturesession_addinput) | \- | Adds a Camera\_Input instance to a session. |
| [Camera\_ErrorCode OH\_CaptureSession\_RemoveInput(Camera\_CaptureSession\* session, Camera\_Input\* cameraInput)](#oh_capturesession_removeinput) | \- | Removes a Camera\_Input instance from a session. |
| [Camera\_ErrorCode OH\_CaptureSession\_AddPreviewOutput(Camera\_CaptureSession\* session, Camera\_PreviewOutput\* previewOutput)](#oh_capturesession_addpreviewoutput) | \- | Adds a PreviewOutput instance to a session. |
| [Camera\_ErrorCode OH\_CaptureSession\_RemovePreviewOutput(Camera\_CaptureSession\* session, Camera\_PreviewOutput\* previewOutput)](#oh_capturesession_removepreviewoutput) | \- | Removes a PreviewOutput instance from a session. |
| [Camera\_ErrorCode OH\_CaptureSession\_AddPhotoOutput(Camera\_CaptureSession\* session, Camera\_PhotoOutput\* photoOutput)](#oh_capturesession_addphotooutput) | \- | Adds a PhotoOutput instance to a session. |
| [Camera\_ErrorCode OH\_CaptureSession\_RemovePhotoOutput(Camera\_CaptureSession\* session, Camera\_PhotoOutput\* photoOutput)](#oh_capturesession_removephotooutput) | \- | Removes a PhotoOutput instance from a session. |
| [Camera\_ErrorCode OH\_CaptureSession\_AddVideoOutput(Camera\_CaptureSession\* session, Camera\_VideoOutput\* videoOutput)](#oh_capturesession_addvideooutput) | \- | Adds a VideoOutput instance to a session. |
| [Camera\_ErrorCode OH\_CaptureSession\_RemoveVideoOutput(Camera\_CaptureSession\* session, Camera\_VideoOutput\* videoOutput)](#oh_capturesession_removevideooutput) | \- | Removes a VideoOutput instance from a session. |
| [Camera\_ErrorCode OH\_CaptureSession\_AddMetadataOutput(Camera\_CaptureSession\* session, Camera\_MetadataOutput\* metadataOutput)](#oh_capturesession_addmetadataoutput) | \- | Adds a MetadataOutput instance to a session. |
| [Camera\_ErrorCode OH\_CaptureSession\_RemoveMetadataOutput(Camera\_CaptureSession\* session, Camera\_MetadataOutput\* metadataOutput)](#oh_capturesession_removemetadataoutput) | \- | Removes a MetadataOutput instance from a session. |
| [Camera\_ErrorCode OH\_CaptureSession\_Start(Camera\_CaptureSession\* session)](#oh_capturesession_start) | \- | Starts a capture session. |
| [Camera\_ErrorCode OH\_CaptureSession\_Stop(Camera\_CaptureSession\* session)](#oh_capturesession_stop) | \- | Stops a capture session. |
| [Camera\_ErrorCode OH\_CaptureSession\_Release(Camera\_CaptureSession\* session)](#oh_capturesession_release) | \- | Releases a CaptureSession instance. |
| [Camera\_ErrorCode OH\_CaptureSession\_HasFlash(Camera\_CaptureSession\* session, bool\* hasFlash)](#oh_capturesession_hasflash) | \- | Checks whether the device has flash. |
| [Camera\_ErrorCode OH\_CaptureSession\_IsFlashModeSupported(Camera\_CaptureSession\* session, Camera\_FlashMode flashMode, bool\* isSupported)](#oh_capturesession_isflashmodesupported) | \- | Checks whether a flash mode is supported. |
| [Camera\_ErrorCode OH\_CaptureSession\_GetFlashMode(Camera\_CaptureSession\* session, Camera\_FlashMode\* flashMode)](#oh_capturesession_getflashmode) | \- | Obtains the flash mode in use. |
| [Camera\_ErrorCode OH\_CaptureSession\_SetFlashMode(Camera\_CaptureSession\* session, Camera\_FlashMode flashMode)](#oh_capturesession_setflashmode) | \- | Sets a flash mode for the device. |
| [Camera\_ErrorCode OH\_CaptureSession\_IsExposureModeSupported(Camera\_CaptureSession\* session, Camera\_ExposureMode exposureMode, bool\* isSupported)](#oh_capturesession_isexposuremodesupported) | \- | Checks whether an exposure mode is supported. |
| [Camera\_ErrorCode OH\_CaptureSession\_GetExposureMode(Camera\_CaptureSession\* session, Camera\_ExposureMode\* exposureMode)](#oh_capturesession_getexposuremode) | \- | Obtains the exposure mode in use. |
| [Camera\_ErrorCode OH\_CaptureSession\_SetExposureMode(Camera\_CaptureSession\* session, Camera\_ExposureMode exposureMode)](#oh_capturesession_setexposuremode) | \- | Sets an exposure mode for the device. |
| [Camera\_ErrorCode OH\_CaptureSession\_GetMeteringPoint(Camera\_CaptureSession\* session, Camera\_Point\* point)](#oh_capturesession_getmeteringpoint) | \- | Obtains the metering point in use. |
| [Camera\_ErrorCode OH\_CaptureSession\_SetMeteringPoint(Camera\_CaptureSession\* session, Camera\_Point point)](#oh_capturesession_setmeteringpoint) | \- | Sets the metering point, which is the center point of the metering rectangle. |
| [Camera\_ErrorCode OH\_CaptureSession\_GetExposureBiasRange(Camera\_CaptureSession\* session, float\* minExposureBias, float\* maxExposureBias, float\* step)](#oh_capturesession_getexposurebiasrange) | \- | Obtains the exposure compensation values of the device. |
| [Camera\_ErrorCode OH\_CaptureSession\_SetExposureBias(Camera\_CaptureSession\* session, float exposureBias)](#oh_capturesession_setexposurebias) | \- | Sets an exposure compensation value for the device. |
| [Camera\_ErrorCode OH\_CaptureSession\_GetExposureBias(Camera\_CaptureSession\* session, float\* exposureBias)](#oh_capturesession_getexposurebias) | \- | Obtains the exposure compensation value in use. |
| [Camera\_ErrorCode OH\_CaptureSession\_IsFocusModeSupported(Camera\_CaptureSession\* session, Camera\_FocusMode focusMode, bool\* isSupported)](#oh_capturesession_isfocusmodesupported) | \- | Checks whether a focus mode is supported. |
| [Camera\_ErrorCode OH\_CaptureSession\_GetFocusMode(Camera\_CaptureSession\* session, Camera\_FocusMode\* focusMode)](#oh_capturesession_getfocusmode) | \- | Obtains the focus mode in use. |
| [Camera\_ErrorCode OH\_CaptureSession\_SetFocusMode(Camera\_CaptureSession\* session, Camera\_FocusMode focusMode)](#oh_capturesession_setfocusmode) | \- | Sets a focus mode for the device. |
| [Camera\_ErrorCode OH\_CaptureSession\_GetFocusPoint(Camera\_CaptureSession\* session, Camera\_Point\* focusPoint)](#oh_capturesession_getfocuspoint) | \- | Obtains the focal point in use. |
| [Camera\_ErrorCode OH\_CaptureSession\_SetFocusPoint(Camera\_CaptureSession\* session, Camera\_Point focusPoint)](#oh_capturesession_setfocuspoint) | \- | Sets a focal point for the device. |
| [Camera\_ErrorCode OH\_CaptureSession\_GetZoomRatioRange(Camera\_CaptureSession\* session, float\* minZoom, float\* maxZoom)](#oh_capturesession_getzoomratiorange) | \- | Obtains the supported zoom ratio range. |
| [Camera\_ErrorCode OH\_CaptureSession\_GetZoomRatio(Camera\_CaptureSession\* session, float\* zoom)](#oh_capturesession_getzoomratio) | \- | Obtains the zoom ratio in use. |
| [Camera\_ErrorCode OH\_CaptureSession\_SetZoomRatio(Camera\_CaptureSession\* session, float zoom)](#oh_capturesession_setzoomratio) | \- | Sets a zoom ratio for the device. |
| [Camera\_ErrorCode OH\_CaptureSession\_IsVideoStabilizationModeSupported(Camera\_CaptureSession\* session, Camera\_VideoStabilizationMode mode, bool\* isSupported)](#oh_capturesession_isvideostabilizationmodesupported) | \- | Checks whether a video stabilization mode is supported. |
| [Camera\_ErrorCode OH\_CaptureSession\_GetVideoStabilizationMode(Camera\_CaptureSession\* session, Camera\_VideoStabilizationMode\* mode)](#oh_capturesession_getvideostabilizationmode) | \- | Obtains the video stabilization mode in use. |
| [Camera\_ErrorCode OH\_CaptureSession\_SetVideoStabilizationMode(Camera\_CaptureSession\* session, Camera\_VideoStabilizationMode mode)](#oh_capturesession_setvideostabilizationmode) | \- | Sets a video stabilization mode for the device. |
| [Camera\_ErrorCode OH\_CaptureSession\_CanAddInput(Camera\_CaptureSession\* session, Camera\_Input\* cameraInput, bool\* isSuccessful)](#oh_capturesession_canaddinput) | \- | Checks whether a Camera\_Input instance can be added to a session. |
| [Camera\_ErrorCode OH\_CaptureSession\_CanAddPreviewOutput(Camera\_CaptureSession\* session, Camera\_PreviewOutput\* cameraOutput, bool\* isSuccessful)](#oh_capturesession_canaddpreviewoutput) | \- | Checks whether a PreviewOutput instance can be added to a session. |
| [Camera\_ErrorCode OH\_CaptureSession\_CanAddPhotoOutput(Camera\_CaptureSession\* session, Camera\_PhotoOutput\* cameraOutput, bool\* isSuccessful)](#oh_capturesession_canaddphotooutput) | \- | Checks whether a PhotoOutput instance can be added to a session. |
| [Camera\_ErrorCode OH\_CaptureSession\_CanAddVideoOutput(Camera\_CaptureSession\* session, Camera\_VideoOutput\* cameraOutput, bool\* isSuccessful)](#oh_capturesession_canaddvideooutput) | \- | Checks whether a VideoOutput instance can be added to a session. |
| [Camera\_ErrorCode OH\_CaptureSession\_CanPreconfig(Camera\_CaptureSession\* session, Camera\_PreconfigType preconfigType, bool\* canPreconfig)](#oh_capturesession_canpreconfig) | \- | Checks whether a preconfigured resolution type is supported. |
| [Camera\_ErrorCode OH\_CaptureSession\_CanPreconfigWithRatio(Camera\_CaptureSession\* session, Camera\_PreconfigType preconfigType, Camera\_PreconfigRatio preconfigRatio, bool\* canPreconfig)](#oh_capturesession_canpreconfigwithratio) | \- | Checks whether a preconfigured resolution type with an aspect ratio is supported. |
| [Camera\_ErrorCode OH\_CaptureSession\_Preconfig(Camera\_CaptureSession\* session, Camera\_PreconfigType preconfigType)](#oh_capturesession_preconfig) | \- | Sets a preconfigured resolution type. |
| [Camera\_ErrorCode OH\_CaptureSession\_PreconfigWithRatio(Camera\_CaptureSession\* session, Camera\_PreconfigType preconfigType, Camera\_PreconfigRatio preconfigRatio)](#oh_capturesession_preconfigwithratio) | \- | Sets a preconfigured resolution type with an aspect ratio. |
| [Camera\_ErrorCode OH\_CaptureSession\_GetExposureValue(Camera\_CaptureSession\* session, float\* exposureValue)](#oh_capturesession_getexposurevalue) | \- | Obtains the exposure value. |
| [Camera\_ErrorCode OH\_CaptureSession\_GetFocalLength(Camera\_CaptureSession\* session, float\* focalLength)](#oh_capturesession_getfocallength) | \- | Obtains the current focal length. |
| [Camera\_ErrorCode OH\_CaptureSession\_SetSmoothZoom(Camera\_CaptureSession\* session, float targetZoom, Camera\_SmoothZoomMode smoothZoomMode)](#oh_capturesession_setsmoothzoom) | \- | Sets smooth zoom. |
| [Camera\_ErrorCode OH\_CaptureSession\_GetSupportedColorSpaces(Camera\_CaptureSession\* session, OH\_NativeBuffer\_ColorSpace\*\* colorSpace, uint32\_t\* size)](#oh_capturesession_getsupportedcolorspaces) | \- | Obtains the supported color spaces. |
| [Camera\_ErrorCode OH\_CaptureSession\_DeleteColorSpaces(Camera\_CaptureSession\* session, OH\_NativeBuffer\_ColorSpace\* colorSpace)](#oh_capturesession_deletecolorspaces) | \- | Deletes color spaces. |
| [Camera\_ErrorCode OH\_CaptureSession\_GetActiveColorSpace(Camera\_CaptureSession\* session, OH\_NativeBuffer\_ColorSpace\* colorSpace)](#oh_capturesession_getactivecolorspace) | \- | Obtains the active color space. |
| [Camera\_ErrorCode OH\_CaptureSession\_SetActiveColorSpace(Camera\_CaptureSession\* session, OH\_NativeBuffer\_ColorSpace colorSpace)](#oh_capturesession_setactivecolorspace) | \- | Sets the active color space. |
| [Camera\_ErrorCode OH\_CaptureSession\_RegisterAutoDeviceSwitchStatusCallback(Camera\_CaptureSession\* session, OH\_CaptureSession\_OnAutoDeviceSwitchStatusChange autoDeviceSwitchStatusChange)](#oh_capturesession_registerautodeviceswitchstatuscallback) | \- | Registers a callback to listen for device switching changes. |
| [Camera\_ErrorCode OH\_CaptureSession\_UnregisterAutoDeviceSwitchStatusCallback(Camera\_CaptureSession\* session, OH\_CaptureSession\_OnAutoDeviceSwitchStatusChange autoDeviceSwitchStatusChange)](#oh_capturesession_unregisterautodeviceswitchstatuscallback) | \- | Unregisters the callback used to listen for device switching changes. |
| [Camera\_ErrorCode OH\_CaptureSession\_IsAutoDeviceSwitchSupported(Camera\_CaptureSession\* session, bool\* isSupported)](#oh_capturesession_isautodeviceswitchsupported) | \- | Checks whether automatic device switching is supported. |
| [Camera\_ErrorCode OH\_CaptureSession\_EnableAutoDeviceSwitch(Camera\_CaptureSession\* session, bool enabled)](#oh_capturesession_enableautodeviceswitch) | \- | Enables or disables automatic device switching. |
| [Camera\_ErrorCode OH\_CaptureSession\_RegisterSystemPressureLevelChangeCallback(Camera\_CaptureSession\* session, OH\_CaptureSession\_OnSystemPressureLevelChange systemPressureLevelChange)](#oh_capturesession_registersystempressurelevelchangecallback) | \- | Registers a callback to listen for capture system pressure level changes. |
| [Camera\_ErrorCode OH\_CaptureSession\_UnregisterSystemPressureLevelChangeCallback(Camera\_CaptureSession\* session, OH\_CaptureSession\_OnSystemPressureLevelChange systemPressureLevelChange)](#oh_capturesession_unregistersystempressurelevelchangecallback) | \- | Unregisters the callback used to listen for capture system pressure level changes. |
| [Camera\_ErrorCode OH\_CaptureSession\_SetQualityPrioritization(Camera\_CaptureSession\* session, Camera\_QualityPrioritization qualityPrioritization)](#oh_capturesession_setqualityprioritization) | \- | 

Sets the priority level for video recording quality.

The default value is **HIGH\_QUALITY**. Switching to **POWER\_BALANCE** will compromise video recording quality to achieve lower power usage. The extent of power conservation achieved varies depending on the platform. It is recommended that this API be called between [OH\_CaptureSession\_CommitConfig](#oh_capturesession_commitconfig) and [OH\_CaptureSession\_Start](#oh_capturesession_start).

 |
| [Camera\_ErrorCode OH\_CaptureSession\_IsMacroSupported(Camera\_CaptureSession\* session, bool\* isSupported)](#oh_capturesession_ismacrosupported) | \- | Checks whether macro photography is supported. |
| [Camera\_ErrorCode OH\_CaptureSession\_EnableMacro(Camera\_CaptureSession\* session, bool enabled)](#oh_capturesession_enablemacro) | \- | Enables or disables macro photography for the camera device. |
| [Camera\_ErrorCode OH\_CaptureSession\_SetWhiteBalance(Camera\_CaptureSession\* session, int32\_t colorTemperature)](#oh_capturesession_setwhitebalance) | \- | 

Sets the white balance color temperature.

Before setting this parameter, you are advised to use [OH\_CaptureSession\_GetWhiteBalanceRange](#oh_capturesession_getwhitebalancerange) to obtain the supported white balance color temperature range.

 |
| [Camera\_ErrorCode OH\_CaptureSession\_GetWhiteBalance(Camera\_CaptureSession\* session, int32\_t \*colorTemperature)](#oh_capturesession_getwhitebalance) | \- | Obtains the white balance color temperature. |
| [Camera\_ErrorCode OH\_CaptureSession\_GetWhiteBalanceMode(Camera\_CaptureSession\* session, Camera\_WhiteBalanceMode\* whiteBalanceMode)](#oh_capturesession_getwhitebalancemode) | \- | Obtains the white balance mode in use. |
| [Camera\_ErrorCode OH\_CaptureSession\_IsWhiteBalanceModeSupported(Camera\_CaptureSession\* session, Camera\_WhiteBalanceMode whiteBalanceMode, bool\* isSupported)](#oh_capturesession_iswhitebalancemodesupported) | \- | Checks whether the specified white balance mode is supported. |
| [Camera\_ErrorCode OH\_CaptureSession\_SetWhiteBalanceMode(Camera\_CaptureSession\* session, Camera\_WhiteBalanceMode whiteBalanceMode)](#oh_capturesession_setwhitebalancemode) | \- | Sets a white balance mode. |
| [Camera\_ErrorCode OH\_CaptureSession\_GetWhiteBalanceRange(Camera\_CaptureSession\* session, int32\_t \*minColorTemperature, int32\_t \*maxColorTemperature)](#oh_capturesession_getwhitebalancerange) | \- | Obtains the supported white balance color temperature range. |
| [Camera\_ErrorCode OH\_CaptureSession\_IsControlCenterSupported(Camera\_CaptureSession\* session, bool\* isSupported)](#oh_capturesession_iscontrolcentersupported) | \- | Checks whether the camera controller is supported. |
| [Camera\_ErrorCode OH\_CaptureSession\_GetSupportedEffectTypes(Camera\_CaptureSession\* session, Camera\_ControlCenterEffectType\*\* types, uint32\_t\* size)](#oh_capturesession_getsupportedeffecttypes) | \- | Obtains the effect types supported by the camera controller. |
| [Camera\_ErrorCode OH\_CaptureSession\_DeleteSupportedEffectTypes(Camera\_CaptureSession\* session, Camera\_ControlCenterEffectType\* types, uint32\_t size)](#oh_capturesession_deletesupportedeffecttypes) | \- | Deletes the effect types supported by the camera controller. |
| [Camera\_ErrorCode OH\_CaptureSession\_EnableControlCenter(Camera\_CaptureSession\* session, bool enabled)](#oh_capturesession_enablecontrolcenter) | \- | Enables or disables the camera controller. |
| [Camera\_ErrorCode OH\_CaptureSession\_RegisterControlCenterEffectStatusChangeCallback(Camera\_CaptureSession\* session, OH\_CaptureSession\_OnControlCenterEffectStatusChange controlCenterEffectStatusChange)](#oh_capturesession_registercontrolcentereffectstatuschangecallback) | \- | Registers a callback to listen for effect status changes of a camera controller. |
| [Camera\_ErrorCode OH\_CaptureSession\_UnregisterControlCenterEffectStatusChangeCallback(Camera\_CaptureSession\* session, OH\_CaptureSession\_OnControlCenterEffectStatusChange controlCenterEffectStatusChange)](#oh_capturesession_unregistercontrolcentereffectstatuschangecallback) | \- | Unregisters the callback used to listen for effect status changes of a camera controller. |
| [typedef void (\*OH\_CaptureSession\_OnMacroStatusChange)(Camera\_CaptureSession\* session, bool isMacroDetected)](#oh_capturesession_onmacrostatuschange) | OH\_CaptureSession\_OnMacroStatusChange | Defines the callback used to listen for macro status changes of a camera session. |
| [Camera\_ErrorCode OH\_CaptureSession\_RegisterMacroStatusChangeCallback(Camera\_CaptureSession\* session, OH\_CaptureSession\_OnMacroStatusChange macroStatusChange)](#oh_capturesession_registermacrostatuschangecallback) | \- | Registers a callback to listen for macro status changes of a camera session. |
| [Camera\_ErrorCode OH\_CaptureSession\_UnregisterMacroStatusChangeCallback(Camera\_CaptureSession\* session, OH\_CaptureSession\_OnMacroStatusChange macroStatusChange)](#oh_capturesession_unregistermacrostatuschangecallback) | \- | Unregisters the callback used to listen for macro status changes of a camera session. |
| [typedef void (\*OH\_CaptureSession\_OnIsoChange)(Camera\_CaptureSession\* session, int32\_t isoValue)](#oh_capturesession_onisochange) | OH\_CaptureSession\_OnIsoChange | Defines the callback used to listen for ISO changes in a camera session. |
| [Camera\_ErrorCode OH\_CaptureSession\_RegisterIsoChangeCallback(Camera\_CaptureSession\* session, OH\_CaptureSession\_OnIsoChange isoChange)](#oh_capturesession_registerisochangecallback) | \- | Registers a callback to listen for ISO changes. |
| [Camera\_ErrorCode OH\_CaptureSession\_UnregisterIsoChangeCallback(Camera\_CaptureSession\* session, OH\_CaptureSession\_OnIsoChange isoChange)](#oh_capturesession_unregisterisochangecallback) | \- | Unregisters the callback used to listen for ISO changes. |

#### Function Description

#### \[h2\]OH\_CaptureSession\_OnFocusStateChange()

typedef void (\*OH\_CaptureSession\_OnFocusStateChange)(Camera\_CaptureSession\* session, Camera\_FocusState focusState)

**Description**

Defines the callback defined in the [CaptureSession\_Callbacks](../../structs/capturesession-callbacks/document.md) struct and used to report focus status changes of a capture session.

**Since**: 11

**Parameters**

| Name | Description |
| :-- | :-- |
| [Camera\_CaptureSession](../../structs/camera-capturesession/document.md)\* session | Pointer to the Camera\_CaptureSession instance that transfers the callback. |
| [Camera\_FocusState](../camera-h/document.md#camera_focusstate) focusState | Focus status. |

#### \[h2\]OH\_CaptureSession\_OnError()

typedef void (\*OH\_CaptureSession\_OnError)(Camera\_CaptureSession\* session, Camera\_ErrorCode errorCode)

**Description**

Defines the callback defined in the [CaptureSession\_Callbacks](../../structs/capturesession-callbacks/document.md) struct and used to report capture session errors.

**Since**: 11

**Parameters**

| Name | Description |
| :-- | :-- |
| [Camera\_CaptureSession](../../structs/camera-capturesession/document.md)\* session | Pointer to the Camera\_CaptureSession instance that transfers the callback. |
| [Camera\_ErrorCode](../camera-h/document.md#camera_errorcode) errorCode | Error code reported in a capture session. |

**See also**

[CAMERA\_SERVICE\_FATAL\_ERROR](../camera-h/document.md#camera_errorcode)

#### \[h2\]OH\_CaptureSession\_OnSmoothZoomInfo()

typedef void (\*OH\_CaptureSession\_OnSmoothZoomInfo)(Camera\_CaptureSession\* session,Camera\_SmoothZoomInfo\* smoothZoomInfo)

**Description**

Defines the callback invoked when smooth zoom is triggered for a capture session.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [Camera\_CaptureSession](../../structs/camera-capturesession/document.md)\* session | Pointer to the Camera\_CaptureSession instance that transfers the callback. |
| [Camera\_SmoothZoomInfo](../../structs/camera-smoothzoominfo/document.md)\* smoothZoomInfo | Pointer to the smooth zoom information passed by the callback. |

#### \[h2\]OH\_CaptureSession\_OnAutoDeviceSwitchStatusChange()

typedef void (\*OH\_CaptureSession\_OnAutoDeviceSwitchStatusChange)(Camera\_CaptureSession\* session, Camera\_AutoDeviceSwitchStatusInfo\* autoDeviceSwitchStatusInfo)

**Description**

Defines the callback used to listen for device switching events.

**Since**: 13

**Parameters**

| Name | Description |
| :-- | :-- |
| [Camera\_CaptureSession](../../structs/camera-capturesession/document.md)\* session | Pointer to the Camera\_CaptureSession instance that transfers the callback. |
| [Camera\_AutoDeviceSwitchStatusInfo](../../structs/camera-autodeviceswitchstatusinfo/document.md)\* autoDeviceSwitchStatusInfo | Pointer to the device switching information passed by the callback. |

#### \[h2\]OH\_CaptureSession\_OnSystemPressureLevelChange()

typedef void (\*OH\_CaptureSession\_OnSystemPressureLevelChange)(Camera\_CaptureSession\* session, Camera\_SystemPressureLevel systemPressureLevel)

**Description**

Defines the callback used to listen for capture system pressure level changes.

**Since**: 20

**Parameters**

| Name | Description |
| :-- | :-- |
| [Camera\_CaptureSession](../../structs/camera-capturesession/document.md)\* session | Pointer to the Camera\_CaptureSession instance that transfers the callback. |
| [Camera\_SystemPressureLevel](../camera-h/document.md#camera_systempressurelevel) systemPressureLevel | Pointer to the system pressure level passed by the callback. |

#### \[h2\]OH\_CaptureSession\_OnControlCenterEffectStatusChange()

typedef void (\*OH\_CaptureSession\_OnControlCenterEffectStatusChange)(Camera\_CaptureSession\* session, Camera\_ControlCenterStatusInfo\* controlCenterStatusInfo)

**Description**

Defines the callback used to listen for effect status changes of a camera controller.

**Since**: 20

**Parameters**

| Name | Description |
| :-- | :-- |
| [Camera\_CaptureSession](../../structs/camera-capturesession/document.md)\* session | Pointer to the Camera\_CaptureSession instance that transfers the callback. |
| [Camera\_ControlCenterStatusInfo](../../structs/camera-controlcenterstatusinfo/document.md)\* controlCenterStatusInfo | Pointer to the effect status information passed by the callback. |

#### \[h2\]OH\_CaptureSession\_RegisterCallback()

Camera\_ErrorCode OH\_CaptureSession\_RegisterCallback(Camera\_CaptureSession\* session, CaptureSession\_Callbacks\* callback)

**Description**

Registers a callback to listen for capture session events.

**Since**: 11

**Parameters**

| Name | Description |
| :-- | :-- |
| [Camera\_CaptureSession](../../structs/camera-capturesession/document.md)\* session | Pointer to the Camera\_CaptureSession instance that transfers the callback. |
| [CaptureSession\_Callbacks](../../structs/capturesession-callbacks/document.md)\* callback | Pointer to the target callback. |

**Returns**

| Type | Description |
| :-- | :-- |
| [Camera\_ErrorCode](../camera-h/document.md#camera_errorcode) | 
**CAMERA\_OK**: The operation is successful.

**CAMERA\_INVALID\_ARGUMENT**: A parameter is missing or the parameter type is incorrect.

 |

#### \[h2\]OH\_CaptureSession\_UnregisterCallback()

Camera\_ErrorCode OH\_CaptureSession\_UnregisterCallback(Camera\_CaptureSession\* session, CaptureSession\_Callbacks\* callback)

**Description**

Unregisters the callback used to listen for capture session events.

**Since**: 11

**Parameters**

| Name | Description |
| :-- | :-- |
| [Camera\_CaptureSession](../../structs/camera-capturesession/document.md)\* session | Pointer to the Camera\_CaptureSession instance that transfers the callback. |
| [CaptureSession\_Callbacks](../../structs/capturesession-callbacks/document.md)\* callback | Pointer to the target callback. |

**Returns**

| Type | Description |
| :-- | :-- |
| [Camera\_ErrorCode](../camera-h/document.md#camera_errorcode) | 
**CAMERA\_OK**: The operation is successful.

**CAMERA\_INVALID\_ARGUMENT**: A parameter is missing or the parameter type is incorrect.

 |

#### \[h2\]OH\_CaptureSession\_RegisterSmoothZoomInfoCallback()

Camera\_ErrorCode OH\_CaptureSession\_RegisterSmoothZoomInfoCallback(Camera\_CaptureSession\* session, OH\_CaptureSession\_OnSmoothZoomInfo smoothZoomInfoCallback)

**Description**

Registers a callback to listen for smooth zoom events.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [Camera\_CaptureSession](../../structs/camera-capturesession/document.md)\* session | Pointer to the Camera\_CaptureSession instance that transfers the callback. |
| [OH\_CaptureSession\_OnSmoothZoomInfo](#oh_capturesession_onsmoothzoominfo) smoothZoomInfoCallback | Pointer to the target callback. |

**Returns**

| Type | Description |
| :-- | :-- |
| [Camera\_ErrorCode](../camera-h/document.md#camera_errorcode) | 
**CAMERA\_OK**: The operation is successful.

**CAMERA\_INVALID\_ARGUMENT**: A parameter is missing or the parameter type is incorrect.

 |

#### \[h2\]OH\_CaptureSession\_UnregisterSmoothZoomInfoCallback()

Camera\_ErrorCode OH\_CaptureSession\_UnregisterSmoothZoomInfoCallback(Camera\_CaptureSession\* session, OH\_CaptureSession\_OnSmoothZoomInfo smoothZoomInfoCallback)

**Description**

Unregisters the callback used to listen for smooth zoom events.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [Camera\_CaptureSession](../../structs/camera-capturesession/document.md)\* session | Pointer to the Camera\_CaptureSession instance that transfers the callback. |
| [OH\_CaptureSession\_OnSmoothZoomInfo](#oh_capturesession_onsmoothzoominfo) smoothZoomInfoCallback | Pointer to the target callback. |

**Returns**

| Type | Description |
| :-- | :-- |
| [Camera\_ErrorCode](../camera-h/document.md#camera_errorcode) | 
**CAMERA\_OK**: The operation is successful.

**CAMERA\_INVALID\_ARGUMENT**: A parameter is missing or the parameter type is incorrect.

 |

#### \[h2\]OH\_CaptureSession\_SetSessionMode()

Camera\_ErrorCode OH\_CaptureSession\_SetSessionMode(Camera\_CaptureSession\* session, Camera\_SceneMode sceneMode)

**Description**

Sets a session mode.

This API cannot be called after [OH\_CaptureSession\_BeginConfig](#oh_capturesession_beginconfig).

You are advised to call this function immediately after [OH\_CameraManager\_CreateCaptureSession](../camera-manager-h/document.md#oh_cameramanager_createcapturesession).

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [Camera\_CaptureSession](../../structs/camera-capturesession/document.md)\* session | Pointer to the target Camera\_CaptureSession instance. |
| [Camera\_SceneMode](../camera-h/document.md#camera_scenemode) sceneMode | Scene mode. |

**Returns**

| Type | Description |
| :-- | :-- |
| [Camera\_ErrorCode](../camera-h/document.md#camera_errorcode) | 
**CAMERA\_OK**: The operation is successful.

**CAMERA\_INVALID\_ARGUMENT**: A parameter is missing or the parameter type is incorrect.

**CAMERA\_OPERATION\_NOT\_ALLOWED**: The operation is not allowed.

**CAMERA\_SESSION\_CONFIG\_LOCKED**: The session configuration is locked.

 |

#### \[h2\]OH\_CaptureSession\_AddSecureOutput()

Camera\_ErrorCode OH\_CaptureSession\_AddSecureOutput(Camera\_CaptureSession\* session, Camera\_PreviewOutput\* previewOutput)

**Description**

Marks a preview output stream as secure output.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [Camera\_CaptureSession](../../structs/camera-capturesession/document.md)\* session | Pointer to the target Camera\_CaptureSession instance. |
| [Camera\_PreviewOutput](../../structs/camera-previewoutput/document.md)\* previewOutput | Pointer to the target Camera\_PreviewOutput instance. |

**Returns**

| Type | Description |
| :-- | :-- |
| [Camera\_ErrorCode](../camera-h/document.md#camera_errorcode) | 
**CAMERA\_OK**: The operation is successful.

**CAMERA\_INVALID\_ARGUMENT**: A parameter is missing or the parameter type is incorrect.

**CAMERA\_OPERATION\_NOT\_ALLOWED**: The operation is not allowed.

**CAMERA\_SESSION\_CONFIG\_LOCKED**: The session configuration is locked.

 |

#### \[h2\]OH\_CaptureSession\_BeginConfig()

Camera\_ErrorCode OH\_CaptureSession\_BeginConfig(Camera\_CaptureSession\* session)

**Description**

Starts the configuration for a capture session.

**Since**: 11

**Parameters**

| Name | Description |
| :-- | :-- |
| [Camera\_CaptureSession](../../structs/camera-capturesession/document.md)\* session | Pointer to the target Camera\_CaptureSession instance. |

**Returns**

| Type | Description |
| :-- | :-- |
| [Camera\_ErrorCode](../camera-h/document.md#camera_errorcode) | 
**CAMERA\_OK**: The operation is successful.

**CAMERA\_INVALID\_ARGUMENT**: A parameter is missing or the parameter type is incorrect.

**CAMERA\_SESSION\_CONFIG\_LOCKED**: The session configuration is locked.

 |

#### \[h2\]OH\_CaptureSession\_CommitConfig()

Camera\_ErrorCode OH\_CaptureSession\_CommitConfig(Camera\_CaptureSession\* session)

**Description**

Commits the configuration for a capture session.

**Since**: 11

**Parameters**

| Name | Description |
| :-- | :-- |
| [Camera\_CaptureSession](../../structs/camera-capturesession/document.md)\* session | Pointer to the target Camera\_CaptureSession instance. |

**Returns**

| Type | Description |
| :-- | :-- |
| [Camera\_ErrorCode](../camera-h/document.md#camera_errorcode) | 
**CAMERA\_OK**: The operation is successful.

**CAMERA\_INVALID\_ARGUMENT**: A parameter is missing or the parameter type is incorrect.

**CAMERA\_OPERATION\_NOT\_ALLOWED**: The operation is not allowed.

**CAMERA\_SERVICE\_FATAL\_ERROR**: The camera service is abnormal.

 |

#### \[h2\]OH\_CaptureSession\_AddInput()

Camera\_ErrorCode OH\_CaptureSession\_AddInput(Camera\_CaptureSession\* session, Camera\_Input\* cameraInput)

**Description**

Adds a Camera\_Input instance to a session.

**Since**: 11

**Parameters**

| Name | Description |
| :-- | :-- |
| [Camera\_CaptureSession](../../structs/camera-capturesession/document.md)\* session | Pointer to the target Camera\_CaptureSession instance. |
| [Camera\_Input](../../structs/camera-input/document.md)\* cameraInput | Pointer to the Camera\_Input instance to add. |

**Returns**

| Type | Description |
| :-- | :-- |
| [Camera\_ErrorCode](../camera-h/document.md#camera_errorcode) | 
**CAMERA\_OK**: The operation is successful.

**CAMERA\_INVALID\_ARGUMENT**: A parameter is missing or the parameter type is incorrect.

**CAMERA\_OPERATION\_NOT\_ALLOWED**: The operation is not allowed.

 |

#### \[h2\]OH\_CaptureSession\_RemoveInput()

Camera\_ErrorCode OH\_CaptureSession\_RemoveInput(Camera\_CaptureSession\* session, Camera\_Input\* cameraInput)

**Description**

Removes a Camera\_Input instance from a session.

**Since**: 11

**Parameters**

| Name | Description |
| :-- | :-- |
| [Camera\_CaptureSession](../../structs/camera-capturesession/document.md)\* session | Pointer to the target Camera\_CaptureSession instance. |
| [Camera\_Input](../../structs/camera-input/document.md)\* cameraInput | Pointer to the Camera\_Input instance to remove. |

**Returns**

| Type | Description |
| :-- | :-- |
| [Camera\_ErrorCode](../camera-h/document.md#camera_errorcode) | 
**CAMERA\_OK**: The operation is successful.

**CAMERA\_INVALID\_ARGUMENT**: A parameter is missing or the parameter type is incorrect.

**CAMERA\_OPERATION\_NOT\_ALLOWED**: The operation is not allowed.

 |

#### \[h2\]OH\_CaptureSession\_AddPreviewOutput()

Camera\_ErrorCode OH\_CaptureSession\_AddPreviewOutput(Camera\_CaptureSession\* session, Camera\_PreviewOutput\* previewOutput)

**Description**

Adds a PreviewOutput instance to a session.

**Since**: 11

**Parameters**

| Name | Description |
| :-- | :-- |
| [Camera\_CaptureSession](../../structs/camera-capturesession/document.md)\* session | Pointer to the target Camera\_CaptureSession instance. |
| [Camera\_PreviewOutput](../../structs/camera-previewoutput/document.md)\* previewOutput | Pointer to the PreviewOutput instance to add. |

**Returns**

| Type | Description |
| :-- | :-- |
| [Camera\_ErrorCode](../camera-h/document.md#camera_errorcode) | 
**CAMERA\_OK**: The operation is successful.

**CAMERA\_INVALID\_ARGUMENT**: A parameter is missing or the parameter type is incorrect.

**CAMERA\_OPERATION\_NOT\_ALLOWED**: The operation is not allowed.

 |

#### \[h2\]OH\_CaptureSession\_RemovePreviewOutput()

Camera\_ErrorCode OH\_CaptureSession\_RemovePreviewOutput(Camera\_CaptureSession\* session, Camera\_PreviewOutput\* previewOutput)

**Description**

Removes a PreviewOutput instance from a session.

**Since**: 11

**Parameters**

| Name | Description |
| :-- | :-- |
| [Camera\_CaptureSession](../../structs/camera-capturesession/document.md)\* session | Pointer to the target Camera\_CaptureSession instance. |
| [Camera\_PreviewOutput](../../structs/camera-previewoutput/document.md)\* previewOutput | Pointer to the PreviewOutput instance to remove. |

**Returns**

| Type | Description |
| :-- | :-- |
| [Camera\_ErrorCode](../camera-h/document.md#camera_errorcode) | 
**CAMERA\_OK**: The operation is successful.

**CAMERA\_INVALID\_ARGUMENT**: A parameter is missing or the parameter type is incorrect.

**CAMERA\_OPERATION\_NOT\_ALLOWED**: The operation is not allowed.

 |

#### \[h2\]OH\_CaptureSession\_AddPhotoOutput()

Camera\_ErrorCode OH\_CaptureSession\_AddPhotoOutput(Camera\_CaptureSession\* session, Camera\_PhotoOutput\* photoOutput)

**Description**

Adds a PhotoOutput instance to a session.

**Since**: 11

**Parameters**

| Name | Description |
| :-- | :-- |
| [Camera\_CaptureSession](../../structs/camera-capturesession/document.md)\* session | Pointer to the target Camera\_CaptureSession instance. |
| [Camera\_PhotoOutput](../../structs/camera-photooutput/document.md)\* photoOutput | Pointer to the PhotoOutput instance to add. |

**Returns**

| Type | Description |
| :-- | :-- |
| [Camera\_ErrorCode](../camera-h/document.md#camera_errorcode) | 
**CAMERA\_OK**: The operation is successful.

**CAMERA\_INVALID\_ARGUMENT**: A parameter is missing or the parameter type is incorrect.

**CAMERA\_OPERATION\_NOT\_ALLOWED**: The operation is not allowed.

 |

#### \[h2\]OH\_CaptureSession\_RemovePhotoOutput()

Camera\_ErrorCode OH\_CaptureSession\_RemovePhotoOutput(Camera\_CaptureSession\* session, Camera\_PhotoOutput\* photoOutput)

**Description**

Removes a PhotoOutput instance from a session.

**Since**: 11

**Parameters**

| Name | Description |
| :-- | :-- |
| [Camera\_CaptureSession](../../structs/camera-capturesession/document.md)\* session | Pointer to the target Camera\_CaptureSession instance. |
| [Camera\_PhotoOutput](../../structs/camera-photooutput/document.md)\* photoOutput | Pointer to the PhotoOutput instance to remove. |

**Returns**

| Type | Description |
| :-- | :-- |
| [Camera\_ErrorCode](../camera-h/document.md#camera_errorcode) | 
**CAMERA\_OK**: The operation is successful.

**CAMERA\_INVALID\_ARGUMENT**: A parameter is missing or the parameter type is incorrect.

**CAMERA\_OPERATION\_NOT\_ALLOWED**: The operation is not allowed.

 |

#### \[h2\]OH\_CaptureSession\_AddVideoOutput()

Camera\_ErrorCode OH\_CaptureSession\_AddVideoOutput(Camera\_CaptureSession\* session, Camera\_VideoOutput\* videoOutput)

**Description**

Adds a **VideoOutput** instance to a session.

**Since**: 11

**Parameters**

| Name | Description |
| :-- | :-- |
| [Camera\_CaptureSession](../../structs/camera-capturesession/document.md)\* session | Pointer to the target Camera\_CaptureSession instance. |
| [Camera\_VideoOutput](../../structs/camera-videooutput/document.md)\* videoOutput | Pointer to the **VideoOutput** instance to add. |

**Returns**

| Type | Description |
| :-- | :-- |
| [Camera\_ErrorCode](../camera-h/document.md#camera_errorcode) | 
**CAMERA\_OK**: The operation is successful.

**CAMERA\_INVALID\_ARGUMENT**: A parameter is missing or the parameter type is incorrect.

**CAMERA\_OPERATION\_NOT\_ALLOWED**: The operation is not allowed.

 |

#### \[h2\]OH\_CaptureSession\_RemoveVideoOutput()

Camera\_ErrorCode OH\_CaptureSession\_RemoveVideoOutput(Camera\_CaptureSession\* session, Camera\_VideoOutput\* videoOutput)

**Description**

Removes a VideoOutput instance from a session.

**Since**: 11

**Parameters**

| Name | Description |
| :-- | :-- |
| [Camera\_CaptureSession](../../structs/camera-capturesession/document.md)\* session | Pointer to the target Camera\_CaptureSession instance. |
| [Camera\_VideoOutput](../../structs/camera-videooutput/document.md)\* videoOutput | Pointer to the VideoOutput instance to remove. |

**Returns**

| Type | Description |
| :-- | :-- |
| [Camera\_ErrorCode](../camera-h/document.md#camera_errorcode) | 
**CAMERA\_OK**: The operation is successful.

**CAMERA\_INVALID\_ARGUMENT**: A parameter is missing or the parameter type is incorrect.

**CAMERA\_OPERATION\_NOT\_ALLOWED**: The operation is not allowed.

 |

#### \[h2\]OH\_CaptureSession\_AddMetadataOutput()

Camera\_ErrorCode OH\_CaptureSession\_AddMetadataOutput(Camera\_CaptureSession\* session, Camera\_MetadataOutput\* metadataOutput)

**Description**

Adds a MetadataOutput instance to a session.

**Since**: 11

**Parameters**

| Name | Description |
| :-- | :-- |
| [Camera\_CaptureSession](../../structs/camera-capturesession/document.md)\* session | Pointer to the target Camera\_CaptureSession instance. |
| [Camera\_MetadataOutput](../../structs/camera-metadataoutput/document.md)\* metadataOutput | Pointer to the MetadataOutput instance to add. |

**Returns**

| Type | Description |
| :-- | :-- |
| [Camera\_ErrorCode](../camera-h/document.md#camera_errorcode) | 
**CAMERA\_OK**: The operation is successful.

**CAMERA\_INVALID\_ARGUMENT**: A parameter is missing or the parameter type is incorrect.

**CAMERA\_OPERATION\_NOT\_ALLOWED**: The operation is not allowed.

 |

#### \[h2\]OH\_CaptureSession\_RemoveMetadataOutput()

Camera\_ErrorCode OH\_CaptureSession\_RemoveMetadataOutput(Camera\_CaptureSession\* session, Camera\_MetadataOutput\* metadataOutput)

**Description**

Removes a MetadataOutput instance from a session.

**Since**: 11

**Parameters**

| Name | Description |
| :-- | :-- |
| [Camera\_CaptureSession](../../structs/camera-capturesession/document.md)\* session | Pointer to the target Camera\_CaptureSession instance. |
| [Camera\_MetadataOutput](../../structs/camera-metadataoutput/document.md)\* metadataOutput | Pointer to the MetadataOutput instance to remove. |

**Returns**

| Type | Description |
| :-- | :-- |
| [Camera\_ErrorCode](../camera-h/document.md#camera_errorcode) | 
**CAMERA\_OK**: The operation is successful.

**CAMERA\_INVALID\_ARGUMENT**: A parameter is missing or the parameter type is incorrect.

**CAMERA\_OPERATION\_NOT\_ALLOWED**: The operation is not allowed.

 |

#### \[h2\]OH\_CaptureSession\_Start()

Camera\_ErrorCode OH\_CaptureSession\_Start(Camera\_CaptureSession\* session)

**Description**

Starts a capture session.

**Since**: 11

**Parameters**

| Name | Description |
| :-- | :-- |
| [Camera\_CaptureSession](../../structs/camera-capturesession/document.md)\* session | Pointer to the Camera\_CaptureSession instance to start. |

**Returns**

| Type | Description |
| :-- | :-- |
| [Camera\_ErrorCode](../camera-h/document.md#camera_errorcode) | 
**CAMERA\_OK**: The operation is successful.

**CAMERA\_INVALID\_ARGUMENT**: A parameter is missing or the parameter type is incorrect.

**CAMERA\_SESSION\_NOT\_CONFIG**: The capture session is not configured.

**CAMERA\_SERVICE\_FATAL\_ERROR**: The camera service is abnormal.

 |

#### \[h2\]OH\_CaptureSession\_Stop()

Camera\_ErrorCode OH\_CaptureSession\_Stop(Camera\_CaptureSession\* session)

**Description**

Stops a capture session.

**Since**: 11

**Parameters**

| Name | Description |
| :-- | :-- |
| [Camera\_CaptureSession](../../structs/camera-capturesession/document.md)\* session | Pointer to the Camera\_CaptureSession instance to stop. |

**Returns**

| Type | Description |
| :-- | :-- |
| [Camera\_ErrorCode](../camera-h/document.md#camera_errorcode) | 
**CAMERA\_OK**: The operation is successful.

**CAMERA\_INVALID\_ARGUMENT**: A parameter is missing or the parameter type is incorrect.

**CAMERA\_SERVICE\_FATAL\_ERROR**: The camera service is abnormal.

 |

#### \[h2\]OH\_CaptureSession\_Release()

Camera\_ErrorCode OH\_CaptureSession\_Release(Camera\_CaptureSession\* session)

**Description**

Releases a CaptureSession instance.

**Since**: 11

**Parameters**

| Name | Description |
| :-- | :-- |
| [Camera\_CaptureSession](../../structs/camera-capturesession/document.md)\* session | Pointer to the Camera\_CaptureSession instance to release. |

**Returns**

| Type | Description |
| :-- | :-- |
| [Camera\_ErrorCode](../camera-h/document.md#camera_errorcode) | 
**CAMERA\_OK**: The operation is successful.

**CAMERA\_INVALID\_ARGUMENT**: A parameter is missing or the parameter type is incorrect.

**CAMERA\_SERVICE\_FATAL\_ERROR**: The camera service is abnormal.

 |

#### \[h2\]OH\_CaptureSession\_HasFlash()

Camera\_ErrorCode OH\_CaptureSession\_HasFlash(Camera\_CaptureSession\* session, bool\* hasFlash)

**Description**

Checks whether the device has flash.

**Since**: 11

**Parameters**

| Name | Description |
| :-- | :-- |
| [Camera\_CaptureSession](../../structs/camera-capturesession/document.md)\* session | Pointer to the target Camera\_CaptureSession instance. |
| bool\* hasFlash | Pointer to the check result for whether the device has flash. **true** if the device has flash, **false** otherwise. |

**Returns**

| Type | Description |
| :-- | :-- |
| [Camera\_ErrorCode](../camera-h/document.md#camera_errorcode) | 
**CAMERA\_OK**: The operation is successful.

**CAMERA\_INVALID\_ARGUMENT**: A parameter is missing or the parameter type is incorrect.

**CAMERA\_SESSION\_NOT\_CONFIG**: The capture session is not configured.

 |

#### \[h2\]OH\_CaptureSession\_IsFlashModeSupported()

Camera\_ErrorCode OH\_CaptureSession\_IsFlashModeSupported(Camera\_CaptureSession\* session, Camera\_FlashMode flashMode, bool\* isSupported)

**Description**

Checks whether a flash mode is supported.

**Since**: 11

**Parameters**

| Name | Description |
| :-- | :-- |
| [Camera\_CaptureSession](../../structs/camera-capturesession/document.md)\* session | Pointer to the target Camera\_CaptureSession instance. |
| [Camera\_FlashMode](../camera-h/document.md#camera_flashmode) flashMode | Flash mode to check. |
| bool\* isSupported | Pointer to the check result for the support of the flash mode. **true** if supported, **false** otherwise. |

**Returns**

| Type | Description |
| :-- | :-- |
| [Camera\_ErrorCode](../camera-h/document.md#camera_errorcode) | 
**CAMERA\_OK**: The operation is successful.

**CAMERA\_INVALID\_ARGUMENT**: A parameter is missing or the parameter type is incorrect.

**CAMERA\_SESSION\_NOT\_CONFIG**: The capture session is not configured.

 |

#### \[h2\]OH\_CaptureSession\_GetFlashMode()

Camera\_ErrorCode OH\_CaptureSession\_GetFlashMode(Camera\_CaptureSession\* session, Camera\_FlashMode\* flashMode)

**Description**

Obtains the flash mode in use.

**Since**: 11

**Parameters**

| Name | Description |
| :-- | :-- |
| [Camera\_CaptureSession](../../structs/camera-capturesession/document.md)\* session | Pointer to the target Camera\_CaptureSession instance. |
| [Camera\_FlashMode](../camera-h/document.md#camera_flashmode)\* flashMode | Pointer to the flash mode. |

**Returns**

| Type | Description |
| :-- | :-- |
| [Camera\_ErrorCode](../camera-h/document.md#camera_errorcode) | 
**CAMERA\_OK**: The operation is successful.

**CAMERA\_INVALID\_ARGUMENT**: A parameter is missing or the parameter type is incorrect.

**CAMERA\_SESSION\_NOT\_CONFIG**: The capture session is not configured.

 |

#### \[h2\]OH\_CaptureSession\_SetFlashMode()

Camera\_ErrorCode OH\_CaptureSession\_SetFlashMode(Camera\_CaptureSession\* session, Camera\_FlashMode flashMode)

**Description**

Sets a flash mode for the device.

**Since**: 11

**Parameters**

| Name | Description |
| :-- | :-- |
| [Camera\_CaptureSession](../../structs/camera-capturesession/document.md)\* session | Pointer to the target Camera\_CaptureSession instance. |
| [Camera\_FlashMode](../camera-h/document.md#camera_flashmode) flashMode | Flash mode to set. |

**Returns**

| Type | Description |
| :-- | :-- |
| [Camera\_ErrorCode](../camera-h/document.md#camera_errorcode) | 
**CAMERA\_OK**: The operation is successful.

**CAMERA\_INVALID\_ARGUMENT**: A parameter is missing or the parameter type is incorrect.

**CAMERA\_SESSION\_NOT\_CONFIG**: The capture session is not configured.

 |

#### \[h2\]OH\_CaptureSession\_IsExposureModeSupported()

Camera\_ErrorCode OH\_CaptureSession\_IsExposureModeSupported(Camera\_CaptureSession\* session, Camera\_ExposureMode exposureMode, bool\* isSupported)

**Description**

Checks whether an exposure mode is supported.

**Since**: 11

**Parameters**

| Name | Description |
| :-- | :-- |
| [Camera\_CaptureSession](../../structs/camera-capturesession/document.md)\* session | Pointer to the target Camera\_CaptureSession instance. |
| [Camera\_ExposureMode](../camera-h/document.md#camera_exposuremode) exposureMode | Exposure mode to check. |
| bool\* isSupported | Pointer to the check result for the support of the exposure mode. **true** if supported, **false** otherwise. |

**Returns**

| Type | Description |
| :-- | :-- |
| [Camera\_ErrorCode](../camera-h/document.md#camera_errorcode) | 
**CAMERA\_OK**: The operation is successful.

**CAMERA\_INVALID\_ARGUMENT**: A parameter is missing or the parameter type is incorrect.

**CAMERA\_SESSION\_NOT\_CONFIG**: The capture session is not configured.

 |

#### \[h2\]OH\_CaptureSession\_GetExposureMode()

Camera\_ErrorCode OH\_CaptureSession\_GetExposureMode(Camera\_CaptureSession\* session, Camera\_ExposureMode\* exposureMode)

**Description**

Obtains the exposure mode in use. This API directly returns an invalid value if you have not set the exposure mode using [OH\_CaptureSession\_SetExposureMode](#oh_capturesession_setexposuremode).

**Since**: 11

**Parameters**

| Name | Description |
| :-- | :-- |
| [Camera\_CaptureSession](../../structs/camera-capturesession/document.md)\* session | Pointer to the target Camera\_CaptureSession instance. |
| [Camera\_ExposureMode](../camera-h/document.md#camera_exposuremode)\* exposureMode | Pointer to the exposure mode. |

**Returns**

| Type | Description |
| :-- | :-- |
| [Camera\_ErrorCode](../camera-h/document.md#camera_errorcode) | 
**CAMERA\_OK**: The operation is successful.

**CAMERA\_INVALID\_ARGUMENT**: A parameter is missing or the parameter type is incorrect.

**CAMERA\_SESSION\_NOT\_CONFIG**: The capture session is not configured.

 |

#### \[h2\]OH\_CaptureSession\_SetExposureMode()

Camera\_ErrorCode OH\_CaptureSession\_SetExposureMode(Camera\_CaptureSession\* session, Camera\_ExposureMode exposureMode)

**Description**

Sets an exposure mode for the device.

**Since**: 11

**Parameters**

| Name | Description |
| :-- | :-- |
| [Camera\_CaptureSession](../../structs/camera-capturesession/document.md)\* session | Pointer to the target Camera\_CaptureSession instance. |
| [Camera\_ExposureMode](../camera-h/document.md#camera_exposuremode) exposureMode | Exposure mode to set. |

**Returns**

| Type | Description |
| :-- | :-- |
| [Camera\_ErrorCode](../camera-h/document.md#camera_errorcode) | 
**CAMERA\_OK**: The operation is successful.

**CAMERA\_INVALID\_ARGUMENT**: A parameter is missing or the parameter type is incorrect.

**CAMERA\_SESSION\_NOT\_CONFIG**: The capture session is not configured.

 |

#### \[h2\]OH\_CaptureSession\_GetMeteringPoint()

Camera\_ErrorCode OH\_CaptureSession\_GetMeteringPoint(Camera\_CaptureSession\* session, Camera\_Point\* point)

**Description**

Obtains the metering point in use.

**Since**: 11

**Parameters**

| Name | Description |
| :-- | :-- |
| [Camera\_CaptureSession](../../structs/camera-capturesession/document.md)\* session | Pointer to the target Camera\_CaptureSession instance. |
| [Camera\_Point](../../structs/camera-point/document.md)\* point | Pointer to the metering point. |

**Returns**

| Type | Description |
| :-- | :-- |
| [Camera\_ErrorCode](../camera-h/document.md#camera_errorcode) | 
**CAMERA\_OK**: The operation is successful.

**CAMERA\_INVALID\_ARGUMENT**: A parameter is missing or the parameter type is incorrect.

**CAMERA\_SESSION\_NOT\_CONFIG**: The capture session is not configured.

 |

#### \[h2\]OH\_CaptureSession\_SetMeteringPoint()

Camera\_ErrorCode OH\_CaptureSession\_SetMeteringPoint(Camera\_CaptureSession\* session, Camera\_Point point)

**Description**

Sets the metering point, which is the center point of the metering rectangle.

**Since**: 11

**Parameters**

| Name | Description |
| :-- | :-- |
| [Camera\_CaptureSession](../../structs/camera-capturesession/document.md)\* session | Pointer to the target Camera\_CaptureSession instance. |
| [Camera\_Point](../../structs/camera-point/document.md) point | Metering point to set. |

**Returns**

| Type | Description |
| :-- | :-- |
| [Camera\_ErrorCode](../camera-h/document.md#camera_errorcode) | 
**CAMERA\_OK**: The operation is successful.

**CAMERA\_INVALID\_ARGUMENT**: A parameter is missing or the parameter type is incorrect.

**CAMERA\_SESSION\_NOT\_CONFIG**: The capture session is not configured.

 |

#### \[h2\]OH\_CaptureSession\_GetExposureBiasRange()

Camera\_ErrorCode OH\_CaptureSession\_GetExposureBiasRange(Camera\_CaptureSession\* session, float\* minExposureBias, float\* maxExposureBias, float\* step)

**Description**

Obtains the exposure compensation values of the device.

**Since**: 11

**Parameters**

| Name | Description |
| :-- | :-- |
| [Camera\_CaptureSession](../../structs/camera-capturesession/document.md)\* session | Pointer to the target Camera\_CaptureSession instance. |
| float\* minExposureBias | Pointer to the minimum exposure compensation value. |
| float\* maxExposureBias | Pointer to the maximum exposure compensation value. |
| float\* step | Pointer to the exposure compensation step. |

**Returns**

| Type | Description |
| :-- | :-- |
| [Camera\_ErrorCode](../camera-h/document.md#camera_errorcode) | 
**CAMERA\_OK**: The operation is successful.

**CAMERA\_INVALID\_ARGUMENT**: A parameter is missing or the parameter type is incorrect.

**CAMERA\_SESSION\_NOT\_CONFIG**: The capture session is not configured.

 |

#### \[h2\]OH\_CaptureSession\_SetExposureBias()

Camera\_ErrorCode OH\_CaptureSession\_SetExposureBias(Camera\_CaptureSession\* session, float exposureBias)

**Description**

Sets an exposure compensation value for the device.

**Since**: 11

**Parameters**

| Name | Description |
| :-- | :-- |
| [Camera\_CaptureSession](../../structs/camera-capturesession/document.md)\* session | Pointer to the target Camera\_CaptureSession instance. |
| float exposureBias | Exposure compensation value to set. |

**Returns**

| Type | Description |
| :-- | :-- |
| [Camera\_ErrorCode](../camera-h/document.md#camera_errorcode) | 
**CAMERA\_OK**: The operation is successful.

**CAMERA\_INVALID\_ARGUMENT**: A parameter is missing or the parameter type is incorrect.

**CAMERA\_SESSION\_NOT\_CONFIG**: The capture session is not configured.

 |

#### \[h2\]OH\_CaptureSession\_GetExposureBias()

Camera\_ErrorCode OH\_CaptureSession\_GetExposureBias(Camera\_CaptureSession\* session, float\* exposureBias)

**Description**

Obtains the exposure compensation value in use.

**Since**: 11

**Parameters**

| Name | Description |
| :-- | :-- |
| [Camera\_CaptureSession](../../structs/camera-capturesession/document.md)\* session | Pointer to the target Camera\_CaptureSession instance. |
| float\* exposureBias | Pointer to the exposure compensation value. |

**Returns**

| Type | Description |
| :-- | :-- |
| [Camera\_ErrorCode](../camera-h/document.md#camera_errorcode) | 
**CAMERA\_OK**: The operation is successful.

**CAMERA\_INVALID\_ARGUMENT**: A parameter is missing or the parameter type is incorrect.

**CAMERA\_SESSION\_NOT\_CONFIG**: The capture session is not configured.

 |

#### \[h2\]OH\_CaptureSession\_IsFocusModeSupported()

Camera\_ErrorCode OH\_CaptureSession\_IsFocusModeSupported(Camera\_CaptureSession\* session, Camera\_FocusMode focusMode, bool\* isSupported)

**Description**

Checks whether a focus mode is supported.

**Since**: 11

**Parameters**

| Name | Description |
| :-- | :-- |
| [Camera\_CaptureSession](../../structs/camera-capturesession/document.md)\* session | Pointer to the target Camera\_CaptureSession instance. |
| [Camera\_FocusMode](../camera-h/document.md#camera_focusmode) focusMode | Focus mode to check. |
| bool\* isSupported | Pointer to the check result for the support of the focus mode. **true** if supported, **false** otherwise. |

**Returns**

| Type | Description |
| :-- | :-- |
| [Camera\_ErrorCode](../camera-h/document.md#camera_errorcode) | 
**CAMERA\_OK**: The operation is successful.

**CAMERA\_INVALID\_ARGUMENT**: A parameter is missing or the parameter type is incorrect.

**CAMERA\_SESSION\_NOT\_CONFIG**: The capture session is not configured.

 |

#### \[h2\]OH\_CaptureSession\_GetFocusMode()

Camera\_ErrorCode OH\_CaptureSession\_GetFocusMode(Camera\_CaptureSession\* session, Camera\_FocusMode\* focusMode)

**Description**

Obtains the focus mode in use.

**Since**: 11

**Parameters**

| Name | Description |
| :-- | :-- |
| [Camera\_CaptureSession](../../structs/camera-capturesession/document.md)\* session | Pointer to the target Camera\_CaptureSession instance. |
| [Camera\_FocusMode](../camera-h/document.md#camera_focusmode)\* focusMode | Pointer to the focus mode. |

**Returns**

| Type | Description |
| :-- | :-- |
| [Camera\_ErrorCode](../camera-h/document.md#camera_errorcode) | 
**CAMERA\_OK**: The operation is successful.

**CAMERA\_INVALID\_ARGUMENT**: A parameter is missing or the parameter type is incorrect.

**CAMERA\_SESSION\_NOT\_CONFIG**: The capture session is not configured.

 |

#### \[h2\]OH\_CaptureSession\_SetFocusMode()

Camera\_ErrorCode OH\_CaptureSession\_SetFocusMode(Camera\_CaptureSession\* session, Camera\_FocusMode focusMode)

**Description**

Sets a focus mode for the device.

**Since**: 11

**Parameters**

| Name | Description |
| :-- | :-- |
| [Camera\_CaptureSession](../../structs/camera-capturesession/document.md)\* session | Pointer to the target Camera\_CaptureSession instance. |
| [Camera\_FocusMode](../camera-h/document.md#camera_focusmode) focusMode | Focus mode to set. |

**Returns**

| Type | Description |
| :-- | :-- |
| [Camera\_ErrorCode](../camera-h/document.md#camera_errorcode) | 
**CAMERA\_OK**: The operation is successful.

**CAMERA\_INVALID\_ARGUMENT**: A parameter is missing or the parameter type is incorrect.

**CAMERA\_SESSION\_NOT\_CONFIG**: The capture session is not configured.

 |

#### \[h2\]OH\_CaptureSession\_GetFocusPoint()

Camera\_ErrorCode OH\_CaptureSession\_GetFocusPoint(Camera\_CaptureSession\* session, Camera\_Point\* focusPoint)

**Description**

Obtains the focal point in use.

**Since**: 11

**Parameters**

| Name | Description |
| :-- | :-- |
| [Camera\_CaptureSession](../../structs/camera-capturesession/document.md)\* session | Pointer to the target Camera\_CaptureSession instance. |
| [Camera\_Point](../../structs/camera-point/document.md)\* focusPoint | Pointer to the focal point. |

**Returns**

| Type | Description |
| :-- | :-- |
| [Camera\_ErrorCode](../camera-h/document.md#camera_errorcode) | 
**CAMERA\_OK**: The operation is successful.

**CAMERA\_INVALID\_ARGUMENT**: A parameter is missing or the parameter type is incorrect.

**CAMERA\_SESSION\_NOT\_CONFIG**: The capture session is not configured.

 |

#### \[h2\]OH\_CaptureSession\_SetFocusPoint()

Camera\_ErrorCode OH\_CaptureSession\_SetFocusPoint(Camera\_CaptureSession\* session, Camera\_Point focusPoint)

**Description**

Sets a focal point for the device.

**Since**: 11

**Parameters**

| Name | Description |
| :-- | :-- |
| [Camera\_CaptureSession](../../structs/camera-capturesession/document.md)\* session | Pointer to the target Camera\_CaptureSession instance. |
| [Camera\_Point](../../structs/camera-point/document.md) focusPoint | Focal point to set. |

**Returns**

| Type | Description |
| :-- | :-- |
| [Camera\_ErrorCode](../camera-h/document.md#camera_errorcode) | 
**CAMERA\_OK**: The operation is successful.

**CAMERA\_INVALID\_ARGUMENT**: A parameter is missing or the parameter type is incorrect.

**CAMERA\_SESSION\_NOT\_CONFIG**: The capture session is not configured.

 |

#### \[h2\]OH\_CaptureSession\_GetZoomRatioRange()

Camera\_ErrorCode OH\_CaptureSession\_GetZoomRatioRange(Camera\_CaptureSession\* session, float\* minZoom, float\* maxZoom)

**Description**

Obtains the supported zoom ratio range.

**Since**: 11

**Parameters**

| Name | Description |
| :-- | :-- |
| [Camera\_CaptureSession](../../structs/camera-capturesession/document.md)\* session | Pointer to the target Camera\_CaptureSession instance. |
| float\* minZoom | Pointer to the minimum zoom ratio. |
| float\* maxZoom | Pointer to the maximum zoom ratio. |

**Returns**

| Type | Description |
| :-- | :-- |
| [Camera\_ErrorCode](../camera-h/document.md#camera_errorcode) | 
**CAMERA\_OK**: The operation is successful.

**CAMERA\_INVALID\_ARGUMENT**: A parameter is missing or the parameter type is incorrect.

**CAMERA\_SESSION\_NOT\_CONFIG**: The capture session is not configured.

 |

#### \[h2\]OH\_CaptureSession\_GetZoomRatio()

Camera\_ErrorCode OH\_CaptureSession\_GetZoomRatio(Camera\_CaptureSession\* session, float\* zoom)

**Description**

Obtains the zoom ratio in use.

**Since**: 11

**Parameters**

| Name | Description |
| :-- | :-- |
| [Camera\_CaptureSession](../../structs/camera-capturesession/document.md)\* session | Pointer to the target Camera\_CaptureSession instance. |
| float\* zoom | Pointer to the zoom ratio. |

**Returns**

| Type | Description |
| :-- | :-- |
| [Camera\_ErrorCode](../camera-h/document.md#camera_errorcode) | 
**CAMERA\_OK**: The operation is successful.

**CAMERA\_INVALID\_ARGUMENT**: A parameter is missing or the parameter type is incorrect.

**CAMERA\_SESSION\_NOT\_CONFIG**: The capture session is not configured.

 |

#### \[h2\]OH\_CaptureSession\_SetZoomRatio()

Camera\_ErrorCode OH\_CaptureSession\_SetZoomRatio(Camera\_CaptureSession\* session, float zoom)

**Description**

Sets a zoom ratio for the device.

**Since**: 11

**Parameters**

| Name | Description |
| :-- | :-- |
| [Camera\_CaptureSession](../../structs/camera-capturesession/document.md)\* session | Pointer to the target Camera\_CaptureSession instance. |
| float zoom | 
Target zoom ratio.

It takes some time for the zoom ratio to take effect at the bottom layer. To obtain the correct zoom ratio, you need to wait for one to two frames.

 |

**Returns**

| Type | Description |
| :-- | :-- |
| [Camera\_ErrorCode](../camera-h/document.md#camera_errorcode) | 
**CAMERA\_OK**: The operation is successful.

**CAMERA\_INVALID\_ARGUMENT**: A parameter is missing or the parameter type is incorrect.

**CAMERA\_SESSION\_NOT\_CONFIG**: The capture session is not configured.

 |

#### \[h2\]OH\_CaptureSession\_IsVideoStabilizationModeSupported()

Camera\_ErrorCode OH\_CaptureSession\_IsVideoStabilizationModeSupported(Camera\_CaptureSession\* session, Camera\_VideoStabilizationMode mode, bool\* isSupported)

**Description**

Checks whether a video stabilization mode is supported.

**Since**: 11

**Parameters**

| Name | Description |
| :-- | :-- |
| [Camera\_CaptureSession](../../structs/camera-capturesession/document.md)\* session | Pointer to the target Camera\_CaptureSession instance. |
| [Camera\_VideoStabilizationMode](../camera-h/document.md#camera_videostabilizationmode) mode | Video stabilization mode to check. |
| bool\* isSupported | Pointer to the check result for the support of the video stabilization mode. **true** if supported, **false** otherwise. |

**Returns**

| Type | Description |
| :-- | :-- |
| [Camera\_ErrorCode](../camera-h/document.md#camera_errorcode) | 
**CAMERA\_OK**: The operation is successful.

**CAMERA\_INVALID\_ARGUMENT**: A parameter is missing or the parameter type is incorrect.

**CAMERA\_SESSION\_NOT\_CONFIG**: The capture session is not configured.

 |

#### \[h2\]OH\_CaptureSession\_GetVideoStabilizationMode()

Camera\_ErrorCode OH\_CaptureSession\_GetVideoStabilizationMode(Camera\_CaptureSession\* session, Camera\_VideoStabilizationMode\* mode)

**Description**

Obtains the video stabilization mode in use.

**Since**: 11

**Parameters**

| Name | Description |
| :-- | :-- |
| [Camera\_CaptureSession](../../structs/camera-capturesession/document.md)\* session | Pointer to the target Camera\_CaptureSession instance. |
| [Camera\_VideoStabilizationMode](../camera-h/document.md#camera_videostabilizationmode)\* mode | Pointer to the video stabilization mode. |

**Returns**

| Type | Description |
| :-- | :-- |
| [Camera\_ErrorCode](../camera-h/document.md#camera_errorcode) | 
**CAMERA\_OK**: The operation is successful.

**CAMERA\_INVALID\_ARGUMENT**: A parameter is missing or the parameter type is incorrect.

**CAMERA\_SESSION\_NOT\_CONFIG**: The capture session is not configured.

 |

#### \[h2\]OH\_CaptureSession\_SetVideoStabilizationMode()

Camera\_ErrorCode OH\_CaptureSession\_SetVideoStabilizationMode(Camera\_CaptureSession\* session, Camera\_VideoStabilizationMode mode)

**Description**

Sets a video stabilization mode for the device.

**Since**: 11

**Parameters**

| Name | Description |
| :-- | :-- |
| [Camera\_CaptureSession](../../structs/camera-capturesession/document.md)\* session | Pointer to the target Camera\_CaptureSession instance. |
| [Camera\_VideoStabilizationMode](../camera-h/document.md#camera_videostabilizationmode) mode | Video stabilization mode to set. |

**Returns**

| Type | Description |
| :-- | :-- |
| [Camera\_ErrorCode](../camera-h/document.md#camera_errorcode) | 
**CAMERA\_OK**: The operation is successful.

**CAMERA\_INVALID\_ARGUMENT**: A parameter is missing or the parameter type is incorrect.

**CAMERA\_SESSION\_NOT\_CONFIG**: The capture session is not configured.

 |

#### \[h2\]OH\_CaptureSession\_CanAddInput()

Camera\_ErrorCode OH\_CaptureSession\_CanAddInput(Camera\_CaptureSession\* session, Camera\_Input\* cameraInput, bool\* isSuccessful)

**Description**

Checks whether a Camera\_Input instance can be added to a session.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [Camera\_CaptureSession](../../structs/camera-capturesession/document.md)\* session | Pointer to the target Camera\_CaptureSession instance. |
| [Camera\_Input](../../structs/camera-input/document.md)\* cameraInput | Pointer to the Camera\_Input instance to check. |
| bool\* isSuccessful | Pointer to the check result for whether the Camera\_Input instance can be added to the session. **true** if it can be added to the session, **false** otherwise. |

**Returns**

| Type | Description |
| :-- | :-- |
| [Camera\_ErrorCode](../camera-h/document.md#camera_errorcode) | 
**CAMERA\_OK**: The operation is successful.

**CAMERA\_INVALID\_ARGUMENT**: A parameter is missing or the parameter type is incorrect.

 |

#### \[h2\]OH\_CaptureSession\_CanAddPreviewOutput()

Camera\_ErrorCode OH\_CaptureSession\_CanAddPreviewOutput(Camera\_CaptureSession\* session, Camera\_PreviewOutput\* cameraOutput, bool\* isSuccessful)

**Description**

Checks whether a PreviewOutput instance can be added to a session.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [Camera\_CaptureSession](../../structs/camera-capturesession/document.md)\* session | Pointer to the target Camera\_CaptureSession instance. |
| [Camera\_PreviewOutput](../../structs/camera-previewoutput/document.md)\* cameraOutput | Pointer to the PreviewOutput instance to check. |
| bool\* isSuccessful | Pointer to the check result for whether the PreviewOutput instance can be added to the session. **true** if it can be added to the session, **false** otherwise. |

**Returns**

| Type | Description |
| :-- | :-- |
| [Camera\_ErrorCode](../camera-h/document.md#camera_errorcode) | 
**CAMERA\_OK**: The operation is successful.

**CAMERA\_INVALID\_ARGUMENT**: A parameter is missing or the parameter type is incorrect.

 |

#### \[h2\]OH\_CaptureSession\_CanAddPhotoOutput()

Camera\_ErrorCode OH\_CaptureSession\_CanAddPhotoOutput(Camera\_CaptureSession\* session, Camera\_PhotoOutput\* cameraOutput, bool\* isSuccessful)

**Description**

Checks whether a PhotoOutput instance can be added to a session.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [Camera\_CaptureSession](../../structs/camera-capturesession/document.md)\* session | Pointer to the target Camera\_CaptureSession instance. |
| [Camera\_PhotoOutput](../../structs/camera-photooutput/document.md)\* cameraOutput | Pointer to the PhotoOutput instance to check. |
| bool\* isSuccessful | Pointer to the check result for whether the PhotoOutput instance can be added to the session. **true** if it can be added to the session, **false** otherwise. |

**Returns**

| Type | Description |
| :-- | :-- |
| [Camera\_ErrorCode](../camera-h/document.md#camera_errorcode) | 
**CAMERA\_OK**: The operation is successful.

**CAMERA\_INVALID\_ARGUMENT**: A parameter is missing or the parameter type is incorrect.

 |

#### \[h2\]OH\_CaptureSession\_CanAddVideoOutput()

Camera\_ErrorCode OH\_CaptureSession\_CanAddVideoOutput(Camera\_CaptureSession\* session, Camera\_VideoOutput\* cameraOutput, bool\* isSuccessful)

**Description**

Checks whether a **VideoOutput** instance can be added to a session.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [Camera\_CaptureSession](../../structs/camera-capturesession/document.md)\* session | Pointer to the target Camera\_CaptureSession instance. |
| [Camera\_VideoOutput](../../structs/camera-videooutput/document.md)\* cameraOutput | Pointer to the **VideoOutput** instance to check. |
| bool\* isSuccessful | Pointer to the check result for whether the VideoOutput instance can be added to the session. **true** if it can be added to the session, **false** otherwise. |

**Returns**

| Type | Description |
| :-- | :-- |
| [Camera\_ErrorCode](../camera-h/document.md#camera_errorcode) | 
**CAMERA\_OK**: The operation is successful.

**CAMERA\_INVALID\_ARGUMENT**: A parameter is missing or the parameter type is incorrect.

 |

#### \[h2\]OH\_CaptureSession\_CanPreconfig()

Camera\_ErrorCode OH\_CaptureSession\_CanPreconfig(Camera\_CaptureSession\* session, Camera\_PreconfigType preconfigType, bool\* canPreconfig)

**Description**

Checks whether a preconfigured resolution type is supported.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [Camera\_CaptureSession](../../structs/camera-capturesession/document.md)\* session | Pointer to the target Camera\_CaptureSession instance. |
| [Camera\_PreconfigType](../camera-h/document.md#camera_preconfigtype) preconfigType | Target preconfigured resolution type. |
| bool\* canPreconfig | Pointer to the check result for the support of the preconfigured resolution type. **true** if supported, **false** otherwise. |

**Returns**

| Type | Description |
| :-- | :-- |
| [Camera\_ErrorCode](../camera-h/document.md#camera_errorcode) | 
**CAMERA\_OK**: The operation is successful.

**CAMERA\_INVALID\_ARGUMENT**: A parameter is missing or the parameter type is incorrect.

 |

#### \[h2\]OH\_CaptureSession\_CanPreconfigWithRatio()

Camera\_ErrorCode OH\_CaptureSession\_CanPreconfigWithRatio(Camera\_CaptureSession\* session, Camera\_PreconfigType preconfigType, Camera\_PreconfigRatio preconfigRatio, bool\* canPreconfig)

**Description**

Checks whether a preconfigured resolution type with an aspect ratio is supported.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [Camera\_CaptureSession](../../structs/camera-capturesession/document.md)\* session | Pointer to the target Camera\_CaptureSession instance. |
| [Camera\_PreconfigType](../camera-h/document.md#camera_preconfigtype) preconfigType | Target preconfigured resolution type. |
| [Camera\_PreconfigRatio](../camera-h/document.md#camera_preconfigratio) preconfigRatio | Target preconfigured aspect ratio. |
| bool\* canPreconfig | Pointer to the check result for the support of the preconfigured resolution type. **true** if supported, **false** otherwise. |

**Returns**

| Type | Description |
| :-- | :-- |
| [Camera\_ErrorCode](../camera-h/document.md#camera_errorcode) | 
**CAMERA\_OK**: The operation is successful.

**CAMERA\_INVALID\_ARGUMENT**: A parameter is missing or the parameter type is incorrect.

 |

#### \[h2\]OH\_CaptureSession\_Preconfig()

Camera\_ErrorCode OH\_CaptureSession\_Preconfig(Camera\_CaptureSession\* session, Camera\_PreconfigType preconfigType)

**Description**

Sets a preconfigured resolution type.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [Camera\_CaptureSession](../../structs/camera-capturesession/document.md)\* session | Pointer to the target Camera\_CaptureSession instance. |
| [Camera\_PreconfigType](../camera-h/document.md#camera_preconfigtype) preconfigType | Target preconfigured resolution type. |

**Returns**

| Type | Description |
| :-- | :-- |
| [Camera\_ErrorCode](../camera-h/document.md#camera_errorcode) | 
**CAMERA\_OK**: The operation is successful.

**CAMERA\_INVALID\_ARGUMENT**: A parameter is missing or the parameter type is incorrect.

**CAMERA\_SERVICE\_FATAL\_ERROR**: The camera service is abnormal.

 |

#### \[h2\]OH\_CaptureSession\_PreconfigWithRatio()

Camera\_ErrorCode OH\_CaptureSession\_PreconfigWithRatio(Camera\_CaptureSession\* session, Camera\_PreconfigType preconfigType, Camera\_PreconfigRatio preconfigRatio)

**Description**

Sets a preconfigured resolution type with an aspect ratio.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [Camera\_CaptureSession](../../structs/camera-capturesession/document.md)\* session | Pointer to the target Camera\_CaptureSession instance. |
| [Camera\_PreconfigType](../camera-h/document.md#camera_preconfigtype) preconfigType | Target preconfigured resolution type. |
| [Camera\_PreconfigRatio](../camera-h/document.md#camera_preconfigratio) preconfigRatio | Target preconfigured aspect ratio. |

**Returns**

| Type | Description |
| :-- | :-- |
| [Camera\_ErrorCode](../camera-h/document.md#camera_errorcode) | 
**CAMERA\_OK**: The operation is successful.

**CAMERA\_INVALID\_ARGUMENT**: A parameter is missing or the parameter type is incorrect.

**CAMERA\_SERVICE\_FATAL\_ERROR**: The camera service is abnormal.

 |

#### \[h2\]OH\_CaptureSession\_GetExposureValue()

Camera\_ErrorCode OH\_CaptureSession\_GetExposureValue(Camera\_CaptureSession\* session, float\* exposureValue)

**Description**

Obtains the exposure value.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [Camera\_CaptureSession](../../structs/camera-capturesession/document.md)\* session | Pointer to the target Camera\_CaptureSession instance. |
| float\* exposureValue | Pointer to the exposure value. |

**Returns**

| Type | Description |
| :-- | :-- |
| [Camera\_ErrorCode](../camera-h/document.md#camera_errorcode) | 
**CAMERA\_OK**: The operation is successful.

**CAMERA\_INVALID\_ARGUMENT**: A parameter is missing or the parameter type is incorrect.

**CAMERA\_SERVICE\_FATAL\_ERROR**: The camera service is abnormal.

 |

#### \[h2\]OH\_CaptureSession\_GetFocalLength()

Camera\_ErrorCode OH\_CaptureSession\_GetFocalLength(Camera\_CaptureSession\* session, float\* focalLength)

**Description**

Obtains the current focal length.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [Camera\_CaptureSession](../../structs/camera-capturesession/document.md)\* session | Pointer to the target Camera\_CaptureSession instance. |
| float\* focalLength | Pointer to the focal length. |

**Returns**

| Type | Description |
| :-- | :-- |
| [Camera\_ErrorCode](../camera-h/document.md#camera_errorcode) | 
**CAMERA\_OK**: The operation is successful.

**CAMERA\_INVALID\_ARGUMENT**: A parameter is missing or the parameter type is incorrect.

**CAMERA\_SESSION\_NOT\_CONFIG**: The capture session is not configured.

 |

#### \[h2\]OH\_CaptureSession\_SetSmoothZoom()

Camera\_ErrorCode OH\_CaptureSession\_SetSmoothZoom(Camera\_CaptureSession\* session, float targetZoom, Camera\_SmoothZoomMode smoothZoomMode)

**Description**

Sets smooth zoom.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [Camera\_CaptureSession](../../structs/camera-capturesession/document.md)\* session | Pointer to the target Camera\_CaptureSession instance. |
| float targetZoom | Target zoom ratio. |
| [Camera\_SmoothZoomMode](../camera-h/document.md#camera_smoothzoommode) smoothZoomMode | Smooth zoom mode. |

**Returns**

| Type | Description |
| :-- | :-- |
| [Camera\_ErrorCode](../camera-h/document.md#camera_errorcode) | 
**CAMERA\_OK**: The operation is successful.

**CAMERA\_INVALID\_ARGUMENT**: A parameter is missing or the parameter type is incorrect.

**CAMERA\_SESSION\_NOT\_CONFIG**: The capture session is not configured.

 |

#### \[h2\]OH\_CaptureSession\_GetSupportedColorSpaces()

Camera\_ErrorCode OH\_CaptureSession\_GetSupportedColorSpaces(Camera\_CaptureSession\* session, OH\_NativeBuffer\_ColorSpace\*\* colorSpace, uint32\_t\* size)

**Description**

Obtains the supported color spaces.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [Camera\_CaptureSession](../../structs/camera-capturesession/document.md)\* session | Pointer to the target Camera\_CaptureSession instance. |
| OH\_NativeBuffer\_ColorSpace\*\* colorSpace | Double pointer to the list of supported color spaces, which are defined in the OH\_NativeBuffer\_ColorSpace struct, if the function is successfully called. |
| uint32\_t\* size | Pointer to the size of the list of supported color spaces. |

**Returns**

| Type | Description |
| :-- | :-- |
| [Camera\_ErrorCode](../camera-h/document.md#camera_errorcode) | 
**CAMERA\_OK**: The operation is successful.

**CAMERA\_INVALID\_ARGUMENT**: A parameter is missing or the parameter type is incorrect.

**CAMERA\_SESSION\_NOT\_CONFIG**: The capture session is not configured.

 |

#### \[h2\]OH\_CaptureSession\_DeleteColorSpaces()

Camera\_ErrorCode OH\_CaptureSession\_DeleteColorSpaces(Camera\_CaptureSession\* session, OH\_NativeBuffer\_ColorSpace\* colorSpace)

**Description**

Deletes color spaces.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [Camera\_CaptureSession](../../structs/camera-capturesession/document.md)\* session | Pointer to the target Camera\_CaptureSession instance. |
| [OH\_NativeBuffer\_ColorSpace](../../../../../graphics/arkgraphics-2d/c-apis/header-files/buffer-common-h/document.md#oh_nativebuffer_colorspace)\* colorSpace | Pointer to the list of color spaces, which are defined in the OH\_NativeBuffer\_ColorSpace struct. |

**Returns**

| Type | Description |
| :-- | :-- |
| [Camera\_ErrorCode](../camera-h/document.md#camera_errorcode) | 
**CAMERA\_OK**: The operation is successful.

**CAMERA\_INVALID\_ARGUMENT**: A parameter is missing or the parameter type is incorrect.

 |

#### \[h2\]OH\_CaptureSession\_GetActiveColorSpace()

Camera\_ErrorCode OH\_CaptureSession\_GetActiveColorSpace(Camera\_CaptureSession\* session, OH\_NativeBuffer\_ColorSpace\* colorSpace)

**Description**

Obtains the active color space.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [Camera\_CaptureSession](../../structs/camera-capturesession/document.md)\* session | Pointer to the target Camera\_CaptureSession instance. |
| [OH\_NativeBuffer\_ColorSpace](../../../../../graphics/arkgraphics-2d/c-apis/header-files/buffer-common-h/document.md#oh_nativebuffer_colorspace)\* colorSpace | Pointer to the OH\_NativeBuffer\_ColorSpace instance. |

**Returns**

| Type | Description |
| :-- | :-- |
| [Camera\_ErrorCode](../camera-h/document.md#camera_errorcode) | 
**CAMERA\_OK**: The operation is successful.

**CAMERA\_INVALID\_ARGUMENT**: A parameter is missing or the parameter type is incorrect.

**CAMERA\_SESSION\_NOT\_CONFIG**: The capture session is not configured.

 |

#### \[h2\]OH\_CaptureSession\_SetActiveColorSpace()

Camera\_ErrorCode OH\_CaptureSession\_SetActiveColorSpace(Camera\_CaptureSession\* session, OH\_NativeBuffer\_ColorSpace colorSpace)

**Description**

Sets the active color space.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [Camera\_CaptureSession](../../structs/camera-capturesession/document.md)\* session | Pointer to the target Camera\_CaptureSession instance. |
| [OH\_NativeBuffer\_ColorSpace](../../../../../graphics/arkgraphics-2d/c-apis/header-files/buffer-common-h/document.md#oh_nativebuffer_colorspace) colorSpace | Target OH\_NativeBuffer\_ColorSpace instance. |

**Returns**

| Type | Description |
| :-- | :-- |
| [Camera\_ErrorCode](../camera-h/document.md#camera_errorcode) | 
**CAMERA\_OK**: The operation is successful.

**CAMERA\_INVALID\_ARGUMENT**: A parameter is missing or the parameter type is incorrect.

**CAMERA\_SESSION\_NOT\_CONFIG**: The capture session is not configured.

 |

#### \[h2\]OH\_CaptureSession\_RegisterAutoDeviceSwitchStatusCallback()

Camera\_ErrorCode OH\_CaptureSession\_RegisterAutoDeviceSwitchStatusCallback(Camera\_CaptureSession\* session, OH\_CaptureSession\_OnAutoDeviceSwitchStatusChange autoDeviceSwitchStatusChange)

**Description**

Registers a callback to listen for device switching changes.

**Since**: 13

**Parameters**

| Name | Description |
| :-- | :-- |
| [Camera\_CaptureSession](../../structs/camera-capturesession/document.md)\* session | Pointer to the target Camera\_CaptureSession instance. |
| [OH\_CaptureSession\_OnAutoDeviceSwitchStatusChange](#oh_capturesession_onautodeviceswitchstatuschange) autoDeviceSwitchStatusChange | Target callback. |

**Returns**

| Type | Description |
| :-- | :-- |
| [Camera\_ErrorCode](../camera-h/document.md#camera_errorcode) | 
**CAMERA\_OK**: The operation is successful.

**CAMERA\_INVALID\_ARGUMENT**: A parameter is missing or the parameter type is incorrect.

 |

#### \[h2\]OH\_CaptureSession\_UnregisterAutoDeviceSwitchStatusCallback()

Camera\_ErrorCode OH\_CaptureSession\_UnregisterAutoDeviceSwitchStatusCallback(Camera\_CaptureSession\* session, OH\_CaptureSession\_OnAutoDeviceSwitchStatusChange autoDeviceSwitchStatusChange)

**Description**

Unregisters the callback used to listen for device switching changes.

**Since**: 13

**Parameters**

| Name | Description |
| :-- | :-- |
| [Camera\_CaptureSession](../../structs/camera-capturesession/document.md)\* session | Pointer to the target Camera\_CaptureSession instance. |
| [OH\_CaptureSession\_OnAutoDeviceSwitchStatusChange](#oh_capturesession_onautodeviceswitchstatuschange) autoDeviceSwitchStatusChange | Target callback. |

**Returns**

| Type | Description |
| :-- | :-- |
| [Camera\_ErrorCode](../camera-h/document.md#camera_errorcode) | 
**CAMERA\_OK**: The operation is successful.

**CAMERA\_INVALID\_ARGUMENT**: A parameter is missing or the parameter type is incorrect.

 |

#### \[h2\]OH\_CaptureSession\_IsAutoDeviceSwitchSupported()

Camera\_ErrorCode OH\_CaptureSession\_IsAutoDeviceSwitchSupported(Camera\_CaptureSession\* session, bool\* isSupported)

**Description**

Checks whether automatic device switching is supported.

**Since**: 13

**Parameters**

| Name | Description |
| :-- | :-- |
| [Camera\_CaptureSession](../../structs/camera-capturesession/document.md)\* session | Pointer to the target Camera\_CaptureSession instance. |
| bool\* isSupported | Pointer to the check result for the support of automatic device switching. **true** if supported, **false** otherwise. |

**Returns**

| Type | Description |
| :-- | :-- |
| [Camera\_ErrorCode](../camera-h/document.md#camera_errorcode) | 
**CAMERA\_OK**: The operation is successful.

**CAMERA\_INVALID\_ARGUMENT**: A parameter is missing or the parameter type is incorrect.

**CAMERA\_SESSION\_NOT\_CONFIG**: The capture session is not configured.

 |

#### \[h2\]OH\_CaptureSession\_EnableAutoDeviceSwitch()

Camera\_ErrorCode OH\_CaptureSession\_EnableAutoDeviceSwitch(Camera\_CaptureSession\* session, bool enabled)

**Description**

Enables or disables automatic device switching.

**Since**: 13

**Parameters**

| Name | Description |
| :-- | :-- |
| [Camera\_CaptureSession](../../structs/camera-capturesession/document.md)\* session | Pointer to the target Camera\_CaptureSession instance. |
| bool enabled | Whether to enable or disable automatic switching. **true** to enable, **false** otherwise. |

**Returns**

| Type | Description |
| :-- | :-- |
| [Camera\_ErrorCode](../camera-h/document.md#camera_errorcode) | 
**CAMERA\_OK**: The operation is successful.

**CAMERA\_INVALID\_ARGUMENT**: A parameter is missing or the parameter type is incorrect.

**CAMERA\_SESSION\_NOT\_CONFIG**: The capture session is not configured.

**CAMERA\_SERVICE\_FATAL\_ERROR**: The camera service is abnormal.

 |

#### \[h2\]OH\_CaptureSession\_RegisterSystemPressureLevelChangeCallback()

Camera\_ErrorCode OH\_CaptureSession\_RegisterSystemPressureLevelChangeCallback(Camera\_CaptureSession\* session, OH\_CaptureSession\_OnSystemPressureLevelChange systemPressureLevelChange)

**Description**

Registers a callback to listen for capture system pressure level changes.

**Since**: 20

**Parameters**

| Name | Description |
| :-- | :-- |
| [Camera\_CaptureSession](../../structs/camera-capturesession/document.md)\* session | Pointer to the Camera\_CaptureSession instance that transfers the callback. |
| [OH\_CaptureSession\_OnSystemPressureLevelChange](#oh_capturesession_onsystempressurelevelchange) systemPressureLevelChange | Target callback, which is OH\_CaptureSession\_OnSystemPressureLevelChange. |

**Returns**

| Type | Description |
| :-- | :-- |
| [Camera\_ErrorCode](../camera-h/document.md#camera_errorcode) | 
**CAMERA\_OK**: The operation is successful.

**CAMERA\_INVALID\_ARGUMENT**: A parameter is missing or the parameter type is incorrect.

 |

#### \[h2\]OH\_CaptureSession\_UnregisterSystemPressureLevelChangeCallback()

Camera\_ErrorCode OH\_CaptureSession\_UnregisterSystemPressureLevelChangeCallback(Camera\_CaptureSession\* session, OH\_CaptureSession\_OnSystemPressureLevelChange systemPressureLevelChange)

**Description**

Unregisters the callback used to listen for capture system pressure level changes.

**Since**: 20

**Parameters**

| Name | Description |
| :-- | :-- |
| [Camera\_CaptureSession](../../structs/camera-capturesession/document.md)\* session | Pointer to the Camera\_CaptureSession instance that transfers the callback. |
| [OH\_CaptureSession\_OnSystemPressureLevelChange](#oh_capturesession_onsystempressurelevelchange) systemPressureLevelChange | Target callback, which is OH\_CaptureSession\_OnSystemPressureLevelChange. |

**Returns**

| Type | Description |
| :-- | :-- |
| [Camera\_ErrorCode](../camera-h/document.md#camera_errorcode) | 
**CAMERA\_OK**: The operation is successful.

**CAMERA\_INVALID\_ARGUMENT**: A parameter is missing or the parameter type is incorrect.

 |

#### \[h2\]OH\_CaptureSession\_SetQualityPrioritization()

Camera\_ErrorCode OH\_CaptureSession\_SetQualityPrioritization(Camera\_CaptureSession\* session, Camera\_QualityPrioritization qualityPrioritization)

**Description**

Sets the priority level for video recording quality.

The default value is **HIGH\_QUALITY**. Switching to **POWER\_BALANCE** will compromise video recording quality to achieve lower power usage. The extent of power conservation achieved varies depending on the platform. It is recommended that this API be called between [OH\_CaptureSession\_CommitConfig](#oh_capturesession_commitconfig) and [OH\_CaptureSession\_Start](#oh_capturesession_start).

**Since**: 14

**Parameters**

| Name | Description |
| :-- | :-- |
| [Camera\_CaptureSession](../../structs/camera-capturesession/document.md)\* session | Pointer to the target Camera\_CaptureSession instance. |
| [Camera\_QualityPrioritization](../camera-h/document.md#camera_qualityprioritization) qualityPrioritization | Priority level to set. The default value is **HIGH\_QUALITY**. |

**Returns**

| Type | Description |
| :-- | :-- |
| [Camera\_ErrorCode](../camera-h/document.md#camera_errorcode) | 
**CAMERA\_OK**: The operation is successful.

**CAMERA\_INVALID\_ARGUMENT**: A parameter is missing or the parameter type is incorrect.

**CAMERA\_SESSION\_NOT\_CONFIG**: The capture session is not configured.

 |

#### \[h2\]OH\_CaptureSession\_IsMacroSupported()

Camera\_ErrorCode OH\_CaptureSession\_IsMacroSupported(Camera\_CaptureSession\* session, bool\* isSupported)

**Description**

Checks whether macro photography is supported.

**Since**: 19

**Parameters**

| Name | Description |
| :-- | :-- |
| [Camera\_CaptureSession](../../structs/camera-capturesession/document.md)\* session | Pointer to the target Camera\_CaptureSession instance. |
| bool\* isSupported | Pointer to the check result for the support of macro photography. **true** if supported, **false** otherwise. |

**Returns**

| Type | Description |
| :-- | :-- |
| [Camera\_ErrorCode](../camera-h/document.md#camera_errorcode) | 
**CAMERA\_OK = 0**: The operation is successful.

**CAMERA\_INVALID\_ARGUMENT**: A parameter is missing or the parameter type is incorrect.

**CAMERA\_SESSION\_NOT\_CONFIG**: The capture session is not configured.

 |

#### \[h2\]OH\_CaptureSession\_EnableMacro()

Camera\_ErrorCode OH\_CaptureSession\_EnableMacro(Camera\_CaptureSession\* session, bool enabled)

**Description**

Enables or disables macro photography for the camera device.

**Since**: 19

**Parameters**

| Name | Description |
| :-- | :-- |
| [Camera\_CaptureSession](../../structs/camera-capturesession/document.md)\* session | Pointer to the target Camera\_CaptureSession instance. |
| bool enabled | Whether to enable or disable macro capability. **true** to enable, **false** otherwise. |

**Returns**

| Type | Description |
| :-- | :-- |
| [Camera\_ErrorCode](../camera-h/document.md#camera_errorcode) | 
**CAMERA\_OK = 0**: The operation is successful.

**CAMERA\_INVALID\_ARGUMENT**: A parameter is missing or the parameter type is incorrect.

**CAMERA\_SESSION\_NOT\_CONFIG**: The capture session is not configured.

**CAMERA\_OPERATION\_NOT\_ALLOWED**: The operation is not allowed.

 |

#### \[h2\]OH\_CaptureSession\_SetWhiteBalance()

Camera\_ErrorCode OH\_CaptureSession\_SetWhiteBalance(Camera\_CaptureSession\* session, int32\_t colorTemperature)

**Description**

Sets the white balance color temperature.

Before setting this parameter, you are advised to use [OH\_CaptureSession\_GetWhiteBalanceRange](#oh_capturesession_getwhitebalancerange) to obtain the supported white balance color temperature range.

**Since**: 20

**Parameters**

| Name | Description |
| :-- | :-- |
| [Camera\_CaptureSession](../../structs/camera-capturesession/document.md)\* session | Pointer to the target Camera\_CaptureSession instance. |
| int32\_t colorTemperature | White balance color temperature, in Kelvin. |

**Returns**

| Type | Description |
| :-- | :-- |
| [Camera\_ErrorCode](../camera-h/document.md#camera_errorcode) | 
**CAMERA\_OK**: The setting is successful.

**CAMERA\_INVALID\_ARGUMENT**: A parameter is missing or the parameter type is incorrect.

**CAMERA\_SESSION\_NOT\_CONFIG**: The camera session is not configured.

 |

#### \[h2\]OH\_CaptureSession\_GetWhiteBalance()

Camera\_ErrorCode OH\_CaptureSession\_GetWhiteBalance(Camera\_CaptureSession\* session, int32\_t \*colorTemperature)

**Description**

Obtains the white balance color temperature.

**Since**: 20

**Parameters**

| Name | Description |
| :-- | :-- |
| [Camera\_CaptureSession](../../structs/camera-capturesession/document.md)\* session | Pointer to the target Camera\_CaptureSession instance. |
| int32\_t \*colorTemperature | Pointer to the white balance color temperature, in Kelvin. |

**Returns**

| Type | Description |
| :-- | :-- |
| [Camera\_ErrorCode](../camera-h/document.md#camera_errorcode) | 
**CAMERA\_OK**: The function is successfully called.

**CAMERA\_INVALID\_ARGUMENT**: A parameter is missing or the parameter type is incorrect.

**CAMERA\_SESSION\_NOT\_CONFIG**: The camera session is not configured.

 |

#### \[h2\]OH\_CaptureSession\_GetWhiteBalanceMode()

Camera\_ErrorCode OH\_CaptureSession\_GetWhiteBalanceMode(Camera\_CaptureSession\* session, Camera\_WhiteBalanceMode\* whiteBalanceMode)

**Description**

Obtains the white balance mode in use.

**Since**: 20

**Parameters**

| Name | Description |
| :-- | :-- |
| [Camera\_CaptureSession](../../structs/camera-capturesession/document.md)\* session | Pointer to the target Camera\_CaptureSession instance. |
| [Camera\_WhiteBalanceMode](../camera-h/document.md#camera_whitebalancemode)\* whiteBalanceMode | Pointer to the white balance mode. |

**Returns**

| Type | Description |
| :-- | :-- |
| [Camera\_ErrorCode](../camera-h/document.md#camera_errorcode) | 
**CAMERA\_OK**: The function is successfully called.

**CAMERA\_INVALID\_ARGUMENT**: A parameter is missing or the parameter type is incorrect.

**CAMERA\_SESSION\_NOT\_CONFIG**: The camera session is not configured.

 |

#### \[h2\]OH\_CaptureSession\_IsWhiteBalanceModeSupported()

Camera\_ErrorCode OH\_CaptureSession\_IsWhiteBalanceModeSupported(Camera\_CaptureSession\* session, Camera\_WhiteBalanceMode whiteBalanceMode, bool\* isSupported)

**Description**

Checks whether the specified white balance mode is supported.

**Since**: 20

**Parameters**

| Name | Description |
| :-- | :-- |
| [Camera\_CaptureSession](../../structs/camera-capturesession/document.md)\* session | Pointer to the target Camera\_CaptureSession instance. |
| [Camera\_WhiteBalanceMode](../camera-h/document.md#camera_whitebalancemode) whiteBalanceMode | White balance mode. |
| bool\* isSupported | Pointer to the check result for the support of the specified white balance mode. **true** if supported, **false** otherwise. |

**Returns**

| Type | Description |
| :-- | :-- |
| [Camera\_ErrorCode](../camera-h/document.md#camera_errorcode) | 
**CAMERA\_OK**: The function is successfully called.

**CAMERA\_INVALID\_ARGUMENT**: A parameter is missing or the parameter type is incorrect.

**CAMERA\_SESSION\_NOT\_CONFIG**: The camera session is not configured.

 |

#### \[h2\]OH\_CaptureSession\_SetWhiteBalanceMode()

Camera\_ErrorCode OH\_CaptureSession\_SetWhiteBalanceMode(Camera\_CaptureSession\* session, Camera\_WhiteBalanceMode whiteBalanceMode)

**Description**

Sets a white balance mode.

**Since**: 20

**Parameters**

| Name | Description |
| :-- | :-- |
| [Camera\_CaptureSession](../../structs/camera-capturesession/document.md)\* session | Pointer to the target Camera\_CaptureSession instance. |
| [Camera\_WhiteBalanceMode](../camera-h/document.md#camera_whitebalancemode) whiteBalanceMode | White balance mode. |

**Returns**

| Type | Description |
| :-- | :-- |
| [Camera\_ErrorCode](../camera-h/document.md#camera_errorcode) | 
**CAMERA\_OK**: The setting is successful.

**CAMERA\_INVALID\_ARGUMENT**: A parameter is missing or the parameter type is incorrect.

**CAMERA\_SESSION\_NOT\_CONFIG**: The camera session is not configured.

 |

#### \[h2\]OH\_CaptureSession\_GetWhiteBalanceRange()

Camera\_ErrorCode OH\_CaptureSession\_GetWhiteBalanceRange(Camera\_CaptureSession\* session, int32\_t \*minColorTemperature, int32\_t \*maxColorTemperature)

**Description**

Obtains the supported white balance color temperature range.

**Since**: 20

**Parameters**

| Name | Description |
| :-- | :-- |
| [Camera\_CaptureSession](../../structs/camera-capturesession/document.md)\* session | Pointer to the target Camera\_CaptureSession instance. |
| int32\_t \*minColorTemperature | Pointer to the minimum supported color temperature, in Kelvin. |
| int32\_t \*maxColorTemperature | Pointer to the maximum supported color temperature, in Kelvin. |

**Returns**

| Type | Description |
| :-- | :-- |
| [Camera\_ErrorCode](../camera-h/document.md#camera_errorcode) | 
**CAMERA\_OK**: The function is successfully called.

**CAMERA\_INVALID\_ARGUMENT**: A parameter is missing or the parameter type is incorrect.

**CAMERA\_SESSION\_NOT\_CONFIG**: The camera session is not configured.

 |

#### \[h2\]OH\_CaptureSession\_IsControlCenterSupported()

Camera\_ErrorCode OH\_CaptureSession\_IsControlCenterSupported(Camera\_CaptureSession\* session, bool\* isSupported)

**Description**

Checks whether the camera controller is supported.

**Since**: 20

**Parameters**

| Name | Description |
| :-- | :-- |
| [Camera\_CaptureSession](../../structs/camera-capturesession/document.md)\* session | Pointer to the target Camera\_CaptureSession instance. |
| bool\* isSupported | Pointer to the check result for the support of the camera controller. **true** if supported, **false** otherwise. |

**Returns**

| Type | Description |
| :-- | :-- |
| [Camera\_ErrorCode](../camera-h/document.md#camera_errorcode) | 
**CAMERA\_OK = 0**: The operation is successful.

**CAMERA\_INVALID\_ARGUMENT**: A parameter is missing or the parameter type is incorrect.

**CAMERA\_SESSION\_NOT\_CONFIG**: The capture session is not configured.

 |

#### \[h2\]OH\_CaptureSession\_GetSupportedEffectTypes()

Camera\_ErrorCode OH\_CaptureSession\_GetSupportedEffectTypes(Camera\_CaptureSession\* session, Camera\_ControlCenterEffectType\*\* types, uint32\_t\* size)

**Description**

Obtains the effect types supported by the camera controller.

**Since**: 20

**Parameters**

| Name | Description |
| :-- | :-- |
| [Camera\_CaptureSession](../../structs/camera-capturesession/document.md)\* session | Pointer to the target Camera\_CaptureSession instance. |
| [Camera\_ControlCenterEffectType](../camera-h/document.md#camera_controlcentereffecttype)\*\* types | Double pointer to the list of supported effect types, which are defined in the Camera\_ControlCenterEffectType struct, if the function is successfully called. |
| uint32\_t\* size | Pointer to the size of the list of supported effect types. |

**Returns**

| Type | Description |
| :-- | :-- |
| [Camera\_ErrorCode](../camera-h/document.md#camera_errorcode) | 
**CAMERA\_OK**: The operation is successful.

**CAMERA\_INVALID\_ARGUMENT**: A parameter is missing or the parameter type is incorrect.

**CAMERA\_SESSION\_NOT\_CONFIG**: The capture session is not configured.

 |

#### \[h2\]OH\_CaptureSession\_DeleteSupportedEffectTypes()

Camera\_ErrorCode OH\_CaptureSession\_DeleteSupportedEffectTypes(Camera\_CaptureSession\* session, Camera\_ControlCenterEffectType\* types, uint32\_t size)

**Description**

Deletes the effect types supported by the camera controller.

**Since**: 20

**Parameters**

| Name | Description |
| :-- | :-- |
| [Camera\_CaptureSession](../../structs/camera-capturesession/document.md)\* session | Pointer to the target Camera\_CaptureSession instance. |
| [Camera\_ControlCenterEffectType](../camera-h/document.md#camera_controlcentereffecttype)\* types | Pointer to the list of effect types, which are defined in the Camera\_ControlCenterEffectType struct. |
| uint32\_t size | Size of the list of supported effect types. |

**Returns**

| Type | Description |
| :-- | :-- |
| [Camera\_ErrorCode](../camera-h/document.md#camera_errorcode) | 
**CAMERA\_OK**: The operation is successful.

**CAMERA\_INVALID\_ARGUMENT**: A parameter is missing or the parameter type is incorrect.

 |

#### \[h2\]OH\_CaptureSession\_EnableControlCenter()

Camera\_ErrorCode OH\_CaptureSession\_EnableControlCenter(Camera\_CaptureSession\* session, bool enabled)

**Description**

Enables or disables the camera controller.

**Since**: 20

**Parameters**

| Name | Description |
| :-- | :-- |
| [Camera\_CaptureSession](../../structs/camera-capturesession/document.md)\* session | Pointer to the target Camera\_CaptureSession instance. |
| bool enabled | Whether to enable the camera controller. **true** to enable, **false** otherwise. |

**Returns**

| Type | Description |
| :-- | :-- |
| [Camera\_ErrorCode](../camera-h/document.md#camera_errorcode) | 
**CAMERA\_OK = 0**: The operation is successful.

**CAMERA\_INVALID\_ARGUMENT**: A parameter is missing or the parameter type is incorrect.

**CAMERA\_SESSION\_NOT\_CONFIG**: The capture session is not configured.

**CAMERA\_SERVICE\_FATAL\_ERROR**: The camera service is abnormal.

 |

#### \[h2\]OH\_CaptureSession\_RegisterControlCenterEffectStatusChangeCallback()

Camera\_ErrorCode OH\_CaptureSession\_RegisterControlCenterEffectStatusChangeCallback(Camera\_CaptureSession\* session, OH\_CaptureSession\_OnControlCenterEffectStatusChange controlCenterEffectStatusChange)

**Description**

Registers a callback to listen for effect status changes of a camera controller.

**Since**: 20

**Parameters**

| Name | Description |
| :-- | :-- |
| [Camera\_CaptureSession](../../structs/camera-capturesession/document.md)\* session | Pointer to the Camera\_CaptureSession instance that transfers the callback. |
| [OH\_CaptureSession\_OnControlCenterEffectStatusChange](#oh_capturesession_oncontrolcentereffectstatuschange) controlCenterEffectStatusChange | Target callback, which is OH\_CaptureSession\_OnControlCenterEffectStatusChange. |

**Returns**

| Type | Description |
| :-- | :-- |
| [Camera\_ErrorCode](../camera-h/document.md#camera_errorcode) | 
**CAMERA\_OK**: The operation is successful.

**CAMERA\_INVALID\_ARGUMENT**: A parameter is missing or the parameter type is incorrect.

 |

#### \[h2\]OH\_CaptureSession\_UnregisterControlCenterEffectStatusChangeCallback()

Camera\_ErrorCode OH\_CaptureSession\_UnregisterControlCenterEffectStatusChangeCallback(Camera\_CaptureSession\* session, OH\_CaptureSession\_OnControlCenterEffectStatusChange controlCenterEffectStatusChange)

**Description**

Unregisters the callback used to listen for effect status changes of a camera controller.

**Since**: 20

**Parameters**

| Name | Description |
| :-- | :-- |
| [Camera\_CaptureSession](../../structs/camera-capturesession/document.md)\* session | Pointer to the Camera\_CaptureSession instance that transfers the callback. |
| [OH\_CaptureSession\_OnControlCenterEffectStatusChange](#oh_capturesession_oncontrolcentereffectstatuschange) controlCenterEffectStatusChange | Target callback, which is OH\_CaptureSession\_OnControlCenterEffectStatusChange. |

**Returns**

| Type | Description |
| :-- | :-- |
| [Camera\_ErrorCode](../camera-h/document.md#camera_errorcode) | 
**CAMERA\_OK**: The operation is successful.

**CAMERA\_INVALID\_ARGUMENT**: A parameter is missing or the parameter type is incorrect.

 |

#### \[h2\]OH\_CaptureSession\_OnMacroStatusChange()

 typedef void (\*OH\_CaptureSession\_OnMacroStatusChange)(Camera\_CaptureSession\* session, bool isMacroDetected)

**Description**

Defines the callback used to listen for macro status changes of a camera session.

**Since**: 20

**Parameters**

| Name | Description |
| :-- | :-- |
| [Camera\_CaptureSession](../../structs/camera-capturesession/document.md)\* session | Pointer to the Camera\_CaptureSession instance. |
| bool isMacroDetected | Whether the camera is in macro mode. **true** if the camera is in macro mode, **false** otherwise. |

#### \[h2\]OH\_CaptureSession\_RegisterMacroStatusChangeCallback()

 Camera\_ErrorCode OH\_CaptureSession\_RegisterMacroStatusChangeCallback(Camera\_CaptureSession\* session, OH\_CaptureSession\_OnMacroStatusChange macroStatusChange)

**Description**

Registers a callback to listen for macro status changes of a camera session.

**Since**: 20

**Parameters**

| Name | Description |
| :-- | :-- |
| [Camera\_CaptureSession](../../structs/camera-capturesession/document.md)\* session | Pointer to the Camera\_CaptureSession instance. |
| [OH\_CaptureSession\_OnMacroStatusChange](#oh_capturesession_onmacrostatuschange) macroStatusChange | Callback used to return the macro status change. |

**Returns**

| Type | Description |
| :-- | :-- |
| [Camera\_ErrorCode](../camera-h/document.md#camera_errorcode) | 
**CAMERA\_OK**: The operation is successful.

**CAMERA\_INVALID\_ARGUMENT**: A parameter is missing or the parameter type is incorrect.

 |

#### \[h2\]OH\_CaptureSession\_UnregisterMacroStatusChangeCallback()

 Camera\_ErrorCode OH\_CaptureSession\_UnregisterMacroStatusChangeCallback(Camera\_CaptureSession\* session, OH\_CaptureSession\_OnMacroStatusChange macroStatusChange)

**Description**

Unregisters the callback used to listen for macro status changes of a camera session.

**Since**: 20

**Parameters**

| Name | Description |
| :-- | :-- |
| [Camera\_CaptureSession](../../structs/camera-capturesession/document.md)\* session | Pointer to the Camera\_CaptureSession instance. |
| [OH\_CaptureSession\_OnMacroStatusChange](#oh_capturesession_onmacrostatuschange) macroStatusChange | Callback used to return the macro status change. |

**Returns**

| Type | Description |
| :-- | :-- |
| [Camera\_ErrorCode](../camera-h/document.md#camera_errorcode) | 
**CAMERA\_OK**: The operation is successful.

**CAMERA\_INVALID\_ARGUMENT**: A parameter is missing or the parameter type is incorrect.

 |

#### \[h2\]OH\_CaptureSession\_OnIsoChange()

typedef void (\*OH\_CaptureSession\_OnIsoChange)(Camera\_CaptureSession\* session, int32\_t isoValue)

**Description**

Defines the callback used to listen for ISO changes in a camera session.

**Since**: 22

**Parameters**

| Name | Description |
| :-- | :-- |
| [Camera\_CaptureSession](../../structs/camera-capturesession/document.md)\* session | Pointer to the **Camera\_CaptureSession** instance. |
| int32\_t isoValue | ISO value obtained in the callback. |

#### \[h2\]OH\_CaptureSession\_RegisterIsoChangeCallback()

Camera\_ErrorCode OH\_CaptureSession\_RegisterIsoChangeCallback(Camera\_CaptureSession\* session, OH\_CaptureSession\_OnIsoChange isoChange)

**Description**

Registers a callback to listen for ISO changes.

**Since**: 22

**Parameters**

| Name | Description |
| :-- | :-- |
| [Camera\_CaptureSession](../../structs/camera-capturesession/document.md)\* session | Pointer to the Camera\_CaptureSession instance. |
| [OH\_CaptureSession\_OnIsoChange](#oh_capturesession_onisochange) isoChange | Callback of the **OH\_CaptureSession\_OnIsoChange** type, which is used to listen for ISO changes. |

**Returns**

| Type | Description |
| :-- | :-- |
| [Camera\_ErrorCode](../camera-h/document.md#camera_errorcode) | 
**CAMERA\_OK**: The operation is successful.

**CAMERA\_INVALID\_ARGUMENT**: A parameter is missing or the parameter type is incorrect.

 |

#### \[h2\]OH\_CaptureSession\_UnregisterIsoChangeCallback()

Camera\_ErrorCode OH\_CaptureSession\_UnregisterIsoChangeCallback(Camera\_CaptureSession\* session, OH\_CaptureSession\_OnIsoChange isoChange)

**Description**

Unregisters the callback used to listen for ISO changes.

**Since**: 22

**Parameters**

| Name | Description |
| :-- | :-- |
| [Camera\_CaptureSession](../../structs/camera-capturesession/document.md)\* session | Pointer to the Camera\_CaptureSession instance. |
| [OH\_CaptureSession\_OnIsoChange](#oh_capturesession_onisochange) isoChange | Callback of the **OH\_CaptureSession\_OnIsoChange** type, which is used to listen for ISO changes. |

**Returns**

| Type | Description |
| :-- | :-- |
| [Camera\_ErrorCode](../camera-h/document.md#camera_errorcode) | 
**CAMERA\_OK**: The operation is successful.

**CAMERA\_INVALID\_ARGUMENT**: A parameter is missing or the parameter type is incorrect.

 |
