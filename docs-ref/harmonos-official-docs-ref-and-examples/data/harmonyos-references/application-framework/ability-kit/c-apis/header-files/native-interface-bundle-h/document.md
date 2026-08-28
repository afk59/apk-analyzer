# native\_interface\_bundle.h

#### Overview

The file declares the APIs for obtaining the application information, including the bundle name, fingerprint information, and appId.

**File to include**: <bundle/native\_interface\_bundle.h>

**Library**: libbundle\_ndk.z.so

**System capability**: SystemCapability.BundleManager.BundleFramework.Core

**Since**: 9

**Related module**: [Native\_Bundle](../../modules/native-bundle/document.md)

#### Summary

#### \[h2\]Structs

| Name | typedef Keyword | Description |
| :-- | :-- | :-- |
| [OH\_NativeBundle\_ApplicationInfo](../../structs/oh-nativebundle-applicationinfo/document.md) | OH\_NativeBundle\_ApplicationInfo | Describes the application information, including the bundle name and fingerprint information. |
| [OH\_NativeBundle\_ElementName](../../structs/oh-nativebundle-elementname/document.md) | OH\_NativeBundle\_ElementName | Describes the elementName information. |
| [OH\_NativeBundle\_Metadata](../../structs/oh-nativebundle-metadata/document.md) | OH\_NativeBundle\_Metadata | Describes the metadata information. |
| [OH\_NativeBundle\_ModuleMetadata](../../structs/oh-nativebundle-modulemetadata/document.md) | OH\_NativeBundle\_ModuleMetadata | Describes the metadata of a module. |

#### \[h2\]Functions

