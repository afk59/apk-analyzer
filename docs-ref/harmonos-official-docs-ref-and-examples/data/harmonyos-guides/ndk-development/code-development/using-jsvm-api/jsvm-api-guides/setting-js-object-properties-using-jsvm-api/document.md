# Setting JS Object Properties Using JSVM-API

#### Introduction

This topic walks you through on how to obtain and set properties of a JavaScript (JS) object using JSVM-API. Properly using these APIs help to implement more complex functionalities and logic.

#### Basic Concepts

Before working with JS objects using JSVM-API, you need to understand the following concepts:

-   Object: a composite data type that allows values of different types in an independent entity in JS. An object is a collection of properties and methods. A property is a value associated with the object, and a method is an operation that the object can perform.
-   Property: a feature, in the key-value format, of an object in JS. Each property has a name (key or identifier) and a value. The property value can be of any data type, including the basic type, object, and function.
-   Enumerable property: a property in JS with **enumerable** set to **true**. An enumerable property can be traversed by **for...in**.
-   Own property: a property defined for an object rather than inherited from the prototype chain.

#### Available APIs

| API | Description |
| :-- | :-- |
| OH\_JSVM\_GetPropertyNames | Obtains the names of all enumerable properties of a JS object as a JS array. |
| OH\_JSVM\_SetProperty | Sets a property for a JS object. |
| OH\_JSVM\_GetProperty | Obtains a property from a JS object. |
| OH\_JSVM\_HasProperty | Checks whether a JS object has the specified property. |
| OH\_JSVM\_DeleteProperty | Deletes a property from a JS object. |
| OH\_JSVM\_HasOwnProperty | Checks whether an object has the own property with the specified name. |
| OH\_JSVM\_SetNamedProperty | Sets a property with the given property name for a JS object. This API is equivalent to calling **OH\_JSVM\_SetProperty** with a **JSVM\_Value** created from the string passed in as **utf8Name**. |
| OH\_JSVM\_GetNamedProperty | Obtains a property from a JS object. This API is equivalent to calling **OH\_JSVM\_GetProperty** with a **JSVM\_Value** created from the string passed in as **utf8Name**. |
| OH\_JSVM\_HasNamedProperty | Checks whether a JS object has the specified property. This API is equivalent to calling **OH\_JSVM\_HasProperty** with a **JSVM\_Value** created from the string passed in as **utf8Name**. |
| OH\_JSVM\_DefineProperties | Defines multiple properties for a JS object. |
| OH\_JSVM\_GetAllPropertyNames | Obtains the names of all available properties of a JS object as a JS array. |

#### Example

If you are just starting out with JSVM-API, see [JSVM-API Development Process](../../jsvm-api-development-process/document.md). The following demonstrates only the C++ code involved in related APIs.

## OH\_JSVM\_GetPropertyNames

Call **OH\_JSVM\_GetPropertyNames** to obtain names of all enumerable properties of a JS object in the form of a string array. If the operation is successful, **JSVM\_OK** is returned.

CPP code:

// Define OH\_JSVM\_GetPropertyNames.
static JSVM\_Value GetPropertyNames(JSVM\_Env env, JSVM\_CallbackInfo info)
{
    // Pass in obj as a parameter.
    size\_t argc = 1;
    JSVM\_Value args\[1\] = {nullptr};
    OH\_JSVM\_GetCbInfo(env, info, &argc, args, nullptr, nullptr);
    // Obtain the names of all the enumerable properties of the object in the form of a string array and output the string array in result.
    JSVM\_Value result = nullptr;
    JSVM\_Status status = OH\_JSVM\_GetPropertyNames(env, args\[0\], &result);
    if (status != JSVM\_OK) {
        OH\_JSVM\_ThrowError(env, nullptr, "Failed to get propertynames");
        return nullptr;
    } else {
        OH\_LOG\_INFO(LOG\_APP, "JSVM OH\_JSVM\_GetPropertyNames success");
    }
    return result;
}
// Register the GetPropertyNames callback.
static JSVM\_CallbackStruct param\[\] = {
    {.data = nullptr, .callback = GetPropertyNames},
};
static JSVM\_CallbackStruct \*method = param;
// Alias for the GetPropertyNames method to be called from JS.
static JSVM\_PropertyDescriptor descriptor\[\] = {
    {"getPropertyNames", nullptr, method++, nullptr, nullptr, nullptr, JSVM\_DEFAULT},
};

