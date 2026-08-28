# FAQs About UI Parallelization

#### How to Obtain and Use Multi-thread NDK APIs

From API version 22, **ARKUI\_MULTI\_THREAD\_NATIVE\_NODE** is added to [ArkUI\_NativeAPIVariantKind](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-native-interface-h#arkui_nativeapivariantkind).

Call the [OH\_ArkUI\_GetModuleInterface](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-native-interface-h#oh_arkui_getmoduleinterface) API and pass **ARKUI\_MULTI\_THREAD\_NATIVE\_NODE** as the input parameter to obtain the multi-threaded NDK API set. Refer to [Using Multi-threaded NDK APIs](../../../using-ndk-apis-to-build-uis/parallelizing-ui-page-building-using-multi-threaded-ndk-apis/document.md#using-multi-threaded-ndk-apis) for the complete example.

#### Calling a multi-threaded NDK API returns the **ARKUI\_ERROR\_CODE\_NODE\_ON\_INVALID\_THREAD** error code.

**Symptom**

Calling a multi-threaded NDK API returns the **ARKUI\_ERROR\_CODE\_NODE\_ON\_INVALID\_THREAD** error code.

**Solution**

Refer to [Multi-threaded NDK API Set Specifications](../../../using-ndk-apis-to-build-uis/parallelizing-ui-page-building-using-multi-threaded-ndk-apis/document.md#multi-threaded-ndk-api-set-specifications) to check whether the called API supports multi-thread calling, and then perform the following steps:

1.  If the API can be called only on the UI thread, adjust the function call timing and call the API on the UI thread.
2.  If the API supports multi-thread calling, the error occurs because the node operated by the API is in the Attached state.
    -   Check whether the node is created by the multi-threaded [createNode](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-arkui-nativemodule-arkui-nativenodeapi-1#createnode) API.
    -   Remove all non-convertible attached components from the component tree where the component is located by referring to [Multi-threaded NDK API Set Specifications](../../../using-ndk-apis-to-build-uis/parallelizing-ui-page-building-using-multi-threaded-ndk-apis/document.md#multi-threaded-ndk-api-set-specifications).

#### How to Ensure Thread Safety When Operating ArkUI Components in Multiple Threads

When multi-threaded NDK APIs are used, multiple threads operate the same component or component tree at the same time. In this case, thread safety cannot be ensured. You need to avoid this situation through proper architectural design.

You can follow the restrictions in [Multi-threaded NDK API Set Specifications](../../../using-ndk-apis-to-build-uis/parallelizing-ui-page-building-using-multi-threaded-ndk-apis/document.md#multi-threaded-ndk-api-set-specifications) to ensure thread safety.
