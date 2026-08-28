# OH\_VObject

typedef struct {...} OH\_VObject

#### Overview

Defines a struct for allowed data types.

**Since**: 10

**Related module**: [RDB](../../modules/rdb/document.md)

**Header file**: [oh\_value\_object.h](../../header-files/oh-value-object-h/document.md)

#### Summary

#### \[h2\]Member Variables

| Name | Description |
| :-- | :-- |
| int64\_t id | Unique identifier of the **OH\_VObject** struct. |

#### \[h2\]Member Functions

| Name | Description |
| :-- | :-- |
| [int (\*putInt64)(OH\_VObject \*valueObject, int64\_t \*value, uint32\_t count)](#putint64) | Converts a single parameter or an array of the int64 type into a value of the OH\_VObject type. |
| [int (\*putDouble)(OH\_VObject \*valueObject, double \*value, uint32\_t count)](#putdouble) | Converts a single parameter or an array of the double type into a value of the OH\_VObject type. |
| [int (\*putText)(OH\_VObject \*valueObject, const char \*value)](#puttext) | Converts a character array of the char \* type to a value of the OH\_VObject type. |
| [int (\*putTexts)(OH\_VObject \*valueObject, const char \*\*value, uint32\_t count)](#puttexts) | Converts a string array of the char \* type to a value of the OH\_VObject type. |
| [int (\*destroy)(OH\_VObject \*valueObject)](#destroy) | Destroys an **OH\_VObject** object and reclaims the memory occupied. |

#### Member Function Description

#### \[h2\]putInt64()

int (\*putInt64)(OH\_VObject \*valueObject, int64\_t \*value, uint32\_t count)

**Description**

Converts a single parameter or an array of the int64 type into a value of the OH\_VObject type.

**Since**: 10

**Parameters**

| Name | Description |
| :-- | :-- |
| OH\_VObject \*valueObject | Pointer to the **OH\_VObject** instance. |
| int64\_t \*value | Pointer to the data to covert. |
| uint32\_t count | If **value** points to a single parameter, **count** is **1**. If **value** points to an array, **count** specifies the length of the array. |

**Returns**

| Type | Description |
| :-- | :-- |
| int | Returns **RDB\_OK** if the operation is successful; returns an error code otherwise. |

#### \[h2\]putDouble()

int (\*putDouble)(OH\_VObject \*valueObject, double \*value, uint32\_t count)

**Description**

Converts a single parameter or an array of the double type into a value of the OH\_VObject type.

**Since**: 10

**Parameters**

| Name | Description |
| :-- | :-- |
| OH\_VObject \*valueObject | Pointer to the **OH\_VObject** instance. |
| double \*value | Pointer to the data to covert. |
| uint32\_t count | If **value** points to a single parameter, **count** is **1**. If **value** points to an array, **count** specifies the length of the array. |

**Returns**

| Type | Description |
| :-- | :-- |
| int | Returns **RDB\_OK** if the operation is successful; returns an error code otherwise. |

#### \[h2\]putText()

int (\*putText)(OH\_VObject \*valueObject, const char \*value)

**Description**

Converts a character array of the char \* type to a value of the OH\_VObject type.

**Since**: 10

**Parameters**

| Name | Description |
| :-- | :-- |
| OH\_VObject \*valueObject | Pointer to the **OH\_VObject** instance. |
| const char \*value | Pointer to the character array to convert. |

**Returns**

| Type | Description |
| :-- | :-- |
| int | Returns **RDB\_OK** if the operation is successful; returns an error code otherwise. |

#### \[h2\]putTexts()

int (\*putTexts)(OH\_VObject \*valueObject, const char \*\*value, uint32\_t count)

**Description**

Converts a string array of the char \* type to a value of the OH\_VObject type.

**Since**: 10

**Parameters**

| Name | Description |
| :-- | :-- |
| OH\_VObject \*valueObject | Pointer to the **OH\_VObject** instance. |
| const char \*\*value | Double pointer to the string array to convert. |
| uint32\_t count | Length of the string array to convert. |

**Returns**

| Type | Description |
| :-- | :-- |
| int | Returns **RDB\_OK** if the operation is successful; returns an error code otherwise. |

#### \[h2\]destroy()

int (\*destroy)(OH\_VObject \*valueObject)

**Description**

Destroys an **OH\_VObject** object and reclaims the memory occupied.

**Since**: 10

**Parameters**

| Name | Description |
| :-- | :-- |
| OH\_VObject \*valueObject | Pointer to the **OH\_VObject** instance. |

**Returns**

| Type | Description |
| :-- | :-- |
| int | Returns **RDB\_OK** if the operation is successful; returns an error code otherwise. |
