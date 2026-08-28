# OH\_AudioDeviceDescriptorArray

typedef struct OH\_AudioDeviceDescriptorArray {...} OH\_AudioDeviceDescriptorArray

#### Overview

The struct describes an array of audio device descriptors.

**Since**: 12

**Related module**: [OHAudio](../../modules/ohaudio/document.md)

**Header file**: [native\_audio\_device\_base.h](../../header-files/native-audio-device-base-h/document.md)

#### Summary

#### \[h2\]Member Variables

| Name | Description |
| :-- | :-- |
| uint32\_t size | Size of the audio device descriptor array. |
| [OH\_AudioDeviceDescriptor](../oh-audiodevicedescriptor/document.md)\*\* descriptors | Double pointer to the audio device descriptors in the array. |
