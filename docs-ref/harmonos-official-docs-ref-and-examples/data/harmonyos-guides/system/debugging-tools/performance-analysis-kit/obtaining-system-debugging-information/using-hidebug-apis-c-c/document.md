# Using HiDebug APIs (C/C++)

The HiDebug C/C++ APIs are independent. You can call them to obtain debugging information. For details, see the following examples.

#### How to Develop

The following describes how to use HiDebug NDK APIs to perform thread stack backtraces and obtain the CPU usage of threads in an application.

Step 1: Create a project

1.  Use DevEco Studio to create a native C++ project and add the **test\_backtrace.cpp** and **test\_backtrace.h** files. The directory structure is as follows:
    
    entry:
      src:
        main:
          cpp:
            - types:
              - libentry:
                - index.d.ts
            - CMakeLists.txt
            - napi\_init.cpp
            - test\_backtrace.cpp
            - test\_backtrace.h
          ets:
            pages:
              - Index.ets
    
2.  Edit the **test\_backtrace.h** file as follows:
    
    #ifndef MYAPPLICATION\_TESTBACKTRACE\_H
    #define MYAPPLICATION\_TESTBACKTRACE\_H
    
    void BacktraceCurrentThread();
    
    #endif // MYAPPLICATION\_TESTBACKTRACE\_H
    
3.  Edit the **test\_backtrace.cpp** file as follows:
    
    #include "test\_backtrace.h"
    #include <condition\_variable>
    #include <csignal>
    #include <unistd.h>
    #include <sys/syscall.h>
    #include "hidebug/hidebug.h"
    #include "hilog/log.h"
    
    #define MAX\_FRAME\_SIZE 256 // Maximum stack backtrace depth. You need to adjust the value based on the service scenario.
    
    namespace {
        constexpr auto LOG\_PRINT\_DOMAIN = 0xFF00;
    }
    
    class BackTraceObject { // Encapsulate the resources required for capturing stacks. You must ensure thread safety and asynchronous signal safety.
    public:
        static BackTraceObject& GetInstance();
        BackTraceObject(const BackTraceObject&) = delete;
        BackTraceObject& operator=(const BackTraceObject&) = delete;
        BackTraceObject(BackTraceObject&&) = delete;
        BackTraceObject& operator=(BackTraceObject&&) = delete;
        bool Init(uint32\_t size);
        void Release();
        int BackTraceFromFp (void\* startFp, int size); // This function is async-signal-safe.
        void SymbolicAddress(int index); // This function is performance-intensive. Do not call it frequently.
        void PrintStackFrame(void\* pc, const HiDebug\_StackFrame& frame);
    private:
        BackTraceObject() = default;
        ~BackTraceObject() = default;
        HiDebug\_Backtrace\_Object backtraceObject\_ = nullptr;
        void\*\* pcs\_ = nullptr;
    };
    
    BackTraceObject& BackTraceObject::GetInstance() // Singleton used for exchanging data between the signal handler and the thread requesting stack capture. Note that this class is not async-signal-safe; application logic must guarantee single-thread access at any given time.
    {
        static BackTraceObject instance;
        return instance;
    }
    
    bool BackTraceObject::Init(uint32\_t size) // Initialize resources.
    {
        backtraceObject\_ = OH\_HiDebug\_CreateBacktraceObject();
        if (backtraceObject\_ == nullptr || size > MAX\_FRAME\_SIZE) {
            return false;
        }
        pcs\_ = new (std::nothrow) void\* \[size\]{nullptr};
        if (pcs\_ == nullptr) {
            return false;
        }
        return true;
    }
    
    void BackTraceObject::Release() // Release resources.
    {
        OH\_HiDebug\_DestroyBacktraceObject(backtraceObject\_);
        backtraceObject\_ = nullptr;
        delete\[\] pcs\_;
        pcs\_ = nullptr;
    }
    
    int BackTraceObject::BackTraceFromFp(void\* startFp, int size) // Perform stack backtracing to obtain the PC address.
    {
        if (size <= MAX\_FRAME\_SIZE) {
            return OH\_HiDebug\_BacktraceFromFp(backtraceObject\_, startFp, pcs\_, size); // Example of calling the OH\_HiDebug\_BacktraceFromFp API.
        }
        return 0;
    }
    
    void BackTraceObject::PrintStackFrame(void\* pc, const HiDebug\_StackFrame& frame) // Output the stack content.
    {
        if (frame.type == HIDEBUG\_STACK\_FRAME\_TYPE\_JS) { // Use different stack frame output modes based on the stack frame type.
            OH\_LOG\_Print(LOG\_APP, LOG\_INFO, LOG\_PRINT\_DOMAIN, "testTag",
                "js stack frame info for pc: %{public}p is "
                "relativePc: %{public}p "
                "line: %{public}d "
                "column: %{public}d "
                "mapName: %{public}s "
                "functionName: %{public}s "
                "url: %{public}s "
                "packageName: %{public}s.",
                pc,
                reinterpret\_cast<void\*>(frame.frame.js.relativePc),
                frame.frame.js.line,
                frame.frame.js.column,
                frame.frame.js.mapName,
                frame.frame.js.functionName,
                frame.frame.js.url,
                frame.frame.js.packageName);
        } else {
            OH\_LOG\_Print(LOG\_APP, LOG\_INFO, LOG\_PRINT\_DOMAIN, "testTag",
                "native stack frame info for pc: %{public}p is "
                "relativePc: %{public}p "
                "funcOffset: %{public}p "
                "mapName: %{public}s "
                "functionName: %{public}s "
                "buildId: %{public}s "
                "reserved: %{public}s.",
                pc,
                reinterpret\_cast<void\*>(frame.frame.native.relativePc),
                reinterpret\_cast<void\*>(frame.frame.native.funcOffset),
                frame.frame.native.mapName,
                frame.frame.native.functionName,
                frame.frame.native.buildId,
                frame.frame.native.reserved);
        }
    }
    
    void BackTraceObject::SymbolicAddress(int index)  // Stack parsing API.
    {
        if (index < 0 || index >= MAX\_FRAME\_SIZE) {
            return;
        }
        OH\_HiDebug\_SymbolicAddress(backtraceObject\_, pcs\_\[index\], this,
            \[\] (void\* pc, void\* arg, const HiDebug\_StackFrame\* frame) {
                reinterpret\_cast<BackTraceObject\*>(arg)->PrintStackFrame(pc, \*frame);
            }); // Call the OH\_HiDebug\_SymbolicAddress API to parse the stack.
    }
    
    void BacktraceCurrentThread() // This API is not thread-safe. It can be used by only one thread at a time.
    {
        if (!BackTraceObject::GetInstance().Init(MAX\_FRAME\_SIZE)) { // Ensure that resources are requested before stack backtracing. Repeated initialization is not allowed.
            BackTraceObject::GetInstance().Release();
            OH\_LOG\_Print(LOG\_APP, LOG\_WARN, LOG\_PRINT\_DOMAIN, "testTag", "failed init backtrace object.");
            return;
        }
        int pcSize = BackTraceObject::GetInstance().BackTraceFromFp(\_\_builtin\_frame\_address(0), MAX\_FRAME\_SIZE);
        for (int i = 0; i < pcSize; i++) {
            BackTraceObject::GetInstance().SymbolicAddress(i); // The main thread parses the value of PC after obtaining it.
        }
        BackTraceObject::GetInstance().Release (); // Release resources in time after stack back tracing and parsing are complete.
    }
    
