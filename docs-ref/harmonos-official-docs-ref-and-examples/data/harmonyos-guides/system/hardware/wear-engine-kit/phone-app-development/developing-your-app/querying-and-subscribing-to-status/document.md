# Querying and Subscribing to Status

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/34/v3/V_FJhdj7RmWP2Nf888JHIg/caution_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062025Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=869D03ADC5E20DECAFC55E7FE246E1DD9DF3AFA2E1A482DE1429C19EEA50A8B3)

To call this API, you need to apply for the basic device information permission and the wearable user status permission on HUAWEI Developers (refer to [Applying for Integrating Wear Engine](../../getting-started/applying-for-integrating-wear-engine/document.md) for details). The wearable user status permission needs to be granted by users.

-   Query the available space and battery level of a wearable device in real time.
-   Subscribe to the connection status, low battery level alerts, and heart rate alerts of a wearable device.
-   Query and subscribe to the charging status, wearing status, and device mode of a wearable device.

Before calling this API, ensure that you have applied for the required permissions for your app (by referring to [Applying for Integrating Wear Engine](../../getting-started/applying-for-integrating-wear-engine/document.md)) and requested the authorization from the phone user (by referring to [Requesting User Authorization](../requesting-user-authorization/document.md)). Otherwise, the API calling will fail.

**Table 1** Permission application: basic device information
| 
Wearable Device Status

 | 

Query Result

 | 

Trigger Condition for Subscription

 | 

Subscription Result

 |
| :-- | :-- | :-- | :-- |
| 

Connection status

 | 

N/A

 | 

-   2: The phone and the wearable device are connected.
-   3: The phone is disconnected from the wearable device. (By disconnecting Bluetooth or enlarging the distance between two devices.)

 | 

-   2: The phone and the wearable device are connected.
-   3: The wearable device is disconnected from the phone.
-   4: Two devices are unable to connect.
-   5: The device is deleted.

 |
| 

Available space

 | 

Available space, in KB (for example: 20480)

 | 

N/A

 | 

N/A

 |
| 

Battery level

 | 

Battery level (for example, 97)

 | 

The wearable's battery level drops by 1% (for example, from 98% to 97%) while not being charged.

 | 

Battery level (for example, 97)

 |
| 

Charging status

 | 

-   1: The wearable device is being charged.
-   2: The wearable device is not being charged.
-   3: The device is being fully charged.

 | 

-   1: Charge the wearable device.
-   2: Stop charging the wearable device.
-   3: The wearable device is fully charged.

 | 

-   1: The charging starts.
-   2: The charging ends.
-   3: The charging completes.

 |
| 

Device mode

 | 

-   –1: The device does not support mode switching.
-   0: The device is in standard mode.
-   1: The device is in ultra-long battery life mode.

 | 

-   0: The device switches from ultra-long battery life mode to standard mode.
-   1: The device switches from standard mode to ultra-long battery life mode.

 | 

-   0: The device is in standard mode.
-   1: The device is in ultra-long battery life mode.

 |

**Table 2** Permission application: wearable user status **USER\_STATUS** (for enterprise developers only)
| 
Wearable User Status

 | 

Query Result

 | 

Trigger Condition for Subscription

 | 

Subscription Result

 |
| :-- | :-- | :-- | :-- |
| 

Wearing status

 | 

-   1: The wearable device is worn.
-   2: The wearable device is not worn.

 | 

-   1: The wearable device is worn on the wrist.
-   2: The wearable device is removed from the wrist.

 | 

-   1: The wearable device is worn.
-   2: The wearable device is not worn.

 |
| 

Heart rate alerts

 | 

N/A

 | 

-   1: The resting heart rate is above the upper limit for 10 consecutive minutes.
-   2: The resting heart rate is below the lower limit for 10 consecutive minutes.
-   3: The exercise heart rate is too high.
-   4: The exercise heart rate is too low.

Note: Open the **Huawei Health** app, go to **Devices**, and touch **Heart rate** from the app and service list to set the heart rate alert.

 | 

-   1: The resting heart rate is too high.
-   2: The resting heart rate is too low.
-   3: The exercise heart rate is too high.
-   4: The exercise heart rate is too low.

 |

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7a/v3/9w2AXB-8RIC14NU6WmZ_Jg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062025Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=8C9E894AB38E7AEA6FB6DDDB4CD638BDFF6A9564C4CDDAC18D49DD463046F6A2)

