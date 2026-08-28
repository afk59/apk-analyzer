# oh\_preferences\_value.h

#### Overview

Provides APIs, enums, and structs for accessing the **PreferencesValue** object.

**File to include**: <database/preferences/oh\_preferences\_value.h>

**Library**: libohpreferences.so

**System capability**: SystemCapability.DistributedDataManager.Preferences.Core

**Since**: 13

**Related module**: [Preferences](../../modules/preferences/document.md)

#### Summary

#### \[h2\]Structs

| Name | typedef Keyword | Description |
| :-- | :-- | :-- |
| [OH\_PreferencesPair](../../structs/oh-preferencespair/document.md) | OH\_PreferencesPair | Defines a struct for the **Preferences** data in KV format. |
| [OH\_PreferencesValue](../../structs/oh-preferencesvalue/document.md) | OH\_PreferencesValue | Defines a struct for the **PreferencesValue** object. |

#### \[h2\]Enums

| Name | typedef Keyword | Description |
| :-- | :-- | :-- |
| [Preference\_ValueType](#preference_valuetype) | Preference\_ValueType | Enumerates the data types of **PreferencesValue**. |

#### \[h2\]Functions

| Name | Description |
| :-- | :-- |
| [const char \*OH\_PreferencesPair\_GetKey(const OH\_PreferencesPair \*pairs, uint32\_t index)](#oh_preferencespair_getkey) | Obtains the key based on the specified index from the KV data. |
| [const OH\_PreferencesValue \*OH\_PreferencesPair\_GetPreferencesValue(const OH\_PreferencesPair \*pairs, uint32\_t index)](#oh_preferencespair_getpreferencesvalue) | Obtains the value based on the specified index from the KV pairs. |
| [Preference\_ValueType OH\_PreferencesValue\_GetValueType(const OH\_PreferencesValue \*object)](#oh_preferencesvalue_getvaluetype) | Obtains the data type of an **OH\_PreferencesValue** instance. |
| [int OH\_PreferencesValue\_GetInt(const OH\_PreferencesValue \*object, int \*value)](#oh_preferencesvalue_getint) | Obtains an integer from an [OH\_PreferencesValue](../../structs/oh-preferencesvalue/document.md) instance. |
| [int OH\_PreferencesValue\_GetBool(const OH\_PreferencesValue \*object, bool \*value)](#oh_preferencesvalue_getbool) | Obtains a Boolean value from an [OH\_PreferencesValue](../../structs/oh-preferencesvalue/document.md) instance. |
| [int OH\_PreferencesValue\_GetString(const OH\_PreferencesValue \*object, char \*\*value, uint32\_t \*valueLen)](#oh_preferencesvalue_getstring) | Obtains a string from an [OH\_PreferencesValue](../../structs/oh-preferencesvalue/document.md) instance. |

#### Enum Description

#### \[h2\]Preference\_ValueType

enum Preference\_ValueType

**Description**

Enumerates the data types of **PreferencesValue**.

**Since**: 13

| Enum Item | Description |
| :-- | :-- |
| PREFERENCE\_TYPE\_NULL = 0 | Null. |
| PREFERENCE\_TYPE\_INT | Integer. |
| PREFERENCE\_TYPE\_BOOL | Boolean. |
| PREFERENCE\_TYPE\_STRING | String. |
| PREFERENCE\_TYPE\_BUTT | End type. |

#### Function Description

#### \[h2\]OH\_PreferencesPair\_GetKey()

const char \*OH\_PreferencesPair\_GetKey(const OH\_PreferencesPair \*pairs, uint32\_t index)

**Description**

Obtains the key based on the specified index from the KV data.

**Since**: 13

**Parameters**

| Name | Description |
| :-- | :-- |
| const [OH\_PreferencesPair](../../structs/oh-preferencespair/document.md) \*pairs | Pointer to the target [OH\_PreferencesPair](../../structs/oh-preferencespair/document.md). |
| uint32\_t index | Index of the target [OH\_PreferencesPair](../../structs/oh-preferencespair/document.md). |

**Returns**

| Type | Description |
| :-- | :-- |
| const char \* | Returns the pointer to the key obtained if the operation is successful; returns a null pointer if the operation fails or invalid parameters are specified. |

#### \[h2\]OH\_PreferencesPair\_GetPreferencesValue()

const OH\_PreferencesValue \*OH\_PreferencesPair\_GetPreferencesValue(const OH\_PreferencesPair \*pairs, uint32\_t index)

**Description**

Obtains the value based on the specified index from the KV pairs.

**Since**: 13

**Parameters**

| Name | Description |
| :-- | :-- |
| const [OH\_PreferencesPair](../../structs/oh-preferencespair/document.md) \*pairs | Pointer to the target [OH\_PreferencesPair](../../structs/oh-preferencespair/document.md). |
| uint32\_t index | Index of the target [OH\_PreferencesPair](../../structs/oh-preferencespair/document.md). |

**Returns**

| Type | Description |
| :-- | :-- |
| const [OH\_PreferencesValue](../../structs/oh-preferencesvalue/document.md) | Returns the pointer to the value obtained if the operation is successful; returns a null pointer if the operation fails or invalid parameters are specified. |

#### \[h2\]OH\_PreferencesValue\_GetValueType()

Preference\_ValueType OH\_PreferencesValue\_GetValueType(const OH\_PreferencesValue \*object)

**Description**

Obtains the data type of a **PreferencesValue** instance.

**Since**: 13

**Parameters**

| Name | Description |
| :-- | :-- |
| const [OH\_PreferencesValue](../../structs/oh-preferencesvalue/document.md) \*object | Pointer to the [OH\_PreferencesValue](../../structs/oh-preferencesvalue/document.md) instance. |

**Returns**

| Type | Description |
| :-- | :-- |
| [Preference\_ValueType](#preference_valuetype) | Returns the obtained data type. If **PREFERENCE\_TYPE\_NULL** is returned, invalid parameters are passed in. |

#### \[h2\]OH\_PreferencesValue\_GetInt()

int OH\_PreferencesValue\_GetInt(const OH\_PreferencesValue \*object, int \*value)

**Description**

Obtains an integer from an [OH\_PreferencesValue](../../structs/oh-preferencesvalue/document.md) instance.

**Since**: 13

**Parameters**

| Name | Description |
| :-- | :-- |
| const [OH\_PreferencesValue](../../structs/oh-preferencesvalue/document.md) \*object | Pointer to the [OH\_PreferencesValue](../../structs/oh-preferencesvalue/document.md) instance. |
| int \*value | Pointer to the integer value obtained. |

**Returns**

| Type | Description |
| :-- | :-- |
| int | 
Returns an error code.

**PREFERENCES\_OK** indicates the operation is successful.

**PREFERENCES\_ERROR\_INVALID\_PARAM** indicates invalid parameters are specified.

**PREFERENCES\_ERROR\_STORAGE** indicates the storage is abnormal.

**PREFERENCES\_ERROR\_MALLOC** indicates a failure in memory allocation.

 |

#### \[h2\]OH\_PreferencesValue\_GetBool()

int OH\_PreferencesValue\_GetBool(const OH\_PreferencesValue \*object, bool \*value)

**Description**

Obtains a Boolean value from an [OH\_PreferencesValue](../../structs/oh-preferencesvalue/document.md) instance.

**Since**: 13

**Parameters**

| Name | Description |
| :-- | :-- |
| const [OH\_PreferencesValue](../../structs/oh-preferencesvalue/document.md) \*object | Pointer to the [OH\_PreferencesValue](../../structs/oh-preferencesvalue/document.md) instance. |
| bool \*value | Pointer to the Boolean value obtained. |

**Returns**

| Type | Description |
| :-- | :-- |
| int | 
Returns an error code.

**PREFERENCES\_OK** indicates the operation is successful.

**PREFERENCES\_ERROR\_INVALID\_PARAM** indicates invalid parameters are specified.

**PREFERENCES\_ERROR\_STORAGE** indicates the storage is abnormal.

**PREFERENCES\_ERROR\_MALLOC** indicates a failure in memory allocation.

 |

#### \[h2\]OH\_PreferencesValue\_GetString()

int OH\_PreferencesValue\_GetString(const OH\_PreferencesValue \*object, char \*\*value, uint32\_t \*valueLen)

**Description**

Obtains a string from an [OH\_PreferencesValue](../../structs/oh-preferencesvalue/document.md) instance.

**Since**: 13

**Parameters**

| Name | Description |
| :-- | :-- |
| const [OH\_PreferencesValue](../../structs/oh-preferencesvalue/document.md) \*object | Pointer to the [OH\_PreferencesValue](../../structs/oh-preferencesvalue/document.md) instance. |
| char \*\*value | Double pointer to the string obtained. If the string is not required, you can use [OH\_Preferences\_FreeString](../oh-preferences-h/document.md#oh_preferences_freestring) to free the string (release the memory occupied by the string). |
| uint32\_t \*valueLen | Pointer to the length of the string obtained. |

**Returns**

| Type | Description |
| :-- | :-- |
| int | 
Returns an error code.

**PREFERENCES\_OK** indicates the operation is successful.

**PREFERENCES\_ERROR\_INVALID\_PARAM** indicates invalid parameters are specified.

**PREFERENCES\_ERROR\_STORAGE** indicates the storage is abnormal.

**PREFERENCES\_ERROR\_MALLOC** indicates a failure in memory allocation.

 |