4.  In the **CMakeLists.txt** file, add the dependencies.
    
    \# Add libohhidebug.so and libhilog\_ndk.z.so (log output).
    add\_library(entry SHARED napi\_init.cpp test\_backtrace.cpp)
    target\_link\_libraries(entry PUBLIC libace\_napi.z.so libhilog\_ndk.z.so libohhidebug.so)
    
5.  In the **napi\_init.cpp** file, import the dependencies and define the test method.
    
    #include <thread>
    #include "hidebug/hidebug.h"
    #include "hilog/log.h"
    #include "test\_backtrace.h"
    
    #undef LOG\_TAG
    #define LOG\_TAG "testTag"
    
    \_\_attribute((noinline)) \_\_attribute((optnone)) void TestNativeFrames(int i)
    {
        if (i > 0) {
            TestNativeFrames(i - 1);
            return;
        }
        BacktraceCurrentThread();
    }
    
    \_\_attribute((noinline)) \_\_attribute((optnone)) napi\_value TestBackTrace(napi\_env env, napi\_callback\_info info)
    {
        TestNativeFrames(1);
        return nullptr;
    }
    
    napi\_value TestGetThreadCpuUsage(napi\_env env, napi\_callback\_info info)
    {
        HiDebug\_ThreadCpuUsagePtr cpuUsage = OH\_HiDebug\_GetAppThreadCpuUsage();
        while (cpuUsage != nullptr) {
            OH\_LOG\_INFO(LogType::LOG\_APP,
                "GetAppThreadCpuUsage: threadId %{public}d, cpuUsage: %{public}f", cpuUsage->threadId, cpuUsage->cpuUsage);
            cpuUsage = cpuUsage->next; // Obtain the CPU usage object pointer of the next thread.
        }
        OH\_HiDebug\_FreeThreadCpuUsage(&cpuUsage); // Release the memory to prevent memory leaks.
        return nullptr;
    }
    
    Register **TestHiDebugNdk** as an ArkTS API and initialize the signal handling function of the main thread.
    
    napi\_property\_descriptor desc\[\] = {
        { "testGetThreadCpuUsage", nullptr, TestGetThreadCpuUsage, nullptr, nullptr, nullptr, napi\_default, nullptr },
        { "testBackTrace", nullptr, TestBackTrace, nullptr, nullptr, nullptr, napi\_default, nullptr },
    };
    
