# Working with BigInt Using Node-API

#### Introduction

BigInt is a data type used to represent integers of any precision in ArkTS, with values greater than the value range of the Number type. You can use Node-API to create, obtain, and operate ArkTS BigInt values.

#### Basic Concepts

Before using Node-API to operate BigInt values, you need to understand the following basic concepts:

-   BigInt: a data type used to represent integers of any precision in ArkTS. Unlike the Number type, BigInt can accurately represent very large integers without losing precision or causing overflows.
-   BigInt creation: You can use Node-API to create a ArkTS BigInt object from a C **Int64** or **Uint64** value. This makes it easy to create BigInt values using C/C++.
-   BigInt operation: Node-API provides APIs for operating BigInt values. You can use these APIs to obtain and convert BigInt values and perform arithmetic and bitwise operations.

#### Available APIs

| API | Description |
| :-- | :-- |
| napi\_create\_bigint\_int64 | Creates an ArkTS BigInt object from a signed 64-bit integer in C/C++. |
| napi\_create\_bigint\_uint64 | Creates an ArkTS BigInt object from an unsigned 64-bit integer in C/C++. |
| napi\_create\_bigint\_words | Creates an ArkTS BigInt object from an unsigned 64-bit integer in C/C++. |
| napi\_get\_value\_bigint\_int64 | Obtains a signed 64-bit integer from an ArkTS BigInt object. |
| napi\_get\_value\_bigint\_uint64 | Obtains an unsigned 64-bit integer from an ArkTS BigInt object. |
| napi\_get\_value\_bigint\_words | Obtains the underlying 64-bit unsigned (uint64) integer from an ArkTS BigInt object. |

#### Example

If you are just starting out with Node-API, see [Node-API Development Process](../../node-api-development-process/document.md). The following demonstrates only the C++ and ArkTS code related to BigInt conversions.

The following header files are required for the C++ code:

#include "napi/native\_api.h"
#include "hilog/log.h"

The following modules are required for the ArkTS code:

import { hilog } from '@kit.PerformanceAnalysisKit';
import testNapi from 'libentry.so';

## napi\_create\_bigint\_int64

Use **napi\_create\_bigint\_int64** to create an ArkTS BigInt object from a signed 64-bit integer in C/C++.

CPP code:

// napi\_create\_bigint\_int64
static napi\_value CreateBigintInt64t(napi\_env env, napi\_callback\_info info)
{
    // Declare the int64\_t variable value.
    int64\_t value = -5555555555555555555;
    // Convert the value to the napi\_value type and return napi\_value.
    napi\_value returnValue = nullptr;
    napi\_create\_bigint\_int64(env, value, &returnValue);
    return returnValue;
}

API declaration:

index.d.ts

export const createBigintInt64t: () => bigint; // napi\_create\_bigint\_int64

ArkTS code:

// napi\_create\_bigint\_int64
hilog.info(0x0000, 'testTag', 'Test Node-API napi\_create\_bigint\_int64: %{public}d',
  testNapi.createBigintInt64t());

## napi\_create\_bigint\_uint64

Use **napi\_create\_bigint\_uint64** to create an ArkTS BigInt object from an unsigned 64-bit integer in C/C++.

CPP code:

// napi\_create\_bigint\_uint64
static napi\_value CreateBigintUint64t(napi\_env env, napi\_callback\_info info)
{
    // Declare the uint64\_t variable value.
    uint64\_t value = 5555555555555555555;
    // Convert the value to the napi\_value type and return napi\_value.
    napi\_value returnValue = nullptr;
    napi\_create\_bigint\_uint64(env, value, &returnValue);
    return returnValue;
}

API declaration:

index.d.ts

export const createBigintUint64t: () => bigint; // napi\_create\_bigint\_uint64

ArkTS code:

// napi\_create\_bigint\_uint64
hilog.info(0x0000, 'testTag', 'Test Node-API napi\_create\_bigint\_uint64: %{public}d',
  testNapi.createBigintUint64t());

## napi\_create\_bigint\_words

Use **napi\_create\_bigint\_words** to create an ArkTS BigInt object based on the given byte data.

CPP code:

// napi\_create\_bigint\_words
static napi\_value CreateBigintWords(napi\_env env, napi\_callback\_info info)
{
    // Call napi\_create\_bigint\_words to create a BigInt object.
    int signBit = 0;
    size\_t wordCount = 3;
    uint64\_t words\[\] = {12ULL, 34ULL, 56ULL};
    napi\_value returnValue = nullptr;
    napi\_status status = napi\_create\_bigint\_words(env, signBit, wordCount, words, &returnValue);
    if (status != napi\_ok) {
        napi\_throw\_error(env, nullptr, "napi\_create\_bigint\_words fail");
        return nullptr;
    }
    return returnValue;
}

