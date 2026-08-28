# oh\_predicates.h

#### Overview

Defines the predicates for an RDB store.

**File to include**: <database/rdb/oh\_predicates.h>

**Library**: libnative\_rdb\_ndk.z.so

**System capability**: SystemCapability.DistributedDataManager.RelationalStore.Core

**Since**: 10

**Related module**: [RDB](../../modules/rdb/document.md)

#### Summary

#### \[h2\]Structs

| Name | typedef Keyword | Description |
| :-- | :-- | :-- |
| [OH\_Predicates](../../structs/oh-predicates/document.md) | OH\_Predicates | Defines a **predicates** object. |

#### \[h2\]Enums

| Name | typedef Keyword | Description |
| :-- | :-- | :-- |
| [OH\_OrderType](#oh_ordertype) | OH\_OrderType | Enumerates the sorting types. |

#### \[h2\]Functions

| Name | Description |
| :-- | :-- |
| [int OH\_Predicates\_NotLike(OH\_Predicates \*predicates, const char \*field, const char \*pattern)](#oh_predicates_notlike) | 
Sets an **OH\_Predicates** object to match a string that is not similar to the specified value.

This API is similar to the SQL **Not like** statement.

 |
| [int OH\_Predicates\_Glob(OH\_Predicates \*predicates, const char \*field, const char \*pattern)](#oh_predicates_glob) | 

Sets an **OH\_Predicates** object to match a string containing a wildcard.

Different from **like**, the input parameters of this API are case-sensitive.

 |
| [int OH\_Predicates\_NotGlob(OH\_Predicates \*predicates, const char \*field, const char \*pattern)](#oh_predicates_notglob) | 

Sets an **OH\_Predicates** object to not match a string containing a wildcard.

Different from **Not Like**, the input parameters of this API are case-sensitive.

 |
| [int OH\_Predicates\_Having(OH\_Predicates \*predicates, const char \*conditions, const OH\_Data\_Values \*values)](#oh_predicates_having) | Sets an **OH\_Predicates** object to filter grouped results by specified conditions. |

#### Enum Description

#### \[h2\]OH\_OrderType

enum OH\_OrderType

**Description**

Enumerates the sorting types.

**Since**: 10

| Enum Item | Description |
| :-- | :-- |
| ASC = 0 | Ascending order. |
| DESC = 1 | Descending order. |

#### Function Description

#### \[h2\]OH\_Predicates\_NotLike()

int OH\_Predicates\_NotLike(OH\_Predicates \*predicates, const char \*field, const char \*pattern)

**Description**

Sets an **OH\_Predicates** object to match a string that is not similar to the specified value.

This API is similar to the SQL **Not like** statement.

**Since**: 20

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Predicates](../../structs/oh-predicates/document.md) \*predicates | Pointer to the [OH\_Predicates](../../structs/oh-predicates/document.md) instance. |
| const char \*field | Pointer to the column name in the database table. |
| const char \*pattern | Pointer to the pattern used. |

**Returns**

| Type | Description |
| :-- | :-- |
| int | 
Returns an execution result.

**RDB\_OK** indicates that the execution is successful.

**RDB\_E\_INVALID\_ARGS** indicates that invalid parameters are specified.

 |

#### \[h2\]OH\_Predicates\_Glob()

int OH\_Predicates\_Glob(OH\_Predicates \*predicates, const char \*field, const char \*pattern)

**Description**

Sets an **OH\_Predicates** object to match a string containing a wildcard.

Different from **like**, the input parameters of this API are case-sensitive.

**Since**: 20

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Predicates](../../structs/oh-predicates/document.md) \*predicates | Pointer to the [OH\_Predicates](../../structs/oh-predicates/document.md) instance. |
| const char \*field | Pointer to the column name in the database table. |
| const char \*pattern | Pointer to the pattern used. |

**Returns**

| Type | Description |
| :-- | :-- |
| int | 
Returns an execution result.

**RDB\_OK** indicates that the execution is successful.

**RDB\_E\_INVALID\_ARGS** indicates that invalid parameters are specified.

 |

#### \[h2\]OH\_Predicates\_NotGlob()

int OH\_Predicates\_NotGlob(OH\_Predicates \*predicates, const char \*field, const char \*pattern)

**Description**

Sets an **OH\_Predicates** object to not match a string containing a wildcard.

Different from **Not Like**, the input parameters of this API are case-sensitive.

**Since**: 20

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Predicates](../../structs/oh-predicates/document.md) \*predicates | Pointer to the [OH\_Predicates](../../structs/oh-predicates/document.md) instance. |
| const char \*field | Pointer to the column name in the database table. |
| const char \*pattern | Pointer to the pattern used. |

**Returns**

| Type | Description |
| :-- | :-- |
| int | 
Returns an execution result.

**RDB\_OK** indicates that the execution is successful.

**RDB\_E\_INVALID\_ARGS** indicates that invalid parameters are specified.

 |

#### \[h2\]OH\_Predicates\_Having()

int OH\_Predicates\_Having(OH\_Predicates \*predicates, const char \*conditions, const OH\_Data\_Values \*values)

**Description**

Sets an **OH\_Predicates** object to filter grouped results by specified conditions.

**Since**: 20

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Predicates](../../structs/oh-predicates/document.md) \*predicates | Pointer to the [OH\_Predicates](../../structs/oh-predicates/document.md) instance. |
| const char \*conditions | Pointer to the filter condition specified in the HAVING clause. |
| const [OH\_Data\_Values](../../structs/oh-data-values/document.md) \*values | Pointer to the [OH\_Data\_Values](../../structs/oh-data-values/document.md) instance. |

**Returns**

| Type | Description |
| :-- | :-- |
| int | 
Returns an execution result.

**RDB\_OK** indicates that the execution is successful.

**RDB\_E\_INVALID\_ARGS** indicates that invalid parameters are specified.

 |
