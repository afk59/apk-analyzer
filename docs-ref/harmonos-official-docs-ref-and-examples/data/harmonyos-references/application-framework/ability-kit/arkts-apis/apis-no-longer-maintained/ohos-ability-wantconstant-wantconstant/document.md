# @ohos.ability.wantConstant (wantConstant)

The module provides the actions, entities, and flags used in Want objects.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/43/v3/bSOoY-UQRZi1BDyJf8JbBw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062211Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=8A35E6B46CAB61DFD22B3420DB9F9F347F5A52C672DC25B63F5F2A5920D987B5)

The APIs of this module are supported since API version 6 and deprecated since API version 9. You are advised to use [@ohos.app.ability.wantConstant](../../both-models-recommended/ohos-app-ability-wantconstant-want-constants/document.md) instead. Newly added APIs will be marked with a superscript to indicate their earliest API version.

#### Modules to Import

import wantConstant from '@ohos.ability.wantConstant';

#### Action

Enumerates the action constants of the Want object. **action** specifies the operation to execute.

**System capability**: SystemCapability.Ability.AbilityBase

| Name | Value | Description |
| :-- | :-- | :-- |
| ACTION\_HOME | ohos.want.action.home | Action of returning to the home page. |
| ACTION\_DIAL | ohos.want.action.dial | Action of launching the numeric keypad. |
| ACTION\_SEARCH | ohos.want.action.search | Action of launching the search function. |
| ACTION\_WIRELESS\_SETTINGS | ohos.settings.wireless | Action of launching the UI that provides wireless network settings, for example, Wi-Fi options. |
| ACTION\_MANAGE\_APPLICATIONS\_SETTINGS | ohos.settings.manage.applications | Action of launching the UI for managing installed applications. |
| ACTION\_APPLICATION\_DETAILS\_SETTINGS | ohos.settings.application.details | Action of launching the UI that displays the details of an application. |
| ACTION\_SET\_ALARM | ohos.want.action.setAlarm | Action of launching the UI for setting the alarm clock. |
| ACTION\_SHOW\_ALARMS | ohos.want.action.showAlarms | Action of launching the UI that displays all alarms. |
| ACTION\_SNOOZE\_ALARM | ohos.want.action.snoozeAlarm | Action of launching the UI for snoozing an alarm. |
| ACTION\_DISMISS\_ALARM | ohos.want.action.dismissAlarm | Action of launching the UI for deleting an alarm. |
| ACTION\_DISMISS\_TIMER | ohos.want.action.dismissTimer | Action of launching the UI for dismissing a timer. |
| ACTION\_SEND\_SMS | ohos.want.action.sendSms | Action of launching the UI for sending an SMS message. |
| ACTION\_CHOOSE | ohos.want.action.choose | Action of launching the UI for opening a contact or picture. |
| ACTION\_IMAGE\_CAPTURE8+ | ohos.want.action.imageCapture | Action of launching the UI for photographing. |
| ACTION\_VIDEO\_CAPTURE8+ | ohos.want.action.videoCapture | Action of launching the UI for shooting a video. |
| ACTION\_SELECT | ohos.want.action.select | Action of launching the UI for application selection. |
| ACTION\_SEND\_DATA | ohos.want.action.sendData | Action of launching the UI for sending a single data record. |
| ACTION\_SEND\_MULTIPLE\_DATA | ohos.want.action.sendMultipleData | Action of launching the UI for sending multiple data records. |
| ACTION\_SCAN\_MEDIA\_FILE | ohos.want.action.scanMediaFile | Action of requesting a media scanner to scan a file and add the file to the media library. |
| ACTION\_VIEW\_DATA | ohos.want.action.viewData | Action of viewing data. |
| ACTION\_EDIT\_DATA | ohos.want.action.editData | Action of editing data. |
| INTENT\_PARAMS\_INTENT | ability.want.params.INTENT | Action of displaying selection options with an action selector. |
| INTENT\_PARAMS\_TITLE | ability.want.params.TITLE | Title of the character sequence dialog box used with the action selector. |
| ACTION\_FILE\_SELECT7+ | ohos.action.fileSelect | Action of selecting a file. |
| PARAMS\_STREAM7+ | ability.params.stream | URI of the data stream associated with the target when the data is sent. The value must be an array of the string type. |
| ACTION\_APP\_ACCOUNT\_OAUTH 8+ | ohos.account.appAccount.action.oauth | Action of providing the OAuth service. |

#### Entity

Enumerates the entity constants of the Want object. **entity** specifies additional information of the target ability.

**System capability**: SystemCapability.Ability.AbilityBase

| Name | Value | Description |
| :-- | :-- | :-- |
| ENTITY\_DEFAULT | entity.system.default | Default entity. The default entity is used if no entity is specified. |
| ENTITY\_HOME | entity.system.home | Home screen entity. |
| ENTITY\_VOICE | entity.system.voice | Voice interaction entity. |
| ENTITY\_BROWSABLE | entity.system.browsable | Browser type entity. |
| ENTITY\_VIDEO | entity.system.video | Video type entity. |

#### Flags

Enumerates the flags that specify how the Want will be handled.

**System capability**: SystemCapability.Ability.AbilityBase

| Name | Value | Description |
| :-- | :-- | :-- |
| FLAG\_AUTH\_READ\_URI\_PERMISSION | 0x00000001 | Grants the permission to read the URI. |
| FLAG\_AUTH\_WRITE\_URI\_PERMISSION | 0x00000002 | Grants the permission to write data to the URI. |
| FLAG\_ABILITY\_FORWARD\_RESULT | 0x00000004 | Returns the result to the ability. |
| FLAG\_ABILITY\_CONTINUATION | 0x00000008 | Indicates whether the ability on the local device can be continued on a remote device. |
| FLAG\_NOT\_OHOS\_COMPONENT | 0x00000010 | Indicates that a component does not belong to OHOS. |
| FLAG\_ABILITY\_FORM\_ENABLED | 0x00000020 | Indicates that an ability is enabled. |
| FLAG\_ABILITYSLICE\_MULTI\_DEVICE | 0x00000100 | Indicates the support for cross-device startup in the distributed scheduler. |
| FLAG\_START\_FOREGROUND\_ABILITY | 0x00000200 | Indicates that the ServiceAbility is started regardless of whether the host application has been started. |
| FLAG\_INSTALL\_ON\_DEMAND | 0x00000800 | Indicates that the specific ability will be installed if it has not been installed. |
| FLAG\_INSTALL\_WITH\_BACKGROUND\_MODE | 0x80000000 | Indicates that the specific ability will be installed in the background if it has not been installed. |
| FLAG\_ABILITY\_CLEAR\_MISSION | 0x00008000 | Clears other operation missions. This flag can be set for the Want passed in [startAbility](../../fa-model/ohos-ability-featureability-featureability-module/document.md#featureabilitystartability). It must be used together with **FLAG\_ABILITY\_NEW\_MISSION**. |
| FLAG\_ABILITY\_NEW\_MISSION | 0x10000000 | Creates a mission on the history mission stack. |
| FLAG\_ABILITY\_MISSION\_TOP | 0x20000000 | Reuses an ability instance if it is on the top of an existing mission stack; creates an ability instance otherwise. |
