# Working with Arrays Using JSVM-API

#### Introduction

JSVM-API provides APIs for directly managing JavaScript (JS) arrays.

#### Basic Concepts

JSVM-API can be used to create, access, modify, and traverse arrays. Before using JSVM-API to work with arrays, it is helpful if you understand the following concepts:

-   Array creation: You can use **OH\_JSVM\_CreateArray** to create an array and pass it to the JS layer.
-   Array-related operations: You can use the APIs provides by the JSVM module to obtain the length of a JS array, retrieve the element at the specified index, and set the element value of the specified index.
-   **TypedArray**: A **TypedArray** object in JS is an array-like view of an underlying binary data buffer. It can be regarded as an array-like data view of the specified type. There is no constructor for **TypedArray** objects, but they can be constructed by their child class constructors. The child classes of **TypedArray** include **Int8Array**, **Uint8Array**, **Uint8ClampedArray**, **Int16Array**, and **Int32Array**.
-   **ArrayBuffer**: **ArrayBuffer** is a data struct used to represent a binary data buffer of fixed length.
-   **DataView**: **DataView** is a JS view that allows a variety of number types to be read and written in an **ArrayBuffer** object.

#### Available APIs

| API | Description |
| :-- | :-- |
| OH\_JSVM\_CreateArray | Creates a JS array object. |
| OH\_JSVM\_CreateArrayWithLength | Creates a JS array object of the specified length. |
| OH\_JSVM\_CreateTypedarray | Creates a JS **TypedArray** object for an **ArrayBuffer**. The TypedArray object provides an array-like view, where each element has the same binary scalar data type. Note that the sum of **length** × **size\_of\_element** and **byte\_offset** must be less than or equal to the array size (in bytes). Otherwise, a **RangeError** exception will be thrown. |
| OH\_JSVM\_CreateDataview | 
Creates a JS **DataView** object based on an existing **ArrayBuffer**. The **DataView** object provides an array-like view on the underlying data buffer. The **ArrayBuffer** allows elements of different sizes and types.

The sum of **byte\_length** and **byte\_offset** must be less than or equal to the array size (in bytes). Otherwise, a **RangeError** exception will be thrown.

 |
| OH\_JSVM\_GetArrayLength | Obtains the length of an array. |
| OH\_JSVM\_GetTypedarrayInfo | Obtains information about a **TypedArray** object. |
| OH\_JSVM\_GetDataviewInfo | Obtains information of a **DataView** object. |
| OH\_JSVM\_IsArray | Checks whether a JS object is an array. |
| OH\_JSVM\_SetElement | Sets an element at the specified index for a JS object. |
| OH\_JSVM\_GetElement | Obtains the element at the specified index of a JS object. |
| OH\_JSVM\_HasElement | Checks whether a JS object has an element at the specified index. |
| OH\_JSVM\_DeleteElement | Deletes the element at the specified index from a JS object. |
| OH\_JSVM\_IsDataview | Checks whether a JS object is a **DataView** object. |
| OH\_JSVM\_IsTypedarray | Checks whether a JS object is a **TypedArray** object. |

#### Example

If you are just starting out with JSVM-API, see [JSVM-API Development Process](../../jsvm-api-development-process/document.md). The following demonstrates only the C++ code involved in array development.

## OH\_JSVM\_CreateArray

Use **OH\_JSVM\_CreateArray** to create a JS array object.

CPP code:

// hello.cpp
#include "napi/native\_api.h"
#include "ark\_runtime/jsvm.h"
#include <hilog/log.h>
// Register the CreateArray callback.
static int DIFF\_VALUE\_FIVE = 5;
// Define OH\_JSVM\_CreateArray.
static JSVM\_Value CreateArray(JSVM\_Env env, JSVM\_CallbackInfo info)
{
    // Create an empty array.
    JSVM\_Value array = nullptr;
    JSVM\_Status status = OH\_JSVM\_CreateArray(env, &array);
    if (status != JSVM\_OK) {
        OH\_LOG\_ERROR(LOG\_APP, "JSVM CreateArray fail");
        return nullptr;
    } else {
        OH\_LOG\_INFO(LOG\_APP, "JSVM CreateArray success");
    }
    // Assign values to the created array.
    for (int i = 0; i < DIFF\_VALUE\_FIVE; i++) {
        JSVM\_Value element;
        JSVM\_CALL(OH\_JSVM\_CreateInt32(env, i, &element));
        JSVM\_CALL(OH\_JSVM\_SetElement(env, array, i, element));
    }
    return array;
}
static JSVM\_CallbackStruct param\[\] = {
    {.data = nullptr, .callback = CreateArray},
};
static JSVM\_CallbackStruct \*method = param;
// Set a property descriptor named createArray and associate it with a callback. This allows the CreateArray callback to be called from JS.
static JSVM\_PropertyDescriptor descriptor\[\] = {
    {"createArray", nullptr, method++, nullptr, nullptr, nullptr, JSVM\_DEFAULT},
};
// Call the C++ code from JS.
const char \*srcCallNative = R"JS(
  function testCreateArray() {
    return createArray();
  }
  testCreateArray();
)JS";

Expected result:

JSVM CreateArray success

## OH\_JSVM\_CreateArrayWithLength

Use **OH\_JSVM\_CreateArrayWithLength** to create a JS array object of the specified length.

CPP code:

// hello.cpp
#include "napi/native\_api.h"
#include "ark\_runtime/jsvm.h"
#include <hilog/log.h>
// Define OH\_JSVM\_CreateArrayWithLength.
static JSVM\_Value CreateArrayWithLength(JSVM\_Env env, JSVM\_CallbackInfo info)
{
    size\_t argc = 1;
    JSVM\_Value argv\[1\] = {nullptr};
    JSVM\_Value result = nullptr;
    // Obtain the callback information.
    OH\_JSVM\_GetCbInfo(env, info, &argc, argv, nullptr, nullptr);
    // Obtain the array length passed.
    int32\_t length = 0;
    OH\_JSVM\_GetValueInt32(env, argv\[0\], &length);
    // Call OH\_JSVM\_CreateArrayWithLength to create an array with the specified length.
    JSVM\_Status status = OH\_JSVM\_CreateArrayWithLength(env, length, &result);
    if (status == JSVM\_OK) {
        // Set an element in the created array.
        for (int32\_t i = 0; i < length; i++) {
            JSVM\_Value value;
            JSVM\_CALL(OH\_JSVM\_CreateInt32(env, i, &value));
            JSVM\_CALL(OH\_JSVM\_SetElement(env, result, i, value));
        }
        OH\_LOG\_INFO(LOG\_APP, "JSVM CreateArrayWithLength success");
    } else {
        OH\_LOG\_ERROR(LOG\_APP, "JSVM CreateArrayWithLength fail");
    }
    return result;
}
// Register the CreateArrayWithLength callback.
static JSVM\_CallbackStruct param\[\] = {
    {.data = nullptr, .callback = CreateArrayWithLength},
};
static JSVM\_CallbackStruct \*method = param;
// Set a property descriptor named createArrayWithLength and associate it with a callback. This allows the CreateArrayWithLength callback to be called from JS.
static JSVM\_PropertyDescriptor descriptor\[\] = {
    {"createArrayWithLength", nullptr, method++, nullptr, nullptr, nullptr, JSVM\_DEFAULT},
};
// Call the C++ code from JS.
const char \*srcCallNative = R"JS(
let num = 7;
function testCreateArrayWithLength(num){
    return createArrayWithLength(num);
}
testCreateArrayWithLength(num);
)JS";

Expected result:

JSVM CreateArrayWithLength success

## OH\_JSVM\_CreateTypedarray

Use **OH\_JSVM\_CreateTypedarray** to create a JS **TypedArray** object based on an **ArrayBuffer**. The **TypedArray** object provides an array-like view over an underlying data buffer, where each element has the same underlying binary scalar data type.

CPP code:

// hello.cpp
#include "napi/native\_api.h"
#include "ark\_runtime/jsvm.h"
#include <hilog/log.h>
// Define OH\_JSVM\_CreateTypedarray.
static int DIFF\_VALUE\_THREE = 3;
static JSVM\_Value CreateTypedArray(JSVM\_Env env, JSVM\_CallbackInfo info)
{
    size\_t argc = 1;
    JSVM\_Value args\[1\] = {nullptr};
    OH\_JSVM\_GetCbInfo(env, info, &argc, args, nullptr, nullptr);
    int32\_t typeNum = 0;
    OH\_JSVM\_GetValueInt32(env, args\[0\], &typeNum);
    JSVM\_TypedarrayType arrayType;
    // Set the element size.
    size\_t elementSize = 0;
    // Convert the value to the JSVM\_TypedarrayType type.
    arrayType = static\_cast<JSVM\_TypedarrayType>(typeNum);
    switch (typeNum) {
        case JSVM\_INT8\_ARRAY:
        case JSVM\_UINT8\_ARRAY:
        case JSVM\_UINT8\_CLAMPED\_ARRAY:
            elementSize = sizeof(int8\_t);
            break;
        case JSVM\_INT16\_ARRAY:
        case JSVM\_UINT16\_ARRAY:
            elementSize = sizeof(int16\_t);
            break;
        case JSVM\_INT32\_ARRAY:
        case JSVM\_UINT32\_ARRAY:
            elementSize = sizeof(int32\_t);
            break;
        case JSVM\_FLOAT32\_ARRAY:
            elementSize = sizeof(float);
            break;
        case JSVM\_FLOAT64\_ARRAY:
            elementSize = sizeof(double);
            break;
        case JSVM\_BIGINT64\_ARRAY:
        case JSVM\_BIGUINT64\_ARRAY:
            elementSize = sizeof(int64\_t);
            break;
        default:
            // By default, an array of the JSVM\_INT8\_ARRAY type is created.
            arrayType = JSVM\_INT8\_ARRAY;
            elementSize = sizeof(int8\_t);
            break;
    }
    size\_t length = DIFF\_VALUE\_THREE;
    JSVM\_Value arrayBuffer = nullptr;
    JSVM\_Value typedArray = nullptr;
    void \*data;
    // Create an ArrayBuffer object.
    OH\_JSVM\_CreateArraybuffer(env, length \* elementSize, (void \*\*)&data, &arrayBuffer);
    // Create a TypedArray object of the specified type.
    JSVM\_Status status = OH\_JSVM\_CreateTypedarray(env, arrayType, length, arrayBuffer, 0, &typedArray);
    if (status != JSVM\_OK) {
        OH\_LOG\_ERROR(LOG\_APP, "JSVM CreateTypedArray fail");
    } else {
        OH\_LOG\_INFO(LOG\_APP, "JSVM CreateTypedArray success");
    }
    return typedArray;
}
// Register the CreateTypedArray callback.
static JSVM\_CallbackStruct param\[\] = {
    {.data = nullptr, .callback = CreateTypedArray},
};
static JSVM\_CallbackStruct \*method = param;
// Set a property descriptor named createTypedArray and associate it with a callback. This allows the CreateTypedArray callback to be called from JS.
static JSVM\_PropertyDescriptor descriptor\[\] = {
    {"createTypedArray", nullptr, method++, nullptr, nullptr, nullptr, JSVM\_DEFAULT},
};
// Call the C++ code from JS.
const char \*srcCallNative = R"JS(
const type = {
    INT8\_ARRAY: 0,
    UINT8\_ARRAY: 1,
    UINT8\_CLAMPED\_ARRAY: 2,
    INT16\_ARRAY: 3,
    UINT16\_ARRAY: 4,
    INT32\_ARRAY: 5,
    UINT32\_ARRAY: 6,
    FLOAT32\_ARRAY: 7,
    FLOAT64\_ARRAY: 8,
    BIGINT64\_ARRAY: 9,
    BIGUINT64\_ARRAY: 10
};
createTypedArray(type.INT8\_ARRAY);
createTypedArray(type.INT32\_ARRAY);
)JS";

