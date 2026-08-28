# Subscribing to Authentication Events

#### Use Cases

Starting from API version 20, unified security audit data multi-client subscription and unsubscription, filter adding and deletion, and authentication APIs are provided for apps to obtain security audit data on a device and perform subscription, filtering, and authentication as needed for auditing purposes.

| 
Audit Event ID

 | 

Description

 |
| :-- | :-- |
| 

0x1C801100

 | 

File creation authentication event.

 |
| 

0x1C801101

 | 

File opening authentication event.

 |
| 

0x1C801102

 | 

File renaming authentication event.

 |
| 

0x1C801103

 | 

File deletion authentication event.

 |
| 

0x1C801104

 | 

Authentication event for extended file attribute setting.

 |
| 

0x1C801105

 | 

Authentication event for extended file attribute deletion.

 |

#### Restrictions

1.  Currently, this capability is supported only on 2-in-1 devices.
2.  A maximum of two client instances can be created for a process, and a maximum of 16 client instances can be created for a device.
3.  A maximum of 256 positive filter values and 256 negative filter values can be set for a client instance. Events meeting the positive filter values are not returned to the subscriber, and events meeting the negative filter values are returned to the subscriber.

#### Service Process

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d1/v3/ecFnkcr2QRSxHQO2tasKkg/en-us_image_0000002515108431.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062007Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=95D2A0D232A10C04B142C352E8FDD391452648A7719A5CC4145FD00334792E66 "Click to enlarge")

The process is as follows:

1.  Create a client instance for subscribing to audit authentication events (hereinafter referred to as events) and provide a callback.
2.  Use the instance created in step 1 to subscribe to events by providing event IDs.
3.  Use the instance created in step 1 to set event filters by providing event IDs and filter information.
4.  When an event occurs, the audit service filters the event based on the specified filter. If the event meets the filter, the callback is triggered to notify the client that has subscribed to the event.
5.  Formulate an authentication policy based on audit data.
6.  Use the instance created in step 1 to set the authentication policy for the received event.
7.  When the service ends, use the instance created in step 1 to delete filters and unsubscribe from the events.
8.  Delete the instance created in step 1.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/41/v3/qI4XdX_-T0qCI83cAnN--w/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062007Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=8D00045F54E4E07A77970E759C2E302AA842B9A8B6C4EF0C5067FA60671FCCA9)
    
    You can also set filters before subscribing to events.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a0/v3/i6AiCxJYSPyDBwqtZw2snw/caution_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062007Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=E0600E193FDCBE8BB3A7B178C8871CB602A7129D3992435782A06320559DAA1B)
    
    After an instance is deleted, all subscriptions and filters of the instance are removed.
    

#### API Description

For details about the APIs, please refer to [API Reference](https://developer.huawei.com/consumer/en/doc/harmonyos-references/devicesecurity-securityaudit-api#section1768135711112).

| 
API

 | 

Description

 |
| :-- | :-- |
| 

newAuthClient(callback: Callback<AuditEvent>): AuthClient;

 | 

Creates an audit authentication event management object (AuthClient). The AuthClient provides the subscription, unsubscription, event filter adding, event filter deletion, and authentication functions.

 |
| 

deleteAuthClient(client: AuthClient): void;

 | 

Deletes an audit authentication event management object.

 |
| 

interface AuthClient {

subscribe(events: AuthEvent\[\]): void;

}

 | 

Subscribes to audit authentication events.

 |
| 

interface AuthClient {

unsubscribe(events: AuthEvent\[\]): void;

}

 | 

Unsubscribes from audit authentication events.

 |
| 

interface AuthClient {

addFilter(event: AuthEvent, filter: Filter): void;

}

 | 

Adds a filter for an audit authentication event.

 |
| 

interface AuthClient {

removeFilter(event: AuthEvent, filter: Filter): void;

}

 | 

Deletes a filter of an audit authentication event.

 |
| 

interface AuthClient {

auth(auditEvent: AuditEvent, authResult: AuthResult): void;

}

 | 

Sets the authentication result for an audit authentication event.

 |

#### Development Procedure

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/61/v3/_PFst2WNRs2izdbEVpWx9g/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062007Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=102663410A0B23F14980B76028777CFF8C5F2E081F119BC61DBA7A1122309545)

