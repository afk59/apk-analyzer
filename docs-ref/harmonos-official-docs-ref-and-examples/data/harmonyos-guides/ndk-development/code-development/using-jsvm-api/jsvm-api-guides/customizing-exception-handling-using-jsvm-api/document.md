# Customizing Exception Handling Using JSVM-API

#### Introduction

JSVM-API provides APIs for handling JSVM exceptions. You can use these APIs to register callbacks with a JSVM. When an exception occurs on the JSVM, the registered callback will be triggered.

With these APIs, you can customize the handling of critical errors in the JS engine, streamlining error and exception handling during runtime.

#### Basic Concepts

JSVM-API provides APIs for handling the following errors:

Out-of-memory (OOM) error: You can use JSVM-API to register an OOM handler with a JSVM. When the JSVM encounters insufficient memory, the system will throw an OOM error and call the registered OOM error handler to perform cleanup or logging operations.

Fatal error: You can use JSVM-API to register a fatal error handler with a JSVM. When the JSVM encounters a fatal error, for example, an unrecoverable error while running JS code, the system will throw a fatal error and call the registered handler to output additional log information or report the error to prevent application crash.

Promise rejection without a catch handler: You can use JSVM-API to register a promise rejection handler with a JSVM. When a promise in JS is rejected without being caught by a catch handler, the system will throw a Promise Reject error and call the registered handler to handle the promise rejection.

#### Available APIs

| API | Description |
| :-- | :-- |
| OH\_JSVM\_SetHandlerForOOMError | Sets an OOM error handler for a JSVM. |
| OH\_JSVM\_SetHandlerForFatalError | Sets a fatal error handler for a JSVM. |
| OH\_JSVM\_SetHandlerForPromiseReject | Sets a promise rejection handler for a JSVM. |

#### Example

If you are just starting out with JSVM-API, see [JSVM-API Development Process](../../jsvm-api-development-process/document.md). The following demonstrates only the C++ code involved in exception handling.

## OH\_JSVM\_SetHandlerForOOMError

Call **OH\_JSVM\_SetHandlerForOOMError** to set a function for handling the OOM error. If this API is called multiple times, only the last setting takes effect. If **NULL** is passed in for the function to set in this API, the previously set handler will be canceled.

**CPP Code**

#include <csetjmp>
#include <vector>

static jmp\_buf buf;
static bool oomHandlerFinished = false;

void OnOOMError(const char \*location, const char \*detail, bool isHeapOOM)
{
    oomHandlerFinished = true;
    longjmp(buf, 1);
}

static JSVM\_Value TriggerOOMError(JSVM\_Env env, JSVM\_CallbackInfo info)
{
    oomHandlerFinished = false;
    JSVM\_VM vm;
    JSVM\_CALL(OH\_JSVM\_GetVM(env, &vm));
    // Set an OOM error handler.
    JSVM\_CALL(OH\_JSVM\_SetHandlerForOOMError(vm, OnOOMError));
    bool oomed = false;
    setjmp(buf);
    if (!oomed) {
        oomed = true;
        // Trigger an OOM error.
        std::vector<JSVM\_Value> arrayVec;
        int loopCount = 1000;
        for (int i = 0; i < loopCount; i++) {
            JSVM\_Value array;
            JSVM\_CALL(OH\_JSVM\_CreateArrayWithLength(env, 0xffffff, &array));
            arrayVec.push\_back(array);
        }
    }
    if (oomHandlerFinished) {
        OH\_LOG\_INFO(LOG\_APP, "JSVM Trigger OOM Error: success");
    } else {
        OH\_LOG\_ERROR(LOG\_APP, "JSVM Trigger OOM Error: failed");
    }
    // Cancel the OOM error handler.
    JSVM\_CALL(OH\_JSVM\_SetHandlerForOOMError(vm, NULL));
    JSVM\_Value checked;
    OH\_JSVM\_GetBoolean(env, true, &checked);
    return checked;
}

static JSVM\_CallbackStruct param\[\] = {
    {.data = nullptr, .callback = TriggerOOMError},
};
static JSVM\_CallbackStruct \*method = param;

static JSVM\_PropertyDescriptor descriptor\[\] = {
    {"triggerOOMError", nullptr, method++, nullptr, nullptr, nullptr, JSVM\_DEFAULT},
};

**JS Example**

const char \*srcCallNative = R"JS(triggerOOMError();)JS";

**Execution Result**

Log output:

JSVM Trigger OOM Error: success

## OH\_JSVM\_SetHandlerForFatalError

Call **OH\_JSVM\_SetHandlerForFatalError** to set a function for handling the fatal error. If this API is called multiple times, only the last setting takes effect. If **NULL** is passed in for the function to set in this API, the previously set handler will be canceled.

**CPP Code**

#include <csetjmp>
#include <vector>

static jmp\_buf buf;
static bool fatalHandlerFinished = false;
void OnFatalError(const char \*location, const char \*message)
{
    fatalHandlerFinished = true;
    OH\_LOG\_INFO(LOG\_APP, "Run in 106");
    longjmp(buf, 1);
}