6.  In the **index.d.ts** file, declare the ArkTS API.
    
    export const testGetThreadCpuUsage: () => void;
    export const testBackTrace: () => void;
    
7.  In the **Index.ets** file, add a button to trigger the API call. The sample code is as follows:
    
    Import dependencies.
    
    import testNapi from 'libentry.so';
    
    Define the test method.
    
    function testBackTraceJsFrame(i : number) : void {
      if (i > 0) {
        return testBackTraceJsFrame(i-1);
      }
      return testNapi.testBackTrace();
    }
    
    function testBackTrace() : void {
      testBackTraceJsFrame(3);
    }
    
    function testGetThreadCpuUsage() : void {
      testNapi.testGetThreadCpuUsage();
    }
    
    Add a button to trigger the API call.
    
    Button('testGetThreadCpuUsage')
      .type(ButtonType.Capsule)
      .margin({
        top: 20
      })
      .backgroundColor('#0D9FFB')
      .width('60%')
      .height('5%')
      // Add a click event.
      .onClick(testGetThreadCpuUsage);
    
    Button('testHiDebugBackTrace')
      .type(ButtonType.Capsule)
      .margin({
        top: 20
      })
      .backgroundColor('#0D9FFB')
      .width('60%')
      .height('5%')
      // Add a click event.
      .onClick(testBackTrace);
    

Step 2: Run the project

1.  Click the **Run** button in DevEco Studio. Then, click the **testGetThreadCpuUsage** and **testHiDebugBackTrace** buttons.
    