// Call the C++ code from JS.
const char \*srcCallNative = R"JS(
    let obj = '{ data: 0, message: "hello world"}';
    let script = getPropertyNames(obj);
)JS";

Expected result:

JSVM OH\_JSVM\_GetPropertyNames success

## OH\_JSVM\_SetProperty

Call **OH\_JSVM\_SetProperty** to set a property for an object.

CPP code:

// Define OH\_JSVM\_SetProperty.
static JSVM\_Value SetProperty(JSVM\_Env env, JSVM\_CallbackInfo info)
{
    // Obtain the parameters passed from JS. The first parameter specifies the object, the second parameter specifies the property name, and the third parameter specifies the property value to set.
    size\_t argc = 3;
    JSVM\_Value args\[3\] = {nullptr};
    JSVM\_Status status = OH\_JSVM\_GetCbInfo(env, info, &argc, args, nullptr, nullptr);
    if (status != JSVM\_OK) {
        OH\_JSVM\_ThrowError(env, nullptr, "JSVM OH\_JSVM\_GetCbInfo fail");
        return nullptr;
    }
    // Call OH\_JSVM\_SetProperty to set the property name and value to the object. If the operation fails, an error is thrown.
    status = OH\_JSVM\_SetProperty(env, args\[0\], args\[1\], args\[2\]);
    if (status != JSVM\_OK) {
        OH\_JSVM\_ThrowError(env, nullptr, "JSVM OH\_JSVM\_SetProperty fail");
        return nullptr;
    } else {
        OH\_LOG\_INFO(LOG\_APP, "JSVM OH\_JSVM\_SetProperty success");
    }
    // Return the object that is successfully set.
    return args\[0\];
}
// Register the SetProperty callback.
static JSVM\_CallbackStruct param\[\] = {
    {.data = nullptr, .callback = SetProperty},
};
static JSVM\_CallbackStruct \*method = param;
// Alias for the SetProperty method to be called from JS.
static JSVM\_PropertyDescriptor descriptor\[\] = {
    {"setProperty", nullptr, method++, nullptr, nullptr, nullptr, JSVM\_DEFAULT},
};

// Call the C++ code from JS.
const char \*srcCallNative = R"JS(
    let obj = { data: 0, message: "hello world", 50: 1};
    setProperty(obj, "code", "hi")
)JS";

Expected result:

JSVM OH\_JSVM\_SetProperty success

## OH\_JSVM\_GetProperty

Call **OH\_JSVM\_GetProperty** to obtain a property value of a JS object based on the property name.

CPP code:

// Define OH\_JSVM\_GetProperty.
static JSVM\_Value GetProperty(JSVM\_Env env, JSVM\_CallbackInfo info)
{
    // Obtain the two parameters passed from JS.
    size\_t argc = 2;
    JSVM\_Value args\[2\] = {nullptr};
    OH\_JSVM\_GetCbInfo(env, info, &argc, args, nullptr, nullptr);
    // The first parameter specifies the target object, and the second specifies the property name. Call OH\_JSVM\_GetProperty to obtain the value of the property.
    JSVM\_Value result = nullptr;
    JSVM\_Status status = OH\_JSVM\_GetProperty(env, args\[0\], args\[1\], &result);
    if (status != JSVM\_OK) {
        OH\_JSVM\_ThrowError(env, nullptr, "JSVM OH\_JSVM\_GetProperty fail");
        return nullptr;
    } else {
        OH\_LOG\_INFO(LOG\_APP, "JSVM OH\_JSVM\_GetProperty success");
    }
    return result;
}
// Register the GetProperty callback.
static JSVM\_CallbackStruct param\[\] = {
    {.data = nullptr, .callback = GetProperty},
};
static JSVM\_CallbackStruct \*method = param;
// Alias for the GetProperty method to be called from JS.
static JSVM\_PropertyDescriptor descriptor\[\] = {
    {"getProperty", nullptr, method++, nullptr, nullptr, nullptr, JSVM\_DEFAULT},
};

