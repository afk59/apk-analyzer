# Error Handling Using JSVM-API

#### Introduction

JSVM-API provides APIs for handling errors occurred in JS code using exceptions. Properly using these APIs helps improve module stability and reliability.

#### Basic Concepts

Exceptions and errors are common concepts in JS programming. An exception indicates the presence of an unexpected condition, and an error indicates that the application cannot perform certain operations correctly. JSVM-API provides a set of APIs for handling errors occurred in JS code using exceptions. Read on the following to learn basic concepts related to exception handling:

-   Exception: indicates an unexpected condition that may occur during the execution of an application. It can be a syntax error, runtime error, or logic error. For example, the division of a non-zero value with zero and an operation on undefined variables are exceptions.
-   Error: indicates that the application cannot perform some operations. Errors can be defined by the underlying system, API, or developer.
-   **TypeError**: indicates that the type of an operation or value does not meet the expectation. Generally, this error is caused by an incorrect data type.
-   **RangeError**: indicates that a value is not in the expected range. For example, an index beyond the array length is accessed.
-   **SyntaxError**: indicates a mistake in the syntax of a piece of code.

These concepts are important in exception and error handling. Properly using methods to capture, handle, or report exceptions and errors help improve application stability. JSVM-API provides APIs for handling errors in JS code using exceptions.

#### Available APIs

| API | Description |
| :-- | :-- |
| OH\_JSVM\_CreateError, OH\_JSVM\_CreateTypeError, OH\_JSVM\_CreateRangeError, OH\_JSVM\_CreateSyntaxError | Creates a JS error. |
| OH\_JSVM\_Throw | Throws a JS error object, which is created by **OH\_JSVM\_CreateError** or obtained by **OH\_JSVM\_GetLastErrorInfo**. |
| OH\_JSVM\_ThrowError, OH\_JSVM\_ThrowTypeError, OH\_JSVM\_ThrowRangeError, OH\_JSVM\_ThrowSyntaxError | Throws a JS error object. |
| OH\_JSVM\_IsError | Checks whether the given **JSVM\_Value** indicates an error. |
| OH\_JSVM\_GetAndClearLastException | Obtains and clears the last JS exception. |
| OH\_JSVM\_IsExceptionPending | Checks whether there is any pending exception. |
| OH\_JSVM\_GetLastErrorInfo | Obtains the last error information. |

#### Example

If you are just starting out with JSVM-API, see [JSVM-API Development Process](../../jsvm-api-development-process/document.md). The following demonstrates only the C++ code involved in related APIs.

## OH\_JSVM\_Throw

Call **OH\_JSVM\_Throw** to throw a JS error object. You can use this API to throw a JS error that indicates an error or unexpected behavior occurred in the native code so that exception can be captured and handled. For details about the example, see the example of **OH\_JSVM\_CreateError**.

## OH\_JSVM\_CreateError

Call **OH\_JSVM\_CreateError** to create a JS error object with text information.

CPP code:

// hello.cpp
// Capture and clear the last exception in the JSVM environment and log the error message. This function is used as a public function and will not be declared or defined in subsequent examples in this document.
static void GetLastErrorAndClean(JSVM\_Env env) {
    // Call OH\_JSVM\_GetAndClearLastException to obtain and clear the last exception. This API can also be used to handle a suspended JS exception.
    JSVM\_Value result = nullptr;
    JSVM\_Status status = OH\_JSVM\_GetAndClearLastException(env, &result);
    // Log error information.
    JSVM\_Value message = nullptr;
    JSVM\_Value errorCode = nullptr;
    OH\_JSVM\_GetNamedProperty((env), result, "message", &message);
    OH\_JSVM\_GetNamedProperty((env), result, "code", &errorCode);
    char messageStr\[256\];
    char codeStr\[256\];
    OH\_JSVM\_GetValueStringUtf8(env, message, messageStr, 256, nullptr);
    OH\_JSVM\_GetValueStringUtf8(env, errorCode, codeStr, 256, nullptr);
    OH\_LOG\_INFO(LOG\_APP, "JSVM error message: %{public}s, error code: %{public}s", messageStr, codeStr);
}

