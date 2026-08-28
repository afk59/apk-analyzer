# oh\_preferences.h

#### Overview

Provides APIs and structs for accessing the **Preferences** object.

**File to include**: <database/preferences/oh\_preferences.h>

**Library**: libohpreferences.so

**System capability**: SystemCapability.DistributedDataManager.Preferences.Core

**Since**: 13

**Related module**: [Preferences](../../modules/preferences/document.md)

#### Summary

#### \[h2\]Structs

| Name | typedef Keyword | Description |
| :-- | :-- | :-- |
| [OH\_Preferences](../../structs/oh-preferences/document.md) | OH\_Preferences | Defines a struct for a **Preferences** object. |

#### \[h2\]Functions

| Name | typedef Keyword | Description |
| :-- | :-- | :-- |
| [typedef void (\*OH\_PreferencesDataObserver)(void \*context, const OH\_PreferencesPair \*pairs, uint32\_t count)](#oh_preferencesdataobserver) | OH\_PreferencesDataObserver | Defines a struct for the callback for data changes. |
| [OH\_Preferences \*OH\_Preferences\_Open(OH\_PreferencesOption \*option, int \*errCode)](#oh_preferences_open) | \- | 
Opens a **Preferences** instance and creates a pointer to it.

If this pointer is no longer required, use [OH\_Preferences\_Close](#oh_preferences_close) to close the instance.

 |
| [int OH\_Preferences\_Close(OH\_Preferences \*preference)](#oh_preferences_close) | \- | Closes a **Preferences** instance. |
| [int OH\_Preferences\_GetInt(OH\_Preferences \*preference, const char \*key, int \*value)](#oh_preferences_getint) | \- | Obtains an integer corresponding to the specified key in a **Preferences** instance. |
| [int OH\_Preferences\_GetBool(OH\_Preferences \*preference, const char \*key, bool \*value)](#oh_preferences_getbool) | \- | Obtains a Boolean value corresponding to the specified key in a **Preferences** instance. |
| [int OH\_Preferences\_GetString(OH\_Preferences \*preference, const char \*key, char \*\*value, uint32\_t \*valueLen)](#oh_preferences_getstring) | \- | Obtains a string corresponding to the specified key in a **Preferences** instance. |
| [void OH\_Preferences\_FreeString(char \*string)](#oh_preferences_freestring) | \- | Releases a string obtained from a **Preferences** instance. |
| [int OH\_Preferences\_SetInt(OH\_Preferences \*preference, const char \*key, int value)](#oh_preferences_setint) | \- | Sets an integer based on the specified key in a **Preferences** instance. |
| [int OH\_Preferences\_SetBool(OH\_Preferences \*preference, const char \*key, bool value)](#oh_preferences_setbool) | \- | Sets a Boolean value based on the specified key in a **Preferences** instance. |
| [int OH\_Preferences\_SetString(OH\_Preferences \*preference, const char \*key, const char \*value)](#oh_preferences_setstring) | \- | Sets a string based on the specified key in a **Preferences** instance. |
| [int OH\_Preferences\_Delete(OH\_Preferences \*preference, const char \*key)](#oh_preferences_delete) | \- | Deletes the KV data corresponding to the specified key from a **Preferences** instance. |
| [int OH\_Preferences\_RegisterDataObserver(OH\_Preferences \*preference, void \*context,OH\_PreferencesDataObserver observer, const char \*keys\[\], uint32\_t keyCount)](#oh_preferences_registerdataobserver) | \- | Subscribes to data changes of the specified keys. If the value of the specified key changes, a callback will be invoked after **OH\_Preferences\_Close()** is called. |
| [int OH\_Preferences\_UnregisterDataObserver(OH\_Preferences \*preference, void \*context,OH\_PreferencesDataObserver observer, const char \*keys\[\], uint32\_t keyCount)](#oh_preferences_unregisterdataobserver) | \- | Unsubscribes from data changes of the specified keys. |
| [int OH\_Preferences\_IsStorageTypeSupported(Preferences\_StorageType type, bool \*isSupported)](#oh_preferences_isstoragetypesupported) | \- | Checks whether the specified storage type is supported. |

#### Function Description

#### \[h2\]OH\_PreferencesDataObserver()

typedef void (\*OH\_PreferencesDataObserver)(void \*context, const OH\_PreferencesPair \*pairs, uint32\_t count)

**Description**

Defines a struct for the callback for data changes.

**Since**: 13

**Parameters**

| Name | Description |
| :-- | :-- |
| void \*context | Pointer to the application context. |
| const [OH\_PreferencesPair](../../structs/oh-preferencespair/document.md) \*pairs | Pointer to the changed KV data. |
| uint32\_t count | Number of KV pairs changed. |

#### \[h2\]OH\_Preferences\_Open()

OH\_Preferences \*OH\_Preferences\_Open(OH\_PreferencesOption \*option, int \*errCode)

**Description**

Opens a **Preferences** instance and creates a pointer to it.

If this pointer is no longer required, use [OH\_Preferences\_Close](#oh_preferences_close) to close the instance.

**Since**: 13

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_PreferencesOption](../../structs/oh-preferencesoption/document.md) \*option | Pointer to the [OH\_PreferencesOption](../../structs/oh-preferencesoption/document.md) instance. |
| int \*errCode | 
Pointer to the error code returned. For details, see [OH\_Preferences\_ErrCode](../oh-preferences-err-code-h/document.md#oh_preferences_errcode).

**PREFERENCES\_OK** indicates the operation is successful.

**PREFERENCES\_ERROR\_INVALID\_PARAM** indicates invalid parameters are specified.

**PREFERENCES\_ERROR\_NOT\_SUPPORTED** indicates the system capability is not supported.

**PREFERENCES\_ERROR\_DELETE\_FILE** indicates the file fails to be deleted.

**PREFERENCES\_ERROR\_STORAGE** indicates the storage is abnormal.

**PREFERENCES\_ERROR\_MALLOC** indicates a failure in memory allocation.

 |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_Preferences](../../structs/oh-preferences/document.md) | Returns a pointer to the [OH\_Preferences](../../structs/oh-preferences/document.md) instance opened if the operation is successful; returns a null pointer otherwise. |

#### \[h2\]OH\_Preferences\_Close()

int OH\_Preferences\_Close(OH\_Preferences \*preference)

**Description**

Closes a **Preferences** instance.

**Since**: 13

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Preferences](../../structs/oh-preferences/document.md) \*preference | Pointer to the [OH\_Preferences](../../structs/oh-preferences/document.md) instance to close. |

**Returns**

| Type | Description |
| :-- | :-- |
| int | 
Returns an error code. For details, see [OH\_Preferences\_ErrCode](../oh-preferences-err-code-h/document.md#oh_preferences_errcode).

**PREFERENCES\_OK** indicates the operation is successful.

**PREFERENCES\_ERROR\_INVALID\_PARAM** indicates invalid parameters are specified.

**PREFERENCES\_ERROR\_STORAGE** indicates the storage is abnormal.

**PREFERENCES\_ERROR\_MALLOC** indicates a failure in memory allocation.

 |

#### \[h2\]OH\_Preferences\_GetInt()

int OH\_Preferences\_GetInt(OH\_Preferences \*preference, const char \*key, int \*value)

**Description**

Obtains an integer corresponding to the specified key in a **Preferences** instance.

**Since**: 13

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Preferences](../../structs/oh-preferences/document.md) \*preference | Pointer to the [OH\_Preferences](../../structs/oh-preferences/document.md) instance. |
| const char \*key | Pointer to the key of the value to obtain. |
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

**PREFERENCES\_ERROR\_KEY\_NOT\_FOUND** indicates the specified key does not exist.

 |

#### \[h2\]OH\_Preferences\_GetBool()

int OH\_Preferences\_GetBool(OH\_Preferences \*preference, const char \*key, bool \*value)

**Description**

Obtains a Boolean value corresponding to the specified key in a **Preferences** instance.

**Since**: 13

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Preferences](../../structs/oh-preferences/document.md) \*preference | Pointer to the [OH\_Preferences](../../structs/oh-preferences/document.md) instance. |
| const char \*key | Pointer to the key of the value to obtain. |
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

**PREFERENCES\_ERROR\_KEY\_NOT\_FOUND** indicates the specified key does not exist.

 |

#### \[h2\]OH\_Preferences\_GetString()

int OH\_Preferences\_GetString(OH\_Preferences \*preference, const char \*key, char \*\*value, uint32\_t \*valueLen)

**Description**

Obtains a string corresponding to the specified key in a **Preferences** instance.

**Since**: 13

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Preferences](../../structs/oh-preferences/document.md) \*preference | Pointer to the [OH\_Preferences](../../structs/oh-preferences/document.md) instance. |
| const char \*key | Pointer to the key of the value to obtain. |
| char \*\*value | Double pointer to the string obtained. If the string is not required, you can use [OH\_Preferences\_FreeString](#oh_preferences_freestring) to free the string (release the memory occupied by the string). |
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

**PREFERENCES\_ERROR\_KEY\_NOT\_FOUND** indicates the specified key does not exist.

 |

#### \[h2\]OH\_Preferences\_FreeString()

void OH\_Preferences\_FreeString(char \*string)

**Description**

Releases a string obtained from a **Preferences** instance.

**Since**: 13

**Parameters**

| Name | Description |
| :-- | :-- |
| char \*string | Pointer to the string to release. |

#### \[h2\]OH\_Preferences\_SetInt()

int OH\_Preferences\_SetInt(OH\_Preferences \*preference, const char \*key, int value)

**Description**

Sets an integer based on the specified key in a **Preferences** instance.

**Since**: 13

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Preferences](../../structs/oh-preferences/document.md) \*preference | Pointer to the [OH\_Preferences](../../structs/oh-preferences/document.md) instance. |
| const char \*key | Pointer to the key of the value to set. |
| int value | Integer value to be set. |

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

#### \[h2\]OH\_Preferences\_SetBool()

int OH\_Preferences\_SetBool(OH\_Preferences \*preference, const char \*key, bool value)

**Description**

Sets a Boolean value based on the specified key in a **Preferences** instance.

**Since**: 13

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Preferences](../../structs/oh-preferences/document.md) \*preference | Pointer to the [OH\_Preferences](../../structs/oh-preferences/document.md) instance. |
| const char \*key | Pointer to the key of the value to set. |
| bool value | Boolean value to be set. |

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

#### \[h2\]OH\_Preferences\_SetString()

int OH\_Preferences\_SetString(OH\_Preferences \*preference, const char \*key, const char \*value)

**Description**

Sets a string based on the specified key in a **Preferences** instance.

**Since**: 13

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Preferences](../../structs/oh-preferences/document.md) \*preference | Pointer to the [OH\_Preferences](../../structs/oh-preferences/document.md) instance. |
| const char \*key | Pointer to the key of the value to set. |
| const char \*value | Pointer to the string to set. |

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

#### \[h2\]OH\_Preferences\_Delete()

int OH\_Preferences\_Delete(OH\_Preferences \*preference, const char \*key)

**Description**

Deletes the KV data corresponding to the specified key from a **Preferences** instance.

**Since**: 13

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Preferences](../../structs/oh-preferences/document.md) \*preference | Pointer to the [OH\_Preferences](../../structs/oh-preferences/document.md) instance. |
| const char \*key | Pointer to the key of the KV pair to delete. |

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

**See**

OH\_Preferences\_ErrCode

#### \[h2\]OH\_Preferences\_RegisterDataObserver()

int OH\_Preferences\_RegisterDataObserver(OH\_Preferences \*preference, void \*context,OH\_PreferencesDataObserver observer, const char \*keys\[\], uint32\_t keyCount)

**Description**

Subscribes to data changes of the specified keys. If the value of the specified key changes, a callback will be invoked after **OH\_Preferences\_Close()** is called.

**Since**: 13

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Preferences](../../structs/oh-preferences/document.md) \*preference | Pointer to the [OH\_Preferences](../../structs/oh-preferences/document.md) instance. |
| void \*context | Pointer to the application context. |
| [OH\_PreferencesDataObserver](#oh_preferencesdataobserver) observer | [OH\_PreferencesDataObserver](#oh_preferencesdataobserver) callback to be invoked when data changes. |
| const char \*keys\[\] | Pointer to the keys of the data to be observed. |
| uint32\_t keyCount | Number of keys. |

**Returns**

| Type | Description |
| :-- | :-- |
| int | 
Returns an error code.

**PREFERENCES\_OK** indicates the operation is successful.

**PREFERENCES\_ERROR\_INVALID\_PARAM** indicates invalid parameters are specified.

**PREFERENCES\_ERROR\_STORAGE** indicates the storage is abnormal.

**PREFERENCES\_ERROR\_MALLOC** indicates a failure in memory allocation.

**PREFERENCES\_ERROR\_GET\_DATAOBSMGRCLIENT** indicates a failure in obtaining the data change subscription service.

 |

#### \[h2\]OH\_Preferences\_UnregisterDataObserver()

int OH\_Preferences\_UnregisterDataObserver(OH\_Preferences \*preference, void \*context,OH\_PreferencesDataObserver observer, const char \*keys\[\], uint32\_t keyCount)

**Description**

Unsubscribes from data changes of the specified keys.

**Since**: 13

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Preferences](../../structs/oh-preferences/document.md) \*preference | Pointer to the [OH\_Preferences](../../structs/oh-preferences/document.md) instance. |
| void \*context | Pointer to the application context. |
| [OH\_PreferencesDataObserver](#oh_preferencesdataobserver) observer | [OH\_PreferencesDataObserver](#oh_preferencesdataobserver) callback to be invoked when data changes. |
| const char \*keys\[\] | Pointer to the keys whose changes are not observed. |
| uint32\_t keyCount | Number of keys. |

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

**See**

OH\_Preferences\_ErrCode

#### \[h2\]OH\_Preferences\_IsStorageTypeSupported()

int OH\_Preferences\_IsStorageTypeSupported(Preferences\_StorageType type, bool \*isSupported)

**Since**: 18

**Parameters**

| Name | Description |
| :-- | :-- |
| [Preferences\_StorageType](../oh-preferences-option-h/document.md#preferences_storagetype) type | Storage type to check. |
| bool \*isSupported | Pointer to the check result. The value **true** means the storage type is supported; the value **false** means the opposite. |

**Returns**

| Type | Description |
| :-- | :-- |
| int | 
Returns an operation status code.

**PREFERENCES\_OK** indicates the operation is successful.

**PREFERENCES\_ERROR\_INVALID\_PARAM** indicates invalid parameters are specified.

 |
