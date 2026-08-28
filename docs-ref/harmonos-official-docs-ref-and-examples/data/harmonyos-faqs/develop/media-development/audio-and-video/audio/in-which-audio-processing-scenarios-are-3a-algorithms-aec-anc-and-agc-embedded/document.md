# In which audio processing scenarios are 3A algorithms (AEC, ANC, and AGC) embedded?

The 3A algorithm refers to three audio processing algorithms: Acoustic Echo Cancellation (AEC), Active Noise Control (ANC), and Automatic Gain Control (AGC).

The 3A processing is automatically enabled for the audio stream with the **STREAM\_USAGE\_VOICE\_COMMUNICATION** configuration. In common recording scenarios, 3A is not enabled. It is enabled only for VoIP calls. You need to configure the corresponding **StreamUsage** type when playing audio streams.

**Reference**

[AudioCapturer](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-audio-audiocapturer)
