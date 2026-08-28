# About This Kit

Test Kit provides automated test frameworks that support unit, UI, and performance tests. It enables you to write and execute automated test scripts in ArkTS and assess the effectiveness of your features based on test results. Since API version 20, the performance test capability is supported.

-   Unit test capability: provides basic APIs and running mechanisms for automated tests. For details, see [JsUnit User Guide](../automated-test-framework-user-guides/jsunit-user-guide/document.md). The main features are as follows:
    -   APIs for defining automated test suites and cases.
    -   Assertion APIs that can be flexibly integrated into your test scripts and support multiple assertion modes to verify that test cases meet expected behavior.
    -   APIs for executing preset and clear actions at both test suite and test case levels.
    -   Multiple test case execution modes, including specified test case execution, random execution, and stress execution.
-   UI test capability: provides automated UI test features. UI test scripts are developed based on JSUnit. For details, see [UITest User Guide](../automated-test-framework-user-guides/uitest-user-guide/document.md). The main features are as follows:
    -   APIs for searching for components in multiple modes, for example, by component attribute or relative position.
    -   APIs for simulating UI operations, such as tapping, double-tapping, swiping, and the two-finger pinch gesture, as well as operations on external devices such as the mouse and keyboard.
    -   APIs for simulating window operations, such as resizing and moving the window.
    -   Shell commands for simulating UI operations, such as tapping, double-tapping, and swiping.
    -   Capabilities of listening for system dialog boxes and toasts, and obtaining prompt messages.
-   Performance test capability: provides automated white-box performance test features. Performance test scripts are developed based on JSUnit. For details, see [PerfTest User Guide](../automated-test-framework-user-guides/perftest-user-guide/document.md). The main features are as follows:
    -   Basic performance data collection during the execution of a specified code segment, including the execution duration, CPU usage, and memory usage.
    -   Application scenario-based performance data collection, including the application launch latency, page switching latency, and list scrolling frame rate.
