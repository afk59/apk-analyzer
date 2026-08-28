# Upon receiving a notification that the device's youth mode is enabled, what actions should the app take?

If the app is running in the background, it can refresh its content when brought to the foreground. You should consider whether background tasks, such as audio or video playback, should be interrupted to prevent minors from bypassing restrictions to access inappropriate content.

When the app is actively in use (e.g., during content browsing or media playback), it should be designed to automatically return to its main screen and refresh the displayed content to align with the user's age-appropriate settings upon detecting that the device's youth mode is enabled. A timely refresh is crucial to prevent several potential issues: (1) Minors might inadvertently access content that is not suitable for their age group, bypassing the implemented content filters. (2) Adults could remain inadvertently locked in youth mode, unable to switch back to their regular user experience. Below is an example of the design for the refreshed youth-mode main screen of an app.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b3/v3/KNIJ5tunQlGcoxwTqc8n_Q/en-us_image_0000002528943243.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062056Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=B242D05194B9A9B3C5EB22B071FCEF7F2651245723618E5E805C4EE053C47043 "Click to enlarge")
