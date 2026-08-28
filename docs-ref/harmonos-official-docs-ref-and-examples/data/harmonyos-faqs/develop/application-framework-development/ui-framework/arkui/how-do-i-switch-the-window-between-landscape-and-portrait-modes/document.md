# How do I switch the window between landscape and portrait modes?

Call **setPreferredOrientation(orientation: Orientation, callback: AsyncCallback<void>): void**, setting **orientation** to **AUTO\_ROTATION**, which indicates the auto-rotation mode. The sample code is as follows:

let orientation = window.Orientation.AUTO\_ROTATION;
try{
  windowClass.setPreferredOrientation(orientation, (err) => {
    if(err.code){
      console.error('Failed to set window orientation. Cause: ' + JSON.stringify(err));
      return;
    }
    console.info('Succeeded in setting window orientation.');
  });
}catch (exception) {
  console.error('Failed to set window orientation. Cause: ' + JSON.stringify(exception));
}

**Reference**

[setPreferredOrientation](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-window-window#setpreferredorientation9)
