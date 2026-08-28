# Subscribing to Notification Events

#### Use Cases

Starting from API version 20, unified security audit data muti-client subscription and unsubscription APIs as well as filter adding and deletion APIs are provided for apps to obtain security audit data on a device based on filters, for auditing purposes.

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

0x010000100

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

0x01C000012

 | 

KIA file read event.

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
| 

0x01C001100

 | 

File interception event.

 |
| 

0x018000100

 | 

App installation interception event.

 |
| 

0x018000101

 | 

App uninstallation interception event.

 |
| 

0x018000102

 | 

App update interception event.

 |
| 

0x018000103

 | 

App restoration interception event.

 |
| 

0x018000104

 | 

App startup interception event.

 |
| 

0x030000000

 | 

USB access interception event.

 |

#### Restrictions

1.  Currently, this capability is supported only on 2-in-1 devices.
2.  A maximum of two client instances can be created for a process, and a maximum of 16 client instances can be created for a device.
3.  A maximum of 256 filters can be set for a client instance, and each filter can have a maximum of 10 values.

#### Service Process

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/95/v3/FO3xh_8JT4eDhjvTGYqRkw/en-us_image_0000002482908436.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062007Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=34F532E22322FE0DDBDB723D1F2B76CA7404244D1AE9CEA3F0DD7E4A0F48116F)

The process is as follows:

1.  Create a client instance for subscribing to audit notification events (hereinafter referred to as events) and provide a callback.
2.  Use the instance created in step 1 to subscribe to events by providing event IDs.
3.  Use the instance created in step 1 to set event filters by providing event IDs and filter information.
4.  When an event occurs, the audit service filters the event based on the specified filter. If the event meets the filter, the callback is triggered to notify the client that has subscribed to the event.
5.  Process services based on the audit data.
6.  If the audit data does not need to be filtered or used any more, use the instance created in step 1 to delete filters and unsubscribe from the events.
7.  If the instance does not need to used any more, delete it.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6e/v3/9mBq4jdeS_SKbEagBOMu_Q/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062007Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=B1409B7E25C8701352F31154E4105984C5C225178233048C2C62AE5176BDC4F5)
    
    You can also set filters before subscribing to events.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/76/v3/fWKMmHGOSIWH47KTfrAOtg/caution_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062007Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=7F1FA66DAB3A1F3C358C3F3AD26792E27622F785D63DA3C4BBB15A56935724A6)
    
    After an instance is deleted, all subscriptions and filters of the instance are removed.
    

#### API Description

For details about the APIs, please refer to [API Reference](https://developer.huawei.com/consumer/en/doc/harmonyos-references/devicesecurity-securityaudit-api#section1137616421363).

| 
API

 | 

Description

 |
| :-- | :-- |
| 

newClient(callback: Callback<AuditEvent>): Client

 | 

Creates an audit notification event management object (client). The client provides the subscription, unsubscription, event filter adding, and event filter deletion functions.

 |
| 

deleteClient(client:Client): void

 | 

Deletes an audit notification event management object.

 |
| 

subscribe(events: NotifyEvent\[\]): void

 | 

Subscribes to audit notification events.

 |
| 

unsubscribe(events: NotifyEvent\[\]): void

 | 

Unsubscribes from audit notification events.

 |
| 

addFilter(event: NotifyEvent, filter: Filter): void

 | 

Adds a filter for an audit notification event.

 |
| 

removeFilter(event: NotifyEvent, filter: Filter): void

 | 

Deletes a filter of an audit notification event.

 |

#### Development Procedure

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/10/v3/9e2NHzaYTqCaTu-0b4BiAg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062007Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=E602F94F2DD827BF4A1720ACC45B27D2CF322D414112FF1C75455A1BC6F834B5)

-   When preparing for the development, you need to apply for the **ohos.permission.QUERY\_AUDIT\_EVENT** permission.
-   Only enterprise apps in the trustlist can apply for this permission. For details about how to apply for this permission, please refer to [Permissions for Enterprise Applications](../../../../application-access-control/application-permission-management/application-permissions/permissions-for-enterprise-applications/document.md).

