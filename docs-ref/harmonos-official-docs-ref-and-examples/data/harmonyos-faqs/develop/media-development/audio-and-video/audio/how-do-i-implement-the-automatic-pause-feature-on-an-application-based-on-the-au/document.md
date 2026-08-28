# How do I implement the automatic pause feature on an application based on the audio output device change information?

**Symptom**

When **audioRoutingManager.on('deviceChange')** is used to listen for the device change information, the application automatically pauses during normal playback.

**Possible Causes**

**audioRoutingManager.on('deviceChange')** is used to listen for the connection status changes of global input and output devices, not bound to audio streams. Therefore, you are not advised to implement the automatic pause feature based on this API.

**Solution**

You can use [audioRenderer.on('outputDeviceChangeWithInfo')](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-audio-audiorenderer#onoutputdevicechangewithinfo11) to listen for the audio output device changes and the causes. When the audio output device is changed due to the online/offline status change, forcible user selection, device preemption, or device selection policy change, the system uses this API to notify the application of the change, including the audio output device information and change reason. The application can process services based on the change reason. For details, see [Device Change Reason](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/audio-output-device-change#device-change-reason).
