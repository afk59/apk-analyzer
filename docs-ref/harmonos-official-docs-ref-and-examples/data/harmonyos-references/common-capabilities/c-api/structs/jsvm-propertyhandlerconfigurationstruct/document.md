# JSVM\_PropertyHandlerConfigurationStruct

typedef struct {...} JSVM\_PropertyHandlerConfigurationStruct

#### Overview

Defines a struct for triggering the corresponding callback when the getter, setter, deleter, or enumerator of an object is executed.

**Since**: 12

**Related module**: [JSVM](../../modules/jsvm/document.md)

**Header file**: [jsvm\_types.h](../../header-files/jsvm-types-h/document.md)

#### Summary

#### \[h2\]Member Variables

| Name | Description |
| :-- | :-- |
| [JSVM\_Value](../jsvm-value/document.md) namedPropertyData | Data used for name property callback. |
| [JSVM\_Value](../jsvm-value/document.md) indexedPropertyData | Data used for index property callback. |

#### \[h2\]Member Functions

| Name | Description |
| :-- | :-- |
| [JSVM\_Value (JSVM\_CDECL\* genericNamedPropertyGetterCallback)(JSVM\_Env env,JSVM\_Value name,JSVM\_Value thisArg,JSVM\_Value namedPropertyData)](#genericnamedpropertygettercallback) | Callback triggered by obtaining the name property of an instance object. |
| [JSVM\_Value (JSVM\_CDECL\* genericNamedPropertySetterCallback)(JSVM\_Env env,JSVM\_Value name,JSVM\_Value property,JSVM\_Value thisArg,JSVM\_Value namedPropertyData)](#genericnamedpropertysettercallback) | Callback triggered by setting the name property of an instance object. |
| [JSVM\_Value (JSVM\_CDECL\* genericNamedPropertyDeleterCallback)(JSVM\_Env env,JSVM\_Value name,JSVM\_Value thisArg,JSVM\_Value namedPropertyData)](#genericnamedpropertydeletercallback) | Callback triggered by deleting the name property of an instance object. |
| [JSVM\_Value (JSVM\_CDECL\* genericNamedPropertyEnumeratorCallback)(JSVM\_Env env,JSVM\_Value thisArg,JSVM\_Value namedPropertyData)](#genericnamedpropertyenumeratorcallback) | Callback triggered by obtaining all name properties of an object. |
| [JSVM\_Value (JSVM\_CDECL\* genericIndexedPropertyGetterCallback)(JSVM\_Env env,JSVM\_Value index,JSVM\_Value thisArg,JSVM\_Value indexedPropertyData)](#genericindexedpropertygettercallback) | Callback triggered by obtaining the index property of an instance object. |
| [JSVM\_Value (JSVM\_CDECL\* genericIndexedPropertySetterCallback)(JSVM\_Env env,JSVM\_Value index,JSVM\_Value property,JSVM\_Value thisArg,JSVM\_Value indexedPropertyData)](#genericindexedpropertysettercallback) | Callback triggered by setting the index property of an instance object. |
| [JSVM\_Value (JSVM\_CDECL\* genericIndexedPropertyDeleterCallback)(JSVM\_Env env,JSVM\_Value index,JSVM\_Value thisArg,JSVM\_Value indexedPropertyData)](#genericindexedpropertydeletercallback) | Callback triggered by deleting the index property of an instance object. |
| [JSVM\_Value (JSVM\_CDECL\* genericIndexedPropertyEnumeratorCallback)(JSVM\_Env env,JSVM\_Value thisArg,JSVM\_Value indexedPropertyData)](#genericindexedpropertyenumeratorcallback) | Callback triggered by obtaining all index properties of an object. |

#### Member Function Description

#### \[h2\]genericNamedPropertyGetterCallback()

JSVM\_Value (JSVM\_CDECL\* genericNamedPropertyGetterCallback)(JSVM\_Env env,JSVM\_Value name,JSVM\_Value thisArg,JSVM\_Value namedPropertyData)

**Description**

Callback triggered by obtaining the name property of an instance object.

#### \[h2\]genericNamedPropertySetterCallback()

JSVM\_Value (JSVM\_CDECL\* genericNamedPropertySetterCallback)(JSVM\_Env env,JSVM\_Value name,JSVM\_Value property,JSVM\_Value thisArg,JSVM\_Value namedPropertyData)

**Description**

Callback triggered by setting the name property of an instance object.

#### \[h2\]genericNamedPropertyDeleterCallback()

JSVM\_Value (JSVM\_CDECL\* genericNamedPropertyDeleterCallback)(JSVM\_Env env,JSVM\_Value name,JSVM\_Value thisArg,JSVM\_Value namedPropertyData)

**Description**

Callback triggered by deleting the name property of an instance object.

#### \[h2\]genericNamedPropertyEnumeratorCallback()

JSVM\_Value (JSVM\_CDECL\* genericNamedPropertyEnumeratorCallback)(JSVM\_Env env,JSVM\_Value thisArg,JSVM\_Value namedPropertyData)

**Description**

Callback triggered by obtaining all name properties on an object.

#### \[h2\]genericIndexedPropertyGetterCallback()

JSVM\_Value (JSVM\_CDECL\* genericIndexedPropertyGetterCallback)(JSVM\_Env env,JSVM\_Value index,JSVM\_Value thisArg,JSVM\_Value indexedPropertyData)

**Description**

Callback triggered by obtaining the index property of an instance object.

#### \[h2\]genericIndexedPropertySetterCallback()

JSVM\_Value (JSVM\_CDECL\* genericIndexedPropertySetterCallback)(JSVM\_Env env,JSVM\_Value index,JSVM\_Value property,JSVM\_Value thisArg,JSVM\_Value indexedPropertyData)

**Description**

Callback triggered by setting the index property of an instance object.

#### \[h2\]genericIndexedPropertyDeleterCallback()

JSVM\_Value (JSVM\_CDECL\* genericIndexedPropertyDeleterCallback)(JSVM\_Env env,JSVM\_Value index,JSVM\_Value thisArg,JSVM\_Value indexedPropertyData)

**Description**

Callback triggered by deleting the index property of an instance object.

#### \[h2\]genericIndexedPropertyEnumeratorCallback()

JSVM\_Value (JSVM\_CDECL\* genericIndexedPropertyEnumeratorCallback)(JSVM\_Env env,JSVM\_Value thisArg,JSVM\_Value indexedPropertyData)

**Description**

Callback triggered by obtaining all index properties on an object.
