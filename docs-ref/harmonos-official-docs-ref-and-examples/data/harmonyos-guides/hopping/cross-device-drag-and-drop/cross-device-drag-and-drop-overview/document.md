# Cross-Device Drag and Drop Overview

Cross-device drag and drop allows the keyboard and mouse to be shared across devices. Files and texts can be dragged and dropped between tablets or any 2-in-1 devices.

For example, two tablets can share a set of keyboard and mouse. A user can drag the material in device **A** to device **B** in one step using cross-device drag and drop, implementing cross-device collaborative work.

In the current system application, the Files and Browser support drag-out, and Notepad supports drag-in. Users can:

-   Drag an image from the file manager of device A to the Notepad application of device B.
-   Drag a text in Notepad on device A to Notepad on device B, and use the keyboard connected to device A to enter the text on device B, implementing collaborative operation.

You can drag components to or out of a device based on service requirements.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7b/v3/OmlkP-yAR2yzMb0kev_6AA/en-us_image_0000002221069978.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062129Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=09396C9F57634ADDC27FABC54F08058ACC30BEC25FCD9880D2979925BBC6B99E "Click to enlarge")

#### Working Principles

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bc/v3/wbb3jMy3TOSg1YsyH7uZ5g/en-us_image_0000002255909701.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062129Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=AD95B635744CA1AC791B07CD221520ACEC5FE583E0875D91BB80D0F33B216F60 "Click to enlarge")

1.  A drag-and-drop event is triggered when a user clicks a component.
2.  The data to be dragged is set in the application.
3.  The system completes cross-device data processing without interrupting the application running.
4.  When a user releases the button, the drag release event is triggered.
5.  The application on the target device obtains and processes the dropped data.
