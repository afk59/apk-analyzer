# @ohos.hiviewdfx.FaultLogExtensionAbility (Delayed Fault Notification)

This module implements the delayed fault notification feature.

When the crash and freeze events are subscribed by [HiAppEvent](../ohos-hiviewdfx-hiappevent-application-event-logging/document.md), the previous event can be received only after the application restarts. If the application fails to start or remains unresponsive for a long time, the fault may not be reported in time.

This module provides APIs for solving this issue. After the application implements FaultLogExtensionAbility, the system service is expected to start FaultLogExtensionAbility 30 minutes later after the application crashes or freezes.

You can subscribe to and process fault events through [onFaultReportReady](#onfaultreportready).

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/64/v3/BArLio6jRNKQKA8OwMmNVA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062413Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=83EA3554E97A3C144019DF69EA17881C32154D08BA2087E16C7865B752506DE1)

-   The initial APIs of this module are supported since API version 21. Newly added APIs will be marked with a superscript to indicate their earliest API version.
-   The APIs of this module can be used only in the stage model.
-   Exceptions may occur if some APIs are called by this module. For details, see [Appendix](#appendix).

#### Modules to Import

import { FaultLogExtensionAbility } from '@kit.PerformanceAnalysisKit';

#### FaultLogExtensionAbility

Implements the delayed fault notification. You can subscribe to and process fault events through [onFaultReportReady](#onfaultreportready).

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d3/v3/2Q4bxRRxR7SMB_k6_DJCPQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062413Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=873264FFD2EB493FA4517BA32F43BED2C2444248D4309A295B946BBA4B8D7A74)

-   After the FaultLogExtensionAbility is started, the fault handling can be completed only in a short period of time. It is recommended that the handling time be less than 10 seconds. If the handling is not complete within the timeout interval, you can save the status in [onDisconnect](#ondisconnect).
-   The timer starts when the application triggers a crash or freeze event for the first time after the device is powered on or FaultLogExtensionAbility is started last time. When a crash or screen freeze event is repeatedly triggered before FaultLogExtensionAbility is started, the timer will not restart.
-   If FaultLogExtensionAbility crashes, it will not be restarted by the system service.

#### \[h2\]Properties

**System capability**: SystemCapability.HiviewDFX.Hiview.FaultLogger

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| context | [FaultLogExtensionContext](../ohos-hiviewdfx-faultlogextensioncontext-delayed-fault-notification-context/document.md) | No | No | Context of the FaultLogExtensionAbility. This context is inherited from [ExtensionContext](../../../../../application-framework/ability-kit/arkts-apis/dependent-elements-and-definitions/application/extensioncontext/document.md). |

#### \[h2\]onConnect

onConnect(): void

Called to perform the initialization operation when the system service completes the connection. This API can be overridden selectively.

**System capability**: SystemCapability.HiviewDFX.Hiview.FaultLogger

**Example**

export default class MyFaultLogExtension extends FaultLogExtensionAbility {
    onConnect() {
      console.info('onConnect');
    }
}

#### \[h2\]onDisconnect

onDisconnect(): void

Called to release resources and clear the running status when the system service completes the disconnection. This API can be overridden selectively.

**System capability**: SystemCapability.HiviewDFX.Hiview.FaultLogger

**Example**

export default class MyFaultLogExtension extends FaultLogExtensionAbility {
    onDisconnect() {
      console.info('onDisconnect');
    }
}

#### \[h2\]onFaultReportReady

onFaultReportReady(): void

Called to subscribe to and process fault events when the system service notifies the FaultLogExtensionAbility to process faults.

**System capability**: SystemCapability.HiviewDFX.Hiview.FaultLogger

**Example**

import { hiAppEvent } from '@kit.PerformanceAnalysisKit';

export default class MyFaultLogExtension extends FaultLogExtensionAbility {
    onFaultReportReady() {
        hiAppEvent.addWatcher({
            name: "watcher",
            appEventFilters: \[
                {
                    domain: hiAppEvent.domain.OS,
                    names: \[hiAppEvent.event.APP\_CRASH, hiAppEvent.event.APP\_FREEZE\]
                }
            \],
            onReceive: (domain: string, appEventGroups: Array<hiAppEvent.AppEventGroup>) => {
                // Process the fault event.
            }
        });
    }
}

#### Appendix

The following table lists the APIs that cannot be called by this module.

| Kit | Module |
| :-- | :-- |
| AVSessionKit | [@ohos.multimedia.avsession (AVSession Management)](../../../../../media/avsession-kit/arkts-apis/ohos-multimedia-avsession-avsession-management/module-description/document.md) |
| AbilityKit | [@ohos.UIAbilityContext](../../../../../application-framework/ability-kit/arkts-apis/dependent-elements-and-definitions/application/uiabilitycontext/document.md) |
| ArkUI | [@ohos.window (Window)](../../../../../application-framework/arkui/arkts-api/window-manager/ohos-window-window/module-description/document.md) |
| AudioKit | [@ohos.multimedia.audio (Audio Management)](../../../../../media/audio-kit/arkts-apis/ohos-multimedia-audio-audio-management/module-description/document.md) |
| BackgroundTasksKit | [@ohos.backgroundTaskManager (Background Task Management)](../../../../../application-framework/background-tasks-kit/arkts-apis/apis-no-longer-maintained/ohos-backgroundtaskmanager-background-task-management/document.md) |
| BackgroundTasksKit | [@ohos.reminderAgent (reminderAgent)](../../../../../application-framework/background-tasks-kit/arkts-apis/apis-no-longer-maintained/ohos-reminderagent-agent-powered-reminder/document.md) |
| BackgroundTasksKit | [@ohos.reminderAgentManager (Agent-Powered Reminders)](../../../../../application-framework/background-tasks-kit/arkts-apis/ohos-reminderagentmanager-agent-powered-reminder/document.md) |
| BackgroundTasksKit | [@ohos.resourceschedule.backgroundTaskManager (Background Task Management)](../../../../../application-framework/background-tasks-kit/arkts-apis/ohos-resourceschedule-backgroundtaskmanager-background-task-management/document.md) |
| BasicServicesKit | [@ohos.power (System Power Management)](../../../../basic-functions/basic-services-kit/arkts-apis/device-management/ohos-power-power-management/document.md) |
| BasicServicesKit | [@ohos.wallpaper (Wallpaper)](../../../../basic-functions/basic-services-kit/arkts-apis/others/ohos-wallpaper-wallpaper/document.md) |
| CameraKit | [@ohos.multimedia.camera (Camera Management)](../../../../../media/camera-kit/arkts-apis/ohos-multimedia-camera-camera-management/module-description/document.md) |
| CameraKit | [@ohos.multimedia.cameraPicker (Camera Picker)](../../../../../media/camera-kit/arkts-apis/ohos-multimedia-camerapicker-camera-picker/document.md) |
| ConnectivityKit | [@ohos.wifiManager (WLAN)](../../../../network/connectivity-kit/arkts-apis/ohos-wifimanager-wlan/document.md) |
| ConnectivityKit | [@ohos.wifiManagerExt (WLAN Extension)](../../../../network/connectivity-kit/arkts-apis/ohos-wifimanagerext-wlan-extension/document.md) |
| ConnectivityKit | [@ohos.wifiext (WLAN Extension)](../../../../network/connectivity-kit/apis-no-longer-maintained/ohos-wifiext-wlan-extension/document.md) |
| IMEKit | [@ohos.inputMethod (Input Method Framework)](../../../../../application-framework/ime-kit/arkts-apis/ohos-inputmethod-input-method-framework/document.md) |
| MediaLibraryKit | [@ohos.multimedia.movingphotoview (MovingPhotoView)](../../../../../media/media-library-kit/arkts-components/ohos-multimedia-movingphotoview-movingphotoview/document.md) |
| NotificationKit | [@ohos.notification (Notification)](../../../../../application-services/notification-kit/arkts-apis/apis-no-longer-maintained/ohos-notification-notification/document.md) |
| NotificationKit | [@ohos.notificationManager (NotificationManager)](../../../../../application-services/notification-kit/arkts-apis/ohos-notificationmanager-notificationmanager/document.md) |
| SensorServiceKit | [@ohos.vibrator (Vibrator)](../../../../hardware/sensor-service-kit/arkts-api/ohos-vibrator-vibrator/document.md) |
| TelephonyKit | [@ohos.telephony.call (Call)](../../../../network/telephony-kit/arkts-api/ohos-telephony-call-call/document.md) |
| TelephonyKit | [@ohos.telephony.sim (SIM Management)](../../../../network/telephony-kit/arkts-api/ohos-telephony-sim-sim-management/document.md) |
| TelephonyKit | [@ohos.telephony.sms (SMS)](../../../../network/telephony-kit/arkts-api/ohos-telephony-sms-sms/document.md) |
| UserAuthenticationKit | [@ohos.userIAM.userAuth (User Authentication)](../../../../security/user-authentication-kit/arkts-apis/ohos-useriam-userauth-user-authentication/document.md) |
