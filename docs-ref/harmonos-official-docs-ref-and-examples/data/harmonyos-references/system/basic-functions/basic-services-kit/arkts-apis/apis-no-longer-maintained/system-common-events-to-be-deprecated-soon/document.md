# System Common Events (To Be Deprecated Soon)

This document provides indexes for predefined system common events.

Common event types are defined in [Support enumeration of the ohos.commonEvent module](../ohos-commonevent-common-event/document.md#support).

**System capability**: SystemCapability.Notification.CommonEvent

-   **COMMON\_EVENT\_BOOT\_COMPLETED(deprecated)** indicates that the boot is complete and the system is loaded.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/21/v3/z0Mc4ZgQS8uzW0Hygm5riw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062358Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=88FD2C405668E8108747FA77BDAB759C90BE4C6ADD9BA4AC11EE150379AF2DC9)
    
    This type is supported since API version 7 and deprecated since API version 9. You are advised to use **COMMON\_EVENT\_BOOT\_COMPLETED** instead.
    
    -   Value: **usual.event.BOOT\_COMPLETED**
    -   Required permissions: **ohos.permission.RECEIVER\_STARTUP\_COMPLETED** (for system applications only)
-   **COMMON\_EVENT\_LOCKED\_BOOT\_COMPLETED(deprecated)** (reserved, not supported yet) indicates that the guidance is complete and the system is loaded, but the screen is still locked.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3a/v3/TLpPnSw1TUyeX1k6WApsrw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062358Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=45C6BC002DB8FB742C263967AF466C9AFB61811D8C874E17E0739E1A3FAF9279)
    
    This type is supported since API version 7 and deprecated since API version 9. You are advised to use [COMMON\_EVENT\_LOCKED\_BOOT\_COMPLETED](../../process-and-thread-communication/system-common-events/document.md#common_event_locked_boot_completed) instead.
    
    -   Value: **usual.event.LOCKED\_BOOT\_COMPLETED**
    -   Required permissions: none
-   **COMMON\_EVENT\_SHUTDOWN(deprecated)** indicates that the device is being shut down and will continue until it is finally shut down.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/80/v3/PW16gfqOQ9ScopLKTeJO8A/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062358Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=C5EF8E00C4FAEE5AE71BB9619EC67F16DC967A711172C75320E6D79F0ABD9018)
    
    This type is supported since API version 7 and deprecated since API version 9. You are advised to use [COMMON\_EVENT\_SHUTDOWN](../../process-and-thread-communication/system-common-events/document.md#common_event_shutdown) instead.
    
    -   Value: **usual.event.SHUTDOWN**
    -   Required permissions: none
-   **COMMON\_EVENT\_BATTERY\_CHANGED(deprecated)** indicates that the battery charging status, battery level, and other information has changed.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/df/v3/Lg82cMT2TCygTW-06VW8SQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062358Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=4224D2BA86255E58A355BD63DC473E1937D8E34559A9B182A8AB0B23CA7DAB36)
    
    This type is supported since API version 7 and deprecated since API version 9. You are advised to use [COMMON\_EVENT\_BATTERY\_CHANGED](../../process-and-thread-communication/system-common-events/document.md#common_event_battery_changed) instead.
    
    -   Value: **usual.event.BATTERY\_CHANGED**
    -   Required permissions: none
-   **COMMON\_EVENT\_BATTERY\_LOW(deprecated)** indicates that the battery level is low.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/92/v3/D6LRvfvdTga4uTNA-7OB0w/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062358Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=07CB59E5904DFC6AA1D5511E3AC734D6AA5369FA361CE6383A891B7F98DCDBB4)
    
    This type is supported since API version 7 and deprecated since API version 9. You are advised to use [COMMON\_EVENT\_BATTERY\_LOW](../../process-and-thread-communication/system-common-events/document.md#common_event_battery_low) instead.
    
    -   Value: **usual.event.BATTERY\_LOW**
    -   Required permissions: none
-   **COMMON\_EVENT\_BATTERY\_OKAY(deprecated)** indicates that the battery level is normal.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2b/v3/zytvzKPPRsOjdp8ndi42yQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062358Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=D3111C48DC101487568E49C0AD9D5E01B4306C9FE4FA7C371805383C45D81162)
    
    This type is supported since API version 7 and deprecated since API version 9. You are advised to use [COMMON\_EVENT\_BATTERY\_OKAY](../../process-and-thread-communication/system-common-events/document.md#common_event_battery_okay) instead.
    
    -   Value: **usual.event.BATTERY\_OKAY**
    -   Required permissions: none
-   **COMMON\_EVENT\_POWER\_CONNECTED(deprecated)** indicates that the device is connected to an external power supply.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3e/v3/NNvaErsoTp2h0P664M4TRQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062358Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=F228749D6E6D4CDB749546D95D988F4355609968F7AEFD90F64001E0462F4A72)
    
    This type is supported since API version 7 and deprecated since API version 9. You are advised to use [COMMON\_EVENT\_POWER\_CONNECTED](../../process-and-thread-communication/system-common-events/document.md#common_event_power_connected) instead.
    
    -   Value: **usual.event.POWER\_CONNECTED**
    -   Required permissions: none
-   **COMMON\_EVENT\_POWER\_DISCONNECTED(deprecated)** indicates that the device is disconnected from the external power supply.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/93/v3/ZoMpGInrQ3GD5nhS88GUCg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062358Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=D7CA8870D2929D8DB6D9BF067219BA650BF8541554684F833EAAF469F37FBDF9)
    
    This type is supported since API version 7 and deprecated since API version 9. You are advised to use [COMMON\_EVENT\_POWER\_DISCONNECTED](../../process-and-thread-communication/system-common-events/document.md#common_event_power_disconnected) instead.
    
    -   Value: **usual.event.POWER\_DISCONNECTED**
    -   Required permissions: none
-   **COMMON\_EVENT\_SCREEN\_OFF(deprecated)** indicates that the device screen is off and the device is in sleep mode.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1c/v3/XCrcCA0aQG-mXpKUllaLiw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062358Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=42CEF7417D3646926230EA4C0084C4318313BE88D5B17C988914BB67A91200D6)
    
    This type is supported since API version 7 and deprecated since API version 9. You are advised to use [COMMON\_EVENT\_SCREEN\_OFF](../../process-and-thread-communication/system-common-events/document.md#common_event_screen_off) instead.
    
    -   Value: **usual.event.SCREEN\_OFF**
    -   Required permissions: none
-   **COMMON\_EVENT\_SCREEN\_ON(deprecated)** indicates that the device screen is on and the device is in interactive state.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cc/v3/r7sgzSvmTzS2mwBPcAbOLg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062358Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=AD68ED75939CEF7F3DA44B2BE79C7CA070758824EB1CE988CEF20026D0DC993D)
    
    This type is supported since API version 7 and deprecated since API version 9. You are advised to use [COMMON\_EVENT\_SCREEN\_ON](../../process-and-thread-communication/system-common-events/document.md#common_event_screen_on) instead.
    
    -   Value: **usual.event.SCREEN\_ON**
    -   Required permissions: none
-   **COMMON\_EVENT\_THERMAL\_LEVEL\_CHANGED(deprecated)** indicates that the device thermal level has changed.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/de/v3/74W8FLkPRlyOhJB67_ulgw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062358Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=7388FAE8F6CD3DCE85501D0FCB3BC2EE501433A6BAB45782B369F132F24719FB)
    
    This type is supported since API version 8 and deprecated since API version 9. You are advised to use [COMMON\_EVENT\_THERMAL\_LEVEL\_CHANGED](../../process-and-thread-communication/system-common-events/document.md#common_event_thermal_level_changed) instead.
    
    -   Value: **usual.event.THERMAL\_LEVEL\_CHANGED**
    -   Required permissions: none
-   **COMMON\_EVENT\_USER\_PRESENT(deprecated)** (reserved, not supported yet) indicates that the user unlocks the device.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/25/v3/vrzJoRprQp-FidBuuj4o3Q/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062358Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=ED8796A3CAFC94578ED5F0B5EB34923A2FA5A008D3B13BEF04738251A8B982AB)
    
    This type is supported since API version 7 and deprecated since API version 9. You are advised to use [COMMON\_EVENT\_USER\_PRESENT](../../process-and-thread-communication/system-common-events/document.md#common_event_user_presentdeprecated) instead.
    
    -   Value: **usual.event.USER\_PRESENT**
    -   Required permissions: none
-   **COMMON\_EVENT\_TIME\_TICK(deprecated)** indicates that the system time has changed as time ticks by.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d2/v3/P7FWye7LTim_LspshltkZg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062358Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=1DC09454A25722335F65DEA0BDB2626E180A4BFD4E3E0FB57508057438BEEE66)
    
    This type is supported since API version 7 and deprecated since API version 9. You are advised to use [COMMON\_EVENT\_TIME\_TICK](../../process-and-thread-communication/system-common-events/document.md#common_event_time_tick) instead.
    
    -   Value: **usual.event.TIME\_TICK**
    -   Required permissions: none
-   **COMMON\_EVENT\_TIME\_CHANGED(deprecated)** indicates that the system time is set.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/40/v3/M9xqvw8nRNaxCQdcNMdTLA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062358Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=51474923D4CA7D8B7EBC76B6458067062A94F5A9952C082C08BCBF0EE0AAA64D)
    
    This type is supported since API version 7 and deprecated since API version 9. You are advised to use [COMMON\_EVENT\_TIME\_CHANGED](../../process-and-thread-communication/system-common-events/document.md#common_event_time_changed) instead.
    
    -   Value: **usual.event.TIME\_CHANGED**
    -   Required permissions: none
-   **COMMON\_EVENT\_DATE\_CHANGED(deprecated)** (reserved, not supported yet) indicates that the system date has been changed.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/66/v3/K3gCd-eESCaBuUcac_YvVg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062358Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=AE1CFD4FC99BDFF118E258E4F59A03E0D75D8833B58AC6AB4BC8C59B1C17C745)
    
    This type is supported since API version 7 and deprecated since API version 9. You are advised to use [COMMON\_EVENT\_DATE\_CHANGED](../../process-and-thread-communication/system-common-events/document.md#common_event_date_changed) instead.
    
    -   Value: **usual.event.DATE\_CHANGED**
    -   Required permissions: none
-   **COMMON\_EVENT\_TIMEZONE\_CHANGED(deprecated)** indicates that the system time zone is changed.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/31/v3/fwXIYNWQQgmkvZOcfWNTJg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062358Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=DB776071BD75454CADA1CE5F087AE77DC65F8F167FD9E90EEA200F8865452BDD)
    
    This type is supported since API version 7 and deprecated since API version 9. You are advised to use [COMMON\_EVENT\_TIMEZONE\_CHANGED](../../process-and-thread-communication/system-common-events/document.md#common_event_timezone_changed) instead.
    
    -   Value: **usual.event.TIMEZONE\_CHANGED**
    -   Required permissions: none
-   **COMMON\_EVENT\_CLOSE\_SYSTEM\_DIALOGS(deprecated)** (reserved, not supported yet) indicates that the user closes a temporary system dialog box.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b5/v3/t-XSTinaRFiqmUYZw5nxeQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062358Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=D5601531CF79F5DA21FCDEC59DC28A18D7E3AF12744428E6E5F7F811CF596132)
    
    This type is supported since API version 7 and deprecated since API version 9. You are advised to use [COMMON\_EVENT\_CLOSE\_SYSTEM\_DIALOGS](../../process-and-thread-communication/system-common-events/document.md#common_event_close_system_dialogs) instead.
    
    -   Value: **usual.event.CLOSE\_SYSTEM\_DIALOGS**
    -   Required permissions: none
-   **COMMON\_EVENT\_PACKAGE\_ADDED(deprecated)** indicates that a new application package has been installed on the device.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c0/v3/0GKN1q1FT1mBtV2tP5_QSw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062358Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=D9CB7843022FE2F1FA8EF0D87A81BFA3D5BF5F8D83CAC15626F948FCC5810C23)
    
    This type is supported since API version 7 and deprecated since API version 9. You are advised to use [COMMON\_EVENT\_PACKAGE\_ADDED](../../process-and-thread-communication/system-common-events/document.md#common_event_package_added) instead.
    
    -   Value: **usual.event.PACKAGE\_ADDED**
    -   Required permissions: none
-   **COMMON\_EVENT\_PACKAGE\_REPLACED(deprecated)** (reserved, not supported yet) indicates that a later version of an installed application package has replaced the previous one on the device.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ff/v3/29Iu31QuQyafDY9ayjJjBQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062358Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=5566973FC7B8F5189154B26FAEA9FD34A4BA546891B08C19735872E88D9A0164)
    
    This type is supported since API version 7 and deprecated since API version 9. You are advised to use [COMMON\_EVENT\_PACKAGE\_REPLACED](../../process-and-thread-communication/system-common-events/document.md#common_event_package_replaced) instead.
    
    -   Value: **usual.event.PACKAGE\_REPLACED**
    -   Required permissions: none
-   **COMMON\_EVENT\_MY\_PACKAGE\_REPLACED(deprecated)** (reserved, not supported yet) indicates that the new version of the application package has replaced the previous version.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/30/v3/pl4_EkaKRJqZS-6BAIBejQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062358Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=DE378936FF03A9E47756BD5C3CA95B729369C206DC92706FB68B21AAE8234E85)
    
    This type is supported since API version 7 and deprecated since API version 9. You are advised to use [COMMON\_EVENT\_MY\_PACKAGE\_REPLACED](../../process-and-thread-communication/system-common-events/document.md#common_event_my_package_replaced) instead.
    
    -   Value: **usual.event.MY\_PACKAGE\_REPLACED**
    -   Required permissions: none
-   **COMMON\_EVENT\_PACKAGE\_REMOVED(deprecated)** indicates that an installed application has been uninstalled from the device with the application data retained.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f2/v3/_M0FGdiHRVqNw5NeRuFfxQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062358Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=C6EC626F8F1CB1BD83BD56EA8783A55FC693CF61761BDF6658040C168245B3DB)
    
    This type is supported since API version 7 and deprecated since API version 9. You are advised to use [COMMON\_EVENT\_PACKAGE\_REMOVED](../../process-and-thread-communication/system-common-events/document.md#common_event_package_removed) instead.
    
    -   Value: **usual.event.PACKAGE\_REMOVED**
    -   Required permissions: none
-   **COMMON\_EVENT\_BUNDLE\_REMOVED(deprecated)** (reserved, not supported yet) indicates that an installed bundle has been uninstalled from the device with the application data retained.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7/v3/XlcjB-eeRGSNkiQZvycp7Q/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062358Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=F54216EA07DD4BB43AF5935569AB5E2530CF832DBBF4A4F9B32D037112FA6F3D)
    
    This type is supported since API version 7 and deprecated since API version 9. You are advised to use [COMMON\_EVENT\_BUNDLE\_REMOVED](../../process-and-thread-communication/system-common-events/document.md#common_event_bundle_removed) instead.
    
    -   Value: **usual.event.BUNDLE\_REMOVED**
    -   Required permissions: none
-   **COMMON\_EVENT\_PACKAGE\_FULLY\_REMOVED(deprecated)** (reserved, not supported yet) indicates that an installed application, including both the application data and code, has been completely uninstalled from the device.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b1/v3/ptO6h4-7Rs6441gNA3PbNw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062358Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=A0645B404C666398031918A7EECF14755E32F6A3EA366782E4EA90FD9C0C0E8B)
    
    This type is supported since API version 7 and deprecated since API version 9. You are advised to use [COMMON\_EVENT\_PACKAGE\_FULLY\_REMOVED](../../process-and-thread-communication/system-common-events/document.md#common_event_package_fully_removed) instead.
    
    -   Value: **usual.event.PACKAGE\_FULLY\_REMOVED**
    -   Required permissions: none
-   **COMMON\_EVENT\_PACKAGE\_CHANGED(deprecated)** indicates that an application package has been changed (for example, an ability in the package has been enabled or disabled).
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9c/v3/XE8TjMBCTWS-8O4_pvAHNQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062358Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=B5727A9E9F987EDCB4282D9CFF2F57E696651FEFF4CE058DD208963233300B02)
    
    This type is supported since API version 7 and deprecated since API version 9. You are advised to use [COMMON\_EVENT\_PACKAGE\_CHANGED](../../process-and-thread-communication/system-common-events/document.md#common_event_package_changed) instead.
    
    -   Value: **usual.event.PACKAGE\_CHANGED**
    -   Required permissions: none
-   **COMMON\_EVENT\_PACKAGE\_RESTARTED(deprecated)** indicates that the user closed all processes of the application and restarted the application.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6a/v3/-TATkANvTfK3WrbW2RphWg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062358Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=A1EA9C4BDBC6D5584EF029D1804C3B93D7987FC0A40421595FA72F23B9EFE3CF)
    
    This type is supported since API version 7 and deprecated since API version 9. You are advised to use [COMMON\_EVENT\_PACKAGE\_RESTARTED](../../process-and-thread-communication/system-common-events/document.md#common_event_package_restarted) instead.
    
    -   Value: **usual.event.PACKAGE\_RESTARTED**
    -   Required permissions: none
-   **COMMON\_EVENT\_PACKAGE\_DATA\_CLEARED(deprecated)** indicates that the user cleared the application package data.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/90/v3/3Cyikhc4TJCMkUAfvvkWpw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062358Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=AB91F7D1A03744BB8351028AC501391D90A8766301D07F5FFE6EC8D69B75488C)
    
    This type is supported since API version 7 and deprecated since API version 9. You are advised to use [COMMON\_EVENT\_PACKAGE\_DATA\_CLEARED](../../process-and-thread-communication/system-common-events/document.md#common_event_package_data_cleared) instead.
    
    -   Value: **usual.event.PACKAGE\_DATA\_CLEARED**
    -   Required permissions: none
-   **COMMON\_EVENT\_PACKAGES\_SUSPENDED(deprecated)** (reserved, not supported yet) indicates that application packages have been suspended.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b1/v3/l34PzJOrT2udqT4aULazSA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062358Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=C74B1D61C01BB9E30799736F572697387C9402D7FC2366CA661C2D0C8F2EF388)
    
    This type is supported since API version 7 and deprecated since API version 9. You are advised to use [COMMON\_EVENT\_PACKAGES\_SUSPENDED](../../process-and-thread-communication/system-common-events/document.md#common_event_packages_suspended) instead.
    
    -   Value: **usual.event.PACKAGES\_SUSPENDED**
    -   Required permissions: none
-   **COMMON\_EVENT\_PACKAGES\_UNSUSPENDED(deprecated)** (reserved, not supported yet) indicates that the application HAP package is not suspended (resumed from the suspended state).
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/42/v3/HAmSnvUTQWuCEDHPpseAOQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062358Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=B43E5EC88CA90402C728A84B5DEE7C6719AB9708BE3A0EDD7EC06AAB25EA43B4)
    
    This type is supported since API version 7 and deprecated since API version 9. You are advised to use [COMMON\_EVENT\_PACKAGES\_UNSUSPENDED](../../process-and-thread-communication/system-common-events/document.md#common_event_packages_unsuspended) instead.
    
    -   Value: **usual.event.PACKAGES\_UNSUSPENDED**
    -   Required permissions: none
-   **COMMON\_EVENT\_MY\_PACKAGE\_SUSPENDED(deprecated)** indicates that the application HAP package is suspended.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/24/v3/5TiyklMlRl2-VFU2wu1qlA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062358Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=25FD7D334E8ADD6020DD40FCCBFD9C534E1DDD549C74451C5A3BBCA1CF9853EE)
    
    This type is supported since API version 7 and deprecated since API version 9. You are advised to use [COMMON\_EVENT\_MY\_PACKAGE\_SUSPENDED](../../process-and-thread-communication/system-common-events/document.md#common_event_my_package_suspended) instead.
    
    -   Value: **usual.event.MY\_PACKAGE\_SUSPENDED**
    -   Required permissions: none
-   **COMMON\_EVENT\_MY\_PACKAGE\_UNSUSPENDED(deprecated)** indicates that the application package is not suspended.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3d/v3/7TT9njuFStG6bs2S7n5ZaQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062358Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=29C94BEFB4F6ABD5DA719875FED46D4EB413F5645787E2FF6520130D8F1ECE00)
    
    This type is supported since API version 7 and deprecated since API version 9. You are advised to use [COMMON\_EVENT\_MY\_PACKAGE\_UNSUSPENDED](../../process-and-thread-communication/system-common-events/document.md#common_event_my_package_unsuspended) instead.
    
    -   Value: **usual.event.MY\_PACKAGE\_UNSUSPENDED**
    -   Required permissions: none
-   **COMMON\_EVENT\_UID\_REMOVED(deprecated)** (reserved, not supported yet) indicates that a user ID has been removed from the system.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ad/v3/KenUJyQIRNyyfg7oKeTc0w/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062358Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=66DB31D1E3F9F1D8C234BCC0B8068989B2C2DD5454039DC3CCF3E5675AD0383B)
    
    This type is supported since API version 7 and deprecated since API version 9. You are advised to use [COMMON\_EVENT\_UID\_REMOVED](../../process-and-thread-communication/system-common-events/document.md#common_event_uid_removed) instead.
    
    -   Value: **usual.event.UID\_REMOVED**
    -   Required permissions: none
-   **COMMON\_EVENT\_PACKAGE\_FIRST\_LAUNCH(deprecated)** (reserved, not supported yet) indicates that an installed application is started for the first time.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/75/v3/fmmJEMZhRrWRtG_t5gA7Gw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062358Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=910F56E684255CFA6556AEFFF149AF28152868468AFF17EE2C4296776F333BF7)
    
    This type is supported since API version 7 and deprecated since API version 9. You are advised to use [COMMON\_EVENT\_PACKAGE\_FIRST\_LAUNCH](../../process-and-thread-communication/system-common-events/document.md#common_event_package_first_launch) instead.
    
    -   Value: **usual.event.PACKAGE\_FIRST\_LAUNCH**
    -   Required permissions: none
-   **COMMON\_EVENT\_PACKAGE\_NEEDS\_VERIFICATION(deprecated)** (reserved, not supported yet) indicates that an application requires system verification.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/70/v3/3YNqrYPiRQu4m-fdlEzTog/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062358Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=45D22E7B203823FB10F872B566BDAC50F88675D5CB31FA5480D33C0B047D9D43)
    
    This type is supported since API version 7 and deprecated since API version 9. You are advised to use [COMMON\_EVENT\_PACKAGE\_NEEDS\_VERIFICATION](../../process-and-thread-communication/system-common-events/document.md#common_event_package_needs_verification) instead.
    
    -   Value: **usual.event.PACKAGE\_NEEDS\_VERIFICATION**
    -   Required permissions: none
-   **COMMON\_EVENT\_PACKAGE\_VERIFIED(deprecated)** (reserved, not supported yet) indicates that an application has been verified by the system.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/21/v3/K-RZq5GaShKeds6qjCfAKw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062358Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=EBC59B7E99E349F65BBF0AE7841F57E9BF71D6630A2DC00C4AFE9860202CBF0F)
    
    This type is supported since API version 7 and deprecated since API version 9. You are advised to use [COMMON\_EVENT\_PACKAGE\_VERIFIED](../../process-and-thread-communication/system-common-events/document.md#common_event_package_verified) instead.
    
    -   Value: **usual.event.PACKAGE\_VERIFIED**
    -   Required permissions: none
-   **COMMON\_EVENT\_EXTERNAL\_APPLICATIONS\_AVAILABLE(deprecated)** (reserved, not supported yet) indicates that applications installed on the external storage are available for the system.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4c/v3/GQnvu0iwQy2vdjTspiEinQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062358Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=3CD9069E8DE39BA4376649CC4DA73EE8DDB83FCD29B9D7DBB904063E338149CC)
    
    This type is supported since API version 7 and deprecated since API version 9. You are advised to use [COMMON\_EVENT\_EXTERNAL\_APPLICATIONS\_AVAILABLE](../../process-and-thread-communication/system-common-events/document.md#common_event_external_applications_available) instead.
    
    -   Value: **usual.event.EXTERNAL\_APPLICATIONS\_AVAILABLE**
    -   Required permissions: none
-   **COMMON\_EVENT\_EXTERNAL\_APPLICATIONS\_UNAVAILABLE(deprecated)** (reserved, not supported yet) indicates that applications installed on the external storage are not available for the system.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d8/v3/wbRghy_6ROaqPC0RDdi3sw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062358Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=AEBE953A9FAD9D471F6458E386EB5ED76A58006D4D080C0C804D111A1F8B6747)
    
    This type is supported since API version 7 and deprecated since API version 9. You are advised to use [COMMON\_EVENT\_EXTERNAL\_APPLICATIONS\_UNAVAILABLE](../../process-and-thread-communication/system-common-events/document.md#common_event_external_applications_unavailable) instead.
    
    -   Value: **usual.event.EXTERNAL\_APPLICATIONS\_UNAVAILABLE**
    -   Required permissions: none
-   **COMMON\_EVENT\_CONFIGURATION\_CHANGED(deprecated)** (reserved, not supported yet) indicates that the device state (for example, orientation and locale) has changed.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9e/v3/7nFCsGxsTO2dVBHQuSXBfw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062358Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=285EF6075B9322FA068889E8906919BC42AA12446F5C23D220C6EE062F26519F)
    
    This type is supported since API version 7 and deprecated since API version 9. You are advised to use [COMMON\_EVENT\_CONFIGURATION\_CHANGED](../../process-and-thread-communication/system-common-events/document.md#common_event_configuration_changed) instead.
    
    -   Value: **usual.event.CONFIGURATION\_CHANGED**
    -   Required permissions: none
-   **COMMON\_EVENT\_LOCALE\_CHANGED(deprecated)** (reserved, not supported yet) indicates that the device locale has changed.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a3/v3/mtb3nce2SOugaooAvsSflw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062358Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=18339E9BFA4113CCFD4058034EB67ED98163BDA909EBF90E871BFCC63A90E97D)
    
    This type is supported since API version 7 and deprecated since API version 9. You are advised to use [COMMON\_EVENT\_LOCALE\_CHANGED](../../process-and-thread-communication/system-common-events/document.md#common_event_locale_changed) instead.
    
    -   Value: **usual.event.LOCALE\_CHANGED**
    -   Required permissions: none
-   **COMMON\_EVENT\_MANAGE\_PACKAGE\_STORAGE(deprecated)** (reserved, not supported yet) indicates that the device storage is insufficient.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/09/v3/ZKj-F-ZuR-KV956uuNn88g/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062358Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=D9D4CE8CEE386120B22D6604F795C6A64971ABA1E52406E62E0184F13DA88D70)
    
    This type is supported since API version 7 and deprecated since API version 9. You are advised to use [COMMON\_EVENT\_MANAGE\_PACKAGE\_STORAGE](../../process-and-thread-communication/system-common-events/document.md#common_event_manage_package_storage) instead.
    
    -   Value: **usual.event.MANAGE\_PACKAGE\_STORAGE**
    -   Required permissions: none
-   **COMMON\_EVENT\_DRIVE\_MODE(deprecated)** (reserved, not supported yet) indicates that the system is in driving mode.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3d/v3/gLMh7lGaQFCqtPAaxamMAg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062358Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=5CAED3174727F4B5BA5EFEC7CEA51D0A012DD13F34F17012A629A7853455B4C2)
    
    This type is supported since API version 7 and deprecated since API version 9. You are advised to use [COMMON\_EVENT\_DRIVE\_MODE](../../process-and-thread-communication/system-common-events/document.md#common_event_drive_mode) instead.
    
    -   Value: **common.event.DRIVE\_MODE**
    -   Required permissions: none
-   **COMMON\_EVENT\_HOME\_MODE(deprecated)** (reserved, not supported yet) indicates that the system is in home mode.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f5/v3/LeExUb3pQAqmnIWyISXnQg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062358Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=DC9C6B080AAEB4C87C7B279B1728C31501E853DEAA5527E4DEE0E7384D48D87D)
    
    This type is supported since API version 7 and deprecated since API version 9. You are advised to use [COMMON\_EVENT\_HOME\_MODE](../../process-and-thread-communication/system-common-events/document.md#common_event_home_mode) instead.
    
    -   Value: **common.event.HOME\_MODE**
    -   Required permissions: none
-   **COMMON\_EVENT\_OFFICE\_MODE(deprecated)** (reserved, not supported yet) indicates that the system is in office mode.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/56/v3/l_6LFRWeQyqcnwmcbU4OKw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062358Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=67419C4E875FD0D526D30E5A0AC64EDFE4715B95803F889066CA848215FD72EE)
    
    This type is supported since API version 7 and deprecated since API version 9. You are advised to use [COMMON\_EVENT\_OFFICE\_MODE](../../process-and-thread-communication/system-common-events/document.md#common_event_office_mode) instead.
    
    -   Value: **common.event.OFFICE\_MODE**
    -   Required permissions: none
-   **COMMON\_EVENT\_USER\_STARTED(deprecated)** (reserved, not supported yet) indicates that the user has been started.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/01/v3/1K-jXF52SSOVTEye33d3kw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062358Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=759C2C353CD7585D79309CB4C1B693F7AC0A65D95D310BEC93E6505187C0E5E8)
    
    This type is supported since API version 7 and deprecated since API version 9. You are advised to use [COMMON\_EVENT\_USER\_STARTED](../../process-and-thread-communication/system-common-events/document.md#common_event_user_started) instead.
    
    -   Value: **usual.event.USER\_STARTED**
    -   Required permissions: none
-   **COMMON\_EVENT\_USER\_BACKGROUND(deprecated)** (reserved, not supported yet) indicates that the user has been brought to the background.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4e/v3/4Ge6aQ8HT2-CmXWHWWJJmg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062358Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=CE93BE4FED2978D942CDB57D34D3A07FA48A1962A2D347BB7A6DA1D6F1E1CE13)
    
    This type is supported since API version 7 and deprecated since API version 9. You are advised to use [COMMON\_EVENT\_USER\_BACKGROUND](../../process-and-thread-communication/system-common-events/document.md#common_event_user_background) instead.
    
    -   Value: **usual.event.USER\_BACKGROUND**
    -   Required permissions: none
-   **COMMON\_EVENT\_USER\_FOREGROUND(deprecated)** (reserved, not supported yet) indicates that the user has been brought to the foreground.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/97/v3/TCLty0VrSIaa1G0KVvGbfQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062358Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=3E15D179AFEF4A6B9C4CF1D5172CF6D915886C085FBB4EBD6F9BF52BF35FAFAD)
    
    This type is supported since API version 7 and deprecated since API version 9. You are advised to use [COMMON\_EVENT\_USER\_FOREGROUND](../../process-and-thread-communication/system-common-events/document.md#common_event_user_foreground) instead.
    
    -   Value: **usual.event.USER\_FOREGROUND**
    -   Required permissions: none
-   **COMMON\_EVENT\_USER\_SWITCHED(deprecated)** indicates that user switching is in progress.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e9/v3/vaLk9VRMTJ6o_11E0hAEQg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062358Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=CCDD193FB032A6D873806C00DDD5D1D3E2E00DE0B6BB3FBF3C1068788EFE4DA5)
    
    This type is supported since API version 7 and deprecated since API version 9. You are advised to use **COMMON\_EVENT\_USER\_SWITCHED** instead.
    
    -   Value: **usual.event.USER\_SWITCHED**
    -   Required permissions: **ohos.permission.MANAGE\_LOCAL\_ACCOUNTS** (for system applications only)
