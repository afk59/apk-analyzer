# @ohos.connectedTag (Active Tags)

The **connectedTag** module provides APIs for using active tags. You can use the APIs to initialize the active tag chip and read and write active tags.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/25/v3/BWZ-fCJQRESndWQeJD18nQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062341Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=A0677FDE4BF77005AEBAB15E5F4C96FDFAC034F022FD3188A37375F441000B7F)

The initial APIs of this module are supported since API version 8. Newly added APIs will be marked with a superscript to indicate their earliest API version.

#### Modules to Import

import { connectedTag } from '@kit.ConnectivityKit';

#### connectedTag.init(deprecated)

init(): boolean

Initializes the active tag chip.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5a/v3/xuNq3b12QsaTz4g8i6FbPQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062341Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=EA7E9F64CAA77EAB97D38E8028F2381A94BE71CD4681CB3FFAF0715F3A1CFBB1)

This API is supported since API version 8 and deprecated since API version 9. Use [initialize](#connectedtaginitialize9) instead.

**Required permissions**: ohos.permission.NFC\_TAG

**System capability**: SystemCapability.Communication.ConnectedTag

**Return value**

| **Type** | **Description** |
| :-- | :-- |
| boolean | 
**true**: The initialization is successful.

**false**: The initialization fails.

 |

#### connectedTag.initialize9+

initialize(): void

Initializes the active tag chip.

**Required permissions**: ohos.permission.NFC\_TAG

**System capability**: SystemCapability.Communication.ConnectedTag

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md) and [NFC Error Codes](../../error-codes/nfc-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 201 | Permission denied. |
| 801 | Capability not supported. |
| 3200101 | Connected NFC tag running state is abnormal in service. |

#### connectedTag.uninit(deprecated)

uninit(): boolean

Uninitializes the active tag resources.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/50/v3/0RRjVTENTfadWIjq1qLGkQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062341Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=A0BD3D45CCA45CD64D25B68E977EA5DA1008A50B45B0A7FEC215E6FCB4BB635B)

This API is supported since API version 8 and deprecated since API version 9. Use [uninitialize](#connectedtaguninitialize9) instead.

**Required permissions**: ohos.permission.NFC\_TAG

**System capability**: SystemCapability.Communication.ConnectedTag

**Return value**

| **Type** | **Description** |
| :-- | :-- |
| boolean | 
**true**: The uninstallation is successful.

**false**: The uninstallation fails.

 |

#### connectedTag.uninitialize9+

uninitialize(): void

Uninitializes the active tag resources.

**Required permissions**: ohos.permission.NFC\_TAG

**System capability**: SystemCapability.Communication.ConnectedTag

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md) and [NFC Error Codes](../../error-codes/nfc-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 201 | Permission denied. |
| 801 | Capability not supported. |
| 3200101 | Connected NFC tag running state is abnormal in service. |

#### connectedTag.readNdefTag(deprecated)

readNdefTag(): Promise<string>

Reads the content of this active tag. This API uses a promise to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1a/v3/2cIujsa_QUOolADKYIjmnQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062341Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=05E370F7A84E03CAB0991ED4DCF812F15B9615B21958D6B174618B5BF7E74A7D)

This API is supported since API version 8 and deprecated since API version 9. Use [uninitialize](#connectedtaguninitialize9) instead.

**Required permissions**: ohos.permission.NFC\_TAG

**System capability**: SystemCapability.Communication.ConnectedTag

**Return value**

| **Type** | **Description** |
| :-- | :-- |
| Promise<string> | Promise used to return the content of the active tag. |

**Example**

import { connectedTag } from '@kit.ConnectivityKit';
import { BusinessError } from '@kit.BasicServicesKit';

connectedTag.readNdefTag().then((data) => {
    console.info("connectedTag readNdefTag Promise data = " + data);
}).catch((err: BusinessError)=> {
    console.error("connectedTag readNdefTag Promise err: " + err);
});

#### connectedTag.read9+

read(): Promise<number\[\]>

Reads the content of this active tag. This API uses a promise to return the result.

**Required permissions**: ohos.permission.NFC\_TAG

**System capability**: SystemCapability.Communication.ConnectedTag

**Return value**

| **Type** | **Description** |
| :-- | :-- |
| Promise<number\[\]> | Promise used to return the content of the active tag. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md) and [NFC Error Codes](../../error-codes/nfc-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 201 | Permission denied. |
| 801 | Capability not supported. |
| 3200101 | Connected NFC tag running state is abnormal in service. |

**Example**

import { connectedTag } from '@kit.ConnectivityKit';
import { BusinessError } from '@kit.BasicServicesKit';

connectedTag.read().then((data) => {
    console.info("connectedTag read Promise data = " + data);
}).catch((err: BusinessError)=> {
    console.error("connectedTag read Promise err: " + err);
});

#### connectedTag.readNdefTag(deprecated)

readNdefTag(callback: AsyncCallback<string>): void

Reads the content of this active tag. This API uses an asynchronous callback to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/82/v3/cuQmuo7GQXinbleiRRU5QA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062341Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=FB959679B917129E3989708F02F7C0947BDE7D2D3746333A01ACA42296174FD5)

