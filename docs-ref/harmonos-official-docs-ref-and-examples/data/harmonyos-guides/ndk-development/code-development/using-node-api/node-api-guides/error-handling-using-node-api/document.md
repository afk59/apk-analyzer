# Error Handling Using Node-API

#### Introduction

Node-API provides APIs for handling errors occurred in ArkTS code via exceptions. Properly using these APIs helps improve module stability and reliability.

#### Basic Concepts

Exceptions and errors are common concepts in ArkTS programming. An exception indicates the presence of an unexpected condition, and an error indicates that the application cannot perform certain operations correctly. Node-API provides a set of APIs for handling errors occurred in ArkTS code via exceptions. Read on the following to learn basic concepts related to error handling:

-   Exception: indicates an unexpected condition that may occur during the execution of an application. It can be a syntax error, runtime error, or logic error. For example, the division of a non-zero value with zero and an operation on undefined variables are exceptions.
-   Error: indicates that the application cannot perform some operations. Errors can be defined by the underlying system, API, or developer.
-   **TypeError**: indicates that the type of an operation or value does not meet the expectation. Generally, this error is caused by an incorrect data type.
-   **RangeError**: indicates that a value is not in the expected range. For example, an index beyond the array length is accessed.

These concepts are important in exception and error handling. Properly using methods to capture, handle, or report exceptions and errors help improve application stability.

#### Available APIs

The following table lists the APIs provided by the Node-API module for handling ArkTS errors and exceptions in C/C++. Procedure:

| API | Description |
| :-- | :-- |
| napi\_create\_error, napi\_create\_type\_error, napi\_create\_range\_error | Creates an error, which can be thrown to ArkTS using **napi\_throw**. |
| napi\_throw | Throws the ArkTS error object created by **napi\_create\_error** or obtained by **napi\_get\_last\_error\_info**. |
| napi\_throw\_error, napi\_throw\_type\_error, napi\_throw\_range\_error | Throws an ArkTS error occurred in C/C++. |
| napi\_is\_error | Checks whether a **napi\_value** is an error object. |
| napi\_get\_and\_clear\_last\_exception | Obtains and clears the latest exception. |
| napi\_is\_exception\_pending | Checks whether there is a pending exception. |
| napi\_fatal\_error | Raises a fatal error to terminate the process immediately. |
| napi\_fatal\_exception | Throws a fatal exception, terminates the process, and generates a crash log. |

#### Example

If you are just starting out with Node-API, see [Node-API Development Process](../../node-api-development-process/document.md). The following demonstrates only the C++ and ArkTS code involved in the APIs for error handling.

## napi\_get\_last\_error\_info

Call **napi\_get\_last\_error\_info** to obtain the last error information, including the error code, error message, and stack information. This API can also be used to handle pending ArkTS exceptions.

CPP code:

#include "napi/native\_api.h"
#include "hilog/log.h"
static napi\_value GetLastErrorInfo(napi\_env env, napi\_callback\_info info)
{
    // Obtain the input parameter, that is the message string in this example.
    size\_t argc = 1;
    napi\_value args\[1\] = {nullptr};
    napi\_get\_cb\_info(env, info, &argc, args, nullptr, nullptr);
    // Call napi\_get\_value\_int32 to obtain the input string parameter to create an error.
    int32\_t value = 0;
    napi\_status status = napi\_get\_value\_int32(env, args\[0\], &value);
    // The return value (status) is not napi\_ok, which means an error occurred.
    if (status != napi\_ok) {
        OH\_LOG\_INFO(LOG\_APP, "Test Node-API napi\_get\_value\_int32 return status, status is not equal to napi\_ok.");
    }

    // Call napi\_get\_last\_error\_info to obtain the last error message.
    const napi\_extended\_error\_info \*errorInfo;
    napi\_get\_last\_error\_info(env, &errorInfo);
    // Obtain the error code and compare it with the return value (status) obtained.
    if (errorInfo->error\_code == status) {
        OH\_LOG\_INFO(LOG\_APP, "Test Node-API napi\_get\_last\_error\_info return errorInfo, error\_code equal to status.");
    }

    // Obtain the error message as the return value and print it.
    napi\_value result = nullptr;
    napi\_create\_string\_utf8(env, errorInfo->error\_message, NAPI\_AUTO\_LENGTH, &result);
    return result;
}

API declaration:

// index.d.ts
export const getLastErrorInfo: (str: string) => string;

ArkTS code:

import { hilog } from '@kit.PerformanceAnalysisKit';
import testNapi from 'libentry.so';

