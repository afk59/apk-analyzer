# What should I do if recording succeeded but the playback effect did not meet expectations?

**Symptom**

The recording succeeded, but the playback effect is not as expected.

**Possible Causes**

1.  The screen of the mobile phone or computer is locked during recording or playback.
2.  The project bundle name during recording is the same as that during playback, but the source code is different. As a result, the component layout is incorrect.

**Solution**

1.  Currently, the recording playback function does not support any screen-off operations on the mobile phone. The Windows system on the computer supports playback after the screen is locked, while macOS does not. Ensure that your phone is unlocked and the screen is on. Otherwise, the playback function will be affected.
2.  Ensure that the bundle name and source code of the project are the same during recording and playback.
