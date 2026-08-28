# telephony\_radio\_type.h

#### Overview

Declares the structs for the C APIs of the radio module.

**File to include**: <telephony/core\_service/telephony\_radio\_type.h>

**Library**: libtelephony\_radio.so

**System capability**: SystemCapability.Telephony.CoreService

**Since**: 13

**Related module**: [Telephony](../../modules/telephony/document.md)

#### Summary

#### \[h2\]Structs

| Name | typedef Keyword | Description |
| :-- | :-- | :-- |
| [Telephony\_NetworkState](../../structs/telephony-networkstate/document.md) | Telephony\_NetworkState | Defines network status information. |

#### \[h2\]Enums

| Name | typedef Keyword | Description |
| :-- | :-- | :-- |
| [Telephony\_RadioResult](#telephony_radioresult) | Telephony\_RadioResult | Result codes. |
| [Telephony\_RegState](#telephony_regstate) | Telephony\_RegState | Network registration status of the device. |
| [Telephony\_RadioTechnology](#telephony_radiotechnology) | Telephony\_RadioTechnology | Radio access technology (RAT) type of the device. |
| [Telephony\_NsaState](#telephony_nsastate) | Telephony\_NsaState | NSA network registration status of the device. |

#### \[h2\]Macros

| Name | Description |
| :-- | :-- |
| [TELEPHONY\_MAX\_OPERATOR\_LEN 64](#) | 
Maximum length of the carrier name.

**Since**: 13

 |
| [TELEPHONY\_MAX\_PLMN\_NUMERIC\_LEN 6](#) | 

Maximum length of the PLMN.

**Since**: 13

 |

#### Enum Description

#### \[h2\]Telephony\_RadioResult

enum Telephony\_RadioResult

**Description**

Result codes.

**Since**: 13

| Enum Item | Description |
| :-- | :-- |
| TEL\_RADIO\_SUCCESS = 0 | Operation succeeded. |
| TEL\_RADIO\_PERMISSION\_DENIED = 201 | Permission denied. |
| TEL\_RADIO\_ERR\_INVALID\_PARAM = 401 | Invalid parameter. |
| TEL\_RADIO\_ERR\_MARSHALLING\_FAILED = 8300001 | Marshaling failed, which is a low-probability error. Try again later when this error occurs. |
| TEL\_RADIO\_ERR\_SERVICE\_CONNECTION\_FAILED = 8300002 | Connection error. Try again later when this error occurs. |
| TEL\_RADIO\_ERR\_OPERATION\_FAILED = 8300003 | Operation failed. Try again later when this error occurs. |

#### \[h2\]Telephony\_RegState

enum Telephony\_RegState

**Description**

Network registration status of the device.

**Since**: 13

| Enum Item | Description |
| :-- | :-- |
| TEL\_REG\_STATE\_NO\_SERVICE = 0 | The device cannot use any service. |
| TEL\_REG\_STATE\_IN\_SERVICE = 1 | The device can use services normally. |
| TEL\_REG\_STATE\_EMERGENCY\_CALL\_ONLY = 2 | The device can use only the emergency call service. |
| TEL\_REG\_STATE\_POWER\_OFF = 3 | The cellular radio service is disabled. |

#### \[h2\]Telephony\_RadioTechnology

enum Telephony\_RadioTechnology

**Description**

RAT type of the device.

**Since**: 13

| Enum Item | Description |
| :-- | :-- |
| TEL\_RADIO\_TECHNOLOGY\_UNKNOWN = 0 | Unknown RAT |
| TEL\_RADIO\_TECHNOLOGY\_GSM = 1 | Global System for Mobile Communication (GSM) |
| TEL\_RADIO\_TECHNOLOGY\_1XRTT = 2 | Single-Carrier Radio Transmission Technology (1XRTT) |
| TEL\_RADIO\_TECHNOLOGY\_WCDMA = 3 | Wideband Code Division Multiple Access (WCDMA) |
| TEL\_RADIO\_TECHNOLOGY\_HSPA = 4 | High Speed Packet Access (HSPA) |
| TEL\_RADIO\_TECHNOLOGY\_HSPAP = 5 | High Speed Packet Access Plus (HSPA+) |
| TEL\_RADIO\_TECHNOLOGY\_TD\_SCDMA = 6 | Time Division-Synchronous Code Division Multiple Access (TD-SCDMA) |
| TEL\_RADIO\_TECHNOLOGY\_EVDO = 7 | Evolution-Data Optimized (EVDO) |
| TEL\_RADIO\_TECHNOLOGY\_EHRPD = 8 | Evolved High Rate Package Data (EHRPD) |
| TEL\_RADIO\_TECHNOLOGY\_LTE = 9 | Long Term Evolution (LTE) |
| TEL\_RADIO\_TECHNOLOGY\_LTE\_CA = 10 | Long Term Evolution\_Carrier Aggregation (LTE\_CA) |
| TEL\_RADIO\_TECHNOLOGY\_IWLAN = 11 | Industrial Wireless LAN (IWLAN) |
| TEL\_RADIO\_TECHNOLOGY\_NR = 12 | New Radio (NR) |

#### \[h2\]Telephony\_NsaState

enum Telephony\_NsaState

**Description**

NSA network registration status of the device.

**Since**: 13

| Enum Item | Description |
| :-- | :-- |
| TEL\_NSA\_STATE\_NOT\_SUPPORTED = 1 | The device is in idle or connected state in an LTE cell that does not support NSA. |
| TEL\_NSA\_STATE\_NO\_DETECTED = 2 | The device is in the idle state in an LTE cell that supports NSA but not NR coverage detection. |
| TEL\_NSA\_STATE\_CONNECTED\_DETECTED = 3 | The device is connected to the LTE network in an LTE cell that supports NSA and NR coverage detection. |
| TEL\_NSA\_STATE\_IDLE\_DETECTED = 4 | The device is in the idle state in an LTE cell that supports NSA and NR coverage detection. |
| TEL\_NSA\_STATE\_DUAL\_CONNECTED = 5 | The device is connected to the LTE/NR network in an LTE cell that supports NSA. |
| TEL\_NSA\_STATE\_SA\_ATTACHED = 6 | The device is idle or connected to the NG-RAN cell when being attached to the 5G Core. |
