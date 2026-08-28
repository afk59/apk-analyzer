# @ohos.telephony.call (Call)

The **call** module provides call management functions, including making calls, redirecting to the dial screen, obtaining the call status, and formatting phone numbers.

To subscribe to call status changes, use [observer.on('callStateChange')](../ohos-telephony-observer-observer/document.md#observeroncallstatechange).

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/dd/v3/r60yGRTIRKCI8PWVcmM71w/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062354Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=1668CE8607C72FC05D37CEEDF0478E7EFE88B481E627B532E3AC7094F2049A8B)

The initial APIs of this module are supported since API version 6. Newly added APIs will be marked with a superscript to indicate their earliest API version.

#### Modules to Import

import { call } from '@kit.TelephonyKit';

#### call.dial(deprecated)

dial(phoneNumber: string, callback: AsyncCallback<boolean>): void

Initiates a call. This API uses an asynchronous callback to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5c/v3/GSymXNjvR8K2oE2Fw9_OFw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062354Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=3DA295EABD1BE7BCC9F2F555B120B1BCA86E0F50DA18A1050F3CF80EFB1C55E6)

This API is supported since API version 6 and deprecated since API version 9. The substitute API is available only for system applications.

**Required permissions**: ohos.permission.PLACE\_CALL (available only for system applications)

**System capability**: SystemCapability.Telephony.CallManager

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| phoneNumber | string | Yes | Phone number. |
| callback | AsyncCallback<boolean> | Yes | Callback used to return the result. The value **true** indicates that the operation is successful, and the value **false** indicates the opposite. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

