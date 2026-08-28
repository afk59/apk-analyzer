# Debugging Overview

DevEco Studio provides a variety of debug features. You can debug your app/atomic service written in a single programming language like JS, ArkTS, or C/C++, or multiple languages, and debug third-party library source code.

You can debug your app/atomic service on a real device or the Emulator or Previewer provided by DevEco Studio. The following figure shows the process of debugging an app/atomic service on a real device. For details about debugging on the Emulator or Previewer, see [Running Your App on the Emulator](../../running-your-app-on-the-emulator/document.md) and [Debugging Your App Using the Previewer](../../previewing-the-ui/debugging-your-app-using-the-previewer/document.md).

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f3/v3/UPg0V0DmR_y-wfA9_bnIqw/en-us_image_0000002500910198.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062150Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=78CA6BBC4211AA527CA4840DB9978CC23C73676D5D277258AFE87B82148C973B)

1.  [Set signing configuration](../../configuring-a-debug-signature/document.md): If you are debugging on a real device, you must first sign the HAP.
2.  [Set the debug type](../running-debugging-configuration/document.md#section1170735241213): The default type is **Detect Automatically**.
3.  [Set the HAP installation mode](../running-debugging-configuration/document.md#section531811771410): You can uninstall the app/atomic service and then reinstall it, or install the app/atomic service in overwrite mode.
4.  [Start debugging](../code-debugging/arkts-code-debugging/starting-and-debugging-an-app-atomic-service/document.md): You can start your app/atomic service and debug it or debug an app/atomic service that is already running.
