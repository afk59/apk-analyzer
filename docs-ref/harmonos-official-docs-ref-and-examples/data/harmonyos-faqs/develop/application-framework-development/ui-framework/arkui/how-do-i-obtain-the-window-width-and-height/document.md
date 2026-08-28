# How do I obtain the window width and height?

Obtain a **Window** object, and use [getWindowProperties()](<https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-window-window#getwindowproperties9 >) of the object to obtain the window properties. The **windowRect** field in the properties specifies the window width and height. To obtain the window width and height information on a page, timing is crucial. The [aboutToAppear](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ts-custom-component-lifecycle#abouttoappear) phase in the page lifecycle does not indicate that the window is visible. It only indicates that the component has been created. As such, the window size information (specified by **windowRect**) obtained in this phase may be incorrect. To obtain the correct window width and height, you are advised to obtain the information in the [onPageShow](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ts-custom-component-lifecycle#onpageshow) phase, which is triggered once the window is visible. Refer to the code snippet below.

//If you need to get the window width and height information in the page, it is recommended to put the following code in the onPageShow stage of the page life cycle, rather than calling it in the aboutToAppear stage of the page life cycle
let windowClass: window.Window | undefined = undefined;
try {
  let promise = window.getLastWindow(this.context);
  promise.then((data) => {
    //Get window object
    windowClass = data;
    try {
      //Get window properties
      let properties = windowClass.getWindowProperties();
      let rect = properties.windowRect;
      //rect.width: Window Width, rect.height: Window height
    } catch (exception) {
      console.error('Failed to obtain the window properties. Cause: ' + JSON.stringify(exception));
    }
    console.info('Succeeded in obtaining the top window. Data: ' + JSON.stringify(data));
  }).catch((err: BusinessError) => {
    console.error('Failed to obtain the top window. Cause: ' + JSON.stringify(err));
  });
} catch (exception) {
  console.error('Failed to obtain the top window. Cause: ' + JSON.stringify(exception));
}
