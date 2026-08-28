# Working with Classes Using JSVM-API

#### Introduction

JSVM-API provides APIs for managing JavaScript (JS) classes, for example, defining a JS class and creating a JS instance.

#### Basic Concepts

To begin with, it is important to understand the following basic concepts:

-   Class: a template used to create an object. It provides a way to define object properties and methods in a structured manner. Classes in JavaScript are based on prototypes. Moreover, unique syntax and semantics of classes are introduced.
-   Instance: an object created from a class. A class defines the structure and behavior of an object, and an instance is a specific representation of a class. Instantiating a class allows access to the properties and methods defined in the class. Each instance has its own property values.

#### Available APIs

| API | Description |
| :-- | :-- |
| OH\_JSVM\_NewInstance | Creates an instance from the given constructor. |
| OH\_JSVM\_GetNewTarget | Obtains the meta property **new.target** of a function. |
| OH\_JSVM\_DefineClass | Defines a JS class and associated functions within a C/C++ addon. It allows you to define a constructor, methods, and properties that can be accessed from JS. |
| OH\_JSVM\_Wrap | Wraps a native instance in a JS object. You can use **OH\_JSVM\_Unwrap()** to retrieve the native instance later. |
| OH\_JSVM\_Unwrap | Unwraps the native instance that is previously encapsulated in a JS object. |
| OH\_JSVM\_RemoveWrap | Removes the wrapping after the native instance is unwrapped from a JS object. |
| OH\_JSVM\_DefineClassWithOptions | Defines a JS class with the given class name, constructor, properties, callback handler, and parent class. The **DefineClassOptions** parameter specifies whether to set a property proxy for the defined class, reserve the internal-field slot, and set a callback when the class is called as a function. |

#### Example

If you are just starting out with JSVM-API, see [JSVM-API Development Process](../../jsvm-api-development-process/document.md). The following demonstrates only the C++ code involved in class development.

## OH\_JSVM\_NewInstance

Call **OH\_JSVM\_NewInstance** to create an instance from the given constructor.

CPP code:

// hello.cpp
#include <string.h>
#include <fstream>

std::string ToString(JSVM\_Env env, JSVM\_Value val) {
    JSVM\_Value jsonString = nullptr;
    JSVM\_CALL(OH\_JSVM\_JsonStringify(env, val, &jsonString));
    size\_t totalLen = 0;
    JSVM\_CALL(OH\_JSVM\_GetValueStringUtf8(env, jsonString, nullptr, 0, &totalLen));
    size\_t needLen = totalLen + 1;
    char\* buff = new char\[needLen\];
    std::memset(buff, 0, needLen);
    JSVM\_CALL(OH\_JSVM\_GetValueStringUtf8(env, jsonString, buff, needLen, &totalLen));
    std::string str(buff);
    delete\[\] buff;
    return str;
}

// Define OH\_JSVM\_NewInstance.
static JSVM\_Value NewInstance(JSVM\_Env env, JSVM\_CallbackInfo info) {
    // Obtain the two parameters passed from JS.
    size\_t argc = 2;
    JSVM\_Value args\[2\] = {nullptr};
    JSVM\_CALL(OH\_JSVM\_GetCbInfo(env, info, &argc, args, nullptr, nullptr));
    JSVM\_Value result = nullptr;
    // Call OH\_JSVM\_NewInstance to create an instance and return the instance created.
    JSVM\_CALL(OH\_JSVM\_NewInstance(env, args\[0\], 1, &args\[1\], &result));
    std::string str = ToString(env, result);
    OH\_LOG\_INFO(LOG\_APP, "NewInstance:%{public}s", str.c\_str());
    return nullptr;
}

// Create an instance from the given constructor.
// Register the NewInstance callback.
static JSVM\_CallbackStruct param\[\] = {
    {.data = nullptr, .callback = NewInstance},
};

static JSVM\_CallbackStruct \*method = param;

