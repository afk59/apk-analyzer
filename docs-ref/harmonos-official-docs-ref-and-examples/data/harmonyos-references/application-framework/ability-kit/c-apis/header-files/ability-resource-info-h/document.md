# ability\_resource\_info.h

#### Overview

The file declares the APIs for obtaining the following ability resource information: bundle name, module name, ability name, icon, clone index, and whether the application is a default application.

**File to include**: <bundle/ability\_resource\_info.h>

**Library**: libbundle\_ndk.z.so

**System capability**: SystemCapability.BundleManager.BundleFramework.Core

**Since**: 21

**Related module**: [Native\_Bundle](../../modules/native-bundle/document.md)

#### Summary

#### \[h2\]Structs

| Name | typedef Keyword | Description |
| :-- | :-- | :-- |
| [OH\_NativeBundle\_AbilityResourceInfo](../../structs/oh-nativebundle-abilityresourceinfo/document.md) | OH\_NativeBundle\_AbilityResourceInfo | Describes the ability resource information. |

#### \[h2\]Functions

| Name | Description |
| :-- | :-- |
| [BundleManager\_ErrorCode OH\_NativeBundle\_GetBundleName(OH\_NativeBundle\_AbilityResourceInfo\* abilityResourceInfo, char\*\* bundleName)](#oh_nativebundle_getbundlename) | Obtains the bundle name of the ability. After using this function, you must manually release the pointer returned to prevent memory leakage. |
| [BundleManager\_ErrorCode OH\_NativeBundle\_GetModuleName(OH\_NativeBundle\_AbilityResourceInfo\* abilityResourceInfo, char\*\* moduleName)](#oh_nativebundle_getmodulename) | Obtains the module name of the ability. After using this function, you must manually release the pointer returned to prevent memory leakage. |
| [BundleManager\_ErrorCode OH\_NativeBundle\_GetAbilityName(OH\_NativeBundle\_AbilityResourceInfo\* abilityResourceInfo, char\*\* abilityName)](#oh_nativebundle_getabilityname) | Obtains the ability name. After using this function, you must manually release the pointer returned to prevent memory leakage. |
| [BundleManager\_ErrorCode OH\_NativeBundle\_GetDrawableDescriptor(OH\_NativeBundle\_AbilityResourceInfo\* abilityResourceInfo, ArkUI\_DrawableDescriptor\*\* drawableIcon)](#oh_nativebundle_getdrawabledescriptor) | Obtains the [DrawableDescriptor](../../../../arkui/c-api/structs/arkui-drawabledescriptor/document.md) object of the ability icon resource. After using this function, you must manually call [OH\_AbilityResourceInfo\_Destroy](#oh_abilityresourceinfo_destroy) to release the pointer returned to prevent memory leakage. |
| [BundleManager\_ErrorCode OH\_NativeBundle\_GetLabel(OH\_NativeBundle\_AbilityResourceInfo\* abilityResourceInfo, char\*\* label)](#oh_nativebundle_getlabel) | Obtains the application name of the ability. After using this function, you must manually release the pointer returned to prevent memory leakage. |
| [BundleManager\_ErrorCode OH\_NativeBundle\_GetAppIndex(OH\_NativeBundle\_AbilityResourceInfo\* abilityResourceInfo, int\* appIndex)](#oh_nativebundle_getappindex) | Obtains the clone index of the ability. |
| [BundleManager\_ErrorCode OH\_NativeBundle\_CheckDefaultApp(OH\_NativeBundle\_AbilityResourceInfo\* abilityResourceInfo, bool\* isDefault)](#oh_nativebundle_checkdefaultapp) | Checks whether the application to which the ability belongs is a default application. |
| [BundleManager\_ErrorCode OH\_AbilityResourceInfo\_Destroy(OH\_NativeBundle\_AbilityResourceInfo\* abilityResourceInfo, size\_t count)](#oh_abilityresourceinfo_destroy) | Releases memory allocated for ability resource information. |
| [int OH\_NativeBundle\_GetSize()](#oh_nativebundle_getsize) | Obtains the size of a single [OH\_NativeBundle\_AbilityResourceInfo](../../structs/oh-nativebundle-abilityresourceinfo/document.md) struct. |

#### Function Description

#### \[h2\]OH\_NativeBundle\_GetBundleName()

BundleManager\_ErrorCode OH\_NativeBundle\_GetBundleName(OH\_NativeBundle\_AbilityResourceInfo\* abilityResourceInfo, char\*\* bundleName)

**Description**

Obtains the bundle name of the ability. After using this function, you must manually release the pointer returned to prevent memory leakage.

**Since**: 21

**Parameters**

| Name | Description |
| :-- | :-- |
| OH\_NativeBundle\_AbilityResourceInfo\* abilityResourceInfo | Pointer to the ability resource information. |
| char\*\* bundleName | Double pointer to the bundle name. |

**Returns**

| Type | Description |
| :-- | :-- |
| [BundleManager\_ErrorCode](../bundle-manager-common-h/document.md#bundlemanager_errorcode) | 
One of the following operation results:

[BUNDLE\_MANAGER\_ERROR\_CODE\_NO\_ERROR](../bundle-manager-common-h/document.md#bundlemanager_errorcode): The retrieval is successful.

[BUNDLE\_MANAGER\_ERROR\_CODE\_PARAM\_INVALID](../bundle-manager-common-h/document.md#bundlemanager_errorcode): The retrieval fails because the **abilityResourceInfo** parameter is nullptr.

 |

#### \[h2\]OH\_NativeBundle\_GetModuleName()

BundleManager\_ErrorCode OH\_NativeBundle\_GetModuleName(OH\_NativeBundle\_AbilityResourceInfo\* abilityResourceInfo, char\*\* moduleName)

**Description**

Obtains the module name of the ability. After using this function, you must manually release the pointer returned to prevent memory leakage.

**Since**: 21

**Parameters**

| Name | Description |
| :-- | :-- |
| OH\_NativeBundle\_AbilityResourceInfo\* abilityResourceInfo | Pointer to the ability resource information. |
| char\*\* moduleName | Double pointer to the module name. |

**Returns**

| Type | Description |
| :-- | :-- |
| [BundleManager\_ErrorCode](../bundle-manager-common-h/document.md#bundlemanager_errorcode) | 
One of the following operation results:

[BUNDLE\_MANAGER\_ERROR\_CODE\_NO\_ERROR](../bundle-manager-common-h/document.md#bundlemanager_errorcode): The retrieval is successful.

[BUNDLE\_MANAGER\_ERROR\_CODE\_PARAM\_INVALID](../bundle-manager-common-h/document.md#bundlemanager_errorcode): The retrieval fails because the **abilityResourceInfo** parameter is nullptr.

 |

#### \[h2\]OH\_NativeBundle\_GetAbilityName()

BundleManager\_ErrorCode OH\_NativeBundle\_GetAbilityName(OH\_NativeBundle\_AbilityResourceInfo\* abilityResourceInfo, char\*\* abilityName)

**Description**

Obtains the ability name. After using this function, you must manually release the pointer returned to prevent memory leakage.

**Since**: 21

**Parameters**

| Name | Description |
| :-- | :-- |
| OH\_NativeBundle\_AbilityResourceInfo\* abilityResourceInfo | Pointer to the ability resource information. |
| char\*\* abilityName | Double pointer to the ability name. |

**Returns**

| Type | Description |
| :-- | :-- |
| [BundleManager\_ErrorCode](../bundle-manager-common-h/document.md#bundlemanager_errorcode) | 
One of the following operation results:

[BUNDLE\_MANAGER\_ERROR\_CODE\_NO\_ERROR](../bundle-manager-common-h/document.md#bundlemanager_errorcode): The retrieval is successful.

[BUNDLE\_MANAGER\_ERROR\_CODE\_PARAM\_INVALID](../bundle-manager-common-h/document.md#bundlemanager_errorcode): The retrieval fails because the **abilityResourceInfo** parameter is nullptr.

 |

#### \[h2\]OH\_NativeBundle\_GetDrawableDescriptor()

BundleManager\_ErrorCode OH\_NativeBundle\_GetDrawableDescriptor(OH\_NativeBundle\_AbilityResourceInfo\* abilityResourceInfo, ArkUI\_DrawableDescriptor\*\* drawableIcon)

**Description**

Obtains the [DrawableDescriptor](../../../../arkui/c-api/structs/arkui-drawabledescriptor/document.md) object of the ability icon resource. After using this function, you must manually call [OH\_AbilityResourceInfo\_Destroy](#oh_abilityresourceinfo_destroy) to release the pointer returned to prevent memory leakage.

**Since**: 21

**Parameters**

| Name | Description |
| :-- | :-- |
| OH\_NativeBundle\_AbilityResourceInfo\* abilityResourceInfo | Pointer to the ability resource information. |
| ArkUI\_DrawableDescriptor\*\* drawableIcon | Double pointer to the [DrawableDescriptor](../../../../arkui/c-api/structs/arkui-drawabledescriptor/document.md) object. |

**Returns**

| Type | Description |
| :-- | :-- |
| [BundleManager\_ErrorCode](../bundle-manager-common-h/document.md#bundlemanager_errorcode) | 
One of the following operation results:

[BUNDLE\_MANAGER\_ERROR\_CODE\_NO\_ERROR](../bundle-manager-common-h/document.md#bundlemanager_errorcode): The retrieval is successful.

[BUNDLE\_MANAGER\_ERROR\_CODE\_PARAM\_INVALID](../bundle-manager-common-h/document.md#bundlemanager_errorcode): The retrieval fails because the **abilityResourceInfo** parameter is nullptr.

 |

#### \[h2\]OH\_NativeBundle\_GetLabel()

BundleManager\_ErrorCode OH\_NativeBundle\_GetLabel(OH\_NativeBundle\_AbilityResourceInfo\* abilityResourceInfo, char\*\* label)

**Description**

Obtains the application name of the ability. After using this function, you must manually release the pointer returned to prevent memory leakage.

**Since**: 21

**Parameters**

| Name | Description |
| :-- | :-- |
| OH\_NativeBundle\_AbilityResourceInfo\* abilityResourceInfo | Pointer to the ability resource information. |
| char\*\* label | Double pointer to the application name. |

**Returns**

| Type | Description |
| :-- | :-- |
| [BundleManager\_ErrorCode](../bundle-manager-common-h/document.md#bundlemanager_errorcode) | 
One of the following operation results:

[BUNDLE\_MANAGER\_ERROR\_CODE\_NO\_ERROR](../bundle-manager-common-h/document.md#bundlemanager_errorcode): The retrieval is successful.

[BUNDLE\_MANAGER\_ERROR\_CODE\_PARAM\_INVALID](../bundle-manager-common-h/document.md#bundlemanager_errorcode): The retrieval fails because the **abilityResourceInfo** parameter is nullptr.

 |

#### \[h2\]OH\_NativeBundle\_GetAppIndex()

BundleManager\_ErrorCode OH\_NativeBundle\_GetAppIndex(OH\_NativeBundle\_AbilityResourceInfo\* abilityResourceInfo, int\* appIndex)

**Description**

Obtains the clone index of the ability.

**Since**: 21

**Parameters**

| Name | Description |
| :-- | :-- |
| OH\_NativeBundle\_AbilityResourceInfo\* abilityResourceInfo | Pointer to the ability resource information. |
| int\* appIndex | Double pointer to the clone index. |

**Returns**

| Type | Description |
| :-- | :-- |
| [BundleManager\_ErrorCode](../bundle-manager-common-h/document.md#bundlemanager_errorcode) | 
One of the following operation results:

[BUNDLE\_MANAGER\_ERROR\_CODE\_NO\_ERROR](../bundle-manager-common-h/document.md#bundlemanager_errorcode): The retrieval is successful.

[BUNDLE\_MANAGER\_ERROR\_CODE\_PARAM\_INVALID](../bundle-manager-common-h/document.md#bundlemanager_errorcode): The retrieval fails because the **abilityResourceInfo** parameter is nullptr.

 |

#### \[h2\]OH\_NativeBundle\_CheckDefaultApp()

BundleManager\_ErrorCode OH\_NativeBundle\_CheckDefaultApp(OH\_NativeBundle\_AbilityResourceInfo\* abilityResourceInfo, bool\* isDefault)

**Description**

Checks whether the application to which the ability belongs is a default application.

**Since**: 21

**Parameters**

| Name | Description |
| :-- | :-- |
| OH\_NativeBundle\_AbilityResourceInfo\* abilityResourceInfo | Pointer to the ability resource information. |
| bool\* isDefault | Pointer to the check result for whether the application is a default application. A default application is the preferred application set by the user for a specific file type or operation. **true** if the application is a default application, **false** otherwise. |

**Returns**

| Type | Description |
| :-- | :-- |
| [BundleManager\_ErrorCode](../bundle-manager-common-h/document.md#bundlemanager_errorcode) | 
One of the following operation results:

[BUNDLE\_MANAGER\_ERROR\_CODE\_NO\_ERROR](../bundle-manager-common-h/document.md#bundlemanager_errorcode): The query is successful.

[BUNDLE\_MANAGER\_ERROR\_CODE\_PARAM\_INVALID](../bundle-manager-common-h/document.md#bundlemanager_errorcode): The query fails because the **abilityResourceInfo** parameter is nullptr.

 |

#### \[h2\]OH\_AbilityResourceInfo\_Destroy()

BundleManager\_ErrorCode OH\_AbilityResourceInfo\_Destroy(OH\_NativeBundle\_AbilityResourceInfo\* abilityResourceInfo, size\_t count)

**Description**

Releases memory allocated for ability resource information.

**Since**: 21

**Parameters**

| Name | Description |
| :-- | :-- |
| OH\_NativeBundle\_AbilityResourceInfo\* abilityResourceInfo | Pointer to the ability resource information. |
| size\_t count | Size of the ability resource information array. |

**Returns**

| Type | Description |
| :-- | :-- |
| [BundleManager\_ErrorCode](../bundle-manager-common-h/document.md#bundlemanager_errorcode) | 
One of the following operation results:

[BUNDLE\_MANAGER\_ERROR\_CODE\_NO\_ERROR](../bundle-manager-common-h/document.md#bundlemanager_errorcode): The release is successful.

[BUNDLE\_MANAGER\_ERROR\_CODE\_PARAM\_INVALID](../bundle-manager-common-h/document.md#bundlemanager_errorcode): The release fails because the **abilityResourceInfo** parameter is nullptr.

 |

#### \[h2\]OH\_NativeBundle\_GetSize()

int OH\_NativeBundle\_GetSize()

**Description**

Obtains the size of a single [OH\_NativeBundle\_AbilityResourceInfo](../../structs/oh-nativebundle-abilityresourceinfo/document.md) struct.

**Since**: 21

**Returns**

| Type | Description |
| :-- | :-- |
| int | Size of a single [OH\_NativeBundle\_AbilityResourceInfo](../../structs/oh-nativebundle-abilityresourceinfo/document.md) struct. |