// Call the C++ code from JS.
const char \*srcCallNative = R"JS(
    let obj = { data: 0, message: "hello world", 50: 1};
    getProperty(obj, "message")
)JS";

Expected result:

JSVM OH\_JSVM\_GetProperty success

## OH\_JSVM\_HasProperty

Call **OH\_JSVM\_HasProperty** to check whether an object has the specified property. This can prevent the exception or error caused by access to a property that does not exist.

CPP code:

// Define OH\_JSVM\_HasProperty.
static JSVM\_Value HasProperty(JSVM\_Env env, JSVM\_CallbackInfo info)
{
    // Pass in two parameters from JS. The first parameter specifies the target object, and the second parameter specifies the property to check.
    size\_t argc = 2;
    JSVM\_Value args\[2\] = {nullptr};
    OH\_JSVM\_GetCbInfo(env, info, &argc, args, nullptr, nullptr);
    // Pass the parameters to OH\_JSVM\_HasProperty. If the API is successfully called, convert the result to JSVM\_Value and return JSVM\_Value. Otherwise, throw an error.
    bool result = false;
    JSVM\_Status status = OH\_JSVM\_HasProperty(env, args\[0\], args\[1\], &result);
    if (status != JSVM\_OK) {
        OH\_JSVM\_ThrowError(env, nullptr, "JSVM OH\_JSVM\_HasProperty fail");
        return nullptr;
    } else {
        OH\_LOG\_INFO(LOG\_APP, "JSVM OH\_JSVM\_HasProperty success:%{public}d", result);
    }
    // If the property exists in the object, output true, convert the result to JSVM\_Value, and return JSVM\_Value.
    JSVM\_Value returnResult = nullptr;
    OH\_JSVM\_GetBoolean(env, result, &returnResult);
    return returnResult;
}
// Register the HasProperty callback.
static JSVM\_CallbackStruct param\[\] = {
    {.data = nullptr, .callback = HasProperty},
};
static JSVM\_CallbackStruct \*method = param;
// Alias for the HasProperty method to be called from JS.
static JSVM\_PropertyDescriptor descriptor\[\] = {
    {"hasProperty", nullptr, method++, nullptr, nullptr, nullptr, JSVM\_DEFAULT},
};

// Call the C++ code from JS.
const char \*srcCallNative = R"JS(
    let obj = { data: 0, message: "hello world", 50: 1};
    hasProperty(obj, "data")
    hasProperty(obj, 0)
)JS";

Expected result:

// hasProperty (obj, "data") output
JSVM OH\_JSVM\_HasProperty success:1
// Output of hasProperty (obj, 0).
JSVM OH\_JSVM\_HasProperty success:0

## OH\_JSVM\_DeleteProperty

Call **OH\_JSVM\_DeleteProperty** to delete the property specified by **key** from an object.

If the object is a non-extensible object or the property is not configurable, the property cannot be deleted.

CPP code:

