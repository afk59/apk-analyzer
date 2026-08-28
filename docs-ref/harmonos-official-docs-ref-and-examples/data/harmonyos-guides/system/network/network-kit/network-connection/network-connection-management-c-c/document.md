# Network Connection Management (C/C++)

#### When to Use

The **NetConnection** module provides the capability of querying common network information.

#### Available APIs

The following table lists the common NetConnection APIs. For details, see [net\_connection.h](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-net-connection-h).

| API | **Test Description** |
| :-- | :-- |
| OH\_NetConn\_HasDefaultNet(int32\_t \*hasDefaultNet) | Checks whether the default data network is activated and determines whether a network connection is available. |
| OH\_NetConn\_GetDefaultNet(NetConn\_NetHandle \*netHandle) | Obtains the default active data network. |
| OH\_NetConn\_IsDefaultNetMetered(int32\_t \*isMetered) | Checks whether the data traffic usage on the current network is metered. |
| OH\_NetConn\_GetConnectionProperties(NetConn\_NetHandle \*netHandle, NetConn\_ConnectionProperties \*prop) | Obtains network connection information based on the specified **netHandle**. |
| OH\_NetConn\_GetNetCapabilities (NetConn\_NetHandle \*netHandle, NetConn\_NetCapabilities \*netCapacities) | Obtains network capability information based on the specified **netHandle**. |
| OH\_NetConn\_GetDefaultHttpProxy (NetConn\_HttpProxy \*httpProxy) | Obtains the default HTTP proxy configuration of the network. If the global proxy is set, the global HTTP proxy configuration is returned. If the application has been bound to the network specified by **netHandle**, the HTTP proxy configuration of this network is returned. In other cases, the HTTP proxy configuration of the default network is returned. |
| OH\_NetConn\_GetAddrInfo (char \*host, char \*serv, struct addrinfo \*hint, struct addrinfo \*\*res, int32\_t netId) | Obtains the DNS result based on the specified **netId**. |
| OH\_NetConn\_FreeDnsResult(struct addrinfo \*res) | Releases the DNS query result. |
| OH\_NetConn\_GetAllNets(NetConn\_NetHandleList \*netHandleList) | Obtains the list of all connected networks. |
| OHOS\_NetConn\_RegisterDnsResolver(OH\_NetConn\_CustomDnsResolver resolver) | 
Registers a custom DNS resolver.

Note: This API is deprecated since API version 13.

You are advised to use **OH\_NetConn\_RegisterDnsResolver** instead.

 |
| OHOS\_NetConn\_UnregisterDnsResolver(void) | 

Unregisters a custom DNS resolver.

Note: This API is deprecated since API version 13.

You are advised to use **OH\_NetConn\_UnregisterDnsResolver** instead.

 |
| OH\_NetConn\_RegisterDnsResolver(OH\_NetConn\_CustomDnsResolver resolver) | Registers a custom DNS resolver. |
| OH\_NetConn\_UnregisterDnsResolver(void) | Unregisters a custom DNS resolver. |
| OH\_NetConn\_SetPacUrl(const char \*pacUrl) | Sets the URL of the system-level proxy auto-config (PAC) script. |
| OH\_NetConn\_GetPacUrl(char \*pacUrl) | Obtains the URL of the system-level PAC script. |
| OH\_NetConn\_QueryProbeResult(char \*destination, int32\_t duration, NetConn\_ProbeResultInfo \*probeResultInfo) | Queries the probe result. |
| OH\_NetConn\_QueryTraceRoute(char \*destination, NetConn\_TraceRouteOption \*option, NetConn\_TraceRouteInfo \*traceRouteInfo) | Queries trace route information. |

#### Development Example

## How to Develop

To use related APIs to obtain network information, you need to create a Native C++ project, encapsulate the APIs in the source file, and call these APIs at the ArkTS layer. You can use hilog or console.log to print the log information on the console or generate device logs.

This document describes how to obtain the default active data network as an example.