static JSVM\_Value TriggerFatalError(JSVM\_Env env, JSVM\_CallbackInfo info)
{
    fatalHandlerFinished = false;
    JSVM\_VM vm;
    JSVM\_CALL(OH\_JSVM\_GetVM(env, &vm));
    // Set a fatal error handler.
    JSVM\_CALL(OH\_JSVM\_SetHandlerForFatalError(vm, OnFatalError));
    bool fataled = false;
    setjmp(buf);
    if (!fataled) {
        fataled = true;
        std::vector<JSVM\_Value> arrayVec;
        int loopCount = 1000;
        for (int i = 0; i < loopCount; i++) {
            JSVM\_Value array;
            JSVM\_CALL(OH\_JSVM\_CreateArrayWithLength(env, 0xffffff, &array));
            arrayVec.push\_back(array);
        }
    }
    if (fatalHandlerFinished) {
        OH\_LOG\_INFO(LOG\_APP, "JSVM Trigger Fatal Error: success");
    } else {
        OH\_LOG\_ERROR(LOG\_APP, "JSVM Trigger Fatal Error: failed");
    }
    // Cancel the fatal error handler.
    JSVM\_CALL(OH\_JSVM\_SetHandlerForFatalError(vm, NULL));
    JSVM\_Value checked;
    OH\_JSVM\_GetBoolean(env, true, &checked);
    return checked;
}

static JSVM\_CallbackStruct param\[\] = {
    {.data = nullptr, .callback = TriggerFatalError},
};
static JSVM\_CallbackStruct \*method = param;

static JSVM\_PropertyDescriptor descriptor\[\] = {
    {"triggerFatalError", nullptr, method++, nullptr, nullptr, nullptr, JSVM\_DEFAULT},
};

**JS Example**

const char\* srcCallNative = R"JS(triggerFatalError())JS";

**Execution Result**

Log output:

JSVM Trigger Fatal Error: success

## OH\_JSVM\_SetHandlerForPromiseReject

Call **OH\_JSVM\_SetHandlerForPromiseReject** to set the function for handling promise rejection. If this API is called multiple times, only the last setting takes effect. If **NULL** is passed in for the function to set in this API, the previously set handler will be canceled.

**CPP Code**

static bool promiseRejectHandlerFinished = false;

void OnPromiseReject(JSVM\_Env env, JSVM\_PromiseRejectEvent rejectEvent, JSVM\_Value rejectInfo)
{
    bool result = false;
    OH\_JSVM\_IsObject(env, rejectInfo, &result);
    JSVM\_Value promise;
    JSVM\_Value key1;
    OH\_JSVM\_CreateStringUtf8(env, "promise", JSVM\_AUTO\_LENGTH, &key1);
    OH\_JSVM\_GetProperty(env, rejectInfo, key1, &promise);
    bool isPromise = false;
    OH\_JSVM\_IsPromise(env, promise, &isPromise);
    JSVM\_Value value;
    JSVM\_Value key2;
    OH\_JSVM\_CreateStringUtf8(env, "value", JSVM\_AUTO\_LENGTH, &key2);
    OH\_JSVM\_GetProperty(env, rejectInfo, key2, &value);
    JSVM\_Value js\_number;
    OH\_JSVM\_CoerceToNumber(env, value, &js\_number);
    double res = 0;
    OH\_JSVM\_GetValueDouble(env, js\_number, &res);
    if (res == 42 && isPromise) {
        promiseRejectHandlerFinished = true;
    }
}

static JSVM\_Value TriggerPromiseReject(JSVM\_Env env, JSVM\_CallbackInfo info)
{
    promiseRejectHandlerFinished = false;
    JSVM\_VM vm;
    JSVM\_CALL(OH\_JSVM\_GetVM(env, &vm));
    // Set a Promise-Reject handler.
    JSVM\_CALL(OH\_JSVM\_SetHandlerForPromiseReject(vm, OnPromiseReject));
    JSVM\_Value strVal;
    char \*str = "new Promise((resolve, reject) => { reject(42); })";
    OH\_JSVM\_CreateStringUtf8(env, str, JSVM\_AUTO\_LENGTH, &strVal);
    JSVM\_Script script;
    OH\_JSVM\_CompileScript(env, strVal, nullptr, 0, false, nullptr, &script);
    JSVM\_Value result;
    JSVM\_Status status = OH\_JSVM\_RunScript(env, script, &result);

    if (promiseRejectHandlerFinished) {
        OH\_LOG\_INFO(LOG\_APP, "JSVM Trigger Promise Reject: success");
    } else {
        OH\_LOG\_ERROR(LOG\_APP, "JSVM Trigger Promise Reject: failed");
    }
    // Cancel the Promise-Reject handler.
    JSVM\_CALL(OH\_JSVM\_SetHandlerForPromiseReject(vm, NULL));
    JSVM\_Value checked;
    OH\_JSVM\_GetBoolean(env, true, &checked);
    return checked;
}

static JSVM\_CallbackStruct param\[\] = {
    {.data = nullptr, .callback = TriggerPromiseReject},
};
static JSVM\_CallbackStruct \*method = param;

static JSVM\_PropertyDescriptor descriptor\[\] = {
    {"triggerPromiseReject", nullptr, method++, nullptr, nullptr, nullptr, JSVM\_DEFAULT},
};

**JS Example**

const char\* srcCallNative = R"JS(triggerPromiseReject())JS";

**Execution Result**

Log output:

JSVM Trigger Promise Reject: success