-   When preparing for the development, you need to apply for the **ohos.permission.kernel.AUTH\_AUDIT\_EVENT** permission.
-   Only enterprise apps in the trustlist can apply for this permission. For details about how to apply for this permission, please refer to [Permissions for Enterprise Applications](../../../../application-access-control/application-permission-management/application-permissions/permissions-for-enterprise-applications/document.md).

1.  Import the Device Security Kit module and related public modules.
    
    import { securityAudit } from '@kit.DeviceSecurityKit'; 
    import { BusinessError } from '@kit.BasicServicesKit'; 
    import { hilog } from '@kit.PerformanceAnalysisKit';
    
2.  Use the callback function containing the authentication policy to create a client instance for audit authentication event management.
    
    const TAG = "SecurityAuditAuthJsTest";
    let authClient: securityAudit.AuthClient | undefined = undefined;
    const allowEventCallback = (event: securityAudit.AuditEvent) => {
      hilog.info(0x0000, TAG, '%{public}s', 'Security\_SecurityAudit\_Auth\_JsApi\_Func eventId= ' + event.eventId);
      hilog.info(0x0000, TAG, '%{public}s', 'Security\_SecurityAudit\_Auth\_JsApi\_Func content= ' + event.content);
      hilog.info(0x0000, TAG, '%{public}s', 'Security\_SecurityAudit\_Auth\_JsApi\_Func metadata= ' + event.metadata);
      try {
        authClient?.auth(event, securityAudit.AuthResult.ALLOW);
      } catch (error) {
        let e: BusinessError = error as BusinessError;
        hilog.error(0x0000, TAG, 'allowEventCallback', 'auth error:' + e.code);
      }
    };
    try {
      authClient = securityAudit.newAuthClient(allowEventCallback);
    } catch (err) {
      let e: BusinessError = err as BusinessError;
      hilog.error(0x0000, TAG, 'newAuthClient failed: %{public}d %{public}s', e.code, e.message);
    }
    
3.  Subscribe to an audit authentication event.
    
    try {
      hilog.info(0x0000, TAG, 'subscribe begin.');
      authClient?.subscribe(\[securityAudit.AuthEvent.FILE\_CREATE\]);
      hilog.info(0x0000, TAG, 'Succeeded in subscribe.');
    } catch (err) {
      let e: BusinessError = err as BusinessError;
      hilog.error(0x0000, TAG, 'subscribe failed: %{public}d %{public}s', e.code, e.message);
    }
    
4.  Add a filter for the audit authentication event.
    
    let filter : securityAudit.Filter = {
      type: securityAudit.FilterType.PROCESS\_PID\_EQUAL,
      isInclude: true,
      values : \["2"\]
    };
    try {
      hilog.info(0x0000, TAG, 'addFilter begin.');
      authClient?.addFilter(securityAudit.AuthEvent.FILE\_CREATE, filter);
      hilog.info(0x0000, TAG, 'Succeeded in addFilter.');
    } catch (err) {
      let e: BusinessError = err as BusinessError;
      hilog.error(0x0000, TAG, 'addFilter failed: %{public}d %{public}s', e.code, e.message);
    }
    
5.  Unsubscribe from the audit authentication event.
    
    try {
      hilog.info(0x0000, TAG, 'unsubscribe begin.');
      authClient?.unsubscribe(\[securityAudit.AuthEvent.FILE\_CREATE\]);
      hilog.info(0x0000, TAG, 'Succeeded in unsubscribe.');
    } catch (err) {
      let e: BusinessError = err as BusinessError;
      hilog.error(0x0000, TAG, 'unsubscribe failed: %{public}d %{public}s', e.code, e.message);
    }
    
6.  Delete the filter of the audit authentication event.
    
    try {
      hilog.info(0x0000, TAG, 'removeFilter begin.');
      authClient?.removeFilter(securityAudit.AuthEvent.FILE\_CREATE, filter);
      hilog.info(0x0000, TAG, 'Succeeded in removeFilter.');
    } catch (err) {
      let e: BusinessError = err as BusinessError;
      hilog.error(0x0000, TAG, 'removeFilter failed: %{public}d %{public}s', e.code, e.message);
    }
    
7.  Delete the client instance for audit authentication event management.
    
    try {
      securityAudit.deleteAuthClient(authClient);
    } catch (err) {
      let e: BusinessError = err as BusinessError;
      hilog.error(0x0000, TAG, 'deleteAuthClient failed: %{public}d %{public}s', e.code, e.message);
    }
