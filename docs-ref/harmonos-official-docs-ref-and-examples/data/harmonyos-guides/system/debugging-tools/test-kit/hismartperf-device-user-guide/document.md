# HiSmartPerf Device User Guide

#### Introduction

HiSmartPerf Device, a performance and power consumption testing tool, supports monitoring key metrics such as FPS, CPU, GPU, RAM, and Temperature, and includes the device daemon. This Daemon can be accessed via shell commands and is compatible with both devices with and without a display.

## Indicators

-   CPU: The tool reads the frequencies and usage of CPU cores on the test device on a per second basis to measure the CPU usage of the target application. Sustained high CPU may lead to overheating.
-   GPU: The tool reads the GPU frequency and load information of the test device on a per second basis to measure the GPU usage of the target application. High GPU usage can lead to performance drops and application slowdowns.
-   FPS: The tool reads the frame rate, in frames per second (FPS), of the target application to measure the smoothness of the application image. A higher FPS generally means smoother visuals.
-   TEMP: The tool reads the temperature information of the test device on a per second basis, including the GPU temperature and system chip temperature.
-   RAM: The tool reads the RAM usage of the target application on a per second basis.
-   snapshot: The tool takes a screenshot of the application UI every 2 seconds.

#### Principles

The figure below demonstrates the main functions of HiSmartPerf Device. Commands entered on the PC are transmitted to the HiSmartPerf Device-daemon via USB. The daemon parses these commands to collect data, outputs the results to the CLI, and generates a CSV file upon completion of data collection.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f3/v3/3cXIOUmhTECCP0I7UI6h5A/en-us_image_0000002484496325.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062031Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=DC51694BA8A5444B21E61578B6B1EE7742A8A9404FB73BDB619BEE072672E466)

#### Constraints

1.  Device-daemon is pre-installed since API version 9.
    
2.  Device-daemon must be connected to a hardware device.
    
3.  Before using Device-daemon, [configure the hdc environment](https://gitee.com/openharmony/developtools_hdc) and go to the shell environment to start the daemon process.

**Switch to Shell**

C:\\Users\\issusser>hdc shell
$

**Start the daemon process**

C:\\Users\\issusser>hdc shell
// Start the daemon process.
$ SP\_daemon 
// Check whether the daemon process is running.
$ ps -ef | grep SP\_daemon
shell          1584     1 0 21:50:05 ?     00:00:00 SP\_daemon
shell          1595  1574 3 21:51:02 pts/0 00:00:00 grep SP\_daemon
$

#### HiSmartPerf Device-daemon

## Viewing the Help Information

$ SP\_daemon --help
OpenHarmony performance testing tool SmartPerf command-line version
Usage: SP\_daemon \[options\] \[arguments\]
 
options:
 -N              set the collection times(default value is 0) range\[1,2147483647\], for example: -N 10
 -PKG            set package name, must add, for example: -PKG ohos.samples.ecg
 -PID            set process pid, must add, for example: -PID 3568
 -threads        get threads, must add -PID or -PKG for example:
                 -threads -PID 3568 or -threads -PKG ohos.samples.ecg
 -c              get device CPU frequency and CPU usage, process CPU usage and CPU load ..
 -ci             get cpu instructions and cycles
 -g              get device GPU frequency and GPU load
 -gc             get gpu counter default frequency is 50
 -f              get app refresh fps(frames per second) and fps jitters and refreshrate
 -profilerfps    get refresh fps and timestamp
 -sections       set collection time period(using with profilerfps)
 -t              get remaining battery power and temperature..
 -p              get battery power consumption and voltage(Not supported by some devices)
 -print          start mode print log
 -r              get process memory and total memory
 -snapshot       get screen capture
 -nav            get page navigation information
 -net            get uplink and downlink traffic
 -start          collection start command
 -stop           collection stop command
 -VIEW           set layler, for example: -VIEW DisplayNode
 -OUT            set csv output path.
 -d              get device DDR information
 -screen         get screen resolution
 -deviceinfo     get device information
 -server         start a process to listen to the socket message of the start and stop commands
 -clear          clear the process ID
 -ohtestfps      used by the vilidator to obtain the fps, the collection times can be set
 -editorServer   start a process to listen to the socket message of the editor
 -recordcapacity get the battery level difference
 --version       get version
 --help          get help
 -editor         scenario-based collection identifier, parameter configuration items can be added later
 responseTime   get the page response delay after an application is operated
 completeTime   get the page completion delay after an application is operated
 fpsohtest      used by the vilidator to obtain the fps
example1:
SP\_daemon -N 20 -c -g -t -p -r -net -snapshot -d
SP\_daemon -N 20 -PKG ohos.samples.ecg -c -g -t -p -f -r -net -snapshot -d -nav -gc
SP\_daemon -start -c
SP\_daemon -stop
example2: These parameters need to be used separately
SP\_daemon -screen
SP\_daemon -deviceinfo
SP\_daemon -server
SP\_daemon -clear
SP\_daemon -ohtestfps 10
SP\_daemon -editorServer
SP\_daemon -recordcapacity
example3: These parameters need to be used separately
SP\_daemon -editor responseTime ohos.samples.ecg app name
SP\_daemon -editor completeTime ohos.samples.ecg app name
SP\_daemon -editor fpsohtest

command exec finished!
$

## Basic Data Collection

This feature collects GPU, FPS, CPU, DDR, and memory metrics for the entire device or specific applications. It supports the following operations:

1.  Per-second sampling

| 
Parameter

 | 

Mandatory

 | 

Description

 |
| :-- | :-- | :-- |
| 

\-N

 | 

Yes

 | 

Sets the number of collection times (once per second).

 |
| 

\-PKG

 | 

No

 | 

Sets the bundle name.

 |
| 

\-PID

 | 

No

 | 

Sets the process ID or thread ID.

 |
| 

\-threads

 | 

No

 | 

Collects the number of child threads of an application.

 |
| 

\-c

 | 

No

 | 

Collects the CPU frequency and usage.

When the application bundle name is set, the system and application CPU information is collected.

Otherwise, only the system CPU information is collected.

 |
| 

\-g

 | 

No

 | 

Collects the GPU frequency and load information.

 |
| 

\-gc

 | 

No

 | 

Collects GPU internal counter information.

 |
| 

\-f

 | 

No

 | 

Collects the screen refresh rate and frame rate of the target application. The application bundle name must be specified. This parameter automatically collects game layers in a game application.

 |
| 

\-t

 | 

No

 | 

Collects the temperature of GPU and system chip.

 |
| 

\-p

 | 

No

 | 

Collects current and voltage information.

 |
| 

\-ci

 | 

No

 | 

Collects the number of CPU instructions.

When the application bundle name is set, the number of CPU instructions of the system and application is collected.

Otherwise, the number of CPU instructions of the system is collected.

 |
| 

\-r

 | 

No

 | 

Collects the memory information.

When the application bundle name is set, the system and application memory information is collected.

Otherwise, only the system memory information is obtained.

 |
| 

\-snapshot

 | 

No

 | 

Takes screenshots.

 |
| 

\-nav

 | 

No

 | 

Switch between pages.

 |
| 

\-net

 | 

No

 | 

Collects the network speed.

 |
| 

\-VIEW

 | 

No

 | 

Sets the view layer. You must obtain the layer name first.

 |
| 

\-d

 | 

No

 | 

Collects the DDR data.

 |
| 

\-sections

 | 

No

 | 

Sets segment-based collection.

 |
| 

\-nav

 | 

No

 | 

Collects the page navigation information. The application bundle name must be specified.

 |

-   Collect the number of application threads once based on the bundle name.

$ SP\_daemon -N 1 -PKG ohos.samples.ecg -threads
 
 
 
order:0 timestamp=1741415592481
order:1 threadsNum=18847:113|
order:2 tids=18847:43411 43409 43350 43236 25783 25622 25384 25381 19423 19170 19167 19166 19165 19163 19162 19159 19157 19156 19154 19153 19152 19151 19150 19149 19147 19146 19145 19142 19141 19140 19139 19136 19135 19134 19120 19112 19111 19088 19083 19081 19077 19076 19075 19074 19073 19072 19071 19070 19055 19044 19040 19039 19034 19033 19032 19031 19030 19029 19028 19027 19019 19017 19016 19015 19014 19013 19012 19011 19009 19007 19006 19005 19004 19003 19001 19000 18999 18998 18997 18996 18995 18994 18993 18992 18991 18990 18989 18988 18987 18986 18985 18984 18983 18982 18981 18980 18977 18974 18946 18942 18936 18934 18933 18931 18930 18929 18928 18927 18926 18925 18924 18923 18847|
 
command exec finished!
$

-   Collect the frequency and usage of CPU cores twice.

$ SP\_daemon -N 2 -c

order:0 timestamp=1739348046398
order:1 TotalcpuUsage=7.072368
order:2 TotalcpuidleUsage=92.927632
order:3 TotalcpuioWaitUsage=0.082237
order:4 TotalcpuirqUsage=0.246711
order:5 TotalcpuniceUsage=0.000000
order:6 TotalcpusoftIrqUsage=0.000000
order:7 TotalcpusystemUsage=3.125000
order:8 TotalcpuuserUsage=3.618421
order:9 cpu0Frequency=550000
order:10 cpu0Usage=16.666667
order:11 cpu0idleUsage=83.333333
order:12 cpu0ioWaitUsage=0.000000
order:13 cpu0irqUsage=2.941176
order:14 cpu0niceUsage=0.000000
order:15 cpu0softIrqUsage=0.000000
order:16 cpu0systemUsage=5.882353
order:17 cpu0userUsage=7.843137
order:18 cpu1Frequency=550000
...
command exec finished!
$

-   Collect the frequency and usage of CPU cores and CPU usage and load of processes twice based on the bundle name.

$ SP\_daemon -N 2 -PKG ohos.samples.ecg -c
 
 
 
order:0 timestamp=1741415021814
order:1 ChildProcCpuLoad=NA
order:2 ChildProcCpuUsage=NA
order:3 ChildProcId=NA
order:4 ChildProcSCpuUsage=NA
order:5 ChildProcUCpuUsage=NA
order:6 ProcAppName=ohos.samples.ecg
order:7 ProcCpuLoad=2.742330
order:8 ProcCpuUsage=7.825508
order:9 ProcId=18847
order:10 ProcSCpuUsage=2.014652
order:11 ProcUCpuUsage=5.810856
order:12 TotalcpuUsage=22.527016
order:13 TotalcpuidleUsage=77.472984
order:14 TotalcpuioWaitUsage=0.000000
order:15 TotalcpuirqUsage=0.083126
order:16 TotalcpuniceUsage=0.000000
order:17 TotalcpusoftIrqUsage=0.000000
order:18 TotalcpusystemUsage=7.148795
order:19 TotalcpuuserUsage=15.295096
order:20 cpu0Frequency=1430000
order:21 cpu0Usage=52.475248
order:22 cpu0idleUsage=47.524752
order:23 cpu0ioWaitUsage=0.000000
order:24 cpu0irqUsage=0.000000
...
command exec finished!
$

-   Collect the frequency and usage of CPU cores and CPU usage and load of processes twice based on the process ID.

$ SP\_daemon -N 2 -PID 18847 -c
 
 
 
order:0 timestamp=1741415133211
order:1 ChildProcCpuLoad=NA
order:2 ChildProcCpuUsage=NA
order:3 ChildProcId=NA
order:4 ChildProcSCpuUsage=NA
order:5 ChildProcUCpuUsage=NA
order:6 ProcAppName=ohos.samples.ecg
order:7 ProcCpuLoad=2.510634
order:8 ProcCpuUsage=7.005678
order:9 ProcId=18847
order:10 ProcSCpuUsage=2.697061
order:11 ProcUCpuUsage=4.308617
order:12 TotalcpuUsage=24.979114
order:13 TotalcpuidleUsage=75.020886
order:14 TotalcpuioWaitUsage=0.000000
order:15 TotalcpuirqUsage=0.083542
order:16 TotalcpuniceUsage=0.000000
order:17 TotalcpusoftIrqUsage=0.000000
order:18 TotalcpusystemUsage=8.270677
order:19 TotalcpuuserUsage=16.624896
order:20 cpu0Frequency=1430000
order:21 cpu0Usage=50.000000
order:22 cpu0idleUsage=50.000000
order:23 cpu0ioWaitUsage=0.000000
order:24 cpu0irqUsage=0.000000
...
command exec finished!
$

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/24/v3/v4hH4J-VRO-d359OiU9jyw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062031Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=E013C971F55424B83E9CC80621431B874E5AFB45C40B0F2E7C1C2538D74DED12)

