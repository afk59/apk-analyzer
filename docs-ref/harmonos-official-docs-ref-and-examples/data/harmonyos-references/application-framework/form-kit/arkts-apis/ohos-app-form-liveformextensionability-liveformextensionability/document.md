# @ohos.app.form.LiveFormExtensionAbility (LiveFormExtensionAbility)

The **LiveFormExtensionAbility** module, inherited from [ExtensionAbility](../../../ability-kit/arkts-apis/stage-model/ohos-app-ability-extensionability-extensionability-base-class/document.md), provides interactive widget functions, including creating and destroying interactive widgets.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/38/v3/kwCjAS0OTI28-Sr_dFAkWQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062323Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=B5C20131C3FE68139D917B46F246C012419F5135E928B8EFEED8EBC98A532FAB)

The initial APIs of this module are supported since API version 20. Newly added APIs will be marked with a superscript to indicate their earliest API version.

The APIs of this module can be used only in the stage model.

Exceptions may occur if some APIs are called. For details about the API list, see [Appendix](#appendix).

#### Modules to Import

import { LiveFormExtensionAbility } from '@kit.FormKit';

#### LiveFormExtensionAbility

Interactive widget extension class. It provides APIs for the widget provider to receive notifications about widget creation and destruction.

#### \[h2\]Properties

**Model restriction**: This API can be used only in the stage model.

**System capability**: SystemCapability.Ability.Form

**Atomic service API**: This API can be used in atomic services since API version 20.

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| context | [LiveFormExtensionContext](../application/liveformextensioncontext/document.md) | No | No | Context of the **LiveFormExtensionAbility**. This context is inherited from [ExtensionContext](../../../ability-kit/arkts-apis/dependent-elements-and-definitions/application/extensioncontext/document.md). |

#### \[h2\]onLiveFormCreate

onLiveFormCreate(liveFormInfo: LiveFormInfo, session: UIExtensionContentSession): void

Called after the UI content of **LiveFormExtensionAbility** is created.

**Model restriction**: This API can be used only in the stage model.

**System capability**: SystemCapability.Ability.Form

**Atomic service API**: This API can be used in atomic services since API version 20.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| liveFormInfo | [LiveFormInfo](#liveforminfo) | Yes | Interactive widget information, including the widget ID. |
| session | [UIExtensionContentSession](../../../ability-kit/arkts-apis/stage-model/ohos-app-ability-uiextensioncontentsession-uiextensionability-ui-operation-class/document.md) | Yes | UI information. |

**Example**

import { UIExtensionContentSession } from '@kit.AbilityKit';
import { LiveFormExtensionAbility, LiveFormInfo } from '@kit.FormKit';

const TAG: string = '\[testTag\] LiveFormExtAbility';

export default class LiveFormExtAbility extends LiveFormExtensionAbility {
  onLiveFormCreate(liveFormInfo: LiveFormInfo, session: UIExtensionContentSession) {
    console.info(TAG, \`onLiveFormCreate, formId: ${liveFormInfo.formId}\`);
  }
}

#### \[h2\]onLiveFormDestroy

onLiveFormDestroy(liveFormInfo: LiveFormInfo): void

Called to clear resources when this **LiveFormExtensionAbility** is destroyed.

**Model restriction**: This API can be used only in the stage model.

**System capability**: SystemCapability.Ability.Form

**Atomic service API**: This API can be used in atomic services since API version 20.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| liveFormInfo | [LiveFormInfo](#liveforminfo) | Yes | Interactive widget information, including the widget ID. |

**Example**

import { LiveFormExtensionAbility, LiveFormInfo } from '@kit.FormKit';

const TAG: string = '\[testTag\] LiveFormExtAbility';

export default class LiveFormExtAbility extends LiveFormExtensionAbility {
  onLiveFormDestroy(liveFormInfo: LiveFormInfo) {
    console.info(TAG, \`onLiveFormDestroy, liveFormInfo: ${liveFormInfo.formId}\`);
  }
}

#### \[h2\]LiveFormInfo

Defines the interactive widget information.

**Model restriction**: This API can be used only in the stage model.

**System capability**: SystemCapability.Ability.Form

**Atomic service API**: This API can be used in atomic services since API version 20.

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| formId | string | No | No | Widget ID. |
| rect | [formInfo.Rect](../ohos-app-form-forminfo-forminfo/document.md#rect20) | No | No | Widget location and dimension. |
| borderRadius | number | No | No | Widget corner radius. The value must be greater than 0, in vp. |

#### Appendix

The following table lists the APIs that cannot be called by this module.

| Kit | Module |
| :-- | :-- |
| AbilityKit | 
[@ohos.ability.featureAbility (FeatureAbility)](../../../ability-kit/arkts-apis/fa-model/ohos-ability-featureability-featureability-module/document.md)

[@ohos.ability.particleAbility (ParticleAbility)](../../../ability-kit/arkts-apis/fa-model/ohos-ability-particleability-particleability-module/document.md)

[@ohos.bundle.launcherBundleManager (launcherBundleManager)](../../../ability-kit/arkts-apis/both-models-recommended/ohos-bundle-launcherbundlemanager-launcherbundlemanager-module/document.md)

[@ohos.continuation.continuationManager (Continuation/Collaboration Management)](../../../ability-kit/arkts-apis/stage-model/ohos-continuation-continuationmanager-continuation-collaboration-management/document.md)

 |
| BasicServicesKit | 

[@ohos.account.appAccount (App Account Management)](../../../../system/basic-functions/basic-services-kit/arkts-apis/account-management/ohos-account-appaccount-application-account-management/document.md)

[@ohos.account.distributedAccount (Distributed Account Management)](../../../../system/basic-functions/basic-services-kit/arkts-apis/account-management/ohos-account-distributedaccount-distributed-account-management/document.md)

[@ohos.account.osAccount (System Account Management)](../../../../system/basic-functions/basic-services-kit/arkts-apis/account-management/ohos-account-osaccount-system-account-management/document.md)

[@ohos.pasteboard (Pasteboard)](../../../../system/basic-functions/basic-services-kit/arkts-apis/data-file-processing/ohos-pasteboard-pasteboard/document.md)

[@ohos.request (Upload and Download)](../../../../system/basic-functions/basic-services-kit/arkts-apis/data-file-processing/ohos-request-upload-and-download/document.md)

[@ohos.wallpaper (Wallpaper)](../../../../system/basic-functions/basic-services-kit/arkts-apis/others/ohos-wallpaper-wallpaper/document.md)

 |
| BackgroundTasksKit | 

[@ohos.backgroundTaskManager (Background Task Management)](../../../background-tasks-kit/arkts-apis/apis-no-longer-maintained/ohos-backgroundtaskmanager-background-task-management/document.md)

[@ohos.resourceschedule.backgroundTaskManager (Background Task Management)](../../../background-tasks-kit/arkts-apis/ohos-resourceschedule-backgroundtaskmanager-background-task-management/document.md)

[@ohos.reminderAgent (reminderAgent)](../../../background-tasks-kit/arkts-apis/apis-no-longer-maintained/ohos-reminderagent-agent-powered-reminder/document.md)

[@ohos.reminderAgentManager (Agent-Powered Reminders)](../../../background-tasks-kit/arkts-apis/ohos-reminderagentmanager-agent-powered-reminder/document.md)

 |
| CalendarKit | [@ohos.calendarManager (Calendar Manager)](../../../../application-services/calendar-kit/arkts-apis/ohos-calendarmanager-calendar-manager/document.md) |
| ConnectivityKit | 

[@ohos.connectedTag (Active Tags)](../../../../system/network/connectivity-kit/arkts-apis/ohos-connectedtag-active-tags/document.md)

[@ohos.nfc.cardEmulation (Standard NFC Card Emulation)](../../../../system/network/connectivity-kit/arkts-apis/ohos-nfc-cardemulation-standard-nfc-card-emulation/document.md)

[@ohos.nfc.controller (Standard NFC)](../../../../system/network/connectivity-kit/arkts-apis/ohos-nfc-controller-standard-nfc/document.md)

[@ohos.nfc.tag (Standard NFC Tags)](../../../../system/network/connectivity-kit/arkts-apis/ohos-nfc-tag-standard-nfc-tags/document.md)

[nfctech (Standard NFC Technologies)](../../../../system/network/connectivity-kit/arkts-apis/tag/nfctech-standard-nfc-technologies/document.md)

[tagSession (Standard NFC Tag Session)](../../../../system/network/connectivity-kit/arkts-apis/tag/tagsession-standard-nfc-tag-session/document.md)

 |
| ContactsKit | [@ohos.contact (Contacts)](../../../../application-services/contacts-kit/arkts-api/ohos-contact-contacts/document.md) |
| ArkData | 

[@ohos.data.distributedData (Distributed Data Management)](../../../arkdata/arkts-apis/apis-no-longer-maintained/ohos-data-distributeddata-distributed-data-management/document.md)

[@ohos.data.distributedDataObject (Distributed Data Object)](../../../arkdata/arkts-apis/ohos-data-distributeddataobject-distributed-data-object/document.md)

[@ohos.data.distributedKVStore (Distributed KV Store)](../../../arkdata/arkts-apis/ohos-data-distributedkvstore-distributed-kv-store/document.md)

 |
| MDMKit | 

[@ohos.enterprise.adminManager (Administrator Permission Management)](../../../../system/basic-functions/mdm-kit/arkts-apis/ohos-enterprise-adminmanager-administrator-permission-management/document.md)

[@ohos.enterprise.deviceInfo (Device Information Management)](../../../../system/basic-functions/mdm-kit/arkts-apis/ohos-enterprise-deviceinfo-device-information-management/document.md)

 |
| CoreFileKit | [@ohos.file.picker (Picker)](../../../core-file-kit/arkts-apis/ohos-file-picker-picker/document.md) |
| MediaLibraryKit | 

[@ohos.file.sendablePhotoAccessHelper (Album Management Based on a Sendable Object)](../../../../media/media-library-kit/arkts-apis/ohos-file-sendablephotoaccesshelper-album-management-based-on-a-sendable-object/document.md)

[@ohos.file.AlbumPickerComponent (AlbumPickerComponent)](../../../../media/media-library-kit/arkts-components/ohos-file-albumpickercomponent-albumpickercomponent/document.md)

[@ohos.file.PhotoPickerComponent (PhotoPicker Component)](../../../../media/media-library-kit/arkts-components/ohos-file-photopickercomponent-photopickercomponent/document.md)

[@ohos.file.RecentPhotoComponent (RecentPhotoComponent)](../../../../media/media-library-kit/arkts-components/ohos-file-recentphotocomponent-recentphotocomponent/document.md)

[@ohos.multimedia.movingphotoview (MovingPhotoView)](../../../../media/media-library-kit/arkts-components/ohos-multimedia-movingphotoview-movingphotoview/document.md)

 |
| PerformanceAnalysisKit | [@ohos.hidebug (HiDebug)](../../../../system/debugging-tools/performance-analysis-kit/arkts-api/ohos-hidebug-hidebug/document.md) |
| AudioKit | [@ohos.multimedia.audio (Audio Management)](../../../../media/audio-kit/arkts-apis/ohos-multimedia-audio-audio-management/module-description/document.md) |
| CameraKit | 

[@ohos.multimedia.cameraPicker (Camera Picker)](../../../../media/camera-kit/arkts-apis/ohos-multimedia-camerapicker-camera-picker/document.md)

[@ohos.multimedia.camera (Camera Management)](../../../../media/camera-kit/arkts-apis/ohos-multimedia-camera-camera-management/module-description/document.md)

 |
| AVSessionKit | 

[@ohos.multimedia.avCastPicker (AVCastPicker)](../../../../media/avsession-kit/arkts-components/ohos-multimedia-avcastpicker-avcastpicker/document.md)

[@ohos.multimedia.avsession (AVSession Management)](../../../../media/avsession-kit/arkts-apis/ohos-multimedia-avsession-avsession-management/module-description/document.md)

 |
| MediaKit | [@ohos.multimedia.media (Media)](../../../../media/media-kit/arkts-apis/ohos-multimedia-media-media/module-description/document.md) |
| NotificationKit | 

[@ohos.notification (Notification)](../../../../application-services/notification-kit/arkts-apis/apis-no-longer-maintained/ohos-notification-notification/document.md)

[@ohos.notificationManager (NotificationManager)](../../../../application-services/notification-kit/arkts-apis/ohos-notificationmanager-notificationmanager/document.md)

 |
| TelephonyKit | 

[@ohos.telephony.call (Call)](../../../../system/network/telephony-kit/arkts-api/ohos-telephony-call-call/document.md)

[@ohos.telephony.data (Cellular Data)](../../../../system/network/telephony-kit/arkts-api/ohos-telephony-data-cellular-data/document.md)

[@ohos.telephony.observer (observer)](../../../../system/network/telephony-kit/arkts-api/ohos-telephony-observer-observer/document.md)

[@ohos.telephony.radio (Network Search)](../../../../system/network/telephony-kit/arkts-api/ohos-telephony-radio-network-search/document.md)

[@ohos.telephony.sim (SIM Management)](../../../../system/network/telephony-kit/arkts-api/ohos-telephony-sim-sim-management/document.md)

[@ohos.telephony.sms (SMS)](../../../../system/network/telephony-kit/arkts-api/ohos-telephony-sms-sms/document.md)

 |
| UserAuthenticationKit | [@ohos.userIAM.userAuth (User Authentication)](../../../../system/security/user-authentication-kit/arkts-apis/ohos-useriam-userauth-user-authentication/document.md) |
| ArkUI | [@ohos.window (Window)](../../../arkui/arkts-api/window-manager/ohos-window-window/module-description/document.md) |
| MapKit | [sceneMap (Scenario-based Controls)](../../../../application-services/map-kit/arkts-apis/scenemap-scenario-based-controls/document.md) |
| ServiceCollaborationKit | 

[devicePicker (Device Selection Controller)](../../../../system/network/service-collaboration-kit/arkts-components/devicepicker-device-selection-controller/document.md)

[CollaborationDevicePicker (Hopping Control)](../../../../system/network/service-collaboration-kit/arkts-components/collaborationdevicepicker-hopping-control/document.md)

 |
| ShareKit | 

[systemShare (System Share)](../../../../application-services/share-kit/arkts-apis/systemshare-system-share/document.md)

[harmonyShare (Huawei Share)](../../../../application-services/share-kit/arkts-apis/harmonyshare-huawei-share/document.md)

 |
| VisionKit | 

[CardRecognition (Card Recognition Control)](../../../../ai/vision-kit/arkts-components/cardrecognition-card-recognition-control/document.md#section143611912403)

[DocumentScanner (Document Scanning Control)](../../../../ai/vision-kit/arkts-components/documentscanner-document-scanning-control/document.md#section143611912403)

 |
| ScanKit | [Scan Kit](../../../../media/scan-kit/document.md) |
