# hilog

HiLog is a log system that provides logging for the system framework, services, and applications to record information on user operations and system running status. You can run the hilog commands to query related log information.

#### Environment Setup

-   The environment for HarmonyOS Device Connector (hdc) has been set up. For details, see [Environment Setup](../hdc/document.md#environment-setup).
    
-   The devices are properly connected and **hdc shell** is executed.
    

#### HiLog Overview

## Log Generation

If the HiLog API is called in the service code, HiLog logs are generated during service running.

## Viewing Logs

**Online Checking**

-   Run the hdc shell hilog command.
-   Use DevEco Studio. For details, see [Log Analysis](../../../../../coding-and-debugging/analyzing-logs-and-faults/log-analysis/document.md).
    
    **Checking Downloaded Files**
    
-   log version: By default, HiLog logs are flushed to disk, and a maximum of 1000 files can be flushed.
-   nolog version: HiLog logs are not flushed to disk by default. You need to manually enable the flushing feature. For details, see [Checking and Setting Persisting Tasks](#checking-and-setting-persisting-tasks).After the developer option is enabled, the flushing feature is automatically enabled.
-   Log storage path: data/log/hilog on the device. You can export and view the logs. For details about the tool, see [hilogtool](../../../debugging-commands/hilogtool/document.md).
-   log and nolog versions: On the phone, go to Settings > About phone > Software version. The log version ends with log.

## Log Format

Date Time Process ID Thread ID Log level Domain ID/Log tag: Log content
04-19 17:02:14.735  5394  5394 I A03200/test\_server/testTag: this is a info level hilog

This is an info log with domainID 0x3200, process name test\_server, and tag testTag.

NOTE:

-   Log level: I indicates the info level. For other levels, refer to the first letter of the word.
    
-   domainID: A in A03200 indicates the application log (LOG\_APP), and 3200 indicates that the domainID is 0x3200. For details about the domainID, see the API guide.
    

#### Commands

| Short Option | Long Option | Parameter | Description |
| :-- | :-- | :-- | :-- |
| \-h | \--help | \- | Shows help information. |
| Default | Default | \- | Performs a blocking read on logs, with no exiting after the read finishes. |
| \-x | \--exit | \- | Performs a non-blocking read on logs, with exiting after the read finishes. |
| \-a | \--head | <n> | Shows the first several lines of logs. The parameter **<n>** indicates the number of first lines to show. |
| \-z | \--tail | <n> | Shows the last several lines of logs. The parameter **<n>** indicates the number of last lines to show. |
| \-t | \--type | <type> | Views logs of a specified type. |
|  |  | app | Views application logs. |
|  |  | core | Views system logs. |
|  |  | init | Views startup logs. |
|  |  | kmsg | Views kernel logs. |
|  |  | only\_prerelease | Views logs that are printed before the system release version. Application developers do not need to pay attention to these logs. |
| \-L | \--level | <level> | Sets the log level, for example, **\-L D/I/W/E/F**. |
| \-D | \--domain | <domain> | Sets the domain. |
| \-T | \--tag | <tag> | Sets the tag. |
| \-P | \--pid | <pid> | Identifies a process. |
| \-e | \--regex | <expr> | Prints only the lines of logs that match the regular expression specified through **<expr>**. |
| \-v | \--format | <format> | Sets the display format. |
|  |  | color/colour | Displays logs in different colors. By default, logs are displayed in black and white. |
|  |  | time | Displays the local time. |
|  |  | epoch | Displays the amount of time elapsed since the epoch time. |
|  |  | monotonic | Displays the amount of time elapsed since the system startup time. |
|  |  | msec | Displays the time in milliseconds. |
|  |  | usec | Displays the time in microseconds. |
|  |  | nsec | Displays the time in nanoseconds. |
|  |  | year | Displays the time with the year portion. |
|  |  | zone | Displays the time with the local time zone. |
|  |  | wrap | Displays logs in different lines without adding prefixes such as the timestamp to the new line. |
|  |  | long | Displays all data fields separated by spaces. |
| \-r | \- | \- | Clears the buffer for logs of a specified type. This option is used together with **\-t**, which specifies a log type. By default, the **app** or **core** types are used. |
| \-g | \- | \- | Checks the buffer size for logs of a specified type. This option is used together with **\-t**, which specifies a log type. By default, the **app** or **core** types are used. |
| \-G | \--buffer-size | <size> | Sets the size of the buffer for logs of a specified type. This option is used together with **\-t**, which specifies a log type. By default, the **app** or **core** types are used. The unit can be B, KB, MB, or GB. The value ranges from 64 KB to 16 MB. |
| \-s | \--statistics | \- | Shows statistics. This option must be used together with **\-t** or **\-D**. |
| \-S | \- | \- | Clears statistics. This option must be used together with **\-t** or **\-D**. |
| \-w | \--write | <control> | Controls a flushing task. |
|  |  | query | Queries flushing tasks. |
|  |  | start | Starts a flushing task. The command line parameters are the file name, size of a single file, flushing mode, and number of rotated files. |
|  |  | stop | Stops a flushing task. |
|  |  | refresh | Refreshes the logs in the buffer to the flushed file. |
|  |  | clear | Deletes log files that are flushed to disks. |
| \-f | \--filename | <filename> | Sets the names of the files to be flushed to disk. |
| \-l | \--length | <length> | Sets the size of the files to be flushed to disk. The value must be greater than or equal to 64 KB. |
| \-n | \--number | <number> | Sets the number of files to be flushed to disk. |
| \-m | \--stream | <algorithm> | Sets the flushing mode. |
|  |  | none | Indicates that data is flushed to disks in non-compression mode. |
|  |  | zlib | Indicates that data is flushed to disks using the zlib compression algorithm. The flushed file is in .gz format. |
| \-j | \--jobid | <jobid> | Sets the ID of a flushing task. |
| \-p | \--privacy | <on/off> | Specifies whether to enable privacy for logs during system debugging. |
|  |  | on | Enables privacy so that parameters are displayed as **<private>** in printed logs. |
|  |  | off | Disables privacy so that parameters are displayed as they are in printed logs. |
| \-k | \- | <on/off> | Specifies whether to enable kernel logging. |
|  |  | on | Enables kernel logging. |
|  |  | off | Disables kernel logging. |
| \-Q | \- | <control-type> | Controls whether to enable the default quota when the threshold is exceeded. |
|  |  | pidon | Enables the process flow control. |
|  |  | pidoff | Disables the process flow control. |
|  |  | domainon | Enables the domain flow control. |
|  |  | domainoff | Disables the domain flow control. |
| \-b | \--baselevel | <loglevel> | Sets the lowest level of logs that can be printed: D(DEBUG)/I(INFO)/W(WARN)/E(ERROR)/F(FATAL). This command can be used together with **\-D** and **\-T** to set the lowest log level. |
| \- | \--persist | \- | Persists the log level setting command. (The setting will not be lost after the system is restarted.) |

#### Displaying the Help Information

hilog -h

**Example**

 $ hilog -h
 Usage:
 -h --help
   Show all help information.
   Show single help information with option:
   query/clear/buffer/stats/persist/private/kmsg/flowcontrol/baselevel/domain/combo
 Querying logs options:
   No option performs a blocking read and keeps printing.
   -x --exit
     Performs a non-blocking read and exits when all logs in buffer are printed.
   -a <n>, --head=<n>
     Show n lines logs on head of buffer.
   -z <n>, --tail=<n>
     Show n lines logs on tail of buffer.

#### **Non-Blocking Log Reading**

hilog -x

**Example**

   $ hilog -x
   11-15 15:51:02.087  2823  2823 I A01B05/com.ohos.sceneboard/AOD: AodClockFullScreen --> timeTextLineHeight:313.3333333333333 clockMarginTop:99
   11-15 15:51:02.087  2823  2823 I A01B05/com.ohos.sceneboard/AOD: AodClockFullScreen --> timeFontSize:114.48717948717947
   11-15 15:51:02.090  2823  2823 I A01B05/com.ohos.sceneboard/AOD: AodClockFullScreen --> timeTextWidth:202,timeTextHeight:292
   11-15 15:51:02.100  2823  2823 I A01B05/com.ohos.sceneboard/AOD: ComponentUtil --> Component(ComponentId-AodClockNumber) draw complete.
   11-15 15:51:02.110  1197  1197 E C01406/render\_service/OHOS::RS: \[LoadImgsbyResolution\] Can't find resolution (1084 x 2412) in config file
   11-15 15:51:02.127  1197  1197 E C01406/render\_service/OHOS::RS: \[LoadImgsbyResolution\] Can't find resolution (1084 x 2412) in config file

#### **Viewing Logs of a Specified Level**

hilog -L D/I/W/E/F

**Example**

   $ hilog -L E
   08-28 09:01:25.730  2678  2678 E A00F00/com.aidataservice/AiDataService\_5.10.7.320: DataChangeNotifyManager: notifyDataChange CommonEntity no valid entity to notify
   08-28 09:01:56.058  8560  8560 E A00500/com.ohos.settingsdata/SettingsData: DB not ready request = datashare:///com.ohos.settingsdata/entry/settingsdata/SETTINGSDATA?Proxy=true&key=analysis\_service\_switch\_on , retry after DB startup
   08-28 09:01:56.082  8560  8560 E A00500/com.ohos.settingsdata/SettingsData: decoder failure: /data/migrate/settings\_global.xml , error code:-1
   08-28 09:01:56.082  8560  8560 E A00500/com.ohos.settingsdata/SettingsData: clearXml failed:No such file or directory, error code:13900002
   08-28 09:01:56.083  8560  8560 E A00500/com.ohos.settingsdata/SettingsData: readText failed:No such file or directory, error code:13900002
   08-28 09:01:56.371  8586  8586 E A00500/com.ohos.settingsdata/SettingsData: DB not ready request =    datashare:///com.ohos.settingsdata/entry/settingsdata/SETTINGSDATA?Proxy=true&key=photo\_network\_connection\_status , retry after DB startup
   08-28 09:01:56.408  8586  8586 E A00500/com.ohos.settingsdata/SettingsData: decoder failure: /data/migrate/settings\_global.xml , error code:-1

#### **Viewing Logs of a Specified Type**

hilog -t app

**Example**

   $ hilog -t app
   11-15 16:04:45.903  5630  5630 I A0A5A5/os.hiviewcare:staticSubscriber/Diagnosis: \[DetectionFilter\]820001084: switch off
   11-15 16:04:45.905  5630  5630 I A0A5A5/os.hiviewcare:staticSubscriber/Diagnosis: \[DetectionFilter\]847005050: frequency limit
   11-15 16:04:45.905  5630  5630 I A0A5A5/os.hiviewcare:staticSubscriber/Diagnosis: \[SmartNotifyHandler\]detections after filter: \[\]
   11-15 16:04:45.905  5630  5630 I A0A5A5/os.hiviewcare:staticSubscriber/Diagnosis: \[SmartNotifyHandler\]no detections to detect
   11-15 16:04:45.924  5687  5687 I A01B06/common/KG: MetaBalls-SystemTopPanelController --> init charging status = 3

#### **Viewing Logs of a Specified Domain**

hilog -D 01B06

**Example**

   $ hilog -D 01B06
   11-15 16:04:54.981  5687  5687 I A01B06/common/KG: MetaBalls-MetaBallRenderer --> pressTime = 0 appearTime = 1731657885972
   11-15 16:04:54.981  5687  5687 I A01B06/common/KG: MetaBalls-MetaBallRenderer --> backAnimator on finish
   11-15 16:04:54.982  5687  5687 I A01B06/common/KG: MetaBalls-MetaBallRenderer --> setTimeout over 9s and begin animate on finish
   11-15 16:04:55.297  5687  5687 I A01B06/common/KG: MetaBalls-MetaBallRenderer --> chargingTextExitAnimation onFinish
   11-15 16:04:55.494  5687  5687 I A01B06/common/KG: MetaBalls-MetaBallRenderer --> uiExtension session send data success,type: exitAnimationFinish

#### **Viewing Logs of a Specified Domain**

hilog -T tag

**Example**

   $ hilog -T SAMGR
   08-28 09:27:59.581   610 11504 I C01800/samgr/SAMGR: CommonEventCollect save extraData 1661
   08-28 09:27:59.581   610 11504 I C01800/samgr/SAMGR: OnReceiveEvent get action: usual.event.BATTERY\_CHANGED code: 0, extraDataId 1661
   08-28 09:27:59.582   610 11504 I C01800/samgr/SAMGR: DoEvent:4 name:usual.event.BATTERY\_CHANGED value:0
   08-28 09:27:59.582   610 11504 W C01800/samgr/SAMGR: LoadSa SA:10120 AddDeath fail,cnt:1,callpid:610
   08-28 09:27:59.583   610 11504 I C01800/samgr/SAMGR: LoadSa SA:10120 size:1,count:1
   08-28 09:27:59.601   610 11504 I C01800/samgr/SAMGR: Scheduler SA:10120 loading
   08-28 09:27:59.965 11518 11518 I C01800/media\_analysis\_service/SAMGR: SA:10120 OpenSo spend 315ms
   08-28 09:27:59.965   610  4064 I C01800/samgr/SAMGR: AddProc:media\_analysis\_service. size:75

#### **Viewing the First n Lines of Logs in the Buffer**

hilog -a 8

**Example**

   $ hilog -a 8
   11-15 16:04:08.628     0     0 I I00000/HiLog: ========Zeroth log of type: init
   11-15 16:04:08.603   506   506 I I02C01/cust\_carrier\_mount/CustCarrierMount: MountCarrierToShared start
   11-15 16:04:08.604   506   506 I I02C01/cust\_carrier\_mount/CustCarrierMount: success to mount carrier to shared
   11-15 16:04:15.394   972   972 I I02C01/cust\_carrier\_mount/CustCarrierMount: UpdateCotaOpkeyLink start
   11-15 16:04:15.396   972   972 W I02C01/cust\_carrier\_mount/CustCarrierMount: not exsit CUST\_GLOBAL\_CARRIER\_DIR or COTA\_PARAM\_CARRIER\_DIR
   11-15 16:04:15.887   972   972 I I02C01/cust\_carrier\_mount/CustCarrierMount: success to update cota carrier
   11-15 16:04:48.749  5777  5901 I A00001/com.hiai.core/HiAI\_Metadata: metadata is null
   11-15 16:04:48.749  5777  5901 I A00001/com.hiai.core/HiAI\_PluginAbilityInfo: abilityInfo is null

#### **Viewing the Last n Lines of Logs in the Buffer**

hilog -z 8

**Example**

   $ hilog -z 8
   11-15 16:12:19.015  1899  7867 W C01719/wifi\_manager\_service/ffrt: 423:FFRTQosApplyForOther:244 tid 7867, Operation not permitted, ret:-1, eno:1
   11-15 16:12:19.125  1043  1072 I C01C42/time\_service/TimeService: uid: 1010 id:428551571 name:wifi\_manager\_service wk:0
   11-15 16:12:19.125  1043  1072 I C01C42/time\_service/TimeService: bat: -1 id:428551571 we:505225000000 mwe:512725000000
   11-15 16:12:19.125  1043  1072 I C01C42/time\_service/TimeService: typ:3 trig: 505 225000000, bt: 495230369193
   11-15 16:12:19.125  1043  1072 I C01C42/time\_service/TimeService: cb: 428551571 ret: 0
   11-15 16:12:19.435  3086  7813 I C01719/com.ohos.contactsdataability/ffrt: 45:~WorkerThread:72 to exit, qos\[3\]
   11-15 16:12:19.691   800  1404 I C01713/resource\_schedule\_service/SUSPEND\_MANAGER: \[(HasSpecialStateFromBgtask):759\] 20020107\_com.ohos.medialibrary.medialibrarydata
   11-15 16:12:19.691   800  1404 I C01713/resource\_schedule\_service/SUSPEND\_MANAGER: \[(DozeFreezeUnit):890\] Doze has special:ERR\_HAS\_PID\_EFFICIENCY\_RESOURCE

#### **Viewing Logs of a Specified Process**

hilog -P pid

**Example**

   $ hilog -P 618
   08-28 10:19:16.872   618 17729 I C02D15/hiview/XPower: \[task\_52\]#current system load is: 0.028767
   08-28 10:19:23.997   618 17580 I C02D10/hiview/CpuCollector: CalculateProcessCpuStatInfos: startTime=1724811553746, endTime=1724811563996, startBootTime=47001084, endBootTime=47011335, period=10251
   08-28 10:19:23.999   618 17580 I C02D10/hiview/CpuCollector: CollectProcessCpuStatInfos: collect process cpu statistics information size=234, isNeedUpdate=1
   08-28 10:19:24.002   618 17580 W C01650/hiview/Rdb:  DB :
   08-28 10:19:24.002   618 17580 W C01650/hiview/Rdb:  device: 12583051 inode: 40230 mode: 432 size: 569344 natime: Wed Aug 28 00:00:06 2024
   08-28 10:19:24.002   618 17580 W C01650/hiview/Rdb:  smtime: Wed Aug 28 00:34:30 2024
   08-28 10:19:24.002   618 17580 W C01650/hiview/Rdb:  sctime: Wed Aug 28 00:34:30 2024

#### **Viewing Logs That Match the Regular Expression Keyword**

hilog -e start

**Example**

   $ hilog -e start
   11-15 16:17:17.578   547  4504 I C01800/SAMGR: AddProc start proc:media\_analysis\_service spend 223ms
   11-15 16:17:17.578   547  4504 I C01800/SAMGR: Scheduler proc:media\_analysis\_service handle started event
   11-15 16:17:17.578   547  4504 I C01800/SAMGR: Scheduler proc:media\_analysis\_service started
   11-15 16:17:17.580  8877  8877 I C01810/media\_analysis\_service/SAFWK: start tasks proc:media\_analysis\_service end,spend 1ms
   11-15 16:17:17.582  8877  8877 I C01651/media\_analysis\_service/DataShare: \[operator()()-data\_share\_manager\_impl.cpp:134\]: RecoverObs start
   11-15 16:17:17.589  8877  8893 I C01651/media\_analysis\_service/DataShare: \[Connect()-ams\_mgr\_proxy.cpp:67\]: connect start, uri = \*\*\*\*\*\*/media
   11-15 16:17:18.225  1155  1633 I C02943/power\_host/ThermalHdi: CreateLogFile start
   11-15 16:17:18.264  1155  1633 I C02943/power\_host/ThermalHdi: CompressFile start

#### **Viewing Logs in Different Formats**

hilog -v time/color/epoch/monotonic/usec/nsec/year/zone/wrap

**Example**

Display the local time in milliseconds.

   $ hilog -v time
   11-15 16:36:21.027  1134  1723 I C02B01/riladapter\_host/HrilExt: \[NotifyToBoosterTel-(hril\_manager\_ext.cpp:440)\] RilExt:Notify to booster tel finish
   11-15 16:36:21.027  1134  1723 I C02B01/riladapter\_host/HrilExt: \[NotifyToBoosterNet-(hril\_manager\_ext.cpp:450)\] RilExt: HNOTI\_BOOSTER\_NET\_IND report to booster net
   11-15 16:36:21.027  1134  1723 I C02B01/riladapter\_host/HrilExt: \[NotifyToBoosterNet-(hril\_manager\_ext.cpp:454)\] RilExt: HNOTI\_BOOSTER\_NET\_IND report to booster net finish
   11-15 16:36:21.027  1134  1723 I P01FFF/riladapter\_host/Rilvendor: CHAN \[HandleUnsolicited\] HandleUnsolicited done for modem:0, index:0, atResponse:^BOOSTERNTF: 3, 20,"0600100001000004000000000102A4FF0202F6FF"
   11-15 16:36:21.802  2809  2831 E C02D06/com.ohos.sceneboard/XCollie: Send kick,foundation to hungtask Successful
   11-15 16:36:21.911   882  3016 I C01F0B/telephony/TelephonyVSim: state machine ProcessEvent Id: 125
   11-15 16:36:21.911   882  3016 I C01F0B/telephony/TelephonyVSim: StateProcess

   $ hilog -v nsec
   11-15 16:37:09.010658555  1134  1723 I C02B01/riladapter\_host/HrilExt: \[BoosterRawInd-(hril\_booster.cpp:296)\] RilExt: BoosterRawInd
   11-15 16:37:09.010676263  1134  1723 I C02B01/riladapter\_host/HrilExt: \[BoosterRawInd-(hril\_booster.cpp:328)\] check need notify to satellite:indType 6
   11-15 16:37:09.010800221  1134  1723 I C02B01/riladapter\_host/HrilExt: \[NotifyToBoosterTel-(hril\_manager\_ext.cpp:436)\] RilExt: report to telephony ext, requestNum: 4201
   11-15 16:37:09.011011680  1134  1723 I C02B01/riladapter\_host/HrilExt: \[NotifyToBoosterTel-(hril\_manager\_ext.cpp:440)\] RilExt:Notify to booster tel finish
   11-15 16:37:09.011064805  1134  1723 I C02B01/riladapter\_host/HrilExt: \[NotifyToBoosterNet-(hril\_manager\_ext.cpp:450)\] RilExt: HNOTI\_BOOSTER\_NET\_IND report to booster net
   11-15 16:37:09.011200742  1134  1723 I C02B01/riladapter\_host/HrilExt: \[NotifyToBoosterNet-(hril\_manager\_ext.cpp:454)\] RilExt: HNOTI\_BOOSTER\_NET\_IND report to booster net finish

#### Checking and Setting Persisting Tasks

**Viewing persist tasks**

hilog -w query

No persist task exists:

$ hilog -w query
Persist task query failed
No running persistent task \[CODE: -63\]

Persist tasks exist:

$ hilog -w query
1 init,core,app,only\_prerelease zlib /data/log/hilog/hilog 4.0M 1000
2 kmsg zlib /data/log/hilog/hilog\_kmsg 4.0M 100

**Enabling a persist task**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ee/v3/z20vJ5hsQiCwjChEUb57Nw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062030Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=B2150D9232801307B91D7F0E7B003758ABC7100A6B4BADD2635FFCBFA18AF579)

You can only enable a persist task when no persist task exists. If a persist task exists, stop it first.

Enable a HiLog persist task and set the number of persist files to **1000**.

$ hilog -w start -n 1000
Persist task \[jobid:1\]\[fileNum:1000\]\[fileSize:4194304\] start successfully

Enable a kmsglog persist task and set the number of persist files to **100**.

$ hilog -w start -n 100 -t kmsg
Persist task \[jobid:2\]\[fileNum:100\]\[fileSize:4194304\] start successfully

When enabling a persist task, you can customize the persist rules. The compression mode can be **zlib**, **zstd**, or **none**.

For example, run the following command to set the persistent file name to **kmsglog**, file size to **2 MB**, number of files to **100**, and compression mode to **zlib**:

$ hilog -w start -t kmsg -f kmsglog -l 2M -n 100 -m zlib
Persist task \[jobid:2\]\[fileNum:100\]\[fileSize:2097152\] start successfully

**Disabling a persist task**

Stop the current persist task:

$ hilog -w stop
Persist task \[jobid:1\] stop successfully
Persist task \[jobid:2\] stop successfully

#### Displaying and Setting Log Levels

**Viewing the Global Log Level**

$ param get hilog.loggable.global
I

The default global log level is **INFO**.

**Setting Log Levels**

// Set the global log level.
hilog -b D/I/W/E/F
// Set the global log level. The setting still takes effect after the device is restarted.
hilog -b D/I/W/E/F --persist
// Set the log output level for \[DOMAINID\] of the LOG\_APP type.
hilog -b D/I/W/E/F -D 0x\[DOMAINID\]
// Set the log output level for \[DOMAINID\] of the LOG\_CORE type.
hilog -b D/I/W/E/F -D d0\[DOMAINID\]
// Set the log output level for \[TAG\].
hilog -b D/I/W/E/F -T \[TAG\]

**Example**:

$ hilog -b E
Set global log level to E successfully
$ hilog -b E --persist
Set global log level to E successfully
Set persist global log level to E successfully
$ hilog -b D -D 0x2d00
Set domain 0x2d00 log level to D successfully
$ hilog -b D -D d001719
Set domain 0xd001719 log level to D successfully
$ hilog -b E -T testTag
Set tag testTag log level to E successfully

#### Other Common Commands

## Displaying the Log Buffer Size

hilog -g

**Example**

$ hilog -g
Log type app buffer size is 16.0M
Log type init buffer size is 16.0M
Log type core buffer size is 16.0M
Log type only\_prerelease buffer size is 16.0M

## Setting the Log Buffer Size

hilog -G size

**Example**

$ hilog -G 16M
Set log type app buffer size to 16.0M successfully
Set log type init buffer size to 16.0M successfully
Set log type core buffer size to 16.0M successfully
Set log type only\_prerelease buffer size to 16.0M successfully

## Clearing the Log Buffer

hilog -r

**Example**

$ hilog -r
Log type core,app,only\_prerelease buffer clear successfully

## Setting Kernel Log Reading

hilog -k on/off

**Example**

$ hilog -k on
Set hilogd storing kmsg log on successfully

$ hilog -k off
Set hilogd storing kmsg log off successfully

## Displaying Statistics

hilog -s

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5e/v3/mk1skvkpT_SNtHtfnl9O3A/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062030Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=24CD053F8394DF6F2F7CED562FFB03C252AD9C57A08B422E4AF23BC568F19AB6)

