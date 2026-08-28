# What should I do if some videos cannot be played properly on the Emulator?

**Symptom**

When the Emulator is playing a video, sometimes the video has sound but no image, or frame freezing occurs.

**Solution**

The Emulator supports only RGBA pixel display, so ensure that the video decoding format is correct. In addition, the Emulator supports only software decoding. If the video decoder depends on hardware decoding, the video may fail to be played properly.
