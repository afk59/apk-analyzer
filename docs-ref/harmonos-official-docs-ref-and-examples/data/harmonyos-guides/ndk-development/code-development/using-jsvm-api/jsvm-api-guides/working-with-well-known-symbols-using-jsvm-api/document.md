# Working with Well-Known Symbols Using JSVM-API

#### Introduction

This topic walks you through on how to use JSVM-API to obtain 11 well-known symbols.

#### Basic Concepts

JSVM-API provides APIs for obtaining 11 well-known symbols.

#### Available APIs

| API | Description |
| :-- | :-- |
| OH\_JSVM\_GetSymbolToStringTag | Obtains the value equivalent to the JS **Symbol.toStringTag**. |
| OH\_JSVM\_GetSymbolToPrimitive | Obtains the value equivalent to the JS **Symbol.toPrimitive**. |
| OH\_JSVM\_GetSymbolSplit | Obtains the value equivalent to the JS **Symbol.split**. |
| OH\_JSVM\_GetSymbolSearch | Obtains the value equivalent to the JS **Symbol.search**. |
| OH\_JSVM\_GetSymbolReplace | Obtains the value equivalent to the JS **Symbol.replace**. |
| OH\_JSVM\_GetSymbolMatch | Obtains the value equivalent to the JS **Symbol.match**. |
| OH\_JSVM\_GetSymbolIsConcatSpreadable | Obtains the value equivalent to the JS **Symbol.isConcatSpreadable**. |
| OH\_JSVM\_GetSymbolHasInstance | Obtains the value equivalent to the JS **Symbol.hasInstance**. |
| OH\_JSVM\_GetSymbolUnscopables | Obtains the value equivalent to the JS **Symbol.unscopables**. |
| OH\_JSVM\_GetSymbolAsyncIterator | Obtains the value equivalent to the JS **Symbol.asyncIterator**. |
| OH\_JSVM\_GetSymbolIterator | Obtains the value equivalent to the JS **Symbol.iterator**. |

#### Example

If you are just starting out with JSVM-API, see [JSVM-API Development Process](../../jsvm-api-development-process/document.md). The following demonstrates only the C++ code involved in symbol-related APIs.

## OH\_JSVM\_GetSymbolToStringTag

CPP code:

#include <string>

static JSVM\_Value WellKnownSymbols(JSVM\_Env env, JSVM\_CallbackInfo info) {
    JSVM\_VM vm;
    OH\_JSVM\_GetVM(env, &vm);

    JSVM\_HandleScope handleScope;
    OH\_JSVM\_OpenHandleScope(env, &handleScope);
    std::string src = R"JS(Symbol.toStringTag)JS";
    JSVM\_Value jsSrc;
    JSVM\_Script script;
    JSVM\_Value result1;

    OH\_JSVM\_CreateStringUtf8(env, src.c\_str(), JSVM\_AUTO\_LENGTH, &jsSrc);
    OH\_JSVM\_CompileScript(env, jsSrc, nullptr, 0, true, nullptr, &script);
    OH\_JSVM\_RunScript(env, script, &result1);
    JSVM\_Value result2;
    OH\_JSVM\_GetSymbolToStringTag(env, &result2);
    bool is\_equals = false;
    OH\_JSVM\_StrictEquals(env, result1, result2, &is\_equals);
    OH\_LOG\_INFO(LOG\_APP, "JSVM OH\_JSVM\_GetSymbolToStringTag result is correct : %{public}d\\n", is\_equals);
    OH\_JSVM\_CloseHandleScope(env, handleScope);

    return nullptr;
}

static JSVM\_CallbackStruct param\[\] = {
    {.data = nullptr, .callback = WellKnownSymbols},
};

static JSVM\_CallbackStruct \*method = param;

// Alias for the wellKnownSymbols method to be called from JS.
static JSVM\_PropertyDescriptor descriptor\[\] = {
    {"wellKnownSymbols", nullptr, method++, nullptr, nullptr, nullptr, JSVM\_DEFAULT},
};

// Call the C++ code from JS.
const char \*srcCallNative = R"JS(wellKnownSymbols();)JS";

Expected result:

JSVM OH\_JSVM\_GetSymbolToStringTag result is correct : 1