-   The wearable device status can be obtained by your phone app even if you don't have a counterpart app installed on the wearable device.
-   Ensure that the wearable device is connected to the Huawei Health app when you query or subscribe to the device status including its battery level, charging status, wearing status, and heart rate alerts. Users can query the connection status on the **Devices** screen in the Huawei Health app. You can determine whether the device is connected to the phone by calling [getConnectedDevices](https://developer.huawei.com/consumer/en/doc/harmonyos-references/wearengine_api#section1828213119411) or by checking the error code. If the device is not connected to the phone, prompt the user to reconnect the device.
-   You will need to apply for the [USER\_STATUS](https://developer.huawei.com/consumer/en/doc/harmonyos-references/wearengine_api#section09971113566) permission to query and subscribe to the wearing status and heart rate alerts.

#### Querying Device Status

Call the [queryStatus](https://developer.huawei.com/consumer/en/doc/harmonyos-references/wearengine_api#section3383841153218) method in the [MonitorClient](https://developer.huawei.com/consumer/en/doc/harmonyos-references/wearengine_api#section178254313113) object to query the wearable device status. A maximum of one status can be queried at one time.

1.  Obtain the list of connected wearable devices by referring to [Querying Connected Wearable Devices](../querying-connected-wearable-devices/document.md).
2.  Select the device to communicate with from the list of connected devices by referring to [Selecting a Target Device](../selecting-a-target-device/document.md).
3.  Call the [getMonitorClient](https://developer.huawei.com/consumer/en/doc/harmonyos-references/wearengine_api#section068883315262) method in [wearEngine](https://developer.huawei.com/consumer/en/doc/harmonyos-references/wearengine_api) to obtain the [MonitorClient](https://developer.huawei.com/consumer/en/doc/harmonyos-references/wearengine_api#section178254313113) object.
4.  Call the [queryStatus](https://developer.huawei.com/consumer/en/doc/harmonyos-references/wearengine_api#section3383841153218) method to query the specified status.
    
    -   Use the [MonitorItem](https://developer.huawei.com/consumer/en/doc/harmonyos-references/wearengine_api#section16422462613) object to query the specified status. Currently, the following status can be queried:
        -   Battery status: **POWER\_STATUS**
        -   Charging status: **CHARGE\_STATUS**
        -   Wearing status: **WEAR\_STATUS**
        -   Device mode: **POWER\_MODE**
        -   Available space: **AVAILABLE\_STORAGE\_SPACE**
    -   Use the [MonitorData](https://developer.huawei.com/consumer/en/doc/harmonyos-references/wearengine_api#section12024822410) object to return the specified device status result.
        
        // Step 3: Obtain the **MonitorClient** object.
        let monitorClient: wearEngine.MonitorClient = wearEngine.getMonitorClient(this.getUIContext().getHostContext());
        
        // Step 4: Query a specified status (the wearing status is used as an example).
        monitorClient.queryStatus(targetDevice.randomId, wearEngine.MonitorItem.WEAR\_STATUS).then((result: wearEngine.MonitorData) => {
          // Obtain the status and process the service logic.
          console.info(\`Succeeded in querying wear status, result is ${result.code}.\`);
        }).catch((error: BusinessError) => {
          // Process the exception captured when the calling fails.
          console.error(\`Failed to query wear status. Code is ${error.code}, message is ${error.message}.\`);
        })
        
    

#### Subscribing to Device Status

1.  Obtain the list of connected wearable devices by referring to [Querying Connected Wearable Devices](../querying-connected-wearable-devices/document.md).
2.  Select the device to communicate with from the list of connected devices by referring to [Selecting a Target Device](../selecting-a-target-device/document.md).
3.  Call the [getMonitorClient](https://developer.huawei.com/consumer/en/doc/harmonyos-references/wearengine_api#section068883315262) method in [wearEngine](https://developer.huawei.com/consumer/en/doc/harmonyos-references/wearengine_api) to obtain the [MonitorClient](https://developer.huawei.com/consumer/en/doc/harmonyos-references/wearengine_api#section178254313113) object.
4.  Define the [Callback](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-base#callback) object of the subscription task.
5.  Call the [subscribeEvent](https://developer.huawei.com/consumer/en/doc/harmonyos-references/wearengine_api#section74368231248) method to subscribe to changes to the specified status.
    
    -   Use the [MonitorEvent](https://developer.huawei.com/consumer/en/doc/harmonyos-references/wearengine_api#section0407141762619) object to subscribe to the status of the wearable device and health data. Currently, the following status can be subscribed to:
        -   Device connection status: EVENT\_CONNECTION\_STATUS\_CHANGED
        -   Battery level decrease status: EVENT\_BATTERY\_LEVEL\_DROPPED
        -   Charging status: EVENT\_CHARGE\_STATUS\_CHANGED
        -   Wearing status: EVENT\_WEAR\_STATUS\_CHANGED
        -   Heart rate alerts: EVENT\_HEART\_RATE\_ALARM
        -   Device mode: EVENT\_POWER\_MODE\_CHANGED
    -   Use the [Callback](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-base#callback)<[MonitorEventData](https://developer.huawei.com/consumer/en/doc/harmonyos-references/wearengine_api#section38571246164212)\> object to return the device status.
    
    // Step 3: Obtain the **MonitorClient** object.
    let monitorClient: wearEngine.MonitorClient = wearEngine.getMonitorClient(this.getUIContext().getHostContext());
    
    // Step 4: Define the callback function.
    let callback = (monitorEventData: wearEngine.MonitorEventData) => {
      // Process the service logic after the status change is detected.
      console.info(\`Succeeded in listening change of ${monitorEventData.event}, the new status is ${monitorEventData.data}.\`)
    }
    
    // Step 5: Call the subscription method.
    monitorClient.subscribeEvent(targetDevice.randomId, wearEngine.MonitorEvent.EVENT\_WEAR\_STATUS\_CHANGED, callback).then(() => {
      console.info(\`Succeeded in subscribing wear status.\`);
    }).catch((error: BusinessError) => {
      console.error(\`Failed to subscribe wear status. Code is ${error.code}, message is ${error.message}.\`);
    })
    

6.  Call the [unsubscribeEvent](https://developer.huawei.com/consumer/en/doc/harmonyos-references/wearengine_api#section182736075018) method to cancel the subscription to the status changes of the wearable device. (Pass the callback function used during the subscription.)
    
    // Step 6: Cancel the subscription. Ensure that the callback function is the same one used during the subscription.
    monitorClient.unsubscribeEvent(targetDevice.randomId, wearEngine.MonitorEvent.EVENT\_WEAR\_STATUS\_CHANGED, callback).then(() => {
      console.info(\`Succeeded in unsubscribing wear status\`);
    }).catch((error: BusinessError) => {
      console.error(\`Failed to unsubscribe wear status. Code is ${error.code}, message is ${error.message}.\`);
    })
