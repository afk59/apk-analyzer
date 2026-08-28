# HiAppEvent FAQs

#### What should I do if the subscribed events cannot be found?

**Symptom**

In the development and debugging phase, when a fault such as crash or freeze occurs, the events subscribed through HiAppEvent cannot be obtained in the **HiLog** window of DevEco Studio.

**Possible Causes and Solutions**

The application exits after the crash or freeze event occurs.

You can restart the application and view the event content.

#### What should I do if the external\_log file cannot be obtained?

**Symptom**

The following log is displayed in HiLog:

-   eventInfo.params.external\_log=\[\]
    
-   HiAppEvent file does not exist
    

**Possible Causes and Solutions**

**Scenario 1**

The directory containing the **external\_log** file reaches its space limit.

The **external\_log** file is stored in the [application sandbox](../../../../../application-framework/core-file-kit/application-files/application-sandbox/document.md), and the directory space is limited. You can use the **log\_over\_limit** field to determine whether the directory containing the external\_log file reaches its space limit. If the value of **log\_over\_limit** is **true**, the directory reaches its space limit and the log file cannot be written.

**external\_log** is a string array. For example:

**external\_log=\["/data/storage/el2/log/hiappevent/APP\_CRASH\_timestamp\_xxxx.log"\]**.

**Solutions**

