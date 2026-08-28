# @ohos.bluetooth.constant (Bluetooth constant Module)

The **constant** module provides constant definitions related to Bluetooth [profiles](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/terminology#profile) and device types.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/43/v3/di3IcKkhRXO5m6pZZCY4AA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062341Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=0CC4D9C6801116CCC9DB14C15BFCF793C1ADBB65D052F77ACFC0264BC84F32B7)

The initial APIs of this module are supported since API version 10. Newly added APIs will be marked with a superscript to indicate their earliest API version.

#### Modules to Import

import { constant } from '@kit.ConnectivityKit';

#### ProfileId

Enumerates the Bluetooth [profile](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/terminology#profile) IDs.

**System capability**: SystemCapability.Communication.Bluetooth.Core

| Name | Value | Description |
| :-- | :-- | :-- |
| PROFILE\_A2DP\_SOURCE | 1 | [A2DP source](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/terminology#a2dp-source) profile, which is used to send audio data. |
| PROFILE\_HANDSFREE\_AUDIO\_GATEWAY | 4 | [HFP AG](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/terminology#hfp-ag) profile, which is used to send call audio data. |
| PROFILE\_HID\_HOST | 6 | [HID host](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/terminology#hid-host) profile, which is used to establish communication with the [HID device](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/terminology#hid-device) and exchange data. |
| PROFILE\_PAN\_NETWORK | 7 | [NAP](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/terminology#nap) profile, which is used to implement network sharing. |

#### ProfileConnectionState

Enumerates the states of the profile connection between the local and peer Bluetooth devices.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Communication.Bluetooth.Core

| Name | Value | Description |
| :-- | :-- | :-- |
| STATE\_DISCONNECTED | 0 | The profile connection is disconnected. |
| STATE\_CONNECTING | 1 | The profile connection is being established. |
| STATE\_CONNECTED | 2 | The profile connection is established. |
| STATE\_DISCONNECTING | 3 | The profile connection is being disconnected. |

#### MajorClass

Enumerates the types of Bluetooth devices. This is a standard field in the Bluetooth protocol.

**System capability**: SystemCapability.Communication.Bluetooth.Core

| Name | Value | Description |
| :-- | :-- | :-- |
| MAJOR\_MISC | 0x0000 | Miscellaneous device, which that does not belong to any standard category. |
| MAJOR\_COMPUTER | 0x0100 | Computer. |
| MAJOR\_PHONE | 0x0200 | Mobile phone. |
| MAJOR\_NETWORKING | 0x0300 | LAN or network access point. |
| MAJOR\_AUDIO\_VIDEO | 0x0400 | Audio or video device. |
| MAJOR\_PERIPHERAL | 0x0500 | Peripheral device. |
| MAJOR\_IMAGING | 0x0600 | Imaging device. |
| MAJOR\_WEARABLE | 0x0700 | Wearable device. |
| MAJOR\_TOY | 0x0800 | Toy. |
| MAJOR\_HEALTH | 0x0900 | Health device. |
| MAJOR\_UNCATEGORIZED | 0x1F00 | Unclassified device. |

#### MajorMinorClass

Enumerates the Bluetooth device subclasses, which are further subdivided based on [MajorClass](#majorclass). This is a standard field in the Bluetooth protocol.

**System capability**: SystemCapability.Communication.Bluetooth.Core

| Name | Value | Description |
| :-- | :-- | :-- |
| COMPUTER\_UNCATEGORIZED | 0x0100 | Unclassified computer. |
| COMPUTER\_DESKTOP | 0x0104 | Desktop computer. |
| COMPUTER\_SERVER | 0x0108 | Server. |
| COMPUTER\_LAPTOP | 0x010C | Laptop. |
| COMPUTER\_HANDHELD\_PC\_PDA | 0x0110 | Hand-held computer. |
| COMPUTER\_PALM\_SIZE\_PC\_PDA | 0x0114 | Palmtop computer. |
| COMPUTER\_WEARABLE | 0x0118 | Wearable computer. |
| COMPUTER\_TABLET | 0x011C | Tablet. |
| PHONE\_UNCATEGORIZED | 0x0200 | Unclassified mobile phone. |
| PHONE\_CELLULAR | 0x0204 | Portable phone. |
| PHONE\_CORDLESS | 0x0208 | Cordless phone. |
| PHONE\_SMART | 0x020C | Smartphone. |
| PHONE\_MODEM\_OR\_GATEWAY | 0x0210 | Modem or gateway phone. |
| PHONE\_ISDN | 0x0214 | ISDN phone. |
| NETWORK\_FULLY\_AVAILABLE | 0x0300 | Network device with a network load of 0%. |
| NETWORK\_1\_TO\_17\_UTILIZED | 0x0320 | Network device with a network load of 1% to 17%. |
| NETWORK\_17\_TO\_33\_UTILIZED | 0x0340 | Network device with a network load of 17% to 33%. |
| NETWORK\_33\_TO\_50\_UTILIZED | 0x0360 | Network device with a network load of 33% to 50%. |
| NETWORK\_60\_TO\_67\_UTILIZED | 0x0380 | Network device with a network load of 60% to 67%. |
| NETWORK\_67\_TO\_83\_UTILIZED | 0x03A0 | Network device with a network load of 67% to 83%. |
| NETWORK\_83\_TO\_99\_UTILIZED | 0x03C0 | Network device with a network load of 83% to 99%. |
| NETWORK\_NO\_SERVICE | 0x03E0 | Network device with a network load of 100%. |
| AUDIO\_VIDEO\_UNCATEGORIZED | 0x0400 | Unclassified audio or video device. |
| AUDIO\_VIDEO\_WEARABLE\_HEADSET | 0x0404 | Wearable audio or video headset. |
| AUDIO\_VIDEO\_HANDSFREE | 0x0408 | Hands-free audio or video device. |
| AUDIO\_VIDEO\_MICROPHONE | 0x0410 | Audio or video microphone. |
| AUDIO\_VIDEO\_LOUDSPEAKER | 0x0414 | Audio or video loudspeaker. |
| AUDIO\_VIDEO\_HEADPHONES | 0x0418 | Audio or video headphones. |
| AUDIO\_VIDEO\_PORTABLE\_AUDIO | 0x041C | Portable audio or video device. |
| AUDIO\_VIDEO\_CAR\_AUDIO | 0x0420 | In-vehicle audio or video device. |
| AUDIO\_VIDEO\_SET\_TOP\_BOX | 0x0424 | Audio or video STB device. |
| AUDIO\_VIDEO\_HIFI\_AUDIO | 0x0428 | High-fidelity audio or video device. |
| AUDIO\_VIDEO\_VCR | 0x042C | Video cassette recording (VCR) device. |
| AUDIO\_VIDEO\_VIDEO\_CAMERA | 0x0430 | Video camera. |
| AUDIO\_VIDEO\_CAMCORDER | 0x0434 | Camcorder. |
| AUDIO\_VIDEO\_VIDEO\_MONITOR | 0x0438 | Video monitor. |
| AUDIO\_VIDEO\_VIDEO\_DISPLAY\_AND\_LOUDSPEAKER | 0x043C | Video device with a display and speaker. |
| AUDIO\_VIDEO\_VIDEO\_CONFERENCING | 0x0440 | Video conference device. |
| AUDIO\_VIDEO\_VIDEO\_GAMING\_TOY | 0x0448 | Video gaming toy. |
| PERIPHERAL\_NON\_KEYBOARD\_NON\_POINTING | 0x0500 | Non-keyboard or non-pointing peripheral device. |
| PERIPHERAL\_KEYBOARD | 0x0540 | Keyboard device. |
| PERIPHERAL\_POINTING\_DEVICE | 0x0580 | Pointing peripheral device. |
| PERIPHERAL\_KEYBOARD\_POINTING | 0x05C0 | Keyboard pointing device. |
| PERIPHERAL\_UNCATEGORIZED | 0x0500 | Unclassified peripheral device. |
| PERIPHERAL\_JOYSTICK | 0x0504 | Peripheral joystick. |
| PERIPHERAL\_GAMEPAD | 0x0508 | Peripheral game pad |
| PERIPHERAL\_REMOTE\_CONTROL | 0x05C0 | Peripheral remote control device |
| PERIPHERAL\_SENSING\_DEVICE | 0x0510 | Peripheral sensing device. |
| PERIPHERAL\_DIGITIZER\_TABLET | 0x0514 | Peripheral digitizer tablet. |
| PERIPHERAL\_CARD\_READER | 0x0518 | Peripheral card reader. |
| PERIPHERAL\_DIGITAL\_PEN | 0x051C | Peripheral digital pen. |
| PERIPHERAL\_SCANNER\_RFID | 0x0520 | Peripheral RFID scanner. |
| PERIPHERAL\_GESTURAL\_INPUT | 0x0522 | Gesture input device. |
| IMAGING\_UNCATEGORIZED | 0x0600 | Unclassified imaging device. |
| IMAGING\_DISPLAY | 0x0610 | Imaging display device. |
| IMAGING\_CAMERA | 0x0620 | Imaging camera device. |
| IMAGING\_SCANNER | 0x0640 | Imaging scanner. |
| IMAGING\_PRINTER | 0x0680 | Imaging printer. |
| WEARABLE\_UNCATEGORIZED | 0x0700 | Unclassified wearable device. |
| WEARABLE\_WRIST\_WATCH | 0x0704 | Smart watch. |
| WEARABLE\_PAGER | 0x0708 | Wearable pager. |
| WEARABLE\_JACKET | 0x070C | Wearable jacket. |
| WEARABLE\_HELMET | 0x0710 | Wearable helmet. |
| WEARABLE\_GLASSES | 0x0714 | Wearable glasses. |
| TOY\_UNCATEGORIZED | 0x0800 | Unclassified toy. |
| TOY\_ROBOT | 0x0804 | Toy robot. |
| TOY\_VEHICLE | 0x0808 | Toy vehicle. |
| TOY\_DOLL\_ACTION\_FIGURE | 0x080C | Humanoid toy doll. |
| TOY\_CONTROLLER | 0x0810 | Toy controller. |
| TOY\_GAME | 0x0814 | Toy gaming device. |
| HEALTH\_UNCATEGORIZED | 0x0900 | Unclassified health devices. |
| HEALTH\_BLOOD\_PRESSURE | 0x0904 | Blood pressure device. |
| HEALTH\_THERMOMETER | 0x0908 | Thermometer |
| HEALTH\_WEIGHING | 0x090C | Body scale. |
| HEALTH\_GLUCOSE | 0x0910 | Blood glucose monitor. |
| HEALTH\_PULSE\_OXIMETER | 0x0914 | Pulse oximeter. |
| HEALTH\_PULSE\_RATE | 0x0918 | Heart rate monitor. |
| HEALTH\_DATA\_DISPLAY | 0x091C | Health data display. |
| HEALTH\_STEP\_COUNTER | 0x0920 | Step counter. |
| HEALTH\_BODY\_COMPOSITION\_ANALYZER | 0x0924 | Body composition analyzer. |
| HEALTH\_PEAK\_FLOW\_MONITOR | 0x0928 | Hygrometer. |
| HEALTH\_MEDICATION\_MONITOR | 0x092C | Medication monitor. |
| HEALTH\_KNEE\_PROSTHESIS | 0x0930 | Prosthetic knee. |
| HEALTH\_ANKLE\_PROSTHESIS | 0x0934 | Prosthetic ankle. |
| HEALTH\_GENERIC\_HEALTH\_MANAGER | 0x0938 | Generic health management device. |
| HEALTH\_PERSONAL\_MOBILITY\_DEVICE | 0x093C | Personal mobility device. |

#### ProfileUuids12+

Enumerates the [Universally Unique Identifiers (UUIDs)](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/terminology#uuid) of Bluetooth profiles, which are defined by [Bluetooth Special Interest Group](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/terminology#bluetooth-sig).

**System capability**: SystemCapability.Communication.Bluetooth.Core

| Name | Value | Description |
| :-- | :-- | :-- |
| PROFILE\_UUID\_HFP\_AG | '0000111F-0000-1000-8000-00805F9B34FB' | Hands-free audio gateway profile. |
| PROFILE\_UUID\_HFP\_HF | '0000111E-0000-1000-8000-00805F9B34FB' | Hands-free profile. |
| PROFILE\_UUID\_HSP\_AG | '00001112-0000-1000-8000-00805F9B34FB' | Headset audio gateway profile. |
| PROFILE\_UUID\_HSP\_HS | '00001108-0000-1000-8000-00805F9B34FB' | Headset profile. |
| PROFILE\_UUID\_A2DP\_SRC | '0000110A-0000-1000-8000-00805F9B34FB' | A2DP source profile. |
| PROFILE\_UUID\_A2DP\_SINK | '0000110B-0000-1000-8000-00805F9B34FB' | A2DP sink profile. |
| PROFILE\_UUID\_AVRCP\_CT | '0000110E-0000-1000-8000-00805F9B34FB' | AVRCP controller profile. |
| PROFILE\_UUID\_AVRCP\_TG | '0000110C-0000-1000-8000-00805F9B34FB' | AVRCP target profile. |
| PROFILE\_UUID\_HID | '00001124-0000-1000-8000-00805F9B34FB' | HID profile. |
| PROFILE\_UUID\_HOGP | '00001812-0000-1000-8000-00805F9B34FB' | HID over GATT profile. |
