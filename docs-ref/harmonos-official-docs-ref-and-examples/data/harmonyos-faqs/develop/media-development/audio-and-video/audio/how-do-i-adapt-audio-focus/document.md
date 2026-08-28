# How do I adapt audio focus?

To provide a seamless audio focus experience, applications should consider the following:

(1) Before starting playback or recording, applications must correctly specify **StreamUsage** or **SourceType** based on the audio usage.

(2) Applications should listen for audio focus events and take appropriate actions when receiving an InterruptEvent.

(3) For more control over audio focus, applications can use the AudioSession APIs to manage audio focus proactively.

**Reference**

[Introduction to Audio Focus and Audio Session](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/audio-playback-concurrency)

[Audio Playback Interaction](https://developer.huawei.com/consumer/en/doc/best-practices/bpta-audio-interaction-practice)
