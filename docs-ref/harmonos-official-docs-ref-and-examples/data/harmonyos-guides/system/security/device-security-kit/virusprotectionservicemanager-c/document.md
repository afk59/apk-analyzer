# VirusProtectionServiceManager (C)

#### Use Cases

Since 6.0.0(20), after a third-party Endpoint Detection and Response (EDR) app is registered with Device Security Kit, it can call the registration, update, and uninstallation (data deletion) APIs to submit its app information to the HarmonyOS VirusProtectionService for unified management. After a zero trust app is registered with Device Security Kit, it can query the list of all registered EDR apps (including the package name, current version number, last update time, antivirus switch status, and user ID). After a Mobile Device Management (MDM) app is registered with Device Security Kit, the enterprise administrator can enable or disable the HarmonyOS VirusProtectionService through the MDM app.

#### Restrictions

1.  Currently, this capability is supported only on 2-in-1 devices.
2.  Concurrent calls are not supported. Only one third-party EDR app or MDM app can call the API of this module at a time.

#### Service Process

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/21/v3/Kv8r9HdgQkivS0J1qrSYIA/en-us_image_0000002515108417.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062008Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=C55D577587758396460399DB139353A9FD3E62A75AEAA5CF0CB447D663A9112D)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7b/v3/PeBb3qQWSe6CWWzAxqiEPw/en-us_image_0000002482788456.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062008Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=803EA029167DF981C0ABA4C1A4606D4883E0FE24B559A9F48761C05A179A4218)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8c/v3/lW-9vFOxRrCBSQB_ZYnx8Q/en-us_image_0000002482908418.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062008Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=EA6A3C97469A97E9075D4269D93C8CBD8AF7D77EE0FD62CFFF338A5166847221)

The process is as follows:

1.  A third-party EDR app calls the API of this module to synchronize its information to the HarmonyOS VirusProtectionService during registration, update, or uninstallation.
2.  A zero trust app calls the API of this module to query information about all registered third-party EDR apps.
3.  An MDM app calls the API of this module to enable or disable the HarmonyOS VirusProtectionService.

#### API Description

The following table lists the APIs of the VirusProtectionServiceManager service. For details about the APIs, please refer to [API Reference](https://developer.huawei.com/consumer/en/doc/harmonyos-references/devicesecurity-capi-securityantivirus).

| 
API

 | 

Description

 |
| :-- | :-- |
| 

SecurityAntivirus\_ErrCode HMS\_SecurityAntivirus\_RegisterAntivirus(const char\* bundleName)

 | 

Called by a third-party EDR app to register with the HarmonyOS VirusProtectionService.

 |
| 

SecurityAntivirus\_ErrCode HMS\_SecurityAntivirus\_UnregisterAntivirus(const char\* bundleName)

 | 

Called by a third-party EDR app to unregister from the HarmonyOS VirusProtectionService.

 |
| 

SecurityAntivirus\_ErrCode HMS\_SecurityAntivirus\_UpdateAntivirus(const SecurityAntivirus\_Antivirus\* antivirus)

 | 

Called by a third-party EDR app to update its information, including the package name, current version number, last update time, antivirus switch status, and user ID, to the HarmonyOS VirusProtectionService.

 |
| 

SecurityAntivirus\_ErrCode HMS\_SecurityAntivirus\_QueryAntivirus(SecurityAntivirus\_Antivirus\*\* list, uint32\_t\* length)

 | 

Called by a zero trust app to query the HarmonyOS VirusProtectionService for the registration information of all third-party EDR apps.

 |
| 

SecurityAntivirus\_ErrCode HMS\_SecurityAntivirus\_QueryPreinstalledAntivirus

(SecurityAntivirus\_Antivirus\*\* list, uint32\_t\* length)

 | 

Called by an MDM app to query the HarmonyOS VirusProtectionService for the antivirus function status of all users.

 |
| 

SecurityAntivirus\_ErrCode HMS\_SecurityAntivirus\_EnablePreinstalledAntivirus(void)

 | 

Called by an MDM app to enable the antivirus function of the HarmonyOS VirusProtectionService for all users.

 |
| 

SecurityAntivirus\_ErrCode HMS\_SecurityAntivirus\_DisablePreinstalledAntivirus(void)

 | 

Called by an MDM app to disable the antivirus function of the HarmonyOS VirusProtectionService for all users.

 |
| 

SecurityAntivirus\_ErrCode HMS\_SecurityAntivirus\_EnablePreinstalledAntivirusByAccount(int32\_t accountId)

 | 

Called by an MDM app to enable the antivirus function of the HarmonyOS VirusProtectionService for a user with the specified **accountId**.

 |
| 

SecurityAntivirus\_ErrCode HMS\_SecurityAntivirus\_DisablePreinstalledAntivirusByAccount(int32\_t accountId)

 | 

Called by an MDM app to disable the antivirus function of the HarmonyOS VirusProtectionService for a user with the specified **accountId**.

 |

#### Development Procedure

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8e/v3/eP2i6RgBTPaJPIVksbTKUQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062008Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=A1487DA2588A9CB2E325ED86DBDF5021EC35612CCE62A9923F2850E83A83B148)