// Define OH\_JSVM\_CreateError.
static JSVM\_Value JsVmCreateThrowError(JSVM\_Env env, JSVM\_CallbackInfo info) {
    // Create a string in the JSVM and store it in the errorCode variable.
    JSVM\_Value errorCode = nullptr;
    OH\_JSVM\_CreateStringUtf8(env, "-1", JSVM\_AUTO\_LENGTH, &errorCode);
    // Create a string in the JSVM and store it in the errorMessage variable.
    JSVM\_Value errorMessage = nullptr;
    OH\_JSVM\_CreateStringUtf8(env, "HasError", JSVM\_AUTO\_LENGTH, &errorMessage);
    // Create a JS error object.
    JSVM\_Value error = nullptr;
    OH\_JSVM\_CreateError(env, errorCode, errorMessage, &error);
    // Call OH\_JSVM\_Throw to throw the error.
    OH\_JSVM\_Throw(env, error);
    GetLastErrorAndClean(env);
    return nullptr;
}

// Register the JsVmCreateThrowError callback.
static JSVM\_CallbackStruct param\[\] = {
    {.data = nullptr, .callback = JsVmCreateThrowError},
};
static JSVM\_CallbackStruct \*method = param;
// Alias for the JsVmCreateThrowError method to be called from JS.
static JSVM\_PropertyDescriptor descriptor\[\] = {
    {"jsVmCreateThrowError", nullptr, method++, nullptr, nullptr, nullptr, JSVM\_DEFAULT},
};
// Call the C++ code from JS.
const char \*srcCallNative = R"JS(jsVmCreateThrowError();)JS";

Expected result:

JSVM error message: HasError, error code: -1

## OH\_JSVM\_ThrowError

Call **OH\_JSVM\_ThrowError** to throw a JS **Error** object with text information.

CPP code:

// hello.cpp
// Define OH\_JSVM\_ThrowError.
static JSVM\_Value JsVmThrowError(JSVM\_Env env, JSVM\_CallbackInfo info)
{
    size\_t argc = 1;
    JSVM\_Value argv\[1\] = {nullptr};
    OH\_JSVM\_GetCbInfo(env, info, &argc, argv, nullptr, nullptr);
    if (argc == 0) {
        // Throw an error if no parameter is passed in.
        OH\_JSVM\_ThrowError(env, "-1", "has Error");
    } else if (argc == 1) {
        size\_t length = 0;
        // Obtain the length of the string passed from JS from the input parameter.
        OH\_JSVM\_GetValueStringUtf8(env, argv\[0\], nullptr, 0, &length);
        char \*buffer = new char\[length + 1\];
        // Obtain the string of the input parameter.
        OH\_JSVM\_GetValueStringUtf8(env, argv\[0\], buffer, length + 1, nullptr);
        // Populate the error information to OH\_JSVM\_ThrowError.
        OH\_JSVM\_ThrowError(env, "self defined error code", buffer);
        delete\[\] buffer;
    }
    GetLastErrorAndClean(env);
    return nullptr;
}
// Register the JsVmThrowError callback.
static JSVM\_CallbackStruct param\[\] = {
    {.data = nullptr, .callback = JsVmThrowError},
};
static JSVM\_CallbackStruct \*method = param;
// Alias for the JsVmThrowError method to be called from JS.
static JSVM\_PropertyDescriptor descriptor\[\] = {
    {"jsVmThrowError", nullptr, method++, nullptr, nullptr, nullptr, JSVM\_DEFAULT},
};
// Call the C++ code from JS.
const char \*srcCallNative = R"JS(jsVmThrowError();jsVmThrowError("self defined error message");)JS";

Expected result:

JSVM error message: has Error, error code: -1
JSVM error message: self defined error message, error code: self defined error code

## OH\_JSVM\_ThrowTypeError

Call **OH\_JSVM\_CreateTypeError** to create a JS **TypeError** object with text information.

CPP code:

