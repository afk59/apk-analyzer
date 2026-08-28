# @ohos.deviceInfo (Device Information)

The **deviceInfo** module provides terminal device information query, which cannot be configured by developers.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/08/v3/kyTnhVaYS0mGL4h8UeT_Gw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062356Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=90F840E37266AD6FCD5DF5841D0207DC2E76DD2B969CB0AF2845BC917908CE83)

The initial APIs of this module are supported since API version 6. Newly added APIs will be marked with a superscript to indicate their earliest API version.

Some parameters whose return value is the default value are not yet available.

The APIs of this module return information about device constants. You are not expected to call these APIs frequently.

#### Modules to Import

import { deviceInfo } from '@kit.BasicServicesKit';

#### Constants

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/37/v3/nBHCRrO3TpSyH_7u_nFKXQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062356Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=E1F7C84B36A7E2BA84488CB5D1163A5B6A6794AC06697C5E462DCA809426F6BC)

Unless otherwise specified, the maximum data length is 96 bytes.

**System capability**: SystemCapability.Startup.SystemInfo

**Required permissions**: The items in the table below require different system capabilities.

| Name | Type | Read-Only | Description |
| :-- | :-- | :-- | :-- |
| deviceType | string | Yes | 
Device type. For details, see [deviceTypes tag](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/module-configuration-file#devicetypes).

**Atomic service API**: This API can be used in atomic services since API version 11.

Example: phone

 |
| manufacture | string | Yes | 

Device manufacturer.

Example: HUAWEI

 |
| brand | string | Yes | 

Device brand.

**Atomic service API**: This API can be used in atomic services since API version 11.

Example: HUAWEI

 |
| marketName | string | Yes | 

Marketing name.

Example: HUAWEI Mate 60 Pro

 |
| productSeries | string | Yes | 

Product series.

Example: ALN

 |
| productModel | string | Yes | 

Product model.

**Atomic service API**: This API can be used in atomic services since API version 11.

Example: ALN-AL00

 |
| productModelAlias14+ | string | Yes | 

Product model alias.

**Atomic service API**: This API can be used in atomic services since API version 14.

Example: TAS-AL00

 |
| softwareModel | string | Yes | 

Software model.

Example: ALN-AL00

 |
| hardwareModel | string | Yes | 

Hardware model.

Example: HL1CMSM

 |
| hardwareProfile(deprecated) | string | Yes | 

Hardware profile.

Note:

This API is supported since API version 6 and deprecated since API version 9.

Example: default

 |
| serial | string | Yes | 

Device serial number (SN).

Note: The device SN can be used as the unique identifier of a device.

**Required permission**: ohos.permission.sec.ACCESS\_UDID (for system applications and enterprise applications only)

Example: The SN varies with the device.

 |
| bootloaderVersion | string | Yes | 

Bootloader version.

Example: bootloader

 |
| abiList | string | Yes | 

Application binary interface (Abi) list.

Example: arm64-v8a

 |
| securityPatchTag | string | Yes | 

Security patch tag.

Example: 2024/1/1

 |
| displayVersion | string | Yes | 

Product version.

Example: ALN-AL00 5.0.0.1(XXX)

 |
| incrementalVersion | string | Yes | 

Incremental version.

Example: default

 |
| osReleaseType | string | Yes | 

OS release type. The options are as follows:

\- **Canary**: Preliminary release open only to specific developers. This release does not promise API stability and may require tolerance of instability.

\- **Beta**: Release open to all developers. This release does not promise API stability and may require tolerance of instability.

\- **Release**: Official release open to all developers. This release promises that all APIs are stable.

Example: Canary1/Beta2/Release

 |
| osFullName | string | Yes | 

System version. The version number is in the format of **HarmonyOS-x.x.x.x**.

**Atomic service API**: This API can be used in atomic services since API version 11.

Example: OpenHarmony-5.0.0.1(Canary1)

 |
| majorVersion | number | Yes | 

Major version number, which increments with the main version. The value is the first digit in **osFullName**. You are advised to use **deviceInfo.majorVersion** instead of parsing **osFullName** to obtain the value, facilitating efficiency improvement.

Example: 5

 |
| seniorVersion | number | Yes | 

Senior version number, which increments with architecture and feature updates. The value is the second digit in **osFullName**. You are advised to use **deviceInfo.seniorVersion** instead of parsing **osFullName** to obtain the value, facilitating efficiency improvement.

Example: 0

 |
| featureVersion | number | Yes | 

Feature version number. The value is the third digit in **osFullName**. You are advised to use **deviceInfo.featureVersion** instead of parsing **osFullName** to obtain the value, facilitating efficiency improvement.

Example: 0

 |
| buildVersion | number | Yes | 

Build version number. The value is the fourth digit in **osFullName**. You are advised to use **deviceInfo.buildVersion** instead of parsing **osFullName** to obtain the value, facilitating efficiency improvement.

Example: 1

 |
| sdkApiVersion | number | Yes | 

SDK API version.

**Atomic service API**: This API can be used in atomic services since API version 14.

Example: 12

 |
| firstApiVersion | number | Yes | 

First API version.

Example: 3

 |
| versionId | string | Yes | 

Version ID. It consists of the following fields: **deviceType**, **manufacture**, **brand**, **productSeries**, **osFullName**, **productModel**, **softwareModel**, **sdkApiVersion**, **incrementalVersion**, and **buildType**.

Example: wearable/HUAWEI/HUAWEI/TAS/OpenHarmony-5.0.0.1/TAS-AL00/TAS-AL00/12/default/release:nolog

 |
| buildType | string | Yes | 

Build type.

Example: default

 |
| buildUser | string | Yes | 

Build user.

Example: default

 |
| buildHost | string | Yes | 

Build host.

Example: default

 |
| buildTime | string | Yes | 

Build time.

Example: default

 |
| buildRootHash | string | Yes | 

Build root hash.

Example: default

 |
| udid7+ | string | Yes | 

Device UDID.

Note: The data length is 65 bytes. The UDID can be used as the unique identifier of a device.

**Required permission**: ohos.permission.sec.ACCESS\_UDID (for system applications and enterprise applications only)

Example: 9D6AABD147XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXE5536412

 |
| distributionOSName10+ | string | Yes | 

Distribution OS name.

Example: HarmonyOS

 |
| distributionOSVersion10+ | string | Yes | 

Distribution OS version. The value is in the format of **x.x.x**, where **x** is a digit.

Example: 5.0.0

 |
| distributionOSApiVersion10+ | number | Yes | 

Distribution OS API version.

Example: 50001

 |
| distributionOSApiName13+ | string | Yes | Distribution OS API name. |
| distributionOSReleaseType10+ | string | Yes | 

Distribution OS release type.

Example: Release

 |
| ODID12+ | string | Yes | 

Open device identifier.

An ODID will be regenerated in the following scenarios:

Restore a phone to its factory settings.

Uninstall and reinstall all applications with the same **developerId** on one device.

An ODID is generated based on the following rules:

The value is generated based on the **groupId** parsed from the **developerId** in the signature information. As **groupId.developerId** is the rule, if no **groupId** exists, the **developerId** is used as the **groupId**.

Applications with the same **developerId** use the same ODID on one device.

Applications with different **developerId**s use different ODIDs on one device.

Applications with the same **developerId** use different ODIDs on different devices.

Applications with different **developerId**s use different ODIDs on different devices.

Note: The data length is 37 bytes (including the terminator).

Example: 1234a567-XXXX-XXXX-XXXX-XXXXXXXXXXXX

 |
| diskSN15+ | string | Yes | 

Disk SN.

Note: This field can be queried only on the 2-in-1 device. For other devices, the query result is empty.

**Required permissions**: ohos.permission.ACCESS\_DISK\_PHY\_INFO

Example: 2502EM400567

 |
| performanceClass19+ | [PerformanceClassLevel](#performanceclasslevel19) | Yes | Device capability level, which is evaluated based on the CPU, memory, storage read/write performance, and screen resolution. |
| chipType21+ | string | Yes | 

CPU chip model.

Example: xxxxx

 |
| bootCount21+ | number | Yes | 

Number of device reboots. If the number cannot be obtained, **–1** is returned.

Example: 100

 |

**Example**

    import { deviceInfo } from '@kit.BasicServicesKit';

    let deviceTypeInfo: string = deviceInfo.deviceType;
    // Output: the value of the deviceType is :wearable
    console.info('the value of the deviceType is :' + deviceTypeInfo);

    let manufactureInfo: string = deviceInfo.manufacture;
    // Output: the value of the manufacture is :HUAWEI
    console.info('the value of the manufactureInfo is :' + manufactureInfo);

    let brandInfo: string = deviceInfo.brand;
    // Output: the value of the brand is :HUAWEI
    console.info('the value of the device brand is :' + brandInfo);

    let marketNameInfo: string = deviceInfo.marketName;
    // Output: the value of the marketName is :Mate XX
    console.info('the value of the deviceInfo marketName is :' + marketNameInfo);

    let productSeriesInfo: string = deviceInfo.productSeries;
    // Output: the value of the productSeries is :TAS
    console.info('the value of the deviceInfo productSeries is :' + productSeriesInfo);

    let productModelInfo: string = deviceInfo.productModel;
    // Output: the value of the productModel is :TAS-AL00
    console.info('the value of the deviceInfo productModel is :' + productModelInfo);

    let productModelAliasInfo: string = deviceInfo.productModelAlias;
    console.info('the value of the deviceInfo productModelAlias is :' + productModelAliasInfo);

    let softwareModelInfo: string = deviceInfo.softwareModel;
    // Output: the value of the softwareModel is :TAS-AL00
    console.info('the value of the deviceInfo softwareModel is :' + softwareModelInfo);

    let hardwareModelInfo: string = deviceInfo.hardwareModel;
    // Output: the value of the hardwareModel is :TASA00CVN1
    console.info('the value of the deviceInfo hardwareModel is :' + hardwareModelInfo);

    let serialInfo: string = deviceInfo.serial;
    // Output: the value of the serial is :The SN varies with the device.
    console.info('the value of the deviceInfo serial is :' + serialInfo);

    let bootloaderVersionInfo: string = deviceInfo.bootloaderVersion;
    // Output: the value of the bootloaderVersion is :bootloader
    console.info('the value of the deviceInfo bootloaderVersion is :' + bootloaderVersionInfo);

    let abiListInfo: string = deviceInfo.abiList;
    // Output: the value of the abiList is :arm64-v8a
    console.info('the value of the deviceInfo abiList is :' + abiListInfo);

    let securityPatchTagInfo: string = deviceInfo.securityPatchTag;
    // Output: the value of the securityPatchTag is :2021/01/01
    console.info('the value of the deviceInfo securityPatchTag is :' + securityPatchTagInfo);

    let displayVersionInfo: string = deviceInfo.displayVersion;
    // Output: the value of the displayVersion is :XXX X.X.X.X
    console.info('the value of the deviceInfo displayVersion is :' + displayVersionInfo);

    let incrementalVersionInfo: string = deviceInfo.incrementalVersion;
    // Output: the value of the incrementalVersion is :default
    console.info('the value of the deviceInfo incrementalVersion is :' + incrementalVersionInfo);

    let osReleaseTypeInfo: string = deviceInfo.osReleaseType;
    // Output: the value of the osReleaseType is :Release
    console.info('the value of the deviceInfo osReleaseType is :' + osReleaseTypeInfo);

    let osFullNameInfo: string = deviceInfo.osFullName;
    // Output: the value of the osFullName is :OpenHarmony-5.0.0.1
    console.info('the value of the deviceInfo osFullName is :' + osFullNameInfo);

    let majorVersionInfo: number = deviceInfo.majorVersion;
    // Output: the value of the majorVersion is :5
    console.info('the value of the deviceInfo majorVersion is :' + majorVersionInfo);

    let seniorVersionInfo: number = deviceInfo.seniorVersion;
    // Output: the value of the seniorVersion is :0
    console.info('the value of the deviceInfo seniorVersion is :' + seniorVersionInfo);

    let featureVersionInfo: number = deviceInfo.featureVersion;
    // Output: the value of the featureVersion is :0
    console.info('the value of the deviceInfo featureVersion is :' + featureVersionInfo);

    let buildVersionInfo: number = deviceInfo.buildVersion;
    // Output: the value of the buildVersion is :1
    console.info('the value of the deviceInfo buildVersion is :' + buildVersionInfo);

    let sdkApiVersionInfo: number = deviceInfo.sdkApiVersion;
    // Output: the value of the sdkApiVersion is :12
    console.info('the value of the deviceInfo sdkApiVersion is :' + sdkApiVersionInfo);

    let firstApiVersionInfo: number = deviceInfo.firstApiVersion;
    // Output: the value of the firstApiVersion is :3
    console.info('the value of the deviceInfo firstApiVersion is :' + firstApiVersionInfo);

    let versionIdInfo: string = deviceInfo.versionId;
    // Output: the value of the versionId is :wearable/HUAWEI/HUAWEI/TAS/OpenHarmony-5.0.0.1/TAS-AL00/TAS-AL00/12/default/release:nolog
    console.info('the value of the deviceInfo versionId is :' + versionIdInfo);

    let buildTypeInfo: string = deviceInfo.buildType;
    // Output: the value of the buildType is :default
    console.info('the value of the deviceInfo buildType is :' + buildTypeInfo);

    let buildUserInfo: string = deviceInfo.buildUser;
    // Output: the value of the buildUser is :default
    console.info('the value of the deviceInfo buildUser is :' + buildUserInfo);

    let buildHostInfo: string = deviceInfo.buildHost;
    // Output: the value of the buildHost is :default
    console.info('the value of the deviceInfo buildHost is :' + buildHostInfo);

    let buildTimeInfo: string = deviceInfo.buildTime;
    // Output: the value of the buildTime is :default
    console.info('the value of the deviceInfo buildTime is :' + buildTimeInfo);

    let buildRootHashInfo: string = deviceInfo.buildRootHash;
    // Output: the value of the buildRootHash is :default
    console.info('the value of the deviceInfo buildRootHash is :' + buildRootHashInfo);

    let udid: string = deviceInfo.udid;
    // Output: the value of the udid is :9D6AABD147XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXE5536412
    console.info('the value of the deviceInfo udid is :' + udid);

    let distributionOSName: string = deviceInfo.distributionOSName
    // Output: the value of the distributionOSName is :OpenHarmony
    console.info('the value of the deviceInfo distributionOSName is :' + distributionOSName);

    let distributionOSVersion: string = deviceInfo.distributionOSVersion
    // Output: the value of the distributionOSVersion is :5.0.0
    console.info('the value of the deviceInfo distributionOSVersion is :' + distributionOSVersion);

    let distributionOSApiVersion: number = deviceInfo.distributionOSApiVersion
    // Output: the value of the distributionOSApiVersion is :500001
    console.info('the value of the deviceInfo distributionOSApiVersion is :' + distributionOSApiVersion);

    let distributionOSApiName: string = deviceInfo.distributionOSApiName
    console.info('the value of the deviceInfo distributionOSApiName is :' + distributionOSApiName);

    let distributionOSReleaseType: string = deviceInfo.distributionOSReleaseType
    // Output: the value of the distributionOSReleaseType is :Release
    console.info('the value of the deviceInfo distributionOSReleaseType is :' + distributionOSReleaseType);

    let odid: string = deviceInfo.ODID;
    // Output: the value of the ODID is :1234a567-XXXX-XXXX-XXXX-XXXXXXXXXXXX
    console.info('the value of the deviceInfo odid is :' + odid);

    let diskSN: string = deviceInfo.diskSN;
    // Output: the value of the deviceInfo diskSN is :2502EM400567
    console.info('the value of the deviceInfo diskSN is :' + diskSN);

    let performanceClass = deviceInfo.performanceClass;
    // Output: the value of the deviceInfo performanceClass is :0
    console.info('the value of the deviceInfo performanceClass is :' + performanceClass);

    let chipType: string = deviceInfo.chipType;
    // Output: the value of the deviceInfo chipType is :xxxxx
    console.info('the value of the deviceInfo chipType is :' + chipType);

    let bootCount: number = deviceInfo.bootCount
    // Output: the value of the bootCount is :100
    console.info('the value of the deviceInfo bootCount is :' + bootCount);

#### PerformanceClassLevel19+

Enumerates the device capability levels.

**System capability**: SystemCapability.Startup.SystemInfo

| Name | Value | Description |
| :-- | :-- | :-- |
| CLASS\_LEVEL\_HIGH | 0 | High |
| CLASS\_LEVEL\_MEDIUM | 1 | Medium |
| CLASS\_LEVEL\_LOW | 2 | Low |

#### DeviceTypes20+

Enumerates device types, which can be used to verify the return value of **deviceType**.

**Atomic service API**: This API can be used in atomic services since API version 20.

**System capability**: SystemCapability.Startup.SystemInfo

| Name | Value | Description |
| :-- | :-- | :-- |
| TYPE\_DEFAULT | 'default' | Default device |
| TYPE\_PHONE | 'phone' | Smartphone |
| TYPE\_TABLET | 'tablet' | Tablet |
| TYPE\_2IN1 | '2in1' | PC/2-in-1 device |
| TYPE\_TV | 'tv' | Smart TV |
| TYPE\_WEARABLE | 'wearable' | Wearable |
| TYPE\_CAR | 'car' | Head unit |

**Example**

    let deviceTypesInfoDefault: string = deviceInfo.DeviceTypes.TYPE\_DEFAULT;
    // Output: the value of the DeviceTypes is :default
    console.info('the value of the DeviceTypes is :' + deviceTypesInfoDefault);

    let deviceTypesInfoPhone: string = deviceInfo.DeviceTypes.TYPE\_PHONE;
    // Output: the value of the DeviceTypes is :phone-type
    console.info('the value of the DeviceTypes is :' + deviceTypesInfoPhone);

    let deviceTypesInfoTablet: string = deviceInfo.DeviceTypes.TYPE\_TABLET;
    // Output: the value of the DeviceTypes is :tablet
    console.info('the value of the DeviceTypes is :' + deviceTypesInfoTablet);

    let deviceTypesInfo2IN1: string = deviceInfo.DeviceTypes.TYPE\_2IN1;
    // Output: the value of the DeviceTypes is :2in1
    console.info('the value of the DeviceTypes is :' + deviceTypesInfo2IN1);

    let deviceTypesInfoTV: string = deviceInfo.DeviceTypes.TYPE\_TV;
    // Output: the value of the DeviceTypes is :tv
    console.info('the value of the DeviceTypes is :' + deviceTypesInfoTV);

    let deviceTypesInfoWearable: string = deviceInfo.DeviceTypes.TYPE\_WEARABLE;
    // Output: the value of the DeviceTypes is :wearable
    console.info('the value of the DeviceTypes is :' + deviceTypesInfoWearable);

    let deviceTypesInfoCar: string = deviceInfo.DeviceTypes.TYPE\_CAR;
    // Output: the value of the DeviceTypes is :car
    console.info('the value of the DeviceTypes is :' + deviceTypesInfoCar);
