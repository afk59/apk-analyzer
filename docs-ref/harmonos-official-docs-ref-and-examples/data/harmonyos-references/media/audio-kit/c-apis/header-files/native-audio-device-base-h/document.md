# native\_audio\_device\_base.h

#### Overview

The file declares the types of audio device parameters and the functions for obtaining these parameters.

**Library**: libohaudio.so

**File to include**: <ohaudio/native\_audio\_device\_base.h>

**System capability**: SystemCapability.Multimedia.Audio.Core

**Since**: 12

**Related module**: [OHAudio](../../modules/ohaudio/document.md)

#### Summary

#### \[h2\]Structs

| Name | typedef Keyword | Description |
| :-- | :-- | :-- |
| [OH\_AudioDeviceDescriptorArray](../../structs/oh-audiodevicedescriptorarray/document.md) | OH\_AudioDeviceDescriptorArray | Describes an array of audio device descriptors. |
| [OH\_AudioDeviceDescriptor](../../structs/oh-audiodevicedescriptor/document.md) | OH\_AudioDeviceDescriptor | Describes an audio device descriptor, which provides attributes of an audio device. |

#### \[h2\]Enums

| Name | typedef Keyword | Description |
| :-- | :-- | :-- |
| [OH\_AudioDevice\_ChangeType](#oh_audiodevice_changetype) | OH\_AudioDevice\_ChangeType | Enumerates the types of audio device changes. |
| [OH\_AudioDevice\_Role](#oh_audiodevice_role) | OH\_AudioDevice\_Role | Enumerates the roles of audio devices. |
| [OH\_AudioDevice\_Type](#oh_audiodevice_type) | OH\_AudioDevice\_Type | Enumerates the types of audio devices. |
| [OH\_AudioDevice\_Flag](#oh_audiodevice_flag) | OH\_AudioDevice\_Flag | Enumerates the flags of audio devices. |
| [OH\_AudioDevice\_Usage](#oh_audiodevice_usage) | OH\_AudioDevice\_Usage | Enumerates the usage scenarios of audio devices. |
| [OH\_AudioDevice\_BlockStatus](#oh_audiodevice_blockstatus) | OH\_AudioDevice\_BlockStatus | Enumerates the blocked status of audio devices. By default, an audio device is not blocked. |

#### \[h2\]Functions

| Name | Description |
| :-- | :-- |
| [OH\_AudioCommon\_Result OH\_AudioDeviceDescriptor\_GetDeviceRole(OH\_AudioDeviceDescriptor \*audioDeviceDescriptor, OH\_AudioDevice\_Role \*deviceRole)](#oh_audiodevicedescriptor_getdevicerole) | Obtains the device role based on an audio device descriptor. |
| [OH\_AudioCommon\_Result OH\_AudioDeviceDescriptor\_GetDeviceType(OH\_AudioDeviceDescriptor \*audioDeviceDescriptor, OH\_AudioDevice\_Type \*deviceType)](#oh_audiodevicedescriptor_getdevicetype) | Obtains the device type based on an audio device descriptor. |
| [OH\_AudioCommon\_Result OH\_AudioDeviceDescriptor\_GetDeviceId(OH\_AudioDeviceDescriptor \*audioDeviceDescriptor, uint32\_t \*id)](#oh_audiodevicedescriptor_getdeviceid) | Obtains the device ID based on an audio device descriptor. |
| [OH\_AudioCommon\_Result OH\_AudioDeviceDescriptor\_GetDeviceName(OH\_AudioDeviceDescriptor \*audioDeviceDescriptor, char \*\*name)](#oh_audiodevicedescriptor_getdevicename) | Obtains the device name based on an audio device descriptor. |
| [OH\_AudioCommon\_Result OH\_AudioDeviceDescriptor\_GetDeviceAddress(OH\_AudioDeviceDescriptor \*audioDeviceDescriptor, char \*\*address)](#oh_audiodevicedescriptor_getdeviceaddress) | Obtains the device address based on an audio device descriptor. |
| [OH\_AudioCommon\_Result OH\_AudioDeviceDescriptor\_GetDeviceSampleRates(OH\_AudioDeviceDescriptor \*audioDeviceDescriptor, uint32\_t \*\*sampleRates, uint32\_t \*size)](#oh_audiodevicedescriptor_getdevicesamplerates) | Obtains the sample rates based on an audio device descriptor. |
| [OH\_AudioCommon\_Result OH\_AudioDeviceDescriptor\_GetDeviceChannelCounts(OH\_AudioDeviceDescriptor \*audioDeviceDescriptor, uint32\_t \*\*channelCounts, uint32\_t \*size)](#oh_audiodevicedescriptor_getdevicechannelcounts) | Obtains an array that holds the number of device channels based on an audio device descriptor. |
| [OH\_AudioCommon\_Result OH\_AudioDeviceDescriptor\_GetDeviceDisplayName(OH\_AudioDeviceDescriptor \*audioDeviceDescriptor, char \*\*displayName)](#oh_audiodevicedescriptor_getdevicedisplayname) | Obtains the device display name based on an audio device descriptor. |
| [OH\_AudioCommon\_Result OH\_AudioDeviceDescriptor\_GetDeviceEncodingTypes(OH\_AudioDeviceDescriptor \*audioDeviceDescriptor, OH\_AudioStream\_EncodingType \*\*encodingTypes, uint32\_t \*size)](#oh_audiodevicedescriptor_getdeviceencodingtypes) | Obtains the device encoding types based on an audio device descriptor. |

#### Enum Description

#### \[h2\]OH\_AudioDevice\_ChangeType

enum OH\_AudioDevice\_ChangeType

**Description**

Enumerates the types of audio device changes.

**Since**: 12

| Enum Item | Description |
| :-- | :-- |
| AUDIO\_DEVICE\_CHANGE\_TYPE\_CONNECT = 0 | Device connected. |
| AUDIO\_DEVICE\_CHANGE\_TYPE\_DISCONNECT = 1 | Device disconnected. |

#### \[h2\]OH\_AudioDevice\_Role

enum OH\_AudioDevice\_Role

**Description**

Enumerates the roles of audio devices.

**Since**: 12

| Enum Item | Description |
| :-- | :-- |
| AUDIO\_DEVICE\_ROLE\_INPUT = 1 | Input device. |
| AUDIO\_DEVICE\_ROLE\_OUTPUT = 2 | Output device. |

#### \[h2\]OH\_AudioDevice\_Type

enum OH\_AudioDevice\_Type

**Description**

Enumerates the types of audio devices.

**Since**: 12

| Enum Item | Description |
| :-- | :-- |
| AUDIO\_DEVICE\_TYPE\_INVALID = 0 | Invalid device. |
| AUDIO\_DEVICE\_TYPE\_EARPIECE = 1 | Earpiece. |
| AUDIO\_DEVICE\_TYPE\_SPEAKER = 2 | Speaker. |
| AUDIO\_DEVICE\_TYPE\_WIRED\_HEADSET = 3 | Wired headset with a microphone. |
| AUDIO\_DEVICE\_TYPE\_WIRED\_HEADPHONES = 4 | Wired headset without microphone. |
| AUDIO\_DEVICE\_TYPE\_BLUETOOTH\_SCO = 7 | Bluetooth device using Synchronous Connection-oriented (SCO) links. |
| AUDIO\_DEVICE\_TYPE\_BLUETOOTH\_A2DP = 8 | Bluetooth device using Advanced Audio Distribution Profile (A2DP) links. |
| AUDIO\_DEVICE\_TYPE\_MIC = 15 | Microphone. |
| AUDIO\_DEVICE\_TYPE\_USB\_HEADSET = 22 | USB headset. |
| AUDIO\_DEVICE\_TYPE\_DISPLAY\_PORT = 23 | Display port device. |
| AUDIO\_DEVICE\_TYPE\_REMOTE\_CAST = 24 | Remote cast device. |
| AUDIO\_DEVICE\_TYPE\_USB\_DEVICE = 25 | 
USB device (excluding USB headsets).

**Since**: 18

 |
| AUDIO\_DEVICE\_TYPE\_ACCESSORY = 26 | 

Accessory device, such as the microphone on a remote control.

**Since**: 19

 |
| AUDIO\_DEVICE\_TYPE\_HDMI = 27 | 

HDMI device (such as HDMI, ARC, and eARC).

**Since**: 19

 |
| AUDIO\_DEVICE\_TYPE\_LINE\_DIGITAL = 28 | 

Wired digital device (such as S/PDIF)

**Since**: 19

 |
| AUDIO\_DEVICE\_TYPE\_HEARING\_AID = 30 | 

Hearing aid device.

**Since**: 20

 |
| AUDIO\_DEVICE\_TYPE\_NEARLINK = 31 | 

NearLink device.

**Since**: 20

 |
| AUDIO\_DEVICE\_TYPE\_DEFAULT = 1000 | Default device type. |

#### \[h2\]OH\_AudioDevice\_Flag

enum OH\_AudioDevice\_Flag

**Description**

Enumerates the flags of audio devices.

**Since**: 12

| Enum Item | Description |
| :-- | :-- |
| AUDIO\_DEVICE\_FLAG\_NONE = 0 | No flag. |
| AUDIO\_DEVICE\_FLAG\_OUTPUT = 1 | Output device. |
| AUDIO\_DEVICE\_FLAG\_INPUT = 2 | Input device. |
| AUDIO\_DEVICE\_FLAG\_ALL = 3 | All devices. |

#### \[h2\]OH\_AudioDevice\_Usage

enum OH\_AudioDevice\_Usage

**Description**

Enumerates the usage scenarios of audio devices.

**Since**: 12

| Enum Item | Description |
| :-- | :-- |
| AUDIO\_DEVICE\_USAGE\_MEDIA\_OUTPUT = 1 | Media output device. |
| AUDIO\_DEVICE\_USAGE\_MEDIA\_INPUT = 2 | Media input device. |
| AUDIO\_DEVICE\_USAGE\_MEDIA\_ALL = 3 | All media devices. |
| AUDIO\_DEVICE\_USAGE\_CALL\_OUTPUT = 4 | Call output device. |
| AUDIO\_DEVICE\_USAGE\_CALL\_INPUT = 8 | Call input device. |
| AUDIO\_DEVICE\_USAGE\_CALL\_ALL = 12 | All call devices. |

#### \[h2\]OH\_AudioDevice\_BlockStatus

enum OH\_AudioDevice\_BlockStatus

**Description**

Enumerates the blocked status of audio devices. By default, an audio device is not blocked.

**Since**: 13

| Enum Item | Description |
| :-- | :-- |
| AUDIO\_DEVICE\_UNBLOCKED = 0 | The audio device is not blocked. |
| AUDIO\_DEVICE\_BLOCKED = 1 | The audio device is blocked. |

#### Function Description

#### \[h2\]OH\_AudioDeviceDescriptor\_GetDeviceRole()

OH\_AudioCommon\_Result OH\_AudioDeviceDescriptor\_GetDeviceRole(OH\_AudioDeviceDescriptor \*audioDeviceDescriptor,OH\_AudioDevice\_Role \*deviceRole)

**Description**

Obtains the device role based on an audio device descriptor.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_AudioDeviceDescriptor](../../structs/oh-audiodevicedescriptor/document.md) \*audioDeviceDescriptor | Pointer to an audio device descriptor, which is obtained by calling [OH\_AudioRoutingManager\_GetDevices](../native-audio-routing-manager-h/document.md#oh_audioroutingmanager_getdevices) or [OH\_AudioRoutingManager\_OnDeviceChangedCallback](../native-audio-routing-manager-h/document.md#oh_audioroutingmanager_ondevicechangedcallback). |
| [OH\_AudioDevice\_Role](#oh_audiodevice_role) \*deviceRole | Pointer to the device role. This variable, which will store the device role value, points to an [OH\_AudioDevice\_Role](#oh_audiodevice_role). |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_AudioCommon\_Result](../native-audio-common-h/document.md#oh_audiocommon_result) | Operation result. **AUDIOCOMMON\_RESULT\_SUCCESS** is returned if the operation is successful; **AUDIOCOMMON\_RESULT\_ERROR\_INVALID\_PARAM** is returned otherwise. |

#### \[h2\]OH\_AudioDeviceDescriptor\_GetDeviceType()

OH\_AudioCommon\_Result OH\_AudioDeviceDescriptor\_GetDeviceType(OH\_AudioDeviceDescriptor \*audioDeviceDescriptor,OH\_AudioDevice\_Type \*deviceType)

**Description**

Obtains the device type based on an audio device descriptor.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_AudioDeviceDescriptor](../../structs/oh-audiodevicedescriptor/document.md) \*audioDeviceDescriptor | Pointer to an audio device descriptor, which is obtained by calling [OH\_AudioRoutingManager\_GetDevices](../native-audio-routing-manager-h/document.md#oh_audioroutingmanager_getdevices) or [OH\_AudioRoutingManager\_OnDeviceChangedCallback](../native-audio-routing-manager-h/document.md#oh_audioroutingmanager_ondevicechangedcallback). |
| [OH\_AudioDevice\_Type](#oh_audiodevice_type) \*deviceType | Pointer to the device type. This variable, which will store the device type value, points to an [OH\_AudioDevice\_Type](#oh_audiodevice_type). |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_AudioCommon\_Result](../native-audio-common-h/document.md#oh_audiocommon_result) | Operation result. **AUDIOCOMMON\_RESULT\_SUCCESS** is returned if the operation is successful; **AUDIOCOMMON\_RESULT\_ERROR\_INVALID\_PARAM** is returned otherwise. |

#### \[h2\]OH\_AudioDeviceDescriptor\_GetDeviceId()

OH\_AudioCommon\_Result OH\_AudioDeviceDescriptor\_GetDeviceId(OH\_AudioDeviceDescriptor \*audioDeviceDescriptor,uint32\_t \*id)

**Description**

Obtains the device ID based on an audio device descriptor.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_AudioDeviceDescriptor](../../structs/oh-audiodevicedescriptor/document.md) \*audioDeviceDescriptor | Pointer to an audio device descriptor, which is obtained by calling [OH\_AudioRoutingManager\_GetDevices](../native-audio-routing-manager-h/document.md#oh_audioroutingmanager_getdevices) or [OH\_AudioRoutingManager\_OnDeviceChangedCallback](../native-audio-routing-manager-h/document.md#oh_audioroutingmanager_ondevicechangedcallback). |
| uint32\_t \*id | Pointer to the device ID, which is a variable for setting the device role. |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_AudioCommon\_Result](../native-audio-common-h/document.md#oh_audiocommon_result) | Operation result. **AUDIOCOMMON\_RESULT\_SUCCESS** is returned if the operation is successful; **AUDIOCOMMON\_RESULT\_ERROR\_INVALID\_PARAM** is returned otherwise. |

#### \[h2\]OH\_AudioDeviceDescriptor\_GetDeviceName()

OH\_AudioCommon\_Result OH\_AudioDeviceDescriptor\_GetDeviceName(OH\_AudioDeviceDescriptor \*audioDeviceDescriptor,char \*\*name)

**Description**

Obtains the device name based on an audio device descriptor.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_AudioDeviceDescriptor](../../structs/oh-audiodevicedescriptor/document.md) \*audioDeviceDescriptor | Pointer to an audio device descriptor, which is obtained by calling [OH\_AudioRoutingManager\_GetDevices](../native-audio-routing-manager-h/document.md#oh_audioroutingmanager_getdevices) or [OH\_AudioRoutingManager\_OnDeviceChangedCallback](../native-audio-routing-manager-h/document.md#oh_audioroutingmanager_ondevicechangedcallback). |
| char \*\*name | 
Double pointer to the device name.

Do not release the pointer to the device name separately. Instead, call [OH\_AudioRoutingManager\_ReleaseDevices](../native-audio-routing-manager-h/document.md#oh_audioroutingmanager_releasedevices) to release all the device descriptors when they are no longer needed.

 |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_AudioCommon\_Result](../native-audio-common-h/document.md#oh_audiocommon_result) | Operation result. **AUDIOCOMMON\_RESULT\_SUCCESS** is returned if the operation is successful; **AUDIOCOMMON\_RESULT\_ERROR\_INVALID\_PARAM** is returned otherwise. |

#### \[h2\]OH\_AudioDeviceDescriptor\_GetDeviceAddress()

OH\_AudioCommon\_Result OH\_AudioDeviceDescriptor\_GetDeviceAddress(OH\_AudioDeviceDescriptor \*audioDeviceDescriptor,char \*\*address)

**Description**

Obtains the device address based on an audio device descriptor.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_AudioDeviceDescriptor](../../structs/oh-audiodevicedescriptor/document.md) \*audioDeviceDescriptor | Pointer to an audio device descriptor, which is obtained by calling [OH\_AudioRoutingManager\_GetDevices](../native-audio-routing-manager-h/document.md#oh_audioroutingmanager_getdevices) or [OH\_AudioRoutingManager\_OnDeviceChangedCallback](../native-audio-routing-manager-h/document.md#oh_audioroutingmanager_ondevicechangedcallback). |
| char \*\*address | 
Double pointer to the MAC address of the device.

Do not release the pointer to the MAC address separately. Instead, call [OH\_AudioRoutingManager\_ReleaseDevices](../native-audio-routing-manager-h/document.md#oh_audioroutingmanager_releasedevices) to release all the device descriptors when they are no longer needed.

 |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_AudioCommon\_Result](../native-audio-common-h/document.md#oh_audiocommon_result) | Operation result. **AUDIOCOMMON\_RESULT\_SUCCESS** is returned if the operation is successful; **AUDIOCOMMON\_RESULT\_ERROR\_INVALID\_PARAM** is returned otherwise. |

#### \[h2\]OH\_AudioDeviceDescriptor\_GetDeviceSampleRates()

OH\_AudioCommon\_Result OH\_AudioDeviceDescriptor\_GetDeviceSampleRates(OH\_AudioDeviceDescriptor \*audioDeviceDescriptor,uint32\_t \*\*sampleRates, uint32\_t \*size)

**Description**

Obtains the sample rates based on an audio device descriptor.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_AudioDeviceDescriptor](../../structs/oh-audiodevicedescriptor/document.md) \*audioDeviceDescriptor | Pointer to an audio device descriptor, which is obtained by calling [OH\_AudioRoutingManager\_GetDevices](../native-audio-routing-manager-h/document.md#oh_audioroutingmanager_getdevices) or [OH\_AudioRoutingManager\_OnDeviceChangedCallback](../native-audio-routing-manager-h/document.md#oh_audioroutingmanager_ondevicechangedcallback). |
| uint32\_t \*\*sampleRates | 
Double pointer to the array of sample rates.

Do not release the pointer to the sample rates separately. Instead, call [OH\_AudioRoutingManager\_ReleaseDevices](../native-audio-routing-manager-h/document.md#oh_audioroutingmanager_releasedevices) to release all the device descriptors when they are no longer needed.

 |
| uint32\_t \*size | Pointer to the size of the array. |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_AudioCommon\_Result](../native-audio-common-h/document.md#oh_audiocommon_result) | Operation result. **AUDIOCOMMON\_RESULT\_SUCCESS** is returned if the operation is successful; **AUDIOCOMMON\_RESULT\_ERROR\_INVALID\_PARAM** is returned otherwise. |

#### \[h2\]OH\_AudioDeviceDescriptor\_GetDeviceChannelCounts()

OH\_AudioCommon\_Result OH\_AudioDeviceDescriptor\_GetDeviceChannelCounts(OH\_AudioDeviceDescriptor \*audioDeviceDescriptor,uint32\_t \*\*channelCounts, uint32\_t \*size)

**Description**

Obtains an array that holds the number of device channels based on an audio device descriptor.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_AudioDeviceDescriptor](../../structs/oh-audiodevicedescriptor/document.md) \*audioDeviceDescriptor | Pointer to an audio device descriptor, which is obtained by calling [OH\_AudioRoutingManager\_GetDevices](../native-audio-routing-manager-h/document.md#oh_audioroutingmanager_getdevices) or [OH\_AudioRoutingManager\_OnDeviceChangedCallback](../native-audio-routing-manager-h/document.md#oh_audioroutingmanager_ondevicechangedcallback). |
| uint32\_t \*\*channelCounts | 
Double pointer to the array that holds the channel counts.

Do not release the pointer to the channel counts separately. Instead, call [OH\_AudioRoutingManager\_ReleaseDevices](../native-audio-routing-manager-h/document.md#oh_audioroutingmanager_releasedevices) to release all the device descriptors when they are no longer needed.

 |
| uint32\_t \*size | Pointer to the size of the array. |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_AudioCommon\_Result](../native-audio-common-h/document.md#oh_audiocommon_result) | Operation result. **AUDIOCOMMON\_RESULT\_SUCCESS** is returned if the operation is successful; **AUDIOCOMMON\_RESULT\_ERROR\_INVALID\_PARAM** is returned otherwise. |

#### \[h2\]OH\_AudioDeviceDescriptor\_GetDeviceDisplayName()

OH\_AudioCommon\_Result OH\_AudioDeviceDescriptor\_GetDeviceDisplayName(OH\_AudioDeviceDescriptor \*audioDeviceDescriptor,char \*\*displayName)

**Description**

Obtains the device display name based on an audio device descriptor.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_AudioDeviceDescriptor](../../structs/oh-audiodevicedescriptor/document.md) \*audioDeviceDescriptor | Pointer to an audio device descriptor, which is obtained by calling [OH\_AudioRoutingManager\_GetDevices](../native-audio-routing-manager-h/document.md#oh_audioroutingmanager_getdevices) or [OH\_AudioRoutingManager\_OnDeviceChangedCallback](../native-audio-routing-manager-h/document.md#oh_audioroutingmanager_ondevicechangedcallback). |
| char \*\*displayName | 
Double pointer to the display name.

Do not release the pointer to the display name separately. Instead, call [OH\_AudioRoutingManager\_ReleaseDevices](../native-audio-routing-manager-h/document.md#oh_audioroutingmanager_releasedevices) to release all the device descriptors when they are no longer needed.

 |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_AudioCommon\_Result](../native-audio-common-h/document.md#oh_audiocommon_result) | Operation result. **AUDIOCOMMON\_RESULT\_SUCCESS** is returned if the operation is successful; **AUDIOCOMMON\_RESULT\_ERROR\_INVALID\_PARAM** is returned otherwise. |

#### \[h2\]OH\_AudioDeviceDescriptor\_GetDeviceEncodingTypes()

OH\_AudioCommon\_Result OH\_AudioDeviceDescriptor\_GetDeviceEncodingTypes(OH\_AudioDeviceDescriptor \*audioDeviceDescriptor,OH\_AudioStream\_EncodingType \*\*encodingTypes, uint32\_t \*size)

**Description**

Obtains the device encoding types based on an audio device descriptor.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_AudioDeviceDescriptor](../../structs/oh-audiodevicedescriptor/document.md) \*audioDeviceDescriptor | Pointer to an audio device descriptor, which is obtained by calling [OH\_AudioRoutingManager\_GetDevices](../native-audio-routing-manager-h/document.md#oh_audioroutingmanager_getdevices) or [OH\_AudioRoutingManager\_OnDeviceChangedCallback](../native-audio-routing-manager-h/document.md#oh_audioroutingmanager_ondevicechangedcallback). |
| [OH\_AudioStream\_EncodingType](../native-audiostream-base-h/document.md#oh_audiostream_encodingtype) \*\*encodingTypes | 
Double pointer to the device encoding type. For details about the available options, see [OH\_AudioStream\_EncodingType](../native-audiostream-base-h/document.md#oh_audiostream_encodingtype).

Do not release the pointer to the encoding type separately. Instead, call [OH\_AudioRoutingManager\_ReleaseDevices](../native-audio-routing-manager-h/document.md#oh_audioroutingmanager_releasedevices) to release all the device descriptors when they are no longer needed.

 |
| uint32\_t \*size | Pointer to the size of the device encoding type. |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_AudioCommon\_Result](../native-audio-common-h/document.md#oh_audiocommon_result) | Operation result. **AUDIOCOMMON\_RESULT\_SUCCESS** is returned if the operation is successful; **AUDIOCOMMON\_RESULT\_ERROR\_INVALID\_PARAM** is returned otherwise. |
