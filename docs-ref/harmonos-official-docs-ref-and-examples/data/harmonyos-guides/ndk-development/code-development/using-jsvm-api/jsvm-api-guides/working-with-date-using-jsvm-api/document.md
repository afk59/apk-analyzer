# Working with Date Using JSVM-API

#### Introduction

JSVM-API provides APIs for processing JavaScript (JS) **Date** objects in C/C++. These APIs are useful for working with time- and date-related logic in the JSVM module.

#### Basic Concepts

In JSVM-API, the value of a JS **Date** object is the number of milliseconds elapsed since the Unix epoch (00:00:00 UTC on January 1, 1970).

JS Date objects are used to represent and manage date and time in JS. With the **Date** object, you can create an object that represents a specific time, perform date- and time-related calculations (such as adding or subtracting time intervals), and format date as a string for display.

With the functions for interacting with the **Date** object, the JSVM module can be closely integrated with the JS environment to perform more complex date- and time-related operations.

#### Available APIs

| API | Description |
| :-- | :-- |
| OH\_JSVM\_CreateDate | Creates a **Date** object representing the given number of milliseconds. |
| OH\_JSVM\_GetDateValue | Obtains the C double primitive of the time value for the given JS **Date** object. |
| OH\_JSVM\_IsDate | Checks whether a JS object is a date. |

#### Example

If you are just starting out with JSVM-API, see [JSVM-API Development Process](../../jsvm-api-development-process/document.md). The following demonstrates only the C++ code involved in related APIs.

## OH\_JSVM\_CreateDate

Use **OH\_JSVM\_CreateDate** to create a **Date** object representing the given number of milliseconds.

CPP code:

#include <time.h>
// Define OH\_JSVM\_CreateDate.
static JSVM\_Value CreateDate(JSVM\_Env env, JSVM\_CallbackInfo info) {
    // Obtain the number of seconds elapsed since the Unix epoch using the C function and convert the value into milliseconds.
    double value = static\_cast<double>(static\_cast<uint64\_t>(time(NULL)) \* 1000ULL);
    // Call OH\_JSVM\_CreateDate to convert the double value into a JS value indicating the date and time.
    JSVM\_Value returnValue = nullptr;

    JSVM\_CALL(OH\_JSVM\_CreateDate(env, value, &returnValue));

    bool isDate = false;
    JSVM\_CALL(OH\_JSVM\_IsDate(env, returnValue, &isDate));
    if (!isDate) {
        OH\_LOG\_ERROR(LOG\_APP, "JSVM IsDate fail");
        return returnValue;
    }

    value = 0;
    JSVM\_CALL(OH\_JSVM\_GetDateValue(env, returnValue, &value));

    uint64\_t time = static\_cast<uint64\_t>(value) / 1000;
    char \*date = ctime(reinterpret\_cast<time\_t \*>(&time));
    OH\_LOG\_INFO(LOG\_APP, "JSVM CreateDate success:%{public}s", date);

    return returnValue;
}

// Register the CreateDate callback.
static JSVM\_CallbackStruct param\[\] = {
    {.data = nullptr, .callback = CreateDate},
};
static JSVM\_CallbackStruct \*method = param;
// Set a property descriptor named createDate and associate it with a callback. This allows the createDate callback to be called from JS.
static JSVM\_PropertyDescriptor descriptor\[\] = {
    {"createDate", nullptr, method, nullptr, nullptr, nullptr, JSVM\_DEFAULT},
};
// Call the C++ code from JS.
const char \*srcCallNative = R"JS(createDate())JS";

Expected result:

JSVM CreateDate success:Mon Jul 7 10:42:34 2025

## OH\_JSVM\_GetDateValue

Use **OH\_JSVM\_GetDateValue** to obtain the C double primitive of the time value for the given JS **Date** object.

CPP code:

#include <ctime>
// Define OH\_JSVM\_GetDateValue.
static JSVM\_Value GetDateValue(JSVM\_Env env, JSVM\_CallbackInfo info) {
    size\_t argc = 1;
    JSVM\_Value args\[1\] = {nullptr};
    JSVM\_CALL(OH\_JSVM\_GetCbInfo(env, info, &argc, args, nullptr, nullptr));
    // Obtain the Unix timestamp passed in.
    double value = 0;
    JSVM\_CALL(OH\_JSVM\_GetDateValue(env, args\[0\], &value));
   
    // Convert the obtained Unix Time Stamp time into a date string for printing.
    uint64\_t time = static\_cast<uint64\_t>(value) / 1000;
    char \*date = ctime(reinterpret\_cast<time\_t \*>(&time));
    OH\_LOG\_INFO(LOG\_APP, "JSVM GetDateValue success:%{public}s", date);
   
    JSVM\_Value returnValue = nullptr;
    JSVM\_CALL(OH\_JSVM\_CreateDouble(env, value, &returnValue));
    return returnValue;
}

// Register the CreateDate callback.
static JSVM\_CallbackStruct param\[\] = {
    {.data = nullptr, .callback = GetDateValue},
};
static JSVM\_CallbackStruct \*method = param;
// Set a property descriptor named createDate and associate it with a callback. This allows the createDate callback to be called from JS.
static JSVM\_PropertyDescriptor descriptor\[\] = {
    {"getDateValue", nullptr, method++, nullptr, nullptr, nullptr, JSVM\_DEFAULT},
};
// Call the C++ code from JS.
const char \*srcCallNative = R"JS(getDateValue(new Date(Date.now())))JS";

Expected result:

JSVM GetDateValue success:Mon Jul 7 10:47:08 2025

## OH\_JSVM\_IsDate

Use **OH\_JSVM\_IsDate** to check whether a JS object is a date.

CPP code:

// Define OH\_JSVM\_IsDate.
static JSVM\_Value IsDate(JSVM\_Env env, JSVM\_CallbackInfo info) {
    size\_t argc = 1;
    JSVM\_Value args\[1\] = {nullptr};
    JSVM\_CALL(OH\_JSVM\_GetCbInfo(env, info, &argc, args, nullptr, nullptr));
    bool isDate = false;
    JSVM\_CALL(OH\_JSVM\_IsDate(env, args\[0\], &isDate));
    OH\_LOG\_INFO(LOG\_APP, "JSVM IsDate success:%{public}d", isDate);
    
    JSVM\_Value result = nullptr;
    JSVM\_CALL(OH\_JSVM\_GetBoolean(env, isDate, &result));
    return result;
}
// Register the CreateDate callback.
static JSVM\_CallbackStruct param\[\] = {
    {.data = nullptr, .callback = IsDate},
};
static JSVM\_CallbackStruct \*method = param;
// Set a property descriptor named createDate and associate it with a callback. This allows the createDate callback to be called from JS.
static JSVM\_PropertyDescriptor descriptor\[\] = {
    {"isDate", nullptr, method, nullptr, nullptr, nullptr, JSVM\_DEFAULT},
};
// Call the C++ code from JS.
const char \*srcCallNative = R"JS(isDate(new Date(Date.now())))JS";

Expected result:

JSVM IsDate success:1
