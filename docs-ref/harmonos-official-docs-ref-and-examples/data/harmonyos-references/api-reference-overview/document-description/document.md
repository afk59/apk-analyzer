# Document Description

API references provide the description of APIs used for application development. This topic describes common fields in the API references to help you better use the reference document.

#### Version Description

In API references, the earliest versions of APIs and components are specified in the following ways:

-   For a new API or component, the version information is provided at the beginning of the reference document. Example: "The initial APIs of this module are supported since API version 7."
-   For a new feature of an existing API or component, a superscript is added following the feature. For example, "uid8+" indicates that the **uid** attribute is supported since API version 8.

#### System Capability Description

System capability refers to a relatively independent feature in the operating system. Different devices provide different system capabilities, and multiple APIs implement a system capability. You can determine whether an API can be used based on system capabilities. For details, see [SystemCapability](../systemcapability/document.md).

The following description is provided for each API in the reference document to describe the system capability of the API: "**System capability**: SystemCapability.xxx.xxx"

-   You can call the **canIUse** API to [check whether an API is available](../systemcapability/document.md#checking-whether-an-api-is-available).
-   The performance of a SysCap may vary by device type. You can [check the differences between devices with a specific SysCap](../systemcapability/document.md#checking-the-differences-between-devices-with-a-specific-syscap).
-   For a specific device model, the capabilities may exceed the capability set defined for the default device. To use these capabilities, you need to configure a custom SysCap. For details, see [Adding Custom SysCap](../systemcapability/document.md#adding-custom-syscap).

#### API Usage Description

The open capabilities (APIs) provided by the HarmonyOS SDK can be used only after the declaration is imported. The SDK encapsulates API modules within each kit, allowing you to access these APIs by importing the respective kit in their code. Detailed definitions of the API modules encapsulated in each kit can be found in the kit subdirectory within the SDK directory.

For details about how to import the kit, see [Importing Open Capabilities of the HarmonyOS SDK](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/introduction-to-arkts#import).

#### Atomic Service Capabilities

[Atomic services](https://developer.huawei.com/consumer/en/doc/atomic-guides/atomic-service) take a lightweight application form and feature instant access, cross-device hopping, and more.

Atomic services can be independently released, distributed, and executed to implement service closure, greatly improving the efficiency of obtaining information and services.

Atomic services are developed based on the HarmonyOS SDK (only the Atomic Service API Set can be used) and can run on HarmonyOS devices in proper scenarios.

-   For APIs that can be used in atomic services, the following description will be added: "Atomic service API: This API can be used in atomic services since API version x."
-   For APIs that cannot be used in atomic services, no special description is provided.

#### Service Widget Description

A [service widget](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/formkit-overview) (also called widget) is a set of UI components that display important information or operations specific to an application or atomic service. It provides users with direct access to a desired service, without the need to open the application first.

-   For APIs that can be used in ArkTS widgets, a description about the widget capability will be added. Example: "Widget capability: This API can be used on the ArkTS widget UI since API version 12."
-   For APIs that cannot be used on the ArkTS widget UI, no special description is provided.

#### Permission Description

By default, applications can access limited system resources. However, in some cases, an application needs to access excess data (including personal data) and functions of the system or another application to implement extended functions. For details, see [Application Permission Management Overview](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/app-permission-mgmt-overview).

To call APIs to access these resources, you must apply for the corresponding permissions by following the instructions provided in [Workflow for Requesting Permissions](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/determine-application-mode).

-   If an application can call an API only after it has obtained a specific permission, the following description is provided for the API: "**Required permissions**: ohos.permission.xxxx"
-   If an application can call an API without any permission, no special description is provided.

#### Error Code Description

You may encounter errors when using ArkTS APIs.

For each API where errors might occur, you can refer to the error code section in the documentation to understand the possible error code IDs and messages for that API and handle them as needed.

ArkTS API includes both asynchronous and synchronous APIs, with the following error handling methods:

-   For synchronous APIs, errors are uniformly thrown as exceptions, and you need to handle potential exceptions using try-catch.
    
-   For asynchronous APIs, errors may include exceptions and rejections. If you use the await/async approach, you need to handle potential exceptions and rejections using try-catch.
    
-   For asynchronous APIs using the Promise approach, errors may include exceptions and rejections. You need to handle synchronous exceptions (usually 401 exceptions) using try-catch and handle rejections using the Promise's **catch()** method or the **onrejected** callback function in the **then()** method.
    
-   For asynchronous APIs using the callback approach (not recommended), errors may include exceptions and errors returned by the callback. If you use the callback approach, you need to handle synchronous exceptions (usually 401 exceptions) using try-catch and handle errors presented through callback parameters (for example, BusinessError objects).
    

#### Application Model Description

Along its evolution, the system has provided two application models: FA model and stage model.

-   If all the APIs of a module support only one model, the following description is provided at the beginning of the reference document: "The APIs of this module can be used only in the FA model." or "The APIs of this module can be used only in the stage model."
-   If certain APIs of a module support only one model, the following description is provided individually for these APIs: "This API can be used only in the FA model." or "This API can be used only in the stage model."
-   If both models are supported, no special description is provided.

#### Deprecated API Description

A deprecated API is an API no longer recommended and is marked with the deprecated superscript.

While deprecated APIs can still be implemented in the five API levels immediately following the version when the API is deprecated, this is not recommended.

-   Do not use deprecated APIs in new code. If possible, rewrite old code by replacing the deprecated APIs with their substitutes.
-   If no substitute is available, change the implementation mode by referring to the deprecation description and changelog.