API declaration:

index.d.ts

export const createBigintWords: () => bigint | undefined; // napi\_create\_bigint\_words

ArkTS code:

// napi\_create\_bigint\_words
try {
  hilog.info(0x0000, 'testTag', 'Test Node-API napi\_create\_bigint\_words: %{public}d',
    testNapi.createBigintWords());
  // ...
} catch (error) {
  hilog.error(0x0000, 'testTag', 'Test Node-API NapiGetValueBigint: %{public}s', error.message);
  // ...
}

## napi\_get\_value\_bigint\_int64

Use **napi\_get\_value\_bigint\_int64** to obtain a signed 64-bit integer from an ArkTS BigInt object.

CPP code:

// napi\_get\_value\_bigint\_int64
static napi\_value GetValueBigintInt64t(napi\_env env, napi\_callback\_info info)
{
    size\_t argc = 1;
    napi\_value args\[1\] = {nullptr};
    napi\_get\_cb\_info(env, info, &argc, args, nullptr, nullptr);
    // Obtain the 64-bit big integer from the input parameter.
    int64\_t value = 0;
    bool lossLess = false;
    napi\_status status = napi\_get\_value\_bigint\_int64(env, args\[0\], &value, &lossLess);
    // Check whether the BigInt value obtained is a product of lossless conversion. If no, throw an exception.
    if (!lossLess) {
        napi\_throw\_error(env, nullptr, "BigInt values have not been lossless converted");
        return nullptr;
    }
    // If the API is successfully called, return true to ArkTS.
    napi\_value returnValue = nullptr;
    if (status == napi\_ok) {
        napi\_get\_boolean(env, true, &returnValue);
        return returnValue;
    } else {
        napi\_throw\_error(env, nullptr, "napi\_get\_value\_bigint\_int64 failed");
        return nullptr;
    }
}

API declaration:

index.d.ts

export const getValueBigintInt64t: (bigInt64: bigint) => boolean | undefined; // napi\_get\_value\_bigint\_int64

ArkTS code:

// napi\_get\_value\_bigint\_int64
let bigInt = BigInt(-5555555555555555);
try {
  hilog.info(0x0000, 'testTag', 'Test Node-API napi\_get\_value\_bigint\_int64: %{public}s',
    JSON.stringify(testNapi.getValueBigintInt64t(bigInt)));
  // ...
} catch (error) {
  hilog.error(0x0000, 'testTag', 'Test Node-API NapiGetValueBigint: %{public}s', error.message);
  // ...
}

## napi\_get\_value\_bigint\_uint64

Use **napi\_get\_value\_bigint\_uint64** to obtain an unsigned 64-bit integer from an ArkTS BigInt object.

CPP code:

// napi\_get\_value\_bigint\_uint64
static napi\_value GetValueBigintUint64t(napi\_env env, napi\_callback\_info info)
{
    size\_t argc = 1;
    napi\_value args\[1\] = {nullptr};
    napi\_get\_cb\_info(env, info, &argc, args, nullptr, nullptr);
    // Obtain the BigInt value.
    uint64\_t value = 0;
    bool lossLess = false;
    napi\_status status = napi\_get\_value\_bigint\_uint64(env, args\[0\], &value, &lossLess);
    // Check whether the BigInt value obtained is a product of lossless conversion. If no, throw an exception.
    if (!lossLess) {
        napi\_throw\_error(env, nullptr, "BigInt values have no lossless converted");
        return nullptr;
    }
    // If the API is successfully called, return true to ArkTS.
    napi\_value returnValue = nullptr;
    napi\_get\_boolean(env, status == napi\_ok, &returnValue);
    return returnValue;
}

API declaration:

index.d.ts

export const getValueBigintUint64t: (bigUint64: bigint) => boolean | undefined; // napi\_get\_value\_bigint\_uint64

ArkTS code:

// napi\_get\_value\_bigint\_uint64
let bigUint = BigInt(5555555555555555);
try {
  hilog.info(0x0000, 'testTag', 'Test Node-API napi\_get\_value\_bigint\_uint64: %{public}s',
    JSON.stringify(testNapi.getValueBigintUint64t(bigUint)));
  // ...
} catch (error) {
  hilog.error(0x0000, 'testTag', 'Test Node-API NapiGetValueBigint: %{public}s', error.message);
  // ...
}

