# avmetadata\_extractor\_base.h

#### Overview

The file declares the constants used by the AVMetadataExtractor.

**File to include**: <multimedia/player\_framework/avmetadata\_extractor\_base.h>

**Library**: libavmetadata\_extractor.so

**System capability**: SystemCapability.Multimedia.Media.AVMetadataExtractor

**Since**: 18

**Related module**: [AVMetadataExtractor](../../modules/avmetadataextractor/document.md)

#### Summary

#### \[h2\]Variables

| Name | Description |
| :-- | :-- |
| static const char\* OH\_AVMETADATA\_EXTRACTOR\_ALBUM = "album" | 
Pointer to the key for obtaining the title of the album. The value type is const char\*.

**Since**: 18

 |
| static const char\* OH\_AVMETADATA\_EXTRACTOR\_ALBUM\_ARTIST = "albumArtist" | 

Pointer to the key for obtaining the artist of the album. The value type is const char\*.

**Since**: 18

 |
| static const char\* OH\_AVMETADATA\_EXTRACTOR\_ARTIST = "artist" | 

Pointer to the key for obtaining the artist of the media asset. The value type is const char\*.

**Since**: 18

 |
| static const char\* OH\_AVMETADATA\_EXTRACTOR\_AUTHOR = "author" | 

Pointer to the key for obtaining the author of the media asset. The value type is const char\*.

**Since**: 18

 |
| static const char\* OH\_AVMETADATA\_EXTRACTOR\_DATE\_TIME = "dateTime" | 

Pointer to the key for obtaining the creation time of the media asset. The value type is const char\*.

**Since**: 18

 |
| static const char\* OH\_AVMETADATA\_EXTRACTOR\_DATE\_TIME\_FORMAT = "dateTimeFormat" | 

Pointer to the key for obtaining the creation time of the media asset. The value type is const char\* and the output format is YYYY-MM-DD HH:mm:ss.

**Since**: 18

 |
| static const char\* OH\_AVMETADATA\_EXTRACTOR\_COMPOSER = "composer" | 

Pointer to the key for obtaining the composer of the media asset. The value type is const char\*.

**Since**: 18

 |
| static const char\* OH\_AVMETADATA\_EXTRACTOR\_DURATION = "duration" | 

Pointer to the key for obtaining the duration of the media asset, in ms. The value type is int64\_t.

**Since**: 18

 |
| static const char\* OH\_AVMETADATA\_EXTRACTOR\_GENRE = "genre" | 

Pointer to the key for obtaining the type or genre of the media asset. The value type is const char\*.

**Since**: 18

 |
| static const char\* OH\_AVMETADATA\_EXTRACTOR\_HAS\_AUDIO = "hasAudio" | 

Pointer to the key for obtaining the flag indicating whether the media asset contains audio. The value type is int32\_t.

**Since**: 18

 |
| static const char\* OH\_AVMETADATA\_EXTRACTOR\_HAS\_VIDEO = "hasVideo" | 

Pointer to the key for obtaining the flag indicating whether the media asset contains video. The value type is int32\_t.

**Since**: 18

 |
| static const char\* OH\_AVMETADATA\_EXTRACTOR\_MIME\_TYPE = "mimeType" | 

Pointer to the key for obtaining the MIME type of the media asset. The value type is const char\*, for example, video/mp4, audio/mp4, and audio/amr wb.

**Since**: 18

 |
| static const char\* OH\_AVMETADATA\_EXTRACTOR\_TRACK\_COUNT = "trackCount" | 

Pointer to the key for obtaining the number of tracks of the media asset. The value type is int32\_t.

**Since**: 18

 |
| static const char\* OH\_AVMETADATA\_EXTRACTOR\_SAMPLE\_RATE = "sampleRate" | 

Pointer to the key for obtaining the audio sample rate, in Hz. The value type is int32\_t.

**Since**: 18

 |
| static const char\* OH\_AVMETADATA\_EXTRACTOR\_TITLE = "title" | 

Pointer to the key for obtaining the title of the media asset. The value type is const char\*.

**Since**: 18

 |
| static const char\* OH\_AVMETADATA\_EXTRACTOR\_VIDEO\_HEIGHT = "videoHeight" | 

Pointer to the key for obtaining the video height, in px. The value type is int32\_t.

**Since**: 18

 |
| static const char\* OH\_AVMETADATA\_EXTRACTOR\_VIDEO\_WIDTH = "videoWidth" | 

Pointer to the key for obtaining the video weight, in px. The value type is int32\_t.

**Since**: 18

 |
| static const char\* OH\_AVMETADATA\_EXTRACTOR\_VIDEO\_ORIENTATION = "videoOrientation" | 

Pointer to the key for obtaining the video rotation direction, in degrees (°). The value type is int32\_t.

**Since**: 18

 |
| static const char\* OH\_AVMETADATA\_EXTRACTOR\_VIDEO\_IS\_HDR\_VIVID = "hdrType" | 

Pointer to the key for obtaining the flag indicating whether the video is an HDR Vivid video. The value type is int32\_t.

For details, see [OH\_Core\_HdrType](../../../../avcodec-kit/c-apis/header-files/media-types-h/document.md#oh_core_hdrtype) in **media\_types.h**.

**Since**: 18

 |
| static const char\* OH\_AVMETADATA\_EXTRACTOR\_LOCATION\_LATITUDE = "latitude" | 

Pointer to the key for obtaining the latitude in the geographical location. The value type is float.

**Since**: 18

 |
| static const char\* OH\_AVMETADATA\_EXTRACTOR\_LOCATION\_LONGITUDE = "longitude" | 

Pointer to the key for obtaining the longitude in the geographical location. The value type is float.

**Since**: 18

 |
