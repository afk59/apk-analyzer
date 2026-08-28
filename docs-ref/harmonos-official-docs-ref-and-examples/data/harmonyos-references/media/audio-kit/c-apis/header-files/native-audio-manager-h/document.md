# native\_audio\_manager.h

#### Overview

The file declares the functions related to an audio manager.

**File to include**: <ohaudio/native\_audio\_manager.h>

**Library**: libohaudio.so

**System capability**: SystemCapability.Multimedia.Audio.Core

**Since**: 12

**Related module**: [OHAudio](../../modules/ohaudio/document.md)

#### Summary

#### \[h2\]Structs

| Name | typedef Keyword | Description |
| :-- | :-- | :-- |
| [OH\_AudioManager](../../structs/oh-audiomanager/document.md) | OH\_AudioManager | Describes an audio manager, which is used for audio management. |

#### \[h2\]Functions

| Name | typedef Keyword | Description |
| :-- | :-- | :-- |
| [typedef void (\*OH\_AudioManager\_OnAudioSceneChangeCallback)(void \*userData, OH\_AudioScene scene)](#oh_audiomanager_onaudioscenechangecallback) | OH\_AudioManager\_OnAudioSceneChangeCallback | Defines the prototype of the audio scene change callback function, which is passed in [OH\_AudioManager\_RegisterAudioSceneChangeCallback](#oh_audiomanager_registeraudioscenechangecallback). |
| [OH\_AudioCommon\_Result OH\_GetAudioManager(OH\_AudioManager \*\*audioManager)](#oh_getaudiomanager) | \- | 
Obtains an OH\_AudioManager instance.

Before using the features related to the audio manager, you must obtain an OH\_AudioManager instance.

 |
| [OH\_AudioCommon\_Result OH\_GetAudioScene(OH\_AudioManager\* manager, OH\_AudioScene \*scene)](#oh_getaudioscene) | \- | Obtains the audio scene. |
| [OH\_AudioCommon\_Result OH\_AudioManager\_RegisterAudioSceneChangeCallback(OH\_AudioManager \*manager, OH\_AudioManager\_OnAudioSceneChangeCallback callback, void \*userData)](#oh_audiomanager_registeraudioscenechangecallback) | \- | Registers the audio scene change callback function. |
| [OH\_AudioCommon\_Result OH\_AudioManager\_UnregisterAudioSceneChangeCallback(OH\_AudioManager \*manager, OH\_AudioManager\_OnAudioSceneChangeCallback callback)](#oh_audiomanager_unregisteraudioscenechangecallback) | \- | Unregisters the audio scene change callback function. |

#### Function Description

#### \[h2\]OH\_AudioManager\_OnAudioSceneChangeCallback()

typedef void (\*OH\_AudioManager\_OnAudioSceneChangeCallback) (void \*userData, OH\_AudioScene scene)

**Description**

Defines the prototype of the audio scene change callback function, which is passed in [OH\_AudioManager\_RegisterAudioSceneChangeCallback](#oh_audiomanager_registeraudioscenechangecallback).

**Since**: 20

**Parameters**

| Name | Description |
| :-- | :-- |
| void \*userData | Pointer to user data. |
| [OH\_AudioScene](../native-audio-common-h/document.md#oh_audioscene) scene | Audio scene after change. |

#### \[h2\]OH\_GetAudioManager()

OH\_AudioCommon\_Result OH\_GetAudioManager(OH\_AudioManager \*\*audioManager)

**Description**

Obtains an OH\_AudioManager instance.

Before using the features related to the audio manager, you must obtain an OH\_AudioManager instance.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_AudioManager](../../structs/oh-audiomanager/document.md) \*\*audioManager | Double pointer to an [OH\_AudioManager](../../structs/oh-audiomanager/document.md), which is used to receive the audio manager instance created. |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_AudioCommon\_Result](../native-audio-common-h/document.md#oh_audiocommon_result) | 
**AUDIOCOMMON\_RESULT\_SUCCESS**: The function is executed successfully.

**AUDIOCOMMON\_RESULT\_ERROR\_INVALID\_PARAM**: The **audioManager** parameter is nullptr.

 |

#### \[h2\]OH\_GetAudioScene()

OH\_AudioCommon\_Result OH\_GetAudioScene(OH\_AudioManager\* manager, OH\_AudioScene \*scene)

**Description**

Obtains the audio scene.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_AudioManager](../../structs/oh-audiomanager/document.md)\* manager | Pointer to an [OH\_AudioManager](../../structs/oh-audiomanager/document.md) instance, which is created by calling [OH\_GetAudioManager](#oh_getaudiomanager). |
| [OH\_AudioScene](../native-audio-common-h/document.md#oh_audioscene) \*scene | Pointer to an [OH\_AudioScene](../native-audio-common-h/document.md#oh_audioscene), which is used to receive the audio scene. |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_AudioCommon\_Result](../native-audio-common-h/document.md#oh_audiocommon_result) | 
**AUDIOCOMMON\_RESULT\_SUCCESS**: The function is executed successfully.

**AUDIOCOMMON\_RESULT\_ERROR\_INVALID\_PARAM**:

1\. The **audioManager** parameter is nullptr.

2\. The **scene** parameter is nullptr.

 |

#### \[h2\]OH\_AudioManager\_RegisterAudioSceneChangeCallback()

OH\_AudioCommon\_Result OH\_AudioManager\_RegisterAudioSceneChangeCallback(OH\_AudioManager \*manager,OH\_AudioManager\_OnAudioSceneChangeCallback callback, void \*userData)

**Description**

Registers the audio scene change callback function.

**Since**: 20

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_AudioManager](../../structs/oh-audiomanager/document.md) \*manager | Pointer to an [OH\_AudioManager](../../structs/oh-audiomanager/document.md) instance. |
| [OH\_AudioManager\_OnAudioSceneChangeCallback](#oh_audiomanager_onaudioscenechangecallback) callback | [OH\_AudioManager\_OnAudioSceneChangeCallback](#oh_audiomanager_onaudioscenechangecallback) invoked when the audio scene changes. |
| void \*userData | Pointer to user data. |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_AudioCommon\_Result](../native-audio-common-h/document.md#oh_audiocommon_result) | 
**AUDIOCOMMON\_RESULT\_SUCCESS**: The function is executed successfully.

**AUDIOCOMMON\_RESULT\_ERROR\_INVALID\_PARAM**:

1\. The **manager** parameter is nullptr.

2\. The **callback** parameter is nullptr.

**AUDIOCOMMON\_RESULT\_ERROR\_SYSTEM**: System error.

 |

#### \[h2\]OH\_AudioManager\_UnregisterAudioSceneChangeCallback()

OH\_AudioCommon\_Result OH\_AudioManager\_UnregisterAudioSceneChangeCallback(OH\_AudioManager \*manager,OH\_AudioManager\_OnAudioSceneChangeCallback callback)

**Description**

Unregisters the audio scene change callback function.

**Since**: 20

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_AudioManager](../../structs/oh-audiomanager/document.md) \*manager | Pointer to an [OH\_AudioManager](../../structs/oh-audiomanager/document.md) instance. |
| [OH\_AudioManager\_OnAudioSceneChangeCallback](#oh_audiomanager_onaudioscenechangecallback) callback | Pointer to the callback function passed by [OH\_AudioManager\_OnAudioSceneChangeCallback](#oh_audiomanager_onaudioscenechangecallback). |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_AudioCommon\_Result](../native-audio-common-h/document.md#oh_audiocommon_result) | 
**AUDIOCOMMON\_RESULT\_SUCCESS**: The function is executed successfully.

**AUDIOCOMMON\_RESULT\_ERROR\_INVALID\_PARAM**:

1\. The **manager** parameter is nullptr.

2\. The **callback** parameter is nullptr.

**AUDIOCOMMON\_RESULT\_ERROR\_SYSTEM**: System error.

 |