// hello.cpp
// Define OH\_JSVM\_ThrowTypeError.
static JSVM\_Value JsVmThrowTypeError(JSVM\_Env env, JSVM\_CallbackInfo info) {
    size\_t argc = 1;
    JSVM\_Value argv\[1\] = {nullptr};
    OH\_JSVM\_GetCbInfo(env, info, &argc, argv, nullptr, nullptr);
    if (argc == 0) {
        // Throw an error if no parameter is passed in.
        OH\_JSVM\_ThrowTypeError(env, "-1", "throwing type error");
    } else if (argc == 1) {
        size\_t length = 0;
        // Obtain the length of the string in the input parameter passed from JS.
        OH\_JSVM\_GetValueStringUtf8(env, argv\[0\], nullptr, 0, &length);
        char \*buffer = new char\[length + 1\];
        // Obtain the string of the input parameter.
        OH\_JSVM\_GetValueStringUtf8(env, argv\[0\], buffer, length + 1, nullptr);
        // Populate the error information to OH\_JSVM\_ThrowTypeError.
        OH\_JSVM\_ThrowTypeError(env, "self defined error code", buffer);
        delete\[\] buffer;
    }
    GetLastErrorAndClean(env);
    return nullptr;
}
// Register the \*\*JsVmThrowTypeError\*\* callback.
static JSVM\_CallbackStruct param\[\] = {
    {.data = nullptr, .callback = JsVmThrowTypeError},
};
static JSVM\_CallbackStruct \*method = param;
// Alias for the JsVmThrowTypeError method to be called from JS.
static JSVM\_PropertyDescriptor descriptor\[\] = {
    {"jsVmThrowTypeError", nullptr, method++, nullptr, nullptr, nullptr, JSVM\_DEFAULT},
};
// Call the C++ code from JS.
const char \*srcCallNative = R"JS(jsVmThrowTypeError();jsVmThrowTypeError("self defined error message");)JS";

Expected result:

JSVM error message: throwing type error, error code: -1
JSVM error message: self defined error message, error code: self defined error code

## OH\_JSVM\_ThrowRangeError

Call **OH\_JSVM\_CreateRangeError** to create a JS **RangeError** with text information.

CPP code:

// hello.cpp
// Define OH\_JSVM\_ThrowRangeError.
static JSVM\_Value JsVmThrowRangeError(JSVM\_Env env, JSVM\_CallbackInfo info)
{
    // Pass two parameters from JS.
    size\_t argc = 2;
    JSVM\_Value argv\[2\] = {nullptr};
    OH\_JSVM\_GetCbInfo(env, info, &argc, argv, nullptr, nullptr);
    // If the number of parameters is not 2,
    if (argc != 2) {
        // Throw a RangeError.
        OH\_JSVM\_ThrowRangeError(env, "OH\_JSVM\_ThrowRangeError", "Expected two numbers as arguments");
        GetLastErrorAndClean(env);
        return nullptr;
    }
    JSVM\_Value result = nullptr;
    OH\_JSVM\_GetBoolean(env, true, &result);
    return result;
}
// Register the JsVmThrowRangeError callback.
static JSVM\_CallbackStruct param\[\] = {
    {.data = nullptr, .callback = JsVmThrowRangeError},
};
static JSVM\_CallbackStruct \*method = param;
// Alias for the JsVmThrowRangeError method to be called from JS.
static JSVM\_PropertyDescriptor descriptor\[\] = {
    {"jsVmThrowRangeError", nullptr, method++, nullptr, nullptr, nullptr, JSVM\_DEFAULT},
};
// Call the C++ code from JS.
const char \*srcCallNative = R"JS(jsVmThrowRangeError(1);)JS";

Expected result:

JSVM error message: Expected two numbers as arguments, error code: OH\_JSVM\_ThrowRangeError

## OH\_JSVM\_ThrowSyntaxError

Call **OH\_JSVM\_ThrowSyntaxError** to create and throw a JS **SyntaxError** object with text information.

CPP code:

