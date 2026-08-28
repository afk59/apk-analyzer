# Lifecycle

#### Application Lifecycle

You can define the following application lifecycle methods in the **app.js** file.

| API | Type | Description | Called When |
| :-- | :-- | :-- | :-- |
| onCreate | () => void | Listens for application creation. | The application is created. |
| onShow6+ | () => void | Listens for whether the application is running in the foreground. | The application is running in the foreground. |
| onHide6+ | () => void | Listens for whether the application is running in the background. | The application is running in the background. |
| onDestroy | () => void | Listens for application uninstallation. | The application exits. |

#### Page Lifecycle

You can define the following page lifecycle functions in the **.js** file of the page.

| API | Type | Description | Called When |
| :-- | :-- | :-- | :-- |
| onInit | () => void | Listens for page initialization. | Page initialization is complete. This function is called only once in the page lifecycle. |
| onReady | () => void | Listens for page creation. | A page is created. This function is called only once in the page lifecycle. |
| onShow | () => void | Listens for page display. | The page is displayed. |
| onHide | () => void | Listens for page hiding. | The page is hidden. |
| onDestroy | () => void | Listens for page destruction. | The page is destroyed. |
| onBackPress | () => boolean | Listens for the back button action. | 
The back button is touched.

\- **true**: The page handles the return logic itself.

\- **false**: The default return logic is used.

\- No value: The default return logic is used.

 |
| onActive()5+ | () => void | Listens for page activation. | The page is activated. |
| onInactive()5+ | () => void | Listens for page suspension. | The page is suspended. |
| onNewRequest()5+ | () => void | Listens for a new FA request. | The FA has been started and a new request is received. |

The typical call sequence of lifecycle functions is illustrated below.

**Figure 1** Lifecycle function call sequence diagram

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ad/v3/OsNGFqVQRLSG7VtNy0ciag/en-us_image_0000002568684617.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061942Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=18630F2F942B30C2D0F4725DA19581997CBD0B4DF0654B8C0DA7CF10D5B82C00)

#### Example

The following example demonstrates the call sequence of lifecycle functions through two pages: pageA and pageB. First, configure page routing in **config.json**:

{
    // ...
    "pages": \[
        "pages/pageA/pageA",
        "pages/pageB/pageB"
    \],
    // ...
}

**pageA** implementation:

<!-- pageA.hml -->
<div class="container">
  <text class="title">This is PageA</text>
  <input type="button" value="Go to the PageB" onclick="launch"></input>
</div>

/\* pageA.css \*/
.container {
  flex-direction: column;
  align-items: center;
  width: 100%;
  height: 100%;
}
.title {
  font-size: 38px;
  text-align: center;
  width: 100%;
  height: 40%;
}

// pageA.js
import router from '@ohos.router';
export default {
  launch() {
    router.push ({
      url: 'pages/pageB/pageB'
    });
  },
  onInit() {
    console.info('PageA onInit');
  },
  onReady() {
    console.info('PageA onReady');
  },
  onShow() {
    console.info('PageA onShow');
  },
  onHide() {
    console.info('PageA onHide');
  },
  onDestroy() {
    console.info('PageA onDestroy');
  },
  onBackPress() {
    console.info('PageA onBackPress');
  },
  onActive() {
    console.info('PageA onActive');
  },
  onInactive() {
    console.info('PageA onInactive');
  },
  onNewRequest() {
    console.info('PageA onNewRequest');
  }
}

**pageB** implementation:

<!-- pageB.hml -->
<div class="container">
  <text class="title">This is PageB</text>
</div>

/\* pageB.css \*/
.container {
  flex-direction: column;
  align-items: center;
  width: 100%;
  height: 100%;
}
.title {
  font-size: 38px;
  text-align: center;
  width: 100%;
  height: 40%;
}

// pageB.js
export default {
  onInit() {
    console.info('PageB onInit');
  },
  onReady() {
    console.info('PageB onReady');
  },
  onShow() {
    console.info('PageB onShow');
  },
  onHide() {
    console.info('PageB onHide');
  },
  onDestroy() {
    console.info('PageB onDestroy');
  },
  onBackPress() {
    console.info('PageB onBackPress');
  },
  onActive() {
    console.info('PageB onActive');
  },
  onInactive() {
    console.info('PageB onInactive');
  },
  onNewRequest() {
    console.info('PageB onNewRequest');
  }
}

Run the program and observe the logs to review the sequence of lifecycle function calls. The call sequence of lifecycle functions of **pageA** is as follows:

-   Launch the application and enter **pageA**: onInit() -> onReady() -> onActive() -> onShow()
    
-   Navigate from **pageA** to **pageB**: onHide()
    
-   Return from **pageB** to **pageA**: onShow()
    
-   Exit **pageA**: onBackPress() -> onInactive() -> onHide()
    
-   **pageA** moves to the background: onInactive() -> onHide()
    
-   **pageA** restores from the background: onNewRequest() -> onShow() -> onActive()
    

The call sequence of lifecycle functions of **pageB** is as follows:

-   Navigate from **pageA** to **pageB**: onInit() -> onReady() -> onShow()
    
-   Return to **pageA** from **pageB**: onBackPress() -> onHide() -> onDestroy()
    
-   **pageB** moves to the background: onInactive() -> onHide()
    
-   **pageB** restores from the background: onNewRequest() -> onShow() -> onActive()