This API is supported since API version 8 and deprecated since API version 9. Use [uninitialize](#connectedtaguninitialize9) instead.

**Required permissions**: ohos.permission.NFC\_TAG

**System capability**: SystemCapability.Communication.ConnectedTag

**Parameters**

| **Name** | **Type** | **Mandatory** | **Description** |
| :-- | :-- | :-- | :-- |
| callback | AsyncCallback<string> | Yes | Callback used to return the active tag content obtained. |

**Example**

import { connectedTag } from '@kit.ConnectivityKit';

connectedTag.readNdefTag((err, data)=> {
    if (err) {
        console.error("connectedTag readNdefTag AsyncCallback err: " + err);
    } else {
        console.info("connectedTag readNdefTag AsyncCallback data: " + data);
    }
});

#### connectedTag.read9+

read(callback: AsyncCallback<number\[\]>): void

Reads the content of this active tag. This API uses an asynchronous callback to return the result.

**Required permissions**: ohos.permission.NFC\_TAG

**System capability**: SystemCapability.Communication.ConnectedTag

**Parameters**

| **Name** | **Type** | **Mandatory** | **Description** |
| :-- | :-- | :-- | :-- |
| callback | AsyncCallback<number\[\]> | Yes | Callback used to return the active tag content obtained. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md) and [NFC Error Codes](../../error-codes/nfc-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 201 | Permission denied. |
| 801 | Capability not supported. |
| 3200101 | Connected NFC tag running state is abnormal in service. |

**Example**

import { connectedTag } from '@kit.ConnectivityKit';

connectedTag.read((err, data)=> {
    if (err) {
        console.error("connectedTag read AsyncCallback err: " + err);
    } else {
        console.info("connectedTag read AsyncCallback data: " + data);
    }
});

#### connectedTag.writeNdefTag(deprecated)

writeNdefTag(data: string): Promise<void>

Writes data to this active tag. This API uses a promise to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a4/v3/wmbJaJskTDyGKYzapxjanA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062341Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=F0B95DC3F032D2948B0E8EFFB5A7A2457CC11B889237C0F15889034ABCDFD203)

This API is supported since API version 8 and deprecated since API version 9. Use [connectedTag.write](#connectedtagwrite9) instead.

**Required permissions**: ohos.permission.NFC\_TAG

**System capability**: SystemCapability.Communication.ConnectedTag

**Parameters**

| **Name** | **Type** | **Mandatory** | **Description** |
| :-- | :-- | :-- | :-- |
| data | string | Yes | Data to be written to the active tag. The maximum length is 1024 bytes. |

**Return value**

| **Type** | **Description** |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Example**

import { connectedTag } from '@kit.ConnectivityKit';
import { BusinessError } from '@kit.BasicServicesKit';

let rawData = "010203"; // change it to be correct.
connectedTag.writeNdefTag(rawData).then(() => {
    console.info("connectedTag.writeNdefTag Promise success.");
}).catch((err: BusinessError)=> {
    console.error("connectedTag.writeNdefTag Promise err: " + err);
});

#### connectedTag.write9+

write(data: number\[\]): Promise<void>

Writes data to this active tag. This API uses a promise to return the result.

**Required permissions**: ohos.permission.NFC\_TAG

**System capability**: SystemCapability.Communication.ConnectedTag

**Parameters**

| **Name** | **Type** | **Mandatory** | **Description** |
| :-- | :-- | :-- | :-- |
| data | number\[\] | Yes | Data to be written to the active tag. The value is a hexadecimal number ranging from 0x00 to 0xFF. |

**Return value**

| **Type** | **Description** |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md) and [NFC Error Codes](../../error-codes/nfc-error-codes/document.md).

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
| 3200101 | Connected NFC tag running state is abnormal in service. |

**Example**

import { connectedTag } from '@kit.ConnectivityKit';
import { BusinessError } from '@kit.BasicServicesKit';

let rawData = \[0x01, 0x02, 0x03\]; // change it to be correct.
connectedTag.write(rawData).then(() => {
    console.info("connectedTag.writeNdefTag Promise success.");
}).catch((err: BusinessError)=> {
    console.error("connectedTag.writeNdefTag Promise err: " + err);
});

#### connectedTag.writeNdefTag(deprecated)

writeNdefTag(data: string, callback: AsyncCallback<void>): void

Writes data to this active tag. This API uses an asynchronous callback to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/17/v3/3lcFBiDwRrW28u77mKUipg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062341Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=F643130726AEA6FEABD82239FAC20A78AD99E661E88BD29A1DAD2E092888D8D6)