// hello.cpp
// Define OH\_JSVM\_ThrowSyntaxError.
static JSVM\_Value JsVmThrowSyntaxError(JSVM\_Env env, JSVM\_CallbackInfo info) {
    // Pass the JS code from JS.
    size\_t argc = 1;
    JSVM\_Value argv\[1\] = {nullptr};
    OH\_JSVM\_GetCbInfo(env, info, &argc, argv, nullptr, nullptr);
    JSVM\_Script script = nullptr;
    // Call OH\_JSVM\_CompileScript to compile the JS code.
    OH\_JSVM\_CompileScript(env, argv\[0\], nullptr, 0, true, nullptr, &script);
    JSVM\_Value scriptResult = nullptr;
    // Call OH\_JSVM\_RunScript to run the JS code.
    JSVM\_Status status = OH\_JSVM\_RunScript(env, script, &scriptResult);
    if (status != JSVM\_OK) {
        // If the value returned by JSVM\_RunScript is not JSVM\_OK, throw a SyntaxError.
        OH\_JSVM\_ThrowSyntaxError(env, "JsVmThrowSyntaxError", "throw syntax error");
        GetLastErrorAndClean(env);
        return nullptr;
    }
    JSVM\_Value result = nullptr;
    OH\_JSVM\_GetBoolean(env, true, &result);
    return result;
}
// Register the JsVmThrowSyntaxError callback.
static JSVM\_CallbackStruct param\[\] = {
    {.data = nullptr, .callback = JsVmThrowSyntaxError},
};
static JSVM\_CallbackStruct \*method = param;
// Alias for the JsVmThrowSyntaxError method to be called from JS.
static JSVM\_PropertyDescriptor descriptor\[\] = {
    {"jsVmThrowSyntaxError", nullptr, method++, nullptr, nullptr, nullptr, JSVM\_DEFAULT},
};
// Call the C++ code from JS.
const char \*srcCallNative = R"JS(jsVmThrowSyntaxError();)JS";

Expected result:

JSVM error message: throw syntax error, error code: JsVmThrowSyntaxError

## OH\_JSVM\_IsError

Call **OH\_JSVM\_IsError** to check whether the given **JSVM\_Value** represents an error object.

CPP code:

// hello.cpp
// Define OH\_JSVM\_IsError.
static JSVM\_Value JsVmIsError(JSVM\_Env env, JSVM\_CallbackInfo info) {
    size\_t argc = 1;
    JSVM\_Value args\[1\] = {nullptr};
    OH\_JSVM\_GetCbInfo(env, info, &argc, args, nullptr, nullptr);
    // Call OH\_JSVM\_IsError to check whether the input parameter is an error object.
    bool result = false;
    // If JSVM\_Value is an error object, set result to true. Otherwise, set result to false.
    JSVM\_Status status = OH\_JSVM\_IsError(env, args\[0\], &result);
    if (status == JSVM\_OK) {
        OH\_LOG\_INFO(LOG\_APP, "JSVM API call OH\_JSVM\_IsError success, result is %{public}d", result);
    }else {
        OH\_LOG\_INFO(LOG\_APP, "JSVM API call OH\_JSVM\_IsError failed");
    }
    // Obtain result, call OH\_JSVM\_GetBoolean to convert result to JSVM\_Value, and return JSVM\_Value.
    JSVM\_Value returnValue = nullptr;
    OH\_JSVM\_GetBoolean(env, result, &returnValue);
    return returnValue;
}
// Register the JsVmIsError callback.
static JSVM\_CallbackStruct param\[\] = {
    {.data = nullptr, .callback = JsVmIsError},
};
static JSVM\_CallbackStruct \*method = param;
// Alias for the JsVmIsError method to be called from JS.
static JSVM\_PropertyDescriptor descriptor\[\] = {
    {"jsVmIsError", nullptr, method++, nullptr, nullptr, nullptr, JSVM\_DEFAULT},
};
// Call the C++ code from JS.
const char \*srcCallNative = R"JS(jsVmIsError(Error()))JS";

Expected result:

JSVM API call OH\_JSVM\_IsError success, result is 1

## OH\_JSVM\_CreateTypeError

Call **OH\_JSVM\_CreateTypeError** to create a JS **TypeError** object with text information.

CPP code:

// hello.cpp
// Define OH\_JSVM\_CreateTypeError.
static JSVM\_Value JsVmCreateTypeError(JSVM\_Env env, JSVM\_CallbackInfo info) {
    // Create a string in the JSVM and store it in the errorCode variable.
    JSVM\_Value errorCode = nullptr;
    OH\_JSVM\_CreateStringUtf8(env, "-1", JSVM\_AUTO\_LENGTH, &errorCode);
    // Create a string in the JSVM and store it in the errorMessage variable.
    JSVM\_Value errorMessage = nullptr;
    OH\_JSVM\_CreateStringUtf8(env, "HasError", JSVM\_AUTO\_LENGTH, &errorMessage);
    JSVM\_Value result = nullptr;
    JSVM\_Status status = OH\_JSVM\_CreateTypeError(env, errorCode, errorMessage, &result);
    if (status == JSVM\_OK) {
        OH\_LOG\_INFO(LOG\_APP, "JSVM API Create TypeError SUCCESS");
    } else {
        OH\_LOG\_INFO(LOG\_APP, "JSVM API Create TypeError FAILED");
    }
    return result;
}
// Register the JsVmCreateTypeError callback.
static JSVM\_CallbackStruct param\[\] = {
    {.data = nullptr, .callback = JsVmCreateTypeError},
};
static JSVM\_CallbackStruct \*method = param;
// Alias for the JsVmCreateTypeError method to be called from JS.
static JSVM\_PropertyDescriptor descriptor\[\] = {
    {"jsVmCreateTypeError", nullptr, method++, nullptr, nullptr, nullptr, JSVM\_DEFAULT},
};
// Call the C++ code from JS.
const char \*srcCallNative = R"JS(jsVmCreateTypeError();)JS";

Expected result:

JSVM API Create TypeError SUCCESS

## OH\_JSVM\_CreateRangeError

Call **OH\_JSVM\_CreateRangeError** to create a JS **RangeError** with text information.

CPP code:

// hello.cpp
// Define OH\_JSVM\_CreateRangeError.
static JSVM\_Value JsVmCreateRangeError(JSVM\_Env env, JSVM\_CallbackInfo info) {
    // Create a string in the JSVM and store it in the errorCode variable.
    JSVM\_Value errorCode = nullptr;
    OH\_JSVM\_CreateStringUtf8(env, "-1", JSVM\_AUTO\_LENGTH, &errorCode);
    // Create a string in the JSVM and store it in the errorMessage variable.
    JSVM\_Value errorMessage = nullptr;
    OH\_JSVM\_CreateStringUtf8(env, "HasError", JSVM\_AUTO\_LENGTH, &errorMessage);
    JSVM\_Value result = nullptr;
    JSVM\_Status status = OH\_JSVM\_CreateRangeError(env, errorCode, errorMessage, &result);
    if (status == JSVM\_OK) {
        OH\_LOG\_INFO(LOG\_APP, "JSVM API CreateRangeError SUCCESS");
    } else {
        OH\_LOG\_INFO(LOG\_APP, "JSVM API CreateRangeError FAILED");
    }
    return result;
}
// Register the JsVmCreateRangeError callback.
static JSVM\_CallbackStruct param\[\] = {
    {.data = nullptr, .callback = JsVmCreateRangeError},
};
static JSVM\_CallbackStruct \*method = param;
// Alias for the JsVmCreateRangeError method to be called from JS.
static JSVM\_PropertyDescriptor descriptor\[\] = {
    {"jsVmCreateRangeError", nullptr, method++, nullptr, nullptr, nullptr, JSVM\_DEFAULT},
};
// Call the C++ code from JS.
const char \*srcCallNative = R"JS(jsVmCreateRangeError();)JS";

Expected result:

JSVM API CreateRangeError SUCCESS

## OH\_JSVM\_CreateSyntaxError

Call **OH\_JSVM\_CreateSyntaxError** to create and throw a JS **SyntaxError** object with text information.

CPP code:

