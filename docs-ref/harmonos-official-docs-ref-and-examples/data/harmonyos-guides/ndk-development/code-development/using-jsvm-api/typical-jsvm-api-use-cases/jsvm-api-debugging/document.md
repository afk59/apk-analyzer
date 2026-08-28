# JSVM-API Debugging

JavaScript virtual machine (JSVM) is a standard JavaScript (JS) code execution engine that strictly complies with the ECMAScript specification. For details, see [JSVM](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-jsvm).

The JSVM-based code debugging and tuning capabilities include Debugger, CPU Profiler, Heap Snapshot, and Heap Statistics. The following APIs are involved:

| API | Description |
| :-- | :-- |
| OH\_JSVM\_GetVM | Obtains the VM instance of a specified environment. |
| OH\_JSVM\_GetHeapStatistics | Obtains heap statistics of a VM. |
| OH\_JSVM\_StartCpuProfiler | Creates and starts a CPU profiler instance. |
| OH\_JSVM\_StopCpuProfiler | Stops the CPU profiler and outputs the result to a stream. |
| OH\_JSVM\_TakeHeapSnapshot | Obtains a snapshot of the current heap and outputs it to a stream. |
| OH\_JSVM\_OpenInspector | Opens an inspector instance on the specified host and port for debugging JS code. |
| OH\_JSVM\_OpenInspectorWithName | Opens an inspector instance based on the PID and name. |
| OH\_JSVM\_CloseInspector | Closes all remaining inspector connections. |
| OH\_JSVM\_WaitForDebugger | Waits for the host to set up a socket connection with the inspector. After the connection is set up, the application continues to run and executes the **Runtime.runIfWaitingForDebugger** command. |

This topic describes how to use Debugger, CPU Profiler, and Heap Snapshot.

#### Using Debugger

## Using OH\_JSVM\_OpenInspector

1.  Configure the permission for accessing the Internet in the **module.json** file of the application project.
    
    "requestPermissions": \[{
      "name": "ohos.permission.INTERNET",
      "reason": "$string:app\_name",
      "usedScene": {
        "abilities": \[
          "FromAbility"
        \],
        "when": "inuse"
      }
    }\]
    
2.  To prevent the pause during the debugging process from being falsely reported as no response, enable the DevEco Studio debug mode by referring to [Starting and Debugging an App/Atomic Service](https://developer.huawei.com/consumer/en/doc/harmonyos-guides-V5/ide-debug-arkts-debug-V5) without setting breakpoints or run JSVM-API in threads except the main thread.
    
    // Run the JSVM sample code in a non-main thread.
    static napi\_value RunTest(napi\_env env, napi\_callback\_info info)
    {
        std::thread testJSVMThread(TestJSVM);
        testJSVMThread.detach();
        return  nullptr;
    }
    
3.  Call **OH\_JSVM\_OpenInspector** to open an inspector instance on the specified host and port. For example, call **OH\_JSVM\_OpenInspector(env, "localhost", 9225)** to create a socket on local port 9225 of the device.
    
4.  Call **OH\_JSVM\_WaitForDebugger** to wait for the setup of a socket connection.
    
5.  Check whether the port on the device is enabled successfully. For example, run **hdc shell "netstat -anp | grep 9225"**. If the status of port 9225 is **LISTEN**, the port is enabled.
    
6.  Forward port. For example, run **hdc fport tcp:9229 tcp:9225** to forward port 9229 on a PC to port 9225 on a device. If **Forwardport result:OK** is returned, the port is forwarded successfully.
    
7.  Input **localhost:9229/json** in the address box of Google Chrome and press **Enter**. Obtain port connection information. Copy the URL in the **devtoolsFrontendUrl** field to the address box and press **Enter**.
    
    On the DevTools source code page displayed, the JS source code executed by **OH\_JSVM\_RunScript** in the application is displayed. The Debugger pauses at the first line of the JS source code.
    
    \> **NOTE**
    
    The URL specified by the **devtoolsFrontendUrl** field can be opened only on Google Chrome or Microsoft Edge. Mozilla Firefox and Apple Safari are not supported.
    
8.  You can set breakpoints on the source code page, send debugging commands using the buttons to control JS code execution, and view variables.
    
9.  Call **OH\_JSVM\_CloseInspector** to close the inspector instance and release the socket connection.
    

**Sample Code**

If you are just starting out with JSVM-API, see [JSVM-API Development Process](../../jsvm-api-development-process/document.md). The following demonstrates only the C++ code involved.

#include "ark\_runtime/jsvm.h"

#include <string>

using namespace std;

// JS source code to be debugged.
static string srcDebugger = R"JS(
const concat = (...args) => args.reduce((a, b) => a + b);
var dialogue = concat('"What ', 'is ', 'your ', 'name ', '?"');
dialogue = concat(dialogue, ' --', '"My ', 'name ', 'is ', 'Bob ', '."');
)JS";