Expected result:

JSVM CreateTypedArray success
JSVM CreateTypedArray success

## OH\_JSVM\_CreateDataview

Use **OH\_JSVM\_CreateDataview** to create a JS **DataView** object based on an **ArrayBuffer**. The **DataView** object provides an array-like view over an underlying data buffer.

CPP code:

static int DIFF\_VALUE\_FOUR = 4;
static int DIFF\_VALUE\_TWELVE = 12;
// Define OH\_JSVM\_CreateDataview.
static JSVM\_Value CreateDataView(JSVM\_Env env, JSVM\_CallbackInfo info)
{
    // Obtain the two parameters passed from JS.
    size\_t argc = 2;
    JSVM\_Value args\[2\] = {nullptr};
    JSVM\_Value arrayBuffer = nullptr;
    JSVM\_Value result = nullptr;
    // Byte length of DataView.
    size\_t byteLength = DIFF\_VALUE\_TWELVE;
    // Offset of the byte.
    size\_t byteOffset = DIFF\_VALUE\_FOUR;
    // Obtain the parameters of the callback.
    OH\_JSVM\_GetCbInfo(env, info, &argc, args, nullptr, nullptr);
    // Convert the parameter into the object type.
    OH\_JSVM\_CoerceToObject(env, args\[0\], &arrayBuffer);
    // Create a DataView object with the specified byte length and offset.
    JSVM\_Status status = OH\_JSVM\_CreateDataview(env, byteLength, arrayBuffer, byteOffset, &result);
    // Obtain the pointer to the DataView object and the length.
    uint8\_t \*data = nullptr;
    // Assign values to DataView.
    int32\_t infoType = 0;
    OH\_JSVM\_GetValueInt32(env, args\[1\], &infoType);
    size\_t returnLength = 0;
    JSVM\_Value returnArrayBuffer = nullptr;
    size\_t returnOffset = 0;
    enum InfoType { BYTE\_LENGTH, ARRAY\_BUFFER, BYTE\_OFFSET };
    // Obtain DataView information.
    OH\_JSVM\_GetDataviewInfo(env, result, &returnLength, (void \*\*)&data, &returnArrayBuffer, &returnOffset);
    JSVM\_Value returnResult = nullptr;
    switch (infoType) {
        case BYTE\_LENGTH:
            JSVM\_Value len;
            JSVM\_CALL(OH\_JSVM\_CreateInt32(env, returnLength, &len));
            returnResult = len;
            if (status != JSVM\_OK) {
                OH\_LOG\_ERROR(LOG\_APP, "JSVM CreateDataView fail");
            } else {
                OH\_LOG\_INFO(LOG\_APP, "JSVM CreateDataView success, returnLength: %{public}d", returnLength);
            }
            break;
        case ARRAY\_BUFFER:
            {
                bool isArraybuffer = false;
                JSVM\_CALL(OH\_JSVM\_IsArraybuffer(env, returnArrayBuffer, &isArraybuffer));
                JSVM\_Value isArray;
                OH\_JSVM\_GetBoolean(env, isArraybuffer, &isArray);
                returnResult = isArray;
                if (status != JSVM\_OK) {
                    OH\_LOG\_ERROR(LOG\_APP, "JSVM CreateDataView fail");
                } else {
                    OH\_LOG\_INFO(LOG\_APP, "JSVM CreateDataView success, isArraybuffer: %{public}d", isArraybuffer);
                }
                break;
            }
        case BYTE\_OFFSET:
            JSVM\_Value offset;
            JSVM\_CALL(OH\_JSVM\_CreateInt32(env, returnOffset, &offset));
            returnResult = offset;
            if (status != JSVM\_OK) {
                OH\_LOG\_ERROR(LOG\_APP, "JSVM CreateDataView fail");
            } else {
                OH\_LOG\_INFO(LOG\_APP, "JSVM CreateDataView success, returnOffset: %{public}d", returnOffset);
            }
            break;
        default:
            break;
    }
    return returnResult;
}
// Register the CreateDataView callback.
static JSVM\_CallbackStruct param\[\] = {
    {.data = nullptr, .callback = CreateDataView},
};
static JSVM\_CallbackStruct \*method = param;
// Set a property descriptor named createDataView and associate it with a callback. This allows the CreateDataView callback to be called from JS.
static JSVM\_PropertyDescriptor descriptor\[\] = {
    {"createDataView", nullptr, method++, nullptr, nullptr, nullptr, JSVM\_DEFAULT},
};
// Call the C++ code from JS.
const char \*srcCallNative = R"JS(
 let BYTE\_LENGTH = 0;
 createDataView(new ArrayBuffer(16), BYTE\_LENGTH);
 let IS\_ARRAYBUFFER = 1;
 createDataView(new ArrayBuffer(16), IS\_ARRAYBUFFER);
 let BYTE\_OFFSET = 2;
 createDataView(new ArrayBuffer(16), BYTE\_OFFSET);
)JS";

