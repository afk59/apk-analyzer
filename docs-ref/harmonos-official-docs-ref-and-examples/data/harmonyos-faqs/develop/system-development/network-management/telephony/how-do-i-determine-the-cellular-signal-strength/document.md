# How do I determine the cellular signal strength?

You can use **radio.getSignalInformation()** to obtain the cellular signal strength. The procedure is as follows:

1.  Import the required modules.
2.  Call **getSignalInformation()** to obtain the **SignalInformation** list.
3.  Traverse the **SignalInformation** array, and check the signal strength of the corresponding radio access technology (RAT) based on **signalType**.
4.  (Optional) Subscribe to cellular network signal changes.

The code snippet is as follows:

import { radio, observer } from '@kit.TelephonyKit';

// Taking obtaining the signal strength of card 1 as an example
let slotId: number = 0;
radio.getSignalInformation(slotId, (err, data) => {
  if (!err) {
    console.log("get signal information success.");
    // Traverse the array and output the signal strength under different network standards
    for (let j = 0; j < data.length; j++) {
      console.log("type:" + data\[j\].signalType + ", level:" + data\[j\].signalLevel);
    }
  } else {
    console.error("get signal information fail, err is:" + JSON.stringify(err));
  }
});

// Subscription to cellular network signal changes (optional)
observer.on("signalInfoChange", (data) => {
  console.log("signal info change, data is:" + JSON.stringify(data));
});

**Reference**

[getSignalInformation](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-radio#radiogetsignalinformation7)