// Enable Debugger.
static void EnableInspector(JSVM\_Env env) {
    // Open an inspector instance on the specified host and port to create a socket.
    OH\_JSVM\_OpenInspector(env, "localhost", 9225);
    // Wait for the host to set up a socket connection with the inspector.
    OH\_JSVM\_WaitForDebugger(env, true);
}

// Close Debugger.
static void CloseInspector(JSVM\_Env env) {
    // Close the inspector to release the socket connection.
    OH\_JSVM\_CloseInspector(env);
}

static void RunScript(JSVM\_Env env) {
    JSVM\_HandleScope handleScope;
    OH\_JSVM\_OpenHandleScope(env, &handleScope);

    JSVM\_Value jsSrc;
    OH\_JSVM\_CreateStringUtf8(env, srcDebugger.c\_str(), srcDebugger.size(), &jsSrc);

    JSVM\_Script script;
    OH\_JSVM\_CompileScript(env, jsSrc, nullptr, 0, true, nullptr, &script);

    JSVM\_Value result;
    OH\_JSVM\_RunScript(env, script, &result);

    OH\_JSVM\_CloseHandleScope(env, handleScope);
}

void TestJSVM() {
    JSVM\_InitOptions initOptions{};
    OH\_JSVM\_Init(&initOptions);

    JSVM\_VM vm;
    OH\_JSVM\_CreateVM(nullptr, &vm);
    JSVM\_VMScope vmScope;
    OH\_JSVM\_OpenVMScope(vm, &vmScope);

    JSVM\_Env env;
    OH\_JSVM\_CreateEnv(vm, 0, nullptr, &env);
    // Enable Debugger before executing the JS code.
    EnableInspector(env);
    JSVM\_EnvScope envScope;
    OH\_JSVM\_OpenEnvScope(env, &envScope);

    // Execute the JS code.
    RunScript(env);

    OH\_JSVM\_CloseEnvScope(env, envScope);
    // Close Debugger after the JS code is executed.
    CloseInspector(env);
    OH\_JSVM\_DestroyEnv(env);
    OH\_JSVM\_CloseVMScope(vm, vmScope);
    OH\_JSVM\_DestroyVM(vm);
}

## Using OH\_JSVM\_OpenInspectorWithName

1.  Configure the permission for accessing the Internet in the **module.json** file of the application project.
    
    "requestPermissions": \[{
      "name": "ohos.permission.INTERNET",
      "reason": "$string:app\_name",
      "usedScene": {
        "abilities": \[
          "FromAbility"
        \],
        "when": "inuse"
      }
    }\]
    