You need to run the **param set persist.sys.hilog.stats true** command to enable the statistics functionality, and restart the device before starting statistics collection.

**Example**

$ param set persist.sys.hilog.stats true
Set parameter persist.sys.hilog.stats true success
$ reboot
$ hilog -s
Log statistic report (Duration: 0h0m32s.564, From: 11-15 16:04:08.628):
Total lines: 137517, length: 8.0M
DEBUG lines: 0(0%), length: 0.0B(0%)
INFO lines: 101795(74%), length: 6.1M(76%)
WARN lines: 10268(7.5%), length: 719.9K(8.8%)
ERROR lines: 25452(19%), length: 1.2M(15%)
FATAL lines: 2(0.0015%), length: 259.0B(0.0031%)
------------------------------------------------------------
Domain Table:
LOGTYPE- DOMAIN---- TAG----------------------------- MAX\_FREQ-- TIME---------------- MAX\_TP---- TIME---------------- LINES----- LENGTH---- DROPPED---
app----- 0xf00----- -------------------------------- 924.00---- 11-15 16:04:25.594-- 111975.00- 11-15 16:04:25.594-- 3386------ 371.5K---- 0---------
app----- 0x0------- -------------------------------- 285.00---- 11-15 16:04:34.877-- 44242.00-- 11-15 16:04:34.877-- 990------- 129.2K---- 0---------