For details about other APIs, see the [Complete Sample Code](https://gitcode.com/openharmony/applications_app_samples/tree/master/code/DocsSample/NetWork_Kit/NetWorkKit_NetManager/NetConnection_Exploitation_case).

## Adding Dependencies

**Adding the Dynamic Link Library**

Add the following library to **CMakeLists.txt**.

libace\_napi.z.so
libnet\_connection.so

**Including Header Files**

#include "napi/native\_api.h"
#include "network/netmanager/net\_connection.h"
#include "network/netmanager/net\_connection\_type.h"

## Building the Project

1.  Write the code for calling the API in the source file, encapsulate it into a value of the napi\_value type, and return the value to the Node.js environment.
    
    // Obtain the default network.
    static napi\_value GetDefaultNet(napi\_env env, napi\_callback\_info info)
    {
        size\_t argc = 1; // Expect one function.
        napi\_value args\[1\] = {nullptr}; // Store the received parameters.
        napi\_get\_cb\_info(env, info, &argc, args, nullptr, nullptr);
        // ...
        int32\_t param;
        napi\_get\_value\_int32(env, args\[0\], &param); // Obtain an integer from args\[0\] and store the integer in param.
        
        NetConn\_NetHandle netHandle;
        if (param == 0) { // If the parameter is 0
            param = OH\_NetConn\_GetDefaultNet(NULL);
        } else {
            param = OH\_NetConn\_GetDefaultNet(&netHandle);
        }
    
        napi\_value result;
        napi\_create\_int32(env, param, &result);
        return result;
    }
    
    // Obtain the default network ID.
    static napi\_value NetId(napi\_env env, napi\_callback\_info info)
    {
        int32\_t defaultNetId;
        NetConn\_NetHandle netHandle;
        OH\_NetConn\_GetDefaultNet(&netHandle);
        defaultNetId = netHandle.netId; // Obtain the default netId.
        napi\_value result;
        napi\_create\_int32(env, defaultNetId, &result);
        return result;
    }
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c1/v3/3fQTwOGbTtuoXdgJ577d7w/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062016Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=B2F407F530100B729CF74F8E420DEEA0777416A45D26EC3430A3688BC1273877)
    
    The two functions are used to obtain information about the default network connection of the system. Wherein, GetDefaultNet is used to receive the test parameters passed from ArkTS and return the corresponding return value after the API is called. You can change param as needed. If the return value is **0**, the parameters are obtained successfully. If the return value is **401**, the parameters are incorrect. If the return value is **201**, the user does not have the operation permission. NetId indicates the ID of the default network connection. You can use the information for further network operations.
    
2.  Initialize and export the napi\_value objects encapsulated through **NAPI**, and expose the preceding two functions to JavaScript through external function APIs.
    
    EXTERN\_C\_START
    static napi\_value Init(napi\_env env, napi\_value exports)
    {
        // Information used to describe an exported attribute. Two properties are defined here: \`GetDefaultNet\` and \`NetId\`.
        napi\_property\_descriptor desc\[\] = {
            {"GetDefaultNet", nullptr, GetDefaultNet, nullptr, nullptr, nullptr, napi\_default, nullptr},
            {"NetId", nullptr, NetId, nullptr, nullptr, nullptr, napi\_default, nullptr},
            // ...
        };
        napi\_define\_properties(env, exports, sizeof(desc) / sizeof(desc\[0\]), desc);
        return exports;
    }
    EXTERN\_C\_END
    
3.  Register the objects successfully initialized in the previous step into the Node.js file by using the napi\_module\_register function of RegisterEntryModule.
    
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
    
4.  Define the types of the two functions in the index.d.ts file of the project.
    
    -   The GetDefaultNet function accepts the numeric parameter code and returns a numeric value.
    -   The NetId function does not accept parameters and returns a numeric value.
    
    export const GetDefaultNet: (code: number) => number;
    export const NetId: () => number;
    
