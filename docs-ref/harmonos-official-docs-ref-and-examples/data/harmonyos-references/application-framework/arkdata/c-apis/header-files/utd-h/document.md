# utd.h

#### Overview

Defines APIs and structs related to the Uniform Type Descriptors (UTDs).

**File to include**: <database/udmf/utd.h>

**Library**: libudmf.so

**System capability**: SystemCapability.DistributedDataManager.UDMF.Core

**Since**: 12

**Related module**: [UDMF](../../modules/udmf/document.md)

#### Summary

#### \[h2\]Structs

| Name | typedef Keyword | Description |
| :-- | :-- | :-- |
| [OH\_Utd](../../structs/oh-utd/document.md) | OH\_Utd | Defines a struct for a UTD. |

#### \[h2\]Functions

| Name | Description |
| :-- | :-- |
| [OH\_Utd\* OH\_Utd\_Create(const char\* typeId)](#oh_utd_create) | Creates an [OH\_Utd](../../structs/oh-utd/document.md) instance and a pointer to it. |
| [void OH\_Utd\_Destroy(OH\_Utd\* pThis)](#oh_utd_destroy) | Destroys an [OH\_Utd](../../structs/oh-utd/document.md) instance. |
| [const char\* OH\_Utd\_GetTypeId(OH\_Utd\* pThis)](#oh_utd_gettypeid) | Obtains the type ID from an [OH\_Utd](../../structs/oh-utd/document.md) instance. |
| [const char\* OH\_Utd\_GetDescription(OH\_Utd\* pThis)](#oh_utd_getdescription) | Obtains the description from an [OH\_Utd](../../structs/oh-utd/document.md) instance. |
| [const char\* OH\_Utd\_GetReferenceUrl(OH\_Utd\* pThis)](#oh_utd_getreferenceurl) | Obtains the URL from an [OH\_Utd](../../structs/oh-utd/document.md) instance. |
| [const char\* OH\_Utd\_GetIconFile(OH\_Utd\* pThis)](#oh_utd_geticonfile) | Obtains the path of the default icon file from an [OH\_Utd](../../structs/oh-utd/document.md) instance. |
| [const char\*\* OH\_Utd\_GetBelongingToTypes(OH\_Utd\* pThis, unsigned int\* count)](#oh_utd_getbelongingtotypes) | Obtains the relationships between the data from an [OH\_Utd](../../structs/oh-utd/document.md) instance. |
| [const char\*\* OH\_Utd\_GetFilenameExtensions(OH\_Utd\* pThis, unsigned int\* count)](#oh_utd_getfilenameextensions) | Obtains the file name extensions associated with an [OH\_Utd](../../structs/oh-utd/document.md) instance. |
| [const char\*\* OH\_Utd\_GetMimeTypes(OH\_Utd\* pThis, unsigned int\* count)](#oh_utd_getmimetypes) | Obtains the MIME types associated with an [OH\_Utd](../../structs/oh-utd/document.md) instance. |
| [const char\*\* OH\_Utd\_GetTypesByFilenameExtension(const char\* extension, unsigned int\* count)](#oh_utd_gettypesbyfilenameextension) | Obtains the uniform data types based on the file name extensions. |
| [const char\*\* OH\_Utd\_GetTypesByMimeType(const char\* mimeType, unsigned int\* count)](#oh_utd_gettypesbymimetype) | Obtains the uniform data types based on the MIME types. |
| [bool OH\_Utd\_BelongsTo(const char\* srcTypeId, const char\* destTypeId)](#oh_utd_belongsto) | Checks whether a UTD belongs to the target UTD. |
| [bool OH\_Utd\_IsLower(const char\* srcTypeId, const char\* destTypeId)](#oh_utd_islower) | Checks whether a UTD is a lower-level type of the target UTD. For example, **TYPE\_SCRIPT** is a lower-level type of **SOURCE\_CODE**, and **TYPE\_SCRIPT** and **SOURCE\_CODE** are lower-level types of **PLAIN\_TEXT**. |
| [bool OH\_Utd\_IsHigher(const char\* srcTypeId, const char\* destTypeId)](#oh_utd_ishigher) | Checks whether a UTD is a higher-level type of the target UTD. For example, **SOURCE\_CODE** is a higher-level type of **TYPE\_SCRIPT**, and **PLAIN\_TEXT** is a higher-level type of **SOURCE\_CODE** and **TYPE\_SCRIPT**. |
| [bool OH\_Utd\_Equals(OH\_Utd\* utd1, OH\_Utd\* utd2)](#oh_utd_equals) | Checks whether two UTDs are the same. |
| [void OH\_Utd\_DestroyStringList(const char\*\* list, unsigned int count)](#oh_utd_destroystringlist) | Destroys a UTD list. |

#### Function Description

#### \[h2\]OH\_Utd\_Create()

OH\_Utd\* OH\_Utd\_Create(const char\* typeId)

**Description**

Creates an [OH\_Utd](../../structs/oh-utd/document.md) instance and a pointer to it.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| const char\* typeId | Pointer to the type ID of the instance to create. |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_Utd](../../structs/oh-utd/document.md)\* | 
Returns a pointer to the [OH\_Utd](../../structs/oh-utd/document.md) instance created if the operation is successful; returns **nullptr** otherwise.

If this pointer is no longer required, use [OH\_Utd\_Destroy](#oh_utd_destroy) to destroy it. Otherwise, memory leaks may occur.

 |

#### \[h2\]OH\_Utd\_Destroy()

void OH\_Utd\_Destroy(OH\_Utd\* pThis)

**Description**

Destroys an [OH\_Utd](../../structs/oh-utd/document.md) instance.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Utd](../../structs/oh-utd/document.md)\* pThis | Pointer to the [OH\_Utd](../../structs/oh-utd/document.md) instance. |

#### \[h2\]OH\_Utd\_GetTypeId()

const char\* OH\_Utd\_GetTypeId(OH\_Utd\* pThis)

**Description**

Obtains the type ID from an [OH\_Utd](../../structs/oh-utd/document.md) instance.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Utd](../../structs/oh-utd/document.md)\* pThis | Pointer to the [OH\_Utd](../../structs/oh-utd/document.md) instance. |

**Returns**

| Type | Description |
| :-- | :-- |
| const char\* | Returns a pointer to the type ID obtained if the operation is successful; returns **nullptr** otherwise. |

#### \[h2\]OH\_Utd\_GetDescription()

const char\* OH\_Utd\_GetDescription(OH\_Utd\* pThis)

**Description**

Obtains the description from an [OH\_Utd](../../structs/oh-utd/document.md) instance.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Utd](../../structs/oh-utd/document.md)\* pThis | Pointer to the [OH\_Utd](../../structs/oh-utd/document.md) instance. |

**Returns**

| Type | Description |
| :-- | :-- |
| const char\* | Returns a pointer to the description obtained if the operation is successful; returns **nullptr** otherwise. |

#### \[h2\]OH\_Utd\_GetReferenceUrl()

const char\* OH\_Utd\_GetReferenceUrl(OH\_Utd\* pThis)

**Description**

Obtains the URL from an [OH\_Utd](../../structs/oh-utd/document.md) instance.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Utd](../../structs/oh-utd/document.md)\* pThis | Pointer to the [OH\_Utd](../../structs/oh-utd/document.md) instance. |

**Returns**

| Type | Description |
| :-- | :-- |
| const char\* | Returns a pointer to the URL obtained if the operation is successful; returns **nullptr** otherwise. |

#### \[h2\]OH\_Utd\_GetIconFile()

const char\* OH\_Utd\_GetIconFile(OH\_Utd\* pThis)

**Description**

Obtains the path of the default icon file from an [OH\_Utd](../../structs/oh-utd/document.md) instance.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Utd](../../structs/oh-utd/document.md)\* pThis | Pointer to the [OH\_Utd](../../structs/oh-utd/document.md) instance. |

**Returns**

| Type | Description |
| :-- | :-- |
| const char\* | Returns a pointer to the path of the default icon file obtained if the operation is successful; returns **nullptr** otherwise. |

#### \[h2\]OH\_Utd\_GetBelongingToTypes()

const char\*\* OH\_Utd\_GetBelongingToTypes(OH\_Utd\* pThis, unsigned int\* count)

**Description**

Obtains the relationships between the data from an [OH\_Utd](../../structs/oh-utd/document.md) instance.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Utd](../../structs/oh-utd/document.md)\* pThis | Pointer to the [OH\_Utd](../../structs/oh-utd/document.md) instance. |
| unsigned int\* count | Pointer to the number of data types obtained. |

**Returns**

| Type | Description |
| :-- | :-- |
| const char\*\* | Returns a pointer to the relationship information obtained if the operation is successful; returns **nullptr** otherwise. |

#### \[h2\]OH\_Utd\_GetFilenameExtensions()

const char\*\* OH\_Utd\_GetFilenameExtensions(OH\_Utd\* pThis, unsigned int\* count)

**Description**

Obtains the file name extensions associated with an [OH\_Utd](../../structs/oh-utd/document.md) instance.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Utd](../../structs/oh-utd/document.md)\* pThis | Pointer to the [OH\_Utd](../../structs/oh-utd/document.md) instance. |
| unsigned int\* count | Pointer to the number of file name extensions obtained. |

**Returns**

| Type | Description |
| :-- | :-- |
| const char\*\* | Returns a pointer to the file name extensions obtained if the operation is successful; returns **nullptr** otherwise. |

#### \[h2\]OH\_Utd\_GetMimeTypes()

const char\*\* OH\_Utd\_GetMimeTypes(OH\_Utd\* pThis, unsigned int\* count)

**Description**

Obtains the MIME types associated with an [OH\_Utd](../../structs/oh-utd/document.md) instance.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Utd](../../structs/oh-utd/document.md)\* pThis | Pointer to the [OH\_Utd](../../structs/oh-utd/document.md) instance. |
| unsigned int\* count | Pointer to the number of MIME types obtained. |

**Returns**

| Type | Description |
| :-- | :-- |
| const char\*\* | Returns a pointer to the MIME types obtained if the operation is successful; returns **nullptr** otherwise. |

#### \[h2\]OH\_Utd\_GetTypesByFilenameExtension()

const char\*\* OH\_Utd\_GetTypesByFilenameExtension(const char\* extension, unsigned int\* count)

**Description**

Obtains the UTDs based on the file name extensions.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| const char\* extension | Pointer to the file name extensions. |
| unsigned int\* count | Pointer to the number of data types obtained. |

**Returns**

| Type | Description |
| :-- | :-- |
| const char\*\* | 
Returns a pointer to the UTDs obtained.

If it is no longer required, use [OH\_Utd\_DestroyStringList](#oh_utd_destroystringlist) to destroy it. Otherwise, memory leakage occurs.

 |

#### \[h2\]OH\_Utd\_GetTypesByMimeType()

const char\*\* OH\_Utd\_GetTypesByMimeType(const char\* mimeType, unsigned int\* count)

**Description**

Obtains the UTDs based on the MIME types.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| const char\* mimeType | Pointer to the MIME types. |
| unsigned int\* count | Pointer to the number of data types obtained. |

**Returns**

| Type | Description |
| :-- | :-- |
| const char\*\* | 
Returns a double pointer to the UTDs obtained.

If it is no longer required, use [OH\_Utd\_DestroyStringList](#oh_utd_destroystringlist) to destroy it. Otherwise, memory leakage occurs.

 |

#### \[h2\]OH\_Utd\_BelongsTo()

bool OH\_Utd\_BelongsTo(const char\* srcTypeId, const char\* destTypeId)

**Description**

Checks whether a UTD belongs to the target UTD.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| const char\* srcTypeId | Pointer to the UTD to check. |
| const char\* destTypeId | Pointer to the target UTD. |

**Returns**

| Type | Description |
| :-- | :-- |
| bool | Returns **true** if the UTD belongs to the target UTD; returns **false** otherwise. |

#### \[h2\]OH\_Utd\_IsLower()

bool OH\_Utd\_IsLower(const char\* srcTypeId, const char\* destTypeId)

**Description**

Checks whether a UTD is a lower-level type of the target UTD. For example, **TYPE\_SCRIPT** is a lower-level type of **SOURCE\_CODE**, and **TYPE\_SCRIPT** and **SOURCE\_CODE** are lower-level types of **PLAIN\_TEXT**.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| const char\* srcTypeId | Pointer to the UTD to check. |
| const char\* destTypeId | Pointer to the target UTD. |

**Returns**

| Type | Description |
| :-- | :-- |
| bool | Returns **true** if the UTD is a lower-level type of the target UTD; returns **false** otherwise. |

#### \[h2\]OH\_Utd\_IsHigher()

bool OH\_Utd\_IsHigher(const char\* srcTypeId, const char\* destTypeId)

**Description**

Checks whether a UTD is a higher-level type of the target UTD. For example, **SOURCE\_CODE** is a higher-level type of **TYPE\_SCRIPT**, and **PLAIN\_TEXT** is a higher-level type of **SOURCE\_CODE** and **TYPE\_SCRIPT**.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| const char\* srcTypeId | Pointer to the UTD to check. |
| const char\* destTypeId | Pointer to the target UTD. |

**Returns**

| Type | Description |
| :-- | :-- |
| bool | Returns **true** if the UTD is a higher-level type of the target UTD; returns **false** otherwise. |

#### \[h2\]OH\_Utd\_Equals()

bool OH\_Utd\_Equals(OH\_Utd\* utd1, OH\_Utd\* utd2)

**Description**

Checks whether two UTDs are the same.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Utd](../../structs/oh-utd/document.md)\* utd1 | Pointer to an [OH\_Utd](../../structs/oh-utd/document.md) instance. |
| [OH\_Utd](../../structs/oh-utd/document.md)\* utd2 | Pointer to another [OH\_Utd](../../structs/oh-utd/document.md) instance. |

**Returns**

| Type | Description |
| :-- | :-- |
| bool | Returns **true** if the two instances are the same; returns **false** otherwise. |

#### \[h2\]OH\_Utd\_DestroyStringList()

void OH\_Utd\_DestroyStringList(const char\*\* list, unsigned int count)

**Description**

Destroys a UTD list.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| const char\*\* list | Double pointer to the UTD list to destroy. |
| unsigned int count | Length of the UTD list. |
