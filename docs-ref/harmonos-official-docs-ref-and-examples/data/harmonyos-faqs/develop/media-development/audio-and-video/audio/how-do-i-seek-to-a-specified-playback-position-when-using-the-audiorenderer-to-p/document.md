# How do I seek to a specified playback position when using the AudioRenderer to play audio?

**Possible Causes**

Seeking is one of the features of the player. However, **AudioRenderer** is mainly used for audio rendering and playback, and does not provide the seeking API.

**Solution**

When **AudioRenderer** registers **writeDataCallback**, the new offset position is calculated based on the seeking timestamp. When the audio data is read next time, the audio data is read from the new offset position, and the audio can be played from the specified position.
