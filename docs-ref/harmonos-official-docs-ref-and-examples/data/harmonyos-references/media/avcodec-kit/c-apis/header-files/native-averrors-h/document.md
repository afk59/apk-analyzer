# native\_averrors.h

#### Overview

The file declares the error codes used by the media framework.

**File to include**: <multimedia/player\_framework/native\_averrors.h>

**Library**: libnative\_media\_core.so

**System capability**: SystemCapability.Multimedia.Media.Core

**Since**: 9

**Related module**: [Core](../../modules/core/document.md)

#### Summary

#### \[h2\]Enums

| Name | typedef Keyword | Description |
| :-- | :-- | :-- |
| [OH\_AVErrCode](#oh_averrcode) | OH\_AVErrCode | Enumerates the error codes used by the media framework. |

#### Enum Description

#### \[h2\]OH\_AVErrCode

enum OH\_AVErrCode

**Description**

Enumerates the error codes used by the media framework.

**System capability**: SystemCapability.Multimedia.Media.Core

**Since**: 9

| Value | Description |
| :-- | :-- |
| AV\_ERR\_OK = 0 | Operation successful. |
| AV\_ERR\_NO\_MEMORY = 1 | No memory. |
| AV\_ERR\_OPERATE\_NOT\_PERMIT = 2 | Operation not allowed. |
| AV\_ERR\_INVALID\_VAL = 3 | Invalid value. |
| AV\_ERR\_IO = 4 | I/O error. |
| AV\_ERR\_TIMEOUT = 5 | Timeout. |
| AV\_ERR\_UNKNOWN = 6 | Unknown error. |
| AV\_ERR\_SERVICE\_DIED = 7 | Unavailable service. |
| AV\_ERR\_INVALID\_STATE = 8 | Unsupported operation in this state. |
| AV\_ERR\_UNSUPPORT = 9 | Unsupported API. |
| AV\_ERR\_INPUT\_DATA\_ERROR = 10 | 
Incorrect input data.

**Since**: 12

 |
| AV\_ERR\_UNSUPPORTED\_FORMAT = 11 | 

Unsupported format.

**Since**: 18

 |
| AV\_ERR\_EXTEND\_START = 100 | Initial value for extended error codes. |
| AV\_ERR\_DRM\_BASE = 200 | 

DRM start error code.

**Since**: 12

 |
| AV\_ERR\_DRM\_DECRYPT\_FAILED = 201 | 

DRM decryption fails.

**Since**: 12

 |
| AV\_ERR\_VIDEO\_BASE = 300 | 

Video start error code.

**Since**: 12

 |
| AV\_ERR\_VIDEO\_UNSUPPORTED\_COLOR\_SPACE\_CONVERSION = 301 | 

Color Space Conversion (CSC) is not supported.

**Since**: 12

 |
| AV\_ERR\_IO\_CANNOT\_FIND\_HOST = 5411001 | 

The host is not found. The possible cause is that the server address is incorrect.

**Since**: 14

 |
| AV\_ERR\_IO\_CONNECTION\_TIMEOUT = 5411002 | 

Network connection times out.

**Since**: 14

 |
| AV\_ERR\_IO\_NETWORK\_ABNORMAL = 5411003 | 

The connection fails due to a network error.

**Since**: 14

 |
| AV\_ERR\_IO\_NETWORK\_UNAVAILABLE = 5411004 | 

The connection fails due to network unavailability.

**Since**: 14

 |
| AV\_ERR\_IO\_NO\_PERMISSION = 5411005 | 

No network access permission.

**Since**: 14

 |
| AV\_ERR\_IO\_NETWORK\_ACCESS\_DENIED = 5411006 | 

The client request parameter is incorrect or exceeds the processing capability.

**Since**: 14

 |
| AV\_ERR\_IO\_RESOURCE\_NOT\_FOUND = 5411007 | 

No network resource is available.

**Since**: 14

 |
| AV\_ERR\_IO\_SSL\_CLIENT\_CERT\_NEEDED = 5411008 | 

Server authentication fails because the client certificate is not carried, is invalid, or has expired.

**Since**: 14

 |
| AV\_ERR\_IO\_SSL\_CONNECT\_FAIL = 5411009 | 

Client authentication fails because the server certificate is not carried, is invalid, or has expired.

**Since**: 14

 |
| AV\_ERR\_IO\_SSL\_SERVER\_CERT\_UNTRUSTED = 5411010 | 

The SSL server certificate is untrusted.

**Since**: 14

 |
| AV\_ERR\_IO\_UNSUPPORTED\_REQUEST = 5411011 | 

The network protocol does not support the request.

**Since**: 14

 |
| AV\_ERR\_STREAM\_CHANGED = 5410005 | 

The stream format changes in synchronous mode. You can call [OH\_VideoEncoder\_GetOutputDescription](../native-avcodec-videoencoder-h/document.md#oh_videoencoder_getoutputdescription) (video encoding), [OH\_VideoDecoder\_GetOutputDescription](../native-avcodec-videodecoder-h/document.md#oh_videodecoder_getoutputdescription) (video decoding), or [OH\_AudioCodec\_GetOutputDescription](../native-avcodec-audiocodec-h/document.md#oh_audiocodec_getoutputdescription) (audio encoding and decoding) to obtain the new stream configuration.

**Since**: 20

 |
| AV\_ERR\_TRY\_AGAIN\_LATER = 5410006 | 

The temporary buffer query fails in synchronous mode. You are advised to wait for a short period of time and try again.

**Since**: 20

 |
