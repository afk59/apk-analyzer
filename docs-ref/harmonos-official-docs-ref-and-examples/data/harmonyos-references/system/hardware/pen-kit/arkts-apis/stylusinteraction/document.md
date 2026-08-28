# stylusInteraction

Entry class of the stylus interaction function, which currently includes the stylus squeeze and double-tap events.

**System capability**: SystemCapability.Stylus.StylusService

**Start version**: 5.1.1(19)

#### Module Import

import { stylusInteraction } from '@kit.Penkit';

#### stylusInteraction.on('squeeze')

on(type: 'squeeze', receiver: Callback<SqueezeEvent>): void

Listens for stylus squeeze events.

**System capability**: SystemCapability.Stylus.StylusService

**Start version**: 5.1.1(19)

**Parameters:**

| 
Parameter

 | 

Type

 | 

Mandatory

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

type

 | 

string

 | 

Yes

 | 

Stylus squeeze event, which has a fixed value of **squeeze**.

 |
| 

receiver

 | 

Callback<[SqueezeEvent](#section10272152161111)\>

 | 

Yes

 | 

Callback function, which is used to return details about the stylus squeeze event.

 |

**Example**:

import { BusinessError } from '@kit.BasicServicesKit';

try {
  stylusInteraction.on('squeeze', (event: stylusInteraction.SqueezeEvent) => {
    console.info(\`got squeeze event, time: ${event.timestamp}\`);
  });
} catch (err) {
  console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
}

#### stylusInteraction.off('squeeze')

off(type: 'squeeze', receiver?: Callback<SqueezeEvent>): void

Cancels listening for stylus squeeze events.

**System capability**: SystemCapability.Stylus.StylusService

**Start version**: 5.1.1(19)

**Parameters:**

| 
Parameter

 | 

Type

 | 

Mandatory

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

type

 | 

string

 | 

Yes

 | 

Stylus squeeze event, which has a fixed value of **squeeze**.

 |
| 

receiver

 | 

Callback<[SqueezeEvent](#section10272152161111)\>

 | 

No

 | 

Callback function to be unregistered, which must be the same as that passed upon subscription. If this parameter is not set, all squeeze events will be unregistered.

 |

**Example**:

import { BusinessError } from '@kit.BasicServicesKit';
try {
  stylusInteraction.off('squeeze', (event: stylusInteraction.SqueezeEvent) => {
    console.info(\`off squeeze event, time: ${event.timestamp}\`);
  });
} catch (err) {
  console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
}

#### stylusInteraction.on('doubleTap')

on(type: 'doubleTap', receiver: Callback<DoubleTapEvent>): void

Listens for stylus double-tap events.

**System capability**: SystemCapability.Stylus.StylusService

**Start version**: 5.1.1(19)

**Parameters:**

| 
Parameter

 | 

Type

 | 

Mandatory

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

type

 | 

string

 | 

Yes

 | 

Stylus double-tap event, which has a fixed value of **doubleTap**.

 |
| 

receiver

 | 

Callback<[DoubleTapEvent](#section4950173171415)\>

 | 

Yes

 | 

Callback function, which is used to return details about the stylus double-tap event.

 |

**Example**:

import { BusinessError } from '@kit.BasicServicesKit';
try {
  stylusInteraction.on('doubleTap', (event: stylusInteraction.DoubleTapEvent) => {
    console.info(\`got doubleTap event, time: ${event.timestamp}\`);
  });
} catch (err) {
  console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
}

#### stylusInteraction.off('doubleTap')

off(type: 'doubleTap', receiver?: Callback<DoubleTapEvent>): void

Cancels listening for stylus double-tap events.

**System capability**: SystemCapability.Stylus.StylusService

**Start version**: 5.1.1(19)

**Parameters:**

| 
Parameter

 | 

Type

 | 

Mandatory

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

type

 | 

string

 | 

Yes

 | 

Stylus double-tap event, which has a fixed value of **doubleTap**.

 |
| 

receiver

 | 

Callback<[DoubleTapEvent](#section4950173171415)\>

 | 

No

 | 

Callback function to be unregistered, which must be the same as that passed upon subscription. If this parameter is not set, all double-tap events will be unregistered.

 |

**Example**:

import { BusinessError } from '@kit.BasicServicesKit';
try {
  stylusInteraction.off('doubleTap', (event: stylusInteraction.DoubleTapEvent) => {
    console.info(\`off doubleTap event, time: ${event.timestamp}\`);
  });
} catch (err) {
  console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
}

#### SqueezeEvent

Information of stylus squeeze events.

**System capability**: SystemCapability.Stylus.StylusService

**Start version**: 5.1.1(19)

**Parameters:**

| 
Name

 | 

**Type**

 | 

Read-Only

 | 

Optional

 | 

**Description**

 |
| :-- | :-- | :-- | :-- | :-- |
| 

timestamp

 | 

number

 | 

No

 | 

No

 | 

Timestamp, which is the time elapsed since the system startup, in ms.

 |

#### DoubleTapEvent

Information of stylus double-tap events.

**System capability**: SystemCapability.Stylus.StylusService

**Start version**: 5.1.1(19)

**Parameters:**

| 
Name

 | 

**Type**

 | 

Read-Only

 | 

Optional

 | 

**Description**

 |
| :-- | :-- | :-- | :-- | :-- |
| 

timestamp

 | 

number

 | 

No

 | 

No

 | 

Timestamp, which is the time elapsed since the system startup, in ms.

 |
