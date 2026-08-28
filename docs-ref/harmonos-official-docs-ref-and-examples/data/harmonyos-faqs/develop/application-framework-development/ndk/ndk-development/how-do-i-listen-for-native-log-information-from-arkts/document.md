# How do I listen for native log information from ArkTS?

**Question**

Would you please provide an example to implement the following: register an ArkTS log listener in native code so that logs can be reported to ArkTS via a callback when the log API is called in any service on the native side?

**Answer**

1.  Create a **Log.ts** file in ArkTS (note that the file name extension is **ts** but not **ets**) and encapsulate the log listening API in a singleton.
    
    import { hilog } from '@kit.PerformanceAnalysisKit';
    
    
    export class GlobalThisAdapter {
      private constructor() {
      }
    
    
      private static instance: GlobalThisAdapter;
      private \_logListener: LogsListener = new LogsListener();
    
    
      public static getInstance(): GlobalThisAdapter {
        if (!GlobalThisAdapter.instance) {
          GlobalThisAdapter.instance = new GlobalThisAdapter();
        }
        return GlobalThisAdapter.instance;
      }
    
    
      getLogsListener(): LogsListener | undefined {
        return this.\_logListener;
      }
    
    
      setLogsListener(value: LogsListener): void {
        this.\_logListener = value;
      }
    }
    
    
    export class LogsListener implements OnLogsListener {
      public constructor() {
      }
    
    
      onLogs(level: LogLevel, message: string): void {
        switch (level) {
          case LogLevel.DEBUG:
            hilog.debug(0x0000, 'debug', 'debug message is %{public}s', message);
            break;
          case LogLevel.INFO:
            hilog.info(0x0000, 'info', 'info message is %{public}s', message);
            break;
          case LogLevel.WARN:
            hilog.warn(0x0000, 'warn', 'warn message is %{public}s', message)
            break;
          case LogLevel.ERROR:
            hilog.error(0x0000, 'error', 'error message is %{public}s', message);
            break;
          case LogLevel.FATAL:
            hilog.fatal(0x0000, 'fatal', 'fatal message is %{public}s', message);
            break;
          default:
            hilog.info(0x0000, 'info', 'info message is %{public}s', message);
        }
      }
    }
    
    
    enum LogLevel {
      DEBUG = 3,
      INFO,
      WARN,
      ERROR,
      FATAL
    }
    
    
    export default interface OnLogsListener {
      onLogs(level: number, message: string): void;
    }
    
2.  Add the API implementation in native code. Note that **napi\_create\_reference** is used to create a reference, and **napi\_ref** is used to manage the object lifecycle and is not affected by **NativeScope**. Use **napi\_get\_named\_property** and **napi\_call\_function** to obtain **OnLogsListener** and **onLogs** and bind them to ArkTS.
    
    #include "napi/native\_api.h"
    #include <bits/alltypes.h>
    #include <cstring>
    #include <hilog/log.h>
    
    
    napi\_ref logListenerRef = nullptr;
    napi\_ref onLogsFuncRef = nullptr;
    static napi\_value RegisterLogListener(napi\_env env, napi\_callback\_info info) {
        size\_t argc = 1;
        napi\_value globalThisAdapter = nullptr;
        napi\_get\_cb\_info(env, info, &argc, &globalThisAdapter, nullptr, nullptr);
    
    
        napi\_value getLogListenerFunc = nullptr;
        napi\_get\_named\_property(env, globalThisAdapter, "getLogsListener", &getLogListenerFunc);
    
    
        napi\_value logListener = nullptr;
        napi\_call\_function(env, globalThisAdapter, getLogListenerFunc, 0, nullptr, &logListener);
    
    
        napi\_value onLogsFunc = nullptr;
        napi\_get\_named\_property(env, logListener, "onLogs", &onLogsFunc);
    
    
        napi\_create\_reference(env, logListener, 1, &logListenerRef);
        napi\_create\_reference(env, onLogsFunc, 1, &onLogsFuncRef);
    
    
        return nullptr;
    }
    
3.  Add the API mappings in native code to implement the APIs.
    
    EXTERN\_C\_START
    static napi\_value Init(napi\_env env, napi\_value exports) {
        napi\_property\_descriptor desc\[\] = {
            {"add", nullptr, Add, nullptr, nullptr, nullptr, napi\_default, nullptr},
            {"registerLogListener", nullptr, RegisterLogListener, nullptr, nullptr, nullptr, napi\_default, nullptr}};
        napi\_define\_properties(env, exports, sizeof(desc) / sizeof(desc\[0\]), desc);
        return exports;
    }
    EXTERN\_C\_END
    
4.  Export APIs from **index.t.ets**.
    
    import { GlobalThisAdapter } from '../../../ets/interface/Log'
    export const add: () => void;
    export const registerLogListener: (a: GlobalThisAdapter) => void;
    
5.  Register the log API. Use **registerLogListener** to register the ArkTS log implementation with the native. In this example, the **onCreate** method in the **EntryAbility.ets** file is used for registration.
    
    onCreate(want: Want, launchParam: AbilityConstant.LaunchParam): void {
      let globalThisAdapter: GlobalThisAdapter = GlobalThisAdapter.getInstance();
      testNapi.registerLogListener(globalThisAdapter);
      hilog.info(0x0000, 'testTag', '%{public}s', 'Ability onCreate');
    }
    
6.  Add the callback to be invoked when the API is called. When the API is called on the native side, the **onLogs** will be called in ArkTS.
    
    static void callOnLogs(napi\_env env, LogLevel level, const char \*message) {
    
    
        size\_t argc = 2;
        napi\_value argv\[2\] = {nullptr};
    
    
        int32\_t tem = level;
        napi\_create\_int32(env, tem, &argv\[0\]);
        napi\_create\_string\_utf8(env, message, strlen(message) + 1, &argv\[1\]);
        napi\_value logListener = nullptr;
        napi\_value onLogsFunc = nullptr;
        napi\_get\_reference\_value(env, logListenerRef, &logListener);
        napi\_get\_reference\_value(env, onLogsFuncRef, &onLogsFunc);
    
    
        napi\_call\_function(env, logListener, onLogsFunc, argc, argv, nullptr);
    }
    
7.  Call other service code. The following uses **Add()** as an example. When the **callOnLogs** method in **Add()** is called, the **onLogs** callback will be invoked on the ArkTS side.
    
    static napi\_value Add(napi\_env env, napi\_callback\_info info) {
        callOnLogs(env, LogLevel::LOG\_INFO, "execute native Add function success");
        return nullptr;
    }
