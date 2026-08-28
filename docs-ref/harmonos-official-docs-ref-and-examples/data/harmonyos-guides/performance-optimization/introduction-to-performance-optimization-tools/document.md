# Introduction to Performance Optimization Tools

An app/atomic service is considered to have poor performance if it encounters the following symptoms when running: slow response, choppy animations, app crash, high power consumption, and device overheating. The poor performance may be caused by misuse of system APIs or memory leak due to improper holding of ArkTS objects. All these result in improper use of system resources, including the CPU, memory, network, file, GPU, and peripherals.

Performance profiling is often conducted to reduce the load, either permanently or temporarily.

-   Permanent load reduction completely clears unnecessary work.
-   Temporary load reduction prevents overcrowding in critical time periods. Lazy loading, for example, can be used to delay processing to off-peak hours.

When encountering performance problems, monitor the app running status and device resource usage to preliminarily identify and locate the problem, and then reduce the load accordingly.

[CodeLinter](../../coding-and-debugging/writing-code/code-check/running-code-linter/document.md) provides the static code scanning capability, which checks code against [rules](../../coding-and-debugging/writing-code/code-check/code-linter-check-rules/performance-performance-rules/document.md) to detect potential performance issues, helping you analyze and modify problematic code.

[DevEco Profiler](../introduction-to-deveco-profiler/document.md) provides Realtime Monitor to comprehensively monitor device resources, covering system events, exception reports, CPU usage, memory usage, real-time frame rate, GPU usage, energy consumption, and network traffic consumption. It facilitates top-down, layered analysis and allows you to jump directly to the corresponding code. You can perform white-box analysis based on the code to pinpoint unnecessary workloads, identify performance bottlenecks, and demarcate the problem.

This chapter focuses on the DevEco Profiler. For details on CodeLinter and AppAnalyzer, refer to their respective documentation.
