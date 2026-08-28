# Performing JSON Operations Using JSVM-API

#### Introduction

This topic walks you through on how to use JSVM-API to manipulate data in JavaScript Object Notation (JSON).

#### Basic Concepts

-   **JSON (JavaScript Object Notation)**: a common data exchange format for data transfer, storage, and communication between the frontend and backend. It interacts with multiple programming languages and is widely used in JavaScript for data processing.

#### Available APIs

| API | Description |
| :-- | :-- |
| OH\_JSVM\_JsonParse | Parses a JSON string and stores the result in a JSON object. |
| OH\_JSVM\_JsonStringify | Converts a JS object into a JSON string stores the result in a JSVM string object. |

#### Example

If you are just starting out with JSVM-API, see [JSVM-API Development Process](../../jsvm-api-development-process/document.md). The following demonstrates only the C++ code involved in related APIs.

## OH\_JSVM\_JsonParse & OH\_JSVM\_JsonStringify

Use **OH\_JSVM\_JsonParse** to parse a JSON object and **OH\_JSVM\_JsonStringify** to output the parsing result.

CPP code:

// hello.cpp
#include <string>

// Parse a JSON number.
static JSVM\_Value JsonParseNumber(JSVM\_Env env, JSVM\_CallbackInfo info)
{
    // Set the JSON number to be parsed.
    std::string strNumber = "10.555";
    JSVM\_Value jsonString = nullptr;
    JSVM\_CALL(OH\_JSVM\_CreateStringUtf8(env, strNumber.c\_str(), strNumber.size(), &jsonString));
    JSVM\_Value jsonObject = nullptr;
    // Call OH\_JSVM\_JsonParse to parse the JSON number and store the result in a JSON object.
    JSVM\_CALL(OH\_JSVM\_JsonParse(env, jsonString, &jsonObject));
    double number = 0.0f;
    JSVM\_CALL(OH\_JSVM\_GetValueDouble(env, jsonObject, &number));
    OH\_LOG\_INFO(LOG\_APP, "Test JSVM jsonParseNumber: %{public}f", number);
    return nullptr;
}

// Parse a JSON object.
static JSVM\_Value JsonParseObject(JSVM\_Env env, JSVM\_CallbackInfo info)
{
    // Set the JSON object string to be parsed.
    std::string strObject = "{\\"first\\": \\"one\\", \\"second\\": \\"two\\", \\"third\\": \\"three\\"}";
    JSVM\_Value strJson = nullptr;
    JSVM\_CALL(OH\_JSVM\_CreateStringUtf8(env, strObject.c\_str(), strObject.size(), &strJson));
    JSVM\_Value jsonObject = nullptr;
    // Call OH\_JSVM\_JsonParse to parse the JSON string object and store the result in a JSON object.
    JSVM\_CALL(OH\_JSVM\_JsonParse(env, strJson, &jsonObject));
    JSVM\_Value jsonString = nullptr;
    // Call OH\_JSVM\_JsonStringify to convert the object into a string and store the string in a JSVM string object.
    JSVM\_CALL(OH\_JSVM\_JsonStringify(env, jsonObject, &jsonString));
    size\_t totalLen = 0;
    JSVM\_CALL(OH\_JSVM\_GetValueStringUtf8(env, jsonString, nullptr, 0, &totalLen));
    size\_t needLen = totalLen + 1;
    char\* buff = new char\[needLen\];
    JSVM\_CALL(OH\_JSVM\_GetValueStringUtf8(env, jsonString, buff, needLen, &totalLen));
    OH\_LOG\_INFO(LOG\_APP, "Test JSVM jsonParseObject: %{public}s", buff);
    delete\[\] buff;
    return nullptr;
}

// Register JsonParse callbacks.
static JSVM\_CallbackStruct param\[\] = {
    {.data = nullptr, .callback = JsonParseNumber},
    {.data = nullptr, .callback = JsonParseObject},
};

static JSVM\_CallbackStruct \*method = param;

JSVM\_PropertyDescriptor descriptor\[\] = {
    {"jsonParseNumber", nullptr, method++, nullptr, nullptr, nullptr, JSVM\_DEFAULT},
    {"jsonParseObject", nullptr, method++, nullptr, nullptr, nullptr, JSVM\_DEFAULT},
};

// JS code to be executed.
static const char \*srcCallNative = R"JS(jsonParseNumber();jsonParseObject();)JS";

#### Expected result:

Test JSVM jsonParseNumber: 10.555000

Test JSVM jsonParseObject: {"first":"one","second":"two","third":"three"}
