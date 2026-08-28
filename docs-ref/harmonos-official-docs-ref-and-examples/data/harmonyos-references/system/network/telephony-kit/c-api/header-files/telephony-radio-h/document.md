# telephony\_radio.h

#### Overview

Defines C APIs for the radio module.

**File to include**: <telephony/core\_service/telephony\_radio.h>

**Library**: libtelephony\_radio.so

**System capability**: SystemCapability.Telephony.CoreService

**Since**: 13

**Related module**: [Telephony](../../modules/telephony/document.md)

#### Summary

#### \[h2\]Functions

| Name | Description |
| :-- | :-- |
| [Telephony\_RadioResult OH\_Telephony\_GetNetworkState(Telephony\_NetworkState \*state)](#oh_telephony_getnetworkstate) | Obtains the network status. |
| [Telephony\_RadioResult OH\_Telephony\_GetNetworkStateForSlot(int32\_t slotId, Telephony\_NetworkState \*state)](#oh_telephony_getnetworkstateforslot) | Obtains the network status of the SIM card in the specified slot. |

#### Function Description

#### \[h2\]OH\_Telephony\_GetNetworkState()

Telephony\_RadioResult OH\_Telephony\_GetNetworkState(Telephony\_NetworkState \*state)

**Description**

Obtains the network status.

**System capability**: SystemCapability.Telephony.CoreService

**Required permissions**: ohos.permission.GET\_NETWORK\_INFO

**Since**: 13

**Parameters**

| Name | Description |
| :-- | :-- |
| [Telephony\_NetworkState](../../structs/telephony-networkstate/document.md) \*state | Structure of the network status information received by the user. |

**Returns**

| Type | Description |
| :-- | :-- |
| [Telephony\_RadioResult](../telephony-radio-type-h/document.md#telephony_radioresult) | 
Result code. For details, see [Telephony\_RadioResult](../telephony-radio-type-h/document.md#telephony_radioresult).

[TEL\_RADIO\_SUCCESS](../telephony-radio-type-h/document.md#telephony_radioresult): Operation succeeded.

[TEL\_RADIO\_PERMISSION\_DENIED](../telephony-radio-type-h/document.md#telephony_radioresult): Permission denied.

[TEL\_RADIO\_ERR\_MARSHALLING\_FAILED](../telephony-radio-type-h/document.md#telephony_radioresult): Marshalling failed.

[TEL\_RADIO\_ERR\_SERVICE\_CONNECTION\_FAILED](../telephony-radio-type-h/document.md#telephony_radioresult): Telephony service connection failed.

[TEL\_RADIO\_ERR\_OPERATION\_FAILED](../telephony-radio-type-h/document.md#telephony_radioresult): Telephony service operation failed.

[TEL\_RADIO\_ERR\_INVALID\_PARAM](../telephony-radio-type-h/document.md#telephony_radioresult): Invalid parameter.

 |

#### \[h2\]OH\_Telephony\_GetNetworkStateForSlot()

Telephony\_RadioResult OH\_Telephony\_GetNetworkStateForSlot(int32\_t slotId, Telephony\_NetworkState \*state)

**Description**

Obtains the network status of the SIM card in the specified slot.

**System capability**: SystemCapability.Telephony.CoreService

**Required permissions**: ohos.permission.GET\_NETWORK\_INFO

**Since**: 13

**Parameters**

| Name | Description |
| :-- | :-- |
| int32\_t slotId | Card slot ID. |
| [Telephony\_NetworkState](../../structs/telephony-networkstate/document.md) \*state | Structure of the network status information received by the user. |

**Returns**

| Type | Description |
| :-- | :-- |
| [Telephony\_RadioResult](../telephony-radio-type-h/document.md#telephony_radioresult) | 
Result code. For details, see [Telephony\_RadioResult](../telephony-radio-type-h/document.md#telephony_radioresult).

[TEL\_RADIO\_SUCCESS](../telephony-radio-type-h/document.md#telephony_radioresult): Operation succeeded.

[TEL\_RADIO\_PERMISSION\_DENIED](../telephony-radio-type-h/document.md#telephony_radioresult): Permission denied.

[TEL\_RADIO\_ERR\_MARSHALLING\_FAILED](../telephony-radio-type-h/document.md#telephony_radioresult): Marshalling failed.

[TEL\_RADIO\_ERR\_SERVICE\_CONNECTION\_FAILED](../telephony-radio-type-h/document.md#telephony_radioresult): Telephony service connection failed.

[TEL\_RADIO\_ERR\_OPERATION\_FAILED](../telephony-radio-type-h/document.md#telephony_radioresult): Telephony service operation failed.

[TEL\_RADIO\_ERR\_INVALID\_PARAM](../telephony-radio-type-h/document.md#telephony_radioresult): Invalid parameter.

 |