// hello.cpp
// Define OH\_JSVM\_CreateSyntaxError.
static JSVM\_Value JsVmCreateSyntaxError(JSVM\_Env env, JSVM\_CallbackInfo info) {
    // Create a string in the JSVM and store it in the errorCode variable.
    JSVM\_Value errorCode = nullptr;
    OH\_JSVM\_CreateStringUtf8(env, "-1", JSVM\_AUTO\_LENGTH, &errorCode);
    // Create a string in the JSVM and store it in the errorMessage variable.
    JSVM\_Value errorMessage = nullptr;
    OH\_JSVM\_CreateStringUtf8(env, "HasError", JSVM\_AUTO\_LENGTH, &errorMessage);
    JSVM\_Value result = nullptr;
    JSVM\_Status status =  OH\_JSVM\_CreateSyntaxError(env, errorCode, errorMessage, &result);
    if (status == JSVM\_OK) {
        OH\_LOG\_INFO(LOG\_APP, "JSVM API CreateSyntaxError SUCCESS");
    } else {
        OH\_LOG\_INFO(LOG\_APP, "JSVM API CreateSyntaxError FAILED");
    }
    return result;
}
// Register the JsVmCreateSyntaxError callback.
static JSVM\_CallbackStruct param\[\] = {
    {.data = nullptr, .callback = JsVmCreateSyntaxError},
};
static JSVM\_CallbackStruct \*method = param;
// Alias for the JsVmCreateSyntaxError method to be called from JS.
static JSVM\_PropertyDescriptor descriptor\[\] = {
    {"jsVmCreateSyntaxError", nullptr, method++, nullptr, nullptr, nullptr, JSVM\_DEFAULT},
};
// Call the C++ code from JS.
const char \*srcCallNative = R"JS(jsVmCreateSyntaxError();)JS";

Expected result:

JSVM API CreateSyntaxError SUCCESS

## OH\_JSVM\_GetAndClearLastException

Call **OH\_JSVM\_GetAndClearLastException** to obtain and clear the latest exception.

CPP code:

// hello.cpp
// Define OH\_JSVM\_GetAndClearLastException.
static JSVM\_Value JsVmGetAndClearLastException(JSVM\_Env env, JSVM\_CallbackInfo info) {
    // Throw an error.
    OH\_JSVM\_ThrowError(env, "OH\_JSVM\_ThrowError errorCode", "OH\_JSVM\_ThrowError errorMessage");
    // Call OH\_JSVM\_GetAndClearLastException to obtain and clear the last exception. This API can also be used to handle a suspended JS exception.
    JSVM\_Value result = nullptr;
    JSVM\_Status status = OH\_JSVM\_GetAndClearLastException(env, &result);
    if (status != JSVM\_OK) {
        OH\_LOG\_INFO(LOG\_APP, "JSVM API OH\_JSVM\_GetAndClearLastException FAILED");
    } else {
        OH\_LOG\_INFO(LOG\_APP, "JSVM API OH\_JSVM\_GetAndClearLastException SUCCESS");
    }
    return result;
}
// Register the JsVmGetAndClearLastException callback.
static JSVM\_CallbackStruct param\[\] = {
    {.data = nullptr, .callback = JsVmGetAndClearLastException},
};
static JSVM\_CallbackStruct \*method = param;
// Alias for the JsVmGetAndClearLastException method to be called from JS.
static JSVM\_PropertyDescriptor descriptor\[\] = {
    {"jsVmGetAndClearLastException", nullptr, method++, nullptr, nullptr, nullptr, JSVM\_DEFAULT},
};
// Call the C++ code from JS.
const char \*srcCallNative = R"JS(jsVmGetAndClearLastException();)JS";

Expected result:

JSVM API OH\_JSVM\_GetAndClearLastException SUCCESS

## OH\_JSVM\_IsExceptionPending

Call **OH\_JSVM\_IsExceptionPending** to check whether there is any pending exception.

CPP code:

