# image\_common.h

#### Overview

The file declares the common enums and structs used by the image interface.

**File to include**: <multimedia/image\_framework/image/image\_common.h>

**Library**: libimage\_common.so

**System capability**: SystemCapability.Multimedia.Image.Core

**Since**: 12

**Related module**: [Image\_NativeModule](../../modules/image-nativemodule/document.md)

#### Summary

#### \[h2\]Structs

| Name | typedef Keyword | Description |
| :-- | :-- | :-- |
| [Image\_Size](../../structs/image-size/document.md) | Image\_Size | Describes the image size. |
| [Image\_Region](../../structs/image-region/document.md) | Image\_Region | Describes the region of an image to decode. |
| [Image\_PositionArea](../../structs/image-positionarea/document.md) | Image\_PositionArea | Describes the area of image pixels to be read from or written to. |
| [Image\_Scale](../../structs/image-scale/document.md) | Image\_Scale | Describes the image scaling factor. |
| [Image\_String](../../structs/image-string/document.md) | Image\_String/Image\_MimeType | Describes an image string. |
| [OH\_PictureMetadata](../../structs/oh-picturemetadata/document.md) | OH\_PictureMetadata | Describes the picture metadata. |

#### \[h2\]Enums

| Name | typedef Keyword | Description |
| :-- | :-- | :-- |
| [Image\_ErrorCode](#image_errorcode) | Image\_ErrorCode | Enumerates the error codes. |
| [Image\_MetadataType](#image_metadatatype) | Image\_MetadataType | Enumerates the metadata types. |
| [IMAGE\_ALLOCATOR\_MODE](#image_allocator_mode) | IMAGE\_ALLOCATOR\_MODE | Enumerates the types of memory allocation for a PixelMap. |

#### \[h2\]Functions

| Name | Description |
| :-- | :-- |
| [Image\_ErrorCode OH\_PictureMetadata\_Create(Image\_MetadataType metadataType, OH\_PictureMetadata \*\*metadata)](#oh_picturemetadata_create) | Creates the pointer to an OH\_PictureMetadata struct. |
| [Image\_ErrorCode OH\_PictureMetadata\_GetProperty(OH\_PictureMetadata \*metadata, Image\_String \*key, Image\_String \*value)](#oh_picturemetadata_getproperty) | Obtains a property of metadata based on the key. The **value.data** obtained through this API lacks the string terminator **\\0**. Please use it with caution. |
| [Image\_ErrorCode OH\_PictureMetadata\_SetProperty(OH\_PictureMetadata \*metadata, Image\_String \*key, Image\_String \*value)](#oh_picturemetadata_setproperty) | Sets a property of metadata based on the key. |
| [Image\_ErrorCode OH\_PictureMetadata\_GetPropertyWithNull(OH\_PictureMetadata \*metadata, Image\_String \*key, Image\_String \*value)](#oh_picturemetadata_getpropertywithnull) | Obtains the metadata value of an OH\_PictureMetadata instance. The output of **value.data** ends with the string terminator **\\0**. |
| [Image\_ErrorCode OH\_PictureMetadata\_Release(OH\_PictureMetadata \*metadata)](#oh_picturemetadata_release) | Releases the pointer to an OH\_PictureMetadata struct. |
| [Image\_ErrorCode OH\_PictureMetadata\_Clone(OH\_PictureMetadata \*oldMetadata, OH\_PictureMetadata \*\*newMetadata)](#oh_picturemetadata_clone) | Clones metadata. |

#### \[h2\]Variables

| Name | Description |
| :-- | :-- |
| static const char \* MIME\_TYPE\_BMP = "image/bmp" | 
BMP image format.

**Since**: 12

 |
| static const char \* MIME\_TYPE\_JPEG = "image/jpeg" | 

JPEG image format.

**Since**: 12

 |
| static const char \* MIME\_TYPE\_HEIC = "image/heic" | 

HEIC image format.

**Since**: 12

 |
| static const char \* MIME\_TYPE\_PNG = "image/png" | 

PNG image format.

**Since**: 12

 |
| static const char \* MIME\_TYPE\_WEBP = "image/webp" | 

WebP image format.

**Since**: 12

 |
| static const char \* MIME\_TYPE\_GIF = "image/gif" | 

GIF image format.

**Since**: 12

 |
| static const char \* MIME\_TYPE\_ICON = "image/x-icon" | 

ICO image format.

**Since**: 12

 |
| static const char \* OHOS\_IMAGE\_PROPERTY\_BITS\_PER\_SAMPLE = "BitsPerSample" | 

Number of bits per sample.

**Since**: 12

 |
| static const char \* OHOS\_IMAGE\_PROPERTY\_ORIENTATION = "Orientation" | 

Image orientation.

**Since**: 12

 |
| static const char \* OHOS\_IMAGE\_PROPERTY\_IMAGE\_LENGTH = "ImageLength" | 

Image length.

**Since**: 12

 |
| static const char \* OHOS\_IMAGE\_PROPERTY\_IMAGE\_WIDTH = "ImageWidth" | 

Image width.

**Since**: 12

 |
| static const char \* OHOS\_IMAGE\_PROPERTY\_GPS\_LATITUDE = "GPSLatitude" | 

Image latitude.

**Since**: 12

 |
| static const char \* OHOS\_IMAGE\_PROPERTY\_GPS\_LONGITUDE = "GPSLongitude" | 

Image longitude.

**Since**: 12

 |
| static const char \* OHOS\_IMAGE\_PROPERTY\_GPS\_LATITUDE\_REF = "GPSLatitudeRef" | 

Whether the latitude is north or south latitude.

**Since**: 12

 |
| static const char \* OHOS\_IMAGE\_PROPERTY\_GPS\_LONGITUDE\_REF = "GPSLongitudeRef" | 

Whether the longitude is east or west longitude.

**Since**: 12

 |
| static const char \* OHOS\_IMAGE\_PROPERTY\_DATE\_TIME\_ORIGINAL = "DateTimeOriginal" | 

Shooting time, for example, 2022:09:06 15:48:00.

**Since**: 12

 |
| static const char \* OHOS\_IMAGE\_PROPERTY\_EXPOSURE\_TIME = "ExposureTime" | 

Exposure time, for example, 1/33 seconds.

**Since**: 12

 |
| static const char \* OHOS\_IMAGE\_PROPERTY\_SCENE\_TYPE = "SceneType" | 

Type of the scene, for example, portrait, scenery, motion, and night.

**Since**: 12

 |
| static const char \* OHOS\_IMAGE\_PROPERTY\_ISO\_SPEED\_RATINGS = "ISOSpeedRatings" | 

ISO sensitivity or ISO speed, for example, 400.

**Since**: 12

 |
| static const char \* OHOS\_IMAGE\_PROPERTY\_F\_NUMBER = "FNumber" | 

F number, for example, f/1.8.

**Since**: 12

 |
| static const char \* OHOS\_IMAGE\_PROPERTY\_COMPRESSED\_BITS\_PER\_PIXEL = "CompressedBitsPerPixel" | 

Number of bits per pixel. It is specific to compressed data.

**Since**: 12

 |
| static const char \* OHOS\_IMAGE\_PROPERTY\_COMPRESSION = "Compression" | 

Compression scheme used on the image data.

**Since**: 12

 |
| static const char \* OHOS\_IMAGE\_PROPERTY\_PHOTOMETRIC\_INTERPRETATION = "PhotometricInterpretation" | 

Color space of the image data, for example, RGB or YCbCr.

**Since**: 12

 |
| static const char \* OHOS\_IMAGE\_PROPERTY\_STRIP\_OFFSETS = "StripOffsets" | 

Byte offset of each strip.

**Since**: 12

 |
| static const char \* OHOS\_IMAGE\_PROPERTY\_SAMPLES\_PER\_PIXEL = "SamplesPerPixel" | 

Number of components per pixel. The value is **3** for RGB and YCbCr images. The **JPEG** key is used in JPEG compressed data.

**Since**: 12

 |
| static const char \* OHOS\_IMAGE\_PROPERTY\_ROWS\_PER\_STRIP = "RowsPerStrip" | 

Number of rows per strip.

**Since**: 12

 |
| static const char \* OHOS\_IMAGE\_PROPERTY\_STRIP\_BYTE\_COUNTS = "StripByteCounts" | 

Number of bytes in each strip after compression.

**Since**: 12

 |
| static const char \* OHOS\_IMAGE\_PROPERTY\_X\_RESOLUTION = "XResolution" | 

Number of pixels per ResolutionUnit in the image width (X) direction.

**Since**: 12

 |
| static const char \* OHOS\_IMAGE\_PROPERTY\_Y\_RESOLUTION = "YResolution" | 

Number of pixels per ResolutionUnit in the image height (Y) direction.

**Since**: 12

 |
| static const char \* OHOS\_IMAGE\_PROPERTY\_PLANAR\_CONFIGURATION = "PlanarConfiguration" | 

Storage format of components of each pixel, which can be chunky or planar.

**Since**: 12

 |
| static const char \* OHOS\_IMAGE\_PROPERTY\_RESOLUTION\_UNIT = "ResolutionUnit" | 

Unit of measurement for XResolution and YResolution.

**Since**: 12

 |
| static const char \* OHOS\_IMAGE\_PROPERTY\_TRANSFER\_FUNCTION = "TransferFunction" | 

Transfer function for the image, which is usually used for color correction.

**Since**: 12

 |
| static const char \* OHOS\_IMAGE\_PROPERTY\_SOFTWARE = "Software" | 

Name and version number of the software used to create the image.

**Since**: 12

 |
| static const char \* OHOS\_IMAGE\_PROPERTY\_ARTIST = "Artist" | 

Person who created the image.

**Since**: 12

 |
| static const char \* OHOS\_IMAGE\_PROPERTY\_WHITE\_POINT = "WhitePoint" | 

Chromaticity of the white point of the image.

**Since**: 12

 |
| static const char \* OHOS\_IMAGE\_PROPERTY\_PRIMARY\_CHROMATICITIES = "PrimaryChromaticities" | 

Chromaticities of the primaries of the image.

**Since**: 12

 |
| static const char \* OHOS\_IMAGE\_PROPERTY\_YCBCR\_COEFFICIENTS = "YCbCrCoefficients" | 

Transformation from RGB to YCbCr image data.

**Since**: 12

 |
| static const char \* OHOS\_IMAGE\_PROPERTY\_YCBCR\_SUB\_SAMPLING = "YCbCrSubSampling" | 

Subsampling factors used for the chrominance components of a YCbCr image.

**Since**: 12

 |
| static const char \* OHOS\_IMAGE\_PROPERTY\_YCBCR\_POSITIONING = "YCbCrPositioning" | 

Positioning of subsampled chrominance components relative to luminance samples.

**Since**: 12

 |
| static const char \* OHOS\_IMAGE\_PROPERTY\_REFERENCE\_BLACK\_WHITE = "ReferenceBlackWhite" | 

A pair of headroom and footroom image data values (codes) for each pixel component.

**Since**: 12

 |
| static const char \* OHOS\_IMAGE\_PROPERTY\_COPYRIGHT = "Copyright" | 

Copyright notice of the image.

**Since**: 12

 |
| static const char \* OHOS\_IMAGE\_PROPERTY\_JPEG\_INTERCHANGE\_FORMAT = "JPEGInterchangeFormat" | 

Offset of the SOI marker of a JPEG interchange format bitstream.

**Since**: 12

 |
| static const char \* OHOS\_IMAGE\_PROPERTY\_JPEG\_INTERCHANGE\_FORMAT\_LENGTH = "JPEGInterchangeFormatLength" | 

Number of bytes of the JPEG stream.

**Since**: 12

 |
| static const char \* OHOS\_IMAGE\_PROPERTY\_EXPOSURE\_PROGRAM = "ExposureProgram" | 

Class of the program used by the camera to set exposure when the image was captured.

**Since**: 12

 |
| static const char \* OHOS\_IMAGE\_PROPERTY\_SPECTRAL\_SENSITIVITY = "SpectralSensitivity" | 

Spectral sensitivity of each channel of the camera.

**Since**: 12

 |
| static const char \* OHOS\_IMAGE\_PROPERTY\_OECF = "OECF" | 

Opto-Electric Conversion Function (OECF) specified in ISO 14524.

**Since**: 12

 |
| static const char \* OHOS\_IMAGE\_PROPERTY\_EXIF\_VERSION = "ExifVersion" | 

Version of the supported Exif standard.

**Since**: 12

 |
| static const char \* OHOS\_IMAGE\_PROPERTY\_DATE\_TIME\_DIGITIZED = "DateTimeDigitized" | 

Date and time when the image was stored as digital data, in the format of YYYY:MM:DD HH:MM:SS.

**Since**: 12

 |
| static const char \* OHOS\_IMAGE\_PROPERTY\_COMPONENTS\_CONFIGURATION = "ComponentsConfiguration" | 

Specific information about compressed data.

**Since**: 12

 |
| static const char \* OHOS\_IMAGE\_PROPERTY\_SHUTTER\_SPEED\_VALUE = "ShutterSpeedValue" | 

Shutter speed, expressed in Additive System of Photographic Exposure (APEX) values.

**Since**: 12

 |
| static const char \* OHOS\_IMAGE\_PROPERTY\_BRIGHTNESS\_VALUE = "BrightnessValue" | 

Value of brightness, expressed in APEX values.

**Since**: 12

 |
| static const char \* OHOS\_IMAGE\_PROPERTY\_MAX\_APERTURE\_VALUE = "MaxApertureValue" | 

Smallest F number of the lens.

**Since**: 12

 |
| static const char \* OHOS\_IMAGE\_PROPERTY\_SUBJECT\_DISTANCE = "SubjectDistance" | 

Distance to the subject, in meters.

**Since**: 12

 |
| static const char \* OHOS\_IMAGE\_PROPERTY\_SUBJECT\_AREA = "SubjectArea" | 

Location and area of the main subject in the entire scene.

**Since**: 12

 |
| static const char \* OHOS\_IMAGE\_PROPERTY\_MAKER\_NOTE = "MakerNote" | 

Marker used by Exif/DCF manufacturers to record any required information.

**Since**: 12

 |
| static const char \* OHOS\_IMAGE\_PROPERTY\_SUBSEC\_TIME = "SubsecTime" | 

Tag used to record fractions of seconds for the **DateTime** tag.

**Since**: 12

 |
| static const char \* OHOS\_IMAGE\_PROPERTY\_SUBSEC\_TIME\_ORIGINAL = "SubsecTimeOriginal" | 

Tag used to record fractions of seconds for the **DateTimeOriginal** tag.

**Since**: 12

 |
| static const char \* OHOS\_IMAGE\_PROPERTY\_SUBSEC\_TIME\_DIGITIZED = "SubsecTimeDigitized" | 

Tag used to record fractions of seconds for the **DateTimeDigitized** tag.

**Since**: 12

 |
| static const char \* OHOS\_IMAGE\_PROPERTY\_FLASHPIX\_VERSION = "FlashpixVersion" | 

FlashPix format version supported by an FPXR file. It is used to enhance device compatibility.

**Since**: 12

 |
| static const char \* OHOS\_IMAGE\_PROPERTY\_COLOR\_SPACE = "ColorSpace" | 

Color space information, which is usually recorded as a color space specifier.

**Since**: 12

 |
| static const char \* OHOS\_IMAGE\_PROPERTY\_RELATED\_SOUND\_FILE = "RelatedSoundFile" | 

Name of an audio file related to the image data.

**Since**: 12

 |
| static const char \* OHOS\_IMAGE\_PROPERTY\_FLASH\_ENERGY = "FlashEnergy" | 

Strobe energy at the time the image was captured, in Beam Candle Power Seconds (BCPS).

**Since**: 12

 |
| static const char \* OHOS\_IMAGE\_PROPERTY\_SPATIAL\_FREQUENCY\_RESPONSE = "SpatialFrequencyResponse" | 

Spatial frequency table of the camera or input device.

**Since**: 12

 |
| static const char \* OHOS\_IMAGE\_PROPERTY\_FOCAL\_PLANE\_X\_RESOLUTION = "FocalPlaneXResolution" | 

Number of pixels in the image width (X) direction per FocalPlaneResolutionUnit.

**Since**: 12

 |
| static const char \* OHOS\_IMAGE\_PROPERTY\_FOCAL\_PLANE\_Y\_RESOLUTION = "FocalPlaneYResolution" | 

Number of pixels in the image height (Y) direction per FocalPlaneResolutionUnit.

**Since**: 12

 |
| static const char \* OHOS\_IMAGE\_PROPERTY\_FOCAL\_PLANE\_RESOLUTION\_UNIT = "FocalPlaneResolutionUnit" | 

Unit for measuring FocalPlaneXResolution and FocalPlaneYResolution.

**Since**: 12

 |
| static const char \* OHOS\_IMAGE\_PROPERTY\_SUBJECT\_LOCATION = "SubjectLocation" | 

Location of the main subject relative to the left edge.

**Since**: 12

 |
| static const char \* OHOS\_IMAGE\_PROPERTY\_EXPOSURE\_INDEX = "ExposureIndex" | 

Exposure index selected at the time the image is captured.

**Since**: 12

 |
| static const char \* OHOS\_IMAGE\_PROPERTY\_SENSING\_METHOD = "SensingMethod" | 

Type of the image sensor on the camera.

**Since**: 12

 |
| static const char \* OHOS\_IMAGE\_PROPERTY\_FILE\_SOURCE = "FileSource" | 

Image source.

**Since**: 12

 |
| static const char \* OHOS\_IMAGE\_PROPERTY\_CFA\_PATTERN = "CFAPattern" | 

Color Filter Array (CFA) geometric pattern of the image sensor.

**Since**: 12

 |
| static const char \* OHOS\_IMAGE\_PROPERTY\_CUSTOM\_RENDERED = "CustomRendered" | 

Special processing on image data.

**Since**: 12

 |
| static const char \* OHOS\_IMAGE\_PROPERTY\_EXPOSURE\_MODE = "ExposureMode" | 

Exposure mode set when the image was captured.

**Since**: 12

 |
| static const char \* OHOS\_IMAGE\_PROPERTY\_DIGITAL\_ZOOM\_RATIO = "DigitalZoomRatio" | 

Digital zoom ratio when the image was captured.

**Since**: 12

 |
| static const char \* OHOS\_IMAGE\_PROPERTY\_SCENE\_CAPTURE\_TYPE = "SceneCaptureType" | 

Type of the scene that was captured.

**Since**: 12

 |
| static const char \* OHOS\_IMAGE\_PROPERTY\_GAIN\_CONTROL = "GainControl" | 

Degree of overall image gain adjustment.

**Since**: 12

 |
| static const char \* OHOS\_IMAGE\_PROPERTY\_CONTRAST = "Contrast" | 

Direction of contrast processing used by the camera.

**Since**: 12

 |
| static const char \* OHOS\_IMAGE\_PROPERTY\_SATURATION = "Saturation" | 

Direction of saturation processing used by the camera.

**Since**: 12

 |
| static const char \* OHOS\_IMAGE\_PROPERTY\_SHARPNESS = "Sharpness" | 

Direction of sharpness processing used by the camera.

**Since**: 12

 |
| static const char \* OHOS\_IMAGE\_PROPERTY\_DEVICE\_SETTING\_DESCRIPTION = "DeviceSettingDescription" | 

Information about the photographing conditions of a specific camera model.

**Since**: 12

 |
| static const char \* OHOS\_IMAGE\_PROPERTY\_SUBJECT\_DISTANCE\_RANGE = "SubjectDistanceRange" | 

Distance to the subject.

**Since**: 12

 |
| static const char \* OHOS\_IMAGE\_PROPERTY\_IMAGE\_UNIQUE\_ID = "ImageUniqueID" | 

Unique identifier assigned to each image.

**Since**: 12

 |
| static const char \* OHOS\_IMAGE\_PROPERTY\_GPS\_VERSION\_ID = "GPSVersionID" | 

Version of GPSInfoIFD.

**Since**: 12

 |
| static const char \* OHOS\_IMAGE\_PROPERTY\_GPS\_ALTITUDE\_REF = "GPSAltitudeRef" | 

Reference altitude for the GPS altitude.

**Since**: 12

 |
| static const char \* OHOS\_IMAGE\_PROPERTY\_GPS\_ALTITUDE = "GPSAltitude" | 

Altitude based on the reference in GPSAltitudeRef.

**Since**: 12

 |
| static const char \* OHOS\_IMAGE\_PROPERTY\_GPS\_SATELLITES = "GPSSatellites" | 

GPS satellites used for measurement.

**Since**: 12

 |
| static const char \* OHOS\_IMAGE\_PROPERTY\_GPS\_STATUS = "GPSStatus" | 

Status of the GPS receiver when the image was recorded.

**Since**: 12

 |
| static const char \* OHOS\_IMAGE\_PROPERTY\_GPS\_MEASURE\_MODE = "GPSMeasureMode" | 

GPS measurement pmode.

**Since**: 12

 |
| static const char \* OHOS\_IMAGE\_PROPERTY\_GPS\_DOP = "GPSDOP" | 

GPS DOP (data degree of precision)

**Since**: 12

 |
| static const char \* OHOS\_IMAGE\_PROPERTY\_GPS\_SPEED\_REF = "GPSSpeedRef" | 

Unit used to express the movement speed of the GPS receiver.

**Since**: 12

 |
| static const char \* OHOS\_IMAGE\_PROPERTY\_GPS\_SPEED = "GPSSpeed" | 

Movement speed of the GPS receiver.

**Since**: 12

 |
| static const char \* OHOS\_IMAGE\_PROPERTY\_GPS\_TRACK\_REF = "GPSTrackRef" | 

Reference of the movement direction of the GPS receiver.

**Since**: 12

 |
| static const char \* OHOS\_IMAGE\_PROPERTY\_GPS\_TRACK = "GPSTrack" | 

Movement direction of the GPS receiver.

**Since**: 12

 |
| static const char \* OHOS\_IMAGE\_PROPERTY\_GPS\_IMG\_DIRECTION\_REF = "GPSImgDirectionRef" | 

Reference of the direction of the image when it was captured.

**Since**: 12

 |
| static const char \* OHOS\_IMAGE\_PROPERTY\_GPS\_IMG\_DIRECTION = "GPSImgDirection" | 

Direction of the image when it was captured.

**Since**: 12

 |
| static const char \* OHOS\_IMAGE\_PROPERTY\_GPS\_MAP\_DATUM = "GPSMapDatum" | 

Geodetic survey data used by the GPS receiver.

**Since**: 12

 |
| static const char \* OHOS\_IMAGE\_PROPERTY\_GPS\_DEST\_LATITUDE\_REF = "GPSDestLatitudeRef" | 

Whether the latitude of the destination point is north or south latitude.

**Since**: 12

 |
| static const char \* OHOS\_IMAGE\_PROPERTY\_GPS\_DEST\_LATITUDE = "GPSDestLatitude" | 

Latitude of the destination point.

**Since**: 12

 |
| static const char \* OHOS\_IMAGE\_PROPERTY\_GPS\_DEST\_LONGITUDE\_REF = "GPSDestLongitudeRef" | 

Whether the longitude of the destination point is east or west longitude.

**Since**: 12

 |
| static const char \* OHOS\_IMAGE\_PROPERTY\_GPS\_PROCESSING\_METHOD = "GPSProcessingMethod" | 

String that records the name of the method used for positioning.

**Since**: 12

 |
| static const char \* OHOS\_IMAGE\_PROPERTY\_GPS\_AREA\_INFORMATION = "GPSAreaInformation" | 

String that records the name of the GPS area.

**Since**: 12

 |
| static const char \* OHOS\_IMAGE\_PROPERTY\_GPS\_DIFFERENTIAL = "GPSDifferential" | 

Whether differential correction is applied to the GPS receiver. It is critical to accurate location accuracy.

**Since**: 12

 |
| static const char \* OHOS\_IMAGE\_PROPERTY\_BODY\_SERIAL\_NUMBER = "BodySerialNumber" | 

Serial number of the camera body.

**Since**: 12

 |
| static const char \* OHOS\_IMAGE\_PROPERTY\_CAMERA\_OWNER\_NAME = "CameraOwnerName" | 

Name of the camera owner.

**Since**: 12

 |
| static const char \* OHOS\_IMAGE\_PROPERTY\_COMPOSITE\_IMAGE = "CompositeImage" | 

Whether the image is a composite image.

**Since**: 12

 |
| static const char \* OHOS\_IMAGE\_PROPERTY\_DNG\_VERSION = "DNGVersion" | 

DNG version. It encodes the DNG 4-tier version number.

**Since**: 12

 |
| static const char \* OHOS\_IMAGE\_PROPERTY\_GPS\_DEST\_LONGITUDE = "GPSDestLongitude" | 

Longitude of the destination point.

**Since**: 12

 |
| static const char \* OHOS\_IMAGE\_PROPERTY\_GPS\_DEST\_BEARING\_REF = "GPSDestBearingRef" | 

Reference of the bearing to the destination point.

**Since**: 12

 |
| static const char \* OHOS\_IMAGE\_PROPERTY\_GPS\_DEST\_BEARING = "GPSDestBearing" | 

Bearing to the destination point.

**Since**: 12

 |
| static const char \* OHOS\_IMAGE\_PROPERTY\_GPS\_DEST\_DISTANCE\_REF = "GPSDestDistanceRef" | 

Unit used to express the distance to the destination point.

**Since**: 12

 |
| static const char \* OHOS\_IMAGE\_PROPERTY\_GPS\_DEST\_DISTANCE = "GPSDestDistance" | 

Distance to the destination point.

**Since**: 12

 |
| static const char \* OHOS\_IMAGE\_PROPERTY\_DEFAULT\_CROP\_SIZE = "DefaultCropSize" | 

Size of the final image area, in raw image coordinates, taking into account extra pixels around the edges of the final image.

**Since**: 12

 |
| static const char \* OHOS\_IMAGE\_PROPERTY\_GAMMA = "Gamma" | 

Gamma value.

**Since**: 12

 |
| static const char \* OHOS\_IMAGE\_PROPERTY\_ISO\_SPEED\_LATITUDEYYY = "ISOSpeedLatitudeyyy" | 

ISO speed latitude yyy value of the camera or input device, which is defined in ISO 12232.

**Since**: 12

 |
| static const char \* OHOS\_IMAGE\_PROPERTY\_ISO\_SPEED\_LATITUDEZZZ = "ISOSpeedLatitudezzz" | 

ISO speed latitude zzz value of the camera or input device, which is defined in ISO 12232.

**Since**: 12

 |
| static const char \* OHOS\_IMAGE\_PROPERTY\_LENS\_MAKE = "LensMake" | 

Manufacturer of the lens.

**Since**: 12

 |
| static const char \* OHOS\_IMAGE\_PROPERTY\_LENS\_MODEL = "LensModel" | 

Model of the lens.

**Since**: 12

 |
| static const char \* OHOS\_IMAGE\_PROPERTY\_LENS\_SERIAL\_NUMBER = "LensSerialNumber" | 

Serial number of the lens.

**Since**: 12

 |
| static const char \* OHOS\_IMAGE\_PROPERTY\_LENS\_SPECIFICATION = "LensSpecification" | 

Specifications of the lens.

**Since**: 12

 |
| static const char \* OHOS\_IMAGE\_PROPERTY\_NEW\_SUBFILE\_TYPE = "NewSubfileType" | 

In Exif, the **NewSubfileType** field is used to identify the data type of a subfile. The value is a bit mask. The value 0 indicates a full-resolution image, **1** indicates a thumbnail, and **2** indicates a part of a multi-frame image.

**Since**: 12

 |
| static const char \* OHOS\_IMAGE\_PROPERTY\_OFFSET\_TIME = "OffsetTime" | 

In Exif, the **OffsetTime** field is used to identify the time with an offset from UTC when the image was captured, in the format of ±HH:MM.

**Since**: 12

 |
| static const char \* OHOS\_IMAGE\_PROPERTY\_OFFSET\_TIME\_DIGITIZED = "OffsetTimeDigitized" | 

Time with an offset from UTC when the image was digitized. It helps to accurately adjust the timestamp.

**Since**: 12

 |
| static const char \* OHOS\_IMAGE\_PROPERTY\_OFFSET\_TIME\_ORIGINAL = "OffsetTimeOriginal" | 

Time with an offset from UTC when the original image was created. It is critical for time-sensitive applications.

**Since**: 12

 |
| static const char \* OHOS\_IMAGE\_PROPERTY\_SOURCE\_EXPOSURE\_TIMES\_OF\_COMPOSITE\_IMAGE = "SourceExposureTimesOfCompositeImage" | 

Exposure time of source images of the composite image.

**Since**: 12

 |
| static const char \* OHOS\_IMAGE\_PROPERTY\_SOURCE\_IMAGE\_NUMBER\_OF\_COMPOSITE\_IMAGE = "SourceImageNumberOfCompositeImage" | 

Number of source images of the composite image.

**Since**: 12

 |
| static const char \* OHOS\_IMAGE\_PROPERTY\_SUBFILE\_TYPE = "SubfileType" | 

Type of data contained in this subfile. This tag has been deprecated. Use **NewSubfileType** instead.

**Since**: 12

 |
| static const char \* OHOS\_IMAGE\_PROPERTY\_GPS\_H\_POSITIONING\_ERROR = "GPSHPositioningError" | 

Horizontal positioning error, in meters.

**Since**: 12

 |
| static const char \* OHOS\_IMAGE\_PROPERTY\_PHOTOGRAPHIC\_SENSITIVITY = "PhotographicSensitivity" | 

Sensitivity of the camera or input device when the image was captured.

**Since**: 12

 |
| static const char \* OHOS\_IMAGE\_PROPERTY\_BURST\_NUMBER = "HwMnoteBurstNumber" | 

Number of burst shooting times.

**Since**: 12

 |
| static const char \* OHOS\_IMAGE\_PROPERTY\_FACE\_CONF = "HwMnoteFaceConf" | 

Face confidence.

**Since**: 12

 |
| static const char \* OHOS\_IMAGE\_PROPERTY\_FACE\_LEYE\_CENTER = "HwMnoteFaceLeyeCenter" | 

Left eye centered.

**Since**: 12

 |
| static const char \* OHOS\_IMAGE\_PROPERTY\_FACE\_MOUTH\_CENTER = "HwMnoteFaceMouthCenter" | 

Mouth centered.

**Since**: 12

 |
| static const char \* OHOS\_IMAGE\_PROPERTY\_FACE\_POINTER = "HwMnoteFacePointer" | 

Face pointer.

**Since**: 12

 |
| static const char \* OHOS\_IMAGE\_PROPERTY\_FACE\_RECT = "HwMnoteFaceRect" | 

Face rectangle.

**Since**: 12

 |
| static const char \* OHOS\_IMAGE\_PROPERTY\_FACE\_REYE\_CENTER = "HwMnoteFaceReyeCenter" | 

Right eye centered.

**Since**: 12

 |
| static const char \* OHOS\_IMAGE\_PROPERTY\_FACE\_SMILE\_SCORE = "HwMnoteFaceSmileScore" | 

Smile score of for faces.

**Since**: 12

 |
| static const char \* OHOS\_IMAGE\_PROPERTY\_FACE\_VERSION = "HwMnoteFaceVersion" | 

Facial recognition algorithm version.

**Since**: 12

 |
| static const char \* OHOS\_IMAGE\_PROPERTY\_FRONT\_CAMERA = "HwMnoteFrontCamera" | 

Whether the front camera is used to take a selfie.

**Since**: 12

 |
| static const char \* OHOS\_IMAGE\_PROPERTY\_SCENE\_POINTER = "HwMnoteScenePointer" | 

Pointer to the scene.

**Since**: 12

 |
| static const char \* OHOS\_IMAGE\_PROPERTY\_SCENE\_VERSION = "HwMnoteSceneVersion" | 

Scene algorithm version.

**Since**: 12

 |
| static const char \* OHOS\_IMAGE\_PROPERTY\_IS\_XMAGE\_SUPPORTED = "HwMnoteIsXmageSupported" | 

Whether XMAGE is supported.

**Since**: 12

 |
| static const char \* OHOS\_IMAGE\_PROPERTY\_XMAGE\_MODE = "HwMnoteXmageMode" | 

XMAGE watermark mode.

**Since**: 12

 |
| static const char \* OHOS\_IMAGE\_PROPERTY\_XMAGE\_LEFT = "HwMnoteXmageLeft" | 

X1 coordinate of the watermark region.

**Since**: 12

 |
| static const char \* OHOS\_IMAGE\_PROPERTY\_XMAGE\_TOP = "HwMnoteXmageTop" | 

Y1 coordinate of the watermark region.

**Since**: 12

 |
| static const char \* OHOS\_IMAGE\_PROPERTY\_XMAGE\_RIGHT = "HwMnoteXmageRight" | 

X2 coordinate of the watermark region.

**Since**: 12

 |
| static const char \* OHOS\_IMAGE\_PROPERTY\_XMAGE\_BOTTOM = "HwMnoteXmageBottom" | 

Y2 coordinate of the watermark region.

**Since**: 12

 |
| static const char \* OHOS\_IMAGE\_PROPERTY\_CLOUD\_ENHANCEMENT\_MODE = "HwMnoteCloudEnhancementMode" | 

Cloud enhancement mode.

**Since**: 12

 |
| static const char \* OHOS\_IMAGE\_PROPERTY\_WIND\_SNAPSHOT\_MODE = "HwMnoteWindSnapshotMode" | 

Motion snapshot mode.

**Since**: 12

 |
| static const char \* OHOS\_IMAGE\_PROPERTY\_GIF\_LOOP\_COUNT = "GIFLoopCount" | 

Number of GIF loops.

**Since**: 12

 |
| static const char \* OHOS\_IMAGE\_PROPERTY\_X\_IN\_ORIGINAL = "XInOriginal" | 

X coordinate of the top-left corner of the fragment map in the original image.

**Since**: 13

 |
| static const char \* OHOS\_IMAGE\_PROPERTY\_Y\_IN\_ORIGINAL = "YInOriginal" | 

Y coordinate of the top-left corner of the fragment map in the original image.

**Since**: 13

 |
| static const char \* OHOS\_IMAGE\_PROPERTY\_FRAGMENT\_WIDTH = "FragmentImageWidth" | 

Width of the fragment map.

**Since**: 13

 |
| static const char \* OHOS\_IMAGE\_PROPERTY\_FRAGMENT\_HEIGHT = "FragmentImageHeight" | 

Height of the fragment map.

**Since**: 13

 |
| static const char \* IMAGE\_PROPERTY\_GIF\_DELAY\_TIME = "GifDelayTime" | 

Duration for playing each frame of a GIF image, in milliseconds.

**Since**: 20

 |
| static const char \* IMAGE\_PROPERTY\_GIF\_DISPOSAL\_TYPE = "GifDisposalType" | 

Disposal type of each frame in a GIF image.

**Since**: 20

 |

#### Enum Description

#### \[h2\]Image\_ErrorCode

enum Image\_ErrorCode

**Description**

Enumerates the error codes.

**Since**: 12

| Enum Item | Description |
| :-- | :-- |
| IMAGE\_SUCCESS = 0 | Operation successful. |
| IMAGE\_BAD\_PARAMETER = 401 | Invalid parameter. |
| IMAGE\_UNSUPPORTED\_MIME\_TYPE = 7600101 | Unsupported MIME type. |
| IMAGE\_UNKNOWN\_MIME\_TYPE = 7600102 | Unknown MIME type. |
| IMAGE\_TOO\_LARGE = 7600103 | The data or image is too large. |
| IMAGE\_DMA\_NOT\_EXIST = 7600173 | The memory is not the DMA memory. |
| IMAGE\_DMA\_OPERATION\_FAILED = 7600174 | The operation on the DMA memory fails. |
| IMAGE\_UNSUPPORTED\_OPERATION = 7600201 | Unsupported operation. |
| IMAGE\_UNSUPPORTED\_METADATA = 7600202 | Unsupported metadata. |
| IMAGE\_UNSUPPORTED\_CONVERSION = 7600203 | Unsupported conversion. |
| IMAGE\_INVALID\_REGION = 7600204 | Invalid region. |
| IMAGE\_UNSUPPORTED\_MEMORY\_FORMAT = 7600205 | 
The memory format is not supported.

**Since**: 13

 |
| IMAGE\_INVALID\_PARAMETER = 7600206 | 

Invalid parameter.

**Since**: 19

 |
| IMAGE\_UNSUPPORTED\_DATA\_FORMAT = 7600207 | 

Unsupported data format.

**Since**: 22

 |
| IMAGE\_ALLOC\_FAILED = 7600301 | Failed to allocate the memory. |
| IMAGE\_COPY\_FAILED = 7600302 | Failed to copy the memory. |
| IMAGE\_LOCK\_UNLOCK\_FAILED = 7600303 | 

Failed to lock or unlock the memory.

**Since**: 15

 |
| IMAGE\_INIT\_FAILED = 7600304 | 

Initialization failed.

**Since**: 22

 |
| IMAGE\_CREATE\_PIXELMAP\_FAILED = 7600305 | 

Failed to create the PixelMap.

**Since**: 22

 |
| IMAGE\_ALLOCATOR\_MODE\_UNSUPPORTED = 7600501 | 

The memory allocator type is not supported, for example, creating HDR images using shared memory.

DMA memory supports HDR metadata.

**Since**: 20

 |
| IMAGE\_UNKNOWN\_ERROR = 7600901 | Unknown error. |
| IMAGE\_BAD\_SOURCE = 7700101 | Abnormal data source. |
| IMAGE\_SOURCE\_UNSUPPORTED\_MIME\_TYPE = 7700102 | 

Unsupported MIME type during image decoding.

**Since**: 15

 |
| IMAGE\_SOURCE\_TOO\_LARGE = 7700103 | 

The image is too large.

**Since**: 15

 |
| IMAGE\_SOURCE\_UNSUPPORTED\_ALLOCATOR\_TYPE = 7700201 | 

The allocator type is not supported. For example, decoding HDR images using shared memory is unsupported because only DMA supports HDR metadata.

**Since**: 15

 |
| IMAGE\_SOURCE\_UNSUPPORTED\_OPTIONS = 7700203 | 

Unsupported options. For example, an image cannot be converted into the required pixel format.

**Since**: 15

 |
| IMAGE\_SOURCE\_INVALID\_PARAMETER = 7700204 | 

Invalid **ImageSource** parameter.

**Since**: 19

 |
| IMAGE\_DECODE\_FAILED = 7700301 | Decoding failed. |
| IMAGE\_SOURCE\_ALLOC\_FAILED = 7700302 | 

Memory allocation failed.

**Since**: 15

 |
| IMAGE\_PACKER\_INVALID\_PARAMETER = 7800202 | 

Invalid **ImagePacker** parameter.

**Since**: 19

 |
| IMAGE\_ENCODE\_FAILED = 7800301 | Encoding failed. |
| IMAGE\_RECEIVER\_INVALID\_PARAMETER = 7900201 | 

Invalid **ImageReceiver** parameter.

**Since**: 20

 |

#### \[h2\]Image\_MetadataType

enum Image\_MetadataType

**Description**

Enumerates the metadata types.

**Since**: 13

| Enum Item | Description |
| :-- | :-- |
| EXIF\_METADATA = 1 | Exif metadata. |
| FRAGMENT\_METADATA = 2 | Fragment map metadata. |
| GIF\_METADATA = 5 | 
GIF image metadata.

**Since**: 20

 |

#### \[h2\]IMAGE\_ALLOCATOR\_MODE

enum IMAGE\_ALLOCATOR\_MODE

**Description**

Enumerates the types of memory allocation for a PixelMap.

**Since**: 20

| Enum Item | Description |
| :-- | :-- |
| IMAGE\_ALLOCATOR\_MODE\_AUTO = 0 | The system determines the type of memory to allocate when creating a PixelMap. |
| IMAGE\_ALLOCATOR\_MODE\_DMA = 1 | Allocates a DMA-type memory buffer. |
| IMAGE\_ALLOCATOR\_MODE\_SHARED\_MEMORY = 2 | Uses shared memory to create a PixelMap. |

#### Function Description

#### \[h2\]OH\_PictureMetadata\_Create()

Image\_ErrorCode OH\_PictureMetadata\_Create(Image\_MetadataType metadataType, OH\_PictureMetadata \*\*metadata)

**Description**

Creates the pointer to an OH\_PictureMetadata struct.

**Since**: 13

**Parameters**

| Name | Description |
| :-- | :-- |
| [Image\_MetadataType](#image_metadatatype) metadataType | Metadata type. |
| [OH\_PictureMetadata](../../structs/oh-picturemetadata/document.md) \*\*metadata | Double pointer to the OH\_PictureMetadata struct created. |

**Returns**

| Type | Description |
| :-- | :-- |
| [Image\_ErrorCode](#image_errorcode) | 
**IMAGE\_SUCCESS**: The operation is successful.

**IMAGE\_BAD\_PARAMETER**: A parameter is incorrect.

 |

#### \[h2\]OH\_PictureMetadata\_GetProperty()

Image\_ErrorCode OH\_PictureMetadata\_GetProperty(OH\_PictureMetadata \*metadata, Image\_String \*key, Image\_String \*value)

**Description**

Obtains a property of metadata based on the key. The **value.data** obtained through this API lacks the string terminator **\\0**. Please use it with caution.

**Since**: 13

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_PictureMetadata](../../structs/oh-picturemetadata/document.md) \*metadata | Pointer to an OH\_PictureMetadata struct. |
| [Image\_String](../../structs/image-string/document.md) \*key | Pointer to the key of the property. |
| [Image\_String](../../structs/image-string/document.md) \*value | Pointer to the value of the property. |

**Returns**

| Type | Description |
| :-- | :-- |
| [Image\_ErrorCode](#image_errorcode) | 
**IMAGE\_SUCCESS**: The operation is successful.

**IMAGE\_BAD\_PARAMETER**: A parameter is incorrect.

**IMAGE\_UNSUPPORTED\_METADATA**: The metadata type is not supported, or the metadata type and the auxiliary picture type do not match.

 |

#### \[h2\]OH\_PictureMetadata\_SetProperty()

Image\_ErrorCode OH\_PictureMetadata\_SetProperty(OH\_PictureMetadata \*metadata, Image\_String \*key, Image\_String \*value)

**Description**

Sets a property of metadata based on the key.

**Since**: 13

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_PictureMetadata](../../structs/oh-picturemetadata/document.md) \*metadata | Pointer to an OH\_PictureMetadata struct. |
| [Image\_String](../../structs/image-string/document.md) \*key | Pointer to the key of the property. |
| [Image\_String](../../structs/image-string/document.md) \*value | Pointer to the value of the property. |

**Returns**

| Type | Description |
| :-- | :-- |
| [Image\_ErrorCode](#image_errorcode) | 
**IMAGE\_SUCCESS**: The operation is successful.

**IMAGE\_BAD\_PARAMETER**: A parameter is incorrect.

**IMAGE\_UNSUPPORTED\_METADATA**: The metadata type is not supported, or the metadata type and the auxiliary picture type do not match.

 |

#### \[h2\]OH\_PictureMetadata\_GetPropertyWithNull()

Image\_ErrorCode OH\_PictureMetadata\_GetPropertyWithNull(OH\_PictureMetadata \*metadata, Image\_String \*key, Image\_String \*value)

**Description**

Obtains the metadata value of an OH\_PictureMetadata instance. The output of **value.data** ends with the string terminator **\\0**.

**Since**: 19

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_PictureMetadata](../../structs/oh-picturemetadata/document.md) \*metadata | Pointer to an OH\_PictureMetadata struct. |
| [Image\_String](../../structs/image-string/document.md) \*key | Pointer to the key of the property. |
| [Image\_String](../../structs/image-string/document.md) \*value | Pointer to the value of the property. |

**Returns**

| Type | Description |
| :-- | :-- |
| [Image\_ErrorCode](#image_errorcode) | 
**IMAGE\_SUCCESS**: The operation is successful.

**IMAGE\_INVALID\_PARAMETER**: The **metadata**, **key**, or **value** parameter is a null pointer.

**IMAGE\_UNSUPPORTED\_METADATA**: The metadata type is not supported, or the metadata type and the auxiliary picture type do not match.

 |

#### \[h2\]OH\_PictureMetadata\_Release()

Image\_ErrorCode OH\_PictureMetadata\_Release(OH\_PictureMetadata \*metadata)

**Description**

Releases the pointer to an OH\_PictureMetadata struct.

**Since**: 13

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_PictureMetadata](../../structs/oh-picturemetadata/document.md) \*metadata | Pointer to an OH\_PictureMetadata struct. |

**Returns**

| Type | Description |
| :-- | :-- |
| [Image\_ErrorCode](#image_errorcode) | 
**IMAGE\_SUCCESS**: The operation is successful.

**IMAGE\_BAD\_PARAMETER**: A parameter is incorrect.

 |

#### \[h2\]OH\_PictureMetadata\_Clone()

Image\_ErrorCode OH\_PictureMetadata\_Clone(OH\_PictureMetadata \*oldMetadata, OH\_PictureMetadata \*\*newMetadata)

**Description**

Clones metadata.

**Since**: 13

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_PictureMetadata](../../structs/oh-picturemetadata/document.md) \*oldMetadata | Pointer to an OH\_PictureMetadata struct. |
| [OH\_PictureMetadata](../../structs/oh-picturemetadata/document.md) \*\*newMetadata | Double pointer to the OH\_PictureMetadata struct obtained. |

**Returns**

| Type | Description |
| :-- | :-- |
| [Image\_ErrorCode](#image_errorcode) | 
**IMAGE\_SUCCESS**: The operation is successful.

**IMAGE\_BAD\_PARAMETER**: A parameter is incorrect.

**IMAGE\_ALLOC\_FAILED**: The memory allocation fails.

**IMAGE\_COPY\_FAILED**: The memory copy fails.

 |
