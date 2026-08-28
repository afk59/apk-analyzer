# hiappevent\_event.h

#### Overview

Defines the names of all predefined events. In addition to custom events associated with specific applications, you can use predefined events for logging.

**File to include**: <hiappevent/hiappevent\_event.h>

**Library**: libhiappevent\_ndk.z.so

**System capability**: SystemCapability.HiviewDFX.HiAppEvent

**Since**: 8

**Related module**: [HiAppEvent](../../modules/hiappevent/document.md)

#### Summary

#### \[h2\]Macros

| Name | Description |
| :-- | :-- |
| [EVENT\_USER\_LOGIN](#event_user_login) "hiappevent.user\_login" | 
User login event.

**Since**: 8

 |
| [EVENT\_USER\_LOGOUT](#event_user_logout) "hiappevent.user\_logout" | 

User logout event.

**Since**: 8

 |
| [EVENT\_DISTRIBUTED\_SERVICE\_START](#event_distributed_service_start) "hiappevent.distributed\_service\_start" | 

Distributed service event.

**Since**: 8

 |
| [EVENT\_APP\_CRASH](#event_app_crash) "APP\_CRASH" | 

Crash event.

**Since**: 12

 |
| [EVENT\_APP\_FREEZE](#event_app_freeze) "APP\_FREEZE" | 

Application freeze event.

**Since**: 12

 |
| [EVENT\_APP\_LAUNCH](#event_app_launch) "APP\_LAUNCH" | 

Time-consuming launch event.

**Since**: 12

 |
| [EVENT\_SCROLL\_JANK](#event_scroll_jank) "SCROLL\_JANK" | 

Scrolling frame loss event.

**Since**: 12

 |
| [EVENT\_CPU\_USAGE\_HIGH](#event_cpu_usage_high) "CPU\_USAGE\_HIGH" | 

High CPU usage event.

**Since**: 12

 |
| [EVENT\_BATTERY\_USAGE](#event_battery_usage) "BATTERY\_USAGE" | 

Battery usage statistics event.

**Since**: 12

 |
| [EVENT\_RESOURCE\_OVERLIMIT](#event_resource_overlimit) "RESOURCE\_OVERLIMIT" | 

Resource leak event.

**Since**: 12

 |
| [EVENT\_ADDRESS\_SANITIZER](#event_address_sanitizer) "ADDRESS\_SANITIZER" | 

Address sanitizer event.

**Since**: 12

 |
| [EVENT\_MAIN\_THREAD\_JANK](#event_main_thread_jank) "MAIN\_THREAD\_JANK" | 

Main thread jank event.

**Since**: 12

 |
| [EVENT\_APP\_HICOLLIE](#event_app_hicollie) "APP\_HICOLLIE" | 

Task execution timeout event.

**Since**: 18

 |
| [EVENT\_APP\_KILLED](#event_app_killed) "APP\_KILLED" | 

Application killed event.

**Since**: 20

 |
| [EVENT\_AUDIO\_JANK\_FRAME](#event_audio_jank_frame) "AUDIO\_JANK\_FRAME" | 

Audio jank event.

**Since**: 21

 |
| [DOMAIN\_OS](#domain_os) "OS" | 

OS scope.

**Since**: 12

 |
| [EVENT\_MAIN\_THREAD\_JANK\_V2](#event_main_thread_jank_v2) "MAIN\_THREAD\_JANK\_V2" | 

Sets the main thread jank event configuration policy.

**Since**: 22

 |

#### Macro Description

#### \[h2\]EVENT\_USER\_LOGIN

#define EVENT\_USER\_LOGIN "hiappevent.user\_login"

**Description**

User login event.

**Since**: 8

#### \[h2\]EVENT\_USER\_LOGOUT

#define EVENT\_USER\_LOGOUT "hiappevent.user\_logout"

**Description**

User logout event.

**Since**: 8

#### \[h2\]EVENT\_DISTRIBUTED\_SERVICE\_START

#define EVENT\_DISTRIBUTED\_SERVICE\_START "hiappevent.distributed\_service\_start"

**Description**

Distributed service event.

**Since**: 8

#### \[h2\]EVENT\_APP\_CRASH

#define EVENT\_APP\_CRASH "APP\_CRASH"

**Description**

Crash event.

**Since**: 12

#### \[h2\]EVENT\_APP\_FREEZE

#define EVENT\_APP\_FREEZE "APP\_FREEZE"

**Description**

Application freeze event.

**Since**: 12

#### \[h2\]EVENT\_APP\_LAUNCH

#define EVENT\_APP\_LAUNCH "APP\_LAUNCH"

**Description**

Time-consuming launch event.

**Since**: 12

#### \[h2\]EVENT\_SCROLL\_JANK

#define EVENT\_SCROLL\_JANK "SCROLL\_JANK"

**Description**

Scrolling frame loss event.

**Since**: 12

#### \[h2\]EVENT\_CPU\_USAGE\_HIGH

#define EVENT\_CPU\_USAGE\_HIGH "CPU\_USAGE\_HIGH"

**Description**

High CPU usage event.

**Since**: 12

#### \[h2\]EVENT\_BATTERY\_USAGE

#define EVENT\_BATTERY\_USAGE "BATTERY\_USAGE"

**Description**

Battery usage statistics event.

**Since**: 12

#### \[h2\]EVENT\_RESOURCE\_OVERLIMIT

#define EVENT\_RESOURCE\_OVERLIMIT "RESOURCE\_OVERLIMIT"

**Description**

Resource leak event.

**Since**: 12

#### \[h2\]EVENT\_ADDRESS\_SANITIZER

#define EVENT\_ADDRESS\_SANITIZER "ADDRESS\_SANITIZER"

**Description**

Address sanitizer event.

**Since**: 12

#### \[h2\]EVENT\_MAIN\_THREAD\_JANK

#define EVENT\_MAIN\_THREAD\_JANK "MAIN\_THREAD\_JANK"

**Description**

Main thread jank event.

**Since**: 12

#### \[h2\]EVENT\_APP\_HICOLLIE

#define EVENT\_APP\_HICOLLIE "APP\_HICOLLIE"

**Description**

Task execution timeout event.

**Since**: 18

#### \[h2\]EVENT\_APP\_KILLED

#define EVENT\_APP\_KILLED "APP\_KILLED"

**Description**

Application killed event.

**Since**: 20

#### \[h2\]EVENT\_AUDIO\_JANK\_FRAME

#define EVENT\_AUDIO\_JANK\_FRAME "AUDIO\_JANK\_FRAME"

**Description**

Audio jank event.

**Since**: 21

#### \[h2\]DOMAIN\_OS

#define DOMAIN\_OS "OS"

**Description**

OS scope.

**Since**: 12

#### \[h2\]EVENT\_MAIN\_THREAD\_JANK\_V2

#define EVENT\_MAIN\_THREAD\_JANK\_V2 "MAIN\_THREAD\_JANK\_V2"

**Description**

Sets the main thread jank event configuration policy.

**Since**: 22
