# Using WebNativeMessagingExtensionAbility to Implement Communication Between Browser Extensions and Applications

#### Overview

Browser extensions can communicate with applications to access services for implementing the application's capabilities. For example, in a password manager, the application stores and encrypts passwords, allowing the browser extension to automatically fill in form fields on web pages.

Since API version 21, you can use the [WebNativeMessagingExtensionAbility](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-web-webnativemessagingextensionability) component in applications to provide backend services for browser extensions.

The browser extension connects to WebNativeMessagingExtensionAbility through the [WebExtensions runtime API](https://developer.mozilla.org/en-US/docs/Mozilla/Add-ons/WebExtensions/API/runtime). The two parties communicate with each other by calling the I/O API after sharing the pipe file descriptor.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d1/v3/Ta4NbfnJSl6EHvZ7kH6-dg/en-us_image_0000002537924974.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061949Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=CD55C3AAB7C29A61D5BC16C26E1F190B6A9C5A87CF46D6FB62E33C7B7E178C42)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/21/v3/z6wWsll6Tq6PzWkODOOSlg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061949Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=0C57179920FD504B2BC179524DD52182D993DE546396AD8CF5C1A82BA093D084)

In this topic, the connection established by a browser extension using the WebExtension API **runtime.connectNative** is referred to as a NativeMessaging connection.

NativeMessaging is provided for both application developers and browser application developers. They need to understand the operation mechanism of WebNativeMessagingExtensionAbility, but they focus on different scenarios and APIs. Application developers use the [WebNativeMessagingExtensionAbility](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-web-webnativemessagingextensionability) component to develop related services. Browser developers use the [WebNativeMessagingExtensionManager](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-web-webnativemessagingextensionmanager) APIs to establish the NativeMessaging connection.

This topic outlines the key considerations for different types of developers.

#### Constraints

## Device Constraints

The WebNativeMessagingExtensionAbility component takes effect only on 2-in-1 devices.

## Specifications

-   The WebNativeMessagingExtensionAbility component does not require permissions and can be integrated into any third-party application. However, the browser that starts the component must apply for the ACL permission (**ohos.permission.WEB\_NATIVE\_MESSAGING**), which is available only to browser applications.
    
-   APIs provided by [Window](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-window) cannot be called in the WebNativeMessagingExtensionAbility.
    
-   WebNativeMessagingExtensionAbility can only start the UIAbility of the current application, and cannot start the UIAbility of other applications or other types of ExtensionAbility.
    
-   WebNativeMessagingExtensionAbility is used only for communication between browser extensions and applications. It does not support other scenarios such as backend services.
    

#### Working Principles

## Overall Process

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3d/v3/7jP4bOxDQmOXvjacyUqh8w/en-us_image_0000002568684751.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061949Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=039BB18B3F04B1BBFFBE3C269040C18C546FB76A8522F4E531597187E96B4D86)

-   **Process**:

1.  The browser extension calls the **runtime.connectNative** API to pass the application's bundle name to create a NativeMessaging connection.
2.  The browser application calls the [dataShare](../../arkdata/cross-application-data-sharing/one-to-many-data-sharing/sharing-configurations-between-applications-arkts/document.md) API to obtain the application's configuration information, including the name of the WebNativeMessagingExtension and the access restriction rule (whether to allow an extension to access the WebNativeMessagingExtension).
3.  The browser application creates two pipes as a bidirectional channel, calls the [WebNativeMessagingExtensionManager.connectNative](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-web-webnativemessagingextensionmanager#webnativemessagingextensionmanagerconnectnative) API, starts the WebNativeMessagingExtension, creates a NativeMessaging connection, and transfers the pipe's file descriptors as parameters.
4.  The application's WebNativeMessagingExtensionAbility is started, the [WebNativeMessagingExtensionAbility.onConnectNative](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-web-webnativemessagingextensionability#onconnectnative) lifecycle callback is triggered, and the pipe's file descriptor is obtained.
5.  The application listens for the read-end file descriptor, obtains the message instructions sent by the browser extension, and sends the message instructions back through the write-end file descriptor.
6.  The application uses [WebNativeMessagingExtensionContext.startAbility](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-web-webnativemessagingextensioncontext#startability) to start its UIAbility page.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/27/v3/rytHjFGtS6-2UAafg4vTBA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061949Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=3ADC5E9A98A03B58AF01107FA0CF6C904A477304BCE38DE975681EEA59A6946C)

WebNativeMessagingExtensionAbility is a single-instance independent process. If the **connectNative** API is called multiple times, only one instance is started, and the **onConnectNative** callback is triggered multiple times. Therefore, the application needs to manage multiple sessions.

## Storing the Extension Configuration of Applications in dataShare

When integrating WebNativeMessagingExtensionAbility, the application needs to provide extension configurations for the browser application through **dataShare**. The browser application uses this configuration to determine the accessible extension and specify the name of the WebNativeMessagingExtensionAbility to be started.

The extension configuration is in JSON string format.

-   **abilityName**: name of the WebNativeMessagingExtensionAbility, in string format. This attribute is used to fill in the **abilityName** field of **want**. An application has only one WebNativeMessagingExtensionAbility.
-   **allowed\_origins**: array of URLs of browser extensions that can access the WebNativeMessagingExtensionAbility. You can configure multiple URLs. Different browser extensions have different scheme protocols. For example, the HUAWEI Browser uses the chrome-extension header.

Extension configuration format:

{
  // Set the application bundle name.
  "name": "com.example.myapplication",
  // Description.
  "description": "Send message to native app.",
  /\*
   \* Name of the WebNativeMessagingExtensionAbility, which is used to fill abilityName in want. An application has only one WebNativeMessagingExtensionAbility.
   \* WebNativeMessagingExtensionAbility
   \*/
  "abilityName": "webExtensionAbility",
  /\*
   \* URLs of browser extensions that are allowed to access the WebNativeMessagingExtensionAbility. Different browser extensions have different scheme protocols. HUAWEI Browser use the chrome-extension header.
   \*/
  "allowed\_origins":\[
    "chrome-extension://knldjmfmopnpolahpmmgbagdohdnhkik/"
  \]
}

The extension configuration is stored in [dataShare](../../arkdata/cross-application-data-sharing/one-to-many-data-sharing/sharing-configurations-between-applications-arkts/document.md#configuration-in-modulejson5). The URI is fixed in the format of **datashareproxy://\[Bundle name\]/browserNativeMessagingHosts**.

## Lifecycle Management of WebNativeMessagingExtensionAbility

-   [onConnectNative](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-web-webnativemessagingextensionability#onconnectnative): Triggered when the browser extension calls **runtime.connectNative**. If **WebNativeMessagingExtensionAbility** is not running, calling **runtime.connectNative** will start **WebNativeMessagingExtensionAbility** and trigger this callback.
-   [onDisconnectNative](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-web-webnativemessagingextensionability#ondisconnectnative): Triggered when the browser extension destroys **runtime.port** or when a nativeMessaging connection disconnects. When all connections are disconnected, the **onDestroy** callback is triggered and WebNativeMessagingExtensionAbility is closed.
-   [onDestroy](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-web-webnativemessagingextensionability#ondestroy): Triggered before the WebNativeMessagingExtensionAbility is destroyed. If all NativeMessaging connections are disconnected, the WebNativeMessagingExtensionAbility will be destroyed.
-   [stopNativeConnection](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-web-webnativemessagingextensioncontext#stopnativeconnection): Triggered to proactively disconnect a NativeMessaging connection. If the last connection is disconnected, the WebNativeMessagingExtensionAbility will be destroyed.
-   [terminateSelf](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-web-webnativemessagingextensioncontext#terminateself): Triggered to proactively exit. If this callback is invoked, all NativeMessaging connections will be destroyed.

## Message Format and Restrictions

Format of NativeMessaging connections: Each message is serialized using JSON, encoded in UTF-8, and prefixed with a 32-bit message length (in native byte order). To protect the browser from being affected by abnormal applications, the maximum size of a single message from WebNativeMessagingExtensionAbility is 1 MB. The maximum size of a message sent to the WebNativeMessagingExtensionAbility is 64 MB.

## Implementing the connectNative Extension (for Application Developers)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/67/v3/5cDRQsttQKSCEUjZh3BhSA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061949Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=30448A67EAAAD6B2C293CE00E43137CE0E2350B19F401B0F9BDCEFA0C5B353FA)

You need to configure **manifest.json** and **background.js** based on the W3C standard to implement communication.

**chrome.runtime.connectNative** or **chrome.runtime.sendNativeMessage** can be used for connection.

Configure the plugin content, send ping strings, and receive pong responses. The sample code is as follows:

Configure the **manifest.json** file.

{
  "name": "com.example.myapplication",
  "version": "1.0.1",
  "description": "Launch APP",
  "manifest\_version": 3,
  "permissions": \["nativeMessaging", "tabs", "scripting"\], // Set this parameter as required.
  "host\_permissions": \["http://\*/\*", "https://\*/\*", "ftp://\*/\*", "file://\*/\*"\], // Set this parameter as required.
  "background": {
    "service\_worker": "background.js" // Used to run the runtime command of the plugin.
  },
  "content\_scripts": \[
    {
      "matches": \["http://\*/\*", "https://\*/\*", "ftp://\*/\*", "file://\*/\*"\], // Set this parameter as required.
      "js": \["main.js"\] // Used to run the JS command of the plugin.
    }
  \],
  "action": {
    "default\_popup": "index.html" // Display the plugin page.
  }
}

Implement the **main.js** file.

// Trigger the calling from HTML.
function sendMessageToNative() {
  var message = "ping"; // Send a ping packet.
  chrome.runtime.sendMessage({
    type: "sendMessage",
    message: message
  }, function (response) {});
}

Implement the **background.js** file.

1.  Use **chrome.runtime.connectNative** for connection.
    
    var port = null;
    // Listen for messages from main.js.
    chrome.runtime.onMessage.addListener(
      function (request, sender, sendResponse) {
        if (request.type == "sendMessage") {
          if (port == null) {
            connectToNativeHost();
          }
          port.postMessage(request.message); // Send messages to the application.
        }
        return true; // Keep the message channel open.
    });
    function connectToNativeHost() {
      var bundleName = "com.example.app"; // Bundle name of the application corresponding to the plugin.
      port = chrome.runtime.connectNative(bundleName); // Obtain the communication port based on the bundleName.
      port.onMessage.addListener(onNativeMessage); // Listen for whether the native application sends messages.
      port.onDisconnect.addListener(onDisconnected); // Listen for disconnection.
    }
     // Triggered when a message is received from the native application.
    async function onNativeMessage(message) {
      console.info('Received message from the native application: ' + JSON.stringify(message)); // Pong in the example.
    }
    // Triggered when the connection is disconnected.
    function onDisconnected() {
      port = null;
    }
    
2.  Use **chrome.runtime.sendNativeMessage** for connection.
    
    function sendNativeMessage() {
      var bundleName = "com.example.app"; // Bundle name of the application corresponding to the plugin.
      var nativeMessage = "ping"; // Message to be sent by the plugin to the application.
      chrome.runtime.sendNativeMessage(
        bundleName,
        {message: nativeMessage},
        function(response) {
        // Disconnect the connection after receiving a response from the application.
        console.info("sendNativeMessage received response from the application:", JSON.stringify (response));
        }
      )
    }
    

## Implementing the WebNativeMessagingExtensionAbility (for Application Developers)

To manually create a WebNativeMessagingExtensionAbility in the DevEco Studio project, perform the following steps:

1.  In the **ets** directory of a module in the project, right-click and choose **New > Directory** to create a directory named **MyWebNativeMessageExtAbility**.
    
2.  Right-click the **MyWebNativeMessageExtAbility** directory, and choose **New > ArkTS File** to create a file named **MyWebNativeMessageExtAbility.ets**.
    
    The directory structure is as follows:
    
     ├── ets
     │ ├── MyWebNativeMessageExtAbility
     │ │   ├── MyWebNativeMessageExtAbility.ets
     └
    
3.  In the **MyWebNativeMessageExtAbility.ets** file, import the [WebNativeMessagingExtensionAbility](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-web-webnativemessagingextensionability) module. Customize a class that inherits from WebNativeMessagingExtensionAbility and implement the lifecycle callbacks.
    
    import { WebNativeMessagingExtensionAbility, ConnectionInfo } from '@kit.ArkWeb';
    import { hilog } from '@kit.PerformanceAnalysisKit';
    import {buffer, util} from '@kit.ArkTS';
    import { fileIo as fs } from '@kit.CoreFileKit';
    
    const TAG: string = '\[MyWebNativeMessageExtAbility\]';
    const DOMAIN\_NUMBER: number = 0xFF00;
    
    export default class MyWebNativeMessageExtAbility extends WebNativeMessagingExtensionAbility {
      // Read the message sent by the extension and reply.
      async ReadAsync(fdRead:number, fdWrite:number) : Promise<void> {
        try {
          // read
          let arrayBuffer = new ArrayBuffer(1024);
          let readLen = await fs.read(fdRead, arrayBuffer);
          if (readLen <= 4) {
            hilog.error(DOMAIN\_NUMBER, TAG, 'read pipe length failed');
            return;
          }
          hilog.info(DOMAIN\_NUMBER, TAG, 'read pipe %{public}s', buffer.from(arrayBuffer, 4, readLen - 4).toString());
    
          // write
          let strResponse : string = "pong";
          const encoder = new util.TextEncoder("utf-8");
          const strBytes = encoder.encodeInto(strResponse);
          let bufferLen = strBytes.length;
          const lenBytes = new Uint8Array(4);
          lenBytes\[0\] = (bufferLen >> 0) & 0xFF;
          lenBytes\[1\] = (bufferLen >> 8) & 0xFF;
          lenBytes\[2\] = (bufferLen >> 16) & 0xFF;
          lenBytes\[3\] = (bufferLen >> 24) & 0xFF;
          const writeBuffer = new Uint8Array(4 + bufferLen);
          writeBuffer.set(lenBytes, 0);
          writeBuffer.set(strBytes, 4);
          let writeLen = await fs.write(fdWrite, writeBuffer.buffer);
          hilog.info(DOMAIN\_NUMBER, TAG, 'write pipe length %{public}d', writeLen);
        } catch (err) {
          hilog.error(DOMAIN\_NUMBER, TAG, 'fs io failed, error code: ' + err.code + " message: " + err.code);
        }
      }
    
      onConnectNative(info: ConnectionInfo): void {
        hilog.info(DOMAIN\_NUMBER, TAG,
          \`onConnectNative, connectionId ${info.connectionId} caller bundle: ${info.bundleName}, extension origin: ${info.extensionOrigin}, pipe Read: ${info.fdRead}, pipe write ${info.fdWrite}  \`);
        this.ReadAsync(info.fdRead, info.fdWrite)
      }
    
      onDisconnectNative(info: ConnectionInfo): void {
        hilog.info(DOMAIN\_NUMBER, TAG, \`onDisconnectNative, connectionId: ${info.connectionId}\`);
      }
    
      onDestroy(): void {
        hilog.info(DOMAIN\_NUMBER, TAG, 'onDestroy');
      }
    };
    
4.  Register the WebNativeMessagingExtensionAbility component in the [module.json5 file](../../../getting-started/development-fundamentals/application-configuration-files-in-stage-model/module-json5-configuration-file/document.md) of the module in the project. Set **type** to **"webNativeMessaging"** and **srcEntry** to the code path of the component.
    
    {
      "module": {
        // ...
        "extensionAbilities": \[
          {
            "name": "MyWebNativeMessageExtAbility",
            "description": "webNativeMessaging",
            "type": "webNativeMessaging",
            "exported": true,
            "srcEntry": "./ets/MyWebNativeMessageExtAbility/ MyWebNativeMessageExtAbility.ets"
          }
        \]
      }
    }
    
5.  Configure **crossAppSharedConfig** in the [module.json5 file](../../../getting-started/development-fundamentals/application-configuration-files-in-stage-model/module-json5-configuration-file/document.md) of the module of the project. The shared configuration file must be stored in the **resources/base/profile** directory of the project and referenced using the **$** symbol.
    
    {
      "module": {
        "crossAppSharedConfig": "$profile:shared\_config"
      }
    }
    
6.  Add the [extension configuration](#storing-the-extension-configuration-of-applications-in-datashare) to **shared\_config.json**.
    
    {
      "crossAppSharedConfig": \[
        // ...
        {
          // Fixed URI format: datashareproxy://\[Bundle name\]/browserNativeMessagingHosts. The browser application obtains the value from the URI, that is, the extension configuration.
          "uri": "datashareproxy://com.example.app/browserNativeMessagingHosts",
          // Extension configuration. For details about the format, see "Storing the Extension Configuration of Native Applications in dataShare". Be sure to use escape characters.
          "value": "{\\"name\\": \\"com.example.myapplication\\",\\"description\\": \\"Send message to native app.\\",\\"abilityName\\": \\"MyWebNativeMessageExtAbility\\", \\"allowed\_origins\\":\[\\"chrome-extension://knldjmfmopnpolahpmmgbagdohdnhkik/\\"\]}",
          "allowList": \[
            // appIdentifier of the application that is allowed to access. Add the appIdentifier of the browser.
            "1234567890123456789"
          \]
        }
      \]
    }
    

## Implementing the WebNativeMessagingExtensionAbility (for Browser Developers)

The browser implements the extension runtime APIs, starts the WebNativeMessagingExtensionAbility, and establishes and manages NativeMessaging connections. The **ohos.permission.WEB\_NATIVE\_MESSAGING** permission is required.

1.  When receiving a NativeMessaging connection creation request, the browser obtains the extension configuration of the target application through the [get() API](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-data-datashare#get20), reads the name of WebNativeMessagingExtensionAbility and the list of extensions that can be accessed, and checks whether the access is allowed.
    
    import { dataShare } from '@kit.ArkData';
    
    interface ExtensionConfig {
      abilityName:string;
      allowed\_origins:string\[\];
    }
    
    async function getManifestData(bundleName:string, connectExtensionOrigin:string) {
      try {
       // Call the dataShare API to obtain the extension configuration.
        const dsProxyHelper = await dataShare.createDataProxyHandle();
        const urisToGet = \[\`datashareproxy://${bundleName}/browserNativeMessagingHosts\`\];
        const config : dataShare.DataProxyConfig = {
          type: dataShare.DataProxyType.SHARED\_CONFIG,
        };
        const results = await dsProxyHelper.get(urisToGet, config);
        let foundValid = false;
        for (let i = 0; i < results.length; i++) {
          try {
            const result = results\[i\];
            const json = result.value;
            if (typeof json !== "string") {
              continue;
            }
            let jsonStr:string = json as string;
            let info:ExtensionConfig = JSON.parse(jsonStr);
            if (info.abilityName) {
              console.info('Native message json info is ok');
              if (!Array.isArray(info.allowed\_origins)) {
                info.allowed\_origins = \[info.allowed\_origins\];
              }
              if (!info.allowed\_origins.includes(connectExtensionOrigin)) {
                console.error('Origin not allowed, continue searching');
                continue;
              }
              foundValid = true;
              break;
            }
          } catch (error) {
            console.error('NativeMessage JSON parse error:', error);
          }
        }
        if (!foundValid) {
          console.error('NativeMessage JSON no valid manifest found');
        } else {
          console.info('NativeMessage allowed\_origins match ok');
        }
      } catch (error) {
        console.error('Error getting config:', error);
      }
    }
    
2.  Call [webNativeMessagingExtensionManager.connectNative](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-web-webnativemessagingextensionmanager#webnativemessagingextensionmanagerconnectnative) to create a NativeMessage. If the WebNativeMessagingExtensionAbility is not running, this API will start the ExtensionAbility and trigger the WebNativeMessagingExtensionAbility.
    
    import { UIAbility, Want, common } from '@kit.AbilityKit';
    import { webNativeMessagingExtensionManager } from '@kit.ArkWeb'
    
    class ConnectionCallback implements webNativeMessagingExtensionManager.WebExtensionConnectionCallback {
      onConnect(connection:webNativeMessagingExtensionManager.ConnectionNativeInfo) {
        // connected
        console.error(\`onConnect id ${connection.connectionId} is connected\`);
      }
      onDisconnect(connection:webNativeMessagingExtensionManager.ConnectionNativeInfo) {
        // disconnect
        console.error(\`onDisconnect id ${connection.connectionId} is connected\`);
      }
      onFailed(code:webNativeMessagingExtensionManager.NmErrorCode, errMsg:string) {
        console.error(\`onFailed error code is ${code}, errMsg is ${errMsg}\`);
      }
    }
    
    function connectNative(abilityContext: common.UIAbilityContext, bundleName: string, abilityName: string,
      connectExtensionOrigin: string, readPipe: number, writePipe: number) : void {
      try {
        let wantInfo:Want = {
          bundleName: bundleName,
          abilityName: abilityName,
          parameters: {
            'ohos.arkweb.messageReadPipe': { 'type': 'FD', 'value': readPipe },
            'ohos.arkweb.messageWritePipe': { 'type': 'FD', 'value': writePipe },
            'ohos.arkweb.extensionOrigin': connectExtensionOrigin
          },
        };
    
        let options : ConnectionCallback = new ConnectionCallback;
        let connectId = webNativeMessagingExtensionManager.connectNative(abilityContext, wantInfo, options);
        console.info(\`innerWebNativeMessageManager  connectionId : ${connectId}\` );
      } catch (error) {
        console.info(\`inner callback error Message: ${JSON.stringify(error)}\`);
      }
    }
    
3.  Call [webNativeMessagingExtensionManager.disconnectNative](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-web-webnativemessagingextensionmanager#webnativemessagingextensionmanagerdisconnectnative) to destroy the NativeMessaging connection.
    
    import { webNativeMessagingExtensionManager } from '@kit.ArkWeb'
    
    function disconnectNative(connectId: number) : void {
      console.info(\`NativeMessageDisconnect start connectionId is ${connectId}\`);
      webNativeMessagingExtensionManager.disconnectNative(connectId);
    }