-   **COMMON\_EVENT\_USER\_STARTING(deprecated)** (reserved, not supported yet) indicates that user starting is in progress.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/dc/v3/pXKqaSIgRh6nxDGrLcnabQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062358Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=75D29FA4D45ADB78D7BE4FB69EDB18134F1D2B562EB4E6F654A05E87044B953D)
    
    This type is supported since API version 7 and deprecated since API version 9. You are advised to use [COMMON\_EVENT\_USER\_STARTING](../../process-and-thread-communication/system-common-events/document.md#common_event_user_starting) instead.
    
    -   Value: **usual.event.USER\_STARTING**
    -   Required permissions: **ohos.permission.INTERACT\_ACROSS\_LOCAL\_ACCOUNTS** (for system applications only)
-   **COMMON\_EVENT\_USER\_UNLOCKED(deprecated)** (reserved, not supported yet) indicates that the credential encryption storage of the current user has been unlocked upon restart.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f0/v3/u_meIMD7QsK5nQ5r11C6_w/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062358Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=2F99F01AC2C484B172D92BA48DD452A57595B9B70727E791FF70CE4A7649EA4A)
    
    This type is supported since API version 7 and deprecated since API version 9. You are advised to use [COMMON\_EVENT\_USER\_UNLOCKED](../../process-and-thread-communication/system-common-events/document.md#common_event_user_unlocked) instead.
    
    -   Value: **usual.event.USER\_UNLOCKED**
    -   Required permissions: none
-   **COMMON\_EVENT\_USER\_STOPPING(deprecated)** (reserved, not supported yet) indicates the user to be stopped.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/61/v3/s6LfnZn9QrS1lKxnnVaKjQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062358Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=B310628789EF65208D40D1080C059E15A2FD2B11A86E78010FCC1FD603F68F71)
    
    This type is supported since API version 7 and deprecated since API version 9. You are advised to use [COMMON\_EVENT\_USER\_STOPPING](../../process-and-thread-communication/system-common-events/document.md#common_event_user_stopping) instead.
    
    -   Value: **usual.event.USER\_STOPPING**
    -   Required permissions: **ohos.permission.INTERACT\_ACROSS\_LOCAL\_ACCOUNTS** (for system applications only)
-   **COMMON\_EVENT\_USER\_STOPPED(deprecated)** (reserved, not supported yet) indicates that the user has been stopped.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/65/v3/pReJ1kfsQDKRqD4mO6SrVA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062358Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=124E2010747CC40E3299F0C11A4448996939598B4A5927DD031AF7B2DA0DE1EE)
    
    This type is supported since API version 7 and deprecated since API version 9. You are advised to use [COMMON\_EVENT\_USER\_STOPPED](../../process-and-thread-communication/system-common-events/document.md#common_event_user_stopped) instead.
    
    -   Value: **usual.event.USER\_STOPPED**
    -   Required permissions: none
-   **COMMON\_EVENT\_WIFI\_POWER\_STATE(deprecated)** indicates a change in the Wi-Fi state (enabled or disabled).
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a5/v3/NDSaRU5qR9m-pqdKwtH0CQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062358Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=2D0851C0D8AAFE7760803F678DE8FF17B75BBAF8BC9DA8712A721179E36E6322)
    
    This type is supported since API version 7 and deprecated since API version 9. You are advised to use [COMMON\_EVENT\_WIFI\_POWER\_STATE](../../process-and-thread-communication/system-common-events/document.md#common_event_wifi_power_state) instead.
    
    -   Value: **usual.event.wifi.POWER\_STATE**
    -   Required permissions: none
-   **COMMON\_EVENT\_WIFI\_SCAN\_FINISHED(deprecated)** indicates that the Wi-Fi access point has been scanned and proved available.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a6/v3/fN5aFuhTQc26N9ULuij_KA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062358Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=953339A2752109D1936312F773161411F6EDA623AAC8D700CA7267239979C63D)
    
    This type is supported since API version 7 and deprecated since API version 9. You are advised to use [COMMON\_EVENT\_WIFI\_SCAN\_FINISHED](../../process-and-thread-communication/system-common-events/document.md#common_event_wifi_scan_finished) instead.
    
    -   Value: **usual.event.wifi.SCAN\_FINISHED**
    -   Required permissions: **ohos.permission.LOCATION**
-   **COMMON\_EVENT\_WIFI\_RSSI\_VALUE(deprecated)** indicates that the Wi-Fi signal strength (RSSI) has changed.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c3/v3/zqXbdM5sT7O8au2qHeKMtQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062358Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=4255662BD984A697F60206CFEA0CB2DEDE21EB45C5FD37124A5B12249B43BC29)
    
    This type is supported since API version 7 and deprecated since API version 9. You are advised to use [COMMON\_EVENT\_WIFI\_RSSI\_VALUE](../../process-and-thread-communication/system-common-events/document.md#common_event_wifi_rssi_value) instead.
    
    -   Value: **usual.event.wifi.RSSI\_VALUE**
    -   Required permissions: **ohos.permission.GET\_WIFI\_INFO**
-   **COMMON\_EVENT\_WIFI\_CONN\_STATE(deprecated)** indicates that the Wi-Fi connection state has changed.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e5/v3/tlKfKFmqTDSHJVxOCCK3Dg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062358Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=56FEE9D2BA5A51011D68E545EE7328B99BB9AAF310D64DC8FED68FB21E385236)
    
    This type is supported since API version 7 and deprecated since API version 9. You are advised to use [COMMON\_EVENT\_WIFI\_CONN\_STATE](../../process-and-thread-communication/system-common-events/document.md#common_event_wifi_conn_state) instead.
    
    -   Value: **usual.event.wifi.CONN\_STATE**
    -   Required permissions: none
-   **COMMON\_EVENT\_WIFI\_HOTSPOT\_STATE(deprecated)** indicates a change in the Wi-Fi hotspot state (enabled or disabled).
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f6/v3/Xg-pXGn-R0yyJEF4WsEKZg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062358Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=80DFF4EFAE6416919C1EF85DCFC97EE616B45048621B2867D774CAF647CC1A16)
    
    This type is supported since API version 7 and deprecated since API version 9. You are advised to use [COMMON\_EVENT\_WIFI\_HOTSPOT\_STATE](../../process-and-thread-communication/system-common-events/document.md#common_event_wifi_hotspot_state) instead.
    
    -   Value: **usual.event.wifi.HOTSPOT\_STATE**
    -   Required permissions: none
-   **COMMON\_EVENT\_WIFI\_AP\_STA\_JOIN(deprecated)** indicates that a client has joined the Wi-Fi hotspot of the current device.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c6/v3/huwEkVdcSRy4D0lJC2fSPQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062358Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=D0F3B25B553EA723E61C0DBBC4A2FC11FAAD8C52704E616FD0151A150E497729)
    
    This type is supported since API version 7 and deprecated since API version 9. You are advised to use [COMMON\_EVENT\_WIFI\_AP\_STA\_JOIN](../../process-and-thread-communication/system-common-events/document.md#common_event_wifi_ap_sta_join) instead.
    
    -   Value: **usual.event.wifi.WIFI\_HS\_STA\_JOIN**
    -   Required permissions: **ohos.permission.GET\_WIFI\_INFO**
-   **COMMON\_EVENT\_WIFI\_AP\_STA\_LEAVE(deprecated)** indicates that the client is disconnected from the Wi-Fi hotspot of the current device.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/40/v3/INaSQakFTjK8nSpzSjk89A/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062358Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=0775A9E1D37F832EC19BA02B45220BF920A0A4D6977EBFD7F58516DCE00CB568)
    
    This type is supported since API version 7 and deprecated since API version 9. You are advised to use [COMMON\_EVENT\_WIFI\_AP\_STA\_LEAVE](../../process-and-thread-communication/system-common-events/document.md#common_event_wifi_ap_sta_leave) instead.
    
    -   Value: **usual.event.wifi.WIFI\_HS\_STA\_LEAVE**
    -   Required permissions: **ohos.permission.GET\_WIFI\_INFO**
-   **COMMON\_EVENT\_WIFI\_MPLINK\_STATE\_CHANGE(deprecated)** (not supported yet) indicates that the state of MPLINK (an enhanced Wi-Fi feature) has changed.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/33/v3/wavJfionSnevjSGTQdULPw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062358Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=767F5907754BEE7EEFAE6794A192DD25E788F0797EFDB7DE621E7A525F7B09FE)
    
    This type is supported since API version 7 and deprecated since API version 9. You are advised to use [COMMON\_EVENT\_WIFI\_MPLINK\_STATE\_CHANGE](../../process-and-thread-communication/system-common-events/document.md#common_event_wifi_mplink_state_change) instead.
    
    -   Value: **usual.event.wifi.mplink.STATE\_CHANGE**
    -   Required permissions: none
-   **COMMON\_EVENT\_WIFI\_P2P\_CONN\_STATE(deprecated)** indicates that the Wi-Fi P2P connection state has changed.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cf/v3/DxmagRXJRYC4Cpw5q4lqbA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062358Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=9784A2CDF80FEB616401F4296D611D81688614536E7F110D8E65A1032C6844E7)
    
    This type is supported since API version 7 and deprecated since API version 9. You are advised to use [COMMON\_EVENT\_WIFI\_P2P\_CONN\_STATE](../../process-and-thread-communication/system-common-events/document.md#common_event_wifi_p2p_conn_state) instead.
    
    -   Value: **usual.event.wifi.p2p.CONN\_STATE\_CHANGE**
    -   Required permissions: **ohos.permission.GET\_WIFI\_INFO** and **ohos.permission.LOCATION**
-   **COMMON\_EVENT\_WIFI\_P2P\_STATE\_CHANGED(deprecated)** indicates a change in the Wi-Fi P2P state (enabled or disabled).
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cc/v3/iYSXw_8YT7W-FeYbkWbeIg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062358Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=90C0DF7D86B0585AA4260592712166375073EA45E31C0FCD08CA38F32AA287BD)
    
    This type is supported since API version 7 and deprecated since API version 9. You are advised to use [COMMON\_EVENT\_WIFI\_P2P\_STATE\_CHANGED](../../process-and-thread-communication/system-common-events/document.md#common_event_wifi_p2p_state_changed) instead.
    
    -   Value: **usual.event.wifi.p2p.STATE\_CHANGE**
    -   Required permissions: **ohos.permission.GET\_WIFI\_INFO**
-   **COMMON\_EVENT\_WIFI\_P2P\_PEERS\_STATE\_CHANGED(deprecated)** indicates that the state of the Wi-Fi P2P peer device has changed.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e4/v3/n-dT0W1rSKeHu0l96U3ruA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062358Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=8CB376A4BD3554393F9474CF48025FA0C4000242D137E129AC394558092A414F)
    
    This type is supported since API version 7 and deprecated since API version 9. You are advised to use [COMMON\_EVENT\_WIFI\_P2P\_PEERS\_STATE\_CHANGED](../../process-and-thread-communication/system-common-events/document.md#common_event_wifi_p2p_peers_state_changed) instead.
    
    -   Value: **usual.event.wifi.p2p.DEVICES\_CHANGE**
    -   Required permissions: **ohos.permission.GET\_WIFI\_INFO**
-   **COMMON\_EVENT\_WIFI\_P2P\_PEERS\_DISCOVERY\_STATE\_CHANGED(deprecated)** indicates that the Wi-Fi P2P discovery state has changed.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/45/v3/ddbcUGivRm65nBs64Yhffw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062358Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=E89DBCCE57F1E924B57F9F6A4B8E40DEFFEF4F893BD6A329D4B6913C95B97991)
    
    This type is supported since API version 7 and deprecated since API version 9. You are advised to use [COMMON\_EVENT\_WIFI\_P2P\_PEERS\_DISCOVERY\_STATE\_CHANGED](../../process-and-thread-communication/system-common-events/document.md#common_event_wifi_p2p_peers_discovery_state_changed) instead.
    
    -   Value: **usual.event.wifi.p2p.PEER\_DISCOVERY\_STATE\_CHANGE**
    -   Required permissions: **ohos.permission.GET\_WIFI\_INFO**
-   **COMMON\_EVENT\_WIFI\_P2P\_CURRENT\_DEVICE\_STATE\_CHANGED(deprecated)** indicates that the state of the Wi-Fi P2P local device has changed.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1a/v3/WYz2zglWREqxmowk8t2adQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062358Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=3020727E393419A235B7B7532AEF9938A345210419BF94D602D0358B73176835)
    
    This type is supported since API version 7 and deprecated since API version 9. You are advised to use [COMMON\_EVENT\_WIFI\_P2P\_CURRENT\_DEVICE\_STATE\_CHANGED](../../process-and-thread-communication/system-common-events/document.md#common_event_wifi_p2p_current_device_state_changed) instead.
    
    -   Value: **usual.event.wifi.p2p.CURRENT\_DEVICE\_CHANGE**
    -   Required permissions: **ohos.permission.GET\_WIFI\_INFO**
-   **COMMON\_EVENT\_WIFI\_P2P\_GROUP\_STATE\_CHANGED(deprecated)** indicates that the Wi-Fi P2P group information has changed.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/af/v3/fitSzj-vS2yHD7EY0Vto3Q/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062358Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=46CF20A4B8F17B5F37EBFD2EFFAD58BEC2FE4841EB00A0AA2A5265D04704E112)
    
    This type is supported since API version 7 and deprecated since API version 9. You are advised to use [COMMON\_EVENT\_WIFI\_P2P\_GROUP\_STATE\_CHANGED](../../process-and-thread-communication/system-common-events/document.md#common_event_wifi_p2p_group_state_changed) instead.
    
    -   Value: **usual.event.wifi.p2p.GROUP\_STATE\_CHANGED**
    -   Required permissions: **ohos.permission.GET\_WIFI\_INFO**
-   **COMMON\_EVENT\_BLUETOOTH\_HANDSFREE\_AG\_CONNECT\_STATE\_UPDATE(deprecated)** (reserved, not supported yet) indicates the connection state of Bluetooth handsfree communication.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/66/v3/UpIoyyDISNCdIx9xI4Xqug/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062358Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=F28254B473B199883D2F45A7E9E8204A4791C826E88D6352CF630B556BEDD6B3)
    
    This type is supported since API version 7 and deprecated since API version 9. You are advised to use [COMMON\_EVENT\_BLUETOOTH\_HANDSFREE\_AG\_CONNECT\_STATE\_UPDATE](../../process-and-thread-communication/system-common-events/document.md#common_event_bluetooth_handsfree_ag_connect_state_updatedeprecated) instead.
    
    -   Value: **usual.event.bluetooth.handsfree.ag.CONNECT\_STATE\_UPDATE**
    -   Required permissions: **ohos.permission.USE\_BLUETOOTH**
-   **COMMON\_EVENT\_BLUETOOTH\_HANDSFREE\_AG\_CURRENT\_DEVICE\_UPDATE(deprecated)** (reserved, not supported yet) indicates that the device connected to the Bluetooth handsfree function is active.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/37/v3/CYHYUjCpQWac-hJJ5Fcicw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062358Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=2AB23BE713F42486A7FC6A69B41C1876579BF9463849EB5FB5C8FDFA72FD3714)
    
    This type is supported since API version 7 and deprecated since API version 9. You are advised to use [COMMON\_EVENT\_BLUETOOTH\_HANDSFREE\_AG\_CURRENT\_DEVICE\_UPDATE](../../process-and-thread-communication/system-common-events/document.md#common_event_bluetooth_handsfree_ag_current_device_updatedeprecated) instead.
    
    -   Value: **usual.event.bluetooth.handsfree.ag.CURRENT\_DEVICE\_UPDATE**
    -   Required permissions: **ohos.permission.USE\_BLUETOOTH**
-   **COMMON\_EVENT\_BLUETOOTH\_HANDSFREE\_AG\_AUDIO\_STATE\_UPDATE(deprecated)** (reserved, not supported yet) indicates that the connection state of Bluetooth A2DP has changed.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/67/v3/eEUe7PpeQeSzA6Ml5d5WXA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062358Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=D63A881C0909A53939D2F8DEC597B45B4E8E8F333670262ADAE816DAFCB92D5F)
    
    This type is supported since API version 7 and deprecated since API version 9. You are advised to use [COMMON\_EVENT\_BLUETOOTH\_HANDSFREE\_AG\_AUDIO\_STATE\_UPDATE](../../process-and-thread-communication/system-common-events/document.md#common_event_bluetooth_handsfree_ag_audio_state_updatedeprecated) instead.
    
    -   Value: **usual.event.bluetooth.handsfree.ag.AUDIO\_STATE\_UPDATE**
    -   Required permissions: **ohos.permission.USE\_BLUETOOTH**
-   **COMMON\_EVENT\_BLUETOOTH\_A2DPSOURCE\_CONNECT\_STATE\_UPDATE(deprecated)** (reserved, not supported yet) indicates the connection state of Bluetooth A2DP.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bd/v3/9qBiHbgxSEeemNe9XXaQeA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062358Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=B981E394ADE14D6233BD1A984E9C3C6A66E7EF959AD7268DA339A1DCB51ACF9C)
    
    This type is supported since API version 7 and deprecated since API version 9. You are advised to use [COMMON\_EVENT\_BLUETOOTH\_A2DPSOURCE\_CONNECT\_STATE\_UPDATE](../../process-and-thread-communication/system-common-events/document.md#common_event_bluetooth_a2dpsource_connect_state_updatedeprecated) instead.
    
    -   Value: **usual.event.bluetooth.a2dpsource.CONNECT\_STATE\_UPDATE**
    -   Required permissions: **ohos.permission.USE\_BLUETOOTH**
-   **COMMON\_EVENT\_BLUETOOTH\_A2DPSOURCE\_CURRENT\_DEVICE\_UPDATE(deprecated)** (reserved, not supported yet) indicates that the device connected using Bluetooth A2DP is active.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/66/v3/z06wdzDqROuHcqFGKZ9Iiw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062358Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=7C2E34482E7B813834005D9E53182116EC4225165214FFC90FB9582B2B21E860)
    
    This type is supported since API version 7 and deprecated since API version 9. You are advised to use [COMMON\_EVENT\_BLUETOOTH\_A2DPSOURCE\_CURRENT\_DEVICE\_UPDATE](../../process-and-thread-communication/system-common-events/document.md#common_event_bluetooth_a2dpsource_current_device_updatedeprecated) instead.
    
    -   Value: **usual.event.bluetooth.a2dpsource.CURRENT\_DEVICE\_UPDATE**
    -   Required permissions: **ohos.permission.USE\_BLUETOOTH**
-   **COMMON\_EVENT\_BLUETOOTH\_A2DPSOURCE\_PLAYING\_STATE\_UPDATE(deprecated)** (reserved, not supported yet) indicates that the playing state of Bluetooth A2DP has changed.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d1/v3/4IUhKSgtQ2OfROVckcA9Uw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062358Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=385A1D708904237BB54351CB344AE38BA0C760273E04E39AE3449589E3B9E77F)
    
    This type is supported since API version 7 and deprecated since API version 9. You are advised to use [COMMON\_EVENT\_BLUETOOTH\_A2DPSOURCE\_PLAYING\_STATE\_UPDATE](../../process-and-thread-communication/system-common-events/document.md#common_event_bluetooth_a2dpsource_playing_state_updatedeprecated) instead.
    
    -   Value: **usual.event.bluetooth.a2dpsource.PLAYING\_STATE\_UPDATE**
    -   Required permissions: **ohos.permission.USE\_BLUETOOTH**
-   **COMMON\_EVENT\_BLUETOOTH\_A2DPSOURCE\_AVRCP\_CONNECT\_STATE\_UPDATE(deprecated)** (reserved, not supported yet) indicates that the AVRCP connection state of Bluetooth A2DP has changed.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f1/v3/5A8HWb4dTuytBosnjSyUFw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062358Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=F01D7B6F336B1DD0665C9DFAABFE00E99F5D5FEEE8C49D3DCF12E710AA8D81C1)
    
    This type is supported since API version 7 and deprecated since API version 9. You are advised to use [COMMON\_EVENT\_BLUETOOTH\_A2DPSOURCE\_AVRCP\_CONNECT\_STATE\_UPDATE](../../process-and-thread-communication/system-common-events/document.md#common_event_bluetooth_a2dpsource_avrcp_connect_state_updatedeprecated) instead.
    
    -   Value: **usual.event.bluetooth.a2dpsource.AVRCP\_CONNECT\_STATE\_UPDATE**
    -   Required permissions: **ohos.permission.USE\_BLUETOOTH**
-   **COMMON\_EVENT\_BLUETOOTH\_A2DPSOURCE\_CODEC\_VALUE\_UPDATE(deprecated)** (reserved, not supported yet) indicates that the audio codec state of Bluetooth A2DP has changed.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/60/v3/id50Z273Q2-c0Enb19W6RA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062358Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=08B4428E25BD1085128CA44856385ADF29CDA92BFF9B7538A40FCE9EF3A1C11E)
    
    This type is supported since API version 7 and deprecated since API version 9. You are advised to use [COMMON\_EVENT\_BLUETOOTH\_A2DPSOURCE\_CODEC\_VALUE\_UPDATE](../../process-and-thread-communication/system-common-events/document.md#common_event_bluetooth_a2dpsource_codec_value_updatedeprecated) instead.
    
    -   Value: **usual.event.bluetooth.a2dpsource.CODEC\_VALUE\_UPDATE**
    -   Required permissions: **ohos.permission.USE\_BLUETOOTH**
-   **COMMON\_EVENT\_BLUETOOTH\_REMOTEDEVICE\_DISCOVERED(deprecated)** (reserved, not supported yet) indicates that a remote Bluetooth device is discovered.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3c/v3/CFOFhtliS2OaE85ZNok41w/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062358Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=0AD4FB3246DF508009337F5AF797880F9672DB7F389FEE012F2F8644A7064876)
    
    This type is supported since API version 7 and deprecated since API version 9. You are advised to use [COMMON\_EVENT\_BLUETOOTH\_REMOTEDEVICE\_DISCOVERED](../../process-and-thread-communication/system-common-events/document.md#common_event_bluetooth_remotedevice_discovereddeprecated) instead.
    
    -   Value: **usual.event.bluetooth.remotedevice.DISCOVERED**
    -   Required permissions: ohos.permission.LOCATION and ohos.permission.USE\_BLUETOOTH
-   **COMMON\_EVENT\_BLUETOOTH\_REMOTEDEVICE\_CLASS\_VALUE\_UPDATE(deprecated)** (reserved, not supported yet) indicates that the Bluetooth class of a remote Bluetooth device has changed.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/be/v3/z9qtzXZoRnWA0mVwH_o1uA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062358Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=FD6EA1E662BE3B84912F54A822669556864F8ABF92272836FD2C710B69425EA2)
    
    This type is supported since API version 7 and deprecated since API version 9. You are advised to use [COMMON\_EVENT\_BLUETOOTH\_REMOTEDEVICE\_CLASS\_VALUE\_UPDATE](../../process-and-thread-communication/system-common-events/document.md#common_event_bluetooth_remotedevice_class_value_updatedeprecated) instead.
    
    -   Value: **usual.event.bluetooth.remotedevice.CLASS\_VALUE\_UPDATE**
    -   Required permissions: **ohos.permission.USE\_BLUETOOTH**
-   **COMMON\_EVENT\_BLUETOOTH\_REMOTEDEVICE\_ACL\_CONNECTED(deprecated)** (reserved, not supported yet) indicates that a low-level (ACL) connection has been established with the remote Bluetooth device.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e4/v3/E4Y5s5DMQ7a-KQSTbb9yRg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062358Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=3371BF3ED8654EEC40E20D83BA151F25FBDDE531BC3BC5F54705DB1B90D04279)
    
    This type is supported since API version 7 and deprecated since API version 9. You are advised to use [COMMON\_EVENT\_BLUETOOTH\_REMOTEDEVICE\_ACL\_CONNECTED](../../process-and-thread-communication/system-common-events/document.md#common_event_bluetooth_remotedevice_acl_connecteddeprecated) instead.
    
    -   Value: **usual.event.bluetooth.remotedevice.ACL\_CONNECTED**
    -   Required permissions: **ohos.permission.USE\_BLUETOOTH**
-   **COMMON\_EVENT\_BLUETOOTH\_REMOTEDEVICE\_ACL\_DISCONNECTED(deprecated)** (reserved, not supported yet) indicates that the low-level (ACL) connection has been disconnected from the remote Bluetooth device.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f3/v3/LL6ryKbKROe-E3EFb3A3lQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062358Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=CEC35C2339BA6F5B877886F618562AA394B86BF2888CD45835E50322F207BAAF)
    
    This type is supported since API version 7 and deprecated since API version 9. You are advised to use [COMMON\_EVENT\_BLUETOOTH\_REMOTEDEVICE\_ACL\_DISCONNECTED](../../process-and-thread-communication/system-common-events/document.md#common_event_bluetooth_remotedevice_acl_disconnecteddeprecated) instead.
    
    -   Value: **usual.event.bluetooth.remotedevice.ACL\_DISCONNECTED**
    -   Required permissions: **ohos.permission.USE\_BLUETOOTH**
-   **COMMON\_EVENT\_BLUETOOTH\_REMOTEDEVICE\_NAME\_UPDATE(deprecated)** (reserved, not supported yet) indicates that the friendly name of a remote Bluetooth device is retrieved for the first time or has changed since the last retrieval.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7c/v3/gKsThcLdTVOtcgxmTkF4hg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062358Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=286AD340DE1B54B3E9EAB74EA54C0223AEB805CFF0FEDBEDC5EA02A044E72294)
    
    This type is supported since API version 7 and deprecated since API version 9. You are advised to use [COMMON\_EVENT\_BLUETOOTH\_REMOTEDEVICE\_NAME\_UPDATE](../../process-and-thread-communication/system-common-events/document.md#common_event_bluetooth_remotedevice_name_updatedeprecated) instead.
    
    -   Value: **usual.event.bluetooth.remotedevice.NAME\_UPDATE**
    -   Required permissions: **ohos.permission.USE\_BLUETOOTH**
-   **COMMON\_EVENT\_BLUETOOTH\_REMOTEDEVICE\_PAIR\_STATE(deprecated)** (reserved, not supported yet) indicates the connection state with a remote Bluetooth device is changed.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c5/v3/_k17yK2tS6Soz9sSQldYVg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062358Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=8BE4ACC4DE9277B191225C33023045A0F3B5002DFEC575F4E662043C8E4F0B70)
    
    This type is supported since API version 7 and deprecated since API version 9. You are advised to use [COMMON\_EVENT\_BLUETOOTH\_REMOTEDEVICE\_PAIR\_STATE](../../process-and-thread-communication/system-common-events/document.md#common_event_bluetooth_remotedevice_pair_statedeprecated) instead.
    
    -   Value: **usual.event.bluetooth.remotedevice.PAIR\_STATE**
    -   Required permissions: **ohos.permission.USE\_BLUETOOTH**
-   **COMMON\_EVENT\_BLUETOOTH\_REMOTEDEVICE\_BATTERY\_VALUE\_UPDATE(deprecated)** (reserved, not supported yet) indicates that the battery level of a remote Bluetooth device is retrieved for the first time or has changed since the last retrieval.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bc/v3/tfrskvWgSE2R-9wxRC5pTw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062358Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=6171377E66C4149DD01E4C6DF5F738AD26E20ACD549A7E981CF4C12A5DFFEA08)
    
    This type is supported since API version 7 and deprecated since API version 9. You are advised to use [COMMON\_EVENT\_BLUETOOTH\_REMOTEDEVICE\_BATTERY\_VALUE\_UPDATE](../../process-and-thread-communication/system-common-events/document.md#common_event_bluetooth_remotedevice_battery_value_updatedeprecated) instead.
    
    -   Value: **usual.event.bluetooth.remotedevice.BATTERY\_VALUE\_UPDATE**
    -   Required permissions: **ohos.permission.USE\_BLUETOOTH**
-   **COMMON\_EVENT\_BLUETOOTH\_REMOTEDEVICE\_SDP\_RESULT(deprecated)** (reserved, not supported yet) indicates the SDP state of a remote Bluetooth device.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a0/v3/oC-MZuHcRkWPHWtM0HE7ew/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062358Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=6FB733E3B118078409EA570473B79A54A40E16D71E07791DCC432CDD470F95A6)
    
    This type is supported since API version 7 and deprecated since API version 9. You are advised to use [COMMON\_EVENT\_BLUETOOTH\_REMOTEDEVICE\_SDP\_RESULT](../../process-and-thread-communication/system-common-events/document.md#common_event_bluetooth_remotedevice_sdp_resultdeprecated) instead.
    
    -   Value: **usual.event.bluetooth.remotedevice.SDP\_RESULT**
    -   Required permissions: none
-   **COMMON\_EVENT\_BLUETOOTH\_REMOTEDEVICE\_UUID\_VALUE(deprecated)** (reserved, not supported yet) indicates the UUID connection state with a remote Bluetooth device.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2c/v3/amoXXaIdRxGSk62aI-gELQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062358Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=D8B4F8321EEC8E02A721D3BB820E68640AEAB953447F83BEA04FB3CA934358DF)
    
    This type is supported since API version 7 and deprecated since API version 9. You are advised to use [COMMON\_EVENT\_BLUETOOTH\_REMOTEDEVICE\_UUID\_VALUE](../../process-and-thread-communication/system-common-events/document.md#common_event_bluetooth_remotedevice_uuid_valuedeprecated) instead.
    
    -   Value: **usual.event.bluetooth.remotedevice.UUID\_VALUE**
    -   Required permissions: **ohos.permission.DISCOVER\_BLUETOOTH**
-   **COMMON\_EVENT\_BLUETOOTH\_REMOTEDEVICE\_PAIRING\_REQ(deprecated)** (reserved, not supported yet) indicates the pairing request from a remote Bluetooth device.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3a/v3/lPE4sC0nSCW1p5bQgJXuVQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062358Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=DB8625ED70F7311554422F3883FE3AEE3A28C4B2118FE2E46F0A6B608FF4447E)
    
    This type is supported since API version 7 and deprecated since API version 9. You are advised to use [COMMON\_EVENT\_BLUETOOTH\_REMOTEDEVICE\_PAIRING\_REQ](../../process-and-thread-communication/system-common-events/document.md#common_event_bluetooth_remotedevice_pairing_reqdeprecated) instead.
    
    -   Value: **usual.event.bluetooth.remotedevice.PAIRING\_REQ**
    -   Required permissions: **ohos.permission.DISCOVER\_BLUETOOTH**
-   **COMMON\_EVENT\_BLUETOOTH\_REMOTEDEVICE\_PAIRING\_CANCEL(deprecated)** (reserved, not supported yet) indicates that Bluetooth pairing has been canceled.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/db/v3/14vsgk5VTSusIPB2EC_uSA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062358Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=48BC8B028EA4329E96082E21ABADC38F4D3CBAB4E63ACA392FA7BEFEB8CE307F)
    
    This type is supported since API version 7 and deprecated since API version 9. You are advised to use [COMMON\_EVENT\_BLUETOOTH\_REMOTEDEVICE\_PAIRING\_CANCEL](../../process-and-thread-communication/system-common-events/document.md#common_event_bluetooth_remotedevice_pairing_canceldeprecated) instead.
    
    -   Value: **usual.event.bluetooth.remotedevice.PAIRING\_CANCEL**
    -   Required permissions: none
-   **COMMON\_EVENT\_BLUETOOTH\_REMOTEDEVICE\_CONNECT\_REQ(deprecated)** (reserved, not supported yet) indicates the connection request from a remote Bluetooth device.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/92/v3/TTvxWvUETiOQSAhhniY-Zg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062358Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=74CE456115A07129C8A60DA7063D2B76FC2967AB69C39FAB8CB7162FE828086B)
    
    This type is supported since API version 7 and deprecated since API version 9. You are advised to use [COMMON\_EVENT\_BLUETOOTH\_REMOTEDEVICE\_CONNECT\_REQ](../../process-and-thread-communication/system-common-events/document.md#common_event_bluetooth_remotedevice_connect_reqdeprecated) instead.
    
    -   Value: **usual.event.bluetooth.remotedevice.CONNECT\_REQ**
    -   Required permissions: none
-   **COMMON\_EVENT\_BLUETOOTH\_REMOTEDEVICE\_CONNECT\_REPLY(deprecated)** (reserved, not supported yet) indicates the response to the connection request from a remote Bluetooth device.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/24/v3/eNnn7GxTQve8eRDfy4qtmw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062358Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=2474D9F63CF42D8B67FD2159400FCCAD3B853BBD7FC926375FC90FAA518DC9E8)
    
    This type is supported since API version 7 and deprecated since API version 9. You are advised to use [COMMON\_EVENT\_BLUETOOTH\_REMOTEDEVICE\_CONNECT\_REPLY](../../process-and-thread-communication/system-common-events/document.md#common_event_bluetooth_remotedevice_connect_replydeprecated) instead.
    
    -   Value: **usual.event.bluetooth.remotedevice.CONNECT\_REPLY**
    -   Required permissions: none
-   **COMMON\_EVENT\_BLUETOOTH\_REMOTEDEVICE\_CONNECT\_CANCEL(deprecated)** (reserved, not supported yet) indicates that the connection to a remote Bluetooth device has been canceled.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f4/v3/WbuGgCjnT82jmTQ6Wqgytw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062358Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=560EC7316AF3CCFA3D905EEFC65FB50796CEB79C27F1D1C7B7475FD33F5CE68C)
    
    This type is supported since API version 7 and deprecated since API version 9. You are advised to use [COMMON\_EVENT\_BLUETOOTH\_REMOTEDEVICE\_CONNECT\_CANCEL](../../process-and-thread-communication/system-common-events/document.md#common_event_bluetooth_remotedevice_connect_canceldeprecated) instead.
    
    -   Value: **usual.event.bluetooth.remotedevice.CONNECT\_CANCEL**
    -   Required permissions: none
-   **COMMON\_EVENT\_BLUETOOTH\_HANDSFREEUNIT\_CONNECT\_STATE\_UPDATE(deprecated)** (reserved, not supported yet) indicates that the connection state with a Bluetooth handsfree has changed.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1c/v3/h2coxVwSQeWn9AwlViNsEQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062358Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=9A465EFC0D9429FE3E4F5765E0053D02BAB0DEAAB2B0AE09F24E52F5D0627355)
    
    This type is supported since API version 7 and deprecated since API version 9. You are advised to use [COMMON\_EVENT\_BLUETOOTH\_HANDSFREEUNIT\_CONNECT\_STATE\_UPDATE](../../process-and-thread-communication/system-common-events/document.md#common_event_bluetooth_handsfreeunit_connect_state_updatedeprecated) instead.
    
    -   Value: **usual.event.bluetooth.handsfreeunit.CONNECT\_STATE\_UPDATE**
    -   Required permissions: none
-   **COMMON\_EVENT\_BLUETOOTH\_HANDSFREEUNIT\_AUDIO\_STATE\_UPDATE(deprecated)** (reserved, not supported yet) indicates that the audio state of a Bluetooth handsfree has changed.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f1/v3/wjrKvY-5TJyOf3sDo18d_A/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062358Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=8E71EBAA7EBDFBD7427D1283C42CA39DBBCFA9B1010279716F981F5B48BB309A)
    
    This type is supported since API version 7 and deprecated since API version 9. You are advised to use [COMMON\_EVENT\_BLUETOOTH\_HANDSFREEUNIT\_AUDIO\_STATE\_UPDATE](../../process-and-thread-communication/system-common-events/document.md#common_event_bluetooth_handsfreeunit_audio_state_updatedeprecated) instead.
    
    -   Value: **usual.event.bluetooth.handsfreeunit.AUDIO\_STATE\_UPDATE**
    -   Required permissions: none
-   **COMMON\_EVENT\_BLUETOOTH\_HANDSFREEUNIT\_AG\_COMMON\_EVENT(deprecated)** (reserved, not supported yet) indicates that the audio gateway state of a Bluetooth handsfree has changed.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/48/v3/NXp7VxXhRru4DBvvfIavAQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062358Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=039A5C99DB381BCFDFE706BAC92151E44FAA4C906A5A2AC04BDB328BAD8A3DDF)
    
    This type is supported since API version 7 and deprecated since API version 9. You are advised to use [COMMON\_EVENT\_BLUETOOTH\_HANDSFREEUNIT\_AG\_COMMON\_EVENT](../../process-and-thread-communication/system-common-events/document.md#common_event_bluetooth_handsfreeunit_ag_common_eventdeprecated) instead.
    
    -   Value: **usual.event.bluetooth.handsfreeunit.AG\_COMMON\_EVENT**
    -   Required permissions: none
-   **COMMON\_EVENT\_BLUETOOTH\_HANDSFREEUNIT\_AG\_CALL\_STATE\_UPDATE(deprecated)** (reserved, not supported yet) indicates that the calling state of a Bluetooth handsfree has changed.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e4/v3/RaS1PBqkSee8aRTQr-36gA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062358Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=4ACD81DEC689D076D4202268F99A8F481DBDAFA45FF86422272F5F8C7F843E5A)
    
    This type is supported since API version 7 and deprecated since API version 9. You are advised to use [COMMON\_EVENT\_BLUETOOTH\_HANDSFREEUNIT\_AG\_CALL\_STATE\_UPDATE](../../process-and-thread-communication/system-common-events/document.md#common_event_bluetooth_handsfreeunit_ag_call_state_updatedeprecated) instead.
    
    -   Value: **usual.event.bluetooth.handsfreeunit.AG\_CALL\_STATE\_UPDATE**
    -   Required permissions: none
-   **COMMON\_EVENT\_BLUETOOTH\_HOST\_STATE\_UPDATE(deprecated)** (reserved, not supported yet) indicates a change in the Bluetooth adapter state (enabled or disabled).
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a6/v3/4UyZ8X_PR9ehRWrl24AEMQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062358Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=7F54868B1776209D2A2E1174CEC0DDD076901418B3E58BA655552DC089CF980E)
    
    This type is supported since API version 7 and deprecated since API version 9. You are advised to use [COMMON\_EVENT\_BLUETOOTH\_HOST\_STATE\_UPDATE](../../process-and-thread-communication/system-common-events/document.md#common_event_bluetooth_host_state_updatedeprecated) instead.
    
    -   Value: **usual.event.bluetooth.host.STATE\_UPDATE**
    -   Required permissions: **ohos.permission.USE\_BLUETOOTH**
-   **COMMON\_EVENT\_BLUETOOTH\_HOST\_REQ\_DISCOVERABLE(deprecated)** (reserved, not supported yet) indicates that Bluetooth is discoverable.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d9/v3/2V1fgUlGSCeRApZjUngE-Q/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062358Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=561C5ACEDE29658BF1FE462D87DB0D94DEC278AE2EAB31B1553BDD4C2643DD28)
    
    This type is supported since API version 7 and deprecated since API version 9. You are advised to use [COMMON\_EVENT\_BLUETOOTH\_HOST\_REQ\_DISCOVERABLE](../../process-and-thread-communication/system-common-events/document.md#common_event_bluetooth_host_req_discoverabledeprecated) instead.
    
    -   Value: **usual.event.bluetooth.host.REQ\_DISCOVERABLE**
    -   Required permissions: none
-   **COMMON\_EVENT\_BLUETOOTH\_HOST\_REQ\_ENABLE(deprecated)** (reserved, not supported yet) indicates that Bluetooth is enabled.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7f/v3/qKEPvkUfTg2Ikutjev4CGQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062358Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=F4B3D3F5F5D9CC8122B13F1716C3D3AF39529AA14FA83D2E41B580740FDE06AF)
    
    This type is supported since API version 7 and deprecated since API version 9. You are advised to use [COMMON\_EVENT\_BLUETOOTH\_HOST\_REQ\_ENABLE](../../process-and-thread-communication/system-common-events/document.md#common_event_bluetooth_host_req_enabledeprecated) instead.
    
    -   Value: **usual.event.bluetooth.host.REQ\_ENABLE**
    -   Required permissions: **ohos.permission.USE\_BLUETOOTH**
-   **COMMON\_EVENT\_BLUETOOTH\_HOST\_REQ\_DISABLE(deprecated)** (reserved, not supported yet) indicates that Bluetooth is disabled.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/78/v3/rV1XAS9MTMW-K6T2dMGhRw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062358Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=743A8A0EABCA1782BD7CB601DC939E87DF1CF57010D0A5B84692EA505C1BC7D5)
    
    This type is supported since API version 7 and deprecated since API version 9. You are advised to use [COMMON\_EVENT\_BLUETOOTH\_HOST\_REQ\_DISABLE](../../process-and-thread-communication/system-common-events/document.md#common_event_bluetooth_host_req_disabledeprecated) instead.
    
    -   Value: **usual.event.bluetooth.host.REQ\_DISABLE**
    -   Required permissions: **ohos.permission.USE\_BLUETOOTH**
-   **COMMON\_EVENT\_BLUETOOTH\_HOST\_SCAN\_MODE\_UPDATE(deprecated)** (reserved, not supported yet) indicates that the Bluetooth scan mode of the device is changed.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/93/v3/v3HwNNOYTZy5Hku8LnhXNQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062358Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=ADBBFFB9C28AB5C518D156BDF6DF9BF306F4ABAF9217B1E823BCB54DBFD07127)
    
    This type is supported since API version 7 and deprecated since API version 9. You are advised to use [COMMON\_EVENT\_BLUETOOTH\_HOST\_SCAN\_MODE\_UPDATE](../../process-and-thread-communication/system-common-events/document.md#common_event_bluetooth_host_scan_mode_updatedeprecated) instead.
    
    -   Value: **usual.event.bluetooth.host.SCAN\_MODE\_UPDATE**
    -   Required permissions: **ohos.permission.USE\_BLUETOOTH**
-   **COMMON\_EVENT\_BLUETOOTH\_HOST\_DISCOVERY\_STARTED(deprecated)** (reserved, not supported yet) indicates that Bluetooth discovery is started on the device.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/dd/v3/LNB-cF58Q3iukQUd-fLivg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062358Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=3A9945CF7D115983010C233A233B41CCBB1A4B48D44304A4F314F62AA503747C)
    
    This type is supported since API version 7 and deprecated since API version 9. You are advised to use [COMMON\_EVENT\_BLUETOOTH\_HOST\_DISCOVERY\_STARTED](../../process-and-thread-communication/system-common-events/document.md#common_event_bluetooth_host_discovery_starteddeprecated) instead.
    
    -   Value: **usual.event.bluetooth.host.DISCOVERY\_STARTED**
    -   Required permissions: **ohos.permission.USE\_BLUETOOTH**
-   **COMMON\_EVENT\_BLUETOOTH\_HOST\_DISCOVERY\_FINISHED(deprecated)** (reserved, not supported yet) indicates that Bluetooth discovery is finished on the device.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2f/v3/T1EP6RYeSQeyiJIyCVpfTg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062358Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=47433F795652C642091139185B09F039229A6FB699F048684D13B6B19DEF3649)
    
    This type is supported since API version 7 and deprecated since API version 9. You are advised to use [COMMON\_EVENT\_BLUETOOTH\_HOST\_DISCOVERY\_FINISHED](../../process-and-thread-communication/system-common-events/document.md#common_event_bluetooth_host_discovery_finisheddeprecated) instead.
    
    -   Value: **usual.event.bluetooth.host.DISCOVERY\_FINISHED**
    -   Required permissions: **ohos.permission.USE\_BLUETOOTH**
-   **COMMON\_EVENT\_BLUETOOTH\_HOST\_NAME\_UPDATE(deprecated)** (reserved, not supported yet) indicates that the name of the device Bluetooth adapter has changed.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fb/v3/HCtuJQE2S-aOyayS7umiPw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062358Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=E0361AABCEA0DD97DD47CF98CA440410264D42F7AECAB5F8CA970656B7AFF7C8)
    
    This type is supported since API version 7 and deprecated since API version 9. You are advised to use [COMMON\_EVENT\_BLUETOOTH\_HOST\_NAME\_UPDATE](../../process-and-thread-communication/system-common-events/document.md#common_event_bluetooth_host_name_updatedeprecated) instead.
    
    -   Value: **usual.event.bluetooth.host.NAME\_UPDATE**
    -   Required permissions: **ohos.permission.USE\_BLUETOOTH**
-   **COMMON\_EVENT\_BLUETOOTH\_A2DPSINK\_CONNECT\_STATE\_UPDATE(deprecated)** (reserved, not supported yet) indicates that the connection state of Bluetooth A2DP Sink has changed.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fc/v3/suuZ2FRQRhuCV0Mn4PriGw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062358Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=BC2BB2337B16354E500DFBDD175EE8B80F83BD1FF5A2FAD9777EF998FBC7506C)
    
    This type is supported since API version 7 and deprecated since API version 9. You are advised to use [COMMON\_EVENT\_BLUETOOTH\_A2DPSINK\_CONNECT\_STATE\_UPDATE](../../process-and-thread-communication/system-common-events/document.md#common_event_bluetooth_a2dpsink_connect_state_updatedeprecated) instead.
    
    -   Value: **usual.event.bluetooth.a2dpsink.CONNECT\_STATE\_UPDATE**
    -   Required permissions: **ohos.permission.USE\_BLUETOOTH**
-   **COMMON\_EVENT\_BLUETOOTH\_A2DPSINK\_PLAYING\_STATE\_UPDATE(deprecated)** (reserved, not supported yet) indicates that the playing state of Bluetooth A2DP Sink has changed.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/63/v3/21bQSj1OQ0y9BNp6EL3GmA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062358Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=76C63C5B3F415E16E2258844711F1E034E40AFB14376F2B81B8BC81C9B28D813)
    
    This type is supported since API version 7 and deprecated since API version 9. You are advised to use [COMMON\_EVENT\_BLUETOOTH\_A2DPSINK\_PLAYING\_STATE\_UPDATE](../../process-and-thread-communication/system-common-events/document.md#common_event_bluetooth_a2dpsink_playing_state_updatedeprecated) instead.
    
    -   Value: **usual.event.bluetooth.a2dpsink.PLAYING\_STATE\_UPDATE**
    -   Required permissions: **ohos.permission.USE\_BLUETOOTH**
-   **COMMON\_EVENT\_BLUETOOTH\_A2DPSINK\_AUDIO\_STATE\_UPDATE(deprecated)** (reserved, not supported yet) indicates that the audio state of Bluetooth A2DP Sink has changed.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1c/v3/8Ppqw0UJRv6e6tg50ghfpQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062358Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=DC2F148B8B74E90AF19E244B8966D460DCB3895A30B9BD838478CB4826725AAF)
    
    This type is supported since API version 7 and deprecated since API version 9. You are advised to use [COMMON\_EVENT\_BLUETOOTH\_A2DPSINK\_AUDIO\_STATE\_UPDATE](../../process-and-thread-communication/system-common-events/document.md#common_event_bluetooth_a2dpsink_audio_state_updatedeprecated) instead.
    
    -   Value: **usual.event.bluetooth.a2dpsink.AUDIO\_STATE\_UPDATE**
    -   Required permissions: **ohos.permission.USE\_BLUETOOTH**
-   **COMMON\_EVENT\_NFC\_ACTION\_ADAPTER\_STATE\_CHANGED(deprecated)** (reserved, not supported yet) indicates that the state of the device NFC adapter has changed.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5c/v3/2UvurtlHSxejywilKyOtig/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062358Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=FB419BB6141AAB2688CB6E0AB6A69C6245D42F68F405D65EE9150D14483F2431)
    
    This type is supported since API version 7 and deprecated since API version 9. You are advised to use [COMMON\_EVENT\_NFC\_ACTION\_ADAPTER\_STATE\_CHANGED](../../process-and-thread-communication/system-common-events/document.md#common_event_nfc_action_adapter_state_changed) instead.
    
    -   Value: **usual.event.nfc.action.ADAPTER\_STATE\_CHANGED**
    -   Required permissions: none
-   **COMMON\_EVENT\_NFC\_ACTION\_RF\_FIELD\_ON\_DETECTED(deprecated)** (reserved, not supported yet) indicates that the NFC RF field is detected to be in the enabled state.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b2/v3/s9r4oobNQ669S2LquEaHfA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062358Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=1FFCD23F34C06FCA5D1AEB47997532B834D3A020544B40A779ED0D2C4CF6A3BB)
    
    This type is supported since API version 7 and deprecated since API version 9. You are advised to use [COMMON\_EVENT\_NFC\_ACTION\_RF\_FIELD\_ON\_DETECTED](../../process-and-thread-communication/system-common-events/document.md#common_event_nfc_action_rf_field_on_detected) instead.
    
    -   Value: **usual.event.nfc.action.RF\_FIELD\_ON\_DETECTED**
    -   Required permissions: **ohos.permission.MANAGE\_SECURE\_SETTINGS** (for system applications only)
-   **COMMON\_EVENT\_NFC\_ACTION\_RF\_FIELD\_OFF\_DETECTED(deprecated)** (reserved, not supported yet) indicates that the NFC RF field is detected to be in the disabled state.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/83/v3/egabFc1yRBK30Ht_Z8cUQA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062358Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=A1A294EE38A91D9BBD2F482A7D0FA5B3D8A4C5D1C8D52777EDC5D0EDA777E2AF)
    
    This type is supported since API version 7 and deprecated since API version 9. You are advised to use [COMMON\_EVENT\_NFC\_ACTION\_RF\_FIELD\_OFF\_DETECTED](../../process-and-thread-communication/system-common-events/document.md#common_event_nfc_action_rf_field_off_detected) instead.
    
    -   Value: **usual.event.nfc.action.RF\_FIELD\_OFF\_DETECTED**
    -   Required permissions: **ohos.permission.MANAGE\_SECURE\_SETTINGS** (for system applications only)
-   **COMMON\_EVENT\_DISCHARGING(deprecated)** indicates that the system stops charging the battery.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3e/v3/Ws9TW161SiqF5QTVBgvPwA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062358Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=EA96E968785F5541E3A65C7C5F1B564F4B521C50E81673C5BB330B5B00B2E982)
    
    This type is supported since API version 7 and deprecated since API version 9. You are advised to use [COMMON\_EVENT\_DISCHARGING](../../process-and-thread-communication/system-common-events/document.md#common_event_discharging) instead.
    
    -   Value: **usual.event.DISCHARGING**
    -   Required permissions: none
-   **COMMON\_EVENT\_CHARGING(deprecated)** indicates that the system starts charging the battery.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/39/v3/c2EH8L1pR0u0OdFiZUGTFA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062358Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=B4E77A761FF37CCB8A466AFF3A693DDE8BD771516ED012FB436BE0BFD490F9B3)
    
    This type is supported since API version 7 and deprecated since API version 9. You are advised to use [COMMON\_EVENT\_CHARGING](../../process-and-thread-communication/system-common-events/document.md#common_event_charging) instead.
    
    -   Value: **usual.event.CHARGING**
    -   Required permissions: none
-   **COMMON\_EVENT\_DEVICE\_IDLE\_MODE\_CHANGED(deprecated)** (reserved, not supported yet) indicates that the system idle mode has changed.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/dd/v3/MG2-nWapQcOX7VfuYDbwZA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062358Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=4EE2F9D234263CCADDF21ECC4CDC8A506A957510B61BE54DC08D6E2C70DCABA7)
    
    This type is supported since API version 7 and deprecated since API version 9. You are advised to use [COMMON\_EVENT\_DEVICE\_IDLE\_MODE\_CHANGED](../../process-and-thread-communication/system-common-events/document.md#common_event_device_idle_mode_changed) instead.
    
    -   Value: **usual.event.DEVICE\_IDLE\_MODE\_CHANGED**
    -   Required permissions: none
-   **COMMON\_EVENT\_POWER\_SAVE\_MODE\_CHANGED(deprecated)** indicates that the system power-saving mode has changed.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ed/v3/No944JFGTce9GISUuvSkwQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062358Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=FA5C6A46B4714B100EE2121CA07ABC9B384607B026F334DE2EBFC470DF325AA6)
    
    This type is supported since API version 7 and deprecated since API version 9. You are advised to use [COMMON\_EVENT\_POWER\_SAVE\_MODE\_CHANGED](../../process-and-thread-communication/system-common-events/document.md#common_event_power_save_mode_changed) instead.
    
    -   Value: **usual.event.POWER\_SAVE\_MODE\_CHANGED**
    -   Required permissions: none
-   **COMMON\_EVENT\_USER\_ADDED(deprecated)** indicates that a user has been added to the system.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d8/v3/TPIYQlc5SZiWVdvFVprn1g/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062358Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=AFFED4BBB7F2EB76A231A100219EA5CEA9279F6796173879130D8AF41DC0B3D7)
    
    This type is supported since API version 7 and deprecated since API version 9. You are advised to use **COMMON\_EVENT\_USER\_ADDED** instead.
    
    -   Value: **usual.event.USER\_ADDED**
    -   Required permissions: **ohos.permission.MANAGE\_LOCAL\_ACCOUNTS** (for system applications only)