-   Make sure you are on the application screen when running this command.

-   Collect the GPU frequency and load of the system once.

$ SP\_daemon -N 1 -g

order:0 timestamp=1705041456507
order:1 gpuFrequency=279000000
order:2 gpuLoad=12.000000

command exec finished!
$

-   Sets the package name and collects the GPU counter information of the five-time instruction application.

$ SP\_daemon -N 5 -PKG ohos.samples.ecg -gc

order:0 timestamp=1755677556978

order:0 timestamp=1755677557984

order:0 gpuCounterData=0\_0\_0\_0\_0\_0\_0\_0\_0\_0\_0\_0;
order:1 timestamp=1755677559018

order:0 timestamp=1755677560021

order:0 gpuCounterData=60164342\_2191\_14546\_42778\_47074251\_370837730\_318640345\_9\_3\_40\_0\_21;
order:1 timestamp=1755677561024
command exec finished!
$

-   Collect the system temperature twice.

$ SP\_daemon -N 2 -t

order:0 Battery=30.000000
order:1 cluster0=34.000000
order:2 gpu=34.000000
order:3 npu\_thermal=35.000000
order:4 shell\_back=32.445000
order:5 shell\_frame=31.445000
order:6 shell\_front=31.438000
order:7 soc\_thermal=41.933000
order:8 system\_h=32.250000
order:9 timestamp=1749275671938

order:0 Battery=30.000000
order:1 cluster0=34.000000
order:2 gpu=34.000000
order:3 npu\_thermal=35.000000
order:4 shell\_back=32.445000
order:5 shell\_frame=31.445000
order:6 shell\_front=31.438000
order:7 soc\_thermal=41.742000
order:8 system\_h=32.200000
order:9 timestamp=1749275673941

command exec finished!
$

-   Collect the current and voltage of the system once.

$ SP\_daemon -N 1 -p

order:0 timestamp=1705041491090
order:1 currentNow=-255
order:2 voltageNow=4377614

command exec finished!
$

