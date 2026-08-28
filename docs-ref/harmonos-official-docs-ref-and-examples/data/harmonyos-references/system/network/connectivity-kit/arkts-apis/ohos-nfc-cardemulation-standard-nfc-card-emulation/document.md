# @ohos.nfc.cardEmulation (Standard NFC Card Emulation)

The **cardEmulation** module implements Near-Field Communication (NFC) card emulation. You can use the APIs provided by this module to determine the card emulation type supported and implement Host Card Emulation (HCE).

HCE provides card emulation that does not depend on a secure element. It allows an application to emulate a card and communicate with an NFC card reader through the NFC service.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ff/v3/bfo2cWI0TfCgGGXO83mNsg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062341Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=A51CD9C9B0B8C9875E4CED5E104C8B4EFA1A03A25D33FCE8A60770B73EC23B74)

The initial APIs of this module are supported since API version 6. Newly added APIs will be marked with a superscript to indicate their earliest API version.

#### HCE and AID Declaration

Before developing an application related to HCE, you must declare NFC-related attributes in the **module.json5** file.

// Applicable to devices other than lite wearables
{
  "module": {
    // Other declared attributes
    "abilities": \[
      {
        // Other declared attributes
        "skills": \[
          {
            "actions": \[
              "ohos.nfc.cardemulation.action.HOST\_APDU\_SERVICE"
            \]
          }
        \],
        "metadata": \[
          {
            "name": "payment-aid",
            "value": "your payment aid"
          },
          {
            "name": "other-aid",
            "value": "your other aid"
          }
        \]
      }
    \],
    "requestPermissions": \[
      {
        "name": "ohos.permission.NFC\_CARD\_EMULATION",
        // Set reason to card\_emulation\_reason.
        "reason": "$string:card\_emulation\_reason"
      }
    \]
  }
}

// Applicable to lite wearables
{
  "module": {
    // Other declared attributes
    "abilities": \[
      {
        // Other declared attributes
        "metaData": {
          "customizeData": \[
            {
              "name": "paymentAid",
              "value": "A0000000041012"
            },
            {
              "name": "otherAid",
              "value": "A0000000041010"
            }
          \]
        },
        "skills": \[
          {
            "entities": \[
              "ohos.nfc.cardemulation.action.HOST\_APDU\_SERVICE"
            \],
            "actions": \[
              "ohos.nfc.cardemulation.action.HOST\_APDU\_SERVICE"
            \]
          }
        \]
      }
    \],
    "reqPermissions": \[
      {
        "name": "ohos.permission.NFC\_CARD\_EMULATION",
        // Set reason to card\_emulation\_reason.
        "reason": "$string:card\_emulation\_reason",
        "usedScene":{
          "ability":\[
            "FormAbility"
          \],
          "when":"always"
        }
      },
      {
        "name": "ohos.permission.NFC\_TAG",
        // Set reason to card\_emulation\_reason.
        "reason": "$string:card\_emulation\_reason",
        "usedScene":{
          "ability":\[
            "FormAbility"
          \],
          "when":"always"
        }
      }
    \]
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/dc/v3/eOARR64NSn2OKITZAk9tEg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062341Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=9FEE0060C76CB919D51B1CA609D513AB5B82A3258ADF5D0858656AC796BEE37C)

1.  The **actions** field must contain **ohos.nfc.cardemulation.action.HOST\_APDU\_SERVICE** and cannot be changed.
2.  When declaring an AID (in compliance with ISO/IEC 7816-4), ensure that **name** is set to **payment-aid** or **other-aid**. Incorrect setting will cause a parsing failure.
3.  The **name** field of **requestPermissions** must be **ohos.permission.NFC\_CARD\_EMULATION** and cannot be changed.
4.  Lite wearables support only the FA model, with attribute configurations and API invocation methods differing from those of other device types. Refer to the example code for detailed implementations.

#### Modules to Import

// Applicable to devices other than lite wearables
import { cardEmulation } from '@kit.ConnectivityKit';

// Applicable to lite wearables
import cardEmulation from '@ohos.nfc.cardEmulation';

#### FeatureType(deprecated)

Enumerates the NFC card emulation types.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/22/v3/ZOYw6Al0TByCcn6SCV_NsQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062341Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=89C17FBEF1BC3EF92D50052245975B2537B3D8088BF7039BEA4FA2546B827305)

