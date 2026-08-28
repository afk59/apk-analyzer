# How do I keep the screen always on?

Obtain a **Window** instance, and then call **setWindowKeepScreenOn** to keep the screen always on.

let isKeepScreenOn: boolean = true;
let windowClass: window.Window = window.findWindow("test");
try {
  windowClass.setWindowKeepScreenOn(isKeepScreenOn, (err: BusinessError) => {
    const errCode: number = err.code;
    if (errCode) {
      console.error('Failed to set the screen to be always on. Cause: ' + JSON.stringify(err));
      return;

    }
    console.info('Succeeded in setting the screen to be always on.');
  });
} catch (exception) {
  console.error('Failed to set the screen to be always on. Cause: ' + JSON.stringify(exception));
}

**Reference**

[setWindowKeepScreenOn](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-window-window#setwindowkeepscreenon9)
