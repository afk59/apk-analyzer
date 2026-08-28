# Listening to HiCar Connection Status

#### Use Cases

An ecosystem app can obtain connection information by listening to the smart mobility connection status to adapt to HiCar services (for example, app hop).

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cf/v3/Yuy1jJJyT8akZvzkUgCR1A/en-us_image_0000002481508030.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062023Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=01D74E910AC2A6B5C53A476FBCC4A95EC3ACBF9544E02D77CD7684ECDE2B1EFB "Click to enlarge")

#### API Description

The following table describes the APIs for listening to the HiCar connection status.

| 
API

 | 

Description

 |
| :-- | :-- |
| 

[on('smartMobilityStatus')](https://developer.huawei.com/consumer/en/doc/harmonyos-references/car-smartmobilitycommon#section6447182819393)

 | 

Registers a smart mobility connection status listener.

 |
| 

[off('smartMobilityStatus')](https://developer.huawei.com/consumer/en/doc/harmonyos-references/car-smartmobilitycommon#section1962104712398)

 | 

Unregisters a smart mobility connection status listener.

 |

#### Development Process

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/08/v3/YG6WZwDnTNSIWzeM3Z_q3Q/en-us_image_0000002513711447.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062023Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=0D5F67D28BEF1FDD125899B790C709A7D6CC2DAB86CABC099B29208099173093 "Click to enlarge")

#### Development Procedure

1.  Import required modules.
    
    import { smartMobilityCommon } from '@kit.CarKit';
    import { hilog } from '@kit.PerformanceAnalysisKit';
    
2.  Listen to HiCar connection status.
    
    When your app is adapted for HiCar, it needs to register a smart mobility connection status listener to execute corresponding service logic.
    
    try {
      // Obtain the **SmartMobilityAwareness** instance.
      let awareness: smartMobilityCommon.SmartMobilityAwareness = smartMobilityCommon.getSmartMobilityAwareness();
    
      // Service type.
      let types: smartMobilityCommon.SmartMobilityType\[\] = \[smartMobilityCommon.SmartMobilityType.HICAR\];
    
      // Callback function of smart mobility connection status.
      const callBack = (info: smartMobilityCommon.SmartMobilityInfo) => {
        hilog.info(0x0000, 'testTag', 'Received smart mobility info: ', JSON.stringify(info));
        if (info.status === smartMobilityCommon.SmartMobilityStatus.RUNNING) {
          // Connection success notification.
        } else if (info.status === smartMobilityCommon.SmartMobilityStatus.IDLE) {
          // Disconnection notification.
        }
      };
    
      // Register a smart mobility connection status listener.
      awareness.on('smartMobilityStatus', types, callBack);
    } catch (e) {
      // Obtain the error code for an API call exception and handle the exception.
      hilog.error(0x0000, 'testTag', \`on smart mobility status listener error, error code: ${e?.code}\`);
    }
    
3.  Unregister the listener.
    
    When exiting, the app needs to unregister the listener to reduce unnecessary system resource consumption.
    
    try {
      // Obtain the **SmartMobilityAwareness** instance.
      let awareness: smartMobilityCommon.SmartMobilityAwareness = smartMobilityCommon.getSmartMobilityAwareness();
      // Service type.
      let types: smartMobilityCommon.SmartMobilityType\[\] = \[smartMobilityCommon.SmartMobilityType.HICAR\];
      // Unregister the smart mobility connection status listener.
      awareness.off('smartMobilityStatus', types);
    } catch (e) {
      // Obtain the error code for an API call exception and handle the exception.
      hilog.error(0x0000, 'testTag', \`off smart mobility status listener error, error code: ${e?.code}\`);
    }
