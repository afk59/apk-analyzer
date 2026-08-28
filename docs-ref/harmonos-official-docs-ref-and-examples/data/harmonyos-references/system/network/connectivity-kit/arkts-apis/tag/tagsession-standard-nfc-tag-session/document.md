# tagSession (Standard NFC Tag Session)

The **tagSession** module provides common APIs for establishing connections and transferring data.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fe/v3/4xIZbiAdSGewBx9iMi2NLg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062342Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=3BEC8C29E5DEBDC20CD5839F913238E9A311779E36FCADD23CF263904AE683C5)

The initial APIs of this module are supported since API version 7. Newly added APIs will be marked with a superscript to indicate their earliest API version.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/46/v3/d30Rul6PQ2mxAXPOx6TNMw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062342Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=C7CA26E76714BB8CD507D024E53FF7F23E49FB0A95144235AAF72E3BF54C5B07)

If an error is reported while importing the tag module editor, the capabilities of a specific device model may exceed the capability set defined for the default device. To use these capabilities, configure a custom SysCap by following instructions in [SystemCapability Development](../../../../../../api-reference-overview/systemcapability/document.md).

#### **Modules to Import**

import { tag } from '@kit.ConnectivityKit';

#### TagSession

Provides common APIs for establishing connections and transferring data. **TagSession** is the base class of all [NFC tag technologies](../nfctech-standard-nfc-technologies/document.md).

A child class instance is required to access the following interfaces. You can use **get** API to obtain a child class instance.

The specific API varies with the NFC tag technology in use. For details, see [NFC Tags](../../ohos-nfc-tag-standard-nfc-tags/document.md).

#### \[h2\]getTagInfo(deprecated)

getTagInfo(): tag.TagInfo

Obtains the **tagInfo** object provided by the NFC service when the tag is dispatched.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/23/v3/pLivcl7qQQ-Lj2K8H13kuw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062342Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=CB9D9E2C875EAF1F21EE296A992AA70200F363F5FE163AB8EDBBEE61C5DDDEE1)

This API is supported since API version 7 and deprecated since API version 9. Use [tag.getTagInfo](../../ohos-nfc-tag-standard-nfc-tags/document.md#taggettaginfo9) instead.

**Required permissions**: ohos.permission.NFC\_TAG

**System capability**: SystemCapability.Communication.NFC.Tag

**Return value**

| **Type** | **Description** |
| :-- | :-- |
| tag.TagInfo | **Taginfo** object obtained. |

**Example**

import { tag } from '@kit.ConnectivityKit';

// tagInfo is the object provided by the NFC service when allocating a tag. For details, see tag.TagInfo in @ohos.nfc.tag.
// getter API, which can be getIsoDep, getNdef, getMifareClassic, and so on.

let tagInfo : TagInfo = tag.getIsoDep(tagInfo).getTagInfo();
console.info("tag tagInfo: " + tagInfo);

#### \[h2\]connectTag(deprecated)

connectTag(): boolean;

Connects to this tag. Call this API to set up a connection before reading data from or writing data to a tag.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/91/v3/x4pkroNFQUaDKb4G3yddcQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062342Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=6D7DC1A67999AE8C2104C4D0EE3785C0CC04454B8F02D78D335D8115AA89F7BE)

