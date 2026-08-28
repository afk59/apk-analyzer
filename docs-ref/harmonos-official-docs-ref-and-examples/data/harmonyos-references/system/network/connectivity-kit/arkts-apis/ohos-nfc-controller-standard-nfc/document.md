# @ohos.nfc.controller (Standard NFC)

The **nfcController** module provides APIs for opening and closing Near-Field Communication (NFC) and reading the NFC state.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a7/v3/NhqXlgiKTPeyzo8sCgzIKA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062341Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=842C043483D4707FC95D41BC386C589FC9499717EB2A9EE39ADEABCFF84566DB)

The initial APIs of this module are supported since API version 7. Newly added APIs will be marked with a superscript to indicate their earliest API version.

#### **Modules to Import**

import { nfcController } from '@kit.ConnectivityKit';

#### NfcState

Enumerates the NFC states.

**System capability**: SystemCapability.Communication.NFC.Core

**Atomic service API**: This API can be used in atomic services since API version 12.

| Name | Value | Description |
| :-- | :-- | :-- |
| STATE\_OFF | 1 | NFC is closed (OFF). |
| STATE\_TURNING\_ON | 2 | NFC is turning on. |
| STATE\_ON | 3 | NFC is open (ON). |
| STATE\_TURNING\_OFF | 4 | NFC is turning off. |

#### nfcController.isNfcAvailable(deprecated)

isNfcAvailable(): boolean

Checks whether the device supports NFC.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/94/v3/JPvSvaGeSjiRikhsMKDiIA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062341Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=D68CEACD5FEE85E12E4704173564029822EA5ABB0BD7AADC1874921D2AE1FD0D)

This API is supported since API version 7 and deprecated since API version 9. Use [canIUse("SystemCapability.Communication.NFC.Core")](../../../../../common-capabilities/c-api/modules/init/document.md#caniuse) instead.

**System capability**: SystemCapability.Communication.NFC.Core

**Return value**

| **Type** | **Description** |
| :-- | :-- |
| boolean | Returns **true** if the device supports NFC; returns **false** otherwise. |

#### nfcController.openNfc(deprecated)

openNfc(): boolean

Opens NFC.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5f/v3/rQ0Bhh3sSoinbXHFmKxuYw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062341Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=F7C674EA89665C009127EE6BA4BEFC291C9F810BCCB20D58D5A92C4F3FEC0E0F)