// Alias for the NewInstance method, which can be called from JS.
static JSVM\_PropertyDescriptor descriptor\[\] = {
    {"newInstance", nullptr, method++, nullptr, nullptr, nullptr, JSVM\_DEFAULT},
};

JS example:

const char \*srcCallNative = R"JS(
   function Fruit(name) {
       this.name = name;
   }
   newInstance(Fruit, "apple");
)JS";

**Execution result**

The following information is displayed in the log:

NewInstance:{"name":"apple"}

## OH\_JSVM\_GetNewTarget

Call **OH\_JSVM\_GetNewTarget** to obtain the **new.target** value in a function. In JS, **new.target** is a special meta-property used to determine whether a function or constructor is called using the **new** operator.

## OH\_JSVM\_DefineClass

Call **OH\_JSVM\_DefineClass** to define a JS class and associated functions within a C/C++ addon. It allows you to define a constructor, methods, and properties that can be accessed from JS.

CPP code:

// hello.cpp
#include <string>

JSVM\_Value CreateInstance(JSVM\_Env env, JSVM\_CallbackInfo info) {
    JSVM\_Value newTarget;
    // Obtain the new.target value of the constructor.
    JSVM\_CALL(OH\_JSVM\_GetNewTarget(env, info, &newTarget));
    OH\_LOG\_INFO(LOG\_APP, "Create Instance");
    OH\_LOG\_INFO(LOG\_APP, "NAPI MyObject::New %{public}s", newTarget != nullptr ? "newTarget != nullptr" : "newTarget == nullptr");
    JSVM\_Value jsObject = nullptr;
    JSVM\_CALL(OH\_JSVM\_CreateObject(env, &jsObject));
    JSVM\_Value jsName = nullptr;
    JSVM\_CALL(OH\_JSVM\_CreateStringUtf8(env, "name", JSVM\_AUTO\_LENGTH, &jsName));
    JSVM\_Value jsValue = nullptr;
    JSVM\_CALL(OH\_JSVM\_CreateStringUtf8(env, "lilei", JSVM\_AUTO\_LENGTH, &jsValue));
    JSVM\_CALL(OH\_JSVM\_SetProperty(env, jsObject, jsName, jsValue));
    return jsObject;
}

std::string ToString(JSVM\_Env env, JSVM\_Value val) {
    JSVM\_Value jsonString = nullptr;
    JSVM\_CALL(OH\_JSVM\_JsonStringify(env, val, &jsonString));
    size\_t totalLen = 0;
    JSVM\_CALL(OH\_JSVM\_GetValueStringUtf8(env, jsonString, nullptr, 0, &totalLen));
    size\_t needLen = totalLen + 1;
    char\* buff = new char\[needLen\];
    std::memset(buff, 0, needLen);
    JSVM\_CALL(OH\_JSVM\_GetValueStringUtf8(env, jsonString, buff, needLen, &totalLen));
    std::string str(buff);
    delete\[\] buff;
    return str;
}

// Encapsulate the struct in C++.
JSVM\_Value DefineClass(JSVM\_Env env, JSVM\_CallbackInfo info) {
    JSVM\_CallbackStruct param;
    param.data = nullptr;
    param.callback = CreateInstance;
    JSVM\_Value cons;
    // Define a class in JS.
    JSVM\_CALL(OH\_JSVM\_DefineClass(env, "MyObject", JSVM\_AUTO\_LENGTH, &param, 0, nullptr, &cons));
    JSVM\_Value instanceValue = nullptr;
    // Called as a constructor of the class.
    JSVM\_CALL(OH\_JSVM\_NewInstance(env, cons, 0, nullptr, &instanceValue));
    std::string str = ToString(env, instanceValue);
    OH\_LOG\_INFO(LOG\_APP, "NewInstance:%{public}s", str.c\_str());
    
    // Called as a common function.
    JSVM\_Value global = nullptr;
    JSVM\_CALL(OH\_JSVM\_GetGlobal(env, &global));
    JSVM\_Value key;
    JSVM\_CALL(OH\_JSVM\_CreateStringUtf8(env, "Constructor", JSVM\_AUTO\_LENGTH, &key));
    JSVM\_CALL(OH\_JSVM\_SetProperty(env, global, key, cons));
    JSVM\_Value result = nullptr;
    JSVM\_CALL(OH\_JSVM\_CallFunction(env, global, cons, 0, nullptr, &result));
    std::string buf = ToString(env, result);
    OH\_LOG\_INFO(LOG\_APP, "NewInstance:%{public}s", buf.c\_str());
    return nullptr;
}

