# native\_audio\_channel\_layout.h

#### Overview

The file declares the functions related to the speaker layout during recording and playback.

**File to include**: <multimedia/native\_audio\_channel\_layout.h>

**Library**: none

**System capability**: SystemCapability.Multimedia.Media.Core

**Since**: 11

**Related module**: [Core](../../modules/core/document.md)

#### Summary

#### \[h2\]Enums

| Name | typedef Keyword | Description |
| :-- | :-- | :-- |
| [OH\_AudioChannelSet](#oh_audiochannelset) | OH\_AudioChannelSet | 
Enumerates the audio channels.

Each channel is mapped to a variable of int64.

 |
| [OH\_AmbAttributeSet](#oh_ambattributeset) | OH\_AmbAttributeSet | 

Enumerates the Hi-Fi stereo reverberation settings.

Int64 integers are used to indicate the Hi-Fi stereo reverberation attributes.

 |
| [OH\_AudioChannelLayout](#oh_audiochannellayout) | OH\_AudioChannelLayout | 

Enumerates the layouts of audio channels.

Int64 integers are used to indicate the appearance and sequence of speakers during recording or playback.

 |

#### Enum Description

#### \[h2\]OH\_AudioChannelSet

enum OH\_AudioChannelSet

**Description**

Enumerates the audio channels.

Each channel is mapped to a variable of int64.

**System capability**: SystemCapability.Multimedia.Media.Core

**Since**: 11

| Value | Description |
| :-- | :-- |
| CH\_SET\_FRONT\_LEFT = 1ULL << 0U | Front left channel. |
| CH\_SET\_FRONT\_RIGHT = 1ULL << 1U | Front right channel. |
| CH\_SET\_FRONT\_CENTER = 1ULL << 2U | Front center channel. |
| CH\_SET\_LOW\_FREQUENCY = 1ULL << 3U | Low-frequency channel. |
| CH\_SET\_BACK\_LEFT = 1ULL << 4U | Rear left channel. |
| CH\_SET\_BACK\_RIGHT = 1ULL << 5U | Rear right channel. |
| CH\_SET\_FRONT\_LEFT\_OF\_CENTER = 1ULL << 6U | Front left center channel. |
| CH\_SET\_FRONT\_RIGHT\_OF\_CENTER = 1ULL << 7U | Front right center channel. |
| CH\_SET\_BACK\_CENTER = 1ULL << 8U | Rear center channel. |
| CH\_SET\_SIDE\_LEFT = 1ULL << 9U | Left channel. |
| CH\_SET\_SIDE\_RIGHT = 1ULL << 10U | Right channel. |
| CH\_SET\_TOP\_CENTER = 1ULL << 11U | Top center channel. |
| CH\_SET\_TOP\_FRONT\_LEFT = 1ULL << 12U | Top left front channel. |
| CH\_SET\_TOP\_FRONT\_CENTER = 1ULL << 13U | Top center front channel. |
| CH\_SET\_TOP\_FRONT\_RIGHT = 1ULL << 14U | Top right front channel. |
| CH\_SET\_TOP\_BACK\_LEFT = 1ULL << 15U | Top left rear channel. |
| CH\_SET\_TOP\_BACK\_CENTER = 1ULL << 16U | Top center rear channel. |
| CH\_SET\_TOP\_BACK\_RIGHT = 1ULL << 17U | Top right rear channel. |
| CH\_SET\_STEREO\_LEFT = 1ULL << 29U | Stereo left channel. |
| CH\_SET\_STEREO\_RIGHT = 1ULL << 30U | Stereo right channel. |
| CH\_SET\_WIDE\_LEFT = 1ULL << 31U | Wide left channel. |
| CH\_SET\_WIDE\_RIGHT = 1ULL << 32U | Wide right channel. |
| CH\_SET\_SURROUND\_DIRECT\_LEFT = 1ULL << 33U | Left surround channel. |
| CH\_SET\_SURROUND\_DIRECT\_RIGHT = 1ULL << 34U | Right surround channel. |
| CH\_SET\_LOW\_FREQUENCY\_2 = 1ULL << 35U | Low-frequency channel 2. |
| CH\_SET\_TOP\_SIDE\_LEFT = 1ULL << 36U | Top left channel. |
| CH\_SET\_TOP\_SIDE\_RIGHT = 1ULL << 37U | Top right channel. |
| CH\_SET\_BOTTOM\_FRONT\_CENTER = 1ULL << 38U | Bottom center front channel. |
| CH\_SET\_BOTTOM\_FRONT\_LEFT = 1ULL << 39U | Bottom left front channel. |
| CH\_SET\_BOTTOM\_FRONT\_RIGHT = 1ULL << 40U | Bottom right front channel. |

#### \[h2\]OH\_AmbAttributeSet

enum OH\_AmbAttributeSet

**Description**

Enumerates the Hi-Fi stereo reverberation settings.

Int64 integers are used to indicate the Hi-Fi stereo reverberation attributes.

**System capability**: SystemCapability.Multimedia.Media.Core

**Since**: 11

| Value | Description |
| :-- | :-- |
| AMB\_ORD\_1 = 1ULL << 0U | First-order Hi-Fi stereo reverberation. |
| AMB\_ORD\_2 = 2ULL << 0U | Second-order Hi-Fi stereo reverberation. |
| AMB\_ORD\_3 = 3ULL << 0U | Third-order Hi-Fi stereo reverberation. |
| AMB\_COM\_ACN = 0ULL << 8U | Hi-Fi stereo reverberation with ACN channel sorting. |
| AMB\_COM\_FUMA = 1ULL << 8U | Hi-Fi stereo reverberation with FUMA channel sorting. |
| AMB\_NOR\_N3D = 0ULL << 12U | N3D normalized Hi-Fi stereo reverberation. |
| AMB\_NOR\_SN3D = 1ULL << 12U | SN3D normalized Hi-Fi stereo reverberation. |
| AMB\_MODE = 1ULL << 44U | Audio channel layout for Hi-Fi stereo reverberation. |

#### \[h2\]OH\_AudioChannelLayout

enum OH\_AudioChannelLayout

**Description**

Enumerates the layouts of audio channels.

Int64 integers are used to indicate the appearance and sequence of speakers during recording or playback.

**System capability**: SystemCapability.Multimedia.Media.Core

**Since**: 11

| Value | Description |
| :-- | :-- |
| CH\_LAYOUT\_UNKNOWN = 0ULL | Unknown. |
| CH\_LAYOUT\_MONO = CH\_SET\_FRONT\_CENTER | Mono layout; 1 audio channel in total. |
| CH\_LAYOUT\_STEREO = CH\_SET\_FRONT\_LEFT | CH\_SET\_FRONT\_RIGHT | Stereo layout; 2 audio channels in total. |
| CH\_LAYOUT\_STEREO\_DOWNMIX = CH\_SET\_STEREO\_LEFT | CH\_SET\_STEREO\_RIGHT | Stereo downmix layout; 2 audio channels in total. |
| CH\_LAYOUT\_2POINT1 = CH\_LAYOUT\_STEREO | CH\_SET\_LOW\_FREQUENCY | 2.1 layout; 3 audio channels in total. |
| CH\_LAYOUT\_3POINT0 = CH\_LAYOUT\_STEREO | CH\_SET\_BACK\_CENTER | 3.0 layout; 3 audio channels in total. |
| CH\_LAYOUT\_SURROUND = CH\_LAYOUT\_STEREO | CH\_SET\_FRONT\_CENTER | Surround; 3 audio channels in total. |
| CH\_LAYOUT\_3POINT1 = CH\_LAYOUT\_SURROUND | CH\_SET\_LOW\_FREQUENCY | 3.1 layout; 4 audio channels in total. |
| CH\_LAYOUT\_4POINT0 = CH\_LAYOUT\_SURROUND | CH\_SET\_BACK\_CENTER | 4.0 layout; 4 audio channels in total. |
| CH\_LAYOUT\_QUAD\_SIDE = CH\_LAYOUT\_STEREO | CH\_SET\_SIDE\_LEFT | CH\_SET\_SIDE\_RIGHT | Quad side layout; 4 audio channels in total. |
| CH\_LAYOUT\_QUAD = CH\_LAYOUT\_STEREO | CH\_SET\_BACK\_LEFT | CH\_SET\_BACK\_RIGHT | Quad layout; 4 audio channels in total. |
| CH\_LAYOUT\_2POINT0POINT2 = CH\_LAYOUT\_STEREO | CH\_SET\_TOP\_SIDE\_LEFT | CH\_SET\_TOP\_SIDE\_RIGHT | 2.0.2 layout; 4 audio channels in total. |
| CH\_LAYOUT\_AMB\_ORDER1\_ACN\_N3D = AMB\_MODE | AMB\_ORD\_1 | AMB\_COM\_ACN | AMB\_NOR\_N3D | First-order FOA layout in ACN\_N3D (ITU standards); 4 audio channels in total. |
| CH\_LAYOUT\_AMB\_ORDER1\_ACN\_SN3D = AMB\_MODE | AMB\_ORD\_1 | AMB\_COM\_ACN | AMB\_NOR\_SN3D | First-order FOA layout in ACN\_SN3D (ITU standards); 4 audio channels in total. |
| CH\_LAYOUT\_AMB\_ORDER1\_FUMA = AMB\_MODE | AMB\_ORD\_1 | AMB\_COM\_FUMA | First-order FOA layout in FUMA (ITU standards); 4 audio channels in total. |
| CH\_LAYOUT\_4POINT1 = CH\_LAYOUT\_4POINT0 | CH\_SET\_LOW\_FREQUENCY | 4.1 layout; 5 audio channels in total. |
| CH\_LAYOUT\_5POINT0 = CH\_LAYOUT\_SURROUND | CH\_SET\_SIDE\_LEFT | CH\_SET\_SIDE\_RIGHT | 5.0 layout; 5 audio channels in total. |
| CH\_LAYOUT\_5POINT0\_BACK = CH\_LAYOUT\_SURROUND | CH\_SET\_BACK\_LEFT | CH\_SET\_BACK\_RIGHT | 5.0 rear layout; 5 audio channels in total. |
| CH\_LAYOUT\_2POINT1POINT2 = CH\_LAYOUT\_2POINT0POINT2 | CH\_SET\_LOW\_FREQUENCY | 2.1.2 layout; 5 audio channels in total. |
| CH\_LAYOUT\_3POINT0POINT2 = CH\_LAYOUT\_2POINT0POINT2 | CH\_SET\_FRONT\_CENTER | 3.0.2 layout; 5 audio channels in total. |
| CH\_LAYOUT\_5POINT1 = CH\_LAYOUT\_5POINT0 | CH\_SET\_LOW\_FREQUENCY | 5.1 layout; 6 audio channels in total. |
| CH\_LAYOUT\_5POINT1\_BACK = CH\_LAYOUT\_5POINT0\_BACK | CH\_SET\_LOW\_FREQUENCY | 5.1 rear layout; 6 audio channels in total. |
| CH\_LAYOUT\_6POINT0 = CH\_LAYOUT\_5POINT0 | CH\_SET\_BACK\_CENTER | 6.0 layout; 6 audio channels in total. |
| CH\_LAYOUT\_3POINT1POINT2 = CH\_LAYOUT\_3POINT1 | CH\_SET\_TOP\_FRONT\_LEFT | CH\_SET\_TOP\_FRONT\_RIGHT | 3.1.2 layout; 6 audio channels in total. |
| CH\_LAYOUT\_6POINT0\_FRONT = CH\_LAYOUT\_QUAD\_SIDE | CH\_SET\_FRONT\_LEFT\_OF\_CENTER | CH\_SET\_FRONT\_RIGHT\_OF\_CENTER | 6.0 front layout; 6 audio channels in total. |
| CH\_LAYOUT\_HEXAGONAL = CH\_LAYOUT\_5POINT0\_BACK | CH\_SET\_BACK\_CENTER | Hexagonal layout; 6 audio channels in total. |
| CH\_LAYOUT\_6POINT1 = CH\_LAYOUT\_5POINT1 | CH\_SET\_BACK\_CENTER | 6.1 layout; 7 audio channels in total. |
| CH\_LAYOUT\_6POINT1\_BACK = CH\_LAYOUT\_5POINT1\_BACK | CH\_SET\_BACK\_CENTER | 6.1 rear layout; 7 audio channels in total. |
| CH\_LAYOUT\_6POINT1\_FRONT = CH\_LAYOUT\_6POINT0\_FRONT | CH\_SET\_LOW\_FREQUENCY | 6.1 front layout; 7 audio channels in total. |
| CH\_LAYOUT\_7POINT0 = CH\_LAYOUT\_5POINT0 | CH\_SET\_BACK\_LEFT | CH\_SET\_BACK\_RIGHT | 7.0 layout; 7 audio channels in total. |
| CH\_LAYOUT\_7POINT0\_FRONT = CH\_LAYOUT\_5POINT0 | CH\_SET\_FRONT\_LEFT\_OF\_CENTER | CH\_SET\_FRONT\_RIGHT\_OF\_CENTER | 7.0 front layout; 7 audio channels in total. |
| CH\_LAYOUT\_7POINT1 = CH\_LAYOUT\_5POINT1 | CH\_SET\_BACK\_LEFT | CH\_SET\_BACK\_RIGHT | 7.1 layout; 8 audio channels in total. |
| CH\_LAYOUT\_OCTAGONAL = CH\_LAYOUT\_5POINT0 | CH\_SET\_BACK\_LEFT | CH\_SET\_BACK\_CENTER | CH\_SET\_BACK\_RIGHT | Octagonal layout; 8 audio channels in total. |
| CH\_LAYOUT\_5POINT1POINT2 = CH\_LAYOUT\_5POINT1 | CH\_SET\_TOP\_SIDE\_LEFT | CH\_SET\_TOP\_SIDE\_RIGHT | 5.1.2 layout; 8 audio channels in total. |
| CH\_LAYOUT\_7POINT1\_WIDE = CH\_LAYOUT\_5POINT1 | CH\_SET\_FRONT\_LEFT\_OF\_CENTER | CH\_SET\_FRONT\_RIGHT\_OF\_CENTER | 7.1 wide layout; 8 audio channels in total. |
| CH\_LAYOUT\_7POINT1\_WIDE\_BACK = CH\_LAYOUT\_5POINT1\_BACK | CH\_SET\_FRONT\_LEFT\_OF\_CENTER | CH\_SET\_FRONT\_RIGHT\_OF\_CENTER | 7.1 rear wide layout; 8 audio channels in total. |
| CH\_LAYOUT\_AMB\_ORDER2\_ACN\_N3D = AMB\_MODE | AMB\_ORD\_2 | AMB\_COM\_ACN | AMB\_NOR\_N3D | Second-order HOA layout in ACN\_N3D (ITU standards); 9 audio channels in total. |
| CH\_LAYOUT\_AMB\_ORDER2\_ACN\_SN3D = AMB\_MODE | AMB\_ORD\_2 | AMB\_COM\_ACN | AMB\_NOR\_SN3D | Second-order HOA layout in ACN\_SN3D (ITU standards); 9 audio channels in total. |
| CH\_LAYOUT\_AMB\_ORDER2\_FUMA = AMB\_MODE | AMB\_ORD\_2 | AMB\_COM\_FUMA | Second-order HOA layout in FUMA (ITU standards); 9 audio channels in total. |
| CH\_LAYOUT\_5POINT1POINT4 = CH\_LAYOUT\_5POINT1 | CH\_SET\_TOP\_FRONT\_LEFT | CH\_SET\_TOP\_FRONT\_RIGHT | CH\_SET\_TOP\_BACK\_LEFT | CH\_SET\_TOP\_BACK\_RIGHT | 5.1.4 layout; 10 audio channels in total. |
| CH\_LAYOUT\_7POINT1POINT2 = CH\_LAYOUT\_7POINT1 | CH\_SET\_TOP\_SIDE\_LEFT | CH\_SET\_TOP\_SIDE\_RIGHT | 7.1.2 layout; 10 audio channels in total. |
| CH\_LAYOUT\_7POINT1POINT4 = CH\_LAYOUT\_7POINT1 | CH\_SET\_TOP\_FRONT\_LEFT | CH\_SET\_TOP\_FRONT\_RIGHT | CH\_SET\_TOP\_BACK\_LEFT | CH\_SET\_TOP\_BACK\_RIGHT | 7.1.4 layout; 12 audio channels in total. |
| CH\_LAYOUT\_10POINT2 = CH\_SET\_FRONT\_LEFT | CH\_SET\_FRONT\_RIGHT | CH\_SET\_FRONT\_CENTER | CH\_SET\_TOP\_FRONT\_LEFT | CH\_SET\_TOP\_FRONT\_RIGHT | CH\_SET\_BACK\_LEFT | CH\_SET\_BACK\_RIGHT | CH\_SET\_BACK\_CENTER | CH\_SET\_SIDE\_LEFT | CH\_SET\_SIDE\_RIGHT | CH\_SET\_WIDE\_LEFT | CH\_SET\_WIDE\_RIGHT | 10.2 layout; 12 audio channels in total. |
| CH\_LAYOUT\_9POINT1POINT4 = CH\_LAYOUT\_7POINT1POINT4 | CH\_SET\_WIDE\_LEFT | CH\_SET\_WIDE\_RIGHT | 9.1.4 layout; 14 audio channels in total. |
| CH\_LAYOUT\_9POINT1POINT6 = CH\_LAYOUT\_9POINT1POINT4 | CH\_SET\_TOP\_SIDE\_LEFT | CH\_SET\_TOP\_SIDE\_RIGHT | 9.1.6 layout; 16 audio channels in total. |
| CH\_LAYOUT\_HEXADECAGONAL = CH\_LAYOUT\_OCTAGONAL | CH\_SET\_WIDE\_LEFT | CH\_SET\_WIDE\_RIGHT | CH\_SET\_TOP\_BACK\_LEFT | CH\_SET\_TOP\_BACK\_RIGHT | CH\_SET\_TOP\_BACK\_CENTER | CH\_SET\_TOP\_FRONT\_CENTER | CH\_SET\_TOP\_FRONT\_LEFT | CH\_SET\_TOP\_FRONT\_RIGHT | Hexadecagonal layout; 16 audio channels in total. |
| CH\_LAYOUT\_AMB\_ORDER3\_ACN\_N3D = AMB\_MODE | AMB\_ORD\_3 | AMB\_COM\_ACN | AMB\_NOR\_N3D | Third-order HOA layout in ACN\_N3D (ITU standards); 16 audio channels in total. |
| CH\_LAYOUT\_AMB\_ORDER3\_ACN\_SN3D = AMB\_MODE | AMB\_ORD\_3 | AMB\_COM\_ACN | AMB\_NOR\_SN3D | Third-order HOA layout in ACN\_SN3D (ITU standards); 16 audio channels in total. |
| CH\_LAYOUT\_AMB\_ORDER3\_FUMA = AMB\_MODE | AMB\_ORD\_3 | AMB\_COM\_FUMA | Third-order HOA layout in FUMA (ITU standards); 16 audio channels in total. |
| CH\_LAYOUT\_22POINT2 = CH\_LAYOUT\_7POINT1POINT4 | CH\_SET\_FRONT\_LEFT\_OF\_CENTER | CH\_SET\_FRONT\_RIGHT\_OF\_CENTER | CH\_SET\_BACK\_CENTER | CH\_SET\_TOP\_CENTER | CH\_SET\_TOP\_FRONT\_CENTER | CH\_SET\_TOP\_BACK\_CENTER | CH\_SET\_TOP\_SIDE\_LEFT | CH\_SET\_TOP\_SIDE\_RIGHT | CH\_SET\_BOTTOM\_FRONT\_LEFT | CH\_SET\_BOTTOM\_FRONT\_RIGHT | CH\_SET\_BOTTOM\_FRONT\_CENTER | CH\_SET\_LOW\_FREQUENCY\_2 | 22.2 layout; 24 audio channels in total. |