-   **COMMON\_EVENT\_USER\_REMOVED(deprecated)** indicates that a user has been removed from the system.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/aa/v3/r52PCmJlQuu-c9IzjSbKow/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062358Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=183D5BF512BF738C9D519FD2A8313E7E089703CCA46FD011B0F6C285462317B2)
    
    This type is supported since API version 7 and deprecated since API version 9. You are advised to use **COMMON\_EVENT\_USER\_REMOVED** instead.
    
    -   Value: **usual.event.USER\_REMOVED**
    -   Required permissions: **ohos.permission.MANAGE\_LOCAL\_ACCOUNTS** (for system applications only)
-   **COMMON\_EVENT\_ABILITY\_ADDED(deprecated)** (reserved, not supported yet) indicates that an ability has been added.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/52/v3/zjmdibr-T4W6MoLzoRVyUw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062358Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=88BD2655E7341637F5C27BDDF0C36C912BC48537A043EB3EA5F9D448E8D0FBBF)
    
    This type is supported since API version 7 and deprecated since API version 9. You are advised to use [COMMON\_EVENT\_ABILITY\_ADDED](../../process-and-thread-communication/system-common-events/document.md#common_event_ability_added) instead.
    
    -   Value: **usual.event.ABILITY\_ADDED**
    -   Required permissions: **ohos.permission.LISTEN\_BUNDLE\_CHANGE**
-   **COMMON\_EVENT\_ABILITY\_REMOVED(deprecated)** (reserved, not supported yet) indicates that an ability has been removed.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/80/v3/DvLI4XLOTzCfPPxcK6L_yQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062358Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=D1AF89E088F6E67984A799FA7B4CCC104BE628E0AB1E7F869A4FC3F45231640A)
    
    This type is supported since API version 7 and deprecated since API version 9. You are advised to use [COMMON\_EVENT\_ABILITY\_REMOVED](../../process-and-thread-communication/system-common-events/document.md#common_event_ability_removed) instead.
    
    -   Value: **usual.event.ABILITY\_REMOVED**
    -   Required permissions: **ohos.permission.LISTEN\_BUNDLE\_CHANGE**
-   **COMMON\_EVENT\_ABILITY\_UPDATED(deprecated)** (reserved, not supported yet) indicates that an ability has been updated.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ba/v3/qQxZCARSSX-rXTcmm2_hlg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062358Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=0F3B97A22BF3486B1246B0C5D4EDC90BF03029CC4D4EA81E6B3454AD4ED22759)
    
    This type is supported since API version 7 and deprecated since API version 9. You are advised to use [COMMON\_EVENT\_ABILITY\_UPDATED](../../process-and-thread-communication/system-common-events/document.md#common_event_ability_updated) instead.
    
    -   Value: **usual.event.ABILITY\_UPDATED**
    -   Required permissions: **ohos.permission.LISTEN\_BUNDLE\_CHANGE**
-   **COMMON\_EVENT\_LOCATION\_MODE\_STATE\_CHANGED(deprecated)** (reserved, not supported yet) indicates that the location mode of the system has changed.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9d/v3/lVB07gLFTjKFwlKf4p8whg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062358Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=BCB88C9F0B44971C3545D98A04A97B48D9201494F3061704498663FB828392C9)
    
    This type is supported since API version 7 and deprecated since API version 9. You are advised to use [COMMON\_EVENT\_LOCATION\_MODE\_STATE\_CHANGED](../../process-and-thread-communication/system-common-events/document.md#common_event_location_mode_state_changed) instead.
    
    -   Value: **usual.event.location.MODE\_STATE\_CHANGED**
    -   Required permissions: none
-   **COMMON\_EVENT\_IVI\_SLEEP(deprecated)** (reserved, not supported yet) indicates that the in-vehicle infotainment (IVI) system of the vehicle is sleeping.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4f/v3/muv4nHqOTyeQuGX2MgLL-g/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062358Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=D8386932BF9D6366B0D47288D134840FC4D679FBDBF20CCD704DF845D0671DB0)
    
    This type is supported since API version 7 and deprecated since API version 9. You are advised to use [COMMON\_EVENT\_IVI\_SLEEP](../../process-and-thread-communication/system-common-events/document.md#common_event_ivi_sleep) instead.
    
    -   Value: **common.event.IVI\_SLEEP**
    -   Required permissions: none
-   **COMMON\_EVENT\_IVI\_PAUSE(deprecated)** (reserved, not supported yet) indicates that the IVI system of the vehicle is in sleep mode and notifies the application to stop playing.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/85/v3/FXgUx6VvRNGm9AebHZeBvg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062358Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=3B4F546DC157CF454F67170AF3E8AFE0F074F430F621D34A9E7E03F32F698C28)
    
    This type is supported since API version 7 and deprecated since API version 9. You are advised to use [COMMON\_EVENT\_IVI\_PAUSE](../../process-and-thread-communication/system-common-events/document.md#common_event_ivi_pause) instead.
    
    -   Value: **common.event.IVI\_PAUSE**
    -   Required permissions: none
-   **COMMON\_EVENT\_IVI\_STANDBY(deprecated)** (reserved, not supported yet) indicates that a third-party application in the IVI system of a vehicle is suspended.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e0/v3/iK175ETtTC-FIIhmtwcnTA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062358Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=2EB570747F536EDC876550110EAC7DBCD682462F552CEFF6FE9AE4A7CE396898)
    
    This type is supported since API version 7 and deprecated since API version 9. You are advised to use [COMMON\_EVENT\_IVI\_STANDBY](../../process-and-thread-communication/system-common-events/document.md#common_event_ivi_standby) instead.
    
    -   Value: **common.event.IVI\_STANDBY**
    -   Required permissions: none
-   **COMMON\_EVENT\_IVI\_LASTMODE\_SAVE(deprecated)** (reserved, not supported yet) indicates that the third-party application in the IVI system of the vehicle saves the last mode.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/78/v3/4QDAhYqyQ2C0nMBOm9f4fw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062358Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=9D3DCC5F6818DE600567D22EA8E380BA5A122060FA6AF420B639C914AE5EAE80)
    
    This type is supported since API version 7 and deprecated since API version 9. You are advised to use [COMMON\_EVENT\_IVI\_LASTMODE\_SAVE](../../process-and-thread-communication/system-common-events/document.md#common_event_ivi_lastmode_save) instead.
    
    -   Value: **common.event.IVI\_LASTMODE\_SAVE**
    -   Required permissions: none
-   **COMMON\_EVENT\_IVI\_VOLTAGE\_ABNORMAL(deprecated)** (reserved, not supported yet) indicates that the voltage of the vehicle's power system is abnormal.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8d/v3/laj34f_hSRiCnESSWA_ecw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062358Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=C0B13773BADE8EABE152F31655C4063C66B3C0AC826953DC2A856EF15A634449)
    
    This type is supported since API version 7 and deprecated since API version 9. You are advised to use [COMMON\_EVENT\_IVI\_VOLTAGE\_ABNORMAL](../../process-and-thread-communication/system-common-events/document.md#common_event_ivi_voltage_abnormal) instead.
    
    -   Value: **common.event.IVI\_VOLTAGE\_ABNORMAL**
    -   Required permissions: none
-   **COMMON\_EVENT\_IVI\_HIGH\_TEMPERATURE(deprecated)** (reserved, not supported yet) indicates that the temperature of the IVI system of the vehicle is too high.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/16/v3/dJC6hzo6SzOeb1SD0ZEdSQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062358Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=9BE6897AE854961F8CDBDD1AC04F266CC8DD40EBEB008379501025653C6CB689)
    
    This type is supported since API version 7 and deprecated since API version 9. You are advised to use [COMMON\_EVENT\_IVI\_HIGH\_TEMPERATURE](../../process-and-thread-communication/system-common-events/document.md#common_event_ivi_high_temperature) instead.
    
    -   Value: **common.event.IVI\_HIGH\_TEMPERATURE**
    -   Required permissions: none
-   **COMMON\_EVENT\_IVI\_EXTREME\_TEMPERATURE(deprecated)** (reserved, not supported yet) indicates that the temperature of the IVI system of the vehicle is extremely high.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ba/v3/Qb49tnrOT-K5viE6JUqGLQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062358Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=87C88BA36912609522D88FA182450F0ADA167715B17674AB14A034BD62A60F29)
    
    This type is supported since API version 7 and deprecated since API version 9. You are advised to use [COMMON\_EVENT\_IVI\_EXTREME\_TEMPERATURE](../../process-and-thread-communication/system-common-events/document.md#common_event_ivi_extreme_temperature) instead.
    
    -   Value: **common.event.IVI\_EXTREME\_TEMPERATURE**
    -   Required permissions: none
-   **COMMON\_EVENT\_IVI\_TEMPERATURE\_ABNORMAL(deprecated)** (reserved, not supported yet) indicates that the IVI system of the vehicle has an extreme temperature.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/af/v3/EKr_soA3QGuRiMAUvKL5Rw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062358Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=0C706AC666D53CEC8BE4C510695D75BCC0349C9D114A67765162A83AD59E4C05)
    
    This type is supported since API version 7 and deprecated since API version 9. You are advised to use [COMMON\_EVENT\_IVI\_TEMPERATURE\_ABNORMAL](../../process-and-thread-communication/system-common-events/document.md#common_event_ivi_temperature_abnormal) instead.
    
    -   Value: **common.event.IVI\_TEMPERATURE\_ABNORMAL**
    -   Required permissions: none
-   **COMMON\_EVENT\_IVI\_VOLTAGE\_RECOVERY(deprecated)** (reserved, not supported yet) indicates that the voltage of the vehicle's power system is restored to normal.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a6/v3/tWw00rYCRme3kEhEODH4zw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062358Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=BA94F4F9B92AAA67A6AACA110A48652D7CF1FEA99A39FE3202B1E2DD8FA4E0AF)
    
    This type is supported since API version 7 and deprecated since API version 9. You are advised to use [COMMON\_EVENT\_IVI\_VOLTAGE\_RECOVERY](../../process-and-thread-communication/system-common-events/document.md#common_event_ivi_voltage_recovery) instead.
    
    -   Value: **common.event.IVI\_VOLTAGE\_RECOVERY**
    -   Required permissions: none
-   **COMMON\_EVENT\_IVI\_TEMPERATURE\_RECOVERY(deprecated)** (reserved, not supported yet) indicates that the temperature of the IVI system is restored to normal.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/44/v3/dMC82Y6RSgGysMQzby3kFQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062358Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=996B5A093E8A9F15B6E213C3ADA27F2C3CD98418472947878FC0EAF1D607400F)
    
    This type is supported since API version 7 and deprecated since API version 9. You are advised to use [COMMON\_EVENT\_IVI\_TEMPERATURE\_RECOVERY](../../process-and-thread-communication/system-common-events/document.md#common_event_ivi_temperature_recovery) instead.
    
    -   Value: **common.event.IVI\_TEMPERATURE\_RECOVERY**
    -   Required permissions: none
-   **COMMON\_EVENT\_IVI\_ACTIVE(deprecated)** (reserved, not supported yet) indicates that the battery service of the vehicle-mounted system is active.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b4/v3/HBiKsHhRQK2Ex-EViCeD4A/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062358Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=5C1E7D896F764EB4A7F753C4FFCF5FC8F8D5754524420051C0B6A8DFBF7BC35D)
    
    This type is supported since API version 7 and deprecated since API version 9. You are advised to use [COMMON\_EVENT\_IVI\_ACTIVE](../../process-and-thread-communication/system-common-events/document.md#common_event_ivi_active) instead.
    
    -   Value: **common.event.IVI\_ACTIVE**
    -   Required permissions: none
-   **COMMON\_EVENT\_USB\_DEVICE\_ATTACHED(deprecated)** indicates that a USB device has been attached to the device functioning as a USB host.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/db/v3/zoD6V1l8R-6cLaISCJvDVg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062358Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=EE8522084B069D8E68D5DEAEFB848B4257DF288471DD087F94161994AD1AE8A2)
    
    This type is supported since API version 7 and deprecated since API version 9. You are advised to use [COMMON\_EVENT\_USB\_DEVICE\_ATTACHED](../../process-and-thread-communication/system-common-events/document.md#common_event_usb_device_attached) instead.
    
    -   Value: **usual.event.hardware.usb.action.USB\_DEVICE\_ATTACHED**
    -   Required permissions: none
-   **COMMON\_EVENT\_USB\_DEVICE\_DETACHED(deprecated)** indicates that a USB device has been detached from the device functioning as a USB host.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4f/v3/ney-djDyToO8MK2tPJzM9Q/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062358Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=4C19EFDE2684F8C2CD55B662855AD26BF405C5E54EECBB093D21D921251C1F18)
    
    This type is supported since API version 7 and deprecated since API version 9. You are advised to use [COMMON\_EVENT\_USB\_DEVICE\_DETACHED](../../process-and-thread-communication/system-common-events/document.md#common_event_usb_device_detached) instead.
    
    -   Value: **usual.event.hardware.usb.action.USB\_DEVICE\_DETACHED**
    -   Required permissions: none
-   **COMMON\_EVENT\_USB\_ACCESSORY\_ATTACHED(deprecated)** (reserved, not supported yet) indicates that a USB accessory was attached.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/35/v3/_t4_5A-wTu-5gsghv3NzGg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062358Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=302A9359509CF15D160B3F9212CD6E31231E2538EF7E534DA83064EE59E25857)
    
    This type is supported since API version 7 and deprecated since API version 9. You are advised to use [COMMON\_EVENT\_USB\_ACCESSORY\_ATTACHED](../../process-and-thread-communication/system-common-events/document.md#common_event_usb_accessory_attached) instead.
    
    -   Value: **usual.event.hardware.usb.action.USB\_ACCESSORY\_ATTACHED**
    -   Required permissions: none
-   **COMMON\_EVENT\_USB\_ACCESSORY\_DETACHED(deprecated)** (reserved, not supported yet) indicates that the USB attachment is uninstalled.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b8/v3/ROZqvHpGRHi9eYeNBPB_Zg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062358Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=5ED5B56E9E2B9A3018E91BAEB7D6C48029D8ABCB3FF754B2683EAA17636A810E)
    
    This type is supported since API version 7 and deprecated since API version 9. You are advised to use [COMMON\_EVENT\_USB\_ACCESSORY\_DETACHED](../../process-and-thread-communication/system-common-events/document.md#common_event_usb_accessory_detached) instead.
    
    -   Value: **usual.event.hardware.usb.action.USB\_ACCESSORY\_DETACHED**
    -   Required permissions: none
-   **COMMON\_EVENT\_DISK\_REMOVED(deprecated)** (reserved, not supported yet) indicates that an external storage device was removed.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/93/v3/LVrWA2sHR6O3dZdUqSYr3g/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062358Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=F280CEF39D77E35422FD4321B5B702D0F4485BD41A3ADFD09EF1935677C2A151)
    
    This type is supported since API version 7 and deprecated since API version 9. You are advised to use [COMMON\_EVENT\_DISK\_REMOVED](../../process-and-thread-communication/system-common-events/document.md#common_event_disk_removed) instead.
    
    -   Value: **usual.event.data.DISK\_REMOVED**
    -   Required permissions: **ohos.permission.STORAGE\_MANAGER** (for system applications only)
-   **COMMON\_EVENT\_DISK\_UNMOUNTED(deprecated)** (reserved, not supported yet) indicates that an external storage device was unmounted.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5b/v3/pu1HmD8lQ-yN4FinniasXw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062358Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=86188667C26B974826C6613D42C85E193710EB5F6726F61BE4DB6D1532C6924E)
    
    This type is supported since API version 7 and deprecated since API version 9. You are advised to use [COMMON\_EVENT\_DISK\_UNMOUNTED](../../process-and-thread-communication/system-common-events/document.md#common_event_disk_unmounted) instead.
    
    -   Value: **usual.event.data.DISK\_UNMOUNTED**
    -   Required permissions: **ohos.permission.STORAGE\_MANAGER** (for system applications only)
-   **COMMON\_EVENT\_DISK\_MOUNTED(deprecated)** (reserved, not supported yet) indicates that an external storage device was mounted.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fb/v3/pf83kWcpQ_CA31HOWWZOFQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062358Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=3FF2BF7D1E208BD699AEA58D712CFB851BE1B938160ACB0937775CBF6A3AECCA)
    
    This type is supported since API version 7 and deprecated since API version 9. You are advised to use [COMMON\_EVENT\_DISK\_MOUNTED](../../process-and-thread-communication/system-common-events/document.md#common_event_disk_mounted) instead.
    
    -   Value: **usual.event.data.DISK\_MOUNTED**
    -   Required permissions: **ohos.permission.STORAGE\_MANAGER** (for system applications only)
-   **COMMON\_EVENT\_DISK\_BAD\_REMOVAL(deprecated)** (reserved, not supported yet) indicates that an external storage device was removed without being unmounted.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b6/v3/HIZ91GGvQwW7YN8D-iH3Dg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062358Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=F190FE5822C74F87D9D0A61DEBA28F732C0CD1122A7DF8C3DCB7D141521BD1DF)
    
    This type is supported since API version 7 and deprecated since API version 9. You are advised to use [COMMON\_EVENT\_DISK\_BAD\_REMOVAL](../../process-and-thread-communication/system-common-events/document.md#common_event_disk_bad_removal) instead.
    
    -   Value: **usual.event.data.DISK\_BAD\_REMOVAL**
    -   Required permissions: **ohos.permission.STORAGE\_MANAGER** (for system applications only)
-   **COMMON\_EVENT\_DISK\_UNMOUNTABLE(deprecated)** (reserved, not supported yet) indicates that the external storage device cannot be mounted when a card is inserted.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a/v3/hmcjvxKLRYylsGmKtSF9Jg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062358Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=8C36C03CA4AE8568EEE952DD4B4D4567281E98789EC147A1F115D48014EF1DD9)
    
    This type is supported since API version 7 and deprecated since API version 9. You are advised to use [COMMON\_EVENT\_DISK\_UNMOUNTABLE](../../process-and-thread-communication/system-common-events/document.md#common_event_disk_unmountable) instead.
    
    -   Value: **usual.event.data.DISK\_UNMOUNTABLE**
    -   Required permissions: **ohos.permission.STORAGE\_MANAGER** (for system applications only)
-   **COMMON\_EVENT\_DISK\_EJECT(deprecated)** (reserved, not supported yet) indicates that the external storage medium has been ejected (interactive operation at the system software layer, not directly ejected physically).
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b9/v3/gthNnkXoSQmI5QdD_0lv0Q/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062358Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=41E8A3C0F9CFBD78535359774A119FEBF44CBD8E2D72BF6AE252C515E66E36F1)
    
    This type is supported since API version 7 and deprecated since API version 9. You are advised to use [COMMON\_EVENT\_DISK\_EJECT](../../process-and-thread-communication/system-common-events/document.md#common_event_disk_eject) instead.
    
    -   Value: **usual.event.data.DISK\_EJECT**
    -   Required permissions: **ohos.permission.STORAGE\_MANAGER** (for system applications only)
-   **COMMON\_EVENT\_VISIBLE\_ACCOUNTS\_UPDATED(deprecated)** (reserved, not supported yet) indicates that the account visibility changed.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/69/v3/JMR7c9bQR0iiKhwDSNNRRg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062358Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=DCDB29074D5B712C4E1E9452D36950D9429D889E19D127024B8972F4C9DAC3AB)
    
    This type is supported since API version 7 and deprecated since API version 9. You are advised to use [COMMON\_EVENT\_VISIBLE\_ACCOUNTS\_UPDATED](../../process-and-thread-communication/system-common-events/document.md#common_event_visible_accounts_updated) instead.
    
    -   Value: **usual.event.data.VISIBLE\_ACCOUNTS\_UPDATED**
    -   Required permissions: **ohos.permission.GET\_APP\_ACCOUNTS** (for system applications only)
-   **COMMON\_EVENT\_ACCOUNT\_DELETED(deprecated)** (reserved, not supported yet) indicates that an account was deleted.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8a/v3/aPRoS8N7S4GV1_mvFUbQFQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062358Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=6DD265CCFD49EF9313EF659246B38FE0E1364490670577A27E8BCF9EA013A690)
    
    This type is supported since API version 7 and deprecated since API version 9. You are advised to use [COMMON\_EVENT\_ACCOUNT\_DELETED](../../process-and-thread-communication/system-common-events/document.md#common_event_account_deleted) instead.
    
    -   Value: **usual.event.data.ACCOUNT\_DELETED**
    -   Required permissions: **ohos.permission.INTERACT\_ACROSS\_LOCAL\_ACCOUNTS** (for system applications only)
-   **COMMON\_EVENT\_FOUNDATION\_READY(deprecated)** (reserved, not supported yet) indicates that the foundation is ready.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/aa/v3/pey3fuMHT7WSI3NByZwCzA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062358Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=E770998875082DBACB69003A327AFBECDA99D2A8D5F2AD67B51FAD41E091B5C7)
    
    This type is supported since API version 7 and deprecated since API version 9. You are advised to use [COMMON\_EVENT\_FOUNDATION\_READY](../../process-and-thread-communication/system-common-events/document.md#common_event_foundation_ready) instead.
    
    -   Value: **usual.event.data.FOUNDATION\_READY**
    -   Required permissions: **ohos.permission.RECEIVER\_STARTUP\_COMPLETED** (for system applications only)
-   **COMMON\_EVENT\_AIRPLANE\_MODE\_CHANGED(deprecated)** indicates that the airplane mode of the device has changed.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8b/v3/CnjSqL1USG-A-YTU_EAEhA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062358Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=E04E2C87351AEAAFA180C473CC90180E4B10B944B7FD8C72EE8E22C8E61AE3C2)
    
    This type is supported since API version 7 and deprecated since API version 9. You are advised to use [COMMON\_EVENT\_AIRPLANE\_MODE\_CHANGED](../../process-and-thread-communication/system-common-events/document.md#common_event_airplane_mode_changed10) instead.
    
    -   Value: **usual.event.AIRPLANE\_MODE**
    -   Required permissions: none
-   **COMMON\_EVENT\_SPLIT\_SCREEN(deprecated)** indicates that the screen has been split.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c0/v3/_N7IgjUIREG4lEr16R4AzA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062358Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=3C32AE5051CEA2F2C98894711C770B36DB0BB31E110786B43EF9924892443A35)
    
    This type is supported since API version 8 and deprecated since API version 9. You are advised to use [COMMON\_EVENT\_SPLIT\_SCREEN](../../process-and-thread-communication/system-common-events/document.md#common_event_split_screen) instead.
