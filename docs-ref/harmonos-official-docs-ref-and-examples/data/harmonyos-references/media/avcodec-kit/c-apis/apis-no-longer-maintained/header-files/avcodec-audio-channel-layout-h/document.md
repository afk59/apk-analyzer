# avcodec\_audio\_channel\_layout.h

#### Overview

The file declares the enums used for audio codec channel layouts.

**File to include**: <multimedia/player\_framework/avcodec\_audio\_channel\_layout.h>

**Library**: libnative\_media\_codecbase.so

**System capability**: SystemCapability.Multimedia.Media.CodecBase

**Since**: 10

**Deprecated from**: 11

**Related module**: [CodecBase](../../../modules/codecbase/document.md)

#### Summary

#### \[h2\]Enums

| Name | Description |
| :-- | :-- |
| [AudioChannelSet](#audiochannelset) | Enumerates the audio channels. Each channel is mapped to a variable of int64. (It is deprecated from API version 11.) |
| [AudioChannelLayout](#audiochannellayout) | Enumerates the layouts of audio channels. The output format of the decoder is described using the channel layout of the codec. (It is deprecated from API version 11.) |

#### Enum Description

#### \[h2\]AudioChannelSet

enum AudioChannelSet : uint64\_t

**Description**

Enumerates the audio channels. Each channel is mapped to a variable of int64.

**System capability**: SystemCapability.Multimedia.Media.CodecBase

**Since**: 10

**Deprecated from**: 11

**Substitute**: [OH\_AudioChannelSet](../../../header-files/native-audio-channel-layout-h/document.md#oh_audiochannelset)

| Value | Description |
| :-- | :-- |
| FRONT\_LEFT = 1ULL << 0U | Front left channel. |
| FRONT\_RIGHT = 1ULL << 1U | Front right channel. |
| FRONT\_CENTER = 1ULL << 2U | Front center channel. |
| LOW\_FREQUENCY = 1ULL << 3U | Low-frequency channel. |
| BACK\_LEFT = 1ULL << 4U | Rear left channel. |
| BACK\_RIGHT = 1ULL << 5U | Rear right channel. |
| FRONT\_LEFT\_OF\_CENTER = 1ULL << 6U | Front left center channel. |
| FRONT\_RIGHT\_OF\_CENTER = 1ULL << 7U | Front right center channel. |
| BACK\_CENTER = 1ULL << 8U | Rear center channel. |
| SIDE\_LEFT = 1ULL << 9U | Left channel. |
| SIDE\_RIGHT = 1ULL << 10U | Right channel. |
| TOP\_CENTER = 1ULL << 11U | Top center channel. |
| TOP\_FRONT\_LEFT = 1ULL << 12U | Top left front channel. |
| TOP\_FRONT\_CENTER = 1ULL << 13U | Top center front channel. |
| TOP\_FRONT\_RIGHT = 1ULL << 14U | Top right front channel. |
| TOP\_BACK\_LEFT = 1ULL << 15U | Top left rear channel. |
| TOP\_BACK\_CENTER = 1ULL << 16U | Top center rear channel. |
| TOP\_BACK\_RIGHT = 1ULL << 17U | Top right rear channel. |
| STEREO\_LEFT = 1ULL << 29U | Stereo left channel. |
| STEREO\_RIGHT = 1ULL << 30U | Stereo right channel. |
| WIDE\_LEFT = 1ULL << 31U | Wide left channel. |
| WIDE\_RIGHT = 1ULL << 32U | Wide right channel. |
| SURROUND\_DIRECT\_LEFT = 1ULL << 33U | Left surround channel. |
| SURROUND\_DIRECT\_RIGHT = 1ULL << 34U | Right surround channel. |
| LOW\_FREQUENCY\_2 = 1ULL << 35U | Low-frequency channel 2. |
| TOP\_SIDE\_LEFT = 1ULL << 36U | Top left channel. |
| TOP\_SIDE\_RIGHT = 1ULL << 37U | Top right channel. |
| BOTTOM\_FRONT\_CENTER = 1ULL << 38U | Bottom center front channel. |
| BOTTOM\_FRONT\_LEFT = 1ULL << 39U | Bottom left front channel. |
| BOTTOM\_FRONT\_RIGHT = 1ULL << 40U | Bottom right front channel. |
| AMBISONICS\_ACN0 = 1ULL << 41U | Channel 0 for the zero-order stereo. |
| AMBISONICS\_ACN1 = 1ULL << 42U | Channel 1 for the first-order stereo. |
| AMBISONICS\_ACN2 = 1ULL << 43U | Channel 2 for the first-order stereo. |
| AMBISONICS\_ACN3 = 1ULL << 44U | Channel 3 for the first-order stereo. |
| AMBISONICS\_W = AMBISONICS\_ACN0 | Equivalent to channel 0 for the zero-order stereo. |
| AMBISONICS\_Y = AMBISONICS\_ACN1 | Equivalent to channel 1 for the first-order stereo. |
| AMBISONICS\_Z = AMBISONICS\_ACN2 | Equivalent to channel 2 for the first-order stereo. |
| AMBISONICS\_X = AMBISONICS\_ACN3 | Equivalent to channel 3 for the first-order stereo. |
| AMBISONICS\_ACN4 = 1ULL << 45U | Channel 4 for the second-order stereo. |
| AMBISONICS\_ACN5 = 1ULL << 46U | Channel 5 for the second-order stereo. |
| AMBISONICS\_ACN6 = 1ULL << 47U | Channel 6 for the second-order stereo. |
| AMBISONICS\_ACN7 = 1ULL << 48U | Channel 7 for the second-order stereo. |
| AMBISONICS\_ACN8 = 1ULL << 49U | Channel 8 for the second-order stereo. |
| AMBISONICS\_ACN9 = 1ULL << 50U | Channel 9 for the third-order stereo. |
| AMBISONICS\_ACN10 = 1ULL << 51U | Channel 10 for the third-order stereo. |
| AMBISONICS\_ACN11 = 1ULL << 52U | Channel 11 for the third-order stereo. |
| AMBISONICS\_ACN12 = 1ULL << 53U | Channel 12 for the third-order stereo. |
| AMBISONICS\_ACN13 = 1ULL << 54U | Channel 13 for the third-order stereo. |
| AMBISONICS\_ACN14 = 1ULL << 55U | Channel 14 for the third-order stereo. |
| AMBISONICS\_ACN15 = 1ULL << 56U | Channel 15 for the third-order stereo. |

#### \[h2\]AudioChannelLayout

enum AudioChannelLayout : uint64\_t

**Description**

Enumerates the layouts of audio channels. The output format of the decoder is described using the channel layout of the codec.

**System capability**: SystemCapability.Multimedia.Media.CodecBase

**Since**: 10

**Deprecated from**: 11

**Substitute**: [OH\_AudioChannelLayout](../../../header-files/native-audio-channel-layout-h/document.md#oh_audiochannellayout)

| Value | Description |
| :-- | :-- |
| UNKNOWN\_CHANNEL\_LAYOUT = 0 | Unknown. |
| MONO = (AudioChannelSet::FRONT\_CENTER) | Mono layout. |
| STEREO = (AudioChannelSet::FRONT\_LEFT | AudioChannelSet::FRONT\_RIGHT) | Stereo layout. |
| CH\_2POINT1 = (STEREO | AudioChannelSet::LOW\_FREQUENCY) | 2.1 layout. |
| CH\_2\_1 = (STEREO | AudioChannelSet::BACK\_CENTER) | 2\_1 layout. |
| SURROUND = (STEREO | AudioChannelSet::FRONT\_CENTER) | Surround layout. |
| CH\_3POINT1 = (SURROUND | AudioChannelSet::LOW\_FREQUENCY) | 3.1 layout. |
| CH\_4POINT0 = (SURROUND | AudioChannelSet::BACK\_CENTER) | 4.0 layout. |
| CH\_4POINT1 = (CH\_4POINT0 | AudioChannelSet::LOW\_FREQUENCY) | 4.1 layout. |
| CH\_2\_2 = (STEREO | AudioChannelSet::SIDE\_LEFT | AudioChannelSet::SIDE\_RIGHT) | 2\_2 layout. |
| QUAD = (STEREO | AudioChannelSet::BACK\_LEFT | AudioChannelSet::BACK\_RIGHT) | Quad layout. |
| CH\_5POINT0 = (SURROUND | AudioChannelSet::SIDE\_LEFT | AudioChannelSet::SIDE\_RIGHT) | 5.0 layout. |
| CH\_5POINT1 = (CH\_5POINT0 | AudioChannelSet::LOW\_FREQUENCY) | 5.1 layout. |
| CH\_5POINT0\_BACK = (SURROUND | AudioChannelSet::BACK\_LEFT | AudioChannelSet::BACK\_RIGHT) | 5.0 rear layout. |
| CH\_5POINT1\_BACK = (CH\_5POINT0\_BACK | AudioChannelSet::LOW\_FREQUENCY) | 5.1 rear layout. |
| CH\_6POINT0 = (CH\_5POINT0 | AudioChannelSet::BACK\_CENTER) | 6.0 layout. |
| CH\_6POINT0\_FRONT = (CH\_2\_2 | AudioChannelSet::FRONT\_LEFT\_OF\_CENTER | AudioChannelSet::FRONT\_RIGHT\_OF\_CENTER) | 6.0 front layout. |
| HEXAGONAL = (CH\_5POINT0\_BACK | AudioChannelSet::BACK\_CENTER) | Hexagonal layout. |
| CH\_6POINT1 = (CH\_5POINT1 | AudioChannelSet::BACK\_CENTER) | 6.1 layout. |
| CH\_6POINT1\_BACK = (CH\_5POINT1\_BACK | AudioChannelSet::BACK\_CENTER) | 6.1 rear layout. |
| CH\_6POINT1\_FRONT = (CH\_6POINT0\_FRONT | AudioChannelSet::LOW\_FREQUENCY) | 6.1 front layout. |
| CH\_7POINT0 = (CH\_5POINT0 | AudioChannelSet::BACK\_LEFT | AudioChannelSet::BACK\_RIGHT) | 7.0 layout. |
| CH\_7POINT0\_FRONT = (CH\_5POINT0 | AudioChannelSet::FRONT\_LEFT\_OF\_CENTER | AudioChannelSet::FRONT\_RIGHT\_OF\_CENTER) | 7.0 front layout. |
| CH\_7POINT1 = (CH\_5POINT1 | AudioChannelSet::BACK\_LEFT | AudioChannelSet::BACK\_RIGHT) | 7.1 layout. |
| CH\_7POINT1\_WIDE = (CH\_5POINT1 | AudioChannelSet::FRONT\_LEFT\_OF\_CENTER | AudioChannelSet::FRONT\_RIGHT\_OF\_CENTER) | 7.1 wide layout. |
| CH\_7POINT1\_WIDE\_BACK = | 7.1 rear wide layout. |
| CH\_3POINT1POINT2 = (CH\_3POINT1 | AudioChannelSet::TOP\_FRONT\_LEFT | AudioChannelSet::TOP\_FRONT\_RIGHT) | 3.1.2 layout. |
| CH\_5POINT1POINT2 = (CH\_5POINT1 | AudioChannelSet::TOP\_SIDE\_LEFT | AudioChannelSet::TOP\_SIDE\_RIGHT) | 5.1.2 layout. |
| (CH\_5POINT1 | AudioChannelSet::TOP\_FRONT\_LEFT | AudioChannelSet::TOP\_FRONT\_RIGHT |AudioChannelSet::TOP\_BACK\_LEFT | AudioChannelSet::TOP\_BACK\_RIGHT) | 5.1.4 layout. |
| CH\_7POINT1POINT2 = (CH\_7POINT1 | AudioChannelSet::TOP\_SIDE\_LEFT | AudioChannelSet::TOP\_SIDE\_RIGHT) | 7.1.2 layout. |
| CH\_7POINT1POINT4 = (CH\_7POINT1 | AudioChannelSet::TOP\_FRONT\_LEFT | AudioChannelSet::TOP\_FRONT\_RIGHT | AudioChannelSet::TOP\_BACK\_LEFT | AudioChannelSet::TOP\_BACK\_RIGHT) | 7.1.4 layout. |
| CH\_9POINT1POINT4 = (CH\_7POINT1POINT4 | AudioChannelSet::WIDE\_LEFT | AudioChannelSet::WIDE\_RIGHT) | 9.1.4 layout. |
| CH\_9POINT1POINT6 = (CH\_9POINT1POINT4 | AudioChannelSet::TOP\_SIDE\_LEFT | AudioChannelSet::TOP\_SIDE\_RIGHT) | 9.1.6 layout. |
| CH\_10POINT2 = (AudioChannelSet::FRONT\_LEFT | AudioChannelSet::FRONT\_RIGHT | AudioChannelSet::FRONT\_CENTER | AudioChannelSet::TOP\_FRONT\_LEFT | AudioChannelSet::TOP\_FRONT\_RIGHT | AudioChannelSet::BACK\_LEFT | AudioChannelSet::BACK\_RIGHT | AudioChannelSet::BACK\_CENTER | AudioChannelSet::SIDE\_LEFT | AudioChannelSet::SIDE\_RIGHT | AudioChannelSet::WIDE\_LEFT | AudioChannelSet::WIDE\_RIGHT) | 10.2 layout. |
| CH\_22POINT2 = (CH\_7POINT1POINT4 | AudioChannelSet::FRONT\_LEFT\_OF\_CENTER | AudioChannelSet::FRONT\_RIGHT\_OF\_CENTER | AudioChannelSet::BACK\_CENTER | AudioChannelSet::TOP\_CENTER | AudioChannelSet::TOP\_FRONT\_CENTER | AudioChannelSet::TOP\_BACK\_CENTER | AudioChannelSet::TOP\_SIDE\_LEFT | AudioChannelSet::TOP\_SIDE\_RIGHT | AudioChannelSet::BOTTOM\_FRONT\_LEFT | AudioChannelSet::BOTTOM\_FRONT\_RIGHT | AudioChannelSet::BOTTOM\_FRONT\_CENTER | AudioChannelSet::LOW\_FREQUENCY\_2) | 22.2 layout. |
| OCTAGONAL = (CH\_5POINT0 | AudioChannelSet::BACK\_LEFT | AudioChannelSet::BACK\_CENTER | AudioChannelSet::BACK\_RIGHT) | Octagonal layout. |
| HEXADECAGONAL = (OCTAGONAL | AudioChannelSet::WIDE\_LEFT | AudioChannelSet::WIDE\_RIGHT | AudioChannelSet::TOP\_BACK\_LEFT | AudioChannelSet::TOP\_BACK\_RIGHT | AudioChannelSet::TOP\_BACK\_CENTER | AudioChannelSet::TOP\_FRONT\_CENTER | AudioChannelSet::TOP\_FRONT\_LEFT | AudioChannelSet::TOP\_FRONT\_RIGHT) | Hexadecagonal layout. |
| STEREO\_DOWNMIX = (AudioChannelSet::STEREO\_LEFT | AudioChannelSet::STEREO\_RIGHT) | Stereo downmix layout. |
| HOA\_FIRST = AudioChannelSet::AMBISONICS\_ACN0 | AudioChannelSet::AMBISONICS\_ACN1 | AudioChannelSet::AMBISONICS\_ACN2 | AudioChannelSet::AMBISONICS\_ACN3 | High-Order Ambisonics (HOA) first-order layout. |
| HOA\_SECOND = HOA\_FIRST | AudioChannelSet::AMBISONICS\_ACN4 | AudioChannelSet::AMBISONICS\_ACN5 | AudioChannelSet::AMBISONICS\_ACN6 | AudioChannelSet::AMBISONICS\_ACN7 | AudioChannelSet::AMBISONICS\_ACN8 | HOA second-order layout. |
| HOA\_THIRD = HOA\_SECOND | AudioChannelSet::AMBISONICS\_ACN9 | AudioChannelSet::AMBISONICS\_ACN10 | AudioChannelSet::AMBISONICS\_ACN11 | AudioChannelSet::AMBISONICS\_ACN12 | AudioChannelSet::AMBISONICS\_ACN13 | AudioChannelSet::AMBISONICS\_ACN14 | AudioChannelSet::AMBISONICS\_ACN15 | HOA third-order layout. |