// Register the DefineClass method.
JSVM\_CallbackStruct param\[\] = {
    {.data = nullptr, .callback = DefineClass},
};

static JSVM\_CallbackStruct \*method = param;

// Alias for the defineClass method, which can be called from JS.
static JSVM\_PropertyDescriptor descriptor\[\] = {
    {"defineClass", nullptr, method++, nullptr, nullptr, nullptr, JSVM\_DEFAULT},
};

JS example:

const char \*srcCallNative = R"JS(
    defineClass();
)JS";

**Execution result**

The following information is displayed in the log:

Create Instance

NAPI MyObject::New newTarget != nullptr

NewInstance:{"name":"lilei"}

Create Instance

NAPI MyObject::New newTarget == nullptr

NewInstance:{"name":"lilei"}

## OH\_JSVM\_Wrap

Call **OH\_JSVM\_Wrap** to wrap a native instance in a JS object. You can use **OH\_JSVM\_Unwrap()** to retrieve the native instance later.

## OH\_JSVM\_Unwrap

Call **OH\_JSVM\_Unwrap** to unwrap the native instance that is previously encapsulated in a JS object.

## OH\_JSVM\_RemoveWrap

Call **OH\_JSVM\_RemoveWrap** to remove the wrapping after the native instance is unwrapped from a JS object.

CPP code:

// hello.cpp
#include <string>

// Define OH\_JSVM\_GetNewTarget, OH\_JSVM\_DefineClass, OH\_JSVM\_Wrap, OH\_JSVM\_Unwrap, and OH\_JSVM\_RemoveWrap.

// Define the struct Object.
struct Object {
    std::string name;
    int32\_t age;
};

// Define a callback function.
static void DerefItem(JSVM\_Env env, void \*data, void \*hint) {
    OH\_LOG\_INFO(LOG\_APP, "JSVM deref\_item");
    (void)hint;
}

static JSVM\_Value WrapObject(JSVM\_Env env, JSVM\_CallbackInfo info) {
    OH\_LOG\_INFO(LOG\_APP, "JSVM wrap");
    Object obj;
    // Set a property for the object.
    obj.name = "lilei";
    obj.age = 18;
    Object \*objPointer = &obj;
    // Obtain the number of parameters in the callback and the values to be wrapped.
    size\_t argc = 1;
    JSVM\_Value toWrap = nullptr;
    JSVM\_CALL(OH\_JSVM\_GetCbInfo(env, info, &argc, &toWrap, nullptr, nullptr));
    // Call OH\_JSVM\_Wrap to wrap the custom struct object.
    JSVM\_CALL(OH\_JSVM\_Wrap(env, toWrap, reinterpret\_cast<void \*>(objPointer), DerefItem, NULL, NULL));
    Object \*data;
    // Call OH\_JSVM\_Unwrap to retrieve the native instance that is previously encapsulated in the JS object.
    JSVM\_CALL(OH\_JSVM\_Unwrap(env, toWrap, reinterpret\_cast<void \*\*>(&data)));
    OH\_LOG\_INFO(LOG\_APP, "JSVM name: %{public}s", data->name.c\_str());
    OH\_LOG\_INFO(LOG\_APP, "JSVM age: %{public}d", data->age);
    return nullptr;
}