// Define OH\_JSVM\_DeleteProperty.
static JSVM\_Value DeleteProperty(JSVM\_Env env, JSVM\_CallbackInfo info)
{
    // Obtain the two parameters passed from JS.
    size\_t argc = 2;
    JSVM\_Value args\[2\] = {nullptr};
    OH\_JSVM\_GetCbInfo(env, info, &argc, args, nullptr, nullptr);
    JSVM\_ValueType valueType;
    OH\_JSVM\_Typeof(env, args\[0\], &valueType);
    if (valueType != JSVM\_OBJECT) {
        OH\_JSVM\_ThrowError(env, nullptr, "Expects an object as argument.");
        return nullptr;
    }
    // Delete the specified property from the object and return a bool value indicating whether the deletion is successful.
    bool result = false;
    JSVM\_Status status = OH\_JSVM\_DeleteProperty(env, args\[0\], args\[1\], &result);
    if (status != JSVM\_OK) {
        OH\_JSVM\_ThrowError(env, nullptr, "JSVM OH\_JSVM\_DeleteProperty failed");
        return nullptr;
    } else {
        OH\_LOG\_INFO(LOG\_APP, "JSVM OH\_JSVM\_DeleteProperty success:%{public}d", result);
    }
    // Convert the bool value to JSVM\_value and return JSVM\_value.
    JSVM\_Value ret;
    OH\_JSVM\_GetBoolean(env, result, &ret);
    return ret;
}
// Register the DeleteProperty callback.
static JSVM\_CallbackStruct param\[\] = {
    {.data = nullptr, .callback = DeleteProperty},
};
static JSVM\_CallbackStruct \*method = param;
// Alias for the DeleteProperty method to be called from JS.
static JSVM\_PropertyDescriptor descriptor\[\] = {
    {"deleteProperty", nullptr, method++, nullptr, nullptr, nullptr, JSVM\_DEFAULT},
};

// Call the C++ code from JS.
const char \*srcCallNative = R"JS(
    let obj = { data: 0, message: "hello world", 50: 1};
    deleteProperty(obj, "message")
)JS";

Expected result:

JSVM OH\_JSVM\_DeleteProperty success:1

## OH\_JSVM\_HasOwnProperty

Call **OH\_JSVM\_HasOwnProperty** to check whether a JS object has its own property.

CPP code:

// Define OH\_JSVM\_HasOwnProperty.
static JSVM\_Value HasOwnProperty(JSVM\_Env env, JSVM\_CallbackInfo info)
{
    // Obtain the two parameters passed from JS.
    size\_t argc = 2;
    JSVM\_Value args\[2\] = {nullptr};
    OH\_JSVM\_GetCbInfo(env, info, &argc, args, nullptr, nullptr);
    // Check whether the first parameter is an object.
    JSVM\_ValueType valueType1;
    OH\_JSVM\_Typeof(env, args\[0\], &valueType1);
    if (valueType1 != JSVM\_OBJECT) {
        OH\_JSVM\_ThrowError(env, nullptr, "First argument must be an object.");
        return nullptr;
    }
    // Check whether the second parameter is a string.
    JSVM\_ValueType valuetype2;
    OH\_JSVM\_Typeof(env, args\[1\], &valuetype2);
    if (valuetype2 != JSVM\_STRING ) {
        OH\_JSVM\_ThrowError(env, nullptr, "Second argument must be a string.");
        return nullptr;
    }
    // Check whether the object has the specified property. The result is in hasProperty.
    bool hasProperty = false;
    JSVM\_Status status = OH\_JSVM\_HasOwnProperty(env, args\[0\], args\[1\], &hasProperty);
    if (status != JSVM\_OK) {
        OH\_JSVM\_ThrowError(env, nullptr, "JSVM OH\_JSVM\_HasOwnProperty failed");
        return nullptr;
    } else {
        OH\_LOG\_INFO(LOG\_APP, "JSVM OH\_JSVM\_HasOwnProperty success:%{public}d", hasProperty);
    }
    // Convert the bool value to JSVM\_Value and return JSVM\_value.
    JSVM\_Value result;
    OH\_JSVM\_GetBoolean(env, hasProperty, &result);
    return result;
}
// Register the HasOwnProperty callback.
static JSVM\_CallbackStruct param\[\] = {
    {.data = nullptr, .callback = HasOwnProperty},
};
static JSVM\_CallbackStruct \*method = param;
// Alias for the HasOwnProperty method to be called from JS.
static JSVM\_PropertyDescriptor descriptor\[\] = {
    {"hasOwnProperty", nullptr, method++, nullptr, nullptr, nullptr, JSVM\_DEFAULT},
};

// Call the C++ code from JS.
const char \*srcCallNative = R"JS(
    let obj = { data: 0, message: "hello world", 50: 1};
    hasOwnProperty(obj, "message")
    hasOwnProperty(obj, "\_\_defineGetter\_\_")
)JS";

