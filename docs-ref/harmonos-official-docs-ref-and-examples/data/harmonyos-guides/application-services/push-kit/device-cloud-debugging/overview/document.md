# Overview

The [Pushing Scenario-Specific Messages](../../pushing-scenario-specific-messages/document.md) section describes all push scenarios of Push Kit. The development of each scenario can be roughly divided into two major steps:

1.  Obtain a push token and complete push scenario ArkTS code development for the device side.
2.  Send an application to Push Kit to request sending a scenario-specific message.

This section provides more detailed cloud-side development content based on the major steps, so you can better conduct device-cloud debugging after device-side development. Before performing operations in this section, please at least [obtain a push token](../../preparations/obtaining-a-push-token/document.md).

#### Service Process

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8f/v3/BbS7ZcoZTTKBRoXh-4WxfQ/en-us_image_0000002368545984.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062116Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=2490FBA2C1F69A24C8CD8C81B026925C48D0B3A1DE9871E7BF804BC1B7A74E40 "Click to enlarge")

The service process on the Push Kit server is as follows:

1.  The app server sends a request to the Push Kit server for pushing a scenario-specific message. For details, please refer to [Pushing Scenario-Specific Messages](../pushing-scenario-specific-messages/document.md). Then the app server receives a response from the Push Kit server.
2.  The Push Kit server delivers the scenario-specific message to the device where the app is installed, and the Push Kit client returns the response status to the Push Kit server.
3.  The Push Kit server sends a message receipt to the app server. You can complete operations in [(Optional) Developing the Message Receipt](../optional-developing-the-message-receipt/document.md), so your server can receive the returned status after the Push Kit server delivers the message to the device side. Not enabling a message receipt will not interfere with the message delivery process.
