# OH\_Predicates

typedef struct {...} OH\_Predicates

#### Overview

Defines a **predicates** object.

**Since**: 10

**Related module**: [RDB](../../modules/rdb/document.md)

**Header file**: [oh\_predicates.h](../../header-files/oh-predicates-h/document.md)

#### \[h2\]Member Variables

| Name | Description |
| :-- | :-- |
| int64\_t id | Unique identifier of the **OH\_Predicates** struct. |

#### \[h2\]Member Functions

| Name | Description |
| :-- | :-- |
| [OH\_Predicates \*(\*equalTo)(OH\_Predicates \*predicates, const char \*field, OH\_VObject \*valueObject)](#equalto) | Pointer to the function used to create a predicates object to search for the field values that are equal to the specified value. |
| [OH\_Predicates \*(\*notEqualTo)(OH\_Predicates \*predicates, const char \*field, OH\_VObject \*valueObject)](#notequalto) | 
Pointer to the function used to create a predicates object to search for the field values that are not equal to the specified value.

This method is equivalent to "!=" in SQL statements.

 |
| [OH\_Predicates \*(\*beginWrap)(OH\_Predicates \*predicates)](#beginwrap) | 

Pointer to the function used to add a left parenthesis to the predicates.

This method is equivalent to "(" in SQL statements.

 |
| [OH\_Predicates \*(\*endWrap)(OH\_Predicates \*predicates)](#endwrap) | 

Pointer to the function used to add a right parenthesis to the predicates.

This method is equivalent to ")" in SQL statements.

 |
| [OH\_Predicates \*(\*orOperate)(OH\_Predicates \*predicates)](#oroperate) | 

Pointer to the function used to add the OR operator to the predicates.

This method is equivalent to **OR** in SQL statements.

 |
| [OH\_Predicates \*(\*andOperate)(OH\_Predicates \*predicates)](#andoperate) | 

Pointer to the function used to add the AND operator to the predicates.

This method is equivalent to **AND** in SQL statements.

 |
| [OH\_Predicates \*(\*isNull)(OH\_Predicates \*predicates, const char \*field)](#isnull) | 

Pointer to the function used to create a predicates object to search for the field values that are null.

This method is equivalent to **IS NULL** in SQL statements.

 |
| [OH\_Predicates \*(\*isNotNull)(OH\_Predicates \*predicates, const char \*field)](#isnotnull) | 

Pointer to the function used to create a predicates object to search for the field values that are not null.

This method is equivalent to **IS NOT NULL** in SQL statements.

 |
| [OH\_Predicates \*(\*like)(OH\_Predicates \*predicates, const char \*field, OH\_VObject \*valueObject)](#like) | 

Pointer to the function used to create a predicates object to search for the field values that are similar to the specified string.

This method is equivalent to **LIKE** in SQL statements.

 |
| [OH\_Predicates \*(\*between)(OH\_Predicates \*predicates, const char \*field, OH\_VObject \*valueObject)](#between) | 

Pointer to the function used to create a predicates object to search for the field values that are within the specified range.

This method is equivalent to **BETWEEN** in SQL statements.

 |
| [OH\_Predicates \*(\*notBetween)(OH\_Predicates \*predicates, const char \*field, OH\_VObject \*valueObject)](#notbetween) | 

Pointer to the function used to create a predicates object to search for the field values that are out of the specified range.

This method is equivalent to **NOT BETWEEN** in SQL statements.

 |
| [OH\_Predicates \*(\*greaterThan)(OH\_Predicates \*predicates, const char \*field, OH\_VObject \*valueObject)](#greaterthan) | 

Pointer to the function used to create a predicates object to search for the field values that are greater than the specified value.

This method is equivalent to ">" in SQL statements.

 |
| [OH\_Predicates \*(\*lessThan)(OH\_Predicates \*predicates, const char \*field, OH\_VObject \*valueObject)](#lessthan) | 

Pointer to the function used to create a predicates object to search for the records that are less than the given value in the specified field.

This method is equivalent to "<" in SQL statements.

 |
| [OH\_Predicates \*(\*greaterThanOrEqualTo)(OH\_Predicates \*predicates, const char \*field, OH\_VObject \*valueObject)](#greaterthanorequalto) | 

Pointer to the function used to create a predicates object to search for the field values that are greater than or equal to the specified value.

This method is equivalent to ">=" in SQL statements.

 |
| [OH\_Predicates \*(\*lessThanOrEqualTo)(OH\_Predicates \*predicates, const char \*field, OH\_VObject \*valueObject)](#lessthanorequalto) | 

Pointer to the function used to create a predicates object to search for the records that are less than or equal to the specified **valueObject** in the specified field.

This method is equivalent to "<=" in SQL statements.

 |
| [OH\_Predicates \*(\*orderBy)(OH\_Predicates \*predicates, const char \*field, OH\_OrderType type)](#orderby) | 

Pointer to the function used to create a predicates object to sort the values in the specified column in ascending or descending order.

This method is equivalent to **ORDER BY** in SQL statements.

 |
| [OH\_Predicates \*(\*distinct)(OH\_Predicates \*predicates)](#distinct) | 

Pointer to the function used to create a predicates object to filter out duplicate records.

This method is equivalent to **DISTINCT** in SQL statements.

 |
| [OH\_Predicates \*(\*limit)(OH\_Predicates \*predicates, unsigned int value)](#limit) | 

Pointer to the function used to create a predicates object to specify the maximum number of records.

This method is equivalent to **LIMIT** in SQL statements.

 |
| [OH\_Predicates \*(\*offset)(OH\_Predicates \*predicates, unsigned int rowOffset)](#offset) | 

Pointer to the function used to create a predicates object to specify the start position of the query result.

This method is equivalent to **OFFSET** in SQL statements.

 |
| [OH\_Predicates \*(\*groupBy)(OH\_Predicates \*predicates, char const \*const \*fields, int length)](#groupby) | 

Pointer to the function used to create a predicates object to group the results by the specified columns.

This method is equivalent to **GROUP BY** in SQL statements.

 |
| [OH\_Predicates \*(\*in)(OH\_Predicates \*predicates, const char \*field, OH\_VObject \*valueObject)](#in) | 

Pointer to the function used to create a predicates object to search for the field values that are within the specified range.

This method is equivalent to **IN** in SQL statements.

 |
| [OH\_Predicates \*(\*notIn)(OH\_Predicates \*predicates, const char \*field, OH\_VObject \*valueObject)](#notin) | 

Pointer to the function used to create a predicates object to search for the field values that are out of the specified range.

This method is equivalent to **NOT IN** in SQL statements.

 |
| [OH\_Predicates \*(\*clear)(OH\_Predicates \*predicates)](#clear) | Pointer to the function used to clear a predicates instance. |
| [int (\*destroy)(OH\_Predicates \*predicates)](#destroy) | Destroys an **OH\_Predicates** object and reclaims the memory occupied. |

#### Member Function Description

#### \[h2\]equalTo()

OH\_Predicates \*(\*equalTo)(OH\_Predicates \*predicates, const char \*field, OH\_VObject \*valueObject)

**Description**

Pointer to the function used to create a predicates object to search for the field values that are equal to the specified value.

**Since**: 10

**Parameters**

| Name | Description |
| :-- | :-- |
| OH\_Predicates \*predicates | Pointer to the **OH\_Predicates** instance. |
| const char \*field | Pointer to the column name in the database table. |
| [OH\_VObject](../oh-vobject/document.md) \*valueObject | Pointer to an [OH\_VObject](../oh-vobject/document.md) instance, indicating the value to be matched with the predicate. |

**Returns**

| Type | Description |
| :-- | :-- |
| OH\_Predicates \* | Predicates that match the specified field. |

#### \[h2\]notEqualTo()

OH\_Predicates \*(\*notEqualTo)(OH\_Predicates \*predicates, const char \*field, OH\_VObject \*valueObject)

**Description**

Pointer to the function used to create a predicates object to search for the field values that are not equal to the specified value.

This method is equivalent to "!=" in SQL statements.

**Since**: 10

**Parameters**

| Name | Description |
| :-- | :-- |
| OH\_Predicates \*predicates | Pointer to the **OH\_Predicates** instance. |
| const char \*field | Column name in the database table. |
| [OH\_VObject](../oh-vobject/document.md) \*valueObject | Pointer to an [OH\_VObject](../oh-vobject/document.md) instance, indicating the value to be matched with the predicate. |

**Returns**

| Type | Description |
| :-- | :-- |
| OH\_Predicates \* | Predicates that match the specified field. |

#### \[h2\]beginWrap()

OH\_Predicates \*(\*beginWrap)(OH\_Predicates \*predicates)

**Description**

Pointer to the function used to add a left parenthesis to the predicates.

This method is equivalent to "(" in SQL statements.

**Since**: 10

**Parameters**

| Name | Description |
| :-- | :-- |
| OH\_Predicates \*predicates | Pointer to the **OH\_Predicates** instance. |

**Returns**

| Type | Description |
| :-- | :-- |
| OH\_Predicates \* | Predicates with a left parenthesis. |

#### \[h2\]endWrap()

OH\_Predicates \*(\*endWrap)(OH\_Predicates \*predicates)

**Description**

Pointer to the function used to add a right parenthesis to the predicates.

This method is equivalent to ")" in SQL statements.

**Since**: 10

**Parameters**

| Name | Description |
| :-- | :-- |
| OH\_Predicates \*predicates | Pointer to the **OH\_Predicates** instance. |

**Returns**

| Type | Description |
| :-- | :-- |
| OH\_Predicates \* | Predicates with a right parenthesis. |

#### \[h2\]orOperate()

OH\_Predicates \*(\*orOperate)(OH\_Predicates \*predicates)

**Description**

Pointer to the function used to add the OR operator to the predicates.

This method is equivalent to **OR** in SQL statements.

**Since**: 10

**Parameters**

| Name | Description |
| :-- | :-- |
| OH\_Predicates \*predicates | Pointer to the **OH\_Predicates** instance. |

**Returns**

| Type | Description |
| :-- | :-- |
| OH\_Predicates \* | Predicates with the OR condition. |

#### \[h2\]andOperate()

OH\_Predicates \*(\*andOperate)(OH\_Predicates \*predicates)

**Description**

Pointer to the function used to add the AND operator to the predicates.

This method is equivalent to **AND** in SQL statements.

**Since**: 10

**Parameters**

| Name | Description |
| :-- | :-- |
| OH\_Predicates \*predicates | Pointer to the **OH\_Predicates** instance. |

**Returns**

| Type | Description |
| :-- | :-- |
| OH\_Predicates \* | Predicates with the AND condition. |

#### \[h2\]isNull()

OH\_Predicates \*(\*isNull)(OH\_Predicates \*predicates, const char \*field)

**Description**

Pointer to the function used to create a predicates object to search for the field values that are null.

This method is equivalent to **IS NULL** in SQL statements.

**Since**: 10

**Parameters**

| Name | Description |
| :-- | :-- |
| OH\_Predicates \*predicates | Pointer to the **OH\_Predicates** instance. |
| const char \*field | Column name in the database table. |

**Returns**

| Type | Description |
| :-- | :-- |
| OH\_Predicates \* | Predicates that match the specified field. |

#### \[h2\]isNotNull()

OH\_Predicates \*(\*isNotNull)(OH\_Predicates \*predicates, const char \*field)

**Description**

Pointer to the function used to create a predicates object to search for the field values that are not null.

This method is equivalent to **IS NOT NULL** in SQL statements.

**Since**: 10

**Parameters**

| Name | Description |
| :-- | :-- |
| OH\_Predicates \*predicates | Pointer to the **OH\_Predicates** instance. |
| const char \*field | Column name in the database table. |

**Returns**

| Type | Description |
| :-- | :-- |
| OH\_Predicates \* | Predicates that match the specified field. |

#### \[h2\]like()

OH\_Predicates \*(\*like)(OH\_Predicates \*predicates, const char \*field, OH\_VObject \*valueObject)

**Description**

Pointer to the function used to create a predicates object to search for the field values that are similar to the specified string.

This method is equivalent to **LIKE** in SQL statements.

**Since**: 10

**Parameters**

| Name | Description |
| :-- | :-- |
| OH\_Predicates \*predicates | Pointer to the **OH\_Predicates** instance. |
| const char \*field | Column name in the database table. |
| [OH\_VObject](../oh-vobject/document.md) \*valueObject | Pointer to an [OH\_VObject](../oh-vobject/document.md) instance, indicating the value to be matched with the predicate. |

**Returns**

| Type | Description |
| :-- | :-- |
| OH\_Predicates \* | Predicates that match the specified field. |

#### \[h2\]between()

OH\_Predicates \*(\*between)(OH\_Predicates \*predicates, const char \*field, OH\_VObject \*valueObject)

**Description**

Pointer to the function used to create a predicates object to search for the field values that are within the specified range.

This method is equivalent to **BETWEEN** in SQL statements.

**Since**: 10

**Parameters**

| Name | Description |
| :-- | :-- |
| OH\_Predicates \*predicates | Pointer to the **OH\_Predicates** instance. |
| const char \*field | Column name in the database table. |
| [OH\_VObject](../oh-vobject/document.md) \*valueObject | Pointer to an [OH\_VObject](../oh-vobject/document.md) instance, indicating the value to be matched with the predicate. |

**Returns**

| Type | Description |
| :-- | :-- |
| OH\_Predicates \* | Predicates that match the specified field. |

#### \[h2\]notBetween()

OH\_Predicates \*(\*notBetween)(OH\_Predicates \*predicates, const char \*field, OH\_VObject \*valueObject)

**Description**

Pointer to the function used to create a predicates object to search for the field values that are out of the specified range.

This method is equivalent to **NOT BETWEEN** in SQL statements.

**Since**: 10

**Parameters**

| Name | Description |
| :-- | :-- |
| OH\_Predicates \*predicates | Pointer to the **OH\_Predicates** instance. |
| const char \*field | Column name in the database table. |
| [OH\_VObject](../oh-vobject/document.md) \*valueObject | Pointer to an [OH\_VObject](../oh-vobject/document.md) instance, indicating the value to be matched with the predicate. |

**Returns**

| Type | Description |
| :-- | :-- |
| OH\_Predicates \* | Predicates that match the specified field. |

#### \[h2\]greaterThan()

OH\_Predicates \*(\*greaterThan)(OH\_Predicates \*predicates, const char \*field, OH\_VObject \*valueObject)

**Description**

Pointer to the function used to create a predicates object to search for the field values that are greater than the specified value.

This method is equivalent to ">" in SQL statements.

**Since**: 10

**Parameters**

| Name | Description |
| :-- | :-- |
| OH\_Predicates \*predicates | Pointer to the **OH\_Predicates** instance. |
| const char \*field | Column name in the database table. |
| [OH\_VObject](../oh-vobject/document.md) \*valueObject | Pointer to an [OH\_VObject](../oh-vobject/document.md) instance, indicating the value to be matched with the predicate. |

**Returns**

| Type | Description |
| :-- | :-- |
| OH\_Predicates \* | Predicates that match the specified field. |

#### \[h2\]lessThan()

OH\_Predicates \*(\*lessThan)(OH\_Predicates \*predicates, const char \*field, OH\_VObject \*valueObject)

**Description**

Pointer to the function used to create a predicates object to search for the records that are less than the given value in the specified field.

This method is equivalent to "<" in SQL statements.

**Since**: 10

**Parameters**

| Name | Description |
| :-- | :-- |
| OH\_Predicates \*predicates | Pointer to the **OH\_Predicates** instance. |
| const char \*field | Column name in the database table. |
| [OH\_VObject](../oh-vobject/document.md) \*valueObject | Pointer to an [OH\_VObject](../oh-vobject/document.md) instance, indicating the value to be matched with the predicate. |

**Returns**

| Type | Description |
| :-- | :-- |
| OH\_Predicates \* | Predicates that match the specified field. |

#### \[h2\]greaterThanOrEqualTo()

OH\_Predicates \*(\*greaterThanOrEqualTo)(OH\_Predicates \*predicates, const char \*field, OH\_VObject \*valueObject)

**Description**

Pointer to the function used to create a predicates object to search for the field values that are greater than or equal to the specified value.

This method is equivalent to ">=" in SQL statements.

**Since**: 10

**Parameters**

| Name | Description |
| :-- | :-- |
| OH\_Predicates \*predicates | Pointer to the **OH\_Predicates** instance. |
| const char \*field | Column name in the database table. |
| [OH\_VObject](../oh-vobject/document.md) \*valueObject | Pointer to an [OH\_VObject](../oh-vobject/document.md) instance, indicating the value to be matched with the predicate. |

**Returns**

| Type | Description |
| :-- | :-- |
| OH\_Predicates \* | Predicates that match the specified field. |

#### \[h2\]lessThanOrEqualTo()

OH\_Predicates \*(\*lessThanOrEqualTo)(OH\_Predicates \*predicates, const char \*field, OH\_VObject \*valueObject)

**Description**

Pointer to the function used to create a predicates object to search for the records that are less than or equal to the specified **valueObject** in the specified field.

This method is equivalent to "<=" in SQL statements.

**Since**: 10

**Parameters**

| Name | Description |
| :-- | :-- |
| OH\_Predicates \*predicates | Pointer to the **OH\_Predicates** instance. |
| const char \*field | Column name in the database table. |
| OH\_VObject \*valueObject | Pointer to an [OH\_VObject](../oh-vobject/document.md) instance, indicating the value to be matched with the predicate. |

**Returns**

| Type | Description |
| :-- | :-- |
| OH\_Predicates \* | Predicates that match the specified field. |

#### \[h2\]orderBy()

OH\_Predicates \*(\*orderBy)(OH\_Predicates \*predicates, const char \*field, OH\_OrderType type)

**Description**

Pointer to the function used to create a predicates object to sort the values in the specified column in ascending or descending order.

This method is equivalent to **ORDER BY** in SQL statements.

**Since**: 10

**Parameters**

| Name | Description |
| :-- | :-- |
| OH\_Predicates \*predicates | Pointer to the **OH\_Predicates** instance. |
| const char \*field | Column name in the database table. |
| [OH\_VObject](../oh-vobject/document.md) type | Sorting type, which is an [OH\_VObject](../oh-vobject/document.md). |

**Returns**

| Type | Description |
| :-- | :-- |
| OH\_Predicates \* | Predicates that match the specified field. |

#### \[h2\]distinct()

OH\_Predicates \*(\*distinct)(OH\_Predicates \*predicates)

**Description**

Pointer to the function used to create a predicates object to filter out duplicate records.

This method is equivalent to **DISTINCT** in SQL statements.

**Since**: 10

**Parameters**

| Name | Description |
| :-- | :-- |
| OH\_Predicates \*predicates | Pointer to the **OH\_Predicates** instance. |

**Returns**

| Type | Description |
| :-- | :-- |
| OH\_Predicates \* | Predicates that can filter out duplicate records. |

#### \[h2\]limit()

OH\_Predicates \*(\*limit)(OH\_Predicates \*predicates, unsigned int value)

**Description**

Pointer to the function used to create a predicates object to specify the maximum number of records.

This method is equivalent to **LIMIT** in SQL statements.

**Since**: 10

**Parameters**

| Name | Description |
| :-- | :-- |
| OH\_Predicates \*predicates | Pointer to the **OH\_Predicates** instance. |
| unsigned int value | Maximum number of data records. |

**Returns**

| Type | Description |
| :-- | :-- |
| OH\_Predicates \* | Predicates that specify the maximum number of records. |

#### \[h2\]offset()

OH\_Predicates \*(\*offset)(OH\_Predicates \*predicates, unsigned int rowOffset)

**Description**

Pointer to the function used to create a predicates object to specify the start position of the query result.

This method is equivalent to **OFFSET** in SQL statements.

**Since**: 10

**Parameters**

| Name | Description |
| :-- | :-- |
| OH\_Predicates \*predicates | Pointer to the **OH\_Predicates** instance. |
| unsigned int rowOffset | Start position, which is a positive integer. |

**Returns**

| Type | Description |
| :-- | :-- |
| OH\_Predicates \* | Predicates that specify the start position of the returned result. |

#### \[h2\]groupBy()

OH\_Predicates \*(\*groupBy)(OH\_Predicates \*predicates, char const \*const \*fields, int length)

**Description**

Pointer to the function used to create a predicates object to group the results by the specified columns.

This method is equivalent to **GROUP BY** in SQL statements.

**Since**: 10

**Parameters**

| Name | Description |
| :-- | :-- |
| OH\_Predicates \*predicates | Pointer to the **OH\_Predicates** instance. |
| char const \*const \*fields | Names of columns to group. |
| int length | Length of **fields**. |

**Returns**

| Type | Description |
| :-- | :-- |
| OH\_Predicates \* | Predicates that group rows with the same value. |

#### \[h2\]in()

OH\_Predicates \*(\*in)(OH\_Predicates \*predicates, const char \*field, OH\_VObject \*valueObject)

**Description**

Pointer to the function used to create a predicates object to search for the field values that are within the specified range.

This method is equivalent to **IN** in SQL statements.

**Since**: 10

**Parameters**

| Name | Description |
| :-- | :-- |
| OH\_Predicates \*predicates | Pointer to the **OH\_Predicates** instance. |
| const char \*field | Pointer to the column name in the database table. |
| [OH\_VObject](../oh-vobject/document.md) \*valueObject | Pointer to an [OH\_VObject](../oh-vobject/document.md) instance, indicating the value to be matched with the predicate. |

**Returns**

| Type | Description |
| :-- | :-- |
| OH\_Predicates \* | Predicates that match the specified field. |

#### \[h2\]notIn()

OH\_Predicates \*(\*notIn)(OH\_Predicates \*predicates, const char \*field, OH\_VObject \*valueObject)

**Description**

Pointer to the function used to create a predicates object to search for the field values that are out of the specified range.

This method is equivalent to **NOT IN** in SQL statements.

**Since**: 10

**Parameters**

| Name | Description |
| :-- | :-- |
| OH\_Predicates \*predicates | Pointer to the **OH\_Predicates** instance. |
| const char \*field | Pointer to the column name in the database table. |
| [OH\_VObject](../oh-vobject/document.md) \*valueObject | Pointer to an [OH\_VObject](../oh-vobject/document.md) instance, indicating the value to be matched with the predicate. |

**Returns**

| Type | Description |
| :-- | :-- |
| OH\_Predicates \* | Predicates that match the specified field. |

#### \[h2\]clear()

OH\_Predicates \*(\*clear)(OH\_Predicates \*predicates)

**Description**

Pointer to the function used to clear a predicates instance.

**Since**: 10

**Parameters**

| Name | Description |
| :-- | :-- |
| OH\_Predicates \*predicates | Pointer to the **OH\_Predicates** instance. |

**Returns**

| Type | Description |
| :-- | :-- |
| OH\_Predicates \* | Cleared predicates. |

#### \[h2\]destroy()

int (\*destroy)(OH\_Predicates \*predicates)

**Description**

Pointer to the function used to destroy an **OH\_Predicates** object and reclaim the memory occupied.

**Since**: 10

**Parameters**

| Name | Description |
| :-- | :-- |
| OH\_Predicates \*predicates | Pointer to the **OH\_Predicates** instance. |

**Returns**

| Type | Description |
| :-- | :-- |
| int | Returns **RDB\_OK** if the operation is successful; returns an error code otherwise. |
