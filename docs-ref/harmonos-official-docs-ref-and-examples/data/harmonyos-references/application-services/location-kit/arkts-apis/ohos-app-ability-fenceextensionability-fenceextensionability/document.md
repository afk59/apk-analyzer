# @ohos.app.ability.FenceExtensionAbility (FenceExtensionAbility)

The **FenceExtensionAbility** class provides geofence-related capabilities. It is inherited from the **ExtensionAbility** class.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/49/v3/i94ygA9kR-2izPj_3xZmNA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062510Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=C9A332F6D738DA09F366106D56AA907415D7CFAA9CDDE0939C8ECEA2AC2292D7)

The initial APIs of this module are supported since API version 14. Newly added APIs will be marked with a superscript to indicate their earliest API version.

The APIs of this module can be used only in the stage model.

#### Modules to Import

import { FenceExtensionAbility } from '@kit.LocationKit';

#### FenceExtensionAbility

Provides geofence-related capabilities. It is inherited from the **ExtensionAbility** class.

#### \[h2\]Attributes

**System capability**: SystemCapability.Location.Location.Geofence

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| context | [FenceExtensionContext](../ohos-app-ability-fenceextensioncontext-fenceextensioncontext/document.md) | No | No | Context of the Geofence service. |

#### \[h2\]onFenceStatusChange

onFenceStatusChange(transition: geoLocationManager.GeofenceTransition, additions: Record<string, string>): void;

Represents the callback triggered when a geofence status change event is received. Service processing is then performed based on the event type and data.

**System capability**: SystemCapability.Location.Location.Geofence

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| transition | [geoLocationManager.GeofenceTransition](../ohos-geolocationmanager-geolocation-manager/document.md#geofencetransition12) | Yes | Geofence transition information, including the geofence ID and geofence event. |
| additions | Record<string, string> | Yes | Additional information. |

**Example**

import { FenceExtensionAbility, geoLocationManager } from '@kit.LocationKit';
import { notificationManager } from '@kit.NotificationKit';
import { Want, wantAgent } from '@kit.AbilityKit';

export class MyFenceExtensionAbility extends FenceExtensionAbility {
  onFenceStatusChange(transition: geoLocationManager.GeofenceTransition, additions: Record<string, string>): void {
    // Receive the geofence status change event and process the service logic.
    console.info(\`on geofence transition,id:${transition.geofenceId},event:${transition.transitionEvent},additions:${JSON.stringify(additions)}\`);

    // Send a geofence notification.
    let wantAgentInfo: wantAgent.WantAgentInfo = {
      wants: \[
        {
          bundleName: 'com.example.myapplication',
          abilityName: 'EntryAbility',
          parameters:
          {
            "geofenceId": transition?.geofenceId,
            "transitionEvent": transition?.transitionEvent,
          }
        } as Want
      \],
      actionType: wantAgent.OperationType.START\_ABILITY,
      requestCode: 100
    };
    wantAgent.getWantAgent(wantAgentInfo).then((wantAgentMy) => {
      let notificationRequest: notificationManager.NotificationRequest = {
        id: 1,
        content: {
          notificationContentType: notificationManager.ContentType.NOTIFICATION\_CONTENT\_BASIC\_TEXT,
          normal: {
            title: "Geofence Notification",
            text: \`on geofence transition,id:${transition.geofenceId},event:${transition.transitionEvent},additions:${JSON.stringify(additions)}\`,
          }
        },
        notificationSlotType: notificationManager.SlotType.SOCIAL\_COMMUNICATION,
        wantAgent: wantAgentMy
      };
      notificationManager.publish(notificationRequest);
    });
  }
}

#### \[h2\]onDestroy

onDestroy(): void;

Represents the callback triggered when a **FenceExtensionAbility** destruction event is received.

**System capability**: SystemCapability.Location.Location.Geofence

**Example**

import { FenceExtensionAbility } from '@kit.LocationKit';

class MyFenceExtensionAbility extends FenceExtensionAbility {
  onDestroy(): void {
    // Process the FenceExtensionAbility destruction event.
    console.info(\`on ability destroy\`);
  }
}
