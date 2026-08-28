# native\_audio\_volume\_manager.h

#### Overview

The file declares the functions related to an audio volume manager.

You can call the functions to create an audio volume manager.

**File to include**: <ohaudio/native\_audio\_volume\_manager.h>

**Library**: libohaudio.so

**System capability**: SystemCapability.Multimedia.Audio.Core

**Since**: 20

**Related module**: [OHAudio](../../modules/ohaudio/document.md)

#### Summary

#### \[h2\]Structs

| Name | typedef Keyword | Description |
| :-- | :-- | :-- |
| [OH\_AudioVolumeManager](../../structs/oh-audiovolumemanager/document.md) | OH\_AudioVolumeManager | Describes an audio volume manager, which provides various functions for obtaining system volume information. |

#### \[h2\]Functions

| Name | typedef Keyword | Description |
| :-- | :-- | :-- |
| [typedef void (\*OH\_AudioVolumeManager\_OnStreamVolumeChangeCallback)(void \*userData, OH\_AudioStream\_Usage usage, int32\_t volumeLevel, bool updateUi)](#oh_audiovolumemanager_onstreamvolumechangecallback) | OH\_AudioVolumeManager\_OnStreamVolumeChangeCallback | Defines the prototype of the volume change callback function, which is passed in [OH\_AudioVolumeManager\_RegisterStreamVolumeChangeCallback](#oh_audiovolumemanager_registerstreamvolumechangecallback). |
| [typedef void (\*OH\_AudioVolumeManager\_OnRingerModeChangeCallback)(void \*userData, OH\_AudioRingerMode ringerMode)](#oh_audiovolumemanager_onringermodechangecallback) | OH\_AudioVolumeManager\_OnRingerModeChangeCallback | Defines the prototype of the ringer mode change callback function, which is passed in [OH\_AudioVolumeManager\_RegisterRingerModeChangeCallback](#oh_audiovolumemanager_registerringermodechangecallback). |
| [OH\_AudioCommon\_Result OH\_AudioManager\_GetAudioVolumeManager(OH\_AudioVolumeManager \*\*volumeManager)](#oh_audiomanager_getaudiovolumemanager) | \- | Obtains an OH\_AudioVolumeManager instance. |
| [OH\_AudioCommon\_Result OH\_AudioVolumeManager\_GetMaxVolumeByUsage(OH\_AudioVolumeManager \*volumeManager, OH\_AudioStream\_Usage usage, int32\_t \*maxVolumeLevel)](#oh_audiovolumemanager_getmaxvolumebyusage) | \- | Obtains the maximum volume level of an audio stream of a specified usage type. |
| [OH\_AudioCommon\_Result OH\_AudioVolumeManager\_GetMinVolumeByUsage(OH\_AudioVolumeManager \*volumeManager, OH\_AudioStream\_Usage usage, int32\_t \*minVolumeLevel)](#oh_audiovolumemanager_getminvolumebyusage) | \- | Obtains the minimum volume level of an audio stream of a specified usage type. |
| [OH\_AudioCommon\_Result OH\_AudioVolumeManager\_GetVolumeByUsage(OH\_AudioVolumeManager \*volumeManager, OH\_AudioStream\_Usage usage, int32\_t \*volumeLevel)](#oh_audiovolumemanager_getvolumebyusage) | \- | Obtains the system volume level of an audio stream of a specified usage type. |
| [OH\_AudioCommon\_Result OH\_AudioVolumeManager\_IsMuteByUsage(OH\_AudioVolumeManager \*volumeManager, OH\_AudioStream\_Usage usage, bool \*muted)](#oh_audiovolumemanager_ismutebyusage) | \- | Checks whether an audio stream of a specified usage type is muted. |
| [OH\_AudioCommon\_Result OH\_AudioVolumeManager\_RegisterStreamVolumeChangeCallback(OH\_AudioVolumeManager \*volumeManager, OH\_AudioStream\_Usage usage, OH\_AudioVolumeManager\_OnStreamVolumeChangeCallback callback, void \*userData)](#oh_audiovolumemanager_registerstreamvolumechangecallback) | \- | Registers the volume change callback function. |
| [OH\_AudioCommon\_Result OH\_AudioVolumeManager\_UnregisterStreamVolumeChangeCallback(OH\_AudioVolumeManager \*volumeManager, OH\_AudioVolumeManager\_OnStreamVolumeChangeCallback callback)](#oh_audiovolumemanager_unregisterstreamvolumechangecallback) | \- | Unregisters the volume change callback function. |
| [OH\_AudioCommon\_Result OH\_AudioVolumeManager\_GetRingerMode(OH\_AudioVolumeManager \*volumeManager, OH\_AudioRingerMode \*ringerMode)](#oh_audiovolumemanager_getringermode) | \- | Obtains the ringer mode in use. |
| [OH\_AudioCommon\_Result OH\_AudioVolumeManager\_RegisterRingerModeChangeCallback(OH\_AudioVolumeManager \*volumeManager, OH\_AudioVolumeManager\_OnRingerModeChangeCallback callback, void \*userData)](#oh_audiovolumemanager_registerringermodechangecallback) | \- | Registers the ringer mode change callback function. |
| [OH\_AudioCommon\_Result OH\_AudioVolumeManager\_UnregisterRingerModeChangeCallback(OH\_AudioVolumeManager \*volumeManager, OH\_AudioVolumeManager\_OnRingerModeChangeCallback callback)](#oh_audiovolumemanager_unregisterringermodechangecallback) | \- | Unregisters the ringer mode change callback function. |

#### Function Description

#### \[h2\]OH\_AudioVolumeManager\_OnStreamVolumeChangeCallback()

typedef void (\*OH\_AudioVolumeManager\_OnStreamVolumeChangeCallback)(void \*userData, OH\_AudioStream\_Usage usage, int32\_t volumeLevel, bool updateUi)

**Description**

Defines the prototype of the volume change callback function, which is passed in [OH\_AudioVolumeManager\_RegisterStreamVolumeChangeCallback](#oh_audiovolumemanager_registerstreamvolumechangecallback).

**Since**: 20

**Parameters**

| Name | Description |
| :-- | :-- |
| void \*userData | Pointer to user data. |
| [OH\_AudioStream\_Usage](../native-audiostream-base-h/document.md#oh_audiostream_usage) usage | Usage type of the audio stream for which the volume is changed. |
| int32\_t volumeLevel | Volume level after change. |
| bool updateUi | Whether to show the volume change on the UI. **true** to show, **false** otherwise. |

#### \[h2\]OH\_AudioVolumeManager\_OnRingerModeChangeCallback()

typedef void (\*OH\_AudioVolumeManager\_OnRingerModeChangeCallback)(void \*userData, OH\_AudioRingerMode ringerMode)

**Description**

Defines the prototype of the ringer mode change callback function, which is passed in [OH\_AudioVolumeManager\_RegisterRingerModeChangeCallback](#oh_audiovolumemanager_registerringermodechangecallback).

**Since**: 20

**Parameters**

| Name | Description |
| :-- | :-- |
| void \*userData | Pointer to user data. |
| [OH\_AudioRingerMode](../native-audio-common-h/document.md#oh_audioringermode) ringerMode | Ringer mode after change. |

#### \[h2\]OH\_AudioManager\_GetAudioVolumeManager()

OH\_AudioCommon\_Result OH\_AudioManager\_GetAudioVolumeManager(OH\_AudioVolumeManager \*\*volumeManager)

**Description**

Obtains an OH\_AudioVolumeManager instance.

**Since**: 20

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_AudioVolumeManager](../../structs/oh-audiovolumemanager/document.md) \*\*volumeManager | Double pointer to an OH\_AudioVolumeManager instance, which is used to receive the created audio volume manager instance. |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_AudioCommon\_Result](../native-audio-common-h/document.md#oh_audiocommon_result) | 
**AUDIOCOMMON\_RESULT\_SUCCESS**: The function is executed successfully.

**AUDIOCOMMON\_RESULT\_ERROR\_INVALID\_PARAM**: The **volumeManager** parameter is nullptr.

 |

#### \[h2\]OH\_AudioVolumeManager\_GetMaxVolumeByUsage()

OH\_AudioCommon\_Result OH\_AudioVolumeManager\_GetMaxVolumeByUsage(OH\_AudioVolumeManager \*volumeManager, OH\_AudioStream\_Usage usage, int32\_t \*maxVolumeLevel)

**Description**

Obtains the maximum volume level of an audio stream of a specified usage type.

**Since**: 20

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_AudioVolumeManager](../../structs/oh-audiovolumemanager/document.md) \*volumeManager | Pointer to an OH\_AudioVolumeManager instance. |
| [OH\_AudioStream\_Usage](../native-audiostream-base-h/document.md#oh_audiostream_usage) usage | Usage type of the audio stream. |
| int32\_t \*maxVolumeLevel | Pointer to the maximum volume level. |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_AudioCommon\_Result](../native-audio-common-h/document.md#oh_audiocommon_result) | 
**AUDIOCOMMON\_RESULT\_SUCCESS**: The function is executed successfully.

**AUDIOCOMMON\_RESULT\_ERROR\_INVALID\_PARAM**: The **volumeManager** or **maxVolumeLevel** parameter is nullptr, or **usage** is invalid.

**AUDIOCOMMON\_RESULT\_ERROR\_SYSTEM**: A system processing error occurs.

 |

#### \[h2\]OH\_AudioVolumeManager\_GetMinVolumeByUsage()

OH\_AudioCommon\_Result OH\_AudioVolumeManager\_GetMinVolumeByUsage(OH\_AudioVolumeManager \*volumeManager, OH\_AudioStream\_Usage usage, int32\_t \*minVolumeLevel)

**Description**

Obtains the minimum volume level of an audio stream of a specified usage type.

**Since**: 20

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_AudioVolumeManager](../../structs/oh-audiovolumemanager/document.md) \*volumeManager | Pointer to an OH\_AudioVolumeManager instance. |
| [OH\_AudioStream\_Usage](../native-audiostream-base-h/document.md#oh_audiostream_usage) usage | Usage type of the audio stream. |
| int32\_t \*minVolumeLevel | Pointer to the minimum volume level. |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_AudioCommon\_Result](../native-audio-common-h/document.md#oh_audiocommon_result) | 
**AUDIOCOMMON\_RESULT\_SUCCESS**: The function is executed successfully.

**AUDIOCOMMON\_RESULT\_ERROR\_INVALID\_PARAM**: The **volumeManager** or **minVolumeLevel** parameter is nullptr, or **usage** is invalid.

**AUDIOCOMMON\_RESULT\_ERROR\_SYSTEM**: A system processing error occurs.

 |

#### \[h2\]OH\_AudioVolumeManager\_GetVolumeByUsage()

OH\_AudioCommon\_Result OH\_AudioVolumeManager\_GetVolumeByUsage(OH\_AudioVolumeManager \*volumeManager, OH\_AudioStream\_Usage usage, int32\_t \*volumeLevel)

**Description**

Obtains the system volume level of an audio stream of a specified usage type.

**Since**: 20

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_AudioVolumeManager](../../structs/oh-audiovolumemanager/document.md) \*volumeManager | Pointer to an OH\_AudioVolumeManager instance. |
| [OH\_AudioStream\_Usage](../native-audiostream-base-h/document.md#oh_audiostream_usage) usage | Usage type of the audio stream. |
| int32\_t \*volumeLevel | Pointer to the system volume level. |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_AudioCommon\_Result](../native-audio-common-h/document.md#oh_audiocommon_result) | 
**AUDIOCOMMON\_RESULT\_SUCCESS**: The function is executed successfully.

**AUDIOCOMMON\_RESULT\_ERROR\_INVALID\_PARAM**: The **volumeManager** or **volumeLevel** parameter is nullptr, or **usage** is invalid.

**AUDIOCOMMON\_RESULT\_ERROR\_SYSTEM**: A system processing error occurs.

 |

#### \[h2\]OH\_AudioVolumeManager\_IsMuteByUsage()

OH\_AudioCommon\_Result OH\_AudioVolumeManager\_IsMuteByUsage(OH\_AudioVolumeManager \*volumeManager, OH\_AudioStream\_Usage usage, bool \*muted)

**Description**

Checks whether an audio stream of a specified usage type is muted.

**Since**: 20

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_AudioVolumeManager](../../structs/oh-audiovolumemanager/document.md) \*volumeManager | Pointer to an OH\_AudioVolumeManager instance. |
| [OH\_AudioStream\_Usage](../native-audiostream-base-h/document.md#oh_audiostream_usage) usage | Usage type of the audio stream. |
| bool \*muted | Pointer to the check result for whether the audio stream is muted. **true** if muted, **false** otherwise. |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_AudioCommon\_Result](../native-audio-common-h/document.md#oh_audiocommon_result) | 
**AUDIOCOMMON\_RESULT\_SUCCESS**: The function is executed successfully.

**AUDIOCOMMON\_RESULT\_ERROR\_INVALID\_PARAM**: The **volumeManager** or **muted** parameter is nullptr, or **usage** is invalid.

**AUDIOCOMMON\_RESULT\_ERROR\_SYSTEM**: A system processing error occurs.

 |

#### \[h2\]OH\_AudioVolumeManager\_RegisterStreamVolumeChangeCallback()

OH\_AudioCommon\_Result OH\_AudioVolumeManager\_RegisterStreamVolumeChangeCallback(OH\_AudioVolumeManager \*volumeManager, OH\_AudioStream\_Usage usage, OH\_AudioVolumeManager\_OnStreamVolumeChangeCallback callback, void \*userData)

**Description**

Registers the volume change callback function.

**Since**: 20

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_AudioVolumeManager](../../structs/oh-audiovolumemanager/document.md) \*volumeManager | Pointer to an OH\_AudioVolumeManager instance. |
| [OH\_AudioStream\_Usage](../native-audiostream-base-h/document.md#oh_audiostream_usage) usage | Usage type of the audio stream. |
| [OH\_AudioVolumeManager\_OnStreamVolumeChangeCallback](#oh_audiovolumemanager_onstreamvolumechangecallback) callback | [OH\_AudioVolumeManager\_OnStreamVolumeChangeCallback](#oh_audiovolumemanager_onstreamvolumechangecallback), which is called when the volume of the audio stream changes. |
| void \*userData | Pointer to user data. |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_AudioCommon\_Result](../native-audio-common-h/document.md#oh_audiocommon_result) | 
**AUDIOCOMMON\_RESULT\_SUCCESS**: The function is executed successfully.

**AUDIOCOMMON\_RESULT\_ERROR\_INVALID\_PARAM**: The **volumeManager**, **usage**, or **callback** parameter is nullptr, or **usage** is invalid.

**AUDIOCOMMON\_RESULT\_ERROR\_SYSTEM**: A system processing error occurs.

 |

#### \[h2\]OH\_AudioVolumeManager\_UnregisterStreamVolumeChangeCallback()

OH\_AudioCommon\_Result OH\_AudioVolumeManager\_UnregisterStreamVolumeChangeCallback(OH\_AudioVolumeManager \*volumeManager, OH\_AudioVolumeManager\_OnStreamVolumeChangeCallback callback)

**Description**

Unregisters the volume change callback function.

**Since**: 20

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_AudioVolumeManager](../../structs/oh-audiovolumemanager/document.md) \*volumeManager | Pointer to an OH\_AudioVolumeManager instance. |
| [OH\_AudioVolumeManager\_OnStreamVolumeChangeCallback](#oh_audiovolumemanager_onstreamvolumechangecallback) callback | Pointer to the callback function passed by [OH\_AudioVolumeManager\_RegisterStreamVolumeChangeCallback](#oh_audiovolumemanager_registerstreamvolumechangecallback). |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_AudioCommon\_Result](../native-audio-common-h/document.md#oh_audiocommon_result) | 
**AUDIOCOMMON\_RESULT\_SUCCESS**: The function is executed successfully.

**AUDIOCOMMON\_RESULT\_ERROR\_INVALID\_PARAM**: The **volumeManager** or **callback** parameter is nullptr.

**AUDIOCOMMON\_RESULT\_ERROR\_SYSTEM**: A system processing error occurs.

 |

#### \[h2\]OH\_AudioVolumeManager\_GetRingerMode()

OH\_AudioCommon\_Result OH\_AudioVolumeManager\_GetRingerMode(OH\_AudioVolumeManager \*volumeManager, OH\_AudioRingerMode \*ringerMode)

**Description**

Obtains the ringer mode in use.

**Since**: 20

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_AudioVolumeManager](../../structs/oh-audiovolumemanager/document.md) \*volumeManager | Pointer to an OH\_AudioVolumeManager instance. |
| [OH\_AudioRingerMode](../native-audio-common-h/document.md#oh_audioringermode) \*ringerMode | Pointer to the ringer mode. |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_AudioCommon\_Result](../native-audio-common-h/document.md#oh_audiocommon_result) | 
**AUDIOCOMMON\_RESULT\_SUCCESS**: The function is executed successfully.

**AUDIOCOMMON\_RESULT\_ERROR\_INVALID\_PARAM**: The **volumeManager** or **ringerMode** parameter is nullptr.

**AUDIOCOMMON\_RESULT\_ERROR\_SYSTEM**: A system processing error occurs.

 |

#### \[h2\]OH\_AudioVolumeManager\_RegisterRingerModeChangeCallback()

OH\_AudioCommon\_Result OH\_AudioVolumeManager\_RegisterRingerModeChangeCallback(OH\_AudioVolumeManager \*volumeManager, OH\_AudioVolumeManager\_OnRingerModeChangeCallback callback, void \*userData)

**Description**

Registers the ringer mode change callback function.

**Since**: 20

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_AudioVolumeManager](../../structs/oh-audiovolumemanager/document.md) \*volumeManager | Pointer to an OH\_AudioVolumeManager instance. |
| [OH\_AudioVolumeManager\_OnRingerModeChangeCallback](#oh_audiovolumemanager_onringermodechangecallback) callback | [OH\_AudioVolumeManager\_OnRingerModeChangeCallback](#oh_audiovolumemanager_onringermodechangecallback), which is called when the ringer mode changes. |
| void \*userData | Pointer to user data. |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_AudioCommon\_Result](../native-audio-common-h/document.md#oh_audiocommon_result) | 
**AUDIOCOMMON\_RESULT\_SUCCESS**: The function is executed successfully.

**AUDIOCOMMON\_RESULT\_ERROR\_INVALID\_PARAM**: The **volumeManager** or **callback** parameter is nullptr.

**AUDIOCOMMON\_RESULT\_ERROR\_SYSTEM**: A system processing error occurs.

 |

#### \[h2\]OH\_AudioVolumeManager\_UnregisterRingerModeChangeCallback()

OH\_AudioCommon\_Result OH\_AudioVolumeManager\_UnregisterRingerModeChangeCallback(OH\_AudioVolumeManager \*volumeManager, OH\_AudioVolumeManager\_OnRingerModeChangeCallback callback)

**Description**

Unregisters the ringer mode change callback function.

**Since**: 20

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_AudioVolumeManager](../../structs/oh-audiovolumemanager/document.md) \*volumeManager | Pointer to an OH\_AudioVolumeManager instance. |
| [OH\_AudioVolumeManager\_OnRingerModeChangeCallback](#oh_audiovolumemanager_onringermodechangecallback) callback | Pointer to the callback function passed by [OH\_AudioVolumeManager\_RegisterRingerModeChangeCallback](#oh_audiovolumemanager_registerringermodechangecallback). |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_AudioCommon\_Result](../native-audio-common-h/document.md#oh_audiocommon_result) | 
**AUDIOCOMMON\_RESULT\_SUCCESS**: The function is executed successfully.

**AUDIOCOMMON\_RESULT\_ERROR\_INVALID\_PARAM**: The **volumeManager** or **callback** parameter is nullptr.

**AUDIOCOMMON\_RESULT\_ERROR\_SYSTEM**: A system processing error occurs.

 |