try {
  hilog.info(0x0000, 'testTag', 'Test Node-API napi\_get\_last\_error\_info: %{public}s', testNapi.getLastErrorInfo('message'));
} catch (error) {
  hilog.error(0x0000, 'testTag', 'Test Node-API napi\_get\_last\_error\_info error: %{public}s', error);
}

## napi\_create\_type\_error

Call **napi\_create\_type\_error** to create an ArkTS **TypeError** object with text information.

CPP code:

#include "napi/native\_api.h"

static napi\_value CreateTypeError(napi\_env env, napi\_callback\_info info)
{
    // Construct errorCode and errorMessage.
    napi\_value errorCode = nullptr;
    napi\_create\_string\_utf8(env, "napi\_create\_error errorCode", NAPI\_AUTO\_LENGTH, &errorCode);
    napi\_value errorMessage = nullptr;
    napi\_create\_string\_utf8(env, "napi\_create\_error errorMessage", NAPI\_AUTO\_LENGTH, &errorMessage);
    // Call napi\_create\_type\_error to create a typeError object.
    napi\_value error = nullptr;
    napi\_create\_type\_error(env, errorCode, errorMessage, &error);
    return error;
}

API declaration:

// index.d.ts
export const createTypeError: () => Error;

ArkTS code:

import { hilog } from '@kit.PerformanceAnalysisKit';
import testNapi from 'libentry.so';

try {
  throw testNapi.createTypeError();
} catch (error) {
  hilog.error(0x0000, 'testTag', 'Test Node-API napi\_create\_type\_error errorCode: %{public}s, errorMessage %{public}s', error.code, error.message);
}

## napi\_create\_range\_error

Call **napi\_create\_range\_error** to create an ArkTS **RangeError** with text information.

CPP code:

#include "napi/native\_api.h"

static napi\_value CreateRangeError(napi\_env env, napi\_callback\_info info)
{
    // Construct errorCode and errorMessage.
    napi\_value errorCode = nullptr;
    napi\_create\_string\_utf8(env, "napi\_create\_error errorCode", NAPI\_AUTO\_LENGTH, &errorCode);
    napi\_value errorMessage = nullptr;
    napi\_create\_string\_utf8(env, "napi\_create\_error errorMessage", NAPI\_AUTO\_LENGTH, &errorMessage);
    // Call napi\_create\_range\_error to create a typeError object.
    napi\_value error = nullptr;
    napi\_create\_range\_error(env, errorCode, errorMessage, &error);
    return error;
}

API declaration:

// index.d.ts
export const createRangeError: () => Error;

ArkTS code:

import { hilog } from '@kit.PerformanceAnalysisKit';
import testNapi from 'libentry.so';

try {
  throw testNapi.createRangeError();
} catch (error) {
  hilog.error(0x0000, 'testTag', 'Test Node-API napi\_create\_range\_error errorCode: %{public}s, errorMessage: %{public}s', error.code, error.message);
}

## napi\_create\_error

Call **napi\_create\_error** to create an ArkTS error object with text information.

## napi\_throw

Call **napi\_throw** to throw an ArkTS exception. You need to create an error object first and pass it to **napi\_throw**. You can use this API to throw an ArkTS exception that indicates an error or unexpected behavior occurred in the native code so that exception can be captured and handled.

CPP code:

#include "napi/native\_api.h"

static napi\_value NapiThrow(napi\_env env, napi\_callback\_info info)
{
    // Perform the following operations to throw an exception to indicate an error occurred:
    // Create a string in the Node-API environment and store it in the errorCode variable.
    napi\_value errorCode = nullptr;
    napi\_create\_string\_utf8(env, "throw errorCode", NAPI\_AUTO\_LENGTH, &errorCode);
    // Create a string in the Node-API environment and store it in the errorMessage variable.
    napi\_value errorMessage = nullptr;
    napi\_create\_string\_utf8(env, "throw errorMessage", NAPI\_AUTO\_LENGTH, &errorMessage);
    // Create an ArkTS error object.
    napi\_value error = nullptr;
    napi\_create\_error(env, errorCode, errorMessage, &error);
    // Call napi\_throw to throw an error.
    napi\_throw(env, error);
    return nullptr;
}

API declaration:

// index.d.ts
export const napiThrow: () => void;

ArkTS code:

import { hilog } from '@kit.PerformanceAnalysisKit';
import testNapi from 'libentry.so';

