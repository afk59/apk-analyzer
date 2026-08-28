# Collecting Network Statistics

#### Introduction

The traffic management module allows you to query real-time or historical data traffic by the specified network interface card (NIC) or user ID (UID).

Its functions include:

-   Obtaining real-time traffic data by NIC or UID
-   Obtaining historical traffic data by NIC or UID
-   Subscribing to traffic change events by NIC or UID

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/63/v3/lfVX17DGToGdZOCo1GN8bg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062016Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=2842011399D3C6C8A3C5A9256DD90869B1BA4CD469F69679EDC15CB8FB51D2A6)

To maximize the application running efficiency, most API calls are called asynchronously in callback or promise mode. The following code examples use the promise mode. For details about the APIs, see [API Reference](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-net-statistics).

The following describes the development procedure specific to each application scenario.

#### How to Develop

1.  Import the **statistics**, **socket**, and **BusinessError** modules.
    
    import { socket, statistics } from '@kit.NetworkKit';
    import { BusinessError } from '@kit.BasicServicesKit';
    import { hilog } from '@kit.PerformanceAnalysisKit';
    
2.  Obtain the real-time data traffic of the specified NIC.
    
    Call **getIfaceRxBytes** with the NIC name specified to obtain the real-time downlink data traffic.
    
      // Obtain the real-time downlink data traffic of the primary Wi-Fi NIC. wlan0 is the name of the primary Wi-Fi NIC.
      statistics.getIfaceRxBytes('wlan0').then((stats: number) => {
        hilog.info(0x0000, 'testTag', JSON.stringify(stats));
        // ...
      })
      .catch((err: BusinessError) => {
        hilog.error(0x0000, 'testTag', JSON.stringify(err));
        // ...
      });
      // ...
      // Obtain the real-time uplink data traffic of the primary Wi-Fi NIC. wlan0 is the name of the primary Wi-Fi NIC.
      statistics.getIfaceTxBytes('wlan0').then((stats: number) => {
        hilog.info(0x0000, 'testTag', JSON.stringify(stats));
        // ...
      })
      .catch((err: BusinessError) => {
        hilog.error(0x0000, 'testTag', JSON.stringify(err));
        // ...
      });
    // ...
    
3.  Obtain the real-time data traffic of the cellular network.
    
    Call **getCellularRxBytes** to obtain the real-time uplink and downlink data traffic of the cellular network.
    
    // Obtain the real-time downlink data traffic of the cellular network.
    statistics.getCellularRxBytes().then((stats: number) => {
      hilog.info(0x0000, 'testTag', JSON.stringify(stats));
      // ...
    })
    // ...
    // Obtain the real-time uplink data traffic of the cellular network.
    statistics.getCellularTxBytes().then((stats: number) => {
      hilog.info(0x0000, 'testTag', JSON.stringify(stats));
      // ...
    })
    // ...
    
4.  Obtain the real-time data traffic of all NICs.
    
    Call **getAllRxBytes** to obtain the real-time uplink and downlink data traffic of all NICs.
    
    // Obtain the real-time downlink data traffic of all NICs.
    statistics.getAllRxBytes().then((stats: number) => {
      hilog.info(0x0000, 'testTag', JSON.stringify(stats));
      // ...
    })
    // ...
    // Obtain the real-time uplink data traffic of all NICs.
    statistics.getAllTxBytes().then((stats: number) => {
      hilog.info(0x0000, 'testTag', JSON.stringify(stats));
      // ...
    })
    // ...
    
5.  Obtain the real-time data traffic of the specified application.
    
    Call **getUidRxBytes** with the UID specified to obtain the real-time uplink and downlink data traffic of the specified application.
    
     let UID = 20010038;
    
    // Obtain the real-time downlink data traffic of the specified application.
    // ...
    statistics.getUidRxBytes(UID).then((stats: number) => {
      hilog.info(0x0000, 'testTag', JSON.stringify(stats));
      // ...
    })
    // ...
    // Obtain the real-time uplink data traffic of the specified application.
    // ...
    statistics.getUidTxBytes(UID).then((stats: number) => {
      hilog.info(0x0000, 'testTag', JSON.stringify(stats));
      // ...
    })
    // ...
    
6.  Obtains the real-time data traffic of the specified socket.
    
    Call **getSockfdRxBytes** with **sockFd** specified to obtain the real-time uplink and downlink data traffic of the specified socket.
    
    // Obtain the real-time downlink data traffic of the specified socket.
    let tcp: socket.TCPSocket = socket.constructTCPSocketInstance();
    // ...
    tcp.getSocketFd().then((sockfd: number) => {
      statistics.getSockfdRxBytes(sockfd).then((stats: number) => {
        hilog.info(0x0000, 'testTag', JSON.stringify(stats));
        // ...
      }).catch((err: BusinessError) => {
        hilog.error(0x0000, 'testTag', JSON.stringify(err));
        // ...
      });
    })
    // ...
    // Obtain the real-time uplink data traffic of the specified socket.
    tcp.getSocketFd().then((sockfd: number) => {
      statistics.getSockfdTxBytes(sockfd).then((stats: number) => {
        hilog.info(0x0000, 'testTag', JSON.stringify(stats));
        // ...
      }).catch((err: BusinessError) => {
        hilog.error(0x0000, 'testTag', JSON.stringify(err));
        // ...
      });
    })
    // ...
