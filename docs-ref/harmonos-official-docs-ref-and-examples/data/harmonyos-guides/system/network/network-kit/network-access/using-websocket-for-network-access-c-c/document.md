# Using WebSocket for Network Access (C/C++)

#### When to Use

The WebSocket module can be used to establish bidirectional connections between the server and the client.

#### Available APIs

The following table lists the common WebSocket APIs. For details, see [net\_websocket.h](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-net-websocket-h).

| API | Description |
| :-- | :-- |
| OH\_WebSocketClient\_Constructor(WebSocket\_OnOpenCallback onOpen, WebSocket\_OnMessageCallback onMessage, WebSocket\_OnErrorCallback onError, WebSocket\_OnCloseCallback onclose) | Constructor used to create a WebSocket client. |
| OH\_WebSocketClient\_AddHeader(struct WebSocket \*client, struct WebSocket\_Header header) | Adds the header information to the client request. |
| OH\_WebSocketClient\_Connect(struct WebSocket \*client, const char \*url, struct WebSocket\_RequestOptions options) | Connects the WebSocket client to the server. |
| OH\_WebSocketClient\_Send(struct WebSocket \*client, char \*data, size\_t length) | Sends data from the WebSocket client to the server. |
| OH\_WebSocketClient\_Close(struct WebSocket \*client, struct WebSocket\_CloseOption options) | Lets the WebSocket client proactively close the connection. |
| OH\_WebSocketClient\_Destroy(struct WebSocket \*client) | Releases the context and resources of the WebSocket connection. |

#### Development Example

## How to Develop

To use related APIs to establish a connection to the WebSocket server, you need to create a Native C++ project, encapsulate the APIs in the source file, and call these APIs at the ArkTS layer. You can use **hilog** or **console.log** to print the log information on the console or generate device logs.

The following walks you through on how to establish a connection to the WebSocket server, send messages to the WebSocket server, and close the WebSocket connection.

## Adding Dependencies

**Adding Dynamic Link Libraries**

Add the following library to **CMakeLists.txt**.

libace\_napi.z.so
libnet\_websocket.so

**Including Header Files**

#include "napi/native\_api.h"
#include "network/netstack/net\_websocket.h"
#include "network/netstack/net\_websocket\_type.h"

## Building the Project

1.  Write the API call code in the source file to allow applications to receive the URL string passed from ArkTS, create a pointer to the **WebSocketClient** object, and check whether the connection to the WebSocket server is successful.

#include "napi/native\_api.h"
#include "network/netstack/net\_websocket.h"
#include "network/netstack/net\_websocket\_type.h"
#include "hilog/log.h"

#include <cstring>

#undef LOG\_DOMAIN
#undef LOG\_TAG
#define LOG\_DOMAIN 0x3200 // Global domain, which identifies the service domain.
#define LOG\_TAG "WSDEMO"  // Global tag, which identifies the module log tag.

// Global variables of the WebSocket client
static struct WebSocket \*g\_client = nullptr;

static void onOpen(struct WebSocket \*wsClient, WebSocket\_OpenResult openResult)
{
    (void)wsClient;
    OH\_LOG\_INFO(LOG\_APP, "onOpen: code: %{public}u, reason: %{public}s", openResult.code, openResult.reason);
}

static void onMessage(struct WebSocket \*wsClient, char \*data, uint32\_t length)
{
    (void)wsClient;
    char \*tmp = new char\[length + 1\];
    for (uint32\_t i = 0; i < length; i++) {
        tmp\[i\] = data\[i\];
    }
    tmp\[length\] = '\\0';
    OH\_LOG\_INFO(LOG\_APP, "onMessage: len: %{public}u, data: %{public}s", length, tmp);
}

static void onError(struct WebSocket \*wsClient, WebSocket\_ErrorResult errorResult)
{
    (void)wsClient;
    OH\_LOG\_INFO(LOG\_APP, "onError: code: %{public}u, message: %{public}s", errorResult.errorCode,
                errorResult.errorMessage);
}

static void onClose(struct WebSocket \*wsClient, WebSocket\_CloseResult closeResult)
{
    (void)wsClient;
    OH\_LOG\_INFO(LOG\_APP, "onClose: code: %{public}u, reason: %{public}s", closeResult.code, closeResult.reason);
}

