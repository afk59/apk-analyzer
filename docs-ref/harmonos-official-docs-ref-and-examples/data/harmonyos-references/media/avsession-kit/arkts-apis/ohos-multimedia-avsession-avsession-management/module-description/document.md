# Module Description

The AVSession module provides APIs for media playback control so that applications can access the system's Media Controller.

This module provides the following typical features related to media sessions:

-   [AVSession](../interface-avsession/document.md): used to set session metadata, playback state information, and more.
-   [AVSessionController](../interface-avsessioncontroller/document.md): used to obtain session IDs, send commands and events to sessions, and obtain the session metadata and playback state information.
-   [AVCastController](../interface-avcastcontroller/document.md): used to control playback, listen for remote playback state changes, and obtain the remote playback state in casting scenarios.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ff/v3/6AAiswYYQ_aWom0EVFqwfA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062424Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=F36E9F63FF2A9542F45B5D79B8BFD9FB198459048B72FA88733EEB028B85E963)

The initial APIs of this module are supported since API version 9. Newly added APIs will be marked with a superscript to indicate their earliest API version.

#### Modules to Import

import { avSession } from '@kit.AVSessionKit';
