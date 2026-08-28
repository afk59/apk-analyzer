# @ohos.telephony.observer (Observer)

The **observer** module provides event subscription management functions. You can register or unregister an observer that listens for the following events: network status change, signal status change, call status change, cellular data connection status, uplink and downlink data flow status of cellular data services, and SIM status change.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/63/v3/73aVZaR1SOuKCHaPo1ykOA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062354Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=322E8D381665C4F8FCEF7941914D3DD49EDD425A569EE04210BD804C951D0831)

The initial APIs of this module are supported since API version 6. Newly added APIs will be marked with a superscript to indicate their earliest API version.

#### Modules to Import

import { observer } from '@kit.TelephonyKit';

#### NetworkState

type NetworkState = radio.NetworkState

Defines the network status.

**System capability**: SystemCapability.Telephony.StateRegistry

| Type | Description |
| :-- | :-- |
| [radio.NetworkState](../ohos-telephony-radio-network-search/document.md#networkstate) | Network status. |

#### SignalInformation

type SignalInformation = radio.SignalInformation

Defines the signal strength.

**System capability**: SystemCapability.Telephony.StateRegistry

| Type | Description |
| :-- | :-- |
| [radio.SignalInformation](../ohos-telephony-radio-network-search/document.md#signalinformation) | Signal strength. |

#### DataConnectState

type DataConnectState = data.DataConnectState

Describes the connection status of a cellular data link.

**System capability**: SystemCapability.Telephony.StateRegistry

| Type | Description |
| :-- | :-- |
| [data.DataConnectState](../ohos-telephony-data-cellular-data/document.md#dataconnectstate) | Connection status of a cellular data link. |

#### RatType

type RatType = radio.RadioTechnology

Enumerates the radio access technologies.

**System capability**: SystemCapability.Telephony.StateRegistry

| Type | Description |
| :-- | :-- |
| [radio.RadioTechnology](../ohos-telephony-radio-network-search/document.md#radiotechnology) | Radio access technology. |

#### DataFlowType

type DataFlowType = data.DataFlowType

Defines the cellular data flow type.

**System capability**: SystemCapability.Telephony.StateRegistry

| Type | Description |
| :-- | :-- |
| [data.DataFlowType](../ohos-telephony-data-cellular-data/document.md#dataflowtype) | Cellular data flow type. |

#### CallState

type CallState = call.CallState

Enumerates call states.

**System capability**: SystemCapability.Telephony.StateRegistry

| Type | Description |
| :-- | :-- |
| [call.CallState](../ohos-telephony-call-call/document.md#callstate) | Call state. (Only the **CALL\_STATE\_OFFHOOK** state is reported during an outgoing call.) |

#### CardType

type CardType = sim.CardType

Enumerates SIM card types.

**System capability**: SystemCapability.Telephony.StateRegistry

| Type | Description |
| :-- | :-- |
| [sim.CardType](../ohos-telephony-sim-sim-management/document.md#cardtype7) | SIM card type. |

#### SimState

type SimState = sim.SimState

SIM card state.

**System capability**: SystemCapability.Telephony.StateRegistry

| Type | Description |
| :-- | :-- |
| [sim.SimState](../ohos-telephony-sim-sim-management/document.md#simstate) | SIM card state. |

#### TelCallState21+

type TelCallState = call.TelCallState

Enumerates call states.

**System capability**: SystemCapability.Telephony.StateRegistry

| Type | Description |
| :-- | :-- |
| [call.TelCallState](../ohos-telephony-call-call/document.md#telcallstate21) | Call state. (**TEL\_CALL\_STATE\_OFFHOOK** and **TEL\_CALL\_STATE\_CONNECTED** are used to report the dialed number status and the call connection status respectively during an outgoing call.) |

#### observer.on('networkStateChange')

on(type: 'networkStateChange', callback: Callback<NetworkState>): void

Registers an observer for network status change events. This API uses an asynchronous callback to return the execution result.

**Required permission**: ohos.permission.GET\_NETWORK\_INFO

**System capability**: SystemCapability.Telephony.StateRegistry

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Network status change event. This field has a fixed value of **networkStateChange**. |
| callback | Callback<[NetworkState](../ohos-telephony-radio-network-search/document.md#networkstate)\> | Yes | Callback used to return the result, which is the [NetworkState](../ohos-telephony-radio-network-search/document.md#networkstate) object. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md) and [Telephony Error Codes](../../error-codes/telephony-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 201 | Permission denied. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 8300001 | Invalid parameter value. |
| 8300002 | Service connection failed. |
| 8300003 | System internal error. |
| 8300999 | Unknown error. |

**Example**

observer.on('networkStateChange', (data: observer.NetworkState) => {
    console.info("on networkStateChange, data:" + JSON.stringify(data));
});

#### observer.on('networkStateChange')

on(type: 'networkStateChange', options: ObserverOptions, callback: Callback<NetworkState>): void

Registers an observer for network status change events of the SIM card in the specified slot. This API uses an asynchronous callback to return the execution result.

**Required permission**: ohos.permission.GET\_NETWORK\_INFO

**System capability**: SystemCapability.Telephony.StateRegistry

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Network status change event. This field has a fixed value of **networkStateChange**. |
| options | [ObserverOptions](#observeroptions11) | Yes | Event subscription parameters. |
| callback | Callback<[NetworkState](../ohos-telephony-radio-network-search/document.md#networkstate)\> | Yes | Callback used to return the result. For details, see [NetworkState](../ohos-telephony-radio-network-search/document.md#networkstate). |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md) and [Telephony Error Codes](../../error-codes/telephony-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 201 | Permission denied. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 8300001 | Invalid parameter value. |
| 8300002 | Service connection failed. |
| 8300003 | System internal error. |
| 8300999 | Unknown error. |

**Example**

let options: observer.ObserverOptions = {
    slotId: 0
}
observer.on('networkStateChange', options, (data: observer.NetworkState) => {
    console.info("on networkStateChange, data:" + JSON.stringify(data));
});

#### observer.off('networkStateChange')

off(type: 'networkStateChange', callback?: Callback<NetworkState>): void

Unregisters the observer for network status change events. This API uses an asynchronous callback to return the execution result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f6/v3/MnstvC5IR1O2ChcEXF5C9g/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062354Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=B11A0B1529B9152775752F0CD74D88FCC1ED7A0369281415C20E82C3B71FDD52)

You can pass the callback of the **on** function if you want to cancel listening for a certain type of event. If you do not pass the callback, you will cancel listening for all events.

**System capability**: SystemCapability.Telephony.StateRegistry

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Network status change event. This field has a fixed value of **networkStateChange**. |
| callback | Callback<[NetworkState](../ohos-telephony-radio-network-search/document.md#networkstate)\> | No | Callback used to return the result. For details, see [NetworkState](../ohos-telephony-radio-network-search/document.md#networkstate). |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md) and [Telephony Error Codes](../../error-codes/telephony-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 8300001 | Invalid parameter value. |
| 8300002 | Service connection failed. |
| 8300003 | System internal error. |
| 8300999 | Unknown error. |

**Example**

let callback: (data: observer.NetworkState) => void = (data: observer.NetworkState) => {
    console.info("on networkStateChange, data:" + JSON.stringify(data));
}
observer.on('networkStateChange', callback);
// You can pass the callback of the on method to cancel listening for a certain type of callback. If you do not pass the callback, you will cancel listening for all callbacks.
observer.off('networkStateChange', callback);
observer.off('networkStateChange');

#### observer.on('signalInfoChange')

on(type: 'signalInfoChange', callback: Callback<Array<SignalInformation>>): void

Registers an observer for signal status change events. This API uses an asynchronous callback to return the execution result.

**System capability**: SystemCapability.Telephony.StateRegistry

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Signal status change event. This field has a fixed value of **signalInfoChange**. |
| callback | Callback<Array<[SignalInformation](../ohos-telephony-radio-network-search/document.md#signalinformation)\>> | Yes | Callback used to return the result. For details, see [SignalInformation](../ohos-telephony-radio-network-search/document.md#signalinformation). |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md) and [Telephony Error Codes](../../error-codes/telephony-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 8300001 | Invalid parameter value. |
| 8300002 | Service connection failed. |
| 8300003 | System internal error. |
| 8300999 | Unknown error. |

**Example**

import { radio } from '@kit.TelephonyKit';

observer.on('signalInfoChange', (data: Array<radio.SignalInformation>) => {
    console.info("on signalInfoChange, data:" + JSON.stringify(data));
});

#### observer.on('signalInfoChange')

on(type: 'signalInfoChange', options: ObserverOptions, callback: Callback<Array<SignalInformation>>): void

Registers an observer for signal status change events of the SIM card in the specified slot. This API uses an asynchronous callback to return the execution result.

**System capability**: SystemCapability.Telephony.StateRegistry

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Signal status change event. This field has a fixed value of **signalInfoChange**. |
| options | [ObserverOptions](#observeroptions11) | Yes | Event subscription parameters. |
| callback | Callback<Array<[SignalInformation](../ohos-telephony-radio-network-search/document.md#signalinformation)\>> | Yes | Callback used to return the result. For details, see [SignalInformation](../ohos-telephony-radio-network-search/document.md#signalinformation). |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md) and [Telephony Error Codes](../../error-codes/telephony-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 8300001 | Invalid parameter value. |
| 8300002 | Service connection failed. |
| 8300003 | System internal error. |
| 8300999 | Unknown error. |

**Example**

import { radio } from '@kit.TelephonyKit';

let options: observer.ObserverOptions = {
    slotId: 0
}
observer.on('signalInfoChange', options, (data: Array<radio.SignalInformation>) => {
    console.info("on signalInfoChange, data:" + JSON.stringify(data));
});

#### observer.off('signalInfoChange')

off(type: 'signalInfoChange', callback?: Callback<Array<SignalInformation>>): void

Unregisters the observer for signal status change events. This API uses an asynchronous callback to return the execution result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f9/v3/w4MRnc1XRTeAbFESfxLieA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062354Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=61E0180ECE98A8A84856F8D816C622D72FA6886D73D91A4512DF585D4DF5ADBE)

You can pass the callback of the **on** function if you want to cancel listening for a certain type of event. If you do not pass the callback, you will cancel listening for all events.

**System capability**: SystemCapability.Telephony.StateRegistry

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Signal status change event. This field has a fixed value of **signalInfoChange**. |
| callback | Callback<Array<[SignalInformation](../ohos-telephony-radio-network-search/document.md#signalinformation)\>> | No | Callback used to return the result. For details, see [SignalInformation](../ohos-telephony-radio-network-search/document.md#signalinformation). |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md) and [Telephony Error Codes](../../error-codes/telephony-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 8300001 | Invalid parameter value. |
| 8300002 | Service connection failed. |
| 8300003 | System internal error. |
| 8300999 | Unknown error. |

**Example**

import { radio } from '@kit.TelephonyKit';

let callback: (data: Array<radio.SignalInformation>) => void = (data: Array<radio.SignalInformation>) => {
    console.info("on signalInfoChange, data:" + JSON.stringify(data));
}
observer.on('signalInfoChange', callback);
// You can pass the callback of the on method to cancel listening for a certain type of callback. If you do not pass the callback, you will cancel listening for all callbacks.
observer.off('signalInfoChange', callback);
observer.off('signalInfoChange');

#### observer.on('callStateChange')

on(type: 'callStateChange', callback: Callback<CallStateInfo>): void

Registers an observer for call status change events. This API uses an asynchronous callback to return the execution result.

**System capability**: SystemCapability.Telephony.StateRegistry

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Call status change event. This field has a fixed value of **callStateChange**. |
| callback | Callback<[CallStateInfo](#callstateinfo11)\> | Yes | 
Callback used to return the result,

which is the **CallStateInfo** object. In this object:

\- Only **state** is accessible to third-party applications. - **number** is only accessible to system applications.

 |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md) and [Telephony Error Codes](../../error-codes/telephony-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 8300001 | Invalid parameter value. |
| 8300002 | Service connection failed. |
| 8300003 | System internal error. |
| 8300999 | Unknown error. |

**Example**

observer.on('callStateChange', (data: observer.CallStateInfo) => {
    console.info("on callStateChange, data:" + JSON.stringify(data));
});

#### observer.on('callStateChange')

on(type: 'callStateChange', options: ObserverOptions, callback: Callback<CallStateInfo>): void

Registers an observer for call status change events. This API uses an asynchronous callback to return the execution result.

**System capability**: SystemCapability.Telephony.StateRegistry

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Call status change event. This field has a fixed value of **callStateChange**. |
| options | [ObserverOptions](#observeroptions11) | Yes | Event subscription parameters. |
| callback | Callback<[CallStateInfo](#callstateinfo11)\> | Yes | 
Callback used to return the result,

which is the **CallStateInfo** object. In this object:

\- Only **state** is accessible to third-party applications. - **number** is only accessible to system applications.

 |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md) and [Telephony Error Codes](../../error-codes/telephony-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 8300001 | Invalid parameter value. |
| 8300002 | Service connection failed. |
| 8300003 | System internal error. |
| 8300999 | Unknown error. |

**Example**

let options: observer.ObserverOptions = {
    slotId: 0
}
observer.on('callStateChange', options, (data: observer.CallStateInfo) => {
    console.info("on callStateChange, data:" + JSON.stringify(data));
});

#### observer.off('callStateChange')

off(type: 'callStateChange', callback?: Callback<CallStateInfo>): void

Unregisters the observer for call status change events. This API uses an asynchronous callback to return the execution result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3e/v3/558Z4d3qQvqa9YJYbquLmQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062354Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=F4F5C15BAD2E2AD859AAF7985455C87C30114B1D3BBB9799DAF6ED43E3BB3A0B)

You can pass the callback of the **on** function if you want to cancel listening for a certain type of event. If you do not pass the callback, you will cancel listening for all events.

**System capability**: SystemCapability.Telephony.StateRegistry

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Call status change event. This field has a fixed value of **callStateChange**. |
| callback | Callback<[CallStateInfo](#callstateinfo11)\> | No | 
Callback used to return the result. For details, see [CallState](../ohos-telephony-call-call/document.md#callstate).

**number**: phone number.

 |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md) and [Telephony Error Codes](../../error-codes/telephony-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 8300001 | Invalid parameter value. |
| 8300002 | Service connection failed. |
| 8300003 | System internal error. |
| 8300999 | Unknown error. |

**Example**

let callback: (data: observer.CallStateInfo) => void = (data: observer.CallStateInfo) => {
    console.info("on callStateChange, data:" + JSON.stringify(data));
}
observer.on('callStateChange', callback);
// You can pass the callback of the on method to cancel listening for a certain type of callback. If you do not pass the callback, you will cancel listening for all callbacks.
observer.off('callStateChange', callback);
observer.off('callStateChange');

#### observer.on('callStateChangeEx')21+

on(type: 'callStateChangeEx', callback: Callback<TelCallState>, options?: ObserverOptions): void

Registers an observer for extended call status change events. This API uses an asynchronous callback to return the execution result.

**System capability**: SystemCapability.Telephony.StateRegistry

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Extended call status change event. This field has a fixed value of **callStateChange**. |
| callback | Callback<[TelCallState](../ohos-telephony-call-call/document.md#telcallstate21)\> | Yes | 
Callback used to return the result,

which is the **TelCallState** object.

 |
| options | [ObserverOptions](#observeroptions11) | No | Event subscription parameters. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md) and [Telephony Error Codes](../../error-codes/telephony-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 8800001 | Invalid parameter value. |
| 8800002 | Service connection failed. |
| 8800003 | System internal error. |
| 8800999 | Unknown error. |

**Example**

import { call } from '@kit.TelephonyKit';

let callback: (data: call.TelCallState) => void = (data: call.TelCallState) => {
    console.info("on callStateChangeEx, data:" + JSON.stringify(data));
}
let options: observer.ObserverOptions = {
    slotId: 0
}

observer.on('callStateChangeEx', callback, options);
observer.on('callStateChangeEx', callback);

#### observer.off('callStateChangeEx')21+

off(type: 'callStateChangeEx', callback?: Callback<TelCallState>): void

Unregisters the observer for extended call status change events. This API uses an asynchronous callback to return the execution result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/36/v3/8AW9glMFTGSCPp1Coh1Zaw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062354Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=DA0EE3A63FEDD5BD206116288BC991859BB581912948FE46517F7C6DEE3E7383)

You can pass the callback of the **on** function if you want to cancel listening for a certain type of event. If you do not pass the callback, you will cancel listening for all events.

**System capability**: SystemCapability.Telephony.StateRegistry

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Call status change event. This field has a fixed value of **callStateChange**. |
| callback | Callback<[TelCallState](../ohos-telephony-call-call/document.md#telcallstate21)\> | No | 
Callback used to return the result. For details, see [TelCallState](../ohos-telephony-call-call/document.md#telcallstate21).

 |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md) and [Telephony Error Codes](../../error-codes/telephony-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 8800001 | Invalid parameter value. |
| 8800002 | Service connection failed. |
| 8800003 | System internal error. |
| 8800999 | Unknown error. |

**Example**

import { call } from '@kit.TelephonyKit';
let callback: (data: call.TelCallState) => void = (data: call.TelCallState) => {
    console.info("on callStateChangeEx, data:" + JSON.stringify(data));
}
observer.on('callStateChangeEx', callback);
// You can pass the callback of the on method to cancel listening for a certain type of callback. If you do not pass the callback, you will cancel listening for all callbacks.
observer.off('callStateChangeEx', callback);
observer.off('callStateChangeEx');

#### observer.on('cellularDataConnectionStateChange')7+

on(type: 'cellularDataConnectionStateChange', callback: Callback<DataConnectionStateInfo>): void

Registers an observer for connection status change events of the cellular data link. This API uses an asynchronous callback to return the result.

**System capability**: SystemCapability.Telephony.StateRegistry

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Cellular data connection status event. This field has a fixed value of **cellularDataConnectionStateChange**. |
| callback | Callback<[DataConnectionStateInfo](#dataconnectionstateinfo11)\> | Yes | Callback used to return the result. For details, see [DataConnectState](../ohos-telephony-data-cellular-data/document.md#dataconnectstate) and [RadioTechnology](../ohos-telephony-radio-network-search/document.md#radiotechnology). |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md) and [Telephony Error Codes](../../error-codes/telephony-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 8300001 | Invalid parameter value. |
| 8300002 | Service connection failed. |
| 8300003 | System internal error. |
| 8300999 | Unknown error. |

**Example**

observer.on('cellularDataConnectionStateChange', (data: observer.DataConnectionStateInfo) => {
    console.info("on cellularDataConnectionStateChange, data:" + JSON.stringify(data));
});

#### observer.on('cellularDataConnectionStateChange')7+

on(type: 'cellularDataConnectionStateChange', options: ObserverOptions, callback: Callback<DataConnectionStateInfo>): void

Registers an observer for connection status change events of the cellular data link over the SIM card in the specified slot. This API uses an asynchronous callback to return the result.

**System capability**: SystemCapability.Telephony.StateRegistry

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Cellular data connection status event. This field has a fixed value of **cellularDataConnectionStateChange**. |
| options | [ObserverOptions](#observeroptions11) | Yes | Event subscription parameters. |
| callback | Callback<[DataConnectionStateInfo](#dataconnectionstateinfo11)\> | Yes | Callback used to return the result. For details, see [DataConnectState](../ohos-telephony-data-cellular-data/document.md#dataconnectstate) and [RadioTechnology](../ohos-telephony-radio-network-search/document.md#radiotechnology). |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md) and [Telephony Error Codes](../../error-codes/telephony-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 8300001 | Invalid parameter value. |
| 8300002 | Service connection failed. |
| 8300003 | System internal error. |
| 8300999 | Unknown error. |

**Example**

let options: observer.ObserverOptions = {
    slotId: 0
}
observer.on('cellularDataConnectionStateChange', options, (data: observer.DataConnectionStateInfo) => {
    console.info("on cellularDataConnectionStateChange, data:" + JSON.stringify(data));
});

#### observer.off('cellularDataConnectionStateChange')7+

off(type: 'cellularDataConnectionStateChange', callback?: Callback<DataConnectionStateInfo>): void

Unregisters the observer for connection status change events of the cellular data link. This API uses an asynchronous callback to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/44/v3/rkySX4y5TP2LPb4KpS_wRQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062354Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=8A9B769DC7DB2225A6457A441BB28306B4833B21C2A52C9A4A08AFC2C199D7B0)

You can pass the callback of the **on** function if you want to cancel listening for a certain type of event. If you do not pass the callback, you will cancel listening for all events.

**System capability**: SystemCapability.Telephony.StateRegistry

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Cellular data connection status event. This field has a fixed value of **cellularDataConnectionStateChange**. |
| callback | Callback<[DataConnectionStateInfo](#dataconnectionstateinfo11)\> | No | Callback used to return the result. For details, see [DataConnectState](../ohos-telephony-data-cellular-data/document.md#dataconnectstate) and [RadioTechnology](../ohos-telephony-radio-network-search/document.md#radiotechnology). |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md) and [Telephony Error Codes](../../error-codes/telephony-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 8300001 | Invalid parameter value. |
| 8300002 | Service connection failed. |
| 8300003 | System internal error. |
| 8300999 | Unknown error. |

**Example**

let callback: (data: observer.DataConnectionStateInfo) => void = (data: observer.DataConnectionStateInfo) => {
    console.info("on cellularDataConnectionStateChange, data:" + JSON.stringify(data));
}
observer.on('cellularDataConnectionStateChange', callback);
// You can pass the callback of the on method to cancel listening for a certain type of callback. If you do not pass the callback, you will cancel listening for all callbacks.
observer.off('cellularDataConnectionStateChange', callback);
observer.off('cellularDataConnectionStateChange');

#### observer.on('cellularDataFlowChange')7+

on(type: 'cellularDataFlowChange', callback: Callback<DataFlowType>): void

Registers an observer for the uplink and downlink data flow status change events of the cellular data service. This API uses an asynchronous callback to return the result.

**System capability**: SystemCapability.Telephony.StateRegistry

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Cellular data flow change event. This field has a fixed value of **cellularDataFlowChange**. |
| callback | Callback<[DataFlowType](../ohos-telephony-data-cellular-data/document.md#dataflowtype)\> | Yes | Callback used to return the result. For details, see [DataFlowType](../ohos-telephony-data-cellular-data/document.md#dataflowtype). |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md) and [Telephony Error Codes](../../error-codes/telephony-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 8300001 | Invalid parameter value. |
| 8300002 | Service connection failed. |
| 8300003 | System internal error. |
| 8300999 | Unknown error. |

**Example**

import { data } from '@kit.TelephonyKit';

observer.on('cellularDataFlowChange', (data: data.DataFlowType) => {
    console.info("on cellularDataFlowChange, data:" + JSON.stringify(data));
});

#### observer.on('cellularDataFlowChange')7+

on(type: 'cellularDataFlowChange', options: ObserverOptions, callback: Callback<DataFlowType>): void

Registers an observer for the uplink and downlink data flow status change events of the cellular data service on the SIM card in the specified slot. This API uses an asynchronous callback to return the result.

**System capability**: SystemCapability.Telephony.StateRegistry

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Cellular data flow change event. This field has a fixed value of **cellularDataFlowChange**. |
| options | [ObserverOptions](#observeroptions11) | Yes | Event subscription parameters. |
| callback | Callback<[DataFlowType](../ohos-telephony-data-cellular-data/document.md#dataflowtype)\> | Yes | Callback used to return the result. For details, see [DataFlowType](../ohos-telephony-data-cellular-data/document.md#dataflowtype). |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md) and [Telephony Error Codes](../../error-codes/telephony-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 8300001 | Invalid parameter value. |
| 8300002 | Service connection failed. |
| 8300003 | System internal error. |
| 8300999 | Unknown error. |

**Example**

import { data } from '@kit.TelephonyKit';

let options: observer.ObserverOptions = {
    slotId: 0
}
observer.on('cellularDataFlowChange', options, (data: data.DataFlowType) => {
    console.info("on cellularDataFlowChange, data:" + JSON.stringify(data));
});

#### observer.off('cellularDataFlowChange')7+

off(type: 'cellularDataFlowChange', callback?: Callback<DataFlowType>): void

Unregisters the observer for the uplink and downlink data flow status change events of the cellular data service. This API uses an asynchronous callback to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/47/v3/6F7RwYYoSauxbEXDHMTJXA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062354Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=1CF4AEAFE55FCC64813869368D18C2934CD4A9A0249227D6C5E283CE36101708)

You can pass the callback of the **on** function if you want to cancel listening for a certain type of event. If you do not pass the callback, you will cancel listening for all events.

**System capability**: SystemCapability.Telephony.StateRegistry

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Cellular data flow change event. This field has a fixed value of **cellularDataFlowChange**. |
| callback | Callback<[DataFlowType](../ohos-telephony-data-cellular-data/document.md#dataflowtype)\> | No | Callback used to return the result. For details, see [DataFlowType](../ohos-telephony-data-cellular-data/document.md#dataflowtype). |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md) and [Telephony Error Codes](../../error-codes/telephony-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 8300001 | Invalid parameter value. |
| 8300002 | Service connection failed. |
| 8300003 | System internal error. |
| 8300999 | Unknown error. |

**Example**

import { data } from '@kit.TelephonyKit';

let callback: (data: data.DataFlowType) => void = (data: data.DataFlowType) => {
    console.info("on cellularDataFlowChange, data:" + JSON.stringify(data));
}
observer.on('cellularDataFlowChange', callback);
// You can pass the callback of the on method to cancel listening for a certain type of callback. If you do not pass the callback, you will cancel listening for all callbacks.
observer.off('cellularDataFlowChange', callback);
observer.off('cellularDataFlowChange');

#### observer.on('simStateChange')7+

on(type: 'simStateChange', callback: Callback<SimStateData>): void

Registers an observer for SIM card status change events. This API uses an asynchronous callback to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/65/v3/-zuEI-ZGQsyCYIdmHuK0gg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062354Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=9D26A0FD2BB6A17C69FCB8EFB20187465250E0D465660AB1E34F0BDF100066E3)

The return result of this API does not contain the activation status of the SIM card. For details, see [sim.isSimActive](../ohos-telephony-sim-sim-management/document.md#simissimactive7).

**System capability**: SystemCapability.Telephony.StateRegistry

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | SIM status change event. This field has a fixed value of **simStateChange**. |
| callback | Callback<[SimStateData](#simstatedata7)\> | Yes | Callback used to return the result. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md) and [Telephony Error Codes](../../error-codes/telephony-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 8300001 | Invalid parameter value. |
| 8300002 | Service connection failed. |
| 8300003 | System internal error. |
| 8300999 | Unknown error. |

**Example**

observer.on('simStateChange', (data: observer.SimStateData) => {
    console.info("on simStateChange, data:" + JSON.stringify(data));
});

#### observer.on('simStateChange')7+

on(type: 'simStateChange', options: ObserverOptions, callback: Callback<SimStateData>): void

Registers an observer for status change events of the SIM card in the specified slot. This API uses an asynchronous callback to return the result.

**System capability**: SystemCapability.Telephony.StateRegistry

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | SIM status change event. This field has a fixed value of **simStateChange**. |
| options | [ObserverOptions](#observeroptions11) | Yes | Event subscription parameters. |
| callback | Callback<[SimStateData](#simstatedata7)\> | Yes | Callback used to return the result. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md) and [Telephony Error Codes](../../error-codes/telephony-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 8300001 | Invalid parameter value. |
| 8300002 | Service connection failed. |
| 8300003 | System internal error. |
| 8300999 | Unknown error. |

**Example**

let options: observer.ObserverOptions = {
    slotId: 0
}
observer.on('simStateChange', options, (data: observer.SimStateData) => {
    console.info("on simStateChange, data:" + JSON.stringify(data));
});

#### observer.off('simStateChange')7+

off(type: 'simStateChange', callback?: Callback<SimStateData>): void

Unregisters the observer for SIM card status change events. This API uses an asynchronous callback to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6f/v3/YbfWM0NiRYiNnAXRiH-1lg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062354Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=91AAB1EE9DB3D9308D7E47B0A37EC8563D67A6FB835D9BB817668E3804997E1D)

You can pass the callback of the **on** function if you want to cancel listening for a certain type of event. If you do not pass the callback, you will cancel listening for all events.

**System capability**: SystemCapability.Telephony.StateRegistry

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | SIM status change event. This field has a fixed value of **simStateChange**. |
| callback | Callback<[SimStateData](#simstatedata7)\> | No | Callback used to return the result. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md) and [Telephony Error Codes](../../error-codes/telephony-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 8300001 | Invalid parameter value. |
| 8300002 | Service connection failed. |
| 8300003 | System internal error. |
| 8300999 | Unknown error. |

**Example**

let callback: (data: observer.SimStateData) => void = (data: observer.SimStateData) => {
    console.info("on simStateChange, data:" + JSON.stringify(data));
}
observer.on('simStateChange', callback);
// You can pass the callback of the on method to cancel listening for a certain type of callback. If you do not pass the callback, you will cancel listening for all callbacks.
observer.off('simStateChange', callback);
observer.off('simStateChange');

#### observer.on('iccAccountInfoChange')10+

on(type: 'iccAccountInfoChange', callback: Callback<void>): void

Registers an observer for account information change events of the SIM card. This API uses an asynchronous callback to return the result.

**System capability**: SystemCapability.Telephony.StateRegistry

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Account information change event. This field has a fixed value of **iccAccountInfoChange**. |
| callback | Callback<void> | Yes | Callback used to return the result. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md) and [Telephony Error Codes](../../error-codes/telephony-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 8300001 | Invalid parameter value. |
| 8300002 | Service connection failed. |
| 8300003 | System internal error. |
| 8300999 | Unknown error. |

**Example**

observer.on('iccAccountInfoChange', () => {
    console.info("on iccAccountInfoChange success");
});

#### observer.off('iccAccountInfoChange')10+

off(type: 'iccAccountInfoChange', callback?: Callback<void>): void

Unregisters the observer for account information change events of the SIM card. This API uses an asynchronous callback to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/87/v3/BVsq49OhSziJErI87gsQBg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062354Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=7009CE6D752918B0E5FA51EBB69CD96A00898B2B03A7E9ADF9C5B4121624811A)

You can pass the callback of the **on** function if you want to cancel listening for a certain type of event. If you do not pass the callback, you will cancel listening for all events.

**System capability**: SystemCapability.Telephony.StateRegistry

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Account information change event. This field has a fixed value of **iccAccountInfoChange**. |
| callback | Callback<void> | No | Callback used to return the result. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md) and [Telephony Error Codes](../../error-codes/telephony-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 8300001 | Invalid parameter value. |
| 8300002 | Service connection failed. |
| 8300003 | System internal error. |
| 8300999 | Unknown error. |

**Example**

let callback: () => void = () => {
    console.info("on iccAccountInfoChange success");
}
observer.on('iccAccountInfoChange', callback);
// You can pass the callback of the on method to cancel listening for a certain type of callback. If you do not pass the callback, you will cancel listening for all callbacks.
observer.off('iccAccountInfoChange', callback);
observer.off('iccAccountInfoChange');

#### LockReason8+

Enumerates SIM card lock types.

**System capability**: SystemCapability.Telephony.StateRegistry

| Name | Value | Description |
| :-- | :-- | :-- |
| SIM\_NONE | 0 | No lock. |
| SIM\_PIN | 1 | PIN lock. |
| SIM\_PUK | 2 | PUK lock. |
| SIM\_PN\_PIN | 3 | Network PIN lock. |
| SIM\_PN\_PUK | 4 | Network PUK lock. |
| SIM\_PU\_PIN | 5 | Subnet PIN lock. |
| SIM\_PU\_PUK | 6 | Subnet PUK lock. |
| SIM\_PP\_PIN | 7 | Service provider PIN lock. |
| SIM\_PP\_PUK | 8 | Service provider PUK lock. |
| SIM\_PC\_PIN | 9 | Organization PIN lock. |
| SIM\_PC\_PUK | 10 | Organization PUK lock. |
| SIM\_SIM\_PIN | 11 | SIM PIN lock. |
| SIM\_SIM\_PUK | 12 | SIM PUK lock. |

#### SimStateData7+

Enumerates SIM card types and states.

**System capability**: SystemCapability.Telephony.StateRegistry

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| type | [CardType](../ohos-telephony-sim-sim-management/document.md#cardtype7) | No | No | SIM card type. |
| state | [SimState](../ohos-telephony-sim-sim-management/document.md#simstate) | No | No | SIM card state. |
| reason8+ | [LockReason](#lockreason8) | No | No | SIM card lock type. |

#### CallStateInfo11+

Defines information about the call status.

**System capability**: SystemCapability.Telephony.StateRegistry

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| state | [CallState](../ohos-telephony-call-call/document.md#callstate) | No | No | Call type. |
| number | string | No | No | Phone number. |

#### DataConnectionStateInfo11+

Defines information about the data connection status.

**System capability**: SystemCapability.Telephony.StateRegistry

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| state | [DataConnectState](../ohos-telephony-data-cellular-data/document.md#dataconnectstate) | No | No | Data connection status. |
| network | [RatType](../ohos-telephony-radio-network-search/document.md#radiotechnology) | No | No | Network type. |

#### ObserverOptions11+

Defines event subscription parameters.

**System capability**: SystemCapability.Telephony.StateRegistry

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| slotId | number | No | No | 
Card slot ID.

\- **0**: card slot 1.

\- **1**: card slot 2.

 |
