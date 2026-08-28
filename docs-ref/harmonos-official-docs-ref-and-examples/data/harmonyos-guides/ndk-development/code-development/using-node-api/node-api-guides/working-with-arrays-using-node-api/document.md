# Working with Arrays Using Node-API

#### Introduction

Node-API provides APIs for directly managing ArkTS arrays.

#### Basic Concepts

Node-API can be used to create, access, modify, and traverse arrays. Before using Node-API, it's helpful if you understand the following concepts:

-   Array creation: You can use **napi\_create\_array** to create an array and pass it to the ArkTS layer.
-   Array-related operations: You can use the APIs provides by the Node-API module to obtain the length of an ArkTS array, retrieve the element at the specified index, and set the element value at the specified index.
-   **TypedArray**: A **TypedArray** object in ArkTS is an array-like view of an underlying binary data buffer. It can be understood as an array of elements of the specified type. There is no constructor for **TypedArray** objects, but they can be constructed by their child class constructors. The child classes of **TypedArray** include **Int8Array**, **Uint8Array**, **Uint8ClampedArray**, **Int16Array**, and **Int32Array**.
-   **DataView**: **DataView** is a flexible binary data access view in ArkTS. It provides methods for reading and writing multiple number types from an **ArrayBuffer**. Unlike **TypedArray**, **DataView** does not require data to be aligned at specific bytes. Therefore, it can process data structures with arbitrary byte offsets. DataView supports the following methods (each method has a **get** and **set** version): **Int8**, **Uint8**, **Int16**, **Uint16**, **Int32**, **Uint32**, **Float32**, and **Float64**.
-   **ArrayBuffer**: **ArrayBuffer** is a data struct used to represent a binary data buffer of fixed length. It cannot be read or written directly, but its content can be operated through **TypedArray** or **DataView**.

#### Available APIs

The following table describes the APIs for managing ArkTS arrays.

