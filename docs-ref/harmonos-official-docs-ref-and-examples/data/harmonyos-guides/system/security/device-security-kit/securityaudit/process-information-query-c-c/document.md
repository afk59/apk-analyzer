# Process Information Query (C/C++)

#### Use Cases

Starting from API version 20, the app process information query API is provided to obtain information about the started app processes on a device. The process information includes the process ID, command line, parent process PID, user ID, user group ID, process start time, process owner ID type, and process owner ID.

#### Restrictions

1.  Currently, this capability is supported only on 2-in-1 devices.
2.  The maximum number of processes that can be queried at a time is 16.

#### Service Process

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4a/v3/E2gFMnT4RCO3c0dgso2sfA/en-us_image_0000002514988435.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062007Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=FC3F81C006836D32D65E51052398471F713E28AC2D0388917C7DFB093E937089)

The process is as follows:

1.  An HAP calls the query API to obtain the app process information.
2.  Device Security Kit synchronously returns the app process information to the HAP, which then processes services based on the returned information.

#### API Description

The following table lists the APIs. For details about the APIs, please refer to [API Reference](https://developer.huawei.com/consumer/en/doc/harmonyos-references/devicesecurity-capi-securityaudit#en-us_topic_0000002349017400_section0945443114617).

| 
API

 | 

Description

 |
| :-- | :-- |
| 

int32\_t HMS\_SecurityAudit\_QueryAllProcesses(char\*\* result)

 | 

Obtains the information about all app processes.

 |
| 

int32\_t HMS\_SecurityAudit\_QueryProcesses(uint64\_t\* pids, uint64\_t count, char\*\* result)

 | 

Obtains the information about app processes with the specified PIDs.

 |

#### Development Procedure

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/46/v3/ve7j8oywQ8yDO5Iypdk9LQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062007Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=D4633FA6C62980E949A2FE0CDE503ECA88F27614D40CA9554370F75CB7AEE36F)

-   When preparing for the development, you need to apply for the **ohos.permission.QUERY\_AUDIT\_EVENT** permission.
-   Only enterprise apps in the trustlist can apply for this permission. For details about how to apply for this permission, please refer to [Permissions for Enterprise Applications](../../../application-access-control/application-permission-management/application-permissions/permissions-for-enterprise-applications/document.md).

1.  Import and link the security audit shared library in **CMakeLists.txt**.
    
    find\_library(dsm-lib libsecurityaudit\_ndk.z.so)
    target\_link\_libraries(entry PUBLIC libace\_napi.z.so ${dsm-lib})
    
2.  Import the security audit header file.
    
    #include <DeviceSecurityKit/security\_audit.h>
    #include <cstdio>
    
3.  Obtain the information about a single app process or all app processes.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6/v3/b4cu6JLkT_WSRBGFzfZHRQ/caution_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062007Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=4B284E4A2B9A5951CA3BE989EA9B6E7259FE7FE74CA99DF2888D3C404A9F3743)
    
    After processing services based on the app process information, the app needs to release the memory allocated for the input and output parameters of the query API.
    
    -   Call the **HMS\_SecurityAudit\_QueryProcesses** API to obtain the information about a single app process.
    
    char \*result = nullptr;
    uint64\_t pids\[\] = {3266};
    int32\_t ret = HMS\_SecurityAudit\_QueryProcesses(pids, sizeof(pids)/sizeof(pids\[0\]), &result);
    if (ret == 0 && result != nullptr) {
        printf("HMS\_SecurityAudit\_QueryProcesses result: %s\\n", result);
    } else {
        printf("HMS\_SecurityAudit\_QueryProcesses failed with error: %d\\n", ret);
    }
    if (result != nullptr) {
        delete\[\] result;
        result = nullptr;
    }
    
    -   Call the **HMS\_SecurityAudit\_QueryAllProcesses** API to obtain the information about all app processes.
    
    char \*result = nullptr;
    int32\_t ret = HMS\_SecurityAudit\_QueryAllProcesses(&result);
    if (ret == 0 && result != nullptr) {
        printf("HMS\_SecurityAudit\_QueryAllProcesses result: %s\\n", result);
    } else {
        printf("HMS\_SecurityAudit\_QueryAllProcesses failed with error: %d\\n", ret);
    }
    if (result != nullptr) {
        delete\[\] result;
        result = nullptr;
    }