-   When preparing for the development, you need to apply for the **ohos.permission.REGISTER\_ANTIVIRUS**, **ohos.permission.MANAGE\_ANTIVIRUS**, and **ohos.permission.MANAGE\_PREINSTALLED\_ANTIVIRUS** permissions.
-   Only apps in the trustlist can apply for these permissions. For details, please refer to [Permissions for Enterprise Applications](../../application-access-control/application-permission-management/application-permissions/permissions-for-enterprise-applications/document.md) and [Permissions for MDM Applications](../../application-access-control/application-permission-management/application-permissions/permissions-for-mdm-applications/document.md).

1.  Import and link the VirusProtectionServiceManager shared library in **CMakeLists.txt**.
    
    find\_library(dsm-lib libsecurityantivirus\_ndk.z.so)
    target\_link\_libraries(entry PUBLIC libace\_napi.z.so ${dsm-lib})
    
2.  Import the VirusProtectionServiceManager header file.
    
    #include <cstdio>
    #include <cstdlib>
    #include "DeviceSecurityKit/security\_antivirus.h"
    
3.  The EDR app calls the APIs to synchronize registration, uninstallation, and update information to the HarmonyOS VirusProtectionService. The **ohos.permission.REGISTER\_ANTIVIRUS** permission is required.
    
    const char \*regisBundleName = "\*\*\*\*"; // Construct the input parameter for the registration API.
    int ret = HMS\_SecurityAntivirus\_RegisterAntivirus(regisBundleName);
    printf("HMS\_SecurityAntivirus\_RegisterAntivirus ret = %d \\n", ret);
    
    const char \*unRegisBundleName = "\*\*\*\*"; // Construct the input parameter for the uninstallation API.
    ret = HMS\_SecurityAntivirus\_UnregisterAntivirus(unRegisBundleName);
    printf("HMS\_SecurityAntivirus\_UnregisterAntivirus ret = %d \\n", ret);
    
    SecurityAntivirus\_Antivirus updateAntivirus; // Construct the input parameter for the update API.
    ret = HMS\_SecurityAntivirus\_UpdateAntivirus(&updateAntivirus);
    printf("HMS\_SecurityAntivirus\_UpdateAntivirus ret = %d \\n", ret);
    
4.  The zero trust app calls the API to query the HarmonyOS VirusProtectionService for the information about all the registered third-party EDR apps. The **ohos.permission.MANAGE\_ANTIVIRUS** permission is required.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/95/v3/tnLlJz5qTLqaeQTw8yz3Ig/caution_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062008Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=4F03CCEF65BD261D62EBB6A2F81C18E26DE60C9D09862AB2DDCFD7B36FE322D5)
    
    After processing services based on the app process information, the zero trust app needs to release the memory allocated for the input and output parameters of the query API.
    
    SecurityAntivirus\_Antivirus \*list = nullptr; // Construct output parameter 1 of the query API.
    uint32\_t length = 0; // Construct output parameter 2 of the query API.
    int ret = HMS\_SecurityAntivirus\_QueryAntivirus(&list, &length);
    printf("HMS\_SecurityAntivirus\_QueryAntivirus ret = %d \\n", ret);
    for (uint32\_t i = 0; i < length; ++i) {
        free((char\*)(list\[i\].bundleName)); // Release the memory allocated for the internal character string of the output parameter.
        free((char\*)(list\[i\].metadata));
    }
    free(list); // Release the memory allocated for the output parameter array itself.
    
5.  The MDM app calls the required API to enable or disable the HarmonyOS VirusProtectionService. The **ohos.permission.MANAGE\_PREINSTALLED\_ANTIVIRUS** permission is required.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ef/v3/0acwlQCERfiiR7wm2HiC-Q/caution_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062008Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=CEC383F410D34FE7ED9F48ED2F793D473C88E341916D034098F46DFE7D07AB06)
    
    After processing services based on the app process information, the MDM app needs to release the memory allocated for the input and output parameters of the query API.
    
    SecurityAntivirus\_Antivirus \*list = nullptr; // Construct output parameter 1 of the query API.
    uint32\_t length = 0; // Construct output parameter 2 of the query API.
    int ret = HMS\_SecurityAntivirus\_QueryPreinstalledAntivirus(&list, &length);
    printf("HMS\_SecurityAntivirus\_QueryPreinstalledAntivirus ret = %d \\n", ret);
    for (uint32\_t i = 0; i < length; ++i) {
        free((char\*)(list\[i\].bundleName)); // Release the memory allocated for the internal character string of the output parameter.
        free((char\*)(list\[i\].metadata));
    }
    free(list); // Release the memory allocated for the output parameter array itself.
    
    ret = HMS\_SecurityAntivirus\_EnablePreinstalledAntivirus();
    printf("HMS\_SecurityAntivirus\_EnablePreinstalledAntivirus ret = %d \\n", ret);
    
    ret = HMS\_SecurityAntivirus\_DisablePreinstalledAntivirus();
    printf("HMS\_SecurityAntivirus\_DisablePreinstalledAntivirus ret = %d \\n", ret);
    
    int32\_t accountId = 0; // Construct a valid user ID.
    ret = HMS\_SecurityAntivirus\_EnablePreinstalledAntivirusByAccount(accountId);
    printf("HMS\_SecurityAntivirus\_EnablePreinstalledAntivirusByAccount ret = %d \\n", ret);
    
    ret = HMS\_SecurityAntivirus\_DisablePreinstalledAntivirusByAccount(accountId );
    printf("HMS\_SecurityAntivirus\_DisablePreinstalledAntivirusByAccount ret = %d \\n", ret);