// hello.cpp
// Sample method of OH\_JSVM\_IsExceptionPending
static JSVM\_Value JsVmIsExceptionPending(JSVM\_Env env, JSVM\_CallbackInfo info) {
    JSVM\_Status status;
    bool isExceptionPending = false;
    // Perform operations that may cause an error.
    OH\_JSVM\_ThrowError(env, "OH\_JSVM\_ThrowError errorCode", "OH\_JSVM\_ThrowError errorMessage");
    // Check whether there is a pending exception.
    status = OH\_JSVM\_IsExceptionPending(env, &isExceptionPending);
    if (status != JSVM\_OK) {
        return nullptr;
    }
    if (isExceptionPending) {
        OH\_LOG\_INFO(LOG\_APP, "JSVM API OH\_JSVM\_IsExceptionPending: SUCCESS");
        // Handle the pending exception.
        JSVM\_Value result = nullptr;
        status = OH\_JSVM\_GetAndClearLastException(env, &result);
        if (status != JSVM\_OK) {
            return nullptr;
        }
        // Return the result.
        return result;
    } else {
        OH\_LOG\_INFO(LOG\_APP, "JSVM API OH\_JSVM\_IsExceptionPending: FAILED");
    }
    return nullptr;
}
// Register the JsVmIsExceptionPending callback.
static JSVM\_CallbackStruct param\[\] = {
    {.data = nullptr, .callback = JsVmIsExceptionPending},
};
static JSVM\_CallbackStruct \*method = param;
// Alias for the JsVmIsExceptionPending method to be called from JS.
static JSVM\_PropertyDescriptor descriptor\[\] = {
    {"jsVmIsExceptionPending", nullptr, method++, nullptr, nullptr, nullptr, JSVM\_DEFAULT},
};
// Call the C++ code from JS.
const char \*srcCallNative = R"JS(jsVmIsExceptionPending();)JS";

Expected result:

JSVM API OH\_JSVM\_IsExceptionPending: SUCCESS

## OH\_JSVM\_GetLastErrorInfo

Call **OH\_JSVM\_GetLastErrorInfo** to obtain the last error information (the return value is not **JSVM\_OK**), including the error code, error message, and stack information. This API can also be used for suspended JS errors.

Note that the errors triggered by APIs such as **OH\_JSVM\_ThrowError** will not be captured by the APIs unless the return value is not **JSVM\_OK**.

CPP code:

// hello.cpp
// Define OH\_JSVM\_GetLastErrorInfo.
static JSVM\_Value JsVmGetLastErrorInfo(JSVM\_Env env, JSVM\_CallbackInfo info) {
    // Obtain the input parameter, that is the message string in this example.
    size\_t argc = 1;
    JSVM\_Value args\[1\] = {nullptr};
    OH\_JSVM\_GetCbInfo(env, info, &argc, args, nullptr, nullptr);
    // Call OH\_JSVM\_GetValueInt32 to obtain the input string parameter to create an error.
    int32\_t value = 0;
    OH\_JSVM\_GetValueInt32(env, args\[0\], &value);
    // Call OH\_JSVM\_GetLastErrorInfo to obtain the last error message.
    const JSVM\_ExtendedErrorInfo \*errorInfo;
    OH\_JSVM\_GetLastErrorInfo(env, &errorInfo);

    // Obtain the error message as the return value and print it.
    JSVM\_Value result = nullptr;
    OH\_LOG\_INFO(LOG\_APP,
                "JSVM API OH\_JSVM\_GetLastErrorInfo: SUCCESS, error message is %{public}s, error code is %{public}d",
                errorInfo->errorMessage, errorInfo->errorCode);
    // Handle the exception to prevent the application from exiting due to the error thrown.
    JSVM\_Value result1 = nullptr;
    OH\_JSVM\_GetAndClearLastException(env, &result1);
    OH\_JSVM\_CreateInt32(env, errorInfo->errorCode, &result);
    return result;
}
// Register the JsVmGetLastErrorInfo callback.
static JSVM\_CallbackStruct param\[\] = {
    {.data = nullptr, .callback = JsVmGetLastErrorInfo},
};
static JSVM\_CallbackStruct \*method = param;
// Alias for the JsVmGetLastErrorInfo method to be called from JS.
static JSVM\_PropertyDescriptor descriptor\[\] = {
    {"jsVmGetLastErrorInfo", nullptr, method++, nullptr, nullptr, nullptr, JSVM\_DEFAULT},
};
// Call the C++ code from JS.
const char \*srcCallNative = R"JS(jsVmGetLastErrorInfo();)JS";

Expected result:

JSVM API OH\_JSVM\_GetLastErrorInfo: SUCCESS, error message is A number was expected, error code is 6