-   Collect the number of CPU instructions of the system once.

$ SP\_daemon -N 1 -ci

order:0 hw-cpu-cycles=2168073451.00000
order:1 hw-instructions=833680950.00000
order:2 timestamp=1705041491090
command exec finished!
$

-   Collect the number of CPU instructions of the system and a specified application once.

$ SP\_daemon -N 1 -PKG ohos.samples.ecg -ci

order:0 hw-cpu-cycles=2168073451.000000
order:1 hw-instructions=833680950.000000
order:2 timestamp=1746835992826
command exec finished!
$

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/40/v3/YRuImTueS5yk6QVnRlTCeQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062031Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=D4A7DD42CE6A69FDEDC784FD2D6F496FA8938C20C0E5133938AFB2E88CBD5406)

-   Make sure you are on the application screen when running this command.

-   Collect the memory information of the system twice.

$ SP\_daemon -N 2 -r
order:0 timestamp=1705041562521
order:1 memAvailable=7339224
order:2 memFree=7164708
order:3 memTotal=11641840

order:0 timestamp=1705041563527
order:1 memAvailable=7339136
order:2 memFree=7164684
order:3 memTotal=11641840

command exec finished!
$

-   Collect the memory of the system and specified application process once based on the bundle name.

$ SP\_daemon -N 1 -PKG ohos.samples.ecg -r
 
 
 
order:0 timestamp=1741415257059
order:1 arktsHeapPss=44835
order:2 childCarktsHeapPss=NA
order:3 childGpuPss=NA
order:4 childGraphicPss=NA
order:5 childHeapAlloc=NA
order:6 childHeapFree=NA
order:7 childHeapSize=NA
order:8 childNativeHeapPss=NA
order:9 childPrivateClean=NA
order:10 childPrivateDirty=NA
order:11 childPss=NA
order:12 childSharedClean=NA
order:13 childSharedDirty=NA
order:14 childStackPss=NA
order:15 childSwap=NA
order:16 childSwapPss=NA
order:17 gpuPss=222377
order:18 graphicPss=184276
order:19 heapAlloc=154696
order:20 heapFree=780
order:21 heapSize=163208
order:22 memAvailable=4612096
order:23 memFree=1240924
order:24 memTotal=11692696
order:25 nativeHeapPss=85290
order:26 privateClean=195816
order:27 privateDirty=418973
order:28 pss=693349
order:29 sharedClean=146848
order:30 sharedDirty=71056
order:31 stackPss=2492
order:32 swap=25360
order:33 swapPss=25356

command exec finished!
$

-   Collect the memory of the system and specified application process once based on the process ID.

$ SP\_daemon -N 1 -PID 18847 -r
 
 
 
order:0 timestamp=1741415293198
order:1 arktsHeapPss=45011
order:2 childCarktsHeapPss=NA
order:3 childGpuPss=NA
order:4 childGraphicPss=NA
order:5 childHeapAlloc=NA
order:6 childHeapFree=NA
order:7 childHeapSize=NA
order:8 childNativeHeapPss=NA
order:9 childPrivateClean=NA
order:10 childPrivateDirty=NA
order:11 childPss=NA
order:12 childSharedClean=NA
order:13 childSharedDirty=NA
order:14 childStackPss=NA
order:15 childSwap=NA
order:16 childSwapPss=NA
order:17 gpuPss=222381
order:18 graphicPss=184276
order:19 heapAlloc=154588
order:20 heapFree=757
order:21 heapSize=163184
order:22 memAvailable=4612096
order:23 memFree=1238420
order:24 memTotal=11692696
order:25 nativeHeapPss=85274
order:26 privateClean=195996
order:27 privateDirty=418977
order:28 pss=693440
order:29 sharedClean=146848
order:30 sharedDirty=71056
order:31 stackPss=2492
order:32 swap=25360
order:33 swapPss=25356

command exec finished!
$

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5f/v3/UU3ogaKISFiXsiEwAE5B7g/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062031Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=6CF903A6F3F8C9CC243E8F6EB7115CDCFCB80D8299A8C5A565872E56B20DBF6B)

-   Make sure you are on the application screen when running this command.

-   Take two screenshots.

$ SP\_daemon -N 2 -snapshot

order:0 timestamp=1739349178766
order:1 capture=data/local/tmp/capture/screenCap\_1739349178766.png

order:0 timestamp=1739349179769
order:1 capture=NA

command exec finished!
$

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f3/v3/6ECkyVhrQ1OJgU3dUsTBRA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062031Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=49731445FBA6A8A45031C682962B06F2BC009181BE68D4BE0A209F84F47F073F)

-   Screenshots are captured every 2 seconds.
    
-   The screenshot report is stored in **data/local/tmp/capture**.
    
-   When the collection is complete, you can view the screenshots in **data/local/tmp/capture**.
    
-   Run the **hdc file recv data/local/tmp/capture/screenCap\_1700725192774.png D:\\** to export the screenshot.
    

-   Collect the network speeds twice.

$ SP\_daemon -N 2 -net

order:0 timestamp=1739349429109
order:1 networkDown=580407
order:2 networkUp=58978

order:0 timestamp=1739349430113
order:1 networkDown=25212
order:2 networkUp=594

command exec finished!
$

-   Collect the frame rate of a specified application five times based on the bundle name.

$ SP\_daemon -N 5 -PKG ohos.samples.ecg -f

order:0 timestamp=1705306472232
order:1 fps=43
order:2 fpsJitters=602261688;;8352083;;8267708;;8305209;;8298437;;8308854;;8313542;;8569271;;8061458;;8300521;;8308333;;8309896;;8429167;;8241667;;8258333;;8318229;;8312500;;8304167;;41760937;;16418750;;8298959;;8319270;;8308334;;8313541;;8302605;;8320312;;8298958;;8326042;;8321354;;8301042;;8310417;;8309895;;8308855;;8331250;;8286458;;8343229;;8278125;;8311458;;8306250;;8312500;;8320834;;8346875;;8283333
order:3 refreshrate=120

order:0 timestamp=1705306473234
order:1 fps=40
order:2 fpsJitters=674427313;;8191145;;8310417;;8319271;;8301562;;8318750;;8302084;;8314062;;8333334;;8283854;;8307812;;8311979;;8310417;;8307813;;8309375;;8323958;;8306250;;8308333;;8317709;;8296875;;8721875;;7895833;;8320833;;8340625;;8276563;;8409896;;8216145;;8310938;;8301042;;8362500;;8252604;;8317708;;8376042;;8256250;;8292187;;8303125;;8313542;;8310417;;8520312
order:3 refreshrate=120
...

command exec finished!
$

-   Collect the frame rate of a specified application five times based on the process ID.

$ SP\_daemon -N 5 -PID 18847 -f
 
 
 
order:0 timestamp=1741415862598
order:1 fps=28
order:2 fpsJitters=50192708;;16733855;;33466145;;33460938;;33468229;;33503125;;50156250;;16731250;;33458854;;33460417;;33462500;;33466667;;33461458;;33622396;;33307291;;50336980;;33302083;;16733854;;33464062;;33456771;;33467188;;50186979;;16728646;;33458854;;16736458;;33461459;;33448958;;33464062
order:3 refreshrate=60
...

command exec finished!
$

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e6/v3/OZFJciYYS364PJ94eNkjaw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062031Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=1DE84F4B7A26506AF6A2DA156E38EEC083155345CF3C73BC174EFBA079C30244)

