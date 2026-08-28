# About This Kit

Performance Analysis Kit provides the event, log, and tracing analysis tools to help you check the running status of your application for further behavior, fault, security, and statistical analysis.

Performance Analysis Kit provides a collection of capabilities for improving application quality.

#### When to Use

-   Application debugging: provides the HiLog functionality to help you record and obtain log information for fault analysis.
    
-   Fault locating: provides log, event, and tracing information related to reliability, performance, power consumption, and distributed faults.
    
-   Online monitoring: provides log, event, and tracing APIs to help you record and analyze the running status of your application.
    

#### Available Capabilities

-   [Fault detection](../fault-detection/overview/document.md): provides the capability of detecting application stability faults, including the crash, address sanitizer, application freeze, resource leak, and task timeout events.
    
-   [Power consumption detection](../power-consumption-detection/document.md): provides the capability of detecting abnormal application power consumption, such as high CPU load.
    
-   [Performance detection](../performance-detection/document.md): provides the capability of detecting application performance exceptions, such as time-consuming application launches and scrolling frame loss.
    
-   [HiLog](../log-printing/using-hilog-arkts/document.md): provides the capability of recording and obtaining logs.
    
-   [HiAppEvent](../event-subscription/introduction-to-hiappevent/document.md): provides the capability of recording fault, behavior, security, and statistical events, subscribing to system events, and setting data processors for data upload.
    
-   [HiTraceMeter](../performance-tracing/introduction-to-hitracemeter/document.md) and [HiTraceChain](../distributed-call-chain-tracing/introduction-to-hitracechain/document.md): provide the capabilities of performance tracing and cross-thread and cross-process distributed tracing.
    
-   [HiChecker](../check-mode/using-hichecker-arkts/document.md): provides the capability of detecting time-consuming application thread calls and ability resource leaks.
    
-   [HiDebug](../obtaining-system-debugging-information/introduction-to-hidebug/document.md): provides the capability of obtaining application and system resource usage.
    
-   [HiCollie](../service-thread-timeout-detection/using-hicollie-to-detect-service-thread-stuck-and-jank-events-c-c/document.md): provides the capability of detecting service thread task execution timeout and reporting timeout events.
    
-   [ErrorManager](../error-manager-and-application-recovery/development-of-error-manager/document.md) and [AppRecovery](../error-manager-and-application-recovery/development-of-application-recovery/document.md): provide the capability of capturing application runtime exceptions and restoring the startup status and data after an application exits unexpectedly.
    
-   Command line tools for debugging the system and applications: [hdc](../command-line-tools/hdc/document.md), [HiLog](../command-line-tools/hilog/document.md), [HiDumper](../command-line-tools/hidumper/hidumper/document.md), [HiTrace](../command-line-tools/hitrace/document.md) and [HiPerf](../command-line-tools/hiperf/document.md) .
    

#### Features

**Hassle-free APM System Setup**

-   Provides [HiDebug](../obtaining-system-debugging-information/introduction-to-hidebug/document.md), [HiAppEvent](../event-subscription/introduction-to-hiappevent/document.md) and [HiLog](../log-printing/using-hilog-arkts/document.md) APIs to build an Application Performance Management (APM) SDK on the device for interconnection with the APM developed by vendors.
    
-   Provides [HiAppEvent system events](../event-subscription/using-hiappevent-to-subscribe-to-events/event-subscription-overview/document.md#system-events) and [application events](../event-subscription/using-hiappevent-to-subscribe-to-events/event-subscription-overview/document.md#application-events) for subscribing to events (such as crash and application freeze events) triggered during application running, and quickly records and collects event information required for O&M.
    

**Powerful Exception Detection and Handling Mechanism**

-   Provides a comprehensive application quality detection mechanism, including [fault detection](../fault-detection/overview/document.md), [performance detection](../performance-detection/document.md) and [power consumption detection](../power-consumption-detection/document.md).
    
-   Provides simplified, standard, and complete exception logs to accurately record exception propagation paths.
    
-   Provides a comprehensive exception detection mechanism to detect exceptions in real time, notify the application of exceptions, and automatically restart the application.
    

**Comprehensive Basic Maintenance and Debugging Capabilities**

-   Classifies logs by level and category and supports multiple languages, privacy processing, and traffic control.
    
-   Provides a complete event framework and mechanisms for event logging, recording, and reporting.
    
-   Traces process tracks for performance analysis.
