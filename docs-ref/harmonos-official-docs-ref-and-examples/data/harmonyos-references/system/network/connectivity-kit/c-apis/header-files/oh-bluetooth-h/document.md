# oh\_bluetooth.h

#### Overview

Defines the API for obtaining the Bluetooth switch state.

**File to include**: <ConnectivityKit/bluetooth/oh\_bluetooth.h>

**Library**: libbluetooth\_ndk.so

**System capability**: SystemCapability.Communication.Bluetooth.Core

**Since**: 13

**Related module**: [Bluetooth](../../modules/bluetooth/document.md)

#### Summary

#### \[h2\]Enums

| Name | typedef Keyword | Description |
| :-- | :-- | :-- |
| [Bluetooth\_SwitchState](#bluetooth_switchstate) | Bluetooth\_SwitchState | Enumerates the Bluetooth switch states. |
| [Bluetooth\_ResultCode](#bluetooth_resultcode) | Bluetooth\_ResultCode | Defines the Bluetooth return value. |

#### \[h2\]Functions

| Name | Description |
| :-- | :-- |
| [Bluetooth\_ResultCode OH\_Bluetooth\_GetBluetoothSwitchState(Bluetooth\_SwitchState \*state)](#oh_bluetooth_getbluetoothswitchstate) | Obtains the Bluetooth state. |

#### Enum Description

#### \[h2\]Bluetooth\_SwitchState

enum Bluetooth\_SwitchState

**Description**

Enumerates the Bluetooth switch states.

**Since**: 13

| Enum Item | Description |
| :-- | :-- |
| BLUETOOTH\_STATE\_OFF = 0 | Bluetooth is turned off. |
| BLUETOOTH\_STATE\_TURNING\_ON = 1 | Bluetooth is being turned on. |
| BLUETOOTH\_STATE\_ON = 2 | Bluetooth is turned on and ready for use. |
| BLUETOOTH\_STATE\_TURNING\_OFF = 3 | Bluetooth is being turned off. |
| BLUETOOTH\_STATE\_BLE\_TURNING\_ON = 4 | The BLE only mode is being turned on. |
| BLUETOOTH\_STATE\_BLE\_ON = 5 | The BLE only mode is turned on. |
| BLUETOOTH\_STATE\_BLE\_TURNING\_OFF = 6 | The BLE only mode is being turned off. |

#### \[h2\]Bluetooth\_ResultCode

enum Bluetooth\_ResultCode

**Description**

Defines the Bluetooth return value.

**Since**: 13

| Enum Item | Description |
| :-- | :-- |
| BLUETOOTH\_SUCCESS = 0 | Operation success. |
| BLUETOOTH\_INVALID\_PARAM = 401 | Invalid parameter. Possible causes: 1. The input parameter is a null pointer. 2. The parameter value exceeds the value range. |

#### Function Description

#### \[h2\]OH\_Bluetooth\_GetBluetoothSwitchState()

Bluetooth\_ResultCode OH\_Bluetooth\_GetBluetoothSwitchState(Bluetooth\_SwitchState \*state)

**Description**

Obtains the Bluetooth state.

**Since**: 13

**Parameters**

| Name | Description |
| :-- | :-- |
| [Bluetooth\_SwitchState](#bluetooth_switchstate) \*state | Pointer to the Bluetooth state obtained. A null pointer is prohibited. If a null pointer is passed in, an error is returned. For details, see [Bluetooth\_SwitchState](#bluetooth_switchstate). |

**Returns**

| Type | Description |
| :-- | :-- |
| [Bluetooth\_ResultCode](#bluetooth_resultcode) | 
Bluetooth switch state enumerated by [Bluetooth\_ResultCode](#bluetooth_resultcode).

The value can be:

[BLUETOOTH\_SUCCESS](#bluetooth_resultcode): The Bluetooth switch status is successfully obtained.

[BLUETOOTH\_INVALID\_PARAM](#bluetooth_resultcode): The input parameter is a null pointer.

 |
