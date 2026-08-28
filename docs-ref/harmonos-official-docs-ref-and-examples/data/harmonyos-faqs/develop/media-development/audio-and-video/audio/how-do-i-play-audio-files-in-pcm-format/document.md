# How do I play audio files in PCM format?

**Symptom**

An error occurs when **AVPlayer** is used to play PCM-format audio files recorded by **AudioCapturer**.

**Possible Causes**

**AVPlayer** does not support direct playback of files in PCM format.

**Solution**

-   [AudioRenderer](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/using-audiorenderer-for-playback): an ArkTS/JS API for audio output that only supports the PCM format. The application needs to continuously write audio data. The applications can perform data preprocessing, for example, setting the sampling rate and bit width of audio files, before audio input. This class can be used to develop more professional and diverse playback applications. To use this class, you must have basic audio processing knowledge.
-   [OHAudio](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/using-ohaudio-for-playback): a native API for audio output. This API is normalized in design and supports both common and low-latency audio channels. They support the PCM format only and are suitable for playback applications that implement audio output at the native layer.