**Description**

MAX\_FREQ: the maximum number of log lines per second
TIME: occurrence time
MAX\_TP: the maximum number of bytes per second
LINES: the total number of lines in a statistical period
LENGTH: the total number of bytes in a statistical period
DROPPED: the number of dropped lines in a statistical period

## Clearing Statistics

hilog -S

**Example**

$ hilog -S
Statistic info clear successfully

## Setting Process Flow Control

hilog -Q pidon/pidoff

**Example**

Enable process flow control:

$ hilog -Q pidon
Set flow control by process to enabled successfully

Disable process flow control:

$ hilog -Q pidoff
Set flow control by process to disabled successfully

## Setting Domain Flow Control

hilog -Q domainon/domainoff

**Example**

Enable domain flow control:

$ hilog -Q domainon
Set flow control by domain to enabled successfully

Disable domain flow control:

$ hilog -Q domainoff
Set flow control by domain to disabled successfully

#### HiLog Flow Control Mechanism

When the number of logs exceeds the upper limit, the HiLog flow control mechanism is triggered. After this mechanism is triggered, excessive logs are discarded, and a warning log is generated. By default, this mechanism is disabled for debug applications.

The flow control mechanism is as follows:

## Application Logs

The flow control is performed by process. The application logs printed in the **LOG\_APP** buffer adapt to the PID flow control mechanism. When the number of logs of the **LOG\_APP** type printed by a process exceeds the threshold within one second, the flow control is triggered. The following example shows the warning log:

04-19 17:02:34.219  5394  5394 W A00032/com.example.myapplication/LOGLIMIT: ==com.example.myapplication LOGS OVER PROC QUOTA, 3091 DROPPED==

This log indicates that the number of logs printed by the\*\* com.example.myapplication\*\* process exceeds the upper limit. Before 17:02:34.219, 3091 lines of logs are discarded due to the upper limit control.

**Solution**: Disable the process control mechanism by referring to [Setting Process Flow Control](#setting-process-flow-control).

## System Logs

The flow control is performed by domain ID. The system logs printed in the **LOG\_CORE** buffer adapt to the domain flow control mechanism. When the number of logs of the **LOG\_CORE** type printed by a domain ID exceeds the threshold within one second, the flow control is triggered. The following is an example of the warning log:

04-19 17:02:34.219  5394  5394 W C02C02/system\_test/LOGLIMIT: 108 line(s) dropped in a second!

This log indicates that the number of logs whose domain ID is **02C02** exceeds the upper limit. Before 17:02:34.219, 108 lines of logs are discarded due to the upper limit control.

**Solution**: Disable the domain control mechanism by referring to [Setting Domain Flow Control](#setting-domain-flow-control).

#### Handling Log Loss

Currently, maintenance and debugging information is available in all log loss scenarios. You can search for the corresponding keyword in HiLog to view the causes.

You can use regular expressions to search for log lines containing the keywords **LOGLIMIT**, **Slow reader missed**, and **write socket failed**.

**LOGLIMIT** indicates that log loss occurs due to process or domain flow control. **Slow reader missed** indicates that global logs are lost. **write socket failed** indicates that process logs are lost.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5b/v3/NHYyecPcT3GgWPF2NDv61g/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062030Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=3C38D2633A19772FEAA541CCB15BB70E76FBCB2579B5C30B93B57C615622589D)

When these messages are displayed, logs are lost and cannot be restored.

If the log loss issue occurs in the online O&M scenario, rectify the fault by referring to the following method, reproduce the issue locally, and view the complete logs.

## LOGLIMIT

**LOGLIMIT** indicates that the number of printed logs exceeds the threshold defined by the process or domain flow control. If domain logs exceed the HiLog specifications, you must reduce and correct them at the domain level. The following is an example of the warning log:

04-19 17:02:34.219  5394  5394 W A00032/com.example.myapplication/LOGLIMIT: ==com.example.myapplication LOGS OVER PROC QUOTA, 3091 DROPPED==

**Solution**: Disable the corresponding control mechanism by referring to [HiLog Flow Control Mechanism](#hilog-flow-control-mechanism)

## Slow reader missed

**Slow reader missed** indicates that a large number of logs are generated before and after the printing time point. As a result, the logs in the HiLog buffer are overwritten circularly before they are persisted. The following is an example of the warning log:

04-19 17:02:34.219     0     0 I C00000/HiLog: ========Slow reader missed log lines: 137

**Cause**: Global logs are lost in any of the following situations:

-   The log level is set to **D**.
    
-   The flow control is disabled.
    
-   A module is repeatedly printing logs.
    

**Solution**

-   Run the **hilog -g** command to query the current buffer size.
    
-   Run the **hilog -G** command to increase the HiLog buffer size. For example, run the following command to change the buffer size to 16 MB (the maximum size is 16 MB):
    
    hilog -G 16M
    
-   Check whether logs are frequently printed in the background. If logs of a domain are frequently printed and log reading is affected, you can run the command to disable the log printing of the domain by referring to the "Solution" of **write socket failed**.
    

## write socket failed

**write socket failed** indicates that logs fail to be written into the socket and packet loss occurs. The following is an example of the warning log:

04-19 17:02:34.219  5394  5394 W A00032/com.example.myapplication/HiLog: write socket failed, 8 line(s) dropped!

**Cause**: Process logs are lost in any of the following situations:

-   The log level is set to **D**.
    
-   The flow control is disabled.
    
-   A module is repeatedly printing logs.
    
-   If a high CPU load or insufficient memory issue occurs, the socket server processes logs slowly and logs are stacked in the socket channel. As a result, the client fails to write socket data.
    

**Solution**: Disable the log printing of other domains and print only the logs of the current module.

-   Disable the log printing of other domains:
    
    hilog -b X
    
-   Enable the log printing of the current module:
    
    **LOG\_APP**:
    
    hilog -b I -D 0x3200  (Set the log print level of the 03200 domain to INFO.)
    
    hilog -b I -D 0x3201  (Set the log print level of the 03201 domain to INFO.)
    
    **LOG\_CORE**:
    
    hilog -b I -D d003200  (Set the log print level of the 03200 domain to INFO.)
    
    hilog -b I -D d003201  (Set the log print level of the 03201 domain to INFO.)
