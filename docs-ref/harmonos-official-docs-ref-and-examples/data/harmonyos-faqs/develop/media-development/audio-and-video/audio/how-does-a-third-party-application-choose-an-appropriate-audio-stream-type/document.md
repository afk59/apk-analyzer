# How does a third-party application choose an appropriate audio stream type?

The type of audio stream is determined by **StreamUsage** for playback streams and by **SourceType** for recording streams.

The audio stream type significantly affects volume control, audio focus management, and the selection of input/output devices.

Applications should select the appropriate audio stream type based on their specific service scenarios and requirements.

WebView policy: Currently, manually setting the audio stream type is not supported. WebView automatically assigns the stream type based on whether there is audio input. If there is a playback stream but no recording stream, it defaults to the Music type. If there are both playback and recording streams, it defaults to the VoiceCommunication type.

**Reference**

[Selecting an Appropriate Audio Stream Type](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/using-right-streamusage-and-sourcetype)