Expected result:

CreateDataView success, returnLength: 12
JSVM CreateDataView success, isArraybuffer: 1
JSVM CreateDataView success, returnOffset: 4

## OH\_JSVM\_GetArrayLength

Use **OH\_JSVM\_GetArrayLength** to obtain the length of an array.

CPP code:

// hello.cpp
#include "napi/native\_api.h"
#include "ark\_runtime/jsvm.h"
#include <hilog/log.h>
// Define OH\_JSVM\_GetArrayLength.
static JSVM\_Value GetArrayLength(JSVM\_Env env, JSVM\_CallbackInfo info)
{
    size\_t argc = 1;
    JSVM\_Value args\[1\] = {nullptr};
    JSVM\_Value result = nullptr;
    // Initialize length.
    uint32\_t length = 0;
    OH\_JSVM\_GetCbInfo(env, info, &argc, args, nullptr, nullptr);
    // Check whether the parameter is an array.
    bool isArray = false;
    OH\_JSVM\_IsArray(env, args\[0\], &isArray);
    if (!isArray) {
        OH\_LOG\_INFO(LOG\_APP, "JSVM Argument must be an array");
        return nullptr;
    }
    /\*
     \* If the array length is successfully obtained, length is assigned to the actual JSArray length, and the API returns the JSVM\_OK status code.
     \* If args\[0\] is not of the JSArray type, for example, args\[0\] is a proxy object, the length cannot be obtained.
     \* In this case, length remains unchanged, and the JSVM\_ARRAY\_EXPECTED status code is returned.
     \*/
    JSVM\_Status status = OH\_JSVM\_GetArrayLength(env, args\[0\], &length);
    if (status == JSVM\_OK) {
        // Create a return value.
        JSVM\_CALL(OH\_JSVM\_CreateInt32(env, length, &result));
        OH\_LOG\_INFO(LOG\_APP, "JSVM length: %{public}d", length);
    }
    return result;
}
// Register the GetArrayLength callback.
static JSVM\_CallbackStruct param\[\] = {
    {.data = nullptr, .callback = GetArrayLength},
};
static JSVM\_CallbackStruct \*method = param;
// Set a property descriptor named getArrayLength and associate it with a callback. This allows the GetArrayLength callback to be called from JS.
static JSVM\_PropertyDescriptor descriptor\[\] = {
    {"getArrayLength", nullptr, method++, nullptr, nullptr, nullptr, JSVM\_DEFAULT},
};
// Call the C++ code from JS.
const char \*srcCallNative = R"JS(
let data = \[0, 1, 2, 3, 4, 5\];
getArrayLength(data);
)JS";

Expected result:

JSVM length: 6

## OH\_JSVM\_GetTypedarrayInfo

Use **OH\_JSVM\_GetTypedarrayInfo** to obtain information about a **TypedArray** object.

CPP code:

