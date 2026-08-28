# What should I do if there is no pause after device switchover?

-   To ensure a seamless user experience when there are changes in the audio output device, it is crucial to listen for such changes and adapt accordingly. You can use [outputDeviceChangeWithInfo](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-audio-audiorenderer#onoutputdevicechangewithinfo11) of **AudioRenderer** to listen for audio output device changes and obtain the change reason. When the audio output device is changed due to the online/offline status change, forcible user selection, device preemption, or device selection policy change, the system uses this API to notify the application of the change, including the audio output device information and change reason.
-   WebView policy: If an application has its own playback button UI, it must monitor the video playback status to refresh the UI accordingly.

**Reference**

[Handling Output Device Changes Gracefully](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/audio-output-device-change)
