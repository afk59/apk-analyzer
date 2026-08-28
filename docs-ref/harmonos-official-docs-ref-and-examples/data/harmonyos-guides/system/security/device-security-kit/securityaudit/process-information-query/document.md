# Process Information Query

#### Use Cases

Starting from API version 20, the app process information query API is provided to obtain information about the started app processes on a device. The process information includes the process ID, command line, parent process PID, user ID, user group ID, process start time, process owner ID type, and process owner ID.

#### Restrictions

1.  Currently, this capability is supported only on 2-in-1 devices.
2.  The maximum number of processes that can be queried at a time is 16.

#### Service Process

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ba/v3/ZAWDoOpaSVWJttc8lS6CQg/en-us_image_0000002482788482.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062007Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=8D10CBE757C6322ECBB9BC498B593C20E734E4B313C90EC592EE85B5CD359A33)

The process is as follows:

1.  An HAP calls the query API to obtain the app process information.
2.  Device Security Kit synchronously returns the app process information to the HAP, which then processes services based on the returned information.

#### API Description

The following table lists the APIs. For details about the APIs, please refer to [API Reference](https://developer.huawei.com/consumer/en/doc/harmonyos-references/devicesecurity-securityaudit-api#section764412911237).

| 
API

 | 

Description

 |
| :-- | :-- |
| 

queryAllProcesses(): string

 | 

Obtains the information about all app processes.

 |
| 

queryProcesses(pids: number\[\]): string

 | 

Obtains the information about app processes with the specified PIDs.

 |

#### Development Procedure

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/48/v3/lxaq0irKRGS2Ysk_bYHmEA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062007Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=755389D1D8C040522EEC976861BA2853E8D7181238F333EF7B3E4DC5BC00F41A)

-   When preparing for the development, you need to apply for the **ohos.permission.QUERY\_AUDIT\_EVENT** permission.
-   Only enterprise apps in the trustlist can apply for this permission. For details about how to apply for this permission, please refer to [Permissions for Enterprise Applications](../../../application-access-control/application-permission-management/application-permissions/permissions-for-enterprise-applications/document.md).

1.  Import the Device Security Kit module and related public modules.
    
    import { securityAudit } from '@kit.DeviceSecurityKit'; 
    import { BusinessError} from '@kit.BasicServicesKit'; 
    import { hilog } from '@kit.PerformanceAnalysisKit';
    
2.  Obtain the information about a single app process or all app processes.
    
    -   Obtain the information about a single app process.
        
        const TAG = "SecurityAuditJsTest"; 
        let pids: number\[\] = \[3622\];
        try { 
          hilog.info(0x0000, TAG, 'queryProcesses begin.'); 
          const result = securityAudit.queryProcesses(pids);
          hilog.info(0x0000, TAG, 'Succeeded in queryProcesses.'); 
        } catch (err) { 
          let e: BusinessError = err as BusinessError; 
          hilog.error(0x0000, TAG, 'queryProcesses failed: %{public}d %{public}s', e.code, e.message); 
        }
        
    
    -   Obtain the information about all app processes.
        
        const TAG = "SecurityAuditJsTest"; 
        try { 
          hilog.info(0x0000, TAG, 'queryAllProcesses begin.'); 
          const result = securityAudit.queryAllProcesses();
          hilog.info(0x0000, TAG, 'Succeeded in queryAllProcesses.'); 
        } catch (err) { 
          let e: BusinessError = err as BusinessError; 
          hilog.error(0x0000, TAG, 'queryAllProcesses failed: %{public}d %{public}s', e.code, e.message);
        }