2.  To prevent the pause during the debugging process from being falsely reported as no response, [enable the DevEco Studio debug mode](https://developer.huawei.com/consumer/en/doc/harmonyos-guides-V5/ide-debug-arkts-debug-V5) without setting breakpoints or run JSVM-API in threads except the main thread.
    
3.  Enable the inspector port and connect to devtools for debugging.
    
    Before executing the JS code, call **OH\_JSVM\_OpenInspector** to open an inspector instance on the specified host and port and create a socket. For example, call **OH\_JSVM\_OpenInspectorWithName (env, 123, "test")** to create a TCP socket and the corresponding unixdomain port.
    
4.  Call **OH\_JSVM\_WaitForDebugger** to wait for the setup of a socket connection.
    
5.  Check whether the port on the device is enabled successfully.
    
    Run **hdc shell "cat /proc/net/unix | grep jsvm"**. An available Unix port is displayed, for example, **jsvm\_devtools\_remote\_9229\_123**, where **9229** is the TCP port number and **123** is the PID.
    
6.  Forward port.
    
    For example, run **hdc fport tcp:9229 tcp:9229** to forward port 9229 on a PC to port 9229 on a device. If **Forwardport result:OK** is returned, the port is forwarded successfully.
    
7.  Input **localhost:9229/json** in the address box of Google Chrome and press **Enter**. Obtain port connection information. Open Google Chrome DevTools, copy the URL in the **devtoolsFrontendUrl** field to the address box, and press **Enter**.
    
    On the DevTools source code page displayed, the JS source code executed by **OH\_JSVM\_RunScript** is displayed. The Debugger pauses at the first line of the JS code.
    
    \> **NOTE**
    
    The URL specified by the **devtoolsFrontendUrl** field can be opened only on Google Chrome or Microsoft Edge. Mozilla Firefox and Apple Safari are not supported.
    
8.  You can set breakpoints on the source code page, send debugging commands using the buttons to control JS code execution, and view variables.
    
9.  Call **OH\_JSVM\_CloseInspector** to close the inspector instance and release the socket connection.
    

**Sample Code**

Replace the "//Enable Debugger" section with the following:

// Enable Debugger.
static void EnableInspector(JSVM\_Env env) {
    // Open an inspector instance on the specified host and port to create a socket.
    OH\_JSVM\_OpenInspectorWithName(env, 123, "test");
    // Wait for the host to set up a socket connection with the inspector.
    OH\_JSVM\_WaitForDebugger(env, true);
}

## Using Chrome Inspect

In addition to opening the URL specified by the **devtoolsFrontendUrl** field for debugging, you can also open the **chrome://inspect/#devices** page on Google Chrome to perform debugging. The procedure is as follows:

1.  On Google Chrome, enter **chrome://inspect/#devices** in the address box and press **Enter**. On the page displayed, select the following options:
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d4/v3/Sbb_e0VUR8uyqTpeBlA2vw/en-us_image_0000002568765023.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062134Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=B428BC644AD18E861C207C4BCCE36E612AFE282ED6356B649A1AAE3324B1D4AB)
2.  Run **hdc fport** \[Port number on the developer's PC\] \[Port number on a device\] to forward a port.
    
    Example: **hdc fport tcp:9227 tcp:9226**
    
3.  Click **Port forwarding**, enter the port number on the PC in the left text box and the port number on the device in the right text box, and click **Done**, as shown in the figure below.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/88/v3/-zfQfHlbT5CokfJ7AHOUKA/en-us_image_0000002537765298.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062134Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=F94203065C416E4B3C9C76B17B70101339E2BE80052D716FB5880B27E69D2CFF)
4.  Click **Configure**, enter the port number on the PC, for example, **localhost:9227**, and click **Done**, as shown in the figure below.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f4/v3/3h8kEH2sRVC5tbnNdz3P0A/en-us_image_0000002537925238.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062134Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=C77A4B8C98947F881B167515A5C55FF892303465FF7D798B99A7DEAA6380917F)
5.  Wait until the debugging content is displayed under **Target**, and click **inspect** to start debugging, as shown in the figure below.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fd/v3/lsRsw__kSkCmSr_Sk9ohLQ/en-us_image_0000002568685015.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062134Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=9667C394BFB400973FEAC2610F2C9843034A82A9D767EF48EC4E3613C4DCF63D)

## Using WebSocket Port

In addition to opening the URL specified by the **devtoolsFrontendUrl** field through Chrome DevTools, if you know how to use Chrome DevTools Protocol (CDP), you can also connect to the WebSocket port provided by Inspector for debugging.

The procedure is as follows: After port mapping (for example, mapping to port 9229) is complete, enter **localhost:9229/json** in the address box of Chrome and press **Enter** to obtain the URL of the **webSocketDebuggerUrl** field. Then, use the standard WebSocket client to connect to the URL to send CDP for debugging. Note that the WebSocket port provided by Inspector of the current version can receive only text frames, ping frames, and connection close frames. All other types of frames are considered as error frames, which will interrupt the WebSocket connection.

For details about CDP, see [the official document](https://chromedevtools.github.io/devtools-protocol/).

#### Using CPU Profiler and Heap Snapshot

## Using CPU Profiler APIs

1.  Before executing the JS code, call **OH\_JSVM\_StartCpuProfiler** to start sampling and return a **JSVM\_CpuProfiler** instance.
2.  Run the JS code and call **OH\_JSVM\_StopCpuProfiler**, in which you need to pass in the **JSVM\_CpuProfiler** instance (obtained in step 1), callback for the output stream, and pointer to the output stream. Then, the data will be written to the specified output stream.
3.  Obtain the output data in JSON strings. You can also save it to the **.cpuprofile** file, which can be parsed into profiling views with the Chrome DevTools-JavaScript Profiler.

## Using Heap Snapshot APIs

1.  To analyze the heap object creation of a piece of JS code, call **OH\_JSVM\_TakeHeapSnapshot** before and after the JS code is executed. You need to pass in the callback used to return the output stream and the pointer to the output stream. Then, the data will be written to the specified output stream.
2.  Save the output data to the **.heapsnapshot** file, which can be parsed into memory analysis views with the Chrome DevTools-Memory.

## Example

If you are just starting out with JSVM-API, see [JSVM-API Development Process](../../jsvm-api-development-process/document.md). The following demonstrates only the C++ code involved.

#include "ark\_runtime/jsvm.h"

#include <fstream>
#include <iostream>

using namespace std;

// JS code to be optimized.
static string srcProf = R"JS(
function sleep(delay) {
    var start = (new Date()).getTime();
    while ((new Date()).getTime() - start < delay) {
        continue;
    }
}

function work3() {
    sleep(300);
}

function work2() {
    work3();
    sleep(200);
}

function work1() {
    work2();
    sleep(100);
}

work1();
)JS";