// hello.cpp
#include "napi/native\_api.h"
#include "ark\_runtime/jsvm.h"
#include <hilog/log.h>
// Define OH\_JSVM\_GetTypedarrayInfo.
static JSVM\_Value GetTypedArrayInfo(JSVM\_Env env, JSVM\_CallbackInfo info)
{
    // Obtain and parse the parameters passed to a JS callback within a JSVM. The first parameter is the TypedArray type of the information to obtain, and the second parameter is the enums of the information type to obtain.
    size\_t argc = 2;
    JSVM\_Value args\[2\] = {nullptr};
    OH\_JSVM\_GetCbInfo(env, info, &argc, args, nullptr, nullptr);

    // Convert the second parameter to the int32 type for comparison.
    int32\_t infoTypeParam = 0;
    OH\_JSVM\_GetValueInt32(env, args\[1\], &infoTypeParam);
    // Define the infoType enums in the same sequence as those in ArkTS.
    enum InfoType { INFO\_TYPE, INFO\_LENGTH, INFO\_ARRAY\_BUFFER, INFO\_BYTE\_OFFSET };
    void \*data;
    JSVM\_TypedarrayType type;
    size\_t byteOffset = 0;
    size\_t length = 0;
    JSVM\_Value arrayBuffer = nullptr;
    // Call OH\_JSVM\_GetTypedarrayInfo to obtain TypedArray information.
    JSVM\_Status status = OH\_JSVM\_GetTypedarrayInfo(env, args\[0\], &type, &length, &data, &arrayBuffer, &byteOffset);
    JSVM\_Value result = nullptr;
    // Return the property value based on the property name.
    switch (infoTypeParam) {
        case INFO\_TYPE:
            // If the input parameter is TypedArray data of the int8 type, the value type is JSVM\_INT8\_ARRAY.
            JSVM\_Value int8\_type;
            OH\_JSVM\_GetBoolean(env, type == JSVM\_INT8\_ARRAY, &int8\_type);
            result = int8\_type;
            if (status != JSVM\_OK) {
                OH\_LOG\_ERROR(LOG\_APP, "JSVM GetTypedArrayInfo fail");
            } else {
                OH\_LOG\_INFO(
                    LOG\_APP, "JSVM GetTypedArrayInfo success, JSVM\_INT8\_ARRAY: %{public}d", type == JSVM\_INT8\_ARRAY);
            }
            break;
        case INFO\_LENGTH:
            // Number of elements in the TypedArray object.
            JSVM\_Value jsvmLength;
            JSVM\_CALL(OH\_JSVM\_CreateInt32(env, length, &jsvmLength));
            result = jsvmLength;
            if (status != JSVM\_OK) {
                OH\_LOG\_ERROR(LOG\_APP, "JSVM GetTypedArrayInfo fail");
            } else {
                OH\_LOG\_INFO(LOG\_APP, "JSVM GetTypedArrayInfo success, length: %{public}d", length);
            }
            break;
        case INFO\_BYTE\_OFFSET:
            // Byte offset of the first TypedArray element in the native array.
            JSVM\_Value jsvmOffset;
            JSVM\_CALL(OH\_JSVM\_CreateInt32(env, byteOffset, &jsvmOffset));
            result = jsvmOffset;
            if (status != JSVM\_OK) {
                OH\_LOG\_ERROR(LOG\_APP, "JSVM GetTypedArrayInfo fail");
            } else {
                OH\_LOG\_INFO(LOG\_APP, "JSVM GetTypedArrayInfo success, byteOffset: %{public}d", byteOffset);
            }
            break;
        case INFO\_ARRAY\_BUFFER:
            {
                // ArrayBuffer under TypedArray.
                bool isArrayBuffer = false;
                JSVM\_CALL(OH\_JSVM\_IsArraybuffer(env, arrayBuffer, &isArrayBuffer));
                JSVM\_Value isArray;
                OH\_JSVM\_GetBoolean(env, isArrayBuffer, &isArray);
                result = isArray;
                if (status != JSVM\_OK) {
                    OH\_LOG\_ERROR(LOG\_APP, "JSVM GetTypedArrayInfo fail");
                } else {
                    OH\_LOG\_INFO(LOG\_APP, "JSVM GetTypedArrayInfo success, isArrayBuffer: %{public}d", isArrayBuffer);
                }
                break;
            }
        default:
            break;
    }
    return result;
}
// Register the GetTypedArrayInfo callback.
static JSVM\_CallbackStruct param\[\] = {
    {.data = nullptr, .callback = GetTypedArrayInfo},
};
static JSVM\_CallbackStruct \*method = param;
// Set a property descriptor named getTypedArrayInfo and associate it with a callback. This allows the GetTypedArrayInfo callback to be called from JS.
static JSVM\_PropertyDescriptor descriptor\[\] = {
    {"getTypedArrayInfo", nullptr, method++, nullptr, nullptr, nullptr, JSVM\_DEFAULT},
};
// Call the C++ code from JS.
const char \*srcCallNative = R"JS(
// is JSVM\_INT8\_ARRAY
getTypedArrayInfo(new Int8Array(3), 0);
// Length
getTypedArrayInfo(new Int8Array(5), 1);
// is\_arraybuffer
getTypedArrayInfo(new Int8Array(5), 2);
// Byte offset.
getTypedArrayInfo(new Int8Array(1), 3);
)JS";

Expected result:

JSVM GetTypedArrayInfo success, JSVM\_INT8\_ARRAY: 1
JSVM GetTypedArrayInfo success, length: 5
JSVM GetTypedArrayInfo success, isArrayBuffer: 1
JSVM GetTypedArrayInfo success, byteOffset: 0

## OH\_JSVM\_GetDataviewInfo

Use **OH\_JSVM\_GetDataviewInfo** to obtain information about a **DataView** object.

CPP code:

