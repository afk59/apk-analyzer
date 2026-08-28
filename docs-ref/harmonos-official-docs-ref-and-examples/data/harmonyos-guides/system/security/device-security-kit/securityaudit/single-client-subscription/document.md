# Single-Client Subscription

#### Use Cases

Unified security audit data single-client subscription and unsubscription APIs are provided for apps to obtain security audit data on a device for auditing purposes.

| 
Audit Event ID

 | 

Description

 |
| :-- | :-- |
| 

0x027000000

 | 

Clipboard copy and paste events.

 |
| 

0x810800800

 | 

Sign-in and sign-out events.

 |
| 

0x007000000

 | 

Screenshot, screen recording, and screen projection events.

 |
| 

0x00F000000

 | 

Insertion and removal events of removable storage devices such as USB flash drives and memory cards.

 |
| 

0x02E000000

 | 

Printer event.

 |
| 

0x01C000007

 | 

File event.

 |
| 

0x01C000008

 | 

Process creation and exit events.

 |
| 

0x01C000009

 | 

Network event.

 |
| 

0x01C00000A

 | 

KIA file interception event.

 |
| 

0x02D000000

 | 

Camera event.

 |
| 

0x010000000

 | 

App event.

 |
| 

0x011000000

 | 

Enterprise device management event.

 |
| 

0x012003000

 | 

Certificate operation event.

 |
| 

0x01C00000B

 | 

KIA file adding event.

 |
| 

0x01C00000C

 | 

KIA file variation event.

 |
| 

0x01C00000E

 | 

Network traffic event.

 |
| 

0x01C00000F

 | 

Network connection event.

 |
| 

0x00B000000

 | 

App permission change event.

 |
| 

0x003000001

 | 

DNS audit event.

 |

#### Restrictions

Currently, this capability is supported only on 2-in-1 devices.

#### Service Process

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/36/v3/Xbt0PQ1sTJSAvYp1LAlvqw/en-us_image_0000002482908430.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062007Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=44C34A85E335057B3111F9DD54E8CEB8DF5C8F92DF2D4AF9DF28823B76FD6188)

The process is as follows:

1.  Your app subscribes to security audit data.
2.  Device Security Kit calls the callback function to notify your app. Your app processes the service based on the audit data.
3.  Your app unsubscribes from security audit data based on service needs.

#### API Description

The following table lists the security audit data subscription and unsubscription APIs. For details, please refer to [API Reference](https://developer.huawei.com/consumer/en/doc/harmonyos-references/devicesecurity-securityaudit-api#section10996135475216).

| 
API

 | 

Description

 |
| :-- | :-- |
| 

on(type: 'auditEventOccur', auditEventInfo: AuditEventInfo, callback: Callback<AuditEvent>): void

 | 

Subscribes to security audit data.

 |
| 

off(type: 'auditEventOccur', auditEventInfo: AuditEventInfo, callback?: Callback<AuditEvent>): void

 | 

Unsubscribes from security audit data.

 |

#### Development Procedure

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cd/v3/BItMf2VGTIK3-7nJW--sVg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062007Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=2E467B402302ED2838E53F8A1EA801B14F1B327B18CB421A6D1D786B4DE2A413)

-   When preparing for the development, you need to apply for the **ohos.permission.QUERY\_AUDIT\_EVENT** permission.
-   Only enterprise apps in the trustlist can apply for this permission. For details about how to apply for this permission, please refer to [Permissions for Enterprise Applications](../../../application-access-control/application-permission-management/application-permissions/permissions-for-enterprise-applications/document.md).

1.  Import the Device Security Kit module and related public modules.
    
    import { securityAudit } from '@kit.DeviceSecurityKit'; 
    import { BusinessError} from '@kit.BasicServicesKit'; 
    import { hilog } from '@kit.PerformanceAnalysisKit';
    
2.  Subscribe to a security audit event.
    
    const TAG = "SecurityAuditJsTest"; 
    const callback = (event: securityAudit.AuditEvent) => { 
      hilog.info(0x0000, TAG, '%{public}s', 'Security\_SecurityAudit\_JsApi\_Func eventId= ' + event.eventId); 
      hilog.info(0x0000, TAG, '%{public}s', 'Security\_SecurityAudit\_JsApi\_Func version= ' + event.version); 
      hilog.info(0x0000, TAG, '%{public}s', 'Security\_SecurityAudit\_JsApi\_Func content= ' + event.content); 
      hilog.info(0x0000, TAG, '%{public}s', 'Security\_SecurityAudit\_JsApi\_Func timestamp= ' + event.timestamp); 
      hilog.info(0x0000, TAG, '%{public}s', 'Security\_SecurityAudit\_JsApi\_Func userId= ' + event.userId); 
      hilog.info(0x0000, TAG, '%{public}s', 'Security\_SecurityAudit\_JsApi\_Func deviceId= ' + event.deviceId); 
    }; 
    let auditEventInfo: securityAudit.AuditEventInfo = { 
       eventId: 0x810800800 
    }; 
     
    try { 
      hilog.info(0x0000, TAG, 'on begin.'); 
      securityAudit.on('auditEventOccur', auditEventInfo, callback); 
      hilog.info(0x0000, TAG, 'Succeeded in on.'); 
    } catch (err) { 
      let e: BusinessError = err as BusinessError; 
      hilog.error(0x0000, TAG, 'on failed: %{public}d %{public}s', e.code, e.message); 
    }
    
3.  Unsubscribe from the security audit event.
    
    try { 
      hilog.info(0x0000, TAG, 'off begin.'); 
      securityAudit.off('auditEventOccur', auditEventInfo, callback); 
      hilog.info(0x0000, TAG, 'Succeeded in off.'); 
    } catch (err) { 
      let e: BusinessError = err as BusinessError; 
      hilog.error(0x0000, TAG, 'off failed: %{public}d %{public}s', e.code, e.message); 
    }
