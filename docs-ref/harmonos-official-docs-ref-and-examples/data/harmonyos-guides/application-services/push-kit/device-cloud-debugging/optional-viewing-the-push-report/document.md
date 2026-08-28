# (Optional) Viewing the Push Report

You can check your app's push reports. Sign in to [AppGallery Connect](https://developer.huawei.com/consumer/en/service/josp/agc/index.html), click **Development and services**, and find and click the desired project in the project list. Then, go to **Grow** > **Push Kit** > **Reports**. On the page displayed, you can view the push details by message and user.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d5/v3/qI08WTyBQCyYKSgklKgGOA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062117Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=3122C8CF92EF517E31276B3BC7D73FB851871433EA508B57FB6C197291109D22)

The report data generated on the current day can only be viewed the next day.

#### Notification Details

You can view details about scenario-specific messages that you have sent in charts and tables. You can either select **AppGallery Connect**, **API**, or **All channels** from the drop-down list box to filter the details by channel, or filter the details by message type.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a7/v3/KF73Q-JoR7yJsEEt4_KjIw/en-us_image_0000002475036913.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062117Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=B766684928E730D463A147E8AA95F382C746254139F0A2C9D81B7C00DC7975F3 "Click to enlarge")

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ec/v3/gRQ0Fh3HSVK6NuIcRYgB7Q/en-us_image_0000002441876790.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062117Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=E1B0B1039571C8DEDD7A40D912C8BE87C37CF9841B3DFD9315BA9613A51C2BF8 "Click to enlarge")

You can click ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cd/v3/U4UPgdenQcySm1FcHaoBcw/en-us_image_0000002441716914.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062117Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=A1D780D7094666C536D54F445DC30248911D089E3862F742BC77C9FCF7018083) next to **Custom** to customize columns displayed in the push message report. By default, the following columns are displayed: **Date**, **Type**, **Requests**, **Sendings**, **Deliveries**, **Displays**, **Tappings**, **Delivery rate (%)**, **Tap-through rate (%)**, **Discarded for silent devices**, **App uninstalled**, **Invalid token**, and **Notification disabled**. You can customize to display all columns or reset to display only default columns.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/61/v3/BwKcGmp_QkiI048AZy1dAg/en-us_image_0000002475491582.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062117Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=270C5B61B95C96473C17092DD5B1581667D4CB6B6BE6D537AFCEE2E4414732FE "Click to enlarge")

The data items in the report are described as follows:

-   **Requests**: estimated number of devices covered by the push task.
-   **Sendings**: number of messages actually sent to devices, which equals the number of requests subtracting the number of messages that do not meet the sending conditions.
-   **Deliveries**: number of messages actually delivered to devices.
-   **Displays**: number of messages displayed in the notification center.
-   **Tappings**: number of messages tapped by users.
-   **Delivery rate (%)**: percentage of delivered messages to sent messages.
-   **Tap-through rate (%)**: percentage of taps to displays.
-   **Discarded for silent devices**: number of messages discarded because the target device has not connected to the Internet for over 30 days.
-   **Discarded due to frequency control**: number of excessive messages discarded because the number of messages sent to the target device exceeds the upper limit.
-   **App uninstalled**: number of messages that are not delivered because the app on the target device has been uninstalled and not reinstalled.
-   **Invalid token**: number of messages that are not displayed because the token is invalid.
-   **Notification disabled**: number of messages that are not delivered because the app notification function is disabled on the target device.
-   **Message overwritten**: number of to-be-sent messages that are overwritten. Only one to-be-sent message is kept. Other to-be-sent messages will be overwritten and not be sent.
-   **Others**: number of messages that are not delivered due to other reasons, for example, the push link cannot be accessed normally.
-   **Expired**: number of messages expired because the target device is offline and does not go online in the message validity period.
-   **Cached**: number of messages that are still in their validity periods but the target device is offline.
-   **Undelivered**: number of messages that are not delivered to devices.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d5/v3/mlMEvsaPQCy3hDylipDkXA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062117Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=C4681420F765FBF5FD781354B3E52F98D063371E9C35566023A32D8797F64065)

Messages that do not meet the sending conditions include the following: **Discarded for silent devices**, **Discarded due to frequency control**, **App uninstalled**, **Invalid token**, **Notification disabled**, **Message overwritten**, **Others**, **Expired**, and **Cached**.

#### Target User Details

You can view details about target users as well as statistics about active users, new users, and total users by time.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fc/v3/vhqQWvrpQtuf7DWqtq0uGw/en-us_image_0000002441716926.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062117Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=18C12005074403F61725FDCBDBBCFEFBA97EEA49A0F9490D7A3F469E89BB35E8 "Click to enlarge")

The data items in the report are described as follows:

-   **Daily active users**: number of users whose devices connect to the Push Kit server on the current day.
-   **Daily new users**: number of users who newly install the app on the current day. If a user uninstalls and reinstalls the app repeatedly, the user will not be counted.
-   **Monthly active users**: number of users whose devices connect to the Push Kit server within the last 30 days before the current day.
-   **Total users**: total number of users who install the app.
