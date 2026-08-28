# HCE Development

#### Introduction

Near Field Communication (NFC) is a short-range, high-frequency radio technology that operates at a frequency of 13.56 MHz, with a typical communication range of within 10 centimeters. Host Card Emulation (HCE) provides card emulation that does not depend on a secure element. It allows an application to emulate a card and communicate with an NFC card reader to complete NFC card swiping. Off Host Card Emulation (OFFHOST) is supported since API version 22. It simulates a card using a separate chip (called as the secure element or SE) on the device. Some SIM cards of wireless carriers contain SEs.

#### When to Use

An application emulates a card and communicates with an NFC card reader to complete NFC card swiping. The device can communicate with an NFC card reader by using a started application (foreground mode) or without starting an application (background mode).

-   HCE foreground card swiping
    
    In the foreground mode, the user has to start a specific application that communicates with the NFC card reader. Specifically, the user starts the application, opens the application page, and taps the device on the NFC card reader. In this case, the transaction data is distributed only to the foreground application. When the application switches to the background or exits, the foreground priority is also suspended.
    
-   HCE background card swiping
    
    The user taps the device on an NFC card reader without starting any HCE application. Then, the device selects an HCE application based on the Applet ID (AID, which complies with ISO/IEC 7816-4) provided by the NFC card reader, and completes the card swiping transaction. If multiple HCE applications are matched, an application selector will be displayed, listing all the available applications. In this case, the user needs to open the desired HCE application and tap the device on the NFC card reader again to trigger the card swiping transaction.
    

The SE emulates an NFC card and communicates with an NFC card reader to complete the NFC card swiping. The card to be emulated is configured in the SE through the application. When the device taps the NFC card reader, data is not processed by the device CPU, but is directly sent to the SE to complete the card swiping.

#### Constraints

1.  For security reasons, regardless of whether the HCE application performs card swiping in the foreground or background, the device does not support HCE card swiping operations when it is in the screen-off state.
    
2.  A device must be equipped with an NFC controller chip to support HCE card swiping capabilities. There are no constraints on whether it has an NFC secure element.
    
3.  An HCE application must declare the NFC card emulation permission. For specific details, see the sample code.
    

#### Available APIs

For details about the APIs and sample code, [NFC Card Emulation](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-cardemulation).

The following table describes the APIs for implementing HCE.

| API | Description |
| :-- | :-- |
| start(elementName: ElementName, aidList: string\[\]): void | Starts HCE, including enabling this application to run in the foreground preferentially and dynamically registering the AID list. |
| stop(elementName: ElementName): void | Stops HCE, including canceling the subscription of APDU data, exiting this application from the foreground, and releasing the dynamically registered AID list. |
| on(type: 'hceCmd', callback: AsyncCallback<number\[\]>): void | Registers a callback to receive APDUs from the peer card reader. |
| transmit(response: number\[\]): Promise<void> | Transmits APDU data to the peer card reader. |
| off(type: 'hceCmd', callback?: AsyncCallback<number\[\]>): void | Unsubscribes from events indicating receiving of APDUs from the peer card reader. |

#### Preparations

## Selecting Foreground or Background Card Swiping

HCE application developers can choose to implement either foreground or background card swiping based on service requirements. These two methods differ in their code implementation.

-   HCE foreground card swiping
    

