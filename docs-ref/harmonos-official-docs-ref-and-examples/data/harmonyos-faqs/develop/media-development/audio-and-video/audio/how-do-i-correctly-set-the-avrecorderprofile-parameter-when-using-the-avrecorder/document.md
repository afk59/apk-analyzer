# How do I correctly set the AVRecorderProfile parameter when using the AVRecorder to record audio files in WAV format?

**Symptom**

An error occurs when the **AVRecorder** is used to record audio files in WAV format.

**Possible Causes**

The **AVRecorderProfile** parameter is incorrectly configured. For the WAV format, it is required to match the corresponding bit rate, number of audio channels, encoding format, sampling rate, and encapsulation format.

**Solution**

Configure the bit rate, number of audio channels, encoding format, sampling rate, and encapsulation format for [AVRecorderProfile](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-media-i#avrecorderprofile9).

private avProfile: media.AVRecorderProfile = {
  audioBitrate: 64000, // set audioBitrate according to device ability.
  audioChannels: 1, // set audioChannels,valid value 1-8,CFT\_WAV supports 1.
  audioCodec: media.CodecMimeType.AUDIO\_G711MU, // set audioCodec,AUDIO\_G711MU matching CFT\_WAV.
  audioSampleRate: 8000, // set audioSampleRate according to device ability.
  fileFormat: media.ContainerFormatType.CFT\_WAV // set fileFormat,CFT\_WAV.
}