Clear historical log files by referring to the solution in [What should I do if the external\_log file cannot be deleted](#what-should-i-do-if-the-external_log-file-cannot-be-deleted).

**Scenario 2**

Some system events (such as time-consuming launch events) do not have **external\_log** files.

**Solutions**

Check whether the event contains **external\_log** by referring to [System Events](../using-hiappevent-to-subscribe-to-events/event-subscription-overview/document.md#system-events).

**Scenario 3**

The fault event occurs before the event subscription.

System events are not subscribed to before the **addWatcher()** API is called. Therefore, the events before event subscription do not have the **external\_log** file.

**Solutions**

Check whether the event occurs before the event subscription. The **external\_log** file of an event can be obtained only when the event occurs after event subscription.

**Scenario 4**

The system event fails to be triggered.

If no system event occurs, no **external\_log** file is generated.

**Solutions**

Obtain other logs of the system event to check whether the system event is triggered successfully.

**Scenario 5**

The **external\_log** file is deleted after being generated.

For example, the system event C is subscribed to by modules A and B in an application. After processing the callback of system event C, module A deletes the **external\_log** file. When module B accesses the **external\_log** file in the callback of system event C, a message is displayed, indicating that the log file does not exist.

**Solutions**

Check whether the **external\_log** file is deleted by other modules.

#### What should I do if the external\_log file cannot be deleted

**Symptom**

The directory containing the **external\_log** files reaches its space limit, but the **external\_log** files cannot be deleted.

**Solution**

-   If you have the permission to access the **/data/app/el2/100/log/application bundle name** directory on the device, you can manually delete the **external\_log** files.
    
    The file directory is **/data/app/el2/100/log/application bundle name/hiappevent** (or **resourcelimit**, or **watchdog**).
    
-   If you do not have the permission to access the **/data/app/el2/100/log/application bundle name** directory on the device, you can delete the **external\_log** files in the application code. The sample code is as follows: For details about the file deletion API, see [fs.unlink](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-file-fs#fsunlink).
    

**Code Example**

import { fileIo as fs } from '@kit.CoreFileKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { hiAppEvent, hilog } from '@kit.PerformanceAnalysisKit';

  hiAppEvent.addWatcher({
    // Set the watcher name. The system identifies different watchers based on their names.
    name: "AppCrashWatcher",
    // Set the subscription filters. For example, subscribe to the crash event of the system event.
    appEventFilters: \[
      {
        domain: hiAppEvent.domain.OS,
        names: \[hiAppEvent.event.APP\_CRASH\]
      }
    \],
    // Implement the onReceive callback, which is called in real time after an event is detected.
    onReceive: (domain: string, appEventGroups: Array<hiAppEvent.AppEventGroup>) => {
      hilog.info(0x0000, 'testTag', \`domain=${domain}\`);
      for (const eventGroup of appEventGroups) {
        hilog.info(0x0000, 'testTag', \`HiAppEvent eventName=${eventGroup.name}\`);
        for (const eventInfo of eventGroup.appEventInfos) {
          // Obtain the timestamp of the crash event.
          hilog.info(0x0000, 'testTag', \`HiAppEvent eventInfo.params.time=${JSON.stringify(eventInfo.params\['time'\])}\`);
          // Obtain the bundle name of the crashed application.
          hilog.info(0x0000, 'testTag', \`HiAppEvent eventInfo.params.bundle\_name=${JSON.stringify(eventInfo.params\['bundle\_name'\])}\`);
          // Obtain the error log file about the crash event.
          hilog.info(0x0000, 'testTag', \`HiAppEvent eventInfo.params.external\_log=${JSON.stringify(eventInfo.params\['external\_log'\])}\`);

          if (eventInfo.params\['external\_log'\] != undefined) {
            for (let index = 0; index < eventInfo.params\['external\_log'\].length; ++index) {
              let externalLog: string = eventInfo.params\['external\_log'\]\[index\];
              hilog.info(0x0000, 'testTag', \`externalLog=${externalLog}\`);
              // Verify the access permission.
              let res = fs.accessSync(externalLog);
              if (res) {
                hilog.info(0x0000, 'testTag', \`HiAppEvent file exists\`);
              } else {
                hilog.error(0x0000, 'testTag', \`HiAppEvent file does not exist\`);
              }
              // Verify the read and write permissions.
              fs.open(externalLog, fs.OpenMode.READ\_WRITE).then((file: fs.File) => {
              hilog.info(0x0000, 'testTag', \`HiAppEvent file=${externalLog} fd=${file.fd}\`);
              fs.closeSync(file);
              }).catch((err: BusinessError) => {
                hilog.info(0x0000, 'testTag',
                \`HiAppEvent open file=${externalLog} failed with error message=${err.message}, error code=${err.code}\`);
              });
              // Delete the external\_log file.
              fs.unlink(externalLog).then(() => {
                console.info("HiAppEvent remove file:" + externalLog + " succeed");
              }).catch((err: BusinessError) => {
                console.error("HiAppEvent remove file:" + externalLog + " failed with error message: " + err.message +
                ", error code: " + err.code);
              });
            }
          }
        }
      }
    }
  });

Log about accessing and deleting the **external\_log** file:

externalLog=/data/storage/el2/log/hiappevent/APP\_CRASH\_1751081104816\_35595.log
HiAppEvent file exists
HiAppEvent file=/data/storage/el2/log/hiappevent/APP\_CRASH\_1751081104816\_35595.log fd=61
HiAppEvent remove file:/data/storage/el2/log/hiappevent/APP\_CRASH\_1751081104816\_35595.log succeed

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bc/v3/P46-SquETPKfwDvtqxepBA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062029Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=1FE009AA233313DF14215C811ACE9A303E3F6F62605C261CF4EB342BD8BC41D7)

The path of **external\_log** is the application sandbox directory, not the actual physical path. The application has the permission to access its own sandbox directory. The **external\_log** space is limited. After processing log files, delete them in a timely manner.

#### Does a thread or process receive only its own event callbacks within the same application?

No, the thread or process also receives event callbacks from other threads or processes within the same application. For example, if an application has two processes (process A and process B) and process A has called **addWatcher()** to subscribe to crash events, process A can receive the crash callback when process B crashes. As long as the application names of processes A and B are the same, the callback can be received.

**API Reference**

[hiAppEvent.addWatcher](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-hiviewdfx-hiappevent#hiappeventaddwatcher)