static napi\_value ConnectWebsocket(napi\_env env, napi\_callback\_info info)
{
    size\_t argc = 2;
    napi\_value args\[2\] = {nullptr};
    napi\_value result;

    napi\_get\_cb\_info(env, info, &argc, args, nullptr, nullptr);

    size\_t length = 0;
    napi\_status status = napi\_get\_value\_string\_utf8(env, args\[0\], nullptr, 0, &length);
    if (status != napi\_ok) {
        napi\_get\_boolean(env, false, &result);
        return result;
    }

    if (g\_client != nullptr) {
        OH\_LOG\_INFO(LOG\_APP, "there is already one websocket client running.");
        napi\_get\_boolean(env, false, &result);
        return result;
    }
    char \*buf = new char\[length + 1\];
    std::memset(buf, 0, length + 1);
    napi\_get\_value\_string\_utf8(env, args\[0\], buf, length + 1, &length);
    // Create a pointer to the WebSocketClient object.
    g\_client = OH\_WebSocketClient\_Constructor(onOpen, onMessage, onError, onClose);
    if (g\_client == nullptr) {
        delete\[\] buf;
        napi\_get\_boolean(env, false, &result);
        return result;
    }
    // Connect to the WebSocket server identified by the URL stored in the buffer.
    int connectRet = OH\_WebSocketClient\_Connect(g\_client, buf, {});

    delete\[\] buf;
    napi\_get\_boolean(env, connectRet == 0, &result);
    return result;
}

static napi\_value SendMessage(napi\_env env, napi\_callback\_info info)
{
    size\_t argc = 1;
    napi\_value args\[1\] = {nullptr};
    napi\_value result;

    napi\_get\_cb\_info(env, info, &argc, args, nullptr, nullptr);

    size\_t length = 0;
    napi\_status status = napi\_get\_value\_string\_utf8(env, args\[0\], nullptr, 0, &length);
    if (status != napi\_ok) {
        napi\_create\_int32(env, -1, &result);
        return result;
    }

    if (g\_client == nullptr) {
        OH\_LOG\_INFO(LOG\_APP, "websocket client not connected.");
        napi\_create\_int32(env, WebSocket\_ErrCode::WEBSOCKET\_CLIENT\_NULL, &result);
        return result;
    }
    char \*buf = new char\[length + 1\];
    std::memset(buf, 0, length + 1);
    napi\_get\_value\_string\_utf8(env, args\[0\], buf, length + 1, &length);
    // Send the messages in the buffer to the server.
    int ret = OH\_WebSocketClient\_Send(g\_client, buf, length);

    delete\[\] buf;
    napi\_create\_int32(env, ret, &result);
    return result;
}

static napi\_value CloseWebsocket(napi\_env env, napi\_callback\_info info)
{
    napi\_value result;
    if (g\_client == nullptr) {
        OH\_LOG\_INFO(LOG\_APP, "websocket client not connected.");
        napi\_create\_int32(env, -1, &result);
        return result;
    }
    // Close the WebSocket connection.
    int ret = OH\_WebSocketClient\_Close(g\_client, {
                                                   .code = 0,
                                                   .reason = "Actively Close",
                                               });
    // Release the WebSocket resources.
    OH\_WebSocketClient\_Destroy(g\_client);
    g\_client = nullptr;
    napi\_create\_int32(env, ret, &result);
    return result;
}

On receiving a WebSocket URL, the **ConnectWebsocket** function attempts to connect to the server identified by the URL. If the connection is successful, **true** is returned. Otherwise, **false** is returned. Before creating a pointer to the **WebSocketClient** object, define the **onOpen**, **onMessage**, **onError**, and **onClose** callbacks for the WebSocket connection. In the sample code, functions such as OH\_WebSocketClient\_Send and OH\_WebSocketClient\_Close are also called to send messages to the server and proactively close the WebSocket connection.

1.  Initialize and export the napi\_value objects encapsulated through **NAPI**, and expose the preceding functions to JavaScript through external function APIs. In the sample code, the ConnectWebsocket function is exposed as the external function Connect, the SendMessage function is exposed as the external function Send, and the CloseWebsocket function is exposed as the external function Close.

EXTERN\_C\_START
static napi\_value Init(napi\_env env, napi\_value exports)
{
    napi\_property\_descriptor desc\[\] = {
        {"Connect", nullptr, ConnectWebsocket, nullptr, nullptr, nullptr, napi\_default, nullptr},
        {"Send", nullptr, SendMessage, nullptr, nullptr, nullptr, napi\_default, nullptr},
        {"Close", nullptr, CloseWebsocket, nullptr, nullptr, nullptr, napi\_default, nullptr},
    };
    napi\_define\_properties(env, exports, sizeof(desc) / sizeof(desc\[0\]), desc);
    return exports;
}
EXTERN\_C\_END

1.  Register the objects successfully initialized in the previous step into the Node.js file by using the napi\_module\_register function of RegisterEntryModule.

static napi\_module demoModule = {
    .nm\_version = 1,
    .nm\_flags = 0,
    .nm\_filename = nullptr,
    .nm\_register\_func = Init,
    .nm\_modname = "entry",
    .nm\_priv = ((void \*)0),
    .reserved = {0},
};

