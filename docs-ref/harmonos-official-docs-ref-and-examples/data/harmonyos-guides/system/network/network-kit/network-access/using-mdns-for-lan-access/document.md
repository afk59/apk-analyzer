# Using MDNS for LAN Access

#### Overview

Multicast DNS (MDNS) provides functions such as adding, removing, discovering, and resolving local services on a LAN.

-   Local service: a service provider on a LAN, for example, a printer or scanner.

Typical MDNS management scenarios include:

-   Managing local services on a LAN, such as adding, removing, and resolving local services.
-   Discovering local services and listening to the status changes of local services of the specified type through the **DiscoveryService** object.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e3/v3/IR-yV4JaRiieELdRw0Zcxg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062016Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=A03362E692F64BF5D78E6F58803118E3AD21EEF45DAF347D9D98F9E9CDA42039)

To maximize the application running efficiency, most API calls are called asynchronously in callback or promise mode. The following code examples use the promise mode. For details about the APIs, see [MDNS Management](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-net-mdns).

The following describes the development procedure specific to each application scenario.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/41/v3/6cMxtjjVTUK8j0bzapgR6w/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062016Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=304782B4466BFE54A729DA584116E0DEB4CE6DB0814A04AAE0BE8D0092835173)

In the sample code provided in this topic, **this.context** is used to obtain the UIAbilityContext, where **this** indicates a UIAbility instance inherited from **UIAbility**. To use **UIAbilityContext** APIs on pages, see [Obtaining the Context of UIAbility](../../../../../application-framework/ability-kit/stage-model-development/stage-model-application-components/uiability-component/uiability-usage/document.md#obtaining-the-context-of-uiability).

#### Managing Local Services

1.  Connect the device to the Wi-Fi network.
2.  Import the **mdns**, **BusinessError**, and **common** namespaces from @kit.NetworkKit.

// Import the mdns namespace from @kit.NetworkKit.
import { mdns } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { common } from '@kit.AbilityKit';

1.  Call **addLocalService** to add a local service.

  // Create a LocalService object.
  private localServiceInfo: mdns.LocalServiceInfo = {
    serviceType: '\_print.\_tcp',
    serviceName: 'servicename',
    port: 5555,
    host: {
      address: '127.0.0.1'
    },
    serviceAttribute: \[{ key: '111', value: \[1\] }\]
  };
// ···
    let context: common.UIAbilityContext = this.getUIContext().getHostContext() as common.UIAbilityContext;
    // Call addLocalService to add a local service.
    mdns.addLocalService(context, this.localServiceInfo).then((data) => {
    // ···
      console.info(\`Local Service Added: ${JSON.stringify(data)}\`);
    })
    // ···

1.  (Optional) Call **resolveLocalService** to resolve the local service for the IP address of the local network.

// (Optional) Call resolveLocalService to resolve the local service.
mdns.resolveLocalService(context, this.localServiceInfo).then((data: mdns.LocalServiceInfo) => {
// ···
  console.info(\`Resolved Local Service: ${JSON.stringify(data)}\`);
})

1.  Call **removeLocalService** to remove the local service.

// Call removeLocalService to remove the local service.
mdns.removeLocalService(context, this.localServiceInfo).then((data: mdns.LocalServiceInfo) => {
// ···
  console.info(\`Local Service Removed: ${JSON.stringify(data)}\`);
})

#### Discovering Local Services

1.  Connect the device to the Wi-Fi network.
2.  Import the **mdns** namespace from **@kit.NetworkKit**.

// Import the mdns namespace from @kit.NetworkKit.
import { mdns } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { common } from '@kit.AbilityKit';

1.  Create a **DiscoveryService** object, which is used to discover MDNS services of the specified type.

let context: common.UIAbilityContext = this.getUIContext().getHostContext() as common.UIAbilityContext;
    
// ···
// Create a DiscoveryService object, which is used to discover mDNS services of the specified type.
let serviceType = '\_print.\_tcp';
let discoveryService = mdns.createDiscoveryService(context, serviceType);

1.  Subscribe to MDNS service discovery status changes.

// Subscribe to mDNS service discovery status changes.
discoveryService.on('discoveryStart', (data: mdns.DiscoveryEventInfo) => {
  console.info(JSON.stringify(data));
});
discoveryService.on('discoveryStop', (data: mdns.DiscoveryEventInfo) => {
  console.info(JSON.stringify(data));
});
discoveryService.on('serviceFound', (data: mdns.LocalServiceInfo) => {
  console.info(JSON.stringify(data));
// ···
});
discoveryService.on('serviceLost', (data: mdns.LocalServiceInfo) => {
  console.info(JSON.stringify(data));
// ···
});

1.  Enable discovery of MDNS services on the LAN.

// Enable discovery of mDNS services on the LAN.
discoveryService.startSearchingMDNS();

1.  Stop searching for MDNS services on the LAN.

// Stop searching for mDNS services on the LAN.
discoveryService.stopSearchingMDNS();

1.  Unsubscribe from MDNS service discovery status changes.

// Unsubscribe from mDNS service discovery status changes.
discoveryService.off('discoveryStart', (data: mdns.DiscoveryEventInfo) => {
  hilog.info(0x0000, 'testTag', JSON.stringify(data));
});
discoveryService.off('discoveryStop', (data: mdns.DiscoveryEventInfo) => {
  hilog.info(0x0000, 'testTag', JSON.stringify(data));
});
discoveryService.off('serviceFound', (data: mdns.LocalServiceInfo) => {
  hilog.info(0x0000, 'testTag', JSON.stringify(data));
  // ···
});
discoveryService.off('serviceLost', (data: mdns.LocalServiceInfo) => {
  hilog.info(0x0000, 'testTag', JSON.stringify(data));
  // ···
});
