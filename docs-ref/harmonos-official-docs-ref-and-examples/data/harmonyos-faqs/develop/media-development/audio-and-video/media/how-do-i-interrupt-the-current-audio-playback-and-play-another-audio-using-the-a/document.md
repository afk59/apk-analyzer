# How do I interrupt the current audio playback and play another audio using the AVPlayer?

Call [reset()](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-media-avplayer#reset9) to interrupt the current audio, and then switch the audio source. Because **reset()** is asynchronous, add **await** in the **reset()** statement.