Expected result:

// hasOwnProperty (obj, "message") output
JSVM OH\_JSVM\_HasOwnProperty success:1
// hasOwnProperty(obj, "\_\_defineGetter\_\_") output
// \`\_\_defineGetter\_\_\` is the prototype method of the object, not OwnProperty. The expected return value is 0.
JSVM OH\_JSVM\_HasOwnProperty success:0

## OH\_JSVM\_SetNamedProperty

Call **OH\_JSVM\_SetNamedProperty** to set a property for a JS object.

CPP code:

// Define OH\_JSVM\_SetNamedProperty.
static JSVM\_Value SetNamedProperty(JSVM\_Env env, JSVM\_CallbackInfo info)
{
    // Obtain the parameter passed from JS.
    size\_t argc = 1;
    JSVM\_Value str;
    char strKey\[32\] = "";
    OH\_JSVM\_GetCbInfo(env, info, &argc, &str, nullptr, nullptr);
    // Obtain the string passed in and store it in strKey.
    size\_t keyLength = 0;
    OH\_JSVM\_GetValueStringUtf8(env, str, strKey, 32, &keyLength);
    // Create an object.
    JSVM\_Value newObj;
    OH\_JSVM\_CreateObject(env, &newObj);
    // Set the property value to 1234.
    int32\_t value = 1234;
    JSVM\_Value numValue;
    OH\_JSVM\_CreateInt32(env, value, &numValue);
    // Associate the integer value with the property name.
    JSVM\_Status status = OH\_JSVM\_SetNamedProperty(env, newObj, strKey, numValue);
    if (status != JSVM\_OK) {
        OH\_JSVM\_ThrowError(env, nullptr, "JSVM OH\_JSVM\_SetNamedProperty failed");
        return nullptr;
    } else {
        OH\_LOG\_INFO(LOG\_APP, "JSVM OH\_JSVM\_SetNamedProperty success");
    }
    // Return the newly created object with the property set.
    return newObj;
}
// Register the SetNamedProperty callback.
static JSVM\_CallbackStruct param\[\] = {
    {.data = nullptr, .callback = SetNamedProperty},
};
static JSVM\_CallbackStruct \*method = param;
// Alias for the SetNamedProperty method to be called from JS.
static JSVM\_PropertyDescriptor descriptor\[\] = {
    {"setNamedProperty", nullptr, method++, nullptr, nullptr, nullptr, JSVM\_DEFAULT},
};

// Call the C++ code from JS.
const char \*srcCallNative = R"JS(
    setNamedProperty("message")
)JS";

Expected result:

JSVM OH\_JSVM\_SetNamedProperty success

## OH\_JSVM\_GetNamedProperty

Call **OH\_JSVM\_GetNamedProperty** to obtain the value of the specified property from a JS object.

CPP code:

// Define OH\_JSVM\_GetNamedProperty.
static JSVM\_Value GetNamedProperty(JSVM\_Env env, JSVM\_CallbackInfo info)
{
    // Obtain the two parameters passed from JS.
    size\_t argc = 2;
    JSVM\_Value args\[2\] = {nullptr};
    char strKey\[32\] = "";
    OH\_JSVM\_GetCbInfo(env, info, &argc, args, nullptr, nullptr);
    // Obtain the name of the property to obtain.
    size\_t keyLength = 0;
    OH\_JSVM\_GetValueStringUtf8(env, args\[1\], strKey, 32, &keyLength);
    // Obtain the value of the property and store it in result.
    JSVM\_Value result;
    JSVM\_Status status = OH\_JSVM\_GetNamedProperty(env, args\[0\], strKey, &result);
    if (status != JSVM\_OK) {
        OH\_JSVM\_ThrowError(env, nullptr, "JSVM OH\_JSVM\_GetNamedProperty failed");
        return nullptr;
    } else {
        OH\_LOG\_INFO(LOG\_APP, "JSVM OH\_JSVM\_GetNamedProperty success");
    }
    return result;
}
// Register the GetNamedProperty callback.
static JSVM\_CallbackStruct param\[\] = {
    {.data = nullptr, .callback = GetNamedProperty},
};
static JSVM\_CallbackStruct \*method = param;
// Alias for the GetNamedProperty method to be called from JS.
static JSVM\_PropertyDescriptor descriptor\[\] = {
    {"getNamedProperty", nullptr, method++, nullptr, nullptr, nullptr, JSVM\_DEFAULT},
};