try {
  testNapi.napiThrow();
} catch (error) {
  hilog.error(0x0000, 'testTag', 'Test Node-API napi\_throw errorCode: %{public}s, errorMessage: %{public}s', error.code, error.message);
}

## napi\_throw\_error

Call **napi\_throw\_error** to throw an ArkTS **Error** object with text information.

CPP code:

#include "napi/native\_api.h"

// Throw an error with an error message.
static napi\_value NapiThrowErrorMessage(napi\_env env, napi\_callback\_info info)
{
    napi\_throw\_error(env, nullptr, "napi\_throw\_error throwing an error");
    return nullptr;
}
// Pass in two parameters. Throw an error when the second parameter, that is, the divisor, is 0.
static napi\_value NapiThrowError(napi\_env env, napi\_callback\_info info)
{
    // Pass two parameters from ArkTS.
    size\_t argc = 2;
    napi\_value argv\[2\] = {nullptr};
    napi\_get\_cb\_info(env, info, &argc, argv, nullptr, nullptr);
    // Convert the two parameters to values of the double type as the dividend and divisor.
    double dividend, divisor;
    napi\_get\_value\_double(env, argv\[0\], &dividend);
    napi\_get\_value\_double(env, argv\[1\], &divisor);
    // If the divisor is 0, throw an error with the error code of DIVIDE\_BY\_ZERO and the error message of Cannot divide by zero.
    if (divisor == 0) {
        napi\_throw\_error(env, "DIVIDE\_BY\_ZERO", "Cannot divide by zero");
    }
    return nullptr;
}

API declaration:

// index.d.ts
export const napiThrowErrorMessage: () => void;
export const napiThrowError: (dividend: number, divisor: number) => void;

ArkTS code:

import { hilog } from '@kit.PerformanceAnalysisKit';
import testNapi from 'libentry.so';

try {
  testNapi.napiThrowErrorMessage();
} catch (error) {
  hilog.error(0x0000, 'testTag', 'Test Node-API napi\_throw\_error error code: %{public}s , message: %{public}s', error.code, error.message);
}
try {
  testNapi.napiThrowError(5, 0);
} catch (error) {
  hilog.error(0x0000, 'testTag', 'Test Node-API napi\_throw\_error errorCode: %{public}s , errorMessage: %{public}s', error.code, error.message);
}

## napi\_throw\_type\_error

Use **napi\_throw\_type\_error** to throw an ArkTS **TypeError** object with text information.

CPP code:

#include "napi/native\_api.h"

// Throw a type error with an error message.
static napi\_value ThrowTypeErrorMessage(napi\_env env, napi\_callback\_info info)
{
    napi\_throw\_type\_error(env, nullptr, "napi\_throw\_type\_error throwing an error");
    return nullptr;
}
// Pass in a parameter of incorrect type. Throw a type error when the parameter type is found incorrect.
static napi\_value ThrowTypeError(napi\_env env, napi\_callback\_info info)
{
    // Pass a parameter from ArkTS.
    size\_t argc = 1;
    napi\_value argv\[1\] = {nullptr};
    napi\_get\_cb\_info(env, info, &argc, argv, nullptr, nullptr);
    // Convert the input parameter to a value of the napi\_valuetype type.
    napi\_valuetype valueType;
    napi\_typeof(env, argv\[0\], &valueType);
    // Throw a type error if the input parameter is not of the napi\_number type.
    if (valueType != napi\_number) {
        // Throw a type error with both errorCode and errorMessage.
        napi\_throw\_type\_error(env, "napi\_throw\_type\_error", "Argument must be a number");
    }
    return nullptr;
}

API declaration:

// index.d.ts
export const throwTypeErrorMessage: () => void;
export const throwTypeError: (message: string) => void;

ArkTS code:

import { hilog } from '@kit.PerformanceAnalysisKit';
import testNapi from 'libentry.so';

try {
  testNapi.throwTypeErrorMessage();
} catch (error) {
  hilog.error(0x0000, 'testTag', 'Test Node-API napi\_throw\_type\_error errorCode: %{public}s, errorMessage: %{public}s', error.code, error.message);
}
try {
  testNapi.throwTypeError('str');
} catch (error) {
  hilog.error(0x0000, 'testTag', 'Test Node-API napi\_throw\_type\_error errorCode: %{public}s, errorMessage: %{public}s', error.code, error.message);
}

## napi\_throw\_range\_error

Use **napi\_throw\_range\_error** to throw an ArkTS **RangeError** with text information.

CPP code:

#include "napi/native\_api.h"

