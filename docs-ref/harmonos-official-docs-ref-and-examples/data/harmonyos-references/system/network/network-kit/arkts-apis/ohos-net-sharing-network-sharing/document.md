# @ohos.net.sharing (Network Sharing)

This module allows you to share your device's network connectivity with other connected devices.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/08/v3/JpwZLCfCSAiCpx8jhWXdcQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062345Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=3084B4E33F7C12EC3AFEE7FEA9593C654AA6EC5BDDB28656381BEF2935626A7B)

The initial APIs of this module are supported since API version 9. Newly added APIs will be marked with a superscript to indicate their earliest API version.

#### Modules to Import

import { sharing } from '@kit.NetworkKit';

#### NetHandle

type NetHandle = connection.NetHandle

Defines the handle of the data network. Before calling the **NetHandle** function, call the **getNetHandle** function to obtain a **NetHandle** object.

**System capability**: SystemCapability.Communication.NetManager.Core

| Type | Description |
| :-- | :-- |
| [connection.NetHandle](../ohos-net-connection-network-connection-management/document.md#nethandle) | Network connection information. |
