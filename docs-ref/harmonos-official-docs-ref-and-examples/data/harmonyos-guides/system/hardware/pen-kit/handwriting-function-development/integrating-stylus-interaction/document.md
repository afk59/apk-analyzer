# Integrating Stylus Interaction

After the stylus interaction function is integrated, a third-party app can call the following APIs to listen for the stylus double-tap or squeeze events and trigger the internal callback of the app to perform specified operations.

#### API Description

| 
Class

 | 

API

 | 

Description

 |
| :-- | :-- | :-- |
| 

stylusInteraction

 | 

[on](https://developer.huawei.com/consumer/en/doc/harmonyos-references/pen-stylusinteraction#section98913119599)(type: 'squeeze', receiver: Callback<[SqueezeEvent](https://developer.huawei.com/consumer/en/doc/harmonyos-references/pen-stylusinteraction#section10272152161111)\>): void

 | 

Listens for stylus squeeze events.

 |
| 

stylusInteraction

 | 

[off](https://developer.huawei.com/consumer/en/doc/harmonyos-references/pen-stylusinteraction#section137391712323)(type: 'squeeze', receiver?: Callback<[SqueezeEvent](https://developer.huawei.com/consumer/en/doc/harmonyos-references/pen-stylusinteraction#section10272152161111)\>): void

 | 

Cancels listening for stylus squeeze events.

 |
| 

stylusInteraction

 | 

[on](https://developer.huawei.com/consumer/en/doc/harmonyos-references/pen-stylusinteraction#section450110191857)(type: 'doubleTap', receiver: Callback<[DoubleTapEvent](https://developer.huawei.com/consumer/en/doc/harmonyos-references/pen-stylusinteraction#section4950173171415)\>): void

 | 

Listens for stylus double-tap events.

 |
| 

stylusInteraction

 | 

[off](https://developer.huawei.com/consumer/en/doc/harmonyos-references/pen-stylusinteraction#section9865271579)(type: 'doubleTap', receiver?: Callback<[DoubleTapEvent](https://developer.huawei.com/consumer/en/doc/harmonyos-references/pen-stylusinteraction#section4950173171415)\>): void

 | 

Cancels listening for stylus double-tap events.

 |

#### Stylus Squeeze Events

1\. Import required modules.

import { stylusInteraction } from '@kit.Penkit';
import { BusinessError } from '@kit.BasicServicesKit';

2\. Listen for stylus squeeze events.

try {
  stylusInteraction.on('squeeze', (event: stylusInteraction.SqueezeEvent) => {
    console.info(\`got squeeze event, time: ${event.timestamp}\`);
  });
} catch (err) {
  console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
}

3\. Cancel listening for stylus squeeze events.

try {
  stylusInteraction.off('squeeze', (event: stylusInteraction.SqueezeEvent) => {
    console.info(\`off squeeze event, time: ${event.timestamp}\`);
  });
} catch (err) {
  console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
}

#### Stylus Double-tap Events

1\. Import required modules.

import { stylusInteraction } from '@kit.Penkit';
import { BusinessError } from '@kit.BasicServicesKit';

2\. Listen for stylus double-tap events.

try {
  stylusInteraction.on('doubleTap', (event: stylusInteraction.DoubleTapEvent) => {
    console.info(\`got doubleTap event, time: ${event.timestamp}\`);
  });
} catch (err) {
  console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
}

3\. Cancel listening for stylus double-tap events.

try {
  stylusInteraction.off('doubleTap', (event: stylusInteraction.DoubleTapEvent) => {
    console.info(\`off doubleTap event, time: ${event.timestamp}\`);
  });
} catch (err) {
  console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
}