-   When running this command, make sure you are on the application screen, and then swipe on the screen or switch between screens.
-   When dynamic refresh rate (DRR) is enabled, the refresh rate changes in real time (multiple changes may occur within one second). The value of **refreshrate** is obtained at a timestamp.

-   Collect the frame rate of the specified view layer 10 times.

$ SP\_daemon -N 10 -VIEW DisplayNode -f
order:0 timestamp=1705306822850
order:1 fps=15
order:2 fpsJitters=876291843;;8314062;;8308334;;8314583;;8310417;;8308333;;8326042;;8314583;;8292708;;8492709;;8143750;;8340104;;8294271;;8302604;;8297396
order:3 refreshrate=120
 
order:0 timestamp=1705306823852
order:1 fps=12
order:2 fpsJitters=906667363;;8279167;;8311458;;8315625;;8291146;;8313021;;8323438;;8293750;;8303125;;8313541;;8301563;;8317708
order:3 refreshrate=120
...

command exec finished!
$

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/eb/v3/mGmTuO7QRhC88GrlCCehBA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062031Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=E9108CC616916C9FD421AB2C0A2A5FF6FFBAC2DB55E83F42A80C3212D75EB999)

-   **DisplayNode** indicates the name of the specified layer.
    
-   When using this command to collect data, you need to operate the page on the specified layer.
    
-   This command cannot be used together with the commands used to collect frame rate of a specified application, such as the **SP\_daemon -N 20 -PKG ohos.samples.ecg -f** or **SP\_daemon -N 20 -VIEW DisplayNode -f** command.
    

-   Collect DDR information once.

$ SP\_daemon -N 1 -d

order:0 timestamp=1739349607442
order:1 ddrFrequency=418000000

command exec finished!
$

-   Collect page navigation information once.

$ SP\_daemon -N 1 -PKG ohos.samples.ecg -nav

order:0 timestamp=1719993861090
order:1 navPathName=about\_device   // Name of the page to be navigated to.

command exec finished!
$

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c2/v3/ILqsD_fXQhyuVr4s8dUieg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062031Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=559A34E7BEB41EC77AD0EB214E46A99BE0070BB8A05B05311BC85F59476CC163)

-   Make sure you are on the application screen when running this command.
    
