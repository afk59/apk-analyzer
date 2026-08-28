# image\_mdk\_common.h

#### Overview

The file declares the common enums and structs used by the image interface.

**File to include**: <multimedia/image\_framework/image\_mdk\_common.h>

**Library**: libimage\_ndk.z.so

**System capability**: SystemCapability.Multimedia.Image.Core

**Since**: 10

**Related module**: [Image](../../modules/image/document.md)

#### Summary

#### \[h2\]Macros

| Name | Description |
| :-- | :-- |
| IMAGE\_RESULT\_BASE 62980096 | 
Common image error code, indicating that the operation fails.

**Since**: 10

 |

#### \[h2\]Structs

| Name | typedef Keyword | Description |
| :-- | :-- | :-- |
| [OhosImageSize](../../structs/ohosimagesize/document.md) | \- | Describes the image size. It is a member variable of [OhosImageDecodingOps](../../structs/ohosimagedecodingops/document.md). |

#### \[h2\]Enums

| Name | typedef Keyword | Description |
| :-- | :-- | :-- |
| [IRNdkErrCode](#irndkerrcode) | IRNdkErrCode | Enumerates the return values that may be used by the interface. |

#### Enum Description

#### \[h2\]IRNdkErrCode

enum IRNdkErrCode

**Description**

Enumerates the return values that may be used by the interface.

**Since**: 10

| Enum Item | Description |
| :-- | :-- |
| IMAGE\_RESULT\_SUCCESS = 0 | Operation succeeded. |
| IMAGE\_RESULT\_BAD\_PARAMETER = -1 | Invalid parameter. |
| IMAGE\_RESULT\_IMAGE\_RESULT\_BASE = IMAGE\_RESULT\_BASE | Operation failed. |
| IMAGE\_RESULT\_ERR\_IPC = IMAGE\_RESULT\_BASE + 1 | IPC error. |
| IMAGE\_RESULT\_ERR\_SHAMEM\_NOT\_EXIST = IMAGE\_RESULT\_BASE + 2 | Sharing the memory fails. |
| IMAGE\_RESULT\_ERR\_SHAMEM\_DATA\_ABNORMAL = IMAGE\_RESULT\_BASE + 3 | Abnormal data in the shared memory. |
| IMAGE\_RESULT\_DECODE\_ABNORMAL = IMAGE\_RESULT\_BASE + 4 | Failed to decode the image. |
| IMAGE\_RESULT\_DATA\_ABNORMAL = IMAGE\_RESULT\_BASE + 5 | Abnormal input data. |
| IMAGE\_RESULT\_MALLOC\_ABNORMAL = IMAGE\_RESULT\_BASE + 6 | An error occurs during memory allocation. |
| IMAGE\_RESULT\_DATA\_UNSUPPORT = IMAGE\_RESULT\_BASE + 7 | The image type is not supported. |
| IMAGE\_RESULT\_INIT\_ABNORMAL = IMAGE\_RESULT\_BASE + 8 | Failed to initialize the image. |
| IMAGE\_RESULT\_GET\_DATA\_ABNORMAL = IMAGE\_RESULT\_BASE + 9 | An error occurs during image data retrieval. |
| IMAGE\_RESULT\_TOO\_LARGE = IMAGE\_RESULT\_BASE + 10 | The image is too large. |
| IMAGE\_RESULT\_TRANSFORM = IMAGE\_RESULT\_BASE + 11 | An error occurs during image transformation. |
| IMAGE\_RESULT\_COLOR\_CONVERT = IMAGE\_RESULT\_BASE + 12 | An error occurs during image color conversion. |
| IMAGE\_RESULT\_CROP = IMAGE\_RESULT\_BASE + 13 | An error occurs during image cropping. |
| IMAGE\_RESULT\_SOURCE\_DATA = IMAGE\_RESULT\_BASE + 14 | The image source data is incorrect. |
| IMAGE\_RESULT\_SOURCE\_DATA\_INCOMPLETE = IMAGE\_RESULT\_BASE + 15 | The image source data is incomplete. |
| IMAGE\_RESULT\_MISMATCHED\_FORMAT = IMAGE\_RESULT\_BASE + 16 | The image format does not match. |
| IMAGE\_RESULT\_UNKNOWN\_FORMAT = IMAGE\_RESULT\_BASE + 17 | Unknown image format. |
| IMAGE\_RESULT\_SOURCE\_UNRESOLVED = IMAGE\_RESULT\_BASE + 18 | The image source is not parsed. |
| IMAGE\_RESULT\_INVALID\_PARAMETER = IMAGE\_RESULT\_BASE + 19 | Invalid image parameter. |
| IMAGE\_RESULT\_DECODE\_FAILED = IMAGE\_RESULT\_BASE + 20 | Failed to decode the image. |
| IMAGE\_RESULT\_PLUGIN\_REGISTER\_FAILED = IMAGE\_RESULT\_BASE + 21 | Failed to register the plug-in. |
| IMAGE\_RESULT\_PLUGIN\_CREATE\_FAILED = IMAGE\_RESULT\_BASE + 22 | Failed to create the plug-in. |
| IMAGE\_RESULT\_ENCODE\_FAILED = IMAGE\_RESULT\_BASE + 23 | Failed to encode the image. |
| IMAGE\_RESULT\_ADD\_PIXEL\_MAP\_FAILED = IMAGE\_RESULT\_BASE + 24 | Failed to add the PixelMap. |
| IMAGE\_RESULT\_HW\_DECODE\_UNSUPPORT = IMAGE\_RESULT\_BASE + 25 | Hardware decoding is not supported. |
| IMAGE\_RESULT\_DECODE\_HEAD\_ABNORMAL = IMAGE\_RESULT\_BASE + 26 | Failed to decode the image header. |
| IMAGE\_RESULT\_DECODE\_EXIF\_UNSUPPORT = IMAGE\_RESULT\_BASE + 27 | Exchangeable Image File (Exif) is not supported for image decoding. |
| IMAGE\_RESULT\_PROPERTY\_NOT\_EXIST = IMAGE\_RESULT\_BASE + 28 | The image property does not exist. |
| IMAGE\_RESULT\_MEDIA\_DATA\_UNSUPPORT = IMAGE\_RESULT\_BASE + 30 | The media type is not supported. |
| IMAGE\_RESULT\_MEDIA\_TOO\_LARGE = IMAGE\_RESULT\_BASE + 31 | The media is too large. |
| IMAGE\_RESULT\_MEDIA\_MALLOC\_FAILED = IMAGE\_RESULT\_BASE + 32 | Memory allocation failed. |
| IMAGE\_RESULT\_MEDIA\_END\_OF\_STREAM = IMAGE\_RESULT\_BASE + 33 | Failed to end the media data stream. |
| IMAGE\_RESULT\_MEDIA\_IO\_ABNORMAL = IMAGE\_RESULT\_BASE + 34 | Abnormal input and output streams. |
| IMAGE\_RESULT\_MEDIA\_MALFORMED = IMAGE\_RESULT\_BASE + 35 | The media service functions abnormally. |
| IMAGE\_RESULT\_MEDIA\_BUFFER\_TOO\_SMALL = IMAGE\_RESULT\_BASE + 36 | The media data is too small. |
| IMAGE\_RESULT\_MEDIA\_OUT\_OF\_RANGE = IMAGE\_RESULT\_BASE + 37 | The media is out of range. |
| IMAGE\_RESULT\_MEDIA\_STATUS\_ABNORMAL = IMAGE\_RESULT\_BASE + 38 | Abnormal media status. |
| IMAGE\_RESULT\_MEDIA\_VALUE\_INVALID = IMAGE\_RESULT\_BASE + 39 | Invalid media value. |
| IMAGE\_RESULT\_MEDIA\_NULL\_POINTER = IMAGE\_RESULT\_BASE + 40 | Media operation failed. |
| IMAGE\_RESULT\_MEDIA\_INVALID\_OPERATION = IMAGE\_RESULT\_BASE + 41 | Invalid media operation. |
| IMAGE\_RESULT\_MEDIA\_ERR\_PLAYER\_NOT\_INIT = IMAGE\_RESULT\_BASE + 42 | An error occurs during media initialization. |
| IMAGE\_RESULT\_MEDIA\_EARLY\_PREPARE = IMAGE\_RESULT\_BASE + 43 | Media preprocessing is carried out too early. |
| IMAGE\_RESULT\_MEDIA\_SEEK\_ERR = IMAGE\_RESULT\_BASE + 44 | The seek operation failed. |
| IMAGE\_RESULT\_MEDIA\_PERMISSION\_DENIED = IMAGE\_RESULT\_BASE + 45 | Permission denied. |
| IMAGE\_RESULT\_MEDIA\_DEAD\_OBJECT = IMAGE\_RESULT\_BASE + 46 | The media object is deregistered. |
| IMAGE\_RESULT\_MEDIA\_TIMED\_OUT = IMAGE\_RESULT\_BASE + 47 | A timeout occurs. |
| IMAGE\_RESULT\_MEDIA\_TRACK\_NOT\_ALL\_SUPPORTED = IMAGE\_RESULT\_BASE + 48 | The media capability is not supported. |
| IMAGE\_RESULT\_MEDIA\_ADAPTER\_INIT\_FAILED = IMAGE\_RESULT\_BASE + 49 | Failed to initialize the media adapter. |
| IMAGE\_RESULT\_MEDIA\_WRITE\_PARCEL\_FAIL = IMAGE\_RESULT\_BASE + 50 | Failed to write data to the parcel. |
| IMAGE\_RESULT\_MEDIA\_READ\_PARCEL\_FAIL = IMAGE\_RESULT\_BASE + 51 | Failed to read data from the parcel. |
| IMAGE\_RESULT\_MEDIA\_NO\_AVAIL\_BUFFER = IMAGE\_RESULT\_BASE + 52 | Invalid data. |
| IMAGE\_RESULT\_MEDIA\_INVALID\_PARAM = IMAGE\_RESULT\_BASE + 53 | Invalid parameters. |
| IMAGE\_RESULT\_MEDIA\_CODEC\_ADAPTER\_NOT\_EXIST = IMAGE\_RESULT\_BASE + 54 | The media codec adapter does not exist. |
| IMAGE\_RESULT\_MEDIA\_CREATE\_CODEC\_ADAPTER\_FAILED = IMAGE\_RESULT\_BASE + 55 | Failed to create the media codec adapter. |
| IMAGE\_RESULT\_MEDIA\_CODEC\_ADAPTER\_NOT\_INIT = IMAGE\_RESULT\_BASE + 56 | The media codec adapter is not initialized. |
| IMAGE\_RESULT\_MEDIA\_ZCODEC\_CREATE\_FAILED = IMAGE\_RESULT\_BASE + 57 | Failed to create media codec. |
| IMAGE\_RESULT\_MEDIA\_ZCODEC\_NOT\_EXIST = IMAGE\_RESULT\_BASE + 58 | Media codec not found. |
| IMAGE\_RESULT\_MEDIA\_JNI\_CLASS\_NOT\_EXIST = IMAGE\_RESULT\_BASE + 59 | The media JNI layer class does not exist. |
| IMAGE\_RESULT\_MEDIA\_JNI\_METHOD\_NOT\_EXIST = IMAGE\_RESULT\_BASE + 60 | The media JNI layer method does not exist. |
| IMAGE\_RESULT\_MEDIA\_JNI\_NEW\_OBJ\_FAILED = IMAGE\_RESULT\_BASE + 61 | Failed to create the object at the media JNI layer. |
| IMAGE\_RESULT\_MEDIA\_JNI\_COMMON\_ERROR = IMAGE\_RESULT\_BASE + 62 | The media JNI layer is abnormal. |
| IMAGE\_RESULT\_MEDIA\_DISTRIBUTE\_NOT\_SUPPORT = IMAGE\_RESULT\_BASE + 63 | Media distribution is not supported. |
| IMAGE\_RESULT\_MEDIA\_SOURCE\_NOT\_SET = IMAGE\_RESULT\_BASE + 64 | The media source is not set. |
| IMAGE\_RESULT\_MEDIA\_RTSP\_ADAPTER\_NOT\_INIT = IMAGE\_RESULT\_BASE + 65 | The media RTSP adapter is not initialized. |
| IMAGE\_RESULT\_MEDIA\_RTSP\_ADAPTER\_NOT\_EXIST = IMAGE\_RESULT\_BASE + 66 | The media RTSP adapter does not exist. |
| IMAGE\_RESULT\_MEDIA\_RTSP\_SURFACE\_UNSUPPORT = IMAGE\_RESULT\_BASE + 67 | The media does not support the RTSP surface. |
| IMAGE\_RESULT\_MEDIA\_RTSP\_CAPTURE\_NOT\_INIT = IMAGE\_RESULT\_BASE + 68 | Failed to initialize the media RTSP capturer. |
| IMAGE\_RESULT\_MEDIA\_RTSP\_SOURCE\_URL\_INVALID = IMAGE\_RESULT\_BASE + 69 | Invalid media RTSP source path. |
| IMAGE\_RESULT\_MEDIA\_RTSP\_VIDEO\_TRACK\_NOT\_FOUND = IMAGE\_RESULT\_BASE + 70 | No video capability is found in the media RTSP. |
| IMAGE\_RESULT\_MEDIA\_RTSP\_CAMERA\_NUM\_REACH\_MAX = IMAGE\_RESULT\_BASE + 71 | The maximum number of RTSP cameras has been reached. |
| IMAGE\_RESULT\_MEDIA\_SET\_VOLUME = IMAGE\_RESULT\_BASE + 72 | Failed to set the volume. |
| IMAGE\_RESULT\_MEDIA\_NUMBER\_OVERFLOW = IMAGE\_RESULT\_BASE + 73 | The number of operations overflows. |
| IMAGE\_RESULT\_MEDIA\_DIS\_PLAYER\_UNSUPPORTED = IMAGE\_RESULT\_BASE + 74 | The distributed media player is not supported. |
| IMAGE\_RESULT\_MEDIA\_DENCODE\_ICC\_FAILED = IMAGE\_RESULT\_BASE + 75 | Failed to decode the ICC. |
| IMAGE\_RESULT\_MEDIA\_ENCODE\_ICC\_FAILED = IMAGE\_RESULT\_BASE + 76 | Failed to encode the ICC. |
| IMAGE\_RESULT\_MEDIA\_READ\_PIXELMAP\_FAILED = IMAGE\_RESULT\_BASE + 150 | Failed to read the PixelMap. |
| IMAGE\_RESULT\_MEDIA\_WRITE\_PIXELMAP\_FAILED = IMAGE\_RESULT\_BASE + 151 | Failed to write the PixelMap. |
| IMAGE\_RESULT\_MEDIA\_PIXELMAP\_NOT\_ALLOW\_MODIFY = IMAGE\_RESULT\_BASE + 152 | The PixelMap cannot be modified. |
| IMAGE\_RESULT\_MEDIA\_CONFIG\_FAILED = IMAGE\_RESULT\_BASE + 153 | Configuration failed. |
| IMAGE\_RESULT\_JNI\_ENV\_ABNORMAL = IMAGE\_RESULT\_BASE + 154 | The JNI environment is abnormal. |
| IMAGE\_RESULT\_SURFACE\_GRALLOC\_BUFFER\_FAILED = IMAGE\_RESULT\_BASE + 155 | Failed to allocate memory for the surface. |
| IMAGE\_RESULT\_CREATE\_SURFACE\_FAILED = IMAGE\_RESULT\_BASE + 156 | Failed to create the surface. |
| IMAGE\_RESULT\_SURFACE\_GET\_PARAMETER\_FAILED = IMAGE\_RESULT\_BASE + 157 | Failed to obtain parameters from the surface. |
| IMAGE\_RESULT\_GET\_SURFACE\_FAILED = IMAGE\_RESULT\_BASE + 158 | Failed to obtain the surface. |
| IMAGE\_RESULT\_SURFACE\_ACQUIRE\_BUFFER\_FAILED = IMAGE\_RESULT\_BASE + 159 | Failed to allocate the memory. |
| IMAGE\_RESULT\_SURFACE\_REQUEST\_BUFFER\_FAILED = IMAGE\_RESULT\_BASE + 160 | Failed to allocate the memory. |
| IMAGE\_RESULT\_REGISTER\_LISTENER\_FAILED = IMAGE\_RESULT\_BASE + 161 | Failed to register the listener. |
| IMAGE\_RESULT\_REGISTER\_BUFFER\_FAILED = IMAGE\_RESULT\_BASE + 162 | Failed to register the buffer. |
| IMAGE\_RESULT\_FREAD\_FAILED = IMAGE\_RESULT\_BASE + 163 | Failed to read the file. |
| IMAGE\_RESULT\_PEEK\_FAILED = IMAGE\_RESULT\_BASE + 164 | Failed to peek the file. |
| IMAGE\_RESULT\_SEEK\_FAILED = IMAGE\_RESULT\_BASE + 165 | Failed to seek the file. |
| IMAGE\_RESULT\_STREAM\_SIZE\_ERROR = IMAGE\_RESULT\_BASE + 166 | The data stream is damaged. |
| IMAGE\_RESULT\_FILE\_FD\_ERROR = IMAGE\_RESULT\_BASE + 167 | The file descriptor is corrupted. |
| IMAGE\_RESULT\_FILE\_DAMAGED = IMAGE\_RESULT\_BASE + 168 | The file is damaged. |
| IMAGE\_RESULT\_CREATE\_DECODER\_FAILED = IMAGE\_RESULT\_BASE + 169 | Failed to create a decoder. |
| IMAGE\_RESULT\_CREATE\_ENCODER\_FAILED = IMAGE\_RESULT\_BASE + 170 | Failed to create an encoder. |
| IMAGE\_RESULT\_CHECK\_FORMAT\_ERROR = IMAGE\_RESULT\_BASE + 171 | Failed to check the format. |
| IMAGE\_RESULT\_THIRDPART\_SKIA\_ERROR = IMAGE\_RESULT\_BASE + 172 | Skia decoding failed. |
| IMAGE\_RESULT\_HW\_DECODE\_FAILED = IMAGE\_RESULT\_BASE + 173 | Hardware decoding failed. |
| IMAGE\_RESULT\_ALLOCATER\_TYPE\_ERROR = IMAGE\_RESULT\_BASE + 174 | Failed to verify the memory type. |
| IMAGE\_RESULT\_ALPHA\_TYPE\_ERROR = IMAGE\_RESULT\_BASE + 175 | Failed to verify the alpha type. |
| IMAGE\_RESULT\_INDEX\_INVALID = IMAGE\_RESULT\_BASE + 176 | Invalid parameter. |
| IMAGE\_RESULT\_MEDIA\_UNKNOWN = IMAGE\_RESULT\_BASE + 200 | Unknown error. |
