# HiAppEvent

#### Overview

Provides APIs for implementing the application event logging functionality. This functionality allows your application to record fault events, statistics events, security events, and user behavior events reported during system running. Based on the event information, you can analyze the operating status of your application.

**Since**: 8

#### Files

| Name | Description |
| :-- | :-- |
| [hiappevent.h](../../header-files/hiappevent-h/document.md) | Defines the application event logging functions of the HiAppEvent module. Before performing application event logging, you must construct a parameter list object to store the input event parameters and specify the event domain, event name, and event type.
Event domain: domain associated with the application event.

Event name: name of the application event.

Event type: fault, statistics, security, or behavior.

Parameter list: a linked list used to store event parameters. Each parameter consists of a parameter name and a parameter value.

 |
| [hiappevent\_cfg.h](../../header-files/hiappevent-cfg-h/document.md) | Defines the configuration items of the event logging configuration function. To configure the application event logging functionality, you can directly use configuration item constants. |
| [hiappevent\_event.h](../../header-files/hiappevent-event-h/document.md) | Defines the names of all predefined events. In addition to custom events associated with specific applications, you can use predefined events for logging. |
| [hiappevent\_param.h](../../header-files/hiappevent-param-h/document.md) | Defines the names of all predefined event parameters. In addition to custom events associated with specific applications, you can use predefined events for logging. |
