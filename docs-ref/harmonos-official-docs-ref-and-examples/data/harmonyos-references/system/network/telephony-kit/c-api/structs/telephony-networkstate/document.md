# Telephony\_NetworkState

typedef struct {...} Telephony\_NetworkState

#### Overview

Defines network status information.

**Since**: 13

**Related module**: [Telephony](../../modules/telephony/document.md)

**Header file**: [telephony\_radio\_type.h](../../header-files/telephony-radio-type-h/document.md)

#### Summary

#### \[h2\]Member Variables

| Name | Description |
| :-- | :-- |
| char longOperatorName\_\[TELEPHONY\_MAX\_OPERATOR\_LEN\] | Long carrier name of the registered network. |
| char shortOperatorName\_\[TELEPHONY\_MAX\_OPERATOR\_LEN\] | Short carrier name of the registered network. |
| char plmnNumeric\_\[TELEPHONY\_MAX\_PLMN\_NUMERIC\_LEN\] | PLMN code of the registered network. |
| bool isRoaming\_ | Whether the user is roaming. |
| Telephony\_RegState regState\_ | Network registration status of the device. |
| Telephony\_RadioTechnology cfgTech\_ | RAT of the device. |
| Telephony\_NsaState nsaState\_ | NSA network registration status of the device. |
| bool isCaActive\_ | CA status. |
| bool isEmergency\_ | Whether only emergency calls are allowed. |