-   The value of **navPathName** is the name of the page to be navigated to. For details, see the example of **this.pageStack.pushPath** for the normal navigation type in [Page Navigation](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V5/arkts-navigation-navigation-V5#页面跳转). If the page navigation is not implemented using the **Navigation** component, the message "No Navigation Info" is returned.

-   Collect the full information of the system 10 times, including the CPU, GPU, temperature, current, voltage, memory, DDR, network speed, and screenshot information.

$ SP\_daemon -N 10 -c -g -t -p -r -d -net -snapshot

order:0 timestamp=1739349730897
order:1 TotalcpuUsage=34.808013
order:2 TotalcpuidleUsage=65.191987
order:3 TotalcpuioWaitUsage=0.166945
order:4 TotalcpuirqUsage=0.083472
order:5 TotalcpuniceUsage=0.083472
order:6 TotalcpusoftIrqUsage=0.000000
order:7 TotalcpusystemUsage=11.936561
order:8 TotalcpuuserUsage=22.537563
order:9 cpu0Frequency=864000
...
order:115 cpu11systemUsage=1.000000
order:116 cpu11userUsage=1.000000
order:117 gpuFrequency=371000000
order:118 gpuLoad=0.000000
order:119 Battery=34.000000
order:120 cluster0=51.000000
order:121 gpu=47.000000
order:122 npu\_thermal=35.000000
order:123 shell\_back=35.870000
order:124 shell\_frame=34.870000
order:125 shell\_front=34.524000
order:126 soc\_thermal=59.114000
order:127 system\_h=36.777000
order:128 memAvailable=3608576
order:129 memFree=753520
order:130 memTotal=11697880
order:131 ddrFrequency=1531000000
order:132 networkDown=1344
order:133 networkUp=54
order:134 capture=data/local/tmp/capture/screenCap\_1739349730947.png
...

command exec finished!
$

-   Collect the information about a specified application 10 times based on the bundle name, including the CPU, GPU, temperature, current, voltage, frame rate, memory, DDR, network rate, screenshot, GPU internal counter, and navigation information.

$ SP\_daemon -N 10 -PKG ohos.samples.ecg -c -g -t -f -r -d -net -snapshot -threads -gc -nav
order:0 Battery=40.000000
order:1 ChildProcCpuLoad=NA
order:2 ChildProcCpuUsage=NA
order:3 ChildProcId=NA
order:4 ChildProcSCpuUsage=NA
order:5 ChildProcUCpuUsage=NA
order:6 ProcAppName=ohos.samples.ecg
order:7 ProcCpuLoad=4.528385
order:8 ProcCpuUsage=3.793903
order:9 ProcId=48875
order:10 ProcSCpuUsage=0.082836
order:11 ProcUCpuUsage=3.711067
order:12 TotalcpuUsage=39.602320
order:13 TotalcpuidleUsage=60.397680
order:14 TotalcpuioWaitUsage=0.248550
order:15 TotalcpuirqUsage=0.248550
order:16 TotalcpuniceUsage=0.000000
order:17 TotalcpusoftIrqUsage=0.000000
order:18 TotalcpusystemUsage=16.735708
order:19 TotalcpuuserUsage=22.369511
order:20 arktsHeapPss=48113
order:21 capture=data/local/tmp/capture/screenCap\_1755656583554.png
...
order:149 ddrFrequency=1531000000
order:150 fps=101
order:151 fpsJitters=66921354;;8493229;;8217188;;8368229;;8495833;;8293750;;8401042;;8276042;;8522395;;8269792;;8326042;;8312500;;8410937;;8453125;;8267709;;8354166;;8361979;;8417709;;8325000;;8405208;;8607292;;8116146;;8619791;;8127604;;8320834;;8407291;;8361459;;8384375;;8294271;;8403645;;8388021;;8357813;;8334375;;8365625;;8380208;;8360417;;8388541;;8376563;;8332292;;8373958;;8352083;;8380729;;8312500;;8394792;;8386458;;8554688;;11023958;;11156771;;11161979;;11124479;;11137500;;11094271;;11269792;;11041667;;11129166;;11140625;;11152084;;11216666;;11247396;;41751042;;8261979;;8399479;;8368229;;8423438;;8289583;;8349479;;8417188;;8419791;;8786980;;8078645;;8131250;;16768230;;8409895;;8306250;;8396355;;8331770;;8329688;;8445312;;8392709;;11126562;;11125521;;11171875;;11208333;;8290105;;8383854;;8339583;;8347396;;8378125;;8496875;;11046875;;11225000;;8276042;;8409895;;8310938;;8371875;;8364062;;8377084;;8323958;;8344792;;8418750
order:152 gpu=53.000000
order:153 gpuCounterData=124860003\_5344\_34432\_101603\_71533935\_725473415\_593611542\_20\_13\_88\_0\_41;
order:154 gpuFrequency=279000000
order:155 gpuLoad=27.000000
order:156 gpuPss=8368
order:157 graphicPss=252
order:158 heapAlloc=81244
order:159 heapFree=860
order:160 heapSize=91492
order:161 memAvailable=3858432
order:162 memFree=1429020
order:163 memTotal=11677756
order:164 nativeHeapPss=56952
order:165 navPathName=No Navigation Info
order:166 networkDown=0
order:167 networkUp=0
order:168 npu\_thermal=52.000000
order:169 privateClean=115064
order:170 privateDirty=11684
order:171 pss=163746
order:172 refreshrate=90
order:173 sharedClean=159052
order:174 sharedDirty=24664
order:175 shell\_back=41.871000
order:176 shell\_frame=40.871000
order:177 shell\_front=40.549000
order:178 soc\_thermal=63.358000
order:179 stackPss=536
order:180 swap=16144
order:181 swapPss=16144
order:182 system\_h=42.764000
order:183 threadsNum=48875:50
order:184 tids=48875:51429 51319 51318 51317 51316 51289 51279 51278 51273 51272 51271 51266 51265 51260 51259 51258 51051 51048 50003 50002 50001 49999 49662 49074 49073 49065 49064 49063 49056 49055 49052 49051 48973 48965 48950 48949 48944 48943 48941 48940 48939 48938 48937 48936 48934 48933 48932 48931 48930 48875
order:185 timestamp=1755656584533
command exec finished!
$

-   Collect the information about a specified application 10 times based on the process ID, including the CPU, GPU, temperature, current, voltage, frame rate, memory, DDR, network rate, screenshot, and navigation information.

$ SP\_daemon -N 10 -PID 18847 -c -g -t -p -f -r -d -net -snapshot -nav -threads

order:0 timestamp=1741416084766
order:1 ChildProcCpuLoad=NA
order:2 ChildProcCpuUsage=NA
order:3 ChildProcId=NA
order:4 ChildProcSCpuUsage=NA
order:5 ChildProcUCpuUsage=NA
order:6 ProcAppName=ohos.samples.ecg
order:7 ProcCpuLoad=2.857003
order:8 ProcCpuUsage=5.932203
order:9 ProcId=18847
order:10 ProcSCpuUsage=1.765537
order:11 ProcUCpuUsage=4.166667
order:12 TotalcpuUsage=28.442728
order:13 TotalcpuidleUsage=71.557272
order:14 TotalcpuioWaitUsage=0.000000
order:15 TotalcpuirqUsage=0.000000
order:16 TotalcpuniceUsage=0.000000
order:17 TotalcpusoftIrqUsage=0.000000
order:18 TotalcpusystemUsage=9.716860
order:19 TotalcpuuserUsage=18.725869
...
order:123 gpuFrequency=279000000
order:124 gpuLoad=0.000000
order:125 Battery=35.000000
order:126 cluster0=51.000000
order:127 gpu=47.000000
order:128 npu\_thermal=35.000000
order:129 shell\_back=36.627000
order:130 shell\_frame=35.627000
order:131 shell\_front=35.652000
order:132 soc\_thermal=59.259000
order:133 system\_h=37.000000
order:134 currentNow=-171
order:135 voltageNow=4190706
order:136 fps=30
order:137 fpsJitters=33501562;;50251042;;33522396;;16743750;;33482812;;33505730;;33507291;;33505209;;33502604;;50258854;;33518229;;33501563;;16753125;;50247916;;16751563;;33507812;;16740104;;16792188;;33464583;;33497917;;50261458;;33493750;;33511459;;33502083;;16744271;;16756250;;33505729;;50254687;;33507292;;50286979
order:138 refreshrate=60
order:139 arktsHeapPss=29564
order:140 gpuPss=254647
order:141 graphicPss=215796
order:142 heapAlloc=174032
order:143 heapFree=1232
order:144 heapSize=187924
order:145 memAvailable=3437568
order:146 memFree=780152
order:147 memTotal=11697880
order:148 nativeHeapPss=91244
order:149 privateClean=162560
order:150 privateDirty=488739
order:151 pss=761908
order:152 sharedClean=225060
order:153 sharedDirty=48740
order:154 stackPss=2596
order:155 swap=62024
order:156 swapPss=62024
order:157 ddrFrequency=1531000000
order:158 networkDown=215
order:159 networkUp=0
...
order:180 capture=data/local/tmp/capture/screenCap\_1741416084923.png
order:181 navPathName=No Navigation Info
order:182 threadsNum=18847:113|
order:183 tids=18847:46736 46734 46731 46663 25783 25622 25384 25381 19423 19170 19167 19166 19165 19163 19162 19159 19157 19156 19154 19153 19152 19151 19150 19149 19147 19146 19145 19142 19141 19140 19139 19136 19135 19134 19120 19112 19111 19088 19083 19081 19077 19076 19075 19074 19073 19072 19071 19070 19055 19044 19040 19039 19034 19033 19032 19031 19030 19029 19028 19027 19019 19017 19016 19015 19014 19013 19012 19011 19009 19007 19006 19005 19004 19003 19001 19000 18999 18998 18997 18996 18995 18994 18993 18992 18991 18990 18989 18988 18987 18986 18985 18984 18983 18982 18981 18980 18977 18974 18946 18942 18936 18934 18933 18931 18930 18929 18928 18927 18926 18925 18924 18923 18847|
...

command exec finished!
$

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/67/v3/_TO2YKe5S9iLO0gefM3csA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062031Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=FB994ACA4A540AF4557C678619AD4027B14604FFE8504F6D17B4A570B68A5B5C)

-   Make sure you are on the application screen when running this command.

2\. On-demand start and stop

Run the **start** command to start collection, operate the device or application, and then run the **stop** command to stop collection.

| 
Parameter

 | 

Mandatory

 | 

Description

 |
| :-- | :-- | :-- |
| 

\-start

 | 

Yes

 | 

Starts collection. You can add a basic collection command after this parameter. The collection is performed every second.

 |
| 

\-stop

 | 

Yes

 | 

Stops collection. A report is generated when collection is complete.

 |
| 

\-print

 | 

No

 | 

Prints collection information every second.

 |

**Starting and Stopping Collection**

Start data collection.
$ SP\_daemon -start -c
SP\_daemon Collection begins

command exec finished!
$

Stop data collection.
$ SP\_daemon -stop
SP\_daemon Collection ended
Output Path: data/local/tmp/smartperf/1/t\_index\_info.csv

command exec finished!
$

**Starting and Stopping Collection and Printing Collection Information**

Start data collection and printing.
$ SP\_daemon -start -c -print
SP\_daemon Collection begins

order:0 TotalcpuUsage=20.860927
order:1 TotalcpuidleUsage=79.139073
order:2 TotalcpuioWaitUsage=0.000000
order:3 TotalcpuirqUsage=0.082781
order:4 TotalcpuniceUsage=0.000000
order:5 TotalcpusoftIrqUsage=0.000000
order:6 TotalcpusystemUsage=8.029801
order:7 TotalcpuuserUsage=12.748344
order:8 cpu0Frequency=1430000
order:9 cpu0Usage=44.554455
order:10 cpu0idleUsage=55.445545
order:11 cpu0ioWaitUsage=0.000000
order:12 cpu0irqUsage=0.000000
order:13 cpu0niceUsage=0.000000
order:14 cpu0softIrqUsage=0.000000
order:15 cpu0systemUsage=17.821782
order:16 cpu0userUsage=26.732673
order:17 cpu10Frequency=1239000
order:18 cpu10Usage=0.000000
order:19 cpu10idleUsage=100.000000
order:20 cpu10ioWaitUsage=0.000000
order:21 cpu10irqUsage=0.000000
order:22 cpu10niceUsage=0.000000
order:23 cpu10softIrqUsage=0.000000
order:24 cpu10systemUsage=0.000000
order:25 cpu10userUsage=0.000000
order:26 cpu11Frequency=1239000
order:27 cpu11Usage=0.000000
order:28 cpu11idleUsage=100.000000
order:29 cpu11ioWaitUsage=0.000000
order:30 cpu11irqUsage=0.000000
order:31 cpu11niceUsage=0.000000
order:32 cpu11softIrqUsage=0.000000
order:33 cpu11systemUsage=0.000000
order:34 cpu11userUsage=0.000000
...
command exec finished!
$