// Call the C++ code from JS.
const char \*srcCallNative = R"JS(
    let obj = { data: 0, message: "hello world", 50: 1};
    getNamedProperty(obj, "message")
)JS";

Expected result:

JSVM OH\_JSVM\_GetNamedProperty success

## OH\_JSVM\_HasNamedProperty

Call **OH\_JSVM\_HasNamedProperty** to check whether a JS object contains the specified property.

CPP code:

// Define OH\_JSVM\_HasNamedProperty.
static JSVM\_Value HasNamedProperty(JSVM\_Env env, JSVM\_CallbackInfo info)
{
    // Obtain the two parameters passed from JS.
    size\_t argc = 2;
    JSVM\_Value args\[2\] = {nullptr};
    char strKey\[32\] = "";
    OH\_JSVM\_GetCbInfo(env, info, &argc, args, nullptr, nullptr);
    // Obtain the property name.
    size\_t keyLength = 0;
    OH\_JSVM\_GetValueStringUtf8(env, args\[1\], strKey, 32, &keyLength);
    // Check whether the object has the specified property. The result is in hasProperty.
    bool hasProperty = false;
    JSVM\_Status status = OH\_JSVM\_HasNamedProperty(env, args\[0\], strKey, &hasProperty);
    if (status != JSVM\_OK) {
        OH\_JSVM\_ThrowError(env, nullptr, "JSVM OH\_JSVM\_HasNamedProperty failed");
        return nullptr;
    } else {
        OH\_LOG\_INFO(LOG\_APP, "JSVM OH\_JSVM\_HasNamedProperty success:%{public}d", hasProperty);
    }
    // Convert the bool value to JSVM\_Value and return JSVM\_value.
    JSVM\_Value result;
    OH\_JSVM\_GetBoolean(env, hasProperty, &result);
    return result;
}
// Register the HasNamedProperty callback.
static JSVM\_CallbackStruct param\[\] = {
    {.data = nullptr, .callback = HasNamedProperty},
};
static JSVM\_CallbackStruct \*method = param;
// Alias for the HasNamedProperty method to be called from JS.
static JSVM\_PropertyDescriptor descriptor\[\] = {
    {"hasNamedProperty", nullptr, method++, nullptr, nullptr, nullptr, JSVM\_DEFAULT},
};

// Call the C++ code from JS.
const char \*srcCallNative = R"JS(
    let obj = { data: 0, message: "hello world", 50: 1};
    hasNamedProperty(obj, "message")
)JS";

Expected result:

JSVM OH\_JSVM\_HasNamedProperty success:1

## OH\_JSVM\_DefineProperties

Call **OH\_JSVM\_DefineProperties** to customize one or more properties for an object.

CPP code:

#include <fstream>
#include <string>
// Callback for defineMethodPropertiesExample in the property descriptor list.
static JSVM\_Value DefineMethodPropertiesExample(JSVM\_Env env, JSVM\_CallbackInfo info)
{
    int32\_t propValue = 26;
    JSVM\_Value returnValue;
    OH\_JSVM\_CreateInt32(env, propValue, &returnValue);
    return returnValue;
}
// Callback for getterCallback in the property descriptor list.
static JSVM\_Value GetterCallback(JSVM\_Env env, JSVM\_CallbackInfo info)
{
    JSVM\_Value result;
    const char \*str = "Hello world!";
    size\_t length = strlen(str);
    // Create property values.
    OH\_JSVM\_CreateStringUtf8(env, str, length, &result);
    return result;
}

