# Working with Proxy Using JSVM-API

#### Introduction

This topic walks you through on how to use JSVM-API to create a proxy instance, check whether the given **JSVM\_Value** is of the proxy type, and obtain the target object from the given proxy.

#### Available APIs

| API | Description |
| :-- | :-- |
| OH\_JSVM\_CreateProxy | Creates a proxy. This API is equivalent to calling **new Proxy (target, handler)** in JS. |
| OH\_JSVM\_IsProxy | Checks whether the **JSVM\_Value** is of the proxy type. |
| OH\_JSVM\_ProxyGetTarget | Obtains the target object of the specified proxy. |

#### Example

If you are just starting out with JSVM-API, see [JSVM-API Development Process](../../jsvm-api-development-process/document.md). The following demonstrates only the C++ code involved in proxy-related APIs.

CPP code:

// Define OH\_JSVM\_CreateProxy.
static JSVM\_Value CreateProxy(JSVM\_Env env, JSVM\_CallbackInfo info) {
    // Pass in two parameters: target and handler.
    size\_t argc = 2;
    JSVM\_Value args\[2\] = {nullptr};
    JSVM\_CALL(OH\_JSVM\_GetCbInfo(env, info, &argc, args, nullptr, nullptr));
    // Call OH\_JSVM\_CreateProxy to create a proxy for the target object.
    JSVM\_Value result = nullptr;
    JSVM\_Status status = OH\_JSVM\_CreateProxy(env, args\[0\], args\[1\], &result);
    if (status != JSVM\_OK) {
        OH\_LOG\_ERROR(LOG\_APP, "JSVM OH\_JSVM\_CreateProxy: failed: %{public}d", status);
    } else {
        OH\_LOG\_INFO(LOG\_APP, "JSVM OH\_JSVM\_CreateProxy: success");
    }

    return result;
}

// Define OH\_JSVM\_IsProxy.
static JSVM\_Value IsProxy(JSVM\_Env env, JSVM\_CallbackInfo info) {
    size\_t argc = 1;
    JSVM\_Value args\[1\] = {nullptr};
    JSVM\_CALL(OH\_JSVM\_GetCbInfo(env, info, &argc, args, nullptr, nullptr));
    // Call OH\_JSVM\_IsProxy to check whether JSVM\_Value is a proxy.
    bool result = false;
    JSVM\_Status status = OH\_JSVM\_IsProxy(env, args\[0\], &result);
    if (status != JSVM\_OK) {
        OH\_LOG\_ERROR(LOG\_APP, "JSVM OH\_JSVM\_IsProxy: failed");
    } else {
        OH\_LOG\_INFO(LOG\_APP, "JSVM OH\_JSVM\_IsProxy: success: %{public}s", result ? "is a proxy" : "is not a proxy");
    }
    JSVM\_Value isProxy;
    JSVM\_CALL(OH\_JSVM\_GetBoolean(env, result, &isProxy));
    return isProxy;
}

// Define OH\_JSVM\_ProxyGetTarget.
static JSVM\_Value GetProxyTarget(JSVM\_Env env, JSVM\_CallbackInfo info) {
    size\_t argc = 1;
    JSVM\_Value args\[1\] = {nullptr};
    JSVM\_CALL(OH\_JSVM\_GetCbInfo(env, info, &argc, args, nullptr, nullptr));
    // Call OH\_JSVM\_ProxyGetTarget to obtain the target object in the proxy.
    JSVM\_Value result = nullptr;
    JSVM\_Status status = OH\_JSVM\_ProxyGetTarget(env, args\[0\], &result);
    if (status != JSVM\_OK) {
        OH\_LOG\_ERROR(LOG\_APP, "JSVM OH\_JSVM\_ProxyGetTarget: failed");
    } else {
        OH\_LOG\_INFO(LOG\_APP, "JSVM OH\_JSVM\_ProxyGetTarget: success");
    }

    return result;
}

// Register the proxy-related callbacks.
static JSVM\_CallbackStruct param\[\] = {{.data = nullptr, .callback = CreateProxy},
                                      {.data = nullptr, .callback = IsProxy},
                                      {.data = nullptr, .callback = GetProxyTarget}};
static JSVM\_CallbackStruct \*method = param;
// Aliases for the proxy-related callbacks to be called from JS.
static JSVM\_PropertyDescriptor descriptor\[\] = {
    {"CreateProxy", nullptr, method++, nullptr, nullptr, nullptr, JSVM\_DEFAULT},
    {"IsProxy", nullptr, method++, nullptr, nullptr, nullptr, JSVM\_DEFAULT},
    {"GetProxyTarget", nullptr, method++, nullptr, nullptr, nullptr, JSVM\_DEFAULT}};

const char \*srcCallNative = R"JS(
       target = {
         message1: "hello",
         message2: "everyone",
       };

       handler = {
         get(target, prop, receiver) {
           return "world";
         },
       };

       proxy = CreateProxy(target, handler)
       isProxy = IsProxy(proxy)
       target1 = GetProxyTarget(proxy)
)JS";

Expected result:

JSVM OH\_JSVM\_CreateProxy: success
JSVM OH\_JSVM\_IsProxy: success: is a proxy
JSVM OH\_JSVM\_ProxyGetTarget: success