5.  Call the encapsulated APIs in the index.ets file.
    
    import testNetManager from 'libentry.so';
    import { hilog } from '@kit.PerformanceAnalysisKit';
    
    enum ReturnCode {
      SUCCESS = 0, // Operation succeeded.
      MISSING\_PERMISSION = 201, // Missing permissions.
      PARAMETER\_ERROR = 401, // Parameter error.
    }
    
    // ...
    @Entry
    @Component
    struct Index {
      @State message: string = ''; // Display log messages.
      // ...
    
      build() {
        Column() { // Display logs output by Logger.
          // ...
          Text(this.message)
            .fontSize(16)
            .fontColor(Color.Black)
            .margin({ bottom: 10 })
            .id('test-message') // Set an ID for the test message to facilitate content obtaining.
    
          Button($r('app.string.GetDefaultNet'))
            .onClick(() => {
              this.GetDefaultNet();
            })
              // ...
    
          Button($r('app.string.CodeNumber'))
            .onClick(() => {
              this.CodeNumber();
            })
              // ...
        }.width('100%').height('100%').justifyContent(FlexAlign.Center);
      }
      
      GetDefaultNet() {
        let netId = testNetManager.NetId();
        // ...
          hilog.info(0x0000, 'testTag', 'The defaultNetId is \[' + netId + '\]');
          // ...
      }
    
      CodeNumber() {
        let testParam = 1;
        // ...
          let codeNumber = testNetManager.GetDefaultNet(testParam);
          switch (codeNumber) {
            case ReturnCode.SUCCESS:
              hilog.info(0x0000, 'testTag', 'Test success. \[' + codeNumber + '\]');
              // ...
              break;
            case ReturnCode.MISSING\_PERMISSION:
              hilog.info(0x0000, 'testTag', 'Missing permissions. \[' + codeNumber + '\]');
              // ...
              break;
            case ReturnCode.PARAMETER\_ERROR:
              hilog.info(0x0000, 'testTag', 'Parameter error. \[' + codeNumber + '\]');
              // ...
              break;
            default:
              hilog.info(0x0000, 'testTag', 'Unexpected result: \[' + codeNumber + '\]');
              // ...
              break;
          }
        // ...
      }
      // ...
    }
    
6.  Configure the CMakeLists.txt file. Add the required shared library, that is, libnet\_connection.so, to target\_link\_libraries in the CMakeLists.txt file automatically generated by the project.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d0/v3/0u9CDcodQUKlU2dlq_v3_w/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062016Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=2D56C1C0DE5E96DB1F189EB7BD3CB1F14ED90D4C49A90485123C2B474658BF94)
    
    As shown in the following figure, entry in add\_library is the modname automatically generated by the project. If you want to change its value, ensure that it is the same as the .nm\_modname in step 3.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/48/v3/Nc8C8lxeTOi_sxsF9sjGjQ/en-us_image_0000002568684811.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062016Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=CB97DAB49766E6318278AE14E7AD3D456A665CD43990DEFD3438E75950BE9874)
    

After the preceding steps, the entire project is set up. Then, you can connect to the device to run the project to view logs.

#### **Test Procedure**

1.  Connect the device and use DevEco Studio to open the project.
    
2.  Run the project. The following figure is displayed on the device.
    
    -   If you click GetDefaultNet, you'll obtain the default network ID.
    -   If you click codeNumber, you'll obtain the status code returned by the API.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bf/v3/N-Uv58V6R4mK9hA_7zvxMw/en-us_image_0000002568764821.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062016Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=542C72ABE7A07A256E09C2EF0EEDA5635D26D3B7F3F451F90A670270933C597E)
    
3.  Click GetDefaultNet. The following log is displayed, as shown below:
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e8/v3/xjesPsfBQWOQlMnfwcQISw/en-us_image_0000002537765096.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062016Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=6B711A78BF17FA180A668ACDFA4D3686977DB0798AAFF530B90D89CF08D2FB23)
    
4.  Click codeNumber. The status code is displayed, as shown below:
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/31/v3/L8KJDS-6QZ2aOgu46OOsOQ/en-us_image_0000002537925036.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062016Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=686562E5A502B1AF27CD8B6C9A67127702640D444FFD3D5D8C0C0596DDFD6F6C)
