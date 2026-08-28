# Extensible Authentication

#### Overview

Extensible authentication is a mechanism provided by the **eap** module to enable third-party clients to participate in custom 802.1X (a port-based network access control protocol) authentication, such as Extensible Authentication Protocol (EAP) authentication.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/23/v3/y_-AI8uKSeWGEotglTFrVg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062016Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=1EF67B9726F76D1CBA11370C0E248292908BDA201283B0EE219EB92B61515C80)

This functionality is supported since API version 20.

To implement extensible authentication, the clients should be able to:

1.  Encapsulate private data into EAP protocol packets based on the data structure agreed upon by the client and authentication server.
2.  During the authentication, perform custom actions such as security check scanning on the local host, and send an authentication response after the custom action is complete.
    
    The OS is required to provide a mechanism for third-party clients to participate in 802.1X authentication.
    

To meet the preceding requirements, the custom 802.1X authentication mechanism should be able to support:

1.  Customizing the listening for 802.1X packets and adapt the packet exchange process.
2.  Initiating 802.1X authentication and deauthentication on the **eth** network port.

#### When to Use

Typical application scenarios of the custom 802.1X authentication include:

1.  For enterprise network management applications, custom security verification needs to be added to the enterprise Wi-Fi's 802.1X authentication process to access the enterprise intranet. The required functions include:
    
    -   Customization of the packet type and EAP type for custom authentication.
    -   Setting of the standard authentication result based on the custom authentication result.
2.  For enterprise network management applications, 802.1X authentication needs to be implemented on the **eth** network port to access the enterprise intranet. The required functions include:
    
    -   Support for the standard 802.1X authentication process.
    -   Customization of the 802.1X authentication process.

The following describes the development procedure specific to each application scenario.

#### Adding Custom Security Verification to the 802.1X Authentication Process

1.  Import the **eap** namespace from **@kit.NetworkKit**.

import { eap } from '@kit.NetworkKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

1.  Call [regCustomEapHandler](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-net-eap#eapregcustomeaphandler) to register the EAP packet types to listen for.
    
    During 802.1X authentication, the system will encapsulate the eligible EAP packets into the callback function (for example, the **eapData** function in the sample code) for enterprise applications to retrieve. After the packets are encapsulated into the callback function,
    
    the 802.1X authentication process will be blocked so that the enterprise applications can retrieve the complete packet content.
    
    (1) If the packets of the registered packet type (that is, eapCode=1) are sent from the server to the client, they include the custom content added by the server. Determine whether to continue the subsequent steps based on the custom content, and call [replyCustomEapData](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-net-eap#eapreplycustomeapdata) to send the packets to the system.
    
    (2) If the packets of the registered packet type (that is, eapCode=2) are sent from the client to the server, they are the original 802.1X authentication packets. Add the custom content to the original packets, and then call [replyCustomEapData](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-net-eap#eapreplycustomeapdata) to send the packets to the system.
    
    (3) If the packets of the registered packet type (that is, eapCode=3 or eapCode=4) are the success or failure result returned by the server, the client can perform custom processing after receiving the result.
    
    The following uses the packet type (that is, eapCode=1 and eapType=25) sent by the server to the client as an example. If other packet types need to be registered, change the value of **eapCode** and then call the [regCustomEapHandler](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-net-eap#eapregcustomeaphandler) API.
    

let netType = 1;
let eapCode= 1; // eap request
let eapType= 25; // EAP\_PEAP
let result = 1;

let eapData = (eapData:eap.EapData):void => {
  hilog.info(0x0000, 'testTag', 'rsp result',JSON.stringify(eapData));
  const newBuffer = new Uint8Array(eapData.bufferLen);
  newBuffer.set(eapData.eapBuffer, 0);
  let eapData2: eap.EapData = {
    msgId: eapData.msgId,
    eapBuffer: newBuffer,
    bufferLen: newBuffer.length
  }

  try{
    eap.replyCustomEapData(result, eapData2);
    hilog.info(0x0000, 'testTag', 'replyCustomEapData success');
  } catch (err) {
    hilog.error(0x0000, 'testTag', 'errCode: ' + err.code + ' , errMessage: ' + err.message);
  }
}

function serverReplyCustomEapData() {
  try{
    eap.regCustomEapHandler(netType, eapCode, eapType, eapData);
    hilog.info(0x0000, 'testTag', 'regCustomEapHandler success');
    // ···
  } catch (err) {
    hilog.error(0x0000, 'testTag', 'errCode: ' + err.code + 'errMessage: ' + err.message);
    // ···
  }

1.  To cancel the custom authentication, call [unregCustomEapHandler](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-net-eap#eapunregcustomeaphandler).

let netType = 1;
let eapCode= 1; // eap request
let eapType= 25; // EAP\_PEAP
let result = 1;

let eapData = (eapData:eap.EapData):void => {
  hilog.info(0x0000, 'testTag', 'rsp result',JSON.stringify(eapData));
  const newBuffer = new Uint8Array(eapData.bufferLen);
  newBuffer.set(eapData.eapBuffer, 0);
  let eapData2: eap.EapData = {
    msgId: eapData.msgId,
    eapBuffer: newBuffer,
    bufferLen: newBuffer.length
  }
// ···
}
// ···
  try {
    eap.unregCustomEapHandler(netType, eapCode, eapType, eapData);
    hilog.info(0x0000, 'testTag', 'unregCustomEapHandler success');
    // ···
  } catch (err) {
    hilog.error(0x0000, 'testTag', 'errCode: ' + err.code + ', errMessage: ' + err.message);
    // ···
  }

#### Initiating 802.1X Authentication on the eth Network Port

1.  Use a network cable to connect the device to the **eth** network port.
2.  Import the **eap** namespace from **@kit.NetworkKit**.

import { eap } from '@kit.NetworkKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

1.  If authentication is required for the network management applications, call [startEthEap](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-net-eap#eapstartetheap) to initiate the 802.1X authentication process.

const netId: number = 100;
// ···
  let profile: eap.EthEapProfile = {
    eapMethod: eap.EapMethod.EAP\_TTLS,
    phase2Method: eap.Phase2Method.PHASE2\_AKA\_PRIME,
    identity: 'identity',
    anonymousIdentity: 'anonymousIdentity',
    password: 'password',
    caCertAliases: 'caCertAliases',
    caPath: 'caPath',
    clientCertAliases: 'clientCertAliases',
    certEntry: new Uint8Array(\[5,6,7,8,9,10\]),
    certPassword: 'certPassword',
    altSubjectMatch: 'altSubjectMatch',
    domainSuffixMatch: 'domainSuffixMatch',
    realm: 'realm',
    plmn: 'plmn',
    eapSubId: 1
  };

  try {
    eap.startEthEap(netId, profile);
    hilog.info(0x0000, 'testTag', 'startEthEap success');
    // ···
  } catch (err) {
    // ···
    hilog.error(0x0000, 'testTag', 'errCode: ' + err.code + ', errMessage: ' + err.message);
  }

1.  If authentication is not required for the network management applications, call [logOffEthEap](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-net-eap#eaplogoffetheap) to initiate the 802.1X deauthentication process.

  try{
    eap.logOffEthEap(netId);
    hilog.error(0x0000, 'testTag', 'logOffEthEap success');
    // ···
  } catch (err) {
    // ···
    hilog.error(0x0000, 'testTag', 'errCode: ' + err.code + ', errMessage: ' + err.message);
  }
