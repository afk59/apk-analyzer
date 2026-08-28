# SystemCapability

#### Overview

## System Capabilities and APIs

SystemCapability (SysCap) refers to a standalone feature in the operating system, for example, Bluetooth, Wi-Fi, NFC, or camera. Each SysCap corresponds to a set of APIs, whose availability depends on the support of the target device. Such a set of APIs can be provided in DevEco Studio for association.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5b/v3/wXSi2Oz_RrCW1cpWoGTcyg/en-us_image_0000002537765304.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T060759Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=55BD04C72A15241ECD15CBBC8EDC2E97578E047E0E9C3B7EFBAE9D5809892C99)

## Supported SysCap Set, Associated SysCap Set, and Required SysCap Set

The supported SysCap set, associated SysCap set, and required SysCap set are collections of SysCaps.

The supported SysCap set covers the device capabilities, and the required SysCap set covers the application capabilities. If the SysCap set required by application A is a subset of the SysCap set supported by device N, application A can be distributed to device N for installation and running. Otherwise, application A cannot be distributed.

The associated SysCap set covers the system capabilities of associated APIs that DevEco Studio offers during application development.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fc/v3/ZmsbIUbpTHuKOCqKiUB25A/en-us_image_0000002537925244.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T060759Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=97ED8303141C20530C2C2597ADEECC70C0ADF06D833DA96C5633665111E3C1B2)

## Devices and Supported SysCap Sets

Each device provides a SysCap set that matches its hardware capability.

The SDK classifies devices into general devices and custom devices. The general devices' supported SysCap set is defined by HarmonyOS, and the custom devices' is defined by device vendors.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d0/v3/NEGiTdp7R86P5w8rnb8zCQ/en-us_image_0000002568685021.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T060759Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=7FB47D70E5C63E0BEB2820F555F9F249F8B6CBD7B625FC7361C5ADB8D771050E)

## Mapping Between Devices and SDK Capabilities

The SDK provides a full set of APIs for DevEco Studio. DevEco Studio identifies the supported SysCap set based on the devices selected for the project, filters the APIs contained in the SysCap set, and provides the supported APIs for association (to autocomplete input).

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/42/v3/P80xnJgTRvqSqHFB58RrtA/en-us_image_0000002568765031.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T060759Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=33B476AB4EA37FE3B1F12E286B5F5BBDF585899DA9588F91C6327B4208F85420)

#### How to Develop

## Adding Custom SysCap

For a specific device model, the capabilities may exceed the capability set defined for the default device. To use these capabilities, you need to configure a custom SysCap.

In the /src/main directory of a project in DevEco Studio, manually create the syscap.json file. For example, right-click entry/src/main and choose New > File.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7c/v3/6gc90CDLT_u1hocQzN2xsw/en-us_image_0000002537765306.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T060759Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=94626C8BCB67FE0E5D42528ABB9CAF0AFA2700BA59633AF143B3D78D10900FA0)

Create a file and name it syscap.json.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fd/v3/Ne1ETJwsQoymUO-sFkGbiw/en-us_image_0000002537925246.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T060759Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=A8A191583C9AB6B96915A94F9CBC0B1E6244C17E3A236CF965B421128E87CED7)

Open the syscap.json file.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/28/v3/kdH-jCjzR7SV3fbYdXluoA/en-us_image_0000002568685023.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T060759Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=9BE68AA9CBECED33D9739CF9AE028A08F09D2B0DC2B03492E296C04CD0B81D10)

Enter the required SysCaps in the following format. The following is an example of the syscap.json file for using the NFC capability:

{
  "devices": {
    "general": \[
      // Each typical device corresponds to a SysCap set. Multiple typical devices can be configured. The devices must be the same as those selected in the project.
      "phone"
    \]
  },
  "development": {
    // The SysCap set in addedSysCaps and the SysCap set supported by each device configured in devices form the associated SysCap set.
    "addedSysCaps": \[
      "SystemCapability.Communication.NFC.Core",
      "SystemCapability.Communication.NFC.CardEmulation",
      "SystemCapability.Communication.NFC.Tag"
    \]
  }
}

## Single-Device Application Development

By default, the associated SysCap set and required SysCap set of the application are the same as the supported SysCap set of the device. Exercise caution when modifying the required SysCap set.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1c/v3/ZbFfsBwnQ_SzoRO7NW09UQ/en-us_image_0000002568765033.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T060759Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=DB9473977840DCAE1B2D34BB998A6ED8752A7EEE9E75BBA371CCEF2F644A665B)