static JSVM\_Value RemoveWrap(JSVM\_Env env, JSVM\_CallbackInfo info) {
    OH\_LOG\_INFO(LOG\_APP, "JSVM removeWrap");
    Object obj;
    // Set a property for the object.
    obj.name = "lilei";
    obj.age = 18;
    Object \*objPointer = &obj;
    // Obtain the number of parameters in the callback and the values to be wrapped.
    size\_t argc = 1;
    JSVM\_Value toWrap = nullptr;
    JSVM\_CALL(OH\_JSVM\_GetCbInfo(env, info, &argc, &toWrap, nullptr, nullptr));
    // Wrap the Object struct.
    JSVM\_CALL(OH\_JSVM\_Wrap(env, toWrap, reinterpret\_cast<void \*>(objPointer), DerefItem, NULL, NULL));
    Object \*data;
    // Unwrap the previously encapsulated object and remove the wrapping.
    JSVM\_CALL(OH\_JSVM\_RemoveWrap(env, toWrap, reinterpret\_cast<void \*\*>(&objPointer)));
    // Check whether the wrapping is removed.
    JSVM\_Status status = OH\_JSVM\_Unwrap(env, toWrap, reinterpret\_cast<void \*\*>(&data));
    if (status != JSVM\_OK) {
        OH\_LOG\_INFO(LOG\_APP, "JSVM OH\_JSVM\_RemoveWrap success");
    }
    return nullptr;
}

// Register the WrapObject and RemoveWrap callbacks.
static JSVM\_CallbackStruct param\[\] = {
    {.data = nullptr, .callback = WrapObject},
    {.data = nullptr, .callback = RemoveWrap},
};
static JSVM\_CallbackStruct \*method = param;
// Aliases for the WrapObject and RemoveWrap methods, which can be called from JS.
static JSVM\_PropertyDescriptor descriptor\[\] = {
    {"wrapObject", nullptr, method++, nullptr, nullptr, nullptr, JSVM\_DEFAULT},
    {"removeWrap", nullptr, method++, nullptr, nullptr, nullptr, JSVM\_DEFAULT},
};

JS example:

const char \*srcCallNative = R"JS(
    class Obj {};
    wrapObject(new Obj());
    removeWrap(new Obj());
)JS";

**Execution result**

The following information is displayed in the log:

JSVM wrap

JSVM name: lilei

JSVM age: 18

JSVM removeWrap

JSVM OH\_JSVM\_RemoveWrap success

JSVM deref\_item

## OH\_JSVM\_DefineClassWithOptions

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a2/v3/cew0Oj1hSWWCgkpIf67fxA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062133Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=FE7230D69ECF44031BDD91415E9F5FEF0C56A1445CB336E329C744288D532250)

The parent class passed in must be created by using an **OH\_JSVM\_DefineClass** API. Otherwise, the **JSVM\_INVALID\_ARG** error will be returned.

**DefineClassOptions** supports the following options:

-   **JSVM\_DEFINE\_CLASS\_NORMAL**: defines a class in normal mode. The default status is **JSVM\_DEFINE\_CLASS\_NORMAL**.
-   **JSVM\_DEFINE\_CLASS\_WITH\_COUNT**: reserves **internal-field** slot for the created class.
-   **JSVM\_DEFINE\_CLASS\_WITH\_PROPERTY\_HANDLER**: sets a listener property for the created class and sets a callback to be invoked when it is called as a function.

CPP code:

#include <string>
#include <memory>
static JSVM\_PropertyHandlerConfigurationStruct propertyCfg{
  nullptr, nullptr, nullptr, nullptr, nullptr, nullptr, nullptr, nullptr, nullptr, nullptr
};

static bool g\_call\_as\_function\_flag = false;
static bool g\_set\_named\_property\_flag = false;
static bool g\_call\_as\_constructor\_flag = false;
static bool g\_properties\_flag = false;

static JSVM\_Value SetNamedPropertyCbInfo2(JSVM\_Env env, JSVM\_Value name, JSVM\_Value property, JSVM\_Value thisArg,
    JSVM\_Value data)
{
    g\_set\_named\_property\_flag = true;
    return property;
}

