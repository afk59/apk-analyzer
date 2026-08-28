# OH\_EqualizerFrequencyBandGains

typedef struct {...} OH\_EqualizerFrequencyBandGains

#### Overview

The struct describes the configuration parameters for the equalizer effect node used in audio creation.

**Since**: 22

**Related module**: [OHAudioSuite](../../modules/ohaudiosuite/document.md)

**Header file**: [native\_audio\_suite\_base.h](../../header-files/native-audio-suite-base-h/document.md)

#### Summary

#### \[h2\]Member Variables

| Name | Description |
| :-- | :-- |
| int32\_t gains\[EQUALIZER\_BAND\_NUM\] | 
Settings for the equalizer band gains. The value of **EQUALIZER\_BAND\_NUM** is **10**, with each gain value ranging from -10 to 10 dB.

Frequency bands: 31 Hz, 62 Hz, 125 Hz, 250 Hz, 500 Hz, 1 kHz, 2 kHz, 4 kHz, 8 kHz, and 16 kHz.

**Since**: 22

 |