// hello.cpp
#include "napi/native\_api.h"
#include "ark\_runtime/jsvm.h"
#include <hilog/log.h>
// Define OH\_JSVM\_GetDataviewInfo.
static JSVM\_Value GetDataViewInfo(JSVM\_Env env, JSVM\_CallbackInfo info)
{
    // Obtain and parse the parameters passed to a JS callback within a JSVM. The first parameter is the DataView type of the information to obtain, and the second parameter is the enums of the information type to obtain.
    size\_t argc = 2;
    JSVM\_Value args\[2\] = {nullptr};
    OH\_JSVM\_GetCbInfo(env, info, &argc, args, nullptr, nullptr);
    // Convert the second parameter to an int32 number.
    int32\_t infoType = 0;
    OH\_JSVM\_GetValueInt32(env, args\[1\], &infoType);
    size\_t byteLength = 0;
    void \*data;
    JSVM\_Value arrayBuffer = nullptr;
    size\_t byteOffset = 0;
    // Define the infoType enums in the same sequence as those in ArkTS.
    enum infoTypeEnum { BYTE\_LENGTH, ARRAY\_BUFFER, BYTE\_OFFSET };
    // Obtain DataView information.
    JSVM\_Status status = OH\_JSVM\_GetDataviewInfo(env, args\[0\], &byteLength, &data, &arrayBuffer, &byteOffset);
    JSVM\_Value result = nullptr;
    switch (infoType) {
        case BYTE\_LENGTH:
            // Return the length of DataView.
            JSVM\_Value len;
            JSVM\_CALL(OH\_JSVM\_CreateInt32(env, byteLength, &len));
            result = len;
            if (status != JSVM\_OK) {
                OH\_LOG\_ERROR(LOG\_APP, "JSVM GetDataViewInfo fail");
            } else {
                OH\_LOG\_INFO(LOG\_APP, "JSVM GetDataViewInfo success, byteLength: %{public}d", byteLength);
            }
            break;
        case ARRAY\_BUFFER:
            {
                // Check whether data in Info of DataView is an ArrayBuffer object.
                bool isArrayBuffer = false;
                JSVM\_CALL(OH\_JSVM\_IsArraybuffer(env, arrayBuffer, &isArrayBuffer));
                JSVM\_Value isArray;
                OH\_JSVM\_GetBoolean(env, isArrayBuffer, &isArray);
                result = isArray;
                if (status != JSVM\_OK) {
                    OH\_LOG\_ERROR(LOG\_APP, "JSVM GetDataViewInfo fail");
                } else {
                    OH\_LOG\_INFO(LOG\_APP, "JSVM GetDataViewInfo success, isArrayBuffer: %{public}d", isArrayBuffer);
                }
                break;
            }
        case BYTE\_OFFSET:
            // Return the offset of DataView.
            JSVM\_Value offset;
            JSVM\_CALL(OH\_JSVM\_CreateInt32(env, byteOffset, &offset));
            result = offset;
            if (status != JSVM\_OK) {
                OH\_LOG\_ERROR(LOG\_APP, "JSVM GetDataViewInfo fail");
            } else {
                OH\_LOG\_INFO(LOG\_APP, "JSVM GetDataViewInfo success, byteOffset: %{public}d", byteOffset);
            }
            break;
        default:
            break;
    }
    return result;
}
// Register the GetDataViewInfo callback.
static JSVM\_CallbackStruct param\[\] = {
    {.data = nullptr, .callback = GetDataViewInfo},
};
static JSVM\_CallbackStruct \*method = param;
// Set a property descriptor named getDataViewInfo and associate it with a callback. This allows the GetDataViewInfo callback to be called from JS.
static JSVM\_PropertyDescriptor descriptor\[\] = {
    {"getDataViewInfo", nullptr, method++, nullptr, nullptr, nullptr, JSVM\_DEFAULT},
};
// Call the C++ code from JS.
const char \*srcCallNative = R"JS(
// Byte length.
getDataViewInfo(new DataView(new Int8Array(\[2,5\]).buffer), 0);
// Check whether the data is an ArrayBuffer object.
let data = 'a';
let isarraybuffer = 1;
getDataViewInfo(data, isarraybuffer);
// Check whether the data is an ArrayBuffer object.
data = new DataView(new Int8Array(\[2,5,3\]).buffer);
isarraybuffer = 1;
getDataViewInfo(data, isarraybuffer);
// byte\_offset
data = new DataView(new Int8Array(\[2,5,3\]).buffer);
isarraybuffer = 2;
getDataViewInfo(data, isarraybuffer);
)JS";

Expected result:

JSVM GetDataViewInfo success, byteLength: 2
JSVM GetDataViewInfo fail
JSVM GetDataViewInfo success, isArrayBuffer: 1
JSVM GetDataViewInfo success, byteOffset: 0

## OH\_JSVM\_IsArray

Use **OH\_JSVM\_IsArray** to check whether a JS object is an array.

CPP code:

// hello.cpp
#include "napi/native\_api.h"
#include "ark\_runtime/jsvm.h"
#include <hilog/log.h>
// Define OH\_JSVM\_IsArray.
static JSVM\_Value IsArray(JSVM\_Env env, JSVM\_CallbackInfo info)
{
    size\_t argc = 1;
    JSVM\_Value args\[1\] = {nullptr};
    OH\_JSVM\_GetCbInfo(env, info, &argc, args, nullptr, nullptr);
    bool result = false;
    JSVM\_Status status = OH\_JSVM\_IsArray(env, args\[0\], &result);
    JSVM\_Value returnValue = nullptr;
    JSVM\_CALL(OH\_JSVM\_GetBoolean(env, result, &returnValue));
    if (status != JSVM\_OK) {
        OH\_LOG\_ERROR(LOG\_APP, "JSVM IsArray fail");
    } else {
        OH\_LOG\_INFO(LOG\_APP, "JSVM IsArray success, IsArray: %{public}d", result);
    }
    return returnValue;
}
// Register the IsArray callback.
static JSVM\_CallbackStruct param\[\] = {
    {.data = nullptr, .callback = IsArray},
};
static JSVM\_CallbackStruct \*method = param;
// Set a property descriptor named isArray and associate it with a callback. This allows the IsArray callback to be called from JS.
static JSVM\_PropertyDescriptor descriptor\[\] = {
    {"isArray", nullptr, method++, nullptr, nullptr, nullptr, JSVM\_DEFAULT},
};
// Call the C++ code from JS.
const char \*srcCallNative = R"JS(
let data = \[1, 2, 3, 4, 5\];
isArray(data);
)JS";

Expected result:

JSVM IsArray success, IsArray: 1

## OH\_JSVM\_SetElement

Use **OH\_JSVM\_SetElement** to set an element at the specified index for a JS object.

CPP code:

// hello.cpp
#include "napi/native\_api.h"
#include "ark\_runtime/jsvm.h"
#include <hilog/log.h>
// Define OH\_JSVM\_SetElement.
static int DIFF\_VALUE\_THREE = 3;
static JSVM\_Value SetElement(JSVM\_Env env, JSVM\_CallbackInfo info)
{
    size\_t argc = DIFF\_VALUE\_THREE;
    JSVM\_Value args\[3\] = {nullptr};
    OH\_JSVM\_GetCbInfo(env, info, &argc, args, nullptr, nullptr);
    int32\_t index = 0;
    OH\_JSVM\_GetValueInt32(env, args\[1\], &index);
    JSVM\_Status status = OH\_JSVM\_SetElement(env, args\[0\], index, args\[2\]);
    if (status != JSVM\_OK) {
        OH\_LOG\_ERROR(LOG\_APP, "JSVM SetElement fail");
    } else {
        OH\_LOG\_INFO(LOG\_APP, "JSVM SetElement success");
    }
    return args\[0\];
}
// Register the SetElement callback.
static JSVM\_CallbackStruct param\[\] = {
    {.data = nullptr, .callback = SetElement},
};
static JSVM\_CallbackStruct \*method = param;
// Set a property descriptor named setElement and associate it with a callback. This allows the SetElement callback to be called from JS.
static JSVM\_PropertyDescriptor descriptor\[\] = {
    {"setElement", nullptr, method++, nullptr, nullptr, nullptr, JSVM\_DEFAULT},
};
// Call the C++ code from JS.
const char \*srcCallNative = R"JS(
let data = \[1, 2, 3, 4, 5\];
setElement(data, 3, undefined);
)JS";