// Throw a range error with an error message.
static napi\_value ThrowRangeErrorMessage(napi\_env env, napi\_callback\_info info)
{
    napi\_throw\_range\_error(env, nullptr, "napi\_throw\_range\_error one");
    return nullptr;
}
// Pass in parameters of incorrect quantity and throw a range error.
static napi\_value ThrowRangeError(napi\_env env, napi\_callback\_info info)
{
    // Pass two parameters from ArkTS.
    size\_t argc = 2;
    napi\_value argv\[2\] = {nullptr};
    napi\_get\_cb\_info(env, info, &argc, argv, nullptr, nullptr);
    // If the number of parameters is not 2,
    if (argc != 2) {
        // Throw a range error.
        napi\_throw\_range\_error(env, "napi\_throw\_range\_error", "Expected two numbers as arguments");
        return nullptr;
    }
    // Add the two input values and return the result.
    double numOne = 0;
    double numTwo = 0;
    napi\_get\_value\_double(env, argv\[0\], &numOne);
    napi\_get\_value\_double(env, argv\[1\], &numTwo);
    double result = numOne + numTwo;
    napi\_value resultValue;
    napi\_create\_double(env, result, &resultValue);
    return resultValue;
}

API declaration:

// index.d.ts
export const throwRangeErrorMessage: () => void;
export const throwRangeError: (num: number) => number | undefined;

ArkTS code:

import { hilog } from '@kit.PerformanceAnalysisKit';
import testNapi from 'libentry.so';

try {
  testNapi.throwRangeErrorMessage();
} catch (error) {
  hilog.error(0x0000, 'testTag', 'Test Node-API napi\_throw\_range\_error errorCode: %{public}s, errorMessage: %{public}s', error.code, error.message);
}

try {
  testNapi.throwRangeError(1);
} catch (error) {
  hilog.error(0x0000, 'testTag', 'Test Node-API napi\_throw\_range\_error errorCode: %{public}s, errorMessage: %{public}s', error.code, error.message);
}

## napi\_is\_error

Call **napi\_is\_error** to check whether the given **napi\_value** represents an error object.

CPP code:

#include "napi/native\_api.h"

static napi\_value NapiIsError(napi\_env env, napi\_callback\_info info)
{
    // Obtain the parameter passed in.
    size\_t argc = 1;
    napi\_value args\[1\] = {nullptr};
    napi\_get\_cb\_info(env, info, &argc, args, nullptr, nullptr);
    // Call napi\_is\_error to check whether the input parameter is an error object.
    bool result = false;
    // If napi\_value is an error object, set result to true. Otherwise, set result to false.
    napi\_is\_error(env, args\[0\], &result);
    // Obtain result, call napi\_get\_boolean to convert result to napi\_value, and return napi\_value.
    napi\_value returnValue = nullptr;
    napi\_get\_boolean(env, result, &returnValue);
    return returnValue;
}

API declaration:

// index.d.ts
export const napiIsError: <T>(obj: T) => boolean;

ArkTS code:

import { hilog } from '@kit.PerformanceAnalysisKit';
import testNapi from 'libentry.so';

try {
  throw new Error("throwing an error");
} catch (error) {
  hilog.error(0x0000, 'testTag', 'Test Node-API napi\_is\_error error: %{public}s', testNapi.napiIsError(error)
    .toString());
  hilog.error(0x0000, 'testTag', 'Test Node-API napi\_is\_error error: %{public}s', testNapi.napiIsError(1)
    .toString());
}

## napi\_get\_and\_clear\_last\_exception

Call **napi\_get\_and\_clear\_last\_exception** to obtain and clear the last exception.

CPP code:

#include "napi/native\_api.h"

static napi\_value GetAndClearLastException(napi\_env env, napi\_callback\_info info)
{
    // Throw an error.
    napi\_throw\_error(env, "napi\_create\_error errorCode", "napi\_create\_error errorMessage");
    // Call napi\_get\_and\_clear\_last\_exception to obtain and clear the last unhandled exception. This API can be called even if there are suspended ArkTS exceptions.
    napi\_value result = nullptr;
    napi\_status status = napi\_get\_and\_clear\_last\_exception(env, &result);
    if (status != napi\_ok) {
        return nullptr;
    }
    return result;
}

API declaration:

// index.d.ts
export const getAndClearLastException: () => Error | undefined;

ArkTS code:

import { hilog } from '@kit.PerformanceAnalysisKit';
import testNapi from 'libentry.so';

