# @ohos.net.vpnExtension (Enhanced VPN Management)

This module implements virtual private network (VPN) management, such as starting and stopping a third-party VPN. Third-party VPNs refer to VPN services provided by third parties. They usually support more security and privacy functions and more comprehensive customization options. Currently, the VPN capabilities provided to third-party applications are primarily used for creating virtual NICs and configuring VPN routing information. The connection tunnel process and internal connection protocols need to be implemented by the applications themselves.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2c/v3/-XS64VsUQUWBMACeqGajKA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062345Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=7D956EE651325A1D4A56841C86BF11684A57EC3503F726847BE63A899753637B)

The initial APIs of this module are supported since API version 11. Newly added APIs will be marked with a superscript to indicate their earliest API version.

The following modules cannot be referenced in the VpnExtensionAbility, as doing so may cause the program to exit abnormally:

-   [@ohos.contact (Contacts)](../../../../../application-services/contacts-kit/arkts-api/ohos-contact-contacts/document.md)
    
-   [@ohos.geolocation](../../../../../application-services/location-kit/arkts-apis/apis-no-longer-maintained/ohos-geolocation-geolocation/document.md), [@ohos.geoLocationManager (Geolocation Manager)](../../../../../application-services/location-kit/arkts-apis/ohos-geolocationmanager-geolocation-manager/document.md)
    
-   [@ohos.multimedia.audio (Audio Management)](../../../../../media/audio-kit/arkts-apis/ohos-multimedia-audio-audio-management/module-description/document.md)
    
-   [@ohos.multimedia.camera (Camera Management)](../../../../../media/camera-kit/arkts-apis/ohos-multimedia-camera-camera-management/module-description/document.md)
    
-   [@ohos.telephony.call (Call)](../../../telephony-kit/arkts-api/ohos-telephony-call-call/document.md)
    
-   [@ohos.telephony.sim (SIM Management)](../../../telephony-kit/arkts-api/ohos-telephony-sim-sim-management/document.md)
    
-   [@ohos.telephony.sms (SMS)](../../../telephony-kit/arkts-api/ohos-telephony-sms-sms/document.md)
    

#### Modules to Import

import { vpnExtension } from '@kit.NetworkKit';

#### LinkAddress

type LinkAddress = connection.LinkAddress

Defines the network link address information.

**System capability**: SystemCapability.Communication.NetManager.Core