## Cross-Device Application Development

By default, the associated SysCap set of an application is the union of multiple devices' supported SysCap sets, while the required SysCap set is the intersection of the devices' supported SysCap sets.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/72/v3/gPfMyCb7Rd-Wi6pturfaCA/en-us_image_0000002537765308.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T060759Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=ADF8E524125538852E746FD124DC9DE1C99C91E205A60718CB4B1D59B532E073)

## Checking Whether an API Is Available

You can use either the ArkTS or native API to determine whether an API is available.

-   ArkTS API
    
    -   Method 1: Use the **canIUse()** API to check whether a SysCap is supported.
        
        if (canIUse("SystemCapability.ArkUI.ArkUI.Full")) {
           console.info("This device supports SystemCapability.ArkUI.ArkUI.Full.");
        } else {
           console.info("This device does not support SystemCapability.ArkUI.ArkUI.Full.");
        }
        
    -   Method 2: Import a module using the **import** API. If the current device does not support the module, the import result is **undefined**. Before using an API, you must make sure the API is available.
        
        import { geoLocationManager } from '@kit.LocationKit';
        
        try {
        geoLocationManager.getCurrentLocation((location) => {
            console.info('current location: ' + JSON.stringify(location));
        });
        } catch(err) {
            console.error('This device does not support location information.' + err);
        }
        
-   Native API
    
    #include <stdio.h>
    #include <stdlib.h>
    #include "syscap\_ndk.h"
    
    char syscap\[\] = "SystemCapability.ArkUI.ArkUI.Full";
    bool result = canIUse(syscap);
    if (result) {
        printf("SysCap: %s is supported!\\n", syscap);
    } else {
        printf("SysCap: %s is not supported!\\n", syscap);
    }
    

You can also find out the SysCap to which an API belongs by referring to the API reference document.

## Checking the Differences Between Devices with a Specific SysCap

The performance of a SysCap may vary by device type. For example, a tablet is superior to a wearable device in terms of the camera capability.

The following code snippet uses the facial recognition capability as an example:

import { userAuth } from '@kit.UserAuthenticationKit';

const authParam : userAuth.AuthParam = {
  challenge: new Uint8Array(),
  authType: \[userAuth.UserAuthType.PIN\],
  authTrustLevel: userAuth.AuthTrustLevel.ATL1,
};
const widgetParam :userAuth.WidgetParam = {
  title: 'Enter password',
};

// Use try...catch to capture exceptions when using the API. If the SysCap of the API is not compatible with the current device, error code 801 is returned.
try {
  let userAuthInstance = userAuth.getUserAuthInstance(authParam, widgetParam);
  userAuthInstance.start();
    console.info('Device authentication succeeded.');
} catch (error) {
    console.error('auth catch error: ' + JSON.stringify(error));
}

## How Do SysCap Differences Arise Between Devices

The device SysCaps in product solutions vary according to the component combination defined by the product solution vendor. The following figure shows the overall process.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fe/v3/3sKlW_YWSVKTAQhtmugk4w/en-us_image_0000002537925248.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T060759Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=088B4E091E4ADF0D34D543A50938A67E8535851AA1475C011EA080DE9A4BCF9E)

1.  A set of operating system source code consists of optional and mandatory components. Different components represent different SysCaps.
    
2.  In a normalized released SDK, APIs are mapped to SysCap sets.
    
3.  Product solution vendors can assemble components based on hardware capabilities and product requirements.
    
4.  The components configured for a product can be system components or proprietary components developed by a third party. Since there is mapping between components and SysCap, the SysCap set of the product can be obtained after all components are assembled.
    
5.  The SysCap set is encoded to generate the PCID. You can import the PCID to DevEco Studio and decode it into SysCaps. During development, compatibility processing is performed to mitigate the SysCap differences of devices.
    
6.  System parameters deployed on devices contain the SysCap set. The system provides native interfaces and application interfaces for components and applications to check whether a specific SysCap is available.
    
7.  During application development, the SysCap set required by the application is encoded into the Required Product Compatibility ID (RPCID) and written into the application installation package. During application installation, the package manager decodes the RPCID to obtain the SysCap set required by the application and compares it with the SysCap set supported by the device. If the SysCap set required by the application is met, the application can be installed on the device.
    
8.  When an application is running on a device, the **canIUse** API can be used to query whether the device is compatible with a specific SysCap.
