# Introduction to HiAppEvent

#### Overview

HiAppEvent is an event subscription and logging mechanism provided for recording faults, statistics, security events, and behavior events during application running. It helps you locate faults, analyze application running status, and collect statistics on access traffic, user activity, operation habits, and other key factors that affect user experience.

#### Basic Concepts

**Logging**: a function that logs changes caused by user operations to provide service data for development, product, and O&M analysis.

-   Event domain: identifies the domain of an event. You are advised to set this parameter to the service domain name to differentiate service domains.
    
-   Event name: specifies the name of an event. You are advised to set this parameter to a specific service name to differentiate services.
    
-   Event type: specifies the type of an event. Four event types are supported:
    
    -   Behavior event: used to record the daily operation behavior of a user, for example, button click and page redirection.
    -   Fault event: used to locate and analyze application faults, for example, frame freezes and network interruption.
    -   Statistical event: used to collect statistics on key application behaviors, for example, usage duration and number of visits.
    -   Security event: used to record events related to application security, for example, user authorization.
-   Event parameter: specifies the parameters of an event. Each event can contain a group of parameters. You are advised to set this parameter to an event attribute or event context to depict the event details.
    

**Event subscription**: You can use the [addWatcher](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-hiviewdfx-hiappevent#hiappeventaddwatcher) API of HiAppEvent to register a watcher for system events or application events that you concern. In this way, when the subscribed event occurs, you can receive and process the event callback information.

#### Implementation Principles

## System Event Subscription Mechanism

In the current system application sandbox mechanism, an application process can access only its own application sandbox directory. For details, see [Application Sandbox](../../../../../application-framework/core-file-kit/application-files/application-sandbox/document.md). However, the system event information is not stored in the application sandbox directory. As a result, the information cannot be directly obtained.

The application calls the **addWatcher** API of HiAppEvent to subscribe to system events and create a shared directory. When the application process is faulty, the DFX system captures the related information, generates events and logs, and writes them to the shared directory. After detecting an event, HiAppEvent sends the event to the application.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/12/v3/oCPrZGLXSIihrbrOqvW1OQ/en-us_image_0000002537765118.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062027Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=58E8196B97D3D679227926B2AF9F8E40C252420AF389B8860F3129A50E7D006E)

## Application Event Subscription Mechanism

After calling the addWatcher API to subscribe to the application event, the application must call the [write](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-hiviewdfx-hiappevent#hiappeventwrite-1) API to log application events.

HiAppEvent associates application events based on the event domain and event name, and sends the events to the application using the callback set through the **addWatcher** API.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/dd/v3/51Q3IYTEToSFH66eiwI1dA/en-us_image_0000002537925058.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062027Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=DC2ABF1D3E48CFDE807083A56425DB327EF94F73E022C4E277DE61DF8F9EE6C0)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/de/v3/IOFgFjvNRCO6D_VD7RGsnA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062027Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=AB41375360FB486EA8FBF598619F6F35C967819B6532F4A1C4E62949A2DED958)

If an application has subscribed to an event but exits before the callback is triggered, the callback of the event will be executed after the application calls **addWatcher** at the next startup. For example, if an application subscribes to the crash event and exits due to a crash, the event callback is executed after **addWatcher** is called upon the next startup.

#### Constraints

-   The **addWatcher** API is a synchronous API and involves I/O operations. For modules that have high requirements on performance, you are advised to call the API on a non-main thread.
    
-   The name passed to the **addWatcher** API should be unique. If the same name is passed, the previous subscription will be overwritten.
    
-   Currently, HarmonyOS supports common applications, [application clones](../../../../../getting-started/development-fundamentals/typical-scenarios-development/creating-an-application-clone/document.md), atomic services, and [input method applications](../../../../../application-framework/ime-kit/implementing-an-input-method-application/document.md). The subscription specifications of system events vary depending on the application type. Since API version 22, you can use the HiAppEvent system event subscription capability in the input method application. The following table lists the specifications.
    

| System Event Name | Application Clone Subscription | Atomic Service Subscription | Input Method Application Subscription |
| :-- | :-- | :-- | :-- |
| Crash event | Supported | Supported | Supported |
| Application freeze event | Supported | Supported | Supported |
| Resource leak event | Supported | Supported | Supported |
| Address sanitizer event | Supported | Not supported | Supported |
| Main thread jank event | Supported | Supported | Supported |
| Task execution timeout event | Supported | Not supported | Supported |
| Application killed event | Supported | Supported | Supported |
| Time-consuming launch event | Not supported | Supported | Not supported |
| Scrolling frame loss event | Not supported | Supported | Not supported |
| High CPU usage event | Not supported | Not supported | Supported |
| Battery usage statistics event | Not supported | Not supported | Supported |
| Audio jank event | Not supported | Not supported | Not supported |
