# native\_audio\_resource\_manager.h

#### Overview

The file declares the functions related to an audio resource manager.

**File to include**: <ohaudio/native\_audio\_resource\_manager.h>

**Library**: libohaudio.so

**System capability**: SystemCapability.Multimedia.Audio.Core

**Since**: 20

**Related module**: [OHAudio](../../modules/ohaudio/document.md)

#### Summary

#### \[h2\]Structs

| Name | typedef Keyword | Description |
| :-- | :-- | :-- |
| [OH\_AudioResourceManager](../../structs/oh-audioresourcemanager/document.md) | OH\_AudioResourceManager | Describes an audio resource manager, which is used to manage audio resources. |
| [OH\_AudioWorkgroup](../../structs/oh-audioworkgroup/document.md) | OH\_AudioWorkgroup | Describes an audio group, which is used to group and manage key audio threads. |

#### \[h2\]Functions

| Name | Description |
| :-- | :-- |
| [OH\_AudioCommon\_Result OH\_AudioManager\_GetAudioResourceManager(OH\_AudioResourceManager \*\*resourceManager)](#oh_audiomanager_getaudioresourcemanager) | 
Obtains an audio resource manager.

Before using the features related to the audio resource manager, you must obtain an audio resource manager instance.

 |
| [OH\_AudioCommon\_Result OH\_AudioResourceManager\_CreateWorkgroup(OH\_AudioResourceManager \*resourceManager, const char \*name, OH\_AudioWorkgroup \*\*group)](#oh_audioresourcemanager_createworkgroup) | Creates an audio workgroup. |
| [OH\_AudioCommon\_Result OH\_AudioResourceManager\_ReleaseWorkgroup(OH\_AudioResourceManager \*resourceManager, OH\_AudioWorkgroup \*group)](#oh_audioresourcemanager_releaseworkgroup) | Releases an audio workgroup. |
| [OH\_AudioCommon\_Result OH\_AudioWorkgroup\_AddCurrentThread(OH\_AudioWorkgroup \*group, int32\_t \*tokenId)](#oh_audioworkgroup_addcurrentthread) | Adds a thread to an audio workgroup. |
| [OH\_AudioCommon\_Result OH\_AudioWorkgroup\_RemoveThread(OH\_AudioWorkgroup \*group, int32\_t tokenId)](#oh_audioworkgroup_removethread) | Removes a thread from an audio workgroup. |
| [OH\_AudioCommon\_Result OH\_AudioWorkgroup\_Start(OH\_AudioWorkgroup \*group, uint64\_t startTime, uint64\_t deadlineTime)](#oh_audioworkgroup_start) | Notifies the system that an audio workgroup starts working and provides the expected end time of the workgroup. |
| [OH\_AudioCommon\_Result OH\_AudioWorkgroup\_Stop(OH\_AudioWorkgroup \*group)](#oh_audioworkgroup_stop) | Notifies the system that an audio workgroup finishes working. |

#### Function Description

#### \[h2\]OH\_AudioManager\_GetAudioResourceManager()

OH\_AudioCommon\_Result OH\_AudioManager\_GetAudioResourceManager(OH\_AudioResourceManager \*\*resourceManager)

**Description**

Obtains an audio resource manager.

Before using the features related to the audio resource manager, you must obtain an audio resource manager instance.

**Since**: 20

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_AudioResourceManager](../../structs/oh-audioresourcemanager/document.md) \*\*resourceManager | Double pointer to an OH\_AudioResourceManager instance, which is used to receive the created audio resource manager instance. |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_AudioCommon\_Result](../native-audio-common-h/document.md#oh_audiocommon_result) | 
**AUDIOCOMMON\_RESULT\_SUCCESS**: The function is executed successfully.

**AUDIOCOMMON\_RESULT\_ERROR\_INVALID\_PARAM**: The **resourceManager** parameter is nullptr.

 |

#### \[h2\]OH\_AudioResourceManager\_CreateWorkgroup()

OH\_AudioCommon\_Result OH\_AudioResourceManager\_CreateWorkgroup(OH\_AudioResourceManager \*resourceManager,const char \*name, OH\_AudioWorkgroup \*\*group)

**Description**

Creates an audio workgroup.

**Since**: 20

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_AudioResourceManager](../../structs/oh-audioresourcemanager/document.md) \*resourceManager | Pointer to an OH\_AudioResourceManager instance, which is created by calling [OH\_AudioManager\_GetAudioResourceManager](#oh_audiomanager_getaudioresourcemanager). |
| const char \*name | Pointer to the name of the audio workgroup. |
| [OH\_AudioWorkgroup](../../structs/oh-audioworkgroup/document.md) \*\*group | Double pointer to an OH\_AudioWorkgroup instance, which is used to receive the created audio workgroup instance. |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_AudioCommon\_Result](../native-audio-common-h/document.md#oh_audiocommon_result) | 
**AUDIOCOMMON\_RESULT\_SUCCESS**: The function is executed successfully.

**AUDIOCOMMON\_RESULT\_ERROR\_INVALID\_PARAM**:

1\. The **resourceManager** parameter is **nullptr**.

2\. The **name** parameter is **nullptr**.

3\. The **group** parameter is nullptr.

**AUDIOCOMMON\_RESULT\_ERROR\_NO\_MEMORY**: The memory is insufficient.

**AUDIOCOMMON\_RESULT\_ERROR\_SYSTEM**: A system processing error occurs.

 |

#### \[h2\]OH\_AudioResourceManager\_ReleaseWorkgroup()

OH\_AudioCommon\_Result OH\_AudioResourceManager\_ReleaseWorkgroup(OH\_AudioResourceManager \*resourceManager,OH\_AudioWorkgroup \*group)

**Description**

Releases an audio workgroup.

**Since**: 20

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_AudioResourceManager](../../structs/oh-audioresourcemanager/document.md) \*resourceManager | Pointer to an OH\_AudioResourceManager instance, which is created by calling [OH\_AudioManager\_GetAudioResourceManager](#oh_audiomanager_getaudioresourcemanager). |
| [OH\_AudioWorkgroup](../../structs/oh-audioworkgroup/document.md) \*group | Pointer to an OH\_AudioWorkgroup instance, which is created by calling [OH\_AudioResourceManager\_CreateWorkgroup](#oh_audioresourcemanager_createworkgroup). |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_AudioCommon\_Result](../native-audio-common-h/document.md#oh_audiocommon_result) | 
**AUDIOCOMMON\_RESULT\_SUCCESS**: The function is executed successfully.

**AUDIOCOMMON\_RESULT\_ERROR\_INVALID\_PARAM**:

1\. The **resourceManager** parameter is **nullptr**.

2\. The **group** parameter is nullptr.

**AUDIOCOMMON\_RESULT\_ERROR\_SYSTEM**: A system processing error occurs.

 |

#### \[h2\]OH\_AudioWorkgroup\_AddCurrentThread()

OH\_AudioCommon\_Result OH\_AudioWorkgroup\_AddCurrentThread(OH\_AudioWorkgroup \*group, int32\_t \*tokenId)

**Description**

Adds a thread to an audio workgroup.

**Since**: 20

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_AudioWorkgroup](../../structs/oh-audioworkgroup/document.md) \*group | Pointer to an OH\_AudioWorkgroup instance, which is created by calling [OH\_AudioResourceManager\_CreateWorkgroup](#oh_audioresourcemanager_createworkgroup). |
| int32\_t \*tokenId | Pointer to the ID of the thread to be added to the audio workgroup. |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_AudioCommon\_Result](../native-audio-common-h/document.md#oh_audiocommon_result) | 
**AUDIOCOMMON\_RESULT\_SUCCESS**: The function is executed successfully.

**AUDIOCOMMON\_RESULT\_ERROR\_INVALID\_PARAM**:

1\. The **group** parameter is **nullptr**.

2\. The **tokenId** parameter is **nullptr**.

**AUDIOCOMMON\_RESULT\_ERROR\_NO\_MEMORY**: The memory is insufficient.

**AUDIOCOMMON\_RESULT\_ERROR\_SYSTEM**: A system processing error occurs.

 |

#### \[h2\]OH\_AudioWorkgroup\_RemoveThread()

OH\_AudioCommon\_Result OH\_AudioWorkgroup\_RemoveThread(OH\_AudioWorkgroup \*group, int32\_t tokenId)

**Description**

Removes a thread from an audio workgroup.

**Since**: 20

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_AudioWorkgroup](../../structs/oh-audioworkgroup/document.md) \*group | Pointer to an OH\_AudioWorkgroup instance, which is created by calling [OH\_AudioResourceManager\_CreateWorkgroup](#oh_audioresourcemanager_createworkgroup). |
| int32\_t tokenId | ID of the thread to be removed from the audio workgroup. |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_AudioCommon\_Result](../native-audio-common-h/document.md#oh_audiocommon_result) | 
**AUDIOCOMMON\_RESULT\_SUCCESS**: The function is executed successfully.

**AUDIOCOMMON\_RESULT\_ERROR\_INVALID\_PARAM**:

1\. The **group** parameter is **nullptr**.

2\. The **tokenId** parameter is set to an invalid value.

**AUDIOCOMMON\_RESULT\_ERROR\_SYSTEM**: A system processing error occurs.

 |

#### \[h2\]OH\_AudioWorkgroup\_Start()

OH\_AudioCommon\_Result OH\_AudioWorkgroup\_Start(OH\_AudioWorkgroup \*group, uint64\_t startTime, uint64\_t deadlineTime)

**Description**

Notifies the system that an audio workgroup starts working and provides the expected end time of the workgroup.

**Since**: 20

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_AudioWorkgroup](../../structs/oh-audioworkgroup/document.md) \*group | Pointer to an OH\_AudioWorkgroup instance, which is created by calling [OH\_AudioResourceManager\_CreateWorkgroup](#oh_audioresourcemanager_createworkgroup). |
| uint64\_t startTime | Time when the audio workgroup starts working. |
| uint64\_t deadlineTime | Expected end time of the audio workgroup. |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_AudioCommon\_Result](../native-audio-common-h/document.md#oh_audiocommon_result) | 
**AUDIOCOMMON\_RESULT\_SUCCESS**: The function is executed successfully.

**AUDIOCOMMON\_RESULT\_ERROR\_INVALID\_PARAM**:

1\. The **group** parameter is **nullptr**.

2\. The **startTime** parameter is set to an invalid value.

3\. The **deadlineTime** parameter is invalid.

**AUDIOCOMMON\_RESULT\_ERROR\_SYSTEM**: A system processing error occurs.

 |

#### \[h2\]OH\_AudioWorkgroup\_Stop()

OH\_AudioCommon\_Result OH\_AudioWorkgroup\_Stop(OH\_AudioWorkgroup \*group)

**Description**

Notifies the system that an audio workgroup finishes working.

**Since**: 20

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_AudioWorkgroup](../../structs/oh-audioworkgroup/document.md) \*group | Pointer to an OH\_AudioWorkgroup instance, which is created by calling [OH\_AudioResourceManager\_CreateWorkgroup](#oh_audioresourcemanager_createworkgroup). |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_AudioCommon\_Result](../native-audio-common-h/document.md#oh_audiocommon_result) | 
**AUDIOCOMMON\_RESULT\_SUCCESS**: The function is executed successfully.

**AUDIOCOMMON\_RESULT\_ERROR\_INVALID\_PARAM**: The **group** parameter is nullptr.

**AUDIOCOMMON\_RESULT\_ERROR\_SYSTEM**: A system processing error occurs.

 |