This API is supported since API version 8 and deprecated since API version 9. Use [connectedTag.write](#connectedtagwrite9) instead.

**Required permissions**: ohos.permission.NFC\_TAG

**System capability**: SystemCapability.Communication.ConnectedTag

**Parameters**

| **Name** | **Type** | **Mandatory** | **Description** |
| :-- | :-- | :-- | :-- |
| data | string | Yes | Data to be written to the active tag. The maximum length is 1024 bytes. |
| callback | AsyncCallback<void> | Yes | Callback used to return the active tag content obtained. |

**Example**

import { connectedTag } from '@kit.ConnectivityKit';

let rawData = "010203"; // change it to be correct.
connectedTag.writeNdefTag(rawData, (err)=> {
    if (err) {
        console.error("connectedTag.writeNdefTag AsyncCallback err: " + err);
    } else {
        console.info("connectedTag.writeNdefTag AsyncCallback success.");
    }
});

#### connectedTag.write9+

write(data: number\[\], callback: AsyncCallback<void>): void

Writes data to this active tag. This API uses an asynchronous callback to return the result.

**Required permissions**: ohos.permission.NFC\_TAG

**System capability**: SystemCapability.Communication.ConnectedTag

**Parameters**

| **Name** | **Type** | **Mandatory** | **Description** |
| :-- | :-- | :-- | :-- |
| data | number\[\] | Yes | Data to be written to the active tag. The value is a hexadecimal number ranging from 0x00 to 0xFF. |
| callback | AsyncCallback<void> | Yes | Callback used to return the active tag content obtained. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md) and [NFC Error Codes](../../error-codes/nfc-error-codes/document.md).

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
| 3200101 | Connected NFC tag running state is abnormal in service. |

**Example**

import { connectedTag } from '@kit.ConnectivityKit';

let rawData = \[0x01, 0x02, 0x03\]; // change it to be correct.
connectedTag.write(rawData, (err)=> {
    if (err) {
        console.error("connectedTag.writeNdefTag AsyncCallback err: " + err);
    } else {
        console.info("connectedTag.writeNdefTag AsyncCallback success.");
    }
});

#### connectedTag.on('notify')

on(type: "notify", callback: Callback<number>): void

Registers the NFC field strength state events.

**Required permissions**: ohos.permission.NFC\_TAG

**System capability**: SystemCapability.Communication.ConnectedTag

**Parameters**

| **Name** | **Type** | **Mandatory** | **Description** |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Event type. This parameter has a fixed value of **notify**. |
| callback | Callback<number> | Yes | Callback used to return the [NfcRfType](#nfcrftype). |

#### connectedTag.off('notify')

off(type: "notify", callback?: Callback<number>): void

Unregisters the NFC field strength state events.

**Required permissions**: ohos.permission.NFC\_TAG

**System capability**: SystemCapability.Communication.ConnectedTag

**Parameters**

| **Name** | **Type** | **Mandatory** | **Description** |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Event type. This parameter has a fixed value of **notify**. |
| callback | Callback<number> | No | Callback used to return the field strength state. If this parameter is not specified, all callbacks associated with the specified event will be unregistered. |

**Example**

import { connectedTag } from '@kit.ConnectivityKit';

function nfcStatusCb(rfState: connectedTag.NfcRfType) {
    console.info("connectedTag on Callback rfState: ", rfState);
}

// Process of using an active NFC tag
async function nfcTagTestOn(): Promise<void> {
    try {
        console.info("connectedTag initialize");
        connectedTag.initialize();
    } catch (error) {
        console.error("initialize error:" + error);
    }
    // Register a callback for NFC status change events.
    connectedTag.on("notify", nfcStatusCb);
    try {
        let tag = \[3, 1, 0\];
        console.info("connectedTag write: tag=" + tag);
        await connectedTag.write(tag);
        let data = await connectedTag.read();
        console.info("connectedTag read: data=" + data);
    } catch (error) {
        console.error("connectedTag error: " + error);
    }
}

// Unregister the callback for NFC status change events and uninitialize the NFC tag.
async function nfcTagTestOff(): Promise<void> {
    // Unregister the callback for NFC status change events.
    connectedTag.off("notify", nfcStatusCb);
    try {
        console.info("connectedTag uninitialize");
        connectedTag.uninitialize();
    } catch (error) {
        console.error("connectedTag error: " + error);
    }
}

export { nfcTagTestOn, nfcTagTestOff }

#### NfcRfType

Enumerates the NFC field strength states.

**System capability**: SystemCapability.Communication.ConnectedTag

| Name | Value | Description |
| :-- | :-- | :-- |
| NFC\_RF\_LEAVE | 0 | NFC exit. |
| NFC\_RF\_ENTER | 1 | NFC entry. |
