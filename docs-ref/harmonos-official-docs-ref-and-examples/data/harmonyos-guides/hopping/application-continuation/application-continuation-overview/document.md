# Application Continuation Overview

The application continuation feature allows the operations being performed by a user on one device to be quickly switched and seamlessly continued in the same application on another device.

For example, when the environment changes during usage and a more appropriate device is detected, the user can migrate an ongoing task to another device without exiting. After the continuation is complete, the application on the previous device can be exited or retained. The started device continues the task.

As shown in the figure, notes being edited on the go can be seamlessly switched from your phone to the tablet when you arrive at the office.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/df/v3/NG6z8Q53RbSsddkN9v_AHA/en-us_image_0000002255909705.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062129Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=73F47446058710A323163572FD3A7C781AEDDD60647042EA260015CE87C0D81D "Click to enlarge")

#### Working Principles

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1e/v3/bwl2LDL2QqKa7BscE26quA/en-us_image_0000002221069986.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062129Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=B9D5A9F6F5975D011E81F65D684DDFCE56CE07EB05DB6510B00CF7AC42A778C6 "Click to enlarge")

1.  On the source device, the UIAbility uses **onContinue()** to save service data to be continued.
    
    For example, to enable a web page being viewed on a device to be viewed on another device, the system automatically saves the page status, such as the browsing progress of the current page, and the **onContinue** callback returns the service content such as the page URL.
    
2.  The distributed framework provides a mechanism for saving and restoring the application UI, page stacks, and service data across devices. It sends the data from the source device to the target device.
3.  On the target device, the same UIAbility restores the service data through the **onCreate** or **onNewWant** API.

#### Scenarios of Initiating an Application Continuation

Application continuation is usually initiated on pages where users spend extended periods. Typical pages and their synchronized contents are as follows:

-   Notepad: Initiate an application continuation on the Notepad details page, and the browsing progress is synchronized.
-   Memo: Initiate an application continuation on the memo editing page, and the memo browsing or editing progress is synchronized.
-   Calendar: Initiate an application continuation on any page, and the date view and schedule browsing or editing progress are synchronized.
-   Email: Initiate an application continuation on the email editing page, and the editing progress and attachments are synchronized.
-   Browser: Initiate an application continuation request on the web details page, and the web page browsing progress is synchronized.
-   Map application: Initiate an application continuation on the route query or navigation page, and the current route and navigation are synchronized.
-   Video/Short video/Micro-drama/Live streaming applications: Initiate an application continuation on the audio/video playback or live page, and the audio/video playback progress and live playback progress are synchronized.
-   Music/Karaoke/Radio/Instrument applications: Initiate an application continuation on the audio/video playback or live page, and the audio/video playback progress and live playback progress are synchronized.
-   Early education/Kids song applications: Initiate an application continuation on the audio/video playback or live page, and the audio/video playback progress and live playback progress are synchronized.
-   Audiobook/eBook/Novel/Magazine: Initiate an application continuation on the home page of a book, novel, or audiobook, and the reading progress is synchronized.
-   News applications: Initiate an application continuation on the news details page, and the browsing progress is synchronized.
-   Meeting applications: Initiate an application continuation on a meeting page, and the current meeting is synchronized.
-   Design applications: Initiate an application continuation on the CAD editing page, and the editing content is synchronized.
-   Social media platform: Initiate an application continuation on the image/video browsing or editing page, and the browsing and editing progresses are synchronized.
-   Photo/Image editing applications: Initiate an application continuation on the image/video editing page, and the editing content and progress are synchronized.

#### Scenarios Where the Source Application Exits After Continuation

By default, the source application automatically exits after continuation is complete. You can configure the exit by referring to [Exiting the Application on Demand](../application-continuation-development/document.md#section976341819443).

Recommended configuration items for different types of applications are as follows:

-   Notepad: Exit.
-   Memo: Exit.
-   Calendar: Exit.
-   Email: Exit.
-   Browser: Exit.
-   Map applications: Exit.
-   Audiobook/eBook/Novel/Magazines: Exit. However, if the audiobook or live streaming is involved, the application may not exit but only pause the playing of the audiobook, or does not exit with live streaming continued.
-   News applications: Exit.
-   Exam preparation/Education applications: Exit.
-   Meeting applications: Exit the meeting and navigate to the chat page without closing the application.
-   House renting/House buying/House decoration applications: Exit.
-   Recipe/Baking/Food/Cookbook applications: Exit.
-   Stock/Stock market/Fund/Securities/Securities investment consulting applications: Exit.
-   Product recommendation applications: Exit.
-   Photo/Image editing applications: Exit.
-   Gaming applications: Exit.