This API is supported since API version 7 and deprecated since API version 9. Use [tagSession.connect](#connect9) instead.

**Required permissions**: ohos.permission.NFC\_TAG

**System capability**: SystemCapability.Communication.NFC.Tag

**Return value**

| **Type** | **Description** |
| :-- | :-- |
| boolean | Returns **true** if the operation is successful; returns **false** otherwise. |

**Example**

import { tag } from '@kit.ConnectivityKit';

// tagInfo is the object provided by the NFC service when allocating a tag. For details, see tag.TagInfo in @ohos.nfc.tag.
// getter API, which can be getIsoDep, getNdef, getMifareClassic, and so on.

let connectStatus : boolean = tag.getIsoDep(tagInfo).connectTag();
console.info("connectStatus: " + connectStatus);

#### \[h2\]connect9+

connect(): void;

Connects to this tag. Call this API to set up a connection before reading data from or writing data to a tag.

**Required permissions**: ohos.permission.NFC\_TAG

**System capability**: SystemCapability.Communication.NFC.Tag

**Atomic service API**: This API can be used in atomic services since API version 12.

**Error codes**

For details about the error codes, see [NFC Error Codes](../../../error-codes/nfc-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 201 | Permission denied. |
| 801 | Capability not supported. |
| 3100201 | The tag running state is abnormal in the service. |

**Example**

import { tag } from '@kit.ConnectivityKit';

// tagInfo is the object provided by the NFC service when allocating a tag. For details, see tag.TagInfo in @ohos.nfc.tag.
// getter API, which can be getIsoDep, getNdef, getMifareClassic, and so on.

try {
    tag.getIsoDep(tagInfo).connect();
    console.info("tag connect success");
} catch (businessError) {
    console.error("tag connect businessError: " + businessError);
}

#### \[h2\]reset()(deprecated)

reset(): void

Resets the connection to this tag.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9b/v3/IQRLU2RESv-bj3yNFyQawg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062342Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=AECB9CD02C4B26F5E538BFAF3F59E26AAE5A775C077833D196CDEC9117E90B9B)

This API is supported since API version 7 and deprecated since API version 9. Use [tagSession.resetConnection](#resetconnection9) instead.

**Required permissions**: ohos.permission.NFC\_TAG

**System capability**: SystemCapability.Communication.NFC.Tag

**Example**

import { tag } from '@kit.ConnectivityKit';

// tagInfo is the object provided by the NFC service when allocating a tag. For details, see tag.TagInfo in @ohos.nfc.tag.
// getter API, which can be getIsoDep, getNdef, getMifareClassic, and so on.

tag.getIsoDep(tagInfo).reset();

#### \[h2\]resetConnection()9+

resetConnection(): void

Resets the connection to this tag.

**Required permissions**: ohos.permission.NFC\_TAG

**System capability**: SystemCapability.Communication.NFC.Tag

**Atomic service API**: This API can be used in atomic services since API version 12.

**Error codes**

For details about the error codes, see [NFC Error Codes](../../../error-codes/nfc-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 201 | Permission denied. |
| 801 | Capability not supported. |
| 3100201 | The tag running state is abnormal in the service. |

**Example**

import { tag } from '@kit.ConnectivityKit';

// tagInfo is the object provided by the NFC service when allocating a tag. For details, see tag.TagInfo in @ohos.nfc.tag.
// getter API, which can be getIsoDep, getNdef, getMifareClassic, and so on.

try {
    tag.getIsoDep(tagInfo).resetConnection();
    console.info("tag resetConnection success");
} catch (businessError) {
    console.error("tag resetConnection businessError: " + businessError);
}

#### \[h2\]isTagConnected(deprecated)

isTagConnected(): boolean

Checks whether the tag is connected.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/25/v3/YLzqHByASwSiWUTgsAHx1A/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062342Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=9FBE12943F57A9F63C4636396169443422413CB039EE19D50C79BAF254D80B2A)

This API is supported since API version 7 and deprecated since API version 9. Use [tagSession.isConnected](#isconnected9) instead.

**System capability**: SystemCapability.Communication.NFC.Tag

**Return value**

| **Type** | **Description** |
| :-- | :-- |
| boolean | Returns **true** if the tag is connected; returns **false** otherwise. |

**Example**

import { tag } from '@kit.ConnectivityKit';

// tagInfo is the object provided by the NFC service when allocating a tag. For details, see tag.TagInfo in @ohos.nfc.tag.
// getter API, which can be getIsoDep, getNdef, getMifareClassic, and so on.

let isTagConnected = tag.getIsoDep(tagInfo).isTagConnected();
console.info("isTagConnected: " + isTagConnected);

#### \[h2\]isConnected9+

isConnected(): boolean

Checks whether the tag is connected. If you receive a message indicating that the tag has not been connected, call [tagSession.connect](#connect9) to connect the tag.

**System capability**: SystemCapability.Communication.NFC.Tag

**Atomic service API**: This API can be used in atomic services since API version 12.

**Return value**

| **Type** | **Description** |
| :-- | :-- |
| boolean | Returns **true** if the tag is connected; returns **false** otherwise. |

**Error codes**

For details about the error codes, see [NFC Error Codes](../../../error-codes/nfc-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 801 | Capability not supported. |

**Example**

import { tag } from '@kit.ConnectivityKit';

// tagInfo is the object provided by the NFC service when allocating a tag. For details, see tag.TagInfo in @ohos.nfc.tag.
// getter API, which can be getIsoDep, getNdef, getMifareClassic, and so on.

try {
    let isConnected = tag.getIsoDep(tagInfo).isConnected();
    console.info("tag isConnected = " + isConnected);
} catch (businessError) {
    console.error("tag isConnected businessError: " + businessError);
}

#### \[h2\]getMaxSendLength(deprecated)

getMaxSendLength(): number

Obtains the maximum length of the data that can be sent to this tag.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/28/v3/zfp--oniRjaAR4Kn1O8IKA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062342Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=EE319DA853C8944AB7B2C3180D5D4D75E2747B2896CCBECE3485823982A6D451)

This API is supported since API version 7 and deprecated since API version 9. Use [tagSession.getMaxTransmitSize](#getmaxtransmitsize9) instead.

**Required permissions**: ohos.permission.NFC\_TAG

**System capability**: SystemCapability.Communication.NFC.Tag

**Return value**

| **Type** | **Description** |
| :-- | :-- |
| number | Maximum data length obtained. The value cannot be a negative number. |

**Example**

import { tag } from '@kit.ConnectivityKit';

// tagInfo is the object provided by the NFC service when allocating a tag. For details, see tag.TagInfo in @ohos.nfc.tag.
// getter API, which can be getIsoDep, getNdef, getMifareClassic, and so on.

let maxSendLen = tag.getIsoDep(tagInfo).getMaxSendLength();
console.info("tag maxSendLen: " + maxSendLen);

#### \[h2\]getMaxTransmitSize9+

getMaxTransmitSize(): number

Obtains the maximum length of the data that can be sent to this tag.

**Required permissions**: ohos.permission.NFC\_TAG

**System capability**: SystemCapability.Communication.NFC.Tag

**Atomic service API**: This API can be used in atomic services since API version 12.

**Return value**

| **Type** | **Description** |
| :-- | :-- |
| number | Maximum data length obtained. The value cannot be a negative number. |

**Error codes**

For details about the error codes, see [NFC Error Codes](../../../error-codes/nfc-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 201 | Permission denied. |
| 801 | Capability not supported. |
| 3100201 | The tag running state is abnormal in the service. |

**Example**

import { tag } from '@kit.ConnectivityKit';

// tagInfo is the object provided by the NFC service when allocating a tag. For details, see tag.TagInfo in @ohos.nfc.tag.
// getter API, which can be getIsoDep, getNdef, getMifareClassic, and so on.

try {
    let maxTransmitSize = tag.getIsoDep(tagInfo).getMaxTransmitSize();
    console.info("tag maxTransmitSize = " + maxTransmitSize);
} catch (businessError) {
    console.error("tag getMaxTransmitSize businessError: " + businessError);
}

#### \[h2\]getSendDataTimeout(deprecated)

getSendDataTimeout(): number

Obtains the timeout period for sending data to this tag, in milliseconds.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1f/v3/yXwLDZYoSXqCpWaefYCcMw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062342Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=A6BA750B65565DD5130DC7ECFA269169F4474AFB0DAC0D9AB68B0106345ECE2E)

This API is supported since API version 7 and deprecated since API version 9. Use [tagSession.getTimeout](#gettimeout9) instead.

**Required permissions**: ohos.permission.NFC\_TAG

**System capability**: SystemCapability.Communication.NFC.Tag

**Return value**

| **Type** | **Description** |
| :-- | :-- |
| number | Timeout period obtained, in milliseconds. The value cannot be a negative number. |

**Example**

import { tag } from '@kit.ConnectivityKit';

// tagInfo is the object provided by the NFC service when allocating a tag. For details, see tag.TagInfo in @ohos.nfc.tag.
// getter API, which can be getIsoDep, getNdef, getMifareClassic, and so on.

let sendDataTimeout = tag.getIsoDep(tagInfo).getSendDataTimeout();
console.info("tag sendDataTimeout: " + sendDataTimeout);

#### \[h2\]getTimeout9+

getTimeout(): number

Obtains the timeout period for sending data to this tag, in milliseconds.

**Required permissions**: ohos.permission.NFC\_TAG

**System capability**: SystemCapability.Communication.NFC.Tag

**Atomic service API**: This API can be used in atomic services since API version 12.

**Return value**

| **Type** | **Description** |
| :-- | :-- |
| number | Timeout period obtained, in milliseconds. The value cannot be a negative number. |

**Error codes**

For details about the error codes, see [NFC Error Codes](../../../error-codes/nfc-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 201 | Permission denied. |
| 801 | Capability not supported. |
| 3100201 | The tag running state is abnormal in the service. |

**Example**

import { tag } from '@kit.ConnectivityKit';

// tagInfo is the object provided by the NFC service when allocating a tag. For details, see tag.TagInfo in @ohos.nfc.tag.
// getter API, which can be getIsoDep, getNdef, getMifareClassic, and so on.

try {
    let timeout = tag.getIsoDep(tagInfo).getTimeout();
    console.info("tag timeout = " + timeout);
} catch (businessError) {
    console.error("tag getTimeout businessError: " + businessError);
}

#### \[h2\]setSendDataTimeout(deprecated)

setSendDataTimeout(timeout: number): boolean

Sets the maximum time allowed for sending data to this tag, in ms.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/39/v3/WL6kJHx_Qjykg6x62TzV3g/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062342Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=885C95B904C60BA6F5F751B7B484B863CF677DB9E05327152B76DE3F53355FE3)

This API is supported since API version 7 and deprecated since API version 9. Use [tagSession.setTimeout](#settimeout9) instead.

**Required permissions**: ohos.permission.NFC\_TAG

**System capability**: SystemCapability.Communication.NFC.Tag

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| timeout | number | Yes | Timeout period to set, in milliseconds. The value cannot be a negative number. |

**Return value**

| **Type** | **Description** |
| :-- | :-- |
| boolean | Returns **true** if the timeout period is set successfully; returns **false** otherwise. |

**Example**

import { tag } from '@kit.ConnectivityKit';

// tagInfo is the object provided by the NFC service when allocating a tag. For details, see tag.TagInfo in @ohos.nfc.tag.
// getter API, which can be getIsoDep, getNdef, getMifareClassic, and so on.

let timeoutMs = 700; // Set the expected timeout interval.
let setStatus = tag.getIsoDep(tagInfo).setSendDataTimeout(timeoutMs);
console.info("tag setSendDataTimeout setStatus: " + setStatus);

#### \[h2\]setTimeout9+

setTimeout(timeout: number): void

Sets the maximum time allowed for sending data to this tag, in ms.

**Required permissions**: ohos.permission.NFC\_TAG

**System capability**: SystemCapability.Communication.NFC.Tag

**Atomic service API**: This API can be used in atomic services since API version 12.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| timeout | number | Yes | Timeout period to set, in milliseconds. The value cannot be a negative number. |

**Error codes**

For details about the error codes, see [NFC Error Codes](../../../error-codes/nfc-error-codes/document.md).

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
| 3100201 | The tag running state is abnormal in the service. |

**Example**

import { tag } from '@kit.ConnectivityKit';

// tagInfo is the object provided by the NFC service when allocating a tag. For details, see tag.TagInfo in @ohos.nfc.tag.
// getter API, which can be getIsoDep, getNdef, getMifareClassic, and so on.

let timeoutMs = 700; // Set the expected timeout interval.
try {
    tag.getIsoDep(tagInfo).setTimeout(timeoutMs);
    console.info("tag setTimeout success");
} catch (businessError) {
    console.error("tag setTimeout businessError: " + businessError);
}

#### \[h2\]sendData(deprecated)

sendData(data: number\[\]): Promise<number\[\]>

Sends data to the tag. This API uses a promise to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/70/v3/5JWEZ6Q5SL6-g7DSkb9uFQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062342Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=4DC4851138910CE011BFF2D0967C6E530403B1F4B484AD17BF3E11F49710319F)

This API is supported since API version 7 and deprecated since API version 9. Use [tagSession.transmit](#transmit9) instead.

**Required permissions**: ohos.permission.NFC\_TAG

**System capability**: SystemCapability.Communication.NFC.Tag

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| data | number\[\] | Yes | Data to send. The data consists of hexadecimal numbers ranging from **0x00** to **0xFF**. |

**Return value**

| **Type** | **Description** |
| :-- | :-- |
| Promise<number\[\]> | Promise used to return the response from the tag. The response consists of hexadecimal numbers ranging from **0x00** to **0xFF**. |

**Example**

import tag from '@kit.ConnectivityKit';
import { BusinessError } from '@ohos.base';

// tagInfo is the object provided by the NFC service when allocating a tag. For details, see tag.TagInfo in @ohos.nfc.tag.
// getter API, which can be getIsoDep, getNdef, getMifareClassic, and so on.

function tagSessionDemo() {
    // Connect the tag if it has not been connected.
    if (!tag.getIsoDep(tagInfo).isTagConnected()) {
        if (!tag.getIsoDep(tagInfo).connectTag()) {
            console.error("tagSession connectTag failed.");
            return;
        }
    }

    let cmdData = \[0x01, 0x02, 0x03, 0x04\]; // Set command data correctly.
    tag.getIsoDep(tagInfo).sendData(cmdData).then((response) => {
    console.info("tagSession sendData Promise response: " + response);
    }).catch((err : BusinessError)=> {
    console.error("tagSession sendData Promise err: " + err);
    });
}

#### \[h2\]sendData(deprecated)

sendData(data: number\[\], callback: AsyncCallback<number\[\]>): void

Sends data to the tag. This API uses an asynchronous callback to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/41/v3/jXiEYonPTnaWfrJd2wgJVw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062342Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=E2FD51830716468E09DCF1924E06F94A76C34DDC255917C876E2F724FBB3D68A)

This parameter is supported since API version 7 and deprecated since API version 9. Use [tagSession.transmit](#transmit9-1) instead.

**Required permissions**: ohos.permission.NFC\_TAG

**System capability**: SystemCapability.Communication.NFC.Tag

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| data | number\[\] | Yes | Data to send. The data consists of hexadecimal numbers ranging from **0x00** to **0xFF**. |
| callback | AsyncCallback<number\[\]> | Yes | Callback used to return the response from the tag. The response consists of hexadecimal numbers ranging from **0x00** to **0xFF**. |

**Example**

import { tag } from '@kit.ConnectivityKit';

// tagInfo is the object provided by the NFC service when allocating a tag. For details, see tag.TagInfo in @ohos.nfc.tag.
// getter API, which can be getIsoDep, getNdef, getMifareClassic, and so on.

function tagSessionDemo() {
    // Connect the tag if it has not been connected.
    if (!tag.getIsoDep(tagInfo).isTagConnected()) {
        if (!tag.getIsoDep(tagInfo).connectTag()) {
            console.error("tagSession connectTag failed.");
            return;
        }
    }

    let cmdData = \[0x01, 0x02, 0x03, 0x04\]; // Set command data correctly.
    tag.getIsoDep(tagInfo).sendData(cmdData, (err, response)=> {
        if (err) {
            console.error("tagSession sendData AsyncCallback err: " + err);
        } else {
            console.info("tagSession sendData AsyncCallback response: " + response);
        }
    });
}

#### \[h2\]transmit9+

transmit(data: number\[\]): Promise<number\[\]>

Sends data to the tag. This API uses a promise to return the result.

**Required permissions**: ohos.permission.NFC\_TAG

**System capability**: SystemCapability.Communication.NFC.Tag

**Atomic service API**: This API can be used in atomic services since API version 12.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| data | number\[\] | Yes | Data to send. The data consists of hexadecimal numbers ranging from **0x00** to **0xFF**. |

**Return value**

| **Type** | **Description** |
| :-- | :-- |
| Promise<number\[\]> | Promise used to return the response from the tag. The response consists of hexadecimal numbers ranging from **0x00** to **0xFF**. |

**Error codes**

For details about the error codes, see [NFC Error Codes](../../../error-codes/nfc-error-codes/document.md).

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
| 3100201 | The tag running state is abnormal in the service. |
| 3100204 | The tag I/O operation failed. |

**Example**

import { tag } from '@kit.ConnectivityKit';
import { BusinessError } from '@kit.BasicServicesKit';

// tagInfo is the object provided by the NFC service when allocating a tag. For details, see tag.TagInfo in @ohos.nfc.tag.
// getter API, which can be getIsoDep, getNdef, getMifareClassic, and so on.

function tagSessionDemo() {
// Connect the tag if it has not been connected.
    try {
        if (!tag.getIsoDep(tagInfo).isConnected()) {
            tag.getIsoDep(tagInfo).connect();
        }
    } catch (businessError) {
        console.error("tag connect businessError: " + businessError);
        return;
    }

    let cmdData = \[0x01, 0x02, 0x03, 0x04\]; // Set command data correctly.
    try {
    tag.getIsoDep(tagInfo).transmit(cmdData).then((response) => {
        console.info("tagSession transmit Promise response: " + response);
    }).catch((err : BusinessError)=> {
        console.error("tagSession transmit Promise err: " + err);
    });
    } catch (businessError) {
        console.error("tag transmit businessError: " + businessError);
        return;
    }
}

#### \[h2\]transmit9+

transmit(data: number\[\], callback: AsyncCallback<number\[\]>): void

Sends data to the tag. This API uses an asynchronous callback to return the result.

**Required permissions**: ohos.permission.NFC\_TAG

**System capability**: SystemCapability.Communication.NFC.Tag

**Atomic service API**: This API can be used in atomic services since API version 12.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| data | number\[\] | Yes | Data to send. The data consists of hexadecimal numbers ranging from **0x00** to **0xFF**. |
| callback | AsyncCallback<number\[\]> | Yes | Callback used to return the response from the tag. The response consists of hexadecimal numbers ranging from **0x00** to **0xFF**. |

**Error codes**

For details about the error codes, see [NFC Error Codes](../../../error-codes/nfc-error-codes/document.md).

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
| 3100201 | The tag running state is abnormal in the service. |
| 3100204 | The tag I/O operation failed.. |

**Example**

import { tag } from '@kit.ConnectivityKit';

// tagInfo is the object provided by the NFC service when allocating a tag. For details, see tag.TagInfo in @ohos.nfc.tag.
// getter API, which can be getIsoDep, getNdef, getMifareClassic, and so on.

function tagSessionDemo() {
    // Connect the tag if it has not been connected.
    try {
        if (!tag.getIsoDep(tagInfo).isConnected()) {
            tag.getIsoDep(tagInfo).connect();
        }
    } catch (businessError) {
        console.error("tag connect businessError: " + businessError);
        return;
    }

    let cmdData = \[0x01, 0x02, 0x03, 0x04\]; // Set command data correctly.
    try {
        tag.getIsoDep(tagInfo).transmit(cmdData, (err, response)=> {
            if (err) {
                console.error("tagSession transmit AsyncCallback err: " + err);
            } else {
                console.info("tagSession transmit AsyncCallback response: " + response);
            }
        });
    } catch (businessError) {
        console.error("tag transmit businessError: " + businessError);
        return;
    }
}
