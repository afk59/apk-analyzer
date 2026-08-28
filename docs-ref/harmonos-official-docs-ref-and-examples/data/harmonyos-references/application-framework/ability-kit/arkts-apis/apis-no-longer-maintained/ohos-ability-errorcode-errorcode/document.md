# @ohos.ability.errorCode (ErrorCode)

The ErrorCode module defines the error codes that may be returned when an ability is started.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2e/v3/hBEGjRzlSn2UgsxIn9F3bg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062211Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=1550AB1C7A39E45FA37DEAA9D02BB814B43D4F8ECF93A49289FC96CC06714081)

The initial APIs of this module are supported since API version 6. Newly added APIs will be marked with a superscript to indicate their earliest API version.

#### Modules to Import

import { ErrorCode } from '@kit.AbilityKit';

#### ErrorCode

Enumerates the error codes that may be returned when an ability is started.

**System capability**: SystemCapability.Ability.AbilityRuntime.Core

| Name | Value | Description |
| :-- | :-- | :-- |
| NO\_ERROR | 0 | The ability is started successfully. |
| INVALID\_PARAMETER | \-1 | Invalid parameter. |
| ABILITY\_NOT\_FOUND | \-2 | The ability is not found. |
| PERMISSION\_DENY | \-3 | Permission denied. |
