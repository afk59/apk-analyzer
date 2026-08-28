# How do I listen for window size changes?

**Symptom**

What methods can be used to listen for window size changes?

**Solution**

Obtain a **Window** instance, and call [on('windowSizeChange')](<https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-window-window#onwindowsizechange7 >) to listen for window size changes.

Note that this event is not triggered if the window size does not change. For example, if the window is rotated by 180 degrees without any size change, the callback is not invoked. In this case, listen for the **display.on('change')** event and obtain the window size through the **display** interface within the callback.

try {
  windowClass.on('windowSizeChange', (data) => {
    console.info('Succeeded in enabling the listener for window size changes. Data: ' + JSON.stringify(data));
  });
} catch (exception) {
  console.error('Failed to enable the listener for window size changes. Cause: ' + JSON.stringify(exception));
}

**Reference**

[display.on('add'|'remove'|'change')](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-display#displayonaddremovechange)