// Callback for the data output stream, which is customized to process the returned data. In this example, the output data is written to a file.
static bool OutputStream(const char \*data, int size, void \*streamData) {
    auto &os = \*reinterpret\_cast<ofstream \*>(streamData);
    if (data) {
        os.write(data, size);
    } else {
        os.close();
    }
    return true;
}

static JSVM\_CpuProfiler ProfilingBegin(JSVM\_VM vm) {
    // Specify the path of the file saving the output profiling data. In this example, the sandbox path is /data/storage/el2/base/files, and the bundle name is com.example.helloworld.
    // The output data will be saved to /data/app/el2/100/base/com.example.helloworld/files/heap-snapshot-begin.heapsnapshot.
    ofstream heapSnapshot("/data/storage/el2/base/files/heap-snapshot-begin.heapsnapshot",
                          ios::out | ios::binary | ios::trunc);
    // Task a heap snapshot before the JS code is executed.
    OH\_JSVM\_TakeHeapSnapshot(vm, OutputStream, &heapSnapshot);
    JSVM\_CpuProfiler cpuProfiler;
    // Start the CPU Profiler.
    OH\_JSVM\_StartCpuProfiler(vm, &cpuProfiler);
    return cpuProfiler;
}

// Stop the profiling data collection tool.
static void ProfilingEnd(JSVM\_VM vm, JSVM\_CpuProfiler cpuProfiler) {
    // Specify the path of the file saving the output profiling data. In this example, the sandbox path is /data/storage/el2/base/files, and the bundle name is com.example.helloworld.
    // The output data will be saved to /data/app/el2/100/base/com.example.helloworld/files/cpu-profile.cpuprofile.
    ofstream cpuProfile("/data/storage/el2/base/files/cpu-profile.cpuprofile",
                        ios::out | ios::binary | ios::trunc);
    // Stop the CPU Profiler to obtain data.
    OH\_JSVM\_StopCpuProfiler(vm, cpuProfiler, OutputStream, &cpuProfile);
    ofstream heapSnapshot("/data/storage/el2/base/files/heap-snapshot-end.heapsnapshot",
                              ios::out | ios::binary | ios::trunc);
    // After the JS is executed, take a heap snapshot again and compare the two snapshots for further analysis.
    OH\_JSVM\_TakeHeapSnapshot(vm, OutputStream, &heapSnapshot);
}

static JSVM\_Value RunScriptWithStatistics(JSVM\_Env env, JSVM\_CallbackInfo info) {
    JSVM\_VM vm;
    OH\_JSVM\_GetVM(env, &vm);

    // Start profiling.
    auto cpuProfiler = ProfilingBegin(vm);

    JSVM\_HandleScope handleScope;
    OH\_JSVM\_OpenHandleScope(env, &handleScope);

    JSVM\_Value jsSrc;
    OH\_JSVM\_CreateStringUtf8(env, srcProf.c\_str(), srcProf.size(), &jsSrc);

    JSVM\_Script script;
    OH\_JSVM\_CompileScript(env, jsSrc, nullptr, 0, true, nullptr, &script);

    JSVM\_Value result;
    // Execute the JS code.
    OH\_JSVM\_RunScript(env, script, &result);

    OH\_JSVM\_CloseHandleScope(env, handleScope);

    // End profiling.
    ProfilingEnd(vm, cpuProfiler);
    return nullptr;
}
static JSVM\_CallbackStruct param\[\] = {
    {.data = nullptr, .callback = RunScriptWithStatistics},
};
static JSVM\_CallbackStruct \*method = param;
// Alias for the runScriptWithStatistics method to be called from JS.
static JSVM\_PropertyDescriptor descriptor\[\] = {
    {"runScriptWithStatistics", nullptr, method++, nullptr, nullptr, nullptr, JSVM\_DEFAULT},
};

JS example:

const char \*srcCallNative = R"JS(runScriptWithStatistics();)JS";

Expected result:

Two files are generated in the HarmonyOS device for subsequent optimization.
heap-snapshot-end.heapsnapshot,
cpu-profile.cpuprofile
For file features, see API usage.
