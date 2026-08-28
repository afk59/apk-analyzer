# Obtaining System Information Attributes by API Calls

#### Use Case

Scenario Fusion Kit provides an API for you to obtain system information attributes such as the device, network, screen, language, and color mode information attributes.

#### Restrictions

Scenario-specific APIs support phones, tablets, 2-in-1 devices, (since 5.1.0(18)) wearables, and (since 5.1.0(18)) TVs.

#### API Description

The following table describes the API for obtaining system information attributes. For other APIs, please refer to [atomicService (Convergent Scenario-specific APIs)](https://developer.huawei.com/consumer/en/doc/harmonyos-references/scenario-fusion-atomicservice).

| 
API

 | 

Description

 |
| :-- | :-- |
| 

[getSystemInfoSync](https://developer.huawei.com/consumer/en/doc/harmonyos-references/scenario-fusion-atomicservice#section1465318121834)(properties?: Array<[SystemInfoType](https://developer.huawei.com/consumer/en/doc/harmonyos-references/scenario-fusion-atomicservice#section994220537517)\>): [SystemInfo](https://developer.huawei.com/consumer/en/doc/harmonyos-references/scenario-fusion-atomicservice#section6926144111527)

 | 

Obtains system information including the device, network, screen, language, and color mode information. The method contains input parameters.

NOTE:

Currently, the **getSystemInfoSync** API cannot be called to obtain the **windowWidth**, **windowHeight**, **statusBarHeight**, and **screenSafeArea** attributes. To obtain them, call the [getSystemInfo](https://developer.huawei.com/consumer/en/doc/harmonyos-references/scenario-fusion-atomicservice#section17779133174510) API instead.

 |

#### Development Procedure

1.  Import the Scenario Fusion Kit module and related common modules.
    
    import { atomicService } from '@kit.ScenarioFusionKit';
    import { hilog } from '@kit.PerformanceAnalysisKit';
    
2.  Call the API, pass required attributes, and obtain the attribute values.
    
    let stateArray: Array<atomicService.SystemInfoType> =
      \['brand', 'deviceModel', 'screenWidth', 'screenHeight', 'language', 'osFullName', 'fontSizeSetting',
        'sdkApiVersion', 'bluetoothEnabled', 'wifiEnabled', 'locationEnabled', 'deviceOrientation', 'theme'\];
    try {
      let data = atomicService.getSystemInfoSync(stateArray);
      hilog.info(0x0000, 'testTag', 'succeeded in getting system info');
      let brand: string | undefined = data.brand;
      let deviceModel: string | undefined = data.deviceModel;
      let screenWidth: number | undefined = data.screenWidth;
      let screenHeight: number | undefined = data.screenHeight;
      let language: string | undefined = data.language;
      let osFullName: string | undefined = data.osFullName;
      let fontSizeSetting: number | undefined = data.fontSizeSetting;
      let sdkApiVersion: number | undefined = data.sdkApiVersion;
      let bluetoothEnabled: boolean | undefined = data.bluetoothEnabled;
      let wifiEnabled: boolean | undefined = data.wifiEnabled;
      let locationEnabled: boolean | undefined = data.locationEnabled;
      let deviceOrientation: string | undefined = data.deviceOrientation;
      let theme: ColorMode | undefined = data.theme;
    } catch (error) {
      hilog.error(0x0000, 'testTag', 'failReason: %{public}d %{public}s', error.code, error.message);
    }
