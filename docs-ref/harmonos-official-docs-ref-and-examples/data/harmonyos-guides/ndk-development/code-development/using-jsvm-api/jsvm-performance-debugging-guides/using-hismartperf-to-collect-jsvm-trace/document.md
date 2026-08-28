# Using HiSmartPerf to Collect JSVM Trace

#### Overview

JSVM trace is a tool provided by the JSVM engine for analyzing and debugging the execution process of JavaScript code. It records and outputs detailed information about code execution, including function calls, execution time, and memory usage, helping you understand code performance, diagnose potential problems, and optimize code.

Currently, HiSmartPerf supports trace points of the **compile**, **runtime**, **builtin**, and **JS\_Execution** types in JSVM. You can view information about events of these types in HiSmartPerf.

#### How to Use

## Default State

JSVM trace collection is controlled by the **web.debug.rcs** switch, which is disabled by default. When a web page is started, "RCS is off" is displayed in HiLog.

## Collecting JSVM Trace

1.  To collect JSVM trace, you need to enable **web.debug.rcs** before starting the web page. Run the following command before starting the web page:
    
    hdc shell setenforce 0
    hdc shell param set web.debug.rcs true
    
2.  When a web page is started, "RCS is on" is displayed in HiLog.
    
3.  Use hitrace to capture traces of the corresponding scenario. For details about how to use hitrace, see [hitrace](../../../../../system/debugging-tools/performance-analysis-kit/command-line-tools/hitrace/document.md).
    
4.  Use HiSmartPerf to parse the captured traces. The trace points prefixed with **RCS\_** are supported by HiSmartPerf.
    
5.  To view the trace data of **compile**, **runtime**, **builtin**, and **JS\_Execution**, use the following keywords to filter the data:
    
    -   **compile**: **RCS\_v8.compile**
    -   **runtime**: **RCS\_V8.Runtime**
    -   **builtin**: **RCS\_v8.runtime\_V8.Builtin**
    -   **JS\_Execution**: **RCS\_JS\_Execution**