extern "C" \_\_attribute\_\_((constructor)) void RegisterEntryModule(void) { napi\_module\_register(&demoModule); }

1.  Define the types of the functions in the index.d.ts file of the project. For example, the Connect function takes a string parameter as the input parameter and returns a Boolean value indicating whether the WebSocket connection is successfully established.

export const Connect: (url: string) => boolean;
export const Send: (data: string) => number;
export const Close: () => number;

1.  Call the encapsulated APIs in the index.ets file.

import testWebsocket from 'libentry.so';

@Entry
@Component
struct Index {
  @State wsUrl: string = '';
  @State content: string = '';
  @State connecting: boolean = false;

  build() {
    Navigation() {
      Column() {
        Column() {
          Text($r('app.string.WebSocket\_address'))
            .fontColor(Color.Gray)
            .textAlign(TextAlign.Start)
            .width('100%')
          TextInput()
            .width('100%')
            .id('textInput\_address')
            .onChange((value) => {
              this.wsUrl = value;
            })
        }
        .margin({
          bottom: 16 // Spacing from the bottom
        })
        .padding({
          left: 16, // Spacing from the left
          right: 16 // Spacing from the right
        })

        Column() {
          Text($r('app.string.Content'))
            .fontColor(Color.Gray)
            .textAlign(TextAlign.Start)
            .width('100%')
          TextInput()
            .width('100%')
            .id('textInput\_content')
            .enabled(this.connecting)
            .onChange((value) => {
              this.content = value;
            })
        }
        .margin({
          bottom: 16 // Spacing from the bottom
        })
        .padding({
          left: 16, // Spacing from the left
          right: 16 // Spacing from the right
        })

        Blank()

        Column({
          space: 12 // Spacing
        }) {
          Button($r('app.string.Connect'))
            .id('Connect')
            .enabled(!this.connecting)
            .onClick(() => {
              let connRet = testWebsocket.Connect(this.wsUrl);
              if (connRet) {
                this.connecting = true;
                // ···
              }
            // ···
            })
          Button($r('app.string.Send'))
            .id('Send')
            .enabled(this.connecting)
            .onClick(() => {
              testWebsocket.Send(this.content);
            // ···
            })
          Button($r('app.string.Close'))
            .id('Close')
            .enabled(this.connecting)
            .onClick(() => {
              let closeResult = testWebsocket.Close();
              if (closeResult != -1) {
                this.connecting = false;
                // ···
              }
            // ···
            })
        }
      }
    }
  }
}

1.  Configure the CMakeLists.txt file. Add the required shared library, that is, libnet\_websocket.so, to target\_link\_libraries in the CMakeLists.txt file automatically generated by the project.

As shown in the following figure, entry in add\_library is the modename automatically generated by the project. If you want to change its value, ensure that it is the same as the .nm\_modname in step 3.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7/v3/x6IJkUiYQKmW0vvclfabkg/en-us_image_0000002568684809.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062016Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=F75227D5DEA2E8BC207DE9B694CDA9F2D6886EE6675F513A5576E1DA233A9832)

1.  To call WebSocket C APIs, make sure that you have the ohos.permission.INTERNET permission. Add this permission to the requestPermissions item in the module.json5 file.

After the preceding steps, the entire project is set up. Then, you can connect to the device to run the project to view logs.

#### Test Procedure

1.  Connect the device and use DevEco Studio to open the project.
    
2.  Run the project. The following page is displayed.
    

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/65/v3/oHlFgHrOSKOcWg8LA_1Oow/en-us_image_0000002568764819.jpg?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062016Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=C2AA47AA24FE4D1FD869B524720F5D777224BA885140BA169D9E660510491252)

Description of settings:

-   In the text box in the first line, enter a WebSocket URL starting with ws:// or wss://.
    
-   Tap Connect. If the connection is successful, the **onOpen** callback is triggered and logs are printed.
    
-   Enter the content to be sent to the server in the Content text box and tap Send. If the server returns a message, the onMessage callback is triggered and logs are printed.
    
-   Tap Close. The WebSocket connection is released. You can enter a new WebSocket URL to establish a new connection.
    

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e5/v3/VU7lA-vGTXOZrp0JGB5ISQ/en-us_image_0000002537765094.jpg?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062016Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=328D8637698E2F6BAB91B39411542A359D22D4199B9375754D0FBCD043872758)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6e/v3/EVr3U4_xRma6cKgC9gHyPA/en-us_image_0000002537925034.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062016Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=1D2C7460654979037DBB5D76A0F225034031A12F09AD3C878A857882F6BA5015)
