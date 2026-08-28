# Network Connection Management

#### Introduction

The Network Connection Management module provides basic network management capabilities, including management of Wi-Fi/cellular/Ethernet connection priorities, network quality evaluation, subscription to network connection status changes, query of network connection information, and DNS resolution.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3b/v3/QbmIZwyOSm6djHYAkZwdVg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062016Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=70BA1C9C434F1FD3B4C2B5E6598E3F081A5F016A3F4565B64BA0BF55F7F68627)

To maximize the application running efficiency, most API calls are called asynchronously in callback or promise mode. The following code examples use the promise mode. For details about the APIs, see [API Reference](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-net-connection).

#### Basic Concepts

-   Producer: a provider of data networks, such as Wi-Fi, cellular, and Ethernet.
-   Consumer: a user of data networks, for example, an application or a system service.
-   Network probe: a mechanism used to detect the network availability to prevent the switch from an available network to an unavailable network. The probe type can be binding network detection, DNS detection, HTTP detection, or HTTPS detection.
-   Network selection: a mechanism used to select the optimal network when multiple networks coexist. It is triggered when the network status, network information, or network quality evaluation score changes.
-   Default network: the network used by the system by default, which is determined by the system and is irrelevant to whether the application specifies a network. Generally, the network is Wi-Fi, cellular, Ethernet, or Bluetooth.
-   Network handle: unique identifier of the network.

#### When to Use

Typical application scenarios of network connection management are as follows:

-   Subscribing to status changes of the specified network
-   Obtaining the list of all registered networks
-   Querying the connection information of the default network or the specified network
-   Resolving the domain name of the default network to obtain all IP addresses

The following describes the development procedure specific to each application scenario.

#### Subscribing to Status Changes of the Specified Network