| API | Description |
| :-- | :-- |
| [napi\_create\_array](https://nodejs.org/docs/latest-v18.x/api/n-api.html#napi_create_array) | Creates an ArkTS array. |
| [napi\_create\_array\_with\_length](https://nodejs.org/docs/latest-v18.x/api/n-api.html#napi_create_array_with_length) | Creates an ArkTS array object of the specified length. |
| [napi\_get\_array\_length](https://nodejs.org/docs/latest-v18.x/api/n-api.html#napi_get_array_length) | Obtains the length of an ArkTS array. |
| [napi\_is\_array](https://nodejs.org/docs/latest-v18.x/api/n-api.html#napi_is_array) | Checks whether the given **napi\_value** is an array. |
| [napi\_set\_element](https://nodejs.org/docs/latest-v18.x/api/n-api.html#napi_set_element) | Sets an element at the specified index in the given ArkTS array. |
| [napi\_get\_element](https://nodejs.org/docs/latest-v18.x/api/n-api.html#napi_get_element) | Obtains the element at the specified index in the given ArkTS array. |
| [napi\_has\_element](https://nodejs.org/docs/latest-v18.x/api/n-api.html#napi_has_element) | Checks whether the element at the specified index exists. |
| [napi\_delete\_element](https://nodejs.org/docs/latest-v18.x/api/n-api.html#napi_delete_element) | Deletes the element at the specified index of the given ArkTS array. |
| [napi\_create\_typedarray](https://nodejs.org/docs/latest-v18.x/api/n-api.html#napi_create_typedarray) | Creates an ArkTS **TypedArray** object of the specified type, such as **Uint8Array** or **Int32Array**. You can use this API to convert a native value into a **TypedArray** object for performant data processing. |
| [napi\_is\_typedarray](https://nodejs.org/docs/latest-v18.x/api/n-api.html#napi_is_typedarray) | Checks whether the given **napi\_value** is a **TypedArray** object. |
| [napi\_get\_typedarray\_info](https://nodejs.org/docs/latest-v18.x/api/n-api.html#napi_get_typedarray_info) | Obtains the properties of a **TypedArray** object. |
| [napi\_create\_dataview](https://nodejs.org/docs/latest-v18.x/api/n-api.html#napi_create_dataview) | Creates a **DataView** object, which allows access to binary data. |
| [napi\_is\_dataview](https://nodejs.org/docs/latest-v18.x/api/n-api.html#napi_is_dataview) | Checks whether the given **napi\_value** is a **DataView** object in ArkTS. |
| [napi\_get\_dataview\_info](https://nodejs.org/docs/latest-v18.x/api/n-api.html#napi_get_dataview_info) | Obtains the properties of a **DataView** object. |

#### Example

If you are just starting out with Node-API, see [Node-API Development Process](../../node-api-development-process/document.md). The following demonstrates only the C++ and ArkTS code for array management APIs.

The following header files are required for the C++ code:

#include "napi/native\_api.h"

The following modules are required for the ArkTS code:

import { hilog } from '@kit.PerformanceAnalysisKit';
import testNapi from 'libentry.so';

## napi\_create\_array

Call **napi\_create\_array** to create an ArkTS array.

CPP code:

static constexpr int INT\_NUM\_5 = 5; // Length of the input parameter index array

// Use napi\_create\_array to develop arrays.
static napi\_value CreateArray(napi\_env env, napi\_callback\_info info)
{
    // Create an empty array.
    napi\_value jsArray = nullptr;
    napi\_create\_array(env, &jsArray);
    // Assign a value to the created array.
    for (int i = 0; i < INT\_NUM\_5; i++) {
        napi\_value element;
        napi\_create\_int32(env, i, &element);
        napi\_set\_element(env, jsArray, i, element);
    }
    // Return the created array.
    return jsArray;
}

API declaration:

index.d.ts

export const createArray: () => number\[\]; // Use napi\_create\_array to develop arrays.

ArkTS code:

// Use napi\_create\_array to develop arrays.
hilog.info(0x0000, 'testTag', 'Test Node-API napi\_create\_array:%{public}s',
  JSON.stringify(testNapi.createArray()));

## napi\_create\_array\_with\_length

Call **napi\_create\_array\_with\_length** to create an ArkTS array of the specified length.

CPP code:

// Use napi\_create\_array\_with\_length to develop arrays.
static napi\_value CreateArrayWithLength(napi\_env env, napi\_callback\_info info)
{
    // Obtain the parameters passed from ArkTS.
    size\_t argc = 1;
    napi\_value argv\[1\] = {nullptr};
    napi\_value jsArray = nullptr;
    napi\_get\_cb\_info(env, info, &argc, argv, nullptr, nullptr);
    // Obtain the array length passed.
    int32\_t length = 0;
    napi\_get\_value\_int32(env, argv\[0\], &length);
    // Use napi\_create\_array\_with\_length to create an array of the specified length.
    napi\_create\_array\_with\_length(env, length, &jsArray);
    // Return the array.
    return jsArray;
}

API declaration:

index.d.ts

export const createArrayWithLength: (length: number) => void\[\]; // Use napi\_create\_array\_with\_length to develop arrays.

ArkTS code:

// Use napi\_create\_array\_with\_length to develop arrays.
let array = testNapi.createArrayWithLength(6);
hilog.info(0x0000, 'testTag', 'Test Node-API napi\_create\_array\_with\_length:%{public}d', array.length);

## napi\_get\_array\_length

Call **napi\_get\_array\_length** to obtain the length of an array.

CPP code:

// Use napi\_get\_array\_length to develop arrays.
static napi\_value GetArrayLength(napi\_env env, napi\_callback\_info info)
{
    // Obtain the parameters passed from ArkTS.
    size\_t argc = 1;
    napi\_value args\[1\] = {nullptr};
    napi\_value result;
    uint32\_t length;
    napi\_get\_cb\_info(env, info, &argc, args, nullptr, nullptr);
    // Check whether the parameter is an array.
    bool isArray;
    napi\_is\_array(env, args\[0\], &isArray);
    if (!isArray) {
        napi\_throw\_error(env, nullptr, "Argument must be an array");
        return nullptr;
    }
    napi\_get\_array\_length(env, args\[0\], &length);
    // Create a return value.
    napi\_create\_uint32(env, length, &result);
    return result;
}

API declaration:

index.d.ts

export const getArrayLength: (arr: Array<any>) => number | undefined; // Use napi\_get\_array\_length to develop arrays.

ArkTS code:

// Use napi\_get\_array\_length to develop arrays.
const arr = \[0, 1, 2, 3, 4, 5\];
hilog.info(0x0000, 'testTag', 'Test Node-API get\_array\_length:%{public}d',
  testNapi.getArrayLength(arr));

## napi\_is\_array

Call **napi\_is\_array** to check whether the given ArkTS value is an array.

CPP code:

// Use napi\_is\_array to develop arrays.
static napi\_value IsArray(napi\_env env, napi\_callback\_info info)
{
    // Obtain the parameters passed from ArkTS.
    size\_t argc = 1;
    napi\_value args\[1\] = {nullptr};
    napi\_get\_cb\_info(env, info, &argc, args, nullptr, nullptr);
    // Call napi\_is\_array to check whether the input parameter is an array.
    bool result = false;
    napi\_status status = napi\_is\_array(env, args\[0\], &result);
    if (status != napi\_ok) {
        napi\_throw\_error(env, nullptr, "Node-API napi\_is\_array fail");
        return nullptr;
    }
    // Convert the result to napi\_value and return it.
    napi\_value returnValue;
    napi\_get\_boolean(env, result, &returnValue);

    return returnValue;
}

API declaration:

index.d.ts

export const isArray: <T>(data: Array<T> | T) => boolean | undefined; // Use napi\_is\_array to develop arrays.

ArkTS code:

// Use napi\_is\_array to develop arrays.
try {
  let value = new Array<number>(1);
  let data = "123";
  hilog.info(0x0000, 'testTag', 'Test Node-API napi\_is\_array: %{public}s',
    testNapi.isArray<number>(value));
  hilog.info(0x0000, 'testTag', 'Test Node-API napi\_is\_array: %{public}s',
    testNapi.isArray<string>(data));
  // ...
} catch (error) {
  hilog.error(0x0000, 'testTag', 'Test Node-API napi\_is\_array error: %{public}s', error.message);
  // ...
}

## napi\_set\_element

Call **napi\_set\_element** to set an element at the specified index in an ArkTS array.

For the object that uses the index value as the key, you can use **napi\_set\_element** to set the property value.

CPP code:

static constexpr int INT\_ARG\_2 = 2; // Input parameter index.
// ...
// Use napi\_set\_element to develop arrays.
static napi\_value NapiSetElement(napi\_env env, napi\_callback\_info info)
{
    // Obtain the parameters passed from ArkTS.
    size\_t argc = 3;
    napi\_value args\[3\] = {nullptr};
    napi\_get\_cb\_info(env, info, &argc, args, nullptr, nullptr);
    // Check whether the first parameter is an array.
    bool isArr = false;
    napi\_is\_array(env, args\[0\], &isArr);
    if (!isArr) {
        napi\_throw\_error(env, nullptr, "Argument should be an object of type array");
        return nullptr;
    }
    // Obtain the index of the element to be set.
    double index = 0;
    napi\_status status = napi\_get\_value\_double(env, args\[1\], &index);
    if (status != napi\_ok || index < 0) {
        napi\_throw\_error(env, nullptr, "The index should be a non-negative number");
        return nullptr;
    }
    // Set the input value at the specified index of the array.
    napi\_set\_element(env, args\[0\], static\_cast<uint32\_t>(index), args\[INT\_ARG\_2\]);

    return nullptr;
}

API declaration:

index.d.ts

export const napiSetElement: <T>(arr: Array<T>, index: number,
  value: T) => void; // Use napi\_set\_element to develop arrays.

ArkTS code:

// Use napi\_set\_element to develop arrays.
try {
  let arr = \[10, 20, 30\];
  testNapi.napiSetElement<number | string>(arr, 1, 'newElement');
  testNapi.napiSetElement<number | string>(arr, 2, 50);
  hilog.info(0x0000, 'testTag', 'Test Node-API napi\_set\_element arr: %{public}s', arr.toString());
  hilog.info(0x0000, 'testTag', 'Test Node-API napi\_set\_element arr\[3\]: %{public}s', arr\[3\]);
  interface MyObject {
    first: number;
    second: number;
  }
  let obj: MyObject = {
    first: 1,
    second: 2
  };
  testNapi.napiSetElement<number | string | Object>(arr, 4, obj);
  let objAsString = JSON.stringify(arr\[4\]);
  hilog.info(0x0000, 'testTag', 'Test Node-API napi\_set\_element arr\[4\]: %{public}s', objAsString);
} catch (error) {
  hilog.error(0x0000, 'testTag', 'Test Node-API napi\_set\_element error: %{public}s', error.message);
}

## napi\_get\_element

Call **napi\_get\_element** to obtain the element at the specified index in an ArkTS array. The index must be within the valid range of the array. Otherwise, **undefined** will be returned.

CPP code:

// Use napi\_get\_element to develop arrays.
static napi\_value NapiGetElement(napi\_env env, napi\_callback\_info info)
{
    // Obtain the parameters passed from ArkTS.
    size\_t argc = 2;
    napi\_value args\[2\] = {nullptr};
    napi\_get\_cb\_info(env, info, &argc, args, nullptr, nullptr);
    // Obtain the index value of the element.
    uint32\_t index;
    napi\_get\_value\_uint32(env, args\[1\], &index);
    // Obtain the element value at the index and store it in result.
    napi\_value result;
    napi\_get\_element(env, args\[0\], index, &result);

    return result;
}

API declaration:

index.d.ts

export const napiGetElement: <T>(arr: Array<T>,
  index: number) => number | string | Object | boolean | undefined; // Use napi\_get\_element to develop arrays.

ArkTS code:

// Use napi\_get\_element to develop arrays.
interface MyObject {
  first: number;
  second: number;
}

let obj: MyObject = {
  first: 1,
  second: 2
};
let arr = \[10, 'hello', null, obj\];
hilog.info(0x0000, 'testTag', 'Test Node-API napi\_get\_element arr\[0\]: %{public}d',
  testNapi.napiGetElement<number | string | null | Object>(arr, 0));
hilog.info(0x0000, 'testTag', 'Test Node-API napi\_get\_element arr\[1\]: %{public}s',
  testNapi.napiGetElement<number | string | null | Object>(arr, 1));
hilog.info(0x0000, 'testTag', 'Test Node-API napi\_get\_element arr\[2\]: %{public}s',
  testNapi.napiGetElement<number | string | null | Object>(arr, 2));
hilog.info(0x0000, 'testTag', 'Test Node-API napi\_get\_element arr\[3\]: %{public}s',
  testNapi.napiGetElement<number | string | null | Object>(arr, 3));
hilog.info(0x0000, 'testTag', 'Test Node-API napi\_get\_element arr\[4\]: %{public}s',
  JSON.stringify(testNapi.napiGetElement(arr, 4)));
hilog.info(0x0000, 'testTag', 'Test Node-API napi\_get\_element arr\[null\]: %{public}s',
  testNapi.napiGetElement<number | string | null | Object>(arr, 5));

## napi\_has\_element

Call **napi\_has\_element** to check whether an ArkTS array has the element at the specified index. If the specified index exceeds the valid range of the array, **false** will be returned, which indicates that the element does not exist.

CPP code:

// Use napi\_has\_element to develop arrays.
static napi\_value NapiHasElement(napi\_env env, napi\_callback\_info info)
{
    // Obtain the parameters passed from ArkTS.
    size\_t argc = 2;
    napi\_value args\[2\] = {nullptr};
    napi\_get\_cb\_info(env, info, &argc, args, nullptr, nullptr);
    // Obtain the index of the element to be checked.
    uint32\_t index;
    napi\_get\_value\_uint32(env, args\[1\], &index);
    // Check whether the element exists based on the given index.
    bool hasElement = true;
    napi\_has\_element(env, args\[0\], index, &hasElement);
    // Convert the bool value to napi\_value and return it.
    napi\_value result;
    napi\_get\_boolean(env, hasElement, &result);
    return result;
}

API declaration:

index.d.ts

export const napiHasElement: <T>(arr: Array<T>, index: number) => boolean; // Use napi\_has\_element to develop arrays.

ArkTS code:

// Use napi\_has\_element to develop arrays.
let arr = \[10, 'hello', null, 'world'\];
hilog.info(0x0000, 'testTag', 'Test Node-API napi\_has\_element arr\[0\]: %{public}s',
  testNapi.napiHasElement<number | string | null>(arr, 0));
hilog.info(0x0000, 'testTag', 'Test Node-API napi\_has\_element arr\[7\]: %{public}s',
  testNapi.napiHasElement<number | string | null>(arr, 7));

## napi\_delete\_element

Call **napi\_delete\_element** to delete the element at the specified index from an ArkTS array.

CPP code:

// Use napi\_delete\_element to develop arrays.
static napi\_value NapiDeleteElement(napi\_env env, napi\_callback\_info info)
{
    // Obtain the parameters passed from ArkTS.
    size\_t argc = 2;
    napi\_value args\[2\] = {nullptr};
    napi\_get\_cb\_info(env, info, &argc, args, nullptr, nullptr);
    // Obtain the index of the element to delete.
    uint32\_t index;
    napi\_get\_value\_uint32(env, args\[1\], &index);
    // Delete the element at the specified index.
    bool deleted = true;
    napi\_delete\_element(env, args\[0\], index, &deleted);
    // Convert the bool value to napi\_value and return it.
    napi\_value result;
    napi\_get\_boolean(env, deleted, &result);
    return result;
}

API declaration:

index.d.ts

export const napiDeleteElement: <T>(arr: Array<T>,
  index: number) => boolean; // Use napi\_delete\_element to develop arrays.

ArkTS code:

Import **napiHasElement** and **napiGetElement** in the preceding sample code to **index.d.ts**.

// Use napi\_delete\_element to develop arrays.
let arr = \[10, 'hello', null, 'world'\];
hilog.info(0x0000, 'testTag', 'Test Node-API napi\_has\_element arr\[0\]: %{public}s',
  testNapi.napiHasElement<number | string | null>(arr, 0));
hilog.info(0x0000, 'testTag', 'Test Node-API napi\_delete\_element arr\[0\]: %{public}s',
  testNapi.napiDeleteElement<number | string | null>(arr, 0));
hilog.info(0x0000, 'testTag', 'Test Node-API napi\_has\_element deleted arr\[0\]: %{public}s',
  testNapi.napiHasElement<number | string | null>(arr, 0));
hilog.info(0x0000, 'testTag', 'Test Node-API napi\_get\_element arr\[0\]: %{public}d',
  testNapi.napiGetElement<number | string | null>(arr, 0));

## napi\_create\_typedarray

Call **napi\_create\_typedarray** to create an ArkTS **TypedArray** object of the specified type from an existing **ArrayBuffer** object.

CPP code:

// Use napi\_create\_typedarray to develop arrays.
static napi\_value CreateTypedArray(napi\_env env, napi\_callback\_info info)
{
    // Obtain the parameters passed from ArkTS.
    size\_t argc = 1;
    napi\_value args\[1\] = {nullptr};
    napi\_get\_cb\_info(env, info, &argc, args, nullptr, nullptr);
    int32\_t typeNum = 0;
    napi\_get\_value\_int32(env, args\[0\], &typeNum);
    napi\_typedarray\_type arrayType;
    // Set the element size.
    size\_t elementSize = 0;
    // Determine the type of the array to create based on the type value passed.
    arrayType = static\_cast<napi\_typedarray\_type>(typeNum);
    switch (arrayType) {
        case napi\_int8\_array:
        case napi\_uint8\_array:
        case napi\_uint8\_clamped\_array:
            elementSize = sizeof(int8\_t);
            break;
        case napi\_int16\_array:
        case napi\_uint16\_array:
            elementSize = sizeof(int16\_t);
            break;
        case napi\_int32\_array:
        case napi\_uint32\_array:
            elementSize = sizeof(int32\_t);
            break;
        case napi\_float32\_array:
            elementSize = sizeof(float);
            break;
        case napi\_float64\_array:
            elementSize = sizeof(double);
            break;
        case napi\_bigint64\_array:
        case napi\_biguint64\_array:
            elementSize = sizeof(int64\_t);
            break;
        default:
        // By default, an array of the napi\_int8\_array type is created.
            arrayType = napi\_int8\_array;
            elementSize = sizeof(int8\_t);
            break;
    }
    size\_t length = 3;
    napi\_value arrayBuffer = nullptr;
    napi\_value typedArray = nullptr;
    void \*data;
    // Create an ArrayBuffer object.
    napi\_create\_arraybuffer(env, length \* elementSize, (void \*\*)&data, &arrayBuffer);
    // Create a TypedArray object of the specified type.
    napi\_create\_typedarray(env, arrayType, length, arrayBuffer, 0, &typedArray);
    return typedArray;
}

API declaration:

index.d.ts

export const enum TypedArrayTypes {
  INT8\_ARRAY = 0,
  UINT8\_ARRAY,
  UINT8\_CLAMPED\_ARRAY,
  INT16\_ARRAY,
  UINT16\_ARRAY,
  INT32\_ARRAY,
  UINT32\_ARRAY,
  FLOAT32\_ARRAY,
  FLOAT64\_ARRAY,
  BIGINT64\_ARRAY,
  BIGUINT64\_ARRAY,
}

export const createTypedArray: <T>(type: TypedArrayTypes) => T; // Use napi\_create\_typedarray to develop arrays.

ArkTS code:

// Use napi\_create\_typedarray to develop arrays.
// Pass the type of the array to create.
let typedArray = testNapi.createTypedArray<Int8Array>(testNapi.TypedArrayTypes\["INT8\_ARRAY"\]);
if (typedArray instanceof Int8Array) {
  hilog.info(0x0000, 'testTag', ' Node-API napi\_create\_typedarray: Int8Array');
  // ...
}
let uint8Array = testNapi.createTypedArray<Uint8Array>(testNapi.TypedArrayTypes\["UINT8\_ARRAY"\]);
if (uint8Array instanceof Uint8Array) {
  hilog.info(0x0000, 'testTag', ' Node-API napi\_create\_typedarray: Uint8Array');
  // ...
}

Modify the module initialization in **use-napi-process.md** as follows:

#include <string>

EXTERN\_C\_START
static napi\_value Init(napi\_env env, napi\_value exports)
{
    // The defined TypedArray type is used by ArkTS to store typedArrayTypes. For details about the example, see createTypedArray() on ArkTS.
    napi\_value typedArrayTypes;
    napi\_create\_object(env, &typedArrayTypes);
    napi\_value typeIndex;
    std::string typeKeys\[\] = {
        "INT8\_ARRAY",   "UINT8\_ARRAY",   "UINT8\_CLAMPED\_ARRAY", "INT16\_ARRAY",      "UINT16\_ARRAY",    "INT32\_ARRAY",
        "UINT32\_ARRAY", "FLOAT32\_ARRAY", "FLOAT64\_ARRAY",       "BIGINT64\_ARRAY", "BIGUINT64\_ARRAY",
    };
    for (int32\_t i = 0; i < sizeof(typeKeys) / sizeof(typeKeys\[0\]); i++) {
        napi\_create\_int32(env, i, &typeIndex);
        napi\_set\_named\_property(env, typedArrayTypes, typeKeys\[i\].c\_str(), typeIndex);
    }
    napi\_property\_descriptor desc\[\] = {
        {"createTypedArray", nullptr, CreateTypedArray, nullptr, nullptr, nullptr, napi\_default, nullptr},
        {"TypedArrayTypes", nullptr, nullptr, nullptr, nullptr, typedArrayTypes, napi\_default, nullptr}
    };
    napi\_define\_properties(env, exports, sizeof(desc) / sizeof(desc\[0\]), desc);
    return exports;
}
EXTERN\_C\_END

## napi\_is\_typedarray

Call **napi\_is\_typedarray** to check whether the **napi\_value** given from ArkTS is a **TypedArray** object.

CPP code:

// Use napi\_is\_typedarray to develop arrays.
static napi\_value IsTypedarray(napi\_env env, napi\_callback\_info info)
{
    // Obtain the parameters passed from ArkTS.
    size\_t argc = 1;
    napi\_value args\[1\] = {nullptr};
    napi\_get\_cb\_info(env, info, &argc, args, nullptr, nullptr);
    // Call napi\_is\_typedarray to check whether the input parameter type is TypedArray.
    bool result = false;
    napi\_status status = napi\_is\_typedarray(env, args\[0\], &result);
    if (status != napi\_ok) {
        napi\_throw\_error(env, nullptr, "Node-API napi\_is\_typedarray fail");
        return nullptr;
    }
    // Convert the result to napi\_value and return it.
    napi\_value returnValue = nullptr;
    napi\_get\_boolean(env, result, &returnValue);

    return returnValue;
}

API declaration:

index.d.ts

export const isTypedarray: (data: Object) => boolean | undefined; // Use napi\_is\_typedarray to develop arrays.

ArkTS code:

// Use napi\_is\_typedarray to develop arrays.
try {
  let value = new Uint8Array(\[1, 2, 3, 4\]);
  let data = "123";
  hilog.info(0x0000, 'testTag', 'Test Node-API napi\_is\_typedarray: %{public}s',
    testNapi.isTypedarray(value));
  hilog.info(0x0000, 'testTag', 'Test Node-API napi\_is\_typedarray: %{public}s',
    testNapi.isTypedarray(data));
  // ...
} catch (error) {
  hilog.error(0x0000, 'testTag', 'Test Node-API napi\_is\_typedarray error: %{public}s', error.message);
  // ...
}

## napi\_get\_typedarray\_info

Call **napi\_get\_typedarray\_info** to obtain properties of a **TypedArray** object.

CPP code:

// Use napi\_get\_typedarray\_info to develop arrays.
static napi\_value GetTypedarrayInfo(napi\_env env, napi\_callback\_info info)
{
    // Obtain and parse the parameters passed from ArkTS. The first parameter is the TypedArray type of the property to obtain, and the second parameter is the enums of the property type to obtain.
    size\_t argc = 2;
    napi\_value args\[2\] = {nullptr};
    napi\_get\_cb\_info(env, info, &argc, args, nullptr, nullptr);
    // Convert the second parameter to the int32 type for comparison.
    int32\_t infoTypeParam;
    napi\_get\_value\_int32(env, args\[1\], &infoTypeParam);
    // Define the InfoType enums in the same sequence as those in ArkTS.
    enum InfoType { INFO\_TYPE = 1, INFO\_LENGTH, INFO\_ARRAY\_BUFFER, INFO\_BYTE\_OFFSET };
    void \*data;
    napi\_typedarray\_type type;
    size\_t byteOffset;
    size\_t length;
    napi\_value arraybuffer;
    // Call napi\_get\_typedarray\_info to obtain TypedArray information.
    napi\_get\_typedarray\_info(env, args\[0\], &type, &length, &data, &arraybuffer, &byteOffset);
    napi\_value result = nullptr;
    // Return the property value based on the property name.
    switch (infoTypeParam) {
        case INFO\_TYPE:
            // If the input parameter is TypedArray data of the int8 type, the value type is napi\_int8\_array.
            napi\_value int8\_type;
            napi\_get\_boolean(env, type == napi\_int8\_array, &int8\_type);
            result = int8\_type;
            break;
        case INFO\_LENGTH:
            // Byte length of elements in TypedArray.
            napi\_value napiLength;
            napi\_create\_int32(env, length, &napiLength);
            result = napiLength;
            break;
        case INFO\_BYTE\_OFFSET:
            // Byte offset of the first TypedArray element in the native array.
            napi\_value napiByteOffset;
            napi\_create\_int32(env, byteOffset, &napiByteOffset);
            result = napiByteOffset;
            break;
        case INFO\_ARRAY\_BUFFER:
            // ArrayBuffer under TypedArray.
            result = arraybuffer;
            break;
        default:
            napi\_throw\_error(env, nullptr, "infoType is not the InfoType");
            break;
    }
    return result;
}

API declaration:

index.d.ts

export const getTypedarrayInfo: <T>(typeArray: T,
  infoType: number) => ArrayBuffer | number | boolean; // Use napi\_get\_typedarray\_info to develop arrays.

ArkTS code:

// Use napi\_get\_typedarray\_info to develop arrays.
// Pass in the TypedArray type. TypedArray is a class array data view used to describe binary data. It does not have a constructor and can be constructed from its child class.
// The child classes of TypedArray include Int8Array, Uint8Array, Uint8ClampedArray, Int16Array, and Int32Array.
let int8Array = new Int8Array(\[15, 7\]);
// Define the InfoType enums, which are the properties of TypedArray.
enum InfoType {
  TYPE = 1, // Type of the TypedArray.
  LENGTH = 2, // Length of the input TypedArray.
  ARRAY\_BUFFER = 3, // ArrayBuffer under TypedArray.
  BYTE\_OFFSET = 4 // Offset of the first ArrayBuffer element in the native array.
};
try {
  let arrBuffer = testNapi.getTypedarrayInfo(int8Array, InfoType.ARRAY\_BUFFER) as ArrayBuffer;
  // Convert arraybuffer to an array.
  let arr = new Array(new Int8Array(arrBuffer));
  hilog.info(0x0000, 'Node-API', 'get\_typedarray\_info\_arraybuffer: %{public}s', arr.toString());
  hilog.info(0x0000, 'Node-API', 'get\_typedarray\_info\_isIn8Array: %{public}s', testNapi.getTypedarrayInfo(int8Array, InfoType.TYPE).toString());
  hilog.info(0x0000, 'Node-API', 'get\_typedarray\_info\_length: %{public}d', testNapi.getTypedarrayInfo(int8Array, InfoType.LENGTH));
  hilog.info(0x0000, 'Node-API', 'get\_typedarray\_info\_byte\_offset: %{public}d', testNapi.getTypedarrayInfo(int8Array, InfoType.BYTE\_OFFSET));
} catch (error) {
  hilog.error(0x0000, 'testTag', 'Test Node-API napi\_get\_typedarray\_info error: %{public}s', error.message);
}

## napi\_create\_dataview

Call **napi\_create\_dataview** to create a **DataView** object to facilitate access and operation of binary data. You need to specify a buffer pointing to the binary data and the number of bytes included.

CPP code:

// Use napi\_create\_dataview to develop arrays.
static napi\_value CreateDataView(napi\_env env, napi\_callback\_info info)
{
    // Obtain the parameters passed from ArkTS.
    size\_t argc = 1;
    napi\_value args\[1\] = {nullptr};
    napi\_value arraybuffer = nullptr;
    napi\_value result = nullptr;
    // Byte length of DataView.
    size\_t byteLength = 12;
    // Offset of the byte.
    size\_t byteOffset = 4;
    // Obtain the parameters of the callback.
    napi\_get\_cb\_info(env, info, &argc, args, nullptr, nullptr);
    // Convert the parameter into the object type.
    napi\_coerce\_to\_object(env, args\[0\], &arraybuffer);
    // Create a DataView object with the specified byte length and offset.
    napi\_status status = napi\_create\_dataview(env, byteLength, arraybuffer, byteOffset, &result);
    if (status != napi\_ok) {
        // Throw an error indicating that the DataView fails to be created.
        napi\_throw\_error(env, nullptr, "Failed to create DataView");
        return nullptr;
    }
    // Obtain the pointer to the DataView object and the length.
    uint8\_t \*data = nullptr;
    size\_t length = 0;
    napi\_get\_dataview\_info(env, result, &length, (void \*\*)&data, nullptr, nullptr);
    // Assign values to DataView.
    for (size\_t i = 0; i < length; i++) {
        data\[i\] = static\_cast<uint8\_t>(i + 1);
    }
    return result;
}

API declaration:

index.d.ts

export const createDataView: (arraybuffer:ArrayBuffer) => DataView | undefined; // Use napi\_create\_dataview to develop arrays.

ArkTS code:

// Use napi\_create\_dataview to develop arrays.
const arrayBuffer = new ArrayBuffer(16);
const dataView = testNapi.createDataView(arrayBuffer) as DataView;
hilog.info(0x0000, 'testTag', 'Test Node-API dataView: %{public}d', dataView.byteLength);
hilog.info(0x0000, 'testTag', 'Test Node-API dataView first data: %{public}d', dataView.getInt8(0));

## napi\_is\_dataview

Call **napi\_is\_dataview** to check whether the **napi\_value** given from ArkTS is a **DataView** object.

CPP code:

// Use napi\_is\_dataview to develop arrays.
static napi\_value IsDataView(napi\_env env, napi\_callback\_info info)
{
    // Obtain the parameters passed from ArkTS.
    size\_t argc = 1;
    napi\_value args\[1\] = {nullptr};
    napi\_get\_cb\_info(env, info, &argc, args, nullptr, nullptr);

    // Call napi\_is\_dataview to check whether the input parameter is a DataView object.
    bool result = false;
    napi\_status status = napi\_is\_dataview(env, args\[0\], &result);
    if (status != napi\_ok) {
        napi\_throw\_error(env, nullptr, "Node-API napi\_is\_dataview fail");
        return nullptr;
    }
    // Convert the result to napi\_value and return it.
    napi\_value returnValue;
    napi\_get\_boolean(env, result, &returnValue);

    return returnValue;
}

API declaration:

index.d.ts

export const isDataView: (date: DataView | string) => boolean | undefined; // Use napi\_is\_dataview to develop arrays.

ArkTS code:

// Use napi\_is\_dataview to develop arrays.
try {
  let buffer = new ArrayBuffer(16);
  let dataView = new DataView(buffer);
  let data = "123";
  hilog.info(0x0000, 'testTag', 'Test Node-API napi\_is\_dataview: %{public}s',
    testNapi.isDataView(dataView));
  hilog.info(0x0000, 'testTag', 'Test Node-API napi\_is\_dataview: %{public}s',
    testNapi.isDataView(data));
  // ...
} catch (error) {
  hilog.error(0x0000, 'testTag', 'Test Node-API napi\_is\_dataview error: %{public}s', error.message);
  // ...
}

## napi\_get\_dataview\_info

Call **napi\_get\_dataview\_info** to obtain properties of a **DataView** object.

CPP code:

// Use napi\_get\_dataview\_info to develop arrays.
static napi\_value GetDataViewInfo(napi\_env env, napi\_callback\_info info)
{
    // Obtain the parameters passed from ArkTS.
    size\_t argc = 2;
    napi\_value args\[2\] = {nullptr};
    napi\_get\_cb\_info(env, info, &argc, args, nullptr, nullptr);
    // Convert the second parameter to an int32 number.
    int32\_t infoType;
    napi\_get\_value\_int32(env, args\[1\], &infoType);
    size\_t byteLength;
    void \*data;
    napi\_value arrayBuffer;
    size\_t byteOffset;
    // Define the InfoType enums in the same sequence as those in ArkTS.
    enum InfoType { BYTE\_LENGTH = 0, ARRAY\_BUFFER, BYTE\_OFFSET };
    // Obtain DataView information.
    napi\_get\_dataview\_info(env, args\[0\], &byteLength, &data, &arrayBuffer, &byteOffset);
    napi\_value result = nullptr;
    switch (infoType) {
        case BYTE\_LENGTH:
            // Return the number of bytes of the DataView object.
            napi\_value napiByteLength;
            napi\_create\_int32(env, byteLength, &napiByteLength);
            result = napiByteLength;
            break;
        case ARRAY\_BUFFER:
            // Return the ArrayBuffer of the DataView object.
            result = arrayBuffer;
            break;
        case BYTE\_OFFSET:
            // Return the byte offset of the DataView object.
            napi\_value napiByteOffset;
            napi\_create\_int32(env, byteOffset, &napiByteOffset);
            result = napiByteOffset;
            break;
        default:
            napi\_throw\_error(env, nullptr, "infoType is not the InfoType");
            break;
    }
    return result;
}

API declaration:

index.d.ts

export const getDataViewInfo: (dataView: DataView,
  infoType: number) => ArrayBuffer | number; // Uses napi\_get\_dataview\_info to develop arrays.

ArkTS code:

// Use napi\_get\_dataview\_info to develop arrays.
// Create an ArrayBuffer object.
let arrayBuffer = new Int8Array(\[2, 5\]).buffer;
// Use arrayBuffer to create a DataView object.
let dataView = new DataView(arrayBuffer);
// Define an enum type.
enum InfoType {
  BYTE\_LENGTH = 0,
  ARRAY\_BUFFER = 1,
  BYTE\_OFFSET = 2,
};
try {
  // Pass in the parameter of DataView to obtain the number of bytes in DataView.
  hilog.info(0x0000, 'Node-API', 'get\_dataview\_info\_bytelength %{public}d', testNapi.getDataViewInfo(dataView, InfoType.BYTE\_LENGTH));
  // Pass in the parameter of DataView to obtain the ArrayBuffer of DataView.
  let arrBuffer = testNapi.getDataViewInfo(dataView, InfoType.ARRAY\_BUFFER) as ArrayBuffer;
  // Convert arraybuffer to an array.
  let arr = Array.from(new Int8Array(arrBuffer));
  hilog.info(0x0000, 'Node-API', 'get\_dataview\_info\_arraybuffer %{public}s', arr.toString());
  // Pass in the parameter of DataView to obtain the byte offset in the data buffer of DataView.
  hilog.info(0x0000, 'Node-API', 'get\_dataview\_info\_byteoffset %{public}d', testNapi.getDataViewInfo(dataView, InfoType.BYTE\_OFFSET));
} catch (error) {
  hilog.error(0x0000, 'testTag', 'Test Node-API napi\_get\_dataview\_info error: %{public}s', error.message);
}

To print logs in the native CPP, add the following information to the **CMakeLists.txt** file and add the header file by using **#include "hilog/log.h"**.

// CMakeLists.txt
add\_definitions( "-DLOG\_DOMAIN=0xd0d0" )
add\_definitions( "-DLOG\_TAG=\\"testTag\\"" )
target\_link\_libraries(entry PUBLIC libace\_napi.z.so libhilog\_ndk.z.so)