Stop collection and printing. (When starting or stopping printing, you need to open the CLI again and run this command.)
$ SP\_daemon -stop
SP\_daemon Collection ended
Output Path: data/local/tmp/smartperf/1/t\_index\_info.csv

command exec finished!
$

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d5/v3/p4NzSUEjRRm2BnnoGvo-BA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062031Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=EDA10F70BFAAA11D35ABC6706334FB1A6FC0C4AEF3EB817A7B2492BB96857697)

-   To start collecting the system data, run the **SP\_daemon -start -c -g -t -r -d -net -snapshot -threads** command.
    
-   To start collecting the system and process data based on the bundle name, run the **SP\_daemon -start -PKG ohos.samples.ecg -c -g -t -f -r -d -net -snapshot -threads** **\-nav** command.
    
-   To start collecting the system and process data based on the process ID, run the **SP\_daemon -start -PID _18847_ -c -g -t -f -r -d -net -snapshot -threads** command.
-   To start collecting and printing the system data, run the **SP\_daemon -start -c -g -t -r -d -net -snapshot -threads -print** command.
-   To start collecting and printing the system and process information based on the process ID, run the **SP\_daemon -start -PID _18847_ -c -g -t -f -r -d -net -snapshot -threads -print** command.
-   The **start** and **stop** commands must be used in pairs. After you start the collection with the **start** command, be sure to stop it with the **stop** command.
-   To stop collection or printing, reopen the CLI and run the **stop** command.
-   After the collection is complete, the collected data is saved in **data/local/tmp/smartperf/1/t\_index\_info.csv**.
-   To export the file, run the **hdc file recv data /local/tmp/smartperf/1/t\_index\_info.csv** command.

3\. CSV output: Writes the collected results to the **data.csv** file for analysis.

To export and view the collected results, follow the instructions in the source document:

-   Run the **\-N** command to enable the collection. The default output path of the collection result is **/data/local/tmp/data.csv**.
-   Check the path to the result file.

C:\\Users\\issusser>hdc shell
$ cd data/local/tmp
$ ls
data.csv
$

-   Export the file.

C:\\Users\\issusser>hdc file recv data/local/tmp/data.csv D:\\
\[I\]\[2023-11-08 16:16:41\] HdcFile::TransferSummary success
FileTransfer finish, Size:429, File count = 1, time:6ms rate:71.50kB/s

C:\\Users\\issusser>

-   Open the **data.csv** file to view data.

The table below describes the data fields in the **data.csv** file.

| 
Data Field

 | 

Description

 | 

Remarks

 |
| :-- | :-- | :-- |
| 

threadsNum

 | 

Total number of threads.

 | 

\-

 |
| 

tids

 | 

Thread ID.

 | 

\-

 |
| 

fdTotal

 | 

Total number of file descriptors.

 | 

\-

 |
| 

cpuFrequency

 | 

CPU core frequency.

 | 

Unit: kHz

 |
| 

cpuUsage

 | 

CPU core usage.

 | 

%

 |
| 

cpuidleUsage

 | 

CPU usage in idle state.

 | 

%

 |
| 

cpuioWaitUsage

 | 

CPU usage of I/O wait.

 | 

%

 |
| 

cpuirqUsage

 | 

CPU usage of hardware interrupts.

 | 

%

 |
| 

cpuniceUsage

 | 

CPU usage of user level processes with lower scheduling priority.

 | 

%

 |
| 

cpusoftIrqUsage

 | 

CPU usage of software interrupts.

 | 

%

 |
| 

cpusystemUsage

 | 

CPU usage in kernel mode.

 | 

%

 |
| 

cpuuserUsage

 | 

CPU usage in user mode.

 | 

%

 |
| 

ProcId

 | 

Process ID.

 | 

\-

 |
| 

ChildProcId

 | 

Child process ID.

 | 

\-

 |
| 

ProcAppName

 | 

Application bundle name.

 | 

\-

 |
| 

ProcCpuLoad

 | 

CPU load of the process.

 | 

%

 |
| 

ChildProcCpuLoad

 | 

CPU load of the child process.

 | 

%

 |
| 

ProcCpuUsage

 | 

CPU usage of the process.

 | 

%

 |
| 

ChildProcCpuUsage

 | 

CPU usage of the child process.

 | 

%

 |
| 

ProcUCpuUsage

 | 

CPU usage of the process in user mode.

 | 

%

 |
| 

ChildProcUCpuUsage

 | 

CPU usage of the child process in user mode.

 | 

%

 |
| 

ProcSCpuUsage

 | 

CPU usage of the process in kernel mode.

 | 

%

 |
| 

ChildProcSCpuUsage

 | 

CPU usage of the child process in kernel mode.

 | 

%

 |
| 

TotalcpuUsage

 | 

Total CPU usage.

 | 

%

 |
| 

TotalcpuidleUsage

 | 

Total CPU usage in idle state.

 | 

%

 |
| 

TotalcpuioWaitUsage

 | 

Total CPU usage of I/O wait.

 | 

%

 |
| 

TotalcpuirqUsage

 | 

Total CPU usage of hard interrupts.

 | 

%

 |
| 

TotalcpuniceUsage

 | 

Total CPU usage of user level processes with lower scheduling priority.

 | 

%

 |
| 

TotalcpusoftIrqUsage

 | 

Total CPU usage of soft interrupts.

 | 

%

 |
| 

TotalcpusystemUsage

 | 

Total CPU usage in kernel mode.

 | 

%

 |
| 

TotalcpuuserUsage

 | 

Total CPU usage in user mode.

 | 

%

 |
| 

gpuFrequency

 | 

GPU frequency of the system.

 | 

Unit: Hz

 |
| 

gpuLoad

 | 

GPU load of the system.

 | 

%

 |
| 

hw-instructions

 | 

Number of executed instructions.

 | 

\-

 |
| 

hw-cpu-cycles

 | 

Number of CPU clock cycles.

 | 

Unit: ns

 |
| 

currentNow

 | 

Current value.

 | 

Unit: mA

 |
| 

voltageNow

 | 

Voltage value.

 | 

Unit: μV

 |
| 

fps

 | 

Frame rate.

 | 

Unit: FPS

 |
| 

fpsJitters

 | 

Frame interval.

 | 

Unit: ns

 |
| 

refreshrate

 | 

Screen refresh rate.

 | 

Unit: Hz

 |
| 

networkDown

 | 

Downstream rate.

 | 

Unit: byte/s

 |
| 

networkUp

 | 

Uplink rate.

 | 

Unit: byte/s

 |
| 

ddrFrequency

 | 

DDR frequency.

 | 

Unit: Hz

 |
| 

