# Persisting User Preferences (ArkTS)

#### When to Use

The **Preferences** module provides APIs for processing data in the form of key-value (KV) pairs, including querying, modifying, and persisting KV pairs. You can use **Preferences** to store lightweight KV data, such as personalized settings, including font size, dark mode, and so on.

#### Working Principles

User applications call **Preference** through the ArkTS interface to read and write data files. You can load the persistence file data to a **Preferences** instance. Each file uniquely corresponds to an instance. The system stores each instance in the memory through a static container until the instance is removed from the memory or the file is deleted.

The preference persistent file of an application is stored in the application sandbox. You can use **context** to obtain the file path. For details about how to obtain the sandbox path, see [Obtaining Application File Paths](../../../ability-kit/stage-model-development/stage-model-application-components/context-stage-model/document.md#obtaining-application-file-paths).

**Figure 1** Preferences working mechanism

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a7/v3/PZYnrrZ4R7q414doz_dDnA/en-us_image_0000002568684087.jpg?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061920Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=D38F8BB6F0BB09E589E62A08A17F8D69E4263B7B981F6C7F42B0324A2D7CFFDA)

#### Storage Types

By default, user preferences are stored in XML format. Since API version 18, the GSKV format is provided.

## XML

Data is stored in the form of XML files, which allow high versatility and cross-platform operations. When XML is used, preference data operations are primarily performed in the memory. You can call [flush](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-data-preferences#flush) to persist the data when necessary. This storage type is recommended for single-process, small data volume scenarios.

## GSKV

GSKV is available since API version 18, where data is stored in binary format within files. It supports concurrent read and write in multiple processes. When GSKV is used, preference data operations are flushed to the storage device in real time. This storage type is recommended for multi-process concurrency scenarios.

#### Constraints

## Preferences Constraints

-   The key in a KV pair must be a string and cannot be empty or exceed 1024 bytes.
    
-   If the value is of the string type, use the UTF-8 encoding format. It can be empty. If not empty, it cannot exceed 16 MB.
    
-   After [removePreferencesFromCache](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-data-preferences#preferencesremovepreferencesfromcache) or [deletePreferences](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-data-preferences#preferencesdeletepreferences) is called, the subscription to data changes will be automatically canceled. If [getPreferences](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-data-preferences#preferencesgetpreferences) is called again, you need to subscribe to data changes again.
    
-   Do not call **deletePreferences** concurrently with other APIs in multi-thread or multi-process mode. Otherwise, unexpected behavior may occur.
    
-   Data cannot be encrypted for storage. If data encryption is required, encrypt the data first, and then store the ciphertext in **preferences** as a Uint8Array.
    

## XML Constraints

-   The XML type (default for preferences) cannot ensure process concurrency safety, posing risks of file corruption and data loss. It is not recommended for use in multi-process scenarios.
    
-   If the data to be stored contains a string that is not in UTF-8 format, store it in a Uint8Array. Otherwise, the persistent file may be damaged due to format errors.
    
-   The memory usage increases as more data is stored. The recommended data limit is 50 MB. For large datasets, using synchronous APIs to create a **Preferences** instance and persist data can be time-consuming. You are advised not to perform these operations in the main thread. Otherwise, application freeze issues may occur.
    

## GSKV Constraints

-   GSKV does not support cross-platform operations. Before using it, call [isStorageTypeSupported](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-data-preferences#preferencesisstoragetypesupported18) to check whether GSKV is supported.

#### Available APIs

The following table lists the APIs related to user preference persistence. For more information about the APIs, see [User Preferences](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-data-preferences).

| API | Description |
| :-- | :-- |
| getPreferencesSync(context: Context, options: Options): Preferences | Obtains a **Preferences** instance. This API returns the result synchronously. An asynchronous API is also provided. |
| putSync(key: string, value: ValueType): void | Writes data to the **Preferences** instance. This API returns the result synchronously. An asynchronous API is also provided. |
| hasSync(key: string): boolean | Checks whether the **Preferences** instance contains the KV pair with the given key. The value **true** means the instance contains the KV pair; the value **false** means the opposite. The key cannot be empty. This API returns the result synchronously. An asynchronous API is also provided. |
| getSync(key: string, defValue: ValueType): ValueType | Obtains the value of the specified key. If the value is null or not of the default value type, **defValue** is returned. This API returns the result synchronously. An asynchronous API is also provided. |
| deleteSync(key: string): void | Deletes a KV pair from the **Preferences** instance. This API returns the result synchronously. An asynchronous API is also provided. |
| flush(callback: AsyncCallback<void>): void | Flushes the data of this **Preferences** instance to a file for data persistence. |
| on(type: 'change', callback: Callback<string>): void | Subscribes to data changes. A callback will be invoked after **flush()** is executed for the data changed. |
| off(type: 'change', callback?: Callback<string>): void | Unsubscribes from data changes. |
| deletePreferences(context: Context, options: Options, callback: AsyncCallback<void>): void | Deletes a **Preferences** instance from the memory. If the **Preferences** instance has a persistent file, this API also deletes the persistent file. |
| isStorageTypeSupported(type: StorageType): boolean | Checks whether the specified storage type is supported. The value **true** means that the storage type is supported, and **false** means the opposite. |

#### How to Develop

1.  Import the **@kit.ArkData** module.
    
    import { preferences } from '@kit.ArkData';
    
2.  (Optional) Set the storage type.
    
    This step is optional. By default, preferences data is stored in XML format. Since API version 18, GSKV is supported.
    
    Before using GSKV, call **isStorageTypeSupported()** to check whether the current platform supports it.
    
    If **false** is returned, the platform does not support GSKV. In this case, use XML.
    

let isGskvSupported = preferences.isStorageTypeSupported(preferences.StorageType.GSKV);
Logger.info('Is gskv supported on this platform: ' + isGskvSupported);

1.  Obtain a **Preferences** instance.
    
    Call **getPreferencesSync()** to obtain a **Preferences** instance in the default XML format.
    

import { UIAbility } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { window } from '@kit.ArkUI';

let dataPreferences: preferences.Preferences | null = null;

class EntryAbility extends UIAbility {
  onWindowStageCreate(windowStage: window.WindowStage) {
    let options: preferences.Options = { name: 'myStore' };
    dataPreferences = preferences.getPreferencesSync(context, options);
  }
}

Call **getPreferencesSync()** to obtain a **Preferences** instance in GSKV format.

If you want to use GSKV and the platform supports it, you can obtain the **Preferences** instance as follows. However, the storage type cannot be changed once selected.

import { UIAbility } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { window } from '@kit.ArkUI';

let dataPreferences: preferences.Preferences | null = null;

class EntryAbility extends UIAbility {
  onWindowStageCreate(windowStage: window.WindowStage) {
    let options: preferences.Options = { name: 'myStore', storageType: preferences.StorageType.GSKV };
    dataPreferences = preferences.getPreferencesSync(context, options);
  }
}

1.  Write data.
    
    Call **putSync()** to write data to a **Preferences** instance.
    
    For the data stored in the default format (XML), you can call **flush()** to persist the data written if required.
    
    If GSKV is used, the data is persisted in a file on realtime basis after being written.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/36/v3/wnAc1la6RKeNQHnbTRP54Q/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061920Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=FBD4ACA46A74C06A563A954EE42AC3F91D8039EFC251FB81A60A0FBA2BE2B95B)
    
    If the key already exists, **putSync()** overwrites the value. You can use **hasSync()** to check whether the KV pair exists.
    
    Example:
    

import { util } from '@kit.ArkTS';
if (dataPreferences.hasSync('startup')) {
  Logger.info('The key startup is contained.');
} else {
  Logger.info('The key startup does not contain.');
  // Add a KV pair.
  dataPreferences.putSync('startup', 'auto');
  // In XML format, if a string contains non-UTF-8 characters, convert the string to Uint8Array format and store it. The length of the string cannot exceed 16 × 1024 × 1024 bytes.
  let uInt8Array1 = new util.TextEncoder().encodeInto('~！@#￥%……&\*（）——+？');
  dataPreferences.putSync('uInt8', uInt8Array1);
}

1.  Read data.
    
    Call **getSync()** to obtain the value of the specified key. If the value is **null** or is not of the default value type, the default data is returned.
    
    Example:
    

let val = dataPreferences.getSync('startup', 'default');
Logger.info('The startup value is ' + val);
let uInt8Array2 : preferences.ValueType = dataPreferences.getSync('uInt8', new Uint8Array(0));
// Convert the obtained Uint8Array data to a string.
let textDecoder = util.TextDecoder.create('utf-8');
val = textDecoder.decodeToString(uInt8Array2 as Uint8Array);
Logger.info('The uInt8 value is ' + val);

1.  Delete data.
    
    Call **deleteSync()** to delete a KV pair. Example:
    

dataPreferences.deleteSync('startup');

1.  Persist data.
    
    You can use **flush()** to persist the data held in a **Preferences** instance to a file. Example:
    

dataPreferences.flush((err: BusinessError) => {
  if (err) {
    Logger.error(\`Failed to flush. Code:${err.code}, message:${err.message}\`);
    return;
  }
  Logger.info('Succeeded in flushing.');
})

1.  Subscribe to data changes.
    
    Specify an observer as the callback to return the data changes for an application.
    
    If the preferences data is stored in the default format (XML), the observer callback will be triggered only after the subscribed value changes and **flush()** is executed.
    
    Example:
    

let observer = (key: string) => {
  Logger.info('The key ' + key + ' changed.');
}
dataPreferences.on('change', observer);
// The data is changed from 'auto' to 'manual'.
dataPreferences.put('startup', 'manual', (err: BusinessError) => {
  if (err) {
    Logger.error(\`Failed to put the value of 'startup'. Code:${err.code},message:${err.message}\`);
    return;
  }
  Logger.info('Succeeded in putting the value of startup.');
  if (dataPreferences !== null) {
    dataPreferences.flush((err: BusinessError) => {
      if (err) {
        Logger.error(\`Failed to flush. Code:${err.code}, message:${err.message}\`);
        return;
      }
      Logger.info('Succeeded in flushing.');
    })
  }
})

If the preferences data is stored in GSKV format, the observer callback will be triggered after the subscribed value changes (without the need for calling **flush()**).

Example:

let observer = (key: string) => {
  Logger.info('The key ' + key + ' changed.');
}
dataPreferences.on('change', observer);
// The data is changed from 'auto' to 'manual'.
dataPreferences.put('startup', 'manual', (err: BusinessError) => {
  if (err) {
    Logger.error(\`Failed to put the value of 'startup'. Code:${err.code},message:${err.message}\`);
    return;
  }
  Logger.info('Succeeded in putting the value of startup.');
})

1.  Delete a **Preferences** instance from the memory.
    
    Call **deletePreferences()** to delete a **Preferences** instance and its data from the memory. If the instance has a persistent file, the persistent file, backup file, and damaged file will also be deleted.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/da/v3/TfEB7xBoRgiUEuVqLWl2aA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061920Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=FEA14AE19DD70303224A7619FB16F8088B8D71B1085D46F66ED7B3A3B569B746)
    
    -   The deleted **Preferences** instance cannot be used for data operations. Otherwise, data inconsistency will be caused.
        
    -   The deleted data and files cannot be restored.
        
    -   If GSKV is used, this API cannot be called concurrently with other APIs (including multiple processes). Otherwise, unexpected behavior may occur.
        
    
    Example:
    

let options: preferences.Options = { name: 'myStore' };
preferences.deletePreferences(context, options, (err: BusinessError) => {
  if (err) {
    Logger.error(\`Failed to delete preferences. Code:${err.code}, message:${err.message}\`);
    return;
  }
  Logger.info('Succeeded in deleting preferences.');
})
