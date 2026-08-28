# Setting the private Property Using JSVM-API

#### Introduction

This topic walks you through on how to use JSVM-API to set a private property.

#### Basic Concepts

JSVM-API provides the capability of creating private keys, creating and deleting properties on objects using the keys, and persistently saving private key symbols.

#### Available APIs

| API | Description |
| :-- | :-- |
| OH\_JSVM\_CreateDataReference | Creates a data reference with a specified reference count in JSVM. |
| OH\_JSVM\_GetReferenceData | Checks whether a specified reference is valid. If the reference is valid, the JavaScript data associated with the reference is returned; otherwise, **result** is set to **NULL**. |
| OH\_JSVM\_CreatePrivate | Creates a JS private key object. |
| OH\_JSVM\_SetPrivate | Sets a private property for a passed-in object. |
| OH\_JSVM\_GetPrivate | Obtains the private property of an object based on the private key. |
| OH\_JSVM\_DeletePrivate | Deletes the private property of an object based on the private key. |

#### Example

If you are just starting out with JSVM-API, see [JSVM-API Development Process](../../jsvm-api-development-process/document.md). The following demonstrates only the C++ code involved in manipulating private properties.

## Creating a private Key, adding a private Property, and Deleting the Property

CPP code:

static JSVM\_Value privateTest(JSVM\_Env env, JSVM\_CallbackInfo info) {
    JSVM\_VM vm;
    JSVM\_HandleScope outerScope;
    OH\_JSVM\_GetVM(env, &vm);
    OH\_JSVM\_OpenHandleScope(env, &outerScope);

    JSVM\_HandleScope handleScope;
    JSVM\_Data privateKey;
    JSVM\_Value object;
    JSVM\_Value property;
    JSVM\_Ref privateRef;
    {
        OH\_JSVM\_OpenHandleScope(env, &handleScope);
        OH\_JSVM\_CreateObject(env, &object);
        OH\_JSVM\_CreatePrivate(env, nullptr, &privateKey);
        OH\_JSVM\_CreateInt32(env, 1, &property);
        OH\_JSVM\_SetPrivate(env, object, privateKey, property);
        OH\_JSVM\_GetPrivate(env, object, privateKey, &property);
        int propertyValue = 0;
        OH\_JSVM\_GetValueInt32(env, property, &propertyValue);
        OH\_LOG\_INFO(LOG\_APP, "private property set: %{public}d\\n", propertyValue);
        OH\_JSVM\_DeletePrivate(env, object, privateKey);
        OH\_JSVM\_GetPrivate(env, object, privateKey, &property);
        bool isUndefined = false;
        OH\_JSVM\_IsUndefined(env, property, &isUndefined);
        OH\_LOG\_INFO(LOG\_APP, "private property deleted is undefined: %{public}d\\n", isUndefined);
        OH\_JSVM\_CreateDataReference(env, privateKey, 1, &privateRef);
        OH\_JSVM\_CloseHandleScope(env, handleScope);
    }
    {
        OH\_JSVM\_OpenHandleScope(env, &handleScope);
        OH\_JSVM\_GetReferenceData(env, privateRef, &privateKey);
        OH\_JSVM\_CreateObject(env, &object);
        OH\_JSVM\_CreateInt32(env, 2, &property);
        OH\_JSVM\_SetPrivate(env, object, privateKey, property);
        OH\_JSVM\_GetPrivate(env, object, privateKey, &property);
        int propertyValue = 0;
        OH\_JSVM\_GetValueInt32(env, property, &propertyValue);
        OH\_LOG\_INFO(LOG\_APP, "second private property set: %{public}d\\n", propertyValue);
        OH\_JSVM\_CloseHandleScope(env, handleScope);
    }

    OH\_JSVM\_CloseHandleScope(env, outerScope);
    return nullptr;
}

static JSVM\_CallbackStruct param\[\] = {
    {.data = nullptr, .callback = privateTest},
};

static JSVM\_CallbackStruct \*method = param;

// Alias for the wrapperObject method to be called from JS.
static JSVM\_PropertyDescriptor descriptor\[\] = {
    {"privateTest", nullptr, method++, nullptr, nullptr, nullptr, JSVM\_DEFAULT},
};

// Call the C++ code from JS.
const char \*srcCallNative = R"JS(privateTest();)JS";

#### Expected Result

private property set: 1
private property deleted is undefined: 1
second private property set: 2