shell\_front

 | 

Front cover temperature.

 | 

Unit: °C

 |
| 

shell\_frame

 | 

Frame temperature.

 | 

Unit: °C

 |
| 

shell\_back

 | 

Rear cover temperature.

 | 

Unit: °C

 |
| 

soc\_thermal

 | 

SoC temperature.

 | 

Unit: °C

 |
| 

system\_h

 | 

System temperature.

 | 

Unit: °C

 |
| 

Battery

 | 

Battery temperature.

 | 

Unit: °C

 |
| 

cluster0

 | 

CPU temperature.

 | 

Unit: °C

 |
| 

gpu

 | 

GPU temperature.

 | 

Unit: °C

 |
| 

npu\_thermal

 | 

NPU temperature.

 | 

Unit: °C

 |
| 

memAvailable

 | 

Available memory of the system.

 | 

Unit: KB

 |
| 

memFree

 | 

Free memory of the system.

 | 

Unit: KB

 |
| 

memTotal

 | 

Total memory of the system.

 | 

Unit: KB

 |
| 

pss

 | 

Proportional set size (PSS) of the process.

 | 

Unit: KB

 |
| 

childPss

 | 

Proportional set size (PSS) of the child process.

 | 

Unit: KB

 |
| 

sharedClean

 | 

Shared unwritten pages.

 | 

Unit: KB

 |
| 

childSharedClean

 | 

Shared unwritten pages of the child process.

 | 

Unit: KB

 |
| 

sharedDirty

 | 

Shared rewritten pages.

 | 

Unit: KB

 |
| 

childSharedDirty

 | 

Shared rewritten pages of the child process.

 | 

Unit: KB

 |
| 

privateClean

 | 

Private unwritten pages.

 | 

Unit: KB

 |
| 

childPrivateClean

 | 

Private unwritten pages of the child process.

 | 

Unit: KB

 |
| 

privateDirty

 | 

Private rewritten pages.

 | 

Unit: KB

 |
| 

childPrivateDirty

 | 

Private rewritten pages of the child process.

 | 

Unit: KB

 |
| 

swap

 | 

Total swap memory.

 | 

Unit: KB

 |
| 

childSwap

 | 

Total swap memory of the child process.

 | 

Unit: KB

 |
| 

swapPss

 | 

Swapped PSS.

 | 

Unit: KB

 |
| 

childSwapPss

 | 

Swapped PSS of the child process.

 | 

Unit: KB

 |
| 

HeapSize

 | 

Heap size.

 | 

Unit: KB

 |
| 

childHeapSize

 | 

Heap size of the child process.

 | 

Unit: KB

 |
| 

HeapAlloc

 | 

Heap size that can be allocated.

 | 

Unit: KB

 |
| 

childHeapAlloc

 | 

Heap size that can be allocated of the child process.

 | 

Unit: KB

 |
| 

HeapFree

 | 

Remaining heap size.

 | 

Unit: KB

 |
| 

childHeapFree

 | 

Remaining heap size of the child process.

 | 

Unit: KB

 |
| 

gpuPss

 | 

Used GPU size.

 | 

Unit: KB

 |
| 

childGpuPss

 | 

Used GPU size of the child process.

 | 

Unit: KB

 |
| 

graphicPss

 | 

Used graphics memory size.

 | 

Unit: KB

 |
| 

childGraphicPss

 | 

Used graphics memory size of the child process.

 | 

Unit: KB

 |
| 

arktsHeapPss

 | 

Used ArkTS memory size.

 | 

Unit: KB

 |
| 

childCarktsHeapPss

 | 

Used ArkTS memory size of the child process.

 | 

Unit: KB

 |
| 

nativeHeapPss

 | 

Used native memory size.

 | 

Unit: KB

 |
| 

childNativeHeapPss

 | 

Used native memory size of the child process.

 | 

Unit: KB

 |
| 

stackPss

 | 

Used stack memory size.

 | 

Unit: KB

 |
| 

childStackPss

 | 

Used stack memory size of the child process.

 | 

Unit: KB

 |
| 

navPathName

 | 

Page navigation information.

 | 

\-

 |
| 

timeStamp

 | 

Current timestamp, corresponding to the collection time.

 | 

\-

 |

## Scenario-based Collection

In addition to basic collection, the response and completion delay can be collected. The result is displayed in the CLI instead of being written into the **data.csv** file.

Scenario-based collection is used to assess the performance of an application page during scrolling and switching operations. The corresponding collection commands are executed based on different operation scenarios to obtain the application performance data, including FPS, hitch time rate, response delay, completion delay, and the maximum number of consecutive lost frames. The collected data is printed for you to analyze and optimize the application performance.

| 
Parameter

 | 

Mandatory

 | 

Description

 |
| :-- | :-- | :-- |
| 

\-editor

 | 

Yes

 | 

Scenario-based collection identifier.

 |
| 

timeDelay

 | 

No

 | 

Used in the page switching scenario. Supported ArkUI modules and components: **Router**, **Navigation**, **Tabs**, and **Swiper**.

 |
| 

slideList

 | 

No

 | 

Used in the page scrolling scenario. Supported ArkUI components: **List**, **Grid**, **Scroll**, and **Waterflow**.

 |

| 
Data Field

 | 

Description

 | 

Remarks

 |
| :-- | :-- | :-- |
| 

ResponseTime

 | 

Response delay during page switching and scrolling.

 | 

Unit: ms.

 |
| 

CompleteTime

 | 

Completion delay during page switching.

 | 

Unit: ms.

 |
| 

HitchTimeRate

 | 

Frame freezing rate during page switching and scrolling.

 | 

Unit: ms/s

 |
| 

MAX\_RENDER\_SEQ\_MISSED\_FRAMES

 | 

The maximum number of consecutive lost frames during page switching and scrolling.

 | 

NA

 |
| 

FPS

 | 

Frame rate during page scrolling.

 | 

Unit: FPS

 |

-   **Page Switching**

Step 1: Open the application page to be tested.

Step 2: Run the **SP\_daemon -editor timeDelay** command in the CLI.

Step 3: Wait for 1 to 2 seconds, tap the button on the page to go to the next page, and wait until the test is complete.

After the test is complete, the following information is displayed:

$ SP\_daemon -editor timeDelay
ResponseTime:41ms
CompleteTime:593ms
HitchTimeRate:68.65ms/s
MAX\_RENDER\_SEQ\_MISSED\_FRAMES:3
$

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/64/v3/eKyFWNU2TCWlAMcbOyKvxQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062031Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=D679AC26717660EB2132A0B927E8E60D17B734763B590156EABCD1F0E2659508)

-   The delay calculation is based on the system logging and reporting. The start time is when the tap event is reported. The end time for response delay is when the system responds and displays the first frame after the tap, and the end time for completion delay is when the first frame is displayed after the page switching. They may be different from what end users perceive.
-   Currently, the **HitchTimeRate** parameter is supported only for the following ArkUI modules and components: **Router**, **Navigation**, **Tabs**, and **Swiper**. Calculation formula: **HitchTimeRate** = Accumulated frame loss time of each frame during page switching (ms)/Animation duration (s)
-   The value of the **MAX\_RENDER\_SEQ\_MISSED\_FRAMES** parameter is subject to the system logging and reporting and may be different from what end users perceive.

-   The trace data collected during page switching is saved in the **data/local/tmp/sp\_trace\_delay.ftrace** path. You can export it by running the **hdc file recv** command.