## napi\_get\_value\_bigint\_words

Use **napi\_get\_value\_bigint\_words** to obtain the sign bit and underlying 64-bit unsigned integer array representation from an ArkTS object.

CPP code:

// napi\_get\_value\_bigint\_words
static napi\_value GetValueBigintWords(napi\_env env, napi\_callback\_info info)
{
    size\_t argc = 1;
    napi\_value args\[1\] = {nullptr};
    napi\_get\_cb\_info(env, info, &argc, args, nullptr, nullptr);
    int signBit = 0;
    size\_t wordCount = 0;
    // Call napi\_get\_value\_bigint\_words to obtain wordCount.
    napi\_status status = napi\_get\_value\_bigint\_words(env, args\[0\], nullptr, &wordCount, nullptr);
    OH\_LOG\_INFO(LOG\_APP, "Node-API , wordCount:%{public}d.", wordCount);
    if (status != napi\_ok) {
        OH\_LOG\_ERROR(LOG\_APP, "Node-API , get wordCount fail, status:%{public}d.", status);
        napi\_throw\_error(env, nullptr, "napi\_get\_value\_bigint\_words call failed");
        return nullptr;
    }
    if (wordCount == 0) {
        OH\_LOG\_ERROR(LOG\_APP, "Node-API , wordCount is 0, invalid BigInt or empty value.");
        napi\_throw\_error(env, nullptr, "napi\_get\_value\_bigint\_words returned wordCount 0");
        return nullptr;
    }
    
    const size\_t MAX\_ALLOWED\_WORDS = 1024; // Maximum number of wordCount (service protection, which is adjusted based on the actual scenario). Example: A maximum of 1024 uint64\_t (8 KB) are allowed.
    if (wordCount > MAX\_ALLOWED\_WORDS) {
        OH\_LOG\_ERROR(LOG\_APP, "Node-API , wordCount(%{public}zu) exceeds max limit(%{public}zu)",
            wordCount, MAX\_ALLOWED\_WORDS);
        napi\_throw\_error(env, nullptr, "wordCount is too large");
        return nullptr;
    }
    // Allocate sufficient space to store all words.
    uint64\_t\* words = new uint64\_t\[wordCount\];
    // Call napi\_get\_value\_bigint\_words to obtain BigInt information, such as whether the value passed by signBit is a positive or negative number.
    status = napi\_get\_value\_bigint\_words(env, args\[0\], &signBit, &wordCount, words);
    OH\_LOG\_INFO(LOG\_APP, "Node-API , signBit: %{public}d.", signBit);
    if (status != napi\_ok) {
        OH\_LOG\_ERROR(LOG\_APP, "Node-API , reason:%{public}d.", status);
        delete\[\] words;
        napi\_throw\_error(env, nullptr, "napi\_get\_value\_bigint\_words fail");
        return nullptr;
    }
    // Process the words array, for example, output logs.
    // ...
    // Convert the sign bit into a value of Int type and pass it.
    napi\_value returnValue = nullptr;
    napi\_create\_int32(env, signBit, &returnValue);
    delete\[\] words;
    return returnValue;
}

API declaration:

index.d.ts

export const getValueBigintWords: (bigIntWords: bigint) => bigint | undefined; // napi\_get\_value\_bigint\_words

ArkTS code:

// napi\_get\_value\_bigint\_words
let bigInt = BigInt(-5555555555555555);
let bigUint = BigInt(5555555555555555);
try {
  hilog.info(0x0000, 'testTag', 'Test Node-API napi\_get\_value\_bigint\_words signBit is: %{public}d',
    testNapi.getValueBigintWords(bigInt));
  hilog.info(0x0000, 'testTag', 'Test Node-API napi\_get\_value\_bigint\_words signBit is: %{public}d',
    testNapi.getValueBigintWords(bigUint));
  // ...
} catch (error) {
  hilog.error(0x0000, 'testTag', 'Test Node-API NapiGetValueBigint: %{public}s', error.message);
  // ...
}

To print logs in the native CPP, add the following information to the **CMakeLists.txt** file and add the header file by using **#include "hilog/log.h"**.

// CMakeLists.txt
add\_definitions( "-DLOG\_DOMAIN=0xd0d0" )
add\_definitions( "-DLOG\_TAG=\\"testTag\\"" )
target\_link\_libraries(entry PUBLIC libace\_napi.z.so libhilog\_ndk.z.so)
