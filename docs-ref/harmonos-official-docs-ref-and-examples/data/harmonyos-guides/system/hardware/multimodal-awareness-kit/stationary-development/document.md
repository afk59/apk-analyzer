# Stationary Development

#### When to Use

An application can call the **Stationary** module to obtain the device status, for example, whether the device is absolutely or relatively still.

For details about the APIs, see [Stationary](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-stationary).

#### Device Status Type Parameters

| Name | Description |
| :-- | :-- |
| still | Absolutely still. |
| relativeStill | Relatively still. |

#### Parameters for Subscribing to Device Status events

| Name | Value | Description |
| :-- | :-- | :-- |
| ENTER | 1 | Event indicating entering device status. |
| EXIT | 2 | Event indicating exiting device status. |
| ENTER\_EXIT | 3 | Event indicating entering and exiting device status. |

#### Returned Device Status Parameters

| Name | Value | Description |
| :-- | :-- | :-- |
| ENTER | 1 | Entering device status. |
| EXIT | 2 | Exiting device status. |

#### Available APIs

| Name | Description |
| :-- | :-- |
| on(activity: ActivityType, event: ActivityEvent, reportLatencyNs: number, callback: Callback<ActivityResponse>): void | Subscribes to the device status. This API uses an asynchronous callback to return the result. |
| once(activity: ActivityType, callback: Callback<ActivityResponse>): void | Obtains the device status. This API uses an asynchronous callback to return the result. |
| off(activity: ActivityType, event: ActivityEvent, callback?: Callback<ActivityResponse>): void | Unsubscribes from the device status. |

#### Constraints

The device is required to support the acceleration sensor.

Currently, only the algorithm framework is provided. The API test framework returns the following result: data={"type":3,"value":-1}.

If the relative stationary and absolute stationary capabilities are required, you must implement them in **device\_status/libs/src/algorithm**. The following code snippet is for reference:

algoPara\_.resultantAcc =
   sqrt((algoPara\_.x \* algoPara\_.x) + (algoPara\_.y \* algoPara\_.y) + (algoPara\_.z \* algoPara\_.z));
if ((algoPara\_.resultantAcc > RESULTANT\_ACC\_LOW\_THRHD) && (algoPara\_.resultantAcc < RESULTANT\_ACC\_UP\_THRHD)) {
   if (state\_ == STILL) {
      return;
   }
   counter\_--;
   if (counter\_ == 0) {
      counter\_ = COUNTER\_THRESHOLD;
      UpdateStateAndReport(VALUE\_ENTER, STILL, TYPE\_ABSOLUTE\_STILL);
   }
} else {
   counter\_ = COUNTER\_THRESHOLD;
   if (state\_ == UNSTILL) {
      return;
   }
   UpdateStateAndReport(VALUE\_EXIT, UNSTILL, TYPE\_ABSOLUTE\_STILL);
}

#### How to Develop

1.  Subscribe to the event indicating entering the absolute still state, and the event is reported every 1 second.
    
    import { stationary } from '@kit.MultimodalAwarenessKit';
    import { BusinessError } from '@kit.BasicServicesKit';
    
    let reportLatencyNs = 1000000000;
    try {
       stationary.on('still', stationary.ActivityEvent.ENTER, reportLatencyNs, (data) => {
          console.info('data=' + JSON.stringify(data));
       })
    } catch (error) {
       let message = (error as BusinessError).message;
       console.error('stationary on failed:' + message);
    }
    
2.  Obtain the event indicating entering the absolute still state.
    
    import { stationary } from '@kit.MultimodalAwarenessKit';
    import { BusinessError } from '@kit.BasicServicesKit';
    
    try {
       stationary.once('still', (data) => {
          console.info('data=' + JSON.stringify(data));
       })
    } catch (error) {
       let message = (error as BusinessError).message;
       console.error('stationary once failed:' + message);
    }
    
3.  Unsubscribe from the event indicating entering the absolute still state.
    
    import { stationary } from '@kit.MultimodalAwarenessKit';
    import { BusinessError } from '@kit.BasicServicesKit';
    
    try {
       stationary.off('still', stationary.ActivityEvent.ENTER, (data) => {
          console.info('data=' + JSON.stringify(data));
       })
    } catch (error) {
       let message = (error as BusinessError).message;
       console.error('stationary off failed:' + message);
    }
