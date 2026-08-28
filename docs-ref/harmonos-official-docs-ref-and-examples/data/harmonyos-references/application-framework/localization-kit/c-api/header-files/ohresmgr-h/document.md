# ohresmgr.h

#### Overview

Provides native APIs for obtaining resources.

**File to include**: <resourcemanager/ohresmgr.h>

**Library**: libohresmgr.so

**System capability**: SystemCapability.Global.ResourceManager

**Since**: 12

**Related module**: [resourcemanager](../../modules/resourcemanager/document.md)

#### Summary

#### \[h2\]Callback

| Name | Description |
| :-- | :-- |
| [ResourceManager\_ErrorCode OH\_ResourceManager\_GetMediaBase64(const NativeResourceManager \*mgr, uint32\_t resId, char \*\*resultValue, uint64\_t \*resultLen, uint32\_t density = 0)](#oh_resourcemanager_getmediabase64) | Obtains the Base64 code of the media resource with the specified screen density based on the specified resource ID. |
| [ResourceManager\_ErrorCode OH\_ResourceManager\_GetMediaBase64Data(const NativeResourceManager \*mgr, uint32\_t resId, char \*\*resultValue, uint64\_t \*resultLen, uint32\_t density)](#oh_resourcemanager_getmediabase64data) | Obtains the Base64 code of the media resource with the specified screen density based on the specified resource ID. |
| [ResourceManager\_ErrorCode OH\_ResourceManager\_GetMediaBase64ByName(const NativeResourceManager \*mgr, const char \*resName, char \*\*resultValue, uint64\_t \*resultLen, uint32\_t density = 0)](#oh_resourcemanager_getmediabase64byname) | Obtains the Base64 code of the media resource with the specified screen density based on the specified resource name. |
| [ResourceManager\_ErrorCode OH\_ResourceManager\_GetMediaBase64DataByName(const NativeResourceManager \*mgr, const char \*resName, char \*\*resultValue, uint64\_t \*resultLen, uint32\_t density)](#oh_resourcemanager_getmediabase64databyname) | Obtains the Base64 code of the media resource with the specified screen density based on the specified resource name. |
| [ResourceManager\_ErrorCode OH\_ResourceManager\_GetMedia(const NativeResourceManager \*mgr, uint32\_t resId, uint8\_t \*\*resultValue, uint64\_t \*resultLen, uint32\_t density = 0)](#oh_resourcemanager_getmedia) | Obtains the content of the media resource with the specified screen density based on the specified resource ID. |
| [ResourceManager\_ErrorCode OH\_ResourceManager\_GetMediaData(const NativeResourceManager \*mgr, uint32\_t resId, uint8\_t \*\*resultValue, uint64\_t \*resultLen, uint32\_t density)](#oh_resourcemanager_getmediadata) | Obtains the content of the media resource with the specified screen density based on the specified resource ID. |
| [ResourceManager\_ErrorCode OH\_ResourceManager\_GetMediaByName(const NativeResourceManager \*mgr, const char \*resName, uint8\_t \*\*resultValue, uint64\_t \*resultLen, uint32\_t density = 0)](#oh_resourcemanager_getmediabyname) | Obtains the content of the media resource with the specified screen density based on the specified resource name. |
| [ResourceManager\_ErrorCode OH\_ResourceManager\_GetMediaDataByName(const NativeResourceManager \*mgr, const char \*resName, uint8\_t \*\*resultValue, uint64\_t \*resultLen, uint32\_t density)](#oh_resourcemanager_getmediadatabyname) | Obtains the content of the media resource with the specified screen density based on the specified resource name. |
| [ResourceManager\_ErrorCode OH\_ResourceManager\_GetDrawableDescriptor(const NativeResourceManager \*mgr, uint32\_t resId, ArkUI\_DrawableDescriptor \*\*drawableDescriptor, uint32\_t density = 0, uint32\_t type = 0)](#oh_resourcemanager_getdrawabledescriptor) | Obtains the **DrawableDescriptor** object of the icon resource with the specified screen density based on the specified resource ID. |
| [ResourceManager\_ErrorCode OH\_ResourceManager\_GetDrawableDescriptorData(const NativeResourceManager \*mgr, uint32\_t resId, ArkUI\_DrawableDescriptor \*\*drawableDescriptor, uint32\_t density, uint32\_t type)](#oh_resourcemanager_getdrawabledescriptordata) | Obtains the **DrawableDescriptor** object of the icon resource with the specified screen density based on the specified resource ID. |
| [ResourceManager\_ErrorCode OH\_ResourceManager\_GetDrawableDescriptorByName(const NativeResourceManager \*mgr, const char \*resName, ArkUI\_DrawableDescriptor \*\*drawableDescriptor, uint32\_t density = 0, uint32\_t type = 0)](#oh_resourcemanager_getdrawabledescriptorbyname) | Obtains the **DrawableDescriptor** object of the icon resource with the specified screen density based on the specified resource name. |
| [ResourceManager\_ErrorCode OH\_ResourceManager\_GetDrawableDescriptorDataByName(const NativeResourceManager \*mgr, const char \*resName, ArkUI\_DrawableDescriptor \*\*drawableDescriptor, uint32\_t density, uint32\_t type)](#oh_resourcemanager_getdrawabledescriptordatabyname) | Obtains the **DrawableDescriptor** object of the icon resource with the specified screen density based on the specified resource name. |
| [ResourceManager\_ErrorCode OH\_ResourceManager\_GetSymbol(const NativeResourceManager \*mgr, uint32\_t resId, uint32\_t \*resultValue)](#oh_resourcemanager_getsymbol) | Obtains a **symbol** resource based on the specified resource ID. |
| [ResourceManager\_ErrorCode OH\_ResourceManager\_GetSymbolByName(const NativeResourceManager \*mgr, const char \*resName, uint32\_t \*resultValue)](#oh_resourcemanager_getsymbolbyname) | Obtains a **symbol** resource based on the specified resource name. |
| [ResourceManager\_ErrorCode OH\_ResourceManager\_GetLocales(const NativeResourceManager \*mgr, char \*\*\*resultValue, uint32\_t \*resultLen, bool includeSystem = false)](#oh_resourcemanager_getlocales) | Obtains the language list. After using this API, you need to call **OH\_ResourceManager\_ReleaseStringArray()** to release the memory of **locales**. |
| [ResourceManager\_ErrorCode OH\_ResourceManager\_GetLocalesData(const NativeResourceManager \*mgr, char \*\*\*resultValue, uint32\_t \*resultLen, bool includeSystem)](#oh_resourcemanager_getlocalesdata) | Obtains the language list. After using this API, you need to call **OH\_ResourceManager\_ReleaseStringArray()** to release the memory of **locales**. |
| [ResourceManager\_ErrorCode OH\_ResourceManager\_GetConfiguration(const NativeResourceManager \*mgr, ResourceManager\_Configuration \*configuration)](#oh_resourcemanager_getconfiguration) | Obtains the device configuration. After using this API, you need to call [OH\_ResourceManager\_ReleaseConfiguration](#oh_resourcemanager_releaseconfiguration) to release the memory. If the **ResourceManager\_Configuration** object is created by using malloc, call **free()** to release the object. (It is deprecated in API version 20.) |
| [ResourceManager\_ErrorCode OH\_ResourceManager\_GetResourceConfiguration(const NativeResourceManager \*mgr, ResourceManager\_Configuration \*configuration)](#oh_resourcemanager_getresourceconfiguration) | Obtains the device configuration. After using this API, you need to call [OH\_ResourceManager\_ReleaseConfiguration](#oh_resourcemanager_releaseconfiguration) to release the memory. If the **ResourceManager\_Configuration** object is created by using malloc, call **free()** to release the object. |
| [ResourceManager\_ErrorCode OH\_ResourceManager\_ReleaseConfiguration(ResourceManager\_Configuration \*configuration)](#oh_resourcemanager_releaseconfiguration) | Releases the memory requested by using [OH\_ResourceManager\_GetConfiguration](#oh_resourcemanager_getconfiguration) or [OH\_ResourceManager\_GetResourceConfiguration](#oh_resourcemanager_getresourceconfiguration). |
| [ResourceManager\_ErrorCode OH\_ResourceManager\_GetString(const NativeResourceManager \*mgr, uint32\_t resId, char \*\*resultValue, ...)](#oh_resourcemanager_getstring) | Obtains a **string** resource based on the specified resource ID. The obtain common string resources, use **OH\_ResourceManager\_GetString(mgr, resId, resultValue)**. The obtain formatted string resources with the **%d**, **%s**, and **%f** placeholders, use **OH\_ResourceManager\_GetString(mgr, resId, resultValue, 10, "format", 10.10)**. After using this API, you need to call **free()** to release the memory of the strings. |
| [ResourceManager\_ErrorCode OH\_ResourceManager\_GetStringByName(const NativeResourceManager \*mgr, const char \*resName, char \*\*resultValue, ...)](#oh_resourcemanager_getstringbyname) | Obtains a **string** resource based on the specified resource name. The obtain common string resources, use **OH\_ResourceManager\_GetString(mgr, resName, resultValue)**. The obtain formatted string resources with the **%d**, **%s**, and **%f** placeholders, use **OH\_ResourceManager\_GetString(mgr, resName, resultValue, 10, "format", 10.10)**. After using this API, you need to call **free()** to release the memory of the strings. |
| [ResourceManager\_ErrorCode OH\_ResourceManager\_GetStringArray(const NativeResourceManager \*mgr, uint32\_t resId, char \*\*\*resultValue, uint32\_t \*resultLen)](#oh_resourcemanager_getstringarray) | Obtains a string array based on the specified resource ID. After using this API, you need to call **OH\_ResourceManager\_ReleaseStringArray()** to release the memory of the string array. |
| [ResourceManager\_ErrorCode OH\_ResourceManager\_GetStringArrayByName(const NativeResourceManager \*mgr, const char \*resName, char \*\*\*resultValue, uint32\_t \*resultLen)](#oh_resourcemanager_getstringarraybyname) | Obtains a string array based on the specified resource name. After using this API, you need to call **OH\_ResourceManager\_ReleaseStringArray()** to release the memory of the string array. |
| [ResourceManager\_ErrorCode OH\_ResourceManager\_ReleaseStringArray(char \*\*\*resValue, uint32\_t len)](#oh_resourcemanager_releasestringarray) | Releases the memory of the string array. |
| [ResourceManager\_ErrorCode OH\_ResourceManager\_GetPluralString(const NativeResourceManager \*mgr, uint32\_t resId, uint32\_t num, char \*\*resultValue)](#oh_resourcemanager_getpluralstring) | Obtains singular and plural strings based on the specified resource ID. After using this API, you need to call **free()** to release the memory of the strings. (It is deprecated in API version 18.) |
| [ResourceManager\_ErrorCode OH\_ResourceManager\_GetPluralStringByName(const NativeResourceManager \*mgr, const char \*resName, uint32\_t num, char \*\*resultValue)](#oh_resourcemanager_getpluralstringbyname) | Obtains singular and plural strings based on the specified resource name. After using this API, you need to call **free()** to release the memory of the strings. (It is deprecated in API version 18.) |
| [ResourceManager\_ErrorCode OH\_ResourceManager\_GetIntPluralString(const NativeResourceManager \*mgr, uint32\_t resId, uint32\_t num, char \*\*resultValue, ...)](#oh_resourcemanager_getintpluralstring) | Obtains singular and plural strings based on the specified resource ID. After using this API, you need to call **free()** to release the memory of the strings. |
| [ResourceManager\_ErrorCode OH\_ResourceManager\_GetDoublePluralString(const NativeResourceManager \*mgr, uint32\_t resId, double num, char \*\*resultValue, ...)](#oh_resourcemanager_getdoublepluralstring) | Obtains singular and plural strings based on the specified resource ID. After using this API, you need to call **free()** to release the memory of the strings. |
| [ResourceManager\_ErrorCode OH\_ResourceManager\_GetIntPluralStringByName(const NativeResourceManager \*mgr, const char \*resName, uint32\_t num, char \*\*resultValue, ...)](#oh_resourcemanager_getintpluralstringbyname) | Obtains singular and plural strings based on the specified resource name. After using this API, you need to call **free()** to release the memory of the strings. |
| [ResourceManager\_ErrorCode OH\_ResourceManager\_GetDoublePluralStringByName(const NativeResourceManager \*mgr, const char \*resName, double num, char \*\*resultValue, ...)](#oh_resourcemanager_getdoublepluralstringbyname) | Obtains singular and plural strings based on the specified resource name. After using this API, you need to call **free()** to release the memory of the strings. |
| [ResourceManager\_ErrorCode OH\_ResourceManager\_GetColor(const NativeResourceManager \*mgr, uint32\_t resId, uint32\_t \*resultValue)](#oh_resourcemanager_getcolor) | Obtains a color value based on the specified resource ID. |
| [ResourceManager\_ErrorCode OH\_ResourceManager\_GetColorByName(const NativeResourceManager \*mgr, const char \*resName, uint32\_t \*resultValue)](#oh_resourcemanager_getcolorbyname) | Obtains a color value based on the specified resource ID. |
| [ResourceManager\_ErrorCode OH\_ResourceManager\_GetInt(const NativeResourceManager \*mgr, uint32\_t resId, int \*resultValue)](#oh_resourcemanager_getint) | Obtains an int value based on the specified resource ID. |
| [ResourceManager\_ErrorCode OH\_ResourceManager\_GetIntByName(const NativeResourceManager \*mgr, const char \*resName, int \*resultValue)](#oh_resourcemanager_getintbyname) | Obtains an int value based on the specified resource name. |
| [ResourceManager\_ErrorCode OH\_ResourceManager\_GetFloat(const NativeResourceManager \*mgr, uint32\_t resId, float \*resultValue)](#oh_resourcemanager_getfloat) | Obtains a float value based on the specified resource ID. |
| [ResourceManager\_ErrorCode OH\_ResourceManager\_GetFloatByName(const NativeResourceManager \*mgr, const char \*resName, float \*resultValue)](#oh_resourcemanager_getfloatbyname) | Obtains a float value based on the specified resource name. |
| [ResourceManager\_ErrorCode OH\_ResourceManager\_GetBool(const NativeResourceManager \*mgr, uint32\_t resId, bool \*resultValue)](#oh_resourcemanager_getbool) | Obtains a bool value based on the specified resource ID. |
| [ResourceManager\_ErrorCode OH\_ResourceManager\_GetBoolByName(const NativeResourceManager \*mgr, const char \*resName, bool \*resultValue)](#oh_resourcemanager_getboolbyname) | Obtains a bool value based on the specified resource name. |
| [ResourceManager\_ErrorCode OH\_ResourceManager\_AddResource(const NativeResourceManager \*mgr, const char \*path)](#oh_resourcemanager_addresource) | Adds overlay resources when an application is running. |
| [ResourceManager\_ErrorCode OH\_ResourceManager\_RemoveResource(const NativeResourceManager \*mgr, const char \*path)](#oh_resourcemanager_removeresource) | Removes overlay resources when an application is running. |

#### Function Description

#### \[h2\]OH\_ResourceManager\_GetMediaBase64()

ResourceManager\_ErrorCode OH\_ResourceManager\_GetMediaBase64(const NativeResourceManager \*mgr, uint32\_t resId, char \*\*resultValue, uint64\_t \*resultLen, uint32\_t density = 0)

**Description**

Obtains the Base64 code of the media resource with the specified screen density based on the specified resource ID.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [const NativeResourceManager](../../structs/nativeresourcemanager/document.md) \*mgr | Pointer to [NativeResourceManager](../../structs/nativeresourcemanager/document.md). It is obtained by using [OH\_ResourceManager\_InitNativeResourceManager](../raw-file-manager-h/document.md#oh_resourcemanager_initnativeresourcemanager). |
| uint32\_t resId | Resource ID. |
| uint32\_t density | Screen density. This parameter is optional. For details about the value range, see [ScreenDensity](../resmgr-common-h/document.md#screendensity). The default value is 0, indicating that the current system screen density (in DPI) is used. |
| char \*\*resultValue | Result of writing **resultValue**. |
| uint64\_t \*resultLen | Length of media written to **resultLen**. |

**Returns**

| Type | Description |
| :-- | :-- |
| [ResourceManager\_ErrorCode](../resmgr-common-h/document.md#resourcemanager_errorcode) | 
[SUCCESS](../resmgr-common-h/document.md#resourcemanager_errorcode) 0 - The operation is successful.

[ERROR\_CODE\_INVALID\_INPUT\_PARAMETER](../resmgr-common-h/document.md#resourcemanager_errorcode) 401 - The input parameter is invalid. Possible causes: 1. The parameter type is incorrect. 2. Parameter verification failed.

[ERROR\_CODE\_RES\_ID\_NOT\_FOUND](../resmgr-common-h/document.md#resourcemanager_errorcode) 9001001 - The resource ID is invalid.

[ERROR\_CODE\_RES\_NOT\_FOUND\_BY\_ID](../resmgr-common-h/document.md#resourcemanager_errorcode) 9001002 - No matching resource is found based on the resource ID.

[ERROR\_CODE\_OUT\_OF\_MEMORY](../resmgr-common-h/document.md#resourcemanager_errorcode) 9001100 - A memory overflow occurs.

 |

#### \[h2\]OH\_ResourceManager\_GetMediaBase64Data()

ResourceManager\_ErrorCode OH\_ResourceManager\_GetMediaBase64Data(const NativeResourceManager \*mgr, uint32\_t resId, char \*\*resultValue, uint64\_t \*resultLen, uint32\_t density)

**Description**

Obtains the Base64 code of the media resource with the specified screen density based on the specified resource ID.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [const NativeResourceManager](../../structs/nativeresourcemanager/document.md) \*mgr | Pointer to [NativeResourceManager](../../structs/nativeresourcemanager/document.md). It is obtained by using [OH\_ResourceManager\_InitNativeResourceManager](../raw-file-manager-h/document.md#oh_resourcemanager_initnativeresourcemanager). |
| uint32\_t resId | Resource ID. |
| char \*\*resultValue | Result of writing **resultValue**. |
| uint64\_t \*resultLen | Length of media written to **resultLen**. |
| uint32\_t density | Screen density. This parameter is optional. For details about the value range, see [ScreenDensity](../resmgr-common-h/document.md#screendensity). The default value is **0**, indicating that the current system screen density (in DPI) is used. If this parameter is not required, set it to **0**. |

**Returns**

| Type | Description |
| :-- | :-- |
| [ResourceManager\_ErrorCode](../resmgr-common-h/document.md#resourcemanager_errorcode) | 
[SUCCESS](../resmgr-common-h/document.md#resourcemanager_errorcode) 0 - The operation is successful.

[ERROR\_CODE\_INVALID\_INPUT\_PARAMETER](../resmgr-common-h/document.md#resourcemanager_errorcode) 401 - The input parameter is invalid. Possible causes: 1. The parameter type is incorrect. 2. Parameter verification failed.

[ERROR\_CODE\_RES\_ID\_NOT\_FOUND](../resmgr-common-h/document.md#resourcemanager_errorcode) 9001001 - The resource ID is invalid.

[ERROR\_CODE\_RES\_NOT\_FOUND\_BY\_ID](../resmgr-common-h/document.md#resourcemanager_errorcode) 9001002 - No matching resource is found based on the resource ID.

[ERROR\_CODE\_OUT\_OF\_MEMORY](../resmgr-common-h/document.md#resourcemanager_errorcode) 9001100 - A memory overflow occurs.

 |

#### \[h2\]OH\_ResourceManager\_GetMediaBase64ByName()

ResourceManager\_ErrorCode OH\_ResourceManager\_GetMediaBase64ByName(const NativeResourceManager \*mgr, const char \*resName, char \*\*resultValue, uint64\_t \*resultLen, uint32\_t density = 0)

**Description**

Obtains the Base64 code of the media resource with the specified screen density based on the specified resource name.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [const NativeResourceManager](../../structs/nativeresourcemanager/document.md) \*mgr | Pointer to [NativeResourceManager](../../structs/nativeresourcemanager/document.md). It is obtained by using [OH\_ResourceManager\_InitNativeResourceManager](../raw-file-manager-h/document.md#oh_resourcemanager_initnativeresourcemanager). |
| const char \*resName | Resource name. |
| char \*\*resultValue | Result of writing **resultValue**. |
| uint64\_t \*resultLen | Length of media written to **resultLen**. |
| uint32\_t density | Screen density. This parameter is optional. For details about the value range, see [ScreenDensity](../resmgr-common-h/document.md#screendensity). The default value is 0, indicating that the current system screen density (in DPI) is used. |

**Returns**

| Type | Description |
| :-- | :-- |
| [ResourceManager\_ErrorCode](../resmgr-common-h/document.md#resourcemanager_errorcode) | 
[SUCCESS](../resmgr-common-h/document.md#resourcemanager_errorcode) 0 - The operation is successful.

[ERROR\_CODE\_INVALID\_INPUT\_PARAMETER](../resmgr-common-h/document.md#resourcemanager_errorcode) 401 - The input parameter is invalid. Possible causes: 1. The parameter type is incorrect. 2. Parameter verification failed.

[ERROR\_CODE\_RES\_NAME\_NOT\_FOUND](../resmgr-common-h/document.md#resourcemanager_errorcode) 9001003 - The resource name is invalid.

[ERROR\_CODE\_RES\_NOT\_FOUND\_BY\_NAME](../resmgr-common-h/document.md#resourcemanager_errorcode) 9001004 - No matching resource is found based on the resource name.

[ERROR\_CODE\_OUT\_OF\_MEMORY](../resmgr-common-h/document.md#resourcemanager_errorcode) 9001100 - A memory overflow occurs.

 |

#### \[h2\]OH\_ResourceManager\_GetMediaBase64DataByName()

ResourceManager\_ErrorCode OH\_ResourceManager\_GetMediaBase64DataByName(const NativeResourceManager \*mgr, const char \*resName, char \*\*resultValue, uint64\_t \*resultLen, uint32\_t density)

**Description**

Obtains the Base64 code of the media resource with the specified screen density based on the specified resource name.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [const NativeResourceManager](../../structs/nativeresourcemanager/document.md) \*mgr | Pointer to [NativeResourceManager](../../structs/nativeresourcemanager/document.md). It is obtained by using [OH\_ResourceManager\_InitNativeResourceManager](../raw-file-manager-h/document.md#oh_resourcemanager_initnativeresourcemanager). |
| const char \*resName | Resource name. |
| char \*\*resultValue | Result of writing **resultValue**. |
| uint64\_t \*resultLen | Length of media written to **resultLen**. |
| uint32\_t density | Screen density. This parameter is optional. For details about the value range, see [ScreenDensity](../resmgr-common-h/document.md#screendensity). The default value is **0**, indicating that the current system screen density (in DPI) is used. If this parameter is not required, set it to **0**. |

**Returns**

| Type | Description |
| :-- | :-- |
| [ResourceManager\_ErrorCode](../resmgr-common-h/document.md#resourcemanager_errorcode) | 
[SUCCESS](../resmgr-common-h/document.md#resourcemanager_errorcode) 0 - The operation is successful.

[ERROR\_CODE\_INVALID\_INPUT\_PARAMETER](../resmgr-common-h/document.md#resourcemanager_errorcode) 401 - The input parameter is invalid. Possible causes: 1. The parameter type is incorrect. 2. Parameter verification failed.

[ERROR\_CODE\_RES\_NAME\_NOT\_FOUND](../resmgr-common-h/document.md#resourcemanager_errorcode) 9001003 - The resource name is invalid.

[ERROR\_CODE\_RES\_NOT\_FOUND\_BY\_NAME](../resmgr-common-h/document.md#resourcemanager_errorcode) 9001004 - No matching resource is found based on the resource name.

[ERROR\_CODE\_OUT\_OF\_MEMORY](../resmgr-common-h/document.md#resourcemanager_errorcode) 9001100 - A memory overflow occurs.

 |

#### \[h2\]OH\_ResourceManager\_GetMedia()

ResourceManager\_ErrorCode OH\_ResourceManager\_GetMedia(const NativeResourceManager \*mgr, uint32\_t resId, uint8\_t \*\*resultValue, uint64\_t \*resultLen, uint32\_t density = 0)

**Description**

Obtains the content of the media resource with the specified screen density based on the specified resource ID.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [const NativeResourceManager](../../structs/nativeresourcemanager/document.md) \*mgr | Pointer to [NativeResourceManager](../../structs/nativeresourcemanager/document.md). It is obtained by using [OH\_ResourceManager\_InitNativeResourceManager](../raw-file-manager-h/document.md#oh_resourcemanager_initnativeresourcemanager). |
| uint32\_t resId | Resource ID. |
| uint32\_t density | Screen density. This parameter is optional. For details about the value range, see [ScreenDensity](../resmgr-common-h/document.md#screendensity). The default value is 0, indicating that the current system screen density (in DPI) is used. |
| uint8\_t \*\*resultValue | Result of writing **resultValue**. |
| uint64\_t \*resultLen | Length of media written to **resultLen**. |

**Returns**

| Type | Description |
| :-- | :-- |
| [ResourceManager\_ErrorCode](../resmgr-common-h/document.md#resourcemanager_errorcode) | 
[SUCCESS](../resmgr-common-h/document.md#resourcemanager_errorcode) 0 - The operation is successful.

[ERROR\_CODE\_INVALID\_INPUT\_PARAMETER](../resmgr-common-h/document.md#resourcemanager_errorcode) 401 - The input parameter is invalid. Possible causes: 1. The parameter type is incorrect. 2. Parameter verification failed.

[ERROR\_CODE\_RES\_ID\_NOT\_FOUND](../resmgr-common-h/document.md#resourcemanager_errorcode) 9001001 - The resource ID is invalid.

[ERROR\_CODE\_RES\_NOT\_FOUND\_BY\_ID](../resmgr-common-h/document.md#resourcemanager_errorcode) 9001002 - No matching resource is found based on the resource ID.

[ERROR\_CODE\_OUT\_OF\_MEMORY](../resmgr-common-h/document.md#resourcemanager_errorcode) 9001100 - A memory overflow occurs.

 |

#### \[h2\]OH\_ResourceManager\_GetMediaData()

ResourceManager\_ErrorCode OH\_ResourceManager\_GetMediaData(const NativeResourceManager \*mgr, uint32\_t resId, uint8\_t \*\*resultValue, uint64\_t \*resultLen, uint32\_t density)

**Description**

Obtains the content of the media resource with the specified screen density based on the specified resource ID.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [const NativeResourceManager](../../structs/nativeresourcemanager/document.md) \*mgr | Pointer to [NativeResourceManager](../../structs/nativeresourcemanager/document.md). It is obtained by using [OH\_ResourceManager\_InitNativeResourceManager](../raw-file-manager-h/document.md#oh_resourcemanager_initnativeresourcemanager). |
| uint32\_t resId | Resource ID. |
| uint8\_t \*\*resultValue | Result of writing **resultValue**. |
| uint64\_t \*resultLen | Length of media written to **resultLen**. |
| uint32\_t density | Screen density. This parameter is optional. For details about the value range, see [ScreenDensity](../resmgr-common-h/document.md#screendensity). The default value is **0**, indicating that the current system screen density (in DPI) is used. If this parameter is not required, set it to **0**. |

**Returns**

| Type | Description |
| :-- | :-- |
| [ResourceManager\_ErrorCode](../resmgr-common-h/document.md#resourcemanager_errorcode) | 
[SUCCESS](../resmgr-common-h/document.md#resourcemanager_errorcode) 0 - The operation is successful.

[ERROR\_CODE\_INVALID\_INPUT\_PARAMETER](../resmgr-common-h/document.md#resourcemanager_errorcode) 401 - The input parameter is invalid. Possible causes: 1. The parameter type is incorrect. 2. Parameter verification failed.

[ERROR\_CODE\_RES\_ID\_NOT\_FOUND](../resmgr-common-h/document.md#resourcemanager_errorcode) 9001001 - The resource ID is invalid.

[ERROR\_CODE\_RES\_NOT\_FOUND\_BY\_ID](../resmgr-common-h/document.md#resourcemanager_errorcode) 9001002 - No matching resource is found based on the resource ID.

[ERROR\_CODE\_OUT\_OF\_MEMORY](../resmgr-common-h/document.md#resourcemanager_errorcode) 9001100 - A memory overflow occurs.

 |

#### \[h2\]OH\_ResourceManager\_GetMediaByName()

ResourceManager\_ErrorCode OH\_ResourceManager\_GetMediaByName(const NativeResourceManager \*mgr, const char \*resName, uint8\_t \*\*resultValue, uint64\_t \*resultLen, uint32\_t density = 0)

**Description**

Obtains the content of the media resource with the specified screen density based on the specified resource name.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [const NativeResourceManager](../../structs/nativeresourcemanager/document.md) \*mgr | Pointer to [NativeResourceManager](../../structs/nativeresourcemanager/document.md). It is obtained by using [OH\_ResourceManager\_InitNativeResourceManager](../raw-file-manager-h/document.md#oh_resourcemanager_initnativeresourcemanager). |
| const char \*resName | Resource name. |
| uint32\_t density | Screen density. This parameter is optional. For details about the value range, see [ScreenDensity](../resmgr-common-h/document.md#screendensity). The default value is 0, indicating that the current system screen density (in DPI) is used. |
| uint8\_t \*\*resultValue | Result of writing **resultValue**. |
| uint64\_t \*resultLen | Length of media written to **resultLen**. |

**Returns**

| Type | Description |
| :-- | :-- |
| [ResourceManager\_ErrorCode](../resmgr-common-h/document.md#resourcemanager_errorcode) | 
[SUCCESS](../resmgr-common-h/document.md#resourcemanager_errorcode) 0 - The operation is successful.

[ERROR\_CODE\_INVALID\_INPUT\_PARAMETER](../resmgr-common-h/document.md#resourcemanager_errorcode) 401 - The input parameter is invalid. Possible causes: 1. The parameter type is incorrect. 2. Parameter verification failed.

[ERROR\_CODE\_RES\_NAME\_NOT\_FOUND](../resmgr-common-h/document.md#resourcemanager_errorcode) 9001003 - The resource name is invalid.

[ERROR\_CODE\_RES\_NOT\_FOUND\_BY\_NAME](../resmgr-common-h/document.md#resourcemanager_errorcode) 9001004 - No matching resource is found based on the resource name.

[ERROR\_CODE\_OUT\_OF\_MEMORY](../resmgr-common-h/document.md#resourcemanager_errorcode) 9001100 - A memory overflow occurs.

 |

#### \[h2\]OH\_ResourceManager\_GetMediaDataByName()

ResourceManager\_ErrorCode OH\_ResourceManager\_GetMediaDataByName(const NativeResourceManager \*mgr, const char \*resName, uint8\_t \*\*resultValue, uint64\_t \*resultLen, uint32\_t density)

**Description**

Obtains the content of the media resource with the specified screen density based on the specified resource name.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [const NativeResourceManager](../../structs/nativeresourcemanager/document.md) \*mgr | Pointer to [NativeResourceManager](../../structs/nativeresourcemanager/document.md). It is obtained by using [OH\_ResourceManager\_InitNativeResourceManager](../raw-file-manager-h/document.md#oh_resourcemanager_initnativeresourcemanager). |
| const char \*resName | Resource name. |
| uint8\_t \*\*resultValue | Result of writing **resultValue**. |
| uint64\_t \*resultLen | Length of media written to **resultLen**. |
| uint32\_t density | Screen density. This parameter is optional. For details about the value range, see [ScreenDensity](../resmgr-common-h/document.md#screendensity). The default value is **0**, indicating that the current system screen density (in DPI) is used. If this parameter is not required, set it to **0**. |

**Returns**

| Type | Description |
| :-- | :-- |
| [ResourceManager\_ErrorCode](../resmgr-common-h/document.md#resourcemanager_errorcode) | 
[SUCCESS](../resmgr-common-h/document.md#resourcemanager_errorcode) 0 - The operation is successful.

[ERROR\_CODE\_INVALID\_INPUT\_PARAMETER](../resmgr-common-h/document.md#resourcemanager_errorcode) 401 - The input parameter is invalid. Possible causes: 1. The parameter type is incorrect. 2. Parameter verification failed.

[ERROR\_CODE\_RES\_NAME\_NOT\_FOUND](../resmgr-common-h/document.md#resourcemanager_errorcode) 9001003 - The resource name is invalid.

[ERROR\_CODE\_RES\_NOT\_FOUND\_BY\_NAME](../resmgr-common-h/document.md#resourcemanager_errorcode) 9001004 - No matching resource is found based on the resource name.

[ERROR\_CODE\_OUT\_OF\_MEMORY](../resmgr-common-h/document.md#resourcemanager_errorcode) 9001100 - A memory overflow occurs.

 |

#### \[h2\]OH\_ResourceManager\_GetDrawableDescriptor()

ResourceManager\_ErrorCode OH\_ResourceManager\_GetDrawableDescriptor(const NativeResourceManager \*mgr, uint32\_t resId, ArkUI\_DrawableDescriptor \*\*drawableDescriptor, uint32\_t density = 0, uint32\_t type = 0)

**Description**

Obtains the **DrawableDescriptor** object of the icon resource with the specified screen density based on the specified resource ID.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [const NativeResourceManager](../../structs/nativeresourcemanager/document.md) \*mgr | Pointer to [NativeResourceManager](../../structs/nativeresourcemanager/document.md). It is obtained by using [OH\_ResourceManager\_InitNativeResourceManager](../raw-file-manager-h/document.md#oh_resourcemanager_initnativeresourcemanager). |
| uint32\_t | Resource ID. |
| uint32\_t density | Screen density. This parameter is optional. For details about the value range, see [ScreenDensity](../resmgr-common-h/document.md#screendensity). The default value is 0, indicating that the current system screen density (in DPI) is used. |
| uint32\_t type | Icon type. The value **0** indicates an application icon, and the value **1** indicates a theme icon. |
| [ArkUI\_DrawableDescriptor](../../../../arkui/c-api/structs/arkui-drawabledescriptor/document.md) \*\*drawableDescriptor | Result of writing **drawableDescriptor**. |

**Returns**

| Type | Description |
| :-- | :-- |
| [ResourceManager\_ErrorCode](../resmgr-common-h/document.md#resourcemanager_errorcode) | 
[SUCCESS](../resmgr-common-h/document.md#resourcemanager_errorcode) 0 - The operation is successful.

[ERROR\_CODE\_INVALID\_INPUT\_PARAMETER](../resmgr-common-h/document.md#resourcemanager_errorcode) 401 - The input parameter is invalid. Possible causes: 1. The parameter type is incorrect. 2. Parameter verification failed.

[ERROR\_CODE\_RES\_ID\_NOT\_FOUND](../resmgr-common-h/document.md#resourcemanager_errorcode) 9001001 - The resource ID is invalid.

[ERROR\_CODE\_RES\_NOT\_FOUND\_BY\_ID](../resmgr-common-h/document.md#resourcemanager_errorcode) 9001002 - No matching resource is found based on the resource ID.

 |

#### \[h2\]OH\_ResourceManager\_GetDrawableDescriptorData()

ResourceManager\_ErrorCode OH\_ResourceManager\_GetDrawableDescriptorData(const NativeResourceManager \*mgr, uint32\_t resId, ArkUI\_DrawableDescriptor \*\*drawableDescriptor, uint32\_t density, uint32\_t type)

**Description**

Obtains the **DrawableDescriptor** object of the icon resource with the specified screen density based on the specified resource ID.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [const NativeResourceManager](../../structs/nativeresourcemanager/document.md) \*mgr | Pointer to [NativeResourceManager](../../structs/nativeresourcemanager/document.md). It is obtained by using [OH\_ResourceManager\_InitNativeResourceManager](../raw-file-manager-h/document.md#oh_resourcemanager_initnativeresourcemanager). |
| uint32\_t resId | Resource ID. |
| [ArkUI\_DrawableDescriptor](../../../../arkui/c-api/structs/arkui-drawabledescriptor/document.md) \*\*drawableDescriptor | Result of writing **drawableDescriptor**. |
| uint32\_t density | Screen density. This parameter is optional. For details about the value range, see [ScreenDensity](../resmgr-common-h/document.md#screendensity). The default value is **0**, indicating that the current system screen density (in DPI) is used. If this parameter is not required, set it to **0**. |
| uint32\_t type | Icon type. This parameter is optional. The value **0** indicates an application icon, and the value **1** indicates a theme icon. If this parameter is not required, set it to **0**. |

**Returns**

| Type | Description |
| :-- | :-- |
| [ResourceManager\_ErrorCode](../resmgr-common-h/document.md#resourcemanager_errorcode) | 
[SUCCESS](../resmgr-common-h/document.md#resourcemanager_errorcode) 0 - The operation is successful.

[ERROR\_CODE\_INVALID\_INPUT\_PARAMETER](../resmgr-common-h/document.md#resourcemanager_errorcode) 401 - The input parameter is invalid. Possible causes: 1. The parameter type is incorrect. 2. Parameter verification failed.

[ERROR\_CODE\_RES\_ID\_NOT\_FOUND](../resmgr-common-h/document.md#resourcemanager_errorcode) 9001001 - The resource ID is invalid.

[ERROR\_CODE\_RES\_NOT\_FOUND\_BY\_ID](../resmgr-common-h/document.md#resourcemanager_errorcode) 9001002 - No matching resource is found based on the resource ID.

 |

#### \[h2\]OH\_ResourceManager\_GetDrawableDescriptorByName()

ResourceManager\_ErrorCode OH\_ResourceManager\_GetDrawableDescriptorByName(const NativeResourceManager \*mgr, const char \*resName, ArkUI\_DrawableDescriptor \*\*drawableDescriptor, uint32\_t density = 0, uint32\_t type = 0)

**Description**

Obtains the **DrawableDescriptor** object of the icon resource with the specified screen density based on the specified resource name.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [const NativeResourceManager](../../structs/nativeresourcemanager/document.md) \*mgr | Pointer to [NativeResourceManager](../../structs/nativeresourcemanager/document.md). It is obtained by using [OH\_ResourceManager\_InitNativeResourceManager](../raw-file-manager-h/document.md#oh_resourcemanager_initnativeresourcemanager). |
| const char \*resName | Resource name. |
| uint32\_t density | Screen density. This parameter is optional. For details about the value range, see [ScreenDensity](../resmgr-common-h/document.md#screendensity). The default value is 0, indicating that the current system screen density (in DPI) is used. |
| uint32\_t type | Icon type. This parameter is optional. The value **0** indicates an application icon, the value **1** indicates a theme icon, and the value **2** indicates a dynamic icon. |
| [ArkUI\_DrawableDescriptor](../../../../arkui/c-api/structs/arkui-drawabledescriptor/document.md) \*\*drawableDescriptor | Result of writing **drawableDescriptor**. |

**Returns**

| Type | Description |
| :-- | :-- |
| [ResourceManager\_ErrorCode](../resmgr-common-h/document.md#resourcemanager_errorcode) | 
[SUCCESS](../resmgr-common-h/document.md#resourcemanager_errorcode) 0 - The operation is successful.

[ERROR\_CODE\_INVALID\_INPUT\_PARAMETER](../resmgr-common-h/document.md#resourcemanager_errorcode) 401 - The input parameter is invalid. Possible causes: 1. The parameter type is incorrect. 2. Parameter verification failed.

[ERROR\_CODE\_RES\_NAME\_NOT\_FOUND](../resmgr-common-h/document.md#resourcemanager_errorcode) 9001003 - The resource name is invalid.

[ERROR\_CODE\_RES\_NOT\_FOUND\_BY\_NAME](../resmgr-common-h/document.md#resourcemanager_errorcode) 9001004 - No matching resource is found based on the resource name.

 |

#### \[h2\]OH\_ResourceManager\_GetDrawableDescriptorDataByName()

ResourceManager\_ErrorCode OH\_ResourceManager\_GetDrawableDescriptorDataByName(const NativeResourceManager \*mgr, const char \*resName, ArkUI\_DrawableDescriptor \*\*drawableDescriptor, uint32\_t density, uint32\_t type)

**Description**

Obtains the **DrawableDescriptor** object of the icon resource with the specified screen density based on the specified resource name.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [const NativeResourceManager](../../structs/nativeresourcemanager/document.md) \*mgr | Pointer to [NativeResourceManager](../../structs/nativeresourcemanager/document.md). It is obtained by using [OH\_ResourceManager\_InitNativeResourceManager](../raw-file-manager-h/document.md#oh_resourcemanager_initnativeresourcemanager). |
| const char \*resName | Resource name. |
| [ArkUI\_DrawableDescriptor](../../../../arkui/c-api/structs/arkui-drawabledescriptor/document.md) \*\*drawableDescriptor | Result of writing **drawableDescriptor**. |
| uint32\_t density | Screen density. This parameter is optional. For details about the value range, see [ScreenDensity](../resmgr-common-h/document.md#screendensity). The default value is **0**, indicating that the current system screen density (in DPI) is used. If this parameter is not required, set it to **0**. |
| uint32\_t type | Icon type. This parameter is optional. The value **0** indicates an application icon, and the value **1** indicates a theme icon. If this parameter is not required, set it to **0**. |

**Returns**

| Type | Description |
| :-- | :-- |
| [ResourceManager\_ErrorCode](../resmgr-common-h/document.md#resourcemanager_errorcode) | 
[SUCCESS](../resmgr-common-h/document.md#resourcemanager_errorcode) 0 - The operation is successful.

[ERROR\_CODE\_INVALID\_INPUT\_PARAMETER](../resmgr-common-h/document.md#resourcemanager_errorcode) 401 - The input parameter is invalid. Possible causes: 1. The parameter type is incorrect. 2. Parameter verification failed.

[ERROR\_CODE\_RES\_NAME\_NOT\_FOUND](../resmgr-common-h/document.md#resourcemanager_errorcode) 9001003 - The resource name is invalid.

[ERROR\_CODE\_RES\_NOT\_FOUND\_BY\_NAME](../resmgr-common-h/document.md#resourcemanager_errorcode) 9001004 - No matching resource is found based on the resource name.

 |

#### \[h2\]OH\_ResourceManager\_GetSymbol()

ResourceManager\_ErrorCode OH\_ResourceManager\_GetSymbol(const NativeResourceManager \*mgr, uint32\_t resId, uint32\_t \*resultValue)

**Description**

Obtains a **symbol** resource based on the specified resource ID.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [const NativeResourceManager](../../structs/nativeresourcemanager/document.md) \*mgr | Pointer to [NativeResourceManager](../../structs/nativeresourcemanager/document.md). It is obtained by using [OH\_ResourceManager\_InitNativeResourceManager](../raw-file-manager-h/document.md#oh_resourcemanager_initnativeresourcemanager). |
| uint32\_t resId | Resource ID. |
| uint32\_t \*resultValue | Result of writing **resultValue**. |

**Returns**

| Type | Description |
| :-- | :-- |
| [ResourceManager\_ErrorCode](../resmgr-common-h/document.md#resourcemanager_errorcode) | 
[SUCCESS](../resmgr-common-h/document.md#resourcemanager_errorcode) 0 - The operation is successful.

[ERROR\_CODE\_INVALID\_INPUT\_PARAMETER](../resmgr-common-h/document.md#resourcemanager_errorcode) 401 - The input parameter is invalid. Possible causes: 1. The parameter type is incorrect. 2. Parameter verification failed.

[ERROR\_CODE\_RES\_ID\_NOT\_FOUND](../resmgr-common-h/document.md#resourcemanager_errorcode) 9001001 - The resource ID is invalid.

[ERROR\_CODE\_RES\_NOT\_FOUND\_BY\_ID](../resmgr-common-h/document.md#resourcemanager_errorcode) 9001002 - No matching resource is found based on the resource ID.

[ERROR\_CODE\_RES\_REF\_TOO\_MUCH](../resmgr-common-h/document.md#resourcemanager_errorcode) 9001006 - The resource is cyclically referenced.

 |

#### \[h2\]OH\_ResourceManager\_GetSymbolByName()

ResourceManager\_ErrorCode OH\_ResourceManager\_GetSymbolByName(const NativeResourceManager \*mgr, const char \*resName, uint32\_t \*resultValue)

**Description**

Obtains a **symbol** resource based on the specified resource name.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [const NativeResourceManager](../../structs/nativeresourcemanager/document.md) \*mgr | Pointer to [NativeResourceManager](../../structs/nativeresourcemanager/document.md). It is obtained by using [OH\_ResourceManager\_InitNativeResourceManager](../raw-file-manager-h/document.md#oh_resourcemanager_initnativeresourcemanager). |
| const char \*resName | Resource name. |
| uint32\_t \*resultValue | Result of writing **resultValue**. |

**Returns**

| Type | Description |
| :-- | :-- |
| [ResourceManager\_ErrorCode](../resmgr-common-h/document.md#resourcemanager_errorcode) | 
[SUCCESS](../resmgr-common-h/document.md#resourcemanager_errorcode) 0 - The operation is successful.

[ERROR\_CODE\_INVALID\_INPUT\_PARAMETER](../resmgr-common-h/document.md#resourcemanager_errorcode) 401 - The input parameter is invalid. Possible causes: 1. The parameter type is incorrect. 2. Parameter verification failed.

[ERROR\_CODE\_RES\_NAME\_NOT\_FOUND](../resmgr-common-h/document.md#resourcemanager_errorcode) 9001003 - The resource name is invalid.

[ERROR\_CODE\_RES\_NOT\_FOUND\_BY\_NAME](../resmgr-common-h/document.md#resourcemanager_errorcode) 9001004 - No matching resource is found based on the resource name.

[ERROR\_CODE\_RES\_REF\_TOO\_MUCH](../resmgr-common-h/document.md#resourcemanager_errorcode) 9001006 - The resource is cyclically referenced.

 |

#### \[h2\]OH\_ResourceManager\_GetLocales()

ResourceManager\_ErrorCode OH\_ResourceManager\_GetLocales(const NativeResourceManager \*mgr, char \*\*\*resultValue, uint32\_t \*resultLen, bool includeSystem = false)

**Description**

Obtains the language list. After using this API, you need to call **OH\_ResourceManager\_ReleaseStringArray()** to release the memory of **locales**.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [const NativeResourceManager](../../structs/nativeresourcemanager/document.md) \*mgr | Pointer to [NativeResourceManager](../../structs/nativeresourcemanager/document.md). It is obtained by using [OH\_ResourceManager\_InitNativeResourceManager](../raw-file-manager-h/document.md#oh_resourcemanager_initnativeresourcemanager). |
| char \*\*\*resultValue | Result of writing **resultValue**. |
| uint32\_t \*resultLen | Length of locales written to **resultLen**. |
| bool includeSystem | Whether system resources are included. The default value is **false**. This parameter does not take effect if only system resources are involved when you query the list of locales. |

**Returns**

| Type | Description |
| :-- | :-- |
| [ResourceManager\_ErrorCode](../resmgr-common-h/document.md#resourcemanager_errorcode) | 
[SUCCESS](../resmgr-common-h/document.md#resourcemanager_errorcode) 0 - The operation is successful.

[ERROR\_CODE\_INVALID\_INPUT\_PARAMETER](../resmgr-common-h/document.md#resourcemanager_errorcode) 401 - The input parameter is invalid. Possible causes: 1. The parameter type is incorrect. 2. Parameter verification failed.

[ERROR\_CODE\_OUT\_OF\_MEMORY](../resmgr-common-h/document.md#resourcemanager_errorcode) 9001100 - A memory overflow occurs.

 |

#### \[h2\]OH\_ResourceManager\_GetLocalesData()

ResourceManager\_ErrorCode OH\_ResourceManager\_GetLocalesData(const NativeResourceManager \*mgr, char \*\*\*resultValue, uint32\_t \*resultLen, bool includeSystem)

**Description**

Obtains the language list. After using this API, you need to call **OH\_ResourceManager\_ReleaseStringArray()** to release the memory of **locales**.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [const NativeResourceManager](../../structs/nativeresourcemanager/document.md) \*mgr | Pointer to [NativeResourceManager](../../structs/nativeresourcemanager/document.md). It is obtained by using [OH\_ResourceManager\_InitNativeResourceManager](../raw-file-manager-h/document.md#oh_resourcemanager_initnativeresourcemanager). |
| char \*\*\*resultValue | Result of writing **resultValue**. |
| uint32\_t \*resultLen | Length of locales written to **resultLen**. |
| bool includeSystem | Whether system resources are included. If this parameter is not required, set it to **false**. |

**Returns**

| Type | Description |
| :-- | :-- |
| [ResourceManager\_ErrorCode](../resmgr-common-h/document.md#resourcemanager_errorcode) | 
[SUCCESS](../resmgr-common-h/document.md#resourcemanager_errorcode) 0 - The operation is successful.

[ERROR\_CODE\_INVALID\_INPUT\_PARAMETER](../resmgr-common-h/document.md#resourcemanager_errorcode) 401 - The input parameter is invalid. Possible causes: 1. The parameter type is incorrect. 2. Parameter verification failed.

[ERROR\_CODE\_OUT\_OF\_MEMORY](../resmgr-common-h/document.md#resourcemanager_errorcode) 9001100 - A memory overflow occurs.

 |

#### \[h2\]OH\_ResourceManager\_GetConfiguration()

ResourceManager\_ErrorCode OH\_ResourceManager\_GetConfiguration(const NativeResourceManager \*mgr, ResourceManager\_Configuration \*configuration)

**Description**

Obtains the device configuration. After this API is used, call [OH\_ResourceManager\_ReleaseConfiguration](#oh_resourcemanager_releaseconfiguration) to release the memory. If the **ResourceManager\_Configuration** object is created by using malloc, call **free()** to release the object.

**Since**: 12

**Deprecated from**: 20

**Substitute**: [OH\_ResourceManager\_GetResourceConfiguration](#oh_resourcemanager_getresourceconfiguration)

**Parameters**

| Name | Description |
| :-- | :-- |
| [const NativeResourceManager](../../structs/nativeresourcemanager/document.md) \*mgr | Pointer to [NativeResourceManager](../../structs/nativeresourcemanager/document.md). It is obtained by using [OH\_ResourceManager\_InitNativeResourceManager](../raw-file-manager-h/document.md#oh_resourcemanager_initnativeresourcemanager). |
| [ResourceManager\_Configuration](../../structs/resourcemanager-configuration/document.md) \*configuration | Device configuration. The return value of **configuration.screenDensity** is the rounded value of the device's DPI divided by 160. |

**Returns**

| Type | Description |
| :-- | :-- |
| [ResourceManager\_ErrorCode](../resmgr-common-h/document.md#resourcemanager_errorcode) | 
[SUCCESS](../resmgr-common-h/document.md#resourcemanager_errorcode) 0 - The operation is successful.

[ERROR\_CODE\_INVALID\_INPUT\_PARAMETER](../resmgr-common-h/document.md#resourcemanager_errorcode) 401 - The input parameter is invalid. Possible causes: 1. The parameter type is incorrect. 2. Parameter verification failed.

[ERROR\_CODE\_SYSTEM\_RES\_MANAGER\_GET\_FAILED](../resmgr-common-h/document.md#resourcemanager_errorcode) 9001009 - The attempt to access system resources fails.

[ERROR\_CODE\_OUT\_OF\_MEMORY](../resmgr-common-h/document.md#resourcemanager_errorcode) 9001100 - A memory overflow occurs.

 |

#### \[h2\]OH\_ResourceManager\_GetResourceConfiguration()

ResourceManager\_ErrorCode OH\_ResourceManager\_GetResourceConfiguration(const NativeResourceManager \*mgr, ResourceManager\_Configuration \*configuration)

**Description**

Obtains the device configuration. After this API is used, call [OH\_ResourceManager\_ReleaseConfiguration](#oh_resourcemanager_releaseconfiguration) to release the memory. If the **ResourceManager\_Configuration** object is created by using malloc, call **free()** to release the object.

**Since**: 20

**Parameters**

| Name | Description |
| :-- | :-- |
| [const NativeResourceManager](../../structs/nativeresourcemanager/document.md) \*mgr | Pointer to [NativeResourceManager](../../structs/nativeresourcemanager/document.md). It is obtained by using [OH\_ResourceManager\_InitNativeResourceManager](../raw-file-manager-h/document.md#oh_resourcemanager_initnativeresourcemanager). |
| [ResourceManager\_Configuration](../../structs/resourcemanager-configuration/document.md) \*configuration | Device configuration. The return value of **configuration.screenDensity** is the device's DPI. |

**Returns**

| Type | Description |
| :-- | :-- |
| [ResourceManager\_ErrorCode](../resmgr-common-h/document.md#resourcemanager_errorcode) | 
[SUCCESS](../resmgr-common-h/document.md#resourcemanager_errorcode) 0 - The operation is successful.

[ERROR\_CODE\_SYSTEM\_RES\_MANAGER\_GET\_FAILED](../resmgr-common-h/document.md#resourcemanager_errorcode) 9001009 - The attempt to access system resources fails.

[ERROR\_CODE\_OUT\_OF\_MEMORY](../resmgr-common-h/document.md#resourcemanager_errorcode) 9001100 - A memory overflow occurs.

 |

#### \[h2\]OH\_ResourceManager\_ReleaseConfiguration()

ResourceManager\_ErrorCode OH\_ResourceManager\_ReleaseConfiguration(ResourceManager\_Configuration \*configuration)

**Description**

Releases the memory requested by using the [OH\_ResourceManager\_GetConfiguration](#oh_resourcemanager_getconfiguration) and [OH\_ResourceManager\_GetResourceConfiguration](#oh_resourcemanager_getresourceconfiguration) methods.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [ResourceManager\_Configuration](../../structs/resourcemanager-configuration/document.md) \*configuration | Configuration object whose memory needs to be released. |

**Returns**

| Type | Description |
| :-- | :-- |
| [ResourceManager\_ErrorCode](../resmgr-common-h/document.md#resourcemanager_errorcode) | 
[SUCCESS](../resmgr-common-h/document.md#resourcemanager_errorcode) 0 - The operation is successful.

[ERROR\_CODE\_INVALID\_INPUT\_PARAMETER](../resmgr-common-h/document.md#resourcemanager_errorcode) 401 - The input parameter is invalid. Possible causes: 1. The parameter type is incorrect. 2. Parameter verification failed.

 |

#### \[h2\]OH\_ResourceManager\_GetString()

ResourceManager\_ErrorCode OH\_ResourceManager\_GetString(const NativeResourceManager \*mgr, uint32\_t resId, char \*\*resultValue, ...)

**Description**

Obtains a **string** resource based on the specified resource ID. The obtain common string resources, use **OH\_ResourceManager\_GetString(mgr, resId, resultValue)**. The obtain formatted string resources with the **%d**, **%s**, and **%f** placeholders, use **OH\_ResourceManager\_GetString(mgr, resId, resultValue, 10, "format", 10.10)**. After using this API, you need to call **free()** to release the memory of the strings.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [const NativeResourceManager](../../structs/nativeresourcemanager/document.md) \*mgr | Pointer to [NativeResourceManager](../../structs/nativeresourcemanager/document.md). It is obtained by using [OH\_ResourceManager\_InitNativeResourceManager](../raw-file-manager-h/document.md#oh_resourcemanager_initnativeresourcemanager). |
| uint32\_t resId | Resource ID. |
| char \*\*resultValue | Result of writing **resultValue**. |
| ... | Variable representing formatted string resources. Supported types include const char\*, int, and float. |

**Returns**

| Type | Description |
| :-- | :-- |
| [ResourceManager\_ErrorCode](../resmgr-common-h/document.md#resourcemanager_errorcode) | 
[SUCCESS](../resmgr-common-h/document.md#resourcemanager_errorcode) 0 - The operation is successful.

[ERROR\_CODE\_INVALID\_INPUT\_PARAMETER](../resmgr-common-h/document.md#resourcemanager_errorcode) 401 - The input parameter is invalid. Possible causes: 1. The parameter type is incorrect. 2. Parameter verification failed.

[ERROR\_CODE\_RES\_ID\_NOT\_FOUND](../resmgr-common-h/document.md#resourcemanager_errorcode) 9001001 - The resource ID is invalid.

[ERROR\_CODE\_RES\_NOT\_FOUND\_BY\_ID](../resmgr-common-h/document.md#resourcemanager_errorcode) 9001002 - No matching resource is found based on the resource ID.

[ERROR\_CODE\_RES\_REF\_TOO\_MUCH](../resmgr-common-h/document.md#resourcemanager_errorcode) 9001006 - The resource is cyclically referenced.

[ERROR\_CODE\_OUT\_OF\_MEMORY](../resmgr-common-h/document.md#resourcemanager_errorcode) 9001100 - A memory overflow occurs.

 |

#### \[h2\]OH\_ResourceManager\_GetStringByName()

ResourceManager\_ErrorCode OH\_ResourceManager\_GetStringByName(const NativeResourceManager \*mgr, const char \*resName, char \*\*resultValue, ...)

**Description**

Obtains a **string** resource based on the specified resource name. The obtain common string resources, use **OH\_ResourceManager\_GetString(mgr, resName, resultValue)**. The obtain formatted string resources with the **%d**, **%s**, and **%f** placeholders, use **OH\_ResourceManager\_GetString(mgr, resName, resultValue, 10, "format", 10.10)**. After using this API, you need to call **free()** to release the memory of the strings.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [const NativeResourceManager](../../structs/nativeresourcemanager/document.md) \*mgr | Pointer to [NativeResourceManager](../../structs/nativeresourcemanager/document.md). It is obtained by using [OH\_ResourceManager\_InitNativeResourceManager](../raw-file-manager-h/document.md#oh_resourcemanager_initnativeresourcemanager). |
| const char \*resName | Resource name. |
| char \*\*resultValue | Result of writing **resultValue**. |
| ... | Variable representing formatted string resources. Supported types include const char\*, int, and float. |

**Returns**

| Type | Description |
| :-- | :-- |
| [ResourceManager\_ErrorCode](../resmgr-common-h/document.md#resourcemanager_errorcode) | 
[SUCCESS](../resmgr-common-h/document.md#resourcemanager_errorcode) 0 - The operation is successful.

[ERROR\_CODE\_INVALID\_INPUT\_PARAMETER](../resmgr-common-h/document.md#resourcemanager_errorcode) 401 - The input parameter is invalid. Possible causes: 1. The parameter type is incorrect. 2. Parameter verification failed.

[ERROR\_CODE\_RES\_NAME\_NOT\_FOUND](../resmgr-common-h/document.md#resourcemanager_errorcode) 9001003 - The resource name is invalid.

[ERROR\_CODE\_RES\_NOT\_FOUND\_BY\_NAME](../resmgr-common-h/document.md#resourcemanager_errorcode) 9001004 - No matching resource is found based on the resource name.

[ERROR\_CODE\_RES\_REF\_TOO\_MUCH](../resmgr-common-h/document.md#resourcemanager_errorcode) 9001006 - The resource is cyclically referenced.

[ERROR\_CODE\_OUT\_OF\_MEMORY](../resmgr-common-h/document.md#resourcemanager_errorcode) 9001100 - A memory overflow occurs.

 |

#### \[h2\]OH\_ResourceManager\_GetStringArray()

ResourceManager\_ErrorCode OH\_ResourceManager\_GetStringArray(const NativeResourceManager \*mgr, uint32\_t resId, char \*\*\*resultValue, uint32\_t \*resultLen)

**Description**

Obtains a string array based on the specified resource ID. After using this API, you need to call **OH\_ResourceManager\_ReleaseStringArray()** to release the memory of the string array.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [const NativeResourceManager](../../structs/nativeresourcemanager/document.md) \*mgr | Pointer to [NativeResourceManager](../../structs/nativeresourcemanager/document.md). It is obtained by using [OH\_ResourceManager\_InitNativeResourceManager](../raw-file-manager-h/document.md#oh_resourcemanager_initnativeresourcemanager). |
| uint32\_t resId | Resource ID. |
| char \*\*\*resultValue | Result of writing **resultValue**. |
| uint32\_t \*resultLen | Length of **StringArray** written to **resultLen**. |

**Returns**

| Type | Description |
| :-- | :-- |
| [ResourceManager\_ErrorCode](../resmgr-common-h/document.md#resourcemanager_errorcode) | 
[SUCCESS](../resmgr-common-h/document.md#resourcemanager_errorcode) 0 - The operation is successful.

[ERROR\_CODE\_INVALID\_INPUT\_PARAMETER](../resmgr-common-h/document.md#resourcemanager_errorcode) 401 - The input parameter is invalid. Possible causes: 1. The parameter type is incorrect. 2. Parameter verification failed.

[ERROR\_CODE\_RES\_ID\_NOT\_FOUND](../resmgr-common-h/document.md#resourcemanager_errorcode) 9001001 - The resource ID is invalid.

[ERROR\_CODE\_RES\_NOT\_FOUND\_BY\_ID](../resmgr-common-h/document.md#resourcemanager_errorcode) 9001002 - No matching resource is found based on the resource ID.

[ERROR\_CODE\_RES\_REF\_TOO\_MUCH](../resmgr-common-h/document.md#resourcemanager_errorcode) 9001006 - The resource is cyclically referenced.

[ERROR\_CODE\_OUT\_OF\_MEMORY](../resmgr-common-h/document.md#resourcemanager_errorcode) 9001100 - A memory overflow occurs.

 |

#### \[h2\]OH\_ResourceManager\_GetStringArrayByName()

ResourceManager\_ErrorCode OH\_ResourceManager\_GetStringArrayByName(const NativeResourceManager \*mgr, const char \*resName, char \*\*\*resultValue, uint32\_t \*resultLen)

**Description**

Obtains a string array based on the specified resource name. After using this API, you need to call **OH\_ResourceManager\_ReleaseStringArray()** to release the memory of the string array.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [const NativeResourceManager](../../structs/nativeresourcemanager/document.md) \*mgr | Pointer to [NativeResourceManager](../../structs/nativeresourcemanager/document.md). It is obtained by using [OH\_ResourceManager\_InitNativeResourceManager](../raw-file-manager-h/document.md#oh_resourcemanager_initnativeresourcemanager). |
| const char \*resName | Resource name. |
| char \*\*\*resultValue | Result of writing **resultValue**. |
| uint32\_t \*resultLen | Length of **StringArray** written to **resultLen**. |

**Returns**

| Type | Description |
| :-- | :-- |
| [ResourceManager\_ErrorCode](../resmgr-common-h/document.md#resourcemanager_errorcode) | 
[SUCCESS](../resmgr-common-h/document.md#resourcemanager_errorcode) 0 - The operation is successful.

[ERROR\_CODE\_INVALID\_INPUT\_PARAMETER](../resmgr-common-h/document.md#resourcemanager_errorcode) 401 - The input parameter is invalid. Possible causes: 1. The parameter type is incorrect. 2. Parameter verification failed.

[ERROR\_CODE\_RES\_NAME\_NOT\_FOUND](../resmgr-common-h/document.md#resourcemanager_errorcode) 9001003 - The resource name is invalid.

[ERROR\_CODE\_RES\_NOT\_FOUND\_BY\_NAME](../resmgr-common-h/document.md#resourcemanager_errorcode) 9001004 - No matching resource is found based on the resource name.

[ERROR\_CODE\_RES\_REF\_TOO\_MUCH](../resmgr-common-h/document.md#resourcemanager_errorcode) 9001006 - The resource is cyclically referenced.

[ERROR\_CODE\_OUT\_OF\_MEMORY](../resmgr-common-h/document.md#resourcemanager_errorcode) 9001100 - A memory overflow occurs.

 |

#### \[h2\]OH\_ResourceManager\_ReleaseStringArray()

ResourceManager\_ErrorCode OH\_ResourceManager\_ReleaseStringArray(char \*\*\*resValue, uint32\_t len)

**Description**

Releases the memory of the string array.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| char \*\*\*resValue | String array whose memory needs to be released. |
| uint32\_t len | Length of the string array. |

**Returns**

| Type | Description |
| :-- | :-- |
| [ResourceManager\_ErrorCode](../resmgr-common-h/document.md#resourcemanager_errorcode) | 
[SUCCESS](../resmgr-common-h/document.md#resourcemanager_errorcode) 0 - The operation is successful.

[ERROR\_CODE\_INVALID\_INPUT\_PARAMETER](../resmgr-common-h/document.md#resourcemanager_errorcode) 401 - The input parameter is invalid. Possible causes: 1. The parameter type is incorrect. 2. Parameter verification failed.

 |

#### \[h2\]OH\_ResourceManager\_GetPluralString()

ResourceManager\_ErrorCode OH\_ResourceManager\_GetPluralString(const NativeResourceManager \*mgr, uint32\_t resId, uint32\_t num, char \*\*resultValue)

**Description**

Obtains singular and plural strings based on the specified resource ID. After using this API, you need to call **free()** to release the memory of the strings.

**Since**: 12

**Deprecated from**: 18

**Substitute**: [OH\_ResourceManager\_GetIntPluralString](#oh_resourcemanager_getintpluralstring)

**Parameters**

| Name | Description |
| :-- | :-- |
| [const NativeResourceManager](../../structs/nativeresourcemanager/document.md) \*mgr | Pointer to [NativeResourceManager](../../structs/nativeresourcemanager/document.md). It is obtained by using [OH\_ResourceManager\_InitNativeResourceManager](../raw-file-manager-h/document.md#oh_resourcemanager_initnativeresourcemanager). |
| uint32\_t resId | Resource ID. |
| uint32\_t num | Number. |
| char \*\*resultValue | Result of writing **resultValue**. |

**Returns**

| Type | Description |
| :-- | :-- |
| [ResourceManager\_ErrorCode](../resmgr-common-h/document.md#resourcemanager_errorcode) | 
[SUCCESS](../resmgr-common-h/document.md#resourcemanager_errorcode) 0 - The operation is successful.

[ERROR\_CODE\_INVALID\_INPUT\_PARAMETER](../resmgr-common-h/document.md#resourcemanager_errorcode) 401 - The input parameter is invalid. Possible causes: 1. The parameter type is incorrect. 2. Parameter verification failed.

[ERROR\_CODE\_RES\_ID\_NOT\_FOUND](../resmgr-common-h/document.md#resourcemanager_errorcode) 9001001 - The resource ID is invalid.

[ERROR\_CODE\_RES\_NOT\_FOUND\_BY\_ID](../resmgr-common-h/document.md#resourcemanager_errorcode) 9001002 - No matching resource is found based on the resource ID.

[ERROR\_CODE\_RES\_REF\_TOO\_MUCH](../resmgr-common-h/document.md#resourcemanager_errorcode) 9001006 - The resource is cyclically referenced.

[ERROR\_CODE\_OUT\_OF\_MEMORY](../resmgr-common-h/document.md#resourcemanager_errorcode) 9001100 - A memory overflow occurs.

 |

#### \[h2\]OH\_ResourceManager\_GetPluralStringByName()

ResourceManager\_ErrorCode OH\_ResourceManager\_GetPluralStringByName(const NativeResourceManager \*mgr, const char \*resName, uint32\_t num, char \*\*resultValue)

**Description**

Obtains singular and plural strings based on the specified resource name. After using this API, you need to call **free()** to release the memory of the strings.

**Since**: 12

**Deprecated from**: 18

**Substitute**: [OH\_ResourceManager\_GetIntPluralStringByName](#oh_resourcemanager_getintpluralstringbyname)

**Parameters**

| Name | Description |
| :-- | :-- |
| [const NativeResourceManager](../../structs/nativeresourcemanager/document.md) \*mgr | Pointer to [NativeResourceManager](../../structs/nativeresourcemanager/document.md). It is obtained by using [OH\_ResourceManager\_InitNativeResourceManager](../raw-file-manager-h/document.md#oh_resourcemanager_initnativeresourcemanager). |
| const char \*resName | Resource name. |
| uint32\_t num | Number. |
| char \*\*resultValue | Result of writing **resultValue**. |

**Returns**

| Type | Description |
| :-- | :-- |
| [ResourceManager\_ErrorCode](../resmgr-common-h/document.md#resourcemanager_errorcode) | 
[SUCCESS](../resmgr-common-h/document.md#resourcemanager_errorcode) 0 - The operation is successful.

[ERROR\_CODE\_INVALID\_INPUT\_PARAMETER](../resmgr-common-h/document.md#resourcemanager_errorcode) 401 - The input parameter is invalid. Possible causes: 1. The parameter type is incorrect. 2. Parameter verification failed.

[ERROR\_CODE\_RES\_NAME\_NOT\_FOUND](../resmgr-common-h/document.md#resourcemanager_errorcode) 9001003 - The resource name is invalid.

[ERROR\_CODE\_RES\_NOT\_FOUND\_BY\_NAME](../resmgr-common-h/document.md#resourcemanager_errorcode) 9001004 - No matching resource is found based on the resource name.

[ERROR\_CODE\_RES\_REF\_TOO\_MUCH](../resmgr-common-h/document.md#resourcemanager_errorcode) 9001006 - The resource is cyclically referenced.

[ERROR\_CODE\_OUT\_OF\_MEMORY](../resmgr-common-h/document.md#resourcemanager_errorcode) 9001100 - A memory overflow occurs.

 |

#### \[h2\]OH\_ResourceManager\_GetIntPluralString()

ResourceManager\_ErrorCode OH\_ResourceManager\_GetIntPluralString(const NativeResourceManager \*mgr, uint32\_t resId, uint32\_t num, char \*\*resultValue, ...)

**Description**

Obtains singular and plural strings based on the specified resource ID. After using this API, you need to call **free()** to release the memory of the strings.

**Since**: 18

**Parameters**

| Name | Description |
| :-- | :-- |
| [const NativeResourceManager](../../structs/nativeresourcemanager/document.md) \*mgr | Pointer to [NativeResourceManager](../../structs/nativeresourcemanager/document.md). It is obtained by using [OH\_ResourceManager\_InitNativeResourceManager](../raw-file-manager-h/document.md#oh_resourcemanager_initnativeresourcemanager). |
| uint32\_t resId | Resource ID. |
| uint32\_t num | Quantity value (an integer number). Its string representation is obtained based on the current language's plural rules. |
| char \*\*resultValue | Result of writing **resultValue**. |
| ... | Variable representing formatted string resources. Supported types include const char\*, int, and float. |

**Returns**

| Type | Description |
| :-- | :-- |
| [ResourceManager\_ErrorCode](../resmgr-common-h/document.md#resourcemanager_errorcode) | 
[SUCCESS](../resmgr-common-h/document.md#resourcemanager_errorcode) 0 - The operation is successful.

[ERROR\_CODE\_INVALID\_INPUT\_PARAMETER](../resmgr-common-h/document.md#resourcemanager_errorcode) 401 - The input parameter is invalid. Possible causes: 1. The parameter type is incorrect. 2. Parameter verification failed.

[ERROR\_CODE\_RES\_ID\_NOT\_FOUND](../resmgr-common-h/document.md#resourcemanager_errorcode) 9001001 - The resource ID is invalid.

[ERROR\_CODE\_RES\_NOT\_FOUND\_BY\_ID](../resmgr-common-h/document.md#resourcemanager_errorcode) 9001002 - No matching resource is found based on the resource ID.

[ERROR\_CODE\_RES\_REF\_TOO\_MUCH](../resmgr-common-h/document.md#resourcemanager_errorcode) 9001006 - The resource is cyclically referenced.

[ERROR\_CODE\_OUT\_OF\_MEMORY](../resmgr-common-h/document.md#resourcemanager_errorcode) 9001100 - A memory overflow occurs.

 |

#### \[h2\]OH\_ResourceManager\_GetDoublePluralString()

ResourceManager\_ErrorCode OH\_ResourceManager\_GetDoublePluralString(const NativeResourceManager \*mgr, uint32\_t resId, double num, char \*\*resultValue, ...)

**Description**

Obtains singular and plural strings based on the specified resource ID. After using this API, you need to call **free()** to release the memory of the strings.

**Since**: 18

**Parameters**

| Name | Description |
| :-- | :-- |
| [const NativeResourceManager](../../structs/nativeresourcemanager/document.md) \*mgr | Pointer to [NativeResourceManager](../../structs/nativeresourcemanager/document.md). It is obtained by using [OH\_ResourceManager\_InitNativeResourceManager](../raw-file-manager-h/document.md#oh_resourcemanager_initnativeresourcemanager). |
| uint32\_t resId | Resource ID. |
| double num | Quantity value (a floating point number). Its string representation is obtained based on the current language's plural rules. |
| char \*\*resultValue | Result of writing **resultValue**. |
| ... | Variable representing formatted string resources. Supported types include const char\*, int, and float. |

**Returns**

| Type | Description |
| :-- | :-- |
| [ResourceManager\_ErrorCode](../resmgr-common-h/document.md#resourcemanager_errorcode) | 
[SUCCESS](../resmgr-common-h/document.md#resourcemanager_errorcode) 0 - The operation is successful.

[ERROR\_CODE\_INVALID\_INPUT\_PARAMETER](../resmgr-common-h/document.md#resourcemanager_errorcode) 401 - The input parameter is invalid. Possible causes: 1. The parameter type is incorrect. 2. Parameter verification failed.

[ERROR\_CODE\_RES\_ID\_NOT\_FOUND](../resmgr-common-h/document.md#resourcemanager_errorcode) 9001001 - The resource ID is invalid.

[ERROR\_CODE\_RES\_NOT\_FOUND\_BY\_ID](../resmgr-common-h/document.md#resourcemanager_errorcode) 9001002 - No matching resource is found based on the resource ID.

[ERROR\_CODE\_RES\_REF\_TOO\_MUCH](../resmgr-common-h/document.md#resourcemanager_errorcode) 9001006 - The resource is cyclically referenced.

[ERROR\_CODE\_OUT\_OF\_MEMORY](../resmgr-common-h/document.md#resourcemanager_errorcode) 9001100 - A memory overflow occurs.

 |

#### \[h2\]OH\_ResourceManager\_GetIntPluralStringByName()

ResourceManager\_ErrorCode OH\_ResourceManager\_GetIntPluralStringByName(const NativeResourceManager \*mgr, const char \*resName, uint32\_t num, char \*\*resultValue, ...)

**Description**

Obtains singular and plural strings based on the specified resource name. After using this API, you need to call **free()** to release the memory of the strings.

**Since**: 18

**Parameters**

| Name | Description |
| :-- | :-- |
| [const NativeResourceManager](../../structs/nativeresourcemanager/document.md) \*mgr | Pointer to [NativeResourceManager](../../structs/nativeresourcemanager/document.md). It is obtained by using [OH\_ResourceManager\_InitNativeResourceManager](../raw-file-manager-h/document.md#oh_resourcemanager_initnativeresourcemanager). |
| const char \*resName | Resource name. |
| uint32\_t num | Quantity value (an integer number). Its string representation is obtained based on the current language's plural rules. |
| char \*\*resultValue | Result of writing **resultValue**. |
| ... | Variable representing formatted string resources. Supported types include const char\*, int, and float. |

**Returns**

| Type | Description |
| :-- | :-- |
| [ResourceManager\_ErrorCode](../resmgr-common-h/document.md#resourcemanager_errorcode) | 
[SUCCESS](../resmgr-common-h/document.md#resourcemanager_errorcode) 0 - The operation is successful.

[ERROR\_CODE\_INVALID\_INPUT\_PARAMETER](../resmgr-common-h/document.md#resourcemanager_errorcode) 401 - The input parameter is invalid. Possible causes: 1. The parameter type is incorrect. 2. Parameter verification failed.

[ERROR\_CODE\_RES\_NAME\_NOT\_FOUND](../resmgr-common-h/document.md#resourcemanager_errorcode) 9001003 - The resource name is invalid.

[ERROR\_CODE\_RES\_NOT\_FOUND\_BY\_NAME](../resmgr-common-h/document.md#resourcemanager_errorcode) 9001004 - No matching resource is found based on the resource name.

[ERROR\_CODE\_RES\_REF\_TOO\_MUCH](../resmgr-common-h/document.md#resourcemanager_errorcode) 9001006 - The resource is cyclically referenced.

[ERROR\_CODE\_OUT\_OF\_MEMORY](../resmgr-common-h/document.md#resourcemanager_errorcode) 9001100 - A memory overflow occurs.

 |

#### \[h2\]OH\_ResourceManager\_GetDoublePluralStringByName()

ResourceManager\_ErrorCode OH\_ResourceManager\_GetDoublePluralStringByName(const NativeResourceManager \*mgr, const char \*resName, double num, char \*\*resultValue, ...)

**Description**

Obtains singular and plural strings based on the specified resource name. After using this API, you need to call **free()** to release the memory of the strings.

**Since**: 18

**Parameters**

| Name | Description |
| :-- | :-- |
| [const NativeResourceManager](../../structs/nativeresourcemanager/document.md) \*mgr | Pointer to [NativeResourceManager](../../structs/nativeresourcemanager/document.md). It is obtained by using [OH\_ResourceManager\_InitNativeResourceManager](../raw-file-manager-h/document.md#oh_resourcemanager_initnativeresourcemanager). |
| const char \*resName | Resource name. |
| double num | Quantity value (a floating point number). Its string representation is obtained based on the current language's plural rules. |
| char \*\*resultValue | Result of writing **resultValue**. |
| ... | Variable representing formatted string resources. Supported types include const char\*, int, and float. |

**Returns**

| Type | Description |
| :-- | :-- |
| [ResourceManager\_ErrorCode](../resmgr-common-h/document.md#resourcemanager_errorcode) | 
[SUCCESS](../resmgr-common-h/document.md#resourcemanager_errorcode) 0 - The operation is successful.

[ERROR\_CODE\_INVALID\_INPUT\_PARAMETER](../resmgr-common-h/document.md#resourcemanager_errorcode) 401 - The input parameter is invalid. Possible causes: 1. The parameter type is incorrect. 2. Parameter verification failed.

[ERROR\_CODE\_RES\_NAME\_NOT\_FOUND](../resmgr-common-h/document.md#resourcemanager_errorcode) 9001003 - The resource name is invalid.

[ERROR\_CODE\_RES\_NOT\_FOUND\_BY\_NAME](../resmgr-common-h/document.md#resourcemanager_errorcode) 9001004 - No matching resource is found based on the resource name.

[ERROR\_CODE\_RES\_REF\_TOO\_MUCH](../resmgr-common-h/document.md#resourcemanager_errorcode) 9001006 - The resource is cyclically referenced.

[ERROR\_CODE\_OUT\_OF\_MEMORY](../resmgr-common-h/document.md#resourcemanager_errorcode) 9001100 - A memory overflow occurs.

 |

#### \[h2\]OH\_ResourceManager\_GetColor()

ResourceManager\_ErrorCode OH\_ResourceManager\_GetColor(const NativeResourceManager \*mgr, uint32\_t resId, uint32\_t \*resultValue)

**Description**

Obtains a color value based on the specified resource ID.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [const NativeResourceManager](../../structs/nativeresourcemanager/document.md) \*mgr | Pointer to [NativeResourceManager](../../structs/nativeresourcemanager/document.md). It is obtained by using [OH\_ResourceManager\_InitNativeResourceManager](../raw-file-manager-h/document.md#oh_resourcemanager_initnativeresourcemanager). |
| uint32\_t resId | Resource ID. |
| uint32\_t \*resultValue | Result of writing **resultValue**. |

**Returns**

| Type | Description |
| :-- | :-- |
| [ResourceManager\_ErrorCode](../resmgr-common-h/document.md#resourcemanager_errorcode) | 
[SUCCESS](../resmgr-common-h/document.md#resourcemanager_errorcode) 0 - The operation is successful.

[ERROR\_CODE\_INVALID\_INPUT\_PARAMETER](../resmgr-common-h/document.md#resourcemanager_errorcode) 401 - The input parameter is invalid. Possible causes: 1. The parameter type is incorrect. 2. Parameter verification failed.

[ERROR\_CODE\_RES\_ID\_NOT\_FOUND](../resmgr-common-h/document.md#resourcemanager_errorcode) 9001001 - The resource ID is invalid.

[ERROR\_CODE\_RES\_NOT\_FOUND\_BY\_ID](../resmgr-common-h/document.md#resourcemanager_errorcode) 9001002 - No matching resource is found based on the resource ID.

[ERROR\_CODE\_RES\_REF\_TOO\_MUCH](../resmgr-common-h/document.md#resourcemanager_errorcode) 9001006 - The resource is cyclically referenced.

 |

#### \[h2\]OH\_ResourceManager\_GetColorByName()

ResourceManager\_ErrorCode OH\_ResourceManager\_GetColorByName(const NativeResourceManager \*mgr, const char \*resName, uint32\_t \*resultValue)

**Description**

Obtains a color value based on the specified resource ID.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [const NativeResourceManager](../../structs/nativeresourcemanager/document.md) \*mgr | Pointer to [NativeResourceManager](../../structs/nativeresourcemanager/document.md). It is obtained by using [OH\_ResourceManager\_InitNativeResourceManager](../raw-file-manager-h/document.md#oh_resourcemanager_initnativeresourcemanager). |
| const char \*resName | Resource name. |
| uint32\_t \*resultValue | Result of writing **resultValue**. |

**Returns**

| Type | Description |
| :-- | :-- |
| [ResourceManager\_ErrorCode](../resmgr-common-h/document.md#resourcemanager_errorcode) | 
[SUCCESS](../resmgr-common-h/document.md#resourcemanager_errorcode) 0 - The operation is successful.

[ERROR\_CODE\_INVALID\_INPUT\_PARAMETER](../resmgr-common-h/document.md#resourcemanager_errorcode) 401 - The input parameter is invalid. Possible causes: 1. The parameter type is incorrect. 2. Parameter verification failed.

[ERROR\_CODE\_RES\_NAME\_NOT\_FOUND](../resmgr-common-h/document.md#resourcemanager_errorcode) 9001003 - The resource name is invalid.

[ERROR\_CODE\_RES\_NOT\_FOUND\_BY\_NAME](../resmgr-common-h/document.md#resourcemanager_errorcode) 9001004 - No matching resource is found based on the resource name.

[ERROR\_CODE\_RES\_REF\_TOO\_MUCH](../resmgr-common-h/document.md#resourcemanager_errorcode) 9001006 - The resource is cyclically referenced.

 |

#### \[h2\]OH\_ResourceManager\_GetInt()

ResourceManager\_ErrorCode OH\_ResourceManager\_GetInt(const NativeResourceManager \*mgr, uint32\_t resId, int \*resultValue)

**Description**

Obtains an int value based on the specified resource ID.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [const NativeResourceManager](../../structs/nativeresourcemanager/document.md) \*mgr | Pointer to [NativeResourceManager](../../structs/nativeresourcemanager/document.md). It is obtained by using [OH\_ResourceManager\_InitNativeResourceManager](../raw-file-manager-h/document.md#oh_resourcemanager_initnativeresourcemanager). |
| uint32\_t resId | Resource ID. |
| int \*resultValue | Result of writing **resultValue**. |

**Returns**

| Type | Description |
| :-- | :-- |
| [ResourceManager\_ErrorCode](../resmgr-common-h/document.md#resourcemanager_errorcode) | 
[SUCCESS](../resmgr-common-h/document.md#resourcemanager_errorcode) 0 - The operation is successful.

[ERROR\_CODE\_INVALID\_INPUT\_PARAMETER](../resmgr-common-h/document.md#resourcemanager_errorcode) 401 - The input parameter is invalid. Possible causes: 1. The parameter type is incorrect. 2. Parameter verification failed.

[ERROR\_CODE\_RES\_ID\_NOT\_FOUND](../resmgr-common-h/document.md#resourcemanager_errorcode) 9001001 - The resource ID is invalid.

[ERROR\_CODE\_RES\_NOT\_FOUND\_BY\_ID](../resmgr-common-h/document.md#resourcemanager_errorcode) 9001002 - No matching resource is found based on the resource ID.

[ERROR\_CODE\_RES\_REF\_TOO\_MUCH](../resmgr-common-h/document.md#resourcemanager_errorcode) 9001006 - The resource is cyclically referenced.

 |

#### \[h2\]OH\_ResourceManager\_GetIntByName()

ResourceManager\_ErrorCode OH\_ResourceManager\_GetIntByName(const NativeResourceManager \*mgr, const char \*resName, int \*resultValue)

**Description**

Obtains an int value based on the specified resource name.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [const NativeResourceManager](../../structs/nativeresourcemanager/document.md) \*mgr | Pointer to [NativeResourceManager](../../structs/nativeresourcemanager/document.md). It is obtained by using [OH\_ResourceManager\_InitNativeResourceManager](../raw-file-manager-h/document.md#oh_resourcemanager_initnativeresourcemanager). |
| const char \*resName | Resource name. |
| int \*resultValue | Result of writing **resultValue**. |

**Returns**

| Type | Description |
| :-- | :-- |
| [ResourceManager\_ErrorCode](../resmgr-common-h/document.md#resourcemanager_errorcode) | 
[SUCCESS](../resmgr-common-h/document.md#resourcemanager_errorcode) 0 - The operation is successful.

[ERROR\_CODE\_INVALID\_INPUT\_PARAMETER](../resmgr-common-h/document.md#resourcemanager_errorcode) 401 - The input parameter is invalid. Possible causes: 1. The parameter type is incorrect. 2. Parameter verification failed.

[ERROR\_CODE\_RES\_NAME\_NOT\_FOUND](../resmgr-common-h/document.md#resourcemanager_errorcode) 9001003 - The resource name is invalid.

[ERROR\_CODE\_RES\_NOT\_FOUND\_BY\_NAME](../resmgr-common-h/document.md#resourcemanager_errorcode) 9001004 - No matching resource is found based on the resource name.

[ERROR\_CODE\_RES\_REF\_TOO\_MUCH](../resmgr-common-h/document.md#resourcemanager_errorcode) 9001006 - The resource is cyclically referenced.

 |

#### \[h2\]OH\_ResourceManager\_GetFloat()

ResourceManager\_ErrorCode OH\_ResourceManager\_GetFloat(const NativeResourceManager \*mgr, uint32\_t resId, float \*resultValue)

**Description**

Obtains a float value based on the specified resource ID.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [const NativeResourceManager](../../structs/nativeresourcemanager/document.md) \*mgr | Pointer to [NativeResourceManager](../../structs/nativeresourcemanager/document.md). It is obtained by using [OH\_ResourceManager\_InitNativeResourceManager](../raw-file-manager-h/document.md#oh_resourcemanager_initnativeresourcemanager). |
| uint32\_t resId | Resource ID. |
| float \*resultValue | Result of writing **resultValue**. |

**Returns**

| Type | Description |
| :-- | :-- |
| [ResourceManager\_ErrorCode](../resmgr-common-h/document.md#resourcemanager_errorcode) | 
[SUCCESS](../resmgr-common-h/document.md#resourcemanager_errorcode) 0 - The operation is successful.

[ERROR\_CODE\_INVALID\_INPUT\_PARAMETER](../resmgr-common-h/document.md#resourcemanager_errorcode) 401 - The input parameter is invalid. Possible causes: 1. The parameter type is incorrect. 2. Parameter verification failed.

[ERROR\_CODE\_RES\_ID\_NOT\_FOUND](../resmgr-common-h/document.md#resourcemanager_errorcode) 9001001 - The resource ID is invalid.

[ERROR\_CODE\_RES\_NOT\_FOUND\_BY\_ID](../resmgr-common-h/document.md#resourcemanager_errorcode) 9001002 - No matching resource is found based on the resource ID.

[ERROR\_CODE\_RES\_REF\_TOO\_MUCH](../resmgr-common-h/document.md#resourcemanager_errorcode) 9001006 - The resource is cyclically referenced.

 |

#### \[h2\]OH\_ResourceManager\_GetFloatByName()

ResourceManager\_ErrorCode OH\_ResourceManager\_GetFloatByName(const NativeResourceManager \*mgr, const char \*resName, float \*resultValue)

**Description**

Obtains a float value based on the specified resource name.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [const NativeResourceManager](../../structs/nativeresourcemanager/document.md) \*mgr | Pointer to [NativeResourceManager](../../structs/nativeresourcemanager/document.md). It is obtained by using [OH\_ResourceManager\_InitNativeResourceManager](../raw-file-manager-h/document.md#oh_resourcemanager_initnativeresourcemanager). |
| const char \*resName | Resource name. |
| float \*resultValue | Result of writing **resultValue**. |

**Returns**

| Type | Description |
| :-- | :-- |
| [ResourceManager\_ErrorCode](../resmgr-common-h/document.md#resourcemanager_errorcode) | 
[SUCCESS](../resmgr-common-h/document.md#resourcemanager_errorcode) 0 - The operation is successful.

[ERROR\_CODE\_INVALID\_INPUT\_PARAMETER](../resmgr-common-h/document.md#resourcemanager_errorcode) 401 - The input parameter is invalid. Possible causes: 1. The parameter type is incorrect. 2. Parameter verification failed.

[ERROR\_CODE\_RES\_NAME\_NOT\_FOUND](../resmgr-common-h/document.md#resourcemanager_errorcode) 9001003 - The resource name is invalid.

[ERROR\_CODE\_RES\_NOT\_FOUND\_BY\_NAME](../resmgr-common-h/document.md#resourcemanager_errorcode) 9001004 - No matching resource is found based on the resource name.

[ERROR\_CODE\_RES\_REF\_TOO\_MUCH](../resmgr-common-h/document.md#resourcemanager_errorcode) 9001006 - The resource is cyclically referenced.

 |

#### \[h2\]OH\_ResourceManager\_GetBool()

ResourceManager\_ErrorCode OH\_ResourceManager\_GetBool(const NativeResourceManager \*mgr, uint32\_t resId, bool \*resultValue)

**Description**

Obtains a bool value based on the specified resource ID.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [const NativeResourceManager](../../structs/nativeresourcemanager/document.md) \*mgr | Pointer to [NativeResourceManager](../../structs/nativeresourcemanager/document.md). It is obtained by using [OH\_ResourceManager\_InitNativeResourceManager](../raw-file-manager-h/document.md#oh_resourcemanager_initnativeresourcemanager). |
| uint32\_t resId | Resource ID. |
| bool \*resultValue | Result of writing **resultValue**. |

**Returns**

| Type | Description |
| :-- | :-- |
| [ResourceManager\_ErrorCode](../resmgr-common-h/document.md#resourcemanager_errorcode) | 
[SUCCESS](../resmgr-common-h/document.md#resourcemanager_errorcode) 0 - The operation is successful.

[ERROR\_CODE\_INVALID\_INPUT\_PARAMETER](../resmgr-common-h/document.md#resourcemanager_errorcode) 401 - The input parameter is invalid. Possible causes: 1. The parameter type is incorrect. 2. Parameter verification failed.

[ERROR\_CODE\_RES\_ID\_NOT\_FOUND](../resmgr-common-h/document.md#resourcemanager_errorcode) 9001001 - The resource ID is invalid.

[ERROR\_CODE\_RES\_NOT\_FOUND\_BY\_ID](../resmgr-common-h/document.md#resourcemanager_errorcode) 9001002 - No matching resource is found based on the resource ID.

[ERROR\_CODE\_RES\_REF\_TOO\_MUCH](../resmgr-common-h/document.md#resourcemanager_errorcode) 9001006 - The resource is cyclically referenced.

 |

#### \[h2\]OH\_ResourceManager\_GetBoolByName()

ResourceManager\_ErrorCode OH\_ResourceManager\_GetBoolByName(const NativeResourceManager \*mgr, const char \*resName, bool \*resultValue)

**Description**

Obtains a bool value based on the specified resource name.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [const NativeResourceManager](../../structs/nativeresourcemanager/document.md) \*mgr | Pointer to [NativeResourceManager](../../structs/nativeresourcemanager/document.md). It is obtained by using [OH\_ResourceManager\_InitNativeResourceManager](../raw-file-manager-h/document.md#oh_resourcemanager_initnativeresourcemanager). |
| const char \*resName | Resource name. |
| bool \*resultValue | Result of writing **resultValue**. |

**Returns**

| Type | Description |
| :-- | :-- |
| [ResourceManager\_ErrorCode](../resmgr-common-h/document.md#resourcemanager_errorcode) | 
[SUCCESS](../resmgr-common-h/document.md#resourcemanager_errorcode) 0 - The operation is successful.

[ERROR\_CODE\_INVALID\_INPUT\_PARAMETER](../resmgr-common-h/document.md#resourcemanager_errorcode) 401 - The input parameter is invalid. Possible causes: 1. The parameter type is incorrect. 2. Parameter verification failed.

[ERROR\_CODE\_RES\_NAME\_NOT\_FOUND](../resmgr-common-h/document.md#resourcemanager_errorcode) 9001003 - The resource name is invalid.

[ERROR\_CODE\_RES\_NOT\_FOUND\_BY\_NAME](../resmgr-common-h/document.md#resourcemanager_errorcode) 9001004 - No matching resource is found based on the resource name.

[ERROR\_CODE\_RES\_REF\_TOO\_MUCH](../resmgr-common-h/document.md#resourcemanager_errorcode) 9001006 - The resource is cyclically referenced.

 |

#### \[h2\]OH\_ResourceManager\_AddResource()

ResourceManager\_ErrorCode OH\_ResourceManager\_AddResource(const NativeResourceManager \*mgr, const char \*path)

**Description**

Adds overlay resources when an application is running.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [const NativeResourceManager](../../structs/nativeresourcemanager/document.md) \*mgr | Pointer to [NativeResourceManager](../../structs/nativeresourcemanager/document.md). It is obtained by using [OH\_ResourceManager\_InitNativeResourceManager](../raw-file-manager-h/document.md#oh_resourcemanager_initnativeresourcemanager). |
| const char \*path | Resource path. |

**Returns**

| Type | Description |
| :-- | :-- |
| [ResourceManager\_ErrorCode](../resmgr-common-h/document.md#resourcemanager_errorcode) | 
[SUCCESS](../resmgr-common-h/document.md#resourcemanager_errorcode) 0 - The operation is successful.

[ERROR\_CODE\_INVALID\_INPUT\_PARAMETER](../resmgr-common-h/document.md#resourcemanager_errorcode) 401 - The input parameter is invalid. Possible causes: 1. The parameter type is incorrect. 2. Parameter verification failed.

[ERROR\_CODE\_OVERLAY\_RES\_PATH\_INVALID](../resmgr-common-h/document.md#resourcemanager_errorcode) 9001010 - The resource path is invalid.

 |

#### \[h2\]OH\_ResourceManager\_RemoveResource()

ResourceManager\_ErrorCode OH\_ResourceManager\_RemoveResource(const NativeResourceManager \*mgr, const char \*path)

**Description**

Removes overlay resources when an application is running.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [const NativeResourceManager](../../structs/nativeresourcemanager/document.md) \*mgr | Pointer to [NativeResourceManager](../../structs/nativeresourcemanager/document.md). It is obtained by using [OH\_ResourceManager\_InitNativeResourceManager](../raw-file-manager-h/document.md#oh_resourcemanager_initnativeresourcemanager). |
| const char \*path | Resource path. |

**Returns**

| Type | Description |
| :-- | :-- |
| [ResourceManager\_ErrorCode](../resmgr-common-h/document.md#resourcemanager_errorcode) | 
[SUCCESS](../resmgr-common-h/document.md#resourcemanager_errorcode) 0 - The operation is successful.

[ERROR\_CODE\_INVALID\_INPUT\_PARAMETER](../resmgr-common-h/document.md#resourcemanager_errorcode) 401 - The input parameter is invalid. Possible causes: 1. The parameter type is incorrect. 2. Parameter verification failed.

[ERROR\_CODE\_OVERLAY\_RES\_PATH\_INVALID](../resmgr-common-h/document.md#resourcemanager_errorcode) 9001010 - The resource path is invalid.

 |
