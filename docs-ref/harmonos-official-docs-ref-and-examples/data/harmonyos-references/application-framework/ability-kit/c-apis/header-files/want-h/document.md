# want.h

#### Overview

Want is a carrier for information transfer between objects (application components). Want can be used as a parameter of **startAbility** to specify a startup target and information that needs to be carried during startup, for example, **bundleName** and **abilityName**, which respectively indicate the bundle name of the target ability and the ability name in the bundle. When ability A needs to start ability B and transfer some data to ability B, it can use Want a carrier to transfer the data.

**File to include**: <AbilityKit/ability\_base/want.h>

**Library**: libability\_base\_want.so

**System capability**: SystemCapability.Ability.AbilityBase

**Since**: 15

**Related module**: [AbilityBase](../../modules/abilitybase/document.md)

#### Summary

#### \[h2\]Structs

| Name | typedef Keyword | Description |
| :-- | :-- | :-- |
| [AbilityBase\_Element](../../structs/abilitybase-element/document.md) | AbilityBase\_Element | Declares the Element struct in Want. |
| [AbilityBase\_Want](../../structs/abilitybase-want/document.md) | AbilityBase\_Want | Declares the struct of Want data. |

#### \[h2\]Functions

| Name | Description |
| :-- | :-- |
| [AbilityBase\_Want\* OH\_AbilityBase\_CreateWant(AbilityBase\_Element element)](#oh_abilitybase_createwant) | Creates Want. |
| [AbilityBase\_ErrorCode OH\_AbilityBase\_DestroyWant(AbilityBase\_Want\* want)](#oh_abilitybase_destroywant) | Destroys Want. Want cannot be used after being destroyed. Otherwise, undefined behavior may occur. |
| [AbilityBase\_ErrorCode OH\_AbilityBase\_SetWantElement(AbilityBase\_Want\* want, AbilityBase\_Element element)](#oh_abilitybase_setwantelement) | Sets the Element struct, which consists of **bundleName**, **moduleName**, and **abilityName** in Want. |
| [AbilityBase\_ErrorCode OH\_AbilityBase\_GetWantElement(AbilityBase\_Want\* want, AbilityBase\_Element\* element)](#oh_abilitybase_getwantelement) | Obtains the Element struct, which consists of **bundleName**, **moduleName**, and **abilityName** in Want. |
| [AbilityBase\_ErrorCode OH\_AbilityBase\_SetWantCharParam(AbilityBase\_Want\* want, const char\* key, const char\* value)](#oh_abilitybase_setwantcharparam) | Sets **Param** in Want. |
| [AbilityBase\_ErrorCode OH\_AbilityBase\_GetWantCharParam(AbilityBase\_Want\* want, const char\* key,char\* value, size\_t valueSize)](#oh_abilitybase_getwantcharparam) | Obtains **Param** in Want. |
| [AbilityBase\_ErrorCode OH\_AbilityBase\_AddWantFd(AbilityBase\_Want\* want, const char\* key, int32\_t fd)](#oh_abilitybase_addwantfd) | Adds a Want file descriptor. |
| [AbilityBase\_ErrorCode OH\_AbilityBase\_GetWantFd(AbilityBase\_Want\* want, const char\* key, int32\_t\* fd)](#oh_abilitybase_getwantfd) | Obtains a Want file descriptor. |
| [AbilityBase\_ErrorCode OH\_AbilityBase\_SetWantUri(AbilityBase\_Want\* want, const char\* uri)](#oh_abilitybase_setwanturi) | Sets **uri** in Want. |
| [AbilityBase\_ErrorCode OH\_AbilityBase\_GetWantUri(AbilityBase\_Want\* want, char\* uri, size\_t uriSize)](#oh_abilitybase_getwanturi) | Obtains **uri** set in Want. For details about the URI, see [uri in Want](../../../arkts-apis/both-models-recommended/ohos-app-ability-want-want/document.md). |
| [AbilityBase\_ErrorCode OH\_AbilityBase\_SetWantInt32Param(AbilityBase\_Want\* want, const char\* key, int32\_t value)](#oh_abilitybase_setwantint32param) | Sets a value of the int32\_t type in Want. |
| [AbilityBase\_ErrorCode OH\_AbilityBase\_GetWantInt32Param(AbilityBase\_Want\* want, const char\* key, int32\_t\* value)](#oh_abilitybase_getwantint32param) | Obtains a value of the int32\_t type set in Want. |
| [AbilityBase\_ErrorCode OH\_AbilityBase\_SetWantBoolParam(AbilityBase\_Want\* want, const char\* key, bool value)](#oh_abilitybase_setwantboolparam) | Sets a value of the bool type in Want. |
| [AbilityBase\_ErrorCode OH\_AbilityBase\_GetWantBoolParam(AbilityBase\_Want\* want, const char\* key, bool\* value)](#oh_abilitybase_getwantboolparam) | Obtains a value of the bool type set in Want. |
| [AbilityBase\_ErrorCode OH\_AbilityBase\_SetWantDoubleParam(AbilityBase\_Want\* want, const char\* key, double value)](#oh_abilitybase_setwantdoubleparam) | Sets a value of the double type in Want. |
| [AbilityBase\_ErrorCode OH\_AbilityBase\_GetWantDoubleParam(AbilityBase\_Want\* want, const char\* key, double\* value)](#oh_abilitybase_getwantdoubleparam) | Obtains a value of the double type set in Want. |

#### Function Description

#### \[h2\]OH\_AbilityBase\_CreateWant()

AbilityBase\_Want\* OH\_AbilityBase\_CreateWant(AbilityBase\_Element element)

**Description**

Creates Want.

**Since**: 15

**Parameters**

| Name | Description |
| :-- | :-- |
| [AbilityBase\_Element](../../structs/abilitybase-element/document.md) element | Element struct. |

**Returns**

| Type | Description |
| :-- | :-- |
| [AbilityBase\_Want](../../structs/abilitybase-want/document.md)\* | Pointer to Want. |

#### \[h2\]OH\_AbilityBase\_DestroyWant()

AbilityBase\_ErrorCode OH\_AbilityBase\_DestroyWant(AbilityBase\_Want\* want)

**Description**

Destroys Want. Want cannot be used after being destroyed. Otherwise, undefined behavior may occur.

**Since**: 15

**Parameters**

| Name | Description |
| :-- | :-- |
| [AbilityBase\_Want](../../structs/abilitybase-want/document.md)\* want | Pointer to Want. |

**Returns**

| Type | Description |
| :-- | :-- |
| [AbilityBase\_ErrorCode](../ability-base-common-h/document.md#abilitybase_errorcode) | 
One of the following execution results:

**ABILITY\_BASE\_ERROR\_CODE\_NO\_ERROR**: Want is destroyed.

**ABILITY\_BASE\_ERROR\_CODE\_PARAM\_INVALID**: **element** is invalid.

 |

#### \[h2\]OH\_AbilityBase\_SetWantElement()

AbilityBase\_ErrorCode OH\_AbilityBase\_SetWantElement(AbilityBase\_Want\* want, AbilityBase\_Element element)

**Description**

Sets the Element struct, which consists of **bundleName**, **moduleName**, and **abilityName** in Want.

**Since**: 15

**Parameters**

| Name | Description |
| :-- | :-- |
| [AbilityBase\_Want](../../structs/abilitybase-want/document.md)\* want | Pointer to Want. |
| [AbilityBase\_Element](../../structs/abilitybase-element/document.md) element | Element struct. |

**Returns**

| Type | Description |
| :-- | :-- |
| [AbilityBase\_ErrorCode](../ability-base-common-h/document.md#abilitybase_errorcode) | 
One of the following execution results:

**ABILITY\_BASE\_ERROR\_CODE\_NO\_ERROR**: The setting is successful.

**ABILITY\_BASE\_ERROR\_CODE\_PARAM\_INVALID**: **want** is null or **element** is invalid.

 |

#### \[h2\]OH\_AbilityBase\_GetWantElement()

AbilityBase\_ErrorCode OH\_AbilityBase\_GetWantElement(AbilityBase\_Want\* want, AbilityBase\_Element\* element)

**Description**

Obtains the Element struct, which consists of **bundleName**, **moduleName**, and **abilityName** in Want.

**Since**: 15

**Parameters**

| Name | Description |
| :-- | :-- |
| [AbilityBase\_Want](../../structs/abilitybase-want/document.md)\* want | Pointer to Want. |
| [AbilityBase\_Element](../../structs/abilitybase-element/document.md)\* element | Pointer to the Element struct. |

**Returns**

| Type | Description |
| :-- | :-- |
| [AbilityBase\_ErrorCode](../ability-base-common-h/document.md#abilitybase_errorcode) | 
One of the following execution results:

**ABILITY\_BASE\_ERROR\_CODE\_NO\_ERROR**: The element struct is obtained.

**ABILITY\_BASE\_ERROR\_CODE\_PARAM\_INVALID**: **want** is null or **element** is invalid.

 |

#### \[h2\]OH\_AbilityBase\_SetWantCharParam()

AbilityBase\_ErrorCode OH\_AbilityBase\_SetWantCharParam(AbilityBase\_Want\* want, const char\* key, const char\* value)

**Description**

Sets **Param** in Want. For details about **Param**, see [parameters in Want](../../../arkts-apis/apis-no-longer-maintained/ability/want/document.md).

**Since**: 15

**Parameters**

| Name | Description |
| :-- | :-- |
| [AbilityBase\_Want](../../structs/abilitybase-want/document.md)\* want | Pointer to Want. |
| const char\* key | Pointer to a key in Want. |
| const char\* value | Pointer to the value of the key in Want. |

**Returns**

| Type | Description |
| :-- | :-- |
| [AbilityBase\_ErrorCode](../ability-base-common-h/document.md#abilitybase_errorcode) | 
One of the following execution results:

**ABILITY\_BASE\_ERROR\_CODE\_NO\_ERROR**: The setting is successful.

**ABILITY\_BASE\_ERROR\_CODE\_PARAM\_INVALID**: **want** is null or invalid.

 |

#### \[h2\]OH\_AbilityBase\_GetWantCharParam()

AbilityBase\_ErrorCode OH\_AbilityBase\_GetWantCharParam(AbilityBase\_Want\* want, const char\* key,char\* value, size\_t valueSize)

**Description**

Obtains **Param** set by [OH\_AbilityBase\_SetWantCharParam](#oh_abilitybase_setwantcharparam) in Want.

**Since**: 15

**Parameters**

| Name | Description |
| :-- | :-- |
| [AbilityBase\_Want](../../structs/abilitybase-want/document.md)\* want | Pointer to Want. |
| const char\* key | Pointer to a key in Want. |
| char\* value | Pointer to the value of the key in Want. |
| size\_t valueSize | Length of the value string. If **valueSize** is less than the actual value length, the [ABILITY\_BASE\_ERROR\_CODE\_PARAM\_INVALID](../ability-base-common-h/document.md#abilitybase_errorcode) error is reported. |

**Returns**

| Type | Description |
| :-- | :-- |
| [AbilityBase\_ErrorCode](../ability-base-common-h/document.md#abilitybase_errorcode) | 
One of the following execution results:

**ABILITY\_BASE\_ERROR\_CODE\_NO\_ERROR**: The param struct is obtained.

**ABILITY\_BASE\_ERROR\_CODE\_PARAM\_INVALID**: **want** is null or invalid.

 |

#### \[h2\]OH\_AbilityBase\_AddWantFd()

AbilityBase\_ErrorCode OH\_AbilityBase\_AddWantFd(AbilityBase\_Want\* want, const char\* key, int32\_t fd)

**Description**

Adds a Want file descriptor. The file descriptor can be obtained through [fs.open](../../../../core-file-kit/arkts-apis/ohos-file-fs-file-management/document.md#fsopen).

**Since**: 15

**Parameters**

| Name | Description |
| :-- | :-- |
| [AbilityBase\_Want](../../structs/abilitybase-want/document.md)\* want | Pointer to Want. |
| const char\* key | Pointer to a key in Want. |
| int32\_t fd | File descriptor, which is obtained by calling [fs.open](../../../../core-file-kit/arkts-apis/ohos-file-fs-file-management/document.md#fsopen). |

**Returns**

| Type | Description |
| :-- | :-- |
| [AbilityBase\_ErrorCode](../ability-base-common-h/document.md#abilitybase_errorcode) | 
One of the following execution results:

**ABILITY\_BASE\_ERROR\_CODE\_NO\_ERROR**: The Want file descriptor is added.

**ABILITY\_BASE\_ERROR\_CODE\_PARAM\_INVALID**: **want** is null or invalid.

 |

#### \[h2\]OH\_AbilityBase\_GetWantFd()

AbilityBase\_ErrorCode OH\_AbilityBase\_GetWantFd(AbilityBase\_Want\* want, const char\* key, int32\_t\* fd)

**Description**

Obtains a Want file descriptor.

**Since**: 15

**Parameters**

| Name | Description |
| :-- | :-- |
| [AbilityBase\_Want](../../structs/abilitybase-want/document.md)\* want | Pointer to Want. |
| const char\* key | Pointer to a key in Want. |
| int32\_t\* fd | Pointer to the file descriptor. |

**Returns**

| Type | Description |
| :-- | :-- |
| [AbilityBase\_ErrorCode](../ability-base-common-h/document.md#abilitybase_errorcode) | 
One of the following execution results:

**ABILITY\_BASE\_ERROR\_CODE\_NO\_ERROR**: The Want file descriptor is obtained.

**ABILITY\_BASE\_ERROR\_CODE\_PARAM\_INVALID**: **want** is null or invalid.

 |

#### \[h2\]OH\_AbilityBase\_SetWantUri()

AbilityBase\_ErrorCode OH\_AbilityBase\_SetWantUri(AbilityBase\_Want\* want, const char\* uri)

**Description**

Sets **uri** in Want. For details about the URI, see [uri in Want](../../../arkts-apis/both-models-recommended/ohos-app-ability-want-want/document.md).

**Since**: 17

**Parameters**

| Name | Description |
| :-- | :-- |
| [AbilityBase\_Want](../../structs/abilitybase-want/document.md)\* want | Pointer to Want. |
| const char\* uri | Pointer to a URI. If a URI is specified in Want, Want will match the specified URI information. For details about the URI, see [uri in Want](../../../arkts-apis/both-models-recommended/ohos-app-ability-want-want/document.md). |

**Returns**

| Type | Description |
| :-- | :-- |
| [AbilityBase\_ErrorCode](../ability-base-common-h/document.md#abilitybase_errorcode) | 
One of the following execution results:

**ABILITY\_BASE\_ERROR\_CODE\_NO\_ERROR**: The setting is successful.

**ABILITY\_BASE\_ERROR\_CODE\_PARAM\_INVALID**: **want** is null or invalid.

 |

#### \[h2\]OH\_AbilityBase\_GetWantUri()

AbilityBase\_ErrorCode OH\_AbilityBase\_GetWantUri(AbilityBase\_Want\* want, char\* uri, size\_t uriSize)

**Description**

Obtains **uri** set in Want. For details about the URI, see [uri in Want](../../../arkts-apis/both-models-recommended/ohos-app-ability-want-want/document.md).

**Since**: 17

**Parameters**

| Name | Description |
| :-- | :-- |
| [AbilityBase\_Want](../../structs/abilitybase-want/document.md)\* want | Pointer to Want. |
| char\* uri | Pointer to a URI. If a URI is specified in Want, Want will match the specified URI information. For details about the URI, see [uri in Want](../../../arkts-apis/both-models-recommended/ohos-app-ability-want-want/document.md). |
| size\_t uriSize | Length of the URI string. If **uriSize** is less than the actual URI length, the [ABILITY\_BASE\_ERROR\_CODE\_PARAM\_INVALID](../ability-base-common-h/document.md#abilitybase_errorcode) error is reported. |

**Returns**

| Type | Description |
| :-- | :-- |
| [AbilityBase\_ErrorCode](../ability-base-common-h/document.md#abilitybase_errorcode) | 
One of the following execution results:

**ABILITY\_BASE\_ERROR\_CODE\_NO\_ERROR**: The URI string in Want is obtained.

**ABILITY\_BASE\_ERROR\_CODE\_PARAM\_INVALID**: **want** is null or invalid.

 |

#### \[h2\]OH\_AbilityBase\_SetWantInt32Param()

AbilityBase\_ErrorCode OH\_AbilityBase\_SetWantInt32Param(AbilityBase\_Want\* want, const char\* key, int32\_t value)

**Description**

Sets a value of the int32\_t type in Want.

**Since**: 17

**Parameters**

| Name | Description |
| :-- | :-- |
| [AbilityBase\_Want](../../structs/abilitybase-want/document.md)\* want | Pointer to Want. |
| const char\* key | Pointer to a key in Want. |
| int32\_t value | Value of the int32\_t type of the key. |

**Returns**

| Type | Description |
| :-- | :-- |
| [AbilityBase\_ErrorCode](../ability-base-common-h/document.md#abilitybase_errorcode) | 
One of the following execution results:

**ABILITY\_BASE\_ERROR\_CODE\_NO\_ERROR**: The setting is successful.

**ABILITY\_BASE\_ERROR\_CODE\_PARAM\_INVALID**: **want** is null or invalid.

 |

#### \[h2\]OH\_AbilityBase\_GetWantInt32Param()

AbilityBase\_ErrorCode OH\_AbilityBase\_GetWantInt32Param(AbilityBase\_Want\* want, const char\* key, int32\_t\* value)

**Description**

Obtains a value of the int32\_t type set in Want.

**Since**: 17

**Parameters**

| Name | Description |
| :-- | :-- |
| [AbilityBase\_Want](../../structs/abilitybase-want/document.md)\* want | Pointer to Want. |
| const char\* key | Pointer to a key in Want. |
| int32\_t\* value | Pointer to the value of the int32\_t type of the key. |

**Returns**

| Type | Description |
| :-- | :-- |
| [AbilityBase\_ErrorCode](../ability-base-common-h/document.md#abilitybase_errorcode) | 
One of the following execution results:

**ABILITY\_BASE\_ERROR\_CODE\_NO\_ERROR**: The value of the int32\_t type is obtained.

**ABILITY\_BASE\_ERROR\_CODE\_PARAM\_INVALID**: **want** is null or invalid.

 |

#### \[h2\]OH\_AbilityBase\_SetWantBoolParam()

AbilityBase\_ErrorCode OH\_AbilityBase\_SetWantBoolParam(AbilityBase\_Want\* want, const char\* key, bool value)

**Description**

Sets a value of the bool type in Want.

**Since**: 17

**Parameters**

| Name | Description |
| :-- | :-- |
| [AbilityBase\_Want](../../structs/abilitybase-want/document.md)\* want | Pointer to Want. |
| const char\* key | Pointer to a key in Want. |
| bool value | Value of the bool type of the key. |

**Returns**

| Type | Description |
| :-- | :-- |
| [AbilityBase\_ErrorCode](../ability-base-common-h/document.md#abilitybase_errorcode) | 
One of the following execution results:

**ABILITY\_BASE\_ERROR\_CODE\_NO\_ERROR**: The setting is successful.

**ABILITY\_BASE\_ERROR\_CODE\_PARAM\_INVALID**: **want** is null or invalid.

 |

#### \[h2\]OH\_AbilityBase\_GetWantBoolParam()

AbilityBase\_ErrorCode OH\_AbilityBase\_GetWantBoolParam(AbilityBase\_Want\* want, const char\* key, bool\* value)

**Description**

Obtains a value of the bool type set in Want.

**Since**: 17

**Parameters**

| Name | Description |
| :-- | :-- |
| [AbilityBase\_Want](../../structs/abilitybase-want/document.md)\* want | Pointer to Want. |
| const char\* key | Pointer to a key in Want. |
| bool\* value | Pointer to the value of the bool type of the key. |

**Returns**

| Type | Description |
| :-- | :-- |
| [AbilityBase\_ErrorCode](../ability-base-common-h/document.md#abilitybase_errorcode) | 
One of the following execution results:

**ABILITY\_BASE\_ERROR\_CODE\_NO\_ERROR**: The value of the bool type is obtained.

**ABILITY\_BASE\_ERROR\_CODE\_PARAM\_INVALID**: **want** is null or invalid.

 |

#### \[h2\]OH\_AbilityBase\_SetWantDoubleParam()

AbilityBase\_ErrorCode OH\_AbilityBase\_SetWantDoubleParam(AbilityBase\_Want\* want, const char\* key, double value)

**Description**

Sets a value of the double type in Want.

**Since**: 17

**Parameters**

| Name | Description |
| :-- | :-- |
| [AbilityBase\_Want](../../structs/abilitybase-want/document.md)\* want | Pointer to Want. |
| const char\* key | Pointer to a key in Want. |
| double value | Value of the double type of the key. |

**Returns**

| Type | Description |
| :-- | :-- |
| [AbilityBase\_ErrorCode](../ability-base-common-h/document.md#abilitybase_errorcode) | 
One of the following execution results:

**ABILITY\_BASE\_ERROR\_CODE\_NO\_ERROR**: The setting is successful.

**ABILITY\_BASE\_ERROR\_CODE\_PARAM\_INVALID**: **want** is null or invalid.

 |

#### \[h2\]OH\_AbilityBase\_GetWantDoubleParam()

AbilityBase\_ErrorCode OH\_AbilityBase\_GetWantDoubleParam(AbilityBase\_Want\* want, const char\* key, double\* value)

**Description**

Obtains a value of the double type set in Want.

**Since**: 17

**Parameters**

| Name | Description |
| :-- | :-- |
| [AbilityBase\_Want](../../structs/abilitybase-want/document.md)\* want | Pointer to Want. |
| const char\* key | Pointer to a key in Want. |
| double\* value | Pointer to the value of the double type of the key. |

**Returns**

| Type | Description |
| :-- | :-- |
| [AbilityBase\_ErrorCode](../ability-base-common-h/document.md#abilitybase_errorcode) | 
One of the following execution results:

**ABILITY\_BASE\_ERROR\_CODE\_NO\_ERROR**: The value of the double type is obtained.

**ABILITY\_BASE\_ERROR\_CODE\_PARAM\_INVALID**: **want** is null or invalid.

 |
