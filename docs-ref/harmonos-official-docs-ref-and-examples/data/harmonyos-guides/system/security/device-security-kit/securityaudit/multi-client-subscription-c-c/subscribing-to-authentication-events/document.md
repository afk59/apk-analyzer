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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9c/v3/FyUNeniRSaGlx5I7XgcF9g/en-us_image_0000002515108431.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062007Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=C800057E767A450F794DB962F033F4995042D5AAD2FA19E946988366AF0E5FF8 "Click to enlarge")

The process is as follows:

1.  Create a client instance for subscribing to audit authentication events (hereinafter referred to as events) and provide a callback.
2.  Use the instance created in step 1 to subscribe to events by providing event IDs.
3.  Use the instance created in step 1 to set event filters by providing event IDs and filter information.
4.  When an event occurs, the audit service filters the event based on the specified filter. If the event meets the filter, the callback is triggered to notify the client that has subscribed to the event.
5.  Formulate an authentication policy based on audit data.
6.  Use the instance created in step 1 to set the authentication policy for the received event.
7.  When the service ends, use the instance created in step 1 to delete filters and unsubscribe from the events.
8.  Delete the instance created in step 1.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f4/v3/GYmG6xSgQmStIpqsQylCZg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062007Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=0C86C015F20B160BA509566B88CE5E420C2DD67D088810A9B68BF519D5B7EB0F)
    
    You can also set filters before subscribing to events.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/34/v3/JvNX04gKSZqkyDv8La-paQ/caution_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062007Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=D54D9C581EBD3EC907B15F8152E1906C07E5282D70779524AC7C77C4BD390049)
    
    After an instance is deleted, all subscriptions and filters of the instance are removed.
    

#### API Description

For details about the APIs, please refer to [API Reference](https://developer.huawei.com/consumer/en/doc/harmonyos-references/devicesecurity-capi-securityaudit#en-us_topic_0000002349017400_gab59201b529a964c3cc7f9ed12ab0330e).

| 
API

 | 

Description

 |
| :-- | :-- |
| 

int32\_t HMS\_SecurityAudit\_NewAuthClient(SecurityAudit\_AuthClient\*\* client, SecurityAudit\_Handler handler);

 | 

Creates an audit authentication event management object (AuthClient). The AuthClient provides the subscription, unsubscription, event filter adding, event filter deletion, and authentication functions.

 |
| 

int32\_t HMS\_SecurityAudit\_DeleteAuthClient(SecurityAudit\_AuthClient\* client);

 | 

Deletes an audit authentication event management object.

 |
| 

int32\_t HMS\_SecurityAudit\_SubscribeAuthEvent(const SecurityAudit\_AuthClient\* client, const SecurityAudit\_Auth\_Event \*events, uint64\_t count);

 | 

Subscribes to audit authentication events.

 |
| 

int32\_t HMS\_SecurityAudit\_UnsubscribeAuthEvent(const SecurityAudit\_AuthClient\* client, const SecurityAudit\_Auth\_Event \*events, uint64\_t count);

 | 

Unsubscribes from audit authentication events.

 |
| 

int32\_t HMS\_SecurityAudit\_AddAuthEventFilter(const SecurityAudit\_AuthClient\* client, SecurityAudit\_Auth\_Event event, const SecurityAudit\_Filter \*filter);

 | 

Adds a filter for an audit authentication event.

 |
| 

int32\_t HMS\_SecurityAudit\_RemoveAuthEventFilter(const SecurityAudit\_AuthClient\* client, SecurityAudit\_Auth\_Event event, const SecurityAudit\_Filter \*filter);

 | 

Deletes a filter of an audit authentication event.

 |
| 

int32\_t HMS\_SecurityAudit\_Auth(const SecurityAudit\_AuthClient\* client, const SecurityAudit\_Event \*event, SecurityAudit\_AuthResult authResult);

 | 

Sets the authentication result for an audit authentication event.

 |

#### Development Procedure

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3d/v3/sqBg2JKRQye-ft9xLYPkaw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062007Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=71ADB07655A5D19E64BDF21F809CFE6E9834D55642F5AD546A873F1B45A15F64)

