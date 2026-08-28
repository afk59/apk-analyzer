# Does AudioRenderer provide an API for seeking to a frame?

The bottom layer of AudioRenderer does not support seeking to a specific frame. AudioRenderer starts playing after obtaining data proactively sent from the client. AvPlayer has a source, for example, a file, and therefore it supports frame seeking. You can use the **avPlayer.seek()** API to seek to the specified playback position. This API can be called only when the AVPlayer is in the prepared, playing, paused, or completed state.

let seekTime: number = 1000
avPlayer.seek(seekTime,media.SeekMode.SEEK\_PREV\_SYNC)

**Reference**

[seek](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-media-avplayer#seek9)
