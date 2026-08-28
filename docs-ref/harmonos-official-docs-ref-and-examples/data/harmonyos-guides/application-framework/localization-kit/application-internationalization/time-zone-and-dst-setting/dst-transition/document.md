# DST Transition

#### Use Cases

DST is a local time system that sees manual adjustment to the time with the aim of saving energy in certain countries/regions. When DST is enabled, the time is usually advanced by a certain period compared to the standard time.

#### How It Works

When the system time reaches the DST transition point, DST transition is automatically implemented based on the DST transition rules configured in the system. If an application uses a standard TS API, for example, Date(), to obtain and display the time, it also displays the DST time when the DST transition time is reached.

## DST Transition Calculation

1.  Import the related modules.
    
    import { i18n } from '@kit.LocalizationKit';
    
2.  Application scenario.
    

-   Calculate the number of hours in a day. The number of hours in a day changes on the day of DST transition. The number of hours is not always 24. In most countries, there are 23 hours on the day when DST starts and there are 25 hours on the day when the DST ends. Calculate the number of hours between the same clock time before and after the DST transition. The following is an example of the code:
    
    let calendar: i18n.Calendar = i18n.getCalendar('zh-Hans');
    calendar.setTimeZone('Europe/London');
    calendar.set (2021, 2, 27, 16, 0, 0); // Time before the DST starts
    let startTime = calendar.getTimeInMillis();
    calendar.set (2021, 2, 28, 16, 0, 0); // Time in the DST period
    let finishTime = calendar.getTimeInMillis();
    let hours = (finishTime - startTime) / (3600 \* 1000); // hours = 23
    

## Storing and Displaying Time Data

Store and display time data according to the local DST timing rules. The time gap and repetition caused by DST transition need to be processed.

The transition into DST will cause a period of time gap, for example, transition from 1:59:59 to 3:00:00. The transition out of DST will cause a period of time overlap, for example, rollback from 3:59:59 to 3:00:00.

It is recommended that the DST flag be added to the local time when DST is active.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8f/v3/6FF6FUjxSAitA3ad2oz-MA/en-us_image_0000002568684791.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061955Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=8301D0D650F2B8717894B3EF37A7AAD17FE863D768D791A8C350D6395125E80A)

## Storing and Transmitting Time Data

You are advised to use the standard time (UTC or GMT) of time zone 0 for time data storage and transmission. This helps prevent data loss or errors caused by DST transition.
