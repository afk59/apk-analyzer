# Initiating and Releasing Multi-Network Concurrency

#### Use Case

Your app can initiate multi-network concurrency for network acceleration based on the service needs and relevant suggestions provided by the device, and promptly release it when the use is complete. Wi-Fi–cellular and primary–secondary SIM combinations are supported for concurrency. Connection paths cannot be freely combined. All combinations are determined by the device.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a8/v3/sgjhJmzsQSiunLgkcu15sg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062017Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=C54EFB4BAB74BCF2D8DD884E6725A03409C953E7F674EE5556CD74E6CB81034E)

-   Primary–secondary SIM concurrency requires that **Smart Data Switch** be enabled and depends on the frequency bands of the networks the two SIMs reside on. If concurrency conditions are not met, such as both SIMs using the same carrier, multi-network concurrency initiation will fail.
-   Due to hardware restrictions, some devices do not support multi-network concurrency in dual-SIM scenarios. You can check the returned error code for details.
-   If the current transmission protocol does not support a specific network to be added for multi-network concurrency, that network cannot be used. For example, if [HTTP](../../../network-kit/network-access/using-http-for-network-access/document.md) supports only the default network, but does not support the added network, multi-network concurrency is not available.

#### Preparations

To initiate multi-network concurrency, ensure that the network acceleration switch must be enabled under **Settings** > **Mobile network** > **Network acceleration** on the device. If you cannot find this switch on a device, the device/ROM does not support multi-network concurrency.

#### API Description

For details about the APIs, please refer to the [API document](https://developer.huawei.com/consumer/en/doc/harmonyos-references/networkboost-nethandover#section8508131819279).

| 
API

 | 

Description

 |
| :-- | :-- |
| 

requestMultiPath(callback: Callback<MultiPathRequestResult>): void

 | 

Initiates a multi-network concurrency request.

 |
| 

releaseMultiPath(): void

 | 

Releases multi-network concurrency.

 |

#### Development Procedure

1.  Import the Network Boost Kit module.
    
    import { netHandover } from '@kit.NetworkBoostKit';
    import { BusinessError } from '@kit.BasicServicesKit';
    
2.  Initiate a multi-network concurrency request and listen for any changes on the multi-network concurrency status.
    
    try {
      netHandover.requestMultiPath((data: netHandover.MultiPathRequestResult) => {
       console.info(\` requestMultiPath result:\` + JSON.stringify(data));
      });
     } catch (err) {
      console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
    }
    
3.  When the service process ends, call the **releaseMultiPath** API to release multi-network concurrency.
    
    try {
      netHandover.releaseMultiPath();
     } catch (err) {
      console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
    }
