# Obtaining System Setting Attributes by API Calls

#### Use Case

Scenario Fusion Kit provides an API for you to obtain system setting attributes such as the Bluetooth, location, Wi-Fi, and screen orientation information attributes.

#### Restrictions

Scenario-specific APIs support phones, tablets, 2-in-1 devices, (since 5.1.0(18)) wearables, and (since 5.1.0(18)) TVs.

#### API Description

The following table describes the API for obtaining system setting attributes. For other APIs, please refer to [atomicService (Convergent Scenario-specific APIs)](https://developer.huawei.com/consumer/en/doc/harmonyos-references/scenario-fusion-atomicservice).

| 
API

 | 

Description

 |
| :-- | :-- |
| 

[getSystemSetting](https://developer.huawei.com/consumer/en/doc/harmonyos-references/scenario-fusion-atomicservice#section171285335615)(properties?: Array<[SystemSettingType](https://developer.huawei.com/consumer/en/doc/harmonyos-references/scenario-fusion-atomicservice#section11423195912475)\>): [SystemSettingInfo](https://developer.huawei.com/consumer/en/doc/harmonyos-references/scenario-fusion-atomicservice#section53111326141919)

 | 

Obtains system setting attributes such as the Bluetooth, location, Wi-Fi, and device direction information attributes.

 |

#### Development Procedure

1.  Import the Scenario Fusion Kit module and related common modules.
    
    import { atomicService } from '@kit.ScenarioFusionKit';
    import { hilog } from '@kit.PerformanceAnalysisKit';
    
2.  Call the API, pass required attributes, and obtain the attribute values.
    
    let stateArray: Array<atomicService.SystemSettingType> =
      \['bluetoothEnabled', 'locationEnabled', 'deviceOrientation', 'wifiEnabled'\];
    try {
      let data = atomicService.getSystemSetting(stateArray);
      hilog.info(0x0000, 'testTag', 'succeeded in getting system setting info');
      let bluetoothEnabled: boolean | undefined = data.bluetoothEnabled;
      let locationEnabled: boolean | undefined = data.locationEnabled;
      let deviceOrientation: string | undefined = data.deviceOrientation;
      let wifiEnabled: boolean | undefined = data.wifiEnabled;
    } catch (error) {
      hilog.error(0x0001, 'testTag', 'failReason: %{public}d %{public}s', error.code, error.message);
    }