// Function to execute a JS string.
static JSVM\_Value RunScriptAndLogResult(JSVM\_Env env, const std::string &srcCode) {
    JSVM\_Value sourceCodeValue;
    OH\_JSVM\_CreateStringUtf8(env, srcCode.c\_str(), srcCode.size(), &sourceCodeValue);
    JSVM\_Script script;
    // Compile the JS code string and return the compiled script.
    OH\_JSVM\_CompileScript(env, sourceCodeValue, nullptr, 0, true, nullptr, &script);
    JSVM\_Value jsVmResult;
    // Execute the JS script.
    OH\_JSVM\_RunScript(env, script, &jsVmResult);
    return jsVmResult;
}

// Define OH\_JSVM\_DefineProperties.
static JSVM\_Value DefineProperties(JSVM\_Env env, JSVM\_CallbackInfo info) {
    // Obtain an empty object passed from JS.
    size\_t argc = 1;
    JSVM\_Value argv\[1\] = {nullptr};
    OH\_JSVM\_GetCbInfo(env, info, &argc, argv, nullptr, nullptr);
    // Create a property value of the string type.
    JSVM\_Value stringValue;
    OH\_JSVM\_CreateStringUtf8(env, "Hello!", JSVM\_AUTO\_LENGTH, &stringValue);
    // Create the callback lists corresponding to the property descriptors.
    JSVM\_CallbackStruct param\[\] = {
        {.data = nullptr, .callback = DefineMethodPropertiesExample},
        {.data = nullptr, .callback = GetterCallback},

    };
    // Create a property descriptor list. For details, see the definition of JSVM\_PropertyDescriptor.
    JSVM\_PropertyDescriptor descriptor\[\] = {
        // Define a property value of the method type.
        {"defineMethodPropertiesExample", nullptr, &param\[0\], nullptr, nullptr, nullptr, JSVM\_DEFAULT},
        // Define the property value of the string type.
        {"defineStringPropertiesExample", nullptr, nullptr, nullptr, nullptr, stringValue, JSVM\_DEFAULT},
        // Define the property value of the getter type.
        {"getterCallback", nullptr, nullptr, &param\[1\], nullptr, nullptr,JSVM\_DEFAULT}};
    // Create properties for the obj object based on the property descriptor list.
    JSVM\_Status statusProperty;
    statusProperty = OH\_JSVM\_DefineProperties(env, \*argv, sizeof(descriptor) / sizeof(descriptor\[0\]), descriptor);
    if (statusProperty != JSVM\_OK) {
        OH\_JSVM\_ThrowError(env, nullptr, "JSVM DefineProperties fail");
        return nullptr;
    }
    // Call the properties added to the obj object.
    // Run obj.defineMethodPropertiesExample() and return the result to JS.
    static std::string srcMethod;
    srcMethod = R"JS(obj.defineMethodPropertiesExample();)JS";
    JSVM\_Value jsVmResult = RunScriptAndLogResult(env, srcMethod);
    if (jsVmResult != nullptr) {
        int32\_t number;
        OH\_JSVM\_GetValueInt32(env, jsVmResult, &number);
        OH\_LOG\_INFO(LOG\_APP, "JSVM DefineMethodPropertiesExample success:%{public}d", number);
    }
    // Run obj.defineStringPropertiesExample() and return the result to JS.
    static std::string srcString;
    srcString = R"JS(obj.defineStringPropertiesExample;)JS";
    JSVM\_Value jsVmResult1 = RunScriptAndLogResult(env, srcString);
    if (jsVmResult1 != nullptr) {
        size\_t length = 0;
        OH\_JSVM\_GetValueStringUtf8(env, jsVmResult1, nullptr, 0, &length);
        char \*buf = (char \*)malloc(length + 1);
        if (buf == nullptr) {
            OH\_LOG\_ERROR(LOG\_APP, "malloc failed");
            return nullptr;
        }
        memset(buf, 0, length + 1);
        OH\_JSVM\_GetValueStringUtf8(env, jsVmResult1, buf, length + 1, &length);
        OH\_LOG\_INFO(LOG\_APP, "JSVM defineStringPropertiesExample success:%{public}s", buf);
        free(buf);
    }
    // Call getterCallback() of obj and return the result string to JS.
    static std::string srcGetter;
    srcGetter = R"JS(obj.getterCallback;)JS";
    JSVM\_Value jsVmResult2 = RunScriptAndLogResult(env, srcGetter);
    if (jsVmResult2 != nullptr) {
        size\_t length = 0;
        OH\_JSVM\_GetValueStringUtf8(env, jsVmResult2, nullptr, 0, &length);
        char \*buf = (char \*)malloc(length + 1);
        if (buf == nullptr) {
            OH\_LOG\_ERROR(LOG\_APP, "malloc failed");
            return nullptr;
        }
        memset(buf, 0, length + 1);
        OH\_JSVM\_GetValueStringUtf8(env, jsVmResult2, buf, length + 1, &length);
        OH\_LOG\_INFO(LOG\_APP, "JSVM getterCallback success:%{public}s", buf);
        free(buf);
    }
    return jsVmResult;
}

