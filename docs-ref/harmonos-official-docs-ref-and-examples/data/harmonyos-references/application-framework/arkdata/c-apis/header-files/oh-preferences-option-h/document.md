# oh\_preferences\_option.h

#### Overview

Provides APIs and structs for accessing the **PreferencesOption** object.

**File to include**: <database/preferences/oh\_preferences\_option.h>

**Library**: libohpreferences.so

**System capability**: SystemCapability.DistributedDataManager.Preferences.Core

**Since**: 13

**Related module**: [Preferences](../../modules/preferences/document.md)

#### Summary

#### \[h2\]Structs

| Name | typedef Keyword | Description |
| :-- | :-- | :-- |
| [OH\_PreferencesOption](../../structs/oh-preferencesoption/document.md) | OH\_PreferencesOption | Defines a struct for **Preferences** configuration. |

#### \[h2\]Enums

| Name | typedef Keyword | Description |
| :-- | :-- | :-- |
| [Preferences\_StorageType](#preferences_storagetype) | Preferences\_StorageType | Enumerates the preferences storage types. |

#### \[h2\]Functions

| Name | Description |
| :-- | :-- |
| [OH\_PreferencesOption \*OH\_PreferencesOption\_Create(void)](#oh_preferencesoption_create) | 
Creates a [OH\_PreferencesOption](../../structs/oh-preferencesoption/document.md) instance and a pointer to it.

If this pointer is no longer required, use [OH\_PreferencesOption\_Destroy](#oh_preferencesoption_destroy) to destroy it. Otherwise, memory leaks may occur.

 |
| [int OH\_PreferencesOption\_SetFileName(OH\_PreferencesOption \*option, const char \*fileName)](#oh_preferencesoption_setfilename) | Sets the file name for an [OH\_PreferencesOption](../../structs/oh-preferencesoption/document.md) instance. |
| [int OH\_PreferencesOption\_SetBundleName(OH\_PreferencesOption \*option, const char \*bundleName)](#oh_preferencesoption_setbundlename) | Sets the bundle name for an [OH\_PreferencesOption](../../structs/oh-preferencesoption/document.md) instance. |
| [int OH\_PreferencesOption\_SetDataGroupId(OH\_PreferencesOption \*option, const char \*dataGroupId)](#oh_preferencesoption_setdatagroupid) | 

Sets the application group ID for an [OH\_PreferencesOption](../../structs/oh-preferencesoption/document.md) instance.

After the application group ID is set, the **Preferences** instance will be created in the sandbox directory of the application group ID. The application group ID must be obtained from AppGallery. This parameter is not supported currently.

If the application group ID is an empty string, the **Preferences** instance will be created in the sandbox directory of the current application.

 |
| [int OH\_PreferencesOption\_SetStorageType(OH\_PreferencesOption \*option, Preferences\_StorageType type)](#oh_preferencesoption_setstoragetype) | Sets the storage type for a **Preferences** instance. |
| [int OH\_PreferencesOption\_Destroy(OH\_PreferencesOption \*option)](#oh_preferencesoption_destroy) | Destroys an [OH\_PreferencesOption](../../structs/oh-preferencesoption/document.md) instance. |

#### Enum Description

#### \[h2\]Preferences\_StorageType

enum Preferences\_StorageType

**Description**

Enumerates the preferences storage types.

**Since**: 18

| Enum | Description |
| :-- | :-- |
| PREFERENCES\_STORAGE\_XML = 0 | XML. In this type is used, data operations are performed in the memory and data is persisted after [OH\_Preferences\_Close](../oh-preferences-h/document.md#oh_preferences_close) is called. This type does not multi-processes operations. |
| PREFERENCES\_STORAGE\_GSKV | CLKV. If this type is used, data operations are flushed on a real-time basis. This type supports multi-process operations. |

#### Function Description

#### \[h2\]OH\_PreferencesOption\_Create()

OH\_PreferencesOption \*OH\_PreferencesOption\_Create(void)

**Description**

Creates a [OH\_PreferencesOption](../../structs/oh-preferencesoption/document.md) instance and a pointer to it.

If this pointer is no longer required, use [OH\_PreferencesOption\_Destroy](#oh_preferencesoption_destroy) to destroy it. Otherwise, memory leaks may occur.

**Since**: 13

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_PreferencesOption](../../structs/oh-preferencesoption/document.md) | Returns a pointer to the [OH\_PreferencesOption](../../structs/oh-preferencesoption/document.md) instance created if the operation is successful; returns a null pointer otherwise. |

#### \[h2\]OH\_PreferencesOption\_SetFileName()

int OH\_PreferencesOption\_SetFileName(OH\_PreferencesOption \*option, const char \*fileName)

**Description**

Sets the file name for an [OH\_PreferencesOption](../../structs/oh-preferencesoption/document.md) instance.

**Since**: 13

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_PreferencesOption](../../structs/oh-preferencesoption/document.md) \*option | Pointer to the [OH\_PreferencesOption](../../structs/oh-preferencesoption/document.md) instance. |
| const char \*fileName | Pointer to the file name to set. |

**Returns**

| Type | Description |
| :-- | :-- |
| int | 
Error code.

**PREFERENCES\_OK** indicates the operation is successful.

**PREFERENCES\_ERROR\_INVALID\_PARAM** indicates invalid parameters are specified.

 |

**See**

OH\_Preferences\_ErrCode

#### \[h2\]OH\_PreferencesOption\_SetBundleName()

int OH\_PreferencesOption\_SetBundleName(OH\_PreferencesOption \*option, const char \*bundleName)

**Description**

Sets the bundle name for an [OH\_PreferencesOption](../../structs/oh-preferencesoption/document.md) instance.

**Since**: 13

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_PreferencesOption](../../structs/oh-preferencesoption/document.md) \*option | Pointer to the [OH\_PreferencesOption](../../structs/oh-preferencesoption/document.md) instance. |
| const char \*bundleName | Pointer to the bundle name to set. |

**Returns**

| Type | Description |
| :-- | :-- |
| int | 
Error code.

**PREFERENCES\_OK** indicates the operation is successful.

**PREFERENCES\_ERROR\_INVALID\_PARAM** indicates invalid parameters are specified.

 |

#### \[h2\]OH\_PreferencesOption\_SetDataGroupId()

int OH\_PreferencesOption\_SetDataGroupId(OH\_PreferencesOption \*option, const char \*dataGroupId)

**Description**

Sets the application group ID for an [OH\_PreferencesOption](../../structs/oh-preferencesoption/document.md) instance.

After the application group ID is set, the **Preferences** instance will be created in the sandbox directory of the application group ID. The application group ID must be obtained from AppGallery. This parameter is not supported currently.

If the application group ID is an empty string, the **Preferences** instance will be created in the sandbox directory of the current application.

**Since**: 13

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_PreferencesOption](../../structs/oh-preferencesoption/document.md) \*option | Pointer to the [OH\_PreferencesOption](../../structs/oh-preferencesoption/document.md) instance. |
| const char \*dataGroupId | Pointer to the application group ID to set. |

**Returns**

| Type | Description |
| :-- | :-- |
| int | 
Error code.

**PREFERENCES\_OK** indicates the operation is successful.

**PREFERENCES\_ERROR\_INVALID\_PARAM** indicates invalid parameters are specified.

 |

#### \[h2\]OH\_PreferencesOption\_SetStorageType()

int OH\_PreferencesOption\_SetStorageType(OH\_PreferencesOption \*option, Preferences\_StorageType type)

**Description**

Sets the storage type for a **Preferences** instance.

**Since**: 18

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_PreferencesOption](../../structs/oh-preferencesoption/document.md) \*option | Pointer to the configuration whose storage type is to set. |
| [Preferences\_StorageType](#preferences_storagetype) type | Storage type to set. |

**Returns**

| Type | Description |
| :-- | :-- |
| int | 
Error code.

**PREFERENCES\_OK** indicates the operation is successful.

**PREFERENCES\_ERROR\_INVALID\_PARAM** indicates invalid parameters are specified.

 |

#### \[h2\]OH\_PreferencesOption\_Destroy()

int OH\_PreferencesOption\_Destroy(OH\_PreferencesOption \*option)

**Description**

Destroys an [OH\_PreferencesOption](../../structs/oh-preferencesoption/document.md) instance.

**Since**: 13

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_PreferencesOption](../../structs/oh-preferencesoption/document.md) \*option | Pointer to the [OH\_PreferencesOption](../../structs/oh-preferencesoption/document.md) instance. |

**Returns**

| Type | Description |
| :-- | :-- |
| int | 
Operation status code.

**PREFERENCES\_OK** indicates the operation is successful.

**PREFERENCES\_ERROR\_INVALID\_PARAM** indicates invalid parameters are specified.

 |
