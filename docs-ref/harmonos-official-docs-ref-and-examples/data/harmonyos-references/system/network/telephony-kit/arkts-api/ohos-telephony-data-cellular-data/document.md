# @ohos.telephony.data (Cellular Data)

The **data** module provides basic mobile data management functions. With the APIs provided by this module, you can obtain the default slot of the SIM card used for mobile data, obtain the cellular data flow type and connection status, and check whether cellular data and roaming are enabled.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/86/v3/wgQqFfS_SP-YfhIt4Vuffg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062354Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=D4DEFD49F723B20DB33AE01C73AB4B3911CCD78C78C07E66F0550E03D047E50D)

The initial APIs of this module are supported since API version 7. Newly added APIs will be marked with a superscript to indicate their earliest API version.

#### Modules to Import

import { data } from '@kit.TelephonyKit';

#### data.getDefaultCellularDataSlotId

getDefaultCellularDataSlotId(callback: AsyncCallback<number>): void

Obtains the default slot of the SIM card used for mobile data. This API uses an asynchronous callback to return the result.

**System capability**: SystemCapability.Telephony.CellularData

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | AsyncCallback<number> | Yes | 
Callback used to return the result.

\- **0**: card slot 1.

\- **1**: card slot 2

\- **2**: slot ID of the mobile data in the eSIM and SkyTone scenarios.

 |

**Example**

import { data } from '@kit.TelephonyKit';
import { BusinessError } from '@kit.BasicServicesKit';

