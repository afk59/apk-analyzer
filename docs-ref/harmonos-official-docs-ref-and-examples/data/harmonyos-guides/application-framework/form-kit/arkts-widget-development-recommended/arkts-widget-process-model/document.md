# ArkTS Widget Process Model

This section describes the processes of a widget from creation to display. For details, see the figure below.

**Figure 1** Widget process model

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/92/v3/pSoJ8B_FQfK0ePbq5-f-qA/en-us_image_0000002537924994.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061952Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=2AF115740EAD4B4671C9DC743FB5C7800479478F2629B052FECE081E3DE5B2E6)

-   Widget host process: a host process that displays the widget UI, for example, the home screen process.
-   Widget rendering process: a process that loads and renders widget UIs in the system. All widgets are rendered in the same process, and different widget UIs are isolated by VMs.
-   Widget Manager process: a System Service ([SA](../../../ability-kit/fa-model-development/fa-model-application-components/serviceability-component-development/serviceability-overview/document.md)) for unifying the widget lifecycle.
-   Widget provider process: an application process that provides widgets, including the main process running the UIAbility of the application and the independent [FormExtensionAbility](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-app-form-formextensionability) process of the widget. The memory of the two processes is isolated, but they share the same file sandbox.
