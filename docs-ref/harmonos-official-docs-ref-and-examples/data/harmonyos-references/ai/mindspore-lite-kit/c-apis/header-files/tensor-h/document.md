# tensor.h

#### Overview

Provides tensor-related APIs, which can be used to create tensors and modify tensor information. These APIs are non-thread-safe.

**File to include**: <mindspore/tensor.h>

**Library**: libmindspore\_lite\_ndk.so

**System capability**: SystemCapability.Ai.MindSpore

**Since**: 9

**Related module**: [MindSpore](../../modules/mindspore/document.md)

#### Summary

#### \[h2\]Structs

| Name | typedef Keyword | Description |
| :-- | :-- | :-- |
| void \* | [OH\_AI\_TensorHandle](../../structs/oh-ai-tensorhandle/document.md) | Defines the handle of a tensor object. |
| void \* | [OH\_AI\_AllocatorHandle](../../structs/oh-ai-allocatorhandle/document.md) | Defines the handle of the memory allocator. |

#### \[h2\]Functions

| Name | Description |
| :-- | :-- |
| [OH\_AI\_API OH\_AI\_TensorHandle OH\_AI\_TensorCreate(const char \*name, OH\_AI\_DataType type, const int64\_t \*shape,size\_t shape\_num, const void \*data, size\_t data\_len)](#oh_ai_tensorcreate) | Creates a tensor object. |
| [OH\_AI\_API void OH\_AI\_TensorDestroy(OH\_AI\_TensorHandle \*tensor)](#oh_ai_tensordestroy) | Destroys a tensor object. |
| [OH\_AI\_API OH\_AI\_TensorHandle OH\_AI\_TensorClone(OH\_AI\_TensorHandle tensor)](#oh_ai_tensorclone) | Clones a tensor. |
| [OH\_AI\_API void OH\_AI\_TensorSetName(OH\_AI\_TensorHandle tensor, const char \*name)](#oh_ai_tensorsetname) | Sets the tensor name. |
| [OH\_AI\_API const char \*OH\_AI\_TensorGetName(const OH\_AI\_TensorHandle tensor)](#oh_ai_tensorgetname) | Obtains the tensor name. |
| [OH\_AI\_API void OH\_AI\_TensorSetDataType(OH\_AI\_TensorHandle tensor, OH\_AI\_DataType type)](#oh_ai_tensorsetdatatype) | Sets the data type of a tensor. |
| [OH\_AI\_API OH\_AI\_DataType OH\_AI\_TensorGetDataType(const OH\_AI\_TensorHandle tensor)](#oh_ai_tensorgetdatatype) | Obtains the tensor type. |
| [OH\_AI\_API void OH\_AI\_TensorSetShape(OH\_AI\_TensorHandle tensor, const int64\_t \*shape, size\_t shape\_num)](#oh_ai_tensorsetshape) | Sets the tensor shape. |
| [OH\_AI\_API const int64\_t \*OH\_AI\_TensorGetShape(const OH\_AI\_TensorHandle tensor, size\_t \*shape\_num)](#oh_ai_tensorgetshape) | Obtains the tensor shape. |
| [OH\_AI\_API void OH\_AI\_TensorSetFormat(OH\_AI\_TensorHandle tensor, OH\_AI\_Format format)](#oh_ai_tensorsetformat) | Sets the tensor data format. |
| [OH\_AI\_API OH\_AI\_Format OH\_AI\_TensorGetFormat(const OH\_AI\_TensorHandle tensor)](#oh_ai_tensorgetformat) | Obtains the tensor data format. |
| [OH\_AI\_API void OH\_AI\_TensorSetData(OH\_AI\_TensorHandle tensor, void \*data)](#oh_ai_tensorsetdata) | Sets the tensor data. |
| [OH\_AI\_API const void \*OH\_AI\_TensorGetData(const OH\_AI\_TensorHandle tensor)](#oh_ai_tensorgetdata) | Obtains the pointer to tensor data. |
| [OH\_AI\_API void \*OH\_AI\_TensorGetMutableData(const OH\_AI\_TensorHandle tensor)](#oh_ai_tensorgetmutabledata) | Obtains the pointer to variable tensor data. If the data is empty, memory will be allocated. |
| [OH\_AI\_API int64\_t OH\_AI\_TensorGetElementNum(const OH\_AI\_TensorHandle tensor)](#oh_ai_tensorgetelementnum) | Obtains the number of tensor elements. |
| [OH\_AI\_API size\_t OH\_AI\_TensorGetDataSize(const OH\_AI\_TensorHandle tensor)](#oh_ai_tensorgetdatasize) | Obtains the number of bytes of the tensor data. |
| [OH\_AI\_API OH\_AI\_Status OH\_AI\_TensorSetUserData(OH\_AI\_TensorHandle tensor, void \*data, size\_t data\_size)](#oh_ai_tensorsetuserdata) | 
Sets the tensor as the user data. This function allows you to reuse user data as the model input, which helps to reduce data copy by one time.

\> **NOTE**

The user data is type of external data for the tensor and is not automatically released when the tensor is destroyed. The caller needs to release the data separately. In addition, the caller must ensure that the user data is valid during use of the tensor.

 |
| [OH\_AI\_API OH\_AI\_AllocatorHandle OH\_AI\_TensorGetAllocator(OH\_AI\_TensorHandle tensor)](#oh_ai_tensorgetallocator) | Obtains a memory allocator. The allocator is responsible for allocating memory for tensors. |
| [OH\_AI\_API OH\_AI\_Status OH\_AI\_TensorSetAllocator(OH\_AI\_TensorHandle tensor, OH\_AI\_AllocatorHandle allocator)](#oh_ai_tensorsetallocator) | Sets the memory allocator. The allocator is responsible for allocating memory for tensors. |

#### Function Description

#### \[h2\]OH\_AI\_TensorCreate()

OH\_AI\_API OH\_AI\_TensorHandle OH\_AI\_TensorCreate(const char \*name, OH\_AI\_DataType type, const int64\_t \*shape,size\_t shape\_num, const void \*data, size\_t data\_len)

**Description**

Creates a tensor object.

**Since**: 9

**Parameters**

| Name | Description |
| :-- | :-- |
| const char \*name | Tensor name. The string length is subject to system restrictions. |
| [OH\_AI\_DataType](../data-type-h/document.md#oh_ai_datatype) type | Tensor data type. |
| const int64\_t \*shape | Tensor dimension array. |
| size\_t shape\_num | Length of the tensor dimension array. |
| const void \*data | Data pointer. |
| size\_t data\_len | Data length. |

**Returns**

| Type | Description |
| :-- | :-- |
| OH\_AI\_API [OH\_AI\_TensorHandle](../../structs/oh-ai-tensorhandle/document.md) | Handle of the tensor object. |

#### \[h2\]OH\_AI\_TensorDestroy()

OH\_AI\_API void OH\_AI\_TensorDestroy(OH\_AI\_TensorHandle \*tensor)

**Description**

Destroys a tensor object.

**Since**: 9

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_AI\_TensorHandle](../../structs/oh-ai-tensorhandle/document.md) \*tensor | Level-2 pointer to the tensor handle. |

#### \[h2\]OH\_AI\_TensorClone()

OH\_AI\_API OH\_AI\_TensorHandle OH\_AI\_TensorClone(OH\_AI\_TensorHandle tensor)

**Description**

Clones a tensor.

**Since**: 9

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_AI\_TensorHandle](../../structs/oh-ai-tensorhandle/document.md) tensor | Handle of the tensor object. |

**Returns**

| Type | Description |
| :-- | :-- |
| OH\_AI\_API [OH\_AI\_TensorHandle](../../structs/oh-ai-tensorhandle/document.md) | Handle of the new tensor object. |

#### \[h2\]OH\_AI\_TensorSetName()

OH\_AI\_API void OH\_AI\_TensorSetName(OH\_AI\_TensorHandle tensor, const char \*name)

**Description**

Sets the tensor name.

**Since**: 9

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_AI\_TensorHandle](../../structs/oh-ai-tensorhandle/document.md) tensor | Handle of the tensor object. |
| const char \*name | Tensor name. The string length is subject to system restrictions. |

#### \[h2\]OH\_AI\_TensorGetName()

OH\_AI\_API const char \*OH\_AI\_TensorGetName(const OH\_AI\_TensorHandle tensor)

**Description**

Obtains the tensor name.

**Since**: 9

**Parameters**

| Name | Description |
| :-- | :-- |
| const [OH\_AI\_TensorHandle](../../structs/oh-ai-tensorhandle/document.md) tensor | Handle of the tensor object. |

**Returns**

| Type | Description |
| :-- | :-- |
| OH\_AI\_API const char \* | Tensor name. |

#### \[h2\]OH\_AI\_TensorSetDataType()

OH\_AI\_API void OH\_AI\_TensorSetDataType(OH\_AI\_TensorHandle tensor, OH\_AI\_DataType type)

**Description**

Sets the data type of a tensor.

**Since**: 9

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_AI\_TensorHandle](../../structs/oh-ai-tensorhandle/document.md) tensor | Handle of the tensor object. |
| [OH\_AI\_DataType](../data-type-h/document.md#oh_ai_datatype) type | Data type. For details, see [OH\_AI\_DataType](../data-type-h/document.md#oh_ai_datatype). |

#### \[h2\]OH\_AI\_TensorGetDataType()

OH\_AI\_API OH\_AI\_DataType OH\_AI\_TensorGetDataType(const OH\_AI\_TensorHandle tensor)

**Description**

Obtains the tensor type.

**Since**: 9

**Parameters**

| Name | Description |
| :-- | :-- |
| const [OH\_AI\_TensorHandle](../../structs/oh-ai-tensorhandle/document.md) tensor | Handle of the tensor object. |

**Returns**

| Type | Description |
| :-- | :-- |
| OH\_AI\_API [OH\_AI\_DataType](../data-type-h/document.md#oh_ai_datatype) | Tensor data type. |

#### \[h2\]OH\_AI\_TensorSetShape()

OH\_AI\_API void OH\_AI\_TensorSetShape(OH\_AI\_TensorHandle tensor, const int64\_t \*shape, size\_t shape\_num)

**Description**

Sets the tensor shape.

**Since**: 9

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_AI\_TensorHandle](../../structs/oh-ai-tensorhandle/document.md) tensor | Handle of the tensor object. |
| const int64\_t \*shape | Shape array. |
| size\_t shape\_num | Length of the tensor shape array. |

#### \[h2\]OH\_AI\_TensorGetShape()

OH\_AI\_API const int64\_t \*OH\_AI\_TensorGetShape(const OH\_AI\_TensorHandle tensor, size\_t \*shape\_num)

**Description**

Obtains the tensor shape.

**Since**: 9

**Parameters**

| Name | Description |
| :-- | :-- |
| const [OH\_AI\_TensorHandle](../../structs/oh-ai-tensorhandle/document.md) tensor | Handle of the tensor object. |
| size\_t \*shape\_num | Length of the tensor shape array. |

**Returns**

| Type | Description |
| :-- | :-- |
| OH\_AI\_API const int64\_t \* | Shape array. |

#### \[h2\]OH\_AI\_TensorSetFormat()

OH\_AI\_API void OH\_AI\_TensorSetFormat(OH\_AI\_TensorHandle tensor, OH\_AI\_Format format)

**Description**

Sets the tensor data format.

**Since**: 9

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_AI\_TensorHandle](../../structs/oh-ai-tensorhandle/document.md) tensor | Handle of the tensor object. |
| [OH\_AI\_Format](../format-h/document.md#oh_ai_format) format | Tensor data format. |

#### \[h2\]OH\_AI\_TensorGetFormat()

OH\_AI\_API OH\_AI\_Format OH\_AI\_TensorGetFormat(const OH\_AI\_TensorHandle tensor)

**Description**

Obtains the tensor data format.

**Since**: 9

**Parameters**

| Name | Description |
| :-- | :-- |
| const [OH\_AI\_TensorHandle](../../structs/oh-ai-tensorhandle/document.md) tensor | Handle of the tensor object. |

**Returns**

| Type | Description |
| :-- | :-- |
| OH\_AI\_API [OH\_AI\_Format](../format-h/document.md#oh_ai_format) | Tensor data format. |

#### \[h2\]OH\_AI\_TensorSetData()

OH\_AI\_API void OH\_AI\_TensorSetData(OH\_AI\_TensorHandle tensor, void \*data)

**Description**

Sets the tensor data.

**Since**: 9

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_AI\_TensorHandle](../../structs/oh-ai-tensorhandle/document.md) tensor | Handle of the tensor object. |
| void \*data | Data pointer. |

#### \[h2\]OH\_AI\_TensorGetData()

OH\_AI\_API const void \*OH\_AI\_TensorGetData(const OH\_AI\_TensorHandle tensor)

**Description**

Obtains the pointer to tensor data.

**Since**: 9

**Parameters**

| Name | Description |
| :-- | :-- |
| const [OH\_AI\_TensorHandle](../../structs/oh-ai-tensorhandle/document.md) tensor | Handle of the tensor object. |

**Returns**

| Type | Description |
| :-- | :-- |
| OH\_AI\_API const void \* | Pointer to tensor data. |

#### \[h2\]OH\_AI\_TensorGetMutableData()

OH\_AI\_API void \*OH\_AI\_TensorGetMutableData(const OH\_AI\_TensorHandle tensor)

**Description**

Obtains the pointer to variable tensor data. If the data is empty, memory will be allocated.

**Since**: 9

**Parameters**

| Name | Description |
| :-- | :-- |
| const [OH\_AI\_TensorHandle](../../structs/oh-ai-tensorhandle/document.md) tensor | Handle of the tensor object. |

**Returns**

| Type | Description |
| :-- | :-- |
| OH\_AI\_API void \* | Pointer to tensor data. |

#### \[h2\]OH\_AI\_TensorGetElementNum()

OH\_AI\_API int64\_t OH\_AI\_TensorGetElementNum(const OH\_AI\_TensorHandle tensor)

**Description**

Obtains the number of tensor elements.

**Since**: 9

**Parameters**

| Name | Description |
| :-- | :-- |
| const [OH\_AI\_TensorHandle](../../structs/oh-ai-tensorhandle/document.md) tensor | Handle of the tensor object. |

**Returns**

| Type | Description |
| :-- | :-- |
| OH\_AI\_API int64\_t | Number of tensor elements. |

#### \[h2\]OH\_AI\_TensorGetDataSize()

OH\_AI\_API size\_t OH\_AI\_TensorGetDataSize(const OH\_AI\_TensorHandle tensor)

**Description**

Obtains the number of bytes of the tensor data.

**Since**: 9

**Parameters**

| Name | Description |
| :-- | :-- |
| const [OH\_AI\_TensorHandle](../../structs/oh-ai-tensorhandle/document.md) tensor | Handle of the tensor object. |

**Returns**

| Type | Description |
| :-- | :-- |
| OH\_AI\_API size\_t | Number of bytes of the tensor data. |

#### \[h2\]OH\_AI\_TensorSetUserData()

OH\_AI\_API OH\_AI\_Status OH\_AI\_TensorSetUserData(OH\_AI\_TensorHandle tensor, void \*data, size\_t data\_size)

**Description**

Sets the tensor as the user data. This function allows you to reuse user data as the model input, which helps to reduce data copy by one time.

\> **NOTE**

The user data is type of external data for the tensor and is not automatically released when the tensor is destroyed. The caller needs to release the data separately. In addition, the caller must ensure that the user data is valid during use of the tensor.

**Since**: 10

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_AI\_TensorHandle](../../structs/oh-ai-tensorhandle/document.md) tensor | Handle of the tensor object. |
| void \*data | Start address of user data. |
| size\_t data\_size | Length of the user data length. |

**Returns**

| Type | Description |
| :-- | :-- |
| OH\_AI\_API [OH\_AI\_Status](../status-h/document.md#oh_ai_status) | Execution status code. The value **OH\_AI\_STATUS\_SUCCESS** indicates that the operation is successful. If the operation fails, an error code is returned. |

#### \[h2\]OH\_AI\_TensorGetAllocator()

OH\_AI\_API OH\_AI\_AllocatorHandle OH\_AI\_TensorGetAllocator(OH\_AI\_TensorHandle tensor)

**Description**

Obtains a memory allocator. The allocator is responsible for allocating memory for tensors.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_AI\_TensorHandle](../../structs/oh-ai-tensorhandle/document.md) tensor | Handle of the tensor object. |

**Returns**

| Type | Description |
| :-- | :-- |
| OH\_AI\_API [OH\_AI\_AllocatorHandle](../../structs/oh-ai-allocatorhandle/document.md) | Handle of the memory allocator. |

#### \[h2\]OH\_AI\_TensorSetAllocator()

OH\_AI\_API OH\_AI\_Status OH\_AI\_TensorSetAllocator(OH\_AI\_TensorHandle tensor, OH\_AI\_AllocatorHandle allocator)

**Description**

Sets the memory allocator. The allocator is responsible for allocating memory for tensors.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_AI\_TensorHandle](../../structs/oh-ai-tensorhandle/document.md) tensor | Handle of the tensor object. |
| [OH\_AI\_AllocatorHandle](../../structs/oh-ai-allocatorhandle/document.md) allocator | Handle of the memory allocator. |

**Returns**

| Type | Description |
| :-- | :-- |
| OH\_AI\_API [OH\_AI\_Status](../status-h/document.md#oh_ai_status) | Execution status code. The value **OH\_AI\_STATUS\_SUCCESS** indicates that the operation is successful. If the operation fails, an error code is returned. |
