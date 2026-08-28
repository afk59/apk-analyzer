# Developing User-Agent

User-Agent (UA) is a special string that contains key information such as the device type, operating system, and version. In web development, servers use this UA string to identify the source device and its features when processing requests, so that they can provide custom content and services appropriately. If UAs cannot be correctly identified, multiple exceptions may occur. For example, a page layout optimized for a mobile device may appear disordered when displayed on a desktop device, and vice versa. In addition, some browser features or CSS attributes are supported only in specific browser versions, so incorrect UA identification may lead to rendering issues or logic errors.

#### Default User-Agent Structure

-   String format
    
    Mozilla/5.0 ({DeviceType}; {OSName} {OSVersion}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{ChromeCompatibleVersion}.0.0.0 Safari/537.36 ArkWeb/{ArkWeb VersionCode} {DeviceCompat} {Extension}
    
-   Example
    
    Mozilla/5.0 (Phone; OpenHarmony 5.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36  ArkWeb/4.1.6.1 Mobile
    
-   Fields
    
    | Field | Description |
    | :-- | :-- |
    | DeviceType | 
    Device type.
    
    The value can be:
    
    \- [Phone](https://developer.huawei.com/consumer/en/doc/design-guides/phone-0000001776694632)
    
    \- [Tablet](https://developer.huawei.com/consumer/en/doc/design-guides/pad-0000001823654157)
    
    \- **PC** ([2-in-1 device](https://developer.huawei.com/consumer/en/doc/design-guides/2in1-0000001777531700))
    
     |
    | OSName | 
    
    [OS name](../../../../getting-started/harmonyos-terms/document.md#section15569823194110).
    
    Default value: **OpenHarmony**
    
     |
    | OSVersion | 
    
    OS version. The value is a two-digit number, in M.S format.
    
    You can obtain the value by extracting the first two digits of the version number from the system parameter **const.ohos.fullname**.
    
    Default value: **5.0**
    
     |
    | ChromeCompatibleVersion | 
    
    The version that is compatible with the main Chrome version. The earliest version is 114.
    
    Default value: **114**
    
     |
    | ArkWeb | 
    
    Web kernel name of the HarmonyOS version.
    
    Default value: **ArkWeb**
    
     |
    | ArkWeb VersionCode | 
    
    ArkWeb version number, in the format of a.b.c.d.
    
    Default value: **4.1.6.1**
    
     |
    | DeviceCompat | 
    
    Forward compatibility settings.
    
    Default value: **Mobile**
    
     |
    | Extension | 
    
    Field that can be extended by a third-party application.
    
    When a third-party application uses the **Web** component, UA can be extended. For example, an application information identifier can be added.
    
     |
    

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2a/v3/4sfp9ywBTOikumQrLU9TEA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061947Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=224AA1A29F30AF45BB290369C0D103756935CAD735FD2A3DC1C033CD5E0D537B)

-   Currently, there are two spaces before the **ArkWeb** field of the default **User-Agent**.
    
-   Currently, the **viewport** parameter of the **meta** tag on the frontend HTML page is enabled or disabled based on whether **User-Agent** contains the **Mobile** field. If a **User-Agent** does not contain the **Mobile** field, the **viewport** property in the **meta** tag is disabled by default. In this case, you can explicitly set the [metaViewport](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-basic-components-web-attributes#metaviewport12) property to **true** to overwrite the disabled state.
    
-   You are advised to use the **OpenHarmony** keyword to identify whether a device is a HarmonyOS device, and use the **DeviceType** keyword to identify the device type for page display on different devices. (The **ArkWeb** keyword indicates the web kernel of the device, and the **OpenHarmony** keyword indicates the operating system of the device.)
    
-   The **{DistributionOSName}** and **{DistributionOSVersion}** fields are not supported in versions earlier than API version 15. Since API version 15, they are not displayed in the default **User-Agent**.
    

#### Custom User-Agent Structure

In the following example, [getUserAgent()](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-webview-webviewcontroller#getuseragent) is used to obtain the default **User-Agent** string, which you can modify or extend as needed.

// xxx.ets
import { webview } from '@kit.ArkWeb';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();

  build() {
    Column() {
      Button('getUserAgent')
        .onClick(() => {
          try {
            let userAgent = this.controller.getUserAgent();
            console.log("userAgent: " + userAgent);
          } catch (error) {
            console.error(\`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}\`);
          }
        })
      Web({ src: 'www.example.com', controller: this.controller })
    }
  }
}

In the following example, [setCustomUserAgent()](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-webview-webviewcontroller#setcustomuseragent10) is used to set a custom user agent, which replaces the default user agent. To preserve compatibility, you are advised to append a custom extension, such as a third-party application identifier, to the default user agent, instead of overwriting it entirely.

When **src** of the **Web** component is set to a URL, set **User-Agent** in **onControllerAttached**, as demonstrated in the following example. Avoid setting **User-Agent** in **onLoadIntercept**, as this can lead to occasional failures. Failure to set **User-Agent** in **onControllerAttached**, may result in mismatches between the loaded page and the intended user agent specified in **setCustomUserAgent**.

When **src** of the **Web** component is set to an empty string, call **setCustomUserAgent** to set **User-Agent** before using **loadUrl** to load a specific page.

// xxx.ets
import { webview } from '@kit.ArkWeb';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();
  // Third-party application information identifier
  @State customUserAgent: string = ' DemoApp';

  build() {
    Column() {
      Web({ src: 'www.example.com', controller: this.controller })
      .onControllerAttached(() => {
        console.log("onControllerAttached");
        try {
          let userAgent = this.controller.getUserAgent() + this.customUserAgent;
          this.controller.setCustomUserAgent(userAgent);
        } catch (error) {
          console.error(\`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}\`);
        }
      })
    }
  }
}

In the following example, [getCustomUserAgent()](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-webview-webviewcontroller#getcustomuseragent10) is used to obtain the custom user agent.

// xxx.ets
import { webview } from '@kit.ArkWeb';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();
  @State userAgent: string = '';

  build() {
    Column() {
      Button('getCustomUserAgent')
        .onClick(() => {
          try {
            this.userAgent = this.controller.getCustomUserAgent();
            console.log("userAgent: " + this.userAgent);
          } catch (error) {
            console.error(\`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}\`);
          }
        })
      Web({ src: 'www.example.com', controller: this.controller })
    }
  }
}

#### FAQs

## How do I use User-Agent to identify different HarmonyOS devices?

HarmonyOS devices can be identified based on the OS name, OS version, and device type in **User-Agent**. You are advised to check all of them to ensure accurate device identification.

1.  Identification based on the OS name
    
    Use the **{OSName}** field.
    
    const isHarmonyOS = () => /OpenHarmony/i.test(navigator.userAgent);
    
2.  Identification based on the OS version
    
    Use the **{OSName}** and **{OSVersion}** fields. The format is **OpenHarmony + Version number**.
    
    const matches = navigator.userAgent.match(/OpenHarmony (\\d+\\.?\\d\*)/);
    matches?.length && Number(matches\[1\]) >= 5;
    
3.  Identification based on the device type
    
    Use the **deviceType** field.
    
    // Check whether the device is a mobile phone.
    const isPhone = () => /Phone/i.test(navigator.userAgent);
    
    // Check whether the device is a tablet.
    const isTablet = () => /Tablet/i.test(navigator.userAgent);
    
    // Check whether the device is a 2-in-1 device.
    const is2in1 = () => /PC/i.test(navigator.userAgent);
    

## How do I simulate HarmonyOS User-Agent for frontend debugging?

In Windows, macOS, and Linux, you can use the **User-Agent** override feature of DevTools to simulate a HarmonyOS **User-Agent** in Chrome, Edge, and Firefox.

#### Sample Code

-   [Web User Agent](https://gitcode.com/harmonyos_samples/web-user-agent/blob/master/README.en.md)