static JSVM\_Value Add(JSVM\_Env env, JSVM\_CallbackInfo info) {
    g\_properties\_flag = true;
    size\_t argc = 2;
    JSVM\_Value args\[2\];
    OH\_JSVM\_GetCbInfo(env, info, &argc, args, NULL, NULL);
    double num1 = 0;
    double num2 = 0;
    OH\_JSVM\_GetValueDouble(env, args\[0\], &num1);
    OH\_JSVM\_GetValueDouble(env, args\[1\], &num2);
    JSVM\_Value sum = nullptr;
    OH\_JSVM\_CreateDouble(env, num1 + num2, &sum);
    return sum;
}

std::string ToString(JSVM\_Env jsvm\_env, JSVM\_Value val)
{
    JSVM\_Value js\_string;
    OH\_JSVM\_CoerceToString(jsvm\_env, val, &js\_string);
    size\_t length = 0;
    OH\_JSVM\_GetValueStringUtf8(jsvm\_env, js\_string, NULL, 0, &length);
    size\_t capacity = length + 1;
    auto buffer = std::make\_unique<char\[\]>(capacity);
    size\_t copy\_length = 0;
    OH\_JSVM\_GetValueStringUtf8(jsvm\_env, js\_string, buffer.get(), capacity, &copy\_length);
    std::string str(buffer.get());
    return str;
}

JSVM\_Value Run(JSVM\_Env env, const char \*s)
{
    // 1. Convert const char\* to JS\_String.
    JSVM\_Value str;
    JSVM\_CALL(OH\_JSVM\_CreateStringUtf8(env, s, JSVM\_AUTO\_LENGTH, &str));
    // 2. Convert JS\_String to JS\_Script.
    JSVM\_Script script;
    OH\_JSVM\_CompileScript(env, str, nullptr, JSVM\_AUTO\_LENGTH,   false, nullptr, &script);
    // 3. Execute JS\_Script.
    JSVM\_Value result = nullptr;
    OH\_JSVM\_RunScript(env, script, &result);
    return result;
}