-   When preparing for the development, you need to apply for the **ohos.permission.kernel.AUTH\_AUDIT\_EVENT** permission.
-   Only enterprise apps in the trustlist can apply for this permission. For details about how to apply for this permission, please refer to [Permissions for Enterprise Applications](../../../../application-access-control/application-permission-management/application-permissions/permissions-for-enterprise-applications/document.md).

1.  Import and link the security audit shared library in **CMakeLists.txt**.
    
    find\_library(dsm-lib libsecurityaudit\_ndk.z.so)
    target\_link\_libraries(entry PUBLIC libace\_napi.z.so ${dsm-lib})
    
2.  Import the security audit header file.
    
    #include <DeviceSecurityKit/security\_audit.h>
    #include <cstdio>
    
3.  Globally define an authentication event management client and a callback function containing the authentication policy.
    
    SecurityAudit\_AuthClient \*client = nullptr;
    void AuthAllowCb(const SecurityAudit\_Event \*events, uint64\_t count)
    {
        if (events == nullptr) {
            printf("events nullptr");
            return;
        }
        if (client == nullptr) {
            printf("client nullptr");
            return;
        }
        for (uint64\_t i = 0; i < count; i++) {
            printf("event metadata = %s \\n", events\[i\].metadata);
            printf("event content = %s \\n", events\[i\].content);
            printf("event id = %ld \\n", events\[i\].eventId);
            const SecurityAudit\_Event \*singleEvent = &events\[i\];
            HMS\_SecurityAudit\_Auth(client, singleEvent, SECURITY\_AUDIT\_AUTH\_RESULT\_DENY);
        }
    }
    
4.  Create a client instance for audit authentication event management.
    
    SecurityAudit\_Handler handler = AuthAllowCb;
    HMS\_SecurityAudit\_NewAuthClient(&client, handler);
    if (client == nullptr) {
        printf("client is null");
        return;
    }
    
5.  Subscribe to an audit authentication event.
    
    SecurityAudit\_Auth\_Event event\[1\] = {};
    event\[0\] = SECURITY\_AUDIT\_AUTH\_EVENT\_FILE\_CREATE;
    int ret = HMS\_SecurityAudit\_SubscribeAuthEvent(client, event, 1);
    if (ret != 0) {
        printf("subscribe fail");
        return;
    }
    
6.  Add a filter for the audit authentication event.
    
    SecurityAudit\_Filter filter = {};
    filter.type = PROCESS\_NAME\_PREFIX;
    const char\* filterStr\[1\] = {};
    filterStr\[0\] = "1";
    filter.value = filterStr;
    filter.valueCount = 1;
    ret = HMS\_SecurityAudit\_AddAuthEventFilter(client, SECURITY\_AUDIT\_AUTH\_EVENT\_FILE\_CREATE, &filter);
    if (ret != 0) {
        printf("addfilter fail");
        return;
    }
    
7.  Unsubscribe from the audit authentication event.
    
    ret = HMS\_SecurityAudit\_UnsubscribeAuthEvent(client, event, 1);
    if (ret != 0) {
        printf("unsubscribe fail");
        return;
    }
    
8.  Delete the filter of the audit authentication event.
    
    ret = HMS\_SecurityAudit\_RemoveAuthEventFilter(client, SECURITY\_AUDIT\_AUTH\_EVENT\_FILE\_CREATE, &filter);
    if (ret != 0) {
        printf("removefilter fail");
        return;
    }
    
9.  Delete the client instance for audit authentication event management.
    
    ret = HMS\_SecurityAudit\_DeleteAuthClient(client);
    if (ret != 0) {
        printf("deleteclient fail");
        return;
    }