| Type | Description |
| :-- | :-- |
| [connection.LinkAddress](../ohos-net-connection-network-connection-management/document.md#linkaddress) | Network link address information. |

#### RouteInfo

type RouteInfo = connection.RouteInfo

Defines the network route information.

**System capability**: SystemCapability.Communication.NetManager.Core

| Type | Description |
| :-- | :-- |
| [connection.RouteInfo](../ohos-net-connection-network-connection-management/document.md#routeinfo) | Network route information. |

#### VpnExtensionContext

type VpnExtensionContext = \_VpnExtensionContext

Defines the VPN extension context. It allows access to serviceExtension-specific resources.

**System capability**: SystemCapability.Ability.AbilityRuntime.Core.

| Type | Description |
| :-- | :-- |
| [\_VpnExtensionContext](../vpnextensioncontext/document.md) | VPN extension context. |

#### vpnExtension.startVpnExtensionAbility

startVpnExtensionAbility(want: Want): Promise<void>

Enables the VPN extension ability. This API uses a promise to return the result.

**System capability**: SystemCapability.Ability.AbilityRuntime.Core.

**Model restriction**: This API can be used only in the stage model.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| want | [Want](../../../../../application-framework/ability-kit/arkts-apis/both-models-recommended/ohos-app-ability-want-want/document.md) | Yes | 
Want information.

Note: From API version 22, the **parameters** field in **want** can be passed when the VPN is started for the first time.

 |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Error codes**

For details about the error codes, see [Ability Error Codes](../../../../../application-framework/ability-kit/error-codes/ability-error-codes/document.md) and [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | If the input parameter is not valid parameter. |
| 16000001 | The specified ability does not exist. |
| 16000002 | Incorrect ability type. |
| 16000006 | Cross-user operations are not allowed. |
| 16000008 | The crowdtesting application expires. |
| 16000011 | The context does not exist. |
| 16000050 | Internal error. |
| 16200001 | The caller has been released. |

**Example**

Stage model:

import { Want } from '@kit.AbilityKit';
import { vpnExtension } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let want: Want = {
  deviceId: "",
  bundleName: "com.example.myvpndemo",
  abilityName: "MyVpnExtAbility",
};

@Entry
@Component
struct Index {
  @State message: string = 'Hello World'

  build() {
    Row() {
      Column() {
        Text(this.message)
          .fontSize(40)
          .fontWeight(FontWeight.Bold).onClick(() => {
          console.info("btn click")
        })
        Button('Start Extension').onClick(() => {
          vpnExtension.startVpnExtensionAbility(want).then(() => {
            console.info('startVpnExtensionAbility success');
          }).catch((err: BusinessError) => {
            console.error('startVpnExtensionAbility error: ' + JSON.stringify(err));
          })
        }).width('70%').fontSize(30).margin(16)
      }.width('100%')
    }.height('100%')
  }
}

#### vpnExtension.stopVpnExtensionAbility

stopVpnExtensionAbility(want: Want): Promise<void>

Stops the VPN extension ability. This API uses a promise to return the result.

**System capability**: SystemCapability.Ability.AbilityRuntime.Core.

**Model restriction**: This API can be used only in the stage model.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| want | [Want](../../../../../application-framework/ability-kit/arkts-apis/both-models-recommended/ohos-app-ability-want-want/document.md) | Yes | Want information. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Error codes**

For details about the error codes, see [Ability Error Codes](../../../../../application-framework/ability-kit/error-codes/ability-error-codes/document.md) and [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | If the input parameter is not valid parameter. |
| 16000001 | The specified ability does not exist. |
| 16000002 | Incorrect ability type. |
| 16000006 | Cross-user operations are not allowed. |
| 16000011 | The context does not exist. |
| 16000050 | Internal error. |
| 16200001 | The caller has been released. |

**Example**

Stage model:

import { Want } from '@kit.AbilityKit';
import { vpnExtension } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let want: Want = {
  deviceId: "",
  bundleName: "com.example.myvpndemo",
  abilityName: "MyVpnExtAbility",
};

@Entry
@Component
struct Index {
  @State message: string = 'Hello World'

  build() {
    Row() {
      Column() {
        Text(this.message)
          .fontSize(50)
          .fontWeight(FontWeight.Bold).onClick(() => {
          console.info("btn click")
        })
        Button('Start Extension').onClick(() => {
          vpnExtension.startVpnExtensionAbility(want).then(() => {
            console.info('startVpnExtensionAbility success');
          }).catch((err: BusinessError) => {
            console.error('startVpnExtensionAbility error: ' + JSON.stringify(err));
          })
        }).width('70%').fontSize(30).margin(16)
        Button('Stop Extension').onClick(() => {
          console.info("btn end")
          vpnExtension.stopVpnExtensionAbility(want).then(() => {
            console.info('stopVpnExtensionAbility success');
          }).catch((err: BusinessError) => {
            console.error('stopVpnExtensionAbility error: ' + JSON.stringify(err));
          })
        }).width('70%').fontSize(30).margin(16)

      }.width('100%')
    }.height('100%')
  }
}

#### vpnExtension.createVpnConnection

createVpnConnection(context: VpnExtensionContext): VpnConnection

Creates a **VpnConnection** object.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a/v3/X3Rd57bqRPecx8lWshWUoA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062345Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=5787AC573A76B0B95065F3553DBC914D39D071D3B5C2FC880C6A1DD33B41ED69)

Before calling **createVpnConnection**, call **startVpnExtensionAbility** to enable the VPN function.

**System capability**: SystemCapability.Communication.NetManager.Vpn

**Model restriction**: This API can be used only in the stage model.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| context | [VpnExtensionContext](../vpnextensioncontext/document.md) | Yes | Specified context. |

**Return value**

| Type | Description |
| :-- | :-- |
| [VpnConnection](#vpnconnection) | VPN connection object. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. |

**Example**

Stage model:

import { vpnExtension, VpnExtensionAbility } from '@kit.NetworkKit';
import { common, Want } from '@kit.AbilityKit';

let context: vpnExtension.VpnExtensionContext;
export default class MyVpnExtAbility extends VpnExtensionAbility {
  onCreate(want: Want) {
    let vpnConnection : vpnExtension.VpnConnection = vpnExtension.createVpnConnection(context);
    console.info("VPN createVpnConnection: " + JSON.stringify(vpnConnection));
  }
}

#### VpnConnection

Defines a VPN connection object. Before calling **VpnConnection** APIs, you need to create a VPN connection object by calling **vpnExt.createVpnConnection**.

#### \[h2\]create

create(config: VpnConfig): Promise<number>

Creates a VPN based on the specified configuration. This API uses a promise to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6b/v3/gUPHZwnxTyaIrbgg-NqEeQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062345Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=051597F6A75C73E1688E5764C744E8C91BF031D0C5FAD59FF0DB1FEB32F590C1)

You are advised to call [destroy()](#destroy) or [destroy(vpnId: string)](#destroy20) to destroy the VPN and clear resources when the VPN is not needed.

**System capability**: SystemCapability.Communication.NetManager.Vpn

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| config | [VpnConfig](#vpnconfig) | Yes | VPN configuration. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<number> | Promise used to return the result, which is the file descriptor of the virtual network interface card (vNIC). |

**Error codes**

For details about the error codes, see [VPN Error Codes](../../error-codes/vpn-error-codes/document.md) and [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. |
| 2200001 | Invalid parameter value. |
| 2200002 | Operation failed. Cannot connect to service. |
| 2200003 | System internal error. |
| 2203001 | VPN creation denied, please check the user type. |
| 2203002 | VPN exist already, please execute destroy first. |

**Example**

import { vpnExtension, VpnExtensionAbility } from '@kit.NetworkKit';
import { common, Want } from '@kit.AbilityKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

let context: vpnExtension.VpnExtensionContext;
export default class MyVpnExtAbility extends VpnExtensionAbility {
  private tunIp: string = '10.0.0.5';
  private blockedAppName: string = 'com.example.myvpndemo';
  onCreate(want: Want) {
    let vpnConnection : vpnExtension.VpnConnection = vpnExtension.createVpnConnection(context);
    console.info("vpn createVpnConnection: " + JSON.stringify(vpnConnection));
    this.SetupVpn();
    
    // If no VPN is required, call destroy() to destroy the VPN and clear resources.
    vpnConnection.destroy().then(() => {
      console.info("destroy success.");
    }).catch((error : BusinessError) => {
      console.error(\`destroy fail. Code:${error.code}, message:${error.message}\`);
    });
  }
  SetupVpn() {
        class Address {
            address: string;
            family: number;

            constructor(address: string, family: number) {
                this.address = address;
                this.family = family;
            }
        }

        class AddressWithPrefix {
            address: Address;
            prefixLength: number;

            constructor(address: Address, prefixLength: number) {
                this.address = address;
                this.prefixLength = prefixLength;
            }
        }

        class Config {
            addresses: AddressWithPrefix\[\];
            mtu: number;
            dnsAddresses: string\[\];
            trustedApplications: string\[\];
            blockedApplications: string\[\];

            constructor(
                tunIp: string,
                blockedAppName: string
            ) {
                this.addresses = \[
                    new AddressWithPrefix(new Address(tunIp, 1), 24)
                \];
                this.mtu = 1400;
                this.dnsAddresses = \["114.114.114.114"\];
                this.trustedApplications = \[\];
                this.blockedApplications = \[blockedAppName\];
            }
        }

        let config = new Config(this.tunIp, this.blockedAppName);

        try {
            let vpnConnection : vpnExtension.VpnConnection = vpnExtension.createVpnConnection(context);
            vpnConnection.create(config).then((data) => {
                hilog.error(0x0000, 'developTag', 'tunfd: %{public}s', JSON.stringify(data) ?? '');
            })
        } catch (error) {
            hilog.error(0x0000, 'developTag', 'VPN setUp fail: %{public}s', JSON.stringify(error) ?? '');
        }
    }
}

#### \[h2\]protect

protect(socketFd: number): Promise<void>

Protects sockets against a VPN connection. The data sent through sockets is directly transmitted over the physical network and therefore the traffic does not traverse through the VPN. This API uses a promise to return the result.

**System capability**: SystemCapability.Communication.NetManager.Vpn

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| socketFd | number | Yes | Socket file descriptor. It can be obtained through [getSocketFd](../ohos-net-socket-socket-connection/document.md#getsocketfd10-1). |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Error codes**

For details about the error codes, see [VPN Error Codes](../../error-codes/vpn-error-codes/document.md) and [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. |
| 2200001 | Invalid parameter value. |
| 2200002 | Operation failed. Cannot connect to service. |
| 2200003 | System internal error. |
| 2203004 | Invalid socket file descriptor. |

**Example**

import { vpnExtension, VpnExtensionAbility } from '@kit.NetworkKit';
import { common, Want } from '@kit.AbilityKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

let g\_tunnelFd = -1;
let context: vpnExtension.VpnExtensionContext;
export default class MyVpnExtAbility extends VpnExtensionAbility {
  private vpnServerIp: string = '192.168.31.13';
  onCreate(want: Want) {
    let vpnConnection : vpnExtension.VpnConnection = vpnExtension.createVpnConnection(context);
    console.info("VPN createVpnConnection: " + JSON.stringify(vpnConnection));
    this.CreateTunnel();
    this.Protect();
  }
  CreateTunnel() {
      g\_tunnelFd = 8888;
  }
  Protect() {
        hilog.info(0x0000, 'developTag', '%{public}s', 'VPN Protect');
        let vpnConnection : vpnExtension.VpnConnection = vpnExtension.createVpnConnection(context);
        vpnConnection.protect(g\_tunnelFd).then(() => {
            hilog.info(0x0000, 'developTag', '%{public}s', 'VPN Protect Success');
        }).catch((err : Error) => {
            hilog.error(0x0000, 'developTag', 'VPN Protect Failed %{public}s', JSON.stringify(err) ?? '');
        })
  }
}

#### \[h2\]destroy

destroy(): Promise<void>

Destroys a VPN. This API uses a promise to return the result.

**System capability**: SystemCapability.Communication.NetManager.Vpn

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Error codes**

For details about the error codes, see [VPN Error Codes](../../error-codes/vpn-error-codes/document.md) and [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. |
| 2200002 | Operation failed. Cannot connect to service. |
| 2200003 | System internal error. |

**Example**

import { vpnExtension, VpnExtensionAbility } from '@kit.NetworkKit';
import { common, Want } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

let context: vpnExtension.VpnExtensionContext;
export default class MyVpnExtAbility extends VpnExtensionAbility {
  onCreate(want: Want) {
    let vpnConnection : vpnExtension.VpnConnection = vpnExtension.createVpnConnection(context);
    console.info("VPN createVpnConnection: " + JSON.stringify(vpnConnection));
    vpnConnection.destroy().then(() => {
      console.info("destroy success.");
    }).catch((error : BusinessError) => {
      console.error("destroy fail" + JSON.stringify(error));
    });
  }
}

#### \[h2\]destroy20+

destroy(vpnId: string): Promise<void>

Destroys a VPN based on the specified VPN ID. This API uses a promise to return the result.

**System capability**: SystemCapability.Communication.NetManager.Vpn

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| vpnId | string | Yes | Unique VPN ID. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Error codes**

For details about the error codes, see [VPN Error Codes](../../error-codes/vpn-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 19900001 | Invalid parameter value. |
| 19900002 | System internal error. |

**Example**

import { vpnExtension, VpnExtensionAbility } from '@kit.NetworkKit';
import { BusinessError } from "@kit.BasicServicesKit";

export default class MyVpnExtAbility extends VpnExtensionAbility {
  onCreate() {
    let vpnConnection = vpnExtension.createVpnConnection(this.context);

    // You can call generateVpnId() to obtain the VPN ID.
    let vpnId = 'testVpnId';
    vpnConnection.destroy(vpnId).then(() => {
      console.info("destroy success");
    }).catch((error: BusinessError) => {
      console.error(\`destroy fail, Code is ${error.code}, message is ${error.message}\`);
    });
  }
}

#### \[h2\]generateVpnId20+

generateVpnId(): Promise<string>

Generates a unique VPN ID. This API uses a promise to return the result.

To use the multi-VPN capability of the system, you need to call this API to generate a VPN ID and configure it in **VpnConfig**.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/25/v3/egNYkie-SJCE2-gMqr3RYQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062345Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=00FC1D4B0E06B15FB243FC784BFFEF817BA2B38F6CF3E3B742CB718395B31FC1)

Currently, the multi-VPN capability of the system supports only IPv4.

**System capability**: SystemCapability.Communication.NetManager.Vpn

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<string> | Promise used to return the result. |

**Error codes**

For details about the error codes, see [VPN Error Codes](../../error-codes/vpn-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 19900001 | Invalid parameter value. |
| 19900002 | System internal error. |

**Example**

import { vpnExtension, VpnExtensionAbility } from '@kit.NetworkKit';
import { BusinessError } from "@kit.BasicServicesKit";

export default class MyVpnExtAbility extends VpnExtensionAbility {
  onCreate() {
    let vpnConnection = vpnExtension.createVpnConnection(this.context);
    vpnConnection.generateVpnId().then((data) => {
      if (data) {
        console.info("generateVpnId success, vpnId = " + JSON.stringify(data));
      }
    }).catch((error: BusinessError) => {
      console.error(\`generateVpnId fail, Code is ${error.code}, message is ${error.message}\`);
    });
  }
}

#### \[h2\]protectProcessNet22+

protectProcessNet(): Promise<void>

Protects application processes against a VPN connection. The data sent through the protected processes is transmitted over the physical network without traversing the VPN. This API uses a promise to return the result.

**System capability**: SystemCapability.Communication.NetManager.Vpn

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Example**

import { vpnExtension, VpnExtensionAbility } from '@kit.NetworkKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

let g\_tunnelFd = -1;
export default class MyVpnExtAbility  extends VpnExtensionAbility {
  onCreate() {
    let vpnConnection = vpnExtension.createVpnConnection(this.context);
    console.info("VPN createVpnConnection: " + JSON.stringify(vpnConnection));
    this.ProtectNetByProcess();
  }
  CreateTunnel() {
    g\_tunnelFd = 8888;
  }
  ProtectNetByProcess() {
    hilog.info(0x0000, 'developTag', '%{public}s', 'vpn ProtectNetByProcess');
    let vpnConnection = vpnExtension.createVpnConnection(this.context);
    vpnConnection.protectProcessNet().then(() => {
      hilog.info(0x0000, 'developTag', '%{public}s', 'vpn ProtectNetByProcess Success');
      this.CreateTunnel();
    }).catch((err: Error) => {
      hilog.error(0x0000, 'developTag', 'vpn ProtectNetByProcess Failed %{public}s', JSON.stringify(err) ?? '');
    })
  }
}

#### VpnConfig

Defines the VPN configuration.

**System capability**: SystemCapability.Communication.NetManager.Vpn

| Name | Type | Read-only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| addresses | Array<[LinkAddress](../ohos-net-connection-network-connection-management/document.md#linkaddress)\> | No | No | IP addresses of vNICs. Before API version 23, a maximum of 64 IP addresses are supported. Starting from API version 23, a maximum of 2000 IP addresses are supported. |
| vpnId20+ | string | No | Yes | Unique VPN ID. |
| routes | Array<[RouteInfo](../ohos-net-connection-network-connection-management/document.md#routeinfo)\> | No | Yes | Routes of vNICs. Currently, a maximum of 1024 routes can be configured. |
| dnsAddresses | Array<string> | No | Yes | IP address of the DNS server. After the IP address is configured, when the VPN is active and proxy-enabled applications access the Internet, the configured DNS server will be used for DNS queries. |
| searchDomains | Array<string> | No | Yes | List of DNS search domains. |
| mtu | number | No | Yes | Maximum transmission unit (MTU), in bytes. The value range is \[576,1500\]. |
| isIPv4Accepted | boolean | No | Yes | 
Whether IPv4 is supported. The value **true** indicates that the IPv4 is supported, and the value **false** indicates the opposite. The default value is **true**.

Note: If the IPv4 is supported, you need to configure IPv4 addresses in **addresses**.

 |
| isIPv6Accepted | boolean | No | Yes | 

Whether IPv6 is supported. The value **true** indicates that the IPV6 is supported, and the value **false** indicates the opposite. The default value is **false**.

Note: If the IPv6 is supported, you need to configure IPv6 addresses in **addresses**.

 |
| isInternal | boolean | No | Yes | Whether the built-in VPN is supported. The value **true** indicates that the built-in VPN is supported, and the value **false** indicates the opposite. The default value is **false**. |
| isBlocking | boolean | No | Yes | Whether the blocking mode is used. The value **true** indicates that the blocking mode is used, and the value **false** indicates the opposite. The default value is **false**. |
| trustedApplications | Array<string> | No | Yes | 

List of trusted applications, which are represented by package names of the string type. After such a list is configured, only the applications in the list can be proxied by the VPN according to the specified **routes**.

**Note**: Configure either **trustedApplications** or **blockedApplications** as they are mutually exclusive.

 |
| blockedApplications | Array<string> | No | Yes | 

List of blocked applications, which are represented by package names of the string type. After such a list is configured, only applications that are not in the list can be proxied by the VPN according to the specified **routes**.

**Note**: Configure either **trustedApplications** or **blockedApplications** as they are mutually exclusive.

 |

**Example**

import { vpnExtension} from '@kit.NetworkKit';

let vpnConfig: vpnExtension.VpnConfig = {
  addresses: \[\],
  vpnId: '123',
  routes: \[{
    interface: "eth0",
    destination: {
      address: {
        address:'',
        family:1,
        port:8080
      },
      prefixLength:1
    },
    gateway: {
      address:'',
      family:1,
      port:8080
    },
    hasGateway: true,
    isDefaultRoute: true,
  }\],
  mtu: 1400,
  dnsAddresses: \["223.5.5.5", "223.6.6.6"\],
  trustedApplications: \[\],
  blockedApplications: \[\],
}
let context: vpnExtension.VpnExtensionContext;

function vpnCreate(){
  let vpnConnection: vpnExtension.VpnConnection = vpnExtension.createVpnConnection(context);
  vpnConnection.create(vpnConfig).then((data) => {
    console.info("VPN create " + JSON.stringify(data));
  })
}
