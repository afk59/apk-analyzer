# UI Stability Issue Analysis Overview

This topic explains the concepts and classification of stability issues, and provides guidance for locating stability issues using system debugging capabilities and tools.

Application stability issues include application crashes, application freezes, and application resource leaks. Performance issues are not classified as stability issues. For details about performance issues, see [High-Performance UI Development](../../high-performance-ui-development/document.md).

#### Application Crash

Application crashes, also referred to as unexpected application exits, occur when an application terminates unexpectedly during runtime. They are typically caused by the following factors:

-   Unhandled JavaScript exceptions, such as **TypeError** and **ReferenceError**.
-   Unhandled native exceptions, such as **SIGSEGV** and **SIGABRT**.
-   System resource limitations, such as insufficient memory and exhausted file handles or thread handles.
-   Application UI freezes.

This document focuses on the first two categories: JavaScript crashes and C++ crashes. Other types are covered under application resource leaks and freezes.

## JavaScript Crash (jscrash)

When a JavaScript crash occurs, the FaultLogger module collects fault information. For details about how to obtain logs, see [Obtaining Logs](../../../../../system/debugging-tools/performance-analysis-kit/fault-detection/crash-detection/js-crash-process-crash-detection/document.md#obtaining-logs).

Reference materials:

-   [JS Crash (Process Crash) Detection](../../../../../system/debugging-tools/performance-analysis-kit/fault-detection/crash-detection/js-crash-process-crash-detection/document.md)

## C++ Crashes (cppcrash)

When a C++ crash occurs, the FaultLogger module collects fault information. For details about how to obtain logs, see [Obtaining Logs](../../../../../system/debugging-tools/performance-analysis-kit/fault-detection/crash-detection/c-crash-process-crash-detection/document.md#obtaining-logs).

Reference materials:

-   [C++ Crash (Process Crash) Detection](../../../../../system/debugging-tools/performance-analysis-kit/fault-detection/crash-detection/c-crash-process-crash-detection/document.md)
-   [Address Sanitizer Detection](../../../../../system/debugging-tools/performance-analysis-kit/fault-detection/address-sanitizer-detection/document.md)

#### Application Freeze

Application freezes, also known as application unresponsiveness, occur when an application becomes unresponsive to user interactions. The following materials provide guidance for analyzing application freeze issues:

-   [Application Freeze Detection](../../../../../system/debugging-tools/performance-analysis-kit/fault-detection/application-freeze-detection/document.md)
-   [Task Timeout Detection](../../../../../system/debugging-tools/performance-analysis-kit/fault-detection/task-timeout-detection/document.md)

#### Application Resource Leak

The following materials provide guidance for analyzing application resource leak issues:

-   [Resource Leak Event Overview](../../../../../system/debugging-tools/performance-analysis-kit/event-subscription/using-hiappevent-to-subscribe-to-events/system-events/resource-leak-events/resource-leak-event-overview/document.md)
-   [Subscribing to Resource Leak Events (ArkTS)](../../../../../system/debugging-tools/performance-analysis-kit/event-subscription/using-hiappevent-to-subscribe-to-events/system-events/resource-leak-events/subscribing-to-resource-leak-events-arkts/document.md)
-   [Subscribing to Resource Leak Events (C/C++)](../../../../../system/debugging-tools/performance-analysis-kit/event-subscription/using-hiappevent-to-subscribe-to-events/system-events/resource-leak-events/subscribing-to-resource-leak-events-c-c/document.md)
