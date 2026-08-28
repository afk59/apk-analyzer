# Event Subscription (C/C++)

HiAppEvent provides APIs for subscribing to application events.

#### Available APIs

For details about the APIs, including the parameter usage and value ranges, see [hiappevent.h](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-hiappevent-h).

**Subscription APIs**

| API | Description |
| :-- | :-- |
| int OH\_HiAppEvent\_AddWatcher(HiAppEvent\_Watcher\* watcher) | Adds a watcher to subscribe to the application event. |
| int OH\_HiAppEvent\_RemoveWatcher(HiAppEvent\_Watcher\* watcher) | Removes a watcher to unsubscribe from the application event. |

**Event Logging APIs**

| API | Description |
| :-- | :-- |
| int OH\_HiAppEvent\_Write(const char\* domain, const char\* name, enum EventType type, const ParamList list) | Logs application events whose parameters are of the list type. |

#### How to Develop

The following describes how to subscribe to a crash event (system event) and a button click event (application event).

## Step 1: Creating a Project and Configuring Compilation Options

1.  Obtain the **jsoncpp** file on which the sample project depends.
    
    Specifically, download the source code package from [JsonCpp](https://github.com/open-source-parsers/jsoncpp) and obtain the **jsoncpp.cpp**, **json.h**, and **json-forwards.h** files by following the procedure described in **Amalgamated source** in the **README** file.
    
    Create a native C++ project and import the **jsoncpp** file to the project. The directory structure is as follows:
    
    entry
    └── src
        └── main
            ├── cpp
            │   ├── CMakeLists.txt
            │   ├── json
            │   │   ├── json-forwards.h
            │   │   └── json.h
            │   ├── jsoncpp.cpp
            │   ├── napi\_init.cpp
            │   └── types
            │       └── libentry
            │           ├── Index.d.ts
            │           └── oh-package.json5
            └── ets
                ├── entryability
                │   └── EntryAbility.ets
                └── pages
                    └── Index.ets
    
2.  In the **CMakeLists.txt** file, add the source file and dynamic libraries.
    
    \# Add the jsoncpp.cpp file, which is used to parse the JSON strings in the subscription events.
    add\_library(entry SHARED napi\_init.cpp jsoncpp.cpp)
    # Add libhiappevent\_ndk.z.so and libhilog\_ndk.z.so (log output).
    target\_link\_libraries(entry PUBLIC libace\_napi.z.so libhilog\_ndk.z.so libhiappevent\_ndk.z.so)
    
3.  Import the dependencies to the **napi\_init.cpp** file, and define **LOG\_TAG**.
    
    #include "napi/native\_api.h"
    #include "json/json.h"
    #include "hilog/log.h"
    #include "hiappevent/hiappevent.h"
    #include "hiappevent/hiappevent\_event.h"
    
    #undef LOG\_TAG
    #define LOG\_TAG "testTag"
    

## Step 2: Subscribing to an Event

1.  Subscribe to the events using **OnReceive** and **OnTrigger**, respectively.
    
    -   Subscribe to the crash event (system event) using **OnReceive**. After receiving the event, the watcher immediately triggers the **OnReceive** callback. In the **napi\_init.cpp** file, define the methods related to the watcher of the **OnReceive** type.
    
    // Define a variable to cache the pointer to the created watcher.
    static HiAppEvent\_Watcher \*eventWatcherR1;
    
    static void OnReceive1(const char \*domain, const struct HiAppEvent\_AppEventGroup \*appEventGroups, uint32\_t groupLen)
    {
        OH\_LOG\_INFO(LogType::LOG\_APP, "AppEvents HiAppEvent success to read events with onReceive callback from C API \\n");
        for (int i = 0; i < groupLen; ++i) {
            for (int j = 0; j < appEventGroups\[i\].infoLen; ++j) {
                OH\_LOG\_INFO(LogType::LOG\_APP, "AppEvents HiAppEvent eventInfo.domain=%{public}s",
                    appEventGroups\[i\].appEventInfos\[j\].domain);
                OH\_LOG\_INFO(LogType::LOG\_APP, "AppEvents HiAppEvent eventInfo.name=%{public}s",
                    appEventGroups\[i\].appEventInfos\[j\].name);
                OH\_LOG\_INFO(LogType::LOG\_APP, "AppEvents HiAppEvent eventInfo.eventType=%{public}d",
                    appEventGroups\[i\].appEventInfos\[j\].type);
                if (strcmp(appEventGroups\[i\].appEventInfos\[j\].domain, DOMAIN\_OS) != 0 ||
                    strcmp(appEventGroups\[i\].appEventInfos\[j\].name, EVENT\_APP\_CRASH) != 0) {
                    continue;
                }
                Json::Value params;
                Json::Reader reader(Json::Features::strictMode());
                Json::FastWriter writer;
                if (reader.parse(appEventGroups\[i\].appEventInfos\[j\].params, params)) {
                    // Obtain the timestamp of the crash event.
                    OH\_LOG\_INFO(LogType::LOG\_APP, "AppEvents HiAppEvent eventInfo.params.time=%{public}lld",
                        params\["time"\].asInt64());
                    // Obtain the bundle name of the crashed application.
                    OH\_LOG\_INFO(LogType::LOG\_APP, "AppEvents HiAppEvent eventInfo.params.bundle\_name=%{public}s",
                        params\["bundle\_name"\].asString().c\_str());
                    auto external\_log = writer.write(params\["external\_log"\]);
                    // Obtain the error log file about the crash event.
                    OH\_LOG\_INFO(LogType::LOG\_APP, "AppEvents HiAppEvent eventInfo.params.external\_log=%{public}s",
                        external\_log.c\_str());
                }
            }
        }
    }
    static napi\_value RegisterWatcherCrash(napi\_env env, napi\_callback\_info info)
    {
        // Set the watcher name. The system identifies different watchers based on their names.
        eventWatcherR1 = OH\_HiAppEvent\_CreateWatcher("AppCrashWatcher1");
        // Set the event name for subscription to EVENT\_APP\_CRASH (the crash event).
        const char \*names\[\] = {EVENT\_APP\_CRASH};
        // Add the events to watch, for example, system events.
        OH\_HiAppEvent\_SetAppEventFilter(eventWatcherR1, DOMAIN\_OS, 0, names, 1);
        // Set the implemented callback. After receiving the event, the watcher immediately triggers the OnReceive1 callback.
        OH\_HiAppEvent\_SetWatcherOnReceive(eventWatcherR1, OnReceive1);
        // Add a watcher to listen for the specified event.
        OH\_HiAppEvent\_AddWatcher(eventWatcherR1);
        return {};
    }
    
    -   Subscribe to the button click event (application event) using **OnTrigger**. The **OnTrigger()** callback can be triggered only when the conditions specified by **OH\_HiAppEvent\_SetTriggerCondition()** are met. In the **napi\_init.cpp** file, define the methods related to the watcher of the **OnTrigger** type.
    
    // Define a variable to cache the pointer to the created watcher.
    static HiAppEvent\_Watcher \*eventWatcherT1;
    // Implement the callback function used to return the listened events. The content pointed to by the events pointer is valid only in this function.
    static void OnTake1(const char \*const \*events, uint32\_t eventLen)
    {
        Json::Reader reader(Json::Features::strictMode());
        OH\_LOG\_INFO(LogType::LOG\_APP, "AppEvents HiAppEvent success to read events with onTrigger callback from C API \\n");
        for (int i = 0; i < eventLen; ++i) {
            OH\_LOG\_INFO(LogType::LOG\_APP, "AppEvents HiAppEvent eventInfo=%{public}s", events\[i\]);
            Json::Value eventInfo;
            if (reader.parse(events\[i\], eventInfo)) {
                auto domain = eventInfo\["domain\_"\].asString();
                auto name = eventInfo\["name\_"\].asString();
                auto type = eventInfo\["type\_"\].asInt();
                OH\_LOG\_INFO(LogType::LOG\_APP, "AppEvents HiAppEvent eventInfo.domain=%{public}s", domain.c\_str());
                OH\_LOG\_INFO(LogType::LOG\_APP, "AppEvents HiAppEvent eventInfo.name=%{public}s", name.c\_str());
                OH\_LOG\_INFO(LogType::LOG\_APP, "AppEvents HiAppEvent eventInfo.eventType=%{public}d", type);
                if (domain == "button" && name == "click") {
                    auto clickTime = eventInfo\["clickTime"\].asInt64();
                    OH\_LOG\_INFO(LogType::LOG\_APP, "AppEvents HiAppEvent eventInfo.params.clickTime=%{public}lld",
                        clickTime);
                }
            }
        }
    }
    
    // Implement the subscription callback function to apply custom processing to the obtained event logging data.
    static void OnTrigger1(int row, int size)
    {
        // After the callback is received, obtain the specified number of received events.
        OH\_HiAppEvent\_TakeWatcherData(eventWatcherT1, row, OnTake1);
    }
    
    static napi\_value RegisterWatcherClick(napi\_env env, napi\_callback\_info info)
    {
        // Set the watcher name. The system identifies different watchers based on their names.
        eventWatcherT1 = OH\_HiAppEvent\_CreateWatcher("ButtonClickWatcher1");
        // Set the name of the subscribed event to click.
        const char \*names\[\] = {"click"};
        // Add the system events to watch, for example, events related to button.
        OH\_HiAppEvent\_SetAppEventFilter(eventWatcherT1, "button", 0, names, 1);
        // Set the implemented callback function. The callback function will be triggered when the conditions set by OH\_HiAppEvent\_SetTriggerCondition are met.
        OH\_HiAppEvent\_SetWatcherOnTrigger(eventWatcherT1, OnTrigger1);
        // Set the conditions for triggering the subscription callback. For example, trigger this onTrigger callback when the number of new event logs is 1.
        OH\_HiAppEvent\_SetTriggerCondition(eventWatcherT1, 1, 0, 0);
        // Add a watcher to listen for the specified event.
        OH\_HiAppEvent\_AddWatcher(eventWatcherT1);
        return {};
    }
    
2.  In the **napi\_init.cpp** file, add the logging API for the button click event.
    
    static napi\_value WriteAppEvent(napi\_env env, napi\_callback\_info info)
    {
        auto params = OH\_HiAppEvent\_CreateParamList();
        OH\_HiAppEvent\_AddInt64Param(params, "clickTime", time(nullptr));
        OH\_HiAppEvent\_Write("button", "click", EventType::BEHAVIOR, params);
        OH\_HiAppEvent\_DestroyParamList(params);
        OH\_LOG\_INFO(LogType::LOG\_APP, "writeEvent C++ success");
        return {};
    }
    
3.  In the **napi\_init.cpp** file, register **RegisterWatcherCrash()** (crash event subscription), **RegisterWatcherClick()** (button click event subscription), and **WriteAppEvent()** (button click event logging) as ArkTS APIs.
    
    // ...
    
    static napi\_value Init(napi\_env env, napi\_value exports)
    {
        napi\_property\_descriptor desc\[\] = {
            // ...
            { "registerWatcherCrash", nullptr, RegisterWatcherCrash, nullptr, nullptr, nullptr, napi\_default, nullptr },
            { "registerWatcherClick", nullptr, RegisterWatcherClick, nullptr, nullptr, nullptr, napi\_default, nullptr },
            { "writeAppEvent", nullptr, WriteAppEvent, nullptr, nullptr, nullptr, napi\_default, nullptr },
            // ...
        };
        napi\_define\_properties(env, exports, sizeof(desc) / sizeof(desc\[0\]), desc);
        return exports;
    }
    
4.  In the **index.d.ts** file, define the ArkTS API.
    
    export const registerWatcherCrash: () => void;
    export const registerWatcherClick: () => void;
    export const writeAppEvent: () => void;
    
5.  In the **EntryAbility.ets** file, add the following API to **onCreate()**.
    
    import testNapi from 'libentry.so';
    
    // Add the C API call in onCreate().
    // Register the crash event watcher at startup.
    testNapi.registerWatcherCrash();
    // Register the button click event watcher at startup.
    testNapi.registerWatcherClick();
    

## Step 3: Triggering an Event

In the **Index.ets** file of the project, add the **WatchAppCrash ArkTS&C++** button to trigger a crash event, and add the writeEvent C++ button in **onClick()** to log the event. The sample code is as follows:

import testNapi from 'libentry.so';

Button('WatchAppCrash ArkTS&C++')
  .type(ButtonType.Capsule)
  .margin({
    top: 20
  })
  .backgroundColor('#0D9FFB')
  .width('80%')
  .height('5%')
  .onClick(() => {
    // Construct a scenario in onClick() to trigger a crash event.
    let result: object = JSON.parse('');
  })

Button('writeEvent C++')
  .type(ButtonType.Capsule)
  .margin({
    top: 20
  })
  .backgroundColor('#0D9FFB')
  .width('80%')
  .height('5%')
  .onClick(() => {
    testNapi.writeAppEvent();
  })

#### Debugging and Verification

1.  Click the **Run** button in DevEco Studio to run the project. On the application UI, click **WatchAppCrash ArkTS&C++** to trigger a crash event. After the application exits, restart it.
    
2.  Search for the keyword **AppEvents** in the HiLog window to view the logs of the crash event processing.
    
    AppEvents HiAppEvent success to read events with onReceive callback from C API
    AppEvents HiAppEvent eventInfo.domain=OS
    AppEvents HiAppEvent eventInfo.name=APP\_CRASH
    AppEvents HiAppEvent eventInfo.eventType=1
    AppEvents HiAppEvent eventInfo.params.time=1750946685473
    AppEvents HiAppEvent eventInfo.params.bundle\_name=com.example.cxxxx
    AppEvents HiAppEvent eventInfo.params.external\_log=\["/data/storage/el2/log/hiappevent/APP\_CRASH\_1750946685805\_64003.log"\]
    
3.  Click the **writeEvent C++** button to trigger the button click event. Search for the keyword **AppEvents** in the HiLog window to view the logs of the button click event processing.
    
    AppEvents HiAppEvent success to read events with onTrigger callback from C API
    AppEvents HiAppEvent eventInfo={"domain\_":"button","name\_":"click","type\_":4,"time\_":1750947007108,"tz\_":"","pid\_":64750,"tid\_":64750,"clickTime":1750947007}
    AppEvents HiAppEvent eventInfo.domain=button
    AppEvents HiAppEvent eventInfo.name=click
    AppEvents HiAppEvent eventInfo.eventType=4
    AppEvents HiAppEvent eventInfo.params.clickTime=1750947007
    
4.  Remove the application event watcher.
    
    static napi\_value RemoveWatcher(napi\_env env, napi\_callback\_info info)
    {
        // Remove the watcher.
        // ...
        OH\_HiAppEvent\_RemoveWatcher(eventWatcherT1);
        OH\_HiAppEvent\_RemoveWatcher(eventWatcherR1);
        // ...
        return {};
    }
    
5.  Destroy the application event watcher.
    
    static napi\_value DestroyWatcher(napi\_env env, napi\_callback\_info info)
    {
        // Destroy the created watcher and set eventWatcher to nullptr.
        // ...
        OH\_HiAppEvent\_DestroyWatcher(eventWatcherT1);
        OH\_HiAppEvent\_DestroyWatcher(eventWatcherR1);
        eventWatcherT1 = nullptr;
        eventWatcherR1 = nullptr;
        // ...
        return {};
    }