-   **Page Scrolling**

Step 1: Open the application page to be tested.

Step 2: Run the **SP\_daemon -editor slideList** command in the CLI.

Step 3: Wait for 1 to 2 seconds, scroll the page, and wait until the test is complete.

After the test is complete, the following information is displayed:

$ SP\_daemon -editor slideList
FPS:107.181fps
ResponseTime:20ms
HitchTimeRate:1.49ms/s
MAX\_RENDER\_SEQ\_MISSED\_FRAMES:0
$

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/80/v3/baT4hX5MQTqG-Fa4Jv7aIg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062031Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=3FE5E88251B29578E1049815FDF59E33B7F142A1E460F64560CC7A5A0618E3F3)

-   The delay calculation is based on the system logging and reporting. The start time is when the tap event is reported. The end time for response delay is when the first frame is displayed after the page scrolling and may be different from what end users perceive. Note that the delay calculation during page scrolling does not support the **Web** component.
-   **FPS** indicates the frame rate during page scrolling. Note that only one scroll per page is counted for this parameter.
-   Currently, the **HitchTimeRate** parameter is supported only for the following ArkUI components: **List**, **Grid**, **Scroll**, and **Waterflow**. Calculation formula: **HitchTimeRate** = Accumulated frame loss time of each frame during page scrolling (ms)/Animation duration (s)
-   The value of the **MAX\_RENDER\_SEQ\_MISSED\_FRAMES** parameter is subject to the system logging and reporting and may be different from what end users perceive.

-   The trace data collected during page scrolling is saved in the **data/local/tmp/sp\_trace\_fps.ftrace** path. You can export it by running the **hdc file recv** command.

## Other Collection

The power collection result of the current device can be written into the **data.csv** file. Other data is collected separately and the collection result is displayed only in the command box.

| 
Data Field

 | 

Description

 | 

Remarks

 |
| :-- | :-- | :-- |
| 

\-screen

 | 

No

 | 

Collects the screen resolution and refresh rate.

 |
| 

\-deviceinfo

 | 

No

 | 

Obtains the device information.

 |
| 

\-server

 | 

No

 | 

Starts a daemon process by starting or stopping the collection.

 |
| 

\-clear

 | 

No

 | 

Clears all the SP\_daemon processes.

 |
| 

\-profilerfps

 | 

No

 | 

Collects the frame rate of the current page.

 |
| 

\-recordcapacity

 | 

No

 | 

Obtains the battery level of the current device.

 |

-   Obtain the screen resolution.

$ SP\_daemon -screen
activeMode: 1260x2720, refreshrate=60

command exec finished!
$

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9f/v3/LwrRx_m6TSqn64k6vYaLVg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062031Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=E1CBC6F682C4D11EE670885CE6E173EA5DA927F8F68F0CF88FDEF5F2E66E9DB5)

-   **activeMode** indicates the current screen resolution, and **refreshrate** indicates the screen refresh rate.

-   Obtain the device information.

$ SP\_daemon -deviceinfo
abilist: default
activeMode: 1260x2720
board: default
brand: default
cpu\_c1\_cluster: 0 1 2 3
cpu\_c1\_max: 1530000
cpu\_c1\_min: 418000
cpu\_c2\_cluster: 4 5 6 7 8 9
cpu\_c2\_max: 2150000
cpu\_c2\_min: 418000
cpu\_c3\_cluster: 10 11
cpu\_c3\_max: 2620000
cpu\_c3\_min: 1239000
cpu\_cluster\_name: policy0 policy1 policy2
daemonPerfVersion: 1.0.5
deviceTypeName: default
fullname: OpenHarmony-5.1.0.50
gpu\_max\_freq: 750000000
gpu\_min\_freq: 279000000
model: ohos
name: default
sn: default
version: default

command exec finished!
$

-   Start a process to listen for the socket messages of the **start** and **stop** commands.

$ SP\_daemon -server
$
$ pidof SP\_daemon
 7024
$

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f1/v3/71xXesXcShu_PGac-g8KXQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062031Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=2C1F4FC47885DBF898C53FBC2277ED442D1082C1C363CA8555ABADA2AA238683)

-   You can run the **pidof SP\_daemon** command to view the process ID.

-   Clear the SP\_daemon process ID.

$ pidof SP\_daemon
 9923 11402   
$ SP\_daemon -clear
$
$ pidof SP\_daemon
$

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/dc/v3/00Vm0oOdQWShYNJG9B3NGg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062031Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=0424536F2CCECEFA7A4015C7CF050D6759BC0F4ECB5F05561CA3230027F752FB)

-   You can run the **pidof SP\_daemon** command to view the process ID.

-   Collect the frame rate of the current page.

$ SP\_daemon -profilerfps 10
set num:10 success
fps:31|1739353731123
fps:30|1739353732123
fps:58|1739353733123
fps:24|1739353734123
fps:19|1739353735123
fps:19|1739353736123
fps:55|1739353737123
fps:26|1739353738123
fps:21|1739353739123
fps:19|1739353740123
SP\_daemon exec finished!
$

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9e/v3/8FoyVDM7Q6-w46GblUNYIw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062031Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=CF45EBFD53DE100A3DAD74F37DF7C6B181EDF42859BD530423656EDCF120AC03)

-   In this command, **10** indicates the number of collection times (collection is performed every second). You can set it to a positive integer.

-   Collect the frame rate of the current page (by segment).

$ SP\_daemon -profilerfps 100 -sections 10
set num:100 success
fps:33|1739353780123
sectionsFps:15|1739353780123
sectionsFps:60|1739353780223
sectionsFps:15|1739353780323
sectionsFps:60|1739353780423
sectionsFps:15|1739353780523
sectionsFps:15|1739353780623
sectionsFps:24|1739353780723
sectionsFps:60|1739353780823
sectionsFps:60|1739353780923
sectionsFps:60|1739353781023
fps:49|1739353781123
sectionsFps:60|1739353781123
sectionsFps:60|1739353781223
sectionsFps:60|1739353781323
sectionsFps:60|1739353781423
sectionsFps:60|1739353781523
sectionsFps:60|1739353781623
623
sectionsFps:15|1739353798723
sectionsFps:15|1739353798823
sectionsFps:10|1739353798923
sectionsFps:60|1739353799023
fps:20|1739353799123
sectionsFps:60|1739353799123
...
SP\_daemon exec finished!
$

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/51/v3/xekP3V0PQgqfuWZn_qWqxg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062031Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=4DF49677992C7645F2270B46DF96D2D72914D77BD349B1D33585DBA1CDD92190)

-   In this command, **100** indicates the number of collection times (collection is performed every second). You can set it to a positive integer.
-   **10** indicates the number of collection segments, which can be set to a positive integer ranging from 1 to 10.

-   Obtain the battery level.

$ SP\_daemon -recordcapacity
recordTime: 1726903063
recordPower: 5502

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fc/v3/V93gRNktSWCVMIIG3aEV7g/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062031Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=23A137A6D16201F60AAF6B3A605B45690F01520F68A602225367795B51371FC1)

-   **recordTime** indicates the timestamp, and **recordPower** indicates the current battery level.
-   The collection result is written to **/data/local/tmp/powerLeftRecord.csv**.
-   Run the **hdc file recv data/local/tmp/powerLeftRecord.csv D:\\** command to export the file.
