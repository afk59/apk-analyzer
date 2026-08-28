# @ohos.bluetooth.common (Bluetooth Common Module)

This module provides Bluetooth common APIs and parameter types. The first batch of APIs allow applications to specify the MAC address and address type of the target device when calling [connection.pairDevice](../ohos-bluetooth-connection-bluetooth-connection-module/document.md#connectionpairdevice21).

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4e/v3/S76gD4uhSOeATQDGFUB06w/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062341Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=3A3742807D24B23C7107181349D152C995D150A6FFCC8F4B8A95975D94DE3A62)

The initial APIs of this module are supported since API version 21. Newly added APIs will be marked with a superscript to indicate their earliest API version.

#### Modules to Import

import { common } from '@kit.ConnectivityKit';

#### BluetoothAddress

Defines the address information of a Bluetooth device, including the address and address type.

**System capability**: SystemCapability.Communication.Bluetooth.Core

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| address | string | No | No | Address of the Bluetooth device, for example, XX:XX:XX:XX:XX:XX. |
| addressType | [BluetoothAddressType](#bluetoothaddresstype) | No | No | Address type, which can be the actual or virtual MAC address of the Bluetooth device. |

#### BluetoothAddressType

Enumerate the address types of the Bluetooth device. The actual MAC address of a Bluetooth device is private information. During device discovery, the Bluetooth subsystem assigns a virtual MAC address to each Bluetooth device and saves the mapping between the virtual MAC address and the actual MAC address.

**System capability**: SystemCapability.Communication.Bluetooth.Core

| Name | Value | Description |
| :-- | :-- | :-- |
| VIRTUAL | 1 | Virtual MAC address. |
| REAL | 2 | Actual MAC address. |