| Name | Description |
| :-- | :-- |
| [OH\_NativeBundle\_ApplicationInfo OH\_NativeBundle\_GetCurrentApplicationInfo()](#oh_nativebundle_getcurrentapplicationinfo) | Obtains the current application information, including the bundle name and fingerprint information. |
| [char\* OH\_NativeBundle\_GetAppId()](#oh_nativebundle_getappid) | Obtains the appId of the current application. The appId is the unique identifier of an application and is determined by the bundle name and signature information of the application. After using this function, you must manually release the pointer returned to prevent memory leakage. |
| [char\* OH\_NativeBundle\_GetAppIdentifier()](#oh_nativebundle_getappidentifier) | Obtains the appIdentifier of the current application. The appIdentifier does not change throughout the application lifecycle, including version updates, certificate changes, public and private key changes, and application migration. After using this function, you must manually release the pointer returned to prevent memory leakage. |
| [OH\_NativeBundle\_ElementName\_OH\_NativeBundle\_GetMainElementName()](#oh_nativebundle_getmainelementname) | Obtains the mainElement information of the current application, including the bundle name, module name, and ability name. After using this function, you must manually release the pointer returned to prevent memory leakage. |
| [char\* OH\_NativeBundle\_GetCompatibleDeviceType()](#oh_nativebundle_getcompatibledevicetype) | Obtains the compatible device type of the current application. After using this function, you must manually release the pointer returned to prevent memory leakage. |
| [bool OH\_NativeBundle\_IsDebugMode(bool\* isDebugMode)](#oh_nativebundle_isdebugmode) | Checks whether the current application is in debug mode. |
| [OH\_NativeBundle\_ModuleMetadata\* OH\_NativeBundle\_GetModuleMetadata(size\_t\* size)](#oh_nativebundle_getmodulemetadata) | Obtains the module metadata array of the current application. After using this function, you must manually release the pointer returned to prevent memory leakage. |
| [BundleManager\_ErrorCode OH\_NativeBundle\_GetAbilityResourceInfo(char\* fileType, OH\_NativeBundle\_AbilityResourceInfo\*\* abilityResourceInfo, size\_t\* size)](#oh_nativebundle_getabilityresourceinfo) | Obtains a list of ability resource information that supports opening a specific file type. After using this function, you must call [OH\_AbilityResourceInfo\_Destroy](../ability-resource-info-h/document.md#oh_abilityresourceinfo_destroy) to release the pointer returned to prevent memory leakage. |

#### Function Description

#### \[h2\]OH\_NativeBundle\_GetCurrentApplicationInfo()

OH\_NativeBundle\_ApplicationInfo OH\_NativeBundle\_GetCurrentApplicationInfo()

**Description**

Obtains the current application information, including the bundle name and fingerprint information.

**Since**: 9

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_NativeBundle\_ApplicationInfo](../../structs/oh-nativebundle-applicationinfo/document.md) | 
Pointer to the OH\_NativeBundle\_ApplicationInfo object. If the returned object is NULL, the creation fails.

The possible cause is that the application address space is full, causing space allocation to fail.

 |

#### \[h2\]OH\_NativeBundle\_GetAppId()

char\* OH\_NativeBundle\_GetAppId()

**Description**

Obtains the appId of the current application. The appId is the unique identifier of an application and is determined by the bundle name and signature information of the application. After using this function, you must manually release the pointer returned to prevent memory leakage.

**Since**: 11

**Returns**

| Type | Description |
| :-- | :-- |
| char\* | 
Pointer to a new string that indicates the appID. If the returned object is NULL, the creation fails.

The possible cause is that the application address space is full, causing space allocation to fail.

 |

#### \[h2\]OH\_NativeBundle\_GetAppIdentifier()

char\* OH\_NativeBundle\_GetAppIdentifier()

**Description**

Obtains the appIdentifier of the current application. The appIdentifier does not change throughout the application lifecycle, including version updates, certificate changes, public and private key changes, and application migration. After using this function, you must manually release the pointer returned to prevent memory leakage.

**Since**: 11

**Returns**

| Type | Description |
| :-- | :-- |
| char\* | 
Pointer to a new string that indicates the appIdentifier. If the returned object is NULL, the creation fails.

The possible cause is that the application address space is full, causing space allocation to fail.

 |

#### \[h2\]OH\_NativeBundle\_GetMainElementName()

OH\_NativeBundle\_ElementName OH\_NativeBundle\_GetMainElementName()

**Description**

Obtains the mainElement information of the current application, including the bundle name, module name, and ability name. After using this function, you must manually release the pointer returned to prevent memory leakage.

**Since**: 13

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_NativeBundle\_ElementName](../../structs/oh-nativebundle-elementname/document.md) | 
Pointer to the OH\_NativeBundle\_ElementName object. If the returned object is NULL, the creation fails.

The possible cause is that the application address space is full, causing space allocation to fail.

 |

#### \[h2\]OH\_NativeBundle\_GetCompatibleDeviceType()

char\* OH\_NativeBundle\_GetCompatibleDeviceType()

**Description**

Obtains the compatible device type of the current application. It helps you optimize the layout and font size when distributing mobile applications to tablets or 2-in-1 devices. After using this function, you must manually release the pointer returned to prevent memory leakage.

**Since**: 14

**Returns**

| Type | Description |
| :-- | :-- |
| char\* | 
Pointer to a new string that indicates the compatible device type. If the returned object is NULL, the creation fails.

The possible cause is that the application address space is full, causing space allocation to fail.

 |

#### \[h2\]OH\_NativeBundle\_IsDebugMode()

bool OH\_NativeBundle\_IsDebugMode(bool\* isDebugMode)

**Description**

Checks whether the current application is in debug mode.

**Since**: 20

**Parameters**

| Name | Description |
| :-- | :-- |
| bool\* isDebugMode | Pointer to the check result indicating whether the application is in debug mode. **true** if in debug mode, **false** otherwise. |

**Returns**

| Type | Description |
| :-- | :-- |
| bool | Operation result. **true** if the call is successful, **false** otherwise. |

#### \[h2\]OH\_NativeBundle\_GetModuleMetadata()

OH\_NativeBundle\_ModuleMetadata\* OH\_NativeBundle\_GetModuleMetadata(size\_t\* size)

**Description**

Obtains the module metadata array of the current application. After using this function, you must manually release the pointer returned to prevent memory leakage.

**Since**: 20

**Parameters**

| Name | Description |
| :-- | :-- |
| size\_t\* size | Pointer to the size of the module metadata array. |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_NativeBundle\_ModuleMetadata](../../structs/oh-nativebundle-modulemetadata/document.md)\* | 
An array of module metadata. If the returned object is NULL, the retrieval fails.

The possible cause is that the application address space is full, causing space allocation to fail.

 |

#### \[h2\]OH\_NativeBundle\_GetAbilityResourceInfo()

BundleManager\_ErrorCode OH\_NativeBundle\_GetAbilityResourceInfo(char\* fileType, OH\_NativeBundle\_AbilityResourceInfo\*\* abilityResourceInfo, size\_t\* size)

**Description**

Obtains a list of ability resource information that supports opening a specific file type. After using this function, you must call [OH\_AbilityResourceInfo\_Destroy](../ability-resource-info-h/document.md#oh_abilityresourceinfo_destroy) to release the pointer returned to prevent memory leakage.

**Since**: 21

**Required permissions**: ohos.permission.GET\_ABILITY\_INFO

**Device behavior differences**: This API can be properly called only on PCs/2-in-1 devices. If it is called on other device types, error code 201 is returned.

**Parameters**

| Name | Description |
| :-- | :-- |
| char\* fileType | File type to query. You are advised to use [UTD types](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/uniform-data-type-descriptors) such as 'general.plain-text' and 'general.image'. For compatibility, [MIME types](https://www.iana.org/assignments/media-types/media-types.xhtml?utm_source=ld246.com) (for example, 'text/xml') and file name extensions (for example, '.png') are also currently accepted. For details about the mappings between file name extensions and file types, see [Prebuilt UTDs](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/uniform-data-type-list). '\*/\*' is not supported. |
| [OH\_NativeBundle\_AbilityResourceInfo](../../structs/oh-nativebundle-abilityresourceinfo/document.md)\*\* abilityResourceInfo | Double pointer to the list of ability resource information. |
| size\_t\* size | Pointer to the size of the ability resource information list. |

**Returns**

| Type | Description |
| :-- | :-- |
| [BundleManager\_ErrorCode](../bundle-manager-common-h/document.md#bundlemanager_errorcode) | 
[BUNDLE\_MANAGER\_ERROR\_CODE\_NO\_ERROR](../bundle-manager-common-h/document.md#bundlemanager_errorcode): The operation is successful.

[BUNDLE\_MANAGER\_ERROR\_CODE\_PERMISSION\_DENIED](../bundle-manager-common-h/document.md#bundlemanager_errorcode): The caller does not have the required permission.

 |
