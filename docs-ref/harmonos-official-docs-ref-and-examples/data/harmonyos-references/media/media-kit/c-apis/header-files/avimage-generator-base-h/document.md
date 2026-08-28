# avimage\_generator\_base.h

#### Overview

The file declares the enums used by the AVImageGenerator.

**File to include**: <multimedia/player\_framework/avimage\_generator\_base.h>

**Library**: libavimage\_generator.so

**System capability**: SystemCapability.Multimedia.Media.AVImageGenerator

**Since**: 18

**Related module**: [AVImageGenerator](../../modules/avimagegenerator/document.md)

#### Summary

#### \[h2\]Enums

| Name | typedef Keyword | Description |
| :-- | :-- | :-- |
| [OH\_AVImageGenerator\_QueryOptions](#oh_avimagegenerator_queryoptions) | OH\_AVImageGenerator\_QueryOptions | Enumerates the mappings between time points and video frames. |

#### Enum Description

#### \[h2\]OH\_AVImageGenerator\_QueryOptions

enum OH\_AVImageGenerator\_QueryOptions

**Description**

Enumerates the mappings between time points and video frames.

**System capability**: SystemCapability.Multimedia.Media.AVImageGenerator

**Since**: 18

| Enum Item | Description |
| :-- | :-- |
| OH\_AVIMAGE\_GENERATOR\_QUERY\_NEXT\_SYNC = 0 | Extracts the key frame at or next to the specified time. |
| OH\_AVIMAGE\_GENERATOR\_QUERY\_PREVIOUS\_SYNC = 1 | Extracts the key frame at or prior to the specified time. |
| OH\_AVIMAGE\_GENERATOR\_QUERY\_CLOSEST\_SYNC = 2 | Extracts the key frame closest to the specified time. |
| OH\_AVIMAGE\_GENERATOR\_QUERY\_CLOSEST = 3 | Extracts the frame (not necessarily a key frame) closest to the specified time. |
