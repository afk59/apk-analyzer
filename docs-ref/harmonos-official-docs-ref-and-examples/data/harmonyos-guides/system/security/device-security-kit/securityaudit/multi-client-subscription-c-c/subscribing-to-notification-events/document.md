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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/87/v3/oU9dYPA-RC-LkA4uJ-AfmQ/en-us_image_0000002482908436.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062007Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=D66D8FA8C74268CF6D3930EC7396642837562538B469102A483CFD187A31C5FF)

The process is as follows:

1.  Create a client instance for subscribing to audit notification events (hereinafter referred to as events) and provide a callback.
2.  Use the instance created in step 1 to subscribe to events by providing event IDs.
3.  Use the instance created in step 1 to set event filters by providing event IDs and filter information.
4.  When an event occurs, the audit service filters the event based on the specified filter. If the event meets the filter, the callback is triggered to notify the client that has subscribed to the event.
5.  Process services based on the audit data.
6.  If the audit data does not need to be filtered or used any more, use the instance created in step 1 to delete filters and unsubscribe from the events.
7.  If the instance does not need to used any more, delete it.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7a/v3/1sm8RakUQFmxDLPWbFXTBg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062007Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=081750186AD071DBDF4AC27EFBD70A06A8DB89C135B02231E854772A4CE47120)
    
    You can also set filters before subscribing to events.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6/v3/zB7DDe4LTUWbbEqvT2tAHA/caution_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062007Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=E98E999B3BEFC7C62F2E8FBC4B884EF3CB3B2DF95169F627C39095C51C5AD7BF)
    
    After an instance is deleted, all subscriptions and filters of the instance are removed.
    

#### API Description

The following table lists the APIs. For details about the APIs, please refer to [API Reference](https://developer.huawei.com/consumer/en/doc/harmonyos-references/devicesecurity-capi-securityaudit#en-us_topic_0000002349017400_ga18d7c9fe5c578d6113c86dd0c09353b4).

| 
API

 | 

Description

 |
| :-- | :-- |
| 

int32\_t HMS\_SecurityAudit\_NewClient(SecurityAudit\_Client\*\* client, SecurityAudit\_Handler handler)

 | 

Creates a notification event management object (client). The client provides the subscription, unsubscription, event filter adding, and event filter deletion functions.

 |
| 

int32\_t HMS\_SecurityAudit\_DeleteClient(SecurityAudit\_Client\* client)

 | 

Deletes an audit notification event management object.

 |
| 

int32\_t HMS\_SecurityAudit\_Subscribe(const SecurityAudit\_Client\* client, const SecurityAudit\_Notify\_Event \*events, uint64\_t count)

 | 

Subscribes to audit notification events.

 |
| 

int32\_t HMS\_SecurityAudit\_Unsubscribe(const SecurityAudit\_Client\* client, const SecurityAudit\_Notify\_Event \*events, uint64\_t count)

 | 

Unsubscribes from audit notification events.

 |
| 

int32\_t HMS\_SecurityAudit\_AddFilter(const SecurityAudit\_Client\* client, SecurityAudit\_Notify\_Event event, const SecurityAudit\_Filter \*filter)

 | 

Adds a filter for an audit notification event.

 |
| 

int32\_t HMS\_SecurityAudit\_RemoveFilter(const SecurityAudit\_Client\* client, SecurityAudit\_Notify\_Event event, const SecurityAudit\_Filter \*filter)

 | 

Deletes a filter of an audit notification event.

 |

#### Development Procedure

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/61/v3/jtQ30QeaSoOQLyVbyD-vdQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062007Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=44E9C24913D35D14ACDE0C5B7BF96F9F9518501960D107DA8E1432003CD2099A)

-   When preparing for the development, you need to apply for the **ohos.permission.QUERY\_AUDIT\_EVENT** permission.
-   Only enterprise apps in the trustlist can apply for this permission. For details about how to apply for this permission, please refer to [Permissions for Enterprise Applications](../../../../application-access-control/application-permission-management/application-permissions/permissions-for-enterprise-applications/document.md).

1.  Import and link the security audit shared library in **CMakeLists.txt**.
    
    find\_library(dsm-lib libsecurityaudit\_ndk.z.so)
    target\_link\_libraries(entry PUBLIC libace\_napi.z.so ${dsm-lib})
    
2.  Import the security audit header file.
    
    #include <DeviceSecurityKit/security\_audit.h>
    #include <cstdio>
    
3.  Define the callback function for notification events globally.
    
    void Notify(const SecurityAudit\_Event \*events, uint64\_t count)
    {
        if (events == nullptr) {
            printf("events nullptr");
            return;
        }
        for (uint64\_t i = 0; i < count; i++) {
            printf("event content = %s", events\[i\].content);
            printf("event id = %ld", events\[i\].eventId);
        }
    }
    
4.  Create a client instance for audit notification event management.
    
    SecurityAudit\_Client \*client = NULL;
    SecurityAudit\_Handler handler = Notify;
    HMS\_SecurityAudit\_NewClient(&client, handler);
    if (client == nullptr) {
        printf("client is null");
        return 0;
    }
    
5.  Subscribe to an audit notification event.
    
    SecurityAudit\_Notify\_Event event\[1\] = {};
    event\[0\] = SECURITY\_AUDIT\_NOTIFY\_EVENT\_KIA\_READ;
    int ret = HMS\_SecurityAudit\_Subscribe(client, event, 1);
    if (ret != 0) {
        printf("subscribe fail");
        return;
    }
    
6.  Add a filter for the audit notification event.
    
    SecurityAudit\_Filter filter = {};
    filter.type = PROCESS\_NAME\_PREFIX;
    const char\* filterStr\[1\] = {};
    filterStr\[0\] = "1";
    filter.value = filterStr;
    filter.valueCount = 1;
    ret = HMS\_SecurityAudit\_AddFilter(client, SECURITY\_AUDIT\_NOTIFY\_EVENT\_KIA\_READ, &filter);
    if (ret != 0) {
        printf("addfilter fail");
        return;
    }
    
7.  Unsubscribe from the audit notification event.
    
    ret = HMS\_SecurityAudit\_Unsubscribe(client, event, 1);
    if (ret != 0) {
        printf("unsubscribe fail");
        return;
    }
    
8.  Delete the filter of the audit notification event.
    
    ret = HMS\_SecurityAudit\_RemoveFilter(client, SECURITY\_AUDIT\_NOTIFY\_EVENT\_KIA\_READ, &filter);
    if (ret != 0) {
        printf("removefilter fail");
        return;
    }
    
9.  Delete the client instance for audit notification event management.
    
    ret = HMS\_SecurityAudit\_DeleteClient(client);
    if (ret != 0) {
        printf("deleteclient fail");
        return;
    }
