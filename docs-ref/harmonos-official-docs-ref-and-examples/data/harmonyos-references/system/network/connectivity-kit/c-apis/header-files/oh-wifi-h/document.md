# oh\_wifi.h

#### Overview

Defines APIs for obtaining Wi-Fi switch state.

**File to include**: <ConnectivityKit/wifi/oh\_wifi.h>

**Library**: libwifi\_ndk.so

**System capability**: SystemCapability.Communication.WiFi.STA

**Since**: 13

**Related module**: [Wifi](../../modules/wifi/document.md)

#### Summary

#### \[h2\]Enums

| Name | typedef Keyword | Description |
| :-- | :-- | :-- |
| [Wifi\_ResultCode](#wifi_resultcode) | Wifi\_ResultCode | Enumerates the error codes returned by Wi-Fi APIs. |

#### \[h2\]Functions

| Name | Description |
| :-- | :-- |
| [Wifi\_ResultCode OH\_Wifi\_IsWifiEnabled(bool \*enabled)](#oh_wifi_iswifienabled) | Checks whether Wi-Fi is enabled. |
| [Wifi\_ResultCode OH\_Wifi\_GetDeviceMACAddress(char \*macAddr, unsigned int \*macAddrLen)](#oh_wifi_getdevicemacaddress) | Obtains the actual MAC address of a device. |

#### Enum Description

#### \[h2\]Wifi\_ResultCode

enum Wifi\_ResultCode

**Description**

Enumerates the error codes returned by Wi-Fi APIs.

**Since**: 13

| Enum Item | Description |
| :-- | :-- |
| WIFI\_SUCCESS = 0 | Operation success. |
| WIFI\_PERMISSION\_DENIED = 201 | Permission verification fails. |
| WIFI\_INVALID\_PARAM = 401 | 
Invalid parameter.

Possible causes: 1. The input parameter is a null pointer. 2. The parameter value is out of the value range.

 |
| WIFI\_NOT\_SUPPORTED = 801 | Function not supported due to limited device capabilities. |
| WIFI\_OPERATION\_FAILED = 2501000 | 

Operation failed.

Possible cause: The internal execution of the service fails.

 |
| WIFI\_STA\_DISABLED = 2501001 | 

STA service not started.

Possible cause: Wi-Fi is disabled.

**Since**: 21

 |

#### Function Description

#### \[h2\]OH\_Wifi\_IsWifiEnabled()

Wifi\_ResultCode OH\_Wifi\_IsWifiEnabled(bool \*enabled)

**Description**

Checks whether Wi-Fi is enabled.

**Since**: 13

**Parameters**

| Name | Description |
| :-- | :-- |
| bool \*enabled | 
Pointer to the boolean value indicating the Wi-Fi state.

The value **true** indicates that Wi-Fi is enabled, and the value **false** indicates the opposite.

A null pointer is prohibited. If a null pointer is passed in, an error is returned.

 |

**Returns**

| Type | Description |
| :-- | :-- |
| [Wifi\_ResultCode](#wifi_resultcode) | 
Operation result, which is specified by [Wifi\_ResultCode](#wifi_resultcode). The value can be:

[WIFI\_SUCCESS](#wifi_resultcode): The Wi-Fi switch status is obtained successfully.

[WIFI\_INVALID\_PARAM](#wifi_resultcode): The input parameter is a null pointer.

[WIFI\_OPERATION\_FAILED](#wifi_resultcode): An internal error occurs during service execution.

 |

#### \[h2\]OH\_Wifi\_GetDeviceMACAddress()

Wifi\_ResultCode OH\_Wifi\_GetDeviceMACAddress(char \*macAddr, unsigned int \*macAddrLen)

**Description**

Obtains the actual MAC address of a device.

**Required permissions**: ohos.permission.GET\_WIFI\_LOCAL\_MAC and ohos.permission.GET\_WIFI\_INFO

**Since**: 21

**Parameters**

| Name | Description |
| :-- | :-- |
| char \*macAddr | Character array of the device MAC address, which ends with '\\0'. |
| unsigned int \*macAddrLen | Memory size allocated to **macAddr**. |

**Returns**

| Type | Description |
| :-- | :-- |
| [Wifi\_ResultCode](#wifi_resultcode) | 
Operation result, which is specified by [Wifi\_ResultCode](#wifi_resultcode). The value can be:

[WIFI\_SUCCESS](#wifi_resultcode): The MAC address of the device is obtained successfully.

[WIFI\_PERMISSION\_DENIED](#wifi_resultcode): The permission is denied.

[WIFI\_NOT\_SUPPORTED](#wifi_resultcode): This capability is not supported.

[WIFI\_INVALID\_PARAM](#wifi_resultcode): The input **macAddr** is a null pointer.

[WIFI\_OPERATION\_FAILED](#wifi_resultcode): An internal error occurs during internal execution.

[WIFI\_STA\_DISABLED](#wifi_resultcode): The Wi-Fi STA mode is disabled.

 |