This API is supported since API version 6 and deprecated since API version 9. Use [hasHceCapability](#cardemulationhashcecapability9) instead.

**System capability**: SystemCapability.Communication.NFC.CardEmulation

| Name | Value | Description |
| :-- | :-- | :-- |
| HCE | 0 | HCE. |
| UICC | 1 | Subscriber identity module (SIM) card emulation. |
| ESE | 2 | Embedded Secure Element (eSE) emulation. |

#### CardType9+

Enumerates the types of services used by the card emulation application.

**System capability**: SystemCapability.Communication.NFC.CardEmulation

**Atomic service API**: This API can be used in atomic services since API version 12.

| Name | Value | Description |
| :-- | :-- | :-- |
| PAYMENT | "payment" | Payment service. |
| OTHER | "other" | Other services. |

#### cardEmulation.isSupported(deprecated)

isSupported(feature: number): boolean

Checks whether a certain type of card emulation is supported.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/73/v3/Ndt-5J3YRXeF3ux1F0oVqg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062341Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=409DD20A611FDD2F8A7EA811B3149C714099085ABD0842FC32C7FACBEE37A759)

This API is supported since API version 6 and deprecated since API version 9. Use [hasHceCapability](#cardemulationhashcecapability9) instead.

**System capability**: SystemCapability.Communication.NFC.CardEmulation

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| feature | number | Yes | Card emulation type to check. For details, see [FeatureType](#featuretypedeprecated). |

**Return value**

| **Type** | **Description** |
| :-- | :-- |
| boolean | Returns **true** if the card emulation type is supported; returns **false** otherwise. |

**Example**

// Applicable to devices other than lite wearables
import { cardEmulation } from '@kit.ConnectivityKit';

let isHceSupported: boolean = cardEmulation.isSupported(cardEmulation.FeatureType.HCE);
if (!isHceSupported) {
    console.info('this device is not supported for HCE, ignore it.');
}

// Applicable to lite wearables
import cardEmulation from '@ohos.nfc.cardEmulation';

let isHceSupported = cardEmulation.isSupported(cardEmulation.FeatureType.HCE);
if (!isHceSupported) {
    console.error('this device is not supported for HCE, ignore it.');
}

#### cardEmulation.hasHceCapability9+

hasHceCapability(): boolean

Checks whether the device supports HCE.

**System capability**: SystemCapability.Communication.NFC.CardEmulation

**Required permissions**: ohos.permission.NFC\_CARD\_EMULATION

**Atomic service API**: This API can be used in atomic services since API version 12.

**Return value**

| **Type** | **Description** |
| :-- | :-- |
| boolean | Returns **true** if HCE is supported; returns **false** otherwise. |

**Error codes**

For details about the error codes, see [NFC Error Codes](../../error-codes/nfc-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 201 | Permission denied. |
| 801 | Capability not supported. |

**Example**

// Applicable to devices other than lite wearables
import { cardEmulation } from '@kit.ConnectivityKit';

let hasHceCap: boolean = cardEmulation.hasHceCapability();
if (!hasHceCap) {
    console.error('this device hasHceCapability false, ignore it.');
}

// Applicable to lite wearables
import cardEmulation from '@ohos.nfc.cardEmulation';

let hasHceCap = cardEmulation.hasHceCapability();
if (!hasHceCap) {
    console.error('this device hasHceCapability false, ignore it.');
}

#### cardEmulation.isDefaultService9+

isDefaultService(elementName: ElementName, type: CardType): boolean

Checks whether an application is the default application of the specified service type.

**System capability**: SystemCapability.Communication.NFC.CardEmulation

**Required permissions**: ohos.permission.NFC\_CARD\_EMULATION

**Atomic service API**: This API can be used in atomic services since API version 12.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| elementName | [ElementName](../../../../../application-framework/ability-kit/arkts-apis/dependent-elements-and-definitions/bundlemanager/elementname/document.md) | Yes | Information about the page, on which the application declares the NFC card emulation capability. It must contain at least **bundleName** and **abilityName** and cannot be empty. |
| type | [CardType](#cardtype9) | Yes | Card emulation service type. Currently, only the default payment application can be queried. |

**Return value**

| **Type** | **Description** |
| :-- | :-- |
| boolean | Returns **true** if the application is the default payment application; returns **false** otherwise. |

**Error codes**

For details about the error codes, see [NFC Error Codes](../../error-codes/nfc-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 201 | Permission denied. |
| 401 | 
The parameter check failed. Possible causes:

1\. Mandatory parameters are left unspecified.

2\. Incorrect parameters types.

3\. Parameter verification failed.

 |
| 801 | Capability not supported. |

**Example**

// Applicable to devices other than lite wearables
import { cardEmulation } from '@kit.ConnectivityKit';
import { bundleManager, Want } from '@kit.AbilityKit';

// Initialize elementName, bundleName, and abilityName and set their values correctly based on the actual application information.
let elementName: bundleManager.ElementName = {
  bundleName: "com.example.myapplication",
  moduleName: "entry",
  abilityName: "EntryAbility"
};

let isDefaultService: boolean = cardEmulation.isDefaultService(elementName, cardEmulation.CardType.PAYMENT);

// Applicable to lite wearables
import cardEmulation from '@ohos.nfc.cardEmulation';

let appName = "com.example.testquestionlite";
let isDefaultService = cardEmulation.isDefaultService(appName, cardEmulation.CardType.PAYMENT);

#### HceService8+

Provides APIs for implementing HCE, including receiving Application Protocol Data Units (APDUs) from the peer card reader and sending a response. Before using HCE-related APIs, check whether the device supports HCE.

#### \[h2\]startHCE(deprecated)

startHCE(aidList: string\[\]): boolean

Starts HCE, including enabling this application to run in the foreground preferentially and dynamically registering the AID list.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3b/v3/gOP5ATRySF6ovyQ_Jo14Hw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062341Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=954D474F0F0D57A49A6445040A5F24798039D1A63E8C95D2BB4FC5655F3F1ECD)

This API is supported since API version 8 and deprecated since API version 9. Use [start](#start9) instead.

**Required permissions**: ohos.permission.NFC\_CARD\_EMULATION

**System capability**: SystemCapability.Communication.NFC.CardEmulation

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| aidList | string\[\] | Yes | List of AIDs to register. |

**Return value**

| **Type** | **Description** |
| :-- | :-- |
| boolean | Returns **true** if HCE is started or has been started; returns **false** otherwise. |

#### \[h2\]start9+

start(elementName: [ElementName](../../../../../application-framework/ability-kit/arkts-apis/dependent-elements-and-definitions/bundlemanager/elementname/document.md), aidList: string\[\]): void

Starts HCE, including enabling this application to run in the foreground preferentially and dynamically registering the AID list.

**Required permissions**: ohos.permission.NFC\_CARD\_EMULATION

**System capability**: SystemCapability.Communication.NFC.CardEmulation

**Atomic service API**: This API can be used in atomic services since API version 12.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| elementName | [ElementName](../../../../../application-framework/ability-kit/arkts-apis/dependent-elements-and-definitions/bundlemanager/elementname/document.md) | Yes | Information about the page, on which the application declares the NFC card emulation capability. It must contain at least **bundleName** and **abilityName** and cannot be empty. |
| aidList | string\[\] | Yes | List of AIDs to register. This parameter can be left empty. |

**Error codes**

For details about the error codes, see [NFC Error Codes](../../error-codes/nfc-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 201 | Permission denied. |
| 401 | 
The parameter check failed. Possible causes:

1\. Mandatory parameters are left unspecified.

2\. Incorrect parameters types.

3\. Parameter verification failed.

 |
| 801 | Capability not supported. |
| 3100301 | Card emulation running state is abnormal in service. |

#### \[h2\]stopHCE(deprecated)

stopHCE(): boolean

Stops HCE, including exiting the current application from the foreground, releasing the dynamically registered AID list, and canceling the subscription of **hceCmd**.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f4/v3/gTsOoux0TPWUZRMO7Mmt5Q/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062341Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=B19A73AFF9650CDC5B553C1F3C47AD7864F1493809A473D33EE688070924A9AA)

This API is supported since API version 8 and deprecated since API version 9. Use [stop](#stop9) instead.

**Required permissions**: ohos.permission.NFC\_CARD\_EMULATION

**System capability**: SystemCapability.Communication.NFC.CardEmulation

**Return value**

| **Type** | **Description** |
| :-- | :-- |
| boolean | **true** if HCE is stopped or disabled; **false** otherwise. |

**Example**

For details, see the example of [on](#on8).

#### \[h2\]stop9+

stop(elementName: [ElementName](../../../../../application-framework/ability-kit/arkts-apis/dependent-elements-and-definitions/bundlemanager/elementname/document.md)): void

Stops HCE, including canceling the subscription of APDU data, exiting this application from the foreground, and releasing the dynamically registered AID list. The application needs to call this API in **onDestroy** of the HCE page.

**Required permissions**: ohos.permission.NFC\_CARD\_EMULATION

**System capability**: SystemCapability.Communication.NFC.CardEmulation

**Atomic service API**: This API can be used in atomic services since API version 12.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| elementName | [ElementName](../../../../../application-framework/ability-kit/arkts-apis/dependent-elements-and-definitions/bundlemanager/elementname/document.md) | Yes | Information about the page, on which the application declares the NFC card emulation capability. It must contain at least **bundleName** and **abilityName** and cannot be empty. |

**Error codes**

For details about the error codes, see [NFC Error Codes](../../error-codes/nfc-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 201 | Permission denied. |
| 401 | 
The parameter check failed. Possible causes:

1\. Mandatory parameters are left unspecified.

2\. Incorrect parameters types.

3\. Parameter verification failed.

 |
| 801 | Capability not supported. |
| 3100301 | Card emulation running state is abnormal in service. |

#### \[h2\]on8+

on(type: 'hceCmd', callback: AsyncCallback<number\[\]>): void

Subscribes to events indicating receiving of APDUs from the peer card reader. The application needs to call this API in **onCreate()** of the HCE page. This API uses an asynchronous callback to return the result.

**Required permissions**: ohos.permission.NFC\_CARD\_EMULATION

**System capability**: SystemCapability.Communication.NFC.CardEmulation

**Atomic service API**: This API can be used in atomic services since API version 12.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Event type. It has a fixed value of **hceCmd**. |
| callback | AsyncCallback<number\[\]> | Yes | Event callback used to return the data array that complies with the APDU. Each number is represented in hexadecimal notation, with values ranging from 0x00 to 0xFF. |

**Error codes**

For details about the error codes, see [NFC Error Codes](../../error-codes/nfc-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 201 | Permission denied. |
| 401 | Invalid parameter. |
| 801 | Capability not supported. |

**Example**

// Applicable to devices other than lite wearables
import { hilog } from '@kit.PerformanceAnalysisKit';
import { cardEmulation } from '@kit.ConnectivityKit';
import { AsyncCallback } from '@kit.BasicServicesKit';
import { ElementName } from './bundleManager/ElementName'
import { AbilityConstant, UIAbility, Want } from '@kit.AbilityKit';

let hceService: cardEmulation.HceService = new cardEmulation.HceService();
let element: ElementName;

export default class EntryAbility extends UIAbility {
  onCreate(want: Want, param: AbilityConstant.LaunchParam) {
    hilog.info(0x0000, 'testHce', '%{public}s', 'Ability onCreate');
    element = {
      bundleName: want.bundleName ?? '',
      abilityName: want.abilityName ?? '',
      moduleName: want.moduleName
    }
    const apduCallback: AsyncCallback<number\[\]> = (err, data) => {
      // Implement data processing and handle exceptions.
      console.info("got apdu data");
    };
    hceService.on('hceCmd', apduCallback);
  }
  onDestroy() {
    hilog.info(0x0000, 'testHce', '%{public}s', 'Ability onDestroy');
    hceService.stop(element);
  }
  // Implement other lifecycle functions as demanded.
}

**Example**

// Applicable to lite wearables
import cardEmulation from '@ohos.nfc.cardEmulation';

let appName = "com.example.testquestionlite";

export default {
  data:{
    fontSize: '30px',
    fontColor: '#50609f',
    hide: 'show',
    headCon: appName,
    paymentAid: \["A0000000041010", "A0000000041012"\]
  },
  onCreate() {
    console.info('onCreate');
  },
  onReady() {
    cardEmulation.hasHceCapability();
    cardEmulation.isDefaultService(appName, cardEmulation.CardType.PAYMENT);
    cardEmulation.isDefaultService(appName, cardEmulation.CardType.OTHER);
    let HceService = new cardEmulation.HceService();

    HceService.start(appName, this.paymentAid);
    HceService.on("hceCmd", (data) => {
      console.info('data:' + data);
      // Data to be sent by the application. The following data is for reference only.
      let responseData = \[0x1, 0x2\];
      HceService.transmit(responseData, () => {
        console.info('sendResponse start');
      });
      console.info('sendResponse end');
    });
  },
  onDestroy() {
  }
  // Implement other lifecycle functions as demanded.
}

#### \[h2\]off18+

off(type: 'hceCmd', callback?: AsyncCallback<number\[\]>): void

Unsubscribes from events indicating receiving of APDUs from the peer card reader. This API uses an asynchronous callback to return the result.

**Required permissions**: ohos.permission.NFC\_CARD\_EMULATION

**System capability**: SystemCapability.Communication.NFC.CardEmulation

**Atomic service API**: This API can be used in atomic services since API version 18.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Event type. It has a fixed value of **hceCmd**. |
| callback | AsyncCallback<number\[\]> | No | Event callback. Each number is represented in hexadecimal notation, with values ranging from 0x00 to 0xFF. |

**Error codes**

For details about the error codes, see [NFC Error Codes](../../error-codes/nfc-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 201 | Permission denied. |
| 801 | Capability not supported. |

**Example**

// Applicable to devices other than lite wearables
import { hilog } from '@kit.PerformanceAnalysisKit';
import { cardEmulation } from '@kit.ConnectivityKit';
import { AsyncCallback } from '@kit.BasicServicesKit';
import { ElementName } from './bundleManager/ElementName'
import { AbilityConstant, UIAbility, Want } from '@kit.AbilityKit';

let hceService: cardEmulation.HceService = new cardEmulation.HceService();
let element: ElementName;
const apduCallback: AsyncCallback<number\[\]> = (err, data) => {
  // Implement data processing and handle exceptions.
  console.info("AsyncCallback got apdu data");
};

export default class EntryAbility extends UIAbility {
  onCreate(want: Want, param: AbilityConstant.LaunchParam) {
    hilog.info(0x0000, 'testHce', '%{public}s', 'Ability onCreate');
    element = {
      bundleName: want.bundleName ?? '',
      abilityName: want.abilityName ?? '',
      moduleName: want.moduleName
    }
    hceService.on('hceCmd', apduCallback);
  }
  onDestroy() {
    hilog.info(0x0000, 'testHce', '%{public}s', 'Ability onDestroy');
    hceService.off('hceCmd', apduCallback);
    hceService.stop(element);
  }
  // Implement other lifecycle functions as demanded.
}

#### \[h2\]sendResponse(deprecated)

sendResponse(responseApdu: number\[\]): void

Sends a response to the peer card reader.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2d/v3/xo3G7Y_WTi-mc8fyvKZ8_w/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062341Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=843708E97BE8E58A874986DADF67E3F3CB4A429C078485425C70B80D1B3780DA)

This API is supported since API version 8 and deprecated since API version 9. Use [transmit](#transmit9) instead.

**Required permissions**: ohos.permission.NFC\_CARD\_EMULATION

**System capability**: SystemCapability.Communication.NFC.CardEmulation

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| responseApdu | number\[\] | Yes | Response APDU sent to the peer card reader. The value consists of hexadecimal numbers ranging from **0x00** to **0xFF**. |

#### \[h2\]transmit9+

transmit(response: number\[\]): Promise<void>

Transmits an APDU to the peer card reader. This API uses a promise to return the result. The application calls this API only after receiving an APDU sent by the card reader via [on](#on8).

**Required permissions**: ohos.permission.NFC\_CARD\_EMULATION

**System capability**: SystemCapability.Communication.NFC.CardEmulation

**Atomic service API**: This API can be used in atomic services since API version 12.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| response | number\[\] | Yes | Response APDU sent to the peer card reader. The value consists of hexadecimal numbers ranging from **0x00** to **0xFF**. |

**Return value**

| **Type** | **Description** |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Error codes**

For details about the error codes, see [NFC Error Codes](../../error-codes/nfc-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 201 | Permission denied. |
| 401 | 
The parameter check failed. Possible causes:

1\. Mandatory parameters are left unspecified.

2\. Incorrect parameters types.

3\. Parameter verification failed.

 |
| 801 | Capability not supported. |
| 3100301 | Card emulation running state is abnormal in service. |

**Example**

// Applicable to devices other than lite wearables
import { cardEmulation } from '@kit.ConnectivityKit';
import { BusinessError } from '@kit.BasicServicesKit';

let hceService: cardEmulation.HceService = new cardEmulation.HceService();

// Data to be sent by the application. The following data is for reference only.
const responseData = \[0x1, 0x2\];
hceService.transmit(responseData).then(() => {
  // Process the promise.
  console.info("transmit Promise success.");
}).catch((err: BusinessError) => {
  console.error("transmit Promise error:", err);
});

// Applicable to lite wearables
import cardEmulation from '@ohos.nfc.cardEmulation';

let hceService = new cardEmulation.HceService();

// Data to be sent by the application. The following data is for reference only.
let responseData = \[0x1, 0x2\];
hceService.transmit(responseData).then(() => {
  // Process the promise.
  console.info("transmit Promise success.");
});
console.info("transmit Promise end.");

#### \[h2\]transmit9+

transmit(response: number\[\], callback: AsyncCallback<void>): void

Sends APDU data to the peer card reader. The application can call this API only after receiving an APDU sent by the card reader via [on](#on8). This API uses an asynchronous callback to return the result.

**Required permissions**: ohos.permission.NFC\_CARD\_EMULATION

**System capability**: SystemCapability.Communication.NFC.CardEmulation

**Atomic service API**: This API can be used in atomic services since API version 12.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| response | number\[\] | Yes | Response APDU sent to the peer card reader. The value consists of hexadecimal numbers ranging from **0x00** to **0xFF**. |
| callback | AsyncCallback<void> | Yes | Callback used to return the operation result. If the operation is successful, **err** is **undefined**; otherwise, **err** is an error object. |

**Error codes**

For details about the error codes, see [NFC Error Codes](../../error-codes/nfc-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 201 | Permission denied. |
| 401 | 
The parameter check failed. Possible causes:

1\. Mandatory parameters are left unspecified.

2\. Incorrect parameters types.

3\. Parameter verification failed.

 |
| 801 | Capability not supported. |
| 3100301 | Card emulation running state is abnormal in service. |

**Example**

// Applicable to devices other than lite wearables
import { cardEmulation } from '@kit.ConnectivityKit';
import { BusinessError } from '@kit.BasicServicesKit';

let hceService: cardEmulation.HceService = new cardEmulation.HceService();

// Data to be sent by the application. The following data is for reference only.
try {
  const responseData = \[0x1, 0x2\];

  hceService.transmit(responseData, (err : BusinessError)=> {
    if (err) {
      console.error(\`transmit AsyncCallback err Code: ${err.code}, message: ${err.message}\`);
    } else {
      console.info("transmit AsyncCallback success.");
    }
  });
} catch (error) {
  console.error(\`transmit AsyncCallback catch Code: ${(error as BusinessError).code}, \` +
    \`message: ${(error as BusinessError).message}\`);
}

// Applicable to lite wearables
import cardEmulation from '@ohos.nfc.cardEmulation';

let hceService = new cardEmulation.HceService();

// Data to be sent by the application. The following data is for reference only.
let responseData = \[0x1, 0x2\];
hceService.transmit(responseData, () => {
  console.info("transmit Promise success.");
});
console.info("transmit Promise end.");