// Register the DefineProperties callback.
static JSVM\_CallbackStruct param\[\] = {
    {.data = nullptr, .callback = DefineProperties},
};
static JSVM\_CallbackStruct \*method = param;
// Alias for the DefineProperties method to be called from JS.
static JSVM\_PropertyDescriptor descriptor\[\] = {
    {"defineProperties", nullptr, method++, nullptr, nullptr, nullptr, JSVM\_DEFAULT},
};

// Call the C++ code from JS.
const char \*srcCallNative = R"JS(
    let obj = {};
    defineProperties(obj)
)JS";

Expected result:

JSVM DefineMethodPropertiesExample success:26
JSVM defineStringPropertiesExample success:Hello!
JSVM getterCallback success:Hello world!

## OH\_JSVM\_GetAllPropertyNames

Call **OH\_JSVM\_GetAllPropertyNames** to obtain the names of all enumerable properties of a JS object as a JS array.

CPP code:

// Define OH\_JSVM\_GetAllPropertyNames.
static JSVM\_Value GetAllPropertyNames(JSVM\_Env env, JSVM\_CallbackInfo info)
{
    // Obtain the parameter passed from JS.
    size\_t argc = 1;
    JSVM\_Value args\[1\];
    OH\_JSVM\_GetCbInfo(env, info, &argc, args, nullptr, nullptr);
    // Obtain names of all properties (own properties) of the specified object.
    JSVM\_Value result;
    JSVM\_Status status = OH\_JSVM\_GetAllPropertyNames(env, args\[0\],
                                         JSVM\_KeyCollectionMode::JSVM\_KEY\_OWN\_ONLY,
                                         JSVM\_KeyFilter::JSVM\_KEY\_WRITABLE,
                                         JSVM\_KeyConversion::JSVM\_KEY\_NUMBERS\_TO\_STRINGS, &result);
    if (status != JSVM\_OK) {
        OH\_JSVM\_ThrowError(env, nullptr, "Failed to get allpropertynames");
        return nullptr;
    } else {
        OH\_LOG\_INFO(LOG\_APP, "JSVM OH\_JSVM\_GetAllPropertyNames success");
    }
    return result;
}
// Register the GetAllPropertyNames callback.
static JSVM\_CallbackStruct param\[\] = {
    {.data = nullptr, .callback = GetAllPropertyNames},
};
static JSVM\_CallbackStruct \*method = param;
// Alias for the GetAllPropertyNames method to be called from JS.
static JSVM\_PropertyDescriptor descriptor\[\] = {
    {"getAllPropertyNames", nullptr, method++, nullptr, nullptr, nullptr, JSVM\_DEFAULT},
};

// Call the C++ code from JS.
const char \*srcCallNative = R"JS(
    let obj = '{ data: 0, message: "hello world", 50: 1}';
    let script = getAllPropertyNames(obj);
)JS";

Expected result:

JSVM OH\_JSVM\_GetAllPropertyNames success
