# Working with Wrapper Objects Using JSVM-API

#### Introduction

This topic walks you through on how to use JSVM-API to quickly determine the wrapper object.

#### Basic Concepts

JSVM-API provides the following APIs to quickly determine five wrapper objects.

#### Available APIs

| API | Description |
| :-- | :-- |
| OH\_JSVM\_IsNumberObject | Checks whether the result is a number object. |
| OH\_JSVM\_IsBooleanObject | Checks whether the result is a Boolean object. |
| OH\_JSVM\_IsBigIntObject | Checks whether the result is a BigInt object. |
| OH\_JSVM\_IsStringObject | Checks whether the result is a string object. |
| OH\_JSVM\_IsSymbolObject | Checks whether the result is a symbol object. |

#### Example

If you are just starting out with JSVM-API, see [JSVM-API Development Process](../../jsvm-api-development-process/document.md). The following demonstrates only the C++ code involved in the APIs.

## Determining a Number Object

CPP code:

#include <string>

static JSVM\_Value WrapperObject(JSVM\_Env env, JSVM\_CallbackInfo info) {
    JSVM\_VM vm;
    OH\_JSVM\_GetVM(env, &vm);

    JSVM\_HandleScope handleScope;
    OH\_JSVM\_OpenHandleScope(env, &handleScope);
    std::string src = R"JS(new Number(42))JS";
    JSVM\_Value jsSrc;
    JSVM\_Script script;
    JSVM\_Value result;

    OH\_JSVM\_CreateStringUtf8(env, src.c\_str(), JSVM\_AUTO\_LENGTH, &jsSrc);
    OH\_JSVM\_CompileScript(env, jsSrc, nullptr, 0, true, nullptr, &script);
    OH\_JSVM\_RunScript(env, script, &result);
    bool isNumberObject = false;
    OH\_JSVM\_IsNumberObject(env, result, &isNumberObject);
    OH\_LOG\_INFO(LOG\_APP, "JSVM OH\_JSVM\_IsNumberObject: %{public}d\\n", isNumberObject);
    OH\_JSVM\_CloseHandleScope(env, handleScope);

    return nullptr;
}

static JSVM\_CallbackStruct param\[\] = {
    {.data = nullptr, .callback = WrapperObject},
};

static JSVM\_CallbackStruct \*method = param;

// Alias for the wrapperObject method to be called from JS.
static JSVM\_PropertyDescriptor descriptor\[\] = {
    {"wrapperObject", nullptr, method++, nullptr, nullptr, nullptr, JSVM\_DEFAULT},
};

// Call the C++ code from JS.
const char \*srcCallNative = R"JS(wrapperObject();)JS";

Expected result:

JSVM OH\_JSVM\_IsNumberObject: 1
