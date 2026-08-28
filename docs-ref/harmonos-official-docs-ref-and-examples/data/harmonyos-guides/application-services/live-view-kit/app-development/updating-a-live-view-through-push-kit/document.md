# Updating a Live View Through Push Kit

#### Use Cases

Updating a live view locally depends on the app's running. To ensure that the live view can be updated and ended properly within the lifecycle, you are advised to use Push Kit to update the live view in real time.

The following figure shows the process of updating a live view through Push Kit.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7b/v3/TeC9rKIERAmiPq9PtPw93Q/en-us_image_0000002511871732.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062111Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=ABCA95CC087817D4F578615459F084E670184FBC9F437B3A2F2FA93ECD140447 "Click to enlarge")

1.  Request a push token from Push Kit.
2.  Create a live view using Live View Kit. Then you need to save the live view ID, push token, live view scenario events, and business service status attributes to your app server.
3.  When the order status of the business service changes, Push Kit pushes update messages to update or end the live view.

For details about the development process, please refer to [Pushing a Live View Message](../../../push-kit/pushing-scenario-specific-messages/pushing-a-live-view-message/document.md) of Push Kit.
