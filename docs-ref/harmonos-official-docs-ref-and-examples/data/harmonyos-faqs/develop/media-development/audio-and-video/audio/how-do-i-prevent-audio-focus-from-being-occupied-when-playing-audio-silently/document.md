# How do I prevent audio focus from being occupied when playing audio silently?

If an application plays audio (or video) in silent mode and wants to ensure that this does not interfere with other audio streams, it can delay requesting audio focus until the silent mode is turned off. To achieve this, you can use the following approaches depending on the audio playback development mode:

-   For [audio playback using AVPlayer (ArkTS)](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/using-avplayer-for-playback), call the [setMediaMuted](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-media-avplayer#setmediamuted12) function.
-   For [audio playback using AudioRenderer](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/using-audiorenderer-for-playback), call the [setSilentModeAndMixWithOthers](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-audio-audiorenderer#setsilentmodeandmixwithothers12) function.
-   For audio playback using WebView, set the audio stream volume to **0** before playback. This allows the system to play the audio concurrently with other streams. Audio focus will be requested only when the audio stream is unmuted.