This API is supported since API version 7 and deprecated since API version 9. Use [enableNfc](#nfccontrollerenablenfc9) instead.

**Required permissions**: ohos.permission.MANAGE\_SECURE\_SETTINGS (available only for system applications)

**System capability**: SystemCapability.Communication.NFC.Core

**Return value**

| **Type** | **Description** |
| :-- | :-- |
| boolean | Returns **true** if the operation is successful; returns **false** otherwise. |

#### nfcController.enableNfc9+

enableNfc(): void

Enables NFC. This API can be called only by system applications.

**Required permissions**: ohos.permission.MANAGE\_SECURE\_SETTINGS (available only for system applications)

**System capability**: SystemCapability.Communication.NFC.Core

**Error codes**

For details about the error codes, see [NFC Error Codes](../../error-codes/nfc-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 201 | Permission denied. |
| 801 | Capability not supported. |
| 3100101 | The NFC state is abnormal in the service. |

#### nfcController.closeNfc(deprecated)

closeNfc(): boolean

Closes NFC.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1f/v3/Cj1GO8iNRm2oHgk5Su7Utg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062341Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=6F1E2D9C9833F2A7883C43443EC2AEFCDF3A0BCE7C196BCD983B94C96D19D554)

This API is supported since API version 7 and deprecated since API version 9. Use [disableNfc](#nfccontrollerdisablenfc9) instead.

**Required permissions**: ohos.permission.MANAGE\_SECURE\_SETTINGS (available only for system applications)

**System capability**: SystemCapability.Communication.NFC.Core

**Return value**

| **Type** | **Description** |
| :-- | :-- |
| boolean | Returns **true** if the operation is successful; returns **false** otherwise. |

#### nfcController.disableNfc9+

disableNfc(): void

Disables NFC. This API can be called only by system applications.

**Required permissions**: ohos.permission.MANAGE\_SECURE\_SETTINGS (available only for system applications)

**System capability**: SystemCapability.Communication.NFC.Core

**Error codes**

For details about the error codes, see [NFC Error Codes](../../error-codes/nfc-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 201 | Permission denied. |
| 801 | Capability not supported. |
| 3100101 | The NFC state is abnormal in the service. |

#### nfcController.isNfcOpen

isNfcOpen(): boolean

Checks whether NFC is open.

**System capability**: SystemCapability.Communication.NFC.Core

**Atomic service API**: This API can be used in atomic services since API version 12.

**Return value**

| **Type** | **Description** |
| :-- | :-- |
| boolean | Returns **true** if NFC is open; returns **false** otherwise. |

#### nfcController.getNfcState

getNfcState(): [NfcState](#nfcstate)

Obtains the NFC state.

**System capability**: SystemCapability.Communication.NFC.Core

**Atomic service API**: This API can be used in atomic services since API version 12.

**Return value**

| **Type** | **Description** |
| :-- | :-- |
| [NfcState](#nfcstate) | NFC state obtained. For details, see [NfcState](#nfcstate). |

#### nfcController.on('nfcStateChange')

on(type: 'nfcStateChange', callback: Callback<[NfcState](#nfcstate)\>): void

Enables listening for NFC state changes. This API uses an asynchronous callback to return the result.

**System capability**: SystemCapability.Communication.NFC.Core

**Atomic service API**: This API can be used in atomic services since API version 12.

**Parameters**

| **Name** | **Type** | **Mandatory** | **Description** |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Event type. The value is **nfcStateChange**. |
| callback | Callback<[NfcState](#nfcstate)\> | Yes | Callback used to return the NFC state. |

#### nfcController.off('nfcStateChange')

off(type: 'nfcStateChange', callback?: Callback<[NfcState](#nfcstate)\>): void

Unsubscribes from the NFC state changes. Upon successful unsubscription, the subscriber will not receive NFC state change notifications. This API uses an asynchronous callback to return the result.

**System capability**: SystemCapability.Communication.NFC.Core

**Atomic service API**: This API can be used in atomic services since API version 12.

**Parameters**

| **Name** | **Type** | **Mandatory** | **Description** |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Event type. The value is **nfcStateChange**. |
| callback | Callback<[NfcState](#nfcstate)\> | No | Callback for the NFC state changes. This parameter can be left blank. If this parameter is not specified, this API unregisters all callbacks for the specified event. |

**Example**

import { nfcController } from '@kit.ConnectivityKit';

// Register a callback for NFC status change events.
nfcController.on("nfcStateChange", (nfcState : number)=> {
  console.info("nfcController on callback nfcState: " + nfcState);
});

// Declare the ohos.permission.MANAGE\_SECURE\_SETTINGS permission for enabling NFC. This permission is available only for system applications.
if (!nfcController.isNfcOpen()) {
  // Use enableNfc to enable NFC since API version 9.
  try {
    nfcController.enableNfc();
    console.info("nfcController enableNfc success");
  } catch (businessError) {
    console.error("nfcController enableNfc businessError: " + businessError);
  }
} else {
  console.info("nfcController NFC has been opened");
}

// Declare the ohos.permission.MANAGE\_SECURE\_SETTINGS permission for disabling NFC. This permission is available only for system applications.
if (nfcController.isNfcOpen()) {
  // Use disableNfc to disable NFC since API version 9.
  try {
    nfcController.disableNfc();
    console.info("nfcController disableNfc success");
  } catch (businessError) {
    console.error("nfcController disableNfc businessError: " + businessError);
  }
} else {
  console.info("nfcController NFC has been closed");
}

// Unregister the callback for NFC status change events.
nfcController.off("nfcStateChange");
