# How do I disable the camera?

Refer to the sample code below:

// Stop the current session
  photoSession.stop();

// Release camera input stream
  cameraInput.close();

// Release preview output stream
  previewOutput.release();

// Release the photo output stream
  photoOutput.release();

// Release session
  photoSession.release();

// Session left blank
  photoSession = undefined;

**Reference**

[Photo Capture Practices (ArkTS)](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/camera-shooting-case)
