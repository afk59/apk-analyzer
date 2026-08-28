# How do I turn on/off the flash?

Use [isFlashModeSupported](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-camera-flashquery#isflashmodesupported11) to check whether a flash mode is supported, and then use [setFlashMode](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-camera-flash#setflashmode11) to set the flash mode.

Refer to the code snippet below.

setFlash(captureSession: camera.PhotoSession,flashMode: camera.FlashMode) {
  if (captureSession != null) {
    let focusModeStatus: boolean = captureSession?.isFlashModeSupported(flashMode);
    if (focusModeStatus) {
      captureSession.setFlashMode(flashMode);
    }
  }
}