// Obtain the last unprocessed exception.
hilog.info(0x0000, 'testTag', 'Test Node-API napi\_get\_and\_clear\_last\_exception, error.message: %{public}s',
           testNapi.getAndClearLastException());

## napi\_is\_exception\_pending

Call **napi\_is\_exception\_pending** to check whether there is any pending exception.

CPP code:

#include "napi/native\_api.h"

static napi\_value IsExceptionPending(napi\_env env, napi\_callback\_info info)
{
    napi\_status status;
    bool isExceptionPending = false;
    // Perform operations that may cause an error.
    napi\_throw\_error(env, "napi\_create\_error errorCode", "napi\_create\_error errorMessage");
    // Check whether there is a pending exception.
    status = napi\_is\_exception\_pending(env, &isExceptionPending);
    if (status != napi\_ok) {
        return nullptr;
    }
    if (isExceptionPending) {
        // Handle the pending exception.
        napi\_value result = nullptr;
        status = napi\_get\_and\_clear\_last\_exception(env, &result);
        if (status != napi\_ok) {
            return nullptr;
        }
        // Return the result.
        return result;
    }
    return nullptr;
}

API declaration:

// index.d.ts
export const isExceptionPending: () => Object | undefined;

ArkTS code:

import { hilog } from '@kit.PerformanceAnalysisKit';
import testNapi from 'libentry.so';

interface MyObject {
  code: string;
  message: string;
}
try {
  let result = testNapi.isExceptionPending() as MyObject;
  hilog.info(0x0000, 'testTag', 'Test Node-API napi\_is\_exception\_pending, error.Code: %{public}s, error.message: %{public}s',
    result.code, result.message);
} catch (error) {
  hilog.error(0x0000, 'testTag', 'Test Node-API napi\_is\_exception\_pending error');
}

## napi\_fatal\_error

Call **napi\_fatal\_error** to raise a fatal error to terminate the process immediately. Calling **napi\_fatal\_error** will terminate the application immediately. Avoid frequently calling this API during normal operations.

CPP code:

#include "napi/native\_api.h"

static napi\_value FatalError(napi\_env env, napi\_callback\_info info)
{
    // Calling \*\*napi\_fatal\_error\*\* will terminate the application process immediately. Use this API only when a fatal error that cannot be rectified occurs.
    // Simulate a fatal error.
    bool errorCondition = true;
    if (errorCondition) {
        // Create a fatal error.
        napi\_fatal\_error("napi\_fatal\_error test", NAPI\_AUTO\_LENGTH, "napi\_create\_error errorMessage", NAPI\_AUTO\_LENGTH);
    }
    return nullptr;
}

API declaration:

// index.d.ts
export const fatalError: () => void;

ArkTS code:

import { hilog } from '@kit.PerformanceAnalysisKit';
import testNapi from 'libentry.so';

try {
  testNapi.fatalError();
} catch (error) {
  hilog.error(0x0000, 'testTag', 'Test Node-API napi\_fatal\_error error');
}

## napi\_fatal\_exception

Call **napi\_fatal\_exception** in the context of the main thread to throw a fatal exception. As a result, the application is terminated and a crash log is generated. Exercise caution when using this API. Avoid frequently calling this API during normal operations.

CPP code:

#include "napi/native\_api.h"

static napi\_value FatalException(napi\_env env, napi\_callback\_info info)
{
    size\_t argc = 1;
    napi\_value args\[1\] = {nullptr};

    napi\_status status = napi\_get\_cb\_info(env, info, &argc, args, nullptr, nullptr);
    if (status != napi\_ok) {
      return nullptr;
    }
    // Calling \*\*napi\_fatal\_exception\*\* will terminate the application process. Use this API only when a fatal error that cannot be rectified occurs in the main thread.
    // Simulate a fatal error.
    status = napi\_fatal\_exception(env, args\[0\]);
    if (status != napi\_ok) {
      return nullptr;
    }
    return nullptr;
}

API declaration:

// index.d.ts
export const fatalException: (err: Error) => void;

ArkTS code:

import testNapi from 'libentry.so';

const err = new Error("a fatal exception occurred");
testNapi.fatalException(err);

To print logs in the native CPP, add the following information to the **CMakeLists.txt** file and add the header file by using **#include "hilog/log.h"**.

// CMakeLists.txt
add\_definitions( "-DLOG\_DOMAIN=0xd0d0" )
add\_definitions( "-DLOG\_TAG=\\"testTag\\"" )
target\_link\_libraries(entry PUBLIC libace\_napi.z.so libhilog\_ndk.z.so)