1.  In the **module.json5** configuration file, there is no need to statically declare the Applet ID (AID, which complies with ISO/IEC 7816-4) selected by the NFC card reader. Instead, dynamically register an AID by using [start](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-cardemulation#start9).
2.  When the card swiping page of the HCE application exits, explicitly called [stop](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-cardemulation#stop9) to release the dynamically registered AID.

-   HCE background card swiping
    

1.  In the **module.json5** configuration file, statically declare the AID selected by the NFC card reader. Based on service requirements, specify whether the declared AID belongs to the **Payment** type or the **Other** type.
2.  If the **Payment** type is selected, the HCE application will appear in the NFC default payment application list on the system settings page. Users can only use background card swiping after selecting this HCE application as the default payment app. Since a default payment app is designated, there will be no conflicts between multiple HCE applications of the **Payment** type.
3.  If the **Other** type is selected, the HCE application will not appear in the NFC default payment app list on the system settings page. However, conflicts may arise if multiple HCE applications declare the same AID of the **Other** type.
4.  When implementing HCE background card swiping, you do not need to call the **start** and **stop** APIs.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/24/v3/GY0NLE1qQWeJkXi1WDKzxw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062014Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=3042D5010BEA9B615951655398912333DE18F8B1520922CEC2ACAE24B0BB5DDA)

-   Starting from API version 9, application development supports the Stage model, which is recommended for long-term evolution.
-   All the HCE sample code in this document is based on the Stage model.

#### How to Develop

## HCE Foreground Card Swiping

1.  Declare the permission required for NFC card emulation and HCE action in the **module.json5** file.
2.  Import modules.
3.  Check whether the device supports the NFC and HCE capabilities.
4.  Enable the foreground HCE application to preferentially process NFC card swiping.
5.  Subscribe to the HCE APDU receiving events.
6.  Receive and send APDU data for HCE card swiping.
7.  Exit the HCE foreground mode when the application exits the NFC card swiping page.

    "abilities": \[
      {
        "name": "EntryAbility",
        "srcEntry": "./ets/entryability/EntryAbility.ts",
        "description": "$string:EntryAbility\_desc",
        "icon": "$media:icon",
        "label": "$string:EntryAbility\_label",
        "startWindowIcon": "$media:icon",
        "startWindowBackground": "$color:start\_window\_background",
        "exported": true,
        "skills": \[
          {
            "entities": \[
              "entity.system.home"
            \],
            "actions": \[
              "ohos.want.action.home",

              // The \*\*actions\*\* field must contain "ohos.nfc.cardemulation.action.HOST\_APDU\_SERVICE".
              "ohos.nfc.cardemulation.action.HOST\_APDU\_SERVICE"
            \]
          }
        \]
      }
    \],
    "requestPermissions": \[
      {
        // Add the permission required for NFC card emulation.
        "name": "ohos.permission.NFC\_CARD\_EMULATION",
        "reason": "$string:app\_name",
      }
    \]

import { cardEmulation } from '@kit.ConnectivityKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { AsyncCallback } from '@kit.BasicServicesKit';
import { AbilityConstant, UIAbility, Want, bundleManager } from '@kit.AbilityKit';

let hceElementName: bundleManager.ElementName;
let hceService: cardEmulation.HceService;

const hceCommandCb: AsyncCallback<number\[\]> = (error: BusinessError, hceCommand: number\[\]) => {
  if (!error) {
    if (hceCommand == null) {
      hilog.error(0x0000, 'testTag', 'hceCommandCb has invalid hceCommand.');
      return;
    }
    // The application checks the content of the received command and sends the matching response data based on its own service implementation.
    hilog.info(0x0000, 'testTag', 'hceCommand = %{public}s', JSON.stringify(hceCommand));
    let responseData = \[0x90, 0x00\]; // Change the response data based on the received command.
    hceService.transmit(responseData).then(() => {
      hilog.info(0x0000, 'testTag', 'hceService transmit Promise success.');
    }).catch((err: BusinessError) => {
      hilog.error(0x0000, 'testTag', 'hceService transmit Promise error = %{public}s', JSON.stringify(err));
    });
  } else {
    hilog.error(0x0000, 'testTag', 'hceCommandCb error %{public}s', JSON.stringify(error));
  }
}

export default class EntryAbility extends UIAbility {
  onCreate(want: Want, launchParam: AbilityConstant.LaunchParam) {
    hilog.info(0x0000, 'testTag', '%{public}s', 'Ability onCreate');

    // Check whether the device supports the NFC and HCE capabilities.
    if (!canIUse("SystemCapability.Communication.NFC.Core")) {
      hilog.error(0x0000, 'testTag', 'nfc unavailable.');
      return;
    }
    if (!cardEmulation.hasHceCapability()) {
      hilog.error(0x0000, 'testTag', 'hce unavailable.');
      return;
    }

    // hceElementName cannot be empty. You can obtain elementName of the application through Want or fill in elementName based on the application information.
    hceElementName = {
      bundleName: want.bundleName ?? '',
      abilityName: want.abilityName ?? '',
      moduleName: want.moduleName,
    }
    hceService = new cardEmulation.HceService();
  }

  onForeground() {
    // Switch the application to the foreground.
    hilog.info(0x0000, 'testTag', '%{public}s', 'Ability onForeground');
    if (hceElementName != undefined) {
      try {
        // Enable the foreground HCE application to preferentially process NFC card swiping.
        let aidList = \["A0000000031010", "A0000000031011"\]; // Set the AID list correctly.
        hceService.start(hceElementName, aidList);

        // Subscribe to the HCE APDU receiving events.
        hceService.on('hceCmd', hceCommandCb);
      } catch (error) {
        hilog.error(0x0000, 'testTag', 'hceService.start error = %{public}s', JSON.stringify(error));
      }
    }
  }

  onBackground() {
    // Switch the application to the background.
    hilog.info(0x0000, 'testTag', '%{public}s', 'Ability onBackground');
    // Switch the application to the foreground and stop HCE.
    if (hceElementName != undefined) {
      try {
        hceService.stop(hceElementName);
      } catch (error) {
        hilog.error(0x0000, 'testTag', 'hceService.stop error = %{public}s', JSON.stringify(error));
      }
    }
  }
}

## HCE background card swiping

1.  Declare the permission required for NFC card emulation, HCE action, and AIDs for application matching in the **module.json5** file.
2.  Import modules.
3.  Check whether the device supports the NFC and HCE capabilities.
4.  Subscribe to the HCE APDU receiving events.
5.  Receive and send APDU data for HCE card swiping.
6.  Cancel the subscription when the application exits.

    "abilities": \[
      {
        "name": "EntryAbility",
        "srcEntry": "./ets/entryability/EntryAbility.ts",
        "description": "$string:EntryAbility\_desc",
        "icon": "$media:icon",
        "label": "$string:EntryAbility\_label",
        "startWindowIcon": "$media:icon",
        "startWindowBackground": "$color:start\_window\_background",
        "exported": true,
        "skills": \[
          {
            "entities": \[
              "entity.system.home"
            \],
            "actions": \[
              "ohos.want.action.home",

              // The \*\*actions\*\* field must contain "ohos.nfc.cardemulation.action.HOST\_APDU\_SERVICE".
              "ohos.nfc.cardemulation.action.HOST\_APDU\_SERVICE"
            \]
          }
        \],

        // Define at least one AID of the Payment or Other type based on service requirements.
        "metadata": \[
          {
            "name": "payment-aid",
            "value": "A0000000031010" // Define the AID of the Payment type.
          },
          {
            "name": "other-aid",
            "value": "A0000000031011" // Define the AID of the Other type.
          }
        \]
      }
    \],
    "requestPermissions": \[
      {
        // Add the permission required for NFC card emulation.
        "name": "ohos.permission.NFC\_CARD\_EMULATION",
        "reason": "$string:app\_name",
      }
    \]

import { cardEmulation } from '@kit.ConnectivityKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { AsyncCallback } from '@kit.BasicServicesKit';
import { AbilityConstant, UIAbility, Want, bundleManager } from '@kit.AbilityKit';

let hceElementName: bundleManager.ElementName;
let hceService: cardEmulation.HceService;

const hceCommandCb: AsyncCallback<number\[\]> = (error: BusinessError, hceCommand: number\[\]) => {
  if (!error) {
    if (hceCommand == null) {
      hilog.error(0x0000, 'testTag', 'hceCommandCb has invalid hceCommand.');
      return;
    }

    // The application checks the content of the received command and sends the matching response data based on its own service implementation.
    hilog.info(0x0000, 'testTag', 'hceCommand = %{public}s', JSON.stringify(hceCommand));
    let responseData = \[0x90, 0x00\]; // Change the response data based on the received command.
    hceService.transmit(responseData).then(() => {
      hilog.info(0x0000, 'testTag', 'hceService transmit Promise success.');
    }).catch((err: BusinessError) => {
      hilog.error(0x0000, 'testTag', 'hceService transmit Promise error = %{public}s', JSON.stringify(err));
    });
  } else {
    hilog.error(0x0000, 'testTag', 'hceCommandCb error %{public}s', JSON.stringify(error));
  }
}

export default class EntryAbility extends UIAbility {
  onCreate(want: Want, launchParam: AbilityConstant.LaunchParam) {
    hilog.info(0x0000, 'testTag', '%{public}s', 'Ability onCreate');

    // Check whether the device supports the NFC and HCE capabilities.
    if (!canIUse("SystemCapability.Communication.NFC.Core")) {
      hilog.error(0x0000, 'testTag', 'nfc unavailable.');
      return;
    }
    if (!cardEmulation.hasHceCapability()) {
      hilog.error(0x0000, 'testTag', 'hce unavailable.');
      return;
    }

    // Subscribe to HCE card swiping data when the application is running in the foreground.
    hceService = new cardEmulation.HceService();
    hceService.on('hceCmd', hceCommandCb);
  }

  onForeground() {
    // Switch the application to the foreground.
    hilog.info(0x0000, 'testTag', '%{public}s', 'Ability onForeground');
  }

  onDestroy() {
    hilog.info(0x0000, 'testTag', '%{public}s', 'Ability onDestroy');
    // Unsubscribe from HCE card swiping data when the application exits.
    hceService.off('hceCmd', hceCommandCb);
  }
}

## OFFHOST Card Swipping

1.  Declare the OFFHOST action, AIDs for application matching, and SEs in the **module.json5** file.
2.  Set the OFFHOST application as the default payment application.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2a/v3/MUYYD4rcSAm0upE9-Vt-rQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062014Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=F679A00EA1DE12D042FA01D64683D6F62AC6BFC52FD97206482109018940E7B4)

-   OFFHOST is supported since API version 22.
-   Only the AID of the **Payment** type is supported.
-   Only the SIM card can be used as the SE.

"abilities": \[
      {
        "name": "EntryAbility",
        "srcEntry": "./ets/entryability/EntryAbility.ts",
        "description": "$string:EntryAbility\_desc",
        "icon": "$media:icon",
        "label": "$string:EntryAbility\_label",
        "startWindowIcon": "$media:icon",
        "startWindowBackground": "$color:start\_window\_background",
        "exported": true,
        "skills": \[
          {
            "entities": \[
              "entity.system.home"
            \],
            "actions": \[
              "ohos.want.action.home",

              // The \*\*actions\*\* field must contain "ohos.nfc.cardemulation.action.OFF\_HOST\_APDU\_SERVICE".
              "ohos.nfc.cardemulation.action.OFF\_HOST\_APDU\_SERVICE"
            \]
          }
        \]
        // Define at least one AID of the Payment type based on service requirements.
        "metadata": \[
          {
            "name": "payment-aid",
            "value": "A0000000031010" // Define the AID of the Payment type. The AID must be correct.
          },
           {
             "name": "secureElement",
             "value": "SIM" //Define secureElement.
            },
        \]
      }
    \]