call.dial("138xxxxxxxx", (err: BusinessError, data: boolean) => {
    console.info(\`callback: err->${JSON.stringify(err)}, data->${JSON.stringify(data)}\`);
});

#### call.dial(deprecated)

dial(phoneNumber: string, options: DialOptions, callback: AsyncCallback<boolean>): void

Initiates a call. You can set call options as needed. This API uses an asynchronous callback to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ba/v3/ltv4jiCwSsGpQ0em-WQV_A/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062354Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=20D815EE1DF4314A86AD91D574A74AA5990A8B10098424520E8BE48F8B278E82)

This API is supported since API version 6 and deprecated since API version 9. The substitute API is available only for system applications.

**Required permissions**: ohos.permission.PLACE\_CALL (available only for system applications)

**System capability**: SystemCapability.Telephony.CallManager

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| phoneNumber | string | Yes | Phone number. |
| options | [DialOptions](#dialoptions) | Yes | Call option, which indicates whether the call is a voice call or video call. |
| callback | AsyncCallback<boolean> | Yes | Callback used to return the result. The value **true** indicates that the operation is successful, and the value **false** indicates the opposite. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

let dialOptions: call.DialOptions = {
    extras: false
}
call.dial("138xxxxxxxx", dialOptions, (err: BusinessError, data: boolean) => {
    console.info(\`callback: err->${JSON.stringify(err)}, data->${JSON.stringify(data)}\`);
});

#### call.dial(deprecated)

dial(phoneNumber: string, options?: DialOptions): Promise<boolean>

Initiates a call. You can set call options as needed. This API uses a promise to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/84/v3/NGTxMQJ_RimFVy2zlc_K1A/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062354Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=ADFA5A5C07BE077D040A5C18C60A33C103CC80B0CD34C9F59FEA59FCEA754173)

This API is supported since API version 6 and deprecated since API version 9. The substitute API is available only for system applications.

**Required permissions**: ohos.permission.PLACE\_CALL (available only for system applications)

**System capability**: SystemCapability.Telephony.CallManager

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| phoneNumber | string | Yes | Phone number. |
| options | [DialOptions](#dialoptions) | No | Call option, which indicates whether the call is a voice call or video call. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<boolean> | Promise used to return the result. The value **true** indicates that the operation is successful, and the value **false** indicates the opposite. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

let dialOptions: call.DialOptions = {
    extras: false
}
call.dial("138xxxxxxxx", dialOptions).then((data: boolean) => {
    console.info(\`dial success, promise: data->${JSON.stringify(data)}\`);
}).catch((err: BusinessError) => {
    console.error(\`dial fail, promise: err->${JSON.stringify(err)}\`);
});

#### call.makeCall7+

makeCall(phoneNumber: string, callback: AsyncCallback<void>): void

Launches the call screen and displays the dialed number. This API uses an asynchronous callback to return the result. This API can be called only in a UIAbility.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Applications.Contacts

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| phoneNumber | string | Yes | Phone number. |
| callback | AsyncCallback<void> | Yes | Callback used to return the result. |

**Error codes**

For details about the error codes, see [ohos.telephony (Telephony) Error Codes](../../error-codes/telephony-error-codes/document.md) and [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2. Incorrect parameters types; |
| 8300001 | Invalid parameter value. |
| 8300002 | Operation failed. Cannot connect to service. |
| 8300003 | System internal error. |
| 8300999 | Unknown error code. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';
// The tel URI format is supported since API version 15, for example, tel:13xxxx.
call.makeCall("138xxxxxxxx", (err: BusinessError) => {
    if (err) {
        console.error(\`makeCall fail, err->${JSON.stringify(err)}\`);
    } else {
        console.info(\`makeCall success\`);
    }
});

#### call.makeCall7+

makeCall(phoneNumber: string): Promise<void>

Launches the call screen and displays the dialed number. This API uses a promise to return the result. This API can be called only in a UIAbility.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Applications.Contacts

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| phoneNumber | string | Yes | Phone number. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise used to return the result. |

**Error codes**

For details about the error codes, see [ohos.telephony (Telephony) Error Codes](../../error-codes/telephony-error-codes/document.md) and [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2. Incorrect parameters types; |
| 8300001 | Invalid parameter value. |
| 8300002 | Operation failed. Cannot connect to service. |
| 8300003 | System internal error. |
| 8300999 | Unknown error code. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';
// The tel URI format is supported since API version 15, for example, tel:13xxxx.
call.makeCall("138xxxxxxxx").then(() => {
    console.info(\`makeCall success\`);
}).catch((err: BusinessError) => {
    console.error(\`makeCall fail, promise: err->${JSON.stringify(err)}\`);
});

#### call.makeCall12+

makeCall(context: Context, phoneNumber: string): Promise<void>

Launches the call screen and displays the dialed number. This API uses a promise to return the result. You need to declare the **ohos.permission.START\_ABILITIES\_FROM\_BACKGROUND** permission if you want to call the API in the background.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Applications.Contacts

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| context | Context | Yes | Application context. |
| phoneNumber | string | Yes | Phone number. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise used to return the result. |

**Error codes**

For details about the error codes, see [ohos.telephony (Telephony) Error Codes](../../error-codes/telephony-error-codes/document.md) and [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2. Incorrect parameters types; |
| 8300002 | Operation failed. Cannot connect to service. |
| 8300003 | System internal error. |

**Example**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/45/v3/lZohp2JESQmmFh_CAuKrEg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062354Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=08677E3169FD51F5B5B47C07E5A107243BEBDBF237D2DB21CCCF7E3E04760350)

In the sample code provided in this topic, **this.context** is used to obtain **UIAbilityContext**, where **this** indicates a UIAbility instance inherited from **UIAbility**. To use UIAbilityContext APIs on pages, see [Obtaining the Context of UIAbility](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/uiability-usage#obtaining-the-context-of-uiability).

import { BusinessError } from '@kit.BasicServicesKit';
// Obtain the application context.
let context = this.getUIContext().getHostContext() as Context;
// The tel URI format is supported since API version 15, for example, tel:13xxxx.
call.makeCall(context, "138xxxxxxxx").then(() => {
    console.info(\`makeCall success\`);
}).catch((err: BusinessError) => {
    console.error(\`makeCall fail, promise: err->${JSON.stringify(err)}\`);
});

#### call.hasCall

hasCall(callback: AsyncCallback<boolean>): void

Checks whether a call is in progress. This API uses an asynchronous callback to return the result.

**System capability**: SystemCapability.Telephony.CallManager

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | AsyncCallback<boolean> | Yes | Callback used to return the result. The value **true** indicates that a call is in progress, and the value **false** indicates the opposite. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

call.hasCall((err: BusinessError, data: boolean) => {
    if (err) {
        console.error(\`hasCall fail, err->${JSON.stringify(err)}\`);
    } else {
        console.info(\`hasCall success, data->${JSON.stringify(data)}\`);
    }
});

#### call.hasCall

hasCall(): Promise<boolean>

Checks whether a call is in progress. This API uses a promise to return the result.

**System capability**: SystemCapability.Telephony.CallManager

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<boolean> | Promise used to return the result. The value **true** indicates that a call is in progress, and the value **false** indicates the opposite. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

call.hasCall().then(() => {
    console.info(\`hasCall success\`);
}).catch((err: BusinessError) => {
    console.error(\`hasCall fail, promise: err->${JSON.stringify(err)}\`);
});

#### call.hasCallSync10+

hasCallSync(): boolean

Checks whether a call is in progress.

**System capability**: SystemCapability.Telephony.CallManager

**Return value**

| Type | Description |
| :-- | :-- |
| boolean | Promise used to return the result. The value **true** indicates that a call is in progress, and the value **false** indicates the opposite. |

**Example**

let hasCall: boolean = call.hasCallSync();
console.info(\`hasCallSync success, has call is \` + hasCall);

#### call.getCallState

getCallState(callback: AsyncCallback<CallState>): void

Obtains the call status. This API uses an asynchronous callback to return the result.

**System capability**: SystemCapability.Telephony.CallManager

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | AsyncCallback<[CallState](#callstate)\> | Yes | Callback used to return the result. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

call.getCallState((err: BusinessError, data: call.CallState) => {
    if (err) {
        console.error(\`getCallState fail, err->${JSON.stringify(err)}\`);
    } else {
        console.info(\`getCallState success, data->${JSON.stringify(data)}\`);
    }
});

#### call.getCallState

getCallState(): Promise<CallState>

Obtains the call status. This API uses a promise to return the result.

**System capability**: SystemCapability.Telephony.CallManager

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<[CallState](#callstate)\> | Promise used to return the result. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

call.getCallState().then((data: call.CallState) => {
    console.info(\`getCallState success, promise: data->${JSON.stringify(data)}\`);
}).catch((err: BusinessError) => {
    console.error(\`getCallState fail, promise: err->${JSON.stringify(err)}\`);
});

#### call.getCallStateSync10+

getCallStateSync(): CallState

Obtains the call status.

**System capability**: SystemCapability.Telephony.CallManager

**Return value**

| Type | Description |
| :-- | :-- |
| [CallState](#callstate) | Promise used to return the result. |

**Example**

let callState: call.CallState = call.getCallStateSync();
console.info(\`the call state is:\` + callState);

#### call.hasVoiceCapability7+

hasVoiceCapability(): boolean

Checks whether a device supports voice calls.

**System capability**: SystemCapability.Telephony.CallManager

**Return value**

| Type | Description |
| :-- | :-- |
| boolean | Result indicating whether the device supports voice calls. The value **true** indicates yes, and the value **false** indicates no. |

let result: boolean = call.hasVoiceCapability();
console.info(\`hasVoiceCapability: ${JSON.stringify(result)}\`);

#### call.isEmergencyPhoneNumber7+

isEmergencyPhoneNumber(phoneNumber: string, callback: AsyncCallback<boolean>): void

Checks whether the called number is an emergency number. This API uses an asynchronous callback to return the result.

**System capability**: SystemCapability.Telephony.CallManager

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| phoneNumber | string | Yes | Phone number. |
| callback | AsyncCallback<boolean> | Yes | Callback used to return the result. The value **true** indicates that the called number is an emergency number, and the value **false** indicates the opposite. |

**Error codes**

For details about the error codes, see [ohos.telephony (Telephony) Error Codes](../../error-codes/telephony-error-codes/document.md) and [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2. Incorrect parameters types; |
| 8300001 | Invalid parameter value. |
| 8300002 | Operation failed. Cannot connect to service. |
| 8300003 | System internal error. |
| 8300999 | Unknown error code. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

call.isEmergencyPhoneNumber("138xxxxxxxx", (err: BusinessError, data: boolean) => {
    if (err) {
        console.error(\`isEmergencyPhoneNumber fail, err->${JSON.stringify(err)}\`);
    } else {
        console.info(\`isEmergencyPhoneNumber success, data->${JSON.stringify(data)}\`);
    }
});

#### call.isEmergencyPhoneNumber7+

isEmergencyPhoneNumber(phoneNumber: string, options: EmergencyNumberOptions, callback: AsyncCallback<boolean>): void

Checks whether the called number is an emergency number based on the phone number. This API uses an asynchronous callback to return the result.

**System capability**: SystemCapability.Telephony.CallManager

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| phoneNumber | string | Yes | Phone number. |
| options | [EmergencyNumberOptions](#emergencynumberoptions7) | Yes | Emergency number options. |
| callback | AsyncCallback<boolean> | Yes | Callback used to return the result. The value **true** indicates that the called number is an emergency number, and the value **false** indicates the opposite. |

**Error codes**

For details about the error codes, see [ohos.telephony (Telephony) Error Codes](../../error-codes/telephony-error-codes/document.md) and [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2. Incorrect parameters types; |
| 8300001 | Invalid parameter value. |
| 8300002 | Operation failed. Cannot connect to service. |
| 8300003 | System internal error. |
| 8300999 | Unknown error code. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

let options: call.EmergencyNumberOptions = {slotId: 1}
call.isEmergencyPhoneNumber("112", options, (err: BusinessError, data: boolean) => {
    if (err) {
        console.error(\`isEmergencyPhoneNumber fail, err->${JSON.stringify(err)}\`);
    } else {
        console.info(\`isEmergencyPhoneNumber success, data->${JSON.stringify(data)}\`);
    }
});

#### call.isEmergencyPhoneNumber7+

isEmergencyPhoneNumber(phoneNumber: string, options?: EmergencyNumberOptions): Promise<boolean>

Checks whether the called number is an emergency number based on the phone number. This API uses a promise to return the result.

**System capability**: SystemCapability.Telephony.CallManager

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| phoneNumber | string | Yes | Phone number. |
| options | [EmergencyNumberOptions](#emergencynumberoptions7) | No | Emergency number options. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<boolean> | Promise used to return the result. The value **true** indicates that the called number is an emergency number, and the value **false** indicates the opposite. |

**Error codes**

For details about the error codes, see [ohos.telephony (Telephony) Error Codes](../../error-codes/telephony-error-codes/document.md) and [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2. Incorrect parameters types; |
| 8300001 | Invalid parameter value. |
| 8300002 | Operation failed. Cannot connect to service. |
| 8300003 | System internal error. |
| 8300999 | Unknown error code. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

let options: call.EmergencyNumberOptions = {slotId: 1}
call.isEmergencyPhoneNumber("138xxxxxxxx", options).then((data: boolean) => {
    console.info(\`isEmergencyPhoneNumber success, promise: data->${JSON.stringify(data)}\`);
}).catch((err: BusinessError) => {
    console.error(\`isEmergencyPhoneNumber fail, promise: err->${JSON.stringify(err)}\`);
});

#### call.formatPhoneNumber7+

formatPhoneNumber(phoneNumber: string, callback: AsyncCallback<string>): void

Formats a phone number. This API uses an asynchronous callback to return the result.

A formatted phone number is a standard numeric string, for example, 555 0100.

**System capability**: SystemCapability.Telephony.CallManager

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| phoneNumber | string | Yes | Phone number. |
| callback | AsyncCallback<string> | Yes | Callback used to return the result. |

**Error codes**

For details about the error codes, see [ohos.telephony (Telephony) Error Codes](../../error-codes/telephony-error-codes/document.md) and [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2. Incorrect parameters types; |
| 8300001 | Invalid parameter value. |
| 8300002 | Operation failed. Cannot connect to service. |
| 8300003 | System internal error. |
| 8300999 | Unknown error code. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

call.formatPhoneNumber("138xxxxxxxx", (err: BusinessError, data: string) => {
    if (err) {
        console.error(\`formatPhoneNumber fail, err->${JSON.stringify(err)}\`);
    } else {
        console.info(\`formatPhoneNumber success, data->${JSON.stringify(data)}\`);
    }
});

#### call.formatPhoneNumber7+

formatPhoneNumber(phoneNumber: string, options: NumberFormatOptions, callback: AsyncCallback<string>): void

Formats a phone number based on specified formatting options. This API uses an asynchronous callback to return the result.

A formatted phone number is a standard numeric string, for example, 555 0100.

**System capability**: SystemCapability.Telephony.CallManager

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| phoneNumber | string | Yes | Phone number. |
| options | [NumberFormatOptions](#numberformatoptions7) | Yes | Number formatting options, for example, country code. |
| callback | AsyncCallback<string> | Yes | Callback used to return the result. |

**Error codes**

For details about the error codes, see [ohos.telephony (Telephony) Error Codes](../../error-codes/telephony-error-codes/document.md) and [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2. Incorrect parameters types; |
| 8300001 | Invalid parameter value. |
| 8300002 | Operation failed. Cannot connect to service. |
| 8300003 | System internal error. |
| 8300999 | Unknown error code. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

let options: call.NumberFormatOptions = {
    countryCode: "CN"
}
call.formatPhoneNumber("138xxxxxxxx", options, (err: BusinessError, data: string) => {
    if (err) {
        console.error(\`formatPhoneNumber fail, err->${JSON.stringify(err)}\`);
    } else {
        console.info(\`formatPhoneNumber success, data->${JSON.stringify(data)}\`);
    }
});

#### call.formatPhoneNumber7+

formatPhoneNumber(phoneNumber: string, options?: NumberFormatOptions): Promise<string>

Formats a phone number based on specified formatting options. This API uses a promise to return the result.

A formatted phone number is a standard numeric string, for example, 555 0100.

**System capability**: SystemCapability.Telephony.CallManager

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| phoneNumber | string | Yes | Phone number. |
| options | [NumberFormatOptions](#numberformatoptions7) | No | Number formatting options, for example, country code. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<string> | Promise used to return the result. |

**Error codes**

For details about the error codes, see [ohos.telephony (Telephony) Error Codes](../../error-codes/telephony-error-codes/document.md) and [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2. Incorrect parameters types; |
| 8300001 | Invalid parameter value. |
| 8300002 | Operation failed. Cannot connect to service. |
| 8300003 | System internal error. |
| 8300999 | Unknown error code. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

let options: call.NumberFormatOptions = {
    countryCode: "CN"
}
call.formatPhoneNumber("138xxxxxxxx", options).then((data: string) => {
    console.info(\`formatPhoneNumber success, promise: data->${JSON.stringify(data)}\`);
}).catch((err: BusinessError) => {
    console.error(\`formatPhoneNumber fail, promise: err->${JSON.stringify(err)}\`);
});

#### call.formatPhoneNumberToE1647+

formatPhoneNumberToE164(phoneNumber: string, countryCode: string, callback: AsyncCallback<string>): void

Converts a phone number into the E.164 format. This API uses an asynchronous callback to return the result.

The phone number must match the specified country code. For example, for a China phone number, the country code must be **CN**. Otherwise, **null** will be returned.

**System capability**: SystemCapability.Telephony.CallManager

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| phoneNumber | string | Yes | Phone number. |
| countryCode | string | Yes | Country code, for example, **CN** (China). All country codes are supported. |
| callback | AsyncCallback<string> | Yes | Callback used to return the result. |

**Error codes**

For details about the error codes, see [ohos.telephony (Telephony) Error Codes](../../error-codes/telephony-error-codes/document.md) and [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2. Incorrect parameters types; |
| 8300001 | Invalid parameter value. |
| 8300002 | Operation failed. Cannot connect to service. |
| 8300003 | System internal error. |
| 8300999 | Unknown error code. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

call.formatPhoneNumberToE164("138xxxxxxxx", "CN", (err: BusinessError, data: string) => {
    if (err) {
        console.error(\`formatPhoneNumberToE164 fail, err->${JSON.stringify(err)}\`);
    } else {
        console.info(\`formatPhoneNumberToE164 success, data->${JSON.stringify(data)}\`);
    }
});

#### call.formatPhoneNumberToE1647+

formatPhoneNumberToE164(phoneNumber: string, countryCode: string): Promise<string>

Converts a phone number into the E.164 format. This API uses a promise to return the result.

The phone number must match the specified country code. For example, for a China phone number, the country code must be **CN**. Otherwise, **null** will be returned.

All country codes are supported.

**System capability**: SystemCapability.Telephony.CallManager

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| phoneNumber | string | Yes | Phone number. |
| countryCode | string | Yes | Country code, for example, **CN** (China). All country codes are supported. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<string> | Promise used to return the result. |

**Error codes**

For details about the error codes, see [ohos.telephony (Telephony) Error Codes](../../error-codes/telephony-error-codes/document.md) and [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2. Incorrect parameters types; |
| 8300001 | Invalid parameter value. |
| 8300002 | Operation failed. Cannot connect to service. |
| 8300003 | System internal error. |
| 8300999 | Unknown error code. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

call.formatPhoneNumberToE164("138xxxxxxxx", "CN").then((data: string) => {
    console.info(\`formatPhoneNumberToE164 success, promise: data->${JSON.stringify(data)}\`);
}).catch((err: BusinessError) => {
    console.error(\`formatPhoneNumberToE164 fail, promise: err->${JSON.stringify(err)}\`);
});

#### DialOptions

Provides an option for determining whether a call is a video call.

**System capability**: SystemCapability.Telephony.CallManager

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| extras | boolean | No | Yes | 
Whether the call is a video call.

\- **true**: video call

\- **false** (default): voice call

 |

#### CallState

Enumerates call states.

**System capability**: SystemCapability.Telephony.CallManager

| Name | Value | Description |
| :-- | :-- | :-- |
| CALL\_STATE\_UNKNOWN | \-1 | The call status fails to be obtained and is unknown. |
| CALL\_STATE\_IDLE | 0 | No call is in progress. |
| CALL\_STATE\_RINGING | 1 | The call is in the ringing or waiting state. |
| CALL\_STATE\_OFFHOOK | 2 | At least one call is in dialing, active, or on hold, and no new incoming call is ringing or waiting. |
| CALL\_STATE\_ANSWERED11+ | 3 | The incoming call is answered. |

#### TelCallState21+

Enumerates call states.

**System capability**: SystemCapability.Telephony.CallManager

| Name | Value | Description |
| :-- | :-- | :-- |
| TEL\_CALL\_STATE\_UNKNOWN | \-1 | The call status fails to be obtained and is unknown. |
| TEL\_CALL\_STATE\_IDLE | 0 | No call is in progress. |
| TEL\_CALL\_STATE\_RINGING | 1 | The call is in the ringing or waiting state. |
| TEL\_CALL\_STATE\_OFFHOOK | 2 | At least one call is being dialed, and no new incoming call is in the ringing or waiting state. |
| TEL\_CALL\_STATE\_ANSWERED | 3 | The incoming call is answered. |
| TEL\_CALL\_STATE\_CONNECTED | 4 | The call is being connected or placed on hold. |

#### EmergencyNumberOptions7+

Provides an option for determining whether a number is an emergency number for the SIM card in the specified slot.

**System capability**: SystemCapability.Telephony.CallManager

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| slotId | number | No | Yes | 
Card slot ID.

\- **0**: card slot 1

\- **1**: card slot 2

 |

#### NumberFormatOptions7+

Provides an option for number formatting.

**System capability**: SystemCapability.Telephony.CallManager

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| countryCode | string | No | Yes | Country code, for example, **CN** (China). All country codes are supported. The default value is **CN**. |