1.  Declare the required permission: **ohos.permission.GET\_NETWORK\_INFO**.
    
    This permission is of the **normal** level. Before applying for the permission, ensure that the [basic principles for permission management](../../../../security/application-access-control/application-permission-management/application-permission-management-overview/document.md#basic-principles-for-using-permissions) are met. Declare the permissions required by your application. For details, see [Declaring Permissions in the Configuration File](../../../../security/application-access-control/application-permission-management/requesting-application-permissions/declaring-permissions/document.md#declaring-permissions-in-the-configuration-file).
    
2.  Import the **connection** namespace from **@kit.NetworkKit**.
    
    // Import the required namespaces.
    import { connection } from '@kit.NetworkKit';
    import { BusinessError } from '@kit.BasicServicesKit';
    import { hilog } from '@kit.PerformanceAnalysisKit';
    
3.  Call [createNetConnection](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-net-connection#connectioncreatenetconnection) to create a **NetConnection** object. You can specify the network type, capability, and timeout interval. If you do not specify parameters, the default values will be used.
    
    let netSpecifier: connection.NetSpecifier = {
      netCapabilities: {
        // Assume that the default network is a cellular network connection. If you need to create a Wi-Fi network connection, set the network type to Wi-Fi.
        bearerTypes: \[connection.NetBearType.BEARER\_WIFI\],
        // Set the network capability to INTERNET.
        networkCap: \[connection.NetCap.NET\_CAPABILITY\_INTERNET\],
      }
    };
    
    // Set the timeout value to 10s. The default value is 0.
    let TIMEOUT = 10 \* NETWORK\_CONNECTION\_TIMEOUT;
    
    // Create a NetConnection object.
    let conn = connection.createNetConnection(netSpecifier, TIMEOUT);
    
4.  Call [on()](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-net-connection#onnetavailable) to subscribe to desired events. You must pass in **type** and **callback**.
    
    // Subscribe to network status change events. If the network is available, an on\_netAvailable event is returned.
    conn.on('netAvailable', (data: connection.NetHandle) => {
      hilog.info(0x0000, 'testTag', 'Network available, NetId is ' + data.netId);
      // ...
    });
      
    // Subscribe to network status change events. If the network is unavailable, an on\_netUnavailable event is returned.
    conn.on('netUnavailable', (data: void) => {
      hilog.info(0x0000, 'testTag', 'Network unavailable, data is ' + JSON.stringify(data));
      // ...
    });
    // Subscribe to network capability change events. If the capability of the specified network changes, an on\_netCapabilitiesChange event is returned.
    conn.on('netCapabilitiesChange', (data: connection.NetCapabilityInfo) => {
      hilog.info(0x0000, 'testTag', 'Network netCapabilitiesChange, data is ' + JSON.stringify(data));
      // ...
    });
      
    // Subscribe to network connection information change events. If the connection information of the specified network changes, an on\_netConnectionPropertiesChange event is returned.
    conn.on('netConnectionPropertiesChange', (data: connection.NetConnectionPropertyInfo) => {
      hilog.info(0x0000, 'testTag', 'Network netConnectionPropertiesChange, data is ' + JSON.stringify(data));
      // ...
    });
      
    // Subscribe to network disconnection events. If the specified network is disconnected, an on\_netLost event is returned.
    conn.on('netLost', (data: connection.NetHandle) => {
      hilog.info(0x0000, 'testTag', 'Network netLost, data is ' + JSON.stringify(data));
      // ...
    });
    
5.  Call [register()](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-net-connection#register) to subscribe to network status changes of the specified network. When the network is available, the **netAvailable** event is triggered. When the network is disconnected, the **netLost** event is triggered. When the network connection information changes (for example, IPv6 addresses are added to linkAddresses), the **netConnectionPropertiesChange** event is triggered. When the network capability changes (for example, the network connectivity changes), the **netCapabilitiesChange** event is triggered.
    
    // Subscribe to connection state changes.
    conn.register((err: BusinessError, data: void) => {
      // ...
        hilog.error(0x0000, 'testTag', 'Error occurred during connection:', JSON.stringify(err));
        // ...
    });
    
6.  Call [unregister()](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-net-connection#unregister) to unsubscribe from the network status changes.
    
    // Unregister the observer for network status changes.
    conn.unregister((err: BusinessError, data: void) => {
      if (err) {
        hilog.error(0x0000, 'testTag', 'Error occurred during unsubscription:', JSON.stringify(err));
      } else {
        // ...
        hilog.info(0x0000, 'testTag', 'Network connection disconnected.');
      }
    });
    

#### Monitoring Changes of the Default Network and Re-establishing the Network Connection

Depending on the current network status and network quality, the default network may change, for example:

1.  Switching the default network to the cellular network when the Wi-Fi signal is weak
2.  Switching the default network to the Wi-Fi network when the cellular network signal is weak
3.  Switching the default network to the cellular network when the Wi-Fi network is disabled
4.  Switching the default network to the Wi-Fi network when the cellular network is disabled
5.  Switching the default network to another Wi-Fi network when the Wi-Fi signal is weak (cross-network scenario)
6.  Switching the default network to cellular Wi-Fi network when the cellular signal is weak (cross-network scenario)

The following describes how to monitor changes of the default network and migrate application packets to the new default network.

## Importing the Connection Namespace

import { connection, socket } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

## Monitoring Changes of the Default Network

const netConnection = connection.createNetConnection();
/\* Listen for changes of the default network \*/
netConnection.on('netAvailable', (data: connection.NetHandle) => {
  hilog.info(0x0000, 'testTag', JSON.stringify(data));
});

## Re-establishing the Network Connection When the Default Network Is Changed

**Original Network Connection Established via the HTTP Module**

If the original network connection is established through the HTTP module, the socket is not closed immediately after the default network is changed and a new network connection is set up. The reason is that the HTTP module does not provide the **Close** API for closing a socket. Therefore, use Remote Communication Kit to re-establish a network connection.

**Original Network Connection Established via Remote Communication Kit**

import { rcp } from '@kit.RemoteCommunicationKit';
import { connection } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let session = rcp.createSession();

async function useRcp() {
  // Create an RCP request. //
  try {
    const request = await session.get('https://www.example.com');
    console.info(request.statusCode.toString());
  } catch (e) {
    console.error(e.code.toString());
  }
}

async function rcpTest() {
  const netConnection = connection.createNetConnection();
  netConnection.on('netAvailable', async (netHandle: connection.NetHandle) => {
    // Re-establish a session when the default network is changed.
    session.close();
    session = rcp.createSession();
    useRcp();
  });
  try {
    netConnection.register(() => {
    });
    useRcp();
  } catch (e) {
    console.error(e.code.toString());
  }
}

**Original Network Connection Established via the Socket Module**

// Create a socket object.
let sock: socket.TCPSocket = socket.constructTCPSocketInstance();

// Original network connection established via the Socket module.
function useSocket() {
  let netAddress: socket.NetAddress = {
    address: '192.168.xx.xxx',
    port: 8080 // Port number. The default value is 8080.
  };

  let tcpConnectOptions: socket.TCPConnectOptions = {
    address: netAddress,
    timeout: 6000 // Connection timeout duration.
  };

  // Set up a socket connection.
  sock.connect(tcpConnectOptions, (err: BusinessError) => {
    if (err) {
      hilog.error(0x0000, 'testTag', 'connect fail: '+JSON.stringify(err));
    // ···
      return;
    }
    hilog.info(0x0000, 'testTag', 'connect success');

    // Send data over the socket.
    let tcpSendOptions: socket.TCPSendOptions = {
      data: 'Hello, server!'
    };
    socketSend(tcpSendOptions);
  });
}

// Send data over the socket.
function socketSend(tcpSendOptions: socket.TCPSendOptions) {
  sock.send(tcpSendOptions).then(() => {
    hilog.info(0x0000, 'testTag', 'send success');
    // ···
  }).catch((err: BusinessError) => {
    hilog.error(0x0000, 'testTag', 'send fail');
    // ···
  });
}

function socketTest() {
  const netConnection = connection.createNetConnection();
  // The original socket becomes invalid if the network is disconnected due to network switching. In this case, you need to create a new socket.
  netConnection.on('netAvailable', (netHandle: connection.NetHandle) => {
    hilog.info(0x0000, 'testTag', 'default network changed: ' + JSON.stringify(netHandle));
    sock.close();
    sock = socket.constructTCPSocketInstance();
    // Send data over the socket.
    useSocket();
  });
// ···
    // Register an observer for network status changes.
    netConnection.register((error: BusinessError) => {
      if (error) {
        hilog.error(0x0000, 'testTag', 'register fail: ' + JSON.stringify(error));
      } else {
        hilog.info(0x0000, 'testTag', 'register success');
      }
    });
    // ···
}

**Original Network Connection Established via Socket Library**

Close the original socket and re-establish a socket connection when the default network is changed.

#### Obtaining the List of All Registered Networks

1.  Declare the required permission: **ohos.permission.GET\_NETWORK\_INFO**.
    
    This permission is of the **normal** level. Before applying for the permission, ensure that the [basic principles for permission management](../../../../security/application-access-control/application-permission-management/application-permission-management-overview/document.md#basic-principles-for-using-permissions) are met. Declare the permissions required by your application. For details, see [Declaring Permissions in the Configuration File](../../../../security/application-access-control/application-permission-management/requesting-application-permissions/declaring-permissions/document.md#declaring-permissions-in-the-configuration-file).
    
2.  Obtain the list of all connected networks.
    
    // Import the connection namespace from @kit.NetworkKit.
    import { connection } from '@kit.NetworkKit';
    import { hilog } from '@kit.PerformanceAnalysisKit';
    // ...
        // Call getAllNets to obtain the list of all connected networks via Array<NetHandle>.
        connection.getAllNets().then((data: connection.NetHandle\[\]) => {
          hilog.info(0x0000, 'testTag', 'getAllNets get data: ' + JSON.stringify(data));
          if (data) {
            // ...
            GlobalContext.getContext().netList = data;
            // ...
          }
        });
    

#### Querying the Connection Information of the Default Network or the Specified Network

1.  Declare the required permission: **ohos.permission.GET\_NETWORK\_INFO**.
    
    This permission is of the **normal** level. Before applying for the permission, ensure that the [basic principles for permission management](../../../../security/application-access-control/application-permission-management/application-permission-management-overview/document.md#basic-principles-for-using-permissions) are met. Declare the permissions required by your application. For details, see [Declaring Permissions in the Configuration File](../../../../security/application-access-control/application-permission-management/requesting-application-permissions/declaring-permissions/document.md#declaring-permissions-in-the-configuration-file).
    
2.  Query the connection information of the default network or the specified network.
    
    Call [getDefaultNet](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-net-connection#connectiongetdefaultnet) to obtain the default data network identified by **NetHandle** and call [getNetCapabilities](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-net-connection#connectiongetnetcapabilities) to obtain its network capability information. The capability information includes information such as the network type (cellular, Wi-Fi, or Ethernet network) and the specific network capabilities. Alternatively, you can call [getConnectionProperties](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-net-connection#connectiongetconnectionproperties) to obtain the connection information of the data network specified by **NetHandle**.
    
    // Import the connection namespace from @kit.NetworkKit.
    import { connection } from '@kit.NetworkKit';
    import { hilog } from '@kit.PerformanceAnalysisKit';
    // ···
        let netHandleInfo:connection.NetHandle|null = null;
        // Call \*\*getDefaultNet\*\* to obtain the default data network specified by \*\*NetHandle\*\*.
        connection.getDefaultNet().then((data: connection.NetHandle) => {
          if (data.netId == 0) {
            hilog.info(0x0000, 'testTag', \`don't have defaultNet\`);
            // If the obtained netid of netHandler is 0 when no default network is specified, an exception has occurred and extra processing is needed.
            return;
          }
          if (data) {
            // ···
            hilog.info(0x0000, 'testTag', 'getDefaultNet get data: ' + JSON.stringify(data));
            // Obtain the network capability information of the data network specified by \*\*NetHandle\*\*. The capability information includes information such as the network type and specific network capabilities.
            netHandleInfo = data;
            connection.getNetCapabilities(netHandleInfo).then(
              (data: connection.NetCapabilities) => {
                hilog.info(0x0000, 'testTag', 'getNetCapabilities get data: ' + JSON.stringify(data));
                // Obtain the network type via bearerTypes.
                let bearerTypes: Set<number> = new Set(data.bearerTypes);
                let bearerTypesNum = Array.from(bearerTypes.values());
                for (let item of bearerTypesNum) {
                  if (item == 0) {
                    // Cellular network
                    hilog.info(0x0000, 'testTag', JSON.stringify('BEARER\_CELLULAR'));
                  } else if (item == 1) {
                    // Wi-Fi network
                    hilog.info(0x0000, 'testTag', JSON.stringify('BEARER\_WIFI'));
                  } else if (item == 3) {
                    // Ethernet network
                    hilog.info(0x0000, 'testTag', JSON.stringify('BEARER\_ETHERNET'));
                  }
                }
    
                // Obtain the specific network capabilities via networkCap.
                let itemNumber: Set<number> = new Set(data.networkCap);
                let dataNumber = Array.from(itemNumber.values());
                for (let item of dataNumber) {
                  if (item == 0) {
                    // The network can connect to the carrier's Multimedia Messaging Service Center (MMSC) to send and receive multimedia messages.
                    hilog.info(0x0000, 'testTag', JSON.stringify('NET\_CAPABILITY\_MMS'));
                  } else if (item == 11) {
                    // The network traffic is not metered.
                    hilog.info(0x0000, 'testTag', JSON.stringify('NET\_CAPABILITY\_NOT\_METERED'));
                  } else if (item == 12) {
                    // The network has the Internet access capability, which is set by the network provider.
                    hilog.info(0x0000, 'testTag', JSON.stringify('NET\_CAPABILITY\_INTERNET'));
                  } else if (item == 15) {
                    // The network does not use a Virtual Private Network (VPN).
                    hilog.info(0x0000, 'testTag', JSON.stringify('NET\_CAPABILITY\_NOT\_VPN'));
                  } else if (item == 16) {
                    // The Internet access capability of the network is successfully verified by the connection management module.
                    hilog.info(0x0000, 'testTag', JSON.stringify('NET\_CAPABILITY\_VALIDATED'));
                  }
                }
              });
          }
        });
    
        // Obtain network connection information based on the specified netHandle.
        connection.getConnectionProperties(netHandleInfo).then((data: connection.ConnectionProperties) => {
          hilog.info(0x0000, 'testTag', 'getConnectionProperties get data: ' + JSON.stringify(data));
        })
    // ···
    
3.  Query the connection information of all connected networks.
    
    Call [getAllNets](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-net-connection#connectiongetallnets) to obtain the list of all connected networks specified by **Array<NetHandle>**. Then, traverse the obtained **NetHandle** array and call [getNetCapabilities](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-net-connection#connectiongetnetcapabilities) to obtain the capability information of the network identified by each **NetHandle**. The capability information includes the network type (cellular network, Wi-Fi network, or Ethernet network) and network capability. Alternatively, you can call [getConnectionProperties](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-net-connection#connectiongetconnectionproperties) to obtain the connection information of the data network specified by **NetHandle**.
    
    // Import the connection namespace from @kit.NetworkKit.
    import { connection } from '@kit.NetworkKit';
    import { hilog } from '@kit.PerformanceAnalysisKit';
    // ...
      getAllNetworks() {
        // Call getAllNets to obtain the list of all connected networks specified by Array<NetHandle>.
        connection.getAllNets().then((data: connection.NetHandle\[\]) => {
          hilog.info(0x0000, 'testTag', 'getAllNets get data: ' + JSON.stringify(data));
          if (data) {
            // ...
            let itemNumber: Set<connection.NetHandle> = new Set(data);
            let dataNumber = Array.from(itemNumber.values());
            for (let item of dataNumber) {
              // Obtain the network capability information of the network specified by each netHandle on the network list cyclically.
              connection.getNetCapabilities(item).then((data: connection.NetCapabilities) => {
                hilog.info(0x0000, 'testTag', 'getNetCapabilities get data: ' + JSON.stringify(data));
              });
    
              // Obtain the connection information of the network specified by each netHandle on the network list cyclically.
              connection.getConnectionProperties(item).then((data: connection.ConnectionProperties) => {
                hilog.info(0x0000, 'testTag', 'getConnectionProperties get data: ' + JSON.stringify(data));
              });
            }
          }
        });
      }
    

#### Checking Whether the Default Network Supports Internet Access

If an application needs to check whether the current network supports Internet access, perform the following steps:

1.  Declare the required permission: **ohos.permission.GET\_NETWORK\_INFO**.
    
    This permission is of the **normal** level. Before applying for the permission, ensure that the [basic principles for permission management](../../../../security/application-access-control/application-permission-management/application-permission-management-overview/document.md#basic-principles-for-using-permissions) are met. Declare the permissions required by your application. For details, see [Declaring Permissions in the Configuration File](../../../../security/application-access-control/application-permission-management/requesting-application-permissions/declaring-permissions/document.md#declaring-permissions-in-the-configuration-file).
    
2.  Check whether the default network supports Internet access.
    
    Call [getDefaultNetSync](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-net-connection#connectiongetdefaultnetsync9) to obtain **netHandle** of the default network. If **netHandle** is valid, call [getNetCapabilitiesSync](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-net-connection#connectiongetnetcapabilitiessync10) to obtain the capability information of the corresponding network via **networkCap** and determine whether Internet access is supported.
    
    **NET\_CAPABILITY\_CHECKING\_CONNECTIVITY** indicates that a network connectivity check is in progress. The network connectivity verification is successful if the network connectivity check is complete and **NET\_CAPABILITY\_VALIDATED** is contained in **networkCap**.
    
    // Import the connection namespace from @kit.NetworkKit.
    import { connection } from '@kit.NetworkKit';
    import { hilog } from '@kit.PerformanceAnalysisKit';
    // ...
        // Obtain the default active data network.
        let netHandle = connection.getDefaultNetSync();
        if (!netHandle || netHandle.netId === 0) {
          hilog.error(0x0000, 'testTag', 'getDefaultNetSync fail');
          // ...
        } else {
          hilog.info(0x0000, 'testTag', 'default network: ' + JSON.stringify(netHandle));
          // Obtain network capability information based on the specified netHandle.
          let netCapabilities = connection.getNetCapabilitiesSync(netHandle);
          let cap = netCapabilities.networkCap;
          hilog.info(0x0000, 'testTag', 'network capabilities: ' + JSON.stringify(netCapabilities));
          // Check whether the network supports Internet access.
          if (cap?.includes(connection.NetCap.NET\_CAPABILITY\_CHECKING\_CONNECTIVITY)) {
            // Network connectivity check is in progress. Please try again later.
            hilog.info(0x0000, 'testTag', 'default network is checking, please try again later');
          } else {
            if (cap?.includes(connection.NetCap.NET\_CAPABILITY\_VALIDATED)) {
              // Network connectivity check is successful. The default network supports Internet access.
              hilog.info(0x0000, 'testTag', 'default network is validated');
              // ...
            } else {
              // Network connectivity check fails. The default network does not support Internet access.
              hilog.info(0x0000, 'testTag', 'default network is not validated');
              // ...
            }
          }
        }
    

#### Resolving the Domain Name of the Default Network to Obtain All IP Addresses

1.  Declare the required permission: **ohos.permission.GET\_NETWORK\_INFO**.
    
    This permission is of the **normal** level. Before applying for the permission, ensure that the [basic principles for permission management](../../../../security/application-access-control/application-permission-management/application-permission-management-overview/document.md#basic-principles-for-using-permissions) are met. Declare the permissions required by your application. For details, see [Declaring Permissions in the Configuration File](../../../../security/application-access-control/application-permission-management/requesting-application-permissions/declaring-permissions/document.md#declaring-permissions-in-the-configuration-file).
    
2.  Use the default network to resolve the host name to obtain the list of all IP addresses.
    
    Call [getAddressesByName](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-net-connection#connectiongetaddressesbyname) to use the default network to resolve the host name to obtain the list of all IP addresses.
    
    // Import the connection namespace from @kit.NetworkKit.
    import { connection } from '@kit.NetworkKit';
    import { BusinessError } from '@kit.BasicServicesKit';
    import { hilog } from '@kit.PerformanceAnalysisKit';
    // ...
          // Use the default network to resolve the host name to obtain the list of all IP addresses.
          connection.getAddressesByName('xxxx').then((data: connection.NetAddress\[\]) => {
            hilog.info(0x0000, 'testTag', 'Successfully retrieved default network IP address: ' + JSON.stringify(data));
            // ...
          })