static JSVM\_Value TestDefineClassWithOptions(JSVM\_Env env, JSVM\_CallbackInfo info)
{
    g\_call\_as\_function\_flag = false;
    g\_set\_named\_property\_flag = false;
    g\_call\_as\_constructor\_flag = false;
    g\_properties\_flag = false;
    // 1. Define parent-class.
    JSVM\_Value parentClass = nullptr;
    JSVM\_CallbackStruct parentClassConstructor;
    parentClassConstructor.data = nullptr;
    parentClassConstructor.callback = \[\](JSVM\_Env env, JSVM\_CallbackInfo info) -> JSVM\_Value {
        JSVM\_Value thisVar = nullptr;
        OH\_JSVM\_GetCbInfo(env, info, nullptr, nullptr, &thisVar, nullptr);
        return thisVar;
    };
    JSVM\_Value fooVal;
    OH\_JSVM\_CreateStringUtf8(env, "bar", JSVM\_AUTO\_LENGTH, &fooVal);
    JSVM\_PropertyDescriptor des\[2\];
    des\[0\] = {
        .utf8name = "foo",
        .value = fooVal,
    };
    JSVM\_CallbackStruct parentProperties\[\] = {
        {.callback = Add, .data = nullptr},
    };
    des\[1\] = {
        .utf8name = "add",
        .method = &parentProperties\[0\],
    };
    JSVM\_DefineClassOptions options\[1\];
    options\[0\].id = JSVM\_DEFINE\_CLASS\_WITH\_COUNT;
    options\[0\].content.num = 3;
    JSVM\_CALL(OH\_JSVM\_DefineClassWithOptions(env, "parentClass", JSVM\_AUTO\_LENGTH, &parentClassConstructor, 2, des,
        nullptr, 1, options, &parentClass));
  
    // 2. Define sub-class.
    JSVM\_Value subClass = nullptr;
    JSVM\_CallbackStruct subClassConstructor;
    subClassConstructor.data = nullptr;
    subClassConstructor.callback = \[\](JSVM\_Env env, JSVM\_CallbackInfo info) -> JSVM\_Value {
        JSVM\_Value thisVar = nullptr;
        g\_call\_as\_constructor\_flag = true;
        OH\_JSVM\_GetCbInfo(env, info, nullptr, nullptr, &thisVar, nullptr);
        return thisVar;
    };
    JSVM\_DefineClassOptions subOptions\[2\];
    JSVM\_CallbackStruct callAsFuncParam;
    callAsFuncParam.data = nullptr;
    callAsFuncParam.callback = \[\](JSVM\_Env env, JSVM\_CallbackInfo info) -> JSVM\_Value {
        JSVM\_Value thisVar = nullptr;
        g\_call\_as\_function\_flag = true;
        OH\_JSVM\_GetCbInfo(env, info, nullptr, nullptr, &thisVar, nullptr);
        return thisVar;
    };
    propertyCfg.genericNamedPropertySetterCallback = SetNamedPropertyCbInfo2;
    JSVM\_PropertyHandler propertyHandler = {
        .propertyHandlerCfg = &propertyCfg,
        .callAsFunctionCallback = &callAsFuncParam,
    };
    subOptions\[0\].id = JSVM\_DEFINE\_CLASS\_WITH\_COUNT;
    subOptions\[0\].content.num = 4;
    subOptions\[1\].id = JSVM\_DEFINE\_CLASS\_WITH\_PROPERTY\_HANDLER;
    subOptions\[1\].content.ptr = &propertyHandler;
    JSVM\_CALL(OH\_JSVM\_DefineClassWithOptions(env, "subClass", JSVM\_AUTO\_LENGTH, &subClassConstructor, 0, nullptr,
        parentClass, 2, subOptions, &subClass));
    // 3. Verify the validity of 'constructor'.
    JSVM\_Value subInstance;
    JSVM\_CALL(OH\_JSVM\_NewInstance(env, subClass, 0, nullptr, &subInstance));

    JSVM\_Value globalVal;
    OH\_JSVM\_GetGlobal(env, &globalVal);
    OH\_JSVM\_SetNamedProperty(env, globalVal, "obj", subInstance);

    // 4. Verify the validity of 'parentClass'.
    JSVM\_Value subRes = nullptr;
    JSVM\_CALL(OH\_JSVM\_GetNamedProperty(env, subInstance, "foo", &subRes));
    if (ToString(env, subRes).compare("bar") != 0) {
        OH\_LOG\_ERROR(LOG\_APP, "Run OH\_JSVM\_DefineClassWithOptions: Failed");
    }
    // 5. Verify the validity of 'properties'.
    Run(env, "obj.add(3, 4);");
    // 6. Verify the validity of 'options'.
    Run(env, "obj()");
    Run(env, "obj.x = 123;");
    if (g\_call\_as\_function\_flag &&
    g\_set\_named\_property\_flag &&
    g\_call\_as\_constructor\_flag &&
    g\_properties\_flag) {
        OH\_LOG\_INFO(LOG\_APP, "Run OH\_JSVM\_DefineClassWithOptions: Success");
    } else {
        OH\_LOG\_ERROR(LOG\_APP, "Run OH\_JSVM\_DefineClassWithOptions: Failed");
    }
    JSVM\_Value checked;
    OH\_JSVM\_GetBoolean(env, true, &checked);
    return checked;
}

static JSVM\_CallbackStruct param\[\] = {
    {.data = nullptr, .callback = TestDefineClassWithOptions},
};
static JSVM\_CallbackStruct \*method = param;

static JSVM\_PropertyDescriptor descriptor\[\] = {
    {"testDefineClassWithOptions", nullptr, method++, nullptr, nullptr, nullptr, JSVM\_DEFAULT},
};

JS example:

const char \*srcCallNative = R"JS(testDefineClassWithOptions();)JS";

**Execution result**

The following information is displayed in the log:

Run OH\_JSVM\_DefineClassWithOptions: Success
