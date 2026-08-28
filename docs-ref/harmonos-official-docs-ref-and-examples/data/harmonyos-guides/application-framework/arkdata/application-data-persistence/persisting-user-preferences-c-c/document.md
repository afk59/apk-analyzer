# Persisting User Preferences (C/C++)

#### When to Use

Use the **Preferences** module to store small amounts of data in key-value (KV) format. The data is stored in files and memory for fast access. If a large amount of data needs to be stored, consider using a KV store or RDB store.

#### Constraints

-   Versions earlier than API version 18: ArkTS APIs support only the [XML](../persisting-user-preferences-arkts/document.md#xml) storage format, and C APIs support only the [GSKV](../persisting-user-preferences-arkts/document.md#gskv) storage format. Storage formats are incompatible, so ArkTS and C APIs cannot operate the same **Preferences** instance.
-   API version 18 and later: Both ArkTS and C APIs support the XML and GSKV storage formats. ArkTS and C APIs can operate the same **Preferences** instance if they use the same format.
-   The maximum key length is 1024 bytes, and the maximum value length is 16 MB.

#### Available APIs

For details about the APIs, see [Preferences](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-preferences).

| API | Description |
| :-- | :-- |
| OH\_Preferences \* OH\_Preferences\_Open (OH\_PreferencesOption \*option, int \*errCode) | Opens a **Preferences** instance and creates a pointer to it. If the pointer is no longer required, use **OH\_Preferences\_Close** to close the instance. |
| int OH\_Preferences\_Close (OH\_Preferences \*preference) | Closes a **Preferences** instance. |
| int OH\_Preferences\_GetInt (OH\_Preferences \*preference, const char \*key, int \*value) | Obtains an integer corresponding to the specified key in a **Preferences** instance. |
| int OH\_Preferences\_GetBool (OH\_Preferences \*preference, const char \*key, bool \*value) | Obtains a Boolean value corresponding to the specified key in a **Preferences** instance. |
| int OH\_Preferences\_GetString (OH\_Preferences \*preference, const char \*key, char \*\*value, uint32\_t \*valueLen) | Obtains a string corresponding to the specified key in a **Preferences** instance. |
| void OH\_Preferences\_FreeString (char \*string) | Releases the string obtained. |
| int OH\_Preferences\_SetInt (OH\_Preferences \*preference, const char \*key, int value) | Sets an integer based on the specified key in a **Preferences** instance. |
| int OH\_Preferences\_SetBool (OH\_Preferences \*preference, const char \*key, bool value) | Sets a Boolean value based on the specified key in a **Preferences** instance. |
| int OH\_Preferences\_SetString (OH\_Preferences \*preference, const char \*key, const char \*value) | Sets a string based on the specified key in a **Preferences** instance. |
| int OH\_Preferences\_Delete (OH\_Preferences \*preference, const char \*key) | Deletes the KV data corresponding to the specified key from a **Preferences** instance. |
| int OH\_Preferences\_RegisterDataObserver (OH\_Preferences \*preference, void \*context, OH\_PreferencesDataObserver observer, const char \*keys\[\], uint32\_t keyCount) | Subscribes to data changes of the specified keys. If the value of the specified key changes, a callback will be invoked after **OH\_Preferences\_Close()** is called. |
| int OH\_Preferences\_UnregisterDataObserver (OH\_Preferences \*preference, void \*context, OH\_PreferencesDataObserver observer, const char \*keys\[\], uint32\_t keyCount) | Unsubscribes from data changes of the specified keys. |
| int OH\_Preferences\_IsStorageTypeSupported (Preferences\_StorageType type, bool \*isSupported) | Checks whether the specified storage type is supported. |
| OH\_PreferencesOption \* OH\_PreferencesOption\_Create (void) | Creates an **OH\_PreferencesOption** instance and a pointer to it. If this pointer is no longer required, use **OH\_PreferencesOption\_Destroy** to destroy it. Otherwise, memory leaks may occur. |
| int OH\_PreferencesOption\_SetFileName (OH\_PreferencesOption \*option, const char \*fileName) | Sets the file name for an **OH\_PreferencesOption** instance. The file name cannot contain a slash (/) or exceed 255 bytes. |
| int OH\_PreferencesOption\_SetBundleName (OH\_PreferencesOption \*option, const char \*bundleName) | Sets the bundle name for an OH\_PreferencesOption instance. |
| int OH\_PreferencesOption\_SetDataGroupId (OH\_PreferencesOption \*option, const char \*dataGroupId) | Sets the application group ID for an **OH\_PreferencesOption** instance. |
| int OH\_PreferencesOption\_SetStorageType (OH\_PreferencesOption \*option, Preferences\_StorageType type) | Sets the storage type for an **OH\_PreferencesOption** instance. |
| int OH\_PreferencesOption\_Destroy (OH\_PreferencesOption \*option) | Destroys an **OH\_PreferencesOption** instance. |
| const char \* OH\_PreferencesPair\_GetKey (const OH\_PreferencesPair \*pairs, uint32\_t index) | Obtains the key based on the specified index from the KV data. |
| const OH\_PreferencesValue \* OH\_PreferencesPair\_GetPreferencesValue (const OH\_PreferencesPair \*pairs, uint32\_t index) | Obtains the value based on the specified index from the KV pairs. |
| Preference\_ValueType OH\_PreferencesValue\_GetValueType (const OH\_PreferencesValue \*object) | Obtains the data type of a **PreferencesValue** instance. |
| int OH\_PreferencesValue\_GetInt (const OH\_PreferencesValue \*object, int \*value) | Obtains an integer value from an **OH\_PreferencesValue** instance. |
| int OH\_PreferencesValue\_GetBool (const OH\_PreferencesValue \*object, bool \*value) | Obtains a Boolean value from an **OH\_PreferencesValue** instance. |
| int OH\_PreferencesValue\_GetString (const OH\_PreferencesValue \*object, char \*\*value, uint32\_t \*valueLen) | Obtains a string from an **OH\_PreferencesValue** instance. |

#### Adding Dynamic Link Libraries

Add the following library to **CMakeLists.txt**.

libohpreferences.so

#### Including Header Files

#include <database/preferences/oh\_preferences.h>
#include <database/preferences/oh\_preferences\_err\_code.h>
#include <database/preferences/oh\_preferences\_option.h>
#include <database/preferences/oh\_preferences\_value.h>

#### How to Develop

The following example shows how to use **Preferences** APIs to modify and persist KV data.

1.  Create a **PreferencesOption** instance and set the name, application group ID, bundle name, and storage type. If the **PreferencesOption** object is no longer required, call **OH\_PreferencesOption\_Destroy** to destroy it.
2.  Call **OH\_Preferences\_Open** to open a **Preferences** instance. When the **Preferences** instance is not required, call **OH\_Preferences\_Close** to close it.
    
    // 1. Create a PreferencesOption instance.
    OH\_PreferencesOption \*option = OH\_PreferencesOption\_Create();
    if (option == nullptr) {
        // Error handling.
    }
    // Set the file name.
    int ret = OH\_PreferencesOption\_SetFileName(option, "testdb");
    if (ret != PREFERENCES\_OK) {
        (void)OH\_PreferencesOption\_Destroy(option);
        // Error handling.
    }
    // Set the application group ID.
    ret = OH\_PreferencesOption\_SetDataGroupId(option, "");
    if (ret != PREFERENCES\_OK) {
        (void)OH\_PreferencesOption\_Destroy(option);
        // Error handling.
    }
    // Set the bundle name.
    ret = OH\_PreferencesOption\_SetBundleName(option, "com.example");
    if (ret != PREFERENCES\_OK) {
        (void)OH\_PreferencesOption\_Destroy(option);
        // Error handling.
    }
    // Set the storage type for the PreferencesOption instance. Before the setting, call OH\_Preferences\_IsStorageTypeSupported to check whether the storage type is supported.
    bool isGskvSupported = false;
    ret = OH\_Preferences\_IsStorageTypeSupported(Preferences\_StorageType::PREFERENCES\_STORAGE\_GSKV, &isGskvSupported);
    if (ret != PREFERENCES\_OK) {
        (void)OH\_PreferencesOption\_Destroy(option);
        // Error handling.
    }
    if (isGskvSupported) {
        ret = OH\_PreferencesOption\_SetStorageType(option, Preferences\_StorageType::PREFERENCES\_STORAGE\_GSKV);
        if (ret != PREFERENCES\_OK) {
            (void)OH\_PreferencesOption\_Destroy(option);
            // Error handling.
        }
    } else {
        ret = OH\_PreferencesOption\_SetStorageType(option, Preferences\_StorageType::PREFERENCES\_STORAGE\_XML);
        if (ret != PREFERENCES\_OK) {
            (void)OH\_PreferencesOption\_Destroy(option);
            // Error handling.
        }
    }
    // 2. Open a Preferences instance.
    int errCode = PREFERENCES\_OK;
    OH\_Preferences \*preference = OH\_Preferences\_Open(option, &errCode);
    // Destroy the PreferencesOption instance that is no longer used, and set the instance pointer to null.
    (void)OH\_PreferencesOption\_Destroy(option);
    option = nullptr;
    if (preference == nullptr || errCode != PREFERENCES\_OK) {
        // Error handling.
    }
    
3.  Call **OH\_Preferences\_RegisterDataObserver** to register a **DataChangeObserverCallback** callback to observe data changes of three keys.
    
    // Callback used to return data changes.
    void DataChangeObserverCallback(void \*context, const OH\_PreferencesPair \*pairs, uint32\_t count)
    {
        for (uint32\_t i = 0; i < count; i++) {
            // Obtain the PreferencesValue corresponding to index i.
            const OH\_PreferencesValue \*pValue = OH\_PreferencesPair\_GetPreferencesValue(pairs, i);
            // Obtain the data type of a value.
            Preference\_ValueType type = OH\_PreferencesValue\_GetValueType(pValue);
            int ret = PREFERENCES\_OK;
            if (type == PREFERENCE\_TYPE\_INT) {
                int intValue = 0;
                ret = OH\_PreferencesValue\_GetInt(pValue, &intValue);
                if (ret == PREFERENCES\_OK) {
                    // Service logic.
                }
            } else if (type == PREFERENCE\_TYPE\_BOOL) {
                bool boolValue = true;
                ret = OH\_PreferencesValue\_GetBool(pValue, &boolValue);
                if (ret == PREFERENCES\_OK) {
                    // Service logic.
                }
            } else if (type == PREFERENCE\_TYPE\_STRING) {
                char \*stringValue = nullptr;
                uint32\_t valueLen = 0;
                ret = OH\_PreferencesValue\_GetString(pValue, &stringValue, &valueLen);
                if (ret == PREFERENCES\_OK) {
                    // Service logic.
                    OH\_Preferences\_FreeString(stringValue);
                }
            } else {
                // Invalid type.
            }
        }
    }
    
4.  Set KV data in the **Preferences** instance.
5.  Obtain data in the **Preferences** instance.
    
    // 3. Subscribe to data changes of key\_int, key\_bool, and key\_string.
    const char \*keys\[\] = {"key\_int", "key\_bool", "key\_string"};
    int ret = OH\_Preferences\_RegisterDataObserver(preference, nullptr, DataChangeObserverCallback, keys, 3);
    if (ret != PREFERENCES\_OK) {
        (void)OH\_Preferences\_Close(preference);
        // Error handling.
    }
    
    // 4. Set KV data in the Preferences instance.
    ret = OH\_Preferences\_SetInt(preference, keys\[0\], 0);
    if (ret != PREFERENCES\_OK) {
        (void)OH\_Preferences\_Close(preference);
        // Error handling.
    }
    ret = OH\_Preferences\_SetBool(preference, keys\[1\], true);
    if (ret != PREFERENCES\_OK) {
        (void)OH\_Preferences\_Close(preference);
        // Error handling.
    }
    int32\_t stringIndex = 2;
    ret = OH\_Preferences\_SetString(preference, keys\[stringIndex\], "string value");
    if (ret != PREFERENCES\_OK) {
        (void)OH\_Preferences\_Close(preference);
        // Error handling.
    }
    
    // 5. Obtain KV data from the Preferences instance.
    int intValue = 0;
    ret = OH\_Preferences\_GetInt(preference, keys\[0\], &intValue);
    if (ret == PREFERENCES\_OK) {
        // Service logic.
    }
    
    bool boolValue = false;
    ret = OH\_Preferences\_GetBool(preference, keys\[1\], &boolValue);
    if (ret == PREFERENCES\_OK) {
        // Service logic.
    }
    
    char \*stringValue = nullptr;
    uint32\_t valueLen = 0;
    ret = OH\_Preferences\_GetString(preference, keys\[stringIndex\], &stringValue, &valueLen);
    if (ret == PREFERENCES\_OK) {
        // Service logic.
        // Release the string obtained by OH\_Preferences\_GetString.
        OH\_Preferences\_FreeString(stringValue);
        stringValue = nullptr;
    }
    
6.  Call **OH\_Preferences\_Close** to close the **Preferences** instance and set the instance pointer to null.
    
    // 6. Close the Preferences instance and set the pointer to null.
    (void)OH\_Preferences\_Close(preference);
    preference = nullptr;