Expected result:

JSVM SetElement success

## OH\_JSVM\_GetElement

Use **OH\_JSVM\_GetElement** to obtain the element at the specified index of a JS object.

CPP code:

// hello.cpp
#include "napi/native\_api.h"
#include "ark\_runtime/jsvm.h"
#include <hilog/log.h>
// Define OH\_JSVM\_GetElement.
static JSVM\_Value GetElement(JSVM\_Env env, JSVM\_CallbackInfo info) {
    // Obtain the two parameters passed from JS.
    size\_t argc = 2;
    JSVM\_Value args\[2\] = {nullptr};
    OH\_JSVM\_GetCbInfo(env, info, &argc, args, nullptr, nullptr);
    // Obtain the index value of the element.
    uint32\_t index = 0;
    OH\_JSVM\_GetValueUint32(env, args\[1\], &index);
    // Obtain the element value at the index and store it in result.
    JSVM\_Value result = nullptr;
    JSVM\_Status status = OH\_JSVM\_GetElement(env, args\[0\], index, &result);
    if (status != JSVM\_OK) {
        OH\_LOG\_ERROR(LOG\_APP, "JSVM GetElement fail");
    } else {
        OH\_LOG\_INFO(LOG\_APP, "JSVM GetElement success");
    }
    return result;
}
// Register the GetElement callback.
static JSVM\_CallbackStruct param\[\] = {
    {.data = nullptr, .callback = GetElement},
};
static JSVM\_CallbackStruct \*method = param;
// Set a property descriptor named getElement and associate it with a callback. This allows the GetElement callback to be called from JS.
static JSVM\_PropertyDescriptor descriptor\[\] = {
    {"getElement", nullptr, method++, nullptr, nullptr, nullptr, JSVM\_DEFAULT},
};
// Call the C++ code from JS.
const char \*srcCallNative = R"JS(
let arr = \[10, 'hello', null, true\];
getElement(arr, 3);
)JS";

Expected result:

JSVM GetElement success

## OH\_JSVM\_HasElement

Use **OH\_JSVM\_HasElement** to check whether a JS object has an element at the specified index.

CPP code:

// hello.cpp
#include "napi/native\_api.h"
#include "ark\_runtime/jsvm.h"
#include <hilog/log.h>
// Define OH\_JSVM\_HasElement.
static JSVM\_Value HasElement(JSVM\_Env env, JSVM\_CallbackInfo info) {
    // Obtain the two parameters passed from JS.
    size\_t argc = 2;
    JSVM\_Value args\[2\] = {nullptr};
    OH\_JSVM\_GetCbInfo(env, info, &argc, args, nullptr, nullptr);
    // Obtain the index of the element to be checked.
    uint32\_t index = 0;
    OH\_JSVM\_GetValueUint32(env, args\[1\], &index);
    // Check whether the element exists based on the given index.
    bool hasElement = true;
    JSVM\_Status status = OH\_JSVM\_HasElement(env, args\[0\], index, &hasElement);
    // Convert the boolean value to JSVM\_Value and return it.
    JSVM\_Value result = nullptr;
    if (status != JSVM\_OK) {
        OH\_LOG\_ERROR(LOG\_APP, "JSVM hasElement fail");
    } else {
        OH\_JSVM\_GetBoolean(env, hasElement, &result);
        OH\_LOG\_INFO(LOG\_APP, "JSVM hasElement: %{public}d", hasElement);
    }
    return result;
}
// Register the HasElement callback.
static JSVM\_CallbackStruct param\[\] = {
    {.data = nullptr, .callback = HasElement},
};
static JSVM\_CallbackStruct \*method = param;
// Set a property descriptor named hasElement and associate it with a callback. This allows the HasElement callback to be called from JS.
static JSVM\_PropertyDescriptor descriptor\[\] = {
    {"hasElement", nullptr, method++, nullptr, nullptr, nullptr, JSVM\_DEFAULT},
};
// Call the C++ code from JS.
const char \*srcCallNative = R"JS(
let arr = \[10, 'hello', null, true\];
hasElement(arr, 0);
hasElement(arr, 4);
)JS";

Expected result:

JSVM hasElement: 1
JSVM hasElement: 0

## OH\_JSVM\_DeleteElement

Use **OH\_JSVM\_DeleteElement** to delete the element at the specified index from a JS object.

CPP code:

// hello.cpp
#include "napi/native\_api.h"
#include "ark\_runtime/jsvm.h"
#include <hilog/log.h>
// Define OH\_JSVM\_DeleteElement.
static JSVM\_Value DeleteElement(JSVM\_Env env, JSVM\_CallbackInfo info) {
    // Obtain the two parameters passed from JS.
    size\_t argc = 2;
    JSVM\_Value args\[2\] = {nullptr};
    JSVM\_CALL(OH\_JSVM\_GetCbInfo(env, info, &argc, args, nullptr, nullptr));
    // Obtain the index of the element to delete.
    uint32\_t index = 0;
    JSVM\_CALL(OH\_JSVM\_GetValueUint32(env, args\[1\], &index));
    // Delete the element at the specified index.
    bool deleted = true;
    JSVM\_Status status = OH\_JSVM\_DeleteElement(env, args\[0\], index, &deleted);
    // Convert the boolean value to JSVM\_Value and return it.
    JSVM\_Value result = nullptr;
    if (status != JSVM\_OK) {
        OH\_LOG\_ERROR(LOG\_APP, "JSVM DeleteElement fail");
    } else {
        OH\_JSVM\_GetBoolean(env, deleted, &result);
        OH\_LOG\_INFO(LOG\_APP, "JSVM DeleteElement: %{public}d", deleted);
    }
    return result;
}
// Register the DeleteElement callback.
static JSVM\_CallbackStruct param\[\] = {
    {.data = nullptr, .callback = DeleteElement},
};
static JSVM\_CallbackStruct \*method = param;
// Set a property descriptor named deleteElement and associate it with a callback. This allows the DeleteElement callback to be called from JS.
static JSVM\_PropertyDescriptor descriptor\[\] = {
    {"deleteElement", nullptr, method++, nullptr, nullptr, nullptr, JSVM\_DEFAULT},
};
// Call the C++ code from JS.
const char \*srcCallNative = R"JS(
let arr = \[10, 'hello', null, true\];
deleteElement(arr, 0);
)JS";

Expected result:

JSVM DeleteElement: 1

## OH\_JSVM\_IsDataview

Use **OH\_JSVM\_IsDataview** to check whether a JS object is a **DataView** object.

CPP code:

// hello.cpp
#include "napi/native\_api.h"
#include "ark\_runtime/jsvm.h"
#include <hilog/log.h>
// Define OH\_JSVM\_IsDataview.
static JSVM\_Value IsDataView(JSVM\_Env env, JSVM\_CallbackInfo info) {
    size\_t argc = 1;
    JSVM\_Value args\[1\] = {nullptr};
    OH\_JSVM\_GetCbInfo(env, info, &argc, args, nullptr, nullptr);
    // Call OH\_JSVM\_IsDataview to check whether the input parameter is a DataView object.
    bool result = false;
    JSVM\_Status status = OH\_JSVM\_IsDataview(env, args\[0\], &result);
    JSVM\_Value isDataView = nullptr;
    OH\_JSVM\_GetBoolean(env, result, &isDataView);
    if (status != JSVM\_OK) {
        OH\_LOG\_ERROR(LOG\_APP, "JSVM IsDataView fail");
    } else {
        OH\_LOG\_INFO(LOG\_APP, "JSVM IsDataView: %{public}d", result);
    }
    return isDataView;
}
// Register the IsDataView callback.
static JSVM\_CallbackStruct param\[\] = {
    {.data = nullptr, .callback = IsDataView},
};
static JSVM\_CallbackStruct \*method = param;
// Set a property descriptor named isDataView and associate it with a callback. This allows the IsDataView callback to be called from JS.
static JSVM\_PropertyDescriptor descriptor\[\] = {
    {"isDataView", nullptr, method++, nullptr, nullptr, nullptr, JSVM\_DEFAULT},
};
// Call the C++ code from JS.
const char \*srcCallNative = R"JS(
let buffer = new ArrayBuffer(16);
let dataView = new DataView(buffer);
isDataView(dataView);
)JS";

Expected result:

JSVM IsDataView: 1

## OH\_JSVM\_IsTypedarray

Use **OH\_JSVM\_IsTypedarray** to check whether a JS object is an **TypedArray** object.

CPP code:

// hello.cpp
#include "napi/native\_api.h"
#include "ark\_runtime/jsvm.h"
#include <hilog/log.h>
// Define OH\_JSVM\_IsTypedarray.
static JSVM\_Value IsTypedarray(JSVM\_Env env, JSVM\_CallbackInfo info) {
    size\_t argc = 1;
    JSVM\_Value args\[1\] = {nullptr};
    OH\_JSVM\_GetCbInfo(env, info, &argc, args, nullptr, nullptr);
    bool result = false;
    JSVM\_Status status = OH\_JSVM\_IsTypedarray(env, args\[0\], &result);
    JSVM\_Value isTypedArray = nullptr;
    OH\_JSVM\_GetBoolean(env, result, &isTypedArray);
    if (status != JSVM\_OK) {
        OH\_LOG\_ERROR(LOG\_APP, "JSVM IsTypedarray fail");
    } else {
        OH\_LOG\_INFO(LOG\_APP, "JSVM IsTypedarray: %{public}d", result);
    }
    return isTypedArray;
}
// Register the IsTypedarray callback.
static JSVM\_CallbackStruct param\[\] = {
    {.data = nullptr, .callback = IsTypedarray},
};
static JSVM\_CallbackStruct \*method = param;
// Set a property descriptor named isTypedarray and associate it with a callback. This allows the IsTypedarray callback to be called from JS.
static JSVM\_PropertyDescriptor descriptor\[\] = {
    {"isTypedarray", nullptr, method++, nullptr, nullptr, nullptr, JSVM\_DEFAULT},
};
// Call the C++ code from JS.
const char \*srcCallNative = R"JS(
isTypedarray(new Uint16Array(\[1, 2, 3, 4\]));
)JS";

Expected result:

JSVM IsTypedarray: 1
