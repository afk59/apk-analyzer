# API Call Error Codes

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/42/v3/HZ6YFIC0QY-z4zZ3bQY6dA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062311Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=2623D6404AA2E4677BEE4BDCB895B94CB090028722ADB5FEDB8C81EAC3A31225)

This topic describes only module-specific error codes. For details about universal error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

#### 100001 Internal Error

**Error Message**

When used for [@ohos.animator](../../../arkts-api/ui/ohos-animator-animator/document.md): "The specified page is not found or the object property list is not obtained."

When used for [@ohos.promptAction](../../../arkts-api/ui/ohos-promptaction-prompt/document.md) or [UIContext](../../../arkts-api/ui/ohos-arkui-uicontext-uicontext/class-uicontext/document.md): "Internal error."

When used for [@ohos.router](../../../arkts-api/ui/ohos-router-page-routing-not-recommended/document.md): "Internal error. UI execution context is not found."

When used for the [Navigation](../../../arkts-components/navigation-and-switching/navigation/document.md) routing framework: "Internal error. Create NavDestination failed, probably caused by wrong UIContext."

When used for [@ohos.arkui.componentSnapshot](../../../arkts-api/ui/ohos-arkui-componentsnapshot-component-snapshot/document.md): "The builder is not a valid build function."

When used for [@ohos.arkui.componentUtils](../../../arkts-api/ui/ohos-arkui-componentutils-componentutils/document.md): "UI execution context not found."

**Symptom**

For [@ohos.animator](../../../arkts-api/ui/ohos-animator-animator/document.md) and [@ohos.promptAction](../../../arkts-api/ui/ohos-promptaction-prompt/document.md), this error code is reported when an internal error that cannot be rectified by developers occurs, with specific details included in the error message.

For [@ohos.router](../../../arkts-api/ui/ohos-router-page-routing-not-recommended/document.md), this error code is represented as a string type.

For the [Navigation](../../../arkts-components/navigation-and-switching/navigation/document.md) routing framework, this error code is represented as a number type.

For [@ohos.arkui.componentSnapshot](../../../arkts-api/ui/ohos-arkui-componentsnapshot-component-snapshot/document.md), this error code is triggered when the internal state is abnormal.

For [UIContext](../../../arkts-api/ui/ohos-arkui-uicontext-uicontext/class-uicontext/document.md), this error code is reported when an internal error that cannot be rectified by developers occurs.

**Possible Cause**

For [@ohos.animator](../../../arkts-api/ui/ohos-animator-animator/document.md), [@ohos.router](../../../arkts-api/ui/ohos-router-page-routing-not-recommended/document.md), or [Navigation](../../../arkts-components/navigation-and-switching/navigation/document.md) routing framework: failure to obtain the rendering engine or parse parameters.

For [@ohos.promptAction](../../../arkts-api/ui/ohos-promptaction-prompt/document.md): failure to obtain the rendering engine or parse parameters, or unclear UI context.

For [@ohos.arkui.componentSnapshot](../../../arkts-api/ui/ohos-arkui-componentsnapshot-component-snapshot/document.md): failure to obtain a valid UI instance, null pointer exception, failed internal state validation of the UI instance, inability to query the node (because the component is not added to the tree), or snapshot size exceeding hardware limits (which may vary by hardware platform).

For [UIContext](../../../arkts-api/ui/ohos-arkui-uicontext-uicontext/class-uicontext/document.md): insufficient memory or JS VM exceptions leading to failed UI instance creation.

**Solution**

For issues related to the issue of [ambiguous UI context](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/arkts-global-interface#ambiguous-ui-context), use the APIs provided in **UIContext**. For details, see [Using the UI Context API for UI Operations (UIContext)](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/arkts-global-interface).