data.getDefaultCellularDataSlotId((err: BusinessError, contextData: number) => {
    if(err) {
        console.error(\`getDefaultCellularDataSlotId fail. code: ${err.code}, message: ${err.message}, contextData: ${contextData}\`);
    } else {
        console.info(\`getDefaultCellularDataSlotId success\`);
    }
});

#### data.getDefaultCellularDataSlotId

getDefaultCellularDataSlotId(): Promise<number>

Obtains the default slot of the SIM card used for mobile data. This API uses a promise to return the result.

**System capability**: SystemCapability.Telephony.CellularData

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<number> | 
Promise used to return the result.

\- **0**: card slot 1.

\- **1**: card slot 2

\- **2**: slot ID of the mobile data in the eSIM and SkyTone scenarios.

 |

**Example**

import { data } from '@kit.TelephonyKit';
import { BusinessError } from '@kit.BasicServicesKit';

data.getDefaultCellularDataSlotId().then((contextData: number) => {
    console.info(\`getDefaultCellularDataSlotId success, contextData: ${contextData}\`);
}).catch((err: BusinessError) => {
    console.error(\`getDefaultCellularDataSlotId fail. code: ${err.code}, message: ${err.message}\`);
});

#### data.getDefaultCellularDataSlotIdSync9+

getDefaultCellularDataSlotIdSync(): number

Card slot ID.

**System capability**: SystemCapability.Telephony.CellularData

**Return value**

| Type | Description |
| :-- | :-- |
| number | 
Card slot ID.

\- **0**: card slot 1.

\- **1**: card slot 2

\- **2**: slot ID of the mobile data in the eSIM and SkyTone scenarios.

 |

**Example**

import { data } from '@kit.TelephonyKit';

console.info("Result: "+ data.getDefaultCellularDataSlotIdSync())

#### data.getCellularDataFlowType

getCellularDataFlowType(callback: AsyncCallback<DataFlowType>): void

Obtains the cellular data flow type, which can be uplink or downlink. This API uses an asynchronous callback to return the result.

**Required permission**: ohos.permission.GET\_NETWORK\_INFO

**System capability**: SystemCapability.Telephony.CellularData

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | AsyncCallback<[DataFlowType](#dataflowtype)\> | Yes | Callback used to return the result. |

**Error codes**

For details about the following error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 201 | Permission denied. |

**Example**

import { data } from '@kit.TelephonyKit';
import { BusinessError } from '@kit.BasicServicesKit';

data.getCellularDataFlowType((err: BusinessError, contextData: data.DataFlowType) => {
    if(err) {
        console.error(\`getCellularDataFlowType fail. code: ${err.code}, message: ${err.message}, contextData: ${contextData}\`);
    } else {
        console.info(\`getCellularDataFlowType success\`);
    }
});

#### data.getCellularDataFlowType

getCellularDataFlowType(): Promise<DataFlowType>

Obtains the cellular data flow type, which can be uplink or downlink. This API uses a promise to return the result.

**Required permission**: ohos.permission.GET\_NETWORK\_INFO

**System capability**: SystemCapability.Telephony.CellularData

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<[DataFlowType](#dataflowtype)\> | Promise used to return the result. |

**Error codes**

For details about the following error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 201 | Permission denied. |

**Example**

import { data } from '@kit.TelephonyKit';
import { BusinessError } from '@kit.BasicServicesKit';

data.getCellularDataFlowType().then((contextData: data.DataFlowType) => {
    console.info(\`getCellularDataFlowType success, contextData: ${contextData}\`);
}).catch((err: BusinessError) => {
    console.error(\`getCellularDataFlowType fail. code: ${err.code}, message: ${err.message}\`);
});

#### data.getCellularDataState

getCellularDataState(callback: AsyncCallback<DataConnectState>): void

Obtains the cellular data connection status. This API uses an asynchronous callback to return the result.

**Required permission**: ohos.permission.GET\_NETWORK\_INFO

**System capability**: SystemCapability.Telephony.CellularData

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | AsyncCallback<[DataConnectState](#dataconnectstate)\> | Yes | Callback used to return the result. |

**Error codes**

For details about the following error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 201 | Permission denied. |

**Example**

import { data } from '@kit.TelephonyKit';
import { BusinessError } from '@kit.BasicServicesKit';

data.getCellularDataState((err: BusinessError, contextData: data.DataConnectState) => {
    if(err) {
        console.error(\`getCellularDataState fail. code: ${err.code}, message: ${err.message}, contextData: ${contextData}\`);
    } else {
        console.info(\`getCellularDataState success\`);
    }
});

#### data.getCellularDataState

getCellularDataState(): Promise<DataConnectState>

Obtains the cellular data connection status. This API uses a promise to return the result.

**Required permission**: ohos.permission.GET\_NETWORK\_INFO

**System capability**: SystemCapability.Telephony.CellularData

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<[DataConnectState](#dataconnectstate)\> | Promise used to return the result. |

**Error codes**

For details about the following error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 201 | Permission denied. |

**Example**

import { data } from '@kit.TelephonyKit';
import { BusinessError } from '@kit.BasicServicesKit';

data.getCellularDataState().then((contextData: data.DataConnectState) => {
    console.info(\`getCellularDataState success, contextData: ${contextData}\`);
}).catch((err: BusinessError) => {
    console.error(\`getCellularDataState fail. code: ${err.code}, message: ${err.message}\`);
});

#### data.isCellularDataEnabled

isCellularDataEnabled(callback: AsyncCallback<boolean>): void

Checks whether the cellular data service is enabled. This API uses an asynchronous callback to return the result.

**Required permission**: ohos.permission.GET\_NETWORK\_INFO

**System capability**: SystemCapability.Telephony.CellularData

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | AsyncCallback<boolean> | Yes | 
Callback used to return the result.

**true**: The cellular data service is enabled.

**false**: The cellular data service is disabled.

 |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md) and [Telephony Error Codes](../../error-codes/telephony-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 201 | Permission denied. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 8300001 | Invalid parameter value. |
| 8300002 | Service connection failed. |
| 8300003 | System internal error. |
| 8300999 | Internal error. |

**Example**

import { data } from '@kit.TelephonyKit';
import { BusinessError } from '@kit.BasicServicesKit';

data.isCellularDataEnabled((err: BusinessError, contextData: boolean) => {
    if(err) {
        console.error(\`isCellularDataEnabled fail. code: ${err.code}, message: ${err.message}, contextData: ${contextData}\`);
    } else {
        console.info(\`isCellularDataEnabled success\`);
    }
});

#### data.isCellularDataEnabled

isCellularDataEnabled(): Promise<boolean>

Checks whether the cellular data service is enabled. This API uses a promise to return the result.

**Required permission**: ohos.permission.GET\_NETWORK\_INFO

**System capability**: SystemCapability.Telephony.CellularData

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<boolean> | 
Promise used to return the result.

**true**: The cellular data service is enabled.

**false**: The cellular data service is disabled.

 |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md) and [Telephony Error Codes](../../error-codes/telephony-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 201 | Permission denied. |
| 8300002 | Service connection failed. |
| 8300003 | System internal error. |
| 8300999 | Internal error. |

**Example**

import { data } from '@kit.TelephonyKit';
import { BusinessError } from '@kit.BasicServicesKit';

data.isCellularDataEnabled().then((contextData: boolean) => {
    console.info(\`isCellularDataEnabled success, contextData: ${contextData}\`);
}).catch((err: BusinessError) => {
    console.error(\`isCellularDataEnabled fail. code: ${err.code}, message: ${err.message}\`);
});

#### data.isCellularDataEnabledSync12+

isCellularDataEnabledSync(): boolean

Checks whether the cellular data service is enabled. This API returns the result synchronously.

**Required permission**: ohos.permission.GET\_NETWORK\_INFO

**System capability**: SystemCapability.Telephony.CellularData

**Return value**

| Type | Description |
| :-- | :-- |
| boolean | 
Whether the cellular data service is enabled.

**true**: The cellular data service is enabled.

**false**: The cellular data service is disabled.

 |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md) and [Telephony Error Codes](../../error-codes/telephony-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 201 | Permission denied. |
| 8300002 | Operation failed. Cannot connect to service. |
| 8300003 | System internal error. |
| 8300999 | Internal error. |

**Example**

import { data } from '@kit.TelephonyKit';

try {
    let isEnabled: boolean = data.isCellularDataEnabledSync();
    console.info(\`isCellularDataEnabledSync success : ${isEnabled}\`);
} catch (err) {
    console.error(\`isCellularDataEnabledSync fail. code: ${err.code}, message: ${err.message}\`);
}

#### data.isCellularDataRoamingEnabled

isCellularDataRoamingEnabled(slotId: number, callback: AsyncCallback<boolean>): void

Checks whether roaming is enabled for the cellular data service. This API uses an asynchronous callback to return the result.

**Required permission**: ohos.permission.GET\_NETWORK\_INFO

**System capability**: SystemCapability.Telephony.CellularData

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| slotId | number | Yes | 
Card slot ID.

\- **0**: card slot 1.

\- **1**: card slot 2

 |
| callback | AsyncCallback<boolean> | Yes | 

Callback used to return the result.

**true**: Roaming is enabled for the cellular data service.

**false**: Roaming is disabled for the cellular data service.

 |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md) and [Telephony Error Codes](../../error-codes/telephony-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 201 | Permission denied. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 8300001 | Invalid parameter value. |
| 8300002 | Service connection failed. |
| 8300003 | System internal error. |
| 8300999 | Internal error. |

**Example**

import { data } from '@kit.TelephonyKit';
import { BusinessError } from '@kit.BasicServicesKit';

data.isCellularDataRoamingEnabled(0, (err: BusinessError, contextData: boolean) => {
    if(err) {
        console.error(\`isCellularDataRoamingEnabled fail. code: ${err.code}, message: ${err.message}, contextData: ${contextData}\`);
    } else {
        console.info(\`isCellularDataRoamingEnabled success\`);
    }
});

#### data.isCellularDataRoamingEnabled

isCellularDataRoamingEnabled(slotId: number): Promise<boolean>

Checks whether roaming is enabled for the cellular data service. This API uses a promise to return the result.

**Required permission**: ohos.permission.GET\_NETWORK\_INFO

**System capability**: SystemCapability.Telephony.CellularData

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| slotId | number | Yes | 
Card slot ID.

\- **0**: card slot 1.

\- **1**: card slot 2

 |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<boolean> | 
Promise used to return the result.

**true**: Roaming is enabled for the cellular data service.

**false**: Roaming is disabled for the cellular data service.

 |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md) and [Telephony Error Codes](../../error-codes/telephony-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 201 | Permission denied. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 8300001 | Invalid parameter value. |
| 8300002 | Service connection failed. |
| 8300003 | System internal error. |
| 8300999 | Internal error. |

**Example**

import { data } from '@kit.TelephonyKit';
import { BusinessError } from '@kit.BasicServicesKit';

data.isCellularDataRoamingEnabled(0).then((contextData: boolean) => {
    console.info(\`isCellularDataRoamingEnabled success, contextData: ${contextData}\`);
}).catch((err: BusinessError) => {
    console.error(\`isCellularDataRoamingEnabled fail. code: ${err.code}, message: ${err.message}\`);
});

#### data.isCellularDataRoamingEnabledSync12+

isCellularDataRoamingEnabledSync(slotId: number): boolean

Checks whether roaming is enabled for the cellular data service. This API returns the result synchronously.

**Required permission**: ohos.permission.GET\_NETWORK\_INFO

**System capability**: SystemCapability.Telephony.CellularData

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| slotId | number | Yes | 
Card slot ID.

\- **0**: card slot 1.

\- **1**: card slot 2

 |

**Return value**

| Type | Description |
| :-- | :-- |
| boolean | 
Whether roaming is enabled for the cellular data service.

**true**: Roaming is enabled for the cellular data service.

**false**: Roaming is disabled for the cellular data service.

 |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md) and [Telephony Error Codes](../../error-codes/telephony-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 201 | Permission denied. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameters types. |
| 8300001 | Invalid parameter value. |
| 8300002 | Operation failed. Cannot connect to service. |
| 8300003 | System internal error. |
| 8300999 | Internal error. |

**Example**

import { data } from '@kit.TelephonyKit';

try {
    let isEnabled: boolean = data.isCellularDataRoamingEnabledSync(0);
    console.info(\`isCellularDataRoamingEnabledSync success : ${isEnabled}\`);
} catch (err) {
    console.error(\`isCellularDataRoamingEnabledSync fail. code: ${err.code}, message: ${err.message}\`);
}

#### data.getDefaultCellularDataSimId10+

getDefaultCellularDataSimId(): number

Obtains the default ID of the SIM card used for mobile data.

**System capability**: SystemCapability.Telephony.CellularData

**Return value**

| Type | Description |
| :-- | :-- |
| number | 
Obtains the default ID of the SIM card used for mobile data.

The return value is bound to the SIM card and increases from 1.

\- **0**: no SIM card.

\- **9999**: ID of the SIM card used for mobile data in the eSIM scenario.

\- **99999**: ID of the SIM card used for mobile data in the SkyTone scenario. The default value is **99999**.

 |

**Example**

import { data } from '@kit.TelephonyKit';

console.info("Result: "+ data.getDefaultCellularDataSimId());

#### data.queryAllApns16+

queryAllApns(): Promise<Array<ApnInfo>>

Obtains the access point name (APN) of the default SIM card used for mobile data. This API returns the result asynchronously.

**Required permissions**: ohos.permission.MANAGE\_APN\_SETTING (Restricted permission used only to connect to the mobile data private network for office tasks. For details, see [Restricted Permissions](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/restricted-permissions#ohospermissionmanage_apn_setting).)

**System capability**: SystemCapability.Telephony.CellularData

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<Array<[ApnInfo](#apninfo16)\>> | Promise used to return the result. |

**Error codes**

For details about the following error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 201 | Permission denied. |

**Example**

import { data } from '@kit.TelephonyKit';
import { BusinessError } from '@kit.BasicServicesKit';

data.queryAllApns().then((apnInfos: Array<data.ApnInfo>) => {
    console.info(\`queryAllApns success, promise: apnInfos->${JSON.stringify(apnInfos)}\`);
}).catch((err: BusinessError) => {
    console.error(\`queryAllApns failed. code: ${err.code}, message: ${err.message}\`);
});

#### data.queryApnIds16+

queryApnIds(apnInfo: ApnInfo): Promise<Array<number>>

Obtains the APN ID corresponding to the specified **ApnInfo**. This API returns the result asynchronously.

**Required permissions**: ohos.permission.MANAGE\_APN\_SETTING (Restricted permission used only to connect to the mobile data private network for office tasks. For details, see [Restricted Permissions](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/restricted-permissions#ohospermissionmanage_apn_setting).)

**System capability**: SystemCapability.Telephony.CellularData

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| apnInfo | [ApnInfo](#apninfo16) | Yes | APN to query. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<Array<number>> | Promise used to return the result. |

**Error codes**

For details about the following error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 201 | Permission denied. |

**Example**

import { data } from '@kit.TelephonyKit';
import { BusinessError } from '@kit.BasicServicesKit';

let apnInfo: data.ApnInfo;
apnInfo = {
  apnName: "CMNET",
  apn: "cmnet",
  mcc: "460",
  mnc: "07",
};

data.queryApnIds(apnInfo).then((apnIds: Array<number>) => {
    console.info(\`queryApnIds success, apnIds: ${apnIds}\`);
}).catch((err: BusinessError) => {
    console.error(\`queryApnIds failed. code: ${err.code}, message: ${err.message}\`);
});

#### data.setPreferredApn16+

setPreferredApn(apnId: number): Promise<boolean>

Sets the APN corresponding to the specified **apnId** as the preferred APN. This API returns the result asynchronously.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f4/v3/RKVK8Hv-Q1OoXMEdALWlVA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062354Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=707931F9C5B33FE64E6E5690C0C9A9EACE0D8B4BD2277D76B77A1AB2B51A242B)

If the input APN ID is invalid, the default preferred APN configured by the carrier is used.

**Required permissions**: ohos.permission.MANAGE\_APN\_SETTING (Restricted permission used only to connect to the mobile data private network for office tasks. For details, see [Restricted Permissions](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/restricted-permissions#ohospermissionmanage_apn_setting).)

**System capability**: SystemCapability.Telephony.CellularData

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| apnId | number | Yes | APN ID, which can be obtained by calling [queryApnIds](#dataqueryapnids16). |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<boolean> | Promise used to return the result. If no SIM card is installed, the value **false** is returned. |

**Error codes**

For details about the following error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 201 | Permission denied. |

**Example**

import { data } from '@kit.TelephonyKit';
import { BusinessError } from '@kit.BasicServicesKit';

let apnId: number = 0; // apnId is a valid value returned by queryApnIds. If an invalid APN ID is passed to setPreferredApn, the default preferred APN configured by the carrier is used.
data.setPreferredApn(apnId).then((result: boolean) => {
    console.info(\`setPreferredApn result: ${result}\`);
}).catch((err: BusinessError) => {
    console.error(\`setPreferredApn failed. code: ${err.code}, message: ${err.message}\`);
});

#### data.getActiveApnName20+

getActiveApnName(): Promise<string>

Obtains the access point name (APN) of the default SIM card used for mobile data. This API returns the result asynchronously.

**Required permission**: ohos.permission.GET\_NETWORK\_INFO

**System capability**: SystemCapability.Telephony.CellularData

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<string> | Promise used to return the result. If mobile data is not activated, an empty string is returned. |

**Error codes**

For details about the following error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 201 | Permission denied. |

**Example**

import { data } from '@kit.TelephonyKit';
import { BusinessError } from '@kit.BasicServicesKit';

data.getActiveApnName().then((apn: string) => {
    console.info(\`getActiveApnName success, apn: ${apn}\`);
}).catch((err: BusinessError) => {
    console.error(\`getActiveApnName failed. code: ${err.code}, message: ${err.message}\`);
});

#### DataFlowType

Defines the cellular data flow type.

**System capability**: SystemCapability.Telephony.CellularData

| Name | Value | Description |
| :-- | :-- | :-- |
| DATA\_FLOW\_TYPE\_NONE | 0 | No uplink or downlink data is available. |
| DATA\_FLOW\_TYPE\_DOWN | 1 | Only the downlink data is available. |
| DATA\_FLOW\_TYPE\_UP | 2 | Only the uplink data is available. |
| DATA\_FLOW\_TYPE\_UP\_DOWN | 3 | Both the uplink data and downlink data are available. |
| DATA\_FLOW\_TYPE\_DORMANT | 4 | No uplink or downlink data is available because the lower-layer link is in the dormant state. |

#### DataConnectState

Describes the connection status of a cellular data link.

**System capability**: SystemCapability.Telephony.CellularData

| Name | Value | Description |
| :-- | :-- | :-- |
| DATA\_STATE\_UNKNOWN | \-1 | The status of the cellular data link is unknown. |
| DATA\_STATE\_DISCONNECTED | 0 | The cellular data link is disconnected. |
| DATA\_STATE\_CONNECTING | 1 | The cellular data link is being connected. |
| DATA\_STATE\_CONNECTED | 2 | The cellular data link is connected. |
| DATA\_STATE\_SUSPENDED | 3 | The cellular data link is suspended. |

#### ApnInfo16+

Defines the APN information.

**System capability**: SystemCapability.Telephony.CellularData

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| apnName | string | No | No | APN name. |
| apn | string | No | No | APN. |
| mcc | string | No | No | Mobile country code (MCC) of the SIM card. |
| mnc | string | No | No | Mobile network code (MNC) of the SIM card. |
| user | string | No | Yes | User name. |
| type | string | No | Yes | APN type. |
| proxy | string | No | Yes | Proxy address. |
| mmsproxy | string | No | Yes | Multimedia messaging service (MMS) proxy. |
