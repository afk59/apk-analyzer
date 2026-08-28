# Pressure Management (C/C++)

Starting from API version 20, the camera framework supports monitoring of system pressure levels.

In scenarios requiring prolonged camera usage (such as live streaming), applications can dynamically adjust image quality parameters (such as the frame rate or resolution) based on system pressure level changes. This helps balance power consumption, heat generation, and system load, ensuring stable and extended camera functionality.

#### Status Listening

To monitor system pressure status changes, register the [OH\_CaptureSession\_OnSystemPressureLevelChange](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-capture-session-h#oh_capturesession_onsystempressurelevelchange) callback.

When the system pressure level changes, the callback returns the **Camera\_SystemPressureLevel** parameter.

For details about this parameter, see [Camera\_SystemPressureLevel](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-camera-h#camera_systempressurelevel).

void SystemPressureLevelChangeCallback(Camera\_CaptureSession \*captureSession,
    Camera\_SystemPressureLevel systemPressureLevel)
{
    OH\_LOG\_INFO(LOG\_APP, "SystemPressureLevelChangeCallback level: %{public}d", systemPressureLevel);
}

Camera\_ErrorCode NDKCamera::RegisterSystemPressureCallback()
{
    Camera\_ErrorCode ret = OH\_CaptureSession\_RegisterSystemPressureLevelChangeCallback(
        captureSession\_, SystemPressureLevelChangeCallback);
    if (ret != CAMERA\_OK) {
        OH\_LOG\_ERROR(LOG\_APP,
            "OH\_CaptureSession\_RegisterSystemPressureLevelChangeCallback failed.");
    }
    return ret;
}