1.  Import the Device Security Kit module and related public modules.
    
    import { securityAudit } from '@kit.DeviceSecurityKit'; 
    import { BusinessError} from '@kit.BasicServicesKit'; 
    import { hilog } from '@kit.PerformanceAnalysisKit';
    
2.  Create a client instance for audit notification event management.
    
    let client: securityAudit.Client | undefined = undefined;
    const TAG = "SecurityAuditJsTest"; 
    const callback = (event: securityAudit.AuditEvent) => { 
      hilog.info(0x0000, TAG, '%{public}s', 'Security\_SecurityAudit\_JsApi\_Func eventId= ' + event.eventId); 
      hilog.info(0x0000, TAG, '%{public}s', 'Security\_SecurityAudit\_JsApi\_Func version= ' + event.version); 
      hilog.info(0x0000, TAG, '%{public}s', 'Security\_SecurityAudit\_JsApi\_Func content= ' + event.content); 
      hilog.info(0x0000, TAG, '%{public}s', 'Security\_SecurityAudit\_JsApi\_Func timestamp= ' + event.timestamp); 
      hilog.info(0x0000, TAG, '%{public}s', 'Security\_SecurityAudit\_JsApi\_Func userId= ' + event.userId); 
      hilog.info(0x0000, TAG, '%{public}s', 'Security\_SecurityAudit\_JsApi\_Func deviceId= ' + event.deviceId); 
    }; 
    try { 
      client = securityAudit.newClient(callback);
    } catch (err) {
      let e: BusinessError = err as BusinessError; 
      hilog.error(0x0000, TAG, 'newClient failed: %{public}d %{public}s', e.code, e.message); 
    }
    
3.  Subscribe to an audit notification event.
    
    try { 
      hilog.info(0x0000, TAG, 'subscribe begin.'); 
      client?.subscribe(\[0x02D000000\]);
      hilog.info(0x0000, TAG, 'Succeeded in subscribe.'); 
    } catch (err) { 
      let e: BusinessError = err as BusinessError; 
      hilog.error(0x0000, TAG, 'subscribe failed: %{public}d %{public}s', e.code, e.message); 
    }
    
4.  Add a filter for the audit notification event.
    
    let filter : securityAudit.Filter = {
      type: 0x00000200,
      isInclude: true,
      values : \["2"\]
    };
    try { 
      hilog.info(0x0000, TAG, 'addFilter begin.'); 
      client?.addFilter(0x02D000000, filter);
      hilog.info(0x0000, TAG, 'Succeeded in addFilter.'); 
    } catch (err) { 
      let e: BusinessError = err as BusinessError; 
      hilog.error(0x0000, TAG, 'addFilter failed: %{public}d %{public}s', e.code, e.message); 
    }
    
5.  Unsubscribe from the audit notification event.
    
    try { 
      hilog.info(0x0000, TAG, 'unsubscribe begin.'); 
      client?.unsubscribe(\[0x2E000000\]);
      hilog.info(0x0000, TAG, 'Succeeded in unsubscribe.'); 
    } catch (err) { 
      let e: BusinessError = err as BusinessError; 
      hilog.error(0x0000, TAG, 'unsubscribe failed: %{public}d %{public}s', e.code, e.message); 
    }
    
6.  Delete the filter of the audit notification event.
    
    try { 
      hilog.info(0x0000, TAG, 'removeFilter begin.'); 
      client?.removeFilter(0x02D000000, filter);
      hilog.info(0x0000, TAG, 'Succeeded in removeFilter.'); 
    } catch (err) { 
      let e: BusinessError = err as BusinessError; 
      hilog.error(0x0000, TAG, 'removeFilter failed: %{public}d %{public}s', e.code, e.message); 
    }
    
7.  Delete the client instance for audit notification event management.
    
    try { 
      securityAudit.deleteClient(client);
    } catch (err) { 
      let e: BusinessError = err as BusinessError; 
      hilog.error(0x0000, TAG, 'deleteClient failed: %{public}d %{public}s', e.code, e.message); 
    }