2.  At the bottom of DevEco Studio, switch to the **Log** tab and set the filter criteria to **testTag** to view related logs.
    
    ...
    10-22 15:46:05.933   19261-19261   A00000/com.sam...gtool/testTag  com.sampl...ebugtool  I     GetAppThreadCpuUsage: threadId 19261, cpuUsage: 0.000104
    10-22 15:46:05.933   19261-19261   A00000/com.sam...gtool/testTag  com.sampl...ebugtool  I     GetAppThreadCpuUsage: threadId 19381, cpuUsage: 0.000000
    10-22 15:46:05.933   19261-19261   A00000/com.sam...gtool/testTag  com.sampl...ebugtool  I     GetAppThreadCpuUsage: threadId 19382, cpuUsage: 0.000040
    10-22 15:46:05.933   19261-19261   A00000/com.sam...gtool/testTag  com.sampl...ebugtool  I     GetAppThreadCpuUsage: threadId 19383, cpuUsage: 0.000010
    10-22 15:46:05.933   19261-19261   A00000/com.sam...gtool/testTag  com.sampl...ebugtool  I     GetAppThreadCpuUsage: threadId 19384, cpuUsage: 0.000001
    10-22 15:46:05.933   19261-19261   A00000/com.sam...gtool/testTag  com.sampl...ebugtool  I     GetAppThreadCpuUsage: threadId 19386, cpuUsage: 0.000038
    10-22 15:46:05.933   19261-19261   A00000/com.sam...gtool/testTag  com.sampl...ebugtool  I     GetAppThreadCpuUsage: threadId 19387, cpuUsage: 0.000000
    10-22 15:46:05.933   19261-19261   A00000/com.sam...gtool/testTag  com.sampl...ebugtool  I     GetAppThreadCpuUsage: threadId 19388, cpuUsage: 0.000007
    10-22 15:46:05.933   19261-19261   A00000/com.sam...gtool/testTag  com.sampl...ebugtool  I     GetAppThreadCpuUsage: threadId 19389, cpuUsage: 0.000004
    10-22 15:46:05.933   19261-19261   A00000/com.sam...gtool/testTag  com.sampl...ebugtool  I     GetAppThreadCpuUsage: threadId 19390, cpuUsage: 0.000007
    10-22 15:46:05.933   19261-19261   A00000/com.sam...gtool/testTag  com.sampl...ebugtool  I     GetAppThreadCpuUsage: threadId 19391, cpuUsage: 0.000006
    10-22 15:46:05.933   19261-19261   A00000/com.sam...gtool/testTag  com.sampl...ebugtool  I     GetAppThreadCpuUsage: threadId 19393, cpuUsage: 0.000001
    10-22 15:46:05.933   19261-19261   A00000/com.sam...gtool/testTag  com.sampl...ebugtool  I     GetAppThreadCpuUsage: threadId 19394, cpuUsage: 0.000004
    10-22 15:46:05.933   19261-19261   A00000/com.sam...gtool/testTag  com.sampl...ebugtool  I     GetAppThreadCpuUsage: threadId 19397, cpuUsage: 0.000002
    10-22 15:46:05.933   19261-19261   A00000/com.sam...gtool/testTag  com.sampl...ebugtool  I     GetAppThreadCpuUsage: threadId 19401, cpuUsage: 0.000001
    ...
    10-22 15:46:13.351   19261-19261   A0FF00/com.sam...gtool/testTag  com.sampl...ebugtool  I     native stack frame info for pc: \*\*\*\*\*\*\*\*\*\*\*\* is relativePc: \*\*\*\*\*\* funcOffset: 0x38 mapName: /data/storage/el1/bundle/libs/arm64/libentry.so functionName: TestNativeFrames(int) buildId: b6d3429f6e2e594b1c696e13049dae7e51694099 reserved: (null).
    10-22 15:46:13.351   19261-19261   A0FF00/com.sam...gtool/testTag  com.sampl...ebugtool  I     native stack frame info for pc: \*\*\*\*\*\*\*\*\*\*\*\* is relativePc: \*\*\*\*\*\* funcOffset: 0x30 mapName: /data/storage/el1/bundle/libs/arm64/libentry.so functionName: TestNativeFrames(int) buildId: b6d3429f6e2e594b1c696e13049dae7e51694099 reserved: (null).
    10-22 15:46:13.351   19261-19261   A0FF00/com.sam...gtool/testTag  com.sampl...ebugtool  I     native stack frame info for pc: \*\*\*\*\*\*\*\*\*\*\*\* is relativePc: \*\*\*\*\*\* funcOffset: 0x1c mapName: /data/storage/el1/bundle/libs/arm64/libentry.so functionName: TestBackTrace(napi\_env\_\_\*, napi\_callback\_info\_\_\*) buildId: b6d3429f6e2e594b1c696e13049dae7e51694099 reserved: (null).
    ...
    10-22 15:46:13.354   19261-19261   A0FF00/com.sam...gtool/testTag  com.sampl...ebugtool  I     js stack frame info for pc: \*\*\*\*\*\*\*\*\*\*\*\* is relativePc: \*\*\*\*\*\* line: 27 column: 21 mapName: /data/storage/el1/bundle/entry.hap functionName: testBackTraceJsFrame url: entry|entry|1.0.0|src/main/ets/pages/Index.ts packageName: .
    10-22 15:46:13.354   19261-19261   A0FF00/com.sam...gtool/testTag  com.sampl...ebugtool  I     js stack frame info for pc: \*\*\*\*\*\*\*\*\*\*\*\* is relativePc: \*\*\*\*\*\* line: 25 column: 16 mapName: /data/storage/el1/bundle/entry.hap functionName: testBackTraceJsFrame url: entry|entry|1.0.0|src/main/ets/pages/Index.ts packageName: .
    10-22 15:46:13.354   19261-19261   A0FF00/com.sam...gtool/testTag  com.sampl...ebugtool  I     js stack frame info for pc: \*\*\*\*\*\*\*\*\*\*\*\* is relativePc: \*\*\*\*\*\* line: 25 column: 16 mapName: /data/storage/el1/bundle/entry.hap functionName: testBackTraceJsFrame url: entry|entry|1.0.0|src/main/ets/pages/Index.ts packageName: .
    10-22 15:46:13.354   19261-19261   A0FF00/com.sam...gtool/testTag  com.sampl...ebugtool  I     js stack frame info for pc: \*\*\*\*\*\*\*\*\*\*\*\* is relativePc: \*\*\*\*\*\* line: 25 column: 16 mapName: /data/storage/el1/bundle/entry.hap functionName: testBackTraceJsFrame url: entry|entry|1.0.0|src/main/ets/pages/Index.ts packageName: ....
    ...
